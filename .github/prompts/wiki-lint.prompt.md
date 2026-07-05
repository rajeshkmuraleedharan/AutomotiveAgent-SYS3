---
name: Wiki Lint
description: Periodic pass over wiki/ — catches contradictions, stale claims, orphan pages, and gaps. Run mechanical checks first, then LLM judgment pass.
---

Lint the wiki for correctness and staleness.

## Steps

1. Run `commands/wiki/lint-wiki.sh --all` and report mechanical findings: schema
   conformance, dangling ID references, dangling ADR links, date-based staleness,
   orphan pages (not in `wiki/index.md`), Current-State bloat/split candidates.
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
3. For each finding, propose a fix (rewrite bullet, add History line, split page,
   archive page) — do not silently apply; present findings for Rajesh to confirm.
4. Append one entry to `wiki/log.md` summarizing the lint run and findings.
