# Safety Requirement Rules

ISO 26262 compliance rules for SYS.3 safety requirements on SA8620P.

## ASIL Allocation Rules

| Rule | Details |
|------|---------|
| ASIL-D cannot be allocated to QNX alone | Must decompose: QNX ASIL-B + SAIL ASIL-B |
| ASIL-B max on QNX:KryoP0 | QNX 8.0 ceiling is ASIL-B |
| QM on Hexagon/Adreno | Accelerators are QM; supervisor on QNX:KryoP0 is ASIL-B |
| ASIL-D max on SAIL:SafeRTOS | Certified ASIL-D; watchdog, GPIO, BIST |
| ASIL-D max on Hardware:PMIC | Safety rail monitoring |

## Safety Mechanism Rules

- Every ASIL ≥ A requirement MUST have `safety_mechanism` field populated
- Safety mechanism must specify: mechanism type, detection latency, DTC name
- Mechanism and monitored function must be on independent elements (no shared failure mode)
- DC class must be consistent with ISO 26262-5 Table D.1

## SPFM / LFM Rules

- SPFM and LFM values must cite the FMEDA source document (`QC-SA8620P-SM §TBD`)
- Do not state SPFM/LFM targets without evidence reference
- Hardware watchdog: DC = High (≥ 99%) per ISO 26262-5
- CBIST concurrent: DC = Medium–High (vendor-specified)

## Traceability Rules

- Every TSR must trace to a FSR (`source: [FSR-TSC-NNN]`)
- Every FSR must trace to a safety goal (`source: [SG-NNN]`)
- Safety goals must be HARA-derived
- ASPICE flow: HARA → Safety Goals → FSR → TSR (SYS.3) → SWE.1

## BIST Rules

- PBIST must complete at power-on before ADAS FunctionGroup activates
- PBIST failure must assert safe-state GPIO and set DTC_SAIL_PBIST_FAIL
- CBIST must run concurrently without disrupting QNX operations
- OBIST on-demand must be triggerable via UDS service 0x31

## Anti-Patterns

- ❌ `safety_mechanism` blank on ASIL-B requirement
- ❌ ASIL-D `allocates_to: [QNX:KryoP0]` without SAIL counterpart
- ❌ Stating SPFM ≥ 99% without FMEDA source
- ❌ Reusing ASIL-B element as both monitored and supervisor (destroys independence)
- ❌ ADAS FunctionGroup start before PBIST result confirmed
