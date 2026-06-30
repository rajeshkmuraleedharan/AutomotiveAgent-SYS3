# TSC — Safety Goals, FSR, TSR

## Safety Goal Derivation (from HARA)

TODO: Add safety goals derived from SA8620P ADAS HARA.

Example structure:
```
SG-001: Avoid unintended AEB activation (ASIL-D)
  → FSR-001: AEB activation shall only occur on valid threat detection
  → TSR-001: AEB enable signal validated by SAIL safety monitor
  → TSR-002: Sensor fusion output gated by heartbeat health status
```

## FSR → TSR Pattern

Each FSR is refined into TSRs that:
1. Allocate to specific SA8620P elements
2. Inherit or decompose ASIL
3. Specify the safety mechanism that provides coverage
4. Reference the verification method

## TODO: Populate with actual safety goals from project HARA
