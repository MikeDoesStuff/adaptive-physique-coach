"""Build self-contained web upload packages; not needed to use the skill."""

import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAME = "adaptive-physique-coach"
SKILL_FILES = (
    "SKILL.md",
    "references/context-and-history.md",
    "references/data-sources.md",
    "references/general-cardio.md",
    "references/google-health-coach.md",
    "references/strength-nutrition-recovery.md",
    "references/work-prompt.md",
    "assets/cardio-session-log.csv",
)


def package_entries(root):
    manifest_path = root / "plugin.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["name"] != NAME:
        raise ValueError("Plugin name must match the packaged skill")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
        raise ValueError("Release version must be major.minor.patch")

    skill_root = root / "skills" / NAME
    # An explicit allowlist keeps exports, private records and upstream out.
    skill_entries = {}
    for relative in SKILL_FILES:
        path = skill_root / relative
        if path.resolve() != skill_root.resolve() / relative or path.is_symlink():
            raise ValueError(f"Skill file must not redirect outside its folder: {relative}")
        skill_entries[relative] = path.read_bytes()
    with (skill_root / "assets/cardio-session-log.csv").open(
        encoding="utf-8-sig", newline=""
    ) as source:
        if len(list(csv.reader(source))) != 1:
            raise ValueError("The distributed cardio log must contain only its header")

    license_data = (root / "LICENSE").read_bytes()
    skill_entries["LICENSE.txt"] = license_data
    standalone = {f"{NAME}/{key}": value for key, value in skill_entries.items()}
    plugin = {f"skills/{NAME}/{key}": value for key, value in skill_entries.items()}
    plugin["plugin.json"] = manifest_path.read_bytes()
    plugin["LICENSE"] = license_data
    return manifest["version"], standalone, plugin


def write_archive(path, entries):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(entries.items()):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content)
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None or set(archive.namelist()) != set(entries):
            raise ValueError(f"Archive verification failed: {path.name}")


def build(root=ROOT):
    version, standalone, plugin = package_entries(root)
    output = root / "dist"
    output.mkdir(exist_ok=True)
    archives = []
    for kind, entries in (("skill", standalone), ("chatgpt-plugin", plugin)):
        path = output / f"{NAME}-{kind}-v{version}.zip"
        write_archive(path, entries)
        archives.append(path)
    checksums = "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
        for path in archives
    )
    (output / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8")
    return archives


if __name__ == "__main__":
    for archive in build():
        print(f"Verified {archive.name} ({archive.stat().st_size} bytes)")
