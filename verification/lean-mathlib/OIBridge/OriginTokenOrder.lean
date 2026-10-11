import OIBridge.CompositionOrder
import OIBridge.RouteB
import OIBridge.ManuscriptAxioms
import OIBridge.LiftAudit
import OIBridge.DiscreteCompletion
import Mathlib.Topology.Instances.Matrix

/-!
# Origin token order — design module of the research thread `research/origin` (round 4, O11)

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It states, in the kernel's vocabulary, whether the stated access supplies an operation datum
of infinite order on the completed body of one token, and decides it.

* **The token body** (`cfg`, `Reach`, `body`): the configuration states; the normalized branches of
  every instrument-realized family of a class (`InstAvail`: one isometric step, native readouts,
  coarse-graining, feed-forward, the discard of uniformly attached ancillas, with the class closed
  under products, scalars, projectors and ancilla blocks) applied to a configuration state; the
  closed convex hull of those states in `Matrix T T ℂ`.
* **The data** (`conjAff`, `availData`): the available unitary conjugations, as real affine
  automorphisms of `Matrix T T ℂ`. ORD∞ on the token body is the kernel's `CompositionOrder.OrdInf`.
* **The stated access has no datum of infinite order on the token body**
  (`reach_diag_of_submonomial`, `finiteOrderOn_of_reach_diag`, `not_ordInf_of_reach_diag`;
  instances `substratum_not_ordInf`, `permClass_not_ordInf`, `substratumTheory_datum_finiteOrderOn`):
  every reachable state is configuration-diagonal, every available unitary carries configuration
  states to configuration states, and a common period of the configuration states
  (`CompositionOrder.exists_return`, `CompositionOrder.exists_common_period`) fixes the whole body.
* **Necessity** (`exists_nonsubmonomial_of_ordInf`): ORD∞ on the token body puts an operator that is
  not submonomial into the class at the token's carrier.
* **The frame-axis rotation** (`framePhase`, `framePhase_avail_substratum`,
  `framePhase_trivial_on_substratum_body`, `framePhase_infiniteOrderOn`,
  `framePhase_infiniteOrderOn_univ`, `framePhase_crosses_stages`): the diagonal unitary with `exp i` at
  one configuration is available in the substratum theory and acts as the identity on its token body;
  it has infinite order on every set containing a state with a nonzero entry between that
  configuration and another, and no finite set containing such a state is carried into itself.
* **The equivalence, one direction at a time** (`coherent_of_ordInf`, `ordInf_of_coherent`,
  `ordInf_iff_coherent`, `ordInf_iff_coherent_of_extends`): ORD∞ on the token body implies a coherent
  state in it, for every class; a coherent state implies ORD∞ for every class containing the frame
  phases at the carrier, in particular every class containing the substratum class there.
* **Control** (`fullClass_coherent`, `fullClass_ordInf`): on the full class ORD∞ holds on the token
  body, so the predicate is not vacuous.
* **What the obstruction satisfies** (`substratum_obstruction`, `obsTheory_obstruction`): the
  substratum theory satisfies `DerivedOICore`, its class is structurally closed and
  configuration-level and it carries the substratum's availability; the observer theory of every
  kernel substratum satisfies the sourced closure, its substratum A1 and A2; and in both the token
  body admits no datum of infinite order.
-/

namespace OIBridge
namespace OriginTokenOrder

open scoped Matrix

/-! ### Section A — configuration states, the diagonal matrices, the token body, the data -/

section Defs

variable {T : Type} [Fintype T] [DecidableEq T]

/-- The configuration state `|s⟩⟨s|`. -/
def cfg (s : T) : Matrix T T ℂ := Matrix.of fun p q => if p = s ∧ q = s then 1 else 0

theorem cfg_apply (s p q : T) : cfg s p q = if p = s ∧ q = s then 1 else 0 := rfl

/-- The configuration-diagonal matrices. -/
def Diag : Set (Matrix T T ℂ) := {X | ∀ p q, p ≠ q → X p q = 0}

end Defs

/-- **The states reachable from a configuration**: a branch of nonzero weight of any family that the
class instrument-realizes, applied to a configuration state and normalized. Feed-forward (`bind`)
makes every later protocol, and conditioning on its outcomes, part of one family. -/
def Reach (𝓘 : InterventionLocality.ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] :
    Set (Matrix T T ℂ) :=
  {ρ | ∃ (O : Type) (_ : Fintype O) (_ : DecidableEq O)
      (F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) (a : O) (s : T),
      InterventionLocality.InstAvail 𝓘 T O F ∧ (F a (cfg s)).trace ≠ 0 ∧
        ρ = ((F a (cfg s)).trace)⁻¹ • F a (cfg s)}

/-- **The completed body of the token**: the closed convex hull of the reachable states. -/
def body (𝓘 : InterventionLocality.ImplementationClass) (T : Type) [Fintype T] [DecidableEq T] :
    Set (Matrix T T ℂ) :=
  closure (convexHull ℝ (Reach 𝓘 T))

/-- Conjugation by a unitary, as a real affine automorphism of the matrices. -/
noncomputable def conjAff {T : Type} [Fintype T] [DecidableEq T] (U : Matrix T T ℂ)
    (hU : Uᴴ * U = 1) : Matrix T T ℂ ≃ᵃ[ℝ] Matrix T T ℂ :=
  LinearEquiv.toAffineEquiv
    { toFun := fun X => U * X * Uᴴ
      invFun := fun X => Uᴴ * X * U
      map_add' := fun X Y => by
        show U * (X + Y) * Uᴴ = U * X * Uᴴ + U * Y * Uᴴ
        rw [Matrix.mul_add, Matrix.add_mul]
      map_smul' := fun c X => by
        show U * (c • X) * Uᴴ = (RingHom.id ℝ) c • (U * X * Uᴴ)
        rw [Matrix.mul_smul, Matrix.smul_mul, RingHom.id_apply]
      left_inv := fun X => by
        show Uᴴ * (U * X * Uᴴ) * U = X
        calc Uᴴ * (U * X * Uᴴ) * U = (Uᴴ * U) * X * (Uᴴ * U) := by simp only [Matrix.mul_assoc]
          _ = X := by rw [hU, Matrix.one_mul, Matrix.mul_one]
      right_inv := fun X => by
        show U * (Uᴴ * X * U) * Uᴴ = X
        have hU' : U * Uᴴ = 1 := mul_eq_one_comm.mp hU
        calc U * (Uᴴ * X * U) * Uᴴ = (U * Uᴴ) * X * (U * Uᴴ) := by simp only [Matrix.mul_assoc]
          _ = X := by rw [hU', Matrix.one_mul, Matrix.mul_one] }

/-- **The available data**: the conjugations by unitaries whose channel the class
instrument-realizes on the carrier. -/
def availData (𝓘 : InterventionLocality.ImplementationClass) (T : Type) [Fintype T]
    [DecidableEq T] : Set (Matrix T T ℂ ≃ᵃ[ℝ] Matrix T T ℂ) :=
  {g | ∃ (U : Matrix T T ℂ) (hU : Uᴴ * U = 1),
    InterventionLocality.InstAvail 𝓘 T Unit (fun _ => MonoidalCompletion.conjChannel U) ∧
      g = conjAff U hU}

/-- A set of states is **coherent** when one of its states has a nonzero entry between two
distinct configurations. -/
def Coherent {T : Type} (Ω : Set (Matrix T T ℂ)) : Prop :=
  ∃ X ∈ Ω, ∃ s t : T, s ≠ t ∧ X s t ≠ 0

/-- **The frame phase on the configuration `t`**: `exp i` at `t`, one elsewhere. Its conjugation
rotates the coherence between `t` and every other configuration by one radian. -/
noncomputable def framePhase {T : Type} [DecidableEq T] (t : T) : Matrix T T ℂ :=
  Matrix.diagonal fun r => if r = t then Complex.exp Complex.I else 1

/-! ### Section B — entries, closedness, the iterates of a conjugation -/

section Lemmas

variable {T : Type} [Fintype T] [DecidableEq T]

theorem trace_cfg (s : T) : (cfg s).trace = 1 := by
  unfold Matrix.trace
  rw [Finset.sum_eq_single s]
  · rw [Matrix.diag_apply, cfg_apply, if_pos ⟨rfl, rfl⟩]
  · intro b _ hb
    rw [Matrix.diag_apply, cfg_apply, if_neg (fun h => hb h.1)]
  · intro h
    exact absurd (Finset.mem_univ s) h

theorem mul_cfg_apply (K : Matrix T T ℂ) (s p j : T) :
    (K * cfg s) p j = if j = s then K p s else 0 := by
  rw [Matrix.mul_apply]
  by_cases hj : j = s
  · rw [if_pos hj, Finset.sum_eq_single s]
    · rw [cfg_apply, if_pos ⟨rfl, hj⟩, mul_one]
    · intro k _ hk
      rw [cfg_apply, if_neg (fun h => hk h.1), mul_zero]
    · intro h
      exact absurd (Finset.mem_univ s) h
  · rw [if_neg hj]
    exact Finset.sum_eq_zero fun k _ => by rw [cfg_apply, if_neg (fun h => hj h.2), mul_zero]

/-- The entries of a conjugated configuration state. -/
theorem conj_cfg_apply (K : Matrix T T ℂ) (s p q : T) :
    (K * cfg s * Kᴴ) p q = K p s * star (K q s) := by
  rw [Matrix.mul_apply, Finset.sum_eq_single s]
  · rw [mul_cfg_apply, if_pos rfl, Matrix.conjTranspose_apply]
  · intro j _ hj
    rw [mul_cfg_apply, if_neg hj, zero_mul]
  · intro h
    exact absurd (Finset.mem_univ s) h

theorem trace_conj {U : Matrix T T ℂ} (hU : Uᴴ * U = 1) (X : Matrix T T ℂ) :
    (U * X * Uᴴ).trace = X.trace := by
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, hU, Matrix.one_mul]

theorem isClosed_diag : IsClosed (Diag (T := T)) := by
  have h : (Diag (T := T)) = ⋂ p : T, ⋂ q : T, {X : Matrix T T ℂ | p ≠ q → X p q = 0} := by
    ext X
    simp [Diag]
  rw [h]
  refine isClosed_iInter fun p => isClosed_iInter fun q => ?_
  by_cases hpq : p = q
  · have h1 : {X : Matrix T T ℂ | p ≠ q → X p q = 0} = Set.univ := by
      ext X
      simp [hpq]
    rw [h1]
    exact isClosed_univ
  · have h1 : {X : Matrix T T ℂ | p ≠ q → X p q = 0} = {X | X p q = 0} := by
      ext X
      simp [hpq]
    rw [h1]
    exact isClosed_eq (continuous_id.matrix_elem p q) continuous_const

theorem convex_diag : Convex ℝ (Diag (T := T)) := by
  intro X hX Y hY a b _ _ _ p q hpq
  rw [Matrix.add_apply, Matrix.smul_apply, Matrix.smul_apply, hX p q hpq, hY p q hpq, smul_zero,
    smul_zero, add_zero]

theorem reach_subset_body (𝓘 : InterventionLocality.ImplementationClass) :
    Reach 𝓘 T ⊆ body 𝓘 T :=
  fun _ hx => subset_closure (subset_convexHull ℝ _ hx)

/-- A body whose reachable states are configuration-diagonal is configuration-diagonal. -/
theorem body_subset_diag {𝓘 : InterventionLocality.ImplementationClass}
    (hR : Reach 𝓘 T ⊆ Diag) : body 𝓘 T ⊆ Diag :=
  closure_minimal (convexHull_min hR convex_diag) isClosed_diag

theorem conjAff_apply (U : Matrix T T ℂ) (hU : Uᴴ * U = 1) (X : Matrix T T ℂ) :
    conjAff U hU X = U * X * Uᴴ := rfl

/-- The iterates of a conjugation are the conjugations by the powers. -/
theorem conjAff_iterate (U : Matrix T T ℂ) (hU : Uᴴ * U = 1) (N : ℕ) (X : Matrix T T ℂ) :
    (⇑(conjAff U hU))^[N] X = U ^ N * X * (U ^ N)ᴴ := by
  induction N with
  | zero =>
    rw [Function.iterate_zero_apply, pow_zero, Matrix.conjTranspose_one, Matrix.one_mul,
      Matrix.mul_one]
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih, conjAff_apply, pow_succ', Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]

/-- A configuration-diagonal matrix is the combination of the configuration states with its
diagonal entries. -/
theorem diag_eq_sum {X : Matrix T T ℂ} (hX : X ∈ Diag) : X = ∑ s, X s s • cfg s := by
  ext p q
  rw [Matrix.sum_apply]
  by_cases hpq : p = q
  · rw [← hpq, Finset.sum_eq_single p]
    · rw [Matrix.smul_apply, cfg_apply, if_pos ⟨rfl, rfl⟩, smul_eq_mul, mul_one]
    · intro b _ hb
      rw [Matrix.smul_apply, cfg_apply, if_neg (fun h => hb h.1.symm), smul_zero]
    · intro h
      exact absurd (Finset.mem_univ p) h
  · rw [hX p q hpq]
    symm
    refine Finset.sum_eq_zero fun s _ => ?_
    rw [Matrix.smul_apply, cfg_apply, if_neg (fun h => hpq (h.1.trans h.2.symm)), smul_zero]

/-- **A unitary that carries a configuration state to a configuration-diagonal state carries it to
a configuration state**: the image is a rank-one projector, and a diagonal rank-one projector has one
nonzero entry. -/
theorem eq_cfg_of_diag {U : Matrix T T ℂ} (hU : Uᴴ * U = 1) (s : T)
    (h : U * cfg s * Uᴴ ∈ Diag) : ∃ t, U * cfg s * Uᴴ = cfg t := by
  have hcol : ∑ p, Uᴴ s p * U p s = 1 := by
    have h1 := congrFun (congrFun hU s) s
    rwa [Matrix.mul_apply, Matrix.one_apply_eq] at h1
  obtain ⟨t, ht⟩ : ∃ t, U t s ≠ 0 := by
    by_contra hall
    push Not at hall
    have hz : ∑ p, Uᴴ s p * U p s = 0 := Finset.sum_eq_zero fun p _ => by rw [hall p, mul_zero]
    rw [hz] at hcol
    exact zero_ne_one hcol
  have hother : ∀ p, p ≠ t → U p s = 0 := by
    intro p hp
    have h2 := h p t hp
    rw [conj_cfg_apply] at h2
    rcases mul_eq_zero.mp h2 with h3 | h3
    · exact h3
    · exact absurd (star_eq_zero.mp h3) ht
  have hnorm : Uᴴ s t * U t s = 1 := by
    have hsum : ∑ p, Uᴴ s p * U p s = Uᴴ s t * U t s :=
      Finset.sum_eq_single t (fun p _ hp => by rw [hother p hp, mul_zero])
        (fun h' => absurd (Finset.mem_univ t) h')
    rw [← hsum]
    exact hcol
  refine ⟨t, ?_⟩
  ext p q
  rw [conj_cfg_apply, cfg_apply]
  by_cases hp : p = t
  · by_cases hq : q = t
    · rw [hp, hq, if_pos ⟨rfl, rfl⟩, mul_comm, ← Matrix.conjTranspose_apply]
      exact hnorm
    · rw [hother q hq, star_zero, mul_zero, if_neg (fun h' => hq h'.2)]
  · rw [hother p hp, zero_mul, if_neg (fun h' => hp h'.1)]

/-- The image of a configuration state under an available unitary is a reachable state. -/
theorem conj_cfg_mem_reach {𝓘 : InterventionLocality.ImplementationClass} {U : Matrix T T ℂ}
    (hU : Uᴴ * U = 1)
    (hav : InterventionLocality.InstAvail 𝓘 T Unit (fun _ => MonoidalCompletion.conjChannel U))
    (s : T) : U * cfg s * Uᴴ ∈ Reach 𝓘 T := by
  have htr : (MonoidalCompletion.conjChannel U (cfg s)).trace = 1 := by
    rw [AncillaClosure.conjChannel_apply, trace_conj hU, trace_cfg]
  refine ⟨Unit, inferInstance, inferInstance, fun _ => MonoidalCompletion.conjChannel U, (), s, hav,
    ?_, ?_⟩
  · try dsimp only
    rw [htr]
    exact one_ne_zero
  · try dsimp only
    rw [htr, inv_one, one_smul, AncillaClosure.conjChannel_apply]

end Lemmas

/-! ### Section C — finite order on a configuration-diagonal body; the stated access -/

section Finite

variable {T : Type} [Fintype T] [DecidableEq T]

/-- **Every available unitary datum has finite order on a configuration-diagonal body.** It carries
each configuration state to a configuration state, injectively, so the configuration states return
together after a common period, and the period fixes every diagonal matrix. -/
theorem finiteOrderOn_of_reach_diag {𝓘 : InterventionLocality.ImplementationClass}
    (hR : Reach 𝓘 T ⊆ Diag) {U : Matrix T T ℂ} (hU : Uᴴ * U = 1)
    (hav : InterventionLocality.InstAvail 𝓘 T Unit (fun _ => MonoidalCompletion.conjChannel U)) :
    CompositionOrder.FiniteOrderOn (body 𝓘 T) (conjAff U hU) := by
  classical
  have hcfg : ∀ s, ∃ t, U * cfg s * Uᴴ = cfg t := fun s =>
    eq_cfg_of_diag hU s (hR (conj_cfg_mem_reach hU hav s))
  have hmaps : ∀ w ∈ Finset.univ.image (cfg (T := T)),
      (conjAff U hU) w ∈ Finset.univ.image (cfg (T := T)) := by
    intro w hw
    obtain ⟨s, -, rfl⟩ := Finset.mem_image.1 hw
    obtain ⟨t, ht⟩ := hcfg s
    rw [conjAff_apply, ht]
    exact Finset.mem_image_of_mem _ (Finset.mem_univ t)
  obtain ⟨N, hN, hNS⟩ := CompositionOrder.exists_common_period (Finset.univ.image (cfg (T := T)))
    (fun w hw => CompositionOrder.exists_return (conjAff U hU).injective hmaps hw)
  have hfix : ∀ s, U ^ N * cfg s * (U ^ N)ᴴ = cfg s := fun s => by
    have h := hNS (cfg s) (Finset.mem_image_of_mem _ (Finset.mem_univ s))
    rwa [conjAff_iterate] at h
  refine ⟨N, hN, fun X hX => ?_⟩
  have hXd : X ∈ Diag := body_subset_diag hR hX
  rw [conjAff_iterate]
  calc U ^ N * X * (U ^ N)ᴴ = U ^ N * (∑ s, X s s • cfg s) * (U ^ N)ᴴ := by
        rw [← diag_eq_sum hXd]
    _ = ∑ s, X s s • (U ^ N * cfg s * (U ^ N)ᴴ) := by
        rw [Matrix.mul_sum, Matrix.sum_mul]
        refine Finset.sum_congr rfl fun s _ => ?_
        rw [Matrix.mul_smul, Matrix.smul_mul]
    _ = ∑ s, X s s • cfg s := by simp only [hfix]
    _ = X := (diag_eq_sum hXd).symm

/-- **No datum of infinite order on a configuration-diagonal body.** -/
theorem not_ordInf_of_reach_diag {𝓘 : InterventionLocality.ImplementationClass}
    (hR : Reach 𝓘 T ⊆ Diag) : ¬ CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) := by
  rintro ⟨g, ⟨U, hU, hav, rfl⟩, hinf⟩
  exact CompositionOrder.not_infiniteOrderOn_of_finiteOrderOn
    (finiteOrderOn_of_reach_diag hR hU hav) hinf

/-- A submonomial operator carries a configuration state to a configuration-diagonal matrix. -/
theorem conj_cfg_diag_of_submonomial {K : Matrix T T ℂ}
    (hK : StructuralClosure.IsSubmonomial K) (s : T) : K * cfg s * Kᴴ ∈ Diag := by
  intro p q hpq
  rw [conj_cfg_apply]
  by_cases hp : K p s = 0
  · rw [hp, zero_mul]
  · by_cases hq : K q s = 0
    · rw [hq, star_zero, mul_zero]
    · exact absurd (hK.2 p q s hp hq) hpq

/-- **Every reachable state of a submonomial architecture is configuration-diagonal**, by every
route of `InstAvail`: each branch is a finite sum of conjugations by members of the class
(`realized_of_instAvail`), ancilla blocks included. -/
theorem reach_diag_of_submonomial {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hsub : ∀ K : Matrix T T ℂ, 𝓘 T K → StructuralClosure.IsSubmonomial K) :
    Reach 𝓘 T ⊆ Diag := by
  rintro ρ ⟨O, _, _, F, a, s, hF, -, rfl⟩
  obtain ⟨ι, _, K, hFa, hK⟩ := InterventionLocality.realized_of_instAvail arch hF a
  have hz : ∀ i, MonoidalCompletion.conjChannel (K i) (cfg s) ∈ Diag := fun i => by
    rw [AncillaClosure.conjChannel_apply]
    exact conj_cfg_diag_of_submonomial (hsub _ (hK i)) s
  intro p q hpq
  rw [Matrix.smul_apply, hFa, LinearMap.sum_apply, Matrix.sum_apply,
    Finset.sum_eq_zero (fun i _ => hz i p q hpq), smul_zero]

/-- The reachable states of the substratum class are configuration-diagonal. -/
theorem substratum_reach_diag : Reach StructuralClosure.substratumClass T ⊆ Diag :=
  reach_diag_of_submonomial StructuralClosure.substratumClass_arch
    (fun _ hK => StructuralClosure.monomial_submonomial hK)

/-- The reachable states of the sourced class of scaled partial permutations are
configuration-diagonal. -/
theorem permClass_reach_diag : Reach SubstratumInterfaceAudit.permClass T ⊆ Diag :=
  reach_diag_of_submonomial SubstratumInterfaceAudit.permClass_arch
    (fun K hK => (show SubstratumInterfaceAudit.IsScaledPartialPerm K from hK).1)

/-- **The stated access: no datum of infinite order on the token body.** -/
theorem substratum_not_ordInf :
    ¬ CompositionOrder.OrdInf (body StructuralClosure.substratumClass T)
      (availData StructuralClosure.substratumClass T) :=
  not_ordInf_of_reach_diag substratum_reach_diag

/-- The same for the sourced class of scaled partial permutations. -/
theorem permClass_not_ordInf :
    ¬ CompositionOrder.OrdInf (body SubstratumInterfaceAudit.permClass T)
      (availData SubstratumInterfaceAudit.permClass T) :=
  not_ordInf_of_reach_diag permClass_reach_diag

/-- **In the substratum theory, at every level, every available unitary datum has finite order on
the token body** (the carrier `Fin 2 × Fin n`, availability `availExt n`). -/
theorem substratumTheory_datum_finiteOrderOn (n : ℕ)
    {U : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ} (hU : Uᴴ * U = 1)
    (hav : (RouteB.substratumTheory (Fin 2)).availExt n Unit
      (fun _ => MonoidalCompletion.conjChannel U)) :
    CompositionOrder.FiniteOrderOn (body StructuralClosure.substratumClass (Fin 2 × Fin n))
      (conjAff U hU) :=
  finiteOrderOn_of_reach_diag substratum_reach_diag hU hav

/-- **Necessity**: ORD∞ on the token body puts an operator that is not submonomial into the class at
the token's carrier. -/
theorem exists_nonsubmonomial_of_ordInf {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (h : CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T)) :
    ∃ K : Matrix T T ℂ, 𝓘 T K ∧ ¬ StructuralClosure.IsSubmonomial K := by
  by_contra hne
  push Not at hne
  exact not_ordInf_of_reach_diag (reach_diag_of_submonomial arch hne) h

end Finite

/-! ### Section D — the frame-axis rotation -/

section Frame

variable {T : Type} [Fintype T] [DecidableEq T]

theorem star_exp_I : star (Complex.exp Complex.I) = Complex.exp (-Complex.I) := by
  have h := Complex.exp_conj Complex.I
  rw [Complex.conj_I, starRingEnd_apply] at h
  exact h.symm

/-- No positive power of `exp i` is one: `π` is irrational. -/
theorem expI_pow_ne_one {m : ℕ} (hm : 1 ≤ m) : Complex.exp Complex.I ^ m ≠ 1 := by
  intro h
  rw [← Complex.exp_nat_mul] at h
  have h0 : Real.cos (m : ℝ) = 1 := by
    have h1 := congrArg Complex.re h
    rwa [← Complex.ofReal_natCast, Complex.exp_ofReal_mul_I_re, Complex.one_re] at h1
  obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff _).mp h0
  have hmpos : (0 : ℝ) < m := by exact_mod_cast hm
  have hn0 : (n : ℝ) ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at hn
    linarith
  apply irrational_pi.ne_rat ((m : ℚ) / (2 * n))
  push_cast
  field_simp
  linear_combination hn

theorem framePhase_entry_unit (t r : T) :
    star (if r = t then Complex.exp Complex.I else 1) * (if r = t then Complex.exp Complex.I else 1)
      = 1 := by
  by_cases hr : r = t
  · rw [if_pos hr, star_exp_I, ← Complex.exp_add, neg_add_cancel, Complex.exp_zero]
  · rw [if_neg hr, star_one, one_mul]

theorem framePhase_unitary (t : T) : (framePhase t)ᴴ * framePhase t = 1 := by
  rw [framePhase, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal,
    ← Matrix.diagonal_one]
  congr 1
  funext r
  exact framePhase_entry_unit t r

/-- The frame phase is a monomial operator: the substratum class contains it. -/
theorem framePhase_mem_substratumClass (t : T) :
    StructuralClosure.substratumClass T (framePhase t) := by
  unfold framePhase
  exact SubstratumInterface.monomial_diagonal _

/-- **The frame-axis rotation is available on the stated access.** -/
theorem framePhase_avail_substratum (t : T) :
    (RouteB.substratumTheory T).avail Unit
      (fun _ => MonoidalCompletion.conjChannel (framePhase t)) :=
  InterventionLocality.InstAvail.op _ (framePhase_mem_substratumClass t) (framePhase_unitary t)

/-- The frame phase fixes every configuration-diagonal matrix. -/
theorem framePhase_fixes_diag (t : T) {X : Matrix T T ℂ} (hX : X ∈ Diag) :
    framePhase t * X * (framePhase t)ᴴ = X := by
  ext p q
  rw [framePhase, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    Pi.star_apply]
  by_cases hpq : p = q
  · rw [← hpq]
    linear_combination X p p * framePhase_entry_unit t p
  · rw [hX p q hpq, mul_zero, zero_mul]

/-- **On the stated access the frame-axis rotation acts as the identity on the token body.** -/
theorem framePhase_trivial_on_substratum_body (t : T) :
    ∀ X ∈ body StructuralClosure.substratumClass T,
      conjAff (framePhase t) (framePhase_unitary t) X = X := fun X hX => by
  rw [conjAff_apply]
  exact framePhase_fixes_diag t (body_subset_diag substratum_reach_diag hX)

/-- The entry between `s` and `t` of the iterates of the frame phase. -/
theorem framePhase_iterate_entry (t s : T) (hst : s ≠ t) (m : ℕ) (X : Matrix T T ℂ) :
    ((⇑(conjAff (framePhase t) (framePhase_unitary t)))^[m] X) s t
      = X s t * star (Complex.exp Complex.I ^ m) := by
  rw [conjAff_iterate, framePhase, Matrix.diagonal_pow, Matrix.diagonal_conjTranspose,
    Matrix.mul_diagonal, Matrix.diagonal_mul, Pi.star_apply, Pi.pow_apply, Pi.pow_apply,
    if_neg hst, if_pos rfl, one_pow, one_mul]

/-- **The frame phase has infinite order on every set containing a state with a nonzero entry
between `t` and another configuration.** -/
theorem framePhase_infiniteOrderOn {Ω : Set (Matrix T T ℂ)} {X : Matrix T T ℂ} (hX : X ∈ Ω)
    {s t : T} (hst : s ≠ t) (hXst : X s t ≠ 0) :
    CompositionOrder.InfiniteOrderOn Ω (conjAff (framePhase t) (framePhase_unitary t)) := by
  intro m hm
  refine ⟨X, hX, fun h => ?_⟩
  have h1 := congrFun (congrFun h s) t
  rw [framePhase_iterate_entry t s hst m X] at h1
  have h2 : star (Complex.exp Complex.I ^ m) = 1 :=
    mul_left_cancel₀ hXst (h1.trans (mul_one (X s t)).symm)
  have h3 : Complex.exp Complex.I ^ m = 1 := by
    have h4 := congrArg star h2
    rwa [star_star, star_one] at h4
  exact expI_pow_ne_one hm h3

/-- **The frame phase has infinite order on the full matrix algebra.** -/
theorem framePhase_infiniteOrderOn_univ {s t : T} (hst : s ≠ t) :
    CompositionOrder.InfiniteOrderOn (Set.univ : Set (Matrix T T ℂ))
      (conjAff (framePhase t) (framePhase_unitary t)) :=
  framePhase_infiniteOrderOn (Set.mem_univ (Matrix.of fun _ _ => (1 : ℂ))) hst (by simp)

/-- **The frame phase crosses every finite stage holding a coherent state**: no finite set
containing a state with a nonzero entry between `t` and another configuration is carried into
itself (the mechanism of `CompositionOrder.not_stagePreserving_of_infiniteOrderOn`, through
`CompositionOrder.exists_return`). -/
theorem framePhase_crosses_stages {S : Finset (Matrix T T ℂ)} {X : Matrix T T ℂ} (hXS : X ∈ S)
    {s t : T} (hst : s ≠ t) (hXst : X s t ≠ 0) :
    ¬ ∀ Y ∈ S, conjAff (framePhase t) (framePhase_unitary t) Y ∈ S := by
  intro hS
  obtain ⟨p, hp, hpX⟩ := CompositionOrder.exists_return
    (conjAff (framePhase t) (framePhase_unitary t)).injective hS hXS
  obtain ⟨Y, hY, hne⟩ := framePhase_infiniteOrderOn (Set.mem_singleton X) hst hXst p (by omega)
  rw [Set.mem_singleton_iff] at hY
  rw [hY] at hne
  exact hne hpX

end Frame

/-! ### Section E — the equivalence, one direction at a time -/

section Equivalence

variable {T : Type} [Fintype T] [DecidableEq T]

/-- **Direction one, for every class: ORD∞ on the token body implies a coherent state in it.** -/
theorem coherent_of_ordInf {𝓘 : InterventionLocality.ImplementationClass}
    (h : CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T)) : Coherent (body 𝓘 T) := by
  by_contra hne
  apply not_ordInf_of_reach_diag _ h
  intro X hX p q hpq
  by_contra hXpq
  exact hne ⟨X, reach_subset_body 𝓘 hX, p, q, hpq, hXpq⟩

/-- **Direction two, for every class containing the frame phases at the carrier: a coherent state in
the token body implies ORD∞.** -/
theorem ordInf_of_coherent {𝓘 : InterventionLocality.ImplementationClass}
    (hph : ∀ t : T, 𝓘 T (framePhase t)) (h : Coherent (body 𝓘 T)) :
    CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) := by
  obtain ⟨X, hX, s, t, hst, hXst⟩ := h
  exact ⟨conjAff (framePhase t) (framePhase_unitary t),
    ⟨framePhase t, framePhase_unitary t,
      InterventionLocality.InstAvail.op _ (hph t) (framePhase_unitary t), rfl⟩,
    framePhase_infiniteOrderOn hX hst hXst⟩

/-- The equivalence under the phase hypothesis, assembled from the two directions. -/
theorem ordInf_iff_coherent {𝓘 : InterventionLocality.ImplementationClass}
    (hph : ∀ t : T, 𝓘 T (framePhase t)) :
    CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) ↔ Coherent (body 𝓘 T) :=
  ⟨coherent_of_ordInf, ordInf_of_coherent hph⟩

/-- **Every class containing the substratum class at the carrier**: ORD∞ on the token body holds
exactly when the body is coherent. -/
theorem ordInf_iff_coherent_of_extends {𝓘 : InterventionLocality.ImplementationClass}
    (hle : ∀ K : Matrix T T ℂ, StructuralClosure.substratumClass T K → 𝓘 T K) :
    CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) ↔ Coherent (body 𝓘 T) :=
  ordInf_iff_coherent fun t => hle _ (framePhase_mem_substratumClass t)

end Equivalence

/-! ### Section F — the control, and the verdict -/

section Control

/-- **Control: on the full class the token body is coherent** — `rot(π/4)` carries the configuration
`0` to a state with entry `sin(π/4) cos(π/4)` between the two configurations. -/
theorem fullClass_coherent : Coherent (body InterventionLocality.fullClass (Fin 2)) := by
  have hu := DiscreteCompletion.rot_unitary (Real.pi / 4)
  refine ⟨StateMixingCoupling.rot (Real.pi / 4) * cfg 0 * (StateMixingCoupling.rot (Real.pi / 4))ᴴ,
    reach_subset_body _ (conj_cfg_mem_reach hu (InterventionLocality.InstAvail.op _ trivial hu) 0),
    1, 0, by decide, ?_⟩
  rw [conj_cfg_apply]
  have hs : StateMixingCoupling.rot (Real.pi / 4) 1 0 = ((Real.sin (Real.pi / 4) : ℝ) : ℂ) := rfl
  have hc : StateMixingCoupling.rot (Real.pi / 4) 0 0 = ((Real.cos (Real.pi / 4) : ℝ) : ℂ) := rfl
  rw [hs, hc, Real.sin_pi_div_four, Real.cos_pi_div_four]
  have h2 : (Real.sqrt 2 / 2 : ℝ) ≠ 0 := by positivity
  exact mul_ne_zero (Complex.ofReal_ne_zero.mpr h2)
    (star_ne_zero.mpr (Complex.ofReal_ne_zero.mpr h2))

/-- **Control: on the full class ORD∞ holds on the token body.** -/
theorem fullClass_ordInf :
    CompositionOrder.OrdInf (body InterventionLocality.fullClass (Fin 2))
      (availData InterventionLocality.fullClass (Fin 2)) :=
  ordInf_of_coherent (fun _ => trivial) fullClass_coherent

/-- **The obstruction, with what it satisfies.** The substratum theory on the two-state token
satisfies the consequence closure with the sealed OI core (`DerivedOICore`), its class is
structurally closed and configuration-level, it carries the substratum's availability, and no
available datum has infinite order on its token body. -/
theorem substratum_obstruction :
    RouteB.DerivedOICore (RouteB.substratumTheory (Fin 2)) ∧
    StructuralClosure.StructurallyClosed StructuralClosure.substratumClass ∧
    ManuscriptAxioms.ConfigurationLevel StructuralClosure.substratumClass ∧
    LiftAudit.SubstratumAvail (RouteB.substratumTheory (Fin 2)) ∧
    ¬ CompositionOrder.OrdInf (body StructuralClosure.substratumClass (Fin 2))
      (availData StructuralClosure.substratumClass (Fin 2)) :=
  ⟨RouteB.substratumTheory_derivedOICore, StructuralClosure.substratumClass_structurallyClosed,
    ManuscriptAxioms.substratumClass_configurationLevel, LiftAudit.substratumTheory_substratumAvail,
    substratum_not_ordInf⟩

/-- **The observer theory of every kernel substratum** (the sourcing arrow from a substratum to its
operational theory): the substratum satisfies A1 and A2, its observer theory satisfies the sourced
closure, and no available datum has infinite order on the body of its configuration carrier. -/
theorem obsTheory_obstruction (𝒮 : SubstratumInterfaceAudit.Substratum) [Fintype 𝒮.ι]
    [Fintype 𝒮.V] [DecidableEq 𝒮.V] :
    𝒮.A1 ∧ 𝒮.A2 ∧
    SubstratumInterfaceAudit.SourcedOI (SubstratumInterfaceAudit.obsTheory 𝒮) ∧
    ¬ CompositionOrder.OrdInf (body SubstratumInterfaceAudit.permClass 𝒮.Conf)
      (availData SubstratumInterfaceAudit.permClass 𝒮.Conf) :=
  ⟨SubstratumInterfaceAudit.obs_a1 𝒮, 𝒮.a2_every_substratum,
    SubstratumInterfaceAudit.obs_sourcedOI 𝒮, permClass_not_ordInf⟩

/-- **Verdict O11.** On the stated access (the substratum class, and the sourced class of scaled
partial permutations) no available datum has infinite order on the token body, at any carrier; for
every architecture ORD∞ forces an operator that is not submonomial; for every class containing the
frame phases ORD∞ holds exactly when the body is coherent; the frame-axis rotation is available on
the stated access, acts as the identity on its token body and has infinite order on the full matrix
algebra; the full class has ORD∞. -/
theorem o11_core :
    (∀ (T : Type) [Fintype T] [DecidableEq T],
      ¬ CompositionOrder.OrdInf (body StructuralClosure.substratumClass T)
        (availData StructuralClosure.substratumClass T)) ∧
    (∀ (T : Type) [Fintype T] [DecidableEq T],
      ¬ CompositionOrder.OrdInf (body SubstratumInterfaceAudit.permClass T)
        (availData SubstratumInterfaceAudit.permClass T)) ∧
    (∀ (𝓘 : InterventionLocality.ImplementationClass) (T : Type) [Fintype T] [DecidableEq T],
      InterventionLocality.Architecture 𝓘 →
      CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) →
        ∃ K : Matrix T T ℂ, 𝓘 T K ∧ ¬ StructuralClosure.IsSubmonomial K) ∧
    (∀ (𝓘 : InterventionLocality.ImplementationClass) (T : Type) [Fintype T] [DecidableEq T],
      (∀ t : T, 𝓘 T (framePhase t)) →
        (CompositionOrder.OrdInf (body 𝓘 T) (availData 𝓘 T) ↔ Coherent (body 𝓘 T))) ∧
    ((RouteB.substratumTheory (Fin 2)).avail Unit
        (fun _ => MonoidalCompletion.conjChannel (framePhase (1 : Fin 2))) ∧
      (∀ X ∈ body StructuralClosure.substratumClass (Fin 2),
        conjAff (framePhase (1 : Fin 2)) (framePhase_unitary 1) X = X) ∧
      CompositionOrder.InfiniteOrderOn (Set.univ : Set (Matrix (Fin 2) (Fin 2) ℂ))
        (conjAff (framePhase (1 : Fin 2)) (framePhase_unitary 1))) ∧
    CompositionOrder.OrdInf (body InterventionLocality.fullClass (Fin 2))
      (availData InterventionLocality.fullClass (Fin 2)) :=
  ⟨fun _ _ _ => substratum_not_ordInf, fun _ _ _ => permClass_not_ordInf,
    fun _ _ _ _ arch h => exists_nonsubmonomial_of_ordInf arch h,
    fun _ _ _ _ hph => ordInf_iff_coherent hph,
    ⟨framePhase_avail_substratum 1, framePhase_trivial_on_substratum_body 1,
      framePhase_infiniteOrderOn_univ (s := 0) (by decide)⟩,
    fullClass_ordInf⟩

end Control

#print axioms cfg_apply
#print axioms trace_cfg
#print axioms mul_cfg_apply
#print axioms conj_cfg_apply
#print axioms trace_conj
#print axioms isClosed_diag
#print axioms convex_diag
#print axioms reach_subset_body
#print axioms body_subset_diag
#print axioms conjAff_apply
#print axioms conjAff_iterate
#print axioms diag_eq_sum
#print axioms eq_cfg_of_diag
#print axioms conj_cfg_mem_reach
#print axioms finiteOrderOn_of_reach_diag
#print axioms not_ordInf_of_reach_diag
#print axioms conj_cfg_diag_of_submonomial
#print axioms reach_diag_of_submonomial
#print axioms substratum_reach_diag
#print axioms permClass_reach_diag
#print axioms substratum_not_ordInf
#print axioms permClass_not_ordInf
#print axioms substratumTheory_datum_finiteOrderOn
#print axioms exists_nonsubmonomial_of_ordInf
#print axioms star_exp_I
#print axioms expI_pow_ne_one
#print axioms framePhase_entry_unit
#print axioms framePhase_unitary
#print axioms framePhase_mem_substratumClass
#print axioms framePhase_avail_substratum
#print axioms framePhase_fixes_diag
#print axioms framePhase_trivial_on_substratum_body
#print axioms framePhase_iterate_entry
#print axioms framePhase_infiniteOrderOn
#print axioms framePhase_infiniteOrderOn_univ
#print axioms framePhase_crosses_stages
#print axioms coherent_of_ordInf
#print axioms ordInf_of_coherent
#print axioms ordInf_iff_coherent
#print axioms ordInf_iff_coherent_of_extends
#print axioms fullClass_coherent
#print axioms fullClass_ordInf
#print axioms substratum_obstruction
#print axioms obsTheory_obstruction
#print axioms o11_core

end OriginTokenOrder
end OIBridge
