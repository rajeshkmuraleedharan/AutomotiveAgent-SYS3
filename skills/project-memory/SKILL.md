# Skill — Project Memory

Skill for accumulating and applying project experience across sessions.
Memory lives in `project-context/` and compounds: the agent gets better at Rajesh's
project the more it is corrected and the more decisions it records.

## Read-before-write (every task)

At the start of any requirements / architecture / concept / analysis task:

1. Read `project-context/conventions.md` — hard conventions, always apply
2. Scan `project-context/LEARNINGS.md` for entries touching the feature at hand
3. Check `project-context/decisions/` for ADRs that constrain the design space
4. Check `imports/normalized/manifest.md` for recent tool state on the topic
5. Check the relevant `wiki/topics/{slug}.md` for the current compiled state
   (subsystem facts, open questions, known bugs) before re-deriving from raw imports
   or `knowledge-base/` from scratch — see `rules/wiki-rules.md`

An output that contradicts an Accepted ADR or a convention is wrong unless Rajesh
explicitly overrides it — then record the override as a new learning/ADR.

## When to record

| Trigger | Record as |
|---------|-----------|
| Rajesh corrects generated output | LEARNINGS entry (`correction`) |
| Review feedback (internal review, CB findings) | LEARNINGS entry (`review-feedback`) |
| A recurring pattern ("we always…") | promote to `conventions.md` |
| A design/process decision with lasting consequences | ADR in `decisions/` |
| Imported Confluence decision page | ADR (extracted, source-linked) |
| A novel, durable fact about subsystem state — analysis produced it, not existing wiki content ("what's true", not "how to work") | `wiki/topics/{slug}.md` Current State + History (see `rules/wiki-rules.md`, `/wiki-update`) |

## Entry formats

- LEARNINGS: `## YYYY-MM-DD — {category}` + 1–3 self-contained bullets + `Source:` line;
  append-only, never rewrite history
- ADR: copy `decisions/ADR-000-template.md`, next free number, ≤ 20 lines
- Superseding: new ADR marks the old one `Superseded by ADR-NNN` — don't delete

## Hygiene

- Don't record what the repo already encodes (schema, rules, KB content)
- One fact per bullet; no session-specific context ("as discussed above")
- Sanitization rules of `project-context/internal-docs/README.md` apply to all memory
