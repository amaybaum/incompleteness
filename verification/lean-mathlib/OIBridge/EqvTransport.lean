/-
  OIBridge/EqvTransport.lean — design module of the research thread `research/equivalence` (node E17).
  Not adopted, not certified, not a round: the transport form of H-DYN (NOTES-E14, reading (R-01);
  R-E14.2) as a predicate on the kernel's `QuasilocalSystem`, the passage to a `ReversibleDynamics`
  stated as a proposition (not proved), the positive control that every Target A system satisfies the
  predicate, and the finite-stage case proved at the matrix level of one stage.

  §A  Matrix units and `{0,1}` matrices of a finite configuration set: `unitM`, `IsZeroOne`, the unit
      algebra (`unitM_mul`, `unitM_conjTranspose`, the sandwich `sandwich_apply`) and the unit
      decomposition `matrix_eq_sum_unitM`.
  §B  The two lemmas of the finite stage: (a) a self-adjoint idempotent `{0,1}` matrix is diagonal
      (`offDiag_eq_zero_of_zeroOne`); (b) a `{0,1}` matrix `V` with `Vᴴ V` idempotent has at most one
      `1` in each column (`col_unique_of_zeroOne`).
  §C  (c) The finite-stage case: a star-algebra automorphism of `Matrix C C ℂ` that maps every matrix
      unit to a `{0,1}` matrix is the transport along a permutation `g` of `C`
      (`finiteStage_transport`, `finiteStage_transport_apply`).
  §D  The transport form on the kernel's target class: `TransportHDyn`, the positive control
      `oiSystem_transportHDyn` (every `OISystem` satisfies it, through `transported`), and the
      statement `Passage` (R-E14.2's conclusion in Target A form), which this module does not prove.

  The transport form is a hypothesis here, introduced, not an OI premise. Nothing here proves the
  infinite-volume passage (Gelfand duality, maximal abelianness of the diagonal, finite range from
  locality are not formalized).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuasilocalCharacterization

namespace OIBridge
namespace EqvTransport

open QuasilocalCharacterization QuasilocalAlgebra RegionTower
open scoped Matrix

noncomputable section

/-! ### §A — matrix units and `{0,1}` matrices -/

section Units

variable {C : Type} [DecidableEq C]

/-- The matrix unit `E_ab` of a configuration set. -/
def unitM (a b : C) : Matrix C C ℂ := Matrix.of fun i j => if i = a ∧ j = b then 1 else 0

theorem unitM_apply (a b i j : C) : unitM a b i j = if i = a ∧ j = b then 1 else 0 := rfl

/-- A matrix with every entry `0` or `1`. -/
def IsZeroOne (M : Matrix C C ℂ) : Prop := ∀ i j, M i j = 0 ∨ M i j = 1

theorem unitM_conjTranspose (a b : C) : (unitM a b)ᴴ = unitM b a := by
  ext i j
  rw [Matrix.conjTranspose_apply, unitM_apply, unitM_apply]
  by_cases h1 : j = a <;> by_cases h2 : i = b <;> simp [h1, h2]

variable [Fintype C]

theorem unitM_mul_apply (a b : C) (M : Matrix C C ℂ) (d e : C) :
    (unitM a b * M) d e = if d = a then M b e else 0 := by
  rw [Matrix.mul_apply]
  by_cases hd : d = a
  · rw [if_pos hd, Finset.sum_eq_single b]
    · rw [unitM_apply, if_pos ⟨hd, rfl⟩, one_mul]
    · intro k _ hk
      rw [unitM_apply, if_neg (fun h => hk h.2), zero_mul]
    · intro h
      exact absurd (Finset.mem_univ b) h
  · rw [if_neg hd]
    apply Finset.sum_eq_zero
    intro k _
    rw [unitM_apply, if_neg (fun h => hd h.1), zero_mul]

theorem mul_unitM_apply (M : Matrix C C ℂ) (a b d e : C) :
    (M * unitM a b) d e = if e = b then M d a else 0 := by
  rw [Matrix.mul_apply]
  by_cases he : e = b
  · rw [if_pos he, Finset.sum_eq_single a]
    · rw [unitM_apply, if_pos ⟨rfl, he⟩, mul_one]
    · intro k _ hk
      rw [unitM_apply, if_neg (fun h => hk h.1), mul_zero]
    · intro h
      exact absurd (Finset.mem_univ a) h
  · rw [if_neg he]
    apply Finset.sum_eq_zero
    intro k _
    rw [unitM_apply, if_neg (fun h => he h.2), mul_zero]

/-- The product of two matrix units. -/
theorem unitM_mul (a b c d : C) :
    unitM a b * unitM c d = if b = c then unitM a d else 0 := by
  ext i j
  rw [unitM_mul_apply]
  by_cases hbc : b = c
  · rw [if_pos hbc, hbc]
    by_cases hi : i = a <;> by_cases hj : j = d <;> simp [unitM_apply, hi, hj]
  · rw [if_neg hbc, Matrix.zero_apply]
    by_cases hi : i = a <;> simp [unitM_apply, hi, hbc]

/-- The sandwich of a matrix between two diagonal units. -/
theorem sandwich_apply (a b : C) (M : Matrix C C ℂ) (d e : C) :
    (unitM a a * M * unitM b b) d e = if d = a ∧ e = b then M a b else 0 := by
  rw [mul_unitM_apply, unitM_mul_apply]
  by_cases he : e = b <;> by_cases hd : d = a <;> simp [he, hd]

/-- Every matrix is the sum of its entries times the matrix units. -/
theorem matrix_eq_sum_unitM (X : Matrix C C ℂ) : X = ∑ c, ∑ c', X c c' • unitM c c' := by
  ext d e
  rw [Matrix.sum_apply, Finset.sum_eq_single d]
  · rw [Matrix.sum_apply, Finset.sum_eq_single e]
    · rw [Matrix.smul_apply, unitM_apply, if_pos ⟨rfl, rfl⟩, smul_eq_mul, mul_one]
    · intro c' _ hc'
      rw [Matrix.smul_apply, unitM_apply, if_neg (fun h => hc' h.2.symm), smul_zero]
    · intro h
      exact absurd (Finset.mem_univ e) h
  · intro c _ hc
    rw [Matrix.sum_apply]
    apply Finset.sum_eq_zero
    intro c' _
    rw [Matrix.smul_apply, unitM_apply, if_neg (fun h => hc h.1.symm), smul_zero]
  · intro h
    exact absurd (Finset.mem_univ d) h

/-- A sum of one column's entries of a matrix unit over any set of rows is `0` or `1`. -/
theorem sum_unitM_zeroOne (s : Finset C) (c c' k : C) :
    (∑ f ∈ s, unitM c c' f k) = 0 ∨ (∑ f ∈ s, unitM c c' f k) = 1 := by
  by_cases hk : k = c'
  · by_cases hc : c ∈ s
    · right
      rw [Finset.sum_eq_single c]
      · rw [unitM_apply, if_pos ⟨rfl, hk⟩]
      · intro f _ hfc
        rw [unitM_apply, if_neg (fun h => hfc h.1)]
      · intro hcs
        exact absurd hc hcs
    · left
      apply Finset.sum_eq_zero
      intro f hf
      have hfc : f ≠ c := fun hfc' => hc (hfc' ▸ hf)
      rw [unitM_apply, if_neg (fun h => hfc h.1)]
  · left
    apply Finset.sum_eq_zero
    intro f _
    rw [unitM_apply, if_neg (fun h => hk h.2)]

end Units

/-! ### §B — the two lemmas of the finite stage -/

section Lemmas

variable {C : Type} [Fintype C] [DecidableEq C]

/-- **(a)** A self-adjoint idempotent `{0,1}` matrix is diagonal: `P_ii = (P²)_ii = Σ_k P_ik` forces
the off-diagonal entries of each row to vanish. -/
theorem offDiag_eq_zero_of_zeroOne {P : Matrix C C ℂ} (h01 : IsZeroOne P) (hsa : Pᴴ = P)
    (hid : P * P = P) : ∀ i k, i ≠ k → P i k = 0 := by
  intro i k hik
  have hsymm : ∀ j, P j i = P i j := by
    intro j
    have h1 : star (P i j) = P j i := by
      have h := congrFun (congrFun hsa j) i
      rwa [Matrix.conjTranspose_apply] at h
    rcases h01 i j with h | h
    · rw [h, star_zero] at h1
      rw [h, ← h1]
    · rw [h, star_one] at h1
      rw [h, ← h1]
  have hsq : ∀ j, P i j * P j i = P i j := by
    intro j
    rw [hsymm j]
    rcases h01 i j with h | h <;> rw [h] <;> norm_num
  have hrow : ∑ j, P i j = P i i := by
    have h := congrFun (congrFun hid i) i
    rw [Matrix.mul_apply] at h
    simp only [hsq] at h
    exact h
  have hsplit : ∑ j ∈ Finset.univ.erase i, P i j = 0 := by
    have h := Finset.add_sum_erase Finset.univ (P i) (Finset.mem_univ i)
    rw [hrow] at h
    linear_combination h
  have hre : ∑ j ∈ Finset.univ.erase i, (P i j).re = 0 := by
    have h := congrArg Complex.re hsplit
    rwa [Complex.re_sum, Complex.zero_re] at h
  have hnn : ∀ j ∈ Finset.univ.erase i, 0 ≤ (P i j).re := by
    intro j _
    rcases h01 i j with h | h <;> rw [h] <;> simp
  have hzero : (P i k).re = 0 := (Finset.sum_eq_zero_iff_of_nonneg hnn).mp hre k
    (Finset.mem_erase.mpr ⟨Ne.symm hik, Finset.mem_univ k⟩)
  rcases h01 i k with h | h
  · exact h
  · rw [h] at hzero
    simp at hzero

/-- **(b)** A `{0,1}` matrix `V` with `Vᴴ V` idempotent has at most one `1` in each column: the
diagonal entry of `Vᴴ V` counts the ones of the column and is at most `1`. -/
theorem col_unique_of_zeroOne {V : Matrix C C ℂ} (h01 : IsZeroOne V)
    (hid : (Vᴴ * V) * (Vᴴ * V) = Vᴴ * V) (j : C) {i i' : C} (hi : V i j = 1)
    (hi' : V i' j = 1) : i = i' := by
  by_contra hne
  have hstar : ∀ a b, star (V a b) * V a b = V a b := by
    intro a b
    rcases h01 a b with h | h <;> rw [h] <;> simp
  have hGh : (Vᴴ * V)ᴴ = Vᴴ * V := by
    rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
  have hGsa : ∀ a b, (Vᴴ * V) b a = star ((Vᴴ * V) a b) := by
    intro a b
    have h := congrFun (congrFun hGh b) a
    rw [Matrix.conjTranspose_apply] at h
    exact h.symm
  have hGjj : (Vᴴ * V) j j = ∑ a, V a j := by
    rw [Matrix.mul_apply]
    exact Finset.sum_congr rfl fun a _ => by rw [Matrix.conjTranspose_apply, hstar]
  have hidjj : (Vᴴ * V) j j = ∑ k, (Vᴴ * V) j k * star ((Vᴴ * V) j k) := by
    have h : ∑ k, (Vᴴ * V) j k * (Vᴴ * V) k j = (Vᴴ * V) j j := by
      rw [← Matrix.mul_apply, hid]
    rw [← h]
    exact Finset.sum_congr rfl fun k _ => by rw [hGsa j k]
  have hnormSq : ∀ z : ℂ, (z * star z).re = Complex.normSq z := by
    intro z
    first
      | (rw [Complex.normSq_apply, Complex.mul_re, Complex.star_def, Complex.conj_re,
          Complex.conj_im]; ring)
      | (rw [Complex.star_def, Complex.mul_conj, Complex.ofReal_re]; done)
      | (simp [Complex.normSq_apply, Complex.mul_re]; done)
      | (simp [Complex.normSq_apply, Complex.mul_re]; ring)
  have hre : ((Vᴴ * V) j j).re = ∑ k, Complex.normSq ((Vᴴ * V) j k) := by
    rw [hidjj, Complex.re_sum]
    exact Finset.sum_congr rfl fun k _ => hnormSq _
  have h1 : Complex.normSq ((Vᴴ * V) j j) ≤ ((Vᴴ * V) j j).re := by
    rw [hre]
    exact Finset.single_le_sum (f := fun k => Complex.normSq ((Vᴴ * V) j k))
      (fun k _ => Complex.normSq_nonneg _) (Finset.mem_univ j)
  have h2 : ((Vᴴ * V) j j).re ^ 2 ≤ Complex.normSq ((Vᴴ * V) j j) := by
    rw [Complex.normSq_apply]
    nlinarith [sq_nonneg ((Vᴴ * V) j j).im]
  have hnn : ∀ a, 0 ≤ (V a j).re := by
    intro a
    rcases h01 a j with h | h <;> rw [h] <;> simp
  have h3 : (2 : ℝ) ≤ ((Vᴴ * V) j j).re := by
    rw [hGjj, Complex.re_sum]
    have hsub : ({i, i'} : Finset C) ⊆ Finset.univ := Finset.subset_univ _
    have h := Finset.sum_le_sum_of_subset_of_nonneg hsub (fun a _ _ => hnn a)
    simp only [Finset.sum_pair hne, hi, hi', Complex.one_re] at h
    linarith
  nlinarith [h1, h2, h3]

end Lemmas

/-! ### §C — (c), the finite-stage case -/

section FiniteStage

variable {C : Type} [Fintype C] [DecidableEq C]

/-- **(c) The finite-stage case.** A star-algebra automorphism of the matrix algebra of a finite
configuration set that maps every matrix unit to a `{0,1}` matrix is the transport along a
permutation of the configurations: `α (E_cc') = E_{g c, g c'}`. -/
theorem finiteStage_transport (α : Matrix C C ℂ ≃⋆ₐ[ℂ] Matrix C C ℂ)
    (h01 : ∀ c c', IsZeroOne (α (unitM c c'))) :
    ∃ g : C ≃ C, ∀ c c', α (unitM c c') = unitM (g c) (g c') := by
  -- the images of the diagonal units are self-adjoint idempotent `{0,1}` matrices
  have hsa : ∀ c, (α (unitM c c))ᴴ = α (unitM c c) := by
    intro c
    rw [← Matrix.star_eq_conjTranspose, ← map_star α (unitM c c), Matrix.star_eq_conjTranspose,
      unitM_conjTranspose]
  have hidem : ∀ c, α (unitM c c) * α (unitM c c) = α (unitM c c) := by
    intro c
    rw [← map_mul α, unitM_mul, if_pos rfl]
  have hdiag : ∀ c d e, d ≠ e → α (unitM c c) d e = 0 := fun c =>
    offDiag_eq_zero_of_zeroOne (h01 c c) (hsa c) (hidem c)
  -- each has a diagonal entry equal to one
  have hne : ∀ c, ∃ d, α (unitM c c) d d = 1 := by
    intro c
    by_contra hcon
    push_neg at hcon
    have hzero : α (unitM c c) = 0 := by
      ext d e
      rw [Matrix.zero_apply]
      by_cases hde : d = e
      · rw [← hde]
        rcases h01 c c d d with h | h
        · exact h
        · exact absurd h (hcon d)
      · exact hdiag c d e hde
    have h0 : unitM c c = (0 : Matrix C C ℂ) := by
      apply EquivLike.injective α
      rw [hzero, map_zero]
    have h1 := congrFun (congrFun h0 c) c
    simp [unitM_apply] at h1
  -- their supports are pairwise disjoint
  have hdisj : ∀ c c' d, α (unitM c c) d d = 1 → α (unitM c' c') d d = 1 → c = c' := by
    intro c c' d h1 h2
    by_contra hcc
    have hprod : α (unitM c c) * α (unitM c' c') = 0 := by
      rw [← map_mul α, unitM_mul, if_neg hcc, map_zero]
    have hdd := congrFun (congrFun hprod d) d
    rw [Matrix.mul_apply, Matrix.zero_apply, Finset.sum_eq_single d] at hdd
    · rw [h1, h2] at hdd
      norm_num at hdd
    · intro k _ hk
      rw [hdiag c d k (Ne.symm hk), zero_mul]
    · intro h
      exact absurd (Finset.mem_univ d) h
  -- a choice of one support point per configuration is a permutation
  choose s hs using hne
  have hinj : Function.Injective s := by
    intro c c' hcc
    exact hdisj c c' (s c) (hs c) (by rw [hcc]; exact hs c')
  have hsurj : Function.Surjective s := by
    first
      | exact Finite.surjective_of_injective hinj
      | exact Finite.injective_iff_surjective.mp hinj
  have hsupp : ∀ c d, α (unitM c c) d d = 1 → d = s c := by
    intro c d hd
    obtain ⟨c₀, rfl⟩ := hsurj d
    have hc := hdisj c c₀ (s c₀) hd (hs c₀)
    rw [hc]
  -- the diagonal units go to the diagonal units of the permuted configurations
  have hdiagUnit : ∀ c, α (unitM c c) = unitM (s c) (s c) := by
    intro c
    ext d e
    rw [unitM_apply]
    by_cases hde : d = e
    · rw [← hde]
      by_cases hd : d = s c
      · rw [if_pos ⟨hd, hd⟩, hd]
        exact hs c
      · rw [if_neg (fun h => hd h.1)]
        rcases h01 c c d d with h | h
        · exact h
        · exact absurd (hsupp c d h) hd
    · rw [if_neg (show ¬(d = s c ∧ e = s c) from fun h => hde (h.1.trans h.2.symm))]
      exact hdiag c d e hde
  -- and every unit goes to the unit of the permuted configurations
  have hunit : ∀ c c', α (unitM c c') = unitM (s c) (s c') := by
    intro c c'
    have hsand : α (unitM c c') = unitM (s c) (s c) * α (unitM c c') * unitM (s c') (s c') := by
      rw [← hdiagUnit c, ← hdiagUnit c', ← map_mul α, ← map_mul α, unitM_mul, if_pos rfl,
        unitM_mul, if_pos rfl]
    have hentry : ∀ d e, α (unitM c c') d e =
        if d = s c ∧ e = s c' then α (unitM c c') (s c) (s c') else 0 := by
      intro d e
      have h := congrFun (congrFun hsand d) e
      rw [sandwich_apply] at h
      exact h
    have hv : α (unitM c c') (s c) (s c') = 1 := by
      rcases h01 c c' (s c) (s c') with h | h
      · exfalso
        have hz : α (unitM c c') = 0 := by
          ext d e
          rw [hentry d e, h, Matrix.zero_apply]
          split_ifs <;> rfl
        have h0 : unitM c c' = (0 : Matrix C C ℂ) := by
          apply EquivLike.injective α
          rw [hz, map_zero]
        have h1 := congrFun (congrFun h0 c) c'
        simp [unitM_apply] at h1
      · exact h
    ext d e
    rw [hentry d e, hv, unitM_apply]
  exact ⟨Equiv.ofBijective s ⟨hinj, hsurj⟩, fun c c' => hunit c c'⟩

/-- The transport along the permutation, on every matrix: `α X = X ∘ (g⁻¹ × g⁻¹)`. -/
theorem finiteStage_transport_apply (α : Matrix C C ℂ ≃⋆ₐ[ℂ] Matrix C C ℂ) (g : C ≃ C)
    (hg : ∀ c c', α (unitM c c') = unitM (g c) (g c')) (X : Matrix C C ℂ) :
    α X = X.submatrix g.symm g.symm := by
  have hX : α X = ∑ c, ∑ c', X c c' • unitM (g c) (g c') := by
    conv_lhs => rw [matrix_eq_sum_unitM X]
    first
      | (simp only [map_sum, map_smul, hg]; done)
      | (simp only [map_sum, StarAlgEquiv.map_smul, hg]; done)
      | (simp [map_sum, hg]; done)
  rw [hX]
  ext d e
  rw [Matrix.submatrix_apply, Matrix.sum_apply, Finset.sum_eq_single (g.symm d)]
  · rw [Matrix.sum_apply, Finset.sum_eq_single (g.symm e)]
    · rw [Matrix.smul_apply, unitM_apply, Equiv.apply_symm_apply, Equiv.apply_symm_apply,
        if_pos ⟨rfl, rfl⟩, smul_eq_mul, mul_one]
    · intro c' _ hc'
      rw [Matrix.smul_apply, unitM_apply, if_neg, smul_zero]
      rintro ⟨_, h⟩
      exact hc' (by rw [h, Equiv.symm_apply_apply])
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro c _ hc
    rw [Matrix.sum_apply]
    apply Finset.sum_eq_zero
    intro c' _
    rw [Matrix.smul_apply, unitM_apply, if_neg, smul_zero]
    rintro ⟨h, _⟩
    exact hc (by rw [h, Equiv.symm_apply_apply])
  · intro h
    exact absurd (Finset.mem_univ _) h

end FiniteStage

/-! ### §D — the transport form on the kernel's target class -/

section Target

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **The transport form of H-DYN** (NOTES-E14, reading (R-01)): every matrix unit of every finite
stage is carried to a `{0,1}` matrix of some finite stage. -/
def TransportHDyn (S : QuasilocalSystem ι Q) (α : S.A ≃⋆ₐ[ℂ] S.A) : Prop :=
  ∀ (Λ : Finset ι) (c c' : Conf Λ Q), ∃ (Λ' : Finset ι) (M : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ),
    IsZeroOne M ∧ α (S.st Λ (unitM c c')) = S.st Λ' M

/-- The transported matrix of a matrix unit has entries `0` and `1`. -/
theorem isZeroOne_transported (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) (c c' : Conf Λ Q) :
    IsZeroOne (transported Φ Λ (unitM c c')) := by
  intro g h
  first
    | exact sum_unitM_zeroOne _ c c' _
    | (unfold transported; exact sum_unitM_zeroOne _ c c' _)
    | (simp only [transported]; exact sum_unitM_zeroOne _ c c' _)

/-- **Positive control**: every Target A system satisfies the transport form. -/
theorem oiSystem_transportHDyn (T : OISystem ι Q) : TransportHDyn T.toQuasilocalSystem T.α :=
  fun Λ c c' => ⟨hat T.Φ Λ, transported T.Φ Λ (unitM c c'), isZeroOne_transported T.Φ Λ c c',
    T.α_stage Λ (unitM c c')⟩

end Target

/-- **The passage, stated (not proved here)**: a star automorphism in transport form that preserves
locality with its inverse is the Target A automorphism of a reversible finite-range dynamics. Its
status is R-E14.2's: a written proof, not a kernel theorem. -/
def Passage (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] : Prop :=
  ∀ (S : QuasilocalSystem ι Q) (α : S.A ≃⋆ₐ[ℂ] S.A), TransportHDyn S α →
    LocalityPreserving S α → LocalityPreserving S α.symm →
    ∃ Φ : ReversibleDynamics ι Q, ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      α (S.st Λ X) = S.st (hat Φ Λ) (transported Φ Λ X)

end

end EqvTransport
end OIBridge

#print axioms OIBridge.EqvTransport.unitM_mul
#print axioms OIBridge.EqvTransport.sandwich_apply
#print axioms OIBridge.EqvTransport.matrix_eq_sum_unitM
#print axioms OIBridge.EqvTransport.offDiag_eq_zero_of_zeroOne
#print axioms OIBridge.EqvTransport.col_unique_of_zeroOne
#print axioms OIBridge.EqvTransport.finiteStage_transport
#print axioms OIBridge.EqvTransport.finiteStage_transport_apply
#print axioms OIBridge.EqvTransport.isZeroOne_transported
#print axioms OIBridge.EqvTransport.oiSystem_transportHDyn
