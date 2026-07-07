#!/usr/bin/env python3
from pathlib import Path
import argparse, datetime, subprocess, json, re
HOME=Path.home(); agent=HOME/'.hermes/agents/helix-system'

def parse_tests(text):
    tests=[]; current=None
    for line in text.splitlines():
        m=re.match(r'## Test \d+:\s*(.+)', line)
        if m:
            if current: tests.append(current)
            current={'name':m.group(1),'lines':[]}
        elif current:
            current['lines'].append(line)
    if current: tests.append(current)
    return tests

def extract_prompt(lines):
    joined='\n'.join(lines)
    m=re.search(r'\*\*Prompt:\*\*\s*"([\s\S]*?)"', joined)
    if m: return m.group(1).strip()
    m=re.search(r'Prompt:\s*\n\s*>\s*(.+)', joined)
    if m: return m.group(1).strip()
    return joined[:500]

def main():
    ap=argparse.ArgumentParser(description='Prepare or run Helix eval prompts')
    ap.add_argument('--run-model', action='store_true')
    ap.add_argument('--limit', type=int, default=3)
    args=ap.parse_args()
    ts=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    out=agent/'evals'/'runs'/ts; out.mkdir(parents=True, exist_ok=True)
    suite=(agent/'prompts/helix-test-suite.md').read_text(encoding='utf-8')
    tests=parse_tests(suite)[:args.limit]
    manifest=[]
    for i,t in enumerate(tests,1):
        prompt=extract_prompt(t['lines'])
        fname=f'{i:02d}-{t["name"].lower().replace(" ","-")}-prompt.txt'
        (out/fname).write_text(prompt, encoding='utf-8')
        manifest.append({'id':i,'name':t['name'],'prompt':prompt,'prompt_file':fname})
        if args.run_model:
            for mode,cmd in [('baseline',['hermes','chat','-q',prompt]),('helix',['hermes','-s','helix-system','chat','-q',prompt])]:
                try:
                    r=subprocess.run(cmd,capture_output=True,text=True,timeout=300)
                    (out/f'{i:02d}-{mode}.txt').write_text(r.stdout+'\n--- stderr ---\n'+r.stderr, encoding='utf-8')
                except Exception as e:
                    (out/f'{i:02d}-{mode}.txt').write_text(f'ERROR: {e}', encoding='utf-8')
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2), encoding='utf-8')
    report='# Helix eval run\n\n'+f'Run: `{ts}`\n\nMode: {"model run" if args.run_model else "prepare only"}\n\n'
    for m in manifest:
        report+=f'## {m["id"]}. {m["name"]}\n\nPrompt file: `{m["prompt_file"]}`\n\nScore manually or with `score_output.py`.\n\n'
    (out/'report.md').write_text(report, encoding='utf-8')
    print(out)
if __name__=='__main__': main()
