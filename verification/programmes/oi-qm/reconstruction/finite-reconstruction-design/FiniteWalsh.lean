import FinitePauli

/- Exact Walsh inversion for any finite number of controls. The Gray ordering
   is a permutation parameter here; adjacency and circuit synthesis are separate
   obligations, rather than premises hidden inside this matrix identity. -/
namespace FiniteReconstructionDesign

open Matrix
noncomputable section

def hadamard : Matrix (Fin 2) (Fin 2) ℝ := !![1, 1; 1, -1]

def walsh : (n : ℕ) → Matrix (Bits n) (Bits n) ℝ
  | 0 => fun _ _ => 1
  | n + 1 => fun a b => walsh n a.1 b.1 * hadamard a.2 b.2

theorem hadamard_symmetric (a b : Fin 2) : hadamard a b = hadamard b a := by
  fin_cases a <;> fin_cases b <;> norm_num [hadamard]

theorem hadamard_orthogonal (a b : Fin 2) :
    (∑ c : Fin 2, hadamard a c * hadamard b c) = if a = b then 2 else 0 := by
  fin_cases a <;> fin_cases b <;> norm_num [hadamard, Fin.sum_univ_two]

theorem walsh_symmetric (n : ℕ) (a b : Bits n) : walsh n a b = walsh n b a := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [walsh, ih, hadamard_symmetric]

theorem walsh_orthogonal (n : ℕ) (a b : Bits n) :
    (∑ c : Bits n, walsh n a c * walsh n b c) =
      if a = b then (2 : ℝ) ^ n else 0 := by
  induction n with
  | zero =>
    have h : a = b := Subsingleton.elim _ _
    simp [walsh, h, Fin.sum_univ_one]
  | succ n ih =>
    rcases a with ⟨a, a'⟩
    rcases b with ⟨b, b'⟩
    have hf :
        (∑ c : Bits n, ∑ d : Fin 2,
          (walsh n a c * hadamard a' d) * (walsh n b c * hadamard b' d)) =
        (∑ c : Bits n, walsh n a c * walsh n b c) *
          (∑ d : Fin 2, hadamard a' d * hadamard b' d) := by
      simp only [Finset.sum_mul, Finset.mul_sum]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro c hc
      apply Finset.sum_congr rfl
      intro d hd
      ring
    simp only [walsh, Fintype.sum_prod_type]
    rw [hf, ih, hadamard_orthogonal]
    by_cases h : a = b <;> by_cases h' : a' = b' <;>
      simp [h, h', pow_succ]

/-- Any bijective ordering, including a cyclic Gray ordering, retains orthogonality. -/
theorem walsh_permuted_orthogonal (n : ℕ) (g : Equiv.Perm (Bits n)) (a b : Bits n) :
    (∑ c : Bits n, walsh n a (g c) * walsh n b (g c)) =
      if a = b then (2 : ℝ) ^ n else 0 := by
  rw [Equiv.sum_comp g (fun c => walsh n a c * walsh n b c)]
  exact walsh_orthogonal n a b

def multiplexorAngles (n : ℕ) (g : Equiv.Perm (Bits n)) (θ : Bits n → ℝ) :
    Bits n → ℝ :=
  fun j => (∑ b, walsh n b (g j) * θ b) / (2 : ℝ) ^ n

/-- Every branch angle is recovered exactly; no rational-angle or density restriction. -/
theorem multiplexorAngles_recover (n : ℕ) (g : Equiv.Perm (Bits n))
    (θ : Bits n → ℝ) (b : Bits n) :
    (∑ j, walsh n b (g j) * multiplexorAngles n g θ j) = θ b := by
  unfold multiplexorAngles
  simp only [mul_div_assoc, Finset.mul_sum]
  rw [← Finset.sum_div, Finset.sum_comm]
  have hinner (c : Bits n) :
      (∑ j : Bits n, walsh n b (g j) * (walsh n c (g j) * θ c)) =
        (if b = c then (2 : ℝ) ^ n else 0) * θ c := by
    simp only [← mul_assoc, ← Finset.sum_mul]
    rw [walsh_permuted_orthogonal]
  simp_rw [hinner]
  simp [eq_comm, pow_ne_zero]

#print axioms walsh_orthogonal
#print axioms walsh_permuted_orthogonal
#print axioms multiplexorAngles_recover

end
end FiniteReconstructionDesign
