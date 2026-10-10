#!/usr/bin/env python3
"""controls.py -- round RELC-SELECT-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F, and F = D plus the preregistration alone)
  controls.py --self-test                   the frozen surfaces against the reference modules; mutation controls that
                                            must fail with their named codes
  controls.py verdict <commit>              the four cells computed from the modules' statements at <commit> and the
                                            landed statements at D

Checks (each prints PASS or FAIL with its code):
  P   paths       delta(D, commit) is exactly the governed execution paths plus the record directory
  L   landed      the landed texts the rules read, read from D, are the frozen ones
  N1  decls       each module declares exactly its frozen declarations, in order, with their kinds
  N2  statements  every theorem statement (signature up to `:=`) is the frozen text; every definition and structure
                  is the frozen text whole; the preamble and every context block is the frozen text, in order -- a
                  proof may change, a statement, definition or binder context may not
  N3  hygiene     no sorry, admit, axiom declaration or native_decide; every frozen `#print axioms` line present
  S1  parity      (RelcSelectParity) from `IsNot (eball d) z N` and the landed `relC` field alone, the two eigenspaces
                  of the homogenized NOT have equal dimension and `d` is not even; the module reads neither `relT`, the
                  frame, positivity, `GateRel` nor any landed statement over `NativeGate`
  S2  selector    (RelcSelectBlock) `CtrlGate` is the landed `NativeGate` with its `relT` field removed, field for
                  field; `IsNot` and `CtrlGate` give the landed selector's conclusion `d = 1 ∨ d = 3`, and with the
                  landed `Entangling` clause `d = 3` through the frame-only exclusion of `d = 1`; every copied
                  declaration is the landed one under the frozen renaming, except the two frozen line edits; the
                  parity step is S1's theorem; nothing in the module or in the parity module reads `relT`
  S3  positivity  (RelcSelectSqueeze) at `d = 5` with the landed `n5` and `z5`: `gSq` has the landed frame, `GateRel`
                  and the landed `posFwd` field and fails the landed `posInv` field through the value `-1 / 2`;
                  `gSq.symm` has the frame, `GateRel`, the landed `posInv` field (stated through
                  `gSq.symm.symm = gSq`) and fails the landed `posFwd` field; the transfer of `relC` to the inverse
                  takes `relT`
  S4  relation    (RelcSelectC5) at `d = 5` with the witness NOT `nC5` and the landed `z5`: `gC5` has the landed
                  frame, `relT`, `posFwd` and `posInv` fields and fails the landed `relC` field, so `IsNot` and those
                  four fields do not give the landed selector's conclusion
  S6  scope       no declaration mentions a complex field or a landed dimension selector of the native gate; only the
                  frozen selector theorems conclude an equation on `d`; no theorem concludes the native gate
  S7  reuse       no declaration shares its name with an OIBridge declaration visible to it or with a declaration of
                  another module of the round; each module's imports are the frozen ones
  S8  phrases     the comments of each module (and, at a commit carrying it, the result note less the frozen earned
                  reading and the frozen non-inference rule) contain none of the frozen phrases
  S9  count       exactly the frozen `#print axioms` lines of each module, in order, distinct, each naming a
                  declaration of that module
  V   verdicts    each cell is computed from the modules' statements and the landed statements at D by its own frozen
                  rule; at a commit carrying the result note, the note states exactly the computed tokens and no
                  other, states the frozen earned reading exactly when all four cells are proved, and states the
                  frozen non-inference rule
  I   imports     OIBridge.lean is D's with exactly the four frozen import lines after `import OIBridge.OddChar`
  C   census      the census is D's with exactly the frozen family inserted after the ODD-CHAR-1 family, byte for byte
  F   freeze      (with --freeze) the preregistration at the commit equals F's, and delta(D, F) is the preregistration
"""
import hashlib, io, json, re, subprocess, sys

D = 'e2426ba4109dcd719d518aefbd3c417b7c6fdc5b'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-relc-select-1/'
PREREG = RDIR + 'preregistration.md'
RESULT = RDIR + 'result.md'
LEAN = 'verification/lean-mathlib/OIBridge/'
MODULES = ['RelcSelectParity', 'RelcSelectBlock', 'RelcSelectSqueeze', 'RelcSelectC5']
MODPATH = {m: LEAN + m + '.lean' for m in MODULES}
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
GOVERNED = dict([(MODPATH[m], 'A') for m in MODULES] + [(IMPORTS, 'M'), (CENSUS, 'M')])
RECORD_FILES = {RDIR + 'preregistration.md', RDIR + 'controls.py', RDIR + 'result.md'}
MOD_REFERENCE_BLOBS = json.loads(r'''{
 "RelcSelectParity": "40cdd044094a5886d916c2c1a8847ff2066433d8",
 "RelcSelectBlock": "4db61452136745e536803f1d6f5789772db3fb50",
 "RelcSelectSqueeze": "ed994d18e322ef61015cba0e7dc3715316b009d6",
 "RelcSelectC5": "4ba97ee39c522faf6cc39ccca9f1c09dbcf0b9a6"
}''')
ANCHOR_IMPORT = 'import OIBridge.OddChar\n'
NEW_IMPORTS = ''.join('import OIBridge.%s\n' % m for m in MODULES)
PREV_FAMILY_MODULES = ['OddChar']
CENSUS_FAMILY = json.loads(r'''{
 "name": "DIM-1's dimension selector without the target relation: the control relation alone forces odd dimension; the frame, both positivity clauses and the control relation give d = 1 or d = 3; and at d = 5 explicit countermodels show that neither positivity clause can be dropped and that the target relation does not replace the control relation (round RELC-SELECT-1, reconstruction)",
 "modules": [
  "RelcSelectParity",
  "RelcSelectBlock",
  "RelcSelectSqueeze",
  "RelcSelectC5"
 ],
 "status": "kernel-only",
 "manuscript": [],
 "note": "Round RELC-SELECT-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-relc-select-1/preregistration.md. Q-PAR: from IsNot (eball d) z N and the control relation alone, the two homogenized eigenspaces of N have equal dimension and d is not even (finrank_plus_eq_finrank_minus_relC, not_even_of_relC). Q-SEL: CtrlGate, NativeGate's frame, two positivity clauses and control relation without its target relation, gives d = 1 ∨ d = 3 with IsNot and d = 3 with Entangling (dim_of_ctrlGate, three_of_ctrlGate), through DIM-1's block reduction restated over CtrlGate with its one target-relation step replaced by actT_slice_ctrl. Q-POS: at d = 5 with PARITY-NOT-1's n5, the squeezed gate gSq has the frame, GateRel and forward positivity and fails inverse positivity, and its inverse has the frame, GateRel and inverse positivity and fails forward positivity (gSq_sep, gSqInv_sep). Q-REL: at d = 5 the witness NOT nC5 and NB-1's J/K map gC5 have the frame, the target relation and both positivity clauses and fail the control relation (c5_sep), so those clauses with IsNot do not give d = 1 ∨ d = 3 (relT_not_dimension_selecting). Carried by no manuscript. CtrlGate is the selector's hypothesis only; NativeGate and GateRel are unchanged and the target relation remains a field of both; the transfer of the control relation to an inverse reads the target relation; the frame is not audited."
}''')
DECLS = json.loads(r'''{
 "RelcSelectParity": [
  [
   "noncomputable def",
   "relCLeft"
  ],
  [
   "noncomputable def",
   "relCConj"
  ],
  [
   "theorem",
   "relCLeft_apply"
  ],
  [
   "theorem",
   "relCConj_apply"
  ],
  [
   "theorem",
   "relCLeft_eq"
  ],
  [
   "theorem",
   "relCConj_eq"
  ],
  [
   "theorem",
   "opGate_homMap_comp_relC"
  ],
  [
   "theorem",
   "opGate_injective_relC"
  ],
  [
   "theorem",
   "finrank_ker_sub_le_relC"
  ],
  [
   "theorem",
   "finrank_ker_add_le_relC"
  ],
  [
   "theorem",
   "finrank_ker_relCLeft_sub"
  ],
  [
   "theorem",
   "finrank_ker_relCLeft_add"
  ],
  [
   "theorem",
   "eq_zero_of_plus_minus_relC"
  ],
  [
   "theorem",
   "homMap_comm_relC"
  ],
  [
   "theorem",
   "homMap_anticomm_relC"
  ],
  [
   "theorem",
   "mem_plusSpace_of_comm_relC"
  ],
  [
   "theorem",
   "mem_minusSpace_of_comm_relC"
  ],
  [
   "theorem",
   "mem_minusSpace_of_anticomm_relC"
  ],
  [
   "theorem",
   "mem_plusSpace_of_anticomm_relC"
  ],
  [
   "noncomputable def",
   "relCSplitEven"
  ],
  [
   "noncomputable def",
   "relCSplitOdd"
  ],
  [
   "theorem",
   "relCSplitEven_injective"
  ],
  [
   "theorem",
   "relCSplitOdd_injective"
  ],
  [
   "theorem",
   "finrank_ker_relCConj_sub_le"
  ],
  [
   "theorem",
   "finrank_ker_relCConj_add_le"
  ],
  [
   "theorem",
   "balance_of_bounds_relC"
  ],
  [
   "theorem",
   "finrank_plus_eq_finrank_minus_relC"
  ],
  [
   "theorem",
   "not_even_of_relC"
  ]
 ],
 "RelcSelectBlock": [
  [
   "structure",
   "CtrlGate"
  ],
  [
   "theorem",
   "ctrlGate_of_nativeGate"
  ],
  [
   "theorem",
   "gate_corner_ctrl"
  ],
  [
   "theorem",
   "gate_corner_symm_ctrl"
  ],
  [
   "theorem",
   "Mfwd_Minv_ctrl"
  ],
  [
   "theorem",
   "lor_Minv_ctrl"
  ],
  [
   "theorem",
   "gate_actC_ctrl"
  ],
  [
   "theorem",
   "gate_corner_neg_ctrl"
  ],
  [
   "theorem",
   "gt_corner_ctrl"
  ],
  [
   "theorem",
   "gt_corner_neg_ctrl"
  ],
  [
   "theorem",
   "gt_center_ctrl"
  ],
  [
   "theorem",
   "gt_tangent_corners_ctrl"
  ],
  [
   "theorem",
   "gt_sphere_ctrl"
  ],
  [
   "theorem",
   "gt_sphere_corner_ctrl"
  ],
  [
   "theorem",
   "Phi_sphere_ctrl"
  ],
  [
   "theorem",
   "Phi_center_ctrl"
  ],
  [
   "theorem",
   "Phi_center_all_ctrl"
  ],
  [
   "theorem",
   "Phi_hom_zero_eq_zero_ctrl"
  ],
  [
   "theorem",
   "Phi_lift_z_eq_zero_ctrl"
  ],
  [
   "theorem",
   "gt_center_two_ctrl"
  ],
  [
   "theorem",
   "phi_lift_minus_ctrl"
  ],
  [
   "theorem",
   "phi_bvec_minus_unit_ctrl"
  ],
  [
   "theorem",
   "phi_minusSpace_ctrl"
  ],
  [
   "theorem",
   "homMap_eq_self_of_orth_minusSpace"
  ],
  [
   "theorem",
   "actT_slice_ctrl"
  ],
  [
   "theorem",
   "blockData_of_orthonormal_ctrl"
  ],
  [
   "theorem",
   "blockData_of_ctrlGate"
  ],
  [
   "theorem",
   "not_entangling_one_ctrl"
  ],
  [
   "theorem",
   "dim_of_ctrlGate"
  ],
  [
   "theorem",
   "three_of_ctrlGate"
  ]
 ],
 "RelcSelectSqueeze": [
  [
   "theorem",
   "add_add_fin2"
  ],
  [
   "theorem",
   "frame_symm"
  ],
  [
   "theorem",
   "relT_symm"
  ],
  [
   "theorem",
   "relC_symm_of_relT"
  ],
  [
   "theorem",
   "gateRel_symm"
  ],
  [
   "def",
   "sqCls"
  ],
  [
   "def",
   "sqSig"
  ],
  [
   "def",
   "sqPc"
  ],
  [
   "def",
   "sqPt"
  ],
  [
   "noncomputable def",
   "sqR"
  ],
  [
   "noncomputable def",
   "sqK"
  ],
  [
   "noncomputable def",
   "sqW"
  ],
  [
   "noncomputable def",
   "sqWi"
  ],
  [
   "noncomputable def",
   "gSqFun"
  ],
  [
   "noncomputable def",
   "gSqInvFun"
  ],
  [
   "theorem",
   "gSqFun_apply"
  ],
  [
   "theorem",
   "gSqInvFun_apply"
  ],
  [
   "theorem",
   "sqPc_sqPc"
  ],
  [
   "theorem",
   "sqPt_sqPt"
  ],
  [
   "theorem",
   "sqCls_sqPc"
  ],
  [
   "theorem",
   "odd5_sqPt"
  ],
  [
   "theorem",
   "odd5_sqPc"
  ],
  [
   "theorem",
   "sqWi_sqW"
  ],
  [
   "theorem",
   "sqW_sqWi"
  ],
  [
   "theorem",
   "gSqInvFun_gSqFun"
  ],
  [
   "theorem",
   "gSqFun_gSqInvFun"
  ],
  [
   "noncomputable def",
   "gSq"
  ],
  [
   "theorem",
   "gSq_apply"
  ],
  [
   "theorem",
   "gSq_symm_apply"
  ],
  [
   "theorem",
   "gSq_frame"
  ],
  [
   "noncomputable def",
   "sqSg"
  ],
  [
   "theorem",
   "homMap_n5_sqSg"
  ],
  [
   "theorem",
   "sqSg_sq"
  ],
  [
   "theorem",
   "sqSg_sqPt"
  ],
  [
   "theorem",
   "sqSg_sqPc"
  ],
  [
   "theorem",
   "gSq_relT"
  ],
  [
   "theorem",
   "gSq_relC"
  ],
  [
   "theorem",
   "gateRel_gSq"
  ],
  [
   "theorem",
   "rsq_cs4"
  ],
  [
   "theorem",
   "rsq_ab"
  ],
  [
   "theorem",
   "rsq_s"
  ],
  [
   "theorem",
   "rsq_key"
  ],
  [
   "theorem",
   "rsq_assemble"
  ],
  [
   "theorem",
   "gSq_core"
  ],
  [
   "theorem",
   "pairVal_gSq_prodState"
  ],
  [
   "theorem",
   "lor_five"
  ],
  [
   "theorem",
   "gSq_pairVal_nonneg"
  ],
  [
   "theorem",
   "gSq_posFwd"
  ],
  [
   "theorem",
   "x5_unit"
  ],
  [
   "theorem",
   "negx5_unit"
  ],
  [
   "theorem",
   "sharpVec_negx5"
  ],
  [
   "theorem",
   "gSq_symm_value"
  ],
  [
   "theorem",
   "gSq_symm_not_mem_maxCone"
  ],
  [
   "theorem",
   "gSq_not_posInv"
  ],
  [
   "theorem",
   "not_nativeGate_gSq"
  ],
  [
   "theorem",
   "not_nativeGate_gSqInv"
  ],
  [
   "theorem",
   "gSq_sep"
  ],
  [
   "theorem",
   "gSqInv_sep"
  ]
 ],
 "RelcSelectC5": [
  [
   "def",
   "oddC5"
  ],
  [
   "def",
   "cC5"
  ],
  [
   "def",
   "nC5"
  ],
  [
   "theorem",
   "cC5_sq"
  ],
  [
   "theorem",
   "homMap_nC5_sign"
  ],
  [
   "theorem",
   "isNot_nC5"
  ],
  [
   "def",
   "sgnC5"
  ],
  [
   "def",
   "pcC5"
  ],
  [
   "def",
   "ptC5"
  ],
  [
   "def",
   "gC5Fun"
  ],
  [
   "theorem",
   "gC5Fun_apply"
  ],
  [
   "theorem",
   "pcC5_pcC5"
  ],
  [
   "theorem",
   "ptC5_ptC5"
  ],
  [
   "theorem",
   "sgnC5_mul_sgnC5"
  ],
  [
   "theorem",
   "oddC5_ptC5"
  ],
  [
   "theorem",
   "gC5Fun_gC5Fun"
  ],
  [
   "def",
   "gC5"
  ],
  [
   "theorem",
   "gC5_apply"
  ],
  [
   "theorem",
   "gC5_symm_apply"
  ],
  [
   "theorem",
   "gC5_frame"
  ],
  [
   "theorem",
   "gC5_relT"
  ],
  [
   "theorem",
   "gC5_relC_lhs"
  ],
  [
   "theorem",
   "gC5_relC_rhs"
  ],
  [
   "theorem",
   "gC5_not_relC"
  ],
  [
   "theorem",
   "selC5_cs"
  ],
  [
   "theorem",
   "selC5_cauchy2"
  ],
  [
   "theorem",
   "selC5_besselJ"
  ],
  [
   "theorem",
   "selC5_besselK"
  ],
  [
   "theorem",
   "selC5_mix"
  ],
  [
   "theorem",
   "selC5_target"
  ],
  [
   "theorem",
   "selC5_ctrl"
  ],
  [
   "theorem",
   "selC5_core"
  ],
  [
   "theorem",
   "selC5_lor"
  ],
  [
   "theorem",
   "prodEffVal_gC5_prodState"
  ],
  [
   "theorem",
   "gC5_prodEffVal_nonneg"
  ],
  [
   "theorem",
   "gC5_posFwd"
  ],
  [
   "theorem",
   "gC5_posInv"
  ],
  [
   "theorem",
   "c5_sep"
  ],
  [
   "theorem",
   "not_nativeGate_gC5"
  ],
  [
   "theorem",
   "relT_not_dimension_selecting"
  ]
 ]
}''')
TEXTS = json.loads(r'''{
 "RelcSelectParity": {
  "relCLeft": "noncomputable def relCLeft (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where\n  toFun F := homMap N ∘ₗ F\n  map_add' F₁ F₂ := LinearMap.ext fun v => by\n    simp only [LinearMap.comp_apply, LinearMap.add_apply, map_add]\n  map_smul' c F := LinearMap.ext fun v => by\n    simp only [LinearMap.comp_apply, LinearMap.smul_apply, map_smul, RingHom.id_apply]",
  "relCConj": "noncomputable def relCConj (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where\n  toFun F := homMap N ∘ₗ F ∘ₗ homMap N\n  map_add' F₁ F₂ := LinearMap.ext fun v => by\n    simp only [LinearMap.comp_apply, LinearMap.add_apply, map_add]\n  map_smul' c F := LinearMap.ext fun v => by\n    simp only [LinearMap.comp_apply, LinearMap.smul_apply, map_smul, RingHom.id_apply]",
  "relCLeft_apply": "theorem relCLeft_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d)\n    (v : HVec d) : relCLeft N F v = homMap N (F v)",
  "relCConj_apply": "theorem relCConj_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d)\n    (v : HVec d) : relCConj N F v = homMap N (F (homMap N v))",
  "relCLeft_eq": "theorem relCLeft_eq (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d) :\n    relCLeft N F = homMap N ∘ₗ F",
  "relCConj_eq": "theorem relCConj_eq (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d) :\n    relCConj N F = homMap N ∘ₗ F ∘ₗ homMap N",
  "opGate_homMap_comp_relC": "theorem opGate_homMap_comp_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)\n    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) (F : HVec d →ₗ[ℝ] HVec d) :\n    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N",
  "opGate_injective_relC": "theorem opGate_injective_relC (G : W d ≃ₗ[ℝ] W d) : Function.Injective (opGate G)",
  "finrank_ker_sub_le_relC": "theorem finrank_ker_sub_le_relC {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]\n    (A L T : V →ₗ[ℝ] V) (hA : Function.Injective A) (hAL : ∀ v, A (L v) = T (A v)) :\n    Module.finrank ℝ (LinearMap.ker (L - LinearMap.id))\n      ≤ Module.finrank ℝ (LinearMap.ker (T - LinearMap.id))",
  "finrank_ker_add_le_relC": "theorem finrank_ker_add_le_relC {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]\n    (A L T : V →ₗ[ℝ] V) (hA : Function.Injective A) (hAL : ∀ v, A (L v) = T (A v)) :\n    Module.finrank ℝ (LinearMap.ker (L + LinearMap.id))\n      ≤ Module.finrank ℝ (LinearMap.ker (T + LinearMap.id))",
  "finrank_ker_relCLeft_sub": "theorem finrank_ker_relCLeft_sub (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Module.finrank ℝ (LinearMap.ker (relCLeft N - LinearMap.id))\n      = (d + 1) * Module.finrank ℝ (plusSpace N)",
  "finrank_ker_relCLeft_add": "theorem finrank_ker_relCLeft_add (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :\n    Module.finrank ℝ (LinearMap.ker (relCLeft N + LinearMap.id))\n      = (d + 1) * Module.finrank ℝ (minusSpace N)",
  "eq_zero_of_plus_minus_relC": "theorem eq_zero_of_plus_minus_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    (F : HVec d →ₗ[ℝ] HVec d) (hp : ∀ u ∈ plusSpace N, F u = 0)\n    (hm : ∀ u ∈ minusSpace N, F u = 0) : F = 0",
  "homMap_comm_relC": "theorem homMap_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))\n    (v : HVec d) : homMap N (F v) = F (homMap N v)",
  "homMap_anticomm_relC": "theorem homMap_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id))\n    (v : HVec d) : homMap N (F v) = -F (homMap N v)",
  "mem_plusSpace_of_comm_relC": "theorem mem_plusSpace_of_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))\n    (u : plusSpace N) : F (u : HVec d) ∈ plusSpace N",
  "mem_minusSpace_of_comm_relC": "theorem mem_minusSpace_of_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)\n    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))\n    (u : minusSpace N) : F (u : HVec d) ∈ minusSpace N",
  "mem_minusSpace_of_anticomm_relC": "theorem mem_minusSpace_of_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : ∀ x, N (N x) = x) {F : HVec d →ₗ[ℝ] HVec d}\n    (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id)) (u : plusSpace N) :\n    F (u : HVec d) ∈ minusSpace N",
  "mem_plusSpace_of_anticomm_relC": "theorem mem_plusSpace_of_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : ∀ x, N (N x) = x) {F : HVec d →ₗ[ℝ] HVec d}\n    (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id)) (u : minusSpace N) :\n    F (u : HVec d) ∈ plusSpace N",
  "relCSplitEven": "noncomputable def relCSplitEven {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    LinearMap.ker (relCConj N - LinearMap.id) →ₗ[ℝ]\n      (plusSpace N →ₗ[ℝ] plusSpace N) × (minusSpace N →ₗ[ℝ] minusSpace N) where\n  toFun F :=\n    (LinearMap.codRestrict (plusSpace N) (F.1 ∘ₗ (plusSpace N).subtype)\n        (fun u => mem_plusSpace_of_comm_relC hN F.2 u),\n      LinearMap.codRestrict (minusSpace N) (F.1 ∘ₗ (minusSpace N).subtype)\n        (fun u => mem_minusSpace_of_comm_relC hN F.2 u))\n  map_add' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)\n  map_smul' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)",
  "relCSplitOdd": "noncomputable def relCSplitOdd {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    LinearMap.ker (relCConj N + LinearMap.id) →ₗ[ℝ]\n      (plusSpace N →ₗ[ℝ] minusSpace N) × (minusSpace N →ₗ[ℝ] plusSpace N) where\n  toFun F :=\n    (LinearMap.codRestrict (minusSpace N) (F.1 ∘ₗ (plusSpace N).subtype)\n        (fun u => mem_minusSpace_of_anticomm_relC hN F.2 u),\n      LinearMap.codRestrict (plusSpace N) (F.1 ∘ₗ (minusSpace N).subtype)\n        (fun u => mem_plusSpace_of_anticomm_relC hN F.2 u))\n  map_add' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)\n  map_smul' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)",
  "relCSplitEven_injective": "theorem relCSplitEven_injective {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    Function.Injective (relCSplitEven hN)",
  "relCSplitOdd_injective": "theorem relCSplitOdd_injective {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    Function.Injective (relCSplitOdd hN)",
  "finrank_ker_relCConj_sub_le": "theorem finrank_ker_relCConj_sub_le {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    Module.finrank ℝ (LinearMap.ker (relCConj N - LinearMap.id))\n      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (plusSpace N)\n        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N)",
  "finrank_ker_relCConj_add_le": "theorem finrank_ker_relCConj_add_le {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :\n    Module.finrank ℝ (LinearMap.ker (relCConj N + LinearMap.id))\n      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (minusSpace N)\n        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N)",
  "balance_of_bounds_relC": "theorem balance_of_bounds_relC {n P Q : ℕ} (hn : P + Q = n) (hQ : 1 ≤ Q)\n    (h1 : n * P ≤ P * P + Q * Q) (h2 : n * Q ≤ P * Q + Q * P) : P = Q",
  "finrank_plus_eq_finrank_minus_relC": "theorem finrank_plus_eq_finrank_minus_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)\n    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :\n    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)",
  "not_even_of_relC": "theorem not_even_of_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)\n    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d"
 },
 "RelcSelectBlock": {
  "CtrlGate": "structure CtrlGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))\n    (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
  "ctrlGate_of_nativeGate": "theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) :\n    CtrlGate Ω z N G",
  "gate_corner_ctrl": "theorem gate_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom z) Y) = tens (hom z) (Mfwd z G Y)",
  "gate_corner_symm_ctrl": "theorem gate_corner_symm_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :\n    G.symm (tens (hom z) Y) = tens (hom z) (Minv z G Y)",
  "Mfwd_Minv_ctrl": "theorem Mfwd_Minv_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :\n    Mfwd z G (Minv z G Y) = Y",
  "lor_Minv_ctrl": "theorem lor_Minv_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {Y : HVec d} (hY : Lor Y) :\n    Lor (Minv z G Y)",
  "gate_actC_ctrl": "theorem gate_actC_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (ω : W d) :\n    G (actC N ω) = actC N (actT N (G ω))",
  "gate_corner_neg_ctrl": "theorem gate_corner_neg_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y))",
  "gt_corner_ctrl": "theorem gt_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom z) (Minv z G t)) = tens (hom z) t",
  "gt_corner_neg_ctrl": "theorem gt_corner_neg_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom (-z)) (Minv z G t)) = tens (hom (-z)) (homMap N t)",
  "gt_center_ctrl": "theorem gt_center_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {t : HVec d}\n    (ht : homMap N t = t) : G (tens (hom 0) (Minv z G t)) = tens (hom 0) t",
  "gt_tangent_corners_ctrl": "theorem gt_tangent_corners_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {f t : HVec d} (hf : Lor f) (ht : Lor t) :\n    pairVal (hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 ∧\n    pairVal (hom z) f (G (tens (lift c) (Minv z G t))) = 0",
  "gt_sphere_ctrl": "theorem gt_sphere_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    pairVal a (hom 0 - u) (G (tens (lift c) (Minv z G (hom 0 + u)))) = 0",
  "gt_sphere_corner_ctrl": "theorem gt_sphere_corner_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    pairVal a (hom z) (G (tens (lift c) (Minv z G (hom z)))) = 0 ∧\n    pairVal a (hom (-z)) (G (tens (lift c) (Minv z G (hom (-z))))) = 0",
  "Phi_sphere_ctrl": "theorem Phi_sphere_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    Phi z G a c u u = Phi z G a c (hom 0) (hom 0) ∧\n    Phi z G a c (hom 0) u = Phi z G a c u (hom 0)",
  "Phi_center_ctrl": "theorem Phi_center_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    Phi z G a c (hom 0) (hom 0) = 0",
  "Phi_center_all_ctrl": "theorem Phi_center_all_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (a : HVec d) :\n    Phi z G a c (hom 0) (hom 0) = 0",
  "Phi_hom_zero_eq_zero_ctrl": "theorem Phi_hom_zero_eq_zero_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (hom 0) c f t = 0",
  "Phi_lift_z_eq_zero_ctrl": "theorem Phi_lift_z_eq_zero_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (lift z) c f t = 0",
  "gt_center_two_ctrl": "theorem gt_center_two_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (t : HVec d) :\n    (2 : ℝ) • G (tens (hom 0) (Minv z G t)) = tens (hom z) t + tens (hom (-z)) (homMap N t)",
  "phi_lift_minus_ctrl": "theorem phi_lift_minus_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) (hNu : homMap N u = -u) {c' : Fin d → ℝ}\n    (hc' : ∑ j, c' j ^ 2 ≤ 1) (hzc' : ∑ j, z j * c' j = 0) :\n    Phi z G (lift c') c u (hom 0) = 0",
  "phi_bvec_minus_unit_ctrl": "theorem phi_bvec_minus_unit_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) (hNu : homMap N u = -u) (μ : Fin (d + 1)) :\n    Phi z G (bvec μ) c u (hom 0) = 0",
  "phi_minusSpace_ctrl": "theorem phi_minusSpace_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {w : HVec d}\n    (hw : w ∈ minusSpace N) (μ : Fin (d + 1)) :\n    Phi z G (bvec μ) c w (hom 0) = 0",
  "homMap_eq_self_of_orth_minusSpace": "theorem homMap_eq_self_of_orth_minusSpace {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hN : IsNot (eball d) z N) {v : HVec d} (h : ∀ w ∈ minusSpace N, ∑ ν, v ν * w ν = 0) :\n    homMap N v = v",
  "actT_slice_ctrl": "theorem actT_slice_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) :\n    actT N (G (tens (lift c) (Minv z G (hom 0)))) = G (tens (lift c) (Minv z G (hom 0)))",
  "blockData_of_orthonormal_ctrl": "theorem blockData_of_orthonormal_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (hd : 2 ≤ d)\n    {q : ℕ} (v : Fin q → HVec d) (hvS : ∀ r, v r ∈ tangentSpace N)\n    (hvv : ∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0)\n    (hspan : ∀ u ∈ tangentSpace N, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0) : BlockData q",
  "blockData_of_ctrlGate": "theorem blockData_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) :\n    BlockData (tangentPlus N)",
  "not_entangling_one_ctrl": "theorem not_entangling_one_ctrl {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}\n    {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : CtrlGate (eball 1) z N G) :\n    ¬ Entangling (eball 1) G",
  "dim_of_ctrlGate": "theorem dim_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) :\n    d = 1 ∨ d = 3",
  "three_of_ctrlGate": "theorem three_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G)\n    (hE : Entangling (eball d) G) : d = 3"
 },
 "RelcSelectSqueeze": {
  "add_add_fin2": "theorem add_add_fin2 : ∀ a b : Fin 2, a + (a + b) = b",
  "frame_symm": "theorem frame_symm {z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d}\n    (hF : ∀ a b : Fin 2,\n      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) :\n    ∀ a b : Fin 2,\n      G.symm (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))",
  "relT_symm": "theorem relT_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω) :\n    ∀ ω, actT N (G.symm (actT N ω)) = G.symm ω",
  "relC_symm_of_relT": "theorem relC_symm_of_relT {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω)\n    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :\n    ∀ ω, actC N (G.symm (actC N ω)) = actT N (G.symm ω)",
  "gateRel_symm": "theorem gateRel_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hR : GateRel N G) : GateRel N G.symm",
  "sqCls": "def sqCls : Fin 6 → Bool\n  | 0 => true | 1 => false | 2 => false | 3 => false | 4 => false | 5 => true",
  "sqSig": "def sqSig : Fin 6 → Fin 6\n  | 0 => 1 | 1 => 0 | 2 => 2 | 3 => 5 | 4 => 4 | 5 => 3",
  "sqPc": "def sqPc (m n : Fin 6) : Fin 6 := if odd5 n then perm5 m else m",
  "sqPt": "def sqPt (m n : Fin 6) : Fin 6 := if sqCls m then n else sqSig n",
  "sqR": "noncomputable def sqR (m : Fin 6) : ℝ := if sqCls m then 1 else 1 / 10",
  "sqK": "noncomputable def sqK (n : Fin 6) : ℝ := if sqCls n then 1 else 1 / 2",
  "sqW": "noncomputable def sqW (m n : Fin 6) : ℝ := sqR m * sqK (sqPt m n)",
  "sqWi": "noncomputable def sqWi (m n : Fin 6) : ℝ := (if sqCls m then 1 else 10) * (if sqCls n then 1 else 2)",
  "gSqFun": "noncomputable def gSqFun (ω : W 5) : W 5 := fun m n => sqW m n * ω (sqPc m n) (sqPt m n)",
  "gSqInvFun": "noncomputable def gSqInvFun (ω : W 5) : W 5 := fun m n => sqWi m n * ω (sqPc m n) (sqPt m n)",
  "gSqFun_apply": "theorem gSqFun_apply (ω : W 5) (m n : Fin 6) :\n    gSqFun ω m n = sqW m n * ω (sqPc m n) (sqPt m n)",
  "gSqInvFun_apply": "theorem gSqInvFun_apply (ω : W 5) (m n : Fin 6) :\n    gSqInvFun ω m n = sqWi m n * ω (sqPc m n) (sqPt m n)",
  "sqPc_sqPc": "theorem sqPc_sqPc : ∀ m n : Fin 6, sqPc (sqPc m n) (sqPt m n) = m",
  "sqPt_sqPt": "theorem sqPt_sqPt : ∀ m n : Fin 6, sqPt (sqPc m n) (sqPt m n) = n",
  "sqCls_sqPc": "theorem sqCls_sqPc : ∀ m n : Fin 6, sqCls (sqPc m n) = sqCls m",
  "odd5_sqPt": "theorem odd5_sqPt : ∀ m n : Fin 6, odd5 (sqPt m n) = odd5 n",
  "odd5_sqPc": "theorem odd5_sqPc : ∀ m n : Fin 6, odd5 (sqPc m n) = (if odd5 n then !odd5 m else odd5 m)",
  "sqWi_sqW": "theorem sqWi_sqW (m n : Fin 6) : sqWi m n * sqW (sqPc m n) (sqPt m n) = 1",
  "sqW_sqWi": "theorem sqW_sqWi (m n : Fin 6) : sqW m n * sqWi (sqPc m n) (sqPt m n) = 1",
  "gSqInvFun_gSqFun": "theorem gSqInvFun_gSqFun (ω : W 5) : gSqInvFun (gSqFun ω) = ω",
  "gSqFun_gSqInvFun": "theorem gSqFun_gSqInvFun (ω : W 5) : gSqFun (gSqInvFun ω) = ω",
  "gSq": "noncomputable def gSq : W 5 ≃ₗ[ℝ] W 5 where\n  toFun := gSqFun\n  invFun := gSqInvFun\n  map_add' ω₁ ω₂ := by\n    funext m n\n    simp only [gSqFun_apply, Pi.add_apply, mul_add]\n  map_smul' c ω := by\n    funext m n\n    simp only [gSqFun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]\n    ring\n  left_inv := gSqInvFun_gSqFun\n  right_inv := gSqFun_gSqInvFun",
  "gSq_apply": "theorem gSq_apply (ω : W 5) : gSq ω = gSqFun ω",
  "gSq_symm_apply": "theorem gSq_symm_apply (ω : W 5) : gSq.symm ω = gSqInvFun ω",
  "gSq_frame": "theorem gSq_frame (a b : Fin 2) :\n    gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))",
  "sqSg": "noncomputable def sqSg (μ : Fin 6) : ℝ := if odd5 μ then -1 else 1",
  "homMap_n5_sqSg": "theorem homMap_n5_sqSg (v : HVec 5) (μ : Fin (5 + 1)) : homMap n5 v μ = sqSg μ * v μ",
  "sqSg_sq": "theorem sqSg_sq (μ : Fin 6) : sqSg μ * sqSg μ = 1",
  "sqSg_sqPt": "theorem sqSg_sqPt (m n : Fin 6) : sqSg (sqPt m n) = sqSg n",
  "sqSg_sqPc": "theorem sqSg_sqPc (m n : Fin 6) : sqSg (sqPc m n) = sqSg m * sqSg n",
  "gSq_relT": "theorem gSq_relT : ∀ ω, actT n5 (gSq (actT n5 ω)) = gSq ω",
  "gSq_relC": "theorem gSq_relC : ∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω)",
  "gateRel_gSq": "theorem gateRel_gSq : GateRel n5 gSq",
  "rsq_cs4": "theorem rsq_cs4 (p1 p2 p3 p4 q1 q2 q3 q4 : ℝ) :\n    (p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4) ^ 2\n      ≤ (p1 ^ 2 + p2 ^ 2 + p3 ^ 2 + p4 ^ 2) * (q1 ^ 2 + q2 ^ 2 + q3 ^ 2 + q4 ^ 2)",
  "rsq_ab": "theorem rsq_ab (f t s u A B : ℝ) (hf : 0 ≤ f) (ht : 0 ≤ t) (hs : 0 ≤ s) (htf : t ≤ f)\n    (hs1 : s ≤ 1) (hu : u ^ 2 ≤ (f ^ 2 - t ^ 2) * (1 - s ^ 2))\n    (hA : f + u - t * s / 2 ≤ A) (hB : f - u - t * s / 2 ≤ B) :\n    0 ≤ A ∧ 0 ≤ B ∧ (t ^ 2 + f ^ 2 * s ^ 2) / 8 ≤ A * B",
  "rsq_s": "theorem rsq_s (f b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 : ℝ)\n    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ f ^ 2)\n    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    (b1 + (f * y0 + b2 * y1) / 2) ^ 2 + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) ^ 2\n      ≤ 2 * (b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2) + f ^ 2 * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2)",
  "rsq_key": "theorem rsq_key (b0 b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 : ℝ) (hb0 : 0 ≤ b0)\n    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ b0 ^ 2)\n    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    0 ≤ b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2\n      ∧ 0 ≤ b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2\n      ∧ ((b1 + (b0 * y0 + b2 * y1) / 2) ^ 2 + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) ^ 2) / 50\n        ≤ (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2)\n          * (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2)",
  "rsq_assemble": "theorem rsq_assemble (α p q A B Se So Ce Co Tc Ta : ℝ) (h1 : 0 ≤ 1 + α) (h2 : 0 ≤ 1 - α)\n    (hp : 0 ≤ p) (hq : 0 ≤ q) (hA : 0 ≤ A) (hB : 0 ≤ B) (hTc0 : 0 ≤ Tc) (hTa0 : 0 ≤ Ta)\n    (hTc : Tc ≤ 1 - α ^ 2) (hTa : Ta ≤ p * q) (hCe : Ce ^ 2 ≤ Tc * Ta) (hCo : Co ^ 2 ≤ Tc * Ta)\n    (hkey : (Se ^ 2 + So ^ 2) / 50 ≤ A * B) :\n    0 ≤ (1 + α) / 2 * (p * A) + (1 - α) / 2 * (q * B) + (Se * Ce + So * Co) / 10",
  "gSq_core": "theorem gSq_core (a0 a1 a2 a3 a4 a5 b0 b1 b2 b3 b4 b5 x0 x1 x2 x3 x4 y0 y1 y2 y3 y4 : ℝ)\n    (ha0 : 0 ≤ a0) (ha : a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2 + a5 ^ 2 ≤ a0 ^ 2)\n    (hb0 : 0 ≤ b0) (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ b0 ^ 2)\n    (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 ≤ 1)\n    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    0 ≤ (1 + x4) / 2 * ((a0 + a5) * (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2))\n      + (1 - x4) / 2 * ((a0 - a5) * (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2))\n      + ((b1 + (b0 * y0 + b2 * y1) / 2) * (x0 * a1 + x1 * a2 + x2 * a3 + x3 * a4)\n        + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) * (x0 * a3 + x1 * a4 + x2 * a1 + x3 * a2)) / 10",
  "pairVal_gSq_prodState": "theorem pairVal_gSq_prodState (a b : HVec 5) (x y : Fin 5 → ℝ) :\n    pairVal a b (gSq (prodState x y))\n      = (1 + x 4) / 2\n          * ((a 0 + a 5) * (b 0 + b 5 * y 4 + (b 1 * y 0 + b 2 * y 1 + b 3 * y 2 + b 4 * y 3) / 2))\n        + (1 - x 4) / 2\n          * ((a 0 - a 5) * (b 0 - b 5 * y 4 + (b 1 * y 0 + b 2 * y 1 - b 3 * y 2 - b 4 * y 3) / 2))\n        + ((b 1 + (b 0 * y 0 + b 2 * y 1) / 2) * (x 0 * a 1 + x 1 * a 2 + x 2 * a 3 + x 3 * a 4)\n          + (b 3 * y 4 + (b 5 * y 2 + b 4 * y 3) / 2)\n            * (x 0 * a 3 + x 1 * a 4 + x 2 * a 1 + x 3 * a 2)) / 10",
  "lor_five": "theorem lor_five {v : HVec 5} (hv : Lor v) :\n    0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2 + v 5 ^ 2 ≤ v 0 ^ 2",
  "gSq_pairVal_nonneg": "theorem gSq_pairVal_nonneg {a b : HVec 5} (ha : Lor a) (hb : Lor b) {x y : Fin 5 → ℝ}\n    (hx : x ∈ eball 5) (hy : y ∈ eball 5) : 0 ≤ pairVal a b (gSq (prodState x y))",
  "gSq_posFwd": "theorem gSq_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5)",
  "x5_unit": "theorem x5_unit : ∑ j, x5 j ^ 2 = 1",
  "negx5_unit": "theorem negx5_unit : ∑ j, (-x5) j ^ 2 = 1",
  "sharpVec_negx5": "theorem sharpVec_negx5 : sharpVec (-x5) = fun μ : Fin (5 + 1) =>\n    if μ = 0 then 1 / 2 else if μ = 1 then -1 / 2 else 0",
  "gSq_symm_value": "theorem gSq_symm_value :\n    prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2",
  "gSq_symm_not_mem_maxCone": "theorem gSq_symm_not_mem_maxCone : gSq.symm (prodState z5 x5) ∉ maxCone (eball 5)",
  "gSq_not_posInv": "theorem gSq_not_posInv :\n    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)",
  "not_nativeGate_gSq": "theorem not_nativeGate_gSq : ¬ NativeGate (eball 5) z5 n5 gSq",
  "not_nativeGate_gSqInv": "theorem not_nativeGate_gSqInv : ¬ NativeGate (eball 5) z5 n5 gSq.symm",
  "gSq_sep": "theorem gSq_sep :\n    IsNot (eball 5) z5 n5\n      ∧ (∀ a b : Fin 2,\n          gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)))\n      ∧ GateRel n5 gSq\n      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))\n      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5))",
  "gSqInv_sep": "theorem gSqInv_sep :\n    IsNot (eball 5) z5 n5\n      ∧ (∀ a b : Fin 2,\n          gSq.symm (prodState (corner z5 a) (corner z5 b))\n            = prodState (corner z5 a) (corner z5 (a + b)))\n      ∧ GateRel n5 gSq.symm\n      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))\n      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5))"
 },
 "RelcSelectC5": {
  "oddC5": "def oddC5 : Fin 6 → Bool\n  | 0 => false | 1 => false | 2 => true | 3 => true | 4 => true | 5 => true",
  "cC5": "def cC5 (j : Fin 5) : ℝ := if oddC5 j.succ then -1 else 1",
  "nC5": "def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5",
  "cC5_sq": "theorem cC5_sq (j : Fin 5) : cC5 j ^ 2 = 1",
  "homMap_nC5_sign": "theorem homMap_nC5_sign (v : HVec 5) (μ : Fin (5 + 1)) :\n    homMap nC5 v μ = (if oddC5 μ then -1 else 1) * v μ",
  "isNot_nC5": "theorem isNot_nC5 : IsNot (eball 5) z5 nC5",
  "sgnC5": "def sgnC5 (μ ν : Fin 6) : ℝ :=\n  if ((μ = 1 ∨ μ = 3) ∧ (ν = 4 ∨ ν = 5)) ∨ ((μ = 2 ∨ μ = 4) ∧ (ν = 2 ∨ ν = 3)) then -1 else 1",
  "pcC5": "def pcC5 : Fin 6 → Fin 6 → Fin 6\n  | 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 5 | 0, 3 => 5 | 0, 4 => 5 | 0, 5 => 5\n  | 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2 | 1, 4 => 2 | 1, 5 => 2\n  | 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1 | 2, 4 => 1 | 2, 5 => 1\n  | 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 4 | 3, 3 => 4 | 3, 4 => 4 | 3, 5 => 4\n  | 4, 0 => 4 | 4, 1 => 4 | 4, 2 => 3 | 4, 3 => 3 | 4, 4 => 3 | 4, 5 => 3\n  | 5, 0 => 5 | 5, 1 => 5 | 5, 2 => 0 | 5, 3 => 0 | 5, 4 => 0 | 5, 5 => 0",
  "ptC5": "def ptC5 : Fin 6 → Fin 6 → Fin 6\n  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3 | 0, 4 => 4 | 0, 5 => 5\n  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 5 | 1, 3 => 4 | 1, 4 => 3 | 1, 5 => 2\n  | 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 5 | 2, 3 => 4 | 2, 4 => 3 | 2, 5 => 2\n  | 3, 0 => 1 | 3, 1 => 0 | 3, 2 => 5 | 3, 3 => 4 | 3, 4 => 3 | 3, 5 => 2\n  | 4, 0 => 1 | 4, 1 => 0 | 4, 2 => 5 | 4, 3 => 4 | 4, 4 => 3 | 4, 5 => 2\n  | 5, 0 => 0 | 5, 1 => 1 | 5, 2 => 2 | 5, 3 => 3 | 5, 4 => 4 | 5, 5 => 5",
  "gC5Fun": "def gC5Fun (ω : W 5) : W 5 := fun μ ν => sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)",
  "gC5Fun_apply": "theorem gC5Fun_apply (ω : W 5) (μ ν : Fin 6) :\n    gC5Fun ω μ ν = sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)",
  "pcC5_pcC5": "theorem pcC5_pcC5 : ∀ μ ν : Fin 6, pcC5 (pcC5 μ ν) (ptC5 μ ν) = μ",
  "ptC5_ptC5": "theorem ptC5_ptC5 : ∀ μ ν : Fin 6, ptC5 (pcC5 μ ν) (ptC5 μ ν) = ν",
  "sgnC5_mul_sgnC5": "theorem sgnC5_mul_sgnC5 : ∀ μ ν : Fin 6, sgnC5 μ ν * sgnC5 (pcC5 μ ν) (ptC5 μ ν) = 1",
  "oddC5_ptC5": "theorem oddC5_ptC5 : ∀ μ ν : Fin 6, oddC5 (ptC5 μ ν) = oddC5 ν",
  "gC5Fun_gC5Fun": "theorem gC5Fun_gC5Fun (ω : W 5) : gC5Fun (gC5Fun ω) = ω",
  "gC5": "def gC5 : W 5 ≃ₗ[ℝ] W 5 where\n  toFun := gC5Fun\n  invFun := gC5Fun\n  map_add' ω₁ ω₂ := by\n    funext μ ν\n    simp only [gC5Fun_apply, Pi.add_apply, mul_add]\n  map_smul' c ω := by\n    funext μ ν\n    simp only [gC5Fun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]\n    ring\n  left_inv := gC5Fun_gC5Fun\n  right_inv := gC5Fun_gC5Fun",
  "gC5_apply": "theorem gC5_apply (ω : W 5) : gC5 ω = gC5Fun ω",
  "gC5_symm_apply": "theorem gC5_symm_apply (ω : W 5) : gC5.symm ω = gC5Fun ω",
  "gC5_frame": "theorem gC5_frame (a b : Fin 2) :\n    gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))",
  "gC5_relT": "theorem gC5_relT (ω : W 5) : actT nC5 (gC5 (actT nC5 ω)) = gC5 ω",
  "gC5_relC_lhs": "theorem gC5_relC_lhs : actC nC5 (gC5 (actC nC5 (OddChar.entW 3 3))) 4 4 = 1",
  "gC5_relC_rhs": "theorem gC5_relC_rhs : actT nC5 (gC5 (OddChar.entW 3 3)) 4 4 = -1",
  "gC5_not_relC": "theorem gC5_not_relC : ¬ ∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)",
  "selC5_cs": "theorem selC5_cs (a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 : ℝ) :\n    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3 + a4 * b4) ^ 2\n      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2)",
  "selC5_cauchy2": "theorem selC5_cauchy2 (s1 s2 a b : ℝ) :\n    (s1 * a + s2 * b) ^ 2 ≤ (s1 ^ 2 + s2 ^ 2) * (a ^ 2 + b ^ 2)",
  "selC5_besselJ": "theorem selC5_besselJ (a0 a1 a2 a3 b0 b1 b2 b3 : ℝ) :\n    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a1 * b0 - a0 * b1 + a3 * b2 - a2 * b3) ^ 2\n      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2)",
  "selC5_besselK": "theorem selC5_besselK (a0 a1 a2 a3 b0 b1 b2 b3 : ℝ) :\n    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a3 * b0 + a2 * b1 - a1 * b2 - a0 * b3) ^ 2\n      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2)",
  "selC5_mix": "theorem selC5_mix (A B u : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) (hu : u ^ 2 ≤ A * B) :\n    0 ≤ A + B + 2 * u",
  "selC5_target": "theorem selC5_target (f0 f1 f2 f3 f4 f5 y0 y1 y2 y3 y4 : ℝ) (hf0 : 0 ≤ f0)\n    (hf : f1 ^ 2 + f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2 ≤ f0 ^ 2)\n    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :\n    0 ≤ (f0 + f1 * y0) + (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ∧\n      0 ≤ (f0 + f1 * y0) - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ∧\n      (f0 * y0 + f1) ^ 2 + (f5 * y1 + f4 * y2 - f3 * y3 - f2 * y4) ^ 2\n        ≤ (f0 + f1 * y0) ^ 2 - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ^ 2",
  "selC5_ctrl": "theorem selC5_ctrl (e0 e5 x4 p m s1 s2 al be : ℝ) (he0 : 0 ≤ e0) (he5 : e5 ^ 2 ≤ e0 ^ 2)\n    (hx4 : x4 ^ 2 ≤ 1) (hpm : 0 ≤ p + m) (hmp : 0 ≤ p - m)\n    (hab : al ^ 2 + be ^ 2 ≤ p ^ 2 - m ^ 2)\n    (hs : s1 ^ 2 + s2 ^ 2 ≤ (e0 ^ 2 - e5 ^ 2) * (1 - x4 ^ 2)) :\n    0 ≤ (e0 + x4 * e5) * p + (e5 + x4 * e0) * m + s1 * al + s2 * be",
  "selC5_core": "theorem selC5_core (e0 e1 e2 e3 e4 e5 x0 x1 x2 x3 x4 p m al be : ℝ) (he0 : 0 ≤ e0)\n    (he : e1 ^ 2 + e2 ^ 2 + e3 ^ 2 + e4 ^ 2 + e5 ^ 2 ≤ e0 ^ 2)\n    (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 ≤ 1)\n    (hpm : 0 ≤ p + m) (hmp : 0 ≤ p - m) (hab : al ^ 2 + be ^ 2 ≤ p ^ 2 - m ^ 2) :\n    0 ≤ (e0 + x4 * e5) * p + (e5 + x4 * e0) * m\n      + (e1 * x0 + e2 * x1 + e3 * x2 + e4 * x3) * al\n      + (e2 * x0 - e1 * x1 + e4 * x2 - e3 * x3) * be",
  "selC5_lor": "theorem selC5_lor {v : HVec 5} (hv : Lor v) :\n    0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2 + v 5 ^ 2 ≤ v 0 ^ 2",
  "prodEffVal_gC5_prodState": "theorem prodEffVal_gC5_prodState (e f : (Fin 5 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 5 → ℝ) :\n    prodEffVal e f (gC5 (prodState x y))\n      = (ehom e 0 + x 4 * ehom e 5) * (ehom f 0 + ehom f 1 * y 0)\n        + (ehom e 5 + x 4 * ehom e 0)\n          * (ehom f 2 * y 1 + ehom f 3 * y 2 + ehom f 4 * y 3 + ehom f 5 * y 4)\n        + (ehom e 1 * x 0 + ehom e 2 * x 1 + ehom e 3 * x 2 + ehom e 4 * x 3)\n          * (ehom f 0 * y 0 + ehom f 1)\n        + (ehom e 2 * x 0 - ehom e 1 * x 1 + ehom e 4 * x 2 - ehom e 3 * x 3)\n          * (ehom f 5 * y 1 + ehom f 4 * y 2 - ehom f 3 * y 3 - ehom f 2 * y 4)",
  "gC5_prodEffVal_nonneg": "theorem gC5_prodEffVal_nonneg {e f : (Fin 5 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball 5) e)\n    (hf : IsEffectOn (eball 5) f) {x y : Fin 5 → ℝ} (hx : x ∈ eball 5) (hy : y ∈ eball 5) :\n    0 ≤ prodEffVal e f (gC5 (prodState x y))",
  "gC5_posFwd": "theorem gC5_posFwd :\n    ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)",
  "gC5_posInv": "theorem gC5_posInv :\n    ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5)",
  "c5_sep": "theorem c5_sep :\n    IsNot (eball 5) z5 nC5 ∧\n      (∀ a b : Fin 2,\n        gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧\n      (∀ ω, actT nC5 (gC5 (actT nC5 ω)) = gC5 ω) ∧\n      (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)) ∧\n      (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5)) ∧\n      ¬ (∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω))",
  "not_nativeGate_gC5": "theorem not_nativeGate_gC5 : ¬ NativeGate (eball 5) z5 nC5 gC5",
  "relT_not_dimension_selecting": "theorem relT_not_dimension_selecting :\n    ¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),\n      IsNot (eball d) z N →\n      (∀ a b : Fin 2,\n        G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) →\n      (∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) →\n      (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) →\n      (∀ ω, actT N (G (actT N ω)) = G ω) →\n      d = 1 ∨ d = 3"
 }
}''')
PRINTS = json.loads(r'''{
 "RelcSelectParity": [
  "OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC",
  "OIBridge.RelcSelect.not_even_of_relC"
 ],
 "RelcSelectBlock": [
  "OIBridge.RelcSelect.ctrlGate_of_nativeGate",
  "OIBridge.RelcSelect.actT_slice_ctrl",
  "OIBridge.RelcSelect.blockData_of_ctrlGate",
  "OIBridge.RelcSelect.dim_of_ctrlGate",
  "OIBridge.RelcSelect.three_of_ctrlGate"
 ],
 "RelcSelectSqueeze": [
  "OIBridge.RelcSelect.frame_symm",
  "OIBridge.RelcSelect.relT_symm",
  "OIBridge.RelcSelect.relC_symm_of_relT",
  "OIBridge.RelcSelect.gateRel_symm",
  "OIBridge.RelcSelect.gSq_frame",
  "OIBridge.RelcSelect.gateRel_gSq",
  "OIBridge.RelcSelect.pairVal_gSq_prodState",
  "OIBridge.RelcSelect.gSq_core",
  "OIBridge.RelcSelect.gSq_posFwd",
  "OIBridge.RelcSelect.gSq_symm_value",
  "OIBridge.RelcSelect.gSq_not_posInv",
  "OIBridge.RelcSelect.not_nativeGate_gSq",
  "OIBridge.RelcSelect.not_nativeGate_gSqInv",
  "OIBridge.RelcSelect.gSq_sep",
  "OIBridge.RelcSelect.gSqInv_sep"
 ],
 "RelcSelectC5": [
  "OIBridge.RelcSelect.isNot_nC5",
  "OIBridge.RelcSelect.gC5_frame",
  "OIBridge.RelcSelect.gC5_relT",
  "OIBridge.RelcSelect.gC5_not_relC",
  "OIBridge.RelcSelect.selC5_target",
  "OIBridge.RelcSelect.selC5_core",
  "OIBridge.RelcSelect.prodEffVal_gC5_prodState",
  "OIBridge.RelcSelect.gC5_posFwd",
  "OIBridge.RelcSelect.gC5_posInv",
  "OIBridge.RelcSelect.c5_sep",
  "OIBridge.RelcSelect.not_nativeGate_gC5",
  "OIBridge.RelcSelect.relT_not_dimension_selecting"
 ]
}''')
PREAMBLE = json.loads(r'''{
 "RelcSelectParity": "import OIBridge.OddChar\n\nnamespace OIBridge\nnamespace RelcSelect\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot\n\nvariable {d : ℕ}\n",
 "RelcSelectBlock": "import OIBridge.RelcSelectParity\nimport OIBridge.ParityNot\n\nnamespace OIBridge\nnamespace RelcSelect\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot\n\nvariable {d : ℕ}\n",
 "RelcSelectSqueeze": "import OIBridge.OddChar\n\nnamespace OIBridge\nnamespace RelcSelect\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot\n\nvariable {d : ℕ}\n",
 "RelcSelectC5": "import OIBridge.OddChar\n\nnamespace OIBridge\nnamespace RelcSelect\n\nopen KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot\n"
}''')
CONTEXT = json.loads(r'''{
 "RelcSelectParity": [
  "namespace OIBridge",
  "namespace RelcSelect",
  "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot",
  "variable {d : ℕ}",
  "end RelcSelect",
  "end OIBridge"
 ],
 "RelcSelectBlock": [
  "namespace OIBridge",
  "namespace RelcSelect",
  "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot",
  "variable {d : ℕ}",
  "end RelcSelect",
  "end OIBridge"
 ],
 "RelcSelectSqueeze": [
  "namespace OIBridge",
  "namespace RelcSelect",
  "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot",
  "variable {d : ℕ}",
  "end RelcSelect",
  "end OIBridge"
 ],
 "RelcSelectC5": [
  "namespace OIBridge",
  "namespace RelcSelect",
  "open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot",
  "end RelcSelect",
  "end OIBridge"
 ]
}''')
LANDED = json.loads(r'''{
 "Entangling": "def Entangling (Ω : Set (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop := ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ, G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬ IsProduct Ω (G (prodState x y))",
 "GateRel#fields": "relT relC",
 "GateRel#relC": "relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "GateRel#relT": "relT : ∀ ω, actT N (G (actT N ω)) = G ω",
 "IsNot": "structure IsNot (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Prop where unit : ∑ j, z j ^ 2 = 1 invol : ∀ x, N (N x) = x preserves : ∀ x ∈ Ω, N x ∈ Ω flips : N z = -z",
 "NativeGate#fields": "frame posFwd posInv relT relC",
 "NativeGate#frame": "frame : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))",
 "NativeGate#header": "structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop",
 "NativeGate#posFwd": "posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω",
 "NativeGate#posInv": "posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω",
 "NativeGate#relC": "relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)",
 "NativeGate#relT": "relT : ∀ ω, actT N (G (actT N ω)) = G ω",
 "blockData_of_nativeGate": "theorem blockData_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : BlockData (tangentPlus N)",
 "c5": "def c5 (j : Fin 5) : ℝ := if odd5 j.succ then -1 else 1",
 "copy#Mfwd_Minv": "theorem Mfwd_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    Mfwd z G (Minv z G Y) = Y := by\n  apply tens_hom_inj (x := z)\n  rw [← gate_corner hN hG, ← gate_corner_symm hN hG, G.apply_symm_apply]",
 "copy#Phi_center": "theorem Phi_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    Phi z G a c (hom 0) (hom 0) = 0 := by\n  have hz0 : lift z 0 = 0 := lift_zero z\n  have hz1 : ∑ μ, lift z μ ^ 2 = 1 := by\n    rw [Fin.sum_univ_succ, lift_zero, zero_pow two_ne_zero, zero_add]\n    simpa using hN.unit\n  obtain ⟨ha1, hb1⟩ := Phi_sphere hN hG hc hzc ha hz0 hz1\n  have hc0 : Phi z G a c (hom z) (hom z) = 0 := (gt_sphere_corner hN hG hc hzc ha).1\n  have hc1 : Phi z G a c (hom (-z)) (hom (-z)) = 0 := (gt_sphere_corner hN hG hc hzc ha).2\n  rw [hom_eq_add_lift z] at hc0\n  rw [hom_eq_add_lift (-z), lift_neg, ← sub_eq_add_neg] at hc1\n  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at hc0 hc1\n  linarith",
 "copy#Phi_center_all": "theorem Phi_center_all {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (a : HVec d) :\n    Phi z G a c (hom 0) (hom 0) = 0 := by\n  have h := linearMap_eq_zero_of_lor (pvLeft (hom 0) (G (tens (lift c) (Minv z G (hom 0)))))\n    (fun a ha => Phi_center hN hG hc hzc ha)\n  have := LinearMap.congr_fun h a\n  rw [LinearMap.zero_apply] at this\n  exact this",
 "copy#Phi_hom_zero_eq_zero": "theorem Phi_hom_zero_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (hom 0) c f t = 0 := by\n  have key : ∀ f t, Lor f → Lor t → Phi z G (hom 0) c f t = 0 := by\n    intro f t hf ht\n    obtain ⟨h1, h2⟩ := gt_tangent_corners hN hG hc hzc hf ht\n    have hboth : pairVal (hom z + hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 := by\n      rw [pairVal_add_left, h1, h2, add_zero]\n    rw [hom_add_hom_neg, pairVal_smul_left] at hboth\n    rw [Phi_apply]\n    linarith\n  have hT : ∀ f, Lor f → Phi z G (hom 0) c f = 0 := fun f hf =>\n    linearMap_eq_zero_of_lor _ (fun t ht => key f t hf ht)\n  have hF : Phi z G (hom 0) c = 0 := linearMap_eq_zero_of_lor _ hT\n  rw [hF, LinearMap.zero_apply, LinearMap.zero_apply]",
 "copy#Phi_lift_z_eq_zero": "theorem Phi_lift_z_eq_zero {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) (f t : HVec d) :\n    Phi z G (lift z) c f t = 0 := by\n  have key : ∀ f t, Lor f → Lor t → Phi z G (lift z) c f t = 0 := by\n    intro f t hf ht\n    have h2 := (gt_tangent_corners hN hG hc hzc hf ht).2\n    have h0 := Phi_hom_zero_eq_zero hN hG hc hzc f t\n    rw [hom_eq_add_lift z, pairVal_add_left] at h2\n    rw [Phi_apply] at h0\n    rw [Phi_apply]\n    linarith\n  have hT : ∀ f, Lor f → Phi z G (lift z) c f = 0 := fun f hf =>\n    linearMap_eq_zero_of_lor _ (fun t ht => key f t hf ht)\n  have hF : Phi z G (lift z) c = 0 := linearMap_eq_zero_of_lor _ hT\n  rw [hF, LinearMap.zero_apply, LinearMap.zero_apply]",
 "copy#Phi_sphere": "theorem Phi_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    Phi z G a c u u = Phi z G a c (hom 0) (hom 0) ∧\n    Phi z G a c (hom 0) u = Phi z G a c u (hom 0) := by\n  have h1 : Phi z G a c (hom 0 - u) (hom 0 + u) = 0 := gt_sphere hN hG hc hzc ha hu0 hu\n  have hu0' : (-u) 0 = 0 := by rw [Pi.neg_apply, hu0, neg_zero]\n  have hu' : ∑ μ, (-u) μ ^ 2 = 1 := by simpa [neg_sq] using hu\n  have h2 : Phi z G a c (hom 0 - -u) (hom 0 + -u) = 0 := gt_sphere hN hG hc hzc ha hu0' hu'\n  rw [sub_neg_eq_add, ← sub_eq_add_neg] at h2\n  simp only [map_add, map_sub, LinearMap.add_apply, LinearMap.sub_apply] at h1 h2\n  constructor <;> linarith",
 "copy#blockData_of_nativeGate": "theorem blockData_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    BlockData (tangentPlus N) := by\n  obtain ⟨q, v, hq, hvS, hvv, hspan⟩ := exists_orthonormal_basis (tangentSpace N)\n  rw [finrank_tangentSpace] at hq\n  rw [← hq]\n  exact blockData_of_orthonormal hN hG hd v hvS hvv hspan",
 "copy#blockData_of_orthonormal": "theorem blockData_of_orthonormal {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (hd : 2 ≤ d)\n    {q : ℕ} (v : Fin q → HVec d) (hvS : ∀ r, v r ∈ tangentSpace N)\n    (hvv : ∀ r s, ∑ μ, v r μ * v s μ = if r = s then 1 else 0)\n    (hspan : ∀ u ∈ tangentSpace N, (∀ r, ∑ μ, v r μ * u μ = 0) → u = 0) : BlockData q := by\n  have hz := hN.unit\n  have hv0 : ∀ r, v r 0 = 0 := fun r => (mem_tangentSpace.mp (hvS r)).2\n  have hvN : ∀ r, homMap N (v r) = v r := fun r => (mem_tangentSpace.mp (hvS r)).1\n  have hvu : ∀ r, ∑ μ, v r μ ^ 2 = 1 := fun r => by\n    have := hvv r r\n    rw [if_pos rfl] at this\n    rw [← this]\n    exact Finset.sum_congr rfl fun μ _ => sq _\n  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,\n      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=\n    fun x hx y hy => hG.posFwd x hx y hy\n  have hsym : ∀ k l r, Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r)\n      = Phi z G (hom (tperp z k)) (tperp z l) (v r) (hom 0) := fun k l r =>\n    (Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)\n      (hvu r)).2\n  have hdiag : ∀ k l r, Phi z G (hom (tperp z k)) (tperp z l) (v r) (v r) = 0 := fun k l r => by\n    rw [(Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) (hv0 r)\n      (hvu r)).1]\n    exact Phi_center hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))\n  have hanti : ∀ k l r s, Phi z G (hom (tperp z k)) (tperp z l) (v r) (v s)\n      + Phi z G (hom (tperp z k)) (tperp z l) (v s) (v r) = 0 := by\n    intro k l r s\n    by_cases hrs : r = s\n    · subst hrs; rw [hdiag, add_zero]\n    · obtain ⟨w, hw⟩ : ∃ w : HVec d, w = (8 / 17 : ℝ) • v r + (15 / 17 : ℝ) • v s := ⟨_, rfl⟩\n      have hw0 : w 0 = 0 := by\n        rw [hw, Pi.add_apply, Pi.smul_apply, Pi.smul_apply, hv0, hv0, smul_zero, smul_zero,\n          add_zero]\n      have hwu : ∑ μ, w μ ^ 2 = 1 := by\n        have e : ∀ μ, w μ ^ 2 = (8 / 17 : ℝ) ^ 2 * (v r μ * v r μ)\n            + 2 * ((8 / 17 : ℝ) * (15 / 17 : ℝ)) * (v r μ * v s μ)\n            + (15 / 17 : ℝ) ^ 2 * (v s μ * v s μ) := fun μ => by\n          rw [hw, Pi.add_apply, Pi.smul_apply, Pi.smul_apply, smul_eq_mul, smul_eq_mul]; ring\n        rw [Finset.sum_congr rfl fun μ _ => e μ, Finset.sum_add_distrib, Finset.sum_add_distrib,\n          ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum, hvv r r, hvv r s, hvv s s,\n          if_pos rfl, if_pos rfl, if_neg hrs]\n        norm_num\n      have hww : Phi z G (hom (tperp z k)) (tperp z l) w w = 0 := by\n        rw [(Phi_sphere hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k)) hw0\n          hwu).1]\n        exact Phi_center hN hG (tperp_le_one hz l) (tperp_dot_z hz l) (lor_hom (tperp_mem hz k))\n      rw [hw] at hww\n      simp only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul,\n        hdiag] at hww\n      linarith\n  refine ⟨d, fun r => Matrix.of fun k l => Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r),\n    fun r s => Matrix.of fun k l => Phi z G (hom (tperp z k)) (tperp z l) (v r) (v s), ?_, ?_, ?_⟩\n  · intro r s\n    ext k l\n    simp only [Matrix.of_apply, Matrix.neg_apply]\n    exact eq_neg_of_add_eq_zero_left (hanti k l r s)\n  · intro k l i s hs b hb\n    simp only [Matrix.of_apply]\n    have hcl := tperp_le_one hz l\n    have hzl := tperp_dot_z hz l\n    have hak : Lor (hom (tperp z k)) := lor_hom (tperp_mem hz k)\n    obtain ⟨f, hf⟩ : ∃ f : HVec d, f = hom 0 + ∑ j, b j • v j := ⟨_, rfl⟩\n    obtain ⟨t, ht⟩ : ∃ t : HVec d, t = hom 0 + s • v i := ⟨_, rfl⟩\n    have hs2 : s ^ 2 = 1 := by rcases hs with h | h <;> rw [h] <;> norm_num\n    have hd00 : dotB (hom 0) (hom 0) = 1 := dot_hom_hom_zero (0 : Fin d → ℝ)\n    have hd0 : ∀ r, dotB (hom 0) (v r) = 0 := fun r => by\n      rw [dotB_apply, Fin.sum_univ_succ, hom_zero, one_mul, hv0 r]; simp [hom_succ]\n    have hd0' : ∀ r, dotB (v r) (hom 0) = 0 := fun r => by\n      rw [dotB_apply, Fin.sum_univ_succ, hom_zero, mul_one, hv0 r]; simp [hom_succ]\n    have hvv' : ∀ r s, dotB (v r) (v s) = if r = s then 1 else 0 := hvv\n    have hS0 : dotB (∑ j, b j • v j) (hom 0) = 0 := by\n      rw [LinearMap.map_sum₂]\n      exact Finset.sum_eq_zero fun j _ => by rw [LinearMap.map_smul₂, hd0', smul_zero]\n    have hS0' : dotB (hom 0) (∑ j, b j • v j) = 0 := by\n      rw [map_sum]\n      exact Finset.sum_eq_zero fun j _ => by rw [map_smul, hd0, smul_zero]\n    have hS1' : ∀ j, dotB (v j) (∑ j', b j' • v j') = b j := fun j => by\n      rw [map_sum]\n      simp only [map_smul, smul_eq_mul, hvv', mul_ite, mul_one, mul_zero]\n      rw [Finset.sum_ite_eq]\n      simp\n    have hSS : dotB (∑ j, b j • v j) (∑ j, b j • v j) = 1 := by\n      rw [LinearMap.map_sum₂, Finset.sum_congr rfl fun j _ =>\n        LinearMap.map_smul₂ dotB (b j) (v j) (∑ j', b j' • v j')]\n      simp only [smul_eq_mul, hS1']\n      rw [← hb]\n      exact Finset.sum_congr rfl fun j _ => (sq _).symm\n    have hf0 : f 0 = 1 := by\n      rw [hf, Pi.add_apply, hom_zero, Finset.sum_apply]\n      simp only [Pi.smul_apply, hv0, smul_zero, Finset.sum_const_zero, add_zero]\n    have ht0 : t 0 = 1 := by\n      rw [ht, Pi.add_apply, hom_zero, Pi.smul_apply, hv0, smul_zero, add_zero]\n    have hfL : Lor f := by\n      apply lor_of_dotB\n      · rw [hf0]; exact zero_le_one\n      · rw [hf0, hf, LinearMap.map_add₂, map_add, map_add, hd00, hS0', hS0, hSS]; norm_num\n    have htL : Lor t := by\n      apply lor_of_dotB\n      · rw [ht0]; exact zero_le_one\n      · rw [ht0]\n        simp only [ht, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul,\n          LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hvv',\n          eq_self_iff_true, if_true]\n        nlinarith [hs2]\n    have htN : homMap N t = t := by\n      rw [ht, map_add, map_smul, homMap_hom, map_zero, hvN]\n    have hR : 0 ≤ pairVal (hom (tperp z k)) f (G (tens (hom (tperp z l)) (Minv z G t))) :=\n      gate_pairVal_nonneg hpos hak (lor_hom (tperp_mem hz l)) hfL (lor_Minv hN hG htL)\n    have hsplit : pairVal (hom (tperp z k)) f (G (tens (hom (tperp z l)) (Minv z G t)))\n        = ∑ ν, t ν * f ν\n          + pairVal (hom (tperp z k)) f (G (tens (lift (tperp z l)) (Minv z G t))) := by\n      rw [hom_eq_add_lift (tperp z l), tens_add_left, map_add, pairVal_add_omega,\n        gt_center hN hG htN, pairVal_tens, dot_hom_hom_zero, one_mul]\n    rw [hsplit] at hR\n    change 0 ≤ dotB t f + Phi z G (hom (tperp z k)) (tperp z l) f t at hR\n    have hft : dotB t f = 1 + s * b i := by\n      simp only [ht, hf, LinearMap.map_add₂, map_add, LinearMap.map_smul₂, map_smul,\n        LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hd00, hd0, hd0', hS0', hS1'] <;> ring\n    have hΦ : Phi z G (hom (tperp z k)) (tperp z l) f t\n        = Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (hom 0)\n          + s * Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v i)\n          + (∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0)\n            + s * ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)) := by\n      rw [hf, ht, LinearMap.map_add₂, map_add, map_add, map_smul, map_smul, LinearMap.map_sum₂,\n        LinearMap.map_sum₂,\n        Finset.sum_congr rfl fun j _ =>\n          LinearMap.map_smul₂ (Phi z G (hom (tperp z k)) (tperp z l)) (b j) (v j) (hom 0),\n        Finset.sum_congr rfl fun j _ =>\n          LinearMap.map_smul₂ (Phi z G (hom (tperp z k)) (tperp z l)) (b j) (v j) (v i)]\n      simp only [smul_eq_mul]\n    have hΦ00 := Phi_center_all hN hG hcl hzl (hom (tperp z k))\n    have hsumsplit : ∑ j, b j * (Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v j)\n          + s * ((if j = i then (1 : ℝ) else 0) + Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)))\n        = ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0) + s * b i\n          + s * ∑ j, b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i) := by\n      have e : ∀ j, b j * (Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v j)\n          + s * ((if j = i then (1 : ℝ) else 0) + Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)))\n          = b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (hom 0)\n            + (if j = i then s * b j else 0)\n            + s * (b j * Phi z G (hom (tperp z k)) (tperp z l) (v j) (v i)) := by\n        intro j; rw [hsym k l j]; split_ifs <;> ring\n      rw [Finset.sum_congr rfl fun j _ => e j, Finset.sum_add_distrib, Finset.sum_add_distrib,\n        Finset.sum_ite_eq', ← Finset.mul_sum]\n      simp only [Finset.mem_univ, if_true]\n    rw [hsumsplit]\n    rw [hft, hΦ, hΦ00] at hR\n    linarith\n  · by_contra hcon\n    have hzero : ∀ r k l, Phi z G (hom (tperp z k)) (tperp z l) (hom 0) (v r) = 0 := by\n      intro r k l\n      by_contra h\n      exact hcon ⟨r, k, l, by simp only [Matrix.of_apply]; exact h⟩\n    obtain ⟨l, hl⟩ := exists_tperp_ne_zero hz hd\n    have hcl := tperp_le_one hz l\n    have hzl := tperp_dot_z hz l\n    obtain ⟨ω, hω⟩ : ∃ ω : W d, ω = G (tens (lift (tperp z l)) (Minv z G (hom 0))) := ⟨_, rfl⟩\n    have hMi0 : Minv z G (hom (0 : Fin d → ℝ)) ≠ 0 := by\n      intro h\n      have := Mfwd_Minv hN hG (hom (0 : Fin d → ℝ))\n      rw [h, map_zero] at this\n      exact hom_zero_ne_zero this.symm\n    have hlift : lift (tperp z l) ≠ 0 := by\n      intro h\n      apply hl\n      funext j\n      have := congrFun h j.succ\n      rwa [lift_succ, Pi.zero_apply] at this\n    have hωne : ω ≠ 0 := by\n      rw [hω]\n      intro h\n      exact tens_ne_zero hlift hMi0 (G.map_eq_zero_iff.mp h)\n    have hrow : ∀ μ, ω μ = 0 := by\n      intro μ\n      apply hspan (ω μ)\n      · rw [mem_tangentSpace]\n        constructor\n        · have h1 : actT N ω = ω := by\n            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]\n          exact congrFun h1 μ\n        · have h := Phi_center_all hN hG hcl hzl (bvec μ)\n          rw [Phi_apply, ← hω, pairVal_bvec, sum_row_hom_zero] at h\n          exact h\n      · intro r\n        have hk : ∀ k, pairVal (hom (tperp z k)) (v r) ω = 0 := by\n          intro k\n          have := hzero r k l\n          rw [hsym k l r, Phi_apply, ← hω] at this\n          exact this\n        have h0 : pairVal (hom 0) (v r) ω = 0 := by\n          have := Phi_hom_zero_eq_zero hN hG hcl hzl (v r) (hom 0)\n          rwa [Phi_apply, ← hω] at this\n        have hz' : pairVal (lift z) (v r) ω = 0 := by\n          have := Phi_lift_z_eq_zero hN hG hcl hzl (v r) (hom 0)\n          rwa [Phi_apply, ← hω] at this\n        have hb : ∀ μ', pairVal (bvec μ') (v r) ω = 0 := by\n          intro μ'\n          refine Fin.cases ?_ (fun k => ?_) μ'\n          · rw [bvec_zero_eq]; exact h0\n          · have hk' := hk k\n            rw [hom_eq_add_lift (tperp z k), lift_tperp, pairVal_add_left, h0, zero_add,\n              pairVal_sub_left, pairVal_smul_left, hz', mul_zero, sub_zero] at hk'\n            exact hk'\n        have := hb μ\n        rw [pairVal_bvec] at this\n        calc ∑ μ', v r μ' * ω μ μ' = ∑ ν, ω μ ν * v r ν :=\n              Finset.sum_congr rfl fun ν _ => mul_comm _ _\n          _ = 0 := this\n    exact hωne (funext hrow)",
 "copy#dim_of_nativeGate": "theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n    d = 1 ∨ d = 3 := by\n  have hpos := pos_of_isNot hN\n  rcases Nat.lt_or_ge d 2 with h | h\n  · left; omega\n  · have hsum := finrank_plus_add_finrank_minus hN.invol\n    have hbal := finrank_plus_eq_finrank_minus hN hG\n    have hp := one_le_finrank_plusSpace N\n    have hle := p_le_one_of_blockData (blockData_of_nativeGate h hN hG)\n    exact NativeGateBall.dim_of_bounds (tangentPlus N) (Module.finrank ℝ (minusSpace N) - 1) d hle\n      (by unfold tangentPlus; omega) (by unfold tangentPlus; omega)",
 "copy#gate_actC": "theorem gate_actC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (ω : W d) :\n    G (actC N ω) = actC N (actT N (G ω)) := by\n  have h2 := congrArg (actC N) (hG.relC ω)\n  rwa [actC_actC hN.invol] at h2",
 "copy#gate_corner": "theorem gate_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom z) Y) = tens (hom z) (Mfwd z G Y) :=\n  corner_form hN.unit\n    (fun b => by\n      have h := hG.frame 0 b\n      rw [corner_zero, zero_add] at h\n      exact h)\n    (fun x hx y hy => hG.posFwd x hx y hy) Y",
 "copy#gate_corner_neg": "theorem gate_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y)) := by\n  have hz' : homMap N (hom z) = hom (-z) := by rw [homMap_hom, hN.flips]\n  rw [← hz', ← actC_tens N (hom z) Y, gate_actC hN hG (tens (hom z) Y), gate_corner hN hG Y,\n    actT_tens N (hom z) (Mfwd z G Y), actC_tens N (hom z) (homMap N (Mfwd z G Y))]",
 "copy#gate_corner_symm": "theorem gate_corner_symm {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (Y : HVec d) :\n    G.symm (tens (hom z) Y) = tens (hom z) (Minv z G Y) :=\n  corner_form hN.unit\n    (fun b => by\n      have h := hG.frame 0 b\n      rw [corner_zero, zero_add] at h\n      calc G.symm (prodState z (corner z b)) = G.symm (G (prodState z (corner z b))) := by rw [h]\n        _ = prodState z (corner z b) := G.symm_apply_apply _)\n    (fun x hx y hy => hG.posInv x hx y hy) Y",
 "copy#gt_center": "theorem gt_center {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {t : HVec d}\n    (ht : homMap N t = t) : G (tens (hom 0) (Minv z G t)) = tens (hom 0) t := by\n  apply eq_of_two_smul_eq\n  rw [← map_smul, ← tens_smul_left 2 (hom 0) (Minv z G t), ← hom_add_hom_neg z, tens_add_left,\n    map_add, gt_corner hN hG,\n    gt_corner_neg hN hG, ht, ← tens_add_left, hom_add_hom_neg z, tens_smul_left]",
 "copy#gt_corner": "theorem gt_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom z) (Minv z G t)) = tens (hom z) t := by\n  rw [gate_corner hN hG, Mfwd_Minv hN hG]",
 "copy#gt_corner_neg": "theorem gt_corner_neg {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (t : HVec d) :\n    G (tens (hom (-z)) (Minv z G t)) = tens (hom (-z)) (homMap N t) := by\n  rw [gate_corner_neg hN hG, Mfwd_Minv hN hG]",
 "copy#gt_sphere": "theorem gt_sphere {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) {u : HVec d}\n    (hu0 : u 0 = 0) (hu : ∑ μ, u μ ^ 2 = 1) :\n    pairVal a (hom 0 - u) (G (tens (lift c) (Minv z G (hom 0 + u)))) = 0 := by\n  have hτ : ∑ j, Matrix.vecTail u j ^ 2 = 1 := by\n    rw [Fin.sum_univ_succ, hu0, zero_pow two_ne_zero, zero_add] at hu\n    exact hu\n  have hτ' : ∑ j, (-Matrix.vecTail u) j ^ 2 = 1 := by simpa [neg_sq] using hτ\n  have h1 : hom 0 + u = hom (Matrix.vecTail u) := by\n    rw [hom_eq_add_lift (Matrix.vecTail u), lift_vecTail hu0]\n  have h2 : hom 0 - u = hom (-Matrix.vecTail u) := by\n    rw [hom_eq_add_lift (-Matrix.vecTail u), lift_neg, lift_vecTail hu0, sub_eq_add_neg]\n  rw [h1, h2]\n  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,\n      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=\n    fun x hx y hy => hG.posFwd x hx y hy\n  let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom (-Matrix.vecTail u)) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ\n    tensR (Minv z G (hom (Matrix.vecTail u)))\n  have hF : ∀ X, F X = pairVal a (hom (-Matrix.vecTail u))\n      (G (tens X (Minv z G (hom (Matrix.vecTail u))))) := fun X => rfl\n  have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by\n    rw [hF]\n    exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hτ') (lor_Minv hN hG (lor_hom_of_unit hτ))\n  have h0 : F (hom z) = 0 := by\n    rw [hF, gt_corner hN hG, pairVal_tens, dot_hom_hom_neg hτ, mul_zero]\n  rw [← hF]\n  exact tangent_vanish F hFpos hN.unit hc hzc h0",
 "copy#gt_sphere_corner": "theorem gt_sphere_corner {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {a : HVec d} (ha : Lor a) :\n    pairVal a (hom z) (G (tens (lift c) (Minv z G (hom z)))) = 0 ∧\n    pairVal a (hom (-z)) (G (tens (lift c) (Minv z G (hom (-z))))) = 0 := by\n  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit\n  have hzc' : ∑ j, (-z) j * c j = 0 := by\n    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc, neg_zero]\n  have hNz : homMap N (hom z) = hom (-z) := by rw [homMap_hom, hN.flips]\n  have hNz' : homMap N (hom (-z)) = hom z := by rw [homMap_hom, map_neg, hN.flips, neg_neg]\n  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,\n      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=\n    fun x hx y hy => hG.posFwd x hx y hy\n  constructor\n  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom z) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G (hom z))\n    have hF : ∀ X, F X = pairVal a (hom z) (G (tens X (Minv z G (hom z)))) := fun X => rfl\n    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by\n      rw [hF]\n      exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hN.unit)\n        (lor_Minv hN hG (lor_hom_of_unit hN.unit))\n    have h0 : F (hom (-z)) = 0 := by\n      rw [hF, gt_corner_neg hN hG, hNz, pairVal_tens, dot_hom_neg_hom hN.unit, mul_zero]\n    rw [← hF]\n    exact tangent_vanish F hFpos hz' hc hzc' h0\n  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega a (hom (-z)) ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ\n      tensR (Minv z G (hom (-z)))\n    have hF : ∀ X, F X = pairVal a (hom (-z)) (G (tens X (Minv z G (hom (-z))))) := fun X => rfl\n    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by\n      rw [hF]\n      exact gate_pairVal_nonneg hpos ha hX (lor_hom_of_unit hz') (lor_Minv hN hG (lor_hom_of_unit hz'))\n    have h0 : F (hom (-z)) = 0 := by\n      rw [hF, gt_corner_neg hN hG, hNz', pairVal_tens, dot_hom_hom_neg hN.unit, mul_zero]\n    rw [← hF]\n    exact tangent_vanish F hFpos hz' hc hzc' h0",
 "copy#gt_tangent_corners": "theorem gt_tangent_corners {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {c : Fin d → ℝ}\n    (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) {f t : HVec d} (hf : Lor f) (ht : Lor t) :\n    pairVal (hom (-z)) f (G (tens (lift c) (Minv z G t))) = 0 ∧\n    pairVal (hom z) f (G (tens (lift c) (Minv z G t))) = 0 := by\n  have hzl : Lor (hom z) := lor_hom_of_unit hN.unit\n  have hz' : ∑ j, (-z) j ^ 2 = 1 := by simpa [neg_sq] using hN.unit\n  have hzc' : ∑ j, (-z) j * c j = 0 := by\n    simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib, hzc, neg_zero]\n  have hzl' : Lor (hom (-z)) := lor_hom_of_unit hz'\n  have hMt : Lor (Minv z G t) := lor_Minv hN hG ht\n  have hpos : ∀ x ∈ eball d, ∀ y ∈ eball d,\n      (G : W d →ₗ[ℝ] W d) (prodState x y) ∈ maxCone (eball d) :=\n    fun x hx y hy => hG.posFwd x hx y hy\n  constructor\n  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom (-z)) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)\n    have hF : ∀ X, F X = pairVal (hom (-z)) f (G (tens X (Minv z G t))) := fun X => rfl\n    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by\n      rw [hF]; exact gate_pairVal_nonneg hpos hzl' hX hf hMt\n    have h0 : F (hom z) = 0 := by\n      rw [hF, gt_corner hN hG, pairVal_tens, dot_hom_neg_hom hN.unit, zero_mul]\n    rw [← hF]\n    exact tangent_vanish F hFpos hN.unit hc hzc h0\n  · let F : HVec d →ₗ[ℝ] ℝ := pvOmega (hom z) f ∘ₗ (G : W d →ₗ[ℝ] W d) ∘ₗ tensR (Minv z G t)\n    have hF : ∀ X, F X = pairVal (hom z) f (G (tens X (Minv z G t))) := fun X => rfl\n    have hFpos : ∀ X, Lor X → 0 ≤ F X := fun X hX => by\n      rw [hF]; exact gate_pairVal_nonneg hpos hzl hX hf hMt\n    have h0 : F (hom (-z)) = 0 := by\n      rw [hF, gt_corner_neg hN hG, pairVal_tens, dot_hom_hom_neg hN.unit, zero_mul]\n    rw [← hF]\n    exact tangent_vanish F hFpos hz' hc hzc' h0",
 "copy#lor_Minv": "theorem lor_Minv {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) {Y : HVec d} (hY : Lor Y) :\n    Lor (Minv z G Y) :=\n  lor_cornerMap hN.unit (fun x hx y hy => hG.posInv x hx y hy) hY",
 "copy#not_entangling_one": "theorem not_entangling_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)}\n    {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) :\n    ¬ Entangling (eball 1) G := by\n  rintro ⟨x, hx, y, hy, -, hnp⟩\n  have hz : z 0 ^ 2 = 1 := by have := hN.unit; rwa [Fin.sum_univ_one] at this\n  obtain ⟨a, rfl⟩ := eq_corner_of_extreme hz hx\n  obtain ⟨b, rfl⟩ := eq_corner_of_extreme hz hy\n  apply hnp\n  rw [hG.frame a b]\n  exact ⟨corner z a, corner_mem_one hz a, corner z (a + b), corner_mem_one hz _, rfl⟩",
 "copy#three_of_nativeGate": "theorem three_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)\n    (hE : Entangling (eball d) G) : d = 3 := by\n  rcases dim_of_nativeGate hN hG with hone | hthree\n  · exfalso\n    subst hone\n    exact not_entangling_one hN hG hE\n  · exact hthree",
 "dim_of_nativeGate": "theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d = 1 ∨ d = 3",
 "homMap_n5_sign": "theorem homMap_n5_sign (v : HVec 5) (μ : Fin (5 + 1)) : homMap n5 v μ = (if odd5 μ then -1 else 1) * v μ",
 "isNot_n5": "theorem isNot_n5 : IsNot (eball 5) z5 n5",
 "n5": "def n5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign c5",
 "nativeGate#names": "Lop_anti Lop_eq_zero Lop_injective Mfwd_Minv Mfwd_homMap Minv_Mfwd Minv_homMap NativeGate Phi_center Phi_center_all Phi_hom_zero_eq_zero Phi_lift_z_eq_zero Phi_sphere blockData_of_nativeGate blockData_of_orthonormal det_of_nativeGate_three dim1_core dim_of_nativeGate finrank_plus_eq_finrank_minus gateRel_of_nativeGate gate_actC gate_actT gate_corner gate_corner_neg gate_corner_symm gt_center gt_corner gt_corner_neg gt_sphere gt_sphere_corner gt_tangent_corners k2guard_entangling k2guard_orientation lor_Minv nativeGate_cnot nativeGate_cnot1 nativeGate_of_avail nativeGate_of_avail_dense nativeGate_of_cone_eq ne_five_of_nativeGate ne_four_of_nativeGate ne_seven_of_nativeGate ne_two_of_nativeGate no_gate_four not_entangling_one not_even_of_nativeGate not_nativeGate_gJ3 not_nativeGate_gJ5 not_nativeGate_gRev opGate_comp_homMap opGate_homMap_comp piRotation_of_nativeGate_three tangentPlus_of_nativeGate_three three_of_nativeGate three_of_nativeGate_of_two_le two_le_load_bearing two_le_of_entangling two_le_satisfiable",
 "nativeGate_cnot": "theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot",
 "nativeGate_cnot1": "theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1",
 "not_entangling_one": "theorem not_entangling_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 → ℝ)} {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) : ¬ Entangling (eball 1) G",
 "not_even_of_balanced": "theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) : ¬ Even d",
 "odd5": "def odd5 : Fin 6 → Bool | 0 => false | 1 => false | 2 => false | 3 => true | 4 => true | 5 => true",
 "three_of_nativeGate": "theorem three_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) (hE : Entangling (eball d) G) : d = 3",
 "x5": "def x5 : Fin 5 → ℝ := fun i => if i = 0 then 1 else 0",
 "z5": "def z5 : Fin 5 → ℝ := fun i => if i = 4 then 1 else 0"
}''')
N_PRINTS = json.loads(r'''{"RelcSelectParity": 2, "RelcSelectBlock": 5, "RelcSelectSqueeze": 15, "RelcSelectC5": 12}''')
EARNED = json.loads(r'''[
 "The target relation relT is unnecessary for the dimension selector. Under IsNot, the frame, both positivity clauses and the control relation relC, the dimension is 1 or 3. The control relation alone already forces odd dimension. Neither positivity clause can be dropped individually: explicit d = 5 gates satisfy all remaining clauses while violating one positivity direction.",
 "This round does not establish that the frame is necessary or unnecessary, and therefore does not claim a globally minimal hypothesis set. It establishes minimality only with respect to the audited relation and positivity clauses."
]''')
NONINF = json.loads(r'''[
 "CtrlGate is the hypothesis of the dimension selector only. This round does not show that relT is redundant in NativeGate or in GateRel, that relT follows from the remaining clauses, or that every CtrlGate is a NativeGate: NativeGate, GateRel and every landed statement over them are unchanged, and relT remains a field of both. It does not show that the control relation of a gate gives the control relation of its inverse: the transfer used for the inverse of the squeezed gate, relC_symm_of_relT, reads the target relation as well. Its countermodel for the control relation uses the witness NOT nC5, whose homogenized map has two indices of sign +1 and four of sign −1; it does not decide whether the target relation, the frame and two-sided positivity select the dimension for a NOT whose two homogenized eigenspaces have equal dimension, such as PARITY-NOT-1's n5. The squeezed gate, its inverse, nC5 and gC5 are mathematical countermodels for the clauses they separate; they are not postulates, adopted models, or a NOT or a gate of a physical theory, and the orthogonal complex structures J and K in the proof of gC5's positivity are tools of that proof. The selector concerns two copies of the Euclidean ball under the stated hypotheses; the round does not claim that OI selects a dimension, adopts no premise, and makes no manuscript claim and no ROADMAP claim."
]''')

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

IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'


def stmt_parts(texts, name):
    b, c = split_statement(texts.get(name, ''))
    return norm(b), norm(c)


def def_body(text):
    j = text.find(' :=')
    return norm(text[j + 3:]) if j != -1 else ''


def groups(b):
    """The top-level bracketed binder groups of a binder string, in order."""
    out, depth, start = [], 0, None
    for i, c in enumerate(b):
        if c in BINDER_OPEN:
            if depth == 0:
                start = i
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
            if depth == 0 and start is not None:
                out.append(norm(b[start:i + 1]))
                start = None
    return out


def group_names(g):
    """The bound names of a binder group (none for an anonymous instance group)."""
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """[(position, variable groups in scope, namespaces in scope, opened namespaces in scope)] at each declaration."""
    stack = [([], [], [])]
    out = {}
    lines = text.split('\n')
    pos = 0
    k = 0
    decl_at = {m.start(): m.group(2) for m in DECL.finditer(text)}
    while k < len(lines):
        line = lines[k]
        block = [line]
        j = k + 1
        if line.startswith('variable') or line.startswith('open '):
            while j < len(lines) and lines[j].startswith('  '):
                block.append(lines[j])
                j += 1
        whole = '\n'.join(block)
        m = re.match(r'^(namespace|section|noncomputable section)\b\s*(\S*)', line)
        if m:
            stack.append(([], [m.group(2)] if m.group(1) == 'namespace' else [], []))
        elif re.match(r'^end\b', line):
            if len(stack) > 1:
                stack.pop()
        elif line.startswith('variable'):
            stack[-1][0].extend(groups(whole[len('variable'):]))
        elif line.startswith('open '):
            stack[-1][2].extend(whole[len('open '):].split())
        if pos in decl_at:
            vs = [g for s in stack for g in s[0]]
            nss = [n for s in stack for n in s[1]]
            ops = [o for s in stack for o in s[2]]
            out[decl_at[pos]] = (vs, nss, ops)
        for l in block:
            pos += len(l) + 1
        k = j
    return out


def effective(text, name):
    """The effective statement of a declaration: the section variables its statement uses (closed under use by the
    included groups, an instance group included with a variable it mentions), in declared order, then its own binders
    and conclusion. None when the declaration is absent."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    vs = scopes_at(text).get(name, ([], [], []))[0]
    b, c = split_statement(stmt)
    used = norm(b) + ' : ' + norm(c)
    inc = [False] * len(vs)
    changed = True
    while changed:
        changed = False
        hay = used + ' ' + ' '.join(g for g, i in zip(vs, inc) if i)
        for n, g in enumerate(vs):
            if inc[n]:
                continue
            names = group_names(g)
            if names and any(token(x, hay) for x in names):
                inc[n] = True
                changed = True
            elif not names and g.startswith('[') and any(token(x, g) for gg, i in zip(vs, inc) if i
                                                          for x in group_names(gg)):
                inc[n] = True
                changed = True
    pre = ' '.join(g for g, i in zip(vs, inc) if i)
    return norm(pre + ' ' + norm(b) + ' : ' + norm(c))


_INV_CACHE = {}


def inventory(files):
    """{fully qualified name} of every declaration in the given module texts, with the namespaces they declare."""
    names, spaces = set(), set()
    for text in files:
        if text in _INV_CACHE:
            n, sp = _INV_CACHE[text]
            names |= n
            spaces |= sp
            continue
        n, sp = inventory_one(text)
        if len(_INV_CACHE) < 4096:
            _INV_CACHE[text] = (n, sp)
        names |= n
        spaces |= sp
    return names, spaces


def inventory_one(text):
    names, spaces = set(), set()
    for text in [text]:
        sc = scopes_at(text)
        for kind, name in decls(text):
            nss = sc.get(name, ([], [], []))[1]
            prefix = '.'.join(nss)
            names.add((prefix + '.' if prefix else '') + name)
            for i in range(1, len(nss) + 1):
                spaces.add('.'.join(nss[:i]))
    return names, spaces


def visible(nss, ops, spaces):
    """The namespaces whose members are in scope: every prefix of the current namespace, and each opened namespace,
    resolved against the current namespace prefixes when that names an OIBridge namespace."""
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
    """Index of the first colon at bracket depth 0 that is not part of `:=`."""
    depth = 0
    for j, c in enumerate(s):
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and s[j:j + 2] != ':=':
            return j
    return len(s)


def strip_binders(eff):
    """The identifiers of an effective statement, without the names it binds: the names of its binder groups and the
    names bound by `∃`, `∀` and `fun` in its conclusion."""
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]

PREFIX = 'OIBridge.RelcSelect.'
CD = LEAN + 'CompositeDimension.lean'
PN = LEAN + 'ParityNot.lean'
GATE_FIELDS = ('frame', 'posFwd', 'posInv', 'relT', 'relC')
DOTTED = ('posFwd', 'posInv', 'relT', 'relC', 'frame')
PAR, BLK, SQZ, C5 = MODULES
# the landed objects the rules read (other than NativeGate's and GateRel's fields), read from D
LANDED_CD_THMS = ('dim_of_nativeGate', 'three_of_nativeGate', 'not_entangling_one', 'blockData_of_nativeGate',
                  'nativeGate_cnot1', 'nativeGate_cnot', 'not_even_of_balanced')
LANDED_PN_DEFS = ('odd5', 'c5', 'n5', 'z5', 'x5')
LANDED_PN_THMS = ('isNot_n5', 'homMap_n5_sign')
# PARITY-NOT-1's NOT n5 and the points of eball 5 the squeezed witness reads, as landed at D
LANDED_N5 = {
    'odd5': 'def odd5 : Fin 6 → Bool | 0 => false | 1 => false | 2 => false | 3 => true | 4 => true | 5 => true',
    'c5': 'def c5 (j : Fin 5) : ℝ := if odd5 j.succ then -1 else 1',
    'n5': 'def n5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign c5',
    'z5': 'def z5 : Fin 5 → ℝ := fun i => if i = 4 then 1 else 0',
    'x5': 'def x5 : Fin 5 → ℝ := fun i => if i = 0 then 1 else 0',
    'isNot_n5': 'theorem isNot_n5 : IsNot (eball 5) z5 n5',
    'homMap_n5_sign': 'theorem homMap_n5_sign (v : HVec 5) (μ : Fin (5 + 1)) : homMap n5 v μ = '
                      '(if odd5 μ then -1 else 1) * v μ'}
# the landed dimension corollaries of the native gate; no declaration of the round names one
LANDED_SELECTORS = ('dim_of_nativeGate', 'dim_of_nativeGateOf', 'dim_of_nativeGateOf_dense', 'ne_two_of_nativeGate',
                    'ne_four_of_nativeGate', 'ne_five_of_nativeGate', 'ne_seven_of_nativeGate',
                    'not_even_of_nativeGate', 'three_of_nativeGate', 'three_of_nativeGate_of_two_le',
                    'three_of_nativeGateOf', 'three_of_nativeGateOf_dense', 'three_of_nativeGateOf_of_two_le',
                    'three_of_nativeGateOf_of_two_le_dense', 'det_of_nativeGate_three',
                    'piRotation_of_nativeGate_three', 'tangentPlus_of_nativeGate_three')
# the landed objects that read `relT`, by name; neither the parity module nor the block module names one
RELT_READERS = ('relT', 'GateRel', 'gate_actT', 'Mfwd_homMap', 'Minv_homMap', 'Minv_Mfwd', 'opGate_comp_homMap',
                'opGate_comp_homMap_rel', 'Lop_eq_zero', 'Lop_injective', 'finrank_plus_eq_finrank_minus',
                'finrank_plus_eq_finrank_minus_rel', 'gateRel_of_nativeGate', 'not_even_of_gateRel')

# --- S1: parity from the control relation (RelcSelectParity) ---
PAR_THM, PAR_ODD = 'finrank_plus_eq_finrank_minus_relC', 'not_even_of_relC'
PAR_BINDERS = ('{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
               '(hN : IsNot (eball d) z N) (hC : %s)')
PAR_CONCL = 'Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)'
PAR_PROOF = ('opGate_injective_relC', 'opGate_homMap_comp_relC', 'finrank_ker_sub_le_relC', 'finrank_ker_add_le_relC',
             'finrank_ker_relCLeft_sub', 'finrank_ker_relCLeft_add', 'finrank_ker_relCConj_sub_le',
             'finrank_ker_relCConj_add_le', 'balance_of_bounds_relC')
PAR_ODD_PROOF = ('not_even_of_balanced', PAR_THM)
LANDED_BALANCED = 'theorem not_even_of_balanced {a b : ℕ} (hsum : a + b = d + 1) (hbal : a = b) : ¬ Even d'
# the parity module reads none of these
PAR_FREE = RELT_READERS + ('NativeGate', 'CtrlGate', 'frame', 'posFwd', 'posInv', 'maxCone', 'prodEffVal',
                           'IsEffectOn', 'sharpEff', 'corner', 'prodState', 'Entangling')

# --- S2: the selector without the target relation (RelcSelectBlock) ---
CTRL = 'CtrlGate'
CTRL_FIELDS = ['frame', 'posFwd', 'posInv', 'relC']
CTRL_OF_NATIVE = ('theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} '
                  '{N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) : '
                  'CtrlGate Ω z N G')
SLICE = ('theorem actT_slice_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} '
         '(hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) '
         '(hzc : ∑ j, z j * c j = 0) : actT N (G (tens (lift c) (Minv z G (hom 0)))) = '
         'G (tens (lift c) (Minv z G (hom 0)))')
SEL_FROM = {'blockData_of_ctrlGate': 'blockData_of_nativeGate', 'not_entangling_one_ctrl': 'not_entangling_one',
            'dim_of_ctrlGate': 'dim_of_nativeGate', 'three_of_ctrlGate': 'three_of_nativeGate'}
SEL_PROOF = {'dim_of_ctrlGate': (PAR_THM, 'blockData_of_ctrlGate'),
             'three_of_ctrlGate': ('dim_of_ctrlGate', 'not_entangling_one_ctrl'),
             'blockData_of_ctrlGate': ('blockData_of_orthonormal_ctrl',),
             'blockData_of_orthonormal_ctrl': ('actT_slice_ctrl',),
             'actT_slice_ctrl': ('phi_minusSpace_ctrl', 'homMap_eq_self_of_orth_minusSpace')}
ENTANGLING_ONLY = ('not_entangling_one_ctrl', 'three_of_ctrlGate')
ATTAIN = {'nativeGate_cnot1': 'theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1',
          'nativeGate_cnot': 'theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot'}
# the copy: each declaration of DIM-1's §Q the block module restates, its name there, and the two line edits
COPY_MAP = {
    'gate_corner': 'gate_corner_ctrl', 'gate_corner_symm': 'gate_corner_symm_ctrl', 'Mfwd_Minv': 'Mfwd_Minv_ctrl',
    'lor_Minv': 'lor_Minv_ctrl', 'gate_actC': 'gate_actC_ctrl', 'gate_corner_neg': 'gate_corner_neg_ctrl',
    'gt_corner': 'gt_corner_ctrl', 'gt_corner_neg': 'gt_corner_neg_ctrl', 'gt_center': 'gt_center_ctrl',
    'gt_tangent_corners': 'gt_tangent_corners_ctrl', 'gt_sphere': 'gt_sphere_ctrl',
    'gt_sphere_corner': 'gt_sphere_corner_ctrl', 'Phi_sphere': 'Phi_sphere_ctrl', 'Phi_center': 'Phi_center_ctrl',
    'Phi_center_all': 'Phi_center_all_ctrl', 'Phi_hom_zero_eq_zero': 'Phi_hom_zero_eq_zero_ctrl',
    'Phi_lift_z_eq_zero': 'Phi_lift_z_eq_zero_ctrl', 'blockData_of_orthonormal': 'blockData_of_orthonormal_ctrl',
    'blockData_of_nativeGate': 'blockData_of_ctrlGate', 'not_entangling_one': 'not_entangling_one_ctrl',
    'dim_of_nativeGate': 'dim_of_ctrlGate', 'three_of_nativeGate': 'three_of_ctrlGate'}
COPY_RENAME = dict(COPY_MAP, NativeGate='CtrlGate')
COPY_EDITS = {
    'blockData_of_orthonormal_ctrl': [(
        '            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]',
        '            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl')],
    'dim_of_ctrlGate': [(
        '    have hbal := finrank_plus_eq_finrank_minus hN hG',
        '    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC')]}
COPY_NEW = ('CtrlGate', 'ctrlGate_of_nativeGate', 'gt_center_two_ctrl', 'phi_lift_minus_ctrl',
            'phi_bvec_minus_unit_ctrl', 'phi_minusSpace_ctrl', 'homMap_eq_self_of_orth_minusSpace', 'actT_slice_ctrl')
HEADL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:private\s+|protected\s+)?"
                   r"(theorem|lemma|def|abbrev|structure|instance|class|inductive)\s+([A-Za-z_][A-Za-z0-9_'.]*)")

# --- S3: the two positivity clauses one at a time (RelcSelectSqueeze) ---
SQ_DEFS = {
    'sqCls': 'def sqCls : Fin 6 → Bool | 0 => true | 1 => false | 2 => false | 3 => false | 4 => false | 5 => true',
    'sqSig': 'def sqSig : Fin 6 → Fin 6 | 0 => 1 | 1 => 0 | 2 => 2 | 3 => 5 | 4 => 4 | 5 => 3',
    'sqPc': 'def sqPc (m n : Fin 6) : Fin 6 := if odd5 n then perm5 m else m',
    'sqPt': 'def sqPt (m n : Fin 6) : Fin 6 := if sqCls m then n else sqSig n',
    'sqR': 'noncomputable def sqR (m : Fin 6) : ℝ := if sqCls m then 1 else 1 / 10',
    'sqK': 'noncomputable def sqK (n : Fin 6) : ℝ := if sqCls n then 1 else 1 / 2',
    'sqW': 'noncomputable def sqW (m n : Fin 6) : ℝ := sqR m * sqK (sqPt m n)',
    'sqWi': 'noncomputable def sqWi (m n : Fin 6) : ℝ := (if sqCls m then 1 else 10) * (if sqCls n then 1 else 2)',
    'gSqFun': 'noncomputable def gSqFun (ω : W 5) : W 5 := fun m n => sqW m n * ω (sqPc m n) (sqPt m n)',
    'gSqInvFun': 'noncomputable def gSqInvFun (ω : W 5) : W 5 := fun m n => sqWi m n * ω (sqPc m n) (sqPt m n)'}
SQ_GATE_HEAD = 'noncomputable def gSq : W 5 ≃ₗ[ℝ] W 5 where toFun := gSqFun invFun := gSqInvFun'
SQ_VALUE = 'prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2'
GRD = '{Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}'

# --- S4: the control relation is not replaced by the target relation (RelcSelectC5) ---
C5_DEFS = {
    'oddC5': 'def oddC5 : Fin 6 → Bool | 0 => false | 1 => false | 2 => true | 3 => true | 4 => true | 5 => true',
    'cC5': 'def cC5 (j : Fin 5) : ℝ := if oddC5 j.succ then -1 else 1',
    'nC5': 'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5',
    'sgnC5': 'def sgnC5 (μ ν : Fin 6) : ℝ := if ((μ = 1 ∨ μ = 3) ∧ (ν = 4 ∨ ν = 5)) ∨ ((μ = 2 ∨ μ = 4) ∧ '
             '(ν = 2 ∨ ν = 3)) then -1 else 1',
    'gC5Fun': 'def gC5Fun (ω : W 5) : W 5 := fun μ ν => sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)'}
C5_TABLES = ('pcC5', 'ptC5')
C5_GATE_HEAD = 'def gC5 : W 5 ≃ₗ[ℝ] W 5 where toFun := gC5Fun invFun := gC5Fun'

# --- S6/S7/S9 ---
D_EQ = re.compile(r'(?<![\w.\'])d\s*(=|≠)\s*\d')
D_EQ_ALLOWED = ('dim_of_ctrlGate', 'three_of_ctrlGate', 'relT_not_dimension_selecting')
SCOPE_TOKENS = ('Complex', 'ℂ') + LANDED_SELECTORS
IMPORTS_OF = {PAR: ['import OIBridge.OddChar'], BLK: ['import OIBridge.RelcSelectParity', 'import OIBridge.ParityNot'],
              SQZ: ['import OIBridge.OddChar'], C5: ['import OIBridge.OddChar']}

# --- S8: the frozen phrases (case-insensitive, backticks removed, whitespace-normalized) ---
PHRASES = (
    # the target relation is not globally redundant; CtrlGate leaves the gate theory as it is
    'redundan', 'superfluous', 'relT is unnecessary', 'relT is not needed', 'relT is never needed',
    'relT plays no role', 'relT can be dropped', 'relT can be removed', 'relT may be dropped', 'drop relT',
    'remove relT', 'removes relT from NativeGate', 'relT is derivable', 'relT is derived', 'relT follows from',
    'relT is implied', 'implies relT', 'derivable from the remaining', 'relT is independent',
    'independent of the remaining', 'equivalent to NativeGate', 'NativeGate is equivalent', 'CtrlGate is equivalent',
    'CtrlGate implies NativeGate', 'every CtrlGate is a NativeGate', 'replaces NativeGate', 'without loss of generality',
    # the control relation is not claimed inverse-stable on its own
    'inverse-stable', 'inverse stable', 'stable under inversion', 'stable under inverses', 'preserved under inversion',
    'preserved by inversion', 'invariant under inversion', 'closed under inversion', 'relC alone transfers',
    'relC transfers to the inverse on its own', 'without relT, relC', 'relC of G.symm follows from relC of G',
    # the control relation is not replaced by the target relation
    'relT can replace relC', 'relT replaces relC', 'relC can be replaced', 'relC is replaceable', 'relT suffices',
    'relT is sufficient', 'relT alone',
    # each positivity clause is read
    'one positivity clause suffices', 'either positivity clause suffices', 'posFwd alone suffices',
    'posInv alone suffices', 'forward positivity alone suffices', 'inverse positivity alone suffices',
    'forward positivity implies inverse positivity', 'inverse positivity implies forward positivity',
    'posFwd implies posInv', 'posInv implies posFwd',
    # the witnesses are witnesses
    'physical gate', 'physical NOT', 'physically realizable', 'physically realized', 'physically carried',
    'physical postulate', 'physical model', 'adopted model', 'adopts a premise', 'premise adopted', 'new postulate',
    'as a postulate', 'is a postulate', 'postulated', 'OI supplies', 'OI provides', 'derived from OI', 'OI selects',
    # minimality only with respect to the audited clauses; the frame is not audited
    'globally minimal', 'minimal hypothesis set', 'minimal set of hypotheses', 'the frame is necessary',
    'the frame is unnecessary', 'the frame is load-bearing', 'the frame is not needed', 'the frame can be dropped',
    'irreducible', 'independent axioms',
    # the selector concludes d = 1 ∨ d = 3; the entangling clause excludes d = 1
    'CtrlGate gives d = 3', 'CtrlGate forces d = 3', 'selects d = 3', 'forces d = 3 without',
    # design leftovers
    'design (round', 'not for landing', 'UNBUILT', 'not been compiled', 'not been checked by the kernel',
    'design module')

# --- V: the frozen decision rule ---
PAR_TOKENS = ('RELC-PARITY-PROVED', 'RELC-PARITY-NOT-ESTABLISHED')
SEL_TOKENS = ('CTRL-SELECTOR-PROVED', 'CTRL-SELECTOR-NOT-ESTABLISHED')
POS_TOKENS = ('POSITIVITY-SEPARATION-PROVED', 'POSITIVITY-SEPARATION-NOT-ESTABLISHED')
REL_TOKENS = ('RELT-NOT-DIMENSION-SELECTING-PROVED', 'RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED')
ALL_TOKENS = PAR_TOKENS + SEL_TOKENS + POS_TOKENS + REL_TOKENS


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def tsub(text, mapping):
    """Token-bounded simultaneous substitution."""
    pat = re.compile(r'(?<![\w.\'])(%s)(?![\w\'])' % '|'.join(re.escape(k) for k in
                                                           sorted(mapping, key=len, reverse=True)))
    return pat.sub(lambda m: mapping[m.group(1)], text)


def kinds_texts_proofs(mod):
    chunks = decl_chunks(mod or '')
    return ({n: k for n, (k, _, _) in chunks.items()}, {n: c for n, (_, c, _) in chunks.items()},
            {n: p for n, (_, _, p) in chunks.items()})


def qualified(name, c):
    """`name` referenced through a namespace (`CompositeDimension.gate_actT`)."""
    return re.search(r'(?<![\w.\'])[A-Z][\w\']*(?:\.[\w\']+)*\.%s(?![\w\'])' % re.escape(name), c) is not None


def mentions(text, toks):
    """The tokens the code of `text` mentions, also through a namespace; a gate field also as a projection
    (`hG.posInv`)."""
    c = code_only(text)
    return [t for t in toks if token(t, c) or qualified(t, c)
            or (t in DOTTED and re.search(r'(?<![\w\'])%s(?![\w\'])' % t, c))]


def body_of(landed, owner, f):
    v = landed.get('%s#%s' % (owner, f))
    p = f + ' : '
    return v[len(p):] if v is not None and v.startswith(p) else None


def on_body(field, gate, body):
    """A landed positivity field at the gate `gate` on the body `body`."""
    s = tsub(field, {'G': gate, 'Ω': '(%s)' % body})
    return s.replace('∈ (%s),' % body, '∈ %s,' % body)


def relations_bad(landed):
    """The landed GateRel is exactly the landed NativeGate relation fields."""
    bad = []
    for f in ('relT', 'relC'):
        a = landed.get('GateRel#' + f)
        if a is None or a != landed.get('NativeGate#' + f):
            bad.append('GateRel#' + f + ' at D')
    if landed.get('GateRel#fields') != 'relT relC':
        bad.append('GateRel fields at D')
    return bad


def thm_bad(kinds, texts, proofs, n, b, c, deps=()):
    bb, cc = split_statement(texts.get(n, ''))
    return kinds.get(n) != 'theorem' or b is None or c is None or norm(bb) != norm(b) or norm(cc) != norm(c) or \
        not all(token(m, proofs.get(n, '')) for m in deps)


def stmt_eq(texts, n, want):
    return want is not None and norm(texts.get(n, '')) == norm(want)


def free_bad(mod, toks, allow=()):
    bad = []
    for kind, name, start, se, nxt, cend in spans(mod or ''):
        if name not in allow and mentions(mod[start:nxt], toks):
            bad.append(name)
    return bad


def nativegate_names_bad(mod, landed, allow=()):
    """No declaration names a landed declaration whose statement takes the native gate."""
    names = set((landed.get('nativeGate#names') or '').split())
    bad = []
    for kind, name, start, se, nxt, cend in spans(mod or ''):
        if name in allow:
            continue
        refs = set()
        for t in IDENT.findall(code_only(mod[start:nxt])):
            refs.add(t)
            if '.' in t and t[0].isupper():
                refs.add(t.split('.')[-1])
        if (refs & names) - {'NativeGate'}:
            bad.append(name)
    return bad


def parity_bad(mods, landed):
    """S1: from IsNot and the landed relC field alone, equal eigenspace dimensions and ¬ Even d; the parity module
    reads neither relT, the frame, positivity, GateRel nor any landed statement over the native gate."""
    mod = mods.get(PAR)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    relc = body_of(landed, 'NativeGate', 'relC')
    b = None if relc is None else PAR_BINDERS % relc
    if thm_bad(kinds, texts, proofs, PAR_THM, b, PAR_CONCL, PAR_PROOF):
        bad.append(PAR_THM)
    if thm_bad(kinds, texts, proofs, PAR_ODD, b, '¬ Even d', PAR_ODD_PROOF):
        bad.append(PAR_ODD)
    if landed.get('not_even_of_balanced') != norm(LANDED_BALANCED):
        bad.append('not_even_of_balanced at D')
    bad += free_bad(mod, PAR_FREE)
    bad += nativegate_names_bad(mod, landed)
    return bad


def line_decls(text):
    """name -> the declaration's lines: its head line and every following line up to the next unindented line."""
    lines = (text or '').split('\n')
    heads = [(i, HEADL.match(l).group(2)) for i, l in enumerate(lines) if HEADL.match(l)]
    out = {}
    for i, name in heads:
        j = i + 1
        while j < len(lines) and not (lines[j] and not lines[j][0].isspace()):
            j += 1
        body = lines[i:j]
        while body and not body[-1].strip():
            body.pop()
        out[name] = None if name in out else body
    return out


def copy_bad(mod, landed):
    """Every copied declaration is the landed one under the frozen renaming, except the two frozen line edits; the
    module declares nothing else but the frozen new declarations."""
    md = line_decls(mod)
    bad = []
    for old, new in COPY_MAP.items():
        got, src = md.get(new), landed.get('copy#' + old)
        if got is None or src is None:
            bad.append(new)
            continue
        exp = [tsub(l, COPY_RENAME) for l in src.split('\n')]
        allowed, used, ok = list(COPY_EDITS.get(new, [])), [], len(exp) == len(got)
        for e, g in zip(exp, got):
            if e != g:
                if (e, g) in allowed and (e, g) not in used:
                    used.append((e, g))
                else:
                    ok = False
        if not ok or len(used) != len(allowed):
            bad.append(new)
    if sorted(md) != sorted(list(COPY_MAP.values()) + list(COPY_NEW)):
        bad.append('the module declares other declarations')
    return bad


def selector_bad(mods, landed):
    """S2: CtrlGate is the landed NativeGate without relT, field for field; IsNot and CtrlGate give the landed
    selector's conclusion, and with Entangling d = 3 through the frame-only exclusion of d = 1; the copy is the
    landed proof under the frozen renaming; the parity step is S1's theorem; neither module reads relT."""
    mod = mods.get(BLK)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    hdr = landed.get('NativeGate#header')
    if kinds.get(CTRL) != 'structure' or hdr is None or \
            norm(def_header(texts.get(CTRL, ''))) != tsub(hdr, {'NativeGate': CTRL}) or \
            fields(texts.get(CTRL, '')) != CTRL_FIELDS or \
            landed.get('NativeGate#fields') != ' '.join(GATE_FIELDS) or \
            any(field_line(texts.get(CTRL, ''), f) is None or
                field_line(texts.get(CTRL, ''), f) != landed.get('NativeGate#' + f) for f in CTRL_FIELDS):
        bad.append(CTRL)
    if not stmt_eq(texts, 'ctrlGate_of_nativeGate', CTRL_OF_NATIVE):
        bad.append('ctrlGate_of_nativeGate')
    if not stmt_eq(texts, 'actT_slice_ctrl', SLICE):
        bad.append('actT_slice_ctrl')
    for new, old in SEL_FROM.items():
        lt = landed.get(old)
        if kinds.get(new) != 'theorem' or lt is None or \
                not stmt_eq(texts, new, tsub(lt, {'NativeGate': CTRL, old: new})):
            bad.append(new)
    for n, deps in SEL_PROOF.items():
        if not all(token(m, proofs.get(n, '')) for m in deps):
            bad.append(n + ' proof')
    for n, want in ATTAIN.items():
        if landed.get(n) != norm(want):
            bad.append(n + ' at D')
    bad += copy_bad(mod, landed)
    bad += free_bad(mod, RELT_READERS)
    bad += free_bad(mod, ('NativeGate',), allow=('ctrlGate_of_nativeGate',))
    bad += nativegate_names_bad(mod, landed)
    bad += free_bad(mod, ('Entangling',), allow=ENTANGLING_ONLY)
    # the parity step the selector cites: S1's statement, and the parity module free of relT
    pk, pt, pp = kinds_texts_proofs(mods.get(PAR))
    relc = body_of(landed, 'NativeGate', 'relC')
    if relc is None or thm_bad(pk, pt, pp, PAR_THM, PAR_BINDERS % relc, PAR_CONCL):
        bad.append(PAR_THM + ' (parity step)')
    if free_bad(mods.get(PAR), RELT_READERS) or nativegate_names_bad(mods.get(PAR), landed):
        bad.append('the parity module reads relT')
    return bad


def sq_conj(landed, gate, inverse):
    """The frozen conclusion of gSq_sep (inverse = False) or gSqInv_sep (inverse = True), from the landed fields."""
    frame, pf, pi = (body_of(landed, 'NativeGate', f) for f in ('frame', 'posFwd', 'posInv'))
    if None in (frame, pf, pi):
        return None
    fr = tsub(frame, {'G': gate, 'z': 'z5'})
    f5, i5 = on_body(pf, gate, 'eball 5'), on_body(pi, gate, 'eball 5')
    if inverse:
        i5 = i5.replace('gSq.symm.symm', 'gSq')
        return 'IsNot (eball 5) z5 n5 ∧ (%s) ∧ GateRel n5 %s ∧ (%s) ∧ ¬ (%s)' % (fr, gate, i5, f5)
    return 'IsNot (eball 5) z5 n5 ∧ (%s) ∧ GateRel n5 %s ∧ (%s) ∧ ¬ (%s)' % (fr, gate, f5, i5)


def positivity_bad(mods, landed):
    """S3: at d = 5 with the landed n5 and z5, gSq has the landed frame, GateRel and the landed posFwd field and
    fails the landed posInv field through the value -1 / 2; gSq.symm has the frame, GateRel and the landed posInv
    field and fails the landed posFwd field; the transfer of relC to the inverse takes relT."""
    mod = mods.get(SQZ)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in SQ_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    if not norm(texts.get('gSq', '')).startswith(SQ_GATE_HEAD):
        bad.append('gSq')
    frame, pf, pi, rt, rc = (body_of(landed, 'NativeGate', f) for f in GATE_FIELDS)
    if None in (frame, pf, pi, rt, rc):
        return bad + ['NativeGate fields at D']
    rows = {
        'gSq_frame': ('(a b : Fin 2)', tsub(frame.split(', ', 1)[1], {'G': 'gSq', 'z': 'z5'}), ()),
        'gSq_relT': ('', tsub(rt, {'N': 'n5', 'G': 'gSq'}), ()),
        'gSq_relC': ('', tsub(rc, {'N': 'n5', 'G': 'gSq'}), ()),
        'gateRel_gSq': ('', 'GateRel n5 gSq', ('gSq_relT', 'gSq_relC')),
        'gSq_posFwd': ('', on_body(pf, 'gSq', 'eball 5'), ('gSq_pairVal_nonneg',)),
        'gSq_symm_value': ('', SQ_VALUE, ()),
        'gSq_symm_not_mem_maxCone': ('', 'gSq.symm (prodState z5 x5) ∉ maxCone (eball 5)',
                                     ('gSq_symm_value', 'sharpEff_isEffectOn', 'z5_unit', 'negx5_unit')),
        'gSq_not_posInv': ('', '¬ ' + on_body(pi, 'gSq', 'eball 5'),
                           ('gSq_symm_not_mem_maxCone', 'z5_mem', 'x5_mem')),
        'not_nativeGate_gSq': ('', '¬ NativeGate (eball 5) z5 n5 gSq', ('gSq_not_posInv',)),
        'not_nativeGate_gSqInv': ('', '¬ NativeGate (eball 5) z5 n5 gSq.symm', ('gSq_not_posInv',)),
        'frame_symm': ('{z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d} (hF : %s)' % frame, tsub(frame, {'G': 'G.symm'}), ()),
        'relT_symm': ('%s (hN : IsNot Ω z N) (hT : %s)' % (GRD, rt), tsub(rt, {'G': 'G.symm'}), ()),
        'relC_symm_of_relT': ('%s (hN : IsNot Ω z N) (hT : %s) (hC : %s)' % (GRD, rt, rc), tsub(rc, {'G': 'G.symm'}),
                              ()),
        'gateRel_symm': ('%s (hN : IsNot Ω z N) (hR : GateRel N G)' % GRD, 'GateRel N G.symm',
                         ('relT_symm', 'relC_symm_of_relT')),
        'gSq_sep': ('', sq_conj(landed, 'gSq', False),
                    ('isNot_n5', 'gSq_frame', 'gateRel_gSq', 'gSq_posFwd', 'gSq_not_posInv')),
        'gSqInv_sep': ('', sq_conj(landed, 'gSq.symm', True),
                       ('isNot_n5', 'frame_symm', 'gateRel_symm', 'gSq_posFwd', 'gSq_not_posInv'))}
    for n, (b, c, deps) in rows.items():
        if thm_bad(kinds, texts, proofs, n, b, c, deps):
            bad.append(n)
    bad += relations_bad(landed)
    for n, want in LANDED_N5.items():
        if landed.get(n) != norm(want):
            bad.append(n + ' at D')
    bad += free_bad(mod, ('Entangling', CTRL))
    return bad


def relation_bad(mods, landed):
    """S4: at d = 5 with the witness NOT nC5 and the landed z5, gC5 has the landed frame, relT, posFwd and posInv
    fields and fails the landed relC field, so IsNot and those four fields do not give the landed selector's
    conclusion; the module names no part of the landed n5."""
    mod = mods.get(C5)
    kinds, texts, proofs = kinds_texts_proofs(mod)
    bad = []
    for n, t in C5_DEFS.items():
        if norm(texts.get(n, '')) != norm(t):
            bad.append(n)
    for n in C5_TABLES:
        if norm(texts.get(n, '')) != norm(TEXTS[C5].get(n, '\0')):
            bad.append(n)
    if not norm(texts.get('gC5', '')).startswith(C5_GATE_HEAD):
        bad.append('gC5')
    frame, pf, pi, rt, rc = (body_of(landed, 'NativeGate', f) for f in GATE_FIELDS)
    dimc = split_statement(landed.get('dim_of_nativeGate', ''))[1]
    if None in (frame, pf, pi, rt, rc) or not dimc:
        return bad + ['NativeGate fields or selector at D']
    w = {'G': 'gC5', 'z': 'z5', 'N': 'nC5'}
    sel = ('¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), '
           'IsNot (eball d) z N → (%s) → (%s) → (%s) → (%s) → %s'
           % (frame, on_body(pf, 'G', 'eball d'), on_body(pi, 'G', 'eball d'), rt, norm(dimc)))
    rows = {
        'isNot_nC5': ('', 'IsNot (eball 5) z5 nC5', ()),
        'homMap_nC5_sign': ('(v : HVec 5) (μ : Fin (5 + 1))', 'homMap nC5 v μ = (if oddC5 μ then -1 else 1) * v μ',
                            ()),
        'gC5_frame': ('(a b : Fin 2)', tsub(frame.split(', ', 1)[1], w), ()),
        'gC5_relT': ('(ω : W 5)', tsub(rt.split(', ', 1)[1], w), ()),
        'gC5_relC_lhs': ('', 'actC nC5 (gC5 (actC nC5 (OddChar.entW 3 3))) 4 4 = 1', ()),
        'gC5_relC_rhs': ('', 'actT nC5 (gC5 (OddChar.entW 3 3)) 4 4 = -1', ()),
        'gC5_not_relC': ('', '¬ ' + tsub(rc, w), ('gC5_relC_lhs', 'gC5_relC_rhs')),
        'gC5_posFwd': ('', on_body(pf, 'gC5', 'eball 5'), ('gC5_prodEffVal_nonneg',)),
        'gC5_posInv': ('', on_body(pi, 'gC5', 'eball 5'), ('gC5_posFwd',)),
        'c5_sep': ('', 'IsNot (eball 5) z5 nC5 ∧ (%s) ∧ (%s) ∧ (%s) ∧ (%s) ∧ ¬ (%s)'
                   % (tsub(frame, w), tsub(rt, w), on_body(pf, 'gC5', 'eball 5'), on_body(pi, 'gC5', 'eball 5'),
                      tsub(rc, w)),
                   ('isNot_nC5', 'gC5_frame', 'gC5_relT', 'gC5_posFwd', 'gC5_posInv', 'gC5_not_relC')),
        'not_nativeGate_gC5': ('', '¬ NativeGate (eball 5) z5 nC5 gC5', ('gC5_not_relC',)),
        'relT_not_dimension_selecting': ('', sel, ('isNot_nC5', 'gC5_frame', 'gC5_posFwd', 'gC5_posInv',
                                                   'gC5_relT'))}
    for n, (b, c, deps) in rows.items():
        if thm_bad(kinds, texts, proofs, n, b, c, deps):
            bad.append(n)
    if landed.get('z5') != norm(LANDED_N5['z5']):
        bad.append('z5 at D')
    bad += free_bad(mod, ('n5', 'c5', 'odd5', 'isNot_n5', 'homMap_n5_sign', 'Entangling', CTRL))
    return bad


def par_cell(mods, landed):
    """RELC-PARITY-PROVED iff S1. Otherwise RELC-PARITY-NOT-ESTABLISHED. Reads the parity module only."""
    return [PAR_TOKENS[1] if parity_bad(mods, landed) else PAR_TOKENS[0]]


def sel_cell(mods, landed):
    """CTRL-SELECTOR-PROVED iff S2. Otherwise CTRL-SELECTOR-NOT-ESTABLISHED. Reads the block module and, for the
    parity step it cites, the parity theorem's statement and the parity module's freedom from relT."""
    return [SEL_TOKENS[1] if selector_bad(mods, landed) else SEL_TOKENS[0]]


def pos_cell(mods, landed):
    """POSITIVITY-SEPARATION-PROVED iff S3. Otherwise POSITIVITY-SEPARATION-NOT-ESTABLISHED. Reads the squeeze
    module only."""
    return [POS_TOKENS[1] if positivity_bad(mods, landed) else POS_TOKENS[0]]


def rel_cell(mods, landed):
    """RELT-NOT-DIMENSION-SELECTING-PROVED iff S4. Otherwise RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED. Reads the
    C5 module only."""
    return [REL_TOKENS[1] if relation_bad(mods, landed) else REL_TOKENS[0]]


def verdicts(mods, landed):
    return par_cell(mods, landed), sel_cell(mods, landed), pos_cell(mods, landed), rel_cell(mods, landed)


def comments(text):
    """The comment text of a module: every block comment (headers and docstrings) and every line comment."""
    return ' '.join(re.findall(r'/-.*?-/', text or '', flags=re.S) + re.findall(r'--[^\n]*', text or ''))


def phrase_norm(text):
    return norm(re.sub(r'(?m)^\s*>\s?', '', (text or '').replace('`', ''))).lower()


def phrase_hits(text, whitelist=()):
    t = phrase_norm(text)
    for w in whitelist:
        t = t.replace(phrase_norm(w), ' ')
    return [p for p in PHRASES if p.lower() in t]


def note_tokens(note):
    return [t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note)]


def earned_stated(note):
    t = phrase_norm(note)
    return [phrase_norm(e) in t for e in EARNED]


def semantic_checks(mods, tag, landed, inv_files):
    for code, label, fn in (('S1', 'parity from IsNot and relC alone; the parity module free of relT, the frame and '
                                   'positivity', parity_bad),
                            ('S2', 'CtrlGate is NativeGate without relT; IsNot and CtrlGate give d = 1 ∨ d = 3, '
                                   'Entangling d = 3; the copy is the landed proof; no relT read', selector_bad),
                            ('S3', 'at d = 5, gSq fails posInv and gSq.symm fails posFwd with every other clause; '
                                   'the relC transfer takes relT', positivity_bad),
                            ('S4', 'at d = 5, gC5 with nC5 has the frame, relT and both positivity clauses and fails '
                                   'relC; the selector does not follow', relation_bad)):
        b = fn(mods, landed)
        check(code, label + tag + ((' %s' % b[:4]) if b else ''), not b)
    bad6 = []
    for m in MODULES:
        mod = mods.get(m) or ''
        texts = {n: c for n, (_, c, _) in decl_chunks(mod).items()}
        for kind, name, start, se, nxt, cend in spans(mod):
            if mentions(mod[start:nxt], SCOPE_TOKENS):
                bad6.append(name)
            if kind in ('theorem', 'lemma'):
                c = norm(split_statement(texts.get(name, ''))[1])
                if (D_EQ.search(c) and name not in D_EQ_ALLOWED) or \
                        (token('NativeGate', c) and not c.startswith('¬')) or \
                        (token(CTRL, c) and name != 'ctrlGate_of_nativeGate'):
                    bad6.append(name)
    check('S6', 'no complex field or landed dimension selector; only the frozen selector theorems conclude on d; no '
                'native gate concluded%s%s' % (tag, (' %s' % bad6[:4]) if bad6 else ''), not bad6)
    others = inventory(inv_files)[0]
    clash, seen, dup = [], {}, []
    for m in MODULES:
        mod = mods.get(m) or ''
        names, spaces = inventory(inv_files + [mod])
        msc = scopes_at(mod)
        for kind, name in decls(mod):
            sc = msc.get(name, ([], [], []))
            if resolve(name, visible(sc[1], sc[2], spaces), others):
                clash.append(name)
            if name in seen:
                dup.append(name)
            seen[name] = m
    imports_ok_ = all(re.findall(r'^import .*$', mods.get(m) or '', re.M) == IMPORTS_OF[m] for m in MODULES)
    check('S7', 'no declaration shares a name with a visible OIBridge declaration or another module of the round; '
                'the imports are the frozen ones%s%s' % (tag, (' %s' % (clash + dup)[:4]) if clash or dup else ''),
          not clash and not dup and imports_ok_)
    ph = sorted({p for m in MODULES for p in phrase_hits(comments(mods.get(m)))})
    check('S8', 'the comments of the modules carry none of the frozen phrases%s%s' % (tag, (' %s' % ph) if ph else ''),
          not ph)
    ok9 = True
    for m in MODULES:
        mod = mods.get(m) or ''
        prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
        local = {n for _, n in decls(mod)}
        pnames = [p[len(PREFIX):] for p in prints if p.startswith(PREFIX)]
        ok9 = ok9 and prints == PRINTS[m] and len(PRINTS[m]) == N_PRINTS[m] and len(set(prints)) == N_PRINTS[m] \
            and len(pnames) == N_PRINTS[m] and all(n in local for n in pnames)
    check('S9', 'exactly the frozen #print axioms lines of each module (%s), distinct, each naming a declaration of '
                'its module%s' % (', '.join('%d' % N_PRINTS[m] for m in MODULES), tag), ok9)
    v = verdicts(mods, landed)
    check('V', 'one outcome per cell by the frozen rules: %s%s' % (', '.join(x[0] for x in v), tag),
          all(len(x) == 1 for x in v))


_INV = []


def d_inventory_files():
    """Every OIBridge module at D (read once)."""
    if not _INV:
        r = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in r.stdout.split() if p.endswith('.lean'))
    return list(_INV)


def module_checks(mods, tag='', landed=None, inv_files=None):
    if landed is None:
        landed = LANDED
    if inv_files is None:
        inv_files = d_inventory_files()
    for m in MODULES:
        mod = mods.get(m)
        if mod is None:
            check('N1', '%s present%s' % (m, tag), False)
            continue
        check('N1', '%s declares exactly its frozen declarations%s' % (m, tag), [list(x) for x in decls(mod)] == DECLS[m])
        check('N2', '%s: the preamble and every context block unchanged and in order%s' % (m, tag),
              '\n/-! ### §A' in mod and '\nimport ' in mod and preamble(mod) == PREAMBLE[m]
              and context_lines(mod) == CONTEXT[m])
        texts = {n: c for n, (_, c, _) in decl_chunks(mod).items()}
        bad = sorted(n for n in TEXTS[m] if texts.get(n) != TEXTS[m][n])
        check('N2', '%s: every frozen statement and definition unchanged%s%s'
              % (m, tag, (' (changed: %s)' % ', '.join(bad[:4])) if bad else ''), not bad)
        c = code_only(mod)
        prints = re.findall(r'^#print axioms (\S+)', mod, re.M)
        check('N3', '%s: no sorry, admit, axiom or native_decide; every frozen #print axioms line present%s' % (m, tag),
              not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', c, re.M)
              and all(p in prints for p in PRINTS[m]))
    semantic_checks(mods, tag, landed, inv_files)


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORTS, 1)


def census_want(d_text):
    d = json.loads(d_text)
    fam = d['families']
    k = [i for i, f in enumerate(fam) if f['modules'] == PREV_FAMILY_MODULES]
    if len(k) != 1:
        return None
    want = dict(d)
    want['families'] = fam[:k[0] + 1] + [CENSUS_FAMILY] + fam[k[0] + 1:]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        want = census_want(d_text)
    except Exception:
        return False
    return want is not None and e_text == want


def landed_texts(show_d):
    """The landed texts the rules read, from D: NativeGate's header and fields, IsNot, Entangling, GateRel's fields,
    DIM-1's selector statements and its two native gates, the balance lemma, the objects of n5, the declarations the
    block module copies, and the names of the landed declarations whose statements take the native gate."""
    out = {}
    cd, pn = show_d(CD), show_d(PN)
    if not cd or not pn:
        return out
    cch, pch = decl_chunks(cd), decl_chunks(pn)
    ch = cch.get('NativeGate')
    if ch and ch[0] == 'structure':
        out['NativeGate#header'] = norm(def_header(ch[1]))
        out['NativeGate#fields'] = ' '.join(fields(ch[1]))
        for f in GATE_FIELDS:
            v = field_line(ch[1], f)
            if v is not None:
                out['NativeGate#' + f] = v
    for n, kind in (('IsNot', 'structure'), ('Entangling', 'def')):
        if n in cch and cch[n][0] == kind:
            out[n] = norm(cch[n][1])
    ch = pch.get('GateRel')
    if ch and ch[0] == 'structure':
        out['GateRel#fields'] = ' '.join(fields(ch[1]))
        for f in ('relT', 'relC'):
            v = field_line(ch[1], f)
            if v is not None:
                out['GateRel#' + f] = v
    for n in LANDED_CD_THMS:
        if n in cch and cch[n][0] == 'theorem':
            out[n] = norm(cch[n][1])
    for n in LANDED_PN_DEFS:
        if n in pch and pch[n][0] == 'def':
            out[n] = norm(pch[n][1])
    for n in LANDED_PN_THMS:
        if n in pch and pch[n][0] == 'theorem':
            out[n] = norm(pch[n][1])
    ld = line_decls(cd)
    for old in COPY_MAP:
        if ld.get(old) is not None:
            out['copy#' + old] = '\n'.join(ld[old])
    names = set()
    r = git('ls-tree', '--name-only', D, LEAN)
    for p in sorted(r.stdout.split()):
        if p.endswith('.lean'):
            for n, (k, stmt, _) in decl_chunks(show_d(p) or '').items():
                if token('NativeGate', stmt):
                    names.add(n)
    out['nativeGate#names'] = ' '.join(sorted(names))
    return out


def landed_at_d():
    return landed_texts(lambda p: show(D, p))


def modules_at(commit):
    return {m: show(commit, MODPATH[m]) for m in MODULES}


def run_check(commit, freeze):
    r = git('diff', '--name-status', '--no-renames', D, commit)
    rows = [l.split('\t') for l in r.stdout.splitlines() if l]
    exec_rows = {p: s for s, p in rows if not p.startswith(RDIR)}
    rec = {p for s, p in rows if p.startswith(RDIR)}
    check('P', 'delta(D, commit) is exactly the governed execution paths plus the record directory',
          r.returncode == 0 and exec_rows == GOVERNED and rec <= RECORD_FILES and PREREG in rec)
    landed = landed_at_d()
    check('L', 'the landed texts read from D are the frozen ones', landed == LANDED)
    mods = modules_at(commit)
    module_checks(mods, landed=landed)
    note = show(commit, RESULT)
    if note is not None:
        ph = phrase_hits(note, EARNED + NONINF)
        check('S8', 'the result note less the frozen earned reading and non-inference rule carries none of the frozen '
                    'phrases%s' % ((' %s' % ph) if ph else ''), not ph)
        v = verdicts(mods, landed)
        cells = [x[0] for x in v if len(x) == 1]
        toks = note_tokens(note)
        check('V', 'the result note states exactly the computed tokens %s and no other outcome token (found %s)'
              % (cells, toks), len(cells) == 4 and sorted(toks) == sorted(cells))
        allp = cells == [PAR_TOKENS[0], SEL_TOKENS[0], POS_TOKENS[0], REL_TOKENS[0]]
        st = earned_stated(note)
        check('V', 'the result note states the frozen earned reading %s' % ('(all four cells proved)' if allp else
                                                                             'not at all (a cell not established)'),
              all(st) if allp else not any(st))
        check('V', 'the result note states the frozen non-inference rule',
              all(phrase_norm(n) in phrase_norm(note) for n in NONINF))
    check('I', 'OIBridge.lean is D\'s with exactly the four frozen import lines', imports_ok(show(D, IMPORTS),
                                                                                         show(commit, IMPORTS)))
    check('C', 'the census is D\'s with exactly the frozen family after the ODD-CHAR-1 family',
          census_ok(show(D, CENSUS), show(commit, CENSUS)))
    if freeze:
        check('F', 'the preregistration is unchanged from F', show(commit, PREREG) == show(freeze, PREREG))
        r = git('diff', '--name-only', D, freeze)
        check('F', 'delta(D, F) is the preregistration alone', r.stdout.split() == [PREREG])


def print_verdicts(commit):
    mods = modules_at(commit)
    landed = landed_at_d()
    v = verdicts(mods, landed)
    for lab, x in zip(('PAR', 'SEL', 'POS', 'REL'), v):
        print('VERDICT  %s  %s' % (lab, '/'.join(x) or 'none'))
    check('V', 'the landed texts read from D are the frozen ones', landed == LANDED)
    check('V', 'exactly one outcome per cell', all(len(x) == 1 for x in v))

def must_fail(code, label, mods2, landed=None):
    before, count = list(FAILS), COUNT[0]
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        module_checks(mods2, landed=landed)
    finally:
        sys.stdout = saved
    new = FAILS[len(before):]
    del FAILS[len(before):]
    COUNT[0] = count
    check('M', 'mutation %s fails with %s' % (label, code), code in new)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def mutate(mods, m, a, b):
    out = dict(mods)
    out[m] = replace_once(mods[m], a, b)
    return out


def append_decl(mods, m, decl):
    """Insert a declaration at the end of the module's namespace."""
    return mutate(mods, m, '\nend RelcSelect\nend OIBridge\n', '\n' + decl + '\n\nend RelcSelect\nend OIBridge\n')


def verdict_of(mods2, landed=None):
    return verdicts(mods2, LANDED if landed is None else landed)


def landed_with(key, a, b):
    lm = dict(LANDED)
    assert lm[key].count(a) >= 1, (key, a)
    lm[key] = lm[key].replace(a, b)
    return lm

RELC = 'actC N (G (actC N ω)) = actT N (G ω)'
RELT = 'actT N (G (actT N ω)) = G ω'
P = (PAR_TOKENS[0], SEL_TOKENS[0], POS_TOKENS[0], REL_TOKENS[0])
NP = (PAR_TOKENS[1], SEL_TOKENS[1], POS_TOKENS[1], REL_TOKENS[1])


def cells(*which):
    """The four verdicts with the named cells (0..3) not established."""
    return tuple([NP[k] if k in which else P[k]] for k in range(4))


def self_test():
    mods = {m: git('cat-file', '-p', MOD_REFERENCE_BLOBS[m]).stdout for m in MODULES}
    check('T', 'the four reference module blobs are readable', all(mods.values()))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED)
    module_checks(mods, ' [reference]')
    check('T', 'the reference modules read %s' % ', '.join(x[0] for x in verdict_of(mods)), verdict_of(mods) == cells())
    check('T', 'the copy check passes on the reference block module', copy_bad(mods[BLK], LANDED) == [])
    # N1-N3
    must_fail('N1', 'a renamed declaration', mutate(mods, SQZ, '\ntheorem x5_unit ', '\ntheorem x5_unit\' '))
    must_fail('N2', 'a changed binder context', mutate(mods, PAR, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {m : ℕ}\n'))
    must_fail('N2', 'a changed open line', mutate(mods, BLK, 'CompositeDimension EffectSpace ParityNot\n',
                                                  'CompositeDimension EffectSpace\n'))
    must_fail('N2', 'a restated conclusion', mutate(mods, SQZ, '      ∧ GateRel n5 gSq\n', '      ∧ True\n'))
    must_fail('N3', 'a sorry', append_decl(mods, C5, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', mutate(mods, SQZ, '#print axioms OIBridge.RelcSelect.gSqInv_sep\n', ''))
    # S1 -- parity from the control relation
    head1 = '    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by'
    must_fail('S1', 'the control relation replaced by GateRel',
              mutate(mods, PAR, '    (hC : ∀ ω, %s) :\n%s' % (RELC, head1), '    (hC : GateRel N G) :\n%s' % head1))
    must_fail('S1', 'the target relation added to the parity corollary',
              mutate(mods, PAR, '    (hC : ∀ ω, %s) : ¬ Even d :=' % RELC,
                     '    (hT : ∀ ω, %s) (hC : ∀ ω, %s) : ¬ Even d :=' % (RELT, RELC)))
    must_fail('S1', 'the count weakened to an inequality', mutate(mods, PAR, head1, head1.replace(' = Module', ' ≤ Module')))
    must_fail('S1', 'a parity proof reading a landed relT lemma',
              mutate(mods, PAR, ' : P = Q := by\n  subst hn\n',
                     ' : P = Q := by\n  have _x := @gateRel_of_nativeGate\n  subst hn\n'))
    m = mutate(mods, PAR, head1, head1.replace(' = Module', ' ≤ Module'))
    check('M', 'decision rule: a broken parity theorem reads RELC-PARITY-NOT-ESTABLISHED and '
               'CTRL-SELECTOR-NOT-ESTABLISHED, whose parity step it is, and leaves the other two cells',
          verdict_of(m) == cells(0, 1))
    check('M', 'landed: a landed relC field that differs fails all four cells',
          verdict_of(mods, landed_with('NativeGate#relC', 'actT N (G ω)', 'G ω')) == cells(0, 1, 2, 3))
    check('M', 'landed: a landed balance lemma that differs fails the parity cell alone',
          verdict_of(mods, landed_with('not_even_of_balanced', '¬ Even d', 'Odd d')) == cells(0))
    check('M', 'landed: a landed relT field that differs fails the positivity and relation cells and leaves the '
               'parity and selector cells, which do not read relT',
          verdict_of(mods, landed_with('NativeGate#relT', '= G ω', '= -G ω')) == cells(2, 3))
    # S2 -- the selector without the target relation
    relc_f = '  relC : ∀ ω, %s\n' % RELC
    must_fail('S2', 'relT restored to CtrlGate', mutate(mods, BLK, relc_f, '  relT : ∀ ω, %s\n%s' % (RELT, relc_f)))
    must_fail('S2', 'posInv dropped from CtrlGate',
              mutate(mods, BLK, '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n', ''))
    must_fail('S2', 'the selector strengthened to d = 3', mutate(mods, BLK, '    d = 1 ∨ d = 3 := by\n  have hpos',
                                                                   '    d = 3 := by\n  have hpos'))
    must_fail('S2', 'the landed parity line restored',
              mutate(mods, BLK, '    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC',
                     '    have hbal := finrank_plus_eq_finrank_minus hN hG'))
    must_fail('S2', 'the relT step restored in the block reduction',
              mutate(mods, BLK, '            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl',
                     '            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]'))
    must_fail('S2', 'a copied proof token changed', mutate(mods, BLK, '  rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG]\n',
                                                          '  rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG, add_zero]\n'))
    must_fail('S2', 'a landed native-gate lemma referenced',
              mutate(mods, BLK, '    exact Phi_hom_zero_eq_zero_ctrl hN hG hc hzc u (hom 0)',
                     '    exact Phi_hom_zero_eq_zero hN hG hc hzc u (hom 0)'))
    must_fail('S2', 'the entangling clause dropped', mutate(mods, BLK, '\n    (hE : Entangling (eball d) G) : d = 3 := by',
                                                            ' : d = 3 := by'))
    check('M', 'reuse: a relT reader named through its namespace is found',
          mentions('theorem x : True := by\n  have := CompositeDimension.gate_actT\n  trivial', RELT_READERS)
          == ['gate_actT'])
    check('M', 'reuse: a landed native-gate lemma named through its namespace is found',
          nativegate_names_bad('theorem x : True := by\n  have := CompositeDimension.gate_corner\n  trivial', LANDED)
          == ['x'])
    m = mutate(mods, BLK, '    d = 1 ∨ d = 3 := by\n  have hpos', '    d = 3 := by\n  have hpos')
    check('M', 'decision rule: a broken selector reads CTRL-SELECTOR-NOT-ESTABLISHED and leaves the other cells',
          verdict_of(m) == cells(1))
    check('M', 'landed: a landed selector that differs fails the selector cell alone',
          verdict_of(mods, landed_with('dim_of_nativeGate', '(hN : IsNot (eball d) z N)',
                                       '(hN : IsNot (eball d) z N) (h2 : 2 ≤ d)')) == cells(1))
    check('M', 'landed: a landed d = 3 native gate that differs fails the selector cell alone',
          verdict_of(mods, landed_with('nativeGate_cnot', 'eball 3', 'eball 5')) == cells(1))
    check('M', 'landed: a landed copied declaration that differs fails the selector cell alone',
          verdict_of(mods, landed_with('copy#gt_corner', 'Mfwd_Minv hN hG]', 'Mfwd_Minv hN hG, add_zero]')) == cells(1))
    check('M', 'landed: a landed posInv field that differs fails every cell but parity',
          verdict_of(mods, landed_with('NativeGate#posInv', 'maxCone Ω', 'jointStates Ω')) == cells(1, 2, 3))
    # S3 -- the positivity clauses one at a time
    sep_tail = ('      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=\n'
                '  ⟨isNot_n5, gSq_frame, gateRel_gSq, gSq_posFwd, gSq_not_posInv⟩')
    must_fail('S3', 'the failure of inverse positivity dropped from gSq_sep',
              mutate(mods, SQZ, '\n' + sep_tail, ' :=\n  ⟨isNot_n5, gSq_frame, gateRel_gSq, gSq_posFwd⟩'))
    inv4 = ('      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))\n'
            '      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=\n'
            '  ⟨isNot_n5, frame_symm')
    must_fail('S3', 'the inverse positivity of gSq.symm restated as its forward positivity',
              mutate(mods, SQZ, inv4, inv4.replace('gSq (prodState', 'gSq.symm (prodState', 1)))
    must_fail('S3', 'the transfer of relC to the inverse without relT',
              mutate(mods, SQZ, '(hN : IsNot Ω z N) (hT : ∀ ω, %s)\n    (hC :' % RELT, '(hN : IsNot Ω z N)\n    (hC :'))
    must_fail('S3', 'the value changed to a sign', mutate(mods, SQZ, '(gSq.symm (prodState z5 x5)) = -1 / 2 := by',
                                                          '(gSq.symm (prodState z5 x5)) < 0 := by'))
    must_fail('S3', 'the squeeze removed', mutate(mods, SQZ, 'if sqCls n then 1 else 1 / 2', 'if sqCls n then 1 else 1'))
    must_fail('S3', 'GateRel weakened to the control relation in gSq_sep',
              mutate(mods, SQZ, '      ∧ GateRel n5 gSq\n', '      ∧ (∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω))\n'))
    m = mutate(mods, SQZ, '(gSq.symm (prodState z5 x5)) = -1 / 2 := by', '(gSq.symm (prodState z5 x5)) < 0 := by')
    check('M', 'decision rule: a broken positivity witness reads POSITIVITY-SEPARATION-NOT-ESTABLISHED and leaves the '
               'other cells', verdict_of(m) == cells(2))
    check('M', 'landed: a landed n5 that differs fails the positivity cell alone',
          verdict_of(mods, landed_with('odd5', '2 => false', '2 => true')) == cells(2))
    check('M', 'landed: a landed GateRel that differs from the landed relations fails the positivity cell alone',
          verdict_of(mods, landed_with('GateRel#relC', 'actT N (G ω)', 'G ω')) == cells(2))
    # S4 -- the control relation is not replaced by the target relation
    must_fail('S4', 'the failure of relC dropped from c5_sep',
              mutate(mods, C5, ' ∧\n      ¬ (∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)) :=\n'
                               '  ⟨isNot_nC5, gC5_frame, gC5_relT, gC5_posFwd, gC5_posInv, gC5_not_relC⟩',
                     ' :=\n  ⟨isNot_nC5, gC5_frame, gC5_relT, gC5_posFwd, gC5_posInv⟩'))
    must_fail('S4', 'relC in place of relT in the non-selection statement',
              mutate(mods, C5, '      (∀ ω, %s) →\n      d = 1 ∨ d = 3 := by' % RELT,
                     '      (∀ ω, %s) →\n      d = 1 ∨ d = 3 := by' % RELC))
    must_fail('S4', 'inverse positivity dropped from the non-selection statement',
              mutate(mods, C5, '      (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) →\n', ''))
    must_fail('S4', 'a sign of the gate changed', mutate(mods, C5, '(ν = 2 ∨ ν = 3)) then -1 else 1',
                                                         '(ν = 2 ∨ ν = 3)) then 1 else -1'))
    must_fail('S4', 'the witness NOT replaced by the landed n5',
              mutate(mods, C5, 'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5',
                     'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := n5'))
    must_fail('S4', 'the non-selection conclusion changed', mutate(mods, C5, '      d = 1 ∨ d = 3 := by\n  intro h',
                                                                   '      d = 3 := by\n  intro h'))
    m = mutate(mods, C5, '(ν = 2 ∨ ν = 3)) then -1 else 1', '(ν = 2 ∨ ν = 3)) then 1 else -1')
    check('M', 'decision rule: a broken relation witness reads RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED and leaves '
               'the other cells', verdict_of(m) == cells(3))
    check('M', 'landed: a landed z5 that differs fails the positivity and relation cells',
          verdict_of(mods, landed_with('z5', 'i = 4', 'i = 3')) == cells(2, 3))
    # S6 -- scope
    must_fail('S6', 'a complex field', append_decl(mods, SQZ, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    must_fail('S6', 'a positive native gate', append_decl(mods, C5, 'theorem pos_gate : NativeGate (eball 5) z5 nC5 gC5 '
                                                                     ':= sorry'))
    must_fail('S6', 'a conclusion on d outside the selector',
              append_decl(mods, BLK, 'theorem d_sel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                     '{G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) '
                                     '(hG : CtrlGate (eball d) z N G) : d ≠ 5 := sorry'))
    must_fail('S6', 'the landed selector read', mutate(mods, BLK, '  rcases dim_of_ctrlGate hN hG with hone | hthree',
                                                       '  rcases dim_of_nativeGate hN hG with hone | hthree'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_decl(mods, C5, 'def odd5 : ℕ := 0'))
    must_fail('S7', 'a declaration of another module of the round re-declared',
              append_decl(mods, C5, 'theorem lor_five : True := trivial'))
    must_fail('S7', 'a second import', mutate(mods, PAR, 'import OIBridge.OddChar\n',
                                              'import OIBridge.OddChar\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a global redundancy claim in a header',
              mutate(mods, BLK, '  remains a field of both.\n', '  remains a field of both; relT is redundant.\n'))
    must_fail('S8', 'an implication between the positivity clauses in a docstring',
              mutate(mods, SQZ, '/-- **Forward positivity does not imply inverse positivity**',
                     '/-- **Forward positivity implies inverse positivity**'))
    must_fail('S8', 'the design header', mutate(mods, C5, 'OIBridge/RelcSelectC5.lean — round RELC-SELECT-1:',
                                                'OIBridge/RelcSelectC5.lean — design module for round RELC-SELECT-1:'))
    frozen = EARNED + NONINF
    check('M', 'phrases: the frozen earned reading and non-inference rule pass when stated; each passes nowhere else',
          not phrase_hits('\n\n'.join(frozen), frozen) and all(phrase_hits(f) for f in frozen))
    check('M', 'phrases: unqualified or global claims fail',
          phrase_hits('relT is unnecessary.') == ['relT is unnecessary']
          and phrase_hits('Hence `relC` is inverse-stable.') == ['inverse-stable']
          and 'redundan' in phrase_hits('relT is globally redundant')
          and phrase_hits('a physical gate') == ['physical gate']
          and phrase_hits('a globally minimal set') == ['globally minimal']
          and phrase_hits('> ' + EARNED[0] + ' Hence relT is unnecessary.', frozen) == ['relT is unnecessary'])
    # S9
    must_fail('S9', 'an extra print', mutate(mods, SQZ, '#print axioms OIBridge.RelcSelect.gSqInv_sep\n',
                                             '#print axioms OIBridge.RelcSelect.gSqInv_sep\n'
                                             '#print axioms OIBridge.RelcSelect.x5_unit\n'))
    must_fail('S9', 'a duplicated print', mutate(mods, C5, '#print axioms OIBridge.RelcSelect.c5_sep\n',
                                                 '#print axioms OIBridge.RelcSelect.c5_sep\n'
                                                 '#print axioms OIBridge.RelcSelect.c5_sep\n'))
    # V
    allp = ', '.join(P)
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens(allp + '.') == list(P)
          and note_tokens('RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED') == [REL_TOKENS[1]])
    quoted = '\n'.join('> ' + l for l in '\n\n'.join(EARNED).split('\n'))
    check('M', 'earned reading: found when quoted across lines, not found when one sentence is changed',
          all(earned_stated(quoted)) and
          not all(earned_stated(quoted.replace('the dimension is 1 or 3', 'the dimension is 3'))))
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORTS, 1)
    check('M', 'imports: the frozen edit passes; a dropped line and a reordered pair fail',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp)
          and not imports_ok(d_imp, good_imp.replace('import OIBridge.RelcSelectParity\nimport OIBridge.RelcSelectBlock\n',
                                                     'import OIBridge.RelcSelectBlock\nimport OIBridge.RelcSelectParity\n')))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; a changed status, a moved family, a whitespace change and the '
               'unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, bad_status) and moved != good
          and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1))
          and not census_ok(d_cen, d_cen))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'verdict':
        print_verdicts(argv[1])
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
