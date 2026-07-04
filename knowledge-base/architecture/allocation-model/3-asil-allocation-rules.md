# ASIL Allocation Rules

## Hard rules (validator-enforced)

1. Element ASIL ≤ target ceiling: KryoP/KryoE = B, SafeRTOS = D, Hexagon/Adreno = QM
2. Element ASIL = max ASIL of realized requirements, unless a documented ASIL
   decomposition applies (`decomposition:` field + @safety-analyst sign-off)
3. `component` elements always carry `allocates_to`

## Decomposition rules (ISO 26262-9)

- Decomposition pairs need **independence** — different targets, no shared single
  point of failure (e.g. B(D) on QNX:KryoP0 + B(D) on SAIL:SafeRTOS is plausible;
  two elements on the same QNX partition is not)
- Confirmation: the decomposed pair plus its comparator/voter is reviewed by
  @safety-analyst and captured as an ADR
- Record decomposition in the element block:
  `decomposition: "ASIL B(D) with ARC-XXX-NNN; ADR-NNN"`

## Typical patterns on SA8620P

| Need | Pattern |
|------|---------|
| ASIL-D function | SAIL-only, or QNX(B) + SAIL(B) decomposition with SAIL-side enforcement |
| ASIL-B perception chain | QM inference (Hexagon) + ASIL-B supervision (KryoE) + plausibility at consumer |
| Network-dependent safety data | E2E protection + timeout at consumer; network HW stays QM/uncommitted |

## Review triggers

- Any ASIL ≥ A element on Hexagon/Adreno → automatic error
- ASIL lowered vs. realized requirements without `decomposition:` → warning, review required
- Monitor and monitored element on the same target → finding (independence)
