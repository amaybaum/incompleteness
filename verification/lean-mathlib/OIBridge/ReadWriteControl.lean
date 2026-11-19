/-
  OIBridge/ReadWriteControl.lean — restricted read/write operators and retained historical
  source implications (round 63; evidential scope corrected by KERNEL-VAC-1).

  THE PRIMITIVE. A ReadWriteFamily is a selectable local coupling: at each real parameter
  its map is a bijection of the finite state set, with a reference and local support.
  Through this specified interface its induced operator is a permutation and therefore
  monomial. The strict interpolation between identity and a pair swap is not monomial.
  These are statements about these operators and this interpolation. The definition does
  not assume continuity, so local constancy of an arbitrary parameterized family does not
  follow from it. The memory-swap example and its proofs are preserved unchanged.

  THE ORIGINAL SOURCE PREDICATE. ReadWriteSourced requires every matrix representative of
  an available conjugation to be an exact permutation. ReadWriteNonvacuity proves that this
  predicate is empty on Fin 2: native level-one readout and coarse-graining make identity
  available, while its representative Complex.I • 1 is not a permutation. The three
  readWriteSourced implications below retain their original statements and proof terms for
  historical and guard compatibility; their antecedent supplies no substantive Fin 2 evidence.

  THE SURVIVING CONDITIONAL. A theory whose available composite conjugations are all monomial
  has no composite unitary control on `Fin 2`, because control would make the non-monomial
  `rot` available. This is SubstratumInterface.monomialSource_not_control. Its existing
  monomialSource_not_qm corollary excludes ExactAllFiniteEndomorphicQuantumOps for that same
  theory under that same MonomialSource hypothesis. ReadWriteNonvacuity's sole witness is
  the existing permTheory (Fin 2), for every extension level and every representative.
  It is one mathematical theory, not a derivation of a native physical source or a universal
  impossibility theorem for read/write interaction.

  No generator or control law is added here; no control law is postulated. Neither the
  memory-swap example nor the chosen interpolation proves that a particular additional
  physical law is uniquely necessary. All existing declarations and proof terms remain.
-/

import OIBridge.SubstratumInterface

namespace OIBridge
namespace ReadWriteControl

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy PrimitiveSource InterventionLocality
open MicroReversibility LieRankSource SubstratumSource SubstratumInterface

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — the substratum primitive -/

section Primitive

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **A READ-WRITE FAMILY**: a selectable local coupling. For each external parameter value
`λ`, a bijection of the finite state set (the reversible substratum evolution, A2); `λ = 0` is
the reference interaction; the modification is local — every state outside the coupled pair
`{a, b}` is left fixed. -/
structure ReadWriteFamily (a b : S) where
  couple : ℝ → Equiv.Perm S
  reference : couple 0 = 1
  local_support : ∀ (l : ℝ) (x : S), x ≠ a → x ≠ b → couple l x = x

/-- The observable operator of a read-write intervention at parameter `λ`, through the round-62
interface: a permutation matrix, hence a bijective operator. -/
def readWriteOperator {a b : S} (F : ReadWriteFamily a b) (l : ℝ) : Matrix S S ℂ :=
  bijectiveOperator (F.couple l)

theorem readWriteOperator_eq_perm {a b : S} (F : ReadWriteFamily a b) (l : ℝ) :
    readWriteOperator F l = permMatrix (F.couple l) := rfl

/-- **THE READ-WRITE OPERATOR IS MONOMIAL**: bijective dynamics supplies only permutations. -/
theorem readWriteOperator_monomial {a b : S} (F : ReadWriteFamily a b) (l : ℝ) :
    IsMonomial (readWriteOperator F l) :=
  bijectiveOperator_monomial (F.couple l)

end Primitive

/-! ### Section B — the tangent test fails -/

section Tangent

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **NO CONTINUOUS OFF-DIAGONAL DIRECTION**: a strict interpolation between the reference
identity and the pair swap is not monomial, so no bijection realizes it. A permutation-valued
family cannot pass continuously through it, so its off-diagonal derivative is zero. -/
theorem offDiagonal_interp_not_monomial (a b : S) (hab : a ≠ b) (l : ℝ) (h0 : 0 < l)
    (h1 : l < 1) :
    ¬ IsMonomial (((1 - l : ℝ) : ℂ) • permMatrix (1 : Equiv.Perm S)
      + ((l : ℝ) : ℂ) • permMatrix (Equiv.swap a b)) := by
  set M : Matrix S S ℂ := ((1 - l : ℝ) : ℂ) • permMatrix (1 : Equiv.Perm S)
    + ((l : ℝ) : ℂ) • permMatrix (Equiv.swap a b) with hM
  have haa : M a a = ((1 - l : ℝ) : ℂ) := by
    rw [hM, Matrix.add_apply, Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul,
      show permMatrix (1 : Equiv.Perm S) a a = 1 by simp [permMatrix],
      show permMatrix (Equiv.swap a b) a a = 0 by
        rw [permMatrix]; simp [Equiv.swap_apply_left, Ne.symm hab]]
    ring
  have hab' : M a b = ((l : ℝ) : ℂ) := by
    rw [hM, Matrix.add_apply, Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul,
      show permMatrix (1 : Equiv.Perm S) a b = 0 by simp [permMatrix, Ne.symm hab],
      show permMatrix (Equiv.swap a b) a b = 1 by
        rw [permMatrix]; simp [Equiv.swap_apply_right]]
    ring
  rintro ⟨σ, d, h⟩
  have e_aa : M a a = if σ a = a then d a else 0 := by rw [h, monomial_entry]
  have e_ab : M a b = if σ b = a then d b else 0 := by rw [h, monomial_entry]
  have h1a : σ a = a := by
    by_contra hc
    rw [if_neg hc] at e_aa
    rw [haa] at e_aa
    exact (Complex.ofReal_ne_zero.mpr (by linarith)) e_aa
  have h1b : σ b = a := by
    by_contra hc
    rw [if_neg hc] at e_ab
    rw [hab'] at e_ab
    exact (Complex.ofReal_ne_zero.mpr (by linarith)) e_ab
  exact hab (σ.injective (h1a.trans h1b.symm))

end Tangent

/-! ### Section C — historical implications with an empty `Fin 2` source antecedent -/

section Outcome

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **ORIGINAL READ-WRITE SOURCE PREDICATE**, retained unchanged. It quantifies over exact
matrix representatives and is empty on `Fin 2`, as proved in `ReadWriteNonvacuity`. -/
def ReadWriteSourced (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → ∃ σ : Equiv.Perm (A × Fin n), V = permMatrix σ

theorem readWriteSourced_monomialSource (T : FiniteOperationalTheory A)
    (h : ReadWriteSourced T) : MonomialSource T := by
  intro n V hV
  obtain ⟨σ, rfl⟩ := h n V hV
  exact monomial_permMatrix σ

/-- Historical implication, retained unchanged; its original antecedent is empty on `Fin 2`. -/
theorem readWriteSourced_not_control (T : FiniteOperationalTheory (Fin 2))
    (h : ReadWriteSourced T) : ¬ HasCompositeUnitaryControl T :=
  monomialSource_not_control T (readWriteSourced_monomialSource T h)

/-- Historical QM implication, retained unchanged; not substantive evidence on `Fin 2`. -/
theorem readWriteSourced_not_qm (T : FiniteOperationalTheory (Fin 2))
    (h : ReadWriteSourced T) : ¬ ExactAllFiniteEndomorphicQuantumOps T :=
  monomialSource_not_qm T (readWriteSourced_monomialSource T h)

end Outcome

/-! ### Section D — the countercontrol: read-write interaction is not controllability -/

section Countercontrol

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **THE MEMORY-SWAP FAMILY**: a genuine nontrivial reversible read-write dynamics that
exchanges two states — bidirectional hidden memory — with the reference at `λ = 0`. -/
noncomputable def memorySwap (a b : S) : ReadWriteFamily a b where
  couple := fun l => if l = 0 then 1 else Equiv.swap a b
  reference := by simp
  local_support := by
    intro l x hxa hxb
    by_cases hl : l = 0
    · simp [hl]
    · simp only [hl, if_false]
      exact Equiv.swap_apply_of_ne_of_ne hxa hxb

/-- The memory-swap family is nontrivial: at a nonzero parameter it moves the two states. -/
theorem memorySwap_nontrivial (a b : S) (hab : a ≠ b) :
    (memorySwap a b).couple 1 ≠ 1 := by
  simp only [memorySwap, one_ne_zero, if_false]
  intro h
  have := Equiv.ext_iff.mp h a
  rw [Equiv.swap_apply_left, Equiv.Perm.one_apply] at this
  exact hab this.symm

/-- Its induced operators are monomial — bidirectional read-write supplies no off-diagonal
generator. -/
theorem memorySwap_operator_monomial (a b : S) (l : ℝ) :
    IsMonomial (readWriteOperator (memorySwap a b) l) :=
  readWriteOperator_monomial _ l

/-- **READ-WRITE INTERACTION IS NOT READ-WRITE CONTROLLABILITY**: a nontrivial reversible
read-write family exists whose every induced operator is monomial, so bidirectional memory
(C4/readback) does not by itself supply a tunable off-diagonal generator. -/
theorem readWriteControl_independent (a b : S) (hab : a ≠ b) :
    ∃ F : ReadWriteFamily a b, F.couple 1 ≠ 1 ∧ ∀ l : ℝ, IsMonomial (readWriteOperator F l) :=
  ⟨memorySwap a b, memorySwap_nontrivial a b hab, fun l => memorySwap_operator_monomial a b l⟩

end Countercontrol

#print axioms readWriteOperator_eq_perm
#print axioms readWriteOperator_monomial
#print axioms offDiagonal_interp_not_monomial
#print axioms readWriteSourced_monomialSource
#print axioms readWriteSourced_not_control
#print axioms readWriteSourced_not_qm
#print axioms memorySwap_nontrivial
#print axioms memorySwap_operator_monomial
#print axioms readWriteControl_independent

end ReadWriteControl
end OIBridge
