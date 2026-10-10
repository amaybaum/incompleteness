# SS-LEDGER: thread SS, a composite-free dimension selector

This is an off-repo, read-only research ledger. Nothing in it is frozen, certified, adopted or proposed as
ROADMAP or manuscript wording. Every premise named below is a candidate and none is sourced.

## 0. Base, scope, evidence layers

- **Base.** `scratchpad/wt-68b` at `68b6df0651f14b2c8ab082635b8d2051918617a2`.
  - Checked with `git rev-parse HEAD`.
  - `git status --porcelain` printed nothing at the end of the pass.
  - No file in any worktree was modified. No git write was run. Nothing was dispatched.
- **SharpTests source.** The base checkout does not contain `SharpTests.lean` (K1-SHARP-TESTS-1, which is landing).
  - It is read from `scratchpad/wt-k1st`, head `e0cf9151` ("K1-SHARP-TESTS-1 Q: the receipt").
  - `68b6df06` is an ancestor of that head.
  - `git diff --stat 68b6df06 HEAD -- verification/lean-mathlib/OIBridge/` shows exactly one added file, `SharpTests.lean` (252 lines).
- **Path convention.** Paths are relative to `verification/lean-mathlib/OIBridge/`. Abbreviations:

  | abbreviation | module |
  | --- | --- |
  | CD | CompositeDimension |
  | NGB | NativeGateBall |
  | ES | EffectSpace |
  | K1B | K1Bridge |
  | K2G | K2Guard |
  | ST | SharpTests (wt-k1st) |
  | OG | OrbitGeneration |
  | ON | OrbitNormalization |
  | KF | KInfFoundations |
  | TB | TransitiveBody |
  | IIP | InvariantInnerProduct |
  | SC | StageCompletion |
  | CA | CompletionAction |
  | CO | CompositionOrder |
  | CI | CompositeInterface |
- **Evidence layers.** They are kept distinct and never substituted for one another:

  | tag | meaning |
  | --- | --- |
  | `[K]` | A kernel identifier at the base (or at `e0cf9151` for ST), with file:line. |
  | `[R]` | A reading of a landed proof: which hypothesis it consumes. This is not a certification. |
  | `[X]` | An exact computation run here: sympy, Rational, symbolic trigonometry, no floats (§6). |
  | `[W]` | A written argument. |
  | `[S]` | An uncompiled Lean sketch, `SingleSystemSelector.sketch.lean`. |
  | `[L]` | Literature from memory, not re-verified in this pass. |
  | `[P]` | Prior off-repo research, cited as data. |
- **Prior notes read.**
  - `twole/TWOLE-LEDGER.md`, `k2d/K2-LEDGER.md`, `sa/SA-LEDGER.md` (§§0–3), `drive/RESULT.md` (§§0–1).
  - `opact/RESULT.md` and `oistage/RESULT.md` were skimmed through the SA ledger's verification of them.
  - Also read, because a corpus search found them: `wave2/R/RESULT.md` (thread R, at base `f7f5c3b0`) and
    `round2/DIM-1-DESIGN.md` rows (b), (c3) and (c5).
- **Thread R is the direct predecessor.** It already contains the single-system "energy observability" (EO) route and the
  "necessity" statement.
  - `f7f5c3b0` is an ancestor of `68b6df06`, and only *added* files lie between them, so thread R's
    file:line citations are still valid.
  - I replayed thread R's `r_checks.py` once. The output was byte-identical: `OK -- 56 checks, 0 failed, 7 written notes`
    (§6).
- **Productivity test (§A.31).** I formulated it before writing the probes and wrote it down after running them. A finding is a gem
  only if both hold:
  - it is strictly stronger than the restatements "K1 needs K2" and "spin-factor balls satisfy the
    single-system vocabulary" (thread R);
  - it either constrains a premise or exposes a hidden assumption.

## 1. Dependency ledger of the current d = 3 chain

**Head of the chain.** `three_of_nativeGateOf_of_two_le` (K2G:253) `[K]`. It assumes `2 ≤ d` together with the hypotheses of the
relative selector `dim_of_nativeGateOf` (K1B:128) `[K]`. `2 ≤ d` is sourced by `HasTwoSharpTests (eball d) ↔ 2 ≤ d`
(`hasTwoSharpTests_iff`, ST:155) `[K at e0cf9151]`.

| # | ingredient | kernel identifier (file:line) | class | role in the count |
| --- | --- | --- | --- | --- |
| 1 | the body | `eball` TB:518; reached from any boundary-transitive compact body by `exists_affine_image_eq_eball` TB:602 / `chartBody_eq_eball` TB:651 | (a) single | the carrier; holds for every `d > 0` |
| 2 | effect soundness | `EffectsOn` ES:567 | (a) | used only inside the cone equality (row 8) |
| 3 | body preservation | `PreservesBody` OG:69 | (a) | same |
| 4 | K∞-Seed | `SharpSeed` OG:65 | (a) | same |
| 5 | K∞-Trans | `BoundaryTransitive` OG:79 | (a) | same |
| 6 | K∞-V4 | `SeedOrbitAvailable` OG:74 | (a) | same |
| 7 | the NOT | `IsNot` CD:210: `unit`, `invol`, `preserves`, `flips` | (a) | `unit` gives `0 < d` (`pos_of_isNot` CD:2712). `invol` gives `p_hom + m_hom = d + 1` (`finrank_plus_add_finrank_minus` CD:274). `flips` gives `m_hom ≥ 1` (CD:306). Self-adjointness for `toOp_actT` (CD:464) through `homMap_dot` CD:395 |
| 8 | cone equality (bridge) | `maxConeOf_avail_eq` ES:572, via `sharpFamily_subset_avail` ES:374 and `maxConeOf_sharpFamily` ES:549; used by `nativeGate_of_cone_eq` K1B:73 and `nativeGate_of_avail` K1B:108 | **mixed**: single-system hypotheses, conclusion about the two-copy object `maxConeOf` ES:411 | rewrites `maxConeOf avail` to `maxCone (eball d)`. Contributes no number |
| 9 | carrier | `HVec` CD:93 (one-copy chart, convenience), `W d` CD:97 | (b) composite | the two-copy space `(d+1)²` |
| 10 | products | `prodState` CD:161, `pairVal` CD:164, `ehom` CD:167, `prodEffVal` CD:182 | (b) | product preparations and product tests (ProductData, K2-LEDGER §1.2) |
| 11 | cones | `maxCone` CD:186, `jointStates` CD:190, `maxConeOf` ES:411 | (b) | the positivity target |
| 12 | local lifts | `actT` CD:198, `actC` CD:201 | (b) | `N ⊗ I`, `I ⊗ N` on `W d` |
| 13 | the gate | `NativeGateOf` K1B:49 (`frame`, `posFwd`, `posInv`, `relT`, `relC`) ⇒ `NativeGate` CD:218 | (b) | carries both decisive facts below |
| 14 | **parity balance** `p_hom = m_hom` | `finrank_plus_eq_finrank_minus` CD:682 ← `NGB.parity` NGB:194, `Lop` CD:552, `Lop_injective` CD:615, `Lop_anti` CD:562, `opGate_comp_homMap` CD:494, `opGate_homMap_comp` CD:503 | (b): consumes `relT`, `relC` on `W d` `[R]` | excludes every even `d` |
| 15 | **block bound** `p_tan ≤ 1` | `blockData_of_nativeGate` CD:2703 ← `tens_mem_maxCone` CD:1608, `gate_corner` CD:1885, `gt_center` CD:1990, `tangent_vanish` CD:2051, …; `p_le_one_of_blockData` CD:722 ← `NGB.p_le_one` NGB:176 | (b): consumes `posFwd` on `maxCone` and the frame `[R]` | excludes `d ≥ 5` |
| 16 | the count | `NGB.dim_of_bounds` NGB:248 (`p ≤ 1`, `p = q`, `p + q + 1 = d ⇒ d ∈ {1,3}`) | pure arithmetic | — |
| 17 | `d ≠ 1` | `2 ≤ d` (K2G:253), sourced by `HasTwoSharpTests` ST:41/155 | (a) | excludes the classical bit |
| 18 | (alternative to 17) | `Entangling` CD:229 / `EntanglingOf` K1B:64, consumed only through `not_entangling_one` CD:1436 | (b) | the same exclusion, composite form |

**Reading `[R]`.** The count has three inputs.
- One is single-system: `p + q + 1 = d`, from `IsNot.invol`.
- Two are composite: parity balance (row 14) and the block bound (row 15).
- **Every exclusion of a `d ≥ 2` other than 3 is composite-sourced.**
- The single-system rows 2–6 enter only to make the product-test cone of the available family equal to `maxCone`
  (row 8). That is a two-copy object, so they cannot select `d` by themselves.
- The single-system inputs give exactly `0 < d` (row 7) and `2 ≤ d` (row 17).

## 2. d-genericity audit of the landed single-system ingredients

### 2.1 The uniform countermodel family (decisive negative)

**Statement.** For every `d ≥ 2`, take:
- `avail = fullEffects (eball d)`;
- `G = fullAut d` (ES:227);
- `r = sharpEff (axisVec)`;
- `z = axisVec`;
- `N = reflLin axisVec`, which is `diag(−1, 1, …, 1)`.

These satisfy `EffectsOn`, `PreservesBody`, `SharpSeed`, `BoundaryTransitive`, `SeedOrbitAvailable`, `IsNot` and
`HasTwoSharpTests` on `eball d`, which are all single-system hypotheses of the current selector. So
**no conjunction of them implies `d = 3`**; the instance `d = 4` refutes it.

- **Layer.**
  - The assembly is `[S]` (`singleSystem_uniform`, `singleSystem_not_select` in the sketch).
  - It mirrors the landed `d = 1` template `two_le_load_bearing_relative` (ST:185) term for term.
  - Every conjunct is a landed lemma `[K]`:

    | conjunct | landed lemma |
    | --- | --- |
    | `PreservesBody` | `preservesBody_fullAut` ES:230 |
    | `SharpSeed` | `sharpEff_sharpSeed` ES:118 with `axisVec_sq` ES:431 |
    | `BoundaryTransitive` | `boundaryTransitive_fullAut` ES:337 |
    | `SeedOrbitAvailable` | `isEffectOn_seedTransport` OG:94 |
    | `IsNot` | `reflLin_reflLin` ES:269, `reflLin_sq` ES:277, and a one-line `reflLin m m = −m` |
    | `HasTwoSharpTests` | `hasTwoSharpTests_of_two_le` ST:137 |

  - The only new term is the `IsNot` instance. It is uncompiled.
- **Exact check `[X]`, P1.** Run at `d ∈ {1, 2, 3, 4, 5, 7}`. 92 checks, 0 failed.
  - Sharp effects are effects, through the identities `1 − sharpEff b x = (|b−x|² + 1 − |x|²)/4` and
    `sharpEff b x = (|b+x|² + 1 − |x|²)/4` (A1–A2).
  - The certain face is a singleton (A3).
  - The seed takes the values 1 and 0 (A4).
  - `N` is an orthogonal involution that flips `z` (B1–B4).
  - The Householder map from `e0` to a rational unit `u` is in `fullAut`, and the seed transport is `sharpEff u` (C1–C3).
  - The two-sharp-tests witness takes the values `(1, 1/2, 0)` (D1, for `d ≥ 2`).

This sharpens the landed `two_le_not_implied` (ST:197, `d = 1`) to every `d`: **the selector's single-system hypotheses
give no upper bound on `d`.** It confirms thread R's necessity item (R §5.5) at the new base, for the relative selector
and with the new modules.

### 2.2 The rest of the landed single-system vocabulary

| ingredient (file:line) | holds on `eball d` for | layer | selects? |
| --- | --- | --- | --- |
| TRB-1 ball theorem `exists_affine_image_eq_eball` TB:602, `eq_qBall_of_boundaryTransitive` TB:457 | every `d > 0` | `[K]` | no |
| boundary transitivity | every `d ≥ 1` (`fullAut`); also `boundaryTransitive_ball4` ON:735 (`EuclideanSpace ℝ (Fin 4)`) | `[K]` | no; ON's own control says it "does not fix dimension three" |
| sharp seeds and sharp tests; `sharp_eq_of_certain` ES:181; `sharpSeed_iff` ST:63 | `d ≥ 1`; two tests `⇔ d ≥ 2` | `[K]` | lower bound 2 only |
| EFF-1 effect set `effect_eq_affine` ES:600, `fullEffects_eq_unitSpan` ES:707, `avail_eq_fullEffects` ES:727 | `d > 0` | `[K]` | no |
| (SEC), (SF), `RelStrictConvex`, `KInf1` (KF:135/139/144/1013) | every `d ≥ 1` (Euclidean balls are strictly convex; certain face of `sharpEff u` is `{u}`) | `[X]` P1 A3 + `[W]`; kernel only at `ball3` (`kInf1_ball3_full` KF:1076) and for `StrictConvexSpace` closed balls (KF:658) | no |
| capacity ≤ 2 | every centrally symmetric body | `[K]` `card_le_two_of_centrallySymmetric` KF:632 | no |
| IIP-1 `invariant_inner_product` IIP:336, `centroid_fixed` IIP:152 | every body with interior | `[K]` | no ("no dimension is claimed", IIP header) |
| CMP-1 (`SCInf` SC:78, `FiniteRank` SC:299, `BinaryVisible` SC:244), OPACT-1 (`OpDatum`, `AffineRespect`, `inducedEquiv` CA:333) | body-independent | `[K]` (definitions) | no: they mention no body shape |
| ORD-1 `OrdInf` | `d ≥ 2` (rotation by one radian in a plane); kernel instance `ordInf_singleton_rot3` CO:447 | `[K]` at 3, `[W]` otherwise | no |
| countable no-go `not_boundaryTransitive_of_countable` ES:858 | stated at `eball 3`; `[W]` for every `d ≥ 2` | `[K]`/`[W]` | no (a constraint on sourcing, not on `d`) |
| **K∞-Drive** `ElementaryDrivability` KF:264 | **`d ≥ 3` only** (bounded bodies) | `d ≥ 3`: `[X]` P1 E1–E4 (rotation flow in plane (0,1), `t₀ = π`, `J` = cyclic permutation of axes 0, 1, 2, off-axis witness `e₂`), `[K]` at `d = 3` (`ball3_drivable` KF:490). `d = 2`: `[X]` E5 (every `J ∈ O(2)` conjugates `R(t)` to `R(±t)`) + `[W]` (`Aut(eball 2) = O(2)`); thread R's B6 (needs boundedness, which holds here). `d = 1`: `[K]` `not_drivable_Icc` KF:529 | **lower bound 3; no upper bound** |

**Net.** At `68b6df06`, every landed single-system item holds on `eball d` for every `d ≥ 3`. All of them except
`ElementaryDrivability` also hold at `d = 2`. `ElementaryDrivability` is not a hypothesis of the current chain. **Strongest exact negative:**

> Fix any conjunction of the landed single-system predicates, instantiated on `eball d` with the uniform family of
> §2.1 together with the plane-rotation drive. That conjunction holds for every `d ≥ 3`, so it cannot select `d = 3`.

- **Exact.** P1 at `d = 3, 4, 5, 7`.
- **Kernel-assembled sketch.** `singleSystem_uniform` for all `d ≥ 2`; the drive part is written for general `d`.
- **Consequence.** A composite-free selector needs a **new premise that the balls `eball d`, `d ≥ 4`, violate** (thread R's
  necessity, re-established here for the current vocabulary).

## 3. Literature check (all `[L]`, from memory, not re-verified here)

| source | where `d = 3` comes from | single-system? | what it smuggles |
| --- | --- | --- | --- |
| Hardy 2001 (five axioms) | `K = N^r` from the composite axiom `K_AB = K_A K_B` and the subspace axiom; `r = 2` by simplicity; `K = 4` at `N = 2` | no | composites (LT counting) and simplicity |
| Dakić–Brukner 2009/2011 | the `d`-ball from one-bit information content; `d = 3` from LT and continuous reversible entangling dynamics of two gbits | no | LT and composite reversibility |
| Masanes–Müller 2011; Masanes–Müller–Augusiak–Pérez-García 2013 (PNAS) | two `d`-ball gbits with LT admit a non-trivial continuous reversible interaction only for `d = 3` | no | LT and an interaction |
| Müller–Masanes 2013 (3D space and the qubit) | `d = 3` tied to spatial rotations through interaction with observers | no | interaction/composite (a spatial `SO(3)`) |
| Chiribella–D'Ariano–Perinotti 2011 | purification | no | purification is composite |
| Höhn 2017; Höhn–Wever 2017 | question-counting rules plus a two-gbit tomographic-locality rule | no | composite |
| Brukner–Zeilinger information invariance; one-bit capacity | holds for every ball (thread R I1; KF:632) | yes | selects nothing |
| self-duality, strong symmetry, bit symmetry (Müller–Ududec 2012), homogeneity, no higher-order interference, transitivity on pure states, "every pure state reachable by a continuous reversible transformation" | all hold for every spin-factor ball `V_d` (the reversible group is `SO(d)`, transitive for `d ≥ 2`) | yes | selects nothing (consistent with §2) |
| **Barnum–Müller–Ududec 2014 (NJP 16 123029)** | classical decomposability, strong symmetry and no third-order interference give Jordan state spaces, all spin factors included; **observability of energy** removes real, quaternionic and spin-factor theories except the qubit | **yes** | the dynamical correspondence (generators ↔ observables), the single-system fingerprint of ℂ |
| **Alfsen–Shultz (dynamical correspondence, 1998); Alfsen–Hanche-Olsen–Shultz 1980 (state spaces of C\*-algebras)** | a JB-algebra admits a dynamical correspondence iff it is the self-adjoint part of a C\*-algebra. The C\*-state-space characterization *assumes* the "3-ball property" for faces generated by two pure states, plus an orientation | yes | `d = 3` is *assumed* there (3-ball property), and the orientation is the extra structure that picks the complex structure (`i` vs `−i`) |
| `PU(2)` / `SU(2)` adjoint action; pure states as `ℂP¹ ≅ S²` (Hopf) | put the reversible group, or the pure-state space, equal to that of ℂ² | yes | ℂ² directly |

Two kinds of fact are kept apart here. The literature result is that no single-system principle satisfied by every spin factor fixes
`d`. The written derivation below is an elementary consequence of standard Jordan-algebra facts, not a re-verified citation:

- the spin factors `V_n` (state space `eball n`) for `n ≥ 2` are simple of rank 2;
- the self-adjoint part of a simple finite-dimensional complex C\*-algebra is `M_k(ℂ)_sa`, of rank `k`;
- hence **`V_n` is the self-adjoint part of a complex C\*-algebra exactly for `n ∈ {0, 1, 3}`**: `ℝ`, `ℝ ⊕ ℝ` and `M_2(ℂ)_sa`.

## 4. Candidate composite-free selector: UE (a proposal, not adopted)

### 4.1 Statement, in the landed vocabulary (the sketch, Part 2)

```
BodyFlow Ω            -- the flow fields of ElementaryDrivability (KF:264): group law, joint continuity,
                         preservation of Ω
Conserved φ e         := ∀ t x, e (φ.flow t x) = e x
UniqueEnergyTest Ω    := every nontrivial BodyFlow conserves a sharp seed e, and every conserved sharp seed
                         agrees with e or with 1 − e on Ω          (test identity = agreement on Ω, TWO-LE G1)

uniqueEnergyTest_eball_iff : UniqueEnergyTest (eball d) ↔ d ≤ 1 ∨ d = 3
three_of_twoSharp_uniqueEnergy : HasTwoSharpTests (eball d) → UniqueEnergyTest (eball d) → d = 3
```

The corollary uses no `W d`, no `NativeGateOf`, no product cone and no `IsNot`.

### 4.2 Proof sketch (`[W]`, with `[X]` at the decisive points)

**(→), the exclusions.** Both are kernel-cheap once a `d`-dimensional plane-rotation flow is defined, generalizing `rot3`, KF:411.
- **`d = 2`.** A conserved `sharpEff u` needs `R(π/2)ᵀu = u`, so `u = 0`. That contradicts `|u| = 1` `[X]` (P2 L1).
- **`d ≥ 4`.** The rotation flow in the plane (0, 1) conserves `sharpEff e₂` and `sharpEff e₃` (symbolic `t`) `[X]` (P2 L2).
  At `x = e₂` they take the values `(1, 1/2, 1 − 1 = 0)`, so they are separated modulo complementation `[X]` (P2 L3).
- **Generator form.** `dim ker J₀₁ = d − 2` `[X]` (P2 K1). So a one-dimensional kernel for the single-plane generator occurs exactly at `d = 3`
  (d = 2…9).

**(←), the cases that hold.**
- **`d ≤ 1`.** There is no nontrivial body flow: `eball 1` has the automorphisms `±id`, a continuous flow starts at `id`
  (`flow_zero_of_add` ON:B1), and `isEmpty_drivability_of_finite_orbits` ON:124 is the template `[W]`.
- **`d = 3`.** The argument is `[W]` and uses no Lie structure theory:
  1. Body automorphisms are linear (the centroid is fixed, `centroid_fixed_of_preservesBody` TB:356) and orthogonal.
  2. Every flow member has `det = 1` by continuity.
  3. Pick a nontrivial member that is not a half-turn. If `φ_t` is a half-turn, `φ_{t/2}` is a quarter-turn. Its fixed space is a line `ℝw`.
  4. Every member commutes with it, so it preserves `ℝw`. The sign `φ_t w = ±w` is continuous and starts at `+`, so `w` is
     conserved.
  5. A second conserved unit `u ≠ ±w` would make every member fix `w`, `u` and `w × u`, so every member would be the identity.
- **Generator-level check `[X]`** (P2 M1–M3). For every nonzero `X ∈ so(3)`, `X = hat(w)` has rank 2: the sum of the squared 2×2
  minors is `(w·w)²`. The kernel is `ℝw`.

### 4.3 Premise it needs (named, not adopted)

**P-UE.** Every nontrivial continuous reversible dynamics of the elementary system has exactly one stationary sharp
binary test, up to complementation. In other words, its stationary pure states form exactly one antipodal pair.

P-UE must quantify over **all** continuous flows of the reversible group. There are two forms:
- **P-FNR form.** Every continuous flow of body automorphisms is a physical dynamics. Under this form the proof above is
  elementary.
- **Closure form.** Quantify over the one-parameter subgroups of the closure of the available boundary-transitive family. The
  exclusions then need the Montgomery–Samelson–Borel classification of transitive actions on spheres `[L]`:
  - every even `d` has a fixed-point-free circle;
  - `SO(2k+1)` with `k ≥ 2` has a single-plane flow;
  - `G₂` at `d = 7` has a flow with a 3-dimensional kernel.

**Load-bearing countercontrol `[X]`** (P2 P1–P4) at `d = 5`:
- Take the conjugation class of the generic flow `X₁ = J₀₁ + √2 J₂₃`. Every member has a 1-dimensional kernel, so UE holds member by member.
- The conjugate `X₂ = J₀₁ − √2 J₂₃`, by `diag(1,1,1,−1,−1)` with `det = +1`, commutes with `X₁`.
- The commuting product of their flows has generator `2J₀₁`, whose kernel has dimension 3.
- The closure of the generated group is `SO(5)` `[W]`, which is transitive.
- So UE stated only on available generators passes at `d = 5`. **FNR, or a closure clause, is load-bearing.** That clause is LIMCLOSE-type (drive note,
  SA §3.2), which no landed object supplies.

### 4.4 Skeptical assessment of this favourable branch (§A.31, §A.29)

1. **It is an equivalent reformulation, not a source.** On balls, with FNR, `UE ⇔ d ∈ {0, 1, 3}`. With `2 ≤ d` it is
   `⇔ DIM3`. Like EO (thread R §5.1), it trades DIM3 for an equally strong unsourced premise.
2. **It is worse than EO as an explanation.**
   - UE is elementary-scoped. It is false for the qutrit: a nondegenerate qutrit Hamiltonian conserves three inequivalent binary
     projector tests `[W]`.
   - So UE makes no postdiction beyond the elementary system, and fails §A.29's "beyond the problem it was built to
     fix" criterion.
   - EO holds for all complex QM (thread R §5.2). UE's advantages are practical only: the proof is elementary under FNR
     (no rank-1 classification, which thread R's step 8 needs and Mathlib lacks), and orientation needs no clause (item 3).
3. **Orientation.**
   - The improper symmetries of a flow (`σ = diag(1,1,−1)` and `−I`, both `det = −1`, both commuting with `R_z(t)`) carry
     the conserved test to its **complement** `[X]` (P2 O1).
   - At Lie level, `g hat(v) gᵀ = det(g) hat(gv)` `[X]` (P2 O2, including `reflY` of K2G:46). This is thread R's
     "wrong-way failure" of full-group EO.
   - So a test-level, modulo-complement formulation is orientation-blind by construction: uniqueness makes the energy test
     canonical, and the orientation sign appears as complementation.
   - This is a property of the single-system formulation only. It is **not** identified with K2-GUARD's composite orientation
     obstruction (`no_candidateCone_cnot_reflY` K2G:143). The two share the ingredient "an improper body automorphism",
     and no formal map relates them.
4. **ℂ in disguise.**
   - The stationary set of a generator `X` is `ker X`. "`ker X` is a line for every `X ≠ 0`" is the hat-map coincidence
     `so(3) ≅ ℝ³`, the same coincidence EO's step 6 uses ("centralizers are lines").
   - UE is the elementary-level shadow of the dynamical correspondence. It does not *derive* ℂ; it is the place where ℂ would enter.
   - Within the stated scope it is field-neutral in letter.
5. **Variants with the same lever.**
   - Under FNR, "the stabilizer algebra of a pure state is nonzero and abelian" also selects exactly `d = 3` among
     `d = 2…7` `[X]` (P2 S1).
   - Thread R's (d4) refuted this *without* FNR (`U(2)` on `B⁴`).
   - What is load-bearing in every such selector is the premise that fixes the reversible group relative to `d`: FNR,
     or EO's equivariant correspondence. The "smallness" clause on top of it is interchangeable.

**Status.** UE is a candidate theorem with an elementary proof plan. It is a reformulation, not a source, and is not
recommended over EO as the named single-system premise. Its use is as a cheap certifiable control if the owner ever
wants a kernel statement of the single-system route.

## 5. Gem-finding: what the K1 ↔ K2 coupling exposes

| # | finding | class | layer | why |
| --- | --- | --- | --- | --- |
| G1 | The number 3 in the current chain is carried entirely by two composite facts: parity balance (`relT`/`relC` on `W d`, CD:682) and the block bound (`posFwd` on `maxCone`, CD:2703). The single-system rows contribute only `0 < d`, `p + q + 1 = d` and `2 ≤ d`. Every single-system hypothesis of the selector holds uniformly at all `d ≥ 2` (§2.1). | CONFIRMING (thread R necessity; K2-LEDGER) + ELABORATING (line-level at `68b6df06`, relative selector, SharpTests, uniform instance) | `[R]`, `[S]`, `[X]` | sharper than "K1 needs K2" and constrains nothing new |
| G2 | No landed single-system item selects `d = 3`. Drivability gives `d ≥ 3` (bounded), sharp tests give `d ≥ 2`, and everything else is `d`-generic (§2.2). A composite-free selector needs a premise that `eball d`, `d ≥ 4`, violates. | CONFIRMING (thread R §5.5), re-established on the new modules | `[K]`, `[X]`, `[W]` | — |
| G3 | **Hidden assumption: the "dimension" selector is a field selector.** `d = 3` = two-level (ball, TRB-1 `[K]`) ∧ non-classical (`HasTwoSharpTests` `[K]`) ∧ **complex type**. The last conjunct has no landed single-system source. DIM-1's output set `{1, 3}` coincides with `{d ≥ 1 : V_d` is the self-adjoint part of a complex C\*-algebra`}` (§3, `[L]+[W]`). For the natural level-exchange NOT, DIM-1's parity balance holds exactly over the classical bit and ℂ, and fails over ℝ, ℍ and 𝕆 (splits `(2, k)`, `k = dim_ℝ 𝔽`) `[X]` (P3). The block bound does no work for that NOT (`p_tan = 1` for all `k ≥ 1`); it only excludes exotic balanced NOTs (P1 F3). The K2-LEDGER real-QT countercontrol (rebits meet every DIM-1 relation on their own carrier and fail only PTQ) fits the same reading. **Assumption-watch AW-SS-1:** any composite-free replacement for K1's selector must supply complex type, and any composite one carries it through LT/PTQ. | **NEW (assumption-watch)**, BORDERLINE in strength | `[X]` + `[W]` + `[L]` | It is a coincidence of output sets on the ball family plus one exact split computation. **No formal map** identifies DIM-1's hypotheses with complex type, and none is claimed. It exposes what the K1 → K2 coupling is coupling. |
| G4 | Every single-system selector has the same lever. It must fix the reversible group relative to `d`, either by FNR / closure (UE, abelian stabilizer) or by an equivariant generator ↔ observable map (EO). The smallness clause is interchangeable. The closure clause is load-bearing (exact `d = 5` countercontrol P2 P). | ELABORATING (sharpens thread R's d3/d4 rows) | `[X]` + `[W]` | it constrains: the countable families the towers supply cannot carry any such selector without a LIMCLOSE-type closure (SA §3.2) |
| G5 | Test-level, modulo-complement formulations are orientation-blind. The Lie-level sign `det(g)` appears as complementation (P2 O). Thread R had to restrict EO to `Ḡ⁰`; UE needs no clause. | POSITIVE (a design constraint for any future single-system statement), ELABORATING | `[X]` | no bridge to K2-GUARD claimed |
| G6 | A NOT that lies on a reversible flow (`det N = +1`, as the drive's NOT does), together with DIM-1's balance, gives `d ≡ 3 (mod 4)`. With the block bound it gives `d = 3` without `2 ≤ d`: the classical bit is excluded by orientation, `det(neg1) = −1` (P1 F2, F4). This is composite-dependent (balance and block come from DIM-1). | ELABORATING (minor) | `[X]` bookkeeping + `[R]` | records that "the NOT is a dynamics" is a single-system alternative to `2 ≤ d`, given the composite chain |
| G7 | UE: an elementary-proof, composite-free candidate selector (§4), equivalent to DIM3 under FNR and `2 ≤ d`. | BORDERLINE (an equivalent reformulation; fails the §A.29 postdiction test, which EO passes) | `[S]` + `[X]` + `[W]` | not a source |

**Verdict on composite-free selection.**
- **With the landed vocabulary: no.** The exact countermodel family `eball d`, `d ≥ 4` (and `d = 2` without the drive)
  satisfies every landed single-system hypothesis.
- **With one new premise: yes, but only as a reformulation.**
  - The premise is EO (thread R) or UE + FNR/closure (here).
  - Each is equivalent to DIM3 given the drive and `2 ≤ d`.
  - Each is unsourced and is the single-system fingerprint of ℂ.
- The coupling of K1 to K2 is therefore not removable by single-system data already in the kernel. It is
  the coupling of field selection to composite structure (G3).

**Fixed point (§A.31).** This was one depth-first pass, and it produced one NEW finding (G3). The fixed point is not reached.
The next pass should start at G3:
- **Next step for G3.** State and test whether DIM-1's parity step with the *level-exchange* NOT, read on a general two-level
  𝔽-system, is equivalent to `dim_ℝ 𝔽 = 2`. That is a candidate formal map, with both directions to be witnessed separately (§A.34).

**Correctness/consistency (§A.23).** This is consistency-axis work only. The bands are unchanged.

## 6. Probe log

All probes are in `scratchpad/ss/`. Each was run as `python3 -I <script>` from that directory and replayed once. Replays were compared with `cmp`.
Hashes are full sha256.

| probe | script (sha256) | output (sha256) | result | replay |
| --- | --- | --- | --- | --- |
| P1 uniform countermodel family | `p1_countermodel.py` (`1259731610c2439e99489cce5d9997a72c229d8b3599394dcbc09e2f757a0592`) | `p1_countermodel.out` (`77fb69da8d02a6fb49ed0def70073feba36cbfe9f9c7534a95b2ad186d925f0e`) | `SUMMARY 92 checks, 0 failed`; VERDICT rendered | `p1_countermodel.replay.out`, identical |
| P2 UE selector | `p2_unique_energy_test.py` (`3a3a4d947f7ce2312f3b59e7853a87226b394bb2af9f610980f503f1030258ba`) | `p2_unique_energy_test.out` (`9a9e2508afa8b3f63b40336c46ce091c4ff3dbb4d16a3f05976f2d786acf6478`) | `SUMMARY 31 checks, 0 failed`; VERDICT rendered | `p2_unique_energy_test.replay.out`, identical |
| P3 field splits | `p3_field_splits.py` (`e41c752a99b5d933628d0526ca09e2e534628db08787aa3165a1e7a8d869f254`) | `p3_field_splits.out` (`e973a0ff341cbdca3c0c6c268098ed689b45fbe1d371b4cb289cab8bf337d031`) | `SUMMARY 7 checks, 0 failed`; VERDICT rendered | `p3_field_splits.replay.out`, identical |
| thread R replay | `../wave2/R/r_checks.py`, unmodified (`fff52b1564f19d0737f6454d0695f5272f3de028d0aa976e699d228bfc8ef8e0`) | `replay_threadR.out` (`e55cf6ac2d583d8a4ff2e6e1076d0324e33c054b58b08056cc0346c48dedfc94`) | `OK -- 56 checks, 0 failed, 7 written notes` | identical to `../wave2/R/r_checks.out` |
| Lean sketch | `SingleSystemSelector.sketch.lean` (`7b17720b4fa4ca9365005dcc5b60e0ed084bde2863408881d05f280ad9daa25f`) | — | uncompiled (no toolchain) | — |

**Run record.**
- **P2, first run (kept only as this note).** The first draft padded section S with six unconditional `CHECKS.append(…, True)` rows, which inflated the
  count to 37. They were removed as non-checks before the recorded run. The decisive check S1 was unchanged.
- **P3.** P3 is near-definitional: the split `(2, k)` is immediate. Its countercontrols are the ℝ, ℍ and 𝕆 rows. The interpretive step (G3) is
  `[W]`.

**Written steps that the exact checks do not cover.**
- `Aut(eball d) = O(d)`.
- Every continuous flow of `SO(3)` is a rotation flow about one axis (§4.2).
- `d ≤ 1` has no nontrivial flow.
- The closure of the `d = 5` conjugation class is `SO(5)`.
- The Montgomery–Samelson–Borel case analysis.
- The Jordan-algebra classification in §3.
- The qutrit counterexample to unscoped UE.

## 7. What is not claimed

- No kernel theorem is claimed. The sketch is uncompiled.
- Neither UE nor EO is proposed as adopted, and neither is sourced.
- No identification of DIM-1's hypotheses with complex type (G3 is a coincidence of output sets plus one exact split).
- No bridge between UE's orientation-blindness and K2-GUARD's obstruction.
- No ROADMAP or manuscript wording.
