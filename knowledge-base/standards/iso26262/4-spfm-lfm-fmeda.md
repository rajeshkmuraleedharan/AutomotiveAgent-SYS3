# ISO 26262 — SPFM, LFM, and FMEDA

## Definitions

- **SPFM** (Single-Point Fault Metric): fraction of single-point faults that are covered by safety mechanisms
- **LFM** (Latent Fault Metric): fraction of latent multi-point faults that are covered
- **FMEDA**: Failure Mode Effects and Diagnostic Analysis — the analysis method

## Targets per ASIL

| ASIL | SPFM | LFM |
|------|------|-----|
| D | ≥ 99% | ≥ 90% |
| C | ≥ 97% | ≥ 80% |
| B | ≥ 90% | ≥ 60% |
| A | ≥ 60% | — |

## SA8620P Evidence Sources

- `QC-SA8620P-SM` — PBIST/CBIST coverage data for SAIL and Kryo
- Vendor FMEDA report (TBD)

## TODO: Add FMEDA calculation methodology
