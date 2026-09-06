import OIBridge.FlowEndpoint

/-!
# The phase-source audit — does the stated substratum and observer access derive the phases?

The preregistered pass of `PHASE-SOURCE-AUDIT.md`. The kernel content is four groups of theorems;
the census of the manuscripts is in the note.

* T1, the invariant, general: for every architecture whose admissible isometries fix the all-ones
  ray, the generated theory has no quarter phase at any level with two or more states
  (`onesFixing_not_phasesAvailable`).
* T2, the stated access is ones-fixing: the sourced class is ones-fixing
  (`permClass_onesFixing`), so its theory has no quarter phase by the same invariant that decides
  the flow endpoint (`permTheory_not_phasesAvailable_onesFixing`); the bijective interventions,
  the read-write operators and the layer gate flows all fix the all-ones vector
  (`bijectiveOperator_mulVec_ones`, `readWriteOperator_mulVec_ones`, `gateFlow_mulVec_ones`).
* T3, the distinctions: the quarter phase is not a scalar and its conjugation is not the identity
  (`phaseGate_not_scalar`, `conjChannel_phaseGate_ne_id`); every diagonal unitary fixes it under
  conjugation, so a rephasing of the representation neither creates nor removes it
  (`diagonal_conj_phaseGate`); a unit scalar acts trivially on every conjugation channel
  (`ReachabilitySeam.conjChannel_smul`).
* T4, the stipulation, isolated: the quarter phase moves the all-ones ray
  (`phaseGate_moves_ones`), so the monomial class of the round-62 interface, which contains it as
  a phase intervention, is not ones-fixing (`substratumClass_not_onesFixing`): it is the one
  intervention kind of the interface that is not.

Not claimed: anything about the lift audit's Q3 from `DerivedOI`; that relative phase is the
unique or minimal resource on the route; that an operator moving the all-ones ray suffices to
source `PhasesAvailable`, the condition being necessary and the sufficient access tested the
quarter-phase intervention itself; anything about a richer substratum ontology than the one the
manuscripts state.
-/

namespace OIBridge
namespace PhaseSource

open Complex Matrix OperationalAssembly MonoidalCompletion SpectatorBridge InterventionLocality
open MicroReversibility LieRankSource SubstratumInterface StructuralClosure
open SubstratumInterfaceAudit RouteB LiftAudit MinimalRepertoire ReadWriteControl LevelOneSeam
open PhysicalCharacterization InstrumentRealization FlowEndpoint

open scoped ComplexOrder

/-! ### Section A — T1: the invariant, general -/

section Invariant

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **T1 — NO ONES-FIXING ARCHITECTURE SOURCES A QUARTER PHASE**: every available unitary
conjugation of its theory fixes the all-ones ray, and the quarter phase moves it. -/
theorem onesFixing_not_phasesAvailable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hf : OnesFixing 𝓘) (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable (genTheory 𝓘 arch A) := by
  intro hp
  obtain ⟨a₀, b₀, hab⟩ := Fintype.exists_pair_of_one_lt_card (by omega : 1 < Fintype.card A)
  set a : A × Fin 1 := (a₀, 0) with ha
  set b : A × Fin 1 := (b₀, 0) with hb
  have hne : a ≠ b := fun h => hab (Prod.mk.inj h).1
  obtain ⟨z, hz⟩ := instAvail_unitary_fixes_ones hf (phaseGate_unitary a) (hp 1 a)
  have h1 := congrFun hz a
  have h2' := congrFun hz b
  rw [phaseGate_mulVec_ones, Pi.smul_apply, ones_apply, smul_eq_mul, mul_one] at h1 h2'
  simp only [if_true] at h1
  rw [if_neg hne] at h2'
  have := congrArg Complex.im (h1.trans h2'.symm)
  simp at this

end Invariant

/-! ### Section B — T2: the stated access is ones-fixing -/

section Access

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T2 — THE SOURCED CLASS IS ONES-FIXING**: an isometry among the scaled partial permutations
has one nonzero entry, the common scalar, in every row, so it carries the all-ones vector to that
scalar times itself. -/
theorem permClass_onesFixing : OnesFixing permClass := by
  intro S _ _ K hK hiso
  obtain ⟨hsub, c₀, -, hall⟩ := hK
  refine ⟨c₀, ?_⟩
  have hKK : K * Kᴴ = 1 := mul_eq_one_comm.mp hiso
  funext i
  have hrow := congrFun (congrFun hKK i) i
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at hrow
  have hex : ∃ j, K i j ≠ 0 := by
    by_contra hno
    have hall0 : ∀ j, K i j = 0 := fun j => by
      by_contra h
      exact hno ⟨j, h⟩
    simp [hall0] at hrow
  obtain ⟨j₀, hj₀⟩ := hex
  have hzero : ∀ j, j ≠ j₀ → K i j = 0 := fun j hj => by
    by_contra h
    exact hj (hsub.1 i j j₀ h hj₀)
  rw [Pi.smul_apply, ones_apply, smul_eq_mul, mul_one]
  simp only [Matrix.mulVec, dotProduct, ones_apply, mul_one]
  rw [Finset.sum_eq_single j₀ (fun j _ hj => hzero j hj) (fun h => absurd (Finset.mem_univ _) h)]
  exact hall i j₀ hj₀

/-- **T2 — THE SOURCED THEORY HAS NO QUARTER PHASE**, by the ones-fixing invariant: the same
mechanism that decides the flow endpoint. -/
theorem permTheory_not_phasesAvailable_onesFixing {A : Type} [Fintype A] [DecidableEq A]
    (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable (permTheory A) :=
  onesFixing_not_phasesAvailable permClass_arch permClass_onesFixing h2

/-- A bijective intervention fixes the all-ones vector. -/
theorem bijectiveOperator_mulVec_ones (σ : Equiv.Perm S) :
    bijectiveOperator σ *ᵥ ones S = ones S :=
  permMatrix_mulVec_ones σ

/-- A read-write operator fixes the all-ones vector. -/
theorem readWriteOperator_mulVec_ones {a b : S} (F : ReadWriteFamily a b) (l : ℝ) :
    readWriteOperator F l *ᵥ ones S = ones S := by
  rw [readWriteOperator_eq_perm]
  exact permMatrix_mulVec_ones _

end Access

/-! ### Section C — T3: the distinctions -/

section Distinctions

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **(D3) THE QUARTER PHASE IS NOT A SCALAR** on a carrier with two or more states. -/
theorem phaseGate_not_scalar (h2 : 2 ≤ Fintype.card S) (a : S) (c : ℂ) :
    phaseGate a ≠ c • (1 : Matrix S S ℂ) := by
  intro h
  have : Nontrivial S := Fintype.one_lt_card_iff_nontrivial.mp (by omega)
  obtain ⟨b, hb⟩ := exists_ne a
  have h1 := congrFun (congrFun h a) a
  have h2' := congrFun (congrFun h b) b
  simp only [phaseGate, Matrix.diagonal_apply_eq, Matrix.smul_apply, Matrix.one_apply_eq,
    smul_eq_mul, mul_one, if_true] at h1 h2'
  rw [if_neg (Ne.symm hb)] at h2'
  have := congrArg Complex.im (h1.trans h2'.symm)
  simp at this

/-- **(D3) THE CONJUGATION BY THE QUARTER PHASE IS NOT THE IDENTITY**: it multiplies the
coherence from `a` to any other state by `i`. -/
theorem conjChannel_phaseGate_ne_id (h2 : 2 ≤ Fintype.card S) (a : S) :
    conjChannel (phaseGate a) ≠ LinearMap.id := by
  intro h
  have : Nontrivial S := Fintype.one_lt_card_iff_nontrivial.mp (by omega)
  obtain ⟨b, hb⟩ := exists_ne a
  have hX : (phaseGate a * Matrix.single a b (1 : ℂ) * (phaseGate a)ᴴ) a b
      = (Matrix.single a b (1 : ℂ)) a b := by
    have h' := congrArg (fun Φ => Φ (Matrix.single a b (1 : ℂ))) h
    exact congrFun (congrFun h' a) b
  rw [phaseGate_conjTranspose, Matrix.mul_diagonal, phaseGate, Matrix.diagonal_mul,
    Matrix.single_apply_same, if_pos rfl, if_neg (Ne.symm hb)] at hX
  have := congrArg Complex.im hX
  simp at this

/-- **(D2) EVERY DIAGONAL UNITARY FIXES THE QUARTER PHASE UNDER CONJUGATION**: a rephasing of
the representation neither creates nor removes it. -/
theorem diagonal_conj_phaseGate (d : S → ℂ) (hd : ∀ i, star (d i) * d i = 1) (a : S) :
    Matrix.diagonal d * phaseGate a * (Matrix.diagonal d)ᴴ = phaseGate a := by
  rw [phaseGate, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal,
    Matrix.diagonal_mul_diagonal]
  congr 1
  funext i
  simp only [Pi.star_apply]
  have := hd i
  calc d i * (if a = i then Complex.I else 1) * star (d i)
      = (if a = i then Complex.I else 1) * (star (d i) * d i) := by ring
    _ = (if a = i then Complex.I else 1) := by rw [this, mul_one]

end Distinctions

/-! ### Section D — T4: the stipulation, isolated -/

section Stipulation

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T4 — THE QUARTER PHASE MOVES THE ALL-ONES RAY** on a carrier with two or more states. -/
theorem phaseGate_moves_ones (h2 : 2 ≤ Fintype.card S) (a : S) (z : ℂ) :
    phaseGate a *ᵥ ones S ≠ z • ones S := by
  intro hz
  have : Nontrivial S := Fintype.one_lt_card_iff_nontrivial.mp (by omega)
  obtain ⟨b, hb⟩ := exists_ne a
  have h1 := congrFun hz a
  have h2' := congrFun hz b
  rw [phaseGate_mulVec_ones, Pi.smul_apply, ones_apply, smul_eq_mul, mul_one] at h1 h2'
  simp only [if_true] at h1
  rw [if_neg (Ne.symm hb)] at h2'
  have := congrArg Complex.im (h1.trans h2'.symm)
  simp at this

/-- **T4 — THE MONOMIAL CLASS IS NOT ONES-FIXING**: the phase intervention of the round-62
interface is admissible in it, unitary, and moves the all-ones ray. It is the one intervention
kind of the interface that is not ones-fixing, and the one `PhasesAvailable` rests on. -/
theorem substratumClass_not_onesFixing : ¬ OnesFixing substratumClass := by
  intro hf
  obtain ⟨z, hz⟩ := hf (Fin 2) (phaseGate 0) (phase_monomial 0) (phaseGate_unitary 0)
  exact phaseGate_moves_ones (by simp) 0 z hz

end Stipulation

#print axioms onesFixing_not_phasesAvailable
#print axioms permClass_onesFixing
#print axioms permTheory_not_phasesAvailable_onesFixing
#print axioms bijectiveOperator_mulVec_ones
#print axioms readWriteOperator_mulVec_ones
#print axioms phaseGate_not_scalar
#print axioms conjChannel_phaseGate_ne_id
#print axioms diagonal_conj_phaseGate
#print axioms phaseGate_moves_ones
#print axioms substratumClass_not_onesFixing

end PhaseSource
end OIBridge
