import OIBridge.RecurrenceHorizon
import OIBridge.EquivalenceChain
import OIBridge.ObservabilityQuotient

/-!
# Exact return of the actual rooted trajectory law

A return of the total iterate gives the rooted identity map for the existing
`RootedRealization`, using its actual common normalized hidden prior. This
closes the return-to-rooted-map step without assuming a uniform prior or full
support. The overlap/identity-return composition is reused from the kernel.

The finite-order return and rooted periodicity are instantiated from the existing
permutation order machinery. The full common-endpoint-history implication and
accessible-window consequences are not asserted here.
-/

namespace OIBridge.RootedRecurrenceBridge

open CausalReadback RecurrenceHorizon

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H]

/-- An exact microscopic iterate return gives the actual rooted identity map. -/
theorem rootedMap_eq_one_of_iterate_return (R : RootedRealization V H) (n : ℕ)
    (hreturn : ∀ s : V × H, ((R.step : V × H → V × H)^[n]) s = s) :
    rootedMap R n = 1 := by
  ext a j
  by_cases haj : a = j
  · subst j
    simp [rootedMap, hreturn, R.prior_sum]
  · simp [rootedMap, hreturn, haj]

/-- The actual trajectory return composes with the existing overlap theorem.
This is a whole-return-horizon conclusion, not a short-window assertion. -/
theorem pIndivisible_of_iterate_return_of_overlap (R : RootedRealization V H)
    {n s : ℕ} (hsn : s < n)
    (hreturn : ∀ z : V × H, ((R.step : V × H → V × H)^[n]) z = z)
    {a b : V} (hab : a ≠ b) {x : V}
    (hax : 0 < rootedMap R s a x) (hbx : 0 < rootedMap R s b x) :
    PIndivisibleWithin n (rootedMap R) :=
  pIndivisible_of_rooted_identity_return_of_overlap R hsn
    (rootedMap_eq_one_of_iterate_return R n hreturn) hab hax hbx

/-- Instantiate exact iterate return at the finite permutation's order.
`Equiv.Perm` powers and function iteration are the same underlying operation. -/
theorem iterate_return_at_order (R : RootedRealization V H) :
    ∀ z : V × H, ((R.step : V × H → V × H)^[orderOf R.step]) z = z := by
  intro z
  change (R.step ^ orderOf R.step) z = z
  rw [pow_orderOf_eq_one]
  rfl

/-- The actual rooted law returns to the identity at that order. -/
theorem rootedMap_at_order (R : RootedRealization V H) :
    rootedMap R (orderOf R.step) = 1 :=
  rootedMap_eq_one_of_iterate_return R _ (iterate_return_at_order R)

/-- The entire actual rooted family shares the microscopic permutation period. -/
theorem rootedMap_add_order (R : RootedRealization V H) (t : ℕ) :
    rootedMap R (t + orderOf R.step) = rootedMap R t := by
  have hiter : ((R.step : V × H → V × H)^[t + orderOf R.step]) =
      ((R.step : V × H → V × H)^[t]) := by
    change ⇑(R.step ^ (t + orderOf R.step)) = ⇑(R.step ^ t)
    rw [pow_add, pow_orderOf_eq_one, mul_one]
  unfold rootedMap
  rw [hiter]

/-- Finite permutation order supplies a positive shared rooted period. -/
theorem exists_positive_rooted_period (R : RootedRealization V H) :
    ∃ n : ℕ, 0 < n ∧ rootedMap R n = 1 ∧
      ∀ t : ℕ, rootedMap R (t + n) = rootedMap R t := by
  refine ⟨orderOf R.step, orderOf_pos R.step, rootedMap_at_order R, ?_⟩
  exact rootedMap_add_order R

/-- A non-permutation rooted map cannot have a stochastic right divisor to a
later identity return. This is the manuscript's stochastic-inverse composition. -/
theorem no_stochastic_divisor_of_return_nonperm (R : RootedRealization V H)
    (n s : ℕ)
    (hreturn : ∀ z : V × H, ((R.step : V × H → V × H)^[n]) z = z)
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, rootedMap R s = σ.permMatrix ℝ) :
    ¬ ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ rootedMap R n = rootedMap R s * Λ := by
  rintro ⟨Λ, hΛ, hfactor⟩
  have hA : rootedMap R s ∈ Matrix.rowStochastic ℝ V :=
    Matrix.mem_rowStochastic_iff_sum.mpr (rootedMap_isRowStochastic R s)
  have hB : Λ ∈ Matrix.rowStochastic ℝ V :=
    Matrix.mem_rowStochastic_iff_sum.mpr hΛ
  have hprod : rootedMap R s * Λ = 1 :=
    hfactor.symm.trans (rootedMap_eq_one_of_iterate_return R n hreturn)
  exact hnonperm (EquivalenceChain.isPermMatrix_of_stochastic_inverse hA hB (Or.inl hprod))

/-- The single forbidden divisor already disproves whole-horizon P-divisibility. -/
theorem pIndivisible_of_return_nonperm (R : RootedRealization V H) {n s : ℕ}
    (hsn : s < n)
    (hreturn : ∀ z : V × H, ((R.step : V × H → V × H)^[n]) z = z)
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, rootedMap R s = σ.permMatrix ℝ) :
    PIndivisibleWithin n (rootedMap R) := by
  intro hdiv
  obtain ⟨Λ, hΛ, hfactor⟩ := hdiv s n hsn le_rfl
  exact no_stochastic_divisor_of_return_nonperm R n s hreturn hnonperm ⟨Λ, hΛ, hfactor⟩

/-- The actual finite representative's non-permutation witness gives the
recurrence-cycle verdict, without a claim about earlier accessible windows. -/
theorem pIndivisible_at_order_of_nonperm (R : RootedRealization V H) {s : ℕ}
    (hsn : s < orderOf R.step)
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, rootedMap R s = σ.permMatrix ℝ) :
    PIndivisibleWithin (orderOf R.step) (rootedMap R) :=
  pIndivisible_of_return_nonperm R hsn (iterate_return_at_order R) hnonperm

#print axioms iterate_return_at_order
#print axioms rootedMap_at_order
#print axioms rootedMap_add_order
#print axioms exists_positive_rooted_period
#print axioms no_stochastic_divisor_of_return_nonperm
#print axioms pIndivisible_of_return_nonperm
#print axioms pIndivisible_at_order_of_nonperm

#print axioms rootedMap_eq_one_of_iterate_return
#print axioms pIndivisible_of_iterate_return_of_overlap

end OIBridge.RootedRecurrenceBridge
