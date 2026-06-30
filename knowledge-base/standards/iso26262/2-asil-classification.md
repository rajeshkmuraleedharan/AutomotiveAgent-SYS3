# ISO 26262 — ASIL Classification

## ASIL = f(Severity × Exposure × Controllability)

| Parameter | Levels |
|-----------|--------|
| Severity (S) | S0 (no injury) → S3 (life-threatening) |
| Exposure (E) | E0 (improbable) → E4 (high probability) |
| Controllability (C) | C0 (controllable) → C3 (difficult to control) |

## ASIL Assignment Table

| S | E | C | ASIL |
|---|---|---|------|
| S3 | E4 | C3 | D |
| S3 | E4 | C2 | C |
| S3 | E3 | C3 | C |
| S2 | E4 | C3 | B |
| S2 | E3 | C3 | A |
| S1 | any | any | A or QM |

## TODO: Add complete ASIL matrix table from ISO 26262-3 Table 4
