import OIBridge.PhysicalC4Discharge

/-!
# Physical C4, round 2 — the storage-time reading of the store clause

Executed under the frozen control plane
`verification/programmes/physical-realization/round-c4-2-storage-readback/preregistration.md`,
blob `16cfd1303e7c279c8d6bab68b7112c3f25a7460e`.

`RoutedReadbackAtStorage` is **the manuscripts' own realization clause** — "a visible-history
record written into hidden boundary degrees is routed back into future visible conditionals within
the accessible window" — on the merged rooted interface, with the store clause and the causal read
leg read on the random variable the Track I discovery round's clause S names: the hidden state
**at the storage time**, `Law(H_s | X_s = x, X_0 = a)`. It is **not a new condition**, it is
**not** called a strengthening of the manuscripts' history-level condition, and **nothing is
numbered beyond C4**. The clause labels W, S, R(1), R(2) and the timing `0 < w ≤ s < t ≤ K` are the
discovery round's, transcribed; `marg` is the kernel's existing pushforward and every other symbol
is the merged rooted interface's.

**Nothing in this module says that C4 holds, or fails, at either physical cut.** The sealed core,
the tape-and-ledger coin and the separating carrier of `CS5` are carriers; the uncoupled product is
a control. No horizon is called accessible and no clock is attached to any carrier.

**Round 1's predicate is untouched.** `PhysicalC4Discharge.RoutedReadback` and
`PhysicalC4Discharge.rootedPosterior` keep their names and their statements, every theorem about
them stands as merged, and this module reopens, re-proves and edits none of them. The two
predicates coexist here under distinct names and every statement below says which one it is about.
Round 1 executed its freeze, reported a prediction falsified under its own spelling, and located
the divergence by a computed certificate, which is what a freeze is for.

Section `CS1` carries the two definitions and their elementary consequences, including the identity
exhibiting the read leg as the conditional visible law `Law(X_t | X_s = x, X_0 = a)`; `CS2` the
sealed C1–C4 core; `CS3` the two controls; `CS4` the return-horizon consequence, whose scope remark
travels with it — nothing below the return horizon; `CS5` the relation between the two readings, in
both directions, each by an exhibited carrier.
-/

namespace OIBridge
namespace PhysicalC4StorageReadback

open Finset Matrix HiddenMemory FiniteEntropy CausalReadback RecurrenceHorizon
open RootedClassification SubstratumInterfaceAudit PhysicalC4Discharge

/-! ### `CS1` — the storage-time reading, and its elementary consequences -/

section Predicate

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-- **`CS1-a`, THE ROOT-CONDITIONED HIDDEN LAW AT THE STORAGE TIME**, in the freeze's spelling: the
prior mass carried into the hidden value `k` at time `s` under the root `a`, jointly with the
visible value `x` at that same time, divided by the rooted probability of that visible value. This
is `Law(H_s | X_s = x, X_0 = a)`.

It is a **second object alongside** round 1's `PhysicalC4Discharge.rootedPosterior`, which divides
the root-conditioned weight of the initial hidden **seed**; that one is reused unmodified and is
neither renamed nor redefined. -/
noncomputable def rootedStatePosterior (R : RootedRealization V H) (a : V) (s : ℕ) (x : V) :
    H → ℝ :=
  fun k => (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) / rootedMap R s a x

/-- **`CS1-a`, ROUTED READBACK AT THE STORAGE SURFACE, WITHIN A WINDOW.**

W, write: the same hidden seed under two roots reaches different hidden states after `w` steps.
S, store: a visible value carries positive probability under both roots while the **storage-time**
root-conditioned hidden laws at that value differ. R(1), causal read: those two storage-time laws,
propagated with the visible value held fixed, give different visible laws at `t`. R(2), rooted
reappearance: the rooted rows at `t` differ. Timing: `0 < w ≤ s < t ≤ K`. -/
def RoutedReadbackAtStorage (K : ℕ) (R : RootedRealization V H) : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedStatePosterior R a s x ≠ rootedStatePosterior R b s x
    ∧ marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
        ≠ marg (rootedStatePosterior R b s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1)
    ∧ rootedMap R t a ≠ rootedMap R t b

/-- **`CS1-b`, MONOTONICITY IN THE WINDOW.** A routed witness at the storage surface within a
window is one within any longer window. -/
theorem routedReadbackAtStorage_mono {K K' : ℕ} {R : RootedRealization V H}
    (h : RoutedReadbackAtStorage K R) (hK : K ≤ K') : RoutedReadbackAtStorage K' R := by
  obtain ⟨a, b, w, s, t, x, hab, hw, hws, hst, htK, rest⟩ := h
  exact ⟨a, b, w, s, t, x, hab, hw, hws, hst, htK.trans hK, rest⟩

/-- **`CS1-c`, THE STORE CLAUSE IS AN OVERLAP.** A routed witness at the storage surface exposes
two distinct roots, a storage time strictly inside the window, and one visible value carrying
positive probability under both — exactly the hypothesis shape
`RecurrenceHorizon.horizon_verdict` consumes. The two positivity conjuncts are the part of the
store clause both readings share. -/
theorem routedReadbackAtStorage_overlap {K : ℕ} {R : RootedRealization V H}
    (h : RoutedReadbackAtStorage K R) :
    ∃ (a b : V) (s : ℕ) (x : V),
      a ≠ b ∧ s < K ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x := by
  obtain ⟨a, b, w, s, t, x, hab, -, -, hst, htK, -, hsa, hsb, -, -, -⟩ := h
  exact ⟨a, b, s, x, hab, lt_of_lt_of_le hst htK, hsa, hsb⟩

/-- The storage-surface weights of one root sum to the rooted probability of the visible value:
summing out the hidden value at time `s` recovers `rootedMap`. -/
theorem storageWeight_sum (R : RootedRealization V H) (a : V) (s : ℕ) (x : V) :
    (∑ k : H, ∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0)
      = rootedMap R s a x := by
  classical
  rw [Finset.sum_comm]
  simp only [rootedMap]
  refine Finset.sum_congr rfl fun h _ => ?_
  have hgen : ∀ p : V × H, (∑ k : H, if p = (x, k) then R.prior h else 0)
      = if p.1 = x then R.prior h else 0 := by
    rintro ⟨v, k₀⟩
    by_cases hv : v = x
    · subst hv
      simp [Finset.sum_ite_eq]
    · simp [Prod.ext_iff, hv]
  exact hgen _

/-- **The two roots' storage surfaces are disjoint.** The update is a bijection, so the preimage of
a visible-hidden pair at time `s` determines its root; a hidden value carrying weight under one
root therefore carries none under any other. -/
theorem storageWeight_eq_zero_of_root_ne (R : RootedRealization V H) {a b : V} (hab : a ≠ b)
    (s : ℕ) (x : V) (k : H)
    (hne : (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) ≠ 0) :
    (∑ h : H, if (⇑R.step)^[s] (b, h) = (x, k) then R.prior h else 0) = 0 := by
  classical
  by_contra hb
  obtain ⟨h₁, -, h₁ne⟩ := Finset.exists_ne_zero_of_sum_ne_zero hne
  obtain ⟨h₂, -, h₂ne⟩ := Finset.exists_ne_zero_of_sum_ne_zero hb
  have e₁ : (⇑R.step)^[s] (a, h₁) = (x, k) := by
    by_contra hc
    exact h₁ne (by rw [if_neg hc])
  have e₂ : (⇑R.step)^[s] (b, h₂) = (x, k) := by
    by_contra hc
    exact h₂ne (by rw [if_neg hc])
  have hinj : Function.Injective ((⇑R.step)^[s]) := R.step.injective.iterate s
  have := hinj (e₁.trans e₂.symm)
  exact hab (congrArg Prod.fst this)

/-- **THE STORE CLAUSE'S THIRD CONJUNCT, AT THE STORAGE SURFACE.** Whenever two distinct roots both
reach the same visible value with positive probability, their storage-time hidden laws differ. Both
are probability laws, and by the disjointness above their supports do not meet. This is a fact about
the storage-time object and is asserted of no other reading. -/
theorem rootedStatePosterior_ne (R : RootedRealization V H) {a b : V} (hab : a ≠ b) (s : ℕ)
    (x : V) (ha : 0 < rootedMap R s a x) (_hb : 0 < rootedMap R s b x) :
    rootedStatePosterior R a s x ≠ rootedStatePosterior R b s x := by
  classical
  intro heq
  have hz : ∀ k : H,
      (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) = 0 := by
    intro k
    by_contra hk
    have hbz := storageWeight_eq_zero_of_root_ne R hab s x k hk
    have hc := congrFun heq k
    simp only [rootedStatePosterior, hbz, zero_div] at hc
    rcases div_eq_zero_iff.mp hc with h | h
    · exact hk h
    · exact absurd h (ne_of_gt ha)
  have hsum := storageWeight_sum R a s x
  rw [Finset.sum_congr rfl fun k _ => hz k, Finset.sum_const_zero] at hsum
  exact absurd hsum.symm (ne_of_gt ha)

/-- **`CS1-d`, THE READ LEG IS A CONDITIONAL VISIBLE LAW.** Propagating the storage-time hidden law
with the visible value held fixed gives exactly `Law(X_t | X_s = x, X_0 = a)`. The identity is
proved from the step's bijectivity and nothing else, no predicate is defined to state it, and it is
**not** called a reformulation of the manuscripts' condition: it is a fact about this kernel
predicate's read leg. -/
theorem rootedStatePosterior_marg_eq (R : RootedRealization V H) (a : V) {s t : ℕ} (hst : s < t)
    (x : V) (_hpos : 0 < rootedMap R s a x) (y : V) :
    marg (rootedStatePosterior R a s x) (fun k => ((⇑R.step)^[t - s] (x, k)).1) y
      = (∑ h : H, if ((⇑R.step)^[s] (a, h)).1 = x ∧ ((⇑R.step)^[t] (a, h)).1 = y
                  then R.prior h else 0) / rootedMap R s a x := by
  classical
  have hiter : ∀ h : H, (⇑R.step)^[t - s] ((⇑R.step)^[s] (a, h)) = (⇑R.step)^[t] (a, h) := by
    intro h
    rw [← Function.iterate_add_apply, Nat.sub_add_cancel hst.le]
  have hinner : ∀ h : H,
      (∑ k : H, if (⇑R.step)^[s] (a, h) = (x, k)
          ∧ ((⇑R.step)^[t - s] (x, k)).1 = y then R.prior h else 0)
        = if ((⇑R.step)^[s] (a, h)).1 = x ∧ ((⇑R.step)^[t] (a, h)).1 = y
          then R.prior h else 0 := by
    intro h
    by_cases hx : ((⇑R.step)^[s] (a, h)).1 = x
    · have hp : (⇑R.step)^[s] (a, h) = (x, ((⇑R.step)^[s] (a, h)).2) := by
        rw [← hx]
      rw [Finset.sum_eq_single ((⇑R.step)^[s] (a, h)).2]
      · have hQ : ((⇑R.step)^[t - s] (x, ((⇑R.step)^[s] (a, h)).2)).1
            = ((⇑R.step)^[t] (a, h)).1 := by
          rw [← hp, hiter]
        rw [hQ, hx]
        simp only [← hp, true_and]
      · intro k _ hk
        refine if_neg ?_
        rintro ⟨hc, -⟩
        exact hk (by rw [hc])
      · intro hc
        exact absurd (Finset.mem_univ _) hc
    · rw [if_neg (by tauto)]
      refine Finset.sum_eq_zero fun k _ => if_neg ?_
      rintro ⟨hc, -⟩
      exact hx (by rw [hc])
  have hcomb : ∀ k : H,
      (if ((⇑R.step)^[t - s] (x, k)).1 = y then
        (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) else 0)
      = ∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k)
          ∧ ((⇑R.step)^[t - s] (x, k)).1 = y then R.prior h else 0 := by
    intro k
    by_cases hQ : ((⇑R.step)^[t - s] (x, k)).1 = y
    · rw [if_pos hQ]
      refine Finset.sum_congr rfl fun h _ => ?_
      by_cases hP : (⇑R.step)^[s] (a, h) = (x, k)
      · rw [if_pos hP, if_pos ⟨hP, hQ⟩]
      · rw [if_neg hP, if_neg (by tauto)]
    · rw [if_neg hQ]
      exact (Finset.sum_eq_zero fun h _ => if_neg (by tauto)).symm
  have hdiv : ∀ k : H,
      (if ((⇑R.step)^[t - s] (x, k)).1 = y then rootedStatePosterior R a s x k else 0)
      = (if ((⇑R.step)^[t - s] (x, k)).1 = y then
          (∑ h : H, if (⇑R.step)^[s] (a, h) = (x, k) then R.prior h else 0) else 0)
        / rootedMap R s a x := by
    intro k
    simp only [rootedStatePosterior]
    split <;> simp
  simp only [marg, Finset.sum_filter]
  rw [Finset.sum_congr rfl fun k _ => hdiv k, ← Finset.sum_div]
  congr 1
  rw [Finset.sum_congr rfl fun k _ => hcomb k, Finset.sum_comm]
  exact Finset.sum_congr rfl fun h _ => hinner h

end Predicate

/-! ### `CS4` — what a discharge under the storage-time reading would buy

The scope remark travels with the statements verbatim, from `[Main]` §2.3 through round 1: *"It does
**not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR control
remains a counterexample to that stronger statement."* Nothing is claimed below the return horizon,
and no horizon is called accessible. -/

section Return

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-- **`CS4-a`.** A routed witness at the storage surface binds its own storage time `s`, strictly
inside the window, and every identity return of the rooted map strictly after `s` carries the
recurrence-horizon conclusion. `RecurrenceHorizon.horizon_verdict` is reused and not re-proved.
Nothing is claimed for any horizon below the return. -/
theorem routedAtStorage_forces_return_indivisibility {K : ℕ} {R : RootedRealization V H}
    (h : RoutedReadbackAtStorage K R) :
    ∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 →
      C4r n (rootedMap R) ∧ PIndivisibleWithin n (rootedMap R) := by
  obtain ⟨a, b, s, x, hab, hsK, hsa, hsb⟩ := routedReadbackAtStorage_overlap h
  exact ⟨s, hsK, fun n hsn hI =>
    horizon_verdict hsn (rootedMap_isRowStochastic R s) hI hab hsa hsb⟩

/-- **`CS4-b`.** Finite reversibility supplies a visible period and root time is the identity, so
some multiple of the period is an identity return beyond the storage time: a routed witness at the
storage surface forces P-indivisibility somewhere in the full recurrence cycle. The horizon reached
is the return, not the accessible window. -/
theorem routedAtStorage_forces_indivisible_somewhere {K : ℕ} {R : RootedRealization V H}
    (h : RoutedReadbackAtStorage K R) : ∃ n, PIndivisibleWithin n (rootedMap R) := by
  obtain ⟨s, -, hcon⟩ := routedAtStorage_forces_return_indivisibility h
  obtain ⟨M, hM, hper⟩ := rootedMap_periodic R
  have hmul : ∀ q : ℕ, rootedMap R (q * M) = 1 := by
    intro q
    induction q with
    | zero => simpa using rootedMap_zero R
    | succ n ih =>
      have hq : (n + 1) * M = n * M + M := by ring
      rw [hq]
      exact (hper (n * M)).trans ih
  refine ⟨(s + 1) * M, (hcon ((s + 1) * M) ?_ (hmul (s + 1))).2⟩
  exact lt_of_lt_of_le (Nat.lt_succ_self s) (Nat.le_mul_of_pos_right _ hM)

end Return

/-! ### `CS2` — the sealed C1–C4 core under the storage-time reading

The carrier is round 1's, pinned by the same two equations and introduced as a **bound variable**:
the sealed core's states `((v, h), b)`, visible `(v, b)`, hidden `h`, passive step
`swapFn ((v, h), b) = ((h, v), b)`, transported along `OIRealization.partIdx` to a
`RootedRealization (Bool × Bool) Bool` with `step ((v, b), h) = ((h, b), v)` and the uniform prior
`1/2`. Satisfiability of the two equations is consumed from round 1's `core_realization_exists`
and is not re-proved.

This is a fact about one carrier under one reading. It licenses nothing about the general relation
of the forms and nothing about either physical cut. -/

section Core

variable (R : RootedRealization (Bool × Bool) Bool)
  (hstep : ∀ v b h : Bool, R.step ((v, b), h) = ((h, b), v))
  (hprior : ∀ h : Bool, R.prior h = 1 / 2)

include hstep hprior in
/-- At an odd storage time the core's **storage-time** hidden law is the point mass at the root's
own visible bit: on this carrier the hidden state at the storage surface is the root's visible bit
and carries all of the root information. -/
theorem core_statePosterior_odd {s : ℕ} (hs : Odd s) (a x : Bool × Bool) (ha : a.2 = x.2) :
    rootedStatePosterior R a s x = fun k => if k = a.1 then (1 : ℝ) else 0 := by
  have hden : rootedMap R s a x = 1 / 2 := by
    rw [core_rootedMap_odd R hstep hprior hs, if_pos ha]
  obtain ⟨v, b⟩ := a
  obtain ⟨y, c⟩ := x
  simp only at ha
  subst ha
  funext k
  simp only [rootedStatePosterior, hden, (core_involutive R hstep).iterate_odd hs, hstep, hprior,
    Prod.mk.injEq, Fintype.sum_bool]
  cases k <;> cases y <;> cases v <;> norm_num

include hstep hprior in
/-- **`CS2-b`, THE LOCATED CONTRAST AT THE STORAGE SURFACE.** On the sealed core at `s = 1` with
`x = (false, false)`: the two roots' **storage-time** hidden laws are the point masses at their own
visible bits and therefore differ, while round 1's `core_posterior_odd` — consumed and not
re-proved — has the two **seed** weights equal. The statement names both objects and asserts
nothing about which reading the manuscripts intend. -/
theorem core_storage_contrast :
    rootedStatePosterior R ((false, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
        = (fun k => if k = false then (1 : ℝ) else 0)
      ∧ rootedStatePosterior R ((true, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
        = (fun k => if k = true then (1 : ℝ) else 0)
      ∧ rootedStatePosterior R ((false, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
        ≠ rootedStatePosterior R ((true, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
      ∧ rootedPosterior R ((false, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
        = rootedPosterior R ((true, false) : Bool × Bool) 1 ((false, false) : Bool × Bool) := by
  have hodd : Odd 1 := ⟨0, by norm_num⟩
  have ha := core_statePosterior_odd R hstep hprior hodd ((false, false) : Bool × Bool)
    ((false, false) : Bool × Bool) rfl
  have hb := core_statePosterior_odd R hstep hprior hodd ((true, false) : Bool × Bool)
    ((false, false) : Bool × Bool) rfl
  refine ⟨ha, hb, ?_, ?_⟩
  · rw [ha, hb]
    intro hc
    have h0 := congrFun hc false
    norm_num at h0
  · rw [core_posterior_odd R hstep hprior hodd ((false, false) : Bool × Bool)
      ((false, false) : Bool × Bool) rfl,
      core_posterior_odd R hstep hprior hodd ((true, false) : Bool × Bool)
      ((false, false) : Bool × Bool) rfl]

include hstep hprior in
/-- **`CS2-a`.** Under the storage-time reading the sealed C1–C4 core carries a routed witness at
window `2`, on **round 1's own frozen witness tuple** `a = (false, false)`, `b = (true, false)`,
`(w, s, t) = (1, 1, 2)`, `x = (h₀, false)` for either `h₀`. -/
theorem core_routedReadbackAtStorage_two (h₀ : Bool) : RoutedReadbackAtStorage 2 R := by
  have hodd : Odd 1 := ⟨0, by norm_num⟩
  have heven : Even 2 := ⟨1, by norm_num⟩
  have hsub : (2 : ℕ) - 1 = 1 := rfl
  have hda : rootedMap R 1 ((false, false) : Bool × Bool) ((h₀, false) : Bool × Bool) = 1 / 2 := by
    rw [core_rootedMap_odd R hstep hprior hodd, if_pos rfl]
  have hdb : rootedMap R 1 ((true, false) : Bool × Bool) ((h₀, false) : Bool × Bool) = 1 / 2 := by
    rw [core_rootedMap_odd R hstep hprior hodd, if_pos rfl]
  have pa := core_statePosterior_odd R hstep hprior hodd ((false, false) : Bool × Bool)
    ((h₀, false) : Bool × Bool) rfl
  have pb := core_statePosterior_odd R hstep hprior hodd ((true, false) : Bool × Bool)
    ((h₀, false) : Bool × Bool) rfl
  refine ⟨(false, false), (true, false), 1, 1, 2, (h₀, false), by decide, by norm_num, le_rfl,
    by norm_num, le_rfl, ⟨false, by rw [hprior]; norm_num, ?_⟩, by rw [hda]; norm_num,
    by rw [hdb]; norm_num, ?_, ?_, ?_⟩
  · rw [Function.iterate_one, hstep, hstep]
    simp
  · rw [pa, pb]
    intro hc
    have h0 := congrFun hc false
    norm_num at h0
  · rw [hsub, pa, pb]
    intro hc
    have h0 := congrFun hc ((false, false) : Bool × Bool)
    simp only [marg, Finset.sum_filter, Function.iterate_one, hstep, Fintype.sum_bool,
      Prod.mk.injEq] at h0
    norm_num at h0
  · intro hc
    have h0 := congrFun hc ((false, false) : Bool × Bool)
    rw [core_rootedMap_even R hstep hprior heven, core_rootedMap_even R hstep hprior heven] at h0
    norm_num at h0

end Core

/-! ### `CS3-a` — recurrence without a write is not readback, under the storage-time reading

The uncoupled product of `partition_coupling_probe.py`: `V = ZMod 3`, `H = ZMod 4`,
`step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`, a bound variable pinned by those equations.
The write clause is the one clause the correction does not touch, and round 1's `product_iterate`
is reused unmodified. -/

section Product

variable (R : RootedRealization (ZMod 3) (ZMod 4))
  (hstep : ∀ (v : ZMod 3) (h : ZMod 4), R.step (v, h) = (v + 1, h + 1))

include hstep in
/-- **`CS3-a`.** The write clause fails at **every** `w`: the hidden component after `w` steps is
the seed advanced by `w` under both roots, so there is no routed witness at the storage surface at
any window either. -/
theorem product_not_routedReadbackAtStorage (K : ℕ) : ¬ RoutedReadbackAtStorage K R := by
  rintro ⟨a, b, w, s, t, x, -, -, -, -, -, ⟨h, -, hne⟩, -, -, -, -, -⟩
  rw [product_iterate R hstep, product_iterate R hstep] at hne
  exact hne rfl

end Product

/-! ### `CS3-b`, `CS3-c` — write and store without in-window routing, under the storage-time reading

The tape-and-ledger coin: `V = Bool`, `H = Bool × Bool × Bool` (tape₁, tape₂, ledger),
`step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x))`, prior `1/4` on a blank ledger and `0`
otherwise, a bound variable pinned by those equations. Round 1's `tapeLedger_step_eq`,
`tapeLedger_rootedMap_mid` and `tapeLedger_rootedMap_four` are reused unmodified. -/

section TapeLedger

variable (R : RootedRealization Bool (Bool × Bool × Bool))
  (hstep : ∀ x t₁ t₂ l : Bool, R.step (x, (t₁, t₂, l)) = (xor x t₁, (t₂, t₁, xor l x)))
  (hprior : ∀ t₁ t₂ l : Bool, R.prior (t₁, t₂, l) = if l then 0 else 1 / 4)

include hstep hprior in
/-- **`CS3-b`.** There is **no** routed witness at the storage surface within `K = 3`, by a computed
certificate rather than a search: the failing clause is R(2), which is spelling-independent — the
rooted rows coincide at every time the window admits for the read. -/
theorem tapeLedger_not_routedReadbackAtStorage_three : ¬ RoutedReadbackAtStorage 3 R := by
  rintro ⟨a, b, w, s, t, x, -, hw, hws, hst, ht3, -, -, -, -, -, hrows⟩
  apply hrows
  have h1t : 1 ≤ t := le_trans hw (le_trans hws hst.le)
  rw [tapeLedger_rootedMap_mid R hstep hprior t h1t ht3]

include hstep hprior in
/-- The coin's storage-time hidden law at `s = 1` on the visible value `false`: uniform on the two
hidden states whose tape-one and ledger entries both equal the root. -/
theorem tapeLedger_statePosterior_one (a : Bool) :
    rootedStatePosterior R a 1 false
      = fun k => if k.2.1 = a ∧ k.2.2 = a then (1 : ℝ) / 2 else 0 := by
  have hs := tapeLedger_step_eq R hstep
  have hmid := tapeLedger_rootedMap_mid R hstep hprior 1 le_rfl (by norm_num)
  funext k
  obtain ⟨k₁, k₂, k₃⟩ := k
  simp only [rootedStatePosterior, hs, hmid, hprior, Function.iterate_succ_apply,
    Function.iterate_zero_apply, Fintype.sum_prod_type, Fintype.sum_bool, Prod.mk.injEq]
  cases a <;> cases k₁ <;> cases k₂ <;> cases k₃ <;> norm_num

include hstep hprior in
/-- **`CS3-c`.** At the return the routed form fires at the storage surface, on **round 1's own
recorded scratch tuple** `(w, s, t) = (1, 1, 4)`, roots `false` and `true`, `x = false`. -/
theorem tapeLedger_routedReadbackAtStorage_four : RoutedReadbackAtStorage 4 R := by
  have hs := tapeLedger_step_eq R hstep
  have hmid := tapeLedger_rootedMap_mid R hstep hprior 1 le_rfl (by norm_num)
  have h4 := tapeLedger_rootedMap_four R hstep hprior
  have hsub : (4 : ℕ) - 1 = 3 := rfl
  have pa := tapeLedger_statePosterior_one R hstep hprior false
  have pb := tapeLedger_statePosterior_one R hstep hprior true
  refine ⟨false, true, 1, 1, 4, false, by decide, by norm_num, le_rfl, by norm_num, le_rfl,
    ⟨(false, false, false), by rw [hprior]; norm_num, ?_⟩, by rw [hmid]; norm_num,
    by rw [hmid]; norm_num, ?_, ?_, ?_⟩
  · simp [hs]
  · exact rootedStatePosterior_ne R (by decide) 1 false (by rw [hmid]; norm_num)
      (by rw [hmid]; norm_num)
  · rw [hsub, pa, pb]
    intro hc
    have h0 := congrFun hc false
    simp only [marg, Finset.sum_filter, hs, Function.iterate_succ_apply,
      Function.iterate_zero_apply, Fintype.sum_prod_type, Fintype.sum_bool] at h0
    norm_num at h0
  · intro hc
    have h0 := congrFun hc false
    rw [h4] at h0
    simp only [Matrix.one_apply] at h0
    norm_num at h0

end TapeLedger

/-! ### `CS5` — the relation between the two readings, in both directions

Each direction is settled by an **exhibited carrier with a computed certificate**, never by a
failed search. Neither reading is called stronger than the other, and no ordering of them is
asserted. These are statements about two kernel predicates and about nothing physical. -/

section Relation

/-- **`CS5-a`, ON THE EXHIBITED CARRIER.** The sealed core satisfies the storage-time reading at
window `2` and, by round 1's merged `core_not_routedReadback` — consumed and not re-proved — round
1's reading at no window. -/
theorem core_storageReadback_and_not_routedReadback
    (R : RootedRealization (Bool × Bool) Bool)
    (hstep : ∀ v b h : Bool, R.step ((v, b), h) = ((h, b), v))
    (hprior : ∀ h : Bool, R.prior h = 1 / 2) :
    RoutedReadbackAtStorage 2 R ∧ ∀ K, ¬ RoutedReadback K R :=
  ⟨core_routedReadbackAtStorage_two R hstep hprior false,
    core_not_routedReadback R hstep hprior⟩

/-- **`CS5-a`.** The storage-time reading does **not** imply round 1's, as a general implication
over every rooted realization on the sealed core's carrier type and every window. The certificate is
the exhibited carrier above. -/
theorem storageReadback_not_implies_routedReadback :
    ¬ ∀ (K : ℕ) (R : RootedRealization (Bool × Bool) Bool),
        RoutedReadbackAtStorage K R → RoutedReadback K R := by
  intro hall
  obtain ⟨R, hstep, hprior⟩ := core_realization_exists
  exact core_not_routedReadback R hstep hprior 2
    (hall 2 R (core_routedReadbackAtStorage_two R hstep hprior false))

end Relation

/-! ### `CS5-b` — the other direction, on a second exhibited carrier

`V = Bool`, `H = Bool × Bool`, the reversible update pinned by the eight equations below, and the
prior `1/2` on the two hidden values whose components differ and `0` on the other two. The carrier
is a **bound variable pinned by those equations**, not a definition, and its prior is pinned in the
statements that need it and is chosen by no later result.

On it round 1's reading fires at window `2` while the storage-time reading fires at no admissible
tuple within window `2`: the two roots' storage-time laws are carried by disjoint hidden values
whose visible futures at `t = 2` coincide, so the causal read leg collapses, while round 1's read
leg — which propagates the root-conditioned **seed** weight through the same dynamics — does not. -/

section Separator

variable (R : RootedRealization Bool (Bool × Bool))
  (hstep : ∀ x h₁ h₂ : Bool, R.step (x, (h₁, h₂)) =
    if x then (if h₁ then (if h₂ then (false, (false, true)) else (false, (true, true)))
                     else (if h₂ then (false, (false, false)) else (true, (false, false))))
          else (if h₁ then (if h₂ then (true, (true, true)) else (true, (false, true)))
                     else (if h₂ then (false, (true, false)) else (true, (true, false)))))
  (hprior : ∀ h : Bool × Bool, R.prior h = if h.1 = h.2 then 0 else 1 / 2)

/-- The carrier of `CS5-b` exists: the eight equations pin a bijection of the eight states and the
declared prior is nonnegative and normalized. -/
theorem sep_realization_exists :
    ∃ R : RootedRealization Bool (Bool × Bool),
      (∀ x h₁ h₂ : Bool, R.step (x, (h₁, h₂)) =
        if x then (if h₁ then (if h₂ then (false, (false, true)) else (false, (true, true)))
                         else (if h₂ then (false, (false, false)) else (true, (false, false))))
              else (if h₁ then (if h₂ then (true, (true, true)) else (true, (false, true)))
                         else (if h₂ then (false, (true, false)) else (true, (true, false)))))
        ∧ ∀ h : Bool × Bool, R.prior h = if h.1 = h.2 then 0 else 1 / 2 := by
  refine ⟨{ step :=
              { toFun := fun p : Bool × Bool × Bool =>
                  if p.1 then
                    (if p.2.1 then (if p.2.2 then (false, (false, true))
                                    else (false, (true, true)))
                     else (if p.2.2 then (false, (false, false)) else (true, (false, false))))
                  else
                    (if p.2.1 then (if p.2.2 then (true, (true, true)) else (true, (false, true)))
                     else (if p.2.2 then (false, (true, false)) else (true, (true, false))))
                invFun := fun q : Bool × Bool × Bool =>
                  if q.1 then
                    (if q.2.1 then (if q.2.2 then (false, (true, true)) else (false, (false, false)))
                     else (if q.2.2 then (false, (true, false)) else (true, (false, false))))
                  else
                    (if q.2.1 then (if q.2.2 then (true, (true, false)) else (false, (false, true)))
                     else (if q.2.2 then (true, (true, true)) else (true, (false, true))))
                left_inv := by decide
                right_inv := by decide }
            prior := fun h => if h.1 = h.2 then 0 else 1 / 2
            prior_nonneg := fun h => by
              show (0 : ℝ) ≤ if h.1 = h.2 then 0 else 1 / 2
              split <;> norm_num
            prior_sum := by
              simp only [Fintype.sum_prod_type, Fintype.sum_bool]
              norm_num },
          fun _ _ _ => rfl, fun _ => rfl⟩

include hstep hprior in
/-- The separating carrier's rooted rows at `1` and `2`. The root `true` is pinned to the visible
value `false` at time `1`, which is what confines every admissible storage surface within window
`2` to `x = false`. -/
theorem sep_rootedMap : rootedMap R 1 false false = 1 / 2 ∧ rootedMap R 1 false true = 1 / 2
    ∧ rootedMap R 1 true false = 1 ∧ rootedMap R 1 true true = 0
    ∧ rootedMap R 2 false false = 1 / 2 ∧ rootedMap R 2 true false = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    · simp only [rootedMap, Function.iterate_succ_apply, Function.iterate_zero_apply, hstep,
        hprior, Fintype.sum_prod_type, Fintype.sum_bool]
      norm_num

include hstep hprior in
/-- The separating carrier's **storage-time** hidden laws at `s = 1` on the visible value `false`:
the root `false` is carried by the single hidden value `(true, false)`, the root `true` by the two
hidden values whose components agree — disjointly, as the general lemma requires. -/
theorem sep_statePosterior :
    rootedStatePosterior R false 1 false
        = (fun k => if k = ((true, false) : Bool × Bool) then (1 : ℝ) else 0)
      ∧ rootedStatePosterior R true 1 false
        = (fun k : Bool × Bool => if k.1 = k.2 then (1 : ℝ) / 2 else 0) := by
  have hd := sep_rootedMap R hstep hprior
  constructor <;>
    · funext k
      obtain ⟨k₁, k₂⟩ := k
      simp only [rootedStatePosterior, hd.1, hd.2.2.1, Function.iterate_succ_apply,
        Function.iterate_zero_apply, hstep, hprior, Fintype.sum_prod_type, Fintype.sum_bool,
        Prod.mk.injEq]
      cases k₁ <;> cases k₂ <;> norm_num

include hstep hprior in
/-- The separating carrier's **seed** laws at the same surface, in round 1's spelling, consumed
here only to exhibit that round 1's read leg separates the roots where the storage-time leg does
not. -/
theorem sep_seedPosterior :
    rootedPosterior R false 1 false
        = (fun h => if h = ((false, true) : Bool × Bool) then (1 : ℝ) else 0)
      ∧ rootedPosterior R true 1 false
        = (fun h : Bool × Bool => if h.1 = h.2 then (0 : ℝ) else 1 / 2) := by
  have hd := sep_rootedMap R hstep hprior
  constructor <;>
    · funext h
      obtain ⟨h₁, h₂⟩ := h
      simp only [rootedPosterior, hd.1, hd.2.2.1, Function.iterate_succ_apply,
        Function.iterate_zero_apply, hstep, hprior, Prod.mk.injEq]
      cases h₁ <;> cases h₂ <;> norm_num

include hstep hprior in
/-- **THE COLLAPSE OF THE CAUSAL READ LEG.** Propagating the two storage-time laws from `s = 1`
with the visible value held fixed gives the **same** visible law at `t = 2`: both are the point mass
at `true`. By `CS1-d` this says `Law(X₂ | X₁ = false, X₀ = false) = Law(X₂ | X₁ = false,
X₀ = true)` on this carrier. -/
theorem sep_read_collapse :
    marg (rootedStatePosterior R false 1 false) (fun k => ((⇑R.step)^[1] (false, k)).1)
      = marg (rootedStatePosterior R true 1 false) (fun k => ((⇑R.step)^[1] (false, k)).1) := by
  have hp := sep_statePosterior R hstep hprior
  funext y
  rw [hp.1, hp.2]
  simp only [marg, Finset.sum_filter, Function.iterate_succ_apply, Function.iterate_zero_apply,
    hstep, Fintype.sum_prod_type, Fintype.sum_bool, Prod.mk.injEq]
  cases y <;> norm_num

include hstep hprior in
/-- **`CS5-b`, THE POSITIVE HALF OF THE CERTIFICATE.** Round 1's reading fires on this carrier at
window `2`, with `a = false`, `b = true`, `(w, s, t) = (1, 1, 2)` and `x = false`. -/
theorem sep_routedReadback_two : RoutedReadback 2 R := by
  have hd := sep_rootedMap R hstep hprior
  have hp := sep_seedPosterior R hstep hprior
  refine ⟨false, true, 1, 1, 2, false, by decide, by norm_num, le_rfl, by norm_num, le_rfl,
    ⟨(false, true), by rw [hprior]; norm_num, ?_⟩, by rw [hd.1]; norm_num,
    by rw [hd.2.2.1]; norm_num, ?_, ?_, ?_⟩
  · simp only [Function.iterate_one, hstep]
    norm_num
  · rw [hp.1, hp.2]
    intro hc
    have h0 := congrFun hc ((false, true) : Bool × Bool)
    norm_num at h0
  · rw [show (2 : ℕ) - 1 = 1 from rfl, hp.1, hp.2]
    intro hc
    have h0 := congrFun hc false
    simp only [marg, Finset.sum_filter, Function.iterate_succ_apply,
      Function.iterate_zero_apply, hstep, Fintype.sum_prod_type, Fintype.sum_bool,
      Prod.mk.injEq] at h0
    norm_num at h0
  · intro hc
    have h0 := congrFun hc false
    rw [hd.2.2.2.2.1, hd.2.2.2.2.2] at h0
    norm_num at h0

include hstep hprior in
/-- **`CS5-b`, THE NEGATIVE HALF OF THE CERTIFICATE.** The storage-time reading fires at **no**
admissible tuple within window `2` on this carrier. The window forces `w = s = 1` and `t = 2`; the
root `true` reaches only the visible value `false` at time `1`, so the store clause's two positivity
conjuncts force `x = false`; and at that surface the causal read leg collapses by
`sep_read_collapse`. This is a computed certificate, not a failed search. -/
theorem sep_not_routedReadbackAtStorage_two : ¬ RoutedReadbackAtStorage 2 R := by
  have hd := sep_rootedMap R hstep hprior
  have hcol := sep_read_collapse R hstep hprior
  rintro ⟨a, b, w, s, t, x, hab, hw, hws, hst, ht2, -, hpa, hpb, -, hr, -⟩
  have hs1 : s = 1 := le_antisymm (by omega) (le_trans hw hws)
  have ht : t = 2 := by omega
  subst hs1
  subst ht
  have hcases : (a = false ∧ b = true) ∨ (a = true ∧ b = false) := by
    revert hab; cases a <;> cases b <;> simp
  have hxf : x = false := by
    cases x with
    | false => rfl
    | true =>
      exfalso
      rcases hcases with ⟨ha, hb⟩ | ⟨ha, hb⟩
      · rw [hb, hd.2.2.2.1] at hpb
        exact lt_irrefl 0 hpb
      · rw [ha, hd.2.2.2.1] at hpa
        exact lt_irrefl 0 hpa
  subst hxf
  rw [show (2 : ℕ) - 1 = 1 from rfl] at hr
  rcases hcases with ⟨ha, hb⟩ | ⟨ha, hb⟩ <;> subst ha <;> subst hb
  · exact hr hcol
  · exact hr hcol.symm

end Separator

section RelationTwo

/-- **`CS5-b`.** Round 1's reading does **not** imply the storage-time reading, as a general
implication over every rooted realization on `Bool` with hidden carrier `Bool × Bool` and every
window. The certificate is the exhibited carrier of the previous section, at window `2`.

Together with `storageReadback_not_implies_routedReadback` this says the two readings are
**incomparable as predicates**, by two exhibited carriers with exact certificates. No ordering of
them is asserted and neither is called stronger than the other. -/
theorem routedReadback_not_implies_storageReadback :
    ¬ ∀ (K : ℕ) (R : RootedRealization Bool (Bool × Bool)),
        RoutedReadback K R → RoutedReadbackAtStorage K R := by
  intro hall
  obtain ⟨R, hstep, hprior⟩ := sep_realization_exists
  exact sep_not_routedReadbackAtStorage_two R hstep hprior
    (hall 2 R (sep_routedReadback_two R hstep hprior))

end RelationTwo

end PhysicalC4StorageReadback
end OIBridge

#print axioms OIBridge.PhysicalC4StorageReadback.routedReadbackAtStorage_mono
#print axioms OIBridge.PhysicalC4StorageReadback.routedReadbackAtStorage_overlap
#print axioms OIBridge.PhysicalC4StorageReadback.storageWeight_sum
#print axioms OIBridge.PhysicalC4StorageReadback.storageWeight_eq_zero_of_root_ne
#print axioms OIBridge.PhysicalC4StorageReadback.rootedStatePosterior_ne
#print axioms OIBridge.PhysicalC4StorageReadback.rootedStatePosterior_marg_eq
#print axioms OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_return_indivisibility
#print axioms OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere
#print axioms OIBridge.PhysicalC4StorageReadback.core_statePosterior_odd
#print axioms OIBridge.PhysicalC4StorageReadback.core_storage_contrast
#print axioms OIBridge.PhysicalC4StorageReadback.core_routedReadbackAtStorage_two
#print axioms OIBridge.PhysicalC4StorageReadback.product_not_routedReadbackAtStorage
#print axioms OIBridge.PhysicalC4StorageReadback.tapeLedger_not_routedReadbackAtStorage_three
#print axioms OIBridge.PhysicalC4StorageReadback.tapeLedger_statePosterior_one
#print axioms OIBridge.PhysicalC4StorageReadback.tapeLedger_routedReadbackAtStorage_four
#print axioms OIBridge.PhysicalC4StorageReadback.core_storageReadback_and_not_routedReadback
#print axioms OIBridge.PhysicalC4StorageReadback.storageReadback_not_implies_routedReadback
#print axioms OIBridge.PhysicalC4StorageReadback.sep_realization_exists
#print axioms OIBridge.PhysicalC4StorageReadback.sep_rootedMap
#print axioms OIBridge.PhysicalC4StorageReadback.sep_statePosterior
#print axioms OIBridge.PhysicalC4StorageReadback.sep_seedPosterior
#print axioms OIBridge.PhysicalC4StorageReadback.sep_read_collapse
#print axioms OIBridge.PhysicalC4StorageReadback.sep_routedReadback_two
#print axioms OIBridge.PhysicalC4StorageReadback.sep_not_routedReadbackAtStorage_two
#print axioms OIBridge.PhysicalC4StorageReadback.routedReadback_not_implies_storageReadback
