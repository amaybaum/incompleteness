# L2-SPEC — statement specification for `OI_L2_Bridge.lean` (b405; authored on gate-pass)

**Discipline.** No `.lean` is authored ahead of the L1 gate (`lean OI_B397_Pilot.lean`).
This document freezes the L2 file's *statements* for owner review under the two-sided
protocol: statements freeze at review; proofs stay repairable. Every concrete number below
is computed fresh by `l2_bridge_mirror_probe.py` (L2M1–L2M7, green), which becomes L2's
acceptance mirror. Mathlib names in brackets are binding *candidates*, resolved at
authoring; the mathematical statements are the review objects.

## B1 — the averaging identity and its instances

**B1.0 (the bridge).** For a finite group `G` and a finite-dimensional `ℚ`-linear
representation `ρ : G →* (V →ₗ[ℚ] V)`:
`(Fintype.card G) • (finrank ℚ (fixedSubspace ρ)) = ∑ g, trace (ρ g)`
[candidates: `Representation.averageMap`, its projection property, `LinearMap.trace`].
This is the ONE classical identity the pilot deferred; everything below instantiates it.

**B1.1 (table certificate).** The O character table over classes `[e, 8C₃, 6C₂', 6C₄, 3C₂]`
with weights `(1,8,6,6,3)` — rows A₁(1,1,1,1,1), A₂(1,1,−1,−1,1), E(2,−1,0,0,2),
T₁(3,0,−1,1,−1), T₂(3,0,1,−1,−1) — is row-orthonormal: `∑_c w_c·T[i,c]·T[j,c] = 24·δᵢⱼ`,
stated over ℤ and proved `by decide` (mirror: L2M1).

**B1.2 (V₆ structure).** With `rots` the 24-element direction action (generated in-file,
pilot pattern): multiplicities of V₆ are `(1,0,1,1,0)` — multiplicity-free with
constituents exactly {A₁,E,T₁} (mirror: L2M2).

**B1.3 (End multiplicities).** `End(V₆) ≅ A₁³ ⊕ A₂¹ ⊕ E⁴ ⊕ T₁⁵ ⊕ T₂³` (36 dims) — the
(3,4,5) split of b397, now table-derived, plus the previously-unstated A₂¹/T₂³ completion
(mirror: L2M2).

**B1.4 (Hom dims).** `finrank Hom_O(V₆, V₆) = 3`, `finrank Hom_O(V₆, End V₆) = 12`,
`finrank Hom_O(V₆, broken₂₂) = 6` — from the pilot's kernel-checked 72/288/144 via B1.0
(mirror: L2M4).

**B1.5 (broken decomposition).** `broken₂₂ ≅ E² ⊕ T₁⁴ ⊕ T₂²` with zero A₁/A₂ — stated with
the explicit isotypic projectors `P_irr = (dim/24)·∑ χ(g)·ρ_brk(g)`, each proved idempotent
with trace `(0,0,4,12,6)` (mirror: L2M3, projectors verified `P² = P`).

**B1.6 (the b402 regulator trap).** By the same B1.0 machinery on `Sym²(ℝ⁴)`:
`|H(4)| = 384` (generated in-file) with invariant dimension `1`; the native
spatial-B₃ × time-reflection group has `96` elements and invariant dimension `2`, with
fixed basis exactly `{diag(1,0,0,0), diag(0,1,1,1)}` (mirror: L2M5). *This kernel-checks
the load-bearing theorem of b401/b402.*

## B2 — ZMod censuses as corollaries

**B2.1.** For `q` odd, every `χ : Multiplicative (ZMod q) →* Gˣ`-style additive character
with `χ² = 1` is trivial — an instance of the pilot's `trivial_connection` transported to
`ZMod q` [candidates: `ZMod`, `AddChar`]; concrete corollaries for `q ∈ {3,5,7,9,11,13}`.

**B2.2 (necessity witness).** For `q = 4` the character `k = 2` is a nontrivial survivor —
the Odd hypothesis is necessary (mirror: L2M6).

## B3 — the b389 Schur sign theorem

**B3.1.** For real matrices `B : Fin m → Fin n → ℝ` and `D` positive definite:
`(-(Bᵀ ∘ D⁻¹ ∘ B))` is negative semidefinite [candidates: `Matrix.PosSemidef`,
`Matrix.PosDef.inv`, congruence `PosSemidef.mul_mul_conjTranspose`]. This is the exact
algebraic core of b389's `ΔH⁽²⁾ ⪯ 0` under a positive gap.

**B3.2 (below-channel necessity).** Existence statement: an indefinite `D` for which the
correction has a positive eigenvalue (mirror: L2M7 exhibits one; the Lean witness may be a
small explicit matrix proved `by decide`/`norm_num`).

## B4 — AddChar alignment

**B4.1.** The pilot's `Ch A G` (map_add hom) is definitionally interchangeable with the
Mathlib additive-character formulation: a two-way transport lemma so pilot theorems
(`plaquette_trivial`, `trivial_connection`) restate in Mathlib vocabulary without change of
content.

## Faithfulness map

B1.1–B1.5 ↔ b397 §counting + b398 AK2 refinement; B1.6 ↔ b401 theorem / b402 AO3;
B2 ↔ b397 census + b399-pilot T2; B3 ↔ b389 (AB-series) + b394-era necessity control;
B4 ↔ b399-pilot Part 1. Out of scope for L2: the G3 interfaces (L5), numerics.

## Review protocol

Owner review = statement sign-off (or line edits) in the gate-pass round; on sign-off,
statements freeze and `OI_L2_Bridge.lean` is authored in this directory against Mathlib,
with `l2_bridge_mirror_probe.py` as the acceptance mirror and the owner's `lake`/`lean`
run as the kernel gate.
