# FRONTIER — owner amendment 1 (2026-10-04; read-only note; round 2 remains idle until L3B closes)

Applies to RESULT.md §1–§4 and DEPENDENCY/FRONTIER rows on TRANS, ORD∞ and the ellipsoid. The thread's files are
left as written; this note records the owner's corrections for the round that uses them.

## Checked at the base b7af4852 (OIBridge/OrbitGeneration.lean)

- `BoundaryTransitive Ω G := ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y` (line 79), with
  `G : Set (V ≃ᵃ[ℝ] V)`; the module header (line 14) states that no group structure, linearity or centrality is
  used. The ball's transitivity in the module is built from Householder reflections (lines 440, 498), each of
  order two.

## Amendments

1. **Finding 1 stands in its diagnosis, not in its ORD∞ corollary.** SELECT's octahedron check tested transitivity
   on the six vertices; the kernel predicate is transitivity on every boundary state. An affine automorphism
   preserving the body preserves extreme points, so no polytope of dimension ≥ 2 satisfies the kernel predicate:
   the old "TRANS is non-selective" argument did not test the predicate OG-1 uses. **But exact `BoundaryTransitive`
   does not imply ORD∞ as stated**: a transitive family need not contain an infinite-order element (the Householder
   reflections are a transitive family of involutions). ORD∞ is redundant only if the available reversible family
   is composition-closed and infinite order is proved in the generated words — a different statement, to be proved
   explicitly, not assumed.

   Revised conclusion: *exact TRANS is much stronger than SELECT previously tested and probably eliminates the
   polytope controls, but ORD∞ is not yet redundant; its redundancy depends on composition closure of the available
   reversible family and a proof of infinite order in the generated words.*

2. **"TRANS + IIP gives the ellipsoid/ball" is promising but not a sealed chain.** IIP-1 gives the crucial
   structure (every body automorphism fixes the centroid and preserves a positive-definite inner product on the
   finite-dimensional affine span), and exact boundary transitivity would force every boundary point to have the
   same radius in that invariant metric. Missing glue: (a) no landed general theorem identifies the corrected
   relative `IsBoundaryState` with Mathlib's topological `frontier`, while Lemma B is stated with `frontier`;
   (b) the completion lives in an infinite-dimensional carrier, so the completed body must first be transferred
   into the finite-rank completion chart and shown compact and full-dimensional there.

3. **EO's independence is research-evidenced, not certified**: the B⁴/Sp(1) countermodel is off-repo; it needs its
   own reproducible round before EO is listed as certified independent.

4. **Ranking.** Strongest frontier conclusions: the sealed negative/independence results around LIMCLOSE-C,
   composites and G, and the absence of field-neutral Naimark primitives.

## Proposed first target of architectural round 2 (predicate reconciliation + ball bridge, before EO)

1. Freeze the intended meaning of TRANS: primitive family G, generated words ⟨G⟩, or an actual subgroup.
2. Prove the completed-chart adapter: the finite-rank completed body is a compact, convex, full-dimensional
   chart body.
3. Prove the corrected-boundary bridge on that chart: `IsBoundaryState Ω x ↔ x ∈ frontier Ω`.
4. Combine exact `BoundaryTransitive` with IIP-1: all boundary states have constant invariant norm.
5. Normalize the positive-definite norm to Euclidean coordinates and invoke Lemma B: a Euclidean ball of
   unspecified dimension.
6. Separately test whether composition closure upgrades exact TRANS to ORD∞; do not assume it.

Expected shape if it succeeds: finite-rank completion + exact TRANS ⟹ ball of some dimension, with IIP supplied by
the landed geometry machinery; EO then has the narrower job of dimension/dynamics selection, V4′ stays on the
effect side (sharp seed orbit → directional family), and the composite G package stays separate:
OI → finite representation → [finite-rank completion + exact TRANS] → ball_d; then [EO / dimension selector] +
[V4′ / effects] + [composite G package] → d = 3 + quantum composite structure.

Nothing in this note alters L3B's execution.
