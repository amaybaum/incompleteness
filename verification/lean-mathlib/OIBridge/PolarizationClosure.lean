import OIBridge.C5Discovery
import Mathlib.Analysis.Real.Cardinality

/-!
# The polarization closure audit — O2 by counting, O1 by construction

The preregistered pass of `POLARIZATION-CLOSURE-AUDIT.md`. Nothing here is named "C5".

* T2, the counting theorem: the gate flow of an involution with a moved configuration takes
  pairwise non-proportional values at distinct times in `[0, 2)` (`gateFlow_not_proportional`);
  a class whose operators at level one are, up to scalar, drawn from a countable set generates no
  theory executing that flow (`countable_not_layerFlowExecutable`), and, contrapositively, any
  class whose theory executes a layer flow has uncountably many pairwise non-proportional
  admissible operators at level one (`uncountable_of_layerFlowExecutable`).
-/

namespace OIBridge
namespace PolarizationClosure

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open Set

/-! ### Section A — T2: the counting theorem -/

section Counting

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The two entries of the gate flow at a moved configuration, at every time. -/
theorem gateFlow_entries {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) (t : ℝ) :
    gateFlow σ t a a = (1 + Complex.exp (Real.pi * Complex.I * t)) / 2
      ∧ gateFlow σ t (σ a) a = (1 - Complex.exp (Real.pi * Complex.I * t)) / 2 := by
  simp only [gateFlow, unit, proj]
  constructor
  · simp only [Matrix.add_apply, Matrix.one_apply_eq, Matrix.smul_apply, Matrix.sub_apply,
      permMat, if_neg ha, smul_eq_mul]
    ring
  · have hne : σ a ≠ a := ha
    simp only [Matrix.add_apply, Matrix.one_apply_ne hne, Matrix.smul_apply, Matrix.sub_apply,
      permMat, smul_eq_mul, ite_true]
    ring

/-- **THE GATE FLOW IS NEVER PROPORTIONAL TO ITSELF AT ANOTHER TIME IN `[0, 2)`**, for an
involution with a moved configuration. -/
theorem gateFlow_not_proportional {σ : Equiv.Perm S} {a : S} (ha : σ a ≠ a) {t t' : ℝ}
    (ht : t ∈ Ico (0 : ℝ) 2) (ht' : t' ∈ Ico (0 : ℝ) 2) (htt' : t ≠ t') (c : ℂ) :
    gateFlow σ t ≠ c • gateFlow σ t' := by
  intro h
  obtain ⟨h1, h2⟩ := gateFlow_entries ha t
  obtain ⟨h1', h2'⟩ := gateFlow_entries ha t'
  have e1 := congrFun (congrFun h a) a
  have e2 := congrFun (congrFun h (σ a)) a
  rw [Matrix.smul_apply, smul_eq_mul, h1, h1'] at e1
  rw [Matrix.smul_apply, smul_eq_mul, h2, h2'] at e2
  set E := Complex.exp (Real.pi * Complex.I * t) with hE
  set E' := Complex.exp (Real.pi * Complex.I * t') with hE'
  have hc : c = 1 := by linear_combination -(e1 + e2)
  subst hc
  have hEE : E = E' := by linear_combination e1 - e2
  rw [hE, hE', Complex.exp_eq_exp_iff_exists_int] at hEE
  obtain ⟨n, hn⟩ := hEE
  have hre : (t : ℂ) = t' + 2 * n := by
    have hπ : (Real.pi : ℂ) * Complex.I ≠ 0 :=
      mul_ne_zero (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero) Complex.I_ne_zero
    have : (Real.pi : ℂ) * Complex.I * t = Real.pi * Complex.I * (t' + 2 * n) := by
      rw [hn]; ring
    exact mul_left_cancel₀ hπ this
  have hre' : t = t' + 2 * n := by exact_mod_cast hre
  have hlt : (n : ℝ) < 1 := by
    have := ht.2; have := ht'.1; linarith
  have hgt : (-1 : ℝ) < n := by
    have := ht.1; have := ht'.2; linarith
  have hn0 : n = 0 := by
    have h1 : n < 1 := by exact_mod_cast hlt
    have h2 : -1 < n := by exact_mod_cast hgt
    omega
  subst hn0
  apply htt'
  simpa using hre'

/-- **T2 — A CLASS COUNTABLE UP TO SCALAR AT LEVEL ONE EXECUTES NO LAYER FLOW**: the flow would
place uncountably many pairwise non-proportional unitaries in a countable set of rays. -/
theorem countable_not_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x)
    (D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ)) (hD : D.Countable)
    (hmem : ∀ K : Matrix (S × Fin 1) (S × Fin 1) ℂ, 𝓘 (S × Fin 1) K →
      ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ), M ∈ D ∧ K = c • M) :
    ¬ LayerFlowExecutable (genTheory 𝓘 arch S) σ := by
  intro hex
  have : Nonempty S := ⟨x⟩
  have hx' : levelPerm σ 1 (x, 0) ≠ (x, 0) := by
    rw [levelPerm_apply]
    intro hc
    exact hx (Prod.mk.inj hc).1
  -- for each time, a ray in `D` carrying the flow
  have hray : ∀ t : ℝ, ∃ M ∈ D, ∃ d : ℂ, gateFlow (levelPerm σ 1) t = d • M := by
    intro t
    obtain ⟨c, hc0, hcK⟩ := exists_scaled_mem_of_instAvail_unitary arch (hex 1 t)
    obtain ⟨c', M, hM, hKM⟩ := hmem _ hcK
    refine ⟨M, hM, c⁻¹ * c', ?_⟩
    calc gateFlow (levelPerm σ 1) t = c⁻¹ • (c • gateFlow (levelPerm σ 1) t) := by
          rw [smul_smul, inv_mul_cancel₀ hc0, one_smul]
      _ = c⁻¹ • (c' • M) := by rw [hKM]
      _ = (c⁻¹ * c') • M := by rw [smul_smul]
  choose f hfD hf using hray
  -- `f` is injective on `[0, 2)`
  have hinj : InjOn f (Ico (0 : ℝ) 2) := by
    intro t ht t' ht' hft
    by_contra hne
    obtain ⟨d, hd⟩ := hf t
    obtain ⟨d', hd'⟩ := hf t'
    have hd'0 : d' ≠ 0 := by
      rintro rfl
      have := congrFun (congrFun hd' (x, 0)) (x, 0)
      rw [(gateFlow_entries hx' t').1, zero_smul, Matrix.zero_apply] at this
      have h2 : Complex.exp (Real.pi * Complex.I * t') = -1 := by linear_combination 2 * this
      -- the diagonal entry vanishes only at `t' ≡ 1`; then the off-diagonal entry is `1`
      have := congrFun (congrFun hd' (levelPerm σ 1 (x, 0))) (x, 0)
      rw [(gateFlow_entries hx' t').2, zero_smul, Matrix.zero_apply, h2] at this
      norm_num at this
    apply gateFlow_not_proportional hx' ht ht' hne (d * d'⁻¹)
    rw [hd, hft, hd', smul_smul, mul_assoc, inv_mul_cancel₀ hd'0, mul_one]
  have hmaps : MapsTo f (Ico (0 : ℝ) 2) D := fun t _ => hfD t
  have hcount : (Ico (0 : ℝ) 2).Countable := hmaps.countable_of_injOn hinj hD
  have := Cardinal.le_aleph0_iff_set_countable.mpr hcount
  rw [Cardinal.mk_Ico_real (by norm_num : (0 : ℝ) < 2)] at this
  exact absurd this (not_le.mpr Cardinal.aleph0_lt_continuum)

/-- **THE NECESSARY CONDITION**: a class whose theory executes a layer flow has no countable set
of rays carrying all its level-one operators. -/
theorem uncountable_of_layerFlowExecutable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) (hex : LayerFlowExecutable (genTheory 𝓘 arch S) σ) :
    ¬ ∃ D : Set (Matrix (S × Fin 1) (S × Fin 1) ℂ), D.Countable ∧
      ∀ K : Matrix (S × Fin 1) (S × Fin 1) ℂ, 𝓘 (S × Fin 1) K →
        ∃ (c : ℂ) (M : Matrix (S × Fin 1) (S × Fin 1) ℂ), M ∈ D ∧ K = c • M :=
  fun ⟨D, hD, hmem⟩ => countable_not_layerFlowExecutable arch hx D hD hmem hex

end Counting

/-! ### Section B — T3: the relabelling-closed class and its countability up to scalar -/

section LabelInvariantClass

/-- **THE RELABELLING-CLOSED POLARIZED CLASS**: `PolGen` together with transport along every
carrier bijection, closed under the architecture operations. -/
inductive PolC : ∀ (T : Type) [Fintype T] [DecidableEq T], Matrix T T ℂ → Prop
  | perm {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : permClass T K) : PolC T K
  | shear (n : ℕ) : PolC (Fin 2 × Fin n) (siteShearImage n)
  | swap (n : ℕ) : PolC (Fin 2 × Fin n) (siteSwapImage n)
  | mul {T : Type} [Fintype T] [DecidableEq T] (K L : Matrix T T ℂ) :
      PolC T K → PolC T L → PolC T (K * L)
  | smul {T : Type} [Fintype T] [DecidableEq T] (a : ℂ) (K : Matrix T T ℂ) (ha : ‖a‖ ≤ 1) :
      PolC T K → PolC T (a • K)
  | proj {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (k : Fin m) :
      PolC (T × Fin m) (Matrix.diagonal fun r => if r.2 = k then 1 else 0)
  | block {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (K : Matrix (T × Fin m) (T × Fin m) ℂ)
      (f e : Fin m) : PolC (T × Fin m) K → PolC T (ancBlock K f e)
  | relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T')
      (K : Matrix T T ℂ) : PolC T K → PolC T' (Matrix.reindex e e K)

theorem polC_arch : Architecture PolC where
  one := fun T _ _ => PolC.perm 1 (permClass_arch.one T)
  mul := fun _ _ _ K L hK hL => PolC.mul K L hK hL
  smul := fun _ _ _ a K ha hK => PolC.smul a K ha hK
  proj := fun _ _ _ m k => PolC.proj m k
  block := fun _ _ _ m K f e hK => PolC.block m K f e hK

theorem polC_labelInvariant : LabelInvariant PolC :=
  fun _ _ _ _ _ _ e K h => PolC.relabel e K h

/-- **`PolGen ⊆ PolC`** at every carrier. -/
theorem polGen_le_polC : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ),
    PolGen T K → PolC T K := by
  intro T _ _ K h
  induction h with
  | perm K h => exact PolC.perm K h
  | shear n => exact PolC.shear n
  | swap n => exact PolC.swap n
  | mul K L _ _ ihK ihL => exact PolC.mul K L ihK ihL
  | smul a K ha _ ih => exact PolC.smul a K ha ih
  | proj m k => exact PolC.proj m k
  | block m K f e _ ih => exact PolC.block m K f e ih

/-- **THE LABEL-INVARIANT POLARIZED THEORY.** -/
noncomputable def polarizedTheoryC (S : Type) [Fintype S] [DecidableEq S] :
    FiniteOperationalTheory S :=
  genTheory PolC polC_arch S

/-- The matrices with entries in `{0, 1}`. -/
def ZeroOne (T : Type) [Fintype T] [DecidableEq T] : Set (Matrix T T ℂ) :=
  {M | ∀ i j, M i j = 0 ∨ M i j = 1}

/-- The two images, relabelled onto a carrier along every bijection from every level. -/
def ImagesAt (T : Type) [Fintype T] [DecidableEq T] : Set (Matrix T T ℂ) :=
  ⋃ (n : ℕ) (e : Fin 2 × Fin n ≃ T),
    ({Matrix.reindex e e (siteShearImage n), Matrix.reindex e e (siteSwapImage n)} :
      Set (Matrix T T ℂ))

/-- **THE DEPTH-INDEXED GENERATING SETS**, scalar-free: at depth zero the `{0,1}` matrices and the
relabelled images; at each further depth the products and the ancilla blocks from every
extension. -/
def Gen : ℕ → (T : Type) → [Fintype T] → [DecidableEq T] → Set (Matrix T T ℂ)
  | 0, T, _, _ => ZeroOne T ∪ ImagesAt T
  | k + 1, T, _, _ =>
      Gen k T ∪ Set.image2 (fun (M N : Matrix T T ℂ) => M * N) (Gen k T) (Gen k T)
        ∪ ⋃ (m : ℕ) (f : Fin m) (e : Fin m),
            (fun K : Matrix (T × Fin m) (T × Fin m) ℂ => ancBlock K f e) '' Gen k (T × Fin m)

theorem gen_succ (k : ℕ) (T : Type) [Fintype T] [DecidableEq T] :
    Gen (k + 1) T = Gen k T ∪ Set.image2 (fun (M N : Matrix T T ℂ) => M * N) (Gen k T) (Gen k T)
        ∪ ⋃ (m : ℕ) (f : Fin m) (e : Fin m),
            (fun K : Matrix (T × Fin m) (T × Fin m) ℂ => ancBlock K f e) '' Gen k (T × Fin m) := rfl

theorem gen_zero (T : Type) [Fintype T] [DecidableEq T] : Gen 0 T = ZeroOne T ∪ ImagesAt T := rfl

theorem gen_mono_succ (k : ℕ) (T : Type) [Fintype T] [DecidableEq T] : Gen k T ⊆ Gen (k + 1) T :=
  fun _ h => Or.inl (Or.inl h)

theorem gen_mono {k k' : ℕ} (h : k ≤ k') (T : Type) [Fintype T] [DecidableEq T] :
    Gen k T ⊆ Gen k' T := by
  induction h with
  | refl => exact fun _ h => h
  | step _ ih => exact fun M hM => gen_mono_succ _ T (ih hM)

theorem zeroOne_finite (T : Type) [Fintype T] [DecidableEq T] : (ZeroOne T).Finite := by
  refine (Set.finite_range (fun b : T → T → Bool =>
    (Matrix.of fun i j => if b i j then (1 : ℂ) else 0))).subset ?_
  intro M hM
  refine ⟨fun i j => decide (M i j = 1), ?_⟩
  ext i j
  rcases hM i j with h | h <;> simp [h]

theorem imagesAt_countable (T : Type) [Fintype T] [DecidableEq T] : (ImagesAt T).Countable := by
  unfold ImagesAt
  refine Set.countable_iUnion fun n => Set.countable_iUnion fun e => ?_
  exact (Set.finite_singleton _).insert _ |>.countable

/-- **EVERY DEPTH IS COUNTABLE**, at every carrier. -/
theorem gen_countable : ∀ (k : ℕ) (T : Type) [Fintype T] [DecidableEq T], (Gen k T).Countable := by
  intro k
  induction k with
  | zero =>
    intro T _ _
    exact (zeroOne_finite T).countable.union (imagesAt_countable T)
  | succ k ih =>
    intro T _ _
    rw [gen_succ]
    refine ((ih T).union ((ih T).image2 (ih T) _)).union ?_
    refine Set.countable_iUnion fun m => Set.countable_iUnion fun f => Set.countable_iUnion fun e => ?_
    exact (ih (T × Fin m)).image _

theorem reindex_reindex' {T T' T'' : Type} (e : T ≃ T') (e' : T' ≃ T'') (M : Matrix T T ℂ) :
    Matrix.reindex e' e' (Matrix.reindex e e M) = Matrix.reindex (e.trans e') (e.trans e') M := by
  ext i j
  simp [Matrix.reindex_apply, Matrix.submatrix_apply]

theorem reindex_ancBlock {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') {m : ℕ} (K : Matrix (T × Fin m) (T × Fin m) ℂ) (f e' : Fin m) :
    Matrix.reindex e e (ancBlock K f e')
      = ancBlock (Matrix.reindex (e.prodCongr (Equiv.refl (Fin m))) (e.prodCongr (Equiv.refl (Fin m))) K)
          f e' := by
  ext i j
  simp [Matrix.reindex_apply, Matrix.submatrix_apply, ancBlock]

theorem reindex_mul' {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') (M N : Matrix T T ℂ) :
    Matrix.reindex e e (M * N) = Matrix.reindex e e M * Matrix.reindex e e N := by
  simp only [Matrix.reindex_apply]
  rw [Matrix.submatrix_mul_equiv]

theorem reindex_smul' {T T' : Type} (e : T ≃ T') (c : ℂ) (M : Matrix T T ℂ) :
    Matrix.reindex e e (c • M) = c • Matrix.reindex e e M := by
  ext i j
  simp [Matrix.reindex_apply, Matrix.submatrix_apply]

theorem ancBlock_smul {T : Type} [Fintype T] [DecidableEq T] {m : ℕ} (c : ℂ)
    (K : Matrix (T × Fin m) (T × Fin m) ℂ) (f e : Fin m) :
    ancBlock (c • K) f e = c • ancBlock K f e := by
  ext i j
  simp [ancBlock]

/-- **THE DEPTHS TRANSPORT ALONG RELABELLINGS.** -/
theorem gen_reindex : ∀ (k : ℕ) (T T' : Type) [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
    (e : T ≃ T') (M : Matrix T T ℂ), M ∈ Gen k T → Matrix.reindex e e M ∈ Gen k T' := by
  intro k
  induction k with
  | zero =>
    intro T T' _ _ _ _ e M hM
    rw [gen_zero] at hM ⊢
    rcases hM with h | h
    · left
      intro i j
      simpa [Matrix.reindex_apply, Matrix.submatrix_apply] using h (e.symm i) (e.symm j)
    · right
      unfold ImagesAt at h ⊢
      simp only [Set.mem_iUnion, Set.mem_insert_iff, Set.mem_singleton_iff] at h ⊢
      obtain ⟨n, e₀, h⟩ := h
      refine ⟨n, e₀.trans e, ?_⟩
      rcases h with rfl | rfl
      · left; exact reindex_reindex' e₀ e _
      · right; exact reindex_reindex' e₀ e _
  | succ k ih =>
    intro T T' _ _ _ _ e M hM
    rw [gen_succ] at hM ⊢
    rcases hM with (h | h) | h
    · exact Or.inl (Or.inl (ih T T' e M h))
    · obtain ⟨M₁, hM₁, M₂, hM₂, rfl⟩ := h
      refine Or.inl (Or.inr ⟨_, ih T T' e M₁ hM₁, _, ih T T' e M₂ hM₂, ?_⟩)
      exact (reindex_mul' e M₁ M₂).symm
    · right
      simp only [Set.mem_iUnion, Set.mem_image] at h ⊢
      obtain ⟨m, f, e', K, hK, rfl⟩ := h
      refine ⟨m, f, e', _, ih (T × Fin m) (T' × Fin m) (e.prodCongr (Equiv.refl (Fin m))) K hK, ?_⟩
      exact (reindex_ancBlock e K f e').symm

/-- **EVERY MEMBER OF `PolC` IS A SCALAR MULTIPLE OF A MEMBER OF SOME DEPTH.** -/
theorem polC_mem_gen : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), PolC T K →
    ∃ (k : ℕ) (c : ℂ) (M : Matrix T T ℂ), M ∈ Gen k T ∧ K = c • M := by
  intro T _ _ K h
  induction h with
  | perm K h =>
    obtain ⟨_, c, _, hall⟩ := h
    refine ⟨0, c, Matrix.of fun i j => if K i j = 0 then 0 else 1, Or.inl ?_, ?_⟩
    · intro i j
      by_cases hij : K i j = 0 <;> simp [hij]
    · ext i j
      by_cases hij : K i j = 0
      · simp [hij]
      · simp [hall i j hij]
  | shear n =>
    refine ⟨0, 1, siteShearImage n, Or.inr ?_, (one_smul _ _).symm⟩
    unfold ImagesAt
    simp only [Set.mem_iUnion, Set.mem_insert_iff, Set.mem_singleton_iff]
    exact ⟨n, Equiv.refl _, Or.inl (by simp)⟩
  | swap n =>
    refine ⟨0, 1, siteSwapImage n, Or.inr ?_, (one_smul _ _).symm⟩
    unfold ImagesAt
    simp only [Set.mem_iUnion, Set.mem_insert_iff, Set.mem_singleton_iff]
    exact ⟨n, Equiv.refl _, Or.inr (by simp)⟩
  | mul K L _ _ ihK ihL =>
    obtain ⟨k₁, c₁, M₁, hM₁, rfl⟩ := ihK
    obtain ⟨k₂, c₂, M₂, hM₂, rfl⟩ := ihL
    refine ⟨max k₁ k₂ + 1, c₁ * c₂, M₁ * M₂, ?_, ?_⟩
    · rw [gen_succ]
      exact Or.inl (Or.inr ⟨M₁, gen_mono (le_max_left _ _) _ hM₁, M₂, gen_mono (le_max_right _ _) _ hM₂, rfl⟩)
    · rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  | smul a K _ _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    exact ⟨k, a * c, M, hM, by rw [smul_smul]⟩
  | proj m k =>
    refine ⟨0, 1, _, Or.inl ?_, (one_smul _ _).symm⟩
    intro i j
    by_cases hij : i = j
    · subst hij; simp only [Matrix.diagonal_apply_eq]; split_ifs <;> simp
    · simp [Matrix.diagonal_apply_ne _ hij]
  | block m K f e _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    refine ⟨k + 1, c, ancBlock M f e, ?_, ancBlock_smul c M f e⟩
    rw [gen_succ]
    right
    simp only [Set.mem_iUnion, Set.mem_image]
    exact ⟨m, f, e, M, hM, rfl⟩
  | relabel e K _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    exact ⟨k, c, Matrix.reindex e e M, gen_reindex k _ _ e M hM, reindex_smul' e c M⟩

/-- **T3 — `PolC` IS COUNTABLE UP TO SCALAR** at every carrier. -/
theorem polC_countable_upToScalar (T : Type) [Fintype T] [DecidableEq T] :
    ∃ D : Set (Matrix T T ℂ), D.Countable ∧
      ∀ K : Matrix T T ℂ, PolC T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M := by
  refine ⟨⋃ k, Gen k T, Set.countable_iUnion fun k => gen_countable k T, fun K hK => ?_⟩
  obtain ⟨k, c, M, hM, rfl⟩ := polC_mem_gen T K hK
  exact ⟨c, M, Set.mem_iUnion.mpr ⟨k, hM⟩, rfl⟩

/-- **T3 — `PolGen` IS COUNTABLE UP TO SCALAR** at every carrier. -/
theorem polGen_countable_upToScalar (T : Type) [Fintype T] [DecidableEq T] :
    ∃ D : Set (Matrix T T ℂ), D.Countable ∧
      ∀ K : Matrix T T ℂ, PolGen T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D ∧ K = c • M := by
  obtain ⟨D, hD, hmem⟩ := polC_countable_upToScalar T
  exact ⟨D, hD, fun K hK => hmem K (polGen_le_polC T K hK)⟩

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T3 — THE LABEL-INVARIANT POLARIZED THEORY EXECUTES NO LAYER FLOW.** -/
theorem polarizedTheoryC_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) :
    ¬ LayerFlowExecutable (polarizedTheoryC S) σ := by
  obtain ⟨D, hD, hmem⟩ := polC_countable_upToScalar (S × Fin 1)
  exact countable_not_layerFlowExecutable polC_arch hx D hD hmem

/-- **T3 — THE POLARIZED THEORY OF THE DISCOVERY AUDIT EXECUTES NO LAYER FLOW**, by transfer. -/
theorem polarizedTheory_not_layerFlowExecutable {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) :
    ¬ LayerFlowExecutable (polarizedTheory S) σ := by
  obtain ⟨D, hD, hmem⟩ := polGen_countable_upToScalar (S × Fin 1)
  exact countable_not_layerFlowExecutable polGen_arch hx D hD hmem

end LabelInvariantClass

/-! ### Section C — T4: O1 for the label-invariant polarized theory, by relabelling and block -/

section Phases

/-- **THE PHASE RELABELLING**: `Fin 2 × Fin (2n) ≃ (Fin 2 × Fin n) × Fin 2`, carrying the
position-one set of level `2n` onto the second ancilla fiber with the configuration `p`
exchanged into the first. -/
def phaseRelabel (n : ℕ) (p : Fin 2 × Fin n) : Fin 2 × Fin (2 * n) ≃ (Fin 2 × Fin n) × Fin 2 :=
  ((Equiv.prodComm (Fin 2) (Fin (2 * n))).trans
    ((finProdFinEquiv (m := 2) (n := n)).symm.prodCongr (Equiv.refl (Fin 2)))).trans
    (Equiv.swap (p, (0 : Fin 2)) (p, (1 : Fin 2)))

theorem phaseRelabel_symm_fst (n : ℕ) (p x : Fin 2 × Fin n) :
    ((phaseRelabel n p).symm (x, (0 : Fin 2))).1 = if x = p then 1 else 0 := by
  unfold phaseRelabel
  by_cases hxp : x = p
  · subst hxp
    simp [Equiv.swap_apply_left]
  · have h1 : (x, (0 : Fin 2)) ≠ (x, (1 : Fin 2)) := by simp
    have h2 : (x, (0 : Fin 2)) ≠ (p, (0 : Fin 2)) := by simp [hxp]
    have h3 : (x, (0 : Fin 2)) ≠ (p, (1 : Fin 2)) := by simp [hxp]
    simp [Equiv.swap_apply_of_ne_of_ne h2 h3, hxp]

/-- **THE FIRST-FIBER BLOCK OF THE RELABELLED SITE PHASE IS THE QUARTER PHASE** on the chosen
configuration. -/
theorem phaseRelabel_block (n : ℕ) (p : Fin 2 × Fin n) :
    ancBlock (Matrix.reindex (phaseRelabel n p) (phaseRelabel n p) (siteShearImage (2 * n))) 0 0
      = phaseGate p := by
  ext x y
  simp only [ancBlock, Matrix.of_apply, Matrix.reindex_apply, siteShearImage,
    Matrix.submatrix_diagonal_equiv, Matrix.diagonal_apply, Function.comp, phaseGate]
  by_cases hxy : x = y
  · subst hxy
    simp only [if_true, phaseRelabel_symm_fst]
    by_cases hxp : x = p
    · subst hxp; simp
    · simp [hxp, Ne.symm hxp]
  · have : (x, (0 : Fin 2)) ≠ (y, (0 : Fin 2)) := by simp [hxy]
    simp [hxy, this]

/-- **T4 — THE QUARTER PHASE ON EVERY CONFIGURATION OF EVERY LEVEL IS IN `PolC`.** -/
theorem polC_phaseGate (n : ℕ) (p : Fin 2 × Fin n) : PolC (Fin 2 × Fin n) (phaseGate p) := by
  rw [← phaseRelabel_block]
  exact PolC.block 2 _ 0 0 (PolC.relabel (phaseRelabel n p) _ (PolC.shear (2 * n)))

/-- **T4 — O1 HOLDS FOR THE LABEL-INVARIANT POLARIZED THEORY.** -/
theorem polarizedTheoryC_phasesAvailable : PhasesAvailable (polarizedTheoryC (Fin 2)) :=
  fun n a => SubstratumSource.genTheory_avail_conj polC_arch (polC_phaseGate n a) (phaseGate_unitary a)

end Phases

/-! ### Section D — T5: the label-invariant polarized theory satisfies the closure and is not quantum -/

section Properties

theorem siteShearImage_conjTranspose (n : ℕ) :
    (siteShearImage n)ᴴ = siteShearImage n * siteShearImage n * siteShearImage n := by
  rw [siteShearImage, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal,
    Matrix.diagonal_mul_diagonal]
  congr 1
  funext p
  simp only [Pi.star_apply]
  split_ifs <;> simp [Complex.conj_I, Complex.I_mul_I]

theorem hadamard_symm (i j : Fin 2) : hadamard j i = hadamard i j := by
  simp only [hadamard_apply, and_comm]

theorem siteSwapImage_conjTranspose (n : ℕ) : (siteSwapImage n)ᴴ = siteSwapImage n := by
  ext p q
  simp only [Matrix.conjTranspose_apply, siteSwapImage_apply, hadamard_symm]
  by_cases h : p.2 = q.2
  · simp only [h, if_true]
    simp only [hadamard_apply]
    split_ifs <;> simp [conj_hc]
  · simp [h, Ne.symm h]

theorem ancBlock_conjTranspose' {T : Type} [Fintype T] [DecidableEq T] {m : ℕ}
    (K : Matrix (T × Fin m) (T × Fin m) ℂ) (f e : Fin m) :
    (ancBlock K f e)ᴴ = ancBlock Kᴴ e f := by
  ext i j
  simp [ancBlock, Matrix.conjTranspose_apply]

/-- **`PolC` IS DAGGER-STABLE.** -/
theorem polC_daggerStable : DaggerStable PolC := by
  intro T _ _ K h
  induction h with
  | perm K h => exact PolC.perm _ (scaled_conjTranspose h)
  | shear n =>
    rw [siteShearImage_conjTranspose]
    exact PolC.mul _ _ (PolC.mul _ _ (PolC.shear n) (PolC.shear n)) (PolC.shear n)
  | swap n => rw [siteSwapImage_conjTranspose]; exact PolC.swap n
  | mul K L _ _ ihK ihL => rw [Matrix.conjTranspose_mul]; exact PolC.mul _ _ ihL ihK
  | smul a K ha _ ih =>
    rw [Matrix.conjTranspose_smul]
    exact PolC.smul _ _ (by simpa using ha) ih
  | proj m k =>
    rw [Matrix.diagonal_conjTranspose]
    have key : ∀ (U : Type) [Fintype U] [DecidableEq U],
        (star fun r : U × Fin m => if r.2 = k then (1 : ℂ) else 0)
          = fun r => if r.2 = k then (1 : ℂ) else 0 := by
      intro U _ _
      funext r; simp only [Pi.star_apply]; split_ifs <;> simp
    rw [key]
    exact PolC.proj m k
  | block m K f e _ ih => rw [ancBlock_conjTranspose']; exact PolC.block m _ e f ih
  | relabel e K _ ih => rw [Matrix.conjTranspose_reindex]; exact PolC.relabel e _ ih

/-- The context relabelling `Fin 2 × Fin (|R| n) ≃ R × (Fin 2 × Fin n)`, preserving the position
coordinate. -/
noncomputable def ctxRelabel (R : Type) [Fintype R] [DecidableEq R] (n : ℕ) :
    Fin 2 × Fin (Fintype.card R * n) ≃ R × (Fin 2 × Fin n) :=
  (((Equiv.refl (Fin 2)).prodCongr
      ((finProdFinEquiv (m := Fintype.card R) (n := n)).symm.trans
        ((Fintype.equivFin R).symm.prodCongr (Equiv.refl (Fin n))))).trans
    (Equiv.prodAssoc (Fin 2) R (Fin n)).symm).trans
    (((Equiv.prodComm (Fin 2) R).prodCongr (Equiv.refl (Fin n))).trans (Equiv.prodAssoc R (Fin 2) (Fin n)))

theorem ctxRelabel_symm_apply (R : Type) [Fintype R] [DecidableEq R] (n : ℕ) (r : R) (s : Fin 2)
    (k : Fin n) :
    (ctxRelabel R n).symm (r, (s, k)) = (s, finProdFinEquiv (Fintype.equivFin R r, k)) := by
  simp [ctxRelabel]

theorem tensorOf_one_siteShearImage (R : Type) [Fintype R] [DecidableEq R] (n : ℕ) :
    tensorOf (1 : Matrix R R ℂ) (siteShearImage n)
      = Matrix.reindex (ctxRelabel R n) (ctxRelabel R n) (siteShearImage (Fintype.card R * n)) := by
  ext ⟨r, s, k⟩ ⟨r', s', k'⟩
  simp only [tensorOf_apply, siteShearImage, Matrix.reindex_apply, Matrix.submatrix_diagonal_equiv,
    Matrix.diagonal_apply, Function.comp, ctxRelabel_symm_apply, Matrix.one_apply]
  by_cases hr : r = r'
  · subst hr
    by_cases hsk : (s, k) = (s', k')
    · obtain ⟨rfl, rfl⟩ := Prod.mk.inj hsk
      simp
    · have : (s, finProdFinEquiv (Fintype.equivFin R r, k)) ≠ (s', finProdFinEquiv (Fintype.equivFin R r, k')) := by
        intro h
        apply hsk
        have h1 := (Prod.mk.inj h).1
        have h2 := finProdFinEquiv.injective (Prod.mk.inj h).2
        exact Prod.ext h1 (Prod.mk.inj h2).2
      simp [hsk]
  · have : (s, finProdFinEquiv (Fintype.equivFin R r, k)) ≠ (s', finProdFinEquiv (Fintype.equivFin R r', k')) := by
      intro h
      apply hr
      have h2 := finProdFinEquiv.injective (Prod.mk.inj h).2
      exact (Fintype.equivFin R).injective (Prod.mk.inj h2).1
    simp [hr]

theorem tensorOf_one_siteSwapImage (R : Type) [Fintype R] [DecidableEq R] (n : ℕ) :
    tensorOf (1 : Matrix R R ℂ) (siteSwapImage n)
      = Matrix.reindex (ctxRelabel R n) (ctxRelabel R n) (siteSwapImage (Fintype.card R * n)) := by
  ext ⟨r, s, k⟩ ⟨r', s', k'⟩
  simp only [tensorOf_apply, siteSwapImage_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    ctxRelabel_symm_apply, Matrix.one_apply]
  by_cases hr : r = r'
  · subst hr
    by_cases hk : k = k'
    · subst hk; simp
    · have : finProdFinEquiv (Fintype.equivFin R r, k) ≠ finProdFinEquiv (Fintype.equivFin R r, k') := by
        intro h; apply hk; exact (Prod.mk.inj (finProdFinEquiv.injective h)).2
      simp [hk, this]
  · have : finProdFinEquiv (Fintype.equivFin R r, k) ≠ finProdFinEquiv (Fintype.equivFin R r', k') := by
      intro h; apply hr
      exact (Fintype.equivFin R).injective (Prod.mk.inj (finProdFinEquiv.injective h)).1
    simp [hr, this]

theorem tensorOf_one_diagonal {R T : Type} [Fintype R] [DecidableEq R] [Fintype T] [DecidableEq T]
    (d : T → ℂ) :
    tensorOf (1 : Matrix R R ℂ) (Matrix.diagonal d) = Matrix.diagonal fun p : R × T => d p.2 := by
  ext ⟨r, x⟩ ⟨r', y⟩
  simp only [tensorOf_apply, Matrix.one_apply, Matrix.diagonal_apply]
  by_cases hr : r = r' <;> by_cases hx : x = y <;> simp [hr, hx, Prod.ext_iff]

theorem tensorOf_one_ancBlock {R T : Type} [Fintype R] [DecidableEq R] [Fintype T] [DecidableEq T]
    {m : ℕ} (K : Matrix (T × Fin m) (T × Fin m) ℂ) (f e : Fin m) :
    tensorOf (1 : Matrix R R ℂ) (ancBlock K f e)
      = ancBlock (Matrix.reindex (Equiv.prodAssoc R T (Fin m)).symm (Equiv.prodAssoc R T (Fin m)).symm
          (tensorOf (1 : Matrix R R ℂ) K)) f e := by
  ext ⟨r, x⟩ ⟨r', y⟩
  simp [tensorOf_apply, ancBlock, Matrix.reindex_apply, Matrix.submatrix_apply]

/-- **`PolC` IS CONTEXT-STABLE**: the identity tensored with an image is a relabelled image of a
higher level. -/
theorem polC_contextStable : ContextStable PolC := by
  intro R T _ _ _ _ K h
  induction h with
  | perm K h => exact PolC.perm _ (scaled_tensor_one h)
  | shear n => rw [tensorOf_one_siteShearImage]; exact PolC.relabel _ _ (PolC.shear _)
  | swap n => rw [tensorOf_one_siteSwapImage]; exact PolC.relabel _ _ (PolC.swap _)
  | mul K L _ _ ihK ihL =>
    have key := tensorOf_mul' (1 : Matrix R R ℂ) (1 : Matrix R R ℂ) K L
    rw [Matrix.one_mul] at key
    rw [← key]
    exact PolC.mul _ _ ihK ihL
  | smul a K ha _ ih => rw [tensorOf_smul_right]; exact PolC.smul _ _ ha ih
  | proj m k =>
    rw [tensorOf_one_diagonal]
    exact PolC.perm _ (scaled_diagonal_indicator _)
  | block m K f e _ ih =>
    rw [tensorOf_one_ancBlock]
    exact PolC.block m _ f e (PolC.relabel _ _ ih)
  | relabel e K _ ih => rw [tensorOf_one_reindex]; exact PolC.relabel _ _ ih

/-- **T5 — THE LABEL-INVARIANT POLARIZED THEORY SATISFIES THE CLOSURE `DerivedOI`**, the phases
by T4. -/
theorem polarizedTheoryC_derivedOI : DerivedOI (polarizedTheoryC (Fin 2)) :=
  ⟨genTheory_reversibleImplementationLocality PolC polC_arch polC_contextStable polC_labelInvariant
      polC_daggerStable,
    genTheory_embeddedObservation PolC polC_arch polC_labelInvariant,
    fun _ a b => SubstratumSource.genTheory_avail_conj polC_arch
      (PolC.perm _ (permClass_permMatrix (Equiv.swap a b))) (permMatrix_isometry _),
    polarizedTheoryC_phasesAvailable,
    fun _ _ _ F l => by
      rw [ReadWriteControl.readWriteOperator_eq_perm]
      exact SubstratumSource.genTheory_avail_conj polC_arch
        (PolC.perm _ (permClass_permMatrix (F.couple l))) (permMatrix_isometry _)⟩

/-- **T5 — IT IS NOT QUANTUM MECHANICS**: the closure with an executable flow would be quantum
mechanics, and no layer flow is executable. -/
theorem polarizedTheoryC_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (polarizedTheoryC (Fin 2)) := by
  intro h
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  exact polarizedTheoryC_not_layerFlowExecutable (x := (0 : Fin 2)) (by simp)
    (derivedOI_layerFlowExecutable_of_qm _ h hσ).2

/-- **THE KILL BATTERY, EXTENDED** by the label-invariant polarized theory. -/
def KillBattery' (T : FiniteOperationalTheory (Fin 2)) : Prop :=
  KillBattery T ∨ T = polarizedTheoryC (Fin 2)

theorem killBattery'_not_qm {T : FiniteOperationalTheory (Fin 2)} (h : KillBattery' T) :
    ¬ ExactAllFiniteEndomorphicQuantumOps T := by
  rcases h with h | rfl
  · exact killBattery_not_qm h
  · exact polarizedTheoryC_not_qm

end Properties

/-! ### Section E — T6: the level-three word and its non-Clifford fiber block -/

section LevelThree

/-- The exchange cycling the three configurations with position one at level three. -/
def cycleP : Equiv.Perm (Fin 2 × Fin 3) :=
  (Equiv.swap ((1 : Fin 2), (1 : Fin 3)) (1, 2)).trans (Equiv.swap ((1 : Fin 2), (0 : Fin 3)) (1, 1))

/-- The level-three word `H · P · H · P · H`. -/
noncomputable def levelThreeWord : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ :=
  siteSwapImage 3 * permMatrix cycleP * siteSwapImage 3 * permMatrix cycleP * siteSwapImage 3

theorem levelThreeWord_mem : PolGen (Fin 2 × Fin 3) levelThreeWord :=
  PolGen.mul _ _ (PolGen.mul _ _ (PolGen.mul _ _ (PolGen.mul _ _ (PolGen.swap 3)
    (PolGen.perm _ (permClass_permMatrix _))) (PolGen.swap 3))
    (PolGen.perm _ (permClass_permMatrix _))) (PolGen.swap 3)

/-- The relabelling of level three as `(Fin 2 × Fin 1) × Fin 3` with the fibers
`{(0,0),(1,1)}`, `{(0,2),(1,0)}`, `{(0,1),(1,2)}`. -/
def fiberRelabel : Fin 2 × Fin 3 ≃ (Fin 2 × Fin 1) × Fin 3 where
  toFun p := match p with
    | (0, 0) => ((0, 0), 0) | (1, 1) => ((1, 0), 0)
    | (0, 2) => ((0, 0), 1) | (1, 0) => ((1, 0), 1)
    | (0, 1) => ((0, 0), 2) | (1, 2) => ((1, 0), 2)
  invFun q := match q with
    | ((0, _), 0) => (0, 0) | ((1, _), 0) => (1, 1)
    | ((0, _), 1) => (0, 2) | ((1, _), 1) => (1, 0)
    | ((0, _), 2) => (0, 1) | ((1, _), 2) => (1, 2)
  left_inv := by decide
  right_inv := by decide

theorem mul_permMatrix_apply {T : Type} [Fintype T] [DecidableEq T] (M : Matrix T T ℂ)
    (σ : Equiv.Perm T) (i j : T) : (M * permMatrix σ) i j = M i (σ j) := by
  rw [Matrix.mul_apply]
  simp only [permMatrix, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_ite_eq]
  simp

theorem hc_cube : hc ^ 3 = hc / 2 := by
  have := hc_mul_hc
  linear_combination hc * this

/-- The word as a double sum, the permutation factors consumed as index shifts. -/
theorem levelThreeWord_apply (p q : Fin 2 × Fin 3) :
    levelThreeWord p q
      = ∑ b, (∑ a, siteSwapImage 3 p (cycleP a) * siteSwapImage 3 a (cycleP b))
          * siteSwapImage 3 b q := by
  unfold levelThreeWord
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [mul_permMatrix_apply, Matrix.mul_apply]
  refine congrArg (· * _) (Finset.sum_congr rfl fun a _ => ?_)
  rw [mul_permMatrix_apply]

/-- The reflection direction of the block, `[[1, 1/2], [1/2, −1]]`, proportional to
`(1/√5) · [[2, 1], [1, −2]]`. -/
noncomputable def refl25 : Matrix (Fin 2) (Fin 2) ℂ := !![(1 : ℂ), 1 / 2; 1 / 2, -1]

/-- The block, as a matrix on the level-one carrier. -/
noncomputable def levelThreeBlock : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  hc • Matrix.of fun x y => refl25 x.1 y.1

/-- **T6 — THE FIBER BLOCK OF THE LEVEL-THREE WORD**: `hc · [[1, 1/2], [1/2, −1]]`, proportional
to the reflection `(1/√5) · [[2, 1], [1, −2]]`. -/
theorem levelThree_word_block :
    ancBlock (Matrix.reindex fiberRelabel fiberRelabel levelThreeWord) 0 1 = levelThreeBlock := by
  ext ⟨x, k⟩ ⟨y, l⟩
  have hk : k = 0 := Subsingleton.elim _ _
  have hl : l = 0 := Subsingleton.elim _ _
  subst hk hl
  simp only [ancBlock, Matrix.of_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    levelThreeWord_apply, levelThreeBlock, refl25, Matrix.smul_apply, smul_eq_mul]
  fin_cases x <;> fin_cases y <;>
    simp [fiberRelabel, Fintype.sum_prod_type, Fin.sum_univ_two,
      siteSwapImage_apply, hadamard_apply, cycleP, Equiv.swap_apply_def] <;>
    ring_nf <;> simp only [hc_cube] <;> ring

theorem levelThree_block_ne_zero : levelThreeBlock ≠ 0 := by
  intro h
  have := congrFun (congrFun h (0, 0)) (0, 0)
  simp [levelThreeBlock, refl25] at this
  exact hc_ne_zero this

/-- **T6 — THE BLOCK IS NOT CLIFFORD**: its unitary direction conjugates `Z` to a matrix that is
not a Pauli up to phase, its off-diagonal entries being nonzero while its diagonal is nonzero. -/
theorem levelThree_block_not_clifford :
    let Z : Matrix (Fin 2) (Fin 2) ℂ := !![(1 : ℂ), 0; 0, -1]
    (refl25 * Z * refl25ᴴ) 0 0 ≠ 0 ∧ (refl25 * Z * refl25ᴴ) 0 1 ≠ 0 := by
  intro Z
  refine ⟨?_, ?_⟩ <;> norm_num [refl25, Z, Matrix.mul_apply, Fin.sum_univ_two, map_ofNat]

/-- **T6 — THE BLOCK LIES IN `PolC` AT LEVEL ONE**, with the fiber structure relabelled. -/
theorem polC_levelThree_block : PolC (Fin 2 × Fin 1) levelThreeBlock := by
  rw [← levelThree_word_block]
  exact PolC.block 3 _ 0 1 (PolC.relabel fiberRelabel _ (polGen_le_polC _ _ levelThreeWord_mem))

end LevelThree

#print axioms gateFlow_entries
#print axioms gateFlow_not_proportional
#print axioms countable_not_layerFlowExecutable
#print axioms uncountable_of_layerFlowExecutable
#print axioms polC_arch
#print axioms polC_labelInvariant
#print axioms polGen_le_polC
#print axioms gen_countable
#print axioms gen_reindex
#print axioms polC_mem_gen
#print axioms polC_countable_upToScalar
#print axioms polGen_countable_upToScalar
#print axioms polarizedTheoryC_not_layerFlowExecutable
#print axioms polarizedTheory_not_layerFlowExecutable
#print axioms phaseRelabel_block
#print axioms polC_phaseGate
#print axioms polarizedTheoryC_phasesAvailable
#print axioms polC_daggerStable
#print axioms polC_contextStable
#print axioms polarizedTheoryC_derivedOI
#print axioms polarizedTheoryC_not_qm
#print axioms killBattery'_not_qm
#print axioms levelThreeWord_mem
#print axioms levelThree_word_block
#print axioms levelThree_block_not_clifford
#print axioms polC_levelThree_block

end PolarizationClosure
end OIBridge
