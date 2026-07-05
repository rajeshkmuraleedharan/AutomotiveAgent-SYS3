# Wiki Rules

Rules for `wiki/` — compiled subject-matter memory synthesized from `imports/normalized/`.

## What the Wiki Is NOT

| Not this | Because |
|---|---|
| A copy of `imports/normalized/` | That's the immutable transcript; wiki is the synthesis |
| A copy of `knowledge-base/` | That's static human-authored reference; wiki is live project state |
| A copy of `project-context/decisions/` | Wiki links ADRs, never restates them |
| Per-requirement or per-issue pages | Duplicates `imports/normalized/`; wiki is topic-level |

## Page Granularity

- One page per existing AREA/topic slug (matches `knowledge-base/features/{slug}/`
  and the `SYS-{AREA}`/`ARC-{AREA}` vocabulary) — start with gptp-timesync,
  htp-orchestration, technical-safety-concept
- New topic page created only when an import references a JIRA Component or
  requirement AREA with no existing page — never split a page pre-emptively
- Split rule (staleness/bloat trigger, not upfront): if a topic page's Current State
  section exceeds ~15 bullets or mixes 2+ unrelated failure domains, `/wiki-lint`
  flags it as a split candidate; a human decides the split, the tool never
  auto-splits
- No entity sub-layer (no per-component or per-person pages) until a topic page's
  Cross-References section becomes unusable for grep — YAGNI

## Ingest vs Update Decision

| New import contains... | Action |
|---|---|
| A SYS-*/ARC-*/CON-* ID matching an existing topic's AREA | Update that topic's Current State + Cross-References + History |
| A JIRA issue with Components matching an existing topic | Same |
| A JIRA issue/requirement with no matching topic | Create new topic page; add row to `wiki/index.md` |
| A fact that contradicts an existing Current State bullet | Do NOT silently overwrite — rewrite the bullet AND add a History line noting the contradiction and which import resolved it |

## Staleness and Contradiction Definitions (for `/wiki-lint`)

- **Stale bullet**: a Current State claim whose only supporting source import is
  superseded by a later import batch touching the same ID, but the bullet wasn't
  updated — mechanically detectable by comparing Cross-References source dates
  against `imports/normalized/manifest.md`
- **Stale page**: no History entry despite `imports/normalized/manifest.md` showing
  new batches referencing that topic's AREA/Components — mechanically detectable
- **Contradiction**: two Current State bullets (same page or across pages) making
  incompatible claims about the same ID or subsystem behavior — requires LLM
  judgment, not mechanical
- **Orphan page**: topic page with no inbound reference from any other page's
  Cross-References and no ingest activity for a long stretch — candidate for an
  archival note in `index.md`, never silent deletion

## Precedence

Same precedence chain as `project-context/` (locked schemas and `rules/*.md` outrank
everything). Wiki content is informative synthesis, never authoritative over
`imports/normalized/` (which carries the real IDs/wording) or over `project-context/`
(which governs agent behavior). If wiki content conflicts with a Current State
bullet, `imports/normalized/` wins and the bullet must be corrected.
