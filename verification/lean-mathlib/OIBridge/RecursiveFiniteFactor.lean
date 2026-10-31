import Mathlib.Logic.Basic

/-!
# SUBSTATE-2: finite-depth aggregation and exact visible-period scope

RESEARCH-ONLY: this module proves *conditional* finite-stage statements
without claiming that physical OI has fractal states.

For a hierarchy of increasingly informative finite-stage projections,
each of the L observation functions can factor through a (possibly
different) stage. A common refinement of these finitely many stages
then determines all L observations. If the *observation functions*
repeat with a common exact period L>0, the same common refinement
determines observations at every natural time.

The crucial topological lemma "any continuous finite-valued map out
of a compact profinite inverse limit factors through a finite stage"
is NOT formalized here and is NOT inserted as an axiom. No inference
from Poincare recurrence to a common period, or from a.e. equality
to a pointwise period, is made.

A second result certifies the two-step reversibility of a visible
Boolean flip controlled by a static hidden predicate. Neither
result yields physical quantum operations, a gauge field or Yang-Mills.
-/

namespace OIBridge.RecursiveFiniteFactor

universe u v w
variable {X : Type u} {C : Type v} {V : Type w}

/-- A function has the same output on states indistinguishable
    at hierarchy depth n. -/
def FactorsAt (prefix : ℕ → X → C) (n : ℕ) (f : X → V) : Prop :=
  ∀ x y, prefix n x = prefix n y → f x = f y

/-- Higher stages are at least as informative as lower stages. -/
def Refines (prefix : ℕ → X → C) : Prop :=
  ∀ n m, n ≤ m → ∀ x y, prefix m x = prefix m y → prefix n x = prefix n y

/-- A factor at depth n is also determined at any deeper stage m. -/
theorem factorsAt_mono (prefix : ℕ → X → C) (f : X → V)
    (href : Refines prefix) {n m : ℕ} (hnm : n ≤ m)
    (hfac : FactorsAt prefix n f) : FactorsAt prefix m f := by
  intro x y hxy
  exact hfac x y (href n m hnm x y hxy)

/-- Finite-time *aggregation*: at every individual time below L,
a possibly different finite stage is enough; one common finite
stage is enough for the whole finite family. The hypothesis that
these finite stages exist is EXPLICIT rather than smuggled in. -/
theorem finite_horizon_depth_bound (prefix : ℕ → X → C)
    (record : ℕ → X → V) (href : Refines prefix) :
    ∀ L : ℕ,
      (∀ t : ℕ, t < L → ∃ n : ℕ, FactorsAt prefix n (record t)) →
      ∃ N : ℕ, ∀ t : ℕ, t < L → FactorsAt prefix N (record t) := by
  intro L
  induction L with
  | zero =>
      intro h
      refine ⟨0, ?_⟩
      intro t ht
      omega
  | succ L ih =>
      intro h
      have hsmall : ∀ t : ℕ, t < L → ∃ n : ℕ, FactorsAt prefix n (record t) := by
        intro t ht
        exact h t (by omega)
      obtain ⟨N, hN⟩ := ih hsmall
      obtain ⟨n, hn⟩ := h L (by omega)
      refine ⟨max N n, ?_⟩
      intro t ht
      by_cases hlt : t < L
      · exact factorsAt_mono prefix (record t) href (Nat.le_max_left N n) (hN t hlt)
      · have heq : t = L := by omega
        subst t
        exact factorsAt_mono prefix (record L) href (Nat.le_max_right N n) hn

/-- Full-time bound if all visible time-indexed observation maps
repeat with one specified period. This is strictly stronger than
Poincare recurrence, and its proof does not assert that OI
satisfies the hypotheses. -/
theorem all_time_depth_bound_of_exact_period (prefix : ℕ → X → C)
    (record : ℕ → X → V) (href : Refines prefix)
    (L : ℕ) (hL : 0 < L)
    (hperiod : ∀ t : ℕ, record t = record (t % L))
    (hlocal : ∀ t : ℕ, t < L → ∃ n : ℕ, FactorsAt prefix n (record t)) :
    ∃ N : ℕ, ∀ t : ℕ, FactorsAt prefix N (record t) := by
  obtain ⟨N, hN⟩ := finite_horizon_depth_bound prefix record href L hlocal
  refine ⟨N, ?_⟩
  intro t
  rw [hperiod t]
  exact hN (t % L) (Nat.mod_lt t hL)

/-- One fixed hidden predicate controls a reversible two-step
visible flip, even when H itself is an infinite type. -/
def feedbackStep {H : Type*} (h : H → Bool) (p : Bool × H) : Bool × H :=
  (Bool.xor p.1 (h p.2), p.2)

theorem feedbackStep_involution {H : Type*} (h : H → Bool) (p : Bool × H) :
    feedbackStep h (feedbackStep h p) = p := by
  rcases p with ⟨b, hidden⟩
  cases b <;> cases h hidden <;> rfl

#print axioms factorsAt_mono
#print axioms finite_horizon_depth_bound
#print axioms all_time_depth_bound_of_exact_period
#print axioms feedbackStep_involution

end OIBridge.RecursiveFiniteFactor
