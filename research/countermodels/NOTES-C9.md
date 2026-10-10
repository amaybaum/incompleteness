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
