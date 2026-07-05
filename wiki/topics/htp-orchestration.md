# HTP Orchestration — Wiki

Area: HTP | Status: Active (seeded from sample fixtures — replace as real imports arrive) | Last updated: 2026-07-05

## Current State

- Deadline supervision: system shall detect an HTP inference exceeding its
  configured 33 ms deadline and signal a violation within 5 ms of expiry
  (SYS-HTP-001, ASIL B, allocated QNX:KryoE0, watchdog timer per DLC instance).
- DLC lifecycle: models are loaded at FunctionGroup activation and supervised per
  frame; violations escalate to the degradation manager; `DEGRADED` state means a
  reduced model set is active (Confluence HTP concept notes).
- Open bug: at Tj > 95 °C (thermal throttling) the deadline violation signal itself
  arrives 40 ms late — violates SYS-HTP-001's ≤ 5 ms signalling budget (ADAS-102,
  Open, linked to ADAS-101 in JIRA).

## Open Questions

- ADAS-102 shows the watchdog/violation-signal path degrades under thermal
  throttling — is the supervisor's own signalling timing budget (not just the DLC's
  inference deadline) covered by any requirement? (raised 2026-06-22, unresolved)

## Decisions

- No ADRs filed for this topic yet.

## Cross-References

- Requirements: SYS-HTP-001
- JIRA: ADAS-102
- Source imports: `imports/normalized/codebeamer/2026-07-04-codebeamer-codebeamer-requirements.md`,
  `imports/normalized/jira/2026-07-04-jira-jira-issues.md`,
  `imports/normalized/confluence/2026-07-04-confluence-confluence-htp-notes.md`

## History

- 2026-07-05: page created (demo/backfill) from CB batch 2026-07-04, JIRA batch
  2026-07-04, and the Confluence HTP concept notes — filed SYS-HTP-001, ADAS-102,
  and the DLC lifecycle/DEGRADED-state notes.
