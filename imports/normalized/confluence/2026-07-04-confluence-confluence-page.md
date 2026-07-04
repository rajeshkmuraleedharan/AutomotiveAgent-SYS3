# Confluence import — confluence-page

| Field | Value |
| --- | --- |
| Tool | confluence |
| Source export | confluence-page.html |
| Imported | 2026-07-04 19:46 |
| Items | 1 |
| Source SHA-256 | 881c51a6ec299115 |

# gPTP Holdover Strategy — Decision Page

Space: **ADAS Platform** | Author: Rajesh | Last updated: 2026-06-18

## Problem

When the grandmaster becomes unreachable, camera fusion needs a bounded time-base drift until re-sync. We must pick a holdover strategy for the *SA8620P* time-base provider.

## Options considered

- Free-running local oscillator (no compensation)
- Drift-compensated holdover using last known rate ratio
- Redundant grandmaster with fast BMCA failover

## Decision

Drift-compensated holdover, with redundant GM as a later platform option. Rate ratio is frozen at sync loss and applied by `tsyncd` on QNX:KryoP0.

## Consequences

| Aspect | Impact |
| --- | --- |
| Accuracy during holdover | ≤ 5 µs drift over 2 s at 25 °C |
| Safety | kUncertain published immediately; DTC_GPTP_SYNC_LOSS after 250 ms |
| Cost | No extra hardware |

## Follow-ups

1. Requirements SYS-GPTP-001/002 updated in Codebeamer
1. Bench test with fault-injection switch (JIRA ADAS-101)
