# Project Conventions

Distilled, current conventions — the "how we do things here" summary. When a LEARNINGS.md
pattern repeats, it gets promoted to a line here. Keep entries short; link the source.

## Requirements

- Canonical YAML attribute block + citation grammar are locked
  (`sys3-requirements-schema.instructions.md`) — never re-litigate fields
- IDs: `SYS-{GPTP|HTP|TSC|TSR}-NNN`, zero-padded, never reused

## Architecture

- Element IDs: `ARC-{AREA}-NNN`; every element `realizes:` ≥ 1 SYS-* requirement
- Allocation vocabulary identical to the locked schema's `allocates_to` targets

## Tools

- Codebeamer is authoritative for requirements; Confluence copies are informative
- All tool state enters offline via `imports/` — no live API assumptions in any output

## Platform

- Classic AUTOSAR is out project-wide; all AUTOSAR is Adaptive on QNX; SAIL runs SafeRTOS only
