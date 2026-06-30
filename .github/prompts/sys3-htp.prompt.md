---
name: SYS.3 HTP Orchestration Requirements
description: Generate ASPICE SYS.3 system requirements for HTP Orchestration on the SA8620P platform in Codebeamer-compatible YAML format.
---

Generate **SYS.3 system requirements** for **HTP Orchestration** on the SA8620P ADAS platform.

## Context

Platform: Qualcomm SA8620P | QNX 8.0 | Hexagon HTP | SNPE/QNN runtime | FastRPC
HTP supervisor ASIL: B (QNX:KryoP0) | Hexagon ASIL: QM (supervised by ASIL-B element)
Output: Codebeamer-compatible YAML attribute blocks + SHALL statements

## Coverage Areas

Cover at least the following areas:
1. DLC model lifecycle — load, warm-up, run, unload; version management
2. Inference deadline — ≤ 100 ms (95th percentile), ara::phm DeadlineSupervision
3. OOD detection — score > 0.7 → degraded mode trigger
4. SMMU isolation — Hexagon DMA bounded; no access to SAIL TCM
5. FastRPC — error handling, timeout, channel lifecycle
6. Thermal / resource — DDR bandwidth cap, throttle policy

## Output Format

```yaml
---
id: SYS-HTP-NNN
level: SYS.3
asil: B             # supervisor element; Hexagon accelerator is QM
source: []
verification: TEST
verification_criteria: |
  [Measurable criterion with units, conditions, confidence]
rationale: |
  [Design constraint or safety argument]
references:
  - QC-SA8620P-TRM §TBD
  - QC-HEXAGON-SM §TBD
safety_mechanism: |
  [How overruns or isolation violations are detected and handled]
allocates_to: [QNX:KryoP0, QNX:Hexagon]
tags: [htp, hexagon, orchestration]
---

**SYS-HTP-NNN — [Title]**

The system shall [requirement text].
```

Generate 6–10 requirements starting from the next available ID.
