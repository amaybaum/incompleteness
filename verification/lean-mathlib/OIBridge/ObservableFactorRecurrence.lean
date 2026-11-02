import OIBridge.RecurrenceHorizon
import OIBridge.EquivalenceChain

/-!
# SUBSTATE-1: finite visible factor, arbitrary hidden carrier

This research module isolates two logically separate, carrier-independent steps:

* The set of microscopic states whose visible label changes is exactly the
  union of the off-diagonal visible cell intersections. This identity does
  **not** assume that the carrier has finitely many states.
* A family of finite row-stochastic rooted matrices with a common exact
  visible identity return is P-indivisible on that horizon whenever an
  earlier rooted matrix is not a permutation. This reuses the existing
  kernel theorem about stochastic inverses.

The separate `ObservableMeasureReturn` module now kernel-proves the
positive-finite-cell **ENNReal** measured-return iff zero-change-mass
identity. THIS module proves only the set identity and the conditional
stochastic-matrix obstruction. Neither module supplies a measurable,
real row-stochastic rooted law or composes the measure-based identity
with the P-indivisibility result.

In particular, nothing here derives the five finite-QM operational
completion conditions or chooses a continuous gauge action.
-/

namespace OIBridge
namespace ObservableFactorRecurrence

open Matrix CausalReadback

universe u v

variable {X : Type u} {V : Type v}

/-- Hidden states whose observable label changes after one supplied iterate. -/
def ChangeEvent (obs : X → V) (advance : X → X) : Set X :=
  {x | obs (advance x) ≠ obs x}

/-- Hidden states in visible cell a that evolve into visible cell b. -/
def OffDiagonalEvent (obs : X → V) (advance : X → X)
    (a b : V) : Set X :=
  {x | obs x = a ∧ obs (advance x) = b}

/-- A visible change is precisely the union of off-diagonal cell events.
No finite hidden-carrier assumption (or measure) enters this identity. -/
theorem changeEvent_eq_iUnion (obs : X → V) (advance : X → X) :
    ChangeEvent obs advance =
      ⋃ a : V, ⋃ b : V, ⋃ (_ : a ≠ b), OffDiagonalEvent obs advance a b := by
  ext x
  simp only [ChangeEvent, OffDiagonalEvent, Set.mem_ofPred_eq, Set.mem_iUnion]
  constructor
  · intro h
    exact ⟨obs x, obs (advance x), Ne.symm h, rfl, rfl⟩
  · rintro ⟨a, b, hab, ha, hb⟩
    intro heq
    exact hab (ha.symm.trans (heq.symm.trans hb))

section RootedMatrix

variable [Fintype V] [DecidableEq V]

/-- Carrier-independent stochastic-inverse obstruction: an exact rooted
identity return plus an earlier non-permutation rooted map implies
P-indivisibility at that horizon. The measurable realization that gives
rise to Gamma is NOT constructed by this theorem. -/
theorem pIndivisible_of_visible_identity_return_nonperm
    (Γ : ℕ → Matrix V V ℝ) {L s : ℕ}
    (hs : s < L) (hsto : IsRowStochastic (Γ s))
    (hreturn : Γ L = 1)
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, Γ s = σ.permMatrix ℝ) :
    PIndivisibleWithin L Γ := by
  intro hdiv
  obtain ⟨Λ, hΛ, hfactor⟩ := hdiv s L hs le_rfl
  have hA : Γ s ∈ Matrix.rowStochastic ℝ V :=
    Matrix.mem_rowStochastic_iff_sum.mpr hsto
  have hB : Λ ∈ Matrix.rowStochastic ℝ V :=
    Matrix.mem_rowStochastic_iff_sum.mpr hΛ
  have hprod : Γ s * Λ = 1 :=
    hfactor.symm.trans hreturn
  exact hnonperm
    (EquivalenceChain.isPermMatrix_of_stochastic_inverse
      hA hB (Or.inl hprod))

end RootedMatrix

#print axioms changeEvent_eq_iUnion
#print axioms pIndivisible_of_visible_identity_return_nonperm

end ObservableFactorRecurrence
end OIBridge
