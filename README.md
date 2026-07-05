# AutomotiveAgent-SYS3

> GitHub Copilot + Claude Code agent for **systems engineering** on the **Qualcomm SA8620P** ADAS platform: SYS.2/SYS.3 requirements, system architecture, concept development, and offline **Codebeamer / JIRA / Confluence** integration. Feature areas: **gPTP TimeSync**, **HTP Orchestration**, **Technical Safety Concept**.

---

## Platform

| Layer | Component |
|-------|-----------|
| SoC | Qualcomm SA8620P (Kryo CPU + Hexagon HTP + SAIL safety MCU + Adreno GPU) |
| Performance OS | QNX 8.0 (ASIL-B) |
| Safety OS | SafeRTOS on SAIL (ASIL-D) |
| AUTOSAR | Vector MICROSAR Adaptive (ara::com, ara::exec, ara::phm, ara::tsync, ara::diag) |
| Ethernet | Marvell 88Q5050 switch + 88Q22xx PHY (IEEE 802.1AS gPTP) |
| PMIC | Intel PMIC |

**Classic AUTOSAR is out project-wide.**

---

## Setup

```bash
git clone https://github.com/rajeshkmuraleedharan/AutomotiveAgent-SYS3.git
python3 -m venv .venv && .venv/bin/pip install pyyaml openpyxl python-docx
```

Copilot use: copy `.github/` into your project (requires VS Code + Copilot).
Claude Code use: open the repo directly — `CLAUDE.md`/`AGENTS.md` are auto-loaded.

---

## Agents

| Agent | Trigger | Purpose |
|-------|---------|---------|
| SYS3 Requirements Engineer | `@sys3-requirements-engineer` | Draft SYS.2/SYS.3 requirements |
| System Architect | `@system-architect` | Architecture views, ARC elements, ara::com interfaces, allocation, concepts |
| Requirements Reviewer | `@requirements-reviewer` | Review requirements + ARC elements |
| Safety Analyst | `@safety-analyst` | TSC, ASIL decomposition, FMEA support |

## Prompts

| Trigger | Output |
|---------|--------|
| `/sys2-reqs` | SYS.2 requirements (stakeholder-derived, solution-free) |
| `/sys3-gptp` `/sys3-htp` `/sys3-safety` | SYS.3 requirements in CB format |
| `/req-review` | ASPICE + Codebeamer compliance review |
| `/verification-criteria` | Write / improve verification criteria |
| `/arch-view` | Static/dynamic architecture view (mermaid + ARC blocks) |
| `/arch-interface` | ara::com service / QNX↔SAIL protocol definition |
| `/arch-allocation` | SYS→ARC→target allocation matrix + findings |
| `/concept-feature` | Feature / operating concept |
| `/concept-trade-study` | Weighted trade study |
| `/import-normalize` | Normalize tool exports from `imports/inbox/` |
| `/record-learning` | Persist decisions/corrections to project memory |

---

## Offline tool integration

No API access needed: drop Codebeamer (CSV/Excel/Word), JIRA (CSV "all fields"), or
Confluence (Word/HTML) exports into `imports/inbox/`, run
`commands/import/normalize-exports.sh`, and the agent works from
`imports/normalized/`. Codebeamer requirement imports come out as canonical YAML
blocks that pass the schema validator directly.

## Project memory

`project-context/` holds conventions, an append-only LEARNINGS log, and ADRs —
consulted at every task start, extended via `/record-learning`. The agent improves
on this project the longer it is used.

---

## Structure

```
.github/
├── agents/          ← Copilot custom agents (4)
├── instructions/    ← Auto-loaded domain context (schema, architecture, tools, concepts)
└── prompts/         ← Slash commands

commands/            ← Shell automation (ID gen, CB export, validation, import)
docs/                ← Writing guide, workflow, CB import guide, wiki Copilot-port guide
imports/             ← Offline tool exchange: inbox → normalized → archive (+ samples)
knowledge-base/
│   ├── standards/   ← ASPICE SYS.2/SYS.3, ISO 26262
│   ├── features/    ← gPTP, HTP, TSC deep dives + requirement banks
│   ├── architecture/← Platform decomposition, ara::com services, allocation model
│   └── tools/       ← Codebeamer, JIRA, Confluence reference
project-context/     ← Project memory: conventions, LEARNINGS, ADRs, internal docs
rules/               ← Authoring rules (requirements, architecture, concepts, imports…)
scripts/             ← Python automation (validators, ID gen, CB formatter, importers)
skills/              ← Copilot + Claude Code skill definitions
```

---

## Standards

| Standard | Scope |
|----------|-------|
| ASPICE v3.1 | SYS.2 requirements analysis + SYS.3 architectural design |
| ISO 26262:2018 | Functional safety — ASIL, HARA, FMEA, SPFM/LFM |
| IEEE 802.1AS-2020 | gPTP precision time protocol |
| AUTOSAR Adaptive R22-11 | ara::tsync, ara::phm, ara::exec, ara::com |
| Codebeamer ALM | Requirement field schema + import format |

## Roadmap

- **Phase 2 — system-level bug analysis**: bug-triage skill (severity/ASIL triage of
  JIRA defect exports, symptom→subsystem localization for QNX/SafeRTOS/ara::com/TSN/PMIC),
  `/bug-rootcause` (5-Whys + fault propagation → candidate requirement/architecture gaps),
  JIRA importer `--defects` profile.
