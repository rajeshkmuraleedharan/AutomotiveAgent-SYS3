# ADR-001 — Adopt the LLM Wiki pattern for compiled subsystem memory

- **Date:** 2026-07-05
- **Status:** Accepted
- **Category:** tooling

## Context

Offline tool imports (`imports/normalized/`) produced a growing pile of inert,
dated files with nothing synthesizing facts across batches — a JIRA bug and the
requirement it violated sat in separate files with no link between them. Andrej
Karpathy's "LLM Wiki" pattern (see `raw/2026-07-05-karpathy-llm-wiki-pattern.md`)
directly targets this: compile sources once into a maintained, cross-referenced
wiki instead of re-deriving from raw documents every time.

## Decision

Adopted the pattern as a fourth memory layer, `wiki/topics/*.md` — distinct from
`knowledge-base/` (static reference), `project-context/` (behavioral memory), and
`imports/normalized/` (immutable transcript). `/import-normalize` now folds every
import batch into the relevant topic page automatically; `/wiki-lint` auto-fixes
safe mechanical issues and reports semantic ones (contradictions, staleness, gaps)
with source suggestions. Extended to auto-ingest arbitrary external sources
(links/articles/papers) into `raw/`, routed into `wiki/` or `project-context/` per
`rules/wiki-rules.md`.

## Consequences

- New capability: `wiki/`, `raw/`, `scripts/lint-wiki.py`, `/wiki-update`,
  `/wiki-lint`, `.github/instructions/wiki.instructions.md`,
  `.github/instructions/raw-sources.instructions.md`, `rules/wiki-rules.md`
- This very ADR is itself the routing example: a meta/process source (this gist)
  about how the agent should work — not ADAS subsystem content — goes to
  `project-context/decisions/`, not a subsystem wiki topic page
- Follow-up: the three seeded topic pages are demo content from sample fixtures;
  replace with real content as actual imports arrive (tracked in `CLAUDE.md` open items)
