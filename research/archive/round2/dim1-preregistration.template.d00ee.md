# Reconstruction round DIM-1 — the composite dimension selector: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round DIM-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-dim-1-dimension-selector/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-dim-1-dimension-selector/
record AM verification/receipts/DIM-1.json
execution A verification/lean-mathlib/OIBridge/CompositeDimension.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/DIM-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, the workflow, no probe, no other round's record (the NB-1 record directory
included), and no line of `verification/ROADMAP.md` other than the two frozen K1 replacements change under any
outcome.**

## The objects

- **`D`** = `00ee70a60cf59d421c0056619709459d704fae99`, the head of `main` after round ORD-1 landed (push run
  37260494801, every job green; the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

TRB-1 landed the coordinate Euclidean ball `eball d` (`TransitiveBody`) with `d` free. NB-1 landed the dimension-free
kernel steps of the finite native-gate ball theorem (`NativeGateBall`: `parity`, `p_le_one`, `dim_of_bounds` and the
lemmas they rest on); its controlled form, block structure and value identity were exact for `d ≤ 7` and written by
hand for general `d`. This round states the composite hypotheses on two identical copies of `eball d`, derives the
data `NativeGateBall` consumes from them in the kernel for every `d`, and proves the selector:

```
two copies of eball d on the bilinear carrier W d, full affine effects (maxCone)
  + IsNot (one common NOT N) + NativeGate (frame, posFwd, posInv, relT, relC)  ⟹  d = 1 ∨ d = 3
  + Entangling                                                                 ⟹  d = 3
```

1. **The carrier.** `W d := Fin (d + 1) → Fin (d + 1) → ℝ`, a real function of a homogenized control index and a
   homogenized target index; product states `prodState x y μ ν = hom x μ * hom y ν`; the value of a product of two
   affine functionals `prodEffVal e f ω`; the maximal cone `maxCone Ω`, nonnegative on every product of two
   `IsEffectOn Ω` effects; the joint states `jointStates Ω`, its vectors with unit entry `ω 0 0 = 1`; the two
   actions `actT N`, `actC N` of a linear map on the target and on the control index. Local tomography is the premise
   this carrier encodes: a joint vector is determined by its values on products of effects because it is a function
   of index pairs. It is not a theorem of the round.
2. **The frozen hypotheses** (§B). `IsNot Ω z N`: `z` a unit vector, `N` a linear involution preserving `Ω` with
   `N z = −z`. `NativeGate Ω z N G` for a linear automorphism `G` of `W d`: the classical CNOT action on the corners
   `±z` (`frame`), `G` and `G⁻¹` carrying product states of `Ω` into `maxCone Ω` (`posFwd`, `posInv`), the target
   relation `actT N ∘ G ∘ actT N = G` (`relT`) and the control relation `actC N ∘ G ∘ actC N = actT N ∘ G` (`relC`),
   with one `N` in both. `Entangling Ω G`: some pair of extreme points `x`, `y` of `Ω` has an image
   `G (prodState x y)` that is an extreme point of `jointStates Ω` and not a product state of `Ω`.
3. **Parity in the kernel** (§C–§J). A linear involution splits a finite-dimensional space into its `±1`
   eigenspaces (`finrank_ker_sub_add_finrank_ker_add`); for the homogenized NOT the two dimensions sum to `d + 1`.
   On operators out of the `−1` eigenspace the gate anticommutes with the control action of `N` and is injective,
   so `NativeGateBall.parity` gives equal dimensions (`finrank_plus_eq_finrank_minus`) and every even `d` is excluded
   (`not_even_of_nativeGate`).
4. **The effect cone** (§L). The homogenized coefficients of every effect of `eball d` lie in the cone
   `Lor` (`lor_ehom`); every cone vector of head at most one half is the coefficient vector of an effect
   (`isEffectOn_affOf`); a maximal-cone vector read as an operator carries the cone into itself
   (`lor_toOp_of_maxCone`). The cone geometry is a theorem about `maxCone`, not a hypothesis.
5. **The block reduction** (§Q), NB-1's S1, S2 and S4 in the kernel for `2 ≤ d`: the controlled form on a corner
   slice (`corner_form`, `gate_corner`, `gate_corner_symm`) with target maps inverse to each other and commuting with
   the NOT (`Mfwd_Minv`, `Minv_Mfwd`, `Mfwd_homMap`, `Minv_homMap`), the `−z` slice by the control relation
   (`gate_corner_neg`); the tangent argument (`lor_curve`, `tangent_vanish`) and the two sphere identities
   (`gt_sphere`, `gt_sphere_corner`); the block form `Phi` (`Phi_sphere`, `Phi_center`); an orthonormal basis of the
   tangent `+1` eigenspace (`finrank_tangentSpace`, `exists_orthonormal_basis`); the block data `BlockData`, the
   hypothesis of `NativeGateBall.p_le_one`, assembled from the frozen hypotheses (`blockData_of_orthonormal`,
   `blockData_of_nativeGate`).
6. **The selectors.** `dim_of_nativeGate`: `IsNot (eball d) z N → NativeGate (eball d) z N G → d = 1 ∨ d = 3`, with
   `d = 0` excluded by the unit clause (`pos_of_isNot`), `d = 1` direct and `2 ≤ d` through the block data and
   `NativeGateBall.dim_of_bounds`; `ne_five_of_nativeGate` and `ne_seven_of_nativeGate` as instances;
   `three_of_nativeGate`: with `Entangling (eball d) G`, `d = 3`, since no gate of two intervals is entangling
   (`not_entangling_one`). Neither `BlockData` nor `2 ≤ d` is a hypothesis of any selector.
7. **Survival at `d = 3`, by exact algebra in the kernel.** The signed permutation `cnot` of the sixteen entries of
   `W 3` with the reflection `nflip` and axis `z3`: `IsNot` (`isNot_nflip`), every native-gate hypothesis including
   two-sided positivity on every product state of the ball (`cnot_core`, `nativeGate_cnot`), and the entangling clause
   (`entangling_cnot`, with the extreme-ray argument `lor_ray`, `phiW_eq_of_segment`). No complex structure enters.
8. **Controls.** The classical gate `cnot1` of two intervals with `neg1` satisfies every hypothesis
   (`isNot_neg1`, `nativeGate_cnot1`) except the entangling clause (`not_entangling_cnot1`) and creates correlations
   from the mixed product input `(0, z1)` (`not_product_cnot1_mixed`), so the entangling clause is the one that
   separates `d = 3` from `d = 1` and creating correlations from a mixed input does not meet it; `eball 4` carries no
   gate (`no_gate_four`). The verdict is `dim1_core`.
9. **Not stated.** No source of local tomography, of the common NOT, of a gate, of the full effect set or of the
   ball; no statement that OI supplies any of them; no complex, tensor-product or Kronecker primitive; no drive,
   transitivity, order or flow statement; no `↔` with an equation in `d`; the uniqueness of the `d = 3` gate up to
   local frame symmetries is not stated. The quantum composite is not identified.

### In scope
- the module `OIBridge/CompositeDimension.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean`, its family in `lean-manuscript-census.json`, and the one frozen sentence of the
  NB-1 family note there;
- the two frozen K1 replacements in `verification/ROADMAP.md`;
- `controls.py` and the result note.

### Frozen out
- any source of local tomography, of the common NOT, of a gate satisfying the native-gate hypotheses, of the full
  effect set, of transitivity or of finite rank; any statement that OI supplies them;
- consumption of COMP-1's `Composite` (an adapter corollary from it to this carrier is a later round), the
  composite as the quantum tensor product (K2), the Bloch adapter, SWAP, composite unitary control, continuous local
  groups, `G² = 1` as a hypothesis, effect cones strictly between the minimal and the maximal one;
- the one-sided variant (`posInv` dropped), different NOTs on the two copies, a sign-diagonal `N` as a premise,
  non-ball bodies, restricted effect sets, DRIVE or ORD∞ as the `d = 1` clause;
- the uniqueness of the `d = 3` gate up to local frame symmetries, which remains research-level evidence;
- any edit to `NativeGateBall`, `TransitiveBody`, `OrbitGeneration`, `OrbitNormalization`, a `ℂ`-typed module, the
  NB-1 record, a manuscript, or any line of `verification/ROADMAP.md` other than the two frozen replacements.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, structure field or hypothesis without a new preregistration revision and new design theorem
identity.

The design theorem identity is the statement surface of `CompositeDimension` embedded in `controls.py` (blob
`8dd1e7895e10210e516efac8395e0fde9fe88c4d`): the preamble (imports, namespaces, `open`, `variable {d : ℕ}`), the 6
context blocks in order, the 319 declarations in order and by kind, every theorem's signature up to `:=` (or up to
`where` for the four witness and control theorems written as structure instances: `isNot_nflip`, `nativeGate_cnot`,
`isNot_neg1`, `nativeGate_cnot1`), every definition and structure whole (proof fields inside a definition included), and
the 87 `#print axioms` lines. The reference module is blob `377f0b25ed0ef58cf6269f71b816e477450131bc`
(`claude/dim1-dev2` at `c5ff17fb`). A repair may change theorem proofs only.
`OIBridge.lean` is `D`'s with `import OIBridge.CompositeDimension` inserted directly after `import
OIBridge.CompositionOrder` (blob `6bfe24300a6a9f695679d4862ba9be35bfd86cf9`). The census is `D`'s with one family,
embedded in `controls.py`, inserted directly after the ORD-1 family (the family whose modules are
`["CompositionOrder"]`), and with one sentence of the NB-1 family note (modules `["NativeGateBall"]`) replaced, written
in `D`'s two-space JSON layout (blob `459fe4c060e35655166e0b31965a78bbfc315df5`). `verification/ROADMAP.md` is `D`'s
with the two replacements of §"Propagation" (blob `0ab126857e9d699abd8c7b04786648ee11179ee8`).

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| CAR | `HVec`, `W`, `hom`, `homMap`, `prodState`, `pairVal`, `ehom`, `prodEffVal`, `maxCone`, `jointStates`, `IsProduct`, `actT`, `actC`, `corner` | the carrier of §1, whole; `maxCone Ω := {ω \| ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}`; `jointStates Ω := {ω \| ω ∈ maxCone Ω ∧ ω 0 0 = 1}` |
| HYP | `IsNot`, `NativeGate`, `Entangling` | the hypotheses of §2, whole: `IsNot` with fields `unit`, `invol`, `preserves`, `flips`; `NativeGate` with fields `frame`, `posFwd`, `posInv`, `relT`, `relC`, one parameter `N` used in both relations; `Entangling` a definition |
| EIG | `finrank_ker_sub_add_finrank_ker_add`, `finrank_plus_add_finrank_minus` | a linear involution `P` of a finite-dimensional real space: `finrank (ker (P − id)) + finrank (ker (P + id)) = finrank V`; for the homogenized NOT the two eigenspaces of the control space have dimensions summing to `d + 1` |
| PAR | `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`, `ne_two_of_nativeGate`, `ne_four_of_nativeGate` | `(hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)`: equal eigenspace dimensions; `¬ Even d`; `d ≠ 2`; `d ≠ 4` |
| CONE | `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone` | `IsEffectOn (eball d) e → Lor (ehom e)`; `Lor v → v 0 ≤ 1 / 2 → IsEffectOn (eball d) (affOf v)`; `ω ∈ maxCone (eball d) → Lor f → Lor (toOp ω f)` |
| BLK | `BlockData`, `p_le_one_of_blockData`, `blockData_of_orthonormal`, `blockData_of_nativeGate` | the block data of `NativeGateBall.p_le_one`, whole; `BlockData p → p ≤ 1`; `(hd : 2 ≤ d) (hN) (hG) : BlockData (tangentPlus N)` |
| S1–S2 | `corner_form`, `gate_corner`, `gate_corner_symm`, `gate_corner_neg`, `tangent_vanish`, `gt_sphere`, `gt_sphere_corner`, `Phi_sphere`, `Phi_center` | the controlled form on the corner slices and the two sphere identities, as listed in §5 |
| SEL | `dim_of_nativeGate`, `ne_five_of_nativeGate`, `ne_seven_of_nativeGate`, `three_of_nativeGate` | `{z} {N} {G} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d = 1 ∨ d = 3`; the same binders `: d ≠ 5`, `: d ≠ 7`; the same binders and `(hE : Entangling (eball d) G) : d = 3` |
| WIT | `isNot_nflip`, `nativeGate_cnot`, `entangling_cnot` | `IsNot (eball 3) z3 nflip`; `NativeGate (eball 3) z3 nflip cnot`; `Entangling (eball 3) cnot` |
| ONE | `not_entangling_one` | `(hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) : ¬ Entangling (eball 1) G` |
| CTL | `isNot_neg1`, `nativeGate_cnot1`, `not_entangling_cnot1`, `not_product_cnot1_mixed`, `no_gate_four` | `IsNot (eball 1) z1 neg1`; `NativeGate (eball 1) z1 neg1 cnot1`; `¬ Entangling (eball 1) cnot1`; `¬ IsProduct (eball 1) (cnot1 (prodState 0 z1))`; `¬ ∃ z N G, IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G` |
| core | `dim1_core` | the parity exclusion, the selector, the selector under the entangling clause, the `d = 3` instance clause `IsNot ∧ NativeGate ∧ Entangling`, the `d = 1` control clause and the `eball 4` exclusion |

Supporting declarations frozen with the surface, by section: §A `hom_zero`, `hom_succ`, `vecTail_add`, `vecTail_smul`,
`homMap_zero`, `homMap_succ`, `vecTail_homMap`, `vecTail_hom`, `homMap_hom`, `homMap_homMap`, `ehom_dot`; §C
`plusSpace`, `minusSpace`, `mem_plusSpace`, `mem_minusSpace`, `hom_zero_mem_plusSpace`, `lift_corner_mem_minusSpace`,
`one_le_finrank_plusSpace`, `one_le_finrank_minusSpace`; §D `not_even_of_balanced`, `split_of_balanced`; §E the
sum-of-squares and dot-product lemmas through `homMap_dot`; §F `toOp`, `fromOp` and their lemmas, `toOp_actC`,
`toOp_actT`, `actT_actT`, `actC_actC`; §G `opGate` and its two relation lemmas; §H `projMinus` and its lemmas; §I
`OpSpace`, `Pop`, `Lop`, `Lop_anti`, `Lop_eq_zero`, `Lop_injective`, `finrank_ker_eq_of_pointwise`,
`finrank_ker_Pop_sub`, `finrank_ker_Pop_add`; §J `tangentPlus`, `sum_univ_four'`, `sum_univ_two'`; §K the gate tables
`sgn`, `pc`, `pt`, `cnotFun`, `cnot`, `z3`, `nflip` and their evaluation lemmas, `cnot_frame`, `cnot_relT`, `cnot_relC`;
§L `Lor`, `affOf` and their lemmas, `pairVal_nonneg_of_maxCone`, `lor_of_forall_pair`, `lor_three`, `lor_of_three`; §M
`cnot_core`, `cnot_target`, `prodEffVal_cnot_prodState`, `cnot_prodEffVal_nonneg`, `cnot_prodState_mem_maxCone`; §N
`extreme_of_unit`, `xplus`, `phiW` and their lemmas, `lor_ray`, `tv`, `ray_eqs`, `phiW_eq_of_segment`; §O `fin1_ext`,
`corner_mem_one`, `eq_corner_of_extreme`; §Q the remaining declarations of the section listed in `controls.py` (`tens` …
`pos_of_isNot`); §P `cnot1Fun`, `cnot1`, `z1`, `neg1` and their lemmas, `cnot1_frame`, `cnot1_relT`, `cnot1_relC`,
`lor_one`, `cnot1_core`, `prodEffVal_cnot1_prodState`, `cnot1_prodState_mem_maxCone`.

### The K1 premises and their kernel objects

ROADMAP K1 names the premises in words; the kernel object carrying each is fixed here and checked by the guards
named in the last column.

| Premise as worded in K1 | Kernel object | Status in the round | Guard |
|---|---|---|---|
| two identical `d`-balls | both copies are literally `eball d` of `TransitiveBody`: one body `Ω = eball d` in `IsNot`, `NativeGate` and `Entangling` in every selector, `posFwd`/`posInv` quantifying `x ∈ Ω, y ∈ Ω` over the same `Ω`, and `W d` indexing both copies by `Fin (d + 1)` | premise (the ball is TRB-1's) | S1, S3, S10 |
| locally tomographic composite | the bilinear carrier `W d`, a function of index pairs, whose docstring states that local tomography is the premise the carrier encodes | encoded by the carrier; not a theorem and not a field | S10 |
| full self-dual effects | `maxCone Ω` quantifies over every affine `IsEffectOn Ω` effect (`IsEffectOn` of `KInfFoundations`, not redeclared); the Lorentz (self-dual) geometry of the effect cone of `eball d` is proved inside the round (§L: `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone`), and `Lor` occurs in no hypothesis | full effect set a premise; cone geometry proved | S3, S5, S10 |
| one common NOT | the single `N` of `IsNot (eball d) z N`, the one linear-map parameter of `NativeGate`, used by both `actT N` and `actC N` in `relT` and `relC` | premise | S3 |
| native CNOT | `NativeGate` with fields `frame`, `posFwd`, `posInv` (two-sided positivity), `relT`, `relC` | premise | S3, S4 |
| entangling | `Entangling (eball d) G`, a hypothesis of `three_of_nativeGate` only | premise of the `d = 3` selector | S1, S4 |

### Semantic guards (in `controls.py`)

One guard per owner decision; each lists the mutation controls `--self-test` drives through it, every one of which
must fail with the named code.

- **S1 the public selector boundary.** `dim_of_nativeGate`, `ne_five_of_nativeGate` and `ne_seven_of_nativeGate`
  have exactly the binders `{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
  (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)` and the conclusions `d = 1 ∨ d = 3`, `d ≠ 5`,
  `d ≠ 7`; `three_of_nativeGate` has those binders and `(hE : Entangling (eball d) G)`, conclusion `d = 3`; each is a
  theorem with its print; `dim1_core` carries the two selector clauses; none of the five statements contains
  `BlockData` or `2 ≤ d` (nor `d ≥ 2`, `1 < d`, `d > 1`); `Entangling` does not occur in `dim_of_nativeGate`.
  Mutations: `(hd : 2 ≤ d)` added to `dim_of_nativeGate`; `(hB : BlockData (tangentPlus N))` added to
  `three_of_nativeGate`; `(hE : Entangling (eball d) G)` added to `dim_of_nativeGate`; `hE` dropped from
  `three_of_nativeGate`.
- **S2 the internal block-reduction chain.** The set of declarations whose statement contains `2 ≤ d` (or the three
  variants) is exactly `exists_tperp_ne_zero`, `blockData_of_orthonormal`, `blockData_of_nativeGate`; the set of
  declarations whose code (statement or proof) contains the token `BlockData` is exactly `BlockData`,
  `p_le_one_of_blockData`, `blockData_of_orthonormal`, `blockData_of_nativeGate`, and the module's code has no other
  occurrence; `BlockData` is a structure equal byte for byte to the frozen text. Mutations: `(hd : 2 ≤ d)` added to
  `gt_sphere`; a theorem `blockData_zero : BlockData 0 → True`; the nonzero-entry clause of `BlockData` replaced by
  `True`.
- **S3 the frozen hypotheses.** `IsNot` and `NativeGate` are structures with the binders
  `(Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))` (and `(G : W d ≃ₗ[ℝ] W d)`), fields
  exactly `[unit, invol, preserves, flips]` and `[frame, posFwd, posInv, relT, relC]`, `N` the one linear-map
  parameter of `NativeGate`, and the field texts `relT : ∀ ω, actT N (G (actT N ω)) = G ω`,
  `relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)`, `posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω`,
  `posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω`; `IsNot`, `NativeGate`, `Entangling`, `maxCone`,
  `jointStates`, `W`, `prodState`, `actT`, `actC` equal their frozen texts whole; `maxCone` ends with the body
  `{ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}`. Mutations: `posInv` removed; a second NOT
  `N'` added to `NativeGate`; `maxCone` restricted to effects with `e 0 = 1`; `Entangling` with the image only a
  joint state, not an extreme one.
- **S4 premises never concluded.** No theorem's conclusion and no definition's type contains `IsNot`, `NativeGate`
  or `Entangling`, except: `isNot_nflip`, `nativeGate_cnot`, `entangling_cnot`, `isNot_neg1`, `nativeGate_cnot1`,
  each a theorem with its print and with exactly the conclusion of rows WIT and CTL; `dim1_core`, whose conclusion
  carries the instance clauses `IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot ∧ Entangling (eball 3)
  cnot` and `IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ …`, the premises otherwise occurring there
  only as antecedents; and the negated forms `¬ Entangling (eball 1) G`, `¬ Entangling (eball 1) cnot1` and the
  conclusion of `no_gate_four`. Mutations: `∃ G, NativeGate (eball d) z N G` concluded from `IsNot`;
  `Entangling (eball d) G` concluded from `NativeGate`; `nativeGate_cnot` concluding `NativeGate … ∧ True`.
- **S5 reuse, not re-proof.** No declaration of the module has the name of a `NativeGateBall` declaration at `D`
  (`averaging_bound`, `blocks_vanish`, `col_sq`, `dim_of_bounds`, `isometry_of_contractions`, `lorentz_of_effects`,
  `nb1_kernel_core`, `p_le_one`, `parity`, `vanish_of_bound`) or the name `eball`, `mem_eball` or `IsEffectOn`; the
  code cites `NativeGateBall.parity`, `NativeGateBall.p_le_one` and `NativeGateBall.dim_of_bounds`; the module imports
  `OIBridge.NativeGateBall`. Mutations: a local `theorem parity`; the citation `NativeGateBall.p_le_one` replaced by a
  local name.
- **S6 field-neutral.** None of the tokens `ℂ`, `Complex`, `TensorProduct`, `⊗ₜ`, `kronecker`, `Kronecker`,
  `unitaryGroup`, `Hilbert`, `Bell` occurs anywhere in the module; every `import` is `OIBridge.TransitiveBody`,
  `OIBridge.NativeGateBall` or `Mathlib.*`; no declaration whose statement contains `↔` contains an equation or
  inequality between `d` and a numeral, `Even d` or `Odd d`. Mutations: a `Mathlib.Analysis.Complex.Basic` import; a
  definition over `ℂ`; `NativeGate (eball d) z N G ↔ d = 3`.
- **S7 phrases.** The module header (the comment before the first `import`) and, at any commit carrying it, the
  result note contain none of "OI selects", "OI implies d", "OI forces d", "copy covariance derived", "local tomography
  derived" (case-insensitive, whitespace-normalized). Mutations: "OI selects the dimension." in the header; a note
  string with "OI forces d" (and a neutral note passes).
- **S8 dimension.** Outside §K, §M, §N, §O, §P and the verdict, a numeral token of value 3, 4, 5 or 7 occurs only
  (a) as the whole conclusion `d = 1 ∨ d = 3`, `d = 3`, `d ≠ 4`, `d ≠ 5` or `d ≠ 7` of a theorem, never in its
  binders or proof, or (b) in the three named coordinate helpers `sum_univ_four'` (§J, the index type `Fin (3 + 1)` of
  `W 3`) and `lor_three`, `lor_of_three` (§L, the cone at `HVec 3`); the preamble and every other declaration of
  those sections, statement and proof, contains none; no `ball3` or `eball_three` token occurs in the code. (`d ≠ 2`
  carries no restricted numeral; the proof of `blockData_of_orthonormal` uses the unit combination
  `(8 / 17, 15 / 17)`, which carries none.) Mutations:
  `(h3 : d = 3)` added to `tangent_vanish`; `(f : Fin 4 → ℝ)` added to `not_even_of_balanced`; the selector's
  conclusion widened to `d = 1 ∨ d = 3 ∨ d = 5`.
- **S9 count.** The module's `#print axioms` lines are exactly the 87 frozen lines, in order and distinct, each
  `OIBridge.CompositeDimension.<name>` for a declaration of the module. Mutations: an 88th print; a duplicated print.
- **S10 the premise correspondence.** The docstring of `W` ends with "Local tomography is the premise this carrier
  encodes."; `Lor` occurs in none of `IsNot`, `NativeGate`, `Entangling`, `maxCone`, `jointStates`; no token `lt` or
  `LocallyTomographic` occurs in the code; `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone` are theorems with
  the conclusions `Lor (ehom e)`, `IsEffectOn (eball d) (affOf v)`, `Lor (toOp ω f)` and their prints. Mutations: the
  carrier's sentence removed; `maxCone` redefined as `{ω | ∀ a b : HVec d, Lor a → Lor b → 0 ≤ pairVal a b ω}`.
- **N1–N3** as COMP-1: declaration list and kinds (an attribute such as `@[simp]` is part of the frozen text),
  preamble and context blocks, statements, definitions and structures, no `sorry`, `admit`, `axiom` or
  `native_decide`, every frozen print present. Mutations: a renamed declaration; a changed `variable` block; a changed
  `open` line; a changed hypothesis of `tangent_vanish`; a `sorry`; a removed print.
- **I, C, R.** `OIBridge.lean` as above; the census as above, compared byte for byte; ROADMAP as in §"Propagation".
  Controls: the frozen import edit passes and an unchanged file fails; the frozen census passes and the family without
  the NB-1 sentence, a changed status, the family moved before ORD-1's and a whitespace change fail; the frozen
  ROADMAP passes and one replacement alone, an extra changed row and an unchanged file fail.

`controls.py`:
- is blob `8dd1e7895e10210e516efac8395e0fde9fe88c4d` (SHA-256
  `6f634394418a3bdbb040d6f38fd01f185bbd58c0c1d377060a72d2fc0902e54f`, 2454 lines), generated from the reference tree by
  `gen_controls_dim1.py` and carried by the predicted execution tree on the disposable branch `claude/dim1-predicted`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 54 checks: the blob read, the 16 checks of the reference module, 33 module mutation controls
  each failing with its named code, the result-note phrase control, and the import, census and ROADMAP controls;
- `check c5ff17fb` passes every check except `P`, which requires this preregistration in the record directory.

### Propagation

The round's governed edits outside the module, applied in stage S1 and frozen in `controls.py` as the constants
`ROADMAP_EDITS`, `NB1_OLD` and `NB1_NEW`. Each text to be replaced occurs exactly once at `D`; the R and C checks
require the file at the commit to be `D`'s with exactly these replacements and nothing else.

1. ROADMAP, the K1 parenthetical in the P1 "K" row. Before:

   ```text
   K1 **CONDITIONAL** (round NB-1: ball, full self-dual effects, the native-gate hypotheses and one common NOT give `d ∈ {1, 3}`)
   ```

   After:

   ```text
   K1 **CONDITIONAL** (rounds NB-1 and DIM-1: two identical balls on the coordinate carrier `W d` with full affine effects, one common NOT and the native-gate hypotheses give `d ∈ {1, 3}`, and `d = 3` with an entangling gate)
   ```

2. ROADMAP, the first five lines of the K1 bullet (the rest of the bullet is unchanged). Before:

   ```text
   - **K1 — the dimension. CONDITIONAL.** For two locally tomographic `d`-balls with full self-dual
     effect cones, one common NOT involution on both copies and a native CNOT satisfying the two NOT
     relations with two-sided product positivity, `d ∈ {1, 3}`. The dimension-free steps are
     kernel-proved, the dimension-dependent steps are exact for `d ≤ 7`, and the theorem for general
     `d` rests on the round's written proof. It does not say that bare OI selects `d = 3`: its OI
   ```

   After:

   ```text
   - **K1 — the dimension. CONDITIONAL.** In the DIM-1 coordinate realization of two identical
     `d`-balls on the locally tomographic bilinear carrier `W d`, using the full affine effect set in
     `maxCone`, one common `IsNot` involution and a `NativeGate` satisfying its frame, two-sided
     positivity and two NOT relations imply `d ∈ {1, 3}` (`dim_of_nativeGate`); adding `Entangling`
     implies `d = 3` (`three_of_nativeGate`). The Lorentz geometry of the effect cone is proved inside
     the round, not assumed. Round NB-1 proved the dimension-free steps in the kernel and the
     dimension-dependent steps exactly for `d ≤ 7`. It does not say that bare OI selects `d = 3`: its OI
   ```

3. The NB-1 census family note (modules `["NativeGateBall"]`), one sentence. Before:

   ```text
   they are not kernel statements, and the theorem for general d is not a kernel theorem.
   ```

   After:

   ```text
   they are not kernel statements of this module, and the theorem for general d is a kernel theorem of round DIM-1 (dim_of_nativeGate and three_of_nativeGate in CompositeDimension).
   ```

No manuscript carries K1 or the NB-1 family, so no manuscript is edited; the NB-1 record directory is not edited.

### Count facts

Two counts are recorded, each from its own source, and neither is inferred from the other:

- the module carries **87** frozen `#print axioms` lines (S9);
- the release gate's `lean-axioms` step printed **5638** named results on the three design runs on `D` (37271632718,
  37274703967 and 37278262616); at `D` it reports 5552.

`tools/lean_axiom_check.py` counts distinct short names: `declared_prints` and the report parser keep the last
dotted component of each printed name in a set. `CompositeDimension.corner_form` has the short name of
`JordanClassification`'s `corner_form` (`#print axioms corner_form`, `JordanClassification.lean:1137` at `D`), and no
other of the 87 short names occurs at `D`; so the 87 prints add 86 names to the set. Running `declared_prints` on the
trees at `D` and at `c5ff17fb` returns 5552 and 5638.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| carrier | `homMap_homMap`, `ehom_dot` | built; axioms within `[propext, Classical.choice, Quot.sound]` | N2, S3, S10 |
| hypotheses | `IsNot`, `NativeGate`, `Entangling` | elaborate; frozen fields | S3 |
| eigenspaces | `finrank_ker_sub_add_finrank_ker_add`, `finrank_plus_add_finrank_minus`, `one_le_finrank_plusSpace`, `one_le_finrank_minusSpace`, `not_even_of_balanced`, `split_of_balanced` | as above | N2 |
| NOT and operators | `sumsq_apply_eq`, `homMap_dot`, `toOp_actC`, `toOp_actT`, `opGate_comp_homMap`, `opGate_homMap_comp` | as above | N2 |
| parity | `Lop_anti`, `Lop_injective`, `finrank_ker_eq_of_pointwise`, `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`, `ne_two_of_nativeGate`, `ne_four_of_nativeGate` | as above | S5 |
| block data | `p_le_one_of_blockData` | as above | S2, S5 |
| effect cone | `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone` | as above | S10 |
| block reduction | `tens_mem_maxCone` … `exists_tperp_ne_zero` (34 prints of §Q), `blockData_of_orthonormal`, `blockData_of_nativeGate` | as above | S2 |
| selectors | `pos_of_isNot`, `dim_of_nativeGate`, `ne_five_of_nativeGate`, `ne_seven_of_nativeGate`, `three_of_nativeGate` | as above | S1, S8 |
| `d = 3` witness | `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`, `cnot_core`, `cnot_prodEffVal_nonneg`, `nativeGate_cnot`, `extreme_of_unit`, `phiW_not_product`, `phiW_mem_jointStates`, `lor_ray`, `phiW_eq_of_segment`, `entangling_cnot` | as above | S4 |
| `d = 1` | `eq_corner_of_extreme`, `not_entangling_one` | as above | S4 |
| controls | `isNot_neg1`, `nativeGate_cnot1`, `not_entangling_cnot1`, `not_product_cnot1_mixed`, `no_gate_four` | as above | S4 |
| verdict | `dim1_core` | as above | S1, S4 |
| count | the 87 prints | each reported within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs (`workflow_dispatch`; the Mathlib bridge job and the release gate read):

| Run | Branch, commit | Workflow run | Result |
|---|---|---|---|
| history | `claude/dim1-dev`, from `afa66d16` (TRB-1's landing), ending at `fb1c701a` | 37266404572 (the last of six) | green; repair history only |
| checkpoint | `claude/dim1-dev` `5eaa1730` | bridge job 111566436954 | green; repair history only |
| 1 | `claude/dim1-dev2` `e641166c` (from `D`: the module, blob `c78fe3ad`; the import after `CompositionOrder`; the census family after ORD-1's and the NB-1 sentence; the K1 propagation) | 37271632718 | **green**: all 32 jobs `success`; the Mathlib bridge (job 111639679874) built the module with each of the 87 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5638 named results, no `sorryAx`; 31 receipts hold; legacy 303 intact) |
| 2 | `claude/dim1-dev2` `1b29c83a` (the module unchanged from run 1; the K1 bullet and P1 parenthetical and the census family name reworded) | 37274703967 | **green**: all 32 jobs `success`; Mathlib bridge (job 111649080160) built 3631 jobs; release gate PASS (`lean-axioms` 5638, `lean-manuscript` OK, legacy 303, 31 receipts) |
| 3 | `claude/dim1-dev2` `c5ff17fb` (the docstring of `BlockData` names its derivation in §Q, and the census family note names this control plane; no declaration changed) | 37278262616 | **green**: all 32 jobs `success`; the Mathlib bridge (job 111660097228) rebuilt the module (3631 jobs) and the release gate passed (`lean-axioms` 5638 named results, no `sorryAx`, no axiom outside the three; `lean-manuscript` OK; legacy 303; 31 receipts) |

The runs on `claude/dim1-dev` were made from TRB-1's landing `afa66d16`, before round ORD-1 landed; they are the
module's repair history and carry no evidence for this freeze. Runs 1 to 3 are the design evidence on `D`, and the
execution blobs of §"The frozen surface" are those of run 3.

Statement-level choices recorded as frozen, relative to the design document (`DIM-1-DESIGN.md` §4): the module is
`CompositeDimension`, not `DimensionSelector`, and imports `TransitiveBody` and `NativeGateBall` only; `0 < d` is not
a hypothesis of any selector (it follows from `IsNot.unit`, `pos_of_isNot`); the route-B transport from a
boundary-transitive body is not in this round; `N` is a general linear involution, diagonalized inside the round by
the eigenspace adapter and an orthonormal basis of the tangent eigenspace, with no sign-diagonal premise; the `d = 1`
clause is `Entangling` (owner decision 3), not DRIVE or ORD∞; the `d = 3` witness is certified in the kernel with its
two-sided positivity (owner decision 5), and no `ℂ`-typed control is used; the block data of `NativeGateBall.p_le_one`
is derived for `2 ≤ d` and appears in no selector.

### The predicted execution tree

- **`@@PRED@@`** (`claude/dim1-predicted`, a single-parent child of `D`) is the execution tree less the result
  note. Its files and blobs:
  - this preregistration in its drafting revision `@@PREREG_DRAFT_COMMIT@@`, blob `@@PREREG_DRAFT_BLOB@@`;
  - `controls.py`, blob `8dd1e7895e10210e516efac8395e0fde9fe88c4d`;
  - `CompositeDimension.lean`, blob `377f0b25ed0ef58cf6269f71b816e477450131bc`;
  - `OIBridge.lean`, blob `6bfe24300a6a9f695679d4862ba9be35bfd86cf9`;
  - the census, blob `459fe4c060e35655166e0b31965a78bbfc315df5`;
  - `verification/ROADMAP.md`, blob `0ab126857e9d699abd8c7b04786648ee11179ee8`.
- `delta(D, @@PRED@@)` is exactly those six paths: the record directory's two files and the four execution paths.
- At that commit `controls.py check @@PRED@@`, run from the tree's own frozen `controls.py`, passes all 20 checks.
- **Run @@PRED_RUN@@** (`workflow_dispatch` on `@@PRED@@`) @@PRED_RESULT@@

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `8dd1e7895e10210e516efac8395e0fde9fe88c4d`, to the record directory. Acceptance: the
   blob is the frozen blob.
2. **S1** adds the module, the import line, the census family with the NB-1 sentence, and the two ROADMAP
   replacements in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom
     set within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit.
   A failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F`
   passes (the result note included in S7) and the exact-head run at `E` has every job green.

## Outcomes

- **`DIM-1-SELECTOR-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head run at `E`
  is green on every job, the Mathlib bridge building `CompositeDimension` with every frozen `#print axioms` reporting
  a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The result note states: on the
  bilinear carrier `W d`, which encodes local tomography, two identical copies of `eball d` with the full affine
  effect set, one common NOT and a native gate (frame, two-sided positivity, the target and control relations) have
  `d = 1` or `d = 3` (`dim_of_nativeGate`), and `d = 3` when the gate is entangling (`three_of_nativeGate`); the block
  data is derived in the kernel and is no premise; the `d = 3` gate satisfies every hypothesis by exact algebra in the
  kernel and the classical gate of two intervals satisfies every hypothesis except the entangling clause; the two
  counts of §"Count facts" as reported at `E`. It states that local tomography, the common NOT, the gate and the full
  effect set are named premises, that no statement here sources them from OI, and that the quantum composite is not
  identified.
- **`DIM-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources local tomography, the common NOT, a gate or the full effect set, states a drive, transitivity,
order or flow, or identifies the quantum composite.
