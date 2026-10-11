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

## 1. Outcome of S0 (written 2026-10-11T06:40Z)

**The runs.** `experiments/b16_preflight.py` (05:32:31Z): P1–P5 green, replay byte-identical. Dispatch 2 (run
38115337569): `BridgeReachDim` did not build. Its error block was printed before the readable tail of the job log (the
job-log reader returns the last 5000 of 38194 lines; no other route to the log is open from this session), so the
failure is recorded without a diagnosis; the failed text is kept as `lean/BridgeReachDim.run38115337569.lean`. For
dispatch 3 the module was rewritten defensively (LOG, 06:24:26Z): the same charts in vector form, chart membership and
smoothness proved entry by entry, the coset map through an explicit equation, the dimension bound through a `calc` in
the module's own instances, and the control through explicit rewriting; it imports `EqvK2Schema` for build order only,
so that its report falls in the readable tail. Dispatch 3 (run 38117986499, job 114406679644): built ("[3655/3659] Built
OIBridge.BridgeReachDim (3.5s)"), 32/32 `#print axioms` on `[propext, Classical.choice, Quot.sound]`; in every
`first` block the first alternative closed the goal; `lean-axioms` PASS (6083, no sorry); gate red only on
`lean-manuscript`. The chart maps are the same functions as P1's, so P1 checks the built definitions.

| id | outcome |
|---|---|
| S0-1 | confirmed [X] P1 and [D] (`kron2_eq_chart0`, `kron2_eq_chart1`, `kron2_mem_chart`) |
| S0-2 | confirmed [D] (`finrank_dom`, `finrank_pvec`) |
| S0-3 | confirmed [D] (`exists_not_mem_ranges`) |
| S0-4 | confirmed [D]: `avoid_of_curves`, `avoidA_of_curves`, `reachUnitary_of_curveCover`, `reachAnti_of_curveCover` (no coset condition), `reachUnitary_of_covers`, `reachAnti_of_covers`, `curveCover_of_countable`, `reachUnitary_countable` |
| S0-5 | confirmed [X] P2 (symbolic) and [D] (`cz_prodDet`, `cz_avoids`, `cz_entry_contDiff`) |
| S0-6 | confirmed [X] P3 and [D] (`ctl_dim_eight`) |
| S0-7 | confirmed [X] P4 |
| S0-8 | not as predicted in dispatch 2 (the module failed to build, cause not recorded); confirmed in dispatch 3 |
| S0-9 | confirmed (§3) |
| S0-10 | ELABORATING (§4) |

## 2. The statements

All of them are invariance statements: orbits of pair vectors under groups of conjugations, no operational
availability.
- **The curve-cover theorem [D].** If countably many C¹ curves of `4 × 4` matrices cover a subgroup `H` of `U(4)`,
  some nonzero pair vector is carried to a product by no element of `H`; with an antiunitary coset `H·(K∘conj)` the
  same vector also avoids the products under every coset element, for every `K`, with no coset condition. So
  `ReachUnitary` and `ReachAnti` (round 3) follow from the existence of covers for their subgroups, and every
  countable subgroup has one (by constant curves).
- **The link to dimension at most one [W + L].** A closed subgroup of `U(4)` is a compact Lie group (Cartan's
  closed-subgroup theorem [L]) with finitely many components; if its identity component has dimension at most one it
  is `{exp(tX)}` or `{1}`, and the finitely many curves `t ↦ g_c exp(tX)` cover it. With the curve-cover theorem: B7-1
  holds for every closed subgroup whose identity component has dimension at most one, CONDITIONAL on that link.
- **The method's limit.** For an identity component of dimension `d ≥ 2` the count gives `d + 6 ≥ 8` and decides
  nothing [X P5]; the tori of dimension 2–4 of NOTES-B7 stay at their written proof.
- **Controls.** On the controlled-phase circle `diag(1, 1, 1, e^{it})`, `prodDet = 5e^{it} − 6`, whose real part is at
  most `−1`, so `(1, 2, 3, 5)` avoids the products for every `t` [D]; the identity map of `ℂ⁴` is a C¹ map from real
  dimension 8 that misses nothing [D]; B12-3's block-diagonal `SU(2) × SU(2)` carries every pair vector to a product
  [X P3], so the dimension hypothesis is load-bearing for the conclusion.

## 3. Defeated alternative (the second addendum's naming)

**"a group" whose identity component has dimension at most one** is not a sufficient bridge for (b): it misses a pure
state with its orbit of products (§2, [D] for curve-covered and countable groups, [W + L] for the dimension link), so
by claim (D) [A] it preserves an exotic cone. Reading: invariance.

## 4. Gem classification (§A.31)

ELABORATING, as predicted: B7-1 moves from [W] to [D] for countable and curve-covered subgroups, and to [D] + [W + L]
for identity components of dimension at most one; no hidden assumption of B7-1's written proof was exposed, and the
method's limit at dimension two is named.

## 5. Manuscript obligations

None.
