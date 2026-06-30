---
name: SYS.3 gPTP Requirements
description: Generate ASPICE SYS.3 system requirements for gPTP TimeSync on the SA8620P platform in Codebeamer-compatible YAML format.
---

Generate **SYS.3 system requirements** for the **gPTP TimeSync** feature on the SA8620P ADAS platform.

## Context

Platform: Qualcomm SA8620P | QNX 8.0 | Marvell 88Q5050 TSN switch | ara::tsync (Vector MICROSAR Adaptive)
Standard: IEEE 802.1AS-2020
ASIL: B (time-base provider allocated to QNX:KryoP0)
Output: Codebeamer-compatible YAML attribute blocks + SHALL statements

## Coverage Areas

Cover at least the following areas:
1. Time accuracy — offset to grandmaster ≤ 1 µs (3σ)
2. Holdover — behaviour and status after 3 missed sync events
3. Startup — gPTP synchronized before ADAS FunctionGroup activates
4. Status publication — kSynchronized / kUncertain to consumers
5. Safety mechanism — holdover monitor, DTC_GPTP_SYNC_LOSS

## Output Format

For each requirement:

```yaml
---
id: SYS-GPTP-NNN
level: SYS.3
asil: B
source: []
verification: TEST
verification_criteria: |
  [Measurable criterion with units, conditions, confidence]
rationale: |
  [Standard clause or design constraint]
references:
  - MRVL-88Q5050-DS §TBD
  - VEC-MSR-ADAPT-TSYNC §TBD
safety_mechanism: |
  [Detection mechanism and system response]
allocates_to: [QNX:KryoP0, Hardware:88Q5050]
tags: [gptp, ieee802-1as]
---

**SYS-GPTP-NNN — [Title]**

The system shall [requirement text].
```

Generate 6–10 requirements starting from the next available ID (ask if unknown).
