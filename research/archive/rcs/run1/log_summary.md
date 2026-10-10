# Lean build diagnostics: job 113038711555 (amaybaum/incompleteness)

Job `Mathlib bridge`, head `336caa539b61f5e04295a86a6f19586eee0a3356`, run 37693331995, conclusion: **failure**.
Source: the MCP `get_job_logs` call returned only the last 4999 of 37599 log lines. That covers lake targets [3638/3643] through the end of the job, which includes all four RelcSelect modules. Timestamps are stripped below.

## RelcSelectParity

**Status: built (with warnings)**

    ⚠ [3638/3643] Built OIBridge.RelcSelectParity (10s)

### Errors (0)

None.

### Warnings (30)

- OIBridge/RelcSelectParity.lean:233:11: Variable name `F₁` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:233:14: Variable name `F₂` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:233:48: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:233:77: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:234:12: Variable name `c` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:234:14: Variable name `F` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:234:47: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:234:76: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:245:11: Variable name `F₁` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:245:14: Variable name `F₂` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:245:48: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:245:77: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:246:12: Variable name `c` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:246:14: Variable name `F` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:246:47: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:246:76: Variable name `u` is not explicitly referenced.
- OIBridge/RelcSelectParity.lean:296:71: Unused tactic linter: `done` does nothing
- OIBridge/RelcSelectParity.lean:297:6: Unused tactic linter: `(simp only [Module.finrank_prod, Module.finrank_linearMap]; done)` does nothing
- OIBridge/RelcSelectParity.lean:297:6: this tactic is never executed
- OIBridge/RelcSelectParity.lean:312:70: Unused tactic linter: `done` does nothing
- OIBridge/RelcSelectParity.lean:313:6: Unused tactic linter: `(simp only [Module.finrank_prod, Module.finrank_linearMap]; done)` does nothing
- OIBridge/RelcSelectParity.lean:313:6: this tactic is never executed
- OIBridge/RelcSelectParity.lean:332:6: Unused tactic linter: `linarith` does nothing
- OIBridge/RelcSelectParity.lean:333:6: Unused tactic linter: `nlinarith [h1]` does nothing
- OIBridge/RelcSelectParity.lean:337:6: Unused tactic linter: `linarith` does nothing
- OIBridge/RelcSelectParity.lean:338:6: Unused tactic linter: `nlinarith [h2]` does nothing
- OIBridge/RelcSelectParity.lean:332:6: this tactic is never executed
- OIBridge/RelcSelectParity.lean:333:6: this tactic is never executed
- OIBridge/RelcSelectParity.lean:337:6: this tactic is never executed
- OIBridge/RelcSelectParity.lean:338:6: this tactic is never executed

### Axiom reports (2)

```
info: OIBridge/RelcSelectParity.lean:377:0: 'OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectParity.lean:378:0: 'OIBridge.RelcSelect.not_even_of_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## RelcSelectBlock

**Status: FAILED**

    ✖ [3641/3643] Building OIBridge.RelcSelectBlock (7.1s)

### Errors (5)

```
error: OIBridge/RelcSelectBlock.lean:339:48: Function expected at
  hom 0 - u
but this term has type
  ?m.472

Note: Expected a function because this term is being applied to the argument
  ν
```

```
error: OIBridge/RelcSelectBlock.lean:340:48: Function expected at
  hom 0 - u
but this term has type
  ?m.536

Note: Expected a function because this term is being applied to the argument
  ν
```

```
error: OIBridge/RelcSelectBlock.lean:342:15: unsolved goals
d : ℕ
z : Fin d → ℝ
N : (Fin d → ℝ) →ₗ[ℝ] Fin d → ℝ
G : W d ≃ₗ[ℝ] W d
hN : IsNot (eball d) z N
hG : CtrlGate (eball d) z N G
c : Fin d → ℝ
hc : ∑ j, c j ^ 2 ≤ 1
hzc : ∑ j, z j * c j = 0
u : HVec d
hu0 : u 0 = 0
hu : ∑ μ, u μ ^ 2 = 1
hNu : (homMap N) u = -u
c' : Fin d → ℝ
hc' : ∑ j, c' j ^ 2 ≤ 1
hzc' : ∑ j, z j * c' j = 0
hτ : ∑ j, Matrix.vecTail u j ^ 2 = 1
hτ' : ∑ j, (-Matrix.vecTail u) j ^ 2 = 1
hfdef : hom 0 - u = hom (-Matrix.vecTail u)
hfL : Lor (hom 0 - u)
hHf : (homMap N) (hom 0 - u) = hom 0 + u
hh0u : ∑ ν, hom 0 ν * u ν = 0
huu : ∑ ν, u ν * u ν = 1
ν : Fin (d + 1)
⊢ hom 0 ν * sorry - u ν * sorry = -(hom 0 ν * u ν * 2) + hom 0 ν ^ 2 + u ν ^ 2
```

```
error: OIBridge/RelcSelectBlock.lean:346:48: Function expected at
  hom 0 - u
but this term has type
  ?m.593

Note: Expected a function because this term is being applied to the argument
  ν
```

```
error: OIBridge/RelcSelectBlock.lean:347:48: Function expected at
  hom 0 - u
but this term has type
  ?m.640

Note: Expected a function because this term is being applied to the argument
  ν
```

### Other info messages (1)

```
info: OIBridge/RelcSelectBlock.lean:342:37: Try this:
  [apply] ring_nf
  
  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
    
  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
```

### Warnings (7)

- OIBridge/RelcSelectBlock.lean:602:23: This simp argument is unused: [LinearMap.map_add₂]
- OIBridge/RelcSelectBlock.lean:602:52: This simp argument is unused: [LinearMap.map_smul₂]
- OIBridge/RelcSelectBlock.lean:604:10: This simp argument is unused: [eq_self_iff_true]
- OIBridge/RelcSelectBlock.lean:618:25: This simp argument is unused: [LinearMap.map_add₂]
- OIBridge/RelcSelectBlock.lean:618:54: This simp argument is unused: [LinearMap.map_smul₂]
- OIBridge/RelcSelectBlock.lean:619:70: This simp argument is unused: [hd0]
- OIBridge/RelcSelectBlock.lean:619:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

### Axiom reports (5)

```
info: OIBridge/RelcSelectBlock.lean:761:0: 'OIBridge.RelcSelect.ctrlGate_of_nativeGate' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:762:0: 'OIBridge.RelcSelect.actT_slice_ctrl' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:763:0: 'OIBridge.RelcSelect.blockData_of_ctrlGate' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:764:0: 'OIBridge.RelcSelect.dim_of_ctrlGate' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:765:0: 'OIBridge.RelcSelect.three_of_ctrlGate' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]
```

## RelcSelectSqueeze

**Status: built (with warnings)**

    ⚠ [3640/3643] Built OIBridge.RelcSelectSqueeze (14s)

### Errors (0)

None.

### Warnings (15)

- OIBridge/RelcSelectSqueeze.lean:175:70: This simp argument is unused: [sqCls]
- OIBridge/RelcSelectSqueeze.lean:175:91: This simp argument is unused: [odd5]
- OIBridge/RelcSelectSqueeze.lean:176:56: Unused tactic linter: `norm_num` does nothing
- OIBridge/RelcSelectSqueeze.lean:176:56: this tactic is never executed
- OIBridge/RelcSelectSqueeze.lean:369:6: Unused tactic linter: `linarith [h]` does nothing
- OIBridge/RelcSelectSqueeze.lean:369:6: this tactic is never executed
- OIBridge/RelcSelectSqueeze.lean:389:6: Unused tactic linter: `simp only [pairVal, gSq_apply, gSqFun_apply, prodState_apply, sum_univ_six']` does nothing
- OIBridge/RelcSelectSqueeze.lean:390:6: Unused tactic linter: `simp +decide [sqW, sqR, sqK, sqPc, sqPt, sqCls, sqSig, perm5, odd5] <;> ring` does nothing
- OIBridge/RelcSelectSqueeze.lean:389:6: this tactic is never executed
- OIBridge/RelcSelectSqueeze.lean:390:6: this tactic is never executed
- OIBridge/RelcSelectSqueeze.lean:447:49: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
- OIBridge/RelcSelectSqueeze.lean:485:6: Unused tactic linter: `(rw [LinearEquiv.symm_symm]; exact gSq_posFwd x hx y hy)` does nothing
- OIBridge/RelcSelectSqueeze.lean:485:6: this tactic is never executed
- OIBridge/RelcSelectSqueeze.lean:556:30: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
- OIBridge/RelcSelectSqueeze.lean:562:25: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

### Axiom reports (19)

```
info: OIBridge/RelcSelectSqueeze.lean:575:0: 'OIBridge.RelcSelect.frame_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:576:0: 'OIBridge.RelcSelect.relT_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:577:0: 'OIBridge.RelcSelect.relC_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:578:0: 'OIBridge.RelcSelect.gateRel_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:579:0: 'OIBridge.RelcSelect.gSq_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:580:0: 'OIBridge.RelcSelect.gateRel_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:581:0: 'OIBridge.RelcSelect.pairVal_gSq_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:582:0: 'OIBridge.RelcSelect.gSq_core' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:583:0: 'OIBridge.RelcSelect.gSq_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:584:0: 'OIBridge.RelcSelect.gSq_symm_value' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:585:0: 'OIBridge.RelcSelect.gSq_not_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:586:0: 'OIBridge.RelcSelect.not_nativeGate_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:587:0: 'OIBridge.RelcSelect.not_nativeGate_gSqInv' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:588:0: 'OIBridge.RelcSelect.gSqInv_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:589:0: 'OIBridge.RelcSelect.gSq_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:590:0: 'OIBridge.RelcSelect.gSqInv_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:591:0: 'OIBridge.RelcSelect.gCtl_value' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:592:0: 'OIBridge.RelcSelect.gSq_ctl_test_value' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectSqueeze.lean:593:0: 'OIBridge.RelcSelect.gCtl_not_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## RelcSelectC5

**Status: built (with warnings)**

    ⚠ [3639/3643] Built OIBridge.RelcSelectC5 (14s)

### Errors (0)

None.

### Warnings (11)

- OIBridge/RelcSelectC5.lean:119:55: This simp argument is unused: [pcC5]
- OIBridge/RelcSelectC5.lean:119:61: This simp argument is unused: [ptC5]
- OIBridge/RelcSelectC5.lean:160:31: Unused tactic linter: `simp_all` does nothing
- OIBridge/RelcSelectC5.lean:160:31: this tactic is never executed
- OIBridge/RelcSelectC5.lean:166:22: Unused tactic linter: `norm_num` does nothing
- OIBridge/RelcSelectC5.lean:166:22: this tactic is never executed
- OIBridge/RelcSelectC5.lean:170:77: This simp argument is unused: [pcC5]
- OIBridge/RelcSelectC5.lean:170:83: This simp argument is unused: [ptC5]
- OIBridge/RelcSelectC5.lean:170:89: This simp argument is unused: [oddC5]
- OIBridge/RelcSelectC5.lean:171:22: Unused tactic linter: `norm_num` does nothing
- OIBridge/RelcSelectC5.lean:171:22: this tactic is never executed

### Axiom reports (12)

```
info: OIBridge/RelcSelectC5.lean:404:0: 'OIBridge.RelcSelect.isNot_nC5' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:405:0: 'OIBridge.RelcSelect.gC5_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:406:0: 'OIBridge.RelcSelect.gC5_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:407:0: 'OIBridge.RelcSelect.gC5_not_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:408:0: 'OIBridge.RelcSelect.selC5_target' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:409:0: 'OIBridge.RelcSelect.selC5_core' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:410:0: 'OIBridge.RelcSelect.prodEffVal_gC5_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:411:0: 'OIBridge.RelcSelect.gC5_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:412:0: 'OIBridge.RelcSelect.gC5_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:413:0: 'OIBridge.RelcSelect.c5_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:414:0: 'OIBridge.RelcSelect.not_nativeGate_gC5' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectC5.lean:415:0: 'OIBridge.RelcSelect.not_dim_of_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Final lake summary

```
error: Lean exited with code 1
Some required targets logged failures:
- OIBridge.RelcSelectBlock
error: build failed
##[error]Process completed with exit code 1.
```

## Steps

| # | Step | Conclusion |
|---|---|---|
| 5 | Build | failure |
| 6 | Release gate | **skipped** (did not run) |

The release gate step did not run because the Build step failed.
