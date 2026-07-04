---
name: SYS.2 Requirements Usage
description: "Use when: writing or reviewing SYS.2 system requirements (stakeholder-derived) for the SA8620P ADAS platform"
applyTo: ["**/requirements/**", "**/*SYS*", "**/*.requirements.md"]
---

# SYS.2 Requirements — Additive Usage of the Canonical Block

SYS.2 (System Requirements Analysis) items reuse the **locked canonical YAML block
unchanged** — the only difference is `level: SYS.2`. The schema file
(`sys3-requirements-schema.instructions.md`) is authoritative and untouched;
`validate-requirements.py` accepts SYS.2 as-is.

## What distinguishes a SYS.2 item

| Aspect | SYS.2 | SYS.3 |
|--------|-------|-------|
| `level` | `SYS.2` | `SYS.3` |
| Abstraction | WHAT the system does for stakeholders | HOW the system realizes it, quantified per element boundary |
| `source:` | STK-* stakeholder reqs, CON-* concepts, standards | SYS.2 IDs, SG-*/FSR, standards |
| `allocates_to` | usually absent (system-level; add only when the stakeholder constraint pins a domain) | mandatory per ASIL-B+ rules |
| `verification` | often DEMONSTRATION / TEST at vehicle or system level | TEST/ANALYSIS at platform level |

## Rules

- Same ID grammar and shared number space: `SYS-{TOPIC}-NNN` via `generate-req-id.py`
  — the `level` field distinguishes SYS.2 from SYS.3; an ID is never reused across levels
- Traceability chain: `STK-* / CON-*  →  SYS.2  →  SYS.3  →  ARC-*`
  — every SYS.3 item's `source:` should reach a SYS.2 item (or a safety goal);
    orphaned SYS.3 items are review findings
- SYS.2 text is still atomic, quantified, single-SHALL — all
  `rules/requirements-rules.md` language rules apply
- Solution bias is the top SYS.2 anti-pattern: naming components, targets, or
  protocols in a SYS.2 item is a finding unless the stakeholder truly constrains them

## Anti-Patterns

- ❌ `level: SYS.2` with `allocates_to: [QNX:KryoP0]` and no stakeholder justification
- ❌ SYS.2 item citing another SYS.2 item as its only source (circular abstraction)
- ❌ Restating a SYS.3 requirement one level up with identical wording
