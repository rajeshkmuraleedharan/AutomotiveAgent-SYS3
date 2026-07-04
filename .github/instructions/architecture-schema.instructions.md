---
name: Architecture Element Schema
description: "Use when: writing, reviewing, or validating system architecture elements (ARC-*) for the SA8620P ADAS platform"
applyTo: ["**/architecture/**", "**/*ARC*", "**/*.architecture.md"]
---

# Architecture Element Schema — SA8620P Platform

Architecture elements get their own YAML block. This schema is **separate from and
additive to** the locked SYS.3 requirement schema — requirement fields are unchanged.
Platform constraint applies: Classic AUTOSAR is out; all AUTOSAR is Adaptive on QNX;
SAIL runs SafeRTOS only.

## Canonical ARC Element Block

```yaml
---
id: ARC-GPTP-001           # Format: ARC-{AREA}-{NNN} — same AREA vocabulary as SYS IDs
type: component            # system | subsystem | component | interface
asil: B                    # QM | A | B | C | D — inherited from realized requirements
realizes:                  # MANDATORY: ≥ 1 SYS-* requirement this element realizes
  - SYS-GPTP-001
  - SYS-GPTP-002
allocates_to:              # Same target vocabulary as the locked requirement schema
  - QNX:KryoP0
interfaces:
  provides:
    - TimeBaseStatusService     # ara::com service or named internal interface
  requires:
    - EthTsnDriverIf
description: |
  [One paragraph: responsibility of the element, its failure behaviour, and its
  place in the decomposition.]
tags: [gptp]
---
```

## Field Rules

| Field | Rule |
|-------|------|
| `id` | `ARC-{AREA}-NNN`, zero-padded; generate with `scripts/generate-req-id.py --prefix ARC` |
| `type` | `system` > `subsystem` > `component`; `interface` for pure interface elements |
| `asil` | max ASIL of `realizes` entries; lower only with documented ASIL decomposition (`decomposition: ASIL-X(Y)` field + safety-analyst sign-off) |
| `realizes` | every entry must resolve to an existing SYS-* requirement |
| `allocates_to` | mandatory for `component`; must respect target ASIL ceilings (locked schema table) |
| `interfaces` | every `requires` must be some element's `provides` (checked at review) |
| `description` | responsibility + failure behaviour — not implementation detail |

## Views

- **Static view**: one mermaid `graph TD/LR` per view; nodes labelled `ARC-ID<br>Name [ASIL]`;
  containment via subgraphs; ≤ 12 elements per diagram — split otherwise
- **Dynamic view**: mermaid `sequenceDiagram` (interactions: startup ordering, mode change,
  degradation cascade) or `stateDiagram-v2` (element modes); participants are ARC IDs
- Every view carries a one-line caption: viewpoint, concern, and the SYS-* requirements it addresses

## Anti-Patterns

- ❌ Element without `realizes` — architecture invented without a requirement
- ❌ ASIL-B element `allocates_to: [QNX:Hexagon]` — Hexagon is QM ceiling
- ❌ `type: component` without `allocates_to`
- ❌ Classic AUTOSAR concepts (BSW, RTE, SWC composition) anywhere
- ❌ One diagram showing the whole platform — split by viewpoint
