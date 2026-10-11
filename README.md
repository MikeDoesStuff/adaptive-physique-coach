# Adaptive Physique Coach

An adaptive coaching skill for strength, physique, general fitness and any cardio, using Google Drive, MacroFactor, Google Health and Strava. Designed for ChatGPT Work, Codex, and other clients that can use the instructions and access the relevant data.

This is a fork of [mprecilio20/adaptive-endurance-coach](https://github.com/mprecilio20/adaptive-endurance-coach). The original review-and-adjust approach is retained, with goals and data handling adapted to general fitness. The original endurance skill and documentation are preserved under [upstream](upstream/README.md); they are outside the active skills directory. The original MIT license and copyright notice are retained.

## Use

Load [skills/adaptive-physique-coach](skills/adaptive-physique-coach/SKILL.md) through your client's supported skill mechanism. The folder is self-contained. For a chat or project workflow, use the [standalone prompt](skills/adaptive-physique-coach/references/work-prompt.md) with accessible source files or an available Drive connection.

Example request:

> Review my last complete training week using my Drive training repository. Check lifting progress, nutrition and recovery, and adapt whichever cardio I have been doing. Use older records only for relevant comparisons. Return the smallest justified changes and a compact dated review.

No TrainingPeaks, custom parser or MacroFactor API is required. The skill provides instructions, not data connections or a background service. Tool access, skill installation, file analysis and persistence depend on the client. [ChatGPT Work guidance](https://learn.chatgpt.com/docs/get-started-with-work), [skill distribution guidance](https://learn.chatgpt.com/docs/enterprise/skills).

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

This repository contains reusable instructions and an empty optional log template. Personal training exports, health data, private Drive links and coaching records belong in the user's own repository, not in this public fork. Coaching analysis does not replace medical assessment of concerning symptoms.
