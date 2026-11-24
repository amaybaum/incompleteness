#!/usr/bin/env python3
"""Read-only re-derivation of the drift facts of DRIFT-RECONCILIATION-PROPOSAL.md from git objects."""
import json, subprocess, hashlib, sys
REPO="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"
P="4c79be642ca631573f06b444903be75ec4f5e2b6"
M="4fb2c1eed350edf95da2b316abcca93717246589"
ED="verification/audits/foundations/a1exit-deletion-20261121/edits.json"
def git(*a, raw=False):
    out=subprocess.run(["git","-C",REPO,*a],check=True,capture_output=True).stdout
    return out if raw else out.decode()
def blob(c,p): return git("show",f"{c}:{p}",raw=True)
print("first-parent H..M:")
print(git("log","--first-parent","--format=  %H %s",f"{H}..{M}"),end="")
changed=[l.split("\t") for l in git("diff","--name-status",H,M).splitlines()]
print("changed H..M:",changed)
ed=json.loads(blob(P,ED))
assert ed["drafting_base"]==H, ed["drafting_base"]
files=sorted({e["file"] for e in ed["edits"]})
print("edits:",len(ed["edits"]),"ledgered files:",len(files))
chp={c[-1] for c in changed}
print("ledgered & changed:",sorted(set(files)&chp))
print("papers/book changed:",[p for p in chp if p.startswith(("papers/","book/"))])
# any edit touching workflow or settings?
print("edits on .github/.claude:",[e["id"] for e in ed["edits"] if e["file"].startswith((".github",".claude"))])
ag=[e for e in ed["edits"] if e["file"]=="AGENTS.md"]
print("AGENTS.md edits:",[e["id"] for e in ag])
aH=blob(H,"AGENTS.md"); aM=blob(M,"AGENTS.md")
print("AGENTS.md sha256 H",hashlib.sha256(aH).hexdigest(),"M",hashlib.sha256(aM).hexdigest())
print("M startswith H:",aM.startswith(aH),"len H",len(aH),"len M",len(aM))
a49=aM.find("## §A.49".encode())
print("§A.49 header offset in M:",a49, " in H:",aH.find("§A.49".encode()))
for e in ag:
    old=e["old"].encode(); new=e["new"].encode()
    cH=aH.count(old); cM=aM.count(old)
    oH=aH.find(old); oM=aM.find(old)
    print(e["id"],"count H",cH,"M",cM,"offset H",oH,"M",oM,"line M",aM[:oM].count(b"\n")+1,
          "char-offset M",aM.decode()[:].find(e["old"]))
    rH=aH.replace(old,new,1); rM=aM.replace(old,new,1)
    print("  result M == result H + appended tail:", rM==rH+aM[len(aH):])
    print("  splice end",oM+len(old),"< §A.49 start",a49, oM+len(old)<=a49)
    print("  §A.49 onwards unchanged:", rM[len(rM)-(len(aM)-a49):]==aM[a49:])
    print("  old:",repr(e["old"][:300])); print("  new:",repr(e["new"][:300]))
    for k in ("base_sha256","sha256_old","old_sha256","new_sha256"):
        if k in e: print("  ",k,e[k])
    print("  keys:",sorted(e.keys()))
print("tail added:\n",aM[len(aH):].decode()[:400])
