# HTP Orchestration — Lifecycle and Supervision

## DLC Lifecycle States

```
Unloaded → Loading → Warm-up → Ready → Running → Unloading → Unloaded
```

## Orchestrator Responsibilities

1. Load DLC from storage at startup
2. Execute warm-up pass (1 inference with dummy input)
3. Accept inference requests via ara::com service
4. Submit to HTP via FastRPC
5. Monitor deadline via ara::phm DeadlineSupervision
6. Process result + OOD score
7. Publish result to sensor fusion

## Deadline Supervision

```
ara::phm DeadlineSupervision
  startCheckpoint: InferenceStart
  endCheckpoint: InferenceComplete
  deadline: 100 ms
  violation → DTC_HTP_DEADLINE_MISS → fusion EKF degraded mode
```

## OOD Detection

Post-processing on QNX:KryoP0:
- OOD score computed from softmax entropy or calibrated uncertainty
- Threshold: 0.7 (TBD — calibrate from SOTIF validation dataset)
- Score > 0.7 → DTC_HTP_OOD_TRIGGER + fusion degraded mode

## TODO: Add inference request queue design, priority arbitration policy
