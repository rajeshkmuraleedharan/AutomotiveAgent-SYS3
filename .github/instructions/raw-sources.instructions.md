---
name: Raw External Sources
description: "Use when: Rajesh shares a URL, article, or paper — fetch, save, and route it automatically, no command needed"
applyTo: ["raw/**"]
---

# Raw External Sources — Auto-Ingest

Standing behavior: when Rajesh shares a link, article, or paper in conversation
(not a Codebeamer/JIRA/Confluence export — those go through `imports/`, see
`tool-export-formats.instructions.md`), fetch and save it without being asked.

## Steps

1. Fetch the URL and extract its full content in detail — not a summary. The saved
   file is the source of record other pages cite back to, so under-extracting here
   loses information permanently.
2. Save to `raw/{YYYY-MM-DD}-{slug}.md`:

   ```markdown
   # {Title}

   | Field | Value |
   |-------|-------|
   | Source URL | {url} |
   | Fetched | {YYYY-MM-DD} |
   | Fetched by | Rajesh (shared in conversation) |

   {full extracted content}
   ```

3. Route the content per `rules/wiki-rules.md`'s routing rule:
   - **Subsystem-technical** (protocol specs, standards, vendor docs, papers about
     gPTP/HTP/TSC/etc.) → fold into the matching (or new) `wiki/topics/{area}.md`,
     same as `/wiki-update` does for tool imports
   - **Agent/process/meta** (patterns for how the agent itself should work — e.g.
     this repo's own wiki pattern) → `project-context/` (a LEARNINGS entry or ADR
     via `/record-learning`), not a subsystem wiki page
   - **General reference, no clear subsystem fit** → `wiki/topics/general-references.md`
     (catch-all, created on first use)
4. Report back: what was saved, where it was routed, and why.

## What NOT to auto-fetch

- Anything requiring authentication (per the standard WebFetch limitation) — say so
  and ask Rajesh for a manual export instead
- Codebeamer/JIRA/Confluence URLs — those need the offline export workflow
  (`skills/tool-exports/SKILL.md`), not live fetch
