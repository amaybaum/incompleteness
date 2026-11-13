# Focused delta review of OA-2 r3 (`OA-2-REPORT-r3.md`), r2 → r3 only

**Reviewer standing.** Independent, read-only, paper-only. No computation on any OI rule, no script,
no commit, push or GitHub write. Sources read with `git show` / `git diff`. Reviewer derivations are
marked [RW]. Gate: owner decision (amaybaum, 2026-11-13) "Run all three (Recommended)"; the historical
ACCEPT of r2 (`REVIEW-OA-2-r2.md`) does not cover the r3 edits.

**Text reviewed.**

- Branch `research/oa1-w1-1-20261112` at `5fec096645b5a201af3ce37c0a60538e8407a365`.
- `OA-2-REPORT-r3.md`, blob **`f7ca0968fee0acc5e7b038702490b467d2026baa`** (equals the r3 row of
  `OBJECTS.md`, SHA-256 `dd637ef6…33bf`).
- Baseline `OA-2-REPORT-r2.md`, blob `70a435ba4c1ebceaa87fada32812e43203dc4e22`.
- Delta: `diff -u r2 r3`, 24 hunks, +238/−75.
- Citation forms: `r3:n` is a line of the r3 blob above; `r2:n` of the r2 blob; `Rev2:n` of
  `REVIEW-OA-2-r2.md` (blob `e55c66e5`). Other sources were read at `origin/main` = `911a5cb6` (which
  contains r3's pin `615cc119`; the cited MECH-1, TUNE-1 and OA-1 lines are byte-identical at both),
  and OA-1 r4 at blob `41a1fb79` (identical at `066be3b1` and `5fec0966`).

## Verdict: **ACCEPT WITH CHANGES**

- N1–N7 of `REVIEW-OA-2-r2.md` are applied, and no verdict needs to move.
- Three required changes are substantive, all local:
  - **D1 (N1).** The new general proof of B(ii)(⇒) is correct only under a hypothesis it does not
    state: the effect set must be closed under convex mixing. Without that hypothesis the direction is
    false; a two-point counterexample is given below.
  - **D2 (N1 propagation).** The corrected Limits line (r3:958–960) is wrong: "Neither direction decides
    simplex-embeddability". (⇐) with (i) is exactly what decides it, positively, in E(b) and class N.
  - **D3 (N6).** The odd-`q` extension of the class-N result rests on MECH-1 Proposition C(d), which
    does not say what is used. The inference it relies on ("inside a noncontextual theory, hence
    noncontextual") is refuted by OA-2's own N2.1 counterexample. The extension is recoverable from
    MECH-1 Corollary S, which r3 did not read.
- The remaining items are wording, citation and propagation nits.

***

## 1. Did r3 apply `REVIEW-OA-2-r2.md`'s required nits?

| Nit | Required (Rev2:268–281) | Applied in r3 | Assessment |
|---|---|---|---|
| **N1** | General (⇒) proof, or display one way. Fix the Limits line | r3:253–278 (proof), r3:848 (status), r3:958–960 (Limits) | **Applied with defects D1, D2.** The proof is the convex-split argument requested, but it omits its convex-closure hypothesis. The new Limits text misstates the (⇐) direction |
| **N2** | Drop "and transformation-" from E(b) step 5, or verify B(iii). State that G3 is the prepare–measure (PM) criterion | r3:512, 519–525, 537, 747, 854 | **Applied.** Transformation NC is withdrawn and PM is stated in E(b), N2.4, §4 and the status table. Propagation nit **D6**: the G3 definition (r3:150), §3.1 (r3:704), §6 (r3:868) and the Limits (r3:955) still carry unqualified "G3"/"Theorem E's NO" |
| **N3** | C-PM for the selector and coin cells, or swap them out. Fix the "returns to position 1" justification. State `K` blanks | r3:112–117, 374–403, 407–411, 433–440, 756, 853, 891, 961–962 | **Applied.** Bounds verified [RW]. Nits **D7** (off-by-one for PREP(ℓ) in the window sentence; the bound is unaffected) and **D8** (the explicit mixture's coin dropped from the C-PM summaries) |
| **N4** | Restate E1 as the contrapositive of (b), translation of the joint record | r3:561–579, 74–75, 856 | **Applied, and correct** [RW]. Nits: **D4**, the unchanged header r3:584 now contradicts the new E1 for non-additive observers; **D5**, the new citation OA1r4:198–204 is the wrong line range |
| **N5** | Per-object partitions and tick horizons; a non-vacuity check; variant-(ii) controls; a preregistered bearing | r3:779–833 | **Applied** as a design sketch, labelled as needing owner authorization (r3:779–780). Nits **D9** (the positive control does not exercise variant (ii)'s distinctive path; the "overwrite" in the single-cell control is not a bijection) |
| **N6** | Preparation side general in `q`, or restrict to `q = 2` | r3:634–652, 858 | **The algebra is correct at every `q`** [RW]. **D3**: the odd-`q` premise source is wrong |
| **N7** | Name (H3) in §0.6. MECH-1:404–418. Credit TUNE-1 Lemma A-T. Update the snapshot | r3:72–73, 492, 501–504, 24–32, 942–946 | **Applied and accurate.** TUNE-1:56–98 is Lemma A-T and says what r3 says: every `q ≥ 2`, `Φ_F`, exchange mode, coset-uniform law, 0-or-1 TV dichotomy. MECH-1:404–418 is Lemma A's statement. The snapshot claim `git diff --stat ec257bee 615cc119` (TUNE-1 drafts only) is verified |

***

## 2. Proposition B(ii)(⇒), redone by hand (r3:257–275)

### 2.1 What the proof establishes

- **Steps 1–6 [RW]: correct as algebra.**
  - Step 2: `d = Σ_P c_i e_i − Σ_N |c_i| e_i = 0` on `W` gives the displayed equality.
  - Step 3: `λ > 0` because `d ≠ 0` forces some `c_i ≠ 0`.
  - Step 4: the weights `c_i/λ` sum to at most 1, so the padding weights are nonnegative.
  - Step 6: `A − B = d/λ`, because the null effect is the zero function.
- **The proof uses two facts it does not establish from OA-2's definitions.**
  1. **Step 4: "both are convex mixtures of available effects, so both are available effects".**
     OA-2 defines effects as "all post-processings of held records other than those label cells"
     (r3:107). It never states that the available effect set is closed under convex mixing with
     arbitrary weights.
  2. **Step 7: "in the configuration model the response of a mixture is the mixture of the
     responses".** This holds when mixing is the convex closure of the fragment, with the response
     convex-linear by construction (the standard GPT accessible fragment). It is false as stated when
     the mixing coin is itself a cell of `S` whose value lies in the ontic configuration. In that case
     `A`'s response at `s` is the deterministic function selected by the coin's value in `s`, not
     `Σ (c_i/λ) e_i(s)`.

### 2.2 The hypothesis is load-bearing: (⇒) fails without convex closure [RW]

- **Setup.**
  - `U = {a, b}`, with one reachable law `p = (1/3, 2/3)`, so `W = span{p}` has dimension 1.
  - The effects are the deterministic post-processings of a complete read: `0`, `[a]`, `[b]` and `1`.
- **No two distinct effects are equivalent.** Their values on `p` are `0`, `1/3`, `2/3` and `1`,
  pairwise distinct. So the configuration model is trivially measurement-noncontextual.
- **But `ρ` is not injective.** The effect span is `ℝ²` and `W*` is `ℝ`.
- **Conclusion.** "Measurement-NC ⇒ `ρ` injective" fails for an effect set that is not convexly
  closed.
- **With a fair coin, the proof's own construction applies.** Take `d = 2[a] − [b]` and `λ = 2`. Then
  `A = [a]` and `B = ½[b] + ½·0` agree on `W` (both equal 1/3) and differ on `U`.

### 2.3 Repair [RW], within OA-2's own resources

- **(a) Rational coefficients suffice.** Under every μ OA-2 uses, and under heralds, reachable laws are
  rational. Deterministic post-processings are `{0, 1}`-valued, and coin post-processings are rational.
  So `ρ` has a rational matrix, a nonzero kernel element `d` can be taken with integer `c_i`, and
  `λ := q^m ≥ max(Σ_P c_i, Σ_N |c_i|)` makes every weight a multiple of `q^{−m}`. Then `m` independent
  uniform `q`-ary coins realize `A` and `B` exactly.
- **(b) A coin that lies in `S`.** Replace step 7's sentence with a marginalization argument:
  - The coin is independent of the prepared cells under every reachable law, and uniform.
  - So `U ⊇ (coin values) × U_sys`, and `A`, `B` agree on `W`.
  - Averaging `A − B` over the coin coordinate gives `d/λ ≠ 0` at some point of `U_sys`.
  - So `A ≠ B` somewhere on `U`, and the configuration model is measurement-contextual.
  - A fresh bath cell under μ-G supplies such a coin, as in 𝔊_K. Under μ-O and μ-R this is not
    established; compare r3:731.
- **(c) Alternatively, make convex closure part of the fragment's definition** (Schmid et al.'s
  accessible fragment), with convex-linear responses. Then (⇒) is measure-free, but the convention
  must be stated in §1.0, because physical realizability is then a separate claim.

### 2.4 §A.34

- With the hypothesis stated, the displayed "iff" at r3:241–242 has a witness in each direction:
  - (⇐) at r3:253–256: correct, and it needs no convexity;
  - (⇒) at r3:257–275: correct under the hypothesis.
- The hypothesis must appear in the display itself, not only in the proof.

### 2.5 Consequence for OA-3 r3 (:357–361, :748)

- **Its conclusions survive.**
  - "This proof route fails" needs only that (⇐) does not apply.
  - "Embeddability … is not decided" does not use (⇒) at all.
- **Its wording inherits D1.** The clause "Proposition B(ii)(⇒) makes the configuration model
  measurement-contextual" holds only under the convex-closure hypothesis. OA-3 says "with complete
  effects"; that clause holds if "complete" includes coin-mixed post-processings with an independent
  coin.
- **No OA-2 edit is needed for this.** It is flagged so that OA-3's next revision carries the
  hypothesis.

### 2.6 D2: the new Limits line is wrong (r3:958–960)

- **The text.** "Neither direction decides simplex-embeddability of the fragment: that needs a separate
  argument, such as the counterexample."
- **(⇐) does decide it.** (⇐) together with B(i) gives a preparation- and measurement-noncontextual
  model of the PM fragment. That is exactly how Theorem E(b) step 5 (r3:519–521) and the class-N result
  (r3:653) conclude embeddability.
- **Only (⇒) is non-decisive.** It shows only that *this* model is contextual (r3:276–278 says this
  correctly).
- The status row r3:848 ("both directions proved") is fine once D1's hypothesis is added.

***

## 3. N6: class N at every `q`, and the odd-`q` premise (r3:634–652, 858)

### 3.1 The algebra, redone [RW]: correct for every `q`, indeed for any finite alphabets

- **Effect span.** `{f(z) + g(x)}` has dimension `q + q − 1 = 2q − 1`.
- **Pairing with the level laws.** Pairing `f + g` with the uniform law on `{z = a}` gives
  `f(a) + mean(g)`; pairing with the uniform law on `{x = b}` gives `mean(f) + g(b)`.
- **Injectivity of `ρ`.** If both pairings vanish, `f ≡ −mean(g)` and `g ≡ −mean(f)` are constants with
  zero sum. So `f + g ≡ 0`, and `ρ` is injective.
- **Dimension of `W`.** `W` is spanned by the row and column indicators. `span(rows) ∩ span(cols)` is
  the constants, so `dim W = 2q − 1`.
- **`R` injective on `W`.** `ρ` is an injective map between spaces of dimension `2q − 1`, so it is
  bijective. For `w ≠ 0` some `φ ∈ W*` has `φ(w) ≠ 0`, and `φ = ρ(e)` for some `e` in the effect span.
- **Conclusion.** B(i) and B(ii)(⇐) give a PM-noncontextual configuration model. No convexity is
  needed, so D1 does not affect this.

### 3.2 D3: what C(d) says, and why it is not what is used

- **What C(d) says (MECH-1:763–766 at `911a5cb6`, unchanged since `615cc119`).** "The reachable class
  lies inside the odd-prime quadrature epistricted theory. Spekkens … shows that theory is
  operationally equivalent to the stabilizer subtheory and is a local noncontextual hidden-variable
  model."
  - It is stated for **odd prime** `q`, in the representation R-W, for **N or N+NNB** (MECH-1:751).
  - r3:649 accurately paraphrases C(d) but says "odd `q`".
- **What the class-N conclusion uses** (r3:631–633, 635–637) is narrower and different:
  - the reachable single-cell laws are exactly the uniform, `z`-level and `x`-level laws and their
    mixtures, with no point laws and no mixed-slope line laws;
  - the effect span is `{f(z) + g(x)}`.
- **C(d) does not give the premise.** The epistricted theory contains every Lagrangian line law, of all
  `q + 1` slopes. Under N+NNB the mixed-slope laws are actually reached, because `P` maps the
  `x`-eigenstate to the `(x − z)`-eigenstate (MECH-1:595–596, :712). With them in `W`, `dim W > 2q − 1`,
  `R` is not injective on `W`, and the algebra above does not apply.
- **The inference "inside a noncontextual theory, hence the fragment is noncontextual" is invalid.**
  - **OA-2's own counterexample refutes it.** N2.1 (r3:280–299) is a fragment of the classical
    `F₂²` theory, which is a simplex. It restricts preparations and keeps complete reads, and it is
    measurement-contextual.
  - **So does 𝔊_K, by restricting reads.** Simplex-embeddability is not monotone under restricting
    either preparations or effects.
  - **Hence C(d) does not establish the odd-`q` class-N conclusion,** even with Spekkens' theorem
    taken as an input.
- **The route also breaks two of r3's own rules.**
  - It rests the conclusion on Spekkens [L] via MECH-1. That contradicts r3:50 ([L] is "context only,
    no verdict rests on it") and r3:964 ("Every proof here is self-contained").
- **MECH-1 Lemma S and Corollary S were not read.**
  - They are at MECH-1:572–597.
  - r3's MECH-1 inventory is :1–137, :390–440, :749–830 and a heading grep (r3:923–927).
  - These lemmas are where the needed premise lives.

### 3.3 Recovery [RW], before any concession

- **MECH-1 Corollary S (MECH-1:593–597)** is the premise r3 needs: "No active cell ever has a
  determined mixed functional `a z + b x` with `ab ≠ 0`".
  - It holds for prime `q`, a **bipartite** armed coupling graph and any process of N, record feedback
    included (Lemma S, MECH-1:578–591).
  - It combines Lemma S with AP1 Lemma 3 (isotropy).
- **From it, the single-cell reachable laws [RW].**
  - Each record branch is uniform on an affine subspace (Lemma S's proof).
  - Its one-cell marginal is uniform on a coset of a subgroup of `F_q²`, by TUNE-1 Lemma 0 (T1:50–54).
  - Isotropy (`ω(z, x) = 1 ≠ 0`) excludes the point coset.
  - Corollary S excludes the mixed-slope lines.
  - What is left is the uniform, `z`-level and `x`-level laws, which is the premise.
- **The effect side** at odd `q` rests on Lemma S as well: a single-cell registration has a
  single-sector functional (MECH-1:585–591), together with Theorem W's Lüders reads (MECH-1:466–499, step 4 at :491–495).
  These are [R].
- **So the odd-`q` statement is recoverable for odd prime `q`, class N (not N+NNB), bipartite graph,
  under P1–P2,** on [R] premises from MECH-1 Lemma S and Corollary S, not C(d). Short of that
  re-sourcing, restrict the conclusion to `q = 2`.

### 3.4 Downstream

- OA-3 r3:517 cites OA2:627–656 for "class N's native `Z`/`X` fragment is NC" in a `q = 2` (`G_SM`)
  row. The `q = 2` reading is unaffected by D3.

***

## 4. Other new or changed statements

### N4: Corollary E1, generalized E(b) (r3:561–579) [RW]: correct

- **The model of (b) uses only:**
  - one joint held record `Z` (H4);
  - `Z = Z₀(ω) + h(c)` with `Z₀` not depending on `c`;
  - (xiv), so that the law of `Z₀` under a preparation does not depend on `c`;
  - singleton indicators of `Z`, which are available as post-processings, for preparation NC;
  - (SP), for measurement NC through the (⇐) argument.
- **No affine or H-AR premise enters,** so "any rule … any observer" (r3:569) is correct.
  - The proof works for any setting-indexed bijection of the record space, of which translation is one
    case.
  - It works because the observer's restriction enters only through the translation hypothesis.
- **The contrapositive (r3:571–573) is correct.**
- **The affine specialization (r3:574–576) is correct.** E(a) needs only (H1) and H-AR for the
  translation form, and (H3) is consistent with that.
- **D4 (nit).** The unchanged header r3:584, "Open exits that need no non-translational setting
  dependence", now conflicts with the new E1, whose condition concerns the *joint held record*.
  - A non-additive observer (AW-OA2-1) holds `g(Z₀ + c)`. Settings then do **not** merely translate the
    held record, though they translate the configuration.
  - So that exit is, in E1's new sense, a non-translational dependence.
  - The other two exits fail (H4) or (SP) instead.
  - Rescope the header (edit E4 below).
- **D5 (nit, citation).** r3:579 cites "(OA1r4:198–204, D7)" for "failure of (xiv) gives preparation
  correlation, not control".
  - OA1r4:198–204 (D7) is about post-hoc and timing selection and says nothing about (xiv).
  - The statement is at OA1r4:180–184, D5's "Measure (R4)" bullet: "(xiv) may fail … That is
    preparation correlation (D7), not control". That bullet is r3 content, not r4-only.

### N2: Theorem E(b) step 5 (r3:519–525): correct [RW]

- **Preparation NC (step 4) and measurement NC (step 5) of the `Z₀` model** together give a
  noncontextual model of the PM fragment. G3 as defined (r3:150, first clause) then fails directly; the
  [L] equivalence is not needed.
- **Applying "Proposition B(ii)(⇐)" to the `Z₀` model** is the same argument with `U` replaced by
  `U_Z`. Acceptable, though "by the argument of B(ii)(⇐)" would be exact.
- **D6 (propagation nit).** Because transformation NC is now withdrawn, unqualified "fails G3" holds
  only if G3 is read as the PM criterion. That reading is stated in E(b), but not in G3's own row
  (r3:150), §3.1's G3 row (r3:704), §6 (r3:868) or the Limits (r3:955).

### N3: 𝔊_K resources and C-PM scope (r3:374–440) [RW]

- **Bath.** A used cell at `M_b` re-enters after `M_b − 1` shifts. At most `K − 1` shifts follow, and
  `K − 1 < M_b − 1` holds iff `M_b > K`. ✓
- **Ready conveyor, PREP(p).** The four used cells go from positions 1–4 to `M_r − 3 … M_r`, and the
  earliest re-enters positions 1–4 after `M_r − 7` shifts. At most `K − 2` intermediate PREPs give at
  most `4(K − 2)` shifts, and `4(K − 2) < M_r − 7` holds iff `M_r ≥ 4K`. ✓ The fresh supply needs
  `M_r ≥ 4K`. ✓
- **D7 (nit).** For PREP(ℓ) the used cells end at `M_r − 2 … M_r` (r3:394–395), so the earliest
  re-enters after `M_r − 6` shifts, not `M_r − 7` (r3:396). The bound still holds: `4(K − 2) < M_r − 6`
  whenever `M_r ≥ 4K`.
- **Blanks: at least `K`.** ✓
- **Claim 1 (r3:407–411).** The same selector serves A and B; `ℓ` is swapped to `z₃` and the coin to
  `M_b`. Physical C-PM′ for Claim 1. ✓
- **Claim 2 step 3 (r3:433–440).** Correctly flagged as using C-PM for the selector and the mixture's
  coin.
  - The "PREP variant" alternative (r3:439–440) is asserted without a recount. It is an untested
    sketch.
  - The verdict does not depend on it, since C-PM is the stated convention.
  - Acceptable, but label it [W] / not checked.
- **D8 (propagation nit).** §1.0 (r3:115–116) and Claim 2 (r3:435–437) put the explicit mixture's coin
  under C-PM. The summaries drop it: r3:756 ("C-PM′ for the label and coin cells, and C-PM for the
  selector cells"), r3:853, r3:891 and r3:961–962. Read literally, these place the mixture coin under
  C-PM′, which r3 itself says is false. The next-step spec r3:784–785 has the same slip for 𝔊_K.

### N5: next-step-2 sketch (r3:776–833)

- **Correctly scoped.** It is labelled a design sketch needing owner authorization; no claim is
  promoted.
- **The decision rule (r3:822–833) is appropriately narrow.**
- **The variant-(ii) negative control's classicality argument is correct.**
  - `W = ℝ^U` from heralded point laws.
  - Complete reads, so `R` is injective on `W` and `ρ` is injective.
  - Hence B(i) and B(ii)(⇐).
- **D9 (nits).**
  - **(a) The positive control does not test variant (ii).** r3:804–805 says 𝔊_K's variants
    "coincide and validate both pipelines". Because they coincide, 𝔊_K cannot detect a defect in
    variant (ii)'s distinctive handling (non-nested, overwritten reads). Say "validates the shared
    pipeline". A variant-(ii)-specific positive control is to be designed in the preregistration;
    AW-OA2-4's herald/ℓ₁ + ℓ₂ pattern (r3:552–554) is the natural candidate.
  - **(b) "Overwrite" is not a bijection.** The single-cell control has a record cell "which the next
    read overwrites" (r3:798). Under one bijection `φ` a read cannot overwrite, and `r ⊕= (x, y)` twice
    under identity dynamics returns the blank. Specify the bijective form, for example: swap the old
    record into an out-of-reach conveyor, then copy.
  - **(c) Optional.** OA-3 r3 N4 (OA-3 r3:384–406, a NEW finding against OA-2's effect class for
    heralded composites) bears on what "held = present `V`" admits. Fix variant (ii)'s effect class
    explicitly when the preregistration is drafted.
  - **(d) Optional.** `N₁` on `Z₇` is a non-bipartite ring (MECH-2:196). That is harmless for Theorem
    E, which is affine, but state the reason for `L = 7`.

### N7 and the bookkeeping hunks

- **TUNE-1 credit (r3:501–504).** Accurate. TUNE-1 self-labels as a WIP research record; [R] is right.
- **Status table (r3:845–858).** Consistent with the body except as D1, D3 and D8 note.
- **Snapshot.** Accurate at r3's pin `615cc119`.
  - `origin/main` has since moved to `911a5cb6`, and `papers/Main.md` changed at :36, :60, :90, :151,
    :700 and :724 (#1255; line count unchanged).
  - r3 cites Main:60 and :724, so a later revision re-checks those two quotations.
  - Not a defect of r3.

***

## 5. Overreach, labels and status text

- **NEW labels.** None was added, and the tally "No NEW finding" (r3:1015) stands. No §A.19 prior-art
  check is triggered.
  - The E1 generalization is the reviewer's [RW] (Rev2:167–169), credited as such.
  - It is ELABORATING of MECH-1 Corollary A′ and OA-1 D7.
- **Quantifier changes.**
  - "for any rule, affine or not, and any observer" (r3:569): supported (§4).
  - "for every `q`" (algebra, r3:652): supported.
  - "at odd `q` on MECH-1's [premises]" (r3:651): not supported as sourced (D3).
- **Effect classes.** B(ii)(⇒) silently assumes convex closure (D1). Elsewhere the delta adds no effect
  class.
- **Measure assumptions.** D1's repair (b) is measure-relative: an independent coin is native under μ-G
  only. r3:730 lists Proposition B as holding "for every law" under all three μ. That is right for
  (i) and (ii)(⇐), and for (ii)(⇒) only under repair (c).
- **Status text.**
  - r3 does not call itself reviewed. The Standing (r3:3–10) says "WIP / UNVERIFIED".
  - Stale item, **D10**: the Disclosure (r3:58) still says "No copy of any source was written at the
    working root **in r2**". State it for r3.
- **OA-1 r4-only dependence.** Of the OA-1 citations the delta adds or retains, only one range touches
  r4-only text.
  - OA1r4:556–572 (MP-1, r3:575) includes the r4 nit-2 sub-bullets at :563–572.
  - E1 uses only MP-1's statement (:557–558, r3 content), so it does not depend on the r4-only text.
  - Narrow the citation to :556–562.
  - D5's corrected target, :180–184, is r3 content.
- **Out-of-delta observation (optional).** The unchanged r3:581 quotes "does not by itself bear on gap
  3" as OA1r4:515. The words are in row 2, at :514.

***

## 6. Hunk accounting (24 hunks, `diff -u r2 r3`)

| # | r3 lines | Content | Disposition |
|---|---|---|---|
| 1 | 1–10 | Title, Standing (r3) | OK (D10 is in the Disclosure, which is unchanged) |
| 2 | 22–39 | Snapshot `615cc119`; `T1`, `Rev2` forms | OK, verified |
| 3 | 72–75 | §0.6 names (H3); §0.7 restated E1 | OK |
| 4 | 112–117 | C-PM′ scope | OK |
| 5 | 251–278 | B(ii) (⇐) detail, (⇒) proof, "what it does not give" | **D1** |
| 6 | 374–376 | Conveyor window sentence | OK |
| 7 | 388–403 | Horizon and resources | OK; **D7** |
| 8 | 407–411 | Claim 1 selector note | OK |
| 9 | 433–440 | Claim 2 step 3, C-PM | OK (label the alternative unchecked) |
| 10 | 492 | MECH-1:404–418 | OK |
| 11 | 501–504 | TUNE-1 Lemma A-T credit | OK, verified |
| 12 | 512 | E(b) heading, PM | OK |
| 13 | 519–525 | E(b) step 5 | OK; **D6** propagation |
| 14 | 536–537 | Verdict N2.4, PM | OK |
| 15 | 561–579 | Corollary E1 | Correct; **D5** |
| 16 | 634–652 | Class N at general `q`; premises by `q` | Algebra OK; **D3** |
| 17 | 747 | §4 row | OK |
| 18 | 756 | 𝔊_K premises | **D8** |
| 19 | 776–833 | Next-step-2 sketch | OK; **D9** |
| 20 | 848–858 | Status rows | Add D1's hypothesis to :848, D3 to :858, D8 to :853 |
| 21 | 891 | Pressure-test line | **D8** |
| 22 | 900–906 | Inventory, snapshots | OK |
| 23 | 940–946 | Inventory additions | Add MECH-1:572–597 if D3 is re-sourced |
| 24 | 958–962 | Limits | **D2**; **D8** |
| 25 | 994–1015 | §10 change map | Update N1 and N6 rows after the edits |

Rows 24 and 25 are parts of the last two hunks.

***

## 7. Required edits (exact)

**E1 (D1), required.**
- **At r3:241–242,** after "**iff** the restriction map … is injective", insert:
  > (the "only if" direction assumes the available effects are closed under convex mixing, with
  > convex-linear responses; see the proof).
- **At r3:268–269,** replace "Both are convex mixtures of available effects, so both are available
  effects with responses in `[0, 1]`." with:
  > **Hypothesis (CVX):** the available effects are closed under mixing with weights in `q^{−m}ℤ`,
  > realized by a coin independent of, and not read with, the prepared cells. `d` may be taken with
  > integer `c_i` (reachable laws and effects are rational), and `λ` may be taken as any `q^m` at least
  > the maximum, so these weights suffice. Under (CVX), `A` and `B` are available effects.
- **At r3:273,** replace step 7's first sentence with:
  > Averaged over the independent coin, the configuration model's response to `A − B` is `d/λ`, which
  > is nonzero at some point of `U`. So `A` and `B` have different responses on `U`.
- **After r3:278,** add:
  > Without (CVX) the direction fails: with `U = {a, b}`, one reachable law `(1/3, 2/3)` and
  > deterministic reads, no two distinct effects are equivalent while `ρ` is not injective.
- **At r3:730,** in §3.3, add: "(⇒) of B(ii) needs (CVX): native under μ-G (fresh bath cell); not
  established under μ-O and μ-R." Alternatively, adopt (CVX) as a convention of the fragment in §1.0
  and say so.
- **At r3:848,** append ", (⇒) under (CVX)".

**E2 (D2), required.** Replace r3:958–960 with:
> Proposition B(ii) is proved in both directions for the configuration model (N1), (⇒) under (CVX).
> (⇐) with (i) gives a noncontextual model of the prepare–measure fragment, as used in Theorem E(b)
> and the class-N result. (⇒) shows only that the configuration model is contextual; it does not decide
> non-embeddability, which needs a separate argument such as the counterexample.

**E3 (D3), required.** Either:
- **(a) Restrict.**
  - At r3:646–652, replace the odd-`q` bullets with: "The conclusion is stated at `q = 2`. The algebra
    holds for every `q`; the reachable-law premise at other `q` is not established here."
  - At r3:858, replace "and at odd `q` via MECH-1 Proposition C(d)" with "premises at `q = 2` only".

or
- **(b) Re-source.** Read MECH-1:572–597 and replace r3:649–651 with:
  > At odd prime `q`, for class N (not N+NNB) on a bipartite graph under P1–P2, MECH-1 Lemma S and
  > Corollary S (MECH-1:578–597) [R] exclude determined mixed functionals and, with isotropy, point
  > laws. Each one-cell branch marginal is uniform on a coset (TUNE-1 Lemma 0), so the reachable laws are
  > the uniform, `z`-level and `x`-level laws and their mixtures, and a single-cell read registers `z` or
  > `x`. Proposition C(d) is not used: inclusion in the epistricted theory does not imply that this
  > restricted fragment is noncontextual (compare N2.1's counterexample).
  - Update r3:858 and the inventory r3:923–927 to match.
  - Write "odd prime `q`" wherever "odd `q`" appears in this result.

**E4 (D4).** Replace r3:584 "Open exits that need no non-translational setting dependence." with:
> Open exits within the affine class, (H1) and (H3) kept:

At r3:585 add: "(H-AR fails, so settings translate the configuration but not the held record)".

**E5 (D5).** At r3:579, change "(OA1r4:198–204, D7)" to "(OA1r4:180–184; D7)". At r3:575, narrow
"OA1r4:556–572" to "OA1r4:556–562".

**E6 (D6).** At r3:150, append to G3's Content: "Assessed on the prepare–measure fragment, with every
procedure folded into a preparation or a measurement (Theorem E(b))." Then add "(prepare–measure)"
after "G3" at r3:704 and r3:868, and after "NO" at r3:955.

**E7 (D7).** At r3:396, replace "only after `M_r − 7` further shifts" with "only after `M_r − 7` further
shifts (`M_r − 6` after PREP(ℓ))". At r3:401 add: "and `4(K − 2) < M_r − 6` likewise".

**E8 (D8).** At r3:756, r3:853, r3:891 and r3:961–962, change "C-PM for the selector cells" to "C-PM
for the selector cells and the explicit mixture's coin". At r3:784–785, change "in 𝔊_K the label and
coin cells" to "in 𝔊_K the label and bath-coin cells".

**E9 (D9).**
- At r3:804–805, replace "so the variants coincide and validate both pipelines" with "so the variants
  coincide; this validates the shared pipeline only, and a variant-(ii)-specific positive control is to
  be designed in the preregistration".
- At r3:798, replace "which the next read overwrites" with "whose previous content the next read first
  swaps into an out-of-reach conveyor (a bijection)".
- At r3:439–440, mark the PREP variant as "[W], not recounted".

**E10 (D10).** At r3:58, change "in r2" to "in r2 or r3".

**E11.** Update §10 rows N1 and N6 (r3:1000, :1005) to match E1–E3.

None of E1–E11 moves a verdict. After E1–E3, r3 can be treated as final at this unit's level. Every
[W]/[RW] item remains an unreviewed hand derivation; none is kernel-checked, adopted or promoted.

***

**Disclosure.** Commands: `git fetch`, `git show`, `git diff`, `git ls-tree`, `git rev-parse`,
`git grep`, `git log`, `diff -u`, `grep`, `sed`, `cat -n`, `wc`. No script, no computation on OI
rules. Working copies of the six OA-2 files and the r2→r3 diff were written under `working/oa2/src/`
and `working/oa2/r2r3.diff`. Nothing was written at the working root.

***
***

# Recheck of r4 (`OA-2-REPORT-r4.md`)

**Standing.** Same reviewer and the same rules as above: read-only, paper-only, no commit, push or
GitHub write, and no file at the working root.

**Text checked.**
- `working/oa2/OA-2-REPORT-r4.md`, 1058 lines, git blob **`1b282d9a`**.
- Against r3, blob `f7ca0968…` (confirmed unchanged).
- Also read: `OA-2-r4-APPLY.md` and `working/oa2-r4-tools/apply.py`.
- `r4:n` is a line of the r4 blob.

## Verdict: **ACCEPT WITH NITS**

- **Edits applied faithfully.** Every applied E-edit is the review's §7 text, at the intended place.
- **No unexpected changes.** `diff r3 r4` shows nothing else changed except:
  - the Standing (r4) line;
  - the §11 change map, r4:1027–1058.
- **Three edits of mine were defective.**
  - E1's step-7 replacement left r3's step 6 in place, and it conflicts with the new step 7.
  - E1's §3.3 sentence overstated "native under μ-G".
  - E3(a)'s status-row text duplicates a phrase when applied literally.
- **R1–R12 below fix these.** They also supply the missing E6, E8 and E11 texts and the [RW] label
  change.
- **No further re-check is needed** if R1–R12 are applied verbatim and the r4→r5 diff shows only them.
  No verdict moves.

## A. Diff audit

| Edit | r4 location | Assessment |
|---|---|---|
| Standing | :3 | Replaced by R12 |
| E1 | :244–246, :272–275, :279–282, :286–287, :738, :857 | Text verbatim. Defects in my own E1, fixed by R1–R4 |
| E2 | :967–970 | Verbatim, correct |
| E3(a) | :659–660, :867 | :659–660 correct. :867 duplicates "premises at `q = 2`" (my error), fixed by R5 |
| E4 | :593–595 | Verbatim. The bold header and double parenthesis are acceptable |
| E5 | :584, :588 | Verbatim, correct. OA1r4:180–184 is D5's measure bullet, r3-era content |
| E6 | :152, :712, :964 | Correct. The `<br>` in the table cell is acceptable. The r3:868 target was my error; see R6 |
| E7 | :405, :410 | Correct. The comma is acceptable |
| E8 | :764, :793, :900 | Correct. The two remaining sites are in R7 |
| E9 | :449, :806, :813–814 | Correct. The parentheses are acceptable |
| E10 | :60 | Correct |
| §11 | :1027–1058 | Accurate record. Line references are r4's; E11 is supplied in R8 |
| Title | :1 | Still "(r3)"; see R9 |

## B. Rulings on the writer's choices

1. **E1 and §3.3: the writer is right.**
   - "Native under μ-G (fresh bath cell)" rests on my §2.3(b) argument and is not proved in r4.
   - The claim is also too strong for OI's native rules. A cell that is uniform, independent of the
     prepared cells and unread is supplied by design in 𝔊_K's bath. That an affine native rule supplies
     one is not shown.
   - The sentence also sits inside the first column of a row whose μ columns read "hold", which
     misreads as (⇒) holding under μ-O and μ-R. **R3 replaces it with a separate row.**
2. **E3, option (a), `q = 2` only, without mentioning Corollary S: accepted.**
   - This is the conservative choice.
   - The odd-prime recovery through MECH-1 Corollary S (§3.3 above) remains available to a later
     revision as [R]-premised work. It is not a claim of r4.
3. **Formatting.** The in-cell `<br>`, the bold E4 header, the E7 comma and the E9 parentheses are all
   accepted.
4. **Title "(r3)": must change** (R9).

## C. Defects found in the applied E1 text (my errors), now corrected

1. **Step 6 conflicts with the new step 7** (r4:278 vs :279–282).
   - Step 6 asserts `A − B = d/λ ≠ 0` on `U` as functions on the configuration.
   - When the coin is a cell of `S`, that is false: it holds only after averaging over the coin, which
     is what step 7 now says.
   - **R1** merges the two steps.
2. **Step 3's `λ := max(…)` is not compatible with (CVX)'s weights in `q^{−m}ℤ`.**
   - Example: coefficients `(3, 1)` give `λ = 3` and a weight of 1/3.
   - (CVX) says `λ` "may be taken as" `q^m`; steps 3–4 should use that choice. **R2.**
3. **The display's parenthesis names "convex-linear responses",** whereas the proof now uses coin
   averaging. **R2** points the display at (CVX).

## D. Main:60 and Main:724 against `origin/main` = `911a5cb6`

The changes since the pin `615cc119` (#1255) are wording: "determinism" becomes "injectivity", the
finite-capacity clause is added, and the rung list is rephrased. Every quotation r4 makes from these
lines still holds.

| r4 | Quoted content | At `911a5cb6` |
|---|---|---|
| :87 | `S` finite (Main:60; ledger (ii), Main:724) | Main:60 still says total finiteness of the representative is "carried as item (ii) of the posit ledger"; ledger (ii) is unchanged in substance. ✓ |
| :893 | Recurrence (Main:60) | Main:60 still states `φ^L = id` for the finite representative. ✓ |
| :92 | μ-R posited, ledger (iv) | (iv) is unchanged: "a standard but substantive epistemic postulate, not derived". ✓ |
| :172, :669 | Ledger (vii), (xiii), A5 | (vii) and (xiii) are unchanged. ✓ |
| :496, :923 | (xiv) | Unchanged. ✓ |
| :492 (not on the list sent to me) | Ledger (vii) | ✓ |

No edit is required. Optionally, add `911a5cb6` to the snapshot block with this result (R10).

## E. Does my derivation discharge [RW]?

**No.**
- r4:51 defines [RW] as "Reviewer's hand derivation, **re-derived here before use**". The following
  were supplied by me and adopted without re-derivation by the author:
  - (CVX);
  - the rational / `q^m` reduction;
  - the coin-averaging step;
  - the two-point counterexample.
- My own derivation (§2.2–2.3 above) and this recheck are by the same reviewer. They are not an
  independent check of the reviewer's text.
- **Two options.**
  - The author re-derives those items by hand; then "[RW, re-derived here]" stands.
  - Or the label changes as in **R11**.
- Either is acceptable. The E2 Limits text is a scope statement, not a derivation, and needs no label.

## F. Required edits to r4 (exact)

**R1 (steps 6–7).** Replace r4:278–282, from "6. Their ontic response functions differ" through
"measurement-contextual. ∎", with:
```
  6. Averaged over the independent coin, the response to `A − B` is `d/λ` as a function of the
     prepared cells, and `d/λ ≠ 0` on `U`.
  7. So `A` and `B` have different responses at some point of `U`: the configuration model gives two
     operationally equivalent effects different responses, so it is measurement-contextual. ∎
```

**R2 (step 3 and the display).**
- At r4:266, replace "Let `λ := max(Σ_P c_i, Σ_N |c_i|)`. It is positive, since `d ≠ 0`." with:
  > Let `λ` be a power `q^m` with `q^m ≥ max(Σ_P c_i, Σ_N |c_i|)`; the maximum is positive, since
  > `d ≠ 0`.
- At r4:244–246, replace "(the "only if" direction assumes the available effects are closed under
  convex mixing, with convex-linear responses; see the proof)" with:
  > (the "only if" direction assumes hypothesis (CVX), stated in the proof)

**R3 (§3.3).** Replace the row at r4:738 with two rows:
```
| Lemma 0, Proposition A, Lemma 1, Propositions B and C, except B(ii) (⇒) | hold (statements about every law) | hold | hold |
| Proposition B(ii) (⇒) | needs (CVX): holds where a cell uniform, independent of the prepared cells and not otherwise read serves as the coin (𝔊_K's bath is one); not shown for native rules | not established | not established |
```

**R4 (status row r4:857).** After "(⇒) under (CVX)", add "; (CVX) holds where an independent uniform
coin is available (§3.3)".

**R5 (r4:867).** Replace "(algebra for every `q`; premises at `q = 2`, premises at `q = 2` only)" with:
> (algebra for every `q`; premises at `q = 2` only)

**R5′ (r4:632–633).** Replace both lines with:
```
  - At odd prime `q`, MECH-1 Proposition C(d) places the reachable class of N and N+NNB inside the
    epistricted theory, which is a noncontextual model (MECH-1:751, :763–766). Inclusion does not by
    itself make a restricted fragment noncontextual (compare N2.1's counterexample).
```

**R6 (E6's missing site; my r3:868 target was wrong).** At r4:877, replace "It is the E3-level,
simplex-embedding corollary of" with:
> It is the E3-level, prepare–measure simplex-embedding corollary of

**R7 (E8's missing sites).**
- At r4:861, replace "under C-PM′ and C-PM (selector cells)" with:
  > under C-PM′ and C-PM (selector cells and the explicit mixture's coin)
- At r4:971–972, replace "and C-PM\n  for its selector cells (N3)" with:
  > and C-PM
  > for its selector cells and the explicit mixture's coin (N3)

**R8 (E11, §10 rows).**
- At r4:1010 (N1 row), append before the closing `|`:
  > . r4 adds hypothesis (CVX) to (⇒), merges steps 6–7, and restates the Limits line (§11)
- At r4:1015 (N6 row), replace "The premises are stated by `q`: `q = 2` per the [R] sources, odd `q`
  via MECH-1 Proposition C(d)" with:
  > The premises are stated at `q = 2`, per the [R] sources. r3's odd-`q` appeal to MECH-1
  > Proposition C(d) is withdrawn in r4 (§11, E3), because inclusion in the epistricted theory does
  > not decide this fragment
- Add R1–R12 as rows of §11, and delete §11's "Not applied" and "Open for the re-check" lists, which
  this recheck resolves.

**R9 (title, r4:1).** Change "# OA-2 (r3):" to "# OA-2 (r4):".

**R10 (optional, snapshot).** Add to the snapshot block:
> `origin/main` moved to `911a5cb6`. `papers/Main.md` changed at :36, :60, :90, :151, :700 and :724
> (#1255, wording). Every Main:60 and Main:724 quotation here was re-checked there and holds.

**R11 ([RW] label; required unless the author re-derives).**
- At r4:261, replace "(⇒) Proved in general [RW, re-derived here] (N1)." with:
  > (⇒) Proved under (CVX) (N1). Steps 1–5 are [RW], re-derived here. (CVX), the `q^m` choice of
  > `λ`, the coin-averaging steps 6–7 and the two-point example below are the reviewer's derivation
  > (`DELTA-REVIEW-OA-2-r3.md` §2.2–2.3), adopted without re-derivation; checked only by that
  > reviewer.
- At r4:857, change the Support cell "[W] + [RW]" to:
  > [W] + [RW]; (⇒)'s (CVX) steps reviewer-supplied, not re-derived here

**R12 (Standing, r4:3).** Replace "**Standing (r4).** r4 is WIP; its edits await a focused re-check."
with:
> **Standing (r4).** WIP / UNVERIFIED author report, revision r4. It applies edits E1–E10 of the
> focused delta review `DELTA-REVIEW-OA-2-r3.md` (verdict ACCEPT WITH CHANGES) and recheck edits
> R1–R11 of the same file's "Recheck of r4" (verdict ACCEPT WITH NITS). No verdict moved. r1–r3 are
> unchanged.

Use this R12 sentence only once the r4→r5 diff shows R1–R11 applied verbatim and nothing else.
Otherwise state "its recheck edits await verification".

**After R1–R12, what OA-2 r4 establishes is unchanged from the r3 review's summary, with two
changes.**
- Class N is now stated at `q = 2` only.
- B(ii)(⇒) is stated under (CVX).
- Every [W] and [RW] item remains an unreviewed hand derivation; none is kernel-checked, adopted or
  promoted.

***

# Confirmation of r4

**Text checked.**
- `working/oa2/OA-2-REPORT-r4.md`, 1067 lines, blob **`655480e9`**.
- Against the pre-recheck copy `.r4-pre-recheck.md`, blob `1b282d9a…`, which equals the r4 checked in
  "Recheck of r4".
- Read-only, as before.

## Verdict: **ACCEPT**, after one bookkeeping edit (C1)

### 1. Diff (`diff .r4-pre-recheck.md OA-2-REPORT-r4.md`)

- **Each R edit is my exact text, correctly placed.** This covers R1–R12, including R5′, R10 and R11
  (the relabel option).
- **Two line-break differences, both accepted.**
  - R2's display keeps the existing line breaks.
  - R2's step 3 wraps at "since".
- **R10's placement is right.** It sits in the snapshot block at :36–37, as a top-level bullet after the
  pins.
- **Nothing else changed,** apart from the R rows added to §11 and the deletion of §11's "Not applied"
  and "Open" lists, as R8 required.

### 2. §11 line numbers

- The rows cite pre-recheck line numbers under "Line numbers are r4's". They are now stale by up to 9
  lines. I did not intend that.
- **C1 (required).** Replace r4:1040–1067, from "Text of each applied edit" to the R12 row, with the
  block below. Its line numbers are those of blob `655480e9`, and were checked by grep against that
  blob.

```
Text of each applied edit is the review's text, verbatim (§7 for E-edits; "Recheck of r4" §F for
R-edits). Line numbers are those of this file after all edits.

| Edit | r4 location |
|---|---|
| **E1** (D1) | display :249–250 (as amended by R2); Hypothesis (CVX) :280–283; step 7 (merged by R1) :286–289; failure without (CVX) :293–294; §3.3 row (replaced by R3) :747; status row :866 |
| **E2** (D2) | Limits :976–979 |
| **E3** (D3), option (a) restrict to `q = 2` | :667–668; status row :876 |
| **E4** (D4) | :600–602 |
| **E5** (D5) | :591, :595 |
| **E6** (D6) | G3 row :157; §3.1 :720; Limits :973 |
| **E7** (D7) | :412, :417 |
| **E8** (D8) | :773, :802, :909 |
| **E9** (D9) | :456, :815, :822–823 |
| **E10** (D10) | :65 |
| **R1** (recheck §F) | steps 6–7 :286–289 |
| **R2** (recheck §F) | display :249–250; step 3 :273–274 |
| **R3** (recheck §F) | §3.3 rows :746–747 |
| **R4** (recheck §F) | status row :866 |
| **R5** (recheck §F) | status row :876 |
| **R5′** (recheck §F) | N2.5 :639–641 |
| **R6** (recheck §F) | §6 :886 |
| **R7** (recheck §F) | status row :870; Limits :980–981 |
| **R8** (recheck §F) | §10 rows N1 :1019 and N6 :1024; this table |
| **R9** (recheck §F) | title :1 |
| **R10** (recheck §F) | snapshot block :36–37 |
| **R11** (recheck §F) | (⇒) :265–268; status row :866, Support cell |
| **R12** (recheck §F) | Standing (r4) :3–6 |
```

- **The block has 28 lines, the same as the 28 it replaces.** The intro takes two lines instead of
  one, and the old separate "Standing (r4) sentence" row is folded into R12. No line cited above lies
  after the block, so the numbers stay valid.
- **Fallback if C1 is not used.** Change only the old r4:1040 sentence "Line numbers are r4's." to
  "Line numbers are r4's before the R-edits." The rows then read correctly, but they point at a text
  that is not on any record. C1 is preferred.

### 3. Standing (r4) sentence (r4:3–6)

- It stands as written once C1 is applied: it names E1–E10, R1–R11 and both verdicts.
- E11 needs no mention, because its content was supplied and applied as R8.
- C1 is a §11 bookkeeping change and touches no claim.
- **No further re-check is required,** provided the next diff shows C1, or the fallback, and nothing
  else.

### Unchanged

- No verdict moved.
- Class N is stated at `q = 2` only.
- B(ii)(⇒) is proved under (CVX), with its reviewer-supplied steps labelled as not re-derived.
- Every [W] and [RW] item remains an unreviewed hand derivation; none is kernel-checked, adopted or
  promoted.
