# Reconstruction round KINF-COPY-1 — type covariance of native inversion suffices for DIM-1's selector, with positivity on the maximal cone or on the cone of the available tests: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** It is drafted from `D` and
built from three sources:
- the design module `CopyCovariance.lean` (Git blob `fb9c73fe`, commit `8c92343e` on `dev-equivalence/split-l3`),
  the predicted module of the earlier draft of this round;
- the design module `RelativeGateTransport.lean` (Git blob `507ac329`) and the exact probe `relgate_counter.py` (blob
  `10a02005`), compiled and replayed at commit `c9f16498`, which is reachable from
  `research/pair-interface-design-20261014`;
- the exact probe `research/equivalence/experiments/e2_copy_conj.py` (blob `481fbf7c`, sha256 `c28e1b97…`) on
  `research/equivalence`.

These are off `main` and are cited as provenance only (AGENTS §A.42). No claim of this file rests on them alone: the
design evidence the decision rules consume is the pre-`F` run of the predicted execution tree at `D` (*Design
evidence*), which is not yet taken. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an
instruction to proceed is not a designation.

```v3-round
round KINF-COPY-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/
record AM verification/receipts/KINF-COPY-1.json
execution A verification/lean-mathlib/OIBridge/CopyCovariance.lean
execution A verification/lean-mathlib/OIBridge/RelativeGateTransport.lean
execution A verification/lean/kinf_copy1_probe.py
execution A verification/lean/kinf_copy1_relative_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: b96662e6be4f537502c772db369ea32a35b213a8.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, `verification/ROADMAP.md`, landed kernel module or other round's record changes under any outcome.**

Measured at `D`:
- every landed object cited below is at the line given, and none of their modules changed between `dee3b5ae` and `D`
  (89 commits; under `verification/lean-mathlib/` they add `TurnpikePremiseOrientation`, change
  `TurnpikeScopeTransfer` and add one import line) or between the design base `5bfdaba6` and `D`;
- the last import line of `OIBridge.lean` is `import OIBridge.TurnpikePremiseOrientation` (:269);
- the census tail is the BG-2 family (census :1485–1492);
- in `verify.yml`, BG-2's shard ends at :459–460 and the aggregate's `needs`, env, echo and test lines for BG-2 are
  :557, :577, :598 and :618;
- the K∞-Copy entry of `verification/ROADMAP.md` is :1040–1043.

## The relative form

The F2 decision memo (`research-planning/f2-decision-memo.md` on `plan/f2-target-extension-scope-20261017` at
`362131e0`, §5.1, row #822) records this round as "type covariance of native inversion suffices for DIM-1's selector
… relative form `RelativeGateTransport` run 38606561330 [CD]", depending on "none of (a)–(d)", and keeping explicit
the "integration of the relative gate with available tests, and its cone hypotheses". The planning note it cites
(`f2-target-extension-scope.md` :44) lists for #822 "available-test relative-gate integration and its cone
hypotheses".

In this file the **relative form** is therefore:
- the two-NOT hypotheses `NativeGate2Of Ω avail z NC NT T`, which are `NativeGate2` with `maxConeOf avail` in place of
  `maxCone Ω` in the two positivity clauses, as K1-BRIDGE-1's `NativeGateOf` (K1Bridge.lean:49) is DIM-1's
  `NativeGate` (CompositeDimension.lean:218);
- each cone hypothesis that moves data between the two forms stated as a named premise, one per direction;
- every claim stated as an implication from hypotheses written out in its statement.

No statement, rule or control of this round reads an F2 choice. It adopts no target (qubit-power registers or all
finite local dimensions, exact or dense), no extension gate, no preserved-law scope and no necessity scope; `d`, `Ω`
and `avail` are arbitrary wherever the statements allow.

## What the round is

K∞-Copy (ROADMAP :1040–1043) is copy naturality: DIM-1's `NativeGate` reads one NOT `N` in both relations, so the NOTs
of identical copies agree. The two-NOT J/K maps at `d = 5, 7` (NB-1 records) meet every two-copy relation with
mismatched NOTs. The ROADMAP records an untested candidate: the frame-preserving conjugacy class of the native
inversion is fixed by system type. At `D` the K1 entry (ROADMAP :68) states the native-gate hypotheses on the cone of
the available tests (`NativeGateOf`, `dim_of_nativeGateOf` K1Bridge.lean:128). The round asks five questions, each read
by its own rule:

- **Q-RED (kernel, maximal form).** Under `NativeGate2 Ω z NC NT G`, does conjugation on the target copy by a linear
  body automorphism fixing the corner axis give two-NOT data with the target NOT conjugated? When `NT` is the conjugate
  of `NC` by such an automorphism (*type covariance*), is the conjugated gate a one-NOT native gate, so that DIM-1's
  selector gives `d = 1 ∨ d = 3`, and `d = 3` with `2 ≤ d`, also for a conjugator reversing the corner axis?
- **Q-REL (kernel, relative form).** Under `NativeGate2Of Ω avail z NC NT T`:
  - does `maxConeOf avail ⊆ maxCone Ω` carry the relative data to the maximal data, and `maxCone Ω ⊆ maxConeOf avail`
    the maximal data to the relative data, each by its own theorem?
  - does the cone equality give the conjugacy results in relative form?
  - do K1-BRIDGE-1's hypotheses, KTRANS-DENSE-1's, or the orbit hypotheses alone give the selector?
  - does copy naturality's conjugation identity give the covariance clause `hcov`?
- **Q-POS (kernel, positive controls).** At `d = 3`, is there two-NOT data with `NT ≠ nflip`, maximal and relative,
  with every hypothesis of the relative selector holding for one available family?
- **Q-EXACT (exact layer).** Do the exact instances behave as the theorems state, and do the two J/K maps at `d = 5, 7`
  violate type covariance?
- **Q-COUNTER (exact layer).** Is there, for an effect-sound family whose cone strictly contains the maximal cone, a
  gate meeting the relative one-NOT hypotheses that is not a native gate?

## The hypotheses, named once

| name | content (as in the statements) |
|---|---|
| **N2** | `NativeGate2 Ω z NC NT G`: frame; `posFwd`, `posInv` on `maxCone Ω`; `relT` with `NT`; `relC` with `NC` on the control side and `NT` on the target |
| **N2-rel** | `NativeGate2Of Ω avail z NC NT T`: as N2 with `maxConeOf avail` in both positivity clauses |
| **CONJ** | `g h` linear with `hgh : ∀ x, g (h x) = x`, `hhg : ∀ x, h (g x) = x`, `hgΩ`, `hhΩ` (both maps preserve `Ω`), and `hgz : g z = z` (or **CONJ⁻**: `hgz : g z = -z`) |
| **TC** | type covariance: CONJ (or CONJ⁻) with `hcov : ∀ x, NT (g x) = g (NC x)` |
| **NOT** | `IsNot (eball d) z NC` (CompositeDimension.lean:210) |
| **INC** | `maxConeOf avail ⊆ maxCone Ω` |
| **SUP** | `maxCone Ω ⊆ maxConeOf avail` |
| **EQ** | `maxConeOf avail = maxCone Ω` |
| **EFF** | `EffectsOn Ω avail` (EffectSpace.lean:567) |
| **ORB** | `PreservesBody (eball d) G`, `SharpSeed (eball d) r`, `BoundaryTransitive (eball d) G`, `SeedOrbitAvailable G r avail` (OrbitGeneration.lean:69, :65, :79, :74): K∞-Trans, K∞-Seed and K∞-V4 with body preservation |
| **ORB-dense** | ORB with `DenseBoundaryOrbit (eball d) G` (DenseOrbit.lean:53) in place of `BoundaryTransitive` |
| **K1B** | `0 < d`, EFF on `eball d` and ORB: the hypotheses of `maxConeOf_avail_eq` (EffectSpace.lean:572), which give EQ on `eball d` |
| **K1B-dense** | `0 < d`, EFF and ORB-dense: the hypotheses of `maxConeOf_avail_eq_of_dense` (DenseOrbit.lean:243) |
| **CN** | `CopyNatural eC eT eg` (KInfFoundations.lean:284) for affine equivalences whose coercions are `NC`, `NT`, `g` |

## The claims, what each is relative to, and its witnesses

Status at `D`: every new declaration is compiled design [CD], not adopted. Under a positive cell at `E` it is a kernel
theorem of the implication shown, from exactly the hypotheses in its statement. No row sources a hypothesis.

| # | statement | relative to | witness (per direction where two) | landed theorems it consumes | status if positive at `E` |
|---|---|---|---|---|---|
| M1 | conjugation on the target copy preserves two-NOT data, with `NT` replaced by `h ∘ₗ NT ∘ₗ g` | N2, CONJ | `nativeGate2_conj` | `actT_prodState` K2Guard.lean:173 | proved |
| M2 | the conjugated gate is a one-NOT native gate with `NC` | N2, TC | `nativeGate_of_conj` | — (via M1) | proved |
| M3 | `d = 1 ∨ d = 3` | NOT, N2 on `eball d`, TC | `dim_of_nativeGate2_conj` | `dim_of_nativeGate` CompositeDimension.lean:2723 | proved |
| M4 | `d = 3` | M3's, with `2 ≤ d` | `three_of_nativeGate2_conj_of_two_le` | `three_of_nativeGate_of_two_le` K2Guard.lean:234 | proved |
| M5 | `d = 1 ∨ d = 3` | NOT, N2, TC with CONJ⁻ | `dim_of_nativeGate2_conj_neg` | via M3 | proved |
| M6 | for `NC = NT = N`, N2 holds iff `NativeGate Ω z N G` | — | → `nativeGate_of_nativeGate2`; ← `nativeGate2_of_nativeGate` | — | proved |
| R0 | for `NC = NT = N`, N2-rel holds iff `NativeGateOf Ω avail z N T` | — | → `nativeGateOf_of_nativeGate2Of`; ← `nativeGate2Of_of_nativeGateOf` | `NativeGateOf` K1Bridge.lean:49 | proved |
| R1 | relative data are maximal data | N2-rel, INC | `nativeGate2_of_cone_subset` | — | proved |
| R2 | maximal data are relative data (two- and one-NOT) | N2 (or `NativeGate`), SUP | `nativeGate2Of_of_cone_superset`, `nativeGateOf_of_cone_superset` | — | proved |
| R3 | EFF gives SUP | EFF | `maxCone_subset_maxConeOf` | `maxConeOf_fullEffects` :415, `maxConeOf_anti` :421 (EffectSpace) | proved |
| R4 | under EQ, N2-rel holds iff N2 | EQ | → `nativeGate2_of_cone_eq`; ← `nativeGate2Of_of_cone_eq`; displayed as `nativeGate2Of_iff_of_cone_eq` | — | proved |
| R5 | M1 and M2 in relative form, the second landing in `NativeGateOf` | N2-rel, CONJ (TC for the second), EQ | `nativeGate2Of_conj`, `nativeGateOf_of_conj` | — (M1, M2 and R4's witnesses; `nativeGateOf_of_cone_eq` of this module) | proved |
| R6 | `d = 1 ∨ d = 3`; `d = 3` with `2 ≤ d`; CONJ⁻ form | NOT, N2-rel on `eball d`, TC, K1B | `dim_of_nativeGate2Of_conj`, `three_of_nativeGate2Of_conj_of_two_le`, `dim_of_nativeGate2Of_conj_neg` | `maxConeOf_avail_eq` EffectSpace.lean:572; M3–M5 | proved |
| R7 | `d = 1 ∨ d = 3` | NOT, N2-rel, TC, K1B-dense | `dim_of_nativeGate2Of_conj_dense` | `maxConeOf_avail_eq_of_dense` DenseOrbit.lean:243 | proved |
| R8 | ORB gives INC on `eball d` for `0 < d`; `d = 1 ∨ d = 3` from NOT, N2-rel, TC and ORB alone (no EFF, no `0 < d` premise) | ORB (and `0 < d` for the inclusion) | `maxConeOf_subset_maxCone_of_orbit`, `dim_of_nativeGate2Of_conj_of_orbit` | `sharpFamily_subset_avail` EffectSpace.lean:374, `maxConeOf_sharp_subset_maxCone` :527, `pos_of_isNot` CompositeDimension.lean:2712 | proved |
| R9 | CN's conjugation identity gives `hcov` | CN, coercion identities | `hcov_of_copyNatural` (this direction only) | `copyNatural_iff_apply` KInfFoundations.lean:294 | proved |
| P1 | two-NOT data at `d = 3` with `NT = swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip` | — | `swapped_nativeGate2`, `swapped_not_ne` | `nativeGate_cnot` CompositeDimension.lean:1160 | proved |
| P2 | the reduction of P1's data is a one-NOT native gate with the control NOT `nflip` | — | `swapped_nativeGate` | — | proved |
| P3 | at `d = 3`, with `sharpUnitFamily 3` and `fullAut 3`, every hypothesis of R6 holds for P1's data | — | `swapped_relative_hyps` (EFF, ORB, NOT, N2-rel, `NT ≠ nflip`, `hcov`), with `swap01_swap01`, `swap01_mem`, `swap01_z3` for CONJ; the first `example` of §F applies R6 to them | `not_fullEffects_of_orbit` EffectSpace.lean:762, `maxConeOf_avail_eq`, `isNot_nflip` CompositeDimension.lean:838 | proved |
| X1 | the exact instances: kernel `cnot` meets the one-NOT relations; P1's gate meets the two-NOT relations and has no one-NOT reading with `nflip`; it has one with the target NOT; the reduction returns `cnot`; the J/K maps at `d = 5, 7` meet the two-NOT relations and their NOTs have unequal ±1 splits, so no linear map conjugates one to the other; neither NOT gives them a one-NOT reading; a shear fixing `z` sends a `maxCone` element out of `maxCone` (value `−1/2`) | the parsed kernel tables of CompositeDimension.lean; the J/K data in the probe | probe 1 (13 checks) | — | exact computation |
| X2 | with `avail = axisFamily`, `T_S` (`cnot` followed by `diag(2, 1, 1)` on both copies) meets the frame and both NOT relations with `nflip` exactly; it is not a `NativeGate (eball 3) z3 nflip` (value `−1/2` on `sharpEff e₃ ⊗ sharpEff (−e₁)` at `prodState z3 xplus`) | the parsed kernel tables; `cone_eq_fails_axis` K1Bridge.lean:157 (EFF holds and EQ fails, so INC fails) | probe 2 (11 checks) | — | exact computation; relative positivity of `T_S` is checked exactly on 37 × 24 sampled pairs and argued in general (written) |

**Open under every outcome.** Type covariance itself (`hcov` with CONJ for any physical pair of copies); NOT; N2 or
N2-rel for any physical gate; EFF, ORB, ORB-dense and INC for any physical `avail`; the converse of R9, and the
conjuncts of TC other than `hcov` from CN; the claim that, for NOTs of the ball, type covariance is equivalent to equal
±1 eigenspace dimensions (a written argument, not part of this round); a kernel statement of the J/K two-NOT clauses
and of X2; a selector for N2-rel with K1-BRIDGE-1's relative entangling clause in place of `2 ≤ d`; whether type
covariance admits any gate that copy naturality excludes.

## The statement surface (frozen; S1 compares both modules with it)

**Module `OIBridge/CopyCovariance.lean`**, namespace `OIBridge.CopyCovariance`, single import `OIBridge.DenseOrbit`.
Its declarations are those of blob `fb9c73fe`, in order and with every statement unchanged:
- §B token-action calculus at every dimension: `homMap_comp'`, `homMap_id'`, `actT_comp'`, `actT_id'`, `actT_congr`,
  `lin_apply_eq_sum'`, `lin_lin_comm'`, `actC_actT_comm'`, and the definition `actTEq g h hgh hhg : W d ≃ₗ[ℝ] W d`;
- §C `sum_mul_ehom`, `affine_linear_apply`, `sum_homMap_mul_ehom`, `prodEffVal_actT`, `isEffectOn_comp`,
  `actT_mem_maxCone (hg : ∀ x ∈ Ω, g x ∈ Ω) (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω`;
- §D the structure `NativeGate2` (fields `frame`, `posFwd`, `posInv`, `relT`, `relC`), `nativeGate2_of_nativeGate`,
  `nativeGate_of_nativeGate2`, `map_corner_of_fix`, `conjGate_apply`, `conjGate_symm_apply`, `nativeGate2_conj`,
  `nativeGate_of_conj`, `dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`,
  `dim_of_nativeGate2_conj_neg`;
- §E `swap01`, `swap01_swap01`, `swap01_mem`, `swap01_z3`, `swapped_nativeGate2`, `swapped_not_ne`,
  `swapped_nativeGate`.

Its twelve `#print axioms` lines, in order: `actC_actT_comm'`, `actTEq`, `prodEffVal_actT`, `actT_mem_maxCone`,
`nativeGate2_conj`, `nativeGate_of_conj`, `dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`,
`dim_of_nativeGate2_conj_neg`, `swapped_nativeGate2`, `swapped_not_ne`, `swapped_nativeGate`.

The headline statements, quoted from blob `fb9c73fe`:

```lean
structure NativeGate2 (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ)
    (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω
  relT : ∀ ω, actT NT (G (actT NT ω)) = G ω
  relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)
theorem nativeGate2_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) :=
theorem nativeGate_of_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)
    (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) :=
theorem dim_of_nativeGate2_conj {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
theorem three_of_nativeGate2_conj_of_two_le (hd : 2 ≤ d) {z : Fin d → ℝ}
    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3 :=
theorem dim_of_nativeGate2_conj_neg {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
theorem swapped_nativeGate2 :
    NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)
      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=
theorem swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip :=
theorem swapped_nativeGate :
    NativeGate (eball 3) z3 nflip
      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ
        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ≪≫ₗ
        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=
```

`swapped_nativeGate` states that the *reduction* of P1's data, conjugated back, is a one-NOT native gate with the
control NOT `nflip`. That P1's gate itself has a one-NOT reading with the target NOT is the exact check C6 of probe 1;
no kernel declaration of this round states it.

**Module `OIBridge/RelativeGateTransport.lean`**, namespace `OIBridge.RelativeGateTransport`, single import
`OIBridge.CopyCovariance`. Its declarations are those of blob `507ac329`, in order and with every statement unchanged:
- §A the structure `NativeGate2Of` (fields `frame`, `posFwd`, `posInv`, `relT`, `relC`),
  `nativeGate2Of_of_nativeGateOf`, `nativeGateOf_of_nativeGate2Of`;
- §B `nativeGate2_of_cone_subset`, `nativeGate2Of_of_cone_superset`, `nativeGateOf_of_cone_superset`,
  `maxCone_subset_maxConeOf`, `nativeGate2_of_cone_eq`, `nativeGate2Of_of_cone_eq`, `nativeGateOf_of_cone_eq`,
  `nativeGate2Of_iff_of_cone_eq`;
- §C `nativeGate2Of_conj`, `nativeGateOf_of_conj`;
- §D `dim_of_nativeGate2Of_conj`, `three_of_nativeGate2Of_conj_of_two_le`, `dim_of_nativeGate2Of_conj_neg`,
  `dim_of_nativeGate2Of_conj_dense`, `maxConeOf_subset_maxCone_of_orbit`, `dim_of_nativeGate2Of_conj_of_orbit`;
- §E `hcov_of_copyNatural`;
- §F `swapped_relative_hyps`, and three `example`s: the positive control through `dim_of_nativeGate2Of_conj`; the
  positive control through `nativeGateOf_of_conj` and the landed `K1Bridge.dim_of_nativeGateOf`; the citation of
  `cone_eq_fails_axis`.

Its thirteen `#print axioms` lines, in order: `nativeGate2_of_cone_subset`, `nativeGate2Of_of_cone_superset`,
`maxCone_subset_maxConeOf`, `nativeGate2Of_iff_of_cone_eq`, `nativeGate2Of_conj`, `nativeGateOf_of_conj`,
`dim_of_nativeGate2Of_conj`, `three_of_nativeGate2Of_conj_of_two_le`, `dim_of_nativeGate2Of_conj_neg`,
`dim_of_nativeGate2Of_conj_dense`, `dim_of_nativeGate2Of_conj_of_orbit`, `hcov_of_copyNatural`,
`swapped_relative_hyps`.

The headline statements, quoted from blob `507ac329` (section variables `{Ω} {avail} {z} {NC NT} {T}` in §B–§C;
`{G} {r} {avail}` in §D; `three_of_nativeGate2Of_conj_of_two_le`, `dim_of_nativeGate2Of_conj_neg` and
`dim_of_nativeGate2Of_conj_dense` differ from `dim_of_nativeGate2Of_conj` only as their names state: `hd : 2 ≤ d` and
conclusion `d = 3`; `hgz : g z = -z`; `hK : DenseBoundaryOrbit (eball d) G`):

```lean
structure NativeGate2Of (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))
    (z : Fin d → ℝ) (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    T (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail
  relT : ∀ ω, actT NT (T (actT NT ω)) = T ω
  relC : ∀ ω, actC NC (T (actC NC ω)) = actT NT (T ω)
theorem nativeGate2_of_cone_subset (h : maxConeOf avail ⊆ maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) : NativeGate2 Ω z NC NT T where
theorem nativeGate2Of_of_cone_superset (h : maxCone Ω ⊆ maxConeOf avail)
    (hT : NativeGate2 Ω z NC NT T) : NativeGate2Of Ω avail z NC NT T where
theorem nativeGateOf_of_cone_superset {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (h : maxCone Ω ⊆ maxConeOf avail) (hT : NativeGate Ω z N T) : NativeGateOf Ω avail z N T where
theorem maxCone_subset_maxConeOf (hE : EffectsOn Ω avail) : maxCone Ω ⊆ maxConeOf avail :=
theorem nativeGate2_of_cone_eq (h : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) : NativeGate2 Ω z NC NT T where
theorem nativeGate2Of_of_cone_eq (h : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2 Ω z NC NT T) : NativeGate2Of Ω avail z NC NT T where
theorem nativeGate2Of_iff_of_cone_eq (h : maxConeOf avail = maxCone Ω) :
    NativeGate2Of Ω avail z NC NT T ↔ NativeGate2 Ω z NC NT T :=
theorem nativeGate2Of_conj (hcone : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2Of Ω avail z NC (h ∘ₗ NT ∘ₗ g)
      (actTEq g h hgh hhg ≪≫ₗ T ≪≫ₗ actTEq h g hhg hgh) :=
theorem nativeGateOf_of_conj (hcone : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)
    (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGateOf Ω avail z NC (actTEq g h hgh hhg ≪≫ₗ T ≪≫ₗ actTEq h g hhg hgh) :=
theorem dim_of_nativeGate2Of_conj (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
theorem maxConeOf_subset_maxCone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) : maxConeOf avail ⊆ maxCone (eball d) :=
theorem dim_of_nativeGate2Of_conj_of_orbit (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
theorem hcov_of_copyNatural {NC NT g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {eC eT eg : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hC : ∀ x, eC x = NC x)
    (hT : ∀ x, eT x = NT x) (hg : ∀ x, eg x = g x) (hnat : CopyNatural eC eT eg) :
    ∀ x, NT (g x) = g (NC x) :=
theorem swapped_relative_hyps :
    ∃ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ),
      EffectsOn (eball 3) (sharpUnitFamily 3) ∧ PreservesBody (eball 3) G ∧
      SharpSeed (eball 3) r ∧ BoundaryTransitive (eball 3) G ∧
      SeedOrbitAvailable G r (sharpUnitFamily 3) ∧ IsNot (eball 3) z3 nflip ∧
      NativeGate2Of (eball 3) (sharpUnitFamily 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)
        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ∧
      swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip ∧
      (∀ x, (swap01 ∘ₗ nflip ∘ₗ swap01) (swap01 x) = swap01 (nflip x)) :=
```

The complete reference for S1 is the declaration list and signature text (up to `:=` or `where`) of the two blobs
above, frozen in `controls.py` (`SURFACE`), with the 25 prints (`PRINTS`).

**Two displayed equivalences (§A.34).** `nativeGate2Of_iff_of_cone_eq` (R4) is proved under EQ, with
`nativeGate2_of_cone_eq` for the forward direction and `nativeGate2Of_of_cone_eq` for the backward one. M6 and R0 are
stated as the two one-way theorems named in their rows. No other equivalence is displayed. Without EQ, INC and SUP each
give one direction (R1, R2), and the round states those directions only.

**Edits to the design blobs before the predicted-tree run (comments only; no statement or proof changes).**
- `CopyCovariance.lean`: its header is rewritten as a module header. The header of blob `fb9c73fe` contains "design
  module" and "Not adopted, not certified, not a round", which S4 rejects.
- `RelativeGateTransport.lean`: its header is rewritten as a module header. The header of blob `507ac329` says the
  file is not a module and not compiled, and states compilation steps for a design branch. The two `-- [unsure]`
  comments are removed: run 38606561330 elaborated both steps.
- Proof hygiene, if any (the unused `first` alternatives the linter reports in `CopyCovariance`), is decided before the
  predicted-tree run and measured by it. After that run, the four execution blobs are frozen.

**Census family** (appended after the BG-2 family, census :1485–1492 at `D`): "type covariance of native inversion
suffices for DIM-1's selector, with positivity on the maximal cone or on the cone of the available tests: two-NOT
native-gate data whose target NOT is the conjugate of the control NOT by a linear body automorphism fixing or
reversing the corner axis reduce to a one-NOT native gate (round KINF-COPY-1, reconstruction)", `modules:
["CopyCovariance", "RelativeGateTransport"]`, `status: "kernel-only"`, `manuscript: []`, its note frozen in
`controls.py` (`FAMILY`).

**Import lines**: `import OIBridge.CopyCovariance` and then `import OIBridge.RelativeGateTransport`, directly after
`import OIBridge.TurnpikePremiseOrientation` (OIBridge.lean:269 at `D`).

## The exact layer (two frozen probes)

Both probes use the Python standard library only, exact rational arithmetic and one `PASS`/`FAIL` line per check, with
the verdict line last. Both parse the kernel's `cnot` tables (`sgn`, `pc`, `pt`), `nflip` and `z3` (probe 2 also
`xplus`) from `CompositeDimension.lean` at its path relative to the probe's own file
(`../lean-mathlib/OIBridge/CompositeDimension.lean`). Neither reads `CopyCovariance` or `RelativeGateTransport`.

**Probe 1, `verification/lean/kinf_copy1_probe.py`.** It is `e2_copy_conj.py` (blob `481fbf7c`) with exactly one
edit: its `KERNEL` constant, `'../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'`, a path relative to
the working directory, becomes the path above resolved from the script's directory
(`os.path.join(os.path.dirname(os.path.abspath(__file__)), …)`), with the `import os` line that requires. Checks:
- C1: kernel `cnot` meets the one-NOT relations with `nflip`;
- C2–C3: P1's gate meets the two-NOT relations, with `NT = diag(−1, 1, −1) ≠ nflip`, both NOTs involutive isometries
  flipping `z`, equal splits;
- C4: P1's gate has no one-NOT reading with the control NOT;
- C6: P1's gate has a one-NOT reading with the target NOT;
- C5: the reduction returns `cnot` exactly;
- J1–J3 at `d = 5` and `d = 7`: the J/K maps meet the two-NOT relations; their NOTs have unequal ±1 splits,
  `(2,2)/(1,3)` and `(3,3)/(1,5)`, so no linear map conjugates one to the other; neither NOT gives a one-NOT reading;
- S1: a shear fixing `z` maps an element of `maxCone` with value `0` to one with value `−1/2`.

Measured on `D`'s `CompositeDimension.lean` with the unedited blob (local replay, drafting measurement): `checks: 13,
failures: 0`, `VERDICT TYPE-COVARIANCE-CONSISTENT`, output byte-identical to `e2_copy_conj.out` on
`research/equivalence` (sha256 of the output `a5b9d6e4…`).

**Probe 2, `verification/lean/kinf_copy1_relative_probe.py`.** It is `relgate_counter.py` (blob `10a02005`) with
three edits:
- its kernel path, read from `argv[1]`, defaults to the path above, resolved as in probe 1 (with `import os`);
- its verdict line becomes `VERDICT TRANSPORT-NEEDS-CONE-INCLUSION`. `axisFamily` meets EFF, so SUP holds for it
  (R3), and the check bears on the inclusion INC, not on the equality;
- its docstring drops "scratch probe, not a round artifact".

Checks: P0 (kernel `cnot` relations), C1–C4 (`T_S`: frame, `relT`, `relC` with `nflip`, inverse), C5 (`axisFamily`
coefficients fixed by `Ŝᵀ`), C6 (relative positivity of `T_S` and `T_S⁻¹` on 37 × 24 sampled pairs), C7 (the value
`−1/2`), C7b, C8 (the same effect pair on `cnot (prodState z3 xplus)` gives `0`), C9 (`S xplus ∉ eball 3`). C6 is an
exact check on samples. Relative positivity for all pairs is a written argument: C5 together with the landed
`cnot_prodState_mem_maxCone` (CompositeDimension.lean:1152).

Measured on `D`'s `CompositeDimension.lean` with the unedited blob (local replay): `checks: 11, failures: 0`, output
byte-identical to `relgate-counter-output.txt` at `c9f16498` (sha256 `ed840fed…`).

Both probes run in one shard, `probes_kinfcopy1`, which also runs `controls.py --self-test`. The shard is spliced after
BG-2's last step, and the aggregate `Numerical probes` job gets the four-place edit (`needs`, env, echo, test).

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Positive token | Rule |
|---|---|---|
| Q-RED | `KINF-COPY-REDUCTION-PROVED` | S1 for `CopyCovariance` §B–§D and S2 pass at `E`. In `E`'s exact-head bridge log, the nine prints of §B–§D lie within `[propext, Classical.choice, Quot.sound]`, and no `sorryAx` or `Lean.ofReduceBool` appears |
| Q-REL | `KINF-COPY-RELATIVE-PROVED` | S1 for `RelativeGateTransport` §A–§E, S2 and S3 pass at `E`. The twelve prints of §B–§E lie within the three axioms, with the same absence conditions |
| Q-POS | `KINF-COPY-SWAPPED-WITNESS` | S1 for `CopyCovariance` §E and `RelativeGateTransport` §F pass at `E`. The prints of `swapped_nativeGate2`, `swapped_not_ne`, `swapped_nativeGate` and `swapped_relative_hyps` lie within the three axioms |
| Q-EXACT | `KINF-COPY-INSTANCES-CONSISTENT` | probe 1's blob at `E`, run by `controls.py` with `python3 -I -B`, prints a `PASS` line for each of C1–C6, J1–J3 at both `d` and S1, no `FAIL` line, `checks: 13, failures: 0` and `VERDICT TYPE-COVARIANCE-CONSISTENT`, with exit 0 and empty standard error |
| Q-COUNTER | `KINF-COPY-TRANSPORT-COUNTER-CONSISTENT` | probe 2's blob at `E`, run the same way, prints a `PASS` line for each of P0, C1–C9 and C7b, no `FAIL` line, `checks: 11, failures: 0` and `VERDICT TRANSPORT-NEEDS-CONE-INCLUSION`, with exit 0 and empty standard error |

S3 (proof shape) for Q-REL:
- the proof of `nativeGate2Of_iff_of_cone_eq` is exactly `⟨nativeGate2_of_cone_eq h, nativeGate2Of_of_cone_eq h⟩`;
- each of the five relative selectors names exactly one maximal-form selector of `CopyCovariance` and one of
  `maxConeOf_avail_eq`, `maxConeOf_avail_eq_of_dense` or `maxConeOf_subset_maxCone_of_orbit`. No relative selector
  names `dim_of_nativeGate` or `three_of_nativeGate_of_two_le` directly;
- `hcov_of_copyNatural` uses `copyNatural_iff_apply` in its forward direction only;
- mutations, each failing S3 alone: an iff proof built from other declarations; a relative selector proved without
  the maximal-form selector; a relative selector naming `dim_of_nativeGate` directly; `hcov_of_copyNatural` naming the
  backward direction of `copyNatural_iff_apply`.

**Gating.** Every positive token is gated on the static controls. If any of C1, C2, S1, S2, S3, S4, W, I, J, P, R, G or
T fails at `E`, or is not reported, `verdict` prints the failed controls, runs no probe and reads no axiom report. Every
cell then prints `KINF-COPY-<REDUCTION|RELATIVE|SWAPPED|INSTANCES|TRANSPORT-COUNTER>-NOT-ESTABLISHED`, the round prints
`KINF-COPY-1-NOT-READ`, and the exit status is 1. When every static control passes, each cell prints its positive token
or its `…-NOT-ESTABLISHED` token by its rule, and the round prints `KINF-COPY-1-READ`. No rule reads another cell's
outcome. The tokens are printed by `controls.py verdict E --freeze F --axioms <E's bridge log>`.

`check` records each control's outcome only when that control runs. Its result maps exactly the controls that ran; a
control with no recorded outcome is absent and counts as failed, as does any value other than `True`. `check` and
`verdict` refuse any stage or mode outside their frozen sets.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all five cells are positive): two-NOT native-gate data whose target NOT is the conjugate
> of the control NOT by a linear body automorphism fixing or reversing the corner axis reduce to one-NOT native-gate
> data, and DIM-1's selector gives d ∈ {1, 3}, and d = 3 with 2 ≤ d. This holds with two-sided positivity on the
> maximal cone. With positivity on the cone of a family of available tests, the inclusion of that cone in the maximal
> cone carries the data to the maximal form, and the selector holds under K1-BRIDGE-1's hypotheses, under the same
> hypotheses with a dense boundary orbit in place of boundary transitivity, and under the orbit hypotheses alone
> without effect soundness. At d = 3 every hypothesis of the relative selector holds for data with two distinct NOTs. The two J/K maps at d = 5 and d = 7 violate type covariance on their exact data. For the one-axis
> family at d = 3, which is effect-sound and whose cone is not inside the maximal cone, one exact gate meets the
> relative one-NOT relations and is not a native gate.

> Non-inference rule: this round does not show that OI supplies a conjugator between the copies' NOTs, a NOT, a native
> gate, a ball, an available-test family, effect soundness, the orbit hypotheses or the cone inclusion; it adopts no
> premise and makes no manuscript claim. It does not show that type covariance admits any gate that copy naturality
> excludes: the positive control's gate also has a one-NOT reading with the target NOT (exact check C6). Copy
> naturality is shown to give the covariance identity `hcov` only; the converse, and the other conjuncts of type
> covariance, are not derived from it. The countercontrol shows, for one family and one gate, that the transport from
> relative to maximal data fails without the inclusion; it does not show that the selector's conclusion fails, or that
> the inclusion is necessary for every family. The J/K result concerns the two named maps only. The equivalence, for
> NOTs of the ball, between type covariance and equal ±1 eigenspace dimensions is a written argument and is not part of
> this round. Positivity of the J/K maps is not re-checked. The probes are exact computations, not Lean kernel proofs,
> and the relative positivity of the countercontrol gate is checked on samples and argued in general. No F2 target,
> extension gate, preserved-law scope or necessity scope is adopted or read, and no contribution to an F2 sufficiency
> statement is claimed.

**Premises this round does not source:** TC (`hcov` with `hgh`, `hhg`, `hgΩ`, `hhΩ`, `hgz`); NOT; N2 and N2-rel (the
frame, NOT relations and positivity clauses); EFF; ORB and ORB-dense (K∞-Trans, K∞-Seed, K∞-V4, body preservation);
INC, SUP and EQ for any `avail` other than those the cited theorems give; CN.

## The ROADMAP wording the round would license (row K∞-Copy; not applied by the round)

At `D`, ROADMAP :1040–1043 reads: "**K∞-Copy** — identical-copy covariance, or copy naturality: identical copies' NOTs
agree. An untested candidate weakening is that the frame-preserving conjugacy class of the native inversion is
determined by system type rather than by token; if the planned exact probe confirms it, the obligation becomes type
covariance of native inversion." Under `KINF-COPY-1-READ` with all five cells positive, the last sentence may be
replaced by: "Type covariance of native inversion (the target copy's NOT is the conjugate of the control copy's NOT by
a linear body automorphism fixing or reversing the corner axis) suffices for DIM-1's selector, with positivity on the
maximal cone (`dim_of_nativeGate2_conj`) or on the cone of the available tests under K1-BRIDGE-1's hypotheses
(`dim_of_nativeGate2Of_conj`); the two-NOT J/K maps at d = 5 and d = 7 violate it." Not licensed: "equivalently, for
NOTs of the ball, equal ±1 eigenspace dimensions" (a written argument); "weakened to" or "the obligation becomes"
(the round proves sufficiency and the `hcov` clause from copy naturality, not that type covariance replaces copy
naturality on the route). K∞-Copy stays OPEN under every outcome.

## The controls (in `controls.py`; not yet generated)

- **S1 surface.** For each module: preamble (the single import, the namespace, the `open` lines); every declaration in
  order and by kind; every signature up to `:=` or `where`; every definition whole; the prints in the frozen order. No
  `sorry`, `admit`, `native_decide`, `axiom`, `implemented_by` or `extern`. Mutations, each failing with its code:
  - `hgz` dropped from `nativeGate_of_conj`;
  - `hcov` reversed (`NC (g x) = g (NT x)`);
  - `hgΩ` dropped from `nativeGate2_conj`;
  - `relC` of `NativeGate2` read with `NT` on the control side;
  - the conclusion of `dim_of_nativeGate2_conj` weakened to `Odd d`;
  - `posFwd` of `NativeGate2Of` stated on `maxCone Ω`;
  - `h : maxConeOf avail ⊆ maxCone Ω` in `nativeGate2_of_cone_subset` reversed;
  - `hE` dropped from `dim_of_nativeGate2Of_conj`;
  - `nativeGate2Of_iff_of_cone_eq` stated without `h`;
  - a second import in either module; an extra print.
- **S2 resolution.** At `E`, the landed objects below are at `D`'s blobs and lines:
  `HVec`, `W`, `hom`, `homMap`, `prodState`, `ehom`, `maxCone`, `actT`, `actC`, `corner`, `IsNot`, `NativeGate`, `cnot`,
  `z3`, `nflip`, `isNot_nflip`, `cnot_prodState_mem_maxCone`, `nativeGate_cnot`, `pos_of_isNot`, `dim_of_nativeGate`
  (CompositeDimension.lean:93, :97, :100, :112, :161, :167, :186, :198, :201, :205, :210, :218, :775, :793, :797,
  :838, :1152, :1160, :2712, :2723); `eball` (TransitiveBody.lean:518); `actT_prodState`,
  `three_of_nativeGate_of_two_le` (K2Guard.lean:173, :234); `NativeGateOf`, `dim_of_nativeGateOf`,
  `cone_eq_fails_axis` (K1Bridge.lean:49, :128, :157); `fullAut`, `sharpFamily_subset_avail`, `maxConeOf`,
  `maxConeOf_fullEffects`, `maxConeOf_anti`, `maxConeOf_sharp_subset_maxCone`, `EffectsOn`, `maxConeOf_avail_eq`,
  `sharpUnitFamily`, `not_fullEffects_of_orbit`, `axisFamily` (EffectSpace.lean:227, :374, :411, :415, :421, :527,
  :567, :572, :736, :762, :811); `DenseBoundaryOrbit`, `maxConeOf_avail_eq_of_dense` (DenseOrbit.lean:53, :243);
  `SharpSeed`, `PreservesBody`, `SeedOrbitAvailable`, `BoundaryTransitive` (OrbitGeneration.lean:65, :69, :74, :79);
  `IsEffectOn`, `CopyNatural`, `copyNatural_iff_apply` (KInfFoundations.lean:116, :284, :294). Mutation: a local
  `maxCone` or `maxConeOf` in either module.
- **S3 proof shape.** As in the decision rules.
- **S4 phrases.** The two module headers and, at `E`, the result note must be present, with none of: "OI supplies",
  "derived from OI", "copy naturality is not needed", "K∞-Copy is discharged", "replaces copy naturality", "admits gates
  that copy naturality excludes", "weakened to", "the obligation becomes", "necessary and sufficient", "kernel proof of"
  (for a probe), "design module", "design draft", "not compiled", "not for merge", "[unsure]".
- **W.** `verify.yml` at `E` is `D`'s with exactly five splices, each anchored once on text: the shard after BG-2's last
  step (:459–460 at `D`), running probe 1, probe 2 and `controls.py --self-test`; and the shard in the aggregate's
  `needs`, env, echo and test lines (:557, :577, :598, :618).
- **I.** `OIBridge.lean` at `E` is `D`'s with the two import lines.
- **J.** The census at `E` is `D`'s with the one family.
- **C2.** The five frozen blobs (*Design evidence*), at stage 1 for `controls.py` and at `E` for all five.
- **P.** The retained evidence pinned below is present at `E` with its digests.
- **R.** The record directory holds exactly this file, `controls.py`, the pinned evidence, `evidence/f-run/`,
  `amendments/` if present, and, at `E`, the result note, which is required there.
- **G.** `git diff --no-renames --name-status D E` lies inside the governed paths, and the legacy manifest is untouched.
- **T.** `delta(D, F)` is the control plane, and the execution is linear after `F`.
- **V (self-test).**
  - `verdict` driven through injected static results: each of the 13 controls failing alone, one unreported, and the
    all-clean case.
  - `verdict` driven end to end through the real `check()` on an in-memory fixture of `D`, `F` and `E`: each
    control's record call removed from the source; each control's inputs absent (the workflow, `OIBridge.lean`, the
    census, each module header, the result note, a pinned evidence file); an unknown stage; an unknown mode; and the
    unmutated case.
  - In every failing case `verdict` returns failure, names the control, prints no positive token and never runs a
    probe. The probe stand-ins record their calls.
  - One-cell mutations: a broken `CopyCovariance` §D signature fails only Q-RED; a broken `RelativeGateTransport` §B
    signature fails only Q-REL; a broken `swapped_relative_hyps` fails only Q-POS; probe 1 with one witness value
    changed fails only Q-EXACT; probe 2 with the `−1/2` witness changed fails only Q-COUNTER.
  - The self-test freezes its own count of self-checks.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; `controls.py`, both modules and both probes are the frozen ones | `C1`: this file's blob at `F`. `C2`: `git rev-parse <commit>:<path>` equal to the frozen blobs, for `controls.py` at stage 1 and all five files at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the dispatch run at exactly `E`, every job `success`; the 25 prints read by `verdict --axioms` |
| each displayed equivalence has one named witness per direction; relative selectors add no dimension argument | `C5`: S1 and S3 in `controls.py check E --freeze F` |
| the exact layer replays and is independent of the new modules | `C3`: shard `probes_kinfcopy1` green; `verdict` re-runs both probe blobs at `E`; `C5` (S1: neither probe names `CopyCovariance` or `RelativeGateTransport`) |
| no positive token is printed while any required static control fails or never ran | `C3`: shard `probes_kinfcopy1` running `controls.py --self-test` with the V cases above |
| the modules are registered; no manuscript or ROADMAP changes | `C4`: the release gate at `E` passing every step, `evidence-retention` included; `C5` (J, G) |
| the change stays inside the governed paths, with exactly the frozen workflow, import and census edits | `C6`: `git diff --no-renames --name-status D E`; `C5` (G, W, I, J) |
| the pre-`F` evidence the rules rest on is retained and unchanged (§A.42 item 2) | `C5` (P) at `E`, against the digests below; reviewers check that each pin resolves to retained content |
| `F`'s exact-head run is retained by the first execution commit (§A.42 item 2) | `C8`: `evidence/f-run/` present at stage 1, naming `F`'s run, job and digest; `C5` (R) |
| `E`'s exact-head run reaches `main` through its own evidence-retention pull request before reconciliation, and the receipt names each retained file's digest (§A.42 item 2) | `C8`: reviewer check of that pull request and of the receipt's candidate entry for `E`; `evidence-retention` at `Q` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence

**Provenance (off `main`; no claim rests on these alone).**

| run | commit | measured |
|---|---|---|
| 38083519826 | `f5367a7a` (`dev-equivalence/kinf-seams`) | design modules `EqvSeams` and `EqvSeamsControl`: build success, fifteen prints within the three axioms |
| 38091534622, job 114328799399 | `8c92343e` (`dev-equivalence/split-l3`) | `CopyCovariance` as blob `fb9c73fe`, built as a library module over `9f9f8257`: build success, the twelve prints within the three axioms; release gate red only at `lean-manuscript` (unregistered module) |
| 38606561330, job 115998853730 | `c9f16498` (reachable from `research/pair-interface-design-20261014`) | over `5bfdaba6`: `CopyCovariance` (blob `fb9c73fe`, checked by hash) compiled with `lean -o`, `RelativeGateTransport` (blob `507ac329`) compiled with `lean`; all 25 prints within the three axioms; the axiom comparison rejects an injected `sorryAx` and a dropped report; `relgate_counter.py` replays byte for byte; legacy records, receipts and placement pass. All steps `success` per the host's job record |
| local replay at `D` | this drafting | both unedited probes on `D`'s `CompositeDimension.lean`: byte-identical to their saved outputs (above). A local run is evidence for the drafter, not a `check-run` attestation (§A.40) |

**Not yet measured.** The predicted execution tree at `D`: both modules as library modules with the edited headers,
both edited probes, the shard, the aggregate lines, the import lines and the family, with `controls.py`. It is built on
a disposable branch from `D`, and the workflow is dispatched on exactly its head (`workflow_dispatch`, so the A42
exclusion shards run). Its expected result is retained and pinned below before `F`. It is design evidence, not a
`check-run` attestation of `F` or `E`.

**Frozen execution blobs** (`C2`; filled from the predicted-tree run):

| path | blob |
| --- | --- |
| `verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/controls.py` | pending |
| `verification/lean-mathlib/OIBridge/CopyCovariance.lean` | pending (statements of `fb9c73fe`) |
| `verification/lean-mathlib/OIBridge/RelativeGateTransport.lean` | pending (statements of `507ac329`) |
| `verification/lean/kinf_copy1_probe.py` | pending (`481fbf7c` with the one edit) |
| `verification/lean/kinf_copy1_relative_probe.py` | pending (`10a02005` with the three edits) |

A different blob at stage 1 or at `E` is a deviation from the frozen design, not a proof repair: it is recorded in the
result note, and the round halts.

**Retained evidence (§A.42).** Each file is a structured expected result in the form of §A.42 item 1: build success;
the release gate's steps and verdict; the 25 `#print axioms` reports; both probes' lines; the self-test summary; the
failure markers. Each names its commit, run, job and recipe, and the digest of the log it was read from. The files are
committed to the record directory by the first execution commit, outside `amendments/`, and pinned here before `F`;
`F` is not designated with a pending pin.

| path | sha256 |
| --- | --- |
| `evidence/predicted-tree.json` | pending (the predicted-tree run) |
| `evidence/drafting-replay.json` | pending (both probes' outputs at `D`, from the frozen probe blobs) |

## Stages and outcomes

**Stages.**
1. `controls.py` at its frozen blob, the pinned evidence and `evidence/f-run/`.
2. Both modules and both probes at their frozen blobs, the workflow edit, the two import lines and the family.
3. The result note, candidate `E`.

**Outcomes.**
- **`KINF-COPY-1-READ`**: `controls.py check E --freeze F` OK; five cell tokens printed by `verdict`; the five frozen
  blobs at `E` (`C2`); the exact-head run at `E` green on every job.
- **`KINF-COPY-1-HALTED`**: anything else (`S12`).

No outcome sources a conjugator, edits the ROADMAP or a manuscript, or changes K∞-Copy's status. Correctness bands are
unchanged (consistency axis).
