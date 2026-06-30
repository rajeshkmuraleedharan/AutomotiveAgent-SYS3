---
name: SYS.3 Technical Safety Requirements
description: Generate ASPICE SYS.3 Technical Safety Requirements (TSR) for the SA8620P platform — covering safety mechanisms, ASIL decomposition, BIST, watchdog, and safe state.
---

Generate **SYS.3 Technical Safety Requirements (TSR)** for the SA8620P ADAS platform.

## Context

Platform: Qualcomm SA8620P | QNX 8.0 (ASIL-B) + SafeRTOS on SAIL (ASIL-D)
Standard: ISO 26262:2018
ASIL pattern: ASIL-D → QNX ASIL-B + SAIL ASIL-B (independence via MPU/SMMU/physical isolation)
Output: Codebeamer-compatible YAML attribute blocks + SHALL statements

## Coverage Areas (specify which to cover)

1. Watchdog — HW_Watchdog_Task timeout ≤ 5 ms, safe-state GPIO
2. Heartbeat — QNX → SAIL protocol, E2E CRC32, 3 missed → safe state
3. BIST — PBIST at boot, CBIST concurrent coverage ≥ TBD%, boot gate
4. ASIL decomposition — independence claims for QNX/SAIL element pairs
5. Safe state — GPIO assertion, FunctionGroup Off, reaction time ≤ 10 ms
6. SPFM/LFM — element-level targets from FMEDA

## Output Format

```yaml
---
id: SYS-TSR-NNN
level: SYS.3
asil: D             # or B depending on element
source:
  - FSR-TSC-NNN
verification: TEST  # or ANALYSIS for SPFM/LFM
verification_criteria: |
  [Measurable criterion — timing in ms, coverage in %, temperature range]
rationale: |
  [ISO 26262 clause + safety goal reference]
references:
  - QC-SA8620P-SM §TBD
  - SRTOS-SM §TBD
safety_mechanism: |
  [The mechanism this requirement itself specifies or depends on]
allocates_to: [SAIL:SafeRTOS]
tags: [tsc, iso26262, asil-d]
---

**SYS-TSR-NNN — [Title]**

The system shall [requirement text].
```

Generate 6–10 requirements. Specify the FSR source IDs if known, or use `FSR-TSC-TBD`.
