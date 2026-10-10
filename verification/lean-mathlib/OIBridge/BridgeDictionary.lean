/-
  OIBridge/BridgeDictionary.lean — design module of the research thread `research/bridge` (node B9).
  Not certified. Built on the disposable branch `dev-bridge/b11-lemma` only; not for merge.

  The two-token dictionary of handoff HO-6, at the table level of DIM-1's pair carrier `W 3`, in the
  kernel's own tensor `tensorOf` (MonoidalCompletion.lean), the operation `ContextStable` uses:
    `tokMat v = ½ Σ v_μ σ_μ`        one token's homogenized vector as a 2 × 2 complex matrix;
    `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν`   a pair table as a 4 × 4 complex matrix.

  Proved here: the product law `dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` (`dict_tens`),
  hence `dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y))` (`dict_prodState`); and,
  restating the certified `substratumClass_contextStable` at the pair carrier, the idle extension
  `tensorOf 1 U` of every monomial `U` on one token is admissible on `Fin 2 × Fin 2`
  (`monomial_extension_admissible`).

  Stated here as a definition (a premise of nothing in this file): the M→P transfer clause
  `TransferClause 𝓘 K` for an implementation class `𝓘` and a pair cone `K ⊆ W 3`: for every admissible
  unitary `U` on the token carrier `Fin 2` and every `ω ∈ K`, conjugation of `dict ω` by the idle
  extension `tensorOf 1 U` is again the dictionary image of a member of `K`. The certified theorem
  supplies admissibility of `tensorOf 1 U`; it says nothing about `K`. The research thread's
  NOTES-B9 records (exact checks, b9 Y3) that for the monomial class the clause is the composite
  action (b) for the phase flow and the NOT on the second token.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositeDimension
import OIBridge.MonoidalCompletion
import OIBridge.ImplementationLocality
import OIBridge.StructuralClosure

namespace OIBridge
namespace BridgeDictionary

open CompositeDimension MonoidalCompletion InterventionLocality StructuralClosure Matrix

/-- The Pauli matrices `σ₀ = 1, σ₁ = X, σ₂ = Y, σ₃ = Z`. -/
noncomputable def pauli : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- One token's homogenized vector as a 2 × 2 complex matrix: `v ↦ ½ Σ v_μ σ_μ`. -/
noncomputable def tokMat (v : HVec 3) : Matrix (Fin 2) (Fin 2) ℂ :=
  ∑ μ : Fin 4, ((v μ : ℂ) / 2) • pauli μ

/-- The two-token dictionary: `ω ↦ ¼ Σ ω_μν σ_μ ⊗ σ_ν`. -/
noncomputable def dict (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • tensorOf (pauli μ) (pauli ν)

/-- **The product law of the dictionary.** -/
theorem dict_tens (X Y : HVec 3) : dict (tens X Y) = tensorOf (tokMat X) (tokMat Y) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [dict, tokMat, tens_apply, Matrix.sum_apply, Matrix.smul_apply, tensorOf_apply,
    smul_eq_mul, Complex.ofReal_mul, Finset.sum_mul, Finset.mul_sum]
  first
    | exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring
    | (simp only [Fin.sum_univ_four]; ring)

/-- The product states of the ball go to Kronecker products of one-token matrices. -/
theorem dict_prodState (x y : Fin 3 → ℝ) :
    dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y)) :=
  dict_tens (hom x) (hom y)

/-- **The certified spectator theorem at the pair carrier**: the idle extension of a monomial
one-token operator is admissible on `Fin 2 × Fin 2` (`substratumClass_contextStable`). -/
theorem monomial_extension_admissible (U : Matrix (Fin 2) (Fin 2) ℂ)
    (hU : substratumClass (Fin 2) U) :
    substratumClass (Fin 2 × Fin 2) (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U) :=
  substratumClass_contextStable (Fin 2) (Fin 2) U hU

/-- **The M→P transfer clause** (a design statement, not a premise of anything here): for every
admissible unitary `U` on one token and every `ω ∈ K`, conjugation of `dict ω` by the idle
extension `tensorOf 1 U` is the dictionary image of a member of `K`. -/
def TransferClause (𝓘 : ImplementationClass) (K : Set (W 3)) : Prop :=
  ∀ U : Matrix (Fin 2) (Fin 2) ℂ, 𝓘 (Fin 2) U → Uᴴ * U = 1 →
    ∀ ω ∈ K, ∃ ω' ∈ K,
      dict ω' = tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ

#print axioms dict_tens
#print axioms dict_prodState
#print axioms monomial_extension_admissible

end BridgeDictionary
end OIBridge
