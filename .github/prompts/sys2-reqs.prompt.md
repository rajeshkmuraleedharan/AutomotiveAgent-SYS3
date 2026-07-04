---
name: SYS.2 Requirements
description: Generate ASPICE SYS.2 system requirements (stakeholder-derived, solution-free) that later refine into SYS.3.
---

Generate **SYS.2 system requirements** for the given feature on the SA8620P ADAS platform.

## Inputs (ask if missing)

- Feature/topic and the stakeholder input: STK-* items, an Agreed concept
  (CON-*), imported JIRA stories, or a described need
- Target count (default 4–8)

## Steps

1. Consult `project-context/` and any Agreed concept for the feature — its
   "Candidate requirements" section is the natural seed
2. Use the canonical YAML block **unchanged** with `level: SYS.2`
   (`sys2-requirements.instructions.md` for the SYS.2-specific field usage)
3. `source:` cites stakeholder reqs / CON-* / standards — never other SYS items
4. Keep items solution-free: WHAT at system boundary, quantified, one SHALL each;
   no component names, no allocation targets unless stakeholder-pinned
5. IDs from `generate-req-id.py --topic {TOPIC}` (shared number space with SYS.3)
6. Validate with `commands/sys3/validate-schema.sh` and fix findings
7. Close with a traceability preview: which SYS.3 areas will refine each SYS.2 item
