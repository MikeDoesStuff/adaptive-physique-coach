# Context and History

## Current First

Start by stating the decision to be made. Use three layers:

1. A compact current brief: confirmed goals/preferences, current programme/version, constraints, recent source coverage, active decisions and unresolved questions.
2. Recent evidence: the requested period and a sufficient comparable baseline. A weekly review typically needs seven complete days plus two to four weeks; a same-day question may need just recent relevant sessions and recovery.
3. Historical lookup: selected older sessions, programme sections or prior decisions that answer a named question. The history is available for retrieval, not preloaded into every interaction.

Use directory listings, manifests, coverage files, sheet names, dates and programme indexes to locate evidence before reading bodies. One cumulative export can supply both current and historical slices; read/process the file with an available analysis tool and return only the relevant subset to conversational context. Do not dump all CSV rows, all 40 workbook tabs, full TCX telemetry, archive trees, or old chats into the model.

For bounded spreadsheet reads, select relevant tabs, columns and date/exercise rows. When tools cannot filter before returning data, use a complete authenticated raw download and structured local analysis if available. Otherwise request/use a focused summary or disclose the unavailable calculation. Truncated readable text is not complete evidence.

As an initial working budget, keep the current brief around 500-800 words or less, choose at most a few relevant files per domain, and show aggregates plus representative anchor exposures. These are context-management defaults, not evidence limits: expand only when an unresolved question needs more evidence. Do not truncate away contradictory records or source limitations to satisfy a word budget.

## Triggered Lookbacks

Before retrieving history, specify the question, comparison window and fields needed:

| Question | Targeted lookup |
|---|---|
| Am I progressing? | Start of the active block or last comparable block; matched exercise/equipment, load/reps/RIR, cardio modality/settings, weigh-in/measurement context |
| What programme suited me? | Selected block schedules and completed exposures, adherence, time demand, documented response and reasons for changes |
| Which workouts do I prefer? | Explicit dated preferences, substitution reasons, discomfort notes and recent user statements; adherence alone does not prove preference |
| Is this plateau new? | Previous comparable exposures and a prior plateau/adjustment, with actual outcome if recorded |
| Has recovery changed? | Same-source baseline for the relevant metric and matched training context; avoid silently mixing devices/measurement methods |
| What did we decide last time? | Most recent relevant decision and follow-up, not the entire coaching history |

Retrieve one bounded historical slice first. Stop when it answers the question with adequate comparability. Widen the window or fetch another relevant record only when the first lookup leaves a stated gap. Explain a material mismatch such as a different machine, body mass, training phase, injury state, environment or RPE scale.

Longitudinal summaries can start with compact milestones (block start/end, comparable anchors, waist/weight observations, cardio exposure), then retrieve exact underlying records for an important claim. Use an existing index where available. If an authorized index is maintained, keep source links/IDs, dates, brief tags and status, not a second copy of raw exports.

## Prevent Drift

- Date and attribute every consequential preference, goal, programme and setting. Label it confirmed current, historical, proposed or awaiting confirmation.
- Latest user statements override old snapshots for the stated field. A programme ending months ago remains historical even if it is the only file in Active Program. Do not infer a new active programme from its name or order inside an export.
- Separate observed, provider-derived and AI-summarized data. A prior coach's recommendation is not a completed session or a measured physiological result.
- Preserve both sides of an unresolved source conflict. Ask or retrieve focused evidence when it affects the decision; do not resolve by repeatedly summarizing one claim until it appears established.
- On a handoff/compaction, reload the current brief and verify current source freshness and pending decisions. Do not restart historical ingestion or treat the last conversation summary as unquestionable truth.
- When checking an old decision's outcome, obtain the relevant later observations before claiming success. Keep untested recommendations marked as proposals.

## Compact Continuity Record

When authorized to persist, maintain a short dated current brief alongside append-only dated reviews in Context Snapshots. Preserve earlier briefs as history; a new brief supersedes current fields explicitly. Include:

```text
As of / timezone:
Confirmed goals and cardio preferences (source/date):
Active programme/version or unresolved status:
Current constraints and exercise/equipment preferences:
Latest source locations and coverage by domain:
Recent comparable performance/body/cardio anchors:
Active decisions and expected responses:
Pending questions and targeted next lookup:
Links to relevant historical programme/review records:
```

Do not carry every historical measurement forward. Persist useful anchors, reasons and links; retrieve the rest when needed. If writes are unavailable or not requested, return this brief as a handoff artifact and state that it has not been saved to Drive.

If a multi-agent workflow is explicitly requested and authorized, give each agent a question, bounded dates, source scope and permitted actions. Require compact findings with source pointers and uncertainties. The coordinating agent resolves conflicts into one current brief; agents must not each ingest the entire repository or independently overwrite shared coaching state.
