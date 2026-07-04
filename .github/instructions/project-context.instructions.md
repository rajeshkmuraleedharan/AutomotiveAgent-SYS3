---
name: Project Context
description: "Use when: starting any engineering task, or when feedback/decisions should be remembered for future sessions"
applyTo: ["project-context/**"]
---

# Project Context — Usage Rules

`project-context/` is the agent's persistent project memory. Full skill:
`skills/project-memory/SKILL.md`.

## Precedence (highest first)

1. Locked schema + `rules/*.md`
2. `project-context/conventions.md` and Accepted ADRs
3. `project-context/LEARNINGS.md` entries
4. `project-context/internal-docs/` background material
5. Generic knowledge-base content

## Task-start checklist

- [ ] `conventions.md` read
- [ ] `LEARNINGS.md` scanned for the feature/topic at hand
- [ ] Relevant ADRs identified (cite them in output: "per ADR-003")
- [ ] Latest imports checked (`imports/normalized/manifest.md`)

## Task-end

If the session produced a correction, review finding, or decision — offer
`/record-learning` before finishing. Don't silently forget project experience.
