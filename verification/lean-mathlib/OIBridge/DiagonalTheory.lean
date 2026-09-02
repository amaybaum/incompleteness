/-
  OIBridge/DiagonalTheory.lean — the control cell of the minimality audit: a quantum theory
  that preserves computational-basis diagonal states has every other physical completion
  condition and realizes the sealed OI core, yet lacks full composite unitary control.

  ROUND FORTY-THREE, PART TWO. Part one proved the five physical completion conditions
  necessary and, with boundary item 2 at the composite carriers, sufficient; and showed
  validity, inert spectators and trivial-ancilla consistency each independent of the other
  four. This file closes the control cell with a clean new witness.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `diagTheory`: system and composite families are normalized quantum            │
      │    instruments (Kraus on the system, CP + aggregate trace on composites) whose  │
      │    every branch PRESERVES DIAGONAL STATES; preparations are reference-tested   │
      │    and diagonal-preserving. The same predicate at every level.                 │
      │  It has: valid probabilities; inert spectators (the amplification of a          │
      │    diagonal-preserving map by an untouched reference is diagonal-preserving —   │
      │    `preservesDiag_amplRef`); iterated ancilla closure (attach, transport and    │
      │    discard preserve diagonals); system-to-level-one (transport does); and it    │
      │    realizes the sealed OI core (permutation channels and Lüders readouts        │
      │    preserve diagonals — `diag_realizesSealedOICore`).                          │
      │  It lacks full composite unitary control: the rational rotation                │
      │    `[[3/5, 4/5], [-4/5, 3/5]]` sends `|0⟩⟨0|` to a matrix with off-diagonal     │
      │    entry `-12/25` (`diag_not_control`).                                         │
      │  `control_independent`: OI realization + validity + inert spectators + closure │
      │    + trivial-ancilla consistency ⇏ full composite unitary control.              │
      │  `minimality_audit`: the four closed cells in one statement, with the closure  │
      │    cell recorded open (`admissible_not_systemToLevelOne`, part one).            │
      └──────────────────────────────────────────────────────────────────────────────┘

  WHAT THIS SETTLES. Universal unitary control is a sufficient RICHNESS certificate, not
  something the operational structure, OI realization, validity or the composition
  principles force: the diagonal-preserving theory is a perfectly consistent completion of
  the same sealed OI process that never creates coherence. With part one, the final answer
  to the original question is a classification: bare finite OI does not select QM; the
  non-quantum completion space has identifiable failure types (non-probabilistic operations,
  positive-but-not-CP composites, sound-but-incomplete composites, restricted control,
  system/level-one disagreement); and satisfying all five conditions is exact finite
  endomorphic QM.

  NOT claimed: the closure cell against all four other conditions (open, named) [CLOSED IN
  ROUND FORTY-FOUR: `RankGapTheory.closure_cell_closed`, `five_way_minimality`]; that any
  condition follows from OI; OI ⟺ QM. No structure field is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.PhysicalCharacterization

namespace OIBridge
namespace DiagonalTheory

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization HiddenCoherence

open scoped ComplexOrder

/-! ### Section A — diagonal preservation -/

section Diag

variable {S S' : Type*} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']

/-- A map preserves diagonal states. -/
def PreservesDiag (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) : Prop :=
  ∀ w : S → ℂ, ∃ w' : S' → ℂ, Φ (Matrix.diagonal w) = Matrix.diagonal w'

theorem preservesDiag_id : PreservesDiag (LinearMap.id : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :=
  fun w => ⟨w, rfl⟩

theorem preservesDiag_zero : PreservesDiag (0 : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) :=
  fun _ => ⟨0, by simp⟩

theorem preservesDiag_add {Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ} (hΦ : PreservesDiag Φ)
    (hΨ : PreservesDiag Ψ) : PreservesDiag (Φ + Ψ) := by
  intro w
  obtain ⟨u, hu⟩ := hΦ w
  obtain ⟨v, hv⟩ := hΨ w
  exact ⟨u + v, by rw [LinearMap.add_apply, hu, hv, Matrix.diagonal_add]; rfl⟩

theorem preservesDiag_sum {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ)
    (h : ∀ i ∈ s, PreservesDiag (Φ i)) : PreservesDiag (∑ i ∈ s, Φ i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using preservesDiag_zero
  | insert a s ha ih =>
    rw [Finset.sum_insert ha]
    exact preservesDiag_add (h a (Finset.mem_insert_self a s))
      (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

theorem preservesDiag_comp {S'' : Type*} [Fintype S''] [DecidableEq S'']
    {Φ : Matrix S' S' ℂ →ₗ[ℂ] Matrix S'' S'' ℂ} {Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ}
    (hΦ : PreservesDiag Φ) (hΨ : PreservesDiag Ψ) : PreservesDiag (Φ.comp Ψ) := by
  intro w
  obtain ⟨u, hu⟩ := hΨ w
  obtain ⟨v, hv⟩ := hΦ u
  exact ⟨v, by rw [LinearMap.comp_apply, hu, hv]⟩

theorem reindex_diagonal {l l' : Type*} [DecidableEq l] [DecidableEq l'] (e : l ≃ l')
    (w : l → ℂ) : Matrix.reindex e e (Matrix.diagonal w) = Matrix.diagonal (w ∘ e.symm) := by
  rw [Matrix.reindex_apply, Matrix.submatrix_diagonal_equiv]

theorem preservesDiag_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ} (h : PreservesDiag Φ) :
    PreservesDiag (transport e Φ) := by
  intro w
  obtain ⟨u, hu⟩ := h (w ∘ e)
  refine ⟨u ∘ e.symm, ?_⟩
  rw [transport_apply, reindex_diagonal, Equiv.symm_symm, hu, reindex_diagonal]

theorem refBlockR_diagonal {R : Type*} [Fintype R] [DecidableEq R] (w : R × S → ℂ) (i j : R) :
    refBlockR (Matrix.diagonal w) i j
      = if i = j then Matrix.diagonal (fun k => w (i, k)) else 0 := by
  ext k l
  by_cases hij : i = j
  · subst hij
    rw [if_pos rfl]
    by_cases hkl : k = l
    · subst hkl
      show Matrix.diagonal w (i, k) (i, k) = Matrix.diagonal _ k k
      rw [Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq]
    · show Matrix.diagonal w (i, k) (i, l) = Matrix.diagonal _ k l
      rw [Matrix.diagonal_apply_ne _ hkl, Matrix.diagonal_apply_ne _ (fun h => hkl (Prod.ext_iff.mp h).2)]
  · rw [if_neg hij]
    show Matrix.diagonal w (i, k) (j, l) = 0
    rw [Matrix.diagonal_apply_ne _ (fun h => hij (Prod.ext_iff.mp h).1)]

/-- **AMPLIFICATION BY AN UNTOUCHED REFERENCE PRESERVES DIAGONALS.** -/
theorem preservesDiag_amplRef (R : Type*) [Fintype R] [DecidableEq R]
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : PreservesDiag Φ) : PreservesDiag (amplRefL R Φ) := by
  choose g hg using h
  intro w
  refine ⟨fun p => g (fun k => w (p.1, k)) p.2, ?_⟩
  ext ⟨i, k⟩ ⟨j, l⟩
  show Φ (refBlockR (Matrix.diagonal w) i j) k l = _
  rw [refBlockR_diagonal]
  by_cases hij : i = j
  · subst hij
    rw [if_pos rfl, hg]
    by_cases hkl : k = l
    · subst hkl
      rw [Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq]
    · rw [Matrix.diagonal_apply_ne _ hkl,
        Matrix.diagonal_apply_ne _ (fun h => hkl (Prod.ext_iff.mp h).2)]
  · rw [if_neg hij, map_zero, Matrix.zero_apply,
      Matrix.diagonal_apply_ne _ (fun h => hij (Prod.ext_iff.mp h).1)]

theorem preservesDiag_withSpectator {A : Type*} [Fintype A] [DecidableEq A] (R : Type)
    [Fintype R] [DecidableEq R] {n m : ℕ} (e : R × (A × Fin n) ≃ A × Fin m)
    {Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : PreservesDiag Φ) : PreservesDiag (withSpectator R e Φ) := by
  rw [withSpectator_eq_transport]
  exact preservesDiag_transport e (preservesDiag_amplRef R h)

theorem preservesDiag_localLuders {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B]
    [DecidableEq B] (k : B) : PreservesDiag (localLuders (A := A) k) := by
  intro w
  refine ⟨fun p => if p.2 = k then w p else 0, ?_⟩
  ext p q
  rw [localLuders_apply]
  by_cases hpq : p = q
  · subst hpq
    rw [Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq]
    by_cases hk : p.2 = k
    · rw [if_pos ⟨hk, hk⟩, if_pos hk]
      obtain ⟨a, b⟩ := p
      simp only at hk
      subst hk
      rfl
    · rw [if_neg (fun h => hk h.1), if_neg hk]
  · rw [Matrix.diagonal_apply_ne _ hpq]
    by_cases h : p.2 = k ∧ q.2 = k
    · rw [if_pos h]
      obtain ⟨a, b⟩ := p
      obtain ⟨c, d⟩ := q
      simp only at h
      obtain ⟨rfl, rfl⟩ := h
      rw [Matrix.diagonal_apply_ne _ (fun hh => hpq (Prod.ext_iff.mpr ⟨(Prod.ext_iff.mp hh).1, rfl⟩))]
    · rw [if_neg h]

theorem preservesDiag_relabel (g : Equiv.Perm S) :
    PreservesDiag (correlationExtension g (onesCorr S)) :=
  fun w => ⟨fun a => w (g.symm a), correlationExtension_diagonal g _ (fun _ => rfl) w⟩

theorem preservesDiag_conjChannel_perm (g : Equiv.Perm S) :
    PreservesDiag (conjChannel (permMatrix g)) := by
  rw [← correlationExtension_ones_eq_conjChannel]
  exact preservesDiag_relabel g

theorem uniformAttach_diagonal {A : Type*} [Fintype A] [DecidableEq A] (n : ℕ) (w : A → ℂ) :
    uniformAttach (A := A) n (Matrix.diagonal w)
      = Matrix.diagonal (fun p : A × Fin n => w p.1 * ((n : ℂ))⁻¹) := by
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [uniformAttach_apply, tensorOf_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  by_cases hab : a = b
  · subst hab
    by_cases hij : i = j
    · subst hij
      simp
    · rw [Matrix.diagonal_apply_ne _ (fun h => hij (Prod.ext_iff.mp h).2), if_neg hij]
      simp
  · rw [Matrix.diagonal_apply_ne _ hab, Matrix.diagonal_apply_ne _ (fun h => hab (Prod.ext_iff.mp h).1)]
    simp

theorem ptraceAnc_diagonal {A : Type*} [Fintype A] [DecidableEq A] (n : ℕ) (w : A × Fin n → ℂ) :
    ptraceAnc n (Matrix.diagonal w) = Matrix.diagonal (fun s => ∑ e, w (s, e)) := by
  ext s t
  rw [ptraceAnc_apply]
  by_cases hst : s = t
  · subst hst
    rw [Matrix.diagonal_apply_eq]
    exact Finset.sum_congr rfl fun e _ => Matrix.diagonal_apply_eq _ _
  · rw [Matrix.diagonal_apply_ne _ hst]
    exact Finset.sum_eq_zero fun e _ =>
      Matrix.diagonal_apply_ne _ (fun h => hst (Prod.ext_iff.mp h).1)

/-- A preparation preserves diagonal states. -/
def PreservesDiagP {A : Type*} [Fintype A] [DecidableEq A] {n : ℕ}
    (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) : Prop :=
  ∀ w : A → ℂ, ∃ w', P (Matrix.diagonal w) = Matrix.diagonal w'

theorem preservesDiagP_uniform {A : Type*} [Fintype A] [DecidableEq A] (n : ℕ) :
    PreservesDiagP (uniformAttach (A := A) n) :=
  fun w => ⟨_, uniformAttach_diagonal n w⟩

theorem preservesDiag_discardWith {A : Type*} [Fintype A] [DecidableEq A] {n : ℕ}
    {P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ} (hP : PreservesDiagP P)
    {Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (hΦ : PreservesDiag Φ) : PreservesDiag (discardWith (A := A) n P Φ) := by
  intro w
  obtain ⟨u, hu⟩ := hP w
  obtain ⟨v, hv⟩ := hΦ u
  refine ⟨fun s => ∑ e, v (s, e), ?_⟩
  show ptraceAnc n (Φ (P (Matrix.diagonal w))) = _
  rw [hu, hv, ptraceAnc_diagonal]

end Diag

/-! ### Section B — the diagonal-preserving theory -/

/-- **THE DIAGONAL-PRESERVING THEORY**: normalized quantum instruments whose branches
preserve computational-basis diagonal states, at every level. -/
noncomputable def diagTheory : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F ∧ ∀ a, PreservesDiag (F a)
  availExt := fun _ _ _ _ F => IsCPInstrument F ∧ ∀ a, PreservesDiag (F a)
  avail_id := ⟨scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩, fun _ => preservesDiag_id⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f ⟨hF, hd⟩
    exact ⟨isKrausFamily_coarse hF f, fun a' => preservesDiag_sum _ _ fun j _ => hd j⟩
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨⟨h2, htr⟩, hd⟩
    refine ⟨⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩,
      fun a' => preservesDiag_sum _ _ fun j _ => hd j⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨⟨hF2, hFtr⟩, hFd⟩ hG
    refine ⟨⟨fun c => cp_comp ((hG c.1).1.1 c.2) (hF2 c.1), fun X => ?_⟩,
      fun c => preservesDiag_comp ((hG c.1).2 c.2) (hFd c.1)⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).1.2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P ∧ PreservesDiagP P
  prepAvail_uniform := fun n =>
    ⟨⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩,
      preservesDiagP_uniform _⟩
  prepAvail_post := by
    rintro n P Φ ⟨⟨hPtr, hPpsd⟩, hPd⟩ ⟨⟨hΦ2, hΦtr⟩, hΦd⟩
    refine ⟨⟨fun ρ => ?_, ?_⟩, fun w => ?_⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact cp_referencePositive (Fin 2) _ (hΦ2 ()) _ hPpsd
    · obtain ⟨u, hu⟩ := hPd w
      obtain ⟨v, hv⟩ := hΦd () u
      exact ⟨v, by rw [LinearMap.comp_apply, hu, hv]⟩
  readout := fun _ k => localLuders k
  readout_avail := fun n =>
    ⟨⟨fun k => localLuders_cp k, localLuders_trace_sum⟩, fun k => preservesDiag_localLuders k⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨⟨hPtr, hPpsd⟩, hPd⟩ ⟨⟨hF2, hFtr⟩, hFd⟩
    refine ⟨isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_), fun a => preservesDiag_discardWith hPd (hFd a)⟩
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef (cp_referencePositive (Fin 2) _ (hF2 a) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

/-! ### Section C — the four other conditions and the OI core -/

theorem diag_krausSoundExt : KrausSoundExt diagTheory :=
  fun _ _ _ _ F ⟨⟨hcp, htr⟩, _⟩ =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F hcp htr

theorem diag_validity : CompositeOperationalValidity diagTheory :=
  validity_of_krausSoundExt _ diag_krausSoundExt

theorem diag_parallelReferenceExtension : HasParallelReferenceExtension diagTheory := by
  intro R _ _ n m e O _ _ F ⟨⟨hcp, htr⟩, hd⟩
  refine ⟨⟨fun a => withSpectator_cp e (hcp a), fun X => ?_⟩,
    fun a => preservesDiag_withSpectator R e (hd a)⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex e.symm]

theorem diag_inert : InertSpectatorCompositionality diagTheory :=
  (inertSpectator_iff_parallelReferenceExtension _).mpr diag_parallelReferenceExtension

theorem preservesDiag_of_transport {l l' : Type*} [Fintype l] [Fintype l'] [DecidableEq l]
    [DecidableEq l'] (e : l ≃ l') {Φ : Matrix l l ℂ →ₗ[ℂ] Matrix l l ℂ}
    (h : PreservesDiag (transport e Φ)) : PreservesDiag Φ := by
  have := preservesDiag_transport e.symm h
  rwa [transport_symm_transport] at this

theorem diag_iteratedAncillaClosure : IteratedAncillaClosure diagTheory := by
  intro n m O _ _ F ⟨⟨hcp, htr⟩, hd⟩
  refine ⟨⟨fun a => discardWith_uniform_cp (cp_of_transport_cp _ (hcp a)), fun X => ?_⟩,
    fun a => preservesDiag_discardWith (preservesDiagP_uniform _) (preservesDiag_of_transport _ (hd a))⟩
  rw [Finset.sum_congr rfl fun a _ => discardWith_trace (m + 1) _ (F a) X]
  have h := htr (Matrix.reindex (shiftIdx (Fin 2) n (m + 1)) (shiftIdx (Fin 2) n (m + 1))
    (uniformAttach (m + 1) X))
  simp only [transport_reindex, trace_reindex] at h
  rw [h, uniformAttach_trace (m + 1) m.succ_ne_zero]

theorem diag_systemToLevelOne : SystemToLevelOne diagTheory := by
  rintro O _ _ F ⟨hK, hd⟩
  obtain ⟨hcp, htr⟩ := krausFamily_cp_tr hK
  refine ⟨⟨fun a => transport_cp _ (hcp a), fun X => ?_⟩,
    fun a => preservesDiag_transport _ (hd a)⟩
  simp only [trace_transport]
  rw [htr, trace_reindex]

/-- A relabelling of the core is available in the diagonal theory: a permutation channel is
CP, trace preserving and diagonal-preserving. -/
theorem diag_relabel_available (g : Equiv.Perm Core) :
    diagTheory.availExt 4 Unit
      (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  refine ⟨⟨fun _ => ?_, fun X => ?_⟩, fun _ => preservesDiag_transport _ (preservesDiag_relabel g)⟩
  · rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
    exact conjChannel_cp _
  · rw [Fintype.sum_unique, correlationExtension_ones_eq_conjChannel, transport_conjChannel]
    exact conjChannel_trace _ (reindex_isometry _ _ (permMatrix_isometry g)) X

/-- **THE DIAGONAL THEORY REALIZES THE SEALED OI CORE.** -/
theorem diag_realizesSealedOICore : RealizesSealedOICore diagTheory := by
  refine ⟨core_isC1C4, diag_relabel_available sigmaPerm, diag_relabel_available tauPerm,
    fun r => ?_, ?_, realizedFold_diagonal⟩
  · rw [readVisible_eq_localLuders, readout_is_localLuders]
  · rw [readVisible_family_eq diagTheory]
    exact readout_relabel_available diagTheory

/-! ### Section D — no full control -/

/-- The rational rotation `[[3/5, 4/5], [-4/5, 3/5]]` on the level-one carrier. -/
noncomputable def rot : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.of fun p q =>
    if p.1 = 0 ∧ q.1 = 0 then ((3 / 5 : ℝ) : ℂ) else if p.1 = 0 ∧ q.1 = 1 then ((4 / 5 : ℝ) : ℂ)
      else if p.1 = 1 ∧ q.1 = 0 then -((4 / 5 : ℝ) : ℂ) else ((3 / 5 : ℝ) : ℂ)

theorem rot_isometry : rotᴴ * rot = 1 := by
  ext ⟨x, i⟩ ⟨y, j⟩
  fin_cases x <;> fin_cases y <;> fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      rot, Matrix.one_apply, Complex.conj_ofReal, map_div₀, map_ofNat] <;>
    norm_num

/-- The rotation creates coherence from `|0⟩⟨0|`: the off-diagonal entry is `-12/25`. -/
theorem rot_not_preservesDiag : ¬ PreservesDiag (conjChannel rot) := by
  rintro h
  obtain ⟨w', hw'⟩ := h (fun p => if p.1 = 0 then 1 else 0)
  have := congrFun (congrFun hw' (0, 0)) (1, 0)
  rw [Matrix.diagonal_apply_ne _ (by decide)] at this
  simp [conjChannel_apply, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
    rot, Matrix.conjTranspose_apply, map_div₀, map_ofNat] at this

/-- **THE DIAGONAL THEORY LACKS FULL COMPOSITE UNITARY CONTROL.** -/
theorem diag_not_control : ¬ HasCompositeUnitaryControl diagTheory :=
  fun h => rot_not_preservesDiag ((h 1 rot rot_isometry).2 ())

/-- Hence it is not exactly quantum (control is necessary). -/
theorem diag_not_exactAll : ¬ ExactAllFiniteEndomorphicQuantumOps diagTheory :=
  fun h => diag_not_control (physical_of_exactAll _ h).2.2.1

/-- **CONTROL IS INDEPENDENT** of the other four conditions and of OI realization. -/
theorem control_independent :
    ∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ HasCompositeUnitaryControl T :=
  ⟨diagTheory, diag_validity, diag_inert, diag_iteratedAncillaClosure, diag_systemToLevelOne,
    diag_realizesSealedOICore, diag_not_control⟩

/-! ### Section E — the minimality audit, frozen -/

/-- **THE MINIMALITY AUDIT.** Four of the five conditions are each independent of the other
four and of OI realization: validity (`everywhereAvailable`), inert spectators (the round-34
countermodel), full control (`diagTheory`), trivial-ancilla consistency (`systemLoose`). The
fifth cell — closure against all four others — is open: the round-38 witness fails
system-to-level-one (`admissible_not_systemToLevelOne`), while bare finite OI ⇏ closure
(round forty) stands. [CLOSED IN ROUND FORTY-FOUR: `RankGapTheory.gapTheory` closes the fifth
cell; the five-way audit is `RankGapTheory.five_way_minimality`.] -/
theorem minimality_audit :
    (∃ T : FiniteOperationalTheory (Fin 2),
      InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ CompositeOperationalValidity T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ HasCompositeUnitaryControl T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ InertSpectatorCompositionality T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T ∧ RealizesSealedOICore T
        ∧ ¬ HasCompositeUnitaryControl T)
    ∧ (∃ T : FiniteOperationalTheory (Fin 2),
      CompositeOperationalValidity T ∧ InertSpectatorCompositionality T
        ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ RealizesSealedOICore T
        ∧ ¬ SystemToLevelOne T)
    ∧ ¬ SystemToLevelOne admissibleTheory :=
  ⟨validity_independent, inert_independent, control_independent, levelOne_independent',
    admissible_not_systemToLevelOne⟩

#print axioms preservesDiag_id
#print axioms preservesDiag_zero
#print axioms preservesDiag_add
#print axioms preservesDiag_sum
#print axioms preservesDiag_comp
#print axioms reindex_diagonal
#print axioms preservesDiag_transport
#print axioms refBlockR_diagonal
#print axioms preservesDiag_amplRef
#print axioms preservesDiag_withSpectator
#print axioms preservesDiag_localLuders
#print axioms preservesDiag_relabel
#print axioms preservesDiag_conjChannel_perm
#print axioms uniformAttach_diagonal
#print axioms ptraceAnc_diagonal
#print axioms preservesDiagP_uniform
#print axioms preservesDiag_discardWith
#print axioms diag_krausSoundExt
#print axioms diag_validity
#print axioms diag_parallelReferenceExtension
#print axioms diag_inert
#print axioms preservesDiag_of_transport
#print axioms diag_iteratedAncillaClosure
#print axioms diag_systemToLevelOne
#print axioms diag_relabel_available
#print axioms diag_realizesSealedOICore
#print axioms rot_isometry
#print axioms rot_not_preservesDiag
#print axioms diag_not_control
#print axioms diag_not_exactAll
#print axioms control_independent
#print axioms minimality_audit

end DiagonalTheory
end OIBridge
