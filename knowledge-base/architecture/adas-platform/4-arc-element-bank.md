# ARC Element Bank — ADAS Platform

Pre-written, validator-clean example elements. Reuse and renumber via
`generate-req-id.py --prefix ARC`. All examples pass `commands/arch/validate-arch.sh`.

---
id: ARC-GPTP-001
type: component
asil: B
realizes:
  - SYS-GPTP-001
  - SYS-GPTP-002
allocates_to:
  - QNX:KryoP0
interfaces:
  provides:
    - TimeBaseStatusService
  requires:
    - EthTsnDriverIf
description: |
  gPTP time-base provider (ara::tsync daemon). Runs BMCA, synchronizes the local
  clock to the grandmaster, applies drift-compensated holdover on sync loss, and
  publishes time-base status. Failure behaviour: on 3 missed Syncs enters holdover,
  publishes kUncertain, raises DTC_GPTP_SYNC_LOSS.
tags: [gptp]
---

**ARC-GPTP-001 — TimeBase Provider**

---
id: ARC-GPTP-002
type: interface
asil: B
realizes:
  - SYS-GPTP-002
description: |
  TimeBaseStatusService ara::com service — carries time-base state
  (kSynchronized/kUncertain/kUnavailable) and holdover budget to all time consumers.
  E2E-protected (P04 events). Full definition per ara-com-interfaces instructions.
tags: [gptp, interface]
---

**ARC-GPTP-002 — TimeBaseStatusService**

---
id: ARC-HTP-001
type: component
asil: B
realizes:
  - SYS-HTP-001
allocates_to:
  - QNX:KryoE0
interfaces:
  provides:
    - InferenceDeadlineSupervisorIf
  requires:
    - FastRpcSessionIf
description: |
  HTP inference deadline supervisor. Arms a watchdog per DLC inference dispatched to
  the Hexagon, detects deadline overruns and signals violations to the degradation
  manager within the budgeted reaction time. Failure behaviour: supervisor loss is
  detected by the SAIL health monitor via missing heartbeat.
tags: [htp, deadline]
---

**ARC-HTP-001 — Inference Deadline Supervisor**

Notes:
- The QM inference execution itself (Hexagon) is a separate QM element — supervision
  and execution are split so the ASIL-B monitor never lands on the QM target.
- SAIL-side supervision elements (`SAIL:SafeRTOS`, up to ASIL-D) follow the same
  pattern; cross-domain heartbeat is a raw-protocol interface element, not ara::com.
