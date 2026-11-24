#!/usr/bin/env python3
"""Read-only generator of the three DRAFT records (r2). Reads git objects only; computes git blob ids in
memory (sha1 of 'blob <len>\\0' + bytes; nothing is written to the object store). Writes only into
records-draft/ and prints a report. Usage: gen_records_r2.py OUTDIR [MAIN_COMMIT]"""
import json, subprocess, hashlib, sys, os, difflib
REPO="<repo>"
H="53c6601a10419b6b333cc992474272501ab542af"; P="4c79be642ca631573f06b444903be75ec4f5e2b6"
W="413b0bb88f39cad901befcf4684355c7ee39480b"; M0="4fb2c1eed350edf95da2b316abcca93717246589"
T1="14ac71b4b0a0c0aa2d7068d6799a73f474097060"
PLAN="verification/audits/foundations/a1exit-deletion-20261121"
AUD="verification/audits/<TOOL-AUDIT-DIR>"   # placeholder: Stage 1's audit directory name is not known
OUT=sys.argv[1]; MAIN=sys.argv[2] if len(sys.argv)>2 else M0
def git(*a, raw=False):
    o=subprocess.run(["git","-C",REPO,*a],check=True,capture_output=True).stdout
    return o if raw else o.decode()
def show(c,p): return git("show",f"{c}:{p}",raw=True)
def sha(b): return hashlib.sha256(b).hexdigest()
def gblob(b): return hashlib.sha1(b"blob %d\0"%len(b)+b).hexdigest()
DRAFT=("UNREVIEWED, UNAUTHORIZED DRAFT. Not a record under DESIGN-v5.1 sec. 6.3: it has no independent "
       "review and no owner authorization, and the tool must treat it as record-invalid. Field names follow "
       "DRIFT-RECONCILIATION-PROPOSAL-r2.md and must be reconciled with the schema implemented in Stage 1 "
       "before review. The audit directory name is a placeholder.")
PLACE={"review_record":"<PLACEHOLDER: oi-review-record/1 {path, blob_sha256} naming this record's blob; separate record, written by a non-author>",
       "owner_authorization":{"schema":"oi-owner-authorization/1 (separate record)","owner":"<PLACEHOLDER: owner login>",
         "time":"<PLACEHOLDER: ISO time of the owner's comment>","comment_id":"<PLACEHOLDER: GitHub comment id>",
         "authorizes":"<PLACEHOLDER: [{record: {path, blob_sha256}, review: {path, blob_sha256}}]>"}}
def dump(o): return (json.dumps(o,indent=2,ensure_ascii=False)+"\n").encode()
def fp_commit(path):
    # first-parent commits on H..MAIN that change path (oldest first)
    return git("log","--first-parent","--reverse","--format=%H",f"{H}..{MAIN}","--",path).split()
assert subprocess.run(["git","-C",REPO,"merge-base","--is-ancestor",H,MAIN]).returncode==0
fpchain=git("rev-list","--first-parent",f"{H}..{MAIN}").split()
os.makedirs(OUT,exist_ok=True)
recs={}
# ---- side-change class records
for cid,path,cls,reason,basis in (
  ("a1exit-scc-tool-configuration-1",".claude/settings.json","tool-configuration",
   "Claude Code configuration file (attribution settings). Not a ledgered path, not a corpus path, and read by no check of the A1 plan.",
   ["#1169 comment 7099655517 (amaybaum, 2026-11-23T11:26:50Z): classified as tool configuration"]),
  ("a1exit-scc-trial-workflow-1",".github/workflows/a1exit-trial-verify.yml","trial-workflow",
   "The A1-EXIT trial workflow. PREREG section 31.12.7 at P defines W as the workflow base that decides how each trial is checked; preserve_check.py --verify-run requires this blob at every dispatch head.",
   ["#1169 comment 7099655517 (amaybaum, 2026-11-23T11:26:50Z): classified as the trial workflow",
    f"PREREG.md section 31.12.7 at {P} (workflow base W = {W})","DESIGN-v5.1 sec. 13.1 and 16.4"])):
    b=show(MAIN,path)
    fpc=fp_commit(path)
    o={"schema":"oi-side-change-classes/1","draft_status":DRAFT,"id":cid,"supersedes":None,
       "author":"<PLACEHOLDER: writer session>","scientific_base":H,
       "items":[{"item":"SC1","path":path,"class":cls,"blob":{"git":gblob(b),"sha256":sha(b)},
                 "blob_at_H":(None if subprocess.run(["git","-C",REPO,"cat-file","-e",f"{H}:{path}"],capture_output=True).returncode else {"git":gblob(show(H,path)),"sha256":sha(show(H,path))}),
                 "introduced_by_first_parent_commit":fpc[-1],
                 "ledgered":False,"corpus":False,"reason":reason,"basis":basis}],
       "checks":["blob at the resolved main equals item.blob (git id and sha256); otherwise the path is REVIEW side-change-unclassified",
                 "path is in no ledger.json files entry and in no corpus path set of the configuration"],
       "ownership_chain":PLACE}
    data=dump(o); fn=f"{cid}.json"; open(os.path.join(OUT,fn),"wb").write(data); recs[cid]=(fn,data)
# ---- reconciliation record
led=json.loads(show(P,PLAN+"/ledger.json")); ed=json.loads(show(P,PLAN+"/edits.json"))
sp=[s for s in led["splices"] if s["file"]=="AGENTS.md"]; assert len(sp)==1; sp=sp[0]
e=[x for x in ed["edits"] if x["id"]=="D296"][0]; old=e["old"].encode(); new=e["new"].encode()
aH=show(H,"AGENTS.md"); aM=show(MAIN,"AGENTS.md")
def occ(b,s):
    n=[];i=b.find(s)
    while i!=-1: n.append(i); i=b.find(s,i+1)
    return n
oH=occ(aH,old); oM=occ(aM,old); assert oH==[sp["start"]] and len(oM)==1
p=0
while p<min(len(aH),len(aM)) and aH[p]==aM[p]: p+=1
assert p>=sp["end"]; sM=oM[0]; eM=sM+len(old); assert sM==sp["start"]
assert sha(aH[sp["start"]:sp["end"]])==sp["old_sha256"]==sha(aM[sM:eM]) and sha(new)==sp["new_sha256"]
X=aH[:sp["start"]]+new+aH[sp["end"]:]; L=aM[:sM]+new+aM[eM:]
assert X==show(T1,"AGENTS.md") and sha(X)==led["files"]["AGENTS.md"]["expected_sha256"]
# byte ranges of MAIN not in H (line-based alignment; ranges in MAIN coordinates)
lh=aH.splitlines(True); lm=aM.splitlines(True); off=[0]
for x in lm: off.append(off[-1]+len(x))
ranges=[]
for t,i1,i2,j1,j2 in difflib.SequenceMatcher(None,lh,lm,autojunk=False).get_opcodes():
    if t!="equal":
        r={"op":t,"main_bytes":[off[j1],off[j2]],"main_lines":[j1+1,j2]}
        r.update({"after_H_line":i1} if i1==i2 else {"H_lines":[i1+1,i2]})
        ranges.append(r)
assert all(r["main_bytes"][0]>=eM for r in ranges)
hdr="## §A.49".encode(); assert aM.count(hdr)==1 and L.count(hdr)==1; a=aM.find(hdr); assert a>=eM
nx=aM.find(b"\n***\n",a); b_=len(aM) if nx==-1 else nx+1
d=len(new)-len(old); assert L[a+d:b_+d]==aM[a:b_] and L[eM+d:]==aM[eM:]
lines=lambda bb:bb.decode().splitlines()
assert lines(L)[35:39]==lines(X)[35:39]
others={f:v["base_sha256"] for f,v in led["files"].items() if f!="AGENTS.md"}
for f,h in others.items(): assert sha(show(MAIN,f))==h and git("rev-parse",f"{H}:{f}")==git("rev-parse",f"{MAIN}:{f}")
changed=[l.split("\t") for l in git("diff","--name-status",H,MAIN).splitlines()]
corpus=[c[-1] for c in changed if c[-1].startswith(("papers/","book/"))]; assert not corpus
scc_refs=[{"path":f"{AUD}/{recs[k][0]}","blob_sha256":sha(recs[k][1]),"git_blob":gblob(recs[k][1])} for k in recs]
o={"schema":"oi-reconciliation/1","draft_status":DRAFT,"id":"a1exit-recon-agents-md-1","supersedes":None,
 "author":"<PLACEHOLDER: writer session>","scientific_base":H,
 "main":{"computed_at":MAIN,
         "applies_while":"at every run (the pre-landing safeguard, F, landing) main is resolved by git ls-remote origin refs/heads/main and the record applies only if R1-R11 hold there: in particular AGENTS.md at that main equals paths[0].blobs.M and the first-parent commits on H..main that change AGENTS.md equal side_change_commits. The record names no later main commit, so the tool's own landing and the plan amendment do not change it; a different AGENTS.md blob means a new record with supersedes"},
 "ledger":{"path":PLAN+"/ledger.json","commit":P,"blob_sha256":sha(show(P,PLAN+"/ledger.json")),"git_blob":gblob(show(P,PLAN+"/ledger.json")),
           "note":"the ledger as frozen at P; at F, the ledger pinned in F's table"},
 "edits":{"path":PLAN+"/edits.json","commit":P,"blob_sha256":sha(show(P,PLAN+"/edits.json"))},
 "paths":[{"path":"AGENTS.md","class":"ledgered",
   "side_change_commits":fp_commit("AGENTS.md"),
   "blobs":{"H":{"git":gblob(aH),"sha256":sha(aH),"bytes":len(aH)},"M":{"git":gblob(aM),"sha256":sha(aM),"bytes":len(aM)}},
   "main_changes":ranges,
   "common_prefix_H_M_bytes":p,
   "splices":[{"id":"D296","start_H":sp["start"],"end_H":sp["end"],"start_M":sM,"end_M":eM,"translation":"identity",
               "old_sha256":sp["old_sha256"],"new_sha256":sp["new_sha256"],"old_count_H":len(oH),"old_count_M":len(oM),
               "char_offset_H":aH.decode().find(e["old"]),"lines":[aM[:sM].count(b"\n")+1,aM[:eM].count(b"\n")+1]}],
   "protected":[{"name":"§A.49","header":"## §A.49","start_M":a,"end_M":b_,"sha256":sha(aM[a:b_])}],
   "expected":{"X":{"git":gblob(X),"sha256":sha(X),"equals":f"ledger files.AGENTS.md.expected_sha256; AGENTS.md at T1' {T1}"},
               "L":{"git":gblob(L),"sha256":sha(L),"bytes":len(L)}},
   "length_delta":d,
   "resolution":"L:AGENTS.md = main's AGENTS.md with C's splices applied at main-translated offsets, each old_sha256 re-verified against main (DESIGN-v5.1 sec. 13.1; v2 sec. 13.2 'both changed')"}],
 "unchanged_ledgered":{"count":len(others),"rule":"blob at main equals blob at H, and sha256 equals base_sha256, for every other ledger files entry"},
 "unchanged_corpus":{"rule":"git diff --name-status H main lists no papers/ or book/ path and no generated corpus artifact (evaluated at run time; not a recorded list)"},
 "side_change_classes":scc_refs,
 "changes_decisions_on_X":[],
 "items":["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11","R12"],
 "item_text":{
  "R1":"main resolved by git ls-remote at F; H on main's first-parent chain; first-parent commits on H..main changing AGENTS.md equal side_change_commits",
  "R2":"AGENTS.md blob at main equals blobs.M",
  "R3":"overlapping occurrence count of D296 old bytes at H is 1, at start_H; sha256(H[start_H:end_H]) = old_sha256",
  "R4":"the same at main: count 1 at start_M; sha256(main[start_M:end_M]) = old_sha256",
  "R5":"common prefix of H and main >= end_H, so translation is identity (else the recorded delta equals the length change before start_H, and no main_changes range meets [start_M,end_M))",
  "R6":"Lx = main[:start_M]+new+main[end_M:]; Lx[start_M:start_M+len(new)] = new; sha256(new) = new_sha256; lines 36-39 of Lx equal those of H+D296 (T1')",
  "R7":"git blob id and sha256 of Lx equal expected.L",
  "R8":"git blob id and sha256 of H+D296 equal expected.X and the ledger's expected_sha256",
  "R9":"'## §A.49' occurs once in main and in Lx, at a >= end_M; Lx[a+delta:b+delta] = main[a:b] with the recorded sha256; and Lx[end_M+delta:] = main[end_M:]",
  "R10":"every other ledgered file unchanged H..main and equal to its base_sha256",
  "R11":"no corpus path changed H..main; every other changed path is covered by a referenced side-change class record (or another reviewed class record, such as the tool's landing paths or the plan amendment's paths)",
  "R12":"changes_decisions_on_X is empty"},
 "ownership_chain":PLACE}
data=dump(o); fn="a1exit-recon-agents-md-1.json"; open(os.path.join(OUT,fn),"wb").write(data); recs["recon"]=(fn,data)
print("main",MAIN,"fp chain",fpchain)
for k,(fn,data) in recs.items(): print(f"{fn}: sha256 {sha(data)} git {gblob(data)} bytes {len(data)}")
print("X",gblob(X),sha(X)); print("L",gblob(L),sha(L)); print("§A.49",a,b_,sha(aM[a:b_])); print("ranges",ranges)
print("side_change_commits",fp_commit("AGENTS.md"))
