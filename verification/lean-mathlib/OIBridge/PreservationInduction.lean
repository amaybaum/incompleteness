import OIBridge.ImplementationLocality

/-!
# Conditional preservation by protocol induction (round PRESERVE-INDUCT-1)

A carrier cone family `C` assigns to every finite carrier `S` a set `C S` of matrices, given as
data and not defined through availability. `instAvail_preserves` derives, by one induction over
the five constructors `op`, `readout`, `coarse`, `bind` and `discard` of `InstAvail`, that every
branch of every available family preserves `C S` from four hypotheses:

* `AdditiveClosure`: each `C S` contains zero and is closed under addition;
* `PrimitivePreservation`: each admitted isometric conjugation preserves `C S` (`op`), and so does
  each branch of an admitted native register readout (`readout`), a separate field because a
  nontrivial projection is not an isometry;
* `UniformAttachPreservation`: for `m > 0`, `uniformAttach m` sends `C S` into `C (S × Fin m)`;
* `AncillaDiscardPreservation`: for `m > 0`, `ptraceAnc m` sends `C (S × Fin m)` into `C S`.

`instAvail_sum_preserves` sums the branches. `instAvail_spectator_preserves` and
`instAvail_transport_preserves` apply the headline to `instAvail_spectator` and
`instAvail_transport`, with their context-stability and label-invariance hypotheses displayed.
The transport corollary concerns the cone assigned to the destination carrier; it does not
identify that cone with a reindexing of the source cone.

Scope: the four hypotheses are premises of the theorem, and no declaration here establishes them
for any physical preparation family. Positive semidefiniteness, Hermiticity, scaling, convexity,
closedness and normalization are not used.
-/

namespace OIBridge.PreservationInduction

open Matrix InterventionLocality OperationalAssembly ReferenceExtension MonoidalCompletion SpectatorBridge

abbrev CarrierConeFamily :=
  ∀ (S : Type) [Fintype S] [DecidableEq S], Set (Matrix S S ℂ)

structure AdditiveClosure (C : CarrierConeFamily) : Prop where
  zero_mem : ∀ (S : Type) [Fintype S] [DecidableEq S], (0 : Matrix S S ℂ) ∈ C S
  add_mem : ∀ (S : Type) [Fintype S] [DecidableEq S] (X Y : Matrix S S ℂ),
    X ∈ C S → Y ∈ C S → X + Y ∈ C S

def PreservesCarrier (C : CarrierConeFamily) (S : Type) [Fintype S] [DecidableEq S]
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X, X ∈ C S → Φ X ∈ C S

structure PrimitivePreservation (𝓘 : ImplementationClass) (C : CarrierConeFamily) : Prop where
  op : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
    𝓘 S K → Kᴴ * K = 1 → PreservesCarrier C S (conjChannel K)
  readout : ∀ (S T : Type) [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S),
    (∀ k, 𝓘 S (Matrix.reindex e e (readProj T m k))) →
    ∀ k, PreservesCarrier C S (conjChannel (Matrix.reindex e e (readProj T m k)))

def UniformAttachPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C S → uniformAttach m X ∈ C (S × Fin m)

def AncillaDiscardPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C (S × Fin m) → ptraceAnc m X ∈ C S

theorem finite_sum_mem (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {S : Type} [Fintype S] [DecidableEq S] {ι : Type} (s : Finset ι)
    (X : ι → Matrix S S ℂ) (hX : ∀ i ∈ s, X i ∈ C S) :
    (∑ i ∈ s, X i) ∈ C S := by
  classical
  revert hX
  induction s using Finset.induction_on with
  | empty => intro hX; simpa using hC.zero_mem S
  | @insert i s hi ih =>
    intro hX
    rw [Finset.sum_insert hi]
    exact hC.add_mem S _ _ (hX i (Finset.mem_insert_self i s))
      (ih fun j hj => hX j (Finset.mem_insert_of_mem hj))

theorem instAvail_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a) := by
  classical
  induction h with
  | op K hK hiso =>
    intro a
    exact hPrim.op _ K hK hiso
  | readout e hP =>
    intro k
    exact hPrim.readout _ _ _ e hP k
  | coarse f _ ih =>
    intro a X hX
    rw [LinearMap.sum_apply]
    exact finite_sum_mem C hC _ _ fun j _ => ih j X hX
  | bind _ _ ihF ihG =>
    intro a X hX
    exact ihG a.1 a.2 _ (ihF a.1 X hX)
  | discard hm _ ih =>
    intro a X hX
    simp only [discardWith, LinearMap.comp_apply]
    exact hDiscard _ _ hm _ (ih a _ (hAttach _ _ hm X hX))

theorem instAvail_sum_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    PreservesCarrier C S (∑ a, F a) := by
  classical
  intro X hX
  rw [LinearMap.sum_apply]
  exact finite_sum_mem C hC _ _ fun a _ =>
    instAvail_preserves C hC hPrim hAttach hDiscard h a X hX

theorem instAvail_spectator_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (R : Type) [Fintype R] [DecidableEq R]
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C (R × S) (amplRefL R (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_spectator hc hl R h)

theorem instAvail_transport_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hl : LabelInvariant 𝓘)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F)
    (S' : Type) [Fintype S'] [DecidableEq S'] (e : S ≃ S') :
    ∀ a, PreservesCarrier C S' (transport e (F a)) :=
  instAvail_preserves C hC hPrim hAttach hDiscard (instAvail_transport hl h S' e)

#print axioms instAvail_preserves
#print axioms instAvail_sum_preserves
#print axioms instAvail_spectator_preserves
#print axioms instAvail_transport_preserves

end OIBridge.PreservationInduction
