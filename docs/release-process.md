# Helix Release Process

1. Run validation:
   - `python3 scripts/check_catalog.py`
   - `python3 scripts/validate_personas.py`
   - `python3 scripts/verify_install.py`
   - `python3 -m py_compile scripts/*.py`
   - `python3 tests/run_design_autonomy_tests.py`
2. Generate integrations with `python3 scripts/helix_convert.py --tool all`.
3. Test project install in a temporary directory.
4. Update CHANGELOG.
5. Commit with conventional message.
6. Tag only after a clean clone/install verifies.
