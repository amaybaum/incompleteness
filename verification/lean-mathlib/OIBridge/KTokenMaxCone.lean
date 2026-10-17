/-
  OIBridge/KTokenMaxCone.lean — conditional k-token cone theorem (KTOKEN-MAXCONE-1).

  Real Pauli tables on k tokens. A set containing the products of `eball 3` states, closed under
  addition and nonnegative scaling, inside the k-fold maxCone, and invariant under CNOT into later
  tokens and the rotation flow and cyclic map off the first token, is the cone of tables with
  positive semidefinite k-fold Pauli dictionary image. The two inclusions, the equality, its
  converse with one witness per direction, and the k = 2 recovery of the pair theorem's statement
  are proved by exact pure-state reachability on the recursive carrier.

  The hypotheses retain their stated scope. The physical realization of the k-token carrier, its
  product tests and its operation-preserving actions has separate source obligations. Proof bodies
  follow the measured finite-reconstruction design sources.
-/
import OIBridge.EqvK2Generation

/-! ## Part 1 — finite tensor identities, recursive carriers and the Pauli dictionary
   No physical carrier identification or synthesis premise is supplied by these identities. -/
namespace OIBridge.KTokenMaxCone

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

scoped instance carrierDecidableEq (d n : ℕ) : DecidableEq (Carrier d n) :=
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
end OIBridge.KTokenMaxCone

/-! ## Part 2 — gates, words, multiplexors and exact pure-state reachability
   Exact pure-state reachability on the recursive k-token carrier from CNOT into later tokens and
   the third-axis flow and cyclic lift off the first token, and the two conditional cone inclusions
   at the Hermitian-matrix level. No physical carrier identification, state space or operation
   source is supplied. -/
namespace OIBridge.KTokenMaxCone

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation
open scoped ComplexOrder

noncomputable section

/-! ### §1 — the carrier, generic tensor facts and the block-diagonal family -/

/-- Square matrices on the recursive `n`-token carrier. -/
abbrev Mat (n : ℕ) := Matrix (Bits n) (Bits n) ℂ

/-- The unique word of the empty tensor. -/
def bitNil : Bits 0 := (0 : Fin 1)

/-- Structural decidable equality on the recursive binary carrier. At `n + 1` it unfolds to the
product instance, so the identity of a generic carrier specializes to the identity that is
synthesized for an explicit successor carrier. -/
def bitsDecEq : (n : ℕ) → DecidableEq (Bits n)
  | 0 => inferInstanceAs (DecidableEq (Fin 1))
  | n + 1 =>
    letI := bitsDecEq n
    inferInstanceAs (DecidableEq (Bits n × Fin 2))

attribute [scoped instance high] bitsDecEq

section Generic

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

theorem tensorK_smul_left (c : ℂ) (P : Matrix A A ℂ) (Q : Matrix B B ℂ) :
    tensorOf (c • P) Q = c • tensorOf P Q := by
  ext p q
  simp only [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  ring

theorem tensorK_smul_right (c : ℂ) (P : Matrix A A ℂ) (Q : Matrix B B ℂ) :
    tensorOf P (c • Q) = c • tensorOf P Q := by
  ext p q
  simp only [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  ring

theorem tensorK_vecMulVec (u : A → ℂ) (v : B → ℂ) :
    tensorOf (vecMulVec u (star u)) (vecMulVec v (star v)) =
      vecMulVec (fun p : A × B => u p.1 * v p.2) (star fun p : A × B => u p.1 * v p.2) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [tensorOf_apply, Matrix.vecMulVec_apply, Pi.star_apply, star_mul']
  ring

end Generic

/-- Conjugating the quadratic form by a matrix. -/
theorem quad_conj {ι : Type*} [Fintype ι] (U M : Matrix ι ι ℂ) (p : ι → ℂ) :
    star (U *ᵥ p) ⬝ᵥ (M *ᵥ (U *ᵥ p)) = star p ⬝ᵥ ((Uᴴ * M * U) *ᵥ p) := by
  simp only [Matrix.star_mulVec, Matrix.dotProduct_mulVec, Matrix.vecMul_vecMul,
    Matrix.mulVec_mulVec, Matrix.mul_assoc]

/-- Scaling the vector of a quadratic form. -/
theorem quad_smul {ι : Type*} [Fintype ι] (M : Matrix ι ι ℂ) (c : ℂ) (q : ι → ℂ) :
    star (c • q) ⬝ᵥ (M *ᵥ (c • q)) = star c * (star q ⬝ᵥ (M *ᵥ q)) * c := by
  rw [Matrix.mulVec_smul, star_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul]
  ring

/-- Conjugating a rank-one matrix. -/
theorem conjK_vecMulVec {ι : Type*} [Fintype ι] (U : Matrix ι ι ℂ) (y : ι → ℂ) :
    U * vecMulVec y (star y) * Uᴴ = vecMulVec (U *ᵥ y) (star (U *ᵥ y)) := by
  rw [Matrix.mul_vecMulVec, Matrix.vecMulVec_mul, Matrix.star_mulVec]

/-- A real scalar on the vector of a rank-one matrix comes out squared. -/
theorem vecMulVec_ofReal_smul {ι : Type*} (r : ℝ) (p : ι → ℂ) :
    vecMulVec (((r : ℝ) : ℂ) • p) (star (((r : ℝ) : ℂ) • p)) = (r ^ 2) • vecMulVec p (star p) := by
  ext i j
  simp only [Matrix.vecMulVec_apply, Pi.smul_apply, Pi.star_apply, smul_eq_mul, Matrix.smul_apply,
    star_mul', Complex.real_smul, Complex.ofReal_pow, Complex.star_def, Complex.conj_ofReal]
  ring

/-- `star c * z * c` is nonnegative when `z` is. -/
theorem star_mul_mul_nonneg (c z : ℂ) (hz : 0 ≤ z) : 0 ≤ star c * z * c := by
  obtain ⟨hre, him⟩ := Complex.nonneg_iff.mp hz
  obtain ⟨r, rfl⟩ : ∃ r : ℝ, z = (r : ℂ) :=
    ⟨z.re, Complex.ext (by simp) (by simp [← him])⟩
  have h : star c * (r : ℂ) * c = ((Complex.normSq c * r : ℝ) : ℂ) := by
    rw [Complex.ofReal_mul, Complex.normSq_eq_conj_mul_self, ← Complex.star_def]
    ring
  rw [h, Complex.zero_le_real]
  exact mul_nonneg (Complex.normSq_nonneg c) (by simpa using hre)

theorem one_pair (n : ℕ) (a b : Bits n) (i j : Fin 2) :
    (1 : Mat (n + 1)) (a, i) (b, j) = (1 : Mat n) a b * (1 : Matrix (Fin 2) (Fin 2) ℂ) i j := by
  by_cases ha : a = b
  · by_cases hi : i = j
    · rw [ha, hi]
      simp only [Matrix.one_apply_eq, mul_one]
    · have hne : ((a, i) : Bits (n + 1)) ≠ (b, j) := fun h => hi (congrArg Prod.snd h)
      rw [Matrix.one_apply_ne hne, Matrix.one_apply_ne hi, mul_zero]
  · have hne : ((a, i) : Bits (n + 1)) ≠ (b, j) := fun h => ha (congrArg Prod.fst h)
    rw [Matrix.one_apply_ne hne, Matrix.one_apply_ne ha, zero_mul]

theorem tensorK_one (n : ℕ) :
    tensorOf (1 : Mat n) (1 : Matrix (Fin 2) (Fin 2) ℂ) = (1 : Mat (n + 1)) := by
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [tensorOf_apply, one_pair]

/-- The block-diagonal matrix `∑_b |b⟩⟨b| ⊗ U_b`: the first `n` tokens control a one-token
matrix on token `n`. -/
def blockFam (n : ℕ) (U : Bits n → Matrix (Fin 2) (Fin 2) ℂ) : Mat (n + 1) :=
  Matrix.of fun p q => if p.1 = q.1 then U p.1 p.2 q.2 else 0

theorem blockFam_apply (n : ℕ) (U : Bits n → Matrix (Fin 2) (Fin 2) ℂ) (a b : Bits n)
    (i j : Fin 2) : blockFam n U (a, i) (b, j) = if a = b then U a i j else 0 := rfl

theorem blockFam_mul (n : ℕ) (U V : Bits n → Matrix (Fin 2) (Fin 2) ℂ) :
    blockFam n U * blockFam n V = blockFam n (fun b => U b * V b) := by
  ext ⟨a, i⟩ ⟨c, j⟩
  simp only [Matrix.mul_apply, Fintype.sum_prod_type, blockFam_apply]
  rw [Finset.sum_eq_single a]
  · by_cases h : a = c
    · subst h
      simp
    · simp [h]
  · intro x _ hx
    have hx' : a ≠ x := fun e => hx e.symm
    simp [hx']
  · intro h
    exact absurd (Finset.mem_univ a) h

theorem blockFam_const (n : ℕ) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    blockFam n (fun _ => V) = tensorOf (1 : Mat n) V := by
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [blockFam_apply, tensorOf_apply]
  by_cases h : a = b
  · subst h
    simp
  · simp [h, Matrix.one_apply_ne h]

theorem blockFam_conjTranspose (n : ℕ) (U : Bits n → Matrix (Fin 2) (Fin 2) ℂ) :
    (blockFam n U)ᴴ = blockFam n (fun b => (U b)ᴴ) := by
  ext ⟨a, i⟩ ⟨c, j⟩
  rw [Matrix.conjTranspose_apply, blockFam_apply, blockFam_apply]
  by_cases h : c = a
  · subst h
    simp [Matrix.conjTranspose_apply]
  · have h' : a ≠ c := fun e => h e.symm
    simp [h, h']

theorem blockFam_mulVec (n : ℕ) (U : Bits n → Matrix (Fin 2) (Fin 2) ℂ) (y : Bits (n + 1) → ℂ)
    (p : Bits (n + 1)) : (blockFam n U *ᵥ y) p = (U p.1 *ᵥ fun j => y (p.1, j)) p.2 := by
  rcases p with ⟨a, i⟩
  simp only [Matrix.mulVec, dotProduct, Fintype.sum_prod_type, blockFam_apply]
  rw [Finset.sum_eq_single a]
  · simp
  · intro x _ hx
    have hx' : a ≠ x := fun e => hx e.symm
    simp [hx']
  · intro h
    exact absurd (Finset.mem_univ a) h

/-- A matrix on `n` tokens, idle on an added last token. -/
def liftM (n : ℕ) (M : Mat n) : Mat (n + 1) := tensorOf M (1 : Matrix (Fin 2) (Fin 2) ℂ)

theorem liftM_mulVec (n : ℕ) (M : Mat n) (y : Bits n → ℂ) (w : Fin 2 → ℂ) :
    liftM n M *ᵥ (fun p : Bits (n + 1) => y p.1 * w p.2) =
      fun p : Bits (n + 1) => (M *ᵥ y) p.1 * w p.2 := by
  funext p
  rcases p with ⟨a, i⟩
  simp only [liftM, Matrix.mulVec, dotProduct, Fintype.sum_prod_type, tensorOf_apply,
    Finset.sum_mul]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [Fin.sum_univ_two]
  have hi : i = 0 ∨ i = 1 := by fin_cases i <;> simp
  rcases hi with rfl | rfl <;> simp <;> ring

/-! ### §2 — the generator matrices -/

/-- Bit `i` of a binary word; positions at or beyond the length read as `0`. -/
def bitAt : (n : ℕ) → ℕ → Bits n → Fin 2
  | 0, _, _ => 0
  | n + 1, i, b => if i = n then b.2 else bitAt n i b.1

theorem bitAt_succ (n i : ℕ) (p : Bits (n + 1)) :
    bitAt (n + 1) i p = if i = n then p.2 else bitAt n i p.1 := rfl

theorem bitAt_last (n : ℕ) (p : Bits (n + 1)) : bitAt (n + 1) n p = p.2 := by
  rw [bitAt_succ]
  exact if_pos rfl

theorem bitAt_lift {n i : ℕ} (hi : i < n) (p : Bits (n + 1)) :
    bitAt (n + 1) i p = bitAt n i p.1 := by
  rw [bitAt_succ]
  exact if_neg (by omega)

theorem fin2_cases (c : Fin 2) : c = 0 ∨ c = 1 := by
  fin_cases c <;> simp

/-- The target flip selected by a control bit. -/
def flipX (c : Fin 2) : Matrix (Fin 2) (Fin 2) ℂ := if c = 1 then Xm else 1

theorem flipX_zero : flipX 0 = 1 := if_neg (by decide)

theorem flipX_one : flipX 1 = Xm := if_pos rfl

theorem xm_conjTranspose : Xmᴴ = Xm := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Xm, Matrix.conjTranspose_apply]

theorem flipX_conjTranspose (c : Fin 2) : (flipX c)ᴴ = flipX c := by
  rcases fin2_cases c with rfl | rfl
  · rw [flipX_zero, Matrix.conjTranspose_one]
  · rw [flipX_one, xm_conjTranspose]

/-- `CNOT(i → j)` on `n` tokens: control token `i`, target token `j`. -/
def cnotM : (n : ℕ) → ℕ → ℕ → Mat n
  | 0, _, _ => 1
  | n + 1, i, j =>
    if j = n then blockFam n (fun b => flipX (bitAt n i b))
    else tensorOf (cnotM n i j) (1 : Matrix (Fin 2) (Fin 2) ℂ)

/-- The one-token matrix `V` on token `j` of `n` tokens. -/
def localM : (n : ℕ) → ℕ → Matrix (Fin 2) (Fin 2) ℂ → Mat n
  | 0, _, _ => 1
  | n + 1, j, V =>
    if j = n then tensorOf (1 : Mat n) V else tensorOf (localM n j V) (1 : Matrix (Fin 2) (Fin 2) ℂ)

theorem cnotM_succ (n i j : ℕ) :
    cnotM (n + 1) i j =
      if j = n then blockFam n (fun b => flipX (bitAt n i b))
      else tensorOf (cnotM n i j) (1 : Matrix (Fin 2) (Fin 2) ℂ) :=
  rfl

theorem localM_succ (n j : ℕ) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    localM (n + 1) j V =
      if j = n then tensorOf (1 : Mat n) V
      else tensorOf (localM n j V) (1 : Matrix (Fin 2) (Fin 2) ℂ) :=
  rfl

theorem cnotM_last (n i : ℕ) : cnotM (n + 1) i n = blockFam n (fun b => flipX (bitAt n i b)) := by
  rw [cnotM_succ]
  exact if_pos rfl

theorem cnotM_lift {n i j : ℕ} (hj : j < n) :
    cnotM (n + 1) i j = tensorOf (cnotM n i j) (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  rw [cnotM_succ]
  exact if_neg (by omega)

theorem localM_last (n : ℕ) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    localM (n + 1) n V = tensorOf (1 : Mat n) V := by
  rw [localM_succ]
  exact if_pos rfl

theorem localM_lift {n j : ℕ} (hj : j < n) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    localM (n + 1) j V = tensorOf (localM n j V) (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  rw [localM_succ]
  exact if_neg (by omega)

theorem localM_last_block (n : ℕ) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    localM (n + 1) n V = blockFam n (fun _ => V) := by
  rw [localM_last, blockFam_const]

theorem localM_mul (V W : Matrix (Fin 2) (Fin 2) ℂ) :
    ∀ n j : ℕ, localM n j (V * W) = localM n j V * localM n j W := by
  intro n
  induction n with
  | zero =>
    intro j
    show (1 : Mat 0) = (1 : Mat 0) * 1
    rw [Matrix.mul_one]
  | succ n ih =>
    intro j
    rw [localM_succ, localM_succ, localM_succ]
    by_cases h : j = n
    · simp only [if_pos h, tensor_mul, Matrix.mul_one]
    · simp only [if_neg h, tensor_mul, ih, Matrix.mul_one]

theorem localM_smul (z : ℂ) (V : Matrix (Fin 2) (Fin 2) ℂ) :
    ∀ {n j : ℕ}, j < n → localM n j (z • V) = z • localM n j V := by
  intro n
  induction n with
  | zero =>
    intro j hj
    exact absurd hj (Nat.not_lt_zero j)
  | succ n ih =>
    intro j hj
    rw [localM_succ, localM_succ]
    by_cases h : j = n
    · simp only [if_pos h]
      exact tensorK_smul_right z (1 : Mat n) V
    · simp only [if_neg h]
      have hj' : j < n := by omega
      rw [ih hj']
      exact tensorK_smul_left z (localM n j V) (1 : Matrix (Fin 2) (Fin 2) ℂ)

theorem localM_conjTranspose (V : Matrix (Fin 2) (Fin 2) ℂ) :
    ∀ n j : ℕ, (localM n j V)ᴴ = localM n j Vᴴ := by
  intro n
  induction n with
  | zero =>
    intro j
    show (1 : Mat 0)ᴴ = 1
    exact Matrix.conjTranspose_one
  | succ n ih =>
    intro j
    rw [localM_succ, localM_succ]
    by_cases h : j = n
    · simp only [if_pos h, tensor_star, Matrix.conjTranspose_one]
    · simp only [if_neg h, tensor_star, ih, Matrix.conjTranspose_one]

theorem cnotM_conjTranspose : ∀ n i j : ℕ, (cnotM n i j)ᴴ = cnotM n i j := by
  intro n
  induction n with
  | zero =>
    intro i j
    exact Matrix.conjTranspose_one
  | succ n ih =>
    intro i j
    rw [cnotM_succ]
    by_cases h : j = n
    · rw [if_pos h]
      exact (blockFam_conjTranspose n (fun b => flipX (bitAt n i b))).trans
        (congrArg (blockFam n) (funext fun b => flipX_conjTranspose (bitAt n i b)))
    · simp only [if_neg h, tensor_star, ih, Matrix.conjTranspose_one]

/-! ### §3 — words in the generators -/

/-- Finite products of unit scalars, `CNOT(i → j)` with `i < j`, and the third-axis phase flow
and the cyclic lift on every token `j > 0`. -/
inductive IsWord (n : ℕ) : Mat n → Prop
  | scalar (z : ℂ) (hz : star z * z = 1) : IsWord n (z • (1 : Mat n))
  | cnot (i j : ℕ) (hij : i < j) (hj : j < n) : IsWord n (cnotM n i j)
  | phase (j : ℕ) (h0 : 0 < j) (hj : j < n) (t : ℝ) :
      IsWord n (localM n j (phaseMat (Real.cos t) (Real.sin t)))
  | cyc (j : ℕ) (h0 : 0 < j) (hj : j < n) : IsWord n (localM n j cycMat)
  | one : IsWord n 1
  | mul {M N : Mat n} : IsWord n M → IsWord n N → IsWord n (M * N)

/-- `C` is carried into itself by conjugation with `U`. -/
def Pres {n : ℕ} (C : Set (Mat n)) (U : Mat n) : Prop := ∀ A ∈ C, U * A * Uᴴ ∈ C

theorem pres_one {n : ℕ} (C : Set (Mat n)) : Pres C 1 := by
  intro A hA
  rw [Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
  exact hA

theorem pres_mul {n : ℕ} {C : Set (Mat n)} {M N : Mat n} (hM : Pres C M) (hN : Pres C N) :
    Pres C (M * N) := by
  intro A hA
  have e : M * N * A * (M * N)ᴴ = M * (N * A * Nᴴ) * Mᴴ := by
    rw [Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]
  rw [e]
  exact hM _ (hN A hA)

theorem pres_scalar {n : ℕ} (C : Set (Mat n)) (z : ℂ) (hz : star z * z = 1) :
    Pres C (z • (1 : Mat n)) := by
  intro A hA
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul, hz,
    one_smul, Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
  exact hA

/-- Preservation under the named generators gives preservation under every word. -/
theorem pres_of_isWord {n : ℕ} {C : Set (Mat n)}
    (hH2 : ∀ i j : ℕ, i < j → j < n → Pres C (cnotM n i j))
    (hA : ∀ j : ℕ, 0 < j → j < n → ∀ t : ℝ,
      Pres C (localM n j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM n j cycMat))
    {U : Mat n} (hU : IsWord n U) : Pres C U := by
  induction hU with
  | scalar z hz => exact pres_scalar C z hz
  | cnot i j hij hj => exact hH2 i j hij hj
  | phase j h0 hj t => exact (hA j h0 hj t).1
  | cyc j h0 hj => exact (hA j h0 hj 0).2
  | one => exact pres_one C
  | mul _ _ ihM ihN => exact pres_mul ihM ihN

/-- Every inverse word is a word: the flow reverses its angle, the gate and the scalars are
closed, and the cyclic lift is inverted by its square up to sign. -/
theorem isWord_conjTranspose {n : ℕ} {U : Mat n} (hU : IsWord n U) : IsWord n Uᴴ := by
  induction hU with
  | scalar z hz =>
    rw [Matrix.conjTranspose_smul, Matrix.conjTranspose_one]
    exact IsWord.scalar (star z) (by rw [star_star, mul_comm]; exact hz)
  | cnot i j hij hj =>
    rw [cnotM_conjTranspose]
    exact IsWord.cnot i j hij hj
  | phase j h0 hj t =>
    have e : phaseMat (Real.cos t) (-Real.sin t) = phaseMat (Real.cos (-t)) (Real.sin (-t)) := by
      rw [Real.cos_neg, Real.sin_neg]
    rw [localM_conjTranspose, phaseMat_conjTranspose, e]
    exact IsWord.phase j h0 hj (-t)
  | cyc j h0 hj =>
    rw [localM_conjTranspose, cycMat_conjTranspose_eq, localM_smul (-1) _ hj, localM_mul]
    have e : (-1 : ℂ) • (localM n j cycMat * localM n j cycMat) =
        ((-1 : ℂ) • (1 : Mat n)) * (localM n j cycMat * localM n j cycMat) := by
      rw [Matrix.smul_mul, Matrix.one_mul]
    rw [e]
    exact IsWord.mul (IsWord.scalar (-1) (by simp))
      (IsWord.mul (IsWord.cyc j h0 hj) (IsWord.cyc j h0 hj))
  | one =>
    rw [Matrix.conjTranspose_one]
    exact IsWord.one
  | mul _ _ ihM ihN =>
    rw [Matrix.conjTranspose_mul]
    exact IsWord.mul ihN ihM

/-- **Spectator transport**: a word on `n` tokens, idle on an added last token, is a word on
`n + 1` tokens. -/
theorem isWord_lift {n : ℕ} {U : Mat n} (hU : IsWord n U) : IsWord (n + 1) (liftM n U) := by
  induction hU with
  | scalar z hz =>
    rw [liftM, tensorK_smul_left, tensorK_one]
    exact IsWord.scalar z hz
  | cnot i j hij hj =>
    rw [liftM, ← cnotM_lift hj]
    exact IsWord.cnot i j hij (Nat.lt_succ_of_lt hj)
  | phase j h0 hj t =>
    rw [liftM, ← localM_lift hj]
    exact IsWord.phase j h0 (Nat.lt_succ_of_lt hj) t
  | cyc j h0 hj =>
    rw [liftM, ← localM_lift hj]
    exact IsWord.cyc j h0 (Nat.lt_succ_of_lt hj)
  | one =>
    rw [liftM, tensorK_one]
    exact IsWord.one
  | @mul M N _ _ ihM ihN =>
    have e : liftM n (M * N) = liftM n M * liftM n N := by
      simp only [liftM, tensor_mul, Matrix.mul_one]
    rw [e]
    exact IsWord.mul ihM ihN

/-! ### §4 — exact multiplexors controlled by every earlier token -/

/-- `cos t + i sin t`. -/
def cisC (t : ℝ) : ℂ := (Real.cos t : ℂ) + (Real.sin t : ℂ) * Complex.I

theorem cisC_add (a b : ℝ) : cisC (a + b) = cisC a * cisC b := by
  simp only [cisC, Real.cos_add, Real.sin_add, Complex.ofReal_add, Complex.ofReal_sub,
    Complex.ofReal_mul]
  linear_combination (-((Real.sin a : ℂ) * (Real.sin b : ℂ))) * Complex.I_sq

theorem star_cisC (t : ℝ) : star (cisC t) = cisC (-t) := by
  simp only [cisC, Real.cos_neg, Real.sin_neg, Complex.ofReal_neg, Complex.star_def, map_add,
    map_mul, Complex.conj_ofReal, Complex.conj_I]
  ring

theorem cisC_unit (t : ℝ) : star (cisC t) * cisC t = 1 := by
  rw [star_cisC, ← cisC_add, show -t + t = (0 : ℝ) by ring]
  simp [cisC]

theorem exists_cisC {z : ℂ} (hz : star z * z = 1) : ∃ t : ℝ, cisC t = z := by
  have h2 : ((Complex.normSq z : ℝ) : ℂ) = 1 := by
    rw [Complex.normSq_eq_conj_mul_self, ← Complex.star_def]
    exact hz
  have h3 : Complex.normSq z = 1 := by exact_mod_cast h2
  rw [Complex.normSq_apply] at h3
  obtain ⟨t, hc, hs⟩ := exists_angle z.re z.im (by nlinarith [h3])
  refine ⟨t, ?_⟩
  show ((Real.cos t : ℝ) : ℂ) + ((Real.sin t : ℝ) : ℂ) * Complex.I = z
  rw [hc, hs]
  exact Complex.re_add_im z

theorem dUnit_mul (z w : ℂ) : dUnit z * dUnit w = dUnit (z * w) := by
  simp only [dUnit, Matrix.mul_fin_two, star_mul']
  refine mat2_ext ?_ ?_ ?_ ?_ <;> ring

theorem xm_dUnit_xm (z : ℂ) : Xm * dUnit z * Xm = dUnit (star z) := by
  simp only [Xm, dUnit, Matrix.mul_fin_two, star_star]
  refine mat2_ext ?_ ?_ ?_ ?_ <;> ring

/-- The diagonal one-parameter group `diag(e^{it}, e^{-it})`. -/
def rz (t : ℝ) : Matrix (Fin 2) (Fin 2) ℂ := dUnit (cisC t)

theorem rz_mul (a b : ℝ) : rz a * rz b = rz (a + b) := by
  simp only [rz]
  rw [dUnit_mul, cisC_add]

/-- The sign `(-1)^c` of a bit. -/
def bsign (c : Fin 2) : ℝ := if c = 1 then -1 else 1

theorem bsign_zero : bsign 0 = 1 := if_neg (by decide)

theorem bsign_one : bsign 1 = -1 := if_pos rfl

/-- The crossing law of the flip with the diagonal group. -/
theorem flipX_rz (c : Fin 2) (a : ℝ) : flipX c * rz a * flipX c = rz (bsign c * a) := by
  rcases fin2_cases c with rfl | rfl
  · rw [flipX_zero, bsign_zero, Matrix.one_mul, Matrix.mul_one, one_mul]
  · simp only [flipX_one, bsign_one, rz, xm_dUnit_xm, star_cisC, neg_one_mul]

theorem pred_congr {α : Sort*} (Q : α → Prop) {x y : α} (h : Q x) (e : x = y) : Q y := e ▸ h

/-- **Sign-character induction.** A predicate on real functions of `n` bits that is closed under
addition, holds for every constant, and is preserved by multiplication with the sign of each bit
holds for every function. Zero controls are the constant case. -/
theorem sign_induction : ∀ (n : ℕ) (Q : (Bits n → ℝ) → Prop),
    (∀ f g, Q f → Q g → Q (fun b => f b + g b)) →
    (∀ c : ℝ, Q (fun _ => c)) →
    (∀ i, i < n → ∀ f, Q f → Q (fun b => bsign (bitAt n i b) * f b)) →
    ∀ f, Q f := by
  intro n
  induction n with
  | zero =>
    intro Q _ hconst _ f
    exact pred_congr Q (hconst (f bitNil))
      (funext fun b => congrArg f (Subsingleton.elim bitNil b))
  | succ n ih =>
    intro Q hadd hconst hsign f
    have hQ := ih (fun u => Q (fun p => u p.1) ∧ Q (fun p => bsign p.2 * u p.1))
      (fun u w hu hw => ⟨hadd _ _ hu.1 hw.1,
        pred_congr Q (hadd _ _ hu.2 hw.2) (funext fun p => by (try dsimp only); ring)⟩)
      (fun c => ⟨hconst c, pred_congr Q (hsign n (Nat.lt_succ_self n) _ (hconst c))
        (funext fun p => by (try dsimp only); rw [bitAt_last])⟩)
      (fun i hi u hu => ⟨pred_congr Q (hsign i (Nat.lt_succ_of_lt hi) _ hu.1)
          (funext fun p => by (try dsimp only); rw [bitAt_lift hi]),
        pred_congr Q (hsign i (Nat.lt_succ_of_lt hi) _ hu.2)
          (funext fun p => by (try dsimp only); rw [bitAt_lift hi]; ring)⟩)
    have hu := (hQ (fun b => (f (b, 0) + f (b, 1)) / 2)).1
    have hv := (hQ (fun b => (f (b, 0) - f (b, 1)) / 2)).2
    refine pred_congr Q (hadd _ _ hu hv) (funext fun p => ?_)
    rcases p with ⟨b, c⟩
    rcases fin2_cases c with rfl | rfl
    · simp only [bsign_zero]
      ring
    · simp only [bsign_one]
      ring

/-- A diagonal special unitary on the last token is a word when that token is not the first. -/
theorem isWord_local_dUnit {n : ℕ} (hn : 0 < n) (z : ℂ) (hz : star z * z = 1) :
    IsWord (n + 1) (tensorOf (1 : Mat n) (dUnit z)) := by
  have hw : (star z ^ 2).re ^ 2 + (star z ^ 2).im ^ 2 = 1 := by
    have h1 : star (star z ^ 2) * star z ^ 2 = 1 := by
      rw [star_pow, star_star]
      linear_combination (star z * z + 1) * hz
    have h2 : ((Complex.normSq (star z ^ 2) : ℝ) : ℂ) = 1 := by
      rw [Complex.normSq_eq_conj_mul_self, ← Complex.star_def]
      exact h1
    have h3 : Complex.normSq (star z ^ 2) = 1 := by exact_mod_cast h2
    rw [Complex.normSq_apply] at h3
    nlinarith [h3]
  obtain ⟨t, hc, hs⟩ := exists_angle _ _ hw
  have h : IsWord (n + 1)
      ((z • (1 : Mat (n + 1))) * localM (n + 1) n (phaseMat (Real.cos t) (Real.sin t))) :=
    IsWord.mul (IsWord.scalar z hz) (IsWord.phase n hn (Nat.lt_succ_self n) t)
  rw [Matrix.smul_mul, Matrix.one_mul, localM_last, hc, hs] at h
  rw [dUnit_eq_smul z hz, tensorK_smul_right]
  exact h

/-- **Diagonal multiplexor.** Every family of diagonal rotations on token `n`, controlled by
tokens `0, …, n - 1`, is a word. -/
theorem isWord_rzFam {n : ℕ} (hn : 0 < n) (θ : Bits n → ℝ) :
    IsWord (n + 1) (blockFam n (fun b => rz (θ b))) := by
  refine sign_induction n (fun θ => IsWord (n + 1) (blockFam n (fun b => rz (θ b)))) ?_ ?_ ?_ θ
  · intro f g hf hg
    show IsWord (n + 1) (blockFam n (fun b => rz (f b + g b)))
    have e : blockFam n (fun b => rz (f b + g b)) =
        blockFam n (fun b => rz (f b)) * blockFam n (fun b => rz (g b)) := by
      rw [blockFam_mul]
      simp only [rz_mul]
    rw [e]
    exact IsWord.mul hf hg
  · intro c
    show IsWord (n + 1) (blockFam n (fun _ => rz c))
    rw [blockFam_const]
    exact isWord_local_dUnit hn (cisC c) (cisC_unit c)
  · intro i hi f hf
    show IsWord (n + 1) (blockFam n (fun b => rz (bsign (bitAt n i b) * f b)))
    have e : blockFam n (fun b => rz (bsign (bitAt n i b) * f b)) =
        cnotM (n + 1) i n * blockFam n (fun b => rz (f b)) * cnotM (n + 1) i n := by
      rw [cnotM_last, blockFam_mul, blockFam_mul]
      simp only [flipX_rz]
    rw [e]
    exact IsWord.mul (IsWord.mul (IsWord.cnot i n hi (Nat.lt_succ_self n)) hf)
      (IsWord.cnot i n hi (Nat.lt_succ_self n))

theorem isWord_dUnitFam {n : ℕ} (hn : 0 < n) (z : Bits n → ℂ) (hz : ∀ b, star (z b) * z b = 1) :
    IsWord (n + 1) (blockFam n (fun b => dUnit (z b))) := by
  choose θ hθ using fun b => exists_cisC (hz b)
  have e : blockFam n (fun b => dUnit (z b)) = blockFam n (fun b => rz (θ b)) :=
    congrArg (blockFam n) (funext fun b => by simp only [rz, hθ b])
  rw [e]
  exact isWord_rzFam hn θ

theorem isWord_rotReFam {n : ℕ} (hn : 0 < n) (c s : Bits n → ℝ)
    (hcs : ∀ b, c b ^ 2 + s b ^ 2 = 1) :
    IsWord (n + 1) (blockFam n (fun b => rotRe (c b) (s b))) := by
  have e : blockFam n (fun b => rotRe (c b) (s b)) =
      localM (n + 1) n cycMatᴴ *
        blockFam n (fun b => dUnit ((c b : ℂ) - (s b : ℂ) * Complex.I)) *
          localM (n + 1) n cycMat := by
    rw [localM_last_block, localM_last_block, blockFam_mul, blockFam_mul]
    simp only [rotRe_eq]
  rw [e]
  have hcyc : IsWord (n + 1) (localM (n + 1) n cycMat) := IsWord.cyc n hn (Nat.lt_succ_self n)
  have hcycH : IsWord (n + 1) (localM (n + 1) n cycMatᴴ) := by
    rw [← localM_conjTranspose]
    exact isWord_conjTranspose hcyc
  exact IsWord.mul (IsWord.mul hcycH
    (isWord_dUnitFam hn _ fun b => dphase_unit (c b) (s b) (hcs b))) hcyc

/-- **Special-unitary multiplexor.** Every family of special unitaries on token `n`, controlled by
tokens `0, …, n - 1`, is a word: the exact Euler factors of each branch, as three multiplexors in
circuit order. -/
theorem isWord_suFam {n : ℕ} (hn : 0 < n) (U : Bits n → Matrix (Fin 2) (Fin 2) ℂ)
    (hU : ∀ b, IsSU (U b)) : IsWord (n + 1) (blockFam n U) := by
  choose a b' ha hb' c s hcs hUe using fun x => su_euler (hU x)
  have e : blockFam n U = blockFam n (fun x => dUnit (a x)) *
      blockFam n (fun x => rotRe (c x) (s x)) * blockFam n (fun x => dUnit (b' x)) := by
    rw [blockFam_mul, blockFam_mul]
    exact congrArg (blockFam n) (funext hUe)
  rw [e]
  exact IsWord.mul (IsWord.mul (isWord_dUnitFam hn a ha) (isWord_rotReFam hn c s hcs))
    (isWord_dUnitFam hn b' hb')

/-! ### §5 — exact pure-state reachability -/

/-- The one-token vector `|0⟩`. -/
def ket0 : Fin 2 → ℂ := ![1, 0]

theorem ket0_unit : star ket0 ⬝ᵥ ket0 = 1 := by
  simp [ket0, dotProduct, Fin.sum_univ_two]

/-- The product vector of one-token vectors `a 0, …, a (n - 1)`. -/
def prodVec : (n : ℕ) → (ℕ → Fin 2 → ℂ) → Bits n → ℂ
  | 0, _ => fun _ => 1
  | n + 1, a => fun p => prodVec n a p.1 * a n p.2

theorem prodVec_zero (a : ℕ → Fin 2 → ℂ) (b : Bits 0) : prodVec 0 a b = 1 := rfl

theorem prodVec_succ (n : ℕ) (a : ℕ → Fin 2 → ℂ) (p : Bits (n + 1)) :
    prodVec (n + 1) a p = prodVec n a p.1 * a n p.2 := rfl

/-- The first token carries `a`; every later token carries `|0⟩`. -/
def padSeq (a : Fin 2 → ℂ) (i : ℕ) : Fin 2 → ℂ := if i = 0 then a else ket0

theorem padSeq_zero (a : Fin 2 → ℂ) : padSeq a 0 = a := if_pos rfl

theorem padSeq_succ (a : Fin 2 → ℂ) (i : ℕ) : padSeq a (i + 1) = ket0 :=
  if_neg (Nat.succ_ne_zero i)

theorem suTo_inv_mulVec (a : Fin 2 → ℂ) :
    (suTo a)ᴴ *ᵥ (fun j => ((nrm a : ℝ) : ℂ) * ket0 j) = a := by
  have h1 : (fun j => ((nrm a : ℝ) : ℂ) * ket0 j) = ![((nrm a : ℝ) : ℂ), 0] := by
    funext j
    fin_cases j <;> simp [ket0]
  have hu : (suTo a)ᴴ * suTo a = 1 := isSU_unitary (suTo_isSU a)
  rw [h1, ← suTo_mulVec a, Matrix.mulVec_mulVec, hu, Matrix.one_mulVec]

/-- **Exact reachability.** Every vector on `k + 1` tokens is a word applied to a product vector
whose first token is arbitrary and whose later tokens are `|0⟩`. The first token is never
driven; zero blocks use the identity branch. -/
theorem reach_prod : ∀ (k : ℕ) (x : Bits (k + 1) → ℂ),
    ∃ U : Mat (k + 1), IsWord (k + 1) U ∧
      ∃ a : Fin 2 → ℂ, x = U *ᵥ prodVec (k + 1) (padSeq a) := by
  intro k
  induction k with
  | zero =>
    intro x
    refine ⟨1, IsWord.one, fun j => x (bitNil, j), ?_⟩
    rw [Matrix.one_mulVec]
    funext p
    rcases p with ⟨b, j⟩
    have hb : b = bitNil := Subsingleton.elim b bitNil
    subst hb
    show x (bitNil, j) = 1 * padSeq (fun j => x (bitNil, j)) 0 j
    rw [padSeq_zero, one_mul]
  | succ k ih =>
    intro x
    obtain ⟨U', hU', a, hr⟩ := ih (fun b => ((nrm (fun j => x (b, j)) : ℝ) : ℂ))
    refine ⟨blockFam (k + 1) (fun b => (suTo (fun j => x (b, j)))ᴴ) * liftM (k + 1) U',
      IsWord.mul (isWord_suFam (Nat.succ_pos k) _
        fun b => isSU_conjTranspose (suTo_isSU (fun j => x (b, j)))) (isWord_lift hU'), a, ?_⟩
    have hpad : prodVec (k + 1 + 1) (padSeq a) =
        fun p : Bits (k + 1 + 1) => prodVec (k + 1) (padSeq a) p.1 * ket0 p.2 := by
      funext p
      rw [prodVec_succ (k + 1) (padSeq a) p, padSeq_succ]
    rw [← Matrix.mulVec_mulVec, hpad,
      liftM_mulVec (k + 1) U' (prodVec (k + 1) (padSeq a)) ket0, ← hr]
    funext p
    rw [blockFam_mulVec]
    rcases p with ⟨b, j⟩
    exact (congrFun (suTo_inv_mulVec (fun j' => x (b, j'))) j).symm

/-- The normalized first-token vector, `a = ‖a‖ • normz a`. -/
def normz (a : Fin 2 → ℂ) : Fin 2 → ℂ := (suTo a)ᴴ *ᵥ ket0

theorem normz_smul (a : Fin 2 → ℂ) : ((nrm a : ℝ) : ℂ) • normz a = a := by
  rw [normz, ← Matrix.mulVec_smul]
  exact suTo_inv_mulVec a

theorem normz_unit (a : Fin 2 → ℂ) : star (normz a) ⬝ᵥ normz a = 1 := by
  have hu : ((suTo a)ᴴ)ᴴ * (suTo a)ᴴ = 1 := isSU_unitary (isSU_conjTranspose (suTo_isSU a))
  have h := quad_conj (suTo a)ᴴ (1 : Matrix (Fin 2) (Fin 2) ℂ) ket0
  rw [Matrix.one_mulVec, Matrix.mul_one, hu, Matrix.one_mulVec, ket0_unit] at h
  exact h

theorem prodVec_padSeq_smul (c : ℂ) (a : Fin 2 → ℂ) : ∀ (k : ℕ) (p : Bits (k + 1)),
    prodVec (k + 1) (padSeq (c • a)) p = c * prodVec (k + 1) (padSeq a) p := by
  intro k
  induction k with
  | zero =>
    intro p
    rw [prodVec_succ 0 (padSeq (c • a)) p, prodVec_succ 0 (padSeq a) p, prodVec_zero, prodVec_zero,
      padSeq_zero, padSeq_zero, Pi.smul_apply, smul_eq_mul]
    ring
  | succ k ih =>
    intro p
    rw [prodVec_succ (k + 1) (padSeq (c • a)) p, prodVec_succ (k + 1) (padSeq a) p, ih p.1,
      padSeq_succ, padSeq_succ]
    ring

/-- Normalized reachability for every token count, including the scalar empty tensor: a word
applied to a nonnegative multiple of a product of unit one-token vectors. -/
theorem reach_norm : ∀ (k : ℕ) (x : Bits k → ℂ), ∃ U : Mat k, IsWord k U ∧ ∃ r : ℝ, 0 ≤ r ∧
    ∃ a : ℕ → Fin 2 → ℂ, (∀ i, star (a i) ⬝ᵥ a i = 1) ∧
      x = U *ᵥ (((r : ℝ) : ℂ) • prodVec k a) := by
  intro k
  cases k with
  | zero =>
    intro x
    obtain ⟨u, hu, hxu⟩ := polar_unit (x bitNil)
    refine ⟨u • (1 : Mat 0), IsWord.scalar u hu, ‖x bitNil‖, norm_nonneg _, fun _ => ket0,
      fun _ => ket0_unit, ?_⟩
    funext b
    have hb : b = bitNil := Subsingleton.elim b bitNil
    subst hb
    rw [Matrix.smul_mulVec, Matrix.one_mulVec]
    show x bitNil = u * (((‖x bitNil‖ : ℝ) : ℂ) * prodVec 0 (fun _ => ket0) bitNil)
    rw [prodVec_zero, mul_one, mul_comm]
    exact hxu
  | succ k =>
    intro x
    obtain ⟨U, hU, a, hx⟩ := reach_prod k x
    refine ⟨U, hU, nrm a, nrm_nonneg a, padSeq (normz a), ?_, ?_⟩
    · intro i
      cases i with
      | zero =>
        rw [padSeq_zero]
        exact normz_unit a
      | succ i =>
        rw [padSeq_succ]
        exact ket0_unit
    · have hv : prodVec (k + 1) (padSeq a) =
          ((nrm a : ℝ) : ℂ) • prodVec (k + 1) (padSeq (normz a)) := by
        funext p
        rw [Pi.smul_apply, smul_eq_mul, ← prodVec_padSeq_smul, normz_smul]
      rw [hx, hv]

/-! ### §6 — the two cone inclusions and the equivalence -/

/-- Products of one-token matrices. -/
def prodMat : (n : ℕ) → (ℕ → Matrix (Fin 2) (Fin 2) ℂ) → Mat n
  | 0, _ => 1
  | n + 1, ρ => tensorOf (prodMat n ρ) (ρ n)

theorem vecMulVec_prodVec (a : ℕ → Fin 2 → ℂ) : ∀ k : ℕ,
    vecMulVec (prodVec k a) (star (prodVec k a)) =
      prodMat k (fun i => vecMulVec (a i) (star (a i))) := by
  intro k
  induction k with
  | zero =>
    ext i j
    rw [Subsingleton.elim i j]
    show (1 : ℂ) * star (1 : ℂ) = (1 : Mat 0) j j
    rw [Matrix.one_apply_eq, star_one, mul_one]
  | succ k ih =>
    show vecMulVec (fun p : Bits k × Fin 2 => prodVec k a p.1 * a k p.2)
        (star fun p : Bits k × Fin 2 => prodVec k a p.1 * a k p.2) =
      tensorOf (prodMat k (fun i => vecMulVec (a i) (star (a i)))) (vecMulVec (a k) (star (a k)))
    rw [← ih, tensorK_vecMulVec]

theorem rank1_state (u : Fin 2 → ℂ) (hu : star u ⬝ᵥ u = 1) :
    (vecMulVec u (star u)).PosSemidef ∧ (vecMulVec u (star u)).trace = 1 :=
  ⟨Matrix.posSemidef_vecMulVec_self_star u, by
    rw [Matrix.trace_vecMulVec, dotProduct_comm]
    exact hu⟩

/-- The positive semidefinite cone on `k` tokens. -/
def psdSet (k : ℕ) : Set (Mat k) := {A | A.PosSemidef}

/-- **Upper inclusion.** Hermitian members with nonnegative expectation on every product vector, preserved
by the named generators, are positive semidefinite. Neither products in `C` nor cone closure is
used. -/
theorem subset_psd_of_maxCone_drive {k : ℕ} {C : Set (Mat k)}
    (hherm : ∀ A ∈ C, A.IsHermitian)
    (hmax : ∀ A ∈ C, ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a))
    (hH2 : ∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j))
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :
    C ⊆ psdSet k := by
  intro A hAC
  show A.PosSemidef
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg (hherm A hAC) fun x => ?_
  obtain ⟨U, hU, r, -, a, -, hx⟩ := reach_norm k x
  have hmem : Uᴴ * A * U ∈ C := by
    have h := pres_of_isWord hH2 hA (isWord_conjTranspose hU) A hAC
    rwa [Matrix.conjTranspose_conjTranspose] at h
  rw [hx, Matrix.mulVec_smul, quad_smul, quad_conj]
  exact star_mul_mul_nonneg _ _ (hmax _ hmem a)

/-- **Lower inclusion.** A set containing every product of trace-one positive one-token matrices, closed
under addition and nonnegative scaling and preserved by the named generators, contains every
positive semidefinite matrix. The product-test bound is not used. -/
theorem psd_subset_of_products_cone_drive {k : ℕ} {C : Set (Mat k)}
    (hprod : ∀ ρ : ℕ → Matrix (Fin 2) (Fin 2) ℂ,
      (∀ i, i < k → (ρ i).PosSemidef ∧ (ρ i).trace = 1) → prodMat k ρ ∈ C)
    (hadd : ∀ A ∈ C, ∀ B ∈ C, A + B ∈ C)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ C, c • A ∈ C)
    (hH2 : ∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j))
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :
    psdSet k ⊆ C := by
  have hpure : ∀ x : Bits k → ℂ, vecMulVec x (star x) ∈ C := by
    intro x
    obtain ⟨U, hU, r, -, a, ha, hx⟩ := reach_norm k x
    have h1 : vecMulVec (prodVec k a) (star (prodVec k a)) ∈ C := by
      rw [vecMulVec_prodVec]
      exact hprod _ fun i _ => rank1_state (a i) (ha i)
    have h2 := hsmul (r ^ 2) (sq_nonneg r) _ h1
    rw [← vecMulVec_ofReal_smul] at h2
    have h3 := pres_of_isWord hH2 hA hU _ h2
    rwa [conjK_vecMulVec, ← hx] at h3
  have hzero : (0 : Mat k) ∈ C := by
    have h := hsmul 0 le_rfl _ (hprod (fun _ => vecMulVec ket0 (star ket0))
      fun _ _ => rank1_state ket0 ket0_unit)
    rwa [zero_smul] at h
  intro A hApsd
  obtain ⟨B, hB⟩ := OIBridge.BoundaryAudit.psdFactorization_discharged (Bits k) A hApsd
  have hsum : A = ∑ j : Bits k, vecMulVec (fun i => B i j) (star fun i => B i j) := by
    rw [hB]
    ext i j
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  rw [hsum]
  exact Finset.sum_induction _ (· ∈ C) (fun a b ha hb => hadd a ha b hb) hzero
    (fun j _ => hpure _)

/-- **The conditional k-token cone theorem, matrix form.** -/
theorem kCone_eq_psd_of_drive_maxCone {k : ℕ} {C : Set (Mat k)}
    (hherm : ∀ A ∈ C, A.IsHermitian)
    (hprod : ∀ ρ : ℕ → Matrix (Fin 2) (Fin 2) ℂ,
      (∀ i, i < k → (ρ i).PosSemidef ∧ (ρ i).trace = 1) → prodMat k ρ ∈ C)
    (hadd : ∀ A ∈ C, ∀ B ∈ C, A + B ∈ C)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ C, c • A ∈ C)
    (hmax : ∀ A ∈ C, ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a))
    (hH2 : ∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j))
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :
    C = psdSet k :=
  Set.Subset.antisymm (subset_psd_of_maxCone_drive hherm hmax hH2 hA)
    (psd_subset_of_products_cone_drive hprod hadd hsmul hH2 hA)

theorem pres_psd {k : ℕ} (U : Mat k) : Pres (psdSet k) U := fun A hA =>
  Matrix.PosSemidef.mul_mul_conjTranspose_same (show A.PosSemidef from hA) U

/-- Forward witness: the positive semidefinite cone is preserved by every conjugation. -/
theorem driveInvariant_of_eq_psd {k : ℕ} {C : Set (Mat k)} (h : C = psdSet k) :
    (∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j)) ∧
      ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
        Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat) := by
  subst h
  exact ⟨fun i j _ _ => pres_psd _, fun j _ _ t => ⟨pres_psd _, pres_psd _⟩⟩

/-- Given the Hermitian carrier, products, cone closure and the product-test bound, equality with
the positive semidefinite cone is equivalent to preservation by the named generators.
Witnesses: `driveInvariant_of_eq_psd` and `kCone_eq_psd_of_drive_maxCone`. -/
theorem kCone_eq_psd_iff_drive_maxCone {k : ℕ} {C : Set (Mat k)}
    (hherm : ∀ A ∈ C, A.IsHermitian)
    (hprod : ∀ ρ : ℕ → Matrix (Fin 2) (Fin 2) ℂ,
      (∀ i, i < k → (ρ i).PosSemidef ∧ (ρ i).trace = 1) → prodMat k ρ ∈ C)
    (hadd : ∀ A ∈ C, ∀ B ∈ C, A + B ∈ C)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ C, c • A ∈ C)
    (hmax : ∀ A ∈ C, ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a)) :
    C = psdSet k ↔ ((∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j)) ∧
      ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
        Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :=
  ⟨driveInvariant_of_eq_psd, fun h =>
    kCone_eq_psd_of_drive_maxCone hherm hprod hadd hsmul hmax h.1 h.2⟩

#print axioms blockFam_mul
#print axioms isWord_conjTranspose
#print axioms isWord_lift
#print axioms sign_induction
#print axioms isWord_rzFam
#print axioms isWord_suFam
#print axioms reach_prod
#print axioms reach_norm
#print axioms subset_psd_of_maxCone_drive
#print axioms psd_subset_of_products_cone_drive
#print axioms kCone_eq_psd_of_drive_maxCone
#print axioms driveInvariant_of_eq_psd
#print axioms kCone_eq_psd_iff_drive_maxCone

end
end OIBridge.KTokenMaxCone

/-! ## Part 3 — real Pauli tables, the token-tuple statement surface and the k = 2 recovery
   Transport of the matrix-form k-token cone theorem to real Pauli tables on the recursive label
   carrier: products of ball states, product tests by forward-cone vectors and by products of ball
   effects, and the generator actions carried through the dictionary. The coordinate formulas of
   those actions, the `Fin`-indexed carriers, the statement surface and its k = 2 recovery are
   proved from §6 on; §12 proves that nonnegativity on product vectors gives the effect form of
   the product bound. No physical premise is supplied. -/
namespace OIBridge.KTokenMaxCone

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation OIBridge.CompositeDimension
open scoped ComplexOrder

noncomputable section

/-! ### §1 — product tables and the dictionary -/

/-- The product table of homogeneous one-token vectors `v 0, …, v (n - 1)`. -/
def prodTab : (n : ℕ) → (ℕ → HVec 3) → Labels n → ℝ
  | 0, _ => fun _ => 1
  | n + 1, v => fun μ => prodTab n v μ.1 * v n μ.2

theorem prodTab_succ (n : ℕ) (v : ℕ → HVec 3) (μ : Labels (n + 1)) :
    prodTab (n + 1) v μ = prodTab n v μ.1 * v n μ.2 := rfl

theorem prodTab_congr {v v' : ℕ → HVec 3} :
    ∀ n : ℕ, (∀ i, i < n → v i = v' i) → prodTab n v = prodTab n v' := by
  intro n
  induction n with
  | zero =>
    intro _
    rfl
  | succ n ih =>
    intro h
    funext μ
    rw [prodTab_succ, prodTab_succ, ih (fun i hi => h i (Nat.lt_succ_of_lt hi)),
      h n (Nat.lt_succ_self n)]

theorem prodMat_succ (n : ℕ) (ρ : ℕ → Matrix (Fin 2) (Fin 2) ℂ) :
    prodMat (n + 1) ρ = tensorOf (prodMat n ρ) (ρ n) := rfl

/-- **The dictionary of a product table is the product of the one-token matrices.** -/
theorem dictionary_prodTab (v : ℕ → HVec 3) : ∀ n : ℕ,
    dictionary n (prodTab n v) = prodMat n (fun i => tokMat (v i)) := by
  intro n
  induction n with
  | zero =>
    ext a b
    rw [Subsingleton.elim a b]
    simp [dictionary, complexDictionary, prodTab, pauliWord, prodMat, Matrix.sum_apply,
      Matrix.smul_apply, Matrix.one_apply_eq]
  | succ n ih =>
    rw [prodMat_succ, ← ih]
    ext ⟨a, i⟩ ⟨b, j⟩
    simp only [dictionary, complexDictionary, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul,
      Fintype.sum_prod_type, pauliWord, tensorOf_apply, prodTab_succ, tokMat, Complex.ofReal_mul,
      pow_succ]
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
    ring

/-- The trace pairing of two dictionary images is the table pairing over `2 ^ n`. -/
theorem trace_dictionary_mul (n : ℕ) (v w : Labels n → ℝ) :
    Matrix.trace (dictionary n v * dictionary n w) =
      ((∑ μ, v μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ n := by
  calc Matrix.trace (dictionary n v * dictionary n w)
      = ∑ μ, ((v μ : ℂ) / (2 : ℂ) ^ n) * Matrix.trace (pauliWord n μ * dictionary n w) := by
        simp only [dictionary, complexDictionary, Finset.sum_mul, Matrix.smul_mul,
          Matrix.trace_sum, Matrix.trace_smul, smul_eq_mul]
    _ = ∑ μ, ((v μ : ℂ) / (2 : ℂ) ^ n) * (w μ : ℂ) := by
        refine Finset.sum_congr rfl fun μ _ => ?_
        have h := congrFun (coordinates_dictionary n (fun ν => (w ν : ℂ))) μ
        exact congrArg (fun z => ((v μ : ℂ) / (2 : ℂ) ^ n) * z) h
    _ = ((∑ μ, v μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ n := by
        push_cast
        rw [Finset.sum_div]
        refine Finset.sum_congr rfl fun μ _ => ?_
        ring

theorem coordinates_add (n : ℕ) (A B : Mat n) :
    coordinates n (A + B) = coordinates n A + coordinates n B := by
  funext μ
  simp only [coordinates, complexCoordinates, Matrix.mul_add, Matrix.trace_add, Complex.add_re,
    Pi.add_apply]

theorem coordinates_smul (n : ℕ) (c : ℝ) (A : Mat n) :
    coordinates n (c • A) = c • coordinates n A := by
  funext μ
  simp only [coordinates, complexCoordinates, Matrix.mul_smul, Matrix.trace_smul, Pi.smul_apply,
    smul_eq_mul, Complex.real_smul, Complex.re_ofReal_mul]

/-! ### §2 — one-token Bloch vectors -/

/-- The homogeneous Bloch vector of a one-token vector. -/
def blochH (u : Fin 2 → ℂ) : HVec 3 :=
  ![Complex.normSq (u 0) + Complex.normSq (u 1), 2 * (star (u 0) * u 1).re,
    2 * (star (u 0) * u 1).im, Complex.normSq (u 0) - Complex.normSq (u 1)]

theorem blochH_apply_zero (u : Fin 2 → ℂ) :
    blochH u 0 = Complex.normSq (u 0) + Complex.normSq (u 1) := rfl

theorem blochH_apply_one (u : Fin 2 → ℂ) : blochH u 1 = 2 * (star (u 0) * u 1).re := rfl

theorem blochH_apply_two (u : Fin 2 → ℂ) : blochH u 2 = 2 * (star (u 0) * u 1).im := rfl

theorem blochH_apply_three (u : Fin 2 → ℂ) :
    blochH u 3 = Complex.normSq (u 0) - Complex.normSq (u 1) := rfl

/-- The rank-one matrix of every one-token vector is the dictionary image of its Bloch vector. -/
theorem tokMat_blochH (u : Fin 2 → ℂ) : tokMat (blochH u) = vecMulVec u (star u) := by
  rw [tokMat_eq, blochH_apply_zero, blochH_apply_one, blochH_apply_two, blochH_apply_three]
  ext i j
  fin_cases i <;> fin_cases j <;> apply Complex.ext <;>
    simp [Matrix.vecMulVec_apply, Complex.normSq_apply, Complex.mul_re, Complex.mul_im,
      Complex.star_def] <;> ring

/-- Bloch vectors lie on the boundary of the forward cone. -/
theorem lor_blochH (u : Fin 2 → ℂ) : Lor (blochH u) := by
  show 0 ≤ blochH u 0 ∧ ∑ j : Fin 3, blochH u j.succ ^ 2 ≤ blochH u 0 ^ 2
  refine ⟨?_, ?_⟩
  · show 0 ≤ Complex.normSq (u 0) + Complex.normSq (u 1)
    exact add_nonneg (Complex.normSq_nonneg _) (Complex.normSq_nonneg _)
  · rw [Fin.sum_univ_three]
    show (2 * (star (u 0) * u 1).re) ^ 2 + (2 * (star (u 0) * u 1).im) ^ 2 +
        (Complex.normSq (u 0) - Complex.normSq (u 1)) ^ 2 ≤
      (Complex.normSq (u 0) + Complex.normSq (u 1)) ^ 2
    apply le_of_eq
    simp only [Complex.normSq_apply, Complex.mul_re, Complex.mul_im, Complex.star_def,
      Complex.conj_re, Complex.conj_im]
    ring

theorem blochH_zero_of_unit {u : Fin 2 → ℂ} (hu : star u ⬝ᵥ u = 1) : blochH u 0 = 1 := by
  have h : ((blochH u 0 : ℝ) : ℂ) = star u ⬝ᵥ u := by
    show ((Complex.normSq (u 0) + Complex.normSq (u 1) : ℝ) : ℂ) = star u ⬝ᵥ u
    rw [Complex.ofReal_add, Complex.normSq_eq_conj_mul_self, Complex.normSq_eq_conj_mul_self]
    simp only [dotProduct, Fin.sum_univ_two, Pi.star_apply, Complex.star_def]
  rw [hu] at h
  exact_mod_cast h

/-- The ball point of a one-token vector. -/
def blochX (u : Fin 2 → ℂ) : Fin 3 → ℝ := fun j => blochH u j.succ

theorem hom_blochX {u : Fin 2 → ℂ} (hu : blochH u 0 = 1) : hom (blochX u) = blochH u := by
  funext μ
  refine Fin.cases ?_ (fun j => ?_) μ
  · exact hu.symm
  · rfl

theorem blochX_mem_eball {u : Fin 2 → ℂ} (hu : blochH u 0 = 1) :
    blochX u ∈ OIBridge.TransitiveBody.eball 3 := by
  show ∑ j : Fin 3, blochX u j ^ 2 ≤ 1
  have h := (lor_blochH u).2
  rw [hu, one_pow] at h
  exact h

/-- The trace of a rank-one matrix against a matrix is the quadratic form. -/
theorem trace_rank1_mul {ι : Type*} [Fintype ι] (p : ι → ℂ) (D : Matrix ι ι ℂ) :
    Matrix.trace (vecMulVec p (star p) * D) = star p ⬝ᵥ (D *ᵥ p) := by
  rw [Matrix.vecMulVec_mul, Matrix.trace_vecMulVec, dotProduct_comm p (star p ᵥ* D),
    ← Matrix.dotProduct_mulVec]

/-- **Product tests.** The expectation of a dictionary image on a product vector is the pairing of
its table with the product table of the Bloch vectors. -/
theorem quad_dictionary_prodVec (k : ℕ) (a : ℕ → Fin 2 → ℂ) (w : Labels k → ℝ) :
    star (prodVec k a) ⬝ᵥ (dictionary k w *ᵥ prodVec k a) =
      ((∑ μ, prodTab k (fun i => blochH (a i)) μ * w μ : ℝ) : ℂ) / (2 : ℂ) ^ k := by
  rw [← trace_rank1_mul, vecMulVec_prodVec,
    show (fun i => vecMulVec (a i) (star (a i))) = fun i => tokMat (blochH (a i)) from
      funext fun i => (tokMat_blochH (a i)).symm,
    ← dictionary_prodTab, trace_dictionary_mul]

/-! ### §3 — the pure-product lower inclusion -/

/-- **Lower inclusion from pure products.** Rank-one products of unit one-token vectors suffice. -/
theorem psd_subset_of_pure_cone_drive {k : ℕ} {C : Set (Mat k)}
    (hpure : ∀ a : ℕ → Fin 2 → ℂ, (∀ i, i < k → star (a i) ⬝ᵥ a i = 1) →
      vecMulVec (prodVec k a) (star (prodVec k a)) ∈ C)
    (hadd : ∀ A ∈ C, ∀ B ∈ C, A + B ∈ C)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ C, c • A ∈ C)
    (hH2 : ∀ i j : ℕ, i < j → j < k → Pres C (cnotM k i j))
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres C (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧ Pres C (localM k j cycMat)) :
    psdSet k ⊆ C := by
  have hrank : ∀ x : Bits k → ℂ, vecMulVec x (star x) ∈ C := by
    intro x
    obtain ⟨U, hU, r, -, a, ha, hx⟩ := reach_norm k x
    have h2 := hsmul (r ^ 2) (sq_nonneg r) _ (hpure a fun i _ => ha i)
    rw [← vecMulVec_ofReal_smul] at h2
    have h3 := pres_of_isWord hH2 hA hU _ h2
    rwa [conjK_vecMulVec, ← hx] at h3
  have hzero : (0 : Mat k) ∈ C := by
    have h := hsmul 0 le_rfl _ (hpure (fun _ => ket0) fun _ _ => ket0_unit)
    rwa [zero_smul] at h
  intro A hApsd
  obtain ⟨B, hB⟩ := OIBridge.BoundaryAudit.psdFactorization_discharged (Bits k) A hApsd
  have hsum : A = ∑ j : Bits k, vecMulVec (fun i => B i j) (star fun i => B i j) := by
    rw [hB]
    ext i j
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  rw [hsum]
  exact Finset.sum_induction _ (· ∈ C) (fun a b ha hb => hadd a ha b hb) hzero
    (fun j _ => hrank _)

/-! ### §4 — the table form of the conditional k-token cone theorem -/

/-- The table carried by conjugation with `U` through the dictionary. -/
def tabAct (k : ℕ) (U : Mat k) (w : Labels k → ℝ) : Labels k → ℝ :=
  coordinates k (U * dictionary k w * Uᴴ)

/-- The Hermitian matrices whose tables lie in `K`. -/
def matCone (k : ℕ) (K : Set (Labels k → ℝ)) : Set (Mat k) :=
  {A | A.IsHermitian ∧ coordinates k A ∈ K}

theorem mem_matCone {k : ℕ} {K : Set (Labels k → ℝ)} {A : Mat k} :
    A ∈ matCone k K ↔ A.IsHermitian ∧ coordinates k A ∈ K := Iff.rfl

/-- **The conditional k-token cone theorem, table form.** A set of real Pauli tables containing
the product tables of ball states, closed under addition and nonnegative scaling, nonnegative on
every product of forward-cone vectors, and carried into itself by the CNOT, third-axis flow and
cyclic actions through the dictionary, is the set of tables with positive semidefinite
dictionary image. -/
theorem tableCone_eq_psd_of_drive_maxCone {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : ∀ w ∈ K, ∀ v : ℕ → HVec 3, (∀ i, i < k → Lor (v i)) →
      0 ≤ ∑ μ, prodTab k v μ * w μ)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    K = {w | (dictionary k w).PosSemidef} := by
  have mem_C : ∀ w, w ∈ K → dictionary k w ∈ matCone k K := fun w hw =>
    mem_matCone.mpr ⟨dictionary_hermitian k w, by rw [coordinates_dictionary_real]; exact hw⟩
  have hpresC : ∀ U : Mat k, (∀ w ∈ K, tabAct k U w ∈ K) → Pres (matCone k K) U := by
    intro U hU A hA'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    refine mem_matCone.mpr ⟨Matrix.isHermitian_mul_mul_conjTranspose U hAh, ?_⟩
    have h := hU _ hAK
    rwa [tabAct, dictionary_coordinates_real k A hAh] at h
  have hH2C : ∀ i j : ℕ, i < j → j < k → Pres (matCone k K) (cnotM k i j) :=
    fun i j hij hj => hpresC _ (hH2 i j hij hj)
  have hAC : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ,
      Pres (matCone k K) (localM k j (phaseMat (Real.cos t) (Real.sin t))) ∧
        Pres (matCone k K) (localM k j cycMat) :=
    fun j h0 hj t => ⟨hpresC _ fun w hw => (hA j h0 hj t w hw).1,
      hpresC _ fun w hw => (hA j h0 hj t w hw).2⟩
  have hmaxC : ∀ A ∈ matCone k K, ∀ a : ℕ → Fin 2 → ℂ,
      0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) := by
    intro A hA' a
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    rw [← dictionary_coordinates_real k A hAh, quad_dictionary_prodVec]
    have hS := hmax _ hAK (fun i => blochH (a i)) fun i _ => lor_blochH (a i)
    rw [show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
        (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
          2 ^ k : ℝ) : ℂ) by push_cast; ring,
      Complex.zero_le_real]
    exact div_nonneg hS (pow_nonneg (by norm_num) k)
  have hpureC : ∀ a : ℕ → Fin 2 → ℂ, (∀ i, i < k → star (a i) ⬝ᵥ a i = 1) →
      vecMulVec (prodVec k a) (star (prodVec k a)) ∈ matCone k K := by
    intro a ha
    rw [vecMulVec_prodVec,
      show (fun i => vecMulVec (a i) (star (a i))) = fun i => tokMat (blochH (a i)) from
        funext fun i => (tokMat_blochH (a i)).symm,
      ← dictionary_prodTab]
    apply mem_C
    rw [prodTab_congr k fun i hi => (hom_blochX (blochH_zero_of_unit (ha i hi))).symm]
    exact hH1 _ fun i hi => blochX_mem_eball (blochH_zero_of_unit (ha i hi))
  have haddC : ∀ A ∈ matCone k K, ∀ B ∈ matCone k K, A + B ∈ matCone k K := by
    intro A hA' B hB'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    obtain ⟨hBh, hBK⟩ := mem_matCone.mp hB'
    refine mem_matCone.mpr ⟨hAh.add hBh, ?_⟩
    rw [coordinates_add]
    exact hadd _ hAK _ hBK
  have hsmulC : ∀ c : ℝ, 0 ≤ c → ∀ A ∈ matCone k K, c • A ∈ matCone k K := by
    intro c hc A hA'
    obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
    refine mem_matCone.mpr ⟨?_, ?_⟩
    · show (c • A)ᴴ = c • A
      rw [Matrix.conjTranspose_smul, star_trivial, hAh.eq]
    · rw [coordinates_smul]
      exact hsmul c hc _ hAK
  have hCeq : matCone k K = psdSet k :=
    Set.Subset.antisymm
      (subset_psd_of_maxCone_drive (fun A hA' => (mem_matCone.mp hA').1) hmaxC hH2C hAC)
      (psd_subset_of_pure_cone_drive hpureC haddC hsmulC hH2C hAC)
  ext w
  constructor
  · intro hw
    have h := mem_C w hw
    rw [hCeq] at h
    exact h
  · intro hw
    have h : dictionary k w ∈ matCone k K := by
      rw [hCeq]
      exact hw
    have h2 := (mem_matCone.mp h).2
    rwa [coordinates_dictionary_real] at h2

/-! ### §5 — the effect form of the product tests and the equivalence -/

/-- The scale that turns a forward-cone vector into the homogeneous vector of an effect. -/
def lorScale (v : HVec 3) : ℝ := 1 / (2 * (v 0 + 1))

theorem lorScale_pos {v : HVec 3} (hv : Lor v) : 0 < lorScale v :=
  div_pos one_pos (by linarith [hv.1])

theorem isEffectOn_lorScale {v : HVec 3} (hv : Lor v) :
    OIBridge.KInfFoundations.IsEffectOn (OIBridge.TransitiveBody.eball 3)
      (affOf (lorScale v • v)) := by
  have hp : 0 < 2 * (v 0 + 1) := by linarith [hv.1]
  have hc0 : 0 < 1 / (2 * (v 0 + 1)) := div_pos one_pos hp
  have hc1 : 1 / (2 * (v 0 + 1)) * (2 * (v 0 + 1)) = 1 := one_div_mul_cancel (ne_of_gt hp)
  refine isEffectOn_affOf (lor_smul hv hc0.le) ?_
  show 1 / (2 * (v 0 + 1)) * v 0 ≤ 1 / 2
  linarith

theorem prodTab_lorScale (v : ℕ → HVec 3) : ∀ (n : ℕ) (μ : Labels n),
    prodTab n (fun i => lorScale (v i) • v i) μ =
      (∏ i ∈ Finset.range n, lorScale (v i)) * prodTab n v μ := by
  intro n
  induction n with
  | zero =>
    intro μ
    simp [prodTab]
  | succ n ih =>
    intro μ
    simp only [prodTab_succ, ih, Finset.prod_range_succ, Pi.smul_apply, smul_eq_mul]
    ring

/-- The k-fold maximal cone of the ball on real Pauli tables: nonnegative on every product of
effects. -/
def maxConeTab (k : ℕ) : Set (Labels k → ℝ) :=
  {w | ∀ e : ℕ → (Fin 3 → ℝ) →ᵃ[ℝ] ℝ,
    (∀ i, i < k → OIBridge.KInfFoundations.IsEffectOn (OIBridge.TransitiveBody.eball 3) (e i)) →
      0 ≤ ∑ μ, prodTab k (fun i => ehom (e i)) μ * w μ}

/-- **Product effects give the forward-cone product tests.** -/
theorem lorPair_nonneg_of_maxConeTab {k : ℕ} {w : Labels k → ℝ} (hw : w ∈ maxConeTab k)
    {v : ℕ → HVec 3} (hv : ∀ i, i < k → Lor (v i)) : 0 ≤ ∑ μ, prodTab k v μ * w μ := by
  have hP : 0 < ∏ i ∈ Finset.range k, lorScale (v i) :=
    Finset.prod_pos fun i hi => lorScale_pos (hv i (Finset.mem_range.mp hi))
  have hsum : ∑ μ, prodTab k (fun i => ehom (affOf (lorScale (v i) • v i))) μ * w μ =
      (∏ i ∈ Finset.range k, lorScale (v i)) * ∑ μ, prodTab k v μ * w μ := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun μ _ => ?_
    simp only [ehom_affOf]
    rw [prodTab_lorScale v k μ]
    ring
  have h : 0 ≤ ∑ μ, prodTab k (fun i => ehom (affOf (lorScale (v i) • v i))) μ * w μ :=
    hw (fun i => affOf (lorScale (v i) • v i)) fun i hi => isEffectOn_lorScale (hv i hi)
  rw [hsum] at h
  have h2 : (∏ i ∈ Finset.range k, lorScale (v i)) * 0 ≤
      (∏ i ∈ Finset.range k, lorScale (v i)) * ∑ μ, prodTab k v μ * w μ := by
    rw [mul_zero]
    exact h
  exact le_of_mul_le_mul_left h2 hP

/-- **The table theorem with the effect-form product bound.** -/
theorem tableCone_eq_psd_of_drive_maxConeTab {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : K ⊆ maxConeTab k)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    K = {w | (dictionary k w).PosSemidef} :=
  tableCone_eq_psd_of_drive_maxCone hH1 hadd hsmul
    (fun w hw v hv => lorPair_nonneg_of_maxConeTab (hmax hw) hv) hH2 hA

theorem tabAct_psd {k : ℕ} (U : Mat k) {w : Labels k → ℝ} (hw : (dictionary k w).PosSemidef) :
    (dictionary k (tabAct k U w)).PosSemidef := by
  rw [tabAct, dictionary_coordinates_real k _
    (Matrix.isHermitian_mul_mul_conjTranspose U (dictionary_hermitian k w))]
  exact hw.mul_mul_conjTranspose_same U

/-- Forward witness: the positive semidefinite tables are carried into themselves by every
action through the dictionary. -/
theorem tableDrive_of_eq_psd {k : ℕ} {K : Set (Labels k → ℝ)}
    (h : K = {w | (dictionary k w).PosSemidef}) :
    (∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K) ∧
      ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
        tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
          tabAct k (localM k j cycMat) w ∈ K := by
  subst h
  exact ⟨fun i j _ _ w hw => tabAct_psd _ hw,
    fun j _ _ t w hw => ⟨tabAct_psd _ hw, tabAct_psd _ hw⟩⟩

/-- Given products of ball states, cone closure and the effect-form product bound, equality with
the positive semidefinite tables is equivalent to invariance under the named actions.
Witnesses: `tableDrive_of_eq_psd` and `tableCone_eq_psd_of_drive_maxConeTab`. -/
theorem tableCone_eq_psd_iff_drive_maxConeTab {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hmax : K ⊆ maxConeTab k) :
    K = {w | (dictionary k w).PosSemidef} ↔
      ((∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K) ∧
        ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
          tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
            tabAct k (localM k j cycMat) w ∈ K) :=
  ⟨tableDrive_of_eq_psd, fun h =>
    tableCone_eq_psd_of_drive_maxConeTab hH1 hadd hsmul hmax h.1 h.2⟩

#print axioms dictionary_prodTab
#print axioms trace_dictionary_mul
#print axioms tokMat_blochH
#print axioms lor_blochH
#print axioms quad_dictionary_prodVec
#print axioms psd_subset_of_pure_cone_drive
#print axioms tableCone_eq_psd_of_drive_maxCone
#print axioms lorPair_nonneg_of_maxConeTab
#print axioms tableCone_eq_psd_of_drive_maxConeTab
#print axioms tableDrive_of_eq_psd
#print axioms tableCone_eq_psd_iff_drive_maxConeTab

/-! ### §6 — the `Fin`-indexed carriers -/

/-- The token tuple of a recursive word: token `n` of `Carrier d (n + 1)` is the last component
and token `t < n` is token `t` of the prefix. -/
def toTup {d : ℕ} : (n : ℕ) → Carrier d n → Fin n → Fin d
  | 0, _ => fun t => Fin.elim0 t
  | n + 1, p => Fin.snoc (α := fun _ => Fin d) (toTup n p.1) p.2

/-- The recursive word of a token tuple. -/
def ofTup {d : ℕ} : (n : ℕ) → (Fin n → Fin d) → Carrier d n
  | 0, _ => (0 : Fin 1)
  | n + 1, f => (ofTup n (fun t => f t.castSucc), f (Fin.last n))

theorem toTup_succ {d : ℕ} (n : ℕ) (p : Carrier d (n + 1)) :
    toTup (n + 1) p = Fin.snoc (α := fun _ => Fin d) (toTup n p.1) p.2 := rfl

theorem toTup_last {d : ℕ} (n : ℕ) (p : Carrier d (n + 1)) :
    toTup (n + 1) p (Fin.last n) = p.2 := by
  rw [toTup_succ, Fin.snoc_last]

theorem toTup_castSucc {d : ℕ} (n : ℕ) (p : Carrier d (n + 1)) (t : Fin n) :
    toTup (n + 1) p t.castSucc = toTup n p.1 t := by
  rw [toTup_succ, Fin.snoc_castSucc]

theorem ofTup_toTup {d : ℕ} : ∀ (n : ℕ) (p : Carrier d n), ofTup n (toTup n p) = p
  | 0, _ => Subsingleton.elim _ _
  | n + 1, p => by
    rcases p with ⟨a, x⟩
    have h : (fun t : Fin n => toTup (n + 1) ((a, x) : Carrier d (n + 1)) t.castSucc) =
        toTup n a := funext fun t => toTup_castSucc n (a, x) t
    show (ofTup n (fun t : Fin n => toTup (n + 1) ((a, x) : Carrier d (n + 1)) t.castSucc),
      toTup (n + 1) ((a, x) : Carrier d (n + 1)) (Fin.last n)) = ((a, x) : Carrier d (n + 1))
    rw [h, ofTup_toTup n a, toTup_last]

theorem toTup_ofTup {d : ℕ} : ∀ (n : ℕ) (f : Fin n → Fin d), toTup n (ofTup n f) = f
  | 0, _ => funext fun t => Fin.elim0 t
  | n + 1, f => by
    show Fin.snoc (α := fun _ => Fin d) (toTup n (ofTup n (fun t => f t.castSucc)))
      (f (Fin.last n)) = f
    rw [toTup_ofTup n]
    exact Fin.snoc_init_self f

/-- **The carrier equivalence**: recursive words are token tuples. -/
def carrierEquiv (d n : ℕ) : Carrier d n ≃ (Fin n → Fin d) where
  toFun := toTup n
  invFun := ofTup n
  left_inv := ofTup_toTup n
  right_inv := toTup_ofTup n

theorem carrierEquiv_apply (d n : ℕ) (p : Carrier d n) : carrierEquiv d n p = toTup n p := rfl

/-- The token tuple of a binary word reads its bits. -/
theorem bitAt_eq_toTup : ∀ (n t : ℕ) (ht : t < n) (p : Bits n), bitAt n t p = toTup n p ⟨t, ht⟩
  | 0, t, ht, _ => absurd ht (Nat.not_lt_zero t)
  | n + 1, t, ht, p => by
    rw [bitAt_succ]
    by_cases h : t = n
    · rw [if_pos h, show (⟨t, ht⟩ : Fin (n + 1)) = Fin.last n from Fin.ext h, toTup_last]
    · have ht' : t < n := by omega
      rw [if_neg h, show (⟨t, ht⟩ : Fin (n + 1)) = Fin.castSucc ⟨t, ht'⟩ from Fin.ext rfl,
        toTup_castSucc, bitAt_eq_toTup n t ht' p.1]

theorem toTup_eq_bitAt (n : ℕ) (p : Bits n) (t : Fin n) : toTup n p t = bitAt n t p :=
  (bitAt_eq_toTup n t t.2 p).symm

theorem toTup_mk_eq_bitAt (n : ℕ) (p : Bits n) (t : ℕ) (ht : t < n) :
    toTup n p ⟨t, ht⟩ = bitAt n t p :=
  (bitAt_eq_toTup n t ht p).symm

/-- **Pauli words are products over tokens.** -/
theorem pauliWord_apply : ∀ (n : ℕ) (μ : Labels n) (a b : Bits n),
    pauliWord n μ a b = ∏ t : Fin n, pauli (toTup n μ t) (toTup n a t) (toTup n b t)
  | 0, μ, a, b => by
    rw [Fin.prod_univ_zero, Subsingleton.elim a b]
    simp [pauliWord, Matrix.one_apply_eq]
  | n + 1, μ, a, b => by
    rw [Fin.prod_univ_castSucc]
    simp only [toTup_castSucc, toTup_last]
    rw [← pauliWord_apply n μ.1 a.1 b.1]
    rfl

/-- **Product tables are products over tokens.** -/
theorem prodTab_eq_prod (v : ℕ → HVec 3) : ∀ (n : ℕ) (μ : Labels n),
    prodTab n v μ = ∏ t : Fin n, v t (toTup n μ t)
  | 0, _ => by
    rw [Fin.prod_univ_zero]
    rfl
  | n + 1, μ => by
    rw [Fin.prod_univ_castSucc, prodTab_succ, prodTab_eq_prod v n μ.1]
    simp only [toTup_castSucc, toTup_last, Fin.val_castSucc, Fin.val_last]

/-! ### §7 — the table carrier, dictionary, products and actions on token tuples -/

/-- The `k`-token table carrier `WK k`. -/
abbrev WK (k : ℕ) := (Fin k → Fin 4) → ℝ

/-- The product state. -/
def prodStateK {k : ℕ} (x : Fin k → Fin 3 → ℝ) : WK k := fun μ => ∏ i, hom (x i) (μ i)

/-- The `k`-fold maximal cone: nonnegative on every product of effects. -/
def maxConeK {k : ℕ} (Ω : Set (Fin 3 → ℝ)) : Set (WK k) :=
  {ω | ∀ e : Fin k → (Fin 3 → ℝ) →ᵃ[ℝ] ℝ,
    (∀ i, OIBridge.KInfFoundations.IsEffectOn Ω (e i)) →
      0 ≤ ∑ μ, (∏ i, ehom (e i) (μ i)) * ω μ}

/-- The `k`-fold Pauli dictionary. -/
noncomputable def dictK {k : ℕ} (ω : WK k) : Matrix (Fin k → Fin 2) (Fin k → Fin 2) ℂ :=
  ∑ μ, ((ω μ : ℂ) / 2 ^ k) • Matrix.of fun a b => ∏ i, pauli (μ i) (a i) (b i)

/-- The tables with positive semidefinite dictionary image. -/
def QK (k : ℕ) : Set (WK k) := {ω | (dictK ω).PosSemidef}

/-- The label map of the CNOT sign-and-label formula. -/
def cnotLabF {k : ℕ} (i j : Fin k) (μ : Fin k → Fin 4) : Fin k → Fin 4 :=
  Function.update (Function.update μ i (pc (μ i) (μ j))) j (pt (μ i) (μ j))

/-- The CNOT sign-and-label map, with the landed `sgn`, `pc`, `pt`. -/
def cnotK {k : ℕ} (i j : Fin k) (ω : WK k) : WK k := fun μ =>
  sgn (μ i) (μ j) * ω (Function.update (Function.update μ i (pc (μ i) (μ j))) j (pt (μ i) (μ j)))

/-- The one-token homogeneous action. -/
def actK {k : ℕ} (j : Fin k) (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : WK k) : WK k :=
  fun μ => homMap N (fun ν => ω (Function.update μ j ν)) (μ j)

theorem cnotK_apply {k : ℕ} (i j : Fin k) (ω : WK k) (μ : Fin k → Fin 4) :
    cnotK i j ω μ = sgn (μ i) (μ j) * ω (cnotLabF i j μ) := rfl

theorem actK_apply {k : ℕ} (j : Fin k) (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : WK k)
    (μ : Fin k → Fin 4) :
    actK j N ω μ = homMap N (fun m : Fin 4 => ω (Function.update μ j m)) (μ j) := rfl

/-- The recursive table of a `Fin`-indexed table. -/
def tabOf (k : ℕ) (ω : WK k) : Labels k → ℝ := fun ν => ω (toTup k ν)

/-- The `Fin`-indexed table of a recursive table. -/
def tupOf (k : ℕ) (w : Labels k → ℝ) : WK k := fun μ => w (ofTup k μ)

theorem tupOf_tabOf (k : ℕ) (ω : WK k) : tupOf k (tabOf k ω) = ω :=
  funext fun μ => congrArg ω (toTup_ofTup k μ)

theorem tabOf_tupOf (k : ℕ) (w : Labels k → ℝ) : tabOf k (tupOf k w) = w :=
  funext fun ν => congrArg w (ofTup_toTup k ν)

/-- The dictionary of a recursive table, entrywise, is the tuple-indexed dictionary on token tuples. -/
theorem dictionary_apply_tabOf (k : ℕ) (ω : WK k) (a b : Bits k) :
    dictionary k (tabOf k ω) a b = dictK ω (toTup k a) (toTup k b) := by
  simp only [dictionary, complexDictionary, dictK, tabOf, Matrix.sum_apply, Matrix.smul_apply,
    Matrix.of_apply, smul_eq_mul, pauliWord_apply]
  exact Equiv.sum_comp (carrierEquiv 4 k)
    (fun μ : Fin k → Fin 4 => ((ω μ : ℂ) / 2 ^ k) * ∏ i, pauli (μ i) (toTup k a i) (toTup k b i))

/-- **The dictionary transport**: the recursive dictionary is the tuple-indexed `dictK` reindexed by the
carrier equivalence. -/
theorem dictionary_tabOf (k : ℕ) (ω : WK k) :
    dictionary k (tabOf k ω) = (dictK ω).submatrix (carrierEquiv 2 k) (carrierEquiv 2 k) := by
  ext a b
  exact dictionary_apply_tabOf k ω a b

theorem mem_QK_iff {k : ℕ} (ω : WK k) : ω ∈ QK k ↔ (dictionary k (tabOf k ω)).PosSemidef := by
  have h : (dictionary k (tabOf k ω)).PosSemidef ↔ (dictK ω).PosSemidef := by
    rw [dictionary_tabOf]
    exact Matrix.posSemidef_submatrix_equiv _
  exact h.symm

/-- **The product-state transport.** -/
theorem tupOf_prodTab {k : ℕ} (x : ℕ → Fin 3 → ℝ) :
    tupOf k (prodTab k (fun i => hom (x i))) = prodStateK (fun t : Fin k => x t) := by
  funext μ
  show prodTab k (fun i => hom (x i)) (ofTup k μ) = ∏ i : Fin k, hom (x i) (μ i)
  rw [prodTab_eq_prod, toTup_ofTup]

/-- **The product-test transport.** -/
theorem sum_prodTab_tupOf {k : ℕ} (v : ℕ → HVec 3) (w : Labels k → ℝ) :
    ∑ ν, prodTab k v ν * w ν = ∑ μ : Fin k → Fin 4, (∏ i : Fin k, v i (μ i)) * tupOf k w μ := by
  refine Fintype.sum_equiv (carrierEquiv 4 k) _ _ fun ν => ?_
  rw [prodTab_eq_prod]
  show (∏ t : Fin k, v t (toTup k ν t)) * w ν =
    (∏ i : Fin k, v i (toTup k ν i)) * w (ofTup k (toTup k ν))
  rw [ofTup_toTup]

/-! ### §8 — the CNOT action in coordinates -/

/-- The bit permutation of `CNOT(i → j)`: bit `j` is flipped by bit `i`. -/
def cnotPerm : (n : ℕ) → ℕ → ℕ → Bits n → Bits n
  | 0, _, _, p => p
  | n + 1, i, j, p => if j = n then (p.1, p.2 + bitAt n i p.1) else (cnotPerm n i j p.1, p.2)

theorem cnotPerm_succ (n i j : ℕ) (a : Bits n) (x : Fin 2) :
    cnotPerm (n + 1) i j (a, x) =
      if j = n then (a, x + bitAt n i a) else (cnotPerm n i j a, x) := rfl

theorem bitAt_pair (n i : ℕ) (a : Bits n) (x : Fin 2) :
    bitAt (n + 1) i (a, x) = if i = n then x else bitAt n i a := rfl

theorem flipX_apply (c x y : Fin 2) : flipX c x y = if y = x + c then 1 else 0 := by
  fin_cases c <;> fin_cases x <;> fin_cases y <;> simp +decide [flipX, Xm]

theorem bitsPair_eq {n : ℕ} {a b : Bits n} {x y : Fin 2} (h1 : a = b) (h2 : x = y) :
    ((a, x) : Bits (n + 1)) = (b, y) :=
  Prod.ext h1 h2

theorem bitsPair_ne_fst {n : ℕ} {a b : Bits n} (x y : Fin 2) (h : a ≠ b) :
    ((a, x) : Bits (n + 1)) ≠ (b, y) :=
  fun e => h (congrArg Prod.fst e)

theorem bitsPair_ne_snd {n : ℕ} (a b : Bits n) {x y : Fin 2} (h : x ≠ y) :
    ((a, x) : Bits (n + 1)) ≠ (b, y) :=
  fun e => h (congrArg Prod.snd e)

/-- **`CNOT(i → j)` is the permutation matrix of `cnotPerm`.** -/
theorem cnotM_apply : ∀ (n i j : ℕ) (p q : Bits n),
    cnotM n i j p q = if q = cnotPerm n i j p then 1 else 0
  | 0, i, j, p, q => by
    rw [if_pos (Subsingleton.elim q (cnotPerm 0 i j p)), Subsingleton.elim p q]
    exact Matrix.one_apply_eq q
  | n + 1, i, j, p, q => by
    rcases p with ⟨a, x⟩
    rcases q with ⟨b, y⟩
    rw [cnotM_succ, cnotPerm_succ]
    by_cases hj : j = n
    · rw [if_pos hj, if_pos hj, blockFam_apply, flipX_apply]
      by_cases hab : a = b
      · rw [if_pos hab]
        by_cases hy : y = x + bitAt n i a
        · rw [if_pos hy, if_pos (bitsPair_eq hab.symm hy)]
        · rw [if_neg hy, if_neg (bitsPair_ne_snd b a hy)]
      · rw [if_neg hab, if_neg (bitsPair_ne_fst y (x + bitAt n i a) (Ne.symm hab))]
    · rw [if_neg hj, if_neg hj]
      simp only [tensorOf_apply]
      rw [cnotM_apply n i j a b, Matrix.one_apply]
      by_cases hb : b = cnotPerm n i j a
      · by_cases hxy : x = y
        · rw [if_pos hb, if_pos hxy, if_pos (bitsPair_eq hb hxy.symm), one_mul]
        · rw [if_pos hb, if_neg hxy, mul_zero,
            if_neg (bitsPair_ne_snd b (cnotPerm n i j a) (Ne.symm hxy))]
      · rw [if_neg hb, zero_mul, if_neg (bitsPair_ne_fst y x hb)]

/-- Conjugation by a permutation matrix permutes the entries. -/
theorem conj_perm_apply {ι : Type*} [Fintype ι] [DecidableEq ι] (P M : Matrix ι ι ℂ)
    (f : ι → ι) (hP : ∀ p q, P p q = if q = f p then 1 else 0) (p q : ι) :
    (P * M * Pᴴ) p q = M (f p) (f q) := by
  have h1 : ∀ s, (P * M) p s = M (f p) s := by
    intro s
    rw [Matrix.mul_apply, Finset.sum_eq_single (f p)]
    · rw [hP, if_pos rfl, one_mul]
    · intro r _ hr
      rw [hP, if_neg hr, zero_mul]
    · intro h
      exact absurd (Finset.mem_univ _) h
  rw [Matrix.mul_apply, Finset.sum_eq_single (f q)]
  · rw [h1, Matrix.conjTranspose_apply, hP, if_pos rfl, star_one, mul_one]
  · intro s _ hs
    rw [Matrix.conjTranspose_apply, hP, if_neg hs, star_zero, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem bitAt_cnotPerm {i j : ℕ} (hij : i < j) : ∀ (n : ℕ), j < n → ∀ (t : ℕ) (p : Bits n),
    bitAt n t (cnotPerm n i j p) = if t = j then bitAt n t p + bitAt n i p else bitAt n t p
  | 0, hj, _, _ => absurd hj (Nat.not_lt_zero j)
  | n + 1, hj, t, p => by
    rcases p with ⟨a, x⟩
    rw [cnotPerm_succ]
    by_cases hjn : j = n
    · rw [if_pos hjn, bitAt_pair, bitAt_pair, bitAt_pair, if_neg (show i ≠ n by omega)]
      by_cases htn : t = n
      · rw [if_pos htn, if_pos htn, if_pos (htn.trans hjn.symm)]
      · rw [if_neg htn, if_neg htn, if_neg (show t ≠ j from fun h => htn (h.trans hjn))]
    · have hj' : j < n := by omega
      rw [if_neg hjn, bitAt_pair, bitAt_cnotPerm hij n hj' t a, bitAt_pair, bitAt_pair,
        if_neg (show i ≠ n by omega)]
      by_cases htn : t = n
      · rw [if_pos htn, if_pos htn, if_neg (show t ≠ j from fun h => hjn (h.symm.trans htn))]
      · rw [if_neg htn, if_neg htn]

/-- The bit vector after `CNOT(i → j)` on token tuples. -/
def cflip {k : ℕ} (i j : Fin k) (a : Fin k → Fin 2) : Fin k → Fin 2 :=
  fun t => if t = j then a t + a i else a t

theorem cflip_apply {k : ℕ} (i j : Fin k) (a : Fin k → Fin 2) (t : Fin k) :
    cflip i j a t = if t = j then a t + a i else a t := rfl

theorem cflip_ne {k : ℕ} {i j t : Fin k} (h : t ≠ j) (a : Fin k → Fin 2) : cflip i j a t = a t :=
  if_neg h

theorem cflip_self {k : ℕ} (i j : Fin k) (a : Fin k → Fin 2) : cflip i j a j = a j + a i :=
  if_pos rfl

/-- **The gate transport**: on token tuples, `cnotPerm` is `cflip`. -/
theorem toTup_cnotPerm {k i j : ℕ} (hij : i < j) (hj : j < k) (p : Bits k) :
    toTup k (cnotPerm k i j p) = cflip ⟨i, lt_trans hij hj⟩ ⟨j, hj⟩ (toTup k p) := by
  funext t
  rw [cflip_apply, toTup_eq_bitAt, toTup_eq_bitAt, toTup_mk_eq_bitAt, bitAt_cnotPerm hij k hj]
  by_cases ht : (t : ℕ) = j
  · rw [if_pos ht, if_pos (Fin.ext ht : t = ⟨j, hj⟩)]
  · rw [if_neg ht, if_neg (show t ≠ ⟨j, hj⟩ from fun h => ht (congrArg Fin.val h))]

theorem cnotLabF_j {k : ℕ} (i j : Fin k) (μ : Fin k → Fin 4) :
    cnotLabF i j μ j = pt (μ i) (μ j) :=
  Function.update_self _ _ _

theorem cnotLabF_i {k : ℕ} {i j : Fin k} (hij : i ≠ j) (μ : Fin k → Fin 4) :
    cnotLabF i j μ i = pc (μ i) (μ j) := by
  rw [cnotLabF, Function.update_of_ne hij, Function.update_self]

theorem cnotLabF_ne {k : ℕ} {i j t : Fin k} (hti : t ≠ i) (htj : t ≠ j) (μ : Fin k → Fin 4) :
    cnotLabF i j μ t = μ t := by
  rw [cnotLabF, Function.update_of_ne htj, Function.update_of_ne hti]

theorem cnotLabF_invol {k : ℕ} {i j : Fin k} (hij : i ≠ j) (μ : Fin k → Fin 4) :
    cnotLabF i j (cnotLabF i j μ) = μ := by
  funext t
  by_cases htj : t = j
  · rw [htj, cnotLabF_j, cnotLabF_i hij, cnotLabF_j, pt_pt]
  · by_cases hti : t = i
    · rw [hti, cnotLabF_i hij, cnotLabF_i hij, cnotLabF_j, pc_pc]
    · rw [cnotLabF_ne hti htj, cnotLabF_ne hti htj]

/-- The label map as an involutive equivalence. -/
def cnotLab {k : ℕ} {i j : Fin k} (hij : i ≠ j) : (Fin k → Fin 4) ≃ (Fin k → Fin 4) where
  toFun := cnotLabF i j
  invFun := cnotLabF i j
  left_inv := cnotLabF_invol hij
  right_inv := cnotLabF_invol hij

theorem cnotLab_apply {k : ℕ} {i j : Fin k} (hij : i ≠ j) (μ : Fin k → Fin 4) :
    cnotLab hij μ = cnotLabF i j μ := rfl

/-- A product with two distinguished factors. -/
theorem prod_two_index {k : ℕ} {i j : Fin k} (hij : i ≠ j) (f g : Fin k → ℂ) (c : ℂ)
    (hrest : ∀ t, t ≠ i → t ≠ j → f t = g t) (hpair : f i * f j = c * (g i * g j)) :
    ∏ t, f t = c * ∏ t, g t := by
  have hj : j ∈ Finset.univ.erase i := Finset.mem_erase.mpr ⟨Ne.symm hij, Finset.mem_univ j⟩
  have hr : ∏ t ∈ (Finset.univ.erase i).erase j, f t =
      ∏ t ∈ (Finset.univ.erase i).erase j, g t := by
    refine Finset.prod_congr rfl fun t ht => ?_
    obtain ⟨htj, ht'⟩ := Finset.mem_erase.mp ht
    obtain ⟨hti, -⟩ := Finset.mem_erase.mp ht'
    exact hrest t hti htj
  rw [← Finset.mul_prod_erase Finset.univ f (Finset.mem_univ i),
    ← Finset.mul_prod_erase (Finset.univ.erase i) f hj,
    ← Finset.mul_prod_erase Finset.univ g (Finset.mem_univ i),
    ← Finset.mul_prod_erase (Finset.univ.erase i) g hj, hr, ← mul_assoc, hpair]
  ring

/-- The pair table with one unit entry. -/
def pairUnit (m n : Fin 4) : W 3 := fun (μ ν : Fin 4) => if μ = m ∧ ν = n then 1 else 0

theorem pairUnit_apply (m n μ ν : Fin 4) :
    pairUnit m n μ ν = if μ = m ∧ ν = n then 1 else 0 := rfl

theorem dict_apply (ω : W 3) (a b : Fin 2 × Fin 2) :
    dict ω a b = ∑ μ : Fin 4, ∑ ν : Fin 4,
      ((ω μ ν : ℂ) / 4) * (pauli μ a.1 b.1 * pauli ν a.2 b.2) := by
  simp only [dict, Matrix.sum_apply, Matrix.smul_apply, tensorOf_apply, smul_eq_mul]

theorem sum_pairUnit (m n : Fin 4) (F : Fin 4 → Fin 4 → ℂ) :
    ∑ μ : Fin 4, ∑ ν : Fin 4, ((pairUnit m n μ ν : ℂ) / 4) * F μ ν = F m n / 4 := by
  rw [Finset.sum_eq_single m]
  · rw [Finset.sum_eq_single n]
    · rw [pairUnit_apply, if_pos (show m = m ∧ n = n from ⟨rfl, rfl⟩), Complex.ofReal_one]
      ring
    · intro ν _ hν
      rw [pairUnit_apply, if_neg (show ¬ (m = m ∧ ν = n) from fun h => hν h.2),
        Complex.ofReal_zero]
      ring
    · intro h
      exact absurd (Finset.mem_univ n) h
  · intro μ _ hμ
    refine Finset.sum_eq_zero fun ν _ => ?_
    rw [pairUnit_apply, if_neg (show ¬ (μ = m ∧ ν = n) from fun h => hμ h.1),
      Complex.ofReal_zero]
    ring
  · intro h
    exact absurd (Finset.mem_univ m) h

theorem dict_pairUnit_apply (m n : Fin 4) (x1 x2 y1 y2 : Fin 2) :
    dict (pairUnit m n) (x1, x2) (y1, y2) = pauli m x1 y1 * pauli n x2 y2 / 4 := by
  rw [dict_apply]
  exact sum_pairUnit m n (fun μ ν => pauli μ x1 y1 * pauli ν x2 y2)

theorem cnot_pairUnit_apply (m n μ ν : Fin 4) :
    cnot (pairUnit m n) μ ν = sgn (pc m n) (pt m n) * pairUnit (pc m n) (pt m n) μ ν := by
  rw [cnot_apply, cnotFun_apply, pairUnit_apply, pairUnit_apply]
  by_cases h : μ = pc m n ∧ ν = pt m n
  · obtain ⟨rfl, rfl⟩ := h
    rw [if_pos (And.intro (pc_pc m n) (pt_pt m n)),
      if_pos (show pc m n = pc m n ∧ pt m n = pt m n from ⟨rfl, rfl⟩)]
  · have h' : ¬ (pc μ ν = m ∧ pt μ ν = n) := by
      rintro ⟨h1, h2⟩
      apply h
      constructor
      · rw [← h1, ← h2, pc_pc]
      · rw [← h1, ← h2, pt_pt]
    rw [if_neg h', if_neg h, mul_zero, mul_zero]

theorem cnot_pairUnit (m n : Fin 4) :
    cnot (pairUnit m n) = sgn (pc m n) (pt m n) • pairUnit (pc m n) (pt m n) :=
  funext fun μ => funext fun ν => cnot_pairUnit_apply m n μ ν

theorem blockMat_one_Xm_apply (p q : Fin 2 × Fin 2) :
    blockMat 1 Xm p q = if q = (p.1, p.2 + p.1) then 1 else 0 := by
  obtain ⟨a, b⟩ := p
  obtain ⟨c, d⟩ := q
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp +decide [blockMat, P0, P1, Xm, tensorOf_apply, Matrix.add_apply]

theorem blockMat_conj_apply (M : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (x1 x2 y1 y2 : Fin 2) :
    (blockMat 1 Xm * M * (blockMat 1 Xm)ᴴ) (x1, x2) (y1, y2) = M (x1, x2 + x1) (y1, y2 + y1) :=
  conj_perm_apply (blockMat 1 Xm) M (fun p => (p.1, p.2 + p.1)) blockMat_one_Xm_apply (x1, x2)
    (y1, y2)

/-- **The two-token sign-and-label identity**, read off the landed two-token gate
`dict_cnot_block` at the unit tables. -/
theorem pauli_cnot_pair (m n : Fin 4) (x1 y1 x2 y2 : Fin 2) :
    pauli m x1 y1 * pauli n (x2 + x1) (y2 + y1) =
      (sgn (pc m n) (pt m n) : ℂ) * (pauli (pc m n) x1 y1 * pauli (pt m n) x2 y2) := by
  have h := congrFun (congrFun (dict_cnot_block (pairUnit m n)) (x1, x2)) (y1, y2)
  rw [cnot_pairUnit, dict_smul, Matrix.smul_apply, dict_pairUnit_apply, blockMat_conj_apply,
    dict_pairUnit_apply, Complex.real_smul] at h
  linear_combination (-4 : ℂ) * h

/-- **CNOT on token tuples**: conjugating the dictionary by `CNOT(i → j)` at permuted indices is
the dictionary of the tuple-indexed sign-and-label map. -/
theorem dictK_cflip {k : ℕ} {i j : Fin k} (hij : i ≠ j) (ω : WK k) (a b : Fin k → Fin 2) :
    dictK ω (cflip i j a) (cflip i j b) = dictK (cnotK i j ω) a b := by
  simp only [dictK, Matrix.sum_apply, Matrix.smul_apply, Matrix.of_apply, smul_eq_mul]
  refine Fintype.sum_equiv (cnotLab hij) _ _ fun ν => ?_
  have hrest : ∀ t, t ≠ i → t ≠ j →
      pauli (ν t) (cflip i j a t) (cflip i j b t) = pauli (cnotLabF i j ν t) (a t) (b t) := by
    intro t hti htj
    rw [cflip_ne htj a, cflip_ne htj b, cnotLabF_ne hti htj]
  have hpair : pauli (ν i) (cflip i j a i) (cflip i j b i) *
      pauli (ν j) (cflip i j a j) (cflip i j b j) =
      (sgn (pc (ν i) (ν j)) (pt (ν i) (ν j)) : ℂ) *
        (pauli (cnotLabF i j ν i) (a i) (b i) * pauli (cnotLabF i j ν j) (a j) (b j)) := by
    rw [cflip_ne hij a, cflip_ne hij b, cflip_self, cflip_self, cnotLabF_i hij, cnotLabF_j]
    exact pauli_cnot_pair (ν i) (ν j) (a i) (b i) (a j) (b j)
  have hprod := prod_two_index hij (fun t => pauli (ν t) (cflip i j a t) (cflip i j b t))
    (fun t => pauli (cnotLabF i j ν t) (a t) (b t)) _ hrest hpair
  rw [cnotLab_apply, cnotK_apply, cnotLabF_invol hij, cnotLabF_i hij, cnotLabF_j, hprod,
    Complex.ofReal_mul]
  ring

/-- **Obligation 1, CNOT**: the dictionary action of `CNOT(i → j)` is the tuple-indexed sign-and-label map
`cnotK`, transported by the carrier equivalence. -/
theorem tabAct_cnotM {k i j : ℕ} (hij : i < j) (hj : j < k) (ω : WK k) :
    tabAct k (cnotM k i j) (tabOf k ω) = tabOf k (cnotK ⟨i, lt_trans hij hj⟩ ⟨j, hj⟩ ω) := by
  have hne : (⟨i, lt_trans hij hj⟩ : Fin k) ≠ ⟨j, hj⟩ :=
    fun h => (Nat.ne_of_lt hij) (congrArg Fin.val h)
  have hconj : cnotM k i j * dictionary k (tabOf k ω) * (cnotM k i j)ᴴ =
      dictionary k (tabOf k (cnotK ⟨i, lt_trans hij hj⟩ ⟨j, hj⟩ ω)) := by
    ext p q
    rw [conj_perm_apply (cnotM k i j) _ (cnotPerm k i j) (cnotM_apply k i j),
      dictionary_apply_tabOf k ω, dictionary_apply_tabOf k (cnotK _ _ ω), toTup_cnotPerm hij hj,
      toTup_cnotPerm hij hj, dictK_cflip hne]
  rw [tabAct, hconj, coordinates_dictionary_real]

/-- Obligation 1, CNOT, on every recursive table. -/
theorem tabAct_cnotM_eq {k i j : ℕ} (hij : i < j) (hj : j < k) (w : Labels k → ℝ) :
    tabAct k (cnotM k i j) w = tabOf k (cnotK ⟨i, lt_trans hij hj⟩ ⟨j, hj⟩ (tupOf k w)) :=
  (congrArg (tabAct k (cnotM k i j)) (tabOf_tupOf k w)).symm.trans
    (tabAct_cnotM hij hj (tupOf k w))

theorem tabAct_cnotK {k : ℕ} {i j : Fin k} (hij : i < j) (ω : WK k) :
    tabAct k (cnotM k i j) (tabOf k ω) = tabOf k (cnotK i j ω) :=
  tabAct_cnotM (i := i.val) (j := j.val) hij j.2 ω

/-! ### §9 — the one-token actions in coordinates -/

/-- The homogeneous action of `N` on label slot `j` of a recursive table. -/
def slotAct (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : (n : ℕ) → ℕ → (Labels n → ℝ) → Labels n → ℝ
  | 0, _, w => w
  | n + 1, j, w => fun μ =>
    if j = n then homMap N (fun m : Fin 4 => w (μ.1, m)) μ.2
    else slotAct N n j (fun ν => w (ν, μ.2)) μ.1

theorem slotAct_succ (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (n j : ℕ) (w : Labels (n + 1) → ℝ)
    (ν : Labels n) (x : Fin 4) :
    slotAct N (n + 1) j w (ν, x) = if j = n then homMap N (fun m : Fin 4 => w (ν, m)) x
      else slotAct N n j (fun ν' => w (ν', x)) ν := rfl

theorem slotAct_last (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (n j : ℕ) (hj : j = n)
    (w : Labels (n + 1) → ℝ) :
    slotAct N (n + 1) j w = fun μ => homMap N (fun m : Fin 4 => w (μ.1, m)) μ.2 :=
  funext fun _ => if_pos hj

theorem slotAct_lift (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (n j : ℕ) (hj : j ≠ n)
    (w : Labels (n + 1) → ℝ) :
    slotAct N (n + 1) j w = fun μ => slotAct N n j (fun ν => w (ν, μ.2)) μ.1 :=
  funext fun _ => if_neg hj

/-- The dictionary split at the last token, with one-token matrices on it. -/
theorem dictionary_succ_tok (n : ℕ) (w : Labels (n + 1) → ℝ) :
    dictionary (n + 1) w = ∑ ν : Labels n,
      tensorOf (((1 : ℂ) / 2 ^ n) • pauliWord n ν) (tokMat (fun m : Fin 4 => w (ν, m))) := by
  ext ⟨a, x⟩ ⟨b, y⟩
  simp only [dictionary, complexDictionary, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul,
    Fintype.sum_prod_type, pauliWord, tensorOf_apply, tokMat]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun m _ => ?_
  ring

/-- The dictionary split at the last token, with the dictionary on the earlier tokens. -/
theorem dictionary_succ_pref (n : ℕ) (w : Labels (n + 1) → ℝ) :
    dictionary (n + 1) w = ∑ m : Fin 4,
      tensorOf (dictionary n (fun ν => w (ν, m))) (((1 : ℂ) / 2) • pauli m) := by
  ext ⟨a, x⟩ ⟨b, y⟩
  simp only [dictionary, complexDictionary, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul,
    Fintype.sum_prod_type, pauliWord, tensorOf_apply]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun m _ => ?_
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun ν _ => ?_
  ring

/-- Conjugating the dictionary by a one-token matrix whose action on one-token matrices is the
homogeneous action of `N`. -/
theorem localM_conj_dictionary (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (V : Matrix (Fin 2) (Fin 2) ℂ)
    (hV : ∀ v : HVec 3, tokMat (homMap N v) = V * tokMat v * Vᴴ) :
    ∀ (n j : ℕ) (w : Labels n → ℝ),
      localM n j V * dictionary n w * (localM n j V)ᴴ = dictionary n (slotAct N n j w)
  | 0, j, w => by
    show (1 : Mat 0) * dictionary 0 w * (1 : Mat 0)ᴴ = dictionary 0 w
    rw [Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
  | n + 1, j, w => by
    rw [localM_succ]
    by_cases hj : j = n
    · rw [if_pos hj, dictionary_succ_tok n w, Finset.mul_sum, Finset.sum_mul,
        slotAct_last N n j hj, dictionary_succ_tok]
      refine Finset.sum_congr rfl fun ν _ => ?_
      rw [tensor_conjugation, Matrix.one_mul, Matrix.conjTranspose_one, Matrix.mul_one, ← hV]
    · rw [if_neg hj, dictionary_succ_pref n w, Finset.mul_sum, Finset.sum_mul,
        slotAct_lift N n j hj, dictionary_succ_pref]
      refine Finset.sum_congr rfl fun m _ => ?_
      rw [tensor_conjugation, localM_conj_dictionary N V hV n j, Matrix.one_mul,
        Matrix.conjTranspose_one, Matrix.mul_one]

/-- **The one-token transport**: the recursive slot action is the tuple-indexed `actK` on token tuples. -/
theorem slotAct_toTup (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : ∀ (n j : ℕ) (hj : j < n) (ω : WK n)
    (ν : Labels n), slotAct N n j (fun ν' => ω (toTup n ν')) ν = actK ⟨j, hj⟩ N ω (toTup n ν)
  | 0, j, hj, _, _ => absurd hj (Nat.not_lt_zero j)
  | n + 1, j, hj, ω, μ => by
    rcases μ with ⟨ν, x⟩
    rw [slotAct_succ, actK_apply]
    by_cases hjn : j = n
    · rw [if_pos hjn, show (⟨j, hj⟩ : Fin (n + 1)) = Fin.last n from Fin.ext hjn]
      simp only [toTup_succ, toTup_last, Fin.update_snoc_last]
    · have hj' : j < n := by omega
      rw [if_neg hjn, show (⟨j, hj⟩ : Fin (n + 1)) = Fin.castSucc ⟨j, hj'⟩ from Fin.ext rfl]
      refine (slotAct_toTup N n j hj' (fun a => ω (Fin.snoc (α := fun _ => Fin 4) a x)) ν).trans ?_
      rw [actK_apply]
      simp only [toTup_succ, toTup_castSucc, ← Fin.snoc_update]

/-- **Obligation 1, one-token actions**: the dictionary action of a one-token matrix carrying
`N` is the tuple-indexed homogeneous action `actK`, transported by the carrier equivalence. -/
theorem tabAct_localM (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (V : Matrix (Fin 2) (Fin 2) ℂ)
    (hV : ∀ v : HVec 3, tokMat (homMap N v) = V * tokMat v * Vᴴ) {k j : ℕ} (hj : j < k)
    (ω : WK k) :
    tabAct k (localM k j V) (tabOf k ω) = tabOf k (actK ⟨j, hj⟩ N ω) := by
  rw [tabAct, localM_conj_dictionary N V hV k j, coordinates_dictionary_real]
  funext ν
  exact slotAct_toTup N k j hj ω ν

/-- Obligation 1, one-token actions, on every recursive table. -/
theorem tabAct_localM_eq (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (V : Matrix (Fin 2) (Fin 2) ℂ)
    (hV : ∀ v : HVec 3, tokMat (homMap N v) = V * tokMat v * Vᴴ) {k j : ℕ} (hj : j < k)
    (w : Labels k → ℝ) :
    tabAct k (localM k j V) w = tabOf k (actK ⟨j, hj⟩ N (tupOf k w)) :=
  (congrArg (tabAct k (localM k j V)) (tabOf_tupOf k w)).symm.trans
    (tabAct_localM N V hV hj (tupOf k w))

theorem tabAct_localK (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (V : Matrix (Fin 2) (Fin 2) ℂ)
    (hV : ∀ v : HVec 3, tokMat (homMap N v) = V * tokMat v * Vᴴ) {k : ℕ} (j : Fin k) (ω : WK k) :
    tabAct k (localM k j V) (tabOf k ω) = tabOf k (actK j N ω) :=
  tabAct_localM N V hV j.2 ω

/-- The third-axis flow on token `j` in coordinates: `actK j (rotLin t)`. -/
theorem tabAct_rotK {k : ℕ} (t : ℝ) (j : Fin k) (ω : WK k) :
    tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) (tabOf k ω) =
      tabOf k (actK j (OIBridge.KInfFoundations.rotLin t) ω) :=
  tabAct_localK _ _ (tokMat_rot t) j ω

/-- The cyclic map on token `j` in coordinates: `actK j cycEquiv`. -/
theorem tabAct_cycK {k : ℕ} (j : Fin k) (ω : WK k) :
    tabAct k (localM k j cycMat) (tabOf k ω) =
      tabOf k (actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω) :=
  tabAct_localK _ _ tokMat_cyc j ω

/-! ### §10 — the separate table inclusions and the statement surface -/

theorem mem_matCone_dictionary {k : ℕ} {K : Set (Labels k → ℝ)} {w : Labels k → ℝ}
    (hw : w ∈ K) : dictionary k w ∈ matCone k K :=
  mem_matCone.mpr ⟨dictionary_hermitian k w, by rw [coordinates_dictionary_real]; exact hw⟩

theorem pres_matCone {k : ℕ} {K : Set (Labels k → ℝ)} {U : Mat k}
    (hU : ∀ w ∈ K, tabAct k U w ∈ K) : Pres (matCone k K) U := by
  intro A hA'
  obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
  refine mem_matCone.mpr ⟨Matrix.isHermitian_mul_mul_conjTranspose U hAh, ?_⟩
  have h := hU _ hAK
  rwa [tabAct, dictionary_coordinates_real k A hAh] at h

theorem maxTest_matCone {k : ℕ} {K : Set (Labels k → ℝ)} (hmax : K ⊆ maxConeTab k) :
    ∀ A ∈ matCone k K, ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) := by
  intro A hA' a
  obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
  rw [← dictionary_coordinates_real k A hAh, quad_dictionary_prodVec]
  have hS := lorPair_nonneg_of_maxConeTab (v := fun i => blochH (a i)) (hmax hAK)
    fun i _ => lor_blochH (a i)
  rw [show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
      (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
        2 ^ k : ℝ) : ℂ) by push_cast; ring,
    Complex.zero_le_real]
  exact div_nonneg hS (pow_nonneg (by norm_num) k)

theorem pure_matCone {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K) :
    ∀ a : ℕ → Fin 2 → ℂ, (∀ i, i < k → star (a i) ⬝ᵥ a i = 1) →
      vecMulVec (prodVec k a) (star (prodVec k a)) ∈ matCone k K := by
  intro a ha
  rw [vecMulVec_prodVec,
    show (fun i => vecMulVec (a i) (star (a i))) = fun i => tokMat (blochH (a i)) from
      funext fun i => (tokMat_blochH (a i)).symm,
    ← dictionary_prodTab]
  apply mem_matCone_dictionary
  rw [prodTab_congr k fun i hi => (hom_blochX (blochH_zero_of_unit (ha i hi))).symm]
  exact hH1 _ fun i hi => blochX_mem_eball (blochH_zero_of_unit (ha i hi))

theorem add_matCone {k : ℕ} {K : Set (Labels k → ℝ)} (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K) :
    ∀ A ∈ matCone k K, ∀ B ∈ matCone k K, A + B ∈ matCone k K := by
  intro A hA' B hB'
  obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
  obtain ⟨hBh, hBK⟩ := mem_matCone.mp hB'
  refine mem_matCone.mpr ⟨hAh.add hBh, ?_⟩
  rw [coordinates_add]
  exact hadd _ hAK _ hBK

theorem smul_matCone {k : ℕ} {K : Set (Labels k → ℝ)}
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K) :
    ∀ c : ℝ, 0 ≤ c → ∀ A ∈ matCone k K, c • A ∈ matCone k K := by
  intro c hc A hA'
  obtain ⟨hAh, hAK⟩ := mem_matCone.mp hA'
  refine mem_matCone.mpr ⟨?_, ?_⟩
  · show (c • A)ᴴ = c • A
    rw [Matrix.conjTranspose_smul, star_trivial, hAh.eq]
  · rw [coordinates_smul]
    exact hsmul c hc _ hAK

/-- **Upper table inclusion.** The effect-form product bound and invariance under the named
actions put every table of `K` in the positive semidefinite tables. Products in `K` and cone
closure are not used. -/
theorem tableCone_subset_psd_of_maxCone_drive {k : ℕ} {K : Set (Labels k → ℝ)}
    (hmax : K ⊆ maxConeTab k)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    K ⊆ {w | (dictionary k w).PosSemidef} := by
  have hC := subset_psd_of_maxCone_drive (C := matCone k K) (fun A hA' => (mem_matCone.mp hA').1)
    (maxTest_matCone hmax) (fun i j hij hj => pres_matCone (hH2 i j hij hj))
    (fun j h0 hj t => ⟨pres_matCone fun w hw => (hA j h0 hj t w hw).1,
      pres_matCone fun w hw => (hA j h0 hj t w hw).2⟩)
  intro w hw
  exact hC (mem_matCone_dictionary hw)

/-- **Lower table inclusion.** Products of ball states, cone closure and invariance under the
named actions put every positive semidefinite table in `K`. The product bound is not used. -/
theorem psd_subset_tableCone_of_products_cone_drive {k : ℕ} {K : Set (Labels k → ℝ)}
    (hH1 : ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ K)
    (hadd : ∀ w ∈ K, ∀ w' ∈ K, w + w' ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ w ∈ K, c • w ∈ K)
    (hH2 : ∀ i j : ℕ, i < j → j < k → ∀ w ∈ K, tabAct k (cnotM k i j) w ∈ K)
    (hA : ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ K ∧
        tabAct k (localM k j cycMat) w ∈ K) :
    {w | (dictionary k w).PosSemidef} ⊆ K := by
  have hC := psd_subset_of_pure_cone_drive (C := matCone k K) (pure_matCone hH1)
    (add_matCone hadd) (smul_matCone hsmul) (fun i j hij hj => pres_matCone (hH2 i j hij hj))
    (fun j h0 hj t => ⟨pres_matCone fun w hw => (hA j h0 hj t w hw).1,
      pres_matCone fun w hw => (hA j h0 hj t w hw).2⟩)
  intro w hw
  have h := (mem_matCone.mp (hC (show dictionary k w ∈ psdSet k from hw))).2
  rwa [coordinates_dictionary_real] at h

/-- The recursive tables of a set of `Fin`-indexed tables. -/
def tabSet (k : ℕ) (K : Set (WK k)) : Set (Labels k → ℝ) := {w | tupOf k w ∈ K}

theorem tabOf_mem_tabSet {k : ℕ} {K : Set (WK k)} {ω : WK k} :
    tabOf k ω ∈ tabSet k K ↔ ω ∈ K := by
  show tupOf k (tabOf k ω) ∈ K ↔ ω ∈ K
  rw [tupOf_tabOf]

theorem tabSet_products {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K) :
    ∀ x : ℕ → Fin 3 → ℝ, (∀ i, i < k → x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodTab k (fun i => hom (x i)) ∈ tabSet k K := by
  intro x hx
  show tupOf k (prodTab k (fun i => hom (x i))) ∈ K
  rw [tupOf_prodTab]
  exact hH1 (fun t => x t) fun t => hx t t.2

theorem tabSet_add {k : ℕ} {K : Set (WK k)} (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K) :
    ∀ w ∈ tabSet k K, ∀ w' ∈ tabSet k K, w + w' ∈ tabSet k K :=
  fun w hw w' hw' => hadd (tupOf k w) hw (tupOf k w') hw'

theorem tabSet_smul {k : ℕ} {K : Set (WK k)} (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K) :
    ∀ c : ℝ, 0 ≤ c → ∀ w ∈ tabSet k K, c • w ∈ tabSet k K :=
  fun c hc w hw => hsmul c hc (tupOf k w) hw

theorem tabSet_maxCone {k : ℕ} {K : Set (WK k)}
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3)) : tabSet k K ⊆ maxConeTab k := by
  intro w hw e he
  have h := hmax (show tupOf k w ∈ K from hw) (fun t => e t) (fun t => he t t.2)
  rw [sum_prodTab_tupOf]
  exact h

theorem tabSet_cnot {k : ℕ} {K : Set (WK k)}
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K) :
    ∀ i j : ℕ, i < j → j < k → ∀ w ∈ tabSet k K, tabAct k (cnotM k i j) w ∈ tabSet k K := by
  intro i j hij hj w hw
  rw [tabAct_cnotM_eq hij hj]
  exact tabOf_mem_tabSet.mpr (hH2 ⟨i, lt_trans hij hj⟩ ⟨j, hj⟩ hij (tupOf k w) hw)

theorem tabSet_local {k : ℕ} {K : Set (WK k)}
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    ∀ j : ℕ, 0 < j → j < k → ∀ t : ℝ, ∀ w ∈ tabSet k K,
      tabAct k (localM k j (phaseMat (Real.cos t) (Real.sin t))) w ∈ tabSet k K ∧
        tabAct k (localM k j cycMat) w ∈ tabSet k K := by
  intro j h0 hj t w hw
  have h := hA ⟨j, hj⟩ (Nat.pos_iff_ne_zero.mp h0) t (tupOf k w) hw
  rw [tabAct_localM_eq _ _ (tokMat_rot t) hj, tabAct_localM_eq _ _ tokMat_cyc hj]
  exact ⟨tabOf_mem_tabSet.mpr h.1, tabOf_mem_tabSet.mpr h.2⟩

/-- **Upper inclusion.** -/
theorem subset_QK_of_maxCone_drive {k : ℕ} {K : Set (WK k)}
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K ⊆ QK k := by
  have hT := tableCone_subset_psd_of_maxCone_drive (K := tabSet k K) (tabSet_maxCone hmax)
    (tabSet_cnot hH2) (tabSet_local hA)
  intro ω hω
  exact (mem_QK_iff ω).mpr (hT (tabOf_mem_tabSet.mpr hω))

/-- **Lower inclusion.** -/
theorem QK_subset_of_products_cone_drive {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    QK k ⊆ K := by
  have hT := psd_subset_tableCone_of_products_cone_drive (K := tabSet k K) (tabSet_products hH1)
    (tabSet_add hadd) (tabSet_smul hsmul) (tabSet_cnot hH2) (tabSet_local hA)
  intro ω hω
  exact tabOf_mem_tabSet.mp
    (hT (show tabOf k ω ∈ {w | (dictionary k w).PosSemidef} from (mem_QK_iff ω).mp hω))

/-- **The conditional k-token cone theorem.** -/
theorem kCone_eq_QK_of_drive_maxCone {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = QK k :=
  Set.Subset.antisymm (subset_QK_of_maxCone_drive hmax hH2 hA)
    (QK_subset_of_products_cone_drive hH1 hadd hsmul hH2 hA)

/-- **Forward witness**: `QK k` is invariant under the named actions, by positive
semidefinite conjugation. -/
theorem driveInvariantK_of_eq_QK {k : ℕ} {K : Set (WK k)} (h : K = QK k) :
    (∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K) ∧
      ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
        actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
          actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  subst h
  refine ⟨fun i j hij ω hω => ?_, fun j _ t ω hω => ⟨?_, ?_⟩⟩
  · rw [mem_QK_iff] at hω ⊢
    rw [← tabAct_cnotK hij]
    exact tabAct_psd _ hω
  · rw [mem_QK_iff] at hω ⊢
    rw [← tabAct_localK _ _ (tokMat_rot t) j]
    exact tabAct_psd _ hω
  · rw [mem_QK_iff] at hω ⊢
    rw [← tabAct_localK _ _ tokMat_cyc j]
    exact tabAct_psd _ hω

/-- **The equivalence.** Given products, cone closure and the `k`-fold maxCone bound,
`K = QK k` if and only if `K` is invariant under the named actions. Witnesses:
`driveInvariantK_of_eq_QK` (→) and `kCone_eq_QK_of_drive_maxCone` (←). -/
theorem kCone_eq_QK_iff_drive_maxCone {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3)) :
    K = QK k ↔ ((∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K) ∧
      ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
        actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
          actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :=
  ⟨driveInvariantK_of_eq_QK, fun h => kCone_eq_QK_of_drive_maxCone hH1 hadd hsmul hmax h.1 h.2⟩

/-! ### §11 — the k = 2 carrier and its five transports -/

/-- The `k = 2` carrier equivalence `W 3 ≃ WK 2`. -/
def pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2 where
  toFun ω := fun μ => ω (μ 0) (μ 1)
  invFun η := fun a b => η ![a, b]
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  left_inv _ := rfl
  right_inv η := funext fun μ => congrArg η (funext fun i => by fin_cases i <;> rfl)

theorem pairCarrierEquiv_apply (ω : W 3) (μ : Fin 2 → Fin 4) :
    pairCarrierEquiv ω μ = ω (μ 0) (μ 1) := rfl

/-- Transport 1: products. -/
theorem pairCarrierEquiv_prodState (x : Fin 2 → Fin 3 → ℝ) :
    pairCarrierEquiv (prodState (x 0) (x 1)) = prodStateK x := by
  funext μ
  exact (Fin.prod_univ_two (fun i => hom (x i) (μ i))).symm

theorem sum_pairCarrier_eq (e : Fin 2 → (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (ω : W 3) :
    ∑ μ : Fin 2 → Fin 4, (∏ i, ehom (e i) (μ i)) * pairCarrierEquiv ω μ =
      prodEffVal (e 0) (e 1) ω := by
  rw [prodEffVal, pairVal, ← Fintype.sum_prod_type']
  refine Fintype.sum_equiv (finTwoArrowEquiv (Fin 4)) _ _ fun μ => ?_
  show (∏ i, ehom (e i) (μ i)) * ω (μ 0) (μ 1) =
    ehom (e 0) (μ 0) * ω (μ 0) (μ 1) * ehom (e 1) (μ 1)
  rw [Fin.prod_univ_two]
  ring

/-- Transport 2: the maximal cone, both directions. -/
theorem pairCarrierEquiv_maxCone {ω : W 3} (hω : ω ∈ maxCone (OIBridge.TransitiveBody.eball 3)) :
    pairCarrierEquiv ω ∈ maxConeK (OIBridge.TransitiveBody.eball 3) := by
  intro e he
  rw [sum_pairCarrier_eq]
  exact hω (e 0) (e 1) (he 0) (he 1)

theorem maxCone_of_pairCarrierEquiv {ω : W 3}
    (hω : pairCarrierEquiv ω ∈ maxConeK (OIBridge.TransitiveBody.eball 3)) :
    ω ∈ maxCone (OIBridge.TransitiveBody.eball 3) := by
  intro e f he hf
  have h := hω ![e, f] (fun i => by fin_cases i; exacts [he, hf])
  rwa [sum_pairCarrier_eq] at h

theorem dictK_pairCarrier (ω : W 3) (a b : Fin 2 → Fin 2) :
    dictK (pairCarrierEquiv ω) a b = dict ω (a 0, a 1) (b 0, b 1) := by
  rw [dict_apply, ← Fintype.sum_prod_type']
  simp only [dictK, Matrix.sum_apply, Matrix.smul_apply, Matrix.of_apply, smul_eq_mul]
  refine Fintype.sum_equiv (finTwoArrowEquiv (Fin 4)) _ _ fun μ => ?_
  show ((pairCarrierEquiv ω μ : ℝ) : ℂ) / 2 ^ 2 * ∏ i, pauli (μ i) (a i) (b i) =
    ((ω (μ 0) (μ 1) : ℝ) : ℂ) / 4 * (pauli (μ 0) (a 0) (b 0) * pauli (μ 1) (a 1) (b 1))
  rw [Fin.prod_univ_two, pairCarrierEquiv_apply]
  norm_num

/-- Transport 3: the positive semidefinite tables. -/
theorem mem_Q3_iff_pairCarrier (ω : W 3) : ω ∈ Q3 ↔ pairCarrierEquiv ω ∈ QK 2 := by
  have h : dictK (pairCarrierEquiv ω) =
      (dict ω).submatrix (finTwoArrowEquiv (Fin 2)) (finTwoArrowEquiv (Fin 2)) := by
    ext a b
    exact dictK_pairCarrier ω a b
  have h2 : ((dict ω).submatrix (finTwoArrowEquiv (Fin 2)) (finTwoArrowEquiv (Fin 2))).PosSemidef ↔
      (dict ω).PosSemidef := Matrix.posSemidef_submatrix_equiv _
  rw [← h] at h2
  exact h2.symm

/-- Transport 4: the gate. -/
theorem pairCarrierEquiv_cnot (ω : W 3) :
    pairCarrierEquiv (cnot ω) = cnotK 0 1 (pairCarrierEquiv ω) := by
  funext μ
  show sgn (μ 0) (μ 1) * ω (pc (μ 0) (μ 1)) (pt (μ 0) (μ 1)) =
    sgn (μ 0) (μ 1) * ω (cnotLabF 0 1 μ 0) (cnotLabF 0 1 μ 1)
  rw [cnotLabF_i (show (0 : Fin 2) ≠ 1 by decide), cnotLabF_j]

/-- Transport 5: the target-token actions. -/
theorem pairCarrierEquiv_actT (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : W 3) :
    pairCarrierEquiv (actT N ω) = actK 1 N (pairCarrierEquiv ω) := by
  funext μ
  show homMap N (ω (μ 0)) (μ 1) =
    homMap N (fun m : Fin 4 => ω (Function.update μ 1 m 0) (Function.update μ 1 m 1)) (μ 1)
  simp only [Function.update_self, Function.update_of_ne (show (0 : Fin 2) ≠ 1 by decide)]

theorem fin2_lt : ∀ i j : Fin 2, i < j → i = 0 ∧ j = 1 := by decide

theorem fin2_ne_zero : ∀ j : Fin 2, (j : ℕ) ≠ 0 → j = 1 := by decide

/-- The `Fin`-indexed tables of a set of pair tables. -/
def pairSet (K : Set (W 3)) : Set (WK 2) := {η | pairCarrierEquiv.symm η ∈ K}

/-- **The k = 2 recovery**: the statement of the landed two-token generator theorem, proved from
the k-token theorem `kCone_eq_QK_of_drive_maxCone` through the five transports. -/
theorem pairCone_eq_Q3_of_kToken {K : Set (W 3)}
    (hH1 : ∀ x ∈ OIBridge.TransitiveBody.eball 3, ∀ y ∈ OIBridge.TransitiveBody.eball 3,
      prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
      actT (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = Q3 := by
  have hmem : ∀ ω : W 3, pairCarrierEquiv ω ∈ pairSet K ↔ ω ∈ K := fun ω => by
    show pairCarrierEquiv.symm (pairCarrierEquiv ω) ∈ K ↔ ω ∈ K
    rw [LinearEquiv.symm_apply_apply]
  have hK : pairSet K = QK 2 := kCone_eq_QK_of_drive_maxCone
    (fun x hx => by
      show pairCarrierEquiv.symm (prodStateK x) ∈ K
      rw [← pairCarrierEquiv_prodState x, LinearEquiv.symm_apply_apply]
      exact hH1 (x 0) (hx 0) (x 1) (hx 1))
    (fun η hη η' hη' => by
      show pairCarrierEquiv.symm (η + η') ∈ K
      rw [map_add]
      exact hadd (pairCarrierEquiv.symm η) hη (pairCarrierEquiv.symm η') hη')
    (fun c hc η hη => by
      show pairCarrierEquiv.symm (c • η) ∈ K
      rw [LinearEquiv.map_smul]
      exact hsmul c hc (pairCarrierEquiv.symm η) hη)
    (fun η hη => by
      have h := pairCarrierEquiv_maxCone (hmax (show pairCarrierEquiv.symm η ∈ K from hη))
      rwa [LinearEquiv.apply_symm_apply] at h)
    (fun i j hij η hη => by
      obtain ⟨rfl, rfl⟩ := fin2_lt i j hij
      show pairCarrierEquiv.symm (cnotK 0 1 η) ∈ K
      rw [← LinearEquiv.apply_symm_apply pairCarrierEquiv η, ← pairCarrierEquiv_cnot,
        LinearEquiv.symm_apply_apply]
      exact hH2 (pairCarrierEquiv.symm η) hη)
    (fun j hj t η hη => by
      obtain rfl := fin2_ne_zero j hj
      refine ⟨?_, ?_⟩
      · show pairCarrierEquiv.symm (actK 1 (OIBridge.KInfFoundations.rotLin t) η) ∈ K
        rw [← LinearEquiv.apply_symm_apply pairCarrierEquiv η, ← pairCarrierEquiv_actT,
          LinearEquiv.symm_apply_apply]
        exact (hA t (pairCarrierEquiv.symm η) hη).1
      · show pairCarrierEquiv.symm (actK 1
          (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) η) ∈ K
        rw [← LinearEquiv.apply_symm_apply pairCarrierEquiv η, ← pairCarrierEquiv_actT,
          LinearEquiv.symm_apply_apply]
        exact (hA t (pairCarrierEquiv.symm η) hη).2)
  ext ω
  rw [← hmem, hK, ← mem_Q3_iff_pairCarrier]

/- The two-token generator theorem of the adopted `EqvK2MaxCone` module is not in this
module's environment, so the recovery above neither cites it nor cites anything proved
from it. -/
open Lean Meta in
#eval show MetaM Unit from do
  if (← getEnv).contains `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone then
    throwError "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is in the environment"
  logInfo "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is not in the environment"

#print axioms pauliWord_apply
#print axioms dictionary_tabOf
#print axioms mem_QK_iff
#print axioms tupOf_prodTab
#print axioms sum_prodTab_tupOf
#print axioms cnotM_apply
#print axioms pauli_cnot_pair
#print axioms dictK_cflip
#print axioms tabAct_cnotM
#print axioms tabAct_cnotM_eq
#print axioms localM_conj_dictionary
#print axioms tabAct_localM
#print axioms tabAct_localM_eq
#print axioms tabAct_rotK
#print axioms tabAct_cycK
#print axioms tableCone_subset_psd_of_maxCone_drive
#print axioms psd_subset_tableCone_of_products_cone_drive
#print axioms subset_QK_of_maxCone_drive
#print axioms QK_subset_of_products_cone_drive
#print axioms kCone_eq_QK_of_drive_maxCone
#print axioms driveInvariantK_of_eq_QK
#print axioms kCone_eq_QK_iff_drive_maxCone
#print axioms pairCarrierEquiv_prodState
#print axioms pairCarrierEquiv_maxCone
#print axioms maxCone_of_pairCarrierEquiv
#print axioms mem_Q3_iff_pairCarrier
#print axioms pairCarrierEquiv_cnot
#print axioms pairCarrierEquiv_actT
#print axioms pairCone_eq_Q3_of_kToken

/-! ### §12 — product-vector tests give the effect form of the product bound -/

/-- The Bloch vector of `(a, p + i q)` for real `a`, `p`, `q`. -/
theorem blochH_real (a p q : ℝ) :
    blochH ![(a : ℂ), (p : ℂ) + (q : ℂ) * Complex.I] =
      ![a ^ 2 + p ^ 2 + q ^ 2, 2 * a * p, 2 * a * q, a ^ 2 - p ^ 2 - q ^ 2] := by
  funext μ
  fin_cases μ <;>
    simp [blochH, Complex.normSq_apply, Complex.mul_re, Complex.mul_im] <;>
    ring

/-- The Bloch vector of `|1⟩`. -/
theorem blochH_down : blochH ![(0 : ℂ), 1] = ![1, 0, 0, -1] := by
  funext μ
  fin_cases μ <;> simp [blochH, Complex.normSq_apply]

/-- **Forward-cone vectors are nonnegative combinations of two Bloch vectors.** -/
theorem lor_blochH_decomp {v : HVec 3} (hv : Lor v) : ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧
    ∃ u u' : Fin 2 → ℂ, v = α • blochH u + β • blochH u' := by
  have h0 : 0 ≤ v 0 := hv.1
  have h2' : v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 ≤ v 0 ^ 2 := by
    have h := hv.2
    rw [Fin.sum_univ_three] at h
    exact h
  by_cases hz : v 0 + v 3 = 0
  · have hv3 : v 3 = -v 0 := by linarith
    have h33 : v 3 ^ 2 = v 0 ^ 2 := by rw [hv3]; ring
    have h12 : v 1 ^ 2 + v 2 ^ 2 ≤ 0 := by linarith
    have hv1 : v 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp
      (le_antisymm (by linarith [sq_nonneg (v 2)]) (sq_nonneg _))
    have hv2 : v 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp
      (le_antisymm (by linarith [sq_nonneg (v 1)]) (sq_nonneg _))
    refine ⟨0, v 0, le_rfl, h0, ![(0 : ℂ), 1], ![(0 : ℂ), 1], ?_⟩
    rw [blochH_down, zero_smul, zero_add]
    funext μ
    fin_cases μ
    · show v 0 = v 0 * 1
      rw [mul_one]
    · show v 1 = v 0 * 0
      rw [mul_zero, hv1]
    · show v 2 = v 0 * 0
      rw [mul_zero, hv2]
    · show v 3 = v 0 * -1
      rw [hv3, mul_neg_one]
  · have hne : v 0 + v 3 ≠ 0 := hz
    have h33 : v 3 ^ 2 ≤ v 0 ^ 2 := by linarith [sq_nonneg (v 1), sq_nonneg (v 2)]
    have hpos : 0 < v 0 + v 3 :=
      lt_of_le_of_ne (by linarith [(abs_le_of_sq_le_sq' h33 h0).1]) (Ne.symm hne)
    have hc : (0 : ℝ) < 2 * (v 0 + v 3) := by linarith
    have hc0 : 2 * (v 0 + v 3) ≠ 0 := ne_of_gt hc
    have hβ : 0 ≤ v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2 := by linarith
    have key : (2 * (v 0 + v 3)) • v =
        (4 : ℝ) • blochH ![(((v 0 + v 3) / 2 : ℝ) : ℂ),
          ((v 1 / 2 : ℝ) : ℂ) + ((v 2 / 2 : ℝ) : ℂ) * Complex.I] +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) • blochH ![(0 : ℂ), 1] := by
      rw [blochH_real, blochH_down]
      funext μ
      fin_cases μ
      · show 2 * (v 0 + v 3) * v 0 =
          4 * (((v 0 + v 3) / 2) ^ 2 + (v 1 / 2) ^ 2 + (v 2 / 2) ^ 2) +
            (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 1
        ring
      · show 2 * (v 0 + v 3) * v 1 = 4 * (2 * ((v 0 + v 3) / 2) * (v 1 / 2)) +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 0
        ring
      · show 2 * (v 0 + v 3) * v 2 = 4 * (2 * ((v 0 + v 3) / 2) * (v 2 / 2)) +
          (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * 0
        ring
      · show 2 * (v 0 + v 3) * v 3 =
          4 * (((v 0 + v 3) / 2) ^ 2 - (v 1 / 2) ^ 2 - (v 2 / 2) ^ 2) +
            (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2) * -1
        ring
    refine ⟨(2 * (v 0 + v 3))⁻¹ * 4,
      (2 * (v 0 + v 3))⁻¹ * (v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2),
      mul_nonneg (inv_nonneg.mpr hc.le) (by norm_num), mul_nonneg (inv_nonneg.mpr hc.le) hβ,
      ![(((v 0 + v 3) / 2 : ℝ) : ℂ), ((v 1 / 2 : ℝ) : ℂ) + ((v 2 / 2 : ℝ) : ℂ) * Complex.I],
      ![(0 : ℂ), 1], ?_⟩
    calc v = (2 * (v 0 + v 3))⁻¹ • (2 * (v 0 + v 3)) • v := (inv_smul_smul₀ hc0 v).symm
      _ = _ := by rw [key, smul_add, smul_smul, smul_smul]

/-- The slice of a table along a homogeneous vector on the last token. -/
def tokSlice {n : ℕ} (u : HVec 3) (w : Labels (n + 1) → ℝ) : Labels n → ℝ :=
  fun ν => ∑ m : Fin 4, u m * w (ν, m)

theorem sum_prodTab_succ (n : ℕ) (v : ℕ → HVec 3) (w : Labels (n + 1) → ℝ) :
    ∑ μ, prodTab (n + 1) v μ * w μ = ∑ ν, prodTab n v ν * tokSlice (v n) w ν := by
  simp only [Fintype.sum_prod_type, prodTab_succ, tokSlice, Finset.mul_sum]
  refine Finset.sum_congr rfl fun ν _ => Finset.sum_congr rfl fun m _ => ?_
  ring

theorem tokSlice_add {n : ℕ} (u u' : HVec 3) (w : Labels (n + 1) → ℝ) :
    tokSlice (u + u') w = tokSlice u w + tokSlice u' w := by
  funext ν
  simp only [tokSlice, Pi.add_apply, add_mul, Finset.sum_add_distrib]

theorem tokSlice_smul {n : ℕ} (c : ℝ) (u : HVec 3) (w : Labels (n + 1) → ℝ) :
    tokSlice (c • u) w = c • tokSlice u w := by
  funext ν
  simp only [tokSlice, Pi.smul_apply, smul_eq_mul, Finset.mul_sum, mul_assoc]

/-- Nonnegativity on every product of Bloch vectors gives nonnegativity on every product of
forward-cone vectors. -/
theorem lorTests_of_blochTests : ∀ (n : ℕ) (w : Labels n → ℝ),
    (∀ a : ℕ → Fin 2 → ℂ, 0 ≤ ∑ μ, prodTab n (fun i => blochH (a i)) μ * w μ) →
    ∀ v : ℕ → HVec 3, (∀ i, i < n → Lor (v i)) → 0 ≤ ∑ μ, prodTab n v μ * w μ
  | 0, _, hw, _, _ => hw (fun _ => ket0)
  | n + 1, w, hw, v, hv => by
    obtain ⟨α, β, hα, hβ, u, u', hvn⟩ := lor_blochH_decomp (hv n (Nat.lt_succ_self n))
    have hslice : ∀ u0 : Fin 2 → ℂ, 0 ≤ ∑ ν, prodTab n v ν * tokSlice (blochH u0) w ν := by
      intro u0
      refine lorTests_of_blochTests n (tokSlice (blochH u0) w) (fun a => ?_) v
        (fun i hi => hv i (Nat.lt_succ_of_lt hi))
      have h := hw (fun i => if i = n then u0 else a i)
      rw [sum_prodTab_succ] at h
      have hp : prodTab n (fun i => blochH (if i = n then u0 else a i)) =
          prodTab n (fun i => blochH (a i)) :=
        prodTab_congr n fun i hi => congrArg blochH (if_neg (Nat.ne_of_lt hi))
      rw [hp, if_pos (rfl : n = n)] at h
      exact h
    have key : ∀ (x y : HVec 3) (c e : ℝ),
        ∑ ν, prodTab n v ν * tokSlice (c • x + e • y) w ν =
          c * ∑ ν, prodTab n v ν * tokSlice x w ν + e * ∑ ν, prodTab n v ν * tokSlice y w ν := by
      intro x y c e
      rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun ν _ => ?_
      simp only [tokSlice_add, tokSlice_smul, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
      ring
    rw [sum_prodTab_succ, hvn, key]
    exact add_nonneg (mul_nonneg hα (hslice u)) (mul_nonneg hβ (hslice u'))

/-- **Product-vector tests give the effect form**, on tables. -/
theorem maxConeTab_of_blochTests {k : ℕ} {w : Labels k → ℝ}
    (hw : ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ ∑ μ, prodTab k (fun i => blochH (a i)) μ * w μ) :
    w ∈ maxConeTab k := by
  intro e he
  exact lorTests_of_blochTests k w hw (fun i => ehom (e i)) fun i hi => lor_ehom (he i hi)

/-- **Product-vector tests give the effect form**, on Hermitian matrices: the converse of
`prodVec_nonneg_of_maxConeTab`. -/
theorem maxConeTab_of_prodVec_nonneg {k : ℕ} {A : Mat k} (hA : A.IsHermitian)
    (h : ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a)) :
    coordinates k A ∈ maxConeTab k := by
  refine maxConeTab_of_blochTests fun a => ?_
  have ha := h a
  rw [← dictionary_coordinates_real k A hA, quad_dictionary_prodVec,
    show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
        (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
          2 ^ k : ℝ) : ℂ) by push_cast; ring,
    Complex.zero_le_real] at ha
  by_contra hneg
  exact absurd ha (not_le.mpr (div_neg_of_neg_of_pos (not_le.mp hneg)
    (pow_pos (by norm_num) k)))

/-- The effect form gives the product-vector tests, on Hermitian matrices. -/
theorem prodVec_nonneg_of_maxConeTab {k : ℕ} {A : Mat k} (hA : A.IsHermitian)
    (h : coordinates k A ∈ maxConeTab k) (a : ℕ → Fin 2 → ℂ) :
    0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) := by
  rw [← dictionary_coordinates_real k A hA, quad_dictionary_prodVec]
  have hS := lorPair_nonneg_of_maxConeTab (v := fun i => blochH (a i)) h
    fun i _ => lor_blochH (a i)
  rw [show ((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ : ℝ) : ℂ) /
      (2 : ℂ) ^ k = (((∑ μ, prodTab k (fun i => blochH (a i)) μ * coordinates k A μ) /
        2 ^ k : ℝ) : ℂ) by push_cast; ring,
    Complex.zero_le_real]
  exact div_nonneg hS (pow_nonneg (by norm_num) k)

/-- **The "equivalently" of the product bound.** For a Hermitian matrix, nonnegativity on every
product of ball effects is equivalent to nonnegative expectation on every product vector.
Witnesses: `prodVec_nonneg_of_maxConeTab` (→) and `maxConeTab_of_prodVec_nonneg` (←). -/
theorem maxConeTab_iff_prodVec_nonneg {k : ℕ} {A : Mat k} (hA : A.IsHermitian) :
    coordinates k A ∈ maxConeTab k ↔
      ∀ a : ℕ → Fin 2 → ℂ, 0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a) :=
  ⟨fun h => prodVec_nonneg_of_maxConeTab hA h, maxConeTab_of_prodVec_nonneg hA⟩

#print axioms blochH_real
#print axioms lor_blochH_decomp
#print axioms lorTests_of_blochTests
#print axioms maxConeTab_of_blochTests
#print axioms maxConeTab_of_prodVec_nonneg
#print axioms prodVec_nonneg_of_maxConeTab
#print axioms maxConeTab_iff_prodVec_nonneg

end
end OIBridge.KTokenMaxCone
