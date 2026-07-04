# ADAS Platform Architecture — Overview

Top-level decomposition knowledge for the SA8620P ADAS platform. This directory feeds
the @system-architect agent; element examples live in `4-arc-element-bank.md`.

## Platform at a glance

| Domain | Compute | OS / runtime | ASIL ceiling |
|--------|---------|--------------|--------------|
| Performance | Kryo CPU clusters (P0/P1, E-cores) | QNX 8.0 + MICROSAR Adaptive | B |
| AI/Vision | Hexagon HTP | QNX (FastRPC from CPU) | QM |
| GPU | Adreno | QNX | QM |
| Safety island | SAIL MCU | SafeRTOS (plain C) | D |
| Network | Marvell 88Q5050 TSN switch + 88Q22xx PHYs | — | (HW) |
| Power | Intel PMIC | — | (HW) |

## Architectural style

- Service-oriented on the performance domain: Adaptive applications communicating via
  ara::com/SOME/IP; Execution Management FunctionGroups gate feature activation
- Safety supervision pattern: QM/ASIL-B compute monitored by the ASIL-D safety island
  (challenge-response, heartbeat, plausibility) — never the other way round
- Time-triggered network: gPTP time base + TSN scheduling on the 88Q5050
- Degradation ladders per feature: full → degraded → safe state, driven by health and
  time-base status

## Decomposition levels

1. `system` — the ADAS platform domains (performance, safety, network, power)
2. `subsystem` — feature clusters (TimeSync, Perception/HTP, Safety supervision)
3. `component` — deployable units with one ASIL and one allocation target
4. `interface` — pure interface elements (cross-domain protocols)

Internal specifics to fill in: `[TBD — actual FunctionGroup list, machine states,
camera/sensor set of the program]`.
