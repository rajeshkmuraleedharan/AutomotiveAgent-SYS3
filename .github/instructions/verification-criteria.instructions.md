---
name: Verification Criteria Guide
description: "Use when: writing or reviewing verification criteria for SYS.3 requirements — gPTP, HTP, or TSC topics"
applyTo: ["**/requirements/**", "**/*SYS*", "**/*verification*"]
---

# Verification Criteria Writing Guide

## Structure of Good Verification Criteria

A verification criterion must be:
1. **Measurable** — specific numeric threshold or binary pass/fail
2. **Testable** — achievable by a defined test method
3. **Conditioned** — specifies environmental/operating conditions
4. **Bounded** — specifies statistical confidence or tolerance (e.g., 3σ, 95th percentile)

## Template

```
[Parameter] shall be [comparison] [threshold] [unit] measured at [conditions]
over [duration] with [sample size or confidence level].
```

## Examples by Topic

### gPTP TimeSync

```
The local time-base offset to the gPTP grandmaster shall be ≤ 1 µs (3σ)
measured over 24-hour soak at –40 °C and +85 °C with nominal network load.
```

```
The holdover period before time-base status transitions to kUncertain
shall be ≥ 3 consecutive missed sync intervals (3 × syncInterval).
```

### HTP Orchestration

```
The HTP inference latency for a DLC model of complexity class C2
shall be ≤ 100 ms (95th percentile) under full CPU load at +85 °C junction temperature.
```

```
The OOD detector shall produce score > 0.7 for ≥ 95% of out-of-distribution
inputs in the SOTIF validation dataset (N ≥ 1000 samples).
```

### Technical Safety Concept (TSC)

```
The hardware watchdog shall reset the SAIL core within 10 ms of a task overrun
detected by the HW_Watchdog_Task (SAIL priority 1), verified by fault injection
on the target hardware.
```

```
SPFM for the HW_Watchdog_Task element shall be ≥ 99% as demonstrated
by FMEDA per QC-SA8620P-SM §[TBD].
```

## Verification Method Selection

| Situation | Method |
|-----------|--------|
| Timing / latency / accuracy | TEST — on-target measurement |
| Safety mechanism DC coverage | ANALYSIS — FMEDA |
| Protocol compliance | TEST — conformance test |
| ASIL allocation correctness | INSPECTION — design review |
| SPFM / LFM targets | ANALYSIS — FMEDA + BIST report |

## Anti-Patterns

- ❌ `shall be verified by testing` — no threshold or condition
- ❌ `shall meet timing requirements` — no value specified
- ❌ `shall be correct` — not measurable
- ❌ Missing temperature / load conditions for timing criteria
- ❌ `≤ 1 ms` without statistical qualifier (mean? 3σ? worst case?)
