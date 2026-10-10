import OIBridge.PhaseSource

/-!
# Origin envelope — design module of the research thread `research/origin`

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It records two kernel facts the thread's no-go envelope uses.

* **Dephasing covariance of the monomial class.** Conjugation by a submonomial operator commutes
  with the complete dephasing in the configuration frame (`conj_dephase_of_submonomial`), so
  every branch of every family instrument-realized by the monomial substratum class
  (`instAvail_substratum_dephase`) or by the sourced class (`instAvail_permClass_dephase`)
  commutes with it. Such a family creates no coherence from a configuration-diagonal state and
  turns no coherence into populations.
* **A ones-fixing class carrying a non-monomial mixer.** The landed ones-fixing architecture
  `onesClass` makes the conjugation by the layer gate flow at time one half available
  (`onesClass_mixer_available`), and that operator is not monomial
  (`gateFlow_half_not_monomial`). So the ones-fixing invariant, which excludes the balanced
  mixer `hMat` and the quarter phase, does not exclude every non-monomial mixer
  (`onesFixing_class_carries_mixer`).
-/

namespace OIBridge
namespace OriginEnvelope

open scoped Matrix

variable {S : Type} [Fintype S] [DecidableEq S]

/-! ### Section A — dephasing covariance -/

section Dephasing

/-- Complete dephasing in the configuration frame. -/
def dephase (X : Matrix S S ℂ) : Matrix S S ℂ := Matrix.diagonal fun i => X i i

theorem dephase_apply (X : Matrix S S ℂ) (p q : S) :
    dephase X p q = if p = q then X p p else 0 := by
  simp [dephase, Matrix.diagonal_apply]

theorem dephase_sum {ι : Type*} (s : Finset ι) (f : ι → Matrix S S ℂ) :
    dephase (∑ i ∈ s, f i) = ∑ i ∈ s, dephase (f i) := by
  ext p q
  by_cases h : p = q <;> simp [dephase_apply, Matrix.sum_apply, h]

/-- **CONJUGATION BY A SUBMONOMIAL OPERATOR COMMUTES WITH THE COMPLETE DEPHASING**: a row of
the operator has at most one nonzero entry, so it reads no coherence; a column has at most one,
so it writes none. -/
theorem conj_dephase_of_submonomial {K : Matrix S S ℂ} (hK : StructuralClosure.IsSubmonomial K)
    (X : Matrix S S ℂ) : K * dephase X * Kᴴ = dephase (K * X * Kᴴ) := by
  have hrow : ∀ p j, (∑ i, K p i * X i j) * star (K p j) = K p j * X j j * star (K p j) := by
    intro p j
    by_cases hpj : K p j = 0
    · simp [hpj]
    · rw [Finset.sum_eq_single j]
      · intro i _ hij
        by_cases hpi : K p i = 0
        · rw [hpi, zero_mul]
        · exact absurd (hK.1 p i j hpi hpj) hij
      · intro hj
        exact absurd (Finset.mem_univ j) hj
  ext p q
  rw [Matrix.mul_apply, dephase_apply]
  simp only [dephase, Matrix.mul_diagonal, Matrix.conjTranspose_apply]
  by_cases hpq : p = q
  · subst hpq
    rw [if_pos rfl, Matrix.mul_apply]
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply]
    exact Finset.sum_congr rfl fun j _ => (hrow _ j).symm
  · rw [if_neg hpq]
    refine Finset.sum_eq_zero fun j _ => ?_
    by_cases hp : K p j = 0
    · simp [hp]
    · by_cases hq : K q j = 0
      · simp [hq]
      · exact absurd (hK.2 p q j hp hq) hpq

/-- **EVERY FAMILY OF THE MONOMIAL SUBSTRATUM CLASS COMMUTES WITH THE DEPHASING**, branch by
branch, at every carrier: each branch is a sum of conjugations by monomial operators
(`realized_of_instAvail`). -/
theorem instAvail_substratum_dephase {T : Type} [Fintype T] [DecidableEq T] {O : Type}
    [Fintype O] [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (h : InterventionLocality.InstAvail StructuralClosure.substratumClass T O F) (a : O)
    (X : Matrix T T ℂ) : F a (dephase X) = dephase (F a X) := by
  obtain ⟨ι, _, K, hF, hK⟩ :=
    InterventionLocality.realized_of_instAvail StructuralClosure.substratumClass_arch h a
  rw [hF, LinearMap.sum_apply, LinearMap.sum_apply, dephase_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [AncillaClosure.conjChannel_apply, AncillaClosure.conjChannel_apply]
  exact conj_dephase_of_submonomial (StructuralClosure.monomial_submonomial (hK i)) X

/-- **THE SAME FOR THE SOURCED CLASS** of contractively scaled partial permutations. -/
theorem instAvail_permClass_dephase {T : Type} [Fintype T] [DecidableEq T] {O : Type}
    [Fintype O] [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (h : InterventionLocality.InstAvail SubstratumInterfaceAudit.permClass T O F) (a : O)
    (X : Matrix T T ℂ) : F a (dephase X) = dephase (F a X) := by
  obtain ⟨ι, _, K, hF, hK⟩ :=
    InterventionLocality.realized_of_instAvail SubstratumInterfaceAudit.permClass_arch h a
  rw [hF, LinearMap.sum_apply, LinearMap.sum_apply, dephase_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [AncillaClosure.conjChannel_apply, AncillaClosure.conjChannel_apply]
  exact conj_dephase_of_submonomial
    (show SubstratumInterfaceAudit.IsScaledPartialPerm (K i) from hK i).1 X

end Dephasing

/-! ### Section B — a ones-fixing class carrying a non-monomial mixer -/

section Mixer

theorem one_add_I_ne_zero : (1 + Complex.I) ≠ 0 := by
  intro h
  have h' := congrArg Complex.re h
  simp at h'

theorem one_sub_I_ne_zero : (1 - Complex.I) ≠ 0 := by
  intro h
  have h' := congrArg Complex.re h
  simp at h'

/-- **THE LAYER GATE FLOW AT TIME ONE HALF IS NOT MONOMIAL** as soon as the involution moves a
configuration: the moved column has two nonzero entries, `(1 + i)/2` and `(1 − i)/2`. -/
theorem gateFlow_half_not_monomial {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) :
    ¬ SubstratumInterface.IsMonomial (LiftAudit.gateFlow σ (1 / 2 : ℝ)) := by
  intro hm
  have hs := StructuralClosure.monomial_submonomial hm
  obtain ⟨h1, h2⟩ := LiftAudit.gateFlow_half_entries ha
  have hne1 : LiftAudit.gateFlow σ (1 / 2 : ℝ) a a ≠ 0 := by
    rw [h1]
    exact div_ne_zero one_add_I_ne_zero two_ne_zero
  have hne2 : LiftAudit.gateFlow σ (1 / 2 : ℝ) (σ a) a ≠ 0 := by
    rw [h2]
    exact div_ne_zero one_sub_I_ne_zero two_ne_zero
  exact ha (hs.2 _ _ _ hne2 hne1)

theorem swap01_invol (x : Fin 2) : (Equiv.swap (0 : Fin 2) 1) ((Equiv.swap (0 : Fin 2) 1) x) = x :=
  Equiv.swap_apply_self _ _ x

/-- The layer involution of the site exchange, read at level one, moves the configuration
`(0, 0)`. -/
theorem levelSwap_moves :
    LiftAudit.levelPerm (Equiv.swap (0 : Fin 2) 1) 1 ((0 : Fin 2), (0 : Fin 1)) ≠ ((0 : Fin 2), (0 : Fin 1)) := by
  decide

/-- **THE ONES-FIXING CLASS MAKES THE MIXER AVAILABLE**: the conjugation by the layer gate flow
of the site exchange at time one half, at level one. -/
theorem onesClass_mixer_available :
    (InterventionLocality.genTheory InstrumentRealization.onesClass
        InstrumentRealization.onesClass_arch (Fin 2)).availExt 1 Unit
      (fun _ => MonoidalCompletion.conjChannel
        (LiftAudit.gateFlow (LiftAudit.levelPerm (Equiv.swap (0 : Fin 2) 1) 1) (1 / 2 : ℝ))) :=
  SubstratumSource.genTheory_avail_conj InstrumentRealization.onesClass_arch
    (InstrumentRealization.onesClass_gateFlow (LiftAudit.levelPerm_involutive swap01_invol 1) _)
    (LiftAudit.gateFlow_unitary (LiftAudit.levelPerm_involutive swap01_invol 1) _)

/-- **A ONES-FIXING ARCHITECTURE CARRYING A NON-MONOMIAL MIXER**: `onesClass` is ones-fixing, the
conjugation by the gate flow at time one half is available in its generated theory, and that
operator is not monomial. -/
theorem onesFixing_class_carries_mixer :
    InstrumentRealization.OnesFixing InstrumentRealization.onesClass
      ∧ (InterventionLocality.genTheory InstrumentRealization.onesClass
          InstrumentRealization.onesClass_arch (Fin 2)).availExt 1 Unit
        (fun _ => MonoidalCompletion.conjChannel
          (LiftAudit.gateFlow (LiftAudit.levelPerm (Equiv.swap (0 : Fin 2) 1) 1) (1 / 2 : ℝ)))
      ∧ ¬ SubstratumInterface.IsMonomial
          (LiftAudit.gateFlow (LiftAudit.levelPerm (Equiv.swap (0 : Fin 2) 1) 1) (1 / 2 : ℝ)) :=
  ⟨InstrumentRealization.isometry_fixes_ones, onesClass_mixer_available,
    gateFlow_half_not_monomial levelSwap_moves⟩

end Mixer

#print axioms dephase_apply
#print axioms dephase_sum
#print axioms conj_dephase_of_submonomial
#print axioms instAvail_substratum_dephase
#print axioms instAvail_permClass_dephase
#print axioms one_add_I_ne_zero
#print axioms one_sub_I_ne_zero
#print axioms gateFlow_half_not_monomial
#print axioms swap01_invol
#print axioms levelSwap_moves
#print axioms onesClass_mixer_available
#print axioms onesFixing_class_carries_mixer

end OriginEnvelope
end OIBridge
