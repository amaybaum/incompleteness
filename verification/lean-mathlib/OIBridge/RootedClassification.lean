import OIBridge.CausalReadback
import OIBridge.Equivalence

/-!
# Finite-visible intrinsic rooted-family classification

Arc B, task #64.  The visible predicate `PPer`, the inherited-interface necessity direction, and
the common-response-table probability lemma used by the T2 sufficiency construction.

`PPer` is a visible predicate, not a renamed hidden-realizability predicate.  The response-table
lemmas below are finite probability identities: they put any finite collection of categorical
marginals on one common finite seed without assuming rational probabilities.
-/

namespace OIBridge
namespace RootedClassification

open Finset Matrix CausalReadback Equivalence

universe u v

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- **FINITE VISIBLE TEMPORAL PERIODICITY.** -/
def PeriodicFamily (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ M : ℕ, 0 < M ∧ ∀ t : ℕ, Γ (t + M) = Γ t

/-- **THE FIRST FALSIFIABLE VISIBLE CLASS `P_per`.** Root identity, row stochasticity at every
 time, and a positive finite visible period. -/
def PPer (Γ : ℕ → Matrix V V ℝ) : Prop :=
  Γ 0 = 1 ∧ (∀ t : ℕ, IsRowStochastic (Γ t)) ∧ PeriodicFamily Γ

/-! ### A common finite response-table prior -/

section ResponsePrior

variable {I : Type v} [Fintype I] [DecidableEq I]

/-- The product weight of one complete response table. -/
def responseWeight (w : I → V → ℝ) (r : I → V) : ℝ :=
  ∏ i : I, w i (r i)

/-- Product response-table weights are nonnegative when every local weight is nonnegative. -/
theorem responseWeight_nonneg {w : I → V → ℝ} (hw : ∀ i j, 0 ≤ w i j) (r : I → V) :
    0 ≤ responseWeight w r := by
  unfold responseWeight
  exact Finset.prod_nonneg fun i _ => hw i (r i)

/-- **ONE COMMON PRIOR.** If every local row sums to one, the product weights on all response
 tables sum to one.  This is the finite product identity `Fintype.prod_sum`; no rationality or
 approximation is used. -/
theorem responseWeight_sum {w : I → V → ℝ} (hsum : ∀ i, ∑ j : V, w i j = 1) :
    ∑ r : I → V, responseWeight w r = 1 := by
  unfold responseWeight
  rw [← Fintype.prod_sum]
  simp [hsum]

/-- **THE COMMON PRIOR HAS THE DECLARED MARGINAL.** Summing product-table weights over all tables
 whose response at one coordinate is `j` gives exactly that coordinate's categorical weight. -/
theorem responseWeight_marginal {w : I → V → ℝ} (hsum : ∀ i, ∑ j : V, w i j = 1)
    (i0 : I) (j0 : V) :
    ∑ r : I → V, (if r i0 = j0 then responseWeight w r else 0) = w i0 j0 := by
  classical
  let w' : I → V → ℝ := fun i j => if i = i0 then (if j = j0 then w i j else 0) else w i j
  calc
    ∑ r : I → V, (if r i0 = j0 then responseWeight w r else 0) =
        ∑ r : I → V, ∏ i : I, w' i (r i) := by
      apply Finset.sum_congr rfl
      intro r _
      by_cases hr : r i0 = j0
      · rw [if_pos hr]
        unfold responseWeight
        rw [Fintype.prod_eq_mul_prod_subtype_ne, Fintype.prod_eq_mul_prod_subtype_ne]
        simp [w', hr]
      · rw [if_neg hr]
        rw [Fintype.prod_eq_mul_prod_subtype_ne]
        simp [w', hr]
    _ = ∏ i : I, ∑ j : V, w' i j := by
      rw [Fintype.prod_sum]
    _ = w i0 j0 := by
      rw [Fintype.prod_eq_mul_prod_subtype_ne]
      simp [w', hsum]

end ResponsePrior

/-! ### T1 necessity -/

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

#print axioms OIBridge.RootedClassification.responseWeight_nonneg
#print axioms OIBridge.RootedClassification.responseWeight_sum
#print axioms OIBridge.RootedClassification.responseWeight_marginal
#print axioms OIBridge.RootedClassification.rootedMap_zero
#print axioms OIBridge.RootedClassification.rootedMap_periodic
#print axioms OIBridge.RootedClassification.rootedMap_mem_PPer
