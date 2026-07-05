# Wiki Rules

Rules for `wiki/` — compiled subject-matter memory synthesized from
`imports/normalized/` (offline tool exports) and `raw/` (live-fetched external
sources — links, articles, papers; see `raw-sources.instructions.md`).

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

## Raw Source Routing (for auto-ingested links/articles/papers)

A fetched `raw/` source is not automatically wiki content — route it first:

| Source is about... | Route to |
|---|---|
| A subsystem topic (protocol specs, standards, vendor docs, papers on gPTP/HTP/TSC/etc.) | Fold into the matching (or new) `wiki/topics/{area}.md`, same as a tool import |
| How the agent/tooling itself should work (patterns, workflows — not ADAS subject matter) | `project-context/` (LEARNINGS entry or ADR via `/record-learning`), never a subsystem wiki page |
| General engineering reference with no clear subsystem fit | `wiki/topics/general-references.md` (catch-all, created on first use, same 5-section schema) |

The `raw/` file itself is never deleted or rewritten once routed — it's the
immutable source of record; the wiki page cites it in Cross-References.

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

## Auto-Fix Categorization (for `/wiki-lint --fix`)

Only genuinely mechanical, no-information-loss findings may be auto-applied.
Everything else is always proposed, never silently applied.

| Finding | Auto-fixable? | Why |
|---|---|---|
| Topic page exists but missing from `wiki/index.md` | Yes | Adding an index row loses nothing and is unambiguous |
| `Last updated` date behind the page's own latest History line | Yes | The date is derivable from the page's own content |
| Dangling ID reference (typo or removed ID) | No | Could be a real error in the source content — needs a human/LLM decision on which is right |
| Dangling ADR link | No | Same — don't guess which ADR was meant |
| Contradiction, content-drift staleness, stale Open Questions | No | Semantic judgment required by definition |
| Bloat/split candidate | No | Splitting is a structural decision, always human-confirmed |

When `/wiki-lint` finds gaps (a topic with thin Cross-References, an Open Question
unresolved across many cycles, an area with no wiki content at all despite active
imports), it should suggest concrete new sources to close the gap (e.g. "no vendor
doc covers ARC-GPTP-003's TSN deployment — look for the 88Q5050 datasheet section on
egress scheduling") rather than only reporting the gap.

## Precedence

Same precedence chain as `project-context/` (locked schemas and `rules/*.md` outrank
everything). Wiki content is informative synthesis, never authoritative over
`imports/normalized/` (which carries the real IDs/wording) or over `project-context/`
(which governs agent behavior). If wiki content conflicts with a Current State
bullet, `imports/normalized/` wins and the bullet must be corrected.
