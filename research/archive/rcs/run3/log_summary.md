# Build diagnostics — job 113045674563 (amaybaum/incompleteness)

Source: `raw.log` beside this file (GitHub job-log tail, 5000 lines of 37314; all four target modules fall inside it). Lines below are verbatim with runner timestamps.

## OIBridge.RelcSelectParity

**Lake status line**

```
2026-10-07T22:21:10.2854065Z ℹ [3638/3643] Built OIBridge.RelcSelectParity (11s)
```

**Errors** (0)

None.

**Warnings** (0)

None.

**Axiom reports** (2; non-standard: 0)

```
2026-10-07T22:21:10.2884489Z info: OIBridge/RelcSelectParity.lean:365:0: 'OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:10.2914413Z info: OIBridge/RelcSelectParity.lean:366:0: 'OIBridge.RelcSelect.not_even_of_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## OIBridge.RelcSelectBlock

**Lake status line**

```
2026-10-07T22:21:21.9058175Z ⚠ [3641/3643] Built OIBridge.RelcSelectBlock (11s)
```

**Errors** (0)

None.

**Warnings** (7)

Warning 1:

```
2026-10-07T22:21:21.9059482Z warning: OIBridge/RelcSelectBlock.lean:602:23: This simp argument is unused:
2026-10-07T22:21:21.9060317Z   LinearMap.map_add₂
2026-10-07T22:21:21.9060584Z 
2026-10-07T22:21:21.9060839Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9062115Z   [apply] simp only [ht, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
2026-10-07T22:21:21.9063466Z     hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]
2026-10-07T22:21:21.9063866Z 
2026-10-07T22:21:21.9064287Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 2:

```
2026-10-07T22:21:21.9065293Z warning: OIBridge/RelcSelectBlock.lean:602:52: This simp argument is unused:
2026-10-07T22:21:21.9066088Z   LinearMap.map_smul₂
2026-10-07T22:21:21.9066422Z 
2026-10-07T22:21:21.9066576Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9067357Z   [apply] simp only [ht, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,
2026-10-07T22:21:21.9068248Z     hd00, hd0, hd0', hvv', eq_self_iff_true, if_true]
2026-10-07T22:21:21.9068527Z 
2026-10-07T22:21:21.9068805Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 3:

```
2026-10-07T22:21:21.9069462Z warning: OIBridge/RelcSelectBlock.lean:604:10: This simp argument is unused:
2026-10-07T22:21:21.9069935Z   eq_self_iff_true
2026-10-07T22:21:21.9070095Z 
2026-10-07T22:21:21.9070226Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9070907Z   [apply] simp only [ht, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
2026-10-07T22:21:21.9071696Z     LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hvv', if_true]
2026-10-07T22:21:21.9072030Z 
2026-10-07T22:21:21.9072302Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 4:

```
2026-10-07T22:21:21.9073242Z warning: OIBridge/RelcSelectBlock.lean:618:25: This simp argument is unused:
2026-10-07T22:21:21.9073760Z   LinearMap.map_add₂
2026-10-07T22:21:21.9073930Z 
2026-10-07T22:21:21.9074071Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9074786Z   [apply] simp only [ht, hf, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
2026-10-07T22:21:21.9075404Z     smul_eq_mul, hd00, hd0, hd0', hS0', hS1']
2026-10-07T22:21:21.9075638Z 
2026-10-07T22:21:21.9075909Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 5:

```
2026-10-07T22:21:21.9076550Z warning: OIBridge/RelcSelectBlock.lean:618:54: This simp argument is unused:
2026-10-07T22:21:21.9077044Z   LinearMap.map_smul₂
2026-10-07T22:21:21.9077215Z 
2026-10-07T22:21:21.9077353Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9078030Z   [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply,
2026-10-07T22:21:21.9078627Z     smul_eq_mul, hd00, hd0, hd0', hS0', hS1']
2026-10-07T22:21:21.9078864Z 
2026-10-07T22:21:21.9079253Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 6:

```
2026-10-07T22:21:21.9079902Z warning: OIBridge/RelcSelectBlock.lean:619:70: This simp argument is unused:
2026-10-07T22:21:21.9080353Z   hd0
2026-10-07T22:21:21.9080482Z 
2026-10-07T22:21:21.9080613Z Hint: Omit it from the simp argument list.
2026-10-07T22:21:21.9081291Z   [apply] simp only [ht, hf, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul, LinearMap.add_apply,
2026-10-07T22:21:21.9081952Z     LinearMap.smul_apply, smul_eq_mul, hd00, hd0', hS0', hS1']
2026-10-07T22:21:21.9082264Z 
2026-10-07T22:21:21.9082527Z Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
```

Warning 7:

```
2026-10-07T22:21:21.9083497Z warning: OIBridge/RelcSelectBlock.lean:619:93: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
2026-10-07T22:21:21.9083963Z 
2026-10-07T22:21:21.9084257Z Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
```

**Axiom reports** (5; non-standard: 0)

```
2026-10-07T22:21:21.9085317Z info: OIBridge/RelcSelectBlock.lean:761:0: 'OIBridge.RelcSelect.ctrlGate_of_nativeGate' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:21.9086551Z info: OIBridge/RelcSelectBlock.lean:762:0: 'OIBridge.RelcSelect.actT_slice_ctrl' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:21.9087757Z info: OIBridge/RelcSelectBlock.lean:763:0: 'OIBridge.RelcSelect.blockData_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:21.9088951Z info: OIBridge/RelcSelectBlock.lean:764:0: 'OIBridge.RelcSelect.dim_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:21.9090115Z info: OIBridge/RelcSelectBlock.lean:765:0: 'OIBridge.RelcSelect.three_of_ctrlGate' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## OIBridge.RelcSelectSqueeze

**Lake status line**

```
2026-10-07T22:21:19.1980731Z ℹ [3640/3643] Built OIBridge.RelcSelectSqueeze (20s)
```

**Errors** (0)

None.

**Warnings** (0)

None.

**Axiom reports** (19; non-standard: 0)

```
2026-10-07T22:21:19.1994554Z info: OIBridge/RelcSelectSqueeze.lean:571:0: 'OIBridge.RelcSelect.frame_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2024847Z info: OIBridge/RelcSelectSqueeze.lean:572:0: 'OIBridge.RelcSelect.relT_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2054478Z info: OIBridge/RelcSelectSqueeze.lean:573:0: 'OIBridge.RelcSelect.relC_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2084470Z info: OIBridge/RelcSelectSqueeze.lean:574:0: 'OIBridge.RelcSelect.gateRel_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2114423Z info: OIBridge/RelcSelectSqueeze.lean:575:0: 'OIBridge.RelcSelect.gSq_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2120865Z info: OIBridge/RelcSelectSqueeze.lean:576:0: 'OIBridge.RelcSelect.gateRel_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2123795Z info: OIBridge/RelcSelectSqueeze.lean:577:0: 'OIBridge.RelcSelect.pairVal_gSq_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2126192Z info: OIBridge/RelcSelectSqueeze.lean:578:0: 'OIBridge.RelcSelect.gSq_core' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2128441Z info: OIBridge/RelcSelectSqueeze.lean:579:0: 'OIBridge.RelcSelect.gSq_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2130688Z info: OIBridge/RelcSelectSqueeze.lean:580:0: 'OIBridge.RelcSelect.gSq_symm_value' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2133234Z info: OIBridge/RelcSelectSqueeze.lean:581:0: 'OIBridge.RelcSelect.gSq_not_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2135533Z info: OIBridge/RelcSelectSqueeze.lean:582:0: 'OIBridge.RelcSelect.not_nativeGate_gSq' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2137908Z info: OIBridge/RelcSelectSqueeze.lean:583:0: 'OIBridge.RelcSelect.not_nativeGate_gSqInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2140521Z info: OIBridge/RelcSelectSqueeze.lean:584:0: 'OIBridge.RelcSelect.gSqInv_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2142939Z info: OIBridge/RelcSelectSqueeze.lean:585:0: 'OIBridge.RelcSelect.gSq_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2145122Z info: OIBridge/RelcSelectSqueeze.lean:586:0: 'OIBridge.RelcSelect.gSqInv_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2147352Z info: OIBridge/RelcSelectSqueeze.lean:587:0: 'OIBridge.RelcSelect.gCtl_value' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2149506Z info: OIBridge/RelcSelectSqueeze.lean:588:0: 'OIBridge.RelcSelect.gSq_ctl_test_value' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:19.2151893Z info: OIBridge/RelcSelectSqueeze.lean:589:0: 'OIBridge.RelcSelect.gCtl_not_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## OIBridge.RelcSelectC5

**Lake status line**

```
2026-10-07T22:21:17.8972351Z ℹ [3639/3643] Built OIBridge.RelcSelectC5 (19s)
```

**Errors** (0)

None.

**Warnings** (0)

None.

**Axiom reports** (12; non-standard: 0)

```
2026-10-07T22:21:17.8974233Z info: OIBridge/RelcSelectC5.lean:404:0: 'OIBridge.RelcSelect.isNot_nC5' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8976416Z info: OIBridge/RelcSelectC5.lean:405:0: 'OIBridge.RelcSelect.gC5_frame' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8978212Z info: OIBridge/RelcSelectC5.lean:406:0: 'OIBridge.RelcSelect.gC5_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8980180Z info: OIBridge/RelcSelectC5.lean:407:0: 'OIBridge.RelcSelect.gC5_not_relC' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8982114Z info: OIBridge/RelcSelectC5.lean:408:0: 'OIBridge.RelcSelect.selC5_target' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8984334Z info: OIBridge/RelcSelectC5.lean:409:0: 'OIBridge.RelcSelect.selC5_core' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8986786Z info: OIBridge/RelcSelectC5.lean:410:0: 'OIBridge.RelcSelect.prodEffVal_gC5_prodState' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8989111Z info: OIBridge/RelcSelectC5.lean:411:0: 'OIBridge.RelcSelect.gC5_posFwd' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8991169Z info: OIBridge/RelcSelectC5.lean:412:0: 'OIBridge.RelcSelect.gC5_posInv' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8993426Z info: OIBridge/RelcSelectC5.lean:413:0: 'OIBridge.RelcSelect.c5_sep' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8995509Z info: OIBridge/RelcSelectC5.lean:414:0: 'OIBridge.RelcSelect.not_nativeGate_gC5' depends on axioms: [propext, Classical.choice, Quot.sound]
2026-10-07T22:21:17.8997581Z info: OIBridge/RelcSelectC5.lean:415:0: 'OIBridge.RelcSelect.not_dim_of_relT' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Release gate

```
2026-10-07T22:22:16.9472183Z release gate
2026-10-07T22:22:16.9472517Z ====================================================================
2026-10-07T22:22:16.9473549Z   PASS  toolchain        toolchain_check: OK (build entry present, unicode-fix.tex co
2026-10-07T22:22:16.9474426Z   PASS  staleness        staleness_check: OK (13 matched, 0 unstamped)
2026-10-07T22:22:16.9475313Z   PASS  baseline-label   baseline_label_check: OK (no baseline archives named)
2026-10-07T22:22:16.9475946Z   PASS  voice            voice_check: OK (no manuscript-voice history narration; 40 m
2026-10-07T22:22:16.9476661Z   PASS  voice-scope      voice_scope_test: OK (6 scope case(s); the checker scans the
2026-10-07T22:22:16.9477611Z   PASS  ci-gate-presence ci_gate_presence_test: OK (CI runs the real release gate)
2026-10-07T22:22:16.9478200Z   PASS  artifact-placement artifact_placement_check: OK (no unaccounted root artifact; 
2026-10-07T22:22:16.9478814Z   PASS  manifest-drift   build_migration_manifest --check: OK (91 artifacts; both gen
2026-10-07T22:22:16.9479386Z   PASS  claims           claims_check: OK (no withdrawn result asserted unconditional
2026-10-07T22:22:16.9479914Z   PASS  duplicate        duplicate_check: OK (no paragraph repeated within a file)
2026-10-07T22:22:16.9480427Z   PASS  mirror           mirror_check: 0 chapter line(s) absent from FULL.md
2026-10-07T22:22:16.9480933Z   PASS  citation         citation_check: 112 citation(s), 0 broken, 0 duplicate bib n
2026-10-07T22:22:16.9481486Z   PASS  architecture     architecture_check: 259 invariant(s), 0 violation(s), 0 self
2026-10-07T22:22:16.9487013Z   PASS  dependency-label dependency_label_check: OK (no stale dependency label, 41 fi
2026-10-07T22:22:16.9487659Z   PASS  coverage         coverage_check: OK (129 canonical statements, 19 unattached 
2026-10-07T22:22:16.9488196Z   PASS  lean-axioms      lean_axiom_check: OK (5864 named result(s) reported, no sorr
2026-10-07T22:22:16.9488762Z   PASS  lean-manuscript  lean_manuscript_census: OK (every cited identifier and path 
2026-10-07T22:22:16.9489320Z   PASS  legacy-records   LEGACY  303 record(s) in 75 closed namespace(s), all intact
2026-10-07T22:22:16.9489779Z   PASS  v3-self-test     v3_verifier: self-test OK
2026-10-07T22:22:16.9490181Z   PASS  v3-corpus        CORPUS  140 vector(s), exact and as expected
2026-10-07T22:22:16.9490596Z   PASS  v3-receipts      RECEIPTS  41 receipt(s), all hold
2026-10-07T22:22:16.9490944Z ====================================================================
2026-10-07T22:22:16.9491442Z release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative mode only)
```
