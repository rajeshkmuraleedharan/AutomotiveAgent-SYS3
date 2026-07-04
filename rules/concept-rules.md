# Concept Rules

Rules for every concept document (CON-*) in AutomotiveAgent-SYS3.

## Ordering Rules

- Concepts precede requirements: no SYS.2/SYS.3 authoring for a feature whose concept
  has open points marked blocking
- The Need section is solution-independent — solution words in the Need are findings
- Agreed concepts feed SYS.2 `source:` entries as `CON-{FEATURE}-NNN`

## Identification Rules

- Format: `CON-{FEATURE}-{NNN}`; FEATURE is a short A–Z/0–9 name (HOLDOVER, DEGLADDER…)
- Generate via `generate-req-id.py --prefix CON --topic {FEATURE}`
- Status lifecycle: `Draft → In Review → Agreed`; superseded concepts marked, not deleted

## Trade Study Rules

- ≥ 2 real options — options nobody would pick are findings, not options
- Mandatory criteria: safety impact, QNX/SafeRTOS partitioning cost, TSN bandwidth/latency
- Weights sum to 100 and each weight has a one-line justification
- Sensitivity check mandatory; a flipping winner means the study is not decision-ready
- Decided studies produce an ADR (`/record-learning`) and follow-up candidates

## Open Point Rules

- Every open point has an owner and a due date — "TBD/someone/later" is not an open point
- Blocking open points are marked; they gate requirement authoring for that area

## Platform Rules

- Classic AUTOSAR options are out of scope and do not appear as trade-study options
- Concepts touching cross-domain behaviour state the QNX ↔ SAIL boundary explicitly
