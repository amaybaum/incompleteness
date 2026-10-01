# Reconstruction round KINF-2 — the corrected field-neutral foundations of the pre-quantum completion: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Round KINF-2 fixes the corrected field-neutral vocabulary of the pre-quantum operational completion — finite stages, effects, proper effects and certain faces, boundary states read in the body, supporting-effect completeness and singleton faces over proper effects, relative strict convexity, full effects, perfect distinguishability, central symmetry, elementary drivability as a group flow of automorphisms of the body, and copy naturality — in place of the vocabulary of the halted round KINF-1, and proves the lemmas that vocabulary supports together with a holding and a failing instance of each premise. It states hypothesis K∞-1 as a definition over compact convex bodies and proves it for no physical family. It sources none of its premises: it does not derive drivability, supporting effects, singleton faces or copy naturality from any OI construction, it does not decide which effects the completion makes available, it does not prove in the kernel that corrected drivability excludes the square gbit or the rebit disk, it freezes no self-duality or homogeneity premise, and it contains no reconstruction theorem. It edits no manuscript and no roadmap row.

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
/-
  OIBridge/KInfFoundations.lean — round KINF-2: the field-neutral vocabulary of the pre-quantum
  operational completion, corrected, and the elementary lemmas that vocabulary supports.

  Nothing in this module mentions ℂ, a matrix carrier, or the substratum, except §F, which is a
  statement of the imported qubit kinematics. It fixes definitions over a real normed space `V`
  and proves small logical facts. It sources nothing: the module does not derive drivability,
  supporting effects, singleton faces or copy naturality from any OI construction, and it
  contains no reconstruction theorem.

  The corrections to the vocabulary of round KINF-1, which halted:
    * an effect is *proper* on `Ω` when some state gives it a value below one, tested on `Ω`;
      supporting-effect completeness and singleton faces quantify over proper effects only, so the
      unit effect may stay available and changes neither (§B′, `…_insert_iff`);
    * the boundary is read in `Ω` alone (`IsBoundaryState`), not in the topology of `V`, so a body
      that is not full-dimensional in `V` is not excluded for a reason of dimension; an open body
      has no boundary state, so K∞-1 is stated for compact convex bodies;
    * elementary drivability is a group flow of automorphisms of `Ω`, with `J` an automorphism of
      `Ω` and the off-axis clause compared on `Ω` (§C).

  Proved here.
    §A  the state body of a finite observer stage is compact and lies on the unit hyperplane;
    §B′ L1–L3: non-proper effects, and the boundary states certain effects pick out;
    §C′ the semantic controls for drivability: the unit ball of `ℝ³` is drivable (rotations about
        one axis, the half-turn, the cyclic permutation of the axes); the classical bit `[-1, 1]`
        and a one-point body are not;
    §D  Lemma C, `relStrictConvex_of_supporting_singleton`, and its converse,
        `singletonFaces_of_relStrictConvex`: given (SEC), singleton faces are equivalent to
        relative strict convexity of the body, each direction proved separately;
        `relStrictConvex_of_strictConvex`; Lemma D;
    §D′ the semantic controls for (SF) and (SEC): singleton faces hold on every closed ball of a
        strictly convex space with any effect family, and fail on the sup-norm square with its
        full effects; (SEC) holds on the segment `[-1, 1]` with its full effects and fails with
        the unit alone;
    §E  Lemma B and the finite-preparation bound; §E′ Theorem F2;
    §F  the qubit certain face, a theorem of the imported matrix kinematics;
    §G  `KInf1`, hypothesis K∞-1, stated as a definition; it holds for the ball with its full
        effects and fails for the ball with the unit effect alone, so it is a proposition about
        the effect family. It is proved for no physical family.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.Convex.Gauge
import Mathlib.Analysis.Convex.Strict
import Mathlib.Analysis.Convex.StrictConvexSpace
import Mathlib.Analysis.Convex.Topology
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Set.Card
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Trace
import OIBridge.CoherentExtension
```

**Definition budget: exactly the frozen definitions.** The module carries the structures and definitions frozen
below and no other; `controls.py` fails on any `def`, `abbrev`, `instance`, `structure`, `class` or `inductive` not in
the frozen list (`attribute [instance]` on the two `Fintype` fields of `FiniteStage` is not a declaration).

**The declarations, FROZEN** — each structure and definition whole, from its keyword to the blank line that ends it,
and each theorem's text from `theorem` to the `:=` that opens its proof, byte for byte, shown here with the proofs
elided:

```lean
structure FiniteStage where
  P : Type
  E : Type
  [fP : Fintype P]
  [fE : Fintype E]
  p : E → P → ℝ
  unit : E
  nonneg : ∀ e x, 0 ≤ p e x
  le_one : ∀ e x, p e x ≤ 1
  unit_eq : ∀ x, p unit x = 1

def vec (x : S.P) : S.E → ℝ := fun e => S.p e x

def states : Set (S.E → ℝ) := convexHull ℝ (Set.range S.vec)

theorem states_isCompact : IsCompact S.states := …

theorem states_isClosed : IsClosed S.states := …

theorem states_convex : Convex ℝ S.states := …

theorem states_unit : ∀ v ∈ S.states, v S.unit = 1 := …

def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=
  ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1

def certainFace (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Set V :=
  {x ∈ Ω | e x = 1}

def IsProperOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=
  ∃ y ∈ Ω, e y < 1

def IsBoundaryState (Ω : Set V) (x : V) : Prop :=
  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω

def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ x, IsBoundaryState Ω x → ∃ e ∈ avail, IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1

def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton

def RelStrictConvex (Ω : Set V) : Prop :=
  ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 →
    a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)

def fullEffects (Ω : Set V) : Set (V →ᵃ[ℝ] ℝ) :=
  {e | IsEffectOn Ω e}

def PerfectlyDistinguishable (Ω : Set V) {ι : Type} [Fintype ι]
    (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ) : Prop :=
  (∀ i, x i ∈ Ω) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ y ∈ Ω, ∑ i, e i y = 1) ∧
    (∀ i, e i (x i) = 1)

def CentrallySymmetric (Ω : Set V) (c : V) : Prop :=
  ∀ x ∈ Ω, c + (c - x) ∈ Ω

theorem affine_combo (e : V →ᵃ[ℝ] ℝ) (x y : V) (a b : ℝ) (hab : a + b = 1) :
    e (a • x + b • y) = a * e x + b * e y := …

theorem affine_reflect (e : V →ᵃ[ℝ] ℝ) (c x : V) :
    e (c + (c - x)) = 2 * e c - e x := …

theorem convex_affine_le (e : V →ᵃ[ℝ] ℝ) (m : ℝ) : Convex ℝ {y : V | e y ≤ m} := …

theorem extension_eq (x y : V) (ε : ℝ) : x + ε • (x - y) = (1 + ε) • x + (-ε) • y := …

theorem not_isProperOn_of_eq_one {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} (h : ∀ y ∈ Ω, e y = 1) :
    ¬ IsProperOn Ω e := …

theorem not_isProperOn_const_one (Ω : Set V) : ¬ IsProperOn Ω (AffineMap.const ℝ V (1 : ℝ)) := …

theorem eq_one_of_certain_of_not_boundary {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}
    (he : IsEffectOn Ω e) (hx : x ∈ Ω) (hnb : ¬ IsBoundaryState Ω x) (hone : e x = 1) :
    ∀ y ∈ Ω, e y = 1 := …

theorem isBoundaryState_of_certain_proper {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}
    (he : IsEffectOn Ω e) (hp : IsProperOn Ω e) (hx : x ∈ Ω) (hone : e x = 1) :
    IsBoundaryState Ω x := …

theorem supportingEffectComplete_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :
    SupportingEffectComplete Ω (insert u avail) ↔ SupportingEffectComplete Ω avail := …

theorem singletonFaces_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :
    SingletonFaces Ω (insert u avail) ↔ SingletonFaces Ω avail := …

structure ElementaryDrivability (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_zero : flow 0 = AffineEquiv.refl ℝ V
  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω
  t₀ : ℝ
  N_involutive : ∀ x ∈ Ω, flow t₀ (flow t₀ x) = x
  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω
  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x

def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V :=
  D.flow D.t₀

def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :=
  N_B = (e.symm.trans N_A).trans e

theorem copyNatural_refl_iff (N_A N_B : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B (AffineEquiv.refl ℝ V) ↔ N_B = N_A := …

theorem copyNatural_iff_apply (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B e ↔ ∀ x, N_B (e x) = e (N_A x) := …

def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}

theorem mem_ball3 (v : Fin 3 → ℝ) : v ∈ ball3 ↔ v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1 := …

theorem vec3_ext {v w : Fin 3 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2) :
    v = w := …

theorem ball3_convex : Convex ℝ ball3 := …

theorem ball3_isCompact : IsCompact ball3 := …

noncomputable def rotFun (t : ℝ) (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]

theorem rotFun_apply (t : ℝ) (v : Fin 3 → ℝ) :
    rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧
      rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2 := …

theorem rotFun_zero (v : Fin 3 → ℝ) : rotFun 0 v = v := …

theorem rotFun_add (s t : ℝ) (v : Fin 3 → ℝ) : rotFun s (rotFun t v) = rotFun (s + t) v := …

theorem rotFun_mem_ball3 (t : ℝ) {v : Fin 3 → ℝ} (hv : v ∈ ball3) : rotFun t v ∈ ball3 := …

noncomputable def rotLin (t : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun := rotFun t
  map_add' v w := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (v + w)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    obtain ⟨c0, c1, c2⟩ := rotFun_apply t w
    apply vec3_ext <;> simp only [Pi.add_apply, a0, a1, a2, b0, b1, b2, c0, c1, c2] <;> ring
  map_smul' r v := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (r • v)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    apply vec3_ext <;>
      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, b0, b1, b2] <;> ring

noncomputable def rotEquiv (t : ℝ) : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) :=
  { rotLin t with
    invFun := rotFun (-t)
    left_inv := fun v => by
      show rotFun (-t) (rotFun t v) = v
      rw [rotFun_add, neg_add_cancel, rotFun_zero]
    right_inv := fun v => by
      show rotFun t (rotFun (-t) v) = v
      rw [rotFun_add, add_neg_cancel, rotFun_zero] }

noncomputable def rot3 (t : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := (rotEquiv t).toAffineEquiv

theorem rot3_apply (t : ℝ) (v : Fin 3 → ℝ) : rot3 t v = rotFun t v := …

noncomputable def cycEquiv : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) where
  toFun v := ![v 2, v 0, v 1]
  invFun v := ![v 1, v 2, v 0]
  map_add' v w := by apply vec3_ext <;> rfl
  map_smul' r v := by apply vec3_ext <;> rfl
  left_inv v := by apply vec3_ext <;> rfl
  right_inv v := by apply vec3_ext <;> rfl

noncomputable def cyc3 : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cycEquiv.toAffineEquiv

theorem cyc3_apply (v : Fin 3 → ℝ) : cyc3 v 0 = v 2 ∧ cyc3 v 1 = v 0 ∧ cyc3 v 2 = v 1 := …

theorem cyc3_symm_apply (v : Fin 3 → ℝ) :
    cyc3.symm v 0 = v 1 ∧ cyc3.symm v 1 = v 2 ∧ cyc3.symm v 2 = v 0 := …

theorem cyc3_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3 v ∈ ball3 := …

theorem cyc3_symm_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3.symm v ∈ ball3 := …

noncomputable def ball3Drive : ElementaryDrivability ball3 where
  flow := rot3
  flow_zero := AffineEquiv.ext fun v => by rw [rot3_apply, rotFun_zero, AffineEquiv.refl_apply]
  flow_add s t := AffineEquiv.ext fun v => by
    simp only [AffineEquiv.trans_apply, rot3_apply, rotFun_add]
  flow_continuous := by
    refine continuous_pi fun i => ?_
    fin_cases i
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => q.2 2
      fun_prop
  flow_preserves t _ hv := rotFun_mem_ball3 t hv
  t₀ := Real.pi
  N_involutive x _ := by
    simp only [rot3_apply]
    obtain ⟨a0, a1, a2⟩ := rotFun_apply Real.pi (rotFun Real.pi x)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply Real.pi x
    apply vec3_ext
    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a2, b2]
  N_moves := ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => by
    have h0 : rot3 Real.pi ![1, 0, 0] 0 = (![1, 0, 0] : Fin 3 → ℝ) 0 := congrFun h 0
    change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0
    rw [Real.cos_pi, Real.sin_pi] at h0
    norm_num at h0⟩
  J := cyc3
  J_preserves _ hv := cyc3_mem_ball3 hv
  J_symm_preserves _ hv := cyc3_symm_mem_ball3 hv
  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1],
    by show (0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2 ≤ 1; norm_num, fun h => by
      have h2 : cyc3 (rot3 Real.pi (cyc3.symm ![0, 0, 1])) 2 = rot3 s ![0, 0, 1] 2 :=
        congrFun h 2
      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2
      rw [Real.sin_pi, Real.cos_pi] at h2
      norm_num at h2⟩⟩

theorem ball3_drivable : Nonempty (ElementaryDrivability ball3) := …

theorem affineEquiv_real_apply (g : ℝ ≃ᵃ[ℝ] ℝ) (x : ℝ) : g x = g 0 + g.linear 1 * x := …

theorem bit_aux {a b c d : ℝ} (h1 : -1 ≤ a + b * 1 ∧ a + b * 1 ≤ 1)
    (h2 : -1 ≤ a + b * -1 ∧ a + b * -1 ≤ 1) (h3 : -1 ≤ c + d * 1 ∧ c + d * 1 ≤ 1)
    (h4 : -1 ≤ c + d * -1 ∧ c + d * -1 ≤ 1) (h5 : a + b * (c + d * 0) = 0)
    (h6 : a + b * (c + d * 1) = 1) : a = 0 ∧ b * b = 1 := …

theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) := …

theorem not_drivable_singleton (x : V) : IsEmpty (ElementaryDrivability ({x} : Set V)) := …

theorem relStrictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hSEC : SupportingEffectComplete Ω avail)
    (hSF : SingletonFaces Ω avail) : RelStrictConvex Ω := …

theorem singletonFaces_of_relStrictConvex {Ω : Set V} (avail : Set (V →ᵃ[ℝ] ℝ))
    (h : RelStrictConvex Ω) : SingletonFaces Ω avail := …

theorem not_isBoundaryState_of_mem_interior {Ω : Set V} {z : V} (hint : z ∈ interior Ω) :
    ¬ IsBoundaryState Ω z := …

theorem relStrictConvex_of_strictConvex {Ω : Set V} (h : StrictConvex ℝ Ω) :
    RelStrictConvex Ω := …

theorem supportingEffectComplete_of_isOpen {Ω : Set V} (hΩ : IsOpen Ω)
    (avail : Set (V →ᵃ[ℝ] ℝ)) : SupportingEffectComplete Ω avail := …

theorem card_le_two_of_centrallySymmetric {Ω : Set V} {c : V} (hΩ : CentrallySymmetric Ω c)
    (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 := …

theorem card_le_two_of_centrallySymmetric_full {Ω : Set V} {c : V}
    (hΩ : CentrallySymmetric Ω c) (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V)
    (e : ι → V →ᵃ[ℝ] ℝ) (_ : ∀ i, e i ∈ fullEffects Ω)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 := …

theorem singletonFaces_closedBall [StrictConvexSpace ℝ V] (x : V) (r : ℝ)
    (avail : Set (V →ᵃ[ℝ] ℝ)) : SingletonFaces (Metric.closedBall x r) avail := …

noncomputable def affR (a b : ℝ) : ℝ →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ ℝ a + (b • LinearMap.id : ℝ →ₗ[ℝ] ℝ).toAffineMap

theorem affR_apply (a b t : ℝ) : affR a b t = a + b * t := …

theorem isBoundaryState_Icc_one : IsBoundaryState (Set.Icc (-1 : ℝ) 1) 1 := …

theorem not_supportingEffectComplete_unit :
    ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ (1 : ℝ)} := …

theorem supportingEffectComplete_Icc :
    SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) (fullEffects (Set.Icc (-1 : ℝ) 1)) := …

noncomputable def squareEdgeEffect : (Fin 2 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 2 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (LinearMap.proj 0 : (Fin 2 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem squareEdgeEffect_apply (v : Fin 2 → ℝ) : squareEdgeEffect v = 1 / 2 + v 0 / 2 := …

theorem not_singletonFaces_square :
    ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1)
      (fullEffects (Metric.closedBall (0 : Fin 2 → ℝ) 1)) := …

theorem not_relStrictConvex_square :
    ¬ RelStrictConvex (Metric.closedBall (0 : Fin 2 → ℝ) 1) := …

theorem eq_closedBall_of_frontier_subset_sphere {Ω : Set V} (hconv : Convex ℝ Ω)
    (hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)
    (hfr : frontier Ω ⊆ Metric.sphere (0 : V) 1) : Ω = Metric.closedBall (0 : V) 1 := …

theorem exists_vertex_of_certain {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)
    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)
    (hx : x ∈ convexHull ℝ (Set.range v)) (hone : e x = 1) : ∃ k, e (v k) = 1 := …

theorem exposed_mem_range {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)
    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)
    (hface : certainFace (convexHull ℝ (Set.range v)) e = {x}) : x ∈ Set.range v := …

def exposedPoints (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Set V :=
  {x | ∃ e ∈ avail, IsEffectOn Ω e ∧ certainFace Ω e = {x}}

theorem exposed_ncard_le {ι : Type} [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)) :
    (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι := …

theorem FiniteStage.exposed_le_card (S : FiniteStage)
    (avail : Set ((S.E → ℝ) →ᵃ[ℝ] ℝ)) :
    (exposedPoints S.states avail).ncard ≤ Fintype.card S.P := …

def simplex (N : ℕ) : Set (Fin N → ℝ) :=
  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1}

def ClassicallyExposed (Ω : Set (Fin N → ℝ)) (x : Fin N → ℝ) : Prop :=
  ∃ c : Fin N → ℝ, (∀ i, 0 ≤ c i ∧ c i ≤ 1) ∧ {p ∈ Ω | ∑ i, c i * p i = 1} = {x}

theorem response_eq_one_forces {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N) {c : Fin N → ℝ}
    (hc : ∀ i, 0 ≤ c i ∧ c i ≤ 1) {x : Fin N → ℝ} (hx : x ∈ Ω)
    (hone : ∑ i, c i * x i = 1) : ∀ i, 0 < x i → c i = 1 := …

theorem mem_of_classicallyExposed {Ω : Set (Fin N → ℝ)} {x : Fin N → ℝ}
    (hx : ClassicallyExposed Ω x) : x ∈ Ω := …

theorem exists_zero_of_classicallyExposed {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)
    (hnt : ¬ Ω.Subsingleton) {x : Fin N → ℝ} (hx : ClassicallyExposed Ω x) :
    ∃ i, x i = 0 := …

theorem classical_exposed_ncard_le {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)
    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :
    {x | ClassicallyExposed Ω x}.ncard ≤ N := …

theorem qubit_certain_face (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hρ : ρ.PosSemidef)
    (htr : ρ.trace = 1) (h00 : ρ 0 0 = 1) :
    ρ = Matrix.of fun i j => if i = 0 ∧ j = 0 then (1 : ℂ) else 0 := …

def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →
    SupportingEffectComplete Ω avail

theorem relStrictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hcomp : IsCompact Ω) (hconv : Convex ℝ Ω) (hK : KInf1 Ω avail)
    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :
    RelStrictConvex Ω := …

noncomputable def ballEffect (u : Fin 3 → ℝ) : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 3 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (u 0 • LinearMap.proj 0 + u 1 • LinearMap.proj 1 + u 2 • LinearMap.proj 2 :
      (Fin 3 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem ballEffect_apply (u v : Fin 3 → ℝ) :
    ballEffect u v = 1 / 2 + (u 0 * v 0 + u 1 * v 1 + u 2 * v 2) / 2 := …

theorem ball3_extend {x0 x1 x2 y0 y1 y2 ε : ℝ} (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 ≤ 1)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 ≤ 1) (hε : 0 < ε)
    (hε' : 16 * ε = 1 - (x0 ^ 2 + x1 ^ 2 + x2 ^ 2)) :
    (x0 + ε * (x0 - y0)) ^ 2 + (x1 + ε * (x1 - y1)) ^ 2 + (x2 + ε * (x2 - y2)) ^ 2 ≤ 1 := …

theorem supportingEffectComplete_ball3 : SupportingEffectComplete ball3 (fullEffects ball3) := …

theorem kInf1_ball3_full : KInf1 ball3 (fullEffects ball3) := …

theorem isBoundaryState_ball3 : IsBoundaryState ball3 ![1, 0, 0] := …

theorem not_kInf1_ball3_unit : ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} := …

theorem kinf2_kernel_core :
    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), Convex ℝ Ω →
      SupportingEffectComplete Ω avail → SingletonFaces Ω avail → RelStrictConvex Ω) ∧
    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), RelStrictConvex Ω → SingletonFaces Ω avail) ∧
    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) (u : V →ᵃ[ℝ] ℝ), ¬ IsProperOn Ω u →
      (SupportingEffectComplete Ω (insert u avail) ↔ SupportingEffectComplete Ω avail) ∧
      (SingletonFaces Ω (insert u avail) ↔ SingletonFaces Ω avail)) ∧
    SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) (fullEffects (Set.Icc (-1 : ℝ) 1)) ∧
    ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ (1 : ℝ)} ∧
    ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1)
      (fullEffects (Metric.closedBall (0 : Fin 2 → ℝ) 1)) ∧
    Nonempty (ElementaryDrivability ball3) ∧
    IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) ∧
    KInf1 ball3 (fullEffects ball3) ∧
    ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} ∧
    (∀ (Ω : Set V) (c : V), CentrallySymmetric Ω c → c ∈ Ω →
      ∀ (ι : Type) [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ),
        PerfectlyDistinguishable Ω x e → Fintype.card ι ≤ 2) ∧
    (∀ Ω : Set V, Convex ℝ Ω → IsCompact Ω → (0 : V) ∈ interior Ω →
      frontier Ω ⊆ Metric.sphere (0 : V) 1 → Ω = Metric.closedBall (0 : V) 1) ∧
    (∀ (ι : Type) [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)),
      (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι) ∧
    (∀ (N : ℕ) (Ω : Set (Fin N → ℝ)), Ω ⊆ simplex N →
      (∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) → {x | ClassicallyExposed Ω x}.ncard ≤ N) := …
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

**Not frozen: the proofs of the theorems.** The reference implementation is blob **`3b8290838f1ee7006996db53a2f1d1a228249a08`**. A proof-only
repair — a change that leaves every frozen surface unchanged — is permitted as a later linear commit before `E`; the
result note names the reference blob and the module's blob at `E`, and, if they differ, states the departure from
the reference implementation and justifies it, which `controls.py` checks. A definition or structure that must
change is a freeze failure (Hazard 5).

### Pre-freeze evidence — design evidence, not attestation

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, on a disposable branch, never landed. None
is a `check-run` attestation, and no predicate of the round reads them. Each was left to finish; the table records,
job by job, what finished and how.

| run | head | what the head carries | the jobs that finished |
| --- | --- | --- | --- |
| 36832326177 | `70d14ad9` on `claude/kinf2-dev` | the first draft of the corrected module; a placeholder census family | **overall conclusion `failure`**. `Mathlib bridge` (job 110271549259) failed at `Build`: `fullEffects _` left a placeholder the elaborator could not fill, at two sites; `squareEdgeEffect` and `affR` lacked `noncomputable`; four `#print axioms` lines lacked the `FiniteStage.` prefix. Every other theorem reported axioms within `[propext, Classical.choice, Quot.sound]`. Failed design run; the next head is its repair |
| 36832691716 | `293e12c3` on `claude/kinf2-dev` | the repaired draft | **overall conclusion `failure`**. `Mathlib bridge` (job 110272707373) failed at `Build` in one proof, `supportingEffectComplete_Icc`, whose anonymous constructor omitted the membership component, so it and the verdict reported `sorryAx`; every other theorem reported axioms within `[propext, Classical.choice, Quot.sound]`. Failed design run; the next head is its repair, with the drivability and K∞-1 controls added |
| (iteration 3 row pending) | | | |

***

## The exact-computation layer — the frozen probe

`verification/lean/kinf2_foundations_probe.py`, blob **`3634e3d3b86405f90f7eecc7674d45442b235e7e`**, is written before `F` and added by the
execution at stage 1 with exactly this blob, and the workflow runs it in its own shard at every execution commit from
stage 1 on. It uses Python integers and `Fraction`s, pairs `a + b√3` and `a + b√5` of them, and `sympy` polynomial
and rational-function identities, for every value it asserts: **no floating point and no randomness.** Every point at
which an identity is tested is fixed in the file, so two runs print the same bytes. It exits 1 on any mismatch. Each
check is tagged `witness`, `identity`, `enumerate` or `sample`; a `sample` check is evidence for the universal claim it
instantiates, not a proof of it, and the written notes it prints are not checks. Its statements are exact arithmetic
replayed; they are not kernel-certified, and the result note names them as this layer's. Its twelve sections are the
instances tabulated above under *What the exact layer instantiates*.

It ends with the line `kinf2_foundations_probe: OK -- 192 checks` on success, which the result note carries verbatim, and
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

> In the kernel, at evidence level 2, over a real normed space and with no field, matrix carrier or substratum object, for the corrected vocabulary in which an effect is proper when some state gives it a value below one and a boundary state is read in the body alone: a non-proper effect, the unit among them, changes neither supporting-effect completeness nor singleton faces (`supportingEffectComplete_insert_iff`, `singletonFaces_insert_iff`); a convex body with supporting-effect completeness and singleton faces is relatively strictly convex (Lemma C, `relStrictConvex_of_supporting_singleton`), and a relatively strictly convex body has singleton faces for every effect family (`singletonFaces_of_relStrictConvex`), the two directions proved separately; each premise holds and fails on named bodies — singleton faces on every closed ball of a strictly convex space and not on the sup-norm square with its full effects, supporting-effect completeness on the segment `[-1, 1]` with its full effects and not with the unit alone, elementary drivability on the unit ball of `ℝ³` and not on the classical bit, and hypothesis K∞-1 for that ball with its full effects and not with the unit alone (`kInf1_ball3_full`, `not_kInf1_ball3_unit`); a centrally symmetric body admits at most two perfectly distinguishable states with any effects (Lemma D); a compact convex body with `0` in its interior whose frontier lies on the unit sphere is the closed unit ball (Lemma B); a finite stage exposes at most as many states as it has preparations, and a body on `N` ontic states meeting each coordinate facet in at most one point exposes at most `N` states by response effects (Theorem F2); joined in the verdict `kinf2_kernel_core`. The qubit certain face is a theorem of the imported matrix kinematics (`qubit_certain_face`), and hypothesis K∞-1 is the definition `KInf1`, proved for no physical family. In exact arithmetic replayed in CI, and not in the kernel, the round's probe instantiates the controls: the square gbit, the torus and Stiefel orbitopes and the regular pentagon violate singleton faces, the pentagon while strongly self-dual, transitive on ordered frames and of capacity two; the 3-ball satisfies every premise together; the SIC ball fails supporting-effect completeness with its response effects; the Carathéodory orbitope `C₂` has capacity three. Nothing here derives drivability, supporting effects, singleton faces or copy naturality from any OI construction; that corrected drivability excludes the square gbit and the rebit disk is a written argument and not a kernel statement; and nothing here is a reconstruction theorem.

### `KINF-2-UNDECIDED`

> The kernel verdict `kinf2_kernel_core` was not obtained. The statement at which the proof stopped is named, with what would settle it; the definitions stand as frozen, the exact layer stands as computed, and no lemma is stated as a result of this round beyond those the kernel checked.

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
the corrected field-neutral vocabulary of the pre-quantum completion — proper effects, boundary states read in the body, relative strict convexity, group-flow drivability — with Lemma C and its converse, the semantic controls, Lemmas B and D and the finite-exposure bounds (round KINF-2, reconstruction)
```

with the note

```text
Round KINF-2, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-kinf-2-foundations/preregistration.md, which records what it replaces in the halted round KINF-1. The kernel layer: given supporting-effect completeness, singleton faces are equivalent to relative strict convexity, each direction proved separately (relStrictConvex_of_supporting_singleton, singletonFaces_of_relStrictConvex); a non-proper effect changes neither premise; the semantic controls show each premise holding and failing on named bodies, drivability holding on the unit ball of R^3 and failing on the classical bit, and K∞-1 holding for the ball with its full effects and failing with the unit alone. Carried by no manuscript. The round sources none of its premises: drivability, supporting effects, singleton faces and copy naturality are discharged by no OI construction, and K∞-1 is proved for no physical family. That corrected drivability excludes the square gbit and the rebit disk is a written argument, not a kernel statement.
```

## The workflow edit, FROZEN

After the NB-1 shard, the job

```yaml
  probes_kinf2:
    name: Numerical probes / KINF-2 foundations
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install the exact-algebra dependency
        run: pip install sympy==1.14.0

      - name: KINF-2 foundations probe
        working-directory: verification/lean
        run: |
          echo "=== kinf2_foundations_probe.py ==="
          python3 kinf2_foundations_probe.py
```

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

`verification/programmes/oi-qm/reconstruction/round-kinf-2-foundations/controls.py`, blob **`e0f6bb3c0106bef39697749fa3b5b4661b848b68`**,
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
each of the two rows and requires both to hold; and applies N mutation controls, each of which must fail with
its named code. Among them, each of KINF-1's defects reintroduced into the corrected definitions — syntactic
properness, the boundary read in `V`, (SEC) or (SF) without properness, drivability without the group law, with `J`
mapping into the body only, or with the off-axis clause compared on `V`, and K∞-1 without compactness — fails with
the code of the definition it changes. Run at `D` beside this file, it prints:

```text
controls: (pending)
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
