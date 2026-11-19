import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.Topology.MetricSpace.Pseudo.Pi
import OIBridge.MeasuredReciprocity
import OIBridge.RecurrenceHorizon

/-!
# A1-RIGID-1: observable recurrence and rooted P-indivisibility

A finite measurable readout of a probability-preserving bimeasurable bijection has
simultaneous near-returns, with bounded gaps at each fixed tolerance, if the joint
forward orbit of its cell indicators has compact closure in real L². The same
invariant law defines every rooted transition. An earlier overlap and a later
near-return then give a strict total-variation revival on a finite horizon.

This is the conditional theorem of the A1-RIGID-1 paper preserved by #1396.
The two controls below concern the matrices of the paper's examples. The
measurable realizations and physical selection of a preparation law are separate.
-/

open Filter Finset Matrix MeasureTheory Set
open scoped BigOperators ENNReal Topology RealInnerProductSpace

namespace OIBridge.ObservableRigidity

open CausalReadback HiddenMemory MeasuredReciprocity RecurrenceHorizon

noncomputable section

set_option autoImplicit false

private theorem bounded_gap_return {E : Type*} [PseudoMetricSpace E]
    (f : E → E) (hf : Isometry f) (x : E)
    (hcompact : IsCompact (closure (Set.range fun m : ℕ => (f^[m]) x)))
    {ε : ℝ} (hε : 0 < ε) :
    ∃ M : ℕ, ∀ q : ℕ, ∃ n : ℕ, q ≤ n ∧ n ≤ q + M ∧ dist ((f^[n]) x) x < ε := by
  obtain ⟨centres, hsubset, hfinite, hcover⟩ :=
    exists_finite_cover_balls_of_isCompact_closure hcompact hε
  have hindex : ∀ y : centres, ∃ m : ℕ, (f^[m]) x = (y : E) := fun y => hsubset y.property
  choose index hindex using hindex
  letI : Fintype centres := hfinite.fintype
  let M := (Finset.univ : Finset centres).sup index
  refine ⟨M, fun q => ?_⟩
  obtain ⟨y, hy⟩ := Set.mem_iUnion.mp (hcover (Set.mem_range_self (q + M)))
  obtain ⟨hyc, hball⟩ := Set.mem_iUnion.mp hy
  let m := index ⟨y, hyc⟩
  let n := q + M - m
  have hm : m ≤ M := Finset.le_sup (f := index) (Finset.mem_univ (⟨y, hyc⟩ : centres))
  have htime : q + M = m + n := by dsimp [n]; omega
  have hdist : dist ((f^[q + M]) x) y < ε := Metric.mem_ball.mp hball
  rw [← hindex ⟨y, hyc⟩, htime, Function.iterate_add_apply, (hf.iterate m).dist_eq] at hdist
  exact ⟨n, by dsimp [n]; omega, Nat.sub_le _ _, hdist⟩

section Matrix

variable {V : Type*} [Fintype V] [DecidableEq V]

private theorem entry_le_one {M : Matrix V V ℝ} (hM : IsRowStochastic M) (a b : V) :
    M a b ≤ 1 := by
  rw [← hM.2 a]
  exact Finset.single_le_sum (fun j _ => hM.1 a j) (Finset.mem_univ b)

private theorem offDiagonal_le_deficit {M : Matrix V V ℝ} (hM : IsRowStochastic M) {a b : V}
    (hab : a ≠ b) : M a b ≤ 1 - M a a := by
  have hsum := Finset.sum_erase_add Finset.univ (M a) (Finset.mem_univ a)
  have hentry : M a b ≤ ∑ j ∈ Finset.univ.erase a, M a j :=
    Finset.single_le_sum (fun j _ => hM.1 a j) (by simpa using hab.symm)
  rw [hM.2 a] at hsum
  linarith

private theorem tv_ge_coordinate_difference {p q : V → ℝ}
    (hp : ∑ j, p j = 1) (hq : ∑ j, q j = 1) (a : V) :
    p a - q a ≤ tv p q := by
  have hsum := Finset.sum_erase_add Finset.univ p (Finset.mem_univ a)
  have hoverlap : (∑ j, min (p j) (q j)) ≤ (∑ j ∈ Finset.univ.erase a, p j) + q a := by
    rw [← Finset.sum_erase_add Finset.univ (fun j => min (p j) (q j)) (Finset.mem_univ a)]
    exact add_le_add (Finset.sum_le_sum fun j _ => min_le_left (p j) (q j)) (min_le_right _ _)
  rw [tv_eq_one_sub_sum_min hp hq]
  linarith

/-- The later sum of the two diagonal deficits must be strictly below one earlier shared mass. -/
theorem tv_revives_of_nearReturn {Γ : ℕ → Matrix V V ℝ} {s n : ℕ} {a b x : V}
    (hsto_s : IsRowStochastic (Γ s)) (hsto_n : IsRowStochastic (Γ n)) (hab : a ≠ b)
    (hmargin : (1 - Γ n a a) + (1 - Γ n b b) < min (Γ s a x) (Γ s b x)) :
    tv (Γ s a) (Γ s b) < tv (Γ n a) (Γ n b) := by
  have hearly := tv_le_one_sub_min (hsto_s.1 a) (hsto_s.1 b) (hsto_s.2 a) (hsto_s.2 b) x
  have hlate := tv_ge_coordinate_difference (hsto_n.2 a) (hsto_n.2 b) a
  have hoff := offDiagonal_le_deficit hsto_n hab.symm
  linarith

/-- A non-permutation among finite square stochastic matrices has two overlapping rows. -/
theorem overlap_of_nonPermutation {A : Matrix V V ℝ} (hA : IsRowStochastic A)
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, A = σ.permMatrix ℝ) :
    ∃ a b x : V, a ≠ b ∧ 0 < A a x ∧ 0 < A b x := by
  by_contra hno
  have hdisjoint {a b x : V} (ha : 0 < A a x) (hb : 0 < A b x) : a = b := by
    by_contra hab
    exact hno ⟨a, b, x, hab, ha, hb⟩
  have hpos : ∀ a : V, ∃ x : V, 0 < A a x := by
    intro a
    by_contra h
    have hz (x : V) : A a x = 0 := le_antisymm (le_of_not_gt fun hx => h ⟨x, hx⟩) (hA.1 a x)
    simpa [hz] using hA.2 a
  choose column hcolumn using hpos
  have hinj : Function.Injective column := by
    intro a b hab
    exact hdisjoint (hab ▸ hcolumn a) (hcolumn b)
  let σ : Equiv.Perm V := Equiv.ofBijective column (Finite.injective_iff_bijective.mp hinj)
  have hzero (a x : V) (hx : x ≠ column a) : A a x = 0 := by
    refine le_antisymm (le_of_not_gt ?_) (hA.1 a x)
    intro hax
    obtain ⟨b, hb⟩ := σ.surjective x
    change column b = x at hb
    have hab : a = b := hdisjoint hax (hb ▸ hcolumn b)
    exact hx (hb.symm.trans (congrArg column hab.symm))
  have hone (a : V) : A a (column a) = 1 := by
    have hsum := hA.2 a
    rwa [Finset.sum_eq_single (column a) (fun j _ hj => hzero a j hj)
      (fun hj => absurd (Finset.mem_univ (column a)) hj)] at hsum
  apply hnonperm
  refine ⟨σ, ?_⟩
  ext a x
  by_cases hx : x = column a
  · subst x
    simp [σ, Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, hone]
  · simp [σ, Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, hzero a x hx,
      Ne.symm hx]

end Matrix

section Measured

variable {S V : Type*} [MeasurableSpace S] [MeasurableSpace V] [MeasurableSingletonClass V]

/-- The rooted transition matrices for one probability and one measurable bijection. -/
def rootedFamily (μ : ProbabilityMeasure S) (X : S → V) (T : S ≃ᵐ S)
    (hpos : ∀ a, 0 < rootMass μ X a) (n : ℕ) : Matrix V V ℝ :=
  fun a b => transition μ X T.toEquiv n a b (hpos a)

variable (μ : ProbabilityMeasure S) (X : S → V) (T : S ≃ᵐ S)
variable (hX : Measurable X) (hT : MeasurePreserving T (μ : Measure S) (μ : Measure S))
variable (hpos : ∀ a, 0 < rootMass μ X a)

private theorem preserving_pow (n : ℕ) :
    MeasurePreserving (⇑(T.toEquiv ^ n)) (μ : Measure S) (μ : Measure S) := by
  simpa only [Equiv.Perm.coe_pow] using hT.iterate n

/-- Finite additivity across the endpoint cells gives the row normalization. -/
theorem rootedFamily_isRowStochastic [Fintype V] (n : ℕ) :
    IsRowStochastic (rootedFamily μ X T hpos n) := by
  refine ⟨fun a b => div_nonneg ENNReal.toReal_nonneg (hpos a).le, fun a => ?_⟩
  have hmeas (b : V) : MeasurableSet (endpointEvent X T.toEquiv n a b) :=
    ((measurableSet_singleton a).preimage hX).inter
      ((measurableSet_singleton b).preimage (hX.comp (preserving_pow μ T hT n).measurable))
  have hdisj : Pairwise (fun b c : V =>
      Disjoint (endpointEvent X T.toEquiv n a b) (endpointEvent X T.toEquiv n a c)) := by
    intro b c hbc
    exact Set.disjoint_left.mpr fun _ hb hc => hbc (hb.2.symm.trans hc.2)
  have hunion : ⋃ b, endpointEvent X T.toEquiv n a b = X ⁻¹' {a} := by
    ext s
    constructor
    · intro hs
      obtain ⟨_, hb⟩ := Set.mem_iUnion.mp hs
      exact hb.1
    · intro hs
      exact Set.mem_iUnion.mpr ⟨X ((T.toEquiv ^ n) s), hs, rfl⟩
  have hsum : (∑ b, flux μ X T.toEquiv n a b) = rootMass μ X a := by
    change (∑ b, (μ : Measure S).real (endpointEvent X T.toEquiv n a b)) =
      (μ : Measure S).real (X ⁻¹' {a})
    rw [← measureReal_iUnion_fintype hdisj hmeas, hunion]
  change (∑ b, flux μ X T.toEquiv n a b / rootMass μ X a) = 1
  rw [← Finset.sum_div, hsum, div_self (hpos a).ne']

/-- The measured rooted family starts at the identity. -/
theorem rootedFamily_zero [DecidableEq V] : rootedFamily μ X T hpos 0 = 1 := by
  ext a b
  rw [Matrix.one_apply]
  change flux μ X T.toEquiv 0 a b / rootMass μ X a = _
  split_ifs with hab
  · subst b
    have hevent : endpointEvent X T.toEquiv 0 a a = X ⁻¹' {a} := by simp [endpointEvent]
    have hflux : flux μ X T.toEquiv 0 a a = rootMass μ X a := by
      rw [flux, hevent, rootMass]
    exact hflux ▸ div_self (hpos a).ne'
  · have hevent : endpointEvent X T.toEquiv 0 a b = ∅ := by
      ext s
      simp only [endpointEvent, pow_zero, Equiv.Perm.one_apply, Set.mem_inter_iff,
        Set.mem_preimage, Set.mem_singleton_iff, Set.notMem_empty, iff_false]
      exact fun h => hab (h.1.symm.trans h.2)
    simp [flux, hevent]

/-- The real L² indicator of the readout cell. -/
def visibleIndicator (a : V) : Lp ℝ 2 (μ : Measure S) :=
  indicatorConstLp 2 ((measurableSet_singleton a).preimage hX) (measure_ne_top _ _) 1

private def indicatorStep (f : V → Lp ℝ 2 (μ : Measure S)) (a : V) : Lp ℝ 2 (μ : Measure S) :=
  Lp.compMeasurePreserving T hT (f a)

/-- Joint forward orbit under the Koopman map acting on each indicator. -/
def jointIndicatorOrbit (n : ℕ) : V → Lp ℝ 2 (μ : Measure S) :=
  ((indicatorStep μ T hT)^[n]) (visibleIndicator μ X hX)

private theorem indicatorStep_isometry [Fintype V] : Isometry (indicatorStep (V := V) μ T hT) := by
  refine Isometry.of_dist_eq fun f g => ?_
  simp only [dist_pi_def, indicatorStep, (Lp.isometry_compMeasurePreserving (E := ℝ) (p := 2) hT).nndist_eq]

private theorem jointIndicatorOrbit_apply (n : ℕ) (a : V) :
    jointIndicatorOrbit μ X T hX hT n a =
      indicatorConstLp 2 (((measurableSet_singleton a).preimage hX).preimage
        (preserving_pow μ T hT n).measurable) (measure_ne_top _ _) 1 := by
  have hproj : Function.Semiconj (fun f : V → Lp ℝ 2 (μ : Measure S) => f a)
      (indicatorStep μ T hT) (Lp.compMeasurePreserving T hT) := fun _ => rfl
  change ((indicatorStep μ T hT)^[n]) (visibleIndicator μ X hX) a = _
  rw [hproj.iterate_right n (visibleIndicator μ X hX), Lp.compMeasurePreserving_iterate]
  simp only [visibleIndicator, indicatorConstLp_compMeasurePreserving, Equiv.Perm.coe_pow]

/-- Invariance gives the exact squared L² norm formula for a diagonal deficit. -/
theorem sq_norm_indicator_sub_eq_deficit (n : ℕ) (a : V) :
    ‖jointIndicatorOrbit μ X T hX hT n a - visibleIndicator μ X hX a‖ ^ 2 =
      2 * rootMass μ X a * (1 - rootedFamily μ X T hpos n a a) := by
  have hA := (measurableSet_singleton a).preimage hX
  have hself (t : Set S) (ht : MeasurableSet t) :
      ‖indicatorConstLp (μ := (μ : Measure S)) 2 ht (measure_ne_top _ _) (1 : ℝ)‖ ^ 2 =
        (μ : Measure S).real t := by
    simpa only [real_inner_self_eq_norm_sq, Set.inter_self] using
      (L2.real_inner_indicatorConstLp_one_indicatorConstLp_one (μ := (μ : Measure S)) ht ht)
  have hbase : ‖visibleIndicator μ X hX a‖ ^ 2 = rootMass μ X a :=
    hself _ hA
  have hnow : ‖jointIndicatorOrbit μ X T hX hT n a‖ ^ 2 = rootMass μ X a := by
    rw [jointIndicatorOrbit_apply, hself]
    change ((μ : Measure S) ((⇑(T.toEquiv ^ n)) ⁻¹' (X ⁻¹' {a}))).toReal =
      ((μ : Measure S) (X ⁻¹' {a})).toReal
    rw [(preserving_pow μ T hT n).measure_preimage hA.nullMeasurableSet]
  have hcross : ⟪jointIndicatorOrbit μ X T hX hT n a, visibleIndicator μ X hX a⟫_ℝ =
      flux μ X T.toEquiv n a a := by
    rw [jointIndicatorOrbit_apply, visibleIndicator,
      L2.real_inner_indicatorConstLp_one_indicatorConstLp_one, Set.inter_comm]
    rfl
  rw [norm_sub_sq_real, hnow, hcross, hbase]
  change _ = 2 * rootMass μ X a * (1 - flux μ X T.toEquiv n a a / rootMass μ X a)
  field_simp [(hpos a).ne'] <;> ring

variable [Fintype V]
variable (hcard : 2 ≤ Fintype.card V)
variable (hcompact : IsCompact (closure (Set.range (jointIndicatorOrbit μ X T hX hT))))

/-- At each positive tolerance one gap bound works for every starting time and every root. -/
theorem exists_bounded_gap_nearReturn {ε : ℝ} (hε : 0 < ε) :
    ∃ M : ℕ, ∀ q : ℕ, 1 ≤ q → ∃ n : ℕ, q ≤ n ∧ n ≤ q + M ∧
      ∀ a : V, 1 - rootedFamily μ X T hpos n a a < ε := by
  letI : Nonempty V := Fintype.card_pos_iff.mp (by omega)
  obtain ⟨a₀, _, hmin⟩ := Finset.exists_min_image Finset.univ (rootMass μ X)
    Finset.univ_nonempty
  let δ := Real.sqrt (2 * rootMass μ X a₀ * ε)
  have hδ_arg : 0 < 2 * rootMass μ X a₀ * ε := mul_pos (mul_pos (by norm_num) (hpos a₀)) hε
  have hδ : 0 < δ := Real.sqrt_pos.2 hδ_arg
  have hδ_sq : δ ^ 2 = 2 * rootMass μ X a₀ * ε := Real.sq_sqrt hδ_arg.le
  obtain ⟨M, hM⟩ := bounded_gap_return (indicatorStep μ T hT) (indicatorStep_isometry μ T hT)
    (visibleIndicator μ X hX) hcompact hδ
  refine ⟨M, fun q _ => ?_⟩
  obtain ⟨n, hqn, hnM, hn⟩ := hM q
  refine ⟨n, hqn, hnM, fun a => ?_⟩
  have hnorm : ‖jointIndicatorOrbit μ X T hX hT n a - visibleIndicator μ X hX a‖ < δ := by
    apply (dist_pi_lt_iff hδ).mp at hn
    simpa only [dist_eq_norm, jointIndicatorOrbit] using hn a
  have hsq := (sq_lt_sq₀ (norm_nonneg _) hδ.le).mpr hnorm
  rw [sq_norm_indicator_sub_eq_deficit, hδ_sq] at hsq
  have hscale : 2 * rootMass μ X a₀ * ε ≤ 2 * rootMass μ X a * ε :=
    mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left (hmin a (Finset.mem_univ a)) (by norm_num))
      hε.le
  exact (mul_lt_mul_left₀ (mul_pos (by norm_num) (hpos a))).mp (hsq.trans_le hscale)

variable [DecidableEq V]

/-- A strictly increasing sequence of simultaneous returns gives entrywise convergence to I. -/
theorem exists_strictMono_rootedFamily_tendsto_one :
    ∃ ns : ℕ → ℕ, StrictMono ns ∧ ∀ a b : V,
      Tendsto (fun k => rootedFamily μ X T hpos (ns k) a b) atTop (𝓝 ((1 : Matrix V V ℝ) a b)) := by
  let Γ := rootedFamily μ X T hpos
  have hchoose (k prev : ℕ) : ∃ n : ℕ, prev < n ∧ ∀ a : V, 1 - Γ n a a < 1 / ((k : ℝ) + 1) := by
    have hε : 0 < (1 : ℝ) / ((k : ℝ) + 1) := by positivity
    obtain ⟨M, hM⟩ := exists_bounded_gap_nearReturn μ X T hX hT hpos hcard hcompact hε
    obtain ⟨n, hqn, _, hn⟩ := hM (prev + 1) (by omega)
    exact ⟨n, by omega, hn⟩
  choose next hnext hreturn using hchoose
  let ns : ℕ → ℕ := Nat.rec (next 0 0) (fun k n => next (k + 1) n)
  have hmono : StrictMono ns := strictMono_nat_of_lt_succ fun k => hnext (k + 1) (ns k)
  have hdeficit (k : ℕ) (a : V) : 1 - Γ (ns k) a a < 1 / ((k : ℝ) + 1) := by
    cases k with
    | zero => exact hreturn 0 0 a
    | succ k => exact hreturn (k + 1) (ns k) a
  have hstoch (n : ℕ) := rootedFamily_isRowStochastic μ X T hX hT hpos n
  have htol : Tendsto (fun k : ℕ => (1 : ℝ) / ((k : ℝ) + 1)) atTop (𝓝 0) :=
    tendsto_one_div_add_atTop_nhds_zero_nat
  have hzero (a : V) : Tendsto (fun k => 1 - Γ (ns k) a a) atTop (𝓝 0) :=
    tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds htol
      (fun k => sub_nonneg.mpr (entry_le_one (hstoch (ns k)) a a)) (fun k => (hdeficit k a).le)
  refine ⟨ns, hmono, fun a b => ?_⟩
  by_cases hab : a = b
  · subst b
    simpa only [Matrix.one_apply_eq, sub_zero, sub_sub_cancel] using
      (tendsto_const_nhds (x := (1 : ℝ)) (f := atTop)).sub (hzero a)
  · have hoff : Tendsto (fun k => Γ (ns k) a b) atTop (𝓝 0) :=
      tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds (hzero a)
        (fun k => (hstoch (ns k)).1 a b) (fun k => offDiagonal_le_deficit (hstoch (ns k)) hab)
    simpa only [Matrix.one_apply_ne hab] using hoff

/-- Earlier overlap gives a later finite revival of the same rooted row pair. -/
theorem exists_reviving_return_of_overlap {s : ℕ} {a b x : V} (hab : a ≠ b)
    (ha : 0 < rootedFamily μ X T hpos s a x) (hb : 0 < rootedFamily μ X T hpos s b x) :
    ∃ n : ℕ, s < n ∧
      tv (rootedFamily μ X T hpos s a) (rootedFamily μ X T hpos s b) <
        tv (rootedFamily μ X T hpos n a) (rootedFamily μ X T hpos n b) := by
  let Γ := rootedFamily μ X T hpos
  have hε : 0 < min (Γ s a x) (Γ s b x) / 2 := half_pos (lt_min ha hb)
  obtain ⟨M, hM⟩ := exists_bounded_gap_nearReturn μ X T hX hT hpos hcard hcompact hε
  obtain ⟨n, hsn, _, hnear⟩ := hM (s + 1) (by omega)
  have hmargin : (1 - Γ n a a) + (1 - Γ n b b) < min (Γ s a x) (Γ s b x) := by
    linarith [hnear a, hnear b]
  exact ⟨n, by omega, tv_revives_of_nearReturn
    (rootedFamily_isRowStochastic μ X T hX hT hpos s)
    (rootedFamily_isRowStochastic μ X T hX hT hpos n) hab hmargin⟩

/-- A non-permutation followed by an observable near-return excludes a stochastic divisor. -/
theorem exists_pIndivisibleWithin_of_nonPermutation {s : ℕ}
    (hnonperm : ¬ ∃ σ : Equiv.Perm V, rootedFamily μ X T hpos s = σ.permMatrix ℝ) :
    ∃ n : ℕ, s < n ∧ C4r n (rootedFamily μ X T hpos) ∧
      PIndivisibleWithin n (rootedFamily μ X T hpos) := by
  obtain ⟨a, b, x, hab, ha, hb⟩ :=
    overlap_of_nonPermutation (rootedFamily_isRowStochastic μ X T hX hT hpos s) hnonperm
  obtain ⟨n, hsn, hrevives⟩ := exists_reviving_return_of_overlap μ X T hX hT hpos hcard hcompact
    hab ha hb
  have hrevival : C4r n (rootedFamily μ X T hpos) := ⟨a, b, s, n, hab, hsn, le_rfl, hrevives⟩
  exact ⟨n, hsn, hrevival, c4r_implies_pIndivisible _ _ hrevival⟩

end Measured

section Product

variable {V H : Type*} [MeasurableSpace V] [MeasurableSpace H]

/-- One product probability, whose hidden factor is shared across all roots. -/
def productLaw (ν : ProbabilityMeasure V) (ρ : ProbabilityMeasure H) : ProbabilityMeasure (V × H) :=
  ⟨(ν : Measure V).prod (ρ : Measure H), inferInstance⟩

theorem rootMass_productLaw (ν : ProbabilityMeasure V) (ρ : ProbabilityMeasure H) (a : V) :
    rootMass (productLaw ν ρ) Prod.fst a = (ν : Measure V).real {a} := by
  have hroot : Prod.fst ⁻¹' ({a} : Set V) = {a} ×ˢ (univ : Set H) := by
    ext p
    simp
  change (((ν : Measure V).prod (ρ : Measure H)) (Prod.fst ⁻¹' ({a} : Set V))).toReal = _
  rw [hroot, Measure.prod_prod, measure_univ, mul_one]
  rfl

/-- The common hidden-prior formula allows arbitrary strictly positive visible weights. -/
theorem rootedFamily_productLaw (ν : ProbabilityMeasure V) (ρ : ProbabilityMeasure H)
    (T : (V × H) ≃ᵐ (V × H)) (hpos : ∀ a, 0 < (ν : Measure V).real {a})
    (n : ℕ) (a b : V) :
    rootedFamily (productLaw ν ρ) Prod.fst T (fun i => by
      rw [rootMass_productLaw]
      exact hpos i) n a b =
      (ρ : Measure H).real {h | (((T.toEquiv ^ n) (a, h))).1 = b} := by
  let B : Set H := {h | (((T.toEquiv ^ n) (a, h))).1 = b}
  have hrect : endpointEvent Prod.fst T.toEquiv n a b = {a} ×ˢ B := by
    ext ⟨v, h⟩
    simp only [endpointEvent, Set.mem_inter_iff, Set.mem_preimage, Set.mem_singleton_iff,
      Set.mem_prod, Set.mem_setOf_eq, B]
    exact ⟨fun ⟨hv, hh⟩ => ⟨hv, hv ▸ hh⟩, fun ⟨hv, hh⟩ => ⟨hv, hv.symm ▸ hh⟩⟩
  change flux (productLaw ν ρ) Prod.fst T.toEquiv n a b /
    rootMass (productLaw ν ρ) Prod.fst a = (ρ : Measure H).real B
  rw [rootMass_productLaw, flux, hrect]
  change (((ν : Measure V).prod (ρ : Measure H)) ({a} ×ˢ B)).toReal /
    (ν : Measure V).real {a} = (ρ : Measure H).real B
  rw [Measure.prod_prod, ENNReal.toReal_mul, mul_div_cancel_left₀ _ (hpos a).ne']

end Product

section Controls

private def rotationRows (r : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  fun a b => if a = b then 1 - r else r

private theorem rotationRows_isRowStochastic {r : ℝ} (hlo : 0 ≤ r) (hhi : r ≤ 1) :
    IsRowStochastic (rotationRows r) := by
  constructor
  · intro a b
    dsimp [rotationRows]
    split_ifs <;> linarith
  · intro a
    fin_cases a <;> simp [Fin.sum_univ_two, rotationRows]

private def rotationControl (n : ℕ) : Matrix (Fin 2) (Fin 2) ℝ :=
  if n = 1 then rotationRows (1 / 2 + 2 * (Real.sqrt 2 / 100))
  else if n = 4 then rotationRows (8 * (Real.sqrt 2 / 100))
  else 1

/-- The paper's rotation matrices at 1 and 4 give the positive revival control. -/
theorem rotation_matrix_control :
    C4r 4 rotationControl ∧ PIndivisibleWithin 4 rotationControl := by
  have hη0 : 0 ≤ Real.sqrt 2 / 100 := by positivity
  have hη : Real.sqrt 2 / 100 < 1 / 50 := by
    have hs : Real.sqrt 2 < 2 := (Real.sqrt_lt (by norm_num) (by norm_num)).2 (by norm_num)
    linarith
  have hs : IsRowStochastic (rotationControl 1) := by
    norm_num [rotationControl]
    exact rotationRows_isRowStochastic (by linarith) (by linarith)
  have hn : IsRowStochastic (rotationControl 4) := by
    norm_num [rotationControl]
    exact rotationRows_isRowStochastic (by linarith) (by linarith)
  have hmargin :
      (1 - rotationControl 4 0 0) + (1 - rotationControl 4 1 1) <
        min (rotationControl 1 0 0) (rotationControl 1 1 0) := by
    norm_num [rotationControl, rotationRows]
    exact lt_min (by linarith) (by linarith)
  have hr : C4r 4 rotationControl :=
    ⟨0, 1, 1, 4, by decide, by decide, le_rfl, tv_revives_of_nearReturn hs hn (by decide) hmargin⟩
  exact ⟨hr, c4r_implies_pIndivisible _ _ hr⟩

/-- The paper's Bernoulli matrix family mixes at every positive time and admits every divisor. -/
theorem bernoulli_matrix_control :
    (∀ K, PDivisible K pdFamily) ∧
      ∀ n : ℕ, 1 ≤ n → ∀ a : Fin 2, 1 - pdFamily n a a = 1 / 2 := by
  refine ⟨pdFamily_pDivisible, fun n hn a => ?_⟩
  cases n with
  | zero => omega
  | succ n => norm_num [pdFamily, J2]

end Controls

#print axioms rootedFamily_isRowStochastic
#print axioms rootedFamily_zero
#print axioms sq_norm_indicator_sub_eq_deficit
#print axioms exists_bounded_gap_nearReturn
#print axioms exists_strictMono_rootedFamily_tendsto_one
#print axioms tv_revives_of_nearReturn
#print axioms overlap_of_nonPermutation
#print axioms exists_reviving_return_of_overlap
#print axioms exists_pIndivisibleWithin_of_nonPermutation
#print axioms rootMass_productLaw
#print axioms rootedFamily_productLaw
#print axioms rotation_matrix_control
#print axioms bernoulli_matrix_control

end OIBridge.ObservableRigidity
