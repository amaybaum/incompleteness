#!/usr/bin/env python3
"""Read-only: ledger base hashes at H and M; the plan's term regexes (edits_check.py at P) on AGENTS.md at H, M and PR #1553 head, and on lines added M..PR."""
import re, subprocess, hashlib, json
REPO="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"; M="4fb2c1eed350edf95da2b316abcca93717246589"
P="4c79be642ca631573f06b444903be75ec4f5e2b6"; PR="47e23023450fb8fcbd61b5c776a69ba61897f267"
X="verification/audits/foundations/a1exit-deletion-20261121"
def show(c,p): return subprocess.run(["git","-C",REPO,"show",f"{c}:{p}"],check=True,capture_output=True).stdout
led=json.loads(show(P,X+"/ledger.json"))
for c,n in ((H,"H"),(M,"M"),(PR,"PR1553")):
    bad=[f for f,v in led["files"].items() if hashlib.sha256(show(c,f)).hexdigest()!=v["base_sha256"]]
    print(f"ledger base_sha256 mismatches at {n}: {bad}")
d=[s for s in led["splices"] if s["file"]=="AGENTS.md"]; print("ledger AGENTS.md splices:",[(s["id"],s["start"],s["end"],s["old_sha256"]) for s in d])
for c,n in ((H,"H"),(M,"M"),(PR,"PR1553")):
    b=show(c,"AGENTS.md"); s=d[0]
    print(f"  bytes[{s['start']}:{s['end']}] sha256 at {n} == old_sha256:", hashlib.sha256(b[s['start']:s['end']]).hexdigest()==s["old_sha256"])
src=show(P,X+"/edits_check.py").decode()
names=sorted(set(re.findall(r'^([A-Z][A-Z0-9_]*) = re\.compile\(',src,re.M)))
print("compiled regex names in edits_check.py:",names)
def grab(name):
    m=re.search(r'^'+name+r' = (re\.compile\(.*?\))\n(?=\S)',src,re.M|re.S); return eval(m.group(1),{"re":re})
pats={}
for n in names:
    try: pats[n]=grab(n)
    except Exception as e: print("  could not extract",n,e)
for c,n in ((H,"H"),(M,"M"),(PR,"PR1553")):
    t=show(c,"AGENTS.md").decode()
    print(n,{k:[(t[:m.start()].count("\n")+1,m.group(0)) for m in p.finditer(t)] for k,p in pats.items() if k in ("PTR","CRIT5","REPO_PAT","IDENT")})
diff=subprocess.run(["git","-C",REPO,"diff","-U0",M,PR,"--","AGENTS.md"],check=True,capture_output=True).stdout.decode()
added="\n".join(l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++"))
print("lines added M..PR:",added.count("\n")+1)
for k,p in pats.items():
    h=[m.group(0) for m in p.finditer(added)]
    print(f"  {k}: {len(h)} {h[:5]}")
# the two non-ledgered side-change files, H and M (tree-scan patterns only)
for c,n,p in ((H,"H",".github/workflows/a1exit-trial-verify.yml"),(M,"M",".github/workflows/a1exit-trial-verify.yml"),(M,"M",".claude/settings.json")):
    t=show(c,p).decode()
    print(n,p,{k:len(list(pats[k].finditer(t))) for k in ("PTR","CRIT5","REPO_PAT","IDENT")})
