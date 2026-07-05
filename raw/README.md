# Raw External Sources

Immutable, curated external references — links, articles, papers — fetched live from
the public web (unlike `imports/`, which holds offline exports from internal tools
with no API access). This is the "raw sources" layer of the wiki pattern: content
lands here once, unedited, and `wiki/topics/*.md` (or `project-context/`) is what
synthesizes it into something query-able. See `rules/wiki-rules.md` for the routing
rule and `.github/instructions/raw-sources.instructions.md` for the save format.

## How sources land here

Standing behavior (no command needed, see `CLAUDE.md`): when Rajesh shares a URL,
article, or paper in conversation, the agent fetches it, saves it here, and routes
it into the wiki or project memory.

## File format

One file per source: `{YYYY-MM-DD}-{slug}.md`, header table (Source URL, Fetched,
Title, Fetched by), then the extracted content in full detail — not a summary, since
this is the source of record other pages cite back to.

## What's committed here

Everything — these are public sources, not sanitized internal exports, so the
`imports/inbox`/`archive` gitignore treatment does not apply.
