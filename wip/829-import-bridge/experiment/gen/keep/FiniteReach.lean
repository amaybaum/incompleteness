import FinitePauli
import OIBridge.EqvK2Generation

/- Research/design only. Exact pure-state reachability on the recursive k-token carrier
   from CNOT into later tokens and the third-axis flow and cyclic lift off the first token,
   and the two conditional cone inclusions at the Hermitian-matrix level. No physical
   carrier identification, state space or operation source is supplied. -/
namespace FiniteReconstructionDesign

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

attribute [instance high] bitsDecEq

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
end FiniteReconstructionDesign
