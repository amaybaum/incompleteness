# Reconstruction round RELC-SELECT-1 — DIM-1's dimension selector without the target relation: parity from the control relation, the selector over the frame, both positivity clauses and the control relation, and a countermodel for each audited clause: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The four questions, the four decision rules, the earned reading, the frozen claims, the non-inference rule, the frozen
surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted execution tree is
recorded before `F`.

```v3-round
round RELC-SELECT-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-relc-select-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-relc-select-1/
record AM verification/receipts/RELC-SELECT-1.json
execution A verification/lean-mathlib/OIBridge/RelcSelectParity.lean
execution A verification/lean-mathlib/OIBridge/RelcSelectBlock.lean
execution A verification/lean-mathlib/OIBridge/RelcSelectSqueeze.lean
execution A verification/lean-mathlib/OIBridge/RelcSelectC5.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/RELC-SELECT-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe, no landed kernel
module and no other round's record change under any outcome.**

## The objects

- **`D`** = `e2426ba4109dcd719d518aefbd3c417b7c6fdc5b`, the head of `main` after round ODD-CHAR-1 landed (merge of `Q`
  `8e72b68e`; the push run 37676443882 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

DIM-1's `NativeGate Ω z N G` has five clauses: the frame `frame`, forward and inverse positivity `posFwd` and `posInv`,
the target relation `relT` and the control relation `relC`. With `IsNot (eball d) z N`, all five give DIM-1's
`dim_of_nativeGate` (`d = 1 ∨ d = 3`), and with the entangling clause `three_of_nativeGate` (`d = 3`). DIM-1's proof
of the selector reads `relT` in two steps: the parity count (`finrank_plus_eq_finrank_minus`), and one line of the
block reduction (`blockData_of_orthonormal`, through `gate_actT` and `Minv_homMap`). PARITY-NOT-1 showed that `relT`
and `relC` together (`GateRel N G`) give the parity count; ODD-CHAR-1 showed that the frame and both relations admit
exactly the odd dimensions and did not separate the two positivity clauses.

RELC-SELECT-1 proves the dimension selector without `relT` among its hypotheses, leaving DIM-1's selector as it is, and
audits the remaining clauses one at a time. It asks four questions, each read from the kernel statements and the landed
statements at `D` by its own frozen decision rule. No rule reads another cell's outcome.

- **Q-PAR.** With `IsNot (eball d) z N` and an invertible gate `G`, does the control relation alone — without `relT`,
  the frame or positivity — give equal dimensions of the two eigenspaces of the homogenized NOT, and so `¬ Even d`?
- **Q-SEL.** For `CtrlGate`, `NativeGate` without its field `relT`, do `IsNot` and `CtrlGate` give DIM-1's conclusion
  `d = 1 ∨ d = 3`, and with the entangling clause `d = 3`, through DIM-1's block reduction restated over `CtrlGate`
  with its single `relT` step replaced, and the parity count of Q-PAR?
- **Q-POS.** At `d = 5`, with PARITY-NOT-1's NOT `n5` and axis `z5`, is there a gate with `IsNot`, the frame, both
  relations and forward positivity that fails inverse positivity, and a gate with `IsNot`, the frame, both relations and
  inverse positivity that fails forward positivity?
- **Q-REL.** At `d = 5`, are there a NOT and a gate with `IsNot`, the frame, `relT` and both positivity clauses that
  fail `relC`, so that `IsNot` and those four clauses do not give `d = 1 ∨ d = 3`?

### The earned reading (frozen)

> The target relation relT is unnecessary for the dimension selector. Under IsNot, the frame, both positivity clauses
> and the control relation relC, the dimension is 1 or 3. The control relation alone already forces odd dimension.
> Neither positivity clause can be dropped individually: explicit d = 5 gates satisfy all remaining clauses while
> violating one positivity direction.
>
> This round does not establish that the frame is necessary or unnecessary, and therefore does not claim a globally
> minimal hypothesis set. It establishes minimality only with respect to the audited relation and positivity clauses.

The result note states this reading in these words exactly when all four cells are proved, and not otherwise.

"Unnecessary for the dimension selector" is Q-SEL: the selector's hypotheses are `IsNot` and `CtrlGate`, which has no
`relT` field, and neither the selector's proof nor the parity theorem it cites names `relT`, `GateRel`, a landed reader
of `relT` or a landed declaration whose statement takes `NativeGate` (S1, S2). "Under IsNot, the frame, both positivity
clauses and the control relation relC, the dimension is 1 or 3" is `dim_of_ctrlGate`. "The control relation alone" is
Q-PAR: `IsNot (eball d) z N`, the gate a linear equivalence of the joint carrier, and `relC`, without `relT`, the frame
or positivity. "Neither positivity clause can be dropped individually" is Q-POS, read against the selector's hypothesis
set: `gSq` satisfies `IsNot`, the frame, `relC` and `posFwd` (and `relT` besides) at `d = 5`, and `gSq.symm` satisfies
`IsNot`, the frame, `relC` and `posInv` (and `relT` besides) at `d = 5`; since `5` is neither `1` nor `3`, neither
implication with one positivity clause removed holds. That failure is each witness theorem beside `5 ∉ {1, 3}`; the
round adds no kernel statement of it and needs none. "The audited relation" is `relC`: Q-REL shows that it is not
replaced by `relT`. Minimality is with respect to `posFwd`, `posInv` and `relC`; `IsNot` and the frame are held fixed
throughout.

### The frozen claims

Each claim below is stated with the kernel statements and the rule that carry it, and nothing stronger is claimed.

1. **`CtrlGate` removes `relT` from the dimension-selection sufficiency theorem, not from the gate theory.** `CtrlGate`
   is `NativeGate` read from `D` with its field `relT` removed, field for field (Q-SEL). It is the hypothesis of
   `blockData_of_ctrlGate`, `dim_of_ctrlGate` and `three_of_ctrlGate`, and `ctrlGate_of_nativeGate` maps every native
   gate to it. `NativeGate`, `GateRel` and every landed statement over them are unchanged — no landed module changes
   under the round (`P`) — and `relT` remains a field of both.
2. **`IsNot` and `CtrlGate` give exactly `d = 1 ∨ d = 3`.** One direction is `dim_of_ctrlGate`: every `z`, `N`, `G`
   with `IsNot (eball d) z N` and `CtrlGate (eball d) z N G` have `d = 1 ∨ d = 3`, DIM-1's conclusion. The other is
   that both values occur: DIM-1's `isNot_neg1` with `ctrlGate_of_nativeGate` applied to `nativeGate_cnot1` at
   `d = 1`, and `isNot_nflip` with it applied to `nativeGate_cnot` at `d = 3`. Each direction is witnessed by
   separately named kernel statements, as §A.34 requires of a displayed equivalence; the second is those statements
   side by side, and the round adds no kernel statement of it.
3. **The entangling clause is what removes the `d = 1` branch.** `three_of_ctrlGate` adds `Entangling (eball d) G` and
   concludes `d = 3`; its proof excludes `d = 1` through `not_entangling_one_ctrl`, which reads, of the gate's
   clauses, the frame alone. Without
   the entangling clause `d = 1` is not excluded: DIM-1's `cnot1`, with `neg1` and `z1`, gives a `CtrlGate` at
   `d = 1`.
4. **Neither `posFwd` nor `posInv` may be dropped individually.** `gSq_sep` and `gSqInv_sep` (Q-POS), each with every
   other clause of `NativeGate` including both relations, at `d = 5` with the landed `n5`.
5. **`relC` may not be replaced by `relT`.** `c5_sep` and `relT_not_dimension_selecting` (Q-REL): `IsNot`, the frame,
   `relT`, `posFwd` and `posInv` hold at `d = 5` for `nC5` and `gC5`, and the implication from them to `d = 1 ∨ d = 3`
   is false.
6. **`relC` is not claimed to pass to the inverse on its own.** The transfer of `relC` from `G` to `G.symm` used in the
   round is `relC_symm_of_relT`, which takes `relT` and `relC` of `G`; the control relation of `gSq.symm` in
   `gSqInv_sep` comes through `gateRel_symm` from `GateRel n5 gSq`. Q-POS fails if the transfer's `relT` hypothesis is
   dropped.
7. **The squeezed `d = 5` gate, its inverse and the C5 construction are countermodel witnesses.** `gSq`, `gSq.symm`,
   `nC5` and `gC5` are not postulates, adopted models, or a NOT or a gate of a physical theory (the non-inference rule;
   the module headers).
8. **No claim that `relT` is globally redundant appears anywhere.** The non-inference rule states the scope, and S8
   fails on such a phrase in any module comment or in the result note outside the frozen texts.

**`nC5` is a new witness construction.** `nC5` is a NOT of `eball 5` with the landed axis `z5`, constructed for the
`relC` countermodel only. It is not PARITY-NOT-1's balanced `n5`, which it neither replaces nor modifies: its
homogenized map has sign `+1` at the homogeneous indices `0` and `1` and `−1` at the other four (`oddC5`,
`homMap_nC5_sign`), where `n5` has three of each (`odd5`, `homMap_n5_sign`). The squeezed witnesses of Q-POS use `n5`
itself.

### The non-inference rule (frozen)

> CtrlGate is the hypothesis of the dimension selector only. This round does not show that relT is redundant in
> NativeGate or in GateRel, that relT follows from the remaining clauses, or that every CtrlGate is a NativeGate:
> NativeGate, GateRel and every landed statement over them are unchanged, and relT remains a field of both. It does not
> show that the control relation of a gate gives the control relation of its inverse: the transfer used for the inverse
> of the squeezed gate, relC_symm_of_relT, reads the target relation as well. Its countermodel for the control relation
> uses the witness NOT nC5, whose homogenized map has two indices of sign +1 and four of sign −1; it does not decide
> whether the target relation, the frame and two-sided positivity select the dimension for a NOT whose two homogenized
> eigenspaces have equal dimension, such as PARITY-NOT-1's n5. The squeezed gate, its inverse, nC5 and gC5 are
> mathematical countermodels for the clauses they separate; they are not postulates, adopted models, or a NOT or a gate
> of a physical theory, and the orthogonal complex structures J and K in the proof of gC5's positivity are tools of
> that proof. The selector concerns two copies of the Euclidean ball under the stated hypotheses; the round does not
> claim that OI selects a dimension, adopts no premise, and makes no manuscript claim and no ROADMAP claim.

The result note states this rule in these words under every outcome.

### The decision rules (frozen; implemented by `controls.py verdict`)

The landed texts the controls read — `NativeGate`'s header and fields `frame`, `posFwd`, `posInv`, `relT`, `relC`;
`IsNot`; `Entangling`; `GateRel`'s field list and fields; DIM-1's `dim_of_nativeGate`, `three_of_nativeGate`,
`not_entangling_one`, `blockData_of_nativeGate`, `nativeGate_cnot1` and `nativeGate_cnot` and the balance lemma
`not_even_of_balanced`; PARITY-NOT-1's `odd5`, `c5`, `n5`, `z5`, `x5`, `isNot_n5` and `homMap_n5_sign`; the 22
declarations of DIM-1's §Q the block module restates; and the names of the landed declarations whose statements take
`NativeGate` — are read from `D` and embedded in `controls.py`, and L requires them unchanged. A field "read from `D`"
is that field's text, whitespace-normalized; "at" a gate, NOT, axis or body is that text with `G`, `N`, `z` or `Ω`
replaced by it.

| Cell | Outcome | Rule |
|---|---|---|
| Q-PAR | `RELC-PARITY-PROVED` | all of: `finrank_plus_eq_finrank_minus_relC` has the binders `{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hC : RELC)`, `RELC` `NativeGate`'s `relC` field read from `D`, and the conclusion `Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)`, and its proof names `opGate_injective_relC`, `opGate_homMap_comp_relC`, `finrank_ker_sub_le_relC`, `finrank_ker_add_le_relC`, `finrank_ker_relCLeft_sub`, `finrank_ker_relCLeft_add`, `finrank_ker_relCConj_sub_le`, `finrank_ker_relCConj_add_le` and `balance_of_bounds_relC`; `not_even_of_relC` has the same binders, the conclusion `¬ Even d`, and a proof naming `not_even_of_balanced` and `finrank_plus_eq_finrank_minus_relC`; the landed `not_even_of_balanced` is the frozen one; and no declaration of the parity module names `relT`, `GateRel`, `NativeGate`, `CtrlGate`, `frame`, `posFwd`, `posInv`, `maxCone`, `prodEffVal`, `IsEffectOn`, `sharpEff`, `corner`, `prodState` or `Entangling`, a landed reader of `relT` (`gate_actT`, `Mfwd_homMap`, `Minv_homMap`, `Minv_Mfwd`, `opGate_comp_homMap`, `opGate_comp_homMap_rel`, `Lop_eq_zero`, `Lop_injective`, `finrank_plus_eq_finrank_minus`, `finrank_plus_eq_finrank_minus_rel`, `gateRel_of_nativeGate`, `not_even_of_gateRel`), or a landed declaration whose statement takes `NativeGate`, directly or through a namespace |
| Q-PAR | `RELC-PARITY-NOT-ESTABLISHED` | otherwise |
| Q-SEL | `CTRL-SELECTOR-PROVED` | all of: `CtrlGate` is a structure with `NativeGate`'s header read from `D` (the name aside) and exactly the fields `frame`, `posFwd`, `posInv`, `relC`, in that order, each `NativeGate`'s field read from `D`, `NativeGate`'s fields at `D` being `frame posFwd posInv relT relC`; `ctrlGate_of_nativeGate` and `actT_slice_ctrl` have their frozen statements; `blockData_of_ctrlGate`, `not_entangling_one_ctrl`, `dim_of_ctrlGate` and `three_of_ctrlGate` have the statements of DIM-1's `blockData_of_nativeGate`, `not_entangling_one`, `dim_of_nativeGate` and `three_of_nativeGate` read from `D`, with `NativeGate` replaced by `CtrlGate`; the proofs of `dim_of_ctrlGate`, `three_of_ctrlGate`, `blockData_of_ctrlGate`, `blockData_of_orthonormal_ctrl` and `actT_slice_ctrl` name, respectively, `finrank_plus_eq_finrank_minus_relC` and `blockData_of_ctrlGate`; `dim_of_ctrlGate` and `not_entangling_one_ctrl`; `blockData_of_orthonormal_ctrl`; `actT_slice_ctrl`; and `phi_minusSpace_ctrl` and `homMap_eq_self_of_orth_minusSpace`; the block copy holds (below); no declaration of the block module names a landed reader of `relT` or a landed declaration whose statement takes `NativeGate`, only `ctrlGate_of_nativeGate` names `NativeGate`, and only `not_entangling_one_ctrl` and `three_of_ctrlGate` name `Entangling`; the parity theorem has the binders and conclusion of Q-PAR's row and the parity module names no landed reader of `relT` and no landed declaration whose statement takes `NativeGate`; and DIM-1's `nativeGate_cnot1` and `nativeGate_cnot` at `D` are the frozen ones |
| Q-SEL | `CTRL-SELECTOR-NOT-ESTABLISHED` | otherwise |
| Q-POS | `POSITIVITY-SEPARATION-PROVED` | all of: the witness definitions `sqCls`, `sqSig`, `sqPc`, `sqPt`, `sqR`, `sqK`, `sqW`, `sqWi`, `gSqFun` and `gSqInvFun` are the frozen ones and `gSq` has `toFun := gSqFun` and `invFun := gSqInvFun`; each row of the positivity table has its frozen binders and conclusion and its proof names; `GateRel` at `D` has exactly the fields `relT relC`, each `NativeGate`'s field at `D`; PARITY-NOT-1's `odd5`, `c5`, `n5`, `z5`, `x5`, `isNot_n5` and `homMap_n5_sign` at `D` are the frozen ones; and no declaration of the squeeze module names `Entangling` or `CtrlGate` |
| Q-POS | `POSITIVITY-SEPARATION-NOT-ESTABLISHED` | otherwise |
| Q-REL | `RELT-NOT-DIMENSION-SELECTING-PROVED` | all of: the witness definitions `oddC5`, `cC5`, `nC5`, `sgnC5`, `pcC5`, `ptC5` and `gC5Fun` are the frozen ones and `gC5` has `toFun := gC5Fun` and `invFun := gC5Fun`; each row of the relation table has its frozen binders and conclusion and its proof names; the landed `z5` is the frozen one; and no declaration of the C5 module names `n5`, `c5`, `odd5`, `isNot_n5`, `homMap_n5_sign`, `Entangling` or `CtrlGate` |
| Q-REL | `RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED` | otherwise |

The round's outcome is `RELC-SELECT-1-READ` when all four cells are assigned, each by its own rule. The design runs
below already exhibit modules read by these rules as `RELC-PARITY-PROVED`, `CTRL-SELECTOR-PROVED`,
`POSITIVITY-SEPARATION-PROVED` and `RELT-NOT-DIMENSION-SELECTING-PROVED`; the rules, not that reading, are what this
file freezes, and the cells at `E` are those `controls.py verdict E` prints.

Q-PAR reads the parity module. Q-SEL reads the block module and, for the parity step it cites, the parity theorem's
statement and the parity module's freedom from `relT`; a broken parity theorem therefore reads not-established in Q-PAR
and Q-SEL. Q-POS reads the squeeze module and Q-REL the C5 module. A landed `relT` field that differs reads
not-established in Q-POS and Q-REL and leaves Q-PAR and Q-SEL, which do not read it.

### The block copy (frozen)

`RelcSelectBlock` restates DIM-1's block reduction. Each of the 22 declarations of `CompositeDimension` below is
restated under the name beside it, its lines equal to the landed lines at `D` with the names of this map and
`NativeGate` replaced by `CtrlGate`, except the two line edits; a declaration's lines are its first line and every
following line up to the next unindented line.

| Landed (`D`) | Restated |
|---|---|
| `gate_corner`, `gate_corner_symm`, `Mfwd_Minv`, `lor_Minv`, `gate_actC`, `gate_corner_neg` | the same names with `_ctrl` |
| `gt_corner`, `gt_corner_neg`, `gt_center`, `gt_tangent_corners`, `gt_sphere`, `gt_sphere_corner` | the same names with `_ctrl` |
| `Phi_sphere`, `Phi_center`, `Phi_center_all`, `Phi_hom_zero_eq_zero`, `Phi_lift_z_eq_zero` | the same names with `_ctrl` |
| `blockData_of_orthonormal` | `blockData_of_orthonormal_ctrl` |
| `blockData_of_nativeGate`, `not_entangling_one` | `blockData_of_ctrlGate`, `not_entangling_one_ctrl` |
| `dim_of_nativeGate`, `three_of_nativeGate` | `dim_of_ctrlGate`, `three_of_ctrlGate` |

The two line edits, each applied once:

- in `blockData_of_orthonormal_ctrl`, the landed line
  `rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]` becomes
  `rw [hω]; exact actT_slice_ctrl hN hG hcl hzl` — the single `relT` step of the block reduction;
- in `dim_of_ctrlGate`, the landed line `have hbal := finrank_plus_eq_finrank_minus hN hG` becomes
  `have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC` — the parity step.

The module declares nothing else but `CtrlGate`, `ctrlGate_of_nativeGate` and the six new lemmas of the replacement:
`gt_center_two_ctrl`, `phi_lift_minus_ctrl`, `phi_bvec_minus_unit_ctrl`, `phi_minusSpace_ctrl`,
`homMap_eq_self_of_orth_minusSpace` and `actT_slice_ctrl`. The replacement: for a unit `u` of head zero in the `−1`
eigenspace of the homogenized NOT, the functional `a ↦ pairVal a (hom 0 − u) (G (hom c ⊗ Minv (hom 0 − u)))` is
nonnegative on the cone, equals `a ↦ a·hom z − 2 Φ(a; u, hom 0)` and vanishes at `hom (−z)`; DIM-1's tangent argument
gives `Φ(a; u, hom 0) = 0` for every control effect, so each row of the slice's image is orthogonal to the `−1`
eigenspace and is fixed by the self-adjoint involution. It reads the frame, both positivity clauses and `relC`.

The copied proofs keep DIM-1's seven linter warnings (unused `simp` arguments and one unnecessary `<;>`), as the
landed proofs carry them; the copy is frozen line for line, so a repair to a copied declaration fails S2.

### The positivity table (frozen)

`FRAME`, `POSFWD`, `POSINV`, `RELT` and `RELC` are `NativeGate`'s fields read from `D`. `X[G.symm]` is the field `X`
with `G` replaced by `G.symm` and nothing else; for the gates `gSq` and `gSq.symm`, `X[gate]` is the field at that
gate, at the axis `z5`, the NOT `n5` and the body `eball 5`. `GRD` is
`{Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}`.

| Declaration | Frozen binders and conclusion | Proof names |
|---|---|---|
| `frame_symm` | `{z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d} (hF : FRAME) : FRAME[G.symm]` | — |
| `relT_symm` | `GRD (hN : IsNot Ω z N) (hT : RELT) : RELT[G.symm]` | — |
| `relC_symm_of_relT` | `GRD (hN : IsNot Ω z N) (hT : RELT) (hC : RELC) : RELC[G.symm]` | — |
| `gateRel_symm` | `GRD (hN : IsNot Ω z N) (hR : GateRel N G) : GateRel N G.symm` | `relT_symm`, `relC_symm_of_relT` |
| `gSq_frame` | `(a b : Fin 2) : ` the body of `FRAME[gSq]` | — |
| `gSq_relT`, `gSq_relC` | `RELT[gSq]`, `RELC[gSq]` | — |
| `gateRel_gSq` | `GateRel n5 gSq` | `gSq_relT`, `gSq_relC` |
| `gSq_posFwd` | `POSFWD[gSq]` | `gSq_pairVal_nonneg` |
| `gSq_symm_value` | `prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2` | — |
| `gSq_symm_not_mem_maxCone` | `gSq.symm (prodState z5 x5) ∉ maxCone (eball 5)` | `gSq_symm_value`, `sharpEff_isEffectOn`, `z5_unit`, `negx5_unit` |
| `gSq_not_posInv` | `¬ POSINV[gSq]` | `gSq_symm_not_mem_maxCone`, `z5_mem`, `x5_mem` |
| `not_nativeGate_gSq`, `not_nativeGate_gSqInv` | `¬ NativeGate (eball 5) z5 n5 gSq`, `¬ NativeGate (eball 5) z5 n5 gSq.symm` | `gSq_not_posInv` |
| `gSq_sep` | `IsNot (eball 5) z5 n5 ∧ (FRAME[gSq]) ∧ GateRel n5 gSq ∧ (POSFWD[gSq]) ∧ ¬ (POSINV[gSq])` | `isNot_n5`, `gSq_frame`, `gateRel_gSq`, `gSq_posFwd`, `gSq_not_posInv` |
| `gSqInv_sep` | `IsNot (eball 5) z5 n5 ∧ (FRAME[gSq.symm]) ∧ GateRel n5 gSq.symm ∧ (POSINV[gSq.symm]) ∧ ¬ (POSFWD[gSq.symm])`, with `gSq.symm.symm` in `POSINV[gSq.symm]` written `gSq` | `isNot_n5`, `frame_symm`, `gateRel_symm`, `gSq_posFwd`, `gSq_not_posInv` |

The witness: on the homogeneous indices `0, …, 5` of `eball 5`, `gSq` maps entry `(m, n)` of a joint vector to
`sqW m n` times entry `(sqPc m n, sqPt m n)`, a weighted involutive index permutation; the classical rows `0` and `5`
have weight `1`, the tangent rows the weight `ε = 1/10`, and the target squeeze `K_λ` gives weight `λ = 1/2` to the
tangent target indices (`sqK`). With `λ = 1` the forward positivity fails; with `λ = 1/2` it holds, through the
square-root-free chain `rsq_cs4`, `rsq_ab`, `rsq_s`, `rsq_key`, `rsq_assemble` and `gSq_core` on the decomposition
`pairVal_gSq_prodState`. The image under `gSq.symm` of the product of the corner `z5` with the first axis `x5` pairs to
`−1/2` with the sharp effects of `z5` and `−x5`. The witness is rational, so the value is exact. `gSqInv_sep` states
the inverse positivity of `gSq.symm` as the forward positivity of `gSq`, since `gSq.symm.symm = gSq`
(`LinearEquiv.symm_symm`).

### The relation table (frozen)

`[gC5]` is a field at the gate `gC5`, the NOT `nC5`, the axis `z5` and the body `eball 5`; `SEL` is the conclusion of
DIM-1's `dim_of_nativeGate` read from `D`; `FRAME`, `POSFWD`, `POSINV` and `RELT` in the last row are the fields at the
body `eball d`, the other variables free.

| Declaration | Frozen binders and conclusion | Proof names |
|---|---|---|
| `isNot_nC5` | `IsNot (eball 5) z5 nC5` | — |
| `homMap_nC5_sign` | `(v : HVec 5) (μ : Fin (5 + 1)) : homMap nC5 v μ = (if oddC5 μ then -1 else 1) * v μ` | — |
| `gC5_frame` | `(a b : Fin 2) : ` the body of `FRAME[gC5]` | — |
| `gC5_relT` | `(ω : W 5) : ` the body of `RELT[gC5]` | — |
| `gC5_relC_lhs`, `gC5_relC_rhs` | `actC nC5 (gC5 (actC nC5 (OddChar.entW 3 3))) 4 4 = 1`, `actT nC5 (gC5 (OddChar.entW 3 3)) 4 4 = -1` | — |
| `gC5_not_relC` | `¬ RELC[gC5]` | `gC5_relC_lhs`, `gC5_relC_rhs` |
| `gC5_posFwd`, `gC5_posInv` | `POSFWD[gC5]`, `POSINV[gC5]` | `gC5_prodEffVal_nonneg`; `gC5_posFwd` |
| `c5_sep` | `IsNot (eball 5) z5 nC5 ∧ (FRAME[gC5]) ∧ (RELT[gC5]) ∧ (POSFWD[gC5]) ∧ (POSINV[gC5]) ∧ ¬ (RELC[gC5])` | `isNot_nC5`, `gC5_frame`, `gC5_relT`, `gC5_posFwd`, `gC5_posInv`, `gC5_not_relC` |
| `not_nativeGate_gC5` | `¬ NativeGate (eball 5) z5 nC5 gC5` | `gC5_not_relC` |
| `relT_not_dimension_selecting` | `¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N → (FRAME) → (POSFWD) → (POSINV) → (RELT) → SEL` | `isNot_nC5`, `gC5_frame`, `gC5_posFwd`, `gC5_posInv`, `gC5_relT` |

The witness: `nC5 = diagSign cC5` with signs `(1, −1, −1, −1, −1)`, and `gC5` is round NB-1's `d = 5` J/K map, the
control `C5` of NB-1's preregistration, a signed permutation of the thirty-six entries with `gC5 ∘ gC5 = id`. NB-1
established its positivity by a written reduction to the complex CNOT; here it is proved directly, by the value identity
`prodEffVal_gC5_prodState`, two Bessel inequalities (`selC5_besselJ`, `selC5_besselK`), Cauchy–Schwarz and
`selC5_mix`. The control relation fails at the entry `(4, 4)` of the image of the matrix unit `entW 3 3`, where its two
sides are `1` and `−1`.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity. A statement mismatch found by a control returns the round to design; it is never repaired during execution.

The design theorem identity is the statement surface of the four modules embedded in `controls.py`, blob
`8cafc140b519495d1687a5507846d320c3c3295f`: for each module, the preamble (the imports, the namespaces and the `open`
line), the context blocks in order, the declarations in order and by kind (28, 30, 58 and 40), every theorem's
signature up to `:=`, every definition and structure whole, and the `#print axioms` lines (2, 5, 15 and 12). The
reference modules are the blobs

- `40cdd044094a5886d916c2c1a8847ff2066433d8` (`RelcSelectParity`),
- `4db61452136745e536803f1d6f5789772db3fb50` (`RelcSelectBlock`),
- `ed994d18e322ef61015cba0e7dc3715316b009d6` (`RelcSelectSqueeze`) and
- `4ba97ee39c522faf6cc39ccca9f1c09dbcf0b9a6` (`RelcSelectC5`).

A repair may change theorem proofs only, and none of a copied declaration's (S2). `OIBridge.lean` is
`D`'s with `import OIBridge.RelcSelectParity`, `import OIBridge.RelcSelectBlock`, `import OIBridge.RelcSelectSqueeze`
and `import OIBridge.RelcSelectC5` inserted, in that order, directly after `import OIBridge.OddChar`. The census is
`D`'s with one family, embedded in `controls.py`, inserted directly after the ODD-CHAR-1 family (modules
`["OddChar"]`), in `D`'s two-space JSON layout.

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **L landed.** The landed texts read from `D` are the frozen ones.
- **N1–N3.** Each module declares exactly its frozen declarations; its preamble, context blocks, statements and
  definitions are the frozen ones; no `sorry`, `admit`, axiom declaration or `native_decide`, and every frozen print
  present. Mutations: a renamed declaration; a changed binder context; a changed `open` line; a restated conclusion; a
  `sorry`; a print removed.
- **S1 parity** (Q-PAR). Mutations: the control relation replaced by `GateRel`; the target relation added to the parity
  corollary; the count weakened to an inequality; a parity proof reading a landed `relT` lemma. Rule controls: a broken
  parity theorem reads not-established in Q-PAR and Q-SEL and leaves Q-POS and Q-REL; a landed `relC` field that differs
  fails all four cells; a landed balance lemma that differs fails Q-PAR alone; a landed `relT` field that differs fails
  Q-POS and Q-REL and leaves Q-PAR and Q-SEL.
- **S2 selector** (Q-SEL). Mutations: `relT` restored to `CtrlGate`; `posInv` dropped from `CtrlGate`; the selector
  strengthened to `d = 3`; the landed parity line restored; the `relT` step restored in the block reduction; a copied
  proof token changed; a landed native-gate lemma referenced; the entangling clause dropped from `three_of_ctrlGate`.
  Controls: a `relT` reader, and a landed native-gate lemma, named through its namespace are found. Rule controls: a
  broken selector reads not-established in Q-SEL alone; a landed selector, a landed `d = 3` native gate, and a landed
  copied declaration that differ each fail Q-SEL alone; a landed `posInv` field that differs fails every cell but
  Q-PAR.
- **S3 positivity** (Q-POS). Mutations: the failure of inverse positivity dropped from `gSq_sep`; the inverse
  positivity of `gSq.symm` restated as its forward positivity; the transfer of `relC` to the inverse without `relT`;
  the value changed to a sign; the squeeze removed (`λ = 1`); `GateRel` weakened to the control relation in `gSq_sep`.
  Rule controls: a broken witness reads not-established in Q-POS alone; a landed `n5`, and a landed `GateRel` that
  differs from the landed relations, each fail Q-POS alone.
- **S4 relation** (Q-REL). Mutations: the failure of `relC` dropped from `c5_sep`; `relC` in place of `relT` in the
  non-selection statement; inverse positivity dropped from it; a sign of the gate changed; the witness NOT replaced by
  the landed `n5`; the non-selection conclusion changed. Rule controls: a broken witness reads not-established in Q-REL
  alone; a landed `z5` that differs fails Q-POS and Q-REL.
- **S6 scope.** No declaration names `Complex`, `ℂ` or a landed dimension corollary of the native gate
  (`dim_of_nativeGate`, `dim_of_nativeGateOf`, `dim_of_nativeGateOf_dense`, `ne_two_of_nativeGate`,
  `ne_four_of_nativeGate`, `ne_five_of_nativeGate`, `ne_seven_of_nativeGate`, `not_even_of_nativeGate`,
  `three_of_nativeGate`, `three_of_nativeGate_of_two_le`, `three_of_nativeGateOf`, `three_of_nativeGateOf_dense`,
  `three_of_nativeGateOf_of_two_le`, `three_of_nativeGateOf_of_two_le_dense`, `det_of_nativeGate_three`,
  `piRotation_of_nativeGate_three`, `tangentPlus_of_nativeGate_three`); only `dim_of_ctrlGate`, `three_of_ctrlGate`
  and `relT_not_dimension_selecting` conclude an equation or inequation on `d`; no theorem concludes `NativeGate`
  without a leading `¬`, and only `ctrlGate_of_nativeGate` concludes `CtrlGate`. Mutations: a complex field; a positive
  native gate; a conclusion `d ≠ 5`; the landed selector read.
- **S7 reuse.** No declaration shares its name with an OIBridge declaration visible to it, or with a declaration of
  another module of the round; the imports are `OIBridge.OddChar` (parity, squeeze, C5) and `OIBridge.RelcSelectParity`
  with `OIBridge.ParityNot` (block). Mutations: a landed definition re-declared; a declaration of another module of
  the round re-declared; a second import.
- **S8 phrases.** The comments of the four modules — headers, docstrings and line comments — and, at a commit carrying
  it, the result note less the frozen earned reading and the frozen non-inference rule, contain none of the frozen
  phrases (case-insensitive, backticks removed, whitespace-normalized). They include "redundan", "relT is unnecessary",
  "relT follows from", "relT is independent", "equivalent to NativeGate", "inverse-stable", "preserved under
  inversion", "relT can replace relC", "relT alone", "posFwd alone suffices", "forward positivity implies inverse
  positivity", "physical gate", "adopted model", "OI selects", "globally minimal", "the frame is necessary",
  "selects d = 3", "design (round", "not for landing" and "UNBUILT". Mutations: a global redundancy claim in a header;
  an implication between the positivity clauses in a docstring; the design header. Controls: the frozen earned reading
  and non-inference rule pass when stated and each carries a frozen phrase elsewhere; "relT is unnecessary." alone,
  "inverse-stable", "relT is globally redundant", "a physical gate", "a globally minimal set", and the earned reading
  followed by "Hence relT is unnecessary.", each fail.
- **S9 count.** Exactly the frozen `#print axioms` lines of each module (2, 5, 15, 12), in order and distinct, each
  naming a declaration of its module. Mutations: an extra print; a duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the four computed tokens and no other, states the frozen earned reading exactly when all four cells are
  proved, and states the frozen non-inference rule. Controls: the note-token reader finds exactly the stated tokens;
  the earned reading is found when quoted across lines and not found when one sentence differs.
- **I, C.** As ODD-CHAR-1, with the four import lines after `OIBridge.OddChar`, in order, and the family after
  ODD-CHAR-1's. Controls: a dropped line and a reordered pair of imports fail; a changed status, a moved family, a
  whitespace change and the unchanged census fail.

`controls.py`:
- is blob `8cafc140b519495d1687a5507846d320c3c3295f` (2400 lines), generated from the four reference
  modules, the frozen family, the frozen earned reading and non-inference rule, and `D` by the round's generator;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 93 checks.

### Count facts

- the modules carry **34** frozen `#print axioms` lines (S9) — 2, 5, 15 and 12 — and 156 declarations;
- none of the 34 short names occurs in a `#print axioms` line at `D`, so the prints add 34 names to
  `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5826 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| parity | `finrank_plus_eq_finrank_minus_relC`, `not_even_of_relC` | built, axioms within `[propext, Classical.choice, Quot.sound]` | S1, V |
| selector | `ctrlGate_of_nativeGate`, `actT_slice_ctrl`, `blockData_of_ctrlGate`, `dim_of_ctrlGate`, `three_of_ctrlGate` | as above | S2, V |
| positivity | `frame_symm`, `relT_symm`, `relC_symm_of_relT`, `gateRel_symm`, `gSq_frame`, `gateRel_gSq`, `pairVal_gSq_prodState`, `gSq_core`, `gSq_posFwd`, `gSq_symm_value`, `gSq_not_posInv`, `not_nativeGate_gSq`, `not_nativeGate_gSqInv`, `gSq_sep`, `gSqInv_sep` | as above | S3, V |
| relation | `isNot_nC5`, `gC5_frame`, `gC5_relT`, `gC5_not_relC`, `selC5_target`, `selC5_core`, `prodEffVal_gC5_prodState`, `gC5_posFwd`, `gC5_posInv`, `c5_sep`, `not_nativeGate_gC5`, `relT_not_dimension_selecting` | as above | S4, V |
| scope | the modules' statements and proofs | no complex field, landed selector, positive native gate, or conclusion on `d` outside the selector | S6 |
| count | the 34 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs on the certified base `D` (`workflow_dispatch` on the disposable branch `claude/relc-select-dev`; the
Mathlib bridge job and the release gate read). Before run 1 the complete proposed statement list of the four draft
modules (167 declarations) and their hashes were recorded; the statements were frozen for runs 1 to 3.

| Run | Commit (module blobs: parity, block, squeeze, C5) | Workflow run | Result |
|---|---|---|---|
| 1 | `336caa53` (`5ce21b24`, `572496e4`, `9d3898ab`, `57cd6e5e`) | 37693331995 | **red**: the block module failed to elaborate — four `Function expected` errors where `hom 0 - u` was applied as a function inside the proof of `phi_lift_minus_ctrl`, and one unsolved goal there; the parity, squeeze and C5 modules built, and the release gate did not run |
| 2 | `7cda4570` (`5ce21b24`, `11e511ed`, `9d3898ab`, `57cd6e5e`) | 37693929094 | **green**: all 32 jobs `success`; the four modules built with each of the 38 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5864, no `sorryAx`; 303 legacy records intact; 41 receipts hold); linter warnings only (63) |
| 3 | `9a3d8f36` (`919dd539`, `11e511ed`, `3fe34e7d`, `c27cc451`) | 37695369269 | **green**: all 32 jobs `success`; 38 prints within the three axioms; release gate PASS (`lean-axioms` 5864, no `sorryAx`; 303 legacy records; 41 receipts); no warning in the parity, squeeze and C5 modules, and the block module's seven, all in its copies of DIM-1's proofs |
| amendment | `f062fcff` (`919dd539`, `11e511ed`, `8ef7aeb7`, `18565f7c`) | 37718803221 | **green**: all 32 jobs `success`; release gate PASS, every step (`lean-axioms` 5860 named results, no `sorryAx`; 303 legacy records intact; 41 receipts hold), the step requiring every declared print to report within the three axioms; no warning in the squeeze and C5 modules |

Run 2 changes the statements of `phi_lift_minus_ctrl`'s internal steps only (`hom 0` written `hom (0 : Fin d → ℝ)`),
inside a proof; no theorem statement, definition or context block changed between runs 1 and 2. Run 3 changes proofs
only — unused `simp` arguments, unreachable alternatives and unused tactics removed, and unused binder names in the
proof fields of `relCSplitEven` and `relCSplitOdd` — and leaves the block module unchanged; no theorem statement or
definition header changed.

**The statement-hygiene amendment.** After run 3 the design batch was closed, and the owner authorized one amendment
whose diff is exactly: `gSqInv_sep` stated with `gSq` in place of `gSq.symm.symm` (proved by `gSq_posFwd`, its
auxiliary `gSqInv_posInv`, which stated the `gSq.symm.symm` form and had no other use, removed); `not_dim_of_relT`
renamed `relT_not_dimension_selecting`; `relC_symm` renamed `relC_symm_of_relT`; and the `λ = 1` countercontrol of the
squeeze module removed (`gCtlFun`, `gCtlFun_apply`, `e5b`, `e5b_unit`, `nege5b_unit`, `sharpVec_x5`,
`sharpVec_nege5b`, `gCtl_value`, `gSq_ctl_test_value`, `gCtl_not_posFwd`), which no control reads; it stays in the
design history at `9a3d8f36`. The two renamed statements are otherwise identical, and every other declaration of the
four modules is that of run 3; the amendment's run is the design evidence for the frozen statement surface (156
declarations, 34 prints).

The reference modules differ from the amendment's only in comments: the module headers, which name the round and give
the final wording, and two comments inside proofs, one removed and one reworded. The census family differs from the
design family only in its text. The predicted execution tree below is the evidence for the frozen blobs.

Statement-level choices recorded as frozen: the parity theorem takes `NativeGate`'s `relC` field verbatim and nothing
else of the gate's clauses; `CtrlGate` is `NativeGate`'s fields verbatim without `relT`; the selector's statements are
DIM-1's with `NativeGate` replaced by `CtrlGate`; the positivity witnesses use PARITY-NOT-1's `n5`, `z5` and `x5`, and
their values are rational, so exact; the C5 witness uses its own NOT `nC5` and the landed axis `z5`.

### The predicted execution tree

The predicted execution tree, its controls reading and its exact-head run are recorded here before `F`.

## Stages

1. **C1** adds `controls.py`, blob `8cafc140b519495d1687a5507846d320c3c3295f`, to the record directory.
   Acceptance: the blob is the frozen blob.
2. **S1** adds the four modules, the four import lines and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the four modules with every printed
     axiom set within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only, and none of a copied declaration's; each passes
   `controls.py check` at its commit. A failure that such a repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S8 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`RELC-SELECT-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints
  exactly one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  the four modules with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and
  the release gate passing. The result note states each cell as its row words it, the earned reading in its frozen
  words when all four cells are proved, and the non-inference rule.
- **`RELC-SELECT-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names
  the failing check or job.

No outcome selects a dimension for a physical theory, adopts a premise, or edits the ROADMAP. Correctness bands are
unchanged by either outcome: the round is consistency-axis work.
