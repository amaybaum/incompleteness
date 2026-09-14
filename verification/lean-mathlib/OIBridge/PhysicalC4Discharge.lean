import OIBridge.RecurrenceHorizon
import OIBridge.RootedClassification
import OIBridge.SubstratumInterfaceAudit

/-!
# Physical C4 discharge, round 1 — the realization clause on the merged rooted interface

Executed under the frozen control plane
`verification/programmes/physical-realization/round-c4-1-physical-discharge/preregistration.md`,
blob `a80334a5d5f19125b69459523acf723b607f97e1`.

`RoutedReadback` is **the manuscripts' own realization clause**, formalized: "a visible-history
record written into hidden boundary degrees is routed back into future visible conditionals within
the accessible window". It is **not a new condition**, it is **not** called a strengthening of the
manuscript's history-level condition, and **nothing is numbered beyond C4**. It is transcribed
clause for clause — W, S, R(1), R(2), timing `0 < w ≤ s < t ≤ K` — from the Track I discovery
round's frozen parent, with `marg` the kernel's existing pushforward and every other symbol the
merged rooted interface's. The discovery round's results are consumed and none is reopened: the
routed form implies the history-level condition, implies neither `C4e` nor `C4r` on the same
window, and does not imply `PIndivisibleWithin K` on the same window.

**Nothing in this module says that C4 holds, or fails, at either physical cut.** The sealed core
and the tape-and-ledger coin are carriers; the uncoupled product is a control; a cut realization
of the wave substratum is an abstract object with a region and a prior as parameters. No horizon
is called accessible and no clock is attached to any carrier.

**A recorded discrepancy, not repaired here.** The frozen spelling of `rootedPosterior` divides the
root-conditioned weight of the **initial hidden seed** by the rooted map, while the discovery
round's clause S names the law of the hidden state **at the storage time**,
`Law(H_s | X_s = x, X_0 = a)`. On a reversible update the two are in bijection for each single
root, but the bijections of two distinct roots differ, so the two readings are not the same
predicate. The kernel spelling below is the frozen one, unreshaped. `core_store_gap` is the
computed certificate locating the divergence on the sealed core, and
`core_not_routedReadback` is its consequence there. The freeze is immutable; this is recorded in
the round's result note and is not edited into the control plane.

Section RD0 carries the predicate and its two extractions; RD1, RD2 and RD3 the three elementary
carriers; RD4 the return-horizon consequence, whose scope remark travels with it — nothing below
the return horizon; RD5 the cut realization and the named lattice residual.
-/

namespace OIBridge
namespace PhysicalC4Discharge

open Finset Matrix HiddenMemory FiniteEntropy CausalReadback RecurrenceHorizon
open RootedClassification SubstratumInterfaceAudit

/-! ### `RD0` — the predicate, and two elementary consequences -/

section Predicate

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-- **THE ROOT-CONDITIONED HIDDEN WEIGHT AT A STORAGE SURFACE**, in the freeze's spelling: the
prior mass of a hidden seed compatible with the visible value `x` at time `s` under the root `a`,
divided by the rooted probability of that visible value. -/
noncomputable def rootedPosterior (R : RootedRealization V H) (a : V) (s : ℕ) (x : V) : H → ℝ :=
  fun h => (if ((⇑R.step)^[s] (a, h)).1 = x then R.prior h else 0) / rootedMap R s a x

/-- **ROUTED READBACK WITHIN A WINDOW** — the manuscripts' realization clause on the merged rooted
interface, transcribed from the Track I discovery round's frozen parent.

W, write: the same hidden seed under two roots reaches different hidden states after `w` steps.
S, store: a visible value carries positive probability under both roots while the root-conditioned
hidden weights at that value differ. R(1), causal read: those two weights, propagated with the
visible value held fixed, give different visible laws at `t`. R(2), rooted reappearance: the rooted
rows at `t` differ. Timing: `0 < w ≤ s < t ≤ K`. -/
def RoutedReadback (K : ℕ) (R : RootedRealization V H) : Prop :=
  ∃ (a b : V) (w s t : ℕ) (x : V),
    a ≠ b ∧ 0 < w ∧ w ≤ s ∧ s < t ∧ t ≤ K
    ∧ (∃ h : H, 0 < R.prior h ∧ ((⇑R.step)^[w] (a, h)).2 ≠ ((⇑R.step)^[w] (b, h)).2)
    ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x
    ∧ rootedPosterior R a s x ≠ rootedPosterior R b s x
    ∧ marg (rootedPosterior R a s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
        ≠ marg (rootedPosterior R b s x) (fun h => ((⇑R.step)^[t - s] (x, h)).1)
    ∧ rootedMap R t a ≠ rootedMap R t b

/-- **`RD0-b`, MONOTONICITY IN THE WINDOW.** A routed witness within a window is a routed witness
within any longer one. -/
theorem routedReadback_mono {K K' : ℕ} {R : RootedRealization V H} (h : RoutedReadback K R)
    (hK : K ≤ K') : RoutedReadback K' R := by
  obtain ⟨a, b, w, s, t, x, hab, hw, hws, hst, htK, rest⟩ := h
  exact ⟨a, b, w, s, t, x, hab, hw, hws, hst, htK.trans hK, rest⟩

/-- **`RD0-c`, THE STORE CLAUSE IS AN OVERLAP.** A routed witness exposes two distinct roots, a
storage time strictly inside the window, and one visible value carrying positive probability under
both — exactly the hypothesis shape `RecurrenceHorizon.horizon_verdict` consumes. -/
theorem routedReadback_overlap {K : ℕ} {R : RootedRealization V H} (h : RoutedReadback K R) :
    ∃ (a b : V) (s : ℕ) (x : V),
      a ≠ b ∧ s < K ∧ 0 < rootedMap R s a x ∧ 0 < rootedMap R s b x := by
  obtain ⟨a, b, w, s, t, x, hab, -, -, hst, htK, -, hsa, hsb, -, -, -⟩ := h
  exact ⟨a, b, s, x, hab, lt_of_lt_of_le hst htK, hsa, hsb⟩

end Predicate

/-! ### `RD4` — what a discharge would buy: indivisibility at the return horizon

The scope remark travels with the statements verbatim: nothing is claimed below the return
horizon, and the discovery round's same-window negative stands. -/

section Return

variable {V H : Type*} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-- **`RD4-a`.** A routed witness binds its own storage time `s`, strictly inside the window, and
every identity return of the rooted map strictly after `s` carries the recurrence-horizon
conclusion. `RecurrenceHorizon.horizon_verdict` is reused and not reproved. Nothing is claimed for
any horizon below the return. -/
theorem routed_forces_return_indivisibility {K : ℕ} {R : RootedRealization V H}
    (h : RoutedReadback K R) :
    ∃ s, s < K ∧ ∀ n, s < n → rootedMap R n = 1 →
      C4r n (rootedMap R) ∧ PIndivisibleWithin n (rootedMap R) := by
  obtain ⟨a, b, s, x, hab, hsK, hsa, hsb⟩ := routedReadback_overlap h
  exact ⟨s, hsK, fun n hsn hI =>
    horizon_verdict hsn (rootedMap_isRowStochastic R s) hI hab hsa hsb⟩

/-- **`RD4-b`.** Finite reversibility supplies a visible period and root time is the identity, so
some multiple of the period is an identity return beyond the storage time: a routed witness forces
P-indivisibility somewhere in the full recurrence cycle. This is `[Main]` §2.3's theorem at the
rooted interface with the routed form as hypothesis; its scope remark is the statement's own — the
horizon reached is the return, not the accessible window. -/
theorem routed_forces_indivisible_somewhere {K : ℕ} {R : RootedRealization V H}
    (h : RoutedReadback K R) : ∃ n, PIndivisibleWithin n (rootedMap R) := by
  obtain ⟨s, -, hcon⟩ := routed_forces_return_indivisibility h
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

/-! ### `RD1` — the kernel's own C1–C4 core, on the rooted interface

The sealed core of `IndependenceCensus` has states `((v, h), b)`, visible `(v, b)`, hidden `h`, and
the passive step `swapFn ((v, h), b) = ((h, v), b)`. Transported along the explicit partition
`OIRealization.partIdx` this is a `RootedRealization (Bool × Bool) Bool` with
`step ((v, b), h) = ((h, b), v)` and the uniform prior `1/2`; the carrier is a **bound variable**
pinned by those two equations, not a definition.

On this carrier the manuscript's history-level condition (`IndependenceCensus.core_history_readback`,
bundled in `CoreC1C4`), the exact marginal-revival form `C4e 2` and `PIndivisibleWithin 2` all hold.
That is a fact about one carrier and licenses nothing about the general relation of the forms. -/

section Core

variable (R : RootedRealization (Bool × Bool) Bool)
  (hstep : ∀ v b h : Bool, R.step ((v, b), h) = ((h, b), v))
  (hprior : ∀ h : Bool, R.prior h = 1 / 2)

/-- The carrier of `RD1` exists: the two equations that pin it are satisfiable. -/
theorem core_realization_exists :
    ∃ R : RootedRealization (Bool × Bool) Bool,
      (∀ v b h : Bool, R.step ((v, b), h) = ((h, b), v)) ∧ ∀ h : Bool, R.prior h = 1 / 2 := by
  have hinv : Function.Involutive
      (fun p : (Bool × Bool) × Bool => ((p.2, p.1.2), p.1.1)) := fun _ => rfl
  refine ⟨{ step := hinv.toPerm
            prior := fun _ => 1 / 2
            prior_nonneg := fun _ => by norm_num
            prior_sum := by rw [Fintype.sum_bool]; norm_num }, fun _ _ _ => rfl, fun _ => rfl⟩

include hstep in
/-- The core's rooted step is an involution. -/
theorem core_involutive : Function.Involutive (⇑R.step) := by
  rintro ⟨⟨v, b⟩, h⟩
  rw [hstep, hstep]

include hstep hprior in
/-- At even times the core's rooted map is the identity: the visible state returns to its root. -/
theorem core_rootedMap_even {s : ℕ} (hs : Even s) (a x : Bool × Bool) :
    rootedMap R s a x = if a = x then 1 else 0 := by
  simp only [rootedMap, (core_involutive R hstep).iterate_even hs, id_eq, hprior,
    Fintype.sum_bool]
  split <;> norm_num

include hstep hprior in
/-- At odd times the core's rooted visible value is `(seed, root's control bit)`: the row is
uniform on the two seeds and supported exactly where the control bit agrees. -/
theorem core_rootedMap_odd {s : ℕ} (hs : Odd s) (a x : Bool × Bool) :
    rootedMap R s a x = if a.2 = x.2 then 1 / 2 else 0 := by
  obtain ⟨v, b⟩ := a
  obtain ⟨y, c⟩ := x
  simp only [rootedMap, (core_involutive R hstep).iterate_odd hs, hstep, hprior,
    Fintype.sum_bool]
  cases b <;> cases c <;> cases y <;> norm_num

include hstep hprior in
/-- At an odd storage time the root-conditioned **seed** weight is the point mass at the observed
seed, whatever the root: it carries no information about the root at all. -/
theorem core_posterior_odd {s : ℕ} (hs : Odd s) (a x : Bool × Bool) (ha : a.2 = x.2) :
    rootedPosterior R a s x = fun h => if h = x.1 then (1 : ℝ) else 0 := by
  have hden : rootedMap R s a x = 1 / 2 := by
    rw [core_rootedMap_odd R hstep hprior hs, if_pos ha]
  obtain ⟨v, b⟩ := a
  obtain ⟨y, c⟩ := x
  simp only at ha
  subst ha
  funext h
  simp only [rootedPosterior, hden, (core_involutive R hstep).iterate_odd hs, hstep, hprior,
    Prod.mk.injEq, and_true]
  rcases eq_or_ne h y with rfl | hne
  · simp
  · simp [hne]

include hstep hprior in
/-- **`RD1-a`, THE RECORDED DISCREPANCY, AS A COMPUTED CERTIFICATE.** On the sealed core at the
storage surface `s = 1`: the write clause holds for every seed, both roots reach the visible value
`x = (false, false)` with positive probability, **and the frozen root-conditioned seed weights
coincide**. The hidden states at that surface are the two roots' own visible bits and separate them;
the seeds do not. This locates the divergence between the freeze's Lean spelling of
`rootedPosterior` and the discovery round's clause S, and nothing more. -/
theorem core_store_gap :
    (∀ h : Bool, 0 < R.prior h
        ∧ ((⇑R.step)^[1] (((false, false) : Bool × Bool), h)).2
            ≠ ((⇑R.step)^[1] (((true, false) : Bool × Bool), h)).2)
      ∧ 0 < rootedMap R 1 ((false, false) : Bool × Bool) ((false, false) : Bool × Bool)
      ∧ 0 < rootedMap R 1 ((true, false) : Bool × Bool) ((false, false) : Bool × Bool)
      ∧ rootedPosterior R ((false, false) : Bool × Bool) 1 ((false, false) : Bool × Bool)
          = rootedPosterior R ((true, false) : Bool × Bool) 1 ((false, false) : Bool × Bool) := by
  have hodd : Odd 1 := ⟨0, by norm_num⟩
  refine ⟨fun h => ⟨by rw [hprior]; norm_num, ?_⟩, ?_, ?_, ?_⟩
  · rw [Function.iterate_one, hstep, hstep]
    simp
  · rw [core_rootedMap_odd R hstep hprior hodd]
    norm_num
  · rw [core_rootedMap_odd R hstep hprior hodd]
    norm_num
  · rw [core_posterior_odd R hstep hprior hodd ((false, false) : Bool × Bool)
      ((false, false) : Bool × Bool) rfl,
      core_posterior_odd R hstep hprior hodd ((true, false) : Bool × Bool)
      ((false, false) : Bool × Bool) rfl]

include hstep hprior in
/-- **`RD1-a`, THE OUTCOME.** Under the frozen spelling the sealed core carries **no** routed
witness at any window: at even storage times both roots are pinned to their own visible value, and
at odd storage times the root-conditioned seed weights coincide, so the store clause fails
everywhere. The negative is a computed certificate, not a failed search. -/
theorem core_not_routedReadback (K : ℕ) : ¬ RoutedReadback K R := by
  rintro ⟨a, b, w, s, t, x, hab, -, -, -, -, -, hsa, hsb, hpost, -, -⟩
  rcases Nat.even_or_odd s with he | ho
  · rw [core_rootedMap_even R hstep hprior he] at hsa hsb
    have ha : a = x := by
      by_contra hc
      rw [if_neg hc] at hsa
      exact lt_irrefl (0 : ℝ) hsa
    have hb : b = x := by
      by_contra hc
      rw [if_neg hc] at hsb
      exact lt_irrefl (0 : ℝ) hsb
    exact hab (ha.trans hb.symm)
  · apply hpost
    rw [core_rootedMap_odd R hstep hprior ho] at hsa hsb
    have ha : a.2 = x.2 := by
      by_contra hc
      rw [if_neg hc] at hsa
      exact lt_irrefl (0 : ℝ) hsa
    have hb : b.2 = x.2 := by
      by_contra hc
      rw [if_neg hc] at hsb
      exact lt_irrefl (0 : ℝ) hsb
    rw [core_posterior_odd R hstep hprior ho a x ha, core_posterior_odd R hstep hprior ho b x hb]

include hstep hprior in
/-- **`RD1-b`.** The core's rooted rows collide at time `1` and separate at the return `2`, so the
exact marginal-revival form holds within `2` and the merged no-go gives P-indivisibility there.
This is a fact about one carrier. -/
theorem core_c4e_two : C4e 2 (rootedMap R) := by
  have hodd : Odd 1 := ⟨0, by norm_num⟩
  have heven : Even 2 := ⟨1, by norm_num⟩
  refine ⟨(false, false), (true, false), 1, 2, by decide, by norm_num, le_rfl, ?_, ?_⟩
  · funext j
    rw [core_rootedMap_odd R hstep hprior hodd, core_rootedMap_odd R hstep hprior hodd]
  · intro hc
    have := congrFun hc ((false, false) : Bool × Bool)
    rw [core_rootedMap_even R hstep hprior heven,
      core_rootedMap_even R hstep hprior heven] at this
    norm_num at this

include hstep hprior in
/-- **`RD1-b`, the endpoint.** -/
theorem core_pIndivisible_two : PIndivisibleWithin 2 (rootedMap R) :=
  c4e_implies_pIndivisible 2 (rootedMap R) (core_c4e_two R hstep hprior)

end Core

/-! ### `RD2` — recurrence without a write is not readback

The uncoupled product of `partition_coupling_probe.py`: `V = ZMod 3`, `H = ZMod 4`,
`step (v, h) = (v + 1, h + 1)`, uniform prior `1/4`. The carrier is a bound variable pinned by
those equations. Here there is not even coupling, and the return is exact. -/

section Product

variable (R : RootedRealization (ZMod 3) (ZMod 4))
  (hstep : ∀ (v : ZMod 3) (h : ZMod 4), R.step (v, h) = (v + 1, h + 1))
  (hprior : ∀ h : ZMod 4, R.prior h = 1 / 4)

/-- The carrier of `RD2` exists. -/
theorem product_realization_exists :
    ∃ R : RootedRealization (ZMod 3) (ZMod 4),
      (∀ (v : ZMod 3) (h : ZMod 4), R.step (v, h) = (v + 1, h + 1))
        ∧ ∀ h : ZMod 4, R.prior h = 1 / 4 := by
  refine ⟨{ step := Equiv.addRight ((1, 1) : ZMod 3 × ZMod 4)
            prior := fun _ => 1 / 4
            prior_nonneg := fun _ => by norm_num
            prior_sum := by rw [Finset.sum_const, Finset.card_univ]; norm_num [ZMod.card] },
          fun _ _ => rfl, fun _ => rfl⟩

include hstep in
/-- Both components advance by the step count, independently of each other. -/
theorem product_iterate (n : ℕ) (v : ZMod 3) (h : ZMod 4) :
    (⇑R.step)^[n] (v, h) = (v + (n : ZMod 3), h + (n : ZMod 4)) := by
  induction n with
  | zero => simp
  | succ m ih =>
    rw [Function.iterate_succ_apply', ih, hstep]
    simp only [Prod.mk.injEq]
    constructor <;> push_cast <;> ring

include hstep in
/-- The rooted map is the permutation matrix of `v ↦ v + t`. -/
theorem product_rootedMap (t : ℕ) :
    rootedMap R t = fun a j => if a + (t : ZMod 3) = j then (1 : ℝ) else 0 := by
  funext a j
  simp only [rootedMap, product_iterate R hstep]
  by_cases hP : a + (t : ZMod 3) = j <;> simp [hP, R.prior_sum]

include hstep in
/-- **`RD2-a`.** The write clause fails at **every** `w`: the hidden component after `w` steps is
the seed advanced by `w` under both roots, so no routed witness exists at any window. Recurrence —
even an exact return of the rooted map to the identity — is not a routed readback. -/
theorem product_not_routedReadback (K : ℕ) : ¬ RoutedReadback K R := by
  rintro ⟨a, b, w, s, t, x, -, -, -, -, -, ⟨h, -, hne⟩, -, -, -, -, -⟩
  rw [product_iterate R hstep, product_iterate R hstep] at hne
  exact hne rfl

include hstep in
/-- **`RD2-b`, the return.** The rooted map returns exactly to the identity at `12`. -/
theorem product_rootedMap_twelve : rootedMap R 12 = 1 := by
  have h12 : ((12 : ℕ) : ZMod 3) = 0 := by decide
  ext a j
  simp only [product_rootedMap R hstep 12, Matrix.one_apply, h12, add_zero]

include hstep in
/-- **`RD2-b`, divisibility.** The rooted family is P-divisible at **every** window: each later map
factors through each earlier one by the permutation propagator of the elapsed time. -/
theorem product_pDivisible (K : ℕ) : PDivisible K (rootedMap R) := by
  intro s t hst _
  have hts : s + (t - s) = t := Nat.add_sub_cancel' hst.le
  have hcast : ((s : ℕ) : ZMod 3) + (((t - s : ℕ)) : ZMod 3) = ((t : ℕ) : ZMod 3) := by
    rw [← Nat.cast_add, hts]
  refine ⟨Matrix.of fun i j => if i + ((t - s : ℕ) : ZMod 3) = j then (1 : ℝ) else 0,
    ⟨fun i j => ?_, fun i => ?_⟩, ?_⟩
  · simp only [Matrix.of_apply]
    split <;> norm_num
  · simp only [Matrix.of_apply]
    rw [Finset.sum_ite_eq]
    simp
  · ext a j
    rw [Matrix.mul_apply]
    simp only [Matrix.of_apply, product_rootedMap R hstep, ite_mul, one_mul, zero_mul,
      Finset.sum_ite_eq, Finset.mem_univ, if_true, add_assoc, hcast]

end Product

/-! ### `RD3` — write and store without in-window routing

The tape-and-ledger coin of `[Main]` §2.3's separation remark, on the carrier that exhibits it:
`V = Bool`, `H = Bool × Bool × Bool` (tape₁, tape₂, ledger),
`step (x, (τ₁, τ₂, ℓ)) = (x ⊕ τ₁, (τ₂, τ₁, ℓ ⊕ x))`, a bijection of the sixteen states, prior
`1/4` on a blank ledger and `0` otherwise. The carrier is a bound variable pinned by those
equations.

There is coupling, a write, a store, and history-level memory within the window — and no routed
readback within `K = 3`, the visible law being P-divisible there, while the routed form and
P-indivisibility both appear at the return `t = 4`. This is `[Main]` §2.3's "influence plus storage
plus capacity, without readback, is noise", on one sixteen-state object. It says nothing about
either physical cut, and it does not say the history-level condition and the routed form are
incomparable in general: the discovery round's T1 stands and `RD3` is the converse's failure on one
carrier. -/

section TapeLedger

variable (R : RootedRealization Bool (Bool × Bool × Bool))
  (hstep : ∀ x t₁ t₂ l : Bool, R.step (x, (t₁, t₂, l)) = (xor x t₁, (t₂, t₁, xor l x)))
  (hprior : ∀ t₁ t₂ l : Bool, R.prior (t₁, t₂, l) = if l then 0 else 1 / 4)

/-- The carrier of `RD3` exists: the sixteen-state update is a bijection and the declared prior is
nonnegative and normalized. -/
theorem tapeLedger_realization_exists :
    ∃ R : RootedRealization Bool (Bool × Bool × Bool),
      (∀ x t₁ t₂ l : Bool, R.step (x, (t₁, t₂, l)) = (xor x t₁, (t₂, t₁, xor l x)))
        ∧ ∀ t₁ t₂ l : Bool, R.prior (t₁, t₂, l) = if l then 0 else 1 / 4 := by
  refine ⟨{ step :=
              { toFun := fun p => (xor p.1 p.2.1, (p.2.2.1, p.2.1, xor p.2.2.2 p.1))
                invFun := fun p => (xor p.1 p.2.2.1,
                  (p.2.2.1, p.2.1, xor (xor p.2.2.2 p.1) p.2.2.1))
                left_inv := by decide
                right_inv := by decide }
            prior := fun h => if h.2.2 then 0 else 1 / 4
            prior_nonneg := fun h => by
              show (0 : ℝ) ≤ if h.2.2 then 0 else 1 / 4
              split <;> norm_num
            prior_sum := by
              simp only [Fintype.sum_prod_type, Fintype.sum_bool]
              norm_num },
          fun _ _ _ _ => rfl, fun _ _ _ => rfl⟩

include hstep in
/-- The rooted step, as a function on the sixteen states. -/
theorem tapeLedger_step_eq :
    (⇑R.step) = fun p : Bool × Bool × Bool × Bool =>
      (xor p.1 p.2.1, (p.2.2.1, p.2.1, xor p.2.2.2 p.1)) := by
  funext p
  obtain ⟨x, t₁, t₂, l⟩ := p
  exact hstep x t₁ t₂ l

include hstep hprior in
/-- The rooted map is uniform at times `1`, `2` and `3`: the visible law forgets the root on the
whole window. -/
theorem tapeLedger_rootedMap_mid (t : ℕ) (h1 : 1 ≤ t) (h3 : t ≤ 3) :
    rootedMap R t = fun _ _ => (1 : ℝ) / 2 := by
  have hs := tapeLedger_step_eq R hstep
  interval_cases t <;>
    · funext a j
      cases a <;> cases j <;>
        simp only [rootedMap, hs, Function.iterate_succ_apply, Function.iterate_zero_apply,
          hprior, Fintype.sum_prod_type, Fintype.sum_bool] <;>
        norm_num

include hstep hprior in
/-- The rooted map returns exactly to the identity at `4`. -/
theorem tapeLedger_rootedMap_four : rootedMap R 4 = 1 := by
  have hs := tapeLedger_step_eq R hstep
  funext a j
  cases a <;> cases j <;>
    simp only [rootedMap, hs, Function.iterate_succ_apply, Function.iterate_zero_apply, hprior,
      Fintype.sum_prod_type, Fintype.sum_bool, Matrix.one_apply] <;>
    norm_num

include hstep hprior in
/-- **`RD3-a`.** The write clause holds at `w = 1` and the store clause at `s = 1`: the ledger takes
the root after one step, and the root-conditioned weights at a common visible value have disjoint
supports. The two conjuncts are proved separately, so the failure below is located at the read
clause and nowhere else. -/
theorem tapeLedger_write_store :
    (∃ h : Bool × Bool × Bool, 0 < R.prior h
        ∧ ((⇑R.step)^[1] (false, h)).2 ≠ ((⇑R.step)^[1] (true, h)).2)
      ∧ 0 < rootedMap R 1 false false ∧ 0 < rootedMap R 1 true false
      ∧ rootedPosterior R false 1 false ≠ rootedPosterior R true 1 false := by
  have hs := tapeLedger_step_eq R hstep
  have hmid := tapeLedger_rootedMap_mid R hstep hprior 1 le_rfl (by norm_num)
  refine ⟨⟨(false, false, false), by rw [hprior]; norm_num, ?_⟩, ?_, ?_, ?_⟩
  · simp [hs]
  · rw [hmid]; norm_num
  · rw [hmid]; norm_num
  · intro hc
    have h0 := congrFun hc (false, false, false)
    simp only [rootedPosterior, hs, Function.iterate_succ_apply, Function.iterate_zero_apply,
      hmid, hprior] at h0
    norm_num at h0

include hstep hprior in
/-- **`RD3-b`.** There is **no** routed witness within `K = 3`, at full strength and by a computed
certificate rather than a search: the rooted rows coincide at every time the window admits for the
read, so the rooted-reappearance clause `R(2)` cannot hold there. -/
theorem tapeLedger_not_routedReadback_three : ¬ RoutedReadback 3 R := by
  rintro ⟨a, b, w, s, t, x, -, hw, hws, hst, ht3, -, -, -, -, -, hrows⟩
  apply hrows
  have h1t : 1 ≤ t := le_trans hw (le_trans hws hst.le)
  rw [tapeLedger_rootedMap_mid R hstep hprior t h1t ht3]

include hstep hprior in
/-- **`RD3-c`.** The visible law is P-divisible within `3`: out of the root by the rooted map
itself, and between any two later times by the identity, the rooted maps there being equal. -/
theorem tapeLedger_pDivisible_three : PDivisible 3 (rootedMap R) := by
  intro s t hst ht3
  rcases Nat.eq_zero_or_pos s with rfl | hs
  · refine ⟨rootedMap R t, rootedMap_isRowStochastic R t, ?_⟩
    rw [rootedMap_zero R, one_mul]
  · refine ⟨1, one_isRowStochastic, ?_⟩
    rw [mul_one, tapeLedger_rootedMap_mid R hstep hprior t (le_trans hs hst.le) ht3,
      tapeLedger_rootedMap_mid R hstep hprior s hs (le_trans hst.le ht3)]

include hstep in
/-- **`RD3-d`, THE HISTORY IDENTITY.** On the prior's support the visible values obey
`X₃ = x ⊕ X₁ ⊕ X₂`: the update's own identity, stated as an identity about the update. No
history-level predicate is defined for it. -/
theorem tapeLedger_history_identity (x : Bool) (h : Bool × Bool × Bool) (hpos : 0 < R.prior h) :
    ((⇑R.step)^[3] (x, h)).1
      = xor (xor x ((⇑R.step)^[1] (x, h)).1) ((⇑R.step)^[2] (x, h)).1 := by
  have hs := tapeLedger_step_eq R hstep
  obtain ⟨t₁, t₂, l⟩ := h
  cases x <;> cases t₁ <;> cases t₂ <;> cases l <;> simp [hs]

include hstep hprior in
/-- **`RD3-e`.** At the return the routed form holds: a witness with `(w, s, t) = (1, 2, 4)` — the
write at one step, the store at the second, and the read at the return — together with the exact
marginal-revival form at `4`, hence P-indivisibility there.

The witness tuple differs from the control plane's recorded scratch tuple `(1, 1, 4)`: under the
frozen spelling of `rootedPosterior` the storage surface that carries the read is `s = 2`. The
statement proved is the frozen one. -/
theorem tapeLedger_routedReadback_four : RoutedReadback 4 R := by
  have hs := tapeLedger_step_eq R hstep
  have hmid2 := tapeLedger_rootedMap_mid R hstep hprior 2 (by norm_num) (by norm_num)
  have h4 := tapeLedger_rootedMap_four R hstep hprior
  refine ⟨false, true, 1, 2, 4, false, by decide, by norm_num, by norm_num, by norm_num,
    le_rfl, ⟨(false, false, false), by rw [hprior]; norm_num, ?_⟩, ?_, ?_, ?_, ?_, ?_⟩
  · simp [hs]
  · rw [hmid2]; norm_num
  · rw [hmid2]; norm_num
  · intro hc
    have h0 := congrFun hc (false, false, false)
    simp only [rootedPosterior, hs, Function.iterate_succ_apply, Function.iterate_zero_apply,
      hmid2, hprior] at h0
    norm_num at h0
  · intro hc
    have h0 := congrFun hc false
    simp only [marg, rootedPosterior, hs, Function.iterate_succ_apply,
      Function.iterate_zero_apply, hmid2, hprior, Finset.sum_filter, Fintype.sum_prod_type,
      Fintype.sum_bool] at h0
    norm_num at h0
  · intro hc
    have h0 := congrFun hc false
    rw [h4] at h0
    simp only [Matrix.one_apply] at h0
    norm_num at h0

include hstep hprior in
/-- **`RD3-e`, the marginal form and the endpoint at the return.** -/
theorem tapeLedger_c4e_four : C4e 4 (rootedMap R) := by
  have hmid := tapeLedger_rootedMap_mid R hstep hprior 1 le_rfl (by norm_num)
  have h4 := tapeLedger_rootedMap_four R hstep hprior
  refine ⟨false, true, 1, 4, by decide, by norm_num, le_rfl, ?_, ?_⟩
  · rw [hmid]
  · intro hc
    have h0 := congrFun (congrFun h4 false) false
    have h1 := congrFun (congrFun h4 true) false
    rw [congrFun hc false] at h0
    rw [h1] at h0
    simp only [Matrix.one_apply] at h0
    norm_num at h0

include hstep hprior in
/-- **`RD3-e`, P-indivisibility at the return.** -/
theorem tapeLedger_pIndivisible_four : PIndivisibleWithin 4 (rootedMap R) :=
  c4e_implies_pIndivisible 4 (rootedMap R) (tapeLedger_c4e_four R hstep hprior)

end TapeLedger

/-! ### `RD5` — the lattice cut's realization datum, and its residual as a named predicate

What the kernel supplies of the lattice datum, and what it does not. `φ` is `waveSubstratum`'s.
`Vs` is a **parameter**: `[SM]` Theorem 22 quantifies over connected regions with `|V| ≤ N/3`, and
connectedness is not formalized here. `μ` is the manuscript's Lemma 3 selection (uniform), which the
architecture does **not** determine by invariance — `StochasticInterface`'s
`waveSubstratum_ensemble_underdetermined` and `waveSubstratum_stochastic_interface_gap` are
consumed and neither is weakened, and the prior is quantified over so a later round may test
another. `K` is the stationarity window `τ_return(Vs)` of `[SM]`'s validity-window remark, which the
kernel does not define and this round does not define either.

**The lattice residual, named and not proved here:** for every connected region `Vs` with
`|Vs| ≤ N/3`, `LatticeCutReadback d L q α Vs (uniform) (τ_return Vs)`, for the manuscript instance
`α = 1`, `d = 3`, and every `L`, `q` in scope. That is Theorem 22's readback genericity lemma in the
exact form the kernel could receive it. -/

section Cut

variable (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]

/-- **`RD5-a`.** A substratum's rooted realization for a visible region and a hidden prior: the
visible carrier is the region's phase-space data, the hidden carrier the complement's, and the step
is `𝒮.φ` transported along the split of `𝒮.Conf` into region and complement. Nothing is added to
the substratum. -/
noncomputable def cutRealization (Vs : Finset 𝒮.ι)
    (μ : ({i // i ∉ Vs} → 𝒮.V × 𝒮.V) → ℝ) (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) :
    RootedRealization ({i // i ∈ Vs} → 𝒮.V × 𝒮.V) ({i // i ∉ Vs} → 𝒮.V × 𝒮.V) where
  step :=
    (Equiv.piEquivPiSubtypeProd (fun i => i ∈ Vs) (fun _ => 𝒮.V × 𝒮.V)).symm.trans
      (𝒮.φ.trans (Equiv.piEquivPiSubtypeProd (fun i => i ∈ Vs) (fun _ => 𝒮.V × 𝒮.V)))
  prior := μ
  prior_nonneg := hμ0
  prior_sum := hμ1

/-- **`RD5-a`, THE PINNING LEMMA.** For every configuration the transported step agrees with `𝒮.φ`
under the split: the cut realization adds no dynamics of its own. -/
theorem cutRealization_step (Vs : Finset 𝒮.ι)
    (μ : ({i // i ∉ Vs} → 𝒮.V × 𝒮.V) → ℝ) (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1)
    (c : 𝒮.Conf) :
    (cutRealization 𝒮 Vs μ hμ0 hμ1).step
        (Equiv.piEquivPiSubtypeProd (fun i => i ∈ Vs) (fun _ => 𝒮.V × 𝒮.V) c)
      = Equiv.piEquivPiSubtypeProd (fun i => i ∈ Vs) (fun _ => 𝒮.V × 𝒮.V) (𝒮.φ c) := by
  simp only [cutRealization, Equiv.trans_apply, Equiv.symm_apply_apply]

/-- **`RD5-c`.** Every cut realization's rooted maps are row-stochastic, consuming
`rootedMap_isRowStochastic` unmodified. -/
theorem cutRealization_rootedMap_isRowStochastic (Vs : Finset 𝒮.ι)
    (μ : ({i // i ∉ Vs} → 𝒮.V × 𝒮.V) → ℝ) (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) (t : ℕ) :
    IsRowStochastic (rootedMap (cutRealization 𝒮 Vs μ hμ0 hμ1) t) :=
  rootedMap_isRowStochastic _ t

/-- **`RD5-c`.** Every cut realization has a finite visible period, consuming `rootedMap_periodic`
unmodified — so `RD4` applies to the lattice datum verbatim. -/
theorem cutRealization_rootedMap_periodic (Vs : Finset 𝒮.ι)
    (μ : ({i // i ∉ Vs} → 𝒮.V × 𝒮.V) → ℝ) (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) :
    PeriodicFamily (fun t => rootedMap (cutRealization 𝒮 Vs μ hμ0 hμ1) t) :=
  rootedMap_periodic _

end Cut

section Lattice

variable (d L q : ℕ) [NeZero L] [NeZero q]

variable (α : ZMod q) [Fintype (waveSubstratum d L q α).ι] [Fintype (waveSubstratum d L q α).V]
  [DecidableEq (waveSubstratum d L q α).V]

set_option maxHeartbeats 1000000

/-- **`RD5-b`, THE LATTICE CUT'S RESIDUAL AS A NAMED PREDICATE.** `[SM]` Theorem 22's fourth
clause — history readback, "the record surviving to a readback the coupling performs" — on exactly
the data the manuscripts leave as parameters: the region, the prior and the window. This is the
manuscripts' own hypothesis named, not a new condition. The three instance arguments are the wave
substratum's own, `Fin d → ZMod L` and `ZMod q`; they are carried explicitly because the
substratum's carriers are projections of a structure and are not found by instance search. -/
def LatticeCutReadback (Vs : Finset (waveSubstratum d L q α).ι)
    (μ : ({i // i ∉ Vs} → (waveSubstratum d L q α).V × (waveSubstratum d L q α).V) → ℝ)
    (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) (K : ℕ) : Prop :=
  RoutedReadback K (cutRealization (waveSubstratum d L q α) Vs μ hμ0 hμ1)

/-- **`RD5-b`, pinned.** The named residual is exactly routed readback of the cut realization of
the wave substratum: the abbreviation adds nothing beyond the name. -/
theorem latticeCutReadback_iff (Vs : Finset (waveSubstratum d L q α).ι)
    (μ : ({i // i ∉ Vs} → (waveSubstratum d L q α).V × (waveSubstratum d L q α).V) → ℝ)
    (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) (K : ℕ) :
    LatticeCutReadback d L q α Vs μ hμ0 hμ1 K
      ↔ RoutedReadback K (cutRealization (waveSubstratum d L q α) Vs μ hμ0 hμ1) :=
  Iff.rfl

/-- **`RD5-c` at the lattice cut.** The lattice cut realization's rooted maps are row-stochastic
and its visible law is periodic, so `RD4`'s return-horizon consequence applies to it verbatim —
which is a statement about the abstract datum and about no physical cut. -/
theorem latticeCut_rootedMap_stochastic_periodic (Vs : Finset (waveSubstratum d L q α).ι)
    (μ : ({i // i ∉ Vs} → (waveSubstratum d L q α).V × (waveSubstratum d L q α).V) → ℝ)
    (hμ0 : ∀ h, 0 ≤ μ h) (hμ1 : ∑ h, μ h = 1) :
    (∀ t, IsRowStochastic
        (rootedMap (cutRealization (waveSubstratum d L q α) Vs μ hμ0 hμ1) t))
      ∧ PeriodicFamily
        (fun t => rootedMap (cutRealization (waveSubstratum d L q α) Vs μ hμ0 hμ1) t) :=
  ⟨fun t => cutRealization_rootedMap_isRowStochastic _ Vs μ hμ0 hμ1 t,
    cutRealization_rootedMap_periodic _ Vs μ hμ0 hμ1⟩

end Lattice

end PhysicalC4Discharge
end OIBridge

#print axioms OIBridge.PhysicalC4Discharge.routedReadback_mono
#print axioms OIBridge.PhysicalC4Discharge.routedReadback_overlap
#print axioms OIBridge.PhysicalC4Discharge.routed_forces_return_indivisibility
#print axioms OIBridge.PhysicalC4Discharge.routed_forces_indivisible_somewhere
#print axioms OIBridge.PhysicalC4Discharge.core_realization_exists
#print axioms OIBridge.PhysicalC4Discharge.core_involutive
#print axioms OIBridge.PhysicalC4Discharge.core_rootedMap_even
#print axioms OIBridge.PhysicalC4Discharge.core_rootedMap_odd
#print axioms OIBridge.PhysicalC4Discharge.core_posterior_odd
#print axioms OIBridge.PhysicalC4Discharge.core_store_gap
#print axioms OIBridge.PhysicalC4Discharge.core_not_routedReadback
#print axioms OIBridge.PhysicalC4Discharge.core_c4e_two
#print axioms OIBridge.PhysicalC4Discharge.core_pIndivisible_two
#print axioms OIBridge.PhysicalC4Discharge.product_realization_exists
#print axioms OIBridge.PhysicalC4Discharge.product_iterate
#print axioms OIBridge.PhysicalC4Discharge.product_rootedMap
#print axioms OIBridge.PhysicalC4Discharge.product_not_routedReadback
#print axioms OIBridge.PhysicalC4Discharge.product_rootedMap_twelve
#print axioms OIBridge.PhysicalC4Discharge.product_pDivisible
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_realization_exists
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_step_eq
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_rootedMap_mid
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_rootedMap_four
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_write_store
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_not_routedReadback_three
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_pDivisible_three
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_history_identity
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_routedReadback_four
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_c4e_four
#print axioms OIBridge.PhysicalC4Discharge.tapeLedger_pIndivisible_four
#print axioms OIBridge.PhysicalC4Discharge.cutRealization_step
#print axioms OIBridge.PhysicalC4Discharge.cutRealization_rootedMap_isRowStochastic
#print axioms OIBridge.PhysicalC4Discharge.cutRealization_rootedMap_periodic
#print axioms OIBridge.PhysicalC4Discharge.latticeCutReadback_iff
#print axioms OIBridge.PhysicalC4Discharge.latticeCut_rootedMap_stochastic_periodic
