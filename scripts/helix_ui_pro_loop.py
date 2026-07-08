#!/usr/bin/env python3
"""Create a Helix UI Pro Loop workspace and starter artifacts.

This is an orchestration scaffold. Agents still generate variants and perform
vision critique, but this script standardizes where behavior maps, references,
variants, screenshots, critiques, repairs, and lessons live.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--project-root', type=Path, required=True)
    ap.add_argument('--surface', required=True)
    ap.add_argument('--brief', required=True)
    ap.add_argument('--out-dir', type=Path)
    args = ap.parse_args()
    root = args.project_root.resolve()
    out = args.out_dir or root / 'design' / 'helix-memory' / 'tournaments' / datetime.now().strftime('%Y%m%d-%H%M%S')
    for sub in ['references', 'variants', 'screenshots', 'critiques', 'repairs', 'lessons']:
        (out / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        'project_root': str(root),
        'surface': args.surface,
        'brief': args.brief,
        'created_at': datetime.now().isoformat(timespec='seconds'),
        'required_steps': [
            'behavior-map',
            'reference-scout',
            'pattern-distillation',
            'generate-3-to-5-variants',
            'render-desktop-mobile',
            'behavioral-visual-jury',
            'repair-winner-twice',
            'implementation-plan-or-repo-patch',
            'verification-and-lesson-promotion'
        ],
        'references': [
            'references/13-reference-scouting.md',
            'references/14-screenshot-learning-loop.md',
            'references/15-ui-pro-tournament.md',
            'references/17-behavior-psychology-map.md',
            'references/19-behavioral-screenshot-critique.md',
            'references/20-reference-pattern-distillation.md'
        ]
    }
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (out / 'README.md').write_text(f"""# Helix UI Pro Loop Workspace

Surface: {args.surface}

Brief: {args.brief}

Follow `manifest.json` step order. Do not implement into the app until references,
variants, screenshots, visual jury, and repair evidence exist.
""")
    print(out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
