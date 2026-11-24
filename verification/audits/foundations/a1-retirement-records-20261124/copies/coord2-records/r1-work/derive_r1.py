#!/usr/bin/env python3
"""Read-only re-derivation for DRIFT-RECONCILIATION-PROPOSAL-r1.md. Reads only git objects."""
import json, subprocess, hashlib, difflib, sys
REPO="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"; P="4c79be642ca631573f06b444903be75ec4f5e2b6"
W="413b0bb88f39cad901befcf4684355c7ee39480b"; M="4fb2c1eed350edf95da2b316abcca93717246589"
PR="47e23023450fb8fcbd61b5c776a69ba61897f267"; T1="14ac71b4b0a0c0aa2d7068d6799a73f474097060"
XD="verification/audits/foundations/a1exit-deletion-20261121"
def git(*a, raw=False):
    o=subprocess.run(["git","-C",REPO,*a],check=True,capture_output=True).stdout
    return o if raw else o.decode()
def show(c,p): return git("show",f"{c}:{p}",raw=True)
def sha(b): return hashlib.sha256(b).hexdigest()
def blobid(c,p): return git("rev-parse",f"{c}:{p}").strip()
print("== first-parent H..M"); print(git("log","--first-parent","--format=%H %P | %s",f"{H}..{M}"),end="")
print("== name-status H..M"); print(git("diff","--name-status",H,M),end="")
print("== numstat H..M"); print(git("diff","--numstat",H,M),end="")
print("== name-status W..M"); print(git("diff","--name-status",W,M),end="")
ed=json.loads(show(P,XD+"/edits.json")); led=json.loads(show(P,XD+"/ledger.json"))
print("drafting_base",ed.get("drafting_base"),"records",len(ed["edits"]))
files=sorted({e["file"] for e in ed["edits"]})
print("ledgered files",len(files))
unch=[f for f in files if blobid(H,f)==blobid(M,f)]; ch=[f for f in files if f not in unch]
print("ledgered unchanged H..M:",len(unch),"changed:",ch)
# ledger.json base hashes
def walk(o):
    if isinstance(o,dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o,list):
        for v in o: yield from walk(v)
bases={}
for d in walk(led):
    if "base_sha256" in d and ("file" in d or "path" in d): bases[d.get("file",d.get("path"))]=d["base_sha256"]
print("ledger.json base entries:",len(bases), "base key:",led.get("base"))
bad=[f for f,h in bases.items() if sha(show(H,f))!=h]; print("base_sha256 mismatches at H:",bad)
badM=[f for f,h in bases.items() if sha(show(M,f))!=h]; print("base_sha256 mismatches at M:",badM)
aH=show(H,"AGENTS.md"); aW=show(W,"AGENTS.md"); aM=show(M,"AGENTS.md"); aPR=show(PR,"AGENTS.md")
for n,c,b in (("H",H,aH),("W",W,aW),("M",M,aM),("PR1553",PR,aPR)):
    print(f"AGENTS.md {n}: blob {blobid(c,'AGENTS.md')} sha256 {sha(b)} bytes {len(b)} lines {b.count(b'\n')}")
d=[e for e in ed["edits"] if e["file"]=="AGENTS.md"]; print("AGENTS.md edit ids:",[e["id"] for e in d]); d=d[0]
print("D296 keys",sorted(d.keys()))
for k in sorted(d):
    if k not in ("old","new"): print("  ",k,d[k])
old=d["old"].encode(); new=d["new"].encode()
print("old repr",repr(d["old"])); print("new repr",repr(d["new"]))
print("old sha256",sha(old),"new sha256",sha(new))
for n,b in (("H",aH),("M",aM),("PR1553",aPR)):
    o=b.find(old); print(f"D296 at {n}: count {b.count(old)} byte {o}-{o+len(old)} char {b.decode().find(d['old'])} line {b[:o].count(b'\n')+1}-{b[:o+len(old)].count(b'\n')+1}")
rH=aH.replace(old,new,1); rM=aM.replace(old,new,1); rPR=aPR.replace(old,new,1)
t1=show(T1,"AGENTS.md")
print("H+D296 sha",sha(rH),"== T1'",rH==t1)
print("M+D296 sha",sha(rM)); print("PR1553+D296 sha",sha(rPR))
# common prefix H vs M
def cp(a,b):
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]: i+=1
    return i
p=cp(aH,aM); print("first differing byte H vs M:",p,"line",aH[:p].count(b"\n")+1)
sm=difflib.SequenceMatcher(None,aH.splitlines(True),aM.splitlines(True),autojunk=False)
for op in sm.get_opcodes():
    if op[0]!="equal":
        t,i1,i2,j1,j2=op; hb=sum(len(x) for x in aH.splitlines(True)[:i1])
        print("  H..M hunk",t,"H lines",i1+1,"-",i2,"M lines",j1+1,"-",j2,"at H byte",hb, "added lines",j2-j1)
        print("    first:",aM.splitlines(True)[j1][:100])
a49=aM.find("## §A.49".encode()); print("§A.49 header byte at M",a49,"line",aM[:a49].count(b"\n")+1)
L=len(aM)-a49
print("M+D296 from §A.49 equals M from §A.49:",rM[len(rM)-L:]==aM[a49:], "delta len",len(rM)-len(aM))
print("M+D296 prefix before splice equals M prefix:",rM[:aM.find(old)]==aM[:aM.find(old)])
# line-level diff H..M == (H+D296)..(M+D296)
def dl(a,b): return [l for l in difflib.unified_diff(a.decode().splitlines(),b.decode().splitlines(),n=0,lineterm="") if l[:1] in "+-" and not l.startswith(("+++","---"))]
print("diff(H,M)==diff(H+D,M+D):",dl(aH,aM)==dl(rH,rM))
# lines 36-38 at M+D296
print("M+D296 lines 36-38:"); print("\n".join(rM.decode().splitlines()[35:38]))
print("== workflow / settings")
wf=".github/workflows/a1exit-trial-verify.yml"
for n,c in (("H",H),("W",W),("M",M),("PR1553",PR)):
    print(f"{wf} {n}: blob {blobid(c,wf)} sha256 {sha(show(c,wf))}")
for n,c in (("M",M),("PR1553",PR)):
    print(f".claude/settings.json {n}: blob {blobid(c,'.claude/settings.json')} sha256 {sha(show(c,'.claude/settings.json'))}")
print("== PR #1553")
print(git("log","--format=%H %P | %s",f"{M}..{PR}"),end="")
print("merge-base PR M:",git("merge-base",PR,M).strip())
print(git("diff","--name-status",M,PR),end="")
print(git("diff","--numstat",M,PR),end="")
p=cp(aM,aPR); print("first differing byte M vs PR:",p,"line",aM[:p].count(b"\n")+1, "D296 end at M", aM.find(old)+len(old))
sm=difflib.SequenceMatcher(None,aM.splitlines(True),aPR.splitlines(True),autojunk=False)
for op in sm.get_opcodes():
    if op[0]!="equal":
        t,i1,i2,j1,j2=op; hb=sum(len(x) for x in aM.splitlines(True)[:i1])
        print("  M..PR hunk",t,"M lines",i1+1,"-",i2,"PR lines",j1+1,"-",j2,"at M byte",hb)
print("lines 37-38 identical M vs PR:",aM.splitlines()[36:38]==aPR.splitlines()[36:38])
a49p=aPR.find("## §A.49".encode()); print("§A.49 header at PR byte",a49p, "§A.49 section identical M vs PR:", aM[a49:]==aPR[a49p:])
print("ledgered files changed M..PR:",[f for f in files if blobid(M,f)!=blobid(PR,f)])
print("PR+D296 from §A.49 unchanged:", rPR[len(rPR)-(len(aPR)-a49p):]==aPR[a49p:])
print("diff(M,PR)==diff(M+D,PR+D):",dl(aM,aPR)==dl(rM,rPR))
