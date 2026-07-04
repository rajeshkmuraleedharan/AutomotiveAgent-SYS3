# Codebeamer — Overview

Codebeamer is the ALM system of record for SYS.2/SYS.3 requirements on this project.
The agent has **no API access** — state flows in via exports (see `skills/tool-exports/`)
and out via re-importable YAML (`scripts/cb-formatter.py`).

## Project structure (fill with internal specifics)

- Project: `[TBD — internal CB project name]`
- Trackers used:
  - `[TBD]` SYS.2 stakeholder/system requirements
  - `[TBD]` SYS.3 system requirements (gPTP / HTP / TSC)
  - `[TBD]` Technical Safety Requirements
- Field IDs for import mapping: see `codebeamer-format.instructions.md` (open item)

## What the agent uses Codebeamer knowledge for

1. Emitting YAML attribute blocks whose fields match tracker fields 1:1
2. Reading normalized exports and spotting status/content drift vs. repo content
3. Respecting workflow state (IDs immutable after `Approved`)
