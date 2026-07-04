# AutomotiveAgent-SYS3 — Agent Context

This file is auto-loaded by Copilot and Claude during agent workflows.

## Repo Purpose

GitHub Copilot + Claude Code agent for **systems engineering** on the **Qualcomm
SA8620P** ADAS platform: SYS.2/SYS.3 requirements, system architecture design,
concept development, and offline integration with Codebeamer, JIRA, and Confluence.

**Feature areas:**
1. gPTP TimeSync (IEEE 802.1AS, Marvell TSN, ara::tsync)
2. HTP Orchestration (Hexagon Tensor Processor, SNPE/QNN, FastRPC)
3. Technical Safety Concept (ISO 26262, ASIL decomposition, safety mechanisms, TSR)

**Output formats:** Codebeamer YAML attribute blocks (requirements), ARC element
blocks + mermaid views (architecture), markdown documents (concepts).

## Agents

| Agent | File | Role |
|-------|------|------|
| SYS3 Requirements Engineer | `.github/agents/sys3-requirements-engineer.md` | Drafts SYS.2/SYS.3 requirements |
| System Architect | `.github/agents/system-architect.md` | Views, ARC decomposition, ara::com interfaces, allocation, concepts |
| Requirements Reviewer | `.github/agents/requirements-reviewer.md` | Reviews requirements + ARC elements |
| Safety Analyst | `.github/agents/safety-analyst.md` | TSC, ASIL decomposition, FMEA support |

## Working Rules

- **Project memory first**: consult `project-context/` (conventions, LEARNINGS, ADRs)
  at task start; offer `/record-learning` at task end
- **Tool state is offline**: read imported tool content only from `imports/normalized/`
- **Traceability chain**: `STK-*/CON-* → SYS.2 → SYS.3 → ARC-*`; architecture without
  a driving requirement is a finding
- The requirement schema is **locked** (`sys3-requirements-schema.instructions.md`)

## Platform

| Layer | Component |
|-------|-----------|
| SoC | Qualcomm SA8620P (Kryo CPU + Hexagon HTP + Adreno GPU + SAIL safety MCU) |
| Performance OS | QNX 8.0 (ASIL-B) |
| Safety OS | SafeRTOS on SAIL (ASIL-D) |
| AUTOSAR stack | Vector MICROSAR Adaptive |
| Ethernet | Marvell 88Q5050 + 88Q22xx (IEEE 802.1AS) |
| PMIC | Intel PMIC |

**Classic AUTOSAR is out project-wide.**

## ID Conventions

- Requirements: `SYS-{GPTP|HTP|TSC|TSR}-NNN` — `level:` distinguishes SYS.2 vs SYS.3
- Architecture elements: `ARC-{AREA}-NNN` | Concepts: `CON-{FEATURE}-NNN`
- NNN zero-padded to 3 digits, never reused
