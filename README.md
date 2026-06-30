# AutomotiveAgent-SYS3

> GitHub Copilot + Claude Code agent for ASPICE SYS.3 system requirements on the **Qualcomm SA8620P** ADAS platform. Focused on three topics: **gPTP TimeSync**, **HTP Orchestration**, **Technical Safety Concept**. Output targets **Codebeamer ALM**.

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

---

## Setup

```bash
git clone https://github.com/rajeshkmuraleedharan/AutomotiveAgent-SYS3.git
cp -r .github/ /path/to/your/adas-project/.github/
```

Requires VS Code + GitHub Copilot extension.

---

## Agents

| Agent | Trigger | Purpose |
|-------|---------|---------|
| SYS3 Requirements Engineer | `@sys3-requirements-engineer` | Draft SYS.3 requirements for gPTP / HTP / TSC |
| Requirements Reviewer | `@requirements-reviewer` | Review for ASPICE + Codebeamer compliance |
| Safety Analyst | `@safety-analyst` | TSC, ASIL decomposition, FMEA support |

## Prompts

| Prompt | Trigger | Output |
|--------|---------|--------|
| `sys3-gptp.prompt.md` | `/sys3-gptp` | gPTP SYS.3 requirements in CB format |
| `sys3-htp.prompt.md` | `/sys3-htp` | HTP orchestration SYS.3 requirements |
| `sys3-safety.prompt.md` | `/sys3-safety` | Technical Safety Concept requirements |
| `req-review.prompt.md` | `/req-review` | ASPICE + Codebeamer compliance review |
| `verification-criteria.prompt.md` | `/verification-criteria` | Write / improve verification criteria |

---

## Structure

```
.github/
├── agents/          ← Copilot custom agents
├── instructions/    ← Auto-loaded domain context
└── prompts/         ← Slash commands

commands/            ← Shell automation (ID gen, CB export, ASPICE check)
docs/                ← Writing guide, workflow, CB import guide
knowledge-base/      ← Deep reference (5-level AutoZYX pattern)
│   ├── standards/   ← ASPICE SYS.3, ISO 26262
│   └── features/    ← gPTP, HTP, TSC deep dives + requirements banks
rules/               ← Requirement authoring rules (CB, ASPICE, safety)
scripts/             ← Python automation (validation, ID gen, CB formatter)
skills/              ← Copilot + Claude Code skill definitions
```

---

## Standards

| Standard | Scope |
|----------|-------|
| ASPICE v3.1 | SYS.3 system architectural design |
| ISO 26262:2018 | Functional safety — ASIL, HARA, FMEA, SPFM/LFM |
| IEEE 802.1AS-2020 | gPTP precision time protocol |
| AUTOSAR Adaptive R22-11 | ara::tsync, ara::phm, ara::exec |
| Codebeamer ALM | Requirement field schema + import format |
