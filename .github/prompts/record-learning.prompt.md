---
name: Record Learning
description: Persist a correction, review finding, convention, or decision into project-context/ so future sessions apply it.
---

Record the given project experience into `project-context/`.

## Steps

1. Classify the input:
   - **Decision with lasting consequences** (chosen option among alternatives, constrains
     future work) → ADR
   - **Correction / review feedback / discovered convention** → LEARNINGS entry
   - **Pattern already recorded 2+ times in LEARNINGS** → also promote a one-liner to
     `conventions.md`
2. For a LEARNINGS entry: append to `project-context/LEARNINGS.md` —
   `## YYYY-MM-DD — {category}`, 1–3 self-contained bullets, `Source:` line.
   Never edit existing entries.
3. For an ADR: copy `project-context/decisions/ADR-000-template.md` to the next free
   `ADR-NNN-{slug}.md`, fill Context / Decision / Consequences (≤ 20 lines),
   status `Accepted` unless told otherwise.
4. Apply the sanitization rules from `project-context/internal-docs/README.md`.
5. Confirm back: what was recorded, where, and one line on how it will change future
   output. If it contradicts an existing ADR/convention, flag the conflict instead of
   recording both.
