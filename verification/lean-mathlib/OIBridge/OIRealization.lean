/-
  OIBridge/OIRealization.lean — the sealed C1–C4 Observation-Incompleteness core, realized
  inside the operational theories with its actual visible readout; the axiom-match audit;
  and the capstone: one and the same finite OI process admits completions on either side
  of the compositional independence matrix.

  ROUND FORTY. Rounds thirty-seven to thirty-nine isolated two compositional existence
  principles — inert-spectator compositionality and iterated ancilla closure — and proved
  them independent of the formalized operational rules, of exact system QM, of control, and
  of realized `H_comp`. The round-39 caveat was that the countermodels had not been
  exhibited as models of the bare OI axioms. This file closes that gap for the finite core
  the project has carried since round twenty-three.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  THE EMBEDDING. `coreIdx : Core ≃ Fin 2 × Fin 4`, `((v,h),b) ↦ (h, pack (v,b))`:  │
      │    the system qubit carries the HIDDEN bit, the four-level ancilla carries     │
      │    exactly the observer-visible pair. This is the physical partition, not a    │
      │    convenience.                                                                │
      │  THE ACTUAL READOUT. `readVisible r` keeps both hidden states with visible pair │
      │    `r` — the embedded observer's readout, NOT round twenty-three's full-basis   │
      │    probe `Step.read k`. `readVisible_eq_localLuders`: under `coreIdx` it IS the  │
      │    theory's native level-4 Lüders readout, `T.readout 4 (visIdx r)`.          │
      │  THE REALIZATION PREDICATE `RealizesSealedOICore T`: C1–C4; the passive step σ │
      │    and the control τ realized as the transported permutation channels; the     │
      │    visible readout equal to the native readout and available as a family; the  │
      │    realized visible comb equal to the classical OI comb on every classical     │
      │    preparation and every finite word (`realizedFold_diagonal`).                │
      │  `realizesSealedOICore_of_control`: every theory with composite unitary control │
      │    realizes the core — so `countermodel`, `admissibleTheory`, `fullQuantum` do. │
      │  THE AUDIT `sealedCore_is_finiteOI`: the core satisfies every ingredient of the │
      │    manuscript's finite-observation definition and Lemmas 1–3 (finite total     │
      │    system, proper hidden sector, explicit product partition, deterministic     │
      │    reversible dynamics, invariant counting measure, recurrence — Axiom 2 —,     │
      │    registered visible content — Axiom 1 —, nontrivial coupling) and C1–C4.     │
      │  THE CAPSTONE `sameCore_both_sides`: the SAME finite, reversible, C1–C4 OI       │
      │    process is realized in a theory with closure but no inert spectators, in one │
      │    with inert spectators but no closure, and in one with both — each exactly    │
      │    quantum on the system with full composite unitary control.                  │
      └──────────────────────────────────────────────────────────────────────────────┘

  THE CLAIM BOUNDARY, decided by the audit. The round-39 caveat read: the countermodels
  are models of the formalized operational rules, not exhibited models of the bare OI
  axioms. The audit exhibits them. Every ingredient the manuscript's definition of an
  observation and its three structural lemmas invoke — a total system, a proper finite
  visible subsystem, a hidden complement, coupling through the dynamics, determinism and
  injectivity hence bijectivity, the product partition, the invariant counting measure —
  together with Axiom 1 (registered differentiation), Axiom 2 (recurrence) and the four
  diagnostics C1–C4, is a kernel-checked property of the sealed core, and the SAME core is
  realized with its actual visible readout in both independence countermodels. So the
  caveat is retired and replaced by the following statement, which is exactly what is
  proved: BARE FINITE OI, as formalized by the sealed core, does not imply either
  compositional existence principle; the two principles are genuinely additional to it.
  What remains outside the kernel is interpretive only: whether some reading of the
  manuscript's prose carries a cross-partition composition principle not present in the
  definition, the lemmas, the axioms or C1–C4 as stated. The audit found none: the only
  cross-partition content is the coupling clause, which is C1, and C1 is satisfied. If a
  reader locates one, it would be one of the two missing clauses under another name — the
  same conclusion by another route.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositionalIndependence

namespace OIBridge
namespace OIRealization

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalCountermodel ReferenceExtension ReferenceSufficiency BoundaryAudit
open SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence

/-! ### Section A — the embedding of the eight-state core -/

section Index

/-- A bit as a level of the system qubit. -/
def bitIdx : Bool ≃ Fin 2 where
  toFun b := if b then 1 else 0
  invFun i := ![false, true] i
  left_inv := by decide
  right_inv := by decide

/-- The observer-visible pair `(v, b)` as a level of the four-level ancilla. -/
def visIdx : Bool × Bool ≃ Fin 4 where
  toFun r := ![(0 : Fin 4), 1, 2, 3] (finProdFinEquiv (bitIdx r.1, bitIdx r.2))
  invFun i := ![(false, false), (false, true), (true, false), (true, true)] i
  left_inv := by decide
  right_inv := by decide

/-- **THE EMBEDDING** `((v,h),b) ↦ (h, pack (v,b))`: the hidden bit on the system qubit, the
visible pair on the ancilla. -/
def coreIdx : Core ≃ Fin 2 × Fin 4 where
  toFun p := (bitIdx p.1.2, visIdx (p.1.1, p.2))
  invFun q := (((visIdx.symm q.2).1, bitIdx.symm q.1), (visIdx.symm q.2).2)
  left_inv := by decide
  right_inv := by decide

theorem coreIdx_apply (v h b : Bool) : coreIdx ((v, h), b) = (bitIdx h, visIdx (v, b)) := rfl

/-- The visible pair of a core state is the ancilla level of its image. -/
theorem vis_coreIdx_symm_iff (x : Fin 2 × Fin 4) (r : Bool × Bool) :
    vis (coreIdx.symm x) = r ↔ x.2 = visIdx r := by
  revert x r
  decide

end Index

/-! ### Section B — the actual visible readout -/

section Readout

/-- **THE EMBEDDED OBSERVER'S READOUT**: keep the states whose visible pair is `r` — both
hidden values survive. This is the OI readout of the `(v,b)` register, not a full-basis
probe. -/
def readVisible (r : Bool × Bool) : Matrix Core Core ℂ →ₗ[ℂ] Matrix Core Core ℂ where
  toFun X := Matrix.of fun p q => if vis p = r ∧ vis q = r then X p q else 0
  map_add' X Y := by
    ext p q
    by_cases h : vis p = r ∧ vis q = r <;> simp [h]
  map_smul' c X := by
    ext p q
    by_cases h : vis p = r ∧ vis q = r <;> simp [h]

theorem readVisible_apply (r : Bool × Bool) (X : Matrix Core Core ℂ) (p q : Core) :
    readVisible r X p q = if vis p = r ∧ vis q = r then X p q else 0 := rfl

/-- **THE VISIBLE READOUT IS THE NATIVE READOUT.** Under `coreIdx`, `readVisible r` is
exactly the theory's level-4 Lüders selector at the ancilla level `visIdx r`. -/
theorem readVisible_eq_localLuders (r : Bool × Bool) :
    transport coreIdx (readVisible r) = localLuders (A := Fin 2) (visIdx r) := by
  refine LinearMap.ext fun N => ?_
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [transport_apply, Matrix.reindex_apply, Matrix.submatrix_apply, localLuders_apply,
    readVisible_apply, Matrix.reindex_apply, Matrix.submatrix_apply, Equiv.symm_symm,
    Equiv.apply_symm_apply, Equiv.apply_symm_apply]
  simp only [vis_coreIdx_symm_iff]
  by_cases hi : i = visIdx r <;> by_cases hj : j = visIdx r <;> simp [hi, hj]

/-- The visible readout family, transported, is the native readout family relabelled. -/
theorem readVisible_family_eq (T : FiniteOperationalTheory (Fin 2)) :
    (fun r => transport coreIdx (readVisible r)) = fun r => T.readout 4 (visIdx r) := by
  funext r
  rw [readVisible_eq_localLuders, readout_is_localLuders]

/-- The relabelled native readout family is available (coarse-graining along `visIdx`). -/
theorem readout_relabel_available (T : FiniteOperationalTheory (Fin 2)) :
    T.availExt 4 (Bool × Bool) (fun r => T.readout 4 (visIdx r)) := by
  have h := T.availExt_coarse 4 (Fin 4) (Bool × Bool) _ visIdx.symm (T.readout_avail 4)
  have hfun : (fun r => ∑ k ∈ Finset.univ.filter (fun k : Fin 4 => visIdx.symm k = r),
      T.readout 4 k) = fun r => T.readout 4 (visIdx r) := by
    funext r
    have hfil : Finset.univ.filter (fun k : Fin 4 => visIdx.symm k = r) = {visIdx r} := by
      ext k
      simp [Equiv.symm_apply_eq]
    rw [hfil, Finset.sum_singleton]
  rw [hfun] at h
  exact h

end Readout

/-! ### Section C — the visible comb -/

section Comb

/-- One OI-operational step with the ACTUAL visible readout. -/
inductive VStep
  | act (g : Gen)
  | readV (r : Bool × Bool)

/-- The coherent map of a visible step, with the trivial (all-ones) correlation on the
interventions — the passive step and the control act as relabellings. -/
def vstepMap : VStep → (Matrix Core Core ℂ →ₗ[ℂ] Matrix Core Core ℂ)
  | .act g => correlationExtension (genPerm g) (onesCorr Core)
  | .readV r => readVisible r

/-- The realized comb: every step transported into the theory's carrier. -/
def realizedFold (steps : List VStep) (N : Matrix (Fin 2 × Fin 4) (Fin 2 × Fin 4) ℂ) :
    Matrix (Fin 2 × Fin 4) (Fin 2 × Fin 4) ℂ :=
  steps.foldl (fun Y s => transport coreIdx (vstepMap s) Y) N

/-- The classical action of a visible step on a weight vector. -/
def visWeightStep : VStep → (Core → ℂ) → (Core → ℂ)
  | .act g, w => fun a => w ((genPerm g).symm a)
  | .readV r, w => fun a => if vis a = r then w a else 0

/-- The classical comb of the bare OI core with the actual visible readout. -/
def visWeightFold (steps : List VStep) (w : Core → ℂ) : Core → ℂ :=
  steps.foldl (fun v s => visWeightStep s v) w

theorem readVisible_diagonal (r : Bool × Bool) (w : Core → ℂ) :
    readVisible r (Matrix.diagonal w)
      = Matrix.diagonal (fun a => if vis a = r then w a else 0) := by
  ext p q
  rw [readVisible_apply]
  by_cases hpq : p = q
  · subst hpq
    rw [Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq]
    by_cases h : vis p = r
    · rw [if_pos ⟨h, h⟩, if_pos h]
    · rw [if_neg (fun hh => h hh.1), if_neg h]
  · rw [Matrix.diagonal_apply_ne _ hpq, Matrix.diagonal_apply_ne _ hpq, ite_self]

theorem vstepMap_diagonal (s : VStep) (w : Core → ℂ) :
    vstepMap s (Matrix.diagonal w) = Matrix.diagonal (visWeightStep s w) := by
  cases s with
  | act g =>
    exact correlationExtension_diagonal (genPerm g) (onesCorr Core) (fun _ => rfl) w
  | readV r => exact readVisible_diagonal r w

/-- **THE REALIZED COMB IS THE CLASSICAL OI COMB.** A classical preparation, embedded, pushed
through any finite word of passive steps, controls and visible readouts realized in the
theory's carrier, is the embedded classical comb. -/
theorem realizedFold_diagonal (steps : List VStep) (w : Core → ℂ) :
    realizedFold steps (Matrix.reindex coreIdx coreIdx (Matrix.diagonal w))
      = Matrix.reindex coreIdx coreIdx (Matrix.diagonal (visWeightFold steps w)) := by
  induction steps generalizing w with
  | nil => rfl
  | cons s rest ih =>
    show List.foldl (fun Y s => transport coreIdx (vstepMap s) Y)
      (transport coreIdx (vstepMap s) (Matrix.reindex coreIdx coreIdx (Matrix.diagonal w))) rest
      = _
    rw [transport_reindex, vstepMap_diagonal]
    exact ih _

end Comb

/-! ### Section D — the realization predicate and the generic theorem -/

/-- **THE SEALED OI CORE, REALIZED IN A THEORY**: the core satisfies C1–C4; the passive
step and the control are available as the transported permutation channels at level four;
the actual visible readout is the native ancilla readout and is available as a family; and
the realized visible comb agrees with the classical OI comb on every classical preparation
and every finite word. -/
def RealizesSealedOICore (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  CoreC1C4
    ∧ T.availExt 4 Unit (fun _ => transport coreIdx (correlationExtension sigmaPerm (onesCorr Core)))
    ∧ T.availExt 4 Unit (fun _ => transport coreIdx (correlationExtension tauPerm (onesCorr Core)))
    ∧ (∀ r : Bool × Bool, transport coreIdx (readVisible r) = T.readout 4 (visIdx r))
    ∧ T.availExt 4 (Bool × Bool) (fun r => transport coreIdx (readVisible r))
    ∧ ∀ (steps : List VStep) (w : Core → ℂ),
        realizedFold steps (Matrix.reindex coreIdx coreIdx (Matrix.diagonal w))
          = Matrix.reindex coreIdx coreIdx (Matrix.diagonal (visWeightFold steps w))

/-- A relabelling of the core is available in any theory with composite unitary control. -/
theorem relabel_available (T : FiniteOperationalTheory (Fin 2))
    (hctrl : HasCompositeUnitaryControl T) (g : Equiv.Perm Core) :
    T.availExt 4 Unit (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
  exact hctrl 4 _ (reindex_isometry _ _ (permMatrix_isometry g))

/-- **CONTROL REALIZES THE SEALED CORE.** -/
theorem realizesSealedOICore_of_control (T : FiniteOperationalTheory (Fin 2))
    (hctrl : HasCompositeUnitaryControl T) : RealizesSealedOICore T := by
  refine ⟨core_isC1C4, relabel_available T hctrl sigmaPerm, relabel_available T hctrl tauPerm,
    fun r => ?_, ?_, realizedFold_diagonal⟩
  · rw [readVisible_eq_localLuders, readout_is_localLuders]
  · rw [readVisible_family_eq T]
    exact readout_relabel_available T

theorem countermodel_realizesSealedOICore : RealizesSealedOICore countermodel :=
  realizesSealedOICore_of_control _ countermodel_control

theorem admissible_realizesSealedOICore : RealizesSealedOICore admissibleTheory :=
  realizesSealedOICore_of_control _ admissible_control

theorem fullQuantum_realizesSealedOICore : RealizesSealedOICore fullQuantum :=
  realizesSealedOICore_of_control _ fullQuantum_control

/-! ### Section E — the axiom-match audit -/

section Audit

/-- The visible/hidden partition of the core as an explicit product, visible first. -/
def partIdx : Core ≃ (Bool × Bool) × Bool where
  toFun p := (vis p, p.1.2)
  invFun x := ((x.1.1, x.2), x.1.2)
  left_inv := by decide
  right_inv := by decide

theorem partIdx_fst (p : Core) : (partIdx p).1 = vis p := rfl

/-- **THE FINITE-OI INGREDIENTS OF THE SEALED CORE**, each as the manuscript states it: a
finite total system (Lemma 1); a proper finite visible subsystem with a hidden complement
of more than one state (Lemma 2); the explicit product partition visible × hidden
(Lemma 2); the dynamics deterministic and injective, hence a bijection with a predecessor
map (Lemma 3); the counting measure invariant under the passive step and the control
(Lemma 3); recurrence — every state returns (Axiom 2, here with period two); registered
differentiation — the visible readout distinguishes states (Axiom 1); coupling through the
dynamics across the partition (the definition's third feature, which is C1); and the four
diagnostics C1–C4. -/
def SealedCoreIsFiniteOI : Prop :=
  Fintype.card Core = 8
    ∧ Fintype.card (Bool × Bool) = 4
    ∧ 1 < Fintype.card Bool
    ∧ (∀ p : Core, (partIdx p).1 = vis p)
    ∧ (∀ p q : Core, swapFn p = swapFn q → p = q)
    ∧ (∀ p : Core, sigmaPerm.symm (sigmaPerm p) = p)
    ∧ (∀ (g : Gen) (c : ℂ), visWeightStep (.act g) (fun _ => c) = fun _ => c)
    ∧ (∀ p : Core, swapFn (swapFn p) = p)
    ∧ (∃ p q : Core, vis p ≠ vis q)
    ∧ (∃ p q : Core, vis p = vis q ∧ p ≠ q ∧ vis (swapFn p) ≠ vis (swapFn q))
    ∧ CoreC1C4

/-- **THE AUDIT PASSES**: the sealed core is a finite OI process in the manuscript's sense. -/
theorem sealedCore_is_finiteOI : SealedCoreIsFiniteOI :=
  ⟨rfl, rfl, by decide, fun _ => rfl, fun p q h => swapFn_involutive.injective h,
    fun p => sigmaPerm.symm_apply_apply p, fun _ _ => rfl, fun p => swapFn_involutive p,
    ⟨((false, false), false), ((true, false), false), by decide⟩,
    core_hidden_drives_visible, core_isC1C4⟩

end Audit

/-! ### Section F — the capstone: one OI process, both sides of the matrix -/

/-- **THE SAME CORE, CLOSURE WITHOUT INERT SPECTATORS** (the round-34 countermodel). -/
theorem sameCore_closure_not_inert :
    RealizesSealedOICore countermodel ∧ ExactFiniteEndomorphicQuantumOps countermodel
      ∧ HasCompositeUnitaryControl countermodel ∧ IteratedAncillaClosure countermodel
      ∧ ¬ InertSpectatorCompositionality countermodel :=
  ⟨countermodel_realizesSealedOICore, countermodel_exact, countermodel_control,
    countermodel_iteratedAncillaClosure, countermodel_not_inert⟩

/-- **THE SAME CORE, INERT SPECTATORS WITHOUT CLOSURE** (the round-38 admissible theory). -/
theorem sameCore_inert_not_closure :
    RealizesSealedOICore admissibleTheory ∧ ExactFiniteEndomorphicQuantumOps admissibleTheory
      ∧ HasCompositeUnitaryControl admissibleTheory
      ∧ InertSpectatorCompositionality admissibleTheory
      ∧ ¬ IteratedAncillaClosure admissibleTheory :=
  ⟨admissible_realizesSealedOICore, admissible_exact, admissible_control,
    admissible_inert, admissible_not_iteratedAncillaClosure⟩

/-- **THE SAME CORE, BOTH** (the full quantum theory). -/
theorem sameCore_both :
    RealizesSealedOICore fullQuantum ∧ ExactFiniteEndomorphicQuantumOps fullQuantum
      ∧ HasCompositeUnitaryControl fullQuantum ∧ InertSpectatorCompositionality fullQuantum
      ∧ IteratedAncillaClosure fullQuantum :=
  ⟨fullQuantum_realizesSealedOICore, fullQuantum_exact,
    fullQuantum_control, fullQuantum_inert, fullQuantum_iteratedAncillaClosure⟩

/-- **THE CAPSTONE.** One and the same finite, reversible, C1–C4 Observation-Incompleteness
process — audited as a finite OI process in the manuscript's sense — admits operational
completions on either side of the compositional independence matrix, and one with both. -/
theorem sameCore_both_sides :
    SealedCoreIsFiniteOI
      ∧ (∃ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T ∧ ExactFiniteEndomorphicQuantumOps T
          ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T
          ∧ ¬ InertSpectatorCompositionality T)
      ∧ (∃ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T ∧ ExactFiniteEndomorphicQuantumOps T
          ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
          ∧ ¬ IteratedAncillaClosure T)
      ∧ (∃ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T ∧ ExactFiniteEndomorphicQuantumOps T
          ∧ HasCompositeUnitaryControl T ∧ InertSpectatorCompositionality T
          ∧ IteratedAncillaClosure T) :=
  ⟨sealedCore_is_finiteOI, ⟨countermodel, sameCore_closure_not_inert⟩,
    ⟨admissibleTheory, sameCore_inert_not_closure⟩, ⟨fullQuantum, sameCore_both⟩⟩

/-- **BARE FINITE OI DOES NOT IMPLY EITHER COMPOSITIONAL PRINCIPLE**: realizing the audited
core, with EXACT system quantum mechanics and full composite unitary control, forces neither
inert-spectator compositionality nor iterated ancilla closure. -/
theorem finiteOI_not_implies_inert :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T → ExactFiniteEndomorphicQuantumOps T
      → HasCompositeUnitaryControl T → InertSpectatorCompositionality T :=
  fun h => countermodel_not_inert
    (h countermodel countermodel_realizesSealedOICore countermodel_exact countermodel_control)

theorem finiteOI_not_implies_closure :
    ¬ ∀ T : FiniteOperationalTheory (Fin 2), RealizesSealedOICore T → ExactFiniteEndomorphicQuantumOps T
      → HasCompositeUnitaryControl T → IteratedAncillaClosure T :=
  fun h => admissible_not_iteratedAncillaClosure
    (h admissibleTheory admissible_realizesSealedOICore admissible_exact admissible_control)

#print axioms coreIdx_apply
#print axioms vis_coreIdx_symm_iff
#print axioms readVisible_apply
#print axioms readVisible_eq_localLuders
#print axioms readVisible_family_eq
#print axioms readout_relabel_available
#print axioms readVisible_diagonal
#print axioms vstepMap_diagonal
#print axioms realizedFold_diagonal
#print axioms relabel_available
#print axioms realizesSealedOICore_of_control
#print axioms countermodel_realizesSealedOICore
#print axioms admissible_realizesSealedOICore
#print axioms fullQuantum_realizesSealedOICore
#print axioms partIdx_fst
#print axioms sealedCore_is_finiteOI
#print axioms sameCore_closure_not_inert
#print axioms sameCore_inert_not_closure
#print axioms sameCore_both
#print axioms sameCore_both_sides
#print axioms finiteOI_not_implies_inert
#print axioms finiteOI_not_implies_closure

end OIRealization
end OIBridge
