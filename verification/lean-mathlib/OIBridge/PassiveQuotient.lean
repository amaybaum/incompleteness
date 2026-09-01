/-
  OIBridge/PassiveQuotient.lean — the canonical passive quotient: the minimal carrier
  of the complete passive observational law, its universal property, and the theorem
  that domain glue earns full G1 on exactly that carrier.

  PHASE THREE, ROUND SIXTEEN. Round fifteen proved the finite-horizon quotient theorem
  span(𝒟_K) = {∼_K-invariants} and classified the residual glue freedom as block-unitary
  freedom inside itinerary fibres. The corpus audit then returned a definite verdict:
  C1–C4 and the ETH/mixing layer CANNOT imply itinerary separation of the raw carrier,
  because the corpus explicitly permits observationally inert hidden-sector enlargement —
  from any carrier, φ̃(s,a) = (φ s, σ_s a) with ṽis(s,a) = vis s preserves the entire
  passive visible law while gluing every hidden fibre. This file records both halves of
  the corrected claim in the kernel:

      ┌───────────────────────────────────────────────────────────────────┐
      │  Bare OI does not make the ontic carrier observable               │
      │  (`hiddenExt_not_separating` + `hiddenExt_same_law`), but the     │
      │  minimal carrier of the complete passive observational law is     │
      │  automatically separating (`quotient_itinerarySeparating`), so    │
      │  domain glue earns full G1 on exactly the state space to which    │
      │  the passive coherent description is operationally accountable   │
      │  (`passiveQuotient_glue_forces_G1`).                              │
      └───────────────────────────────────────────────────────────────────┘

  §A — THE CANONICAL QUOTIENT. `itiSetoid` bundles `itiRelInf` as an equivalence;
  `MinimalCarrier φ vis := S/∼_∞`. The relation is a dynamical congruence in both
  directions because `φ⁻¹` is a power of `φ` (`itiRelInf_pow`, `itiRelInf_symm_evolve`),
  so the dynamics DESCENDS TO A PERMUTATION `quotPerm` and the labelling descends to
  `quotVis`. `itiRelInf_greatest_congruence`: ∼_∞ is the greatest relation that is
  invisible to `vis` and respected by `φ` — any observation-preserving dynamical
  congruence is contained in it. `quotient_itinerarySeparating`: the quotient is
  itinerary-separating by construction.

  §B — MINIMALITY AND UNIQUENESS (the finite deterministic Nerode quotient).
  `passiveMinimal_iff_itinerarySeparating`: a carrier admits no nontrivial
  observation-preserving congruence exactly when it is itinerary-separating — "minimal"
  means no quotient preserves the complete passive visible history, not minimal ontic
  reality. `minimal_realization_bijective` + `realizationMap_equivariant` +
  `realizationMap_vis` + `realization_factor_unique`: every separating realization
  reached by an intertwining surjection is canonically isomorphic to the quotient, and
  the factorization is unique — S/∼_∞ is THE minimal deterministic realization of the
  labelled passive dynamics.

  §C — LAW PRESERVATION. Pushing a preparation forward along the quotient
  (`quotMeasure`) preserves every finite visible trajectory probability
  (`trajProb_quotient`) and commutes with the two branch-domain operations
  (`quotMeasure_evolve`, `quotMeasure_branch`): the full closed multi-time passive law
  is unchanged. Hence the capstone, with no separation hypothesis left:

      ┌───────────────────────────────────────────────────────────────────┐
      │  On the canonical minimal passive carrier,  G_𝒟  ⟹  G1           │
      │  (`passiveQuotient_glue_forces_G1`, `…_forces_monomial`), and     │
      │  with an ergodic shell, physical-flow SRC with canonical B        │
      │  (`ergodicShell_SRC_of_passiveQuotient`).                         │
      └───────────────────────────────────────────────────────────────────┘

  §D — THE MANDATORY NEGATIVE CONTROL. `hiddenExt φ σ` attaches a hidden fibre with
  arbitrary per-state fibre dynamics. It glues every fibre (`hiddenExt_itiRelInf_fibre`),
  destroys separation whenever the fibre is nontrivial (`hiddenExt_not_separating`), and
  preserves the entire passive visible law for every prior with the right marginal
  (`hiddenExt_same_law`) — so no passive OI condition can derive raw-carrier separation.
  The quotient strips exactly this fibre: `hiddenExt_quotient_recovers_base`. This
  placement is deliberate and observer-relative: the itinerary quotient lives at the
  observational-equivalence level (Structure's Level G4, Definitions 9.3/9.4), NOT at
  the substratum gauge group G3 — the corpus treats the hidden state as physically
  meaningful, and another partition or an intervention may distinguish microstates that
  the passive quotient glues.

  §E — THE LINEAR OBSERVABILITY BRIDGE. For an additive automorphism `step` read
  through an additive map `read` (the SM reference branch: the mod-q wave equation in
  companion form, current field visible on the observer's sites), itinerary equivalence
  is exactly membership of the difference in the unobservable subgroup
  (`linear_itiRelInf_iff`), and itinerary separation is exactly classical observability
  — trivial kernel of the stacked readout family (`linear_separating_iff_observability`).
  Probe F28 computes those kernels for the actual lattice wave rule.

  WHAT THIS DOES NOT DECIDE. Whether the coherent noncommuting instrument algebra is
  consistent with the passive representation (interventions may separate states the
  passive quotient glues) remains behind this round, as does the concrete SM/GR cut
  beyond the linear reference branch.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ObservabilityQuotient

namespace OIBridge
namespace PassiveQuotient

open Complex Matrix CoherentLift CycleFibreHull DynamicsGlue DomainGlue
  ObservabilityQuotient
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S I : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A — the canonical passive quotient -/

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The itinerary relation is invariant under any forward power of the dynamics. -/
theorem itiRelInf_pow {φ : Equiv.Perm S} {vis : S → I} (m : ℕ) {s t : S}
    (h : itiRelInf φ vis s t) : itiRelInf φ vis ((φ ^ m) s) ((φ ^ m) t) := by
  intro k
  rw [show (φ ^ k) ((φ ^ m) s) = (φ ^ (k + m)) s from by rw [pow_add]; rfl,
    show (φ ^ k) ((φ ^ m) t) = (φ ^ (k + m)) t from by rw [pow_add]; rfl]
  exact h (k + m)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- One forward step of the congruence. -/
theorem itiRelInf_evolve {φ : Equiv.Perm S} {vis : S → I} {s t : S}
    (h : itiRelInf φ vis s t) : itiRelInf φ vis (φ s) (φ t) := by
  have h1 := itiRelInf_pow 1 h
  rwa [pow_one] at h1

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- One backward step: because `φ⁻¹` is a power of `φ` on a finite carrier, the
itinerary relation is a congruence in both directions. -/
theorem itiRelInf_symm_evolve {φ : Equiv.Perm S} {vis : S → I} {s t : S}
    (h : itiRelInf φ vis s t) : itiRelInf φ vis (φ.symm s) (φ.symm t) := by
  have hinv : φ ^ (orderOf φ - 1) = φ⁻¹ := by
    refine eq_inv_of_mul_eq_one_left ?_
    rw [← pow_succ, Nat.sub_add_cancel (orderOf_pos φ), pow_orderOf_eq_one]
  have h1 := itiRelInf_pow (orderOf φ - 1) h
  rwa [hinv, Equiv.Perm.inv_def] at h1

/-- The passive itinerary setoid: `∼_∞` bundled as an equivalence. -/
def itiSetoid (φ : Equiv.Perm S) (vis : S → I) : Setoid S :=
  ⟨itiRelInf φ vis,
    ⟨fun _ _ => rfl, fun h k => (h k).symm, fun h1 h2 k => (h1 k).trans (h2 k)⟩⟩

/-- **THE MINIMAL CARRIER**: the canonical passive quotient `S/∼_∞` — the state space
of the complete passive observational law. -/
abbrev MinimalCarrier (φ : Equiv.Perm S) (vis : S → I) : Type _ :=
  Quotient (itiSetoid φ vis)

instance itiRelKDec (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) (s t : S) :
    Decidable (itiRelK φ vis K s t) :=
  decidable_of_iff (∀ k, k < K → vis ((φ ^ k) s) = vis ((φ ^ k) t)) Iff.rfl

noncomputable instance itiRelInfDec (φ : Equiv.Perm S) (vis : S → I) :
    DecidableRel (itiRelInf φ vis) := fun s t =>
  decidable_of_iff _ (itiRelInf_iff_orderOf φ vis s t).symm

noncomputable instance (φ : Equiv.Perm S) (vis : S → I) :
    DecidableEq (MinimalCarrier φ vis) :=
  fun a b => Quotient.recOnSubsingleton₂ a b fun s t =>
    decidable_of_iff (itiRelInf φ vis s t)
      ⟨fun h => Quotient.sound (s := itiSetoid φ vis) h,
        fun h => Quotient.exact (s := itiSetoid φ vis) h⟩

noncomputable instance (φ : Equiv.Perm S) (vis : S → I) :
    Fintype (MinimalCarrier φ vis) :=
  Fintype.ofSurjective (Quotient.mk (itiSetoid φ vis))
    fun q => Quotient.exists_rep q

instance (φ : Equiv.Perm S) (vis : S → I) [Nonempty S] :
    Nonempty (MinimalCarrier φ vis) :=
  Nonempty.map (Quotient.mk (itiSetoid φ vis)) inferInstance

/-- The labelling descends to the quotient. -/
def quotVis (φ : Equiv.Perm S) (vis : S → I) : MinimalCarrier φ vis → I :=
  Quotient.lift vis fun _ _ h => by
    have h0 := h 0
    rwa [pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply] at h0

/-- **The dynamics descends to a permutation** of the minimal carrier: both the forward
and the backward step respect `∼_∞`. -/
def quotPerm (φ : Equiv.Perm S) (vis : S → I) : Equiv.Perm (MinimalCarrier φ vis) where
  toFun := Quotient.lift (fun s => Quotient.mk (itiSetoid φ vis) (φ s))
    fun _ _ h => Quotient.sound (itiRelInf_evolve h)
  invFun := Quotient.lift (fun s => Quotient.mk (itiSetoid φ vis) (φ.symm s))
    fun _ _ h => Quotient.sound (itiRelInf_symm_evolve h)
  left_inv := fun q => by
    obtain ⟨s⟩ := q
    show Quotient.mk (itiSetoid φ vis) (φ.symm (φ s)) = Quotient.mk (itiSetoid φ vis) s
    rw [Equiv.symm_apply_apply]
  right_inv := fun q => by
    obtain ⟨s⟩ := q
    show Quotient.mk (itiSetoid φ vis) (φ (φ.symm s)) = Quotient.mk (itiSetoid φ vis) s
    rw [Equiv.apply_symm_apply]

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Computation rule for the descended dynamics. -/
theorem quotPerm_mk (φ : Equiv.Perm S) (vis : S → I) (s : S) :
    quotPerm φ vis (Quotient.mk (itiSetoid φ vis) s)
      = Quotient.mk (itiSetoid φ vis) (φ s) := rfl

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Powers of the descended dynamics act as powers of the base dynamics. -/
theorem quotPerm_pow_mk (φ : Equiv.Perm S) (vis : S → I) (k : ℕ) (s : S) :
    (quotPerm φ vis ^ k) (Quotient.mk (itiSetoid φ vis) s)
      = Quotient.mk (itiSetoid φ vis) ((φ ^ k) s) := by
  induction k generalizing s with
  | zero => rw [pow_zero, pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply]
  | succ k ih =>
      rw [pow_succ, pow_succ, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply,
        quotPerm_mk, ih]

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **THE GREATEST-CONGRUENCE THEOREM.** Any relation that is invisible to the labelling
and respected by the dynamics is contained in `∼_∞`: the itinerary relation is the
greatest observation-preserving dynamical congruence. -/
theorem itiRelInf_greatest_congruence {φ : Equiv.Perm S} {vis : S → I}
    (r : S → S → Prop) (hvis : ∀ s t, r s t → vis s = vis t)
    (hdyn : ∀ s t, r s t → r (φ s) (φ t)) :
    ∀ s t, r s t → itiRelInf φ vis s t := by
  intro s t h k
  induction k generalizing s t with
  | zero =>
      rw [pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply]
      exact hvis s t h
  | succ k ih =>
      rw [show (φ ^ (k + 1)) s = (φ ^ k) (φ s) from by
          rw [pow_succ, Equiv.Perm.mul_apply],
        show (φ ^ (k + 1)) t = (φ ^ k) (φ t) from by
          rw [pow_succ, Equiv.Perm.mul_apply]]
      exact ih (φ s) (φ t) (hdyn s t h)

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **THE QUOTIENT IS SEPARATING BY CONSTRUCTION**: distinct classes of the minimal
carrier have distinct visible itineraries. -/
theorem quotient_itinerarySeparating (φ : Equiv.Perm S) (vis : S → I) :
    ItinerarySeparating (quotPerm φ vis) (quotVis φ vis) := by
  intro q1 q2
  refine Quotient.inductionOn₂ q1 q2 fun s t h => ?_
  refine Quotient.sound (s := itiSetoid φ vis) fun k => ?_
  have hk := h k
  rwa [quotPerm_pow_mk, quotPerm_pow_mk] at hk

/-! ### Section B — minimality and uniqueness -/

/-- An observation-preserving dynamical congruence: invisible to the labelling,
respected by the dynamics. -/
def ObservationCongruence (φ : Equiv.Perm S) (vis : S → I) (r : S → S → Prop) : Prop :=
  (∀ s t, r s t → vis s = vis t) ∧ (∀ s t, r s t → r (φ s) (φ t))

/-- **Passive minimality**: no nontrivial quotient preserves the complete passive
visible history — every observation-preserving congruence is trivial. This is
minimality of the REPRESENTATION, not minimal ontic reality. -/
def PassivelyMinimal (φ : Equiv.Perm S) (vis : S → I) : Prop :=
  ∀ r : S → S → Prop, ObservationCongruence φ vis r → ∀ s t, r s t → s = t

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **MINIMALITY IS SEPARATION.** A carrier is passively minimal exactly when its cut
is itinerary-separating. -/
theorem passiveMinimal_iff_itinerarySeparating (φ : Equiv.Perm S) (vis : S → I) :
    PassivelyMinimal φ vis ↔ ItinerarySeparating φ vis := by
  constructor
  · intro hmin s t hst
    refine hmin (itiRelInf φ vis) ⟨fun s t h => ?_, fun _ _ h => itiRelInf_evolve h⟩
      s t hst
    have h0 := h 0
    rwa [pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply] at h0
  · intro hsep r hr s t hrst
    exact hsep s t (itiRelInf_greatest_congruence r hr.1 hr.2 s t hrst)

section Realization

variable {S' : Type*}

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- An intertwining map transports powers of the dynamics. -/
theorem realization_pow {φ : Equiv.Perm S} (φ' : Equiv.Perm S') (π : S → S')
    (hπφ : ∀ s, π (φ s) = φ' (π s)) (k : ℕ) (s : S) :
    π ((φ ^ k) s) = (φ' ^ k) (π s) := by
  induction k generalizing s with
  | zero => rw [pow_zero, pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply]
  | succ k ih =>
      rw [pow_succ, pow_succ, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply,
        ih (φ s), hπφ]

/-- The canonical factorization of a separating realization through the quotient. -/
def realizationMap (φ : Equiv.Perm S) (vis : S → I) (φ' : Equiv.Perm S')
    (vis' : S' → I) (π : S → S') (hπφ : ∀ s, π (φ s) = φ' (π s))
    (hπvis : ∀ s, vis' (π s) = vis s) (hsep' : ItinerarySeparating φ' vis') :
    MinimalCarrier φ vis → S' :=
  Quotient.lift π fun s t h => hsep' (π s) (π t) fun k => by
    rw [← realization_pow φ' π hπφ, ← realization_pow φ' π hπφ, hπvis, hπvis]
    exact h k

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **NERODE UNIQUENESS.** Any itinerary-separating realization reached from the carrier
by an intertwining surjection is canonically isomorphic to the minimal carrier: the
factorization map is a bijection. -/
theorem minimal_realization_bijective (φ : Equiv.Perm S) (vis : S → I)
    (φ' : Equiv.Perm S') (vis' : S' → I) (π : S → S')
    (hπφ : ∀ s, π (φ s) = φ' (π s)) (hπvis : ∀ s, vis' (π s) = vis s)
    (hsep' : ItinerarySeparating φ' vis') (hsurj : Function.Surjective π) :
    Function.Bijective (realizationMap φ vis φ' vis' π hπφ hπvis hsep') := by
  constructor
  · intro q1 q2
    refine Quotient.inductionOn₂ q1 q2 fun s t h => ?_
    refine Quotient.sound (s := itiSetoid φ vis) fun k => ?_
    have hst : π s = π t := h
    rw [← hπvis, ← hπvis, realization_pow φ' π hπφ, realization_pow φ' π hπφ, hst]
  · intro y
    obtain ⟨s, hs⟩ := hsurj y
    exact ⟨Quotient.mk (itiSetoid φ vis) s, hs⟩

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The factorization intertwines the dynamics. -/
theorem realizationMap_equivariant (φ : Equiv.Perm S) (vis : S → I)
    (φ' : Equiv.Perm S') (vis' : S' → I) (π : S → S')
    (hπφ : ∀ s, π (φ s) = φ' (π s)) (hπvis : ∀ s, vis' (π s) = vis s)
    (hsep' : ItinerarySeparating φ' vis') (q : MinimalCarrier φ vis) :
    realizationMap φ vis φ' vis' π hπφ hπvis hsep' (quotPerm φ vis q)
      = φ' (realizationMap φ vis φ' vis' π hπφ hπvis hsep' q) := by
  refine Quotient.inductionOn q fun s => ?_
  exact hπφ s

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The factorization intertwines the labelling. -/
theorem realizationMap_vis (φ : Equiv.Perm S) (vis : S → I)
    (φ' : Equiv.Perm S') (vis' : S' → I) (π : S → S')
    (hπφ : ∀ s, π (φ s) = φ' (π s)) (hπvis : ∀ s, vis' (π s) = vis s)
    (hsep' : ItinerarySeparating φ' vis') (q : MinimalCarrier φ vis) :
    vis' (realizationMap φ vis φ' vis' π hπφ hπvis hsep' q) = quotVis φ vis q := by
  refine Quotient.inductionOn q fun s => ?_
  exact hπvis s

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The factorization through the quotient is unique. -/
theorem realization_factor_unique (φ : Equiv.Perm S) (vis : S → I)
    (φ' : Equiv.Perm S') (vis' : S' → I) (π : S → S')
    (hπφ : ∀ s, π (φ s) = φ' (π s)) (hπvis : ∀ s, vis' (π s) = vis s)
    (hsep' : ItinerarySeparating φ' vis') (g : MinimalCarrier φ vis → S')
    (hg : ∀ s, g (Quotient.mk (itiSetoid φ vis) s) = π s) :
    g = realizationMap φ vis φ' vis' π hπφ hπvis hsep' := by
  funext q
  refine Quotient.inductionOn q fun s => ?_
  rw [hg]
  rfl

end Realization

/-! ### Section C — law preservation -/

/-- The probability the passive law assigns to a finite visible trajectory. -/
noncomputable def trajProb (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I)
    (μ : S → ℝ) : ℝ :=
  ∑ s, itiIndicator φ vis T c s * μ s

/-- The pushforward of a preparation along the quotient: sum over itinerary fibres. -/
noncomputable def quotMeasure (φ : Equiv.Perm S) (vis : S → I) (μ : S → ℝ) :
    MinimalCarrier φ vis → ℝ :=
  fun q => ∑ s, if Quotient.mk (itiSetoid φ vis) s = q then μ s else 0

omit [DecidableEq S] [Fintype I] in
/-- Weighted sums against the pushforward collapse to weighted sums on the carrier. -/
theorem quotMeasure_weighted_sum (φ : Equiv.Perm S) (vis : S → I) (μ : S → ℝ)
    (f : MinimalCarrier φ vis → ℝ) :
    ∑ q, f q * quotMeasure φ vis μ q
      = ∑ s, f (Quotient.mk (itiSetoid φ vis) s) * μ s := by
  have h1 : ∀ q : MinimalCarrier φ vis, f q * quotMeasure φ vis μ q
      = ∑ s, if Quotient.mk (itiSetoid φ vis) s = q then f q * μ s else 0 := by
    intro q
    rw [quotMeasure, Finset.mul_sum]
    exact Finset.sum_congr rfl fun s _ => by rw [mul_ite, mul_zero]
  rw [Finset.sum_congr rfl fun q _ => h1 q, Finset.sum_comm]
  refine Finset.sum_congr rfl fun s _ => ?_
  exact Finset.sum_ite_eq_of_mem Finset.univ _ (fun q => f q * μ s)
    (Finset.mem_univ _)

omit [DecidableEq S] [Fintype I] in
/-- The itinerary indicator of a class is the itinerary indicator of any representative. -/
theorem itiIndicator_quotient_mk (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I)
    (s : S) :
    itiIndicator (quotPerm φ vis) (quotVis φ vis) T c
        (Quotient.mk (itiSetoid φ vis) s)
      = itiIndicator φ vis T c s := by
  classical
  exact if_congr
    ⟨fun h k hk => by
        have hh := h k hk
        rwa [quotPerm_pow_mk] at hh,
      fun h k hk => by
        rw [quotPerm_pow_mk]
        exact h k hk⟩ rfl rfl

omit [DecidableEq S] [Fintype I] in
/-- **LAW PRESERVATION.** Every finite visible trajectory probability — hence the full
closed multi-time passive law — is unchanged by passing to the minimal carrier. -/
theorem trajProb_quotient (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I)
    (μ : S → ℝ) :
    trajProb (quotPerm φ vis) (quotVis φ vis) T c (quotMeasure φ vis μ)
      = trajProb φ vis T c μ := by
  rw [trajProb, trajProb,
    quotMeasure_weighted_sum φ vis μ (itiIndicator (quotPerm φ vis) (quotVis φ vis) T c)]
  exact Finset.sum_congr rfl fun s _ => by rw [itiIndicator_quotient_mk]

omit [DecidableEq S] [Fintype I] in
/-- The pushforward commutes with reversible evolution. -/
theorem quotMeasure_evolve (φ : Equiv.Perm S) (vis : S → I) (μ : S → ℝ) :
    quotMeasure φ vis (fun s => μ (φ s))
      = fun q => quotMeasure φ vis μ (quotPerm φ vis q) := by
  funext q
  rw [quotMeasure, quotMeasure,
    show (∑ s, if Quotient.mk (itiSetoid φ vis) s = q then μ (φ s) else 0)
      = ∑ s, if Quotient.mk (itiSetoid φ vis) (φ.symm s) = q then μ s else 0 from
    Fintype.sum_equiv φ _ _ fun s => by rw [Equiv.symm_apply_apply]]
  refine Finset.sum_congr rfl fun s _ => ?_
  refine if_congr ⟨fun h => ?_, fun h => ?_⟩ rfl rfl
  · rw [← h, quotPerm_mk, Equiv.apply_symm_apply]
  · refine (quotPerm φ vis).injective ?_
    rw [quotPerm_mk, Equiv.apply_symm_apply]
    exact h

omit [DecidableEq S] [Fintype I] in
/-- The pushforward commutes with visible branch selection. -/
theorem quotMeasure_branch (φ : Equiv.Perm S) (vis : S → I) (i : I) (μ : S → ℝ) :
    quotMeasure φ vis (fun s => if vis s = i then μ s else 0)
      = fun q => if quotVis φ vis q = i then quotMeasure φ vis μ q else 0 := by
  funext q
  by_cases hq : quotVis φ vis q = i
  · rw [if_pos hq, quotMeasure, quotMeasure]
    refine Finset.sum_congr rfl fun s _ => ?_
    by_cases hs : Quotient.mk (itiSetoid φ vis) s = q
    · have hvs : vis s = i := by rw [← hs] at hq; exact hq
      rw [if_pos hs, if_pos hs, if_pos hvs]
    · rw [if_neg hs, if_neg hs]
  · rw [if_neg hq, quotMeasure]
    refine Finset.sum_eq_zero fun s _ => ?_
    by_cases hs : Quotient.mk (itiSetoid φ vis) s = q
    · have hvs : ¬vis s = i := fun h => hq (by rw [← hs]; exact h)
      rw [if_pos hs, if_neg hvs]
    · rw [if_neg hs]

/-! ### Section C′ — the capstone: glue on the minimal carrier -/

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Transitivity descends to the quotient. -/
theorem quotient_transitive (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) :
    ∀ q1 q2 : MinimalCarrier φ vis, ∃ k : ℕ, (quotPerm φ vis ^ k) q1 = q2 := by
  intro q1 q2
  refine Quotient.inductionOn₂ q1 q2 fun s t => ?_
  obtain ⟨k, hk⟩ := htrans s t
  exact ⟨k, by rw [quotPerm_pow_mk, hk]⟩

omit [DecidableEq S] [Fintype I] in
/-- **THE CAPSTONE, HALF ONE.** On the canonical minimal passive carrier, the
domain-relative glue alone forces the full diagonal-sector glue — no separation
hypothesis remains, because the carrier is separating by construction. -/
theorem passiveQuotient_glue_forces_G1
    (φ : Equiv.Perm S) (vis : S → I)
    (U : Matrix (MinimalCarrier φ vis) (MinimalCarrier φ vis) ℂ)
    (hglue : CompatibilityDomainGlue U (quotPerm φ vis)
      {w | ClassicalBranchDomain (quotPerm φ vis) (quotVis φ vis) w}) :
    DiagonalSectorGlue U (quotPerm φ vis) :=
  classicalBranch_glue_forces_G1 U (quotPerm φ vis) (quotVis φ vis)
    (quotient_itinerarySeparating φ vis) hglue

omit [DecidableEq S] [Fintype I] in
/-- **THE CAPSTONE, HALF TWO.** On the minimal passive carrier the glue-compatible
sampled dynamics is a phased permutation. -/
theorem passiveQuotient_glue_forces_monomial
    (φ : Equiv.Perm S) (vis : S → I)
    (U : Matrix (MinimalCarrier φ vis) (MinimalCarrier φ vis) ℂ)
    (hglue : CompatibilityDomainGlue U (quotPerm φ vis)
      {w | ClassicalBranchDomain (quotPerm φ vis) (quotVis φ vis) w}) :
    ∃ d : MinimalCarrier φ vis → ℂ, (∀ x, d x * conj' (d x) = 1)
      ∧ U = Matrix.diagonal d * permMatrix (quotPerm φ vis) :=
  classicalBranch_glue_forces_monomial U (quotPerm φ vis) (quotVis φ vis)
    (quotient_itinerarySeparating φ vis) hglue

omit [DecidableEq S] [Fintype I] in
/-- **THE FULL CAPSTONE.** On the minimal passive carrier of an ergodic shell, OI
compatibility — the domain glue on the classical branch domain — closes physical-flow
SRC with the canonical carrier, existence and uniqueness, with no separation premise. -/
theorem ergodicShell_SRC_of_passiveQuotient [Nonempty S]
    (φ : Equiv.Perm S) (vis : S → I)
    (U : Matrix (MinimalCarrier φ vis) (MinimalCarrier φ vis) ℂ)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t)
    (hglue : CompatibilityDomainGlue U (quotPerm φ vis)
      {w | ClassicalBranchDomain (quotPerm φ vis) (quotVis φ vis) w}) :
    (∃ ρ : Matrix (MinimalCarrier φ vis) (MinimalCarrier φ vis) ℂ,
        ρ.PosSemidef ∧ Matrix.trace ρ = 1
        ∧ U * ρ * Uᴴ = ρ
        ∧ ∀ i, Matrix.trace (fiberProj (quotVis φ vis) i * ρ)
            = ((countMarginal (quotVis φ vis) i : ℝ) : ℂ))
    ∧ ∀ ρ : Matrix (MinimalCarrier φ vis) (MinimalCarrier φ vis) ℂ,
        ρ.PosSemidef → Matrix.trace ρ = 1
        → U * ρ * Uᴴ = ρ
        → ∀ i, Matrix.trace (fiberProj (quotVis φ vis) i * ρ)
            = ((countMarginal (quotVis φ vis) i : ℝ) : ℂ) :=
  ergodicShell_SRC_of_domainGlue U (quotPerm φ vis) (quotVis φ vis)
    (quotient_itinerarySeparating φ vis) (quotient_transitive φ vis htrans) hglue

/-! ### Section D — the mandatory negative control: hidden-fibre extension -/

section HiddenFibre

variable {A : Type*}

/-- The hidden-fibre extension: attach a fibre `A` with arbitrary per-state fibre
dynamics `σ`, leaving the visible labelling blind to it. This is the enlargement the
corpus explicitly permits. -/
def hiddenExt (φ : Equiv.Perm S) (σ : S → Equiv.Perm A) : Equiv.Perm (S × A) where
  toFun p := (φ p.1, σ p.1 p.2)
  invFun p := (φ.symm p.1, (σ (φ.symm p.1)).symm p.2)
  left_inv p := by
    obtain ⟨s, a⟩ := p
    show (φ.symm (φ s), (σ (φ.symm (φ s))).symm (σ s a)) = (s, a)
    rw [Equiv.symm_apply_apply, Equiv.symm_apply_apply]
  right_inv p := by
    obtain ⟨s, a⟩ := p
    show (φ (φ.symm s), σ (φ.symm s) ((σ (φ.symm s)).symm a)) = (s, a)
    rw [Equiv.apply_symm_apply, Equiv.apply_symm_apply]

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The extension projects onto the base dynamics. -/
theorem hiddenExt_pow_fst (φ : Equiv.Perm S) (σ : S → Equiv.Perm A) (k : ℕ)
    (p : S × A) : (((hiddenExt φ σ) ^ k) p).1 = (φ ^ k) p.1 := by
  induction k generalizing p with
  | zero => rw [pow_zero, pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply]
  | succ k ih =>
      rw [pow_succ, pow_succ, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply]
      exact ih ((hiddenExt φ σ) p)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Every hidden fibre is glued: states differing only in the hidden coordinate have
identical visible itineraries. -/
theorem hiddenExt_itiRelInf_fibre (φ : Equiv.Perm S) (vis : S → I)
    (σ : S → Equiv.Perm A) (s : S) (a b : A) :
    itiRelInf (hiddenExt φ σ) (fun p => vis p.1) (s, a) (s, b) := by
  intro k
  show vis ((((hiddenExt φ σ) ^ k) (s, a)).1) = vis ((((hiddenExt φ σ) ^ k) (s, b)).1)
  exact congrArg vis ((hiddenExt_pow_fst φ σ k (s, a)).trans
    (hiddenExt_pow_fst φ σ k (s, b)).symm)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- **RAW-CARRIER SEPARATION IS NOT DERIVABLE.** Any carrier extends, by an
observationally inert hidden fibre, to a carrier that is NOT itinerary-separating. -/
theorem hiddenExt_not_separating [Nonempty S] (φ : Equiv.Perm S) (vis : S → I)
    (σ : S → Equiv.Perm A) (hA : ∃ a b : A, a ≠ b) :
    ¬ItinerarySeparating (hiddenExt φ σ) (fun p => vis p.1) := by
  intro hsep
  obtain ⟨a, b, hab⟩ := hA
  exact hab (congrArg Prod.snd
    (hsep (Classical.arbitrary S, a) (Classical.arbitrary S, b)
      (hiddenExt_itiRelInf_fibre φ vis σ _ a b)))

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- The itinerary indicator of the extension reads only the base coordinate. -/
theorem hiddenExt_itiIndicator (φ : Equiv.Perm S) (vis : S → I)
    (σ : S → Equiv.Perm A) (T : ℕ) (c : ℕ → I) (p : S × A) :
    itiIndicator (hiddenExt φ σ) (fun p => vis p.1) T c p
      = itiIndicator φ vis T c p.1 := by
  classical
  exact if_congr
    ⟨fun h k hk => by
        have hh : vis ((((hiddenExt φ σ) ^ k) p).1) = c k := h k hk
        rwa [hiddenExt_pow_fst] at hh,
      fun h k hk => by
        show vis ((((hiddenExt φ σ) ^ k) p).1) = c k
        rw [hiddenExt_pow_fst]
        exact h k hk⟩ rfl rfl

omit [DecidableEq S] [Fintype I] in
/-- **THE PASSIVE LAW CANNOT SEE THE FIBRE.** For every prior on the extension with the
right base marginal, every finite visible trajectory probability agrees with the base —
the entire closed passive law is preserved while separation fails. -/
theorem hiddenExt_same_law [Fintype A] (φ : Equiv.Perm S) (vis : S → I)
    (σ : S → Equiv.Perm A) (ν : S × A → ℝ) (μ : S → ℝ)
    (hmarg : ∀ s, ∑ a, ν (s, a) = μ s) (T : ℕ) (c : ℕ → I) :
    trajProb (hiddenExt φ σ) (fun p => vis p.1) T c ν = trajProb φ vis T c μ := by
  rw [trajProb, trajProb, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [show (∑ a, itiIndicator (hiddenExt φ σ) (fun p => vis p.1) T c (s, a) * ν (s, a))
      = ∑ a, itiIndicator φ vis T c s * ν (s, a) from
    Finset.sum_congr rfl fun a _ => by rw [hiddenExt_itiIndicator]]
  rw [← Finset.mul_sum, hmarg]

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- The quotient strips exactly the hidden fibre: when the base is separating, the
minimal carrier of the extension is canonically the base carrier. -/
theorem hiddenExt_quotient_recovers_base [Fintype A] [DecidableEq A] [Nonempty A]
    (φ : Equiv.Perm S) (vis : S → I) (σ : S → Equiv.Perm A)
    (hsep : ItinerarySeparating φ vis) :
    Function.Bijective (realizationMap (hiddenExt φ σ) (fun p => vis p.1) φ vis
      Prod.fst (fun _ => rfl) (fun _ => rfl) hsep) :=
  minimal_realization_bijective (hiddenExt φ σ) (fun p => vis p.1) φ vis
    Prod.fst (fun _ => rfl) (fun _ => rfl) hsep
    fun s => ⟨(s, Classical.arbitrary A), rfl⟩

end HiddenFibre

/-! ### Section E — the linear observability bridge -/

section LinearObservability

variable {M W : Type*} [AddCommGroup M] [AddCommGroup W]

/-- Powers of the permutation underlying an additive automorphism are additive:
subtraction passes through every iterate. -/
theorem addEquiv_pow_sub (step : M ≃+ M) (k : ℕ) (x y : M) :
    (step.toEquiv ^ k) (x - y) = (step.toEquiv ^ k) x - (step.toEquiv ^ k) y := by
  induction k with
  | zero =>
      rw [pow_zero, Equiv.Perm.one_apply, Equiv.Perm.one_apply,
        Equiv.Perm.one_apply]
  | succ k ih =>
      rw [pow_succ', Equiv.Perm.mul_apply, Equiv.Perm.mul_apply,
        Equiv.Perm.mul_apply, ih]
      exact map_sub step _ _

/-- **ITINERARY EQUIVALENCE IS THE UNOBSERVABLE COSET.** For linear passive dynamics
read through an additive map, two states share a visible itinerary exactly when their
difference lies in the unobservable subgroup — the joint kernel of the stacked readout
family. -/
theorem linear_itiRelInf_iff (step : M ≃+ M) (read : M →+ W) (x y : M) :
    itiRelInf step.toEquiv (⇑read) x y
      ↔ ∀ k : ℕ, read ((step.toEquiv ^ k) (x - y)) = 0 := by
  constructor
  · intro h k
    rw [addEquiv_pow_sub, map_sub, sub_eq_zero]
    exact h k
  · intro h k
    have hk := h k
    rw [addEquiv_pow_sub, map_sub, sub_eq_zero] at hk
    exact hk

/-- **ITINERARY SEPARATION IS CLASSICAL OBSERVABILITY.** The linear passive cut is
itinerary-separating exactly when the stacked readout family `x ↦ (C x, C A x, …)` has
trivial kernel — the Kalman observability condition, exactly as the SM reference
branch's component-complete site observer poses it. -/
theorem linear_separating_iff_observability (step : M ≃+ M) (read : M →+ W) :
    ItinerarySeparating step.toEquiv (⇑read)
      ↔ ∀ x : M, (∀ k : ℕ, read ((step.toEquiv ^ k) x) = 0) → x = 0 := by
  constructor
  · intro hsep x hx
    refine hsep x 0 fun k => ?_
    have h0 : (step.toEquiv ^ k) (0 : M) = 0 := by
      have h := addEquiv_pow_sub step k 0 0
      rwa [sub_self, sub_self] at h
    rw [hx k, h0, map_zero]
  · intro hobs x y h
    exact sub_eq_zero.mp (hobs (x - y) ((linear_itiRelInf_iff step read x y).mp h))

end LinearObservability

#print axioms itiRelInf_pow
#print axioms itiRelInf_evolve
#print axioms itiRelInf_symm_evolve
#print axioms quotPerm_mk
#print axioms quotPerm_pow_mk
#print axioms itiRelInf_greatest_congruence
#print axioms quotient_itinerarySeparating
#print axioms passiveMinimal_iff_itinerarySeparating
#print axioms realization_pow
#print axioms minimal_realization_bijective
#print axioms realizationMap_equivariant
#print axioms realizationMap_vis
#print axioms realization_factor_unique
#print axioms quotMeasure_weighted_sum
#print axioms itiIndicator_quotient_mk
#print axioms trajProb_quotient
#print axioms quotMeasure_evolve
#print axioms quotMeasure_branch
#print axioms quotient_transitive
#print axioms passiveQuotient_glue_forces_G1
#print axioms passiveQuotient_glue_forces_monomial
#print axioms ergodicShell_SRC_of_passiveQuotient
#print axioms hiddenExt_pow_fst
#print axioms hiddenExt_itiRelInf_fibre
#print axioms hiddenExt_not_separating
#print axioms hiddenExt_itiIndicator
#print axioms hiddenExt_same_law
#print axioms hiddenExt_quotient_recovers_base
#print axioms addEquiv_pow_sub
#print axioms linear_itiRelInf_iff
#print axioms linear_separating_iff_observability

end PassiveQuotient
end OIBridge
