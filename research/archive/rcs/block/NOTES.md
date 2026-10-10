# RELC-SELECT-1: block module draft (`RelcSelectBlock.lean`)

This is an unbuilt design draft. There is no local Lean toolchain, so nothing here has been compiled.

- Source snapshot: `L = e2426ba4`, worktree `wt-L`, opened read only.
- Target path in the repo: `verification/lean-mathlib/OIBridge/RelcSelectBlock.lean`.
- The module is also not registered anywhere yet. A governed round must add `import OIBridge.RelcSelectBlock` to
  `OIBridge.lean`, and must decide whether the census registry (§A.35) needs updating.

## Files

| file | role |
|---|---|
| `RelcSelectBlock.lean` | the module. It has 765 lines, 30 declarations and **0 `sorry`**. It is generated; do not hand-edit it. |
| `RelcSelectBlock.template.lean` | The hand-written parts: header, `CtrlGate`, the §C lemmas and the docstrings. Each copy appears as a `-- @@COPY <landed name>` marker. |
| `rcs_common.py`, `gen_block.py` | The generator. It extracts the landed bodies, renames them, and applies the two listed line edits. Each edit must match exactly one line, otherwise the generator stops. |
| `verify_block.py` → `verify_output.txt` | An independent verifier that imports nothing from the generator. Its checks and controls are described below. **VERDICT: PASS.** |
| `mathlib_root_clash.py` → `…_output.txt` | Parses Mathlib v4.33.0, a sparse clone at `scratchpad/ml-v433-src` with 25,438 root declarations. None of them has the same name as any of the 92 opened-namespace names the module uses. |
| `attest_names.py` → `attest_output.txt` | Lists which of those 92 names are already used through `open CompositeDimension` in a landed module. 35 are; the other 57 are covered by the clash check above. |
| `finset_open_check.py`, `mathlib_usage_check.py` → outputs | Confirm two things: `open Finset` is not needed, and every Mathlib name in the new lemmas already occurs in landed OIBridge code. |
| `replacement_probe.py` → `replacement_probe_output.txt` | Exact `Fraction` check of every intermediate statement of §C. It runs on `cnot` and `G_R` (positive controls) and on `KG` (countercontrol), reusing `relc/relc_probe.py`. **PASS.** |

### What `verify_block.py` checks

- **V1.** Each copy is line-for-line equal to the landed body after renaming. The only exceptions are the two
  allowed edits, and each of those must be used exactly once.
- **V2.** The module declares exactly the 22 copies and the 8 new declarations, nothing else.
- **V3.** No forbidden reference appears:
  - no `gate_actT`, `Mfwd_homMap`, `Minv_homMap`, `Minv_Mfwd`, `opGate_comp_homMap`, `Lop_*` or `finrank_plus_eq_finrank_minus`;
  - no `.relT`;
  - no `NativeGate` inside a copy.
- **V4.** Two closure checks:
  - no landed lemma that takes `NativeGate` is referenced without being renamed;
  - all 30 declarations are reachable from the exports.
- **V5.** Every new name is fresh across `OIBridge/`.
- **V6.** No identifier is ambiguous between the opened namespaces, and none is shadowed by an `OIBridge` or
  `OIBridge.RelcSelect` declaration.
- **V7.** The module contains no `sorry` or `admit`.
- **Controls C1–C3.** The verifier must reject three mutated versions of the module, and it does:
  - C1: a changed proof token in a copy;
  - C2: an un-renamed reference;
  - C3: the `relT` line restored.

## Exported statements

```lean
structure CtrlGate (Ω) (z) (N) (G : W d ≃ₗ[ℝ] W d) : Prop where
  frame posFwd posInv relC   -- field texts verbatim from NativeGate (CompositeDimension.lean:218), relT dropped
theorem ctrlGate_of_nativeGate : NativeGate Ω z N G → CtrlGate Ω z N G
theorem actT_slice_ctrl (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)
    {c} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) :
    actT N (G (tens (lift c) (Minv z G (hom 0)))) = G (tens (lift c) (Minv z G (hom 0)))
theorem blockData_of_ctrlGate (hd : 2 ≤ d) (hN) (hG : CtrlGate (eball d) z N G) : BlockData (tangentPlus N)
theorem dim_of_ctrlGate (hN) (hG : CtrlGate (eball d) z N G) : d = 1 ∨ d = 3
theorem three_of_ctrlGate (hN) (hG : CtrlGate …) (hE : Entangling (eball d) G) : d = 3
```

`dim_of_ctrlGate` reads parity from `finrank_plus_eq_finrank_minus_relC hN hG.relC`. That theorem belongs to the
separately drafted `OIBridge.RelcSelectParity` and must live in namespace `OIBridge.RelcSelect`.

## Renaming map, and why each lemma is copied

The rule is `X ↦ X_ctrl` with the exceptions shown, plus `NativeGate ↦ CtrlGate`. Every copy takes `hG`, and
`blockData_of_ctrlGate` reaches every copy transitively. Of the extra copies, `not_entangling_one` reaches it
through `three_of_ctrlGate` only, and `dim_of_nativeGate` and `three_of_nativeGate` are the selector itself.

| landed (CompositeDimension.lean) | copy | read by |
|---|---|---|
| gate_corner :1885 | gate_corner_ctrl | Mfwd_Minv, gate_corner_neg, gt_corner |
| gate_corner_symm :1895 | gate_corner_symm_ctrl | Mfwd_Minv |
| Mfwd_Minv :1906 | Mfwd_Minv_ctrl | gt_corner(_neg), blockData_of_orthonormal (hMi0) |
| lor_Minv :1918 | lor_Minv_ctrl | gt_tangent_corners, gt_sphere(_corner), blockData_of_orthonormal, §C |
| gate_actC :1945 | gate_actC_ctrl | gate_corner_neg (the only `relC` use) |
| gate_corner_neg :1965 | gate_corner_neg_ctrl | gt_corner_neg |
| gt_corner :1973, gt_corner_neg :1979 | gt_corner_ctrl, gt_corner_neg_ctrl | gt_center, gt_tangent_corners, gt_sphere(_corner), §C |
| gt_center :1990 | gt_center_ctrl | blockData_of_orthonormal (hsplit) |
| gt_tangent_corners :2070 | gt_tangent_corners_ctrl | Phi_hom_zero_eq_zero, Phi_lift_z_eq_zero, §C |
| gt_sphere :2104, gt_sphere_corner :2134 | `_ctrl` | Phi_sphere, Phi_center |
| Phi_sphere :2224, Phi_center :2239, Phi_center_all :2256 | `_ctrl` | blockData_of_orthonormal, §C |
| Phi_hom_zero_eq_zero :2267, Phi_lift_z_eq_zero :2285 | `_ctrl` | blockData_of_orthonormal, §C |
| blockData_of_orthonormal :2491 | blockData_of_orthonormal_ctrl | blockData_of_ctrlGate |
| blockData_of_nativeGate :2703 | **blockData_of_ctrlGate** | dim_of_ctrlGate |
| not_entangling_one :1436 | not_entangling_one_ctrl | three_of_ctrlGate (it reads `hG.frame` only) |
| dim_of_nativeGate :2723 | **dim_of_ctrlGate** | three_of_ctrlGate |
| three_of_nativeGate :2748 | **three_of_ctrlGate** | export |

**Not copied.**
- `gate_actT`, `Mfwd_homMap` and `Minv_homMap` read `relT`.
- `Minv_Mfwd` is used only by `Minv_homMap`.
- The following take no `hG`, so the landed versions are used directly: `tangent_vanish`, `lor_curve`,
  `exists_orthonormal_basis`, `tperp_*`, `Phi`, `Phi_apply`, `dotB` and others.

**The two non-renaming edits.**
1. `blockData_of_orthonormal` L2668 (module line 679). The landed line
   `rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]` becomes
   `rw [hω]; exact actT_slice_ctrl hN hG hcl hzl`. Its goal is unchanged: `actT N ω = ω`, with
   `ω = G (tens (lift (tperp z l)) (Minv z G (hom 0)))`.
2. `dim_of_nativeGate`. `finrank_plus_eq_finrank_minus hN hG` becomes `finrank_plus_eq_finrank_minus_relC hN hG.relC`.

**Line counts.** The 22 copies total 461 lines. The 8 new declarations total 186 lines: `CtrlGate`,
`ctrlGate_of_nativeGate` and the 6 lemmas of §C.

## The replacement lemma (§C) and its proof route

The route is the LEDGER's Proof B, the tangent curve. I chose it over Proof A because it needs no splitting of `c`
into eigen-components and no norm bounds for those components. It reuses the landed lemmas almost as they stand.

1. **`gt_center_two_ctrl`.**
   - Claim: `2 • G(hom 0 ⊗ Minv t) = hom z ⊗ t + hom(−z) ⊗ H t` for every `t`.
   - Proof: the same `rw` chain as `gt_center`, without `ht`.
2. **`phi_lift_minus_ctrl`.**
   - Setting: a unit `u` with `u 0 = 0` and `H u = −u`. Put `f = hom 0 − u`, which equals `hom(−τ)` and is a
     boundary cone vector. Then `H f = hom 0 + u`, `f·f = 2` and `(Hf)·f = 0`.
   - The functional `F(a) = pairVal a f (G(hom c ⊗ Minv f))` is nonnegative on `Lor`. This uses posFwd,
     `lor_hom` and `lor_Minv`.
   - `F(a) = a·hom z + Φ(a; f, f)`. This follows from step 1 and `hom_eq_add_lift`.
   - `Φ(a; f, f) = −2 Φ(a; u, hom 0)` holds on `Lor`, using `Phi_sphere` (both parts) and `Phi_center`. It then
     holds everywhere by `linearMap_eq_zero_of_lor`.
   - `F(hom(−z)) = 0`. This uses `dot_hom_neg_hom` and `gt_tangent_corners.1`.
   - `tangent_vanish` at `w = −z` gives `F(lift c') = 0`. Since `lift c'·hom z = 0`, this yields
     `Φ(lift c'; u, hom 0) = 0`.
3. **`phi_bvec_minus_unit_ctrl`.** `Φ(bvec μ; u, hom 0) = 0` for every `μ`. The argument is a `Fin.cases`:
   - `μ = 0` uses `Phi_hom_zero_eq_zero`;
   - `μ = k+1` uses `lift_tperp`, `Phi_lift_z_eq_zero` and step 2 with `c' = tperp z k`.
   This is the same pattern as the landed `hb`.
4. **`phi_minusSpace_ctrl`.** Extends step 3 to every `w ∈ minusSpace N` by rescaling to a unit vector. This is the
   `Real.sqrt` pattern of `sumsq_apply_le_of_preserves`; the case `w = 0` is separate.
5. **`homMap_eq_self_of_orth_minusSpace`.**
   - Claim: a vector `v` with `v ⊥ E₋` satisfies `H v = v`. It reads `IsNot` only.
   - Proof: `w = v − Hv` lies in `E₋`. Then `v·w = 0`, and `Hv·w = v·Hw = −v·w = 0` by `homMap_dot`. So `w·w = 0`.
6. **`actT_slice_ctrl`.** Every row of `ω` is orthogonal to `E₋` by step 4, using `Phi_apply` and `pairVal_bvec`.
   By step 5, every row is therefore fixed.

**Landed lemmas used by §C, with lines in CompositeDimension.lean.**
- Copied over `CtrlGate`: gt_corner 1973, gt_corner_neg 1979, lor_Minv 1918, gt_tangent_corners 2070,
  Phi_sphere 2224, Phi_center 2239, Phi_hom_zero_eq_zero 2267, Phi_lift_z_eq_zero 2285.
- Used directly:
  - cone and tangent argument: tangent_vanish 2051, linearMap_eq_zero_of_lor 1722, gate_pairVal_nonneg 1621,
    lor_hom 1679, lor_hom_of_unit 1685;
  - homogenized vectors: hom_add_hom_neg 1735, dot_hom_neg_hom 1743, dot_hom_hom_zero 2450, hom_eq_add_lift 1646,
    hom_zero 102, hom_succ 104;
  - lifts: lift_neg 1664, lift_vecTail 1670, lift_zero 1641, lift_succ 1643, lift_tperp 2424;
  - tensors: tens_smul_left 1462, tens_add_left 1456;
  - the homogenized NOT: homMap_hom 144, homMap_homMap 152, homMap_zero 129, homMap_dot 395, mem_minusSpace 268;
  - pairings: pairVal_smul_omega 1499, pairVal_add_omega 1490, pairVal_tens 1530, pairVal_sub_left 2477,
    pairVal_smul_left 976, pairVal_bvec 2460, pvLeft 1545, pvLeft_apply 1550;
  - the block form: Phi 2202, Phi_apply 2219;
  - control tangent directions: tperp_le_one 2408, tperp_dot_z 2412, bvec_zero_eq 1632;
  - other: sumsq_smul 336.
- From `TransitiveBody.lean`: mem_eball 520.

**Hypotheses read.** The route reads frame, posFwd and posInv, through `gate_corner`, `lor_Minv` and `Mfwd_Minv`.
It reads `relC` only through `gate_corner_neg`. It does not read `relT`.

**Exact probe.** `replacement_probe_output.txt` checks the intermediate statements on two positive controls and
one countercontrol:
- `cnot` and `G_R` satisfy every step.
- On `KG` (frame and `relC`, not positive), the centre steps hold, the positivity-derived identity `hext` fails, and
  the conclusion fails. So the chain is not vacuous.

## Mathlib names

There are no `-- MATHLIB-NAME-UNVERIFIED` markers. Every Mathlib name in the new lemmas already appears in landed
OIBridge code (`mathlib_usage_check.py`). This includes `mul_self_nonneg`, `mul_self_eq_zero`, `one_div_mul_cancel`,
`neg_sub`, `smul_neg` and `sub_neg_eq_add`. The declarations of the less common names were also checked in the
v4.33.0 clone.

## Header deviations

- **Extra import.** I added `import OIBridge.ParityNot` after `import OIBridge.RelcSelectParity`. It is redundant if
  the parity module already imports it. It guarantees that `open EffectSpace ParityNot` resolves.
- **The `open` line.** It is the same as in `OddChar.lean`. CompositeDimension's extra `open Finset` is not needed:
  the copied proofs qualify every `Finset.` name, and `map_sum` is a root name.

## Top compile risks

1. **The six new lemmas of §C have never been elaborated.** The likeliest failure points are these, all in
   `phi_lift_minus_ctrl`:
   - the `rw … at h2` chain in `hcen`, which needs `hS1` and `hS2` to match the output of `pairVal_tens`
     syntactically;
   - the `change` steps that fold `pairVal` into `Phi` in `hext`;
   - `rw [hsplit, hext] at hT` over the `let F`.

   The copies carry little risk: they are verbatim bodies of compiled proofs. Their only change is
   `NativeGate`→`CtrlGate`, and the field names are identical.
2. **Interface to `RelcSelectParity`.**
   - The name and argument order of `finrank_plus_eq_finrank_minus_relC` must match.
   - Both modules share the namespace `OIBridge.RelcSelect`. If the parity module also declares `CtrlGate`, or any
     name listed above, the build fails with a duplicate declaration.
3. **Name resolution after `open`.** 57 of the 92 opened names are used through `open` for the first time. Two
   checks found no clash:
   - against the root declarations of Mathlib v4.33.0, using a parser-based list that excludes names generated by
     `to_additive`;
   - against OIBridge namespaces.

   Lean core root names were not scanned. A clash there would show up as an "ambiguous, possible interpretations"
   error.
