# Skill — System Architecture Design

Skill for SYS.3 architecture work on the SA8620P ADAS platform: decomposition,
views, interfaces, and allocation. Complements `sys3-authoring` (requirements) —
architecture is only ever created against existing SYS-* requirements.

## Capabilities

1. **ARC element decomposition** — canonical YAML blocks
   (`architecture-schema.instructions.md`): id, type, asil, realizes, allocates_to,
   interfaces, description
2. **Static views** — mermaid `graph`, ≤ 12 elements, ASIL annotated, containment as
   subgraphs, caption naming viewpoint + addressed requirements
3. **Dynamic views** — mermaid `sequenceDiagram` / `stateDiagram-v2`; standard scenarios:
   - startup ordering (gPTP synchronized before ADAS FunctionGroup activation)
   - degradation ladder (kSynchronized → kUncertain → kUnavailable and feature shedding)
   - fault reaction (detection → DTC → degraded mode entry, with timing budget)
4. **ara::com interfaces** — service definition tables incl. E2E profile and SOME/IP
   deployment (`ara-com-interfaces.instructions.md`)
5. **Allocation matrices** — SYS-* → ARC-* → target tables, ASIL-ceiling conflicts flagged

## ID Convention

| Artefact | Prefix | Example |
|----------|--------|---------|
| Architecture element | `ARC-{AREA}` | `ARC-GPTP-003` |
| AREA vocabulary | same as SYS IDs | GPTP, HTP, TSC, plus new areas as they appear |

Generate: `python scripts/generate-req-id.py --prefix ARC --topic GPTP`

## Quality Checklist

- [ ] Every element `realizes:` ≥ 1 existing SYS-* requirement
- [ ] Element ASIL = max of realized requirements (or documented decomposition)
- [ ] No ASIL ≥ A element on a QM target (`QNX:Hexagon`, `QNX:Adreno`)
- [ ] Every `component` has `allocates_to`
- [ ] Every `requires` interface has a `provides` counterpart somewhere
- [ ] QNX ↔ SAIL interfaces are raw-protocol elements, never ara::com
- [ ] `commands/arch/validate-arch.sh` passes
- [ ] No Classic AUTOSAR concepts

## Validation

`scripts/validate-architecture.py` checks structure, ID grammar, realizes-resolution
against the repo's SYS-* population, allocation ceilings, and ASIL inheritance.
