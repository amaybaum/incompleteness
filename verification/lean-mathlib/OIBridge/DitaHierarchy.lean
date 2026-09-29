import OIBridge.DitaHull

/-!
# Act 36 — the Diţă factorization hierarchy at the product-embedded stratum

At act 29's product configuration, act 35's column and row Diţă constructions with `4 × 4` factors
give two fourteen-dimensional hulls through every stratum point. This module states Diţă's
construction over any factorization of the sixteen-point carrier — an outer factor on `α`, inner
factors on `β`, a twist, and any bijections of `α × β` with the product carrier for rows and for
columns — realizable for flat unitary factors and unit twists; its `2 × 8` and `8 × 2` instances;
an exact one-parameter family through the certified rational stratum point `F₄(z) ⊗ F₄(w)`,
`z = (3+4i)/5`, `w = (5+12i)/13`, whose every member is a `2 × 8` Diţă matrix; and the named point
`P = SIG ∘ u^W`, `u = (60+i)/(60−i)`, realizable, off the stratum by an exact cross-ratio value
`u/256`. Exact computation over every index map (act 41) shows that `P` admits no `4 × 4` Diţă
factorization of either orientation: the `4 × 4` hierarchy is locally insufficient at the stratum,
and the first escaping family belongs to the `2 × 8` construction.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaHierarchy

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull

theorem a36_shared_sq_quarter :
    ∀ x : ℝ, 0 ≤ x → x ^ 2 = 1 / 16 → x = 1 / 4 := by
  intro x hx h
  have h2 : (x - 1 / 4) * (x + 1 / 4) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h2 with h3 | h3
  · linarith
  · linarith
#print axioms a36_shared_sq_quarter

theorem a36_shared_pow_unit :
    ∀ (u : ℂ) (n : ℕ), star u * u = 1 → star (u ^ n) * u ^ n = 1 := by
  intro u n hu
  rw [star_pow, ← mul_pow, hu, one_pow]
#print axioms a36_shared_pow_unit

theorem a36_shared_z_unit :
    star (3 / 5 + (4 / 5) * Complex.I) * (3 / 5 + (4 / 5) * Complex.I) = (1 : ℂ) := by
  simp [Complex.ext_iff, Complex.star_def] <;> norm_num
#print axioms a36_shared_z_unit

theorem a36_shared_w_unit :
    star (5 / 13 + (12 / 13) * Complex.I) * (5 / 13 + (12 / 13) * Complex.I) = (1 : ℂ) := by
  simp [Complex.ext_iff, Complex.star_def] <;> norm_num
#print axioms a36_shared_w_unit

theorem a36_shared_u60_unit :
    star (3599 / 3601 + (120 / 3601) * Complex.I) * (3599 / 3601 + (120 / 3601) * Complex.I) = (1 : ℂ) := by
  simp [Complex.ext_iff, Complex.star_def] <;> norm_num
#print axioms a36_shared_u60_unit

theorem a36_shared_div :
    ∀ a : Fin 4, @Fin.divNat 2 2 a = ![0, 0, 1, 1] a := by
  decide
#print axioms a36_shared_div

theorem a36_shared_mod :
    ∀ a : Fin 4, @Fin.modNat 2 2 a = ![0, 1, 0, 1] a := by
  decide
#print axioms a36_shared_mod

theorem a36_shared_dg_unitary :
    ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), X ∈ Matrix.unitaryGroup α ℂ → (∀ c, Y c ∈ Matrix.unitaryGroup β ℂ) → (∀ c b, ‖D c b‖ = 1) → (Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) ∈ Matrix.unitaryGroup (α × β) ℂ := by
  intro α β _ _ _ _ X Y D hX hY hD
  rw [Matrix.mem_unitaryGroup_iff]
  have hX' := Matrix.mem_unitaryGroup_iff.1 hX
  have hY' := fun c => Matrix.mem_unitaryGroup_iff.1 (hY c)
  have hDD : ∀ c b, D c b * star (D c b) = 1 := fun c b => by
    rw [mul_comm]; exact a35_shared_unit_of_norm _ (hD c b)
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  rw [Fintype.sum_prod_type]
  have key : ∀ c : α, ∑ d : β, X i.1 c * D c i.2 * Y c i.2 d * star (X i'.1 c * D c i'.2 * Y c i'.2 d)
      = X i.1 c * star (X i'.1 c) * (D c i.2 * star (D c i'.2)) * (Y c * star (Y c)) i.2 i'.2 := by
    intro c
    rw [Matrix.mul_apply, Finset.mul_sum]
    refine Finset.sum_congr rfl fun d _ => ?_
    simp only [Matrix.star_apply, star_mul]
    ring
  simp only [key, hY', Matrix.one_apply]
  have hx := congrFun (congrFun hX' i.1) i'.1
  rw [Matrix.mul_apply, Matrix.one_apply] at hx
  simp only [Matrix.star_apply] at hx
  by_cases h2 : i.2 = i'.2
  · simp only [h2, if_true, mul_one, hDD]
    rw [hx]
    by_cases h1 : i.1 = i'.1
    · simp [h1, Prod.ext_iff, h2]
    · simp [h1, Prod.ext_iff]
  · simp [h2, Prod.ext_iff]
#print axioms a36_shared_dg_unitary

theorem a36_shared_dgT_eq :
    ∀ {α β : Type} (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) = (Matrix.of fun i j : α × β => Xᵀ i.1 j.1 * E j.1 i.2 * (fun a => (Y a)ᵀ) j.1 i.2 j.2)ᵀ := by
  intro α β X Y E
  ext i j
  simp only [Matrix.transpose_apply, Matrix.of_apply]
#print axioms a36_shared_dgT_eq

theorem a36_shared_dgT_unitary :
    ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), X ∈ Matrix.unitaryGroup α ℂ → (∀ a, Y a ∈ Matrix.unitaryGroup β ℂ) → (∀ a d, ‖E a d‖ = 1) → (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) ∈ Matrix.unitaryGroup (α × β) ℂ := by
  intro α β _ _ _ _ X Y E hX hY hE
  rw [a36_shared_dgT_eq]
  exact transpose_unitary (a36_shared_dg_unitary Xᵀ (fun a => (Y a)ᵀ) E (transpose_unitary hX) (fun a => transpose_unitary (hY a)) hE)
#print axioms a36_shared_dgT_unitary

theorem a36_shared_reindex_unitary :
    ∀ {m n : Type} [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n] (M : Matrix n n ℂ) (r c : m → n), Function.Bijective r → Function.Bijective c → M ∈ Matrix.unitaryGroup n ℂ → (Matrix.of fun i j : m => M (r i) (c j)) ∈ Matrix.unitaryGroup m ℂ := by
  intro m n _ _ _ _ M r c hr hc hM
  rw [Matrix.mem_unitaryGroup_iff] at hM ⊢
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have h := congrFun (congrFun hM (r i)) (r i')
  rw [Matrix.mul_apply, Matrix.one_apply] at h
  simp only [Matrix.star_apply] at h
  rw [show (∑ j, M (r i) (c j) * star (M (r i') (c j))) = ∑ j, M (r i) j * star (M (r i') j) from
    Function.Bijective.sum_comp hc (fun j => M (r i) j * star (M (r i') j)), h]
  simp only [hr.injective.eq_iff]
#print axioms a36_shared_reindex_unitary

theorem a36_shared_dg_norm_sq :
    ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), (∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)) → (∀ c, ∀ b d, ‖Y c b d‖ ^ 2 = 1 / (Fintype.card β : ℝ)) → (∀ c b, ‖D c b‖ = 1) → ∀ i j : α × β, ‖X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2‖ ^ 2 = 1 / ((Fintype.card α : ℝ) * (Fintype.card β : ℝ)) := by
  intro α β _ _ _ _ X Y D hX hY hD i j
  rw [norm_mul, norm_mul, mul_pow, mul_pow, hX, hD, hY, one_pow, mul_one, div_mul_div_comm, one_mul]
#print axioms a36_shared_dg_norm_sq

theorem a36_shared_dgT_norm_sq :
    ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), (∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)) → (∀ a, ∀ b d, ‖Y a b d‖ ^ 2 = 1 / (Fintype.card β : ℝ)) → (∀ a d, ‖E a d‖ = 1) → ∀ i j : α × β, ‖X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2‖ ^ 2 = 1 / ((Fintype.card α : ℝ) * (Fintype.card β : ℝ)) := by
  intro α β _ _ _ _ X Y E hX hY hE i j
  rw [norm_mul, norm_mul, mul_pow, mul_pow, hX, hE, hY, one_pow, mul_one, div_mul_div_comm, one_mul]
#print axioms a36_shared_dgT_norm_sq

theorem a36_shared_hullg_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), (X ∈ Matrix.unitaryGroup (α) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (α) : ℝ)) → (∀ c, (Y c ∈ Matrix.unitaryGroup (β) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (β) : ℝ))) → (∀ c b, ‖D c b‖ = 1) →
    (Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm i j) * (Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm i k) := by
  intro Γ₀ hΓ₀ α β _ _ _ _ eR eC X Y D hX hY hD
  have hcard0 : Fintype.card α * Fintype.card β = 16 := by
    rw [← Fintype.card_prod, Fintype.card_congr eR]; simp
  have hcard : (Fintype.card α : ℝ) * (Fintype.card β : ℝ) = 16 := by exact_mod_cast hcard0
  have hu : (Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
    a36_shared_reindex_unitary (Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) eR.symm eC.symm eR.symm.bijective eC.symm.bijective (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
  have hn : ∀ i j, ‖(Matrix.of fun i j : α × β => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2).submatrix eR.symm eC.symm i j‖ = 1 / 4 := by
    intro i j
    apply a36_shared_sq_quarter _ (norm_nonneg _)
    simp only [Matrix.submatrix_apply, Matrix.of_apply]
    rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD, hcard]
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩
#print axioms a36_shared_hullg_core

theorem a36_shared_hullgt_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), (X ∈ Matrix.unitaryGroup (α) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (α) : ℝ)) → (∀ c, (Y c ∈ Matrix.unitaryGroup (β) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (β) : ℝ))) → (∀ c d, ‖E c d‖ = 1) →
    (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm i j) * (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm i k) := by
  intro Γ₀ hΓ₀ α β _ _ _ _ eR eC X Y E hX hY hE
  have hcard0 : Fintype.card α * Fintype.card β = 16 := by
    rw [← Fintype.card_prod, Fintype.card_congr eR]; simp
  have hcard : (Fintype.card α : ℝ) * (Fintype.card β : ℝ) = 16 := by exact_mod_cast hcard0
  have hu : (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
    a36_shared_reindex_unitary (Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) eR.symm eC.symm eR.symm.bijective eC.symm.bijective (a36_shared_dgT_unitary X Y E hX.1 (fun c => (hY c).1) hE)
  have hn : ∀ i j, ‖(Matrix.of fun i j : α × β => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2).submatrix eR.symm eC.symm i j‖ = 1 / 4 := by
    intro i j
    apply a36_shared_sq_quarter _ (norm_nonneg _)
    simp only [Matrix.submatrix_apply, Matrix.of_apply]
    rw [a36_shared_dgT_norm_sq X Y E hX.2 (fun c => (hY c).2) hE, hcard]
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩
#print axioms a36_shared_hullgt_core

theorem a36_shared_hull28_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) → (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) → (∀ c b, ‖D c b‖ = 1) →
    (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) i k) := by
  intro Γ₀ hΓ₀ X Y D hX hY hD
  first
  | exact a36_shared_hullg_core Γ₀ hΓ₀ (((@finProdFinEquiv 2 2).symm.prodCongr (Equiv.refl (Fin 4))).trans ((Equiv.prodAssoc (Fin 2) (Fin 2) (Fin 4)).trans ((Equiv.refl (Fin 2)).prodCongr (@finProdFinEquiv 2 4)))).symm ((((@finProdFinEquiv 2 2).symm.trans (Equiv.prodComm (Fin 2) (Fin 2))).prodCongr (Equiv.refl (Fin 4))).trans ((Equiv.prodAssoc (Fin 2) (Fin 2) (Fin 4)).trans ((Equiv.refl (Fin 2)).prodCongr (@finProdFinEquiv 2 4)))).symm X Y D hX hY hD
  | (have hr : Function.Bijective (fun i : Fin 4 × Fin 4 => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))) :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hc : Function.Bijective (fun j : Fin 4 × Fin 4 => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hu : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
      a36_shared_reindex_unitary (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))) (fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) hr hc (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
     have hn : ∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) i j‖ = 1 / 4 := by
       intro i j
       apply a36_shared_sq_quarter _ (norm_nonneg _)
       simp only [Matrix.of_apply]
       rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD]
       norm_num [Fintype.card_fin]
     exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩)
#print axioms a36_shared_hull28_core

theorem a36_shared_hull82_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) → (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) → (∀ c b, ‖D c b‖ = 1) →
    (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) i k) := by
  intro Γ₀ hΓ₀ X Y D hX hY hD
  first
  | exact a36_shared_hullg_core Γ₀ hΓ₀ (((Equiv.refl (Fin 4)).prodCongr (@finProdFinEquiv 2 2).symm).trans ((Equiv.prodAssoc (Fin 4) (Fin 2) (Fin 2)).symm.trans ((@finProdFinEquiv 4 2).prodCongr (Equiv.refl (Fin 2))))).symm (((Equiv.refl (Fin 4)).prodCongr (@finProdFinEquiv 2 2).symm).trans ((Equiv.prodAssoc (Fin 4) (Fin 2) (Fin 2)).symm.trans ((@finProdFinEquiv 4 2).prodCongr (Equiv.refl (Fin 2))))).symm X Y D hX hY hD
  | (have hr : Function.Bijective (fun i : Fin 4 × Fin 4 => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)) :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hc : Function.Bijective (fun j : Fin 4 × Fin 4 => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hu : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
      a36_shared_reindex_unitary (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)) (fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) hr hc (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
     have hn : ∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2) (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)) i j‖ = 1 / 4 := by
       intro i j
       apply a36_shared_sq_quarter _ (norm_nonneg _)
       simp only [Matrix.of_apply]
       rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD]
       norm_num [Fintype.card_fin]
     exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩)
#print axioms a36_shared_hull82_core

theorem a36_shared_xo_flat :
    ((Matrix.of fun a c : Fin 2 => ((1 + Complex.I) / 2) * !![1, 1; 1, -1] a c) ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 2 => ((1 + Complex.I) / 2) * !![1, 1; 1, -1] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff]
    ext i j
    rw [Matrix.mul_apply, Matrix.one_apply, Fin.sum_univ_two]
    simp only [Matrix.star_apply, Matrix.of_apply]
    fin_cases i <;> fin_cases j <;> simp [Complex.ext_iff, Complex.star_def] <;> norm_num
  · intro a c
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, Fintype.card_fin]
    simp only [Matrix.of_apply]
    fin_cases a <;> fin_cases c <;> simp <;> norm_num
#print axioms a36_shared_xo_flat

theorem a36_shared_xi_flat :
    ((Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff]
    ext i j
    rw [Matrix.mul_apply, Matrix.one_apply, Fin.sum_univ_two]
    simp only [Matrix.star_apply, Matrix.of_apply]
    fin_cases i <;> fin_cases j <;> simp [Complex.ext_iff, Complex.star_def] <;> norm_num
  · intro a c
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, Fintype.card_fin]
    simp only [Matrix.of_apply]
    fin_cases a <;> fin_cases c <;> simp <;> norm_num
#print axioms a36_shared_xi_flat

theorem a36_shared_phase_unitary :
    ∀ {n : Type} [Fintype n] [DecidableEq n] (M : Matrix n n ℂ) (s : ℂ) (p : n → ℂ), M ∈ Matrix.unitaryGroup n ℂ → star s * s = 1 → (∀ b, star (p b) * p b = 1) → (Matrix.of fun b d : n => s * p b * M b d) ∈ Matrix.unitaryGroup n ℂ := by
  intro n _ _ M s p hM hs hp
  have hs' : s * star s = 1 := by rw [mul_comm]; exact hs
  have hp' : ∀ b, p b * star (p b) = 1 := fun b => by rw [mul_comm]; exact hp b
  rw [Matrix.mem_unitaryGroup_iff] at hM ⊢
  ext b b'
  have h := congrFun (congrFun hM b) b'
  rw [Matrix.mul_apply, Matrix.one_apply] at h
  simp only [Matrix.star_apply] at h
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have key : ∀ d, s * p b * M b d * star (s * p b' * M b' d) = (s * star s) * (p b * star (p b')) * (M b d * star (M b' d)) := by
    intro d; simp only [star_mul]; ring
  simp only [key, ← Finset.mul_sum, h]
  by_cases hb : b = b'
  · subst hb
    rw [if_pos rfl, mul_one, hs', hp', mul_one]
  · rw [if_neg hb, mul_zero]
#print axioms a36_shared_phase_unitary

theorem a36_shared_zp_flat :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (c a : Fin 2), ((fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) a ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖(fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) a a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) := by
  intro Γ₀ hΓ₀ z w u hz hw hu c a
  have hs : star (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 1 ∧ a = 1 then z else (1 : ℂ)) = 1 := by
    split_ifs <;> first | exact hz | simp
  have hp : ∀ b : Fin 4, star (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) = 1 := by
    intro b
    split_ifs <;> first | exact a36_shared_pow_unit u _ hu | simp
  refine ⟨?_, ?_⟩
  · exact a36_shared_phase_unitary (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) _ _ (a35_shared_f4_flat Γ₀ hΓ₀ w hw).1 hs hp
  · intro b d
    show ‖(if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * ((1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] b d)‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)
    have h3 : ‖(1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] b d‖ = 1 / 2 := a35_shared_half w hw b d
    rw [norm_mul, norm_mul, a35_shared_norm_of_unit _ hs, a35_shared_norm_of_unit _ (hp b), h3, Fintype.card_fin]
    norm_num
#print axioms a36_shared_zp_flat

theorem a36_shared_y8_flat :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ c : Fin 2, ((fun c : Fin 2 => Matrix.of fun k l : Fin 8 => (Matrix.of fun i j : Fin 2 × Fin 4 => (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) i.1 j.2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) i.1 i.2 j.2) ((@finProdFinEquiv 2 4).symm k) ((@finProdFinEquiv 2 4).symm l)) c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖(fun c : Fin 2 => Matrix.of fun k l : Fin 8 => (Matrix.of fun i j : Fin 2 × Fin 4 => (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) i.1 j.2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) i.1 i.2 j.2) ((@finProdFinEquiv 2 4).symm k) ((@finProdFinEquiv 2 4).symm l)) c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) := by
  intro Γ₀ hΓ₀ z w u hz hw hu c
  have hE : ∀ (a : Fin 2) (d : Fin 4), ‖(fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) a d‖ = 1 := by
    intro a d
    show ‖(if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ))‖ = 1
    split_ifs <;> first | exact a35_shared_norm_of_unit _ (a36_shared_pow_unit u _ hu) | simp
  have hZ := a36_shared_zp_flat Γ₀ hΓ₀ z w u hz hw hu c
  have hU := a36_shared_dgT_unitary (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) a36_shared_xi_flat.1 (fun a => (hZ a).1) hE
  refine ⟨?_, ?_⟩
  · exact a36_shared_reindex_unitary (Matrix.of fun i j : Fin 2 × Fin 4 => (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) i.1 j.2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) i.1 i.2 j.2) (@finProdFinEquiv 2 4).symm (@finProdFinEquiv 2 4).symm (@finProdFinEquiv 2 4).symm.bijective (@finProdFinEquiv 2 4).symm.bijective hU
  · intro k l
    show ‖(Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) ((@finProdFinEquiv 2 4).symm k).1 ((@finProdFinEquiv 2 4).symm l).1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) ((@finProdFinEquiv 2 4).symm k).1 ((@finProdFinEquiv 2 4).symm l).2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) ((@finProdFinEquiv 2 4).symm k).1 ((@finProdFinEquiv 2 4).symm k).2 ((@finProdFinEquiv 2 4).symm l).2‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)
    rw [a36_shared_dgT_norm_sq (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) a36_shared_xi_flat.2 (fun a => (hZ a).2) hE]
    norm_num [Fintype.card_fin]
#print axioms a36_shared_y8_flat

theorem a36_shared_nested_eq :
    ∀ z w u : ℂ, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => ((1 + Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (1 : ℂ)) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun k l : Fin 8 => (Matrix.of fun i j : Fin 2 × Fin 4 => (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) i.1 j.2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) i.1 i.2 j.2) ((@finProdFinEquiv 2 4).symm k) ((@finProdFinEquiv 2 4).symm l)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) := by
  intro z w u
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [Matrix.of_apply, Equiv.symm_apply_apply]
  fin_cases a <;> fin_cases c <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod] <;> (try split_ifs) <;> ring_nf <;> (try simp only [Complex.I_sq]) <;> (try ring)
#print axioms a36_shared_nested_eq

theorem a36_shared_line_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))))
    ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G ∧ featureVec G = x} := by
  intro Γ₀ hΓ₀ z w u hz hw hu
  have hX := a36_shared_xo_flat
  have hY := a36_shared_y8_flat Γ₀ hΓ₀ z w u hz hw hu
  have hD : ∀ (c : Fin 2) (b : Fin 8), ‖(fun (_ : Fin 2) (_ : Fin 8) => (1 : ℂ)) c b‖ = 1 := fun c b => by simp
  have hid := a36_shared_nested_eq z w u
  have hh := a36_shared_hull28_core Γ₀ hΓ₀ (Matrix.of fun a c : Fin 2 => ((1 + Complex.I) / 2) * !![1, 1; 1, -1] a c) (fun c : Fin 2 => Matrix.of fun k l : Fin 8 => (Matrix.of fun i j : Fin 2 × Fin 4 => (Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c) i.1 j.1 * (fun (a : Fin 2) (d : Fin 4) => if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ)) i.1 j.2 * (fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) b d) i.1 i.2 j.2) ((@finProdFinEquiv 2 4).symm k) ((@finProdFinEquiv 2 4).symm l)) (fun (_ : Fin 2) (_ : Fin 8) => (1 : ℂ)) hX hY hD
  refine ⟨⟨_, _, _, hX, hY, hD, hid⟩, ?_, ?_⟩
  · rw [hid]; exact hh.2.2
  · rw [hid]; exact ⟨_, hh.2.2, rfl⟩
#print axioms a36_shared_line_core

theorem a36_shared_p_val :
    (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) (0, 0) (0, 0) (1, 0) * (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) (0, 1) (1, 0) (0, 0) = (3599 / 3601 + (120 / 3601) * Complex.I) / 256 := by
  simp (config := { decide := true }) [Matrix.of_apply, Complex.star_def, Complex.ext_iff] <;> norm_num
#print axioms a36_shared_p_val

theorem a36_shared_p_notin :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
  intro Γ₀ hΓ₀ hS
  obtain ⟨X, Y, hX, hY, hxy⟩ := hS
  have hq := (a34_shared_feature_ext _ _).1 hxy ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
  have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY 0 0 1 0 1 0
  have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY 0 1 0 0
  have hL : mixedTriple (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)))) = 1 / 4096 := by
    simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢
    rw [hc, hd]
    norm_num
  rw [hL] at hq
  simp (config := { decide := true }) [mixedTriple, Matrix.of_apply, Complex.star_def, Complex.ext_iff, map_add, map_mul, map_div₀, map_ofNat, map_neg, map_one] at hq <;> norm_num at hq
#print axioms a36_shared_p_notin

theorem a36_shared_point_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → star (3599 / 3601 + (120 / 3601) * Complex.I) * (3599 / 3601 + (120 / 3601) * Complex.I) = 1 ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G ∧ featureVec G = x} ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}
  ∧ (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) (0, 0) (0, 0) (1, 0) * (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * (3599 / 3601 + (120 / 3601) * Complex.I) ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) i k) (0, 1) (1, 0) (0, 0) = (3599 / 3601 + (120 / 3601) * Complex.I) / 256 := by
  intro Γ₀ hΓ₀
  have hl := a36_shared_line_core Γ₀ hΓ₀ _ _ _ a36_shared_z_unit a36_shared_w_unit a36_shared_u60_unit
  exact ⟨a36_shared_u60_unit, hl.2.1, hl.2.2, a36_shared_p_notin Γ₀ hΓ₀, a36_shared_p_val⟩
#print axioms a36_shared_point_core

theorem a36_shared_one_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
  intro Γ₀ hΓ₀
  refine ⟨?_, ?_⟩
  · ext i j
    simp only [Matrix.of_apply, one_pow, mul_one]
  · refine ⟨FibreGram (0 : Fin 1) (Matrix.of fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] p.1 q.1), FibreGram (0 : Fin 1) (Matrix.of fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] p.1 q.1), sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ _ a36_shared_z_unit), sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ _ a36_shared_w_unit), ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [fibreGram_apply, fibreGram_apply, Fin.sum_univ_one, Fin.sum_univ_one]
    simp only [Matrix.of_apply, star_mul]
    ring
#print axioms a36_shared_one_core

theorem a36_shared_hull_g :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro α β _ _ _ _ eR eC X Y D hX hY hD
  exact a36_shared_hullg_core Γ₀ hΓ₀ eR eC X Y D hX hY hD
#print axioms a36_shared_hull_g

theorem a36_shared_hull_gt :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro α β _ _ _ _ eR eC X Y E hX hY hE
  exact a36_shared_hullgt_core Γ₀ hΓ₀ eR eC X Y E hX hY hE
#print axioms a36_shared_hull_gt

theorem a36_control_hull28 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita28 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita28 X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita28 X Y D)) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro X Y D hX hY hD
  exact a36_shared_hull28_core Γ₀ hΓ₀ X Y D hX hY hD
#print axioms a36_control_hull28

theorem a36_control_hull82 :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita82 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita82 X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita82 X Y D)) := by
  intro Γ₀ hΓ₀
  dsimp only
  intro X Y D hX hY hD
  exact a36_shared_hull82_core Γ₀ hΓ₀ X Y D hX hY hD
#print axioms a36_control_hull82

theorem a36_shared_line :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u hu
  exact a36_shared_line_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu
#print axioms a36_shared_line

theorem a36_shared_point :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256 := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a36_shared_point_core Γ₀ hΓ₀
#print axioms a36_shared_point

theorem a36_control_stratum :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  Pu 1 = SIG ∧ featureVec (gram SIG) ∈ S := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a36_shared_one_core Γ₀ hΓ₀
#print axioms a36_control_stratum

theorem a36_hierarchy :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)))
  ∧ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)))
  ∧ (∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N)
  ∧ (star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256) := by
  intro Γ₀ hΓ₀
  dsimp only
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro α β _ _ _ _ eR eC X Y D hX hY hD
    exact a36_shared_hullg_core Γ₀ hΓ₀ eR eC X Y D hX hY hD
  · intro α β _ _ _ _ eR eC X Y E hX hY hE
    exact a36_shared_hullgt_core Γ₀ hΓ₀ eR eC X Y E hX hY hE
  · intro u hu
    exact a36_shared_line_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu
  · exact a36_shared_point_core Γ₀ hΓ₀
#print axioms a36_hierarchy

theorem a36_c_exclusive :
    (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ¬ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)))
  ∨ ¬ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N)
  ∨ ¬ (star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256)) → ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)))
  ∧ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)))
  ∧ (∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N)
  ∧ (star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256)) := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with h | h | h | h
  · exact h r.1
  · exact h r.2.1
  · exact h r.2.2.1
  · exact h r.2.2.2
#print axioms a36_c_exclusive
end DitaHierarchy
end OIBridge
