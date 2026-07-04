---
name: Concept Templates
description: "Use when: writing feature concepts, operating concepts, or trade studies for the SA8620P ADAS platform"
applyTo: ["**/concepts/**", "**/*CON-*", "**/*concept*"]
---

# Concept Templates — SA8620P Platform

Concepts are markdown documents (no YAML requirement blocks). IDs: `CON-{FEATURE}-NNN`.
Platform constraint applies everywhere: Classic AUTOSAR is out; all AUTOSAR is Adaptive
on QNX; SAIL runs SafeRTOS only.

## Feature Concept — `CON-{FEATURE}-NNN`

```markdown
# CON-{FEATURE}-NNN — {Title}

| | |
|---|---|
| Status | Draft / In Review / Agreed |
| Date | YYYY-MM-DD |
| Owner | {name} |

## Need
{Stakeholder problem, solution-independent. Cite stakeholder reqs / JIRA stories.}

## Function
{What the feature does. Main function chains, actors, data in/out.}

## Constraints
{Platform, timing, safety, network, power. Cite vendor refs and standards.}

## Interfaces touched
{Existing ARC elements / services affected; new ones anticipated.}

## Open points
| # | Question | Owner | Due |
|---|----------|-------|-----|

## Candidate requirements (SYS.2 seeds — preliminary)
| Candidate | ASIL (prelim.) | Verification idea |
|-----------|----------------|-------------------|
```

## Operating Concept — `CON-{FEATURE}-NNN`

Same header block, then:

```markdown
## Modes and states
{stateDiagram-v2: operating modes incl. degraded modes and safe state}

## Mode transitions
| From | To | Trigger | Budget | Announced to driver? |

## Degradation ladder
{full → degraded → safe; what sheds at each rung; time-base/health triggers}

## Driver interaction
{HMI states, takeover requests, warnings — reference HMI concept if separate}
```

## Trade Study — `CON-{FEATURE}-NNN`

Same header block, then:

```markdown
## Question
{One sentence: what is being decided.}

## Options
### Option A — {name}
{2–4 lines + key vendor/standard citations}
### Option B — {name}

## Criteria & weights (sum = 100)
| Criterion | Weight | Why this weight |
{mandatory: safety impact, QNX/SafeRTOS partitioning cost, TSN bandwidth/latency}

## Score matrix (1–5)
| Criterion (weight) | Option A | Option B |
| **Weighted total** | | |

## Sensitivity
{Does the winner flip if the top weight shifts ±10 %? If yes: say what would settle it.}

## Recommendation
{Option, 2–3 line justification, risks, follow-ups (ADR, requirements, tickets).}
```
