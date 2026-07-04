---
name: Architecture Allocation
description: Build a SYS-* → ARC-* → execution-target allocation matrix and flag ASIL/target conflicts.
---

Build a **requirement-to-element allocation matrix** for the given scope.

## Inputs (ask if missing)

- Scope: a feature (all its SYS-* IDs) or an explicit SYS-* ID list
- Current ARC population (scan `*.architecture.md`, KB banks, and prior outputs)

## Steps

1. Collect the requirements: repo content + latest Codebeamer imports
   (`imports/normalized/codebeamer/`) — imports are authoritative for status
2. Produce the matrix:

   | SYS-* | ASIL | Realized by (ARC-*) | Allocated target | Ceiling OK? |
   |-------|------|---------------------|------------------|-------------|

3. Flag, in a findings list after the table:
   - requirements realized by **no** element (coverage gap)
   - elements whose target violates the ASIL ceiling (KryoP/E = B, SafeRTOS = D,
     Hexagon/Adreno = QM)
   - element ASIL lower than the max of its realized requirements without a
     documented decomposition
   - requirements allocated in Codebeamer (`allocates_to`) inconsistently with the
     architecture
4. Propose concrete fixes for each finding (new element, re-allocation, decomposition
   with @safety-analyst review)
5. Cross-check with `commands/arch/validate-arch.sh`
