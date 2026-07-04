# AutomotiveAgent-SYS3 — Claude Daily Use Guide

Systems-engineering agent for SA8620P ADAS: SYS.2/SYS.3 requirements, system
architecture, concepts, and offline Codebeamer/JIRA/Confluence integration.
Output: Codebeamer YAML (requirements), ARC blocks + mermaid (architecture),
markdown (concepts).

## Session workflow

1. **Task start**: consult `project-context/` (conventions.md, LEARNINGS.md, ADRs)
   and check `imports/normalized/manifest.md` for recent tool state
2. Work with the agents/prompts below
3. **Task end**: if the session produced a correction, review finding, or decision —
   offer `/record-learning`

## Quick Start

```
@sys3-requirements-engineer Draft 6 SYS.3 requirements for gPTP grandmaster clock selection
@system-architect Decompose the TimeSync subsystem and define its ara::com services
@requirements-reviewer Review SYS-GPTP-001 through SYS-GPTP-010 for ASPICE compliance
@safety-analyst Perform ASIL decomposition for the gPTP time-base provider function
```

## Agents

| Agent | Use when |
|-------|----------|
| `@sys3-requirements-engineer` | Writing SYS.2/SYS.3 requirements (gPTP / HTP / TSC) |
| `@system-architect` | Architecture views, ARC decomposition, ara::com interfaces, allocation, concepts |
| `@requirements-reviewer` | Reviewing requirements AND ARC elements for compliance |
| `@safety-analyst` | TSC, ASIL decomposition, FMEA, SPFM/LFM analysis |

## Prompts

| Prompt | Use when |
|--------|----------|
| `/sys2-reqs` | Stakeholder-derived SYS.2 requirements (solution-free) |
| `/sys3-gptp` `/sys3-htp` `/sys3-safety` | SYS.3 requirements per feature |
| `/req-review` | Review selected requirements |
| `/verification-criteria` | Write or improve verification criteria |
| `/arch-view` | Static or dynamic architecture view for a feature |
| `/arch-interface` | ara::com service or QNX↔SAIL protocol definition |
| `/arch-allocation` | SYS→ARC→target allocation matrix with conflict findings |
| `/concept-feature` | Feature or operating concept (pre-requirements) |
| `/concept-trade-study` | Weighted trade study between design options |
| `/import-normalize` | Process Codebeamer/JIRA/Confluence exports from `imports/inbox/` |
| `/record-learning` | Persist a correction/decision into project memory |

## ID Conventions

- Requirements: `SYS-{GPTP|HTP|TSC|TSR}-NNN` (level field distinguishes SYS.2/SYS.3)
- Architecture: `ARC-{AREA}-NNN` | Concepts: `CON-{FEATURE}-NNN`
- Generate: `python scripts/generate-req-id.py [--prefix ARC|CON] --topic {TOPIC}`

## Validation

- Requirements: `commands/sys3/validate-schema.sh <file>` (locked schema — never edit it)
- Architecture: `commands/arch/validate-arch.sh <file>` (realizes-resolution, ASIL ceilings)
- Imports: `commands/import/normalize-exports.sh [--dry-run]`

## Offline tool integration

No API access to Codebeamer/JIRA/Confluence. Raw exports → `imports/inbox/` →
normalizer → `imports/normalized/` (the only import content the agent reads).
Details: `skills/tool-exports/SKILL.md`, `rules/import-rules.md`.

## Platform Constraint

Classic AUTOSAR is out. SAIL runs SafeRTOS only. All AUTOSAR is Adaptive on QNX.

## Open Items

- [ ] Resolve vendor document TBD placeholders in `vendor-references.instructions.md`
- [ ] Fill knowledge-base feature files with real content
- [ ] Add Codebeamer project field IDs to `codebeamer-format.instructions.md`
- [ ] Validate CB import format against live Codebeamer instance
- [ ] Fill `[TBD]` internal specifics in `knowledge-base/tools/` and `knowledge-base/architecture/`
- [ ] Phase 2: system-level bug analysis (bug-triage skill, `/bug-rootcause`, JIRA `--defects` profile)
