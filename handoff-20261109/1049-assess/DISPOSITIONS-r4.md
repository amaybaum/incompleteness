# ASSESS-1049 r4: dispositions of REVIEW-1049-r3

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).**

This file maps each finding of `review/REVIEW-1049-r3.md` to its change in `ASSESS-1049.md` r4.
- **Review.** sha256 `aa3430051ea4495a0b30131917283601f6aba5a49c32f697cd95f7426c3bbb4b`; verdict
  REVISE (blockers R3-B1, R3-B2; nits N1–N9).
- **From.** r3, copied unchanged to `r3/ASSESS-1049.md`, sha256
  `75d6af06fcac7750dcdd7677abf42fbbbeb50caa0acbb8db619e42fb39b82fa9`.
- **To.** r4, `ASSESS-1049.md`, sha256
  `14c2279f384818b454209409f2e8bb3e4d58a5960b8601baac0563dd85b5199a`.
- **Source snapshot.** Every source was read with `git show fd539e15:<path>`.
  - `origin/main` is now `cac5d264` (#1212, "correct SM ring degree bounds"), checked with
    `git ls-remote`, which writes no ref.
  - `git diff fd539e15 cac5d264` touches only `papers/SM.{md,tex,pdf}`. The `SM.md` change is
    SM:112's degree-bound sentence, edited in place, so no `SM.md` line moves. `SM.tex` gains one
    line within :781–794; the one `SM.tex` line cited (:717) is before it.
  - Substratum, Structure, Main, ch02, FULL (`.md` and `.tex`) and `verification/` have identical
    blobs at both commits. No clause cited or proposed for correction changed. SM:112 is cited
    only for G_SM's non-affinity and its x_{i+1} = 0 switch, which are unchanged.
  - Recorded in the r4 header.
- **Reviewer's probe.** `review/rv3_link_affinity.py` (`a260d6dd…536f`) was re-run with
  `python3 -I` into `reassess/rerun-1049-r4/`: exit 0, about 17 s, output byte-identical
  (`49e4b993…4a28`).
- **Writes.** No git or GitHub write and no manuscript edit. No `--depth`, `gc` or `prune`. The
  working tree is clean.

## Blockers

### R3-B1: the recovery's basis is misattributed in the headline

**Verified against.** G1 and §7 item 7 of r3 itself; E3 (non-additive link sum); kernel
`linkSubstratum_A5` (`M i j : V →+ V`); Sub:100, :102, :104, :220; ch02:84 = FULL:718.

**Decision.** Accepted. The headline is now "not refuted; conditionally recovered", with two results
stated separately at every listed site:
- **Withdrawal (shown).** Every written A6 interface is a link sum with linear links. P1's rules are
  not link sums, so they are not candidate rules at the A1–A6 sites, and the P1-based narrowings are
  withdrawn.
- **Recovery of the route "gauge ⇒ base-point form ⇒ affine" (conditional on GA7-α).** It needs
  non-additive link maps, which the corpus never states. Under the written, additive interface the
  rule is linear by type, the gauge does no work, and the "precisely to the extent" and "exactly
  when" clauses hold one way only.

**Changes.**
- **§0 item 2.** Rewritten under the new headline, with the two results as separate bullets plus
  the G2 bullet.
- **§0 item 1.** The header reads "within the link-sum class with non-additive link maps (GA7-α)".
  The sub-bullet "The link sum is the form in which the corpus writes A6's interface" now reads "The
  corpus writes A6's interface as a link sum only with additive links; the class with non-additive
  link maps (GA7-α) is not stated in the corpus". The r3 sentence was the same fusion as item 2.
- **§2.1 *Consequence* (r3 :266–268).** "Among link-sum rules, the form in which the corpus writes
  A6's interface" now reads "Among link-sum rules with link maps not assumed additive (GA7-α, not
  stated in the corpus)". A sentence is added saying that the written interface is additive and
  that gauge is idle there (G1).
- **§2.1 *Consequence*, A1–A6 bullet.** "The claim is recovered under A6's written interface" now
  reads "not refuted …; its route through gauge is recovered only conditionally, on GA7-α".
- **§2.1, "How the site claims fare".** "With (R-uni) and A6's link-sum interface, Sub:220 holds"
  is now split: as written, Sub:220's "exactly when" holds one way (G1); under GA7-α it holds both
  ways for q ≥ 3.
- **§2.1 (R-uni) d = 2, 3 bullet.** "Among link-sum rules" becomes "with link maps not assumed
  additive (GA7-α)".
- **§2.3 per-site table.**
  - Sub:100: "The claim is recovered" now reads "Not refuted; its gauge route is recovered
    conditionally on GA7-α".
  - Sub:104: "Recovered … is the recovered one" now reads "Not refuted. Its route … holds
    conditionally on GA7-α. Under the written interface the conclusion holds by typing and gauge is
    idle (G1)".
  - Sub:220: "Recovered" now reads "Not refuted; its gauge route is recovered conditionally on
    GA7-α".
  - Structure:259: "Recovered under A6" now reads "Not refuted under A6; its gauge route is
    conditional on GA7-α".
- **§2.4 item 1, E3 corollary.** "In the link-sum class" becomes "In the link-sum class with link
  maps not assumed additive (GA7-α)".
- **§2.4 item 2, bold conclusion.** Replaced with REVIEW-1049-r3's suggested wording, adapted
  minimally. The r3 text "recoverable and is not an overstatement" is gone.
- **§4 O-A.** The first-level link-sum bullet carries "(GA7-α)". The A1–A6 sub-bullet now reads:
  "not refuted …; the 'partly derived' route through gauge is recovered only conditionally, on
  GA7-α … Under the written, additive interface the affine part holds by typing and the attribution
  to gauge is idle (G1)".
- **§4 O-F.** "Structure:259 is recovered under A6" now reads "is not refuted under A6". This is a
  necessary consequence that the review did not list.
- **§6 Q2.** "P1's class is excluded and the affine claim at the A1–A6 sites holds" now reads "…
  is excluded and is no counterexample at the A1–A6 sites".
- **§7 F-9.** "POSITIVE … under A6's written interface" now reads "**POSITIVE under GA7-α** (not
  stated in the corpus) for the A1–A6 sites' route through gauge. Under the written interface the
  relevant results are E2 and the kernel's typing, with the gauge principle idle (G1)". It adds
  that the withdrawal does not depend on GA7-α.
- **Re-grep.** `grep -n -i "recover"` over r4 leaves no unconditional "recovered" at a site. The
  surviving hits are the section titles, E3's name, G3 ("Sites not recovered"), pressure-test
  item 7, the conditional forms above, and one QP context row. "not an overstatement" survives only
  at Structure:301, where it is correct and unrelated.

### R3-B2: a false clause missed in Sub:272's second sentence

**Verified against.** Sub:272 at fd539e15. The clause is at Substratum.tex:1733–1735 (r3's mirror
range :1736–1739 had omitted it). Also P1 [X: P1; rv_p1 A–C; rv3 V5].

**Decision.** Accepted. F6 is added and scoped like F1–F5. Of the review's two V1 options, **(α)**
is taken.

**Changes.**
- **§2.3.1 "What is false", new F6.** The clause needs "unobservable ⇒ affine".
  - Under (R-uni) it is false for d = 2, 3 (P1).
  - Under (R-rel) it is false at every d.
  - It is true only under (R-site), or under GA7-α, which Sub:272 does not state.
  - After the second sentence's V1, it would also no longer connect to that sentence's conclusion.
- **§2.3.1, new block "Sub:272, second sentence, opening clause (F6)".**
  - **V1:** "the affine restriction" becomes "the principle itself".
  - **V2:** V1 plus the clause "which for $d=2,3$ would not by itself make the affine restriction
    unconditional". This is a new negative claim, needing P1's proof on `main`, as for the other
    V2 texts.
- **§2.3.1, new block "Which reading each sentence of the corrected paragraph uses".**
  - Sentence 1 (V1) uses the base-point form.
  - Sentence 2 (V1) uses uniform symmetries.
  - Sentence 3 is about the principle as stated.
  - Each sentence names its form in its own text, so no further paper text is proposed.
- **§2.3.1 "Why V1 is a correction".** One line for F6's change of subject.
- **Propagated to:**
  - the §2.3 table's Sub:272 row ("four clauses are false (F1–F3, F6)", with the `.tex` range
    :1733–1739);
  - the §2.1 `.tex` list;
  - §0 item 3;
  - §7 F-8 (a new bullet).

**Partial refusal: option (β).** Option (β) keeps "the affine restriction" and reads
"unobservability" in base-point form, and it is not taken. The sentence's conclusion would then have
to be in base-point form too, and "states that differ only in absolute amplitude" is not a
base-point notion. Option (α) is the smaller change, and it agrees with the paragraph's own last
sentence ("an operational input …, not a theorem"). The reason is stated in §2.3.1.

## Nits

| Nit | Decision | Change in r4 |
|---|---|---|
| N1 | Accepted | §2.3.1 inference row. Under (a): "the inference is valid, but the argument is unsound: its premise is false". Under (b): "the inference is invalid". F-8's heading and bullets, §0 item 3 and the §2.1 (R-site) bullet now say "argument … under (b) the inference is invalid; under (a) its premise is false" |
| N2 | Accepted | §2.3.1 first-sentence table, (R-uni) cell: "false. At odd q … incomparable … At q = 2 the comparative is true …; there only the 'excludes' clause fails [X: rv3 V6; r4 C2]". F1 is restated the same way. The link-sum remark under the table is split by odd q and q = 2. "Each reading falsifies at least one clause" still holds, because F2 fails at q = 2 (P1's q = 2 rule) |
| N3 | Accepted | §2.4 G4, new bullet. E3 is proved for K = 1. On (ℤ/q)^K it holds with shifts by every c ∈ A. Diagonal shifts do not suffice: the witness ((x₁ − x₂)², 0) at q = 3 [A; X: rv3 V2; r4 C3]. Which shifts the gauge includes on a K-component carrier is not settled. The K scope is also carried in §0 item 1 and F-9 |
| N4 | Accepted | Sub:100 and Sub:220 rows, §2.4 G1, and §2.1 "How the site claims fare". "Both directions under GA7-α" now reads "for q ≥ 3". At q = 2 every map ℤ/2 → ℤ/2 is affine, so Σ x_j² = Σ x_j and the clauses hold one way [A; X: rv3 V1; r4 C1] |
| N5 | Accepted | §2.3.1, second-sentence V1. "so the inference is valid" is replaced by: valid with "unobservable" read as dynamical indistinguishability; in the observer-resolution reading the sentence sets up, it also needs the open step "distinguished by the dynamics ⇒ resolvable", which the Status note flags |
| N6 | Accepted, with one deviation (below) | §2.3.1 Sub:274: new **V1′** (subject-changing), with part (ii) as in V1. A note that "more primitive and better-motivated" (Substratum.tex:1776) and "more primitive and more defensible place" (:1781–1783) attach to a condition equivalent to affinity under V1 and V1′. §2.3.1 Sub:272 first-sentence V1: one sentence saying its remaining reason is true only because the base-point principle is affinity restated. §6 Q1(d) raises the hollowness question for all three passages and offers V1′ |
| N7 | Accepted | §2.4 item 2 Assessment, new bullet. The vacuous-conditional reading of A6 is not the written one: Sub:102 and ch02:86 = FULL:720 assert "the coupling is link-valued data on which the transformations act" (verified byte-for-byte in all three). So "outside A6's domain" does not mean "satisfies A6" |
| N8 | Accepted, with corrected coordinates (below) | §2.1 `.tex` list and §2.3 table. Substratum.tex:743–752 (Sub:100's parenthetical, with "restricts the update to an affine one" at :744); :1733–1739 (Sub:272, second sentence); :1768–1773 (Sub:274's F4 sentence ends at :1773). Structure.tex:980–982, :1144–1145 and :1269–1271 |
| N9 | Accepted | §2.4 item 2. The written forms are split into the substratum level (kernel `linkF`, with `linkRule` and `linkSubstratum` at `Fin 6 → ZMod q`) and prose (SM:116; SM:312–314, quoted as "on the observer-level branch …, not the ℤ/qℤ alphabet of the substratum"). The GA7-cov row is updated to match |

### Deviations and refusals

1. **N8 coordinates.**
   - Sub:100's parenthetical begins at Substratum.tex:743 ("(Amplitude-scale gauge invariance ---
     that the field-value scale is"). Its claim "restricts the update to an affine one" is at :744,
     the line the review gives. r4 records :743–752, with the claim at :744.
   - For Structure:301 the review says ":1273 is the next sentence". At fd539e15 the next
     sentence, "The hypothesis adds …", begins at the end of :1271. r4 says so.
2. **N6: no replacement text for the hollow passages.** "Stated operationally it is *not*
   viciously circular", "more primitive and better-motivated" and "more primitive and more
   defensible place" are evaluative. After V1 or V1′ they are not mathematically false. Rewording
   or removing them is an editorial decision for the owner, so r4 raises it in §6 Q1(d) and
   proposes no text for them.
3. **N6: V1′ wording.** V1′ adds "for $q \ge 4$" to the review's example. Otherwise it would restate
   "a proper subgroup of all permutations", which is false at q = 2, 3 (F7 below).
4. **R3-B2: option (α), not (β).** Reason given above.

## Additions beyond the review

- **F7 (scope; elementary, not a P1 finding).**
  - Sub:274 (Substratum.tex:1771–1772) and SM:96 (SM.tex:717) call the additive-automorphism group
    x ↦ λx + c on ℤ/q "a proper subgroup of all permutations".
  - That group has q·φ(q) elements, which equals q! exactly when q ≤ 3. So the clause is false at
    q = 2, 3, and SM:96's "A nonlinear relabelling …" is vacuous there [A; X: r4 C4].
  - On the kernel's (ℤ/q)⁶ alphabet the affine group is proper at every q.
  - Qualifier-only correction: "for $q \ge 4$". Found while drafting N6's V1′.
  - It bears on no other finding. It is raised in §0 item 3 and §6 Q1(a), as a question of whether
    to record it with the Sub:272/274 corrections or separately.
  - `git grep "proper subgroup"` over `papers/` and `book/` at fd539e15 finds SM.md:96, SM.tex:717,
    Substratum.md:274 and Substratum.tex:1771, and one unrelated Main:672 hit. No book passage
    carries it.
- **Header.** Revision r4; r3 kept at `r3/`; the owner direction is applied to F6; the source-snapshot
  note for `cac5d264`.
- **§8.** r4 paper items, the r4 probe, the rv3 re-run, and r4 reading coverage.

## Probe added

`probes/r4_scope_checks.py`, sha256
`23c659f42756c5d8ab710bd64eedf8f5af73ba6c134d1beaa9099cca9df8b991`. Output
`probes/r4_scope_checks.out`, `d5bc1d8d5cfe29fe6e819aeff36f04784efe4aa217c580726158f2d90c63492c`.
ALL PASS (31 checks), exit 0, under 1 s, run with `python3 -I`.

It is labelled an exact generic check: modular arithmetic on generic local functions and one-step
identities. It imports only `itertools`, `math` and `sys`. It imports nothing from `probes/` or
`review/`, iterates no dynamics, computes no observable and instantiates no OI mechanism.

- **C1 (N4).** At q = 2 every map is affine and Σ x_j² = Σ x_j. At q = 3, 5, Σ x_j² is a non-affine
  link sum excluded by uniform shift gauge. Control: Σ x_j.
- **C2 (N2).** At q = 2, all 128 affine rules satisfy the κ-general form, and they satisfy κ = 2 iff
  Σa is even. P1's q = 2 rule satisfies the κ = 2 form and is not affine. Countercontrol: 2Σx + 1 at
  q = 3. Control: 2Σx.
- **C3 (N3).** The diagonal-shift witness ((x₁ − x₂)², 0) at q = 3, K = 2. Control: an affine map.
- **C4 (F7).** The affine permutations of ℤ/q number q·φ(q), and they are all of S_q exactly when
  q ≤ 3, for q = 2–7.

## Not changed

- §2.2, §3, §4 O-B to O-E and O-G, §5, and §6 Q3–Q5.
- §7 F-1 to F-7 and F-10.
- Pressure-test items 1–7.

The review found no defect in any of these, and none is affected by the changes above.
