# SYS.3 Requirements Writing Guide

How to use AutomotiveAgent-SYS3 to author SYS.3 requirements daily.

## Workflow

```
1. Open VS Code in your ADAS project (with .github/ copied from this repo)
2. Open Copilot Chat
3. Choose the right agent or prompt for your task
4. Review output with /req-review
5. Copy approved YAML + text to Codebeamer
```

## Step 1 — Choose Your Agent

| Task | Agent / Prompt |
|------|---------------|
| Draft new gPTP requirements | `@sys3-requirements-engineer` + topic: gPTP |
| Draft new HTP requirements | `@sys3-requirements-engineer` + topic: HTP |
| Draft TSC / safety reqs | `@safety-analyst` or `/sys3-safety` |
| Review requirements | `@requirements-reviewer` or `/req-review` |
| Improve verification criteria | `/verification-criteria` |

## Step 2 — Provide Context

Good prompts include:
- The feature or function being specified
- The ASIL level (if known)
- The upstream requirement or safety goal ID (if available)
- The starting requirement number (e.g., "start from SYS-GPTP-012")

Example:
```
@sys3-requirements-engineer
Draft 6 SYS.3 gPTP requirements covering grandmaster selection and BMCA tie-breaking.
ASIL: B. Start from SYS-GPTP-012. Upstream: STK-NET-003, STK-NET-004.
```

## Step 3 — Review Output

Always run `/req-review` on generated requirements before importing to Codebeamer.

The review checks: atomicity, quantification, ASIL, safety mechanisms, vendor refs, CB fields.

## Step 4 — Import to Codebeamer

See `docs/codebeamer-import-guide.md` for the import procedure.

Status on import: `Draft`. Move to `In Review` when submitted for design review.

## Requirement ID Management

Run `scripts/generate-req-id.py` to get the next available ID without gaps.

```bash
python scripts/generate-req-id.py --topic GPTP
# → Next available: SYS-GPTP-023
```
