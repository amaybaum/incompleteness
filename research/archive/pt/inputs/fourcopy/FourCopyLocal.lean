/-
  OIBridge/FourCopyLocal.lean — design (EQ4-F), not adopted: the local-map calculus of the
  four-copy package and the gate data it supplies. Every proof in this file is complete.

  * G3: the transpose of a local map is its adjoint for the table pairing (`ipW_actC`,
    `ipW_actT`); the token actions compose (`actC_comp`, `actT_comp`) and commute
    (`actC_actT_comm`); orthogonal local maps are orthogonal for the pairing.
  * O14: a reflection chart on the first token turns `cnot` into `cnotTw`.
  * O15: N-CLASS gates are orthogonal for the pairing (`NClass.ipW_map`).
  * O16, O17: an N-CLASS gate carries a product state of the ball to its Bell table, and a product
    of sharp effects to a quarter of it (`NClass.bell_state`, `NClass.bell_effect`).
  * G4: Bell tables lie in a cone preserved by the gate (`bell_mem`) and, when the inverse gate
    preserves the cone, in its dual (`bell_mem_dual`); products of sharp effects are dual-cone
    tables of every cone inside the maximal cone (`sharp_mem_dualW`).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyCore

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody
open scoped Matrix

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### §A — the transpose -/

theorem trn_apply (N : E3) (u : Fin 3 → ℝ) : trn N u = (LinearMap.toMatrix' N)ᵀ *ᵥ u := by
  rw [trn, Matrix.toLin'_apply]

theorem toMatrix'_trn (A : E3) : LinearMap.toMatrix' (trn A) = (LinearMap.toMatrix' A)ᵀ := by
  rw [trn, LinearMap.toMatrix'_toLin']

theorem trn_trn (A : E3) : trn (trn A) = A := by
  apply LinearMap.toMatrix'.injective
  rw [toMatrix'_trn, toMatrix'_trn, Matrix.transpose_transpose]

/-- The transpose is the adjoint for the dot product of one ball. -/
theorem lin_adj (N : E3) (u v : Fin 3 → ℝ) : ∑ j, u j * N v j = ∑ j, trn N u j * v j := by
  rw [trn_apply, ← LinearMap.toMatrix'_mulVec N v]
  show u ⬝ᵥ (LinearMap.toMatrix' N *ᵥ v) = ((LinearMap.toMatrix' N)ᵀ *ᵥ u) ⬝ᵥ v
  rw [Matrix.dotProduct_mulVec, Matrix.mulVec_transpose]

/-- The homogenized action of the transpose is the adjoint of the homogenized action. -/
theorem homMap_adj (N : E3) (u v : HVec 3) :
    ∑ μ, u μ * homMap N v μ = ∑ μ, homMap (trn N) u μ * v μ := by
  conv_lhs => rw [Fin.sum_univ_succ]
  conv_rhs => rw [Fin.sum_univ_succ]
  rw [homMap_zero, homMap_zero]
  congr 1
  simp only [homMap_succ]
  exact lin_adj N (Matrix.vecTail u) (Matrix.vecTail v)

/-- **G3a.** The transpose of a control-side map is its adjoint for the table pairing. -/
theorem ipW_actC (M : E3) (E X : W 3) : ipW E (actC M X) = ipW (actC (trn M) E) X := by
  have h : ∀ ν, ∑ μ, E μ ν * actC M X μ ν = ∑ μ, actC (trn M) E μ ν * X μ ν := fun ν =>
    homMap_adj M (fun κ => E κ ν) (fun κ => X κ ν)
  unfold ipW
  rw [Finset.sum_comm]
  conv_rhs => rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun ν _ => h ν

/-- **G3b.** The same on the target side. -/
theorem ipW_actT (M : E3) (E X : W 3) : ipW E (actT M X) = ipW (actT (trn M) E) X := by
  unfold ipW
  exact Finset.sum_congr rfl fun μ _ => homMap_adj M (E μ) (X μ)

/-! ### §B — composition and commutation of the token actions -/

theorem homMap_comp (M N : E3) (v : HVec 3) : homMap (M ∘ₗ N) v = homMap M (homMap N v) := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rfl
  · rw [homMap_succ, homMap_succ, vecTail_homMap, LinearMap.comp_apply]

theorem homMap_id (v : HVec 3) : homMap LinearMap.id v = v := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · rfl
  · rw [homMap_succ, LinearMap.id_apply] <;> rfl

/-- **G3c.** -/
theorem actC_comp (M N : E3) (ω : W 3) : actC M (actC N ω) = actC (M ∘ₗ N) ω := by
  funext μ ν
  show homMap M (homMap N (fun κ => ω κ ν)) μ = homMap (M ∘ₗ N) (fun κ => ω κ ν) μ
  rw [homMap_comp]

theorem actT_comp (M N : E3) (ω : W 3) : actT M (actT N ω) = actT (M ∘ₗ N) ω := by
  funext μ
  show homMap M (homMap N (ω μ)) = homMap (M ∘ₗ N) (ω μ)
  rw [homMap_comp]

theorem actC_id (ω : W 3) : actC LinearMap.id ω = ω := by
  funext μ ν
  exact congrFun (homMap_id (fun κ => ω κ ν)) μ

theorem actT_id (ω : W 3) : actT LinearMap.id ω = ω := by
  funext μ
  exact homMap_id (ω μ)

theorem lin_apply_eq_sum (M : E3) (x : Fin 3 → ℝ) (i : Fin 3) :
    M x i = ∑ k, LinearMap.toMatrix' M i k * x k :=
  (congrFun (LinearMap.toMatrix'_mulVec M x) i).symm

theorem lin_lin_comm (M N : E3) (Ω' : Fin 3 → Fin 3 → ℝ) (i j : Fin 3) :
    M (fun i' => N (Ω' i') j) i = N (fun j' => M (fun i' => Ω' i' j') i) j := by
  simp only [lin_apply_eq_sum M, lin_apply_eq_sum N, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun l _ => Finset.sum_congr rfl fun k _ => ?_
  ring

/-- **G3d.** The two token actions commute. -/
theorem actC_actT_comm (M N : E3) (ω : W 3) : actC M (actT N ω) = actT N (actC M ω) := by
  funext μ ν
  refine Fin.cases ?_ (fun i => ?_) μ <;> refine Fin.cases ?_ (fun j => ?_) ν
  · rfl
  · rfl
  · rfl
  · simp only [actC_apply, actT_apply, homMap_succ, Matrix.vecTail, Function.comp_def]
    exact lin_lin_comm M N (fun i' j' => ω i'.succ j'.succ) i j

/-! ### §C — orthogonal local maps -/

theorem trn_comp_self {A : E3} (hA : IsOrth3 A) : trn A ∘ₗ A = LinearMap.id := by
  apply LinearMap.toMatrix'.injective
  rw [LinearMap.toMatrix'_comp, toMatrix'_trn, LinearMap.toMatrix'_id]
  exact (Matrix.mem_orthogonalGroup_iff' _ _).1 hA

theorem comp_trn_self {A : E3} (hA : IsOrth3 A) : A ∘ₗ trn A = LinearMap.id := by
  apply LinearMap.toMatrix'.injective
  rw [LinearMap.toMatrix'_comp, toMatrix'_trn, LinearMap.toMatrix'_id]
  exact (Matrix.mem_orthogonalGroup_iff _ _).1 hA

theorem trn_apply_apply {A : E3} (hA : IsOrth3 A) (x : Fin 3 → ℝ) : trn A (A x) = x := by
  show (trn A ∘ₗ A) x = x
  rw [trn_comp_self hA, LinearMap.id_apply]

theorem apply_trn_apply {A : E3} (hA : IsOrth3 A) (x : Fin 3 → ℝ) : A (trn A x) = x := by
  show (A ∘ₗ trn A) x = x
  rw [comp_trn_self hA, LinearMap.id_apply]

theorem isOrth3_trn {A : E3} (hA : IsOrth3 A) : IsOrth3 (trn A) := by
  unfold IsOrth3
  rw [toMatrix'_trn, Matrix.mem_orthogonalGroup_iff, Matrix.transpose_transpose]
  exact (Matrix.mem_orthogonalGroup_iff' _ _).1 hA

theorem isOrth3_comp {A B : E3} (hA : IsOrth3 A) (hB : IsOrth3 B) : IsOrth3 (A ∘ₗ B) := by
  unfold IsOrth3 at *
  rw [LinearMap.toMatrix'_comp]
  exact Submonoid.mul_mem _ hA hB

theorem toMatrix'_reflY :
    LinearMap.toMatrix' reflY = Matrix.diagonal (![1, -1, 1] : Fin 3 → ℝ) := by
  have h : reflY = Matrix.toLin' (Matrix.diagonal (![1, -1, 1] : Fin 3 → ℝ)) := by
    refine LinearMap.ext fun x => funext fun i => ?_
    rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal, reflY_apply]
  rw [h, LinearMap.toMatrix'_toLin']

theorem isOrth3_reflY : IsOrth3 reflY := by
  unfold IsOrth3
  rw [toMatrix'_reflY, Matrix.mem_orthogonalGroup_iff, Matrix.diagonal_transpose,
    Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  funext i
  fin_cases i <;> norm_num

/-- Orthogonal maps preserve the sum of squares. -/
theorem sumsq_orth {A : E3} (hA : IsOrth3 A) (x : Fin 3 → ℝ) :
    ∑ j, A x j ^ 2 = ∑ j, x j ^ 2 := by
  have h := lin_adj A (A x) x
  rw [trn_apply_apply hA] at h
  simp only [sq]
  exact h

theorem orth_mem_eball {A : E3} (hA : IsOrth3 A) {x : Fin 3 → ℝ} (hx : x ∈ eball 3) :
    A x ∈ eball 3 := by
  rw [mem_eball, sumsq_orth hA]
  exact hx

theorem ipW_actC_orth {A : E3} (hA : IsOrth3 A) (Y Z : W 3) :
    ipW (actC A Y) (actC A Z) = ipW Y Z := by
  rw [ipW_actC, actC_comp, trn_comp_self hA, actC_id]

theorem ipW_actT_orth {A : E3} (hA : IsOrth3 A) (Y Z : W 3) :
    ipW (actT A Y) (actT A Z) = ipW Y Z := by
  rw [ipW_actT, actT_comp, trn_comp_self hA, actT_id]

theorem cnot_cnot (ω : W 3) : cnot (cnot ω) = ω := by
  show cnotFun (cnotFun ω) = ω
  exact cnotFun_cnotFun ω

theorem ipW_cnot_orth (Y Z : W 3) : ipW (cnot Y) (cnot Z) = ipW Y Z := by
  rw [ipW_cnot, cnot_cnot]

theorem ipW_smul_left (c : ℝ) (E X : W 3) : ipW (c • E) X = c * ipW E X := by
  unfold ipW
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun ν _ => ?_
  simp only [Pi.smul_apply, smul_eq_mul]
  ring

/-! ### §D — O14: the reflection chart on the first token -/

/-- **O14.** A reflection chart on the first token also turns `cnot` into `cnotTw`. -/
theorem actC_reflY_cnot_actC_reflY (ω : W 3) :
    actC reflY (cnot (actC reflY ω)) = cnotTw ω := by
  rw [cnotTw_apply]
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actC_apply, actT_apply, cnot_apply, cnotFun_apply, sgn, pc, pt]

/-! ### §E — O15–O17: N-CLASS gates -/

/-- **O15.** N-CLASS gates are orthogonal for the pairing. -/
theorem NClass.ipW_map {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (h : NClass N A B A' B')
    (E X : W 3) : ipW (N E) (N X) = ipW E X := by
  obtain ⟨hA, hB, hA', hB', hN⟩ := h
  rw [hN, hN, ipW_actC_orth hA, ipW_actT_orth hB, ipW_cnot_orth, ipW_actC_orth hA',
    ipW_actT_orth hB']

theorem actC_prodState (M : E3) (x y : Fin 3 → ℝ) :
    actC M (prodState x y) = prodState (M x) y := by
  show actC M (tens (hom x) (hom y)) = tens (hom (M x)) (hom y)
  rw [actC_tens, homMap_hom]

/-- An N-CLASS gate on a product state, with its pre-locals absorbed. -/
theorem NClass.apply_prodState {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (h : NClass N A B A' B')
    (x y : Fin 3 → ℝ) :
    N (prodState (trn A' x) (trn B' y)) = actC A (actT B (cnot (prodState x y))) := by
  obtain ⟨-, -, hA', hB', hN⟩ := h
  rw [hN, actT_prodState, actC_prodState, apply_trn_apply hA', apply_trn_apply hB']

/-- **O16.** Bell state: the gate applied to a product state of the ball. -/
theorem NClass.bell_state {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (h : NClass N A B A' B') :
    ∃ x ∈ eball 3, ∃ y ∈ eball 3, N (prodState x y) = bellOf A B := by
  refine ⟨trn A' xplus, orth_mem_eball (isOrth3_trn h.2.2.1) xplus_mem, trn B' z3,
    orth_mem_eball (isOrth3_trn h.2.2.2.1) z3_mem, ?_⟩
  rw [h.apply_prodState, cnot_prodState_xplus_z3, bellOf]

/-- **O17.** Bell effect: the gate applied to a product of sharp effects is `¼ H_R`. -/
theorem NClass.bell_effect {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (h : NClass N A B A' B') :
    ∃ b c : Fin 3 → ℝ, ∑ j, b j ^ 2 = 1 ∧ ∑ j, c j ^ 2 = 1 ∧
      N (tens (sharpVec b) (sharpVec c)) = (1 / 4 : ℝ) • bellOf A B := by
  refine ⟨trn A' xplus, trn B' z3, (sumsq_orth (isOrth3_trn h.2.2.1) xplus).trans xplus_sq,
    (sumsq_orth (isOrth3_trn h.2.2.2.1) z3).trans z3_sq, ?_⟩
  rw [tens_sharpVec, N.map_smul, h.apply_prodState, cnot_prodState_xplus_z3, bellOf]

/-! ### §F — G4: Bell data in the cone and in its dual -/

/-- **G4a.** Products of sharp effects are dual-cone tables of every cone inside the maximal
cone. -/
theorem sharp_mem_dualW {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3)) {b c : Fin 3 → ℝ}
    (hb : ∑ j, b j ^ 2 = 1) (hc : ∑ j, c j ^ 2 = 1) :
    tens (sharpVec b) (sharpVec c) ∈ dualW K := by
  refine mem_dualW.2 fun X hX => ?_
  rw [ipW_tens, ← prodEffVal_sharp]
  exact hK hX _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- **G4b.** The Bell table lies in every cone containing the products that the gate preserves. -/
theorem bell_mem {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hprod : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hgate : ∀ ω ∈ K, N ω ∈ K) : bellOf A B ∈ K := by
  obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state
  rw [← hxy]
  exact hgate _ (hprod x hx y hy)

/-- **G4c.** The Bell table is a dual-cone table when the inverse gate preserves the cone. -/
theorem bell_mem_dual {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3)) (hinv : ∀ ω ∈ K, N.symm ω ∈ K) :
    bellOf A B ∈ dualW K := by
  obtain ⟨b, c, hb, hc, hbc⟩ := hcls.bell_effect
  have h := dualW_of_inv hcls.ipW_map hinv (sharp_mem_dualW hK hb hc)
  rw [hbc] at h
  refine mem_dualW.2 fun X hX => ?_
  have h1 := mem_dualW.1 h X hX
  rw [ipW_smul_left] at h1
  exact (mul_nonneg_iff_of_pos_left (by norm_num)).1 h1

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.lin_adj
#print axioms OIBridge.FourCopy.homMap_adj
#print axioms OIBridge.FourCopy.ipW_actC
#print axioms OIBridge.FourCopy.ipW_actT
#print axioms OIBridge.FourCopy.actC_comp
#print axioms OIBridge.FourCopy.actT_comp
#print axioms OIBridge.FourCopy.actC_id
#print axioms OIBridge.FourCopy.actT_id
#print axioms OIBridge.FourCopy.actC_actT_comm
#print axioms OIBridge.FourCopy.trn_trn
#print axioms OIBridge.FourCopy.trn_comp_self
#print axioms OIBridge.FourCopy.comp_trn_self
#print axioms OIBridge.FourCopy.isOrth3_trn
#print axioms OIBridge.FourCopy.isOrth3_comp
#print axioms OIBridge.FourCopy.isOrth3_reflY
#print axioms OIBridge.FourCopy.sumsq_orth
#print axioms OIBridge.FourCopy.ipW_actC_orth
#print axioms OIBridge.FourCopy.ipW_actT_orth
#print axioms OIBridge.FourCopy.actC_reflY_cnot_actC_reflY
#print axioms OIBridge.FourCopy.NClass.ipW_map
#print axioms OIBridge.FourCopy.NClass.apply_prodState
#print axioms OIBridge.FourCopy.NClass.bell_state
#print axioms OIBridge.FourCopy.NClass.bell_effect
#print axioms OIBridge.FourCopy.sharp_mem_dualW
#print axioms OIBridge.FourCopy.bell_mem
#print axioms OIBridge.FourCopy.bell_mem_dual
