# Data Sources

## Drive Workflow

Ground the training root through the user-provided folder or `00 - START HERE - Training Repository Guide.txt`. List its immediate children, then follow only relevant folders. Avoid broad personal-Drive searches after the training root is known. Connector search, folder listing, readable fetch, raw download, and native Sheets operations are different capabilities; consult the tools actually available.

Observed repository layout:

| Location | Purpose |
|---|---|
| Active Program | Intended schedule and progression |
| Programs | Reference or archived programmes |
| Workouts / Strength Training / MacroFactor Exports / year | Full exports and completed sets; full exports can also contain nutrition/body data |
| Workouts / Running | Run originals, activity index, and ingestion manifests |
| Nutrition | Nutrition exports; compare coverage with newer full MacroFactor exports elsewhere |
| Health Data / Google Health / Agent-Ready Snapshots / export timestamp | Normalized health, sleep, body and workout CSVs, manifest, coverage |
| Context Snapshots | Dated goals, profile, constraints and decisions |
| Archive / Raw Takeout Exports | Recovery source when normalized data cannot answer the task |

Cardio records may live in several of these locations. A `Running` folder name is not an instruction to exclude walks or stairs. Support a future `Workouts / Cardio` folder if the user adds it; no move or folder reorganization is required for analysis.

Google Health and Strava normally supply completed cardio. MacroFactor cardio rows are occasional supplemental evidence, not the expected primary log. Include current Google Health Coach summaries via [Google Health Coach](google-health-coach.md) when available, with their period, provenance and limitations. Watch data availability depends on actual recording and the metric; do not assume every app metric is directly measured by the watch.

Read the newest suitable Google Health manifest before its CSVs. Prefer a newer complete snapshot that supersedes the same coverage. Do not stack cumulative snapshots or treat a newer partial snapshot as replacing unavailable older history. Keep source timestamp, coverage, and completeness in the report.

The latest user request can supersede old running preferences. An Active Program file dated July whose block ends in August remains historical in October unless continuation is explicitly confirmed. A programme stored inside a newer export also needs evidence that it is currently active.

## MacroFactor Schemas Observed in the Examples

The full XLSX has 40 sheets spanning nutrition, body data, exercise summaries, programmes, notes and settings. Classify by contents rather than extension or filename.

| Sheet or file | Use and limitations |
|---|---|
| Calories & Macros | Dated recorded intake: kcal and grams of fat, carbs, protein. Sparse or low entries can be incomplete logging. |
| Scale Weight, Weight Trend, Expenditure | Separate actual weigh-ins, app-generated trend, and expenditure estimate. Daily generated values are not daily independent measurements. |
| Body Metrics | Measurement headers specify units. The example labels circumference columns `(in)`; validate suspect values before converting or interpreting them. |
| Partial Logging | Explicit partial flags. An absent flag alone does not prove that a food log is complete. |
| Nutrition Program Settings, Weight Goals | Target history and goal status. Respect update dates, weekday distribution, goal rate units and active status. |
| Muscle Groups - Sets / Volume, Exercises - ... | App-generated summaries. Useful cross-checks, not additional completed work to add to set-level totals. |
| Training Programs | Block/cycle prescription with repeated headers, notes, rep ranges, RIR and rest; not a flat completed-set table. |
| Workouts | Exercise/workout definitions and prescriptions in this example; inspect structure before treating any row as an actual logged set. |
| Workout Log Notes | Dated exercise context for equipment, technique and modifications. |
| Completed-workout CSV | One row per logged set/component, including cardio. Headers include Date, Workout Duration, Workout, Exercise, Exercise Base Weight (kg), Set Type, Weight (kg), Reps, RIR, Duration, Distance short (Yd), Distance long (Mi). |

The separate July import workbook is a single `Training Programs` sheet. Read it as a prescription, including cardio instructions embedded in lifting notes.

CSV handling:

- Use a CSV parser with UTF-8 handling. The supplied completed-set CSV has a malformed first header containing literal mojibake BOM characters and embedded quotes around `Date`. Normalize that recognized header in a working copy to `Date`; preserve the original. Do not globally replace text or silently accept unknown schema changes.
- `Workout Duration` repeats across rows belonging to a session. Count it once per identifiable session; never sum it across sets. Grouping by date and workout name is provisional because the file has no stable session ID or start time. Flag multiple same-day sessions or ambiguous grouping.
- `Duration` is the component field, distinct from total workout duration. The observed stair entry has `Duration=900`, consistent with 15 minutes in seconds; validate units against notes/provider definitions for unfamiliar exports.
- Weight is kg, but distance columns explicitly use yards and miles. If needed, convert yards to metres with 0.9144 and miles to km with 1.609344. Preserve source values and units.
- A row named `Stair Climbing (Duration Only)` is cardio even when `Set Type=Standard Set` and `Weight (kg)=0`. Include its duration once and exclude it from lifting set totals. `Walking` alone does not establish treadmill use or incline.
- Classify cardio using exercise identity and notes, not a zero weight, missing reps, or duration alone. Timed holds and loaded carries can be strength work.

XLSX handling:

- Use a spreadsheet reader. Honour the workbook's date system when decoding serial dates. Parse explicit text dates according to the observed format; examples include UK day/month/year and dates in prose. Preserve UTC timestamps separately from local training dates.
- Inspect sheets, row labels, cell positions and units before extracting. Sparse rows and repeated block headers require structured interpretation. Do not flatten cells by dropping blanks: that shifts values into the wrong columns.
- Nutrition/body evidence can lag the export timestamp. Report latest actual weigh-in, latest usable intake, latest target update and trend/expenditure coverage independently.

## Google Health Agent-Ready CSVs

Observed `workouts.csv` columns:

```text
exercise_id,start,end,duration_seconds,activity_name,activity_label,log_type,
calories_kcal,steps,distance_km,average_heart_rate_bpm,peak_heart_rate_bpm,
cardio_load,data_source
```

Treat `exercise_id` as a string. The observed identifiers exceed JavaScript's safe integer range. Inspect activity name/label and log type: automatic outdoor walks, tracker recordings, manual workouts and strength sessions can overlap. Preserve manual-versus-recorded provenance. A generic `Workout` label cannot establish modality.

Zero HR is missing/invalid physiology. Zero distance can be a legitimate indoor record or an unavailable measurement; it does not invalidate duration. Manual records with all-zero calories, steps and HR do not demonstrate zero workload. `cardio_load=0` alone does not prove a recovery session.

Observed `daily_health_metrics.csv` includes date, day_status, steps, activity-minute categories, active-zone minutes, sleep, RHR, HRV, readiness and provider workload fields. Respect `partial_at_export`. Blank values are missing; do not turn them into zero. Keep Fitbit active-zone minutes separate from elapsed session minutes because intensity weighting and overlap can differ. Do not add daily totals to the workouts that generated them.

Use `sleep_sessions.csv`, `body_measurements.csv`, and `data_coverage.csv` when relevant. Assign sleep according to the snapshot's documented convention and preserve naps/overlapping records appropriately. Compare HRV/RHR with the user's baseline from the same measurement source.

## Strava and Reconciliation

The running index contains Date, Title, ActivityId, Distance, Duration, OriginalFormat, SourceFile, ImportBatch. Preserve IDs as strings. Titles do not establish measured intensity or prove that a treadmill session was a run rather than a walk.

Parse TCX as namespaced XML. Lap duration/distance, trackpoint timestamps and HR can support detailed analysis. Distinguish elapsed, moving and recorded duration; reconcile lap summaries rather than assuming they match the index. Retain indoor records with zero GPS distance. Do not invent speed from it, reconstruct incline from altitude, or infer stairs from cadence. FIT needs an available decoder; GPX may lack duration summaries or HR.

Deduplicate identical Strava IDs across batches/formats. Different Strava IDs can still describe overlapping recordings of one physical session; flag candidate overlap using timestamps, modality, notes and duration rather than merging by title/date alone. Retain provenance for every source.

For Google Health versus Strava versus MacroFactor, build one physical-session view when matching evidence is strong. Within a mixed gym session, retain lifting and cardio components without adding the full gym duration to cardio. When linkage is ambiguous, report certain totals and uncertain overlap separately. Do not sum all apps and call it weekly training load.

Automatic Google Health-to-Strava sync makes a matching pair likely to be one activity, not two independently corroborating workouts. Prefer explicit source/activity linkage. If no linkage exists, compare actual start/end, modality and recorded duration. Retain source-specific fields without duplicating the session. User corrections take precedence for the corrected field when their provenance is documented.

## Minimal Analysis View

Keep available fields and missing fields explicit:

- Sources: file/link, export date, coverage, completeness, measurement source.
- Lifting: session key, date, exact exercise/equipment, set order, type, side, kg, reps, RIR, notes.
- Cardio: source IDs as strings, start/end, modality, duration, effort, HR quality, machine settings and units, notes, overlap status.
- Daily context: date, observed weight, modelled trend, recorded intake, completeness, sleep, steps, RHR/HRV.

No custom parser is mandatory. Use available spreadsheet/code tools for accurate calculations; readable connector text is suitable for discovery and bounded review. If it is truncated or cannot expose relevant rows, obtain the complete raw file through an available authenticated download or use an accessible attachment before calculating totals.
