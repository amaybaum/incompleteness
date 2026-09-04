/-
  OIBridge/InstrumentAvailability.lean — post-Level III instrument audit, second entry:
  countermodel 1, and Q3 decided negatively.

  THE QUESTION. Q3 of the audit: are stage-compatible operations that no finite region carries
  operationally available from the assumptions OI_Q already carries, or is that a further
  principle? The first entry showed such operations exist as maps. Existence is not availability,
  and this entry tests whether availability follows.

  THE TEST. Build a theory that keeps everything the frozen levels supply and withholds exactly
  one thing: the availability of operations no finite region carries. If such a theory exists and
  is closed under the operations the framework already performs, the availability claim is
  independent of the frozen structure, and any target containing those operations needs a new
  principle to reach them.

  WHAT THE COUNTERMODEL IS. `AvailFS` declares an operation available exactly when it is a
  finite-support instrument. It is a predicate ON the Level III objects, not a replacement for
  them: the quasilocal algebra, its states and its dynamics are unchanged, witnessed by
  `states_untouched` — every consistent family of density matrices, not merely the reference one,
  still extends to a state with the same values on the finite stages — and `dynamics_untouched`. Instrument data is generalized from `Fin n` to an arbitrary finite
  index (`IsQInstrJ`, `IsFSJ`, `qTotalJ`, `qBranchJ`, agreeing with the first entry's predicates on
  `Fin n` by `isQInstrJ_fin`, `isFSJ_fin`, `qTotalJ_fin`) so that composition can use a product
  index.

  NOTHING FROZEN IS WEAKENED. Every finite-region endomorphic Kraus instrument supplied by the
  Level II theory is available in this fixed-carrier interface (`availFS_of_kraus`), and conversely
  every available operation is one (`kraus_of_availFS`), so the theory contains exactly the
  operations the first entry characterized. Level II is typed and also has dimension-changing
  operations — carrier attachment and discard — which no predicate on this fixed carrier can
  express; that structure stays separately frozen and unchanged, neither modelled nor withheld.

  The theory is closed under the operations this interface performs: the identity (`availFS_id`),
  composition on the union of the
  regions (`availFS_comp`), outcome relabelling (`availFS_relabel`), outcome coarse-graining
  (`qBranchJ_coarse`, `sum_qBranchJ` — the branches of a coarser outcome map are sums of branches,
  which holds for any instrument data and so for every available one), and the frozen OI-induced
  dynamics, which carries an available operation to an available operation on the hat region
  (`availFS_dyn`).

  WHAT IT WITHHOLDS. The all-sites phase map of the first entry is the total map of no available
  operation, at any finite outcome index (`phaseAll_not_availFS`, through
  `qTotalJ_stage_of_disjoint`: an available operation fixes the observables of a region disjoint
  from its support, while the phase map moves a single-site matrix unit at every site).

  Q3, DECIDED NEGATIVELY (`q3_countermodel`). The current frozen structure together with
  finite-support quasilocal availability does not entail the availability of genuinely
  infinite-support coherent operations, within this fixed-algebra operational interface. Q5
  sharpens accordingly: an extension of the target requiring such operations needs some additional
  principle supplying them. "Operational completion" is a proposed name for such a principle, not a
  uniquely forced one — a different additional physical principle, or a different substratum, could
  supply the same availability.

  WHAT IS NOT CLAIMED: that OI forbids such operations — the countermodel shows independence from
  the frozen structure, not impossibility, and a different substratum or a further principle may
  well supply them; that the finite-support theory is the intended physics — it is a witness, not
  a proposal; that the closure list above is exhaustive of every operation a completed framework
  might perform; and nothing about Q2, Q4, the abstract completely positive class, continuous time,
  or sector selection, all untouched. Bare OI and the frozen Level I, Level II and Level III
  statements are untouched, and no manuscript change is made in this round.
-/

import OIBridge.InstrumentCompletion

namespace OIBridge
namespace InstrumentAvailability

open Complex Matrix RegionTower QuasilocalAlgebra QuasilocalCharacterization InstrumentCompletion

open scoped ComplexOrder Matrix.Norms.L2Operator

set_option linter.unusedSectionVars false
set_option maxHeartbeats 1000000

/-! ### Section A — instruments over an arbitrary finite outcome index -/

section General

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- Instrument data over an arbitrary finite index, the first entry's predicate with the index
generalized so that composition can use a product index. -/
def IsQInstrJ {J : Type} [Fintype J] (β : J → Quasilocal ι Q) : Prop :=
  ∑ k, star (β k) * β k = 1

/-- Finite support over an arbitrary finite index. -/
def IsFSJ {J : Type} [Fintype J] (β : J → Quasilocal ι Q) : Prop :=
  ∃ Λ : Finset ι, ∀ k, β k ∈ Set.range (stage Λ)

/-- The total map over an arbitrary finite index. -/
noncomputable def qTotalJ {J : Type} [Fintype J] (β : J → Quasilocal ι Q) (z : Quasilocal ι Q) :
    Quasilocal ι Q :=
  ∑ k, star (β k) * z * β k

/-- One branch over an arbitrary finite index. -/
noncomputable def qBranchJ {J O : Type} [Fintype J] [DecidableEq O] (β : J → Quasilocal ι Q)
    (out : J → O) (x : O) (z : Quasilocal ι Q) : Quasilocal ι Q :=
  ∑ k ∈ Finset.univ.filter (fun k => out k = x), star (β k) * z * β k

/-- On `Fin n` the generalized predicates are the first entry's. -/
theorem isQInstrJ_fin {n : ℕ} (β : Fin n → Quasilocal ι Q) :
    IsQInstrJ β ↔ IsQInstrument β := Iff.rfl

theorem isFSJ_fin {n : ℕ} (β : Fin n → Quasilocal ι Q) :
    IsFSJ β ↔ IsFiniteSupport β := Iff.rfl

theorem qTotalJ_fin {n : ℕ} (β : Fin n → Quasilocal ι Q) (z : Quasilocal ι Q) :
    qTotalJ β z = qTotal β z := rfl

/-- Reindexing the outcome set leaves the total map unchanged. -/
theorem qTotalJ_equiv {J J' : Type} [Fintype J] [Fintype J'] (e : J' ≃ J)
    (β : J → Quasilocal ι Q) (z : Quasilocal ι Q) : qTotalJ (β ∘ e) z = qTotalJ β z := by
  unfold qTotalJ
  simp only [Function.comp_apply]
  exact Equiv.sum_comp e (fun k => star (β k) * z * β k)

theorem isQInstrJ_equiv {J J' : Type} [Fintype J] [Fintype J'] (e : J' ≃ J)
    {β : J → Quasilocal ι Q} (h : IsQInstrJ β) : IsQInstrJ (β ∘ e) := by
  unfold IsQInstrJ at h ⊢
  simp only [Function.comp_apply]
  rw [Equiv.sum_comp e (fun k => star (β k) * β k)]
  exact h

/-- **COARSE-GRAINING**: merging outcomes sums the branches. -/
theorem qBranchJ_coarse {J O O' : Type} [Fintype J] [Fintype O] [DecidableEq O] [DecidableEq O']
    (β : J → Quasilocal ι Q) (out : J → O) (f : O → O') (x' : O') (z : Quasilocal ι Q) :
    qBranchJ β (f ∘ out) x' z
      = ∑ x ∈ Finset.univ.filter (fun x => f x = x'), qBranchJ β out x z := by
  unfold qBranchJ
  symm
  calc ∑ x ∈ Finset.univ.filter (fun x => f x = x'),
          ∑ k ∈ Finset.univ.filter (fun k => out k = x), star (β k) * z * β k
      = ∑ x ∈ Finset.univ.filter (fun x => f x = x'),
          ∑ k ∈ (Finset.univ.filter (fun k => (f ∘ out) k = x')).filter (fun k => out k = x),
            star (β k) * z * β k := by
        refine Finset.sum_congr rfl fun x hx => ?_
        simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hx
        refine Finset.sum_congr ?_ fun _ _ => rfl
        ext k
        simp only [Finset.mem_filter, Finset.mem_univ, true_and, Function.comp_apply]
        constructor
        · intro h2
          exact ⟨by rw [h2, hx], h2⟩
        · rintro ⟨_, h2⟩
          exact h2
    _ = ∑ k ∈ Finset.univ.filter (fun k => (f ∘ out) k = x'), star (β k) * z * β k := by
        refine Finset.sum_fiberwise_of_maps_to (fun k hk => ?_) _
        simp only [Finset.mem_filter, Finset.mem_univ, true_and, Function.comp_apply] at hk ⊢
        exact hk

theorem sum_qBranchJ {J O : Type} [Fintype J] [Fintype O] [DecidableEq O]
    (β : J → Quasilocal ι Q) (out : J → O) (z : Quasilocal ι Q) :
    ∑ x : O, qBranchJ β out x z = qTotalJ β z := by
  unfold qTotalJ qBranchJ
  exact Finset.sum_fiberwise Finset.univ out (fun k => star (β k) * z * β k)

end General

/-! ### Section B — the countermodel theory: availability is finite support -/

section Countermodel

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **THE COUNTERMODEL THEORY.** An operation is available exactly when it is a finite-support
instrument. This is a predicate on the frozen quasilocal algebra: the algebra, its states and its
dynamics are the Level III objects, unmodified. The only thing withheld is availability of
operations that no finite region carries. -/
def AvailFS {J : Type} [Fintype J] (β : J → Quasilocal ι Q) : Prop :=
  IsQInstrJ β ∧ IsFSJ β

/-- **THE IDENTITY OPERATION IS AVAILABLE.** -/
theorem availFS_id : AvailFS (fun _ : Unit => (1 : Quasilocal ι Q)) := by
  constructor
  · unfold IsQInstrJ
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_unit, one_smul, star_one, one_mul]
  · exact ⟨∅, fun _ => ⟨1, map_one _⟩⟩

/-- Membership in one stage is preserved by enlarging the region. -/
theorem mem_range_stage_mono {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') {z : Quasilocal ι Q}
    (hz : z ∈ Set.range (stage Λ)) : z ∈ Set.range (stage Λ') := by
  obtain ⟨X, rfl⟩ := hz
  exact ⟨inclObs h X, stage_inclObs h X⟩

/-- **COMPOSITION IS AVAILABLE.** Running one available operation after another is available, on
the union of their regions. -/
theorem availFS_comp {J J' : Type} [Fintype J] [Fintype J'] {β : J → Quasilocal ι Q}
    {γ : J' → Quasilocal ι Q} (hβ : AvailFS β) (hγ : AvailFS γ) :
    AvailFS (fun p : J × J' => γ p.2 * β p.1) := by
  obtain ⟨hβi, Λ₁, hΛ₁⟩ := hβ
  obtain ⟨hγi, Λ₂, hΛ₂⟩ := hγ
  constructor
  · unfold IsQInstrJ at hβi hγi ⊢
    rw [Fintype.sum_prod_type]
    have hstep : ∀ k : J, (∑ l : J', star (γ l * β k) * (γ l * β k)) = star (β k) * β k := by
      intro k
      have : ∀ l : J', star (γ l * β k) * (γ l * β k)
          = star (β k) * (star (γ l) * γ l) * β k := by
        intro l
        rw [star_mul]
        simp only [mul_assoc]
      simp only [this, ← Finset.sum_mul, ← Finset.mul_sum, hγi, mul_one]
    simp only [hstep]
    exact hβi
  · refine ⟨Λ₁ ∪ Λ₂, fun p => ?_⟩
    obtain ⟨X, hX⟩ := mem_range_stage_mono (Finset.subset_union_left (s₂ := Λ₂)) (hΛ₁ p.1)
    obtain ⟨Y, hY⟩ := mem_range_stage_mono (Finset.subset_union_right (s₁ := Λ₁)) (hΛ₂ p.2)
    exact ⟨Y * X, by rw [map_mul, hX, hY]⟩

/-- **OUTCOME RELABELLING IS AVAILABLE.** -/
theorem availFS_relabel {J J' : Type} [Fintype J] [Fintype J'] (e : J' ≃ J)
    {β : J → Quasilocal ι Q} (hβ : AvailFS β) : AvailFS (β ∘ e) :=
  ⟨isQInstrJ_equiv e hβ.1, by
    obtain ⟨Λ, hΛ⟩ := hβ.2
    exact ⟨Λ, fun k => hΛ (e k)⟩⟩

/-- **THE FROZEN DYNAMICS PRESERVES AVAILABILITY.** The Level III Heisenberg action carries an
available operation to an available operation, on the hat region. -/
theorem availFS_dyn {J : Type} [Fintype J] (Φ : ReversibleDynamics ι Q)
    {β : J → Quasilocal ι Q} (hβ : AvailFS β) : AvailFS (fun k => heisQ Φ (β k)) := by
  obtain ⟨hβi, Λ, hΛ⟩ := hβ
  constructor
  · unfold IsQInstrJ at hβi ⊢
    have h : ∀ k, star (heisQ Φ (β k)) * heisQ Φ (β k)
        = heisEquiv Φ (star (β k) * β k) := by
      intro k
      rw [map_mul, map_star]
      rfl
    simp only [h, ← map_sum, hβi, map_one]
  · refine ⟨hat Φ Λ, fun k => ?_⟩
    obtain ⟨X, hX⟩ := hΛ k
    exact ⟨transported Φ Λ X, by rw [← heisQ_stage, hX]⟩

/-- **EVERY FINITE-REGION ENDOMORPHIC KRAUS INSTRUMENT IS AVAILABLE.** These are the operations the
Level II theory supplies inside the fixed-carrier quasilocal interface. The typed
attachment/discard structure of Level II changes the carrier and is not expressible by this
predicate; it stays separately frozen and unchanged, neither modelled nor withheld here. -/
theorem availFS_of_kraus {n : ℕ} (Λ : Finset ι) (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (hK : ∑ k, (K k)ᴴ * K k = 1) : AvailFS (fun k => stage Λ (K k)) :=
  qInstrument_of_kraus Λ K hK

/-- Conversely every available operation is a finite-region Kraus instrument. -/
theorem kraus_of_availFS {J : Type} [Fintype J] {β : J → Quasilocal ι Q} (hβ : AvailFS β) :
    ∃ (Λ : Finset ι) (K : J → Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      (∀ k, β k = stage Λ (K k)) ∧ ∑ k, (K k)ᴴ * K k = 1 := by
  obtain ⟨hβi, Λ, hΛ⟩ := hβ
  choose K hK using hΛ
  refine ⟨Λ, K, fun k => (hK k).symm, ?_⟩
  apply stage_injective Λ
  rw [map_sum, map_one]
  have h : ∀ k, stage Λ ((K k)ᴴ * K k) = star (β k) * β k := by
    intro k
    rw [map_mul, ← Matrix.star_eq_conjTranspose, map_star, hK k]
  simp only [h]
  exact hβi

end Countermodel

/-! ### Section C — the exclusion: no available operation is the all-sites phase map -/

section Exclusion

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- An available operation fixes the observables of a region disjoint from its support. -/
theorem qTotalJ_stage_of_disjoint {J : Type} [Fintype J] {Λ₀ Λ : Finset ι} (hd : Disjoint Λ₀ Λ)
    {K : J → Matrix (Conf Λ₀ Q) (Conf Λ₀ Q) ℂ} (hK : ∑ k, (K k)ᴴ * K k = 1)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    qTotalJ (fun k => stage Λ₀ (K k)) (stage Λ X) = stage Λ X := by
  rw [qTotalJ]
  have hstep : ∀ k, star (stage Λ₀ (K k)) * stage Λ X * stage Λ₀ (K k)
      = stage Λ X * stage Λ₀ ((K k)ᴴ * K k) := by
    intro k
    rw [← map_star, Matrix.star_eq_conjTranspose,
      stage_comm_of_disjoint hd ((K k)ᴴ) X, mul_assoc, ← map_mul]
  simp only [hstep, ← Finset.mul_sum, ← map_sum, hK, map_one, mul_one]

/-- **THE EXCLUSION**: the all-sites phase map is the total map of no available operation, at any
finite outcome index. -/
theorem phaseAll_not_availFS [Infinite ι] [Nontrivial Q] {J : Type} [Fintype J]
    (β : J → Quasilocal ι Q) (hβ : AvailFS β) :
    phaseAllQ (ι := ι) (Q := Q) ≠ qTotalJ β := by
  intro hEq
  obtain ⟨Λ₀, K, hK, hnorm⟩ := kraus_of_availFS hβ
  obtain ⟨j, hj⟩ := Infinite.exists_notMem_finset Λ₀
  set q₀ : Q := Classical.arbitrary Q with hq₀
  obtain ⟨q₁, hq₁⟩ := exists_ne q₀
  set Λ : Finset ι := {j} with hΛ
  set f₀ : Conf Λ Q := fun _ => q₀ with hf₀
  set f₁ : Conf Λ Q := fun _ => q₁ with hf₁
  set E : Matrix (Conf Λ Q) (Conf Λ Q) ℂ := Matrix.single f₀ f₁ (1 : ℂ) with hE
  have hd : Disjoint Λ₀ Λ := by
    rw [Finset.disjoint_singleton_right]
    exact hj
  have hβK : β = fun k => stage Λ₀ (K k) := funext hK
  have h1 : qTotalJ β (stage Λ E) = stage Λ E := by
    rw [hβK]
    exact qTotalJ_stage_of_disjoint hd hnorm E
  have h2 : phaseAllQ (stage Λ E) = stage Λ (wtConj (phaseAll ι Q) Λ E) := phaseAllQ_stage Λ E
  have hne : wtConj (phaseAll ι Q) Λ E ≠ E := by
    intro habs
    have hentry := congrFun (congrFun habs f₀) f₁
    rw [wtConj_apply] at hentry
    have hw₀ : (phaseAll ι Q).wt Λ f₀ = I := by
      show phaseAllWt Λ f₀ = I
      rw [phaseAllWt_singleton]
      unfold siteWt
      rw [if_pos rfl]
    have hw₁ : (phaseAll ι Q).wt Λ f₁ = 1 := by
      show phaseAllWt Λ f₁ = 1
      rw [phaseAllWt_singleton]
      unfold siteWt
      rw [if_neg hq₁]
    have hE01 : E f₀ f₁ = 1 := Matrix.single_apply_same f₀ f₁ 1
    rw [hw₀, hw₁, hE01, star_one, mul_one, mul_one] at hentry
    have him := congrArg Complex.im hentry
    simp at him
  exact hne (stage_injective Λ (by rw [← h2, hEq, h1]))

end Exclusion

/-! ### Section D — the audit summary for the second entry -/

section Summary

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **Q3, DECIDED NEGATIVELY.** The finite-support availability theory sits on the frozen Level III
objects — the same quasilocal algebra, the same states, the same dynamics — contains every
finite-region endomorphic Kraus instrument the Level II theory supplies inside this fixed-carrier
interface, and is closed under the identity, composition, outcome relabelling, outcome
coarse-graining and the frozen OI-induced dynamics; yet the all-sites phase map is the total map of
no available operation. The current frozen structure together with finite-support quasilocal
availability therefore does not entail the availability of genuinely infinite-support coherent
operations, within this fixed-algebra operational interface. -/
theorem q3_countermodel [Infinite ι] [Nontrivial Q] (Φ : ReversibleDynamics ι Q) :
    AvailFS (fun _ : Unit => (1 : Quasilocal ι Q))
    ∧ (∀ (n : ℕ) (Λ : Finset ι) (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        ∑ k, (K k)ᴴ * K k = 1 → AvailFS (fun k => stage Λ (K k)))
    ∧ (∀ (J J' : Type) (_ : Fintype J) (_ : Fintype J') (β : J → Quasilocal ι Q)
        (γ : J' → Quasilocal ι Q), AvailFS β → AvailFS γ →
        AvailFS (fun p : J × J' => γ p.2 * β p.1))
    ∧ (∀ (J J' : Type) (_ : Fintype J) (_ : Fintype J') (e : J' ≃ J) (β : J → Quasilocal ι Q),
        AvailFS β → AvailFS (β ∘ e))
    ∧ (∀ (J : Type) (_ : Fintype J) (β : J → Quasilocal ι Q), AvailFS β →
        AvailFS (fun k => heisQ Φ (β k)))
    ∧ (∀ (J : Type) (_ : Fintype J) (β : J → Quasilocal ι Q), AvailFS β →
        phaseAllQ (ι := ι) (Q := Q) ≠ qTotalJ β) := by
  refine ⟨availFS_id, fun _ Λ K hK => availFS_of_kraus Λ K hK, ?_, ?_, ?_, ?_⟩
  · intro J J' _ _ β γ hβ hγ
    exact availFS_comp hβ hγ
  · intro J J' _ _ e β hβ
    exact availFS_relabel e hβ
  · intro J _ β hβ
    exact availFS_dyn Φ hβ
  · intro J _ β hβ
    exact phaseAll_not_availFS β hβ

/-- The frozen Level III state layer is untouched by the countermodel: **every** consistent family
of density matrices still extends to a state of the same algebra, with the same values on the
finite stages. Not merely the reference family — the whole state layer. -/
theorem states_untouched (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (hρ : IsStateFamily ρ) :
    IsState (quasiState hρ)
    ∧ ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
        quasiState hρ (stage Λ X) = (X * ρ Λ).trace :=
  ⟨quasiState_isState hρ, quasiState_stage hρ⟩

/-- The frozen Level III dynamics is untouched: it is still an isometric star map of the same
algebra. -/
theorem dynamics_untouched (Φ : ReversibleDynamics ι Q) :
    (∀ z w : Quasilocal ι Q, heisQ Φ (z * w) = heisQ Φ z * heisQ Φ w)
    ∧ (∀ z : Quasilocal ι Q, ‖heisQ Φ z‖ = ‖z‖)
    ∧ (∀ z : Quasilocal ι Q, heisQ Φ.inv (heisQ Φ z) = z) :=
  ⟨heisQ_mul Φ, norm_heisQ Φ, heisQ_inv_heisQ Φ⟩

end Summary

#print axioms isQInstrJ_fin
#print axioms isFSJ_fin
#print axioms qTotalJ_fin
#print axioms qTotalJ_equiv
#print axioms isQInstrJ_equiv
#print axioms qBranchJ_coarse
#print axioms sum_qBranchJ
#print axioms availFS_id
#print axioms mem_range_stage_mono
#print axioms availFS_comp
#print axioms availFS_relabel
#print axioms availFS_dyn
#print axioms availFS_of_kraus
#print axioms kraus_of_availFS
#print axioms qTotalJ_stage_of_disjoint
#print axioms phaseAll_not_availFS
#print axioms q3_countermodel
#print axioms states_untouched
#print axioms dynamics_untouched

end InstrumentAvailability
end OIBridge
