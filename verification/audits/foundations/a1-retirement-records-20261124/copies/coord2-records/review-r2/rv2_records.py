#!/usr/bin/env python3
"""Independent read-only check of every field of the r2 draft records (and the #1553 variant) against git objects."""
import json, subprocess, hashlib, sys
R="<repo>"; S="<records>/coord2-records"
H="53c6601a10419b6b333cc992474272501ab542af"; P="4c79be642ca631573f06b444903be75ec4f5e2b6"; W="413b0bb88f39cad901befcf4684355c7ee39480b"
M="4fb2c1eed350edf95da2b316abcca93717246589"; Q="47e23023450fb8fcbd61b5c776a69ba61897f267"; T1="14ac71b4b0a0c0aa2d7068d6799a73f474097060"
PD="verification/audits/foundations/a1exit-deletion-20261121"
def g(*a): return subprocess.run(["git","-C",R,*a],check=True,capture_output=True).stdout
def show(c,p): return g("show",f"{c}:{p}")
def rp(c,p): return g("rev-parse",f"{c}:{p}").decode().strip()
sh=lambda b: hashlib.sha256(b).hexdigest()
bid=lambda b: hashlib.sha1(b"blob %d\0"%len(b)+b).hexdigest()
fails=[]
def chk(name,ok,got=None):
    print(("OK  " if ok else "FAIL"),name,"" if ok else got)
    if not ok: fails.append(name)
led_b=show(P,PD+"/ledger.json"); ed_b=show(P,PD+"/edits.json"); led=json.loads(led_b); ed=json.loads(ed_b)
d=[e for e in ed["edits"] if e["id"]=="D296"][0]; old=d["old"].encode(); new=d["new"].encode()
sp=[x for x in led["splices"] if x["file"]=="AGENTS.md"]; assert len(sp)==1; sp=sp[0]
def occ(h,n):
    o=[];i=h.find(n)
    while i!=-1: o.append(i); i=h.find(n,i+1)
    return o
def pref(a,b):
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]: i+=1
    return i
def fp_changes(mainc,path):
    revs=g("rev-list","--first-parent",f"{H}..{mainc}").decode().split()
    out=[]
    for c in revs:
        par=g("rev-parse",c+"^1").decode().strip()
        if g("diff","--name-only",par,c,"--",path).strip(): out.append(c)
    return list(reversed(out))
def check_recon(rec, mainc, tag):
    print("== recon",tag)
    A_H=show(H,"AGENTS.md"); A_M=show(mainc,"AGENTS.md"); p=rec["paths"][0]
    chk("schema/id",rec["schema"]=="oi-reconciliation/1" and rec["id"]=="a1exit-recon-agents-md-1" and rec["supersedes"] is None)
    chk("draft_status marks unreviewed+unauthorized","UNREVIEWED" in rec.get("draft_status","") and "UNAUTHORIZED" in rec["draft_status"] and "record-invalid" in rec["draft_status"])
    chk("author placeholder",rec["author"].startswith("<PLACEHOLDER"))
    oc=rec["ownership_chain"]; chk("ownership placeholders", all(str(v).startswith("<PLACEHOLDER") for v in [oc["review_record"],oc["owner_authorization"]["owner"],oc["owner_authorization"]["time"],oc["owner_authorization"]["comment_id"],oc["owner_authorization"]["authorizes"]]))
    chk("scientific_base",rec["scientific_base"]==H==led["base"])
    chk("main.computed_at",rec["main"]["computed_at"]==mainc,rec["main"]["computed_at"])
    L=rec["ledger"]; chk("ledger pin",L["commit"]==P and L["blob_sha256"]==sh(led_b) and L["git_blob"]==rp(P,PD+"/ledger.json") and L["path"]==PD+"/ledger.json")
    E=rec["edits"]; chk("edits pin",E["commit"]==P and E["blob_sha256"]==sh(ed_b) and E["path"]==PD+"/edits.json")
    chk("path/class",p["path"]=="AGENTS.md" and p["class"]=="ledgered" and len(rec["paths"])==1)
    sc=fp_changes(mainc,"AGENTS.md"); chk("side_change_commits",p["side_change_commits"]==sc,(p["side_change_commits"],sc))
    bH=p["blobs"]["H"]; chk("blobs.H",bH=={"git":rp(H,"AGENTS.md"),"sha256":sh(A_H),"bytes":len(A_H)})
    bM=p["blobs"]["M"]; chk("blobs.M",bM=={"git":rp(mainc,"AGENTS.md"),"sha256":sh(A_M),"bytes":len(A_M)},bM)
    pr=pref(A_H,A_M); chk("common_prefix",p["common_prefix_H_M_bytes"]==pr,pr)
    # main_changes: verify reconstruction main = H[:a]+ins1+H[a:]+tail
    mc=p["main_changes"]; a0,b0=mc[0]["main_bytes"]; a1,b1=mc[1]["main_bytes"]
    recon=A_M[:a0]+A_H[a0:]  # remove ins1
    ok = (a0==pr and A_M[:a0]==A_H[:a0] and A_M[b0:b0+len(A_H)-a0]==A_H[a0:] and b0+len(A_H)-a0==a1 and b1==len(A_M))
    chk("main_changes byte ranges",ok,mc)
    ln=lambda b,o: b[:o].count(b"\n")+1
    chk("main_changes lines",mc[0]["main_lines"]==[ln(A_M,a0),ln(A_M,b0-1)] and mc[1]["main_lines"]==[ln(A_M,a1),ln(A_M,b1-1)] and mc[0]["after_H_line"]==ln(A_H,a0)-1 and mc[1]["after_H_line"]==A_H.count(b"\n"),
        (mc,[ln(A_M,a0),ln(A_M,b0-1),ln(A_M,a1),ln(A_M,b1-1),ln(A_H,a0)-1,A_H.count(b"\n")]))
    s=p["splices"][0]; oH=occ(A_H,old); oM=occ(A_M,old)
    chk("splice D296",s["id"]=="D296" and s["start_H"]==sp["start"]==oH[0]==2332 and s["end_H"]==sp["end"]==2382 and s["start_M"]==oM[0] and s["end_M"]==oM[0]+len(old)
        and s["translation"]=="identity" and pr>=2382 and s["old_sha256"]==sp["old_sha256"]==sh(old) and s["new_sha256"]==sp["new_sha256"]==sh(new)
        and s["old_count_H"]==len(oH)==1 and s["old_count_M"]==len(oM)==1 and s["char_offset_H"]==len(A_H[:2332].decode()) and s["lines"]==[ln(A_H,2332),ln(A_H,2381)],s)
    Lx=A_M[:2332]+new+A_M[2382:]; Xx=A_H[:2332]+new+A_H[2382:]
    pr0=p["protected"][0]; a=A_M.find("## §A.49".encode()); nx=A_M.find(b"\n***\n",a); b=nx+1 if nx!=-1 else len(A_M)
    dl=len(new)-len(old)
    chk("protected §A.49",pr0["start_M"]==a and pr0["end_M"]==b and pr0["sha256"]==sh(A_M[a:b]) and A_M.count("## §A.49".encode())==1 and Lx[a+dl:b+dl]==A_M[a:b] and Lx[2382+dl:]==A_M[2382:],(pr0,a,b))
    eX=p["expected"]["X"]; eL=p["expected"]["L"]
    chk("expected.X",eX["git"]==bid(Xx)==rp(T1,"AGENTS.md") and eX["sha256"]==sh(Xx)==led["files"]["AGENTS.md"]["expected_sha256"])
    chk("expected.L",eL["git"]==bid(Lx) and eL["sha256"]==sh(Lx) and eL["bytes"]==len(Lx),(eL,bid(Lx),sh(Lx),len(Lx)))
    chk("length_delta",p["length_delta"]==dl)
    others=[f for f in led["files"] if f!="AGENTS.md"]
    chk("unchanged_ledgered 43",rec["unchanged_ledgered"]["count"]==len(others)==43 and all(rp(H,f)==rp(mainc,f) and sh(show(mainc,f))==led["files"][f]["base_sha256"] for f in others))
    ch=g("diff","--name-only",H,mainc).decode().split()
    chk("no corpus path changed H..main",not [x for x in ch if x.startswith(("papers/","book/"))],ch)
    scc=rec["side_change_classes"]
    for e,fn in zip(scc,["a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"]):
        fb=open(f"{S}/records-draft/{fn}","rb").read()
        chk("scc ref "+fn,e["path"].endswith("/"+fn) and e["blob_sha256"]==sh(fb) and e["git_blob"]==bid(fb))
    chk("changes_decisions_on_X empty",rec["changes_decisions_on_X"]==[])
    chk("items R1-R12",rec["items"]==[f"R{i}" for i in range(1,13)] and set(rec["item_text"])==set(rec["items"]))
    return sh(Lx),bid(Lx)
def check_scc(fn,path,cls,intro,hb):
    rec=json.load(open(f"{S}/records-draft/{fn}")); it=rec["items"]; print("== scc",fn)
    chk("draft_status",("UNREVIEWED" in rec["draft_status"] and "UNAUTHORIZED" in rec["draft_status"]))
    chk("id/schema",rec["schema"]=="oi-side-change-classes/1" and rec["id"]==fn[:-5] and rec["supersedes"] is None and rec["scientific_base"]==H and len(it)==1)
    i=it[0]; b=show(M,path)
    chk("blob",i["path"]==path and i["class"]==cls and i["blob"]=={"git":rp(M,path),"sha256":sh(b)} and rp(Q,path)==rp(M,path))
    chk("blob_at_H",i["blob_at_H"]==hb)
    chk("introduced_by",i["introduced_by_first_parent_commit"]==intro and fp_changes(M,path)==[intro],fp_changes(M,path))
    chk("not ledgered",path not in led["files"] and i["ledgered"] is False and i["corpus"] is False)
    oc=rec["ownership_chain"]; chk("ownership placeholders",oc["owner_authorization"]["comment_id"].startswith("<PLACEHOLDER") and rec["author"].startswith("<PLACEHOLDER"))
rec=json.load(open(f"{S}/records-draft/a1exit-recon-agents-md-1.json")); check_recon(rec,M,"draft at M")
check_scc("a1exit-scc-tool-configuration-1.json",".claude/settings.json","tool-configuration",M,None)
wb=show(H,".github/workflows/a1exit-trial-verify.yml")
check_scc("a1exit-scc-trial-workflow-1.json",".github/workflows/a1exit-trial-verify.yml","trial-workflow",W,{"git":rp(H,".github/workflows/a1exit-trial-verify.yml"),"sha256":sh(wb)})
v=json.load(open(f"{S}/r2-work/variant-pr1553-head/a1exit-recon-agents-md-1.json")); check_recon(v,Q,"variant at Q")
# field-level diff draft vs variant
def flat(o,pre=""):
    if isinstance(o,dict):
        for k,x in o.items(): yield from flat(x,pre+"."+k)
    elif isinstance(o,list):
        for i,x in enumerate(o): yield from flat(x,f"{pre}[{i}]")
    else: yield pre,o
fa=dict(flat(rec)); fb=dict(flat(v))
print("== fields differing draft vs variant:")
for k in sorted(set(fa)|set(fb)):
    if fa.get(k)!=fb.get(k): print("  ",k,":",fa.get(k),"->",fb.get(k))
for fn in ("a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"):
    chk("variant scc identical "+fn,open(f"{S}/records-draft/{fn}","rb").read()==open(f"{S}/r2-work/variant-pr1553-head/{fn}","rb").read())
for fn in ("a1exit-recon-agents-md-1.json","a1exit-scc-tool-configuration-1.json","a1exit-scc-trial-workflow-1.json"):
    b=open(f"{S}/records-draft/{fn}","rb").read(); print(fn,sh(b),bid(b),len(b))
print("FAILS:",fails)
