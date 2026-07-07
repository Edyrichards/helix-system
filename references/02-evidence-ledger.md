# Helix Evidence Ledger

Before reporting progress or completion, audit every claim against evidence from this run.

## Ledger format

```md
## Evidence ledger
| Claim | Evidence | Status |
|---|---|---|
| <what I claim> | <tool output/path/source/screenshot/command> | ✅ verified / ⚠️ unverified / ❌ failed |
```

## Evidence types
- File exists/read: absolute or repo-relative path + what was read/written.
- Command: exact command + exit status + important output.
- UI: screenshot path, viewport, route, and visible issue checked.
- Research: URL opened + claim supported.
- Data: row/column counts, duplicate count, spot-checks.
- Handoff: named files/materials included and verification labels applied.

## Reporting rule
Only include claims in the final summary that appear in the ledger as ✅ or clearly label ⚠️/❌. Do not convert planned work into past-tense progress.

## Failure honesty
If verification fails, say what failed with the evidence and give the next smallest fix. Do not bury failure behind “mostly done.”
