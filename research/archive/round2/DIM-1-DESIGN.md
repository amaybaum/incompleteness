# Round `DIM-1` ("dimension selector") — design study, read-only

Base `afa66d16d7adaffe94fb9bac391e6039c51dad8a` (current `main`, TRB-1's landing, PR #787), read in the detached
worktree `scratchpad/wt-dim1`. Every kernel citation is `identifier` + `file:line` at that commit under
`verification/lean-mathlib/OIBridge/`; Mathlib names were grepped in the pinned source tree `v4.33.0`
(`scratchpad/wave2/N/mathlib-v4.33.0/Mathlib`, matching `lakefile.toml` rev `v4.33.0`, `lean-toolchain`
`leanprover/lean4:v4.33.0`). No Lean toolchain is installed in this container, so nothing below was compiled; every
Lean fragment is a signature up to `:=`. Exact computations were run in Python under `scratchpad/round2/`
(`dim1_probe_fast.py`, output `dim1_probe_fast.out`; the follow-up inline check is reproduced in §3.4). Nothing in the
repository was changed.

Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, IIP `InvariantInnerProduct`,
TB `TransitiveBody`, NGB `NativeGateBall`, SC `StageCompletion`, CA `CompletionAction`. Prior work consumed, not
repeated: thread R (`wave2/R/RESULT.md`, `NOTES.md`), the NB-1 record (preregistration and result), COMP-1's design
(`round2/COMP-1-DESIGN.md`), K∞ §4–§6 and §16 (`k-infinity/K-INF-DESIGN.md`), FRONTIER F8/F13–F16 and
OWNER-AMENDMENT-1.

***

## 0. Verdict in one paragraph

The only selector that closes `d = 3` on top of TRB-1's `ball_d` field-neutrally and without presupposing dimension
three is the **composite** one: the two-copy, locally tomographic, copy-covariant native-gate theorem of NB-1, now on
"route B" (the ball supplied by TRB-1 in every `d`). Its kernel-missing steps (S1 controlled form, S2 block structure,
S4 value identity, written for every `d` and exact for `d ≤ 7`) are **elementary** — convexity of the Euclidean
ball, a conditional-state argument, a rational one-parameter positivity argument and polynomial identities on the
sphere — and need no Lie theory, no Jordan classification and no spectral theory beyond diagonalizing one orthogonal
involution. The single-system alternative (thread R's TRANS + energy observability) is equivalent to DIM3 given a
drive, is the single-system fingerprint of ℂ, and needs the compact rank-one classification, which the pinned Mathlib
does not have; every other candidate either fails on a `B^d` countermodel or restates `d = 3`. The theorem's honest
conclusion is `d ∈ {1, 3}`; `d = 1` (the classical bit, where the classical CNOT satisfies every composite hypothesis)
is excluded only by a non-classicality clause, which the round must name (§5, decision 3). What stays a premise after
DIM-1: local tomography (F13), the existence of a reversible interaction satisfying the gate relations (F14), one common
NOT on identical copies (F15), full effects (K0), and the upstream TRANS and finite rank. None of these mentions ℂ or
`3`; ℂ enters this chain nowhere before the Bloch adapter.

***

## 1. Question 1 — which selector condition, stated in the landed vocabulary

### 1.1 What TRB-1 hands over

| id | statement at `afa66d16` | where |
|---|---|---|
| EB | `0 < d → IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty → PreservesBody Ω G → BoundaryTransitive Ω G → ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d` | `exists_affine_image_eq_eball` TB:602 |
| QB | same hypotheses `→ ∃ R, 0 < R ∧ Ω = qBall Ω R` | `eq_qBall_of_boundaryTransitive` TB:457 |
| PUR | boundary states of a body-preserving boundary-transitive body are extreme | `extreme_of_isBoundaryState_of_transitive` TB:290 |
| EXC | a non-extreme boundary state ⟹ no body-preserving transitive family | `not_boundaryTransitive_of_nonextreme_boundary` TB:301 |
| CH | EB for `chartBody C` of a completion chart | `chartBody_eq_eball` TB:651 |
| D3 | `eball 3 = ball3` | `eball_three` TB:671 |
| `eball d := {x | ∑ j, x j ^ 2 ≤ 1}` | the coordinate Euclidean ball, `d` free | TB:518 |

`d` is a variable in every principal statement; the module's guard S1 forbids a `3` outside D3 and the controls. The
input to any selector is therefore `eball d` with `d : ℕ`, `0 < d`, plus whatever the selector adds.

### 1.2 The candidates

| candidate | statement in landed vocabulary | excludes | survives (countermodel) | sourced / premise | ℂ or `3` in disguise? | verdict |
|---|---|---|---|---|---|---|
| **(a) composite native gate** (NB-1; Masanes–Müller 2011, de la Torre–Masanes–Short–Müller 2012, MMAP 2013 in discrete form) | two copies of `eball d` with all `IsEffectOn` effects (KF:116), locally tomographic composite (COMP-1 `lt`), one involutive isometry `N` of `eball d` with `N z = −z` on both copies (`CopyNatural N N (refl)`, KF:284/289), a linear automorphism `G` of the composite with F (CNOT on the corners `±z`), Rt `(I⊗N)G(I⊗N) = G`, Rc `(N⊗I)G(N⊗I) = (I⊗N)G`, and `G`, `G⁻¹` sending product states into the maximal cone ⟹ `d ∈ {1, 3}` | every even `d` by parity (S5); every odd `d ≥ 5` by `p ≤ 1` (S3–S4) | `d = 1` (classical CNOT on two bits); `d = 3` (complex CNOT, NB-1 C3) | LT, `G`, common `N`, full effects: **premises** (F13, F14, F15, K0); the ball: **TRB-1**; `d ∈ {1,3}` from them: NB-1 kernel core + written S1/S2/S4 (F16) | no: F, Rt, Rc are classical-logic covariances of a controlled gate; P± is reversibility and positivity; no field, no `3`, no phase. The premise set was abstracted from the quantum CNOT, so §A.29 asks for an independent consequence — §3.4 supplies a candidate | **recommended**; the only non-circular selector available |
| (b) single-system TRANS + EO (thread R §3) | `BoundaryTransitive Ω G` for the drive's words + an injective equivariant linear map from the generator Lie algebra to the observables ⟹ `finrank = 3` | every `d ≠ 3` | none among balls | EO **unsourced**; given DRIVE, `{TRANS, EO} ⇔ DIM3` (R §5.1) | field-neutral in letter; EO is the dynamical correspondence, the single-system fingerprint of ℂ (Alfsen–Shultz; Barnum–Müller–Ududec 2014) | declined: no kernel route (step 8 needs compact rank-one classification, absent at `v4.33.0`, §3.1) and no gain over DIM3 as a premise |
| (c1) TRANS alone | landed `BoundaryTransitive` | none `≥ 2` | `boundaryTransitive_ball4` ON:735 (kernel); `B^d` with `O(d)` for every `d` | — | — | fails |
| (c2) DRIVE / minimal generator algebra / stationary state / `dim G = d` | `ElementaryDrivability` KF:264 and the R-thread variants | at most some `d` | `B^4` with `Sp(1)`, `U(2)`, `SO(4)`; `B^5` with `SO(5)`; `B^5` spin-2 (R §6, exact) | — | — | fail (R §2 d1–d4) |
| (c3) Hardy `K = N^r` + simplicity | composite counting | binary scope: none; with three systems `d ∈ {3, 7, 15, …}` | `K(2^n) = (d+1)^n` for every `d` (R exact I2) | LT is a premise here too | "minimal drivable dimension" restates DIM3 | fails |
| (c4) information capacity / one bit | `card_le_two_of_centrallySymmetric` KF:632 | none among balls | every centrally symmetric body has capacity ≤ 2 | — | "three complementary questions" restates `d = 3` | fails |
| (c5) Jordan-algebra / spin-factor classification + LT (Barnum–Graydon–Wilce 2020; Koecher–Vinberg) | self-dual homogeneous cone + LT composites closed in the class ⟹ complex Hermitian matrices | all non-ℂ spin factors | — | self-duality and homogeneity are premises; classification is literature | selects ℂ directly | not formalizable at `v4.33.0` (no Jordan algebras, no Koecher–Vinberg); literature cross-check only |
| (c6) spatial `SO(3)` acting transitively (Müller–Masanes 2013) | an effective `SO(3)` transitive on pure states ⟹ `d ≤ 3` (`S^3` is not `SO(3)`-homogeneous) | `d ≥ 4` | — | continuous spatial rotations are emergent on the cubic lattice (Step-5 interface) | imports space, not ℂ | borderline; not recommended (R §2(e)) |

**Necessity (thread R §5.5, confirmed here).** `B^d` with `O(d)`, `d ≥ 4`, satisfies every landed single-system
predicate — `PreservesBody`, `BoundaryTransitive` (kernel at `d = 4`), `SharpSeed`, full effects, capacity two,
`ElementaryDrivability` (exact: `Sp(1)` left multiplication on `B^4`) — and TRB-1's conclusion. Hence no selector
satisfied by every spin-factor ball can source `d = 3`; the selector must be violated by `B^d`, `d ≠ 3`, and the two
known such principles are EO (single-system, ℂ-fingerprint) and LT with an entangling reversible interaction
(composite). This is why (a) is recommended and not merely preferred.

### 1.3 What each clause of (a) excludes, and the countermodel bank

| `d` | ball + TRANS | DRIVE | (a) clause that excludes it | kernel piece | exact/witness |
|---|---|---|---|---|---|
| 1 (segment, classical bit) | holds (`{id, flip}`) | fails (`not_drivable_Icc` KF:529, on `Icc (−1) 1 ⊂ ℝ`) | **none**: the classical CNOT meets F, P±, Rt, Rc with `N = flip` | — | excluded only by a non-classicality clause (§4 T6) |
| 2 (rebit disk) | holds | fails (R B6, bounded) | parity: `p + q = 1` has no `p = q` | `parity` NGB:194, `dim_of_bounds` NGB:248 | NB-1 C2; consistent with real QM's LT failure (`X⊗Z ↦ −Y⊗Y` leaves the 9-dimensional LT span) |
| 3 (qubit) | holds (`transBody_fullAut3` TB) | holds (`ball3_drivable` KF:490) | survives | — | complex CNOT (NB-1 C3, exact); §3.4: on the scanned grid the only two-sided-positive gates are its 8 frame-preserving local conjugates |
| 4 (`Sp(1)`, `U(2)`, `SO(4)` on `B^4`) | holds (`boundaryTransitive_ball4` ON:735) | holds (R B1, exact) | parity: `p + q = 3` odd | `parity`, `dim_of_bounds` | — |
| 5 (quaternionic bit, `SO(5)`) | holds | holds (written) | `p ≤ 1` via positivity **with the common `N` and Rc**: drop Rc → the J/K map survives (C5); two NOTs → survives (C2N) | `p_le_one` NGB:176 | NB-1 probe (exact) |
| 7 (`SO(7)`, `G2`) | holds | holds | `p ≤ 1`: all algebra of a candidate holds, positivity fails at `1 − √3` (C7) | `p_le_one` | NB-1 probe (exact); with two NOTs of determinant `+1` a J/K map exists (K∞ §6) |
| 6 (`B^3 × B^3` as one system) | **fails**: `(pure, mixed)` is boundary, not extreme | holds | excluded upstream by TRB-1 EXC | `not_boundaryTransitive_of_nonextreme_boundary` TB:301 | — |
| 8 (qutrit body) | **fails**: rank-two states are boundary, not extreme | holds | excluded upstream by TRB-1 EXC | same | — |

Division of labour: TRANS (TRB-1) removes the non-elementary bodies; the selector removes the wrong-dimensional balls.
The load-bearing clauses at the surviving odd dimensions are Rc and the common `N` (both `d = 5` countermodels) and
two-sided positivity (`d = 7`); copy covariance by itself excludes nothing (an involution of every split `(p, q)`
exists on every `eball d`, probe Q4).

### 1.4 The ordering tension with the owner's chain

The owner's post-DIM path reads `B^3 → full local effect space → strong composite theorem → nonlocal reversible
interaction → …`. Under (a), the nonlocal reversible interaction (F14), local tomography (F13) and copy covariance
(F15) are **premises of the dimension selector**, so they enter before `B^3`, not after it. A dimension selector that
precedes the composite layer exists only in single-system form (EO), with the costs in row (b). This is decision 1 of §5.

***

## 2. Question 2 — circularity audit of (a) against NB-1

### 2.1 The chain at `afa66d16`

```
OI tower (F1, open) ─▶ DirectedStages + SC∞ (premise) ─▶ body D (CMP-1) ─▶ FiniteRank (F2, open) ─▶ CompletionChart (CA:144)
   ─▶ chartBody: compact, convex, interior (TB:109/80/121, no finite-dimensional CSpace)
   ─▶ OPACT-1 data ⟹ PreservesBody (CA:352)      TRANS = BoundaryTransitive (OG:79)  [premise K∞-R, unsourced]
   ─▶ EB (TB:602): ∃ A, A '' chartBody = eball d                                  ← ROUTE B REALIZED: the ball in every d
   ─▶ [DIM-1] eball d × eball d, LT (F13), common N (F15), G with F/P±/Rt/Rc (F14), full effects (K0) ⟹ d ∈ {1, 3}
   ─▶ non-classicality (ORD∞ / DRIVE / entangling) ⟹ d = 3 ─▶ eball_three (TB:671) ─▶ ball3
   ─▶ OG-1 / ON (SharpSeed, V4′) ⟹ directional family ⟹ lorentz_of_effects at p = 3 (NGB:105) ─▶ K2 (open)
```

### 2.2 Findings

1. **NB-1's d-ball input now comes from TRB-1.** NB-1's header (NGB:4–9) assumes "two locally tomographic d-ball
   systems with their full self-dual effect cones". Thread R's loop was: on route A the ball came from
   `DIM3 → ball3 → T0`. EB supplies `eball d` from compactness, convexity, interior, `PreservesBody` and
   `BoundaryTransitive` alone, with `d` free (guard S1 of TRB-1). Route B is realized up to the DIM-1 round itself.
2. **Nothing upstream presupposes `3`.** TB, IIP, CA, SC, OG, ON state their principal theorems for every `d`; the
   `ball3`/`Fin 3` objects at the base are controls (TB C1–C4), the `d = 3` corollary (TB D3), and OG/ON *consumers*
   (`seedOrbit_ball3_eq` OG:348, `lorentz_of_available` OG:422) that DIM-1 would make applicable. NGB's kernel core
   has `p`, `m`, `d` as variables; `3` appears only in `dim_of_bounds`' conclusion.
3. **Nothing upstream presupposes ℂ.** The modules KF, OG, ON, SC, CA, IIP, TB, NGB contain no `ℂ` token outside
   KF's comments (COMP-1 §1 census; TB and NGB re-checked here). NGB imports only four Mathlib files, none complex.
4. **What (a) still takes as premise, named:** LT (F13; COMP-1's `lt` field, chosen *as* a premise); existence of
   `G` with F, P±, Rt, Rc (F14; nothing single-system supplies it, `fullAut3`/`ball3Drive` act on one ball); the
   common `N` (F15; `CopyNatural` KF:284 is defined, unsourced; two-NOT countermodels at `d = 5, 7` are exact);
   full effects (K0: positivity is quantified over every `IsEffectOn (eball d)` functional — this *strengthens* the
   hypothesis P and is therefore load-bearing for the no-go; NB-1 lists "effect cones smaller than the dual cone"
   as open); upstream, TRANS (K∞-R), SC∞, FiniteRank.
5. **Two ways `3` could still re-enter, and why they do not.** (i) The NOT `N` is an involutive automorphism of
   `eball d` swapping two antipodal boundary points; that is a `d`-free statement, and its `±1` eigenspace split
   `(p, q+1)` is *derived*, not assumed; the `det N = +1` reading of a NOT on a flow (K∞ §4) is a further
   premise not used here. (ii) The corners `±z` are a perfectly distinguishable pair (`card_le_two_of_centrallySymmetric`
   KF:632 says there is no larger one); again `d`-free.
6. **Where the loop would re-form.** If the round stated the theorem on `ball3` or `Fin 3`, or took `N` from
   `ball3Drive.N`, or the composite from any ℂ-module (`FiniteOperationalTheory`, `tensorOf`, `kronId`,
   `local_tomography_physical`: COMP-1 §4 lists them). The guards of §4 forbid each.

***

## 3. Question 3 — Lean/Mathlib feasibility at `v4.33.0`

### 3.1 What the pinned Mathlib has and lacks (grepped)

| need | present | absent |
|---|---|---|
| orthogonal/unitary groups | `Matrix.orthogonalGroup` (abbrev of `unitaryGroup`, `LinearAlgebra/UnitaryGroup.lean:295`); `LieAlgebra.Orthogonal.so` (`Algebra/Lie/Classical.lean:168`); `skewAdjointMatricesLieSubalgebra` (`Algebra/Lie/SkewAdjoint.lean:114`) | — |
| Lie theory | `LieAlgebra.rank` (`Rank.lean:65`), `IsCartanSubalgebra` (`CartanSubalgebra.lean:50`), Killing form and Cartan's criterion (`Killing.lean`, `CartanCriterion.lean`), `sl₂` (`Sl2.lean`), `LieGroup` class (`Geometry/Manifold/Algebra/LieGroup.lean:73`) | closed-subgroup theorem, compact Lie algebra classification, rank-one classification, any `so(3) ≅ ℝ³` Lie isomorphism (only `crossProduct` with `jacobi_cross`, `leibniz_cross`, `LinearAlgebra/CrossProduct.lean:146/123`) |
| Clifford / quaternions | `CliffordAlgebra`, `pinGroup`, `lipschitzGroup` (`SpinGroup.lean`); `Quaternion` with `NormedDivisionRing ℍ` (`Analysis/Quaternion.lean:87`) | `Spin(n) → SO(n)` as a Lie group fact; Hopf/hairy-ball |
| convexity | `strictConvex_closedBall` (`StrictConvexSpace.lean:75`), `mem_extremePoints` (`Extreme.lean:133`), `IsCompact.exists_isMaxOn` (`Topology/Order/Compact.lean:248`), everything TRB-1 used | — |
| spectral theory | `LinearMap.IsSymmetric.eigenvectorBasis`, `hasEigenvector_eigenvectorBasis` (`Analysis/InnerProductSpace/Spectrum.lean:306`) | — |
| determinants | `Matrix.det_neg` (`Determinant/Basic.lean:284`), `det_mul` (`:138`), `det_transpose` (`:203`) | a named "skew-symmetric of odd order has zero determinant" |

Consequence: route (b) (EO) is out of reach — its step 8 is the rank-one classification, and the Lie algebra of the
closure of a word group is not even definable without the closed-subgroup theorem. Route (a) needs none of this.

### 3.2 The recommended route, step by step, with cost

Setting (all in `Fin d → ℝ`, homogenized to `Fin (d+1) → ℝ` by `Fin.cons 1`; the composite carrier is the function
space `W d := Fin (d+1) → Fin (d+1) → ℝ`, with product states `vecMulVec x̂ ŷ` and product-effect values
`ê ⬝ᵥ (ω *ᵥ f̂)`; see §3.3 for why this carrier is legitimate here).

| step | content | needs | class | cost |
|---|---|---|---|---|
| 1 | definitions: homogenization, `prodState`, `prodEff`, `maxCone`, `minCone`, the two `N`-actions, the corners `k a = ±z` | nothing | elementary | small |
| 2 | marginals of a max-cone state are states: `x ∉ eball d` is separated by the effect `(1 − v·y)/2`, `v = x/‖x‖` | `Real.sqrt`, Cauchy–Schwarz as a sum inequality | elementary | small |
| 3 | affine functional `≥ 0` on `eball d` vanishing at two antipodal boundary points vanishes identically (vanishes at the centre, then by central symmetry everywhere) | — | elementary | small |
| 4 | **control marginal is the corner**: by F and step 3, `(k_{1−a}ᵀ ⊗ 1)(G(k_a ⊗ ω)) = 0`; the only state of the ball on which the sharp effect `(1 − z·x)/2` vanishes is `z` (singleton face; `singletonFaces_closedBall` KF:658 is stated for a `StrictConvexSpace` closed ball, so either transport through `EuclideanSpace` or re-prove by Cauchy–Schwarz) | KF | elementary | small |
| 5 | **extreme marginal ⟹ product** (the core of S1): for a max-cone state `Z` whose control marginal is extreme, conditional states `(1 ⊗ g)(Z)/g(m)` and `(1 ⊗ (1−g))(Z)/(1−g(m))` are states averaging to the marginal, so both equal it; effects span, so `Z = k_a ⊗ m` | extremality of `±z` in `eball d` (parallelogram identity, or TB PUR with a transitive family on `eball d`, which is not landed for general `d`; prefer the direct proof) | elementary | medium |
| 6 | `M_a` (the target marginal map) is an affine automorphism of `eball d` fixing `0` and orthogonal: step 5 for `G` and `G⁻¹`, unique centre of symmetry, `isometry_of_contractions` NGB (restated with the Euclidean sum norm); Rt gives `N M_a N = M_a`, F and Rc give `M₁ = N M₀` | NGB:§E | elementary | medium |
| 7 | **diagonal form of `N`**: an orthogonal involution is symmetric, so `V = ker (N − 1) ⊕ ker (N + 1)` with an orthonormal basis of each (spectral theorem at `v4.33.0`, or `gramSchmidt`); `p := finrank (ker (N − 1))`, `q + 1 := finrank (ker (N + 1))` | `Analysis/InnerProductSpace/Spectrum.lean` | standard, Mathlib-supported | medium–high (the one step with instance friction: `EuclideanSpace ℝ (Fin d)` vs `Fin d → ℝ`) |
| 8 | **S2 tangent argument**: for `c ∈ T_A`, the pure control curve `u + ((1 − s²) z + 2 s c)/(1 + s²)` makes the value `(A − B) s² + 2 C s ≥ 0` for all `s` with `A + B = 0`, so `C = 0`: `(1, −t)·Φ(1, t) = 0` and `(1, −N t)·Φ(1, t) = 0` on the sphere for every control-output component `Φ` | rational parametrization, `nlinarith` | elementary | medium |
| 9 | **S2 block form**: evaluate the two sphere identities at `±e_i` and `(3e_i + 4e_j)/5` (rational points, no roots): `Φ_00 = 0`, `Φ_0r = Φ_r0` for `r ∈ V₊`, zero for `V₋` in row/column `0`, antisymmetric `V₊` and `V₋` blocks, zero cross blocks | — | elementary | medium (bookkeeping) |
| 10 | **S4 value identity**: with the block form, `(f ⊗ g)(G̃(s ⊗ t)) = (1, b)(I + Γ_ac)(1, t)` on basis control states/effects and `V₊`-affine target data | `Finset.sum` manipulation | elementary | medium |
| 11 | S4 conclusion, S5, count | `p_le_one` NGB:176, `parity` NGB:194, `dim_of_bounds` NGB:248 | **landed** | none |
| 12 | S5 input: `G` maps the subspace `T_A ⊗ V₋` into itself (S2 + Rt), anticommutes there with `N ⊗ 1` (Rc), `finrank (V₊ ⊗ V₋) = p(q+1)`, `finrank (T₋ ⊗ V₋) = q(q+1)`, hence `p = q` | `LinearMap.restrict`, `finrank` of spans of matrix units | elementary | medium |
| 13 | `d = 1` exclusion (§4 T6) | one of: `minCone = maxCone` at `d = 1`; ORD-1's predicate; `isEmpty_drivability_of_finite_orbits` ON:124 | elementary | small |
| 14 | transport from `Ω` with TRANS to `eball d` (EB) and back for the composite hypotheses (`isEffectOn_tr` ON:217 pattern) | TB, ON | elementary | small–medium |

Total: a 700–1100 line module, comparable to TB (924) and larger than NGB (289). No step is research mathematics; the
risk is engineering (indices over `Fin (d+1) × Fin (d+1)`, the `EuclideanSpace`/`Fin d → ℝ` seam in step 7).

### 3.3 The carrier question (COMP-1 interaction)

COMP-1 (design only; `CompositeInterface.lean` is **not** in the tree at `afa66d16`) types the composite abstractly
and makes `lt` a field; its L11 embeds any LT composite into the function-space model. For a composite of two copies of
`eball d`, LT forces the carrier up to isomorphism, so stating DIM-1 on `W d` loses nothing *given LT*; the price is
that LT is then built into the carrier rather than carried as a field. Two honest options: (i) state DIM-1 on `W d`
now, with LT named in the header as the premise the carrier encodes, and add the one-line L11 corollary when COMP-1
lands; (ii) wait for COMP-1 and state DIM-1 on `Composite (eball d) (eball d)`. Option (i) decouples the rounds and
keeps NGB's block coordinates; option (ii) is the architecturally clean form. Decision 2 of §5.

### 3.4 Cheap exact probe run here (§A.16; read-only, not a governed artifact)

`dim1_probe_fast.py` at `d = 3` (basis `u, x, y, z`; `N = diag(1, 1, −1, −1)`): parametrize `G̃` by S1
(`G̃(k_a ⊗ t) = k_a ⊗ N^a t`) and the S2 form on every control-output component (16 parameters), impose normalization,
Rt and Rc exactly (sympy): **7 free parameters** remain, `det G̃ = a₁₁² a₂₂² b₁₂² b₂₁²`; the complex CNOT lies in the
family at `(a₁₁, a₂₂, b₁₂, b₂₁) = (1, 1, −1, 1)`, others `0`. Two-sided product positivity, sampled on `22 × 22`
pure product states and effects over a grid of parameter values (`{±1, ±½}` for the four determinant factors,
`{0, ±½}` for the other three): one-sided positivity survives at 136 grid points (a continuum), two-sided positivity at
exactly **8**, and these 8 are exactly the orbit of the complex CNOT under the 64 frame-preserving local symmetries
`(L_A' ⊗ L_B) G (L_A ⊗ L_B)`, `L = diag(1, ±1, ±1, 1)` (keeping `M₀ = I`). The script as run recorded both minima but
filtered only on the first; the filtering was redone from the recorded output. A closed form on the equator,
`(1 + g_x t_x) + a₁₁ (g_x + t_x)`, gives `2 − 2a₁₁ ≥ 0` for `G` and `2 − 2/a₁₁ ≥ 0` for `G⁻¹`, so `a₁₁ = ±1`
analytically (likewise `a₂₂`); the vanishing of `a₃₂, b₀₂, b₃₁` and `|b₁₂| = |b₂₁| = 1` are grid evidence only.

Reading, with the skepticism §A.31 asks for on a favourable branch: this is a **candidate** §A.29 postdiction — the
premise set, built to fix `d`, also determines the gate at `d = 3` up to local frame symmetries, which is true of the
quantum CNOT — and it shows that inverse positivity P⁻ is load-bearing for uniqueness at `d = 3` (not for the
dimension). It is research-level evidence (exact family, sampled positivity), not a theorem; a DIM-1 round should not
freeze it, and a follow-up round could.

### 3.5 Honest statement of what cannot be certified

`d = 3` cannot be certified from TRB-1's output alone, nor from any single-system principle every spin factor obeys
(§1.2, necessity). With the composite premises F13–F15 and K0 named, `d ∈ {1, 3}` can be certified in the kernel at
`v4.33.0` by elementary means; `d = 3` additionally needs a non-classicality premise (§4 T6). The independent
postdictions of the premise set are: the branch structure of S1 (`M_a` isometries, `M₁ = N M₀`); the gate's
uniqueness at `d = 3` up to local frame symmetries (§3.4, candidate); and the exclusion of the rebit and the quaternionic
bit, consistent with the known failure of local tomography in real and quaternionic QM.

***

## 4. Question 4 — typed skeleton for `OIBridge/DimensionSelector.lean`

Imports: `OIBridge.TransitiveBody`, `OIBridge.NativeGateBall`, Mathlib convexity/spectral files as needed. No ℂ
module, no `TensorProduct`. Namespace `OIBridge.DimensionSelector`; `open KInfFoundations OrbitGeneration
TransitiveBody NativeGateBall`.

### 4.1 Definitions

```lean
variable {d : ℕ}

/-- Homogenization `x ↦ (1, x)`. -/
def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x
/-- The composite carrier of two copies: a real function on index pairs (local tomography is the
premise this carrier encodes; see the header). -/
abbrev W (d : ℕ) := Fin (d + 1) → Fin (d + 1) → ℝ
/-- Product state. -/
def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν
/-- Homogenized affine functional: `e x = ehom e ⬝ᵥ hom x`. -/
noncomputable def ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : Fin (d + 1) → ℝ
/-- Value of the product effect `e ⊗ f` on a composite vector. -/
def prodEffVal (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (ω : W d) : ℝ := ∑ μ, ∑ ν, ehom e μ * ω μ ν * ehom f ν
/-- The maximal cone of two copies of `Ω`: nonnegative on every product effect. -/
def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) :=
  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}
/-- The minimal cone: the convex cone generated by product states. -/
def minCone (Ω : Set (Fin d → ℝ)) : Set (W d)
/-- `N` acting on the target index and on the control index of a composite vector. -/
def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : W d →ₗ[ℝ] W d
def actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : W d →ₗ[ℝ] W d
/-- The corners `k 0 = z`, `k 1 = −z`. -/
def corner (z : Fin d → ℝ) : Fin 2 → (Fin d → ℝ) := ![z, -z]

/-- The NOT of a copy: a linear involution preserving the ball and inverting the corner axis. -/
structure IsNot (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Prop where
  unit     : ∑ j, z j ^ 2 = 1
  invol    : ∀ x, N (N x) = x
  preserves: ∀ x ∈ Ω, N x ∈ Ω
  flips    : N z = -z

/-- The native-gate hypotheses on two identical copies of `Ω` (copy covariance: one `N` in both relations). -/
structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
    (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame   : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd  : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv  : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relT    : ∀ ω, actT N (G (actT N ω)) = G ω
  relC    : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)
```

`CopyNatural` (KF:284) is not a field: the structure uses one `N` in `relT` and `relC`, which *is* copy covariance for
identical copies (`copyNatural_refl_iff` KF:289). The header states this.

### 4.2 Principal theorems (signatures up to `:=`)

```lean
/-- T1 (S1 core). A max-cone vector with an extreme control marginal is a product. -/
theorem prod_of_extreme_marginal {Ω : Set (Fin d → ℝ)} (hconv : Convex ℝ Ω) (hc : IsCompact Ω)
    {ω : W d} (hω : ω ∈ maxCone Ω) (hnorm : prodEffVal 1 1 ω = 1) {x : Fin d → ℝ}
    (hx : x ∈ Ω.extremePoints ℝ) (hmarg : margC ω = x) : ω = prodState x (margT ω)

/-- T2 (S1). The gate is controlled: on a corner it acts locally by an affine automorphism of the ball. -/
theorem controlled_form (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (a : Fin 2) :
    ∃ M : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), (∀ y ∈ eball d, M y ∈ eball d) ∧
      ∀ y, G (prodState (corner z a) y) = prodState (corner z a) (M y)
theorem branch_isometry (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (a : Fin 2) :
    ∀ y, ∑ j, (branch hN hG a y) j ^ 2 = ∑ j, y j ^ 2
theorem branch_relations (hN) (hG) :
    (∀ a y, N (branch hN hG a y) = branch hN hG a (N y)) ∧ (∀ y, branch hN hG 1 y = N (branch hN hG 0 y))

/-- T3 (S2, tangent). For a control tangent direction `c` and every control-output component, the
antipodal target effect annihilates `G̃ (c ⊗ ·)` on pure target states, at both corners. -/
theorem tangent_vanish (hN) (hG) {c : Fin d → ℝ} (hcz : c ⬝ᵥ z = 0) (i : Fin (d + 1))
    {t : Fin d → ℝ} (ht : ∑ j, t j ^ 2 = 1) :
    (∑ ν, (hom (-t)) ν * normGate hN hG (tangentVec c t) i ν) = 0 ∧
    (∑ ν, (hom (-(N t))) ν * normGate hN hG (tangentVec c t) i ν) = 0

/-- T4 (S2, block form), stated in a basis diagonalizing `N`: the `E₊` block is `[[0, A],[A, B]]` with
`B` antisymmetric, the `V₋` block antisymmetric, cross blocks zero. -/
theorem block_form (hN) (hG) (D : DiagonalizingBasis N) : BlockForm hN hG D

/-- T5 (S4 value identity) — the bridge into `NativeGateBall.blocks_vanish`'s hypothesis. -/
theorem value_identity (hN) (hG) (D : DiagonalizingBasis N) :
    ∀ k l : Fin (d - 1), ∀ i : Fin D.p, ∀ s : ℝ, (s = 1 ∨ s = -1) → ∀ b : Fin D.p → ℝ, (∑ j, b j ^ 2) = 1 →
      0 ≤ (1 + s * blockA hN hG D i k l) + ∑ j, b j * (blockA hN hG D j k l
            + s * ((if j = i then (1:ℝ) else 0) + blockB hN hG D j i k l))

/-- T6 (S5 input). -/
theorem split_balanced (hN) (hG) (D : DiagonalizingBasis N) : D.p = D.q

/-- **Principal.** Two identical copies of the Euclidean ball with a native gate have dimension one or three. -/
theorem dim_of_nativeGate (hd : 0 < d) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d = 1 ∨ d = 3

/-- **Route B, assembled.** A compact convex body with interior, boundary transitive under a body-preserving
family, whose two identical copies carry a native gate (hypotheses stated on `Ω` and transported along EB),
has dimension one or three. -/
theorem dim_of_transitive_nativeGate (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {Gb : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hGb : PreservesBody Ω Gb) (hT : BoundaryTransitive Ω Gb)
    {z N G} (hN : IsNotBody Ω z N) (hG : NativeGateBody Ω z N G) : d = 1 ∨ d = 3

/-- The `d = 1` exclusion, one theorem per clause (decision 3 picks which is frozen; all three are cheap). -/
theorem nativeGate_entangling_ne_one (hd : 0 < d) (hN) (hG : NativeGate (eball d) z N G)
    (hent : ∃ x ∈ eball d, ∃ y ∈ eball d, G (prodState x y) ∉ minCone (eball d)) : d ≠ 1
theorem nativeGate_drivable_ne_one (hd : 0 < d) (hN) (hG) (hD : Nonempty (ElementaryDrivability (eball d))) : d ≠ 1
theorem nativeGate_ordInf_ne_one … -- only if ORD-1's predicate has landed; otherwise omitted

/-- The selector: dimension three. -/
theorem three_of_nativeGate (hd : 0 < d) (hN) (hG) (hnc : <the frozen non-classicality clause>) : d = 3
```

### 4.3 Controls as kernel theorems

```lean
/-- C1 (positive control, classical). At `d = 1` the classical CNOT is a native gate with `N = −1`. -/
theorem nativeGate_classical : NativeGate (eball 1) ![1] (-LinearMap.id) cnot1
theorem minCone_eq_maxCone_one : minCone (eball 1) = maxCone (eball 1)       -- why the clause of T6 is needed

/-- C2 (positive control, algebraic part). At `d = 3`, the Pauli-coordinate CNOT satisfies the frame, both
relations, and is an involution (`G² = 1`); its positivity is NOT claimed here (§5, decision 5). -/
theorem cnot3_frame : ∀ a b, cnot3 (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b))
theorem cnot3_relT : ∀ ω, actT N3 (cnot3 (actT N3 ω)) = cnot3 ω
theorem cnot3_relC : ∀ ω, actC N3 (cnot3 (actC N3 ω)) = actT N3 (cnot3 ω)
theorem cnot3_sq : ∀ ω, cnot3 (cnot3 ω) = ω

/-- C3 (even dimensions fail by parity alone). -/
theorem no_balanced_split_even (hd : Even d) (p q : ℕ) (h : p + q + 1 = d) : p ≠ q

/-- C4 (the ball in dimension four is transitive and drivable-by-record but admits no native gate). -/
theorem not_nativeGate_four {z N G} (hN : IsNot (eball 4) z N) : ¬ NativeGate (eball 4) z N G
-- together with the landed `boundaryTransitive_ball4` ON:735 cited in the header, not re-proved

/-- C5 (clause independence pointers). The `d = 5` and `d = 7` countermodels (NB-1 C5, C2N, C7) stay at the
exact layer (`native_gate_ball_probe.py`, replayed in CI); the header cites them and the module claims nothing
about them. -/
```

Reverse-direction obligation (§A.34): the principal theorem is one direction (hypotheses ⟹ `d ∈ {1, 3}`); the
witnesses at `d = 1` (C1, complete) and `d = 3` (C2, algebraic part only) are separate theorems; no `↔` with `d`.

### 4.4 Semantic guards for `controls.py` (TRB-1 style, `check(code, name, cond)` over `split_statement`)

| guard | content | mutation that must fail |
|---|---|---|
| S1 field-neutral | no token `ℂ`, `Complex`, `TensorProduct`, `⊗ₜ`, `⊗ₖ`, `kroneckerMap`, `Kronecker`, `unitaryGroup`, `Hilbert`; imports ⊆ `{OIBridge.TransitiveBody, OIBridge.NativeGateBall, Mathlib.*}` | a `Complex` import |
| S2 dimension | outside the controls section, `3` occurs only in the conclusions `d = 1 ∨ d = 3` and `d = 3` of the principal theorems; no `ball3`, `Fin 3`, `eball 3`, `finrank … = 3`; every principal theorem binds `d` | a hypothesis `d = 3` or `Fin 3` in a principal theorem |
| S3 frozen hypotheses | `NativeGate` has exactly the fields `frame`, `posFwd`, `posInv`, `relT`, `relC`; `IsNot` exactly `unit`, `invol`, `preserves`, `flips`; the principal theorems take exactly `0 < d`, `IsNot`, `NativeGate` (plus TRANS clauses in the route-B form) | `posInv` removed; `d ≠ 1` smuggled into `NativeGate` |
| S4 premises never concluded | no theorem's conclusion is `NativeGate …`, `IsNot …`, `BoundaryTransitive …`, `∃ G, …`, except the named controls C1–C2 | a theorem concluding `∃ G, NativeGate …` for general `d` |
| S5 directional | no `↔` whose one side is an equation in `d`; witnesses are separate theorems | `dim_of_nativeGate` restated as `↔` |
| S6 one `N` | both relation fields mention the same bound `N`; no second NOT variable in `NativeGate` | a two-NOT variant |
| S7 reuse, not re-proof | `p_le_one`, `parity`, `dim_of_bounds` are cited from `NativeGateBall` (import present; no theorem of those names declared here) | a local re-declaration of `parity` |
| S8 non-classicality explicit | `three_of_nativeGate` carries the frozen clause as a hypothesis; `dim_of_nativeGate` does not | the clause folded into `NativeGate` |
| S9 controls present | C1, C2 (four theorems), C3, C4 with `#print axioms` | C2's `cnot3_relC` removed |
| S10 forbidden phrases | result note and header contain none of *OI selects*, *OI implies d*, *OI forces d*, *kernel theorem that OI …*, *copy covariance derived*, *local tomography derived* | — |
| N1–N3 | declaration list and kinds, binder contexts, no `sorryAx`; every `#print axioms` within `[propext, Classical.choice, Quot.sound]` | as TRB-1 |

### 4.5 Dependency map

```
TB EB (exists_affine_image_eq_eball) ──▶ eball d ──┐
TB PUR / direct parallelogram ──▶ ±z extreme ──────┤
KF IsEffectOn, PerfectlyDistinguishable ───────────┼──▶ T1 prod_of_extreme_marginal ──▶ T2 controlled_form
NGB isometry_of_contractions ──────────────────────┘                                   ──▶ branch_isometry, branch_relations
                                                                                            │
Mathlib spectral theorem ──▶ DiagonalizingBasis N (p, q) ◀──────────────────────────────────┤
                                                                                            ▼
T3 tangent_vanish ──▶ T4 block_form ──▶ T5 value_identity ──▶ NGB p_le_one ─┐
                                   └──▶ T6 split_balanced (NGB parity) ─────┼──▶ NGB dim_of_bounds ──▶ dim_of_nativeGate
                                                                             │
ON isEffectOn_tr, TB EB ──▶ transport ──▶ dim_of_transitive_nativeGate ◀─────┘
non-classicality clause (T6′) ──▶ three_of_nativeGate ──▶ TB eball_three ──▶ ball3 ──▶ OG/ON consumers (downstream, not in the round)
```

No node depends on COMP-1, ORD-1 (unless decision 3 selects ORD∞), EO, DRIVE (unless decision 3 selects it), L3B, K2,
or any ℂ module.

### 4.6 Frozen out

- any source of LT, of `G`, of the common `N`, of full effects, of TRANS or of finite rank; any statement that OI
  supplies them;
- K2 (the composite as the quantum tensor product), the CP/antiunitary bridge, the Bloch adapter (F18), SWAP,
  composite unitary control, continuous local groups, `G² = I` as a hypothesis, intermediate cones;
- the positivity of the `d = 3` witness in the kernel (exact layer only, decision 5), and the §3.4 uniqueness
  statement;
- EO, DIM3 as a premise, the one-sided variant (`G⁻¹` positivity dropped: NB-1's open item), non-ball bodies,
  restricted effect cones, unrelated NOTs;
- edits to NGB, TB, OG, ON, manuscripts; `verification/ROADMAP.md` (see §5, note after decision 5).

### 4.7 Outcomes

- `DIM-1-SELECTOR-PROVED`: every frozen theorem built within the three axioms; controls OK at `E`; the result note's
  sentence states: two identical copies of the Euclidean ball of any dimension with a native gate (F, P±, Rt, Rc,
  one `N`) have `d ∈ {1, 3}`; with the frozen non-classicality clause, `d = 3`; the hypotheses are named premises
  (LT encoded by the carrier, `G`, `N`, full effects) and the ball is TRB-1's; nothing here says that OI supplies any
  of them; the `d = 3` witness is certified algebraically in the kernel and positively at the exact layer.
- `DIM-1-HALTED` (anything else, under `S12`), the note naming the failing step. If step 7 (diagonalization) cannot
  be closed, the frozen surface may carry `N` in diagonal form as a hypothesis **only if that choice is made before
  `F`**, with the general-`N` adapter moved to a successor round; no post-`F` weakening.

Governed paths (proposed): record directory `verification/programmes/oi-qm/reconstruction/round-dim-1-dimension-selector/`,
receipt `verification/receipts/DIM-1.json`; execution `A verification/lean-mathlib/OIBridge/DimensionSelector.lean`,
`M verification/lean-mathlib/OIBridge.lean` (import after `import OIBridge.TransitiveBody`, OIBridge.lean:252),
`M verification/lean-manuscript-census.json` (one `kernel-only` family after the TRB-1 family at census.json:1351).

***

## 5. Owner decision points

1. **Accept the composite route as the dimension selector.** It moves local tomography, the reversible interaction
   and copy covariance ahead of `B^3` in the chain (§1.4). The alternative — a single-system selector before the
   composite layer — exists only as EO, which is equivalent to DIM3 given a drive, is the fingerprint of ℂ, and has
   no kernel route at `v4.33.0`.
2. **Carrier.** State DIM-1 now on the function-space carrier `W d` with LT named as the premise it encodes
   (independent of COMP-1; NGB's coordinates), or wait for COMP-1 and state it on `Composite (eball d) (eball d)`
   (architecturally clean; serializes the rounds).
3. **The `d = 1` clause.** Entangling (`G` not `minCone`-preserving; self-contained, cheap, a new named premise),
   DRIVE (`Nonempty (ElementaryDrivability (eball d))`, ties to K∞-R's object, needs the `Fin 1` adapter of
   KF:529/ON:124), or ORD∞ (ORD-1's predicate; only if ORD-1 lands first). Recommendation: freeze the entangling
   clause as the theorem's own, and add the DRIVE corollary; leave ORD∞ to a follow-up.
4. **Form of `N`.** General involutive isometry with the diagonalization adapter inside the round (spectral theorem;
   the one Mathlib-friction step), or `N` in coordinate sign form as the frozen hypothesis with the adapter as a
   successor round. Recommendation: general `N`, with a design run on the adapter before `F` and the fallback fixed
   before `F`.
5. **Depth of the `d = 3` positive control.** Algebraic hypotheses in the kernel and positivity at the exact layer
   (recommended; no ℂ anywhere), a separate ℂ control module proving `|⟨f⊗g|U|s⊗t⟩|² ≥ 0` (needs the Bloch adapter),
   or deferral of the witness entirely to the Bloch-adapter round.

Propagation note (§A.25): a `DIM-1-SELECTOR-PROVED` landing makes ROADMAP K1's sentence "the theorem for general `d`
rests on the round's written proof" (ROADMAP:984–990) and the NB-1 census note's "the theorem for general d is not a
kernel theorem" (census.json:1302) stale. The NB-1 record is immutable; the correction is a ROADMAP K1 edit and the
DIM-1 census note, either in the round's governed paths or in a same-day hygiene change — to be fixed before `F`.

***

## Owner decisions (2026-10-04)

1. The DIM-1 route is composite. Frozen target: `B^d` + local tomography + a common NOT + a reversible CNOT-frame
   action + two-sided positivity ⟹ `d ∈ {1, 3}`; with the non-classicality clause of decision 3, `d = 3`.
2. Carrier: the function-space (bilinear) carrier, stated inside DIM-1 with local tomography named explicitly as the
   premise that makes the joint carrier a function/bilinear space. No consumption of COMP-1's `Composite`; after COMP-1
   lands, an adapter corollary shows its structure instantiates the DIM-1 carrier.
3. `d = 1` is excluded by an entangling-action premise, genuinely composite: there is a pure (extreme) product input
   whose reversible joint image is an extreme joint state outside the image of the product states. Creating
   correlations from a mixed product distribution does not qualify (classical reversible gates do that). Not DRIVE,
   not ORD∞.
4. The NOT `N` is a general involution; the diagonalization adapter (spectral theorem) lives inside DIM-1 and is part
   of the design evidence before `F`. The statement stays basis-independent; sign-diagonal `N` is not a premise.
5. Both exclusion and survival are kernel theorems: the hypotheses eliminate every `d ∉ {1, 3}`, and the `d = 3` CNOT
   construction satisfies the exact frozen conditions, with the positivity algebra in the kernel. No ℂ-typed control
   stands in for existence. The "exactly 8 frame-preserving local conjugates survive" observation is a research
   postdiction only, outside the frozen claim.

Propagation, preregistered before `F`: on a PROVED landing, exactly the stale ROADMAP K1 rows and NB-1's census sentence
("not a kernel theorem") are edited; no other manuscript or roadmap change in the round.
