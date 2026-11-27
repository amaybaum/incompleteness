# r6 amendment 8: minimum-sufficient path to A1 retirement (paper draft r1)

**Status.** Paper draft r1. It goes to one focused independent review and then to the owner for adoption at DP-1 (sec. 5).
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
  - custody 120/120;
  - adjudication 38/38;
  - OBL-29 144/144;
  - staging 82/82
  (#1577 comment 7211786545);
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
- *Change.* A row stays in the gate when either:
  - (a) it is named by a requirement of sec. 18 (the plan's checks), R6.RECON, R6.OBL29, R6.CUST, R6.ADJ, R6.REC,
    R6.CFG or R6.A1CFG; or
  - (b) it already holds.
  Every other row is recorded NOT RUN with the reason "outside the A1 path (amendment 8)". A testable requirement with
  no control and outside (a) is verified by review. TR28 is covered by its components. The retained list is generated
  from EXPECTATIONS.json and REQUIREMENTS.json before any gate run and is checked in the focused review.
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
- *Clauses.* OBL-28 C-7, C-11, C-12, C-14, C-15, C-22, C-23, C-24, RE-13, RE-27 and RE-29, and C-5 for rows outside
  M8-3 (a).
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
| commit counts against `53c6601a` (`git rev-list --count 53c6601a..origin/main` at `69d4d1c2`) | sec. 4 | support on `main` (recomputable) |
