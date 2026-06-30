---
name: HTP Orchestration — SA8620P
description: "Use when: writing SYS.3 requirements for Hexagon HTP DLC lifecycle, inference scheduling, OOD detection, deadline supervision, or FastRPC on SA8620P"
applyTo: ["**/htp**", "**/hexagon**", "**/orchestration**", "**/*SYS-HTP*"]
---

# HTP Orchestration — SA8620P Platform

## Topic Scope (SYS.3)

HTP orchestration requirements covering:
- DLC model load / unload lifecycle
- Inference scheduling and priority arbitration
- FastRPC channel management (QNX ↔ Hexagon DSP)
- Deadline supervision (ara::phm DeadlineSupervision)
- OOD (Out-of-Distribution) detection and degraded mode
- SMMU isolation — Hexagon DMA cannot access SAIL TCM
- SNPE / QNN runtime integration

## SA8620P Architecture

```
QNX (Kryo P0) — HTP Orchestrator Service (ASIL-B supervisor)
    │ FastRPC (SMMU-isolated)
    ▼
Hexagon HTP (QM accelerator)
    │ DLC model execution (SNPE / QNN runtime)
    │ Inference result → QNX
    ▼
OOD Detector (Kryo P0, post-processing) — score > 0.7 → degraded mode
    │
Sensor Fusion EKF (consumer)
```

## Key Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Inference deadline | ≤ 100 ms (95th percentile) | SYS-HTP-TBD |
| OOD threshold | > 0.7 | SYS-HTP-TBD |
| SMMU isolation | Hexagon DMA ≠ SAIL TCM | QC-SA8620P-TRM |
| HTP supervisor ASIL | B | allocated to QNX:KryoP0 |
| Hexagon / Adreno ASIL | QM | supervised by ASIL-B element |

## Requirement Areas

See `knowledge-base/features/htp-orchestration/` for deep reference and requirements bank.

1. DLC lifecycle — load, warm-up, run, unload; version management
2. Scheduling — priority arbitration, preemption policy, FIFO/priority queue
3. Deadline supervision — ara::phm DeadlineSupervision, 100 ms timeout
4. OOD detection — score computation, threshold, EKF degraded mode trigger
5. SMMU isolation — Hexagon DMA regions bounded; no SAIL access
6. FastRPC — channel setup, error handling, timeout
7. Resource monitoring — DDR bandwidth cap, thermal throttle policy

## Safety

- Hexagon HTP is QM — supervised by ASIL-B element on QNX:KryoP0
- Safety mechanism: ara::phm DeadlineSupervision → DTC_HTP_DEADLINE_MISS
- OOD mechanism: score > 0.7 → DTC_HTP_OOD_TRIGGER + fusion degraded mode
- SMMU: independence argument for ASIL decomposition
