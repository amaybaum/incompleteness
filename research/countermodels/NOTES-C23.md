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

## Runs (written 2026-10-11T10:35:24Z, `date -u`)
| script | run | result | replay | sha256 (script / out) |
|---|---|---|---|---|
| `c23_torus.py` | 1 (10:31:53Z) | 6/6, `VERDICT C23-EXACT`; certificate written (267 group elements, sha256 `d5841161f024006d1f4951d845253508e8813cd8a71e211264175ab80af60d03`) | identical (`cmp`) | `e6a3555e…` / `e7e58309…` |
| `c23_check.py` | 1 (10:33:52Z) | 9/9, `CHECK C23-CERTIFICATE-OK` | identical (`cmp`) | `c13e14e1…` / `dd7f2aea…` |

Pre-run edits of `c23_torus.py` (before run 1): dead code and a redundant special case removed; no check changed. Every
S0 prediction held (G3's `D_min(h₂) = 25/900 = 1/36`; the checker prints `(gh)†y(gh)` unnormalized, `−31/2450 =
|gh|²·(−1/4900)`).

## Results

### C23-1 — every `G_T`-orbit carries an orthogonal pair [W + X G2, K2, K3]
Lemma C23-1 as stated in the design: the identity `⟨h|D(u, v)X_Bh⟩ = β + uvβ̄ + uα + vᾱ` and the modulus identity
(`|β + uα|² − |ᾱ + uβ̄|² = (|u|² − 1)(|α|² − |β|²)`) are verified symbolically twice by different routes (the construction's
complex simplification; the checker's real-coordinate expansion); the five-class solution is [W]; exact instances in all
five classes, each realized by an element accepted by the checker's own membership test. **Every `G_T`-orbit of rays —
hence, through the closure step, every orbit of the countable group `G_∞` of B10-5's stages taken together, whose
closure is `G_T` — contains an orthogonal pair, realized by `D(u, v)X_B`.**

### C23-2 — the rank-one route is closed [W + X G3, G4, K4–K6 + A Z]
(a) No compact `G_T`-invariant rank-one surgery with every `c < 2` is self-dual (C18-1's witness on the orbit of largest
`c`, Lemma C23-5 for the closed hull); exact instance: `c* = 51/50` on `(6, i, 4, 3)` with a second orbit `(4, i, 2, 3)`
at `101/100`, 200 sample defects, `⟨y, d_h⟩ = 0`, `(gh)†y(gh)/|gh|² = −1/4900`; the maximum is load-bearing (the witness
built with the smaller value pairs `−199/19800`). (b) At `c = 2` the only admissible orbit is `C1′ ∪ C2′`, and its surgery
`= (1 ⊗ H)K_T(1 ⊗ H)†` is not self-dual: stage 4's pair transported and re-verified exactly, `tr(y′w′) = −6/625` with
both in `K*` (decompositions, 15 principal minors, the Lorentz-dual conditions). (c) Mixtures with the Bell circles: not
self-dual under the overlap condition (instance `(3, 2i, 2, 1)` at `1001/1000`, 16 Bell defects and 36 orbit samples);
OPEN otherwise.

### C23-3 — the balanced route: the engine certifies nothing [W + X G5, K7–K9]
Every seed falls in exactly one case: `r = 3` (class (i)): no balanced partner (exact: partners of rank 3,
`{k ⊥ partners} = ℂh`); `r = 2` (classes (ii), (iii), (iv)): the partner is forced (`k₀`, exact and unique), zero pairing holds
on the orthogonalizing family, `p₁ + p₂ ≠ 0` in general (the five subcase formulas, [W]), and the first-order tightness
breaks the local condition (exact instances at `c = 3/2` and `c = 101/100` in all three classes, normalized values
`−0.077 … −0.00024`); two vanishing coordinates: H1 excludes (products in the orbit). So for no seed and no `c ∈ (1, 2)`
does the engine `selfDual_of_local` certify a balanced rank-two surgery on a `G_T`-orbit.

### C23-4 — the node's outcome under its decision rule: **OBSTRUCTED**
Both conditions hold: every seed orbit meets an orthogonal pair (C23-1, all five classes, identities verified twice) and
the balanced engine fails (C23-3, every case, with the instances the rule names), each instance part passing the
independent checker. Consequences, stated at their scope: (1) **no surgery-type cone — rank-one with any weights, or
balanced rank-two through the engine — is invariant under `G_T`**, and therefore (closure step (b) for surgeries; step
(a) with H3 for any closed cone) **none is invariant under all of B10-5's stages `G_n` at once**; this extends HO-36
item 1 (HO-24's cone fails from `n = 3`) to the whole surgery class. (2) An explicit `G_T`-invariant exotic cone stays
**OPEN**; existence stays CONDITIONAL on claim (D) [A] through B7-2 (HO-36 item 2, cited at its label). (3) Nothing here
is evidence for the owner's outcome (D): no cone is produced. Groups named exactly: the countable group `G_∞ = ⋃ G_n`
(each `G_n` finitely generated), its closure `G_T = T² ⋊ V4` (modulo phase); closedness of a cone (H3) is the step from
the one to the other.

### Residual (OPEN)
Mixtures of the Bell circles with orbits outside the overlap condition; balanced rank-two surgeries without the engine
(self-duality not decided); defects with a higher-rank subtracted part and one negative eigenvalue; non-surgery
constructions — C18-3's linear-perturbation lemma does not transfer verbatim (the torus's off-diagonal real blocks pair
up: `E₀₂` (`ū`) with `E₁₃` (`u`) and `E₀₃` (`v̄`) with `E₁₂` (`v`) are equivalent as real representations); the explicit cone.

## Gem classification (§A.31)
- NEW: the universal orthogonal pair for the tower's closure with an explicit realizing element and identities; the
  rank classification of orthogonalizing families (r = 3 ⇔ `αβ ≠ 0`, `|α| ≠ |β|`), which decides when a balanced partner
  exists; the complete failure of the engine on `G_T`; the extension of HO-36 item 1 to the whole surgery class.
  Productivity test met.
- Assumption-watch markers: (1) "an explicit cone invariant under every stage of the tower can be found among surgery
  cones" is false (rank-one and engine-certified balanced); a construction for `G_T` needs a sufficiency argument of
  another kind (as C18's marker for case B). (2) "invariance under a dense subgroup is invariance under its closure" holds
  for closed cones only; the step uses H3 (owner's point (2)), recorded wherever used.

## What is not claimed
No kernel statement (Lemma C23-1's case analysis, Theorems C23-2, C23-3 and Lemma C23-5 are [W]; the identities and
instances are [X], checked twice); no statement about cones outside the surgery and engine routes; the existence of a
`G_T`-invariant exotic cone is HO-36's (claim (D)), not decided here; no availability statement; no claim about OI beyond
the audited scope (the stage-6 inventory at L, level (i), invariance reading).

## Round 6 — forward correction F-C5-1 (appended 2026-10-11T15:20:46Z, `date -u`; the text above stays as written)

**What is corrected, and why.** Design item 2 (b)–(c) above, the Results paragraph C23-2 (b)–(c), row C23.2's `c = 2` and
mixture clauses, C23.6's first residual item and HP-countermodels-11 statement 2 treat the two Bell circles
`C1′ = {|00⟩ + w|11⟩}`, `C2′ = {|01⟩ + w|10⟩}` as a `G_T`-orbit admissible for H1 at `c = 2`. That is false for `G_T`:
`CNOT ∈ G_T` (it lies in every stage `G_n`) carries `|00⟩ + w|11⟩` to `(|0⟩ + w|1⟩) ⊗ |0⟩` and `|01⟩ + w|10⟩` to
`(|0⟩ + w|1⟩) ⊗ |1⟩`, products; the argument of (b) used the torus and `X_B` and omitted `CNOT`. The coordinator's audit
(AUDIT-COUNTERMODELS-R5 §8, finding F-C5-1) found it; HO-42 item 3 is the corrected statement; the bridge reached the same
statement independently (HO-40 items 1–2). This thread's own records already contained the facts that refute it: G3's
`D_min` formula gives `D_min = 0` on these seeds, and C23-3 (c) excludes `(h₀, 0, 0, h₃)`, `(0, h₁, h₂, 0)` by H1 because
`CNOT` maps them to products.

**Admissibility, stated exactly.** H1 (products in `K`) and H3 (`K = K*`) give `K ⊆ maxCone` (the dual of the products),
so every defect `I − cP_h` of a cone with H1 and H3 is block-positive, `c · λ_max(h) ≤ 1` (`λ_max` the largest squared
Schmidt coefficient of the unit `h`); for a surgery `K(Z)`, block-positivity of every defect of `Z` is also sufficient
for H1 (products then lie in `Q ∩ Z*`). For an orbit `G_T·h`, admissibility at weight `c` reads
`c ≤ c_max(h) := 2/(1 + √(1 − 4D_min(h)))`, `D_min(h) = min_{g ∈ G_T} |det Ψ(gh)|²/|h|⁴`.

**The corrected statements (to be checked by `experiments/c23f_correction.py` before they are recorded).**
- **(F-a)** `det Ψ(D(u, v)h) = v(h₀h₃ − u²h₁h₂)`, `det Ψ(CNOT·D(u, v)h) = u(h₀h₂ − v²h₁h₃)`, and the `X_B`-cosets give the
  same two moduli; with `a_i = |h_i|`, `x = a₀a₃ − a₁a₂`, `y = a₀a₂ − a₁a₃`, `S = Σa_i²`: `D_min(h) = min(x², y²)/S²` [W:
  `min_{|u|=1}|A − u²B| = ||A| − |B||`] with exact identities [X].
- **(F-b)** `x + y = (a₀ − a₁)(a₂ + a₃)`, `x − y = (a₀ + a₁)(a₃ − a₂)`, `|x| + |y| = max(|x + y|, |x − y|)`, and the two
  certificates `S²/2 − (x + y)² = (A − B)²/2 + A(a₂ − a₃)² + 2a₀a₁(a₂ + a₃)²`,
  `S²/2 − (x − y)² = (A − B)²/2 + B(a₀ − a₁)² + 2a₂a₃(a₀ + a₁)²` (`A = a₀² + a₁²`, `B = a₂² + a₃²`), each a sum of
  nonnegative terms for `a ≥ 0`. Hence `D_min(h) ≤ ((|x| + |y|)/2)²/S² ≤ 1/8` for every `h ≠ 0`, with equality at
  `h* = (√2/2, 0, 1/2, 1/2)`; so **H1 and H3 admit a rank-one defect orbit of `G_T` only at weights
  `c ≤ c_max(h) ≤ 2/(1 + 1/√2) = 4 − 2√2 ≈ 1.1716`**, the bound attained on the orbit of `h*`. In particular **no `G_T`-orbit
  is admissible at `c = 2`**, and none at any `c ∈ (4 − 2√2, 2]`.
- **(F-c)** Consequence for C23-2: every `G_T`-invariant set `Z` of rank-one defects `I − c_dP_d` (`c_d > 1`) whose
  surgery has H1 and H3 has every weight `≤ 4 − 2√2 < 2`; and the compactness hypothesis of C23-2 (a) costs nothing:
  `K(Z) = K(cl Z)` (step (b) of the closure paragraph above), `cl Z` is compact and `G_T`-invariant, its points are
  defects with weights in `(1, 4 − 2√2]` or PSD limits `I − P` (weight 1), and C18-1's identity
  `⟨y, d_l⟩ = c*(1 − s_{hl}) + (c* − c_l)(s_{hl} + λ) + λc*c_l s_{h′l}` is nonnegative for every `c_l ∈ [0, c*]`; so the
  maximum `c*` (attained on `cl Z`, an orbit with an orthogonal pair by C23-1) gives `y ∈ K(Z)* \ K(Z)`. **No `G_T`-invariant
  rank-one surgery satisfies H1 and H3, with any weights and any number of orbits, closed or not** — the rank-one route for
  `G_T` is closed with no residual (HO-42 item 3; it also covers HO-40 item 3's "unattained supremum of `c`" for `G_T`).
  C23.2's verdict and C23.4 (OBSTRUCTED) stand.
- **(F-d)** The Bell-circle statements of C23-2 (b)–(c) are statements about the subgroup `T² ⋊ ⟨X_B⟩` (no `CNOT`): it
  maps `C1′ ∪ C2′` onto itself, every point of `C1′ ∪ C2′` is maximally entangled (admissible at `c = 2`), and the surgery on
  the two circles is `(1 ⊗ H)K_T(1 ⊗ H)†`, not self-dual by the transported stage-4 pair (`tr(y′w′) = −6/625`, C23's G4); the
  mixture instance `(3, 2i, 2, 1)` at `1001/1000` with the Bell circles at `c = 2` is likewise a `T² ⋊ ⟨X_B⟩` statement.
  For `G_T` a set containing a Bell defect at `c = 2` contains the `c = 2` defect of its `CNOT` image, which pairs `−1` with
  that product, so H1 and H3 exclude it. C23.6's first residual item (mixtures outside the overlap condition) does not
  arise for `G_T`; it remains a question for `T² ⋊ ⟨X_B⟩` only.
- **(F-e)** Scope of C23-3, stated more exactly (audit §10, no change of substance): the engine `selfDual_of_local` takes a
  finite family; what C23-3 shows is that its local condition fails on a pair inside every `G_T`-orbit, which also blocks
  any compact extension that keeps the same local condition.
- **(F-f)** The closure step in rule (iii)'s form (round 6): from invariance under the countable dense subgroup
  `G_∞ = ⋃G_n` to invariance under its closure `G_T`. Closure premise: the cone is **closed** — H3 (`K = K*`; a dual cone is
  closed), introduced, not an OI premise; LIMCLOSE-C (an availability closure premise) is not used. Form of transfer:
  none in this thread's invariance reading (the group acts on the pair cone by conjugation); a route that starts from the
  availability of `G_∞`'s elements would need the transfer clause for unitaries, (T)_𝓘 (HO-39 item 2), to reach
  invariance under `G_∞`, and then H3 for the closure. Closedness of the cone used: `K` closed, from H3.

**Design of the check (exact; Fractions, Gaussian rationals; sympy for the identities and for `√2`).**
- **F1** For ten rational `w` (`±1, ±i, (±3 ± 4i)/5, (5 + 12i)/13, (8 + 15i)/17`) and both circles: `b = (1, 0, 0, w)`,
  `(0, 1, w, 0)` are maximally entangled (`|det Ψ|²/|b|⁴ = 1/4`); `CNOT·b` is a product (`det Ψ = 0`); the `c = 2` defect of
  `CNOT·b` has `(CNOT b)†d(CNOT b)/|b|² = −1`. Symbolically: `det Ψ(CNOT·D(u, v)·(1, 0, 0, w)) = 0`,
  `det Ψ(CNOT·D(u, v)·(0, 1, w, 0)) = 0`. `CNOT` is the permutation `(2 3)` and lies in `G_1`. Predicted: as stated.
- **F2** The four coset determinant identities (symbolic in `h` and `u, v`); the formula `D_min = min(x², y²)/S²` on 12
  exact seeds against an exact minimization over the orbit's two moduli (the minimum of `|A − u²B|²` attained at the
  rational point `u² = (A B̄)/|AB|`… realized by exact algebraic values where the seeds are chosen so that `A B̄/|AB|` is a
  rational square; else compared through `(|A| − |B|)²` with `|A|, |B|` as exact square roots). Predicted: identities hold;
  formula agrees on every seed.
- **F3** The two factorizations and the two certificates of (F-b) by `sympy.expand` (difference zero). Predicted: zero.
- **F4** At `h* = (√2/2, 0, 1/2, 1/2)` (sympy exact): `x² = y² = 1/8`, `D_min = 1/8`, `c_max = 4 − 2√2` exactly, and
  `(4 − 2√2)·(2 + √2)/4 = 1`; the round-5 instances `51/50`, `101/100`, `1001/1000` are `< 4 − 2√2`; the weight `6/5` is
  `> 4 − 2√2`. Predicted: as stated.
- **F5** Exhaustive exact control of `D_min ≤ 1/8` over moduli: every `a ∈ {0, …, 6}⁴` (integers) and every
  `m = (a_i²) ∈ {0, …, 9}⁴` with `a_i = √m_i` (exact through `min(P, Q) − 2√(m₀m₁m₂m₃) ≤ S²/8`, squared when needed): no
  violation; the maximum of `D_min` equals `1/8` and is attained (at `m = (2, 0, 1, 1)` and its images). Predicted: no
  violation; maximum `1/8`.
- **F6** Countercontrols and consequences: (a) without `CNOT` (the group `T² ⋊ ⟨X_B⟩`) the orbit of `(1, 0, 0, 1)` keeps
  `|det Ψ|²/|h|⁴ = 1/4` at 16 sampled torus points and under `X_B` — the bound `1/8` fails for that subgroup, so `CNOT` is
  load-bearing; (b) `T² ⋊ ⟨X_B⟩` maps sampled points of `C1′ ∪ C2′` into `C1′ ∪ C2′` (exact), while `CNOT` maps them to
  products; (c) the mixture seed `(3, 2i, 2, 1)` has `D_min = 1/324` under `G_T` and is admissible at `1001/1000`, but a
  `G_T`-invariant set containing it and a Bell defect at `c = 2` contains a non-block-positive defect (F1); (d) C18-1's
  identity holds symbolically in `(c*, c_l, s, s′)` and its three terms are nonnegative at `c_l ∈ {0, 1, c*}` for
  `c* = 51/50` (sampled `s, s′`). Predicted: as stated.

Decision rule (fixed now): `VERDICT C23F-EXACT` iff F1–F6 give the predicted outcomes, countercontrols included (a failed
run is kept as `.run1.*`). Then rows C23.2c (the corrected statement, CONDITIONAL), C23.2bf (the refuted sub-claim of
C23-2 (b), FAILED) and C23.6c (the residual after the correction, OPEN) are appended to RESULTS; no existing row is edited
and no existing label changes. Any other outcome: the correction is recorded only as received (HO-42 item 3 at its label)
and the discrepancy is examined before any row is written.
