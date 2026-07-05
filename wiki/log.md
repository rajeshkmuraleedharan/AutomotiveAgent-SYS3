# Wiki Activity Log

Append-only. One entry per `/wiki-update` or `/wiki-lint` run touching the wiki.
Never edit past entries — corrections go in the affected topic page's own History
section, with a note here pointing at it.

---

## 2026-07-05 — wiki-update (backfill, --all, demo seed)

Replayed the full existing `imports/normalized/` history (all sample-fixture-derived
content — no real project data yet) to seed the wiki end-to-end.

- Created `topics/gptp-timesync.md`: filed SYS-GPTP-001, SYS-GPTP-002, ADAS-101
  (BMCA re-run transient bug), ADAS-105 (degradation-ladder story), holdover-strategy
  decision from the Confluence page
- Created `topics/htp-orchestration.md`: filed SYS-HTP-001, ADAS-102 (thermal
  throttling deadline-signal bug), DLC lifecycle notes from Confluence
- Created `topics/technical-safety-concept.md`: filed ADAS-104 (SafeRTOS DTC latch bug)
- Open questions raised: BMCA transient coverage gap (gptp-timesync), thermal
  supervisor timing gap (htp-orchestration), DTC latch window (technical-safety-concept)
- ADAS-103 (a process task, not a subsystem fact) intentionally not filed into
  Current State per `rules/wiki-rules.md` (wiki is not a per-issue mirror)
- All three pages marked "(demo)" — replace with real content as actual exports arrive

---

## 2026-07-05 — wiki-update (import batch jira/2026-07-05-jira-jira-issues-followup.md)

End-to-end test of a live incremental import (not backfill): dropped a new JIRA
export into `imports/inbox/`, ran the real `/import-normalize` pipeline, folded the
result into the wiki.

- Updated `topics/gptp-timesync.md` in place: ADAS-101 resolved (BMCA settle/grace
  period fix, bench-verified) — removed from Open Questions, folded into Current
  State; page no longer "(demo)" now that a real update has landed
- Created `topics/diagnostics.md`: new topic, JIRA Component "Diagnostics" had no
  existing page (ADAS-106, DTC snapshot gap) — cross-referenced against the related
  PMIC brown-out bug already on `technical-safety-concept.md` (ADAS-104)
- Updated `topics/technical-safety-concept.md`: added a back-reference to the new
  diagnostics topic (same brown-out event, different open question)
- `wiki/index.md`: updated 2 existing rows, added 1 new row
- Confirms: existing-topic updates land in place (not duplicated), new-topic
  creation follows the granularity rule (Component with no existing page), and
  cross-topic references work in both directions
