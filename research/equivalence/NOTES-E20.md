# NOTES-E20 — E16's residual: odd chart dimension at least five with K∞-Geom

Base L = `9f9f8257`. Node E20 of round 5 (priority 2). The residual R-E16.5: with K∞-Geom added (`SingletonFaces`,
KInfFoundations.lean:139, or `RelStrictConvex`, :144), does a drivable, non-ellipsoidal token body of odd chart
dimension `d ≥ 5` carry a native gate (`IsNot`, CompositeDimension.lean:210; `NativeGate`, :218: frame, `posFwd`,
`posInv`, `relT`, `relC`)? The gate's control relation gives `(d + 1) tr H = (tr H)²` (R-E16.1; necessary, not
sufficient — HO-28's precision); `Ω_h` (`d = 7`) meets every pair-level clause in the kernel's form and fails K∞-Geom
(R-E16.3). Inventory ids are the stage-6 inventory's (`pt/I3/INVENTORY.md`, sha256 `51eff9af…`).

## S0 (written 2026-10-11T08:27Z, before the probe's first run)

**What E20 is (§A.31).** Gem-finding on the residual: the hidden assumption under test is "the next candidate bodies
behave like `Ω_h`". **Productivity test (fixed now).** A finding counts iff (a) a body with `d` odd `≥ 5` is shown
exactly to meet every pair-level clause and K∞-Geom (the residual is real and named); or (b) an exact obstruction
excludes a named strictly convex candidate (an exact certificate that no gate exists for it, in a stated class of
`(z, N)`); or (c) the candidate families named by the instruction are each placed exactly on one side (count,
K∞-Geom, the gate clauses) with the residual narrowed to a stated class. A restatement that the residual is open, with
no candidate decided, is a non-gem.

**The candidates (fixed now), each with its natural `(z, N)` in the chart basis.**
- *The sector family* `Ω(k; d₁, …, d_k)`: `k` superselection sectors, sector `i` a Euclidean ball of chart dimension
  `d_i` (`d_i = 3` a qubit, `d_i = 1` a classical bit, `d_i = 5` an `eball 5`), chart dimension `D = (k − 1) + Σ d_i`
  (the weights `t_1, …, t_{k−1}`, `t_0 = 1 − Σ t_i`, and the unnormalised Bloch parts `r̃_i = t_i r_i`). The NOT is
  the direct sum of the sectors' NOTs (`nflip`-type with `m_i` minus signs on sector `i`, the weights fixed); the
  count (R-E16.1) requires `H` to have `(D + 1)/2` eigenvalues `+1`: `1 + (k − 1) + Σ (d_i − m_i) = (k + Σ d_i)/2`.
  Members probed: `(2; 3, 3)` = `Ω_h` (`D = 7`), `(3; 3, 3, 3)` (`D = 11`), `(4; 3, 3, 3, 3)` (`D = 15`), `(2; 3, 1)`
  (`D = 5`), `(2; 3, 5)` (`D = 9`), `(2; 5, 5)` (`D = 11`), `(2; 1, 1)` (`D = 3`, two bits — a control: the count
  with `m = (1, 1)` holds, `D = 3`).
- *The strictly convex family in chart dimension five*: `Ω⋆⁵ = {(X, S) ∈ ℝ⁴ × ℝ : ‖X‖³ ≤ (1 + S)(1 − S)²}` (the power
  cone of E18 one dimension up; chart `(X₁, X₂, X₃, X₄, S)`, `N = diag(1, −1, −1, −1, 1)`, `z = e₂`, a boundary state
  at `S = 0`); `eball 5` (`N = diag(1, 1, −1, −1, −1)`, `z = e₃`): the kernel excludes its gate (`dim_of_nativeGate`,
  CompositeDimension.lean:2723, hence `ne_five_of_nativeGate` :2736) — the **negative control** of the method;
  `eball 3` (`N = nflip`, `z = z3`): `cnot` is a gate (`nativeGate_cnot`, :1160) — the **positive control**. `Ω_cs`
  and `Ω⋆` of round 3 have chart dimension 4 and are excluded by the count (R-E16.1); the odd-dimensional revolution
  body of `Ω_cs`'s meridian is not probed (its exact points need the conic arcs; recorded as not probed).

**The exact checks (fixed now).**
- *(C1) The count* for every candidate with its natural `N`: `tr H`, the number of `+1` eigenvalues against
  `(D + 1)/2`. For the sector family the count is the arithmetic condition above (the sector NOTs fix `m_i`:
  `m = 2` for a 3-ball with `nflip`, `m = 1` for a bit with `−1`, `m = 3` for an `eball 5` with
  `diag(1, 1, −1, −1, −1)`); a member failing it carries no native gate with that `N` (R-E16.1).
- *(C2) K∞-Geom*, in the kernel's two forms, on exact instances. For every sector body with `k ≥ 2`: `RelStrictConvex`
  (KInfFoundations.lean:144) fails — two distinct pure states `x ≠ y` of sector 0 have a midpoint `m ∈ Ω` that is a
  boundary state (`IsBoundaryState`, :130: with `y′` a state of sector 1, `m + ε (m − y′)` has sector-1 weight
  `−ε t_1(y′) < 0` for every `ε > 0`, so it lies outside `Ω`); `SingletonFaces` (:139) fails — the sector-0 weight
  `t_0` is an effect (:116), proper (:125, value `0` on sector 1) and certain (:120) on two distinct states. For `Ω⋆⁵`:
  `RelStrictConvex` on instances (midpoints of exact boundary points are interior: `F(m) < 0` strictly), the general
  statement [W] as R-E13.1's strict convexity one dimension up (the body of revolution of the same meridian).
- *(C3) The linear gate clauses.* With `H = homMap N` diagonal (`h_μ = ±1`, `h_0 = 1`), `relT` makes `G` preserve
  the target parity and `relC` makes it carry the control parity `h_{μ'}` to `h_μ = h_{μ'} h_{ν'}`: the free entries
  of `G` are `G[(μ, ν)][(μ′, ν′)]` with `h_ν = h_{ν′}` and `h_μ = h_{μ′} h_{ν′}` — four blocks of size `((D + 1)/2)²`,
  `(D + 1)⁴/4` entries (`64` for `D = 3`, `324` for `D = 5`) — and every other entry is `0` (written: both relations
  are commutation relations with the involutions `1 ⊗ H`, `H ⊗ 1`, `H ⊗ H`, which are diagonal in the table basis).
  The frame (four equations) is then a linear system in the free entries; its exact solution set `F` (a particular
  solution and a nullspace basis, Fraction arithmetic) is the set of `G` meeting frame, `relT`, `relC`; an
  inconsistent system would exclude the body at once.
- *(C4) The positivity relaxation (`posFwd` only).* For exact states `x, y ∈ Ω` and exact effects `e, f` on `Ω`, the
  clause `prodEffVal e f (G (prodState x y)) ≥ 0` is **linear** in `G`; over `F` it is a linear inequality in the
  nullspace coordinates. The probe builds pools of exact states and effects — for the balls the tight effects
  `(1 + v·x)/2` at Pythagorean unit `v`; for `Ω⋆⁵` the supporting effects at exact boundary points (`S ∈ {0, ±7/9}`,
  `‖X‖ ∈ {1, 4/9, 8/9}`, the poles) with a rational upper bound of the support value (valid effects, not tight) and
  loose directional effects — and solves the feasibility LP by a cutting-plane loop (float, HiGHS): maximise the
  margin `t` subject to the sampled inequalities; separate over the pool; stop when no pool constraint is violated
  (`FEASIBLE(pool)`: a float candidate `G`, recorded, not a proof) or when the margin is negative (`INFEASIBLE`),
  in which case a Farkas certificate `y ≥ 0`, `yᵀA = 0`, `yᵀb > 0` is extracted from the dual LP and **exactified**
  over its support in Fraction arithmetic (the exact nullspace of `A_Sᵀ`, the sign and the pairing checked exactly).
  Only an exactly verified certificate counts (`INFEASIBLE-CERTIFIED`); a float-only infeasibility is reported as
  undecided. Validity: every pool inequality is a true consequence of `posFwd` (the effects are effects on `Ω`, the
  states are states), so an exact certificate proves that no `G` in `F` satisfies `posFwd` for that `(z, N)` — with
  no use of `posInv` or `Entangling`.
- *(C5) The sector gate.* For `(3; 3, 3, 3)`: `G = cnot ⊗ id` on the qubit factor (the chart transport `Φ ⊗ Φ`, as
  E16b) meets frame, `relT`, `relC` on all `(D + 1)²` basis tables and `G² = 1`; `posFwd` on exact products through
  the blockwise PSD test; `Entangling` through a rank-four block — so the family supplies native gates in every
  `D ≡ 3 (mod 4)` without K∞-Geom.

**Decision rule (fixed now; `VERDICT E20-ODD-BODIES-EXACT` iff every check and countercontrol behaves as stated;
the outcome is read from the table, not required).**
- **Outcome A (residual real and named):** some probed body with `D` odd `≥ 5` meets (C1), every clause of (C3)
  and (C4) exactly (an exact `G` in `F` with `posFwd`, `posInv` on the probe's instances) **and** (C2).
- **Outcome B′ (exact obstruction for the probed candidates):** `INFEASIBLE-CERTIFIED` for every probed strictly
  convex body of odd `D ≥ 5` (here `Ω⋆⁵`) with its natural `(z, N)`, and for the negative control `eball 5`; the
  positive control `eball 3` `FEASIBLE(pool)`. Then no native gate exists for `Ω⋆⁵` with that `(z, N)` — an exact
  theorem for the body, not the general statement "K∞-Geom with the count forces `d = 3`", which is beyond a probe
  (it would need an argument for every body; the instruction's outcome B is recorded as not reachable by this probe).
- **Outcome C (neither):** the relaxation is `FEASIBLE(pool)` for a strictly convex candidate (no certificate) or
  infeasible but uncertified; the residual stays OPEN, narrowed to the recorded candidate and the method's verdict on
  the negative control (if `eball 5` is `FEASIBLE(pool)`, the relaxation is too weak to see the kernel's exclusion,
  and the `Ω⋆⁵` verdict says nothing).
Countercontrols: XO1 "`eball 3` is `INFEASIBLE`" must fail (`cnot` is a solution in `F`); XO2 "the sector body
`(2; 3, 3)` is relatively strictly convex at the probed midpoint" must fail; XO3 "the frame equations are
inconsistent for `eball 3`" must fail.

**Predictions (sign, strength, reason).** (C1): `(2; 3, 3)`, `(3; 3, 3, 3)`, `(4; 3, 3, 3, 3)` meet the count (`m_i = 2`,
`k + 3k` even, `Σ m_i = 2k` — certain); `(2; 3, 1)` meets it with `m = (2, 1)` (`D = 5`; certain); `(2; 3, 5)` with
`m = (2, 3)` (`D = 9`); `(2; 5, 5)` with `m = (3, 3)` (`D = 11`); `(2; 1, 1)` with `m = (1, 1)` (`D = 3`); `Ω⋆⁵`,
`eball 5`, `eball 3` meet it (certain). (C2): every sector body fails both forms (certain); `Ω⋆⁵` strictly convex on
instances (high). (C3): `F` nonempty for all three strictly convex bodies, of dimension `64 − r₃` and `324 − r₅` with
`r` the frame's rank (high; the four frame vectors span four dimensions, `r = 4·(D+1)` at most, likely less). (C4):
`eball 3` `FEASIBLE(pool)` (certain); `eball 5`: `INFEASIBLE` is more likely than not (0.6) — the kernel's exclusion
rests on the Lorentz positivity of the `E₊` blocks against unit effects, which the tight ball effects express; whether
the certificate exactifies is uncertain (0.5); `Ω⋆⁵`: if `eball 5` is infeasible, `Ω⋆⁵` infeasible with probability
0.6 (its effects are looser, which weakens the test), else undecided. (C5): the `(3; 3, 3, 3)` gate meets everything
(high; E16b's construction with one more sector). Node outcome: C with probability 0.5, B′ 0.35, A 0.15.
