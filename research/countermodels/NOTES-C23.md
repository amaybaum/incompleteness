# NOTES-C23 — the 2-torus group of the tower's closure: an explicit invariant cone, or the obstruction

Round-5 node C23. S0 first drafted 2026-10-11T08:34:52Z (uncommitted; sha256 `b1683d44…`, kept in the session
scratchpad) and **revised before any C23 script ran** at 2026-10-11T10:26Z–10:32Z (`date -u`); the revision is the S0 of
record. What the revision changed, and why: (1) the draft used a class-(v) seed `(2, 0, 0, 1 + i)` as a balanced-route
instance — its `G_T`-orbit contains a product (`CNOT·(2, 0, 0, 1 + i) = (2, 0, 1 + i, 0)`), so H1 excludes it; class-(v)
seeds are now treated by H1; (2) the draft's balanced-route analysis covered only the generic class; the revision
classifies every seed by the rank of its orthogonalizing family (Design 3) and adds the class-(ii) seeds, which the draft
had put with the generic ones; (3) the draft's mixture seed `(1, 1, 1, i)` is reachable (`|h₀h₃| = |h₁h₂|`), replaced;
(4) G3's countercontrol made the one of C18's A1-cc (two values of `c` on one orbit); (5) a drafting word in G5 removed.
Parameters of the tightness instances (G5) were chosen by scratch computations after the draft and before the revision
(`x23_tight.py` float, `x23_exact.py`, `x23_exact2.py` exact searches, session scratchpad; guidance, not evidence); the
recorded checks are the scripts below.

Object (HO-36 item 2, HO-35 item 3; NOTES-B10 §4–§5 read at `research/bridge` @ `a34d20b5`, LOG 08:34Z entry): the closure
of B10-5's locally finite tower. Conventions: computational basis `|00⟩, |01⟩, |10⟩, |11⟩` (control first; indices
`0, 1, 2, 3`), `CNOT` the permutation `(2 3)`, `X_B = 1 ⊗ X` the permutation `(0 1)(2 3)`, `R_B(t) = 1 ⊗ diag(1, e^{it})
= diag(1, e^{it}, 1, e^{it})`; defects `d_h = I − cP_h`, `P_h = hh†/|h|²`; `K(Z) = (Q ∩ Z*) + cl cone Z` (C22's `surgeryC`;
equal to `(Q ∩ Z*) + cone Z` for compact `Z`, C22.3). Reading of every statement: **invariance** (cone-preserving
admissibility); nothing here is about operational availability (HO-33 item 5; the C21 safeguard).

## Groups, named exactly (owner's points of 07:48Z and 08:03Z)

- **The finitely generated stages** `G_n := ⟨CNOT, X_B, R_B(2π/2ⁿ)⟩` (B10-5) and their union `G_∞ := ⋃_n G_n`, generated
  by the countable set `{CNOT, X_B, R_B(2π/2ⁿ) : n ≥ 1}` (countable, not finitely generated).
- **The topological closure** `G_T := cl(G_∞) = cl⟨CNOT, X_B, R_B(t) : t ∈ ℝ⟩`. Claim (G): as unitaries modulo phase,
  `G_T = T² ⋊ V4`, `T² = {D(u, v) := diag(1, uv, u, v) : |u| = |v| = 1}`, `V4 = {1, CNOT, X_B, X_B·CNOT}` acting as the
  permutations `{e, (23), (01)(23), (01)}`. Steps: `R_B(t) = D(1, e^{it})`, `CNOT·R_B(t)·CNOT = D(e^{it}, 1)` [X], so the
  dyadic points `D(ω_n^a, ω_n^b)` lie in `G_∞` and are dense in `T²` [W]; `CNOT·D(u, v)·CNOT = D(v, u)`,
  `X_B·D(u, v)·X_B = uv·D(ū, v̄)` [X], so `T² ⋊ V4` (with phases) is a closed group containing every generator; hence
  `cl(G_∞) = T² ⋊ V4` modulo phase [W]. Phases act trivially by conjugation.
- **The step from `G_∞` to `G_T`** (owner's point (2)): (a) a cone invariant under `G_∞` and **closed** is invariant under
  `G_T` — for `g = lim g_m`, `g_m ∈ G_∞`, and `x ∈ K`, `gxg† = lim g_mxg_m† ∈ K` because `K` is closed, and the same for
  `g⁻¹` [W]; a cone with H3 is closed (a dual cone is closed). (b) For a surgery, `K(Z) = K(cl Z)` (`Z* = (cl Z)*`,
  `cl cone Z = cl cone (cl Z)`) and `cl Z` is `G_T`-invariant when `Z` is `G_∞`-invariant [W]. So every statement below
  about `G_T`-invariant surgeries applies to surgeries invariant under every stage `G_n` at once.

## Question, design, productivity test (§A.31)

**Question.** Is there an explicit `G_T`-invariant closed self-dual cone with H1–H3 (`≠ Q3`), or an obstruction to the
explicit routes available — rank-one orbit surgeries with any weights (C13-O, C18-1) and balanced rank-two surgeries
through the engine `selfDual_of_local` (C17.1 [D], C18-2)?

**Design (fixed before the first run).**
1. **Lemma C23-1 (universal orthogonal pair).** For `h ∈ ℂ⁴` put `α = h̄₂h₃`, `β = h̄₀h₁`. Then
   `⟨h | D(u, v)X_B h⟩ = β + uvβ̄ + uα + vᾱ` (identity), and for every `h ≠ 0` some `(u, v) ∈ T²` makes it vanish:
   (i) `αβ ≠ 0`, `|α| ≠ |β|`, and (ii) `αβ ≠ 0`, `|α| = |β|`: for every `u` with `ᾱ + uβ̄ ≠ 0` (all but at most one),
   `v = −(β + uα)/(ᾱ + uβ̄)`, unimodular since `|β + uα| = |ᾱ + uβ̄|` for `|u| = 1` (identity); in class (ii) `v` is
   constant; (iii) `α = 0 ≠ β`: `uv = −β/β̄`; (iv) `β = 0 ≠ α`: `v = −uα/ᾱ`; (v) `α = β = 0`: every `(u, v)`. Hence
   **every `G_T`-orbit of rays contains an orthogonal pair**, realized by `g = D(u, v)X_B`. Mechanism: the double
   transposition `(01)(23)` with a torus that moves a relative phase inside both swapped pairs (NOTES-C16's marker).
2. **Theorem C23-2 (rank-one route closed).** (a) No rank-one surgery `K(Z)` with `Z` a compact `G_T`-invariant set of
   defects `I − c_dP_d`, every `c_d ∈ (1, 2)`, is self-dual: `c` is constant on orbits (`c = 1 − λ_min`), its maximum `c*`
   is attained on an orbit, which carries an orthogonal pair (C23-1), and Lemma C18-1 gives `y = P_h + λd_{gh}`,
   `λ = (c* − 1)/(4 − 2c*)`, in `K* \ K` (the decomposition step in closed-hull form: Lemma C23-5). (b) **Bell corner.**
   `det Ψ(D(u, v)h) = v(h₀h₃ − u²h₁h₂)` (identity), so a `T²`-orbit is maximally entangled iff `h ∈ C1′ ∪ C2′`,
   `C1′ = {(|00⟩ + w|11⟩)/√2}`, `C2′ = {(|01⟩ + w|10⟩)/√2}` [W]; `X_B` swaps the circles, so the only orbit admissible for H1
   at `c = 2` is `C1′ ∪ C2′`, whose surgery is `(1 ⊗ H) K_T (1 ⊗ H)†` (`1 ⊗ H` carries stage 4's S2 circles onto `C1′, C2′`),
   not self-dual by stage 4's exact pair (`research/archive/pt/Z/z2e_s2_surgery.py` S2–S3), transported to the
   computational basis and re-verified exactly here. (c) **Mixtures** of the Bell circles at `c = 2` with orbits at
   `c < 2`: not self-dual when the orbit of largest `c < 2` has `max((|h₀| + |h₃|)², (|h₁| + |h₂|)²) ≤ |h|²` (then every
   Bell state has squared overlap `≤ 1/2` with every orbit state, and C18-1's witness pairs `1 − 2s + λ(2 − c* + 2c*s′)
   ≥ 0` with every Bell defect while `⟨d_b, d_h⟩ ≥ 2 − c* > 0`); otherwise OPEN (as C18.8).
3. **Theorem C23-3 (balanced route: the engine certifies nothing).** For `d = I − cP_h − (2 − c)P_k` (`k ⊥ h`,
   `c ∈ (1, 2)`; C18-2 (b) shows balance is forced) the engine needs, for every `g ∈ G_T` with `gh ⊥ h`, zero pairing
   `⟨d, gdg†⟩ = 0`, i.e. `span(h, k) ⊥ span(gh, gk)` (otherwise `u = h`, `x = gh` violate its local condition); in
   particular `k ⊥ F_X(h) := span{gh : g ∈ O_X(h)}`, `O_X(h) = {D(u, v)X_B : ⟨h|D(u, v)X_Bh⟩ = 0}`. Let
   `r = dim F_X(h)` (`F_X(h) ⊆ h^⊥`). (a) **`r = 3`** (exactly class (i)): `k ∈ F_X(h)^⊥ ∩ h^⊥ = {0}` — **no balanced
   partner**; the rank: the functions `1, uv, u, v` on the solution curve satisfy exactly one linear relation when
   `αβ ≠ 0`, `|α| ≠ |β|` (the 3 × 4 system for the coefficients of a relation has rank 3 there and rank 2 iff
   `|α| = |β|`) [W]. (b) **`r = 2`** (class (ii), and classes (iii), (iv) with exactly one vanishing coordinate): the partner
   is unique up to scale, `k₀` (class (ii) in the normal form `h = (|h₀|, |h₁|e^{iθ}, |h₂|, |h₃|)`:
   `k₀ = (|h₂|, −e^{iθ}|h₃|, −|h₀|, |h₁|)`; class (iv) with `h₁ = 0`: `k₀ = (−(|h₂|² + |h₃|²)/h̄₀, 0, h₂, h₃)`; the other
   subcases alike) [W]; then **tightness**: the pairs `(d, UdU†)`, `U = e^{iεH} ∈ T²`, have positive pairing for small `ε`,
   and the first-order change of `x†(UdU†)x` on the cap-boundary circle of `d` in `span(h, k₀)` (`u = (ĥ + e^{iφ}k̂₀)/√2`,
   `x ⊥ u`) is `2(c − 1) Im(e^{iφ}a₁₂)`, `a₁₂ = ĥ†Hk̂₀`; with `p_i := h̄_ik₀,ᵢ`, `a₁₂ ∝ p₁ + p₂` for `H₁ = diag(0, 1, 1, 0)` and
   `∝ p₁ + p₃` for `H₂ = diag(0, 1, 0, 1)`, and both vanish only if `p = (t, t, −t, −t)`, which no class-(ii)–(iv) partner
   satisfies (class (ii): `p = (|h₀h₂|, −|h₁h₃|, −|h₀h₂|, |h₁h₃|)`; class (iv): `p = (−r², 0, |h₂|², |h₃|²)`; the others
   alike) [W]; so a cap point near the boundary and a small torus element violate the local condition [W + X instances].
   (c) **Two or more vanishing coordinates**: products (no defect), or `(h₀, 0, 0, h₃)`, `(0, h₁, h₂, 0)`, whose orbits
   contain a product through `CNOT`, so H1 excludes every defect with such a negative eigenvector [X]. Whether some
   balanced surgery is self-dual without the engine is **not** decided (OPEN, as C18.8).
4. **Lemma C23-5 (the decomposition step with the closed hull) [W].** In C18-1 with `Z` compact: if `y = q + z`,
   `q ∈ Q ∩ Z*`, `z ∈ cl cone Z`, `⟨y, d_h⟩ = 0` and `⟨d, d_h⟩ ≥ 4 − 2c* > 0` on `Z`, then `z = 0` (for `z = lim z_m`,
   `z_m = Σ t^{(m)}_k d_k`: `⟨z_m, d_h⟩ ≥ (4 − 2c*)Σ_k t^{(m)}_k` and `⟨z_m, d_h⟩ → ⟨z, d_h⟩ = −⟨q, d_h⟩ ≤ 0`, so
   `Σt^{(m)} → 0`, and entries are bounded by `3Σt^{(m)}`), hence `y = q ⪰ 0`, against `(gh)†y(gh) < 0`. (With C22.3,
   `cl cone Z = cone Z` and C18-1's argument applies verbatim; C23-5 is the closed-hull form.)

**Decision rule (fixed now, the node's).** **EXPLICIT** iff a cone with H1–H3 and `G_T`-invariance is exhibited with exact
checks on a finite certificate set plus a compact-form theorem; **OBSTRUCTED** iff (every seed orbit meets an orthogonal
pair for `c < 2`: C23-1 holds with exact instances in all five classes and its two identities are verified) **and** (the
balanced engine fails: C23-3 with the exact rank instance for `r = 3`, the exact partner, zero-pairing and tightness
instances for each `r = 2` class, and the exact product-in-orbit instances for two vanishing coordinates) — each part
also passing the independent checker; **OPEN** otherwise. Expected: OBSTRUCTED. Then an explicit cone for `G_T` stays OPEN,
existence at claim (D) [A] through B7-2 (HO-36 item 2), and **no row of this node is evidence for outcome (D)** (no cone
is produced).

**Productivity test.** Gem iff strictly stronger than "the tower's closure has no known explicit cone": here, that **no
surgery-type cone — rank-one with any weights, or balanced through the engine — is invariant under all the tower's stages
at once** (through the closure step), extending HO-36 item 1 from HO-24's cone to the whole surgery class, and the
universal orthogonal pair with its rank classification as a mechanism other torus nodes can reuse. Below that: record
only.

## Hypothesis classification (standing rule 1; owner's point (1))

`G_T`-invariance is the (b)-instance under test (reading: invariance); H1 and H3 are introduced (the composite-cone
conditions, not OI premises); no OI inventory item is used. Lemma C18-1 [W], C13-O [W], the engine's statement (C17.1 [D])
and C22.1 [D] are cited at their labels. Scope: at the audited scope — the stage-6 inventory at L, level (i) (pair cones on
two copies of the ball; `G_T` acts by `CNOT` and on the target token); the obstruction concerns the surgery and balanced
routes only, not every cone, not every extension of OI, and not availability.

## S0 — predictions and decision rules for the scripts (written before the first run)

### `experiments/c23_torus.py` (the construction; exact: Fractions and Gaussian rationals; sympy for identities)
- **G1** group structure: `R_B(t) = D(1, w)`, `CNOT D(u, v) CNOT = D(v, u)`, `X_B D(u, v) X_B = uv D(1/u, 1/v)` (symbolic,
  `u, v` invertible symbols, `ū = 1/u` on the torus); `CNOT`, `X_B` generate the four permutations of `V4`; countercontrol:
  the 3-4-5 rotation on the target, `1 ⊗ [[3/5, −4/5], [4/5, 3/5]]`, is not monomial. Predicted: as stated.
- **G2** C23-1: the inner-product identity (symbolic in the eight real coordinates and `u, v`), the modulus identity
  (symbolic, `u = (1 − t² + 2it)/(1 + t²)`); exact instances: (i) `h = (6, i, 4, 3)`, `(u, v) = (1, −(3 + 4i)/5)`;
  (ii) `h = (2, 3i, 1, 6)`, `(1, −i)`, and `v(u) = −i` at `u ∈ {i, (3 + 4i)/5, (5 + 12i)/13}`; (iii) `h = (3, 1, 2i, 0)`,
  `(1, −1)`; (iv) `h = (3, 0, 2i, 1)`, `(1, 1)`; (v) `h = (2, 0, 0, 1 + i)`, `(1, 1)`; each `⟨h|gh⟩ = 0` with `gh ∉ ℂh`.
  Countercontrol: for (i), `v = 1` gives a nonzero product. Predicted: as stated.
- **G3** C23-2 (a): seeds `h = (6, i, 4, 3)` at `c* = 51/50` and `h₂ = (4, i, 2, 3)` at `c₂ = 101/100`, both unreachable
  (`|det Ψ|²_min/|h|⁴ = 49/961`, `25/900` by the formula `min((|h₀h₃| − |h₁h₂|)², (|h₀h₂| − |h₁h₃|)²)/|h|⁴` [W]) with H1
  (`1 − 4D_min ≤ (2/c − 1)²`); `λ = 1/98`; the witness `y = P_h + λd_{gh}` with `g` from G2 (i): `⟨y, d_h⟩ = 0`,
  `(gh)†y(gh)/|gh|² = λ(1 − c*) < 0`, and on 200 sample defects of the two orbits (25 rational torus points × 4 `σ` × 2
  seeds): `⟨y, d⟩ ≥ 0`, equal to C18-1's identity, `⟨d, d_h⟩ > 0`, H1 at each sample. Countercontrol (C18's A1-cc): on the
  `c*` orbit carried at both values, the witness built with `c₂` pairs negatively with the `c*` copy of `d_h`. Predicted:
  as stated.
- **G4** C23-2 (b)–(c): the determinant identity (symbolic); the transported stage-4 pair `y′, w′` (permutation
  `π = [0, 3, 1, 2]` of z2e's basis `(|0+⟩, |1−⟩, |0−⟩, |1+⟩)`): `y′ = q₀′ + ℓ₁′(u₀, 7/17)` with `q₀′` PSD (all principal
  minors `≥ 0`, exact) and `|u₀| ≤ 7/17`; `w′ = P_v′ + ℓ₁′(ζ, 17)` with `|ζ| ≤ 17`; both in `L₁′* ∩ L₂′*`
  (`2|Y₀₃| ≤ Y₁₁ + Y₂₂`, `2|Y₁₂| ≤ Y₀₀ + Y₃₃`); `tr(y′w′) = −6/625`; `1 ⊗ H′` (`H′ = [[1, 1], [1, −1]]`) maps the rays
  `C1(γ) ↦ C1′(γ)`, `C2(γ) ↦ C2′(γ)` (exact at `e^{iγ} ∈ {1, i, (3 + 4i)/5}`); mixture instance: `h = (3, 2i, 2, 1)`
  (unreachable, `max((|h₀| + |h₃|)², (|h₁| + |h₂|)²) = 16 ≤ 18 = |h|²`) at `c* = 1001/1000` with H1, its C18-1 witness pairs
  `≥ 0` with sampled Bell defects on both circles (`w ∈ {±1, ±i, (±3 ± 4i)/5}`) and with its own orbit samples. Countercontrol:
  `P_{(1, 0, 0, 1)}` violates `L₁′*`. Predicted: as stated.
- **G5** C23-3: (a) `h = (6, i, 4, 3)`: partners `g_uh` at `u ∈ {1, i, (3 + 4i)/5, (5 + 12i)/13}`: rank 3; the system
  `{k ⊥ g_uh}` has nullspace exactly `ℂh`; with `k ⊥ h` added, nullspace `{0}`. Countercontrol: replacing one partner by
  `D(u, 1)X_Bh` (not orthogonalizing) gives rank 4. (b) for each `r = 2` seed — (ii) `h = (2, 3i, 1, 6)`, (iii)
  `h = (3, 1, 2i, 0)`, (iv) `h = (3, 0, 2i, 1)` — partners at four rational `u`: rank 2; the unique partner (nullspace
  dimension 1 after `k ⊥ h`), predicted `k₀ ∝ (1, −6i, −2, 3)`, `(3, 1, −5i, 0)`, `(−5, 0, 6i, 3)`; zero pairing
  `⟨d, gdg†⟩ = 0` for the four sampled `g ∈ O_X` (at `c = 3/2`); `p₁ + p₂ ≠ 0`; tightness with `U = D(u_ε, 1)`: at `c = 3/2`,
  `u_ε = (99 + 20i)/101` for all three and `b = 199i/200`, `629i/1000`, `(47 − 443i)/1000`; at `c = 101/100`,
  `u_ε = (99 + 20i)/101`, `(399 + 40i)/401`, `(399 + 40i)/401` and `b = 199i/200`, `(242 + 581i)/1000`, `(322 − 307i)/1000`;
  for each: `u = h + bk₀` with `u†du < 0`, `x = k₀ − (⟨u|k₀⟩/⟨u|u⟩)u`, `x†dx > 0`, `⟨d, UdU†⟩ > 0`, `x†(UdU†)x < 0`.
  (c) `CNOT·(2, 0, 0, 1 + i)` and `CNOT·(0, 2, 1 + i, 0)` are products (`det Ψ = 0`). Predicted: as stated.
- **G6** the certificate `experiments/c23_certificate.json` with every exact datum of G2–G5 (seeds, group elements as
  matrices, witnesses, sample defects with their group elements, the Bell-corner pair with its decompositions, the partner
  systems and the tightness data).

`VERDICT C23-EXACT` iff G1–G6 give the predicted outcomes, countercontrols included (a failed run is kept as
`.run1.*`); the node's label then follows the node's decision rule.

### `experiments/c23_check.py` (the independent verifier; reads only `c23_certificate.json`)
Its own Gaussian-rational arithmetic and its own characterization of the group: a listed element is accepted as an
element of `G_T` (modulo phase) iff it is unitary (`gg† = I` exactly) and monomial with permutation in
`V4 = {e, (23), (01)(23), (01)}` and its four phases `φ_i = g[i][σ⁻¹(i)]` satisfy `φ₀φ₁ = φ₂φ₃` (the condition for
`diag(φ) ∈ U(1)·T²`) — no `(u, v)` parametrization is read. It recomputes every inner product, defect, witness, pairing,
principal minor, rank and quadratic-form value from the listed vectors and matrices; it checks the two identities of
C23-1 and the determinant identity by expanding polynomials in real coordinates (sympy `expand` on real and imaginary
parts), not by the construction's complex simplification. `CHECK C23-CERTIFICATE-OK` iff every item passes. Predicted:
every item passes.
