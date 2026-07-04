# Codebeamer import — codebeamer-requirements

| Field | Value |
| --- | --- |
| Tool | codebeamer |
| Source export | codebeamer-requirements.csv |
| Imported | 2026-07-04 19:46 |
| Items | 3 |
| Source SHA-256 | 5fb6649052d4746e |

---
id: SYS-GPTP-001
level: SYS.3
asil: B
source:
  - STK-NET-001
  - IEEE-802.1AS-2020 §7.6
verification: TEST
verification_criteria: |
  Measured offset to GM ≤ 1 µs (3σ) over 24 h on-target run, sampled at 1 Hz, ambient 25 °C.
rationale: |
  IEEE 802.1AS-2020 accuracy budget for the camera fusion path requires ≤ 1 µs end-to-end.
references:
  - MRVL-88Q5050-DS §4.2
  - VEC-MSR-ADAPT-TSYNC §2.3
safety_mechanism: |
  Holdover monitor raises DTC_GPTP_SYNC_LOSS within 250 ms of sync loss and publishes kUncertain to consumers.
allocates_to:
  - QNX:KryoP0
  - Hardware:88Q5050
tags:
  - gptp
  - ieee802-1as
cb_meta:
  assignee: rajesh
  item_id: 1001234
  modified: 2026-06-28 14:12
  status: In Review
  tracker: SYS.3 Requirements
---

**SYS-GPTP-001 — Time accuracy to grandmaster**

The system shall maintain a time offset to the gPTP grandmaster of ≤ 1 µs (3σ) on all synchronized ports during nominal operation.

---
id: SYS-GPTP-002
level: SYS.3
asil: B
source:
  - STK-NET-001
  - IEEE-802.1AS-2020 §10.2
verification: TEST
verification_criteria: |
  Holdover entry latency ≤ 31.25 ms after 3rd missed Sync, verified on bench with fault-injection switch, 100 repetitions, 0 misses.
rationale: |
  Downstream fusion must know when the time base degrades; 3 missed syncs = 3 × sync interval at 125 ms... bounded detection.
references:
  - VEC-MSR-ADAPT-TSYNC §5.1
safety_mechanism: |
  Sync-loss counter in ara::tsync daemon; DTC_GPTP_SYNC_LOSS set; kUncertain flag propagated via time-base status API.
allocates_to:
  - QNX:KryoP0
tags:
  - gptp
  - holdover
cb_meta:
  assignee: rajesh
  item_id: 1001235
  modified: 2026-06-28 14:15
  status: In Review
  tracker: SYS.3 Requirements
---

**SYS-GPTP-002 — Holdover entry after missed syncs**

The system shall enter holdover state within 31.25 ms after 3 consecutive missed Sync messages and publish time status kUncertain to all time consumers.

---
id: SYS-HTP-001
level: SYS.3
asil: B
source:
  - STK-PERC-004
  - SG-002
verification: TEST
verification_criteria: |
  Deadline violation signalled ≤ 5 ms after 33 ms deadline expiry, fault-injection with delayed model stub, 500 inferences, 100% detection.
rationale: |
  Perception pipeline budget allocates 33 ms per frame at 30 FPS; undetected overruns violate the fusion freshness contract.
references:
  - QC-SNPE-UG §7.4
safety_mechanism: |
  Watchdog timer per DLC instance on KryoE supervisor; violation escalated to degradation manager.
allocates_to:
  - QNX:KryoE0
tags:
  - htp
  - deadline
cb_meta:
  assignee: rajesh
  item_id: 1001236
  modified: 2026-06-30 09:41
  status: Draft
  tracker: SYS.3 Requirements
---

**SYS-HTP-001 — Model deadline supervision**

The system shall detect an HTP inference exceeding its configured deadline of 33 ms and signal a deadline violation to the orchestration supervisor within 5 ms of expiry.
