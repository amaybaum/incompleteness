# Thread N — the ellipsoid / K∞-R step (result)

Read-only research against certified main `L = f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`. Nothing here is landed or
governed. Paths are under `verification/lean-mathlib/OIBridge/`. KF = `KInfFoundations.lean`, OG =
`OrbitGeneration.lean`, ON = `OrbitNormalization.lean`. Line numbers were checked at L (NOTES.md has the table).

**Evidence levels.**
- **kernel**: a landed identifier at L. No new kernel result is claimed.
- **exact**: `n_checks.py`, which prints `OK -- 66 checks`. The replay is byte-identical. sha256 of the script is
  `7b8d0ab5…cdf0`, and of the output `3f996bc5…7f58`. It uses sympy rationals, exact radicals and symbolic trig.
- **written**: an argument given here.
- **citation**: literature. Lowenthal's paper was not readable through the proxy; its formula is taken from a search
  summary and independently re-derived here (written).

**Input IIP.** IIP is the proposed interface, treated as a named premise and nothing more. Let `Ω ⊆ ℝⁿ` be compact and
convex with nonempty interior. Then every affine `g` with `g '' Ω = Ω` fixes the centroid `c`, and its linear part `A`
satisfies `A S Aᵀ = S`. Here `S` is the second-moment matrix, which is positive definite. The inner product of this
report is `⟨u,v⟩ = uᵀS⁻¹v`, and Q denotes its quadratic form.

**Input DIM3.** The affine dimension of Ω is exactly 3. It is never derived.

**The drive.** D is an arbitrary `ElementaryDrivability Ω` (KF:264). It is never taken from
`elementaryDrivability_of_substratum` or from any sourcing route.

***

## Verdicts

| # | question | verdict | level |
| --- | --- | --- | --- |
| 1a | flow members and `J` orthogonal about `c` for ⟨,⟩ | **yes**, from IIP plus `preservesBody_drive` (OG:161) | written + exact X1 |
| 1b | flow inside one rotation circle `SO(2)_a` | **yes**, using only `flow_add`, `flow_preserves`, the J fields and DIM3+IIP. No continuity, no NOT fields | written + exact X2, X3 |
| 1c | flow *equal to* the full circle | **needs `flow_continuous`**; without it the image is only dense in the circle | written |
| 1d | role of `t₀`, `N_involutive`, `N_moves` | **inert** for all of (1)–(5). `J_off_axis` already forces a non-trivial flow; `N_involutive` only identifies N as the half-turn about a | written |
| 2a | which field gives non-parallel axes | `J_off_axis` exactly as landed, compared on Ω. Under DIM3+IIP it is **equivalent** to `B a ∉ {±a}`, where B is J's linear part | written + exact X4, X5 |
| 2b | can J conjugate the flow to the same circle while satisfying `J_off_axis`? | **no** in dimension 3: every axis-preserving `B ∈ O(3)` sends `flow t` to `flow(±t)` (X4). An off-axis clause read on V instead of Ω *would* be too weak (X13) | exact |
| 2c | closure of ⟨flow, J⟩ | **⊇ SO(3)** for ⟨,⟩ about c; it equals SO(3) iff `det J = 1`, and is O(3) otherwise (X5.5). This holds **without** `flow_continuous` | written |
| 3 | exact finite words | **yes**, given `flow_continuous`. Every rotation is an alternating product of `N(α) = ⌈π/α⌉+1` circle elements, where α ∈ (0, π/2] is the angle between the axes. This is sharp for every α. There is no uniform bound over drives (α → 0) | written + exact X7 + citation |
| 3′ | K∞-R (`BoundaryTransitive Ω (words …)`) | **holds** given DIM3 + IIP + D, with `flow_continuous` **load-bearing**. In the Hamel model (2c and 4 hold, 3 fails) closure-transitivity holds and K∞-R fails | written |
| 4 | ellipsoid | Ω = {x : Q(x−c) ≤ R²} with R > 0. Needs Ω closed, convex, bounded (compact) and with nonempty interior. Closure-invariance suffices, so **no continuity** is needed | written + exact X11 |
| 5a | dimension 3 load-bearing for (2) | **yes**. On B⁴, with `R(t)⊕I₂` and the block swap, IIP and every drive field hold, yet neither the words nor their closure is transitive on S³ (X8.1–8.4). The bidisk is a drivable non-ellipsoid (X8.5) | exact |
| 5b | dimension ≤ 2 (B6) | **falls out of (1)**. In O(2), J sends `R(θ)` to `R(±θ)` = `flow(±t)`, so `J_off_axis` fails. In dimension 1 the flow is trivial. No continuity or NOT fields are used | written + exact X6 |

***

## §1. Linear parts and the flow circle (question 1)

**Setting.** After restriction to the affine span (DIM3), V is 3-dimensional and Ω has nonempty interior.

1. **Generators preserve Ω exactly.** By `preservesBody_drive` (OG:161), `flow t`, `flow t`⁻¹, `J` and `J⁻¹` all map
   Ω into Ω. Hence `g '' Ω = Ω` for each generator g; this is a two-line lemma, not landed. IIP then gives:
   - `g c = c`;
   - the linear part `A_g` satisfies `A_g S A_gᵀ = S`, equivalently `A_gᵀ S⁻¹ A_g = S⁻¹` (X1.1–X1.2).

   So every generator is a ⟨,⟩-orthogonal map about c. `J` may have determinant −1.
2. **Determinant.** `A(t) = A(t/2)²`, so `det A(t) = det(A(t/2))² > 0` (X2.1). Thus `A(ℝ) ⊆ SO(3)`. No continuity is
   used.
3. **Nontriviality comes from `J_off_axis`.** Take `s = 0`. If `flow t = id` on Ω, then for x ∈ Ω,
   `J(flow t (J⁻¹x)) = x = flow 0 x`, using `J_symm_preserves`. So the t of `J_off_axis` has `A(t) ≠ I`. Equality on
   Ω implies equality on V, because Ω has interior and both maps are affine.
4. **One axis.** Let `Q = A(t/2)`. It is not I, and it is not a half-turn, since its square is `A(t) ≠ I`. Every
   `A(s)` commutes with Q. The commutant of a non-half-turn rotation is the circle `SO(2)_a` about its axis a (X3.1).
   Half-turns about orthogonal axes commute without sharing an axis (X3.2), which is why t/2 is used. So
   `A(ℝ) ⊆ SO(2)_a`.
5. **Full circle.** This is where `flow_continuous` is used.
   - With continuity: for a unit e ⊥ a, the map `t ↦ ⟨A(t)e, e⟩` is continuous, equals 1 at 0 and is < 1 somewhere.
     By the IVT and the group property, the image contains `R_a(φ)` for `|φ| ≤ θ₁`, and powers give all of `SO(2)_a`.
     So `A` is a continuous homomorphism ℝ → `SO(2)_a` with `A(t) = R_a(ωt)`, ω ≠ 0. The last form is standard and is
     not needed below.
   - Without continuity: `A(ℝ)` is a non-trivial divisible subgroup of the circle. Finite non-trivial groups are not
     divisible, so it is infinite, hence dense. Its closure is the whole circle.
6. **N fields.** With `N_involutive`, `A(t₀)² = I` and `A(t₀) ≠ I` (by `N_moves`), so N is the half-turn about a.
   Nothing in §§1–5 uses `t₀`, `N_involutive` or `N_moves` (**NEW**). `flow_zero` is redundant by `flow_zero_of_add`
   (ON:114).

## §2. Non-parallel axes and the closure (question 2)

**`J_off_axis` ⇒ `Ba ∉ {±a}`.** Suppose `Ba = ±a`. Then `B R_a(θ) B⁻¹ = R_a(±θ)`, with sign `det(B|a⊥)`. This holds for
all four axis-preserving O(3) types: rotation, reflection in a plane through a, half-turn about an axis ⊥ a, and
rotoreflection (X4, symbolic in θ, φ). Hence `J flow(t) J⁻¹ = flow(±t)` on all of V, and `J_off_axis` fails. Only the
subgroup property of `A(ℝ) ⊆ SO(2)_a` is used, not continuity. Example: the Hamel flow with `J = cyc3` passes
`J_off_axis` (X9.1).

**Converse.** If `Ba ∉ ±a` and `A(t) ≠ I`, then `J flow(t) J⁻¹` fixes `Ba` and moves a, so it is no flow member
(X5.1–X5.4).

So under DIM3+IIP, `J_off_axis` is **exactly** "the conjugate circle has a different axis" (POSITIVE). The comparison
"on Ω" is the right reading. In X13, `V = ℝ⁴` and Ω = ball3 × {0}, with a sheared flow and `J(x,w) = (x + w·e_y, w)`.
There J is the identity on Ω, `J flow J⁻¹ = flow` on Ω, and the two differ on V. A V-level clause would accept a drive
whose group on Ω is one circle.

**Closure.** Let G be the words of `range flow ∪ {J}` (ON:53). Then
- `cl(G) ⊇ cl(A(ℝ)) = SO(2)_a`, and `cl(G) ⊇ J SO(2)_a J⁻¹ = SO(2)_{Ba}`;
- by §3, the group generated by two full circles with non-parallel axes is all of SO(3);
- so `cl(G) ⊇ SO(3)` (for ⟨,⟩, about c), with or without continuity;
- `cl(G) = SO(3)` iff `det J = 1`; otherwise `cl(G) = O(3)` (X5.5, where J is a reflection).

A connected-Lie-subgroup argument is not needed.

**Countermodel shape for "too weak".** In dimension 3 there is none (above). In dimension 4, `J_off_axis` is too weak
to give transitivity (§5).

## §3. Exact finite words (question 3) — a separate theorem

**ROT-WORDS(α).**
- *Setting.* Let a, b be unit vectors in Euclidean ℝ³ with `|⟨a,b⟩| = cos α`, α ∈ (0, π/2]. Replace b by −b if
  needed; this gives the same circle.
- *Statement.* For n ≥ 1, the following are equivalent:
  - every g ∈ SO(3) is an alternating product of n factors from `SO(2)_a` and `SO(2)_b`, for one fixed choice of
    first letter;
  - every g ∈ SO(3) is such a product for either choice of first letter;
  - `(n−1)α ≥ π`.

  So the order of generation is `N(α) = ⌈π/α⌉ + 1`.
- *Proof, written.*
  - Cap lemma: the points `W·a` reached by words `W = R_a R_b ⋯ R_a R_b` with k b-factors form exactly the closed cap
    of angular radius `min(π, 2kα)` about a.
    - "⊆" is the spherical triangle inequality: `∠(a, R_a R_b p) ≤ ∠(a,b) + ∠(b,p) ≤ 2α + ∠(a,p)`.
    - "⊇" uses the IVT along `θ ↦ R_b(θ)·cap` together with azimuthal closure under `R_a`. The step value is
      `(R_b(π)a)·a = cos 2α` (X7.3).
  - Odd n = 2k+1, of the form a…a: g is reachable iff `∠(a, g a) ≤ 2kα`. The final `R_a` is the stabilizer.
  - Even n = 2k, of the form (ab)^k: g is reachable iff `∠(a, g b) ≤ (2k−1)α`. Write `g = W R_b(θ)`; then `W a` runs
    over the circle of radius α about `g b`, whose nearest distance to a is `|∠(a,gb) − α|`.
  - Both conditions hold for every g iff `(n−1)α ≥ π`.
  - Sharpness witnesses, for every α (X7.14): the half-turn about `a×b`, which sends a, b to −a, −b (odd n), and the
    half-turn about `a−b`, which sends b to −a and a to −b (even n). Each defeats both choices of first letter.
- *Exact instances.*
  - α = π/2: a rational rotation is an exact `Rz Rx Rz` word (X7.1).
  - α = π/3: the odd witness is not a 3-factor word (X7.9) and is an exact 4-factor word `R_a R_b R_a R_b(π)`, with
    `cos θ₂ = 1/3` (X7.10–X7.11).
- *Citation.* Lowenthal, "Uniform finite generation of the rotation group", *Rocky Mountain J. Math.* 1 (1971):
  `π/(k+1) ≤ ψ < π/k` gives order k+2, and ψ = π/2 gives 3. This is identical to ⌈π/α⌉+1 (X7.L2–L6). Also
  Davenport (1973) for three axes: `R_{n₁}R_{n₂}R_{n₃}` is onto iff `n₂ ⊥ n₁, n₃`, which is the n = 3 case. A 2026
  *RMJ* paper on "the order of finite generation of SO(3)" exists and was not read.

**For the drive.**
- `SO(2)_a = A(ℝ)` requires `flow_continuous`.
- `SO(2)_{Ba} = J A(ℝ) J⁻¹`, and each factor costs the generator word `J·flow·J⁻¹`.
- So every ⟨,⟩-rotation about c lies in `words (range D.flow ∪ {D.J})`, as a word of at most `N(α) + 2⌈N(α)/2⌉ ≤ 2N(α)+1` generator letters: an a-factor is one
  flow letter, a b-factor is three letters `J·flow·J⁻¹`.
- Once Ω is a Q-ball (§4), its boundary states are its Q-sphere, and SO(3) is transitive on it. This gives K∞-R as
  OG-1 states it: `BoundaryTransitive Ω (words …)`.

**Closure-transitivity is not K∞-R** (**NEW**: the separation is exact). The **Hamel model** takes:
- flow `t ↦ rot3(φ t)`, with φ additive, `φ(1) = π` and `φ(ℝ) = ℚπ`, which needs a ℚ-basis of ℝ;
- `t₀ = 1` and `J = cyc3` on ball3.

It satisfies every field except `flow_continuous`. Then:
- **ELL-closure holds**: `ℚπ` is dense, so `cl(words) ⊇ SO(3)`;
- **ELL-ellipsoid holds**: Ω = ball3;
- **K∞-R fails**: `words` is countable (`FreeGroup.range_lift_eq_closure` and `Countable (FreeGroup α)` in
  Mathlib), and the sphere is not.

So `flow_continuous` is load-bearing for exactly KR-exact-words and for nothing upstream of it.

## §4. The ellipsoid (question 4)

**Argument.**
1. Suppose `cl(G·x) ⊇ {y : Q(y−c) = Q(x−c)}` for every x (§2), and Ω is closed with `g '' Ω = Ω` for g ∈ G.
2. Then each x ∈ Ω has its whole Q-sphere inside Ω.
3. By convexity, Ω contains the convex hull of that sphere, which is the Q-ball through x. In Mathlib this is
   `convexHull_sphere_eq_closedBall`, after normalization.
4. Let `R = max_{x∈Ω} √Q(x−c)`. The maximum exists by compactness, and R > 0 because Ω has interior. Hence
   Ω = {x : Q(x−c) ≤ R²}.
5. Taking `T(x) = R⁻¹·M⁻¹(x − c)` with `S = M Mᵀ` gives `T '' Ω = ball3`. This is exactly the hypothesis `hT` of
   `seedOrbit_eq_of_normalization` (ON:307) and `lorentz_of_normalization` (ON:340).

**What each hypothesis does.**
- *Closedness.* It lets closure-invariance replace exact invariance. Without it, take the Hamel G and
  Ω = open ball ∪ G·e_z. This set is convex, bounded and G-invariant, but not SO(3)-invariant, so it is not a Q-ball
  (written). With continuity, exact invariance makes this moot.
- *Convexity.* The shell 1 ≤ |x| ≤ 2 is drivable by the `ball3Drive` maps (X11.1) and is SO(3)-invariant, but it is
  not a ball (X11.2).
- *Boundedness/compactness.* It is needed for IIP itself. The cylinder `x²+y² ≤ 1` in ℝ³ with `J(x,y,z) = (x,y,z+x)`
  passes every drive field (X12.2, X12.4). J is unipotent, so it is orthogonal for no inner product (X12.1). The words
  are nonetheless transitive on the lateral boundary (X12.3, written). So K∞-R can hold on a non-ellipsoid once
  compactness is dropped.
- *Interior.* Needed for R > 0 and for IIP; it comes from DIM3 after restriction
  (`Convex.interior_nonempty_iff_affineSpan_eq_top`).

## §5. Countercontrols (question 5)

- **Dimension 3 is load-bearing for (2).**
  - B⁴ with `flow = R(t)⊕I₂`, `N = R(π)⊕I₂` and J the block swap passes every field; `J_off_axis` uses the point
    (0,0,1,0) (X8.2). B⁴ satisfies IIP with S ∝ I.
  - The words and J preserve `m = |x₁₂|²|x₃₄|²` (X8.3), and m is continuous. So the closure preserves it too.
  - m separates `e₁` (m = 0) from `(e₁+e₃)/√2` (m = 1/4) (X8.4). The closure `(SO(2)×SO(2))⋊ℤ₂` is not transitive on
    S³ and contains no SO(4).
  - K's `SO(3)⊕1` drive fixes `x₄` (X8.6).
  - These separate from `boundaryTransitive_ball4` (ON:735): there the *full* isometry group is transitive in
    dimension 4, but a *drive's* group need not be.
- **Dimension 3 is load-bearing for (4).** The bidisk with the same drive is not an ellipsoid: its boundary contains
  the segment {(1,0,0,s)} (X8.5).
- **Dimension 2 (B6) falls out of (1).**
  - Flow members are squares, so they lie in SO(2) (X6.3).
  - Every `B ∈ O(2)` conjugates `R(θ)` to `R(±θ)` (X6.1–X6.2), so `J flow(t) J⁻¹ = flow(±t)` and `J_off_axis` fails.
  - Hence a compact convex body of affine dimension 2 satisfying IIP has no drive.
  - In dimension 1, `O(1) = {±1}` and squares are 1 (X6.4). The flow is trivial, so `J_off_axis` fails. This
    generalizes `not_drivable_Icc` (KF:529) beyond Icc, given IIP.
  - Neither `flow_continuous` nor any NOT field is used.
  - **Scope warning.** OG-1's preregistration froze B6 out as "a dimension-exclusion step". It is a lower bound only,
    and with an UPPER3 premise it would complete DIM3. It is **not** needed by any statement below, which takes
    DIM3 as input.

## §6. Candidate theorem statements (deliverable 9a)

Every statement is conditional. None is proved. Names are proposals. Notation: `sq3 v := v 0^2 + v 1^2 + v 2^2`, the
quadratic form of `ball3` (KF:311).

**Infrastructure (premise-free; needed by all).**
```lean
-- (I1) image equality from PreservesBody (OG:69)
theorem image_eq_of_preservesBody {Ω} {G} (hG : PreservesBody Ω G) {g} (hg : g ∈ G) : g '' Ω = Ω
-- (I2) the drive without continuity and without the NOT, and the forgetful map
structure DriveCore (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω
  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x
def ElementaryDrivability.toCore (D : ElementaryDrivability Ω) : DriveCore Ω
-- (I3) restriction of a drive to an affine chart of aff Ω (ON:357 vocabulary; flow continuity via the
--      finite-dimensional range, NOT via chartRetract's Lg — see §7)
def ElementaryDrivability.restrict (hL : LinearMap.ker L = ⊥) (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ range (chart L p0))
    (D : ElementaryDrivability Ω) : ElementaryDrivability (bodyR L p0 Ω)
theorem words_restrict … -- a word of the restricted generators intertwines with the same word upstairs
```

**IIP-N.** This is the interface in normalized coordinates: a premise, derived from IIP by LDL (X1.3–X1.5). It is
stated on the restricted body `Ω ⊆ Fin 3 → ℝ` (DIM3 enters as the chart's domain `Fin 3 → ℝ` plus `hint`):
```lean
def NormalizedInvariance (Ω : Set (Fin 3 → ℝ)) : Prop :=
  ∀ g : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ), g '' Ω = Ω → g 0 = 0 ∧ ∀ v, sq3 (g v) = sq3 v
theorem normalizedInvariance_of_IIP … : ∃ T : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ), NormalizedInvariance (T '' Ω)
```

**ROT-WORDS (pure geometry, no OI content).**
```lean
-- SO(2)_u := {g | g 0 = 0 ∧ (∀ v, sq3 (g v) = sq3 v) ∧ g u = u ∧ (g.linear : _ →ₗ[ℝ] _).det = 1}
theorem rotWords {a b : Fin 3 → ℝ} (ha : sq3 a = 1) (hb : sq3 b = 1) (hab : b ≠ a ∧ b ≠ -a) :
    ∀ g, g 0 = 0 → (∀ v, sq3 (g v) = sq3 v) → (g.linear).det = 1 →
      g ∈ Subgroup.closure (SO2 a ∪ SO2 b)
-- optional, sharp: rotWords_length : … alternating product of n factors ↔ (n - 1) * α ≥ π
```

**ELL-closure** (DIM3 + IIP-N + DriveCore; no continuity):
```lean
theorem ell_closure {Ω : Set (Fin 3 → ℝ)} (hcomp : IsCompact Ω) (hconv : Convex ℝ Ω)
    (hint : (interior Ω).Nonempty) (hN : NormalizedInvariance Ω) (D : DriveCore Ω) :
    ∀ x y, sq3 y = sq3 x → y ∈ closure {z | ∃ g ∈ words (Set.range D.flow ∪ {D.J}), g x = z}
```

**ELL-ellipsoid** (same hypotheses; via ell_closure, or via KR-core when D has continuity):
```lean
theorem ell_ellipsoid … (D : DriveCore Ω) : ∃ R : ℝ, 0 < R ∧ Ω = {v | sq3 v ≤ R ^ 2}
theorem ell_normalization {V} … (hdim : Module.finrank ℝ (affineSpan ℝ Ω).direction = 3)
    (hcomp hconv) (hIIP : IIP-conclusion on the chart) (D : ElementaryDrivability Ω) :
    ∃ T : V ≃ᵃ[ℝ] (Fin 3 → ℝ), T '' Ω = ball3   -- this requires `affineSpan ℝ Ω = ⊤` in V, else T cannot be an equiv;
                                              -- for a lower-dimensional Ω in a bigger V, state it on bodyR
```
The last remark matters. `seedOrbit_eq_of_normalization` takes `T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)`, so it consumes the
*restricted* body. For Ω in ℓ^∞ the composite is `hypotheses_restrict` (ON:529), then `ell_normalization` on `bodyR`,
then `seedOrbit_eq_of_normalization`.

**KR-exact-words** (DIM3 + IIP-N + ElementaryDrivability; continuity load-bearing):
```lean
theorem kR_exact_words {Ω : Set (Fin 3 → ℝ)} (hcomp) (hconv) (hint) (hN : NormalizedInvariance Ω)
    (D : ElementaryDrivability Ω) : BoundaryTransitive Ω (words (Set.range D.flow ∪ {D.J}))
-- original coordinates, via (I3) + isBoundaryState_restrict (ON:407):
theorem kR_exact_words_of_affineDim3 {V} {Ω : Set V} (hdim …) (hcomp) (hconv) (hIIP …) (D : ElementaryDrivability Ω) :
    BoundaryTransitive Ω (words (Set.range D.flow ∪ {D.J}))
```

**Countercontrols** (each is a kernel instance, not a premise):
```lean
theorem not_kR_hamel : ∃ D : DriveCore ball3, ¬ BoundaryTransitive ball3 (words (Set.range D.flow ∪ {D.J}))
theorem ball4_swapDrive : ElementaryDrivability ball4 ∧ ¬ BoundaryTransitive ball4 (words …)   -- with IIP-N true
theorem bidisk_drive_not_ellipsoid : …
theorem dimLeTwo_no_drive (hN2 : NormalizedInvariance₂ Ω) (hint) : IsEmpty (DriveCore Ω)   -- B6; scope warning §5
```

## §7. Dependency chain and circularity audit (deliverables 9b, 9c)

```
IIP (proposed round; premise here) ──LDL──▶ IIP-N
DIM3 (input) ──▶ chart W = Fin 3 → ℝ, interior (Convex.interior_nonempty_iff_affineSpan_eq_top)
D : ElementaryDrivability Ω ──(I3 restrict)──▶ D|W ──toCore──▶ DriveCore
preservesBody_drive (OG:161, kernel) ──I1──▶ g '' Ω = Ω for generators
IIP-N + I1 ──▶ §1.1 orthogonal about 0
flow_add ──▶ §1.2 det 1 ; J_off_axis(s=0) ──▶ nontrivial ; flow_add ──▶ §1.4 one axis a
J_off_axis + §1.4 ──▶ §2 Ba ≠ ±a
  ├─ no continuity: divisible ⇒ dense circle ──┐
  └─ flow_continuous + IVT ⇒ full circle ──────┤
ROT-WORDS (pure) ◀───────────────────────────────┘
  ├─▶ ELL-closure (dense circles + continuity of multiplication) ──(closed, convex, compact, interior)──▶ ELL-ellipsoid
  └─▶ (full circles) SO(3) ⊆ words ──▶ ELL-ellipsoid ──▶ boundary = Q-sphere (sphere_of_isBoundaryState_ball3 after T)
                                    ──▶ KR-exact-words = BoundaryTransitive Ω (words …)  [OG:79, ON:53]
ELL-ellipsoid ──▶ T '' Ω = ball3 ──▶ seedOrbit_eq_of_normalization (ON:307), lorentz_of_normalization (ON:340)
```

**Hypothesis audit.** Each row gives a model where the hypothesis fails, and what then breaks.

| hypothesis | countermodel | what breaks |
| --- | --- | --- |
| DIM3 | B⁴ + `R⊕I₂` + swap (X8.1–8.4); bidisk (X8.5); B⁴ + `SO(3)⊕1` (X8.6) | ROT-WORDS has no analogue: closure ⊉ SO(4), K∞-R fails, no ellipsoid |
| dim ≤ 2 | X6 | vacuous: no drive exists |
| IIP (compactness inside it) | cylinder + shear (X12) | no invariant inner product (J unipotent), not an ellipsoid; K∞-R still holds |
| convexity | shell (X11) | the ellipsoid step (sphere ⇒ ball) |
| closedness | open ball ∪ Hamel orbit (written) | closure-invariance; ELL-ellipsoid in its no-continuity form |
| interior | — | IIP is inapplicable; DIM3 supplies interior after restriction |
| `flow_add` | — | det-1 and one-axis steps; used everywhere |
| `flow_preserves`, `J_preserves`, `J_symm_preserves` | ½·id control (Thread L O1, recorded in M) | IIP is inapplicable to the generator |
| `J_off_axis` | `J = Rz(π/2)` or `diag(1,−1,−1)` on ball3 (K 1.12–1.13; X4) | single circle; not K∞-R (`not_boundaryTransitive_flow`, OG:620) |
| `flow_continuous` | Hamel model (written; X9.1) | **only** KR-exact-words |
| `t₀`, `N_involutive`, `N_moves` | not needed | — (inert) |

**Circularity.**
- Dimension 3 is an input. It is not taken from NB-1, nor from B6. B6 is a lower bound only and is not on the chain.
- The inner product comes only from IIP (IIP-N). There is no Haar averaging and no compact group.
- The normalization in KR-exact-words uses IIP's frame, not the ellipsoid. The ellipsoid is a conclusion, used only
  afterwards to identify boundary states.
- The drive is a hypothesis D, never sourced. No route through `elementaryDrivability_of_substratum` is used.
- `flow_continuous` is not used to obtain ELL. ELL-closure is not presented as K∞-R.
- NB-1 (`nativeGateBall`) and `lorentz_of_effects` are downstream only.

## §8. Mathlib machinery (checked at tag v4.33.0 = `db584cd6`, the tag the lakefile pins)

| need | name (file:line in the clone `N/mathlib-v4.33.0`) | status |
| --- | --- | --- |
| IVT | `intermediate_value_univ` (Topology/Order/IntermediateValue.lean:175), `intermediate_value_Icc` (:559) | present |
| spherical triangle inequality (sharp count) | `InnerProductGeometry.angle_le_angle_add_angle_of_norm_eq_one` (Geometry/Euclidean/Angle/Unoriented/TriangleInequality.lean:112) | present (EuclideanSpace form) |
| interior from affine span | `Convex.interior_nonempty_iff_affineSpan_eq_top` (Analysis/Normed/Affine/AddTorsorBases.lean:144) | present |
| sphere hull = ball | `convexHull_sphere_eq_closedBall` (Analysis/Normed/Module/Convex.lean:93) | present (normed space; use EuclideanSpace or the `ball3` form via T) |
| Cholesky-type factor | `LDL.lower_conj_diag` (Analysis/Matrix/LDL.lean:115) | present |
| inner product from B | `InnerProductSpace.ofCore` (Analysis/InnerProductSpace/Defs.lean:569); `Orthonormal.exists_orthonormalBasis_extension` (Analysis/InnerProductSpace/PiL2.lean:1034) | present (alternative to LDL) |
| linear parts / det | `AffineEquiv.linearHom` (LinearAlgebra/AffineSpace/AffineEquiv.lean:354), `LinearMap.det_conj` (LinearAlgebra/Determinant.lean:306), `Matrix.det_fin_three` (…/Determinant/Basic.lean:818) | present |
| SO(n) | `Matrix.orthogonalGroup` (LinearAlgebra/UnitaryGroup.lean:295), `Matrix.specialOrthogonalGroup` (:315) | present |
| continuity in finite dim | `LinearMap.continuous_of_finiteDimensional` (Topology/Algebra/Module/FiniteDimension.lean:283), `LinearEquiv.toContinuousLinearEquiv` (:367), `AffineEquiv.continuous_of_finiteDimensional` (Analysis/Normed/Module/FiniteDimension.lean:131) | present |
| continuous complement (I3 alternative) | `Submodule.ClosedComplemented.of_finiteDimensional` (Analysis/LocallyConvex/HahnBanach.lean:122) | present |
| dense subgroups (no-continuity ELL) | `AddSubgroup.dense_or_cyclic` (Topology/Algebra/Order/Archimedean.lean:77, `to_additive`) | present (pull back from the circle to ℝ) |
| Hamel model | `Module.Basis.ofVectorSpace` (LinearAlgebra/Basis/VectorSpace.lean:152); `FreeGroup.range_lift_eq_closure` (GroupTheory/FreeGroup/Basic.lean:716); `instance Countable (FreeGroup α)` (SetTheory/Cardinal/Free.lean:57) | present |
| angles | `Real.sin_arccos` (…/Trigonometric/Inverse.lean:352), `Real.injOn_cos` (…/Trigonometric/Basic.lean:591); landed `exists_euler_angles` (ON:614) | present |
| bilinear form | `LinearMap.BilinForm`, `LinearMap.BilinForm.IsSymm` (LinearAlgebra/BilinearForm/Properties.lean:88) | present |
| classification of continuous homs ℝ → circle | not found by grep; **not needed**, because the IVT route avoids it | — |

## §9. Recommendation

Freeze only after IIP lands.
1. **Round A, ready now as a statement; it needs nothing from IIP.** It contains ROT-WORDS (qualitative) and the
   premise-free infrastructure I1, I2 and I3 (drive restriction).
   - Cost is moderate. Use the IVT and cosine-doubling route: `x ↦ 2x²−1` (X7.12–X7.13) gives a perpendicular axis,
     and the landed `euler_apply_pole` / `exists_euler_angles` (ON:589/614) close it. No spherical triangle
     inequality is needed.
   - The sharp count `rotWords_length` is optional. It is formalizable with
     `angle_le_angle_add_angle_of_norm_eq_one`, but it is a separate statement and not needed for K∞-R.
2. **Round B, ready once IIP lands.** It contains IIP → IIP-N (LDL), KR-exact-words, ELL-ellipsoid in its continuity
   form (as a corollary of `SO(3) ⊆ words`), and `ell_normalization` feeding ON:307/340.
   - Countercontrols: `ball4_swapDrive` (IIP-N holds; K∞-R fails) and `bidisk_drive_not_ellipsoid`, as DIM3 controls.
     These are exact-checked here (X8).
   - The result note must say: DIM3 is an input, the inner product is IIP's, and the drive is a hypothesis.
3. **Round C, optional and diagnostic.** It contains ELL-closure for `DriveCore` (no continuity) and `not_kR_hamel`.
   This is the formal witness that closure-transitivity ≠ K∞-R. It costs more (dense-circle argument,
   approximation) and buys only the separation.
4. **Keep B6 (`dimLeTwo_no_drive`) out of A–C unless the owner reopens dimension exclusion.** It is cheap given IIP-N
   (X6), but OG-1 froze it out as a dimension-exclusion step.

**Output classification.**
- **NEW:**
  - (i) `flow_continuous` is load-bearing exactly for KR-exact-words. ELL-closure and the ellipsoid hold without it
    (Hamel model).
  - (ii) The NOT fields are inert for the whole ellipsoid/K∞-R step, and for B6.
  - (iii) The exact order `N(α) = ⌈π/α⌉+1` is sharp, with no uniform bound over drives.
- **POSITIVE:** `J_off_axis`, as landed and compared on Ω, is exactly "non-parallel axes" in dimension 3 under IIP.
- **ELABORATING:**
  - the closure is O(3) when `det J = −1`;
  - B6 follows from IIP + `J_off_axis` in two lines;
  - the drive-restriction continuity pitfall (`Lg` may be discontinuous on infinite-dimensional V);
  - the cylinder: K∞-R without an ellipsoid, once compactness is dropped.
- No BORDERLINE items. Fixed point after four passes.
