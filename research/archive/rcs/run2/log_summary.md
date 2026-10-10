# Build diagnostics: OIBridge.RelcSelect{Parity,Block,Squeeze,C5}

Source: GitHub Actions job 113040684292, repo amaybaum/incompleteness (last 5000 log lines, fetched via get_job_logs). Runner timestamps stripped; message text otherwise verbatim. Warnings are listed in log order.

## Summary

| Module | Status line | errors | warnings | by linter | axiom lines | non-standard axioms |
|---|---|---|---|---|---|---|
| RelcSelectParity | `⚠ [3638/3643] Built OIBridge.RelcSelectParity (12s)` | 0 | 30 | unreachableTactic: 6, unusedTactic: 8, unusedVariables: 16 | 2 | 0 |
| RelcSelectBlock | `⚠ [3641/3643] Built OIBridge.RelcSelectBlock (9.8s)` | 0 | 7 | unnecessarySeqFocus: 1, unusedSimpArgs: 6 | 5 | 0 |
| RelcSelectSqueeze | `⚠ [3640/3643] Built OIBridge.RelcSelectSqueeze (19s)` | 0 | 15 | unnecessarySeqFocus: 3, unreachableTactic: 5, unusedSimpArgs: 2, unusedTactic: 5 | 19 | 0 |
| RelcSelectC5 | `⚠ [3639/3643] Built OIBridge.RelcSelectC5 (17s)` | 0 | 11 | unreachableTactic: 3, unusedSimpArgs: 5, unusedTactic: 3 | 12 | 0 |

## OIBridge.RelcSelectParity

Status line:

```
⚠ [3638/3643] Built OIBridge.RelcSelectParity (12s)
```

### errors (0)

None.

### warnings (30)

Counts by linter: unreachableTactic: 6, unusedTactic: 8, unusedVariables: 16

1.

```
warning: OIBridge/RelcSelectParity.lean:233:11: Variable name `F₁` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F₁

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

2.

```
warning: OIBridge/RelcSelectParity.lean:233:14: Variable name `F₂` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F₂

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

3.

```
warning: OIBridge/RelcSelectParity.lean:233:48: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

4.

```
warning: OIBridge/RelcSelectParity.lean:233:77: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

5.

```
warning: OIBridge/RelcSelectParity.lean:234:12: Variable name `c` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _c

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

6.

```
warning: OIBridge/RelcSelectParity.lean:234:14: Variable name `F` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

7.

```
warning: OIBridge/RelcSelectParity.lean:234:47: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

8.

```
warning: OIBridge/RelcSelectParity.lean:234:76: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

9.

```
warning: OIBridge/RelcSelectParity.lean:245:11: Variable name `F₁` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F₁

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

10.

```
warning: OIBridge/RelcSelectParity.lean:245:14: Variable name `F₂` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F₂

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

11.

```
warning: OIBridge/RelcSelectParity.lean:245:48: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

12.

```
warning: OIBridge/RelcSelectParity.lean:245:77: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

13.

```
warning: OIBridge/RelcSelectParity.lean:246:12: Variable name `c` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _c

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

14.

```
warning: OIBridge/RelcSelectParity.lean:246:14: Variable name `F` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _F

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

15.

```
warning: OIBridge/RelcSelectParity.lean:246:47: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

16.

```
warning: OIBridge/RelcSelectParity.lean:246:76: Variable name `u` is not explicitly referenced.

Hint: The binding can be removed (if unused) or named `_` (if used implicitly). Alternatively, prefix the name with `_` to silence this warning:
  [apply] _u

Note: This linter can be disabled with `set_option linter.unusedVariables false`
```

17.

```
warning: OIBridge/RelcSelectParity.lean:296:71: Unused tactic linter: `done` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

18.

```
warning: OIBridge/RelcSelectParity.lean:297:6: Unused tactic linter: `(simp only [Module.finrank_prod, Module.finrank_linearMap]; done)` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

19.

```
warning: OIBridge/RelcSelectParity.lean:297:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

20.

```
warning: OIBridge/RelcSelectParity.lean:312:70: Unused tactic linter: `done` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

21.

```
warning: OIBridge/RelcSelectParity.lean:313:6: Unused tactic linter: `(simp only [Module.finrank_prod, Module.finrank_linearMap]; done)` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

22.

```
warning: OIBridge/RelcSelectParity.lean:313:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

23.

```
warning: OIBridge/RelcSelectParity.lean:332:6: Unused tactic linter: `linarith` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

24.

```
warning: OIBridge/RelcSelectParity.lean:333:6: Unused tactic linter: `nlinarith [h1]` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

25.

```
warning: OIBridge/RelcSelectParity.lean:337:6: Unused tactic linter: `linarith` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

26.

```
warning: OIBridge/RelcSelectParity.lean:338:6: Unused tactic linter: `nlinarith [h2]` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

27.

```
warning: OIBridge/RelcSelectParity.lean:332:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

28.

```
warning: OIBridge/RelcSelectParity.lean:333:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

29.

```
warning: OIBridge/RelcSelectParity.lean:337:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

30.

```
warning: OIBridge/RelcSelectParity.lean:338:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

### axiom lines (2)

```
info: OIBridge/RelcSelectParity.lean:377:0: 'OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectParity.lean:378:0: 'OIBridge.RelcSelect.not_even_of_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Axiom sets other than `[propext, Classical.choice, Quot.sound]`: none.

## OIBridge.RelcSelectBlock

Status line:

```
⚠ [3641/3643] Built OIBridge.RelcSelectBlock (9.8s)
```

### errors (0)

None.

### warnings (7)

Counts by linter: unnecessarySeqFocus: 1, unusedSimpArgs: 6

1.

```
warning: OIBridge/RelcSelectBlock.lean:602:23: This simp argument is unused:
  LinearMap.map_add₂

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
    hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

2.

```
warning: OIBridge/RelcSelectBlock.lean:602:52: This simp argument is unused:
  LinearMap.map_smul₂

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
    hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

3.

```
warning: OIBridge/RelcSelectBlock.lean:604:10: This simp argument is unused:
  eq_self_iff_true

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
    LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hvv', if_true]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

4.

```
warning: OIBridge/RelcSelectBlock.lean:618:25: This simp argument is unused:
  LinearMap.map_add₂

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, hf, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
    smul_eq_mul, hd00, hd0, hd0', hS0', hS1']

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

5.

```
warning: OIBridge/RelcSelectBlock.lean:618:54: This simp argument is unused:
  LinearMap.map_smul₂

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
    smul_eq_mul, hd00, hd0, hd0', hS0', hS1']

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

6.

```
warning: OIBridge/RelcSelectBlock.lean:619:70: This simp argument is unused:
  hd0

Hint: Omit it from the simp argument list.
  [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
    LinearMap.smul_apply, smul_eq_mul, hd00, hd0', hS0', hS1']

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

7.

```
warning: OIBridge/RelcSelectBlock.lean:619:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

### axiom lines (5)

```
info: OIBridge/RelcSelectBlock.lean:761:0: 'OIBridge.RelcSelect.ctrlGate_of_nativeGate' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:762:0: 'OIBridge.RelcSelect.actT_slice_ctrl' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:763:0: 'OIBridge.RelcSelect.blockData_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:764:0: 'OIBridge.RelcSelect.dim_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
info: OIBridge/RelcSelectBlock.lean:765:0: 'OIBridge.RelcSelect.three_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Axiom sets other than `[propext, Classical.choice, Quot.sound]`: none.

## OIBridge.RelcSelectSqueeze

Status line:

```
⚠ [3640/3643] Built OIBridge.RelcSelectSqueeze (19s)
```

### errors (0)

None.

### warnings (15)

Counts by linter: unnecessarySeqFocus: 3, unreachableTactic: 5, unusedSimpArgs: 2, unusedTactic: 5

1.

```
warning: OIBridge/RelcSelectSqueeze.lean:175:70: This simp argument is unused:
  sqCls

Hint: Omit it from the simp argument list.
  [apply] simp +decide [gSq_apply, gSqFun_apply, sqW, sqR, sqK, sqPc, sqPt, sqSig, perm5, odd5, prodState_apply,
    corner_zero, corner_one, z5]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

2.

```
warning: OIBridge/RelcSelectSqueeze.lean:175:91: This simp argument is unused:
  odd5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [gSq_apply, gSqFun_apply, sqW, sqR, sqK, sqPc, sqPt, sqCls, sqSig, perm5, prodState_apply,
    corner_zero, corner_one, z5]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

3.

```
warning: OIBridge/RelcSelectSqueeze.lean:176:56: Unused tactic linter: `norm_num` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

4.

```
warning: OIBridge/RelcSelectSqueeze.lean:176:56: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

5.

```
warning: OIBridge/RelcSelectSqueeze.lean:369:6: Unused tactic linter: `linarith [h]` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

6.

```
warning: OIBridge/RelcSelectSqueeze.lean:369:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

7.

```
warning: OIBridge/RelcSelectSqueeze.lean:389:6: Unused tactic linter: `simp only [pairVal, gSq_apply, gSqFun_apply, prodState_apply, sum_univ_six']` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

8.

```
warning: OIBridge/RelcSelectSqueeze.lean:390:6: Unused tactic linter: `simp +decide [sqW, sqR, sqK, sqPc, sqPt, sqCls, sqSig, perm5, odd5] <;> ring` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

9.

```
warning: OIBridge/RelcSelectSqueeze.lean:389:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

10.

```
warning: OIBridge/RelcSelectSqueeze.lean:390:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

11.

```
warning: OIBridge/RelcSelectSqueeze.lean:447:49: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

12.

```
warning: OIBridge/RelcSelectSqueeze.lean:485:6: Unused tactic linter: `(rw [LinearEquiv.symm_symm]; exact gSq_posFwd x hx y hy)` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

13.

```
warning: OIBridge/RelcSelectSqueeze.lean:485:6: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

14.

```
warning: OIBridge/RelcSelectSqueeze.lean:556:30: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

15.

```
warning: OIBridge/RelcSelectSqueeze.lean:562:25: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice

Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

### axiom lines (19)

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

Axiom sets other than `[propext, Classical.choice, Quot.sound]`: none.

## OIBridge.RelcSelectC5

Status line:

```
⚠ [3639/3643] Built OIBridge.RelcSelectC5 (17s)
```

### errors (0)

None.

### warnings (11)

Counts by linter: unreachableTactic: 3, unusedSimpArgs: 5, unusedTactic: 3

1.

```
warning: OIBridge/RelcSelectC5.lean:119:55: This simp argument is unused:
  pcC5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [sgnC5, ptC5]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

2.

```
warning: OIBridge/RelcSelectC5.lean:119:61: This simp argument is unused:
  ptC5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [sgnC5, pcC5]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

3.

```
warning: OIBridge/RelcSelectC5.lean:160:31: Unused tactic linter: `simp_all` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

4.

```
warning: OIBridge/RelcSelectC5.lean:160:31: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

5.

```
warning: OIBridge/RelcSelectC5.lean:166:22: Unused tactic linter: `norm_num` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

6.

```
warning: OIBridge/RelcSelectC5.lean:166:22: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

7.

```
warning: OIBridge/RelcSelectC5.lean:170:77: This simp argument is unused:
  pcC5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [actT_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, sgnC5, ptC5, oddC5, OddChar.entW]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

8.

```
warning: OIBridge/RelcSelectC5.lean:170:83: This simp argument is unused:
  ptC5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [actT_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, sgnC5, pcC5, oddC5, OddChar.entW]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

9.

```
warning: OIBridge/RelcSelectC5.lean:170:89: This simp argument is unused:
  oddC5

Hint: Omit it from the simp argument list.
  [apply] simp +decide [actT_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, sgnC5, pcC5, ptC5, OddChar.entW]

Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

10.

```
warning: OIBridge/RelcSelectC5.lean:171:22: Unused tactic linter: `norm_num` does nothing

Note: This linter can be disabled with `set_option linter.unusedTactic false`
```

11.

```
warning: OIBridge/RelcSelectC5.lean:171:22: this tactic is never executed

Note: This linter can be disabled with `set_option linter.unreachableTactic false`
```

### axiom lines (12)

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

Axiom sets other than `[propext, Classical.choice, Quot.sound]`: none.
