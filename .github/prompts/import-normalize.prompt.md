---
name: Import Normalize
description: Process raw Codebeamer/JIRA/Confluence exports from imports/inbox/ into normalized markdown and summarize what changed.
---

Process the offline tool exports waiting in `imports/inbox/`.

## Steps

1. Run `commands/import/normalize-exports.sh --dry-run` and report what was detected
   (tool, item counts). If detection looks wrong, re-run with `--tool`.
2. Run `commands/import/normalize-exports.sh` for real.
3. For Codebeamer imports: run `commands/sys3/validate-schema.sh imports/normalized/codebeamer/*.md`
   and report any schema gaps (missing verification criteria, invalid `allocates_to`, …) —
   gaps are findings about the tracker content, not import errors.
4. Read the new files under `imports/normalized/` and summarize:
   - **Codebeamer**: which requirement IDs arrived, status changes vs. previous imports
     (check `imports/normalized/manifest.md` and older files), schema gaps
   - **JIRA**: new/changed issues by status and priority; anything referencing a `SYS-*`
     requirement ID gets flagged with that requirement
   - **Confluence**: page topics and any decisions recorded
5. Propose follow-up actions (e.g. "SYS-GPTP-002 criteria weakened in CB — review",
   "ADAS-104 suggests a missing timing requirement for PMIC brown-out recovery").
6. If a decision or convention was imported that should persist, offer `/record-learning`.
