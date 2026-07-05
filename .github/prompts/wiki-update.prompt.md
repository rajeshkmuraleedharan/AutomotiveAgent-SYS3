---
name: Wiki Update
description: Synthesize imports/normalized/ content into wiki/ topic pages — runs automatically after /import-normalize, or standalone for backfill/replay.
---

Fold normalized import content into the wiki.

## Steps

1. Determine scope:
   - Default: files under `imports/normalized/` newer than the last `wiki/log.md` entry
   - `--since <date|manifest-row>`: files from that point forward
   - `--all`: replay the full `imports/normalized/` history (backfill mode)
2. For each normalized file in scope, extract IDs (`SYS-*`, `ARC-*`, `CON-*`, JIRA keys)
   and map to topic(s) via AREA or JIRA Components, per `rules/wiki-rules.md`'s
   ingest-vs-update decision table.
3. For each affected topic:
   - Update **Current State** — rewrite affected bullets in place, cite the IDs
   - Update **Cross-References** — append new IDs
   - Update **Open Questions** — file anything with no owning requirement/element yet
   - Append one line to **History**
   - Create the page (all 5 sections) + a `wiki/index.md` row if no existing topic
     matches (per the granularity rule — never split pre-emptively)
4. If new content contradicts an existing Current State bullet, do NOT silently
   overwrite: rewrite the bullet to reflect the newest evidence AND add a History
   line naming the contradiction and which import resolved it.
5. Update `wiki/index.md` (Last updated, Sources folded in) for every touched topic.
6. Append one entry to `wiki/log.md` summarizing the run: which import batch(es),
   which topics were created/updated, what was filed under Open Questions.
7. Report back: pages created, pages updated, contradictions/open questions raised.

Pages seeded from `imports/samples/*` rather than real imports must be labeled as
demo content in their header line (see `wiki.instructions.md`).
