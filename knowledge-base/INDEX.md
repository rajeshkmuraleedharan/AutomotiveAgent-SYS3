# Knowledge Base Index

Deep reference for the AutomotiveAgent-SYS3 agent. All files are workspace-indexed by Copilot.

## Standards

| Directory | Topic | Status |
|-----------|-------|--------|
| `standards/aspice-sys2/` | ASPICE v3.1 SYS.2 process | Seeded |
| `standards/aspice-sys3/` | ASPICE v3.1 SYS.3 process | Stub |
| `standards/iso26262/` | ISO 26262:2018 functional safety | Stub |

## Features

| Directory | Topic | Status |
|-----------|-------|--------|
| `features/gptp-timesync/` | IEEE 802.1AS gPTP + Marvell TSN | Stub |
| `features/htp-orchestration/` | Hexagon HTP + orchestration | Stub |
| `features/technical-safety-concept/` | TSC + ASIL decomposition | Stub |

## Architecture

| Directory | Topic | Status |
|-----------|-------|--------|
| `architecture/adas-platform/` | Platform decomposition, static/dynamic view patterns | Seeded |
| `architecture/ara-com-services/` | ara::com service design + SOME/IP/TSN deployment | Seeded |
| `architecture/allocation-model/` | SYS→ARC→target allocation, ASIL rules | Seeded |

## Tools (offline integration)

| Directory | Topic | Status |
|-----------|-------|--------|
| `tools/codebeamer/` | Trackers, workflows, export/re-import | Seeded (`[TBD]` internals) |
| `tools/jira/` | Issue lifecycle, CSV export format | Seeded (`[TBD]` internals) |
| `tools/confluence/` | Page conventions, export formats | Seeded (`[TBD]` internals) |

Each feature directory uses the **5-level depth pattern**:
- `1-overview.md` — what it is, why it matters
- `2-*-protocol/architecture.md` — conceptual deep dive
- `3-*-integration.md` — SA8620P-specific integration
- `4-sys3-requirements-bank.md` — pre-written SYS.3 requirement examples
