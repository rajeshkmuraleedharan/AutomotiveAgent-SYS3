---
name: Verification Criteria
description: Write or improve verification criteria for one or more SYS.3 requirements. Ensures criteria are measurable, conditioned, and tied to a specific verification method.
---

Write or improve **verification criteria** for the following SYS.3 requirement(s).

## Input

Paste the requirement(s) here:

```
[PASTE REQUIREMENT(S) HERE]
```

## Requirements for Good Criteria

- Measurable: numeric threshold with unit (µs, ms, %, °C, count)
- Conditioned: operating conditions specified (temperature, load, duration)
- Statistical: confidence level or sample size (3σ, 95th percentile, N ≥ N)
- Method-matched: TEST for timing/accuracy; ANALYSIS for coverage targets; INSPECTION for configuration

## Output

For each requirement, produce:

1. **Improved `verification_criteria` block** (ready to paste into YAML)
2. **Verification method** (`TEST` / `ANALYSIS` / `INSPECTION` / `DEMONSTRATION`)
3. **Test approach** — 1–2 sentences on how to actually measure it

## Examples

### gPTP offset criterion:
```
The local time-base offset to the gPTP grandmaster shall be ≤ 1 µs (3σ)
measured over a 24-hour soak at –40 °C and +85 °C with nominal network load.
```
Method: TEST | Approach: hardware timestamping via Marvell 88Q5050, logged by ara::tsync.

### BIST coverage criterion:
```
SPFM for HW_Watchdog_Task shall be ≥ 99% as demonstrated by FMEDA
per QC-SA8620P-SM §[TBD] and PBIST report at end-of-line test.
```
Method: ANALYSIS | Approach: FMEDA document review + PBIST pass rate from manufacturing test.
