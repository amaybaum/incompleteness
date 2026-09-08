import OIBridge.CausalReadback
import OIBridge.Equivalence

/-!
# Finite-visible intrinsic rooted-family classification

Arc B, task #64.  This module begins with the neutral T1 infrastructure fixed by the frozen
`OI-ROOTED-CLASSIFICATION-AUDIT.md`: the visible predicate `PPer` and the necessity direction for
the inherited `CausalReadback.RootedRealization` interface on a finite visible carrier.

The sufficiency construction is intentionally not encoded in these first lemmas.  In particular,
`PPer` is a visible predicate, not a renamed hidden-realizability predicate.
-/

namespace OIBridge
namespace RootedClassification

open Finset Matrix CausalReadback Equivalence

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- **FINITE VISIBLE TEMPORAL PERIODICITY.** -/
def PeriodicFamily (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ M : ℕ, 0 < M ∧ ∀ t : ℕ, Γ (t + M) = Γ t

/-- **THE FIRST FALSIFIABLE VISIBLE CLASS `P_per`.** Root identity, row stochasticity at every
 time, and a positive finite visible period. -/
def PPer (Γ : ℕ → Matrix V V ℝ) : Prop :=
  Γ 0 = 1 ∧ (∀ t : ℕ, IsRowStochastic (Γ t)) ∧ PeriodicFamily Γ

/-- **ROOT TIME IS THE IDENTITY.** This uses only the common hidden prior normalization and the
 canonical visible projection. -/
theorem rootedMap_zero {H : Type*} [Fintype H] (R : RootedRealization V H) :
    rootedMap R 0 = (1 : Matrix V V ℝ) := by
  classical
  ext a j
  by_cases h : a = j
  · subst j
    simp [rootedMap, R.prior_sum]
  · simp [rootedMap, Matrix.one_apply, h]

/-- **FINITE REVERSIBILITY FORCES A FINITE VISIBLE PERIOD.** The witness used here is the cardinality
 of the finite permutation group on the microscopic carrier.  It is intentionally coarse and is
 not asserted to be the minimal visible period or the microscopic order. -/
theorem rootedMap_periodic {H : Type*} [Fintype H] (R : RootedRealization V H) :
    PeriodicFamily (fun t => rootedMap R t) := by
  classical
  let M : ℕ := Fintype.card (Equiv.Perm (V × H))
  have hM : 0 < M := by
    dsimp [M]
    exact Fintype.card_pos
  have hpow : R.step ^ M = 1 := by
    dsimp [M]
    exact pow_card_eq_one
  refine ⟨M, hM, ?_⟩
  intro t
  ext a j
  simp only [rootedMap]
  apply Finset.sum_congr rfl
  intro h _
  congr 1
  rw [R.step.iterate_eq_pow, R.step.iterate_eq_pow, pow_add, hpow, mul_one]

/-- **T1 NECESSITY, AT THE MERGED ROOTED INTERFACE.** Every inherited realization on a finite visible
 carrier lies in the visible class `PPer`.  The three conjuncts expose their dependencies: root
 identity from the normalized common prior and canonical projection, row stochasticity from the
 existing rooted-map theorem, and periodicity from finiteness plus reversibility. -/
theorem rootedMap_mem_PPer {H : Type*} [Fintype H] (R : RootedRealization V H) :
    PPer (fun t => rootedMap R t) :=
  ⟨rootedMap_zero R, fun t => rootedMap_isRowStochastic R t, rootedMap_periodic R⟩

end RootedClassification
end OIBridge

#print axioms OIBridge.RootedClassification.rootedMap_zero
#print axioms OIBridge.RootedClassification.rootedMap_periodic
#print axioms OIBridge.RootedClassification.rootedMap_mem_PPer
