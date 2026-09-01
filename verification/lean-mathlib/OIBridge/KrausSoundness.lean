/-
  OIBridge/KrausSoundness.lean — the soundness half: from "every quantum instrument is
  available" to "exactly the quantum instruments are available".

  PHASE THREE, ROUND TWENTY-SIX. The Kraus round proved COMPLETENESS —
  `fullInstruments_of_control` delivers every normalized square Kraus family. That is an
  INCLUSION and not an identity:

      QM_instruments  ⊆  Ops(T),        proved.
      Ops(T)  =  QM_instruments,        NOT proved, and not implied.

  `FiniteOperationalTheory.avail` is an abstract predicate. Nothing in the structure stops a
  theory from carrying every operation the Kraus round constructs AND a transpose, a
  trace-amplifier, or any other non-quantum linear map. An everywhere-available theory
  satisfies composite unitary control and the capstone outright, and is still strictly
  larger than quantum mechanics. This file kernelizes that gap and closes it.

  §A — THE REPRESENTATION PREDICATE, and the one exact identity behind it.
  `IsFiniteEndomorphicKrausInstrument F` says `F` HAS a normalized square Kraus
  representation. `instrumentBranch_trace` is the fact that gives the predicate observable
  teeth: a normalized family is TRACE PRESERVING in the aggregate,
  `∑ₐ tr(Fₐ X) = tr X`, proved from `∑ₖ Kₖ† Kₖ = 1` by trace cyclicity alone. That single
  identity is what refutes every trace-scaling impostor.

  §B — SOUNDNESS AND EXACTNESS.

      `KrausSound T`                        every AVAILABLE system instrument has one
      `ExactFiniteEndomorphicQuantumOps T`  available ⟺ Kraus-representable

      ┌────────────────────────────────────────────────────────────────────┐
      │  `exact_iff_sound_and_full`:                                        │
      │      Exact  ⟺  KrausSound ∧ HasFullFiniteEndomorphicInstruments.    │
      └────────────────────────────────────────────────────────────────────┘

  The two conjuncts are the two INCLUSIONS, named separately because they are proved by
  completely different means: completeness is CONSTRUCTED (the Stinespring circuit),
  soundness is a RESTRICTION on what the theory admits and cannot be constructed at all.
  `exact_of_sound_control` then reads off the substantive corollary: soundness plus finite
  isometry extension plus composite unitary control gives the exact endpoint.
  `krausSound_trace_preserving` records what soundness buys operationally.

  §C — THE COUNTERCONTROL, KERNELIZED. `everywhereAvailable` is a genuine
  `FiniteOperationalTheory` — every closure rule discharged, the derived readout structure
  intact — whose availability predicates are all `True`. It HAS composite unitary control
  and therefore full instrument richness, and it is NOT sound: `traceAmplifier_not_kraus`
  exhibits `ρ ↦ 2ρ` as an available one-outcome map with no Kraus representation, refuted
  by §A's trace identity. So `everywhereAvailable_full_not_exact` proves

      compositionality + control  ⟹  quantum COMPLETENESS,
      quantum SOUNDNESS is additionally required for exact quantum operational content,

  and the second line is now a theorem rather than a caveat.

  WHAT THIS ROUND DOES NOT CLAIM. `HasCompositeUnitaryControl` is a SUFFICIENT Stinespring
  architecture for richness, not a necessary condition for exact system-level quantum
  operations: a theory could make every instrument on `A` primitive without exposing
  arbitrary unitary control on every `A × Fin n`, exactly as universal operational control
  did not imply the round-nineteen Lie certificate (`centralDrift_not_HControl`). So the
  eventual characterization is NOT `QM ⟺ H_comp ∧ H_compositeControl`. Both control
  principles are constructive sufficient certificates for richness; neither is a definition
  of quantum mechanics. The non-necessity countermodel is NOT built here — it needs a second
  full theory whose `availExt` omits some unitary while still carrying the readout — and
  nothing in this file asserts it.

  THE THREE AXES, as they now stand: COMPOSITION (rounds 24/25), quantum SOUNDNESS (this
  round), quantum COMPLETENESS (the Kraus round). The remaining interface is that
  round twenty-four's `HComp` speaks about coherent completions of OI intervention words
  while `FiniteOperationalTheory` speaks about operational circuits; those are not yet one
  object, and conjoining predicates on unrelated parameters would not make them one.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.StinespringAssembly

namespace OIBridge
namespace KrausSoundness

open Complex Matrix MonoidalCompletion
open OperationalAssembly StinespringAssembly

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — the representation predicate, and the identity behind it -/

/-- **A NORMALIZED KRAUS FAMILY IS TRACE PRESERVING IN THE AGGREGATE.** Summed over the
outcome label, `∑ₐ tr(Fₐ X) = tr X`. Proved from `∑ₖ Kₖ† Kₖ = 1` by fibrewise regrouping
and trace cyclicity; no positivity and no completeness assumption enters.

This is the identity that gives the representation predicate observable teeth: any map that
scales the trace is thereby NOT Kraus-representable, whatever else is true of it. -/
theorem instrumentBranch_trace {n m : ℕ} (K : Fin n → Matrix A A ℂ)
    (out : Fin n → Fin m) (hnorm : ∑ k, (K k)ᴴ * K k = 1) (X : Matrix A A ℂ) :
    ∑ a, ((instrumentBranch K out a) X).trace = X.trace := by
  have hbranch : ∀ a : Fin m, ((instrumentBranch K out a) X).trace
      = ∑ k ∈ Finset.univ.filter (fun k => out k = a), (K k * X * (K k)ᴴ).trace := by
    intro a
    rw [instrumentBranch, LinearMap.sum_apply, Matrix.trace_sum]
    rfl
  rw [Finset.sum_congr rfl fun a _ => hbranch a,
    Finset.sum_fiberwise_of_maps_to (fun k _ => Finset.mem_univ (out k))
      (fun k => (K k * X * (K k)ᴴ).trace)]
  have hcyc : ∀ k, (K k * X * (K k)ᴴ).trace = ((K k)ᴴ * K k * X).trace := by
    intro k
    rw [Matrix.trace_mul_comm, Matrix.mul_assoc]
  rw [Finset.sum_congr rfl fun k _ => hcyc k, ← Matrix.trace_sum, ← Finset.sum_mul, hnorm,
    Matrix.one_mul]

/-- **THE REPRESENTATION PREDICATE.** `F` is a finite ENDOMORPHIC Kraus instrument when it
HAS a normalized square Kraus representation with some classical output map. Stated as an
existential over the representation rather than through a CP/Kraus classification theorem,
so no external analytic fact is consumed. -/
def IsFiniteEndomorphicKrausInstrument {m : ℕ}
    (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) : Prop :=
  ∃ (n : ℕ) (K : Fin (n + 1) → Matrix A A ℂ) (out : Fin (n + 1) → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) ∧ F = instrumentBranch K out

/-- The predicate is satisfied by exactly what the Kraus round constructs. -/
theorem instrumentBranch_isKraus {n m : ℕ} (K : Fin (n + 1) → Matrix A A ℂ)
    (out : Fin (n + 1) → Fin m) (hnorm : ∑ k, (K k)ᴴ * K k = 1) :
    IsFiniteEndomorphicKrausInstrument (instrumentBranch K out) :=
  ⟨n, K, out, hnorm, rfl⟩

/-! ### Section B — soundness and exactness -/

/-- **QUANTUM SOUNDNESS.** Every AVAILABLE system instrument has a normalized Kraus
representation. This is the inclusion the Kraus round does not touch, and it cannot be
constructed: it is a RESTRICTION on what the theory admits. -/
def KrausSound (T : FiniteOperationalTheory A) : Prop :=
  ∀ (m : ℕ) (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail (Fin m) F → IsFiniteEndomorphicKrausInstrument F

/-- **THE EXACT ENDPOINT.** Available ⟺ Kraus-representable: not merely that every finite
endomorphic quantum instrument is available, but that EXACTLY those are. -/
def ExactFiniteEndomorphicQuantumOps (T : FiniteOperationalTheory A) : Prop :=
  ∀ (m : ℕ) (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F

/-- **EXACTNESS SPLITS INTO THE TWO INCLUSIONS, AND INTO NOTHING ELSE.** The endpoint is
soundness together with completeness — no third condition is hiding in it, and neither
conjunct is redundant (§C refutes the direction that would make completeness suffice). -/
theorem exact_iff_sound_and_full (T : FiniteOperationalTheory A) :
    ExactFiniteEndomorphicQuantumOps T
      ↔ KrausSound T ∧ HasFullFiniteEndomorphicInstruments T := by
  constructor
  · intro h
    refine ⟨fun m F hF => (h m F).mp hF, fun n m K out hnorm => ?_⟩
    exact (h m (instrumentBranch K out)).mpr (instrumentBranch_isKraus K out hnorm)
  · rintro ⟨hs, hf⟩ m F
    refine ⟨hs m F, ?_⟩
    rintro ⟨n, K, out, hnorm, rfl⟩
    exact hf n m K out hnorm

/-- **THE SUBSTANTIVE COROLLARY.** Quantum soundness, finite isometry extension and
composite unitary control together give the EXACT endpoint: exactly the finite endomorphic
quantum instruments are available. The Kraus round supplies the completeness half
constructively; soundness is the only additional premise. -/
theorem exact_of_sound_control (T : FiniteOperationalTheory A)
    (hsound : KrausSound T) (hext : FiniteIsometryExtensionSF A)
    (hctrl : HasCompositeUnitaryControl T) :
    ExactFiniteEndomorphicQuantumOps T :=
  (exact_iff_sound_and_full T).mpr ⟨hsound, fullInstruments_of_control T hext hctrl⟩

/-- **WHAT SOUNDNESS BUYS OPERATIONALLY.** In a sound theory every available outcome family
conserves the trace when the outcome is forgotten — the observable content of the
restriction, and the property the countercontrol below violates. -/
theorem krausSound_trace_preserving (T : FiniteOperationalTheory A) (hsound : KrausSound T)
    {m : ℕ} (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) (hF : T.avail (Fin m) F)
    (X : Matrix A A ℂ) : ∑ a, ((F a) X).trace = X.trace := by
  obtain ⟨n, K, out, hnorm, rfl⟩ := hsound m F hF
  exact instrumentBranch_trace K out hnorm X

/-! ### Section C — the countercontrol -/

/-- **THE NON-QUANTUM WITNESS.** Doubling is a perfectly good linear map and a perfectly
good CP map; it is not a quantum instrument, because it doubles the trace and §A's identity
says a normalized Kraus family cannot. Nonemptiness is what makes the trace of the identity
matrix nonzero, and it is the only hypothesis. -/
theorem traceAmplifier_not_kraus [Nonempty A] :
    ¬ IsFiniteEndomorphicKrausInstrument
        (fun _ : Fin 1 => (2 : ℂ) • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)) := by
  rintro ⟨n, K, out, hnorm, hF⟩
  have htr := instrumentBranch_trace K out hnorm (1 : Matrix A A ℂ)
  rw [← hF] at htr
  rw [Fintype.sum_unique] at htr
  have h2 : (((2 : ℂ) • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ))
      (1 : Matrix A A ℂ)).trace = 2 * (Fintype.card A : ℂ) := by
    rw [LinearMap.smul_apply, LinearMap.id_apply, Matrix.trace_smul, Matrix.trace_one,
      smul_eq_mul]
  rw [h2, Matrix.trace_one] at htr
  exact (Nat.cast_ne_zero.mpr (Fintype.card_ne_zero (α := A))) (by linear_combination htr)

/-- **THE EVERYWHERE-AVAILABLE THEORY.** A genuine `FiniteOperationalTheory` — every
closure rule discharged and the derived readout structure intact, with `localLuders` as the
native readout so `readout_is_localLuders` and `pureSeedPrep_available` apply to it exactly
as to any other theory — whose availability predicates are all `True`. It is the theory that
contains everything, quantum or not. -/
def everywhereAvailable (A : Type*) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A where
  avail := fun _ _ _ _ => True
  availExt := fun _ _ _ _ _ => True
  avail_id := trivial
  avail_coarse := by intros; trivial
  availExt_coarse := by intros; trivial
  availExt_bind := by intros; trivial
  prepAvail := fun _ _ => True
  prepAvail_uniform := by intros; trivial
  prepAvail_post := by intros; trivial
  readout := fun _ k => localLuders k
  readout_avail := by intros; trivial
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by intros; trivial

/-- **THE EVERYWHERE-AVAILABLE THEORY IS NOT SOUND.** It admits the trace amplifier, which
has no Kraus representation. -/
theorem everywhereAvailable_not_sound [Nonempty A] :
    ¬ KrausSound (everywhereAvailable A) := fun h =>
  traceAmplifier_not_kraus (A := A)
    (h 1 (fun _ => (2 : ℂ) • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)) trivial)

/-- **COMPLETENESS DOES NOT GIVE EXACTNESS.** One theory that has composite unitary control,
therefore has every finite endomorphic quantum instrument, and is still strictly larger than
quantum mechanics. So the wording is forced: compositionality and control deliver quantum
COMPLETENESS; quantum SOUNDNESS is an additional requirement for exact quantum operational
content, and cannot be derived from richness. -/
theorem everywhereAvailable_full_not_exact [Nonempty A] :
    HasCompositeUnitaryControl (everywhereAvailable A)
      ∧ HasFullFiniteEndomorphicInstruments (everywhereAvailable A)
      ∧ ¬ ExactFiniteEndomorphicQuantumOps (everywhereAvailable A) :=
  ⟨fun _ _ _ => trivial, fun _ _ _ _ _ => trivial,
    fun h => everywhereAvailable_not_sound ((exact_iff_sound_and_full _).mp h).1⟩

#print axioms instrumentBranch_trace
#print axioms instrumentBranch_isKraus
#print axioms exact_iff_sound_and_full
#print axioms exact_of_sound_control
#print axioms krausSound_trace_preserving
#print axioms traceAmplifier_not_kraus
#print axioms everywhereAvailable_not_sound
#print axioms everywhereAvailable_full_not_exact

end KrausSoundness
end OIBridge
