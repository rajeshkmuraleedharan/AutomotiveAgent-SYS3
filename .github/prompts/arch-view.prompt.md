---
name: Architecture View
description: Generate a static or dynamic architecture view (mermaid + ARC element blocks) for a feature on the SA8620P platform.
---

Generate an **architecture view** for the given feature on the SA8620P ADAS platform.

## Inputs (ask if missing)

- Feature/area (e.g. gPTP TimeSync, HTP Orchestration)
- View type: **static** (decomposition) or **dynamic** (startup | degradation | fault reaction | mode change)
- Driving requirements (SYS-* IDs) — check `imports/normalized/codebeamer/` and the
  KB requirement banks for the current population

## Steps

1. Consult `project-context/` (conventions, ADRs) and `knowledge-base/architecture/`
2. List the SYS-* requirements the view addresses; if the feature has none, stop and
   propose requirements instead
3. Produce:
   - ARC element YAML blocks for every element in the view (schema:
     `architecture-schema.instructions.md`; IDs via `generate-req-id.py --prefix ARC`)
   - One mermaid diagram (`graph TD` for static; `sequenceDiagram`/`stateDiagram-v2`
     for dynamic), ≤ 12 elements, ASIL annotations, timing budgets where quantified
   - A one-line caption: viewpoint, concern, addressed SYS-* IDs
4. Run `commands/arch/validate-arch.sh` on the result and fix findings
5. Flag open points (unassigned interfaces, TBD allocations) at the end

Platform constraint: Classic AUTOSAR is out; QNX ↔ SAIL is raw protocol, not ara::com.
