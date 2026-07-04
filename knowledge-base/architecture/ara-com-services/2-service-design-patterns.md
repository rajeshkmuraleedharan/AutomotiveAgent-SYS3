# ara::com — Service Design Patterns

## 1. Status distribution (most common)

State producer publishes an enum event + heartbeat; consumers subscribe.
Example: `TimeBaseStatusService` (kSynchronized/kUncertain/kUnavailable, 100 ms heartbeat).
Use when: many consumers, one producer, freshness matters.
E2E: P04 on the event; consumers treat E2E failure like kUnavailable.

## 2. Supervised command

Method with result + monitored execution event. Use for mode changes
(e.g. degradation manager commands feature shedding). The commanding side never
assumes success from the method return alone — it waits for the state event.

## 3. Health reporting

Components report to a central health aggregate via a common `HealthReportService`;
the aggregate feeds the SAIL supervision boundary via the raw cross-domain protocol.
Keeps ara::com inside QNX; the safety island sees one consolidated channel.

## 4. Data freshness contract

Sensor/fusion data services carry a gPTP timestamp field; consumers enforce
max-age against the synchronized time base. Never distribute "age" — distribute
timestamps and let consumers judge against their own deadline.

## Anti-patterns

- ❌ Chatty method-call APIs for periodic data (use events)
- ❌ ara::com across the QNX↔SAIL boundary
- ❌ Unversioned breaking changes to a deployed service
- ❌ QM producer feeding an ASIL consumer without E2E + plausibility at the consumer
