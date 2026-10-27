## Review of PR #957 (head `b25dcfc4`, base `55e3217b`). Verdict: ACCEPT WITH CHANGES

The core correction is right. I checked every mathematical claim in the new §3.5 independently and found no errors, including the sign and orientation conventions. The boxed equivalence and the "same fact" paragraph are gone, with no remnants anywhere in papers/, book/ or verification/. The corrected lemma states only the direction that is proved, and the time-orientation point stays open, which is correct.

Four required changes remain. Three are small overclaims or stale scope statements, and one is a stale dependent in ch19 and its FULL mirror.

Setup and replay:
- **Disk:** 23 GB free.
- **Worktree:** a fresh detached worktree at `b25dcfc4`, removed after the review.
- **Audit script:** `cubic_counterexample.py` from `audit/intro-corpus-20261026` (`9ff27719`), replayed with `python3 -I -B` from an empty directory.
  - It exits 0 and prints "ALL CONTROLS GREEN".
  - Its output is byte-identical to the committed `cubic_counterexample.out`.

### Mathematics (task item 1): all verified
- **Λn = ±n.** A Lorentz Λ that maps the parallel family n^⊥+c to itself preserves n^⊥, hence (n^⊥)^⊥ = ℝn. Then η(Λn,Λn) = η(n,n) gives λ² = 1.
- **Stab(ℝn) ≅ O(3)×O(1).** This is a direct product: O(n^⊥) ≅ O(3) times ±1 on ℝn.
- **Orthochronous elements fix n.** An orthochronous Λ with Λn = ±n, n future-directed, has Λn = n.
- **Little group.** The stabilizer of a timelike vector is O(n^⊥) ≅ O(3); it includes parity and lies inside O⁺(3,1).
- **Boosts are excluded.** A boost relative to n maps n to γ(n+v) ≠ ±n. More generally, a pure boost relative to any frame fixes only a spacelike 2-plane, so it moves every timelike vector. The lemma's "boosts, which move n" therefore holds without qualification.
- **Maximal compact subgroups.**
  - In O(3,1) they are the conjugates of O(3)×O(1), each preserving exactly one timelike line.
  - In O⁺(3,1) they are the conjugates of O(3). N(O(3)) = O(3), because a normalizing element must send n to a vector fixed by all of O(3) and is orthochronous. This gives the bijection with O⁺/O(3) = H³, each subgroup fixing exactly one future-directed unit timelike vector.
  - The base text's "maximal compact subgroup (isomorphic to O(3))" of O(3,1) was wrong. The PR fixes it.
- **Cubic kernel.** The kernel is S = {n ± e_i}, with invariance meaning ΛS = S. The enumeration over all 360 basis images is exhaustive, since S spans ℝ⁴. G_T is the 48 signed permutations (O_h) on the spatial block, and every element fixes n. −1 ∈ O_h, so the group fixes no nonzero spatial vector.

### The script's controls (critical read)
They are non-vacuous:
- The rational (3/5, 4/5) rotation shows that Stab(n) is not contained in G_T.
- The time-symmetric set S∪(−S) gives |G| = 96 = |O_h×O(1)| and contains a Λ with Λn = −n. This tests the enumerator on a second group of a different order and exercises the ± branch.
- The boost countercontrol is valid but logically implied by the other checks.

Minor weaknesses:
- The "fixed subspace is ℝn" check only checks that parity has first row (1,0,0,0). Together with the all-fix-n check, that suffices logically.
- Block-diagonality is implicit (Lorentz plus fixing n), not checked.
- There is no control with a kernel that has smaller symmetry, such as unequal weights.

Is invariance-of-a-step-kernel a fair instance of the lemma's hypotheses?
- It is a fair witness that the inference "fixes n ⇒ invariance" is invalid. The proof uses the hypotheses only through n, and the step kernel is a map whose defining data include n.
- It is **not** an instance of "the coarse-graining map induced by a horizon partition". The script's README says so correctly, and Main must not use the kernel for more than that (see Finding 1).

### Owner questions
**(a) Is every substantive claim supported by its stated evidence and assumptions?** Not quite. Findings 1, 3 and 4 are the exceptions:
- one witness-to-universal overclaim;
- one attribution ("set by the substratum constitution") that SM §3.1 contradicts;
- one unstated premise in the proof's first step.

Everything else is supported.

**(b) Is any established result unnecessarily weakened?**
- **The ± form: no.** The corpus does not establish that T fixes a time orientation. Substratum §5.4 (:359) says the choice of "future" is "imposed by the observer, not derived", with φ ↔ φ⁻¹ gauge-equivalent. GR :68–70 derives time-reversed detailed balance from microreversibility, which is positive evidence against assuming an orientation.
- **The corollary: no (with one exception).** It keeps the rest frame, the absence of a partition-selected spatial axis, and the boost/rotation inequivalence, so it states everything that survives. The one understatement is Finding 6, which the PR did not introduce.

### Findings

**1. Main.md:666, Converse paragraph (required).**
- **Current text:** "rest-frame selection is compatible with any rotational invariance group inside $O(3)$, as the cubic step kernel shows."
- **Problem:** This goes from one witness to a universal claim. One kernel shows that rest-frame selection does not force O(3). It does not show that every subgroup is realized.
- **Evidence:** In the step-kernel class, SO(3) cannot be realized at all. Any SO(3)-invariant measure on ℝ³ is radial, hence also −I-invariant. The kernel is also not shown to be an instance of the horizon-partition hypotheses.
- **Proposed replacement:** "rest-frame selection does not force the full little group: the cubic step kernel selects $n$ with invariance group $O_h$, a proper subgroup of $O(3)$."

**2. ch19-open-problems.md:240 and :242, mirrored at FULL.md:5400 and :5402 (required, §A.25).** These are stale dependents of the old "T is O(3)-invariant" reading.
- **:240, current text:** "the map touches what distinguishes time from space (boosts), and is silent on what distinguishes one spatial direction from another (rotations)."
- **:242, current text:** "the rest-frame lemma's map is silent on spatial axes."
- **Problem:** Under the corrected lemma, T may carry the lattice axes (for example O_h); only the rest-frame selection is silent. The PR made exactly this switch from "map" to "partition" in Main's corollary, and in the parenthetical of the same ch19 paragraph, but not in these sentences.
- **Proposed replacement for :240:** "…the rest-frame selection touches what distinguishes time from space (boosts) and is silent on what distinguishes one spatial direction from another (rotations)."
- **Proposed replacement for :242:** "…that the rest-frame selection of the lemma is silent on spatial axes."
- **Mirror:** Apply the same edits to FULL.md:5400 and :5402.
- **Optional, same family:** :246 "structurally silent on space and rotation".
- **Mirror check:** ch19:240/242/246/248 and FULL:5400/5402/5406/5408 are byte-identical now (checked with cmp).

**3. Main.md:660, last sentence of the lemma, and Substratum.md:329 (required, minor).**
- **Current text:** "Which transformations fixing $n$ are invariances of $T$ is not determined by the partition; it is set by the substratum constitution."
- **Problem:** SM.md:136, and ch19:228 and :248, make the partition's own spatial shape one of three ingredients of O_h invariance: "If the microscopic action, the measure, and the partition are each exactly $O_h$-invariant…". They also list an O(ε/R_H) observer-position boundary anisotropy that the partition induces. Attributing the group to the constitution alone contradicts them. What is proved is that n does not determine it.
- **Proposed replacement:** "Which transformations fixing $n$ are invariances of $T$ is not fixed by $n$; it depends on the substratum dynamics and on the lattice geometry of the partition."
- **Corollary :664, optional:** "whatever spatial axes it carries come from the substratum constitution" could be adjusted the same way.
- **Substratum, same issue:** In "compact rotations about that worldline are not excluded by the partition", "by the partition's rest-frame data" would be more accurate.

**4. Main.md:662, first step of the proof (required, small; the gap predates this PR).**
- **Current text:** "$\Lambda$ is an invariance of $T$ only if it preserves the data defining $T$, hence only if it maps the foliation to itself".
- **Problem:** An invariance of a map need not preserve the data used to construct it. If T does not depend on the foliation, for example a trivial T, every boost is an invariance. So the boost exclusion, which is everything GR uses, rests on the unstated premise that T determines its foliation.
- **Proposed fix:** Add to the lemma's hypotheses: "…and suppose $T$ determines this foliation, so that any $\Lambda$ leaving $T$ invariant maps the foliation to itself."
- **Why this is permitted:** It makes explicit an assumption the forward direction already uses. It does not rescue the removed equivalence.

**5. Substratum.md:329 (optional, recommended).**
- **Current text:** "The framework does not derive that structure; it exhibits it as the necessary shadow of worldline-centered observation".
- **Problem:** The FRW symmetry structure includes isotropy, which the same sentence now says is only "not broken by the partition" and enters as input. "Necessary shadow" overstates this.
- **Proposed replacement:** "…it exhibits the partition's breaking pattern as compatible with that structure: worldline-centered observation breaks no more symmetry than an FRW cosmology does."

**6. Main.md:664, corollary (optional; text the PR did not change).**
- **Current text:** "where the cubic point group protects it only at tree level".
- **Problem:** This understates SM §3.1 (:136). There, O_h invariance holds to all orders, conditional on exact O_h invariance of the action, measure and partition, and a numerical check finds the E_g coefficient zero within errors at the 2×10⁻⁵ level.
- **Proposed replacement:** "…protects it at tree level, and to all orders conditional on exact $O_h$ invariance of the action, measure and partition ([SM §3.1])."

**7. Main.md:662 and :666, wording (optional).**
- **"fixes $n$":** "A nearest-neighbour step kernel… fixes $n$" should read "selects $n$ (its invariance group fixes $n$ and no other direction)".
- **"which fixes no spatial vector":** should read "…no nonzero spatial vector".
- **"moving a site by $n \pm e_i$":** should read "with spacetime increments $n \pm e_i$".
- **Possible strengthening of the Converse:** Add "combined with the lemma, such a group equals $\mathrm{Stab}(n)$ for the horizon's $n$". This follows by maximality.
- **"The statement is one-way":** could be made precise as "its converse fails, as the cubic step kernel shows".

**8. Voice (optional).**
- I scanned the added lines with the §A.32/§A.33 battery: caps-emphasis regex, history phrases, and reader-instruction and meta phrases. There were no hits in newly written words.
- Two old phrases sit on lines the PR touched, so a line-based added-lines scan will flag them: "a caution against over-reading them" (:668 heading) and "Two honest qualifications" (:670).
- Also old: :668 identifies C2 with "the same feature that selects the simultaneity surface", with no formal map.

**9. Ledger (optional).**
- The re-affirmed fingerprints match the current census exactly:
  - `MAIN:L-rest-frame-selection` 523dc521032a4f76;
  - `MAIN:C-boost-rotation-inequivalence` 806a149b266fbc51.
- They remain GAP / "not formalized", which is correct. The Converse is not a census statement, as at base.
- The entries' `line` fields (644/648) are stale against 660/664. This was already so at base and is not enforced.

### Dependencies (task item 4)
- **GR.md:641 and :653** cite [Main §3.5] only for the boost-sector item ("local-boost-invariance…"; "identical to the open Lorentz-sector boost item"). They need only the boost exclusion, which survives.
- **SM.md:134** ("aligned to the cosmic rest frame") and **SM.md:1418** ("selects a timelike direction but no spatial one") are consistent.
- **SM.md:136** relies on O_h, not O(3), and is consistent with the corrected lemma. It is the source of Finding 3.
- **Explainer.md** has no dependent sites.
- No other site anywhere in the corpus still asserts the removed equality. The only stale sites are the ch19/FULL sentences in Finding 2.

### §A.34
No displayed equivalence remains in §3.5. The only "exactly" is "exactly the octahedral group", which is not an equivalence. The Converse is one-way and does not need a second witness.

### Gate and artifacts
- **Release gate:** `python3 tools/release_gate.py` passes every step except `lean-axioms`, which fails because lake is missing locally, as expected.
- **.tex files:** Regenerated with the build.sh recipe, including the source-sha256 footer, `papers/Main.tex`, `papers/Substratum.tex` and `book/The-Incompleteness-of-Observation-FULL.tex` are byte-identical to the committed files.
- **PDFs:** Their text contains the new wording and none of the removed equivalence or "same fact" text. Page counts are 96, 53 and 557.

### Files
- `/home/user/incompleteness/papers/Main.md` (:660–670)
- `/home/user/incompleteness/papers/Substratum.md` (:329)
- `/home/user/incompleteness/book/ch19-open-problems.md` (:240, :242)
- `/home/user/incompleteness/book/The-Incompleteness-of-Observation-FULL.md` (:5400, :5402)
- `/home/user/incompleteness/papers/SM.md` (:136)

All line numbers refer to head `b25dcfc4`.
