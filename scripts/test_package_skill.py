import json
from pathlib import Path
import posixpath
import re
import shutil
import tempfile
import unittest
from urllib.parse import urlsplit
import zipfile

from package_skill import NAME, ROOT, SKILL_FILES, build


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in ("plugin.json", "LICENSE"):
            shutil.copyfile(ROOT / relative, self.root / relative)
        for relative in SKILL_FILES:
            target = self.root / "skills" / NAME / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / "skills" / NAME / relative, target)

    def test_layout_content_links_and_reproducibility(self):
        private = self.root / "skills" / NAME / "private-export.csv"
        private.write_text("must not ship", encoding="utf-8")
        archives = build(self.root)
        original = [path.read_bytes() for path in archives]
        self.assertEqual(original, [path.read_bytes() for path in build(self.root)])
        for path in archives:
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                prefix = f"{NAME}/" if "-skill-" in path.name else f"skills/{NAME}/"
                expected = {prefix + relative for relative in (*SKILL_FILES, "LICENSE.txt")}
                if "-chatgpt-plugin-" in path.name:
                    expected |= {"plugin.json", "LICENSE"}
                    self.assertEqual(json.loads(archive.read("plugin.json"))["name"], NAME)
                self.assertEqual(names, expected)
                self.assertIsNone(archive.testzip())
                self.assertEqual(archive.read(prefix + "LICENSE.txt"), (self.root / "LICENSE").read_bytes())
                for name in sorted(names):
                    if not name.endswith(".md"):
                        continue
                    document = archive.read(name).decode("utf-8")
                    for link in re.findall(r"\]\(([^)]+)\)", document):
                        url = urlsplit(link)
                        if url.scheme or not url.path:
                            continue
                        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), url.path))
                        self.assertTrue(target.startswith(prefix), (name, link))
                        self.assertIn(target, names, (name, link))

    def test_populated_cardio_log_is_rejected(self):
        path = self.root / "skills" / NAME / "assets/cardio-session-log.csv"
        with path.open("a", encoding="utf-8") as log:
            log.write("private,session\n")
        with self.assertRaisesRegex(ValueError, "only its header"):
            build(self.root)

    def test_mismatched_name_is_rejected(self):
        path = self.root / "plugin.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["name"] = "wrong-skill"
        path.write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "must match"):
            build(self.root)


if __name__ == "__main__":
    unittest.main()
