---
name: Technical Safety Concept — SA8620P
description: "Use when: writing TSC safety requirements, performing ASIL decomposition, specifying safety mechanisms, or deriving TSRs from FSRs on the SA8620P platform"
applyTo: ["**/safety**", "**/*TSC*", "**/*TSR*", "**/*asil*", "**/*SYS-TSC*", "**/*SYS-TSR*"]
---

# Technical Safety Concept — SA8620P Platform

## Topic Scope (SYS.3)

TSC requirements covering:
- Safety goals → Functional Safety Requirements (FSR) → Technical Safety Requirements (TSR)
- ASIL decomposition (ASIL-D → QNX ASIL-B + SAIL ASIL-B)
- Safety mechanism specification (watchdog, alive/deadline/logical supervision, E2E, BIST)
- SPFM / LFM targets and FMEDA evidence
- Hardware safety (PBIST, CBIST, OBIST)
- Safe state definition and GPIO assertion

## ASIL Decomposition Pattern

```
ASIL-D Safety Function
    │
    ├── QNX 8.0 Element (Kryo)        ASIL-B
    │     detection, decision, ara::phm supervision
    │     heartbeat to SAIL every 10 ms
    │
    └── SafeRTOS SAIL Element          ASIL-B
          watchdog, safe-state GPIO, heartbeat monitor
          boots before QNX; independent MPU/power
```

**Independence arguments:**
- SAIL MPU: QNX Kryo cannot write SAIL TCM/SRAM
- SMMU: Adreno/Hexagon DMA isolated from SAIL memory
- Physical isolation: SAIL is separate MCU fabric on SA8620P die
- Independent POR: SAIL not reset by QNX

## Safety Mechanism Categories

| Category | SA8620P Example | DC class |
|----------|----------------|---------|
| Hardware watchdog | SafeRTOS HW_Watchdog_Task (5 ms) | High |
| Alive supervision | ara::phm AliveSupervision on ASIL-B services | High |
| Deadline supervision | ara::phm DeadlineSupervision on HTP (100 ms) | High |
| Logical supervision | ara::phm LogicalSupervision on CBIST result | High |
| E2E protection | CRC32 + seq + alive counter on QNX↔SAIL heartbeat | High |
| BIST | PBIST (power-on), CBIST (concurrent), OBIST (on-demand) | High |
| OOD detector | OOD score > 0.7 → fusion EKF degraded mode | Medium |
| ASIL decomposition | ASIL-D → QNX ASIL-B + SAIL ASIL-B | — |
| Safe state | SAIL GPIO to braking ECU; FunctionGroup stays Off | — |

## SPFM / LFM Targets

| ASIL | SPFM | LFM |
|------|------|-----|
| D | ≥ 99% | ≥ 90% |
| C | ≥ 97% | ≥ 80% |
| B | ≥ 90% | ≥ 60% |

## Element ASIL Table

| Element | ASIL | OS |
|---------|------|----|
| HW_Watchdog_Task | D | SAIL SafeRTOS |
| Safe-state GPIO driver | D | SAIL SafeRTOS |
| QNX_Heartbeat_Monitor | B | SAIL SafeRTOS |
| Sensor fusion EKF | B | QNX Kryo P-core |
| AEB / safety decision | B | QNX Kryo E-core |
| gPTP time-base provider | B | QNX Kryo P-core |
| HTP inference supervisor | B | QNX Kryo P-core |
| BIST boot sequencer | D | SAIL + ara::exec |
| Object detection DNN | QM | QNX Hexagon/Adreno |

## Requirement Areas

See `knowledge-base/features/technical-safety-concept/` for deep reference and requirements bank.

1. Safety goals — HARA output, hazardous events, S/E/C ratings
2. FSR → TSR derivation — allocation to SA8620P elements
3. ASIL decomposition — independence claims per element pair
4. Watchdog — HW_Watchdog_Task timeout ≤ 5 ms
5. Heartbeat — QNX → SAIL protocol, E2E CRC32, missed = 3 → safe state
6. BIST — PBIST at boot, CBIST concurrent, OBIST on-demand; boot gate
7. Safe state — GPIO assertion, FunctionGroup Off, reaction time ≤ 10 ms
8. SPFM/LFM — FMEDA-derived targets per element
