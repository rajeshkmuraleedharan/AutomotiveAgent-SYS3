# Allocation Bank — Reference Matrices

Reusable allocation matrix examples (format used by `/arch-allocation`).

## Example: gPTP TimeSync

| SYS-* | ASIL | Realized by (ARC-*) | Allocated target | Ceiling OK? |
|-------|------|---------------------|------------------|-------------|
| SYS-GPTP-001 | B | ARC-GPTP-001 | QNX:KryoP0 | ✓ (B ≤ B) |
| SYS-GPTP-002 | B | ARC-GPTP-001, ARC-GPTP-002 | QNX:KryoP0 / (interface) | ✓ |

Findings format (always after the table):

- **Coverage gap**: `SYS-XXX-NNN realized by no element` → propose element
- **Ceiling violation**: `ARC-XXX-NNN (ASIL-B) on QNX:Hexagon (QM)` → re-allocate or split
- **Inheritance gap**: `ARC-XXX-NNN ASIL A < max realized B, no decomposition` → decompose or raise
- **CB inconsistency**: requirement's `allocates_to` in Codebeamer differs from
  architecture → align tracker or architecture, record decision

## Example: HTP supervision split

| SYS-* | ASIL | Realized by | Allocated target | Ceiling OK? |
|-------|------|-------------|------------------|-------------|
| SYS-HTP-001 | B | ARC-HTP-001 (supervisor) | QNX:KryoE0 | ✓ (B ≤ B) |
| (inference itself) | QM | ARC-HTP-002 (executor, QM) | QNX:Hexagon | ✓ (QM) |

The QM executor element realizes the functional (QM) requirements of the model
pipeline; the ASIL-B supervisor realizes the safety requirement. This split is the
canonical SA8620P pattern for accelerator workloads.
