/-
  OIBridge/SubstratumInterface.lean — the substratum-source audit, second entry: the interface
  between substratum interventions and implementation operators, and the permutation-only no-go.

  ROUND SIXTY-TWO. Round 61 reduced "which conditions select quantum mechanics" to a single
  object — a stable, elementary-driving implementation architecture — and named elementary
  drivability as its decisive property. Before asking whether the concrete OI physics drives
  the elementary transitions, this file settles a type-level prerequisite: what an
  implementation operator supplied by the substratum IS, and a baseline obstruction showing
  that finite bijective dynamics alone does not supply the decisive operator.

  THE INTERFACE. The concrete substratum starts from finite states and bijective dynamics
  (axiom A2) together with a phase structure. Its directly selectable interventions are
  therefore of two kinds: a bijective intervention, whose observable operator is a permutation
  matrix (`bijectiveOperator`, from a permutation of the states), and a phase intervention,
  whose observable operator is a diagonal phase (`phaseOperator`). Both kinds are MONOMIAL —
  one nonzero entry per row and per column (`IsMonomial`, here in the factored form
  `permMatrix σ · diagonal d`). The interface keeps these separate from admissibility: the
  question is not whether a desired matrix has an intervention (that would assume the result),
  but which operators the two kinds of intervention directly supply.

  THE MONOMIAL INVARIANT. A conjugation by a monomial operator preserves diagonal matrices
  (`preservesDiag_conj_of_monomial`): a permutation relabels the diagonal and a phase leaves it
  fixed. So a source that supplies only monomial operators generates only diagonal-preserving
  conjugations, and it cannot create the coherence a genuine two-state rotation produces.

  THE PERMUTATION-ONLY NO-GO. The rational two-state rotation `rot` — a value of the flow of a
  real off-diagonal generator, with every entry nonzero — is not monomial
  (`rot_not_monomial`): its first row already has two nonzero entries, which no permutation of
  a diagonal allows. Hence a theory whose available composite conjugations are all monomial has
  no composite unitary control (`monomialSource_not_control`) and is not finite operational
  quantum mechanics (`monomialSource_not_qm`):

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  finite bijective dynamics alone ⇏ elementary drivability ⇏ operational QM.    │
      └──────────────────────────────────────────────────────────────────────────────┘

  This separates A2 reversibility from the missing physical controllability: bijective dynamics
  supplies the state exchanges and the phase structure supplies the phases — two of the three
  elementary operations (`exchange_monomial`, `phase_monomial`) — but neither supplies the
  continuously driven off-diagonal transition, whose flow values are not monomial.

  WHAT IS NOT CLAIMED. This does not compute a matrix exponential; it uses the concrete rational
  rotation `rot` as the witness that a nontrivial flow of a real off-diagonal generator is not a
  permutation. It does not decide whether the continuous-time extension, the read-write
  coupling, or the gauge/phase structure supplies a non-monomial generator — those candidate
  escape routes are recorded in `SUBSTRATUM-SOURCE-AUDIT.md` as open distinctions. Nothing here
  modifies the frozen OI⁺ statements.
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

/-- **A MONOMIAL OPERATOR**: a permutation of the states composed with a diagonal phase. This is
the observable-operator shape of the substratum's two direct intervention kinds. -/
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

/-- The state exchange is a bijective operator, hence monomial: A2 supplies it. -/
theorem exchange_monomial (a b : S) : IsMonomial (permMatrix (Equiv.swap a b)) :=
  monomial_permMatrix _

/-- The quarter phase is a phase operator, hence monomial: the phase structure supplies it. -/
theorem phase_monomial (a : S) : IsMonomial (LieRankSource.phaseGate a) :=
  monomial_diagonal _

/-- The entry of `permMatrix σ · diagonal d`: a single nonzero per row. -/
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

/-- **A MONOMIAL CONJUGATION PRESERVES THE DIAGONAL**: a permutation relabels it, a phase fixes
it. -/
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

/-! ### Section C — the permutation-only no-go -/

section NoGo

/-- **THE RATIONAL TWO-STATE ROTATION IS NOT MONOMIAL**: its first row has two nonzero entries,
which a permutation of a diagonal cannot produce. `rot` is a value of the flow of a real
off-diagonal generator, so a nontrivial such flow is not a permutation. -/
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

/-- **A MONOMIAL SOURCE**: every available composite conjugation is monomial. -/
def MonomialSource (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → IsMonomial V

/-- **THE PERMUTATION-ONLY NO-GO, CONTROL**: a monomial source has no composite unitary control,
because control would make the non-monomial rotation `rot` available. -/
theorem monomialSource_not_control (T : FiniteOperationalTheory (Fin 2)) (h : MonomialSource T) :
    ¬ HasCompositeUnitaryControl T := by
  intro hctrl
  exact rot_not_monomial (h 1 rot (hctrl 1 rot rot_isometry))

/-- **THE PERMUTATION-ONLY NO-GO, QM**: a monomial source is not finite operational QM. -/
theorem monomialSource_not_qm (T : FiniteOperationalTheory (Fin 2)) (h : MonomialSource T) :
    ¬ ExactAllFiniteEndomorphicQuantumOps T :=
  fun hqm => monomialSource_not_control T h (physical_of_exactAll T hqm).2.2.1

/-- **THE FLOW IS THE MISSING OPERATOR.** Bijective dynamics supplies the state exchanges and the
phase structure supplies the phases — both monomial — but the continuously driven transition,
whose nontrivial flow values are not monomial (`rot` as witness), is the operation neither
supplies. -/
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
