import OIBridge.CompletedOI
import OIBridge.PassiveObservation

/-!
# Passive incompleteness is theory-insensitive, and carries no information about the OI core (OI-N4)

`OICore T` says that a finite operational theory `T` on the qubit realizes the sealed OI core:
the passive step and the control of the hidden-memory gadget are available as permutation
channels at ancilla level four, and the native readout reproduces the classical OI comb. It is a
statement about which operations `T` makes available. **Passive incompleteness** is the property
OI-N1 proved of the matrix algebra: no passive instrument separates states. This file relates the
two at the level of theories. The exact logic is asymmetric: one implication holds, vacuously,
and the other fails; what the two results show together is that passive incompleteness is
theory-insensitive and therefore non-discriminating with respect to the OI core.

* **Passive incompleteness is carrier-intrinsic** (`passivelyIncomplete_of_card`,
  `passivelyIncomplete_qubit`). Define `PassivelyIncomplete T`: no instrument *available in `T`*
  is both passive and state-separating. By N1 this holds for **every** theory on a carrier with
  at least two states, whatever `T` makes available. The property does not vary with `T`.
* **The OI core varies with `T`.** `diagTheory` realizes it (`diag_realizesSealedOICore`). The
  theory built here, `labelTheory` — every composite operation keeps the ancilla label, so
  nothing can move information between ancilla values — does not (`label_not_oiCore`): the OI
  control `τ` flips the ancilla's second bit and is therefore unavailable (`tau_moves_label`).
* **The diagram** (`passive_nondiscriminating`). `OICore T → PassivelyIncomplete T` holds for
  every `T`, but only vacuously: the consequent holds for every `T`, and the proof does not
  consult the hypothesis (`oiCore_to_passive_vacuous` is N1 alone). `PassivelyIncomplete T →
  OICore T` fails (`passivelyIncomplete_without_oiCore`, witness `labelTheory`). So passive
  incompleteness, being constant across theories, carries no discriminatory information about
  whether the OI core is realized. The two notions are orthogonal: one is fixed by the observable
  algebra, the other by the theory's hidden-memory and control structure.
* **What does vary is the sector, not the OI status** (`sector_diagram`). Relative to the
  commutative sector — diagonal states, diagonal passivity — both `diagTheory` and `labelTheory`
  are passively *complete* (the pinching instrument is available in both); relative to the full
  algebra both are passively incomplete. Passive (in)completeness tracks the observable algebra
  the states live in, and is the same on both sides of the OI-core line.

**Definitions.** `PassivelyIncomplete T` quantifies over the families `T.avail` makes available
on the system. `PassivelyCompleteOnDiagonal T` asks for an available family, completely positive,
whose nonselective channel fixes every diagonal matrix and which separates diagonal matrices by
outcome law. `labelTheory` is `diagTheory` with the diagonal-preservation predicate on composite
operations replaced by ancilla-label preservation (`KeepsLabels`), and with reference-tested
preparations alone.

**Not claimed.** That quantum mechanics requires OI, or that passive incompleteness is evidence
for a hidden ontology: the theorem here is the opposite, that passive incompleteness holds in a
theory that realizes no OI core at all. That `labelTheory` satisfies any of the five physical
completion conditions; it is used only as a witness against `OICore`. That the cell
`OICore ∧ ¬ PassivelyCompleteOnDiagonal` is inhabited or empty: no theory is constructed for it,
and the sector diagram does not need it. Nothing here bears on the OI ↔ QM equivalence, on the
concrete-cut freeze, or on CT3.
-/

namespace OIBridge
namespace PassiveIndependence

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence OIHierarchy PassiveObservation

open scoped ComplexOrder

/-! ### Section A — passive incompleteness at the level of theories -/

section TheoryLevel

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **Passive incompleteness of a theory**: no family of operations the theory makes available
on the system is both passive (completely positive branches summing to the identity) and
state-separating. -/
def PassivelyIncomplete (T : FiniteOperationalTheory A) : Prop :=
  ∀ (O : Type) [Fintype O] [DecidableEq O] (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail O F → IsPassiveInstrument F → ¬ SeparatesStates F

/-- **Passive incompleteness is carrier-intrinsic.** On any carrier with two or more states,
every theory is passively incomplete, by OI-N1 — availability plays no role. -/
theorem passivelyIncomplete_of_card (T : FiniteOperationalTheory A) (hA : 1 < Fintype.card A) :
    PassivelyIncomplete T :=
  fun _ _ _ _ _ hF => no_complete_passive_observation hF hA

end TheoryLevel

/-- Every theory on the qubit is passively incomplete. -/
theorem passivelyIncomplete_qubit (T : FiniteOperationalTheory (Fin 2)) : PassivelyIncomplete T :=
  passivelyIncomplete_of_card T (by simp)

/-! ### Section B — a theory whose composite operations keep the ancilla label -/

section Labels

variable {A B : Type*}

/-- Supported on the ancilla block `(k, l)`: every entry whose row ancilla is not `k` or whose
column ancilla is not `l` vanishes. -/
def SuppAnc (k l : B) (X : Matrix (A × B) (A × B) ℂ) : Prop :=
  ∀ p q, ¬ (p.2 = k ∧ q.2 = l) → X p q = 0

/-- **Keeps the ancilla label**: every ancilla block is mapped into itself. No such map moves
information from one ancilla value to another. -/
def KeepsLabels (Φ : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ) : Prop :=
  ∀ (k l : B) (X : Matrix (A × B) (A × B) ℂ), SuppAnc k l X → SuppAnc k l (Φ X)

theorem keepsLabels_id : KeepsLabels (LinearMap.id : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] _) :=
  fun _ _ _ h => h

theorem keepsLabels_zero : KeepsLabels (0 : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] _) :=
  fun _ _ _ _ _ _ _ => rfl

theorem keepsLabels_add {Φ Ψ : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ}
    (hΦ : KeepsLabels Φ) (hΨ : KeepsLabels Ψ) : KeepsLabels (Φ + Ψ) := by
  intro k l X hX p q hpq
  rw [LinearMap.add_apply, Matrix.add_apply, hΦ k l X hX p q hpq, hΨ k l X hX p q hpq, add_zero]

theorem keepsLabels_sum {ι : Type*} (s : Finset ι)
    (Φ : ι → Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ)
    (h : ∀ i ∈ s, KeepsLabels (Φ i)) : KeepsLabels (∑ i ∈ s, Φ i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using keepsLabels_zero
  | insert a s ha ih =>
    rw [Finset.sum_insert ha]
    exact keepsLabels_add (h a (Finset.mem_insert_self a s))
      (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

theorem keepsLabels_comp {Φ Ψ : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ}
    (hΦ : KeepsLabels Φ) (hΨ : KeepsLabels Ψ) : KeepsLabels (Φ.comp Ψ) :=
  fun k l X hX => hΦ k l _ (hΨ k l X hX)

/-- The local Lüders readout keeps the ancilla label: it projects onto one ancilla value. -/
theorem keepsLabels_localLuders [DecidableEq B] (k' : B) :
    KeepsLabels (localLuders (A := A) k') := by
  intro k l X hX p q hpq
  rw [localLuders_apply]
  by_cases h : p.2 = k' ∧ q.2 = k'
  · rw [if_pos h]
    apply hX
    rintro ⟨h1, h2⟩
    exact hpq ⟨h.1.symm ▸ h1 ▸ rfl, h.2.symm ▸ h2 ▸ rfl⟩
  · rw [if_neg h]

end Labels

/-- **The label theory.** Kraus families on the system; on every composite carrier, completely
positive trace-normalized instruments whose every branch keeps the ancilla label; reference-tested
preparations. The same closure proofs as `diagTheory`, with label preservation in place of
diagonal preservation. -/
noncomputable def labelTheory : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F
  availExt := fun _ _ _ _ F => IsCPInstrument F ∧ ∀ a, KeepsLabels (F a)
  avail_id := scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f hF
    exact isKrausFamily_coarse hF f
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨⟨h2, htr⟩, hd⟩
    refine ⟨⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩,
      fun a' => keepsLabels_sum _ _ fun j _ => hd j⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨⟨hF2, hFtr⟩, hFd⟩ hG
    refine ⟨⟨fun c => cp_comp ((hG c.1).1.1 c.2) (hF2 c.1), fun X => ?_⟩,
      fun c => keepsLabels_comp ((hG c.1).2 c.2) (hFd c.1)⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).1.2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P
  prepAvail_uniform := fun n =>
    ⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩
  prepAvail_post := by
    rintro n P Φ ⟨hPtr, hPpsd⟩ ⟨⟨hΦ2, hΦtr⟩, -⟩
    refine ⟨fun ρ => ?_, ?_⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact cp_referencePositive (Fin 2) _ (hΦ2 ()) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n =>
    ⟨⟨fun k => localLuders_cp k, localLuders_trace_sum⟩, fun k => keepsLabels_localLuders k⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hPtr, hPpsd⟩ ⟨⟨hF2, hFtr⟩, -⟩
    refine isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_)
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef (cp_referencePositive (Fin 2) _ (hF2 a) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

/-! ### Section C — the label theory does not realize the OI core -/

section NotCore

/-- The unit at the composite index `(0, 0)`: system `|0⟩`, ancilla value `0`. -/
def unit00 : Matrix (Fin 2 × Fin 4) (Fin 2 × Fin 4) ℂ := Matrix.single (0, 0) (0, 0) 1

theorem unit00_suppAnc : SuppAnc (A := Fin 2) (0 : Fin 4) 0 unit00 := by
  intro p q hpq
  simp only [unit00, Matrix.single, Matrix.of_apply]
  rw [if_neg]
  rintro ⟨h1, h2⟩
  exact hpq ⟨by rw [← h1], by rw [← h2]⟩

/-- The OI control `τ` flips the ancilla's second bit: it carries the composite index `(0, 1)`
to `(0, 0)` under the core embedding. -/
theorem coreIdx_tau_symm :
    coreIdx (tauPerm.symm (coreIdx.symm ((0 : Fin 2), (1 : Fin 4)))) = (0, 0) := by
  decide

/-- **`τ` moves the ancilla label.** The transported control sends the unit at `(0, 0)` to a
matrix with entry `1` at `((0, 1), (0, 1))`, outside the ancilla block `(0, 0)`. -/
theorem tau_moves_label :
    ¬ KeepsLabels (transport coreIdx (correlationExtension tauPerm (onesCorr Core))) := by
  intro h
  have hY := h 0 0 unit00 unit00_suppAnc ((0 : Fin 2), (1 : Fin 4)) ((0 : Fin 2), (1 : Fin 4))
    (by simp)
  rw [transport_apply, Matrix.reindex_apply, Matrix.submatrix_apply, correlationExtension_ones,
    Matrix.of_apply, Matrix.reindex_apply, Matrix.submatrix_apply, Equiv.symm_symm,
    coreIdx_tau_symm] at hY
  simp [unit00, Matrix.single] at hY

/-- **The label theory does not realize the OI core.** `RealizesSealedOICore` is a conjunction
whose third conjunct is the availability, at level four with the trivial outcome set, of the
transported control `τ`; there is no existential over alternative routes, so the unavailability
of that one channel refutes it. -/
theorem label_not_oiCore : ¬ OICore labelTheory :=
  fun h => tau_moves_label (h.2.2.1.2 ())

end NotCore

/-! ### Section D — the diagram: one vacuous implication, one failing converse -/

section Diagram

/-- **The forward implication is vacuous.** `OICore T → PassivelyIncomplete T` holds for every
theory, and the proof does not consult the hypothesis: the conclusion is N1 on the carrier. -/
theorem oiCore_to_passive_vacuous (T : FiniteOperationalTheory (Fin 2)) :
    OICore T → PassivelyIncomplete T :=
  fun _ => passivelyIncomplete_qubit T

/-- **Passive incompleteness without any OI core.** The label theory is passively incomplete and
realizes no OI core. Passive incompleteness is therefore not evidence for a hidden-memory
realization. -/
theorem passivelyIncomplete_without_oiCore :
    ∃ T : FiniteOperationalTheory (Fin 2), PassivelyIncomplete T ∧ ¬ OICore T :=
  ⟨labelTheory, passivelyIncomplete_qubit _, label_not_oiCore⟩

/-- **The converse implication fails.** -/
theorem passive_not_implies_oiCore :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2), PassivelyIncomplete T → OICore T := by
  intro h
  exact label_not_oiCore (h _ (passivelyIncomplete_qubit _))

/-- **OI-N4, the diagram.** Passive incompleteness holds in every theory on the qubit; the OI
core holds in some (`diagTheory`) and fails in others (`labelTheory`). Passive incompleteness is
theory-insensitive, so it carries no discriminatory information about whether the OI core is
realized: the forward implication is vacuous and the converse fails. -/
theorem passive_nondiscriminating :
    (∀ T : FiniteOperationalTheory (Fin 2), PassivelyIncomplete T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ PassivelyIncomplete T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), ¬ OICore T ∧ PassivelyIncomplete T) :=
  ⟨passivelyIncomplete_qubit,
    ⟨diagTheory, diag_realizesSealedOICore, passivelyIncomplete_qubit _⟩,
    ⟨labelTheory, label_not_oiCore, passivelyIncomplete_qubit _⟩⟩

end Diagram

/-! ### Section E — the sector, not the OI status, is what varies -/

section Sector

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **Passive completeness on the commutative sector**: some available family is completely
positive, fixes every diagonal matrix nonselectively, and separates diagonal matrices by outcome
law. -/
def PassivelyCompleteOnDiagonal (T : FiniteOperationalTheory A) : Prop :=
  ∃ (O : Type) (_ : Fintype O) (_ : DecidableEq O) (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ),
    T.avail O F ∧ (∀ a, IsCompletelyPositive (F a)) ∧ (∀ X, IsDiagonal X → ∑ a, (F a) X = X)
    ∧ ∀ ρ σ : Matrix A A ℂ, IsDiagonal ρ → IsDiagonal σ →
        (∀ a, ((F a) ρ).trace = ((F a) σ).trace) → ρ = σ

/-- The pinching instrument sums to the trace: it is a normalized instrument. -/
theorem pinching_trace_sum (X : Matrix A A ℂ) : ∑ a, (pinching a X).trace = X.trace := by
  simp only [pinching_trace]
  rfl

/-- The pinching instrument is a Kraus family, through the kernel's factorization. -/
theorem pinching_isKrausFamily [Nonempty A] : IsKrausFamily (pinching (S := A)) :=
  isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _ pinching_cp
    pinching_trace_sum

/-- The pinching branches preserve diagonal states. -/
theorem pinching_preservesDiag (a : A) : PreservesDiag (pinching a) := by
  intro w
  refine ⟨fun i => if i = a then w a else 0, ?_⟩
  ext i j
  rw [pinching_apply, diagonal_apply]
  by_cases hi : i = a
  · by_cases hj : j = a
    · simp [hi, hj]
    · simp [hi, hj, diagonal_apply]
      exact fun h => absurd h.symm hj
  · by_cases hj : j = a
    · simp [hi, hj]
    · simp [hi, hj, diagonal_apply]

end Sector

/-- **The diagonal theory is passively complete on its commutative sector.** -/
theorem diag_passivelyCompleteOnDiagonal : PassivelyCompleteOnDiagonal diagTheory :=
  ⟨Fin 2, inferInstance, inferInstance, pinching,
    ⟨pinching_isKrausFamily, pinching_preservesDiag⟩, pinching_cp,
    pinching_passive_on_diagonal, pinching_separates_diagonal⟩

/-- **The label theory is passively complete on its commutative sector.** -/
theorem label_passivelyCompleteOnDiagonal : PassivelyCompleteOnDiagonal labelTheory :=
  ⟨Fin 2, inferInstance, inferInstance, pinching, pinching_isKrausFamily, pinching_cp,
    pinching_passive_on_diagonal, pinching_separates_diagonal⟩

/-- **OI-N4, the sector diagram.** On both sides of the OI-core line the same pattern holds:
passively complete on the commutative sector, passively incomplete on the full algebra. What
passive (in)completeness tracks is the sector, and the OI status does not move it. -/
theorem sector_diagram :
    (∃ T : FiniteOperationalTheory (Fin 2),
        OICore T ∧ PassivelyCompleteOnDiagonal T ∧ PassivelyIncomplete T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
        ¬ OICore T ∧ PassivelyCompleteOnDiagonal T ∧ PassivelyIncomplete T) :=
  ⟨⟨diagTheory, diag_realizesSealedOICore, diag_passivelyCompleteOnDiagonal,
      passivelyIncomplete_qubit _⟩,
    ⟨labelTheory, label_not_oiCore, label_passivelyCompleteOnDiagonal,
      passivelyIncomplete_qubit _⟩⟩

#print axioms passivelyIncomplete_of_card
#print axioms passivelyIncomplete_qubit
#print axioms keepsLabels_localLuders
#print axioms tau_moves_label
#print axioms label_not_oiCore
#print axioms oiCore_to_passive_vacuous
#print axioms passivelyIncomplete_without_oiCore
#print axioms passive_not_implies_oiCore
#print axioms passive_nondiscriminating
#print axioms pinching_isKrausFamily
#print axioms pinching_preservesDiag
#print axioms diag_passivelyCompleteOnDiagonal
#print axioms label_passivelyCompleteOnDiagonal
#print axioms sector_diagram

end PassiveIndependence
end OIBridge
