# TSC — SA8620P ASIL Decomposition

## Decomposition Pattern

```
ASIL-D → ASIL-B (QNX element) + ASIL-B (SAIL element)
```

Per ISO 26262-9, the two elements must be sufficiently independent.

## Independence Arguments

| Independence measure | SA8620P implementation |
|---------------------|----------------------|
| Memory protection | SAIL MPU blocks QNX Kryo write access to SAIL TCM |
| DMA isolation | SMMU bounds Hexagon/Adreno DMA; no access to SAIL memory |
| Physical isolation | SAIL is separate MCU fabric on die |
| Power independence | SAIL powered independently; not reset by QNX |
| Dependent failure analysis | TODO: DFA document reference |

## Element ASIL Table

| Element | ASIL | OS | Role |
|---------|------|----|------|
| HW_Watchdog_Task | D | SAIL SafeRTOS | Last line of defence |
| Safe-state GPIO | D | SAIL SafeRTOS | Braking ECU signal |
| QNX_Heartbeat_Monitor | B | SAIL SafeRTOS | Part of decomposed ASIL-D |
| Sensor fusion EKF | B | QNX Kryo P0 | Part of decomposed ASIL-D |
| HTP inference supervisor | B | QNX Kryo P0 | Supervises QM HTP |
| BIST boot sequencer | D | SAIL + ara::exec | Boot gate |

## TODO: Add dependent failure analysis (DFA) reference
