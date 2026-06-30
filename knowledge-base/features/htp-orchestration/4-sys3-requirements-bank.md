# HTP Orchestration — SYS.3 Requirements Bank

Pre-written SYS.3 requirements. Adapt IDs and import to Codebeamer.

---
id: SYS-HTP-001
level: SYS.3
asil: B
source:
  - STK-PERC-001
verification: TEST
verification_criteria: |
  HTP inference latency for DLC complexity class C2 shall be ≤ 100 ms (95th percentile)
  measured under full CPU load at +85 °C junction temperature over 1000 consecutive inferences.
rationale: |
  100 ms deadline set by sensor fusion EKF cycle requirement (SYS-PERC-TBD).
  95th percentile used to allow occasional thermal throttle events.
references:
  - QC-SA8620P-TRM §TBD
  - QC-HEXAGON-SM §TBD
safety_mechanism: |
  ara::phm DeadlineSupervision with 100 ms deadline;
  violation sets DTC_HTP_DEADLINE_MISS and triggers fusion EKF degraded mode.
allocates_to: [QNX:KryoP0, QNX:Hexagon]
tags: [htp, orchestration, deadline]
---

**SYS-HTP-001 — HTP inference deadline**

The system shall complete HTP inference and deliver results to the sensor fusion service within ≤ 100 ms (95th percentile) of inference start.

## TODO: Add requirements for DLC lifecycle, OOD threshold, SMMU isolation, FastRPC error handling
