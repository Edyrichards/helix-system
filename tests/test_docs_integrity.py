#!/usr/bin/env python3
"""Docs/catalog integrity tests for the lightweight Helix test runner."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, timeout=60)
    if p.returncode != 0:
        raise AssertionError(f"command failed: {' '.join(cmd)}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}")
    return p.stdout + p.stderr


def main() -> int:
    run([sys.executable, 'scripts/check_catalog.py'])
    run([sys.executable, 'scripts/validate_personas.py'])
    for rel in [
        'SKILL.md',
        'catalog/tools.json',
        'catalog/modules.json',
        'catalog/personas.json',
        'runbooks/runbooks.json',
        'references/architecture.md',
        'references/hermes-takeover-contract.md',
        'references/safety-security-model.md',
    ]:
        if not (ROOT/rel).exists():
            raise AssertionError(f'missing required file {rel}')
    print('PASS test_docs_integrity_catalogs_and_required_files')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
