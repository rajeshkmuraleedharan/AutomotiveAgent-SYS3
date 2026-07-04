---
name: Concept Feature
description: Draft a feature concept or operating concept (CON-*) that later seeds SYS.2 requirements.
---

Draft a **feature concept** (or **operating concept**) for the given topic.

## Inputs (ask if missing)

- Topic + which template: feature concept | operating concept
- Stakeholder input: JIRA stories, Confluence pages (check `imports/normalized/`),
  or a described need

## Steps

1. Consult `project-context/` (conventions, ADRs, LEARNINGS) and
   `knowledge-base/architecture/` for platform constraints
2. Reserve an ID: `generate-req-id.py --prefix CON --topic {FEATURE}`
3. Fill the matching template from `concept-templates.instructions.md` — completely:
   - Need must be solution-independent
   - every open point gets owner + due date
   - operating concepts include the mermaid state diagram and degradation ladder
4. End with **Candidate requirements** — SYS.2 seeds with preliminary ASIL guesses,
   each traceable back to this concept ID
5. Check against `rules/concept-rules.md`; flag anything that contradicts an
   Accepted ADR instead of silently deviating
6. Offer `/record-learning` if the session settled a decision
