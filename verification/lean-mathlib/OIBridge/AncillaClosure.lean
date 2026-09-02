/-
  OIBridge/AncillaClosure.lean — the shifted theory: any composite carrier may itself be
  used as the working system, and composite COMPLETENESS follows.

  ROUND THIRTY-EIGHT, PART ONE. Round thirty-seven closed the SOUNDNESS half of composite
  quantum operations. The completeness half — every normalized finite Kraus instrument on
  a composite carrier `A × Fin n` is available — is what the Stinespring assembly of round
  twenty-five would deliver if `A × Fin n` could be treated as the system of a
  `FiniteOperationalTheory` with a fresh finite ancilla. This file attempts exactly that
  construction, records field by field what the existing rules can and cannot fill, states
  the one missing rule, and closes completeness under it.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  THE FAILURE AUDIT (`shift`): from `T : FiniteOperationalTheory A` build       │
      │    `T⁽ⁿ⁾ : FiniteOperationalTheory (A × Fin n)` with `avail = T.availExt n` and  │
      │    `availExt m` = `T.availExt (n·m)` along the explicit reindexing `shiftIdx`.  │
      │    identity / coarse-graining / feed-forward on composites: FREE (structure);   │
      │    composite identity at the new base: composite unitary control (`U = 1`);     │
      │    relative readout of the fresh ancilla: INERT-SPECTATOR COMPOSITIONALITY      │
      │      (the old ancilla is the inert spectator of the readout at level `m`);      │
      │    fresh-ancilla preparation AND discard back to the composite base: MISSING —  │
      │      the one new rule `IteratedAncillaClosure`.                                │
      │  THE CLOSURE THEOREM: under that rule (+ control + inert spectators) the shifted │
      │    theory exists, has composite unitary control, and the round-25 Stinespring    │
      │    assembly applies to it at every positive level:                              │
      │    `compositeCompleteness` — every normalized finite Kraus instrument on          │
      │    `A × Fin (k+1)` is `T.availExt (k+1)`-available, against boundary item 2 at   │
      │    the composite carriers.                                                       │
      │  THE ENDPOINT (`exactComposite_of_conditions`, qubit system):                    │
      │    KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T │
      │      ∧ IteratedAncillaClosure T  ⟹  ExactCompositeQuantumOps T                  │
      │    (availExt (k+1) (Fin m) F ⟺ F is a normalized finite Kraus instrument),       │
      │    against boundary item 2 at `Unit` (soundness) and at `Fin 2 × Fin (k+1)`      │
      │    (completeness). `fullQuantum` satisfies all four conditions.                  │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE MISSING RULE, in physical words. ITERATED ANCILLA CLOSURE: a composite carrier may
  itself be used as the working system in a larger experiment — attach a fresh uniformly
  mixed finite ancilla to `A × Fin n`, run any intervention available on the enlarged
  carrier, discard the fresh ancilla: the result is an available intervention on
  `A × Fin n`. Formally it is the structure's own `prepAvail_uniform` + `prepAvail_discard`
  pair relative to the composite base, packaged as ONE rule (the uniform attachment is the
  declared preparation, the discard rule is the content). Nothing about pure seeds, Kraus
  forms or unitaries is assumed in it. It is distinct from inert-spectator compositionality
  (adding an unused system must not change what an intervention does), and the audit shows
  both are used at different fields.

  WHY THIS IS THE RIGHT PACKAGING. Preparation in `FiniteOperationalTheory` is an
  availability predicate whose only assumed member is the uniform attachment, and whose only
  link to interventions is the discard rule. At the composite base the structure has no
  preparation notion at all (`prepAvail` starts from `A`), so the shifted theory must supply
  one; the smallest choice — "exactly the uniform attachment followed by available
  transported interventions" — makes `prepAvail_uniform` and `prepAvail_post` free and
  leaves `prepAvail_discard` as the single obligation, which is `IteratedAncillaClosure`
  verbatim. Part two (`ClosureObstruction.lean`) shows this obligation is NOT derivable from
  the existing rules together with control, inert-spectator compositionality, exact system
  QM and composite soundness: a theory with all of those has no shifted theory at level two.

  WHAT IS AND IS NOT CLAIMED. Proved: the audit as named lemmas with their exact
  hypotheses; the shifted theory under the rule; composite completeness at every positive
  level; exact composite finite endomorphic quantum operations for a qubit system under the
  four conditions and boundary item 2; satisfiability by `fullQuantum`. NOT claimed: that OI
  implies iterated ancilla closure or inert-spectator compositionality — that is precisely
  the reformulated research question; "full QM" beyond the finite endomorphic instrument
  scope of the existing endpoint (the Kraus operators are square, the carriers finite); any
  new boundary item (item 2 is consumed at the composite carriers, where the assembly needs
  it, and named as such). No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.SpectatorBridge

namespace OIBridge
namespace AncillaClosure

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalCountermodel ReferenceExtension ReferenceSufficiency BoundaryAudit
open SpectatorBridge

open scoped ComplexOrder

/-! ### Section A — transport along a reindexing, algebraically -/

section Transport

variable {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']

theorem transport_id (e : l ≃ l') : transport e LinearMap.id = LinearMap.id := by
  refine LinearMap.ext fun N => ?_
  rw [transport_apply, LinearMap.id_apply, ← Matrix.reindex_symm, Equiv.apply_symm_apply]
  rfl

theorem transport_comp (e : l ≃ l') (Φ Ψ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e (Φ.comp Ψ) = (transport e Φ).comp (transport e Ψ) := by
  refine LinearMap.ext fun N => ?_
  simp only [transport_apply, LinearMap.comp_apply]
  rw [← Matrix.reindex_symm, Equiv.symm_apply_apply]

theorem transport_sum (e : l ≃ l') {ι : Type*} (s : Finset ι)
    (Φ : ι → Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e (∑ i ∈ s, Φ i) = ∑ i ∈ s, transport e (Φ i) := by
  refine LinearMap.ext fun N => ?_
  ext p q
  simp only [transport_apply, LinearMap.sum_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    Matrix.sum_apply]

theorem transport_smul (e : l ≃ l') (c : ℂ) (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e (c • Φ) = c • transport e Φ := by
  refine LinearMap.ext fun N => ?_
  ext p q
  simp only [transport_apply, LinearMap.smul_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    Matrix.smul_apply]

theorem transport_symm_transport (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ) :
    transport e.symm (transport e Φ) = Φ := by
  refine LinearMap.ext fun N => ?_
  simp only [transport_apply, Equiv.symm_symm]
  rw [← Matrix.reindex_symm, Equiv.symm_apply_apply, Equiv.symm_apply_apply]

/-- Transport on a reindexed input is the reindexed output. -/
theorem transport_reindex (e : l ≃ l') (Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ)
    (Y : Matrix l l ℂ) :
    transport e Φ (Matrix.reindex e e Y) = Matrix.reindex e e (Φ Y) := by
  rw [transport_apply, ← Matrix.reindex_symm, Equiv.symm_apply_apply]

end Transport

/-! ### Section B — the reindexings of the shifted carrier -/

section Index

variable (A : Type*) [Fintype A] [DecidableEq A]

/-- `(A × Fin n) × Fin m ≃ A × Fin (n·m)`: the composite base keeps the system slot, the old
and fresh ancillas are packed. -/
def shiftIdx (n m : ℕ) : (A × Fin n) × Fin m ≃ A × Fin (n * m) :=
  (Equiv.prodAssoc A (Fin n) (Fin m)).trans (Equiv.prodCongr (Equiv.refl A) finProdFinEquiv)

theorem shiftIdx_apply (n m : ℕ) (a : A) (j : Fin n) (k : Fin m) :
    shiftIdx A n m ((a, j), k) = (a, finProdFinEquiv (j, k)) := rfl

/-- The old ancilla as a SPECTATOR of the level-`m` carrier: `Fin n × (A × Fin m) ≃ A × Fin (n·m)`,
compatible with `shiftIdx`. -/
def specIdx (n m : ℕ) : Fin n × (A × Fin m) ≃ A × Fin (n * m) :=
  ((Equiv.prodAssoc (Fin n) A (Fin m)).symm.trans
    (Equiv.prodCongr (Equiv.prodComm (Fin n) A) (Equiv.refl (Fin m)))).trans (shiftIdx A n m)

theorem specIdx_apply (n m : ℕ) (j : Fin n) (a : A) (k : Fin m) :
    specIdx A n m (j, (a, k)) = (a, finProdFinEquiv (j, k)) := rfl

end Index

/-! ### Section C — the audit, field by field -/

section Audit

variable {A : Type*} [Fintype A] [DecidableEq A]

theorem conjChannel_one {S : Type*} [Fintype S] [DecidableEq S] :
    conjChannel (1 : Matrix S S ℂ) = LinearMap.id := by
  refine LinearMap.ext fun X => ?_
  show (1 : Matrix S S ℂ) * X * (1 : Matrix S S ℂ)ᴴ = X
  rw [Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]

/-- **COMPOSITE IDENTITY NEEDS CONTROL.** The structure's composite rules never produce the
identity at a positive level (readout sums to the dephasing, not the identity); composite
unitary control supplies it at `U = 1`. -/
theorem availExt_id_of_control (T : FiniteOperationalTheory A)
    (hctrl : HasCompositeUnitaryControl T) (n : ℕ) :
    T.availExt n Unit (fun _ => LinearMap.id) := by
  have h := hctrl n 1 (by rw [Matrix.conjTranspose_one, Matrix.one_mul])
  rwa [conjChannel_one] at h

/-- Sequential composition of two one-outcome composite interventions, by feed-forward and
coarse-graining — free. -/
theorem availExt_comp_unit (T : FiniteOperationalTheory A) (n : ℕ)
    (Φ Ψ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hΦ : T.availExt n Unit (fun _ => Φ)) (hΨ : T.availExt n Unit (fun _ => Ψ)) :
    T.availExt n Unit (fun _ => Ψ.comp Φ) := by
  have hb := T.availExt_bind n Unit Unit (fun _ => Φ) (fun _ _ => Ψ) hΦ (fun _ => hΨ)
  have hc := T.availExt_coarse n (Unit × Unit) Unit _ (fun _ => ()) hb
  have hfun : (fun a : Unit => ∑ j ∈ Finset.univ.filter (fun _ : Unit × Unit => () = a),
      Ψ.comp Φ) = fun _ => Ψ.comp Φ := by
    funext a
    rw [Finset.filter_true_of_mem (fun _ _ => rfl), Fintype.sum_subsingleton _ ((), ())]
  rw [hfun] at hc
  exact hc

theorem filter_snd_unit {O : Type} [Fintype O] [DecidableEq O] (a : O) :
    Finset.univ.filter (fun c : Unit × O => c.2 = a) = {((), a)} := by
  ext ⟨⟨⟩, b⟩
  simp

/-- Post-composing an available composite family with an available one-outcome intervention
— free. -/
theorem availExt_comp_family (T : FiniteOperationalTheory A) (n : ℕ) {O : Type} [Fintype O]
    [DecidableEq O]
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hΦ : T.availExt n Unit (fun _ => Φ)) (hF : T.availExt n O F) :
    T.availExt n O (fun a => (F a).comp Φ) := by
  have hb := T.availExt_bind n Unit O (fun _ => Φ) (fun _ a => F a) hΦ (fun _ => hF)
  have hc := T.availExt_coarse n (Unit × O) O _ Prod.snd hb
  have hc' : T.availExt n O (fun a => ∑ c ∈ Finset.univ.filter (fun c : Unit × O => c.2 = a),
      (F c.2).comp Φ) := hc
  have hfun : (fun a => ∑ c ∈ Finset.univ.filter (fun c : Unit × O => c.2 = a),
      (F c.2).comp Φ) = fun a => (F a).comp Φ := by
    funext a
    rw [filter_snd_unit, Finset.sum_singleton]
  rw [hfun] at hc'
  exact hc'

/-- **THE RELATIVE READOUT IS A SPECTATOR EXTENSION.** The Lüders selector of the fresh
ancilla, on `(A × Fin n) × Fin m` and transported to `A × Fin (n·m)`, is the level-`m`
readout with the OLD ancilla adjoined as an inert spectator. -/
theorem transport_localLuders (n m : ℕ) (k : Fin m) :
    transport (shiftIdx A n m) (localLuders (A := A × Fin n) k)
      = withSpectator (Fin n) (specIdx A n m) (localLuders (A := A) k) := by
  refine LinearMap.ext fun N => ?_
  ext p q
  rfl

/-- **RELATIVE READOUT NEEDS INERT-SPECTATOR COMPOSITIONALITY**: the transported fresh-ancilla
readout family is available at level `n·m`. -/
theorem availExt_relativeReadout (T : FiniteOperationalTheory A)
    (hin : InertSpectatorCompositionality T) (n m : ℕ) :
    T.availExt (n * m) (Fin m)
      (fun k => transport (shiftIdx A n m) (localLuders (A := A × Fin n) k)) := by
  have h := (inertSpectator_iff_parallelReferenceExtension T).mp hin (Fin n) m (n * m)
    (specIdx A n m) (Fin m) (T.readout m) (T.readout_avail m)
  simp only [readout_is_localLuders] at h
  simp only [transport_localLuders]
  exact h

/-- **THE MISSING RULE: ITERATED ANCILLA CLOSURE.** Attach a fresh uniformly mixed finite
ancilla to the composite carrier `A × Fin n`, run any intervention available on the enlarged
carrier (transported along `shiftIdx` into the theory's own carrier at level `n·(m+1)`),
discard the fresh ancilla: the result is available on `A × Fin n`. In physical words, any
subsystem may itself be used as the working system in a larger experiment. This is the
structure's uniform-attach-then-discard pair, relative to a composite base. -/
def IteratedAncillaClosure (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n m : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix ((A × Fin n) × Fin (m + 1)) ((A × Fin n) × Fin (m + 1)) ℂ →ₗ[ℂ]
      Matrix ((A × Fin n) × Fin (m + 1)) ((A × Fin n) × Fin (m + 1)) ℂ),
    T.availExt (n * (m + 1)) O (fun a => transport (shiftIdx A n (m + 1)) (F a)) →
      T.availExt n O
        (fun a => discardWith (A := A × Fin n) (m + 1) (uniformAttach (m + 1)) (F a))

end Audit

/-! ### Section D — the shifted theory -/

section Shift

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **THE SHIFTED THEORY** `T⁽ⁿ⁾` on the carrier `A × Fin n`: its system families are
`T.availExt n`, its level-`m` families are `T.availExt (n·m)` along `shiftIdx`, its
preparations are the uniform attachment followed by available transported interventions,
its readout the Lüders selector of the fresh ancilla. Each field is discharged by the audit
lemma named beside it. -/
noncomputable def shift (T : FiniteOperationalTheory A) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ) :
    FiniteOperationalTheory (A × Fin n) where
  avail := fun O _ _ F => T.availExt n O F
  availExt := fun m O _ _ F => T.availExt (n * m) O (fun a => transport (shiftIdx A n m) (F a))
  -- composite identity: CONTROL
  avail_id := availExt_id_of_control T hctrl n
  -- coarse-graining: FREE
  avail_coarse := fun O O' _ _ _ _ F f hF => T.availExt_coarse n O O' F f hF
  availExt_coarse := by
    intro m O O' _ _ _ _ F f hF
    have h := T.availExt_coarse (n * m) O O' _ f hF
    show T.availExt (n * m) O' (fun a => transport (shiftIdx A n m)
      (∑ j ∈ Finset.univ.filter (fun j => f j = a), F j))
    simp only [transport_sum]
    exact h
  -- feed-forward: FREE
  availExt_bind := by
    intro m O O' _ _ _ _ F G hF hG
    show T.availExt (n * m) (O × O')
      (fun c => transport (shiftIdx A n m) ((G c.1 c.2).comp (F c.1)))
    simp only [transport_comp]
    exact T.availExt_bind (n * m) O O' _ (fun a b => transport (shiftIdx A n m) (G a b)) hF hG
  -- preparations: the uniform attachment followed by available transported interventions
  prepAvail := fun m P => 0 < m ∧ ∃ Φ,
    T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) Φ)
      ∧ P = Φ.comp (uniformAttach m)
  -- fresh uniform attachment: DECLARED (the identity is available by CONTROL)
  prepAvail_uniform := fun m =>
    ⟨Nat.succ_pos m, LinearMap.id, by
      rw [transport_id]
      exact availExt_id_of_control T hctrl _, by rw [LinearMap.id_comp]⟩
  -- post-composition: FREE
  prepAvail_post := by
    rintro m P Φ ⟨hm, Ψ, hΨ, rfl⟩ hΦ
    refine ⟨hm, Φ.comp Ψ, ?_, by rw [LinearMap.comp_assoc]⟩
    show T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) (Φ.comp Ψ))
    simp only [transport_comp]
    exact availExt_comp_unit T _ _ _ hΨ hΦ
  -- readout of the fresh ancilla: the Lüders selector; available by INERT SPECTATORS
  readout := fun _ k => localLuders k
  readout_avail := fun m => availExt_relativeReadout T hin n m
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  -- discard of the fresh ancilla back to the composite base: THE CLOSURE RULE
  prepAvail_discard := by
    rintro m P O _ _ F ⟨hm, Φ, hΦ, rfl⟩ hF
    obtain ⟨m', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hm.ne'
    show T.availExt n O (fun a => discardWith (m' + 1) (Φ.comp (uniformAttach (m' + 1))) (F a))
    have hcomp : T.availExt (n * (m' + 1)) O
        (fun a => transport (shiftIdx A n (m' + 1)) ((F a).comp Φ)) := by
      simp only [transport_comp]
      exact availExt_comp_family T _ _ _ hΦ hF
    have h := hclos n m' O (fun a => (F a).comp Φ) hcomp
    simpa only [discardWith, LinearMap.comp_assoc] using h

theorem shift_avail_iff (T : FiniteOperationalTheory A) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (shift T hctrl hin hclos n).avail O F ↔ T.availExt n O F := Iff.rfl

/-- The shifted theory inherits composite unitary control: a unitary on `(A × Fin n) × Fin m`
is a unitary on `A × Fin (n·m)` after reindexing. -/
theorem shift_control (T : FiniteOperationalTheory A) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ) :
    HasCompositeUnitaryControl (shift T hctrl hin hclos n) := by
  intro m U hU
  show T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) (conjChannel U))
  rw [transport_conjChannel]
  exact hctrl _ _ (reindex_isometry _ _ hU)

/-- **THE STINESPRING ASSEMBLY APPLIES TO THE SHIFTED THEORY**, against boundary item 2 at the
composite carrier. -/
theorem shift_full (T : FiniteOperationalTheory A) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ)
    (hext : FiniteIsometryExtensionSF (A × Fin n)) :
    HasFullFiniteEndomorphicInstruments (shift T hctrl hin hclos n) :=
  fullInstruments_of_control _ hext (shift_control T hctrl hin hclos n)

end Shift

/-! ### Section E — composite completeness and the exact composite endpoint -/

section Endpoint

variable {A : Type*} [Fintype A] [DecidableEq A]

/-- **COMPOSITE COMPLETENESS**: every normalized finite Kraus instrument on every positive-level
composite carrier is available. -/
def HasFullCompositeInstruments (T : FiniteOperationalTheory A) : Prop :=
  ∀ (k r m : ℕ) (K : Fin (r + 1) → Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ)
    (out : Fin (r + 1) → Fin m),
    (∑ i, (K i)ᴴ * K i = 1) → T.availExt (k + 1) (Fin m) (instrumentBranch K out)

/-- **EXACT COMPOSITE QUANTUM OPERATIONS**: at every positive level, the available finite
outcome families are EXACTLY the normalized finite Kraus instruments on the composite. -/
def ExactCompositeQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ∀ (k m : ℕ) (F : Fin m → Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ →ₗ[ℂ]
      Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ),
    T.availExt (k + 1) (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F

/-- **COMPOSITE COMPLETENESS FROM THE CLOSURE RULE.** Control, inert-spectator
compositionality and iterated ancilla closure, against boundary item 2 at each composite
carrier, make every normalized finite Kraus instrument on every positive-level composite
available. -/
theorem compositeCompleteness (T : FiniteOperationalTheory A)
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (A × Fin (k + 1)))
    (hctrl : HasCompositeUnitaryControl T) (hin : InertSpectatorCompositionality T)
    (hclos : IteratedAncillaClosure T) : HasFullCompositeInstruments T :=
  fun k r m K out hnorm => shift_full T hctrl hin hclos (k + 1) (hext k) r m K out hnorm

/-- Exactness splits into composite soundness and composite completeness. -/
theorem exactComposite_of_soundExt_full (T : FiniteOperationalTheory A)
    (hs : KrausSoundExt T) (hf : HasFullCompositeInstruments T) :
    ExactCompositeQuantumOps T := by
  intro k m F
  constructor
  · intro hF
    exact (isKrausFamily_iff F).mp (hs k (Fin m) F hF)
  · rintro ⟨r, K, out, hnorm, rfl⟩
    exact hf k r m K out hnorm

theorem exactComposite_iff (T : FiniteOperationalTheory A) :
    ExactCompositeQuantumOps T
      ↔ (∀ (k m : ℕ) (F : Fin m → Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ →ₗ[ℂ]
            Matrix (A × Fin (k + 1)) (A × Fin (k + 1)) ℂ),
          T.availExt (k + 1) (Fin m) F → IsFiniteEndomorphicKrausInstrument F)
        ∧ HasFullCompositeInstruments T := by
  constructor
  · intro h
    exact ⟨fun k m F hF => (h k m F).mp hF,
      fun k r m K out hnorm => (h k m _).mpr (instrumentBranch_isKraus K out hnorm)⟩
  · rintro ⟨hs, hf⟩ k m F
    exact ⟨hs k m F, by rintro ⟨r, K, out, hnorm, rfl⟩; exact hf k r m K out hnorm⟩

end Endpoint

/-- **THE ENDPOINT, FOR A QUBIT SYSTEM.** System Kraus soundness, full composite unitary
control, inert-spectator compositionality and iterated ancilla closure give exact composite
finite endomorphic quantum operations at every positive level — soundness from round
thirty-seven against boundary item 2 at `Unit`, completeness from the shifted Stinespring
assembly against boundary item 2 at the composite carriers. -/
theorem exactComposite_of_conditions (T : FiniteOperationalTheory (Fin 2))
    (hextU : FiniteIsometryExtensionSF Unit)
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1)))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T)
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) :
    ExactCompositeQuantumOps T :=
  exactComposite_of_soundExt_full T
    (krausSoundExt_of_sound_control_inert T hextU hsound hctrl hin)
    (compositeCompleteness T hext hctrl hin hclos)

/-! ### Section F — the full quantum theory has iterated ancilla closure -/

section FullClosure

variable {S : Type*} [Fintype S] [DecidableEq S]

theorem choiMatrix_smul (c : ℂ) (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    choiMatrix (c • Φ) = c • choiMatrix Φ := by
  ext p q
  rfl

theorem cp_smul {c : ℂ} (hc : 0 ≤ c) {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (h : IsCompletelyPositive Φ) : IsCompletelyPositive (c • Φ) := by
  show (choiMatrix _).PosSemidef
  rw [choiMatrix_smul]
  exact Matrix.PosSemidef.smul h hc

theorem conjChannel_apply (V X : Matrix S S ℂ) : conjChannel V X = V * X * Vᴴ := rfl

/-- Transport preserves complete positivity (through the internal Kraus form). -/
theorem transport_cp {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l] [DecidableEq l']
    (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ} (h : IsCompletelyPositive Φ) :
    IsCompletelyPositive (transport e Φ) := by
  have h' : (choiMatrix Φ).PosSemidef := h
  obtain ⟨B, hB⟩ := psdFactorization_discharged _ _ h'
  rw [kraus_of_choi_factor Φ B hB, transport_sum]
  refine cp_sum _ _ fun i _ => ?_
  rw [transport_conjChannel]
  exact conjChannel_cp _

theorem cp_of_transport_cp {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ}
    (h : IsCompletelyPositive (transport e Φ)) : IsCompletelyPositive Φ := by
  have := transport_cp e.symm h
  rwa [transport_symm_transport] at this

/-- The fresh-ancilla block of an operator on `S × Fin m`. -/
def ancBlock {m : ℕ} (K : Matrix (S × Fin m) (S × Fin m) ℂ) (f e : Fin m) : Matrix S S ℂ :=
  Matrix.of fun s t => K (s, f) (t, e)

/-- **ATTACH-CONJUGATE-DISCARD IS A SCALED KRAUS SUM** over the fresh-ancilla blocks. -/
theorem discardWith_uniform_conjChannel {m : ℕ} (K : Matrix (S × Fin m) (S × Fin m) ℂ) :
    discardWith (A := S) m (uniformAttach m) (conjChannel K)
      = ((m : ℂ))⁻¹ • ∑ c : Fin m × Fin m, conjChannel (ancBlock K c.1 c.2) := by
  refine LinearMap.ext fun ρ => ?_
  ext s t
  show ptraceAnc m (K * tensorOf ρ (((m : ℂ))⁻¹ • (1 : Matrix (Fin m) (Fin m) ℂ)) * Kᴴ) s t = _
  rw [ptraceAnc_apply, LinearMap.smul_apply, LinearMap.sum_apply, Matrix.smul_apply,
    Matrix.sum_apply, Fintype.sum_prod_type, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [Finset.mul_sum]
  simp only [conjChannel_apply, Matrix.mul_apply, Matrix.conjTranspose_apply, tensorOf_apply,
    Matrix.smul_apply, Matrix.one_apply, smul_eq_mul, mul_ite, mul_one, mul_zero,
    Fintype.sum_prod_type, Finset.sum_ite_eq', Finset.mem_univ, if_true, ancBlock,
    Matrix.of_apply]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Finset.sum_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun v _ => ?_
  refine Finset.sum_congr rfl fun u _ => ?_
  ring

theorem discardWith_sum {m : ℕ} (P : Matrix S S ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ)
    {ι : Type*} (s : Finset ι)
    (Φ : ι → Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ) :
    discardWith (A := S) m P (∑ i ∈ s, Φ i) = ∑ i ∈ s, discardWith (A := S) m P (Φ i) := by
  refine LinearMap.ext fun ρ => ?_
  simp only [discardWith, LinearMap.comp_apply, LinearMap.sum_apply, map_sum]

/-- **ATTACH-RUN-DISCARD PRESERVES COMPLETE POSITIVITY.** -/
theorem discardWith_uniform_cp {m : ℕ}
    {Φ : Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ}
    (h : IsCompletelyPositive Φ) :
    IsCompletelyPositive (discardWith (A := S) m (uniformAttach m) Φ) := by
  have h' : (choiMatrix Φ).PosSemidef := h
  obtain ⟨B, hB⟩ := psdFactorization_discharged _ _ h'
  rw [kraus_of_choi_factor Φ B hB, discardWith_sum]
  refine cp_sum _ _ fun i _ => ?_
  rw [discardWith_uniform_conjChannel]
  exact cp_smul (natInv_nonneg m) (cp_sum _ _ fun c _ => conjChannel_cp _)

end FullClosure

/-- **THE FULL QUANTUM THEORY HAS ITERATED ANCILLA CLOSURE.** -/
theorem fullQuantum_iteratedAncillaClosure : IteratedAncillaClosure fullQuantum := by
  intro n m O _ _ F ⟨hcp, htr⟩
  refine ⟨fun a => discardWith_uniform_cp (cp_of_transport_cp _ (hcp a)), fun X => ?_⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx (Fin 2) n (m + 1)) (shiftIdx (Fin 2) n (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

/-- **THE FOUR CONDITIONS ARE JOINTLY SATISFIABLE**, by the full quantum theory. -/
theorem conditions_satisfiable :
    ∃ T : FiniteOperationalTheory (Fin 2),
      KrausSound T ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T ∧ KrausSoundExt T :=
  ⟨fullQuantum, ((exact_iff_sound_and_full _).mp fullQuantum_exact).1, fullQuantum_control,
    fullQuantum_inert, fullQuantum_iteratedAncillaClosure, fullQuantum_krausSoundExt⟩

/-- The full theory is exactly quantum on every composite, against boundary item 2. -/
theorem fullQuantum_exactComposite (hextU : FiniteIsometryExtensionSF Unit)
    (hext : ∀ k : ℕ, FiniteIsometryExtensionSF (Fin 2 × Fin (k + 1))) :
    ExactCompositeQuantumOps fullQuantum :=
  exactComposite_of_conditions fullQuantum hextU hext
    ((exact_iff_sound_and_full _).mp fullQuantum_exact).1 fullQuantum_control
    fullQuantum_inert fullQuantum_iteratedAncillaClosure

#print axioms transport_id
#print axioms transport_comp
#print axioms transport_sum
#print axioms transport_smul
#print axioms transport_symm_transport
#print axioms transport_reindex
#print axioms shiftIdx_apply
#print axioms specIdx_apply
#print axioms conjChannel_one
#print axioms availExt_id_of_control
#print axioms availExt_comp_unit
#print axioms filter_snd_unit
#print axioms availExt_comp_family
#print axioms transport_localLuders
#print axioms availExt_relativeReadout
#print axioms shift_avail_iff
#print axioms shift_control
#print axioms shift_full
#print axioms compositeCompleteness
#print axioms exactComposite_of_soundExt_full
#print axioms exactComposite_iff
#print axioms exactComposite_of_conditions
#print axioms choiMatrix_smul
#print axioms cp_smul
#print axioms conjChannel_apply
#print axioms transport_cp
#print axioms cp_of_transport_cp
#print axioms discardWith_uniform_conjChannel
#print axioms discardWith_sum
#print axioms discardWith_uniform_cp
#print axioms fullQuantum_iteratedAncillaClosure
#print axioms conditions_satisfiable
#print axioms fullQuantum_exactComposite

end AncillaClosure
end OIBridge
