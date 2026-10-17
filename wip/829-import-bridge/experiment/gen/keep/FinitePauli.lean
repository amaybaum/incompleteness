import OIBridge.EqvK2MaxCone

/- Research/design only. No physical carrier identification or synthesis premise
   is supplied by these finite tensor identities. -/
namespace FiniteReconstructionDesign

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema

noncomputable section

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-- Spectators of arbitrary finite size, rather than a fixed two-qubit tensor. -/
theorem tensor_mul (P R : Matrix A A ℂ) (Q S : Matrix B B ℂ) :
    tensorOf P Q * tensorOf R S = tensorOf (P * R) (Q * S) := by
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type]
  simp only [Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  ring

theorem tensor_trace (P : Matrix A A ℂ) (Q : Matrix B B ℂ) :
    Matrix.trace (tensorOf P Q) = Matrix.trace P * Matrix.trace Q := by
  simp only [Matrix.trace, Matrix.diag_apply, tensorOf_apply, Fintype.sum_prod_type,
    Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]

theorem tensor_star (P : Matrix A A ℂ) (Q : Matrix B B ℂ) :
    (tensorOf P Q)ᴴ = tensorOf Pᴴ Qᴴ := by
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [Matrix.conjTranspose_apply, tensorOf_apply]
  exact star_mul' _ _

theorem tensor_conjugation (U P : Matrix A A ℂ) (V Q : Matrix B B ℂ) :
    tensorOf U V * tensorOf P Q * (tensorOf U V)ᴴ =
      tensorOf (U * P * Uᴴ) (V * Q * Vᴴ) := by
  rw [tensor_star, tensor_mul, tensor_mul]

/-- Recursive binary and Pauli-label carriers include the empty tensor. -/
abbrev Carrier (d : ℕ) : ℕ → Type
  | 0 => Fin 1
  | n + 1 => Carrier d n × Fin d

instance carrierFintype (d n : ℕ) : Fintype (Carrier d n) := by
  induction n with
  | zero => exact inferInstanceAs (Fintype (Fin 1))
  | succ n ih =>
    letI := ih
    exact inferInstanceAs (Fintype (Carrier d n × Fin d))

instance carrierDecidableEq (d n : ℕ) : DecidableEq (Carrier d n) :=
  Classical.decEq _

abbrev Bits := Carrier 2
abbrev Labels := Carrier 4

def pauliWord : (n : ℕ) → Labels n → Matrix (Bits n) (Bits n) ℂ
  | 0, _ => 1
  | n + 1, μ => tensorOf (pauliWord n μ.1) (pauli μ.2)

theorem pauliWord_hermitian (n : ℕ) (μ : Labels n) :
    (pauliWord n μ)ᴴ = pauliWord n μ := by
  induction n with
  | zero => simp [pauliWord]
  | succ n ih =>
    simp only [pauliWord, tensor_star, ih, pauli_conjTranspose]

/-- Exact orthogonality for every finite token count. -/
theorem pauliWord_orthogonal (n : ℕ) (μ ν : Labels n) :
    Matrix.trace (pauliWord n μ * pauliWord n ν) =
      if μ = ν then (2 : ℂ) ^ n else 0 := by
  induction n with
  | zero =>
    have h : μ = ν := Subsingleton.elim _ _
    simp [pauliWord, h, Matrix.trace, Matrix.diag_apply, Fin.sum_univ_one]
  | succ n ih =>
    rcases μ with ⟨μ, a⟩
    rcases ν with ⟨ν, b⟩
    simp only [pauliWord, tensor_mul, tensor_trace, ih, trace_pauli_mul]
    by_cases h : μ = ν <;> by_cases hab : a = b <;>
      simp [h, hab, pow_succ]

/-- Entrywise completeness is the finite-dimensional spanning witness. -/
theorem pauliWord_complete (n : ℕ) (a b c d : Bits n) :
    (∑ μ : Labels n, pauliWord n μ a b * pauliWord n μ c d) =
      if a = d ∧ b = c then (2 : ℂ) ^ n else 0 := by
  induction n with
  | zero =>
    have ha : a = d := Subsingleton.elim _ _
    have hb : b = c := Subsingleton.elim _ _
    have hcd : c = d := Subsingleton.elim _ _
    simp [pauliWord, Matrix.one_apply, ha, hb, hcd, Fin.sum_univ_one]
  | succ n ih =>
    rcases a with ⟨a, a'⟩
    rcases b with ⟨b, b'⟩
    rcases c with ⟨c, c'⟩
    rcases d with ⟨d, d'⟩
    have hf :
        (∑ μ : Labels n, ∑ ν : Fin 4,
          (pauliWord n μ a b * pauli ν a' b') *
            (pauliWord n μ c d * pauli ν c' d')) =
        (∑ μ : Labels n, pauliWord n μ a b * pauliWord n μ c d) *
          (∑ ν : Fin 4, pauli ν a' b' * pauli ν c' d') := by
      simp only [Finset.sum_mul, Finset.mul_sum]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro μ hμ
      apply Finset.sum_congr rfl
      intro ν hν
      ring
    simp only [pauliWord, Fintype.sum_prod_type, tensorOf_apply]
    rw [hf, ih, pauli_complete]
    by_cases ha : a = d <;> by_cases hb : b = c <;>
      by_cases ha' : a' = d' <;> by_cases hb' : b' = c' <;>
        simp [ha, hb, ha', hb', pow_succ]

def complexDictionary (n : ℕ) (w : Labels n → ℂ) : Matrix (Bits n) (Bits n) ℂ :=
  ∑ μ, (w μ / (2 : ℂ) ^ n) • pauliWord n μ

def complexCoordinates (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ) : Labels n → ℂ :=
  fun μ => Matrix.trace (pauliWord n μ * H)

theorem coordinates_dictionary (n : ℕ) (w : Labels n → ℂ) :
    complexCoordinates n (complexDictionary n w) = w := by
  funext μ
  simp only [complexCoordinates, complexDictionary, Finset.mul_sum, Matrix.mul_smul,
    Matrix.trace_sum, Matrix.trace_smul, pauliWord_orthogonal, smul_eq_mul]
  simp [eq_comm, pow_ne_zero]

theorem pauliWord_reconstruction (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ) :
    (∑ μ : Labels n, Matrix.trace (pauliWord n μ * H) • pauliWord n μ) =
      ((2 : ℂ) ^ n) • H := by
  ext a b
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul, Matrix.trace,
    Matrix.diag_apply, Matrix.mul_apply]
  have hexpand :
      (∑ μ : Labels n, (∑ i : Bits n, ∑ j : Bits n,
        pauliWord n μ i j * H j i) * pauliWord n μ a b) =
      ∑ i : Bits n, ∑ j : Bits n, H j i *
        (∑ μ : Labels n, pauliWord n μ i j * pauliWord n μ a b) := by
    simp only [Finset.sum_mul, Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro i hi
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro j hj
    apply Finset.sum_congr rfl
    intro μ hμ
    ring
  rw [hexpand]
  simp only [pauliWord_complete]
  have hrow (i : Bits n) :
      (∑ j : Bits n, H j i * (if i = b ∧ j = a then (2 : ℂ) ^ n else 0)) =
        if i = b then H a b * (2 : ℂ) ^ n else 0 := by
    by_cases hi : i = b <;> simp [hi]
  simp_rw [hrow]
  simp [mul_comm]

theorem dictionary_coordinates (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ) :
    complexDictionary n (complexCoordinates n H) = H := by
  have h := pauliWord_reconstruction n H
  have hn : (2 : ℂ) ^ n ≠ 0 := pow_ne_zero _ (by norm_num)
  ext a b
  have hab := congrFun (congrFun h a) b
  simp only [Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul] at hab
  simp only [complexDictionary, complexCoordinates, Matrix.sum_apply,
    Matrix.smul_apply, smul_eq_mul]
  simp_rw [div_mul_eq_mul_div]
  rw [← Finset.sum_div, hab, mul_div_cancel_left₀ _ hn]

def dictionary (n : ℕ) (w : Labels n → ℝ) : Matrix (Bits n) (Bits n) ℂ :=
  complexDictionary n (fun μ => (w μ : ℂ))

def coordinates (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ) : Labels n → ℝ :=
  fun μ => (complexCoordinates n H μ).re

theorem dictionary_hermitian (n : ℕ) (w : Labels n → ℝ) :
    (dictionary n w).IsHermitian := by
  change (dictionary n w)ᴴ = dictionary n w
  simp [dictionary, complexDictionary, Matrix.conjTranspose_sum,
    Matrix.conjTranspose_smul, pauliWord_hermitian]

theorem coordinates_dictionary_real (n : ℕ) (w : Labels n → ℝ) :
    coordinates n (dictionary n w) = w := by
  funext μ
  simp only [coordinates, dictionary, coordinates_dictionary, Complex.ofReal_re]

theorem coordinates_real (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ)
    (hH : H.IsHermitian) (μ : Labels n) :
    ((coordinates n H μ : ℝ) : ℂ) = complexCoordinates n H μ := by
  unfold coordinates complexCoordinates
  rw [← Complex.conj_eq_iff_re, starRingEnd_apply, ← Matrix.trace_conjTranspose,
    Matrix.conjTranspose_mul, hH.eq, pauliWord_hermitian, Matrix.trace_mul_comm]

theorem dictionary_coordinates_real (n : ℕ) (H : Matrix (Bits n) (Bits n) ℂ)
    (hH : H.IsHermitian) : dictionary n (coordinates n H) = H := by
  have h : (fun μ => (coordinates n H μ : ℂ)) = complexCoordinates n H := by
    funext μ
    exact coordinates_real n H hH μ
  unfold dictionary
  rw [h, dictionary_coordinates]

#print axioms tensor_conjugation
#print axioms pauliWord_orthogonal
#print axioms pauliWord_complete
#print axioms coordinates_dictionary
#print axioms dictionary_coordinates
#print axioms dictionary_hermitian
#print axioms coordinates_dictionary_real
#print axioms dictionary_coordinates_real

end
end FiniteReconstructionDesign
