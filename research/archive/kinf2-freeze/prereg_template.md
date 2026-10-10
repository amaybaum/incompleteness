# Reconstruction round KINF-2 — the corrected field-neutral foundations of the pre-quantum completion: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> {{CLAUSE}}

## The declarations

```v3-round
round KINF-2
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kinf-2-foundations/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kinf-2-foundations/
record AM verification/receipts/KINF-2.json
execution A verification/lean-mathlib/OIBridge/KInfFoundations.lean
execution A verification/lean/kinf2_foundations_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/KINF-2.json`. Every other path the round changes is an
execution path listed above. The paths are the same under both outcomes. **No manuscript, no built artifact,
`verification/ROADMAP.md` and no file of the halted round KINF-1's record change under either outcome.**

The module path `OIBridge/KInfFoundations.lean` is the path KINF-1 named for its module. KINF-1 halted with no `E`,
and its withdrawal commit restored that path to its absence at its `F`, so the path does not exist at `D`; the
module this round adds there is this round's, frozen below, and KINF-1's frozen text is not its predecessor in any
build.

The workflow changes by one frozen edit in five places: the round's probe runs in a shard of its own, `probes_kinf2`,
`Numerical probes / KINF-2 foundations`, inserted after the NB-1 shard, which installs `sympy` at the pinned version
`1.14.0`; and the aggregate `Numerical probes` job lists it in its `needs`, reads its result into its environment,
echoes it and tests it for `success`. `controls.py` checks that the workflow at `E` is `D`'s with exactly that edit.

## The objects

- **`D`** = `d6b6458010a6d2812bd3215a8bb6f8a1bab37f00`: the head of `main` after pull request #776; its parents are
  `4507b025` and `25ea67ee`. It is certified by push run 36830862465, overall conclusion `success`: every job
  succeeded (the act 42 exclusion matrix skipped on a push event, as the workflow requires), the release gate passing
  21 of 21 steps with twenty-one receipts holding and the 303 legacy records intact, `lean-axioms` at 5288 named
  results and no sorry. The owner designated it as this round's `D`. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only `verification/receipts/KINF-2.json`.

No other round runs beside KINF-2 at this freeze. Should one land first, its movement of `main` enters KINF-2 only by
reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — vocabulary is not sourcing.** The module defines the objects of the pre-quantum operational completion
over an arbitrary real normed space and proves the lemmas those definitions support. It does not derive any of them
from the substratum, from the finite operational characterization, or from any OI construction: no theorem of this
round has a premise of the form *the completion has property P* discharged by a corpus declaration. Field-neutral
drivability (K∞-R), supporting-effect completeness (K∞-1), singleton faces (SF) and copy naturality stay open, and
this round names them as definitions so that later rounds can state what discharges them. **No outcome says that OI
supplies, derives or sources any of them.**

**Hazard 2 — one theorem is imported kinematics.** `qubit_certain_face` is a statement about complex `2 × 2`
matrices: a density matrix certain for the effect `ρ ↦ ρ 0 0` is `|0⟩⟨0|`. It is not a field-neutral result and it
does not source (SF). It is the only theorem of the module that consumes a corpus declaration
(`OIBridge.CoherentExtension.psd_diag_zero_entry_zero`), and the only one that mentions `ℂ`.

**Hazard 3 — K∞-1 is a definition.** `KInf1 Ω avail` is the proposition *a compact convex body admitting an
elementary drive has supporting-effect completeness relative to `avail`*. The module proves it for the unit ball of
`ℝ³` with its full effects and refutes it for the same ball with the unit effect alone; both are controls that show
the proposition is neither vacuous nor automatic, and neither is a statement about the completion's effects.
`relStrictConvex_of_kInf1` records only what the hypothesis buys together with singleton faces. **No outcome says that
K∞-1 holds for the completion**, and nothing in the module is a reconstruction theorem.

**Hazard 4 — three layers, never merged.** The round certifies its content in three layers that do not substitute for
one another (`AGENTS.md`, *Keep verification layers distinct*):

| layer | what it carries | where |
| --- | --- | --- |
| **kernel** (evidence level 2) | the definitions; L1–L7 and Lemma C with its converse; the semantic controls of Hazard 6; Lemma D and its full-effects corollary; Lemma B; the finite-exposure bounds; Theorem F2; `copyNatural_iff_apply`; `qubit_certain_face`; `KInf1` with its two controls and `relStrictConvex_of_kInf1`; the verdict `kinf2_kernel_core` | `KInfFoundations.lean` |
| **exact computation**, replayed in CI | the instances tabulated under *What the exact layer instantiates*, among them the square gbit, the torus and Stiefel orbitopes, the 3-ball and the disk, the SIC ball, the Carathéodory orbitope `C₂`, the regular pentagon, the degenerate bodies and the route-neutrality controls | `kinf2_foundations_probe.py` |
| **written argument** | that corrected drivability excludes the square gbit and the rebit disk (the proof obligation below); that strict convexity relative to the affine span gives the facet condition of Theorem F2; the reduction behind the pentagon's capacity bound | this file, *The mathematics* |

**Hazard 5 — definitions are frozen whole.** Unlike a theorem, a definition has no proof to repair: its text *is* its
content. Every `structure` and `def` of the module is frozen byte for byte, proof fields included where a definition
carries them (`rotLin`, `rotEquiv`, `cycEquiv`, `ball3Drive`), and `controls.py` compares each at `E`. A definition
that cannot be kept as frozen is a **freeze failure**, not a repair, and the round halts under the specification's
`S12`.

**Hazard 6 — semantic controls, before `F`.** Round KINF-1 halted because two of its frozen predicates did not mean
what its preregistration said: every one of its definitions elaborated and every theorem was true, and the defect was
in what the definitions said. This round therefore carries, for every frozen predicate, a check that it holds
somewhere without holding vacuously and a check that it fails somewhere, chosen so that each failure is the one the
predicate exists to detect. The checks are kernel theorems where the table says so:

| predicate | holds | fails | layer |
| --- | --- | --- | --- |
| `IsProperOn` | the proper effects `not_singletonFaces_square`, `supportingEffectComplete_Icc` and `supportingEffectComplete_ball3` exhibit | the unit, and every effect identically one on the body (`not_isProperOn_const_one`, `not_isProperOn_of_eq_one`) | kernel |
| `IsBoundaryState` | `1` in `[-1, 1]` (`isBoundaryState_Icc_one`); `(1, 0, 0)` in the ball (`isBoundaryState_ball3`) | every interior point (`not_isBoundaryState_of_mem_interior`), so an open body has none (`supportingEffectComplete_of_isOpen`) | kernel |
| `SupportingEffectComplete` | `[-1, 1]` with its full effects (`supportingEffectComplete_Icc`); the ball with its full effects (`supportingEffectComplete_ball3`) | `[-1, 1]` with the unit alone (`not_supportingEffectComplete_unit`) | kernel |
| `SingletonFaces` | every closed ball of a strictly convex space, with any family (`singletonFaces_closedBall`) | the sup-norm square with its full effects (`not_singletonFaces_square`) | kernel |
| `RelStrictConvex` | every strictly convex body (`relStrictConvex_of_strictConvex`) | the sup-norm square (`not_relStrictConvex_square`) | kernel |
| `ElementaryDrivability` | the unit ball of `ℝ³` (`ball3_drivable`) | the classical bit `[-1, 1]` (`not_drivable_Icc`) and a one-point body (`not_drivable_singleton`) | kernel |
| `KInf1` | the ball with its full effects (`kInf1_ball3_full`), non-vacuously, since the ball is compact, convex and drivable | the ball with the unit effect alone (`not_kInf1_ball3_unit`) | kernel |
| `CentrallySymmetric`, capacity | the torus and Stiefel orbitopes | `C₂` and the regular pentagon | exact |

Review compares each predicate's text with its prose meaning on the unit effect, on a lower-dimensional body, on an
open body and on a contracting `J`, the four probes that expose KINF-1's defects. The kernel controls cannot show that
a predicate means what the prose says; they show that it is neither vacuous nor automatic on the bodies named, which
is the property whose absence halted KINF-1.

**Hazard 7 — manuscripts.** None. The census family is `kernel-only` with no anchor, under both outcomes.

**Hazard 8 — history.** Round KINF-1 and every earlier round stand as recorded; KINF-1's record directory and receipt
are not touched, and the provenance table below is this round's account of what replaces what. The research notes
behind this round, from `D`, are design evidence only; none is a record of this round.

***

## Provenance — KINF-1's frozen statements, their defects, and their replacements here

Round KINF-1 halted under `S12`; its record, `programmes/oi-qm/reconstruction/round-kinf-1-foundations/`, and its
receipt `verification/receipts/KINF-1.json` stand unchanged. Its result note lists `ElementaryDrivability` among the
definitions unaffected by the defect for which it halted. **That statement is incorrect**: the third row below
records the defect it missed. The table is the authoritative account of how each defective KINF-1 statement is
replaced here.

| KINF-1 frozen statement | defect discovered | successor replacement |
| --- | --- | --- |
| `SupportingEffectComplete Ω avail := ∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x = 1` | (i) the unit effect is certain everywhere, so the condition holds for every body once the unit is available; (ii) `frontier` is read in `V`, so a body that is not full-dimensional in `V` — every finite-stage body, which lies in the hyperplane `v unit = 1` — has no interior, and the condition then concerns points the body's own geometry does not treat as boundary | `IsBoundaryState` reads the boundary in `Ω`; the witnessing effect must be `IsProperOn Ω`, tested on `Ω`. A syntactic test such as `e ≠ const 1` reintroduces (i) on finite-stage bodies, which the probe checks |
| `SingletonFaces Ω avail := ∀ e ∈ avail, IsEffectOn Ω e → (certainFace Ω e).Subsingleton` | the unit's certain face is all of `Ω`, so the condition fails for every body with two states once the unit is available | the condition bounds proper effects only; `singletonFaces_insert_iff` and `supportingEffectComplete_insert_iff` prove that a non-proper effect changes neither condition |
| `ElementaryDrivability`: `flow_preserves`, `J_preserves` mapping `Ω` into `Ω`, no group law, `J_off_axis` compared on `V` | the flow need not compose as a group and need not map `Ω` onto itself, `J` need not be an automorphism of `Ω`, and the off-axis clause can be met off `Ω`; exact witnesses show that the square gbit (a rotate-and-shrink path from `I` to `−I`), the rebit disk (a contracting `J`) and the disk placed in `ℝ⁴` (a `J` that is the identity on `Ω`) all satisfy it | `flow_add`, a one-parameter group; `N_involutive` on `Ω`; `J_symm_preserves`, so that `J` is an automorphism of `Ω`; `J_off_axis` compared on `Ω`. That this excludes the square gbit and the disk is the written proof obligation below, not a kernel statement |
| `strictConvex_of_supporting_singleton : Convex → IsClosed → SEC → SF → StrictConvex ℝ Ω` | its hypotheses were jointly unsatisfiable on every body with two states whose effect family contains the unit, and `StrictConvex` is read in `V` | `relStrictConvex_of_supporting_singleton : Convex → SEC → SF → RelStrictConvex Ω`, with the converse `singletonFaces_of_relStrictConvex` proved separately and `relStrictConvex_of_strictConvex` as the bridge to Mathlib's notion |
| `KInf1 Ω avail := Nonempty (ElementaryDrivability Ω) → SEC Ω avail`; `strictConvex_of_kInf1` | `KInf1 Ω (fullEffects Ω)` held trivially for every body; and on an open body, with no boundary state, any corrected (SEC) holds vacuously | `KInf1` restated over the corrected definitions for compact convex bodies, with the controls `kInf1_ball3_full` and `not_kInf1_ball3_unit`; `relStrictConvex_of_kInf1` |

## The proof obligation this round does not discharge

**Corrected drivability excludes the square gbit and the rebit disk.** This round states it as an obligation, with
the argument written and not certified:

- *The square.* An affine automorphism of `V` preserving the square, with its inverse, permutes its four vertices,
  and the probe enumerates exactly eight such maps on the vertices (`D₄`). A flow `t ↦ flow t` is continuous into the
  maps of `V`, so on each vertex it is a continuous path into a four-point set, hence constant; at `t = 0` it is the
  identity. So every flow member fixes the vertices, hence the square, and no member moves a state: `N_moves` fails.
- *The disk.* An affine automorphism of `V` preserving the disk, with its inverse, acts on it as an element of
  `O(2)` about its centre, and a continuous one-parameter group of them acts as rotations `R_{ct}`. If `c = 0`, no
  flow member moves a state and `N_moves` fails. Otherwise every rotation is a flow member on the disk, and
  conjugating a rotation by any element of `O(2)` gives a rotation, so `J_off_axis`, compared on `Ω`, fails. The probe
  checks the conjugation identity for a reflection.

The continuity step, the passage from preserving the body to acting through its vertex or isometry group, and the
group-theoretic step are written. A later round that proves either exclusion in the kernel discharges this
obligation; no outcome of this round says either exclusion is a kernel statement. The classical bit's exclusion is
proved in the kernel here (`not_drivable_Icc`), by a different route: a flow member at half the NOT's parameter is an
affine map of the line preserving `[-1, 1]` with an inverse that preserves it too, hence `±` the identity, so the NOT,
its square, is the identity.

## The route-neutral geometric slot

The module freezes `RelStrictConvex Ω` as the body-level geometric input, and the singleton-face route as one
producer of it: given (SEC), (SF) for a family implies `RelStrictConvex Ω` (L4), and `RelStrictConvex Ω` implies (SF)
for every family (L5), each direction proved by its own theorem. The module freezes no self-duality or homogeneity
definition. A later round may add another producer of `RelStrictConvex Ω`. The exact layer's regular pentagon fixes
what such a producer needs: the pentagon is strongly self-dual, its automorphism group acts transitively on ordered
frames, it has capacity two with its full effects, it is not centrally symmetric, and an edge effect is proper and
certain on a whole edge, so it violates (SF) and is not relatively strictly convex. Self-duality, frame transitivity
and capacity two together therefore do not produce the slot. The real qutrit and the classical trit, whose cones are
symmetric, are not relatively strictly convex either.

## Provenance of the module

The module imports Mathlib and one corpus module:

- `Mathlib.Analysis.Convex.Gauge`, `Mathlib.Analysis.Convex.Strict`, `Mathlib.Analysis.Convex.StrictConvexSpace`,
  `Mathlib.Analysis.Convex.Topology`, `Mathlib.Analysis.Normed.Module.Basic`,
  `Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic`, `Mathlib.Data.Set.Card`,
  `Mathlib.LinearAlgebra.Matrix.PosDef`, `Mathlib.LinearAlgebra.Matrix.Trace`.
- `OIBridge.CoherentExtension`, for `psd_diag_zero_entry_zero` alone, consumed by `qubit_certain_face` alone.

The probe imports the Python standard library (`sys`, `fractions`, `itertools`) and `sympy`, pinned at `1.14.0` in
its shard.

## Locating controls — at `D`

The sources this round's hazards cite:

| what | where | line |
| --- | --- | --- |
| `psd_diag_zero_entry_zero` | `verification/lean-mathlib/OIBridge/CoherentExtension.lean` | 183 |
| `DrivesElementary`, the matrix-level drivability premise | `verification/lean-mathlib/OIBridge/SubstratumSource.lean` | 77 |
| `genTheory_elementary`, `genTheory_qm_of_quantumArchitecture` (matrix K∞-R ⇒ matrix K∞-E) | `verification/lean-mathlib/OIBridge/SubstratumSource.lean` | 109, 136 |
| the halted round KINF-1: its preregistration, result note and receipt | `verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/`, `verification/receipts/KINF-1.json` | — |

| file at `D` | blob |
| --- | --- |
| `CoherentExtension.lean` | `81c71c78614d64f82839799ec7f87738ad9a0be5` |
| `SubstratumSource.lean` | `4d053fe6c2d8c1d9ee96a8dcfaff721493c21269` |
| KINF-1 `preregistration.md` | `5630f1f595679673784b1d433dbf59e33d9b0140` |
| KINF-1 `result.md` | `153f6034e28606b34b46e4cc3e390a25a10bde85` |
| `verification/receipts/KINF-1.json` | `ebd0c597d4dae7d8324f7bfc0d9c4bb96fccf368` |
| `verification/lean-mathlib/OIBridge.lean` | `5143e4bc6320773d0e1b5578fc267ea4cb5960cd` |
| `verification/lean-manuscript-census.json` | `242443c63a4a0183e8495fd2b86b39b222b54002` |
| `.github/workflows/verify.yml` | `df249b7c9c3ca8f3fd7a07ffdcdc5a28c176036d` |

The names this round introduces return nothing from `git grep -l` at `D`: `kinf2`, `KINF-2`, `round-kinf-2`,
`IsProperOn`, `IsBoundaryState`, `RelStrictConvex` and `ball3Drive`. `KInfFoundations` occurs at `D` only in KINF-1's
record.

***

## Why this round exists

The K programme tracks the obligation to reach the quantum kinematics from field-free principles. Round KINF-1 was
to fix the vocabulary in which that obligation is stated, and halted on a freeze failure: its supporting-effect and
singleton-face predicates were trivialized and falsified by the unit effect, and, as research after the halt found,
its drivability structure admitted the square gbit and the rebit disk. This round fixes the corrected vocabulary,
proves the lemmas it supports, and carries the semantic controls that KINF-1 lacked: each frozen predicate is shown
to hold and to fail on named bodies, in the kernel where the table of Hazard 6 says so. Its geometric input is
route-neutral: relative strict convexity of the body, produced here by the singleton-face route and by nothing else,
with the pentagon fixing what another producer would need. It does not claim to source quantum theory.

***

## The mathematics — FROZEN

**Setting.** `V` is a real normed space. A **body** is a subset `Ω ⊆ V`; the lemmas add convexity or compactness as
they need them. An **effect** on `Ω` is an affine functional `e : V →ᵃ[ℝ] ℝ` with `0 ≤ e ≤ 1` on `Ω`; it is
**proper** on `Ω` when `e y < 1` for some `y ∈ Ω`; its **certain face** is `{x ∈ Ω | e x = 1}`. A **boundary state**
of `Ω` is an `x ∈ Ω` for which some `y ∈ Ω` has `x + ε(x − y) ∉ Ω` for every `ε > 0`: the segment from `y` through `x`
cannot be extended beyond `x` in `Ω`. A family `avail` of affine functionals is the round's stand-in for *the effects
the completion makes available*; the **full effects** are every affine functional that is an effect on `Ω`, the unit
among them.

**The definitions.**

| name | statement |
| --- | --- |
| `FiniteStage`, `FiniteStage.vec`, `FiniteStage.states` | finitely many preparations and effects, a table in `[0, 1]`, a unit effect; the probability vectors and their convex hull |
| `IsEffectOn Ω e`, `certainFace Ω e`, `IsProperOn Ω e`, `IsBoundaryState Ω x` | as above |
| `SupportingEffectComplete Ω avail` (SEC) | every boundary state of `Ω` is certain for some proper available effect |
| `SingletonFaces Ω avail` (SF) | every proper available effect is certain on at most one state |
| `RelStrictConvex Ω` | every point strictly between two distinct states is a state and not a boundary state |
| `fullEffects Ω`, `PerfectlyDistinguishable Ω x e`, `CentrallySymmetric Ω c` | as in KINF-1, unchanged |
| `ElementaryDrivability Ω` | a continuous one-parameter group `flow : ℝ → V ≃ᵃ[ℝ] V` of affine automorphisms of `V` preserving `Ω`, the identity at `0`; a parameter `t₀` at which the flow is an involution of `Ω` moving some state (the NOT `N`); an automorphism `J` of `V` with `J` and `J⁻¹` preserving `Ω`, such that for some `t` the conjugate `J ∘ flow t ∘ J⁻¹` agrees on `Ω` with no flow member |
| `CopyNatural N_A N_B e` | `N_B = e ∘ N_A ∘ e⁻¹` |
| `exposedPoints`, `simplex`, `ClassicallyExposed` | as in KINF-1, unchanged |
| `ball3`, `rotFun`, `rotLin`, `rotEquiv`, `rot3`, `cycEquiv`, `cyc3`, `ball3Drive` | the unit ball `{v | v₀² + v₁² + v₂² ≤ 1}` of `ℝ³`; the rotation by `t` about the third axis, as a function, a linear map, a linear equivalence and an affine automorphism; the cyclic permutation `(x, y, z) ↦ (z, x, y)`; the drive of the ball they make |
| `affR`, `squareEdgeEffect`, `ballEffect` | the effects `t ↦ a + b t` on `ℝ`, `v ↦ (1 + v₀)/2` on the plane and `v ↦ (1 + u · v)/2` on `ℝ³` |
| `KInf1 Ω avail` | `IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail` |

**The lemmas, each with its proof.**

- **`states_isCompact`, `states_convex`, `states_isClosed`, `states_unit`** *(kernel)*. As in KINF-1.
- **L1, `not_isProperOn_of_eq_one`, `not_isProperOn_const_one`** *(kernel)*. An effect identically one on `Ω` has no
  state below one.
- **L2, `eq_one_of_certain_of_not_boundary`** *(kernel)*. If `e x = 1` at a state `x` that is not a boundary state,
  then for each `y ∈ Ω` some `x + ε(x − y)` with `ε > 0` lies in `Ω`, and
  `e(x + ε(x − y)) = (1 + ε) − ε·e y ≤ 1` forces `e y ≥ 1`, so `e y = 1`.
- **L3, `isBoundaryState_of_certain_proper`** *(kernel)*. A proper effect certain at a state picks out a boundary
  state: otherwise L2 makes it identically one.
- **L6, `supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff`** *(kernel)*. Both predicates quantify over
  proper effects, so adding a non-proper one changes neither.
- **Lemma C (L4), `relStrictConvex_of_supporting_singleton`** *(kernel)*. `Ω` convex with (SEC) and (SF); for `x ≠ y`
  in `Ω` and `a, b > 0`, `a + b = 1`, the point `z = a•x + b•y` is in `Ω`. If `z` were a boundary state, a proper
  available effect `e` would have `e z = 1`, so `a·e x + b·e y = 1` with `e x, e y ≤ 1` forces `e x = e y = 1`, and
  (SF) gives `x = y`.
- **L5, `singletonFaces_of_relStrictConvex`** *(kernel)*. If a proper effect `e` were certain at `x ≠ y`, it would be
  certain at their midpoint, which is a state and not a boundary state, and L2 would make `e` identically one.
- **L7, `relStrictConvex_of_strictConvex`, with `not_isBoundaryState_of_mem_interior`** *(kernel)*. An interior point
  `z` has a neighbourhood in `Ω`, and `ε ↦ z + ε(z − w)` is continuous at `0`, so some `ε > 0` stays in `Ω`.
  `supportingEffectComplete_of_isOpen` follows: an open body has no boundary state.
- **The semantic controls** *(kernel)*. `singletonFaces_closedBall` is L5 ∘ L7 with Mathlib's `strictConvex_closedBall`.
  `not_singletonFaces_square`: `(1 + v₀)/2` is an effect on the sup-norm square, `1/2` at `0`, and certain at
  `(1, 1)` and `(1, −1)`; `not_relStrictConvex_square` is its contrapositive through L5. `supportingEffectComplete_Icc`: the boundary states of `[-1, 1]` are `±1`, certain for
  `(1 ± t)/2`. `not_supportingEffectComplete_unit`: `1` is a boundary state and the unit is not proper.
  `ball3_drivable`: the rotations about the third axis are a continuous group preserving `v₀² + v₁² + v₂²`
  (`(cos t·v₀ − sin t·v₁)² + (sin t·v₀ + cos t·v₁)² = (cos² t + sin² t)(v₀² + v₁²)`), the half-turn sends `(1, 0, 0)`
  to `(−1, 0, 0)`, and with `J` the cyclic permutation, `J ∘ flow π ∘ J⁻¹` sends `(0, 0, 1)` to `(0, 0, −1)` while
  every flow member fixes it. `not_drivable_Icc`: with `h = flow(t₀/2)` and `k = flow(−t₀/2)`, both affine maps of
  the line `x ↦ a + b x` and `x ↦ c + d x` preserve `[-1, 1]` and `h ∘ k = id`, so `b d = 1`, `a² + b² ≤ 1` and
  `c² + d² ≤ 1`, whence `b² ≥ 1`, `a = 0` and `b² = 1`; the NOT, `h ∘ h`, is `x ↦ b² x`, the identity.
  `supportingEffectComplete_ball3`: a state with `|x|² < 1` is not a boundary state, since a step of a sixteenth of
  `1 − |x|²` towards any `y` stays in the ball (`ball3_extend`); at `|x|² = 1` the effect `(1 + x · v)/2` lies in
  `[0, 1]` on the ball, is `1/2` at `0` and is `1` at `x`. `not_kInf1_ball3_unit`: the ball is compact, convex and
  drivable, `(1, 0, 0)` is a boundary state, and the unit is not proper.
- **Lemma D, Lemma B, the finite-exposure bounds, Theorem F2, `copyNatural_*`, `qubit_certain_face`** *(kernel)*. As
  in KINF-1, statements and proofs unchanged.
- **`relStrictConvex_of_kInf1`** *(kernel)*. Lemma C with `KInf1 Ω avail`, compactness, convexity and a drive in place
  of (SEC).
- **Written remarks, not kernel statements.** The exclusions of the proof obligation above. A body strictly convex
  relative to its affine span meets each coordinate facet in at most one point, the hypothesis of Theorem F2 as the
  kernel states it. Three perfectly distinguishable states of a polytope give three perfectly distinguishable
  vertices, which reduces the pentagon's capacity bound to its vertex triples.

**What the exact layer instantiates** (the probe; not the kernel):

| section | what is checked exactly | what it shows |
| --- | --- | --- |
| 1, 2 | the line-extension and affine-combination identities; the unit, and an effect identically one on a lower-dimensional body but not constant on `V`, are not proper, while a syntactic properness test admits them | L1–L3 as identities; the properness test must be read on `Ω` |
| 3 | the square gbit: facet effects proper and certain on an edge; (SEC) with facet effects on a boundary grid; capacity two; KINF-1's drivability met by a rotate-and-shrink path; exactly eight affine automorphisms on the vertices | the KINF-1 drivability defect, and the enumeration behind the written exclusion |
| 4, 5 | the torus and Stiefel orbitopes: centrally symmetric, a proper effect certain on a flat face, drivability witnessed | (SF) fails independently of capacity, central symmetry and drivability |
| 6 | the 3-ball: (SEC), (SF) and relative strict convexity with full effects, drivability; the disk: KINF-1's `J` clause met by a contraction, the corrected clause failing by the reflection conjugation identity | every corrected premise holds together on the ball; the disk witness for the proof obligation |
| 7 | the SIC ball in `ℚ(√3)`: at a generic pure state a certain response effect is the unit, so (SEC) with response effects fails there and holds at the four tangency points | K∞-1 is a proposition about the effect family; Theorem F2 is attained |
| 8 | the Carathéodory orbitope `C₂` in `ℚ(√3)`: the three effects sum to the unit, are `δᵢⱼ` at the triple, and are nonnegative on the whole circle by a symbolic product identity; `C₂` is not centrally symmetric | Lemma D's hypothesis is load-bearing |
| 9 | the regular pentagon in `ℚ(√5)`: an affine image of the regular pentagon; ten affine automorphisms, transitive on ordered frames; strongly self-dual; capacity two with full effects, every vertex triple excluded; not centrally symmetric; an edge effect proper and certain on a whole edge | the route-neutral slot's control |
| 10 | empty, singleton and open bodies; the segment; the triangle | the degenerate cases and the compactness requirement |
| 11 | the real qutrit violates (SF); the Lean composition order of the off-axis clause | symmetric cones reach the slot only with more than self-duality |
| 12 | each mutated predicate, identity or enumeration gives the opposite verdict | the probe's checks are not vacuous |

***

## The frozen Lean text

The module is `verification/lean-mathlib/OIBridge/KInfFoundations.lean`. Its header, up to `namespace OIBridge`, is
frozen byte for byte:

```lean
{{HEADER}}
```

**Definition budget: exactly the frozen definitions.** The module carries the structures and definitions frozen
below and no other; `controls.py` fails on any `def`, `abbrev`, `instance`, `structure`, `class` or `inductive` not in
the frozen list (`attribute [instance]` on the two `Fintype` fields of `FiniteStage` is not a declaration).

**The declarations, FROZEN** — each structure and definition whole, from its keyword to the blank line that ends it,
and each theorem's text from `theorem` to the `:=` that opens its proof, byte for byte, shown here with the proofs
elided:

```lean
{{DECLARATIONS}}
```

### The declarations, FROZEN by name and role

| role | declaration |
| --- | --- |
| verdict, `KINF-2-FOUNDATIONS-PROVED` | `kinf2_kernel_core` |
| the finite stage | `FiniteStage`, `FiniteStage.vec`, `FiniteStage.states`, `states_isCompact`, `states_isClosed`, `states_convex`, `states_unit` |
| effects and the premises | `IsEffectOn`, `certainFace`, `IsProperOn`, `IsBoundaryState`, `SupportingEffectComplete`, `SingletonFaces`, `RelStrictConvex`, `fullEffects`, `PerfectlyDistinguishable`, `CentrallySymmetric`, `affine_combo`, `affine_reflect`, `convex_affine_le` |
| proper effects and boundary states | `extension_eq`, `not_isProperOn_of_eq_one`, `not_isProperOn_const_one`, `eq_one_of_certain_of_not_boundary`, `isBoundaryState_of_certain_proper`, `supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff` |
| drivability and copy naturality | `ElementaryDrivability`, `ElementaryDrivability.N`, `CopyNatural`, `copyNatural_refl_iff`, `copyNatural_iff_apply` |
| the drivability controls | `ball3`, `mem_ball3`, `vec3_ext`, `ball3_convex`, `ball3_isCompact`, `rotFun`, `rotFun_apply`, `rotFun_zero`, `rotFun_add`, `rotFun_mem_ball3`, `rotLin`, `rotEquiv`, `rot3`, `rot3_apply`, `cycEquiv`, `cyc3`, `cyc3_apply`, `cyc3_symm_apply`, `cyc3_mem_ball3`, `cyc3_symm_mem_ball3`, `ball3Drive`, `ball3_drivable`, `affineEquiv_real_apply`, `bit_aux`, `not_drivable_Icc`, `not_drivable_singleton` |
| Lemma C and its converse | `relStrictConvex_of_supporting_singleton`, `singletonFaces_of_relStrictConvex`, `not_isBoundaryState_of_mem_interior`, `relStrictConvex_of_strictConvex`, `supportingEffectComplete_of_isOpen` |
| Lemma D | `card_le_two_of_centrallySymmetric`, `card_le_two_of_centrallySymmetric_full` |
| the (SF) and (SEC) controls | `singletonFaces_closedBall`, `not_relStrictConvex_square`, `affR`, `affR_apply`, `isBoundaryState_Icc_one`, `not_supportingEffectComplete_unit`, `supportingEffectComplete_Icc`, `squareEdgeEffect`, `squareEdgeEffect_apply`, `not_singletonFaces_square` |
| Lemma B and the finite-preparation bound | `eq_closedBall_of_frontier_subset_sphere`, `exists_vertex_of_certain`, `exposed_mem_range`, `exposedPoints`, `exposed_ncard_le`, `FiniteStage.exposed_le_card` |
| Theorem F2 | `simplex`, `ClassicallyExposed`, `response_eq_one_forces`, `mem_of_classicallyExposed`, `exists_zero_of_classicallyExposed`, `classical_exposed_ncard_le` |
| imported kinematics | `qubit_certain_face` |
| hypothesis K∞-1 and its controls | `KInf1`, `relStrictConvex_of_kInf1`, `ballEffect`, `ballEffect_apply`, `ball3_extend`, `supportingEffectComplete_ball3`, `kInf1_ball3_full`, `isBoundaryState_ball3`, `not_kInf1_ball3_unit` |

Every theorem is followed, after the namespace closes, by its `#print axioms OIBridge.KInfFoundations.…` line. A
proof-only repair may add theorems named `kinf2_shared_…`.

### The reference implementation

**Frozen**, and checked by `controls.py` at `E`: the header, every declaration's text, the theorem names, one
`#print axioms` line per theorem, no definition beyond the frozen ones, the forbidden tokens (`sorry`, `admit`,
`native_decide`, `axiom`, `unsafe`, `opaque`, `implemented_by`, `extern`), and no `set_option` but
`linter.unusedSectionVars false`.

**Not frozen: the proofs of the theorems.** The reference implementation is blob **`{{REF_BLOB}}`**. A proof-only
repair — a change that leaves every frozen surface unchanged — is permitted as a later linear commit before `E`; the
result note names the reference blob and the module's blob at `E`, and, if they differ, states the departure from
the reference implementation and justifies it, which `controls.py` checks. A definition or structure that must
change is a freeze failure (Hazard 5).

### Pre-freeze evidence — design evidence, not attestation

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, on a disposable branch, never landed. None
is a `check-run` attestation, and no predicate of the round reads them. Each was left to finish; the table records,
job by job, what finished and how.

{{DESIGNRUNS}}

***

## The exact-computation layer — the frozen probe

`verification/lean/kinf2_foundations_probe.py`, blob **`{{PROBE_BLOB}}`**, is written before `F` and added by the
execution at stage 1 with exactly this blob, and the workflow runs it in its own shard at every execution commit from
stage 1 on. It uses Python integers and `Fraction`s, pairs `a + b√3` and `a + b√5` of them, and `sympy` polynomial
and rational-function identities, for every value it asserts: **no floating point and no randomness.** Every point at
which an identity is tested is fixed in the file, so two runs print the same bytes. It exits 1 on any mismatch. Each
check is tagged `witness`, `identity`, `enumerate` or `sample`; a `sample` check is evidence for the universal claim it
instantiates, not a proof of it, and the written notes it prints are not checks. Its statements are exact arithmetic
replayed; they are not kernel-certified, and the result note names them as this layer's. Its twelve sections are the
instances tabulated above under *What the exact layer instantiates*.

It ends with the line `{{PROBE_OK}}` on success, which the result note carries verbatim, and
`kinf2_foundations_probe: FAILED …` otherwise. It runs in about a second.

***

## The question, FROZEN — one target

### `KINF-2` — the corrected vocabulary, its lemmas and its controls, in the kernel

**Do the frozen definitions elaborate, and do the frozen theorems hold in the kernel about them, as the verdict
`kinf2_kernel_core` states; and, with the frozen probe green at `E`, does the exact layer instantiate the controls as
tabulated? The frozen answer is yes, in the layers Hazard 4 names.**

| part | statement | witness | layer |
| --- | --- | --- | --- |
| inert non-proper effects | adding a non-proper effect changes neither (SEC) nor (SF) | `supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff` | kernel |
| Lemma C | convex + (SEC) + (SF) ⇒ relatively strictly convex | `relStrictConvex_of_supporting_singleton` | kernel |
| its converse | relatively strictly convex ⇒ (SF) for every family | `singletonFaces_of_relStrictConvex` | kernel |
| the semantic controls | each premise holds and fails as Hazard 6 tabulates | the theorems named there | kernel |
| Lemma D | central symmetry ⇒ at most two perfectly distinguishable states, with any effects | `card_le_two_of_centrallySymmetric`, `…_full` | kernel |
| Lemma B | compact convex, `0` interior, frontier on the unit sphere ⇒ the closed unit ball | `eq_closedBall_of_frontier_subset_sphere` | kernel |
| finite preparations | exposed points are preparation vectors; at most `|ι|` | `exposed_mem_range`, `exposed_ncard_le` | kernel |
| Theorem F2 | at most `N` classically exposed points given the facet condition | `classical_exposed_ncard_le` | kernel |
| copy naturality | the pointwise conjugation identity | `copyNatural_iff_apply` | kernel |
| the qubit face | the certain face of `ρ ↦ ρ 0 0` is `{|0⟩⟨0|}` | `qubit_certain_face` | kernel, imported kinematics |
| K∞-1 | stated as `KInf1`; holding and failing on the ball; Lemma C under it | `KInf1`, `kInf1_ball3_full`, `not_kInf1_ball3_unit`, `relStrictConvex_of_kInf1` | kernel (definition and controls) |
| the instances | sections 1–12 | the probe | exact computation |
| drivability's exclusions | the square gbit and the rebit disk are not drivable | this file | written, a proof obligation |

When this table, the result note or the census displays the two-way relation between (SF) and relative strict
convexity given (SEC), it cites L4 for one direction and L5 for the other.

The answer is reported as one of two labels: `KINF-2-FOUNDATIONS-PROVED`, the verdict `kinf2_kernel_core` in the
kernel with the probe green at `E`; `KINF-2-UNDECIDED`. The probe is not a label: green at `E`, it certifies its
layer; red at `E`, the round halts as a freeze failure.

## The controls

| role | object | what it is for |
| --- | --- | --- |
| each premise is neither vacuous nor automatic | the kernel controls of Hazard 6 | the check whose absence halted KINF-1 |
| Lemma D's hypothesis is load-bearing | `C₂`, capacity three | a body that is not centrally symmetric exceeds the bound |
| (SF) is independent of capacity, central symmetry and drivability | the torus and Stiefel orbitopes | capacity two, full effects, flat faces, drivable |
| self-duality, frame transitivity and capacity two do not give (SF) | the regular pentagon | the route-neutral slot's control |
| K∞-1 depends on the effect family | the SIC ball with response effects; `not_kInf1_ball3_unit` | (SEC) fails for a restricted family on a drivable body |
| the probe's checks are not vacuous | section 12 | each mutation gives the opposite verdict |
| the frozen surfaces | `controls.py check E` | the declarations, the header, the note, the surfaces and the paths |

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `KINF-2` | `KINF-2-FOUNDATIONS-PROVED` | **very high** | every declaration elaborated and every theorem built within the three axioms in the design runs recorded above; the probe shard succeeded at the same heads |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `KINF-2-FOUNDATIONS-PROVED`

> {{SENT_P}}

### `KINF-2-UNDECIDED`

> {{SENT_U}}

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, the label's sentence, the clause at
its mention `**THE CLAUSE, carried at this mention — the result.**`, the probe's summary line from the run at `E`, and
the reference blob and the module's blob at `E`. Outside the frozen sentence and the clause it does not contain any of
the phrases *OI supplies*, *OI derives*, *OI sources*, *sourced from OI*, *derived from the substratum*, *K∞-1 holds
for the completion*, *K∞-1 is proved*, *proves K∞-1*, *reconstruction theorem for*, *the completion is a ball*, *full
effects hold*, *excludes the square gbit in the kernel*, *kernel-certified exclusion*, *self-duality is excluded* or
*self-duality is required*, which `controls.py` checks.

| row | outcome |
| --- | --- |
| 1 | `KINF-2-FOUNDATIONS-PROVED` |
| 2 | `KINF-2-UNDECIDED` |

## The census, FROZEN

`verification/lean-manuscript-census.json` gains one family, appended last, the same under both outcomes: modules
`["KInfFoundations"]`, status `kernel-only`, no manuscript anchor, named

```text
{{FAMILY_NAME}}
```

with the note

```text
{{FAMILY_NOTE}}
```

## The workflow edit, FROZEN

After the NB-1 shard, the job

```yaml
{{WORKFLOW_JOB}}```

and, in the aggregate `Numerical probes` job, `probes_kinf2` after `probes_nb1` in `needs`,
`KINF2_RESULT: ${{ needs.probes_kinf2.result }}` after `NB1_RESULT`, `echo "kinf2=${KINF2_RESULT}"` after the NB-1
echo, and `test "${KINF2_RESULT}" = success` after the NB-1 test. `OIBridge.lean` gains
`import OIBridge.KInfFoundations` directly after `import OIBridge.NativeGateBall`.

***

## What no outcome licenses

- **No outcome says that OI supplies, derives or sources** drivability, supporting effects, singleton faces or copy
  naturality; the definitions name them, and nothing discharges them.
- **No outcome says that K∞-1 holds for the completion**, or that the completion's state space is a ball, or that its
  effects are the full effects. The ball's two K∞-1 controls are controls.
- **No outcome says that corrected drivability's exclusion of the square gbit or the rebit disk is a kernel
  statement**; it is a written argument and an open proof obligation.
- **No outcome says that self-duality or homogeneity is excluded, preferred or required**; the module freezes no such
  premise, and the pentagon shows only that three named properties together do not give (SF).
- **No outcome calls `qubit_certain_face` a field-neutral result**: it is a theorem of the imported qubit kinematics.
- **No outcome calls the passage from strict convexity to the facet condition a kernel statement.**
- **No outcome revises any earlier verdict, edits any manuscript, changes any roadmap row or edits KINF-1's record.**

## Non-doings

This round does not do any of the following:
- define anything in the module beyond the frozen declarations;
- import into the module anything beyond the frozen imports;
- edit any closed round's record, any manuscript, any built artifact or `verification/ROADMAP.md`;
- change the workflow beyond the frozen edit that adds the probe's shard;
- freeze any self-duality, homogeneity, conjugacy, update or observation premise;
- start the sourcing questions — K∞-R, (SEC), (SF), copy naturality, full effects — or any reconstruction theorem.

## Evidence level

**2** for the kernel layer — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic replayed in CI, and the
written arguments are arguments on paper; each is named as its own layer wherever it is cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/reconstruction/round-kinf-2-foundations/controls.py`, blob **`{{CONTROLS_BLOB}}`**,
is written before `F` and added by the execution with exactly this blob. It imports nothing from the repository and
changes nothing; it reads `D` and the commit under check through `git`; it embeds every frozen text it compares
against.

`controls.py check <commit> [--freeze F]` fails unless all of the following hold:
- **the module**: the frozen header, no declaration beyond the frozen ones, no forbidden token or option, every
  theorem named in the frozen list or `kinf2_shared_…` with one `#print axioms` line, each frozen declaration byte
  for byte, and the verdict present exactly under `KINF-2-FOUNDATIONS-PROVED`;
- **the result note**: the outcome line once; the label's sentence once and no other label's; the clause after its
  mention; the probe's summary line; the reference blob and the module's blob at `E` in backticks, and, if they differ,
  the words *departure from the reference implementation*; none of the forbidden phrases outside the frozen texts;
- **the probe** has its frozen blob; **the workflow** is `D`'s with the frozen edit; **`OIBridge.lean`** is `D`'s with
  the frozen import line; **the census** is `D`'s with the frozen family appended;
- **the paths** changed from `D` are exactly the governed ones, KINF-1's record among the untouched; with
  `--freeze F`, `F` is `D` plus this file alone and this file is unchanged at the commit.

`controls.py --self-test` checks its constants against this file (the sentences, the clause, the header, every frozen
declaration, the workflow job, the census family, both blobs and the probe's line); builds a synthetic execution for
each of the two rows and requires both to hold; and applies {{NMUT}} mutation controls, each of which must fail with
its named code. Among them, each of KINF-1's defects reintroduced into the corrected definitions — syntactic
properness, the boundary read in `V`, (SEC) or (SF) without properness, drivability without the group law, with `J`
mapping into the body only, or with the off-axis clause compared on `V`, and K∞-1 without compactness — fails with
the code of the definition it changes. Run at `D` beside this file, it prints:

```text
{{SELFTEST}}
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear commits from `F`, each
with one parent:

1. **Stage 1 — the controls, the probe and the shard.** `controls.py` with its frozen blob; the probe with its frozen
   blob; the frozen workflow edit. No Lean changes.
2. **Stage 2 — the module without its verdict, and the census.** The reference implementation without
   `kinf2_kernel_core` and its `#print axioms` line; the import line; the census family.
3. **Stage 3 — the verdict.** `kinf2_kernel_core`, making the module the reference implementation; or, if it cannot
   be obtained, no verdict.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from the run at `E`'s
   predecessor and is confirmed by the run at `E`.

**Every attestation run is left to finish.** The dispatch runs whose `head_sha` is `F` and `E` run to completion, act
42's dispatch-only exclusion shards included; no job of either is cancelled, and each stands as exact-head evidence only
with every job, the aggregate `Numerical probes` job among them, concluded `success`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build fails is followed by
a fixing commit, never rewritten, and a fix may touch the proofs of theorems only.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one, deterministic, and green in its own shard with its pinned dependency | `C3`: the probe's blob at stage 1 and at `E`; `Numerical probes / KINF-2 foundations` green at every execution commit and at `E` with the probe's `OK` line; the aggregate `Numerical probes` job green |
| every frozen declaration elaborates and every frozen theorem is kernel-checked within the three axioms | `C8`: the dispatch run at `E`, run to completion with no job cancelled and every job concluded `success`; its `Mathlib bridge` build and the release gate's `lean-axioms` step |
| each premise holds and fails as Hazard 6 tabulates | `C8`, through the verdict `kinf2_kernel_core`, which conjoins the drivability and K∞-1 controls with the (SEC) and (SF) controls; `C9`, through the frozen statements |
| the module is classified and no manuscript changes | `C8`: the release gate at `E` — `lean-manuscript`, `staleness`, `voice`, `claims`, `mirror` — all green; `C7` |
| the frozen surfaces, the note and the paths | `C9`: `controls.py check E --freeze F` prints `controls: check OK` |
| the change stays inside the governed paths, KINF-1's record untouched | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen surfaces unchanged** is repaired by later linear commits before `E`,
  and reported in the result note as a departure from the reference implementation.
- **A verdict that cannot be obtained** is reported `KINF-2-UNDECIDED`, with the statement named.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target or any frozen
  surface: a frozen declaration that does not elaborate or is false as frozen; a frozen predicate found, after `F`,
  not to mean what this file says it means; the probe red at `E` with the frozen blob; a frozen surface that the
  release gate rejects. The round then halts under the specification's `S12`, with the result note naming the
  failure.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
