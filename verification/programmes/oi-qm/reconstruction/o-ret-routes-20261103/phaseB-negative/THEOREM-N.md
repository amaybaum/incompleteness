# O-RET Phase B: Theorem N, the NRR-1 obstruction (landed paper record)

**Status.** A scoped paper negative for the family `𝔉` of §3.2, independently reviewed at exact head,
reviewed in `REVIEW.md` (this directory). No manuscript or correctness status changes; the recording
comment #1115 c.6652197336 notes scientific status unchanged.
- **Support.** Paper derivations only, marked [D]. No computation, enumeration, simulation or kernel
  check supports them.
- **Scope.** A negative for `𝔉` as stated in §6.1. **It is not a universal no-go for OI retention**
  (owner ruling, #1032 c.6651202161, amaybaum, 2026-11-05T06:15:39Z: "a negative for this rule,
  register, preparation and decoder family is not a universal no-go theorem for OI retention"). It
  sits on the consistency axis (AGENTS.md §A.23).
- **No premise is adopted.** E-SDC (SMR read as physics), `ν_r` (H-sel) and H-cur (declared access)
  stay labelled and unadopted, and nothing here is eligible as a premise beyond its proved scope
  (§A.46 item 7).
- **O4** (restricted carrier preparations) is recorded per owner ruling (a) (§4.9): a
  restricted-carrier mathematical test case with its restricted preparation stated, not an established
  physical-retention mechanism, not physically available without independent sourcing, and with its
  J-i failure at hold tick `t₀+2` stated.
- **No Phase B run** is planned or authorized (#1032 c.6651202161: "**Not authorized:** Phase B freeze,
  enumeration, execution, any new physical premise, or scientific promotion").
- **Accountable Issue:** #1032 (O-RET). **Provenance:** #1115 and its branch
  `research/o-ret-phaseb-design-20261105`.

**Source.** This file is an extract of `phase-b-design/DESIGN-PHASE-B.md` (DPB) at
`4b4cacc93884039afadd0069373b0ac448761a6b` on that branch, sha256
`22cdae48f345760323778e7d080124118c508c5e0600f5008f1c4d43f22cf023`: DPB 105–270, 275–458, 624–741 and
a reference table rebuilt from DPB 790–806. Section numbers are DPB's. "The draft" means the design
draft at `43370576` on the same branch, which defined the family NRR-1; `𝔉` (§3.2) is NRR-1 with the
ring size `N = 7` and the one-sided laws the draft considered. Draft-only terms are glossed where
they occur. Not carried: DPB §1, §2, §5 (decoder D2, Proposition IP, the calibration controls, an
unadopted counting criterion), §8 and §9, Corollary AE-D2 (DPB 271–274) and the E-SDC §A.29
assessment (DPB 116–119); no claim here uses them. The passages are verbatim except
for these adaptations:
1. this header replaces DPB 1–41;
2. section numbers are kept, so no heading or internal reference is renumbered;
3. DPB 116–119 are cut after the E-SDC label; the decoder sentence at DPB 127–129 keeps its first
   sentence only; the decoder-rule names D1, D1′ and D2 are removed at DPB 433 and 633;
4. Corollary AE-D2 (DPB 271–274) is removed;
5. one-line glosses with `43370576` as provenance for B-1, I-10, the amendments B-2 to B-6, G-6 (b),
   G-6 (c), G-9 (a) and the draft's locality gate;
6. W1's status, O4's row and the O4 paragraph are restated per owner ruling (a), which is quoted in
   §4.9; DPB 417–419 are kept verbatim;
7. the status lines at DPB 426–427 and 638–639 are replaced, and the "not independently reviewed"
   labels removed, since `REVIEW.md` covers every [D] item kept;
8. line locators `D:n`, `P:n`, `R:n`, `MR:n` refer to `DESIGN-PULSE.md`, `PREREG-PHASE-A.md`,
   `ROUTES.md` at `F = 49f0bd41` and `MR-star.md`, as at `f5c281ae`; they are unchanged at the landing
   base `53a3eb3d`, where those files are identical;
9. the reference table (§10) is rebuilt to the references this file cites;
10. at DPB 661, "(O1, O3, O4)" is retargeted to the DESIGN-PULSE obligations (D:32–37).

**Support labels.** [PA] Phase A evidence on `main`; [DP] `DESIGN-PULSE.md` r6, definitions only;
[R] `ROUTES.md` at `F`, motivation only (programme `README.md:30–35`); [MR] the frozen MR-1 record
`../../measurement-record-formation/amendments/MR-star.md`; [O] an owner record quoted with its comment
id; [D] a paper derivation recorded here.

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
    unadopted F2 extension E-SDC (state-dependent coupling realized by this switching rule).
- **Carrier.** `Σ` = site 0, both slices. `σ = κ = (x₀, y₀)(t₀)`, `μ_Σ` uniform, `P` = all four
  values, `f(σ) = c := y₀(t₀)`, so `m = 2`.
- **Law.** A product `μ = μ_Σ ⊗ ν` at `t₀`.
- **Register.** A fixed set `A` of sites with `0 ∉ A`. Locus `R = (x_A, y_A)` (both slices); read
  cells `y_A` (current slice; H-cur, declared). `Q := Par(R) ∖ R`, computed from `φ` on all of `S`,
  is the current slice of the structural outside neighbours of `A` (design amendment B-1 at
  `43370576`, provenance: the locus convention defined in this sentence). The register update is written `R_{t+1} = f_R(R_t, Q_t)`.
- **Decoder.** Any deterministic function `g` of the read cells, fixed for the whole window.
- **Window.** `W_T = {t₀+1, …, t₀+1+T}`, hold ticks `H_T = {t₀+1, …, t₀+T}`, `T ≥ 1` (P:57). So
  `t₀+1` is a hold tick and `t₀+2 ∈ W_T` for every `T ≥ 1`.
- **Metrics** (P:79–80). `ε_max(t) = max_{σ∈P} μ(g(y_A(t)) ≠ f(σ) | σ)`. `TV_t` between
  preparation-conditioned readout laws.

**Lemma TV (an elementary bound) [D].** Let `σ, σ′ ∈ P` with `f(σ) = 0` and `f(σ′) = 1`. If the
readout's laws given `σ` and given `σ′` differ in total variation by at most `δ`, every decoder,
deterministic or randomized, has `ε_max ≥ (1 − δ)/2`.
*Proof.* `μ(g ≠ 0 | σ) + μ(g ≠ 1 | σ′) = μ_σ(g = 1) + 1 − μ_{σ′}(g = 1) ≥ 1 − δ`, so the larger term
is at least `(1 − δ)/2`. ∎
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
- The one-sided laws are those of the draft's alternative G-6 (c) at `43370576` (provenance; defined here): for an arc `A` on one
  side of the carrier, `Z = A ∪ {sites beyond A's far end within distance a} ∪ {sites on the other
  side of the carrier within distance b of site 0}`, both slices 0 on `Z`, all other non-carrier
  cells uniform.
- **Site-level laws.** Every law of `𝔉` other than `π₀` is *site-level with `A` ready*: each
  non-carrier site is, independently, either ready (both slices 0) or free (both slices uniform and
  independent), and every site of `A` is ready. `π₀` is site-level with every site free.
- `N = 5` with K1 is K-18(b). The ring sizes 5 and 8 are those of the draft; `N = 7` is the pairing
  the draft considered for robustness (its G-9 (a) at `43370576`, provenance: pairing `N = 8` with
  `N = 6` or `7` when comparing ring sizes).

### 3.3 What a storage row requires

From PREREG §4 (P:418–500) and DESIGN-PULSE §2.3 [DP, definitions]:
- Steps 2–4 precede the storage step. In particular, a failure of J-1 ((J-i) `Q_t ⫫ κ` jointly, or
  (J-ii) `κ ⫫ Q_t | R_t`, under `μ(·|σ∈P)`) at any hold tick assigns row 1 first.
- **ST** (step 6): `ε_max(t) ≤ ε*` at every `t ∈ W_T`, and either exact DIL∃ on `W_T`, or a
  nonempty consistent `G ⊆ 𝒬_{W_T}` whose Lemma H bound `ε_max(t₀+1) + Σ_{s∈H_T, s<t} η_s` is
  `≤ ε*` at every `t ∈ W_T`, with `η_s = max_σ μ(Q_s ∉ G | σ)`.
- Rows 5, 6 and the draft's locality row I-10 all require ST. (I-10, at `43370576`, provenance: a
  storage row whose environment outside `Σ`, the sites of `R` and the sites of `Q` is empty.)

The conclusions of §4 use only J-1 at `t₀+1`, `ε_max` at `t₀+1` and `t₀+2`, exact DIL∃ and the Lemma H
bound at `t₀+2`. They do not depend on the draft's amendments B-2 to B-6 (at `43370576`, provenance: its write
gate, decoder rule, locality gate, handling of `T*` and `w*`, and guard for PREREG's exit 4), on
`T*` or `w*`, or on any counting rule. Lemma H [DP] is not used as a premise: only the definition of the bound is used.

***

## 4. Paper derivations [D]

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

- *Provenance.* Stated in #1115 c.6650968100 Task 3.
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
  register's slices, so SS-2 gives a second proof for every width-1 register of `𝔉` under every law
  other than `π₀`.
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
- *Locality gate.* The draft's locality gate (at `43370576`, provenance) relabels a storage row whose
  environment is empty as I-10.
- *Status.* Outside `𝔉` by definition: `𝔉` requires all four preparations, and this preparation set
  lacks `x₀ = 1`, which is what Proposition AE's translation uses. It is the one instance recorded for
  the open family O4 of §7, and §4 leaves O4 undecided beyond it. The `T = 1` outcome is a
  one-hold-tick toy outcome under an imposed preparation, and is not evidence of retention.
- *Owner ruling (a)* (amaybaum, Claude Code session chat, 2026-11-05; recorded in #1115
  c.6652197336, 2026-11-05T07:19:55Z): "Accept O4 as a restricted-carrier mathematical test case,
  but not as an established physical-retention mechanism. Its restricted preparation must be
  explicit, and it cannot be treated as physically available without independent sourcing. Its
  failure to maintain the required retention condition at the later tick must also remain visible."
  The restricted preparation is `P = {(0,0), (0,1)}`: `x₀(t₀) = 0` fixed, `c` free. The failure is
  J-i at hold tick `t₀+2`.
- *Classification.* ELABORATING.

### 4.10 Theorem N (the scoped negative)

- *Status.* [D], assembled from §4.1–§4.7: a scoped paper negative for `𝔉`, independently reviewed
  at exact head, reviewed in `REVIEW.md` (this directory); no manuscript or correctness status
  changes.
- *Statement.* For every tuple of `𝔉` (§3.2), every `T ≥ 1` and every deterministic decoder `g` of
  the read cells fixed over `W_T`, one of the following holds:
  - J-1 fails at the hold tick `t₀+1`, so PREREG §4 step 2 assigns row 1; or
  - ST fails on `W_T` at every `ε* < 1/4`, in particular at `ε* = 1/20`.

  So no tuple of `𝔉` takes row 5, row 6 or the locality row I-10, under any fixed decoder, whatever `T*`, `w*` or counting rule is chosen.
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

## 6. Scope of the negative

### 6.1 Exactly what is claimed, and at what status

**Scope statement.** *For the rules K1 and SMR over `𝔽₂` on rings `ℤ/N` with `N ∈ {5, 7, 8}`; a
one-site carrier at site 0 (both slices), uniform, with all four preparations and `f = y₀(t₀)`; the
fixed declared registers of §3.2 (every nonempty `A ⊆ {1, …, 4}` at `N = 5`, arcs of width `≤ 3` in
`{1, …, N−1}` at `N ∈ {7, 8}`), with the two-slice locus and current-slice read; product starting laws
`ν_r`, `r ∈ {−1, 0, 1, 2, ∞}`, and, at `N ∈ {7, 8}`, the one-sided site-level laws of §3.2; every
deterministic decoder of the read cells fixed over the window; and the Phase
A classifier's J-1 and ST at any `ε* < 1/4` (`1/20` included) and any `T ≥ 1`: no tuple takes a
storage row (Theorem N). Within this scope the classifier cannot certify retention, so a run of this
family cannot discriminate retained information from information passing through.*

- **Status.** A scoped paper negative for `𝔉`, independently reviewed at exact head, reviewed in
  `REVIEW.md` (this directory); no manuscript or correctness status changes.
- **Wider statements inside §4 are the propositions' own hypotheses, not the negative's scope.**
  Proposition AE holds for K1 on any finite graph and any product law; Lemma SS-2 holds for any
  copy-form centre-free rule. They are recorded with those hypotheses, and the scope
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
- read sets other than the current slice (H-cur);
- other carriers or record functions `f`;
- other retention criteria, other loci or other tolerances `ε* ≥ 1/4`;
- observers, access mechanisms or sources of readiness (DESIGN-PULSE obligations O1, O3 and O4,
  D:32–37).

The failure of NRR-1 on `𝔉` is a failure of this construction, not an impossibility for every
observer-level or register-level extension (Code Review Rules, "Bridge and no-go scope").

***

## 7. Open families and the missing ingredient

### 7.1 Families not decided by §4

| Id | Family | What §4 leaves open |
|---|---|---|
| O1 | SMR registers meeting `{N−2, N−1}`, of width `≥ 2`, under slice-level laws | LS needs site-level laws; AE does not apply (non-additive entry); SS-2 needs width 1. Not decided on paper. |
| O2 | SMR one-site registers `{N−2}`, `{N−1}` (and one-site registers of other rules with non-additive carrier entry) whose current slice is not fixed at `t₀`, with the previous slice restricted (slice-level) | PAD needs `x_A(t₀)` uniform; SS-2 needs `y_i(t₀)` constant; AE and U decide every other one-site register of K1 and SMR under product laws. Not decided on paper, except the shape of §4.8. |
| O3 | Correlated (non-product) laws, on either rule, except width-1 registers with a fixed current slice, decided by SS-2 for any law | AE, NP, PAD and U use the product form. |
| O4 | Restricted carrier preparations (for example `x₀ = 0`, the draft's alternative G-6 (b) at `43370576`, provenance), outside `𝔉` by definition | A restricted-carrier mathematical test case (owner ruling (a), §4.9): its preparation is restricted (`x₀(t₀)` fixed), and it is not physically available without independent sourcing. AE's translation needs both `x₀` values. Observation W1 is one instance; it fails J-i at hold tick `t₀+2` (`T = 2`). §4 leaves O4 undecided beyond W1. The family restricts the independent preparations requirement 2 of #1032 asks for. |
| O5 | SMR registers of width `≥ 2` meeting `{N−2, N−1}` outside LS's hypotheses (non-arc registers, arcs wider than 3, or `N = 6`), under the preregistered `ν_r` or under readiness to nonzero values; and `q > 2`, for both rules | LS needs arcs of width `≤ 3`, `N ≥ 7` and ready = 0; AE needs `q = 2`. Readiness to nonzero values and non-arc registers are open only for SMR registers meeting `{N−2, N−1}`: AE and U decide every other register under any product law. Width-1 registers are decided by SS-2 (or PAD under `π₀`). |
| O6 | Other copy-form rules, including rule h (`|S| ≥ 2⁴⁸`, `INTERFACE-CONTRACT.md:35–36`) | Only PAD, NP and SS-2 apply; AE applies where the carrier enters additively. |
| O7 | Routes outside a fixed current-slice register of a copy-form step: state-selected access (route I, R:233–240), E-reg models (route III, R:421–426), derived, moving or clocked registers (requirement 1 of #1032; row 4 and Remark C) | Outside NRR-1; not examined here. |

The question that bears on O1, O5 and O6 is whether SS-2's `t₀+2` obstruction extends to registers
of width `≥ 2` under J-1 at `t₀+1` (§4.7, open). For O2 the open question is instead a one-site
register whose current slice is not fixed at `t₀`.

### 7.2 The unresolved ingredient

A genuinely discriminating test needs, frozen before any run, a family containing at least one tuple
whose storage verdict none of Lemma PAD, Lemma NP, Proposition AE, Proposition LS, Observation U and
Lemma SS-2 fixes (Lemma TV is the bound inside several of them). A tuple escapes a lemma only by
failing at least one of its hypotheses, or, for NP, by meeting its exception. So a fixed
current-slice register of a copy-form rule escapes all six only if it fails at least one hypothesis
of each:
- **PAD:** its previous slice `x_A(t₀)` is not uniform and independent of `(y(t₀), x_{Λ∖A}(t₀))`;
- **NP:** where NP's hypotheses hold (a product law, and both values of `x₀` in `P` for some `c`),
  `G₀(y(t₀))` is uniform, if J-1 is to hold at `t₀+1`; otherwise NP's hypotheses fail;
- **AE:** the carrier enters the register's update non-additively or with a state-dependent
  coefficient, or the law is not a product, or `P` lacks both values of `x₀` for each `c` (the proof
  needs both values for only some `c`), or the value group is not `𝔽₂` (`q > 2`);
- **LS** (it applies only to SMR registers meeting `{N−2, N−1}`): the register is not an arc of width
  `≤ 3`, or `N < 7`, or the law is not site-level with `A` ready, or `P` is not all four values, or the
  value group is not `𝔽₂` (`q > 2`), or the rule is not SMR;
- **U:** some cell of `y′_A` reads `y₀`, or the law is not a product;
- **SS-2:** the register has width `≥ 2`, or its current slice is not fixed at `t₀`.

**Escape routes.** The combinations found, each listed in §7.1:
- **O1, a law outside the site-level class.** An SMR register of width `≥ 2` meeting `{N−2, N−1}`,
  within LS's arc, width and `N` hypotheses, under a slice-level or correlated readiness law. It fails
  LS through the law, AE through non-additive entry, U because `y′_A` reads `y₀`, SS-2 through its
  width, and PAD through a previous slice that is not a uniform pad; NP is met by a law with `G₀` uniform.
- **O5, a register outside LS's hypotheses under the preregistered laws.** An SMR register of width
  `≥ 2` meeting `{N−2, N−1}` that is not an arc of width `≤ 3` at `N ≥ 7` (for example a non-arc
  register at `N = 8`), under `ν_r`, `r ≥ 0` (under `π₀ = ν_{−1}` Lemma PAD decides it). It fails LS
  through the register, and the other five as for O1.
  No paper argument here decides it.
- **O4, a restricted carrier.** Fixing `x₀` fails AE's and NP's preparation hypothesis. In
  Observation W1, fixing `x₀ = 0` silences `y₀(t₀+1)`, so J-1 holds at `t₀+1`; the record then reaches
  site 0 at `t₀+2` (`y₀(t₀+2) = c`) and J-i fails there. O4 lies outside `𝔉` by
  definition, since `𝔉` requires all four preparations. By owner ruling (a) (§4.9) it is a
  restricted-carrier mathematical test case, not an established physical-retention mechanism, and not
  physically available without independent sourcing. RET-st, a route-analysis criterion and not the
  adopted retention definition (R:33–34), requires full carrier support to exclude the static-carrier
  trick HC-K4 (R:46–50, R:163–168 [R, motivation only]); it is kept as motivation for `𝔉`'s
  full-preparation requirement, as is requirement 2 of #1032, which asks for independently available
  preparations. §4 leaves O4 undecided beyond W1.
- **O6, other rules with non-additive carrier entry.** They fail AE's form, and LS does not apply.

**Whether one route is smallest is not established.** O1 keeps 𝔉's register family and adds a
readiness shape; O5 keeps the preregistered laws and adds a register shape. D-SML compares resources
rather than ranking by one scalar (DEFINITIONS:215–218), and no comparison here orders them. What O1,
O5 and O6 have in common, and what this record leaves unresolved, is:
1. **A paper analysis of the second hold tick** for a register of width `≥ 2` into which the carrier
   enters non-additively, in particular whether SS-2 extends to width `≥ 2`, so that the family is
   known, before the run, to contain a tuple whose outcome is open.
2. **A reason for the chosen shape independent of this analysis.** A law or register shape chosen
   after the planned family was shown unable to pass is a variant fitted to escape these lemmas, with
   no independent prediction (§A.29). For O1, without a source for the law (the unsourced ready region
   of MR★ C-3, MR:1342), a positive could be at most a CONDITIONAL witness on E-SDC, H-sel and H-cur;
   for O5 the same conditions apply, with the register shape a further declared choice.

The specific slice-level shape of §4.8 is not such an ingredient: it fails at `t₀+2`.

***

## 10. References (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1032 c.6651202161 (amaybaum, 2026-11-05T06:15:39Z) | the scope limit and the authorization limits, quoted in the header | owner record, quoted with author and time (§A.42 item 7) |
| #1115 c.6652197336 (posted 2026-11-05T07:19:55Z; amaybaum, Claude Code session chat, 2026-11-05) | owner ruling (a) on O4, quoted in §4.9; the landing mandate | owner record, quoted with author and time |
| #1115 c.6649925951, c.6650383732, c.6650681094, c.6650968100 | first statements of PAD, NP, AE (K1 and SMR), LS, the `N = 5` cases, SS-2 and §4.8, cited in each item's provenance | provenance: model-authored host comments. Each argument is carried in full here; their unretained exact checks support no claim |
| #1115 c.6651949245, c.6652079353, c.6652150358 | reviews of DPB at `250ab402`, `179acca3` and `4b4cacc9` | provenance. The review this record relies on is `REVIEW.md` |
| #1032 c.6567189236; #914 c.6563955678 | the CN control; P2-G (§4.1) | provenance |
| DPB at `4b4cacc9`; drafts `43370576` and `5839e064` on `research/o-ret-phaseb-design-20261105` | the source of this extract; the draft-only terms glossed here | provenance. These commits exist in the repository but are not reachable from `main`, and none is offered as support (§A.42 item 3) |
| `PREREG-PHASE-A.md` (P:57, P:79–80, P:418–500), `DESIGN-PULSE.md` (D:32–37, D:98–99, D:151–155), `DEFINITIONS.md:215–218`, `papers/SM.md:106`, `:112`, `papers/Main.md:726`, `MR-star.md` (MR:464–465, MR:1342), `../../native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md:35–36` | definitions, rule forms, posits, the unsourced ready region | support on `main` |
| `ROUTES.md` at `F = 49f0bd41` (R:33–34, R:46–50, R:163–168, R:233–240, R:314–315, R:421–426) | the RET-st and HC-K4 motivation; routes I and III | [R], motivation only; `F` is reachable from `main` |
