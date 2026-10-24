*Redaction (on committing this review to `design/emb/`): two absolute paths are replaced by descriptive references, the reviewer's worktree path in the home directory (header) and the reviewer's session scratchpad directory path in the system temporary directory (§Reviewer artifacts). The reviewer's `own/` checks are committed unchanged as `review2/`. No other change.*

# Re-review: corrected node 9 embedded-observer report (EMB) at `a9af8ef0`

**Reviewed:** `mc-node9/design/emb/` at `a9af8ef053a94fe89a42fd5776135622209733a0` (branch `research/missing-component-20261020`, draft PR #885), from a fresh detached worktree (`revemb2`, outside the repository).

**How the review was done:**
- Git was used read-only.
- The `design/emb` tree is identical at `3f11c8f7` and `a9af8ef0` (tree `6afbdab5`), so the corrections all landed in `3f11c8f7`. `a9af8ef0` only adds the G1 review.
- `EMB-REPORT.md` is blob `4e693fb7` at both commits.
- All arithmetic is exact over F₂.
- My own spot checks are `own/spot.py` and `own/rankFu.py` in this directory. They are a fresh explicit-state simulator with symbolic tracking, and they import nothing from the repo.

**Line references:**
- `EMB` means `EMB-REPORT.md`.
- `PREREG` and `NOTES` mean the files in `mc-node9/`.
- Line numbers are those at `a9af8ef0`.

## Disposition: **ACCEPT WITH CORRECTIONS**

All four blocking findings are fixed:
- **F2:** the persist bug is fixed. The rerun matches the patched output exactly.
- **F1, F3, F4:** correctly applied.
- **F5–F11:** applied. The author's departure from the review in F6 is correct: the review's bound was wrong.

One required correction remains, **N1**. It is wording only and needs no rerun. Some existence statements from the earlier review were adopted word for word, and they read as universal claims. The report's own data contradicts the universal reading. Once N1 is applied in EMB and in PREREG, the report's findings may be cited. A diff check is enough for that; a new full review is not needed.

N2–N7 are non-blocking.

## 1. The earlier findings, one by one

| finding | verdict | evidence |
|---|---|---|
| **F1** E2 Q-forget cell | **Applied.** The E2 row is merged into "E1, \|R\| ≥ 2". The cell says L1 does not apply, and W-E2's pointer alone gives a point mass at t = 4 and t = 12 with prior 4. My simulation confirms the pointer-only sequence 2 2 2 **1** 2 2 2 4 2 2 2 **1** 2 2 2 4 and the memory-only sequence of 4s. The cell's last sentence before the witness overstates; see **N1**. | EMB l.17; `own/spot.out` |
| **F2** persist bug | **Correct and complete.** See §1.1. | |
| **F3** headline | **Applied and consistent.** Every site says two separate limits: one read-out pair and one clean pair, either of which can be relaxed on its own. No "budget" wording is left. The two remaining uses of "budget" (EMB l.223, l.283) are compute budgets. "lifts it" and "determine" are worded universally; see **N1**. | EMB l.22, l.116, l.239, l.252, l.260, l.308 |
| **F4** classification | **Applied.** K-EXTHIST is ELABORATING; L1 and the r = m form are NEW pending the literature gate; L3 is CONFIRMING. | EMB l.264–267 |
| **F5** L1 presentation | **Applied.** (a) Contradiction hypothesis: l.108. (b) and (c) kᵢ ≠ 0 and k₁ = k₂: l.115. (d) Scope: l.116. I re-derived every line of the proof and it is correct. | EMB l.106–117 |
| **F6** L2 | **Applied. The author's capacity bound is right and the review's was wrong.** See §1.2. The r = m proof is correct, with one implicit step (N4). | EMB l.124–126 |
| **F7** W-E2 content | **Applied, and the numbers are right.** See §1.3. | EMB l.17, l.49, l.164–167, l.188–201 |
| **F8** E2 is vacuous | **Applied.** The rows are merged (l.17), the reduction is kept in §1 (l.42), and the nonlinear note sits under the table (l.20). | |
| **F9** H9–H11, H4, H6 | **Applied.** "an observer who builds one more memory site" is gone (no match for "builds"). Q-build is now qualified by H9 (l.12). | EMB l.241–248 |
| **F10** engine identities | **Applied.** They form a separate table, apart from the verdict controls. | EMB l.79–98 |
| **F11** wording | **Applied, every item.** E1-K2 prior 2, 1, 2 (l.68; my simulation agrees). Transient knowledge (l.24). Retention scoped to W-E3 (l.215). The REC analogy and "requirement 5" are gone. L3 is scoped to "this lattice, under FULL" (l.133). "C5 needs Q-build" is marked as the report's own framing (l.12). Base clause (l.5). Replay recipe (l.300). | |

### 1.1 F2 in detail

- **The fix.** At `e12_exhaustive.py` l.175–176 the background rows are now `Tb`. `T0` is assigned only at l.131 and read only at l.145, so no other reuse remains.
- **The counts.** The committed `e12_exhaustive_n6.out` equals the earlier reviewer's `patched/e12_patched_n6.out` except for one `[elapsed]` line (107 s vs 108 s).
  - FULL `persist` lines: 0 in the output.
  - U and V: n = 5, 112 → 114 and 221 → 232; n = 6, 643 → 645, U 1683 / V 1679 → **1733**, and U 1671 / V 1653 → **1709**.
  - The old FULL values quoted in Corrections are confirmed in `b71199a8`'s output: 31 and 89 at n = 5, and 111, 1272 and 603 at n = 6. The earlier review listed only four of them, and the author correctly adds 89.
  - The script no longer prints the line `earliest 'old record kept…' decl=FULL`.
- **The withdrawn claim.** There is no match in EMB for "displayed lattice", "first FULL" or "fresh uncertainty". The only remaining mention of "old records retained…" is the definition in the script's docstring (l.26–27), which is fine. The independent recount `review/persist_check.out` gives FULL total 0 at n ≤ 5.

### 1.2 F6 in detail

**The capacity bound.**
- The span of F ∪ T has dimension 2r + 2m. Complete learning maps it onto span F_u, with kernel span(F ∪ T) ∩ K. That gives dim K ≥ 2m.
- Full prior with T_u ⊆ span F_u gives rank F_u ≥ 2m. F_u has 2r rows, so rank F_u ≤ 2r. Together these give m ≤ r.
- The review's "m ≤ rank F_u ≤ r" mixes up pairs and functionals, and it fails:
  - in W-E2 at t = 4, where the visible cells (u₃ + u₄, v₃ + v₄, u₀ + v₃ + v₄, v₀ + u₃ + u₄) (EMB l.193–194) have rank F_u = 4 > r = 2;
  - in the mixed n = 3 case, where rank F_u = 4 > r = 2 (`own/rankFu.out`).

**The r = m proof.** I checked each step:
- ψ is injective because rank T_u = 2m.
- ω(ψh, κg) = ω(ψh, ψg) follows from ω(W_V, W_T) = 0.
- κ is injective by non-degeneracy of W_V.
- The expansion gives ω(κg, κg′) = ω(g, g′) + ω(ψg, ψg′) over F₂.
- The adjoint exists because W_T is non-degenerate.
- K is non-degenerate under FULL.
- For m = 1, ψ†ψ = det ψ · I = I, which gives L1.

### 1.3 F7 in detail

My spot checks (`own/spot.out`):
- **W-E2:** own-content rank 0 at t = 4 and t = 12, the only learning times.
- **The rank-2 example:** n = 5, edges (0,1), (0,3), (0,4), (1,2), R = {0, 3, 4}, toy 1. The support sequence is 2 2 2 **1** 2 2 2 4 2 2 2 **1** 2 2 2 4, with prior 4 throughout and own-content rank 2 at every t. This confirms it.
- **n = 4, path 3–0–1–2, R = {2, 3}, toy 0, t = 2:** support 1, prior 4, own rank 2. This confirms it.

The 6/19/25 split of 50 matches `review/single_app.out`:
- with a bath, n = 5: 1 + 2 + 2;
- with a bath, n = 6: 5 + 17 + 23.

## 2. Propagation into PREREG and NOTES

**The citation by blob.**
- It is accurate: `4e693fb7` is `EMB-REPORT.md` at both `3f11c8f7` and `a9af8ef0`.
- It departs from PREREG's own tag convention, which l.36 defines as "[rec, design/… at SHA] … at that commit". See **N5**.

**Model A's clean-resource declaration.**
- It now makes (i), the number of visible read-out sites, and (ii), the number of clean pairs, separate postulates (PREREG l.433–435, with §1.1 at l.107–110 and NOTES l.67–69).
- It no longer meets the EMB finding "by declaration".
- It says L1's hypotheses do not cover model A's coordinate-level pointer (l.437–439).
- The count in (ii) is not the one EMB calls operative, and (i) may leave out coin cells; see **N3**.

**Reliance on the old one-pair-budget headline.**
- None is left. The old "L1, a one-clean-site budget lemma" text and "This meets the emb finding below by declaration" are both gone.
- `grep` across `missing-component-20261020/**/*.md` finds no "one-clean", "budget lemma" or "second clean visible site" outside the report itself.
- The PREREG §4 baseline (l.471–481) restates the corrected findings. Two of its sentences carry the N1 overstatement.

## 3. Findings of this re-review

### N1 (required correction): existence results read as universal statements

These sentences came from the earlier review's replacement text. Each reads as a universal claim, and the report's own data refutes the universal reading.

| site | text | correct form |
|---|---|---|
| EMB l.17, Q-forget cell | "With two clean visible sites the apparatus does not forget." | "…the apparatus need not forget." |
| EMB l.22 | "…lifts it. Two clean visible sites determine the toy completely…" | "…can lift it. Two clean visible sites can determine the toy completely…" |
| PREREG l.473–474 | "relaxing either alone lifts it" | "can lift it" |
| PREREG l.477 | "Two clean visible sites determine the current toy state…" | "In some arrangements, two clean visible sites determine…" |

The report's own counterexamples:
- **Family A (EMB l.178):** a memory chain behind the pointer, with up to 5 clean visible sites, has no learning at any t.
- **Lattice-like graphs (l.185):** C₆, C₈, the grids and the cube learn **only for |R| ≥ 3**. Two clean visible sites never learn there.
- **The table (l.151):** at n = 6 with |R| = 2, 857 of 8524 cases learn.
- **The mixed declaration (l.161):** 1650 of 30 720 labelled cases at n = 5.

EMB l.252 ("removes it") reads as the same overstatement. Fix it with "can remove it".

Under AGENTS' claim/evidence rule (witness → universal), this class is a blocker. It is fixed by those few words.

### N2 (non-blocking): the mixed n = 3 witness is described ambiguously

- **What the report says:** EMB l.161 and PREREG l.475 call it "the 3-site path at t = 2: R = {0 FULL, 1 NONE}, toy 2".
- **What the witness actually is:** `review/l1_attack.out` [5] has edges (0,1), (0,2). That is the path 1–0–2, with the FULL site in the middle.
- **Why it matters:** on the labelled path 0–1–2 with the same R and toy, t = 2 gives support 2, and the point masses at t = 3 and t = 4 are overwrite (prior 2 and 1; `own/spot.out`).
- The visible-cell formula on l.161 fixes the right case, but the prose should read "path 1–0–2 (centre 0, the FULL site)".

### N3 (non-blocking; pre-freeze for PREREG): the counts declared do not match EMB's operative counts

**Clean pairs versus clean coordinates.**
- EMB's L2 (l.125) and H2 (l.239) say the operative counts are **clean coordinates** (≥ 2m) and visible pairs (≥ m).
- The case "a U, b U" has two clean coordinates and **zero** clean pairs, and it learns: 6, 24 and 300 cases (EMB l.162).
- PREREG §1.1 (l.107–110), §4 (l.434–435) and NOTES l.68 instead make the **number of clean pairs** the second postulate. That conflicts with PREREG's own l.476.
- For model A nothing is missed, because the clean coordinates are declared by count in l.429–431 (b_p Q cells and b_m X cells). But the general §1.1 rule, which Option B inherits, should count clean coordinates, and say which of them come with their conjugate.

**Coin cells.**
- Postulate (i) lists only the pointers and the memory cells.
- §1.2 (l.135) introduces **visible coin cells** that hold bath bits. These are visible cells with no clean coordinate, exactly the class that EMB shows can lift L1.
- The declaration should either count coins under (i) or state that no coupling step brings a coin into contact with the toy, a pointer or the records.

**A small logic point.** In PREREG l.435–436, "Withholding a second clean pair is not enough: … and so does a second clean pair read through one site" gives the second clause as a reason for the first, but it is not one. It supports the claim that the clean count also matters.

### N4 (non-blocking): the r = m proof uses a step it does not state, and one label is confusing

- **The unstated step.** Writing g = ψg + κg uniquely needs W_V ∩ K = 0. That follows from capacity: rank F_u ≥ 2m = 2r = number of rows, so F_u is injective. Add one clause saying so.
- **The label.** "B := ψ, the memory → target read-off map W_T → W_V" names the map in one direction and then gives it the other. Write "the target-to-memory decomposition map W_T → W_V".
- **The notation.** "v ↦ ω(v, (I + B\*B)v′)" should be the bilinear form (v, v′) ↦ ….

### N5 (non-blocking): citation form and provenance

- **Cite the commit or the tree.** PREREG l.36 defines the tag as "at that commit". A blob also pins only the report text, not the scripts and outputs its findings rest on. "design/emb at blob" also calls a blob a directory, at PREREG l.112, l.436 and l.471 and NOTES l.69 and l.71.
  - Now that the commit exists, cite `design/emb at 3f11c8f7` (tree `6afbdab5`). It could not cite itself from inside that commit.
  - Keep the blob as a secondary pin if you want it.
  - This is also the moment to update "reviewed REVISE → corrected" to this review's disposition.
- **The earlier EMB review is not in the repository.**
  - The report cites REVIEW-EMB-b71199a8 (l.3, l.304) and its F-numbers.
  - It attributes the r = m proof to the review (l.126).
  - The G1 precedent committed its review for exactly this reason (`a9af8ef0`: "commit the independent review cited by the corrected records").
  - Either commit it under `design/emb/review/` and add it to SHA256SUMS, or make §Corrections readable on its own. §A.42 item 2 allows provenance off the branch, but the F-numbers cannot be resolved without the review.

### N6 (non-blocking): the deviation from the review in F6 is not recorded

The Corrections entry for F6 (l.311) presents 2m ≤ rank F_u ≤ 2r as if it applied the review. In fact it corrects the review's bound. Say so in one clause, with the W-E2 t = 4 counterexample (rank F_u = 4 > r = 2).

### N7 (trivial)

- **Own-content counts (l.167).** "in 19 own-content rank 1, and in 25 own-content rank 2" are maxima over the learning times (`single_app.py`). Write "maximum own-content rank 1 (19) or 2 (25)".
- **"former E2 row" (l.17).** This is the report narrating its own revision history. It is tolerable in a design record with a §Corrections section. It can go, since l.42 already gives the reduction.

## 4. Scope

- No M0–M5 verdict is given, and there is no claim about OI in general.
- EMB l.5 disclaims both. The headline is bounded ("Within these bounds", l.22). L3 is scoped (l.133).
- PREREG l.482 keeps "No decision rule rests on these until a review accepts the corrected report."
- Nothing contradicts this, apart from the universal wording in N1, which is internal to the lattice regime.

## 5. Replay results

All replays ran from a copy of the committed directory, `replay/`. Outputs are in `rev_out/` and `e12_replay.out`.

| script | result | time |
|---|---|---|
| `e12_exhaustive.py 6` | **byte-identical**: even the `[elapsed 107 s]` line matched this time | 1 min 47 s |
| `review/witness_check.py` | byte-identical | < 1 s |
| `review/content_check.py` | byte-identical | 1 s |
| `review/single_app.py` | byte-identical | 1 s |
| `review/persist_check.py` | byte-identical | 8 s |
| `review/l2_check.py` | byte-identical | 3 s |
| `review/l1_attack.py` | byte-identical (fixed seed) | 6 s |
| `check_core.py` | byte-identical | 20 s |
| `e1_controls.py`, `e2_families.py`, `e3_w4.py`, `mtarget.py 6` | byte-identical | < 5 s each |

- **`e3_gating.py`: not replayed.** It is unchanged since `b71199a8`, where the earlier review replayed it, and it takes about 6 min (§A.40).
- **The committed review scripts.** They are identical to the earlier reviewer's originals, except for the `sys.path` line in `l2_check.py` and `single_app.py`, which EMB l.293 discloses. `witness_check.out` is byte-identical to the reviewer's original.
- **SHA256SUMS: 31 entries, all OK.** The brief expected 30. The 31 are 16 scripts (9 main and 7 review), 13 outputs (7 main and 6 review) and 2 timing files. The only files in the directory it does not list are `EMB-REPORT.md` and `SHA256SUMS`.

## Reviewer artifacts (scratch, not for the repo)

All are in the reviewer's session scratchpad directory `revemb2/`:
- `own/spot.py` and `own/spot.out`
- `own/rankFu.py` and `own/rankFu.out`
- `replay/`
- `rev_out/`
- `e12_replay.out`
- `sha_check.txt`
