# NOTES-C23 — the 2-torus group of the tower's closure: an explicit invariant cone, or the obstruction

Round-5 node C23, opened after C22's second dispatch; S0 written 2026-10-11T08:34:52Z (`date -u`), before any C23 script ran. Object
(HO-36 item 2, HO-35 item 3, NOTES-B10 §4–§5 read at `research/bridge` @ `a34d20b5`): the closure of B10-5's locally
finite tower. Conventions: computational basis `|00⟩, |01⟩, |10⟩, |11⟩` (control first; indices `0, 1, 2, 3`),
`CNOT` the permutation `(2 3)`, `X_B = 1 ⊗ X` the permutation `(0 1)(2 3)`, `R_B(t) = 1 ⊗ diag(1, e^{it})`; defects
`d_h = I − cP_h`, `P_h = hh†/|h|²`; `K(Z) = (Q ∩ Z*) + cl cone Z` (the closed conic hull, C22's `surgeryC`; equal to
`(Q ∩ Z*) + cone Z` whenever `cone Z` is closed, NOTES-C13 C13-S [W]). Reading of every statement: **invariance**
(cone-preserving admissibility); nothing here is about operational availability (HO-33 item 5; C21 safeguard).

## Groups, named exactly (owner's point (2))

- **The finitely generated group** `G_∞ := ⟨CNOT, X_B, R_B(2π/2ⁿ) : n ≥ 1⟩ = ⋃_n G_n`, `G_n = ⟨CNOT, X_B, R_B(2π/2ⁿ)⟩`
  (B10-5's stages; `|G_n| = 4^{n+1}` modulo phases, NOTES-B10 T8 [X there], not relied on). Countable.
- **Its topological closure** `G_T := cl(G_∞) = cl⟨CNOT, X_B, R_B(t) : t ∈ ℝ⟩`. Claim (G, [W + X]): as unitaries modulo
  phase, `G_T = T² ⋊ V4` with the 2-torus `T² = {D(u, v) := diag(1, uv, u, v) : |u| = |v| = 1}` and
  `V4 = {1, CNOT, X_B, X_B·CNOT}` acting as the permutations `{e, (23), (01)(23), (01)}`: `R_B(t) = D(1, e^{it})`,
  `CNOT·R_B(t)·CNOT = D(e^{it}, 1)`, so `T² ⊆ G_T`; `CNOT·D(u, v)·CNOT = D(v, u)` and `X_B·D(u, v)·X_B ∝ D(ū, v̄)`, so
  `T² ⋊ V4` is a closed group containing the generators; the dyadic points `(ω_n^a, ω_n^b)` are dense in `T²`, so
  `cl(G_∞) ⊇ T²`. The density step is [W] (standard); the conjugation identities are [X] (symbolic in `u, v`).
- **The step from `G_∞` to `G_T`** (owner's point (2)): a cone `K` invariant under `G_∞` and **closed** is invariant
  under `G_T` (`g = lim g_m`, `g_m K = K` ⇒ `gK ⊆ K` and `g⁻¹K ⊆ K` by closedness) [W]; H3 (`K = K*`) gives
  closedness (a dual cone is closed). For a rank-one surgery over the countable orbit `Z₀ = G_∞·d_h`: `Z₀* = (cl Z₀)*`
  and `cl cone Z₀ = cl cone (cl Z₀)`, so `K(Z₀) = K(cl Z₀) = K(G_T·d_h)` [W]. Every statement below about `G_T`
  therefore applies to `G_∞` (to every cone invariant under all stages at once) through this step.

## Question, design, productivity test (§A.31)

**Question.** Is there an explicit `G_T`-invariant closed self-dual cone with H1–H3 (`≠ Q3`), or is there an obstruction
to the explicit routes available (rank-one orbit surgeries with any `c`-weights, C13-O/C18-1; balanced rank-two
surgeries through the engine `selfDual_of_local`, C17.1 [D]/C18-2)?

**Design (fixed before the first run).**
1. **Lemma C23-1 (universal orthogonal pair).** For `h ∈ ℂ⁴` put `α = h̄₂h₃`, `β = h̄₀h₁`. Then
   `⟨h | D(u, v) X_B h⟩ = β + uv β̄ + u α + v ᾱ` (symbolic identity), and for every `h ≠ 0` some `(u, v) ∈ T²` makes it
   vanish, in five classes: (i) `αβ ≠ 0`, `|α| ≠ |β|`: every `u`, with `v = −(β + uα)/(ᾱ + uβ̄)` (unimodular by the
   identity `|β + uα|² = |ᾱ + uβ̄|²` for `|u| = 1`); (ii) `|α| = |β| ≠ 0`: every `u` with `ᾱ + uβ̄ ≠ 0`, same `v`;
   (iii) `α = 0 ≠ β`: `uv = −β/β̄`; (iv) `β = 0 ≠ α`: `v = −uα/ᾱ`; (v) `α = β = 0`: every `(u, v)`. Hence **every
   `G_T`-orbit of rays contains an orthogonal pair** — the element realizing it is `D(u, v)·X_B` (the double
   transposition `(01)(23)` with the torus moving the relative phases inside both swapped pairs, the mechanism of
   NOTES-C16's marker). Classes (iii)–(v) are the seeds with a vanishing coordinate pair; class (v) (`h₀h₁ = h₂h₃ = 0`)
   contains the products and the Bell-type states `(h₀, 0, 0, h₃)`, `(0, h₁, h₂, 0)`.
2. **Theorem C23-2 (rank-one route closed).** No rank-one surgery `K(Z)`, `Z` a finite union of `G_T`-orbits of
   defects `I − c_iP_{h_i}` with `c_i ∈ (1, 2)`, is self-dual: the orbit of largest `c` carries an orthogonal pair
   (C23-1), and Lemma C18-1 (C13-O for one value) gives the exact witness `y = P_h + λ d_{gh}`, `λ = (c* − 1)/(4 − 2c*)`,
   in `K* \ K` — with the closed-hull form of the decomposition step (Lemma C23-5 below). **The Bell corner.** A `T²`-orbit
   consists of maximally entangled states iff `h ∈ C1′ ∪ C2′`, `C1′ = {(|00⟩ + w|11⟩)/√2}`, `C2′ = {(|01⟩ + w|10⟩)/√2}`
   (symbolic: `|det Ψ(D(u, v)h)|² = |h₀h₃ − u²h₁h₂|²`, constant in `u` iff `h₀h₃h₁h₂ = 0`, then `= 1/4` only on the two
   circles); `X_B` swaps the circles, so the only orbit admissible for H1 at `c = 2` is `C1′ ∪ C2′`, whose surgery is
   `(1 ⊗ H) K_T (1 ⊗ H)†` with `K_T` stage 4's refuted cone ([A] Z: an exact pair `y, w ∈ K_T*` with `tr(yw) = −6/625`),
   `1 ⊗ H` carrying the S2 circles `(|0±⟩ + w|1∓⟩)/√2` onto `C1′, C2′`; the pair is transported to the computational
   basis and re-verified exactly here (Gaussian rationals; membership in `K*` through a PSD part plus a Bell-cone part,
   and the dual conditions `tr y − y_aa − y_bb ≥ 2|y_ab|` for both circles). Mixtures (the Bell circles at `c = 2` with
   other orbits at `c < 2`) are not covered by C18-1 and are recorded OPEN as in C18.8, except where a C18.2-type bound
   decides them (not attempted here).
3. **Lemma C23-3 (balanced route: the engine fails).** The engine `selfDual_of_local` needs zero pairing on every
   orthogonal pair (C18-2 (b)). (a) For a seed with `h₀h₁h₂h₃ ≠ 0` (classes (i)–(ii)) the orthogonal partners
   `g_u h = D(u, v(u))X_B h = (h₁, uv h₀, u h₃, v h₂)` span a 3-dimensional space as `u` varies (the coordinate
   functions `1, u, v(u), uv(u)` satisfy exactly one linear relation, `β + β̄uv + αu + ᾱv = 0`, and `v` is not affine in
   `u` since `β ≠ 0`); its orthogonal complement is `ℂh` (as `h ⊥ g_u h` for all `u`); so a balanced partner `k ⊥ h` with
   `k ⊥ g_u h` for all `u` is `0`: **no balanced rank-two defect has zero pairing on its orthogonal partners**, and the
   engine certifies nothing. (b) For a seed with a zero coordinate (class (iii)/(iv), e.g. `h = (h₀, 0, h₂, h₃)`) the
   partner family is 2-dimensional and `k₀ ∝ (−(p₂ + p₃)/h̄₀, 0, h₂, h₃)` gives zero pairing on all of it; but the local
   condition fails for nearby torus images (C18.4's tightness mechanism): an exact instance with `U = D(u_ε, 1)`, a cap
   point `u` of `d = I − cP_h − (2 − c)P_{k₀}` and `x ⊥ u` with `x†(UdU†)x < 0`, `⟨d, UdU†⟩ > 0`. (c) Class (v) seeds
   `(h₀, 0, 0, h₃)` (non-Bell, `|h₀| ≠ |h₃|`): the partner planes are orthogonal for every torus element; the engine's
   failure on the circle is shown by the same tightness instance. Whether any balanced surgery is self-dual is **not**
   decided (OPEN, as C18.8).
4. **Lemma C23-5 (closed-hull form of the decomposition step).** In C13-O/C18-1 with `Z` compact and `K = (Q ∩ Z*) +
   cl cone Z`: if `y = q + z`, `q ∈ Q ∩ Z*`, `z ∈ cl cone Z`, and `⟨y, d_h⟩ = 0` with `⟨d, d_h⟩ ≥ 4 − 2c* > 0` for every
   `d ∈ Z`, then `z = 0`: `z = lim Σ t^{(m)}_k d_k^{(m)}`, `0 ≤ ⟨z, d_h⟩ = lim Σ t^{(m)}_k ⟨d_k^{(m)}, d_h⟩ ≥ (4 − 2c*) limsup
   Σ_k t^{(m)}_k` forces `Σ t^{(m)} → 0`, and entries are bounded by `3 Σ t^{(m)}`, so `z = 0` and `y = q ⪰ 0`, against
   `(gh)†y(gh) < 0`. [W]

**Decision rule (fixed now, the node's):** **EXPLICIT** iff a cone with H1–H3 and `G_T`-invariance is exhibited with
exact checks on a finite certificate set plus a compact-form theorem; **OBSTRUCTED** iff (every seed orbit meets an
orthogonal pair for `c < 2`, i.e. Lemma C23-1 holds in all five classes with exact instances) and (the balanced engine
fails: C23-3 (a) with an exact rank instance and (b)/(c) with exact tightness instances); **OPEN** otherwise. The
expected outcome is OBSTRUCTED; an explicit cone for `G_T` then stays OPEN with existence at claim (D) [A] through B7-2
(HO-36 item 2), and no (D)-evidence row is written for this node (no cone is produced).

**Productivity test.** Gem iff the result is strictly stronger than "the tower's closure has no known explicit cone":
here, that **no surgery-type cone (rank-one with any weights, or balanced through the engine) is invariant under all
stages of the tower at once** — which constrains HO-36's "the stages' explicit cones are not one cone carried up the
tower" from HO-24's cone to the whole surgery class — and the universal orthogonal pair as a mechanism (a double
transposition whose two swapped pairs both see a free relative phase) applicable to other torus nodes. Below that bar:
record only.

## Hypothesis classification (standing rule 1; owner's point (1))

Cone geometry: `G_T`-invariance (the (b)-instance under test, invariance reading), H1 and H3 (introduced, not OI
premises); no OI inventory item is used. Lemma C18-1, C13-O, Theorem S′ and the engine are cited at their labels
(C18-1 [W], C17.1 [D] for the engine's statement). Scope: at the audited scope — the stage-6 inventory at L, level (i)
(the pair cone on two copies of the ball, `G_T` acting on the target token and through `CNOT`); the obstruction says
nothing about cones outside the surgery/balanced classes, nothing about every conceivable extension of OI, and nothing
about availability.

## S0 — predictions and decision rules for the scripts (written before the first run)

### `experiments/c23_torus.py` (exact: Fractions, Gaussian rationals; sympy for the symbolic identities)
- **G1** the conjugation identities and `R_B(t) = D(1, e^{it})`, `CNOT R_B CNOT = D(e^{it}, 1)` (symbolic `u, v`; `X_B D X_B
  = uv·D(ū, v̄)`), `G_n ⊆ T² ⋊ V4` on the generators. Countercontrol: `1 ⊗ R_x(t)` (not in the group) is not of the form
  `D·σ` for any `σ ∈ V4`. Predicted: as stated.
- **G2** Lemma C23-1's identity (symbolic) and the modulus identity `|β + uα|² = |ᾱ + uβ̄|²` for `|u| = 1` (symbolic with
  `u = (1 − t²+ 2it)/(1 + t²)`); exact instances of the five classes with Gaussian-integer seeds: (i) `(3, 1 + i, 2, −1 + 2i)`,
  (ii) a seed with `|α| = |β|` (`(2, 1, 1, 2i)`), (iii) `(2, 1 + i, 0, 3)`, (iv) `(0, 2, 1 + i, 3)`, (v) `(2, 0, 0, 1 + i)`;
  for each, `(u, v)` exact unimodular Gaussian rationals and `⟨h | D(u, v) X_B h⟩ = 0`. Countercontrol: for seed (i) a
  wrong `v` (`v = 1`) gives a nonzero inner product. Predicted: all zero; countercontrol nonzero.
- **G3** Theorem C23-2 on the class-(i) seed: `c* = 51/50` (and a second orbit at `c₂ = 101/100` seeded by
  `(1, 2i, 3, 1 + i)`), the witness `y = P_h + λ d_{gh}`: `⟨y, d_h⟩ = 0`, `⟨y, d⟩ ≥ 0` for a sample of 40 orbit defects
  of both orbits (torus points at rational angles, all four `σ`), `⟨d, d_h⟩ ≥ 4 − 2c*` on the sample, `(gh)†y(gh) < 0`;
  the identity `⟨y, d_l⟩ = c*(1 − s_{hl}) + (c* − c_l)(s_{hl} + λ) + λc*c_l s_{h′l}` on the sample. Predicted: as stated.
- **G4** the Bell corner: `|det Ψ(D(u, v)h)|² = |h₀h₃ − u²h₁h₂|²` (symbolic); the two circles are the only admissible
  orbits (the constancy criterion, symbolic); `1 ⊗ H` carries the S2 circles onto `C1′, C2′` (symbolic `w`); the
  transported Z pair `y_B, w_B`: `tr(y_B w_B) = −6/625`; `y_B ∈ K(C1′ ∪ C2′)*` and `w_B ∈ K(C1′ ∪ C2′)*` by exact
  certificates (a PSD part by exact LDLᵀ/characteristic-polynomial signs plus a Bell-cone part `ℓ(u, L)` with `|u| ≤ L`,
  and the dual conditions on both circles). Countercontrol: the pure state `P_{(1,0,0,1)}` is not in `K*` (fails the
  C1′ dual condition). Predicted: as stated.
- **G5** balanced route: (a) class-(i) seed: four orthogonal partners `g_{u_j} h` at `u_j ∈ {1, i, (3 + 4i)/5, (5 + 12i)/13}`,
  exact rank 3, and the solution space of `k ⊥ g_{u_j} h (j = 1..4)` is `ℂh` (exact nullspace); countercontrol: without
  the relation (a generic 4-tuple of vectors) the rank is 4. (b) class-(iii) seed `h = (3, 0, 2, 1 + i)` hmm — a seed with
  `h₁ = 0`: `k₀`, the zero-pairing identities `k₀ ⊥ g_u h`, `h ⊥ g_u k₀`, `k₀ ⊥ g_u k₀` for sampled `u` (and symbolic); the
  tightness instance with `c = 3/2`, `U = D((399 + 40i)/401, 1)`, a cap point and `x ⊥ u` in `span(h, k₀)` with
  `x†(UdU†)x < 0`, `u†du < 0`, `⟨d, UdU†⟩ > 0`; control: at `U = 1`, `x†dx > 0`. (c) the class-(v) seed `(2, 0, 0, 1 + i)`
  with its `k₀ ∝ (−(1 − i), 0, 0, 2)`: the same tightness instance with `U = D(1, u_ε)`. Predicted: (a) rank 3,
  nullspace `ℂh`; (b), (c) negative values at the stated points, positive at `U = 1`. (The cap point and `x` are chosen
  by a float scratch computation before run 1, disclosed here; the recorded check is exact.)
- **G6** the certificate file `experiments/c23_certificate.json` is written with every exact datum above (seeds, `(u, v)`,
  group elements as matrices, witnesses, sample defects with their group elements, the Bell-corner pair with its
  decompositions, the balanced instances); the checker `experiments/c23_check.py` reads only this file.

`VERDICT C23-EXACT` iff G1–G6 give the predicted outcomes, countercontrols included; the node's label follows the
node's decision rule above.

### `experiments/c23_check.py` (the independent verifier; reads only `c23_certificate.json`)
Its own Gaussian-rational matrix arithmetic, no formula of the construction: for each listed group element it checks
unitarity and the form `D(u, v)·σ` with `|u|² = |v|² = 1` and `σ ∈ V4`; for each class it recomputes `⟨h | g h⟩` from
the matrices and checks it is `0`; for each witness it recomputes `y` from the listed `h`, `g`, `c`, `λ`, checks
Hermiticity, `y − P_h − λ d_{gh} = 0`, every listed sample defect as `g′ d_h g′†` with `g′` of the stated form, the
pairings `⟨y, d′⟩ ≥ 0`, `⟨y, d_h⟩ = 0`, `(gh)†y(gh) < 0`, and `⟨d′, d_h⟩ ≥ 4 − 2c*`; for the Bell corner it checks the
PSD parts (its own exact principal-minor test), the Bell-cone parts, the dual conditions on both circles (as inequalities
between rationals, squares for moduli) and `tr(y_B w_B) < 0`; for the balanced instances it recomputes the rank, the
nullspace dimension and the quadratic-form values from the listed matrices. `CHECK C23-CERTIFICATE-OK` iff every item
passes. Predicted: every item passes.
