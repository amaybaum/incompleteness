#!/usr/bin/env python3
"""Independent recomputation of the R13 ledger-binding hashes from git objects at P, plus mutation checks
of the binding function (my own implementation), and r2->r3 record diffs."""
import json, subprocess, hashlib, copy
R="<repo>"; S="<records>/coord2-records"
P="4c79be642ca631573f06b444903be75ec4f5e2b6"; H="53c6601a10419b6b333cc992474272501ab542af"
PD="verification/audits/foundations/a1exit-deletion-20261121"
show=lambda c,p: subprocess.check_output(["git","-C",R,"show",f"{c}:{p}"])
cj=lambda o: hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
bid=lambda b: hashlib.sha1(b"blob %d\0"%len(b)+b).hexdigest()
lb=show(P,PD+"/ledger.json"); eb=show(P,PD+"/edits.json"); led=json.loads(lb); ed=json.loads(eb)
fe=led["files"]["AGENTS.md"]; spl=[s for s in led["splices"] if s["file"]=="AGENTS.md"]; er=[e for e in ed["edits"] if e["file"]=="AGENTS.md"]
print("files entry",cj(fe)); print("splices",cj(spl),[s["id"] for s in spl]); print("edit records",cj(er),[e["id"] for e in er])
print("ledger blob",hashlib.sha256(lb).hexdigest(),bid(lb)); print("edits blob",hashlib.sha256(eb).hexdigest(),bid(eb))
print("ledger top-level keys",list(led.keys())); print("retained_unchanged type",type(led["retained_unchanged"]).__name__, str(led["retained_unchanged"])[:300])
print("AGENTS in retained_unchanged:", "AGENTS.md" in json.dumps(led["retained_unchanged"]))
print("edits top-level keys",list(ed.keys()))
print("AGENTS mentions in other edits records (mirror_of/site):",[e["id"] for e in ed["edits"] if e["file"]!="AGENTS.md" and "AGENTS.md" in json.dumps({k:e.get(k) for k in ("site","mirror_of","file")})])
rec=json.load(open(f"{S}/records-draft-r3/a1exit-recon-agents-md-1.json")); b=rec["ledger_binding"]
want=(cj(fe),cj(spl),cj(er))
print("record matches:",(b["agents_files_entry"]["sha256"],b["agents_splices"]["sha256"],b["agents_edit_records"]["sha256"])==want, b["agents_files_entry"]["value"]==fe, b["ledger_base"]==led["base"]==H)
print("edits.git_blob ok:",rec["edits"]["git_blob"]==bid(eb), "ledger git ok:",rec["ledger"]["git_blob"]==bid(lb))
def r13(L,E):
    if L.get("base")!=H: return False
    f=L.get("files",{}).get("AGENTS.md")
    if f is None: return False
    s=[x for x in L["splices"] if x["file"]=="AGENTS.md"]; e=[x for x in E["edits"] if x["file"]=="AGENTS.md"]
    return (cj(f),cj(s),cj(e))==want
cases={}
cases["P5 at P"]=(led,ed,True)
L=copy.deepcopy(led);E=copy.deepcopy(ed)
o=[s for s in L["splices"] if s["file"]!="AGENTS.md"][0]; o["new"]=o.get("new","")+"x"; L["edits_sha256"]="0"*64
oe=[e for e in E["edits"] if e["file"]!="AGENTS.md"][0]; oe["reason"]+="x"; cases["P6 other-file amendment"]=(L,E,True)
def mut(fn):
    L=copy.deepcopy(led);E=copy.deepcopy(ed);fn(L,E);return L,E
def d296(L): return [s for s in L["splices"] if s["id"]=="D296"][0]
cases["N12 new changed"]=(*mut(lambda L,E: d296(L).__setitem__("new","including\n  X (A5),")),False)
cases["N13 expected changed"]=(*mut(lambda L,E: L["files"]["AGENTS.md"].__setitem__("expected_sha256","0"*64)),False)
cases["N14 span shift"]=(*mut(lambda L,E: (d296(L).__setitem__("start",2333),d296(L).__setitem__("end",2383))),False)
cases["N15 extra splice"]=(*mut(lambda L,E: L["splices"].append(dict(d296(L),id="D999",start=102700,end=102710))),False)
cases["N16 edit reason"]=(*mut(lambda L,E: [e for e in E["edits"] if e["id"]=="D296"][0].__setitem__("reason","x")),False)
cases["N17 entry removed"]=(*mut(lambda L,E: L["files"].pop("AGENTS.md")),False)
cases["N18 base"]=(*mut(lambda L,E: L.__setitem__("base","0"*40)),False)
# extra cases of my own
cases["X1 splice order swapped with another file (AGENTS-only order unchanged)"]=(*mut(lambda L,E: L["splices"].reverse()),True)
cases["X2 new AGENTS edit record only in edits.json"]=(*mut(lambda L,E: E["edits"].append(dict([e for e in E["edits"] if e["id"]=="D296"][0],id="D998"))),False)
for k,(L,E,exp) in cases.items():
    got=r13(L,E); print(("OK  " if got==exp else "FAIL"),k,"R13",got,"expected",exp)
# r2 -> r3 diffs
def flat(o,pre=""):
    if isinstance(o,dict):
        for k,x in o.items(): yield from flat(x,pre+"."+k)
    elif isinstance(o,list):
        for i,x in enumerate(o): yield from flat(x,f"{pre}[{i}]")
    else: yield pre,o
for fn in ("a1exit-recon-agents-md-1.json","a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"):
    a=dict(flat(json.load(open(f"{S}/records-draft/{fn}")))); b2=dict(flat(json.load(open(f"{S}/records-draft-r3/{fn}"))))
    ks=[k for k in sorted(set(a)|set(b2)) if a.get(k)!=b2.get(k)]
    print("== r2->r3",fn,len(ks),"fields differ"); [print("   ",k) for k in ks]
a=dict(flat(rec)); v=dict(flat(json.load(open(f"{S}/r3-work/variant-pr1553-head/a1exit-recon-agents-md-1.json"))))
print("== draft-r3 -> variant-r3 recon"); [print("   ",k,":",a.get(k),"->",v.get(k)) for k in sorted(set(a)|set(v)) if a.get(k)!=v.get(k)]
for fn in ("a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"):
    print("variant identical",fn,open(f"{S}/records-draft-r3/{fn}","rb").read()==open(f"{S}/r3-work/variant-pr1553-head/{fn}","rb").read())
for fn in ("a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"):
    bb=open(f"{S}/records-draft-r3/{fn}","rb").read(); print(fn,hashlib.sha256(bb).hexdigest(),bid(bb))
print("recon side_change_classes:",json.dumps(rec["side_change_classes"]))
print("unchanged_ledgered:",json.dumps(rec["unchanged_ledgered"]))
print("draft_status:",rec["draft_status"][:200])
