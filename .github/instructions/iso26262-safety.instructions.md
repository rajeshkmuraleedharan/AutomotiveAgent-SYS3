---
name: ISO 26262 Safety Reference — SA8620P
description: "Use when: classifying ASIL, writing safety requirements, specifying SPFM/LFM, referencing safety lifecycle processes, or citing ISO 26262 clauses"
applyTo: ["**/safety**", "**/*FMEA*", "**/*HARA*", "**/*asil*", "**/*SYS-TSC*", "**/*SYS-TSR*"]
---

# ISO 26262 Safety Reference — SA8620P Platform

## HARA-to-Requirements Flow

```
HARA (SYS.1)       → hazardous events, S/E/C classification, ASIL, safety goals
Safety goals       → Functional Safety Requirements (FSR) per ISO 26262-3
SYS.3 requirements → system architectural design, ASIL allocation, safety mechanisms
FMEA / FMEDA       → safety mechanism coverage evidence (SPFM, LFM)
SWE.1 requirements → software requirements, refines SYS.3
```

Never start FMEA after code. Never start SWE.1 before SYS.3 safety mechanisms are defined.

## ASIL Classification (S × E × C)

| Severity | Exposure | Controllability | ASIL |
|----------|----------|----------------|------|
| S3 | E4 | C3 | D |
| S3 | E4 | C2 | C |
| S3 | E3 | C3 | C |
| S2 | E4 | C3 | B |
| S2 | E3 | C3 | A |

## SPFM / LFM Targets

| ASIL | SPFM | LFM |
|------|------|-----|
| D | ≥ 99% | ≥ 90% |
| C | ≥ 97% | ≥ 80% |
| B | ≥ 90% | ≥ 60% |
| A | ≥ 60% | not specified |

## Safety Requirement Allocation Rules

| Target | ASIL ceiling |
|--------|-------------|
| `SAIL:SafeRTOS` | D |
| `QNX:KryoP0` / `QNX:KryoP1` | B |
| `QNX:KryoE<n>` | B |
| `QNX:Hexagon` / `QNX:Adreno` | QM |
| `Hardware:88Q5050` / `Hardware:88Q22xx` | per design |
| `Hardware:PMIC` | per design |

## Diagnostic Coverage per Mechanism

| Safety Mechanism | DC class | DTC |
|-----------------|---------|-----|
| Watchdog (< 10 ms timeout) | High (≥ 99%) | DTC_SAIL_WD_TIMEOUT |
| Alive supervision | High | DTC_FUSION_ALIVE_FAIL |
| Deadline supervision | High | DTC_HTP_DEADLINE_MISS |
| PBIST (full structural) | High | DTC_SAIL_PBIST_FAIL |
| CBIST (concurrent) | Medium–High | DTC_KRYO_CBIST_FAULT |
| E2E (CRC + seq) | High | DTC_HEARTBEAT_CRC_FAIL |
| OOD detector | Medium | DTC_HTP_OOD_TRIGGER |

## Anti-Patterns

- ❌ ASIL-D allocation to QNX without complementary SAIL element
- ❌ `safety_mechanism` empty on ASIL ≥ A
- ❌ SPFM/LFM stated without FMEDA source citation
- ❌ Reusing same diagnostic element for monitored function and supervisor
- ❌ Starting ADAS FunctionGroup before PBIST result confirmed
