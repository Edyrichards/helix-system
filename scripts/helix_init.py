#!/usr/bin/env python3
from pathlib import Path
import argparse, json, sys

def detect_package_manager(root):
    for name, pm in [('pnpm-lock.yaml','pnpm'),('yarn.lock','yarn'),('bun.lockb','bun'),('package-lock.json','npm')]:
        if (root/name).exists(): return pm
    return 'npm' if (root/'package.json').exists() else 'unknown'

def read_json(path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception: return {}

def command_for(scripts, pm, keys):
    for k in keys:
        if k in scripts: return f'{pm} run {k}' if pm not in ['npm','unknown'] else f'npm run {k}'
    return 'not found'

def find_token_files(root):
    names={'globals.css','global.css','tailwind.config.js','tailwind.config.ts','theme.ts','theme.js','tokens.css','tokens.ts','design-tokens.ts'}
    found=[]
    for p in root.rglob('*'):
        if len(found)>=8: break
        if p.is_file() and p.name in names and 'node_modules' not in p.parts and '.git' not in p.parts:
            found.append(str(p.relative_to(root)))
    return found or ['not found']

def main():
    ap=argparse.ArgumentParser(description='Generate a Helix CLAUDE.md from repo inspection')
    ap.add_argument('repo', nargs='?', default='.')
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--force', action='store_true')
    args=ap.parse_args()
    root=Path(args.repo).expanduser().resolve()
    if not root.exists(): sys.exit(f'No such repo: {root}')
    pkg=read_json(root/'package.json') if (root/'package.json').exists() else {}
    scripts=pkg.get('scripts',{}) if isinstance(pkg.get('scripts',{}),dict) else {}
    pm=detect_package_manager(root)
    deps=list((pkg.get('dependencies') or {}).keys())+list((pkg.get('devDependencies') or {}).keys())
    stack=[m for m in ['next','react','vue','svelte','vite','tailwindcss','typescript','supabase','prisma','drizzle-orm'] if m in deps] or (['node'] if pkg else [])
    dirs=[p.name+'/' for p in sorted(root.iterdir()) if p.is_dir() and p.name not in ['.git','node_modules','.next','dist','build']][:12]
    summary=pkg.get('description') or f'{root.name} project. Fill this line with who uses it and what it does.'
    arch='\n'.join(f'- `{d}`' for d in dirs) or '- Fill after repo inspection.'
    token_files=find_token_files(root)
    lines=['# CLAUDE.md','', '## Project', summary, f"Stack: {', '.join(stack) if stack else 'unknown; inspect before editing'}. Package manager: {pm}.",'','## Commands', f"- Dev: `{command_for(scripts, pm, ['dev','start'])}`", f"- Build: `{command_for(scripts, pm, ['build'])}`", f"- Test: `{command_for(scripts, pm, ['test','unit','test:unit'])}`", f"- Lint/typecheck: `{command_for(scripts, pm, ['lint','typecheck','check'])}`", '', '## Architecture map', arch, '', '## Helix Operating Style', '- Do exactly what was asked; the diff should read as one intentional change.', '- Read manifest/config and relevant files before editing.', '- Search for existing implementations and mirror the closest pattern.', '- No drive-by refactors, renames, reformatting, dependency upgrades, or bonus features.', '- End with `Verified: <actual check>` or `Implemented, unverified: <exact step>`.', '', '## Design', '- Before editing UI, identify the screen’s one job in a sentence.', '- Preserve the existing brand system unless explicitly asked to rebrand.', f"- Use design tokens from: {', '.join(token_files)}.", '- Mobile-first. Check around 375px and desktop when changing UI.', '- Handle empty, loading, error, and success states where relevant.', '- Avoid generic AI defaults: purple gradients, emoji icons, decorative blobs, fake trust claims, identical three-card grids.', '', '## Verification', '- Code: run the narrowest command that proves the change first.', '- UI: render/screenshot before claiming visual verification.', '- Bug fixes: reproduce the original symptom after the fix.', '- Research/data: cite opened sources and spot-check numbers.', '']
    content='\n'.join(lines)
    out=root/'CLAUDE.md'
    if args.write:
        if out.exists() and not args.force: sys.exit(f'{out} exists. Re-run with --force to overwrite, or redirect output and merge manually.')
        out.write_text(content, encoding='utf-8')
        print(f'Wrote {out}')
    else:
        print(content)
if __name__=='__main__': main()
