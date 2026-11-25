# Review of REUSE-TEST-SPEC r1

**Object.** `REUSE-TEST-SPEC-r1.md` on branch `research/ro1-sector-c-1169-20261114` at `bf809e3b`,
directory `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, off `main`.
The object's inputs at `6ab9515d` were checked against its stated blobs: `S3-U3-r3.md` `77b815b4`,
`LIT-REUSE-r2.md` `291abebf`, `RR1-REGISTER-BRIEF-r1.md` `953c6f58`, `S3-U1-r5.md` `68983f86`,
`S3-U2-r4.md` `1bcb9e17`, `REVIEW-U3-L2-L3.md` `3a81d18d`, and TSI on `main` `65db5a7c`. All match.
`bf809e3b` adds only the object to `6ab9515d`.

**Reviewer.** Independent and not an author. Paper-only: hand derivations and reading. I ran no
computation beyond one arithmetic evaluation of the arm W threshold in §1.2, and made no edits,
commits or GitHub writes. Every derivation below is my own hand check
[A-inf]. Literature pointers that come from my memory are marked *unverified*.

**Verdict: ACCEPT WITH CHANGES.** Q-2 and Q-3 are correct at the stated hypotheses. Q-3 holds at a
wider scope than the note claims. The S-R schedule realizes both lemma patterns on both wings, and
both RR-1 forms can be evaluated from its records. The quantum predictions are correct. The changes
listed as required are local corrections:
- arm W's lemma coverage is wrong (countermodel M-2);
- the [A-inf] on the fair-coin `⊥` rule is false (countermodel M-1);
- DR-3's exclusion is dominated by a baseline test that the note does not state;
- DR-3 and DR-4 have no countercontrol;
- the outcome map is not a function;
- two platform statements go beyond LIT's record.

None of them touches the design's core or any conditional OI statement in §10.1, except the arm scope.

***

## 1. Q-2 and Q-3, re-derived

### 1.1 Q-2: correct, and tight

Setting: (k1) and (k4), with first-use responses `A₁(x, y, λ)` and `B₁(x, y, λ)` and a law of `λ`
that does not depend on the policies.

- Put `a′(x) := A₁(x, 0, λ)` and `b′(y) := B₁(0, y, λ)`. These are local responses under a
  policy-independent weight, so `|S′| ≤ 2` (Main:389).
- For every `(x, y)`: `|E_xy − E′_xy| = |E[(−1)^{A₁⊕B₁} − (−1)^{a′⊕b′}]| ≤ 2 P(A₁⊕B₁ ≠ a′⊕b′)`, and
  this is at most `2[P(A₁ ≠ a′) + P(B₁ ≠ b′)]`.
- Terms, one per `(x, y)`:
  - `(0,0)`: 0;
  - `(0,1)`: `δ_A(0)`, since `B₁(0,1) = b′(1)`;
  - `(1,0)`: `δ_B(0)`, since `A₁(1,0) = a′(1)`;
  - `(1,1)`: `δ_A(1) + δ_B(1)`.
- The triangle inequality over the four terms gives `|S₁| ≤ 2 + 2Σδ`. The bound does not depend on
  which CHSH term carries the minus sign. ✓

Tightness: a mixture with weight `p` of the PR table `a = r ⊕ xy, b = r` (`δ_A(1) = 1`) and a local
table with `S = 2` gives `S = 2 + 2p` and `Σδ = p`. So Q-2 holds with equality on that family, and
`2√2` needs `Σδ ≥ √2 − 1`. The instances on record satisfy it with slack: TSI's candidate has
`Δ_B(1) = 1` against a margin of `0.414`, and `T` has `δ_B(1) = 1`.

**Use in DR-3: correct under (U), for arm P, with a deterministic `⊥` rule.**
- Under (U), `ε_A(x; (0,0)) = 0` and `ε_A(x; (0,1)) = P(A₁(x,0) ≠ A₁(x,1)) = δ_A(x)`, so
  `Δ_A(x) = δ_A(x)`. Likewise `Δ_B(y) = δ_B(y)`.
- The (F)-form TV bound `H ≥ δ_A(x)` holds: the off-diagonal mass is 0 against `δ_A(x)`.
- Inter-event memory: Q-2 and the identity `Δ = δ` are linear in the per-event conditional law. They
  therefore hold for history-averaged rates, and the martingale estimators of §8.1 are the right
  objects. ✓

Two scope failures follow (M-1, M-2).

**M-1: the fair-coin `⊥` rule breaks DR-3's inference.**
- Model: `λ = r`, fair. Alice's raw response is `R_A(0, y) = r`, `R_A(1, 0) = ⊥` and
  `R_A(1, 1) = r ⊕ 1`. Bob's is `R_B = r`.
- It is (U): the same functions at both uses and `λ` unchanged.
- With a fresh fair coin per `⊥`:
  - `E₀₀ = E₀₁ = 1`, `E₁₀ = 0` and `E₁₁ = −1`, so `S₁ = 3`.
  - Alice holding `(1,1)`: under Bob `(0,0)` she has two independent coins, so `ε = ½`. Under Bob
    `(0,1)` she has a coin against `r ⊕ 1`, so `ε = ½`. Hence `Δ_A(1) = 0`. All other `Δ` are 0.
- So `ΣΔ = 0 < (S₁ − 2)/2 = ½`. DR-3 would return `ns-excludes-U` on a (U) realization.
- In general, under the coin rule `Δ_A(x) = δ_A(x) − ½ P(⊥ at (x,0) only)`.
- §6.3's [A-inf], that an assigned outcome is "a fixed function of that wing's own raw record" and
  keeps the source structure, is false for the coin. A coin drawn fresh at each use is fresh noise,
  which is case (N).
- DR-2's unassigned test would flag this model's raw `⊥` pattern. The inference is still invalid as
  stated.
- With the deterministic rules `⊥ ↦ 0` and `⊥ ↦ 1`, the same model gives `ΣΔ = ½`, consistent with
  Q-2.
- A repair that keeps a randomized rule: draw one coin per wing per event and apply it to every `⊥`
  of that wing in that event. The coin then sits in `λ`, and (U) is kept.
- DR-4 is not affected. Under Q-3 the fresh coin goes into `ν`.

**M-2: arm W is outside L-2 and outside DR-3.**
- (k2) requires that "the second use applies the same response functions" (U3 §5.1, §2.2). An unsharp
  first use followed by a projective second use is tick-indexed (`A₂ ≠ A₁`), which U3 §2.2 places in
  case (N).
- The proof of L-2 then fails. With different functions, the comparison under Bob `(0,0)` against
  `(0,1)` tests only `A₂`'s dependence on `y₂`, while S₁ is governed by `A₁`.
- Countermodel:
  - `λ = (R, C, f_A, f_B)`, with `R`, `f_A` and `f_B` fair and `C ~ w_{η*}`, all independent;
  - first use: `a₁ = R` and `b₁ = R ⊕ x₁y₁ ⊕ C`, so `S₁ = 2√2`;
  - second use: `a₂ = f_A` and `b₂ = f_B`, with `λ` unchanged.
  - Both complete local histories are uniform on `{0,1}²` whatever the remote policy. This meets
    (k1), (k3), (k4), (k5) and the `λ`-unchanged half of (k2), and it violates L-2's conclusion.
- Separately, a same-function (U) realization predicts `ε = 0` at fully repeated policies, while arm
  W's QM value is `(1 − η)/2`. In arm W, (U) is therefore excluded trivially, without L-2.
- §5's "Lemma coverage: L-2 only" and "L-2's comparison at a different instrument" have no support,
  and neither does the `η_Aη_B > 1/√2` threshold as an L-2 condition.

### 1.2 Q-3: correct, and its scope is wider than stated

- Under Alice `(x, x)` and Bob `(y₁, y₂)`: `a₂ = A₂(x, y₂, G(λ, ν, x)) =: g(λ, ν)`, which does not
  depend on `y₁`. By (k4′), `(λ, ν)` has one law across the policies.
- The triangle inequality gives
  `P(A₁(x,0) ≠ A₁(x,1)) ≤ P(A₁(x,0) ≠ g) + P(g ≠ A₁(x,1)) = ε_A(x; (0, y₂)) + ε_A(x; (1, y₂))`. ✓
- Within U3's formalism the joint second use reads `κ`, so `a₂` cannot depend on `b₂` except through
  `κ`. No hidden route via Bob's second output is open.
- Dilation carries over:
  - first-use noise with a policy-independent law goes into `λ′ = (λ, μ₁)`;
  - second-use noise goes into `ν`;
  - `G(λ′, ν, x₁)` still cannot compute `a₁` without `y₁`.
  The §A "Scope" caveat can therefore be discharged.
- **DR-4 use:** `Λ ≥ Σδ ≥ (|S₁| − 2)/2` when neither wing's content depends on `(y₁, a₁, b₁)`, or
  on `(x₁, a₁, b₁)` for wing B. ✓
- **Wider scope (finding, POSITIVE).** The derivation uses neither repeatability, nor `Θ`'s
  identification with the Lüders law, nor (k5′). The ε's enter only as measured rates. Q-3 therefore
  holds for any first-use instrument, arm W included.
  - At ideal QM in arm W with `η_A = η_B = η`: `Λ = 4(1 − η)` and the margin is `√2 η² − 1`.
  - DR-4 can then exclude (U) and (N) for `η > (−4 + √(16 + 20√2))/(2√2) ≈ 0.9385`.
  - The note's "L-3 says nothing about non-repeatable instruments" is correct for L-3 but does not
    carry over to Q-3.
- Q-3 also covers "(U) plus fresh local noise per use", which is (N). This is the realistic class
  that DR-3 does not reach (§2.3).

## 2. Does the design test what U3 §10.3 needs?

### 2.1 Schedule

- Four fair independent bits per event give all 16 joint policies.
- Every holding policy `(s, s)` on each wing meets all four remote policies. That covers (k3), since
  Bob `(0,0)/(0,1)` occur with Alice `(x,x)`, and (k3′), since Bob `(0,y₂)/(1,y₂)` occur with Alice
  `(x,x)`, and the mirror pairs of both.
- I recounted the "eleven of sixteen" claim:
  - (k3) and its mirror give 7 joint policies;
  - (k3′) and its mirror at `y₂* = x₂* = 0` add 4;
  - the total is 11. ✓
- The setting changes between uses that §10.3 asks for occur on both wings. ✓
- Drawing the second setting after the first use is complete is consistent with (k3): the lemmas do
  not need it, and C-2 tests its physical counterpart. ✓

### 2.2 Records and forms

- §6.1 keeps both outcomes per wing per event, with `⊥` and every attempt.
- RR-1(R) is computed as `w₁ ⊕ w₂` (BRIEF §4). ✓
- Both forms can be evaluated. The (R)-form `Δ` and `Λ` are numerically the same statistics as the
  (F)-form repeat-failure rates. Only `H_W` differs between the forms. The separate DR-3 rows are
  therefore one number reported twice, and the note should say so (O-5).

### 2.3 Finding (NEW): DR-3's exclusion is dominated by a baseline test

- Under strict (U) the outputs at a fully repeated joint policy (Alice `(x,x)`, Bob `(r,r)`) are
  identical, so `ε_W(s; (r,r)) = 0` exactly. This also holds after dilation, because the noise sits
  in the unchanged `λ`, and it holds in both forms.
- Any apparatus with imperfect repeatability (Leupold: `R ≈ 0.996`) gives `LCB(ε_W(s; (r,r))) > 0` at
  `N ~ 10⁶`. That excludes every strict (U) realization with no Bell violation and no use of L-2 or
  Q-2.
- DR-3's `Δ = ε(0,1) − ε(0,0)` subtracts exactly the baseline that already excludes (U).
- The robust class, unchanged `λ` with fresh local noise, is (N). L-2 does not reach it, and DR-4
  does (Q-3).
- So in arm P, `ns-excludes-U` adds information only when every fully repeated cell is consistent
  with 0, and otherwise it is implied twice over: by the baseline and by `rep-excludes-UN`.
- The L-2 half of §10.3 is still served. DR-2 supplies the setting-independence record that §10.3's
  L-2 condition asks for. But the design and §10.1 should state what DR-3 adds.

## 3. Quantum predictions for `|Φ⁺⟩`

All checked by hand. ✓ throughout:
- **Arm P.**
  - `S₁ = 2√2` with the CHSH angles in the x–z plane, where `⟨σ_a⊗σ_b⟩ = a·b` (TSI (1)).
  - `ε = 0` and `Λ = 0` (Lüders, rank one).
  - `F_W = ½`: after the first uses the state is a product of eigenstates, and the orthogonal axis
    gives a fair outcome independent of `(a₁, b₁)` (TSI (9)).
  - `H_W = 0` and `P₁₂ = 0`.
- **Arm W.**
  - With effects `(I ± η σ_n)/2`, the correlators scale by `η_Aη_B`, so `S₁ = 2√2 η_A η_B`.
  - Repeat failure: with `K_± = √((I ± ησ_n)/2)`, `P(a₁ ≠ a₂) = ((1−η)/2)(ρ₊₊ + ρ₋₋) = (1−η)/2` for
    every local input. So the value is independent of π, and of conditioning on remote outcomes. ✓
  - `H_W = 0`: a local CP instrument on Bob leaves Alice's reduced dynamics unchanged.
- Arm W's second use at a changed axis is **not** fair given the first records. With
  `K σ_m K = (√(1−η²)/2) σ_m`, a remote-induced Bloch component along `m` survives, scaled by
  `√(1−η²)`. The note uses `F_W` only in arm P, so nothing is wrong. If `F_W` is ever reported for arm
  W, its QM value is not ½ (O-6).
- C-3's choice of input is right. Each wing's reduced input is maximally mixed under every remote
  policy, so the entangled-wing ε equals the single-system ε on a maximally mixed input, for any
  instrument, including asymmetric detection error.

## 4. Decision rule and controls

### 4.1 Do the margins let the data choose the threshold (§A.29)?

No. The inequality `ΣΔ ≥ (|S₁| − 2)/2`, or `Λ ≥ …`, is a theorem-derived constraint between two
measured quantities. Its form is fixed in advance, and the uncertainty in S₁ is carried by `LCB(S₁)`
under a union bound. That is preregistering the rule, not the numbers, which is what §A.29 asks for.
Three residual freedoms should be pinned at freeze:
- **(a)** the CHSH orientation, meaning which term carries the minus sign. The note writes `|S₁|` in
  Q-2 and `S₁` in DR-1, DR-3 and DR-4. Choosing the maximum over the four forms after the data needs
  a selection correction (R-6).
- **(b)** the confidence construction. Holm's step-down does not define a "level allocated" to a
  confidence bound. Use Bonferroni weights for the bounds, or a single martingale bound on the linear
  statistic `(S₁ − 2)/2 − ΣΔ` (respectively `− Λ`), which is cleaner and more powerful (O-2).
- **(c)** which `⊥` rule governs a verdict. Under C-12, an exclusion should be claimed only if it
  holds under every rule in the set that keeps the source structure (R-2).

### 4.2 Controls

Postselection (C-7), detection (C-9), locality (C-11), measurement independence (C-1), prefix (C-2),
memory between events (C-10), crosstalk (C-5, C-6), source quality (C-4), repeatability (C-3),
analysis freeze (C-8) and `⊥` sensitivity (C-12) are the right list. The locality inequality
`L > c(τ_A + τ_B)` is sufficient; `c·max(τ_A, τ_B)` already suffices for windows that start
together. Gaps:
- **No countercontrol for DR-3 or DR-4** (required; AGENTS.md, Exactness and controls). C-4 makes
  DR-1 fail, so DR-3 and DR-4 are never evaluated on it. Nothing shows that DR-3 and DR-4 can return
  `ns-unresolved` or `rep-unresolved` when a (U) or (N) realization with `S₁ > 2` is present. Cheap
  forms, specified now and not run:
  - frozen-code runs on synthetic records of TSI's (U) candidate, the fresh-replacement (N) and
    LREV R3's (S) realization. The expected outputs are unresolved, unresolved and excludes;
  - optionally, a laboratory emulator with a deliberate classical channel between the wings.
- **C-5 must run in a separate calibration block.** Injected into production events, it produces
  `ns-disagree` by construction. The note does not say which.
- **Pass criteria are missing for C-10 and C-6**, and C-10 is marked required. DR-0 cannot declare a
  control failed without a criterion. Fold this into §11 item 5.
- **T-C ensemble.** Q-2 and Q-3 relate S₁ and ε on one ensemble. Under fair sampling, DR-1, DR-3 and
  DR-4 must be computed on a common subensemble, for example events with all four uses detected,
  with the fair-sampling assumption stated in model terms: detection independent of `λ` and of the
  policy. Mixing coincidence-conditioned S₁ with ⊥-kept ε is not covered.
- **Freedom of choice (T-A).** The setting draws should lie outside the future light cone of the
  pair's emission or herald, as in loophole-free Bell tests. C-1 is statistical only.
- **Setting-probability bias.** The IPW estimators assume exactly 1/16, and χ² detects only gross
  bias. Carry a declared bias bound into the martingale bound (O-3).
- **Setting fidelity.** A misapplied second setting inflates ε at "held" cells. The applied-time field
  exists, but no fidelity monitor does (O-4).
- **T-B wording.** "bounded by C-5 and C-6" should read "probed by". These controls detect specific
  couplings and do not bound unknown ones.

### 4.3 The outcome map is not a function

- `(ns-consistent, ns-unresolved, ·, rep-disagree)` matches both the third row and the fifth row.
- `(ns-consistent, ns-excludes-U, ·, rep-disagree)` loses the L-2 half that is met.
- Arm-W-only runs, where DR-4 is not evaluated, have no row.
- The verdict text is to be generated by frozen code, so the map needs a stated precedence and an
  exhaustive set of rows (R-5).

## 5. Conditionality, the bearing section, and the platform claims

- **Conditionality.** Every OI-attributed entry in §7.2 and §10.1 carries L-2 or L-3, with Q-2 and Q-3
  where they are used. The exceptions are:
  - the arm W coverage (M-2);
  - two entries that rest on other [OFF] results, the fresh-cell lemma and LREV R3. The header's "every
    statement attributed to OI is a consequence of L-2, L-3, Q-2 or Q-3" should name these (O-7).
  - §10.1's bullet on RQ-UPD-1 should carry Q-2 and `Θ` as well as L-2.
- **The bearing section, §10.1–10.3.** It claims nothing beyond the lemmas:
  - it states that no model executes an update;
  - it states that (S) cannot be separated from QM;
  - it states that PR has no target law;
  - it places the result on the consistency axis. ✓
  §10.1's first OI bullet should be restricted to arm P (M-2).
- **Platform claims against LIT-REUSE-r2.** Leupold (53 million, QRNG latency below 50 µs, above
  99.6 %, the public dataset, the purge), Kirchmair, Mao (the four-detector quote, time-tagging,
  `η`), Zhu (matched indices), White (`φ`, all four qubits read out, near-unit efficiency, rescaling,
  "cannot be ruled out here"), Padovan's quote, and Choi (abstract only) all match. Mismatches:
  - "Mao set wave plates per acquisition" is LIT's *[writer's reading]* (LIT §1.8), and it should carry
    that label;
  - the arm P first uses for P-1, local nondestructive fluorescence detection of one ion of an
    entangled two-ion crystal with the other ion preserved, and for P-2, Mao's coupling at full
    strength, are not on LIT's record. They belong in the "Additions" row;
  - "Detection loophole: none expected" for P-1 is a design expectation and should be marked [DES].

## 6. Claim/evidence boundary

- Overclaims found:
  - §6.3's [A-inf] (finite rule → all rules; M-1);
  - §5's coverage row (necessary ingredient → coverage; M-2);
  - T-B's "bounded".
- Correctly bounded:
  - the [A-inf] "no outcome favours one form";
  - the consistency-axis classification;
  - §10.2's refusal to read `ns-disagree` as support for (U);
  - Appendix B's labelling as illustrative. Its figures check: `16·√(ln 10⁴ / 2N) ≈ 34/√N`;
    `8 × 34 ≈ 270`; margin `0.273` at `S₁ = 2.546`; `N ~ 10⁶`. The joint per-event estimator of Λ
    has range 32, not 8 × 16, so the planning figure is conservative by about 4 in half-width (O-2).
- Q-2 is elementary, but a literature check is still owed (§11 item 1). Pointer, *unverified*:
  bounds on CHSH under relaxed parameter independence, for example Hall 2010 on indeterminism and
  signalling.

***

## Required changes

- **R-1 (M-2).** Remove L-2 coverage from arm W (§5 table and bullet), restrict DR-3 to arm P, and
  restrict §10.1's L-2 bullet to arm P. Arm W keeps DR-2 and C-6. Optionally it gains DR-4 through
  Q-3's wider scope (O-1).
- **R-2 (M-1).** Correct §6.3's [A-inf]. Either drop the fresh fair coin from the set used for DR-3,
  or replace it with one coin per wing per event. State that DR-3 and DR-4 exclusions are claimed
  only under rules that keep the source structure.
- **R-3 (§2.3).** State that strict (U) is excluded by `LCB(ε_W(s; (r,r))) > 0` alone. Add that
  baseline as a reported statistic, and state when DR-3 adds information. Make §10.1's attribution
  match.
- **R-4 (§4.2).** Add a countercontrol for DR-3 and DR-4 that shows they can return unresolved on
  (U) and (N) realizations with `S₁ > 2`, as a freeze precondition. Also specify C-5 as a separate
  calibration block, give pass criteria for C-6 and C-10, and define the common subensemble for T-C.
- **R-5 (§4.3).** Make the outcome map exhaustive and give it a precedence order.
- **R-6 (§4.1).** Pin the CHSH orientation at freeze and use one sign convention in Q-2 and in the
  rule.
- **R-7 (§5).** Label Mao's per-acquisition setting as LIT's writer's reading. Add P-1's local ion
  detection and P-2's full-strength coupling to "Additions", and mark P-1's detection expectation
  [DES].

## Optional

- **O-1.** Extend Q-3's stated scope to any first-use instrument. DR-4 then applies to arm W at
  `η ≳ 0.94` (ideal QM), and averaging Q-3 over both `y₂` (and `x₂`) uses all four remote policies,
  which improves power.
- **O-2.** Use a single martingale bound on the linear test statistic, or Bonferroni weights. Note
  the factor of about 4 in Appendix B.
- **O-3.** Carry a declared bound on setting bias into the confidence bounds.
- **O-4.** Add a monitor of applied-setting fidelity.
- **O-5.** State that the (F)-form and (R)-form DR-3 and DR-4 statistics coincide. Only `H_W`
  differs.
- **O-6.** Note that `F_W`'s QM value ½ is specific to arm P. DR-6's `UCB(F_W) < 1` is nearly
  automatic and adds little.
- **O-7.** Widen the header's list of OI sources to the [OFF] results used: the fresh-cell lemma and
  LREV R3.
- **O-8.** "windows that start together" needs a frame; the general condition is
  `|t_reg − t_choice| < L/c` for every cross-wing pair.
