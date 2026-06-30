# SYS.3 Requirements Workflow

ASPICE SYS.3 process flow for the SA8620P ADAS platform.

## Full Flow

```
HARA (SYS.1)
    │  hazardous events, S/E/C → ASIL, safety goals
    ▼
Safety Goals → FSR
    │  @safety-analyst: derive Technical Safety Requirements
    ▼
SYS.3 Requirements (this repo)
    │  @sys3-requirements-engineer: draft per topic
    │  @requirements-reviewer: review for ASPICE + CB compliance
    │  → Import to Codebeamer, status = Approved
    ▼
FMEA / FMEDA
    │  @safety-analyst: safety mechanism coverage analysis
    │  → SPFM/LFM evidence documented
    ▼
SWE.1 Requirements
    │  (downstream from SYS.3 — out of scope for this repo)
    ▼
Code + Unit Tests
    │  (implementation — out of scope for this repo)
```

## Three-Topic Workflow

### gPTP TimeSync

1. Identify grandmaster placement and network topology
2. Draft requirements: `/sys3-gptp`
3. Review: `/req-review`
4. Import to CB tracker, trace to STK-NET-* requirements

### HTP Orchestration

1. Define DLC model inventory and inference deadlines
2. Draft requirements: `/sys3-htp`
3. Review: `/req-review`
4. Import to CB tracker, trace to stakeholder AI/perception requirements

### Technical Safety Concept

1. Confirm safety goals and FSRs from HARA output
2. Derive TSRs: `/sys3-safety` or `@safety-analyst`
3. Review: `/req-review`
4. FMEDA analysis with `@safety-analyst`
5. Import to CB tracker, trace to FSR-TSC-* requirements

## Baseline Management

- Requirements baseline: cut when all SYS.3 requirements are `Approved`
- Baseline triggers SWE.1 start
- Post-baseline changes require formal CR in Codebeamer
