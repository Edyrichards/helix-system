#!/usr/bin/env python3
from pathlib import Path
import argparse, json
CHECKS={'specificity':['specific','exact','file','path','class','value','token','command'],'verification':['verified','screenshot','render','test','ran','source','evidence','checked'],'scope':['not doing','scope','smallest','no refactor','assumption'],'design':['screen job','mobile','desktop','empty','loading','error','success','tokens'],'research':['findings','patterns','gaps','recommendation','source','cite','http']}
def score(text):
    lower=text.lower(); out={}; total=0
    for name,words in CHECKS.items():
        hits=sum(1 for w in words if w in lower); pts=min(2,hits); out[name]=pts; total+=pts
    out['total_heuristic']=total; out['note']='Heuristic only; use Helix rubric/verifier for final score.'; return out
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('files', nargs='+'); args=ap.parse_args()
    for f in args.files:
        p=Path(f); print(json.dumps({'file':str(p), **score(p.read_text(encoding='utf-8',errors='replace'))}, indent=2))
