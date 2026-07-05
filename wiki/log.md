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
