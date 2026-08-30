/-
  OIBridge/Separability.lean — the Choi matrix, partial transpose, separability, and PPT.

      Separable M  ⟹  (partial transpose of M) is positive semidefinite.

  LAYER 2 of [Main] Theorem (separability threshold). Deliberately narrow: this is not a quantum
  information library. It defines exactly the four objects that theorem needs and proves exactly
  the one implication that its harder direction consumes.

  WHY THIS DEFINITION OF SEPARABILITY. The separable cone is defined as the set of FINITE SUMS OF
  PURE PRODUCT PROJECTORS — no convexity library, no closure, no partial-trace theory. Nonnegative
  weights are absorbed into the vectors (`√c` into `x`), which is why the definition carries no
  coefficients; `separable_of_conic` supplies the weighted form as a constructor so a consumer can
  write the decomposition either way. That choice makes BOTH directions of the theorem
  constructive: the maximal case exhibits a decomposition, and the non-maximal case exhibits a
  negative eigenvalue of the partial transpose, with `separable_imp_ppt` in between. Defining
  separability by measure-and-prepare instead would leave the converse needing duality.

  POSITIVITY IS DEFINED HERE, not imported. Mathlib's `Matrix.PosSemidef` needs the order on ℂ,
  which lives only in the `ComplexOrder` scope and does not resolve cleanly here; and the two
  directions of the theorem want positivity in exactly one form — the quadratic form is a
  nonnegative real. `PosSemidefOn` says that and nothing else, which is also what makes the
  non-maximal direction's refutation a single vector rather than a spectral argument.

  THE INDEX CONVENTION IS AN ACCEPTANCE GATE. Partial transpose swaps the SECOND factor's indices
  only; the Choi matrix puts the untouched ancilla first and the output second. Transpose versus
  conjugate transpose is invisible on real matrices, so the companion probe checks both against
  genuinely complex vectors — the same discipline `KrausUniqueness.krausMatrix_eq_transpose`
  applies to the Kraus index order.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Basis
import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Data.Complex.Basic
import Mathlib.Data.Complex.BigOperators
import Mathlib.Algebra.Star.BigOperators
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace OIBridge

namespace Separability

set_option autoImplicit false

/- Several statements are pure index bookkeeping and do not use the finiteness assumptions; they
share the section variables because they exist to serve `separable_imp_ppt`, which does. -/
set_option linter.unusedSectionVars false

open Matrix

variable {m n : Type*} [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n]

/-! ### Product vectors and product projectors -/

/-- The product vector `x ⊗ y`. -/
def prodVec (x : m → ℂ) (y : n → ℂ) : m × n → ℂ := fun p => x p.1 * y p.2

/-- The pure product projector `|x⟩⟨x| ⊗ |y⟩⟨y|`. -/
def prodProj (x : m → ℂ) (y : n → ℂ) : Matrix (m × n) (m × n) ℂ :=
  vecMulVec (prodVec x y) (star (prodVec x y))

@[simp] theorem prodProj_apply (x : m → ℂ) (y : n → ℂ) (p q : m × n) :
    prodProj x y p q = (x p.1 * y p.2) * star (x q.1 * y q.2) := rfl

/-! ### Positivity, in the one form this file needs -/

/-- The quadratic form of a matrix at a vector. -/
def qform (M : Matrix (m × n) (m × n) ℂ) (w : m × n → ℂ) : ℂ :=
  ∑ p, ∑ q, star (w p) * M p q * w q

theorem qform_sum {k : ℕ} (f : Fin k → Matrix (m × n) (m × n) ℂ) (w : m × n → ℂ) :
    qform (∑ r, f r) w = ∑ r, qform (f r) w := by
  simp only [qform, Matrix.sum_apply]
  have h1 : ∀ p q : m × n, star (w p) * (∑ r, f r p q) * w q
      = ∑ r, star (w p) * f r p q * w q := fun p q => by
    rw [Finset.mul_sum, Finset.sum_mul]
  simp only [h1]
  rw [Finset.sum_congr rfl fun p (_ : p ∈ Finset.univ) => Finset.sum_comm, Finset.sum_comm]

/-- **Positive semidefiniteness**: the quadratic form is a nonnegative real at every vector. -/
def PosSemidefOn (M : Matrix (m × n) (m × n) ℂ) : Prop :=
  ∀ w : m × n → ℂ, 0 ≤ (qform M w).re ∧ (qform M w).im = 0

theorem posSemidefOn_sum {k : ℕ} {f : Fin k → Matrix (m × n) (m × n) ℂ}
    (h : ∀ r, PosSemidefOn (f r)) : PosSemidefOn (∑ r, f r) := by
  intro w
  rw [qform_sum]
  constructor
  · rw [Complex.re_sum]
    exact Finset.sum_nonneg fun r _ => (h r w).1
  · rw [Complex.im_sum]
    exact Finset.sum_eq_zero fun r _ => (h r w).2


/-- **The quadratic form of a pure product projector is a modulus squared.** -/
theorem qform_prodProj (x : m → ℂ) (y : n → ℂ) (w : m × n → ℂ) :
    qform (prodProj x y) w
      = (∑ p, star (w p) * (x p.1 * y p.2))
        * star (∑ p, star (w p) * (x p.1 * y p.2)) := by
  rw [qform]
  have hrow : ∀ p : m × n, (∑ q, star (w p) * (prodProj x y p q) * w q)
      = (star (w p) * (x p.1 * y p.2)) * ∑ q, star (x q.1 * y q.2) * w q := fun p => by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun q _ => by simp only [prodProj_apply]; ring
  rw [Finset.sum_congr rfl fun p (_ : p ∈ Finset.univ) => hrow p, ← Finset.sum_mul]
  congr 1
  rw [star_sum]
  exact Finset.sum_congr rfl fun q _ => by simp only [star_mul', star_star]; ring

/-- `z · z̄` is a nonnegative real — the only positivity fact this file needs. -/
theorem mul_star_self (z : ℂ) : 0 ≤ (z * star z).re ∧ (z * star z).im = 0 := by
  have h : z * star z = ((Complex.normSq z : ℝ) : ℂ) := Complex.mul_conj z
  rw [h]
  exact ⟨by simpa using Complex.normSq_nonneg z, by simp⟩

/-- A pure product projector is positive semidefinite. -/
theorem prodProj_posSemidefOn (x : m → ℂ) (y : n → ℂ) : PosSemidefOn (prodProj x y) := by
  intro w
  rw [qform_prodProj]
  exact mul_star_self _

/-! ### Separability

A finite sum of pure product projectors. Nonnegative weights are absorbed into the vectors, which
is what keeps the definition free of a convexity library. -/

/-- **Separability.** -/
def Separable (M : Matrix (m × n) (m × n) ℂ) : Prop :=
  ∃ (k : ℕ) (x : Fin k → (m → ℂ)) (y : Fin k → (n → ℂ)),
    M = ∑ r, prodProj (x r) (y r)

/-- A nonnegative real weight is absorbed by scaling the first vector by its square root. -/
theorem prodProj_smul (c : ℝ) (hc : 0 ≤ c) (x : m → ℂ) (y : n → ℂ) :
    (c : ℂ) • prodProj x y = prodProj ((Real.sqrt c : ℂ) • x) y := by
  refine Matrix.ext fun p q => ?_
  have hs : star ((Real.sqrt c : ℂ)) = (Real.sqrt c : ℂ) := by simp
  have hsq : (Real.sqrt c : ℂ) * (Real.sqrt c : ℂ) = (c : ℂ) := by
    rw [← Complex.ofReal_mul, Real.mul_self_sqrt hc]
  simp only [prodProj_apply, Matrix.smul_apply, Pi.smul_apply, smul_eq_mul, star_mul', hs]
  rw [← hsq]
  ring

/-- **A decomposition indexed by any finite type.** The definition uses `Fin k` so that it stays a
plain finite sum; a consumer whose decomposition is naturally indexed by characters, or by anything
else finite, reindexes through this. -/
theorem separable_of_fintype {ι : Type*} [Fintype ι] {M : Matrix (m × n) (m × n) ℂ}
    (x : ι → (m → ℂ)) (y : ι → (n → ℂ)) (hM : M = ∑ r, prodProj (x r) (y r)) : Separable M := by
  classical
  refine ⟨Fintype.card ι, fun r => x ((Fintype.equivFin ι).symm r),
    fun r => y ((Fintype.equivFin ι).symm r), ?_⟩
  rw [hM]
  exact (Fintype.sum_equiv (Fintype.equivFin ι).symm
    (fun r => prodProj (x ((Fintype.equivFin ι).symm r)) (y ((Fintype.equivFin ι).symm r)))
    (fun i => prodProj (x i) (y i)) fun _ => rfl).symm

/-- **The weighted form is the same cone.** A consumer may present a decomposition with
nonnegative weights; they are absorbed, so the definition itself carries none. -/
theorem separable_of_conic {M : Matrix (m × n) (m × n) ℂ} {k : ℕ} (c : Fin k → ℝ)
    (x : Fin k → (m → ℂ)) (y : Fin k → (n → ℂ)) (hc : ∀ r, 0 ≤ c r)
    (hM : M = ∑ r, (c r : ℂ) • prodProj (x r) (y r)) : Separable M :=
  ⟨k, fun r => (Real.sqrt (c r) : ℂ) • x r, y,
   hM.trans (Finset.sum_congr rfl fun r _ => prodProj_smul (c r) (hc r) (x r) (y r))⟩

/-- Separable matrices are positive semidefinite. -/
theorem Separable.posSemidefOn {M : Matrix (m × n) (m × n) ℂ} (h : Separable M) :
    PosSemidefOn M := by
  obtain ⟨k, x, y, rfl⟩ := h
  exact posSemidefOn_sum fun r => prodProj_posSemidefOn (x r) (y r)

/-! ### Partial transpose

Transposing the SECOND factor only. The convention is fixed here once and checked numerically
against complex vectors, because transpose and conjugate transpose agree on real matrices and a
mistake between them would otherwise be invisible. -/

/-- **Partial transpose on the second factor.** -/
def ptranspose (M : Matrix (m × n) (m × n) ℂ) : Matrix (m × n) (m × n) ℂ :=
  fun p q => M (p.1, q.2) (q.1, p.2)

@[simp] theorem ptranspose_apply (M : Matrix (m × n) (m × n) ℂ) (p q : m × n) :
    ptranspose M p q = M (p.1, q.2) (q.1, p.2) := rfl

theorem ptranspose_sum {k : ℕ} (f : Fin k → Matrix (m × n) (m × n) ℂ) :
    ptranspose (∑ r, f r) = ∑ r, ptranspose (f r) := by
  refine Matrix.ext fun p q => ?_
  simp [ptranspose, Matrix.sum_apply]

/-- **The key identity.** Partial transposition conjugates the second factor:
`(|x⟩⟨x| ⊗ |y⟩⟨y|)^Γ = |x⟩⟨x| ⊗ |ȳ⟩⟨ȳ|`. This is the whole reason separability survives it. -/
theorem ptranspose_prodProj (x : m → ℂ) (y : n → ℂ) :
    ptranspose (prodProj x y) = prodProj x (star y) := by
  refine Matrix.ext fun p q => ?_
  simp only [ptranspose_apply, prodProj_apply, Pi.star_apply, star_mul', star_star]
  ring

/-- **Separable ⟹ PPT.** -/
theorem separable_imp_ppt {M : Matrix (m × n) (m × n) ℂ} (h : Separable M) :
    PosSemidefOn (ptranspose M) := by
  obtain ⟨k, x, y, rfl⟩ := h
  rw [ptranspose_sum]
  refine posSemidefOn_sum fun r => ?_
  rw [ptranspose_prodProj]
  exact prodProj_posSemidefOn _ _

/-- **The contrapositive, in the form the non-maximal direction uses.** A single vector on which
the partial transpose is negative certifies non-separability. -/
theorem not_separable_of_neg {M : Matrix (m × n) (m × n) ℂ} {w : m × n → ℂ}
    (h : (qform (ptranspose M) w).re < 0) : ¬ Separable M :=
  fun hs => absurd (separable_imp_ppt hs w).1 (not_le.2 h)

/-! ### The Choi matrix and entanglement breaking

The Choi matrix carries the untouched ancilla index first and the output second, matching the
bipartition separability is stated across. -/

/-- **The Choi matrix** of a map on `n × n` matrices: `J(Φ)((i,a),(j,b)) = Φ(E_{ij})_{ab}`. -/
def choi (Φ : Matrix n n ℂ → Matrix n n ℂ) : Matrix (n × n) (n × n) ℂ :=
  fun p q => Φ (Matrix.single p.1 q.1 1) p.2 q.2

@[simp] theorem choi_apply (Φ : Matrix n n ℂ → Matrix n n ℂ) (p q : n × n) :
    choi Φ p q = Φ (Matrix.single p.1 q.1 1) p.2 q.2 := rfl

/-- The Choi matrix is linear in the map: a channel presented as a finite sum of pieces has the
sum of their Choi matrices. -/
theorem choi_sum {ι : Type*} [Fintype ι] (Ψ : ι → (Matrix n n ℂ → Matrix n n ℂ)) :
    choi (fun ρ => ∑ e, Ψ e ρ) = ∑ e, choi (Ψ e) := by
  refine Matrix.ext fun p q => ?_
  rw [choi_apply, Matrix.sum_apply]
  simp only [Matrix.sum_apply, choi_apply]

/-- **The Choi matrix of a single conjugation `ρ ↦ M ρ M†` with `M` of rank one is a pure product
projector.** Rank one is used only through the entrywise factorization `M a i = x a · y i`, which
is why the maximal case never needs normalized eigenvectors, an orthonormal basis, or a square
root. Note the index order: the Choi ancilla index picks up `y` and the output index `x`. -/
theorem choi_conj_of_factor (M : Matrix n n ℂ) (x y : n → ℂ) (hM : ∀ a i, M a i = x a * y i) :
    choi (fun ρ => M * ρ * Mᴴ) = prodProj y x := by
  refine Matrix.ext fun p q => ?_
  have hentry : ∀ a b : n,
      (M * Matrix.single p.1 q.1 (1 : ℂ) * Mᴴ : Matrix n n ℂ) a b
        = M a p.1 * star (M b q.1) := by
    intro a b
    rw [Matrix.mul_apply, Finset.sum_eq_single q.1]
    · rw [Matrix.mul_single_apply_same, mul_one, Matrix.conjTranspose_apply]
    · intro l _ hl
      rw [Matrix.mul_single_apply_of_ne _ _ _ _ _ hl, zero_mul]
    · intro hc; exact absurd (Finset.mem_univ _) hc
  rw [choi_apply, hentry, prodProj_apply, hM, hM]
  simp only [star_mul']
  ring

/-- **Entanglement breaking**: the Choi matrix is separable. -/
def EntanglementBreaking (Φ : Matrix n n ℂ → Matrix n n ℂ) : Prop := Separable (choi Φ)

/-- The form the non-maximal direction will discharge: one negative direction of the partially
transposed Choi matrix refutes entanglement breaking. -/
theorem not_eb_of_neg_witness {Φ : Matrix n n ℂ → Matrix n n ℂ} {w : n × n → ℂ}
    (h : (qform (ptranspose (choi Φ)) w).re < 0) : ¬ EntanglementBreaking Φ :=
  not_separable_of_neg h

/-! ### What these proofs rest on -/

#print axioms mul_star_self
#print axioms qform_prodProj
#print axioms prodProj_posSemidefOn
#print axioms prodProj_smul
#print axioms separable_of_conic
#print axioms Separable.posSemidefOn
#print axioms ptranspose_prodProj
#print axioms separable_imp_ppt
#print axioms not_separable_of_neg
#print axioms not_eb_of_neg_witness
#print axioms separable_of_fintype
#print axioms choi_sum
#print axioms choi_conj_of_factor

end Separability

end OIBridge
