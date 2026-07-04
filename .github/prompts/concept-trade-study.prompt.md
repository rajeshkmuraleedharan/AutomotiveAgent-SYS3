---
name: Concept Trade Study
description: Run a weighted trade study between design options, with mandatory safety/partitioning/TSN criteria and a sensitivity check.
---

Run a **trade study** for the given design question.

## Inputs (ask if missing)

- The question (one sentence, one decision)
- Candidate options (≥ 2 real ones; ask for more context if only one is real)
- Any fixed constraints (cost cap, reuse mandate, timeline)

## Steps

1. Consult `project-context/decisions/` — if an Accepted ADR already answers the
   question, stop and cite it
2. Reserve an ID: `generate-req-id.py --prefix CON --topic {FEATURE}`
3. Build the study per `concept-templates.instructions.md`:
   - Options: 2–4, each with vendor/standard citations; no Classic AUTOSAR options
   - Criteria: mandatory three (safety impact, QNX/SafeRTOS partitioning cost,
     TSN bandwidth/latency) + feature-specific; weights sum to 100, each justified
   - Score matrix 1–5 with a one-line justification per score
   - Sensitivity: shift the top weight ±10 % and report whether the winner flips
4. Recommendation with risks and follow-ups (candidate requirements, ARC impacts,
   proposed JIRA tickets with `NEW-` keys)
5. If Rajesh accepts the recommendation → `/record-learning` to create the ADR
