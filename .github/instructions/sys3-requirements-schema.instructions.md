---
name: SYS.3 Requirements Schema
description: "Use when: writing, reviewing, or validating SYS.3 requirements for the SA8620P ADAS platform"
applyTo: ["**/requirements/**", "**/*SYS*", "**/*.requirements.md"]
---

# SYS.3 Requirements Schema — SA8620P Platform

## Canonical YAML Attribute Block

```yaml
---
id: SYS-GPTP-001          # Format: SYS-{TOPIC}-{NNN} — GPTP | HTP | TSC | TSR
level: SYS.3
asil: B                    # QM | A | B | C | D
source:                    # Upstream traceability (stakeholder reqs, standards)
  - STK-NET-001
  - IEEE-802.1AS-2020 §6.2
verification: TEST         # TEST | ANALYSIS | INSPECTION | DEMONSTRATION
verification_criteria: |
  [Measurable pass/fail criterion — must include: unit, threshold, conditions]
rationale: |
  [Why this requirement exists. Standard clause or design constraint.]
references:
  - MRVL-88Q5050-DS §4.2
  - VEC-MSR-ADAPT-TSYNC §2.3
safety_mechanism: |        # Required for ASIL ≥ A
  [How failures are detected and the system responds]
refines:                   # Parent SYS.3 req (if this is a derived/decomposed req)
  - SYS-TSC-005
allocates_to:              # SA8620P allocation targets
  - QNX:KryoP0
tags: []
---
```

## Required Fields by ASIL

| Field | QM | A | B | C | D |
|-------|----|---|---|---|---|
| `id` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `level` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `asil` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `source` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `verification` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `verification_criteria` | ✓ | ✓ | ✓ | ✓ | ✓ |
| `rationale` | — | ✓ | ✓ | ✓ | ✓ |
| `references` | — | ✓ | ✓ | ✓ | ✓ |
| `safety_mechanism` | — | ✓ | ✓ | ✓ | ✓ |
| `allocates_to` | — | — | ✓ | ✓ | ✓ |

## Valid `allocates_to` Targets

| Target | OS | ASIL ceiling |
|--------|----|-------------|
| `QNX:KryoP0` / `QNX:KryoP1` | QNX 8.0, SCHED_FIFO | B |
| `QNX:KryoE<n>` | QNX 8.0, ara::exec | B |
| `SAIL:SafeRTOS` | SafeRTOS plain C | D |
| `QNX:Hexagon` / `QNX:Adreno` | QNX 8.0, FastRPC | QM |
| `Hardware:88Q5050` | Marvell TSN switch | — |
| `Hardware:88Q22xx` | Marvell PHY | — |
| `Hardware:PMIC` | Intel PMIC | — |

## Requirement Text Rules

- One `shall` per requirement — atomic
- No `should`, `may`, `as appropriate`, `reasonable`, `fast`
- Quantify all constraints: time (µs/ms), percentage (%), temperature (°C), count (#)
- Format: `**SYS-{ID} — {Title}**\n\nThe system shall {verb} {object} {constraint}.`

## Anti-Patterns

- ❌ `The system should maintain synchronization` → ❌ "should", not quantified
- ❌ `shall perform BIST at startup` → missing: pass/fail criterion, ASIL, safety_mechanism
- ❌ `allocates_to: [QNX:Hexagon]` for ASIL-B function → Hexagon is QM
- ❌ Empty `verification_criteria` or criteria without units
- ❌ `safety_mechanism` left blank on ASIL-B/D requirement
