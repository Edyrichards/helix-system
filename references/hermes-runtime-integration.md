# Hermes Runtime Integration

Helix uses Hermes as a runtime provider while remaining portable.

## Current integration

- `SKILL.md` exposes Helix as a Hermes skill.
- `scripts/verify_install.py` confirms skill visibility.
- `scripts/install_helix.sh . hermes` syncs the repo into the Hermes skill directory.

## Next integration: helix-router plugin

A future plugin should expose lazy operations:

- `helix_search_modules`
- `helix_load_reference`
- `helix_load_persona`
- `helix_plan_swarm`
- `helix_delegate_persona`
- `helix_verify_artifact`

Backing data should come from `catalog/*.json` and `runbooks/runbooks.json`, not always-loaded prompt text.

## Runtime policy

- Load references lazily.
- Delegate only when task branches are independent.
- Preserve evidence in task output, not hidden tool logs.
- Keep portable core independent of Hermes-only APIs.
