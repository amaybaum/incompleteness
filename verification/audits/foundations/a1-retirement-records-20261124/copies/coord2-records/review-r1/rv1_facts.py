#!/usr/bin/env python3
"""Independent read-only re-derivation for the r1 drift proposal. Reads only git objects."""
import json, subprocess, hashlib, re
R="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"; P="4c79be642ca631573f06b444903be75ec4f5e2b6"
W="413b0bb88f39cad901befcf4684355c7ee39480b"; M="4fb2c1eed350edf95da2b316abcca93717246589"
Q="47e23023450fb8fcbd61b5c776a69ba61897f267"; T1="14ac71b4b0a0c0aa2d7068d6799a73f474097060"
X="verification/audits/foundations/a1exit-deletion-20261121"
def g(*a): return subprocess.run(["git","-C",R,*a],check=True,capture_output=True).stdout
def show(c,p): return g("show",f"{c}:{p}")
def blobid(c,p): return g("rev-parse",f"{c}:{p}").decode().strip()
sh=lambda b: hashlib.sha256(b).hexdigest()
def occ(hay,needle):
    out=[];i=hay.find(needle)
    while i!=-1: out.append(i); i=hay.find(needle,i+1)
    return out
led=json.loads(show(P,X+"/ledger.json")); ed=json.loads(show(P,X+"/edits.json"))
print("ledger keys",list(led.keys())[:12]); print("ledger base",led.get("base"))
files=led["files"]; print("ledger files",len(files))
print("splices",len(led["splices"]))
ag=files["AGENTS.md"]; print("AGENTS entry keys",list(ag.keys()))
sp=[x for x in led["splices"] if x.get("file")=="AGENTS.md"]; print("AGENTS splices",json.dumps(sp)[:700])
print("AGENTS base",ag.get("base_sha256"),"expected",ag.get("expected_sha256"))
d=[e for e in ed["edits"] if e["id"]=="D296"][0]; old=d["old"].encode(); new=d["new"].encode()
print("sha old",sh(old),"sha new",sh(new),"len old",len(old),"len new",len(new),"delta",len(new)-len(old))
A={c:show(c,"AGENTS.md") for c in (H,M,Q,T1)}
for n,c in (("H",H),("M",M),("Q",Q)):
    b=A[c]; o=occ(b,old)
    print(n,"blob",blobid(c,"AGENTS.md"),sh(b),"len",len(b),"occ",o,"line",b[:o[0]].count(b"\n")+1,
          "slice sha==old",sh(b[2332:2382])==sh(old),"char off",len(b[:o[0]].decode()))
def pref(a,b):
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]: i+=1
    return i
print("common prefix H,M",pref(A[H],A[M]),"H,Q",pref(A[H],A[Q]),"M,Q",pref(A[M],A[Q]))
# #1552 insertion structure
h,m=A[H],A[M]; p=pref(h,m)
ins_len=354
print("M[p:p+354] + H[p:] prefix check:", m[:p]+m[p:p+ins_len]+h[p:]==m[:len(h)+ins_len], "tail start",len(h)+ins_len, "M len",len(m))
print("H tail == M[46677+354:102604]:", h[p:]==m[p+ins_len:len(h)+ins_len])
print("inserted lines 1:",m[p:p+ins_len].decode()[:60],"...",m[p:p+ins_len].decode()[-30:])
print("M line of 46677",m[:p].count(b"\n")+1,"; appended block start line",m[:len(h)+ins_len].count(b"\n")+1)
def app(b): o=b.find(old); return b[:o]+new+b[o+len(old):]
for n,c in (("H",H),("M",M),("Q",Q)):
    r=app(A[c]); print(n,"+D296 sha",sh(r))
print("H+D296 == T1'",app(A[H])==A[T1])
for n,c in (("M",M),("Q",Q)):
    b=A[c]; a=b.find(b"## \xc2\xa7A.49"); cnt=b.count(b"## \xc2\xa7A.49")
    nxt=b.find(b"\n***\n",a); end=nxt+1 if nxt!=-1 else len(b)
    a50=b.find(b"## \xc2\xa7A.50")
    r=app(b); dl=len(new)-len(old)
    print(n,"A.49 hdr",a,"count",cnt,"extent",(a,end),"sha",sh(b[a:end]),"A.50",a50,
          "after splice equal",r[2382+dl:]==b[2382:], "A49 in r",r[a+dl:end+dl]==b[a:end], r.count(b"## \xc2\xa7A.49"))
# other ledgered files
bad=[]
for f,v in files.items():
    if f=="AGENTS.md": continue
    if blobid(H,f)!=blobid(M,f) or sh(show(M,f))!=v["base_sha256"] or blobid(Q,f)!=blobid(H,f): bad.append(f)
print("other ledgered files:",len(files)-1,"bad",bad)
for c,n in ((H,"H"),(W,"W"),(M,"M"),(Q,"Q")):
    for f in (".github/workflows/a1exit-trial-verify.yml",".claude/settings.json"):
        try: print(n,f,blobid(c,f),sh(show(c,f)))
        except subprocess.CalledProcessError: print(n,f,"absent")
print("diff M..Q:",g("diff","--numstat",M,Q).decode())
print("log M..Q:",g("log","--format=%H %P %s",f"{M}..{Q}").decode())
# scans
src=show(P,X+"/edits_check.py").decode()
def grab(nm):
    mm=re.search(r'^'+nm+r' = (re\.compile\(.*?\))\n(?=\S)',src,re.M|re.S); return eval(mm.group(1),{"re":re})
pats={k:grab(k) for k in ("PTR","CRIT5","REPO_PAT","IDENT")}
for c,n in ((H,"H"),(M,"M"),(Q,"Q")):
    for f in ("AGENTS.md",".github/workflows/a1exit-trial-verify.yml",".claude/settings.json"):
        try: t=show(c,f).decode()
        except subprocess.CalledProcessError: print(n,f,"absent"); continue
        print(n,f,{k:[(t[:x.start()].count("\n")+1,x.group(0)) for x in p.finditer(t)] for k,p in pats.items()})
