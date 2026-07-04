---
name: ara::com Interface Definitions
description: "Use when: defining or reviewing Adaptive AUTOSAR service interfaces (ara::com) for the SA8620P platform"
applyTo: ["**/architecture/**", "**/*interface*", "**/*service*"]
---

# ara::com Service Interface Definitions — Vector MICROSAR Adaptive

Interface definition format for services between Adaptive applications on QNX and
to the SAIL safety island. Stack: Vector MICROSAR Adaptive; binding: SOME/IP over
the Marvell TSN network (88Q5050). Classic AUTOSAR (RTE, COM signals) is out.

## Canonical Service Definition Block

```markdown
### Service: TimeBaseStatusService

| Attribute | Value |
|-----------|-------|
| ARC element | ARC-GPTP-002 (provider) |
| Instance specifier | `TimeSync/TimeBaseProvider/TimeBaseStatusService` |
| Service ID (SOME/IP) | 0x[TBD — from internal SOME/IP ID registry] |
| Instance ID | 0x[TBD] |
| Major.Minor version | 1.0 |
| ASIL | B |
| E2E profile | P04 (events), P01 (fields) — per VEC-MSR-ADAPT-E2E §[TBD] |

**Events**

| Event | Type | Cycle / trigger | E2E |
|-------|------|-----------------|-----|
| `TimeBaseStatusChanged` | `TimeBaseStatus` (enum: kSynchronized, kUncertain, kUnavailable) | on change + 100 ms heartbeat | P04 |

**Methods**

| Method | In | Out | Fire&Forget |
|--------|----|----|-------------|
| `GetRateDeviation` | — | `float64 ppm` | no |

**Fields**

| Field | Type | Notify | Get | Set |
|-------|------|--------|-----|-----|
| `HoldoverBudgetRemaining` | `uint32 ms` | yes | yes | no |
```

## Rules

- Every service is provided by exactly one ARC element and listed in that element's
  `interfaces.provides`; consumers list it under `interfaces.requires`
- ASIL of the service = max ASIL of the data it carries; E2E protection mandatory for ASIL ≥ A
- Naming: `UpperCamelCase` service/event/method names, `Service` suffix for services
- Types are Adaptive platform types (`uint32`, `float64`, enums defined in the service section)
- Service/Instance IDs come from the internal SOME/IP registry — use `0x[TBD]` until
  assigned; never invent concrete IDs
- Cross-domain (QNX ↔ SAIL) communication does NOT use ara::com — define it as a raw
  protocol interface element (type: `interface`) with the transport named explicitly
  (e.g. SPI heartbeat, shared-memory mailbox)
- Deployment notes state VLAN/priority (802.1Q PCP) and bandwidth estimate for TSN planning
