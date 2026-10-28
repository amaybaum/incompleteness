import OIBridge.RecurrenceHorizon

/-!
# Exact return of the actual rooted trajectory law

A return of the total iterate gives the rooted identity map for the existing
`RootedRealization`, using its actual common normalized hidden prior. This
closes the return-to-rooted-map step without assuming a uniform prior or full
support. The overlap/identity-return composition is reused from the kernel.

The full common-endpoint-history implication, a finite-order existence result,
and accessible-window consequences are not asserted here.
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

#print axioms rootedMap_eq_one_of_iterate_return
#print axioms pIndivisible_of_iterate_return_of_overlap

end OIBridge.RootedRecurrenceBridge
