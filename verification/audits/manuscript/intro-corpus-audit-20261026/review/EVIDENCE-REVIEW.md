*Recorded by the coordinator from the independent reviewer's report, verbatim. `S` in paths below is the session scratch directory, not retained.*

# Independent review: step 7 (evidence verification) of the Introduction corpus audit

Reviewed object: branch `audit/intro-corpus-20261026` (PR #942) at `290822b3717a9511c2aa97ce4421ff9c4b1b69bf`, in a detached
worktree. Audit directory `verification/audits/manuscript/intro-corpus-audit-20261026/` (written `AUD/` below). Audited
object: `papers/Introduction.md` at `4a260ca9`. The review was read-only: no commits, pushes, comments or dispatches.
I did not take part in the audit.

**Verdict: ACCEPT WITH CHANGES** (7 required, 8 optional).

The item-level work is sound. Every E2 script reproduces when re-run, both black-hole replays are byte-identical, the
Lean statements I re-checked match their coverage items, and an independent re-implementation of E4's rule agrees on all
409 rows. The problems are in the aggregation rule. Several of its clauses give rows levels stronger than their evidence
supports, including "reproduced" on open claims whose chains are paper-only. Separately, one E2 item rests on a
computation that cannot fail, and the integration controls miss one form of drift.

## What I ran (all `python3 -I -B`, from the worktree or a scratch copy)

| Check | Result |
|---|---|
| `E4_aggregate.py --check`, `render_matrix.py --check` | both pass |
| `merge_matrix.py` re-run in a scratch copy | `matrix.json` byte-identical |
| `matrix.json` 29111ca6 vs 290822b3, row by row | 409 rows, same order. No row differs apart from `evidence_level`/`evidence_basis`. Only one top-level key was added, `evidence_levels` |
| My own aggregation, `reagg.py` (imports nothing from E4) | 0 row differences from `evidence.json` and `matrix.json`; counts 67 / 153 / 187 / 2 |
| All eight `E2_*.py` scripts | all exit 0 in about 13 s. Every value matches its item (1376/12672/11776/14496, 2688, 2368, 24/60/172, 32, 36416/36368/36032; item F intervals; the Page values; c4 exact Q1 = 1 and Q2 = 2/3, Q5 interval; 1 of 15 and 2 of 16; the convention factors; the Appendix B battery and the Thm 3 census) |
| BHa `checks.py --out` at eae01647 | 32 s, `result.json` byte-identical |
| BHb `checks.py` at eae01647 | 18 s, `result.json` byte-identical, including C1 at (3,2), CC1 = 2 and CC2 = 2 |
| `E1_decls.py` on `verification/lean-mathlib` | 65 declarations, 49 with print, 30 retained; only PDivisible is off (52 → 54); forbidden-construct scan clean |
| `b5_check.py` plus my countercontrols (`b5_counter.py`) | see D |
| Lean re-read | `finite_horizon_equivalence`, `S_imp_D`, `Qfb_imp_S`, `D_imp_Qfb` and the (S)/(D)/(Q_fb) structures (Equivalence.lean:146–212, 245, 294, 422, 462); `exactAll_iff_physical_general` and `oi_alone_not_qm` (GeneralCarrier.lean:93–160); `five_way_minimality` (RankGapTheory.lean:702); `RealizesSealedOICore` (OIRealization.lean:234); `RoutedReadback` and `routed_forces_indivisible_somewhere` (PhysicalC4Discharge.lean:66–134); `tools/lean_axiom_check.py` |

The Lean statements match E1-57, E1-58, E1-60, E1-59, E1-76, E1-83 and E1-84, and the Introduction's wording at L42–44,
L112–120 and L96. E1-70's new observation is correct: `routed_forces_indivisible_somewhere` consumes only
`routedReadback_overlap` (:88–92) and `rootedMap_periodic`; the write, store and read clauses are unused. No
(module, short name) collision exists among the 65 cited declarations: the only duplicate short name,
`permMatrix_mem_unitaryGroup`, sits in two different modules. Every row that cites a declaration is listed by that
declaration's formal-coverage item (`covgap.py`: 0 gaps).

## Required changes

**R1. The CI-receipt fallback gives "reproduced" to physics rows with paper-only chains.**
Location: `evidence/scripts/E4_aggregate.py:122-125`, `EVIDENCE.md:11`.

- The rule's scope is "claims about the build, the toolchain or CI". But E3-17 and E3-18 (`part-E3.json:347, 382`) list
  black-hole physics rows, and those rows have no evidence-bearing link.
- So nine rows become *reproduced* on review-chain items:
  - I-207, I-208, I-209 and I-217, all proved-paper;
  - I-020, I-228, I-237, I-239 and I-287, all **open**.
- For example, `MATRIX.md:102` shows "The framework's Page curve is not established | open | reproduced".
- Fix: limit the fallback to rows whose claim is about build, toolchain, CI or records. A mechanical test is a chain
  whose layers are all `none`, or an explicit allow-list. These nine rows should be traced-only (no step-7 artifact)
  unless a computation link is added to the chain. I-044 is a records claim and can keep its level, with that stated.

**R2. The rule breaks weakest-link monotonicity: a partial evidence-bearing link raises a row above its load-bearing paper
step.**
Location: `E4_aggregate.py:92-95, 117-121`, `EVIDENCE.md:8, 11`.

- A row with only a paper link is traced-only. The same row with a kernel or computation link added that covers part of
  the claim becomes certificate-checked or reproduced. Adding a link can never strengthen a weakest-link verdict.
- 43 rows are above traced-only although their proof status is weaker than the evidence-bearing layer: proved-paper 35,
  open 5, conditional 2, unsupported 1. The list is in `variants.py` output. Clear cases:
  - **I-008 and I-093–I-096:** the time-t identification and the CMI vanishing criterion are paper steps, and E1-55 says
    the latter is not in the kernel. Yet the rows are certificate-checked.
  - **I-129:** E1-92 says the kernel covers only the premise.
  - **I-216 and I-218:** universal claims (C1, C2) rated "reproduced" on a finite enumeration, while E2-04 and E2-05 say
    universality rests on the written proof. This is the "finite test → universal claim" pattern of the Code Review
    Rules.
  - **I-146 and I-289:** open claims rated certificate-checked.
- Fix: when a row's proof status is proved-paper, conditional, open, calibration or unsupported, and its chain has a
  load-bearing paper, literature or none link, cap it with a basis such as "paper step outside step 7". Alternatively,
  give it a qualified level such as "certificate-checked (kernel part only)" and count those rows separately. Rows whose
  computation covers the whole stated value keep their level, after per-row review: I-372, I-377 and I-358, where the
  paper link is the citation.

**R3. Partial coverage items must carry a per-row outcome.**
Location: `EVIDENCE.md:95` ("The level stands"), `E4_aggregate.py:105-110`.

- Three items say a row is *not* covered:
  - E1-99 (`part-E1.json:2353`): `responseRealization` "does not cover I-071";
  - E1-92 (`:2228`): `isDiag_Phi` covers I-129's premise only;
  - E1-98 (`:2334`): `rootedMap_periodic` does not cover I-088.
- Yet I-071 and I-129 are certificate-checked. I-088 is traced-only only by accident, through an unrelated exact-algebra
  gap.
- Fix: give formal-coverage items a per-claim result (covered / partial / not covered). A link whose item does not cover
  the row takes traced-only, or the link is removed from that row's chain.

**R4. E2-07's independent sweep is vacuous, and E2 contradicts E3 on the BHb replay.**
Location: `evidence/scripts/E2_bh02.py:28-50`, `part-E2.json:125`, `part-E2.md:48, 76`.

- `c1_sweep` stores the state as a single-entry dict and applies `img` to its keys. A permutation of keys keeps one key,
  so `len(nz) != 1` and `len(state) != 1` can never be true, and the unpack line would raise before either could fire.
  The sweep cannot detect a rank above 1. Under the Code Review Rules a vacuous control cannot carry a verdict.
- E2-07 and part-E2.md say that BHb `checks.py` was not replayed, that (3,2) and CC1/CC2 were not re-run, and that a CI
  run is needed for them. E3-18 replayed `checks.py` byte-for-byte, and I did too: it runs in 18 s, includes the (3,2)
  sweep, and gives CC1 = 2 and CC2 = 2.
- Fix:
  - base E2-07 on the `checks.py` replay and its countercontrols;
  - either drop the independent-sweep claim, or add a control that can fail (for example a Hadamard or CNOT·rotation
    state must give rank 2);
  - correct the CI proposal at `part-E2.md:76`: only the `-O` replay and `mutants.py` remain.

  This affects I-225, I-227, I-265 and I-286.

**R5. E2-10 and E2-11 are scoped inconsistently, and the failed rows' basis does not scope the failure.**
Location: `part-E2.json:182, 205`, `E4_aggregate.py:117-118`.

- L30 defines an exact probe as "an exhaustive computation in exact rational arithmetic". E2-10 fails L84's tag, partly
  because its instances are "none exhaustive". E2-11 records that the L56 probes also fail L30's definition (they are not
  exhaustive), yet it is graded *partial*, because they meet R-03's *proposed* narrowing.
- Judged against the Introduction as written, the L56 tag fails too. E2-11's tag check should therefore be *fail*, with
  "meets R-03's narrowed definition" recorded. Otherwise E2-10 has to be re-scoped to the floating-point ground alone.
- The basis of each failed row must also say what failed. For I-103 the evidence tag "with exact probes" fails; the bound
  (paper proof plus Pinsker) and its instance values (E2-09, reproduced) stand. The current basis, "an item listing the
  row failed: E2-10", reads as a failure of the bound.
- E2-10's own finding is correct: `c4_backflow_probes.py:23` accumulates `float(p)*log2(float(...))`, and :52, :63 and
  :97 decide with tolerances.

**R6. Theorem 1 (I-063) ends step 7 at traced-only because of a mislabelled chain link.**
Location: `EVIDENCE.md:86-91`, `MATRIX.md:175`.

- I-063's chain carries a `kernel`-layer link to `verification/coverage/LEDGER.json`, which no item names. The row is
  therefore traced-only, while E1-06 and E1-57 checked `finite_horizon_equivalence` against exactly this statement, and
  I-002 and I-063.a–c are certificate-checked.
- EVIDENCE.md records seven such relabellings "and not applied": I-042, I-052, I-063, I-258, I-281 and I-282 (I-052
  twice).
- The matrix is the audit's own artifact, so the corrections should be applied (through `resolutions.json` and
  `merge_matrix.py`) and the aggregation re-run. A headline theorem should not leave step 7 under a known-wrong label.
  Apply R2 to whatever results.

**R7. Nothing checks that `matrix.json`'s levels equal `evidence.json`'s.**
Location: `render_matrix.py:127-129`, `E4_aggregate.py:254-258`.

- The new counts control compares the merge's summary with the same rows, so it only detects an edit made without
  updating the summary.
- I changed I-002's `evidence_level` in a scratch copy, updated `evidence_levels` and re-rendered. Both `--check` modes
  then passed while the row disagreed with `evidence.json`. That is the §A.25 drift pattern.
- Fix: E4 `--check`, or render `--check`, should compare every row's `evidence_level` and `evidence_basis` with
  `evidence.json[claims][id]`, and fail on any difference.

## Optional changes

- **O1.** Computation links are matched per row, not per link (`E4_aggregate.py:111-114`). Example: I-045's BH-02
  numerical link inherits *reproduced* from E2-01, a BHa item. The level happens to be supported, by E3-18's
  byte-identical BHb replay, but the mechanism would also accept a wrong match. Match on item sources against the link
  source path.
- **O2.** Some listing gaps leave rows weaker than their evidence:
  - E2-17 checks L140's "some 120 orders" but does not list I-172;
  - E2-12 and `E2_appendixB.py` compute what I-368, I-370 and I-379 state (the peek variants, the instrument
    decomposition) but do not list them;
  - E2-13 refutes I-123 and I-124, which stay traced-only.
- **O3.** `E4_aggregate.py:99, 107, 113` drop levels outside RANK. A *fail* item that matches a link but does not list
  the row therefore yields traced-only instead of failed. Treat a matched fail as failing the link.
- **O4.** EVIDENCE.md "Limits that apply across rows" (`:132`) should also state:
  - E3-11's finding that 9 of the 14 Appendix A modules have no observed fresh elaboration at these sources;
  - that for the 21 printed declarations outside the retained result, "exactly the three axioms" is read from log text.
    The structured certificate there is the Release gate step's conclusion, which under `lean_axiom_check`'s contract
    establishes only ⊆ allow-list and a report for every printed short name.

  E1 says this honestly (`part-E1.md`, "Per-declaration axiom reports"). E3-14 (`part-E3.json:278`) states the log-text
  fact at certificate-checked and should be reworded the same way. In my judgement, using digest-matched logs as
  provenance and diagnostics is appropriate for an audit under §A.44 and §A.42 item 2, provided no level rests on the
  log text alone.
- **O5.** State in the rule that the level grades the evidence of the chain, not the claim. For refuted rows it is the
  counter-evidence: I-225, unsupported/OVERCLAIM, shows *reproduced*.
- **O6.** E2-19 is a git-diff and path check, typed `exhaustive-computation` (`part-E2.json:395`). I-309's chain layer
  has the same mislabel. Retype both as `ci-receipt`; the level is unaffected.
- **O7.** `b5_check.py` has no in-file countercontrols. Add those of `b5_counter.py`. `sp.nsimplify` is unneeded on exact
  expressions.
- **O8.** `merge_matrix.py` reads `evidence.json` if one is present, so the order is merge → E4 → merge. Document it,
  or have E4's `--check` cover it (see R7).

## Answers to the questions

**A. Evidence items.**

- **"Certificate-checked" on cached builds (E1-122, E3-11).** Justified under PLAN's definition. The check is against a
  retained expected result whose log digests match, and against the gate's structured step conclusions. Lake replays a
  module only when its trace hashes match, so the replayed reports belong to these sources. The level must carry the
  limit, and it does at item level and in EVIDENCE.md, but not at row level (O4). No item labels "reproduced" what it
  only compared: E3-06, E3-16, E3-17 and E3-18 regenerate what they state. Nothing traced-only is labelled
  certificate-checked; E1-55 is conservatively traced-only.
- **The exception is E2-07.** Its "reproduced" rests on a computation that cannot fail (R4).
- **E2-10.** Correct as a failure of the evidence tag. It needs a scoped row basis, and E2-11 needs to be made
  consistent with it (R5).
- **Coverage gaps beyond EVIDENCE.md's list:**
  - the listing gaps in O2;
  - the concept DOI and release archive cited at L197–200 (E3-16 limits; "Not checked" in `part-E3.md`);
  - otherwise none found.

  EVIDENCE.md's 28 traced-only evidence-bearing rows are listed correctly.

**B. The aggregation rule.**

- Matching kernel links by (module, short name) is safe in this corpus. Taking the weaker of certificate and coverage is
  right.
- Matching computation links at claim level is too coarse (O1).
- The "no evidence-bearing link → traced-only" clause is fine on its own, but together with the kernel rule it breaks
  monotonicity (R2).
- The CI-receipt clause is applied outside its stated scope (R1).
- Context items not setting levels is right.
- "Partial does not lower" is wrong where the partial item excludes the row (R3).
- The level is weaker than the evidence in R6 and O2.

**C. Integration.**

- Rows are unchanged apart from the two evidence fields, `MATRIX.md` is the rendering, and both `--check` modes pass.
- The counts control is real but narrow (R7).

**D. `b5_check.py`.** Both fixes are correct and non-vacuous.

- **B.2:** I(X0;X2|X1) = 1 bit is now computed. The function returns 0 for an independent X2 and for X2 = X1, and
  1 − h(1/4) = 0.18872 for a noisy copy.
- **Three-hidden variant:** `cond_general_a` is −a/(a−2) = a/(2−a). The test returns False against a/(1+a) and against
  1/3, and the expression evaluates to 1/3, 1 and 0 at a = 1/2, 1 and 0.

**E. What step 7 can claim, and what remains.**

- **Done:** every one of the 409 rows has an evidence level, and the 178 items are individually sound apart from E2-07.
  The E2 reproductions and both black-hole replays hold on re-run.
- **Before "done" under PLAN's criteria:** R1–R7, including re-aggregation and a re-check by a reviewer.
- **Remains, needing owner authorization:**
  - a fresh-build CI reproduction of `introduction_repro` at `17b830bc`;
  - the BHa and BHb `mutants.py` replays, and the BHb `-O` replay;
  - optionally, the foundations probes added to CI.
- **Remains, not needing CI:** the extended expected result for E3-14's modules and the OD-15 additions can be
  re-derived locally from the digest-checked log of job 121598983127. This is time-sensitive, because the log expires
  under the host's retention, and landing it in `papers/introduction_repro/` is a §A.42 change on #918.
- **Also unchecked:** the concept DOI and the release archive.

## Reviewer files

All in `S/audit-review-e/`:

- `reagg.py` and `reagg.out`: the independent aggregation and its diagnostics;
- `variants.py`: the R1 and R2 counts;
- `covgap.py`: the per-row formal-coverage check;
- `b5_counter.py`: the b5 countercontrols;
- `e2out/`: the E2 outputs;
- `bh01/` and `bh02/`: the black-hole replays.
