# Review of U4-CALC r1 (hand calculations for U4, item 2b)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/U4-CALC-r1.md`
at PR #1294 head `f86dd1f791774f68237c8b82ef810855f14dd6d8` (introduced by that commit).
**Reviewer.** Independent, non-author. Read-only: no repository file, commit, push, Issue or status
was changed. **Method.** Every proof and instance below was re-derived by hand (exact algebra over
`ℤ/q`, matrix identities, path counting). No program was run to compute or enumerate anything; git
was used only to read sources and to check blob ids.
**Authorization.** Issue #1169 c.6891511297, item (2b) (paper-only).
**Sources.** `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`: MR★ (blob `45af1678`), PREREG
(blob `c36fb14b`), `papers/Main.md` (blob `0db17597`), OAC (blob `d5c49365`). Branch drafts S3-U4-r1,
S3-U1-r5, S3-PLAN-r9, VERIFY-SL3-CC-r2, U4-SOURCES-r1. The five branch blob ids the note cites match
both `e18126ee` and `f86dd1f7`. The three `main` blob ids match. Spot-checked lines: MR★:464–466,
470–477, 491–496, 642; Main:54, Main:682; OAC:132–134; PREREG:485–487. All say what the note quotes.

## Verdict: ACCEPT WITH CHANGES

The mathematics is correct. Theorem 1, Theorem 1′, Propositions 1.4–1.6, Instances 1.1–1.3,
Lemmas 2.1–2.4, Theorem 2, Propositions 2.5–2.8 and the controls C1-2 to C1-4, C1-6 and C2-1, C2-3 to
C2-5 check by hand. No numerical argument stands in for an exact one. Nothing blocks. The required
changes restore hypotheses that the summaries drop (`d = 3`, a prime-power `q`, S-L2 [NP]),
correct one cross-reference and one remaining-step scope, narrow one finding's wording, add one
missing converse (§A.34), and relabel three controls that cannot fail.

***

## Findings

### Blocking

None.

### Required

**1. Proposition 1.5 cites the wrong instance for its failed converse.** The note says other regions
can fill `K_t` without self-masking, "(Instance 1.3 below)". Instance 1.3 is Instance 1.1 at `t = 1`,
where the marker self-masks (Proposition 1.4), so it is not an example. The example is control C1-6.
Hand check: with `e_1` moved to the environment, `y_{e_1}` enters `u_1(0)`. It does not enter
`u_2(0)`, because no neighbour of `0` neighbours `e_1` on the cubic lattice. `x_{e_1}` enters
`u_2(0)` with coefficient `−1`. Together with the marker's `(−x_0, 5y_0)` this spans `𝐑²` while the
marker alone does not when `5 | q`. *Change:* cite C1-6, the variant of Instance 1.2.

**2. The `d = 3` scope of Proposition 2.5(b) is dropped in CALC-F3 and in §3's S-L3 bullet.** Both
say "a torus with an even side `≥ 4`". The proof uses `Av = (2d − 4)v = 2v`, so `M_2` is unipotent,
which holds only for `d = 3`. Hand check of what goes wrong elsewhere:
- for `d = 2`, the same `v` gives `Av = 0`, `M_0 = [[0,1],[−1,0]]`, and `M_0² = −I`;
- for `d = 1`, `Av = −2v`, and `M_{−2} = −I + N′` with `N′ = [[1,1],[−1,−1]]` and `N′² = 0`. So
  `M_{−2}^t = (−1)^t (I − tN′)`, which equals `−I` at odd `t ≡ 0 (mod q)`, for example `t = q` with
  `q` odd.

The `v`-mode therefore excludes no `γ ≠ 1` outside `d = 3`. §2.8 says "native torus", which is
correct. *Change:* write "native cubic torus (`d = 3`) with an even side `≥ 4`" in CALC-F3 and §3.
(Optional finding O3 gives a separate exclusion for rings.)

**3. The A-cur candidate ticks need a prime-power `q`; §2.8 drops the hypothesis.** Proposition 2.7
assumes `q = p^k`. The hypothesis is needed. Over `ℤ/6`, `β = 3`, `γ = 4` satisfy `βγ ≡ 0` and
`β² + γ² = 25 ≡ 1`, with neither of them `0`. So the mixed CRT case gives background-free ticks that
are neither `N − 1` nor `N/2 − 1, N/2` (R-3 records this). §2.8's sentence "Under A-cur the
candidates are `N/2 − 1`, `N/2` (scalar case) and `N − 1`" drops the hypothesis.

Also, for an A-cur return, what must be aperiodic is the current-slice (`y_Σ`) marginal of `λ`, not
`λ` on `S_Σ`. The two agree for point carriers, which are the case used. *Change:* add "`q` a prime
power" to §2.8, and state the A-cur aperiodicity hypothesis on the `y_Σ`-marginal in Proposition 2.7.

**4. R-1's parenthesis "(every odd `q`)" misstates the open case.** A unit `γ ≠ 1` with `γ² = 1`
exists for every `q ≥ 3`, since `γ = −1 ≠ 1`; for example `q = 4` and `q = 8` have one. With all
sides odd, Proposition 2.5 covers only `q = 2` (part (a)). *Change:* R-1 is the case "all sides
odd, `q ≥ 3`".

**5. Theorem 2(c)'s negative rests on S-L2 [NP], and the conclusions do not carry it.** "Some
available `φ^n`" uses H-avail, that the available transformations are the time shifts (S-L2,
labelled [NP] in §0). Parts (a), (b) and (d) are statements about laws at ticks and do not need it;
(c), the "no available operation restores" statement, does.
- §2.8's answer, CALC-F3 and §3's SNR-1 bullet name only the assumed carrier preparation as the
  negative's reliance.
- Every condition must reach the conclusion.

*Change:* add "given S-L2 [NP] (H-avail)" to Theorem 2(c), §2.8, CALC-F3 and the SNR-1 bullet.

**6. CALC-F2's last clause overstates.** "The PLAN §8.4 masking sentence holds at `t ≤ 1` only"
reads as "fails at every `t ≥ 2`". The note's own results contradict that reading. Masking is
complete at `t ≥ 2` in:
- Instance 1.1 under A-cur at `t = 2`;
- Instance 1.1 over `ℤ/2` at `t = 3`;
- Instance 1.2 with `5 ∤ q`;
- C1-6.

§3's wording ("exact at `t ≤ 1` and is not a general fact") is correct. *Change:* "holds in every
geometry at `t ≤ 1`; at `t ≥ 2` it holds iff `K_t = R_A`, which fails in Instances 1.1 and 1.2".
"Records" in CALC-F2 should read "holds a single-tick (R1) record of the carrier functional `q_t`".
The perfect *path* record of a point-path pair also uses the assumed point preparation of the
carrier (H-μ, U1 C-PREP).

**7. Three controls cannot fail, and the table's heading says each could have.**
- **C1-1** (`t = 0`): `K_0 = R_A` holds by definition once `A ⊆ Σ^c`.
- **C2-2** (`t = N`): `φ^N = id` holds by definition of `N`.
- **C1-5** (Instance 1.2 with `5 ∤ q`) reads the same expression `5y_0 + f` with `5` a unit, so it is
  not independent of the instance it checks.

C1-3 and C1-4 are genuine, since direct expansion and the dual pulse are independent computations;
C1-6, C2-1 and C2-3 to C2-5 are genuine. *Change:* relabel C1-1, C2-2 and C1-5 as consistency
checks, and add independent checks. The reviewer did the following two by hand, and the note may use
them:
- **Dual of Instance 1.2** (an independent check of the `5 | q` record). A-reg covectors on site `0`
  annihilating `K_2 = image of (x_0, y_0) ↦ (−x_0, 5y_0)` have `c₁ = 0` and `5c₂ = 0`. So
  `α_2 = 0` and `α_1 = −c₂δ_0`. Running the recurrence backwards gives:
  - `α_0 = Aα_1 − α_2 = −c₂ Σ_{j∼0} δ_j`;
  - `α_{−1} = Aα_0 − α_1 = −c₂(5δ_0 + Σ δ_{±2e_c} + 2Σ δ_{±e_c±e_{c′}})`.

  When `5c₂ = 0`, both are supported in `Σ`. The value `α_0·x − α_{−1}·y` equals `c₂ f(s_Σ)`, which
  agrees with the direct expansion. With `5` a unit, `c₂ = 0` and nothing is recorded.
- **Dual of C1-4** (the prediction was stated, not computed). On `ℤ/4` with `Σ = {3, 0}` and
  `A = {1, 2}`, write `α_0 = aδ_3 + bδ_0` and `α_{−1} = cδ_3 + eδ_0`. Support of `α_1` in `A` forces
  `e = a` and `c = b`. Then `α_1 = aδ_2 + bδ_1` and `α_2 = aδ_1 + bδ_2`. So `𝒟_2 ≅ 𝐑²` under A-reg,
  in agreement with the quotient `𝐑²`, and `α_2 = 0` forces `a = b = 0` under A-cur.

**8. Two directional gaps (§A.34).**
- **(a)** Proposition 2.7 is an "iff", and its proof gives only "background-free ⇒ `φ^t` or `φ^{t+1}`
  scalar". The converse takes one line: if `φ^t = γ·id`, the current slice is `γy`; if
  `φ^{t+1} = γ·id`, then `φ^t = γφ^{−1}` and the current slice is `γx`. Both are free of
  background. *Change:* write it.
- **(b)** Proposition 2.8(ii) writes "At a J-return tick (`B_t = 0`)". J-return ⇒ `B_t = 0` is
  Theorem 2(a), which needs `λ` aperiodic and `Per(Σ) = {0}`. The step `B_t = 0 ⇒ K^D_t = R_D` needs
  neither: `φ^t` maps `S_{Σ^c}` injectively into itself, hence onto it. *Change:* cite Theorem 2(a)
  and its hypotheses for "a J-return and visibility at `D` exclude each other".

**9. §3 asserts a PLAN revision that the note does not make.** "The sentence is replaced by the
criterion of Theorem 1" is in an [A-inf] section of a note that changes no file, and owner question
1 asks exactly this. *Change:* "would be replaced, pending owner question 1".

**10. Theorem 2(b)'s T0 clause.** "T0's witness, if any, returns" makes the coincidence in (b) a
coincidence with T3's equivalence clause. On the record T0 is not shown on K1 (U4 §3.2; MR★ σ1:
"That T0 fails is not claimed"). *Change:* say that (b) identifies J-return and full return with the
§5.3 equivalence part of T3's unconditional sub-label, and that T0's witness clause holds only where
a witness exists.

### Optional

**O1. Notation.** `A` names both the adjacency operator and the marker region, for example in
"`(A y_A)|_A`" (Proposition 1.4) and "`A = Aᵀ`" (Theorem 1(d)). The text can be parsed, but renaming
the region (for example `𝒜`) removes the ambiguity.

**O2. "Smallest nontrivial"** (Instance 1.1) is an unproved superlative. Remove it or justify it.

**O3. Rings are excluded for every `L` and `q`.** On any ring (`d = 1`, `L ≥ 3`) the constant vector
`v = 1` has `Av = 2v`, so `φ` acts on `{(α1, β1)}` by the same unipotent `M_2` as in Proposition
2.5(b), and every scalar power is `I`. So `T_γ = Nℤ` on every ring. Instance 1.1's "no J-return
below recurrence" then holds for every `q`, not only `ℤ/2`. In `d = 3` the constant mode gives
`M_6`, which does not exclude: over `ℤ/5`, `6 ≡ 1` and `M_1³ = −I`.

**O4. CALC-F5's class.** POSITIVE (§A.31) means that an inheritance or assumption is validated.
CALC-F5 limits the reach of CALC-F3's negative (it bears on carrier transport in a uniform
background, not on erasure), which fits ELABORATING, or NEW as a scope limitation.

**O5. AW-1 can name the source of the tension.** MR★ σ6 ("lies beyond any budget that R2 admits")
and PLAN's S-L3 scope ("the global wait `φ^{N−1}` lies beyond it") concern the *operation*
`φ^{N−1}`, with `n = N − 1`. The A-cur tick-`N − 1` return is reached by `n = N − 1 − m ≤ T` when
`m + T = N − 1`, and the half-period scalar return by `n = N/2 − m`. AW-1 is correct (see "Brief
items" 6); stating this distinction makes the marker precise.

**O6. SNR-1 vocabulary.** §3 says the negative "is reported as conditional on that assumption".
SNR-1's category for an outcome that relies on an assumed capability is "reported as … concerning an
assumed apparatus [preparation], and it does not count". Use SNR-1's wording.

**O7. Pressure test, one further step.** The informative alternative to PREREG's literal T3 would
compare the marked and the unmarked preparation at the same tick. Proposition 2.8(i) shows that this
comparison is degenerate on K1 under μ-G: declaring a marker changes no law. This strengthens the
note's conclusion that the T3-sense negative has no erasure-specific content.

***

## Brief items

**1. Theorem 1 and its instances: correct.**
- (a): the pushforward of a uniform law under a homomorphism is uniform on the image. So `Y_t` given
  `s_Σ = x` is uniform on `M_t x + K_t`, and `W → q_t(s_Σ) → Y_t` with `q_t = Y_t + K_t` gives
  equality of the mutual informations.
- (b): `π_A pr_A φ^t` is surjective, so `im M_t + K_t = R_A`, and hence `q_t = 0 ⟺ K_t = R_A`.
- (c): the all-or-nothing case is immediate.
- (d): checked:
  - the pullback `φ*(c₁, c₂) = (−c₂, c₁ + Ac₂)` and its inverse `(d₂ + Ad₁, −d₁)`;
  - the recurrence for `α_k`;
  - the readout `(α_t, −α_{t−1})`, the A-cur condition `α_t = 0`, and the value
    `α_0·x − α_{−1}·y`.
- Theorem 1′: the three cases are equality, disjointness and the remainder of two translates. Its
  μ-G reduction is correct.
- Proposition 1.4: the inverse `(x′, y′) ↦ (A_{AA}x′ − y′, x′)` is checked; under A-cur the map is
  surjective through `x_A`.
- Instance 1.1: `u_2(i) = y_i + 2y_{i+2} − x_{i−1} − x_{i+1}` on `ℤ/4`. All four entries check, and
  so do `K_2 = {(a,b,b,a)}`, both annihilating readouts and `q_2 = (0, −r)` against `(−r, 0)`. Both
  pulses check: the left-moving one needs `c = 3`. Over `ℤ/2`, `A² ≡ 0`, `φ²` and `φ⁴ = id`, and the
  `t = 3` content all check.
- Instance 1.2 checks:
  - the 2-walk counts `6, 1, 2`;
  - the coefficient `5`, with `x_0` absent;
  - `K_2 = 𝐑 ⊕ 5𝐑` (A-reg) and `5𝐑` (A-cur);
  - the class `f + 5𝐑`, and the pair `f = −1` against `1` over `ℤ/5`;
  - that `L ≥ 5` keeps `±2e_c` distinct.
- Instance 1.3: `u_1(1) − y_2 = y_0 + x_1`, a binary symmetric channel, gives `1 − h(p)`. This holds
  whatever the law of the other cells, given that `x_1` is independent of them.

**2. Theorem 2: correct; both directions re-derived separately.**
- Chebyshev form and Cassini: the base case and the inductive step check.
- Lemma 2.2: uses translation covariance and `|Σ + v| = |Σ|`.
- Lemma 2.3:
  - (⇒) the three `Σ`-row conditions become scalars; `βA = (γ + δ)I` with unit off-diagonal
    entries, valid for `L_c ≥ 3`, gives `β = 0` and `δ = −γ`; Cassini gives `γ² = 1`.
  - (⇐) immediate.
- Lemma 2.4: the subgroup, the homomorphism into an exponent-2 group, and the kernel `Nℤ` check.
- Theorem 2(a):
  - (⇒) the `Σ`-marginal is `B_t`-invariant, aperiodicity forces `B_t = 0`, and Lemma 2.3 applies;
  - (⇐) `(γ·)_*λ ⊗ U = λ ⊗ U`.
- Theorem 2(b): the chain J-return ⇒ full return (via (a)) ⇒ T3's equivalence ⇒ J-return. The last
  step needs `Σ ∪ A` read at the tick, as R-5 records. Full return ⇒ J-return is a marginal.
- Theorem 2(c): `T_γ ∩ [1, N−1]` is `∅` or `{N/2}`. A return for every point carrier requires
  `γ = 1`, since a unit vector `e` has `(γ − 1)e ≠ 0`.
- Theorem 2(d): immediate.
- Proposition 2.5:
  - (a) is immediate.
  - (b): `Av = 2v` for `v = (−1)^{i_1}` in `d = 3`, `N_0² = 0`, and
    `M_2^t = [[1−t, t], [−t, 1+t]]` all check; a scalar power forces `γ = 1`.
  - "Ruled out" holds for `ℤ/2` and for native cubic tori with an even side `≥ 4`. The summaries
    need the `d = 3` scope (finding 2).
- Proposition 2.6:
  - the ball-support induction and the value `ũ_t(i + te) = r` check;
  - the translate estimate `|t − k_c| ≥ L_c − t > t` checks;
  - symmetry of `U_t(A)` moves the leakage to a `Σ`-row.
- Proposition 2.7: Cassini gives `β² + γ² − 1 = βγA`; the prime-power dichotomy and `U_{t+1} = −βI`
  check. The ticks `N/2 − 1`, `N/2` and `N − 1` are correct for prime-power `q` (finding 3). The
  converse is missing (finding 8(a)).
- §2.1's `Per(Σ) = {0}` criterion: a coset of a subgroup of order `k ≥ 2` spans at least `L/2 + 1`
  residues.

**3. Visibility at `D`: correct.** Proposition 2.8(i) is S-L5 at the level of laws:
`K^D_t = π_D pr_D φ^t(S_{Σ^c})` does not see how `Σ^c` is partitioned. In (ii), at `B_t = 0`, `φ^t`
maps `S_{Σ^c}` onto itself, so `D` shows no carrier dependence. The link to J-return needs Theorem
2(a)'s hypotheses (finding 8(b)). In (iii), Instance 1.1 with `D = {1, 2}` over `ℤ/2` checks, and
C2-3 confirms directly that no tick `1 ≤ t ≤ 3` is a J-return.

**4. Pressure test: correct.**
- Lemma 2.3 and the forward direction of Theorem 2(a) use only the `Σ`-marginal. The marker plays
  no role, and the obstruction is present with no marker declared.
- The conclusion that the negative "is not specific to erasing a which-path record" is right.
- So is the statement that it does not discriminate K1 from an eraser experiment: PREREG's T3
  compares with the pre-marking preparation, and a propagating carrier does not satisfy that in any
  theory.
- The negative is specific to the μ-G background. With a quiet (assumed) background the leakage
  would carry no content. The note's scope "in a uniform background" is correct.
- O7 adds one step.

**5. D-1 consequences: correct, at the right status.**
- "(β) generically fails" is exact at `t ≤ 1` in every geometry. Elsewhere it holds iff
  `K_t = R_A`. CALC-F2's "only" needs finding 6.
- Where `K_t ≠ R_A`, (β) holds as a single-tick (R1) correlation for the partition by `q_t`. Its
  reading as a which-path partition is correctly left to (γ). D-1 is undecided at (γ).
- The miss branch stays unreachable: (γ), T0 and the prepared carrier are unsourced.
- Nothing counts under SNR-1. All of this is labelled [A-inf], which is the right status. The SNR-1
  bullet must also carry S-L2 [NP] (finding 5) and use SNR-1's own wording (O6).

**6. AW-1: correct.**
- With `m + T < N`:
  - `N/2` lies in the window whenever `m ≤ N/2 ≤ m + T`;
  - `N − 1` lies in it exactly when `m + T = N − 1`.
- Both are reached by an available `n ≤ T`. Theorem 2(d) shows the first acts on every region as a
  scalar multiple of the identity; `φ^{N−1} = φ^{−1}` is likewise a global map.
- AD-1(f)'s "below the recurrence order" excludes neither.
- AW-1 is a genuine assumption-watch marker. O5 names its source.

**7. Hypotheses, labels, honesty: satisfactory, with the changes above.**
- §0's hypotheses are explicit.
- [proved here], [NP], [A-inf] and [assumed] are kept apart. §1.7, §2.8's pressure test and §3 are
  correctly [A-inf].
- No numerical argument appears anywhere.
- R-1 to R-7 are real remaining steps. R-1's scope needs correcting (finding 4). R-3 is correctly
  stated, but §2.8 must carry the prime-power hypothesis it concerns (finding 3). R-5 is the exact
  condition for T3 ⇒ J-return. R-6's slab lift checks: transverse-constant `g` gives
  `(Au)(i) = g(i_1+1) + g(i_1−1) + 4g(i_1)`, and for `q | 4` that is the ring rule.
- The off-`main` table (§6) classifies the branch drafts correctly as support off `main`.

***

## Checked

- Every proof in §§0–2: the Chebyshev form, Cassini, Theorem 1(a)–(d), Theorem 1′, Propositions
  1.4–1.6, Lemmas 2.1–2.4, Theorem 2(a)–(d), Propositions 2.5–2.8, and the `Per(Σ)` criterion.
- Instances 1.1, 1.2 and 1.3 entry by entry, and the `ℤ/2` order computation `N = 4`.
- Each control: whether it holds, and whether it could have failed (finding 7).
- Two independent dual computations, for Instance 1.2 and for C1-4.
- Counterexamples confirming that the `d = 3` and prime-power hypotheses are needed (findings 2, 3).
- The constant-mode exclusion for rings (O3).
- The directions of every "iff" (finding 8).
- The cited blob ids and the spot-checked line quotations.
- The D-1, SNR-1 and AW-1 readings against PLAN §8.4 and §8.6, U1 AD-1, U4 §3.2 and §4.2, VER §1.3
  to §1.5, and PREREG §5.3 and T3.

## Not checked

- U4-SOURCES-r1's content, and the parts of U1, PLAN and U4 the note does not use.
- Whether S-L2 holds under U1's §3 criterion. It enters as [NP], and that standing is unchanged here.
- R-1 (half-period scalar returns on all-odd native tori with `q ≥ 3`), R-2, R-4, R-6 and R-7. These
  are open, and nobody computed them.
- The general-`W` clause of Theorem 1′, beyond its statement.
- No Lean, no program and no enumeration were used, per the paper-only authorization.
