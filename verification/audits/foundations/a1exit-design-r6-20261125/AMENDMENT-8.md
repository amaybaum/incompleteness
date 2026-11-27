# r6 amendment 8: minimum-sufficient path to A1 retirement (paper draft r2)

**Status.** Paper draft r2. It answers the focused review of r1 on #1630, which accepted every item except M8-3 (REVISE).
r2 replaces M8-3's rule with the reviewer's rule, adds the generated row list (appendix A), aligns C-5 in M8-5 and applies
the two nits. It goes to the owner for adoption at DP-1 (sec. 5).
Until then it changes nothing. Adoption, implementation, staging, freeze, trials, execution and merges keep their
separate gates. On adoption, a generator-amendment8 applies the adopted wording to DESIGN-r6.md, EXPECTATIONS.json and
REQUIREMENTS.json, as generator-amendment1 to generator-amendment6 did. The changes to the plan (#1477) and to staging
r2 are made by the plan amendment (checklist row 4.1) and by the tool revision. This amendment only fixes their content.

**Owner directions.** Quoted:

- amaybaum, 2026-11-27T08:39:51Z (#1169 comment 7213780573): "Minimize the remaining A1 retirement requirements to
  those strictly necessary for correctness and scientific integrity." and "Identify remaining obligations that are
  redundant, disproportionate or exclusively administrative, and propose their removal through one consolidated
  amendment where necessary." and "Maintain fail-closed behaviour for substantive correctness requirements, but remove
  unnecessary procedural blockers through explicit design corrections."
- amaybaum, 2026-11-27T08:47:14Z (#1169 comment 7213920280): "Prefer removing redundant requirements entirely over
  designing simpler replacements for them." and "We should not spend additional effort simplifying completed
  infrastructure unless it actively obstructs retirement or future research."

**Placement.** This is the eighth r6 amendment, numbered after AMENDMENT-7.md in this directory, because most clauses it
changes are r6 clauses (sec. 32 and the gate). Its staging r2 and custody items name their clauses exactly.

**Goal link (AGENTS.md sec. A.47).** Serves A1 retirement (#1477, #1169). It decides which of the remaining
obligations gate retirement. It does not decide whether A1 is retired.

**Safety rule.** No removal weakens a check that decides A1 retirement. No removal lets a category-3 finding be lost or
lifted. No removal turns a failure into a pass. Every removal names what is lost. No new mechanism is introduced: where
a row stops gating, it is recorded NOT RUN with its reason under the existing R6.GATE.15.

## 1. Preserved verification

Completed verification stays as it is and is not repeated without a concrete reason. This covers:

- every accepted independent review on #1577 (r1 to r29 and the delta reviews), on PRs #1593, #1601, #1605, #1616,
  #1617, #1618, #1620 and #1628, and on #1477 through PREREG sec. 31;
- the controls that hold, including:
  - custody 120/120 and adjudication 38/38 at `b2d0e45d3` (#1577 comment 7211786545);
  - staging 107/107 and OBL-29 144/144 at the tool head `0e201f2d9` (focused review on #1630);
- the history-cost run (#1577 comment 7208907628);
- adverse findings and scoped negative results, including the W1-a REVISE and the five baseline conformance FAILs.

None of this is re-opened by this amendment.

## 2. Removals

Each entry gives: the clause, the change, the reason, what is lost, and why correctness is unaffected.

**M8-1. Operational custody becomes conditional.**
- *Clauses.* Custody design (`a1exit-obl29-custody-20261126/DESIGN.md`) sec. 12 items 5 and 9 and R6.CUST.10, as
  gates on A1 retirement; checklist rows 3.1–3.4, 5.3 and 8.3; OBL-29 "Discharged by".
- *Change.* The following are required only before the first freeze of a discharge-bearing configuration (custody
  design sec. 1):
  - designation of B0;
  - the bootstrap blob;
  - the custody file;
  - R6.CUST.10 activation;
  - the `freeze` and `close` entries.
  The A1 configuration, if not discharge-bearing, needs none of them. OBL-29 is discharged by the R\* walk (r9
  R6.OBL29.1 and .7), implemented and independently accepted, once the tool lands.
- *Reason.* R6.CUST.9 applies only "for every cited reassessment discharge". The deletion defect of OBL-29 is closed by
  R\*, which "needs no custody" (custody design sec. 1).
- *Lost.* Nothing for a run that cites no discharge.
- *Correctness.* A cited discharge without established custody already fails (`custody-missing`, and `custody_unverified`
  when there is no report). If a finding arises before execution, there are two routes:
  - drop the bound edit (R6.RECON.26), which needs no custody;
  - activate custody first.

**M8-2. RT-L2 and RT-O9-L2 stop gating the tool's landing.**
- *Clauses.* Sec. 32 OBL-13 and OBL-14 ("Gates: the tool's landing"); the matching rows of the sec. 32 trace table;
  OBL-28 C-29; checklist row 2.12.
- *Change.* Both rows are recorded NOT RUN at the tool's landing. The drift check runs once, at the A1 retirement
  landing, on the real `M`, with the reconciliation records of checklist row 4.6 and the four-tree check RT-L.
- *Reason.* A reviewed record against a predicted `M0` decays each time `main` moves.
- *Lost.* An early demonstration on a predicted `M0`.
- *Correctness.* The same check decides the same question on the tree that actually lands.

**M8-3. The landing gate covers the A1 path only.**
- *Clauses.* R6.GATE.12 (orphan requirements and rows); R6.CTRL.3's both-directions scope; OBL-20; OBL-25; OBL-28 C-1,
  C-3 and C-26; the blockers B1 to B3 recorded in the implementation plan.
- *Change.* The rule is computed once, from the inputs of appendix A. A row of EXPECTATIONS.json stays in the gate
  when any of the following holds:
  - (k1) `a1_controls.py` or `a1_conformance.py` runs it;
  - (k2) it is a row of sec. 3's necessary list: TR5, RT-T, RT-T0, S11-2a, S11-2b, S11-2c, RT-L, EI14-dispatch, G-A1;
  - (k3) it cites, or is listed as a control of, a requirement of R6.PLAN, ITEM2, TREE, RDIR, HP, HIT, CTX, DENY,
    PROF, RULE, CLASS, DELEG, ANCH, PUR, RECON, OBL29, CUST, ADJ, REC, CFG or A1CFG.

  Only the following rows are dropped:
  - the `MUT:` rows (M8-4), which are dropped even where (k3) would keep them;
  - the gate self-test rows that (k1) to (k3) do not keep. The gate's own self-test still runs, as R6.GATE requires;
  - rows whose only purpose is generality: their only requirements beyond R6.CTRL and R6.GATE are R6.SYN or R6.CORE,
    or they are Z9-style purity rows outside (k1) to (k3).

  Every other row stays. Every row paired, composed or depended on by a kept row stays too. Dropped rows are recorded
  NOT RUN with the reason "outside the A1 path (amendment 8)". Kept rows keep both their directions; in particular
  the pair RT-T / RT-T0 is kept with both directions. A testable requirement without a control outside (k3) is
  verified by review. TR28 is covered by its components.

  Result (appendix A): 484 of 619 rows kept and 135 dropped (107 `MUT:`, 24 gate self-test, 3 R6.SYN, 1 Z9). All 10
  `paired_with` rows and their partners are kept.
- *Reason.* As adopted, the gate cannot hold without expectation changes (B1–B3), and much of it tests generality that
  A1 does not use.
- *Lost.* Evidence that the tool is correct for configurations other than A1. A later configuration must establish that
  before it relies on the tool.
- *Correctness.* Every check that decides A1 keeps its rows. Retained rows keep both directions, fail closed, and stay
  in OBL-19, OBL-21 and the fail-open OBL-28 rows.

**M8-4. The mutation evidence obligation is removed.**
- *Clauses.* OBL-24; OBL-28 C-28; R6.GATE.10; the word "mutation" in R6.PLACE.11's local suite; the `MUT:` rows (NOT
  RUN).
- *Change.* No mutation re-establishment gates the landing.
- *Reason.* Redundant with the targeted mutation probes recorded in each accepted unit review on #1577.
- *Lost.* Systematic mutants on code that no reviewed unit touched. The seven known survivors stay recorded as
  limitations.
- *Correctness.* Control strength on the changed units rests on the recorded probes. No verdict changes.

**M8-5. Diagnostic-only implementation rows are removed.**
- *Clauses.* OBL-28 C-7, C-11, C-12, C-14, C-15, C-22, C-23, C-24, RE-13, RE-27 and RE-29, and C-5 for the rows that
  M8-3 drops (C-5 stays for every kept row).
- *Change.* These rows stop gating.
- *Reason.* Each row changes an error class, a field name, a diagnostic or a purpose note.
- *Lost.* Uniform error reporting.
- *Correctness.* Both the current and the corrected behaviour fail closed. No pass or fail outcome changes.

**M8-6. RE-18 is removed.**
- *Clause.* OBL-28 RE-18 (the regeneration procedure for derived artifacts at `L`, OC-4).
- *Reason.* Redundant with:
  - the plan's sec. 11 item 3 (builds);
  - `preserve_check.py --pdf-compare` against the CI-built PDFs;
  - the T1′ trial.
  Each of these regenerates and compares independently.
- *Lost.* A second procedure for the same comparison.
- *Correctness.* The derived artifacts are still regenerated and compared before landing.

**M8-7. The identifier migration is removed.**
- *Clauses.* OBL-22; the sentence in sec. 34 applying the migration in the tool revision.
- *Change.* Identifiers stay as implemented. MIGRATION.json stays as the index.
- *Reason.* Names only.
- *Lost.* Uniform identifiers.
- *Correctness.* Names only; no check changes.

**M8-8. Implementation certification stops gating retirement.**
- *Clauses.* OBL-26; R6.STAT.10's certification bullet as a precondition of use.
- *Change.* None of this gates A1 retirement.
- *Reason.* Redundant with the accepted unit reviews, the final delta review (M8-12) and the gate of M8-3.
- *Lost.* A second read-only conformance pass after landing.
- *Correctness.* The same requirements are checked by the controls and the reviews.

**M8-9. Obligations discharged by others.**
- *OBL-2.* Narrowed to "measured during design, not retained", which OBL-2 itself allows. OBL-1's retained script and
  its seeded counts are the evidence.
- *OBL-6.* Discharged by OBL-3.
- *OBL-7.* Discharged by OBL-15.
- *OBL-23.* Discharged by the representative-snapshot runs.
- *OBL-12, ESC-1 to ESC-4.* Discharged by records re-derived on `main` at the final H:
  - the allow root (ESC-1);
  - the OBL-1 script (ESC-2);
  - the configuration's scope record (ESC-3);
  - the hit classifications of OBL-15 (ESC-4).
- *ESC-6.* Goes with the tool revision's README.
- *Reason.* The same evidence is not required twice.
- *Lost.* Nothing.
- *Correctness.* Each obligation's content is still discharged.

**M8-10. The staging activation is folded into the designation of F.**
- *Clause.* Staging r2 sec. 2, "In a later, separately approved activation, the owner records one verified preparation
  commit `B` and the path and SHA-256 of each root at `B`".
- *Change.* No separate activation record is made. The transition descriptor pinned by F's Record pins table carries
  `B` and the root digests. The owner's designation of F quotes it.
- *Reason.* The same digests are bound twice.
- *Lost.* One owner record.
- *Correctness.* The owner still binds the same digests, at F. The tool's checks of the descriptor are unchanged.

**M8-11. The designs land with the tool.**
- *Clause.* R6.PLACE.8 (the landing paths).
- *Change.* The paths also cover `a1exit-staging-amendment-20261126/` and `a1exit-adjudication-design-20261126/`.
- *Reason.* This avoids two separate landings.
- *Lost.* Nothing.
- *Correctness.* The designs are on `main` no later than the tool that implements them (sec. A.42 item 2).

**M8-12. Delta reviews replace full reviews.**
- *Clauses.* R6.PLACE.11 ("independent implementation review against r6"); for the plan amendment, PREREG sec. 25.7
  item 3 and sec. 31.12.18 item 10.
- *Change.* Each review is a focused delta review of what changed since the last accepted head.
- *Reason.* The owner directs focused delta reviews over repeated full reviews.
- *Lost.* Re-reading of text that is already accepted.
- *Correctness.* Every change is still independently reviewed.

**M8-13. The CI diagnostic is optional.**
- *Clause.* PREREG sec. 31.12.18 item 9 (the `verify.yml` diagnostic on the T0′ ref), carried into the plan amendment.
- *Change.* The diagnostic is optional. If it is used, it runs under the DP-3 launch approval.
- *Reason.* The T1′ trial decides the same jobs on the predicted tree.
- *Lost.* An early warning before F.
- *Correctness.* A failure in T1′ still blocks execution.

**M8-14. OBL-10's form clause is removed.**
- *Clause.* OBL-10, "The amendment refers to no authority record, freeze ledger, comment form or automated
  authorization check."
- *Change.* The sentence is removed. The pins and execution-identity sentences stay.
- *Reason.* A constraint on form only.
- *Lost.* Nothing.
- *Correctness.* Unaffected.

**M8-15 (for the owner to confirm). r6 adoption.** R6.STAT.1 and the title of DESIGN-r6.md read "draft, not adopted",
and no single adoption record was found. The owner confirms at DP-1 that r6 with amendments 1 to 7 is adopted, quoting
the confirmation. The generator then corrects R6.STAT.1 and the title in place (AGENTS.md sec. A.27).

## 3. What stays necessary

**Tool (#1577):**
- the S-2 implementation;
- the representative-snapshot runner (OC-3);
- the gate holding on the rows of M8-3, including OBL-19, OBL-20 and OBL-25 on those rows, OBL-21, and OBL-28 C-9,
  C-13, C-16, C-17, C-18, C-19, C-25, Q12 and Q13;
- the S11-2c CK5 evidence;
- a disposition of each of the five conformance FAILs;
- one CI validation run of the exact commit (R6.PLACE.11);
- a delta review;
- the merge.

**Staging:**
- the plan amendment (row 4.1, with OBL-4, OBL-5, OBL-8, OBL-9 and the rest of OBL-10), re-based to the final H (S-3);
- OBL-1;
- OBL-3, the allow root and the rule records;
- OBL-15, with RT-T PASS at the candidate F;
- OBL-11 and its descriptors;
- OBL-27.

**Freeze, trials and execution:**
- the pre-freeze gate items 1–8;
- TR5 and the sec. A.39 check-run at F;
- T0′/T1′, including the FULL.pdf correction;
- EI14-dispatch;
- the independent scientific delta review (7.1);
- the final regression audit (#1468);
- the plan's sec. 11 checks 1–14;
- the reconciliation records at `M` and RT-L;
- a merge-commit landing;
- TeX/PDF regeneration and the census update.

## 4. Recommendation on H (not a rule unless the owner adopts it)

`main` has moved 396 commits past the current H `53c6601a`, with 30 files changed under `papers/` and `book/`. Every
record pinned at H decays as `main` moves. The recommendation:
- choose H only after the tool lands;
- keep the window from H to the retirement landing short;
- during that window, merge nothing that touches a ledgered or corpus path, except the retirement itself.

## 5. Decisions

| DP | Content | AGENTS.md sec. A.50 |
|---|---|---|
| DP-1 | adopt this amendment (with M8-15), the S-4 default EXPLAINED handling, and authorization and a writer for #1468; optionally adopt sec. 4 | none reserved |
| DP-2 | the tool's CI validation launch, and the merge of #1577 conditional on green CI and an accepted delta review | item 1 |
| DP-3 | the pre-freeze dispatches, the designation of F (including M8-10), and the T0′/T1′ and EI14 dispatches | items 2, 5 |
| DP-4 | execution, including the narrow SC-42 regeneration approval, and the landing merge conditional on checks 1–14 green, RT-L, and 7.1 and 7.2 accepted | items 1, 2, 6 |

DP-3 and DP-4 may be given as one conditional approval if the owner chooses.

## 6. References (AGENTS.md sec. A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| DESIGN-r6.md, EXPECTATIONS.json, REQUIREMENTS.json on `main` | the clauses changed; the B1–B3 conditions, checkable from these files | support on `main` |
| custody design and r9 design on `main` (R6.CUST.9, sec. 1; R6.OBL29.1, .7) | M8-1's reasoning | support on `main` |
| #1169 comments 7213780573 and 7213920280 | the owner directions, quoted with author and time | owner record, quoted here |
| tool branch `tools/a1-ledger-coverage-r6` at `eeeaee74e`: `engine/category3.py` (`custody_problems`), `engine/custody.py`; IMPLEMENTATION-PLAN-r6 secs. 7 and 14 | confirms M8-1 and M8-3 against the code; the 89-of-572 count | provenance (each removal rests on the design text on `main`) |
| staging r2 `AMENDMENT.md` sec. 2 on the tool branch | the clause M8-10 changes | provenance here; it lands with the tool (M8-11) |
| PREREG.md on PR #1477 at `4c79be642` (secs. 25.7, 31.12.18) | the plan clauses of M8-12 and M8-13 | provenance here; those changes are made by the plan amendment |
| #1577 reviews r1–r29 and comment 7211786545; checklist v2 (#1169 comment 7209180142) and v3 (#1577 comment 7210380649) | the preserved verification and the statuses | provenance |
| tool branch `tools/a1-ledger-coverage-r6` at `0e201f2d9`: `tools/ledger_coverage/adapters/a1_controls.py` (blob `03aabb3a53faa47dd7dba178a3c1df86741e621e`) and `a1_conformance.py` (blob `335960831ebb0b57ce749ac1de53245e5d8eafc5`) | rule (k1) of M8-3; it only adds rows, and five rows (M7, M8, V3-countercontrol, Y8, Z9h) are kept by (k1) alone | support off `main` until the tool lands; both files land with it (DP-2, M8-11) before any gate run, which closes the gap |
| #1630, the focused review of r1 | the M8-3 revision and the nits r2 answers; the counts at `0e201f2d9` | provenance |
| commit counts against `53c6601a` (`git rev-list --count 53c6601a..origin/main` at `69d4d1c2`) | sec. 4 | support on `main` (recomputable) |

## Appendix A. The rows M8-3 keeps

**Inputs.**
- From `main` at `69d4d1c2`: EXPECTATIONS.json (blob `2f1829da32e49b5d61f48d651439f694aa0841c8`, 619 rows) and
  REQUIREMENTS.json (blob `70b759ba1239c140fafaad0400be69e8dcadb4de`), both in this directory.
- From the tool branch: the two runner files named in sec. 6.

**Recipe.** Put the four files in a directory `S` as `exp_main.json`, `req.json`, `a1_controls.py` and
`a1_conformance.py`, then run `python3 -I m83.py S`. The program is below. It writes `S/m83.json` and prints
`total 619 kept 484 dropped 135`, `unpaired []`, and the counts by reason. A row counts as run by a runner file (k1)
when its id is a string literal in that file or its `runner` field names the file. This reading can only keep more
rows. Rows that are neither kept by (k1) to (k3) nor in a drop category stay kept; there are 34 of them.

```python
import json,re,sys,collections
S=sys.argv[1]
rows=json.load(open(S+'/exp_main.json'))['rows']
ids={r['id'] for r in rows}
src=open(S+'/a1_controls.py').read()+open(S+'/a1_conformance.py').read()
lits=set(re.findall(r"['\"]([A-Za-z0-9][A-Za-z0-9_.:/\-]*)['\"]",src))
A={r['id'] for r in rows if r['id'] in lits or (r.get('runner') or '').split(':')[0] in ('a1_controls.py','a1_conformance.py')}
Bn={'TR5','RT-T','RT-T0','S11-2a','S11-2b','S11-2c','RT-L','EI14-dispatch','G-A1'}
assert Bn<=ids, Bn-ids
P={'PLAN','ITEM2','TREE','RDIR','HP','HIT','CTX','DENY','PROF','RULE','CLASS','DELEG','ANCH','PUR','RECON','OBL29','CUST','ADJ','REC','CFG','A1CFG'}
C={r['id'] for r in rows if any(q.startswith('R6.') and q.split('.')[1] in P for q in r['requirements'])}
req=json.load(open(S+'/req.json'))
C|={c for q in req if q.get('section') in P for c in (q.get('controls') or []) if c in ids}
K=(A|Bn|C)-{i for i in ids if i.startswith('MUT:')}
Aonly=A-Bn-C
def why(r):
    ru=(r.get('runner') or '')
    if r['id'].startswith('MUT:') or 'mutation' in ru: return 'mutant row'
    if ru.startswith('gate self-test'): return 'gate self-test'
    pre={q.split('.')[1] for q in r['requirements'] if q.startswith('R6.')}-{'CTRL','GATE'}
    if r['id'].startswith('Z9'): return 'purity (Z9)'
    if pre and pre<= {'SYN','CORE'}: return 'generality (%s)'%'/'.join(sorted(pre))
    return None
D={}; extra=set()
for r in rows:
    if r['id'] in K: continue
    w=why(r)
    if w: D[r['id']]=w
    else: extra.add(r['id'])
K|=extra
# closure over pairing, composition, dependency
changed=True
byid={r['id']:r for r in rows}
while changed:
    changed=False
    for i in list(K):
        r=byid[i]
        for j in (r.get('paired_with') or [])+(r.get('composed_of') or [])+([r['depends_on']] if isinstance(r.get('depends_on'),str) else (r.get('depends_on') or [])):
            if j in byid and j not in K: K.add(j); D.pop(j,None); changed=True
# composites whose components are all dropped and that are not kept
bad=[(i,j) for i in K for j in (byid[i].get('paired_with') or []) if j not in K]
print('total',len(rows),'kept',len(K),'dropped',len(D),'A',len(A),'C',len(C),'extra',len(extra),'unpaired',bad)
print(collections.Counter(D.values()))
json.dump({'kept':sorted(K),'dropped':{k:D[k] for k in sorted(D)},'extra':sorted(extra)},open(S+'/m83.json','w'),indent=0)
```

**Kept rows (484).** `A10r`, `A11r`, `A12r`, `A1r`, `A2r`, `A3r`, `A4r`, `A5r`, `A5r-generic`, `A6r`, `A7r`, `A8r`, `A9r`, `ACCEPT-SCHEMA`, `ADM-CONFIG-AT-F`, `ANCH-OVERRIDE`, `B1`, `B2`, `B3`, `B4`, `B4-MEANING`, `B5`, `B6`, `BLOCK-KEY`, `CANON-JSON`, `CHAIN-REFUSAL`, `CLASS-PIN-TARGET`, `CLASS-PROV-AMBIGUOUS`, `CLASS-RECORD-CHECKS`, `CLASS-RETAINED`, `CLASS-SCHEMA`, `CLASS-UNLEDGERED`, `CONFIG-LINT`, `CONFIG-REFS`, `CTX-INDICATOR`, `DELEG-RECDIR`, `DELEG-REGEN`, `E-A1r`, `E-A2r`, `E-A3r`, `E-A6r`, `E-A8r`, `E-L1`, `E-L3`, `E-S1r`, `E-S2r`, `EI1`, `EI10`, `EI11`, `EI12`, `EI13`, `EI14`, `EI14-dispatch`, `EI15`, `EI2`, `EI2-consumer`, `EI3`, `EI4`, `EI5`, `EI6`, `EI7`, `EI7-consumer`, `EI7-tool`, `EI8`, `EI9`, `FINDING-FORM`, `FINDING-KEYS`, `FINDING-LINEAGE`, `G-A1`, `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `GATE-13`, `GATE-14`, `GATE-15`, `GATE-16`, `GATE-18`, `GATE-19`, `GV-CACHE`, `GV-CACHE-AFTER-READ`, `GV-CACHE-IMMUTABLE`, `GV-CACHE-KEY`, `GV1`, `GV2`, `GV3`, `GV4`, `GV5`, `GV6`, `GV6-disk`, `GV7`, `GV7-consumer`, `GV7-tool`, `H1`, `H2`, `H3`, `H4`, `H5`, `H6`, `H7`, `HIT-REPLACEMENT`, `HP-MERGE-PR`, `HP-RECORDS`, `HP-SEMCLASS`, `I2-1`, `I2-2`, `I2-3`, `I2-4`, `I2-5`, `I2-6`, `I2-7`, `I2-8`, `K1`, `K1-GRAPH`, `K10`, `K2`, `K3`, `K4`, `K5`, `K6`, `K7`, `K8`, `K9`, `L1`, `L2`, `L3`, `L4`, `LC-1`, `LC-2`, `LC-3`, `LC-4`, `LC-5`, `LC-6`, `LC-7`, `LINE-PATCH-RC8`, `LN1`, `LN10`, `LN2`, `LN3`, `LN4`, `LN5`, `LN6`, `LN7`, `LN8`, `M1`, `M10`, `M11`, `M2`, `M3`, `M4`, `M5`, `M6`, `M7`, `M8`, `M9`, `MIGRATION-RECORD`, `N-W`, `N1`, `N10`, `N11`, `N12`, `N13`, `N14`, `N15`, `N16`, `N16-file`, `N17`, `N18`, `N18-record`, `N2`, `N3`, `N3-config-route`, `N4`, `N5`, `N6`, `N7`, `N8`, `N9`, `O1`, `O2`, `O3`, `O3-FILTER`, `O5`, `O6`, `O7`, `O8`, `O9`, `OUT-ADAPTERS`, `OUT-CONFINED`, `OUT-EXPLAIN`, `OUT-FROZEN`, `OUT-NOTRUNC`, `PIPE-CHAIN`, `PIPE-PRIOR`, `PIPE-REPO`, `PIPE-STAGES`, `PIPE-UNRESOLVED`, `POSTF-1`, `POSTF-2`, `POSTF-3`, `POSTF-4`, `POSTF-5`, `PROF-LANDING-LIST`, `PROF-PARAMS-LINT`, `R15`, `R16`, `R17`, `R18`, `R18-engine`, `R19`, `R19-engine`, `R3-F2`, `R4-B3`, `R4-B3-DUP`, `R5-N6`, `R6-G6`, `R8-S6`, `RB-C10`, `RB-C11`, `RB-C4`, `RB-C4b`, `RB-C4c`, `RB-C4d`, `RB-C4e`, `RB-C5`, `RB-C5b`, `RB-C7`, `RB-C7b`, `RB-C8`, `RB-P1`, `RDIR-1`, `RDIR-10`, `RDIR-11`, `RDIR-12`, `RDIR-12b`, `RDIR-13`, `RDIR-14`, `RDIR-15`, `RDIR-16`, `RDIR-17`, `RDIR-18`, `RDIR-19`, `RDIR-2`, `RDIR-20`, `RDIR-21`, `RDIR-22`, `RDIR-23`, `RDIR-24`, `RDIR-25`, `RDIR-3`, `RDIR-4`, `RDIR-5`, `RDIR-6`, `RDIR-7`, `RDIR-8`, `RDIR-9`, `REASSESS-FORM`, `REASSESS-KEYS`, `RECLINT-ORPHAN`, `RECON-BLOCK`, `RECON-CATEGORY`, `RECON-CONFLICT`, `RECON-CORPUS`, `RECON-ENUM`, `RECON-FIELDS`, `RECON-MULTI`, `RECON-OVERLAP`, `RECON-RETAINED`, `RECON-SCHEMA`, `RECON-SCI`, `RECON-TRIAL`, `RECORD-BASE`, `REP-BUILD`, `REPRO-DOUBLE`, `REPRO-PYVER`, `RESOLUTION-SCHEMA`, `REVIEW-SCHEMA`, `RL`, `RT-A`, `RT-C`, `RT-D`, `RT-D-gr58`, `RT-DR`, `RT-DR3W`, `RT-E`, `RT-H0`, `RT-I7`, `RT-I7A`, `RT-L`, `RT-L2`, `RT-M`, `RT-O9`, `RT-O9-L2`, `RT-SHIFT`, `RT-T`, `RT-T0`, `RT-X`, `RTL2-BIND`, `RULE-MINLIT`, `RULE-ZEROFP`, `S11-1`, `S11-10`, `S11-11`, `S11-12`, `S11-13`, `S11-14`, `S11-2`, `S11-2a`, `S11-2b`, `S11-2c`, `S11-3`, `S11-4`, `S11-5`, `S11-56`, `S11-57a`, `S11-57b`, `S11-57c`, `S11-57d`, `S11-58a-f`, `S11-58g`, `S11-58h`, `S11-58i`, `S11-58j`, `S11-58k`, `S11-6`, `S11-7`, `S11-8`, `S11-9`, `S1r`, `S2r`, `S4a`, `S7-schema-and-checker`, `SCAN-PARSE`, `SIDE-NONREG`, `SUPERSEDES-RESOLVE`, `SW1`, `SW2`, `TR1`, `TR13`, `TR14`, `TR14-tool`, `TR15`, `TR15-consumer`, `TR2`, `TR28`, `TR28-consumer`, `TR28-tool`, `TR29`, `TR29-tool`, `TR3`, `TR30`, `TR45`, `TR45-opB`, `TR45-opC`, `TR46`, `TR48`, `TR5`, `TR5-sim`, `TR50`, `TR50-consumer`, `TR51`, `TR51-consumer`, `TR52`, `TR52-consumer`, `TT1`, `TT10`, `TT11`, `TT12`, `TT13`, `TT14`, `TT2`, `TT3`, `TT4`, `TT5`, `TT6`, `TT7`, `TT8`, `TT9`, `U1`, `U10`, `U11`, `U12`, `U14`, `U2`, `U3`, `U4`, `U5`, `U6`, `U7`, `U8`, `U9`, `V1`, `V10`, `V11`, `V12`, `V13`, `V14`, `V15`, `V16`, `V17`, `V18`, `V19`, `V2`, `V20`, `V21`, `V22`, `V23`, `V24`, `V25`, `V26`, `V27`, `V27-glossary`, `V3`, `V3-countercontrol`, `V4`, `V5`, `V6`, `V7a`, `V7b`, `V7c`, `V9`, `VD2-HP-SEARCH`, `VD3-CONTEXT`, `VD3-COUNT`, `WB1`, `WB10`, `WB11`, `WB12`, `WB13`, `WB14`, `WB15`, `WB2`, `WB3`, `WB4`, `WB5`, `WB6`, `WB7`, `WB8`, `WB9`, `X1`, `X10`, `X11`, `X2`, `X3`, `X4`, `X5`, `X6`, `X7`, `X8`, `X9`, `Y10`, `Y2`, `Y3`, `Y4`, `Y6`, `Y7`, `Y8`, `Z1`, `Z10`, `Z11`, `Z2`, `Z3`, `Z4`, `Z5`, `Z6`, `Z6b`, `Z7`, `Z8`, `Z9-STAGED`, `Z9a`, `Z9b`, `Z9c`, `Z9d`, `Z9f`, `Z9g`, `Z9h`, `item11-T1p`, `lint-ok`, `rule-negative`.

**Dropped rows (135), recorded NOT RUN with the reason "outside the A1 path (amendment 8)":**

- mutant row (107): `MUT:c1:C01`, `MUT:c1:C02`, `MUT:c1:C03`, `MUT:c1:C04`, `MUT:c1:C05`, `MUT:c1:C06`, `MUT:c1:C07`, `MUT:c1:C08`, `MUT:c1:C09`, `MUT:c1:C10`, `MUT:c1:C11`, `MUT:c1:C12`, `MUT:c2:D01`, `MUT:c2:D02`, `MUT:c2:D03`, `MUT:cache:K01`, `MUT:cache:K02`, `MUT:cache:K03`, `MUT:cache:K04`, `MUT:cache:K05`, `MUT:cache:K06`, `MUT:cache:K07`, `MUT:cache:K08`, `MUT:o9:RDIR-m1`, `MUT:o9:RDIR-m10`, `MUT:o9:RDIR-m11`, `MUT:o9:RDIR-m12`, `MUT:o9:RDIR-m13`, `MUT:o9:RDIR-m14`, `MUT:o9:RDIR-m15`, `MUT:o9:RDIR-m16`, `MUT:o9:RDIR-m17`, `MUT:o9:RDIR-m2`, `MUT:o9:RDIR-m3`, `MUT:o9:RDIR-m4`, `MUT:o9:RDIR-m5`, `MUT:o9:RDIR-m6`, `MUT:o9:RDIR-m7`, `MUT:o9:RDIR-m8`, `MUT:o9:RDIR-m9`, `MUT:v60e:A01`, `MUT:v60e:A02`, `MUT:v60e:A03`, `MUT:v60e:A04`, `MUT:v60e:A05`, `MUT:v60e:A06`, `MUT:v60e:A07`, `MUT:v60e:A08`, `MUT:v60e:A09`, `MUT:v60e:A10`, `MUT:v60e:A11`, `MUT:v60e:A12`, `MUT:v60e:A13`, `MUT:v60e:A14`, `MUT:v60e:C01`, `MUT:v60e:C02`, `MUT:v60e:C03`, `MUT:v60e:C04`, `MUT:v60e:C05`, `MUT:v60e:C06`, `MUT:v60e:C07`, `MUT:v60e:C08`, `MUT:v60e:C09`, `MUT:v60e:C10`, `MUT:v60e:C11`, `MUT:v60e:C12`, `MUT:v60e:C13`, `MUT:v60e:C14`, `MUT:v60e:C15`, `MUT:v60e:C16`, `MUT:v60e:E01`, `MUT:v60e:E02`, `MUT:v60e:H01`, `MUT:v60e:H02`, `MUT:v60e:H03`, `MUT:v60e:I01`, `MUT:v60e:I02`, `MUT:v60e:I03`, `MUT:v60e:I04`, `MUT:v60e:I05`, `MUT:v60e:I06`, `MUT:v60e:I07`, `MUT:v60e:I08`, `MUT:v60e:I09`, `MUT:v60e:I10`, `MUT:v60e:I11`, `MUT:v60e:I12`, `MUT:v60e:I13`, `MUT:v60e:I14`, `MUT:v60e:O01`, `MUT:v60e:O02`, `MUT:v60e:P01`, `MUT:v60e:R01`, `MUT:v60e:R02`, `MUT:v60e:R03`, `MUT:v60e:U01`, `MUT:v60e:U02`, `MUT:v60e:U03`, `MUT:v60e:U04`, `MUT:v60e:U05`, `MUT:v60e:V01`, `MUT:v60e:V02`, `MUT:v60e:V03`, `MUT:v60e:V04`, `MUT:v60e:V05`, `MUT:v60e:V06`, `MUT:v60e:V07`.
- gate self-test (24): `GATE-1`, `GATE-10`, `GATE-11`, `GATE-12`, `GATE-17`, `GATE-2`, `GATE-20`, `GATE-21`, `GATE-22`, `GATE-23`, `GATE-24`, `GATE-25`, `GATE-26`, `GATE-27`, `GATE-28`, `GATE-29`, `GATE-3`, `GATE-30`, `GATE-4`, `GATE-5`, `GATE-6`, `GATE-7`, `GATE-8`, `GATE-9`.
- generality (SYN) (3): `Y1`, `Y5`, `Y9`.
- purity (Z9) (1): `Z9e`.
