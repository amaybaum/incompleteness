/-
  Conditional pair-cone design proof: replace self-duality H3 with the maxCone upper bound
  and explicit addition/nonnegative-scaling closure. The exact SU(2) block generation and
  pure-state reduction are the measured E19 design dependencies.

  UPPER uses only maxCone and block invariance. LOWER uses products, scaling, addition
  and block invariance. No closedness, self-duality or assumed ReachPure occurs in either
  headline. Full-flow A_miss still includes the cyclic datum.

  This design module does not derive any premise from observational incompleteness.
-/
import OIBridge.EqvK2Generation

namespace OIBridge
namespace EqvK2MaxCone

open Matrix CompositeDimension MonoidalCompletion EqvK2Schema EqvK2Converse EqvK2Block
open scoped ComplexOrder

noncomputable section

/-- Symmetry of the real table pairing. -/
theorem ipW_comm (ω η : W 3) : ipW ω η = ipW η ω := by
  unfold ipW
  apply Finset.sum_congr rfl
  intro μ _
  apply Finset.sum_congr rfl
  intro ν _
  exact mul_comm _ _

/-- The product-state table represents the unscaled product quadratic test. -/
theorem ipW_prodState (ω : W 3) (x y : Fin 3 → ℝ) :
    ipW ω (prodState x y) = pairVal (hom x) (hom y) ω := by
  unfold ipW prodState pairVal
  apply Finset.sum_congr rfl
  intro μ _
  apply Finset.sum_congr rfl
  intro ν _
  ring

/-- A maxCone bound makes every product table a member of the dual. -/
theorem products_mem_dualW_of_maxCone {K : Set (W 3)}
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3)) :
    ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      prodState x y ∈ dualW K := by
  intro x hx y hy
  rw [mem_dualW]
  intro ω hω
  rw [ipW_prodState]
  exact pairVal_nonneg_of_maxCone (hmax hω) (lor_hom hx) (lor_hom hy)

/-- The dual is closed under nonnegative scaling without a closedness assumption on K. -/
theorem dualW_smul {K : Set (W 3)} (c : ℝ) (hc : 0 ≤ c) {ω : W 3}
    (hω : ω ∈ dualW K) : c • ω ∈ dualW K := by
  rw [mem_dualW] at hω ⊢
  intro η hη
  rw [ipW_smul_right]
  exact mul_nonneg hc (hω η hη)

theorem blockMat_conjTranspose (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) :
    (blockMat U₀ U₁)ᴴ = blockMat U₀ᴴ U₁ᴴ := by
  have hP0 : P0ᴴ = P0 := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [P0]
  have hP1 : P1ᴴ = P1 := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [P1]
  simp only [blockMat, Matrix.conjTranspose_add, tensorOf_conjTranspose, hP0, hP1]

/-- The inverse block action is the adjoint of the block action for the table pairing. -/
theorem ipW_blockAct_adjoint (U₀ U₁ : Matrix (Fin 2) (Fin 2) ℂ) (ω η : W 3) :
    ipW ω (blockAct U₀ U₁ η) = ipW (blockAct U₀ᴴ U₁ᴴ ω) η := by
  apply Complex.ofReal_injective
  rw [ipW_eq_trace, ipW_eq_trace, dict_blockAct, dict_blockAct]
  rw [← blockMat_conjTranspose U₀ U₁, Matrix.conjTranspose_conjTranspose]
  congr 1
  calc
    Matrix.trace (dict ω * (blockMat U₀ U₁ * dict η * (blockMat U₀ U₁)ᴴ)) =
        Matrix.trace ((dict ω * blockMat U₀ U₁ * dict η) * (blockMat U₀ U₁)ᴴ) := by
          simp only [Matrix.mul_assoc]
    _ = Matrix.trace ((blockMat U₀ U₁)ᴴ * (dict ω * blockMat U₀ U₁ * dict η)) :=
          Matrix.trace_mul_comm _ _
    _ = Matrix.trace (((blockMat U₀ U₁)ᴴ * dict ω * blockMat U₀ U₁) * dict η) := by
          simp only [Matrix.mul_assoc]

/-- Block invariance transfers to the dual through the available inverse block actions. -/
theorem dualW_blockInvariant {K : Set (W 3)} (hB : BlockInvariant K) :
    BlockInvariant (dualW K) := by
  intro U₀ U₁ hU₀ hU₁ η hη
  rw [mem_dualW] at hη ⊢
  intro ω hω
  rw [ipW_blockAct_adjoint]
  exact hη _ (hB U₀ᴴ U₁ᴴ (isSU_conjTranspose hU₀) (isSU_conjTranspose hU₁) ω hω)

/-- Products and scaling suffice to carry the proved pure-state orbit into K. -/
theorem pure_mem_of_products_scaling_block {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hB : BlockInvariant K) :
    ∀ x : Fin 2 × Fin 2 → ℂ, ∃ ω ∈ K, dict ω = Matrix.vecMulVec x (star x) := by
  intro x
  obtain ⟨U₀, U₁, hU₀, hU₁, x₀, hx₀, c, hc, h⟩ := reach_block x
  refine ⟨blockAct U₀ U₁ (c • prodState x₀ z3),
    hB U₀ U₁ hU₀ hU₁ _ (hsmul c hc _ (hH1 x₀ hx₀ z3 z3_mem_eball)), ?_⟩
  rw [dict_blockAct, h]

/-- LOWER: every PSD table is in K. Addition is explicit; no self-duality is used. -/
theorem Q3_subset_of_products_cone_block {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hB : BlockInvariant K) : Q3 ⊆ K :=
  Q3_subset_of_pure hadd (pure_mem_of_products_scaling_block hH1 hsmul hB)

/-- UPPER: product-test positivity and block invariance force every table in K to be PSD.
This inclusion does not assume that K contains products or is a cone. -/
theorem subset_Q3_of_maxCone_block {K : Set (W 3)}
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3)) (hB : BlockInvariant K) : K ⊆ Q3 := by
  have hpure := pure_mem_of_products_scaling_block (products_mem_dualW_of_maxCone hmax)
    (fun c hc ω hω => dualW_smul c hc hω) (dualW_blockInvariant hB)
  intro η hη
  show (dict η).PosSemidef
  refine posSemidef_dict_of_pure fun x => ?_
  obtain ⟨ω, hω, heq⟩ := hpure x
  refine ⟨ω, heq, ?_⟩
  have h0 := mem_dualW.mp hω η hη
  rw [ipW_comm] at h0
  exact h0

/-- The conditional block theorem with cone closure and maxCone replacing H3. -/
theorem pairCone_eq_Q3_of_block_maxCone {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3)) (hB : BlockInvariant K) : K = Q3 :=
  Set.Subset.antisymm (subset_Q3_of_maxCone_block hmax hB)
    (Q3_subset_of_products_cone_block hH1 hadd hsmul hB)

/-- Forward witness for the block equivalence. -/
theorem blockInvariant_of_eq_Q3 {K : Set (W 3)} (h : K = Q3) : BlockInvariant K := by
  rw [h]
  exact Q3_blockInvariant

/-- Given the cone/product/maxCone premises, equality is equivalent to block invariance.
Witnesses: blockInvariant_of_eq_Q3 and pairCone_eq_Q3_of_block_maxCone. -/
theorem pairCone_eq_Q3_iff_block_maxCone {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3)) : K = Q3 ↔ BlockInvariant K :=
  ⟨blockInvariant_of_eq_Q3, pairCone_eq_Q3_of_block_maxCone hH1 hadd hsmul hmax⟩

/-- Generator form: exact CNOT and full-flow/cyclic invariance generate the needed blocks. -/
theorem pairCone_eq_Q3_of_drive_maxCone {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) : K = Q3 :=
  pairCone_eq_Q3_of_block_maxCone hH1 hadd hsmul hmax
    (EqvK2Generation.blockInvariant_of_drive hH2 hA)

/-- Forward witness for the generator equivalence. -/
theorem driveInvariant_of_eq_Q3 {K : Set (W 3)} (h : K = Q3) :
    (∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ t : ℝ, ∀ ω ∈ K,
      actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  rw [h]
  exact ⟨EqvK2Generation.Q3_cnot, Q3_aMiss⟩

/-- Given cone/product/maxCone premises, equality is equivalent to the full generator invariance.
Witnesses: driveInvariant_of_eq_Q3 and pairCone_eq_Q3_of_drive_maxCone. -/
theorem pairCone_eq_Q3_iff_drive_maxCone {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (TransitiveBody.eball 3)) :
    K = Q3 ↔ ((∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ t : ℝ, ∀ ω ∈ K,
      actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :=
  ⟨driveInvariant_of_eq_Q3, fun ⟨hH2, hA⟩ =>
    pairCone_eq_Q3_of_drive_maxCone hH1 hadd hsmul hmax hH2 hA⟩

end
end EqvK2MaxCone
end OIBridge

#print axioms OIBridge.EqvK2MaxCone.ipW_prodState
#print axioms OIBridge.EqvK2MaxCone.products_mem_dualW_of_maxCone
#print axioms OIBridge.EqvK2MaxCone.ipW_blockAct_adjoint
#print axioms OIBridge.EqvK2MaxCone.dualW_blockInvariant
#print axioms OIBridge.EqvK2MaxCone.pure_mem_of_products_scaling_block
#print axioms OIBridge.EqvK2MaxCone.Q3_subset_of_products_cone_block
#print axioms OIBridge.EqvK2MaxCone.subset_Q3_of_maxCone_block
#print axioms OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_block_maxCone
#print axioms OIBridge.EqvK2MaxCone.blockInvariant_of_eq_Q3
#print axioms OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_block_maxCone
#print axioms OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone
#print axioms OIBridge.EqvK2MaxCone.driveInvariant_of_eq_Q3
#print axioms OIBridge.EqvK2MaxCone.pairCone_eq_Q3_iff_drive_maxCone
