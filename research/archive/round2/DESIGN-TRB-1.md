# Architectural round 2 — design and freeze preparation (candidate round `TRB-1`, "transitive body")

Drafting snapshot `D` = `7c821261e2537a97b85ab78ae50c6998600bc019` (L3B's landing). Read-only design phase: no branch, no
preregistration commit, no execution. Every kernel citation below was read at `D` in the worktree `scratchpad/wt-r2`
(`verification/lean-mathlib/OIBridge/*.lean`; Lean `v4.33.0`, Mathlib tag `v4.33.0`). Scope excluded by owner
direction: 3A banking, the EO countermodel round, manuscript follow-ups.

Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, SC `StageCompletion`,
CA `CompletionAction`, IIP `InvariantInnerProduct`.

***

## 0. The separation the round must preserve

```
TRANS  ⇏  ORD∞            (by definition; witnessed in the kernel by the round's control C3 below)
completion + reversible TRANS + invariant inner product  ⟹  Euclidean ball of dimension d   (T4)
ORD∞ tested independently as what excludes the finite-polytope controls              (T3 + T5 + the 2×2 of §6)
```

Finding stated up front (§5, H4): on a composition-closed boundary-transitive group of dimension ≥ 2, the existence
of an infinite-order element is a theorem of Jordan–Schur type (torsion linear groups are countable modulo an
abelian subgroup), which is not in Mathlib at the pinned tag. So ORD∞ is not merely *chosen* independent of TRANS:
at kernel level it currently *cannot* be derived from it. The round therefore carries ORD∞ as a separate predicate
and tests it; it does not try to derive it.

***

## 1. Landed inputs (the only kernel facts the theorems consume)

| id | statement (as at `D`) | where |
|---|---|---|
| L1 | `IsBoundaryState Ω x := x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε > 0, x + ε • (x - y) ∉ Ω` (relative; no topology) | KF:130 |
| L2 | `not_isBoundaryState_of_mem_interior : z ∈ interior Ω → ¬ IsBoundaryState Ω z` | KF:601 |
| L3 | `PreservesBody Ω G := ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω`; `G : Set (V ≃ᵃ[ℝ] V)` | OG:69 |
| L4 | `BoundaryTransitive Ω G := ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y` | OG:79 |
| L5 | `invariant_inner_product (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)` on `Ω : Set (Fin n → ℝ)`: `invMatrix Ω` symmetric, positive definite; every `g` with `g '' Ω = Ω` fixes `centroid Ω` and `linMatrix g` preserves `u ⬝ᵥ (invMatrix Ω *ᵥ v)` | IIP:336 |
| L6 | `eq_closedBall_of_frontier_subset_sphere (hconv) (hcomp) (h0 : 0 ∈ interior Ω) (hfr : frontier Ω ⊆ Metric.sphere 0 1) : Ω = Metric.closedBall 0 1` — **in the ambient norm of `V`** | KF:770 |
| L7 | `isBoundaryState_restrict (hL : ker L = ⊥) (hΩ : Ω ⊆ range (chart L p0)) : IsBoundaryState (bodyR L p0 Ω) w ↔ IsBoundaryState Ω (chart L p0 w)` | ON:407 |
| L8 | `isBoundaryState_tr (T : V ≃ᵃ[ℝ] W) : IsBoundaryState Ω x ↔ IsBoundaryState (T '' Ω) (T x)` | ON:229 |
| L9 | `DirectedStages`, `CSpace D = lp (fun _ : Label D => ℝ) ∞`, `body D = closure (convexHull ℝ (range prepVec))`, `norm_val_le_one`, `body_convex`, `body_isClosed`, `FiniteRank Ω := FiniteDimensional ℝ (affineSpan ℝ Ω).direction` | SC:63/128/141/130/299; CA:200/202 |
| L10 | `CompletionChart D` (`d`, `L`, `p0`, `Lg`, `hL`, `hLg`, `hspan`); `chartBody C := bodyR C.L C.p0 (body D)`; `isClosedEmbedding_chart`; `affineSpan_gen : affineSpan ℝ (range (gen C)) = ⊤`; `coordsOf_mem_chartBody`; `exists_completionChart (hne) (hfr)` | CA:144/166/189/218/184/154 |
| L11 | `OpDatum D`, `AffineRespect`, `after`, `induced_after`, `Undoes`, `inducedEquiv`, `preservesBody_inducedEquiv : PreservesBody (chartBody C) {inducedEquiv C hS hT hST hTS}` | CA:46/58/305/319/325/333/352 |
| L12 | `sharpSeed_completion (hSC : SCInf D) …`, `boundary_completion (hSC) … : IsBoundaryState (body D) (prepVec D x1)` | SC:224/232 |
| L13 | `hypotheses_restrict`, `seedOrbit_eq_of_normalization (T : V ≃ᵃ[ℝ] (Fin 3 → ℝ)) (hT : T '' Ω = ball3)`, `ball3 = {x | x 0^2 + x 1^2 + x 2^2 ≤ 1}` | ON:529/307; KF |
| L14 | controls already landed: `boundaryTransitive_fullAut3` (through Householder reflections `hh3`), `not_boundaryTransitive_flow : ¬ BoundaryTransitive ball3 (range rot3)`, `boundaryTransitive_ball4` with `finrank_E4 = 4`, `not_singletonFaces_square` on `Metric.closedBall (0 : Fin 2 → ℝ) 1`, `isEmpty_drivability_of_finite_orbits` | OG:537/620; ON:735/744; KF; ON:124 |

Not consumed, by design: `ElementaryDrivability` (KF:264), any flow, `SharpSeed`, `SeedOrbitAvailable`, `SCInf`,
`BinaryVisible`, any `Fin 3` or `ball3` fact (except in the d = 3 corollary and the controls), anything from L3B.

***

## 2. New definitions (module `OIBridge/TransitiveBody.lean`; all over `V` a real normed space, or `Fin d → ℝ`)

```lean
/-- **TRANS, the group clause**: `G` is a group of affine automorphisms of `V` under composition
(`trans`), inversion (`symm`) and the identity, each member and its inverse mapping `Ω` into `Ω`. -/
structure IsBodyGroup (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop where
  one_mem   : AffineEquiv.refl ℝ V ∈ G
  mul_mem   : ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G
  inv_mem   : ∀ g ∈ G, g.symm ∈ G
  preserves : ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω

theorem IsBodyGroup.preservesBody (h : IsBodyGroup Ω G) : PreservesBody Ω G     -- from inv_mem + preserves

/-- **TRANS**: a body group acting transitively on *every* boundary state of `Ω` (L4), not on a
distinguished finite subset. -/
def Trans (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G

/-- Infinite order on the body: some member moves some state under every positive power. -/
def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (g^[m]) x ≠ x
/-- **ORD∞**: `G` has a member of infinite order on `Ω`. Stated separately from `Trans`; never folded in. -/
def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈ G, InfiniteOrderOn Ω g

/-- The coordinate Euclidean ball of dimension `d` (the `d`-dimensional form of KF's `ball3`). -/
def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}
/-- The `Q`-ball of the invariant form about the centroid, radius `R`. -/
def qBall (Ω : Set (Fin d → ℝ)) (R : ℝ) : Set (Fin d → ℝ) :=
  {x | (x - centroid Ω) ⬝ᵥ (invMatrix Ω *ᵥ (x - centroid Ω)) ≤ R ^ 2}
```

Continuity. In the chart `Fin C.d → ℝ` every affine equivalence is continuous (finite dimension), so the
"continuity requirement" of TRANS is discharged definitionally for a finite-rank body; it is *not* an extra field.
For a body of infinite rank it would have to be imposed, and the round does not treat that case (FiniteRank is the
standing open premise, §5 H6). No topology on `G` itself is assumed anywhere; closure of `G` in `Aut Ω` is exactly
the ORD∞/drive territory the round keeps out.

***

## 3. Typed theorem skeleton

Each entry: statement (signature up to `:=`), proof route from §1 inputs and Mathlib, what it needs, what it does not.

### T1 — completed-chart adapter (compact, convex, interior, with no `[FiniteDimensional ℝ (CSpace D)]`)

```lean
theorem chartBody_isCompact (C : CompletionChart D) : IsCompact (chartBody C)
theorem chartBody_convex   (C : CompletionChart D) : Convex ℝ (chartBody C)
theorem chartBody_interior_nonempty (C : CompletionChart D) : (interior (chartBody C)).Nonempty
```
Route. Convex: `body_convex` and `Convex.affine_preimage (chart C.L C.p0)`. Closed: `body_isClosed`, chart continuous
(`LinearMap.continuous_of_finiteDimensional` for `C.L`; `chart = L + const`). Bounded: `body D ⊆ closedBall 0 1` in
`CSpace D` (from `norm_val_le_one` through `prepVec`, closed convex hull of a bounded set); `C.L` injective from a
finite-dimensional space is bounded below (`LinearEquiv.ofInjective` + continuity of its inverse in finite dimension,
or `AntilipschitzWith` from `LinearMap.exists_antilipschitzWith` of the injective map on a finite-dimensional
domain); so `chartBody C` is bounded; compact by `Metric.isCompact_of_isClosed_isBounded`. Interior: `range (gen C) ⊆
chartBody C` (`coordsOf_mem_chartBody`), `affineSpan_gen` gives `affineSpan ℝ (chartBody C) = ⊤`, then
`Convex.interior_nonempty_iff_affineSpan_eq_top`. **Needs** only L9–L10 and Mathlib finite-dimensional facts.
**Does not need** SC∞, `BinaryVisible`, any operation datum. This is FRONTIER F3 / DRIVE Γ0; it is the one missing
piece between CMP-1/OPACT-1 and IIP-1, and it imports no field or matrix structure: the chart is ℝ-affine data of
CMP-1, and `invMatrix` is *derived* from the body (IIP-1), never assumed.

### T2 — boundary-state bridge, one direction per theorem (§A.34)

```lean
/-- (→) A boundary state is not interior (landed L2) and lies in `Ω`: it is in the frontier. -/
theorem frontier_of_isBoundaryState {Ω : Set V} (hcl : IsClosed Ω) {x : V}
    (hx : IsBoundaryState Ω x) : x ∈ frontier Ω
/-- (←) In a convex set with an interior point, a point of `Ω` outside the interior is a boundary state. -/
theorem isBoundaryState_of_frontier {Ω : Set V} (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {x : V}
    (hxΩ : x ∈ Ω) (hx : x ∉ interior Ω) : IsBoundaryState Ω x
```
Route (→): `frontier = closure \ interior`, `hcl.closure_eq`, L2. Route (←): take `y ∈ interior Ω`; if
`x + ε • (x - y) ∈ Ω` for some `ε > 0`, then `x` lies on the open segment from the interior point `y` to a point of
`Ω`, hence `x ∈ interior Ω` (`Convex.openSegment_interior_closure_subset_interior` or
`Convex.add_smul_mem_interior`-family), contradiction; so the witness `y` works for every `ε`. The two directions are
kept as two theorems; a combined `↔` is admitted only as a corollary citing both names (§A.34).

The stage side of the bridge is already landed and is cited, not reproved: `boundary_completion` (SC:232) makes the
certain state of a stage effect with values 1 and 0 a boundary state of `body D` (conditional on SC∞), and L7 carries
boundary states exactly between `body D` and `chartBody C`. What the round adds is the *topological* reading in the
chart; on the ℓ^∞ body only the relative notion L1 is ever used.

### T3 — boundary purity and polytope exclusion (TRANS without the inner product)

```lean
theorem extremePoints_image {Ω : Set V} {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) :
    g '' extremePoints ℝ Ω = extremePoints ℝ Ω
theorem isBoundaryState_of_extreme [FiniteDimensional ℝ V] {Ω : Set V} (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) {x : V} (hx : x ∈ extremePoints ℝ Ω) : IsBoundaryState Ω x
theorem extreme_of_isBoundaryState_of_transitive [FiniteDimensional ℝ V] {Ω : Set V} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G)
    {x : V} (hx : IsBoundaryState Ω x) : x ∈ extremePoints ℝ Ω
/-- Polytope exclusion: a body with a boundary state that is not extreme is not boundary transitive for any
body-preserving `G`. -/
theorem not_boundaryTransitive_of_nonextreme_boundary [FiniteDimensional ℝ V] {Ω : Set V} (hc) (hconv) (hi)
    {x : V} (hx : IsBoundaryState Ω x) (hne : x ∉ extremePoints ℝ Ω) (G) (hG : PreservesBody Ω G) :
    ¬ BoundaryTransitive Ω G
```
Route. `IsCompact.extremePoints_nonempty` gives an extreme `x₀`; extreme points are not interior in finite dimension
(an interior point is the midpoint of a segment in `Ω`), so `x₀` is a boundary state by T2(←); any boundary `x` is
`g x₀`, and `extremePoints_image` keeps it extreme. **Needs** T2 and Mathlib's `extremePoints`. **Does not need**
IIP-1. This is the lemma that makes the Level-3A octahedron and every finite-stage polytope (OI-STAGE NG1) fail
TRANS *as a theorem*, so those counterexamples stay usable as controls (§6, C1).

### T4 — exact transitivity ⟹ Euclidean ball of dimension `d` (the round's principal statement)

```lean
/-- Every boundary state lies on one `Q`-sphere about the centroid. -/
theorem boundary_qnorm_const {d} {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    {G} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) :
    ∃ R : ℝ, ∀ x, IsBoundaryState Ω x →
      (x - centroid Ω) ⬝ᵥ (invMatrix Ω *ᵥ (x - centroid Ω)) = R ^ 2
/-- The body is the closed `Q`-ball about its centroid. -/
theorem eq_qBall_of_boundaryTransitive {d} {Ω : Set (Fin d → ℝ)} (hc) (hconv : Convex ℝ Ω) (hi)
    {G} (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R, 0 < R ∧ Ω = qBall Ω R
/-- Normalization: an affine change of coordinates carries the body onto the coordinate Euclidean ball. -/
theorem exists_affine_image_eq_eball {d} {Ω : Set (Fin d → ℝ)} (hc) (hconv) (hi) {G} (hG) (hT) :
    ∃ T : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), T '' Ω = eball d
/-- Completed-body form: with T1, for the chart body and an OPACT-1 group. -/
theorem chartBody_eq_eball (C : CompletionChart D) {G} (hG : PreservesBody (chartBody C) G)
    (hT : BoundaryTransitive (chartBody C) G) :
    ∃ T : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ), T '' chartBody C = eball C.d
/-- d = 3 corollary, in the form ON/OG consume. -/
theorem chartBody_eq_ball3 (C : CompletionChart D) (h3 : C.d = 3) … : ∃ T, T '' chartBody C = ball3
```
Route. `boundary_qnorm_const`: fix a boundary `x₀` (exists by T2(←): a compact proper subset of `Fin d → ℝ`, `d ≥ 1`,
has a non-interior point; the case `d = 0` is `Ω = univ = eball 0`, handled separately); for boundary `y`, `y = g x₀`
with `g ∈ G`; by L5 with `g '' Ω = Ω` (from `PreservesBody`, adapter A2 of §5), `g c = c` and `linMatrix g` preserves
the form, and `g y' - c = linMatrix g *ᵥ (y' - c)` for an affine map fixing `c`; so `Q(y - c) = Q(x₀ - c) =: R²`.
`eq_qBall` (as built in the design runs): Lemma B is **not** used. With `c ∈ interior Ω` (T3′, below) and every
boundary state on the sphere `Q(· − c) = R²`: for `x ∈ Ω`, `x ≠ c`, the ray from `c` through `x` meets the boundary
at a state `y = c + t (x − c)`, `t ≥ 1` (`exists_boundary_ray`, the segment up to `y` inside), so
`Q(x − c) = Q(y − c)/t² ≤ R²`; conversely for `Q(x − c) ≤ R²`, `x ∉ Ω` would put the ray's boundary state strictly
between `c` and `x` with `Q(y − c) = R² < Q(x − c)`, contradicting the sphere. This needs no norm change on
`Fin d → ℝ`. **T3′ (centroid interior):** `c ∈ Ω` by Hahn–Banach against the uniform measure; `c ∈ interior Ω` under
transitivity because two distinct boundary states exist and all lie on one `Q`-sphere about `c`, so `c` is not a
boundary state. The normalization adapter then reads `invMatrix Ω = Bᵀ * B` from the LDL decomposition
(`Matrix.LDL.lower_conj_diag` at `v4.33.0`; `PosSemidef.sqrt` and `posSemidef_iff_eq_conjTranspose_mul_self` are
absent there), `T := toLin' B` injective by positivity, and `exists_affine_image_eq_eball` composes the translation
by `-c`, `T` and the scaling by `R⁻¹`. **Needs** T1 (for the completed-body form), T2, L5, the normalization adapter.
**Does not need** `IsBodyGroup` (composition closure), `OrdInf`, any flow, EO, DIM3, `SharpSeed`, V4′. **Conclusion
is dimension `d`**, never 3; the `ball3` corollary is a separate, explicitly `d = 3` statement.

### T5 — the composition-closure test (ORD∞ kept separate)

```lean
/-- (a) Separation witness: the Householder reflections of the ball are body-preserving, boundary transitive,
and every member is an involution — TRANS as a *set* property carries no infinite order. -/
def refls3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := {g | ∃ d k hk, g = hh3 d k hk} ∪ {AffineEquiv.refl ℝ _}
theorem preservesBody_refls3 : PreservesBody ball3 refls3
theorem boundaryTransitive_refls3 : BoundaryTransitive ball3 refls3           -- the proof of OG:537 already uses only hh3
theorem refls3_involutive : ∀ g ∈ refls3, ∀ x, g (g x) = x
theorem not_ordInf_refls3 : ¬ OrdInf ball3 refls3
/-- (b) An infinite-order reversible datum survives the completed composition law: its powers are operation
data, each `AffineRespect`, and remain pairwise distinct on the chart body. -/
theorem ordInf_of_inducedEquiv (C) {S T : OpDatum D} (hS) (hT) (hST) (hTS)
    (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :
    ∀ m, 1 ≤ m → AffineRespect (iterAfter C T hT m) ∧ ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x
/-- (c) Stage-preserving data have finite order on a finite-rank body (DRIVE F-D3): the composition law
kills infinite order unless the datum crosses stages. -/
def StagePreserving (T : OpDatum D) : Prop := ∀ i (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩
theorem finite_order_of_stagePreserving (C) {S T : OpDatum D} (hS) (hT) (hST) (hTS) (hsp : StagePreserving T) :
    ∃ N, 1 ≤ N ∧ ∀ w ∈ chartBody C, ((inducedEquiv C hS hT hST hTS)^[N]) w = w
```
Route. (a) is the extraction of the reflection step from `boundaryTransitive_fullAut3`'s proof plus
`hhFun_hhFun`. (b) is `induced_after` iterated. (c): finitely many stage preparations affinely span the chart
(`affineSpan_gen` + finite-dimensional extraction of an affine basis); each orbit under `T` stays in a finite stage
set, so some power fixes a spanning set, and `induced_unique` gives the identity. **Needs** L10–L11. **Does not
need** anything of T1–T4.

**T5(d), deliberately not in the round's frozen surface (see §5 H4):** `Trans Ω G → 2 ≤ d → OrdInf Ω G` for a
composition-closed `G`. Its proof needs Jordan–Schur or the closed-subgroup theorem. It is listed here as the
preregistered *open question* the round reports on, not as a theorem the round claims; an elementary proof exists
for `d = 2` (an uncountable subgroup of `O(2)` has uncountable intersection with `SO(2) ≅ ℝ/ℤ`, whose torsion is
countable) and may be included as `ordInf_of_trans_dim2` if the design run finds the Mathlib support cheap.

### T6 — the 2 × 2 of controls as kernel theorems (§6, C2–C5)

```lean
theorem infiniteOrderOn_rot3_one : InfiniteOrderOn ball3 (rot3 1)          -- π irrational: rot3 m = id ↔ m ∈ 2πℤ
theorem ordInf_fullAut3 : OrdInf ball3 fullAut3                            -- from the line above
theorem trans_fullAut3 : Trans ball3 fullAut3                              -- IsBodyGroup: all automorphisms form a group
theorem not_trans_flow : ¬ Trans ball3 (Set.range rot3)                    -- L14, not_boundaryTransitive_flow
theorem ordInf_flow : OrdInf ball3 (Set.range rot3)
theorem not_boundaryTransitive_square (G) (hG : PreservesBody square2 G) : ¬ BoundaryTransitive square2 G
    -- square2 := Metric.closedBall (0 : Fin 2 → ℝ) 1 (the kernel's square, KF); edge midpoint ![1, 0] is boundary, not extreme
theorem not_ordInf_square_symmetries : ¬ OrdInf square2 (dihedral symmetries)   -- optional; NG1 shape
```

***

## 4. Dependency map (new nodes in bold; every edge is one theorem above or one landed identifier)

```
L9 body D (ℓ^∞)  ──L10 chart──▶  chartBody C ⊆ Fin d → ℝ
                                   │ T1 (compact ∧ convex ∧ interior)            [needs: L9, L10, Mathlib fin-dim]
                                   ▼
L11 OPACT-1 data ──▶ G ⊆ Aut(chartBody C)  (PreservesBody, L11)
                                   │
   TRANS = IsBodyGroup ∧ BoundaryTransitive (L3, L4)      ORD∞ = OrdInf   (separate node; no edge from TRANS, §5 H4)
                                   │                                 │
          T2 (frontier bridge) ◀───┤                                 ├── T5(c): stage-preserving ⇒ finite order
          T3 (boundary purity, polytope exclusion) ◀──┤              ├── T5(b): infinite order survives `after`
                                   │                                 └── T5(a)/T6: the 2×2 controls
   L5 IIP-1 (centroid, invMatrix) ─┤
                                   ▼
          T4a boundary states on one Q-sphere  ──▶  T4b Ω = qBall  ──L6 Lemma B via normalization (H1)──▶  T4c T '' Ω = eball d
                                                                                                             │ d = 3 only
                                                                                                             ▼
                                                                      L13 seedOrbit_eq_of_normalization (OG-1 / NB-1 tail)
```
No node of the round depends on: EO, DIM3, `ElementaryDrivability`, SC∞ (except as the hypothesis of the already-landed
L12 which is cited, not used), `BinaryVisible`, V4′, L3B. `FiniteRank (body D)` enters only through the existence of
`C : CompletionChart D` (L10) and remains an open premise (§5 H6).

***

## 5. Hidden-dependence findings from the type check (what drafting exposed)

- **H1 — Lemma B is stated in the ambient norm, and `Fin d → ℝ` carries the sup norm.** Applying L6 on `Fin d → ℝ`
  as it stands would prove the body is a *cube*. **Resolved in the design runs** by not invoking Lemma B: QB is
  proved by the ray argument in the invariant form directly (T4 above), and the normalization adapter enters only
  afterwards, to pass from the `Q`-ball to `eball d`. The frozen conclusions `Ω = qBall Ω R` and `A '' Ω = eball d`
  are route-independent and unchanged.
- **H9 — Mathlib `v4.33.0` has no matrix square root in the imported files.** `Matrix.PosSemidef.sqrt`,
  `Matrix.PosDef.det_pos` and `Matrix.posSemidef_iff_eq_conjTranspose_mul_self` are absent; the LDL decomposition
  (`Mathlib.Analysis.Matrix.LDL`, `L * diagonal D * Lᴴ = S` with `D` positive) gives the factor
  `B = diagonal (√D) * Lᴴ`. The adapter's matrix row is therefore frozen as `∃ B, Bᵀ * B = invMatrix Ω`, which is
  exactly what NRM consumes; the symmetric-square-root form was never read downstream. `Set.extremePoints` at this
  version is `{x ∈ A | ∀ ⦃x₁⦄, x₁ ∈ A → ∀ ⦃x₂⦄, x₂ ∈ A → x ∈ openSegment 𝕜 x₁ x₂ → x₁ = x}` (one equation, not two).
- **H2 — `PreservesBody` versus `g '' Ω = Ω`.** IIP-1 quantifies over `g '' Ω = Ω`, OG-1 over `PreservesBody`; the
  two are equivalent, two lines (`image_bodyR_eq` is the chart instance). Adapter A2, cheap; recorded so that the
  frozen statements use `PreservesBody` uniformly.
- **H3 — composition closure is not used by the ball theorem.** T4 consumes only `PreservesBody` and
  `BoundaryTransitive` (each `g` separately, via IIP-1). `IsBodyGroup` is needed nowhere in T1–T4 and only becomes
  load-bearing in the ORD∞ question T5(d). Consequence: TRANS as frozen (group + transitivity) is *stronger than
  the ball theorem needs*; the round states T4 in the weaker form and derives the `Trans` form as a corollary, so
  the record shows exactly which clause does what.
- **H4 — ORD∞ from a transitive group needs Jordan–Schur.** For a composition-closed `G` transitive on the
  boundary of a body of dimension ≥ 2, "G has an infinite-order element" is true but its proof passes through the
  countability of torsion linear groups modulo an abelian subgroup (or Cartan's closed-subgroup theorem), neither
  in Mathlib `v4.33.0` to my knowledge. So keeping ORD∞ independent is forced at kernel level, not a stylistic
  choice; the set-level separation (T5a) is the kernel-cheap half and is the one the round proves.
- **H5 — the frontier bridge is finite-dimensional.** T2(←) uses an interior point, which the ℓ^∞ body never has
  (its interior in `CSpace D` is empty whenever `d < ∞`); the bridge is proved in the chart and transported by L7.
  Nothing is assumed about `body D`'s frontier in `CSpace D`.
- **H6 — FiniteRank stays open (FRONTIER F2).** Every theorem takes `C : CompletionChart D` as data; the round does
  not source `FiniteRank (body D)` and says so. For finite substrata the body is a polytope (OI-STAGE NG1), where T3
  shows TRANS fails: the round's theorems are vacuous there by design, which is the correct reading.
- **H7 — continuity.** Discharged definitionally in the chart (finite dimension); no topology on `G` is assumed;
  `Trans` carries no continuity field. Recorded so that no later reading mistakes `Trans` for a Lie-group premise.
- **H8 — `extremePoints` under affine equivalences.** Mathlib has the linear-equivalence image lemma; the affine
  form is a two-line proof from the definition. Not a dependency risk.

***

## 6. Controls

### The separation table (each cell a kernel theorem, T5/T6)

| witness on `ball3` | TRANS | ORD∞ | theorem(s) |
|---|---|---|---|
| all automorphisms `fullAut3` | holds | holds | `trans_fullAut3`, `ordInf_fullAut3` (via `infiniteOrderOn_rot3_one`) |
| Householder set `refls3` | **BoundaryTransitive holds, not a group** | fails (all involutions) | `boundaryTransitive_refls3`, `not_ordInf_refls3` — TRANS ⇏ ORD∞ as a set property |
| rotation flow `range rot3` | fails | holds | `not_trans_flow` (L14), `ordInf_flow` — ORD∞ ⇏ TRANS (landed half) |
| the square (finite-stage polytope shape) | fails for every body-preserving `G` | fails for its finite symmetry group | `not_boundaryTransitive_square` (T3), optional `not_ordInf_square_symmetries` |

C1 (polytope exclusion) is what keeps the Level-3A octahedron and NG1 useful: they fail TRANS *by theorem* (T3), so
the earlier SELECT reading "transitivity does not select" is refuted at the kernel predicate, as FRONTIER §6.1
anticipated, without any appeal to ORD∞.

### Semantic guards for `controls.py` (IIP-1 style; each with a mutation control)

- **S1 dimension.** No principal theorem (T1–T4, T5) has `3`, `ball3`, `Fin 3` or `finrank … = 3` in its conclusion;
  `chartBody_eq_ball3` is the only `ball3` statement and carries the hypothesis `C.d = 3`. Mutation: a `3` in T4's
  conclusion.
- **S2 separation.** `Trans` is defined as `IsBodyGroup ∧ BoundaryTransitive` and mentions no order, flow,
  `ElementaryDrivability` or `OrdInf`; `OrdInf` mentions no `BoundaryTransitive`; no theorem has `Trans` or
  `BoundaryTransitive` among its hypotheses and `OrdInf` in its conclusion (T5(d) absent). Mutation: a theorem
  `Trans → OrdInf`.
- **S3 ball hypotheses.** `eq_qBall_of_boundaryTransitive` and `exists_affine_image_eq_eball` have exactly the
  hypotheses compact, convex, interior, `PreservesBody`, `BoundaryTransitive`; none of `OrdInf`, `IsBodyGroup`, a
  flow, `SharpSeed`, `SeedOrbitAvailable`, EO-vocabulary. Mutation: `OrdInf` added as a hypothesis.
- **S4 directional bridge.** `frontier_of_isBoundaryState` and `isBoundaryState_of_frontier` are two theorems; any
  `↔` cites both. Mutation: one direction removed.
- **S5 all-boundary transitivity.** `Trans` unfolds to `BoundaryTransitive` (quantifying over `IsBoundaryState`),
  never to a statement about `extremePoints` or a finite set. Mutation: `BoundaryTransitive` replaced by
  transitivity on `extremePoints`.
- **S6 controls present.** The four table cells are kernel theorems with `#print axioms` lines. Mutation: a cell
  removed.
- **S7 no L3B.** No identifier or header text names L3B, a rule, a rank, edge-permutivity or a hidden law.
- **N1–N3** as IIP-1: declaration list and kinds, binder contexts, no `sorryAx`; axiom prints within
  `[propext, Classical.choice, Quot.sound]`.

***

## 7. L3B as selector evidence only

L3B-READ (rank behaviour under I₃ tracks edge-permutivity; the hidden-law block) is cited in the preregistration's
§0 only to say which operation families of the OI towers are worth packaging as `OpDatum` sources in a later round;
no premise, hypothesis, control or theorem of this round refers to it, and `controls.py` S7 enforces that. Its
tallies are not promoted into any statement.

***

## 8. Proposed freeze boundary

- **Frozen at `F`:** this preregistration; `controls.py` embedding the statement surface of
  `OIBridge/TransitiveBody.lean` (every definition whole, every theorem signature up to `:=`, in order), the
  `OIBridge.lean` import insertion (after `import OIBridge.CompletionAction`), the census family for
  `lean-manuscript-census.json`, and the outcome vocabulary. T5(d) is **not** in the frozen surface; the result note
  reports its status as an open question with the gap named (H4). The `d = 2` instance is admitted to the surface
  only if the design run proves it.
- **Execution (proofs only; the design-run rule of IIP-1 applies):** C1 `controls.py`; S1 the module, the import,
  the census family; proof-only repairs; S2 the result note (candidate `E`).
- **Design runs before `F`, on a disposable branch, read for Mathlib-name verification only:** the normalization
  adapter (H1, both routes), `Convex.interior_nonempty_iff_affineSpan_eq_top`, `IsCompact.extremePoints_nonempty`,
  the affine `extremePoints` image lemma, `LinearMap.continuous_of_finiteDimensional`, bounded-below of an injective
  linear map from a finite-dimensional space, `irrational_pi` for `infiniteOrderOn_rot3_one`. The predicted execution
  tree is dispatched exactly as IIP-1 did and recorded in the preregistration.
- **Outcomes:** `TRB-1-BALL-PROVED` (every frozen theorem built, controls OK, exact-head green);
  `TRB-1-HALTED` (anything else; the result note names the failing check). Neither outcome claims DIM3, EO, a drive,
  ORD∞ from TRANS, or anything about OI sourcing of `FiniteRank`, SC∞ or operation data.
- **Governed paths:** record directory `verification/programmes/oi-qm/reconstruction/round-trb-1-transitive-body/`,
  receipt `verification/receipts/TRB-1.json`; execution `A verification/lean-mathlib/OIBridge/TransitiveBody.lean`,
  `M verification/lean-mathlib/OIBridge.lean`, `M verification/lean-manuscript-census.json`. No manuscript.

***

## 9. Decisions for the owner before drafting the preregistration

1. **T5(d) placement.** Report it as the preregistered open question (recommended), or split it into a follow-up
   round with its own design study of an elementary route (the `d = 2` proof is elementary; general `d` is not).
2. **Form of T4's conclusion.** Coordinate ball `eball d` in `Fin d → ℝ` (recommended; matches `ball3`'s shape and
   ON/OG's consumers at `d = 3`) versus `Metric.closedBall` in `EuclideanSpace ℝ (Fin d)`.
3. **Whether the round also lands the `Trans` corollaries** (the `IsBodyGroup` form of T3/T4) alongside the weaker
   `PreservesBody` forms, so that the frozen TRANS is visibly stronger than what the ball needs (H3), or only the
   weaker forms with `Trans` defined but unused by theorems.
4. **The square as the polytope control** (kernel-cheap, already a KF object) versus adding the octahedron in
   `Fin 3 → ℝ` as a second control for continuity with Level 3A.
