## Delta review of A1 design r6, round 3 (commit c33d5b71a3e4e15028d19ff153afcee8f5aa90a3, parent 400e4b4fe5f3474b96ee4faa3c437e76e09db782)

**Verdict: ACCEPT-WITH-NITS for round 3.** Decisions 1 to 4 are quoted exactly as written and applied as the owner decided them. R1–R6 and N1–N6 are addressed, the S1-D3 marking rules were applied consistently, and the generator reproduces every output byte for byte. Nothing in round 3 weakens a safeguard. Round 3 does not need to be revised. But five items have to be settled at or before the adoption decision (listed below). Most are small. One of them (F1) goes beyond the writer's own list and touches what blocks retirement.

### How I checked
- **Scope.** I read the full diff 400e4b4f..c33d5b71. It touches only the r6 directory (12 files). I also read CORRECTION-REPORT-round3.md and the previous review.
- **Owner and review comments.** I fetched #1169 comments 7166666428 and 7166844576 with GET requests only.
  - `generator-round3/comments-round3.json` matches the live comments: body, `created_at` and login.
  - `generator-round3/review-r6-round2.md` has sha256 f09d7cb0…, which equals the digest stated in 7166666428. It also equals the text between that comment's two marker lines, with one trailing newline.
  - REVIEW-r6-round2.md contains that text verbatim.
- **Generator: I re-ran it, and it reproduces.**
  - In my scratch directory I rebuilt its input layout. `out-final3/` holds the nine round-2 outputs at 400e4b4f, plus `build/text2.py` and `build/correct2.py` taken from `generator-round2/`. Alongside it: `gh7/sel.json` (= `generator-round2/comments-1169.json`), `MAPPING.json`, `INVENTORY.json`, and `out-final4/build/` holding `correct3.py` and `inputs/`.
  - All 16 input hashes match sec. 1 of the report.
  - `python3 -I -B correct3.py` exits 0 and its self-rerun passes.
  - All 11 outputs are byte-identical to the committed files. This includes CORRECTION-REPORT-round3.md (sha256 df7aab49…).
- **Decision 1.**
  - Parsed out of the review's text, the 22 and 19 lists match exactly the 41 blocks marked "Confirmed by owner decision 1". REQUIREMENTS.json `owner_decision` agrees.
  - R6.STAT.4 and R6.EVID.5 carry the scope-statement text.
  - R6.OUT.15 carries the deferral, and so does the replay mode of R6.REC.24.
- **Decision 2.** FRESH-AUTHORIZATION.md sec. 2 records six (b), two (c) and four (d). R6.A1CFG.7 is added as (c).
- **Decision 3.**
  - V4, V15, V27 and V27-glossary: each `expect` equals the earlier "reversal adopted" candidate byte for byte.
  - `candidate_expectations` is removed, and the flags are rewritten.
  - The other 554 rows are identical, and so is `retired`. The only other change is `record_id`, r6-final3-1 → r6-final4-1.
- **Sec. 0.1.** With the "> " prefixes stripped, the quoted block equals decisions 1 to 4 of 7166844576 exactly. The four quoted decision-5 sentences also occur verbatim.
- **Counts.** 428 requirements (R6.TREE.19 added), 558 rows, 50 pending (all keyed S1-D3), OPEN markers only on R6.STAT.10 and R6.TREE.12.
- **R3.** All 46 entries say "If not confirmed: … stays pending". Withdrawal appears only as an explicit owner choice, in FRESH-AUTHORIZATION.md, PARAPHRASED-DECISIONS.md and DESIGN sec. 0.1.

### S1-D3 identification (54 found, 50 marked)
- **The rules were applied consistently.** I applied rules A and B myself to REQUIREMENTS.json, using the item list and control list in FRESH-AUTHORIZATION.md sec. 3, which I checked against E-034's B1–B6 rows. I got exactly 22 under rule A and 30 under rule B only. Rule C adds REC.7 and REC.17, for 54 in total. Of these, REC.7, REC.24, CTRL.14 and CTRL.23 are confirmed by decision 1, and the other 50 are keyed and marked. No requirement is marked pending that the rules did not find.
- **Over-marking is real but harmless.** Rule B sweeps in requirements that are older than S1-D3, for example CORE.1 and CORE.2 through Z9g, and the report says so. Over-marking only adds confirmations, which is the conservative direction.
- **Possible misses (from a sample).** Rule C read only secs. 11, 13 and 16. In other sections I found:
  - **R6.OUT.5** (E-101). Its `CONFIG_UNREVIEWED` branch, "not admitted from `F`'s pin table", restates the B3 content for which R6.REC.5 *is* marked.
  - **R6.OUT.18** (E-106). The schema `/5` exists because of "the admission snapshot of sec. 6.3". That is B1/B3 content in v6.0e sec. 5, which E-034 maps to B1.
  - **Borderline: R6.DELEG.8** (E-1043, a sec. 7.2 item). It is the local-run fallback that sends G4–G8 to CI.
  - The label-driven rule A is a defensible narrowing; section-level mapping would sweep in about 45 more requirements. But under decision 5 these residues should be named. See item 4 below.

### R6.TREE.19 (LC-7 regeneration and byte comparison, decision 4 (ii))
- **Sound and fail-closed.** Only equal bytes discharge the case. A difference is FAIL. A checker that cannot run, an exit that is not zero, missing output, or a missing or unpinned input all stay REVIEW_REQUIRED. No claim, log, record or attestation supplied by the evaluated tree is an input. There is no normalization. I see no path that discharges the case falsely: equal bytes mean that `L[p]` is exactly what the program pinned at `F` produces from `L`'s tree.
- **Decidable, given the configuration at `F`.** When the contract names no program that *produces* `p`, the case falls to REVIEW_REQUIRED.
- **Smallest rigorous fix: close, with three non-blocking defects.**
  - (a) It calls the program "the checker", but it must be a generator. Most contract checkers, such as preserve_check, are verifiers. It should say that the delegation contract pinned at `F` names the generator and command for each class in the derived set, and that a class naming none leaves `p` REVIEW_REQUIRED.
  - (b) It repeats the regenerate-and-compare logic of R6.DELEG.3 but leaves out DELEG.3's isolation: no network, fixed environment, `-I -B`, permitted outputs. Its failure classes also differ for the same event. DELEG.3 makes missing output FAIL `regeneration-output-missing` and a difference FAIL `regeneration-mismatch`; TREE.19 makes missing output REVIEW_REQUIRED and a difference FAIL `delegated-evidence-invalid`. TREE.19 should either cite DELEG.3's isolation and failure handling, run at `L`, or say why it differs.
  - (c) A class whose generator is not byte-deterministic, such as a PDF build, would always FAIL. That is a false FAIL, still fail-closed. Either restrict the derived set to deterministic generators or state the consequence.
  - None of these allows a false discharge, and I accept the procedure as reviewed with these nits.
- **A window where the text contradicts the expectations.** R6.TREE.12 keeps the case REVIEW_REQUIRED "until that procedure has passed its independent review … and r6 is adopted". After that, a tool that implements TREE.19 contradicts LC-7, which expects REVIEW_REQUIRED in every case (OC-4 enforces this). TREE.12's condition should instead be "until LC-7's cases are restated by an owner-approved expectation change". TREE.19's Controls line already anticipates that change.

### Findings
- **F1 (non-blocking for round 3; must be resolved at or before adoption). The deferral of R6.OUT.15 is applied to only half of the offline replay.**
  - Location: DESIGN-r6.md R6.OUT.15 and sec. 0.1 (decision 1 bullet), OBL-17, R6.GATE.15, R6.CTRL.5, and rows TR45-opB, TR45-opC and TR45.
  - Defect: the owner deferred "R6.OUT.15 and its dependent offline replay mode", and OUT.15 itself specifies the op-C replay ("For op C, every delegated and native class is decided from the snapshot's delegated evidence"). But only REC.24's replay mode and TR45-opB were marked deferred.
  - Consequence: OBL-17 still gates *the A1 retirement execution* on "TR45-opC run and PASS". TR45-opC is the op-C offline replay, and its runner is still to be implemented. So retirement depends on a feature the owner deferred.
  - The writer's list catches TR45 and TR45-opB but not OBL-17 or TR45-opC. The previous review's dependent list, which I relied on in part, has the same gap.
  - The result fails closed: retirement is blocked rather than allowed. But the adopted text would contradict decision 1.
  - Fix: one owner-approved change that defers TR45-opC, TR45 and OBL-17 together with TR45-opB. Or an explicit owner statement that op-C replay stays required.
- **F2 (non-blocking; text fix before adoption). The flags on item11-T1p contradict decision 4 (iii).**
  - Location: EXPECTATIONS.json row item11-T1p, which is byte-identical to round 2.
  - Defect: its flags "acceptance reference only for runs with those pinned inputs (RD-23)" and "the enduring claim is a named provenance gap (OBL-23)" contradict OBL-23 as it now reads ("not an acceptance reference for the tool's landing, and no enduring claim rests on it").
  - Table 17.1's row ("candidate evidence for the landing decision only") is in mild tension with the same text.
  - Fix: replace the two flags with "candidate evidence only, not acceptance support (owner decision 4 (iii); OBL-23)". This is a change to flags only, and no expectation changes.
- **F3 (non-blocking; must precede adoption). S1-D3 possible under-marks: R6.OUT.5 and R6.OUT.18, and DELEG.8 as borderline.** See above.
- **F4 (non-blocking). R6.TREE.19 nits (a)–(c) and the LC-7 window.** See above.

### What the writer left undone, and when each must be resolved
- **TR45/TR45-opB inconsistent with the deferral: before or at adoption.** Fold it into F1, which also covers TR45-opC and OBL-17. The adopted expectation file must not require a deferred feature.
- **The item11-T1p flag: before adoption.** F2; a mechanical text change.
- **LC-7's expectation cases: can follow adoption.** LC-7 stays REVIEW_REQUIRED, which fails closed. The restatement must precede certification of the tool. I recommend the TREE.12 condition change above before adoption; it is one phrase.
- **R6.STAT.8's restatement: must precede adoption.** This is the requirement's own condition. It can go into the adoption record.
- **R6.DENY.1/2: can be settled in the adoption decision.** Round 2's settled F4 left them unmarked, and they take effect with adoption. Listing them in the adoption decision would make them explicit, but it is not required.
- **Landing scope of the directory: must precede adoption** (R6.STAT.10: the documents and their review must reach `main` first).
  - The directory has 37 files and about 4 MB, including drafts (OUTLINE.md, GATE-draft.md, EXPECTATIONS-draft.json, RESIDUAL*.md) and two generator directories.
  - Under §A.28 and §A.42 item 5, keep only what a surviving claim needs.
  - Under §A.42 item 8, trace every reference to content not on `main`. The tool commit a37992449… is not on `main`. Others are the records-branch v6.0e/v5.5.9 blobs and the T1′ objects.
  - This delta review must also land as a record.

### Items that must precede adoption
1. F1: settle the deferral for TR45-opB, TR45-opC, TR45 and OBL-17 in one owner-approved change.
2. F2: correct the item11-T1p flags.
3. The owner restates the landing-order decision in their own words, per R6.STAT.8.
4. The owner confirms the 50 S1-D3 requirements, or chooses withdrawal explicitly. The adoption decision should also say that the identification is bounded by its rules, and should either add R6.OUT.5 and R6.OUT.18 (and optionally R6.DELEG.8) or confirm them by name.
5. Landing: decide the scope, trace off-`main` references under §A.42 item 8, and get an owner-approved merge of the r6 documents, REVIEW-r6-round2.md and this review (R6.STAT.10; §A.50 item 1).

Recommended, but they can follow adoption: the TREE.12 condition change, TREE.19 nits (a)–(c), and the LC-7 restatement before tool certification.

### Nits
- **N-a.** The new flags on V4, V27, V27-glossary and V15 call the rejected candidate "reversal rejected (a plan rule record of this form under a new identifier …)". That label occurs nowhere in the round-2 files, which recorded "(a plan rule record restored for this form, sec. 12)". V4-COMPARISON.md says the label was restated, but the flag reads as if it quotes the recorded label.
- **N-b.** FRESH-AUTHORIZATION.md sec. 2: the R6.A1CFG.7 row sits in the column "Reviewer's reason (quoted)" but is a paraphrase of R6, not a quote.
- **N-c.** R6.EVID.5 still lists GATE-16 under Controls. The added sentence explains why, but decision 1 says "without redundant checks"; moving GATE-16 into the prose would be cleaner.
- **N-d.** Review-finding labels such as "(R3)", "(R4)", "(N4)" and "(N5)" now appear in the design's own text. They are harmless in a verification record but cannot be resolved without the review.

### Limitations
- I did not re-review parts of DESIGN-r6.md that round 3 left unchanged, beyond the passages the questions touch. I did not re-verify MAPPING.json, MIGRATION.json or INVENTORY.json, beyond the fact that they match their pinned hashes.
- The S1-D3 search for misses is a sample: a keyword and section-item scan with judgment calls. It does not establish completeness. The rule-A/B reproduction relies on the item and control lists in FRESH-AUTHORIZATION.md, which I checked against E-034's text in INVENTORY.json.
- I did not run the tool, any control or any real-tree measurement.
- My TREE.19 assessment is a reviewer's judgment, not a formal proof.
- I made no git or GitHub writes. My scratch reconstruction and generator run were confined to the scratch directory I was given.
- This review was run by a Claude agent launched by the coordinating session, from the same model family as the writer and the previous reviewer. It is non-author only in that it wrote none of the reviewed work.