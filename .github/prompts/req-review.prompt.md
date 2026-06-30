---
name: Requirements Review
description: Review selected SYS.3 requirements for ASPICE compliance, Codebeamer field completeness, and ISO 26262 safety requirement quality. Returns a scored review with rewrites.
---

Review the following SYS.3 requirements against:
1. ASPICE SYS.3 quality criteria (atomic, unambiguous, testable, traceable, consistent)
2. Codebeamer mandatory field completeness
3. ISO 26262 safety requirement rules
4. SA8620P platform allocation constraints

## Input

Paste the requirements to review below (YAML + text blocks):

```
[PASTE REQUIREMENTS HERE]
```

## Review Output

For each requirement produce:

### Scorecard

| Criterion | Result | Finding |
|-----------|--------|---------|
| Atomic — one SHALL | ✓ / ✗ | |
| No weak verbs (should/may) | ✓ / ✗ | |
| Quantified constraint (value + unit) | ✓ / ✗ | |
| Testable verification criteria | ✓ / ✗ | |
| Source traceability present | ✓ / ✗ | |
| ASIL assigned | ✓ / ✗ | |
| Safety mechanism (if ASIL ≥ A) | ✓ / ✗ | |
| Vendor reference present | ✓ / ✗ | |
| allocates_to valid target | ✓ / ✗ | |
| CB mandatory fields complete | ✓ / ✗ | |

### Rewrite

If any criterion fails, provide a corrected version of the full YAML + requirement text.

### Summary

`X / 10 criteria passed. Y requirements need rework.`
