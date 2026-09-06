import OIBridge.ScalarClosure
import Mathlib.Data.Matrix.ColumnRowPartitioned

/-!
# The instrument-realization audit — one-instrument provenance for realized operations

The preregistered pass of `INSTRUMENT-REALIZATION-AUDIT.md`. `Realized 𝓘 S Φ` takes the
branches of an operation from the class one at a time, with nothing connecting them, and so
admits the replication of a post-selected contraction `c • U` into the unitary conjugation by
`U`. This file defines the replacement, `InstAvail`: a family of operations on a carrier is
instrument-realized when it is built from admissible isometric steps, the native readout of a
register, coarse-graining, sequential composition with outcome-dependent continuation, and the
discard of a uniformly attached ancilla, by exactly those five constructors and no sum. Its
uniformly weighted preparation label is summed inside the discard and is never an outcome.

* T1, soundness: every instrument-realized family is branch-realized and trace preserving
  (`realized_of_instAvail`, `instAvail_trace`, `isGenInstrument_of_instAvail`).
* T3, the generated theory: `instTheory 𝓘 S` is a finite operational theory for every
  architecture, with embedded observation when the class is label-invariant
  (`instTheory_embeddedObservation`); the predicate is closed under relabelling
  (`instAvail_transport`) and under uncoupled spectators (`instAvail_spectator`).
* T4, survival: the implementation-locality stack re-established for the new primitive under
  the names `InstrumentGenerated`, `InstrumentLocality`, `ReversibleInstrumentLocality`,
  `OIPlusInst`, `OIPlusMinInst`, `DerivedOIInst`, `SourcedOIInst`, with validity, observational
  independence, the exact quantum theories, the countermodel, the substratum and the sourced
  theories; inverse accessibility with the added hypothesis `PhaseSaturated`.
* T2, the converse fails: the invariant `OnesNormal` of complete instruments, a Kraus
  decomposition of the whole family whose operators sum against the all-ones vector to the
  all-ones vector, is preserved by every constructor including the feed-forward
  (`instAvail_onesNormal`); in a class whose admissible unitaries fix the all-ones vector
  (`OnesFixing`), an instrument-realized unitary conjugation fixes it
  (`instAvail_unitary_fixes_ones`). The closed-form class `onesClass` of contractive
  compressions of all-ones-fixing unitaries is an architecture, context-stable,
  label-invariant, dagger-stable and ones-fixing (`isometry_fixes_ones`); a contractive multiple
  of the transition flow lies in it (`transition_scaled_mem_onesClass`), so the flow's
  conjugation is branch-realized with the trace preserved and is not instrument-realized on a
  carrier with a third point (`flow_realized_not_instrumentRealized`).

No theorem here asserts or refutes the flow endpoint.
-/

namespace OIBridge
namespace InstrumentRealization

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure ReadWriteControl MinimalRepertoire
open LevelOneSeam PhysicalCharacterization RouteB ManuscriptAxioms OIRealization
open ReferenceExtension ReferenceSufficiency CompositeSoundness DimensionalCountermodel
open StinespringAssembly IsometryExtension SubstratumSource SubstratumInterfaceAudit
open ScalarClosure CoherentExtension OIHierarchyGeneral GeneralCarrier BoundaryAudit
open OperationalValidity DimensionalObstruction OIHierarchy IndependenceCensus

open scoped ComplexOrder

/-! ### Section A — the primitive -/

section Primitive

/-- The readout projector onto the register value `k` of the carrier `T × Fin m`. -/
def readProj (T : Type) [DecidableEq T] (m : ℕ) (k : Fin m) :
    Matrix (T × Fin m) (T × Fin m) ℂ :=
  Matrix.diagonal fun r => if r.2 = k then 1 else 0

/-- **INSTRUMENT REALIZATION.** A family of operations on the carrier `T` with outcomes `O` is
instrument-realized by the class `𝓘` when it is built from: one admissible isometric step;
the native Lüders readout of a register `T' × Fin m ≃ T` of the carrier, its projectors
admissible; classical coarse-graining of the outcome; sequential composition with
outcome-dependent continuation; and the discard of a uniformly attached ancilla of positive
size. There is no constructor taking a sum of admissible operators: the branches of a realized
family arise together as the outcomes of one protocol, and the uniformly weighted preparation
label is summed inside the discard and is never an outcome. -/
inductive InstAvail (𝓘 : ImplementationClass) :
    ∀ (T : Type) [Fintype T] [DecidableEq T] (O : Type) [Fintype O] [DecidableEq O],
      (O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) → Prop
  | op {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (hK : 𝓘 T K)
      (hiso : Kᴴ * K = 1) : InstAvail 𝓘 T Unit (fun _ => conjChannel K)
  | readout {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] {m : ℕ}
      (e : T' × Fin m ≃ T) (hP : ∀ k, 𝓘 T (Matrix.reindex e e (readProj T' m k))) :
      InstAvail 𝓘 T (Fin m) (fun k => conjChannel (Matrix.reindex e e (readProj T' m k)))
  | coarse {T : Type} [Fintype T] [DecidableEq T] {O O' : Type} [Fintype O] [DecidableEq O]
      [Fintype O'] [DecidableEq O'] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (f : O → O')
      (h : InstAvail 𝓘 T O F) :
      InstAvail 𝓘 T O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  | bind {T : Type} [Fintype T] [DecidableEq T] {O O' : Type} [Fintype O] [DecidableEq O]
      [Fintype O'] [DecidableEq O'] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
      {G : O → O' → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (hF : InstAvail 𝓘 T O F)
      (hG : ∀ a, InstAvail 𝓘 T O' (G a)) :
      InstAvail 𝓘 T (O × O') (fun c => (G c.1 c.2).comp (F c.1))
  | discard {T : Type} [Fintype T] [DecidableEq T] {m : ℕ} (hm : 0 < m) {O : Type} [Fintype O]
      [DecidableEq O]
      {F : O → Matrix (T × Fin m) (T × Fin m) ℂ →ₗ[ℂ] Matrix (T × Fin m) (T × Fin m) ℂ}
      (h : InstAvail 𝓘 (T × Fin m) O F) :
      InstAvail 𝓘 T O (fun a => discardWith (A := T) m (uniformAttach m) (F a))

variable {𝓘 : ImplementationClass}

/-- A one-outcome conjugation preserves the trace exactly when its operator is an isometry: the
contractive-plus-normalized reading of a step is the isometric one. -/
theorem conjChannel_trace_iff {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) :
    (∀ X : Matrix T T ℂ, (conjChannel K X).trace = X.trace) ↔ Kᴴ * K = 1 := by
  constructor
  · intro h
    have := sum_conjTranspose_mul_eq_one_of_trace (fun _ : Unit => K) fun X => by
      rw [Fintype.sum_unique]; exact h X
    rwa [Fintype.sum_unique] at this
  · intro h X
    exact conjChannel_trace K h X

theorem instAvail_mono {𝓙 : ImplementationClass}
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → 𝓙 S K)
    {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) : InstAvail 𝓙 T O F := by
  induction h with
  | op K hK hiso => exact InstAvail.op K (hle _ _ hK) hiso
  | readout e hP => exact InstAvail.readout e fun k => hle _ _ (hP k)
  | coarse f _ ih => exact InstAvail.coarse f ih
  | bind _ _ ihF ihG => exact InstAvail.bind ihF ihG
  | discard hm _ ih => exact InstAvail.discard hm ih

/-- **T1, THE TRACE**: an instrument-realized family preserves the trace in aggregate. -/
theorem instAvail_trace {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O]
    [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) :
    ∀ X, ∑ a, ((F a) X).trace = X.trace := by
  induction h with
  | op K hK hiso =>
    intro X
    rw [Fintype.sum_unique]
    exact conjChannel_trace K hiso X
  | readout e hP =>
    intro X
    have h1 : ∀ k, conjChannel (Matrix.reindex e e (readProj _ _ k)) = transport e (localLuders k) :=
      fun k => by rw [localLuders_eq_conjChannel, transport_conjChannel]; rfl
    simp only [h1, trace_transport]
    rw [localLuders_trace_sum, trace_reindex]
  | coarse f _ ih =>
    intro X
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))]
    exact ih X
  | bind _ hG ihF ihG =>
    intro X
    rw [Fintype.sum_prod_type]
    simp only [LinearMap.comp_apply]
    rw [Finset.sum_congr rfl fun a _ => ihG a _]
    exact ihF X
  | discard hm _ ih =>
    intro X
    simp only [discardWith_trace]
    rw [ih, uniformAttach_trace _ hm.ne']

/-- **T1, SOUNDNESS**: for an architecture, every branch of an instrument-realized family is
branch-realized: the step and the readout are conjugations by admissible operators, the
continuation multiplies admissible operators, and the discard takes contractive blocks. -/
theorem realized_of_instAvail (arch : Architecture 𝓘) {T : Type} [Fintype T] [DecidableEq T]
    {O : Type} [Fintype O] [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (h : InstAvail 𝓘 T O F) : ∀ a, Realized 𝓘 T (F a) := by
  induction h with
  | op K hK hiso => exact fun _ => realized_conj hK
  | readout e hP => exact fun k => realized_conj (hP k)
  | coarse f _ ih => exact fun a => realized_sum _ _ fun j _ => ih j
  | bind _ _ ihF ihG => exact fun c => realized_comp (arch.mul _) (ihG c.1 c.2) (ihF c.1)
  | discard hm _ ih => exact fun a => realized_discard (arch.block _ _) (arch.smul _) (ih a)

/-- **T1**: an instrument-realized family is a generated instrument of the branch-wise notion. -/
theorem isGenInstrument_of_instAvail (arch : Architecture 𝓘) {T : Type} [Fintype T]
    [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) : IsGenInstrument 𝓘 T F :=
  ⟨realized_of_instAvail arch h, instAvail_trace h⟩

/-- Every branch of an instrument-realized family is completely positive, for every class. -/
theorem cp_of_instAvail {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O]
    [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) (a : O) :
    IsCompletelyPositive (F a) :=
  cp_of_realized (realized_of_instAvail fullClass_arch
    (instAvail_mono (fun _ _ _ _ _ => trivial) h) a)

/-- Post-composition of every branch by an available one-outcome operation: the continuation
with a constant choice, coarse-grained along the outcome. -/
theorem instAvail_comp_one {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O]
    [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    {Φ : Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (hF : InstAvail 𝓘 T O F)
    (hΦ : InstAvail 𝓘 T Unit (fun _ => Φ)) : InstAvail 𝓘 T O (fun a => (F a).comp Φ) := by
  have h := InstAvail.coarse (fun c : Unit × O => c.2) (InstAvail.bind hΦ (fun _ => hF))
  have e : (fun a => (F a).comp Φ)
      = fun a => ∑ j ∈ Finset.univ.filter (fun j : Unit × O => j.2 = a), (F j.2).comp Φ := by
    funext a
    rw [Finset.sum_filter, Fintype.sum_prod_type, Fintype.sum_unique]
    simp
  rw [e]
  exact h

theorem instAvail_one_comp {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O]
    [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    {Φ : Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (hΦ : InstAvail 𝓘 T Unit (fun _ => Φ))
    (hF : InstAvail 𝓘 T O F) : InstAvail 𝓘 T O (fun a => Φ.comp (F a)) := by
  have h := InstAvail.coarse (fun c : O × Unit => c.1) (InstAvail.bind hF (fun _ => hΦ))
  have e : (fun a => Φ.comp (F a))
      = fun a => ∑ j ∈ Finset.univ.filter (fun j : O × Unit => j.1 = a), Φ.comp (F j.1) := by
    funext a
    rw [Finset.sum_filter, Fintype.sum_prod_type]
    simp
  rw [e]
  exact h

/-- The identity is instrument-realized in every class containing the identity operator. -/
theorem instAvail_id {T : Type} [Fintype T] [DecidableEq T] (hone : 𝓘 T 1) :
    InstAvail 𝓘 T Unit (fun _ => LinearMap.id) := by
  have h := InstAvail.op (𝓘 := 𝓘) (1 : Matrix T T ℂ) hone (by simp)
  rwa [conjChannel_one] at h

end Primitive

/-! ### Section B — relabelling and spectators -/

section Transport

variable {𝓘 : ImplementationClass}

theorem transport_refl {T : Type} [Fintype T] [DecidableEq T]
    (Φ : Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) : transport (Equiv.refl T) Φ = Φ := by
  refine LinearMap.ext fun X => ?_
  simp [transport_apply]

theorem transport_trans {T T' T'' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    [Fintype T''] [DecidableEq T''] (e : T ≃ T') (e' : T' ≃ T'')
    (Φ : Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) :
    transport e' (transport e Φ) = transport (e.trans e') Φ := by
  refine LinearMap.ext fun X => ?_
  simp only [transport_apply, Matrix.reindex_apply, Matrix.submatrix_submatrix]
  rfl

theorem transport_comp {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') (Φ Ψ : Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) :
    transport e (Φ.comp Ψ) = (transport e Φ).comp (transport e Ψ) := by
  refine LinearMap.ext fun X => ?_
  simp only [transport_apply, LinearMap.comp_apply]
  rw [← Matrix.reindex_symm, Equiv.symm_apply_apply]

theorem reindex_reindex {l m n : Type} (e₀ : l ≃ m) (e : m ≃ n) (M : Matrix l l ℂ) :
    Matrix.reindex e e (Matrix.reindex e₀ e₀ M) = Matrix.reindex (e₀.trans e) (e₀.trans e) M := by
  rw [← Matrix.reindex_trans]
  rfl

theorem reindex_isometry' {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') {K : Matrix T T ℂ} (hK : Kᴴ * K = 1) :
    (Matrix.reindex e e K)ᴴ * Matrix.reindex e e K = 1 := by
  rw [Matrix.reindex_apply, Matrix.conjTranspose_submatrix, Matrix.submatrix_mul_equiv, hK,
    Matrix.submatrix_one_equiv]

theorem uniformAttach_reindex {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T']
    [DecidableEq T'] (e : T ≃ T') (m : ℕ) (X : Matrix T' T' ℂ) :
    uniformAttach m (Matrix.reindex e.symm e.symm X)
      = Matrix.reindex (e.prodCongr (Equiv.refl (Fin m))).symm
          (e.prodCongr (Equiv.refl (Fin m))).symm (uniformAttach m X) := by
  ext ⟨s, f⟩ ⟨t, f'⟩
  simp [Matrix.reindex_apply, Matrix.submatrix_apply]

/-- Relabelling the carrier commutes with the discard of a fresh ancilla. -/
theorem transport_discard {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') {m : ℕ}
    (Φ : Matrix (T × Fin m) (T × Fin m) ℂ →ₗ[ℂ] Matrix (T × Fin m) (T × Fin m) ℂ) :
    transport e (discardWith (A := T) m (uniformAttach m) Φ)
      = discardWith (A := T') m (uniformAttach m)
          (transport (e.prodCongr (Equiv.refl (Fin m))) Φ) := by
  refine LinearMap.ext fun X => ?_
  ext s t
  simp only [transport_apply, discardWith, LinearMap.comp_apply, Matrix.reindex_apply,
    Matrix.submatrix_apply]
  show ptraceAnc m (Φ (uniformAttach m (Matrix.reindex e.symm e.symm X))) (e.symm s) (e.symm t)
    = ptraceAnc m (Matrix.reindex _ _ (Φ (Matrix.reindex _ _ (uniformAttach m X)))) s t
  rw [uniformAttach_reindex]
  simp [Matrix.reindex_apply, Matrix.submatrix_apply]

/-- **RELABELLING**: for a label-invariant class the predicate is transported along every
carrier bijection. -/
theorem instAvail_transport (hl : LabelInvariant 𝓘) {T : Type} [Fintype T] [DecidableEq T]
    {O : Type} [Fintype O] [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (h : InstAvail 𝓘 T O F) :
    ∀ (T' : Type) [Fintype T'] [DecidableEq T'] (e : T ≃ T'),
      InstAvail 𝓘 T' O (fun a => transport e (F a)) := by
  induction h with
  | op K hK hiso =>
    intro T' _ _ e
    have := InstAvail.op (𝓘 := 𝓘) (Matrix.reindex e e K) (hl _ _ e _ hK) (reindex_isometry' e hiso)
    simpa only [transport_conjChannel] using this
  | readout e₀ hP =>
    intro T' _ _ e
    have := InstAvail.readout (𝓘 := 𝓘) (e₀.trans e) fun k => by
      rw [← reindex_reindex]; exact hl _ _ e _ (hP k)
    simpa only [transport_conjChannel, reindex_reindex] using this
  | coarse f _ ih =>
    intro T' _ _ e
    have := InstAvail.coarse f (ih T' e)
    simpa only [transport_sum] using this
  | bind _ _ ihF ihG =>
    intro T' _ _ e
    have := InstAvail.bind (ihF T' e) (fun a => ihG a T' e)
    simpa only [transport_comp] using this
  | discard hm _ ih =>
    intro T' _ _ e
    have := InstAvail.discard (𝓘 := 𝓘) hm (ih _ (e.prodCongr (Equiv.refl _)))
    simpa only [transport_discard] using this

end Transport

section Spectator

variable {𝓘 : ImplementationClass}

theorem tensorOf_conjTranspose {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (A : Matrix R R ℂ) (B : Matrix S S ℂ) : (tensorOf A B)ᴴ = tensorOf Aᴴ Bᴴ := by
  ext p q
  simp [Matrix.conjTranspose_apply, tensorOf_apply]

theorem tensorOf_mul' {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (A C : Matrix R R ℂ) (B D : Matrix S S ℂ) :
    tensorOf A B * tensorOf C D = tensorOf (A * C) (B * D) := by
  ext p q
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
  ring

theorem tensorOf_one_isometry' {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    {K : Matrix S S ℂ} (hK : Kᴴ * K = 1) :
    (tensorOf (1 : Matrix R R ℂ) K)ᴴ * tensorOf (1 : Matrix R R ℂ) K = 1 := by
  rw [tensorOf_conjTranspose, tensorOf_mul', Matrix.conjTranspose_one, Matrix.one_mul, hK,
    tensorOf_one_one]

theorem amplRefL_conjChannel (R : Type) [Fintype R] [DecidableEq R] {S : Type} [Fintype S]
    [DecidableEq S] (K : Matrix S S ℂ) :
    amplRefL R (conjChannel K) = conjChannel (tensorOf (1 : Matrix R R ℂ) K) :=
  LinearMap.ext fun M => amplRef_conjChannel K M

theorem amplRefL_sum (R : Type) [Fintype R] [DecidableEq R] {S : Type} [Fintype S] [DecidableEq S]
    {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    amplRefL R (∑ i ∈ s, Φ i) = ∑ i ∈ s, amplRefL R (Φ i) := by
  refine LinearMap.ext fun M => ?_
  rw [LinearMap.sum_apply]
  exact amplRef_sum_map s Φ M

theorem amplRef_apply' {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (M : Matrix (R × S) (R × S) ℂ) (p q : R × S) :
    amplRef R Φ M p q = Φ (refBlockR M p.1 q.1) p.2 q.2 := rfl

theorem refBlockR_amplRef {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (M : Matrix (R × S) (R × S) ℂ) (r r' : R) :
    refBlockR (amplRef R Ψ M) r r' = Ψ (refBlockR M r r') := by
  ext k l
  rfl

theorem amplRefL_comp (R : Type) [Fintype R] [DecidableEq R] {S : Type} [Fintype S] [DecidableEq S]
    (Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    amplRefL R (Φ.comp Ψ) = (amplRefL R Φ).comp (amplRefL R Ψ) := by
  refine LinearMap.ext fun M => ?_
  ext ⟨r, k⟩ ⟨r', l⟩
  show amplRef R (Φ.comp Ψ) M (r, k) (r', l) = amplRef R Φ (amplRef R Ψ M) (r, k) (r', l)
  rw [amplRef_apply', amplRef_apply', refBlockR_amplRef]
  rfl

theorem tensorOf_one_reindex {R S S' : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    [Fintype S'] [DecidableEq S'] (e : S ≃ S') (K : Matrix S S ℂ) :
    tensorOf (1 : Matrix R R ℂ) (Matrix.reindex e e K)
      = Matrix.reindex ((Equiv.refl R).prodCongr e) ((Equiv.refl R).prodCongr e)
          (tensorOf (1 : Matrix R R ℂ) K) := by
  ext ⟨r, x⟩ ⟨r', y⟩
  simp [Matrix.reindex_apply, Matrix.submatrix_apply]

theorem tensorOf_one_readProj {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    (m : ℕ) (k : Fin m) :
    tensorOf (1 : Matrix R R ℂ) (readProj S m k)
      = Matrix.reindex (Equiv.prodAssoc R S (Fin m)) (Equiv.prodAssoc R S (Fin m))
          (readProj (R × S) m k) := by
  ext ⟨r, x, f⟩ ⟨r', y, f'⟩
  simp only [tensorOf_apply, readProj, Matrix.diagonal_apply, Matrix.one_apply, Matrix.reindex_apply,
    Matrix.submatrix_apply, Equiv.prodAssoc_symm_apply, Prod.mk.injEq]
  by_cases hr : r = r' <;> by_cases hx : x = y <;> by_cases hf : f = f' <;> simp [hr, hx, hf]

/-- Amplification by a spectator commutes with relabelling of the carrier. -/
theorem amplRefL_transport (R : Type) [Fintype R] [DecidableEq R] {S S' : Type} [Fintype S]
    [DecidableEq S] [Fintype S'] [DecidableEq S'] (e : S ≃ S')
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    amplRefL R (transport e Φ)
      = transport ((Equiv.refl R).prodCongr e) (amplRefL R Φ) := by
  refine LinearMap.ext fun M => ?_
  ext ⟨r, x⟩ ⟨r', y⟩
  simp only [amplRefL_apply, amplRef, Matrix.of_apply, transport_apply, Matrix.reindex_apply,
    Matrix.submatrix_apply, Equiv.prodCongr_symm, Equiv.prodCongr_apply, Equiv.refl_symm,
    Equiv.coe_refl, Prod.map_apply, id_eq]
  congr 2

theorem refBlockR_reindex_uniformAttach {R S : Type} [Fintype R] [DecidableEq R] [Fintype S]
    [DecidableEq S] (m : ℕ) (M : Matrix (R × S) (R × S) ℂ) (r r' : R) :
    refBlockR (Matrix.reindex (Equiv.prodAssoc R S (Fin m)) (Equiv.prodAssoc R S (Fin m))
        (uniformAttach m M)) r r'
      = uniformAttach m (refBlockR M r r') := by
  ext ⟨x, f⟩ ⟨y, f'⟩
  simp [refBlockR, Matrix.reindex_apply, Matrix.submatrix_apply]

/-- Amplification by a spectator commutes with the discard of a fresh ancilla, the ancilla
being regrouped past the spectator. -/
theorem amplRefL_discard (R : Type) [Fintype R] [DecidableEq R] {S : Type} [Fintype S]
    [DecidableEq S] {m : ℕ}
    (Φ : Matrix (S × Fin m) (S × Fin m) ℂ →ₗ[ℂ] Matrix (S × Fin m) (S × Fin m) ℂ) :
    amplRefL R (discardWith (A := S) m (uniformAttach m) Φ)
      = discardWith (A := R × S) m (uniformAttach m)
          (transport (Equiv.prodAssoc R S (Fin m)).symm (amplRefL R Φ)) := by
  refine LinearMap.ext fun M => ?_
  ext ⟨r, x⟩ ⟨r', y⟩
  simp only [amplRefL_apply, amplRef, Matrix.of_apply, discardWith, LinearMap.comp_apply,
    transport_apply, Equiv.symm_symm]
  show ∑ f, (Φ (uniformAttach m (refBlockR M r r'))) (x, f) (y, f)
    = ∑ f, (Matrix.reindex (Equiv.prodAssoc R S (Fin m)).symm (Equiv.prodAssoc R S (Fin m)).symm
        (amplRef R Φ (Matrix.reindex (Equiv.prodAssoc R S (Fin m)) (Equiv.prodAssoc R S (Fin m))
          (uniformAttach m M)))) ((r, x), f) ((r', y), f)
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [Matrix.reindex_apply, Matrix.submatrix_apply, Equiv.symm_symm, Equiv.prodAssoc_apply,
    Equiv.prodAssoc_apply, amplRef_apply', refBlockR_reindex_uniformAttach]

/-- **SPECTATORS**: for a context-stable, label-invariant class the predicate is closed under
an uncoupled spectator. -/
theorem instAvail_spectator (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘) (R : Type) [Fintype R]
    [DecidableEq R] {T : Type} [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) :
    InstAvail 𝓘 (R × T) O (fun a => amplRefL R (F a)) := by
  induction h with
  | op K hK hiso =>
    have := InstAvail.op (𝓘 := 𝓘) (tensorOf (1 : Matrix R R ℂ) K) (hc R _ _ hK)
      (tensorOf_one_isometry' hiso)
    simpa only [amplRefL_conjChannel] using this
  | readout e hP =>
    have hre : ∀ k, tensorOf (1 : Matrix R R ℂ) (Matrix.reindex e e (readProj _ _ k))
        = Matrix.reindex ((Equiv.prodAssoc R _ _).trans ((Equiv.refl R).prodCongr e))
            ((Equiv.prodAssoc R _ _).trans ((Equiv.refl R).prodCongr e)) (readProj (R × _) _ k) :=
      fun k => by rw [tensorOf_one_reindex, tensorOf_one_readProj, reindex_reindex]
    have := InstAvail.readout (𝓘 := 𝓘)
      ((Equiv.prodAssoc R _ _).trans ((Equiv.refl R).prodCongr e))
      fun k => by rw [← hre]; exact hc R _ _ (hP k)
    simpa only [amplRefL_conjChannel, hre] using this
  | coarse f _ ih =>
    have := InstAvail.coarse f ih
    simpa only [amplRefL_sum] using this
  | bind _ _ ihF ihG =>
    have := InstAvail.bind ihF ihG
    simpa only [amplRefL_comp] using this
  | discard hm _ ih =>
    have := InstAvail.discard (𝓘 := 𝓘) hm
      (instAvail_transport hl ih _ (Equiv.prodAssoc R _ _).symm)
    simpa only [amplRefL_discard] using this

/-- **THE LOCAL FORM KEEPS INSTRUMENT REALIZATION**: the spectator extension of an
instrument-realized family is instrument-realized. -/
theorem instAvail_withSpectator (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘) {A : Type}
    [Fintype A] [DecidableEq A] {R : Type} [Fintype R] [DecidableEq R] {n m : ℕ}
    (e : R × (A × Fin n) ≃ A × Fin m) {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : InstAvail 𝓘 (A × Fin n) O F) :
    InstAvail 𝓘 (A × Fin m) O (fun a => withSpectator R e (F a)) :=
  instAvail_transport hl (instAvail_spectator hc hl R h) _ e

end Spectator

/-! ### Section C — the theory an architecture generates by instruments -/

section Generated

variable (𝓘 : ImplementationClass) (arch : Architecture 𝓘)

/-- **THE INSTRUMENT THEORY OF AN ARCHITECTURE** on a carrier: availability is instrument
realization, on the system and at every level. -/
noncomputable def instTheory (S : Type) [Fintype S] [DecidableEq S] :
    FiniteOperationalTheory S where
  avail := fun _ _ _ F => InstAvail 𝓘 S _ F
  availExt := fun _ _ _ _ F => InstAvail 𝓘 _ _ F
  avail_id := instAvail_id (arch.one S)
  avail_coarse := fun _ _ _ _ _ _ _ f h => InstAvail.coarse f h
  availExt_coarse := fun _ _ _ _ _ _ _ _ f h => InstAvail.coarse f h
  availExt_bind := fun _ _ _ _ _ _ _ _ _ hF hG => InstAvail.bind hF hG
  prepAvail := fun n P => 0 < n ∧ ∃ Φ, InstAvail 𝓘 _ Unit (fun _ : Unit => Φ)
    ∧ P = Φ.comp (uniformAttach n)
  prepAvail_uniform := fun n =>
    ⟨n.succ_pos, LinearMap.id, instAvail_id (arch.one _), by rw [LinearMap.id_comp]⟩
  prepAvail_post := by
    rintro n P Φ ⟨hn, Ψ, hΨ, rfl⟩ hΦ
    exact ⟨hn, Φ.comp Ψ, instAvail_one_comp hΦ hΨ, by rw [LinearMap.comp_assoc]⟩
  readout := fun _ k => localLuders k
  readout_avail := fun n => by
    have h := InstAvail.readout (𝓘 := 𝓘) (Equiv.refl (S × Fin n))
      (fun k => by rw [Matrix.reindex_refl_refl]; exact arch.proj S n k)
    simp only [Matrix.reindex_refl_refl] at h
    have e : (fun k : Fin n => localLuders (A := S) k)
        = fun k => conjChannel (readProj S n k) := funext fun k => localLuders_eq_conjChannel k
    rw [e]
    exact h
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hn, Φ, hΦ, rfl⟩ hF
    have e : (fun a => discardWith n (Φ.comp (uniformAttach n)) (F a))
        = fun a => discardWith (A := S) n (uniformAttach n) ((F a).comp Φ) := by
      funext a
      simp only [discardWith, LinearMap.comp_assoc]
    rw [e]
    exact InstAvail.discard hn (instAvail_comp_one hF hΦ)

/-- The instrument family. -/
noncomputable def instFamily : TheoryFamily := fun S _ _ => instTheory 𝓘 arch S

theorem instFamily_regrouping : RegroupingInvariant (instFamily 𝓘 arch) := by
  intro S _ _ m _ O _ _ F
  exact Iff.rfl

theorem instFamily_relabelling (hl : LabelInvariant 𝓘) :
    RelabellingInvariant (instFamily 𝓘 arch) := by
  intro S S' _ _ _ _ e O _ _ F h
  exact instAvail_transport hl h S' e

variable {A : Type} [Fintype A] [DecidableEq A]

theorem instTheory_ambient : IsAmbientMember (instTheory 𝓘 arch A) (instFamily 𝓘 arch) :=
  ⟨fun _ _ _ _ => Iff.rfl, fun _ _ _ _ _ _ => Iff.rfl⟩

/-- **T3: INSTRUMENT THEORIES CARRY EMBEDDED OBSERVATION** when the class is label-invariant. -/
theorem instTheory_embeddedObservation (hl : LabelInvariant 𝓘) :
    EmbeddedObservation (instTheory 𝓘 arch A) :=
  ⟨instFamily 𝓘 arch, instFamily_regrouping 𝓘 arch, instFamily_relabelling 𝓘 arch hl,
    instTheory_ambient 𝓘 arch⟩

theorem instTheory_availExt_iff (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (instTheory 𝓘 arch A).availExt n O F ↔ InstAvail 𝓘 (A × Fin n) O F :=
  Iff.rfl

/-- **THE INSTRUMENT THEORY LIES INSIDE THE GENERATED THEORY**: every family available by
instruments is available branch-wise. -/
theorem instTheory_le_genTheory (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (h : (instTheory 𝓘 arch A).availExt n O F) : (genTheory 𝓘 arch A).availExt n O F :=
  isGenInstrument_of_instAvail arch h

/-- A unitary conjugation is available in the instrument theory of a class containing the
unitary. -/
theorem instTheory_avail_conj {n : ℕ} {V : Matrix (A × Fin n) (A × Fin n) ℂ}
    (hV : 𝓘 (A × Fin n) V) (hiso : Vᴴ * V = 1) :
    (instTheory 𝓘 arch A).availExt n Unit (fun _ => conjChannel V) :=
  InstAvail.op V hV hiso

/-- **COMPOSITE UNITARY CONTROL IN THE INSTRUMENT THEORY OF THE FULL CLASS.** -/
theorem instTheory_fullClass_control : HasCompositeUnitaryControl (instTheory fullClass fullClass_arch A) :=
  fun _ U hU => InstAvail.op U trivial hU

/-- Class inclusion carries instrument availability at every level. -/
theorem instTheory_mono {𝓙 : ImplementationClass} (arch' : Architecture 𝓙)
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → 𝓙 S K) (n : ℕ)
    {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (h : (instTheory 𝓘 arch A).availExt n O F) : (instTheory 𝓙 arch' A).availExt n O F :=
  instAvail_mono hle h

end Generated

/-! ### Section D — the implementation-locality stack for the new primitive -/

section Stack

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **(G′) INSTRUMENT GENERATION**: at every positive level, availability is instrument
realization by the class. The normalization half of validity is a theorem of the predicate
(`instAvail_trace`), not a clause. -/
def InstrumentGenerated (T : FiniteOperationalTheory A) (𝓘 : ImplementationClass) : Prop :=
  ∀ (N : ℕ), 0 < N → ∀ (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ),
    T.availExt N O F ↔ InstAvail 𝓘 (A × Fin N) O F

/-- **INSTRUMENT LOCALITY**: availability is instrument-generated by a context-stable,
label-invariant implementation class. -/
def InstrumentLocality (T : FiniteOperationalTheory A) : Prop :=
  ∃ 𝓘 : ImplementationClass, InstrumentGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘

/-- **REVERSIBLE INSTRUMENT LOCALITY**: instrument locality with a dagger-stable class. -/
def ReversibleInstrumentLocality (T : FiniteOperationalTheory A) : Prop :=
  ∃ 𝓘 : ImplementationClass, InstrumentGenerated T 𝓘 ∧ ContextStable 𝓘 ∧ LabelInvariant 𝓘
    ∧ DaggerStable 𝓘

theorem instrumentLocality_of_reversible {T : FiniteOperationalTheory A}
    (h : ReversibleInstrumentLocality T) : InstrumentLocality T := by
  obtain ⟨𝓘, hg, hc, hl, -⟩ := h
  exact ⟨𝓘, hg, hc, hl⟩

variable {𝓘 : ImplementationClass}

theorem instTheory_generated (arch : Architecture 𝓘) :
    InstrumentGenerated (instTheory 𝓘 arch A) 𝓘 :=
  fun _ _ _ _ _ _ => Iff.rfl

theorem instTheory_instrumentLocality (arch : Architecture 𝓘) (hc : ContextStable 𝓘)
    (hl : LabelInvariant 𝓘) : InstrumentLocality (instTheory 𝓘 arch A) :=
  ⟨𝓘, instTheory_generated arch, hc, hl⟩

theorem instTheory_reversibleInstrumentLocality (arch : Architecture 𝓘) (hc : ContextStable 𝓘)
    (hl : LabelInvariant 𝓘) (hd : DaggerStable 𝓘) :
    ReversibleInstrumentLocality (instTheory 𝓘 arch A) :=
  ⟨𝓘, instTheory_generated arch, hc, hl, hd⟩

/-- **INSTRUMENT GENERATION IS SOUND FOR BRANCH-WISE GENERATION**: every family available in an
instrument-generated theory of an architecture is a generated instrument of the branch-wise
notion. The converse is the content of T2. -/
theorem isGenInstrument_of_instrumentGenerated (arch : Architecture 𝓘)
    {T : FiniteOperationalTheory A} (hg : InstrumentGenerated T 𝓘) {N : ℕ} (hN : 0 < N)
    {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (A × Fin N) (A × Fin N) ℂ →ₗ[ℂ] Matrix (A × Fin N) (A × Fin N) ℂ}
    (hF : T.availExt N O F) : IsGenInstrument 𝓘 (A × Fin N) F :=
  isGenInstrument_of_instAvail arch ((hg N hN O F).mp hF)

/-- **OBSERVATIONAL INDEPENDENCE FROM INSTRUMENT LOCALITY**, in its parallel reference-extension
form. -/
theorem parallel_of_instrumentLocal [Nonempty A] {T : FiniteOperationalTheory A}
    (hg : InstrumentGenerated T 𝓘) (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘) :
    HasParallelReferenceExtension T := by
  intro R _ _ n m e O _ _ F hF
  rcases m with _ | m'
  · exact availExt_zero T _
  rcases n with _ | k
  · exfalso
    have hc' := Fintype.card_congr e
    simp only [Fintype.card_prod, Fintype.card_fin, mul_zero] at hc'
    exact absurd hc'.symm (Nat.mul_pos Fintype.card_pos m'.succ_pos).ne'
  exact (hg (m' + 1) m'.succ_pos O _).mpr
    (instAvail_withSpectator hc hl e ((hg (k + 1) k.succ_pos O F).mp hF))

theorem observationalIndependence_of_instrumentLocality [Nonempty A]
    {T : FiniteOperationalTheory A} (h : InstrumentLocality T) : ObservationalIndependence T := by
  obtain ⟨𝓘, hg, hc, hl⟩ := h
  exact parallel_of_instrumentLocal hg hc hl

/-- Instrument-generated theories are composite Kraus-sound, for every class. -/
theorem krausSoundExt_of_instrumentGenerated [Nonempty A] {T : FiniteOperationalTheory A}
    (hg : InstrumentGenerated T 𝓘) : KrausSoundExt T := by
  intro n O _ _ F hF
  have h := (hg (n + 1) n.succ_pos O F).mp hF
  exact isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
    (cp_of_instAvail h) (instAvail_trace h)

/-- **VALIDITY IS DERIVED** from instrument locality. -/
theorem validity_of_instrumentLocality [Nonempty A] {T : FiniteOperationalTheory A}
    (h : InstrumentLocality T) : CompositeOperationalValidity T := by
  obtain ⟨𝓘, hg, -, -⟩ := h
  exact validity_of_krausSoundExt T (krausSoundExt_of_instrumentGenerated hg)

/-- **EVERY FINITE KRAUS FAMILY IS INSTRUMENT-REALIZED BY THE FULL CLASS**: the Stinespring
circuit of the instrument theory of the full class, a pure seed obtained from the uniform ancilla
by readout and feed-forward, a composite unitary extending the Stinespring isometry, the readout
and the discard, followed by the coarse-graining along the outcome labelling. -/
theorem instAvail_fullClass_of_krausFamily {S : Type} [Fintype S] [DecidableEq S] {O : Type}
    [Fintype O] [DecidableEq O] {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hK : IsKrausFamily F) :
    InstAvail fullClass S O F := by
  obtain ⟨n, K, out, hnorm, hKF⟩ := hK
  have hfull := fullInstruments_of_control (instTheory fullClass fullClass_arch S)
    (finiteIsometryExtensionSF_discharged S) instTheory_fullClass_control
  have h := InstAvail.coarse out (hfull n (n + 1) K id hnorm)
  have e : F = fun a => ∑ j ∈ Finset.univ.filter (fun j => out j = a), instrumentBranch K id j := by
    funext a
    rw [hKF a]
    refine Finset.sum_congr rfl fun j _ => ?_
    simp [instrumentBranch, Finset.filter_eq']
  rw [e]
  exact h

/-- **AN EXACT THEORY IS INSTRUMENT-GENERATED BY THE FULL CLASS.** -/
theorem instrumentGenerated_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : InstrumentGenerated T fullClass := by
  intro N hN O _ _ F
  constructor
  · intro hF
    exact instAvail_fullClass_of_krausFamily (krausFamily_of_exactComposite T h.2 N hN F hF)
  · intro hI
    have : Nonempty (A × Fin N) := ⟨(Classical.arbitrary A, ⟨0, hN⟩)⟩
    exact availExt_of_krausFamily T h.2 N hN F
      (isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
        (cp_of_instAvail hI) (instAvail_trace hI))

/-- **EXACT FINITE OPERATIONAL QM IS INSTRUMENT-LOCAL.** -/
theorem instrumentLocality_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : InstrumentLocality T :=
  ⟨fullClass, instrumentGenerated_of_qm T h, fullClass_contextStable, fullClass_labelInvariant⟩

theorem reversibleInstrumentLocality_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : ReversibleInstrumentLocality T :=
  ⟨fullClass, instrumentGenerated_of_qm T h, fullClass_contextStable, fullClass_labelInvariant,
    fun _ _ _ _ _ => trivial⟩

/-- **THE DIAGNOSIS**: the countermodel is not instrument-generated by any class. -/
theorem countermodel_not_instrumentGenerated :
    ¬ ∃ 𝓘 : ImplementationClass, InstrumentGenerated countermodel 𝓘 := by
  rintro ⟨𝓘, hg⟩
  have h := (hg 2 two_pos Unit (fun _ => reduction2 (Fin 2 × Fin 2))).mp
    countermodel_reduction2_available
  exact reduction2_not_cp (cp_of_instAvail h ())

theorem countermodel_not_instrumentLocality : ¬ InstrumentLocality countermodel :=
  fun ⟨𝓘, hg, _⟩ => countermodel_not_instrumentGenerated ⟨𝓘, hg⟩

/-- **INSTRUMENT LOCALITY IS NOT SUPPLIED** by the core, validity, reversible richness and
embedded observation. -/
theorem instrumentLocality_independent :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ CompositeOperationalValidity T
      ∧ OIHierarchyGeneral.ReversibleRichness T ∧ EmbeddedObservation T ∧ ¬ InstrumentLocality T :=
  ⟨countermodel, countermodel_realizesSealedOICore, countermodel_validity,
    countermodel_reversibleRichness, countermodel_embeddedObservation,
    countermodel_not_instrumentLocality⟩

/-- **THE COMPRESSED SET, INSTRUMENT FORM**: instrument locality, reversible richness, embedded
observation. -/
def OIPlusInst (T : FiniteOperationalTheory A) : Prop :=
  InstrumentLocality T ∧ OIHierarchyGeneral.ReversibleRichness T ∧ EmbeddedObservation T

/-- **THE MINIMAL-REPERTOIRE PACKAGE, INSTRUMENT FORM**: instrument locality, phase-free
richness, embedded observation. -/
def OIPlusMinInst (T : FiniteOperationalTheory A) : Prop :=
  InstrumentLocality T ∧ PhaseFreeRichness T ∧ EmbeddedObservation T

variable [Nonempty A] (T : FiniteOperationalTheory A)

theorem oiPlusEmbedded_of_oiPlusInst (h : OIPlusInst T) : OIPlusEmbedded T :=
  ⟨validity_of_instrumentLocality h.1, observationalIndependence_of_instrumentLocality h.1,
    h.2.1, h.2.2⟩

theorem qm_of_oiPlusInst (h : OIPlusInst T) : ExactAllFiniteEndomorphicQuantumOps T :=
  qm_of_oiPlusEmbedded T (oiPlusEmbedded_of_oiPlusInst T h)

theorem oiPlusInst_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusInst T :=
  have hp := oiPlusEmbedded_of_qm T h
  ⟨instrumentLocality_of_qm T h, hp.2.2.1, hp.2.2.2⟩

/-- **THE COMPRESSED SET, INSTRUMENT FORM, ⟺ FINITE OPERATIONAL QM.** -/
theorem oiPlusInst_iff_qm : OIPlusInst T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusInst T, oiPlusInst_of_qm T⟩

theorem qm_of_oiPlusMinInst (h : OIPlusMinInst T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨hloc, hrich, hemb⟩ := h
  have hwf : WellFormed T :=
    ⟨validity_of_instrumentLocality hloc, systemToLevelOne_of_embeddedObservation hemb⟩
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp
      (observationalIndependence_of_instrumentLocality hloc),
    control_of_phaseFree T (closure_of_embeddedObservation hemb) hrich,
    closure_of_embeddedObservation hemb⟩

theorem oiPlusMinInst_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusMinInst T :=
  ⟨instrumentLocality_of_qm T h,
    phaseFree_of_elementary T (elementary_of_control T (physical_of_exactAll T h).2.2.1),
    embeddedObservation_of_qm T h⟩

/-- **THE MINIMAL-REPERTOIRE PACKAGE, INSTRUMENT FORM, ⟺ FINITE OPERATIONAL QM.** -/
theorem oiPlusMinInst_iff_qm : OIPlusMinInst T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusMinInst T, oiPlusMinInst_of_qm T⟩

/-- The two forms of the package agree, through quantum mechanics. -/
theorem oiPlusMinInst_iff_oiPlusMin : OIPlusMinInst T ↔ OIPlusMin T := by
  rw [oiPlusMinInst_iff_qm, oiPlusMin_iff_qm]

end Stack

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlusMinInst :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]
      (T : FiniteOperationalTheory A),
      OIPlusMinInst T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlusMinInst_iff_qm T

/-! ### Section E — inverse accessibility, with the hypothesis it now needs -/

section Inverse

variable {A : Type} [Fintype A] [DecidableEq A] {𝓘 : ImplementationClass}

/-- **PHASE SATURATION**: a class that contains a nonzero contractive multiple of a unitary
contains the unitary. The four classes of the kernel have it; the closed-form class of the
countercontrol does not. -/
def PhaseSaturated (𝓘 : ImplementationClass) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (c : ℂ) (V : Matrix S S ℂ), c ≠ 0 → Vᴴ * V = 1 →
    𝓘 S (c • V) → 𝓘 S V

theorem conjChannel_zero' {S : Type} [Fintype S] [DecidableEq S] :
    conjChannel (0 : Matrix S S ℂ) = 0 := by
  refine LinearMap.ext fun X => ?_
  show (0 : Matrix S S ℂ) * X * (0 : Matrix S S ℂ)ᴴ = 0
  simp

/-- **AN INSTRUMENT-REALIZED UNITARY CONJUGATION HAS ITS UNITARY ADMISSIBLE** up to a nonzero
contractive scalar: every branch of its branch-wise realization is proportional to the unitary,
and some branch is nonzero. -/
theorem exists_scaled_mem_of_instAvail_unitary (arch : Architecture 𝓘) {S : Type} [Fintype S]
    [DecidableEq S] [Nonempty S] {V : Matrix S S ℂ}
    (h : InstAvail 𝓘 S Unit (fun _ => conjChannel V)) : ∃ c : ℂ, c ≠ 0 ∧ 𝓘 S (c • V) := by
  obtain ⟨ι, _, K, hK, hadm⟩ := realized_of_instAvail arch h ()
  have hiso : Vᴴ * V = 1 := (conjChannel_trace_iff V).mp fun X => by
    have := instAvail_trace h X
    rwa [Fintype.sum_unique] at this
  have hV0 : V ≠ 0 := by
    intro h0
    rw [h0, Matrix.mul_zero] at hiso
    exact zero_ne_one hiso
  have hK' := kraus_of_conj_unitary K V hV0 hK.symm
  choose c hc using hK'
  by_contra hall
  have hall' : ∀ c' : ℂ, c' ≠ 0 → ¬ 𝓘 S (c' • V) := fun c' hc' hm => hall ⟨c', hc', hm⟩
  have hzero : ∀ i, K i = 0 := fun i => by
    by_cases hci : c i = 0
    · rw [hc i, hci, zero_smul]
    · exact absurd (hc i ▸ hadm i) (hall' (c i) hci)
  have h0 : conjChannel V = 0 := by
    rw [hK]
    exact Finset.sum_eq_zero fun i _ => by rw [hzero i, conjChannel_zero']
  have h1 := congrFun (congrFun (congrArg (fun Φ => Φ (1 : Matrix S S ℂ)) h0)
    (Classical.arbitrary S)) (Classical.arbitrary S)
  simp only [conjChannel_apply, Matrix.mul_one, mul_eq_one_comm.mp hiso, LinearMap.zero_apply,
    Matrix.one_apply_eq, Matrix.zero_apply] at h1
  exact one_ne_zero h1

/-- **INVERSE ACCESSIBILITY FROM DAGGER-STABLE INSTRUMENT GENERATION, UNDER PHASE
SATURATION.** The branch-wise proof re-summed the adjoint branches; the adjoint of a protocol
is not a protocol, so the unitary itself has to be admissible: phase saturation supplies it
from the nonzero branch, dagger stability supplies the adjoint, and one step realizes it. -/
theorem inverseAccessibility_of_instrumentGenerated [Nonempty A] {T : FiniteOperationalTheory A}
    (arch : Architecture 𝓘) (hg : InstrumentGenerated T 𝓘) (hd : DaggerStable 𝓘)
    (hs : PhaseSaturated 𝓘) : InverseAccessibility T := by
  intro n V hV
  rcases n with _ | k
  · exact availExt_zero T _
  have hI := (hg (k + 1) k.succ_pos Unit _).mp hV
  have hiso : Vᴴ * V = 1 := (conjChannel_trace_iff V).mp fun X => by
    have := instAvail_trace hI X
    rwa [Fintype.sum_unique] at this
  have : Nonempty (A × Fin (k + 1)) := ⟨(Classical.arbitrary A, ⟨0, k.succ_pos⟩)⟩
  obtain ⟨c, hc0, hcV⟩ := exists_scaled_mem_of_instAvail_unitary arch hI
  have hVmem : 𝓘 _ V := hs _ c V hc0 hiso hcV
  refine (hg (k + 1) k.succ_pos Unit _).mpr (InstAvail.op Vᴴ (hd _ _ hVmem) ?_)
  rw [Matrix.conjTranspose_conjTranspose]
  exact mul_eq_one_comm.mp hiso

theorem inverseAccessibility_of_reversibleInstrumentLocality [Nonempty A]
    {T : FiniteOperationalTheory A} (h : ReversibleInstrumentLocality T)
    (harch : ∀ 𝓘, InstrumentGenerated T 𝓘 → Architecture 𝓘 ∧ PhaseSaturated 𝓘) :
    InverseAccessibility T := by
  obtain ⟨𝓘, hg, -, -, hd⟩ := h
  exact inverseAccessibility_of_instrumentGenerated (harch 𝓘 hg).1 hg hd (harch 𝓘 hg).2

/-- The four classes of the kernel are phase-saturated. -/
theorem fullClass_phaseSaturated : PhaseSaturated fullClass := fun _ _ _ _ _ _ _ _ => trivial

theorem diagClass_phaseSaturated : PhaseSaturated diagClass := by
  intro S _ _ c V hc _ h p q hpq
  have := h p q hpq
  rw [Matrix.smul_apply, smul_eq_mul] at this
  exact (mul_eq_zero.mp this).resolve_left hc

theorem substratumClass_phaseSaturated : PhaseSaturated substratumClass := by
  intro S _ _ c V hc _ h
  obtain ⟨σ, d, hd⟩ := h
  refine ⟨σ, c⁻¹ • d, ?_⟩
  rw [Matrix.diagonal_smul, Matrix.mul_smul, ← hd, smul_smul, inv_mul_cancel₀ hc, one_smul]

theorem permClass_phaseSaturated : PhaseSaturated permClass := by
  intro S _ _ c V hc hV hK
  obtain ⟨hsub, c₀, hc₀, hall⟩ := hK
  have hne : ∀ i j, V i j ≠ 0 → (c • V) i j ≠ 0 := fun i j h => by
    rw [Matrix.smul_apply, smul_eq_mul]
    exact mul_ne_zero hc h
  have hentry : ∀ i j, V i j ≠ 0 → V i j = c₀ / c := fun i j h => by
    have := hall i j (hne i j h)
    rw [Matrix.smul_apply, smul_eq_mul] at this
    rw [← this, mul_div_cancel_left₀ _ hc]
  refine ⟨⟨fun i j j' h h' => hsub.1 i j j' (hne i j h) (hne i j' h'),
    fun i i' j h h' => hsub.2 i i' j (hne i j h) (hne i' j h')⟩, ?_⟩
  by_cases hex : ∃ i j, V i j ≠ 0
  · obtain ⟨i, j, hij⟩ := hex
    refine ⟨c₀ / c, ?_, hentry⟩
    have hVV : V * Vᴴ = 1 := mul_eq_one_comm.mp hV
    have hrow := congrFun (congrFun hVV i) i
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at hrow
    have h1 : (∑ k, Complex.normSq (V i k) : ℝ) = 1 := by
      have h2 : ∑ k, V i k * Vᴴ k i = ((∑ k, Complex.normSq (V i k) : ℝ) : ℂ) := by
        push_cast
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [Matrix.conjTranspose_apply, Complex.star_def, Complex.mul_conj]
      rw [h2] at hrow
      exact_mod_cast hrow
    have hle : Complex.normSq (V i j) ≤ 1 := by
      rw [← h1]
      exact Finset.single_le_sum (fun k _ => Complex.normSq_nonneg _) (Finset.mem_univ j)
    rw [hentry i j hij, Complex.normSq_eq_norm_sq] at hle
    exact (pow_le_one_iff_of_nonneg (norm_nonneg _) two_ne_zero).mp hle
  · have hex' : ∀ i j, V i j = 0 := fun i j => by_contra fun h => hex ⟨i, j, h⟩
    exact ⟨0, by simp, fun i j h => absurd (hex' i j) h⟩

end Inverse

/-! ### Section F — T2: the converse fails -/

section Converse

variable {𝓘 : ImplementationClass}

/-- The all-ones vector on a carrier. -/
def ones (T : Type) : T → ℂ := fun _ => 1

theorem ones_apply (T : Type) (t : T) : ones T t = 1 := rfl

theorem ones_prod (R S : Type) : ones (R × S) = fun p => ones R p.1 * ones S p.2 := by
  funext p
  simp [ones]

theorem ones_sum (R S : Type) : ones (R ⊕ S) = Sum.elim (ones R) (ones S) := by
  funext p
  cases p <;> rfl

theorem mulVec_sum' {R T : Type} [Fintype R] [Fintype T] (A : Matrix R T ℂ) {ι : Type*}
    (s : Finset ι) (v : ι → T → ℂ) : A *ᵥ (∑ i ∈ s, v i) = ∑ i ∈ s, A *ᵥ v i := by
  have := map_sum (Matrix.mulVecLin A) v s
  simpa only [Matrix.mulVecLin_apply] using this

/-- **THE PROTOCOL INVARIANT**: a Kraus decomposition of the whole family, over one index set
with an outcome labelling, whose operators sum against the all-ones vector to the all-ones
vector. -/
def OnesNormal (T : Type) [Fintype T] [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ) : Prop :=
  ∃ (ι : Type) (_ : Fintype ι) (K : ι → Matrix T T ℂ) (out : ι → O),
    (∀ a, F a = ∑ i ∈ Finset.univ.filter (fun i => out i = a), conjChannel (K i))
    ∧ ∑ i, (K i)ᴴ *ᵥ ones T = ones T

/-- **ONES-FIXING CLASSES**: every admissible isometry fixes the all-ones vector up to a
scalar. -/
def OnesFixing (𝓘 : ImplementationClass) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → Kᴴ * K = 1 →
    ∃ z : ℂ, K *ᵥ ones S = z • ones S

theorem star_ones_dotProduct_ones (S : Type) [Fintype S] :
    star (ones S) ⬝ᵥ ones S = (Fintype.card S : ℂ) := by
  simp [dotProduct, ones, Finset.sum_const, Finset.card_univ]

/-- A unitary eigenvalue on the all-ones vector has modulus one. -/
theorem unitary_eigen_ones {S : Type} [Fintype S] [DecidableEq S] [Nonempty S]
    {K : Matrix S S ℂ} (hK : Kᴴ * K = 1) {z : ℂ} (hz : K *ᵥ ones S = z • ones S) :
    star z * z = 1 := by
  have h1 : star (K *ᵥ ones S) ⬝ᵥ (K *ᵥ ones S) = star (ones S) ⬝ᵥ ones S := by
    rw [Matrix.star_mulVec, Matrix.dotProduct_mulVec, Matrix.vecMul_vecMul, hK, Matrix.vecMul_one]
  rw [hz, star_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul, ← mul_assoc,
    star_ones_dotProduct_ones] at h1
  have hc : (Fintype.card S : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  exact mul_right_cancel₀ hc (by rw [h1, one_mul])

theorem conjTranspose_mulVec_ones_of_eigen {S : Type} [Fintype S] [DecidableEq S]
    {K : Matrix S S ℂ} (hK : Kᴴ * K = 1) {z : ℂ} (hz : K *ᵥ ones S = z • ones S)
    (hz1 : star z * z = 1) : Kᴴ *ᵥ ones S = star z • ones S := by
  have h : ones S = star z • (K *ᵥ ones S) := by
    rw [hz, smul_smul, hz1, one_smul]
  conv_lhs => rw [h]
  rw [Matrix.mulVec_smul, Matrix.mulVec_mulVec, hK, Matrix.one_mulVec]

theorem readProj_sum (T : Type) [Fintype T] [DecidableEq T] (m : ℕ) :
    ∑ k, readProj T m k = 1 := by
  ext p q
  by_cases h : p = q
  · subst h
    simp [readProj, Matrix.sum_apply]
  · simp [readProj, Matrix.sum_apply, h]

theorem reindex_sum {l m : Type} [Fintype l] [Fintype m] (e : l ≃ m) {ι : Type*} (s : Finset ι)
    (M : ι → Matrix l l ℂ) :
    Matrix.reindex e e (∑ i ∈ s, M i) = ∑ i ∈ s, Matrix.reindex e e (M i) := by
  ext p q
  simp [Matrix.reindex_apply, Matrix.submatrix_apply, Matrix.sum_apply]

theorem reindex_one {l m : Type} [Fintype l] [DecidableEq l] [Fintype m] [DecidableEq m]
    (e : l ≃ m) : Matrix.reindex e e (1 : Matrix l l ℂ) = 1 := by
  rw [Matrix.reindex_apply, Matrix.submatrix_one_equiv]

/-- Coarse-graining regroups the fibres. -/
theorem sum_filter_comp {ι O O' M : Type*} [Fintype ι] [Fintype O] [DecidableEq O] [DecidableEq O']
    [AddCommMonoid M] (out : ι → O) (f : O → O') (g : ι → M) (a' : O') :
    ∑ j ∈ Finset.univ.filter (fun j => f j = a'),
        ∑ i ∈ Finset.univ.filter (fun i => out i = j), g i
      = ∑ i ∈ Finset.univ.filter (fun i => f (out i) = a'), g i := by
  rw [← Finset.sum_fiberwise_of_maps_to (s := Finset.univ.filter (fun i => f (out i) = a'))
    (t := Finset.univ.filter (fun j => f j = a')) (g := out) (fun i hi => by simpa using hi) g]
  refine Finset.sum_congr rfl fun j hj => Finset.sum_congr ?_ fun _ _ => rfl
  ext i
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · intro h
    exact ⟨by rw [h]; simpa using hj, h⟩
  · intro h
    exact h.2

/-- The continuations of a feed-forward can be decomposed over one common index set. -/
theorem onesNormal_uniform {T : Type} [Fintype T] [DecidableEq T] {O O' : Type} [Fintype O]
    [DecidableEq O] [Fintype O'] [DecidableEq O'] {G : O → O' → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (hG : ∀ a, OnesNormal T (G a)) :
    ∃ (ι : Type) (_ : Fintype ι) (K : O → ι → Matrix T T ℂ) (out : ι → O'),
      (∀ a b, G a b = ∑ i ∈ Finset.univ.filter (fun i => out i = b), conjChannel (K a i))
      ∧ ∀ a, ∑ i, (K a i)ᴴ *ᵥ ones T = ones T := by
  choose ι inst K out hfam hsum using hG
  refine ⟨Σ a, ι a, inferInstance, fun a p => if p.1 = a then K p.1 p.2 else 0,
    fun p => out p.1 p.2, ?_, ?_⟩
  · intro a b
    rw [hfam a b, Finset.sum_filter, Finset.sum_filter, Fintype.sum_sigma, Finset.sum_eq_single a]
    · simp
    · intro a' _ ha'
      refine Finset.sum_eq_zero fun j _ => ?_
      simp [ha', conjChannel_zero']
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro a
    rw [Fintype.sum_sigma, Finset.sum_eq_single a]
    · simpa using hsum a
    · intro a' _ ha'
      refine Finset.sum_eq_zero fun j _ => ?_
      simp [ha']
    · intro h
      exact absurd (Finset.mem_univ _) h

/-- The adjoints of the ancilla blocks of one operator, summed over the readout value, act on the
all-ones vector as the operator's adjoint does on one preparation sector. -/
theorem ancBlock_conjTranspose_mulVec_ones {T : Type} [Fintype T] [DecidableEq T] {m : ℕ}
    (K : Matrix (T × Fin m) (T × Fin m) ℂ) (e : Fin m) :
    ∑ f, (ancBlock K f e)ᴴ *ᵥ ones T = fun t => (Kᴴ *ᵥ ones (T × Fin m)) (t, e) := by
  funext t
  simp only [Finset.sum_apply, Matrix.mulVec, dotProduct, Matrix.conjTranspose_apply, ancBlock,
    Matrix.of_apply, ones_apply, mul_one, Fintype.sum_prod_type]
  exact Finset.sum_comm

/-- The three weights of the split: `1/m`, `β`, `−β` with `β² = (m − 1)/(2m²)`, so that they sum
to `1/m` and their squares sum to `1/m`. -/
noncomputable def splitWeight (m : ℕ) : Fin 3 → ℂ :=
  ![((m : ℝ)⁻¹ : ℝ), (Real.sqrt (((m : ℝ) - 1) / (2 * (m : ℝ) ^ 2)) : ℝ),
    -(Real.sqrt (((m : ℝ) - 1) / (2 * (m : ℝ) ^ 2)) : ℝ)]

theorem splitWeight_sum_star (m : ℕ) : ∑ s, star (splitWeight m s) = ((m : ℂ))⁻¹ := by
  simp [splitWeight, Fin.sum_univ_three]

theorem splitWeight_sum_normSq {m : ℕ} (hm : 0 < m) :
    ∑ s, splitWeight m s * star (splitWeight m s) = ((m : ℂ))⁻¹ := by
  have hm' : (1 : ℝ) ≤ m := Nat.one_le_cast.mpr hm
  have hβ : Real.sqrt (((m : ℝ) - 1) / (2 * (m : ℝ) ^ 2)) ^ 2 = ((m : ℝ) - 1) / (2 * (m : ℝ) ^ 2) :=
    Real.sq_sqrt (by positivity)
  have hm0 : (m : ℝ) ≠ 0 := by positivity
  set β := Real.sqrt (((m : ℝ) - 1) / (2 * (m : ℝ) ^ 2)) with hβ_def
  have h0 : splitWeight m 0 = (((m : ℝ)⁻¹ : ℝ) : ℂ) := rfl
  have h1 : splitWeight m 1 = (β : ℂ) := rfl
  have h2 : splitWeight m 2 = -(β : ℂ) := rfl
  rw [Fin.sum_univ_three, h0, h1, h2]
  simp only [Complex.star_def, Complex.conj_ofReal, map_neg, neg_mul_neg]
  rw [← Complex.ofReal_mul, ← Complex.ofReal_mul, ← Complex.ofReal_add, ← Complex.ofReal_add]
  have key : (m : ℝ)⁻¹ * (m : ℝ)⁻¹ + β * β + β * β = (m : ℝ)⁻¹ := by
    rw [← sq, ← sq, hβ]
    field_simp
    ring
  rw [key]
  push_cast
  rfl

/-- **THE PROTOCOL INVARIANT SURVIVES EVERY CONSTRUCTOR**, the feed-forward included: the
continuations are decomposed over one index set and multiplied into the branches they follow,
and the discard is split into three contractive copies of each block whose weights sum to the
uniform weight. For a ones-fixing class. -/
theorem instAvail_onesNormal (hf : OnesFixing 𝓘) {T : Type} [Fintype T] [DecidableEq T]
    {O : Type} [Fintype O] [DecidableEq O] {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ}
    (h : InstAvail 𝓘 T O F) : OnesNormal T F := by
  induction h with
  | op K hK hiso =>
    rename_i T' iT dT
    obtain ⟨z, hz⟩ := hf _ K hK hiso
    rcases isEmpty_or_nonempty T' with hT | hT
    · exact ⟨Unit, inferInstance, fun _ => K, fun _ => (), fun _ => by simp,
        Subsingleton.elim _ _⟩
    · have hz1 := unitary_eigen_ones hiso hz
      have hsm : conjChannel (star z • K) = conjChannel K := by
        rw [conjChannel_smul, star_star, hz1, one_smul]
      refine ⟨Unit, inferInstance, fun _ => star z • K, fun _ => (), fun _ => ?_, ?_⟩
      · simp only [hsm]
        simp
      · rw [Fintype.sum_unique, Matrix.conjTranspose_smul, star_star, Matrix.smul_mulVec,
          conjTranspose_mulVec_ones_of_eigen hiso hz hz1, smul_smul, mul_comm, hz1, one_smul]
  | readout e hP =>
    refine ⟨Fin _, inferInstance, fun k => Matrix.reindex e e (readProj _ _ k), id,
      fun k => by simp [Finset.filter_eq'], ?_⟩
    rw [← Matrix.sum_mulVec, ← Matrix.conjTranspose_sum, ← reindex_sum, readProj_sum, reindex_one,
      Matrix.conjTranspose_one, Matrix.one_mulVec]
  | coarse f _ ih =>
    obtain ⟨ι, _, K, out, hfam, hsum⟩ := ih
    refine ⟨ι, inferInstance, K, f ∘ out, fun a' => ?_, hsum⟩
    simp only [hfam, Function.comp]
    exact sum_filter_comp out f _ a'
  | bind _ _ ihF ihG =>
    obtain ⟨ι, _, K, out, hfam, hsum⟩ := ihF
    obtain ⟨ι', _, K', out', hfam', hsum'⟩ := onesNormal_uniform ihG
    refine ⟨ι × ι', inferInstance, fun p => K' (out p.1) p.2 * K p.1,
      fun p => (out p.1, out' p.2), ?_, ?_⟩
    · rintro ⟨a, b⟩
      dsimp only
      rw [hfam' a b, hfam a, sum_comp']
      simp only [comp_sum', OIHierarchyGeneral.conjChannel_mul_general]
      conv_lhs => rw [Finset.sum_comm]
      simp only [Finset.sum_filter, Fintype.sum_prod_type]
      refine Finset.sum_congr rfl fun i _ => ?_
      by_cases hi : out i = a
      · simp only [hi, if_true]
        refine Finset.sum_congr rfl fun j _ => ?_
        by_cases hj : out' j = b <;> simp [hj]
      · simp [hi]
    · rw [Fintype.sum_prod_type]
      simp only [Matrix.conjTranspose_mul, ← Matrix.mulVec_mulVec]
      rw [Finset.sum_congr rfl fun i _ => by rw [← mulVec_sum', hsum' (out i)]]
      exact hsum
  | discard hm _ ih =>
    rename_i T' _ _ m O' _ _ F' _
    obtain ⟨ι, _, K, out, hfam, hsum⟩ := ih
    have hw1 := splitWeight_sum_normSq hm
    have hw2 := splitWeight_sum_star m
    refine ⟨ι × (Fin m × Fin m) × Fin 3, inferInstance,
      fun p => splitWeight m p.2.2 • ancBlock (K p.1) p.2.1.1 p.2.1.2, fun p => out p.1, ?_, ?_⟩
    · intro a
      dsimp only
      rw [hfam a, discardWith_sum]
      simp only [Finset.sum_filter, Fintype.sum_prod_type, discardWith_uniform_conjChannel,
        conjChannel_smul]
      refine Finset.sum_congr rfl fun i _ => ?_
      by_cases h : out i = a
      · simp only [h, if_true, Finset.smul_sum]
        refine Finset.sum_congr rfl fun f _ => Finset.sum_congr rfl fun e _ => ?_
        rw [← Finset.sum_smul, hw1]
      · simp [h]
    · simp only [Fintype.sum_prod_type, Matrix.conjTranspose_smul, Matrix.smul_mulVec,
        ← Finset.sum_smul, hw2]
      have hblock : ∀ e : Fin m, ∑ i, ∑ f, (ancBlock (K i) f e)ᴴ *ᵥ ones T' = ones T' := by
        intro e
        simp only [ancBlock_conjTranspose_mulVec_ones]
        funext t
        rw [Finset.sum_apply]
        have := congrFun hsum (t, e)
        rw [Finset.sum_apply] at this
        exact this
      rw [Finset.sum_congr rfl fun i _ => Finset.sum_comm, Finset.sum_comm]
      simp only [← Finset.smul_sum, hblock, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
        ← Nat.cast_smul_eq_nsmul ℂ, smul_smul]
      rw [inv_mul_cancel₀ (Nat.cast_ne_zero.mpr hm.ne' : (m : ℂ) ≠ 0), one_smul]

/-- **AN INSTRUMENT-REALIZED UNITARY CONJUGATION FIXES THE ALL-ONES VECTOR** in a ones-fixing
class: every operator of the invariant's decomposition is proportional to the unitary, and their
sum against the all-ones vector is the all-ones vector. -/
theorem instAvail_unitary_fixes_ones (hf : OnesFixing 𝓘) {T : Type} [Fintype T] [DecidableEq T]
    {U : Matrix T T ℂ} (hU : Uᴴ * U = 1)
    (h : InstAvail 𝓘 T Unit (fun _ => conjChannel U)) : ∃ z : ℂ, U *ᵥ ones T = z • ones T := by
  obtain ⟨ι, _, K, out, hfam, hsum⟩ := instAvail_onesNormal hf h
  have hK : ∑ i, conjChannel (K i) = conjChannel U := by
    have := hfam ()
    simpa using this.symm
  rcases isEmpty_or_nonempty T with hT | hT
  · exact ⟨1, Subsingleton.elim _ _⟩
  have hU0 : U ≠ 0 := by
    intro h0
    rw [h0, Matrix.mul_zero] at hU
    exact zero_ne_one hU
  choose c hc using kraus_of_conj_unitary K U hU0 hK
  have hsum' : (∑ i, star (c i)) • (Uᴴ *ᵥ ones T) = ones T := by
    calc (∑ i, star (c i)) • (Uᴴ *ᵥ ones T) = ∑ i, (K i)ᴴ *ᵥ ones T := by
          rw [Finset.sum_smul]
          exact Finset.sum_congr rfl fun i _ => by
            rw [hc i, Matrix.conjTranspose_smul, Matrix.smul_mulVec]
      _ = ones T := hsum
  set s := ∑ i, star (c i) with hs_def
  have hs : s ≠ 0 := by
    intro h0
    rw [h0, zero_smul] at hsum'
    exact one_ne_zero (congrFun hsum' (Classical.arbitrary T)).symm
  have h1 : Uᴴ *ᵥ ones T = s⁻¹ • ones T := (eq_inv_smul_iff₀ hs).mpr hsum'
  refine ⟨s, ?_⟩
  calc U *ᵥ ones T = U *ᵥ (s • (Uᴴ *ᵥ ones T)) := by
        rw [h1, smul_smul, mul_inv_cancel₀ hs, one_smul]
    _ = s • ((U * Uᴴ) *ᵥ ones T) := by rw [Matrix.mulVec_smul, Matrix.mulVec_mulVec]
    _ = s • ones T := by rw [mul_eq_one_comm.mp hU, Matrix.one_mulVec]

end Converse

/-! ### Section G — the closed-form ones-fixing class -/

section OnesClass

/-- An isometry from a carrier into a larger one that carries the all-ones vector to the
all-ones vector. -/
def OnesCompatible {R T : Type} [Fintype R] [Fintype T] [DecidableEq T] (E : Matrix R T ℂ) : Prop :=
  Eᴴ * E = 1 ∧ Eᴴ *ᵥ ones R = ones T

/-- **THE CLOSED-FORM CLASS OF THE COUNTERCONTROL**: contractive compressions `c • Eᴴ * W * F`
of unitaries `W` fixing the all-ones vector, along ones-compatible isometries `E`, `F`. It
contains every permutation matrix and every gate flow of a layer, and it is an architecture,
context-stable, label-invariant and dagger-stable, so it contains the least such class
containing them. -/
def onesClass : ImplementationClass := fun T _ _ K =>
  ∃ (c : ℂ) (R : Type) (_ : Fintype R) (_ : DecidableEq R) (W : Matrix R R ℂ) (E F : Matrix R T ℂ),
    ‖c‖ ≤ 1 ∧ Wᴴ * W = 1 ∧ W *ᵥ ones R = ones R ∧ OnesCompatible E ∧ OnesCompatible F
      ∧ K = c • (Eᴴ * W * F)

variable {T : Type} [Fintype T] [DecidableEq T]

theorem onesCompatible_one : OnesCompatible (1 : Matrix T T ℂ) :=
  ⟨by simp, by simp⟩

theorem onesCompatible_mul {R R' : Type} [Fintype R] [Fintype R'] [DecidableEq R']
    {E : Matrix R R' ℂ} {G : Matrix R' T ℂ} (hE : OnesCompatible E) (hG : OnesCompatible G) :
    OnesCompatible (E * G) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Eᴴ, hE.1, Matrix.one_mul,
      hG.1]
  · rw [Matrix.conjTranspose_mul, ← Matrix.mulVec_mulVec, hE.2, hG.2]

theorem unitary_conjTranspose_ones {R : Type} [Fintype R] [DecidableEq R] {W : Matrix R R ℂ}
    (hW : Wᴴ * W = 1) (h1 : W *ᵥ ones R = ones R) : Wᴴ *ᵥ ones R = ones R := by
  conv_lhs => rw [← h1]
  rw [Matrix.mulVec_mulVec, hW, Matrix.one_mulVec]

/-- A unitary fixing the all-ones vector is in the class. -/
theorem onesClass_of_unitary_ones {W : Matrix T T ℂ} (hW : Wᴴ * W = 1)
    (h1 : W *ᵥ ones T = ones T) : onesClass T W :=
  ⟨1, T, inferInstance, inferInstance, W, 1, 1, by simp, hW, h1, onesCompatible_one,
    onesCompatible_one, by simp⟩

theorem permMatrix_mulVec_ones (σ : Equiv.Perm T) : permMatrix σ *ᵥ ones T = ones T := by
  funext s
  simp only [Matrix.mulVec, dotProduct, ones_apply, mul_one]
  rw [Finset.sum_eq_single (σ.symm s)]
  · simp [permMatrix]
  · intro t _ ht
    have hts : σ t ≠ s := fun h => ht (by rw [← h, Equiv.symm_apply_apply])
    simp [permMatrix, hts]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem onesClass_permMatrix (σ : Equiv.Perm T) : onesClass T (permMatrix σ) :=
  onesClass_of_unitary_ones (permMatrix_isometry σ) (permMatrix_mulVec_ones σ)

/-- The gate flow of an involution fixes the all-ones vector, since its projection annihilates
it. -/
theorem gateFlow_mulVec_ones {σ : Equiv.Perm T} (hσ : ∀ x, σ (σ x) = x) (t : ℝ) :
    LiftAudit.gateFlow σ t *ᵥ ones T = ones T := by
  have hP : SecondOrderCircuit.permMat σ *ᵥ ones T = ones T := by
    funext s
    simp only [Matrix.mulVec, dotProduct, ones_apply, mul_one, SecondOrderCircuit.permMat]
    rw [Finset.sum_eq_single (σ s)]
    · simp [hσ]
    · intro t _ ht
      rw [if_neg]
      intro h
      exact ht (by rw [← h, hσ])
    · intro h
      exact absurd (Finset.mem_univ _) h
  simp only [LiftAudit.gateFlow, SecondOrderCircuit.unit, SecondOrderCircuit.proj,
    Matrix.add_mulVec, Matrix.one_mulVec, Matrix.smul_mulVec, Matrix.sub_mulVec, hP,
    sub_self, smul_zero, add_zero]

theorem onesClass_gateFlow {σ : Equiv.Perm T} (hσ : ∀ x, σ (σ x) = x) (t : ℝ) :
    onesClass T (LiftAudit.gateFlow σ t) :=
  onesClass_of_unitary_ones (LiftAudit.gateFlow_unitary hσ t) (gateFlow_mulVec_ones hσ t)

/-- The embedding of the carrier as one sector of a register. -/
def secEmb (T : Type) [DecidableEq T] (m : ℕ) (f : Fin m) : Matrix (T × Fin m) T ℂ :=
  Matrix.of fun p t => if p = (t, f) then 1 else 0

theorem onesCompatible_secEmb (m : ℕ) (f : Fin m) : OnesCompatible (secEmb T m f) := by
  refine ⟨?_, ?_⟩
  · ext s t
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, secEmb, Matrix.of_apply,
      Fintype.sum_prod_type, Matrix.one_apply, Prod.mk.injEq]
    rw [Finset.sum_eq_single s]
    · rw [Finset.sum_eq_single f]
      · simp
      · intro g _ hg
        simp [hg]
      · intro h
        exact absurd (Finset.mem_univ _) h
    · intro u _ hu
      simp [hu]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · funext t
    simp only [Matrix.mulVec, dotProduct, Matrix.conjTranspose_apply, secEmb, Matrix.of_apply,
      ones_apply, mul_one, Fintype.sum_prod_type, Prod.mk.injEq]
    rw [Finset.sum_eq_single t]
    · rw [Finset.sum_eq_single f]
      · simp
      · intro g _ hg
        simp [hg]
      · intro h
        exact absurd (Finset.mem_univ _) h
    · intro u _ hu
      simp [hu]
    · intro h
      exact absurd (Finset.mem_univ _) h

theorem ancBlock_eq_secEmb {m : ℕ} (K : Matrix (T × Fin m) (T × Fin m) ℂ) (f e : Fin m) :
    ancBlock K f e = (secEmb T m f)ᴴ * K * secEmb T m e := by
  ext s t
  simp only [ancBlock, Matrix.of_apply, Matrix.mul_apply, Matrix.conjTranspose_apply, secEmb,
    Fintype.sum_prod_type, Prod.mk.injEq]
  rw [Finset.sum_eq_single t]
  · rw [Finset.sum_eq_single e]
    · simp only [and_self, if_true, mul_one]
      rw [Finset.sum_eq_single s]
      · rw [Finset.sum_eq_single f]
        · simp
        · intro g _ hg
          simp [hg]
        · intro h
          exact absurd (Finset.mem_univ _) h
      · intro u _ hu
        simp [hu]
      · intro h
        exact absurd (Finset.mem_univ _) h
    · intro g _ hg
      simp [hg]
    · intro h
      exact absurd (Finset.mem_univ _) h
  · intro u _ hu
    simp [hu]
  · intro h
    exact absurd (Finset.mem_univ _) h

omit [Fintype T] in
theorem readProj_conjTranspose (m : ℕ) (k : Fin m) : (readProj T m k)ᴴ = readProj T m k := by
  rw [readProj, Matrix.diagonal_conjTranspose]
  congr 1
  funext r
  simp only [Pi.star_apply]
  split_ifs <;> simp

theorem readProj_mul_self (m : ℕ) (k : Fin m) : readProj T m k * readProj T m k = readProj T m k := by
  rw [readProj, Matrix.diagonal_mul_diagonal]
  congr 1
  funext r
  split_ifs <;> simp

theorem fromBlocks_diag_unitary {R₁ R₂ : Type} [Fintype R₁] [DecidableEq R₁] [Fintype R₂]
    [DecidableEq R₂] {A : Matrix R₁ R₁ ℂ} {B : Matrix R₂ R₂ ℂ} (hA : Aᴴ * A = 1) (hB : Bᴴ * B = 1) :
    (Matrix.fromBlocks A 0 0 B)ᴴ * Matrix.fromBlocks A 0 0 B = 1 := by
  rw [Matrix.fromBlocks_conjTranspose, Matrix.fromBlocks_multiply]
  simp [hA, hB, Matrix.fromBlocks_one]

theorem fromBlocks_diag_mulVec_ones {R₁ R₂ : Type} [Fintype R₁] [Fintype R₂]
    {A : Matrix R₁ R₁ ℂ} {B : Matrix R₂ R₂ ℂ} (hA : A *ᵥ ones R₁ = ones R₁)
    (hB : B *ᵥ ones R₂ = ones R₂) :
    Matrix.fromBlocks A 0 0 B *ᵥ ones (R₁ ⊕ R₂) = ones (R₁ ⊕ R₂) := by
  rw [ones_sum, Matrix.fromBlocks_mulVec]
  simp [hA, hB]

theorem onesCompatible_fromRows_left {R₁ R₂ : Type} [Fintype R₁] [Fintype R₂]
    {E : Matrix R₁ T ℂ} (hE : OnesCompatible E) :
    OnesCompatible (Matrix.fromRows E (0 : Matrix R₂ T ℂ)) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromRows,
      hE.1]
    simp
  · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, ones_sum,
      Matrix.fromCols_mulVec_sumElim, hE.2]
    simp

theorem onesCompatible_fromRows_right {R₁ R₂ : Type} [Fintype R₁] [Fintype R₂]
    {E : Matrix R₂ T ℂ} (hE : OnesCompatible E) :
    OnesCompatible (Matrix.fromRows (0 : Matrix R₁ T ℂ) E) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromRows,
      hE.1]
    simp
  · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, ones_sum,
      Matrix.fromCols_mulVec_sumElim, hE.2]
    simp

/-- **THE CLASS IS AN ARCHITECTURE.** Products are compressions of a product on the disjoint
union of the two carriers, joined by a reflection that exchanges the two embedded copies of the
system; the readout projectors are compressions of the identity along a two-copy embedding; the
blocks compose the embeddings with a sector embedding. -/
theorem onesClass_arch : Architecture onesClass where
  one := fun T _ _ => onesClass_of_unitary_ones (by simp) (Matrix.one_mulVec _)
  mul := by
    intro T _ _ K L hK hL
    obtain ⟨c₁, R₁, _, _, W₁, E₁, F₁, hc₁, hW₁, h1₁, hE₁, hF₁, rfl⟩ := hK
    obtain ⟨c₂, R₂, _, _, W₂, E₂, F₂, hc₂, hW₂, h1₂, hE₂, hF₂, rfl⟩ := hL
    set G : Matrix (R₁ ⊕ R₂) T ℂ := Matrix.fromRows F₁ (-E₂) with hG
    set S : Matrix (R₁ ⊕ R₂) (R₁ ⊕ R₂) ℂ := 1 - G * Gᴴ with hS
    have hGG : Gᴴ * G = (2 : ℂ) • (1 : Matrix T T ℂ) := by
      rw [hG, Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromRows,
        hF₁.1, Matrix.conjTranspose_neg, Matrix.neg_mul, Matrix.mul_neg, neg_neg, hE₂.1, two_smul]
    have hSH : Sᴴ = S := by
      rw [hS, Matrix.conjTranspose_sub, Matrix.conjTranspose_one, Matrix.conjTranspose_mul,
        Matrix.conjTranspose_conjTranspose]
    have hSS : Sᴴ * S = 1 := by
      rw [hSH, hS, Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub, Matrix.one_mul, Matrix.mul_one,
        Matrix.mul_assoc, ← Matrix.mul_assoc Gᴴ G, hGG, Matrix.smul_mul, Matrix.one_mul,
        Matrix.mul_smul, ← Matrix.mul_assoc, Matrix.mul_one, two_smul]
      abel
    have hS1 : S *ᵥ ones (R₁ ⊕ R₂) = ones (R₁ ⊕ R₂) := by
      have hG1 : Gᴴ *ᵥ ones (R₁ ⊕ R₂) = 0 := by
        rw [hG, Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, ones_sum,
          Matrix.fromCols_mulVec_sumElim, hF₁.2, Matrix.conjTranspose_neg, Matrix.neg_mulVec, hE₂.2,
          add_neg_cancel]
      rw [hS, Matrix.sub_mulVec, Matrix.one_mulVec, ← Matrix.mulVec_mulVec, hG1, Matrix.mulVec_zero,
        sub_zero]
    set B₁ : Matrix (R₁ ⊕ R₂) (R₁ ⊕ R₂) ℂ :=
      Matrix.fromBlocks W₁ (0 : Matrix R₁ R₂ ℂ) (0 : Matrix R₂ R₁ ℂ) (1 : Matrix R₂ R₂ ℂ) with hB₁
    set B₂ : Matrix (R₁ ⊕ R₂) (R₁ ⊕ R₂) ℂ :=
      Matrix.fromBlocks (1 : Matrix R₁ R₁ ℂ) (0 : Matrix R₁ R₂ ℂ) (0 : Matrix R₂ R₁ ℂ) W₂ with hB₂
    have hX : (Matrix.fromRows E₁ (0 : Matrix R₂ T ℂ))ᴴ * B₁
        = Matrix.fromCols (E₁ᴴ * W₁) (0 : Matrix T R₂ ℂ) := by
      rw [hB₁, Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromBlocks]
      simp
    have hY : B₂ * Matrix.fromRows (0 : Matrix R₁ T ℂ) F₂
        = Matrix.fromRows (0 : Matrix R₁ T ℂ) (W₂ * F₂) := by
      rw [hB₂, Matrix.fromBlocks_mul_fromRows]
      simp
    have hXY : Matrix.fromCols (E₁ᴴ * W₁) (0 : Matrix T R₂ ℂ)
        * Matrix.fromRows (0 : Matrix R₁ T ℂ) (W₂ * F₂) = 0 := by
      rw [Matrix.fromCols_mul_fromRows]
      simp
    have hXG : Matrix.fromCols (E₁ᴴ * W₁) (0 : Matrix T R₂ ℂ) * G = E₁ᴴ * W₁ * F₁ := by
      rw [hG, Matrix.fromCols_mul_fromRows]
      simp
    have hGY : Gᴴ * Matrix.fromRows (0 : Matrix R₁ T ℂ) (W₂ * F₂) = -(E₂ᴴ * (W₂ * F₂)) := by
      rw [hG, Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromRows]
      simp
    refine ⟨c₁ * c₂, R₁ ⊕ R₂, inferInstance, inferInstance, B₁ * S * B₂,
      Matrix.fromRows E₁ (0 : Matrix R₂ T ℂ), Matrix.fromRows (0 : Matrix R₁ T ℂ) F₂, ?_, ?_, ?_,
      onesCompatible_fromRows_left hE₁, onesCompatible_fromRows_right hF₂, ?_⟩
    · rw [norm_mul]
      exact mul_le_one₀ hc₁ (norm_nonneg _) hc₂
    · have hB₁u : B₁ᴴ * B₁ = 1 := fromBlocks_diag_unitary hW₁ (by simp)
      have hB₂u : B₂ᴴ * B₂ = 1 := fromBlocks_diag_unitary (by simp) hW₂
      calc (B₁ * S * B₂)ᴴ * (B₁ * S * B₂) = B₂ᴴ * (Sᴴ * ((B₁ᴴ * B₁) * (S * B₂))) := by
            simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]
        _ = 1 := by rw [hB₁u, Matrix.one_mul, ← Matrix.mul_assoc Sᴴ, hSS, Matrix.one_mul, hB₂u]
    · have hB₁1 : B₁ *ᵥ ones (R₁ ⊕ R₂) = ones (R₁ ⊕ R₂) :=
        fromBlocks_diag_mulVec_ones h1₁ (Matrix.one_mulVec _)
      have hB₂1 : B₂ *ᵥ ones (R₁ ⊕ R₂) = ones (R₁ ⊕ R₂) :=
        fromBlocks_diag_mulVec_ones (Matrix.one_mulVec _) h1₂
      rw [← Matrix.mulVec_mulVec, ← Matrix.mulVec_mulVec, hB₂1, hS1, hB₁1]
    · have key : (Matrix.fromRows E₁ (0 : Matrix R₂ T ℂ))ᴴ * (B₁ * S * B₂)
          * Matrix.fromRows (0 : Matrix R₁ T ℂ) F₂
          = E₁ᴴ * W₁ * F₁ * (E₂ᴴ * W₂ * F₂) := by
        have e1 : (Matrix.fromRows E₁ (0 : Matrix R₂ T ℂ))ᴴ * (B₁ * S * B₂)
            * Matrix.fromRows (0 : Matrix R₁ T ℂ) F₂
            = Matrix.fromCols (E₁ᴴ * W₁) (0 : Matrix T R₂ ℂ) * S
              * Matrix.fromRows (0 : Matrix R₁ T ℂ) (W₂ * F₂) := by
          rw [← hX, ← hY]
          simp only [Matrix.mul_assoc]
        rw [e1, hS, Matrix.mul_sub, Matrix.mul_one, Matrix.sub_mul, hXY,
          ← Matrix.mul_assoc (Matrix.fromCols (E₁ᴴ * W₁) (0 : Matrix T R₂ ℂ)) G Gᴴ, hXG,
          Matrix.mul_assoc, hGY, Matrix.mul_neg, zero_sub, neg_neg]
        simp only [Matrix.mul_assoc]
      rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, key]
  smul := by
    intro T _ _ a K ha hK
    obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
    refine ⟨a * c, R, inferInstance, inferInstance, W, E, F, ?_, hW, h1, hE, hF, by rw [smul_smul]⟩
    rw [norm_mul]
    exact mul_le_one₀ ha (norm_nonneg _) hc
  proj := by
    intro T _ _ m k
    show onesClass _ (readProj T m k)
    refine ⟨1, (T × Fin m) ⊕ (T × Fin m), inferInstance, inferInstance, 1,
      Matrix.fromRows (readProj T m k) (1 - readProj T m k), Matrix.fromRows 1 0, by simp,
      by simp, Matrix.one_mulVec _, ?_, onesCompatible_fromRows_left onesCompatible_one, ?_⟩
    · refine ⟨?_, ?_⟩
      · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, Matrix.fromCols_mul_fromRows,
          readProj_conjTranspose, Matrix.conjTranspose_sub, Matrix.conjTranspose_one,
          readProj_conjTranspose, readProj_mul_self, Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub]
        simp only [Matrix.one_mul, Matrix.mul_one, readProj_mul_self]
        abel
      · rw [Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose, ones_sum,
          Matrix.fromCols_mulVec_sumElim, readProj_conjTranspose, Matrix.conjTranspose_sub,
          Matrix.conjTranspose_one, readProj_conjTranspose, Matrix.sub_mulVec, Matrix.one_mulVec]
        abel
    · rw [one_smul, Matrix.mul_one, Matrix.conjTranspose_fromRows_eq_fromCols_conjTranspose,
        Matrix.fromCols_mul_fromRows, readProj_conjTranspose]
      simp
  block := by
    intro T _ _ m K f e hK
    obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
    refine ⟨c, R, inferInstance, inferInstance, W, E * secEmb T m f, F * secEmb T m e, hc, hW, h1,
      onesCompatible_mul hE (onesCompatible_secEmb m f),
      onesCompatible_mul hF (onesCompatible_secEmb m e), ?_⟩
    rw [ancBlock_smul, ancBlock_eq_secEmb]
    simp only [Matrix.conjTranspose_mul, Matrix.mul_assoc]

/-- The rectangular tensor product with a square factor on the left. -/
def tensorRect {R₁ R₂ R T : Type} (A : Matrix R₁ R₂ ℂ) (E : Matrix R T ℂ) :
    Matrix (R₁ × R) (R₂ × T) ℂ :=
  Matrix.of fun p q => A p.1 q.1 * E p.2 q.2

theorem tensorOf_eq_tensorRect {R S : Type} (A : Matrix R R ℂ) (K : Matrix S S ℂ) :
    tensorOf A K = tensorRect A K := rfl

theorem tensorRect_mul {R₁ R₂ R₃ R T T₂ : Type} [Fintype R₂] [Fintype T]
    (A : Matrix R₁ R₂ ℂ) (B : Matrix R₂ R₃ ℂ) (E : Matrix R T ℂ) (G : Matrix T T₂ ℂ) :
    tensorRect A E * tensorRect B G = tensorRect (A * B) (E * G) := by
  ext p q
  simp only [Matrix.mul_apply, tensorRect, Matrix.of_apply, Fintype.sum_prod_type,
    Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
  ring

theorem tensorRect_conjTranspose {R₁ R₂ R T : Type} (A : Matrix R₁ R₂ ℂ) (E : Matrix R T ℂ) :
    (tensorRect A E)ᴴ = tensorRect Aᴴ Eᴴ := by
  ext p q
  simp [tensorRect, Matrix.conjTranspose_apply]

theorem tensorRect_smul {R₁ R₂ R T : Type} (c : ℂ) (A : Matrix R₁ R₂ ℂ) (E : Matrix R T ℂ) :
    tensorRect A (c • E) = c • tensorRect A E := by
  ext p q
  simp [tensorRect, mul_left_comm]

theorem tensorRect_mulVec_ones {R₁ R₂ R T : Type} [Fintype R₂] [Fintype T] (A : Matrix R₁ R₂ ℂ)
    (E : Matrix R T ℂ) :
    tensorRect A E *ᵥ ones (R₂ × T) = fun p => (A *ᵥ ones R₂) p.1 * (E *ᵥ ones T) p.2 := by
  funext p
  simp only [Matrix.mulVec, dotProduct, tensorRect, Matrix.of_apply, ones_apply, mul_one,
    Fintype.sum_prod_type, Finset.sum_mul_sum]

theorem onesCompatible_tensorRect_one {R₁ R : Type} [Fintype R₁] [DecidableEq R₁] [Fintype R]
    {E : Matrix R T ℂ} (hE : OnesCompatible E) :
    OnesCompatible (tensorRect (1 : Matrix R₁ R₁ ℂ) E) := by
  refine ⟨?_, ?_⟩
  · rw [tensorRect_conjTranspose, tensorRect_mul, Matrix.conjTranspose_one, Matrix.one_mul, hE.1,
      ← tensorOf_eq_tensorRect, tensorOf_one_one]
  · rw [tensorRect_conjTranspose, tensorRect_mulVec_ones, Matrix.conjTranspose_one,
      Matrix.one_mulVec, hE.2, ones_prod]

theorem onesClass_contextStable : ContextStable onesClass := by
  intro R₁ S _ _ _ _ K hK
  obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
  refine ⟨c, R₁ × R, inferInstance, inferInstance, tensorRect 1 W, tensorRect 1 E, tensorRect 1 F,
    hc, ?_, ?_, onesCompatible_tensorRect_one hE, onesCompatible_tensorRect_one hF, ?_⟩
  · rw [tensorRect_conjTranspose, tensorRect_mul, Matrix.conjTranspose_one, Matrix.one_mul, hW,
      ← tensorOf_eq_tensorRect, tensorOf_one_one]
  · rw [tensorRect_mulVec_ones, Matrix.one_mulVec, h1, ones_prod]
  · rw [tensorOf_eq_tensorRect, tensorRect_smul, tensorRect_conjTranspose, tensorRect_mul,
      tensorRect_mul, Matrix.conjTranspose_one, Matrix.one_mul, Matrix.one_mul]

omit [Fintype T] [DecidableEq T] in
theorem reindex_left_conjTranspose_mulVec {R T₂ : Type} [Fintype R] [Fintype T₂] (E : Matrix R T ℂ)
    (e : T ≃ T₂) (v : R → ℂ) :
    (Matrix.reindex (Equiv.refl R) e E)ᴴ *ᵥ v = fun t' => (Eᴴ *ᵥ v) (e.symm t') := by
  funext t'
  simp [Matrix.mulVec, dotProduct, Matrix.reindex_apply, Matrix.submatrix_apply,
    Matrix.conjTranspose_apply]

theorem onesCompatible_reindex_left {R T₂ : Type} [Fintype R] [Fintype T₂] [DecidableEq T₂]
    {E : Matrix R T ℂ} (hE : OnesCompatible E) (e : T ≃ T₂) :
    OnesCompatible (Matrix.reindex (Equiv.refl R) e E) := by
  refine ⟨?_, ?_⟩
  · rw [Matrix.reindex_apply, Matrix.conjTranspose_submatrix, Matrix.submatrix_mul_equiv, hE.1,
      Matrix.submatrix_one_equiv]
  · rw [reindex_left_conjTranspose_mulVec, hE.2]
    rfl

theorem onesClass_labelInvariant : LabelInvariant onesClass := by
  intro S S' _ _ _ _ e K hK
  obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
  refine ⟨c, R, inferInstance, inferInstance, W, Matrix.reindex (Equiv.refl R) e E,
    Matrix.reindex (Equiv.refl R) e F, hc, hW, h1, onesCompatible_reindex_left hE e,
    onesCompatible_reindex_left hF e, ?_⟩
  ext s t
  simp [Matrix.reindex_apply, Matrix.submatrix_apply, Matrix.mul_apply, Matrix.conjTranspose_apply]

theorem onesClass_daggerStable : DaggerStable onesClass := by
  intro S _ _ K hK
  obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
  refine ⟨star c, R, inferInstance, inferInstance, Wᴴ, F, E, by simpa using hc, ?_,
    unitary_conjTranspose_ones hW h1, hF, hE, ?_⟩
  · rw [Matrix.conjTranspose_conjTranspose]
    exact mul_eq_one_comm.mp hW
  · rw [Matrix.conjTranspose_smul, Matrix.conjTranspose_mul, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, Matrix.mul_assoc]

/-- **AN ISOMETRIC COMPRESSION OF A ONES-FIXING UNITARY FIXES THE ALL-ONES VECTOR.** The
defect `(1 − E Eᴴ) W F` has `Vᴴ V + Mᴴ M = 1`; contractivity of the scalar together with the
isometry forces the scalar to have modulus one and the defect to vanish, so `W F = E V`, and
then `Vᴴ` carries the all-ones vector to itself through the two embeddings. -/
theorem isometry_fixes_ones : OnesFixing onesClass := by
  intro T _ _ K hK hiso
  obtain ⟨c, R, _, _, W, E, F, hc, hW, h1, hE, hF, rfl⟩ := hK
  rcases isEmpty_or_nonempty T with hT | hT
  · exact ⟨1, Subsingleton.elim _ _⟩
  set V := Eᴴ * W * F with hV
  set M := (1 - E * Eᴴ) * W * F with hM
  have hP : (1 - E * Eᴴ)ᴴ * (1 - E * Eᴴ) = 1 - E * Eᴴ := by
    rw [Matrix.conjTranspose_sub, Matrix.conjTranspose_one, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub,
      Matrix.one_mul, Matrix.mul_one, Matrix.mul_assoc, ← Matrix.mul_assoc Eᴴ E, hE.1,
      Matrix.one_mul, Matrix.one_mul]
    abel
  have hVM : Vᴴ * V + Mᴴ * M = 1 := by
    have e1 : Vᴴ * V = Fᴴ * (Wᴴ * ((E * Eᴴ) * (W * F))) := by
      simp only [hV, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose, Matrix.mul_assoc]
    have e2 : Mᴴ * M = Fᴴ * (Wᴴ * ((1 - E * Eᴴ) * (W * F))) := by
      simp only [hM, Matrix.conjTranspose_mul, Matrix.mul_assoc]
      rw [← Matrix.mul_assoc (1 - E * Eᴴ)ᴴ (1 - E * Eᴴ), hP]
    rw [e1, e2, ← Matrix.mul_add, ← Matrix.mul_add, ← Matrix.add_mul, add_sub_cancel,
      Matrix.one_mul, ← Matrix.mul_assoc Wᴴ, hW, Matrix.one_mul, hF.1]
  have hc0 : c ≠ 0 := by
    rintro rfl
    rw [zero_smul, Matrix.mul_zero] at hiso
    have := congrFun (congrFun hiso (Classical.arbitrary T)) (Classical.arbitrary T)
    simp at this
  set a : ℝ := Complex.normSq c with ha_def
  have hsc : star c * c = (a : ℂ) := by rw [ha_def, Complex.normSq_eq_conj_mul_self]; rfl
  have ha0 : 0 < a := Complex.normSq_pos.mpr hc0
  have ha1 : a ≤ 1 := by
    rw [ha_def, Complex.normSq_eq_norm_sq]
    exact pow_le_one₀ (norm_nonneg c) hc
  have hK' : (a : ℂ) • (Vᴴ * V) = 1 := by
    rw [← hsc, ← hiso, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  have hVV : Vᴴ * V = ((a⁻¹ : ℝ) : ℂ) • (1 : Matrix T T ℂ) := by
    rw [← hK', smul_smul, Complex.ofReal_inv, inv_mul_cancel₀ (Complex.ofReal_ne_zero.mpr ha0.ne'),
      one_smul]
  have hMM : Mᴴ * M = ((1 - a⁻¹ : ℝ) : ℂ) • (1 : Matrix T T ℂ) := by
    rw [← sub_eq_of_eq_add' hVM.symm, hVV, Complex.ofReal_sub, Complex.ofReal_one, sub_smul,
      one_smul]
  have hpsd := Matrix.posSemidef_conjTranspose_mul_self M
  have hdiag := hpsd.diag_nonneg (i := Classical.arbitrary T)
  rw [hMM, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one, Complex.zero_le_real]
    at hdiag
  have hainv : a⁻¹ ≤ 1 := by linarith
  have ha : a = 1 := le_antisymm ha1 ((inv_le_one₀ ha0).mp hainv)
  have hM0 : M = 0 := by
    rw [← Matrix.conjTranspose_mul_self_eq_zero, hMM, ha, inv_one, sub_self, Complex.ofReal_zero,
      zero_smul]
  have hVu : Vᴴ * V = 1 := by rw [hVV, ha, inv_one, Complex.ofReal_one, one_smul]
  have hWF : W * F = E * V := by
    have h0 : (1 - E * Eᴴ) * (W * F) = 0 := by rw [← Matrix.mul_assoc, ← hM, hM0]
    rw [Matrix.sub_mul, Matrix.one_mul, sub_eq_zero] at h0
    rw [h0, hV, Matrix.mul_assoc, Matrix.mul_assoc]
  have hV1 : Vᴴ *ᵥ ones T = ones T := by
    have h2 : Vᴴ * Eᴴ = Fᴴ * Wᴴ := by
      rw [← Matrix.conjTranspose_mul, ← hWF, Matrix.conjTranspose_mul]
    conv_lhs => rw [← hE.2]
    rw [Matrix.mulVec_mulVec, h2, ← Matrix.mulVec_mulVec, unitary_conjTranspose_ones hW h1, hF.2]
  refine ⟨c, ?_⟩
  rw [Matrix.smul_mulVec]
  congr 1
  conv_lhs => rw [← hV1]
  rw [Matrix.mulVec_mulVec, mul_eq_one_comm.mp hVu, Matrix.one_mulVec]

end OnesClass

/-! ### Section H — the countercontrol -/

section Witness

variable {T : Type} [Fintype T] [DecidableEq T]

omit [Fintype T] in
theorem pairProj_eq_diagonal {a b : T} (hab : a ≠ b) :
    LiftAudit.pairProj a b = Matrix.diagonal fun s => if s = a ∨ s = b then (1 : ℂ) else 0 := by
  ext i j
  simp only [LiftAudit.pairProj, Matrix.add_apply, Matrix.single_apply, Matrix.diagonal_apply]
  by_cases hij : i = j
  · subst hij
    by_cases ha : a = i
    · subst ha
      simp [hab, hab.symm]
    · by_cases hb : b = i
      · subst hb
        simp [ha, Ne.symm ha]
      · simp [ha, hb, Ne.symm ha, Ne.symm hb]
  · have h1 : ¬ (a = i ∧ a = j) := fun h => hij (h.1.symm.trans h.2)
    have h2 : ¬ (b = i ∧ b = j) := fun h => hij (h.1.symm.trans h.2)
    simp [hij, h1, h2]

/-- The indicator of the pair. -/
def pairInd (a b : T) : T → ℂ := fun s => if s = a ∨ s = b then 1 else 0

theorem pairProj_mulVec_ones {a b : T} (hab : a ≠ b) :
    LiftAudit.pairProj a b *ᵥ ones T = pairInd a b := by
  funext s
  rw [pairProj_eq_diagonal hab, Matrix.mulVec_diagonal, ones_apply, mul_one]
  rfl

theorem transition_mulVec_ones {a b : T} (hab : a ≠ b) :
    transition a b *ᵥ ones T = pairInd a b := by
  funext s
  simp only [Matrix.mulVec, dotProduct, transition, Matrix.add_apply, Matrix.single_apply, ones_apply,
    mul_one, Finset.sum_add_distrib, pairInd]
  by_cases ha : s = a
  · subst ha
    simp [hab, Ne.symm hab]
  · by_cases hb : s = b
    · subst hb
      simp [ha, Ne.symm ha]
    · simp [ha, hb, Ne.symm ha, Ne.symm hb]

omit [Fintype T] in
theorem pairProj_conjTranspose {a b : T} (hab : a ≠ b) :
    (LiftAudit.pairProj a b)ᴴ = LiftAudit.pairProj a b := by
  rw [pairProj_eq_diagonal hab, Matrix.diagonal_conjTranspose]
  congr 1
  funext s
  simp only [Pi.star_apply]
  split_ifs <;> simp

/-- The transition flow acts as the identity off the pair. -/
theorem flow_mul_one_sub_pairProj {a b : T} (hab : a ≠ b) (t : ℝ) :
    ReachabilitySeam.flow (transition a b) t * (1 - LiftAudit.pairProj a b)
      = 1 - LiftAudit.pairProj a b := by
  rw [LiftAudit.flow_transition_closedForm hab, Matrix.mul_sub, Matrix.mul_one, Matrix.sub_mul,
    Matrix.add_mul, Matrix.one_mul, Matrix.smul_mul, Matrix.smul_mul,
    LiftAudit.pairProj_mul_pairProj hab, LiftAudit.transition_mul_pairProj hab]
  abel

theorem flow_mul_pairProj {a b : T} (hab : a ≠ b) (t : ℝ) :
    ReachabilitySeam.flow (transition a b) t * LiftAudit.pairProj a b
      = (Real.cos t : ℂ) • LiftAudit.pairProj a b
        - ((Real.sin t : ℂ) * Complex.I) • transition a b := by
  rw [LiftAudit.flow_transition_closedForm hab, Matrix.sub_mul, Matrix.add_mul, Matrix.one_mul,
    Matrix.smul_mul, Matrix.smul_mul, LiftAudit.pairProj_mul_pairProj hab,
    LiftAudit.transition_mul_pairProj hab, sub_smul, one_smul]
  abel

/-- The phased flow `e^{it} U P + (1 − P)`: unitary, fixing the all-ones vector. -/
noncomputable def pairPhase (a b : T) (t : ℝ) : Matrix T T ℂ :=
  Complex.exp (t * Complex.I) • (ReachabilitySeam.flow (transition a b) t * LiftAudit.pairProj a b)
    + (1 - LiftAudit.pairProj a b)

theorem exp_star_mul_self (t : ℝ) :
    star (Complex.exp (t * Complex.I)) * Complex.exp (t * Complex.I) = 1 := by
  rw [Complex.star_def, Complex.conj_mul', Complex.norm_exp_ofReal_mul_I]
  simp

theorem exp_ofReal_mul_I_eq (t : ℝ) :
    Complex.exp (t * Complex.I) = (Real.cos t : ℂ) + (Real.sin t : ℂ) * Complex.I := by
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]

theorem star_exp_ofReal_mul_I (t : ℝ) :
    star (Complex.exp (t * Complex.I)) = (Real.cos t : ℂ) - (Real.sin t : ℂ) * Complex.I := by
  rw [exp_ofReal_mul_I_eq, Complex.star_def, map_add, map_mul, Complex.conj_ofReal,
    Complex.conj_ofReal, Complex.conj_I]
  ring

theorem pairPhase_isometry {a b : T} (hab : a ≠ b) (t : ℝ) :
    (pairPhase a b t)ᴴ * pairPhase a b t = 1 := by
  set U := ReachabilitySeam.flow (transition a b) t with hU
  set P := LiftAudit.pairProj a b with hPdef
  have hUU : Uᴴ * U = 1 := OIHierarchy.flow_isometry _ (transition_hermitian a b) t
  have hPP : P * P = P := LiftAudit.pairProj_mul_pairProj hab
  have hPH : Pᴴ = P := pairProj_conjTranspose hab
  have hU1 : U * (1 - P) = 1 - P := flow_mul_one_sub_pairProj hab t
  have hUd1 : Uᴴ * (1 - P) = 1 - P := by
    conv_lhs => rw [← hU1]
    rw [← Matrix.mul_assoc, hUU, Matrix.one_mul]
  have h1U : (1 - P) * U = 1 - P := by
    have h := congrArg Matrix.conjTranspose hUd1
    rwa [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose, Matrix.conjTranspose_sub,
      Matrix.conjTranspose_one, hPH] at h
  have hP1 : P * (1 - P) = 0 := by rw [Matrix.mul_sub, Matrix.mul_one, hPP, sub_self]
  have h1P : (1 - P) * P = 0 := by rw [Matrix.sub_mul, Matrix.one_mul, hPP, sub_self]
  have h11 : (1 - P) * (1 - P) = 1 - P := by rw [Matrix.mul_sub, Matrix.mul_one, h1P, sub_zero]
  set q := Complex.exp (t * Complex.I) with hq_def
  have hq' : q * star q = 1 := by rw [mul_comm]; exact exp_star_mul_self t
  simp only [pairPhase, ← hU, ← hPdef, ← hq_def, Matrix.conjTranspose_add, Matrix.conjTranspose_smul,
    Matrix.conjTranspose_mul, hPH, Matrix.conjTranspose_sub, Matrix.conjTranspose_one,
    Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul]
  rw [show P * Uᴴ * (U * P) = P from by
      rw [Matrix.mul_assoc, ← Matrix.mul_assoc Uᴴ, hUU, Matrix.one_mul, hPP],
    show P * Uᴴ * (1 - P) = 0 from by rw [Matrix.mul_assoc, hUd1, hP1],
    show (1 - P) * (U * P) = 0 from by rw [← Matrix.mul_assoc, h1U, h1P], h11]
  simp only [smul_zero, add_zero, zero_add, smul_smul, hq', one_smul]
  abel

theorem pairPhase_mulVec_ones {a b : T} (hab : a ≠ b) (t : ℝ) :
    pairPhase a b t *ᵥ ones T = ones T := by
  rw [pairPhase, Matrix.add_mulVec, Matrix.smul_mulVec, ← Matrix.mulVec_mulVec,
    pairProj_mulVec_ones hab, Matrix.sub_mulVec, Matrix.one_mulVec, pairProj_mulVec_ones hab]
  have hUP : ReachabilitySeam.flow (transition a b) t *ᵥ pairInd a b
      = star (Complex.exp (t * Complex.I)) • pairInd a b := by
    rw [← pairProj_mulVec_ones hab, Matrix.mulVec_mulVec, flow_mul_pairProj hab, Matrix.sub_mulVec,
      Matrix.smul_mulVec, Matrix.smul_mulVec, pairProj_mulVec_ones hab,
      transition_mulVec_ones hab, star_exp_ofReal_mul_I, sub_smul]
  rw [hUP, smul_smul, mul_comm, exp_star_mul_self, one_smul]
  abel

/-- The phase on each configuration: `e^{−it}` on the pair, `e^{it}` elsewhere. -/
noncomputable def pairPhaseOf (a b : T) (t : ℝ) (s : T) : ℂ :=
  if s = a ∨ s = b then star (Complex.exp (t * Complex.I)) else Complex.exp (t * Complex.I)

omit [Fintype T] in
theorem pairPhaseOf_star_mul_self (a b : T) (t : ℝ) (s : T) :
    star (pairPhaseOf a b t s) * pairPhaseOf a b t s = 1 := by
  unfold pairPhaseOf
  split_ifs
  · rw [star_star, mul_comm]
    exact exp_star_mul_self t
  · exact exp_star_mul_self t

/-- The two-level gate on each configuration, a `2 × 2` block with diagonal `(1 + φ)/2` and
off-diagonal `(1 − φ)/2`. -/
noncomputable def levelGate (φ : T → ℂ) : Matrix (T × Fin 2) (T × Fin 2) ℂ :=
  Matrix.of fun p q =>
    if p.1 = q.1 then (if p.2 = q.2 then (1 + φ p.1) / 2 else (1 - φ p.1) / 2) else 0

theorem levelGate_isometry {φ : T → ℂ} (hφ : ∀ s, star (φ s) * φ s = 1) :
    (levelGate φ)ᴴ * levelGate φ = 1 := by
  ext ⟨s, i⟩ ⟨t, j⟩
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, levelGate, Matrix.of_apply,
    Fintype.sum_prod_type, Matrix.one_apply, Prod.mk.injEq]
  rw [Finset.sum_eq_single s]
  · by_cases hst : s = t
    · subst hst
      simp only [if_true, true_and, Fin.sum_univ_two]
      have h' : φ s * star (φ s) = 1 := by rw [mul_comm]; exact hφ s
      have h'' : (starRingEnd ℂ) (φ s) * φ s = 1 := hφ s
      fin_cases i <;> fin_cases j <;> simp <;>
        first
        | linear_combination (1 / 2 : ℂ) * h''
        | linear_combination (-1 / 2 : ℂ) * h''
    · simp [hst]
  · intro u _ hu
    simp [hu]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem levelGate_mulVec_ones (φ : T → ℂ) : levelGate φ *ᵥ ones (T × Fin 2) = ones (T × Fin 2) := by
  funext ⟨s, i⟩
  simp only [Matrix.mulVec, dotProduct, levelGate, Matrix.of_apply, ones_apply, mul_one,
    Fintype.sum_prod_type]
  rw [Finset.sum_eq_single s]
  · fin_cases i <;> simp [Fin.sum_univ_two] <;> ring
  · intro u _ hu
    simp [Ne.symm hu]
  · intro h
    exact absurd (Finset.mem_univ _) h

omit [Fintype T] in
theorem levelGate_ancBlock (φ : T → ℂ) :
    ancBlock (levelGate φ) 0 0 = Matrix.diagonal fun s => (1 + φ s) / 2 := by
  ext s t
  simp only [ancBlock, Matrix.of_apply, levelGate, Matrix.diagonal_apply]
  by_cases h : s = t <;> simp [h]

theorem secEmb_conjTranspose_mul_tensorOf (V : Matrix T T ℂ) (m : ℕ) (f : Fin m) :
    (secEmb T m f)ᴴ * tensorOf V (1 : Matrix (Fin m) (Fin m) ℂ) = V * (secEmb T m f)ᴴ := by
  ext s q
  rw [Matrix.mul_apply, Matrix.mul_apply, Finset.sum_eq_single (s, f), Finset.sum_eq_single q.1]
  · by_cases h : q.2 = f
    · simp [secEmb, Matrix.conjTranspose_apply, Matrix.one_apply, h, Prod.ext_iff]
    · simp [secEmb, Matrix.conjTranspose_apply, h, Ne.symm h, Prod.ext_iff]
  · intro u _ hu
    have : q ≠ (u, f) := fun h => hu (by rw [h])
    simp [secEmb, Matrix.conjTranspose_apply, this]
  · intro h
    exact absurd (Finset.mem_univ _) h
  · intro p _ hp
    simp [secEmb, Matrix.conjTranspose_apply, hp]
  · intro h
    exact absurd (Finset.mem_univ _) h

omit [Fintype T] in
theorem diagonal_pairPhase_eq {a b : T} (hab : a ≠ b) (t : ℝ) :
    (Matrix.diagonal fun s => (1 + pairPhaseOf a b t s) / 2)
      = ((1 + star (Complex.exp (t * Complex.I))) / 2) • LiftAudit.pairProj a b
        + ((1 + Complex.exp (t * Complex.I)) / 2) • (1 - LiftAudit.pairProj a b) := by
  rw [pairProj_eq_diagonal hab, ← Matrix.diagonal_one, Matrix.diagonal_sub, ← Matrix.diagonal_smul,
    ← Matrix.diagonal_smul, Matrix.diagonal_add]
  congr 1
  funext s
  simp only [pairPhaseOf, Pi.smul_apply, smul_eq_mul]
  split_ifs <;> ring

/-- **THE GADGET BLOCK**: the level-zero block of the phased flow tensored with the identity,
followed by the two-level gate, is the transition flow scaled by `(1 + e^{it})/2`. -/
theorem gadget_block {a b : T} (hab : a ≠ b) (t : ℝ) :
    ancBlock (tensorOf (pairPhase a b t) (1 : Matrix (Fin 2) (Fin 2) ℂ)
        * levelGate (pairPhaseOf a b t)) 0 0
      = ((1 + Complex.exp (t * Complex.I)) / 2) • ReachabilitySeam.flow (transition a b) t := by
  set U := ReachabilitySeam.flow (transition a b) t with hU
  set P := LiftAudit.pairProj a b with hPdef
  set q := Complex.exp (t * Complex.I) with hq_def
  have hq : star q * q = 1 := exp_star_mul_self t
  have hPP : P * P = P := LiftAudit.pairProj_mul_pairProj hab
  have hU1 : U * (1 - P) = 1 - P := flow_mul_one_sub_pairProj hab t
  have hP1 : P * (1 - P) = 0 := by rw [Matrix.mul_sub, Matrix.mul_one, hPP, sub_self]
  have h1P : (1 - P) * P = 0 := by rw [Matrix.sub_mul, Matrix.one_mul, hPP, sub_self]
  have h11 : (1 - P) * (1 - P) = 1 - P := by rw [Matrix.mul_sub, Matrix.mul_one, h1P, sub_zero]
  rw [ancBlock_eq_secEmb, ← Matrix.mul_assoc, secEmb_conjTranspose_mul_tensorOf, Matrix.mul_assoc,
    Matrix.mul_assoc, ← Matrix.mul_assoc (secEmb T 2 0)ᴴ, ← ancBlock_eq_secEmb, levelGate_ancBlock,
    diagonal_pairPhase_eq hab, pairPhase, ← hU, ← hPdef, ← hq_def]
  simp only [Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul]
  rw [Matrix.mul_assoc U P P, hPP, Matrix.mul_assoc U P (1 - P), hP1, h1P, h11, Matrix.mul_zero]
  simp only [smul_zero, add_zero, zero_add, smul_smul]
  have hqq : (1 + star q) / 2 * q = (1 + q) / 2 := by
    linear_combination (1 / 2 : ℂ) * hq
  rw [hqq, ← smul_add, ← hU1, ← Matrix.mul_add, add_sub_cancel, Matrix.mul_one]

/-- **A CONTRACTIVE MULTIPLE OF THE TRANSITION FLOW LIES IN THE CLASS**: it is the level-zero
block of a product of two ones-fixing unitaries on the doubled carrier. -/
theorem transition_scaled_mem_onesClass {a b : T} (hab : a ≠ b) (t : ℝ) :
    onesClass T (((1 + Complex.exp (t * Complex.I)) / 2)
      • ReachabilitySeam.flow (transition a b) t) := by
  rw [← gadget_block hab t]
  refine onesClass_arch.block T 2 _ 0 0 (onesClass_arch.mul _ _ _ ?_ ?_)
  · refine onesClass_of_unitary_ones ?_ ?_
    · rw [tensorOf_conjTranspose, tensorOf_mul', pairPhase_isometry hab t, Matrix.conjTranspose_one,
        Matrix.one_mul, tensorOf_one_one]
    · rw [tensorOf_eq_tensorRect, tensorRect_mulVec_ones, pairPhase_mulVec_ones hab,
        Matrix.one_mulVec, ones_prod]
  · exact onesClass_of_unitary_ones (levelGate_isometry (pairPhaseOf_star_mul_self a b t))
      (levelGate_mulVec_ones _)

theorem flow_mulVec_ones_apply {a b : T} (hab : a ≠ b) (t : ℝ) (s : T) :
    (ReachabilitySeam.flow (transition a b) t *ᵥ ones T) s
      = if s = a ∨ s = b then (Real.cos t : ℂ) - (Real.sin t : ℂ) * Complex.I else 1 := by
  rw [LiftAudit.flow_transition_closedForm hab, Matrix.sub_mulVec, Matrix.add_mulVec,
    Matrix.smul_mulVec, Matrix.smul_mulVec, Matrix.one_mulVec, pairProj_mulVec_ones hab,
    transition_mulVec_ones hab]
  simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, ones_apply, pairInd, smul_eq_mul]
  split_ifs <;> ring

/-- **T2, THE COUNTERCONTROL.** On a carrier with a third point, the conjugation by the
transition flow at a quarter turn is branch-realized by the ones-fixing class with the trace
preserved, by two contractive copies of the gadget block, and is not instrument-realized by it:
every instrument-realized unitary conjugation of the class fixes the all-ones vector, and the
transition flow moves it. Provenance removes the replication. -/
theorem flow_realized_not_instrumentRealized {a b c : T} (hab : a ≠ b) (hca : c ≠ a) (hcb : c ≠ b) :
    IsGenInstrument onesClass T
        (fun _ : Unit => conjChannel (ReachabilitySeam.flow (transition a b) (Real.pi / 2)))
    ∧ ¬ InstAvail onesClass T Unit
        (fun _ => conjChannel (ReachabilitySeam.flow (transition a b) (Real.pi / 2))) := by
  set U := ReachabilitySeam.flow (transition a b) (Real.pi / 2) with hU
  have hUU : Uᴴ * U = 1 := OIHierarchy.flow_isometry _ (transition_hermitian a b) _
  set q := Complex.exp ((Real.pi / 2 : ℝ) * Complex.I) with hq_def
  have hqI : q = Complex.I := by
    rw [hq_def, exp_ofReal_mul_I_eq, Real.cos_pi_div_two, Real.sin_pi_div_two]
    simp
  have hmem : onesClass T (((1 + q) / 2) • U) := transition_scaled_mem_onesClass hab _
  have hmem' : onesClass T ((-Complex.I * ((1 + q) / 2)) • U) := by
    rw [← smul_smul]
    exact onesClass_arch.smul T _ _ (by simp) hmem
  refine ⟨⟨fun _ => ⟨Fin 2, inferInstance,
    ![((1 + q) / 2) • U, (-Complex.I * ((1 + q) / 2)) • U], ?_, ?_⟩,
    fun X => by rw [Fintype.sum_unique]; exact conjChannel_trace U hUU X⟩, ?_⟩
  · rw [Fin.sum_univ_two]
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, conjChannel_smul]
    rw [← add_smul, hqI]
    have h2 : (1 + Complex.I) / 2 * star ((1 + Complex.I) / 2)
        + -Complex.I * ((1 + Complex.I) / 2) * star (-Complex.I * ((1 + Complex.I) / 2)) = 1 := by
      apply Complex.ext <;> simp <;> norm_num
    rw [h2, one_smul]
  · intro i
    fin_cases i
    · exact hmem
    · exact hmem'
  · intro h
    obtain ⟨z, hz⟩ := instAvail_unitary_fixes_ones isometry_fixes_ones hUU h
    have hc := congrFun hz c
    have ha := congrFun hz a
    rw [flow_mulVec_ones_apply hab, Pi.smul_apply, ones_apply, smul_eq_mul, mul_one] at hc ha
    simp only [hca, hcb, or_self, if_false] at hc
    simp only [true_or, if_true, Real.cos_pi_div_two, Real.sin_pi_div_two, Complex.ofReal_zero,
      Complex.ofReal_one, one_mul, zero_sub] at ha
    rw [← hc] at ha
    exact absurd (congrArg Complex.re ha) (by simp)

end Witness

/-! ### Section I — the substratum and the sourced theories by instruments -/

section Theories

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **THE CONSEQUENCE CLOSURE, INSTRUMENT FORM**: reversible instrument locality, embedded
observation, the exchanges, the phases and the read-write operators at every level. -/
def DerivedOIInst (T : FiniteOperationalTheory A) : Prop :=
  ReversibleInstrumentLocality T ∧ EmbeddedObservation T
    ∧ ExchangesAvailable T ∧ PhasesAvailable T ∧ ReadWriteAvailable T

/-- **THE SOURCED CLOSURE, INSTRUMENT FORM**: the conjuncts other than the phases. -/
def SourcedOIInst (T : FiniteOperationalTheory A) : Prop :=
  ReversibleInstrumentLocality T ∧ EmbeddedObservation T
    ∧ ExchangesAvailable T ∧ ReadWriteAvailable T

theorem derivedOIInst_iff_sourcedOIInst_phases (T : FiniteOperationalTheory A) :
    DerivedOIInst T ↔ SourcedOIInst T ∧ PhasesAvailable T := by
  constructor
  · rintro ⟨h1, h2, h3, h4, h5⟩
    exact ⟨⟨h1, h2, h3, h5⟩, h4⟩
  · rintro ⟨⟨h1, h2, h3, h5⟩, h4⟩
    exact ⟨h1, h2, h3, h4, h5⟩

theorem sourcedOIInst_of_derivedOIInst {T : FiniteOperationalTheory A} (h : DerivedOIInst T) :
    SourcedOIInst T :=
  ((derivedOIInst_iff_sourcedOIInst_phases T).mp h).1

theorem derivedOIInst_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : DerivedOIInst T :=
  have hd := derivedOI_of_qm T h
  ⟨reversibleInstrumentLocality_of_qm T h, hd.2.1, hd.2.2.1, hd.2.2.2.1, hd.2.2.2.2⟩

/-- **UNDER THE INSTRUMENT CLOSURE, QUANTUM MECHANICS IS EXACTLY PHASE-FREE RICHNESS.** -/
theorem derivedOIInst_qm_iff_phaseFree [Nonempty A] {T : FiniteOperationalTheory A}
    (h : DerivedOIInst T) : ExactAllFiniteEndomorphicQuantumOps T ↔ PhaseFreeRichness T :=
  ⟨fun hqm => ((oiPlusMinInst_iff_qm T).mpr hqm).2.1,
    fun hpf => (oiPlusMinInst_iff_qm T).mp ⟨instrumentLocality_of_reversible h.1, hpf, h.2.1⟩⟩

theorem sourcedOIInst_qm_iff_phaseFree [Nonempty A] {T : FiniteOperationalTheory A}
    (h : SourcedOIInst T) : ExactAllFiniteEndomorphicQuantumOps T ↔ PhaseFreeRichness T :=
  ⟨fun hqm => ((oiPlusMinInst_iff_qm T).mpr hqm).2.1,
    fun hpf => (oiPlusMinInst_iff_qm T).mp ⟨instrumentLocality_of_reversible h.1, hpf, h.2.1⟩⟩

/-- **THE SUBSTRATUM INSTRUMENT THEORY**: the instrument theory of the monomial class. -/
noncomputable abbrev substratumInstTheory (A : Type) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  instTheory substratumClass substratumClass_arch A

/-- **THE SOURCED INSTRUMENT THEORY**: the instrument theory of the sourced class. -/
noncomputable abbrev permInstTheory (A : Type) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  instTheory permClass permClass_arch A

/-- **THE SUBSTRATUM INSTRUMENT THEORY SATISFIES THE INSTRUMENT CLOSURE** on every carrier. -/
theorem substratumInstTheory_derivedOIInst : DerivedOIInst (substratumInstTheory A) :=
  ⟨instTheory_reversibleInstrumentLocality _ substratumClass_contextStable
      substratumClass_labelInvariant substratumClass_daggerStable,
    instTheory_embeddedObservation _ _ substratumClass_labelInvariant,
    fun _ a b => instTheory_avail_conj _ _ (exchange_monomial a b) (permMatrix_isometry _),
    fun _ a => instTheory_avail_conj _ _ (phase_monomial a) (phaseGate_unitary a),
    fun _ _ _ F l => instTheory_avail_conj _ _ (readWriteOperator_monomial F l)
      (by rw [readWriteOperator_eq_perm]; exact permMatrix_isometry _)⟩

/-- **THE SOURCED INSTRUMENT THEORY SATISFIES THE SOURCED INSTRUMENT CLOSURE.** -/
theorem permInstTheory_sourcedOIInst : SourcedOIInst (permInstTheory A) :=
  ⟨instTheory_reversibleInstrumentLocality _ permClass_contextStable permClass_labelInvariant
      permClass_daggerStable,
    instTheory_embeddedObservation _ _ permClass_labelInvariant,
    fun _ a b => instTheory_avail_conj _ _ (permClass_permMatrix (Equiv.swap a b))
      (permMatrix_isometry _),
    fun _ _ _ F l => instTheory_avail_conj _ _ (permClass_readWrite F l)
      (by rw [readWriteOperator_eq_perm]; exact permMatrix_isometry _)⟩

/-- **NO PHASE IN THE INSTRUMENT THEORY OF A BIJECTION-LEVEL CLASS**, through soundness. -/
theorem bijectionLevel_not_phasesAvailable_inst [Nonempty A] {𝓘 : ImplementationClass}
    (arch : Architecture 𝓘) (hb : BijectionLevel 𝓘) : ¬ PhasesAvailable (instTheory 𝓘 arch A) := by
  intro hp
  have hav := hp 2 (Classical.arbitrary A, 0)
  exact phaseGate_not_preservesNonneg _
    (preservesNonneg_of_realized hb (realized_of_instAvail arch hav ()))

theorem permInstTheory_not_phasesAvailable [Nonempty A] : ¬ PhasesAvailable (permInstTheory A) :=
  bijectionLevel_not_phasesAvailable_inst permClass_arch permClass_bijectionLevel

/-- **THE SOURCED INSTRUMENT THEORY FAILS THE INSTRUMENT CLOSURE**: the phases are the failing
conjunct. -/
theorem permInstTheory_not_derivedOIInst [Nonempty A] : ¬ DerivedOIInst (permInstTheory A) :=
  fun h => permInstTheory_not_phasesAvailable h.2.2.2.1

/-- **A CONFIGURATION-LEVEL CLASS GENERATES INSIDE THE SUBSTRATUM INSTRUMENT THEORY.** -/
theorem configurationLevel_instAvailExt_le {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (h : ConfigurationLevel 𝓘) {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hF : (instTheory 𝓘 arch A).availExt n O F) : (substratumInstTheory A).availExt n O F :=
  instAvail_mono (fun S _ _ K hK => h S K hK) hF

/-- **THE SOURCED INSTRUMENT THEORY LIES INSIDE THE SUBSTRATUM INSTRUMENT THEORY.** -/
theorem permInstTheory_availExt_le_substratum {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hF : (permInstTheory A).availExt n O F) : (substratumInstTheory A).availExt n O F :=
  instAvail_mono (fun _ _ _ K hK => permClass_le_substratum K hK) hF

/-- **THE FALSIFIER IS UNAVAILABLE IN THE SUBSTRATUM INSTRUMENT THEORY.** -/
theorem substratumInstTheory_falsifierUnavailable :
    FalsifierUnavailable (substratumInstTheory (Fin 2)) := by
  intro h
  obtain ⟨ι, _, K, hK, hadm⟩ := realized_of_instAvail substratumClass_arch h ()
  have hK' : conjChannel rot = ∑ i, conjChannel (K i) := hK
  apply rot_not_preservesDiag
  rw [hK']
  exact preservesDiag_sum _ _ fun i _ => preservesDiag_conj_of_monomial (hadm i)

theorem permInstTheory_falsifierUnavailable : FalsifierUnavailable (permInstTheory (Fin 2)) :=
  fun h => substratumInstTheory_falsifierUnavailable (permInstTheory_availExt_le_substratum _ h)

theorem substratumInstTheory_not_phaseFree : ¬ PhaseFreeRichness (substratumInstTheory (Fin 2)) :=
  not_phaseFree_of_falsifier_unavailable _ substratumInstTheory_derivedOIInst.2.1
    substratumInstTheory_falsifierUnavailable

/-- A transported permutation of the core is available in the substratum instrument theory. -/
theorem substratumInstTheory_relabel (g : Equiv.Perm Core) :
    (substratumInstTheory (Fin 2)).availExt 4 Unit
      (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
  exact instTheory_avail_conj _ _
    (substratumClass_labelInvariant _ _ coreIdx _ (monomial_permMatrix g))
    (SpectatorBridge.reindex_isometry _ _ (permMatrix_isometry g))

theorem permInstTheory_relabel (g : Equiv.Perm Core) :
    (permInstTheory (Fin 2)).availExt 4 Unit
      (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
  exact instTheory_avail_conj _ _
    (permClass_labelInvariant _ _ coreIdx _ (permClass_permMatrix g))
    (SpectatorBridge.reindex_isometry _ _ (permMatrix_isometry g))

/-- **THE SUBSTRATUM INSTRUMENT THEORY REALIZES THE SEALED OI CORE.** -/
theorem substratumInstTheory_realizesSealedOICore :
    RealizesSealedOICore (substratumInstTheory (Fin 2)) :=
  ⟨core_isC1C4, substratumInstTheory_relabel sigmaPerm, substratumInstTheory_relabel tauPerm,
    fun r => by rw [readVisible_eq_localLuders, readout_is_localLuders],
    by rw [readVisible_family_eq (substratumInstTheory (Fin 2))]; exact readout_relabel_available _,
    fun steps w => realizedFold_diagonal steps w⟩

/-- **THE SOURCED INSTRUMENT THEORY REALIZES THE SEALED OI CORE**, with no phase. -/
theorem permInstTheory_realizesSealedOICore : RealizesSealedOICore (permInstTheory (Fin 2)) :=
  ⟨core_isC1C4, permInstTheory_relabel sigmaPerm, permInstTheory_relabel tauPerm,
    fun r => by rw [readVisible_eq_localLuders, readout_is_localLuders],
    by rw [readVisible_family_eq (permInstTheory (Fin 2))]; exact readout_relabel_available _,
    fun steps w => realizedFold_diagonal steps w⟩

/-- **THE SUBSTRATUM INSTRUMENT THEORY'S AVAILABILITY**, as a property of a theory. -/
def SubstratumAvailInst (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    (substratumInstTheory A).availExt n O F → T.availExt n O F

theorem substratumAvailInst_phasesAvailable {T : FiniteOperationalTheory A}
    (hsub : SubstratumAvailInst T) : PhasesAvailable T :=
  fun n a => hsub n Unit _ (substratumInstTheory_derivedOIInst.2.2.2.1 n a)

/-- **THE SOURCED INSTRUMENT THEORY FAILS THE SUBSTRATUM INSTRUMENT AVAILABILITY**, the phases
witnessing the failure. -/
theorem permInstTheory_not_substratumAvailInst [Nonempty A] :
    ¬ SubstratumAvailInst (permInstTheory A) :=
  fun h => permInstTheory_not_phasesAvailable (substratumAvailInst_phasesAvailable h)

/-- **THE ROUTE B TARGET, INSTRUMENT FORM.** -/
def RouteBTargetInst : Prop :=
  ∃ T : FiniteOperationalTheory (Fin 2),
    (DerivedOIInst T ∧ RealizesSealedOICore T) ∧ FalsifierUnavailable T

/-- **THE ROUTE B TARGET HOLDS FOR THE NEW PRIMITIVE**, with the substratum instrument theory as
the witness. -/
theorem routeB_target_inst : RouteBTargetInst :=
  ⟨substratumInstTheory (Fin 2),
    ⟨substratumInstTheory_derivedOIInst, substratumInstTheory_realizesSealedOICore⟩,
    substratumInstTheory_falsifierUnavailable⟩

end Theories

#print axioms conjChannel_trace_iff
#print axioms instAvail_mono
#print axioms instAvail_trace
#print axioms realized_of_instAvail
#print axioms isGenInstrument_of_instAvail
#print axioms cp_of_instAvail
#print axioms instAvail_comp_one
#print axioms instAvail_one_comp
#print axioms instAvail_id
#print axioms transport_refl
#print axioms transport_trans
#print axioms transport_comp
#print axioms reindex_reindex
#print axioms reindex_isometry'
#print axioms uniformAttach_reindex
#print axioms transport_discard
#print axioms instAvail_transport
#print axioms tensorOf_conjTranspose
#print axioms tensorOf_mul'
#print axioms tensorOf_one_isometry'
#print axioms amplRefL_conjChannel
#print axioms amplRefL_sum
#print axioms amplRef_apply'
#print axioms refBlockR_amplRef
#print axioms amplRefL_comp
#print axioms tensorOf_one_reindex
#print axioms tensorOf_one_readProj
#print axioms amplRefL_transport
#print axioms refBlockR_reindex_uniformAttach
#print axioms amplRefL_discard
#print axioms instAvail_spectator
#print axioms instAvail_withSpectator
#print axioms instFamily_regrouping
#print axioms instFamily_relabelling
#print axioms instTheory_ambient
#print axioms instTheory_embeddedObservation
#print axioms instTheory_availExt_iff
#print axioms instTheory_le_genTheory
#print axioms instTheory_avail_conj
#print axioms instTheory_fullClass_control
#print axioms instTheory_mono
#print axioms instrumentLocality_of_reversible
#print axioms instTheory_generated
#print axioms instTheory_instrumentLocality
#print axioms instTheory_reversibleInstrumentLocality
#print axioms isGenInstrument_of_instrumentGenerated
#print axioms parallel_of_instrumentLocal
#print axioms observationalIndependence_of_instrumentLocality
#print axioms krausSoundExt_of_instrumentGenerated
#print axioms validity_of_instrumentLocality
#print axioms instAvail_fullClass_of_krausFamily
#print axioms instrumentGenerated_of_qm
#print axioms instrumentLocality_of_qm
#print axioms reversibleInstrumentLocality_of_qm
#print axioms countermodel_not_instrumentGenerated
#print axioms countermodel_not_instrumentLocality
#print axioms instrumentLocality_independent
#print axioms oiPlusEmbedded_of_oiPlusInst
#print axioms qm_of_oiPlusInst
#print axioms oiPlusInst_of_qm
#print axioms oiPlusInst_iff_qm
#print axioms qm_of_oiPlusMinInst
#print axioms oiPlusMinInst_of_qm
#print axioms oiPlusMinInst_iff_qm
#print axioms oiPlusMinInst_iff_oiPlusMin
#print axioms carrier_general_oiPlusMinInst
#print axioms conjChannel_zero'
#print axioms exists_scaled_mem_of_instAvail_unitary
#print axioms inverseAccessibility_of_instrumentGenerated
#print axioms inverseAccessibility_of_reversibleInstrumentLocality
#print axioms fullClass_phaseSaturated
#print axioms diagClass_phaseSaturated
#print axioms substratumClass_phaseSaturated
#print axioms permClass_phaseSaturated
#print axioms ones_apply
#print axioms ones_prod
#print axioms ones_sum
#print axioms mulVec_sum'
#print axioms star_ones_dotProduct_ones
#print axioms unitary_eigen_ones
#print axioms conjTranspose_mulVec_ones_of_eigen
#print axioms readProj_sum
#print axioms reindex_sum
#print axioms reindex_one
#print axioms sum_filter_comp
#print axioms onesNormal_uniform
#print axioms ancBlock_conjTranspose_mulVec_ones
#print axioms splitWeight_sum_star
#print axioms splitWeight_sum_normSq
#print axioms instAvail_onesNormal
#print axioms instAvail_unitary_fixes_ones
#print axioms onesCompatible_one
#print axioms onesCompatible_mul
#print axioms unitary_conjTranspose_ones
#print axioms onesClass_of_unitary_ones
#print axioms permMatrix_mulVec_ones
#print axioms onesClass_permMatrix
#print axioms gateFlow_mulVec_ones
#print axioms onesClass_gateFlow
#print axioms onesCompatible_secEmb
#print axioms ancBlock_eq_secEmb
#print axioms readProj_conjTranspose
#print axioms readProj_mul_self
#print axioms fromBlocks_diag_unitary
#print axioms fromBlocks_diag_mulVec_ones
#print axioms onesCompatible_fromRows_left
#print axioms onesCompatible_fromRows_right
#print axioms onesClass_arch
#print axioms tensorOf_eq_tensorRect
#print axioms tensorRect_mul
#print axioms tensorRect_conjTranspose
#print axioms tensorRect_smul
#print axioms tensorRect_mulVec_ones
#print axioms onesCompatible_tensorRect_one
#print axioms onesClass_contextStable
#print axioms reindex_left_conjTranspose_mulVec
#print axioms onesCompatible_reindex_left
#print axioms onesClass_labelInvariant
#print axioms onesClass_daggerStable
#print axioms isometry_fixes_ones
#print axioms pairProj_eq_diagonal
#print axioms pairProj_mulVec_ones
#print axioms transition_mulVec_ones
#print axioms pairProj_conjTranspose
#print axioms flow_mul_one_sub_pairProj
#print axioms flow_mul_pairProj
#print axioms exp_star_mul_self
#print axioms exp_ofReal_mul_I_eq
#print axioms star_exp_ofReal_mul_I
#print axioms pairPhase_isometry
#print axioms pairPhase_mulVec_ones
#print axioms pairPhaseOf_star_mul_self
#print axioms levelGate_isometry
#print axioms levelGate_mulVec_ones
#print axioms levelGate_ancBlock
#print axioms secEmb_conjTranspose_mul_tensorOf
#print axioms diagonal_pairPhase_eq
#print axioms gadget_block
#print axioms transition_scaled_mem_onesClass
#print axioms flow_mulVec_ones_apply
#print axioms flow_realized_not_instrumentRealized
#print axioms derivedOIInst_iff_sourcedOIInst_phases
#print axioms sourcedOIInst_of_derivedOIInst
#print axioms derivedOIInst_of_qm
#print axioms derivedOIInst_qm_iff_phaseFree
#print axioms sourcedOIInst_qm_iff_phaseFree
#print axioms substratumInstTheory_derivedOIInst
#print axioms permInstTheory_sourcedOIInst
#print axioms bijectionLevel_not_phasesAvailable_inst
#print axioms permInstTheory_not_phasesAvailable
#print axioms permInstTheory_not_derivedOIInst
#print axioms configurationLevel_instAvailExt_le
#print axioms permInstTheory_availExt_le_substratum
#print axioms substratumInstTheory_falsifierUnavailable
#print axioms permInstTheory_falsifierUnavailable
#print axioms substratumInstTheory_not_phaseFree
#print axioms substratumInstTheory_relabel
#print axioms permInstTheory_relabel
#print axioms substratumInstTheory_realizesSealedOICore
#print axioms permInstTheory_realizesSealedOICore
#print axioms substratumAvailInst_phasesAvailable
#print axioms permInstTheory_not_substratumAvailInst
#print axioms routeB_target_inst

end InstrumentRealization
end OIBridge
