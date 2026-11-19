/-
  OIBridge/SubstratumInterface.lean — the substratum-source audit, second entry: the interface
  between substratum interventions and implementation operators, and a conditional obstruction.

  ROUND SIXTY-TWO. Round 61 reduced "which conditions select quantum mechanics" to a single
  object — a stable, elementary-driving implementation architecture — and named elementary
  drivability as its decisive property. The stated finite-model interface represents bijective
  interventions by permutation matrices (`bijectiveOperator`) and declared phase interventions
  by diagonal matrices (`phaseOperator`). Both have the form `permMatrix σ · diagonal d`,
  with complex weights that may vanish. Conjugation by such a matrix preserves the diagonal
  subspace (`preservesDiag_conj_of_monomial`).

  On `Fin 2`, `MonomialSource` requires every matrix representative of each available
  composite conjugation to be monomial at every extension level. Composite unitary control
  would make the rational rotation `rot` available at level one. Its first row has two
  nonzero entries (`rot_not_monomial`), so the hypothesis excludes composite unitary control
  (`monomialSource_not_control`) and exact completeness for finite endomorphic quantum
  operations (`monomialSource_not_qm`).

  The rotation proof uses explicit matrix entries and does not compute a matrix exponential.
  The mathematical instance `permTheory (Fin 2)` is established in `ReadWriteNonvacuity.lean`.
  Whether a native physical observer interface satisfies the hypothesis remains open.
  The physical sources of off-diagonal control are investigated in `SUBSTRATUM-SOURCE-AUDIT.md`.
-/

import OIBridge.SubstratumSource

namespace OIBridge
namespace SubstratumInterface

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy PrimitiveSource InterventionLocality
open MicroReversibility LieRankSource SubstratumSource

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — the interface: bijective and phase interventions are monomial -/

section Interface

variable {S : Type} [Fintype S] [DecidableEq S]

/-- A monomial operator is a permutation matrix times a complex diagonal whose weights may
vanish. The two stated intervention types have this form. -/
def IsMonomial (K : Matrix S S ℂ) : Prop :=
  ∃ (σ : Equiv.Perm S) (d : S → ℂ), K = permMatrix σ * Matrix.diagonal d

/-- The observable operator of a bijective intervention (autonomous evolution or a selectable
permutation of the finite states, A2). -/
def bijectiveOperator (σ : Equiv.Perm S) : Matrix S S ℂ := permMatrix σ

/-- The observable operator of a phase intervention. -/
def phaseOperator (d : S → ℂ) : Matrix S S ℂ := Matrix.diagonal d

theorem monomial_permMatrix (σ : Equiv.Perm S) : IsMonomial (permMatrix σ) :=
  ⟨σ, fun _ => 1, by rw [Matrix.diagonal_one, Matrix.mul_one]⟩

theorem monomial_diagonal (d : S → ℂ) : IsMonomial (Matrix.diagonal d) :=
  ⟨1, d, by rw [permMatrix_one', Matrix.one_mul]⟩

theorem bijectiveOperator_monomial (σ : Equiv.Perm S) : IsMonomial (bijectiveOperator σ) :=
  monomial_permMatrix σ

theorem phaseOperator_monomial (d : S → ℂ) : IsMonomial (phaseOperator d) :=
  monomial_diagonal d

/-- A state exchange is represented by a monomial permutation matrix. -/
theorem exchange_monomial (a b : S) : IsMonomial (permMatrix (Equiv.swap a b)) :=
  monomial_permMatrix _

/-- The quarter-phase operator of the stated phase intervention is monomial. -/
theorem phase_monomial (a : S) : IsMonomial (LieRankSource.phaseGate a) :=
  monomial_diagonal _

/-- A product `permMatrix σ · diagonal d` has at most one nonzero entry per row and column. -/
theorem monomial_entry (σ : Equiv.Perm S) (d : S → ℂ) (i j : S) :
    (permMatrix σ * Matrix.diagonal d) i j = if σ j = i then d j else 0 := by
  rw [Matrix.mul_apply, Finset.sum_eq_single j]
  · simp only [Matrix.diagonal_apply_eq, permMatrix]
    split_ifs <;> simp
  · intro k _ hk
    rw [Matrix.diagonal_apply_ne _ hk, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ j) h

end Interface

/-! ### Section B — the monomial invariant -/

section Invariant

variable {S : Type} [Fintype S] [DecidableEq S]

/-- Conjugation by a monomial operator preserves the diagonal subspace. The diagonal weights
rescale its entries and the permutation relabels them. -/
theorem preservesDiag_conj_of_monomial {K : Matrix S S ℂ} (h : IsMonomial K) :
    PreservesDiag (conjChannel K) := by
  obtain ⟨σ, d, rfl⟩ := h
  intro w
  refine ⟨fun s => d (σ.symm s) * w (σ.symm s) * star (d (σ.symm s)), ?_⟩
  rw [conjChannel_apply, Matrix.conjTranspose_mul, Matrix.diagonal_conjTranspose]
  have hmid : Matrix.diagonal d * Matrix.diagonal w * Matrix.diagonal (star d)
      = Matrix.diagonal (fun i => d i * w i * star (d i)) := by
    rw [Matrix.diagonal_mul_diagonal, Matrix.diagonal_mul_diagonal]
    rfl
  calc permMatrix σ * Matrix.diagonal d * Matrix.diagonal w
          * ((Matrix.diagonal (star d)) * (permMatrix σ)ᴴ)
        = permMatrix σ * (Matrix.diagonal d * Matrix.diagonal w * Matrix.diagonal (star d))
          * (permMatrix σ)ᴴ := by
          simp only [Matrix.mul_assoc]
    _ = permMatrix σ * Matrix.diagonal (fun i => d i * w i * star (d i)) * (permMatrix σ)ᴴ := by
          rw [hmid]
    _ = Matrix.diagonal (fun s => d (σ.symm s) * w (σ.symm s) * star (d (σ.symm s))) :=
          permMatrix_conj_diagonal σ _

end Invariant

/-! ### Section C — the conditional monomial-source obstruction on two states -/

section NoGo

/-- The rational two-state rotation `rot` is nonmonomial because its first row has two
nonzero entries. -/
theorem rot_not_monomial : ¬ IsMonomial rot := by
  rintro ⟨σ, d, h⟩
  have e00 : rot (0, 0) (0, 0) = if σ (0, 0) = (0, 0) then d (0, 0) else 0 := by
    rw [h, monomial_entry]
  have e10 : rot (0, 0) (1, 0) = if σ (1, 0) = (0, 0) then d (1, 0) else 0 := by
    rw [h, monomial_entry]
  have v00 : rot (0, 0) (0, 0) = ((3 / 5 : ℝ) : ℂ) := by simp [rot]
  have v10 : rot (0, 0) (1, 0) = ((4 / 5 : ℝ) : ℂ) := by simp [rot]
  have h00 : σ (0, 0) = (0, 0) := by
    by_contra hc
    rw [if_neg hc] at e00
    rw [v00] at e00
    norm_num at e00
  have h10 : σ (1, 0) = (0, 0) := by
    by_contra hc
    rw [if_neg hc] at e10
    rw [v10] at e10
    norm_num at e10
  have : ((0 : Fin 2), (0 : Fin 1)) = ((1 : Fin 2), (0 : Fin 1)) :=
    σ.injective (h00.trans h10.symm)
  simp at this

variable {A : Type} [Fintype A] [DecidableEq A]

/-- Every matrix representative of an available single-outcome composite conjugation is
monomial, at every extension level. -/
def MonomialSource (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → IsMonomial V

/-- On `Fin 2`, `MonomialSource` rules out composite unitary control because such control
would make the nonmonomial rotation `rot` available. -/
theorem monomialSource_not_control (T : FiniteOperationalTheory (Fin 2)) (h : MonomialSource T) :
    ¬ HasCompositeUnitaryControl T := by
  intro hctrl
  exact rot_not_monomial (h 1 rot (hctrl 1 rot rot_isometry))

/-- On `Fin 2`, `MonomialSource` rules out exact completeness for finite endomorphic
quantum operations. -/
theorem monomialSource_not_qm (T : FiniteOperationalTheory (Fin 2)) (h : MonomialSource T) :
    ¬ ExactAllFiniteEndomorphicQuantumOps T :=
  fun hqm => monomialSource_not_control T h (physical_of_exactAll T hqm).2.2.1

/-- State-exchange operators and the named phase operators are monomial. The concrete
rotation `rot` is nonmonomial. -/
theorem elementary_split :
    (∀ (S : Type) [Fintype S] [DecidableEq S] (a b : S), IsMonomial (permMatrix (Equiv.swap a b)))
      ∧ (∀ (S : Type) [Fintype S] [DecidableEq S] (a : S), IsMonomial (LieRankSource.phaseGate a))
      ∧ ¬ IsMonomial rot :=
  ⟨fun _ _ _ a b => exchange_monomial a b, fun _ _ _ a => phase_monomial a, rot_not_monomial⟩

end NoGo

#print axioms monomial_permMatrix
#print axioms monomial_diagonal
#print axioms bijectiveOperator_monomial
#print axioms phaseOperator_monomial
#print axioms exchange_monomial
#print axioms phase_monomial
#print axioms monomial_entry
#print axioms preservesDiag_conj_of_monomial
#print axioms rot_not_monomial
#print axioms monomialSource_not_control
#print axioms monomialSource_not_qm
#print axioms elementary_split

end SubstratumInterface
end OIBridge
