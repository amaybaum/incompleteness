/-
  OIBridge/QuantumRepresentationT3.lean — target T3 of `OI-QUANTUM-REPRESENTATION-AUDIT.md`.

  Frozen preregistration: commit `38a8f09d9d314fdd3d7747d0d0351f07c693c582`, blob
  `8177527b11a0970c7fc71f1bff382112aaf93aa6`; Amendment 1 blob
  `e809e04aee45181d162bd4a2cc2782751b65f509`.

  T3 asks whether `C_OI ⊆ Q*`.  The answer is CARRIERWISE, and both halves are proved here.

  THE EMPTY CARRIER IS A GENUINE FAILURE, not an oversight.  Over an empty visible carrier `C_OI` is
  inhabited — take `H = Unit` and the identity update — while `Q*` is EMPTY: `IsLaw` forces
  `∑ b, init b = 1`, so the basis is nonempty, and there is no map from a nonempty basis into an
  empty carrier.  The obstruction is in the shape of the representation datum, not in the dynamics,
  and no construction repairs it.

  ON EVERY NONEMPTY FINITE CARRIER the inclusion holds, and the construction is the Arc B one read
  as a quantum system.  A `RootedRealization` carries a reversible `step : V × H ≃ V × H`, which is
  already an `Equiv.Perm (V × H)`, so its permutation matrix is unitary by the merged
  `permMatrix_mem_unitaryGroup` — no new unitarity argument is needed.  The hidden prior, shared by
  every root, is spread over the product with the visible coordinate uniform; conditioning on the
  visible fibre `read (B_0) = a` then removes that uniform factor exactly and returns `rootedMap`.

  ORIENTATION, which is easy to get backwards.  Mathlib's `permMatrix σ i j = if σ i = j then 1
  else 0`, while the Born weight reads `‖U b' b‖^2` — the TRANSPOSED index order.  Using
  `step.permMatrix` would therefore run the chain along `step⁻¹`.  The datum below uses
  `step.symm.permMatrix`, so that the chain advances along `step`, matching `rootedMap`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuantumRepresentation
import OIBridge.RootedClassificationAllTime

namespace OIBridge

namespace QuantumRepresentation

open Finset Matrix OIBridge.CausalReadback OIBridge.RootedClassification
open OIBridge.EquivalenceChain (permMatrix_mem_unitaryGroup)

universe u

set_option linter.unusedSectionVars false

variable {V : Type u} [Fintype V] [DecidableEq V]

/-! ### A representation datum needs somewhere to read into

Membership in `Q*` forces the visible carrier to be inhabited.  This is the half of the carrierwise
answer that needs no construction. -/

/-- Any `Q*` member forces a nonempty visible carrier: the initial law is normalised, so the basis
is nonempty, and the readout lands in `V`. -/
theorem nonempty_of_qStar {Γ : ℕ → Matrix V V ℝ} (h : QStar Γ) : Nonempty V := by
  obtain ⟨Q, hQ, _, _⟩ := h
  have hb : Nonempty Q.Bas := by
    by_contra hemp
    rw [not_nonempty_iff] at hemp
    have : ∑ b : Q.Bas, Q.init b = 0 := Finset.sum_of_isEmpty _
    rw [hQ.2.2] at this
    exact one_ne_zero this
  exact ⟨Q.read hb.some⟩

/-- **The empty carrier is outside `Q*` altogether.** -/
theorem not_qStar_of_isEmpty [IsEmpty V] (Γ : ℕ → Matrix V V ℝ) : ¬ QStar Γ :=
  fun h => (nonempty_of_qStar h).elim (fun a => (IsEmpty.false a).elim)

/-! ### The Arc B realization read as a quantum system -/

variable {H : Type u} [Fintype H] [DecidableEq H]

/-- The representation datum built from an inherited rooted realization: the reversible update as a
permutation matrix, the shared hidden prior spread over the product with the visible coordinate
uniform, and the visible projection as readout. -/
noncomputable def permData [Nonempty V] (R : RootedRealization V H) : QfbData V where
  Bas := V × H
  fB := inferInstance
  dB := inferInstance
  U := Equiv.Perm.permMatrix ℂ (show Equiv.Perm (V × H) from R.step.symm)
  init := fun b => R.prior b.2 / (Fintype.card V : ℝ)
  read := Prod.fst

theorem permData_card_pos [Nonempty V] : (0 : ℝ) < (Fintype.card V : ℝ) := by
  exact_mod_cast Fintype.card_pos

/-- The Born weight of a permutation datum is the deterministic step, oriented along `step`. -/
theorem permData_born [Nonempty V] (R : RootedRealization V H) (b b' : V × H) :
    (permData R).born b b' = if b' = R.step b then 1 else 0 := by
  show ‖(Equiv.Perm.permMatrix ℂ (show Equiv.Perm (V × H) from R.step.symm)) b' b‖ ^ 2 = _
  rw [Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply]
  by_cases h : b' = R.step b
  · have : R.step.symm b' = b := by rw [h, Equiv.symm_apply_apply]
    simp [this, h]
  · have : R.step.symm b' ≠ b := fun hc => h (by rw [← hc, Equiv.apply_symm_apply])
    simp [this, h]

/-- Its iterate is the iterated step, by the general deterministic-step lemma. -/
theorem permData_bornPow [Nonempty V] (R : RootedRealization V H) (t : ℕ) (b b' : V × H) :
    (permData R).bornPow t b b' = if b' = (⇑R.step)^[t] b then 1 else 0 :=
  (permData R).bornPow_of_det (fun b => R.step b) (permData_born R) t b b'

/-! ### Conditioning on the visible fibre returns the inherited rooted family -/

theorem permData_rootMass [Nonempty V] (R : RootedRealization V H) (a : V) :
    (permData R).rootMass a = 1 / (Fintype.card V : ℝ) := by
  unfold QfbData.rootMass permData
  dsimp only
  rw [Finset.sum_filter, Fintype.sum_prod_type]
  have hv : ∀ v : V, (∑ h : H, if v = a then R.prior h / (Fintype.card V : ℝ) else 0)
      = if v = a then 1 / (Fintype.card V : ℝ) else 0 := by
    intro v
    split
    · rw [← Finset.sum_div, R.prior_sum]
    · simp
  rw [Finset.sum_congr rfl fun v _ => hv v, Finset.sum_ite_eq' univ a]
  simp

theorem permData_positiveRootMass [Nonempty V] (R : RootedRealization V H) :
    (permData R).PositiveRootMass := by
  intro a
  rw [permData_rootMass]
  exact div_pos one_pos permData_card_pos

theorem permData_isLaw [Nonempty V] (R : RootedRealization V H) : (permData R).IsLaw := by
  refine ⟨permMatrix_mem_unitaryGroup _, fun b => ?_, ?_⟩
  · show 0 ≤ R.prior b.2 / (Fintype.card V : ℝ)
    exact div_nonneg (R.prior_nonneg _) permData_card_pos.le
  · show ∑ b : V × H, R.prior b.2 / (Fintype.card V : ℝ) = 1
    rw [Fintype.sum_prod_type]
    have hv : ∀ _v : V, (∑ h : H, R.prior h / (Fintype.card V : ℝ))
        = 1 / (Fintype.card V : ℝ) := fun _ => by rw [← Finset.sum_div, R.prior_sum]
    rw [Finset.sum_congr rfl fun v _ => hv v, Finset.sum_const, Finset.card_univ,
      nsmul_eq_mul, mul_one_div]
    exact div_self permData_card_pos.ne'

/-- **The identification.**  Conditioning the permutation datum on the visible root fibre returns
exactly the inherited rooted family. -/
theorem permData_rooted [Nonempty V] (R : RootedRealization V H) (t : ℕ) (a j : V) :
    (permData R).rooted t a j = rootedMap R t a j := by
  have hjoint : (permData R).jointMass t a j
      = (1 / (Fintype.card V : ℝ)) * rootedMap R t a j := by
    show ∑ b ∈ univ.filter (fun b : V × H => b.1 = a),
        ∑ b' ∈ univ.filter (fun b' : V × H => b'.1 = j),
          R.prior b.2 / (Fintype.card V : ℝ) * (permData R).bornPow t b b' = _
    rw [Finset.sum_filter, Fintype.sum_prod_type]
    have hinner : ∀ (v : V) (h : H),
        (∑ b' ∈ univ.filter (fun b' : V × H => b'.1 = j),
            R.prior h / (Fintype.card V : ℝ) * (permData R).bornPow t (v, h) b')
        = if ((⇑R.step)^[t] (v, h)).1 = j then R.prior h / (Fintype.card V : ℝ) else 0 := by
      intro v h
      rw [Finset.sum_filter]
      have hb : ∀ b' : V × H,
          (if b'.1 = j then R.prior h / (Fintype.card V : ℝ) * (permData R).bornPow t (v, h) b'
            else 0)
          = (if b' = (⇑R.step)^[t] (v, h) then
              (if b'.1 = j then R.prior h / (Fintype.card V : ℝ) else 0) else 0) := by
        intro b'
        rw [permData_bornPow]
        by_cases h1 : b' = (⇑R.step)^[t] (v, h) <;> by_cases h2 : b'.1 = j <;> simp [h1, h2]
      rw [Finset.sum_congr rfl fun b' _ => hb b',
        Finset.sum_ite_eq' univ ((⇑R.step)^[t] (v, h))]
      simp
    have hv : ∀ v : V,
        (∑ h : H, if v = a then
            (∑ b' ∈ univ.filter (fun b' : V × H => b'.1 = j),
              R.prior h / (Fintype.card V : ℝ) * (permData R).bornPow t (v, h) b') else 0)
        = if v = a then (1 / (Fintype.card V : ℝ)) * rootedMap R t v j else 0 := by
      intro v
      split
      · rw [Finset.sum_congr rfl fun h _ => hinner v h]
        show _ = (1 / (Fintype.card V : ℝ)) * ∑ h : H, if ((⇑R.step)^[t] (v, h)).1 = j
            then R.prior h else 0
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun h _ => ?_
        split <;> [rw [one_div, inv_mul_eq_div]; rw [mul_zero]]
      · simp
    rw [Finset.sum_congr rfl fun v _ => hv v, Finset.sum_ite_eq' univ a]
    simp
  show (permData R).jointMass t a j / (permData R).rootMass a = _
  rw [hjoint, permData_rootMass]
  field_simp

/-! ### T3, carrierwise -/

/-- Every inherited rooted realization is represented, on a nonempty visible carrier. -/
theorem qStar_of_rootedRealization [Nonempty V] (R : RootedRealization V H) :
    QStar (fun t => rootedMap R t) :=
  ⟨permData R, permData_isLaw R, permData_positiveRootMass R,
    fun a t j => (permData_rooted R t a j).symm⟩

/-- **T3 PROVED for nonempty finite visible carriers.**  Everything realizable at the inherited
interface is representable. -/
theorem qStar_of_finiteRootedRealizable [Nonempty V] {Γ : ℕ → Matrix V V ℝ}
    (h : FiniteRootedRealizable (V := V) Γ) : QStar Γ := by
  obtain ⟨H', hH', R, hR⟩ := h
  letI : Fintype H' := hH'
  letI : DecidableEq H' := Classical.decEq H'
  have hfun : (fun t => rootedMap R t) = Γ := funext hR
  have hq := qStar_of_rootedRealization R
  rwa [hfun] at hq

/-- The same statement through the Arc B characterization: every `PPer` family is represented. -/
theorem qStar_of_pper [Nonempty V] {Γ : ℕ → Matrix V V ℝ} (h : PPer Γ) : QStar Γ :=
  qStar_of_finiteRootedRealizable ((finiteRootedRealizable_iff_pper Γ).mpr h)

/-- **T3 IS EXACTLY A NONEMPTINESS CONDITION.**  The inclusion holds on a finite visible carrier if
and only if that carrier is inhabited.  The forward direction is the construction; the reverse is
the shape of the representation datum, since over an empty carrier `C_OI` is inhabited while `Q*`
is not. -/
theorem qStar_inclusion_iff_nonempty :
    (∀ Γ : ℕ → Matrix V V ℝ, FiniteRootedRealizable (V := V) Γ → QStar Γ) ↔ Nonempty V := by
  constructor
  · intro h
    by_contra hemp
    rw [not_nonempty_iff] at hemp
    have hone : FiniteRootedRealizable (V := V) (fun _ => 1) := by
      refine ⟨PUnit, inferInstance, ⟨Equiv.refl _, fun _ => 1, fun _ => zero_le_one, by simp⟩, ?_⟩
      intro t
      funext a
      exact (IsEmpty.false a).elim
    exact not_qStar_of_isEmpty _ (h _ hone)
  · intro hne Γ hΓ
    exact qStar_of_finiteRootedRealizable hΓ

end QuantumRepresentation

end OIBridge

#print axioms OIBridge.QuantumRepresentation.nonempty_of_qStar
#print axioms OIBridge.QuantumRepresentation.not_qStar_of_isEmpty
#print axioms OIBridge.QuantumRepresentation.permData_card_pos
#print axioms OIBridge.QuantumRepresentation.permData_born
#print axioms OIBridge.QuantumRepresentation.permData_bornPow
#print axioms OIBridge.QuantumRepresentation.permData_rootMass
#print axioms OIBridge.QuantumRepresentation.permData_positiveRootMass
#print axioms OIBridge.QuantumRepresentation.permData_isLaw
#print axioms OIBridge.QuantumRepresentation.permData_rooted
#print axioms OIBridge.QuantumRepresentation.qStar_of_rootedRealization
#print axioms OIBridge.QuantumRepresentation.qStar_of_finiteRootedRealizable
#print axioms OIBridge.QuantumRepresentation.qStar_of_pper
#print axioms OIBridge.QuantumRepresentation.qStar_inclusion_iff_nonempty
