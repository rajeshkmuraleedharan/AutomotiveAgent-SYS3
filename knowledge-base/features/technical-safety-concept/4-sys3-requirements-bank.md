# TSC — SYS.3 Requirements Bank

Pre-written TSR requirements. Adapt IDs, insert FSR source IDs, import to Codebeamer.

---
id: SYS-TSR-001
level: SYS.3
asil: D
source:
  - FSR-TSC-001
verification: TEST
verification_criteria: |
  The HW_Watchdog_Task shall assert the safe-state GPIO within 10 ms of detecting
  a SAIL task overrun, verified by fault injection on target hardware at +25 °C.
rationale: |
  ISO 26262-4 §6.4.9 — watchdog provides the last-resort safe state.
  10 ms reaction time derived from system-level hazard response time budget.
references:
  - QC-SA8620P-SM §TBD
  - SRTOS-SM §TBD
safety_mechanism: |
  HW_Watchdog_Task (SAIL priority 1, 5 ms kick period);
  GPIO asserted on watchdog timeout or explicit task failure detection.
allocates_to: [SAIL:SafeRTOS]
tags: [tsc, watchdog, safe-state, asil-d]
---

**SYS-TSR-001 — Hardware watchdog safe-state assertion**

The SAIL hardware watchdog shall assert the safe-state GPIO within 10 ms of detecting a SAIL task failure or watchdog timeout, forcing the ADAS FunctionGroup to the Off state.

---
id: SYS-TSR-002
level: SYS.3
asil: B
source:
  - FSR-TSC-001
verification: TEST
verification_criteria: |
  After 3 consecutive missed QNX heartbeat messages (3 × 10 ms = 30 ms),
  the SAIL heartbeat monitor shall assert safe-state GPIO within 5 ms,
  verified by fault injection (QNX heartbeat task killed) on target hardware.
rationale: |
  QNX element failure (ASIL-B part of decomposed ASIL-D) must be detected
  by the independent SAIL element within the system hazard response time budget.
references:
  - SRTOS-USR §TBD
  - QC-SA8620P-SM §TBD
safety_mechanism: |
  SAIL QNX_Heartbeat_Monitor task (10 ms period);
  E2E CRC32 + sequence counter on heartbeat message;
  3 missed or CRC fail → GPIO assertion + DTC_HEARTBEAT_LOSS.
allocates_to: [SAIL:SafeRTOS, QNX:KryoP0]
tags: [tsc, heartbeat, safe-state, asil-b]
---

**SYS-TSR-002 — QNX heartbeat monitoring by SAIL**

The system shall detect loss of QNX-side heartbeat (≥ 3 consecutive missed messages or E2E CRC failure) and assert the safe-state GPIO within 5 ms of detection.

## TODO: Add requirements for PBIST boot gate, CBIST coverage, safe state GPIO spec
