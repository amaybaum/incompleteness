# NOTES-B16 — B7-1 for identity components of dimension at most one

Node B16 of `research/bridge` (round 4). Base L = `9f9f8257`. Evidence levels as in NOTES-B14. Reading (the
coordinator's third addendum): every statement of this node concerns orbits of pair vectors under groups of
conjugations, i.e. the invariance side (which cones a group can preserve); none is about the operational availability
of an operation.

## 0. Question

The round-4 directive: B7-1 (NOTES-B7) for groups whose identity component has dimension one, and the positive-dimension
case of `ReachUnitary` (BridgeReach, round 3: definitions and the finite case, built in run 38101591388) as a design
statement with proof. The second addendum: a RESULTS row recording that an alternative weaker than a sufficient bridge
fails names the alternative ("a group", "a finite stage", "local finiteness without (A)").

## S0. Design, productivity test and predictions (written 2026-10-11T05:31:29Z, before any run or dispatch)

**Design.** A dimension count replaces the case analysis of NOTES-B7 for small groups. A pair vector `v` is carried to a
product by some `h ∈ H` iff `v ∈ h⁻¹·P`, `P` the products. The products are covered by two C¹ charts of `ℂ³`,
`(1, x₀) ⊗ (x₁, x₂)` and `(0, 1) ⊗ (x₁, x₂)`. If countably many C¹ curves `γ_k` of matrices cover `H` (a "curve
cover"), the bad vectors lie in the ranges of countably many C¹ maps `(t, x) ↦ γ_k(t)·chart(x)` from `ℝ × ℂ³` (real
dimension 7) to `ℂ⁴` (real dimension 8). By Mathlib's `ContDiff.dimH_range_le` and `dense_compl_of_dimH_lt_finrank`
their union has dense complement, so some `v` is bad for no element; `v ≠ 0` because `0` is bad for `1 ∈ H`. The
antiunitary coset `H·(K∘conj)` contributes the maps `(t, x) ↦ conj(K*·γ_k(t)·chart(x))`, with no condition on `K`.
Module `lean/BridgeReachDim.lean`, importing `BridgeReach`.

**The link to dimension one [W + L].** A closed subgroup `H` of `U(4)` is a compact Lie group (Cartan's closed-subgroup
theorem [L]) with finitely many components (compactness). If its identity component `H₀` has dimension at most one,
`H₀ = {exp(tX)}` or `{1}`, and `H = ⋃ g_c H₀` over finitely many cosets; the curves `t ↦ g_c exp(tX)` are C^∞ and cover
`H`. This link is written, not built; the module proves the conclusion for every curve-covered subgroup and, built, for
every countable subgroup.

**Limits fixed in advance.** For an identity component of dimension `d ≥ 2` the count gives `d + 6 ≥ 8` and decides
nothing; the tori of dimension 2–4 of NOTES-B7 stay at their written proof.

**Controls.** Positive: on the controlled-phase circle `diag(1, 1, 1, e^{it})` the vector `(1, 2, 3, 5)` avoids the
products at every `t` (`prodDet = 5e^{it} − 6`, never zero), an explicit witness for a one-dimensional family.
Countercontrols: the identity of `ℂ⁴` (dimension 8) misses nothing, so the gap `7 < 8` is load-bearing; the
block-diagonal `SU(2) × SU(2) = {P₀ ⊗ U₀ + P₁ ⊗ U₁}` in the control's `Z` basis (dimension 6, B12-3's group) carries
every pair vector to a product, so the dimension hypothesis is load-bearing for the conclusion, not only for the
method.

**Productivity test (§A.31), fixed now.** B16 is a gem iff it gives more than "B7-1's small-group case, now built":
e.g. a hidden assumption of B7-1's written proof exposed by the dimension count, or a group class newly decided. The
expected outcome is ELABORATING (B7-1 moves from [W] to [D] for dimension at most one; the method's limit at dimension
two is named).

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | Every product `a ⊗ b` equals `chart0 x` (if `a₀ ≠ 0`, `x = (a₁/a₀, a₀b₀, a₀b₁)`) or `chart1 x` (if `a₀ = 0`, `x = (·, a₁b₀, a₁b₁)`) | P1 (exact, random Gaussian rationals); D2 |
| S0-2 | `finrank ℝ (ℝ × ℂ³) = 7`, `finrank ℝ ℂ⁴ = 8` | D2 |
| S0-3 | Countably many C¹ maps `ℝ × ℂ³ → ℂ⁴` miss a common vector | D2 |
| S0-4 | `avoid_of_curves`, `avoidA_of_curves`, `reachUnitary_of_curveCover`, `reachAnti_of_curveCover` (no coset condition), `reachUnitary_of_covers`, `reachAnti_of_covers`, `curveCover_of_countable`, `reachUnitary_countable` | D2 |
| S0-5 | `prodDet(diag(1,1,1,e^{it})·(1,2,3,5)) = 5e^{it} − 6`, nonzero for every `t` | P2 (symbolic, exact); D2 |
| S0-6 | For random pair vectors, an element of the block-diagonal group carries `v` to a product (exact zero of `prodDet`); and the identity map misses nothing | P3; D2 |
| S0-7 | The coset identity `K*·h⁻¹·(h·K) = 1` and the conjugation step, on random exact unitaries | P4 (exact, Cayley unitaries) |
| S0-8 | D2: `BridgeReachDim` builds; every `#print axioms` line standard; `lean-axioms` PASS | D2 job log |
| S0-9 | Defeated, as a sufficient bridge for (b): "a group" whose identity component has dimension at most one — it misses a pure state with its product orbit [D + W + L], so by claim (D) [A] it preserves an exotic cone | §3 |
| S0-10 | Gem: ELABORATING | §4 |
