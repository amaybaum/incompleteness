/-
  OIBridge/CompletedOI.lean — the layered hierarchy: bare OI unchanged, completed OI made
  explicit, and the three substantive completion principles compressed to principles with
  independent observational meaning.

  ROUND FIFTY-THREE. The completion classification (`GeneralCarrier.main_result`) says: on a
  well-formed finite operational theory, exact finite operational QM is exactly the three
  substantive principles (inert spectators, sufficient reversible control, iterated
  composition), and bare OI does not select QM. The census of round fifty-two says the three
  principles are three independent axes on the class of well-formed OI-compatible theories.
  This file does two things with that.

  THE HIERARCHY, LAYERED. `OICore` is the original observation-incompleteness principle
  (`RealizesSealedOICore`), unchanged, so every existing result keeps its meaning.
  `CompletedOI` is the core plus the five completion conditions. Within the scope of the
  theorem, `CompletedOI ⟺ finite operational QM` (`completedOI_iff_qm`); and the file records
  the redundancy the classification already exposes — full composite control realizes the
  sealed core, so `CompletedOI ⟺ the five conditions` (`completedOI_iff_physical`). Bare OI
  is not completed OI (`oiCore_not_completedOI`).

  THE COMPRESSION. For each substantive principle, the weakest natural extension of the OI
  idea that implies it, formulated in the kernel's own language, proved to imply the
  operational condition, and proved equivalent to it on the relevant class:

      · OBSERVATIONAL INDEPENDENCE — an available operation on a composite acts as itself
        when an untouched system is adjoined (`ObservationalIndependence`, the parallel
        reference extension). It is inert-spectator compositionality restated
        (`observationalIndependence_iff_inert`), and it is exactly what makes independent
        observations jointly performable: two available operations on disjoint composites
        compose in parallel (`parallel_of_observationalIndependence`). The compression here
        is nil beyond the equivalence: the principle IS the condition, and the census shows
        it cannot be derived from the other two.
      · REVERSIBLE RICHNESS — every available reversible transformation can be undone, and
        at every level there is a passive drift with finitely many controls whose Lie
        algebra contains `su(D)` (`ReversibleRichness`). By the round-fifty reachability
        theorem this gives full composite unitary control (`control_of_reversibleRichness`);
        conversely a well-formed theory with full control is reversibly rich, with the
        rank-one projector as drift and all unitaries as controls
        (`reversibleRichness_of_control`). Reversible richness is a finite drift/control
        certificate — a statement about a generating set — not the postulate that every
        unitary is available.
      · OBSERVER RECURSION — a composite observable system is itself an admissible observable
        system: for every level `n` there is a finite operational theory on the level-`n`
        composite whose system families are the level-`n` families and whose ancilla
        families are the transported higher-level families (`ObserverRecursion`,
        `IsShiftedTheory`). It implies iterated composition
        (`closure_of_observerRecursion`: the shifted theory's own discard rule), and
        conversely iterated composition plus the identity and the relative readout at every
        level yield the shifted theory (`observerRecursion_of_closure`, the round-38
        construction with its control and spectator hypotheses weakened to exactly what it
        consumes).

  THE STRENGTHENED PRINCIPLE. `OIPlus` is the core, well-formedness, observational
  independence, reversible richness and observer recursion. Then

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `qm_of_oiPlus`: OI⁺ ⟹ exact finite operational QM.                            │
      │  `oiPlus_of_qm`: exact finite operational QM ⟹ OI⁺.                            │
      │  `oiPlus_iff_qm`: OI⁺ ⟺ exact finite operational QM, on the qubit carrier.     │
      │  `oiPlus_independence`: each of the three principles fails on a theory with    │
      │      the core, well-formedness and the other two — from the census cells.      │
      │  `completedOI_iff_qm`, `completedOI_iff_physical`, `oiCore_not_completedOI`.   │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT IS AND IS NOT CLAIMED. Proved: everything above, on the qubit carrier, with the usual
  axiom footprint. NOT claimed: that any of the three principles follows from bare OI (the
  census proves the opposite); that observational independence is compressed beyond its
  equivalent forms; that the principles are the only natural ones; anything about
  well-formedness being derivable. `OICore` is `RealizesSealedOICore` and is not modified.
  No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.SubstantiveCensus

namespace OIBridge
namespace OIHierarchy

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

attribute [local instance 100] LieRing.ofAssociativeRing

/-! ### Section A — the hierarchy, layered -/

section Hierarchy

/-- **BARE OI**: the original observation-incompleteness principle, unchanged. -/
def OICore (T : FiniteOperationalTheory (Fin 2)) : Prop := RealizesSealedOICore T

/-- **COMPLETED OI**: the core plus the five completion conditions. -/
def CompletedOI (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  OICore T ∧ PhysicalCompletionConditions T

/-- **COMPLETED OI IS FINITE OPERATIONAL QM**, within the scope of the theorem. -/
theorem completedOI_iff_qm (T : FiniteOperationalTheory (Fin 2)) :
    CompletedOI T ↔ ExactAllFiniteEndomorphicQuantumOps T := by
  rw [exactAll_iff_physical_general]
  exact ⟨fun h => h.2, fun h => ⟨realizesSealedOICore_of_control T h.2.2.1, h⟩⟩

/-- **THE REDUNDANCY, MADE EXPLICIT**: because full composite control realizes the sealed
core, the OI clause of completed OI is implied by the five conditions. -/
theorem completedOI_iff_physical (T : FiniteOperationalTheory (Fin 2)) :
    CompletedOI T ↔ PhysicalCompletionConditions T :=
  ⟨fun h => h.2, fun h => ⟨realizesSealedOICore_of_control T h.2.2.1, h⟩⟩

/-- **BARE OI IS NOT COMPLETED OI.** -/
theorem oiCore_not_completedOI :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ ¬ CompletedOI T :=
  ⟨diagTheory, diag_realizesSealedOICore, fun h => diag_not_control h.2.2.2.1⟩

end Hierarchy

/-! ### Section B — observational independence -/

section Independence

variable (T : FiniteOperationalTheory (Fin 2))

/-- **OBSERVATIONAL INDEPENDENCE**: an available operation on a composite acts as itself when
an untouched system is adjoined. -/
def ObservationalIndependence : Prop := HasParallelReferenceExtension T

theorem observationalIndependence_iff_inert :
    ObservationalIndependence T ↔ InertSpectatorCompositionality T :=
  (inertSpectator_iff_parallelReferenceExtension T).symm

/-- Two operations on disjoint composites, performed jointly: `F` on the level-`n` factor and
`G` on the level-`k` factor of a level-`m` composite, along a reindexing `e`. -/
def parallelPair {n k m : ℕ} (e : (Fin 2 × Fin k) × (Fin 2 × Fin n) ≃ Fin 2 × Fin m)
    {O O' : Type}
    (F : O → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
    (G : O' → Matrix (Fin 2 × Fin k) (Fin 2 × Fin k) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin k) (Fin 2 × Fin k) ℂ) :
    O' × O → Matrix (Fin 2 × Fin m) (Fin 2 × Fin m) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin m) (Fin 2 × Fin m) ℂ :=
  fun c => (withSpectator (Fin 2 × Fin k) e (F c.2)).comp
    (withSpectator (Fin 2 × Fin n) ((Equiv.prodComm _ _).trans e) (G c.1))

/-- **INDEPENDENT OBSERVATIONS ARE JOINTLY PERFORMABLE**: under observational independence,
two available operations on disjoint factors compose in parallel. -/
theorem parallel_of_observationalIndependence (h : ObservationalIndependence T) {n k m : ℕ}
    (e : (Fin 2 × Fin k) × (Fin 2 × Fin n) ≃ Fin 2 × Fin m) {O O' : Type} [Fintype O]
    [DecidableEq O] [Fintype O'] [DecidableEq O']
    {F : O → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    {G : O' → Matrix (Fin 2 × Fin k) (Fin 2 × Fin k) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin k) (Fin 2 × Fin k) ℂ}
    (hF : T.availExt n O F) (hG : T.availExt k O' G) :
    T.availExt m (O' × O) (parallelPair e F G) := by
  have hF' := h (Fin 2 × Fin k) n m e O F hF
  have hG' := h (Fin 2 × Fin n) k m ((Equiv.prodComm _ _).trans e) O' G hG
  have := T.availExt_bind m O' O
    (fun b => withSpectator (Fin 2 × Fin n) ((Equiv.prodComm _ _).trans e) (G b))
    (fun _ a => withSpectator (Fin 2 × Fin k) e (F a)) hG' (fun _ => hF')
  exact this

end Independence

/-! ### Section C — reversible richness -/

section Richness

variable (T : FiniteOperationalTheory (Fin 2))

/-- **REVERSIBLE RICHNESS**: every available reversible transformation can be undone, and at
every level a passive drift with finitely many controls generates `su(D)`. -/
def ReversibleRichness : Prop :=
  (∀ (n : ℕ) (V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ),
    T.availExt n Unit (fun _ => conjChannel V) → T.availExt n Unit (fun _ => conjChannel Vᴴ))
  ∧ ∀ n : ℕ, ∃ (G : Type) (H : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ)
      (U : G → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ),
      Hᴴ = H ∧ (∀ g, (U g)ᴴ * U g = 1) ∧ HControl H U
        ∧ (∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow H t)))
        ∧ (∀ g, T.availExt n Unit (fun _ => conjChannel (U g)))

theorem flow_zero {S : Type} [Fintype S] [DecidableEq S] (H : Matrix S S ℂ) :
    flow H 0 = 1 := by
  simp [flow, NormedSpace.exp_zero]

/-- A passive flow of a Hermitian drift is an isometry. -/
theorem flow_isometry {S : Type} [Fintype S] [DecidableEq S] (H : Matrix S S ℂ) (hH : Hᴴ = H)
    (t : ℝ) : (flow H t)ᴴ * flow H t = 1 := by
  have := (Unitary.mem_iff.mp (flow_mem_unitary H hH t)).1
  rwa [Matrix.star_eq_conjTranspose] at this

theorem single_diag_hermitian' {l : Type} [Fintype l] [DecidableEq l] (i₀ : l) :
    (Matrix.single i₀ i₀ (1 : ℂ))ᴴ = Matrix.single i₀ i₀ 1 := by
  ext a b
  rw [Matrix.conjTranspose_apply, single_entry, single_entry]
  by_cases h : i₀ = a ∧ i₀ = b
  · rw [if_pos ⟨h.2, h.1⟩, if_pos h, star_one]
  · rw [if_neg (fun hh => h ⟨hh.2, hh.1⟩), if_neg h, star_zero]

/-- **REVERSIBLE RICHNESS GIVES FULL COMPOSITE UNITARY CONTROL**, by the round-fifty
reachability theorem at every level. -/
theorem control_of_reversibleRichness (h : ReversibleRichness T) :
    HasCompositeUnitaryControl T := by
  intro n V hV
  obtain ⟨G, H, U, hH, hU, hLie, hflow, hctrl⟩ := h.2 n
  let avail : ∀ m : ℕ, (Fin m → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) → Prop :=
    fun m F => ∀ i : Fin m, T.availExt n Unit (fun _ => F i)
  have hreach : UniversalUnitaryReachability avail :=
    universalReachability_of_lieRank_unconditional H U hH hU hLie avail
      (fun V W hV hW i => by
        have := availExt_comp_unit T n _ _ (hW i) (hV i)
        rwa [conjChannel_mul] at this)
      (fun V hV i => h.1 n V (hV i))
      (fun _ => by
        have := hflow 0
        rwa [flow_zero] at this)
      (fun t _ => hflow t) (fun g _ => hctrl g)
  exact hreach V hV 0

/-- Conjugation by a permutation moves a matrix unit. -/
theorem perm_conj_single {l : Type} [Fintype l] [DecidableEq l] (i₀ i : l) :
    permMatrix (Equiv.swap i₀ i) * Matrix.single i₀ i₀ (1 : ℂ) * (permMatrix (Equiv.swap i₀ i))ᴴ
      = Matrix.single i i 1 := by
  rw [permMatrix_conjTranspose, Equiv.symm_swap]
  ext x y
  simp only [Matrix.mul_apply, permMatrix, single_entry, mul_ite, mul_one, mul_zero, ite_and,
    Finset.sum_ite_eq, Finset.mem_univ, if_true]
  have key : ∀ z, (i₀ = (Equiv.swap i₀ i) z) ↔ (z = i) := by
    intro z
    rw [eq_comm, Equiv.swap_apply_eq_iff, Equiv.swap_apply_left]
  simp only [key]
  by_cases h1 : i = x <;> by_cases h2 : i = y <;> simp [h1, h2, eq_comm]

/-- A rank-one spectral projector is the conjugate of a matrix unit. -/
theorem edyad_eq_conj_single' {l : Type} [Fintype l] [DecidableEq l] (W : Matrix l l ℂ) (i : l) :
    edyad W i = W * Matrix.single i i (1 : ℂ) * Wᴴ := by
  ext x y
  simp only [edyad_apply, Matrix.mul_apply, Matrix.conjTranspose_apply, single_entry, mul_ite,
    mul_one, mul_zero, ite_mul, zero_mul, ite_and, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- A rank-one spectral projector is the conjugate of the base matrix unit by a unitary. -/
theorem edyad_eq_conj_single {l : Type} [Fintype l] [DecidableEq l] (W : Matrix l l ℂ)
    (i₀ i : l) :
    edyad W i = (W * permMatrix (Equiv.swap i₀ i)) * Matrix.single i₀ i₀ (1 : ℂ)
      * (W * permMatrix (Equiv.swap i₀ i))ᴴ := by
  rw [edyad_eq_conj_single' W i, Matrix.conjTranspose_mul, ← perm_conj_single i₀ i]
  simp only [Matrix.mul_assoc]

/-- The product of a unitary and a permutation is unitary. -/
theorem mul_permMatrix_unitary {l : Type} [Fintype l] [DecidableEq l] {W : Matrix l l ℂ}
    (hW : Wᴴ * W = 1) (g : Equiv.Perm l) :
    (W * permMatrix g)ᴴ * (W * permMatrix g) = 1 := by
  rw [Matrix.conjTranspose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Wᴴ, hW, Matrix.one_mul,
    permMatrix_isometry]

/-- **THE RANK-ONE DRIFT WITH ALL UNITARIES AS CONTROLS GENERATES `su(D)`**: every
skew-Hermitian matrix is a real combination of conjugates of `−i·E₁₁`. -/
theorem hControl_single_all {l : Type} [Fintype l] [DecidableEq l] (i₀ : l) :
    HControl (Matrix.single i₀ i₀ (1 : ℂ))
      (fun W : {W : Matrix l l ℂ // Wᴴ * W = 1} => W.1) := by
  intro A hA
  have hB : (Complex.I • A).IsHermitian := by
    show (Complex.I • A)ᴴ = Complex.I • A
    rw [Matrix.conjTranspose_smul, hA.1, Complex.star_def, Complex.conj_I, neg_smul, smul_neg,
      neg_neg]
  obtain ⟨W, hW, hspec⟩ := hermitian_spectral_edyad hB
  have hA' : A = (-Complex.I) • (Complex.I • A) := by
    rw [smul_smul, neg_mul, Complex.I_mul_I, neg_neg, one_smul]
  rw [hA', hspec, Finset.smul_sum, ← LieSubalgebra.mem_toSubmodule]
  refine Submodule.sum_mem _ fun i _ => ?_
  rw [smul_comm]
  refine Submodule.smul_mem _ _ ?_
  rw [LieSubalgebra.mem_toSubmodule]
  refine LieSubalgebra.subset_lieSpan
    ⟨⟨W * permMatrix (Equiv.swap i₀ i), mul_permMatrix_unitary hW _⟩, ?_⟩
  rw [edyad_eq_conj_single W i₀ i]

/-- **FULL CONTROL ON A WELL-FORMED THEORY IS REVERSIBLY RICH.** -/
theorem reversibleRichness_of_control (hwf : WellFormed T) (hctrl : HasCompositeUnitaryControl T) :
    ReversibleRichness T := by
  refine ⟨fun n V hV => ?_, fun n => ?_⟩
  · -- an available conjugation is trace preserving, hence by an isometry, hence unitary
    have htr := (hwf.1 n Unit _ hV).2
    have hV1 : Vᴴ * V = 1 := by
      have h := sum_conjTranspose_mul_eq_one_of_trace (fun _ : Unit => V) fun X => htr X
      rwa [Fintype.sum_unique] at h
    exact hctrl n Vᴴ (by rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hV1)
  · rcases Nat.eq_zero_or_pos n with rfl | hn
    · refine ⟨Unit, 0, fun _ => 1, by simp, fun _ => by simp, fun A _ => ?_, fun t => ?_,
        fun _ => ?_⟩
      · have hA0 : A = 0 := by
          ext i _
          exact isEmptyElim i
        rw [hA0]
        exact (controlLie (0 : Matrix (Fin 2 × Fin 0) (Fin 2 × Fin 0) ℂ)
          (fun _ : Unit => (1 : Matrix (Fin 2 × Fin 0) (Fin 2 × Fin 0) ℂ))).zero_mem
      · exact hctrl 0 _ (flow_isometry (0 : Matrix (Fin 2 × Fin 0) (Fin 2 × Fin 0) ℂ) (by simp) t)
      · exact hctrl 0 1 (by simp)
    · let i₀ : Fin 2 × Fin n := (0, ⟨0, hn⟩)
      refine ⟨{W : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ // Wᴴ * W = 1},
        Matrix.single i₀ i₀ (1 : ℂ), fun W => W.1, single_diag_hermitian' i₀, fun W => W.2,
        hControl_single_all i₀, fun t => hctrl n _ (flow_isometry _ (single_diag_hermitian' i₀) t),
        fun W => hctrl n W.1 W.2⟩

end Richness

/-! ### Section D — observer recursion -/

section Recursion

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **A SHIFTED THEORY**: a finite operational theory on the level-`n` composite whose system
families are `T`'s level-`n` families and whose ancilla families are `T`'s transported
higher-level families. -/
def IsShiftedTheory (T : FiniteOperationalTheory A) (n : ℕ)
    (T' : FiniteOperationalTheory (A × Fin n)) : Prop :=
  (∀ (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T'.avail O F ↔ T.availExt n O F)
  ∧ ∀ (m : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix ((A × Fin n) × Fin m) ((A × Fin n) × Fin m) ℂ →ₗ[ℂ]
      Matrix ((A × Fin n) × Fin m) ((A × Fin n) × Fin m) ℂ),
    T'.availExt m O F ↔ T.availExt (n * m) O (fun a => transport (shiftIdx A n m) (F a))

/-- **OBSERVER RECURSION**: a composite observable system is itself an admissible observable
system, at every level. -/
def ObserverRecursion (T : FiniteOperationalTheory A) : Prop :=
  ∀ n : ℕ, ∃ T' : FiniteOperationalTheory (A × Fin n), IsShiftedTheory T n T'

/-- **OBSERVER RECURSION GIVES ITERATED COMPOSITION**: the shifted theory's own discard rule,
applied to its fresh uniform ancilla, is the closure rule. -/
theorem closure_of_observerRecursion {T : FiniteOperationalTheory A} (h : ObserverRecursion T) :
    IteratedAncillaClosure T := by
  intro n m O _ _ F hF
  obtain ⟨T', hsys, hext⟩ := h n
  have hF' : T'.availExt (m + 1) O F := (hext (m + 1) O F).mpr hF
  exact (hsys O _).mp (T'.prepAvail_discard (m + 1) (uniformAttach (m + 1)) O F
    (T'.prepAvail_uniform m) hF')

/-- **THE SHIFTED THEORY FROM ITERATED COMPOSITION**, with the round-38 control and spectator
hypotheses weakened to exactly what the construction consumes: the identity available at
every level, and the relative Lüders readout available at every level pair. -/
noncomputable def shiftOfClosure (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hread : ∀ n m, T.availExt (n * m) (Fin m)
      (fun k => transport (shiftIdx A n m) (localLuders (A := A × Fin n) k)))
    (hclos : IteratedAncillaClosure T) (n : ℕ) : FiniteOperationalTheory (A × Fin n) where
  avail := fun O _ _ F => T.availExt n O F
  availExt := fun m O _ _ F => T.availExt (n * m) O (fun a => transport (shiftIdx A n m) (F a))
  avail_id := hid n
  avail_coarse := fun O O' _ _ _ _ F f hF => T.availExt_coarse n O O' F f hF
  availExt_coarse := by
    intro m O O' _ _ _ _ F f hF
    have h := T.availExt_coarse (n * m) O O' _ f hF
    show T.availExt (n * m) O' (fun a => transport (shiftIdx A n m)
      (∑ j ∈ Finset.univ.filter (fun j => f j = a), F j))
    simp only [transport_sum]
    exact h
  availExt_bind := by
    intro m O O' _ _ _ _ F G hF hG
    show T.availExt (n * m) (O × O')
      (fun c => transport (shiftIdx A n m) ((G c.1 c.2).comp (F c.1)))
    simp only [transport_comp]
    exact T.availExt_bind (n * m) O O' _ (fun a b => transport (shiftIdx A n m) (G a b)) hF hG
  prepAvail := fun m P => 0 < m ∧ ∃ Φ,
    T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) Φ)
      ∧ P = Φ.comp (uniformAttach m)
  prepAvail_uniform := fun m =>
    ⟨Nat.succ_pos m, LinearMap.id, by
      rw [transport_id]
      exact hid _, by rw [LinearMap.id_comp]⟩
  prepAvail_post := by
    rintro m P Φ ⟨hm, Ψ, hΨ, rfl⟩ hΦ
    refine ⟨hm, Φ.comp Ψ, ?_, by rw [LinearMap.comp_assoc]⟩
    show T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) (Φ.comp Ψ))
    simp only [transport_comp]
    exact availExt_comp_unit T _ _ _ hΨ hΦ
  readout := fun _ k => localLuders k
  readout_avail := fun m => hread n m
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
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

theorem observerRecursion_of_closure (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hread : ∀ n m, T.availExt (n * m) (Fin m)
      (fun k => transport (shiftIdx A n m) (localLuders (A := A × Fin n) k)))
    (hclos : IteratedAncillaClosure T) : ObserverRecursion T :=
  fun n => ⟨shiftOfClosure T hid hread hclos n, by intros; exact Iff.rfl, by intros; exact Iff.rfl⟩

/-- **OBSERVER RECURSION IS ITERATED COMPOSITION** on theories with the identity and the
relative readout at every level. -/
theorem observerRecursion_iff_closure (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hread : ∀ n m, T.availExt (n * m) (Fin m)
      (fun k => transport (shiftIdx A n m) (localLuders (A := A × Fin n) k))) :
    ObserverRecursion T ↔ IteratedAncillaClosure T :=
  ⟨closure_of_observerRecursion, observerRecursion_of_closure T hid hread⟩

end Recursion

/-! ### Section E — the strengthened principle and its equivalence with QM -/

section OIPlus

variable (T : FiniteOperationalTheory (Fin 2))

/-- **OI⁺**: the core, well-formedness, observational independence, reversible richness and
observer recursion. -/
def OIPlus : Prop :=
  OICore T ∧ WellFormed T ∧ ObservationalIndependence T ∧ ReversibleRichness T
    ∧ ObserverRecursion T

/-- **OI⁺ IMPLIES FINITE OPERATIONAL QM.** -/
theorem qm_of_oiPlus (h : OIPlus T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨-, hwf, hind, hrich, hrec⟩ := h
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp hind, control_of_reversibleRichness T hrich,
    closure_of_observerRecursion hrec⟩

/-- **FINITE OPERATIONAL QM SATISFIES OI⁺.** -/
theorem oiPlus_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlus T := by
  have hp := physical_of_exactAll T h
  have hwf : WellFormed T := ⟨hp.1, hp.2.2.2.2⟩
  refine ⟨realizesSealedOICore_of_control T hp.2.2.1, hwf,
    (observationalIndependence_iff_inert T).mpr hp.2.1,
    reversibleRichness_of_control T hwf hp.2.2.1,
    observerRecursion_of_closure T (availExt_id_of_control T hp.2.2.1)
      (availExt_relativeReadout T hp.2.1) hp.2.2.2.1⟩

/-- **OI⁺ ⟺ FINITE OPERATIONAL QM**, on the qubit carrier. -/
theorem oiPlus_iff_qm : OIPlus T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlus T, oiPlus_of_qm T⟩

/-- OI⁺ is completed OI. -/
theorem oiPlus_iff_completedOI : OIPlus T ↔ CompletedOI T := by
  rw [oiPlus_iff_qm, completedOI_iff_qm]

end OIPlus

/-! ### Section F — the three principles are independent, from the census -/

section IndependenceOfPrinciples

theorem countermodel_hid : ∀ n, countermodel.availExt n Unit (fun _ => LinearMap.id) :=
  availExt_id_of_control countermodel countermodel_control

theorem countermodel_hread (n m : ℕ) : countermodel.availExt (n * m) (Fin m)
    (fun k => transport (shiftIdx (Fin 2) n m) (localLuders (A := Fin 2 × Fin n) k)) := by
  refine ⟨fun k => twoPositive_transport _ (localLuders_twoPositive k), fun X => ?_⟩
  simp only [trace_transport]
  rw [localLuders_trace_sum, trace_reindex]

theorem diag_hid : ∀ n, diagTheory.availExt n Unit (fun _ => LinearMap.id) := fun n =>
  ⟨⟨fun _ => by rw [← conjChannel_one]; exact conjChannel_cp _, fun X => by
    rw [Fintype.sum_unique, LinearMap.id_apply]⟩, fun _ => preservesDiag_id⟩

theorem diag_hread (n m : ℕ) : diagTheory.availExt (n * m) (Fin m)
    (fun k => transport (shiftIdx (Fin 2) n m) (localLuders (A := Fin 2 × Fin n) k)) := by
  refine ⟨⟨fun k => transport_cp _ (localLuders_cp k), fun X => ?_⟩,
    fun k => preservesDiag_transport _ (preservesDiag_localLuders k)⟩
  simp only [trace_transport]
  rw [localLuders_trace_sum, trace_reindex]

/-- **OBSERVATIONAL INDEPENDENCE IS INDEPENDENT** of the core, well-formedness, reversible
richness and observer recursion: the round-34 countermodel. -/
theorem independence_independent :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ReversibleRichness T
      ∧ ObserverRecursion T ∧ ¬ ObservationalIndependence T :=
  ⟨countermodel, countermodel_realizesSealedOICore,
    ⟨countermodel_validity, countermodel_systemToLevelOne⟩,
    reversibleRichness_of_control _ ⟨countermodel_validity, countermodel_systemToLevelOne⟩
      countermodel_control,
    observerRecursion_of_closure _ countermodel_hid countermodel_hread
      countermodel_iteratedAncillaClosure,
    fun h => countermodel_not_inert ((observationalIndependence_iff_inert _).mp h)⟩

/-- **REVERSIBLE RICHNESS IS INDEPENDENT**: the diagonal theory. -/
theorem richness_independent :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ObservationalIndependence T
      ∧ ObserverRecursion T ∧ ¬ ReversibleRichness T :=
  ⟨diagTheory, diag_realizesSealedOICore, ⟨diag_validity, diag_systemToLevelOne⟩,
    (observationalIndependence_iff_inert _).mpr diag_inert,
    observerRecursion_of_closure _ diag_hid diag_hread diag_iteratedAncillaClosure,
    fun h => diag_not_control (control_of_reversibleRichness _ h)⟩

/-- **OBSERVER RECURSION IS INDEPENDENT**: the rank-gap theory. -/
theorem recursion_independent :
    ∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ObservationalIndependence T
      ∧ ReversibleRichness T ∧ ¬ ObserverRecursion T :=
  ⟨gapTheory, gap_realizesSealedOICore, ⟨gap_validity, gap_systemToLevelOne⟩,
    (observationalIndependence_iff_inert _).mpr gap_inert,
    reversibleRichness_of_control _ ⟨gap_validity, gap_systemToLevelOne⟩ gap_control,
    fun h => gap_not_iteratedAncillaClosure (closure_of_observerRecursion h)⟩

/-- **THE THREE PRINCIPLES OF OI⁺ ARE INDEPENDENT**, each of the core, well-formedness and the
other two. -/
theorem oiPlus_independence :
    (∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ReversibleRichness T
      ∧ ObserverRecursion T ∧ ¬ ObservationalIndependence T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ObservationalIndependence T
      ∧ ObserverRecursion T ∧ ¬ ReversibleRichness T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2), OICore T ∧ WellFormed T ∧ ObservationalIndependence T
      ∧ ReversibleRichness T ∧ ¬ ObserverRecursion T) :=
  ⟨independence_independent, richness_independent, recursion_independent⟩

end IndependenceOfPrinciples

/-! ### Section F — the forward redundancy of the OI core

`oiPlus_of_qm` already contains the implication `QM → OICore`, but it is buried inside a
five-conjunct construction and is easy to miss, and easier still to misread. This section states it
on its own and pairs it with the two facts that fix how it may be read.

**Containment.** Every theory in the characterized quantum class realizes the sealed OI core. The
route is `QM → full composite unitary control → RealizesSealedOICore`, so the core is reached
because the theory is *operationally rich enough to build the four-state hidden-memory gadget*, not
because it is quantum.

**Redundancy.** `completedOI_iff_physical` is the sharper statement: the OI conjunct of completed OI
is implied by the five physical conditions, so removing it changes nothing. The OI core does **no
work** in the forward derivation of quantum mechanics. What selects QM is coherent controllability.

**No ontological necessity.** Neither statement shows that quantum mechanics requires a hidden
sub-quantum level, or that observational incompleteness explains quantum structure. `OICore` is an
existential realizability condition — the theory *can implement* a particular gadget — and a
containment theorem about it is not an explanatory one. Any reading of the form "QM requires hidden
information", "observation incompleteness produces quantum mechanics" or "QM cannot exist without
OI" is unsupported by anything here except in the narrow core-containment sense stated above.

**What the core is still for.** It defines what counts as an OI realization, and it is what makes
`oiCore_not_completedOI` and `oi_alone_not_qm` say something: non-quantum theories satisfy it, so
"bare OI is not enough" has content. Its role is to seal the class, not to generate the theorem.
-/

section ForwardRedundancy

/-- **QUANTUM MECHANICS REALIZES THE SEALED OI CORE.** The forward implication, on its own and
findable. Containment only: the route is through full composite unitary control, so this says the
quantum class is rich enough to build the core's gadget, not that observation explains it. -/
theorem qm_implies_oiCore (T : FiniteOperationalTheory (Fin 2))
    (h : ExactAllFiniteEndomorphicQuantumOps T) : OICore T :=
  realizesSealedOICore_of_control T (physical_of_exactAll T h).2.2.1

/-- **THE FORWARD-REDUNDANCY AUDIT ENTRY**, in one place: containment holds, the core is redundant
in the forward direction, and the converse fails. The three together are the whole of what the
formalization supports about "QM and OI", and they are exactly what rules out reading the
containment as an explanatory necessity. -/
theorem oiCore_forward_redundancy :
    (∀ T : FiniteOperationalTheory (Fin 2), ExactAllFiniteEndomorphicQuantumOps T → OICore T)
    ∧ (∀ T : FiniteOperationalTheory (Fin 2),
        CompletedOI T ↔ PhysicalCompletionConditions T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
        OICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T) :=
  ⟨qm_implies_oiCore, completedOI_iff_physical, by
    obtain ⟨T, hcore, hnc⟩ := oiCore_not_completedOI
    exact ⟨T, hcore, fun hq => hnc ((completedOI_iff_qm T).mpr hq)⟩⟩

end ForwardRedundancy

#print axioms qm_implies_oiCore
#print axioms oiCore_forward_redundancy
#print axioms completedOI_iff_qm
#print axioms completedOI_iff_physical
#print axioms oiCore_not_completedOI
#print axioms observationalIndependence_iff_inert
#print axioms parallel_of_observationalIndependence
#print axioms flow_zero
#print axioms flow_isometry
#print axioms single_diag_hermitian'
#print axioms control_of_reversibleRichness
#print axioms perm_conj_single
#print axioms edyad_eq_conj_single'
#print axioms edyad_eq_conj_single
#print axioms mul_permMatrix_unitary
#print axioms hControl_single_all
#print axioms reversibleRichness_of_control
#print axioms closure_of_observerRecursion
#print axioms observerRecursion_of_closure
#print axioms observerRecursion_iff_closure
#print axioms qm_of_oiPlus
#print axioms oiPlus_of_qm
#print axioms oiPlus_iff_qm
#print axioms oiPlus_iff_completedOI
#print axioms countermodel_hid
#print axioms countermodel_hread
#print axioms diag_hid
#print axioms diag_hread
#print axioms independence_independent
#print axioms richness_independent
#print axioms recursion_independent
#print axioms oiPlus_independence

end OIHierarchy
end OIBridge
