# Reconstruction round KINF-1 — the field-neutral foundations of the pre-quantum completion: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Round KINF-1 fixes the field-neutral vocabulary of the pre-quantum operational completion — finite stages, effects and certain faces, supporting-effect completeness, singleton faces, full effects, perfect distinguishability, central symmetry, elementary drivability and copy naturality — and proves the elementary lemmas that vocabulary supports: Lemmas B, C and D, the finite-exposure bounds, and the qubit certain face as a theorem of the imported matrix kinematics. It states hypothesis K∞-1 as a definition and proves it for nothing. It sources none of its premises: it does not derive drivability, supporting effects, singleton faces or copy naturality from any OI construction, it does not decide whether the completion's effects are the full effects, and it contains no reconstruction theorem. It edits no manuscript and no roadmap row.

## The declarations

```v3-round
round KINF-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/
record AM verification/receipts/KINF-1.json
execution A verification/lean-mathlib/OIBridge/KInfFoundations.lean
execution A verification/lean/kinf_foundations_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/KINF-1.json`. Every other path the round changes is an
execution path listed above. The paths are the same under both outcomes. **No manuscript, no built artifact and
`verification/ROADMAP.md` change under either outcome.**

The workflow changes by one frozen edit in five places: the round's probe runs in a shard of its own, `probes_kinf1`,
`Numerical probes / KINF-1 foundations`, inserted after the NB-1 shard, and the aggregate `Numerical probes` job lists
it in its `needs`, reads its result into its environment, echoes it and tests it for `success`. `controls.py` checks
that the workflow at `E` is `D`'s with exactly that edit.

## The objects

- **`D`** = `98f5f08bad2d02aba00b9cfce51538c5e890cc18`: the head of `main` after round NB-1's landing, receipt
  `verification/receipts/NB-1.json`; its parents are `fdebc6e3` and `0580cdf8`. It is certified by push run
  36754815367, overall conclusion `success`: every job succeeded (the act 42 exclusion matrix skipped on a push event,
  as the workflow requires), the release gate passing 21 of 21 steps with twenty receipts holding and the 303 legacy
  records intact, `lean-axioms` at 5288 named results and no sorry. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only `verification/receipts/KINF-1.json`.

No other round runs beside KINF-1 at this freeze. Should one land first, its movement of `main` enters KINF-1 only by
reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — vocabulary is not sourcing.** The module defines the objects of the pre-quantum operational completion
over an arbitrary real normed space and proves the elementary lemmas those definitions support. It does not derive
any of them from the substratum, from the finite operational characterization, or from any OI construction: no
theorem of this round has a premise of the form *the completion has property P* discharged by a corpus declaration.
The premises that the read-only K∞ audit at `D` left open — field-neutral drivability (K∞-R), sharp supporting
effects (K∞-E, derived from drivability only at the matrix level, by `genTheory_qm_of_quantumArchitecture`),
singleton faces (SF) and copy naturality — stay open, and this round names them as definitions so that later rounds
can state what discharges them. **No outcome says that OI supplies, derives or sources any of them.**

**Hazard 2 — one theorem is imported kinematics.** `qubit_certain_face` is a statement about complex `2 × 2`
matrices: a density matrix certain for the effect `ρ ↦ ρ 0 0` is `|0⟩⟨0|`. It shows that singleton faces hold for one
rank-one effect of the qubit, in the kinematics the finite characterization *assumes*; it is not a field-neutral
result and it does not source (SF). It is the only theorem of the module that consumes a corpus declaration
(`OIBridge.CoherentExtension.psd_diag_zero_entry_zero`), and the only one that mentions `ℂ`.

**Hazard 3 — K∞-1 is a definition.** `KInf1 Ω avail` is the proposition *a body admitting an elementary drive has
supporting-effect completeness relative to `avail`*. The module proves it for no `Ω` and no `avail`.
`strictConvex_of_kInf1` records only what the hypothesis buys together with singleton faces; it is Lemma C with the
hypothesis in place of its premise. **No outcome says that K∞-1 holds**, for any body, and nothing in the module is a
reconstruction theorem.

**Hazard 4 — three layers, never merged.** The round certifies its content in three layers that do not substitute for
one another (`AGENTS.md`, *Keep verification layers distinct*):

| layer | what it carries | where |
| --- | --- | --- |
| **kernel** (evidence level 2) | the definitions; `states_isCompact`, `states_unit`; Lemma C; Lemma D and its full-effects corollary; Lemma B; `exposed_mem_range`, `exposed_ncard_le`; Theorem F2 with `response_eq_one_forces` and `exists_zero_of_classicallyExposed`; `copyNatural_iff_apply`; `qubit_certain_face`; the verdict `kinf1_kernel_core` | `KInfFoundations.lean` |
| **exact computation**, replayed in CI | the SIC-embedded ball on four ontic states: interior states with every coordinate positive, the four tangency points each on exactly one facet and exposed by the response effect `1 − pᵢ`, the facet identity `|r + aᵢ|² = 2 + 2 aᵢ·r`; the Carathéodory capacity-three triple, exact in `ℚ(√3)`; the torus and Stiefel flat faces with central symmetry; the 3-ball's singleton faces | `kinf_foundations_probe.py` |
| **written remark** | that a body strictly convex relative to its affine span meets each coordinate facet in at most one point (the hypothesis of Theorem F2 as stated in the kernel); that the exact instances are what the lemmas say they are | this file, *The mathematics* |

Theorem F2 in the kernel takes the facet condition as a hypothesis; the passage from strict convexity to that
condition is a written remark and not a kernel statement, and nothing in the result note, the census or the module
says otherwise.

**Hazard 5 — definitions are frozen whole.** Unlike a theorem, a definition has no proof to repair: its text *is* its
content. Every `structure` and `def` of the module is frozen byte for byte, and `controls.py` compares each at `E`.
A definition that cannot be kept as frozen — one that does not elaborate, or that a theorem cannot be proved about as
frozen — is a **freeze failure**, not a repair, and the round halts under the specification's `S12`.

**Hazard 6 — manuscripts.** None. The census family is `kernel-only` with no anchor, under both outcomes. The K
roadmap row and the `Main.md` remark on the four-state model are later changes with their own review, not part of
this round.

**Hazard 7 — history.** Round NB-1 and every earlier round stand as recorded. The K∞ research notes behind this
round, from `D`, are design evidence only; none is a record of this round.

***

## Provenance

The module imports Mathlib and one corpus module:

- `Mathlib.Analysis.Convex.Gauge`, `Mathlib.Analysis.Convex.Strict`, `Mathlib.Analysis.Convex.Topology`,
  `Mathlib.Analysis.Normed.Module.Basic`, `Mathlib.Data.Set.Card`, `Mathlib.LinearAlgebra.Matrix.PosDef`,
  `Mathlib.LinearAlgebra.Matrix.Trace`; among the lemmas used, `Set.Finite.isCompact_convexHull`, `convexHull_min`,
  `subset_convexHull`, `convexHull_empty`, `AffineMap.lineMap_apply_module`, `AffineMap.apply_lineMap`,
  `AffineMap.map_vadd`, `AffineMap.linearMap_vsub`, `AffineEquiv.trans_apply`, `AffineEquiv.symm_apply_apply`,
  `AffineEquiv.apply_symm_apply`, `Finset.sum_le_sum`, `Finset.sum_lt_sum`, `Finset.sup'_lt_iff`, `Finset.le_sup'`,
  `mem_interior_iff_mem_nhds`, `absorbent_nhds_zero`, `gauge_smul_of_nonneg`, `gauge_eq_one_iff_mem_frontier`,
  `gauge_le_one_iff_mem_closure`, `gauge_le_one_of_mem`, `le_gauge_of_subset_closedBall`,
  `Metric.isBounded_iff_subset_closedBall`, `Metric.closedBall_subset_closedBall`, `mem_sphere_zero_iff_norm`,
  `norm_smul`, `norm_inv`, `Set.ncard_le_ncard`, `Set.ncard_image_le`, `Set.ncard_univ`,
  `Set.ncard_le_ncard_of_injOn`, `Set.ncard_le_one`, `Matrix.trace_fin_two`, and the tactics `simp`, `rw`, `ring`,
  `linarith`, `nlinarith`, `linear_combination`, `ext`, `subst`, `fin_cases`, `by_contra`, `calc`.
- `OIBridge.CoherentExtension`, for `psd_diag_zero_entry_zero` alone, consumed by `qubit_certain_face` alone.

The probe imports nothing but the Python standard library (`sys`, `fractions`).

## Locating controls — at `D`

The sources this round's hazards cite:

| what | where | line |
| --- | --- | --- |
| `psd_diag_zero_entry_zero` | `verification/lean-mathlib/OIBridge/CoherentExtension.lean` | 183 |
| `DrivesElementary`, the matrix-level drivability premise | `verification/lean-mathlib/OIBridge/SubstratumSource.lean` | 77 |
| `genTheory_elementary`, `genTheory_qm_of_quantumArchitecture` (matrix K∞-R ⇒ matrix K∞-E) | `verification/lean-mathlib/OIBridge/SubstratumSource.lean` | 109, 136 |
| `inclObs`, the region inclusion `X ↦ X ⊗ 1` | `verification/lean-mathlib/OIBridge/RegionLimit.lean` | 102 |
| the four-state model with the ball's geometry and restricted effects | `papers/Main.md` | 540 |

| file at `D` | blob |
| --- | --- |
| `CoherentExtension.lean` | `81c71c78614d64f82839799ec7f87738ad9a0be5` |
| `SubstratumSource.lean` | `4d053fe6c2d8c1d9ee96a8dcfaff721493c21269` |
| `RegionLimit.lean` | `1edf1ccaf0ae8916d3afe604aaece7c033570ca6` |
| `papers/Main.md` | `536e5f59c958cf1ea9790f89a592a2a448e5993d` |
| `verification/lean-mathlib/OIBridge.lean` | `5143e4bc6320773d0e1b5578fc267ea4cb5960cd` |
| `verification/lean-manuscript-census.json` | `242443c63a4a0183e8495fd2b86b39b222b54002` |
| `.github/workflows/verify.yml` | `df249b7c9c3ca8f3fd7a07ffdcdc5a28c176036d` |

The names this round introduces return nothing from `git grep -l` at `D`: `KInfFoundations`, `kinf_foundations`,
`kinf1_`, `KINF-1`, `round-kinf-1`, `ClassicallyExposed` and `SupportingEffectComplete`.

***

## Why this round exists

The finite operational characterization is stated over complex matrix carriers, so the quantum kinematics sits in
its premises. The K programme tracks the obligation to reach that kinematics from field-free principles, and the
read-only K∞ audit at `D` found that the corpus has no object for a state space as a convex set, no effect object,
and no statement of the completion's premises in a form a later round could discharge. The audit also found the
small logical facts that the programme keeps re-deriving in prose: that supporting effects with singleton certain
faces force strict convexity; that central symmetry alone bounds the capacity by two, so capacity is not a
state-geometric premise; that a strictly convex body with a transitive symmetry group is a ball once its frontier
lies on a sphere; and that a finite classical realization exposes at most as many states as it has ontic states,
attained by the four-state model. This round puts the vocabulary and those lemmas into the kernel, so that the open
premises can be named in a fixed idiom and the lemmas cited by identifier. It is deliberately modest: it formalizes
the vocabulary and the small lemmas, and it does not claim to source quantum theory.

***

## The mathematics — FROZEN

**Setting.** `V` is a real normed space. A **body** is a subset `Ω ⊆ V`; the lemmas add convexity, closedness or
compactness as they need them. An **effect** on `Ω` is an affine functional `e : V →ᵃ[ℝ] ℝ` with `0 ≤ e ≤ 1` on `Ω`;
its **certain face** is `{x ∈ Ω | e x = 1}`. A family `avail` of affine functionals is the round's stand-in for *the
effects the completion makes available*; the **full effects** are every affine functional that is an effect on `Ω`.

**The definitions.**

| name | statement |
| --- | --- |
| `FiniteStage` | finitely many preparations `P` and effects `E`, a table `p e x ∈ [0, 1]`, and a unit effect certain on every preparation |
| `FiniteStage.vec`, `FiniteStage.states` | the probability vector of a preparation, and the convex hull of the preparation vectors |
| `IsEffectOn Ω e`, `certainFace Ω e` | as above |
| `SupportingEffectComplete Ω avail` (SEC) | every frontier point of `Ω` is certain for some available effect |
| `SingletonFaces Ω avail` (SF) | every available effect is certain on at most one state |
| `fullEffects Ω` | every affine functional that is an effect on `Ω` |
| `PerfectlyDistinguishable Ω x e` | states `x i ∈ Ω` and effects `e i` on `Ω` with `∑ i, e i = 1` on `Ω` and `e i (x i) = 1` |
| `CentrallySymmetric Ω c` | `x ∈ Ω → c + (c − x) ∈ Ω` |
| `ElementaryDrivability Ω` | a continuous family `flow : ℝ → V ≃ᵃ[ℝ] V` of affine automorphisms preserving `Ω`, the identity at `0`; a parameter `t₀` at which the flow is an involution moving some state (the NOT `N`); a reversible `J` preserving `Ω` with `J ∘ flow t ∘ J⁻¹` off the flow for some `t` |
| `CopyNatural N_A N_B e` | `N_B = e ∘ N_A ∘ e⁻¹` |
| `exposedPoints Ω avail` | the states exposed by some available effect with a singleton certain face |
| `simplex N`, `ClassicallyExposed Ω x` | the probability simplex on `Fin N`; `x` exposed by a response effect `p ↦ ∑ cᵢ pᵢ`, `cᵢ ∈ [0, 1]` |
| `KInf1 Ω avail` | `Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail` |

**The lemmas, each with its proof.**

- **`states_isCompact`, `states_convex`, `states_isClosed`, `states_unit`** *(kernel)*. The convex hull of a finite set
  is compact; the unit hyperplane is convex and contains every preparation vector, so it contains the hull.
- **Lemma C, `strictConvex_of_supporting_singleton`** *(kernel)*. `Ω` convex and closed with (SEC) and (SF). For
  `x ≠ y` in `Ω` and `a, b > 0`, `a + b = 1`, suppose `z = a•x + b•y` is not interior. It is in `Ω`, hence in the
  frontier, so an available effect `e` has `e z = 1`. Affinity gives `a·e x + b·e y = 1` with `e x, e y ≤ 1`, forcing
  `e x = e y = 1`; (SF) then gives `x = y`.
- **Lemma D, `card_le_two_of_centrallySymmetric`** *(kernel)*. `Ω` centrally symmetric about `c ∈ Ω`, and `x`, `e`
  perfectly distinguishable over `ι`. For each `i`, the reflection `c + (c − x i)` lies in `Ω`, and
  `e i (c + (c − x i)) = 2·e i c − e i (x i) = 2·e i c − 1 ≥ 0`, so `e i c ≥ 1/2`. Summing, `1 = ∑ e i c ≥ |ι|/2`.
  The corollary `card_le_two_of_centrallySymmetric_full` is the same statement with the effects drawn from
  `fullEffects Ω`: the bound does not depend on which effects are available.
- **Lemma B, `eq_closedBall_of_frontier_subset_sphere`** *(kernel)*. `Ω` convex and compact with `0` interior and
  `frontier Ω ⊆ sphere 0 1`. `Ω` is a neighbourhood of `0`, hence absorbent, and bounded, so its gauge `g` is
  positive off `0`. For `x ≠ 0`, `g((g x)⁻¹•x) = 1`, so that point is in the frontier and has norm `1`; hence
  `‖x‖ = g x`. Then `x ∈ Ω` gives `g x ≤ 1`, and `‖x‖ ≤ 1` gives `g x ≤ 1`, hence `x ∈ closure Ω = Ω`.
- **`exposed_mem_range`, `exposed_ncard_le`** *(kernel)*. On the hull of `range v`, an effect `e ≤ 1` certain at
  `x` is certain at some `v k`: otherwise `e < m < 1` on every `v k` for `m` the finite maximum, and the sublevel
  set `{e ≤ m}` is convex and contains the hull. If the certain face is `{x}`, then `x = v k`. So the exposed points
  lie in `range v`, and their number is at most `|ι|`.
- **Theorem F2, `classical_exposed_ncard_le`** *(kernel, with the facet condition as a hypothesis)*. `Ω ⊆ simplex N`,
  and `Ω ∩ {p | p i = 0}` has at most one point for each `i`. *`response_eq_one_forces`*: if `∑ cᵢ xᵢ = 1` with
  `x` in the simplex and `cᵢ ≤ 1`, then `cᵢ = 1` wherever `xᵢ > 0`, since otherwise `∑ cᵢ xᵢ < ∑ xᵢ = 1`.
  *`exists_zero_of_classicallyExposed`*: if `Ω` has two points and `x` is exposed by `c`, some `xᵢ = 0`; otherwise
  `c = 1`, the effect is the unit, its certain face is `Ω`, and `Ω = {x}`. *The count*: if `Ω` is a singleton the
  exposed set has at most one point and `N ≥ 1` when it is nonempty; otherwise each exposed `x` is sent to a zero
  coordinate `f x`, and two exposed points with the same `f` lie in one facet, hence coincide, so the exposed set
  injects into `Fin N`.
- **Written remark, not a kernel statement.** A body strictly convex relative to its affine span meets each
  coordinate facet in at most one point: the facet is the intersection of `Ω` with a supporting hyperplane (`pᵢ ≥ 0`
  on `Ω`), hence a face, and a strictly convex body has no face of positive dimension. The kernel states Theorem F2
  with the facet condition as its hypothesis and does not derive it from strict convexity.
- **`copyNatural_iff_apply`, `copyNatural_refl_iff`** *(kernel)*. `CopyNatural N_A N_B e` is the pointwise identity
  `N_B (e x) = e (N_A x)`; under the identity identification it is `N_B = N_A`.
- **`qubit_certain_face`** *(kernel; imported kinematics)*. `ρ` positive semidefinite with trace `1` and `ρ 0 0 = 1`
  has `ρ 1 1 = 0`, so its off-diagonal entries vanish (`psd_diag_zero_entry_zero`), and `ρ = |0⟩⟨0|`.
- **`strictConvex_of_kInf1`** *(kernel)*. Lemma C with `KInf1 Ω avail` and a drive in place of (SEC).

**What the exact layer instantiates** (the probe; not the kernel):

| instance | what is checked exactly | what it shows |
| --- | --- | --- |
| the SIC-embedded ball, `N = 4` | twelve rational sphere points have every `pᵢ > 0`; the four tangency points `r = −aᵢ` have exactly one `pᵢ = 0` and `pⱼ = 1/3` otherwise; the response effect `1 − pᵢ` is certain there and `< 1` at every other sample; `|r + aᵢ|² = 2 + 2 aᵢ·r` on the sphere; `p(r)` in the simplex | Theorem F2's bound is attained, on a body with a continuum of extreme points, and the facet condition holds by the identity |
| the Carathéodory orbitope `C₂` | the three effects `eᵢ = (4/9)(1 − cos(t − tⱼ))(1 − cos(t − tₖ))`, `t ∈ {0, 2π/3, 4π/3}`, as affine functionals in `ℚ(√3)`: they sum to the unit, satisfy `eᵢ(x(tⱼ)) = δᵢⱼ`, and agree with the product form, hence are nonnegative, on twelve rational circle points | a body that is not centrally symmetric can have capacity three: Lemma D's hypothesis is load-bearing |
| the torus orbitope `conv(S¹ × S¹)` | `e = (1 + x₀)/2` is valid on sixty generators and certain on two distinct generators and on their midpoint, which is not a generator; `u ↦ −1/u` negates rational circle points | singleton faces fail with full effects while Lemma D bounds the capacity by two |
| the Stiefel orbitope `conv V₂(ℝ³)` | `e(A) = (1 + A₁₁)/2` is valid on thirty-three exact rational frames and certain on two distinct frames and their midpoint, which is not a frame; `−A` is a frame | the same, for a non-abelian transitive group |
| the 3-ball | `(1 + n·x)/2 = 1` exactly at `x = n` on twelve rational sphere points, by `|x − n|² = 2 − 2 n·x` | singleton faces hold: the control distinguishes the ball from the orbitopes |

***

## The frozen Lean text

The module is `verification/lean-mathlib/OIBridge/KInfFoundations.lean`. Its header, up to `namespace OIBridge`, is
frozen byte for byte:

```lean
/-
  OIBridge/KInfFoundations.lean — round KINF-1: the field-neutral vocabulary of the pre-quantum
  operational completion, and the elementary lemmas that vocabulary supports.

  Nothing in this module mentions ℂ, a matrix carrier, or the substratum. It fixes definitions
  over a real normed space `V` and proves the small logical facts that later rounds cite. It
  sources nothing: the module does not derive drivability, supporting effects, singleton faces
  or copy naturality from any OI construction, and it contains no reconstruction theorem.

  Defined here.
    §A  a finite observer stage: finitely many preparations and effects and a probability table
        with a unit effect; its state body is the convex hull of the preparation vectors.
    §B  effects on a convex body, the certain face of an effect, supporting-effect completeness
        (SEC), singleton faces (SF), full effects, perfect distinguishability, central symmetry.
    §C  elementary drivability: a continuous one-parameter family of affine automorphisms of
        the body, starting at the identity, with a distinguished member `N` and a reversible
        `J` that does not normalize the flow; and copy naturality of two NOTs under a copy
        identification.
    §G  `KInf1`, the statement of hypothesis K∞-1 as a proposition about a body and a family of
        available effects. It is a definition and is proved for nothing here.

  Proved here.
    §A  `states_isCompact`, `states_unit`: the state body of a finite stage is compact and lies
        on the unit hyperplane.
    §D  Lemma C, `strictConvex_of_supporting_singleton`: a closed convex body with (SEC) and (SF)
        is strictly convex.
    §D  Lemma D, `card_le_two_of_centrallySymmetric`: a centrally symmetric body admits at most
        two perfectly distinguishable states, whatever effects are available.
    §E  Lemma B, `eq_closedBall_of_frontier_subset_sphere`: a compact convex body with `0` in
        its interior whose frontier lies on the unit sphere is the closed unit ball.
    §E  the finite-preparation bound, `exposed_mem_range` and `exposed_ncard_le`: every point of
        a finite stage's body exposed by an effect with a singleton certain face is the vector
        of one of its preparations, so at most `|P|` points are exposed.
    §E′ Theorem F2, `classical_exposed_ncard_le`: a body realized on `N` ontic states, meeting
        each coordinate facet in at most one point, has at most `N` points exposed by response
        effects; `response_eq_one_forces` is the step that puts every exposed point on a facet.
    §F  `qubit_certain_face`: for the imported qubit kinematics, the certain face of the effect
        `ρ ↦ ρ 0 0` on density matrices is the single point `|0⟩⟨0|`. This is a theorem of matrix
        kinematics, stated as such.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.Convex.Gauge
import Mathlib.Analysis.Convex.Strict
import Mathlib.Analysis.Convex.Topology
import Mathlib.Analysis.Normed.Module.Basic
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

def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x = 1

def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, IsEffectOn Ω e → (certainFace Ω e).Subsingleton

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

structure ElementaryDrivability (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_zero : flow 0 = AffineEquiv.refl ℝ V
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω
  t₀ : ℝ
  N_involutive : ∀ x, flow t₀ (flow t₀ x) = x
  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_off_axis : ∃ t, ∀ s, (J.symm.trans (flow t)).trans J ≠ flow s

def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V :=
  D.flow D.t₀

def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :=
  N_B = (e.symm.trans N_A).trans e

theorem copyNatural_refl_iff (N_A N_B : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B (AffineEquiv.refl ℝ V) ↔ N_B = N_A := …

theorem copyNatural_iff_apply (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B e ↔ ∀ x, N_B (e x) = e (N_A x) := …

theorem strictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω)
    (hSEC : SupportingEffectComplete Ω avail) (hSF : SingletonFaces Ω avail) :
    StrictConvex ℝ Ω := …

theorem card_le_two_of_centrallySymmetric {Ω : Set V} {c : V} (hΩ : CentrallySymmetric Ω c)
    (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 := …

theorem card_le_two_of_centrallySymmetric_full {Ω : Set V} {c : V}
    (hΩ : CentrallySymmetric Ω c) (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V)
    (e : ι → V →ᵃ[ℝ] ℝ) (_ : ∀ i, e i ∈ fullEffects Ω)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 := …

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

structure of §B, since the bound needs only the form `∑ cᵢ pᵢ`. -/

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
  Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail

theorem strictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω) (hK : KInf1 Ω avail)
    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :
    StrictConvex ℝ Ω := …

theorem kinf1_kernel_core :
    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), Convex ℝ Ω → IsClosed Ω →
      SupportingEffectComplete Ω avail → SingletonFaces Ω avail → StrictConvex ℝ Ω) ∧
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
| verdict, `KINF-1-FOUNDATIONS-PROVED` | `kinf1_kernel_core` |
| the finite stage | `FiniteStage`, `FiniteStage.vec`, `FiniteStage.states`, `states_isCompact`, `states_isClosed`, `states_convex`, `states_unit` |
| effects and the premises | `IsEffectOn`, `certainFace`, `SupportingEffectComplete`, `SingletonFaces`, `fullEffects`, `PerfectlyDistinguishable`, `CentrallySymmetric`, `affine_combo`, `affine_reflect`, `convex_affine_le` |
| drivability and copy naturality | `ElementaryDrivability`, `ElementaryDrivability.N`, `CopyNatural`, `copyNatural_refl_iff`, `copyNatural_iff_apply` |
| Lemma C | `strictConvex_of_supporting_singleton` |
| Lemma D | `card_le_two_of_centrallySymmetric`, `card_le_two_of_centrallySymmetric_full` |
| Lemma B | `eq_closedBall_of_frontier_subset_sphere` |
| the finite-preparation bound | `exists_vertex_of_certain`, `exposed_mem_range`, `exposedPoints`, `exposed_ncard_le`, `FiniteStage.exposed_le_card` |
| Theorem F2 | `simplex`, `ClassicallyExposed`, `response_eq_one_forces`, `mem_of_classicallyExposed`, `exists_zero_of_classicallyExposed`, `classical_exposed_ncard_le` |
| imported kinematics | `qubit_certain_face` |
| hypothesis K∞-1 | `KInf1`, `strictConvex_of_kInf1` |

Every theorem is followed, after the namespace closes, by its `#print axioms OIBridge.KInfFoundations.…` line. A
proof-only repair may add theorems named `kinf1_shared_…`.

### The reference implementation

**Frozen**, and checked by `controls.py` at `E`: the header, every declaration's text, the theorem names, one
`#print axioms` line per theorem, no definition beyond the frozen ones, the forbidden tokens (`sorry`, `admit`,
`native_decide`, `axiom`, `unsafe`, `opaque`, `implemented_by`, `extern`), and no `set_option` but
`linter.unusedSectionVars false`.

**Not frozen: the proofs of the theorems.** The reference implementation is blob **`0c07f7950c36559ee02066c0e989b9c552777848`**. A proof-only
repair — a change that leaves every frozen surface unchanged — is permitted as a later linear commit before `E`; the
result note names the reference blob and the module's blob at `E`, and, if they differ, states the departure from
the reference implementation and justifies it, which `controls.py` checks. A definition or structure that must
change is a freeze failure (Hazard 5).

### Pre-freeze evidence — design evidence, not attestation

Each run is a `workflow_dispatch` run whose `head_sha` is the commit named, on the disposable branch
`claude/kinf1-dev`, never landed. None is a `check-run` attestation, and no predicate of the round reads them. Each
was left to finish; the table records, job by job, what finished and how.

| run | head | what the head carries | the jobs that finished |
| --- | --- | --- | --- |
| (pending) | | | |

***

## The exact-computation layer — the frozen probe

`verification/lean/kinf_foundations_probe.py`, blob **`3c1adfe7b5025ae72856cf18d5a2f9937e46bd4f`**, is written before `F` and added by the
execution at stage 1 with exactly this blob, and the workflow runs it in its own shard at every execution commit from
stage 1 on. It uses Python integers and `Fraction`s, and pairs `(a, b) = a + b√3` of them, for every value it asserts:
**no floating point and no randomness.** Every point at which an identity is tested is fixed in the file, so two runs
print the same bytes. It exits 1 on any mismatch. Its statements are exact arithmetic replayed; they are not
kernel-certified, and the result note names them as this layer's. Its five sections are the instances tabulated
above under *What the exact layer instantiates*.

It ends with the line `kinf_foundations_probe: OK -- 384 checks` on success, which the result note carries verbatim, and
`kinf_foundations_probe: FAILED …` otherwise. It runs in under a second.

***

## The question, FROZEN — one target

### `KINF-1` — the vocabulary and its lemmas, in the kernel

**Do the frozen definitions elaborate, and do the frozen theorems hold in the kernel about them, as the verdict
`kinf1_kernel_core` states; and, with the frozen probe green at `E`, does the exact layer instantiate the bounds and
the lemmas as tabulated? The frozen answer is yes, in the layers Hazard 4 names.**

| part | statement | witness | layer |
| --- | --- | --- | --- |
| finite stage | the state body is compact and lies on the unit hyperplane | `states_isCompact`, `states_unit` | kernel |
| Lemma C | (SEC) + (SF) on a closed convex body ⇒ strict convexity | `strictConvex_of_supporting_singleton` | kernel |
| Lemma D | central symmetry ⇒ at most two perfectly distinguishable states, with any effects | `card_le_two_of_centrallySymmetric`, `…_full` | kernel |
| Lemma B | compact convex, `0` interior, frontier on the unit sphere ⇒ the closed unit ball | `eq_closedBall_of_frontier_subset_sphere` | kernel |
| finite preparations | exposed points are preparation vectors; at most `|ι|` | `exposed_mem_range`, `exposed_ncard_le` | kernel |
| Theorem F2 | at most `N` classically exposed points given the facet condition | `classical_exposed_ncard_le` | kernel |
| copy naturality | the pointwise conjugation identity | `copyNatural_iff_apply` | kernel |
| the qubit face | the certain face of `ρ ↦ ρ 0 0` is `{|0⟩⟨0|}` | `qubit_certain_face` | kernel, imported kinematics |
| K∞-1 | stated as `KInf1`; Lemma C under it | `KInf1`, `strictConvex_of_kInf1` | kernel (definition) |
| the instances | SIC, `C₂`, torus, Stiefel, 3-ball | the probe, sections 1–5 | exact computation |
| strict convexity ⇒ the facet condition | as stated above | this file | written remark |

The answer is reported as one of two labels: `KINF-1-FOUNDATIONS-PROVED`, the verdict `kinf1_kernel_core` in the
kernel with the probe green at `E`; `KINF-1-UNDECIDED`. The probe is not a label: green at `E`, it certifies its
layer; red at `E`, the round halts as a freeze failure.

## The controls

| role | object | what it is for |
| --- | --- | --- |
| Lemma D's hypothesis is load-bearing | `C₂`, capacity three | a body that is not centrally symmetric exceeds the bound |
| (SF) is independent of capacity and of full effects | the torus and Stiefel orbitopes | capacity two, full effects, flat faces |
| the singleton-face check is not vacuous | the 3-ball | singleton faces hold, so the check distinguishes |
| Theorem F2's bound is attained | the SIC ball | four exposed points on four ontic states |
| Theorem F2's step is not vacuous | the interior samples | every coordinate positive, so no response effect is certain |
| the frozen surfaces | `controls.py check E` | the declarations, the header, the note, the surfaces and the paths |

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `KINF-1` | `KINF-1-FOUNDATIONS-PROVED` | **very high** | every declaration elaborated and every theorem built within the three axioms in the design runs recorded above; the probe shard succeeded at the same heads |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `KINF-1-FOUNDATIONS-PROVED`

> In the kernel, at evidence level 2, over a real normed space and with no field, matrix carrier or substratum object: the state body of a finite observer stage is compact and lies on the unit hyperplane (`states_isCompact`, `states_unit`); a closed convex body with supporting-effect completeness and singleton faces is strictly convex (Lemma C, `strictConvex_of_supporting_singleton`); a centrally symmetric body admits at most two perfectly distinguishable states, with any family of effects and in particular with the full effects (Lemma D, `card_le_two_of_centrallySymmetric`, `card_le_two_of_centrallySymmetric_full`); a compact convex body with `0` in its interior whose frontier lies on the unit sphere is the closed unit ball (Lemma B, `eq_closedBall_of_frontier_subset_sphere`); a body generated by finitely many preparations exposes only their vectors (`exposed_mem_range`, `exposed_ncard_le`); a body realized on `N` ontic states and meeting each coordinate facet in at most one point exposes at most `N` states by response effects (Theorem F2, `classical_exposed_ncard_le`, through `response_eq_one_forces`); and, for the imported qubit kinematics, the certain face of the effect `ρ ↦ ρ 0 0` on density matrices is the single point `|0⟩⟨0|` (`qubit_certain_face`), joined in the verdict `kinf1_kernel_core`. Copy naturality is the pointwise conjugation identity (`copyNatural_iff_apply`), and hypothesis K∞-1 is stated as the definition `KInf1`, proved for nothing, with `strictConvex_of_kInf1` recording what it buys with singleton faces. In exact arithmetic replayed in CI, and not in the kernel, the round's probe instantiates the bounds and the lemmas: the SIC-embedded ball on four ontic states has exactly four exposed points, the tangency points, on a body with a continuum of extreme points; the Carathéodory orbitope `C₂` carries the exact capacity-three triple at `t = 0, 2π/3, 4π/3`; the torus and Stiefel orbitopes are centrally symmetric with flat faces exposed by valid effects, so singleton faces fail there while the capacity bound holds; and the 3-ball has singleton faces. Nothing here derives drivability, supporting effects, singleton faces or copy naturality from any OI construction, and nothing here is a reconstruction theorem.

### `KINF-1-UNDECIDED`

> The kernel verdict `kinf1_kernel_core` was not obtained. The statement at which the proof stopped is named, with what would settle it; the definitions stand as frozen, the exact layer stands as computed, and no lemma is stated as a result of this round beyond those the kernel checked.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, the label's sentence, the clause at
its mention `**THE CLAUSE, carried at this mention — the result.**`, the probe's summary line from the run at `E`, and
the reference blob and the module's blob at `E`. Outside the frozen sentence and the clause it does not contain any of
the phrases *OI supplies*, *OI derives*, *OI sources*, *sourced from OI*, *derived from the substratum*, *K∞-1 holds*,
*K∞-1 is proved*, *KInf1 holds*, *proves K∞-1*, *reconstruction theorem for*, *the completion is a ball* or *full
effects hold*, which `controls.py` checks.

| row | outcome |
| --- | --- |
| 1 | `KINF-1-FOUNDATIONS-PROVED` |
| 2 | `KINF-1-UNDECIDED` |

## The census, FROZEN

`verification/lean-manuscript-census.json` gains one family, appended last, the same under both outcomes: modules
`["KInfFoundations"]`, status `kernel-only`, no manuscript anchor, named

```text
the field-neutral vocabulary of the pre-quantum operational completion and its elementary lemmas: finite stages, effects, supporting-effect completeness, singleton faces, elementary drivability, copy naturality, Lemmas B, C and D, the finite-exposure bounds, the qubit certain face, and hypothesis K-infinity-1 as a definition (round KINF-1, reconstruction)
```

with the note

```text
Round KINF-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-kinf-1-foundations/preregistration.md. Definitions over a real normed space, with no field, matrix carrier or substratum object: FiniteStage with its state body, IsEffectOn, certainFace, SupportingEffectComplete, SingletonFaces, fullEffects, PerfectlyDistinguishable, CentrallySymmetric, ElementaryDrivability, CopyNatural, and KInf1, the statement of hypothesis K-infinity-1, proved for nothing. Theorems: states_isCompact and states_unit; Lemma C strictConvex_of_supporting_singleton; Lemma D card_le_two_of_centrallySymmetric; Lemma B eq_closedBall_of_frontier_subset_sphere; the finite-preparation bound exposed_ncard_le; Theorem F2 classical_exposed_ncard_le; qubit_certain_face, a theorem of the imported qubit matrix kinematics; verdict kinf1_kernel_core. The module sources none of its premises from any OI construction and contains no reconstruction theorem. The SIC, Caratheodory, torus, Stiefel and 3-ball instances are the round's probe kinf_foundations_probe.py, exact arithmetic and not the kernel. Carried by no manuscript.
```

## The workflow edit, FROZEN

After the NB-1 shard, the job

```yaml
  probes_kinf1:
    name: Numerical probes / KINF-1 foundations
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: KINF-1 foundations probe
        working-directory: verification/lean
        run: |
          echo "=== kinf_foundations_probe.py ==="
          python3 kinf_foundations_probe.py
```

and, in the aggregate `Numerical probes` job, `probes_kinf1` after `probes_nb1` in `needs`,
`KINF1_RESULT: ${{ needs.probes_kinf1.result }}` after `NB1_RESULT`, `echo "kinf1=${KINF1_RESULT}"` after the NB-1
echo, and `test "${KINF1_RESULT}" = success` after the NB-1 test. `OIBridge.lean` gains
`import OIBridge.KInfFoundations` directly after `import OIBridge.NativeGateBall`.

***

## What no outcome licenses

- **No outcome says that OI supplies, derives or sources** drivability, supporting effects, singleton faces or copy
  naturality; the definitions name them, and nothing discharges them.
- **No outcome says that K∞-1 holds** for any body, or that the completion's state space is a ball, or that its
  effects are the full effects.
- **No outcome calls `qubit_certain_face` a field-neutral result**: it is a theorem of the imported qubit kinematics.
- **No outcome calls the passage from strict convexity to the facet condition a kernel statement.**
- **No outcome revises any earlier verdict, edits any manuscript or changes any roadmap row.**

## Non-doings

This round does not do any of the following:
- define anything in the module beyond the frozen declarations;
- import into the module anything beyond the frozen imports;
- edit any closed round's record, any manuscript, any built artifact or `verification/ROADMAP.md`;
- change the workflow beyond the frozen edit that adds the probe's shard;
- start the sourcing questions — K∞-R, (SF), copy naturality, full effects — or any reconstruction theorem.

## Evidence level

**2** for the kernel layer — Lean theorems, kernel-checked, every named result printing its axioms, each within
`propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic replayed in CI, and the
written remark is a remark on paper; each is named as its own layer wherever it is cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/controls.py`, blob **`3086fafb4d2ad90b414c94f6742e11b62cc86866`**,
is written before `F` and added by the execution with exactly this blob. It imports nothing from the repository and
changes nothing; it reads `D` and the commit under check through `git`; it embeds every frozen text it compares
against.

`controls.py check <commit> [--freeze F]` fails unless all of the following hold:
- **the module**: the frozen header, no declaration beyond the frozen ones, no forbidden token or option, every
  theorem named in the frozen list or `kinf1_shared_…` with one `#print axioms` line, each frozen declaration byte
  for byte, and the verdict present exactly under `KINF-1-FOUNDATIONS-PROVED`;
- **the result note**: the outcome line once; the label's sentence once and no other label's; the clause after its
  mention; the probe's summary line; the reference blob and the module's blob at `E` in backticks, and, if they differ,
  the words *departure from the reference implementation*; none of the forbidden phrases outside the frozen texts;
- **the probe** has its frozen blob; **the workflow** is `D`'s with the frozen edit; **`OIBridge.lean`** is `D`'s with
  the frozen import line; **the census** is `D`'s with the frozen family appended;
- **the paths** changed from `D` are exactly the governed ones; with `--freeze F`, `F` is `D` plus this file alone and
  this file is unchanged at the commit.

`controls.py --self-test` checks its constants against this file (the sentences, the clause, the header, every frozen
declaration, the workflow job, the census family, both blobs and the probe's line); builds a synthetic execution for
each of the two rows and requires both to hold; and applies N mutation controls, each of which must fail with
its named code. Run at `D` beside this file, it prints:

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
   `kinf1_kernel_core` and its `#print axioms` line; the import line; the census family.
3. **Stage 3 — the verdict.** `kinf1_kernel_core`, making the module the reference implementation; or, if it cannot
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
| the probe is the frozen one, deterministic, and green in its own shard | `C3`: the probe's blob at stage 1 and at `E`; `Numerical probes / KINF-1 foundations` green at every execution commit and at `E` with the probe's `OK` line; the aggregate `Numerical probes` job green |
| every frozen declaration elaborates and every frozen theorem is kernel-checked within the three axioms | `C8`: the dispatch run at `E`, run to completion with no job cancelled and every job concluded `success`; its `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the module is classified and no manuscript changes | `C8`: the release gate at `E` — `lean-manuscript`, `staleness`, `voice`, `claims`, `mirror` — all green; `C7` |
| the frozen surfaces, the note and the paths | `C9`: `controls.py check E --freeze F` prints `controls: check OK` |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen surfaces unchanged** is repaired by later linear commits before `E`,
  and reported in the result note as a departure from the reference implementation.
- **A verdict that cannot be obtained** is reported `KINF-1-UNDECIDED`, with the statement named.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target or any frozen
  surface: a frozen declaration that does not elaborate or is false as frozen; the probe red at `E` with the frozen
  blob; a frozen surface that the release gate rejects. The round then halts under the specification's `S12`, with
  the result note naming the failure.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
