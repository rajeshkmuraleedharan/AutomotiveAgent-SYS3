# JIRA — CSV Export Format

How to produce exports the importer understands (`scripts/importers/jira.py`).

## Export procedure

1. Issue search / filter → select the issues
2. Export → **CSV (all fields)** — "current fields" loses description and links
3. Drop the file into `imports/inbox/`

## Format quirks handled by the importer

- Repeated column headers (`Labels`, `Comment`, link columns) — values are collected
- `Inward/Outward issue link (TYPE)` columns → normalized `Links` row
- Wiki markup in Description → markdown (headings demoted below the issue heading)

## Sample

`imports/samples/jira-issues.csv` — synthetic 5-issue export (2 timing bugs, 1 safety
bug, 1 task, 1 concept story) used as the regression fixture.
