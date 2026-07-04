---
name: Architecture Interface
description: Define an ara::com service interface (or QNX↔SAIL raw protocol interface) with E2E and SOME/IP deployment notes.
---

Define a **service interface** for the SA8620P platform.

## Inputs (ask if missing)

- Provider ARC element (or feature, if the element doesn't exist yet)
- Data/operations to be exposed and their consumers
- ASIL of the carried data

## Steps

1. Decide the interface kind:
   - Adaptive app ↔ Adaptive app on QNX → **ara::com service**
     (`ara-com-interfaces.instructions.md`)
   - QNX ↔ SAIL → **raw protocol interface element** (explicit transport, no ara::com)
2. Produce the canonical service definition: attribute table (instance specifier,
   `0x[TBD]` SOME/IP IDs, version, ASIL, E2E profile) + Events / Methods / Fields tables
3. Add deployment notes: VLAN/PCP priority, cycle times, bandwidth estimate for TSN
   planning on the 88Q5050
4. Update or emit the provider/consumer ARC blocks (`interfaces.provides/requires`)
5. State which SYS-* requirements the interface realizes; E2E profile is mandatory
   for ASIL ≥ A data
6. Run `commands/arch/validate-arch.sh` on emitted ARC blocks

Never invent concrete SOME/IP service IDs — use `0x[TBD]` until the internal registry assigns them.
