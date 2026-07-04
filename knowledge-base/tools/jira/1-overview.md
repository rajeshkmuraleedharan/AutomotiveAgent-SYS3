# JIRA — Overview

JIRA tracks defects, tasks, and stories for the ADAS platform program. The agent sees
JIRA state only through CSV/Excel exports (`skills/tool-exports/`).

## Internal specifics (fill in)

- Project key(s): `ADAS-…` `[TBD — confirm actual keys]`
- Issue types in use: Bug, Task, Story `[TBD]`
- Priority scheme: P1–P4 `[TBD]`
- Components relevant to systems engineering: TimeSync, Perception, Safety `[TBD]`

## What the agent uses JIRA knowledge for

1. Summarizing imported issue exports (status, priority, ownership)
2. Cross-referencing bugs against `SYS-*` requirements they violate
3. Drafting re-importable ticket proposals (`NEW-` placeholder keys)
4. (Phase 2) system-level bug triage and root-cause support
