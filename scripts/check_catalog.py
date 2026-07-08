#!/usr/bin/env python3
"""Validate Helix catalogs, runbooks, personas, and referenced files."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = [ROOT/'catalog/tools.json', ROOT/'catalog/modules.json', ROOT/'catalog/personas.json', ROOT/'runbooks/runbooks.json']
MD_LINK_RE = re.compile(r'(?<!https://)(?<!http://)(?<!@)(?P<path>(?:references|personas|scripts|docs|templates|project-knowledge|source-skills|research|examples|catalog|runbooks|schemas)/[A-Za-z0-9_.\-/]+\.(?:md|py|json|sh|template|skill\.md)|(?:README|INSTALL|QUICKSTART_CLAUDE|PERSONA_CATALOG|GO_TO_MARKET|BEST_IN_CLASS_ROADMAP|SKILL|CHANGELOG)\.md)')


def load_json(path: Path):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise AssertionError(f'{path.relative_to(ROOT)} invalid JSON: {exc}')


def check_file(path: str, errors: list[str], context: str):
    p = ROOT / path
    if not p.exists():
        errors.append(f'{context}: missing {path}')


def main() -> int:
    errors: list[str] = []
    for path in CATALOGS:
        if not path.exists():
            errors.append(f'missing catalog {path.relative_to(ROOT)}')
        else:
            load_json(path)

    modules = load_json(ROOT/'catalog/modules.json').get('modules', []) if (ROOT/'catalog/modules.json').exists() else []
    for m in modules:
        check_file(m['path'], errors, f'module {m.get("id")}')

    personas = load_json(ROOT/'catalog/personas.json').get('personas', []) if (ROOT/'catalog/personas.json').exists() else []
    persona_ids = {p['id'] for p in personas}
    for p in personas:
        check_file(p['path'], errors, f'persona {p.get("id")}')

    runbooks = load_json(ROOT/'runbooks/runbooks.json').get('runbooks', []) if (ROOT/'runbooks/runbooks.json').exists() else []
    for rb in runbooks:
        for ref in rb.get('references', []):
            check_file(ref, errors, f'runbook {rb.get("slug")}')
        for script in rb.get('scripts', []):
            check_file(script, errors, f'runbook {rb.get("slug")}')
        for persona in rb.get('personas', []):
            if persona not in persona_ids:
                errors.append(f'runbook {rb.get("slug")}: unknown persona {persona}')

    # Detect obvious broken repo-relative references in primary docs.
    scan_files = [ROOT/'README.md', ROOT/'INSTALL.md', ROOT/'agent.md', ROOT/'PERSONA_CATALOG.md'] + list((ROOT/'references').glob('*.md'))
    for path in scan_files:
        if not path.exists():
            continue
        for match in MD_LINK_RE.finditer(path.read_text(errors='ignore')):
            rel = match.group('path')
            if rel.startswith('docs/en/'):
                continue
            if not (ROOT/rel).exists():
                errors.append(f'{path.relative_to(ROOT)} references missing {rel}')

    if errors:
        print('Helix catalog/docs validation FAILED')
        for e in sorted(set(errors)):
            print('-', e)
        return 1
    print('Helix catalog/docs validation PASSED')
    print(f'modules={len(modules)} personas={len(personas)} runbooks={len(runbooks)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
