/-
  OIBridge/RegionTower.lean — OI_Q Level III, second entry: the quasilocal region tower, the
  causal cone, and the state-selection audit.

  LEVEL III, ROUND TWO. The first entry established, in the one-step form `S × R`, that the
  restriction of states between regions is the Level II discard with the observable inclusion
  as its dual, and that continuous time is not determined by the discrete dynamics. This entry
  formalizes the ACTUAL region tower — regions as finite sets of sites `Λ ⊆ Λ' ⊆ Λ''` of a
  fixed-spacing lattice — and settles what the finite stages say about the two pre-registered
  outcomes that remained: whether the discrete dynamics is compatible across regions, and
  whether a distinguished representation is a theory-level input.

  THE TOWER. A site type `ι`, a state set `Q` per site, and for a region `Λ : Finset ι` the
  configuration carrier `Λ → Q`. For `Λ ⊆ Λ'`, the inclusion of observables
  `inclObs h : M_Λ → M_{Λ'}` extends an observable by the identity on the sites of `Λ' \ Λ`
  (entrywise: the observable's entry on the restricted configurations, times the indicator that
  the two configurations agree off `Λ`), and the restriction of states
  `restrict h : M_{Λ'} → M_Λ` sums the state over the configurations of `Λ' \ Λ` (the partial
  trace). Both are the Level II operations of the first entry written on the lattice.

  (1) FUNCTORIALITY. `inclObs` is the identity for `Λ ⊆ Λ` and composes along `Λ ⊆ Λ' ⊆ Λ''`
      (`inclObs_refl`, `inclObs_trans`); `restrict` is the identity for `Λ ⊆ Λ` and composes
      (`restrict_refl`, `restrict_trans`); and the two are dual under the trace pairing
      (`trace_inclObs_mul_restrict`). The transitivity of restriction is derived from the
      transitivity of inclusion through the duality and the nondegeneracy of the pairing, so the
      projective system of states is determined by the inductive system of observables — the
      standard quasilocal structure, with no new postulate.

  (2) THE CAUSAL CONE. The substratum update is a map on global configurations; its coupling
      graph records, for each site, the neighbourhood its next value depends on
      (`DependsOnlyOn`). The corpus states by induction that `k` steps depend only on the
      `k`-ball; the kernel proves it (`iterate_dependsOnlyOn_ball`): an observable supported in
      a region `A` after `k` steps depends only on the `k`-ball of `A`, so an intervention
      supported outside that ball cannot alter it (`readout_unaffected_outside_ball`).
      Discrete-time dynamics is therefore compatible across regions by locality alone; nothing
      beyond the finite update and its coupling graph enters.

  (3) THE STATE-SELECTION AUDIT. Consistent state families — one state on every region, each
      the restriction of the next — form the admissible state space of the quasilocal theory.
      They are closed under mixing (`consistent_mix`), the reference family (the uniformly mixed
      configurations, the only preparation the interface assumes) is a member
      (`uniform_family_consistent`), and it is the UNIQUE family on each region invariant under
      every local unitary: a state commuting with every unitary is a multiple of the identity
      (`invariant_state_scalar`, the finite Schur lemma, proved from the permutation and
      diagonal unitaries the substratum itself supplies). The laws of the theory — which
      instruments are available — mention no state (the typed interface's availability
      predicate has no state argument), so every consistent family is a state of the SAME theory
      with the SAME laws; a distinguished representation would be a choice among them, and the
      interface's own preparation rule already singles out one canonical family. At the finite
      stages, then, no law-level object distinguishes sectors: outcome A of the pre-registered
      fork holds at the level of laws, and a sector selector would be a state-level input of the
      initial-condition kind. Whether some OI prediction requires a distinguished sector is
      not a question the finite theory can pose, and it is not claimed either way.

  WHAT IS NOT CLAIMED: no infinite-volume algebra, no limiting representation, and no
  inequivalence of representations is constructed; the uniqueness of the invariant family is a
  finite-stage theorem; the causal
  cone is proved for an abstract update with a coupling graph, not for a specific lattice
  Hamiltonian. Bare OI and the frozen Level I and Level II statements are untouched.
-/

import OIBridge.RegionLimit

namespace OIBridge
namespace RegionTower

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy PrimitiveSource InterventionLocality
open MicroReversibility LieRankSource SubstratumSource SubstratumInterface ReadWriteControl
open StructuralClosure TypedCompletion RegionLimit

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — regions, configurations, restriction and inclusion -/

section Tower

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q]

/-- The configurations of a region: one state per site. -/
abbrev Conf (Λ : Finset ι) (Q : Type) := (↥Λ → Q)

/-- Restrict a configuration of `Λ'` to `Λ ⊆ Λ'`. -/
def confRestrict {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (F : Conf Λ' Q) : Conf Λ Q :=
  fun x => F ⟨x.1, h x.2⟩

/-- Two configurations of `Λ'` agree off `Λ`. -/
def AgreeOff {Λ Λ' : Finset ι} (_ : Λ ⊆ Λ') (F G : Conf Λ' Q) : Prop :=
  ∀ x : ↥Λ', x.1 ∉ Λ → F x = G x

instance {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (F G : Conf Λ' Q) : Decidable (AgreeOff h F G) := by
  unfold AgreeOff; infer_instance

theorem confRestrict_refl {Λ : Finset ι} (F : Conf Λ Q) :
    confRestrict (Finset.Subset.refl Λ) F = F := rfl

theorem confRestrict_trans {Λ Λ' Λ'' : Finset ι} (h : Λ ⊆ Λ') (h' : Λ' ⊆ Λ'') (F : Conf Λ'' Q) :
    confRestrict h (confRestrict h' F) = confRestrict (h.trans h') F := rfl

theorem agreeOff_refl {Λ : Finset ι} (F G : Conf Λ Q) :
    AgreeOff (Finset.Subset.refl Λ) F G := fun x hx => absurd x.2 hx

/-- Agreement off `Λ` inside `Λ''` is agreement off `Λ'` together with agreement of the
restrictions off `Λ`. -/
theorem agreeOff_trans_iff {Λ Λ' Λ'' : Finset ι} (h : Λ ⊆ Λ') (h' : Λ' ⊆ Λ'')
    (F G : Conf Λ'' Q) :
    AgreeOff (h.trans h') F G
      ↔ AgreeOff h' F G ∧ AgreeOff h (confRestrict h' F) (confRestrict h' G) := by
  constructor
  · intro hFG
    refine ⟨fun x hx => hFG x (fun hx' => hx (h hx')), fun x hx => hFG ⟨x.1, h' x.2⟩ hx⟩
  · rintro ⟨h1, h2⟩ x hx
    by_cases hx' : x.1 ∈ Λ'
    · exact h2 ⟨x.1, hx'⟩ hx
    · exact h1 x hx'

/-- **INCLUSION OF OBSERVABLES**: extend by the identity on the adjoined sites. -/
def inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ :=
  fun F G => if AgreeOff h F G then X (confRestrict h F) (confRestrict h G) else 0

/-- **RESTRICTION OF STATES**: sum over the configurations of the adjoined sites. -/
def restrict {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (ρ : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ :=
  fun f g => ∑ F : Conf Λ' Q, ∑ G : Conf Λ' Q,
    if confRestrict h F = f ∧ confRestrict h G = g ∧ AgreeOff h F G then ρ F G else 0

theorem inclObs_apply {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (F G : Conf Λ' Q) :
    inclObs h X F G = if AgreeOff h F G then X (confRestrict h F) (confRestrict h G) else 0 :=
  rfl

theorem restrict_apply {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (ρ : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ)
    (f g : Conf Λ Q) :
    restrict h ρ f g = ∑ F : Conf Λ' Q, ∑ G : Conf Λ' Q,
      if confRestrict h F = f ∧ confRestrict h G = g ∧ AgreeOff h F G then ρ F G else 0 :=
  rfl

/-- Inclusion is the identity on a region. -/
theorem inclObs_refl {Λ : Finset ι} (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs (Finset.Subset.refl Λ) X = X := by
  ext F G
  rw [inclObs_apply, if_pos (agreeOff_refl F G)]
  rfl

/-- **INCLUSION COMPOSES** along `Λ ⊆ Λ' ⊆ Λ''`. -/
theorem inclObs_trans {Λ Λ' Λ'' : Finset ι} (h : Λ ⊆ Λ') (h' : Λ' ⊆ Λ'')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs h' (inclObs h X) = inclObs (h.trans h') X := by
  ext F G
  simp only [inclObs_apply, agreeOff_trans_iff h h' F G, confRestrict_trans]
  by_cases h1 : AgreeOff h' F G
  · by_cases h2 : AgreeOff h (confRestrict h' F) (confRestrict h' G)
    · rw [if_pos h1, if_pos h2, if_pos ⟨h1, h2⟩]
    · rw [if_pos h1, if_neg h2, if_neg (fun h12 => h2 h12.2)]
  · rw [if_neg h1, if_neg (fun h12 => h1 h12.1)]

/-- Restriction is the identity on a region. -/
theorem restrict_refl {Λ : Finset ι} (ρ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    restrict (Finset.Subset.refl Λ) ρ = ρ := by
  ext f g
  rw [restrict_apply]
  simp only [confRestrict_refl, agreeOff_refl, and_true]
  rw [Finset.sum_eq_single f (fun F _ hF => Finset.sum_eq_zero fun G _ => by simp [hF])
    (by simp)]
  rw [Finset.sum_eq_single g (fun G _ hG => by simp [hG]) (by simp)]
  simp

/-- Reordering a four-fold sum: the outer two indices move inside. -/
theorem sum4_comm {α β γ δ : Type} [Fintype α] [Fintype β] [Fintype γ] [Fintype δ]
    (T : α → β → γ → δ → ℂ) :
    ∑ a : α, ∑ b : β, ∑ c : γ, ∑ d : δ, T a b c d
      = ∑ c : γ, ∑ d : δ, ∑ a : α, ∑ b : β, T a b c d :=
  calc ∑ a : α, ∑ b : β, ∑ c : γ, ∑ d : δ, T a b c d
      = ∑ a : α, ∑ c : γ, ∑ b : β, ∑ d : δ, T a b c d :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ c : γ, ∑ a : α, ∑ b : β, ∑ d : δ, T a b c d := Finset.sum_comm
    _ = ∑ c : γ, ∑ a : α, ∑ d : δ, ∑ b : β, T a b c d :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ c : γ, ∑ d : δ, ∑ a : α, ∑ b : β, T a b c d :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm

/-- **DUALITY**: the trace pairing of an included observable with a state is the pairing of the
observable with the restricted state. -/
theorem trace_inclObs_mul_restrict {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (ρ : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    (inclObs h X * ρ).trace = (X * restrict h ρ).trace := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, inclObs_apply, restrict_apply,
    Finset.mul_sum]
  -- LHS: ∑ F, ∑ G, (if AgreeOff h F G then X (F|Λ) (G|Λ) else 0) * ρ G F
  -- RHS: ∑ f, ∑ g, ∑ G, ∑ F, X f g * (if G|Λ = g ∧ F|Λ = f ∧ AgreeOff h G F then ρ G F else 0)
  symm
  calc ∑ f : Conf Λ Q, ∑ g : Conf Λ Q, ∑ G : Conf Λ' Q, ∑ F : Conf Λ' Q,
          X f g * (if confRestrict h G = g ∧ confRestrict h F = f ∧ AgreeOff h G F then ρ G F
            else 0)
        = ∑ G : Conf Λ' Q, ∑ F : Conf Λ' Q, ∑ f : Conf Λ Q, ∑ g : Conf Λ Q,
          X f g * (if confRestrict h G = g ∧ confRestrict h F = f ∧ AgreeOff h G F then ρ G F
            else 0) := sum4_comm _
      _ = ∑ G : Conf Λ' Q, ∑ F : Conf Λ' Q,
          (if AgreeOff h G F then X (confRestrict h F) (confRestrict h G) * ρ G F else 0) := by
          refine Finset.sum_congr rfl fun G _ => Finset.sum_congr rfl fun F _ => ?_
          rw [Finset.sum_eq_single (confRestrict h F)
            (fun f _ hf => Finset.sum_eq_zero fun g _ => by simp [Ne.symm hf]) (by simp)]
          rw [Finset.sum_eq_single (confRestrict h G) (fun g _ hg => by simp [Ne.symm hg])
            (by simp)]
          by_cases hGF : AgreeOff h G F
          · simp [hGF]
          · simp [hGF]
      _ = ∑ F : Conf Λ' Q, ∑ G : Conf Λ' Q,
          (if AgreeOff h F G then X (confRestrict h F) (confRestrict h G) else 0) * ρ G F := by
          rw [Finset.sum_comm]
          refine Finset.sum_congr rfl fun F _ => Finset.sum_congr rfl fun G _ => ?_
          have hsymm : AgreeOff h G F ↔ AgreeOff h F G :=
            ⟨fun a x hx => (a x hx).symm, fun a x hx => (a x hx).symm⟩
          by_cases hFG : AgreeOff h F G
          · rw [if_pos hFG, if_pos (hsymm.mpr hFG)]
          · rw [if_neg hFG, if_neg (fun a => hFG (hsymm.mp a)), zero_mul]

/-- The trace pairing is nondegenerate: matrices pairing equally with every observable are
equal. -/
theorem eq_of_trace_pairing {S : Type} [Fintype S] [DecidableEq S]
    {ρ σ : Matrix S S ℂ} (h : ∀ X : Matrix S S ℂ, (X * ρ).trace = (X * σ).trace) : ρ = σ := by
  ext i j
  have := h (Matrix.single j i 1)
  simpa [Matrix.trace_single_mul] using this

/-- **RESTRICTION COMPOSES**, derived from the composition of inclusion through the duality. -/
theorem restrict_trans {Λ Λ' Λ'' : Finset ι} (h : Λ ⊆ Λ') (h' : Λ' ⊆ Λ'')
    (ρ : Matrix (Conf Λ'' Q) (Conf Λ'' Q) ℂ) :
    restrict h (restrict h' ρ) = restrict (h.trans h') ρ := by
  refine eq_of_trace_pairing fun X => ?_
  rw [← trace_inclObs_mul_restrict, ← trace_inclObs_mul_restrict, inclObs_trans,
    trace_inclObs_mul_restrict]

end Tower

/-! ### Section B — the causal cone of a local update -/

section CausalCone

variable {ι Q : Type} [DecidableEq ι]

/-- A function of global configurations depends only on the sites of `A`. -/
def DependsOnlyOn (f : (ι → Q) → Q) (A : Finset ι) : Prop :=
  ∀ s s' : ι → Q, (∀ x ∈ A, s x = s' x) → f s = f s'

/-- A coupling graph for an update `φ`: each site's next value depends only on its
neighbourhood. -/
structure CouplingGraph (φ : (ι → Q) → (ι → Q)) where
  nbhd : ι → Finset ι
  local_dep : ∀ i, DependsOnlyOn (fun s => φ s i) (nbhd i)

/-- The `k`-ball of a region: the neighbourhoods iterated `k` times. -/
def ball {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ) (A : Finset ι) : ℕ → Finset ι
  | 0 => A
  | k + 1 => (ball G A k).biUnion G.nbhd

theorem ball_zero {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ) (A : Finset ι) :
    ball G A 0 = A := rfl

theorem ball_succ {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ) (A : Finset ι) (k : ℕ) :
    ball G A (k + 1) = (ball G A k).biUnion G.nbhd := rfl

/-- One step: a function depending only on `A` becomes, after the update, a function depending
only on the neighbourhood of `A`. -/
theorem dependsOnlyOn_comp_step {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ)
    (f : (ι → Q) → Q) (A : Finset ι) (hf : DependsOnlyOn f A) :
    DependsOnlyOn (fun s => f (φ s)) (A.biUnion G.nbhd) := by
  intro s s' hss'
  apply hf
  intro x hx
  apply G.local_dep x
  intro y hy
  exact hss' y (Finset.mem_biUnion.mpr ⟨x, hx, hy⟩)

/-- **THE CAUSAL CONE**: after `k` steps, a function depending only on `A` depends only on the
`k`-ball of `A`. -/
theorem iterate_dependsOnlyOn_ball {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ)
    (f : (ι → Q) → Q) (A : Finset ι) (hf : DependsOnlyOn f A) (k : ℕ) :
    DependsOnlyOn (fun s => f (φ^[k] s)) (ball G A k) := by
  induction k with
  | zero => exact fun s s' hss' => hf s s' hss'
  | succ k ih =>
    have h2 := dependsOnlyOn_comp_step G (fun s => f (φ^[k] s)) (ball G A k) ih
    intro s s' hss'
    have := h2 s s' hss'
    show f (φ^[k + 1] s) = f (φ^[k + 1] s')
    rw [Function.iterate_succ_apply, Function.iterate_succ_apply]
    exact this

/-- A site's value after `k` steps depends only on the `k`-ball of the site. -/
theorem site_iterate_dependsOnlyOn {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ) (i : ι)
    (k : ℕ) : DependsOnlyOn (fun s => φ^[k] s i) (ball G {i} k) :=
  iterate_dependsOnlyOn_ball G (fun s => s i) {i} (fun _ _ h => h i (Finset.mem_singleton_self i)) k

/-- **AN INTERVENTION OUTSIDE THE CONE CANNOT ALTER THE READOUT**: two configurations that
differ only outside the `k`-ball of `A` give the same value to every `A`-supported function
after `k` steps. -/
theorem readout_unaffected_outside_ball {φ : (ι → Q) → (ι → Q)} (G : CouplingGraph φ)
    (f : (ι → Q) → Q) (A : Finset ι) (hf : DependsOnlyOn f A) (k : ℕ) (s s' : ι → Q)
    (hout : ∀ x ∈ ball G A k, s x = s' x) : f (φ^[k] s) = f (φ^[k] s') :=
  iterate_dependsOnlyOn_ball G f A hf k s s' hout

end CausalCone

/-! ### Section C — the state-selection audit: consistent families and the invariant state -/

section Selection

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q]

/-- **A CONSISTENT FAMILY**: one state on every region, each the restriction of every larger
one. -/
def Consistent (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : Prop :=
  ∀ (Λ Λ' : Finset ι) (h : Λ ⊆ Λ'), restrict h (ρ Λ') = ρ Λ

/-- Restriction is additive and homogeneous. -/
theorem restrict_add {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (ρ σ : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    restrict h (ρ + σ) = restrict h ρ + restrict h σ := by
  ext f g
  simp only [restrict_apply, Matrix.add_apply]
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun F _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun G _ => ?_
  split_ifs <;> simp

theorem restrict_smul {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (c : ℂ)
    (ρ : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) : restrict h (c • ρ) = c • restrict h ρ := by
  ext f g
  simp only [restrict_apply, Matrix.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun F _ => Finset.sum_congr rfl fun G _ => ?_
  split_ifs <;> simp

/-- **CONSISTENT FAMILIES ARE CLOSED UNDER MIXING**: the admissible state space is convex. -/
theorem consistent_mix {ρ σ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : Consistent ρ) (hσ : Consistent σ) (p : ℂ) :
    Consistent (fun Λ => p • ρ Λ + (1 - p) • σ Λ) := by
  intro Λ Λ' h
  rw [restrict_add, restrict_smul, restrict_smul, hρ Λ Λ' h, hσ Λ Λ' h]

/-- The reference family: the uniformly mixed configurations on every region. -/
noncomputable def uniformFamily (ι Q : Type) [DecidableEq ι] [Fintype Q]
    [DecidableEq Q] : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ :=
  fun Λ => ((Fintype.card (Conf Λ Q) : ℂ))⁻¹ • (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)

/-- The number of configurations of `Λ'` restricting to a given configuration of `Λ ⊆ Λ'` and
agreeing with a given configuration off `Λ`: exactly one. -/
theorem card_extensions_agree {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (f : Conf Λ Q) (G : Conf Λ' Q) :
    (Finset.univ.filter (fun F : Conf Λ' Q => confRestrict h F = f ∧ AgreeOff h F G)).card
      = 1 := by
  rw [Finset.card_eq_one]
  refine ⟨fun x => if hx : x.1 ∈ Λ then f ⟨x.1, hx⟩ else G x, ?_⟩
  ext F
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
  constructor
  · rintro ⟨hF, hG⟩
    funext x
    by_cases hx : x.1 ∈ Λ
    · rw [dif_pos hx, ← hF]
      rfl
    · rw [dif_neg hx]
      exact hG x hx
  · rintro rfl
    refine ⟨?_, ?_⟩
    · funext x
      simp [confRestrict, x.2]
    · intro x hx
      simp [hx]

/-- The configurations of `Λ'` restricting to `f` on `Λ ⊆ Λ'` correspond to the configurations
of `Λ' \ Λ`. -/
def fibreEquiv {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (f : Conf Λ Q) :
    {F : Conf Λ' Q // confRestrict h F = f} ≃ Conf (Λ' \ Λ) Q where
  toFun F := fun x => F.1 ⟨x.1, (Finset.mem_sdiff.mp x.2).1⟩
  invFun u := ⟨fun x => if hx : x.1 ∈ Λ then f ⟨x.1, hx⟩
      else u ⟨x.1, Finset.mem_sdiff.mpr ⟨x.2, hx⟩⟩, by
    funext x
    simp [confRestrict, x.2]⟩
  left_inv F := by
    apply Subtype.ext
    funext x
    by_cases hx : x.1 ∈ Λ
    · simp only [dif_pos hx]
      exact (congrFun F.2 ⟨x.1, hx⟩).symm
    · simp only [dif_neg hx]
  right_inv u := by
    funext x
    have hx : x.1 ∉ Λ := (Finset.mem_sdiff.mp x.2).2
    simp only [dif_neg hx]

/-- The fibre count: `|Q|^{|Λ' \ Λ|}` configurations of `Λ'` restrict to a given one on `Λ`. -/
theorem card_fibre {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (f : Conf Λ Q) :
    (Finset.univ.filter (fun F : Conf Λ' Q => confRestrict h F = f)).card
      = Fintype.card Q ^ (Λ' \ Λ).card := by
  rw [← Fintype.card_subtype, Fintype.card_congr (fibreEquiv h f), Fintype.card_fun,
    Fintype.card_coe]

theorem card_conf (Λ : Finset ι) : Fintype.card (Conf Λ Q) = Fintype.card Q ^ Λ.card := by
  rw [Fintype.card_fun, Fintype.card_coe]

/-- Restricting the uniform state on `Λ'` gives the uniform state on `Λ`, entrywise. -/
theorem restrict_uniform_apply [Nonempty Q] {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (f g : Conf Λ Q) :
    restrict h (((Fintype.card (Conf Λ' Q) : ℂ))⁻¹ • (1 : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ)) f g
      = ((Fintype.card (Conf Λ Q) : ℂ))⁻¹ * (if f = g then 1 else 0) := by
  rw [restrict_apply]
  have hinner : ∀ F : Conf Λ' Q, (∑ G : Conf Λ' Q,
      if confRestrict h F = f ∧ confRestrict h G = g ∧ AgreeOff h F G
        then (((Fintype.card (Conf Λ' Q) : ℂ))⁻¹ • (1 : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ)) F G
        else 0)
      = if confRestrict h F = f ∧ confRestrict h F = g
          then ((Fintype.card (Conf Λ' Q) : ℂ))⁻¹ else 0 := by
    intro F
    rw [Finset.sum_eq_single F (fun G _ hG => by
        simp only [Matrix.smul_apply, Matrix.one_apply, if_neg (Ne.symm hG), smul_zero, ite_self])
      (by simp)]
    simp only [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one]
    have hFF : AgreeOff h F F := fun _ _ => rfl
    by_cases h1 : confRestrict h F = f
    · by_cases h2 : confRestrict h F = g
      · rw [if_pos ⟨h1, h2, hFF⟩, if_pos ⟨h1, h2⟩]
      · rw [if_neg (fun a => h2 a.2.1), if_neg (fun a => h2 a.2)]
    · rw [if_neg (fun a => h1 a.1), if_neg (fun a => h1 a.1)]
  simp only [hinner]
  by_cases hfg : f = g
  · subst hfg
    simp only [and_self, if_true, mul_one]
    rw [Finset.sum_ite, Finset.sum_const_zero, add_zero, Finset.sum_const, nsmul_eq_mul,
      card_fibre, card_conf, card_conf]
    have hq : (Fintype.card Q : ℂ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
    have hcard : Λ'.card = (Λ' \ Λ).card + Λ.card := (Finset.card_sdiff_add_card_eq_card h).symm
    rw [hcard, pow_add]
    push_cast
    field_simp
  · simp only [hfg, if_false, mul_zero]
    refine Finset.sum_eq_zero fun F _ => ?_
    rw [if_neg]
    rintro ⟨h1, h2⟩
    exact hfg (h1.symm.trans h2)

/-- **THE REFERENCE FAMILY IS CONSISTENT.** -/
theorem uniform_family_consistent [Nonempty Q] : Consistent (uniformFamily ι Q) := by
  intro Λ Λ' h
  ext f g
  rw [uniformFamily, uniformFamily, restrict_uniform_apply h f g, Matrix.smul_apply,
    Matrix.one_apply, smul_eq_mul]

end Selection

/-! ### Section D — the finite Schur lemma: the invariant state is the uniform one -/

section Schur

variable {S : Type} [Fintype S] [DecidableEq S]

/-- A phase-gate conjugation multiplies the entry `(i, j)` by `d i * star (d j)`. -/
theorem phaseGate_conj_apply (a : S) (ρ : Matrix S S ℂ) (i j : S) :
    (phaseGate a * ρ * (phaseGate a)ᴴ) i j
      = (if a = i then Complex.I else 1) * ρ i j * star (if a = j then Complex.I else 1) := by
  rw [phaseGate, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul]
  simp only [Pi.star_apply]

/-- Invariance under the phase gates kills every off-diagonal entry. -/
theorem offDiag_zero_of_phase_invariant (ρ : Matrix S S ℂ)
    (hinv : ∀ a : S, phaseGate a * ρ * (phaseGate a)ᴴ = ρ) (i j : S) (hij : i ≠ j) :
    ρ i j = 0 := by
  have h := congrFun (congrFun (hinv i) i) j
  rw [phaseGate_conj_apply, if_pos rfl, if_neg hij, star_one, mul_one] at h
  -- h : I * ρ i j = ρ i j
  have h2 : (Complex.I - 1) * ρ i j = 0 := by rw [sub_mul, h, one_mul, sub_self]
  rcases mul_eq_zero.mp h2 with h3 | h3
  · exfalso
    have : Complex.I = 1 := sub_eq_zero.mp h3
    have := congrArg Complex.im this
    simp at this
  · exact h3

/-- Invariance under the state exchanges makes every diagonal entry equal. -/
theorem diag_eq_of_perm_invariant (ρ : Matrix S S ℂ)
    (hinv : ∀ σ : Equiv.Perm S, permMatrix σ * ρ * (permMatrix σ)ᴴ = ρ) (i j : S) :
    ρ i i = ρ j j := by
  have h := congrFun (congrFun (hinv (Equiv.swap i j)) i) i
  rw [permMatrix_conj_apply, Equiv.symm_swap, Equiv.swap_apply_left] at h
  exact h.symm

/-- **THE FINITE SCHUR LEMMA**: a state invariant under the substratum's own bijective and phase
interventions is a multiple of the identity. -/
theorem invariant_state_scalar [Nonempty S] (ρ : Matrix S S ℂ)
    (hperm : ∀ σ : Equiv.Perm S, permMatrix σ * ρ * (permMatrix σ)ᴴ = ρ)
    (hphase : ∀ a : S, phaseGate a * ρ * (phaseGate a)ᴴ = ρ) :
    ρ = (ρ (Classical.arbitrary S) (Classical.arbitrary S)) • (1 : Matrix S S ℂ) := by
  ext i j
  rw [Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  by_cases hij : i = j
  · subst hij
    rw [if_pos rfl, mul_one]
    exact diag_eq_of_perm_invariant ρ hperm i _
  · rw [if_neg hij, mul_zero]
    exact offDiag_zero_of_phase_invariant ρ hphase i j hij

/-- **THE UNIFORM STATE IS THE UNIQUE NORMALIZED INVARIANT STATE.** -/
theorem invariant_normalized_eq_uniform [Nonempty S] (ρ : Matrix S S ℂ)
    (hperm : ∀ σ : Equiv.Perm S, permMatrix σ * ρ * (permMatrix σ)ᴴ = ρ)
    (hphase : ∀ a : S, phaseGate a * ρ * (phaseGate a)ᴴ = ρ) (htr : ρ.trace = 1) :
    ρ = ((Fintype.card S : ℂ))⁻¹ • (1 : Matrix S S ℂ) := by
  have hs := invariant_state_scalar ρ hperm hphase
  set c := ρ (Classical.arbitrary S) (Classical.arbitrary S) with hc
  have htr' : (Fintype.card S : ℂ) * c = 1 := by
    rw [hs, Matrix.trace_smul, Matrix.trace_one, smul_eq_mul, mul_comm] at htr
    exact htr
  have hcard : (Fintype.card S : ℂ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  rw [hs]
  congr 1
  field_simp
  linear_combination htr'

/-- The uniform state is invariant under every unitary. -/
theorem uniform_invariant (U : Matrix S S ℂ) (hU : Uᴴ * U = 1) :
    U * (((Fintype.card S : ℂ))⁻¹ • (1 : Matrix S S ℂ)) * Uᴴ
      = ((Fintype.card S : ℂ))⁻¹ • (1 : Matrix S S ℂ) := by
  rw [Matrix.mul_smul, Matrix.mul_one, Matrix.smul_mul, mul_eq_one_comm.mp hU]

end Schur

/-! ### Section E — the audit summary for the second entry -/

section Summary

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q]

/-- **THE STATE-SELECTION AUDIT.** The admissible state space (consistent families) is convex,
contains the reference family, and on every region the reference state is the unique normalized
state invariant under the substratum's own bijective and phase interventions. -/
theorem state_selection_audit [Nonempty Q] :
    Consistent (uniformFamily ι Q)
    ∧ (∀ (ρ σ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ), Consistent ρ → Consistent σ →
        ∀ p : ℂ, Consistent (fun Λ => p • ρ Λ + (1 - p) • σ Λ))
    ∧ (∀ (Λ : Finset ι) (ρ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        (∀ σ : Equiv.Perm (Conf Λ Q), permMatrix σ * ρ * (permMatrix σ)ᴴ = ρ) →
        (∀ a : Conf Λ Q, phaseGate a * ρ * (phaseGate a)ᴴ = ρ) → ρ.trace = 1 →
        ρ = uniformFamily ι Q Λ) :=
  ⟨uniform_family_consistent, fun _ _ hρ hσ p => consistent_mix hρ hσ p,
    fun _ ρ hperm hphase htr => invariant_normalized_eq_uniform ρ hperm hphase htr⟩

end Summary

#print axioms confRestrict_trans
#print axioms agreeOff_trans_iff
#print axioms inclObs_refl
#print axioms inclObs_trans
#print axioms restrict_refl
#print axioms sum4_comm
#print axioms trace_inclObs_mul_restrict
#print axioms eq_of_trace_pairing
#print axioms restrict_trans
#print axioms dependsOnlyOn_comp_step
#print axioms iterate_dependsOnlyOn_ball
#print axioms site_iterate_dependsOnlyOn
#print axioms readout_unaffected_outside_ball
#print axioms restrict_add
#print axioms restrict_smul
#print axioms consistent_mix
#print axioms card_extensions_agree
#print axioms card_fibre
#print axioms card_conf
#print axioms restrict_uniform_apply
#print axioms uniform_family_consistent
#print axioms phaseGate_conj_apply
#print axioms offDiag_zero_of_phase_invariant
#print axioms diag_eq_of_perm_invariant
#print axioms invariant_state_scalar
#print axioms invariant_normalized_eq_uniform
#print axioms uniform_invariant
#print axioms state_selection_audit

end RegionTower
end OIBridge
