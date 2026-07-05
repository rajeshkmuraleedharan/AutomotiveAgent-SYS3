---
name: Wiki Lint
description: Periodic pass over wiki/ — fixes what it safely can, then reports contradictions, stale claims, orphan pages, and gaps with suggestions for new sources.
---

Lint the wiki for correctness, staleness, and gaps.

## Steps

1. Run `commands/wiki/lint-wiki.sh --all --fix`. This applies only the two
   auto-fixable findings from `rules/wiki-rules.md`'s Auto-Fix Categorization table
   (missing `wiki/index.md` row; `Last updated` behind the page's own History) and
   reports them as `FIXED`. Report remaining mechanical findings: dangling ID
   references, dangling ADR links, Current-State bloat/split candidates — these are
   never auto-applied (see the table for why).
2. Read all `wiki/topics/*.md` pages and perform judgment checks per
   `rules/wiki-rules.md`'s staleness/contradiction definitions:
   - **Contradictions**: two Current State bullets (same page or cross-page) making
     incompatible claims about the same ID or subsystem behavior
   - **Content-drift staleness**: a bullet that's date-fresh but superseded in
     substance by a later import that wasn't folded in cleanly
   - **Stale Open Questions**: unresolved across many cycles with no owner —
     candidate to become a requirement, ADR, or JIRA follow-up
   - **Orphan judgment**: a page no other page or recent import references in
     practice, even if the mechanical check didn't flag it by activity count
3. For each judgment finding, propose a fix (rewrite bullet, add History line,
   split page, archive page) — do not silently apply; present findings for Rajesh
   to confirm, same as before `--fix` existed. `--fix` never touches semantic content.
4. For gaps (thin Cross-References, an Open Question unresolved across many cycles,
   a topic with no wiki content despite active imports referencing it), suggest a
   concrete new source that would close the gap — e.g. "no vendor doc covers
   ARC-GPTP-003's TSN deployment — look for the 88Q5050 datasheet section on egress
   scheduling" — rather than only reporting the gap.
5. Append one entry to `wiki/log.md` summarizing the lint run: auto-fixes applied,
   findings reported, source suggestions made.
