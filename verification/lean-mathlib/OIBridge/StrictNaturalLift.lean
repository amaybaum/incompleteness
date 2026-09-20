import OIBridge.OrbitGeometryRigidity

/-!
# Act 27: the single-carrier gauge lemmas

The configuration is `Fin 4`, `Fin 1`, anchor `0`, and the uniform visible
matrix with entries `1 / 4`. All predicates are consumed from the pinned
modules. This module introduces no top-level definition.

The initial module commit contains shared lemmas only. The class-map targets
are executed in their separately ordered verdict commits.
-/

namespace OIBridge
namespace StrictNaturalLift

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  RepresentativeNaturality OrbitLawRigidityTwisted OrbitGeometryIsometries

theorem a27_shared_fibreGram_entry
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (i j k : Fin 4) :
    FibreGram (0 : Fin 1) U i j k = star (U (i, 0) (j, 0)) * U (i, 0) (k, 0) := by
  simpa only [Fin.sum_univ_one] using fibreGram_apply (0 : Fin 1) U i j k

theorem a27_shared_weak_diagonal (c : Fin 4 → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    WeakAnchorStabilizer (0 : Fin 1)
      (Matrix.diagonal fun p : Fin 4 × Fin 1 => c p.1) := by
  have h := (weak_diagonal_phase (a₀ := (0 : Fin 1)) c hc).1
  have heq : (Matrix.diagonal fun p : Fin 4 × Fin 1 => if p.2 = 0 then c p.1 else 1) =
      Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
    congr 1
    funext p
    simp [Subsingleton.elim p.2 (0 : Fin 1)]
  rw [heq] at h
  exact h

theorem a27_shared_weak_one :
    WeakAnchorStabilizer (0 : Fin 1) (1 : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) := by
  simpa only [Matrix.diagonal_one] using a27_shared_weak_diagonal (fun _ => 1) (fun _ => by simp)

theorem a27_shared_left_diagonal (c : Fin 4 → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    LeftFibreGroup (Matrix.diagonal fun p : Fin 4 × Fin 1 => c p.1) := by
  refine ⟨(a27_shared_weak_diagonal c hc).1, ?_⟩
  intro p q hpq
  exact Matrix.diagonal_apply_ne _ (fun h => hpq (congrArg Prod.fst h))

theorem a27_shared_weak_shape (K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    WeakAnchorStabilizer (0 : Fin 1) K ↔
      ∃ c : Fin 4 → ℂ, (∀ j, ‖c j‖ = 1) ∧
        K = Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
  constructor
  · rintro ⟨hK, c, hc⟩
    refine ⟨c, weak_anchor_coeff_norm_one hK hc, ?_⟩
    ext p q
    obtain ⟨j, a⟩ := q
    have ha : a = 0 := Subsingleton.elim _ _
    subst a
    rw [hc, Matrix.diagonal_apply]
    split_ifs with hp
    · subst p; rfl
    · rfl
  · rintro ⟨c, hc, rfl⟩
    exact a27_shared_weak_diagonal c hc

theorem a27_shared_left_shape (L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    LeftFibreGroup L ↔
      ∃ c : Fin 4 → ℂ, (∀ j, ‖c j‖ = 1) ∧
        L = Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
  constructor
  · intro hL
    let c : Fin 4 → ℂ := fun i => L (i, 0) (i, 0)
    have hc : ∀ p j, L p (j, 0) = if p = (j, 0) then c j else 0 := by
      intro p j
      by_cases hp : p = (j, 0)
      · subst p; simp [c]
      · rw [if_neg hp]
        apply hL.2
        intro h
        apply hp
        exact Prod.ext h (Subsingleton.elim _ _)
    exact (a27_shared_weak_shape L).mp ⟨hL.1, c, hc⟩
  · rintro ⟨c, hc, rfl⟩
    exact a27_shared_left_diagonal c hc

theorem a27_shared_left_mul
    {L M : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hL : LeftFibreGroup L) (hM : LeftFibreGroup M) : LeftFibreGroup (L * M) := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_left_shape L).mp hL
  obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape M).mp hM
  rw [Matrix.diagonal_mul_diagonal]
  exact a27_shared_left_diagonal (fun i => c i * d i)
    (fun i => by rw [norm_mul, hc, hd, one_mul])

theorem a27_shared_left_star
    {L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hL : LeftFibreGroup L) : LeftFibreGroup Lᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_left_shape L).mp hL
  rw [Matrix.diagonal_conjTranspose]
  exact a27_shared_left_diagonal (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a27_shared_weak_star
    {K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hK : WeakAnchorStabilizer (0 : Fin 1) K) : WeakAnchorStabilizer (0 : Fin 1) Kᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_weak_shape K).mp hK
  rw [Matrix.diagonal_conjTranspose]
  exact a27_shared_weak_diagonal (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a27_shared_left_admissible_iff
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ} (hL : LeftFibreGroup L)
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) (L * U) ↔
      AdmissibleDilationAt Γ₀ (0 : Fin 1) U := by
  have hLL : Lᴴ * L = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff'.mp hL.1
  constructor
  · intro h
    have h' := left_preserves_admissible (a27_shared_left_star hL) h
    simpa only [← Matrix.mul_assoc, hLL, Matrix.one_mul] using h'
  · exact left_preserves_admissible hL

theorem a27_shared_right_admissible_iff
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) (U * K) ↔
      AdmissibleDilationAt Γ₀ (0 : Fin 1) U := by
  have hKK : K * Kᴴ = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff.mp hK.1
  constructor
  · intro h
    have h' := weak_preserves_admissible h (a27_shared_weak_star hK)
    simpa only [Matrix.mul_assoc, hKK, Matrix.mul_one] using h'
  · exact fun h => weak_preserves_admissible h hK

theorem a27_shared_admissible_shape
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) U ↔
      U ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ ∧
        ∀ i j, ‖U (i, 0) (j, 0)‖ ^ 2 = (1 / 4 : ℝ) := by
  constructor
  · intro h
    exact ⟨h.1, fun i j => by simpa [hΓ₀, Fin.sum_univ_one] using (h.2 i j).symm⟩
  · rintro ⟨hU, h⟩
    exact ⟨hU, fun i j => by simpa [hΓ₀, Fin.sum_univ_one] using (h i j).symm⟩

theorem a27_shared_admissible_entry_ne_zero
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) (p q : Fin 4 × Fin 1) : U p q ≠ 0 := by
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  have ha : a = 0 := Subsingleton.elim _ _
  have hb : b = 0 := Subsingleton.elim _ _
  subst a
  subst b
  intro hzero
  have h := OrbitGeometrySelector.realizable_entry_ne_zero
    (A := Fin 1) (by simp) Γ₀ (by intro i j; norm_num [hΓ₀])
    (FibreGram (0 : Fin 1) U) (sh1_necessity hU) i j j
  apply h
  simp only [a27_shared_fibreGram_entry, hzero, star_zero, mul_zero]

theorem a27_shared_same_gram
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U U' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (_hU' : AdmissibleDilationAt Γ₀ (0 : Fin 1) U')
    (hG : FibreGram (0 : Fin 1) U = FibreGram (0 : Fin 1) U') :
    ∃ L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, LeftFibreGroup L ∧ U' = L * U := by
  classical
  have hrows : ∀ i : Fin 4, ∃ c : ℂ, ‖c‖ = 1 ∧ ∀ j, U' (i, 0) (j, 0) = c * U (i, 0) (j, 0) := by
    intro i
    apply rows_phase (fun j => U (i, 0) (j, 0)) (fun j => U' (i, 0) (j, 0))
    · intro j k
      simpa only [a27_shared_fibreGram_entry] using congrArg (fun G => G i j k) hG
    · exact fun j => a27_shared_admissible_entry_ne_zero Γ₀ hΓ₀ hU (i, 0) (j, 0)
  choose c hc hrow using hrows
  refine ⟨Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1), a27_shared_left_diagonal c hc, ?_⟩
  ext p q
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  have ha : a = 0 := Subsingleton.elim _ _
  have hb : b = 0 := Subsingleton.elim _ _
  subst a
  subst b
  simpa only [Matrix.diagonal_mul] using hrow i j

theorem a27_shared_realizable_of_equiv
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (hG : RealizableGram (Fin 1) Γ₀ G) (h : GramPhaseEquiv G G') :
    RealizableGram (Fin 1) Γ₀ G' := by
  obtain ⟨U, hU, hUG⟩ := sh1_sufficiency (0 : Fin 1) hG
  obtain ⟨c, hc, hphase⟩ := h
  obtain ⟨hK, hKcol⟩ := weak_diagonal_phase (a₀ := (0 : Fin 1)) c hc
  have hUK := weak_preserves_admissible hU hK
  have hEq : FibreGram (0 : Fin 1)
      (U * Matrix.diagonal (fun p : Fin 4 × Fin 1 => if p.2 = 0 then c p.1 else 1)) = G' := by
    funext i j k
    rw [fibreGram_mul_weak_apply hKcol, hUG, hphase]
  rw [← hEq]
  exact sh1_necessity hUK

theorem a27_shared_phase_coeff_eq
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (d d' k k' : Fin 4 → ℂ)
    (h : Matrix.diagonal (fun p : Fin 4 × Fin 1 => d p.1) * U *
        Matrix.diagonal (fun p : Fin 4 × Fin 1 => k p.1) =
      Matrix.diagonal (fun p : Fin 4 × Fin 1 => d' p.1) * U *
        Matrix.diagonal (fun p : Fin 4 × Fin 1 => k' p.1)) :
    ∀ i j, d i * k j = d' i * k' j := by
  intro i j
  have e := congrArg (fun M => M (i, 0) (j, 0)) h
  simp only [Matrix.diagonal_mul, Matrix.mul_diagonal] at e
  apply mul_right_cancel₀ (a27_shared_admissible_entry_ne_zero Γ₀ hΓ₀ hU (i, 0) (j, 0))
  calc
    (d i * k j) * U (i, 0) (j, 0) = d i * U (i, 0) (j, 0) * k j := by ring
    _ = d' i * U (i, 0) (j, 0) * k' j := e
    _ = (d' i * k' j) * U (i, 0) (j, 0) := by ring

/-- Equal phase representations act equally on every target matrix. -/
theorem a27_shared_transport_eq
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U D D' K K' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (hK' : WeakAnchorStabilizer (0 : Fin 1) K')
    (h : D * U * K = D' * U * K')
    (W : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) : D * W * K = D' * W * K' := by
  obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape D).mp hD
  obtain ⟨d', hd', rfl⟩ := (a27_shared_left_shape D').mp hD'
  obtain ⟨k, hk, rfl⟩ := (a27_shared_weak_shape K).mp hK
  obtain ⟨k', hk', rfl⟩ := (a27_shared_weak_shape K').mp hK'
  have e := a27_shared_phase_coeff_eq Γ₀ hΓ₀ hU d d' k k' h
  ext p q
  simp only [Matrix.diagonal_mul, Matrix.mul_diagonal]
  calc
    d p.1 * W p q * k q.1 = (d p.1 * k q.1) * W p q := by ring
    _ = (d' p.1 * k' q.1) * W p q := by rw [e]
    _ = d' p.1 * W p q * k' q.1 := by ring

/-- The common phase is the complete stabilizer of an admissible base dilation. -/
theorem a27_shared_torsor
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U D D' K K' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (hK' : WeakAnchorStabilizer (0 : Fin 1) K') :
    D * U * K = D' * U * K' ↔
      ∃ u : ℂ, ‖u‖ = 1 ∧ D' = u • D ∧ K' = u⁻¹ • K := by
  constructor
  · intro h
    obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape D).mp hD
    obtain ⟨d', hd', rfl⟩ := (a27_shared_left_shape D').mp hD'
    obtain ⟨k, hk, rfl⟩ := (a27_shared_weak_shape K).mp hK
    obtain ⟨k', hk', rfl⟩ := (a27_shared_weak_shape K').mp hK'
    have e := a27_shared_phase_coeff_eq Γ₀ hΓ₀ hU d d' k k' h
    have hk0 : k 0 ≠ 0 := by intro hz; have := hk 0; simp [hz] at this
    have hk'0 : k' 0 ≠ 0 := by intro hz; have := hk' 0; simp [hz] at this
    have hd'0 : d' 0 ≠ 0 := by intro hz; have := hd' 0; simp [hz] at this
    have ed : ∀ i, d' i = (k 0 / k' 0) * d i := by
      intro i
      rw [div_mul_eq_mul_div, eq_div_iff hk'0]
      calc
        d' i * k' 0 = d i * k 0 := (e i 0).symm
        _ = k 0 * d i := mul_comm _ _
    have ek : ∀ j, k' j = (k 0 / k' 0)⁻¹ * k j := by
      intro j
      rw [inv_div, div_mul_eq_mul_div, eq_div_iff hk0]
      apply mul_left_cancel₀ hd'0
      linear_combination -(k 0) * e 0 j + (k j) * e 0 0
    refine ⟨k 0 / k' 0, by rw [norm_div, hk, hk', div_self one_ne_zero], ?_, ?_⟩
    · ext p q
      by_cases hpq : p = q
      · subst q; simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ed p.1
      · simp [hpq, Matrix.smul_apply]
    · ext p q
      by_cases hpq : p = q
      · subst q; simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ek p.1
      · simp [hpq, Matrix.smul_apply]
  · rintro ⟨u, hu, rfl, rfl⟩
    have hn : u ≠ 0 := by intro hz; simp [hz] at hu
    simp only [Matrix.smul_mul, Matrix.mul_smul, smul_smul,
      inv_mul_cancel₀ hn, one_smul]

#print axioms a27_shared_fibreGram_entry
#print axioms a27_shared_weak_diagonal
#print axioms a27_shared_weak_one
#print axioms a27_shared_left_diagonal
#print axioms a27_shared_weak_shape
#print axioms a27_shared_left_shape
#print axioms a27_shared_left_mul
#print axioms a27_shared_left_star
#print axioms a27_shared_weak_star
#print axioms a27_shared_left_admissible_iff
#print axioms a27_shared_right_admissible_iff
#print axioms a27_shared_admissible_shape
#print axioms a27_shared_admissible_entry_ne_zero
#print axioms a27_shared_same_gram
#print axioms a27_shared_realizable_of_equiv
#print axioms a27_shared_phase_coeff_eq
#print axioms a27_shared_transport_eq
#print axioms a27_shared_torsor

end StrictNaturalLift
end OIBridge
