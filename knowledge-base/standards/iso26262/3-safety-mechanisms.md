# ISO 26262 — Safety Mechanisms

## Definition

A safety mechanism detects and handles faults to prevent or mitigate hazardous events.

## Mechanism Types (ISO 26262-5 Annex D)

| Type | SA8620P Example |
|------|----------------|
| Hardware watchdog | SafeRTOS HW_Watchdog_Task (5 ms) |
| Alive supervision | ara::phm AliveSupervision |
| Deadline supervision | ara::phm DeadlineSupervision (HTP 100 ms) |
| Logical supervision | ara::phm LogicalSupervision (CBIST) |
| E2E protection | CRC32 + seq counter (QNX↔SAIL) |
| BIST | PBIST / CBIST / OBIST on SAIL + Kryo |

## Diagnostic Coverage (DC)

| DC class | Range |
|----------|-------|
| Low | < 60% |
| Medium | 60–90% |
| High | > 90% |

## TODO: Add full DC table from ISO 26262-5 Table D.1
