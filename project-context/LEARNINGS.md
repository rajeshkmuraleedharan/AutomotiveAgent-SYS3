# Project Learnings

Append-only log of project experience: review feedback received, conventions discovered,
corrections from Rajesh. Read this at the start of every task (`skills/project-memory/`).
Decisions with lasting consequences get an ADR in `decisions/` instead.

Entry format:

```
## YYYY-MM-DD — {category: review-feedback | convention | correction | tool | domain}

- {1–3 bullets, each self-contained}
- Source: {where this came from — review, import, chat}
```

---

## 2026-07-04 — convention

- Platform baseline is locked project-wide: SA8620P + QNX 8 + SafeRTOS (SAIL) +
  Vector MICROSAR Adaptive + Marvell TSN + Intel PMIC. Classic AUTOSAR is out;
  never propose Classic AUTOSAR elements, BSW modules, or RTE concepts.
- Source: repo baseline / Rajesh
