*Recorded by the coordinator from the independent reviewer's report, verbatim. `S` in paths below is the session scratch directory, not retained.*

# Re-review: the step-7 evidence layer at 818bcd60 (the response to EVIDENCE-REVIEW.md)

Reviewed object: `audit/intro-corpus-20261026` at `818bcd60a7afb0cf859c58eaea2c03b5162d8ca7`, checked out as a
detached worktree. The previous state was `290822b3`. `AUD` below is
`verification/audits/manuscript/intro-corpus-audit-20261026/`, and `E4` is `AUD/evidence/scripts/E4_aggregate.py`.
The review was read-only: no commits, pushes, comments or dispatches. I did not take the commit message or
EVIDENCE.md on trust. Every statement below was checked against the code and the data.

## Verdict: CHANGES NEEDED

Most of the response holds up. R1, R4, R5 and R7 are resolved, and so are O1 and O3–O6.

- An independent re-implementation of the rule agrees with `evidence.json` on all 409 rows.
- The pipeline regenerates every artifact byte for byte.
- The rewritten C1 sweep can now fail.
- The drift controls catch level and basis drift.

Three new defects need fixing before step 7 can be called done:

1. **N1.** The relabels give I-052 and I-258 a higher level by moving kernel steps out of the graded set. For I-258,
   the step that drops out has no evidence item.
2. **N2.** I-227, a universal claim, is rated *reproduced* on a finite sweep. This is the R2 pattern again: it gets
   through because its paper lines are labelled `exact-algebra`.
3. **N3.** Nothing checks the chains in `matrix.json` against `chain-relabels.json` or the `part-B*.json` files. As a
   result, EVIDENCE.md can list a correction that was never applied while both `--check` modes pass.

## Status of R1–R7 and O1–O8

| ID | Status | Evidence (file:line at 818bcd60) |
|---|---|---|
| R1 | **Resolved** | E4:22-23, :152-157, :184. CI receipts set a level only when every link in the chain is `none`. All nine rows (I-207, I-208, I-209, I-217, I-020, I-228, I-237, I-239, I-287) are now traced-only, with no artifact level. I-044 keeps certificate-checked as a records claim, through a relabel (`matrix/chain-relabels.json:73-81`). The relabel is justified. |
| R2 | **Partially resolved** | E4:28-31, :55-56, :187-214. Open, conditional, conjecture and unsupported rows are traced-only by status. For proved-paper, exhaustive-exact, numerical and calibration rows, every link bears load, so a paper step caps the row. Every row R2 named is now traced-only: I-008, I-093–I-096, I-129, I-216, I-218, I-146, I-289. Two gaps remain. First, I-227 has the same universal-on-finite-sweep pattern and is *reproduced* (N2). Second, the per-row review R2 asked for (I-372, I-377, I-358) was not done: these rows are traced-only, with artifact level *reproduced*. That is conservative and acceptable. |
| R3 | **Partially resolved** | `not_covered` is in `part-E1.json:2244, 2354, 2375` and in `E1_build_part.py:355-360, 377-378`. E4 uses it at :126-132. I-071, I-129 and I-088 no longer get a level from those items. However, the per-claim result R3 asked for exists only for these three items. The other partial formal-coverage items (E1-66, E1-67, E1-70, E1-71, E1-85, E1-101) still have no per-claim outcome; see O-3 for I-149. E1-98's recorded reason does not fit I-088 (O-2). |
| R4 | **Resolved** | `E2_bh02.py:33-99, :130-134`. The sweep now evolves dense vectors and takes exact ranks. `part-E2.json:125-145` (E2-07) rests on the BHb `checks.py` replay, which I re-ran: byte-identical. The CI proposal in part-E2.md is corrected. My mutation test confirms the sweep can fail (see below). One residual weakness remains: the sweep does not check that the permutation is actually applied (O-4). |
| R5 | **Resolved** | E2-11 is now `fail` (`part-E2.json:207-228`), and it records R-03's narrowed definition in `limits`. E2-10 and E2-11 carry `failure_scope` (:204, :227), and E4:205 uses it as the basis. The failure at L56 is correct against L30 at 4a260ca9: only L30, L56 and L84 contain "exact probe", so the two tags are now graded the same way. A note on the reading is at O-6. |
| R6 | **Resolved for I-063; introduces N1** | `matrix/chain-relabels.json` is applied at `merge_matrix.py:43-54`, which checks that each entry's source and old layer match the chain. I-063 is certificate-checked on `finite_horizon_equivalence` (E1-06 and E1-57). Four of the relabels, however, are not justified by their links' own text (N1). |
| R7 | **Resolved** | E4:405-409 and `render_matrix.py:130-135` compare every row's level and basis. My mutation test detects a change to a level, a swap of two levels, a change to a basis, and a change to `evidence.json` alone. |
| O1 | **Resolved, with a loose case** | E4:80-96, :141-151. I-045's BH-02 link now matches only E3-18, and E2-01 and E3-17 are rejected. However, a link that names no record or probe file matches *every* computation item that lists the row. That is how I-227 gets its level (N2). |
| O2 | **Partially resolved** | E2-12 now lists I-368, I-370 and I-379, and they are *reproduced*. E2-17 lists I-172, but this has no effect, because I-172's chain has no computation link (artifact level `None`). I-123 records E2-13 as counter-evidence. I-124 does not, although E4:200 says it does: the `UNSUPPORTED`/`OVERCLAIM` filter at E4:199 excludes I-124, whose verdict is IMPRECISE. |
| O3 | **Resolved** | E4:103-109, :133, :150. A matched failed item fails the link. |
| O4 | **Resolved** | EVIDENCE.md:207-209 states the 9 of 14 modules, the log-text limit and the unchecked DOI and archive. E3-14 is reworded (`part-E3.json:278-280`). The E1 lean-certificate items still say "exactly the three axioms" in `what`, but their `limits` state the log-text basis, as before. |
| O5 | **Resolved** | E4:8-9, :34-37; EVIDENCE.md:7. Rows now carry `artifact_level` and `artifact_role`. I-225 shows traced-only, with *reproduced* as counter-evidence. |
| O6 | **Resolved** | E2-19 is now typed `ci-receipt` (`part-E2.json:402-404`). I-309's link is relabelled to `none` (`chain-relabels.json:64-72`). |
| O7 | **Mostly resolved** | `b5_check.py:89-91, :147-159` add the countercontrols, and `nsimplify` is gone. The controls are printed but do not gate: with a mutant, the script prints `False` and still exits 0 (O-5). |
| O8 | **Resolved as documentation** | `merge_matrix.py:9-11` and E4:5-6 document the order. R7's control covers copying the levels into `matrix.json`, but nothing covers the chains (N3). |

## New required changes

### N1. Four relabels contradict their links' text and raise I-052 and I-258

**Location.** `matrix/chain-relabels.json:3-54`: I-042 link 1, I-052 links 0 and 1, I-258 link 5 and I-281 link 5,
each `kernel → paper-derivation`. Grading at E4:188-190.

**What is wrong.**

- The links' own text says each step is a kernel result, not a paper derivation:
  - I-052 link 0: "Theorem 4, independence, oi_alone_not_qm: … no paper proof (proof inventory: kernel-only)";
  - I-052 link 1: "no written proofs";
  - I-042 link 1: "kernel proofs and no paper proof".
- `inventory/PROOFS-README.md:155` classifies GR.md:218 as **kernel-only**.
- I-052's verdict is MISCITED precisely *because* these results have no written proofs. Relabelling them as
  `paper-derivation` records the opposite of the row's own finding.
- The relabel also has a mechanical effect. In a proved-kernel row, E4 grades only the kernel links, so a link
  relabelled `paper-derivation` drops out of the grading.
- Only 7 rows went up a level between 290822b3 and 818bcd60: I-034, I-052, I-063, I-258, I-368, I-370 and I-379.
  I-052 and I-258 are among them, and they went up only because of these relabels.

**Failure scenario: I-258.**

- I-258 is "which of (iii)–(v) a physical substratum supplies is open".
- Its link 5 is GR.md:266, the layer-flow form. That passage cites kernel declarations: `derivedOI_qm_iff_layerFlowExecutable'`, `configurationLevel_not_layerFlowExecutable` and others in `C5Discovery`, `ExecSource` and `TypedCompletion`.
- `part-E1.json` contains no item for any of them (`grep -c C5Discovery` gives 0; no `layerFlow` match).
- At 290822b3 this kernel step held I-258 at traced-only. Now the step has dropped out of the grading, and I-258 is
  certificate-checked although one of its kernel steps was never checked.

For I-052, the level would probably hold after a correct fix, since `oi_alone_not_qm`, `five_way_minimality` and
`exactAll_iff_physical_general` have E1 items. But the basis "weakest of its kernel links" now covers only
`bridge_traj`, while the claim covers all of §3.2–§3.3.

**Fix.**

- Correct these links to `kernel` with declaration sources: the declarations GR.md:218-228, GR.md:266 and Main.md:624
  cite. This needs either a source field in `chain-relabels.json` or edits to the part files.
- Add E1 items for the layer-flow declarations, or leave I-258 at traced-only with the gap recorded.
- The relabels of I-063 (ledger → none), I-282 (ROADMAP → none), I-309 (git → none) and I-044 (status line → none)
  are justified. Keep them.

### N2. I-227, a universal claim, is reproduced on a finite sweep

**Location.** `matrix/part-B3.json:1936` (I-227's chain); E4:141-151 (the matching).

**What is wrong.**

- I-227 is "H-scramble fails for every bijection acting on a definite initial configuration …". It is proved-paper,
  and its level is *reproduced*.
- All three of its links are labelled `exact-algebra`:
  - link 0 is a paper line, GR.md:833, carrying the one-line argument;
  - link 1 is BHb REPORT.md:14, whose own text says "the universal claim rests on the one-line proof";
  - link 2 is the book mirror, ch07:126.
- Links 0 and 2 name no record or probe file, so any computation item that lists the row matches them. E2-07 and
  E3-18 match all three links.
- E2-07's own `limits` say: "The universal claim rests on the one-line proof …; the sweeps check it at three sizes."
- I-216 and I-218 have the same pattern: a written proof plus an exhaustive check. They are now traced-only because
  their proof link is labelled `paper-derivation`. A label decides between the two outcomes. This is the "finite test
  → universal claim" case from the Code Review Rules.

**Failure scenario.** MATRIX.md shows "H-scramble fails for every bijection …" at *reproduced*. That level asserts the
audit regenerated a universal result, when it regenerated three finite sweeps.

**Fix.**

- Relabel I-227 links 0 and 1, which carry the proof, as `paper-derivation`. I-227 then becomes traced-only, with
  artifact level *reproduced*, as I-216 is.
- Alternatively, let an `exact-algebra` link be matched only by an item that checks the algebra exactly, such as
  E2-12's symbolic checks, and not by an enumeration.
- I checked the other proved-paper rows above traced-only. Their universal clauses are checked symbolically: I-086
  with `p` symbolic in `E2_small_exact.py:41-44`, and I-366 and I-381 with a general 2×2 matrix in
  `E2_appendixB.py:140, :157-160`. Their levels are sound.

### N3. Nothing checks the chains against chain-relabels.json or the part files

**Location.**

- E4:397 renders the relabel list from `matrix/chain-relabels.json`.
- E4:113 grades the chains from `matrix.json`.
- `merge_matrix.py` has no `--check` mode.

**Failure scenario, demonstrated.**

1. In a scratch copy, I set I-063's relabel `to` field to `paper-derivation` and re-ran `E4_aggregate.py` without
   re-running the merge.
2. Both `E4 --check` and `render --check` then **pass**.
3. EVIDENCE.md:166 now says "kernel → paper-derivation", while `matrix.json` still has `none`.
4. Editing a chain in `matrix/part-B3.json` alone also passes both checks.

So a correction the matrix never received can be published as applied, and the levels are computed from stale chains.
This is the §A.25 drift pattern on the file this commit adds.

**Fix.** Either of:

- add `merge_matrix.py --check`, which re-merges in memory and compares the result with `matrix.json`'s bytes;
- have E4 `--check` assert, for each relabel, that the link in `matrix.json` has `layer == to` and
  `mapper_layer == from`.

## Optional changes

**O-1. The docstring does not match the code at three points** (E4:17, :28-29).

- File-source kernel links are matched only to items of type lean-certificate, formal-coverage or ci-receipt (E4:178),
  from any part, E2 included. The docstring says "the E1 or E3 items naming that file". A literal reading gives I-053
  traced-only: E1-122, an open-obligation item at traced-only, names `papers/introduction_repro/README.md`.
- Proved-kernel rows also drop computation links, not only paper, literature and none links. I-034 link 1 is an
  unmatched `exact-algebra` link.
- The "restate the result" justification does not fit the open-status context links of I-147, I-258, I-259, I-300
  and I-302 (ROADMAP P0, F2 and H-∞). Say instead that these are context.

**O-2. E1-98's `not_covered` reason fits I-089, not I-088.** I-088 says only "A finite bijection has finite order
$L$". The multi-time-law clause is I-089. Restate the reason: the kernel's statement is the periodicity of rooted
maps, and the finite order is a step inside the proof (`pow_card_eq_one`, RootedClassification.lean:144). I-088's
level, traced-only, is unchanged.

**O-3. Give E1-71 a per-claim result for I-149.** I-149 includes "compose exactly across times". E1-71's limit says
`CoherentLift` does not encode this, and the GL2 docstring (CoherentLiftGauge.lean:531-532; see also :67) calls the cocycle
condition vacuous. If the clause is covered because it is vacuous, record that; if not, add `not_covered`. Do the same
for the other partial coverage items.

**O-4. Add a check in `E2_bh02.py` that the permutation is applied.**

- A mutant that never applies the permutation (`nxt[x] += amp`) passes every check and gives
  `all_as_reported: true`. Its CC-a counts are 48 and 241,920, against 64 and 677,376.
- CC-a fires on the start vector before any evolution, so it tests the rank function and not the evolution.
- Fix: assert the recorded CC-a counts, or the expected total of the orbit lengths.
- E2-07's "448 states" mutant is not retained in the file, so that statement cannot be reproduced.

**O-5. Make `b5_check.py` exit nonzero when a countercontrol is False.** Mutants that condition the CMI on X0, or set
`c3 := a/(1+a)`, print `False` tuples and still exit 0.

**O-6. State the reading behind E2-11's failure.** The probes enumerate each instance's full trajectory space exactly.
They fail L30 only if "exhaustive" means exhaustive over a class of laws, which is the corpus's usage ("exhaustive
over S_8"). Unlike E2-10, E2-11 has no second ground such as floating point. Say in `failure_scope` that its failure
rests on this reading alone.

**O-7. Close the listing gaps.**

- I-384 and I-385 ("unpublished research record, internally reviewed") are traced-only. No ci-receipt item lists
  them, though E3-16, E3-17 and E3-18 check exactly these facts. I-044, a claim of the same kind, is
  certificate-checked.
- I-124 (see O2 in the table).
- I-172: listing it has no effect while its chain has no computation link.

## Independent re-implementation (`scripts/reagg2.py`, `scripts/reagg2_typed.py`)

Both scripts implement E4's docstring and import nothing from E4.

- **Literal reading** (`reagg2.py`): 1 difference, I-053. It is traced-only where `evidence.json` has
  certificate-checked, because E1-122 (open-obligation, traced-only) names the README that I-053's link 0 cites. This
  is the docstring gap in O-1.
- **With the code's type restriction** (`reagg2_typed.py`): **0 differences in 409 rows.** The counts are 43
  reproduced, 130 certificate-checked, 233 traced-only and 3 failed, which matches the commit message.
- Adding the E2 items to the file-source matching makes no difference. No failed row has an open, conditional,
  conjecture or unsupported status.

**Is the rule monotone?**

- **Raising an item's level never lowers a row.** The rule is monotone in item levels.
- **Adding a link never raises a row, with one exception.** Within a fixed proof status, extra links can only lower
  the level. The exception is a proved-kernel row with no kernel link (I-308, I-309, I-310, I-312): adding a kernel
  link would switch the graded set from all links to that kernel link. No row is affected now.
- **The one real breach is the relabel route.** Relabelling a kernel link as `paper-derivation` in a proved-kernel row
  removes it from the grading. This is how N1 raises two rows.

## Spot checks (chain, items and level against the claim)

| Row | Level | Assessment |
|---|---|---|
| I-002 | certificate-checked | Correct: E1-06 and E1-57 on `finite_horizon_equivalence`. |
| I-063 | certificate-checked | Correct after the ledger relabel. |
| I-088 | traced-only | The level is defensible. The reason recorded is I-089's (O-2). |
| I-129 | traced-only | Correct: a paper step, and E1-92 is excluded by `not_covered`. |
| I-071 | failed | Correct given E2-11. The basis scopes the failure to the tag, and link 5 is excluded by E1-99. |
| I-103 | failed | Correct. The scope says the bound and its instance values stand. |
| I-054 | failed | Consistent: both tags fail, and both scopes are recorded. |
| I-225 | traced-only | Correct: unsupported, with artifact level *reproduced* as counter-evidence. |
| I-123 | traced-only | Correct, with E2-13 recorded as counter-evidence. I-124 lacks it (O-7). |
| I-045 | reproduced | Acceptable. This is a records claim. E2-01 and E3-17 cover BH-01, and E3-18 alone covers BH-02. |
| I-309 | certificate-checked | Correct. The chain has only none links and is graded on ci-receipts; this is the weakest level, which is conservative. |
| I-044 | certificate-checked | Correct. The relabel is justified, and E3-16 to E3-19 apply. |
| I-216 | traced-only | Correct per R2, with artifact level *reproduced*. |
| I-372 | traced-only | Conservative. The computation covers the statement, and Main:278 defines the embedding. |
| I-384 | traced-only | This is a listing gap (O-7). |
| I-227 | reproduced | **Wrong** (N2). |
| I-258 | certificate-checked | **Unsupported** (N1). |
| I-052 | certificate-checked | The level is plausible, but the mechanism and basis are wrong (N1). |
| I-114, I-312, I-008, I-147, I-149 | as recorded | Consistent with the rule. For I-149, see O-3. |

## What I ran

All runs used `python3 -I -B`, in the worktree or in scratch copies.

**Integration and drift controls**

| Check | Result |
|---|---|
| `E4_aggregate.py --check`, `render_matrix.py --check` | Both pass. |
| `merge_matrix.py` in a scratch copy | `matrix.json` is byte-identical. |
| Full pipeline from scratch: evidence.json, EVIDENCE.md and MATRIX.md deleted, then merge → E4 → merge → render | All four files are byte-identical. |
| Drift mutations (`scripts/mutate.sh`, `outputs/drift-mutations.txt`) | A changed level, a swapped pair of levels, a changed basis and an edit to `evidence.json` alone are each caught by both checks. A chain edit in `matrix.json`, an edit to the relabel file and removing `not_covered` are caught by E4 only. An edit to a part file alone, and a relabel edit followed by an E4 re-run, are caught by neither (N3). |

**Computations and replays**

| Check | Result |
|---|---|
| All eight `E2_*.py` scripts | All exit 0, about 6 s in total. The values match the items: the BHa counts, C1 at 0/64 and 0/677,376, CC-b 2/2/2/1, `all_as_reported` true (`e2out/`). |
| BHb `checks.py` at eae01647 | 18 s. `result.json` is byte-identical: CC1 = 2, CC2 = 2, `K-rank` true. The files were extracted with `git show`, because the directory is export-ignored. |
| C1 mutation test (`scripts/bh02_mutants.py`, `outputs/bh02-mutants.txt`) | Caught: rank capped at 1, rank equal to the nonzero count, a leaking evolution and Hadamard-like mixing. A mutant that never applies the permutation passes (O-4). |
| `b5_check.py` and two mutants | The controls print `False`, and the exit code is 0 (O-5). |

**Analysis scripts**

| Check | Result |
|---|---|
| `scripts/reagg2.py`, `scripts/reagg2_typed.py` | See the re-implementation section. |
| `scripts/complinks.py` (`outputs/complinks.out`) | Every computation link, with its matched and rejected items. |
| `scripts/show.py` | Per-row dumps used for the spot checks. |
| Diff of levels, 290822b3 → 818bcd60 | 7 rows went up: I-034, I-052, I-063, I-258, I-368, I-370, I-379. |

**Reviewer files.** All are in
`S/rereview-e/`:
`scripts/`, `outputs/` and `e2out/`. The worktree was removed after the review.
