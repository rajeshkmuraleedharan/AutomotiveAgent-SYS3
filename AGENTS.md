# AutomotiveAgent-SYS3 — Agent Context

This file is auto-loaded by Copilot and Claude during agent workflows.

## Repo Purpose

Focused GitHub Copilot + Claude Code agent for authoring **ASPICE SYS.3 system requirements** on the **Qualcomm SA8620P** ADAS platform.

**Three topics only:**
1. gPTP TimeSync (IEEE 802.1AS, Marvell TSN, ara::tsync)
2. HTP Orchestration (Hexagon Tensor Processor, SNPE/QNN, FastRPC)
3. Technical Safety Concept (ISO 26262, ASIL decomposition, safety mechanisms, TSR)

**Output format:** Codebeamer ALM — YAML attribute blocks + requirement text.

## Agents

| Agent | File | Role |
|-------|------|------|
| SYS3 Requirements Engineer | `.github/agents/sys3-requirements-engineer.md` | Primary: drafts SYS.3 requirements |
| Requirements Reviewer | `.github/agents/requirements-reviewer.md` | Reviews ASPICE + Codebeamer compliance |
| Safety Analyst | `.github/agents/safety-analyst.md` | TSC, ASIL decomposition, FMEA support |

## Platform

| Layer | Component |
|-------|-----------|
| SoC | Qualcomm SA8620P (Kryo CPU + Hexagon HTP + SAIL safety MCU) |
| Performance OS | QNX 8.0 (ASIL-B) |
| Safety OS | SafeRTOS on SAIL (ASIL-D) |
| AUTOSAR stack | Vector MICROSAR Adaptive |
| Ethernet | Marvell 88Q5050 + 88Q22xx (IEEE 802.1AS) |
| PMIC | Intel PMIC |

**Classic AUTOSAR is out project-wide.**

## Requirement ID Conventions

- gPTP: `SYS-GPTP-NNN`
- HTP: `SYS-HTP-NNN`
- Technical Safety: `SYS-TSC-NNN` / `SYS-TSR-NNN`
- NNN zero-padded to 3 digits
