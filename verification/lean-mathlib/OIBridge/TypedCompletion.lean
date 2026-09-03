/-
  OIBridge/TypedCompletion.lean — OI_Q Level II, first entry: the typed finite operational
  interface, its endomorphic shadow, and the determination test.

  LEVEL II, ROUND ONE. Level I closed with: current OI substratum + continuous off-diagonal
  controllability ⟺ exact finite ENDOMORPHIC operational quantum mechanics. Every operation in
  that statement acts from a finite carrier back to the same carrier (`FiniteOperationalTheory`
  has only `avail` on `A` and `availExt n` on `A × Fin n`). Full finite-dimensional quantum
  mechanics also has operations `M_S → M_{S'}` between different carriers: preparations,
  embeddings, partial traces, instruments whose input and output dimensions differ. This file
  asks whether "endomorphic" is a physical limitation or an artifact of the typing, and it asks
  it as a REDUNDANCY TEST rather than by postulate.

  THE TYPED INTERFACE HAS INDEPENDENT MEANING. A typed finite operational theory
  (`TypedOperationalTheory`) has an availability predicate on finite outcome families of maps
  `M_S → M_{S'}` for every pair of finite carriers, with exactly the operational closure rules
  the endomorphic structure already has, stated at their natural carrier-general type: doing
  nothing, classical coarse-graining, feed-forward composition across carriers, relabelling
  along carrier bijections, attaching a uniformly mixed fresh factor (the only preparation
  assumed, as in the endomorphic structure), discarding a factor, and a native factor readout
  that is assumed only to exist and to be spectator-independent. NOTHING in the interface says
  "there exists an endomorphic dilation": a typed operation is available or not on its own
  terms.

  THE ENDOMORPHIC SHADOW. Restricting a typed theory to maps from a carrier to itself, with
  `A × Fin n` as the levels, yields a `FiniteOperationalTheory` on every carrier (`shadow`), and
  the shadow family is regrouping-invariant BY DEFINITION and relabelling-invariant by the typed
  relabelling rule, so every shadow is an embedded-observation theory
  (`shadow_embeddedObservation`). This settles the first cross-carrier coherence question: the
  product-type coherence that embedded observation asks for is automatic for a typed theory.

  THE DETERMINATION THEOREM. Suppose the shadow is exact finite endomorphic quantum mechanics on
  every nonempty carrier — exactly what Level I supplies from the OI⁺ package
  (`ShadowQuantum`). Then, between any two nonempty finite carriers, an outcome family of maps
  is typed-available if and only if it is a finite typed Kraus instrument
  (`IsTypedKrausInstrument`: rectangular Kraus operators `M_{S'×S}`, normalized on `S`):

    soundness   (`typedKraus_of_availT`): a typed-available family, wrapped by discard, attach
                and relabelling into an endomorphic family on the register `S × S'`, is a
                square Kraus instrument there by exactness, and the typed family is recovered
                from it by slice embeddings — its Kraus operators are the compressions
                `|S'|^{-1/2} · P_s L_k V_t`;
    completeness (`availT_of_typedKraus`): a typed Kraus instrument is realized by attaching a
                uniform ancilla `S' × Fin (n+1)`, relabelling to the register
                `S' × (S × Fin (n+1))`, running the square Kraus instrument whose operators
                place `K_k` on the output factor and record `k` on the ancilla, and discarding
                the second factor — every step is a typed closure rule or an endomorphic
                availability supplied by exactness on the register.

  The typed theory is therefore DETERMINED by its endomorphic shadow (`typed_determined`), and
  in the Level I vocabulary, by OI⁺ on every carrier (`typed_determined_of_oiPlusElem`); the
  converse holds by restriction to one carrier, so the shadow is quantum exactly when the typed
  theory is the finite typed quantum theory (`typed_determined_iff`).

  THE INTERFACE CARRIES NO QUANTUM CONTENT. The typed diagonal theory (`typedDiag`), in which a
  family is available exactly when every branch preserves diagonal matrices, satisfies every
  rule of the interface, and its shadow on the qubit has no composite unitary control and is not
  quantum mechanics (`typedDiag_shadow_not_qm`). The quantum content of the determination
  theorem lies entirely in the shadow hypothesis; the interface is the carrier-general form of
  the closure rules the endomorphic structure already assumed.

  THE FORK, DECIDED FOR THIS INTERFACE. Of the four outcomes — full redundancy, a preparation
  gap, a coherence gap, another missing operation — the first holds: no fresh chosen-state
  preparation is needed (the uniform attachment plus exactness on the register suffices), and no
  cross-carrier coherence beyond the typed closure rules is needed. "Endomorphic" is a typing
  artifact for this interface. WHAT IS NOT CLAIMED: that the typed interface is the only
  reasonable one; that infinite-dimensional quantum mechanics is reached (Level III is a
  different programme); anything about bare OI, which is untouched.
-/

import OIBridge.StructuralClosure

namespace OIBridge
namespace TypedCompletion

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy PrimitiveSource InterventionLocality
open MicroReversibility LieRankSource SubstratumSource SubstratumInterface ReadWriteControl
open StructuralClosure BranchSelector

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — typed maps -/

section Maps

variable {S S' T T' : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
  [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']

/-- Transport of a typed map along bijections of both carriers. -/
def transportT (e : S ≃ T) (e' : S' ≃ T') (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) :
    Matrix T T ℂ →ₗ[ℂ] Matrix T' T' ℂ :=
  (Matrix.reindexLinearEquiv ℂ ℂ e' e').toLinearMap ∘ₗ Φ
    ∘ₗ (Matrix.reindexLinearEquiv ℂ ℂ e.symm e.symm).toLinearMap

omit [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Fintype T] [DecidableEq T]
  [Fintype T'] [DecidableEq T'] in
theorem transportT_apply (e : S ≃ T) (e' : S' ≃ T') (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (X : Matrix T T ℂ) :
    transportT e e' Φ X = Matrix.reindex e' e' (Φ (Matrix.reindex e.symm e.symm X)) := rfl

omit [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T] in
/-- On one carrier, typed transport is the endomorphic transport. -/
theorem transportT_self (e : S ≃ T) (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    transportT e e Φ = transport e Φ := rfl

/-- Attach a uniformly mixed fresh factor `R`. -/
noncomputable def attachUniform (R : Type) [Fintype R] [DecidableEq R] :
    Matrix S S ℂ →ₗ[ℂ] Matrix (S × R) (S × R) ℂ where
  toFun X := tensorOf X (((Fintype.card R : ℂ))⁻¹ • (1 : Matrix R R ℂ))
  map_add' X Y := tensorOf_add_left X Y _
  map_smul' c X := tensorOf_smul_left c X _

omit [Fintype S] [DecidableEq S] in
theorem attachUniform_apply (R : Type) [Fintype R] [DecidableEq R] (X : Matrix S S ℂ) :
    attachUniform R X = tensorOf X (((Fintype.card R : ℂ))⁻¹ • (1 : Matrix R R ℂ)) := rfl

/-- At a level `Fin n` the typed attachment is the endomorphic structure's own. -/
theorem attachUniform_fin (n : ℕ) : attachUniform (S := S) (Fin n) = uniformAttach n := by
  refine LinearMap.ext fun X => ?_
  rw [attachUniform_apply, uniformAttach_apply, Fintype.card_fin]

/-- Discard the second factor. -/
def discardR (R : Type) [Fintype R] [DecidableEq R] :
    Matrix (S × R) (S × R) ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun M := Matrix.of fun s t => ∑ r : R, M (s, r) (t, r)
  map_add' M N := by
    ext s t
    simp [Matrix.add_apply, Finset.sum_add_distrib]
  map_smul' c M := by
    ext s t
    simp [Matrix.smul_apply, Finset.mul_sum]

omit [Fintype S] [DecidableEq S] in
theorem discardR_apply (R : Type) [Fintype R] [DecidableEq R] (M : Matrix (S × R) (S × R) ℂ)
    (s t : S) : discardR R M s t = ∑ r : R, M (s, r) (t, r) := rfl

omit [Fintype S] [DecidableEq S] in
/-- At a level `Fin n` the typed discard is the endomorphic structure's partial trace. -/
theorem discardR_fin (n : ℕ) : discardR (S := S) (Fin n) = ptraceAncL n := rfl

/-- Discarding a uniformly attached factor returns the state. -/
theorem discardR_attachUniform (R : Type) [Fintype R] [DecidableEq R] [Nonempty R]
    (X : Matrix S S ℂ) : discardR R (attachUniform R X) = X := by
  ext s t
  rw [discardR_apply, attachUniform_apply]
  simp only [tensorOf_apply, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one,
    Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  have hc : (Fintype.card R : ℂ) ≠ 0 := by
    exact_mod_cast Fintype.card_ne_zero
  field_simp

end Maps

/-! ### Section B — the typed interface -/

/-- **A TYPED FINITE OPERATIONAL THEORY**: availability of finite outcome families of maps
between any two finite carriers, with the closure rules of the endomorphic structure stated at
their carrier-general type. No clause mentions a dilation. -/
structure TypedOperationalTheory where
  /-- Available finite outcome families of maps from carrier `S` to carrier `S'`. -/
  availT : ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
    (O : Type) [Fintype O] [DecidableEq O], (O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) → Prop
  /-- Doing nothing is available. -/
  id : ∀ (S : Type) [Fintype S] [DecidableEq S], availT S S Unit (fun _ => LinearMap.id)
  /-- Classical coarse-graining of the outcome label. -/
  coarse : ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
    (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (f : O → O'), availT S S' O F →
    availT S S' O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  /-- Feed-forward composition across carriers. -/
  bind : ∀ (S S' S'' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
    [Fintype S''] [DecidableEq S''] (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O']
    [DecidableEq O'] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (G : O → O' → Matrix S' S' ℂ →ₗ[ℂ] Matrix S'' S'' ℂ),
    availT S S' O F → (∀ a, availT S' S'' O' (G a)) →
    availT S S'' (O × O') (fun c => (G c.1 c.2).comp (F c.1))
  /-- Relabelling along carrier bijections. -/
  relabel : ∀ (S S' T T' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
    [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : S ≃ T) (e' : S' ≃ T')
    (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
    availT S S' O F → availT T T' O (fun a => transportT e e' (F a))
  /-- Attaching a uniformly mixed fresh factor: the only preparation assumed. -/
  attach : ∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R] [Nonempty R],
    availT S (S × R) Unit (fun _ => attachUniform R)
  /-- Discarding a factor. -/
  discard : ∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R],
    availT (S × R) S Unit (fun _ => discardR R)
  /-- A native readout of a factor exists and is spectator-independent; its form is derived. -/
  readout : ∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R],
    R → (Matrix (S × R) (S × R) ℂ →ₗ[ℂ] Matrix (S × R) (S × R) ℂ)
  readout_avail : ∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R],
    availT (S × R) (S × R) R (readout S R)
  readout_local : ∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R]
    (k : R), MapSpectatorIndependent (ludersLift k) (readout S R k)

namespace TypedOperationalTheory

variable (𝒯 : TypedOperationalTheory)

section Outcomes

variable {S S' : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']

/-- Outcome labels may be renamed along a bijection. -/
theorem availT_equiv {O O' : Type} [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
    (e : O ≃ O') (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (h : 𝒯.availT S S' O F) :
    𝒯.availT S S' O' (fun a => F (e.symm a)) := by
  have h2 := 𝒯.coarse S S' O O' F e h
  convert h2 using 1
  funext a
  symm
  refine Finset.sum_eq_single_of_mem (e.symm a) (by simp) ?_
  intro b hb hne
  exfalso
  apply hne
  rw [Finset.mem_filter] at hb
  rw [← hb.2, Equiv.symm_apply_apply]

end Outcomes

/-! ### Section C — the endomorphic shadow and its coherence -/

/-- **THE ENDOMORPHIC SHADOW**: the typed theory restricted to maps from a carrier to itself,
with `A × Fin n` as the levels. -/
noncomputable def shadow (A : Type) [Fintype A] [DecidableEq A] : FiniteOperationalTheory A where
  avail := fun O _ _ F => 𝒯.availT A A O F
  availExt := fun n O _ _ F => 𝒯.availT (A × Fin n) (A × Fin n) O F
  avail_id := 𝒯.id A
  avail_coarse := fun O O' _ _ _ _ F f h => 𝒯.coarse A A O O' F f h
  availExt_coarse := fun _ O O' _ _ _ _ F f h => 𝒯.coarse _ _ O O' F f h
  availExt_bind := fun _ O O' _ _ _ _ F G hF hG => 𝒯.bind _ _ _ O O' F G hF hG
  prepAvail := fun n P => 𝒯.availT A (A × Fin n) Unit (fun _ => P)
  prepAvail_uniform := fun n => by
    have h := 𝒯.attach A (Fin (n + 1))
    rwa [attachUniform_fin] at h
  prepAvail_post := fun n P Φ hP hΦ => by
    have h := 𝒯.bind A (A × Fin n) (A × Fin n) Unit Unit (fun _ => P) (fun _ _ => Φ) hP
      (fun _ => hΦ)
    exact 𝒯.availT_equiv (Equiv.prodPUnit Unit) _ h
  readout := fun n => 𝒯.readout A (Fin n)
  readout_avail := fun n => 𝒯.readout_avail A (Fin n)
  readout_local := fun n k => 𝒯.readout_local A (Fin n) k
  prepAvail_discard := fun n P O _ _ F hP hF => by
    have h1 := 𝒯.bind A (A × Fin n) (A × Fin n) Unit O (fun _ => P) (fun _ => F) hP
      (fun _ => hF)
    have h2 := 𝒯.bind A (A × Fin n) A (Unit × O) Unit _ (fun _ _ => discardR (Fin n)) h1
      (fun _ => 𝒯.discard A (Fin n))
    have h3 := 𝒯.availT_equiv ((Equiv.prodPUnit (Unit × O)).trans (Equiv.punitProd O)) _ h2
    exact h3

theorem shadow_avail (A : Type) [Fintype A] [DecidableEq A] (O : Type) [Fintype O]
    [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) :
    (𝒯.shadow A).avail O F ↔ 𝒯.availT A A O F := Iff.rfl

theorem shadow_availExt (A : Type) [Fintype A] [DecidableEq A] (n : ℕ) (O : Type) [Fintype O]
    [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (𝒯.shadow A).availExt n O F ↔ 𝒯.availT (A × Fin n) (A × Fin n) O F := Iff.rfl

/-- The shadow family: one endomorphic theory on every carrier. -/
noncomputable def shadowFamily : TheoryFamily := fun S _ _ => 𝒯.shadow S

/-- **REGROUPING INVARIANCE IS DEFINITIONAL** for a typed theory. -/
theorem shadow_regroupingInvariant : RegroupingInvariant 𝒯.shadowFamily :=
  fun _ _ _ _ _ _ _ _ _ => Iff.rfl

/-- **RELABELLING INVARIANCE** of the shadow family is the typed relabelling rule. -/
theorem shadow_relabellingInvariant : RelabellingInvariant 𝒯.shadowFamily := by
  intro S S' _ _ _ _ e O _ _ F h
  exact 𝒯.relabel S S S' S' e e O F h

theorem shadow_isAmbientMember (A : Type) [Fintype A] [DecidableEq A] :
    IsAmbientMember (𝒯.shadow A) 𝒯.shadowFamily :=
  ⟨fun _ _ _ _ => Iff.rfl, fun _ _ _ _ _ _ => Iff.rfl⟩

/-- **EVERY SHADOW IS AN EMBEDDED-OBSERVATION THEORY**: the product-type cross-carrier
coherence is automatic for a typed theory. -/
theorem shadow_embeddedObservation (A : Type) [Fintype A] [DecidableEq A] :
    EmbeddedObservation (𝒯.shadow A) :=
  ⟨𝒯.shadowFamily, 𝒯.shadow_regroupingInvariant, 𝒯.shadow_relabellingInvariant,
    𝒯.shadow_isAmbientMember A⟩

/-- **THE SHADOW HYPOTHESIS**: the endomorphic shadow is exact finite endomorphic quantum
mechanics on every nonempty carrier — what Level I supplies. -/
def ShadowQuantum : Prop :=
  ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A],
    ExactAllFiniteEndomorphicQuantumOps (𝒯.shadow A)

#print axioms availT_equiv
#print axioms shadow_regroupingInvariant
#print axioms shadow_relabellingInvariant
#print axioms shadow_isAmbientMember
#print axioms shadow_embeddedObservation

end TypedOperationalTheory

/-! ### Section D — slice embeddings and typed Kraus instruments -/

section Slices

variable {X Y : Type} [Fintype X] [DecidableEq X] [Fintype Y] [DecidableEq Y]

/-- Embed `X` into the slice `y` of `X × Y`. -/
def embL (X : Type) [Fintype X] [DecidableEq X] {Y : Type} [Fintype Y] [DecidableEq Y]
    (y : Y) : Matrix (X × Y) X ℂ :=
  fun p x => if p.1 = x ∧ p.2 = y then 1 else 0

/-- Embed `Y` into the slice `x` of `X × Y`. -/
def embR {X : Type} [Fintype X] [DecidableEq X] (Y : Type) [Fintype Y] [DecidableEq Y]
    (x : X) : Matrix (X × Y) Y ℂ :=
  fun p y => if p.1 = x ∧ p.2 = y then 1 else 0

theorem embL_apply (y : Y) (p : X × Y) (x : X) :
    embL X y p x = if p.1 = x ∧ p.2 = y then 1 else 0 := rfl

theorem embR_apply (x : X) (p : X × Y) (y : Y) :
    embR Y x p y = if p.1 = x ∧ p.2 = y then 1 else 0 := rfl

theorem embLH_apply (y : Y) (x : X) (p : X × Y) :
    (embL X y)ᴴ x p = if p.1 = x ∧ p.2 = y then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, embL_apply]
  split_ifs <;> simp

theorem embRH_apply (x : X) (y : Y) (p : X × Y) :
    (embR Y x)ᴴ y p = if p.1 = x ∧ p.2 = y then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, embR_apply]
  split_ifs <;> simp

/-- A slice embedding is an isometry. -/
theorem embL_isometry (y : Y) : (embL X y)ᴴ * embL X y = 1 := by
  ext x x'
  simp only [Matrix.mul_apply, embLH_apply, embL_apply, Matrix.one_apply]
  rw [Finset.sum_eq_single (x, y)
    (fun p _ hp => by
      simp [show ¬(p.1 = x ∧ p.2 = y) from fun h => hp (Prod.ext h.1 h.2)])
    (by simp)]
  simp

theorem embR_isometry (x : X) : (embR Y x)ᴴ * embR Y x = 1 := by
  ext y y'
  simp only [Matrix.mul_apply, embRH_apply, embR_apply, Matrix.one_apply]
  rw [Finset.sum_eq_single (x, y)
    (fun p _ hp => by
      simp [show ¬(p.1 = x ∧ p.2 = y) from fun h => hp (Prod.ext h.1 h.2)])
    (by simp)]
  simp

/-- The slice projectors sum to the identity. -/
theorem sum_embL_proj : ∑ y : Y, embL X y * (embL X y)ᴴ = 1 := by
  ext p q
  simp only [Matrix.sum_apply, Matrix.mul_apply, embL_apply, embLH_apply, Matrix.one_apply]
  rw [Finset.sum_eq_single p.2
    (fun y _ hy => Finset.sum_eq_zero fun x _ => by simp [Ne.symm hy]) (by simp)]
  rw [Finset.sum_eq_single p.1 (fun x _ hx => by simp [Ne.symm hx]) (by simp)]
  by_cases h : p = q
  · subst h; simp
  · have : ¬(q.1 = p.1 ∧ q.2 = p.2) := fun h' => h (Prod.ext h'.1.symm h'.2.symm)
    simp [this, h]

theorem sum_embR_proj : ∑ x : X, embR Y x * (embR Y x)ᴴ = 1 := by
  ext p q
  simp only [Matrix.sum_apply, Matrix.mul_apply, embR_apply, embRH_apply, Matrix.one_apply]
  rw [Finset.sum_eq_single p.1
    (fun x _ hx => Finset.sum_eq_zero fun y _ => by simp [Ne.symm hx]) (by simp)]
  rw [Finset.sum_eq_single p.2 (fun y _ hy => by simp [Ne.symm hy]) (by simp)]
  by_cases h : p = q
  · subst h; simp
  · have : ¬(q.1 = p.1 ∧ q.2 = p.2) := fun h' => h (Prod.ext h'.1.symm h'.2.symm)
    simp [this, h]

/-- Conjugating by a slice embedding places a matrix in the slice. -/
theorem embL_conj_apply (y : Y) (M : Matrix X X ℂ) (p q : X × Y) :
    (embL X y * M * (embL X y)ᴴ) p q = if p.2 = y ∧ q.2 = y then M p.1 q.1 else 0 := by
  simp only [Matrix.mul_apply, embL_apply, embLH_apply]
  rw [Finset.sum_eq_single q.1 (fun b _ hb => by simp [Ne.symm hb]) (by simp)]
  rw [Finset.sum_eq_single p.1 (fun a _ ha => by simp [Ne.symm ha]) (by simp)]
  simp only [true_and]
  split_ifs <;> simp_all

/-- Compressing by a slice embedding reads the slice. -/
theorem embR_compress_apply (x : X) (N : Matrix (X × Y) (X × Y) ℂ) (y y' : Y) :
    ((embR Y x)ᴴ * N * embR Y x) y y' = N (x, y) (x, y') := by
  simp only [Matrix.mul_apply, embR_apply, embRH_apply]
  rw [Finset.sum_eq_single (x, y')
    (fun q _ hq => by
      simp [show ¬(q.1 = x ∧ q.2 = y') from fun h => hq (Prod.ext h.1 h.2)])
    (by simp)]
  rw [Finset.sum_eq_single (x, y)
    (fun p _ hp => by
      simp [show ¬(p.1 = x ∧ p.2 = y) from fun h => hp (Prod.ext h.1 h.2)])
    (by simp)]
  simp

/-- Discarding the slice factor of a slice-placed matrix returns the matrix. -/
theorem discardR_embL_conj (y : Y) (M : Matrix X X ℂ) :
    discardR Y (embL X y * M * (embL X y)ᴴ) = M := by
  ext s t
  rw [discardR_apply]
  simp only [embL_conj_apply, and_self]
  simp [Finset.sum_ite_eq']

/-- The uniform attachment is the uniform mixture of the slice embeddings. -/
theorem attachUniform_eq_sum (M : Matrix X X ℂ) :
    attachUniform Y M = ((Fintype.card Y : ℂ))⁻¹ • ∑ y : Y, embL X y * M * (embL X y)ᴴ := by
  ext p q
  rw [attachUniform_apply]
  simp only [tensorOf_apply, Matrix.smul_apply, Matrix.sum_apply, Matrix.one_apply, smul_eq_mul,
    embL_conj_apply]
  by_cases h : p.2 = q.2
  · rw [if_pos h]
    have : ∑ y : Y, (if p.2 = y ∧ q.2 = y then M p.1 q.1 else 0) = M p.1 q.1 := by
      rw [← h]
      simp [Finset.sum_ite_eq]
    rw [this]
    ring
  · rw [if_neg h]
    have : ∑ y : Y, (if p.2 = y ∧ q.2 = y then M p.1 q.1 else 0) = 0 := by
      refine Finset.sum_eq_zero fun y _ => ?_
      rw [if_neg]
      rintro ⟨h1, h2⟩
      exact h (h1.trans h2.symm)
    rw [this]
    ring

end Slices

section Kraus

variable {S S' : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']

/-- Conjugation by a rectangular operator. -/
def conjT (K : Matrix S' S ℂ) : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ where
  toFun X := K * X * Kᴴ
  map_add' X Y := by simp only [Matrix.mul_add, Matrix.add_mul]
  map_smul' c X := by simp only [Matrix.mul_smul, Matrix.smul_mul, RingHom.id_apply]

omit [DecidableEq S] [Fintype S'] in
theorem conjT_apply (K : Matrix S' S ℂ) (X : Matrix S S ℂ) : conjT K X = K * X * Kᴴ := rfl

/-- **A TYPED KRAUS INSTRUMENT**: finitely many rectangular Kraus operators, normalized on
the input carrier, grouped by outcome. -/
def IsTypedKrausInstrument {m : ℕ} (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) : Prop :=
  ∃ (n : ℕ) (K : Fin (n + 1) → Matrix S' S ℂ) (out : Fin (n + 1) → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) ∧
      ∀ a, F a = ∑ k ∈ Finset.univ.filter (fun k => out k = a), conjT (K k)

omit [DecidableEq S'] in
/-- A Kraus family over any nonempty finite index is a typed Kraus instrument. -/
theorem isTypedKraus_of_family {m : ℕ} {ι : Type} [Fintype ι] [Nonempty ι]
    (K : ι → Matrix S' S ℂ) (out : ι → Fin m) (hn : ∑ i, (K i)ᴴ * K i = 1)
    (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (hF : ∀ a, F a = ∑ i ∈ Finset.univ.filter (fun i => out i = a), conjT (K i)) :
    IsTypedKrausInstrument F := by
  obtain ⟨n, hn'⟩ : ∃ n, Fintype.card ι = n + 1 :=
    Nat.exists_eq_succ_of_ne_zero Fintype.card_ne_zero
  let e : ι ≃ Fin (n + 1) := (Fintype.equivFin ι).trans (finCongr hn')
  refine ⟨n, fun k => K (e.symm k), fun k => out (e.symm k), ?_, fun a => ?_⟩
  · rw [← hn]
    exact Equiv.sum_comp e.symm (fun i => (K i)ᴴ * K i)
  · rw [hF a, Finset.sum_filter, Finset.sum_filter]
    exact (Equiv.sum_comp e.symm (fun i => if out i = a then conjT (K i) else 0)).symm

end Kraus

/-! ### Section E — exactness on a register, read through the typed theory -/

section Register

variable (𝒯 : TypedOperationalTheory)

/-- Under the shadow hypothesis every normalized square Kraus family on a nonempty register is
typed-available there. -/
theorem availT_of_krausFamily (hq : 𝒯.ShadowQuantum) {C : Type} [Fintype C] [DecidableEq C]
    [Nonempty C] {ι : Type} [Fintype ι] [Nonempty ι] (L : ι → Matrix C C ℂ) {m : ℕ}
    (out : ι → Fin m) (hn : ∑ i, (L i)ᴴ * L i = 1) :
    𝒯.availT C C (Fin m)
      (fun a => ∑ i ∈ Finset.univ.filter (fun i => out i = a), conjChannel (L i)) := by
  obtain ⟨n, hn'⟩ : ∃ n, Fintype.card ι = n + 1 :=
    Nat.exists_eq_succ_of_ne_zero Fintype.card_ne_zero
  let e : ι ≃ Fin (n + 1) := (Fintype.equivFin ι).trans (finCongr hn')
  have hK : IsFiniteEndomorphicKrausInstrument
      (instrumentBranch (fun k => L (e.symm k)) (fun k => out (e.symm k))) :=
    ⟨n, _, _, by rw [← hn]; exact Equiv.sum_comp e.symm (fun i => (L i)ᴴ * L i), rfl⟩
  have h : 𝒯.availT C C (Fin m)
      (instrumentBranch (fun k => L (e.symm k)) (fun k => out (e.symm k))) :=
    ((hq C).1 m _).mpr hK
  have hEq : (fun a => ∑ i ∈ Finset.univ.filter (fun i => out i = a), conjChannel (L i))
      = instrumentBranch (fun k => L (e.symm k)) (fun k => out (e.symm k)) := by
    funext a
    simp only [instrumentBranch]
    rw [Finset.sum_filter, Finset.sum_filter]
    exact (Equiv.sum_comp e.symm (fun i => if out i = a then conjChannel (L i) else 0)).symm
  rw [hEq]
  exact h

end Register

/-! ### Section F — soundness: typed-available families are typed Kraus instruments -/

section Soundness

variable (𝒯 : TypedOperationalTheory)
variable {S S' : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']

/-- The endomorphic wrapper of a typed map on the register `S × S'`: discard `S'`, apply, attach
a uniform `S`, and swap the factors back. -/
noncomputable def wrap (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) :
    Matrix (S × S') (S × S') ℂ →ₗ[ℂ] Matrix (S × S') (S × S') ℂ :=
  transportT (Equiv.refl (S' × S)) (Equiv.prodComm S' S) LinearMap.id
    ∘ₗ attachUniform S ∘ₗ Φ ∘ₗ discardR S'

/-- The wrapper is typed-available when the map is. -/
theorem wrap_availT [Nonempty S] {m : ℕ} (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (hF : 𝒯.availT S S' (Fin m) F) :
    𝒯.availT (S × S') (S × S') (Fin m) (fun a => wrap (F a)) := by
  have h1 := 𝒯.bind (S × S') S S' Unit (Fin m) (fun _ => discardR S') (fun _ => F)
    (𝒯.discard S S') (fun _ => hF)
  have h2 := 𝒯.bind (S × S') S' (S' × S) (Unit × Fin m) Unit _ (fun _ _ => attachUniform S) h1
    (fun _ => 𝒯.attach S' S)
  have hsw := 𝒯.relabel (S' × S) (S' × S) (S' × S) (S × S') (Equiv.refl _) (Equiv.prodComm S' S)
    Unit (fun _ => LinearMap.id) (𝒯.id (S' × S))
  have h3 := 𝒯.bind (S × S') (S' × S) (S × S') ((Unit × Fin m) × Unit) Unit _
    (fun _ _ => transportT (Equiv.refl (S' × S)) (Equiv.prodComm S' S) LinearMap.id) h2
    (fun _ => hsw)
  have h4 := 𝒯.availT_equiv
    (((Equiv.prodPUnit ((Unit × Fin m) × Unit)).trans (Equiv.prodPUnit (Unit × Fin m))).trans
      (Equiv.punitProd (Fin m))) _ h3
  exact h4

/-- The wrapper's entries. -/
theorem wrap_apply (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (X : Matrix (S × S') (S × S') ℂ)
    (p q : S × S') :
    wrap Φ X p q = (Φ (discardR S' X)) p.2 q.2 * (((Fintype.card S : ℂ))⁻¹ *
      (if p.1 = q.1 then 1 else 0)) := by
  simp only [wrap, LinearMap.comp_apply, transportT_apply, LinearMap.id_apply,
    Equiv.refl_symm, Equiv.refl_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    attachUniform_apply, tensorOf_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul,
    Equiv.prodComm_symm, Equiv.prodComm_apply, Prod.swap]

/-- The typed map is recovered from its wrapper by attaching a uniform `S'` and reading the
slices. -/
theorem recover_of_wrap [Nonempty S] [Nonempty S'] (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (X : Matrix S S ℂ) :
    Φ X = ∑ s : S, (embR S' s)ᴴ * wrap Φ (attachUniform S' X) * embR S' s := by
  ext v v'
  simp only [Matrix.sum_apply, embR_compress_apply, wrap_apply, discardR_attachUniform, if_true,
    mul_one, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  have hc : (Fintype.card S : ℂ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  field_simp

/-- **SOUNDNESS**: under the shadow hypothesis, a typed-available family between nonempty
carriers is a typed Kraus instrument. -/
theorem typedKraus_of_availT (hq : 𝒯.ShadowQuantum) [Nonempty S] [Nonempty S'] {m : ℕ}
    (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (hF : 𝒯.availT S S' (Fin m) F) :
    IsTypedKrausInstrument F := by
  have hH : (𝒯.shadow (S × S')).avail (Fin m) (fun a => wrap (F a)) := wrap_availT 𝒯 F hF
  obtain ⟨n, L, out, hL, hHL⟩ := ((hq (S × S')).1 m _).mp hH
  set c : ℝ := ((Fintype.card S' : ℝ))⁻¹ with hc
  set r : ℂ := (Real.sqrt c : ℂ) with hr
  have hr2 : star r * r = (c : ℂ) := by
    rw [hr, Complex.star_def, Complex.conj_ofReal, ← Complex.ofReal_mul,
      Real.mul_self_sqrt (by positivity)]
  have hc0 : (Fintype.card S' : ℂ) ≠ 0 := by exact_mod_cast Fintype.card_ne_zero
  have hcC : (c : ℂ) = ((Fintype.card S' : ℂ))⁻¹ := by
    rw [hc, Complex.ofReal_inv, Complex.ofReal_natCast]
  set M : Fin (n + 1) × (S × S') → Matrix S' S ℂ :=
    fun i => (embR S' i.2.1)ᴴ * L i.1 * embL S i.2.2 with hM
  refine isTypedKraus_of_family (fun i => r • M i) (fun i => out i.1) ?_ F fun a => ?_
  · -- normalization
    have hterm : ∀ i : Fin (n + 1) × (S × S'), (r • M i)ᴴ * (r • M i)
        = (c : ℂ) • ((embL S i.2.2)ᴴ * ((L i.1)ᴴ * ((embR S' i.2.1 * (embR S' i.2.1)ᴴ)
            * (L i.1 * embL S i.2.2)))) := by
      intro i
      rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, hr2]
      congr 1
      simp only [hM, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
        Matrix.mul_assoc]
    have hin : ∀ t : S', ∑ k : Fin (n + 1), ∑ s : S,
        (embL S t)ᴴ * ((L k)ᴴ * ((embR S' s * (embR S' s)ᴴ) * (L k * embL S t))) = 1 := by
      intro t
      have h1 : ∀ k : Fin (n + 1), ∑ s : S,
          (embL S t)ᴴ * ((L k)ᴴ * ((embR S' s * (embR S' s)ᴴ) * (L k * embL S t)))
            = (embL S t)ᴴ * (((L k)ᴴ * L k) * embL S t) := by
        intro k
        rw [← Matrix.mul_sum, ← Matrix.mul_sum, ← Matrix.sum_mul, sum_embR_proj, Matrix.one_mul,
          Matrix.mul_assoc]
      simp only [h1]
      rw [← Matrix.mul_sum, ← Matrix.sum_mul, hL, Matrix.one_mul, embL_isometry]
    calc ∑ i : Fin (n + 1) × (S × S'), (r • M i)ᴴ * (r • M i)
        = ∑ i : Fin (n + 1) × (S × S'), (c : ℂ) • ((embL S i.2.2)ᴴ * ((L i.1)ᴴ *
            ((embR S' i.2.1 * (embR S' i.2.1)ᴴ) * (L i.1 * embL S i.2.2)))) :=
          Finset.sum_congr rfl fun i _ => hterm i
      _ = (c : ℂ) • ∑ t : S', ∑ k : Fin (n + 1), ∑ s : S, (embL S t)ᴴ * ((L k)ᴴ *
            ((embR S' s * (embR S' s)ᴴ) * (L k * embL S t))) := by
          rw [Finset.smul_sum]
          simp only [Finset.smul_sum]
          rw [Fintype.sum_prod_type]
          simp only [Fintype.sum_prod_type]
          conv_lhs => arg 2; ext k; rw [Finset.sum_comm]
          exact Finset.sum_comm
      _ = 1 := by
          simp only [hin, Finset.sum_const, Finset.card_univ]
          rw [hcC, ← Nat.cast_smul_eq_nsmul ℂ, smul_smul, inv_mul_cancel₀ hc0, one_smul]
  · -- the branches
    refine LinearMap.ext fun X => ?_
    have hcomp : ∀ (s : S) (N : Matrix (S × S') (S × S') ℂ),
        (embR S' s)ᴴ * (N * attachUniform S' X * Nᴴ) * embR S' s
          = ∑ t : S', (c : ℂ) • ((((embR S' s)ᴴ * N * embL S t) * X)
              * ((embR S' s)ᴴ * N * embL S t)ᴴ) := by
      intro s N
      rw [attachUniform_eq_sum, ← hcC]
      simp only [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_sum, Matrix.sum_mul,
        Finset.smul_sum, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
        Matrix.mul_assoc]
    rw [recover_of_wrap (F a) X, congrFun hHL a]
    simp only [instrumentBranch, LinearMap.sum_apply, Finset.sum_filter, Matrix.mul_sum,
      Matrix.sum_mul]
    rw [Finset.sum_comm, Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun k _ => ?_
    by_cases hk : out k = a
    · simp only [hk, if_true, Fintype.sum_prod_type]
      refine Finset.sum_congr rfl fun s _ => ?_
      rw [conjChannel_apply, hcomp]
      refine Finset.sum_congr rfl fun t _ => ?_
      rw [conjT_apply]
      simp only [hM]
      rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul,
        smul_smul, hr2]
    · simp [hk]

end Soundness

/-! ### Section G — completeness: typed Kraus instruments are typed-available -/

section Completeness

variable (𝒯 : TypedOperationalTheory)
variable {S S' : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']

/-- The register relabelling `S × (S' × Fin (n+1)) ≃ S' × (S × Fin (n+1))`. -/
def shuffle (S S' : Type) (n : ℕ) : (S × (S' × Fin (n + 1))) ≃ (S' × (S × Fin (n + 1))) where
  toFun p := (p.2.1, (p.1, p.2.2))
  invFun q := (q.2.1, (q.1, q.2.2))
  left_inv _ := rfl
  right_inv _ := rfl

/-- Embed `S` into the ancilla slice `(v, w)` of the register `S' × (S × Fin (n+1))`. -/
def emb2 (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] (n : ℕ)
    (v : S') (w : Fin (n + 1)) : Matrix (S' × (S × Fin (n + 1))) S ℂ :=
  fun q u => if q.1 = v ∧ q.2.1 = u ∧ q.2.2 = w then 1 else 0

theorem emb2_apply (n : ℕ) (v : S') (w : Fin (n + 1)) (q : S' × (S × Fin (n + 1))) (u : S) :
    emb2 S S' n v w q u = if q.1 = v ∧ q.2.1 = u ∧ q.2.2 = w then 1 else 0 := rfl

theorem emb2H_apply (n : ℕ) (v : S') (w : Fin (n + 1)) (u : S) (q : S' × (S × Fin (n + 1))) :
    (emb2 S S' n v w)ᴴ u q = if q.1 = v ∧ q.2.1 = u ∧ q.2.2 = w then 1 else 0 := by
  rw [Matrix.conjTranspose_apply, emb2_apply]
  split_ifs <;> simp

/-- The ancilla-slice projectors sum to the identity. -/
theorem sum_emb2_proj (n : ℕ) :
    ∑ r : S' × Fin (n + 1), emb2 S S' n r.1 r.2 * (emb2 S S' n r.1 r.2)ᴴ = 1 := by
  ext p q
  simp only [Matrix.sum_apply, Matrix.mul_apply, emb2_apply, emb2H_apply, Matrix.one_apply]
  rw [Finset.sum_eq_single (p.1, p.2.2)
    (fun r _ hr => Finset.sum_eq_zero fun u _ => by
      simp [show ¬(p.1 = r.1 ∧ p.2.1 = u ∧ p.2.2 = r.2) from
        fun h => hr (Prod.ext h.1.symm h.2.2.symm)])
    (by simp)]
  rw [Finset.sum_eq_single p.2.1 (fun u _ hu => by simp [Ne.symm hu]) (by simp)]
  by_cases h : p = q
  · subst h; simp
  · have : ¬(q.1 = p.1 ∧ q.2.1 = p.2.1 ∧ q.2.2 = p.2.2) :=
      fun h' => h (Prod.ext h'.1.symm (Prod.ext h'.2.1.symm h'.2.2.symm))
    simp [this, h]

/-- Compressing the relabelled uniform attachment by an ancilla slice reads the input state. -/
theorem emb2_compress (n : ℕ) (X : Matrix S S ℂ) (v : S') (w : Fin (n + 1)) :
    (emb2 S S' n v w)ᴴ *
        Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X)
      * emb2 S S' n v w
      = ((Fintype.card (S' × Fin (n + 1)) : ℂ))⁻¹ • X := by
  ext u u'
  simp only [Matrix.mul_apply, emb2_apply, emb2H_apply]
  rw [Finset.sum_eq_single (v, (u', w))
    (fun q _ hq => by
      simp [show ¬(q.1 = v ∧ q.2.1 = u' ∧ q.2.2 = w) from
        fun h => hq (Prod.ext h.1 (Prod.ext h.2.1 h.2.2))])
    (by simp)]
  rw [Finset.sum_eq_single (v, (u, w))
    (fun q _ hq => by
      simp [show ¬(q.1 = v ∧ q.2.1 = u ∧ q.2.2 = w) from
        fun h => hq (Prod.ext h.1 (Prod.ext h.2.1 h.2.2))])
    (by simp)]
  simp [Matrix.reindex_apply, Matrix.submatrix_apply, shuffle, attachUniform_apply,
    tensorOf_apply, Matrix.smul_apply]
  ring

/-- The register operator placing `K_k` on the output factor and recording `k` on the ancilla,
for the ancilla initially in the basis state `(v, w)`. -/
def regOp (s₀ : S) {n : ℕ} (K : Fin (n + 1) → Matrix S' S ℂ)
    (i : Fin (n + 1) × (S' × Fin (n + 1))) :
    Matrix (S' × (S × Fin (n + 1))) (S' × (S × Fin (n + 1))) ℂ :=
  embL S' (s₀, i.1) * K i.1 * (emb2 S S' n i.2.1 i.2.2)ᴴ

/-- The register operators are a normalized Kraus family. -/
theorem regOp_normalized (s₀ : S) {n : ℕ} (K : Fin (n + 1) → Matrix S' S ℂ)
    (hn : ∑ k, (K k)ᴴ * K k = 1) :
    ∑ i : Fin (n + 1) × (S' × Fin (n + 1)), (regOp s₀ K i)ᴴ * regOp s₀ K i = 1 := by
  have h1 : ∀ i : Fin (n + 1) × (S' × Fin (n + 1)),
      (regOp s₀ K i)ᴴ * regOp s₀ K i
        = emb2 S S' n i.2.1 i.2.2 * (((K i.1)ᴴ * K i.1) * (emb2 S S' n i.2.1 i.2.2)ᴴ) := by
    intro i
    simp only [regOp, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (embL S' (s₀, i.1))ᴴ, embL_isometry, Matrix.one_mul]
  simp only [h1]
  rw [Fintype.sum_prod_type, Finset.sum_comm]
  simp only [← Matrix.sum_mul, ← Matrix.mul_sum, hn, Matrix.one_mul]
  exact sum_emb2_proj n

/-- Discarding the ancilla after a register operator yields the Kraus branch, scaled by the
ancilla weight. -/
theorem discardR_regOp_conj (s₀ : S) {n : ℕ} (K : Fin (n + 1) → Matrix S' S ℂ)
    (i : Fin (n + 1) × (S' × Fin (n + 1))) (X : Matrix S S ℂ) :
    discardR (S × Fin (n + 1))
      (regOp s₀ K i *
        Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X)
        * (regOp s₀ K i)ᴴ)
      = ((Fintype.card (S' × Fin (n + 1)) : ℂ))⁻¹ • (K i.1 * X * (K i.1)ᴴ) := by
  have hre : regOp s₀ K i *
        Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X)
        * (regOp s₀ K i)ᴴ
      = embL S' (s₀, i.1) * (K i.1 * ((emb2 S S' n i.2.1 i.2.2)ᴴ *
          Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X)
          * emb2 S S' n i.2.1 i.2.2) * (K i.1)ᴴ) * (embL S' (s₀, i.1))ᴴ := by
    simp only [regOp, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      Matrix.mul_assoc]
  rw [hre, emb2_compress, discardR_embL_conj, Matrix.mul_smul, Matrix.smul_mul]

/-- **COMPLETENESS**: under the shadow hypothesis, a typed Kraus instrument between nonempty
carriers is typed-available. -/
theorem availT_of_typedKraus (hq : 𝒯.ShadowQuantum) [Nonempty S] [Nonempty S'] {m : ℕ}
    (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (hF : IsTypedKrausInstrument F) :
    𝒯.availT S S' (Fin m) F := by
  obtain ⟨n, K, out, hn, hFK⟩ := hF
  let s₀ : S := Classical.arbitrary S
  let G : Fin m → Matrix (S' × (S × Fin (n + 1))) (S' × (S × Fin (n + 1))) ℂ →ₗ[ℂ]
      Matrix (S' × (S × Fin (n + 1))) (S' × (S × Fin (n + 1))) ℂ :=
    fun a => ∑ i ∈ Finset.univ.filter (fun i => out i.1 = a), conjChannel (regOp s₀ K i)
  have hG : 𝒯.availT _ _ (Fin m) G :=
    availT_of_krausFamily 𝒯 hq (regOp s₀ K) (fun i => out i.1) (regOp_normalized s₀ K hn)
  have h1 := 𝒯.attach S (S' × Fin (n + 1))
  have hsh := 𝒯.relabel (S × (S' × Fin (n + 1))) (S × (S' × Fin (n + 1)))
    (S × (S' × Fin (n + 1))) (S' × (S × Fin (n + 1))) (Equiv.refl _) (shuffle S S' n) Unit
    (fun _ => LinearMap.id) (𝒯.id _)
  have h2 := 𝒯.bind S (S × (S' × Fin (n + 1))) (S' × (S × Fin (n + 1))) Unit Unit _
    (fun _ _ => transportT (Equiv.refl _) (shuffle S S' n) LinearMap.id) h1 (fun _ => hsh)
  have h3 := 𝒯.bind S (S' × (S × Fin (n + 1))) (S' × (S × Fin (n + 1))) (Unit × Unit) (Fin m) _
    (fun _ => G) h2 (fun _ => hG)
  have h4 := 𝒯.bind S (S' × (S × Fin (n + 1))) S' ((Unit × Unit) × Fin m) Unit _
    (fun _ _ => discardR (S × Fin (n + 1))) h3 (fun _ => 𝒯.discard S' (S × Fin (n + 1)))
  have h5 := 𝒯.availT_equiv
    ((Equiv.prodPUnit ((Unit × Unit) × Fin m)).trans
      ((Equiv.prodCongr (Equiv.prodPUnit Unit) (Equiv.refl (Fin m))).trans
        (Equiv.punitProd (Fin m)))) _ h4
  convert h5 using 1
  funext a
  refine LinearMap.ext fun X => ?_
  have hcard : ((Fintype.card (S' × Fin (n + 1)) : ℂ)) ≠ 0 := by
    exact_mod_cast Fintype.card_ne_zero
  show F a X = discardR (S × Fin (n + 1)) (G a (transportT (Equiv.refl _) (shuffle S S' n)
    LinearMap.id (attachUniform (S' × Fin (n + 1)) X)))
  have hY : transportT (Equiv.refl (S × (S' × Fin (n + 1)))) (shuffle S S' n) LinearMap.id
      (attachUniform (S' × Fin (n + 1)) X)
      = Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X) := by
    rw [transportT_apply, LinearMap.id_apply, Equiv.refl_symm, Matrix.reindex_refl_refl]
  have hterm : ∀ i : Fin (n + 1) × (S' × Fin (n + 1)),
      discardR (S × Fin (n + 1)) (conjChannel (regOp s₀ K i)
        (Matrix.reindex (shuffle S S' n) (shuffle S S' n) (attachUniform (S' × Fin (n + 1)) X)))
        = ((Fintype.card (S' × Fin (n + 1)) : ℂ))⁻¹ • (K i.1 * X * (K i.1)ᴴ) := fun i => by
    rw [conjChannel_apply, discardR_regOp_conj]
  rw [hFK a, hY]
  simp only [G, LinearMap.sum_apply, map_sum, Finset.sum_filter]
  rw [Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun k _ => ?_
  by_cases hk : out k = a
  · simp only [hk, if_true]
    rw [conjT_apply]
    calc K k * X * (K k)ᴴ
        = ∑ _r : S' × Fin (n + 1),
            ((Fintype.card (S' × Fin (n + 1)) : ℂ))⁻¹ • (K k * X * (K k)ᴴ) := by
          rw [Finset.sum_const, Finset.card_univ, ← Nat.cast_smul_eq_nsmul ℂ, smul_smul,
            mul_inv_cancel₀ hcard, one_smul]
      _ = _ := Finset.sum_congr rfl fun r _ => (hterm (k, r)).symm
  · simp [hk]

end Completeness

/-! ### Section H — the determination theorem -/

section Determination

variable (𝒯 : TypedOperationalTheory)

/-- **THE TYPED THEORY IS DETERMINED BY ITS ENDOMORPHIC SHADOW**: under the shadow
hypothesis, between nonempty finite carriers a family is typed-available exactly when it is a
typed Kraus instrument. -/
theorem typed_determined (hq : 𝒯.ShadowQuantum) :
    ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Nonempty S]
      [Nonempty S'] (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
      𝒯.availT S S' (Fin m) F ↔ IsTypedKrausInstrument F :=
  fun _ _ _ _ _ _ _ _ _ F =>
    ⟨typedKraus_of_availT 𝒯 hq F, availT_of_typedKraus 𝒯 hq F⟩

/-- On one carrier, rectangular conjugation is the endomorphic conjugation. -/
theorem conjT_eq_conjChannel {A : Type} [Fintype A] [DecidableEq A] (K : Matrix A A ℂ) :
    conjT K = conjChannel K := rfl

/-- On one carrier, a typed Kraus instrument is exactly an endomorphic Kraus instrument. -/
theorem typedKraus_iff_endomorphic {A : Type} [Fintype A] [DecidableEq A] {m : ℕ}
    (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) :
    IsTypedKrausInstrument F ↔ IsFiniteEndomorphicKrausInstrument F := by
  constructor
  · rintro ⟨n, K, out, hn, hF⟩
    exact ⟨n, K, out, hn, funext fun a => hF a⟩
  · rintro ⟨n, K, out, hn, hF⟩
    exact ⟨n, K, out, hn, fun a => congrFun hF a⟩

/-- **THE CONVERSE**: a typed theory whose available families between nonempty carriers are
exactly the typed Kraus instruments has a quantum shadow. -/
theorem shadowQuantum_of_typed
    (h : ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Nonempty S]
      [Nonempty S'] (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
      𝒯.availT S S' (Fin m) F ↔ IsTypedKrausInstrument F) : 𝒯.ShadowQuantum := by
  intro A _ _ _
  refine ⟨fun m F => ?_, fun k m F => ?_⟩
  · rw [TypedOperationalTheory.shadow_avail, h A A m F, typedKraus_iff_endomorphic]
  · rw [TypedOperationalTheory.shadow_availExt, h (A × Fin (k + 1)) (A × Fin (k + 1)) m F,
      typedKraus_iff_endomorphic]

/-- **THE DETERMINATION, BOTH WAYS**: the shadow is quantum on every nonempty carrier exactly
when the typed theory is the finite typed quantum theory. -/
theorem typed_determined_iff :
    𝒯.ShadowQuantum ↔
      ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Nonempty S]
        [Nonempty S'] (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
        𝒯.availT S S' (Fin m) F ↔ IsTypedKrausInstrument F :=
  ⟨typed_determined 𝒯, shadowQuantum_of_typed 𝒯⟩

/-- **IN THE LEVEL I VOCABULARY**: if every shadow satisfies OI⁺ in its primitive-source form,
the typed theory is the finite typed quantum theory. -/
theorem typed_determined_of_oiPlusElem
    (h : ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A], OIPlusElem (𝒯.shadow A)) :
    ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Nonempty S]
      [Nonempty S'] (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
      𝒯.availT S S' (Fin m) F ↔ IsTypedKrausInstrument F :=
  typed_determined 𝒯 fun A _ _ _ => (carrier_general_oiPlusElem A (𝒯.shadow A)).mp (h A)

end Determination

/-! ### Section I — the interface carries no quantum content -/

section NoSmuggling

variable {S S' T T' R : Type} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
  [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] [Fintype R] [DecidableEq R]

theorem preservesDiag_transportT (e : S ≃ T) (e' : S' ≃ T')
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ} (h : PreservesDiag Φ) :
    PreservesDiag (transportT e e' Φ) := by
  intro w
  obtain ⟨w', hw'⟩ := h (w ∘ e)
  refine ⟨w' ∘ e'.symm, ?_⟩
  rw [transportT_apply]
  simp only [Matrix.reindex_apply, Equiv.symm_symm]
  rw [Matrix.submatrix_diagonal_equiv, hw', Matrix.submatrix_diagonal_equiv]

theorem preservesDiag_attachUniform : PreservesDiag (attachUniform (S := S) R) := by
  intro w
  refine ⟨fun p => w p.1 * ((Fintype.card R : ℂ))⁻¹, ?_⟩
  ext p q
  rw [attachUniform_apply]
  simp only [tensorOf_apply, Matrix.diagonal_apply, Matrix.smul_apply, Matrix.one_apply,
    smul_eq_mul, Prod.ext_iff]
  split_ifs <;> simp_all

theorem preservesDiag_discardR : PreservesDiag (discardR (S := S) R) := by
  intro w
  refine ⟨fun s => ∑ r : R, w (s, r), ?_⟩
  ext s t
  rw [discardR_apply]
  by_cases h : s = t
  · subst h
    simp
  · simp [h]

omit [Fintype S] in
theorem preservesDiag_localLuders (k : R) :
    PreservesDiag (localLuders (A := S) k) := by
  intro w
  refine ⟨fun p => if p.2 = k then w (p.1, k) else 0, ?_⟩
  ext p q
  show (if p.2 = k ∧ q.2 = k then (Matrix.diagonal w) (p.1, k) (q.1, k) else 0) = _
  simp only [Matrix.diagonal_apply, Prod.ext_iff]
  split_ifs <;> simp_all

/-- **THE TYPED DIAGONAL THEORY**: a family is available exactly when every branch preserves
diagonal matrices. It satisfies every rule of the interface. -/
noncomputable def typedDiag : TypedOperationalTheory where
  availT := fun _ _ _ _ _ _ _ _ _ F => ∀ a, PreservesDiag (F a)
  id := fun _ _ _ _ => preservesDiag_id
  coarse := fun _ _ _ _ _ _ _ _ _ _ _ _ _ _ h _ =>
    preservesDiag_sum _ _ fun j _ => h j
  bind := fun _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ hF hG c =>
    preservesDiag_comp (hG c.1 c.2) (hF c.1)
  relabel := fun _ _ _ _ _ _ _ _ _ _ _ _ e e' _ _ _ _ h a =>
    preservesDiag_transportT e e' (h a)
  attach := fun _ _ _ _ _ _ _ _ => preservesDiag_attachUniform
  discard := fun _ _ _ _ _ _ _ => preservesDiag_discardR
  readout := fun _ _ _ _ _ _ k => localLuders k
  readout_avail := fun _ _ _ _ _ _ k => preservesDiag_localLuders k
  readout_local := fun _ _ _ _ _ _ k => (mapSpectatorIndependent_iff_localLuders k _).mpr rfl

/-- The typed diagonal theory's qubit shadow has no composite unitary control. -/
theorem typedDiag_shadow_not_control :
    ¬ HasCompositeUnitaryControl (typedDiag.shadow (Fin 2)) := by
  intro h
  have := h 1 rot rot_isometry
  exact rot_not_preservesDiag (this ())

/-- **THE INTERFACE CARRIES NO QUANTUM CONTENT**: the typed diagonal theory satisfies every
rule and its shadow is not quantum mechanics. -/
theorem typedDiag_shadow_not_qm :
    ¬ ExactAllFiniteEndomorphicQuantumOps (typedDiag.shadow (Fin 2)) :=
  fun h => typedDiag_shadow_not_control (physical_of_exactAll _ h).2.2.1

theorem typed_interface_not_quantum : ∃ 𝒯 : TypedOperationalTheory, ¬ 𝒯.ShadowQuantum :=
  ⟨typedDiag, fun h => typedDiag_shadow_not_qm (h (Fin 2))⟩

end NoSmuggling

#print axioms attachUniform_fin
#print axioms discardR_fin
#print axioms discardR_attachUniform
#print axioms embL_isometry
#print axioms embR_isometry
#print axioms sum_embL_proj
#print axioms sum_embR_proj
#print axioms embL_conj_apply
#print axioms embR_compress_apply
#print axioms discardR_embL_conj
#print axioms attachUniform_eq_sum
#print axioms isTypedKraus_of_family
#print axioms availT_of_krausFamily
#print axioms wrap_availT
#print axioms wrap_apply
#print axioms recover_of_wrap
#print axioms typedKraus_of_availT
#print axioms sum_emb2_proj
#print axioms emb2_compress
#print axioms regOp_normalized
#print axioms discardR_regOp_conj
#print axioms availT_of_typedKraus
#print axioms typed_determined
#print axioms conjT_eq_conjChannel
#print axioms typedKraus_iff_endomorphic
#print axioms shadowQuantum_of_typed
#print axioms typed_determined_iff
#print axioms typed_determined_of_oiPlusElem
#print axioms preservesDiag_transportT
#print axioms preservesDiag_attachUniform
#print axioms preservesDiag_discardR
#print axioms preservesDiag_localLuders
#print axioms typedDiag_shadow_not_control
#print axioms typedDiag_shadow_not_qm
#print axioms typed_interface_not_quantum

end TypedCompletion
end OIBridge
