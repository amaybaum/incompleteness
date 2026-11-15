# U4-CALC: masking completeness and T3-sense return on K1, r2

**Status: hand calculation; reviewed at r1 (ACCEPT WITH CHANGES); r2 unreviewed.** Exact algebra and
proof by hand only. No simulation, no enumeration by program, no computation, no Lean. No repository
file, Issue or status is changed by this note.

**Revision.** r2 applies the ten required findings and the seven optional findings (O1 in part, see the
response) of the independent review of r1, `REVIEW-U4-CALC-r1.md` (PR #1294 at `b547c9f2`). r1 is kept
unchanged. The disposition of each finding is in `RESPONSE-U4-CALC-r1.md`.

**Purpose.** The two calculations that S3-U4 r1 left as stops and routed to #866 (O-REC, MR-1):
1. **Calculation 1 (masking completeness, U4-F1).** Under the K1 rule and μ-G, what a native
   (uniformly prepared) marker region holds about the carrier, in which quotient, as a function of the
   marker's preparation law and the tick; necessary and sufficient conditions for complete and for
   partial masking; worked instances and countercontrols.
2. **Calculation 2 (T3-sense return, U4-F2 and VER r2 §1.5).** Whether an available operation restores
   the carrier–marker joint law after marking within a budget below recurrence; the exact condition;
   the distinction between restoration of the joint law, restoration of unconditional visibility and
   global recurrence.

**Authorization.** Owner `amaybaum`, 2026-11-15, Issue #1169 comment 6891511297, item (2b): two hand
and exact-algebra calculations named by U4. Writer: Claude. Results route to #866 (O-REC, MR-1).

**Inputs, at exact objects.**
- RO-1 drafts, directory `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`,
  branch `research/ro1-sector-c-1169-20261114` at `e18126ee4d4605f70ec73628ba9d4ff8b34f8ebb`:
  - `S3-U4-r1.md`, blob `e6d8101a2e8017c9b1d09a0909e66c1faae52df7` (cited U4; U4-F1, U4-F2, PK-1 to
    PK-6, D-1);
  - `S3-U1-r5.md`, blob `68983f8666df0ca6c26ec4b9ec00d0a9e4072f67` (cited U1; accepted criterion:
    G1–G7, levels, AD-1, C-RET);
  - `S3-PLAN-r9.md`, blob `46ebc72d866e24a6ea5a0050f7afca3f18c8fffb` (cited PLAN; §8.4 D-1, §8.6 SNR-1);
  - `VERIFY-SL3-CC-r2.md`, blob `9f81ad0ea5b517c6d3758a328ee2c16de5bb4fc7` (cited VER; accepted as
    relayed in the brief: S-L3's four bullets verified, its erasure gloss at narrower scope,
    supplements Sup-1 to Sup-3);
  - `U4-SOURCES-r1.md`, blob `2e75b8862afe9ec7a0673b67d64658bf06a1a33a` (cited INV).
- Corpus at `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git show`:
  - `verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md`,
    blob `45af1678c401c03ac55938761d8f012a48225743` (cited MR★:N; §S.1 the K1 step, S-L1 to S-L7,
    S-C1, S-C4a/b, §S.3 σ1);
  - `.../measurement-record-formation/preregistration.md`, blob
    `c36fb14bd7761d242049100fde0bbc7fa6c4dcd9` (cited PREREG:N; R1–R5, §3.5, §5.3, T3);
  - `papers/Main.md`, blob `0db1759754bfaa85d1f5271f03dc6e0ca55d2209` (Lemma 3, Main:54; Main:682);
  - `verification/programmes/oi-qm/reconstruction/observer-access-20261106/ASSESSMENT.md`, blob
    `d5c49365e3c4554de5c8184d659c6500800b6532` (OAC:132–134, the recovery identity).
- Provenance only: the independent review of r1 of this note (`REVIEW-U4-CALC-r1.md`, PR #1294 at
  `b547c9f2`), whose two dual computations are adopted as controls C1-4 and C1-7 and re-derived here.
- Provenance only: the independent review of U4 r1 (`REVIEW-S3-U4-r1.md`, at PR #1294 head
  `3a08a4463b64bde2fa1cd09e2c415b7a65972180`), findings 5 and 12. Its statement at `t = 1` is re-derived
  below (Proposition 1.4); nothing here rests on it.

**Labels.** **[proved here]**: proved by hand in this note, unreviewed. **[NP]**: named premise
(§A.46 item 7). **[A-inf]**: author-side interpretation or consequence, not a proof. **[assumed]**: an
input the corpus does not source (U1 §2.3, "assumed").

***

## 0. Setting and hypotheses

**H-K1 (the step).** `S = 𝐑^Λ × 𝐑^Λ`, a state written `s = (x, y)` with `x` the previous and `y` the
current slice; `φ(x, y) = (y, A y − x)`, `(A u)_i = a Σ_{j∼i} u_j` with the relation sum (MR★:464–466;
VER §1.2). Here `a = 1` (MR★:473–477, reading), `𝐑 = ℤ/q` (finite, so `S` is finite and μ-G is
defined), and `Λ = ∏_{c=1}^{d} ℤ/L_c` with nearest neighbours and every side `L_c ≥ 3`. The native
graph is `d = 3` (MR★:467–471). One-dimensional rings (`d = 1`) are used only as instances of the
algebra, at §PC★2a's proof generality; they are not the native graph (MR★:470–472, σ10).

**Facts used, all re-derived here from H-K1.**
- *Additivity and S-L1.* `pr_Y φ^t(s) = Σ_X Φ^t_{YX}(s_X)` with `Φ^t_{YX} = pr_Y φ^t ι_X` (MR★:491–496;
  VER §1.2).
- *Chebyshev form.* Define integer polynomials `U_{−1} = 0`, `U_0 = I`, `U_{k+1} = A U_k − U_{k−1}`
  (so `U_{−2} = −I`). Then `u_t = U_t(A) y − U_{t−1}(A) x` solves `u_{t+1} = A u_t − u_{t−1}` with
  `u_{−1} = x`, `u_0 = y` (induction), and
  `φ^t(x, y) = (u_{t−1}, u_t) = (−U_{t−2}(A) x + U_{t−1}(A) y, −U_{t−1}(A) x + U_t(A) y)`.
- *Cassini identity.* `U_{t−1}² − U_t U_{t−2} = I` for all `t ≥ 1`. *Proof.* `t = 1`: `I − A·0 = I`.
  Both `U_t² − U_{t+1}U_{t−1}` and `U_{t−1}² − U_t U_{t−2}` expand, using the recurrence, to
  `U_t² − A U_t U_{t−1} + U_{t−1}²` (all `U_k` commute). `□`
- *Notation.* `A` denotes the adjacency operator when it acts on a field (`A y`, `P(A)`, `A = Aᵀ`); as
  a set, a subscript or a region it denotes the marker region (`S_A`, `R_A`, `π_A`, `Σ ∪ A`). Where both
  occur, `A_{AA}` is the block of the operator on the marker region.
- *Translation covariance.* Translations `τ_v` of the torus commute with `A`, so every `P(A)` with
  `P ∈ ℤ[z]` has entries `P(A)_{ij} = g_P(j − i)`. `A` is symmetric, with zero diagonal and entry `1`
  at each neighbour pair.
- *Order.* `φ` is a bijection of the finite set `S` (PC★ P-1), of finite order `N`.

**H-μ (the law).** Regions `X` partition `Λ`, each carrying both slices; `Σ` is the carrier, `A` the
marker, the rest environment and observers. The initial law is `λ ⊗ U_{S_{Σ^c}}`: an arbitrary carrier
law `λ` on `S_Σ`, and every non-carrier region uniform and independent. With `λ` uniform this is μ-G
itself (the counting measure on a product is the product of counting measures; Main:54, Lemma 3).
With `λ` not uniform it is μ-G conditioned on an event of the carrier, which is a representation unless
the event is executed; a prepared carrier is **[assumed]** (U1 C-PREP, first missing step).

**H-acc (access).** A region `B`'s *readable configuration* is `π_B(s_B)`, with `π_B = id` under A-reg
(both slices) and `π_B` = the current slice under A-cur (U1 AD-1(b)). `R_B := π_B(S_B)`.

**H-avail (operations).** Under U1's criterion on K1 the joint-state transformations a program effects
are the time shifts `φ^n`, `n` within the budget `T` (S-L2 [NP]; U4 §2.2; VER §1.4 checks it as a
definitional consequence of the availability standard). The read schedule is fixed (AD-1(e)); a held
record is a function of a present configuration (AD-1(d)). Conditioning on an executed herald (U1
§2.1) gives T3's heralded sub-label, which is not treated here (§4, R-4).

***

## 1. Calculation 1: what a native marker holds

### 1.1 Objects

For a readable region `A` (the marker) and tick `t`:
- `M_t := π_A pr_A φ^t ι_Σ : S_Σ → R_A`, the carrier's transfer into `A`'s readable configuration;
- `K_t := π_A pr_A φ^t (S_{Σ^c}) ⊆ R_A`, the image of all non-carrier content (marker included). Under
  A-reg `K_t = Σ_{X≠Σ} im Φ^t_{AX}`, U4's `K^t_A`;
- `Y_t := π_A pr_A φ^t(s) = M_t s_Σ + N_t`, with `N_t := π_A pr_A φ^t ι_{Σ^c} s_{Σ^c}`;
- `q_t := (M_t mod K_t) : S_Σ → R_A / K_t`, a homomorphism.

### 1.2 Theorem 1 (masking under μ-G) [proved here]

*Hypotheses:* H-K1, H-μ with any carrier law `λ`, H-acc. Parts (a)–(c) use only additivity and
bijectivity of `φ` on a finite abelian group; (d) as stated uses `𝐑 = ℤ/q` and `A = Aᵀ`. Let `W` be any path variable with `W → s_Σ → (rest)`, i.e. `W` depends on the
carrier content and on randomness independent of the non-carrier regions (a partition of `S_Σ`, or a
choice among carrier preparations).

(a) **Sufficiency.** `N_t` is uniform on `K_t` and independent of `s_Σ`. Given `s_Σ = x`, `Y_t` is
uniform on the coset `M_t x + K_t`. The class `Y_t + K_t = q_t(s_Σ)` is a deterministic function of the
carrier, and `Y_t` is conditionally independent of `s_Σ` given `q_t(s_Σ)`. Hence, for every readable
record `f(Y_t)` of the marker,

    I(W; f(Y_t)) ≤ I(W; Y_t) = I(W; q_t(s_Σ)).

**The marker holds exactly the class `q_t(s_Σ) ∈ R_A / K_t`, and nothing else about the carrier.**

(b) **Complete masking.** `I(W; Y_t) = 0` iff `W` is independent of `q_t(s_Σ)`. For two point-prepared
paths `x_L, x_R`: iff `M_t(x_L − x_R) ∈ K_t`. For every carrier law and every `W`: iff `q_t = 0`, iff
`K_t = R_A`.

(c) **No partial masking for two point paths.** For two point-prepared paths, `I(W; Y_t)` is either `0`
or `H(W)`: the marker either masks the path completely or records it perfectly. Partial masking under
μ-G (`0 < I(W; Y_t) < H(W)`) occurs only for path variables that are not functions of `q_t(s_Σ)` and
not independent of it (path cells of a partition of `S_Σ` that cut across the cosets of `ker q_t`).

(d) **Dual form.** With `𝐑 = ℤ/q`, `|R_A / K_t| = |𝒟_t|`, where `𝒟_t` is the set of readable
covectors `c` on `A` (A-reg: on both slices of `A`; A-cur: on its current slice) such that the
functional `s ↦ c · Y_t(s)` depends on the carrier content alone. The marker's record is the list of
values `c · Y_t = d_c · s_Σ`, `c ∈ 𝒟_t`. Equivalently: `𝒟_t ≠ 0` iff some nonzero K1 solution `(α_k)`
has `(α_{−1}, α_0)` supported in `Σ` and, at tick `t`, `(α_{t−1}, α_t)` supported in `A` (A-reg), or
`α_t = 0` and `α_{t−1}` supported in `A` (A-cur). The readout is `c = (α_t, −α_{t−1})` on (previous,
current) slices at `t`, and its value is `α_0 · x_Σ − α_{−1} · y_Σ` at tick `0`.

*Proof.*
(a) `N_t` is the image of `s_{Σ^c}`, uniform on `S_{Σ^c}` and independent of `s_Σ` (H-μ), under one
homomorphism; the pushforward of a uniform law under a homomorphism of finite groups is uniform on the
image, since the fibres are cosets of the kernel. So `N_t ~ U_{K_t}`, independent of `s_Σ`, and given
`s_Σ = x`, `Y_t` is uniform on `M_t x + K_t`. Hence
`P(Y_t = y | s_Σ = x) = [y + K_t = q_t(x)] / |K_t|`, which depends on `x` only through `q_t(x)`. So
`W → q_t(s_Σ) → Y_t` is a Markov chain and `I(W; Y_t) ≤ I(W; q_t(s_Σ))`; and `q_t(s_Σ) = Y_t + K_t` is a
function of `Y_t`, so `I(W; q_t(s_Σ)) ≤ I(W; Y_t)`. Data processing gives `I(W; f(Y_t)) ≤ I(W; Y_t)`.
(b) The first two statements follow from (a). For the third: `π_A pr_A φ^t : S → R_A` is surjective,
since `φ^t` is a bijection and `π_A pr_A` is surjective. With `S = S_Σ ⊕ S_{Σ^c}` this gives
`im M_t + K_t = R_A`. Hence `q_t` is surjective, and `q_t = 0 ⟺ im M_t ⊆ K_t ⟺ K_t = R_A`.
(c) For point paths `q_t(x_W)` is a function of `W`, and two values are either equal or distinct.
(d) Characters of `(ℤ/q)^n` are `s ↦ e^{2πi c·s/q}`; a subgroup and its annihilator satisfy
`|R_A/K_t| = |K_t^⊥|`, and an element of `R_A/K_t` is determined by its character values. A covector
`c` annihilates `K_t` iff `c · π_A pr_A φ^t` vanishes on `S_{Σ^c}`, i.e. iff that functional of the
tick-0 state is supported on `Σ`. For the wave form: the pullback `φ*c := c ∘ φ` acts by
`φ*(c₁, c₂) = (−c₂, c₁ + A c₂)` (compare coefficients in `c₁·y + c₂·(A y − x)`, `A = Aᵀ`), with inverse
`(d₁, d₂) ↦ (d₂ + A d₁, −d₁)`. Writing `(φ*)^{−k} d = (α_k, −α_{k−1})`, the inverse gives
`α_{k+1} = A α_k − α_{k−1}`: the covectors evolve by the K1 recurrence itself. `c = (φ*)^{−t} d` has
`c ∘ φ^t = d`, and `d = (α_0, −α_{−1})` is supported on `Σ` iff `α_{−1}, α_0` are. Readability of `c`
under A-reg is support of `α_t, α_{t−1}` in `A`; under A-cur, in addition, `c₁ = α_t = 0`. `□`

### 1.3 Theorem 1′ (any marker preparation law) [proved here]

*Hypotheses:* as Theorem 1, except that the non-carrier regions have an arbitrary law `ν`, independent
of the carrier (for example a biased marker: an unsourced preparation, U1 C-PREP). Let `ν_t` be the law
of `N_t`. Given `s_Σ = x`, `Y_t` has law `ν_t(· − M_t x)`. For two point paths with
`δ := x_L − x_R`:
- **complete masking** iff `ν_t` is invariant under translation by `M_t δ`;
- **perfect record** iff `M_t δ ∉ supp ν_t − supp ν_t` (the two conditional laws have disjoint supports);
- **partial masking** otherwise.

For a general path variable, complete masking iff the laws `λ_w^{M} * ν_t` coincide for all `w`, with
`λ_w^{M}` the law of `M_t s_Σ` given `W = w`. *Proof.* Independence of `N_t` and `s_Σ` gives the
conditional law; the three cases are equality, disjointness and the remainder of the two translates.
`□` Under μ-G, `ν_t = U_{K_t}`: invariance under `M_t δ` is `M_t δ ∈ K_t`, and `supp − supp = K_t`, so
the middle case is the complement of the first, which is Theorem 1(c).

### 1.4 Propositions on the tick [proved here]

- **Proposition 1.4 (`t = 0, 1`: complete masking in every geometry).** At `t = 0`, `Y_0 = π_A s_A` and
  `K_0 = R_A`. At `t = 1`, `pr_A φ ι_A (x_A, y_A) = (y_A, A_{AA} y_A − x_A)`, a bijection of `S_A` (inverse
  `(x′, y′) ↦ (A_{AA} x′ − y′, x′)`); under A-cur its current-slice part is surjective through `x_A`. So
  `K_1 = R_A` for every marker region, value group and slice form, and the PLAN §8.4 sentence is exact
  at `t ≤ 1`.
- **Proposition 1.5 (self-masking).** If `π_A Φ^t_{AA}` is surjective onto `R_A`, masking is complete at
  `t`. The converse fails: other regions can fill `K_t` (control C1-6: with `5 | q` the marker alone
  spans only `𝐑 ⊕ 5𝐑`, and the environment site `e_1` fills the rest).
- **Proposition 1.6 (time profile).** `K_t` and `q_t` depend on `t` only through `t mod N`; at every
  `t` with `φ^t = γ·id` (§2.3), `K_t = R_A` again.

### 1.5 Worked instances (checked by hand)

**Instance 1.1 (ring, A-reg).** `d = 1`, `Λ = ℤ/4`, any `q`, `a = 1`;
`Σ = {3, 0}`, `A = {1, 2}`, no environment. On `ℤ/4`, `i + 2 ≡ i − 2`, so

    u_1(i) = y_{i−1} + y_{i+1} − x_i,      u_2(i) = y_i + 2 y_{i+2} − x_{i−1} − x_{i+1}.

The A-reg readable configuration of `A` at `t = 2` is `(u_1(1), u_1(2), u_2(1), u_2(2))` with

    u_1(1) = y_0 + y_2 − x_1         u_2(1) = y_1 + 2y_3 − x_0 − x_2
    u_1(2) = y_1 + y_3 − x_2         u_2(2) = y_2 + 2y_0 − x_1 − x_3.

The marker's own content contributes `(y_2 − x_1, y_1 − x_2, y_1 − x_2, y_2 − x_1)`, so
`K_2 = {(a, b, b, a)}`, a proper subgroup (quotient `≅ 𝐑²`). The annihilating readouts are

    u_1(1) − u_2(2) = x_3 − y_0,        u_1(2) − u_2(1) = x_0 − y_3,

both functions of the carrier alone: `q_2(s_Σ) = (x_3 − y_0, x_0 − y_3)`. For the path pair
`L: y_3 = r`, `R: y_0 = r` (all other carrier content `0`, `r ≠ 0`), `q_2 = (0, −r)` against `(−r, 0)`:
**the uniformly prepared marker records the path perfectly at `t = 2`**, with no retention of `s_A`.
- *Dual check (control C1-3).* The right-moving pulse `α_k = δ_k` solves the recurrence on `ℤ/L` (`L ≥ 3`); it has
  `(α_{−1}, α_0) = (δ_3, δ_0)` in `Σ` and `(α_1, α_2) = (δ_1, δ_2)` in `A`, and Theorem 1(d) predicts the
  readout `(α_2, −α_1) = u_1(2) − u_2(1)` with value `α_0 · x − α_{−1} · y = x_0 − y_3`. It agrees with the
  direct expansion above (the left-moving pulse gives the other readout).
- *Same instance, other ticks and form.* `t = 1`: complete (Proposition 1.4). `t = 2` under A-cur: the
  readable `(u_2(1), u_2(2))` receives `(y_1 − x_2, y_2 − x_1)` from the marker, which is surjective, so
  masking is complete. Over `ℤ/2`, `φ² = (x, y) ↦ (x + Ay, Ax + y)` (since `A² ≡ 0` on `ℤ/4` mod 2),
  `φ⁴ = id`, `N = 4`, and at `t = 3 = N − 1`, `φ³ = φ^{−1}`: the readable `A`-content is
  `(x_0 + x_2 + y_1, x_1 + x_3 + y_2, x_1, x_2)`, onto which the marker maps surjectively; masking is
  complete. Over `ℤ/2` the record is present at `t = 2` only: the carrier's pulse passes through `A`.

**Instance 1.2 (native cubic torus; bounded single-site marker).** `d = 3`, `Λ = (ℤ/L)³` with
`L ≥ 5`, `a = 1`, `𝐑 = ℤ/q`; `A = {0}`, `Σ = {k : 1 ≤ |k|₁ ≤ 2}` (24 sites), environment the rest.
Paths of length 2 from `0` give `(A²y)(0) = 6y_0 + Σ_{c,±} y_{±2e_c} + 2Σ_{c<c′,±,±} y_{±e_c±e_{c′}}`, so

    u_2(0) = 5 y_0 + f(s_Σ),     f(s_Σ) := Σ y_{±2e_c} + 2 Σ y_{±e_c ± e_{c′}} − Σ_{j∼0} x_j,

and `x_0` does not occur. `u_1(0) = Σ_{j∼0} y_j − x_0`. Environment sites lie at `|k|₁ ≥ 3` and enter
neither. The marker contributes `(−x_0, 5y_0)` to `(u_1(0), u_2(0))`, so `K_2 = 𝐑 ⊕ 5𝐑` (A-reg) and
`K_2 = 5𝐑` (A-cur). **In both forms the marker holds `f(s_Σ) + 5𝐑 ∈ 𝐑/5𝐑 ≅ ℤ/gcd(5, q)`**: nontrivial
iff `5 | q`, and the complete value of `f` when `q = 5`. Over `ℤ/5`, the pair `L: x_{−e_1} = 1`,
`R: y_{2e_1} = 1` gives `f = −1` against `f = 1`: a perfect record. `f` is invariant under the point group
at `0`, so mirror-related path pairs are masked.

**Instance 1.3 (partial masking, non-μ-G marker).** Instance 1.1 at `t = 1`, with carrier content
`0` except `y_0 ∈ {0, 1}` (the path variable, equiprobable, `q = 2`), and a marker whose `x_1` is
Bernoulli(`p`) independent of its other cells. The readable content gives `u_1(1) − y_2 = y_0 + x_1`, and
no other readable function depends on `y_0`. So `I(W; Y_1) = 1 − h(p)` bits: complete masking iff
`p = 1/2` (the μ-G value), perfect record iff `p ∈ {0, 1}` (a quiet cell, [assumed]), partial otherwise.

### 1.6 Controls and consistency checks

Controls are independent computations whose outcome could have contradicted the prediction.
Consistency checks (CC) hold by definition or re-read the same expression; they are listed for
completeness and are not counted as controls.

| # | Control | Prediction | Hand result |
|---|---|---|---|
| C1-2 | `t = 1`, every geometry | `K_1 = R_A` | `Φ^1_{AA}` bijective (Prop. 1.4); in Instance 1.1 direct: holds |
| C1-3 | Instance 1.1, `t = 2`, A-reg | Theorem 1(d) from the pulse predicts readout `x_0 − y_3` | direct expansion gives `u_1(2) − u_2(1) = x_0 − y_3`: agrees; a nonzero marker term would have refuted it |
| C1-4 | Instance 1.1, `t = 2`: the dual count of Theorem 1(d) against the direct quotient | A-reg: `𝒟_2 ≅ 𝐑²`; A-cur: `𝒟_2 = 0` (masked) | Write `α_0 = aδ_3 + bδ_0`, `α_{−1} = cδ_3 + eδ_0`. Then `α_1 = Aα_0 − α_{−1} = aδ_2 + bδ_1 + (a − e)δ_0 + (b − c)δ_3`; support in `A` forces `e = a`, `c = b`, and `α_2 = Aα_1 − α_0 = aδ_1 + bδ_2`. So `𝒟_2 ≅ 𝐑²` (A-reg), with readouts `a(u_1(1) − u_2(2)) + b(u_1(2) − u_2(1))` of value `a(x_3 − y_0) + b(x_0 − y_3)`, the quotient found directly. Under A-cur `α_2 = 0` forces `a = b = 0`, agreeing with the direct surjectivity of the marker map. Holds |
| C1-6 | Instance 1.2 with `e_1` moved from `Σ` to the environment | `x_{e_1}` enters `u_2(0)` with coefficient `−1`: masked | holds (A-reg: environment contributes `(y_{e_1}, −x_{e_1})`, surjective with the marker's) |
| C1-7 | Instance 1.2, `t = 2`: the dual computation against the direct expansion | the marker records `c₂ f(s_Σ)` exactly when `5c₂ = 0` | A-reg covectors on site `0` annihilating `K_2 = {(−x_0, 5y_0)}` have `c₁ = 0`, `5c₂ = 0`, so `α_2 = 0`, `α_1 = −c₂δ_0`. Backwards: `α_0 = Aα_1 − α_2 = −c₂Σ_{j∼0}δ_j`; `α_{−1} = Aα_0 − α_1 = −c₂(5δ_0 + Σδ_{±2e_c} + 2Σδ_{±e_c±e_{c′}})`. With `5c₂ = 0` both lie in `Σ`, and `α_0·x − α_{−1}·y = c₂ f(s_Σ)`, agreeing with the direct expansion. With `5` a unit, `c₂ = 0`: nothing recorded. Holds |
| CC1-1 | `t = 0` | `q_0 = 0` | holds by definition (`A ⊆ Σ^c`, so `K_0 = R_A`) |
| CC1-5 | Instance 1.2 with `5 ∤ q` (e.g. `ℤ/2`, `ℤ/3`) | masked | re-reads `5y_0 + f` with `5` a unit; the independent check of this case is C1-7's `c₂ = 0` branch |

### 1.7 Answer to Calculation 1

[proved here] Under K1 and μ-G (carrier law arbitrary), the native marker at tick `t` holds exactly
the class `q_t(s_Σ) = M_t s_Σ + K_t` in `R_A / K_t`, with `R_A` the readable group of the declared slice
form and `K_t` the image of all non-carrier content. Masking of every path variable is complete iff
`K_t = R_A` (U4-F1's "for example" is the exact condition); for a given point-path pair iff
`M_t(x_L − x_R) ∈ K_t`, and otherwise the record is perfect. It is complete at `t ≤ 1` in every
geometry, and fails at `t = 2` in Instances 1.1 (ring, A-reg) and 1.2 (native cubic torus, both forms,
`5 | q`). For other marker laws the condition is translation invariance of `ν_t` (Theorem 1′), and
partial masking occurs.

[A-inf] Where the record is nonzero it is the carrier's own field transported into `A`, not covered by
background content (in Instance 1.1 the dual is the travelling pulse): record and outgoing carrier
coincide (MR★ §S.3 σ1, `Out` row). The result is a single-tick correlation (R1 for the partition of
`S_Σ` by `q_t`). Under strict μ-G (uniform carrier) that correlation needs no assumed input, so it is
at U1's derived level for that partition. Persistence (C-RET, R2), R3 and R4 are not addressed, and
whether the partition by `q_t` is a which-path partition is (γ).

***

## 2. Calculation 2: T3-sense return

### 2.1 Definitions

Marking occupies ticks `0` to `m ≥ 1`; the undo is `φ^n`, `0 ≤ n ≤ T`; the return tick is `t = m + n`,
in the window `[m, m + T]`. "Below recurrence" is read as `m + T < N` (VER Sup-2). Let `C = Σ ∪ A` and
`P_t := (φ^t)_*(λ ⊗ U_{S_{Σ^c}})`.
- **J-return at `t`:** the carrier–marker joint law `J_t := law of π_C pr_C φ^t s` equals `J_0`.
- **T3 (unconditional sub-label) at `t`:** `P_t` and `P_0` are equivalent (PREREG §5.3) over `Acc`,
  without postselection, and T0's witness returns (PREREG:485–487).
- **Full return at `t`:** `P_t = P_0`.
- **Visibility at `D` at `t`:** for a recombination region `D ⊆ Σ^c` and a family `F` of carrier
  preparations, `D`'s readable law at `t` depends on the member of `F`.
- **Global recurrence:** `t ∈ Nℤ`.
- **Aperiodic carrier law:** `λ` is invariant under translation by no nonzero element of `S_Σ` (every
  point mass is; so is every law with a unique most likely point).
- `Per(Σ) := {v : Σ + v = Σ}`, the translations fixing `Σ`. `Per(Σ) = {0}` whenever `Σ` fits in a box
  with fewer than `L_c/2` consecutive residues along every axis: if `Σ + v = Σ` with `v_c ≠ 0`, the
  projection of `Σ` to axis `c` is a union of cosets of a nontrivial subgroup of `ℤ/L_c`, and such a
  coset is not contained in any arc of fewer than `L_c/2` residues.

### 2.2 Lemmas [proved here]

**Lemma 2.1 (structure).** Under H-μ, `J_t = (Φ^t_{CΣ})_*λ * U_{K^C_t}`, with
`K^C_t := pr_C φ^t(S_{Σ^c})` (A-reg). Its `Σ`-marginal is `(Φ^t_{ΣΣ})_*λ * U_{B_t}`, with the
**leakage group** `B_t := pr_Σ φ^t(S_{Σ^c})`. *Proof.* As Theorem 1(a), with `C` in place of `A`. `□`

**Lemma 2.2 (rows).** If `Per(Σ) = {0}` and `P ∈ ℤ[z]`, then `P(A)_{ij} = 0` for all `i ∈ Σ, j ∉ Σ`
iff `P(A)` is a scalar matrix. *Proof.* `P(A)_{ij} = g(j − i)`. If `v ≠ 0` then `Σ + v ≠ Σ`, and since
`|Σ + v| = |Σ|` some `i ∈ Σ` has `i + v ∉ Σ`; so `g(v) = 0` for every `v ≠ 0`, and `P(A) = g(0) I`. The
converse is immediate. `□`

**Lemma 2.3 (leakage-free ticks are scalar).** Let `Per(Σ) = {0}`. Then `B_t = 0` iff `φ^t = γ·id`
for some `γ ∈ 𝐑` with `γ² = 1`. *Proof.* By the Chebyshev form, `B_t = 0` iff the `Σ`-rows of
`U_{t−2}(A)`, `U_{t−1}(A)`, `U_t(A)` vanish off `Σ`, iff (Lemma 2.2) all three are scalar:
`U_{t−1} = βI`, `U_t = γI`, `U_{t−2} = δI`. The recurrence `U_t = A U_{t−1} − U_{t−2}` gives
`βA = (γ + δ) I`; an off-diagonal neighbour entry of `A` is `1`, so `β = 0` and `δ = −γ`. Cassini gives
`0 − γ(−γ) = γ² = 1`. Then `φ^t(x, y) = (γx, γy)`. Conversely `φ^t = γ·id` preserves `S_{Σ^c}`. `□`

**Lemma 2.4 (the scalar ticks).** `T_γ := {t ∈ ℤ : φ^t = γ_t·id, γ_t² = 1}` is either `Nℤ` or
`(N/2)ℤ`, the latter exactly when `N` is even and `φ^{N/2} = γ·id` with `γ ≠ 1`. *Proof.* `T_γ` is a
subgroup and `t ↦ γ_t` a homomorphism into `{γ ∈ 𝐑^× : γ² = 1}`, every element of which has order at
most 2; its image is cyclic, so of order 1 or 2; its kernel is `Nℤ`. `□`

### 2.3 Theorem 2 (A-reg) [proved here]

*Hypotheses:* H-K1 on a torus, H-μ with an aperiodic carrier law `λ` [assumed preparation], A-reg with
`Σ ∪ A` readable at the return tick, `Per(Σ) = {0}`, H-avail.

(a) `J_t = J_0` iff `φ^t = γ·id` with `γ² = 1` and `(γ·)_*λ = λ`; for a point carrier `x`, iff
`φ^t = γ·id` and `(γ − 1)x = 0`.

(b) J-return and full return coincide at every `t`, and both coincide with the §5.3-equivalence part
of T3's unconditional sub-label. T3's further clause, that T0's witness returns, is met at a full
return wherever a T0 witness exists; on the record T0 is not shown on K1 (U4 §3.2; MR★ σ1, "That T0
fails is not claimed").

(c) **Window condition, given S-L2 [NP] (H-avail).** Some available `φ^n` gives a J-return within `[m, m + T]` iff the window
contains a tick `t ∈ T_γ` with `(γ_t·)_*λ = λ`. Below recurrence (`m + T < N`) this holds iff `N` is
even, `φ^{N/2} = γ·id` with `γ ≠ 1`, `m ≤ N/2 ≤ m + T`, and `λ` is `γ`-invariant. A return for **every**
carrier preparation occurs only at `t ∈ Nℤ`, outside every budget below recurrence. That `φ^n` are the
only available operations is S-L2, a named premise; parts (a), (b) and (d) are statements about laws at
ticks and do not use it.

(d) **Every return is global.** At any J-return tick `φ^t` is `γ` times the identity on all of `S`:
every region, the marker and any observer included, holds `γ` times its tick-0 content. A ready
observer at tick 0 holds no carrier information at `t` (S-L6's second bullet, at every `t ∈ T_γ`).

*Proof.* (a) If `J_t = J_0`, the `Σ`-marginal gives `λ = (Φ^t_{ΣΣ})_*λ * U_{B_t}`, which is
`B_t`-invariant; aperiodicity forces `B_t = 0`, and Lemma 2.3 gives `φ^t = γ·id`. Then `J_t` is the law
of `γ·(s_Σ, s_A)`, that is `(γ·)_*λ ⊗ U_{S_A}` (`γ` is a unit), which equals `J_0 = λ ⊗ U_{S_A}` iff
`(γ·)_*λ = λ`. The converse is the same computation. (b) Under the same conditions
`P_t = (γ·)_*λ ⊗ U_{S_{Σ^c}} = P_0`, so every continuation gives equal laws of every record: T3 holds
for every `Acc` in its §5.3-equivalence part, and a T0 witness returns wherever one exists. Conversely, T3 over an `Acc` that reads `Σ ∪ A`
under A-reg at the return tick (continuation `φ^0`) requires `J_t = J_0`. (c) Lemma 2.4, with the available operations given by H-avail. (d) Immediate
from `φ^t = γ·id`. `□`

### 2.4 When the half-period scalar return is excluded [proved here]

**Proposition 2.5.** `φ^{N/2} = γ·id` with `γ ≠ 1` is impossible in each of the following cases, so
under Theorem 2's hypotheses no J-return exists below recurrence:
- **(a)** `𝐑 = ℤ/2`: the only `γ` with `γ² = 1` is `1`.
- **(b)** `d = 3`, some side `L_1` even and `≥ 4`, the others `≥ 3`, any `q`. *Proof.* `v(i) = (−1)^{i_1}`
  has `Av = (−2 + 4)v = 2v`, and `(α, β) ↦ (αv, βv)` embeds `𝐑²` in `S` (entries of `v` are units). There
  `φ` acts by `M_2 = [[0, 1], [−1, 2]] = I + N_0`, `N_0 = [[−1, 1], [−1, 1]]`, `N_0² = 0`, so
  `M_2^t = [[1 − t, t], [−t, 1 + t]]`. `M_2^t = γI` forces `t ≡ 0 (mod q)` and `γ = 1`. `□`
- **(c)** `d = 1` (rings), any `L ≥ 3`, any `q`. *Proof.* The constant vector `v = 1` has `Av = 2v`
  (two distinct neighbours), so `φ` acts on `{(α1, β1)}` by the same unipotent `M_2` as in (b), and every
  scalar power is `I`. Hence `T_γ = Nℤ` on every ring; in particular Instance 1.1 has no J-return below
  recurrence for every `q`, not only `ℤ/2`. `□`
- **The dimension in (b) is needed.** The proof of (b) uses `Av = (2d − 4)v = 2v`. For `d = 2` the same
  `v` has `Av = 0`, and `M_0 = [[0, 1], [−1, 0]]` has `M_0² = −I`. For `d = 1`, `Av = −2v` and
  `M_{−2} = −I + N′`, `N′ = [[1, 1], [−1, −1]]`, `N′² = 0`, so `M_{−2}^t = (−1)^t(I − tN′)`, which is `−I`
  at `t = q` for odd `q`. So this mode excludes no `γ ≠ 1` outside `d = 3` (rings are excluded by (c)
  instead). In `d = 3` the constant mode does not exclude either: over `ℤ/5`, `6 ≡ 1` and `M_1³ = −I`.
- More generally: any `v` with a unit entry and `Av = λv` such that no power of
  `M_λ = [[0, 1], [−1, λ]]` over `ℤ/q` is a scalar other than `I`.

**Proposition 2.6 (lattice size; any `Σ`, both forms).** If `1 ≤ t < L_c/2` and `Σ + t e ⊄ Σ` for
`e = e_c` or `e = −e_c`, then `B_t ≠ 0`, and also the current-slice leakage of §2.5 is nonzero. *Proof.*
Take `i ∈ Σ` with `i + te ∉ Σ` and the tick-0 state `(0, rδ_i)`, `r ≠ 0`. On `ℤ^d` its solution `ũ` has
`ũ_t` supported in the ℓ1-ball of radius `t` about `i` (induction), and `ũ_t(i + te) = r` (induction: of
the neighbours of `i + (t+1)e` only `i + te` lies in the ball of radius `t`, and `ũ_{t−1}` vanishes
there). The torus solution is the finite sum of the `∏ L_cℤ`-translates (additivity, translation
covariance, sides `≥ 3`). A translate by `k ≠ 0` reaches `i + te` only if `|te − k|₁ ≤ t`, which fails:
if `k_c ≠ 0` then `|t − k_c| ≥ L_c − t > t`; otherwise `|te − k|₁ = t + Σ_{c′≠c} |k_{c′}| > t`. So
`u_t(i + te) = r ≠ 0`, i.e. column `i` of `U_t(A)` is nonzero at a site off `Σ`; `U_t(A)` is symmetric,
so a `Σ`-row of `U_t(A)` is nonzero off `Σ`. `□`

### 2.5 The current-slice form [proved here]

**Proposition 2.7 (A-cur).** Let `Per(Σ) = {0}` and `q` a prime power. The current slice of `Σ` at `t`
receives no background content iff `φ^t = γ·id` or `φ^{t+1} = γ·id` (`γ² = 1`). If the current-slice
(`y_Σ`) marginal of `λ` is aperiodic (for a point carrier it is), a single-tick A-cur return of the
readable carrier–marker law requires this background-free condition, since the readable `Σ`-marginal
at `t` is a law convolved with the uniform law on the current-slice leakage group. Below recurrence the
candidate ticks are therefore `t = N − 1` (always) and, when `φ^{N/2}` is a non-identity scalar,
`t ∈ {N/2 − 1, N/2}`. At `t = N − 1`, `φ^{N−1} = φ^{−1}`, so the current slice at `t` is the tick-0
previous slice `x`. A single-tick A-cur return at `N − 1` holds iff the law of `x_Σ` under `λ` equals the
law of `y_Σ` (for a point carrier: `x_Σ = y_Σ`).

*Proof.* The background-free condition is that the `Σ`-rows of `U_t(A)` and `U_{t−1}(A)` vanish off `Σ`,
i.e. (Lemma 2.2) `U_{t−1} = βI`, `U_t = γI`. Then `U_{t−2} = βA − γI`, and Cassini gives
`β² + γ² − 1 = βγ A`; `A` has zero diagonal and unit off-diagonal neighbour entries, so `βγ = 0` and
`β² + γ² = 1`. For `q = p^k`, `p` cannot divide both `β` and `γ` (else `β² + γ² ≡ 0 mod p`), so one is a
unit and the other is `0`. If `β = 0`, `φ^t = γ·id`. If `γ = 0`, then `β² = 1`, `U_t = 0` and
`U_{t+1} = −βI`, so `φ^{t+1} = −β·id`. *Converse.* If `φ^t = γ·id`, the current slice at `t` is `γy`;
if `φ^{t+1} = γ·id`, then `φ^t = γφ^{−1}` and the current slice at `t` is `γx`. Both are free of
background. `φ^{−1}(x, y) = (Ax − y, x)` gives the `N − 1` statement. *The prime power is needed.* Over
`ℤ/6`, `β = 3`, `γ = 4` satisfy `βγ ≡ 0` and `β² + γ² = 25 ≡ 1` with neither zero, so the step that
excludes other ticks fails for composite `q`. Whether such `U_{t−1}, U_t` occur on a torus is not
decided (R-3). `□`

[A-inf] The `N − 1` return is S-L3's global inverse wait, measured from tick 0: every region's current
slice shows its tick-0 previous slice. It lies inside the budget only when `m + T = N − 1`.

### 2.6 Visibility at `D`, distinguished from the joint law [proved here]

**Proposition 2.8.** Let `D ⊆ Σ^c` be readable, under H-μ.
- (i) `D`'s readable law, given carrier `x`, is uniform on `M^D_t x + K^D_t`, where
  `M^D_t = π_D pr_D φ^t ι_Σ` and `K^D_t = π_D pr_D φ^t(S_{Σ^c})` (Theorem 1 applied to `D`). Neither
  depends on how `Σ^c` is partitioned, **so the declaration of a marker region, coupled or not, does not
  change `D`'s law at any tick.** This is S-L5 at the level of laws.
- (ii) If `B_t = 0`, `φ^t` maps `S_{Σ^c}` injectively into itself, hence onto it, so `K^D_t = R_D` and `D`
  shows no carrier dependence; this step needs only H-μ. Under Theorem 2(a)'s hypotheses (aperiodic `λ`,
  `Per(Σ) = {0}`) a J-return implies `B_t = 0`, so there a J-return and visibility at `D` at the same
  tick exclude each other. The same holds at `t ∈ Nℤ`.
- (iii) Visibility at `D` occurs at ticks with no J-return. Instance 1.1 with `D := {1, 2}`, read as a
  recombination region (no marker declared): at `t = 2`, `D` distinguishes `y_3 = r` from `y_0 = r`, and
  over `ℤ/2` (`N = 4`) no tick `1 ≤ t ≤ 3` is a J-return (Proposition 2.5(a)).

[A-inf] On K1, "restoring unconditional visibility after marking" has no operational counterpart: the
marker's coupling never entered `D`'s law (i), and the only available choice is which tick `D` is read
at, which AD-1(e) fixes in the program. A change of visibility between ticks is a change of the
noise-masking condition at `D` (review finding 5's coset question at `D`), not an undo of a record.

[A-inf] The informative alternative to PREREG's literal T3 would compare the marked and the unmarked
preparation at the same tick. By (i) that comparison is degenerate on K1 under μ-G: declaring a marker
region changes no law of any region other than the marker's own. So the T3-sense negative of §2.3 has
no erasure-specific content (§2.8, pressure test).

### 2.7 Controls and consistency checks

As in §1.6, a consistency check (CC) cannot fail and is not counted as a control.

| # | Control | Prediction | Hand result |
|---|---|---|---|
| C2-1 | `λ` uniform (strict μ-G) | `J_t = J_0` at every `t`; Theorem 2's aperiodicity hypothesis must exclude it | `λ` is invariant under every translation: excluded. T0 also fails there (`D`'s law is carrier-free), so the case is vacuous |
| C2-3 | Instance 1.1 over `ℤ/2` (`N = 4`), `Σ = {3, 0}`, `Per(Σ) = {0}` | `B_t ≠ 0` for `t = 1, 2, 3` (Prop. 2.5(a)) | `u_1(0) = y_3 + y_1 + x_0` (contains marker `y_1`); `u_2(0) = y_0 + x_3 + x_1` (contains `x_1`); `t = 3`: previous slice `(Ax)_0 + y_0 = x_3 + x_1 + y_0` (contains `x_1`). A background-free carrier row would have refuted it |
| C2-4 | Same, A-cur, `t = 3 = N − 1` | current slice of `Σ` background-free (Prop. 2.7) | `φ^{−1}`: current slice `= (x_3, x_0)`: holds |
| C2-5 | Same, A-cur, `t = 1 = N/2 − 1` | not background-free, since `φ²` is not scalar | `φ²(x, y) = (x + Ay, Ax + y)` is not scalar; `u_1(0)` contains `y_1`: holds |
| C2-6 | Countercontrol for the `d = 3` hypothesis of Prop. 2.5(b): the alternating mode on a ring | a non-identity scalar power exists, so (b)'s argument does not transfer | `M_{−2}^q = −I` for odd `q` (Prop. 2.5, dimension bullet): holds; a unipotent block would have refuted the need for `d = 3` |
| C2-7 | Countercontrol for the prime-power hypothesis of Prop. 2.7 | the dichotomy `β = 0` or `γ = 0` fails for some composite `q` | `ℤ/6`, `β = 3`, `γ = 4`: holds |
| CC2-2 | `t = N` | full return | holds by definition of `N` |

### 2.8 Answer to Calculation 2

[proved here] Under K1, μ-G background, an aperiodic (for example point-prepared, [assumed]) carrier on
a region with `Per(Σ) = {0}`, A-reg access to `Σ ∪ A`, and S-L2 [NP] for the available operations, an
available `φ^n` restores the carrier–marker joint law (equivalently the full law, equivalently the
§5.3-equivalence part of T3's unconditional sub-label) exactly at the ticks where
`φ^t` is a scalar `γ·id` with `γ² = 1` that fixes the carrier law. These ticks are `Nℤ` or `(N/2)ℤ`.
Below recurrence the only candidate is `t = N/2`, with `φ^{N/2}` a non-identity scalar, inside the
window and fixing the carrier law. That candidate is excluded for `𝐑 = ℤ/2`, for every ring, and for
every native cubic torus (`d = 3`) with an even side `≥ 4`; no return then exists within any budget
below recurrence. A return for every
carrier preparation is global recurrence only. Every return that does occur is a global map on all of
`S`, not a subsystem undo. Under A-cur, for `q` a prime power, the candidates are `N/2 − 1`, `N/2`
(scalar case) and `N − 1` (the global inverse wait, single-tick and preparation-specific); for composite
`q` other ticks are not excluded (R-3). Before half the torus side no return
of any kind occurs, for any `Σ` not translation-periodic by `t` (Proposition 2.6). Visibility at `D` is
a different condition, the masking condition of Theorem 1 at `D`, unaffected by any marker declaration.
It cannot hold at a joint-law return tick, and it holds at ticks without one.

[A-inf] **Pressure test of the negative.** The obstruction is leakage of background content into
the carrier region (`B_t ≠ 0`). It is present with no marker declared at all (Lemma 2.3 does not use
`A`). The negative therefore says that a free K1 field in a uniform background does not return a
localized carrier's law below recurrence. It is not specific to erasing a which-path record, and it
does not by itself discriminate K1 from an eraser experiment, whose carrier also does not return to its
pre-marking location. The negative is specific to the uniform background: with a quiet ([assumed])
background the leakage would carry no content.

***

## 3. Consequences for D-1 [A-inf]

- **Does (β) fail generically?** The PLAN §8.4 sentence ("(β) generically fails unless `s_A` is held
  elsewhere") is exact at `t ≤ 1` and is not a general fact. At `t ≥ 2` masking is complete iff
  `K_t = R_A`. It fails in Instance 1.2, on the native cubic torus (`5 | q`, bounded single-site
  marker), and in Instance 1.1 (ring). There the uniformly prepared native marker holds a single-tick
  (R1) record of the carrier functional `q_t`, with no retention of `s_A` anywhere; the perfect record
  of a point-path pair also uses the assumed point preparation of the carrier (H-μ, U1 C-PREP). No measure over geometries is on record,
  so "generic" has no defined sense. If owner question 1 is answered in favour of a revision, the
  sentence would be replaced by the criterion of Theorem 1.
- **D-1's (β)–(δ) outcome.** "Unsourced at (β)–(δ)" is the correct outcome only at geometries and ticks
  where `K_t = R_A`. Elsewhere (β) holds at the level of a single-tick correlation (R1), and the record
  is transported carrier content, which is the trace route of C-4 at one tick. "Empty on K1" is not
  reached. **D-1 stays undecided at (γ)**: whether the partition by `q_t` is a which-path partition, and
  whether `D`'s quotient corresponds to observed fringes, is the open correspondence (Main:682).
- **Native-marker miss branch.** Its condition "(β) with a sourced retention of `s_A`" is not needed
  where masking is incomplete. The branch still needs (γ), T0 and a prepared carrier, all unsourced
  (U4-F9), so **it does not become reachable**.
- **S-L3 branch (U4-F2).** The T3-sense statement VER r2 §1.5 lists as unverified is now proved by hand
  at the scope of Theorem 2 and Proposition 2.5: no unconditional joint-law return within a budget below
  recurrence for `ℤ/2`, for rings, or for a native cubic torus (`d = 3`) with an even side `≥ 4`, and in
  general only by a global half-period scalar map. As a statement about available operations it is
  conditional on S-L2 [NP]. It does not reach the raw-direct observable. On K1 visibility at `D` is fixed by geometry,
  tick and background and is not changed by any marker declaration (Proposition 2.8). So the "candidate
  raw-direct miss on eraser behaviour" still turns on (γ).
- **SNR-1.** Nothing here counts toward (a′). The Calculation 2 negative relies on an assumed carrier
  preparation (U1 C-PREP) and on S-L2, a named premise, for the claim that no other operation is
  available. Under SNR-1 it is reported as concerning an assumed apparatus (the prepared carrier), and
  it does not count; its S-L2 dependence would in any case make it conditional on that premise. It is
  also a hand result of r2, not yet re-reviewed. Calculation 1 is a positive result and removes the basis of the
  "unsourced at (β)–(δ)" outcome only where `K_t ≠ R_A`.

## 4. What is not decided (precise remaining steps)

- **R-1.** For native tori with all sides odd and `q ≥ 3` (every such `q` has the unit `γ = −1 ≠ 1`;
  Proposition 2.5 covers only `q = 2` there), whether
  `φ^{N/2} = γ·id` occurs. Equivalently, whether `U_{N/2−1}(A) = 0` with `U_{N/2}(A)` scalar. This is a
  finite calculation per `(L_c, q)`, not done here. Where the eigen-decomposition of `A` mod `q` is
  available, it is the condition that every block `M_λ` has `M_λ^{N/2} = γI`.
- **R-2.** Periodic carrier regions (`Per(Σ) ≠ {0}`) at ticks `t ≥ L_c/2`: only Proposition 2.6 applies.
- **R-3.** A-cur for `q` not a prime power: the dichotomy of Proposition 2.7 holds per CRT component
  and fails for `q` itself (C2-7); whether mixed background-free ticks occur on a torus, and the combined
  condition, are not written out.
- **R-4.** T3's heralded-probabilistic sub-label, conditioning on an executed herald (U1 §2.1). A
  success branch would need a readable region whose content determines the leakage `B_t`, as in the
  recovery identity OAC:132–134. Not decided.
- **R-5.** T3 over an `Acc` that reads less than `Σ ∪ A` under A-reg, or uses multi-tick held records:
  the direction "T3 ⇒ J-return" in Theorem 2(b) needs `Σ ∪ A` read at the return tick.
- **R-6.** Calculation 1 on the native torus with `𝐑 = ℤ/2` and bounded regions. For `q | 4`,
  transverse-constant configurations evolve by the one-dimensional rule (`(Au)(i) = g(i_1 + 1) +
  g(i_1 − 1) + 4g(i_1)`), so Instance 1.1 lifts to slabs. A slab spans a full transverse plane, so the
  lift is not a bounded-region instance. A bounded instance over `ℤ/2` is not decided.
- **R-7.** Persistence of the single-tick records of §1.5 under C-RET, and their R3/R4 standing.

## 5. Findings and assumption-watch markers (§A.31)

| # | Finding | Check | Class |
|---|---|---|---|
| CALC-F1 | The native marker holds exactly `q_t(s_Σ) ∈ R_A/K_t`; complete masking for all paths iff `K_t = R_A`; for two point paths masking is all-or-nothing | Theorem 1; C1-2 to C1-4, C1-6, C1-7 | NEW: sharpens U4-F1 from a sufficient example to the exact condition |
| CALC-F2 | Masking fails at `t = 2` on the native cubic torus (`5 | q`) and on rings: a uniform marker holds a single-tick (R1) record of the carrier functional `q_t` without retention of `s_A` | Instances 1.1, 1.2; C1-3, C1-7 | NEW: the PLAN §8.4 masking sentence holds in every geometry at `t ≤ 1`; at `t ≥ 2` it holds iff `K_t = R_A` (for example Instance 1.1 under A-cur at `t = 2`, and over `ℤ/2` at `t = 3`; Instance 1.2 with `5 ∤ q`; C1-6), and fails in Instances 1.1 and 1.2 |
| CALC-F3 | Under μ-G background, a joint-law (T3 unconditional) return for a bounded aperiodic carrier occurs only at ticks with `φ^t = γ·id`, `γ² = 1`: at `N/2` at most below recurrence; excluded for `ℤ/2`, for rings, and for native cubic tori (`d = 3`) with an even side `≥ 4` | Lemmas 2.2–2.4, Theorem 2, Prop. 2.5; C2-1, C2-3 to C2-7 | NEW: supplies the §5.3-equivalence part of the T3-sense statement at stated scope; concerns an assumed carrier preparation, and its "no available operation" form is conditional on S-L2 [NP] |
| CALC-F4 | `D`'s law does not depend on any marker declaration; visibility at `D` and a joint-law return exclude each other at a tick | Prop. 2.8 | ELABORATING: S-L5 at the level of laws |
| CALC-F5 | The obstruction to return is background leakage into the carrier, present without any marker | Lemma 2.3; Prop. 2.8(i) | ELABORATING (scope limitation of CALC-F3): the negative concerns carrier transport in a uniform background, not erasure; the marked-against-unmarked comparison is degenerate on K1 |
| AW-1 | AD-1(f) and C-RET exclude return "by recurrence" (`t ∈ Nℤ`). MR★ σ6 ("lies beyond any budget that R2 admits") and PLAN's S-L3 scope ("the global wait `φ^{N−1}` lies beyond it") concern the operation `φ^{N−1}`, with `n = N − 1`. The A-cur tick-`(N − 1)` return is reached by `n = N − 1 − m ≤ T` when `m + T = N − 1`, and the half-period scalar return by `n = N/2 − m`. Both lie below `N`, yet act on every region as a recurrence does | Theorem 2(d), Prop. 2.7 | assumption-watch marker: whether the budget clause is meant as "below the least `t` with `φ^t` scalar" (owner question 2) |

## 6. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| U4, U1, PLAN, VER, INV on `research/ro1-sector-c-1169-20261114` at `e18126ee` | the questions posed; AD-1, the availability criterion, C-PREP; D-1 and SNR-1; S-L3's verified scope | support off `main` (gap), as in U4 §9; every proof here uses only the K1 step and the corpus lines cited on `main` |
| REVIEW-U4-CALC-r1 at `b547c9f2` | C1-4, C1-7 (dual computations); C2-6, C2-7 (counterexamples) | provenance: all re-derived here |
| REVIEW-S3-U4-r1 at `3a08a446` | Proposition 1.4, Prop. 2.8's coset reading at `D` | provenance: both are re-derived here |
| #1169 c.6891511297 | authorization | governance |

## 7. Owner questions

1. Should Theorem 1's criterion replace the PLAN §8.4 masking sentence, as a revision of PLAN, or be
   recorded as a U4 finding only (with U4 owner question 4)?
2. AW-1: should AD-1(f)'s budget be read as excluding the half-period scalar return and the global
   inverse wait, which act on all regions as a recurrence does?
3. Should R-1 (half-period scalar returns on odd tori) and R-4 (heralded sub-label) be routed to #866
   as a further bounded unit?
