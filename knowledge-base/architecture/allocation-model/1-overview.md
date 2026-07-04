# Allocation Model — Overview

How SYS-* requirements map to ARC-* elements and onto SA8620P execution targets.
The allocation vocabulary is identical to the locked requirement schema's
`allocates_to` — the architecture never invents new targets.

## The three-step chain

```
SYS-* requirement  --realized by-->  ARC-* element  --allocated to-->  execution target
```

- A requirement may be realized by several elements (each covering part of it)
- An element realizes ≥ 1 requirement — always
- A `component` element has exactly one allocation target set
- `commands/arch/validate-arch.sh` checks the whole chain including ASIL ceilings

## Allocation drivers (in priority order)

1. **ASIL** — target ceiling is a hard limit (see `3-asil-allocation-rules.md`)
2. **Failure independence** — redundant/monitoring elements never share the target
   of what they monitor
3. **Latency** — deadline-critical paths avoid cross-domain hops
4. **Bandwidth/locality** — high-rate data stays near its producer (Hexagon-adjacent)
5. **Load** — CPU/memory budget per target `[TBD — internal budget sheet]`
