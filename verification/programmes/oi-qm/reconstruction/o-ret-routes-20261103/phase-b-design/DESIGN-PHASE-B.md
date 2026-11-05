# O-RET Phase B: the NRR-1 obstruction (paper record)

**Status: WIP / UNVERIFIED.** A paper-only negative record under the owner's ruling on Phase B
(#1032 c.6651202161, amaybaum, 2026-11-05T06:15:39Z): "Option 1, a paper-only negative analysis.
… Phase B is revised to document this obstruction, rather than to run a test whose outcome its
assumptions already determine." Every derivation in this record is a hand derivation and is **not
independently reviewed** in the form given here. None is an established result (AGENTS.md §A.46
items 1 and 3), and none is a premise of any other claim (§A.46 item 7). No computation,
enumeration, simulation, script, probe or Lean build was run for this record. **No Phase B run is
planned** (§8).

**The ruling's requirements and limits** (c.6651202161, quoted): "Correct the counting criterion,
and distinguish strict tautologies from genuinely informative controls. Record the SMR exclusions,
SS-2 and the related arguments as paper derivations, marking the new results unreviewed. Obtain
independent review of those derivations and of the resulting negative conclusion. Keep the narrower
scope: a negative for this rule, register, preparation and decoder family is not a universal no-go
theorem for OI retention. Record the remaining candidate families, and the smallest unresolved
ingredient a genuinely discriminating test would need." "**Not authorized:** Phase B freeze,
enumeration, execution, any new physical premise, or scientific promotion."

**Governing principle for tests** (owner, #1032 c.6649977592, amaybaum, 2026-11-05T04:49:59Z): "a
test must be able to fail even when all its declared assumptions hold. A positive result that a
decoder guarantees by construction cannot establish independent retention."

**Support labels.**
- **[PA]** Phase A evidence on `main`: the frozen inputs at `F = 49f0bd41` and `phaseA/run-1/`.
- **[DP]** `DESIGN-PULSE.md` r6, frozen at `F`. Its definitions are used as definitions. Its lemmas
  have no review record on `main` and are not used as premises.
- **[R]** `ROUTES.md` at `F`, read with `git show 49f0bd41:…/ROUTES.md`. Motivation only
  (programme `README.md:30–35`).
- **[MR]** the frozen MR-1 record `../measurement-record-formation/amendments/MR-star.md`.
- **[O]** an owner decision on #1032 or #914, quoted with its comment id.
- **[D]** a paper derivation recorded here; **not independently reviewed** unless stated otherwise.
  Where an earlier statement of the same argument was checked in a #1115 review comment, the comment
  is cited as provenance; it is not a review record on `main` and is not support.

`D:n`, `P:n`, `R:n`, `MR:n` are line numbers of `DESIGN-PULSE.md`, `PREREG-PHASE-A.md`, `ROUTES.md`
at `F`, and `MR-star.md`, at the drafting snapshot `D` = `f5c281ae`.

***

## 1. Summary

- **The obstruction [D].** For the family `𝔉` of §3.2 (the native-ready-register family NRR-1 on
  the rules K1 and SMR, with its laws, registers, preparations and decoders), no tuple takes a
  storage row of the Phase A classifier, for any window `T ≥ 1` and any deterministic decoder of the
  read cells. Each tuple either fails the storage condition ST on `W_T`, or fails J-1 at the first
  hold tick, which assigns row 1 before the storage step (Theorem N, §4.10). The bounds used are
  `≥ 1/4` throughout, so the same holds for every tolerance `ε* < 1/4`.
- **Consequence for a test.** A run of `𝔉` can yield only non-storage rows. It could check that an
  implementation agrees with the derivations of §4, but it cannot distinguish retained information
  from information passing through, because the outcome is fixed in advance on paper.
- **Scope.** The negative is established, if at all, only for the rules, registers, preparations,
  decoder class, readiness laws and classifier stated in §6.1. **It is not a universal no-go theorem
  for OI retention** (§6.2).
- **A more elementary obstruction [D].** Lemma SS-2 (§4.7): for any copy-form, centre-free rule and
  any one-site register whose current slice is fixed at `t₀`, J-1 at `t₀+1` forces the register's
  value at `t₀+2` to be independent of the carrier. Whether this extends to wider registers is open.
- **The counting criterion [D].** Relative to a stated comparison class (the free-map class, §5.2),
  a pass under decoder D2 is implied by D2's construction exactly when the window's inputs all
  occurred at the first hold tick: the syntactic flag `IP` (§5.3), with the caveats stated there.
  The relation-level flag `IP′` does not have this property (§5.4). The corrected criterion is §5.6.
  It acts on no tuple of `𝔉`, since none reaches storage.
- **Open families and the missing ingredient** (§7). The families not decided by §4 are listed. The
  smallest unresolved ingredient identified is a readiness law outside the site-level product class,
  on a register of width `≥ 2` into which the carrier enters non-additively, together with a paper
  analysis of its second hold tick and a reason for the law independent of this analysis.

***

## 2. Starting point

### 2.1 What Phase A established [PA]

- `phaseA/run-1/phase-a/summary.json` has `tuples_frozen` 49, 49 entries in `tuples_evaluated`,
  `verdict` `PASS`, `exit` 0 and `first_failure` null. `RESULT.md:42–43`: "`summary.json` has
  `verdict` PASS, `exit` 0, `first_failure` null, and 49 of 49 frozen tuples evaluated in the frozen
  order."
- Owner (RESULT.md:55–57): "The verified PASS establishes that the implementation agrees with its 49
  frozen calibration expectations. It does not establish physical retention in native OI dynamics or
  validate the classifier outside this test set."
- PREREG §9 (P:666–668): "A pass shows that the implementation and the hand algebra agree. It does
  not show that the criteria separate storage from transport on cases outside the set."
- Reproducibility: `REPLAY.json`, "Not replayed"; hash-seed independence "Not established"
  (`REPLAY.json:105`).

So the classifier (rows, precedence, DIL∃, J-1, the `G`-rule) is calibrated on 49 toy cases only. This
record uses its definitions, not any claim of its validity elsewhere.

### 2.2 What Phase B was to test

Phase A left open whether any in-corpus native step, with a declared register and a preregistered
starting law, gives a storage row that the classifier certifies with a test able to fail (#1032;
owner, c.6649977592). The design draft at `43370576` proposed NRR-1 (§3) for that test. The arguments of
§4, first stated in the #1115 reviews (c.6649925951, c.6650383732, c.6650681094, c.6650968100), show
that the family's outcome is fixed on paper.

***

## 3. The family examined, and what a storage row requires

### 3.1 Setting

- **Copy form.** A bijection `φ(x, y) = (y, G(y) − x)` on sites `Λ = ℤ/N`, each site `i` carrying a
  previous slice `x_i` and a current slice `y_i` in `𝔽₂`. `G_i` reads the current slice only and not
  `y_i` (centre-free). SM:106: "x_i(t+1) = f(neighbors of i at time t) − x_i(t−1)".
  - **K1:** `G_i(y) = y_{i−1} + y_{i+1}` (`MR:464–465`; the native step form of posit (vii),
    Main:726, here on a 1-D toy graph rather than the simple-cubic graph of posit (x)).
  - **SMR** (SM:112): `y′_i = y_{i−1} + y_{R(i,y)} − x_i`, `R(i, y) = i+2` if `y_{i+1} = 0`, else
    `i+1`. Over `𝔽₂` this is `y′_i = y_{i−1} ⊕ (y_{i+1} ∨ y_{i+2}) ⊕ x_i`. As physics it is the
    unadopted F2 extension E-SDC (state-dependent coupling realized by this switching rule); no
    independent consequence of the switching rule is identified, so E-SDC fails §A.29's
    hard-to-vary test as it stands.
- **Carrier.** `Σ` = site 0, both slices. `σ = κ = (x₀, y₀)(t₀)`, `μ_Σ` uniform, `P` = all four
  values, `f(σ) = c := y₀(t₀)`, so `m = 2`.
- **Law.** A product `μ = μ_Σ ⊗ ν` at `t₀`.
- **Register.** A fixed set `A` of sites with `0 ∉ A`. Locus `R = (x_A, y_A)` (both slices); read
  cells `y_A` (current slice; H-cur, declared). `Q := Par(R) ∖ R`, computed from `φ` on all of `S`,
  is the current slice of the structural outside neighbours of `A` (design amendment B-1 at
  `43370576`). The register update is written `R_{t+1} = f_R(R_t, Q_t)`.
- **Decoder.** Any deterministic function `g` of the read cells, fixed for the whole window. This
  class contains the rules D1 (Q8 exactly: the lexicographically least worst-case write-tick
  minimizer, #1032 c.6621961326), D1′ and D2 (§5.1).
- **Window.** `W_T = {t₀+1, …, t₀+1+T}`, hold ticks `H_T = {t₀+1, …, t₀+T}`, `T ≥ 1` (P:57). So
  `t₀+1` is a hold tick and `t₀+2 ∈ W_T` for every `T ≥ 1`.
- **Metrics** (P:79–80). `ε_max(t) = max_{σ∈P} μ(g(y_A(t)) ≠ f(σ) | σ)`. `TV_t` between
  preparation-conditioned readout laws.

**Lemma TV (an elementary bound) [D].** Fix `x₀`. If the readout's laws given `c = 0` and `c = 1`
differ in total variation by at most `δ`, every decoder, deterministic or randomized, has
`ε_max ≥ (1 − δ)/2`.
*Proof.* `μ(g ≠ 0 | c=0) + μ(g ≠ 1 | c=1) = μ₀(g = 1) + 1 − μ₁(g = 1) ≥ 1 − δ`, so the larger term is
at least `(1 − δ)/2`. ∎
A blind readout (`δ = 0`) gives `ε_max ≥ 1/2`. A readout in which `c` is masked with probability at
least 1/2 has `δ ≤ 1/2` and gives `ε_max ≥ 1/4`.

### 3.2 The family `𝔉`

| Component | `N = 5` | `N ∈ {7, 8}` |
|---|---|---|
| Rules | K1, SMR | K1, SMR |
| Registers | all 15 nonempty `A ⊆ {1, 2, 3, 4}` | all arcs `{a, …, a+w−1} ⊆ {1, …, N−1}`, `w ≤ 3` |
| Laws `ν` | `ν_r`, `r ∈ {−1, 0, 1, 2, ∞}` | `ν_r`, `r ∈ {−1, 0, 1, 2, ∞}`, and the one-sided laws `ν^{(a,b)}`, `a, b ∈ {0, 1, 2}` |
| Preparations | `P` all four carrier values | the same |
| Decoders | every deterministic decoder of `y_A` | the same |
| Windows | every `T ≥ 1` | the same |

- `ν_{−1} = π₀`, uniform on all non-carrier cells.
- For `0 ≤ r < ∞`, `ν_r` is uniform on the non-carrier cells conditioned on both slices of every site
  of `Z_r(A) := {i ≠ 0 : dist(i, A) ≤ r}` being 0. `ν_∞ = δ₀` on all non-carrier cells. At `N = 5`,
  `r = 2` gives `Z = {1, 2, 3, 4}` for every `A`, so `ν_2 = δ₀` there.
- The one-sided laws are those of the draft's alternative G-6 (c) at `43370576`: for an arc `A` on one
  side of the carrier, `Z = A ∪ {sites beyond A's far end within distance a} ∪ {sites on the other
  side of the carrier within distance b of site 0}`, both slices 0 on `Z`, all other non-carrier
  cells uniform.
- **Site-level laws.** Every law of `𝔉` other than `π₀` is *site-level with `A` ready*: each
  non-carrier site is, independently, either ready (both slices 0) or free (both slices uniform and
  independent), and every site of `A` is ready. `π₀` is site-level with every site free.
- `N = 5` with K1 is K-18(b). The ring sizes 5 and 8 are those of the draft; `N = 7` is the pairing
  the draft considered for robustness (its G-9 (a)).

### 3.3 What a storage row requires

From PREREG §4 (P:418–500) and DESIGN-PULSE §2.3 [DP, definitions]:
- Steps 2–4 precede the storage step. In particular, a failure of J-1 ((J-i) `Q_t ⫫ κ` jointly, or
  (J-ii) `κ ⫫ Q_t | R_t`, under `μ(·|σ∈P)`) at any hold tick assigns row 1 first.
- **ST** (step 6): `ε_max(t) ≤ ε*` at every `t ∈ W_T`, and either exact DIL∃ on `W_T`, or a
  nonempty consistent `G ⊆ 𝒬_{W_T}` whose Lemma H bound `ε_max(t₀+1) + Σ_{s∈H_T, s<t} η_s` is
  `≤ ε*` at every `t ∈ W_T`, with `η_s = max_σ μ(Q_s ∉ G | σ)`.
- Rows 5, 6 and the draft's locality row I-10 all require ST.

The conclusions of §4 use only J-1 at `t₀+1`, `ε_max` at `t₀+1` and `t₀+2`, exact DIL∃ and the Lemma H
bound at `t₀+2`. They do not depend on the draft's amendments B-2 to B-6, on `T*` or `w*`, or on any
counting rule. Lemma H [DP] is not used as a premise: only the definition of the bound is used.

***

## 4. Paper derivations [D, not independently reviewed]

Each item gives its hypotheses, its claim in one direction, and its proof. Provenance is the review
comment in which an earlier statement appeared; none of those comments is a review record on `main`.

### 4.1 Lemma PAD (the register's previous slice as a pad)

- *Provenance.* Draft `43370576` §1.3; checked on paper in #1115 c.6649925951 item 2.
- *Hypotheses.* A copy-form rule. Under `μ`, `x_A(t₀)` is uniform on `𝔽₂^A` and independent of
  `W := (y(t₀), x_{Λ∖A}(t₀))`, and `κ` is a function of `W`.
- *Claim.* `y_A(t₀+1)` is independent of `κ`: `TV_{t₀+1} = 0` and `ε_max(t₀+1) ≥ 1/2`.
- *Proof.* Given `W`, `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` is a fixed translate of a uniform variable
  independent of `W`, so it is uniform given `W`. Lemma TV with `δ = 0`. ∎
- *Use.* Every tuple of `𝔉` with `ν = π₀`.
- *Classification (§A.31).* CONFIRMING: DESIGN-PULSE Observation K (K-1) (D:151–155); R:314–315; the
  CN control (#1032 c.6567189236); P2-G (#914 c.6563955678 §2).

### 4.2 Lemma NP (the carrier's own site)

- *Provenance.* Draft `43370576` §1.3; checked in #1115 c.6650383732 §2.
- *Hypotheses.* A copy-form rule; a product law; `P` contains both values of `x₀` for some `c`.
- *Claim.* If `y_A(t₀+1)` depends on `c`, then `y₀ ∈ Q`, and J-i fails at `t₀+1` unless the law of
  `G₀(y(t₀))` is uniform.
- *Proof.*
  1. `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` depends on `σ` only through `y₀(t₀)`, so `y₀` is a structural
     parent of a cell of `y′_A`. Since `0 ∉ A`, `y₀ ∉ R`, so `y₀ ∈ Q`.
  2. `y₀(t₀+1) = G₀(y(t₀)) − x₀(t₀)`. `G₀` does not read `y₀` and reads no carrier cell, so under the
     product law its law `L_G` does not depend on `σ`.
  3. Given `σ`, `y₀(t₀+1)` has law `L_G` translated by `−x₀`. J-i implies `y₀(t₀+1) ⫫ κ`, so the
     translates by `0` and by `1` coincide, which over `𝔽₂` means `L_G` is uniform. ∎
- *Use.* Under `δ₀` on the non-carrier cells, `G₀ = 0`: every tuple whose readout depends on `c`
  fails J-i at `t₀+1`. This covers `r = ∞`, `r = 2` at `N = 5`, and every `N = 5` law equal to `δ₀`.
- *Classification.* ELABORATING: D-TRN (T-2)'s "carrier has left" applied to the carrier's own site.

### 4.3 Proposition AE (additive entry of the carrier)

- *Provenance.* The K1 case: #1115 c.6649925951 item 9(c), restated without an independence
  hypothesis in c.6650383732 §2 and checked there. The SMR right-side case: stated in c.6650383732
  §2, narrowed to `A ∌ N−2` in draft `43370576`, and checked for any product law in c.6650968100
  Task 2.
- *Hypotheses.*
  - (AE-1) A copy-form rule over `𝔽₂` whose register update has the form
    `f_R((x, y); q) = (y, H(y, q_rest) + q₀·b − x)`, where `q₀ := y₀`, `q_rest` is the rest of `Q`,
    `H` is any function, and `b ∈ 𝔽₂^A` is a fixed vector.
  - (AE-2) `μ = μ_Σ ⊗ ν` for any `ν`; `P` = all four carrier values.
  - (AE-3) The locus, read cells and `Q` of §3.1.
- *Claim.* For every deterministic decoder `g` and every `T ≥ 1`, either
  - (a) `ε_max(t₀+1) ≥ 1/2`, or
  - (b) exact DIL∃ fails on `W_T`, and every `G ⊆ 𝒬_{W_T}` for which `~_G` is consistent on
    `𝓛_{W_T}` has `η_{t₀+1} ≥ 1/2`, so the Lemma H bound at `t₀+2` is `≥ 1/2`.

  In either case ST fails.
- *Proof.*
  1. *Write structure.* `y_A(t₀+1) = H(y_A(t₀), q_rest(t₀)) + c·b − x_A(t₀) =: n + c·b`, and
     `x_A(t₀+1) = y_A(t₀) =: n_x`. Here `n` and `n_x` are functions of non-carrier cells only (`q₀`
     enters only through the term `q₀ b`), so their joint law does not depend on `σ`. The
     write-supported configurations are therefore `(n_x, n)` (with `c = 0`) and `(n_x, n + b)`
     (with `c = 1`), for every `(n_x, n)` in that support.
  2. *Case (a).* If `g(n) = g(n + b)` for every supported `n`, the decoded value at `t₀+1` equals
     `g(n)`, whose law does not depend on `c`. Lemma TV with `δ = 0` gives `ε_max(t₀+1) ≥ 1/2`.
  3. *Case (b): the join.* Otherwise fix a supported `(n_x, n)` with `g(n) ≠ g(n + b)`. For any `q`,
     let `ℓ* := (H(n_x, q_rest) + q₀ b − n, n_x) ∈ config(R)`. Then
     `f_R(ℓ*; q) = (n_x, H(n_x, q_rest) + q₀ b − H(n_x, q_rest) − q₀ b + n) = (n_x, n)` and
     `f_R(ℓ*; q + e_{y₀}) = (n_x, n + b)`. DIL∃'s relation is generated over all of `config(R)`
     (D:98–99). So any `G` containing both `q` and `q + e_{y₀}` joins `(n_x, n)` and `(n_x, n + b)`,
     two members of `𝓛_{W_T}` that decode differently, and `~_G` is inconsistent. The nonlinearity
     of `H` plays no role.
  4. *Translation.* Fix `c` and let `σ₀ = (0, c)`, `σ₁ = (1, c)`, both in `P`. The `y₀`-component
     of `Q_{t₀+1}` is `G₀(y(t₀)) − x₀`, where `G₀` reads neither `y₀` nor `x₀`. Every other component
     is `G_j(y(t₀)) − x_j(t₀)`, `j ≠ 0`, which may read `c` but not `x₀`. With `c` fixed in both, the
     law of `Q_{t₀+1}` given `σ₁` is the law given `σ₀` translated by `e_{y₀}`.
  5. *Exact DIL∃ fails.* By 4, `supp Q_{t₀+1}` contains `q` and `q + e_{y₀}` for some `q`, and
     `supp Q_{t₀+1} ⊆ 𝒬_{W_T}`. By 3, `~_{𝒬_{W_T}}` is inconsistent.
  6. *The bound.* Let `~_G` be consistent. By 3, `G` contains no pair `{q, q + e_{y₀}}`, so
     `1_G(q) + 1_G(q + e_{y₀}) ≤ 1` for every `q`. With `p := L(Q_{t₀+1} | σ₀)`, step 4 gives
     `μ(Q ∈ G | σ₀) + μ(Q ∈ G | σ₁) = Σ_q p(q)[1_G(q) + 1_G(q + e_{y₀})] ≤ 1`. Hence
     `μ(Q ∉ G | σ₀) + μ(Q ∉ G | σ₁) ≥ 1`, and `η_{t₀+1} ≥ 1/2`. The Lemma H bound at
     `t₀+2 ∈ W_T` is then `≥ 1/2 > ε*`. ∎
- *Instances.*
  - **K1, every register.** `y′_A = Adj_A y_A + B y_Q − x_A`, so (AE-1) holds with `H` linear and
    `b = B e_{y₀}`, the indicator of the sites of `A` adjacent to site 0. If `b = 0`, the readout does
    not depend on `c` and (a) holds. The proof uses no property of the ring.
  - **SMR, `A ∋ 1` and `A ∌ N−2, N−1`.** `y₀` is a structural parent of `y′_i` only for
    `i ∈ {1, N−2, N−1}`: as `y_{i−1}` for `i = 1` (additively, coefficient 1), inside
    `y_{i+1} ∨ y_{i+2}` for `i = N−1` and `i = N−2`. With `N−2, N−1 ∉ A`, (AE-1) holds with
    `b = e₁` and `H` nonlinear. This includes registers whose `Q` contains `y_{N−1}` (for example
    `N = 5`, `A = {1, 2}`), since `c` is fixed in `σ₀` and `σ₁`.
- *Corollary AE-D2 (decoder D2 on these tuples).* In case (b), `supp Q_{t₀+1}` contains a pair
  `{q, q + e_{y₀}}`, so D2's relation `~₁` (§5.1) contains the join of step 3 and merges two
  write-supported configurations that `g` decodes differently. D2 is then `undetermined`, and the
  draft's rule falls back to D1's values. This is shown for the AE instances only.
- *Not covered.* `q > 2`; laws that are not products; preparation sets without both `x₀` values;
  SMR registers containing `N−2` or `N−1`.

### 4.4 Proposition LS (SMR, registers on the left of the carrier, site-level laws)

- *Provenance.* Cases (i)–(iii) stated in #1115 c.6650681094 §4; checked, with the joint-leak repair
  in (i) and (iii-a), in c.6650968100 Task 2.
- *Hypotheses.* SMR over `𝔽₂` on `ℤ/N`, `N ≥ 7`. `A` an arc of width `≤ 3` in `{1, …, N−1}` with
  `A ∩ {N−2, N−1} ≠ ∅`. A site-level law with `A` ready (§3.2). `P` all four values.
- *Claim.* Every decoder has `ε_max(t₀+1) ≥ 1/4`, or J-1 fails at `t₀+1`.
- *Facts used.* Under such a law, ready sites contribute 0 and free sites independent uniform bits.
  `x_A(t₀) = y_A(t₀) = 0`. Since `N ≥ 7`, `1 ∉ A`. In cases (i) and (iii), `A ⊆ {N−3, N−2, N−1}`, so
  sites 1, 2, 3 are not in `A`; case (ii) uses only sites 1 and `N−1`.
  `y′₀ = y_{N−1} ⊕ (y₁ ∨ y₂) ⊕ x₀` and `y′₁ = y₀ ⊕ (y₂ ∨ y₃) ⊕ x₁`.
- *Proof.* The arcs split into three cases.
  - **(i) `A = {N−1}`** (the only such arc with `N−2 ∉ A`). `y′_{N−1} = y_{N−2} ⊕ (c ∨ y₁)`, and
    `Q = {y_{N−2}, y₀, y₁}`.
    - If site `N−2` is free, `y′_{N−1}` is padded by `y_{N−2}`: blind, `ε_max ≥ 1/2`.
    - If site `N−2` is ready and site 1 free, `y′_{N−1} = c ∨ y₁` masks `c` with probability 1/2:
      `δ ≤ 1/2`, `ε_max ≥ 1/4`.
    - If sites `N−2` and 1 are ready (so `x₁ = 0`), `y′₀ = y₂ ⊕ x₀` and `y′₁ = c ⊕ (y₂ ∨ y₃)`.
      - Site 2 ready: `y′₀ = x₀`, so J-i fails.
      - Site 2 free, site 3 free: `μ(y′₁ = c ⊕ 1) = 3/4`, so the law of `y′₁` depends on `c` and J-i
        fails.
      - Site 2 free, site 3 ready: `y′₁ = c ⊕ y₂` is marginally uniform, but
        `y′₀ ⊕ y′₁ = c ⊕ x₀`, so `(y′₀, y′₁)` is not independent of `κ`: J-i fails.
  - **(ii) `N−2 ∈ A`, `N−1 ∉ A`** (`A = {N−2}`, `{N−3, N−2}` or `{N−4, N−3, N−2}`). `c` enters the
    readout only through `y′_{N−2} = y_{N−3} ⊕ (y_{N−1} ∨ c) ⊕ x_{N−2}`; no other cell of `A` reads
    `y₀`.
    - If site `N−1` is free, then given `y_{N−1} = 1` the readout's law does not depend on `c`, even
      where another register cell reads `y_{N−1}`. So `δ ≤ 1/2` and `ε_max ≥ 1/4`.
    - If site `N−1` is ready, `y_{N−1} ∈ Q` and `y′_{N−1} = y_{N−2} ⊕ (c ∨ y₁) ⊕ x_{N−1} = c ∨ y₁`.
      Whether site 1 is ready (`= c`) or free (`μ(=1 | c=0) = 1/2`, `μ(=1 | c=1) = 1`), its law
      depends on `c`: J-i fails.
  - **(iii) `{N−2, N−1} ⊆ A`** (`A = {N−2, N−1}` or `{N−3, N−2, N−1}`). `y′_{N−1} = c ∨ y₁`,
    `y′_{N−2} = y_{N−3} ⊕ c`, `y₀, y₁ ∈ Q`, and `G₀ = y₁ ∨ y₂`.
    - By Lemma NP, J-i fails unless `y₁ ∨ y₂` is uniform. Under a site-level law that holds only if
      exactly one of sites 1, 2 is free (both ready gives 0; both free gives `μ(=1) = 3/4`).
    - **(iii-a) Site 1 ready, site 2 free.** `y′₁ = c ⊕ (y₂ ∨ y₃)`. If site 3 is free, its law
      depends on `c` and J-i fails. If site 3 is ready, `y′₁ = c ⊕ y₂` and `y′₀ = y₂ ⊕ x₀`, so
      `y′₀ ⊕ y′₁ = c ⊕ x₀` and J-i fails.
    - **(iii-b) Site 1 free, site 2 ready.** If `N−3 ∉ A` and site `N−3` is free, `y′_{N−2}` is
      padded and the readout carries `c` only through `c ∨ y₁`: `ε_max ≥ 1/4`. Otherwise
      `y′_{N−2} = c`, so `R_{t₀+1}` fixes `c`, and when `c = 0` it fixes `y₁ = y′_{N−1}`. Then
      `y′₀ = y₁ ⊕ x₀` determines `x₀` given `R_{t₀+1}`, while `x₀` is uniform given `R_{t₀+1}`: J-ii
      fails. ∎
- *Not covered.* Slice-level readiness (one slice of a site fixed, the other free); readiness to the
  value 1; correlated laws; a restricted carrier; `q > 2`; non-arc registers at `N ≥ 7`; registers
  whose sites are not all ready.

### 4.5 Observation U (SMR registers the carrier does not reach)

- *Claim [D].* For SMR, a register with `A ∩ {1, N−2, N−1} = ∅` has `y_A(t₀+1)` independent of `κ`
  under any product law: `TV_{t₀+1} = 0`, `ε_max(t₀+1) ≥ 1/2`.
- *Proof.* By §4.3's parent list, no cell of `y′_A` reads `y₀`, and none reads `x₀`. Under a product
  law the readout at `t₀+1` is a function of non-carrier cells. Lemma TV. ∎
- *Use.* `N = 5`: `{2}`. `N = 8`: `{2}, {3}, {4}, {5}, {2,3}, {3,4}, {4,5}, {2,3,4}, {3,4,5}`.
  `N = 7`: the arcs in `{2, 3, 4}`.

### 4.6 SMR at `N = 5`

- *Provenance.* The non-arc cases in #1115 c.6650968100 Task 2; the arc cases in draft `43370576`
  §6.4 and c.6650383732 §4. Re-derived here.
- `N−2 = 3`, `N−1 = 4`. At `t₀`:
  `y′₁ = c ⊕ (y₂ ∨ y₃) ⊕ x₁`, `y′₂ = y₁ ⊕ (y₃ ∨ y₄) ⊕ x₂`, `y′₃ = y₂ ⊕ (y₄ ∨ c) ⊕ x₃`,
  `y′₄ = y₃ ⊕ (c ∨ y₁) ⊕ x₄`, `y′₀ = y₄ ⊕ (y₁ ∨ y₂) ⊕ x₀`.
- `r = −1`: Lemma PAD. `r ∈ {2, ∞}`: the law is `δ₀`, Lemma NP. `{1}` and `{1, 2}`: Proposition AE at
  every `r`. `{2}`: Observation U.
- The remaining registers at `r ∈ {0, 1}` (`Z_0 = A`; `Z_1 = A` and its neighbours other than 0):

| `A` | `r = 0` | `r = 1` |
|---|---|---|
| `{3}` | `y′₃ = y₂ ⊕ (y₄ ∨ c)`, `y₂` free: blind | `Z = {2,3,4}`: `y′₃ = c`; `y′₄ = c ∨ y₁ ∈ Q` depends on `c`: J-i fails (case ii) |
| `{4}` | `y′₄ = y₃ ⊕ (c ∨ y₁)`, `y₃` free: blind | `Z = {3,4}`: `y′₄ = c ∨ y₁`, `y₁` free: `ε_max ≥ 1/4` |
| `{2,3}` | `y′₃ = y₄ ∨ c`, `y₄` free; `y′₂ = y₁ ⊕ y₄` is padded by `y₁`: `ε_max ≥ 1/4` | `δ₀`: Lemma NP |
| `{3,4}` | `G₀ = y₁ ∨ y₂`, both free, not uniform; the readout depends on `c` through `y′₄`: J-i fails (NP) | `Z = {2,3,4}`: case (iii-b) with site 2 ready: `y′₃ = c`, `y′₄ = c ∨ y₁`, `y′₀ = y₁ ⊕ x₀`: J-ii fails |
| `{2,3,4}` | `y′₂ = y₁`, `y′₃ = c`, `y′₄ = c ∨ y₁`, `Q = {y₀, y₁}`, `y′₀ = y₁ ⊕ x₀`, and `R` fixes `y₁`: J-ii fails | `δ₀`: Lemma NP |
| `{1,3}` | `(y′₁, y′₃) = (c ⊕ y₂, y₂ ⊕ (y₄ ∨ c))`: the information is in `c ⊕ (y₄ ∨ c)`, which is 0 if `c = 1` and `y₄` if `c = 0`: `δ = 1/2`, `ε_max ≥ 1/4` | `δ₀`: Lemma NP |
| `{1,4}` | `(y′₁, y′₄) = (c ⊕ (y₂ ∨ y₃), c ⊕ y₃)`: the two conditional laws are `{00: 1/4, 10: 1/4, 11: 1/2}` and `{11: 1/4, 01: 1/4, 00: 1/2}`, `δ = 1/2`, `ε_max ≥ 1/4` (attained) | `δ₀`: Lemma NP |
| `{2,4}` | `(y′₂, y′₄) = (y₁ ⊕ y₃, y₃ ⊕ (c ∨ y₁))`: the information is in `y₁ ⊕ (c ∨ y₁)`, which is 0 if `c = 0` and uniform if `c = 1`: `ε_max ≥ 1/4` | `δ₀`: Lemma NP |
| `{1,2,3}` | `y′₁ = c`, `y′₂ = y₄`, `y′₃ = y₄ ∨ c`; `Q = {y₀, y₄}`, `y′₀ = y₄ ⊕ x₀`, and `R` fixes `y₄`: J-ii fails | `δ₀`: Lemma NP |
| `{1,3,4}` | `y′₁ = c ⊕ y₂`, `y′₃ = y₂ ⊕ c`, `y′₄ = c`; `y′₀ = y₂ ⊕ x₀`, and `R` fixes `c` and `y₂`: J-ii fails | `δ₀`: Lemma NP |
| `{1,2,4}` | `G₀ = y₄ ⊕ (y₁ ∨ y₂) = 0`, `y′₀ = x₀`; the readout depends on `c` (`y′₁ = c ⊕ y₃`, `y′₂ = y₃`): J-i fails | `δ₀`: Lemma NP |
| `{1,2,3,4}` | `δ₀`: Lemma NP | `δ₀`: Lemma NP |

- For `r = 1`, the laws equal to `δ₀` are those of every register containing 1 and one of 3, 4, and
  of `{2, 3}`, `{2, 4}`, `{2, 3, 4}`: in each case `Z_1(A) = {1, 2, 3, 4}`.
- *Classification.* ELABORATING: case checks of AE, LS, NP and Lemma TV on one ring.

### 4.7 Lemma SS-2 (a ready one-site register at the second hold tick)

- *Provenance.* Stated in #1115 c.6650968100 Task 3. Not independently reviewed.
- *Hypotheses.* A copy-form rule, centre-free. A one-site register `A = {i}` with the two-slice locus
  and current-slice read. Under `μ(·|σ∈P)`, `y_i(t₀)` is almost surely constant. No product law, no
  condition on `P` beyond `f(P) = {0, 1}`, and no condition on the rule's linearity is needed.
- *Claim.* If J-i holds at `t₀+1`, then `y_i(t₀+2)` is independent of `κ`. So `TV_{t₀+2} = 0` and
  every decoder has `ε_max(t₀+2) ≥ 1/2`.
- *Proof.*
  1. `R = (x_i, y_i)`. `Par(x′_i) = {y_i} ⊆ R`, and `Par(y′_i)` is `x_i` together with the current
     slice of the structural neighbours of `i`, none equal to `i` (centre-free). So `Q` is that
     neighbour slice, and `G_i` reads only `Q`'s cells.
  2. `y_i(t₀+2) = G_i(y(t₀+1)) − x_i(t₀+1) = G_i(Q_{t₀+1}) − y_i(t₀)`.
  3. `y_i(t₀)` is constant, so `y_i(t₀+2)` is a function of `Q_{t₀+1}`. J-i at `t₀+1` gives
     `Q_{t₀+1} ⫫ κ`, so `y_i(t₀+2) ⫫ κ`. Lemma TV with `δ = 0`. ∎
- *Consequence.* `t₀+1 ∈ H_T` and `t₀+2 ∈ W_T` for every `T ≥ 1`. So a one-site register with a
  fixed current slice takes no storage row at any `T`, under any decoder: either J-1 fails at
  `t₀+1` (row 1), or ST fails at `t₀+2`. Every `ν_r` with `r ≥ 0` and every one-sided law fixes the
  register's slices, so SS-2 gives a second proof for every width-1 register of `𝔉`.
- *Mechanism.* In a copy-form step the register's previous slice at `t₀+1` is its own current slice
  at `t₀`. A ready current slice is therefore no pad at `t₀+1` (Lemma PAD's mechanism, one tick
  later), and a centre-free one-site update at `t₀+2` reads only inputs that J-1 has made
  carrier-independent.
- *Classification (§A.31).* ELABORATING Lemma PAD, one tick later. It constrains every candidate
  one-site current-slice register of a copy-form rule, beyond `𝔉`.
- *Open.* Whether the conclusion extends to registers of width `≥ 2`, where `G_i` also reads
  register cells that carry the record at `t₀+1`. No proof is given in either direction.

### 4.8 The slice-level shape on SMR's left side

- *Provenance.* Proposed as open in #1115 c.6650681094 §4; shown to fail at `t₀+2` in c.6650968100
  Task 4.
- *Shape.* `A = {N−1}`, `N ≥ 6`; site `N−2` ready; `y₁(t₀) = 0` with `x₁` free; site 2 free; every
  site outside offsets `−2…1` free, so site `N−3` is free. The register is ready. This law is not
  site-level, so Proposition LS does not cover it; it lies outside `𝔉`.
- *Claim [D].* `y_{N−1}(t₀+2)` is uniform given `σ`, so every decoder has `ε_max(t₀+2) ≥ 1/2`: no
  storage row at any `T`.
- *Proof.* By SS-2 when J-i holds at `t₀+1`, since the register's current slice is ready. Directly:
  `y_{N−1}(t₀+2) = y_{N−2}(t₀+1) ⊕ (y₀ ∨ y₁)(t₀+1) ⊕ y_{N−1}(t₀)`, with
  `y_{N−2}(t₀+1) = y_{N−3} ⊕ (y_{N−1} ∨ c) ⊕ x_{N−2} = y_{N−3} ⊕ c`. For `N ≥ 7`, `y_{N−3}(t₀)` enters
  no other term (`y′₀` reads sites `N−1, 1, 2`; `y′₁` reads sites 0, 2, 3 and `x₁`). At `N = 6`,
  `y_{N−3} = y₃` also enters `y′₁`, but `x₁` pads `y′₁` independently of `y₃`. In both cases
  `y_{N−1}(t₀+2)` is the free bit `y_{N−3}` added to a term independent of it given `σ`, so it is
  uniform given `σ`. ∎

### 4.9 Observation W1 (a restricted carrier on K1)

- *Provenance.* Draft `43370576` §1.3; checked in #1115 c.6649925951 item 3 with its scope
  corrected.
- *Instance.* K1 at K-18(b) (`ℤ/5`), background `δ₀`, `A` = sites 1–4, carrier previous slice
  restricted to 0 (`P = {(0,0), (0,1)}`; a restricted carrier, as in HC-K4, R:163–168, which
  restricts it to `x₀ = y₀`), decoder `OR(y₁, …, y₄)`.
- *Values.* `y(t₀+1) = (0, c, 0, 0, c)`, `y(t₀+2) = (c, 0, c, c, 0)`. At `T = 1`: DIL∃ holds, `τ = ∞`,
  SCH fails, storage step reached (row 6 before the draft's locality gate). At `T = 2`:
  `y₀(t₀+2) = c`, J-i fails, row 1.
- *Status.* Outside `𝔉`: its preparation set lacks `x₀ = 1`, which is what Proposition AE's
  translation uses. It is the one instance recorded for the open family O4 of §7.
- *Classification.* ELABORATING.

### 4.10 Theorem N (the scoped negative)

- *Status.* [D], assembled from §4.1–§4.7. **Not independently reviewed.** Not established (§A.46
  item 3).
- *Statement.* For every tuple of `𝔉` (§3.2), every `T ≥ 1` and every deterministic decoder `g` of
  the read cells fixed over `W_T`, one of the following holds:
  - J-1 fails at the hold tick `t₀+1`, so PREREG §4 step 2 assigns row 1; or
  - ST fails on `W_T` at every `ε* < 1/4`, in particular at `ε* = 1/20`.

  So no tuple of `𝔉` takes row 5, row 6 or the locality row I-10, under D1, D1′, D2 or any other
  fixed decoder, whatever `T*`, `w*` or counting rule is chosen.
- *Proof (coverage).* Every tuple falls under at least one item:

| Tuples | Item | Failure |
|---|---|---|
| `ν = π₀` (both rules, all `N`) | Lemma PAD | `ε_max(t₀+1) ≥ 1/2` |
| K1, every other law | Proposition AE (K1) | `ε_max(t₀+1) ≥ 1/2`, or Lemma H bound `≥ 1/2` and exact DIL∃ failing |
| SMR, `A ∋ 1`, `A ∌ N−2, N−1` | Proposition AE (SMR) | as above |
| SMR, `A ∩ {1, N−2, N−1} = ∅` | Observation U | `ε_max(t₀+1) ≥ 1/2` |
| SMR, `N ∈ {7, 8}`, arcs meeting `{N−2, N−1}`, every site-level law with `A` ready | Proposition LS | `ε_max(t₀+1) ≥ 1/4`, or J-1 fails at `t₀+1` |
| SMR, `N = 5`, the other registers | §4.6 (with PAD, NP, Lemma TV) | `ε_max(t₀+1) ≥ 1/4`, or J-1 fails at `t₀+1` |

  At `N ∈ {7, 8}` an arc of width `≤ 3` in `{1, …, N−1}` cannot contain both 1 and `N−2`, so each arc
  falls in exactly one of AE (SMR), U and LS. Every law of `𝔉` other than `π₀` is site-level with `A`
  ready (§3.2). `t₀+1 ∈ H_T` and `t₀+2 ∈ W_T` for every `T ≥ 1`. Each failure listed is either a
  J-1 failure at `t₀+1` or a violation of ST's `ε_max` clause or of both of ST's DIL∃ alternatives at
  `t₀+1` or `t₀+2`, with every bound `≥ 1/4`. ∎
- *What it does not use.* Lemma H's sufficiency direction, Lemma P, Lemmas S′, Q, L [R, DP], the
  draft's amendments B-2 to B-6, and any computation.
- *Classification (§A.31).* NEW for the planned test: a structural reason that the test's outcome is
  fixed by its own choice of laws, registers and preparations. It is not a new fact about OI dynamics
  beyond `𝔉` except through SS-2.

***

## 5. The counting criterion

### 5.1 Decoder D2 and the one-tick test

- **D2** (draft `43370576` §6.2). D1's values on the write-tick support; `~₁` is the equivalence on
  `config(R)` generated by `ℓ ~ f_R(ℓ, q)`, `q ∈ supp Q_{t₀+1}`; each read configuration in the
  `~₁`-class of a write-supported `ℓ` takes `g(ρ(ℓ))`; if two values are assigned to one read
  configuration, `d2_status = undetermined` and D1's values are used off the support.
- **Observation D2-T1 [D].** *Provenance:* draft `43370576` §1.3; checked in #1115 c.6650383732 §2.
  If `d2_status = consistent`, DIL∃ holds on `W₁` and `τ = ∞` on `W₁`.
  *Proof.* Every configuration in `supp R_{t₀+2}` is `f_R(ℓ, q)` with `ℓ ∈ supp R_{t₀+1}` and
  `q ∈ supp Q_{t₀+1}`, so every member of `𝓛_{W₁}` lies in the `~₁`-class of a write-supported
  configuration, and `𝒬_{W₁} = supp Q_{t₀+1}`. A consistent D2 makes `g∘ρ` constant on each such
  class, so no class holds two members of `𝓛_{W₁}` that decode differently. ∎
  It is the `T = 1` case of §5.3 (⇐).

### 5.2 The comparison class

With `φ`, the law and the decoder rule declared, a tuple's verdict is determined. "Guaranteed by
construction" and "able to fail with every declared assumption holding" therefore have content only
relative to a stated class of alternatives. The class used here:

**The free-map class `𝓕(φ)` [D].** Fix the tuple's law, carrier, register, locus and `Q`, and the
decoder rule D2. `𝓕(φ)` is the set of bijections `φ′` of `S` such that `φ′ = φ` on every state
whose `Q`-value lies in `supp Q_{t₀} ∪ supp Q_{t₀+1}`, and whose register map `f′_R` is a function of
`(R, Q)`.
- Everything D2 reads (`supp R_{t₀+1}`, `supp Q_{t₀+1}` and `f_R(·, q)` for `q ∈ supp Q_{t₀+1}`) is the
  same for every `φ′ ∈ 𝓕(φ)`, so D2's table and status are the same.
- The maps `f_R(·, q)` at inputs D2 never read are free.
- `φ′` need not be an in-corpus rule or copy-form. `𝓕(φ)` is a device for defining "implied by the
  decoder's construction", not a family of physical alternatives.

Other classes (for example, alternatives restricted to a parametrized family of rules, or ones that
vary the law and fix `φ`) define other flags; the definitions alone do not choose among them.

### 5.3 Proposition IP (the strict-tautology flag)

- *Provenance.* The flag `IP := (𝒬_{W_T} ⊆ supp Q_{t₀+1})` is the draft's checkpoint-3 flag
  (`5839e064`); the characterization is stated in #1115 c.6650968100 Task 1. **Not independently
  reviewed.**
- *Hypotheses.* `d2_status = consistent`, and `ε_max(t₀+1) < 1/2`, so `g∘ρ` is nonconstant on the
  write-tick support.
- *(⇐) If `IP` holds, the retention part of a storage verdict on `W_T` (exact DIL∃ on `W_T`, `τ = ∞`,
  and `ε_max(t) = ε_max(t₀+1)` on `W_T`) follows from D2's construction data and the input supports
  alone.*
  *Proof.* Under `IP`, `𝒬_{W_T} = supp Q_{t₀+1}`, so the window's relation `~_W` equals `~₁`. By
  induction, `R_{t+1} = f_R(R_t, Q_t)` with `Q_t ∈ 𝒬_{W_T}`, so every supported `R_t`, `t ∈ W_T`, is
  `~₁`-equivalent to a write-supported configuration. A consistent D2 makes `g∘ρ` constant on that
  class. So no class of `~_W` holds two members of `𝓛_{W_T}` decoded differently: DIL∃ holds, no hit
  exists (`τ = ∞`), and `g(R_{t+1}) = g(R_t)` on supported states, so `ε_max` is constant. Every step
  uses only data D2 read and the supports. ∎
- *(⇒) If some `q* ∈ 𝒬_{W_T}` lies outside `supp Q_{t₀} ∪ supp Q_{t₀+1}`, and `g∘ρ` is nonconstant
  on the image of `f_R(·, q*)`, then some `φ′ ∈ 𝓕(φ)` has the same D2 table and the same law, and
  under it exact DIL∃ fails on `W_T` and `τ < ∞`.*
  *Proof.*
  1. Let `t* ∈ H_T` be the first hold tick with `q* ∈ supp Q_{t*}`; `t* ≥ t₀+2`. Let `ℓ` be jointly
     supported with `q*` at `t*`.
  2. Pick `ℓ′` in the image of `f_R(·, q*)` with `g(ρ(ℓ′)) ≠ g(ρ(ℓ))`, and `ℓ̃` with
     `f_R(ℓ̃, q*) = ℓ′`. Let `π` swap the register configurations `ℓ` and `ℓ̃` on states with
     `Q = q*`, and fix every other state. Since `Q ∩ R = ∅`, `π` is a bijection of `S`, and so is
     `φ′ := φ∘π`. Then `f′_R(·, q) = f_R(·, q)` for `q ≠ q*`, and `f′_R(ℓ, q*) = ℓ′`.
  3. `φ′` differs from `φ` only on states with `Q = q*`, which have probability 0 at `t₀`, …,
     `t*−1`. So the state law at every tick up to `t*` is unchanged, D2's inputs and table are
     unchanged, and `φ′ ∈ 𝓕(φ)`.
  4. Under `φ′`, `ℓ ∈ supp R_{t*}` and `ℓ′ ∈ supp R_{t*+1}`, with `t*+1 ∈ W_T`. Both lie in
     `𝓛′_{W_T}`, `q* ∈ 𝒬′_{W_T}`, and `ℓ ~′ ℓ′` with different decoded values: exact DIL∃ fails.
  5. `ℓ` is reached from some write-supported `ℓ₀` through supported inputs. Either
     `g(ρ(ℓ)) ≠ g(ρ(ℓ₀))`, or `g(ρ(ℓ′)) ≠ g(ρ(ℓ₀))`; in both cases a hit exists and `τ < ∞`. ∎
- *Caveats.*
  - (C-1) The characterization is exact only relative to `𝓕(φ)` (§5.2).
  - (C-2) **Write-tick inputs.** (⇒) needs a new input outside `supp Q_{t₀}`. If every input of
    `𝒬_{W_T} ∖ supp Q_{t₀+1}` also occurs at the write tick, D2 has read part of `f_R(·, q*)` through
    `supp R_{t₀+1}`, and this record does not decide whether the pass is implied.
  - (C-3) **Realizability.** (⇒) needs `g∘ρ` nonconstant on the image of `f_R(·, q*)`. For a
    copy-form register `f_R(·, q)` is a bijection of `config(R)`, and the condition follows from the
    hypothesis `ε_max(t₀+1) < 1/2`.
  - (C-4) (⇒) states only that the retention part fails under some `φ′`. Under `φ′` other quantities
    (J-1 after `t*`, `ε` after `t*`) may change; no row under `φ′` is asserted.
  - (C-5) `IP` holds at every `T = 1`. So under D2 every `T = 1` pass is a strict tautology
    (D2-T1).

### 5.4 Flags that do not mark strict tautology

- **`IP′`** (draft `43370576` §1.3: every `~_W`-class meeting `𝓛_{W_T}` is a single `~₁`-class).
  - `IP ⇒ IP′`. So `IP′ = false` implies `IP = false`, and, under (C-2) and (C-3), that the pass was
    not implied.
  - `IP′ = true` does not imply a strict tautology. DT-S1q (§5.5) has `IP = false`, `IP′ = true`; its
    pass depends on `f_R(·, (0, 1)) = id`, a map D2 never read. `IP′` reads the hold-tick maps whose
    action the test examines, so it marks a pass as implied *because* the later hold ticks merged no
    classes, which is what static storage looks like.
  - `IP′` depends on unread cells of `R`. In the DT-S2s dynamics, `R = (r, s)` gives `IP′ = false`
    and `R = (r)` gives `IP′ = true`, with the same record in `r`.
- **`IP*`** (#1115 c.6650681094 §2: count a D2-consistent storage tuple iff its D1 row is the same
  storage row, or some window link joins members of `𝓛_{W_T}` with different read configurations in
  different `~₁`-classes). It asks whether D2's extension was tested, not whether the pass is
  implied. In the DT-S2s dynamics with `R = (r)`, `IP` holds (a strict D2 tautology) and `IP*`
  counts it through its D1 clause. Its second clause has no proof in either direction.

### 5.5 Controls: strict tautologies and informative cases

All are instances of route III's toy `M_F` (E-reg) and are calibration devices for the counting
criterion only. None is a Phase A tuple, and none bears on native retention. In `M_F`, each channel
cell carries presence bits and a value `v`; the gate acts at position 0 and the channel then shifts
(PREREG §3.1, S1). `Q` is the position-0 cell. `L = 3`, so the carrier's cell returns to position 0 at
`t₀+3`. The values below are hand derivations; those of DT-S13, DT-S1q and DT-S2s were checked on paper
in #1115 c.6650681094 §2 and c.6650968100 Task 1 (provenance).

| Control | Model and law | Decoder | `IP` | `IP′` | Values | Kind |
|---|---|---|---|---|---|---|
| DT-S13 | S1(3): if `p = 1`, swap `v ↔ r`; law uniform on `{p₂ = 0}`; `P` the two fired preparations; `T = 2` | D2 = D1, `g = r` | false | false | `ε = 0, 0, 1/4`; `TV = 1, 1, 1/2`; DIL∃ fails; `τ = 1`; J-1 holds at both hold ticks; `G*_{W₂} = {p = 0}`, consistent; row 2b | informative: fails with every declared assumption holding |
| DT-S1q | S1(3); law uniform on `{p₂ = 0, v₂ = 0, p₁ = 0}`; `T = 2` | D2 = D1, `g = r` | false | true | `ε = 0, 0, 0`; DIL∃ holds; `τ = ∞`; J-1 holds; SCH holds; row 5 | informative: a use-novel pass; its pass depends on `f_R(·, (0,1)) = id`, which D2 never read |
| DT-S2s | cells `(p, p′, v)`; if `p = 1` swap `v ↔ r`, else if `p′ = 1` swap `v ↔ s`; register `(r, s)`, read cell `r`; law uniform on `{p₂ = p′₂ = 0, p₁ = 0}`; `P = {(1,0,0), (1,0,1)}`; `T = 2` | D2 = D1, `g = r` | false | false | `ε = 0, 0, 0`; `TV = 1, 1, 1`; DIL∃ holds; `τ = ∞`; J-1 holds; SCH holds; `D = 3`; row 5 | informative in `𝓕(φ)`: had the `t₀+2` input swapped `v` into `r`, the check would have failed as in DT-S13 |
| DT-S2s′ | DT-S2s dynamics and law with `R = (r)`; then `Q = (p₀, v₀)` | D2 = D1, `g = r` | true | true | as DT-S2s; row 5 | **strict D2 tautology**; D1, which reads no hold-tick data, reaches the same row 5 independently |
| DT-SX | cells `(p, p′, v)`; register `(r₁, r₂)`, both read; if `p = 1`, `r₁ ← r₁ ⊕ v ⊕ r₂`; if `p′ = 1`, swap `r₁ ↔ r₂`; law uniform on `{p₂ = p′₂ = 0, p₁ = 0, r₁ = 0}`; `P = {(1,0,0), (1,0,1)}`; `T = 2` only | D1 = D2 = `r₁ ⊕ r₂` | false | false | `ε = 0, 0, 0`; `TV = 1, 1, 1`; DIL∃ holds; `τ = ∞`; J-1 holds; SCH holds vacuously; `D = 4`; row 5 | informative under every flag above |
| any D2 pass at `T = 1` | — | D2 | true | true | — | **strict D2 tautology** (D2-T1) |

- *Hand derivation of DT-SX [D, not independently reviewed; its values were stated and checked in
  #1115 c.6650681094 §2 and c.6650968100 Task 1].*
  - Write: at `t₀` position 0 holds the carrier `(1, 0, c)`, so `r₁ = 0 ⊕ c ⊕ r₂` with `r₂` uniform.
    The read configuration `(c ⊕ r₂, r₂)` ranges over all four values, and the unique zero-error
    decoder is `r₁ ⊕ r₂`, so D1 = D2 = `r₁ ⊕ r₂`.
  - `t₀+1`: the arriving cell is old cell 2, `(0, 0, v₂)`: no action. `supp Q_{t₀+1} = {(0,0,0), (0,0,1)}`,
    `f_R = id` there, and `~₁` is the identity.
  - `t₀+2`: the arriving cell is old cell 1, `(0, p′₁, v₁)` with `p′₁, v₁` uniform. When `p′₁ = 1` the
    swap preserves `r₁ ⊕ r₂`. So `ε = 0` at `t₀+1, t₀+2, t₀+3`, DIL∃ holds and `τ = ∞`.
  - `(0, 1, v)` lies in neither `supp Q_{t₀}` (whose cells have `p = 1`) nor `supp Q_{t₀+1}`: `IP`
    false, with (C-2) met. The swap joins the write-supported `10` and `01`, both decoded 1, across
    distinct `~₁`-classes: `IP′` and `IP*` false.
  - J-1 holds at both hold ticks: the arriving cells are old cells 2 and 1, independent of `(κ, R)`.
  - Each single read cell is independent of `κ` at `t₀+1` and `t₀+2`, so SCH holds only vacuously.
    The control does not separate static from circulating storage.
  - At `T = 3` the carrier's cell returns at `t₀+3` and J-i fails there. `D = 4` bits (`p₂`, `p′₂`,
    `p₁`, `r₁`).
- *Roles.* DT-S13 shows that the `T ≥ 2` step under D2 can fail with every declared assumption
  holding. DT-S1q, DT-S2s and DT-SX are use-novel passes: their retention part depends on hold-tick
  maps D2 did not read. DT-S2s′ and every `T = 1` D2 pass are strict tautologies under D2. These roles
  concern toy calibration models only.

### 5.6 The corrected counting criterion (recorded, not adopted)

For any later family, a storage row (5 or 6, with a nonempty environment) is counted as a test that
could have failed iff it is **use-novel**:
- **(U-1)** the same storage row is reached under D1, which reads no hold-tick data; or
- **(U-2)** it is reached under a consistent D2, and `𝒬_{W_T}` contains an input outside
  `supp Q_{t₀} ∪ supp Q_{t₀+1}` (so `IP` is false, with (C-2) met).

A D2 storage row with `IP` true and no D1 storage row is a strict tautology and never counts. A D2
storage row whose new inputs all lie in `supp Q_{t₀}` is reported as undecided by this criterion.
Using D1 alone (Q8 exactly) meets the governing principle with no flag, at the cost of rejecting
circulating storage whose invariant decoder differs from D1 (HC-SW, P:212–215).

Under this criterion DT-S1q, DT-S2s, DT-S2s′ (through U-1) and DT-SX count, and DT-S13 does not. The
verdict on the DT-S2s dynamics is the same for `R = (r)` and `R = (r, s)`. (U-1) carries the analogue
of (C-2) for D1: a hold-tick input that also occurs at the write tick was partly read by D1.

**On `𝔉` the criterion acts on no tuple**, since no tuple reaches a storage row (Theorem N).

***

## 6. Scope of the negative

### 6.1 Exactly what is claimed, and at what status

**Scope statement.** *For the rules K1 and SMR over `𝔽₂` on rings `ℤ/N` with `N ∈ {5, 7, 8}`; a
one-site carrier at site 0 (both slices), uniform, with all four preparations and `f = y₀(t₀)`; the
fixed declared registers of §3.2 (every nonempty `A ⊆ {1, …, 4}` at `N = 5`, arcs of width `≤ 3` in
`{1, …, N−1}` at `N ∈ {7, 8}`), with the two-slice locus and current-slice read; product starting laws
`ν_r`, `r ∈ {−1, 0, 1, 2, ∞}`, and, at `N ∈ {7, 8}`, the one-sided site-level laws of §3.2; every
deterministic decoder of the read cells fixed over the window (D1, D1′ and D2 included); and the Phase
A classifier's J-1 and ST at any `ε* < 1/4` (`1/20` included) and any `T ≥ 1`: no tuple takes a
storage row (Theorem N). Within this scope the classifier cannot certify retention, so a run of this
family cannot discriminate retained information from information passing through.*

- **Status.** A paper derivation, **not independently reviewed**, not established (§A.46 items 1, 3).
  The owner's ruling requires independent review of §4 and of this conclusion.
- **Wider statements inside §4 are the propositions' own hypotheses, not the negative's scope.**
  Proposition AE holds for K1 on any finite graph and any product law; Lemma SS-2 holds for any
  copy-form centre-free rule. They are recorded with those hypotheses, unreviewed, and the scope
  statement above does not extend to them.
- **Axis.** Consistency (§A.23). No correctness band moves. No premise is adopted.

### 6.2 Not a universal no-go theorem for OI retention

Theorem N says nothing about:
- other update rules (rule h, other copy-form rules in which the carrier enters non-additively
  everywhere, non-copy-form rules), `q > 2`, or K1 with other coupling constants;
- the native simple-cubic graph or `d = 3` dynamics for SMR-type rules, or rings other than
  `N ∈ {5, 7, 8}`;
- non-product laws, slice-level readiness, readiness to nonzero values, restricted carrier
  preparations, or laws in which the register's sites are not all ready;
- non-arc registers at `N ≥ 7`, registers wider than 3, moving, derived, state-selected or clocked
  registers, or readouts that change with the tick;
- decoders that are randomized or that change with the tick;
- other retention criteria, other loci or other tolerances `ε* ≥ 1/4`;
- observers, access mechanisms or sources of readiness (O1, O3, O4).

The failure of NRR-1 on `𝔉` is a failure of this construction, not an impossibility for every
observer-level or register-level extension (Code Review Rules, "Bridge and no-go scope").

***

## 7. Open families and the smallest missing ingredient

### 7.1 Families not decided by §4

| Id | Family | What §4 leaves open |
|---|---|---|
| O1 | SMR registers meeting `{N−2, N−1}`, of width `≥ 2`, under slice-level laws | LS needs site-level laws; AE does not apply (non-additive entry); SS-2 needs width 1. Not decided on paper. |
| O2 | One-site registers whose current slice is not fixed at `t₀`, with the previous slice restricted (slice-level) | PAD needs `x_A(t₀)` uniform; SS-2 needs `y_i(t₀)` constant. Not decided on paper, except the shape of §4.8. |
| O3 | Correlated (non-product) laws, on either rule | AE, NP and PAD use the product form. |
| O4 | Restricted carrier preparations (for example `x₀ = 0`, the draft's G-6 (b)) | AE's translation needs both `x₀` values. Observation W1 is one instance; it fails J-i at `T = 2`. The family restricts the independent preparations requirement 2 of #1032 asks for. |
| O5 | Readiness to nonzero values; `q > 2`; non-arc registers at `N ≥ 7` | LS uses ready = 0 and arcs; AE uses `q = 2`. |
| O6 | Other copy-form rules, including rule h (`|S| ≥ 2⁴⁸`, `INTERFACE-CONTRACT.md:35–36`) | Only PAD, NP and SS-2 apply; AE applies where the carrier enters additively. |
| O7 | Routes outside a fixed current-slice register of a copy-form step: state-selected access (route I, R:233–240), E-reg models (route III, R:421–426), derived, moving or clocked registers (requirement 1 of #1032; row 4 and Remark C) | Outside NRR-1; not examined here. |

The question that bears on O1, O2 and O6 at once is whether SS-2's `t₀+2` obstruction extends to
registers of width `≥ 2` under J-1 at `t₀+1` (§4.7, open).

### 7.2 The smallest unresolved ingredient

A genuinely discriminating test needs, frozen before any run, a family containing at least one tuple
whose storage verdict none of Lemma PAD, Lemma NP, Proposition AE, Proposition LS, Observation U or
Lemma SS-2 fixes. By §4, a fixed current-slice register of a copy-form rule escapes all six only if
**every** one of the following holds:
- its previous slice at `t₀` is not a uniform independent pad (PAD);
- `G₀(y(t₀))` is uniform, if J-1 is to hold at `t₀+1` (NP);
- the carrier enters its update non-additively or with a state-dependent coefficient, or the
  preparation set lacks both values of `x₀` for each `c`, or the law is not a product (AE);
- for SMR's left side, the law is not site-level (LS);
- it has width `≥ 2`, or its current slice is not fixed at `t₀` (SS-2).

The smallest ingredient identified that meets all five is family O1: a register of width `≥ 2` on
SMR's left side under a slice-level (or correlated) readiness law. Two things are missing before it
could serve:
1. **A paper analysis of its second hold tick**, in particular whether SS-2 extends to width `≥ 2`,
   so that the family is known, before the run, to contain a tuple whose outcome is open.
2. **A reason for the readiness law independent of this analysis.** A law shape chosen after the
   planned families were shown unable to pass is a variant fitted to escape these lemmas, with no
   independent prediction (§A.29). Without a source for it (the unsourced ready region of MR★ C-3,
   MR:1342), a positive could be at most a CONDITIONAL witness on E-SDC, H-sel and H-cur.

The specific slice-level shape of §4.8 is not such an ingredient: it fails at `t₀+2`.

***

## 8. Phase B run

**No Phase B run is planned.** The owner's ruling selects a paper-only negative and authorizes no
freeze, enumeration, execution, new physical premise or scientific promotion.

For the record, a run of `𝔉` under the draft's design at `43370576` could only:
- check that an implementation agrees with §4 on these instances (consistency-axis evidence, which
  could expose an error in §4 or in the implementation);
- tally which non-storage row removes each record (3w, 1, 2a, 2b, 3).

It could not establish anything about retention, or any negative beyond §4. The test specification
of the draft at `43370576` (decision rule, invariant table, output schema, budget and gate items G-1
to G-16) is provenance only.

***

## 9. Review packet

The owner's ruling requires independent review of the derivations and of the negative conclusion.
The reviewer is asked to check, at the exact head:
1. **Lemma TV and Lemma PAD** (§3.1, §4.1).
2. **Lemma NP** (§4.2), including its use for every `δ₀`-equal law.
3. **Proposition AE** (§4.3): the write structure; the join for nonlinear `H`; the translation by
   `x₀`; the bound `η_{t₀+1} ≥ 1/2`; the K1 and SMR right-side instances; Corollary AE-D2.
4. **Proposition LS** (§4.4): each case and sub-case, including the joint leak `y′₀ ⊕ y′₁ = c ⊕ x₀`,
   the `δ ≤ 1/2` bound in (ii), and the use of `N ≥ 7`.
5. **Observation U** (§4.5) and the parent list of SMR.
6. **The `N = 5` table** (§4.6), entry by entry, and the list of `δ₀`-equal laws at `r = 1`.
7. **Lemma SS-2** (§4.7) and its hypotheses.
8. **The slice-level shape** (§4.8), at `N = 6` and `N ≥ 7`.
9. **Theorem N** (§4.10): that the coverage table assigns every tuple of `𝔉` to an item, that every
   failure precedes or violates ST, and that every bound is `≥ 1/4`.
10. **The free-map class and Proposition IP** (§5.2–§5.3): both directions and caveats (C-1)–(C-5),
    in particular the swap construction of (⇒) and its realizability.
11. **§5.4**: the counterexamples to `IP′` and `IP*` as tautology flags.
12. **§5.5**: every control's values and role, in particular DT-SX's derivation and DT-S2s′ as a
    strict tautology.
13. **§5.6**: the criterion, and that it acts on no tuple of `𝔉`.
14. **§6**: that the scope statement claims nothing beyond §4, and that no sentence presents a
    universal no-go or an established result.
15. **§7**: that each listed family is in fact undecided by §4, and the five conditions of §7.2.
16. **§10**: each off-`main` reference and its classification.

***

## 10. References off `main`, and literature (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1032 c.6651202161 (amaybaum, 2026-11-05T06:15:39Z) | the owner's ruling: Option 1, its requirements and limits, quoted at the head | provenance; owner record quoted with author and time (§A.42 item 7) |
| #1032 c.6649977592 (amaybaum, 2026-11-05T04:49:59Z) | the governing principle, quoted at the head | provenance; owner record quoted with author and time |
| #1032 c.6649418760, c.6621961326, c.6622434587, c.6567189236, c.6610742427, c.6611966162, c.6612956983 | the Phase B design grant; Q8; the off-support decoder rule; the CN control; owner decisions on scope, access and `ε*` | provenance |
| #914 c.6563955678, c.6566997020 | P2-G; K-8 (H-cur declared) | provenance |
| #1115 c.6649925951, c.6650383732, c.6650681094, c.6650968100 | the reviews of the draft at `fdacce54`, `5839e064` and `43370576`; the first statements of AE (K1 and SMR), LS, the `N = 5` cases, SS-2, the slice-level failure, the strict-tautology characterization, `IP*` and DT-SX | provenance. Every argument used is re-derived in full here. Their unretained exact checks support no claim |
| Branch `research/o-ret-phaseb-design-20261105` at `43370576`, `fdacce54`, `5839e064` | the draft design (NRR-1, D1, D1′, D2, the one-sided laws, the controls DT-S13, DT-S2s, DT-S1q, Observation W1) | provenance; the definitions used are restated here |
| PR #1078 (closed) | the review history of `ROUTES.md` and DESIGN-PULSE | provenance; texts used are on `main` at `F`, labelled [R] and [DP] |
| `research/o-obsmu-20261104` at `f67b9f0c` | the name P-SDC for state-dependent coupling | provenance; E-SDC rests on SM:104 and SM:112 on `main` |

**Literature.** J. T. Lizier, M. Prokopenko, A. Y. Zomaya, arXiv:0811.2690v2, abstract page read
directly: local information storage and transfer in cellular automata; statistical, per-cell
measures. Toffoli and Margolus, *Cellular Automata Machines* (1987), on second-order reversible
rules: cited from memory, not re-read. Neither is used as support.
