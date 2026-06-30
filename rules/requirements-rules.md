# Requirements Authoring Rules

Rules for every SYS.3 requirement in AutomotiveAgent-SYS3.

## Language Rules

| Rule | Correct | Wrong |
|------|---------|-------|
| Use SHALL for requirements | "The system shall..." | "should", "may", "must" |
| Quantify all constraints | "≤ 1 µs (3σ)" | "low latency", "fast", "adequate" |
| One SHALL per requirement | Split into two reqs | Two conditions in one sentence |
| Active voice | "The system shall detect..." | "Faults shall be detected..." |
| No escape clauses | Remove "where applicable", "if necessary" | |

## Atomicity Rules

- One testable behaviour per requirement
- If a requirement contains "and", evaluate whether it should be split
- Exception: AND joining two conditions that are always tested together

## Identification Rules

- Format: `SYS-{TOPIC}-{NNN}` — `GPTP`, `HTP`, `TSC`, `TSR`
- NNN is zero-padded: `001`, `002`, ...
- Never reuse a retired ID — mark as `[RETIRED]` in the tracker
- ID is immutable after `Approved` status in Codebeamer

## Source Traceability Rules

- Every requirement must have at least one `source` entry
- Acceptable sources: stakeholder requirement ID, standard clause, safety goal ID
- Format: `STK-NET-001`, `IEEE-802.1AS-2020 §6.2`, `SG-001`

## Verification Rules

- `verification_criteria` must include: parameter, threshold, unit, conditions
- TEST requirements need a measurement method (on-target, bench, HIL)
- ANALYSIS requirements need a cited document (FMEDA, safety manual)
- INSPECTION requirements need a reviewable artefact (design doc, config file)
