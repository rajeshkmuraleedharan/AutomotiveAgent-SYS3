---
name: Wiki Schema
description: "Use when: creating or updating wiki/ topic pages, or deciding whether a new topic page is needed"
applyTo: ["wiki/**"]
---

# Wiki — Page Schema and Conventions

`wiki/` is compiled, continuously-updated subject-matter memory synthesized FROM
`imports/normalized/`. It is distinct from `knowledge-base/` (static reference,
human-authored), `project-context/` (behavioral/process memory), and
`imports/normalized/` (the immutable transcript). Full rules: `rules/wiki-rules.md`.

## Page Sections (mandatory, in this order)

1. **Current State** — rewritten in place as facts change, not appended; each bullet
   cites the ID(s) it's derived from (SYS-*/ARC-*/CON-*/ADAS-*)
2. **Open Questions** — unresolved items surfaced by imports; each self-contained
   with a date raised
3. **Decisions** — links only to `project-context/decisions/ADR-NNN-*.md`; never
   copies ADR content
4. **Cross-References** — flat list of every ID touched: Requirements / Architecture /
   Concepts / JIRA / Source imports
5. **History** — append-only trail, one line per `/wiki-update` run touching this page

## ID Linking

Use existing ID vocabulary only — no new linking scheme: `SYS-{AREA}-NNN`,
`ARC-{AREA}-NNN`, `CON-{FEATURE}-NNN`, `ADAS-NNN` (or the project's actual JIRA prefix).

## Frontmatter

None required on topic pages — they are content, not agent-consumed instructions.
Status and last-updated live in the page body (header line) and in `wiki/index.md`.

## Demo Content

Pages seeded from `imports/samples/*` (rather than real imports) must say so
explicitly in their header line, e.g. `Status: Active (seeded from sample fixtures —
replace as real imports arrive)`.
