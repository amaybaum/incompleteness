import OIBridge.ObservableFactorRecurrence
import Mathlib.MeasureTheory.Measure.MeasureSpace
import Mathlib.Data.ENNReal.Inv

/-!
# SUBSTATE-1: measurable visible return (research candidate)

For an arbitrary *measurable* hidden carrier, measure on it, and a finite
observable alphabet, the mass of the visible-change event is zero iff every
off-diagonal joint-observation cell has zero mass.

With all visible initial cells of positive finite measure, the actual
conditional rooted transition matrix, defined from joint cell measures,
equals the identity iff the visible label returns almost everywhere.
No assumption of finite hidden cardinality or of microscopic periodicity
is used. The measure is a parameter; T-invariance is needed for other
physical questions, not this equivalence itself.

Status: candidate submitted for Lean/Mathlib CI. No Lean proof of the
all-L Fourier wave statement, no quantum operational completion claim.
-/

namespace OIBridge
namespace ObservableMeasureReturn

open MeasureTheory
open ObservableFactorRecurrence

universe u v

variable {X : Type u} {V : Type v}
variable [MeasurableSpace X] [Fintype V] [DecidableEq V]

/-- The observable state cell at a fixed observation value. -/
def VisibleCell (obs : X → V) (a : V) : Set X := {x | obs x = a}

/-- The diagonal joint event is the visible cell minus visible changes. -/
theorem diagonalEvent_eq_diff (obs : X → V) (advance : X → X) (a : V) :
    OffDiagonalEvent obs advance a a =
      VisibleCell obs a \\ ChangeEvent obs advance := by
  ext x
  change (obs x = a ∧ obs (advance x) = a) ↔
    (obs x = a ∧ ¬ obs (advance x) ≠ obs x)
  constructor
  · rintro ⟨ha, hb⟩
    refine ⟨ha, ?_⟩
    intro hne
    exact hne (hb.trans ha.symm)
  · rintro ⟨ha, hnot⟩
    refine ⟨ha, ?_⟩
    by_contra hne
    apply hnot
    intro h
    exact hne (h.trans ha)

/-- A visible return holds almost everywhere exactly when every
off-diagonal joint cell has zero measure. This applies to any hidden
type and does not require an invariant prior. -/
theorem measure_change_zero_iff (μ : Measure X) (obs : X → V)
    (advance : X → X) :
    μ (ChangeEvent obs advance) = 0 ↔
      ∀ a b : V, a ≠ b → μ (OffDiagonalEvent obs advance a b) = 0 := by
  rw [changeEvent_eq_iUnion]
  simp only [measure_iUnion_null_iff]

/-- Rooted transition built from actual conditional joint cell measures.
A positive finite measure is required for each initial visible cell in
the identity-return theorem. -/
noncomputable def measuredGamma (μ : Measure X) (obs : X → V)
    (advance : X → X) : Matrix V V ENNReal :=
  fun a b => μ (OffDiagonalEvent obs advance a b) / μ (VisibleCell obs a)

/-- Exact return of the *measured* conditional rooted matrix is equivalent
to almost-sure equality of visible observations after the supplied iterate.

Here `advance` can be `T^[L]`. This lemma only needs one iterate;
invertibility or measure preservation is not used. -/
theorem measuredGamma_eq_one_iff (μ : Measure X) (obs : X → V)
    (advance : X → X)
    (hpos : ∀ a : V, μ (VisibleCell obs a) ≠ 0)
    (hfin : ∀ a : V, μ (VisibleCell obs a) ≠ ⊤) :
    measuredGamma μ obs advance = 1 ↔
      μ (ChangeEvent obs advance) = 0 := by
  constructor
  · intro hGamma
    apply (measure_change_zero_iff μ obs advance).2
    intro a b hab
    have hentry : μ (OffDiagonalEvent obs advance a b) /
        μ (VisibleCell obs a) = 0 := by
      have h := congrFun (congrFun hGamma a) b
      simpa [measuredGamma, Matrix.one_apply, hab] using h
    exact (ENNReal.div_eq_zero_iff.mp hentry).resolve_right (hfin a)
  · intro hchange
    ext a b
    by_cases hab : a = b
    · subst b
      have hdiag : μ (OffDiagonalEvent obs advance a a) =
          μ (VisibleCell obs a) := by
        rw [diagonalEvent_eq_diff, measure_sdiff_null hchange]
      simp only [measuredGamma, Matrix.one_apply, if_pos rfl]
      rw [hdiag]
      exact ENNReal.div_self (hpos a) (hfin a)
    · have hzero := (measure_change_zero_iff μ obs advance).1 hchange a b hab
      simp [measuredGamma, Matrix.one_apply, hab, hzero]

#print axioms measure_change_zero_iff
#print axioms measuredGamma_eq_one_iff

end ObservableMeasureReturn
end OIBridge
