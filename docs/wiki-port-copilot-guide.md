# Porting the Wiki Feature to Another Repo (Copilot-Only)

Step-by-step runbook for manually copying **just the wiki layer** (Karpathy's "LLM
Wiki" pattern) out of this repo into a different, unrelated GitHub repo, for
**GitHub Copilot only** — no Claude Code files.

Assumes: the target repo is a different domain (none of this repo's SA8620P/gPTP/HTP
demo content should travel), and the target repo has **neither** an offline import
pipeline (`imports/`) **nor** a project-memory layer (`project-context/`) yet — so
this guide includes the minimal scaffold the wiki needs from each, not the full
features.

Full background and rationale: see the plan this guide was generated from, or ask
the agent to re-derive it — the key decisions are repeated inline below so this
document stands alone.

---

## Prerequisites

- A local clone of both repos. Set two shell variables to make the commands below
  copy-pasteable:
  ```bash
  SOURCE=/path/to/AutomotiveAgent-SYS3
  TARGET=/path/to/the-other-repo
  ```
- GitHub Copilot enabled in your editor. For `.github/prompts/*.prompt.md` to appear
  as slash commands, confirm Copilot's "reusable prompt files" support is turned on
  in your editor's Copilot/Chat settings (the exact setting name has changed across
  Copilot versions — check your version's docs if the prompts don't show up).

---

## Step 1 — Copy the mechanism files verbatim

```bash
mkdir -p "$TARGET/.github/instructions" "$TARGET/.github/prompts" \
         "$TARGET/rules" "$TARGET/scripts" "$TARGET/commands/wiki" "$TARGET/raw"

cp "$SOURCE/.github/instructions/wiki.instructions.md"        "$TARGET/.github/instructions/"
cp "$SOURCE/.github/instructions/raw-sources.instructions.md" "$TARGET/.github/instructions/"
cp "$SOURCE/.github/prompts/wiki-update.prompt.md"             "$TARGET/.github/prompts/"
cp "$SOURCE/.github/prompts/wiki-lint.prompt.md"                "$TARGET/.github/prompts/"
cp "$SOURCE/rules/wiki-rules.md"                                "$TARGET/rules/"
cp "$SOURCE/scripts/lint-wiki.py"                                "$TARGET/scripts/"
cp "$SOURCE/commands/wiki/lint-wiki.sh"                          "$TARGET/commands/wiki/"
cp "$SOURCE/raw/README.md"                                      "$TARGET/raw/"

chmod +x "$TARGET/commands/wiki/lint-wiki.sh"
```

No edits needed for: `raw-sources.instructions.md`, `wiki-lint.prompt.md`,
`lint-wiki.py`, `lint-wiki.sh`, `raw/README.md` — fully generic already, and the
script gracefully no-ops if `imports/normalized/` or `knowledge-base/` don't exist
(both are existence-checked, not hard dependencies).

---

## Step 2 — Edit the three files with domain-specific content

**`.github/instructions/wiki.instructions.md`** — find the `## ID Linking` section:

```markdown
## ID Linking

Use existing ID vocabulary only — no new linking scheme:
SYS-{AREA}-NNN, ARC-{AREA}-NNN, CON-{FEATURE}-NNN, ADAS-NNN.
```

Replace the second line with whatever ID scheme (if any) the target repo actually
uses, or delete the section entirely if it has none yet.

**`.github/prompts/wiki-update.prompt.md`** — find the line mentioning
`` `SYS-*`, `ARC-*`, `CON-*` `` and trim/replace those examples the same way.

**`rules/wiki-rules.md`** — two edits:

1. Opening line currently reads:
   ```markdown
   Rules for `wiki/` — compiled subject-matter memory synthesized from
   `imports/normalized/` (offline tool exports) and `raw/` (live-fetched external
   sources — links, articles, papers; see `raw-sources.instructions.md`).
   ```
   Reword to reflect that only `raw/` exists so far:
   ```markdown
   Rules for `wiki/` — compiled subject-matter memory synthesized from `raw/`
   (live-fetched external sources — links, articles, papers; see
   `raw-sources.instructions.md`), and from `imports/normalized/` if/when an offline
   tool-export pipeline is added later.
   ```
2. In the `## Ingest vs Update Decision` table, remove or comment out the row
   `A JIRA issue with Components matching an existing topic | Same` — there's no
   JIRA integration in the target repo yet.

---

## Step 3 — Add a Query Behavior section to `wiki.instructions.md`

This repo's query-integration lived partly in `skills/project-memory/SKILL.md` — a
Claude Code-only file Copilot never reads. Since the target repo won't have that
skill, fold the equivalent behavior directly into the schema file instead. Append
this section to the end of `wiki.instructions.md`:

```markdown
## Query Behavior

For any knowledge question, check `wiki/index.md` first and cite the relevant topic
page(s) before re-deriving from scratch. If analysis produces a novel, durable fact
about subsystem state that isn't already in the wiki, file it into the relevant
`wiki/topics/{slug}.md` (Current State + History) or run `/wiki-update`.
```

---

## Step 4 — Create the empty scaffold (no demo data)

```bash
mkdir -p "$TARGET/wiki/topics" "$TARGET/project-context/decisions"
```

**`$TARGET/wiki/index.md`**:

```markdown
# Wiki Index

Compiled, continuously-updated state of the project's subsystems — synthesized from
`raw/` (and `imports/normalized/`, if an offline import pipeline is added later).
NOT a substitute for static reference docs or behavioral/process memory. See
`rules/wiki-rules.md`.

Status vocabulary: `Active` (current, has content) | `Stale` (flagged by
`/wiki-lint`, needs a pass) | `Orphan` (no ingest activity in several cycles —
archival candidate).

| Topic | Area | Status | Last updated | Sources folded in |
|-------|------|--------|--------------|--------------------|
```

**`$TARGET/wiki/log.md`**:

```markdown
# Wiki Activity Log

Append-only. One entry per `/wiki-update` or `/wiki-lint` run touching the wiki.
Never edit past entries — corrections go in the affected topic page's own History
section, with a note here pointing at it.
```

**`project-context/decisions/ADR-000-template.md`** — copy just this one template
file (the *only* piece of the project-memory feature the wiki needs, since its
Decisions section only needs somewhere to link ADRs):

```bash
cp "$SOURCE/project-context/decisions/ADR-000-template.md" \
   "$TARGET/project-context/decisions/"
```

Do **not** bring `LEARNINGS.md`, `conventions.md`, `internal-docs/`, or the
project-memory skill — those are the full feature, out of scope here.

---

## Step 5 — Hand-edit the target repo's own existing files

Do not copy this repo's versions of these — they're specific to this repo's domain
and agents. Only the *pattern* ports.

**Their `.github/copilot-instructions.md`** — append:

```markdown
## Standing behaviors (no command needed)

- **Auto-ingest**: when a URL, article, or paper is shared in conversation, fetch
  it, save it to `raw/{date}-{slug}.md`, and route it into `wiki/` or
  `project-context/` per `rules/wiki-rules.md` — don't wait to be asked.
- **Auto-query**: for any knowledge question, check `wiki/index.md` first and cite
  the relevant topic page(s) before researching from scratch.
```

**Each of their existing `.github/agents/*.md` files** — add one line under
whatever "Context Files" (or equivalent) section already exists:

```markdown
- Compiled subsystem state: `wiki/topics/{their-topic-slugs}.md`
```

Their topic slugs will be whatever fits their own domain — this repo's
`gptp-timesync`/`htp-orchestration`/`technical-safety-concept` don't apply.

---

## Step 6 — Explicitly leave behind

Do not copy any of these — they're Claude Code-only, this project's own demo/example
content, or tied to a feature (`imports/`) the target repo doesn't have:

- `CLAUDE.md`, `skills/project-memory/SKILL.md` (Claude Code-only conventions)
- `AGENTS.md` (general multi-tool convention, not Copilot-exclusive — skip for a
  Copilot-only port; add later if other agents are used)
- `.github/prompts/import-normalize.prompt.md` (its wiki-fold step assumes the
  offline import pipeline exists — revisit this file if that pipeline is added later)
- `.github/instructions/project-context.instructions.md` (belongs to the full
  project-memory feature)
- All 4 demo topic pages (`wiki/topics/gptp-timesync.md`, `htp-orchestration.md`,
  `technical-safety-concept.md`, `diagnostics.md`)
- `raw/2026-07-05-karpathy-llm-wiki-pattern.md`,
  `project-context/decisions/ADR-001-llm-wiki-pattern.md` (this project's own
  example/history content)
- All of `imports/` (`manifest.md`, `normalized/*`, `samples/*`, `inbox/`, `archive/`),
  `commands/import/`, `scripts/normalize-imports.py`, `scripts/importers/*`,
  `skills/tool-exports/` (the separate offline-import feature)

---

## Step 7 — Verify end-to-end in the target repo

1. Run the lint script on the empty scaffold — should report cleanly with zero
   topic pages, not error:
   ```bash
   cd "$TARGET" && bash commands/wiki/lint-wiki.sh --all
   ```
2. In a Copilot chat, paste a URL and confirm the auto-ingest behavior fires
   without a slash command: it should fetch the content, save
   `raw/{date}-{slug}.md`, and report where it routed it (a new `wiki/topics/*.md`
   page or a note that it belongs in `project-context/`).
3. Confirm the resulting topic page has all 5 mandatory sections (Current State,
   Open Questions, Decisions, Cross-References, History) and passes:
   ```bash
   bash commands/wiki/lint-wiki.sh --all --fix
   ```
4. Ask a knowledge question unrelated to the source you just ingested, then ask
   one that *is* related, and confirm the agent checks `wiki/index.md` first for
   the second question (per the new Query Behavior section) rather than
   re-researching from scratch.
5. Commit in the target repo:
   ```bash
   cd "$TARGET"
   git add .github/instructions/wiki.instructions.md \
           .github/instructions/raw-sources.instructions.md \
           .github/prompts/wiki-update.prompt.md \
           .github/prompts/wiki-lint.prompt.md \
           .github/copilot-instructions.md \
           rules/wiki-rules.md scripts/lint-wiki.py commands/wiki/lint-wiki.sh \
           raw/ wiki/ project-context/decisions/ADR-000-template.md
   git commit -m "Add wiki layer (LLM-compiled subsystem memory), ported from AutomotiveAgent-SYS3"
   git push
   ```
