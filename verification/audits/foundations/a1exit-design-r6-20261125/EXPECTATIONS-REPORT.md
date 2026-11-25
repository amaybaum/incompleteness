# r6 expectation file: report (draft for review, not adopted)

Status: drafting output under the owner's approval of RD-1 to RD-35 with Q6-Q10 (amaybaum, 2026-11-25, coordinating session). It adopts nothing, changes no tool, control or workflow, and starts no run. Every item in section 8 is still an open owner decision; this file settles none of them.
Goal link (sec. A.47): A1-EXIT (#1169). It decides how each control's expected result is stated and gated. It decides no scientific question.

## 1. Basis
- `EXPECTATIONS-draft.json` (00b97b2b...873af): 399 rows and 9 retired entries.
- `EXPECTATION-SOURCES.json`: 382 ids.
- `GATE-draft.md` (f9083a8f...7fe65).
- `RESIDUAL.md` (db111ea0...e1fd) and `DECISIONS.md`.
- Tool commit a3799244 (read only).
- CI run 45569710442: `9-mutation-results.json` and `ci-results.json`.
- Design sources cited as D: (v6.0e), v1:, v2: and r5:.

## 2. Counts (mechanical)
**Rows: 526. Retired entries: 10.**

| Kind | Rows |
|---|---|
| Control rows | 388 |
| Composite rows (EI7, GV7, S11-2, TR28, TR45) | 5 |
| Mutation rows (`MUT:<set>:<id>`) | 107 |
| Gate self-test rows (GATE-1 to GATE-26) | 26 |

**Draft to final:** all 399 draft rows are kept and 127 are added:
- 107 MUT rows;
- GATE-21 to GATE-26;
- U14, restated (it was a retired entry in the draft);
- 13 control rows: EI14-dispatch, EI7-consumer, RECLINT-ORPHAN, REPRO-DOUBLE, RT-O9-L2, TR15-consumer, TR28, TR45, TR45-opC, TR50-consumer, TR51-consumer, TR52-consumer, Z9-STAGED.

**Null expectations: 0.** No open decision is held as a null inside the file. Each affected row carries a flag naming its section 8 item.

**`operations` is on all 526 rows (RD-32).**
- 241 come from the draft (controls.json).
- 285 were assigned by reading the runner call at the tool commit, by family, with 54 explicit assignments.
- 190 rows have `[]`: the control invokes no tool operation (mutation harness, gate, consumer predicate, pre-run step, or lint library).

**Restored (Q7): 223 rows carry `restored`, all of them sec. 10 controls.** That means D:2080-2328, plus U1-U12, U14 and M1-M11, which v1 8.2/S8 and D:2096 say stand in both directions.
- 46 name a counterpart within the row: a positive or clean case, a runner baseline read in code, or a composite.
- **177 carry "VD-RESTORE: no restored case executed"** (section 4).

**NOT RUN rows: 7.** Each has a reason, a release condition and a release check.
- RT-T: every reviewed sec. 8.2 record present at F and verifying.
- TR5: F on main with Record pins, and the pinned workflow dispatched there.
- G-A1: TR5 released, with X and C fetchable.
- RT-L2: a reviewed reconciliation record bound to exact H, M and C.
- RT-O9-L2: as RT-L2 (`depends_on` RT-L2).
- TR45-opC: delegated evidence recorded by native runs at X and C.
- EI14-dispatch: the pinned workflow dispatched on a branch with the CX-3 tree after F.

No row admits SKIP (RD-7). RT-O9 is no longer NOT RUN (Q6).

**Mutation rows by state (RD-1, Q8): KILLED 99, SURVIVED 7, NOT APPLIED 1, total 107.** This equals the CI run's counts.
- **KILLED rows:** `status_allowed ["KILLED"]`, the invariant `killed_by_nonempty`, and the killers kept in `reference`. Killer ids are mapped to r6 ids: O9-n becomes RDIR-n, R1-R14 become TT1-TT14.
- **Survivors:** c2:D02, cache:K08, v60e:C08, v60e:H03, v60e:I06, v60e:P01 and v60e:V05 have `status_allowed ["SURVIVED"]` and a LIMITATION flag with its reason.
- **Not applied:** v60e:U01 has `["NOT APPLIED"]` and a LIMITATION flag.
- **Gate behaviour:**
  - any other survivor or unapplied mutant fails as status-not-allowed;
  - a missing mutant fails as missing-id;
  - GATE-21, -22 and -24 test these; GATE-23 is the positive case.
- **o9 mutants:** they become `MUT:o9:RDIR-m1` to `-m17`, with `migrated_from` `o9:O9-mN`.

## 3. Reconciliation
**Source ids: all 382 are covered exactly once.**
- 340 as row ids.
- 40 as `migrated_from` (O9-* to RDIR-*, R1-R14 to TT*).
- 2 as retired entries (U13, U15).
- No duplicate ids.

**The draft's 34 nulls:**
- They are the 32 runner-only rows that RD-24 enumerates. Its heading says 31, but the list names 32.
- Plus G-A1 and TT12 from RD-25.
- RD-25's other items were not null rows:
  - RT-L had a null `outcome` inside its first case; this is the "+1" in "32+3";
  - Z9-STAGED was not yet a row;
  - TT7 already had its class.
- All are now filled. RT-L's first case is REVIEW_REQUIRED, exit 10.

**Gate controls:** GATE-1 to GATE-20 match GATE-draft 16.7 id for id. GATE-21 to GATE-26 are new.

**Ids the runners recorded in CI (steps 1-8):**
- **Recorded but not a row:** U13 and U15 (retired) and the purity job's `outcome`, which becomes Z9-STAGED. Each would be unexpected-id until the tool revision renames or drops it.
- **Rows with no record today:**
  - S11-7 (VD-6);
  - Z9-STAGED (renamed);
  - 10 rows still to implement: EI14-dispatch, EI7-consumer, RECLINT-ORPHAN, REPRO-DOUBLE, RT-O9-L2, TR15-consumer, TR45-opC, TR50-consumer, TR51-consumer, TR52-consumer.

  These are named blockers (Q10).
- **Exception and diagnostic ids are not rows:**
  - exception ids: H, U, X-group-error, GV-CACHE-group, TR-group, acceptance-group;
  - diagnostic keys: `_S7_bad`, `_Z10_detail`.

  Exception ids appear as killers of 8 mutants (cache:K01, K02, K05, K06; v60e:A05, I05, I13, V06). Each of those also has a named killer. Mechanical fix for the tool revision: record a group error as a failed record for each member id, and stop recording diagnostic keys as records.

## 4. VD-RESTORE: 177 sec. 10 rows with no restored case executed
Each row states its `restored` expectation: RESULT_EQUAL_CLEAN against a named baseline.

A row counts as executed only if one of these holds:
- the row has a positive or clean case beside an adversarial one;
- I read the runner code and it runs the unmutated counterpart: M1, M3, N1, N2, SW1, SW2, G6, G7, EI6, EI7-tool, EI14, GV1, GV2, GV3, GV5.

Two special cases:
- A11r keeps its draft `restored` but is flagged, because that half is unreachable in the runner (VD-7).
- A5r is flagged because its runner's `unmutated_rule_lints_clean` check is not the restored tree's outcome.

**(a) No-mutation or positive controls, where the restored case is the control run itself (43; R-2):** B1 B2 B3 B4 B6 EI8 K10 K2 K9 L1 L2 N-W O9 R17 RT-A RT-C RT-D RT-D-gr58 RT-DR RT-DR3W RT-E RT-H0 RT-I7 RT-I7A RT-T RT-T0 S11-56 S11-57d TR48 TR5 TR5-sim U1 U10 U11 U2 U3 U6 V27 V27-glossary V4 WB1 WB13 WB8.

**(b) Adversarial controls with no restored case (134):** A10r A11r A1r A2r A3r A4r A5r A6r A7r A8r A9r B5 EI10 EI11 EI12 EI13 EI9 G1 G2 G3 G8 GV4 GV6 GV6-disk GV7-consumer GV7-tool H1-H7 K1 K5 K6 K7 K8 L3 L4 M10 M11 M2 M4 M5 M6 M7 M8 M9 O1 O2 O3 O5 O6 O7 O8 R16 S11-57a S11-57b S11-57c S11-58a-f S11-58g S11-58h S11-58i S11-58j S11-58k S1r S2r TR1 TR13 TR14-tool TR15 TR2 TR28-tool TR29-tool TR3 TR46 TR50 TR51 TR52 U12 U4 U5 U7 U8 U9 V1 V2 V3 V5 V6 V7a V7b V7c V9-V24 V26 WB2-WB7 WB9-WB12 WB14 WB15 X1-X9 X11 EI14-dispatch.

Some (b) rows have a positive counterpart in another row: TR48 for the TR rows, EI8 for EI9-EI15, and N-W and RT-D for the V rows. Under Q7 a counterpart in another row is not the row's own restored case unless the owner decides otherwise (R-2).

## 5. Q9: 33 runner-only predicates checked against their requirements
None is weakened to fit the code.

**Predicate matches the requirement (20):** lint-ok, E-L1, E-L3, ACCEPT-SCHEMA, ADM-CONFIG-AT-F, CHAIN-REFUSAL, CONFIG-LINT, B4-MEANING, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH, O3-FILTER, R3-F2, R4-B3, R5-N6, R6-G6, RL, Z6b.

**Weaker or mismatched, flagged "Q9: ..." (13):**

| Rows | What the predicate misses |
|---|---|
| E-A1r, E-A2r, E-A3r, E-A6r, E-A8r | It checks a truthy lint or widening result; sec. 10.4 (D:2238-2240) requires an emitted FAIL record-invalid. |
| E-S1r, E-S2r, rule-negative | Class inclusion only; no outcome asserted. |
| A5r-generic | No rule named (D:2083-2084 requires it). |
| R4-B3-DUP | The lint cases assert findings, not an emitted FAIL; the op-C case does carry it. |
| S7-schema-and-checker | Passes vacuously when no result exists; the row now requires at least one. |
| V3-countercontrol | Does not assert the count of 95 itself. |
| U14 | The positive case asserts no item, but not the status `adjudicated`. |

The E-* rows stay as engine analogues, each flagged "preserved-at" its v6.0e control. None is identical to its v6.0e control, so none is merged.

## 6. Resolutions applied

**RD-1, Q8: mutation.** The 107 MUT rows described in section 2.

**RD-2: double run.** REPRO-DOUBLE (D:3112-3113) with procedure `double-run`, and GATE-25.

**RD-3: reference figures promoted to `expect`.**
- RT-H0: 113/7/7 and the 7 structure sites.
- RT-A: 0 errors, 697 anchors.
- RT-E: 697.
- RT-DR at H: DR-1 61 (a/b/c 6/2/55), DR-3 0, DR-4 28, DR-5 1, 86 lines. New case at E: 95.
- RT-T0: 197, 4, 383, 168, 215, 9, 22, 31 splices, 18 line-attributed, overlap at D029 only.
- RT-I7 at H: 11/1/2, A1 179, 14 items; plus the 7 named T1' lines.
- RT-I7A: 86/123/209, 93/216, 95 retired; T1' 12.
- RT-C: 399/23/21 and the LEDGER.json exception.
- No `reference` field remains on any control row.
- Figures the runner does not assert today are flagged as verification defects: RT-T0's 383, 18 and D029 overlap; RT-I7's H split; RT-C's 399/23/21.

**RD-23: inputs off main.** These rows carry "inputs off main: acceptance reference only for runs with those pinned inputs": RT-T0, RT-I7 (T1' case), RT-I7A, RT-C, RT-D, RT-DR (T1' case), RT-DR3W, item11-T1p, N10, N11.

**RD-4: halves and `composed_of`.**
- New composites: TR28 (TR28-tool, TR28-consumer) and TR45 (TR45-opB, TR45-opC).
- `composed_of` added to parents that also have their own record: TR29, EI2, GV6, RT-D, V27, TR14, EI14, TR15, TR50, TR51, TR52.

**RD-5: identifiers.** The o9 mutants become RDIR-mN. RT-O9 and R15-R19 keep their ids. A retired entry records v1's RT-T as succeeded by RT-T0.

**RD-6, Q6: RT-O9 split.**
- RT-O9 is gated, with PASS as its only allowed status. It checks: entry-set equality, directory state active, no unequal path, directory admitted, no side-change-unclassified, and no stop.
- RT-O9-L2 holds "no base-drift" and "RT-L2 PASS". It has `depends_on` RT-L2 and is NOT RUN under RT-L2's release condition (see R-6).

**RD-9: U14, orphan records, stale-adjudication.**
- U14 is restated:
  - positive case: a matching provenance adjudication leaves the site `adjudicated`;
  - negative case: the old U15 wrong-region-hash case, FAIL.
- RECLINT-ORPHAN is added: an orphan record entry gives FAIL record-invalid.
- A retired entry records the class name `stale-adjudication`.
- U15 is now preserved-at U14, H1, H2, H6 and RECLINT-ORPHAN.
- U13 stays retired.

**RD-25: other null expectations.**
- G-A1 is stated from sec. 7.2 (D:1859-1916) and stays NOT RUN.
- TT12 gets landing-extra-change, which agrees with `execution.py:414`.
- Z9-STAGED gets runner `selftest.py:30`.
- RT-L gets REVIEW_REQUIRED, exit 10.

**RD-26: unexecuted halves.**
- TR45-opC is a NOT RUN row.
- EI14 is split: the simulated pre-run case stays in EI14, and the real dispatch becomes EI14-dispatch (NOT RUN).
- EI7-consumer and the TR15/TR50/TR51/TR52 consumer rows are added with runner null, flagged to implement.

**RD-31: Z9h.** Its text is now "'guard-pin' planted in an engine module, with the adapter companions in the value set: lint FAIL (the value occurs in edits.json)".

**RD-35: findings.**
- A2r states the mutated literal `(A1)`.
- A5r requires the deny item to name DR-3 on ch19:212.
- K4 keeps both halves and is flagged.
- RT-D keeps its 45, flagged against controls.json, which omits it.

**RD-14, Q10: V4 reversal.** V4, V27, V27-glossary and V15 are flagged: the reversal is decided at r6 adoption, not by this draft.

**RD-13: retired v6.0e ids.** The grouped retired entry now points to r6 sec. 33. The per-id entries are dependency D-1.

**Text rule.** Where a quoted mutant rule contains "@", it is written as "(at)".

## 7. Mechanical amendments GATE-draft.md needs
- **16.2 row fields:**
  - add `case` (used by the GATE rows);
  - define `composed_of` on a row with its own runner: the row holds only if its own record and every component hold (GATE-26).
- **16.2 `expect` fields:** add `gate_findings_include` and `gate_findings_exact`.
- **16.2 outcomes:** add GATE_FAIL, GATE_HOLDS, GATE_ERROR, KILLED, SURVIVED, NOT_APPLIED.
- **Invariant annex:** it must list all 136 invariant keys the file uses.
- **16.3:**
  - record statuses are PASS, FAIL and NOT RUN (SKIP removed);
  - a mutation record schema is needed.
- **16.4:** add the library entry `double-run`.
- **16.5:** report an allowed SURVIVED or NOT APPLIED as `limitation-reported`, which does not fail the gate.
- **16.7:** add GATE-21 to GATE-26.
- **16.9:** the NOT RUN list becomes RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC, EI14-dispatch.
- **Requirement list:** add R6.REPRO.mutation and R6.REPRO.double-run.

## 8. Residual owner decisions

**R-1. Scope of the deferred V4 reversal.**
- V4, V27 (with V27-glossary) and V15 all rest on V5-D1 (DR-2 and DR-1d dropped). That decision is recorded only in paraphrase.
- What adopting it permits:
  - V4 ("sixth structural property, finiteness of the bijection") and V27 ("... is finiteness of the substratum") pass with no hit;
  - V15 ("sixth axiom, finiteness") gets only REVIEW, through resid.
- So restating A1 in those forms is never a FAIL.

Options:
- (a) The deferral covers V4 only.
- (b) It covers all four, each decided at r6 adoption. Recommended, because they share one basis.
- (c) Reject now: restore DR-2 and DR-1d as plan rule records (OD-8), with expected result FAIL deny-match.

**R-2. Restored case of a control with no mutation** (the 43 rows in section 4(a)).

Options:
- (a) Literal reading: each row needs its own executed counterpart (as drafted).
- (b) For a control with no mutation, its own run is the restored outcome, recorded per row as `baseline: identity`.
- (c) As (b), and also accept a counterpart in another row (TR48, EI8, N-W, RT-D) as the baseline for an adversarial row.

**R-3. Class for U14's wrong-region-hash case.**
- RD-9 says it FAILs "through unauthorized-change".
- The runner asserts provenance-mismatch, which is v6.0e sec. 9's class.
- v1 expected unauthorized-change plus stale-adjudication.

Options:
- (a) provenance-mismatch (as drafted).
- (b) Both provenance-mismatch and unauthorized-change; this needs a code check.
- (c) unauthorized-change only.

**R-4. Does sec. 10's both-directions rule reach controls defined elsewhere?** Those controls are:
- sec. 13.2: TT, R15-R19, N3-N18, RT-X, RT-L, RT-L2 (v2 called the R controls "added to the test matrix");
- sec. 16.5: Y, Z, Z9;
- sec. 11: S11;
- r5: RDIR, I2, RT-O9.

Options:
- (a) sec. 10 rows only (as drafted).
- (b) Every control in the catalogue.
- (c) (a) plus sec. 13.2.

**R-5. Where the mutation harness lives.**
- The mutants and the harness are in `ledger-coverage-suite-ci.yml` at CI commit 233412cc, a child of the tool commit, not in the tool commit itself.
- Under sec. A.42 item 1, gated MUT rows need them on a commit reachable from main, with a recipe.

Options:
- (a) Land them, pinned, with the tool revision. Recommended.
- (b) Keep them CI-only. The MUT rows would then rest on provenance, against RD-1.

This is also an outstanding evidence obligation (Q10).

**R-6. RT-O9's "no base-drift" clause.**
- Q6 names only "RT-L2 still PASS" as dependent.
- But in the RT-O9 run, "no base-drift" holds only because of the drafted, unreviewed AGENTS.md reconciliation record. So I moved that clause to RT-O9-L2 as well.

Options:
- (a) Keep the clause in RT-O9-L2 (as drafted).
- (b) Keep it in RT-O9. RT-O9 would then pass only on an unreviewed record, which OD-18 rejects for RT-L2.

**R-7. Survivors with no recorded equivalence argument.**
- D02, H03 and V05 have a recorded equivalence argument.
- K08, C08, I06 and P01 do not. Each names a property no control detects:
  - K08: the path map omitting submodules;
  - C08: TR52 at the consumer;
  - I06: TR51's regular-files-only check;
  - P01: the Z9 allowlist exempting only its listed values.

Options:
- (a) Limitation only (as drafted).
- (b) Limitation plus a verification defect each, with a distinguishing control. TR52-consumer would close C08.

**D-1 (input dependency, not a decision).** RD-13(a) needs per-id dispositions for O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47, TR49, TR53-TR70, LN9, LN11 and LN12. They come from INVENTORY-v6.0e table 2, which is on the records branch and was not among my inputs. Until those per-id entries are written, the grouped retired entry stands, pointing to them.
