# LLM Wiki Pattern by Andrej Karpathy

| Field | Value |
|-------|-------|
| Source URL | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Fetched | 2026-07-05 |
| Fetched by | Rajesh (shared in conversation) |

## Title & Description

**"LLM Wiki"** — A design pattern for building personal knowledge bases where LLMs
incrementally maintain a persistent, structured wiki rather than performing
retrieval-augmented generation (RAG) on raw documents at query time.

## Core Problem Solved

Traditional RAG systems rediscover knowledge from scratch on every query. This
pattern shifts the burden: instead of retrieving and synthesizing document fragments
repeatedly, an LLM compiles sources once into a maintained wiki, then keeps it
current as new information arrives. The wiki becomes a "compounding artifact" where
cross-references, contradictions, and synthesis accumulate over time.

## Three-Layer Architecture

**Raw sources** — Immutable curated documents (articles, papers, PDFs, notes)

**The wiki** — LLM-generated markdown files organizing summaries, entity pages,
concept pages, and an index

**The schema** — Configuration file (e.g., `CLAUDE.md`) encoding wiki structure,
naming conventions, and workflows

## Key Workflows

**Ingest:** New sources trigger multi-page updates — a single document might touch
10-15 wiki pages as the LLM updates entities, concepts, and cross-references.

**Query:** Users ask questions against the wiki. Good answers can be filed back as
new pages, compounding knowledge.

**Lint:** Periodic health checks identify contradictions, stale claims, orphan
pages, and data gaps.

## Critical Techniques

- **Index.md** (content catalog) + **log.md** (append-only timeline) for navigation
  at scale
- **No RAG embeddings needed** — hybrid BM25/vector search or simple index suffices
  for hundreds of pages
- **Optional CLI tools** for search and traversal (e.g., qmd for on-device search)
- **Graph visualization** (Obsidian) shows wiki structure and connectivity
- **Git versioning** built-in for history and collaboration

## Why It Works

The pattern recognizes that human knowledge bases fail because maintenance burden
outpaces value. LLMs excel at bookkeeping (updating cross-references, flagging
contradictions, keeping summaries current) at near-zero cost. Humans curate sources
and ask questions; LLMs do the grunt work. The result is a wiki that stays
maintained and grows richer with each source.

## Optional Enhancements

- Voice/image support with local downloads
- Marp slide deck generation from wiki content
- Dataview plugin for dynamic frontmatter queries
- Telegram bot interface for queries and exports

The gist explicitly frames itself as pattern documentation, not a specific
implementation, encouraging users to collaborate with LLMs to instantiate versions
suited to their domain.
