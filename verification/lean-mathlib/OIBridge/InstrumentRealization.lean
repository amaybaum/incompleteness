import OIBridge.ScalarClosure
import Mathlib.Data.Matrix.ColumnRowPartitioned

/-!
# The instrument-realization audit — one-instrument provenance for realized operations

The preregistered pass of `INSTRUMENT-REALIZATION-AUDIT.md`, after the migration of
`INSTRUMENT-MIGRATION-AUDIT.md`. `Realized 𝓘 S Φ` takes the branches of an operation from the
class one at a time, with nothing connecting them, and so admits the replication of a
post-selected contraction `c • U` into the unitary conjugation by `U`. The replacement,
`InstAvail`, is the implementation semantics of the kernel (`ImplementationLocality`): a family
of operations on a carrier is instrument-realized when it is built from admissible isometric
steps, the native readout of a register, coarse-graining, sequential composition with
outcome-dependent continuation, and the discard of a uniformly attached ancilla, by exactly
those five constructors and no sum. This file keeps the branch-wise notion as the comparison
object and proves that the two differ.

* The comparison object: the branch-wise instruments `IsGenInstrument` and the branch-wise
  theory `branchTheory` of an architecture; every instrument-realized family is a branch-wise
  instrument (`isGenInstrument_of_instAvail`), so the generated theory lies inside the
  branch-wise theory at every level (`genTheory_le_branchTheory`).
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

open Complex Matrix SpectatorBridge OperationalAssembly AncillaClosure
open CoherentLift hiding readProj
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure ReadWriteControl MinimalRepertoire
open LevelOneSeam PhysicalCharacterization RouteB ManuscriptAxioms OIRealization
open ReferenceExtension ReferenceSufficiency CompositeSoundness DimensionalCountermodel
open StinespringAssembly IsometryExtension SubstratumSource SubstratumInterfaceAudit
open ScalarClosure CoherentExtension OIHierarchyGeneral GeneralCarrier BoundaryAudit
open OperationalValidity DimensionalObstruction OIHierarchy IndependenceCensus

open scoped ComplexOrder

/-! ### Section A — the branch-wise notion, the comparison object -/

section Branch

/-- **THE BRANCH-WISE INSTRUMENTS**: branch-realized branches, trace preserved in aggregate. -/
def IsGenInstrument (𝓘 : ImplementationClass) (S : Type) [Fintype S] [DecidableEq S]
    {O : Type} [Fintype O] [DecidableEq O] (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (∀ a, Realized 𝓘 S (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

variable (𝓘 : ImplementationClass) (arch : Architecture 𝓘)

/-- **THE BRANCH-WISE THEORY OF AN ARCHITECTURE** on a carrier: availability is branch
realization with the aggregate trace preserved. The comparison object of T2; no theory of the
kernel is generated this way. -/
noncomputable def branchTheory (S : Type) [Fintype S] [DecidableEq S] :
    FiniteOperationalTheory S where
  avail := fun _ _ _ F => IsGenInstrument 𝓘 S F
  availExt := fun _ _ _ _ F => IsGenInstrument 𝓘 _ F
  avail_id := ⟨fun _ => realized_id (arch.one S), fun X => by
    rw [Fintype.sum_unique, LinearMap.id_apply]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => realized_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => realized_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => realized_comp (arch.mul _) ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => 0 < n ∧ ∃ Φ, IsGenInstrument 𝓘 _ (fun _ : Unit => Φ)
    ∧ P = Φ.comp (uniformAttach n)
  prepAvail_uniform := fun n =>
    ⟨n.succ_pos, LinearMap.id,
      ⟨fun _ => realized_id (arch.one _), fun X => by
        rw [Fintype.sum_unique, LinearMap.id_apply]⟩, by rw [LinearMap.id_comp]⟩
  prepAvail_post := by
    rintro n P Φ ⟨hn, Ψ, ⟨hΨ2, hΨtr⟩, rfl⟩ ⟨hΦ2, hΦtr⟩
    refine ⟨hn, Φ.comp Ψ, ⟨fun _ => realized_comp (arch.mul _) (hΦ2 ()) (hΨ2 ()), fun X => ?_⟩,
      by rw [LinearMap.comp_assoc]⟩
    rw [Fintype.sum_unique]
    have h1 := hΦtr (Ψ X)
    rw [Fintype.sum_unique] at h1
    have h2 := hΨtr X
    rw [Fintype.sum_unique] at h2
    exact h1.trans h2
  readout := fun _ k => localLuders k
  readout_avail := fun _ => ⟨fun k => realized_localLuders (arch.proj _ _) k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hn, Φ, ⟨hΦ2, hΦtr⟩, rfl⟩ ⟨hF2, hFtr⟩
    refine ⟨fun a => ?_, fun X => ?_⟩
    · show Realized 𝓘 S (discardWith n (Φ.comp (uniformAttach n)) (F a))
      have h : discardWith n (Φ.comp (uniformAttach n)) (F a)
          = discardWith n (uniformAttach n) ((F a).comp Φ) := by
        simp only [discardWith, LinearMap.comp_assoc]
      rw [h]
      exact realized_discard (arch.block _ _) (arch.smul _)
        (realized_comp (arch.mul _) (hF2 a) (hΦ2 ()))
    · show ∑ a, ((discardWith n (Φ.comp (uniformAttach n)) (F a)) X).trace = X.trace
      rw [Finset.sum_congr rfl fun a _ => discardWith_trace n _ (F a) X, hFtr]
      have h := hΦtr (uniformAttach n X)
      rw [Fintype.sum_unique] at h
      exact h.trans (uniformAttach_trace n hn.ne' X)

variable {A : Type} [Fintype A] [DecidableEq A] {𝓘}

/-- **T1**: an instrument-realized family is a branch-wise instrument. -/
theorem isGenInstrument_of_instAvail (arch : Architecture 𝓘) {T : Type} [Fintype T]
    [DecidableEq T] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix T T ℂ →ₗ[ℂ] Matrix T T ℂ} (h : InstAvail 𝓘 T O F) : IsGenInstrument 𝓘 T F :=
  ⟨realized_of_instAvail arch h, instAvail_trace h⟩

/-- **THE GENERATED THEORY LIES INSIDE THE BRANCH-WISE THEORY**: every family available by
instruments is available branch-wise. The converse fails (T2). -/
theorem genTheory_le_branchTheory (arch : Architecture 𝓘) (n : ℕ) {O : Type} [Fintype O]
    [DecidableEq O] (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (h : (genTheory 𝓘 arch A).availExt n O F) : (branchTheory 𝓘 arch A).availExt n O F :=
  isGenInstrument_of_instAvail arch h

end Branch

/-! ### Section B — T2: the converse fails -/

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

/-! ### Section C — the closed-form ones-fixing class -/

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

/-! ### Section D — the countercontrol -/

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

#print axioms isGenInstrument_of_instAvail
#print axioms genTheory_le_branchTheory
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

end InstrumentRealization
end OIBridge
