#!/usr/bin/env python3
"""controls.py -- round KINF-COPY-1's own contracts, to be frozen with the preregistration beside it.

Imports nothing from the repository and changes nothing in it. Reads D and the commit under check through git, and
embeds every frozen text it compares against: the predicted module (with the header of the design blob it was split
from, so that the link to the built blob is checked from this file alone), the predicted probe (the measured
e2_copy_conj.py with its kernel line alone changed, checked by sha256), the declarations, statements and definitions,
the resolution map of every identifier at D, the workflow edit, the import line, the census family, the round and
governed-path blocks, the earned reading, the non-inference rule and the phrase list.

The round's claim is scoped to two-NOT data. The one-NOT limitation is kept: the kernel surface carries no statement
that the swapped gate lacks a one-NOT reading, the result note must state the non-inference rule's limitation sentence
under every outcome, and a probe asserting that the swapped gate has no one-NOT reading with the target NOT is refuted
by measurement (self-test).

  controls.py freeze <F>                                  F mode: the frozen control plane
  controls.py check <commit> --freeze <F> [--axioms X]    a stage commit (C1, S1 or E) against D and F; at E the note
                                                          must state the three tokens computed with the axiom
                                                          expected result X (for a commit with the same module blob)
  controls.py verdict <commit> [--axioms X]               the three tokens from the measurements; X must be the
                                                          expected result of the exact-head run at <commit>
  controls.py axioms-from-log <log> <commit> [--run N --job N]
                                                          the expected result (AGENTS §A.42 item 1) from a build log
  controls.py --self-test                                 positive controls, the frozen mutations, one-cell mutations,
                                                          the one-NOT limitation controls, countercontrols and an
                                                          end-to-end run of the real modes on fixture commits

Codes: F freeze; K controls blob; G governed paths and stage shape; R record directory; L linear execution from F;
N1-N3 declarations, frozen texts, hygiene; S1 surface and two-NOT scope; S2 resolution; S3 hypotheses load-bearing on
the exact layer; S4 phrases; P probe blob; W workflow edit; V verdicts and note; I import line; C census; T self-test
assertion; M mutation or countercontrol outcome.
Every mode passes only if every code it requires was recorded and every record passed; a check that did not run
counts as failed. Unknown modes are refused. Exit 1 on any failure, 2 on a refused invocation.
"""
import hashlib, io, json, os, re, shutil, subprocess, sys, tempfile

D = 'dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/'
PREREG = 'verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/preregistration.md'
CONTROLS = 'verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/controls.py'
RESULT = 'verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/result.md'
RECEIPT = 'verification/receipts/KINF-COPY-1.json'
LEAN = 'verification/lean-mathlib/OIBridge/'
MOD = 'verification/lean-mathlib/OIBridge/CopyCovariance.lean'
PROBE = 'verification/lean/kinf_copy1_probe.py'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
EXEC_PATHS = {'verification/lean-mathlib/OIBridge/CopyCovariance.lean': 'A', 'verification/lean/kinf_copy1_probe.py': 'A', 'verification/lean-mathlib/OIBridge.lean': 'M', 'verification/lean-manuscript-census.json': 'M', '.github/workflows/verify.yml': 'M'}
ROUND_BLOCK = ['round KINF-COPY-1', 'kind non-sealing', 'record-directory verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/']
GOVERNED_BLOCK = ['record AM verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/', 'record AM verification/receipts/KINF-COPY-1.json', 'execution A verification/lean-mathlib/OIBridge/CopyCovariance.lean', 'execution A verification/lean/kinf_copy1_probe.py', 'execution M verification/lean-mathlib/OIBridge.lean', 'execution M verification/lean-manuscript-census.json', 'execution M .github/workflows/verify.yml']
ANCHOR_IMPORT = 'import OIBridge.EqvK2MaxCone\n'
NEW_IMPORT = 'import OIBridge.CopyCovariance\n'
IMPORT_ONLY = 'import OIBridge.DenseOrbit'
PREFIX = 'OIBridge.CopyCovariance.'
CENSUS_FAMILY = {'name': "type covariance of native inversion suffices for DIM-1's selector: two-NOT native-gate data whose target NOT is the conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis reduce to a one-NOT native gate (round KINF-COPY-1, reconstruction)", 'modules': ['CopyCovariance'], 'status': 'kernel-only', 'manuscript': []}
PRINTS = ["OIBridge.CopyCovariance.actC_actT_comm'", 'OIBridge.CopyCovariance.actTEq', 'OIBridge.CopyCovariance.prodEffVal_actT', 'OIBridge.CopyCovariance.actT_mem_maxCone', 'OIBridge.CopyCovariance.nativeGate2_conj', 'OIBridge.CopyCovariance.nativeGate_of_conj', 'OIBridge.CopyCovariance.dim_of_nativeGate2_conj', 'OIBridge.CopyCovariance.three_of_nativeGate2_conj_of_two_le', 'OIBridge.CopyCovariance.dim_of_nativeGate2_conj_neg', 'OIBridge.CopyCovariance.swapped_nativeGate2', 'OIBridge.CopyCovariance.swapped_not_ne', 'OIBridge.CopyCovariance.swapped_nativeGate']
DECLS = [['theorem', "homMap_comp'"], ['theorem', "homMap_id'"], ['theorem', "actT_comp'"], ['theorem', "actT_id'"], ['theorem', 'actT_congr'], ['theorem', "lin_apply_eq_sum'"], ['theorem', "lin_lin_comm'"], ['theorem', "actC_actT_comm'"], ['def', 'actTEq'], ['theorem', 'sum_mul_ehom'], ['theorem', 'affine_linear_apply'], ['theorem', 'sum_homMap_mul_ehom'], ['theorem', 'prodEffVal_actT'], ['theorem', 'isEffectOn_comp'], ['theorem', 'actT_mem_maxCone'], ['structure', 'NativeGate2'], ['theorem', 'nativeGate2_of_nativeGate'], ['theorem', 'nativeGate_of_nativeGate2'], ['theorem', 'map_corner_of_fix'], ['theorem', 'conjGate_apply'], ['theorem', 'conjGate_symm_apply'], ['theorem', 'nativeGate2_conj'], ['theorem', 'nativeGate_of_conj'], ['theorem', 'dim_of_nativeGate2_conj'], ['theorem', 'three_of_nativeGate2_conj_of_two_le'], ['theorem', 'dim_of_nativeGate2_conj_neg'], ['def', 'swap01'], ['theorem', 'swap01_swap01'], ['theorem', 'swap01_mem'], ['theorem', 'swap01_z3'], ['theorem', 'swapped_nativeGate2'], ['theorem', 'swapped_not_ne'], ['theorem', 'swapped_nativeGate']]
TEXTS = {"homMap_comp'": "theorem homMap_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :\n    homMap (M ∘ₗ N) v = homMap M (homMap N v)", "homMap_id'": "theorem homMap_id' (v : HVec d) : homMap LinearMap.id v = v", "actT_comp'": "theorem actT_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :\n    actT M (actT N ω) = actT (M ∘ₗ N) ω", "actT_id'": "theorem actT_id' (ω : W d) : actT LinearMap.id ω = ω", 'actT_congr': 'theorem actT_congr {M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (h : ∀ x, M x = N x) (ω : W d) :\n    actT M ω = actT N ω', "lin_apply_eq_sum'": "theorem lin_apply_eq_sum' (M : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) (i : Fin d) :\n    M x i = ∑ k, LinearMap.toMatrix' M i k * x k", "lin_lin_comm'": "theorem lin_lin_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (Ω' : Fin d → Fin d → ℝ)\n    (i j : Fin d) :\n    M (fun i' => N (Ω' i') j) i = N (fun j' => M (fun i' => Ω' i' j') i) j", "actC_actT_comm'": "theorem actC_actT_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :\n    actC M (actT N ω) = actT N (actC M ω)", 'actTEq': "def actTEq (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) : W d ≃ₗ[ℝ] W d where\n  toFun := actT g\n  invFun := actT h\n  map_add' ω₁ ω₂ := by\n    funext μ ν\n    simp only [actT_apply, Pi.add_apply, map_add]\n  map_smul' c ω := by\n    funext μ ν\n    simp only [actT_apply, Pi.smul_apply, map_smul, smul_eq_mul, RingHom.id_apply]\n  left_inv ω := by\n    show actT h (actT g ω) = ω\n    rw [actT_comp', actT_congr (M := h ∘ₗ g) (N := LinearMap.id)\n      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hhg x), actT_id']\n  right_inv ω := by\n    show actT g (actT h ω) = ω\n    rw [actT_comp', actT_congr (M := g ∘ₗ h) (N := LinearMap.id)\n      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hgh x), actT_id']", 'sum_mul_ehom': 'theorem sum_mul_ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (v : HVec d) :\n    ∑ ν, v ν * ehom e ν = v 0 * e 0 + e.linear (Matrix.vecTail v)', 'affine_linear_apply': 'theorem affine_linear_apply (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    f.linear x = f x - f 0', 'sum_homMap_mul_ehom': 'theorem sum_homMap_mul_ehom (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n    (v : HVec d) :\n    ∑ ν, homMap g v ν * ehom f ν = ∑ ν, v ν * ehom (f.comp g.toAffineMap) ν', 'prodEffVal_actT': 'theorem prodEffVal_actT (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n    (ω : W d) : prodEffVal e f (actT g ω) = prodEffVal e (f.comp g.toAffineMap) ω', 'isEffectOn_comp': 'theorem isEffectOn_comp {Ω : Set (Fin d → ℝ)} {f : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (hf : IsEffectOn Ω f)\n    {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hg : ∀ x ∈ Ω, g x ∈ Ω) :\n    IsEffectOn Ω (f.comp g.toAffineMap)', 'actT_mem_maxCone': 'theorem actT_mem_maxCone {Ω : Set (Fin d → ℝ)} {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hg : ∀ x ∈ Ω, g x ∈ Ω) {ω : W d} (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω', 'NativeGate2': 'structure NativeGate2 (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ)\n    (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n  relT : ∀ ω, actT NT (G (actT NT ω)) = G ω\n  relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)', 'nativeGate2_of_nativeGate': 'theorem nativeGate2_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate Ω z N G) :\n    NativeGate2 Ω z N N G', 'nativeGate_of_nativeGate2': 'theorem nativeGate_of_nativeGate2 {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate2 Ω z N N G) :\n    NativeGate Ω z N G', 'map_corner_of_fix': 'theorem map_corner_of_fix {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {z : Fin d → ℝ} (hgz : g z = z)\n    (b : Fin 2) : g (corner z b) = corner z b', 'conjGate_apply': 'theorem conjGate_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :\n    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) ω = actT h (G (actT g ω))', 'conjGate_symm_apply': 'theorem conjGate_symm_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :\n    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh).symm ω = actT h (G.symm (actT g ω))', 'nativeGate2_conj': 'theorem nativeGate2_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :\n    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)', 'nativeGate_of_conj': 'theorem nativeGate_of_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)\n    (hcov : ∀ x, NT (g x) = g (NC x)) :\n    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)', 'dim_of_nativeGate2_conj': 'theorem dim_of_nativeGate2_conj {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3', 'three_of_nativeGate2_conj_of_two_le': 'theorem three_of_nativeGate2_conj_of_two_le (hd : 2 ≤ d) {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3', 'dim_of_nativeGate2_conj_neg': 'theorem dim_of_nativeGate2_conj_neg {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3', 'swap01': "def swap01 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun v := ![v 1, v 0, v 2]\n  map_add' v w := by apply vec3_ext <;> rfl\n  map_smul' r v := by apply vec3_ext <;> rfl", 'swap01_swap01': 'theorem swap01_swap01 (v : Fin 3 → ℝ) : swap01 (swap01 v) = v', 'swap01_mem': 'theorem swap01_mem {v : Fin 3 → ℝ} (hv : v ∈ eball 3) : swap01 v ∈ eball 3', 'swap01_z3': 'theorem swap01_z3 : swap01 z3 = z3', 'swapped_nativeGate2': 'theorem swapped_nativeGate2 :\n    NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)\n      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ\n        actTEq swap01 swap01 swap01_swap01 swap01_swap01)', 'swapped_not_ne': 'theorem swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip', 'swapped_nativeGate': 'theorem swapped_nativeGate :\n    NativeGate (eball 3) z3 nflip\n      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ\n        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ\n          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ≪≫ₗ\n        actTEq swap01 swap01 swap01_swap01 swap01_swap01)'}
EFFECTIVE = {"homMap_comp'": '{d : ℕ} (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) : homMap (M ∘ₗ N) v = homMap M (homMap N v)', "homMap_id'": '{d : ℕ} (v : HVec d) : homMap LinearMap.id v = v', "actT_comp'": '{d : ℕ} (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : actT M (actT N ω) = actT (M ∘ₗ N) ω', "actT_id'": '{d : ℕ} (ω : W d) : actT LinearMap.id ω = ω', 'actT_congr': '{d : ℕ} {M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (h : ∀ x, M x = N x) (ω : W d) : actT M ω = actT N ω', "lin_apply_eq_sum'": "{d : ℕ} (M : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) (i : Fin d) : M x i = ∑ k, LinearMap.toMatrix' M i k * x k", "lin_lin_comm'": "{d : ℕ} (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (Ω' : Fin d → Fin d → ℝ) (i j : Fin d) : M (fun i' => N (Ω' i') j) i = N (fun j' => M (fun i' => Ω' i' j') i) j", "actC_actT_comm'": '{d : ℕ} (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : actC M (actT N ω) = actT N (actC M ω)', 'sum_mul_ehom': '{d : ℕ} (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (v : HVec d) : ∑ ν, v ν * ehom e ν = v 0 * e 0 + e.linear (Matrix.vecTail v)', 'affine_linear_apply': '{d : ℕ} (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) : f.linear x = f x - f 0', 'sum_homMap_mul_ehom': '{d : ℕ} (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (v : HVec d) : ∑ ν, homMap g v ν * ehom f ν = ∑ ν, v ν * ehom (f.comp g.toAffineMap) ν', 'prodEffVal_actT': '{d : ℕ} (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (ω : W d) : prodEffVal e f (actT g ω) = prodEffVal e (f.comp g.toAffineMap) ω', 'isEffectOn_comp': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {f : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (hf : IsEffectOn Ω f) {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hg : ∀ x ∈ Ω, g x ∈ Ω) : IsEffectOn Ω (f.comp g.toAffineMap)', 'actT_mem_maxCone': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hg : ∀ x ∈ Ω, g x ∈ Ω) {ω : W d} (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω', 'nativeGate2_of_nativeGate': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate Ω z N G) : NativeGate2 Ω z N N G', 'nativeGate_of_nativeGate2': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate2 Ω z N N G) : NativeGate Ω z N G', 'map_corner_of_fix': '{d : ℕ} {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {z : Fin d → ℝ} (hgz : g z = z) (b : Fin 2) : g (corner z b) = corner z b', 'conjGate_apply': '{d : ℕ} (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) : (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) ω = actT h (G (actT g ω))', 'conjGate_symm_apply': '{d : ℕ} (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) : (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh).symm ω = actT h (G.symm (actT g ω))', 'nativeGate2_conj': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) : NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)', 'nativeGate_of_conj': '{d : ℕ} {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)', 'dim_of_nativeGate2_conj': '{d : ℕ} {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d) (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3', 'three_of_nativeGate2_conj_of_two_le': '{d : ℕ} (hd : 2 ≤ d) {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d) (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3', 'dim_of_nativeGate2_conj_neg': '{d : ℕ} {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x) (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d) (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3', 'swap01_swap01': '(v : Fin 3 → ℝ) : swap01 (swap01 v) = v', 'swap01_mem': '{v : Fin 3 → ℝ} (hv : v ∈ eball 3) : swap01 v ∈ eball 3', 'swap01_z3': ': swap01 z3 = z3', 'swapped_nativeGate2': ': NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01) (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ actTEq swap01 swap01 swap01_swap01 swap01_swap01)', 'swapped_not_ne': ': swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip', 'swapped_nativeGate': ': NativeGate (eball 3) z3 nflip (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ actTEq swap01 swap01 swap01_swap01 swap01_swap01) ≪≫ₗ actTEq swap01 swap01 swap01_swap01 swap01_swap01)'}
PREAMBLE = 'import OIBridge.DenseOrbit\n\nnamespace OIBridge\nnamespace CopyCovariance\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction\nopen TransitiveBody CompositeDimension K2Guard DenseOrbit\n\nnoncomputable section\n'
CONTEXT = ['namespace OIBridge', 'namespace CopyCovariance', 'open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction', 'open TransitiveBody CompositeDimension K2Guard DenseOrbit', 'noncomputable section', 'variable {d : ℕ}', 'end', 'end CopyCovariance', 'end OIBridge']
RED_NAMES = ["homMap_comp'", "homMap_id'", "actT_comp'", "actT_id'", 'actT_congr', "lin_apply_eq_sum'", "lin_lin_comm'", "actC_actT_comm'", 'actTEq', 'sum_mul_ehom', 'affine_linear_apply', 'sum_homMap_mul_ehom', 'prodEffVal_actT', 'isEffectOn_comp', 'actT_mem_maxCone', 'NativeGate2', 'nativeGate2_of_nativeGate', 'nativeGate_of_nativeGate2', 'map_corner_of_fix', 'conjGate_apply', 'conjGate_symm_apply', 'nativeGate2_conj', 'nativeGate_of_conj', 'dim_of_nativeGate2_conj', 'three_of_nativeGate2_conj_of_two_le', 'dim_of_nativeGate2_conj_neg']
POS_NAMES = ['swapped_nativeGate2', 'swapped_not_ne']
POS_DEPS = ['NativeGate2', 'actTEq', 'swap01']
Q_RED_HEADLINES = ['nativeGate2_conj', 'nativeGate_of_conj', 'dim_of_nativeGate2_conj', 'three_of_nativeGate2_conj_of_two_le', 'dim_of_nativeGate2_conj_neg']
PROOF_PINNED = {'dim_of_nativeGate2_conj|dim_of_nativeGate': 'OIBridge.CompositeDimension.dim_of_nativeGate', 'three_of_nativeGate2_conj_of_two_le|three_of_nativeGate_of_two_le': 'OIBridge.K2Guard.three_of_nativeGate_of_two_le'}
PROOF_PINNED_KEYS = [['dim_of_nativeGate2_conj', 'dim_of_nativeGate'], ['three_of_nativeGate2_conj_of_two_le', 'three_of_nativeGate_of_two_le']]
RESOLVED = {'NativeGate2|W': ['OIBridge.CompositeDimension.W'], 'NativeGate2|actC': ['OIBridge.CompositeDimension.actC'], 'NativeGate2|actT': ['OIBridge.CompositeDimension.actT'], 'NativeGate2|corner': ['OIBridge.CompositeDimension.corner'], 'NativeGate2|maxCone': ['OIBridge.CompositeDimension.maxCone'], 'NativeGate2|prodState': ['OIBridge.CompositeDimension.prodState'], "actC_actT_comm'|W": ['OIBridge.CompositeDimension.W'], "actC_actT_comm'|actC": ['OIBridge.CompositeDimension.actC'], "actC_actT_comm'|actT": ['OIBridge.CompositeDimension.actT'], 'actTEq|W': ['OIBridge.CompositeDimension.W'], 'actTEq|actT': ['OIBridge.CompositeDimension.actT'], 'actTEq|actT_apply': ['OIBridge.CompositeDimension.actT_apply'], "actTEq|actT_comp'": ["OIBridge.CopyCovariance.actT_comp'"], 'actTEq|actT_congr': ['OIBridge.CopyCovariance.actT_congr'], "actTEq|actT_id'": ["OIBridge.CopyCovariance.actT_id'"], "actT_comp'|W": ['OIBridge.CompositeDimension.W'], "actT_comp'|actT": ['OIBridge.CompositeDimension.actT'], 'actT_congr|W': ['OIBridge.CompositeDimension.W'], 'actT_congr|actT': ['OIBridge.CompositeDimension.actT'], "actT_id'|W": ['OIBridge.CompositeDimension.W'], "actT_id'|actT": ['OIBridge.CompositeDimension.actT'], 'actT_mem_maxCone|W': ['OIBridge.CompositeDimension.W'], 'actT_mem_maxCone|actT': ['OIBridge.CompositeDimension.actT'], 'actT_mem_maxCone|maxCone': ['OIBridge.CompositeDimension.maxCone'], 'conjGate_apply|W': ['OIBridge.CompositeDimension.W'], 'conjGate_apply|actT': ['OIBridge.CompositeDimension.actT'], 'conjGate_apply|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'conjGate_symm_apply|W': ['OIBridge.CompositeDimension.W'], 'conjGate_symm_apply|actT': ['OIBridge.CompositeDimension.actT'], 'conjGate_symm_apply|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'dim_of_nativeGate2_conj|IsNot': ['OIBridge.CompositeDimension.IsNot'], 'dim_of_nativeGate2_conj|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'dim_of_nativeGate2_conj|W': ['OIBridge.CompositeDimension.W'], 'dim_of_nativeGate2_conj|dim_of_nativeGate#proof': ['OIBridge.CompositeDimension.dim_of_nativeGate'], 'dim_of_nativeGate2_conj|eball': ['OIBridge.TransitiveBody.eball'], 'dim_of_nativeGate2_conj_neg|IsNot': ['OIBridge.CompositeDimension.IsNot'], 'dim_of_nativeGate2_conj_neg|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'dim_of_nativeGate2_conj_neg|W': ['OIBridge.CompositeDimension.W'], 'dim_of_nativeGate2_conj_neg|eball': ['OIBridge.TransitiveBody.eball'], "homMap_comp'|HVec": ['OIBridge.CompositeDimension.HVec'], "homMap_comp'|homMap": ['OIBridge.CompositeDimension.homMap'], "homMap_id'|HVec": ['OIBridge.CompositeDimension.HVec'], "homMap_id'|homMap": ['OIBridge.CompositeDimension.homMap'], 'isEffectOn_comp|IsEffectOn': ['OIBridge.KInfFoundations.IsEffectOn'], 'map_corner_of_fix|corner': ['OIBridge.CompositeDimension.corner'], 'nativeGate2_conj|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'nativeGate2_conj|W': ['OIBridge.CompositeDimension.W'], 'nativeGate2_conj|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'nativeGate2_of_nativeGate|NativeGate': ['OIBridge.CompositeDimension.NativeGate'], 'nativeGate2_of_nativeGate|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'nativeGate2_of_nativeGate|W': ['OIBridge.CompositeDimension.W'], 'nativeGate_of_conj|NativeGate': ['OIBridge.CompositeDimension.NativeGate'], 'nativeGate_of_conj|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'nativeGate_of_conj|W': ['OIBridge.CompositeDimension.W'], 'nativeGate_of_conj|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'nativeGate_of_nativeGate2|NativeGate': ['OIBridge.CompositeDimension.NativeGate'], 'nativeGate_of_nativeGate2|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'nativeGate_of_nativeGate2|W': ['OIBridge.CompositeDimension.W'], 'prodEffVal_actT|W': ['OIBridge.CompositeDimension.W'], 'prodEffVal_actT|actT': ['OIBridge.CompositeDimension.actT'], 'prodEffVal_actT|prodEffVal': ['OIBridge.CompositeDimension.prodEffVal'], 'sum_homMap_mul_ehom|HVec': ['OIBridge.CompositeDimension.HVec'], 'sum_homMap_mul_ehom|ehom': ['OIBridge.CompositeDimension.ehom'], 'sum_homMap_mul_ehom|homMap': ['OIBridge.CompositeDimension.homMap'], 'sum_mul_ehom|HVec': ['OIBridge.CompositeDimension.HVec'], 'sum_mul_ehom|ehom': ['OIBridge.CompositeDimension.ehom'], 'swap01|vec3_ext': ['OIBridge.KInfFoundations.vec3_ext'], 'swap01_mem|eball': ['OIBridge.TransitiveBody.eball'], 'swap01_mem|swap01': ['OIBridge.CopyCovariance.swap01'], 'swap01_swap01|swap01': ['OIBridge.CopyCovariance.swap01'], 'swap01_z3|swap01': ['OIBridge.CopyCovariance.swap01'], 'swap01_z3|z3': ['OIBridge.CompositeDimension.z3'], 'swapped_nativeGate|NativeGate': ['OIBridge.CompositeDimension.NativeGate'], 'swapped_nativeGate|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'swapped_nativeGate|cnot': ['OIBridge.CompositeDimension.cnot'], 'swapped_nativeGate|eball': ['OIBridge.TransitiveBody.eball'], 'swapped_nativeGate|nflip': ['OIBridge.CompositeDimension.nflip'], 'swapped_nativeGate|swap01': ['OIBridge.CopyCovariance.swap01'], 'swapped_nativeGate|swap01_swap01': ['OIBridge.CopyCovariance.swap01_swap01'], 'swapped_nativeGate|z3': ['OIBridge.CompositeDimension.z3'], 'swapped_nativeGate2|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'swapped_nativeGate2|actTEq': ['OIBridge.CopyCovariance.actTEq'], 'swapped_nativeGate2|cnot': ['OIBridge.CompositeDimension.cnot'], 'swapped_nativeGate2|eball': ['OIBridge.TransitiveBody.eball'], 'swapped_nativeGate2|nflip': ['OIBridge.CompositeDimension.nflip'], 'swapped_nativeGate2|swap01': ['OIBridge.CopyCovariance.swap01'], 'swapped_nativeGate2|swap01_swap01': ['OIBridge.CopyCovariance.swap01_swap01'], 'swapped_nativeGate2|z3': ['OIBridge.CompositeDimension.z3'], 'swapped_not_ne|nflip': ['OIBridge.CompositeDimension.nflip'], 'swapped_not_ne|swap01': ['OIBridge.CopyCovariance.swap01'], 'three_of_nativeGate2_conj_of_two_le|IsNot': ['OIBridge.CompositeDimension.IsNot'], 'three_of_nativeGate2_conj_of_two_le|NativeGate2': ['OIBridge.CopyCovariance.NativeGate2'], 'three_of_nativeGate2_conj_of_two_le|W': ['OIBridge.CompositeDimension.W'], 'three_of_nativeGate2_conj_of_two_le|eball': ['OIBridge.TransitiveBody.eball'], 'three_of_nativeGate2_conj_of_two_le|three_of_nativeGate_of_two_le#proof': ['OIBridge.K2Guard.three_of_nativeGate_of_two_le']}
PINNED = {'NativeGate': 'OIBridge.CompositeDimension.NativeGate', 'IsNot': 'OIBridge.CompositeDimension.IsNot', 'actT': 'OIBridge.CompositeDimension.actT', 'actC': 'OIBridge.CompositeDimension.actC', 'maxCone': 'OIBridge.CompositeDimension.maxCone', 'prodState': 'OIBridge.CompositeDimension.prodState', 'corner': 'OIBridge.CompositeDimension.corner', 'W': 'OIBridge.CompositeDimension.W', 'eball': 'OIBridge.TransitiveBody.eball'}
EARNED = "DIM-1's selector holds for two-NOT native-gate data whose target NOT is the conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis; the two known two-NOT countermodels at d = 5 and d = 7 violate that condition on their exact data."
NONINF = "this round does not show that OI supplies a conjugator between the copies' NOTs, a NOT, a native gate or a ball; adopts no premise; and makes no manuscript claim. It does not show that type covariance admits any gate that copy naturality excludes: the positive control's gate is also a one-NOT native gate with the target NOT. The equivalence, for NOTs of the ball, between type covariance and equal ±1 eigenspace dimensions is a written argument and is not part of this round. Positivity of the J/K maps is not re-checked. The probe is an exact computation, not a Lean kernel proof."
PREREG_TEXTS = {'earned reading': "DIM-1's selector holds for two-NOT native-gate data whose target NOT is the conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis; the two known two-NOT countermodels at d = 5 and d = 7 violate that condition on their exact data.", 'non-inference rule': "this round does not show that OI supplies a conjugator between the copies' NOTs, a NOT, a native gate or a ball; adopts no premise; and makes no manuscript claim. It does not show that type covariance admits any gate that copy naturality excludes: the positive control's gate is also a one-NOT native gate with the target NOT. The equivalence, for NOTs of the ball, between type covariance and equal ±1 eigenspace dimensions is a written argument and is not part of this round. Positivity of the J/K maps is not re-checked. The probe is an exact computation, not a Lean kernel proof.", 'census family': "type covariance of native inversion suffices for DIM-1's selector: two-NOT native-gate data whose target NOT is the conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis reduce to a one-NOT native gate (round KINF-COPY-1, reconstruction)", "declaration homMap_comp'": "homMap_comp'", "declaration homMap_id'": "homMap_id'", "declaration actT_comp'": "actT_comp'", "declaration actT_id'": "actT_id'", 'declaration actT_congr': 'actT_congr', "declaration lin_apply_eq_sum'": "lin_apply_eq_sum'", "declaration lin_lin_comm'": "lin_lin_comm'", "declaration actC_actT_comm'": "actC_actT_comm'", 'declaration actTEq': 'actTEq', 'declaration sum_mul_ehom': 'sum_mul_ehom', 'declaration affine_linear_apply': 'affine_linear_apply', 'declaration sum_homMap_mul_ehom': 'sum_homMap_mul_ehom', 'declaration prodEffVal_actT': 'prodEffVal_actT', 'declaration isEffectOn_comp': 'isEffectOn_comp', 'declaration actT_mem_maxCone': 'actT_mem_maxCone', 'declaration NativeGate2': 'NativeGate2', 'declaration nativeGate2_of_nativeGate': 'nativeGate2_of_nativeGate', 'declaration nativeGate_of_nativeGate2': 'nativeGate_of_nativeGate2', 'declaration map_corner_of_fix': 'map_corner_of_fix', 'declaration conjGate_apply': 'conjGate_apply', 'declaration conjGate_symm_apply': 'conjGate_symm_apply', 'declaration nativeGate2_conj': 'nativeGate2_conj', 'declaration nativeGate_of_conj': 'nativeGate_of_conj', 'declaration dim_of_nativeGate2_conj': 'dim_of_nativeGate2_conj', 'declaration three_of_nativeGate2_conj_of_two_le': 'three_of_nativeGate2_conj_of_two_le', 'declaration dim_of_nativeGate2_conj_neg': 'dim_of_nativeGate2_conj_neg', 'declaration swap01': 'swap01', 'declaration swap01_swap01': 'swap01_swap01', 'declaration swap01_mem': 'swap01_mem', 'declaration swap01_z3': 'swap01_z3', 'declaration swapped_nativeGate2': 'swapped_nativeGate2', 'declaration swapped_not_ne': 'swapped_not_ne', 'declaration swapped_nativeGate': 'swapped_nativeGate'}
DESIGN_HEADER = "/-\n  OIBridge/CopyCovariance.lean — design module of the research thread `research/equivalence`\n  (node E8, draft S2): the predicted module of round KINF-COPY-1, split from the design modules\n  `EqvSeams` (§B–§D) and `EqvSeamsControl`, built in run 38083519826, with no statement changed.\n  Not adopted, not certified, not a round.\n\n  `NativeGate2` is DIM-1's `NativeGate` with two NOTs, `NC` on the control copy and `NT` on the\n  target copy. Conjugating such data on the target copy by a linear automorphism of the body fixing\n  the corner axis gives two-NOT data with the target NOT conjugated (`nativeGate2_conj`); when `NT`\n  is the conjugate of `NC` by such an automorphism (type covariance), the conjugated gate is a native\n  gate with the single NOT `NC` (`nativeGate_of_conj`) and DIM-1's selector applies\n  (`dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg`).\n  §E: the swapped `cnot` at `d = 3` is two-NOT data with distinct NOTs (`swapped_nativeGate2`,\n  `swapped_not_ne`); it is also a one-NOT native gate with the target NOT (`swapped_nativeGate`).\n  Every hypothesis is a premise; nothing here sources a conjugator, a NOT or a gate.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/"
PRED_HEADER = "/-\n  OIBridge/CopyCovariance.lean — round KINF-COPY-1: type covariance of native inversion and\n  DIM-1's selector for two-NOT native-gate data.\n\n  `NativeGate2` is DIM-1's `NativeGate` with two NOTs, `NC` on the control copy and `NT` on the\n  target copy. Conjugating such data on the target copy by a linear automorphism of the body fixing\n  the corner axis gives two-NOT data with the target NOT conjugated (`nativeGate2_conj`); when `NT`\n  is the conjugate of `NC` by such an automorphism (type covariance), the conjugated gate is a native\n  gate with the single NOT `NC` (`nativeGate_of_conj`) and DIM-1's selector applies\n  (`dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg`).\n  §E: the swapped `cnot` at `d = 3` is two-NOT data with distinct NOTs (`swapped_nativeGate2`,\n  `swapped_not_ne`); its reduction is a native gate with the single NOT `nflip`\n  (`swapped_nativeGate`).\n  Every hypothesis is a premise; nothing here sources a conjugator, a NOT or a gate.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/"
BODY = "\nimport OIBridge.DenseOrbit\n\nnamespace OIBridge\nnamespace CopyCovariance\n\nopen Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction\nopen TransitiveBody CompositeDimension K2Guard DenseOrbit\n\nnoncomputable section\n\n/-! ### §B — the token-action calculus at every dimension -/\n\nvariable {d : ℕ}\n\ntheorem homMap_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :\n    homMap (M ∘ₗ N) v = homMap M (homMap N v) := by\n  funext μ\n  refine Fin.cases ?_ (fun j => ?_) μ\n  · rfl\n  · rw [homMap_succ, homMap_succ, vecTail_homMap, LinearMap.comp_apply]\n\ntheorem homMap_id' (v : HVec d) : homMap LinearMap.id v = v := by\n  funext μ\n  refine Fin.cases ?_ (fun j => ?_) μ\n  · rfl\n  · rw [homMap_succ, LinearMap.id_apply]; rfl\n\ntheorem actT_comp' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :\n    actT M (actT N ω) = actT (M ∘ₗ N) ω := by\n  funext μ\n  show homMap M (homMap N (ω μ)) = homMap (M ∘ₗ N) (ω μ)\n  rw [homMap_comp']\n\ntheorem actT_id' (ω : W d) : actT LinearMap.id ω = ω := by\n  funext μ\n  exact homMap_id' (ω μ)\n\ntheorem actT_congr {M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (h : ∀ x, M x = N x) (ω : W d) :\n    actT M ω = actT N ω := by\n  rw [LinearMap.ext h]\n\ntheorem lin_apply_eq_sum' (M : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x : Fin d → ℝ) (i : Fin d) :\n    M x i = ∑ k, LinearMap.toMatrix' M i k * x k :=\n  (congrFun (LinearMap.toMatrix'_mulVec M x) i).symm\n\ntheorem lin_lin_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (Ω' : Fin d → Fin d → ℝ)\n    (i j : Fin d) :\n    M (fun i' => N (Ω' i') j) i = N (fun j' => M (fun i' => Ω' i' j') i) j := by\n  simp only [lin_apply_eq_sum' M, lin_apply_eq_sum' N, Finset.mul_sum]\n  rw [Finset.sum_comm]\n  refine Finset.sum_congr rfl fun l _ => Finset.sum_congr rfl fun k _ => ?_\n  ring\n\n/-- The two token actions commute, at every dimension. -/\ntheorem actC_actT_comm' (M N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :\n    actC M (actT N ω) = actT N (actC M ω) := by\n  funext μ ν\n  refine Fin.cases ?_ (fun i => ?_) μ <;> refine Fin.cases ?_ (fun j => ?_) ν\n  · rfl\n  · rfl\n  · rfl\n  · simp only [actC_apply, actT_apply, homMap_succ, Matrix.vecTail, Function.comp_def]\n    exact lin_lin_comm' M N (fun i' j' => ω i'.succ j'.succ) i j\n\n/-- The target action of a linear map with a two-sided inverse, as a linear equivalence. -/\ndef actTEq (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) : W d ≃ₗ[ℝ] W d where\n  toFun := actT g\n  invFun := actT h\n  map_add' ω₁ ω₂ := by\n    funext μ ν\n    simp only [actT_apply, Pi.add_apply, map_add]\n  map_smul' c ω := by\n    funext μ ν\n    simp only [actT_apply, Pi.smul_apply, map_smul, smul_eq_mul, RingHom.id_apply]\n  left_inv ω := by\n    show actT h (actT g ω) = ω\n    rw [actT_comp', actT_congr (M := h ∘ₗ g) (N := LinearMap.id)\n      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hhg x), actT_id']\n  right_inv ω := by\n    show actT g (actT h ω) = ω\n    rw [actT_comp', actT_congr (M := g ∘ₗ h) (N := LinearMap.id)\n      (fun x => by simp only [LinearMap.comp_apply, LinearMap.id_apply]; exact hgh x), actT_id']\n\n/-! ### §C — the maximal cone under a body-preserving map of one copy -/\n\n/-- The homogenized pairing of a vector with the coefficients of an affine functional. -/\ntheorem sum_mul_ehom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (v : HVec d) :\n    ∑ ν, v ν * ehom e ν = v 0 * e 0 + e.linear (Matrix.vecTail v) := by\n  rw [Fin.sum_univ_succ, LinearMap.pi_apply_eq_sum_univ e.linear (Matrix.vecTail v)]\n  congr 1\n  all_goals first\n    | rfl\n    | (refine Finset.sum_congr rfl fun j _ => ?_\n       simp only [ehom, Matrix.cons_val_succ, smul_eq_mul, Matrix.vecTail, Function.comp_apply])\n\ntheorem affine_linear_apply (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :\n    f.linear x = f x - f 0 := by\n  have hd := congrFun (AffineMap.decomp f) x\n  simp only [Pi.add_apply] at hd\n  linarith\n\ntheorem sum_homMap_mul_ehom (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n    (v : HVec d) :\n    ∑ ν, homMap g v ν * ehom f ν = ∑ ν, v ν * ehom (f.comp g.toAffineMap) ν := by\n  rw [sum_mul_ehom, sum_mul_ehom, homMap_zero, vecTail_homMap, affine_linear_apply f,\n    affine_linear_apply (f.comp g.toAffineMap)]\n  simp only [AffineMap.comp_apply, LinearMap.coe_toAffineMap, map_zero]\n\n/-- A product effect read after a target-side map is the product effect with the target factor\npulled back. -/\ntheorem prodEffVal_actT (g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ)\n    (ω : W d) : prodEffVal e f (actT g ω) = prodEffVal e (f.comp g.toAffineMap) ω := by\n  unfold prodEffVal pairVal\n  refine Finset.sum_congr rfl fun μ _ => ?_\n  calc ∑ ν, ehom e μ * actT g ω μ ν * ehom f ν\n      = ehom e μ * ∑ ν, homMap g (ω μ) ν * ehom f ν := by\n        rw [Finset.mul_sum]\n        refine Finset.sum_congr rfl fun ν _ => ?_\n        rw [actT_apply]\n        ring\n    _ = ehom e μ * ∑ ν, ω μ ν * ehom (f.comp g.toAffineMap) ν := by\n        rw [sum_homMap_mul_ehom]\n    _ = ∑ ν, ehom e μ * ω μ ν * ehom (f.comp g.toAffineMap) ν := by\n        rw [Finset.mul_sum]\n        refine Finset.sum_congr rfl fun ν _ => ?_\n        ring\n\ntheorem isEffectOn_comp {Ω : Set (Fin d → ℝ)} {f : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (hf : IsEffectOn Ω f)\n    {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hg : ∀ x ∈ Ω, g x ∈ Ω) :\n    IsEffectOn Ω (f.comp g.toAffineMap) := by\n  intro x hx\n  simpa only [AffineMap.comp_apply, LinearMap.coe_toAffineMap] using hf (g x) (hg x hx)\n\n/-- A target-side linear map carrying the body into itself preserves the maximal cone. -/\ntheorem actT_mem_maxCone {Ω : Set (Fin d → ℝ)} {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hg : ∀ x ∈ Ω, g x ∈ Ω) {ω : W d} (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω := by\n  intro e f he hf\n  rw [prodEffVal_actT]\n  exact hω e _ he (isEffectOn_comp hf hg)\n\n/-! ### §D — two NOTs, and the conjugation reduction -/\n\n/-- DIM-1's native-gate hypotheses with two NOTs: `NC` on the control copy, `NT` on the target\ncopy. With `NC = NT` it is `NativeGate` (`nativeGate2_of_nativeGate`, `nativeGate_of_nativeGate2`). -/\nstructure NativeGate2 (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ)\n    (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where\n  frame : ∀ a b : Fin 2,\n    G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))\n  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω\n  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n  relT : ∀ ω, actT NT (G (actT NT ω)) = G ω\n  relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)\n\ntheorem nativeGate2_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate Ω z N G) :\n    NativeGate2 Ω z N N G :=\n  ⟨h.frame, h.posFwd, h.posInv, h.relT, h.relC⟩\n\ntheorem nativeGate_of_nativeGate2 {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (h : NativeGate2 Ω z N N G) :\n    NativeGate Ω z N G :=\n  ⟨h.frame, h.posFwd, h.posInv, h.relT, h.relC⟩\n\ntheorem map_corner_of_fix {g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {z : Fin d → ℝ} (hgz : g z = z)\n    (b : Fin 2) : g (corner z b) = corner z b := by\n  fin_cases b\n  · first\n      | exact hgz\n      | simp [corner, hgz]\n  · first\n      | (show g (-z) = -z; rw [map_neg, hgz])\n      | simp [corner, hgz]\n\n/-- The conjugated gate applied: `actT h ∘ G ∘ actT g`. -/\ntheorem conjGate_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :\n    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) ω = actT h (G (actT g ω)) := rfl\n\ntheorem conjGate_symm_apply (g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (hgh : ∀ x, g (h x) = x)\n    (hhg : ∀ x, h (g x) = x) (G : W d ≃ₗ[ℝ] W d) (ω : W d) :\n    (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh).symm ω = actT h (G.symm (actT g ω)) :=\n  rfl\n\n/-- **Conjugation on the target copy.** Two-NOT native-gate data, conjugated on the target copy by\na linear automorphism of the body fixing the corner axis, are two-NOT native-gate data with the\ntarget NOT conjugated. -/\ntheorem nativeGate2_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :\n    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) := by\n  have hhz : h z = z := by\n    have hz := hhg z\n    rwa [hgz] at hz\n  have eT1 : ∀ X : W d, actT (h ∘ₗ NT ∘ₗ g) (actT h X) = actT h (actT NT X) := fun X => by\n    rw [actT_comp', actT_comp']\n    exact actT_congr (fun x => by simp only [LinearMap.comp_apply, hgh]) X\n  have eT2 : ∀ X : W d, actT g (actT (h ∘ₗ NT ∘ₗ g) X) = actT NT (actT g X) := fun X => by\n    rw [actT_comp', actT_comp']\n    exact actT_congr (fun x => by simp only [LinearMap.comp_apply, hgh]) X\n  refine ⟨fun a b => ?_, fun x hx y hy => ?_, fun x hx y hy => ?_, fun ω => ?_, fun ω => ?_⟩\n  · rw [conjGate_apply, actT_prodState, map_corner_of_fix hgz, hG.frame, actT_prodState,\n      map_corner_of_fix hhz]\n  · rw [conjGate_apply, actT_prodState]\n    exact actT_mem_maxCone hhΩ (hG.posFwd x hx (g y) (hgΩ y hy))\n  · rw [conjGate_symm_apply, actT_prodState]\n    exact actT_mem_maxCone hhΩ (hG.posInv x hx (g y) (hgΩ y hy))\n  · rw [conjGate_apply, conjGate_apply, eT1, eT2, hG.relT]\n  · rw [conjGate_apply, conjGate_apply, ← actC_actT_comm' NC g ω, actC_actT_comm' NC h, hG.relC, eT1]\n\n/-- **Type covariance of native inversion suffices.** If the target NOT is the conjugate of the\ncontrol NOT by a linear automorphism of the body fixing the corner axis, the conjugated gate is a\nnative gate with the single NOT `NC`. -/\ntheorem nativeGate_of_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)\n    (hcov : ∀ x, NT (g x) = g (NC x)) :\n    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh) := by\n  have h2 := nativeGate2_conj hG hgh hhg hgΩ hhΩ hgz\n  have hN : h ∘ₗ NT ∘ₗ g = NC := LinearMap.ext fun x => by\n    simp only [LinearMap.comp_apply, hcov, hhg]\n  rw [hN] at h2\n  exact nativeGate_of_nativeGate2 h2\n\n/-- **The selector under type covariance.** DIM-1's `dim_of_nativeGate` through the reduction. -/\ntheorem dim_of_nativeGate2_conj {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=\n  dim_of_nativeGate hN (nativeGate_of_conj hG hgh hhg hgΩ hhΩ hgz hcov)\n\n/-- **Three under type covariance and `2 ≤ d`.** K2-GUARD-1's selector through the reduction. -/\ntheorem three_of_nativeGate2_conj_of_two_le (hd : 2 ≤ d) {z : Fin d → ℝ}\n    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n    (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3 :=\n  three_of_nativeGate_of_two_le hd hN (nativeGate_of_conj hG hgh hhg hgΩ hhΩ hgz hcov)\n\n/-- **A conjugator reversing the corner axis.** Composed with `NC` it fixes the axis and still\nconjugates `NC` to `NT`, so the selector applies. -/\ntheorem dim_of_nativeGate2_conj_neg {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G)\n    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)\n    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)\n    (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 := by\n  refine dim_of_nativeGate2_conj (g := g ∘ₗ NC) (h := NC ∘ₗ h) hN hG ?_ ?_ ?_ ?_ ?_ ?_\n  · intro x\n    simp only [LinearMap.comp_apply, hN.invol, hgh]\n  · intro x\n    simp only [LinearMap.comp_apply, hhg, hN.invol]\n  · intro x hx\n    simp only [LinearMap.comp_apply]\n    exact hgΩ _ (hN.preserves x hx)\n  · intro x hx\n    simp only [LinearMap.comp_apply]\n    exact hN.preserves _ (hhΩ x hx)\n  · simp only [LinearMap.comp_apply, hN.flips, map_neg, hgz, neg_neg]\n  · intro x\n    simp only [LinearMap.comp_apply, hcov, hN.invol]\n\n/-! ### §E — the positive control at `d = 3` -/\n\n/-- The exchange of the first two axes of one copy. -/\ndef swap01 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where\n  toFun v := ![v 1, v 0, v 2]\n  map_add' v w := by apply vec3_ext <;> rfl\n  map_smul' r v := by apply vec3_ext <;> rfl\n\ntheorem swap01_swap01 (v : Fin 3 → ℝ) : swap01 (swap01 v) = v := by\n  apply vec3_ext <;> rfl\n\ntheorem swap01_mem {v : Fin 3 → ℝ} (hv : v ∈ eball 3) : swap01 v ∈ eball 3 := by\n  rw [eball_three] at hv ⊢\n  rw [mem_ball3] at hv ⊢\n  show v 1 ^ 2 + v 0 ^ 2 + v 2 ^ 2 ≤ 1\n  linarith\n\ntheorem swap01_z3 : swap01 z3 = z3 := by\n  apply vec3_ext <;> rfl\n\n/-- **Two-NOT data with distinct NOTs.** -/\ntheorem swapped_nativeGate2 :\n    NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)\n      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ\n        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=\n  nativeGate2_conj (nativeGate2_of_nativeGate nativeGate_cnot) swap01_swap01 swap01_swap01\n    (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3\n\n/-- The two NOTs of `swapped_nativeGate2` differ: at the first axis the target NOT is `−1` and the\ncontrol NOT is `1`. -/\ntheorem swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip := by\n  intro h\n  have h0 := congrArg (fun L : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) => L ![1, 0, 0] 0) h\n  have hl : (swap01 ∘ₗ nflip ∘ₗ swap01) ![1, 0, 0] 0 = -1 := by\n    show nflip (swap01 ![1, 0, 0]) 1 = -1\n    rw [nflip_one]\n    show -((![1, 0, 0] : Fin 3 → ℝ) 0) = -1\n    norm_num\n  have hr : nflip ![1, 0, 0] 0 = 1 := by\n    rw [nflip_zero']\n    rfl\n  have h1 : (swap01 ∘ₗ nflip ∘ₗ swap01) ![1, 0, 0] 0 = nflip ![1, 0, 0] 0 := h0\n  rw [hl, hr] at h1\n  norm_num at h1\n\n/-- The reduction carries the swapped data back to a native gate with the single NOT `nflip`. -/\ntheorem swapped_nativeGate :\n    NativeGate (eball 3) z3 nflip\n      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ\n        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ\n          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ≪≫ₗ\n        actTEq swap01 swap01 swap01_swap01 swap01_swap01) :=\n  nativeGate_of_conj swapped_nativeGate2 swap01_swap01 swap01_swap01\n    (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3\n    (fun x => by simp only [LinearMap.comp_apply, swap01_swap01])\n\nend\n\nend CopyCovariance\nend OIBridge\n\n#print axioms OIBridge.CopyCovariance.actC_actT_comm'\n#print axioms OIBridge.CopyCovariance.actTEq\n#print axioms OIBridge.CopyCovariance.prodEffVal_actT\n#print axioms OIBridge.CopyCovariance.actT_mem_maxCone\n#print axioms OIBridge.CopyCovariance.nativeGate2_conj\n#print axioms OIBridge.CopyCovariance.nativeGate_of_conj\n#print axioms OIBridge.CopyCovariance.dim_of_nativeGate2_conj\n#print axioms OIBridge.CopyCovariance.three_of_nativeGate2_conj_of_two_le\n#print axioms OIBridge.CopyCovariance.dim_of_nativeGate2_conj_neg\n#print axioms OIBridge.CopyCovariance.swapped_nativeGate2\n#print axioms OIBridge.CopyCovariance.swapped_not_ne\n#print axioms OIBridge.CopyCovariance.swapped_nativeGate\n"
DESIGN_BLOB = 'fb9c73fe804cc96d09c450a9036e11612e151ea2'
PRED_BLOB = '70e2f62187c1f2905c9db7c651d26db0accf8d60'
PROBE_TEXT = '"""E2 probe 1 -- K-inf-Copy: is "type covariance of native inversion" a sufficient weakening?  (exact; Fractions)\n\nQUESTION (ROADMAP.md:1027-1030 at L).  Copy naturality (one NOT N in both of DIM-1\'s relations) is load-bearing: the\ntwo-NOT J/K maps of NB-1 at d = 5 and d = 7 meet every two-copy relation with mismatched NOTs.  The candidate weakening:\nthe target copy\'s NOT is the conjugate of the control copy\'s NOT by a body automorphism fixing the corner axis\n("type covariance").  The design module EqvSeams (branch dev-equivalence/kinf-seams) states the reduction\n(two-NOT data + type covariance => a one-NOT native gate, hence d in {1, 3}); this probe checks it on instances and\nchecks that the surviving countermodels are excluded by the weaker premise.\n\nREPRESENTATION.  W d = (d+1) x (d+1) real tables w[c][t] (c control index, t target index; index 0 = unit u,\nindex d = the corner axis z).  A NOT or a local map is given by its homogenized (d+1) x (d+1) matrix H (H[0][0] = 1).\n  actT H w = w H^T   (target index),   actC H w = H w   (control index)        [CompositeDimension.lean:198-203]\n  prodState x y = hom(x) hom(y)^T,  corners hom(+z) = u + z, hom(-z) = u - z.\nRelations (two-NOT reading, NC on the control side, NT on the target):\n  frame:  G(k_a (x) k_b) = k_a (x) k_(a+b)\n  relT :  actT NT (G (actT NT w)) = G w            for every w (checked on the full basis of W d)\n  relC :  actC NC (G (actC NC w)) = actT NT (G w)  for every w\nThe d = 3 gate `cnot` is PARSED from CompositeDimension.lean (sgn, pc, pt; cnotFun w mu nu = sgn * w (pc) (pt)).\nThe J/K maps are rebuilt here from NB-1\'s construction (data as in research/archive/threads/B/part2_three_copy.py:60-70\nand blib.jk_gate); every relation check below is this script\'s own code.\n\nCHECKS.\n  C1  kernel cnot with nflip: frame, relT, relC (one NOT)                          -- positive control of the code\n  C2  swapped gate G2 = actT s . cnot . actT s (s = swap of axes 0,1; s z = z): frame, relT(NT), relC(nflip, NT),\n      with NT = s nflip s\n  C3  NT != nflip; both involutive isometries flipping z with the same split (1,1)\n  C4  G2 has no one-NOT reading with the CONTROL copy\'s NOT: relT(nflip) fails for G2\n  C6  G2 DOES have a one-NOT reading with the target NOT: relT(NT) and relC(NT, NT) hold (observed in run 1;\n      re-checked here as a recorded fact, not a prediction)\n  C5  the reduction: actT s . G2 . actT s == cnot exactly, and it meets the one-NOT relations with nflip\n  J1  d = 5, 7 J/K maps: frame, relT(NB), relC(NA, NB) hold                         -- countermodel clauses re-derived\n  J2  d = 5, 7: split(NA) != split(NB) (exact ranks of H -/+ I); hence NA, NB are not similar, so no conjugator of any\n      kind exists and type covariance FAILS for these data\n  J3  d = 5, 7 one-NOT countercontrol: for N in {NA, NB}, relT(N) and relC(N, N) do not both hold (no one-NOT\n      reading of the J/K map with either NOT)\n  S1  transfer countercontrol: a shear g fixing z (g = diag(2,1,1) on R^3) does not preserve the ball, and\n      actT g carries the product state prodState(0, e0) (in maxCone) to a table on which the product effect\n      (unit) (x) (sharp effect along -e0) takes the value -1/2 < 0  -- the ball-preservation hypothesis of the\n      transfer lemma `actT_mem_maxCone` is load-bearing\nRUN HISTORY.  Run 1 (kept: e2_copy_conj.run1.{py,out,err}) did not render: two COUNTERCONTROL expectations were\nwrong -- the swapped gate G2 meets relT(NT) and relC(NT, NT) (so its old C4, "relC(NT, NT) fails", was false), and the\nd = 7 J/K map meets relT(NA) (so its old J3, "relT(NA) fails", was false at d = 7).  Both were over-specific forms of\n"no one-NOT reading"; C4 and J3 are restated above in the form the verdict needs, C6 records the run-1 fact, and no\ncheck of the reduction (C1-C3, C5, J1, J2, S1) was changed.\nDECISION RULE (fixed before run 2).  VERDICT TYPE-COVARIANCE-CONSISTENT is printed iff every check C1-C6, J1-J3, S1\npasses.  Otherwise the verdict line is "VERDICT NOT RENDERED" followed by the failing checks.\nThe verdict says only: on these instances the reduction behaves as the [D] theorem states, and the two known two-NOT\ncountermodels violate type covariance.  Positivity of the J/K maps is NOT re-checked here (thread B / NB-1, [A]); the\nswapped gate\'s positivity is the [D] theorem\'s (`actT_mem_maxCone`), not a check of this script.\n"""\nimport re\nimport sys\nfrom fractions import Fraction as Fr\n\nKERNEL = \'../lean-mathlib/OIBridge/CompositeDimension.lean\'\nRESULTS = []\n\n\ndef check(name, ok, detail=\'\'):\n    RESULTS.append((name, bool(ok)))\n    print(\'%s %s%s\' % (\'PASS\' if ok else \'FAIL\', name, (\' -- \' + detail) if detail else \'\'))\n\n\n# ------------------------------------------------------------------ linear algebra on tables\ndef zeros(n, m=None):\n    m = n if m is None else m\n    return [[Fr(0)] * m for _ in range(n)]\n\n\ndef eye(n):\n    M = zeros(n)\n    for i in range(n):\n        M[i][i] = Fr(1)\n    return M\n\n\ndef mm(A, B):\n    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Fr(0)) for j in range(len(B[0]))] for i in range(len(A))]\n\n\ndef tr(A):\n    return [list(r) for r in zip(*A)]\n\n\ndef diag(v):\n    M = zeros(len(v))\n    for i, x in enumerate(v):\n        M[i][i] = Fr(x)\n    return M\n\n\ndef rank(M):\n    M = [list(r) for r in M]\n    r = 0\n    rows, cols = len(M), len(M[0])\n    for c in range(cols):\n        p = next((i for i in range(r, rows) if M[i][c] != 0), None)\n        if p is None:\n            continue\n        M[r], M[p] = M[p], M[r]\n        for i in range(rows):\n            if i != r and M[i][c] != 0:\n                f = M[i][c] / M[r][c]\n                M[i] = [a - f * b for a, b in zip(M[i], M[r])]\n        r += 1\n        if r == rows:\n            break\n    return r\n\n\ndef split(H):\n    n = len(H)\n    I = eye(n)\n    plus = n - rank([[H[i][j] - I[i][j] for j in range(n)] for i in range(n)])\n    minus = n - rank([[H[i][j] + I[i][j] for j in range(n)] for i in range(n)])\n    return (plus - 1, minus - 1)  # transverse split (p, q): u is +1, z is -1\n\n\ndef actT(H, w):\n    return mm(w, tr(H))\n\n\ndef actC(H, w):\n    return mm(H, w)\n\n\ndef basis(n):\n    for c in range(n):\n        for t in range(n):\n            w = zeros(n)\n            w[c][t] = Fr(1)\n            yield w\n\n\ndef hom_corner(n, a):\n    v = [Fr(0)] * n\n    v[0] = Fr(1)\n    v[n - 1] = Fr(1) if a == 0 else Fr(-1)\n    return v\n\n\ndef prod_state(x, y):\n    return [[a * b for b in y] for a in x]\n\n\ndef frame_ok(G, n):\n    for a in (0, 1):\n        for b in (0, 1):\n            if G(prod_state(hom_corner(n, a), hom_corner(n, b))) != prod_state(hom_corner(n, a), hom_corner(n, a ^ b)):\n                return False\n    return True\n\n\ndef relT_ok(G, n, NT):\n    return all(actT(NT, G(actT(NT, w))) == G(w) for w in basis(n))\n\n\ndef relC_ok(G, n, NC, NT):\n    return all(actC(NC, G(actC(NC, w))) == actT(NT, G(w)) for w in basis(n))\n\n\ndef is_invol_isometry_flipping_z(H):\n    n = len(H)\n    return mm(H, H) == eye(n) and mm(tr(H), H) == eye(n) and [H[i][n - 1] for i in range(n)] == \\\n        [Fr(0)] * (n - 1) + [Fr(-1)]\n\n\n# ------------------------------------------------------------------ the kernel\'s d = 3 gate, parsed\ndef parse_table(src, name):\n    m = re.search(r\'def %s : Fin 4 → Fin 4 → Fin 4\\n((?:  \\|.*\\n)+)\' % name, src)\n    entries = re.findall(r\'(\\d), (\\d) => (\\d)\', m.group(1))\n    T = {(int(a), int(b)): int(c) for a, b, c in entries}\n    assert len(T) == 16\n    return T\n\n\ndef parse_sgn(src):\n    m = re.search(r\'def sgn \\(μ ν : Fin 4\\) : ℝ := if \\(μ = (\\d) ∧ ν = (\\d)\\) ∨ \\(μ = (\\d) ∧ ν = (\\d)\\) then -1 else 1\', src)\n    neg = {(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))}\n    return {(a, b): (Fr(-1) if (a, b) in neg else Fr(1)) for a in range(4) for b in range(4)}\n\n\nsrc = open(KERNEL, encoding=\'utf-8\').read()\nPC, PT, SGN = parse_table(src, \'pc\'), parse_table(src, \'pt\'), parse_sgn(src)\nnflip_m = re.search(r\'def nflip : \\(Fin 3 → ℝ\\) →ₗ\\[ℝ\\] \\(Fin 3 → ℝ\\) where\\n  toFun x := fun i => \\(!\\[(.*?)\\] : Fin 3 → ℝ\\) i \\* x i\', src)\nNFLIP_DIAG = [int(s.strip()) for s in nflip_m.group(1).split(\',\')]\nz3_m = re.search(r\'def z3 : Fin 3 → ℝ := !\\[(.*?)\\]\', src)\nZ3 = [int(s.strip()) for s in z3_m.group(1).split(\',\')]\nprint(\'parsed: pc, pt, sgn tables (16 entries each); nflip diagonal %s; z3 = %s\' % (NFLIP_DIAG, Z3))\nassert Z3 == [0, 0, 1], \'the probe assumes the corner axis is the last coordinate\'\n\n\ndef cnot(w):\n    return [[SGN[(m, v)] * w[PC[(m, v)]][PT[(m, v)]] for v in range(4)] for m in range(4)]\n\n\nNFLIP = diag([1] + NFLIP_DIAG)\nS = [[Fr(1), 0, 0, 0], [0, 0, Fr(1), 0], [0, Fr(1), 0, 0], [0, 0, 0, Fr(1)]]  # homogenized swap01\nS = [[Fr(x) for x in r] for r in S]\nNT3 = mm(mm(S, NFLIP), S)\n\nprint(\'== d = 3 (kernel cnot, nflip, swapped target)\')\ncheck(\'C1 kernel cnot meets frame, relT(nflip), relC(nflip, nflip)\',\n      frame_ok(cnot, 4) and relT_ok(cnot, 4, NFLIP) and relC_ok(cnot, 4, NFLIP, NFLIP))\n\n\ndef G2(w):\n    return actT(S, cnot(actT(S, w)))\n\n\ncheck(\'C2 G2 = actT s . cnot . actT s meets frame, relT(NT), relC(nflip, NT) with NT = s nflip s\',\n      frame_ok(G2, 4) and relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NFLIP, NT3),\n      \'NT diagonal %s\' % [str(NT3[i][i]) for i in range(4)])\ncheck(\'C3 NT != nflip; both involutive isometries flipping z; equal splits\',\n      NT3 != NFLIP and is_invol_isometry_flipping_z(NT3) and is_invol_isometry_flipping_z(NFLIP)\n      and split(NT3) == split(NFLIP), \'splits %s %s\' % (split(NFLIP), split(NT3)))\ncheck(\'C4 G2 has no one-NOT reading with the control NOT: relT(nflip) fails\', not relT_ok(G2, 4, NFLIP))\ncheck(\'C6 G2 has a one-NOT reading with the target NOT: relT(NT) and relC(NT, NT) hold (run-1 fact)\',\n      relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NT3, NT3))\n\n\ndef RED(w):\n    return actT(S, G2(actT(S, w)))\n\n\ncheck(\'C5 the reduction actT s . G2 . actT s equals cnot on the basis of W 3 and meets the one-NOT relations\',\n      all(RED(w) == cnot(w) for w in basis(4)) and frame_ok(RED, 4) and relT_ok(RED, 4, NFLIP)\n      and relC_ok(RED, 4, NFLIP, NFLIP))\n\n\n# ------------------------------------------------------------------ the J/K maps (NB-1\'s construction)\ndef jk_gate(d, NB, J, K):\n    """NB-1\'s J/K map, M_0 = I (rebuilt from research/archive/threads/B/blib.py:249).  Returns the gate as a\n    dict col -> {row: coef} on the flat index c*n + t."""\n    n = d + 1\n    plus = [i for i in range(1, d) if NB[i] == 1]\n    assert len(plus) == 1\n    x = plus[0]\n    G = {}\n    for j in range(n):\n        if NB[j] == 1:\n            G[0 * n + j] = {0 * n + j: Fr(1)}\n            G[d * n + j] = {d * n + j: Fr(1)}\n        else:\n            G[0 * n + j] = {d * n + j: Fr(1)}\n            G[d * n + j] = {0 * n + j: Fr(1)}\n    for c in range(1, d):\n        G[c * n + 0] = {c * n + x: Fr(1)}\n        G[c * n + x] = {c * n + 0: Fr(1)}\n        for j in range(1, n):\n            if NB[j] == -1:\n                s1, cc = J[c]\n                s2, l = K[j]\n                G[c * n + j] = {cc * n + l: Fr(s1 * s2)}\n    return G\n\n\ndef as_fun(Gd, n):\n    def f(w):\n        out = zeros(n)\n        for col, rows in Gd.items():\n            c0, t0 = divmod(col, n)\n            if w[c0][t0] != 0:\n                for row, coef in rows.items():\n                    r0, s0 = divmod(row, n)\n                    out[r0][s0] += coef * w[c0][t0]\n        return out\n    return f\n\n\nMODELS = {\n    5: dict(NB=[1, 1, -1, -1, -1, -1], NA=[1, 1, -1, 1, -1, -1],\n            J={1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}, K={2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}),\n    7: dict(NB=[1, 1, -1, -1, -1, -1, -1, -1], NA=[1, 1, 1, 1, -1, -1, -1, -1],\n            J={1: (1, 4), 4: (-1, 1), 2: (1, 5), 5: (-1, 2), 3: (1, 6), 6: (-1, 3)},\n            K={2: (1, 3), 3: (-1, 2), 4: (1, 5), 5: (-1, 4), 6: (1, 7), 7: (-1, 6)}),\n}\nfor d, M in MODELS.items():\n    n = d + 1\n    print(\'== d = %d J/K map\' % d)\n    G = as_fun(jk_gate(d, M[\'NB\'], M[\'J\'], M[\'K\']), n)\n    NA, NB = diag(M[\'NA\']), diag(M[\'NB\'])\n    check(\'J1 d=%d frame, relT(NB), relC(NA, NB) hold\' % d,\n          frame_ok(G, n) and relT_ok(G, n, NB) and relC_ok(G, n, NA, NB))\n    sa, sb = split(NA), split(NB)\n    check(\'J2 d=%d split(NA) = %s != split(NB) = %s: NA, NB not similar, no conjugator; type covariance fails\' %\n          (d, sa, sb), sa != sb and is_invol_isometry_flipping_z(NA) and is_invol_isometry_flipping_z(NB))\n    check(\'J3 d=%d no one-NOT reading: not (relT(N) and relC(N, N)) for N = NA and for N = NB\' % d,\n          not (relT_ok(G, n, NA) and relC_ok(G, n, NA, NA)) and not (relT_ok(G, n, NB) and relC_ok(G, n, NB, NB)))\n\n# ------------------------------------------------------------------ transfer countercontrol\nprint(\'== transfer countercontrol (shear)\')\ng = diag([1, 2, 1, 1])  # homogenized shear: x0 -> 2 x0, fixes x1 and z\nx0 = [Fr(1), Fr(0), Fr(0), Fr(0)]          # hom(0)\ne0 = [Fr(1), Fr(1), Fr(0), Fr(0)]          # hom(e0), e0 on the unit sphere\nw = prod_state(x0, e0)\nw2 = actT(g, w)\nunit = [Fr(1), Fr(0), Fr(0), Fr(0)]        # ehom of the unit effect\nsharp_neg_e0 = [Fr(1, 2), Fr(-1, 2), Fr(0), Fr(0)]   # ehom of (1 - x0)/2\nval = sum(unit[m] * w2[m][v] * sharp_neg_e0[v] for m in range(4) for v in range(4))\nval0 = sum(unit[m] * w[m][v] * sharp_neg_e0[v] for m in range(4) for v in range(4))\ncheck(\'S1 shear fixing z: value on prodState(0, e0) is %s >= 0, on its actT g image %s < 0\' % (val0, val),\n      val0 >= 0 and val == Fr(-1, 2) and g[3][3] == 1)\n\nfails = [nm for nm, ok in RESULTS if not ok]\nprint(\'checks: %d, failures: %d\' % (len(RESULTS), len(fails)))\nif not fails:\n    print(\'VERDICT TYPE-COVARIANCE-CONSISTENT\')\nelse:\n    print(\'VERDICT NOT RENDERED: \' + \'; \'.join(fails))\nsys.exit(0)\n'
PROBE_BLOB = 'f5cc2aaf00e884343622447ce0bed76f844af492'
RESEARCH_PROBE_SHA256 = 'c28e1b97b3ec51cb6a919d13b526278047efab53bdc23dea706ef85ccb055eda'
KERNEL_LINE_RESEARCH = "KERNEL = '../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'"
KERNEL_LINE_PRED = "KERNEL = '../lean-mathlib/OIBridge/CompositeDimension.lean'"
PROBE_IDS = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'J1 d=5', 'J2 d=5', 'J3 d=5', 'J1 d=7', 'J2 d=7', 'J3 d=7', 'S1']
SHARD = '  probes_kinfcopy1:\n    name: Numerical probes / KINF-COPY-1 type covariance\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n        with:\n          fetch-depth: 0\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n      - name: KINF-COPY-1 exact instances probe\n        working-directory: verification/lean\n        run: |\n          echo "=== kinf_copy1_probe.py ==="\n          python3 -I -B kinf_copy1_probe.py | tee "$RUNNER_TEMP/kinf_copy1.out"\n          test "$(tail -n 1 "$RUNNER_TEMP/kinf_copy1.out")" = "VERDICT TYPE-COVARIANCE-CONSISTENT"\n      - name: KINF-COPY-1 control mutation tests\n        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/controls.py --self-test\n\n'
SHARD_ANCHOR = '        run: python3 -I -B verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/controls.py --self-test\n\n'
EDITS = [['probes_oimaxcone, probes_a42_witness', 'probes_oimaxcone, probes_kinfcopy1, probes_a42_witness'], ['          OIMAXCONE_RESULT: ${{ needs.probes_oimaxcone.result }}\n', '          OIMAXCONE_RESULT: ${{ needs.probes_oimaxcone.result }}\n          KINFCOPY1_RESULT: ${{ needs.probes_kinfcopy1.result }}\n'], ['          echo "oimaxcone=${OIMAXCONE_RESULT}"\n', '          echo "oimaxcone=${OIMAXCONE_RESULT}"\n          echo "kinfcopy1=${KINFCOPY1_RESULT}"\n'], ['          test "${OIMAXCONE_RESULT}" = success\n', '          test "${OIMAXCONE_RESULT}" = success\n          test "${KINFCOPY1_RESULT}" = success\n']]
SELF_TEST_RECORDS = 59

# ===================================================================================================== core
# Shared mechanics. Every frozen text the rules compare against is embedded above; this part only reads git.

ALLOWED_AXIOMS = ('propext', 'Classical.choice', 'Quot.sound')
DECL = re.compile(r'^(?:@\[[^\]\n]*\]\s+)?(theorem|lemma|def|noncomputable def|abbrev|noncomputable abbrev|structure'
                  r'|instance)\s+(\S+)', re.M)
CTX = re.compile(r'^(variable|open|namespace|section|end|attribute|universe|set_option|noncomputable section)\b.*$',
                 re.M)
IDENT = re.compile(r'(?<![\w.\'@])[A-Za-z_][\w\'.]*')
BINDER_OPEN, BINDER_CLOSE = '({[⦃', ')}]⦄'
HEX40 = re.compile(r'^[0-9a-f]{40}$')

# --------------------------------------------------------------------------------------- the outcome registry
# Every check records its outcome as it runs. A mode passes only if every code the mode requires was recorded and
# every recorded outcome is True: a check that did not run counts as failed.
RESULTS = []


def check(code, name, cond):
    ok = cond is True
    RESULTS.append((code, ok))
    print(('  PASS  ' if ok else '  FAIL  ') + code + ' ' + name, flush=True)
    return ok


def finalize(required, results=None):
    """(ok, failed codes, codes required but never recorded)."""
    res = RESULTS if results is None else results
    seen = {c for c, _ in res}
    failed = sorted({c for c, ok in res if not ok})
    missing = sorted(set(required) - seen)
    return (not failed and not missing), failed, missing


# ------------------------------------------------------------------------------------------------------- git
GIT_ENV = [None]   # replaced by the self-test's fixture with a temporary object directory


def git_run(*args, data=None):
    return subprocess.run(['git'] + list(args), capture_output=True, input=data, env=GIT_ENV[0])


def git(*args, data=None):
    r = git_run(*args, data=data)
    if r.returncode != 0:
        raise RuntimeError('git %s: %s' % (' '.join(args), r.stderr.decode('utf-8', 'replace').strip()))
    return r.stdout.decode('utf-8')


def show(commit, path):
    r = git_run('show', '%s:%s' % (commit, path))
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob_of(commit, path):
    r = git_run('rev-parse', '--verify', '-q', '%s:%s' % (commit, path))
    return r.stdout.decode('utf-8').strip() if r.returncode == 0 else None


def rev(commit):
    r = git_run('rev-parse', '--verify', '-q', commit + '^{commit}')
    return r.stdout.decode('utf-8').strip() if r.returncode == 0 else None


def parents(commit):
    return git('rev-list', '--parents', '-n', '1', commit).split()[1:]


def name_status(a, b):
    out = git('diff', '--no-renames', '--name-status', a, b)
    rows = []
    for line in out.splitlines():
        if line:
            s, p = line.split('\t', 1)
            rows.append((s, p))
    return rows


def is_ancestor(a, b):
    return git_run('merge-base', '--is-ancestor', a, b).returncode == 0


def git_blob_id(text):
    """The git blob id of a text, computed without git."""
    data = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def own_text():
    with open(os.path.abspath(__file__), 'rb') as f:
        return f.read().decode('utf-8')


# ------------------------------------------------------------------------------------------------ Lean surface
def norm(s):
    return ' '.join(s.split())


def header(text):
    i = text.find('\nimport ')
    return text[:i] if i != -1 else text


def preamble(text):
    """From the first import to the first section marker."""
    i = text.find('\nimport ')
    j = text.find('\n/-! ### ')
    return text[i + 1:j] if i != -1 and j != -1 else None


def context_lines(text):
    lines = text.split('\n')
    out = []
    for k, line in enumerate(lines):
        if CTX.match(line):
            block = [line]
            j = k + 1
            while j < len(lines) and lines[j].startswith('  ') and (line.startswith('variable') or
                                                                    line.startswith('open ')):
                block.append(lines[j])
                j += 1
            out.append('\n'.join(block))
    return out


def decls(text):
    return [[m.group(1), m.group(2)] for m in DECL.finditer(text)]


def stmt_end(chunk):
    ends = [j for j in (chunk.find(' :='),) if j != -1]
    m = re.search(r' where\n', chunk)
    if m:
        ends.append(m.start())
    return min(ends) if ends else -1


def spans(text):
    out = []
    ms = list(DECL.finditer(text))
    for k, m in enumerate(ms):
        start = m.start()
        nxt = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        chunk = text[start:nxt]
        for stop in ('\n/--', '\n/-!', '\n#print', '\nend ', '\nend\n', '\nvariable', '\nopen ', '\nattribute'):
            j = chunk.find(stop)
            if j != -1:
                chunk = chunk[:j]
        chunk = chunk.rstrip()
        se = -1
        if m.group(1) in ('theorem', 'lemma'):
            j = stmt_end(chunk)
            if j != -1:
                se = start + j
        out.append((m.group(1), m.group(2), start, se if se != -1 else start + len(chunk), start + len(chunk)))
    return out


def decl_chunks(text):
    """name -> (kind, statement (theorems) or whole text (definitions), proof text (theorems))."""
    out = {}
    for kind, name, start, se, cend in spans(text):
        if kind in ('theorem', 'lemma'):
            out[name] = (kind, text[start:se], text[se:cend])
        else:
            out[name] = (kind, text[start:cend], '')
    return out


def colon_index(stmt):
    m = DECL.match(stmt)
    i = m.end() if m else 0
    depth = 0
    for j in range(i, len(stmt)):
        c = stmt[j]
        if c in BINDER_OPEN:
            depth += 1
        elif c in BINDER_CLOSE:
            depth -= 1
        elif c == ':' and depth == 0 and stmt[j:j + 2] != ':=':
            return j
    return -1


def split_statement(stmt):
    m = DECL.match(stmt)
    i = m.end() if m else 0
    j = colon_index(stmt)
    if j == -1:
        return stmt[i:], ''
    return stmt[i:j], stmt[j + 1:]


def code_only(text):
    text = re.sub(r'/-.*?-/', ' ', text, flags=re.S)
    return re.sub(r'--[^\n]*', ' ', text)


def token(name, text):
    return re.search(r'(?<![\w.\'])%s(?![\w\'])' % re.escape(name), text) is not None


def groups(b):
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
    inner = g[1:-1]
    j = inner.find(' : ')
    if j == -1:
        return []
    return inner[:j].split()


def scopes_at(text):
    """name -> (variable groups in scope, namespaces in scope, opened namespaces in scope) at each declaration."""
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
            out[decl_at[pos]] = ([g for s in stack for g in s[0]], [n for s in stack for n in s[1]],
                                 [o for s in stack for o in s[2]])
        for ln in block:
            pos += len(ln) + 1
        k = j
    return out


def effective(text, name):
    """The section variables a declaration's statement uses, in declared order, then its binders and conclusion."""
    chunks = decl_chunks(text)
    if name not in chunks:
        return None
    stmt = chunks[name][1]
    if chunks[name][0] not in ('theorem', 'lemma'):
        j = stmt_end(stmt)
        stmt = stmt[:j] if j != -1 else stmt
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


def inventory_one(text):
    if text in _INV_CACHE:
        return _INV_CACHE[text]
    names, spaces = set(), set()
    sc = scopes_at(text)
    for kind, name in decls(text):
        nss = sc.get(name, ([], [], []))[1]
        prefix = '.'.join(nss)
        names.add((prefix + '.' if prefix else '') + name)
        for i in range(1, len(nss) + 1):
            spaces.add('.'.join(nss[:i]))
    _INV_CACHE[text] = (names, spaces)
    return names, spaces


def inventory(files):
    names, spaces = set(), set()
    for t in files:
        n, s = inventory_one(t)
        names |= n
        spaces |= s
    return names, spaces


def visible(nss, ops, spaces):
    out = [''] + ['.'.join(nss[:i]) for i in range(1, len(nss) + 1)]
    for o in ops:
        hit = [p + '.' + o for p in ['.'.join(nss[:i]) for i in range(len(nss), 0, -1)] if p + '.' + o in spaces]
        out.append(hit[0] if hit else o)
    return out


def resolve(tok, vis, names):
    return sorted({(v + '.' if v else '') + tok for v in vis} & names)


def top_colon(s):
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
    k = top_colon(eff)
    bound = set()
    for g in groups(eff[:k]):
        bound.update(group_names(g))
    for m in re.finditer(r'(?:∃|∀|fun|λ)\s+([^,:=]+?)\s*(?::|,|=>)', eff[k:]):
        bound.update(x for x in m.group(1).split() if re.match(r"^[A-Za-zΩ_][\w']*$", x))
    return [t for t in IDENT.findall(eff) if t not in bound]


def resolution_map(mod, names_of_interest, inv_files, proof_tokens=()):
    """{(declaration, identifier): [fully qualified OIBridge names it resolves to]} for every identifier of every
    named declaration's effective statement (and, for the (declaration, identifier) pairs of proof_tokens, of its
    proof), resolved in the module's namespace context against the inventory of inv_files and the module."""
    names, spaces = inventory(inv_files + [mod])
    sc = scopes_at(mod)
    chunks = decl_chunks(mod)
    out = {}
    for dn in names_of_interest:
        eff = effective(mod, dn)
        if eff is None:
            out[(dn, '<absent>')] = []
            continue
        s = sc.get(dn, ([], [], []))
        vis = visible(s[1], s[2], spaces)
        toks = set(strip_binders(eff))
        kind, whole, _ = chunks[dn]
        if kind not in ('theorem', 'lemma'):
            j = stmt_end(whole)
            body = whole[j:] if j != -1 else ''
            fields = set(re.findall(r'^  ([A-Za-zΩ_][\w\']*) :', body, re.M))
            toks |= {t for t in IDENT.findall(code_only(body)) if t not in fields}
        for t in sorted(toks):
            hits = resolve(t, vis, names)
            if hits:
                out[(dn, t)] = hits
    for dn, t in proof_tokens:
        s = sc.get(dn, ([], [], []))
        vis = visible(s[1], s[2], spaces)
        proof = chunks.get(dn, ('', '', ''))[2]
        out[(dn, t + '#proof')] = resolve(t, vis, names) if token(t, code_only(proof)) else []
    return out


def print_lines(mod):
    return re.findall(r'^#print axioms (\S+)', mod, re.M)


# ------------------------------------------------------------------------------------- governed paths and F
def fenced_block(text, tag):
    """The lines of the one fenced block opened by exactly ```tag, or None unless there is exactly one."""
    if text is None:
        return None
    ms = list(re.finditer(r'^```%s\n(.*?)^```\n' % re.escape(tag), text, re.M | re.S))
    if len(ms) != 1:
        return None
    return [l for l in ms[0].group(1).split('\n') if l]


def governed_rows(lines):
    rows = []
    for l in lines or []:
        p = l.split(' ')
        if len(p) != 3 or p[0] not in ('record', 'execution') or not set(p[1]) <= set('AMD'):
            return None
        rows.append((p[0], p[1], p[2]))
    return rows


def row_covers(row, status, path):
    cls, letters, p = row
    if status not in letters:
        return False
    return path.startswith(p) if p.endswith('/') else path == p


def delta_bad(rows, ns):
    """The (status, path) entries of a name-status list no governed row covers."""
    return [(s, p) for s, p in ns if not any(row_covers(r, s, p) for r in rows)]


def control_plane(path):
    return path == PREREG or path.startswith(RDIR + 'amendments/')


def freeze_checks(F):
    """F mode: the frozen control plane. F is a descendant of D along single-parent commits that change only
    control-plane files; delta(D, F) is the preregistration (and amendments); the round and governed-path blocks are
    the frozen ones; the preregistration states the frozen texts these controls compare against and pins this
    controls.py's blob."""
    Fc = rev(F)
    check('F', 'F resolves to a commit', Fc is not None)
    if Fc is None:
        return
    chain = git('rev-list', '--reverse', '%s..%s' % (D, Fc)).split() if is_ancestor(D, Fc) else []
    check('F', 'D is an ancestor of F', is_ancestor(D, Fc))
    bad = []
    for c in chain:
        ps = parents(c)
        ch = [p for _, p in name_status(ps[0], c)] if len(ps) == 1 else ['<merge>']
        if len(ps) != 1 or not all(control_plane(p) for p in ch):
            bad.append(c[:12])
    check('F', 'every commit of D..F has one parent and changes only control-plane files%s'
          % ((' (bad: %s)' % bad[:3]) if bad else ''), bool(chain) and not bad)
    ns = name_status(D, Fc)
    check('F', 'delta(D, F) is the preregistration and amendments only, the preregistration among them',
          all(control_plane(p) for _, p in ns) and ('A', PREREG) in ns)
    pre = show(Fc, PREREG) or ''
    check('F', 'the v3-round block at F is the frozen one', fenced_block(pre, 'v3-round') == ROUND_BLOCK)
    check('F', 'the v3-governed-paths block at F is the frozen one', fenced_block(pre, 'v3-governed-paths') ==
          GOVERNED_BLOCK and governed_rows(GOVERNED_BLOCK) is not None)
    missing = [k for k, t in PREREG_TEXTS.items() if norm(t) not in norm(unquote(pre))]
    check('F', 'the preregistration at F states every frozen text these controls compare against%s'
          % ((' (missing: %s)' % missing[:3]) if missing else ''), not missing)
    own = git_blob_id(own_text())
    check('K', 'the preregistration at F pins this controls.py blob %s' % own, own in pre)


def unquote(note):
    return '\n'.join(re.sub(r'^\s*>\s?', '', line) for line in note.split('\n'))


def stage_of(ns):
    """C1, S1 or E from delta(D, commit); None for any other shape (refused)."""
    rec = {p for s, p in ns if p.startswith(RDIR) and not control_plane(p)}
    exe = {p for s, p in ns if not p.startswith(RDIR)}
    if exe == set() and rec == {CONTROLS}:
        return 'C1'
    if exe == set(EXEC_PATHS) and rec == {CONTROLS}:
        return 'S1'
    if exe == set(EXEC_PATHS) and rec == {CONTROLS, RESULT}:
        return 'E'
    return None


def path_checks(commit, F):
    """G, R, L and K at a stage commit after F."""
    ns = name_status(D, commit)
    rows = governed_rows(fenced_block(show(commit, PREREG), 'v3-governed-paths'))
    check('G', 'the governed-path block at the commit is the frozen one', rows is not None and
          fenced_block(show(commit, PREREG), 'v3-governed-paths') == GOVERNED_BLOCK)
    bad = delta_bad(governed_rows(GOVERNED_BLOCK), ns)
    check('G', 'every path of delta(D, commit) is covered by a governed row with its status%s'
          % ((' (uncovered: %s)' % bad[:3]) if bad else ''), not bad)
    exe = {p: s for s, p in ns if not p.startswith(RDIR)}
    stage = stage_of(ns)
    check('G', 'the commit is a recognized stage (C1, S1 or E): %s' % stage, stage is not None)
    if stage in ('S1', 'E'):
        check('G', 'delta(D, commit) carries exactly the governed execution paths with their frozen statuses',
              exe == EXEC_PATHS)
    check('G', 'the receipt is absent before the receipt commit', blob_of(commit, RECEIPT) is None)
    files = set(git('ls-tree', '-r', '--name-only', commit, '--', RDIR).split())
    want = {PREREG, CONTROLS} | ({RESULT} if stage == 'E' else set())
    allowed_am = {p for p in files if p.startswith(RDIR + 'amendments/')}
    check('R', 'the record directory holds exactly %s (and amendments)' % sorted(os.path.basename(p) for p in want),
          files - allowed_am == want)
    check('K', 'controls.py at the commit is this file', show(commit, CONTROLS) == own_text())
    # linear execution from F
    Fc = rev(F)
    okF = Fc is not None and is_ancestor(Fc, commit)
    check('L', 'F is an ancestor of the commit', okF)
    chain = git('rev-list', '--reverse', '%s..%s' % (Fc, commit)).split() if okF else []
    shape = []
    for k, c in enumerate(chain):
        ps = parents(c)
        if len(ps) != 1 or (k == 0 and ps[0] != Fc) or (k > 0 and ps[0] != chain[k - 1]):
            shape.append('nonlinear ' + c[:12])
            continue
        ch = name_status(ps[0], c)
        if k == 0:
            if ch != [('A', CONTROLS)]:
                shape.append('C1 is not the controls.py addition alone')
        elif any(p.startswith(RDIR) for _, p in ch) and not (ch == [('A', RESULT)] and k == len(chain) - 1):
            shape.append('record change outside C1 and the final note ' + c[:12])
        elif any(p.startswith(RDIR) for _, p in ch) is False and not all(p in EXEC_PATHS for _, p in ch):
            shape.append('a stage commit leaves the execution paths ' + c[:12])
    check('L', 'F..commit is linear: C1 adds controls.py alone, stage commits change execution paths only, the note '
               'comes last%s' % ((' (%s)' % shape[:2]) if shape else ''), bool(chain) and not shape)
    check('F', 'the preregistration is unchanged from F', okF and blob_of(commit, PREREG) == blob_of(Fc, PREREG))
    amend_ok = okF and [p for p in files if p.startswith(RDIR + 'amendments/')] == \
        [p for p in git('ls-tree', '-r', '--name-only', Fc, '--', RDIR + 'amendments/').split()]
    check('F', 'the amendments are unchanged from F', amend_ok)
    return stage


def imports_ok(d_text, e_text):
    return d_text is not None and e_text is not None and d_text.count(ANCHOR_IMPORT) == 1 and \
        e_text == d_text.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)


def census_want(d_text):
    d = json.loads(d_text)
    want = dict(d)
    want['families'] = list(d['families']) + [CENSUS_FAMILY]
    return json.dumps(want, indent=2, ensure_ascii=False) + '\n'


def census_ok(d_text, e_text):
    try:
        return d_text is not None and json.dumps(json.loads(d_text), indent=2, ensure_ascii=False) + '\n' == d_text \
            and e_text == census_want(d_text)
    except Exception:
        return False


# ------------------------------------------------------------------------------------------ axiom expected results
def axioms_from_log(text, commit, run=None, job=None):
    """An expected result (AGENTS §A.42 item 1) from a Lean build log: the module's `#print axioms` reports."""
    out = {}
    for m in re.finditer(r"'(%s[^']+)' depends on axioms: \[([^\]]*)\]" % re.escape(PREFIX), text):
        out[m.group(1)] = [a.strip() for a in m.group(2).split(',') if a.strip()]
    for m in re.finditer(r"'(%s[^']+)' does not depend on any axioms" % re.escape(PREFIX), text):
        out[m.group(1)] = []
    return {'commit': commit, 'recipe': 'workflow_dispatch of .github/workflows/verify.yml at commit; Mathlib bridge '
            'job; the module\'s #print axioms reports', 'run': run, 'job': job,
            'source_digest': 'sha256:' + hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'build': 'success' if re.search(r'Build completed successfully', text) else 'not-observed',
            'axioms': out}


def axioms_status(ax, commit, exact=True):
    """(within, reason): every frozen print reported within the three axioms, by a well-formed expected result for
    this commit (exact) or for a commit whose module blob is this commit's (not exact)."""
    if ax is None:
        return False, 'no axiom expected result supplied'
    if not isinstance(ax, dict) or not HEX40.match(str(ax.get('commit', ''))) or ax.get('build') != 'success' or \
            not isinstance(ax.get('axioms'), dict) or not ax.get('recipe') or 'source_digest' not in ax:
        return False, 'the axiom expected result is malformed or reports no successful build'
    c = rev(commit)
    if exact and ax['commit'] != c:
        return False, 'the axiom expected result is for %s, not the commit under check' % ax['commit'][:12]
    if not exact and (rev(ax['commit']) is None or blob_of(ax['commit'], MOD) != blob_of(commit, MOD)):
        return False, 'the axiom expected result is for a commit with another module blob'
    rep = ax['axioms']
    if sorted(rep) != sorted(PRINTS):
        return False, 'the reports are not exactly the frozen prints'
    bad = [n for n in PRINTS if not isinstance(rep[n], list) or not set(rep[n]) <= set(ALLOWED_AXIOMS)]
    return (not bad), ('outside the three axioms: %s' % bad[:3]) if bad else 'within the three axioms'


def load_axioms(path):
    if path is None:
        return None
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {'malformed': True}


# --------------------------------------------------------------------------------------------- fixture (self-test)
class Fixture:
    """Real commits D -> F -> C1 -> S1 -> E built in a temporary object directory that borrows the repository's
    objects as an alternate; nothing is written to the repository."""

    def __init__(self):
        self.td = tempfile.mkdtemp(prefix='controls-fixture-')
        objs = os.path.abspath(git('rev-parse', '--git-path', 'objects').strip())
        os.makedirs(os.path.join(self.td, 'objects', 'info'))
        env = dict(os.environ)
        env.update({'GIT_OBJECT_DIRECTORY': os.path.join(self.td, 'objects'),
                    'GIT_ALTERNATE_OBJECT_DIRECTORIES': objs, 'GIT_INDEX_FILE': os.path.join(self.td, 'index'),
                    'GIT_AUTHOR_NAME': 'fixture', 'GIT_AUTHOR_EMAIL': 'fixture',
                    'GIT_COMMITTER_NAME': 'fixture', 'GIT_COMMITTER_EMAIL': 'fixture',
                    'GIT_AUTHOR_DATE': '2026-01-01T00:00:00Z', 'GIT_COMMITTER_DATE': '2026-01-01T00:00:00Z'})
        self.env = env
        self.saved = GIT_ENV[0]
        GIT_ENV[0] = env

    def close(self):
        GIT_ENV[0] = self.saved
        shutil.rmtree(self.td, ignore_errors=True)

    def commit(self, parent_list, base_tree_commit, changes, msg='fixture'):
        """changes: {path: text or None (delete)} applied to base_tree_commit's tree."""
        git('read-tree', base_tree_commit + '^{tree}')
        for p, t in sorted(changes.items()):
            if t is None:
                git('update-index', '--force-remove', p)
            else:
                b = git('hash-object', '-w', '--stdin', data=t.encode('utf-8')).strip()
                git('update-index', '--add', '--cacheinfo', '100644,%s,%s' % (b, p))
        tree = git('write-tree').strip()
        args = ['commit-tree', tree, '-m', msg]
        for p in parent_list:
            args += ['-p', p]
        return git(*args).strip()


def quiet(fn, *a, **k):
    """Run a mode with its output captured; return (ok, failed codes, missing codes) from its own records."""
    start = len(RESULTS)
    saved = sys.stdout
    sys.stdout = io.StringIO()
    try:
        req = fn(*a, **k)
    except Exception as e:
        sys.stdout = saved
        del RESULTS[start:]
        return False, ['EXC:%s' % type(e).__name__], []
    finally:
        sys.stdout = saved
    mine = RESULTS[start:]
    del RESULTS[start:]
    return finalize(req or [], mine)


def expect(label, cond):
    """A self-test assertion, recorded under code T."""
    return check('T', label, cond)

# =========================================================================================== round KINF-COPY-1
RED_TOKENS = ('KINF-COPY-REDUCTION-PROVED', 'KINF-COPY-REDUCTION-NOT-ESTABLISHED')
POS_TOKENS = ('KINF-COPY-SWAPPED-WITNESS', 'KINF-COPY-SWAPPED-NOT-ESTABLISHED')
EXACT_TOKENS = ('KINF-COPY-INSTANCES-CONSISTENT', 'KINF-COPY-INSTANCES-NOT-ESTABLISHED')
ALL_TOKENS = RED_TOKENS + POS_TOKENS + EXACT_TOKENS
PHRASES = ('OI supplies', 'derived from OI', 'copy naturality is not needed', 'K∞-Copy is discharged',
           'replaces copy naturality', 'admits gates that copy naturality excludes', 'kernel proof of',
           'design module', 'not for merge')
THEOREMS = [n for k, n in DECLS if k in ('theorem', 'lemma')]
REQUIRED_BASE = ['G', 'R', 'K', 'L', 'F']
REQUIRED_MODULE = ['N1', 'N2', 'N3', 'S1', 'S2', 'S3', 'S4', 'I', 'C', 'P', 'W']


def phrase_hits(text):
    t = norm(unquote(text)).lower()
    for frozen in (EARNED, NONINF):
        t = t.replace(norm(frozen).lower(), ' ')
    return [p for p in PHRASES if norm(p).lower() in t]


def note_tokens(note):
    return sorted(t for t in ALL_TOKENS if re.search(r'(?<![\w-])%s(?![\w-])' % re.escape(t), note))


_INV = []


def d_inventory_files():
    if not _INV:
        out = git('ls-tree', '--name-only', D, LEAN)
        _INV.extend(show(D, p) for p in out.split() if p.endswith('.lean'))
    return list(_INV)


def surface_bad(mod, names):
    """The frozen names whose text or effective statement differs."""
    ch = decl_chunks(mod)
    return sorted(n for n in names if ch.get(n, ('', None))[1] != TEXTS[n] or
                  (n in EFFECTIVE and effective(mod, n) != EFFECTIVE[n]))


def resolution_bad(mod, names, inv_files):
    pt = [k for k in PROOF_PINNED_KEYS if k[0] in names]
    rm = resolution_map(mod, names, inv_files, proof_tokens=pt)
    bad = sorted('%s:%s' % k for k, v in rm.items() if len(v) != 1)
    for (dn, t), v in rm.items():
        if t in PINNED and v != [PINNED[t]]:
            bad.append('%s:%s->%s' % (dn, t, v))
        if t.endswith('#proof') and v != [PROOF_PINNED['%s|%s' % (dn, t[:-6])]]:
            bad.append('%s:%s->%s' % (dn, t, v))
    want = {k: v for k, v in RESOLVED.items() if k.split('|')[0] in names}
    if {'%s|%s' % k: v for k, v in rm.items()} != want:
        bad.append('resolution differs from the frozen map at D')
    return bad


def frame_ok(mod):
    imports = re.findall(r'^import .*$', mod, re.M)
    return decls(mod) == DECLS and preamble(mod) == PREAMBLE and context_lines(mod) == CONTEXT and \
        imports == [IMPORT_ONLY]


def ax_reports(ax, commit, exact=True):
    """{print: within the three axioms} from a well-formed expected result, or None."""
    within, why = axioms_status(ax, commit, exact)
    if ax is None or not isinstance(ax, dict) or not isinstance(ax.get('axioms'), dict) or \
            why.startswith(('no axiom', 'the axiom expected result', 'the reports')):
        return None
    return {n: isinstance(ax['axioms'].get(n), list) and set(ax['axioms'][n]) <= set(ALLOWED_AXIOMS) for n in PRINTS}


def red_cell(mod, rep, inv_files):
    """REDUCTION-PROVED iff the §B-§D declarations have exactly their frozen texts and effective statements, in the
    frozen module frame (S1), resolve to the landed objects (S2), and every frozen print is within the three axioms
    (measured). Reads no §E statement and no probe output."""
    ok = mod is not None and frame_ok(mod) and print_lines(mod) == PRINTS and not surface_bad(mod, RED_NAMES) and \
        not resolution_bad(mod, RED_NAMES, inv_files) and rep is not None and all(rep[n] for n in PRINTS)
    return RED_TOKENS[0] if ok else RED_TOKENS[1]


def pos_cell(mod, rep, inv_files):
    """SWAPPED-WITNESS iff swapped_nativeGate2 and swapped_not_ne, and the module definitions their statements name
    (NativeGate2, actTEq, swap01), have their frozen texts and resolve to the frozen objects, and their two prints are
    within the three axioms (measured). Reads no §B-§D theorem statement and no probe output."""
    names = list(POS_NAMES) + list(POS_DEPS)
    ok = mod is not None and frame_ok(mod) and not surface_bad(mod, names) and \
        not resolution_bad(mod, list(POS_NAMES), inv_files) and rep is not None and \
        all(rep[PREFIX + n] for n in POS_NAMES)
    return POS_TOKENS[0] if ok else POS_TOKENS[1]


def run_probe_text(probe_text, kernel_text):
    with tempfile.TemporaryDirectory() as td:
        for path, text in ((PROBE, probe_text), (LEAN + 'CompositeDimension.lean', kernel_text)):
            dest = os.path.join(td, path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(text)
        try:
            r = subprocess.run([sys.executable, '-I', '-B', os.path.basename(PROBE)],
                               cwd=os.path.join(td, os.path.dirname(PROBE)), capture_output=True, timeout=900)
        except subprocess.TimeoutExpired:
            return -1, ''
        return r.returncode, r.stdout.decode('utf-8', 'replace')


def parse_probe(stdout):
    passes, fails = set(), set()
    for line in stdout.split('\n'):
        m = re.match(r'^(PASS|FAIL) (J\d d=\d+|C\d|S1)(?= )', line)
        if m:
            (passes if m.group(1) == 'PASS' else fails).add(m.group(2))
    lines = [l for l in stdout.split('\n') if l.strip()]
    return passes, fails, lines


def exact_cell(rc, stdout):
    """INSTANCES-CONSISTENT iff the probe, run by these controls with python3 -I, prints a PASS line for each of the
    thirteen frozen checks, no FAIL line, `checks: 13, failures: 0`, and the verdict line last. Reads no module."""
    passes, fails, lines = parse_probe(stdout)
    ok = rc == 0 and passes == set(PROBE_IDS) and not fails and 'checks: 13, failures: 0' in lines and \
        bool(lines) and lines[-1] == 'VERDICT TYPE-COVARIANCE-CONSISTENT'
    return EXACT_TOKENS[0] if ok else EXACT_TOKENS[1]


def apply_edit(workflow):
    if workflow is None or workflow.count(SHARD_ANCHOR) != 1:
        return None
    out = workflow.replace(SHARD_ANCHOR, SHARD_ANCHOR + SHARD, 1)
    for old, new in EDITS:
        if out.count(old) != 1:
            return None
        out = out.replace(old, new, 1)
    return out


def module_checks(mod, tag='', inv_files=None):
    if inv_files is None:
        inv_files = d_inventory_files()
    if mod is None:
        check('N1', 'module present' + tag, False)
        return
    check('N1', 'the module declares exactly the frozen declarations, in order, by kind' + tag, decls(mod) == DECLS)
    check('N2', 'the preamble is the frozen one' + tag, preamble(mod) == PREAMBLE)
    check('N2', 'every context line is the frozen one, in order' + tag, context_lines(mod) == CONTEXT)
    bad = surface_bad(mod, list(TEXTS))
    check('N2', 'every theorem signature and every definition whole unchanged%s' % ((' (changed: %s)' % bad[:4])
                                                                                     if bad else '') + tag, not bad)
    check('N3', 'no sorry, admit, axiom declaration or native_decide' + tag,
          not re.search(r'\bsorry\b|\badmit\b|^\s*axiom\b|native_decide', code_only(mod), re.M))
    check('S1', 'the surface (frame, statements, the %d prints in order, the single import) is the frozen one'
          % len(PRINTS) + tag, frame_ok(mod) and not bad and print_lines(mod) == PRINTS)
    heads = [n for n in Q_RED_HEADLINES if '(hG : NativeGate2 ' not in TEXTS[n] or
             '(hG : NativeGate2 ' not in (decl_chunks(mod).get(n, ('', ''))[1] or '')]
    check('S1', 'two-NOT scope: every Q-RED headline takes NativeGate2 data%s' % ((' %s' % heads) if heads else '')
          + tag, not heads)
    bad2 = resolution_bad(mod, [n for _, n in DECLS], inv_files)
    check('S2', 'every identifier resolves uniquely, to the landed declaration it resolves to at D%s'
          % ((' %s' % bad2[:3]) if bad2 else '') + tag, not bad2)
    ph = phrase_hits(header(mod))
    check('S4', 'the module header carries none of the frozen phrases%s' % ((' %s' % ph) if ph else '') + tag, not ph)


def note_checks(note, toks3):
    ph = phrase_hits(note)
    check('S4', 'the result note carries none of the frozen phrases%s' % ((' %s' % ph) if ph else ''), not ph)
    found = note_tokens(note)
    check('V', 'the note states exactly the computed tokens %s (found %s)' % (toks3, found), found == sorted(toks3))
    n = norm(unquote(note))
    allpos = toks3 == [RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[0]]
    check('V', 'the earned reading is stated, in its frozen two-NOT words, exactly when all three cells are positive',
          (norm(EARNED) in n) == allpos)
    check('V', 'the non-inference rule, with the one-NOT limitation, is stated in its frozen words under every '
               'outcome', norm(NONINF) in n)


def cells_at(c, ax, exact):
    mod = show(c, MOD)
    inv = d_inventory_files()
    rep = ax_reports(ax, c, exact)
    probe, kernel = show(c, PROBE), show(c, LEAN + 'CompositeDimension.lean')
    rc, out = run_probe_text(probe, kernel) if probe is not None and kernel is not None else (-1, '')
    return [red_cell(mod, rep, inv), pos_cell(mod, rep, inv), exact_cell(rc, out)], (rc, out)


def run_freeze(F):
    freeze_checks(F)
    return ['F', 'K']


def run_check(commit, F, axioms_path=None, axioms=None):
    c = rev(commit)
    check('G', 'the commit resolves', c is not None)
    if c is None:
        return REQUIRED_BASE + REQUIRED_MODULE
    freeze_checks(F)
    stage = path_checks(c, F)
    if stage in ('S1', 'E'):
        module_checks(show(c, MOD))
        check('I', 'OIBridge.lean is D\'s with exactly the frozen import line', imports_ok(show(D, IMPORTS),
                                                                                        show(c, IMPORTS)))
        check('C', 'the census is D\'s with exactly the frozen family at the end, in D\'s two-space layout',
              census_ok(show(D, CENSUS), show(c, CENSUS)))
        probe = show(c, PROBE)
        check('P', 'the probe is the frozen blob %s' % PROBE_BLOB[:12], probe is not None and
              git_blob_id(probe) == PROBE_BLOB)
        want = apply_edit(show(D, WORKFLOW))
        check('W', 'the workflow is D\'s with exactly the frozen shard and four-place aggregate edit',
              want is not None and show(c, WORKFLOW) == want)
        rc, out = run_probe_text(probe or '', show(c, LEAN + 'CompositeDimension.lean') or '')
        passes, fails, _ = parse_probe(out)
        check('S3', 'hypotheses load-bearing on the exact layer: the shear breaks the positivity transfer (S1) and no '
                    'conjugator exists for the J/K data (J2 at d = 5, 7)',
              {'S1', 'J2 d=5', 'J2 d=7'} <= passes and not ({'S1', 'J2 d=5', 'J2 d=7'} & fails))
    if stage == 'E':
        ax = axioms if axioms is not None else load_axioms(axioms_path)
        rep = ax_reports(ax, c, exact=False)
        check('V', 'the axiom expected result is well formed and covers this module blob', rep is not None)
        toks, _ = cells_at(c, ax, exact=False)
        note_checks(show(c, RESULT), toks)
    return REQUIRED_BASE + ([] if stage == 'C1' else REQUIRED_MODULE) + (['V'] if stage == 'E' else [])


def run_verdict(commit, axioms_path=None, axioms=None):
    c = rev(commit)
    ax = axioms if axioms is not None else load_axioms(axioms_path)
    if c is None:
        check('V', 'the commit resolves', False)
        return ['V']
    toks, (rc, out) = cells_at(c, ax, exact=True)
    print('VERDICT  Q-RED    %s' % toks[0])
    print('VERDICT  Q-POS    %s' % toks[1])
    print('VERDICT  Q-EXACT  %s' % toks[2])
    summ = [l for l in out.split('\n') if l.startswith(('checks:', 'VERDICT'))]
    print('  probe: exit %s; %s' % (rc, ' | '.join(summ) or 'no summary'))
    check('V', 'one token per cell, each generated from the measurements', toks[0] in RED_TOKENS and
          toks[1] in POS_TOKENS and toks[2] in EXACT_TOKENS)
    return ['V']


# ------------------------------------------------------------------------------------------------------ self-test
def must_fail(code, label, mod2):
    ok, failed, missing = quiet(lambda: (module_checks(mod2), [])[1])
    check('M', 'mutation %s fails with %s' % (label, code), code in failed)


def replace_once(text, a, b):
    assert text.count(a) == 1, a
    return text.replace(a, b, 1)


def std_axioms(commit):
    return {'commit': commit, 'recipe': 'fixture', 'run': None, 'job': None, 'source_digest': 'sha256:0',
            'build': 'success', 'axioms': {n: list(ALLOWED_AXIOMS) for n in PRINTS}}


def fixture_note(toks):
    body = '# KINF-COPY-1: RESULT (fixture)\n\n' + ''.join('- %s\n' % t for t in toks) + '\n'
    if toks == [RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[0]]:
        body += '> ' + EARNED + '\n\n'
    return body + '> ' + NONINF + '\n'


NOC = '    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)\n    (hcov : ∀ x, NT (g x) = g (NC x)) :\n'
CONJ = ('    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :\n'
        '    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g)')
RELC = '  relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)\n'
DIMC = '    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=\n  dim_of_nativeGate hN'
NOC_HG = ('theorem nativeGate_of_conj {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}\n'
          '    {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}\n'
          '    (hG : NativeGate2 Ω z NC NT G)')
NE = 'theorem swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip := by'
SNG = 'theorem swapped_nativeGate :\n    NativeGate (eball 3) z3 nflip\n'
LASTP = '#print axioms OIBridge.CopyCovariance.swapped_nativeGate\n'
C6 = ("check('C6 G2 has a one-NOT reading with the target NOT: relT(NT) and relC(NT, NT) hold (run-1 fact)',\n"
      "      relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NT3, NT3))")
NA5 = "NA=[1, 1, -1, 1, -1, -1]"
EXCL = ('theorem swapped_not_nativeGate_target :\n'
        '    ¬ NativeGate (eball 3) z3 (swap01 ∘ₗ nflip ∘ₗ swap01)\n'
        '      (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ\n'
        '        actTEq swap01 swap01 swap01_swap01 swap01_swap01) := by\n  sorry\n')


def self_test():
    mod = PRED_HEADER + BODY
    expect('the embedded predicted module has the frozen blob id %s' % PRED_BLOB[:12], git_blob_id(mod) == PRED_BLOB)
    expect('the embedded design header with the same body is design blob %s (built in run 3)' % DESIGN_BLOB[:12],
           git_blob_id(DESIGN_HEADER + BODY) == DESIGN_BLOB)
    expect('the predicted probe has the frozen blob id %s' % PROBE_BLOB[:12], git_blob_id(PROBE_TEXT) == PROBE_BLOB)
    research = PROBE_TEXT.replace(KERNEL_LINE_PRED, KERNEL_LINE_RESEARCH, 1)
    expect('the predicted probe is the measured e2_copy_conj.py (sha256 %s...) with its kernel line alone changed'
           % RESEARCH_PROBE_SHA256[:12], hashlib.sha256(research.encode('utf-8')).hexdigest() == RESEARCH_PROBE_SHA256
           and PROBE_TEXT.count(KERNEL_LINE_PRED) == 1 and len(PROBE_TEXT.split('\n')) == len(research.split('\n')))
    inv = d_inventory_files()
    expect('D\'s inventory is readable (%d modules)' % len(inv), len(inv) > 100)
    ok, failed, missing = quiet(lambda: (module_checks(mod), [])[1])
    expect('the predicted module passes every module check (failed: %s)' % failed, ok)
    ok, failed, missing = quiet(lambda: (module_checks(DESIGN_HEADER + BODY), [])[1])
    expect('countercontrol: the design blob itself fails S4 only (its header says "design module"): %s' % failed,
           failed == ['S4'])
    kernel = show(D, LEAN + 'CompositeDimension.lean')
    rc, out = run_probe_text(PROBE_TEXT, kernel)
    expect('the predicted probe, run on D\'s kernel, reads INSTANCES-CONSISTENT (%s)' % exact_cell(rc, out),
           exact_cell(rc, out) == EXACT_TOKENS[0])
    rcr, outr = run_probe_text(research, kernel)
    expect('countercontrol: the research probe\'s own kernel path does not resolve from verification/lean, so it '
           'reads NOT-ESTABLISHED there (exit %d)' % rcr, exact_cell(rcr, outr) == EXACT_TOKENS[1] and rcr != 0)
    std = {n: True for n in PRINTS}
    expect('the predicted module with standard prints reads REDUCTION-PROVED and SWAPPED-WITNESS',
           red_cell(mod, std, inv) == RED_TOKENS[0] and pos_cell(mod, std, inv) == POS_TOKENS[0])
    # S1 -- the prereg's mutations
    must_fail('S1', 'hgz dropped from nativeGate_of_conj', replace_once(mod, NOC, NOC.replace(' (hgz : g z = z)', '')))
    must_fail('S1', 'hcov reversed', replace_once(mod, NOC, NOC.replace('NT (g x) = g (NC x)', 'NC (g x) = g (NT x)')))
    must_fail('S1', 'hgΩ dropped from nativeGate2_conj', replace_once(mod, CONJ, CONJ.replace(
        '(hgΩ : ∀ x ∈ Ω, g x ∈ Ω) ', '')))
    must_fail('S1', 'relC of NativeGate2 read with NT on the control side',
              replace_once(mod, RELC, RELC.replace('actC NC (G (actC NC ω))', 'actC NT (G (actC NT ω))')))
    must_fail('S1', 'the conclusion of dim_of_nativeGate2_conj weakened to Odd d',
              replace_once(mod, DIMC, DIMC.replace(': d = 1 ∨ d = 3 :=', ': Odd d :=')))
    must_fail('S1', 'a thirteenth print', replace_once(mod, LASTP, LASTP + '#print axioms OIBridge.CopyCovariance.swap01\n'))
    must_fail('N3', 'a sorry', replace_once(mod, '  exact nativeGate_of_nativeGate2 h2\n', '  sorry\n'))
    # S2
    must_fail('S2', 'a local maxCone', replace_once(mod, '/-! ### §B', 'def maxCone (d : ℕ) : Set (W d) := Set.univ\n\n'
                                                                       '/-! ### §B'))
    must_fail('S2', 'CompositeDimension no longer opened (actT, maxCone, NativeGate no longer resolve)',
              replace_once(mod, 'open TransitiveBody CompositeDimension K2Guard DenseOrbit\n',
                           'open TransitiveBody K2Guard DenseOrbit\n'))
    # S4
    must_fail('S4', 'a frozen phrase in the header', replace_once(mod, '  Every hypothesis is a premise;',
                                                                 '  This replaces copy naturality. Every hypothesis is a premise;'))
    # V -- one-cell mutations, each read by its own rule
    m = replace_once(mod, NOC, NOC.replace(' (hgz : g z = z)', ''))
    check('M', 'decision rule: a broken signature fails only Q-RED',
          [red_cell(m, std, inv), pos_cell(m, std, inv)] == [RED_TOKENS[1], POS_TOKENS[0]])
    m = replace_once(mod, NE, NE.replace('≠ nflip', '≠ swap01'))
    check('M', 'decision rule: a broken control fails only Q-POS',
          [red_cell(m, std, inv), pos_cell(m, std, inv)] == [RED_TOKENS[0], POS_TOKENS[1]])
    p2 = replace_once(PROBE_TEXT, NA5, "NA=[1, 1, -1, -1, -1, -1]")
    rc2, out2 = run_probe_text(p2, kernel)
    check('M', 'decision rule: a probe with one witness value changed (NA at d = 5) fails only Q-EXACT',
          exact_cell(rc2, out2) == EXACT_TOKENS[1] and 'J2 d=5' in parse_probe(out2)[1]
          and red_cell(mod, std, inv) == RED_TOKENS[0] and pos_cell(mod, std, inv) == POS_TOKENS[0])
    rep = dict(std)
    rep[PREFIX + 'swapped_not_ne'] = False
    check('M', 'decision rule: an axiom outside the three on a Q-POS print fails Q-POS and Q-RED, which reads every '
               'print', [red_cell(mod, rep, inv), pos_cell(mod, rep, inv)] == [RED_TOKENS[1], POS_TOKENS[1]])
    rep = dict(std)
    rep[PREFIX + 'nativeGate2_conj'] = False
    check('M', 'decision rule: an axiom outside the three on a Q-RED print fails only Q-RED',
          [red_cell(mod, rep, inv), pos_cell(mod, rep, inv)] == [RED_TOKENS[1], POS_TOKENS[0]])
    check('M', 'decision rule: unmeasured axioms read NOT-ESTABLISHED in both kernel cells',
          [red_cell(mod, None, inv), pos_cell(mod, None, inv)] == [RED_TOKENS[1], POS_TOKENS[1]])
    m = replace_once(mod, RELC, RELC.replace('actC NC (G (actC NC ω))', 'actC NT (G (actC NT ω))'))
    check('M', 'decision rule: NativeGate2 changed fails both kernel cells (Q-POS reads the definitions it names)',
          [red_cell(m, std, inv), pos_cell(m, std, inv)] == [RED_TOKENS[1], POS_TOKENS[1]])
    # the one-NOT limitation: the claim stays scoped to two NOTs
    m = replace_once(mod, NOC_HG, NOC_HG.replace('(hG : NativeGate2 Ω z NC NT G)', '(hG : NativeGate Ω z NC G)'))
    must_fail('S1', 'one-NOT limitation: the reduction restated for one-NOT data', m)
    check('M', 'one-NOT limitation: the reduction restated for one-NOT data fails only Q-RED',
          [red_cell(m, std, inv), pos_cell(m, std, inv)] == [RED_TOKENS[1], POS_TOKENS[0]])
    must_fail('N1', 'one-NOT limitation: a theorem asserting that the swapped gate has no one-NOT reading',
              replace_once(mod, '\nend\n\nend CopyCovariance', '\n' + EXCL + '\nend\n\nend CopyCovariance'))
    must_fail('S1', 'one-NOT limitation: swapped_nativeGate restated with the target NOT (the exact-layer C6 fact is '
                    'not part of the kernel surface)',
              replace_once(mod, SNG, SNG.replace('z3 nflip', 'z3 (swap01 ∘ₗ nflip ∘ₗ swap01)')))
    p3 = replace_once(PROBE_TEXT, C6, C6.replace('relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NT3, NT3)',
                                                 'not (relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NT3, NT3))'))
    rc3, out3 = run_probe_text(p3, kernel)
    check('M', 'one-NOT limitation, measured: a probe asserting that the swapped gate has no one-NOT reading with the '
               'target NOT prints FAIL C6 and reads NOT-ESTABLISHED',
          'C6' in parse_probe(out3)[1] and exact_cell(rc3, out3) == EXACT_TOKENS[1])
    good = [RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[0]]
    note = fixture_note(good)

    def note_fails(n2, toks=good):
        start = len(RESULTS)
        saved = sys.stdout
        sys.stdout = io.StringIO()
        try:
            note_checks(n2, toks)
        finally:
            sys.stdout = saved
        mine = RESULTS[start:]
        del RESULTS[start:]
        return sorted({c for c, ok in mine if not ok})
    check('M', 'note: the fixture note passes V and S4', note_fails(note) == [])
    check('M', 'one-NOT limitation: an earned reading broadened beyond two-NOT data fails V',
          'V' in note_fails(note.replace(EARNED, EARNED.replace('two-NOT native-gate data', 'native-gate data'))))
    lim = 'It does not show that type covariance admits any gate that copy naturality excludes'
    check('M', 'one-NOT limitation: a note without the limitation sentence fails V',
          NONINF.count(lim) == 1 and 'V' in note_fails(note.replace(lim, 'It shows more')))
    check('M', 'one-NOT limitation: a note saying type covariance admits gates that copy naturality excludes fails S4',
          'S4' in note_fails(note + '\nThus type covariance admits gates that copy naturality excludes.\n'))
    check('M', 'note: the earned reading under a non-positive cell fails V',
          'V' in note_fails(fixture_note(good).replace(EXACT_TOKENS[0], EXACT_TOKENS[1]),
                            [RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[1]]))
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens(' '.join(good)) == sorted(good) and note_tokens('KINF-COPY-1-READ') == [])
    # W, P, axioms, registry, I, C
    wd = show(D, WORKFLOW)
    we = apply_edit(wd)
    check('M', 'workflow: the frozen edit applies at D, gates the shard on the verdict line, and a missing test line '
               'or the unchanged file differ from it',
          we is not None and 'test "$(tail -n 1' in SHARD and
          we.replace('          test "${KINFCOPY1_RESULT}" = success\n', '', 1) != we and wd != we)
    check('M', 'axioms: a sorryAx report is outside the three axioms',
          axioms_status(axioms_from_log("'%s' depends on axioms: [propext, sorryAx]\nBuild completed successfully\n"
                                        % PRINTS[0], rev(D)), rev(D))[0] is False)
    check('M', 'registry: a required check that never ran fails the mode, and a False outcome fails it',
          finalize(['A', 'B'], [('A', True)])[0] is False and finalize(['A'], [('A', False)])[0] is False)
    d_imp, d_cen = show(D, IMPORTS), show(D, CENSUS)
    check('M', 'imports and census: the frozen edits pass and the unchanged files fail',
          imports_ok(d_imp, d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)) and
          not imports_ok(d_imp, d_imp) and census_ok(d_cen, census_want(d_cen)) and not census_ok(d_cen, d_cen))
    end_to_end(mod, we)


def end_to_end(mod, we):
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, 'preregistration.md'), encoding='utf-8') as f:
            prereg = f.read()
    except OSError:
        prereg = None
    expect('the preregistration beside this file is readable', prereg is not None)
    if prereg is None:
        return
    own = own_text()
    pin = git_blob_id(own)
    print('  NOTE  the preregistration beside this file %s this controls.py blob %s'
          % ('pins' if pin in prereg else 'does not yet pin', pin))
    pre_f = prereg if pin in prereg else prereg + '\ncontrols.py blob `%s`\n' % pin
    fx = Fixture()
    try:
        d_imp, d_cen = show(D, IMPORTS), show(D, CENSUS)
        exe = {MOD: mod, PROBE: PROBE_TEXT, IMPORTS: d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1),
               CENSUS: census_want(d_cen), WORKFLOW: we}
        good = [RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[0]]
        F = fx.commit([D], D, {PREREG: pre_f})
        C1 = fx.commit([F], F, {CONTROLS: own})
        S1 = fx.commit([C1], C1, exe)
        E = fx.commit([S1], S1, {RESULT: fixture_note(good)})
        print('  NOTE  predicted trees: F %s, S1 %s, E %s' % (git('rev-parse', F + '^{tree}').strip(),
                                                              git('rev-parse', S1 + '^{tree}').strip(),
                                                              git('rev-parse', E + '^{tree}').strip()))
        ax = std_axioms(S1)
        for label, fn, args in (('F mode passes on the fixture F', run_freeze, (F,)),
                                ('check passes at C1', run_check, (C1, F)),
                                ('check passes at S1', run_check, (S1, F)),
                                ('check passes at E with the S1 axiom expected result', run_check, (E, F, None, ax))):
            r = quiet(fn, *args)
            expect('end to end: %s (%s %s)' % (label, r[1], r[2]), r[0])
        start = len(RESULTS)
        saved = sys.stdout
        sys.stdout = io.StringIO()
        try:
            run_verdict(E, axioms=std_axioms(E))
            out = sys.stdout.getvalue()
        finally:
            sys.stdout = saved
            del RESULTS[start:]
        check('M', 'end to end: verdict at E with E\'s own standard axioms prints the three positive tokens',
              dict(re.findall(r'^VERDICT\s+(Q-\S+)\s+(\S+)$', out, re.M)) ==
              {'Q-RED': good[0], 'Q-POS': good[1], 'Q-EXACT': good[2]})
        bad = []
        Fx = fx.commit([D, rev(D + '^')], D, {PREREG: pre_f})
        bad.append(('an F with two parents', 'F', quiet(run_freeze, Fx)))
        Fu = fx.commit([D], D, {PREREG: prereg.replace(pin, '')})
        bad.append(('an F that does not pin this controls.py', 'K', quiet(run_freeze, Fu)))
        Fg = fx.commit([D], D, {PREREG: pre_f.replace('execution M .github/workflows/verify.yml\n', '')})
        bad.append(('an F with the workflow path dropped from the governed block', 'F', quiet(run_freeze, Fg)))
        Sp = fx.commit([C1], C1, dict(exe, **{PROBE: PROBE_TEXT.replace(NA5, "NA=[1, 1, -1, -1, -1, -1]")}))
        bad.append(('a probe changed at S1', 'P', quiet(run_check, Sp, F)))
        Sw = fx.commit([C1], C1, dict(exe, **{WORKFLOW: we.replace('          test "${KINFCOPY1_RESULT}" = success\n',
                                                                     '', 1)}))
        bad.append(('a workflow edit without the aggregate test line', 'W', quiet(run_check, Sw, F)))
        Sk = fx.commit([C1], C1, dict(exe, **{LEAN + 'CompositeDimension.lean':
                                              show(D, LEAN + 'CompositeDimension.lean') + '\n'}))
        bad.append(('the probe\'s kernel source changed', 'G', quiet(run_check, Sk, F)))
        Ee = fx.commit([E], E, {RDIR + 'evidence/axioms.json': '{}\n'})
        bad.append(('an evidence file in the record directory (record control as frozen; AGENTS §A.42 item 2)', 'R',
                    quiet(run_check, Ee, F, None, ax)))
        Er = fx.commit([E], E, {RECEIPT: '{}\n'})
        bad.append(('a receipt before Q', 'G', quiet(run_check, Er, F, None, ax)))
        En = fx.commit([S1, D], S1, {RESULT: fixture_note(good)})
        bad.append(('a merge between S1 and E', 'L', quiet(run_check, En, F, None, ax)))
        Ew = fx.commit([S1], S1, {RESULT: fixture_note([RED_TOKENS[0], POS_TOKENS[0], EXACT_TOKENS[1]])})
        bad.append(('a note stating a token the cells do not give', 'V', quiet(run_check, Ew, F, None, ax)))
        Eb = fx.commit([S1], S1, {RESULT: fixture_note(good).replace('two-NOT native-gate data', 'native-gate data')})
        bad.append(('a note whose earned reading drops the two-NOT scope', 'V', quiet(run_check, Eb, F, None, ax)))
        for label, code, r in bad:
            check('M', 'end to end: %s fails %s (%s)' % (label, code, r[1]), code in r[1])
    finally:
        fx.close()


def main(argv):
    if argv == ['--self-test']:
        self_test()
        n = len(RESULTS)
        req = ['T', 'M']
        expect('the self-test recorded the frozen number of checks (%d of %d)' % (n, SELF_TEST_RECORDS),
               n == SELF_TEST_RECORDS)
    elif len(argv) == 2 and argv[0] == 'freeze':
        req = run_freeze(argv[1])
    elif len(argv) in (4, 6) and argv[0] == 'check' and argv[2] == '--freeze' and \
            (len(argv) == 4 or argv[4] == '--axioms'):
        req = run_check(argv[1], argv[3], argv[5] if len(argv) == 6 else None)
    elif len(argv) in (2, 4) and argv[0] == 'verdict' and (len(argv) == 2 or argv[2] == '--axioms'):
        req = run_verdict(argv[1], argv[3] if len(argv) == 4 else None)
    elif len(argv) in (3, 7) and argv[0] == 'axioms-from-log':
        with open(argv[1], encoding='utf-8') as f:
            text = f.read()
        run = job = None
        if len(argv) == 7 and argv[3] == '--run' and argv[5] == '--job':
            run, job = int(argv[4]), int(argv[6])
        elif len(argv) == 7:
            print(__doc__)
            return 2
        print(json.dumps(axioms_from_log(text, argv[2], run, job), indent=2, sort_keys=True))
        return 0
    else:
        print(__doc__)
        print('controls: refused -- unknown mode or arguments: %s' % ' '.join(argv))
        return 2
    ok, failed, missing = finalize(req)
    if not ok:
        print('controls: FAILED (%d records; failed %s; never ran %s)' % (len(RESULTS), failed, missing))
        return 1
    print('controls: OK -- %d checks' % len(RESULTS))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
