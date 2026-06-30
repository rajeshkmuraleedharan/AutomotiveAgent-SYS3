# AutomotiveAgent-SYS3 — Claude Daily Use Guide

Focused SYS.3 requirements agent for SA8620P ADAS (gPTP, HTP, TSC). Output: Codebeamer YAML.

## Quick Start

```
@sys3-requirements-engineer Draft 6 SYS.3 requirements for gPTP grandmaster clock selection on SA8620P
@requirements-reviewer Review SYS-GPTP-001 through SYS-GPTP-010 for ASPICE compliance
@safety-analyst Perform ASIL decomposition for the gPTP time-base provider function
```

## Agents

| Agent | Use when |
|-------|----------|
| `@sys3-requirements-engineer` | Writing new SYS.3 requirements for gPTP / HTP / TSC |
| `@requirements-reviewer` | Reviewing requirements for ASPICE + Codebeamer compliance |
| `@safety-analyst` | TSC, ASIL decomposition, FMEA, SPFM/LFM analysis |

## Prompts

| Prompt | Use when |
|--------|----------|
| `/sys3-gptp` | Need gPTP TimeSync requirements |
| `/sys3-htp` | Need HTP Orchestration requirements |
| `/sys3-safety` | Need TSC / Technical Safety Requirements |
| `/req-review` | Review selected requirements |
| `/verification-criteria` | Write or improve verification criteria |

## Requirement ID Conventions

- `SYS-GPTP-NNN` — gPTP TimeSync (001, 002, …)
- `SYS-HTP-NNN` — HTP Orchestration
- `SYS-TSC-NNN` — Technical Safety Concept
- `SYS-TSR-NNN` — Technical Safety Requirements

## Platform Constraint

Classic AUTOSAR is out. SAIL runs SafeRTOS only. All AUTOSAR is Adaptive on QNX.

## Open Items

- [ ] Resolve vendor document TBD placeholders in `vendor-references.instructions.md`
- [ ] Fill knowledge-base feature files with real content
- [ ] Add Codebeamer project field IDs to `codebeamer-format.instructions.md`
- [ ] Validate CB import format against live Codebeamer instance
