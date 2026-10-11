# Google Health Coach

Use the Google Health Coach AI agent as an additional route to recent or historical metrics available in the user's account, including data from a paired Pixel Watch and linked apps. Google describes its inputs as activity/exercise, sleep, body/health metrics and associated account data. Availability varies with actual device recording, sync, metric and account features. [Google's source description](https://support.google.com/googlehealth/answer/17055092?hl=en).

## Ask for the Gap

Define the missing period and metrics before asking. Use an accessible, authorized app/browser integration when available, or prepare the exact focused query for the user to send and use their returned answer. A Drive connector alone does not provide live access to the Coach conversation. Do not claim to query the agent if no working route exists. Do not require a full Takeout export when a bounded answer can support the decision.

Select only fields needed for the question. Possible categories include cardio sessions, sleep, RHR, HRV, steps, readiness, active-zone minutes, and other actually tracked metrics. Discover unfamiliar metrics from the available account rather than hard-coding all Pixel Watch capabilities or presuming the Coach can expose every raw measurement.

Ask for dates/timezone, units, observation counts or missing days, source/device where known, and the newest synced observation. Prefer a small dated table and aggregates. Separate recorded values from the Coach's interpretation. Do not accept claims of no missing days unless coverage supports them.

Example weekly query; replace dates and select only the fields needed:

```text
For [start date] through [end date] in [timezone], summarize my recorded cardio
sessions of any type. Give date/start time, original activity type, duration,
average HR if recorded, and source/activity IDs if accessible. Distinguish
manual and tracked entries and note overlapping/synced duplicates where known.
Report missing fields rather than guessing and keep daily active-zone minutes
separate from elapsed session duration.

For the same period, summarize sleep duration, resting HR, overnight HRV and
steps with units, days recorded and latest synced date. Compare with the
preceding [baseline window] using the same sources. Return a compact table,
not all sensor records. Keep observed/provider-derived values separate from
interpretation. Say explicitly if you cannot access exact values or coverage.
```

For a historical question, request one matched window or programme period, not all recorded history. For an unfamiliar metric, ask what is available, its definition/unit, whether it is measured or estimated, and which dates/source support the answer. Request individual sessions only when they affect the analysis.

## Interpret and Reconcile

Capture the query period, response date, metric definitions and coverage. Label the answer `Google Health Coach summary`, not a direct raw export. Use dated numeric facts as provisional summary evidence, and attribute the Coach's recommendations separately. Check surprising values, unsupported claims or calculations that materially drive a decision against a focused export or app record when possible. If unavailable, qualify that conclusion rather than turning an AI answer into a measurement.

A Coach summary, Google Health export and synced Strava activity may all describe the same underlying observation. They are not three independent confirmations or additional sessions. Preserve source linkage and count physical sessions once. A current Coach summary can supplement an old export for its stated dates; it does not refresh the older file or supply missing detailed set/telemetry data.

If saving the answer is authorized, store a dated compact summary with the query, relevant numeric table, units, coverage limitations and provenance in the existing Context Snapshots location. Link it from the current brief. Omit unnecessary personal/account/location details and avoid copying a full conversation. Verify persistence before saying it is saved.
