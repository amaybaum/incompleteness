/-
  OIBridge/EmbeddedObservation.lean — the primitive-source audit, first target: observer
  recursion derived from a regrouping-invariant embedded-observation principle, with the
  countercontrol that bare OI does not already supply it.

  ROUND FIFTY-SIX. OI⁺ (`CompletedOI.lean`, `CarrierGeneralOIPlus.lean`) is the OI core,
  well-formedness and three principles — observational independence, reversible richness,
  observer recursion — and it is equivalent to exact finite operational QM on every nonempty
  finite carrier. The next question is which of those ingredients are CONSTITUTIVE (part of
  what it means to observe) and which are DERIVED from something more primitive. This file
  settles the first entry of that audit.

  THE PRIMITIVE. Observer recursion (`ObserverRecursion`) says: for every level `n` there
  EXISTS a finite operational theory on `A × Fin n` whose system families are `T`'s level-`n`
  families and whose ancilla families are `T`'s transported higher-level families. Stated so,
  it is an existence claim made separately at each level. The deeper principle replaces the
  per-level existence by one uniform structure:

      EMBEDDED OBSERVATION. There is a family `𝒯` assigning a finite operational theory to
      EVERY finite carrier, such that
        (R) REGROUPING INVARIANCE — the level-`m` families of the observer at `S` are the
            system families of the observer at `S × Fin m` (`RegroupingInvariant`);
        (L) RELABELLING INVARIANCE — availability is transported along every bijection of
            carriers (`RelabellingInvariant`);
        (M) AMBIENCE — the given theory `T` is the family's member at its own carrier, on the
            system and at every positive level (`IsAmbientMember`).

  Nothing in (R), (L), (M) mentions a discard, a closure rule, or a shifted theory. What the
  derivation consumes from the embedded theories is only what every finite operational theory
  already carries: the identity, the uniform preparation with its discard rule, and the
  native readout — whose form is forced (`readout_is_localLuders`).

  WHAT IS DERIVED.
      · iterated ancilla closure (`closure_of_embedded`): the discard rule of the embedded
        observer at `A × Fin n`, read back through (R), (L), (M);
      · the identity and the relative readout at every level (`id_of_embedded`,
        `read_of_embedded`);
      · hence OBSERVER RECURSION (`observerRecursion_of_embeddedObservation`), through the
        round-53 construction `observerRecursion_of_closure`;
      · and, unasked for, SYSTEM-TO-LEVEL-ONE (`systemToLevelOne_of_embeddedObservation`):
        relabelling along `A ≃ A × Fin 1` is exactly the level-one seam. So one of the two
        admissibility clauses of well-formedness is not constitutive either; only composite
        operational validity remains as pure admissibility.

  NECESSITY. Exact finite operational QM satisfies the principle
  (`embeddedObservation_of_qm`): the family is the CP-instrument theory on every carrier
  (`cpTheory`, `cpFamily`), for which (R) is definitional and (L) is transport of complete
  positivity.

  THE COUNTERCONTROL. Bare OI does not supply the principle, and neither do the core,
  well-formedness, observational independence and reversible richness together
  (`embeddedObservation_independent`, `core_not_embeddedObservation`): the rank-gap theory
  carries all of them and has no iterated ancilla closure, hence no embedded-observation
  family.

  THE COMPRESSED PRINCIPLE SET. `OIPlusEmbedded` is composite operational validity,
  observational independence, reversible richness and embedded observation — the level-one
  seam is dropped because it is derived. Then `OIPlusEmbedded ⟺ exact finite operational
  QM` on every nonempty finite carrier (`carrier_general_oiPlusEmbedded`), and it is
  equivalent to carrier-general OI⁺ (`oiPlusEmbedded_iff_oiPlus`).

  WHAT IS NOT CLAIMED. The converse `ObserverRecursion → EmbeddedObservation` is not proved
  outside the OI⁺ context (inside it both are equivalent to QM). The independence of
  observational independence and of reversible richness from EMBEDDED observation is not
  re-established here; the round-53 witnesses establish it relative to observer recursion.
  Composite operational validity is treated as admissibility and no source for it is
  proposed. Nothing here bears on the sources of observational independence or of either
  clause of reversible richness; those are the remaining entries of the audit.
-/

import OIBridge.CarrierGeneralOIPlus

namespace OIBridge
namespace PrimitiveSource

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — the embedded-observation principle -/

section Principle

variable {A : Type} [Fintype A] [DecidableEq A]

/-- A finite operational theory at every finite carrier. -/
abbrev TheoryFamily :=
  ∀ (S : Type) [Fintype S] [DecidableEq S], FiniteOperationalTheory S

/-- **(R) REGROUPING INVARIANCE**: the positive-level families of the observer at `S` are the
system families of the observer at the regrouped carrier `S × Fin m`. -/
def RegroupingInvariant (𝒯 : TheoryFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ),
      (𝒯 S).availExt m O F ↔ (𝒯 (S × Fin m)).avail O F

/-- **(L) RELABELLING INVARIANCE**: availability is transported along every bijection of
carriers. -/
def RelabellingInvariant (𝒯 : TheoryFamily) : Prop :=
  ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] (e : S ≃ S')
    (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ),
    (𝒯 S).avail O F → (𝒯 S').avail O (fun a => transport e (F a))

/-- **(M) AMBIENCE**: `T` is the family's member at its own carrier, on the system and at
every positive level. Only the positive-level clause is consumed by the recursion derivation;
the system clause is consumed by the level-one seam. -/
def IsAmbientMember (T : FiniteOperationalTheory A) (𝒯 : TheoryFamily) : Prop :=
  (∀ (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail O F ↔ (𝒯 A).avail O F)
  ∧ ∀ (N : ℕ), 0 < N → ∀ (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ),
      T.availExt N O F ↔ (𝒯 A).availExt N O F

/-- **EMBEDDED OBSERVATION**: `T` is the ambient member of a regrouping- and
relabelling-invariant family of finite operational theories on all finite carriers. -/
def EmbeddedObservation (T : FiniteOperationalTheory A) : Prop :=
  ∃ 𝒯 : TheoryFamily, RegroupingInvariant 𝒯 ∧ RelabellingInvariant 𝒯 ∧ IsAmbientMember T 𝒯

end Principle

/-! ### Section B — what the principle yields -/

section Derivation

variable {A : Type} [Fintype A] [DecidableEq A]

/-- Level zero is available for every family, in the form needed under a product index. -/
theorem availExt_of_eq_zero (T : FiniteOperationalTheory A) :
    ∀ (N : ℕ) (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ),
      N = 0 → T.availExt N O F := by
  rintro N O _ _ F rfl
  exact availExt_zero T F

/-- Positive-level availability in `T` is system availability of the embedded observer at
`A × Fin N`: (M) then (R). -/
theorem availExt_iff_embedded {T : FiniteOperationalTheory A} {𝒯 : TheoryFamily}
    (hreg : RegroupingInvariant 𝒯) (hamb : IsAmbientMember T 𝒯) (N : ℕ) (hN : 0 < N)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ) :
    T.availExt N O F ↔ (𝒯 (A × Fin N)).avail O F :=
  (hamb.2 N hN O F).trans (hreg A N hN O F)

/-- The identity at every level: the embedded observer's `avail_id`. -/
theorem id_of_embedded {T : FiniteOperationalTheory A} {𝒯 : TheoryFamily}
    (hreg : RegroupingInvariant 𝒯) (hamb : IsAmbientMember T 𝒯) (n : ℕ) :
    T.availExt n Unit (fun _ => LinearMap.id) := by
  rcases n with _ | k
  · exact availExt_zero T _
  · exact (availExt_iff_embedded hreg hamb (k + 1) k.succ_pos Unit _).mpr
      (𝒯 (A × Fin (k + 1))).avail_id

/-- The relative readout at every level pair: the embedded observer's native readout, whose
form is forced, regrouped by (R) and relabelled along `shiftIdx` by (L). -/
theorem read_of_embedded {T : FiniteOperationalTheory A} {𝒯 : TheoryFamily}
    (hreg : RegroupingInvariant 𝒯) (hrel : RelabellingInvariant 𝒯)
    (hamb : IsAmbientMember T 𝒯) (n m : ℕ) :
    T.availExt (n * m) (Fin m)
      (fun k => transport (shiftIdx A n m) (localLuders (A := A × Fin n) k)) := by
  rcases n with _ | k
  · exact availExt_of_eq_zero T _ _ _ (Nat.zero_mul _)
  rcases m with _ | l
  · exact availExt_of_eq_zero T _ _ _ (Nat.mul_zero _)
  have hpos : 0 < (k + 1) * (l + 1) := Nat.mul_pos k.succ_pos l.succ_pos
  have h0 := (𝒯 (A × Fin (k + 1))).readout_avail (l + 1)
  have hro : (𝒯 (A × Fin (k + 1))).readout (l + 1)
      = fun j => localLuders (A := A × Fin (k + 1)) j :=
    funext (readout_is_localLuders _ _)
  rw [hro] at h0
  have h1 := (hreg (A × Fin (k + 1)) (l + 1) l.succ_pos (Fin (l + 1)) _).mp h0
  have h2 := hrel _ _ (shiftIdx A (k + 1) (l + 1)) (Fin (l + 1)) _ h1
  exact (availExt_iff_embedded hreg hamb _ hpos (Fin (l + 1)) _).mpr h2

/-- **ITERATED ANCILLA CLOSURE IS DERIVED**: the discard rule of the embedded observer at
`A × Fin n`, with the hypothesis carried in by (M), (R), (L) along `shiftIdx⁻¹` and the
conclusion carried out by (R), (M). -/
theorem closure_of_embedded {T : FiniteOperationalTheory A} {𝒯 : TheoryFamily}
    (hreg : RegroupingInvariant 𝒯) (hrel : RelabellingInvariant 𝒯)
    (hamb : IsAmbientMember T 𝒯) : IteratedAncillaClosure T := by
  intro n m O _ _ F hF
  rcases n with _ | k
  · exact availExt_zero T _
  have hpos : 0 < (k + 1) * (m + 1) := Nat.mul_pos k.succ_pos m.succ_pos
  have h1 : (𝒯 (A × Fin ((k + 1) * (m + 1)))).avail O
      (fun a => transport (shiftIdx A (k + 1) (m + 1)) (F a)) :=
    (availExt_iff_embedded hreg hamb _ hpos O _).mp hF
  have h2 := hrel _ _ (shiftIdx A (k + 1) (m + 1)).symm O _ h1
  simp only [transport_symm_transport] at h2
  have h3 : (𝒯 (A × Fin (k + 1))).availExt (m + 1) O F :=
    (hreg (A × Fin (k + 1)) (m + 1) m.succ_pos O F).mpr h2
  have h4 := (𝒯 (A × Fin (k + 1))).prepAvail_discard (m + 1) (uniformAttach (m + 1)) O F
    ((𝒯 (A × Fin (k + 1))).prepAvail_uniform m) h3
  exact (availExt_iff_embedded hreg hamb (k + 1) k.succ_pos O _).mpr h4

/-- **THE LEVEL-ONE SEAM IS DERIVED**: relabelling along `A ≃ A × Fin 1`. -/
theorem systemToLevelOne_of_embedded {T : FiniteOperationalTheory A} {𝒯 : TheoryFamily}
    (hreg : RegroupingInvariant 𝒯) (hrel : RelabellingInvariant 𝒯)
    (hamb : IsAmbientMember T 𝒯) : SystemToLevelOne T := by
  intro O _ _ F hF
  have h1 : (𝒯 A).avail O F := (hamb.1 O F).mp hF
  have h2 := hrel A (A × Fin 1) (levelOneIdx A).symm O F h1
  exact (availExt_iff_embedded hreg hamb 1 Nat.one_pos O _).mpr h2

theorem closure_of_embeddedObservation {T : FiniteOperationalTheory A}
    (h : EmbeddedObservation T) : IteratedAncillaClosure T := by
  obtain ⟨𝒯, hreg, hrel, hamb⟩ := h
  exact closure_of_embedded hreg hrel hamb

/-- **OBSERVER RECURSION IS DERIVED** from embedded observation. -/
theorem observerRecursion_of_embeddedObservation {T : FiniteOperationalTheory A}
    (h : EmbeddedObservation T) : ObserverRecursion T := by
  obtain ⟨𝒯, hreg, hrel, hamb⟩ := h
  exact observerRecursion_of_closure T (id_of_embedded hreg hamb) (read_of_embedded hreg hrel hamb)
    (closure_of_embedded hreg hrel hamb)

theorem systemToLevelOne_of_embeddedObservation {T : FiniteOperationalTheory A}
    (h : EmbeddedObservation T) : SystemToLevelOne T := by
  obtain ⟨𝒯, hreg, hrel, hamb⟩ := h
  exact systemToLevelOne_of_embedded hreg hrel hamb

end Derivation

/-! ### Section C — necessity: the CP-instrument family -/

section Necessity

/-- **THE CP-INSTRUMENT THEORY** on an arbitrary finite carrier: completely positive branches
with the trace preserved in aggregate, on the system and on every composite; preparations
are the uniform attachment followed by an available channel. -/
noncomputable def cpTheory (S : Type) [Fintype S] [DecidableEq S] :
    FiniteOperationalTheory S where
  avail := fun _ _ _ F => IsCPInstrument F
  availExt := fun _ _ _ _ F => IsCPInstrument F
  avail_id := ⟨fun _ => by rw [← conjChannel_one]; exact conjChannel_cp _, fun X => by
    rw [Fintype.sum_unique, LinearMap.id_apply]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => cp_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => 0 < n ∧ ∃ Φ, IsCPInstrument (fun _ : Unit => Φ)
    ∧ P = Φ.comp (uniformAttach n)
  prepAvail_uniform := fun n =>
    ⟨n.succ_pos, LinearMap.id,
      ⟨fun _ => by rw [← conjChannel_one]; exact conjChannel_cp _, fun X => by
        rw [Fintype.sum_unique, LinearMap.id_apply]⟩, by rw [LinearMap.id_comp]⟩
  prepAvail_post := by
    rintro n P Φ ⟨hn, Ψ, ⟨hΨcp, hΨtr⟩, rfl⟩ ⟨hΦcp, hΦtr⟩
    refine ⟨hn, Φ.comp Ψ, ⟨fun _ => cp_comp (hΦcp ()) (hΨcp ()), fun X => ?_⟩,
      by rw [LinearMap.comp_assoc]⟩
    rw [Fintype.sum_unique]
    have h1 := hΦtr (Ψ X)
    rw [Fintype.sum_unique] at h1
    have h2 := hΨtr X
    rw [Fintype.sum_unique] at h2
    exact h1.trans h2
  readout := fun _ k => localLuders k
  readout_avail := fun _ => ⟨fun k => localLuders_cp k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hn, Φ, ⟨hΦcp, hΦtr⟩, rfl⟩ ⟨hFcp, hFtr⟩
    refine ⟨fun a => ?_, fun X => ?_⟩
    · show IsCompletelyPositive (discardWith n (Φ.comp (uniformAttach n)) (F a))
      have h : discardWith n (Φ.comp (uniformAttach n)) (F a)
          = discardWith n (uniformAttach n) ((F a).comp Φ) := by
        simp only [discardWith, LinearMap.comp_assoc]
      rw [h]
      exact discardWith_uniform_cp (cp_comp (hFcp a) (hΦcp ()))
    · show ∑ a, ((discardWith n (Φ.comp (uniformAttach n)) (F a)) X).trace = X.trace
      rw [Finset.sum_congr rfl fun a _ => discardWith_trace n _ (F a) X, hFtr]
      have h := hΦtr (uniformAttach n X)
      rw [Fintype.sum_unique] at h
      exact h.trans (uniformAttach_trace n hn.ne' X)

/-- The CP-instrument family. -/
noncomputable def cpFamily : TheoryFamily := fun S _ _ => cpTheory S

/-- (R) holds definitionally for the CP-instrument family. -/
theorem cpFamily_regrouping : RegroupingInvariant cpFamily := by
  intro S _ _ m _ O _ _ F
  exact Iff.rfl

/-- (L) is transport of complete positivity and of the trace. -/
theorem cpFamily_relabelling : RelabellingInvariant cpFamily := by
  intro S S' _ _ _ _ e O _ _ F ⟨hcp, htr⟩
  refine ⟨fun a => transport_cp e (hcp a), fun X => ?_⟩
  simp only [trace_transport]
  rw [htr, trace_reindex]

variable {A : Type} [Fintype A] [DecidableEq A]

/-- (M) for an exact theory: exactness on the system and on every positive composite is
membership in the CP-instrument family at `A`. -/
theorem ambient_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : IsAmbientMember T cpFamily := by
  refine ⟨fun O _ _ F => ⟨fun hF => krausFamily_cp_tr (krausFamily_of_exactSystem T h.1 F hF),
    fun hF => ?_⟩, fun N hN O _ _ F => availExt_pos_iff T h.2 N hN F⟩
  obtain ⟨hcp, htr⟩ := hF
  exact avail_of_krausFamily_fin (fun O _ _ G => T.avail O G)
    (fun O O' _ _ _ _ G f hG => T.avail_coarse O O' G f hG) h.1 F
    (isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F hcp htr)

/-- **EXACT FINITE OPERATIONAL QM SATISFIES EMBEDDED OBSERVATION.** -/
theorem embeddedObservation_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : EmbeddedObservation T :=
  ⟨cpFamily, cpFamily_regrouping, cpFamily_relabelling, ambient_of_qm T h⟩

end Necessity

/-! ### Section D — the countercontrol -/

section Countercontrol

/-- The rank-gap theory has no embedded-observation family. -/
theorem gap_not_embeddedObservation : ¬ EmbeddedObservation gapTheory :=
  fun h => gap_not_iteratedAncillaClosure (closure_of_embeddedObservation h)

/-- **BARE OI DOES NOT SUPPLY EMBEDDED OBSERVATION**, nor do the core, well-formedness,
observational independence and reversible richness together. -/
theorem embeddedObservation_independent :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ObservationalIndependence T
      ∧ ReversibleRichness T ∧ ¬ EmbeddedObservation T :=
  ⟨gapTheory, gap_realizesSealedOICore, ⟨gap_validity, gap_systemToLevelOne⟩,
    (observationalIndependence_iff_inert _).mpr gap_inert,
    reversibleRichness_of_control _ ⟨gap_validity, gap_systemToLevelOne⟩ gap_control,
    gap_not_embeddedObservation⟩

theorem core_not_embeddedObservation :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ ¬ EmbeddedObservation T :=
  ⟨gapTheory, gap_realizesSealedOICore, gap_not_embeddedObservation⟩

end Countercontrol

/-! ### Section E — the compressed principle set -/

section Compressed

variable {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A)

/-- **THE COMPRESSED PRINCIPLE SET**: composite operational validity (admissibility),
observational independence, reversible richness, embedded observation. The level-one seam is
absent because it is derived. -/
def OIPlusEmbedded : Prop :=
  CompositeOperationalValidity T ∧ OIHierarchyGeneral.ObservationalIndependence T
    ∧ OIHierarchyGeneral.ReversibleRichness T ∧ EmbeddedObservation T

theorem oiPlus_of_oiPlusEmbedded (h : OIPlusEmbedded T) : OIHierarchyGeneral.OIPlus T :=
  ⟨⟨h.1, systemToLevelOne_of_embeddedObservation h.2.2.2⟩, h.2.1, h.2.2.1,
    observerRecursion_of_embeddedObservation h.2.2.2⟩

variable [Nonempty A]

theorem qm_of_oiPlusEmbedded (h : OIPlusEmbedded T) : ExactAllFiniteEndomorphicQuantumOps T :=
  OIHierarchyGeneral.qm_of_oiPlus T (oiPlus_of_oiPlusEmbedded T h)

theorem oiPlusEmbedded_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusEmbedded T :=
  have hp := OIHierarchyGeneral.oiPlus_of_qm T h
  ⟨hp.1.1, hp.2.1, hp.2.2.1, embeddedObservation_of_qm T h⟩

/-- **THE COMPRESSED SET ⟺ FINITE OPERATIONAL QM**, on any nonempty finite carrier. -/
theorem oiPlusEmbedded_iff_qm : OIPlusEmbedded T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusEmbedded T, oiPlusEmbedded_of_qm T⟩

/-- The compressed set is carrier-general OI⁺. -/
theorem oiPlusEmbedded_iff_oiPlus : OIPlusEmbedded T ↔ OIHierarchyGeneral.OIPlus T := by
  rw [oiPlusEmbedded_iff_qm, OIHierarchyGeneral.oiPlus_iff_qm]

end Compressed

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlusEmbedded :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (T : FiniteOperationalTheory A),
      OIPlusEmbedded T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlusEmbedded_iff_qm T

#print axioms availExt_of_eq_zero
#print axioms availExt_iff_embedded
#print axioms id_of_embedded
#print axioms read_of_embedded
#print axioms closure_of_embedded
#print axioms systemToLevelOne_of_embedded
#print axioms closure_of_embeddedObservation
#print axioms observerRecursion_of_embeddedObservation
#print axioms systemToLevelOne_of_embeddedObservation
#print axioms cpFamily_regrouping
#print axioms cpFamily_relabelling
#print axioms ambient_of_qm
#print axioms embeddedObservation_of_qm
#print axioms gap_not_embeddedObservation
#print axioms embeddedObservation_independent
#print axioms core_not_embeddedObservation
#print axioms oiPlus_of_oiPlusEmbedded
#print axioms qm_of_oiPlusEmbedded
#print axioms oiPlusEmbedded_of_qm
#print axioms oiPlusEmbedded_iff_qm
#print axioms oiPlusEmbedded_iff_oiPlus
#print axioms carrier_general_oiPlusEmbedded

end PrimitiveSource
end OIBridge
