# Adaptive Physique Coach

An adaptive coaching skill for strength, physique, general fitness and any cardio, using Google Drive, MacroFactor, Google Health and Strava. Packaged for Claude web, eligible ChatGPT Work web workspaces, and Codex.

This is a fork of [mprecilio20/adaptive-endurance-coach](https://github.com/mprecilio20/adaptive-endurance-coach). The original review-and-adjust approach is retained, with goals and data handling adapted to general fitness. The original endurance skill and documentation are preserved under [upstream](upstream/README.md); they are outside the active skills directory. The original MIT license and copyright notice are retained.

## Install on the Web

Download the appropriate asset from [release v1.0.0](https://github.com/MikeDoesStuff/adaptive-physique-coach/releases/tag/v1.0.0), not GitHub's whole-repository source ZIP. Both upload packages contain the same skill and its references, an empty optional log, and the MIT notice. Neither contains personal health data, credentials, executable runtime scripts, local MCP servers or desktop-only dependencies.

### Claude Web

1. Download [adaptive-physique-coach-skill-v1.0.0.zip](https://github.com/MikeDoesStuff/adaptive-physique-coach/releases/download/v1.0.0/adaptive-physique-coach-skill-v1.0.0.zip).
2. Enable Code execution and file creation in Settings > Capabilities, subject to your organization's policy.
3. Open Customize > Skills > + > + Create skill > Upload a skill. Upload the ZIP without extracting it, then enable the skill.

The ZIP has a single top-level `adaptive-physique-coach/` folder containing `SKILL.md`. Its name matches the metadata, and its description is below Claude's documented 200-character limit. [Claude installation guidance](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [custom-skill packaging guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### ChatGPT Work Web

For an eligible workspace with personal skill uploads enabled, open Plugins > Skills > Create > Upload from your computer. Use the single-skill ZIP above if the picker accepts ZIP archives. OpenAI documents skill uploading but does not specify the accepted archive layout in its web help article. [ChatGPT skills guidance](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

For the explicitly documented plugin ZIP upload route:

1. Download [adaptive-physique-coach-chatgpt-plugin-v1.0.0.zip](https://github.com/MikeDoesStuff/adaptive-physique-coach/releases/download/v1.0.0/adaptive-physique-coach-chatgpt-plugin-v1.0.0.zip).
2. With eligible upload access, open the Admin console, select the intended ChatGPT workspace, then Plugins > Add > Upload plugin.
3. Review and install the uploaded plugin as offered by your workspace. Use it in Work, selecting or mentioning the plugin when needed.

This is a skills-only portable plugin with `plugin.json` at the archive root and the skill under `skills/adaptive-physique-coach/`. Plugin and skill availability depend on your plan, role, workspace settings and rollout; a package cannot bypass those restrictions. [ChatGPT plugin upload guidance](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt), [portable plugin format](https://developers.openai.com/plugins/build/plugins).

Connect Google Drive separately in the chosen client, or attach the required exports. Skill installation does not authorize data access, automatically sync records, or connect Google Health Coach. Use an available authorized Coach route or return its answer to a focused query. Installing in one client does not automatically install in another.

### Codex and Prompt Fallback

Load [skills/adaptive-physique-coach](skills/adaptive-physique-coach/SKILL.md) through your client's supported skill mechanism. For a chat or project environment without native skill uploads, the [standalone prompt](skills/adaptive-physique-coach/references/work-prompt.md) is an alternative, not a native skill installation.

## Use

Example request:

> Review my last complete training week using my Drive training repository. Check lifting progress, nutrition and recovery, and adapt whichever cardio I have been doing. Use older records only for relevant comparisons. Return the smallest justified changes and a compact dated review.

No TrainingPeaks, custom parser or MacroFactor API is required. The skill provides instructions, not data connections or a background service. Tool access, file analysis and persistence depend on the client.

## Data and Review

- Google Drive remains the durable repository. Follow its guide and existing folder structure.
- MacroFactor completed-set exports provide lifting evidence; its full export can include nutrition/body data, programmes and summaries. MacroFactor Nutrition remains the calorie-adjustment authority.
- Google Health and Strava normally supply cardio. Reconcile automatically synced activities rather than double-counting them. Occasional MacroFactor cardio entries are supported.
- Google Health Coach can provide focused recent or historical metric summaries through an available app route or a user-returned answer. Preserve dates, units, coverage and AI-summary provenance.
- Any cardio modality is supported through session purpose, duration, effort, movement demands and recovery. Machine-specific examples do not constrain activity choice.
- A compact current brief and bounded recent analysis keep reviews focused. Targeted historical lookups support progress comparisons, preferences, previous programmes and earlier decisions.

Reviews prepare a dated decision record. Saving requires existing authorization and working tools, with successful readback before persistence is claimed. Original exports and historical snapshots are preserved.

The optional [cardio session log](skills/adaptive-physique-coach/assets/cardio-session-log.csv) captures details missing from existing records. It is a supplement, not a second mandatory logging system.

## Structure

```text
plugin.json
scripts/
  package_skill.py
  test_package_skill.py
skills/adaptive-physique-coach/
  SKILL.md
  references/
    context-and-history.md
    data-sources.md
    general-cardio.md
    google-health-coach.md
    strength-nutrition-recovery.md
    work-prompt.md
  assets/
    cardio-session-log.csv
upstream/
  README.md
  AGENT.md
  skills/adaptive-endurance-coach/
```

## Build and Verification

Maintainers can rebuild the release assets with Python 3 (standard library only):

```sh
python -m unittest discover -s scripts -p "test_*.py"
python scripts/package_skill.py
```

Generated ZIPs and `SHA256SUMS.txt` are written to ignored `dist/`. The builder uses an explicit file allowlist and refuses to distribute a populated cardio log. Tests verify archive layouts, matching manifests, bundled license, internal reference links, exclusion of non-package files and reproducible output for identical source bytes. The build helper is not included in either upload package.

The archives are structurally validated against the documented formats. Actual import, platform scanning, skill invocation and Drive access in a specific web account still require testing after upload. These packages are not represented as marketplace-approved or already installed.

This repository contains reusable instructions and an empty optional log template. Personal training exports, health data, private Drive links and coaching records belong in the user's own repository, not in this public fork. Coaching analysis does not replace medical assessment of concerning symptoms.
