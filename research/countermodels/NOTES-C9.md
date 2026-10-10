# NOTES-C9 — the single-system analogue of T: Ω₄ and the ball

Node C9 (round 2). Object: HO-7 v1 item 1, `Ω₄ = {(x, s) ∈ ℝ³ × ℝ : |x|⁴ + s⁴ ≤ 1}` (received 2026-10-10T22:08Z; only its
definition is used, every property below is recomputed here). Evidence levels as in NOTES-C1. Kernel anchors at L:
TransitiveBody.lean:602 `exists_affine_image_eq_eball` (a compact convex body with interior, boundary transitive under a
body-preserving family, is an affine image of the Euclidean ball) and DenseOrbit.lean:174
`exists_affine_image_eq_eball_of_dense` (the same under a dense boundary orbit), both read at L in this session.

## S0 — predictions written before the first run of `c9_omega4.py` (2026-10-10T22:51Z)

1. `det Hess N = 2304 s² |x|⁶` for `N = |x|⁴ + s⁴`; with the chain rule and unique factorization this forces every
   linear map preserving `N` to be `B ⊕ (±1)` with `B ∈ O(3)`: **Aut(Ω₄) = O(3) × ℤ₂** (affine automorphisms fix the
   centre of symmetry).
2. The orbits of Aut(Ω₄) on the extreme points (= the boundary, Ω₄ being strictly convex) are the level sets of `s⁴`
   on `∂Ω₄`: a one-parameter family; not transitive, no dense orbit (each orbit closed).
3. The exact analogue of the facial invariant `c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}` of a self-dual cone is, for a
   body with state cone `V₊` and effect cone `V₊*`, `c*(ω) = dim span{e ∈ V₊* : e(ω) = 0}` (for self-dual `K` the two
   coincide). Predicted: `c* = 1` at every pure state of Ω₄ and of the ball (smooth boundaries), `c* = 2` at the edge of
   the cylinder (countercontrol), `c* = 9` at a pure state of `Q3` (d = 4). So `c*` cannot see Ω₄'s non-transitivity.
4. The second-order invariant that does see part of it: the rank of the second fundamental form of `∂Ω₄`, predicted 3
   at generic points, 2 on the equator `s = 0`, 0 at the poles `x = 0`; on the ball 3 everywhere.
5. Ω₄ is not linearly isomorphic to its polar `{(y, t) : |y|^{4/3} + |t|^{4/3} ≤ 1}`, so no inner product makes its
   cone self-dual; the pair-level `c` transfers only as `c*`.

**Provenance note (added 2026-10-10T23:01Z, `date -u`).** The time in the S0 heading above is an estimate; by file
modification time this section was last written at 22:50:02 UTC, before `c9_omega4.py`'s run 1 (22:51:12; the script's
last pre-run edit at 22:50:58). The header time inside `c9_omega4.py` ("22:53Z") is likewise an estimate (LOG).

## Runs
`c9_omega4.py`: run 1 12/12, `VERDICT C9-OMEGA4-EXACT`, replay identical (out `88c5fc06…`). Pre-run edit: the wording
of CC1 in the header (no code change).

## Results

### C9.1 — Aut(Ω₄) = O(3) × ℤ₂ [W + X A1–A4, CC1]
Proof. Ω₄ is centrally symmetric about 0 and the centre of symmetry of a convex body is unique, so every affine
automorphism `A` fixes 0 and is linear; it preserves the gauge `N^{1/4}`, so `N ∘ A = N` (`N = |x|⁴ + s⁴`). For a linear
substitution, `det Hess(N ∘ A)(w) = det(A)² · det(Hess N)(Aw)` [X A2], and `det Hess N = 2304 s²|x|⁶` [X A1]. Hence
`s²|x|⁶ = det(A)² ℓ(w)² Q(w)³` with `ℓ = cᵀx + ds` (the last row of `A`) and `Q = |Bx + bs|²` (the first three rows). In
the UFD `ℝ[x, s]`, `s` and `ℓ` are irreducible (linear) and `|x|²`, `Q` are irreducible (quadratic forms of rank 3 [X A3];
a product of two linear forms has rank ≤ 2). Matching the factor of multiplicity 3 and that of multiplicity 2:
`Q ∝ |x|²` (so `b = 0`, `BᵀB = κI`) and `ℓ ∝ s` (so `c = 0`). Then `N ∘ A = κ²|x|⁴ + d⁴s⁴ = N` gives `κ = 1`, `d = ±1`,
`B ∈ O(3)`. Conversely `O(3) × ℤ₂` preserves `N` [X A4]; the shear, the scaling `s ↦ 2s` and an `x₁`–`s` rotation do not
[X CC1]. ∎
**Strict convexity** [W]: the gauge is `ℓ₄(|x|, |s|)`; equality in the triangle inequality for two boundary points
forces equal `(|x|, |s|)` (strict convexity of `ℓ₄`) and then `x₁ = x₂`, `s₁ = s₂` (strict convexity of `|·|`, equality of
signs). So the extreme points of Ω₄ are its boundary points.

### C9.2 — the single-system T fails exactly [W + X O1]
The orbits of Aut(Ω₄) on the extreme points are the level sets of `s⁴ ∈ [0, 1]` on `∂Ω₄` (O(3) is transitive on spheres
of fixed `|x|`; ℤ₂ flips `s`): a one-parameter family of closed orbits, no dense orbit. On the ball the group O(4) is
transitive. At L, the single-system T is a uniqueness theorem: boundary transitivity, or a dense boundary orbit, forces
an affine image of the Euclidean ball — CERTIFIED [K at L TransitiveBody.lean:602 `exists_affine_image_eq_eball`,
DenseOrbit.lean:174 `exists_affine_image_eq_eball_of_dense`]; with C9.1 this gives Ω₄'s exclusion directly. Its pair
analogue (T for the composite cone) is OPEN (C3.1).

### C9.3 — the exact analogue of the facial invariant `c` [W + X F1, CC2, CC3]
For a self-dual cone `K`, `c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}` is the dimension of the face of `K* = K` exposed by the
ray `x`. For a single system with state cone `V₊ = cone({1} × Ω)` and effect cone `V₊*`, the same quantity without the
self-duality identification is
`c*(ω) = dim span{e ∈ V₊* : e(ω) = 0}`,
the dimension of the face of the effect cone exposed by the pure state `ω` (for self-dual `K` the two coincide; an
automorphism `g` of `V₊` acts on effects by `g^{−T}` and preserves `c*`). Values: `c* = 1` at every pure state of Ω₄ and of
the ball (`∇N = (4|x|²x, 4s³) ≠ 0` on the boundary, so the supporting hyperplane is unique) [X F1]; `c* = 2` at the edge
of the cylinder (countercontrol: non-smooth points raise `c*`) [X CC2]; `c* = 9` at a pure state of Q3, `d = 4` [X CC3];
`c ∈ {15, 9, 10}` on K(Z_F) (NOTES-C2). **On every smooth strictly convex body `c*` is constant (= 1), so the invariant
that excludes the finite-defect exotic pair cones from T (NOTES-C3) has no single-system counterpart able to see Ω₄'s
non-transitivity.**

### C9.4 — where Ω₄'s non-transitivity is visible [X S1]
At second order: the rank of the second fundamental form (an affine invariant) is 3 at generic boundary points, 2 on
the equator `s = 0`, 0 at the poles `x = 0`; on the ball 3 everywhere. This separates three orbit types but not the
generic orbits; the complete invariant is `s⁴` itself (C9.2).

### C9.5 — Ω₄'s cone is not self-dual for any inner product [W + X P1]
The polar body is `{(y, t) : |y|^{4/3} + |t|^{4/3} ≤ 1}` (Hölder); its boundary function has `∂²/∂t² → ∞` at `(1, 0⁺)`
[X P1], so the polar's boundary is not `C²` there, while `∂Ω₄` is real-analytic with `∇N ≠ 0`. A linear isomorphism of
the cones would induce a projective map between the bases, preserving `C²` smoothness; so the state cone of Ω₄ is not
linearly isomorphic to its dual, and the pair-level premise H3 (self-duality) has no counterpart that Ω₄ satisfies.

## Assumption-watch marker (proposed to the equivalence thread: handoff-proposals/HP2)
"Every pure state has the same facial structure" (constancy of `c*`, the single-system form of the invariant used
against T at the pair level) holds on Ω₄ as on the ball; it cannot source K∞-Trans. Any proposed source of K∞-Trans
must constrain second-order data or the automorphism group itself. A premise that Ω₄ violates, such as self-duality of
the state cone (C9.5), excludes Ω₄; whether such a premise, with the other seams, implies K∞-Trans is not decided here.

## Gem classification (§A.31)
- NEW: Aut(Ω₄) = O(3) × ℤ₂ by a factorization argument (HO-7's negative half re-derived independently, sharper: the
  whole group, its orbits, and their invariant); `c*` as the exact analogue of `c`, constant on smooth bodies; Ω₄'s cone
  not self-dual for any inner product.
- POSITIVE: HO-7 item 1's non-transitivity confirmed by an independent route.
