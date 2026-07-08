#!/usr/bin/env python3
"""Generate Helix adapters for supported agent hosts.

This is clean-room converter scaffolding: Helix source remains references/personas/scripts;
adapters are reproducible generated output under integrations/<tool>/ or a chosen --out dir.
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_catalog():
    return json.loads((ROOT/'catalog/tools.json').read_text())['tools']


def copy_common(out: Path):
    (out/'references').mkdir(parents=True, exist_ok=True)
    (out/'personas').mkdir(parents=True, exist_ok=True)
    for rel in [
        'references/00-operating-contract.md',
        'references/08-intake-sufficiency-prompt-restructuring.md',
        'references/12-prompt-reprompt-engine.md',
        'references/10-design-reasoning-engine.md',
        'references/11-advanced-design-psychology.md',
        'PERSONA_CATALOG.md',
        'GO_TO_MARKET.md',
    ]:
        src=ROOT/rel
        if src.exists():
            dest=out/rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
    for src in (ROOT/'personas').glob('*.md'):
        shutil.copy2(src, out/'personas'/src.name)


def render_claude(out: Path):
    copy_common(out)
    (out/'.claude/skills').mkdir(parents=True, exist_ok=True)
    for src in (ROOT/'source-skills').glob('*.skill.md'):
        shutil.copy2(src, out/'.claude/skills'/src.name)
    shutil.copy2(ROOT/'master-claude-project-instructions.md', out/'CLAUDE.md')


def render_codex(out: Path):
    copy_common(out)
    text = (ROOT/'master-claude-project-instructions.md').read_text()
    text += '\n\n## Helix Portable Bundle\nLoad references/ and personas/ lazily according to PERSONA_CATALOG.md and catalog/modules.json.\n'
    (out/'AGENTS.md').write_text(text)


def render_generic(out: Path):
    copy_common(out)
    shutil.copy2(ROOT/'README.md', out/'README.md')
    shutil.copy2(ROOT/'INSTALL.md', out/'INSTALL.md')
    (out/'catalog').mkdir(exist_ok=True)
    for src in (ROOT/'catalog').glob('*.json'):
        shutil.copy2(src, out/'catalog'/src.name)


def render_hermes(out: Path):
    render_generic(out)
    shutil.copy2(ROOT/'agent.md', out/'SKILL.md')


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--tool', default='generic-markdown', help='tool id or all')
    ap.add_argument('--out', default=None, help='output directory; default integrations/<tool>')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args=ap.parse_args()
    tools={t['id']:t for t in load_catalog()}
    if args.list:
        for t in tools.values(): print(f"{t['id']}\t{t['label']}\t{t['format']}")
        return 0
    selected=list(tools) if args.tool=='all' else [args.tool]
    missing=[t for t in selected if t not in tools]
    if missing:
        raise SystemExit(f'Unknown tool(s): {missing}')
    for tool in selected:
        out=Path(args.out) if args.out and len(selected)==1 else ROOT/'integrations'/tool
        print(f'generate {tool} -> {out}')
        if args.dry_run: continue
        if out.exists(): shutil.rmtree(out)
        out.mkdir(parents=True)
        if tool in ('claude-code','cursor'):
            render_claude(out)
        elif tool=='codex':
            render_codex(out)
        elif tool=='hermes':
            render_hermes(out)
        else:
            render_generic(out)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
