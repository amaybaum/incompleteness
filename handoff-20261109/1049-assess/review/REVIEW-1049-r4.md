# REVIEW-1049-r4: independent review of ASSESS-1049 r4 (linear vs affine microscopic dynamics)

**WIP / UNVERIFIED. Model-written (Claude Code reviewer subagent, 2026-11-09). This is a fresh,
independent review, not a human review.** It adopts, promotes and authorizes nothing. I made no git
or GitHub write and no manuscript edit. I wrote only this file and `review/rv4_scope_checks.py`.
Re-run outputs were hashed from stdout and not kept on disk.

- **Under review.** `ASSESS-1049.md` r4, sha256
  `14c2279f384818b454209409f2e8bb3e4d58a5960b8601baac0563dd85b5199a`. I re-hashed it first, and it
  matched. Also checked: `r3/ASSESS-1049.md` is `75d6af06…2fa9`, `review/REVIEW-1049-r3.md` is
  `aa343005…bb4b` and `DISPOSITIONS-r4.md` is `9d26ba43…37a0`.
- **Sources.** Every corpus read used `git show fd539e15:<path>`. `origin/main` is `cac5d264`. The
  local working tree is clean at `b1d782f9`, an earlier `main` commit. No manuscript file is
  modified, so the proposals exist only in the record.
- **Reviewer probe.** `review/rv4_scope_checks.py`, sha256
  `0d8427bc31f70746d651837a7da5e4c58a355b7fe1d2b3f0c209654dc712e92f`. Its stdout has sha256
  `3f5f51c2d1bc1e294a08f1793c6d4a3679895ed41e9a579c0c0e995ec080df5c`. Result: ALL PASS (39 checks),
  exit 0, about 1 s, run with `python3 -I` from `/tmp`.
  - It is an exact generic check: integer arithmetic on finite sets.
  - It imports only `itertools`, `math` and `sys`, and nothing from `probes/` or `review/`.
  - It iterates no dynamics and instantiates no OI mechanism.

## Verdict: REVISE

R3-B1, R3-B2 and N1–N9 are fixed correctly (§1). The writer's four deviations are sound (§2). F7 is
correct, and I proved it independently (§3), but its scope is incomplete. That gives one blocker,
which is textual and needs no new computation.

- **R4-B1. F7 misses the same defect at q ≤ 3 in three sibling clauses.** F7 qualifies "a proper
  subgroup of all permutations" at Sub:274 and SM:96. It does not cover the clauses that make the
  same contrast, which are equally false at q = 2, 3, where every permutation of ℤ/q is affine:
  - SM:96, the paragraph's first sentence: the gauge transformations are the additive-group
    automorphisms, "not arbitrary relabellings of ℤ/qℤ" (SM.tex:709–710 at both commits);
  - Sub:274, the same paragraph as F7's clause: "the strong reading (arbitrary relabellings of
    ℤ/qℤ are gauge) *overshoots* — a nonlinear permutation conjugating a linear rule …"
    (Substratum.tex:1762–1768). At q ≤ 3 no nonlinear permutation exists. The strong reading then
    coincides with the group the next sentence says delivers "without overshooting", so it does not
    overshoot;
  - SM:811: "The physical gauge is the alphabet's additive-automorphism group — not arbitrary
    relabellings of ℤ/qℤ, since a nonlinear relabelling changes the fluctuation dispersion"
    (SM.tex:4683–4685 at fd539e15, :4684–4686 at cac5d264).

  The corpus takes q ≥ 2 throughout (SM:90; Sub:255). So each of these clauses is false as stated at
  q = 2, 3, on F7's own ground.
  - Applying F7's correction alone would leave SM:96's first sentence asserting the contrast that
    its last clause then qualifies. The same holds in the Sub:274 paragraph.
  - The cause is the propagation grep, which was literal (`git grep "proper subgroup"`). §A.25
    step 1 asks for paraphrases too.
  - This is the R3-B2 class: a false clause missed in a passage for which a correction is proposed.

  **Fix.** Extend F7 to the three clauses, each with a qualifier-only V1 in F7's form, or say why a
  clause needs none. SM:811 may be scoped by SM:92's "large-q statement" for §6.5. If so, say that
  rather than leaving it unexamined. Carry the extension into §0 item 3, §6 Q1(a), the §2.3 Sub:274
  row (nit M4) and DISPOSITIONS.

***

## 1. The r3 findings

### R3-B1 (headline): fixed

The withdrawal (shown) and the recovery (conditional on GA7-α) are now separate at every site that
R3-B1 listed, and at the necessary consequences.

| Site | r4 text | Check |
|---|---|---|
| §0 item 1 | "it is, within the link-sum class with non-additive link maps (GA7-α)"; "The corpus writes A6's interface as a link sum only with additive links" | separate; wording nit M2 |
| §0 item 2 | heading "not refuted; conditionally recovered"; separate bullets for **Withdrawal (shown)**, **Recovery … (conditional on GA7-α)** and G2 | ✓ |
| §2.1 (R-uni) d = 2, 3 bullet; *Consequence*; A1–A6 bullet; "How the site claims fare" | GA7-α named at each; the written interface is "linear by type", with gauge idle; "exactly when" holds one way as written, and both ways under GA7-α for q ≥ 3 | ✓ |
| §2.3 rows Sub:100, :104, :220, ch02:84 = FULL:718 ("As Sub:100"), Structure:259 | "Not refuted; its gauge route is recovered conditionally on GA7-α" or equivalent | ✓ |
| §2.4 item 1 corollary; item 2 bold | the review's suggested wording, adapted; "not an overstatement" is gone | ✓ |
| O-A, O-F, O-G, §6 Q2 | O-A states "not refuted" and "recovered only conditionally"; O-F says "not refuted under A6"; O-G says "under GA7-α it comes from gauge"; Q2 says "no counterexample" | ✓ |
| §7 F-9 | "**POSITIVE under GA7-α** … Under the written interface the relevant results are E2 and the kernel's typing" | ✓ |

My re-grep of r4 for "recover", "written interface", "not an overstatement" and "holds as stated"
found no unconditional recovery claim at an A1–A6 site. The unqualified "link-sum class" in §2.4's
title, at F-1 and in the remark under the §2.3.1 table names E3's mathematical class (arbitrary
link maps), not the corpus's interface, so it is correct.

### R3-B2 (Sub:272, second sentence): fixed

- **F6 is correct.** The clause needs "unobservable ⇒ affine".
  - Under (R-uni) it is false for d = 2, 3. I re-coded the three witnesses (rv4 W4): d = 2 at
    q = 7, and d = 3 at q = 5 and at q = 2. Each satisfies f(λx + c𝟙) = λf(x) + 2c for every unit
    λ, every c and every x, and none is affine. The countercontrol 4Σ + 1 at q = 7 fails.
  - Under (R-rel) it is false at every d.
  - It is true only under (R-site) or GA7-α.
  - The coordinates are right: the clause is at Substratum.tex:1733–1735.
- **V1** replaces "the affine restriction" with "the principle itself".
  - The resulting clause is true: deriving the principle would make the principle unconditional.
  - It agrees with the sentence's V1 conclusion, which is about uniform symmetries, and with the
    paragraph's last sentence.
  - The subject changes inside the clause, so this is a correction, not assert-then-qualify (§A.30).
- **V2** adds the negative claim and is correctly marked as needing P1's proof on `main`.
- **Propagation.** F6 is in the §2.3 Sub:272 row ("four clauses … F1–F3, F6", `.tex` :1733–1739),
  the §2.1 `.tex` list, §0 item 3, F-8 and "Why V1 is a correction".
- **"Which reading each sentence uses."** The block is present and accurate.
  - Sentence 1 (V1) uses the base-point form.
  - Sentence 2 uses uniform symmetries, fixed by its parenthetical and its conclusion.
  - Sentence 3 is about the principle as stated.
  - The cost of the mix is stated, and it is put to the owner in Q1(d).

### N1–N9

| Nit | Fixed? | Check |
|---|---|---|
| N1 | yes | §2.3.1 inference row; F-8 heading and both bullets; §0 item 3; §2.1 (R-site) bullet. "Valid but unsound" under (a); "invalid" under (b) |
| N2 | yes, with precision nit M1 | The F1 cell, F1 and the link-sum remark are split into odd q and q = 2. "Each reading falsifies at least one clause" still holds, because F2 fails at q = 2 (P1's q = 2 rule, rv4 W4) |
| N3 | yes | G4's new bullet. The witness ((x₁ − x₂)², 0) at q = 3 (r4 C3). The K scope is carried into §0 item 1 and F-9 |
| N4 | yes | Sub:100 and Sub:220 rows, G1, §2.1. rv4 W6: x ↦ x² is affine on ℤ/q iff q = 2 (q = 2–16), so Σ x_j² is a non-affine link sum exactly for q ≥ 3 |
| N5 | yes | §2.3.1 second-sentence V1: valid under dynamical indistinguishability; conditional on the open "distinguished ⇒ resolvable" step in the observer-resolution reading. The r3 sentence moved into this bullet, and no content was lost |
| N6 | yes; the deviation is accepted (§2) | V1′; the hollowness sentences at Sub:272 V1 and Sub:274; Q1(d) |
| N7 | yes | §2.4 item 2 Assessment. The quote "the coupling is link-valued data on which the transformations act" is verbatim at Sub:102, ch02:86 and FULL:720 (fd539e15) |
| N8 | yes, with the writer's corrections (§2) | Verified at fd539e15: Substratum.tex:743 opens Sub:100's parenthetical and :744 carries "restricts the update to an affine one"; :1733–1739; :1768–1773; Structure.tex:980–982, :1144–1145, :1269–1271. One residual: nit M3 |
| N9 | yes | §2.4 item 2 and the GA7-cov row. SM:312's quote "stated on the observer-level branch … not the ℤ/qℤ alphabet of the substratum" is verbatim. `linkRule` (A6Instantiation.lean:103), `linkSubstratum` (:118) and the `Fin 6 → ZMod q` instance (:231–243) |

## 2. The writer's deviations

1. **Option β not taken: agreed.** The second sentence's V1 conclusion ("states that differ only
   in absolute amplitude") is a uniform notion. Reading "unobservability" in base-point form would
   force the conclusion into a form it cannot take. Option α is the smaller change, and it matches
   the paragraph's last sentence.
2. **The N8 coordinates: the writer is right on both points.** Sub:100's parenthetical opens at
   :743 ("(Amplitude-scale gauge invariance --- that the field-value scale is"). For Structure:301,
   "The hypothesis adds …" begins at the end of :1271, so r3's ":1273 is the next sentence" was my
   predecessor's error.
3. **No replacement text for the evaluative passages: agreed.** The three passages are "not
   viciously circular", "more primitive and better-motivated" and "more primitive and more
   defensible place". After V1 or V1′ none of them is mathematically false. Their adequacy is an
   editorial and evaluative judgement, and it is outside a paper-only unit's authority, so raising it
   in Q1(d) is right. Nit M6 adds one option to that question.
4. **V1′ adds "for q ≥ 4": correct and necessary.** Without it V1′ would restate F7's false
   clause. Nit M5 notes one more inherited clause in V1′.

## 3. F7

**The mathematics is correct.** rv4 W1 tests every permutation of ℤ/q for affinity directly; it does
not generate the family. p is affine iff p(x) = p(0) + (p(1) − p(0))x for all x, with p(1) − p(0) a
unit.
- For q = 2–8 the count is q·φ(q), with φ taken from the prime factorization.
- The count equals q! exactly when q ≤ 3: 2 = 2! and 6 = 3!, but 8 < 24, 20 < 120 and so on up to
  32 < 40320.
- Integer comparison gives q·φ(q) < q! for every 4 ≤ q ≤ 200. The paper reason is
  q·φ(q) ≤ q(q − 1) < q! for q ≥ 4.
- Controls: the transposition (0 1) at q = 4 is rejected, and 3x + 1 is accepted. Mutation:
  dropping the unit condition admits 8 non-bijective maps at q = 4, so the bijection filter is
  load-bearing.

**The kernel-carrier remark is correct.** On (ℤ/q)⁶ both the scalar family x ↦ λx + c and the full
AGL(6) are proper for q = 2–7 (rv4 W2). One side observation, for the record only: at (ℤ/2)²,
|AGL(2, 2)| = 24 = 4!. So properness on a K-component carrier depends on K, and it holds at the
kernel's K = 6.

**The cited sites and coordinates are right.**
- Sub:274's clause is at Substratum.tex:1771–1772, and SM:96's at SM.tex:717. Both are identical at
  fd539e15 and cac5d264.
- The Substratum blob is unchanged. In SM.tex the one added line falls within :781–794, after :717.
- The literal `git grep "proper subgroup"` over `papers/` and `book/` gives what r4 says: SM.md:96,
  SM.tex:717, Substratum.md:274, Substratum.tex:1771, and the unrelated Main:672.

**Scope.** The paraphrase sites are incomplete. That is R4-B1.

## 4. The cac5d264 move

`git diff fd539e15 cac5d264` touches only `papers/SM.{md,tex,pdf}`.
- `SM.md` has one line changed in place: 1769 lines at both commits.
- `SM.tex` gains one line, 9194 → 9195, inside the degree-bound sentence (:781–794).
- Substratum, Structure, Main, ch02, FULL `.md`/`.tex` and `verification/` have identical blobs at
  both commits.
- No clause cited or proposed for correction changed. SM:112 is cited at §2.1 and O-E only for
  G_SM's non-affinity and its switch on x_{i+1} = 0, which the change does not touch.
- Every `SM.tex` line the record cites (:717) is before the insertion.
- The one SM.tex coordinate that shifts is SM:811's, which r4 does not cite. R4-B1 gives both
  coordinates.

## 5. Probes, hunks and proposals

**Re-runs.** All ten scripts were re-run with `python3 -I` from a scratch directory, and stdout was
hashed against the stored `.out`: `p1`, `p2`, `p3`, `r2_gauge_inventory`, `r3_link_recovery`,
`r4_scope_checks`, `rv_p1`, `rv_p2`, `rv2_gauge_audit` and `rv3_link_affinity`. Every one exited 0,
printed ALL PASS and matched.
- `r4_scope_checks.py` (`23c659f4…b991`) prints 31 PASS lines, as §8 states.
- Its C1–C4 do what §8 says. C4 compares a generated set's size with q·φ(q), which my W1 replaces
  by direct testing, with the same result.

**Hunks.** I mapped each of the 50 hunks of `diff r3/ASSESS-1049.md ASSESS-1049.md` to a disposition
entry: the header, R3-B1, R3-B2/F6, N1–N9, F7, or §8. Every hunk is accounted for. The one entry
that DISPOSITIONS does not list explicitly is §0 item 3's sentence "At Sub:274 a subject-changing
variant (V1′) is also offered", a consequence of N6 (nit M7). The r3 bullet deleted at :527–528 is
carried into the new N5 bullet and not lost. No hunk touches a section the dispositions list as
unchanged.

**Proposals only in the file.** Confirmed. The working tree is clean, and no `papers/` or `book/`
file differs from its committed blob.

## 6. Scope, columns and register

- **Scope.** F-1 and F6 are scoped to d = 2, 3 and to rules outside the link-sum class. F7 is
  scoped to the alphabet ℤ/q, with the K = 6 carrier noted. No universal negative is stated. [H]
  material is used only as hypotheses (§A.46 item 7).
- **Column separation.** The reading table keeps (R-rel), (R-uni) and (R-site) in their own
  columns. The q = 2 material added for N2 sits in the (R-uni) cell only. The per-site table keeps
  "assumptions stated", "A6 / P1 under A6", "all satisfied?" and "disposition" apart. The
  withdrawal stays in the "all satisfied?" column ("no, under the written interface"), and the
  conditional recovery stays in "disposition".
- **Verification layers.** The new items are labelled by layer: F6 [A; X], F7 [A; X: r4 C4], G4
  [A; X], N4 [A; X]. No numerical evidence stands in for an exact claim.
- **Register.** All proposed paper text (F6 V1/V2, V1′, "for $q \ge 4$") is neutral under
  §A.32–§A.33. It has no reader instruction, no caps emphasis, no revision-history voice and no
  self-assessment.

## 7. Nits

- **M1 (F1 at q = 2).** "At q = 2 the comparative is true" holds in the κ-general form. The
  record's primary (R-uni) (§2.1, :208–210) is the κ = 2 form, and there the comparative holds only
  among rules with Σa even, which includes every isotropic rule. The affine rule x₊ₓ fails the
  κ = 2 form (rv4 W5; r4 C2). Say "in the κ-general form". F1's verdict does not change.
- **M2 (wording).** §0 item 1 says "the link-sum class with non-additive link maps", and the §2.4
  bold sentence says "the non-additive link-sum class". GA7-α is defined as link maps *not assumed*
  additive, which is the wording used elsewhere. Harmonize the two.
- **M3 (Sub:104 `.tex`).** The Sub:104 row now turns on "via the linearity-equivalence lemma",
  which is at Substratum.tex:785. The cited range is :783–784. Make it :783–785.
- **M4 (§2.3 Sub:274 row).** The row says "two clauses are false (F4–F5)". F7 (and R4-B1) add
  clauses at Sub:274, and SM:96 has no entry. Add a cross-reference to F7.
- **M5 (V1′, inherited clause).** V1′ re-proposes "it preserves the alphabet's '+'". For c ≠ 0,
  x ↦ λx + c is not an automorphism of (ℤ/q, +), because it moves 0. It preserves the affine
  operation x − y + z (rv4 W3). This is elementary and not a P1 finding, and it is defensible only
  under an affine-structure reading. Note it beside F7, or keep V1′'s wording identical to the
  source for that clause and say so.
- **M6 (Q1(d) completeness).** Q1(d) presents the remaining support for "Stated operationally it
  is *not* viciously circular" as hollow after V1. In the uniform form the principle does exclude
  some coherent non-affine F, for example (1/3)Σ + x₊ₓ² (rv2 R2c), without presupposing affinity.
  So if "excludes" is read existentially, a non-hollow support exists in the operational form. F2
  rests on the universal reading. Q1(d) should list this as an option for the owner.
- **M7 (DISPOSITIONS).** The N6 row should also list §0 item 3's V1′ sentence.
- **M8 (cosmetic).** §0 lines 67 and 77 of r4 overrun the wrap.

## 8. Summary

| ID | Kind | One line |
|---|---|---|
| R4-B1 | blocker | F7 is incomplete. The same false-at-q ≤ 3 contrast stands in SM:96's first sentence ("not arbitrary relabellings", SM.tex:709–710), in Sub:274's "strong reading … overshoots" (Substratum.tex:1762–1768) and in SM:811 (SM.tex:4683–4685; :4684–4686 at cac5d264). Extend F7 or disposition each; the grep was literal, not paraphrase-wide (§A.25 step 1) |
| M1 | nit | F1 at q = 2: the comparative holds in the κ-general form; in the κ = 2 form only for Σa even (x₊ₓ fails; rv4 W5) |
| M2 | nit | "non-additive link maps" → "link maps not assumed additive" (§0 item 1, §2.4 bold) |
| M3 | nit | Sub:104 `.tex` range :783–785 (the route clause is at :785) |
| M4 | nit | §2.3 Sub:274 row and SM:96: cross-reference F7 |
| M5 | nit | V1′'s inherited "preserves the alphabet's '+'" fails for c ≠ 0; x − y + z is preserved (rv4 W3) |
| M6 | nit | Q1(d): the existential reading of "excludes" gives the operational form a non-hollow support (rv2 R2c) |
| M7 | nit | DISPOSITIONS N6 row: add §0 item 3's V1′ sentence |
| M8 | nit | Cosmetic line-wrap at §0 :67, :77 |

**What re-review needs.** R4-B1 applied: F7 extended to the three clauses, or each one
dispositioned, and propagated to §0 item 3, Q1(a), the §2.3 row and DISPOSITIONS. Then a diff check
of the changed passages. No new computation is needed. rv4 W1 covers the q ≤ 3 equality on which
every one of the clauses rests.
