#!/usr/bin/env python3
"""controls.py -- round DIM-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference module; mutation controls that
                                            must fail with their named codes

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  N1  decls       the module declares exactly the frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=` or `where`) is the frozen text; every definition and
                  structure is the frozen text whole; the preamble and every context block is the frozen text, in
                  order -- a proof may change, a statement, definition, structure or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  selectors   the public selectors carry exactly the frozen binders and conclusions; none of them, nor the verdict,
                  contains `BlockData` or `2 ≤ d`; `Entangling` is a hypothesis of `three_of_nativeGate` and not of
                  `dim_of_nativeGate`
  S2  internal    `2 ≤ d` occurs only in the statements of the three block-reduction theorems; `BlockData` occurs only
                  in its structure and the three theorems that build or consume it; `BlockData` is the frozen text
  S3  hypotheses  `IsNot` and `NativeGate` carry exactly their frozen binders and fields, both relations with the one
                  bound `N`; `Entangling`, `maxCone`, `jointStates`, `W`, `prodState`, `actT`, `actC` are the frozen
                  texts whole, and `maxCone` quantifies over every `IsEffectOn` effect of the body
  S4  premises    no theorem or definition concludes `IsNot`, `NativeGate` or `Entangling`, other than the five named
                  witness and control theorems and the verdict's two instance clauses
  S5  reuse       no declaration shares a name with `NativeGateBall`, `eball`, `mem_eball` or `IsEffectOn`; the proofs
                  cite `NativeGateBall.parity`, `NativeGateBall.p_le_one` and `NativeGateBall.dim_of_bounds`
  S6  neutral     no complex, tensor-product, Kronecker, unitary-group, Hilbert or Bell token in the module; every
                  import is `OIBridge.TransitiveBody`, `OIBridge.NativeGateBall` or a Mathlib module; no statement
                  with `↔` carries an equation in `d`
  S7  phrases     the module header (and, at a commit carrying it, the result note) contains none of the frozen phrases
  S8  dimension   outside the witness and control sections and the verdict, a numeral 3, 4, 5 or 7 occurs only as the
                  conclusion `d = 1 ∨ d = 3`, `d = 3`, `d ≠ 4`, `d ≠ 5` or `d ≠ 7`, or in one of the three named
                  coordinate helpers; no `ball3` or `eball_three` token
  S9  count       exactly the 87 frozen `#print axioms` lines, in order, distinct, each naming a declaration of the
                  module
  S10 premise map the carrier `W` carries its local-tomography sentence; no hypothesis or cone definition mentions
                  `Lor`; the three cone theorems are theorems with their frozen conclusions and prints
  I   imports     OIBridge.lean is D's with exactly the frozen import line after `import OIBridge.CompositeInterface`
  C   census      the census is D's with exactly the frozen family inserted after the COMP-1 family and exactly the
                  frozen sentence of the NB-1 family note replaced, byte for byte
  R   roadmap     verification/ROADMAP.md is D's with exactly the two frozen replacements: the K1 parenthetical of the
                  P1 "K" row and the K1 bullet
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import io, json, re, subprocess, sys

D = '8f3299c1e191ae575bb6ee56fc4b63fbe0773623'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-dim-1-dimension-selector/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
MOD = 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
GOVERNED = {MOD: 'A', IMPORTS: 'M', CENSUS: 'M', ROADMAP: 'M'}
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOB = '377f0b25ed0ef58cf6269f71b816e477450131bc'
ANCHOR_IMPORT = 'import OIBridge.CompositeInterface\n'
NEW_IMPORT = 'import OIBridge.CompositeDimension\n'
PREV_FAMILY_MODULES = ['CompositeInterface']
NB1_FAMILY_MODULES = ['NativeGateBall']
CENSUS_FAMILY = json.loads(r'''{
 "name": "the composite dimension selector in the coordinate realization: two identical balls on the locally tomographic bilinear carrier W d with the full affine effect set, one common NOT and the native-gate hypotheses force d into {1, 3}, and 3 under the entangling clause (round DIM-1, reconstruction)",
 "modules": [
  "CompositeDimension"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round DIM-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-dim-1-dimension-selector/preregistration.md. The kernel layer states the composite hypotheses on the bilinear carrier of two homogenized copies of the coordinate Euclidean ball eball d of TransitiveBody, with local tomography as the premise the carrier encodes: one common NOT (IsNot), the CNOT frame, the target and control relations and two-sided positivity on the maximal cone (NativeGate), and the entangling clause (Entangling). It proves the eigenspace adapter for a linear involution (finrank_ker_sub_add_finrank_ker_add), parity of the two eigenspaces of the homogenized NOT from the frozen hypotheses (finrank_plus_eq_finrank_minus), the exclusion of every even d (not_even_of_nativeGate), the block reduction of NB-1's S1, S2 and S4 in the kernel for d at least two (corner_form, the sphere identities gt_sphere and gt_sphere_corner, the block form Phi, blockData_of_nativeGate), so that the block data of NativeGateBall.p_le_one is derived from the frozen hypotheses, the selector d = 1 or d = 3 from the frozen hypotheses alone (dim_of_nativeGate, with d = 5 and d = 7 as instances ne_five_of_nativeGate and ne_seven_of_nativeGate), and d = 3 under the entangling clause (three_of_nativeGate), since no gate of two intervals is entangling (not_entangling_one). The d = 3 witness is a kernel theorem by exact algebra: the signed permutation cnot with the reflection nflip satisfies every hypothesis including two-sided positivity (nativeGate_cnot) and the entangling clause (entangling_cnot). Controls: the classical gate of two intervals satisfies every hypothesis except the entangling clause and creates correlations from a mixed product input (nativeGate_cnot1, not_entangling_cnot1, not_product_cnot1_mixed); eball 4 carries no gate (no_gate_four); the verdict is dim1_core. Carried by no manuscript. Nothing here claims that OI supplies local tomography, the common NOT, the gate or the full effects; the ball is TransitiveBody's."
}''')
NB1_OLD = json.loads(r'''"they are not kernel statements, and the theorem for general d is not a kernel theorem."''')
NB1_NEW = json.loads(r'''"they are not kernel statements of this module, and the theorem for general d is a kernel theorem of round DIM-1 (dim_of_nativeGate and three_of_nativeGate in CompositeDimension)."''')
ROADMAP_EDITS = json.loads(r'''[
 [
  "K1 **CONDITIONAL** (round NB-1: ball, full self-dual effects, the native-gate hypotheses and one common NOT give `d ∈ {1, 3}`)",
  "K1 **CONDITIONAL** (rounds NB-1 and DIM-1: two identical balls on the coordinate carrier `W d` with full affine effects, one common NOT and the native-gate hypotheses give `d ∈ {1, 3}`, and `d = 3` with an entangling gate)"
 ],
 [
  "- **K1 — the dimension. CONDITIONAL.** For two locally tomographic `d`-balls with full self-dual\n  effect cones, one common NOT involution on both copies and a native CNOT satisfying the two NOT\n  relations with two-sided product positivity, `d ∈ {1, 3}`. The dimension-free steps are\n  kernel-proved, the dimension-dependent steps are exact for `d ≤ 7`, and the theorem for general\n  `d` rests on the round's written proof. It does not say that bare OI selects `d = 3`: its OI\n",
  "- **K1 — the dimension. CONDITIONAL.** In the DIM-1 coordinate realization of two identical\n  `d`-balls on the locally tomographic bilinear carrier `W d`, using the full affine effect set in\n  `maxCone`, one common `IsNot` involution and a `NativeGate` satisfying its frame, two-sided\n  positivity and two NOT relations imply `d ∈ {1, 3}` (`dim_of_nativeGate`); adding `Entangling`\n  implies `d = 3` (`three_of_nativeGate`). The Lorentz geometry of the effect cone is proved inside\n  the round, not assumed. Round NB-1 proved the dimension-free steps in the kernel and the\n  dimension-dependent steps exactly for `d ≤ 7`. It does not say that bare OI selects `d = 3`: its OI\n"
 ]
]''')
NGB_NAMES = json.loads(r'''["averaging_bound", "blocks_vanish", "col_sq", "dim_of_bounds", "isometry_of_contractions", "lorentz_of_effects", "nb1_kernel_core", "p_le_one", "parity", "vanish_of_bound"]''')
DECLS = json.loads(r'''[
 [
  "abbrev",
  "HVec"
 ],
 [
  "abbrev",
  "W"
 ],
 [
  "def",
  "hom"
 ],
 [
  "theorem",
  "hom_zero"
 ],
 [
  "theorem",
  "hom_succ"
 ],
 [
  "theorem",
  "vecTail_add"
 ],
 [
  "theorem",
  "vecTail_smul"
 ],
 [
  "def",
  "homMap"
 ],
 [
  "theorem",
  "homMap_zero"
 ],
 [
  "theorem",
  "homMap_succ"
 ],
 [
  "theorem",
  "vecTail_homMap"
 ],
 [
  "theorem",
  "vecTail_hom"
 ],
 [
  "theorem",
  "homMap_hom"
 ],
 [
  "theorem",
  "homMap_homMap"
 ],
 [
  "def",
  "prodState"
 ],
 [
  "def",
  "pairVal"
 ],
 [
  "noncomputable def",
  "ehom"
 ],
 [
  "theorem",
  "ehom_dot"
 ],
 [
  "noncomputable def",
  "prodEffVal"
 ],
 [
  "def",
  "maxCone"
 ],
 [
  "def",
  "jointStates"
 ],
 [
  "def",
  "IsProduct"
 ],
 [
  "def",
  "actT"
 ],
 [
  "def",
  "actC"
 ],
 [
  "def",
  "corner"
 ],
 [
  "structure",
  "IsNot"
 ],
 [
  "structure",
  "NativeGate"
 ],
 [
  "def",
  "Entangling"
 ],
 [
  "theorem",
  "finrank_ker_sub_add_finrank_ker_add"
 ],
 [
  "def",
  "plusSpace"
 ],
 [
  "def",
  "minusSpace"
 ],
 [
  "theorem",
  "mem_plusSpace"
 ],
 [
  "theorem",
  "mem_minusSpace"
 ],
 [
  "theorem",
  "finrank_plus_add_finrank_minus"
 ],
 [
  "theorem",
  "hom_zero_mem_plusSpace"
 ],
 [
  "theorem",
  "lift_corner_mem_minusSpace"
 ],
 [
  "theorem",
  "one_le_finrank_plusSpace"
 ],
 [
  "theorem",
  "one_le_finrank_minusSpace"
 ],
 [
  "theorem",
  "not_even_of_balanced"
 ],
 [
  "theorem",
  "split_of_balanced"
 ],
 [
  "theorem",
  "sumsq_smul"
 ],
 [
  "theorem",
  "sumsq_apply_le_of_preserves"
 ],
 [
  "theorem",
  "sumsq_apply_eq"
 ],
 [
  "theorem",
  "sumsq_add"
 ],
 [
  "theorem",
  "dot_apply_apply"
 ],
 [
  "theorem",
  "dot_apply"
 ],
 [
  "theorem",
  "homMap_dot"
 ],
 [
  "def",
  "toOp"
 ],
 [
  "def",
  "fromOp"
 ],
 [
  "theorem",
  "toOp_fromOp"
 ],
 [
  "theorem",
  "fromOp_toOp"
 ],
 [
  "theorem",
  "toOp_injective"
 ],
 [
  "theorem",
  "toOp_apply"
 ],
 [
  "def",
  "toOpLin"
 ],
 [
  "theorem",
  "toOpLin_apply"
 ],
 [
  "def",
  "fromOpLin"
 ],
 [
  "theorem",
  "fromOpLin_apply"
 ],
 [
  "theorem",
  "toOp_actC"
 ],
 [
  "theorem",
  "toOp_actT"
 ],
 [
  "theorem",
  "actT_actT"
 ],
 [
  "theorem",
  "actC_actC"
 ],
 [
  "def",
  "opGate"
 ],
 [
  "theorem",
  "opGate_toOp"
 ],
 [
  "theorem",
  "opGate_comp_homMap"
 ],
 [
  "theorem",
  "opGate_homMap_comp"
 ],
 [
  "noncomputable def",
  "projMinus"
 ],
 [
  "theorem",
  "projMinus_apply"
 ],
 [
  "theorem",
  "projMinus_of_mem"
 ],
 [
  "theorem",
  "projMinus_homMap"
 ],
 [
  "abbrev",
  "OpSpace"
 ],
 [
  "def",
  "Pop"
 ],
 [
  "theorem",
  "Pop_apply"
 ],
 [
  "noncomputable def",
  "Lop"
 ],
 [
  "theorem",
  "Lop_apply"
 ],
 [
  "theorem",
  "Lop_anti"
 ],
 [
  "theorem",
  "Lop_eq_zero"
 ],
 [
  "theorem",
  "Lop_injective"
 ],
 [
  "theorem",
  "finrank_ker_eq_of_pointwise"
 ],
 [
  "theorem",
  "finrank_ker_Pop_sub"
 ],
 [
  "theorem",
  "finrank_ker_Pop_add"
 ],
 [
  "theorem",
  "finrank_plus_eq_finrank_minus"
 ],
 [
  "theorem",
  "not_even_of_nativeGate"
 ],
 [
  "theorem",
  "ne_two_of_nativeGate"
 ],
 [
  "theorem",
  "ne_four_of_nativeGate"
 ],
 [
  "structure",
  "BlockData"
 ],
 [
  "theorem",
  "p_le_one_of_blockData"
 ],
 [
  "noncomputable def",
  "tangentPlus"
 ],
 [
  "theorem",
  "sum_univ_four'"
 ],
 [
  "theorem",
  "sum_univ_two'"
 ],
 [
  "def",
  "sgn"
 ],
 [
  "def",
  "pc"
 ],
 [
  "def",
  "pt"
 ],
 [
  "def",
  "cnotFun"
 ],
 [
  "theorem",
  "cnotFun_apply"
 ],
 [
  "theorem",
  "pc_pc"
 ],
 [
  "theorem",
  "pt_pt"
 ],
 [
  "theorem",
  "sgn_mul_sgn"
 ],
 [
  "theorem",
  "cnotFun_cnotFun"
 ],
 [
  "def",
  "cnot"
 ],
 [
  "theorem",
  "cnot_apply"
 ],
 [
  "theorem",
  "cnot_symm_apply"
 ],
 [
  "def",
  "z3"
 ],
 [
  "def",
  "nflip"
 ],
 [
  "theorem",
  "nflip_apply"
 ],
 [
  "theorem",
  "nflip_zero'"
 ],
 [
  "theorem",
  "nflip_one"
 ],
 [
  "theorem",
  "nflip_two"
 ],
 [
  "theorem",
  "homMap_nflip_zero"
 ],
 [
  "theorem",
  "homMap_nflip_one"
 ],
 [
  "theorem",
  "homMap_nflip_two"
 ],
 [
  "theorem",
  "homMap_nflip_three"
 ],
 [
  "theorem",
  "hom_one'"
 ],
 [
  "theorem",
  "hom_two'"
 ],
 [
  "theorem",
  "hom_three'"
 ],
 [
  "theorem",
  "z3_zero"
 ],
 [
  "theorem",
  "z3_one"
 ],
 [
  "theorem",
  "z3_two"
 ],
 [
  "theorem",
  "corner_zero"
 ],
 [
  "theorem",
  "corner_one"
 ],
 [
  "theorem",
  "actT_apply"
 ],
 [
  "theorem",
  "actC_apply"
 ],
 [
  "theorem",
  "prodState_apply"
 ],
 [
  "theorem",
  "isNot_nflip"
 ],
 [
  "theorem",
  "cnot_frame"
 ],
 [
  "theorem",
  "cnot_relT"
 ],
 [
  "theorem",
  "cnot_relC"
 ],
 [
  "def",
  "Lor"
 ],
 [
  "theorem",
  "lor_smul"
 ],
 [
  "theorem",
  "lor_pair_bound"
 ],
 [
  "noncomputable def",
  "affOf"
 ],
 [
  "theorem",
  "affOf_apply"
 ],
 [
  "theorem",
  "affOf_linear"
 ],
 [
  "theorem",
  "ehom_affOf"
 ],
 [
  "theorem",
  "isEffectOn_affOf"
 ],
 [
  "theorem",
  "ehom_zero_eq"
 ],
 [
  "theorem",
  "lor_ehom"
 ],
 [
  "theorem",
  "pairVal_eq_sum_toOp"
 ],
 [
  "theorem",
  "pairVal_smul_left"
 ],
 [
  "theorem",
  "pairVal_smul_right"
 ],
 [
  "theorem",
  "pairVal_nonneg_of_maxCone"
 ],
 [
  "theorem",
  "lor_of_forall_pair"
 ],
 [
  "theorem",
  "lor_toOp_of_maxCone"
 ],
 [
  "theorem",
  "lor_three"
 ],
 [
  "theorem",
  "lor_of_three"
 ],
 [
  "theorem",
  "cnot_core"
 ],
 [
  "theorem",
  "cnot_target"
 ],
 [
  "theorem",
  "prodEffVal_cnot_prodState"
 ],
 [
  "theorem",
  "cnot_prodEffVal_nonneg"
 ],
 [
  "theorem",
  "cnot_prodState_mem_maxCone"
 ],
 [
  "theorem",
  "nativeGate_cnot"
 ],
 [
  "theorem",
  "extreme_of_unit"
 ],
 [
  "def",
  "xplus"
 ],
 [
  "theorem",
  "xplus_zero"
 ],
 [
  "theorem",
  "xplus_one"
 ],
 [
  "theorem",
  "xplus_two"
 ],
 [
  "def",
  "phiW"
 ],
 [
  "theorem",
  "cnot_prodState_xplus_z3"
 ],
 [
  "theorem",
  "xplus_mem"
 ],
 [
  "theorem",
  "z3_mem"
 ],
 [
  "theorem",
  "phiW_not_product"
 ],
 [
  "theorem",
  "phiW_mem_jointStates"
 ],
 [
  "theorem",
  "toOp_phiW_zero"
 ],
 [
  "theorem",
  "toOp_phiW_one"
 ],
 [
  "theorem",
  "toOp_phiW_two"
 ],
 [
  "theorem",
  "toOp_phiW_three"
 ],
 [
  "theorem",
  "lor_ray"
 ],
 [
  "def",
  "tv"
 ],
 [
  "theorem",
  "toOp_tv1"
 ],
 [
  "theorem",
  "toOp_tv2"
 ],
 [
  "theorem",
  "toOp_tv3"
 ],
 [
  "theorem",
  "ray_eqs"
 ],
 [
  "theorem",
  "phiW_eq_of_segment"
 ],
 [
  "theorem",
  "entangling_cnot"
 ],
 [
  "theorem",
  "fin1_ext"
 ],
 [
  "theorem",
  "corner_mem_one"
 ],
 [
  "theorem",
  "eq_corner_of_extreme"
 ],
 [
  "theorem",
  "not_entangling_one"
 ],
 [
  "def",
  "tens"
 ],
 [
  "theorem",
  "tens_apply"
 ],
 [
  "theorem",
  "prodState_eq_tens"
 ],
 [
  "theorem",
  "tens_add_left"
 ],
 [
  "theorem",
  "tens_add_right"
 ],
 [
  "theorem",
  "tens_smul_left"
 ],
 [
  "theorem",
  "tens_smul_right"
 ],
 [
  "theorem",
  "tens_zero_left"
 ],
 [
  "theorem",
  "tens_zero_right"
 ],
 [
  "def",
  "tensL"
 ],
 [
  "theorem",
  "tensL_apply"
 ],
 [
  "def",
  "tensR"
 ],
 [
  "theorem",
  "tensR_apply"
 ],
 [
  "theorem",
  "pairVal_add_omega"
 ],
 [
  "theorem",
  "pairVal_smul_omega"
 ],
 [
  "theorem",
  "pairVal_zero_omega"
 ],
 [
  "theorem",
  "pairVal_add_left"
 ],
 [
  "theorem",
  "pairVal_add_right"
 ],
 [
  "theorem",
  "pairVal_tens"
 ],
 [
  "def",
  "pvOmega"
 ],
 [
  "theorem",
  "pvOmega_apply"
 ],
 [
  "def",
  "pvLeft"
 ],
 [
  "theorem",
  "pvLeft_apply"
 ],
 [
  "theorem",
  "pairVal_hom_zero_left"
 ],
 [
  "theorem",
  "smul_mem_maxCone"
 ],
 [
  "theorem",
  "zero_mem_maxCone"
 ],
 [
  "theorem",
  "lor_eq_zero_of_head"
 ],
 [
  "theorem",
  "lor_eq_smul_hom"
 ],
 [
  "theorem",
  "tens_mem_maxCone"
 ],
 [
  "theorem",
  "gate_pairVal_nonneg"
 ],
 [
  "def",
  "bvec"
 ],
 [
  "theorem",
  "bvec_apply"
 ],
 [
  "theorem",
  "bvec_zero_eq"
 ],
 [
  "def",
  "lift"
 ],
 [
  "theorem",
  "lift_zero"
 ],
 [
  "theorem",
  "lift_succ"
 ],
 [
  "theorem",
  "hom_eq_add_lift"
 ],
 [
  "theorem",
  "lift_add"
 ],
 [
  "theorem",
  "lift_smul"
 ],
 [
  "theorem",
  "lift_neg"
 ],
 [
  "theorem",
  "lift_vecTail"
 ],
 [
  "theorem",
  "lor_hom_zero"
 ],
 [
  "theorem",
  "lor_hom"
 ],
 [
  "theorem",
  "lor_hom_of_unit"
 ],
 [
  "theorem",
  "lor_hom_zero_add_smul_bvec"
 ],
 [
  "theorem",
  "linearMap_eq_zero_of_nonneg_lor"
 ],
 [
  "theorem",
  "linearMap_eq_zero_of_lor"
 ],
 [
  "theorem",
  "hom_add_hom_neg"
 ],
 [
  "theorem",
  "dot_hom_neg_hom"
 ],
 [
  "theorem",
  "dot_hom_hom_neg"
 ],
 [
  "theorem",
  "lor_face"
 ],
 [
  "theorem",
  "tens_hom_inj"
 ],
 [
  "theorem",
  "toOp_bvec"
 ],
 [
  "def",
  "cornerMap"
 ],
 [
  "theorem",
  "cornerMap_apply"
 ],
 [
  "theorem",
  "corner_form"
 ],
 [
  "theorem",
  "lor_cornerMap"
 ],
 [
  "def",
  "Mfwd"
 ],
 [
  "def",
  "Minv"
 ],
 [
  "theorem",
  "gate_corner"
 ],
 [
  "theorem",
  "gate_corner_symm"
 ],
 [
  "theorem",
  "Mfwd_Minv"
 ],
 [
  "theorem",
  "Minv_Mfwd"
 ],
 [
  "theorem",
  "lor_Minv"
 ],
 [
  "theorem",
  "actT_tens"
 ],
 [
  "theorem",
  "actC_tens"
 ],
 [
  "theorem",
  "gate_actT"
 ],
 [
  "theorem",
  "gate_actC"
 ],
 [
  "theorem",
  "Mfwd_homMap"
 ],
 [
  "theorem",
  "Minv_homMap"
 ],
 [
  "theorem",
  "gate_corner_neg"
 ],
 [
  "theorem",
  "gt_corner"
 ],
 [
  "theorem",
  "gt_corner_neg"
 ],
 [
  "theorem",
  "eq_of_two_smul_eq"
 ],
 [
  "theorem",
  "gt_center"
 ],
 [
  "theorem",
  "eq_zero_of_quadratic_nonneg"
 ],
 [
  "theorem",
  "lor_curve"
 ],
 [
  "theorem",
  "tangent_vanish"
 ],
 [
  "theorem",
  "gt_tangent_corners"
 ],
 [
  "theorem",
  "gt_sphere"
 ],
 [
  "theorem",
  "gt_sphere_corner"
 ],
 [
  "def",
  "dotB"
 ],
 [
  "theorem",
  "dotB_apply"
 ],
 [
  "theorem",
  "lor_of_dotB"
 ],
 [
  "noncomputable def",
  "Phi"
 ],
 [
  "theorem",
  "Phi_apply"
 ],
 [
  "theorem",
  "Phi_sphere"
 ],
 [
  "theorem",
  "Phi_center"
 ],
 [
  "theorem",
  "Phi_center_all"
 ],
 [
  "theorem",
  "Phi_hom_zero_eq_zero"
 ],
 [
  "theorem",
  "Phi_lift_z_eq_zero"
 ],
 [
  "def",
  "tangentSpace"
 ],
 [
  "theorem",
  "mem_tangentSpace"
 ],
 [
  "theorem",
  "hom_zero_ne_zero"
 ],
 [
  "theorem",
  "finrank_tangentSpace"
 ],
 [
  "theorem",
  "exists_orthonormal_basis"
 ],
 [
  "def",
  "tperp"
 ],
 [
  "theorem",
  "tperp_apply"
 ],
 [
  "theorem",
  "sum_ite_mul"
 ],
 [
  "theorem",
  "tperp_sq"
 ],
 [
  "theorem",
  "tperp_le_one"
 ],
 [
  "theorem",
  "tperp_dot_z"
 ],
 [
  "theorem",
  "tperp_mem"
 ],
 [
  "theorem",
  "lift_tperp"
 ],
 [
  "theorem",
  "exists_tperp_ne_zero"
 ],
 [
  "theorem",
  "dot_hom_hom_zero"
 ],
 [
  "theorem",
  "sum_bvec_mul"
 ],
 [
  "theorem",
  "pairVal_bvec"
 ],
 [
  "theorem",
  "sum_row_hom_zero"
 ],
 [
  "theorem",
  "tens_ne_zero"
 ],
 [
  "theorem",
  "pairVal_sub_left"
 ],
 [
  "theorem",
  "blockData_of_orthonormal"
 ],
 [
  "theorem",
  "blockData_of_nativeGate"
 ],
 [
  "theorem",
  "pos_of_isNot"
 ],
 [
  "theorem",
  "dim_of_nativeGate"
 ],
 [
  "theorem",
  "ne_five_of_nativeGate"
 ],
 [
  "theorem",
  "ne_seven_of_nativeGate"
 ],
 [
  "theorem",
  "three_of_nativeGate"
 ],
 [
  "def",
  "cnot1Fun"
 ],
 [
  "theorem",
  "add_add_self_fin2"
 ],
 [
  "def",
  "cnot1"
 ],
 [
  "theorem",
  "cnot1_apply"
 ],
 [
  "def",
  "z1"
 ],
 [
  "def",
  "neg1"
 ],
 [
  "theorem",
  "neg1_apply"
 ],
 [
  "theorem",
  "z1_zero"
 ],
 [
  "theorem",
  "hom_one1"
 ],
 [
  "theorem",
  "homMap_neg1_zero"
 ],
 [
  "theorem",
  "homMap_neg1_one"
 ],
 [
  "theorem",
  "isNot_neg1"
 ],
 [
  "theorem",
  "cnot1_frame"
 ],
 [
  "theorem",
  "cnot1_relT"
 ],
 [
  "theorem",
  "cnot1_relC"
 ],
 [
  "theorem",
  "lor_one"
 ],
 [
  "theorem",
  "cnot1_core"
 ],
 [
  "theorem",
  "prodEffVal_cnot1_prodState"
 ],
 [
  "theorem",
  "cnot1_prodState_mem_maxCone"
 ],
 [
  "theorem",
  "nativeGate_cnot1"
 ],
 [
  "theorem",
  "not_entangling_cnot1"
 ],
 [
  "theorem",
  "not_product_cnot1_mixed"
 ],
 [
  "theorem",
  "no_gate_four"
 ],
 [
  "theorem",
  "dim1_core"
 ]
]''')
TEXTS = json.loads(r'''{
 "HVec": "abbrev HVec (d : ℕ) := Fin (d + 1) → ℝ",
 "W": "abbrev W (d : ℕ) := Fin (d + 1) → Fin (d + 1) → ℝ",
 "hom": "def hom (x : Fin d → ℝ) : HVec d := Matrix.vecCons 1 x",
 "hom_zero": "@[simp] theorem hom_zero (x : Fin d → ℝ) : hom x 0 = 1",
 "hom_succ": "@[simp] theorem hom_succ (x : Fin d → ℝ) (j : Fin d) : hom x j.succ = x j",
 "vecTail_add": "theorem vecTail_add (u v : HVec d) : Matrix.vecTail (u + v) = Matrix.vecTail u + Matrix.vecTail v",
 "vecTail_smul": "theorem vecTail_smul (c : ℝ) (v : HVec d) : Matrix.vecTail (c • v) = c • Matrix.vecTail v",
 "homMap": "def homMap (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : HVec d →ₗ[ℝ] HVec d where\n  toFun v := Matrix.vecCons (v 0) (N (Matrix.vecTail v))\n  map_add' u v := by\n    funext i\n    refine Fin.cases ?_ (fun j => ?_) i\n    · simp\n    · simp only [Matrix.cons_val_succ, Pi.add_apply]\n      rw [vecTail_add, map_add]\n      rfl\n  map_smul' c v := by\n    funext i\n    refine Fin.cases ?_ (fun j => ?_) i\n    · simp\n    · simp only [Matrix.cons_val_succ, Pi.smul_apply, RingHom.id_apply]\n      rw [vecTail_smul, map_smul]\n      rfl",
 "homMap_zero": "@[simp] theorem homMap_zero (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :\n    homMap N v 0 = v 0",
 "homMap_succ": "@[simp] theorem homMap_succ (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) (j : Fin d) :\n    homMap N v j.succ = N (Matrix.vecTail v) j",
 "vecTail_homMap": "theorem vecTail_homMap (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :\n    Matrix.vecTail (homMap N v) = N (Matrix.vecTail v)",
 "vecTail_hom": "theorem vecTail_hom (x : Fin d → ℝ) : Matrix.vecTail (hom x) = x",
 "homMap_hom": "theorem homMap_hom (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) :\n    homMap N (hom x) = hom (N x)",
 "homMap_homMap": "theorem homMap_homMap {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (v : HVec d) :\n    homMap N (homMap N v) = v",
 "prodState": "def prodState (x y : Fin d → ℝ) : W d := fun μ ν => hom x μ * hom y ν",
 "pairVal": "def pairVal (a b : HVec d) (ω : W d) : ℝ := ∑ μ, ∑ ν, a μ * ω μ ν * b ν",
 "ehom": "noncomputable def ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : HVec d :=\n  Matrix.vecCons (e 0) fun j => e.linear fun i => if j = i then (1 : ℝ) else 0",
 "ehom_dot": "theorem ehom_dot (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    e x = ∑ μ, ehom e μ * hom x μ",
 "prodEffVal": "noncomputable def prodEffVal (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (ω : W d) : ℝ :=\n  pairVal (ehom e) (ehom f) ω",
 "maxCone": "def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) :=\n  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}",
 "jointStates": "def jointStates (Ω : Set (Fin d → ℝ)) : Set (W d) :=\n  {ω | ω ∈ maxCone Ω ∧ ω 0 0 = 1}",
 "IsProduct": "def IsProduct (Ω : Set (Fin d → ℝ)) (ω : W d) : Prop :=\n  ∃ x ∈ Ω, ∃ y ∈ Ω, ω = prodState x y",
 "actT": "def actT (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)",
 "actC": "def actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : W d :=\n  fun μ ν => homMap N (fun κ => ω κ ν) μ",
 "corner": "def corner (z : Fin d → ℝ) : Fin 2 → (Fin d → ℝ) := ![z, -z]",
 "IsNot": "structure IsNot (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Prop where\n  unit : ∑ j, z j ^ 2 = 1\n  invol : ∀ x, N (N x) = x\n  preserves : ∀ x ∈ Ω, N x ∈ Ω\n  flips : N z = -z",
 "NativeGate": "structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n    (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n  relT : ∀ ω, actT N (G (actT N ω)) = G ω\n  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "Entangling": "def Entangling (Ω : Set (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop :=\n  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ,\n    G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬ IsProduct Ω (G (prodState x y))",
 "finrank_ker_sub_add_finrank_ker_add": "theorem finrank_ker_sub_add_finrank_ker_add {V : Type*} [AddCommGroup V] [Module ℝ V]\n    [FiniteDimensional ℝ V] (P : V →ₗ[ℝ] V) (hP : ∀ v, P (P v) = v) :\n    Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))\n      + Module.finrank ℝ (LinearMap.ker (P + LinearMap.id)) = Module.finrank ℝ V",
 "plusSpace": "def plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=\n  LinearMap.ker (homMap N - LinearMap.id)",
 "minusSpace": "def minusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=\n  LinearMap.ker (homMap N + LinearMap.id)",
 "mem_plusSpace": "theorem mem_plusSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :\n    v ∈ plusSpace N ↔ homMap N v = v",
 "mem_minusSpace": "theorem mem_minusSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :\n    v ∈ minusSpace N ↔ homMap N v = -v",
 "finrank_plus_add_finrank_minus": "theorem finrank_plus_add_finrank_minus {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : ∀ x, N (N x) = x) :\n    Module.finrank ℝ (plusSpace N) + Module.finrank ℝ (minusSpace N) = d + 1",
 "hom_zero_mem_plusSpace": "theorem hom_zero_mem_plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    hom (0 : Fin d → ℝ) ∈ plusSpace N",
 "lift_corner_mem_minusSpace": "theorem lift_corner_mem_minusSpace {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : IsNot Ω z N) :\n    Matrix.vecCons (0 : ℝ) z ∈ minusSpace N",
 "one_le_finrank_plusSpace": "theorem one_le_finrank_plusSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    1 ≤ Module.finrank ℝ (plusSpace N)",
 "one_le_finrank_minusSpace": "theorem one_le_finrank_minusSpace {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : IsNot Ω z N) :\n    1 ≤ Module.finrank ℝ (minusSpace N)",
 "not_even_of_balanced": "theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) : ¬ Even d",
 "split_of_balanced": "theorem split_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) :\n    (a - 1) = (b - 1) ∧ (a - 1) + (b - 1) + 1 = d",
 "sumsq_smul": "theorem sumsq_smul (c : ℝ) (x : Fin d → ℝ) : ∑ j, (c • x) j ^ 2 = c ^ 2 * ∑ j, x j ^ 2",
 "sumsq_apply_le_of_preserves": "theorem sumsq_apply_le_of_preserves {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 ≤ ∑ j, x j ^ 2",
 "sumsq_apply_eq": "theorem sumsq_apply_eq {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (x : Fin d → ℝ) : ∑ j, (N x) j ^ 2 = ∑ j, x j ^ 2",
 "sumsq_add": "theorem sumsq_add (u v : Fin d → ℝ) :\n    ∑ j, (u + v) j ^ 2 = ∑ j, u j ^ 2 + 2 * ∑ j, u j * v j + ∑ j, v j ^ 2",
 "dot_apply_apply": "theorem dot_apply_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :\n    ∑ j, (N x) j * (N y) j = ∑ j, x j * y j",
 "dot_apply": "theorem dot_apply {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (x y : Fin d → ℝ) :\n    ∑ j, (N x) j * y j = ∑ j, x j * (N y) j",
 "homMap_dot": "theorem homMap_dot {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (u v : HVec d) :\n    ∑ μ, homMap N u μ * v μ = ∑ μ, u μ * homMap N v μ",
 "toOp": "def toOp (ω : W d) : HVec d →ₗ[ℝ] HVec d := Matrix.toLin' (Matrix.of ω)",
 "fromOp": "def fromOp (F : HVec d →ₗ[ℝ] HVec d) : W d := Matrix.of.symm (Matrix.toLin'.symm F)",
 "toOp_fromOp": "theorem toOp_fromOp (F : HVec d →ₗ[ℝ] HVec d) : toOp (fromOp F) = F",
 "fromOp_toOp": "theorem fromOp_toOp (ω : W d) : fromOp (toOp ω) = ω",
 "toOp_injective": "theorem toOp_injective : Function.Injective (toOp : W d → HVec d →ₗ[ℝ] HVec d)",
 "toOp_apply": "theorem toOp_apply (ω : W d) (v : HVec d) (μ : Fin (d + 1)) :\n    toOp ω v μ = ∑ ν, ω μ ν * v ν",
 "toOpLin": "def toOpLin : W d →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where\n  toFun := toOp\n  map_add' ω₁ ω₂ := by\n    apply LinearMap.ext; intro v; funext μ\n    simp only [toOp_apply, LinearMap.add_apply, Pi.add_apply, add_mul, Finset.sum_add_distrib]\n  map_smul' c ω := by\n    apply LinearMap.ext; intro v; funext μ\n    simp only [toOp_apply, LinearMap.smul_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply,\n      Finset.mul_sum, mul_assoc]",
 "toOpLin_apply": "theorem toOpLin_apply (ω : W d) : toOpLin ω = toOp ω",
 "fromOpLin": "def fromOpLin : (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] W d where\n  toFun := fromOp\n  map_add' F₁ F₂ := by\n    apply toOp_injective\n    rw [toOp_fromOp, ← toOpLin_apply, map_add, toOpLin_apply, toOpLin_apply, toOp_fromOp,\n      toOp_fromOp]\n  map_smul' c F := by\n    apply toOp_injective\n    rw [toOp_fromOp, ← toOpLin_apply, map_smul, toOpLin_apply, toOp_fromOp, RingHom.id_apply]",
 "fromOpLin_apply": "theorem fromOpLin_apply (F : HVec d →ₗ[ℝ] HVec d) : fromOpLin F = fromOp F",
 "toOp_actC": "theorem toOp_actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :\n    toOp (actC N ω) = homMap N ∘ₗ toOp ω",
 "toOp_actT": "theorem toOp_actT {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) (ω : W d) : toOp (actT N ω) = toOp ω ∘ₗ homMap N",
 "actT_actT": "theorem actT_actT {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :\n    actT N (actT N ω) = ω",
 "actC_actC": "theorem actC_actC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (ω : W d) :\n    actC N (actC N ω) = ω",
 "opGate": "def opGate (G : W d ≃ₗ[ℝ] W d) : (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) :=\n  toOpLin ∘ₗ G.toLinearMap ∘ₗ fromOpLin",
 "opGate_toOp": "theorem opGate_toOp (G : W d ≃ₗ[ℝ] W d) (ω : W d) : opGate G (toOp ω) = toOp (G ω)",
 "opGate_comp_homMap": "theorem opGate_comp_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    (F : HVec d →ₗ[ℝ] HVec d) : opGate G (F ∘ₗ homMap N) = opGate G F ∘ₗ homMap N",
 "opGate_homMap_comp": "theorem opGate_homMap_comp {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    (F : HVec d →ₗ[ℝ] HVec d) :\n    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N",
 "projMinus": "noncomputable def projMinus {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    HVec d →ₗ[ℝ] minusSpace N :=\n  LinearMap.codRestrict (minusSpace N) ((1 / 2 : ℝ) • (LinearMap.id - homMap N)) fun v => by\n    rw [mem_minusSpace]\n    simp only [LinearMap.smul_apply, LinearMap.sub_apply, LinearMap.id_apply, map_smul, map_sub,\n      homMap_homMap hN]\n    module",
 "projMinus_apply": "theorem projMinus_apply {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) (v : HVec d) :\n    (projMinus hN v : HVec d) = (1 / 2 : ℝ) • (v - homMap N v)",
 "projMinus_of_mem": "theorem projMinus_of_mem {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) {u : HVec d}\n    (hu : u ∈ minusSpace N) : (projMinus hN u : HVec d) = u",
 "projMinus_homMap": "theorem projMinus_homMap {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    (v : HVec d) : projMinus hN (homMap N v) = - projMinus hN v",
 "OpSpace": "abbrev OpSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) := minusSpace N →ₗ[ℝ] HVec d",
 "Pop": "def Pop (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : OpSpace N →ₗ[ℝ] OpSpace N :=\n  LinearMap.llcomp ℝ (minusSpace N) (HVec d) (HVec d) (homMap N)",
 "Pop_apply": "theorem Pop_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : OpSpace N) (u : minusSpace N) :\n    Pop N f u = homMap N (f u)",
 "Lop": "noncomputable def Lop (G : W d ≃ₗ[ℝ] W d) {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : ∀ x, N (N x) = x) :\n    OpSpace N →ₗ[ℝ] OpSpace N :=\n  LinearMap.lcomp ℝ (HVec d) (minusSpace N).subtype ∘ₗ opGate G ∘ₗ\n    LinearMap.lcomp ℝ (HVec d) (projMinus hN)",
 "Lop_apply": "theorem Lop_apply (G : W d ≃ₗ[ℝ] W d) {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    (f : OpSpace N) (u : minusSpace N) :\n    Lop G hN f u = opGate G (f ∘ₗ projMinus hN) u",
 "Lop_anti": "theorem Lop_anti {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (f : OpSpace N) :\n    Lop G hN.invol (Pop N f) = - Pop N (Lop G hN.invol f)",
 "Lop_eq_zero": "theorem Lop_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (f : OpSpace N)\n    (hf : Lop G hN.invol f = 0) : f = 0",
 "Lop_injective": "theorem Lop_injective {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    Function.Injective (Lop G hN.invol)",
 "finrank_ker_eq_of_pointwise": "theorem finrank_ker_eq_of_pointwise {M E : Type*} [AddCommGroup M] [Module ℝ M]\n    [FiniteDimensional ℝ M] [AddCommGroup E] [Module ℝ E] [FiniteDimensional ℝ E]\n    (S : Submodule ℝ E) (T : (M →ₗ[ℝ] E) →ₗ[ℝ] (M →ₗ[ℝ] E))\n    (hT : ∀ f, T f = 0 ↔ ∀ u, f u ∈ S) :\n    Module.finrank ℝ (LinearMap.ker T) = Module.finrank ℝ M * Module.finrank ℝ S",
 "finrank_ker_Pop_sub": "theorem finrank_ker_Pop_sub (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Module.finrank ℝ (LinearMap.ker (Pop N - LinearMap.id))\n      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N)",
 "finrank_ker_Pop_add": "theorem finrank_ker_Pop_add (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Module.finrank ℝ (LinearMap.ker (Pop N + LinearMap.id))\n      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N)",
 "finrank_plus_eq_finrank_minus": "theorem finrank_plus_eq_finrank_minus {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)",
 "not_even_of_nativeGate": "theorem not_even_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    ¬ Even d",
 "ne_two_of_nativeGate": "theorem ne_two_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 2",
 "ne_four_of_nativeGate": "theorem ne_four_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 4",
 "BlockData": "structure BlockData (p : ℕ) : Prop where\n  blocks : ∃ (m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ)\n      (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ),\n    (∀ r s, B r s = - B s r) ∧\n    (∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →\n      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →\n        0 ≤ (1 + s * A i k l)\n          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) ∧\n    (∃ r k l, A r k l ≠ 0)",
 "p_le_one_of_blockData": "theorem p_le_one_of_blockData {p : ℕ} (h : BlockData p) : p ≤ 1",
 "tangentPlus": "noncomputable def tangentPlus (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : ℕ :=\n  Module.finrank ℝ (plusSpace N) - 1",
 "sum_univ_four'": "theorem sum_univ_four' (f : Fin (3 + 1) → ℝ) : ∑ i, f i = f 0 + f 1 + f 2 + f 3",
 "sum_univ_two'": "theorem sum_univ_two' (f : Fin (1 + 1) → ℝ) : ∑ i, f i = f 0 + f 1",
 "sgn": "def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1",
 "pc": "def pc : Fin 4 → Fin 4 → Fin 4\n  | 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 3 | 0, 3 => 3\n  | 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2\n  | 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1\n  | 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 0 | 3, 3 => 0",
 "pt": "def pt : Fin 4 → Fin 4 → Fin 4\n  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3\n  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 3 | 1, 3 => 2\n  | 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 3 | 2, 3 => 2\n  | 3, 0 => 0 | 3, 1 => 1 | 3, 2 => 2 | 3, 3 => 3",
 "cnotFun": "def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)",
 "cnotFun_apply": "theorem cnotFun_apply (ω : W 3) (μ ν : Fin 4) : cnotFun ω μ ν = sgn μ ν * ω (pc μ ν) (pt μ ν)",
 "pc_pc": "theorem pc_pc : ∀ μ ν : Fin 4, pc (pc μ ν) (pt μ ν) = μ",
 "pt_pt": "theorem pt_pt : ∀ μ ν : Fin 4, pt (pc μ ν) (pt μ ν) = ν",
 "sgn_mul_sgn": "theorem sgn_mul_sgn : ∀ μ ν : Fin 4, sgn μ ν * sgn (pc μ ν) (pt μ ν) = 1",
 "cnotFun_cnotFun": "theorem cnotFun_cnotFun (ω : W 3) : cnotFun (cnotFun ω) = ω",
 "cnot": "def cnot : W 3 ≃ₗ[ℝ] W 3 where\n  toFun := cnotFun\n  invFun := cnotFun\n  map_add' ω₁ ω₂ := by\n    funext μ ν\n    simp only [cnotFun_apply, Pi.add_apply, mul_add]\n  map_smul' c ω := by\n    funext μ ν\n    simp only [cnotFun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]\n    ring\n  left_inv := cnotFun_cnotFun\n  right_inv := cnotFun_cnotFun",
 "cnot_apply": "theorem cnot_apply (ω : W 3) : cnot ω = cnotFun ω",
 "cnot_symm_apply": "theorem cnot_symm_apply (ω : W 3) : cnot.symm ω = cnotFun ω",
 "z3": "def z3 : Fin 3 → ℝ := ![0, 0, 1]",
 "nflip": "def nflip : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i\n  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]\n  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring",
 "nflip_apply": "theorem nflip_apply (x : Fin 3 → ℝ) (i : Fin 3) : nflip x i = (![1, -1, -1] : Fin 3 → ℝ) i * x i",
 "nflip_zero'": "@[simp] theorem nflip_zero' (x : Fin 3 → ℝ) : nflip x 0 = x 0",
 "nflip_one": "@[simp] theorem nflip_one (x : Fin 3 → ℝ) : nflip x 1 = -x 1",
 "nflip_two": "@[simp] theorem nflip_two (x : Fin 3 → ℝ) : nflip x 2 = -x 2",
 "homMap_nflip_zero": "@[simp] theorem homMap_nflip_zero (v : HVec 3) : homMap nflip v 0 = v 0",
 "homMap_nflip_one": "@[simp] theorem homMap_nflip_one (v : HVec 3) : homMap nflip v 1 = v 1",
 "homMap_nflip_two": "@[simp] theorem homMap_nflip_two (v : HVec 3) : homMap nflip v 2 = -v 2",
 "homMap_nflip_three": "@[simp] theorem homMap_nflip_three (v : HVec 3) : homMap nflip v 3 = -v 3",
 "hom_one'": "@[simp] theorem hom_one' (x : Fin 3 → ℝ) : hom x 1 = x 0",
 "hom_two'": "@[simp] theorem hom_two' (x : Fin 3 → ℝ) : hom x 2 = x 1",
 "hom_three'": "@[simp] theorem hom_three' (x : Fin 3 → ℝ) : hom x 3 = x 2",
 "z3_zero": "@[simp] theorem z3_zero : z3 0 = 0",
 "z3_one": "@[simp] theorem z3_one : z3 1 = 0",
 "z3_two": "@[simp] theorem z3_two : z3 2 = 1",
 "corner_zero": "theorem corner_zero (z : Fin d → ℝ) : corner z 0 = z",
 "corner_one": "theorem corner_one (z : Fin d → ℝ) : corner z 1 = -z",
 "actT_apply": "theorem actT_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) (μ ν : Fin (d + 1)) :\n    actT N ω μ ν = homMap N (ω μ) ν",
 "actC_apply": "theorem actC_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) (μ ν : Fin (d + 1)) :\n    actC N ω μ ν = homMap N (fun κ => ω κ ν) μ",
 "prodState_apply": "theorem prodState_apply (x y : Fin d → ℝ) (μ ν : Fin (d + 1)) :\n    prodState x y μ ν = hom x μ * hom y ν",
 "isNot_nflip": "theorem isNot_nflip : IsNot (eball 3) z3 nflip",
 "cnot_frame": "theorem cnot_frame (a b : Fin 2) :\n    cnot (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b))",
 "cnot_relT": "theorem cnot_relT (ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω",
 "cnot_relC": "theorem cnot_relC (ω : W 3) : actC nflip (cnot (actC nflip ω)) = actT nflip (cnot ω)",
 "Lor": "def Lor (v : HVec d) : Prop := 0 ≤ v 0 ∧ ∑ j : Fin d, v j.succ ^ 2 ≤ v 0 ^ 2",
 "lor_smul": "theorem lor_smul {v : HVec d} (hv : Lor v) {c : ℝ} (hc : 0 ≤ c) : Lor (c • v)",
 "lor_pair_bound": "theorem lor_pair_bound {v : HVec d} (hv : Lor v) {x : Fin d → ℝ} (hx : x ∈ eball d) :\n    -v 0 ≤ ∑ j : Fin d, v j.succ * x j ∧ ∑ j : Fin d, v j.succ * x j ≤ v 0",
 "affOf": "noncomputable def affOf (v : HVec d) : (Fin d → ℝ) →ᵃ[ℝ] ℝ where\n  toFun x := v 0 + ∑ j : Fin d, v j.succ * x j\n  linear := ∑ j : Fin d, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ)\n  map_vadd' p w := by\n    simp only [vadd_eq_add, Pi.add_apply, mul_add, Finset.sum_add_distrib, LinearMap.sum_apply,\n      LinearMap.smul_apply, LinearMap.proj_apply, smul_eq_mul]\n    ring",
 "affOf_apply": "theorem affOf_apply (v : HVec d) (x : Fin d → ℝ) : affOf v x = v 0 + ∑ j : Fin d, v j.succ * x j",
 "affOf_linear": "theorem affOf_linear (v : HVec d) :\n    (affOf v).linear = ∑ j : Fin d, v j.succ • (LinearMap.proj j : (Fin d → ℝ) →ₗ[ℝ] ℝ)",
 "ehom_affOf": "theorem ehom_affOf (v : HVec d) : ehom (affOf v) = v",
 "isEffectOn_affOf": "theorem isEffectOn_affOf {v : HVec d} (hv : Lor v) (hv0 : v 0 ≤ 1 / 2) :\n    IsEffectOn (eball d) (affOf v)",
 "ehom_zero_eq": "theorem ehom_zero_eq (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : ehom e 0 = e 0",
 "lor_ehom": "theorem lor_ehom {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) : Lor (ehom e)",
 "pairVal_eq_sum_toOp": "theorem pairVal_eq_sum_toOp (a b : HVec d) (ω : W d) :\n    pairVal a b ω = ∑ μ, a μ * toOp ω b μ",
 "pairVal_smul_left": "theorem pairVal_smul_left (c : ℝ) (a b : HVec d) (ω : W d) :\n    pairVal (c • a) b ω = c * pairVal a b ω",
 "pairVal_smul_right": "theorem pairVal_smul_right (c : ℝ) (a b : HVec d) (ω : W d) :\n    pairVal a (c • b) ω = c * pairVal a b ω",
 "pairVal_nonneg_of_maxCone": "theorem pairVal_nonneg_of_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {a b : HVec d}\n    (ha : Lor a) (hb : Lor b) : 0 ≤ pairVal a b ω",
 "lor_of_forall_pair": "theorem lor_of_forall_pair {g : HVec d} (h : ∀ a : HVec d, Lor a → 0 ≤ ∑ μ, a μ * g μ) :\n    Lor g",
 "lor_toOp_of_maxCone": "theorem lor_toOp_of_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {f : HVec d} (hf : Lor f) :\n    Lor (toOp ω f)",
 "lor_three": "theorem lor_three {v : HVec 3} (hv : Lor v) : 0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2",
 "lor_of_three": "theorem lor_of_three {v : HVec 3} (h0 : 0 ≤ v 0) (h : v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2) :\n    Lor v",
 "cnot_core": "theorem cnot_core (e0 a1 a2 a3 x1 x2 x3 P Q R S : ℝ) (he0 : 0 ≤ e0)\n    (ha : a1 ^ 2 + a2 ^ 2 + a3 ^ 2 ≤ e0 ^ 2) (hx : x1 ^ 2 + x2 ^ 2 + x3 ^ 2 ≤ 1)\n    (hP : 0 ≤ P) (hPQ : R ^ 2 + S ^ 2 ≤ P ^ 2 - Q ^ 2) :\n    0 ≤ e0 * (P + x3 * Q) + a1 * (x1 * R - x2 * S) + a2 * (x2 * R + x1 * S)\n      + a3 * (x3 * P + Q)",
 "cnot_target": "theorem cnot_target (f0 b1 b2 b3 y1 y2 y3 : ℝ) (hf0 : 0 ≤ f0)\n    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 ≤ f0 ^ 2) (hy : y1 ^ 2 + y2 ^ 2 + y3 ^ 2 ≤ 1) :\n    0 ≤ f0 + b1 * y1 ∧\n      (b1 + f0 * y1) ^ 2 + (b3 * y2 - b2 * y3) ^ 2\n        ≤ (f0 + b1 * y1) ^ 2 - (b2 * y2 + b3 * y3) ^ 2",
 "prodEffVal_cnot_prodState": "theorem prodEffVal_cnot_prodState (e f : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 3 → ℝ) :\n    prodEffVal e f (cnot (prodState x y))\n      = ehom e 0 * ((ehom f 0 + ehom f 1 * y 0) + x 2 * (ehom f 2 * y 1 + ehom f 3 * y 2))\n        + ehom e 1 * (x 0 * (ehom f 1 + ehom f 0 * y 0) - x 1 * (ehom f 3 * y 1 - ehom f 2 * y 2))\n        + ehom e 2 * (x 1 * (ehom f 1 + ehom f 0 * y 0) + x 0 * (ehom f 3 * y 1 - ehom f 2 * y 2))\n        + ehom e 3 * (x 2 * (ehom f 0 + ehom f 1 * y 0) + (ehom f 2 * y 1 + ehom f 3 * y 2))",
 "cnot_prodEffVal_nonneg": "theorem cnot_prodEffVal_nonneg {e f : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball 3) e)\n    (hf : IsEffectOn (eball 3) f) {x y : Fin 3 → ℝ} (hx : x ∈ eball 3) (hy : y ∈ eball 3) :\n    0 ≤ prodEffVal e f (cnot (prodState x y))",
 "cnot_prodState_mem_maxCone": "theorem cnot_prodState_mem_maxCone {x y : Fin 3 → ℝ} (hx : x ∈ eball 3) (hy : y ∈ eball 3) :\n    cnot (prodState x y) ∈ maxCone (eball 3)",
 "nativeGate_cnot": "theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot",
 "extreme_of_unit": "theorem extreme_of_unit {x : Fin 3 → ℝ} (hx : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 = 1) :\n    x ∈ (eball 3).extremePoints ℝ",
 "xplus": "def xplus : Fin 3 → ℝ := ![1, 0, 0]",
 "xplus_zero": "@[simp] theorem xplus_zero : xplus 0 = 1",
 "xplus_one": "@[simp] theorem xplus_one : xplus 1 = 0",
 "xplus_two": "@[simp] theorem xplus_two : xplus 2 = 0",
 "phiW": "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0",
 "cnot_prodState_xplus_z3": "theorem cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW",
 "xplus_mem": "theorem xplus_mem : xplus ∈ eball 3",
 "z3_mem": "theorem z3_mem : z3 ∈ eball 3",
 "phiW_not_product": "theorem phiW_not_product : ¬ IsProduct (eball 3) phiW",
 "phiW_mem_jointStates": "theorem phiW_mem_jointStates : phiW ∈ jointStates (eball 3)",
 "toOp_phiW_zero": "@[simp] theorem toOp_phiW_zero (t : HVec 3) : toOp phiW t 0 = t 0",
 "toOp_phiW_one": "@[simp] theorem toOp_phiW_one (t : HVec 3) : toOp phiW t 1 = t 1",
 "toOp_phiW_two": "@[simp] theorem toOp_phiW_two (t : HVec 3) : toOp phiW t 2 = -t 2",
 "toOp_phiW_three": "@[simp] theorem toOp_phiW_three (t : HVec 3) : toOp phiW t 3 = t 3",
 "lor_ray": "theorem lor_ray {f g h : HVec 3} (hf : f 1 ^ 2 + f 2 ^ 2 + f 3 ^ 2 = f 0 ^ 2)\n    (hg : Lor g) (hh : Lor h) {a b : ℝ} (ha : 0 < a) (hb : 0 < b)\n    (hsum : a • g + b • h = f) :\n    f 0 * g 1 = g 0 * f 1 ∧ f 0 * g 2 = g 0 * f 2 ∧ f 0 * g 3 = g 0 * f 3",
 "tv": "def tv (i : Fin 4) (s : ℝ) : HVec 3 := fun μ => if μ = 0 then 1 else if μ = i then s else 0",
 "toOp_tv1": "theorem toOp_tv1 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 1 s) μ = ω μ 0 + ω μ 1 * s",
 "toOp_tv2": "theorem toOp_tv2 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 2 s) μ = ω μ 0 + ω μ 2 * s",
 "toOp_tv3": "theorem toOp_tv3 (ω : W 3) (s : ℝ) (μ : Fin 4) : toOp ω (tv 3 s) μ = ω μ 0 + ω μ 3 * s",
 "ray_eqs": "theorem ray_eqs {ω₁ ω₂ : W 3} (h₁ : ω₁ ∈ maxCone (eball 3)) (h₂ : ω₂ ∈ maxCone (eball 3))\n    {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (hsum : a • ω₁ + b • ω₂ = phiW) {t : HVec 3}\n    (ht0 : t 0 = 1) (ht : t 1 ^ 2 + t 2 ^ 2 + t 3 ^ 2 = 1) :\n    toOp ω₁ t 1 = toOp ω₁ t 0 * t 1 ∧ toOp ω₁ t 2 = toOp ω₁ t 0 * (-t 2) ∧\n      toOp ω₁ t 3 = toOp ω₁ t 0 * t 3",
 "phiW_eq_of_segment": "theorem phiW_eq_of_segment {ω₁ ω₂ : W 3} (h₁ : ω₁ ∈ jointStates (eball 3))\n    (h₂ : ω₂ ∈ jointStates (eball 3)) {a b : ℝ} (ha : 0 < a) (hb : 0 < b)\n    (hsum : a • ω₁ + b • ω₂ = phiW) : ω₁ = phiW",
 "entangling_cnot": "theorem entangling_cnot : Entangling (eball 3) cnot",
 "fin1_ext": "theorem fin1_ext {x y : Fin 1 → ℝ} (h : x 0 = y 0) : x = y",
 "corner_mem_one": "theorem corner_mem_one {z : Fin 1 → ℝ} (hz : z 0 ^ 2 = 1) : ∀ a : Fin 2, corner z a ∈ eball 1",
 "eq_corner_of_extreme": "theorem eq_corner_of_extreme {z : Fin 1 → ℝ} (hz : z 0 ^ 2 = 1) {x : Fin 1 → ℝ}\n    (hx : x ∈ (eball 1).extremePoints ℝ) : ∃ a : Fin 2, x = corner z a",
 "not_entangling_one": "theorem not_entangling_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}\n    {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) :\n    ¬ Entangling (eball 1) G",
 "tens": "def tens (X Y : HVec d) : W d := fun μ ν => X μ * Y ν",
 "tens_apply": "theorem tens_apply (X Y : HVec d) (μ ν : Fin (d + 1)) : tens X Y μ ν = X μ * Y ν",
 "prodState_eq_tens": "theorem prodState_eq_tens (x y : Fin d → ℝ) : prodState x y = tens (hom x) (hom y)",
 "tens_add_left": "theorem tens_add_left (X X' Y : HVec d) : tens (X + X') Y = tens X Y + tens X' Y",
 "tens_add_right": "theorem tens_add_right (X Y Y' : HVec d) : tens X (Y + Y') = tens X Y + tens X Y'",
 "tens_smul_left": "theorem tens_smul_left (c : ℝ) (X Y : HVec d) : tens (c • X) Y = c • tens X Y",
 "tens_smul_right": "theorem tens_smul_right (c : ℝ) (X Y : HVec d) : tens X (c • Y) = c • tens X Y",
 "tens_zero_left": "theorem tens_zero_left (Y : HVec d) : tens 0 Y = 0",
 "tens_zero_right": "theorem tens_zero_right (X : HVec d) : tens X 0 = 0",
 "tensL": "def tensL (X : HVec d) : HVec d →ₗ[ℝ] W d where\n  toFun Y := tens X Y\n  map_add' Y Y' := tens_add_right X Y Y'\n  map_smul' c Y := tens_smul_right c X Y",
 "tensL_apply": "theorem tensL_apply (X Y : HVec d) : tensL X Y = tens X Y",
 "tensR": "def tensR (Y : HVec d) : HVec d →ₗ[ℝ] W d where\n  toFun X := tens X Y\n  map_add' X X' := tens_add_left X X' Y\n  map_smul' c X := tens_smul_left c X Y",
 "tensR_apply": "theorem tensR_apply (X Y : HVec d) : tensR Y X = tens X Y",
 "pairVal_add_omega": "theorem pairVal_add_omega (a b : HVec d) (ω ω' : W d) :\n    pairVal a b (ω + ω') = pairVal a b ω + pairVal a b ω'",
 "pairVal_smul_omega": "theorem pairVal_smul_omega (c : ℝ) (a b : HVec d) (ω : W d) :\n    pairVal a b (c • ω) = c * pairVal a b ω",
 "pairVal_zero_omega": "theorem pairVal_zero_omega (a b : HVec d) : pairVal a b (0 : W d) = 0",
 "pairVal_add_left": "theorem pairVal_add_left (a a' b : HVec d) (ω : W d) :\n    pairVal (a + a') b ω = pairVal a b ω + pairVal a' b ω",
 "pairVal_add_right": "theorem pairVal_add_right (a b b' : HVec d) (ω : W d) :\n    pairVal a (b + b') ω = pairVal a b ω + pairVal a b' ω",
 "pairVal_tens": "theorem pairVal_tens (a b X Y : HVec d) :\n    pairVal a b (tens X Y) = (∑ μ, a μ * X μ) * ∑ ν, Y ν * b ν",
 "pvOmega": "def pvOmega (a b : HVec d) : W d →ₗ[ℝ] ℝ where\n  toFun ω := pairVal a b ω\n  map_add' ω ω' := pairVal_add_omega a b ω ω'\n  map_smul' c ω := pairVal_smul_omega c a b ω",
 "pvOmega_apply": "theorem pvOmega_apply (a b : HVec d) (ω : W d) : pvOmega a b ω = pairVal a b ω",
 "pvLeft": "def pvLeft (b : HVec d) (ω : W d) : HVec d →ₗ[ℝ] ℝ where\n  toFun a := pairVal a b ω\n  map_add' a a' := pairVal_add_left a a' b ω\n  map_smul' c a := pairVal_smul_left c a b ω",
 "pvLeft_apply": "theorem pvLeft_apply (a b : HVec d) (ω : W d) : pvLeft b ω a = pairVal a b ω",
 "pairVal_hom_zero_left": "theorem pairVal_hom_zero_left (b : HVec d) (ω : W d) :\n    pairVal (hom (0 : Fin d → ℝ)) b ω = ∑ ν, b ν * ω 0 ν",
 "smul_mem_maxCone": "theorem smul_mem_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {c : ℝ} (hc : 0 ≤ c) :\n    c • ω ∈ maxCone (eball d)",
 "zero_mem_maxCone": "theorem zero_mem_maxCone : (0 : W d) ∈ maxCone (eball d)",
 "lor_eq_zero_of_head": "theorem lor_eq_zero_of_head {X : HVec d} (hX : Lor X) (h0 : X 0 = 0) : X = 0",
 "lor_eq_smul_hom": "theorem lor_eq_smul_hom {X : HVec d} (hX : Lor X) (hpos : 0 < X 0) :\n    X = X 0 • hom (fun j => (X 0)⁻¹ * X j.succ) ∧ (fun j => (X 0)⁻¹ * X j.succ) ∈ eball d",
 "tens_mem_maxCone": "theorem tens_mem_maxCone {G' : W d →ₗ[ℝ] W d}\n    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))\n    {X Y : HVec d} (hX : Lor X) (hY : Lor Y) : G' (tens X Y) ∈ maxCone (eball d)",
 "gate_pairVal_nonneg": "theorem gate_pairVal_nonneg {G' : W d →ₗ[ℝ] W d}\n    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))\n    {a X b Y : HVec d} (ha : Lor a) (hX : Lor X) (hb : Lor b) (hY : Lor Y) :\n    0 ≤ pairVal a b (G' (tens X Y))",
 "bvec": "def bvec (i : Fin (d + 1)) : HVec d := fun k => if i = k then 1 else 0",
 "bvec_apply": "theorem bvec_apply (i k : Fin (d + 1)) : bvec i k = if i = k then (1 : ℝ) else 0",
 "bvec_zero_eq": "theorem bvec_zero_eq : bvec (0 : Fin (d + 1)) = hom (0 : Fin d → ℝ)",
 "lift": "def lift (c : Fin d → ℝ) : HVec d := Matrix.vecCons 0 c",
 "lift_zero": "@[simp] theorem lift_zero (c : Fin d → ℝ) : lift c 0 = 0",
 "lift_succ": "@[simp] theorem lift_succ (c : Fin d → ℝ) (j : Fin d) : lift c j.succ = c j",
 "hom_eq_add_lift": "theorem hom_eq_add_lift (x : Fin d → ℝ) : hom x = hom 0 + lift x",
 "lift_add": "theorem lift_add (c c' : Fin d → ℝ) : lift (c + c') = lift c + lift c'",
 "lift_smul": "theorem lift_smul (c : ℝ) (x : Fin d → ℝ) : lift (c • x) = c • lift x",
 "lift_neg": "theorem lift_neg (x : Fin d → ℝ) : lift (-x) = -lift x",
 "lift_vecTail": "theorem lift_vecTail {u : HVec d} (h : u 0 = 0) : lift (Matrix.vecTail u) = u",
 "lor_hom_zero": "theorem lor_hom_zero : Lor (hom (0 : Fin d → ℝ))",
 "lor_hom": "theorem lor_hom {x : Fin d → ℝ} (hx : x ∈ eball d) : Lor (hom x)",
 "lor_hom_of_unit": "theorem lor_hom_of_unit {x : Fin d → ℝ} (hx : ∑ j, x j ^ 2 = 1) : Lor (hom x)",
 "lor_hom_zero_add_smul_bvec": "theorem lor_hom_zero_add_smul_bvec (j : Fin d) {s : ℝ} (hs : s ^ 2 ≤ 1) :\n    Lor (hom (0 : Fin d → ℝ) + s • bvec j.succ)",
 "linearMap_eq_zero_of_nonneg_lor": "theorem linearMap_eq_zero_of_nonneg_lor (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, Lor X → 0 ≤ F X)\n    (h0 : F (hom 0) = 0) : F = 0",
 "linearMap_eq_zero_of_lor": "theorem linearMap_eq_zero_of_lor {E : Type*} [AddCommGroup E] [Module ℝ E] (F : HVec d →ₗ[ℝ] E)\n    (h : ∀ X, Lor X → F X = 0) : F = 0",
 "hom_add_hom_neg": "theorem hom_add_hom_neg (z : Fin d → ℝ) : hom z + hom (-z) = (2 : ℝ) • hom 0",
 "dot_hom_neg_hom": "theorem dot_hom_neg_hom {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) :\n    ∑ μ, hom (-z) μ * hom z μ = 0",
 "dot_hom_hom_neg": "theorem dot_hom_hom_neg {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) :\n    ∑ μ, hom z μ * hom (-z) μ = 0",
 "lor_face": "theorem lor_face {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {m : HVec d} (hm : Lor m)\n    (h : ∑ μ, hom (-z) μ * m μ = 0) : m = m 0 • hom z",
 "tens_hom_inj": "theorem tens_hom_inj {x : Fin d → ℝ} {Y Y' : HVec d} (h : tens (hom x) Y = tens (hom x) Y') :\n    Y = Y'",
 "toOp_bvec": "theorem toOp_bvec (ω : W d) (ν μ : Fin (d + 1)) : toOp ω (bvec ν) μ = ω μ ν",
 "cornerMap": "def cornerMap (z : Fin d → ℝ) (G' : W d →ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=\n  (LinearMap.proj (0 : Fin (d + 1)) : W d →ₗ[ℝ] HVec d) ∘ₗ G' ∘ₗ tensL (hom z)",
 "cornerMap_apply": "theorem cornerMap_apply (z : Fin d → ℝ) (G' : W d →ₗ[ℝ] W d) (Y : HVec d) :\n    cornerMap z G' Y = G' (tens (hom z) Y) 0",
 "corner_form": "theorem corner_form {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {G' : W d →ₗ[ℝ] W d}\n    (hframe : ∀ b : Fin 2, G' (prodState z (corner z b)) = prodState z (corner z b))\n    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d)) (Y : HVec d) :\n    G' (tens (hom z) Y) = tens (hom z) (cornerMap z G' Y)",
 "lor_cornerMap": "theorem lor_cornerMap {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) {G' : W d →ₗ[ℝ] W d}\n    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G' (prodState x y) ∈ maxCone (eball d))\n    {Y : HVec d} (hY : Lor Y) : Lor (cornerMap z G' Y)",
 "Mfwd": "def Mfwd (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=\n  cornerMap z (G : W d →ₗ[ℝ] W d)",
 "Minv": "def Minv (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) : HVec d →ₗ[ℝ] HVec d :=\n  cornerMap z (G.symm : W d →ₗ[ℝ] W d)",
 "gate_corner": "theorem gate_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom z) Y) = tens (hom z) (Mfwd z G Y)",
 "gate_corner_symm": "theorem gate_corner_symm {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G.symm (tens (hom z) Y) = tens (hom z) (Minv z G Y)",
 "Mfwd_Minv": "theorem Mfwd_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    Mfwd z G (Minv z G Y) = Y",
 "Minv_Mfwd": "theorem Minv_Mfwd {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    Minv z G (Mfwd z G Y) = Y",
 "lor_Minv": "theorem lor_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {Y : HVec d} (hY : Lor Y) :\n    Lor (Minv z G Y)",
 "actT_tens": "theorem actT_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y : HVec d) :\n    actT N (tens X Y) = tens X (homMap N Y)",
 "actC_tens": "theorem actC_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y : HVec d) :\n    actC N (tens X Y) = tens (homMap N X) Y",
 "gate_actT": "theorem gate_actT {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (ω : W d) :\n    G (actT N ω) = actT N (G ω)",
 "gate_actC": "theorem gate_actC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (ω : W d) :\n    G (actC N ω) = actC N (actT N (G ω))",
 "Mfwd_homMap": "theorem Mfwd_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    Mfwd z G (homMap N Y) = homMap N (Mfwd z G Y)",
 "Minv_homMap": "theorem Minv_homMap {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    Minv z G (homMap N Y) = homMap N (Minv z G Y)",
 "gate_corner_neg": "theorem gate_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y))",
 "gt_corner": "theorem gt_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom z) (Minv z G t)) = tens (hom z) t",
 "gt_corner_neg": "theorem gt_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom (-z)) (Minv z G t)) = tens (hom (-z)) (homMap N t)",
 "eq_of_two_smul_eq": "theorem eq_of_two_smul_eq {A B : W d} (h : (2 : ℝ) • A = (2 : ℝ) • B) : A = B",
 "gt_center": "theorem gt_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {t : HVec d}\n    (ht : homMap N t = t) : G (tens (hom 0) (Minv z G t)) = tens (hom 0) t",
 "eq_zero_of_quadratic_nonneg": "theorem eq_zero_of_quadratic_nonneg {α β : ℝ} (hα : 0 ≤ α)\n    (h : ∀ s : ℝ, 0 ≤ α * s ^ 2 + β * s) : β = 0",
 "lor_curve": "theorem lor_curve {w c : Fin d → ℝ} (hw : ∑ j, w j ^ 2 = 1) (hc : ∑ j, c j ^ 2 ≤ 1)\n    (hwc : ∑ j, w j * c j = 0) (s : ℝ) :\n    Lor ((1 + s ^ 2) • hom (0 : Fin d → ℝ) + (1 - s ^ 2) • lift w + (2 * s) • lift c)",
 "tangent_vanish": "theorem tangent_vanish (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, Lor X → 0 ≤ F X) {w c : Fin d → ℝ}\n    (hw : ∑ j, w j ^ 2 = 1) (hc : ∑ j, c j ^ 2 ≤ 1) (hwc : ∑ j, w j * c j = 0)\n    (h0 : F (hom w) = 0) : F (lift c) = 0",
 "gt_tangent_corners": "theorem gt_tangent_corners {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {f t : HVec d} (hf : Lor f) (ht : Lor t) :\n    pairVal (hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 ∧\n    pairVal (hom z) f (G (tens (lift c) (Minv z G t))) = 0",
 "gt_sphere": "theorem gt_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    pairVal a (hom 0 - u) (G (tens (lift c) (Minv z G (hom 0 + u)))) = 0",
 "gt_sphere_corner": "theorem gt_sphere_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    pairVal a (hom z) (G (tens (lift c) (Minv z G (hom z)))) = 0 ∧\n    pairVal a (hom (-z)) (G (tens (lift c) (Minv z G (hom (-z))))) = 0",
 "dotB": "def dotB : HVec d →ₗ[ℝ] HVec d →ₗ[ℝ] ℝ :=\n  LinearMap.mk₂ ℝ (fun u w => ∑ μ, u μ * w μ)\n    (fun u u' w => by\n      show ∑ μ, (u + u') μ * w μ = ∑ μ, u μ * w μ + ∑ μ, u' μ * w μ\n      rw [← Finset.sum_add_distrib]\n      exact Finset.sum_congr rfl fun μ _ => by rw [Pi.add_apply]; ring)\n    (fun r u w => by\n      show ∑ μ, (r • u) μ * w μ = r • ∑ μ, u μ * w μ\n      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]\n      exact Finset.sum_congr rfl fun μ _ => by ring)\n    (fun u w w' => by\n      show ∑ μ, u μ * (w + w') μ = ∑ μ, u μ * w μ + ∑ μ, u μ * w' μ\n      rw [← Finset.sum_add_distrib]\n      exact Finset.sum_congr rfl fun μ _ => by rw [Pi.add_apply]; ring)\n    (fun r u w => by\n      show ∑ μ, u μ * (r • w) μ = r • ∑ μ, u μ * w μ\n      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]\n      exact Finset.sum_congr rfl fun μ _ => by ring)",
 "dotB_apply": "theorem dotB_apply (u w : HVec d) : dotB u w = ∑ μ, u μ * w μ",
 "lor_of_dotB": "theorem lor_of_dotB {X : HVec d} (h0 : 0 ≤ X 0) (h : dotB X X ≤ 2 * X 0 ^ 2) : Lor X",
 "Phi": "noncomputable def Phi (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) (a : HVec d) (c : Fin d → ℝ) :\n    HVec d →ₗ[ℝ] HVec d →ₗ[ℝ] ℝ :=\n  LinearMap.mk₂ ℝ (fun f t => pairVal a f (G (tens (lift c) (Minv z G t))))\n    (fun f f' t => pairVal_add_right a f f' _)\n    (fun r f t => by\n      show pairVal a (r • f) (G (tens (lift c) (Minv z G t)))\n        = r • pairVal a f (G (tens (lift c) (Minv z G t)))\n      rw [pairVal_smul_right, smul_eq_mul])\n    (fun f t t' => by\n      show pairVal a f (G (tens (lift c) (Minv z G (t + t'))))\n        = pairVal a f (G (tens (lift c) (Minv z G t))) + pairVal a f (G (tens (lift c) (Minv z G t')))\n      rw [map_add, tens_add_right, map_add, pairVal_add_omega])\n    (fun r f t => by\n      show pairVal a f (G (tens (lift c) (Minv z G (r • t))))\n        = r • pairVal a f (G (tens (lift c) (Minv z G t)))\n      rw [map_smul, tens_smul_right, map_smul, pairVal_smul_omega, smul_eq_mul])",
 "Phi_apply": "theorem Phi_apply (z : Fin d → ℝ) (G : W d ≃ₗ[ℝ] W d) (a : HVec d) (c : Fin d → ℝ)\n    (f t : HVec d) : Phi z G a c f t = pairVal a f (G (tens (lift c) (Minv z G t)))",
 "Phi_sphere": "theorem Phi_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    Phi z G a c u u = Phi z G a c (hom 0) (hom 0) ∧\n    Phi z G a c (hom 0) u = Phi z G a c u (hom 0)",
 "Phi_center": "theorem Phi_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    Phi z G a c (hom 0) (hom 0) = 0",
 "Phi_center_all": "theorem Phi_center_all {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (a : HVec d) :\n    Phi z G a c (hom 0) (hom 0) = 0",
 "Phi_hom_zero_eq_zero": "theorem Phi_hom_zero_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (hom 0) c f t = 0",
 "Phi_lift_z_eq_zero": "theorem Phi_lift_z_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (lift z) c f t = 0",
 "tangentSpace": "def tangentSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Submodule ℝ (HVec d) :=\n  plusSpace N ⊓ LinearMap.ker (LinearMap.proj (0 : Fin (d + 1)) : HVec d →ₗ[ℝ] ℝ)",
 "mem_tangentSpace": "theorem mem_tangentSpace {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {v : HVec d} :\n    v ∈ tangentSpace N ↔ homMap N v = v ∧ v 0 = 0",
 "hom_zero_ne_zero": "theorem hom_zero_ne_zero : hom (0 : Fin d → ℝ) ≠ 0",
 "finrank_tangentSpace": "theorem finrank_tangentSpace (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Module.finrank ℝ (tangentSpace N) = tangentPlus N",
 "exists_orthonormal_basis": "theorem exists_orthonormal_basis (S : Submodule ℝ (HVec d)) :\n    ∃ (q : ℕ) (v : Fin q → HVec d), q = Module.finrank ℝ S ∧ (∀ r, v r ∈ S) ∧\n      (∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0) ∧\n      (∀ u ∈ S, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0)",
 "tperp": "def tperp (z : Fin d → ℝ) (k : Fin d) : Fin d → ℝ := fun j => (if k = j then 1 else 0) - z k * z j",
 "tperp_apply": "theorem tperp_apply (z : Fin d → ℝ) (k j : Fin d) :\n    tperp z k j = (if k = j then (1 : ℝ) else 0) - z k * z j",
 "sum_ite_mul": "theorem sum_ite_mul (k : Fin d) (f : Fin d → ℝ) :\n    ∑ j, (if k = j then (1 : ℝ) else 0) * f j = f k",
 "tperp_sq": "theorem tperp_sq {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :\n    ∑ j, tperp z k j ^ 2 = 1 - z k ^ 2",
 "tperp_le_one": "theorem tperp_le_one {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :\n    ∑ j, tperp z k j ^ 2 ≤ 1",
 "tperp_dot_z": "theorem tperp_dot_z {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) :\n    ∑ j, z j * tperp z k j = 0",
 "tperp_mem": "theorem tperp_mem {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (k : Fin d) : tperp z k ∈ eball d",
 "lift_tperp": "theorem lift_tperp (z : Fin d → ℝ) (k : Fin d) :\n    lift (tperp z k) = bvec k.succ - z k • lift z",
 "exists_tperp_ne_zero": "theorem exists_tperp_ne_zero {z : Fin d → ℝ} (hz : ∑ j, z j ^ 2 = 1) (hd : 2 ≤ d) :\n    ∃ l, tperp z l ≠ 0",
 "dot_hom_hom_zero": "theorem dot_hom_hom_zero (x : Fin d → ℝ) : ∑ μ, hom x μ * hom (0 : Fin d → ℝ) μ = 1",
 "sum_bvec_mul": "theorem sum_bvec_mul (μ : Fin (d + 1)) (g : HVec d) : ∑ μ', bvec μ μ' * g μ' = g μ",
 "pairVal_bvec": "theorem pairVal_bvec (μ : Fin (d + 1)) (b : HVec d) (ω : W d) :\n    pairVal (bvec μ) b ω = ∑ ν, ω μ ν * b ν",
 "sum_row_hom_zero": "theorem sum_row_hom_zero (ω : W d) (μ : Fin (d + 1)) :\n    ∑ ν, ω μ ν * hom (0 : Fin d → ℝ) ν = ω μ 0",
 "tens_ne_zero": "theorem tens_ne_zero {X Y : HVec d} (hX : X ≠ 0) (hY : Y ≠ 0) : tens X Y ≠ 0",
 "pairVal_sub_left": "theorem pairVal_sub_left (a a' b : HVec d) (ω : W d) :\n    pairVal (a - a') b ω = pairVal a b ω - pairVal a' b ω",
 "blockData_of_orthonormal": "theorem blockData_of_orthonormal {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (hd : 2 ≤ d)\n    {q : ℕ} (v : Fin q → HVec d) (hvS : ∀ r, v r ∈ tangentSpace N)\n    (hvv : ∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0)\n    (hspan : ∀ u ∈ tangentSpace N, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0) : BlockData q",
 "blockData_of_nativeGate": "theorem blockData_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    BlockData (tangentPlus N)",
 "pos_of_isNot": "theorem pos_of_isNot {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) : 0 < d",
 "dim_of_nativeGate": "theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    d = 1 ∨ d = 3",
 "ne_five_of_nativeGate": "theorem ne_five_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 5",
 "ne_seven_of_nativeGate": "theorem ne_seven_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 7",
 "three_of_nativeGate": "theorem three_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    (hE : Entangling (eball d) G) : d = 3",
 "cnot1Fun": "def cnot1Fun (ω : W 1) : W 1 := fun μ ν => ω (μ + ν) ν",
 "add_add_self_fin2": "theorem add_add_self_fin2 : ∀ μ ν : Fin 2, μ + ν + ν = μ",
 "cnot1": "def cnot1 : W 1 ≃ₗ[ℝ] W 1 where\n  toFun := cnot1Fun\n  invFun := cnot1Fun\n  map_add' ω₁ ω₂ := by funext μ ν; rfl\n  map_smul' c ω := by funext μ ν; rfl\n  left_inv ω := by\n    funext μ ν\n    show ω (μ + ν + ν) ν = ω μ ν\n    rw [add_add_self_fin2]\n  right_inv ω := by\n    funext μ ν\n    show ω (μ + ν + ν) ν = ω μ ν\n    rw [add_add_self_fin2]",
 "cnot1_apply": "theorem cnot1_apply (ω : W 1) (μ ν : Fin 2) : cnot1 ω μ ν = ω (μ + ν) ν",
 "z1": "def z1 : Fin 1 → ℝ := fun _ => 1",
 "neg1": "def neg1 : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ) := -LinearMap.id",
 "neg1_apply": "theorem neg1_apply (x : Fin 1 → ℝ) (i : Fin 1) : neg1 x i = -x i",
 "z1_zero": "@[simp] theorem z1_zero : z1 0 = 1",
 "hom_one1": "@[simp] theorem hom_one1 (x : Fin 1 → ℝ) : hom x 1 = x 0",
 "homMap_neg1_zero": "@[simp] theorem homMap_neg1_zero (v : HVec 1) : homMap neg1 v 0 = v 0",
 "homMap_neg1_one": "@[simp] theorem homMap_neg1_one (v : HVec 1) : homMap neg1 v 1 = -v 1",
 "isNot_neg1": "theorem isNot_neg1 : IsNot (eball 1) z1 neg1",
 "cnot1_frame": "theorem cnot1_frame (a b : Fin 2) :\n    cnot1 (prodState (corner z1 a) (corner z1 b)) = prodState (corner z1 a) (corner z1 (a + b))",
 "cnot1_relT": "theorem cnot1_relT (ω : W 1) : actT neg1 (cnot1 (actT neg1 ω)) = cnot1 ω",
 "cnot1_relC": "theorem cnot1_relC (ω : W 1) : actC neg1 (cnot1 (actC neg1 ω)) = actT neg1 (cnot1 ω)",
 "lor_one": "theorem lor_one {v : HVec 1} (hv : Lor v) : 0 ≤ v 0 ∧ v 1 ^ 2 ≤ v 0 ^ 2",
 "cnot1_core": "theorem cnot1_core (e0 a1 f0 b1 x y : ℝ) (he0 : 0 ≤ e0) (ha : a1 ^ 2 ≤ e0 ^ 2) (hf0 : 0 ≤ f0)\n    (hb : b1 ^ 2 ≤ f0 ^ 2) (hx : x ^ 2 ≤ 1) (hy : y ^ 2 ≤ 1) :\n    0 ≤ (e0 + a1 * x) * f0 + y * (e0 * x + a1) * b1",
 "prodEffVal_cnot1_prodState": "theorem prodEffVal_cnot1_prodState (e f : (Fin 1 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 1 → ℝ) :\n    prodEffVal e f (cnot1 (prodState x y))\n      = (ehom e 0 + ehom e 1 * x 0) * ehom f 0 + y 0 * (ehom e 0 * x 0 + ehom e 1) * ehom f 1",
 "cnot1_prodState_mem_maxCone": "theorem cnot1_prodState_mem_maxCone {x y : Fin 1 → ℝ} (hx : x ∈ eball 1) (hy : y ∈ eball 1) :\n    cnot1 (prodState x y) ∈ maxCone (eball 1)",
 "nativeGate_cnot1": "theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1",
 "not_entangling_cnot1": "theorem not_entangling_cnot1 : ¬ Entangling (eball 1) cnot1",
 "not_product_cnot1_mixed": "theorem not_product_cnot1_mixed : ¬ IsProduct (eball 1) (cnot1 (prodState 0 z1))",
 "no_gate_four": "theorem no_gate_four : ¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ))\n    (G : W 4 ≃ₗ[ℝ] W 4), IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G",
 "dim1_core": "theorem dim1_core :\n    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n      IsNot (eball d) z N → NativeGate (eball d) z N G → ¬ Even d) ∧\n    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n      IsNot (eball d) z N → NativeGate (eball d) z N G → d = 1 ∨ d = 3) ∧\n    (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n      IsNot (eball d) z N → NativeGate (eball d) z N G → Entangling (eball d) G → d = 3) ∧\n    (IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot ∧ Entangling (eball 3) cnot) ∧\n    (IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧\n      ¬ Entangling (eball 1) cnot1 ∧ ¬ IsProduct (eball 1) (cnot1 (prodState 0 z1))) ∧\n    ¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ)) (G : W 4 ≃ₗ[ℝ] W 4),\n      IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G"
}''')
PRINTS = json.loads(r'''[
 "OIBridge.CompositeDimension.isNot_nflip",
 "OIBridge.CompositeDimension.cnot_frame",
 "OIBridge.CompositeDimension.cnot_relT",
 "OIBridge.CompositeDimension.cnot_relC",
 "OIBridge.CompositeDimension.lor_ehom",
 "OIBridge.CompositeDimension.isEffectOn_affOf",
 "OIBridge.CompositeDimension.lor_toOp_of_maxCone",
 "OIBridge.CompositeDimension.cnot_core",
 "OIBridge.CompositeDimension.cnot_prodEffVal_nonneg",
 "OIBridge.CompositeDimension.nativeGate_cnot",
 "OIBridge.CompositeDimension.extreme_of_unit",
 "OIBridge.CompositeDimension.phiW_not_product",
 "OIBridge.CompositeDimension.phiW_mem_jointStates",
 "OIBridge.CompositeDimension.lor_ray",
 "OIBridge.CompositeDimension.phiW_eq_of_segment",
 "OIBridge.CompositeDimension.entangling_cnot",
 "OIBridge.CompositeDimension.eq_corner_of_extreme",
 "OIBridge.CompositeDimension.not_entangling_one",
 "OIBridge.CompositeDimension.isNot_neg1",
 "OIBridge.CompositeDimension.nativeGate_cnot1",
 "OIBridge.CompositeDimension.not_entangling_cnot1",
 "OIBridge.CompositeDimension.not_product_cnot1_mixed",
 "OIBridge.CompositeDimension.no_gate_four",
 "OIBridge.CompositeDimension.dim1_core",
 "OIBridge.CompositeDimension.ehom_dot",
 "OIBridge.CompositeDimension.homMap_homMap",
 "OIBridge.CompositeDimension.finrank_ker_sub_add_finrank_ker_add",
 "OIBridge.CompositeDimension.finrank_plus_add_finrank_minus",
 "OIBridge.CompositeDimension.one_le_finrank_plusSpace",
 "OIBridge.CompositeDimension.one_le_finrank_minusSpace",
 "OIBridge.CompositeDimension.not_even_of_balanced",
 "OIBridge.CompositeDimension.split_of_balanced",
 "OIBridge.CompositeDimension.sumsq_apply_eq",
 "OIBridge.CompositeDimension.homMap_dot",
 "OIBridge.CompositeDimension.toOp_actC",
 "OIBridge.CompositeDimension.toOp_actT",
 "OIBridge.CompositeDimension.opGate_comp_homMap",
 "OIBridge.CompositeDimension.opGate_homMap_comp",
 "OIBridge.CompositeDimension.Lop_anti",
 "OIBridge.CompositeDimension.Lop_injective",
 "OIBridge.CompositeDimension.finrank_ker_eq_of_pointwise",
 "OIBridge.CompositeDimension.finrank_plus_eq_finrank_minus",
 "OIBridge.CompositeDimension.not_even_of_nativeGate",
 "OIBridge.CompositeDimension.ne_two_of_nativeGate",
 "OIBridge.CompositeDimension.ne_four_of_nativeGate",
 "OIBridge.CompositeDimension.p_le_one_of_blockData",
 "OIBridge.CompositeDimension.ne_five_of_nativeGate",
 "OIBridge.CompositeDimension.ne_seven_of_nativeGate",
 "OIBridge.CompositeDimension.tens_mem_maxCone",
 "OIBridge.CompositeDimension.linearMap_eq_zero_of_nonneg_lor",
 "OIBridge.CompositeDimension.linearMap_eq_zero_of_lor",
 "OIBridge.CompositeDimension.lor_face",
 "OIBridge.CompositeDimension.corner_form",
 "OIBridge.CompositeDimension.gate_corner",
 "OIBridge.CompositeDimension.gate_corner_symm",
 "OIBridge.CompositeDimension.Mfwd_Minv",
 "OIBridge.CompositeDimension.Minv_Mfwd",
 "OIBridge.CompositeDimension.lor_Minv",
 "OIBridge.CompositeDimension.Mfwd_homMap",
 "OIBridge.CompositeDimension.Minv_homMap",
 "OIBridge.CompositeDimension.gate_corner_neg",
 "OIBridge.CompositeDimension.gt_corner",
 "OIBridge.CompositeDimension.gt_corner_neg",
 "OIBridge.CompositeDimension.gt_center",
 "OIBridge.CompositeDimension.eq_zero_of_quadratic_nonneg",
 "OIBridge.CompositeDimension.lor_curve",
 "OIBridge.CompositeDimension.tangent_vanish",
 "OIBridge.CompositeDimension.gt_tangent_corners",
 "OIBridge.CompositeDimension.gt_sphere",
 "OIBridge.CompositeDimension.gt_sphere_corner",
 "OIBridge.CompositeDimension.lor_of_dotB",
 "OIBridge.CompositeDimension.Phi_sphere",
 "OIBridge.CompositeDimension.Phi_center",
 "OIBridge.CompositeDimension.Phi_center_all",
 "OIBridge.CompositeDimension.Phi_hom_zero_eq_zero",
 "OIBridge.CompositeDimension.Phi_lift_z_eq_zero",
 "OIBridge.CompositeDimension.finrank_tangentSpace",
 "OIBridge.CompositeDimension.exists_orthonormal_basis",
 "OIBridge.CompositeDimension.tperp_sq",
 "OIBridge.CompositeDimension.tperp_dot_z",
 "OIBridge.CompositeDimension.lift_tperp",
 "OIBridge.CompositeDimension.exists_tperp_ne_zero",
 "OIBridge.CompositeDimension.blockData_of_orthonormal",
 "OIBridge.CompositeDimension.blockData_of_nativeGate",
 "OIBridge.CompositeDimension.pos_of_isNot",
 "OIBridge.CompositeDimension.dim_of_nativeGate",
 "OIBridge.CompositeDimension.three_of_nativeGate"
]''')
PREAMBLE = json.loads(r'''"import OIBridge.TransitiveBody\nimport OIBridge.NativeGateBall\nimport Mathlib.LinearAlgebra.FiniteDimensional.Lemmas\nimport Mathlib.LinearAlgebra.FreeModule.Finite.Matrix\nimport Mathlib.LinearAlgebra.Matrix.ToLin\nimport Mathlib.Analysis.InnerProductSpace.PiL2\n\nnamespace OIBridge\nnamespace CompositeDimension\n\nopen KInfFoundations TransitiveBody NativeGateBall Finset\n\nvariable {d : ℕ}\n"''')
CONTEXT = json.loads(r'''[
 "namespace OIBridge",
 "namespace CompositeDimension",
 "open KInfFoundations TransitiveBody NativeGateBall Finset",
 "variable {d : ℕ}",
 "end CompositeDimension",
 "end OIBridge"
]''')
N_PRINTS = 87

DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
FAILS, COUNT = [], [0]


def check(code, name, cond):
    COUNT[0] += 1
    print(('  PASS  ' if cond else '  FAIL  ') + code + ' ' + name, flush=True)
    if not cond:
        FAILS.append(code)


def git(*a):
    return subprocess.run(['git'] + list(a), capture_output=True, text=True)


def show(commit, path):
    r = git('show', '%s:%s' % (commit, path))
    return r.stdout if r.returncode == 0 else None


def header(text):
    i = text.find('\nimport ')
    return text[:i] if i != -1 else text


def preamble(text):
    i = text.index('\nimport ') + 1
    j = text.index('\n/-! ### §A')
    return text[i:j]


def context_lines(text):
    """Each context line with its indented continuation lines (a `variable` block spanning several lines)."""
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and line.startswith('variable'):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


def decls(text):
    return [(m.group(1), m.group(2)) for m in DECL.finditer(text)]


def stmt_end(chunk):
    """End of a theorem's statement: the first ` :=`, or a ` where` closing a line, whichever is earlier."""
    ends = [j for j in (chunk.find(' :='),) if j != -1]
    m = re.search(r' where\n', chunk)
    if m:
        ends.append(m.start())
    return min(ends) if ends else -1


def spans(text):
    """[(kind, name, start, statement end or -1, end)] for every declaration, in order."""
    out = []
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        se = -1
        if m.group(1) in ('theorem', 'lemma'):
            j = stmt_end(chunk)
            if j != -1:
                se = start + j
        out.append((m.group(1), m.group(2), start, se if se != -1 else start + len(chunk), nxt, start + len(chunk)))
    return out


def decl_chunks(text):
    """name -> (kind, statement or whole text, proof text after the statement for theorems)."""
    out = {}
    for kind, name, start, se, nxt, cend in spans(text):
        if kind in ('theorem', 'lemma'):
            out[name] = (kind, text[start:se], text[se:nxt])
        else:
            out[name] = (kind, text[start:cend], '')
    return out


def colon_index(stmt):
    """Index of the colon separating binders from the conclusion: the first at bracket depth 0 after the name."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in '({[⦃':
            depth += 1
        elif c in ')}]⦄':
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return j
    return -1


def split_statement(stmt):
    """(binders, conclusion) of a declaration header."""
    m = DECL.match(stmt)
    i = m.end() if m else 0
    j = colon_index(stmt)
    if j == -1:
        return stmt[i:], ''
    return stmt[i:j], stmt[j + 1:]


def def_header(text):
    """A definition's header: up to ` :=` or a ` where` closing a line."""
    j = stmt_end(text)
    return text[:j] if j != -1 else text


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def norm(s):
    return ' '.join(s.split())


def fields(structure_text):
    """The field names of a structure chunk: the two-space-indented `name :` lines after `where`."""
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    return [m.group(1) for m in re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M)]


def field_line(structure_text, name):
    body = structure_text.split(' where', 1)[1] if ' where' in structure_text else ''
    ms = list(re.finditer(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M))
    for k, m in enumerate(ms):
        if m.group(1) == name:
            return norm(body[m.start():ms[k + 1].start() if k + 1 < len(ms) else len(body)])
    return None


def token(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def sections(text):
    """[(position, label)] of the section markers, label `§A` ... or `verdict`."""
    out = []
    for m in re.finditer(r'^/-! ### (§[A-Z]|The verdict)', text, re.M):
        out.append((m.start(), 'verdict' if m.group(1) == 'The verdict' else m.group(1)))
    return out


def section_at(secs, pos):
    lab = None
    for p, l in secs:
        if p <= pos:
            lab = l
    return lab


PREFIX = 'OIBridge.CompositeDimension.'
# S1 -- the public selector boundary
SEL_BINDERS = ('{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
               '(hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)')
SELECTORS = {
    'dim_of_nativeGate': (SEL_BINDERS, 'd = 1 ∨ d = 3'),
    'three_of_nativeGate': (SEL_BINDERS + ' (hE : Entangling (eball d) G)', 'd = 3'),
    'ne_five_of_nativeGate': (SEL_BINDERS, 'd ≠ 5'),
    'ne_seven_of_nativeGate': (SEL_BINDERS, 'd ≠ 7'),
}
CORE_CLAUSES = ('IsNot (eball d) z N → NativeGate (eball d) z N G → d = 1 ∨ d = 3)',
                'IsNot (eball d) z N → NativeGate (eball d) z N G → Entangling (eball d) G → d = 3)')
TWO_LE_D = re.compile(r'2\s*≤\s*d(?![\w\'])|(?<![\w\'])d\s*≥\s*2|1\s*<\s*d(?![\w\'])|(?<![\w\'])d\s*>\s*1')
# S2 -- the internal block-reduction chain
TWO_LE_D_ONLY = ['blockData_of_nativeGate', 'blockData_of_orthonormal', 'exists_tperp_ne_zero']
BLOCKDATA_ONLY = ['BlockData', 'blockData_of_nativeGate', 'blockData_of_orthonormal', 'p_le_one_of_blockData']
# S3 -- the frozen hypotheses
ISNOT_BINDERS = '(Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))'
ISNOT_FIELDS = ['unit', 'invol', 'preserves', 'flips']
GATE_BINDERS = ('(Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) '
                '(G : W d ≃ₗ[ℝ] W d)')
GATE_FIELDS = ['frame', 'posFwd', 'posInv', 'relT', 'relC']
REL_T = 'relT : ∀ ω, actT N (G (actT N ω)) = G ω'
REL_C = 'relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)'
POS_FWD = 'posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω'
POS_INV = 'posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω'
MAXCONE_BODY = '{ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}'
FROZEN_WHOLE = ['IsNot', 'NativeGate', 'Entangling', 'maxCone', 'jointStates', 'W', 'prodState', 'actT', 'actC']
# S4 -- premises concluded only by the named witnesses
PREMISES = ('IsNot', 'NativeGate', 'Entangling')
WITNESSES = {
    'isNot_nflip': 'IsNot (eball 3) z3 nflip',
    'nativeGate_cnot': 'NativeGate (eball 3) z3 nflip cnot',
    'entangling_cnot': 'Entangling (eball 3) cnot',
    'isNot_neg1': 'IsNot (eball 1) z1 neg1',
    'nativeGate_cnot1': 'NativeGate (eball 1) z1 neg1 cnot1',
}
CORE_INSTANCES = ('IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot ∧ Entangling (eball 3) cnot',
                  'IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧')
CORE_ANTECEDENTS = ('IsNot (eball d) z N → NativeGate (eball d) z N G →', 'Entangling (eball d) G →')
NEGATED = ('¬ Entangling (eball 1) G', '¬ Entangling (eball 1) cnot1',
           '¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ)) (G : W 4 ≃ₗ[ℝ] W 4), '
           'IsNot (eball 4) z N ∧ NativeGate (eball 4) z N G')
# S5 -- reuse, not re-proof
REUSED = ('eball', 'mem_eball', 'IsEffectOn')
CITED = ('NativeGateBall.parity', 'NativeGateBall.p_le_one', 'NativeGateBall.dim_of_bounds')
# S6 -- field-neutral
NEUTRAL_TOKENS = ('ℂ', 'Complex', 'TensorProduct', '⊗ₜ', 'kronecker', 'Kronecker', 'unitaryGroup', 'Hilbert', 'Bell')
IMPORT_OK = re.compile(r'^import (OIBridge\.TransitiveBody|OIBridge\.NativeGateBall|Mathlib\.[\w.]+)$')
D_EQUATION = re.compile(r'(?<![\w\'])d\s*[=≠<>≤≥]\s*\d|\d\s*[=≠<>≤≥]\s*d(?![\w\'])|\b(Even|Odd)\s+d(?![\w\'])')
# S7 -- phrases
PHRASES = ('OI selects', 'OI implies d', 'OI forces d', 'copy covariance derived', 'local tomography derived')
# S8 -- dimension
WITNESS_SECTIONS = ('§K', '§M', '§N', '§O', '§P', 'verdict')
COORD_HELPERS = ("sum_univ_four'", 'lor_three', 'lor_of_three')
SELECTOR_CONCLUSIONS = ('d = 1 ∨ d = 3', 'd = 3', 'd ≠ 4', 'd ≠ 5', 'd ≠ 7')
NUMERAL = re.compile(r'(?<![\w\'.])(\d+)(?![\w\'])')
DIM_TOKENS = ('ball3', 'eball_three')
# S10 -- the premise correspondence
W_SENTENCE = ('/-- The joint bilinear carrier of two copies: a real function of a control index and a target index.\n'
              'Local tomography is the premise this carrier encodes. -/\nabbrev W (d : ℕ)')
CONE_THEOREMS = {
    'lor_ehom': 'Lor (ehom e)',
    'isEffectOn_affOf': 'IsEffectOn (eball d) (affOf v)',
    'lor_toOp_of_maxCone': 'Lor (toOp ω f)',
}
NO_LOR = ['IsNot', 'NativeGate', 'Entangling', 'maxCone', 'jointStates']


def numerals(text):
    return [n for n in NUMERAL.findall(code_only(text)) if int(n) in (3, 4, 5, 7)]


def dimension_violations(mod):
    """Outside the witness and control sections and the verdict: every numeral 3, 4, 5 or 7, except in a selector
    conclusion of the frozen list or in a named coordinate helper."""
    secs = sections(mod)
    sp = spans(mod)
    bad = []
    first = sp[0][2] if sp else len(mod)
    if numerals(mod[:first]):
        bad.append('preamble')
    for kind, name, start, se, nxt, cend in sp:
        if section_at(secs, start) in WITNESS_SECTIONS or name in COORD_HELPERS:
            continue
        if kind in ('theorem', 'lemma'):
            stmt = mod[start:se]
            c = colon_index(stmt)
            binders, concl = stmt[:c + 1], stmt[c + 1:]
            if numerals(binders) or numerals(mod[se:nxt]):
                bad.append(name)
            elif numerals(concl) and norm(concl) not in SELECTOR_CONCLUSIONS:
                bad.append(name)
        elif numerals(mod[start:nxt]):
            bad.append(name)
    return bad


def semantic_checks(mod, chunks, prints, tag):
    kinds = {n: k for n, (k, _, _) in chunks.items()}
    texts = {n: c for n, (_, c, _) in chunks.items()}
    proofs = {n: p for n, (_, _, p) in chunks.items()}
    code = code_only(mod)
    # S1
    bad1 = []
    for n, (b, c) in SELECTORS.items():
        bb, cc = split_statement(texts.get(n, ''))
        if kinds.get(n) != 'theorem' or norm(bb) != b or norm(cc) != c or PREFIX + n not in prints:
            bad1.append(n)
    core = norm(texts.get('dim1_core', ''))
    for n in list(SELECTORS) + ['dim1_core']:
        if 'BlockData' in texts.get(n, '') or TWO_LE_D.search(texts.get(n, '')):
            bad1.append(n)
    check('S1', 'the selectors carry exactly the frozen binders and conclusions, free of BlockData and 2 ≤ d; '
                'Entangling only in three_of_nativeGate%s%s' % (tag, (' %s' % bad1[:3]) if bad1 else ''),
          not bad1 and 'Entangling' not in texts.get('dim_of_nativeGate', 'Entangling')
          and 'Entangling (eball d) G' in texts.get('three_of_nativeGate', '')
          and all(c in core for c in CORE_CLAUSES) and PREFIX + 'dim1_core' in prints)
    # S2
    two = sorted(n for n, t in texts.items() if TWO_LE_D.search(code_only(t)))
    bd = sorted(n for n in texts if token('BlockData', code_only(texts[n] + proofs[n])))
    bd_total = len(re.findall(r'(?<![\w.\'])BlockData(?![\w\'])', code))
    bd_listed = sum(len(re.findall(r'(?<![\w.\'])BlockData(?![\w\'])', code_only(texts[n] + proofs[n])))
                    for n in bd)
    check('S2', '`2 ≤ d` only in the three block-reduction statements; BlockData only in its four declarations and '
                'frozen whole%s%s' % (tag, (' %s %s' % (two, bd)) if two != TWO_LE_D_ONLY
                                      or bd != BLOCKDATA_ONLY else ''),
          two == TWO_LE_D_ONLY and bd == BLOCKDATA_ONLY and bd_total == bd_listed
          and kinds.get('BlockData') == 'structure' and texts.get('BlockData') == TEXTS['BlockData'])
    # S3
    isnot, gate = texts.get('IsNot', ''), texts.get('NativeGate', '')
    lin = [n for n in re.findall(r'\((\w+) : \(Fin d → ℝ\) →ₗ\[ℝ\]', def_header(gate))]
    check('S3', 'IsNot and NativeGate with their frozen binders and fields and one bound N; the frozen definitions '
                'whole; maxCone over every effect' + tag,
          kinds.get('IsNot') == 'structure' and kinds.get('NativeGate') == 'structure'
          and norm(split_statement(def_header(isnot))[0]) == ISNOT_BINDERS and fields(isnot) == ISNOT_FIELDS
          and norm(split_statement(def_header(gate))[0]) == GATE_BINDERS and fields(gate) == GATE_FIELDS
          and lin == ['N'] and field_line(gate, 'relT') == REL_T and field_line(gate, 'relC') == REL_C
          and field_line(gate, 'posFwd') == POS_FWD and field_line(gate, 'posInv') == POS_INV
          and all(texts.get(n) == TEXTS[n] for n in FROZEN_WHOLE)
          and norm(texts.get('maxCone', '')).endswith(':= ' + MAXCONE_BODY))
    # S4
    bad4 = []
    for n, (k, t, _) in chunks.items():
        if k == 'structure':
            continue
        if k in ('theorem', 'lemma'):
            concl = norm(split_statement(t)[1])
        else:
            concl = norm(split_statement(def_header(t))[1])
        if n in WITNESSES:
            if concl != WITNESSES[n] or kinds.get(n) != 'theorem' or PREFIX + n not in prints:
                bad4.append(n)
            continue
        if n == 'dim1_core':
            if not all(c in concl for c in CORE_INSTANCES):
                bad4.append(n)
            for c in CORE_INSTANCES + CORE_ANTECEDENTS:
                concl = concl.replace(c, '')
        for c in NEGATED:
            concl = concl.replace(c, '')
        if any(token(p, concl) for p in PREMISES):
            bad4.append(n)
    check('S4', 'IsNot, NativeGate and Entangling concluded only by the five named witnesses and the verdict\'s '
                'instance clauses%s%s' % (tag, (' %s' % bad4[:3]) if bad4 else ''), not bad4)
    # S5
    local = {n for _, n in decls(mod)}
    clash = sorted(local & (set(NGB_NAMES) | set(REUSED)))
    check('S5', 'NativeGateBall reused, not re-proved: no local name of NativeGateBall, eball, mem_eball or '
                'IsEffectOn; parity, p_le_one and dim_of_bounds cited%s%s' % (tag, (' %s' % clash) if clash else ''),
          not clash and all(c in code for c in CITED) and 'import OIBridge.NativeGateBall' in mod)
    # S6
    hits = [t for t in NEUTRAL_TOKENS if t in mod]
    imports = re.findall(r'^import .*$', mod, re.M)
    bad_imp = [l for l in imports if not IMPORT_OK.match(l)]
    iff = [n for n, t in texts.items() if '↔' in t and D_EQUATION.search(code_only(t))]
    check('S6', 'field-neutral: no complex, tensor, Kronecker, unitary-group, Hilbert or Bell token; imports '
                'whitelisted; no ↔ with an equation in d%s%s' % (tag, (' %s' % (hits + bad_imp + iff)[:3])
                                                               if hits or bad_imp or iff else ''),
          not hits and not bad_imp and bool(imports) and not iff)
    # S7
    ph = phrase_hits(header(mod))
    check('S7', 'the header carries none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''), not ph)
    # S8
    bad8 = dimension_violations(mod)
    dt = [t for t in DIM_TOKENS if token(t, code)]
    check('S8', 'outside the witness and control sections a numeral 3, 4, 5 or 7 only in a selector conclusion or a '
                'named coordinate helper; no ball3 token%s%s' % (tag, (' %s' % (bad8 + dt)[:3]) if bad8 or dt else ''),
          not bad8 and not dt)
    # S9
    names = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
    check('S9', 'exactly the %d frozen #print axioms lines, distinct, each naming a declaration of the module%s'
          % (N_PRINTS, tag),
          len(PRINTS) == N_PRINTS and prints == PRINTS and len(set(prints)) == N_PRINTS and len(names) == N_PRINTS
          and all(n in local for n in names))
    # S10
    lor = [n for n in NO_LOR if token('Lor', texts.get(n, 'Lor'))]
    check('S10', 'the carrier names local tomography as its premise; no hypothesis or cone definition mentions Lor; '
                 'the cone theorems proved with prints%s%s' % (tag, (' %s' % lor) if lor else ''),
          W_SENTENCE in mod and not lor and not token('lt', code) and not token('LocallyTomographic', code)
          and all(kinds.get(n) == 'theorem' and norm(split_statement(texts.get(n, ''))[1]) == c
                  and PREFIX + n in prints for n, c in CONE_THEOREMS.items()))


def phrase_hits(text):
    t = norm(text).lower()
    return [p for p in PHRASES if p.lower() in t]


def module_checks(mod, tag=''):
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations' + tag, [list(x) for x in decls(mod)] == DECLS)
    check('N2', 'the preamble unchanged' + tag,
          '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE)
    check('N2', 'every context block unchanged and in order' + tag, context_lines(mod) == CONTEXT)
    chunks = decl_chunks(mod)
    texts = {n: c for n, (_, c, _) in chunks.items()}
    bad = sorted(n for n in TEXTS if texts.get(n) != TEXTS[n])
    check('N2', 'every frozen statement, definition and structure unchanged%s%s'
          % (tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
    c = code_only(mod)
    check('N3', 'no sorry, admit, axiom or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M))
    prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
    check('N3', 'every frozen #print axioms line present' + tag, all(p in prints for p in PRINTS))
    semantic_checks(mod, chunks, prints, tag)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_want(d_text):
    d = json.loads(d_text)
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['modules'] == PREV_FAMILY_MODULES]
    nb = [i for i, f in enumerate(fam) if f['modules'] == NB1_FAMILY_MODULES]
    if len(k) != 1 or len(nb) != 1 or fam[nb[0]]['note'].count(NB1_OLD) != 1:
        return None
    fam = [dict(f) for f in fam]
    fam[nb[0]]['note'] = fam[nb[0]]['note'].replace(NB1_OLD, NB1_NEW, 1)
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        want = census_want(d_text)
    except Exception:
        return False
    return want is not None and e_text == want


def roadmap_want(d_text):
    if d_text is None or any(d_text.count(old) != 1 for old, _ in ROADMAP_EDITS):
        return None
    out = d_text
    for old, new in ROADMAP_EDITS:
        out = out.replace(old, new, 1)
    return out


def roadmap_ok(d_text, e_text):
    want = roadmap_want(d_text)
    return want is not None and e_text == want


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    module_checks(show(commit, MOD))
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note)
        check('S7', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
    check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                    show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family and the frozen NB-1 sentence',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    check('R', 'ROADMAP is D\'s with exactly the two frozen K1 replacements',
          roadmap_ok(show(D, ROADMAP), show(commit, ROADMAP)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def must_fail(code, label, mod2):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mod2)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def append_decl(text, decl):
    """Insert a declaration just before the verdict section (inside §P)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_before(text, anchor, decl):
    i = text.index(anchor)
    return text[:i] + decl + '\n\n' + text[i:]


SEL_HEAD = ('theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
            '    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n'
            '    d = 1 ∨ d = 3 := by')
THREE_HEAD = ('    (hE : Entangling (eball d) G) : d = 3 := by')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem dim1_core :', '\ntheorem dim1_core\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed preamble',
              replace_once(mod, 'open KInfFoundations TransitiveBody NativeGateBall Finset',
                           'open KInfFoundations TransitiveBody NativeGateBall'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem tangent_vanish (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, Lor X → 0 ≤ F X)',
                           'theorem tangent_vanish (F : HVec d →ₗ[ℝ] ℝ) (hpos : ∀ X, 0 ≤ F X)'))
    must_fail('N3', 'a sorry', append_decl(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.CompositeDimension.gt_sphere\n', ''))
    # S1
    must_fail('S1', '`2 ≤ d` added to the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                           '(hG : NativeGate (eball d) z N G) (hd : 2 ≤ d) :')))
    must_fail('S1', 'a BlockData hypothesis on the entangling selector',
              replace_once(mod, THREE_HEAD,
                           '    (hE : Entangling (eball d) G) (hB : BlockData (tangentPlus N)) : d = 3 := by'))
    must_fail('S1', 'the entangling clause added to the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                           '(hG : NativeGate (eball d) z N G)\n'
                                                           '    (hE : Entangling (eball d) G) :')))
    must_fail('S1', 'the entangling clause dropped from three_of_nativeGate',
              replace_once(mod, '(hG : NativeGate (eball d) z N G)\n' + THREE_HEAD,
                           '(hG : NativeGate (eball d) z N G) :\n    d = 3 := by'))
    # S2
    must_fail('S2', '`2 ≤ d` in a sphere identity',
              replace_once(mod, 'theorem gt_sphere {z : Fin d → ℝ}', 'theorem gt_sphere (hd : 2 ≤ d) {z : Fin d → ℝ}'))
    must_fail('S2', 'BlockData used outside its four declarations',
              append_decl(mod, 'theorem blockData_zero : BlockData 0 → True := fun _ => trivial'))
    must_fail('S2', 'the nonzero entry dropped from BlockData',
              replace_once(mod, '          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) ∧\n'
                                '    (∃ r k l, A r k l ≠ 0)',
                           '          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) ∧\n'
                           '    True'))
    # S3
    must_fail('S3', 'inverse positivity removed',
              replace_once(mod, '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n', ''))
    must_fail('S3', 'a second NOT in the control relation',
              replace_once(mod, '    (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame',
                           '    (N\' : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame'))
    must_fail('S3', 'the maximal cone restricted to normalized effects',
              replace_once(mod, '  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}',
                           '  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → e 0 = 1 → 0 ≤ prodEffVal e f ω}'))
    must_fail('S3', 'the entangling clause without extremality of the image',
              replace_once(mod, '    G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬ IsProduct Ω',
                           '    G (prodState x y) ∈ jointStates Ω ∧ ¬ IsProduct Ω'))
    # S4
    must_fail('S4', 'a gate concluded for a general NOT',
              append_decl(mod, 'theorem exists_gate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
                               '    (hN : IsNot (eball d) z N) : ∃ G : W d ≃ₗ[ℝ] W d, NativeGate (eball d) z N G := '
                               'by\n  exact absurd hN (by simp)'))
    must_fail('S4', 'the entangling clause concluded from the gate',
              append_decl(mod, 'theorem entangling_of_gate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
                               '    {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate (eball d) z N G) : Entangling (eball d) G '
                               ':= by\n  exact absurd hG (by simp)'))
    must_fail('S4', 'a witness concluding a different gate',
              replace_once(mod, 'theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot where',
                           'theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot ∧ True where'))
    # S5
    must_fail('S5', 'parity re-declared locally',
              insert_before(mod, '/-- **Parity (S5) from the frozen hypotheses.**',
                            'theorem parity : True := trivial'))
    must_fail('S5', 'the NativeGateBall citation of p_le_one replaced',
              replace_once(mod, '  exact NativeGateBall.p_le_one p m A B hB hpos hne',
                           '  exact p_le_one\' p m A B hB hpos hne'))
    # S6
    must_fail('S6', 'a complex-number import',
              replace_once(mod, 'import OIBridge.NativeGateBall\n',
                           'import OIBridge.NativeGateBall\nimport Mathlib.Analysis.Complex.Basic\n'))
    must_fail('S6', 'a complex scalar',
              replace_once(mod, 'def hom (x : Fin d → ℝ)',
                           'def homC (x : Fin d → ℂ) : Fin d → ℂ := x\n\ndef hom (x : Fin d → ℝ)'))
    must_fail('S6', 'the selector stated as an equivalence',
              append_decl(mod, 'theorem dim_iff {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
                               '    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) :\n'
                               '    NativeGate (eball d) z N G ↔ d = 3 := by\n  exact absurd hN (by simp)'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  Proved here:\n', '  OI selects the dimension.\n\n  Proved here:\n'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('Two identical copies of the ball with a native gate have d = 1 or d = 3.')
          and phrase_hits('The round shows that OI forces\nd = 3.') == ['OI forces d'])
    # S8
    must_fail('S8', 'a dimension hypothesis in a block-reduction lemma',
              replace_once(mod, 'theorem tangent_vanish (F : HVec d →ₗ[ℝ] ℝ)',
                           'theorem tangent_vanish (h3 : d = 3) (F : HVec d →ₗ[ℝ] ℝ)'))
    must_fail('S8', 'a coordinate index type in the eigenspace adapter',
              replace_once(mod, 'theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) '
                                ': ¬ Even d',
                           'theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) '
                           '(f : Fin 4 → ℝ) : ¬ Even d'))
    must_fail('S8', 'a widened selector conclusion',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('d = 1 ∨ d = 3 := by', 'd = 1 ∨ d = 3 ∨ d = 5 := by')))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.CompositeDimension.dim1_core\n',
                           '#print axioms OIBridge.CompositeDimension.dim1_core\n'
                           '#print axioms OIBridge.CompositeDimension.hom_zero\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.CompositeDimension.three_of_nativeGate',
                           '#print axioms OIBridge.CompositeDimension.three_of_nativeGate\n'
                           '#print axioms OIBridge.CompositeDimension.three_of_nativeGate'))
    # S10
    must_fail('S10', 'the carrier\'s local-tomography sentence removed',
              replace_once(mod, 'Local tomography is the premise this carrier encodes. -/\nabbrev W',
                           '-/\nabbrev W'))
    must_fail('S10', 'the effect cone assumed in place of the full effects',
              replace_once(mod, '  {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω}',
                           '  {ω | ∀ a b : HVec d, Lor a → Lor b → 0 ≤ pairVal a b ω}'))
    # I, C, R
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    fam_only = dict(dd)
    fam_only['families'] = dd['families'][:k + 1] + [CENSUS_FAMILY] + dd['families'][k + 1:]
    fam_only = json.dumps(fam_only, indent=2, ensure_ascii=False) + '\n'
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; the family without the NB-1 sentence, a changed status and a moved '
               'family fail',
          census_ok(d_cen, good) and not census_ok(d_cen, fam_only) and not census_ok(d_cen, bad_status)
          and moved != good and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1)))
    d_rm = show(D, ROADMAP)
    good_rm = roadmap_want(d_rm)
    one_only = d_rm.replace(ROADMAP_EDITS[0][0], ROADMAP_EDITS[0][1], 1)
    extra = good_rm.replace('- **K2 — the composite. OPEN.**', '- **K2 — the composite. CONDITIONAL.**', 1)
    check('M', 'roadmap: the frozen edit passes; one replacement alone and an extra edited row fail',
          good_rm is not None and roadmap_ok(d_rm, good_rm) and not roadmap_ok(d_rm, one_only)
          and extra != good_rm and not roadmap_ok(d_rm, extra) and not roadmap_ok(d_rm, d_rm))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
