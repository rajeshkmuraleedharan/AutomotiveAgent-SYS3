# Skill — Concept Development

Skill for the pre-requirements phase: feature concepts, operating concepts, and trade
studies for the SA8620P ADAS platform. Concepts come **before** requirements and feed
SYS.2 `source:` entries; the Technical Safety Concept keeps its existing home
(`knowledge-base/features/technical-safety-concept/`) — no duplication here.

## Artefact types

| Artefact | Purpose | Template |
|----------|---------|----------|
| Feature concept | need → function → constraints → open points | `concept-templates.instructions.md` |
| Operating concept | modes, states, driver interaction, degradation ladder | same |
| Trade study | option selection with weighted criteria | same |

## ID Convention

- `CON-{FEATURE}-NNN`, generated via `generate-req-id.py --prefix CON --topic {FEATURE}`
- Concepts are markdown documents, NOT YAML requirement blocks
- When a concept matures, its "Candidate requirements" section seeds SYS.2 items whose
  `source:` cites the concept ID

## Trade study method

1. ≥ 2 real options (a strawman option is a finding, not an option)
2. Weighted criteria — mandatory ones for this platform:
   - safety impact (ASIL achievability, independence)
   - QNX/SafeRTOS partitioning cost
   - TSN bandwidth / latency impact
   plus feature-specific criteria (accuracy, BOM cost, effort…)
3. Score matrix (1–5 per criterion, weights sum to 100)
4. Sensitivity note: does the winner change if the top weight shifts ±10 %?
5. Recommendation + risks + follow-ups (ADR via `/record-learning` once decided)

## Quality Checklist

- [ ] Problem stated independent of any solution
- [ ] Platform constraint respected (Classic AUTOSAR out; SAIL = SafeRTOS)
- [ ] Every open point has an owner and a date
- [ ] Candidate requirements listed with target ASIL guesses (marked preliminary)
- [ ] Consulted `project-context/` — no contradiction with Accepted ADRs
- [ ] Trade studies: mandatory criteria present, sensitivity checked
