# Skill — SA8620P Platform

Platform overview skill for the Qualcomm SA8620P ADAS SoC.

## Platform Summary

| Layer | Component | ASIL ceiling |
|-------|-----------|-------------|
| SoC | Qualcomm SA8620P | — |
| Performance cores | Kryo (QNX 8.0) | B |
| GPU | Adreno (QM only) | QM |
| AI accelerator | Hexagon HTP (FastRPC, QM) | QM |
| Safety MCU | SAIL (SafeRTOS) | D |
| AUTOSAR | Vector MICROSAR Adaptive | B (QNX) |
| Ethernet switch | Marvell 88Q5050 | — |
| Ethernet PHY | Marvell 88Q22xx | — |
| PMIC | Intel PMIC | D |

## Core Allocation

| Workload | Core | ASIL |
|----------|------|------|
| Sensor fusion EKF | Kryo P0 | B |
| AEB / safety decision | Kryo E0 | B |
| HTP orchestrator | Kryo P0 | B |
| ara::phm / ara::exec | Kryo E-core | B |
| Object detection DNN | Hexagon HTP | QM |
| Watchdog / safe-state | SAIL | D |
| Heartbeat monitor | SAIL | B |
| BIST sequencer | SAIL + ara::exec | D |

## ASIL Decomposition (D → B + B)

```
ASIL-D function
├── QNX element (Kryo)   ASIL-B  ← detection + decision + ara::phm
└── SAIL element          ASIL-B  ← watchdog + safe-state GPIO + heartbeat
```

Independence: SAIL MPU, SMMU, physical core, independent POR.

## Boot Sequence

```
PMIC on → SAIL powers up → PBIST → QNX boots → ADAS FunctionGroup starts
```

ADAS FunctionGroup MUST NOT start until PBIST passes (BistReady=true).
