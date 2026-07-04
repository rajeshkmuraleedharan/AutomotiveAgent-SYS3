# JIRA — Issue Lifecycle

Default lifecycle assumed by the agent (adjust to the internal workflow):

```
Open → In Progress → In Review → Done
   ↘ Blocked ↗           ↓
                      Reopened
```

## Rules the agent must respect

- Reference issues by key (`ADAS-NNN`) — keys are stable, summaries are not
- A Bug that violates a `SYS-*` requirement should name that requirement in analysis
  output — that link is the system-level traceability JIRA itself doesn't hold
- Proposed tickets: `NEW-` placeholder key, summary ≤ 90 chars, wiki-markup body,
  suggested component + priority with a one-line justification
- Never propose closing an issue — that's a human workflow decision

## Internal specifics (fill in)

- Actual workflow states: `[TBD]`
- Link types in use (Blocks, Relates, Duplicates…): `[TBD]`
- Fix-version naming (SW-Bxx?): `[TBD]`
