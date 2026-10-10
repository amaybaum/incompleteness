import OIBridge.ProductStratum

/-!
# Act 35 — the Diţă hulls of the product-embedded stratum

At act 29's product configuration (`V = Fin 4 × Fin 4`, the ancilla `Fin 1 × Fin 1`, `Γ ≡ 1/16`), this
module studies the two twisted-tensor families through act 34's stratum: the column construction
`X[a,c] · D[c,b] · Y_c[b,d]` and the row construction `X[a,c] · E[a,d] · Y_a[b,d]`, each realizable
for every choice of flat unitary factors and unit twist phases, each containing the stratum, and
each preserved by the product relabellings and the conjugation, the transpose exchanging them. Act
34's properness witness is a point of the column hull; the identity every product tuple satisfies
on its same-row-block, same-column-in-block cross ratios is what it violates. A non-product
relabelling carries a stratum point off the stratum inside its isometry class. The twist phases
enter the feature vector injectively modulo the two gauges, so the hull through one point is
infinite and no finite set of maps applied to a finite set reaches it.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaHull

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum

theorem a35_shared_star_mul :
    ∀ z : ℂ, star z * z = ((‖z‖ ^ 2 : ℝ) : ℂ) := by
  intro z
  rw [mul_comm, RCLike.star_def, Complex.mul_conj]
  norm_cast
  exact Complex.normSq_eq_norm_sq _
#print axioms a35_shared_star_mul
theorem a35_shared_unit_of_norm :
    ∀ z : ℂ, ‖z‖ = 1 → star z * z = 1 := by
  intro z h
  rw [a35_shared_star_mul, h]
  norm_num
#print axioms a35_shared_unit_of_norm
theorem a35_shared_norm_of_unit :
    ∀ z : ℂ, star z * z = 1 → ‖z‖ = 1 := by
  intro z h
  have h2 : ‖z‖ ^ 2 = 1 := by
    have := a35_shared_star_mul z
    rw [h] at this
    exact_mod_cast this.symm
  have h0 : 0 ≤ ‖z‖ := norm_nonneg z
  have h3 : (‖z‖ - 1) * (‖z‖ + 1) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h3 with h4 | h4
  · linarith
  · linarith
#print axioms a35_shared_norm_of_unit
theorem a35_shared_ne_zero :
    ∀ (z : ℂ) (r : ℝ), 0 < r → ‖z‖ = r → z ≠ 0 := by
  intro z r hr h hz
  rw [hz, norm_zero] at h
  linarith
#print axioms a35_shared_ne_zero
theorem a35_shared_half :
    ∀ z : ℂ, star z * z = 1 → ∀ a c : Fin 4, ‖((1 / 2 : ℂ) * ![![1, 1, 1, 1], ![1, z, -1, -z], ![1, -1, 1, -1], ![1, -z, -1, z]] a c)‖ = 1 / 2 := by
  intro z hz a c
  have h1 : ‖z‖ = 1 := a35_shared_norm_of_unit z hz
  have h12 : ‖(1 / 2 : ℂ)‖ = 1 / 2 := by
    rw [show (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) by push_cast; ring, Complex.norm_real]
    norm_num
  rw [norm_mul, h12]
  fin_cases a <;> fin_cases c <;> simp [h1]
#print axioms a35_shared_half
theorem a35_shared_f4_flat :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ z : ℂ, star z * z = 1 → ((Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a₀ c₀) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a₀ c₀) a₁ c₁‖ = 1 / 2) := by
  intro Γ₀ hΓ₀ z hz
  refine ⟨?_, ?_⟩
  · have h := vpart_unitary (hadamard_z_admissible Γ₀ hΓ₀ z hz).1
    have e : (Matrix.of fun i j : Fin 4 => (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) (i, 0) (j, 0)) = (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a₀ c₀) := by
      ext a c
      simp only [Matrix.of_apply]
    rw [e] at h
    exact h
  · intro a c
    show ‖(1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c‖ = 1 / 2
    exact a35_shared_half z hz a c
#print axioms a35_shared_f4_flat
theorem a35_shared_dita_unitary :
    ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), X ∈ Matrix.unitaryGroup (Fin 4) ℂ → (∀ c, Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ) → (∀ c b, ‖D c b‖ = 1) → (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
  intro X Y D hX hY hD
  rw [Matrix.mem_unitaryGroup_iff]
  have hX' := Matrix.mem_unitaryGroup_iff.1 hX
  have hY' := fun c => Matrix.mem_unitaryGroup_iff.1 (hY c)
  have hDD : ∀ c b, D c b * star (D c b) = 1 := fun c b => by
    rw [mul_comm]; exact a35_shared_unit_of_norm _ (hD c b)
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  rw [Fintype.sum_prod_type]
  have key : ∀ c : Fin 4, ∑ d : Fin 4, X i.1 c * D c i.2 * Y c i.2 d * star (X i'.1 c * D c i'.2 * Y c i'.2 d)
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
#print axioms a35_shared_dita_unitary
theorem a35_shared_dita_norm :
    ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (∀ a c : Fin 4, ‖X a c‖ = 1 / 2) → (∀ c, ∀ a d : Fin 4, ‖Y c a d‖ = 1 / 2) → (∀ c b, ‖D c b‖ = 1) → ∀ i j : Fin 4 × Fin 4, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j‖ = 1 / 4 := by
  intro X Y D hX hY hD i j
  show ‖X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2‖ = 1 / 4
  rw [norm_mul, norm_mul, hX, hD, hY]
  norm_num
#print axioms a35_shared_dita_norm
theorem a35_shared_pad_unitary :
    ∀ H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) ∈ Matrix.unitaryGroup ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ := by
  intro H hH
  have hsum : ∀ f : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) → ℂ, ∑ x, f x = ∑ r : Fin 4 × Fin 4, f (r, ((0 : Fin 1), (0 : Fin 1))) := by
    intro f
    rw [Fintype.sum_prod_type]
    exact Finset.sum_congr rfl (fun r _ => by rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one])
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at hH ⊢
  ext ⟨p, a⟩ ⟨q, b⟩
  have hab : a = b := Subsingleton.elim a b
  subst hab
  have hpq := congrFun (congrFun hH p) q
  rw [Matrix.mul_apply, Matrix.one_apply] at hpq
  simp only [Matrix.conjTranspose_apply] at hpq
  rw [Matrix.mul_apply, Matrix.one_apply, hsum]
  simp only [Matrix.conjTranspose_apply, Matrix.of_apply, Prod.mk.injEq, and_true]
  exact hpq
#print axioms a35_shared_pad_unitary
theorem a35_shared_gram_realizable :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖H i j‖ = 1 / 4) → RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((H) i j) * (H) i k) := by
  intro Γ₀ hΓ₀ H hH hn
  have hsum1 : ∀ f : Fin 1 × Fin 1 → ℝ, ∑ a, f a = f ((0 : Fin 1), (0 : Fin 1)) := by
    intro f
    rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
  have hU : AdmissibleDilationAt (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) := by
    refine ⟨a35_shared_pad_unitary H hH, ?_⟩
    intro i j
    rw [hsum1, hΓ₀]
    simp only [Matrix.of_apply, hn]
    norm_num
  have hG : FibreGram ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((H) i j) * (H) i k := by
    funext i
    ext j k
    rw [fibreGram_apply, Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
    simp only [Matrix.of_apply]
  rw [← hG]
  exact sh1_necessity hU
#print axioms a35_shared_gram_realizable
theorem a35_shared_hull_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) → (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) → (∀ c b, ‖D c b‖ = 1) → (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) := by
  intro Γ₀ hΓ₀ X Y D hX hY hD
  have hu := a35_shared_dita_unitary X Y D hX.1 (fun c => (hY c).1) hD
  have hn := a35_shared_dita_norm X Y D hX.2 (fun c => (hY c).2) hD
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩
#print axioms a35_shared_hull_core
theorem a35_shared_ditaT_eq :
    ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) = (Matrix.of fun i j : Fin 4 × Fin 4 => Xᵀ i.1 j.1 * E j.1 i.2 * (fun a => (Y a)ᵀ) j.1 i.2 j.2)ᵀ := by
  intro X Y E
  ext i j
  simp only [Matrix.transpose_apply, Matrix.of_apply]
#print axioms a35_shared_ditaT_eq
theorem a35_shared_hull_t_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) → (∀ a, ((Y a) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y a) a₁ c₁‖ = 1 / 2)) → (∀ a d, ‖E a d‖ = 1) → (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i k) := by
  intro Γ₀ hΓ₀ X Y E hX hY hE
  have hXt : Xᵀ ∈ Matrix.unitaryGroup (Fin 4) ℂ := transpose_unitary hX.1
  have hYt : ∀ a, (Y a)ᵀ ∈ Matrix.unitaryGroup (Fin 4) ℂ := fun a => transpose_unitary (hY a).1
  have hu : (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
    rw [a35_shared_ditaT_eq]
    exact transpose_unitary (a35_shared_dita_unitary Xᵀ (fun a => (Y a)ᵀ) E hXt hYt hE)
  have hn : ∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i j‖ = 1 / 4 := by
    intro i j
    show ‖X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2‖ = 1 / 4
    rw [norm_mul, norm_mul, hX.2, hE, (hY _).2]
    norm_num
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩
#print axioms a35_shared_hull_t_core
theorem a35_shared_vpart_flat :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → ((Matrix.of fun a c : Fin 4 => U (a, 0) (c, 0)) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Matrix.of fun a c : Fin 4 => U (a, 0) (c, 0)) a₁ c₁‖ = 1 / 2) := by
  intro Γ₀ hΓ₀ U hU
  refine ⟨vpart_unitary hU.1, ?_⟩
  intro a c
  have h1 := hU.2 a c
  rw [Fin.sum_univ_one, hΓ₀] at h1
  simp only [Matrix.of_apply] at h1 ⊢
  have h0 : 0 ≤ ‖U (a, 0) (c, 0)‖ := norm_nonneg _
  have h2 : (‖U (a, 0) (c, 0)‖ - 1 / 2) * (‖U (a, 0) (c, 0)‖ + 1 / 2) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h2 with h3 | h3
  · linarith
  · linarith
#print axioms a35_shared_vpart_flat
theorem a35_shared_gram_of_dilation :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (X : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), FibreGram (0 : Fin 1) U = X → ∀ a j k : Fin 4, X a j k = star (U (a, 0) (j, 0)) * U (a, 0) (k, 0) := by
  intro Γ₀ hΓ₀ U X hX a j k
  rw [← hX, fibreGram_apply, Fin.sum_univ_one]
#print axioms a35_shared_gram_of_dilation
theorem a35_shared_sigma_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ({x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} ⊆ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x}) ∧ ({x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} ⊆ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ a, ((Y a) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y a) a₁ c₁‖ = 1 / 2)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i k) = x}) := by
  intro Γ₀ hΓ₀
  constructor
  · intro x hx
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx
    obtain ⟨UX, hUX, hFX⟩ := sh1_sufficiency (0 : Fin 1) hX
    obtain ⟨UY, hUY, hFY⟩ := sh1_sufficiency (0 : Fin 1) hY
    refine ⟨Matrix.of fun a c : Fin 4 => UX (a, 0) (c, 0), fun _ => Matrix.of fun a c : Fin 4 => UY (a, 0) (c, 0), fun _ _ => 1, a35_shared_vpart_flat Γ₀ hΓ₀ UX hUX, fun _ => a35_shared_vpart_flat Γ₀ hΓ₀ UY hUY, fun _ _ => by simp, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [a35_shared_gram_of_dilation Γ₀ hΓ₀ UX X hFX i.1 j.1 k.1, a35_shared_gram_of_dilation Γ₀ hΓ₀ UY Y hFY i.2 j.2 k.2]
    simp only [star_mul, mul_one]
    ring
  · intro x hx
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx
    obtain ⟨UX, hUX, hFX⟩ := sh1_sufficiency (0 : Fin 1) hX
    obtain ⟨UY, hUY, hFY⟩ := sh1_sufficiency (0 : Fin 1) hY
    refine ⟨Matrix.of fun a c : Fin 4 => UX (a, 0) (c, 0), fun _ => Matrix.of fun a c : Fin 4 => UY (a, 0) (c, 0), fun _ _ => 1, a35_shared_vpart_flat Γ₀ hΓ₀ UX hUX, fun _ => a35_shared_vpart_flat Γ₀ hΓ₀ UY hUY, fun _ _ => by simp, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [a35_shared_gram_of_dilation Γ₀ hΓ₀ UX X hFX i.1 j.1 k.1, a35_shared_gram_of_dilation Γ₀ hΓ₀ UY Y hFY i.2 j.2 k.2]
    simp only [star_mul, mul_one]
    ring
#print axioms a35_shared_sigma_core
theorem a35_shared_cross_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → ∀ a b b' c c' d : Fin 4, (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) (a, b) (c, d) (c', d) * (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) (a, b') (c', d) (c, d) = 1 / 256 := by
  intro Γ₀ hΓ₀ X Y hX hY a b b' c c' d
  simp only [Matrix.of_apply]
  have hYd : ∀ b, Y b d d = ((1 / 4 : ℝ) : ℂ) := fun b => by rw [hY.2.2.2 b d, hΓ₀]; simp
  have hXh : X a c' c = star (X a c c') := ((a34_shared_hermitian Γ₀ hΓ₀ X hX a).apply c' c).symm
  have h := a35_shared_star_mul (X a c c')
  rw [a34_shared_entry_norm Γ₀ hΓ₀ X hX a c c'] at h
  rw [hYd, hYd, hXh]
  push_cast at h ⊢
  linear_combination (1 / 16 : ℂ) * h
#print axioms a35_shared_cross_core
theorem a35_shared_diag_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → ∀ a b c d : Fin 4, (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) (a, b) (c, d) (c, d) = 1 / 16 := by
  intro Γ₀ hΓ₀ X Y hX hY a b c d
  simp only [Matrix.of_apply]
  rw [hX.2.2.2 a c, hY.2.2.2 b d, hΓ₀]
  simp
  norm_num
#print axioms a35_shared_diag_core
theorem a35_shared_wit_eq :
    (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) = Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun c : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if c.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if c.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if c.val % 2 = 0 then Complex.I else -Complex.I), -1, (if c.val % 2 = 0 then Complex.I else -Complex.I)] a₀ c₀)) j.1 i.2 j.2 := by
  ext i j
  simp only [Matrix.of_apply]
  ring
#print axioms a35_shared_wit_eq
theorem a35_shared_untw_eq :
    (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.2 j.2) = Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2 := by
  ext i j
  simp only [Matrix.of_apply]
  ring
#print axioms a35_shared_untw_eq
theorem a35_shared_wit_rel :
    ∀ i j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i (((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) j) := by
  intro i j
  obtain ⟨a, b⟩ := i
  obtain ⟨c, d⟩ := j
  simp only [Matrix.of_apply, Equiv.trans_apply, Equiv.swap_apply_def]
  fin_cases c <;> fin_cases b <;> fin_cases d <;> simp <;> ring
#print axioms a35_shared_wit_rel
theorem a35_shared_wit_mem :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x} := by
  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  refine ⟨(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀), (fun c : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if c.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if c.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if c.val % 2 = 0 then Complex.I else -Complex.I), -1, (if c.val % 2 = 0 then Complex.I else -Complex.I)] a₀ c₀)), fun _ _ => 1, a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, ?_, fun _ _ => by simp, ?_⟩
  · intro c
    show ((Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if c.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if c.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if c.val % 2 = 0 then Complex.I else -Complex.I), -1, (if c.val % 2 = 0 then Complex.I else -Complex.I)] a₀ c₀) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if c.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if c.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if c.val % 2 = 0 then Complex.I else -Complex.I), -1, (if c.val % 2 = 0 then Complex.I else -Complex.I)] a₀ c₀) a₁ c₁‖ = 1 / 2)
    exact a35_shared_f4_flat Γ₀ hΓ₀ _ (by split_ifs <;> simp)
  · rw [a35_shared_wit_eq]
#print axioms a35_shared_wit_mem
theorem a35_shared_wit_notin :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
  intro Γ₀ hΓ₀ hS
  have h34 := a34_control_proper Γ₀ hΓ₀
  dsimp only at h34
  obtain ⟨X, Y, hX, hY, hxy⟩ := hS
  exact h34.2 X Y hxy
#print axioms a35_shared_wit_notin
theorem a35_shared_wit_val :
    (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) (0, 1) (0, 1) (1, 1) * (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) (0, 0) (1, 1) (0, 1) = -(1 / 256) := by
  simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four] <;> norm_num
#print axioms a35_shared_wit_val
theorem a35_shared_wit_feat :
    featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) = featureVec (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) i).submatrix ((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) ((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4))))) := by
  congr 1
  funext i
  ext j k
  show star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k = star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i (((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) j)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i (((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) k)
  rw [a35_shared_wit_rel i j, a35_shared_wit_rel i k]
#print axioms a35_shared_wit_feat
theorem a35_shared_wit_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) = Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun c : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (if c.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if c.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if c.val % 2 = 0 then Complex.I else -Complex.I), -1, (if c.val % 2 = 0 then Complex.I else -Complex.I)] a₀ c₀)) j.1 i.2 j.2)
  ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x} ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}
  ∧ (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) (0, 1) (0, 1) (1, 1) * (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) (0, 0) (1, 1) (0, 1) = -(1 / 256)
  ∧ (∀ i j, (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i (((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) j))
  ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2) i k) = featureVec (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) i).submatrix ((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))) ((Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4))))) := by
  intro Γ₀ hΓ₀
  exact ⟨a35_shared_wit_eq, a35_shared_wit_mem Γ₀ hΓ₀, a35_shared_wit_notin Γ₀ hΓ₀, a35_shared_wit_val, a35_shared_wit_rel, a35_shared_wit_feat⟩
#print axioms a35_shared_wit_core
theorem a35_shared_twist_notin :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
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
  simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four] at hq <;> norm_num at hq
#print axioms a35_shared_twist_notin
theorem a35_shared_real_notin :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
  intro Γ₀ hΓ₀ hS
  obtain ⟨X, Y, hX, hY, hxy⟩ := hS
  have hq := (a34_shared_feature_ext _ _).1 hxy ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((0 : Fin 4), (3 : Fin 4))), (((0 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
  have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY 0 0 3 0 3 0
  have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY 0 3 0 0
  have hL : mixedTriple (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((0 : Fin 4), (3 : Fin 4))), (((0 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)))) = 1 / 4096 := by
    simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢
    rw [hc, hd]
    norm_num
  rw [hL] at hq
  simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four] at hq <;> norm_num at hq
#print axioms a35_shared_real_notin
theorem a35_shared_twist_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x} ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}
  ∧ ∑ k : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) (0, 0) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) (0, 1) k) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) (0, 2) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) (1, 1) k) = Complex.I / 32 := by
  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  refine ⟨⟨(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀), fun _ => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀), (fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ)), a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, fun _ => a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, ?_, rfl⟩, a35_shared_twist_notin Γ₀ hΓ₀, ?_⟩
  · intro c b
    by_cases hc : c = 1
    · simp only [hc, if_true]
      fin_cases b <;> simp
    · simp [hc]
  · simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four]
    norm_num
#print axioms a35_shared_twist_core
theorem a35_shared_real_im :
    ∀ i j : Fin 4 × Fin 4, ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i j).im = 0 := by
  intro i j
  have hM : ∀ a c : Fin 4, ((1 / 2 : ℂ) * (!![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] : Matrix (Fin 4) (Fin 4) ℂ) a c).im = 0 := by
    intro a c
    fin_cases a <;> fin_cases c <;> simp
  have h2 : ∀ c b : Fin 4, (if c = 3 ∧ b = 3 then (-1 : ℂ) else 1).im = 0 := by
    intro c b
    split_ifs <;> simp
  have key : ∀ x y w : ℂ, x.im = 0 → y.im = 0 → w.im = 0 → (x * y * w).im = 0 := by
    intro x y w hx hy hw
    simp [Complex.mul_im, hx, hy, hw]
  exact key _ _ _ (hM i.1 j.1) (h2 j.1 i.2) (hM i.2 j.2)
#print axioms a35_shared_real_im
theorem a35_shared_real_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  (∀ i j, ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i j).im = 0) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x} ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) i k) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}
  ∧ ∑ k : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) (0, 0) k * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) (0, 1) k * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) (0, 2) k * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀)) j.1 i.2 j.2) (0, 3) k = 1 / 32 := by
  intro Γ₀ hΓ₀
  have h1 : star (1 : ℂ) * 1 = 1 := by simp
  refine ⟨a35_shared_real_im, ⟨(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀), fun _ => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] a₀ c₀), (fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1), a35_shared_f4_flat Γ₀ hΓ₀ 1 h1, fun _ => a35_shared_f4_flat Γ₀ hΓ₀ 1 h1, ?_, rfl⟩, a35_shared_real_notin Γ₀ hΓ₀, ?_⟩
  · intro c b
    dsimp only
    split_ifs <;> simp
  · simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four]
    norm_num
#print axioms a35_shared_real_core
theorem a35_shared_untw_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun _ _ : Fin 4 => (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} := by
  intro Γ₀ hΓ₀
  have h := a34_control_product Γ₀ hΓ₀
  dsimp only at h
  obtain ⟨X, Y, hX, hY, hxy⟩ := h
  refine ⟨X, Y, hX, hY, ?_⟩
  rw [← a35_shared_untw_eq]
  exact hxy
#print axioms a35_shared_untw_core
theorem a35_shared_relab_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))))
  ∧ (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, dist (featureVec (fun i => (G ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))))) (featureVec (fun i => (G' ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))))) = dist (featureVec G) (featureVec G'))
  ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x} ∧ featureVec (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))) ∉ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}
  ∧ (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))) (0, 0) (0, 2) (1, 2) * (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))) (0, 1) (1, 2) (0, 2) = -(Complex.I / 256) := by
  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  have hT := a34_shared_tup_real Γ₀ hΓ₀ 0 Complex.I hI
  have hP : RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.1 j.1 k.1 * ((fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).1 i)).submatrix (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2 (![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)] 0).2)) i.2 j.2 k.2) := by
    obtain ⟨U1, hU1, hF1⟩ := sh1_sufficiency (0 : Fin 1) hT
    obtain ⟨U, hU, hFU⟩ := product_realizable hU1 hU1
    have := sh1_necessity hU
    rw [hFU, hF1] at this
    exact this
  refine ⟨?_, ?_, ⟨_, _, hT, hT, rfl⟩, ?_, ?_⟩
  · exact relabel2_realizable (A := Fin 1 × Fin 1) _ (fun i j i' j' => by rw [hΓ₀]; simp) _ _ _ hP
  · intro G G'
    let d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ := fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)
    have h1 := dist_featureVec d rfl (fun i => (G ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)))) (fun i => (G' ((Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) i)).submatrix (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))) (Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))))
    have h2 := dist_featureVec d rfl G G'
    rw [← h1, ← h2]
    exact relabel2_isometry d rfl _ _ G G'
  · intro hS
    obtain ⟨X, Y, hX, hY, hxy⟩ := hS
    have hq := (a34_shared_feature_ext _ _).1 hxy ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4))))
    have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY 0 0 1 0 1 2
    have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY 0 1 0 2
    have hL : mixedTriple (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)))) = 1 / 4096 := by
      simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢
      rw [hc, hd]
      norm_num
    rw [hL] at hq
    simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four] at hq <;> norm_num at hq
  · simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four]
    norm_num
#print axioms a35_shared_relab_core
theorem a35_shared_perm_unitary :
    ∀ (A : Matrix (Fin 4) (Fin 4) ℂ) (e f : Equiv.Perm (Fin 4)), A ∈ Matrix.unitaryGroup (Fin 4) ℂ → A.submatrix e f ∈ Matrix.unitaryGroup (Fin 4) ℂ := by
  intro A e f hA
  rw [Matrix.mem_unitaryGroup_iff] at hA ⊢
  ext i j
  have h := congrFun (congrFun hA (e i)) (e j)
  rw [Matrix.mul_apply, Matrix.one_apply] at h ⊢
  simp only [Matrix.star_apply, Matrix.submatrix_apply] at h ⊢
  rw [Equiv.sum_comp f (fun k => A (e i) k * star (A (e j) k)), h]
  simp [e.injective.eq_iff]
#print axioms a35_shared_perm_unitary
theorem a35_shared_conj_unitary :
    ∀ A : Matrix (Fin 4) (Fin 4) ℂ, A ∈ Matrix.unitaryGroup (Fin 4) ℂ → (Matrix.of fun a c : Fin 4 => star (A a c)) ∈ Matrix.unitaryGroup (Fin 4) ℂ := by
  intro A hA
  rw [Matrix.mem_unitaryGroup_iff] at hA ⊢
  ext i j
  have h := congrFun (congrFun hA j) i
  rw [Matrix.mul_apply, Matrix.one_apply] at h ⊢
  simp only [Matrix.star_apply, Matrix.of_apply, star_star] at h ⊢
  rw [Finset.sum_congr rfl (fun k _ => mul_comm (star (A i k)) (A j k)), h]
  by_cases hij : i = j
  · subst hij
    simp
  · simp [hij, Ne.symm hij]
#print axioms a35_shared_conj_unitary
theorem a35_shared_ext_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) → (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) → (∀ c b, ‖D c b‖ = 1) →
    featureVec (fun i => ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x}
    ∧ featureVec (fun i => Matrix.of fun j k => star ((fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) i j k)) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ c, ((Y c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y c) a₁ c₁‖ = 1 / 2)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) i k) = x}
    ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2)ᵀ) i j) * ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2)ᵀ) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) ∧ (∀ a, ((Y a) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖(Y a) a₁ c₁‖ = 1 / 2)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2) i k) = x} := by
  intro Γ₀ hΓ₀ π₁ π₂ τ₁ τ₂ X Y D hX hY hD
  refine ⟨?_, ?_, ?_⟩
  · refine ⟨X.submatrix π₁ τ₁, fun c => (Y (τ₁ c)).submatrix π₂ τ₂, fun c b => D (τ₁ c) (π₂ b), ⟨a35_shared_perm_unitary X π₁ τ₁ hX.1, fun a c => by simp only [Matrix.submatrix_apply]; exact hX.2 _ _⟩, fun c => ⟨a35_shared_perm_unitary _ π₂ τ₂ (hY _).1, fun a d => by simp only [Matrix.submatrix_apply]; exact (hY _).2 _ _⟩, fun c b => hD _ _, ?_⟩
    congr 1
  · refine ⟨Matrix.of fun a c : Fin 4 => star (X a c), fun c => Matrix.of fun a d : Fin 4 => star (Y c a d), fun c b => star (D c b), ⟨a35_shared_conj_unitary X hX.1, fun a c => by simp only [Matrix.of_apply, norm_star]; exact hX.2 a c⟩, fun c => ⟨a35_shared_conj_unitary _ (hY c).1, fun a d => by simp only [Matrix.of_apply, norm_star]; exact (hY c).2 a d⟩, fun c b => by rw [norm_star]; exact hD c b, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply, star_mul, star_star]
    ring
  · refine ⟨Xᵀ, fun a => (Y a)ᵀ, D, ⟨transpose_unitary hX.1, fun a c => by simp only [Matrix.transpose_apply]; exact hX.2 c a⟩, fun a => ⟨transpose_unitary (hY a).1, fun b d => by simp only [Matrix.transpose_apply]; exact (hY a).2 d b⟩, hD, ?_⟩
    congr 1
#print axioms a35_shared_ext_core
theorem a35_shared_unit_solve :
    ∀ p q r s p' q' r' s' : ℂ, star p * p = 1 → star q * q = 1 → star r * r = 1 → star s * s = 1 → star p' * p' = 1 → star q' * q' = 1 → star r' * r' = 1 → star s' * s' = 1 →
    star p * q * star r * s * star s * s = star p' * q' * star r' * s' * star s' * s' → p' = (s' * star s) * (q' * star q * r * star r') * p := by
  intro p q r s p' q' r' s' hp hq hr hs hp' hq' hr' hs' h
  have h1 : star p * q * star r * s = star p' * q' * star r' * s' := by
    linear_combination h - (star p * q * star r * s) * hs + (star p' * q' * star r' * s') * hs'
  linear_combination (p' * p * r * star q * star s) * h1 - p' * (q * star q * (star r * r) * (s * star s)) * hp - p' * (star r * r * (s * star s)) * hq - p' * (s * star s) * hr - p' * hs + (s' * star s * (q' * star q * r * star r') * p) * hp'
#print axioms a35_shared_unit_solve
theorem a35_shared_mod_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ (X Y : Matrix (Fin 4) (Fin 4) ℂ) (D D' : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖X a₁ c₁‖ = 1 / 2) → (Y ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖Y a₁ c₁‖ = 1 / 2) → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D' c b‖ = 1) →
    featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * (fun _ => Y) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * (fun _ => Y) j.1 i.2 j.2) i k) = featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D' j.1 i.2 * (fun _ => Y) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D' j.1 i.2 * (fun _ => Y) j.1 i.2 j.2) i k) →
    ∃ u v : Fin 4 → ℂ, ∀ c b, D' c b = u c * v b * D c b := by
  intro Γ₀ hΓ₀ X Y D D' hX hY hD hD' hfeat
  refine ⟨fun c => D' c 0 * star (D c 0), fun b => D' 0 b * star (D 0 b) * D 0 0 * star (D' 0 0), fun c b => ?_⟩
  have hq := (a34_shared_feature_ext _ _).1 hfeat ((((0 : Fin 4), b), ((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))), ((c, (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), (c, (0 : Fin 4))))
  simp only [mixedTriple, Matrix.of_apply, star_mul] at hq
  have hXne : ∀ a c : Fin 4, X a c ≠ 0 := fun a c => a35_shared_ne_zero _ _ (by norm_num) (hX.2 a c)
  have hYne : ∀ a c : Fin 4, Y a c ≠ 0 := fun a c => a35_shared_ne_zero _ _ (by norm_num) (hY.2 a c)
  have hK : star (X 0 c) * X 0 0 * star (X 0 0) * X 0 c * star (X 0 c) * X 0 c * star (Y b 0) * Y b 0 * star (Y 0 0) * Y 0 0 * star (Y 0 0) * Y 0 0 ≠ 0 := by
    repeat' apply mul_ne_zero
    all_goals first
      | exact hXne _ _
      | exact hYne _ _
      | (rw [ne_eq, star_eq_zero]; exact hXne _ _)
      | (rw [ne_eq, star_eq_zero]; exact hYne _ _)
  have hf : star (D c b) * D 0 b * star (D 0 0) * D c 0 * star (D c 0) * D c 0 = star (D' c b) * D' 0 b * star (D' 0 0) * D' c 0 * star (D' c 0) * D' c 0 := by
    apply mul_left_cancel₀ hK
    linear_combination hq
  have u := fun c b => a35_shared_unit_of_norm _ (hD c b)
  have u' := fun c b => a35_shared_unit_of_norm _ (hD' c b)
  have := a35_shared_unit_solve (D c b) (D 0 b) (D 0 0) (D c 0) (D' c b) (D' 0 b) (D' 0 0) (D' c 0) (u c b) (u 0 b) (u 0 0) (u c 0) (u' c b) (u' 0 b) (u' 0 0) (u' c 0) hf
  exact this
#print axioms a35_shared_mod_core
theorem a35_shared_zn :
    ∀ n : ℕ, ‖(((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I))‖ = 1 ∧ ((n : ℂ) - Complex.I) ≠ 0 := by
  intro n
  have hne : ((n : ℂ) - Complex.I) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
  have hne2 : ((n : ℂ) + Complex.I) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
  refine ⟨?_, hne⟩
  have hst : star ((n : ℂ) + Complex.I) = (n : ℂ) - Complex.I := by
    simp [Complex.star_def, Complex.conj_I, sub_eq_add_neg]
  rw [norm_div, ← hst, norm_star, div_self (norm_ne_zero_iff.2 hne2)]
#print axioms a35_shared_zn
theorem a35_shared_zn_inj :
    ∀ n m : ℕ, (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) = (((m : ℂ) + Complex.I) / ((m : ℂ) - Complex.I)) → n = m := by
  intro n m h
  have hn := (a35_shared_zn n).2
  have hm := (a35_shared_zn m).2
  rw [div_eq_div_iff hn hm] at h
  have him := congrArg Complex.im h
  simp [Complex.mul_im, Complex.mul_re] at him
  have : (n : ℝ) = m := by linarith
  exact_mod_cast this
#print axioms a35_shared_zn_inj
theorem a35_shared_inf_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k)}
  ∧ ∀ (G : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))) (T : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧
    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k) := by
  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  have hF := a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI
  have hDn : ∀ n : ℕ, ∀ c b : Fin 4, ‖((fun c b : Fin 4 => if c = 1 ∧ b = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ))) c b‖ = 1 := by
    intro n c b
    simp only []
    split_ifs
    · exact (a35_shared_zn n).1
    · simp
  have hinf : Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * D j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k)} := by
    refine Set.infinite_of_injective_forall_mem (f := fun n : ℕ => featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 ∧ b = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀) i.1 j.1 * (fun c b : Fin 4 => if c = 1 ∧ b = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) j.1 i.2 * (fun _ : Fin 4 => (Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] a₀ c₀)) j.1 i.2 j.2) i k)) ?_ ?_
    · intro n m h
      obtain ⟨u, v, huv⟩ := a35_shared_mod_core Γ₀ hΓ₀ _ _ _ _ hF hF (hDn n) (hDn m) h
      have hx00 : ¬((0 : Fin 4) = 1 ∧ (0 : Fin 4) = 1) := by decide
      have hx01 : ¬((0 : Fin 4) = 1 ∧ (1 : Fin 4) = 1) := by decide
      have hx10 : ¬((1 : Fin 4) = 1 ∧ (0 : Fin 4) = 1) := by decide
      have hx11 : ((1 : Fin 4) = 1 ∧ (1 : Fin 4) = 1) := by decide
      have h00 : (if (0 : Fin 4) = 1 ∧ (0 : Fin 4) = 1 then (((m : ℂ) + Complex.I) / ((m : ℂ) - Complex.I)) else (1 : ℂ)) = u 0 * v 0 * (if (0 : Fin 4) = 1 ∧ (0 : Fin 4) = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) := huv 0 0
      have h01 : (if (0 : Fin 4) = 1 ∧ (1 : Fin 4) = 1 then (((m : ℂ) + Complex.I) / ((m : ℂ) - Complex.I)) else (1 : ℂ)) = u 0 * v 1 * (if (0 : Fin 4) = 1 ∧ (1 : Fin 4) = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) := huv 0 1
      have h10 : (if (1 : Fin 4) = 1 ∧ (0 : Fin 4) = 1 then (((m : ℂ) + Complex.I) / ((m : ℂ) - Complex.I)) else (1 : ℂ)) = u 1 * v 0 * (if (1 : Fin 4) = 1 ∧ (0 : Fin 4) = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) := huv 1 0
      have h11 : (if (1 : Fin 4) = 1 ∧ (1 : Fin 4) = 1 then (((m : ℂ) + Complex.I) / ((m : ℂ) - Complex.I)) else (1 : ℂ)) = u 1 * v 1 * (if (1 : Fin 4) = 1 ∧ (1 : Fin 4) = 1 then (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) else (1 : ℂ)) := huv 1 1
      rw [if_neg hx00, if_neg hx00] at h00
      rw [if_neg hx01, if_neg hx01] at h01
      rw [if_neg hx10, if_neg hx10] at h10
      rw [if_pos hx11, if_pos hx11] at h11
      apply a35_shared_zn_inj
      linear_combination -h11 + (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) * h10 + (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) * u 1 * v 0 * h01 - (((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I)) * u 1 * v 1 * h00
    · intro n
      exact ⟨_, hDn n, rfl⟩
  refine ⟨hinf, ?_⟩
  intro G T
  by_contra hcon
  push_neg at hcon
  apply hinf
  have hK : (⋃ g ∈ G, ⋃ t ∈ T, ({g t} : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))))).Finite :=
    Set.Finite.biUnion (Finset.finite_toSet G) (fun g _ => Set.Finite.biUnion (Finset.finite_toSet T) (fun t _ => Set.finite_singleton _))
  refine hK.subset ?_
  rintro x ⟨D, hD, rfl⟩
  obtain ⟨g, hg, t, ht, hgt⟩ := hcon D hD
  simp only [Set.mem_iUnion, Set.mem_singleton_iff]
  exact ⟨g, hg, t, ht, hgt.symm⟩
#print axioms a35_shared_inf_core
theorem a35_shared_hull :
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
  ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita X Y D)) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_hull_core Γ₀ hΓ₀
#print axioms a35_shared_hull
theorem a35_shared_hull_t :
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
  ∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X → (∀ a, fl (Y a)) → (∀ a d, ‖E a d‖ = 1) →
    ditaT X Y E ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖ditaT X Y E i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (ditaT X Y E)) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_hull_t_core Γ₀ hΓ₀
#print axioms a35_shared_hull_t
theorem a35_shared_hull_sub :
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
  Δc ⊆ N ∧ Δr ⊆ N := by
  intro Γ₀ hΓ₀
  dsimp only
  constructor
  · intro x hx
    obtain ⟨X, Y, D, hX, hY, hD, rfl⟩ := hx
    exact ⟨_, (a35_shared_hull_core Γ₀ hΓ₀ X Y D hX hY hD).2.2, rfl⟩
  · intro x hx
    obtain ⟨X, Y, E, hX, hY, hE, rfl⟩ := hx
    exact ⟨_, (a35_shared_hull_t_core Γ₀ hΓ₀ X Y E hX hY hE).2.2, rfl⟩
#print axioms a35_shared_hull_sub
theorem a35_shared_sigma_hull :
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
  S ⊆ Δc ∧ S ⊆ Δr := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_sigma_core Γ₀ hΓ₀
#print axioms a35_shared_sigma_hull
theorem a35_shared_cross :
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
  ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → ∀ a b b' c c' d : Fin 4,
    prod X Y (a, b) (c, d) (c', d) * prod X Y (a, b') (c', d) (c, d) = 1 / 256 := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_cross_core Γ₀ hΓ₀
#print axioms a35_shared_cross
theorem a35_control_witness :
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
  let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2
  let ρ : Equiv.Perm (Fin 4 × Fin 4) := (Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))
  H = dita (F4 Complex.I) (fun c => F4 (if c.val % 2 = 0 then Complex.I else -Complex.I)) (fun _ _ => 1)
  ∧ featureVec (gram H) ∈ Δc ∧ featureVec (gram H) ∉ S
  ∧ gram H (0, 1) (0, 1) (1, 1) * gram H (0, 0) (1, 1) (0, 1) = -(1 / 256)
  ∧ (∀ i j, H i j = dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1) i (ρ j))
  ∧ featureVec (gram H) = featureVec (fun i => (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1)) i).submatrix ρ ρ) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_wit_core Γ₀ hΓ₀
#print axioms a35_control_witness
theorem a35_control_twist :
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
  let Dw : Fin 4 → Fin 4 → ℂ := fun c b => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else 1
  let Hw : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := dita (F4 Complex.I) (fun _ => F4 Complex.I) Dw
  featureVec (gram Hw) ∈ Δc ∧ featureVec (gram Hw) ∉ S
  ∧ ∑ k : Fin 4 × Fin 4, Hw (0, 0) k * star (Hw (0, 1) k) * Hw (0, 2) k * star (Hw (1, 1) k) = Complex.I / 32 := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_twist_core Γ₀ hΓ₀
#print axioms a35_control_twist
theorem a35_control_real :
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
  let Dr : Fin 4 → Fin 4 → ℂ := fun c b => if c = 3 ∧ b = 3 then -1 else 1
  let Hr : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := dita (F4 1) (fun _ => F4 1) Dr
  (∀ i j, (Hr i j).im = 0) ∧ featureVec (gram Hr) ∈ Δc ∧ featureVec (gram Hr) ∉ S
  ∧ ∑ k : Fin 4 × Fin 4, Hr (0, 0) k * Hr (0, 1) k * Hr (0, 2) k * Hr (0, 3) k = 1 / 32 := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_real_core Γ₀ hΓ₀
#print axioms a35_control_real
theorem a35_control_relabel :
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
  let σ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
  let P : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := prod (tup 0 Complex.I) (tup 0 Complex.I)
  let Pσ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i => (P (σ i)).submatrix σ σ
  RealizableGram (Fin 1 × Fin 1) Γ Pσ
  ∧ (∀ G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, dist (featureVec (fun i => (G (σ i)).submatrix σ σ)) (featureVec (fun i => (G' (σ i)).submatrix σ σ)) = dist (featureVec G) (featureVec G'))
  ∧ featureVec P ∈ S ∧ featureVec Pσ ∉ S
  ∧ Pσ (0, 0) (0, 2) (1, 2) * Pσ (0, 1) (1, 2) (0, 2) = -(Complex.I / 256) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_relab_core Γ₀ hΓ₀
#print axioms a35_control_relabel
theorem a35_shared_extend :
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
  ∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    featureVec (fun i => (gram (dita X Y D) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ Δc
    ∧ featureVec (fun i => Matrix.of fun j k => star (gram (dita X Y D) i j k)) ∈ Δc
    ∧ featureVec (gram (dita X Y D)ᵀ) ∈ Δr := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_ext_core Γ₀ hΓ₀
#print axioms a35_shared_extend
theorem a35_shared_modulus :
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
  ∀ (X Y : Matrix (Fin 4) (Fin 4) ℂ) (D D' : Fin 4 → Fin 4 → ℂ), fl X → fl Y → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D' c b‖ = 1) →
    featureVec (gram (dita X (fun _ => Y) D)) = featureVec (gram (dita X (fun _ => Y) D')) →
    ∃ u v : Fin 4 → ℂ, ∀ c b, D' c b = u c * v b * D c b := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_mod_core Γ₀ hΓ₀
#print axioms a35_shared_modulus
theorem a35_shared_infinite :
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
  Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))}
  ∧ ∀ (G : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))) (T : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧
    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D)) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_inf_core Γ₀ hΓ₀
#print axioms a35_shared_infinite
theorem a35_control_untwisted :
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
  featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1))) ∈ S := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a35_shared_untw_core Γ₀ hΓ₀
#print axioms a35_control_untwisted
theorem a35_dita_stratified :
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
  (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita X Y D)))
  ∧ (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X → (∀ a, fl (Y a)) → (∀ a d, ‖E a d‖ = 1) →
    ditaT X Y E ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖ditaT X Y E i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (ditaT X Y E)))
  ∧ (S ⊆ Δc ∧ S ⊆ Δr)
  ∧ (∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    featureVec (fun i => (gram (dita X Y D) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ Δc
    ∧ featureVec (fun i => Matrix.of fun j k => star (gram (dita X Y D) i j k)) ∈ Δc
    ∧ featureVec (gram (dita X Y D)ᵀ) ∈ Δr)
  ∧ (∀ (X Y : Matrix (Fin 4) (Fin 4) ℂ) (D D' : Fin 4 → Fin 4 → ℂ), fl X → fl Y → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D' c b‖ = 1) →
    featureVec (gram (dita X (fun _ => Y) D)) = featureVec (gram (dita X (fun _ => Y) D')) →
    ∃ u v : Fin 4 → ℂ, ∀ c b, D' c b = u c * v b * D c b)
  ∧ (Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))}
  ∧ ∀ (G : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))) (T : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧
    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact ⟨a35_shared_hull_core Γ₀ hΓ₀, a35_shared_hull_t_core Γ₀ hΓ₀, a35_shared_sigma_core Γ₀ hΓ₀, a35_shared_ext_core Γ₀ hΓ₀, a35_shared_mod_core Γ₀ hΓ₀, a35_shared_inf_core Γ₀ hΓ₀⟩
#print axioms a35_dita_stratified
theorem a35_c_exclusive :
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
  ¬ (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita X Y D)))
  ∨ ¬ (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X → (∀ a, fl (Y a)) → (∀ a d, ‖E a d‖ = 1) →
    ditaT X Y E ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖ditaT X Y E i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (ditaT X Y E)))
  ∨ ¬ (S ⊆ Δc ∧ S ⊆ Δr)
  ∨ ¬ (∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    featureVec (fun i => (gram (dita X Y D) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ Δc
    ∧ featureVec (fun i => Matrix.of fun j k => star (gram (dita X Y D) i j k)) ∈ Δc
    ∧ featureVec (gram (dita X Y D)ᵀ) ∈ Δr)
  ∨ ¬ (∀ (X Y : Matrix (Fin 4) (Fin 4) ℂ) (D D' : Fin 4 → Fin 4 → ℂ), fl X → fl Y → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D' c b‖ = 1) →
    featureVec (gram (dita X (fun _ => Y) D)) = featureVec (gram (dita X (fun _ => Y) D')) →
    ∃ u v : Fin 4 → ℂ, ∀ c b, D' c b = u c * v b * D c b)
  ∨ ¬ (Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))}
  ∧ ∀ (G : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))) (T : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧
    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D)))) → ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
  (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita X Y D)))
  ∧ (∀ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X → (∀ a, fl (Y a)) → (∀ a d, ‖E a d‖ = 1) →
    ditaT X Y E ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖ditaT X Y E i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (ditaT X Y E)))
  ∧ (S ⊆ Δc ∧ S ⊆ Δr)
  ∧ (∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    featureVec (fun i => (gram (dita X Y D) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ Δc
    ∧ featureVec (fun i => Matrix.of fun j k => star (gram (dita X Y D) i j k)) ∈ Δc
    ∧ featureVec (gram (dita X Y D)ᵀ) ∈ Δr)
  ∧ (∀ (X Y : Matrix (Fin 4) (Fin 4) ℂ) (D D' : Fin 4 → Fin 4 → ℂ), fl X → fl Y → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D' c b‖ = 1) →
    featureVec (gram (dita X (fun _ => Y) D)) = featureVec (gram (dita X (fun _ => Y) D')) →
    ∃ u v : Fin 4 → ℂ, ∀ c b, D' c b = u c * v b * D c b)
  ∧ (Set.Infinite {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))}
  ∧ ∀ (G : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))) (T : Finset (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))))), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧
    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D)))) := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with h | h | h | h | h | h
  · exact h r.1
  · exact h r.2.1
  · exact h r.2.2.1
  · exact h r.2.2.2.1
  · exact h r.2.2.2.2.1
  · exact h r.2.2.2.2.2
#print axioms a35_c_exclusive
end DitaHull
end OIBridge
