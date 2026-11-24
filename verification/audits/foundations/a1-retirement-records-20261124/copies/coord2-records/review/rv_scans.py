#!/usr/bin/env python3
"""Read-only: apply the plan's own term regexes (edits_check.py at P) to AGENTS.md at H and at M, and D296 at M."""
import re, subprocess, hashlib
REPO="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"; M="4fb2c1eed350edf95da2b316abcca93717246589"
P="4c79be642ca631573f06b444903be75ec4f5e2b6"; X="verification/audits/foundations/a1exit-deletion-20261121"
def show(c,p): return subprocess.run(["git","-C",REPO,"show",f"{c}:{p}"],check=True,capture_output=True).stdout
src=show(P,X+"/edits_check.py").decode()
def grab(name):
    m=re.search(r'^'+name+r' = (re\.compile\(.*?\))\n(?=\S)',src,re.M|re.S); return eval(m.group(1),{"re":re})
pats={n:grab(n) for n in ("PTR","CRIT5","REPO_PAT","IDENT")}
for c in (H,M):
    t=show(c,"AGENTS.md").decode()
    print(c[:8],{n:[(t[:m.start()].count("\n")+1,m.group(0)) for m in p.finditer(t)] for n,p in pats.items()})
# apply D296 at M; compare with H-applied result outside the inserted regions
import json
ed=json.loads(show(P,X+"/edits.json")); d=[e for e in ed["edits"] if e["id"]=="D296"][0]
tH=show(H,"AGENTS.md").decode(); tM=show(M,"AGENTS.md").decode()
rH=tH.replace(d["old"],d["new"],1); rM=tM.replace(d["old"],d["new"],1)
print("D296 at M, lines 35-40:"); print("\n".join(rM.splitlines()[34:40]))
import difflib
print("diff(H+D296, M+D296) == diff(H, M):", list(difflib.unified_diff(rH.splitlines(),rM.splitlines(),n=0,lineterm=""))[2:]==list(difflib.unified_diff(tH.splitlines(),tM.splitlines(),n=0,lineterm=""))[2:] if False else
      [l for l in difflib.unified_diff(rH.splitlines(),rM.splitlines(),n=0,lineterm="") if l[:1] in "+-" and not l.startswith(("+++","---"))]==[l for l in difflib.unified_diff(tH.splitlines(),tM.splitlines(),n=0,lineterm="") if l[:1] in "+-" and not l.startswith(("+++","---"))])
T1="14ac71b4b0a0c0aa2d7068d6799a73f474097060"
t1=show(T1,"AGENTS.md").decode()
print("H+D296 == AGENTS.md at T1':", rH==t1, hashlib.sha256(t1.encode()).hexdigest())
print("M+D296 sha256:", hashlib.sha256(rM.encode()).hexdigest())
