# Agent Guidance

Use [Adaptive Physique Coach](skills/adaptive-physique-coach/SKILL.md) for the active workflow. Read its relevant references before making coaching decisions.

## Setup and Capabilities

Identify the client's actual skill-loading, Drive/file-read, spreadsheet analysis and write capabilities. Load the self-contained skill folder where supported, or use its [standalone prompt](skills/adaptive-physique-coach/references/work-prompt.md). Do not install TrainingPeaks or execute archived upstream setup for this adaptation.

The instructions do not supply app credentials, a MacroFactor API, a live Google Health Coach connection, automatic sync or scheduled execution. Use available authenticated tools and report capability gaps. Ask for only the missing data needed for the current question.

## Data Scope

The user's training repository guide establishes source locations. Keep personal data and source exports outside this code repository. Prefer current source manifests and bounded date/exercise slices. Use [Context and History](skills/adaptive-physique-coach/references/context-and-history.md) for targeted progress, preference and programme lookups rather than loading all history.

Google Health and Strava normally supply cardio; synced copies represent one activity. MacroFactor supplies lifting and nutrition/body context, with occasional cardio. Use [Google Health Coach](skills/adaptive-physique-coach/references/google-health-coach.md) for focused metric queries when available. Support any cardio according to purpose, effort and recovery demands.

## Changes and Verification

Preserve original exports, historical snapshots and unrelated user work. Persist dated coaching records only within the user's authorization and verify writes. Do not claim current readiness from stale data or a workout outcome from a proposal.

When editing this skill, verify YAML frontmatter, relative links, self-contained distribution and the standalone prompt's consistency with core rules. Review scenarios involving synced cardio duplicates, incomplete nutrition, unfamiliar activities, stale programmes and targeted historical lookup. Structural validation alone does not prove coaching quality or client integration.

For web distribution, run `python -m unittest discover -s scripts -p "test_*.py"` and `python scripts/package_skill.py`. Keep the skill metadata within Claude's name/description limits. The standalone ZIP has one skill folder; the ChatGPT plugin ZIP has root `plugin.json` and `skills/`. Distribute only release assets built from the allowlist, with the MIT notice; never bundle source exports or a populated log. The build helper is not a runtime dependency. Document account prerequisites and distinguish local validation from successful web installation.

Upstream source and license are preserved for attribution. The archived endurance skill is not part of the default active skill package.
