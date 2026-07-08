# Helix Integrations

Generated adapters for supported agent hosts live here.

Use:

```bash
python scripts/helix_convert.py --list
python scripts/helix_convert.py --tool claude-code
python scripts/helix_convert.py --tool codex
python scripts/helix_convert.py --tool all
```

The source of truth remains the Helix repo root:

- `references/`
- `personas/`
- `project-knowledge/`
- `source-skills/`
- `scripts/`
- `catalog/*.json`
- `runbooks/runbooks.json`

Generated adapters should be reproducible from source and can be deleted/rebuilt.
