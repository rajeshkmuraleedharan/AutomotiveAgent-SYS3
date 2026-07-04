# Architecture Rules

Rules for every ARC element and view in AutomotiveAgent-SYS3.

## Identification Rules

- Format: `ARC-{AREA}-{NNN}`; AREA shares the SYS vocabulary (GPTP, HTP, TSC, …)
- NNN zero-padded, never reused; generate via `generate-req-id.py --prefix ARC`
- One YAML block per element; blocks live in `*.architecture.md` files or KB banks

## Traceability Rules

- `realizes:` is mandatory and every entry must resolve to an existing SYS-* requirement
- Architecture without a driving requirement is a finding, not a starting point —
  propose the missing requirement first
- Requirement changes triggered by architecture work go through
  @sys3-requirements-engineer, never inline edits of SYS blocks

## ASIL & Allocation Rules

| Target | ASIL ceiling |
|--------|--------------|
| `QNX:KryoP0` / `QNX:KryoP1` / `QNX:KryoE<n>` | B |
| `SAIL:SafeRTOS` | D |
| `QNX:Hexagon` / `QNX:Adreno` | QM |
| `Hardware:*` | — (not checked) |

- Element ASIL = max ASIL of realized requirements; lower values only with a
  `decomposition:` note and safety-analyst sign-off
- ASIL ≥ A on a QM target is an error, always
- Mixed-ASIL elements are split until each part has one ASIL

## View Rules

- One diagram per viewpoint; ≤ 12 elements; caption = viewpoint + concern + SYS-* IDs
- Dynamic views carry timing budgets on the arrows where a requirement quantifies them
- No whole-platform mega-diagrams

## Interface Rules

- On-SoC Adaptive communication: ara::com services (`ara-com-interfaces.instructions.md`)
- QNX ↔ SAIL: raw protocol interface elements with explicit transport
- Every `requires` must have a `provides` counterpart; unmatched pairs are findings

## Platform Rules

- Classic AUTOSAR is out — no BSW, RTE, SWC compositions, COM signal matrices
- All AUTOSAR is Adaptive on QNX; SAIL runs SafeRTOS only
