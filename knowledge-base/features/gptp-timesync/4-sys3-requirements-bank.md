# gPTP TimeSync — SYS.3 Requirements Bank

Pre-written SYS.3 requirements. Reviewed and ready to adapt for your project.
Copy, adjust IDs, and import to Codebeamer.

---
id: SYS-GPTP-001
level: SYS.3
asil: B
source:
  - STK-NET-001
  - IEEE-802.1AS-2020 §10.2
verification: TEST
verification_criteria: |
  The local time-base offset to the gPTP grandmaster shall be ≤ 1 µs (3σ)
  measured over 24-hour soak at –40 °C and +85 °C with nominal network load.
rationale: |
  IEEE 802.1AS-2020 §10.2 end-station accuracy requirement.
  Sub-µs alignment required for camera/radar/IMU fusion EKF.
references:
  - MRVL-88Q5050-DS §4.2
  - VEC-MSR-ADAPT-TSYNC §2.3
safety_mechanism: |
  Holdover monitor: ≥ 3 missed sync events transitions status to kUncertain;
  sensor fusion EKF widens association gate in response.
allocates_to: [QNX:KryoP0, Hardware:88Q5050, Hardware:88Q22xx]
tags: [gptp, ieee802-1as, timesync]
---

**SYS-GPTP-001 — Time-base accuracy to gPTP grandmaster**

The system shall maintain a local time-base aligned to the gPTP grandmaster within ≤ 1 µs (3σ) under nominal operating conditions.

---
id: SYS-GPTP-002
level: SYS.3
asil: B
source:
  - STK-NET-002
verification: TEST
verification_criteria: |
  After 3 consecutive missed sync intervals (3 × 125 ms), the time-base status
  shall transition to kUncertain within one additional sync interval.
rationale: |
  Holdover detection must be fast enough to trigger EKF degraded mode before
  a stale timestamp causes a fusion error exceeding the safety threshold.
references:
  - VEC-MSR-ADAPT-TSYNC §3.1
safety_mechanism: |
  Status kUncertain reported to fusion EKF via ara::tsync API;
  DTC_GPTP_SYNC_LOSS set in ara::diag.
allocates_to: [QNX:KryoP0]
tags: [gptp, holdover, timesync]
---

**SYS-GPTP-002 — Holdover detection on sync loss**

The system shall detect loss of gPTP synchronization after 3 consecutive missed Sync messages and transition the time-base status to kUncertain.

## TODO: Add more requirements covering BMCA, startup gate, temperature range
