import OIBridge.OrbitReachability
import OIBridge.LieRankSource

/-!
# Positive reachability: Lie-rank richness gives full control with no inverse clause

The round-fifty theorem `universalReachability_of_lieRank_unconditional` turns membership in the
reachable **subgroup** — words in the flows `e^{-itH}`, the controls `U_g`, their inverses and the
phases — into availability, and its hypothesis `hstar` is what makes the inverses of the controls
available. This file proves the same conclusion for the reachable **submonoid**, with no inverse
of a control anywhere: every unitary is a positive word in the flows, the controls and the phases.

* **The positive reachable monoid** `posReach H U` (Section A). Every element has an available
  conjugation channel by composition alone (`avail_of_mem_posReach`).
* **Recurrence** (Section B). The positive powers of a unitary return to the identity
  (`exists_pow_tendsto_one`): the sequence lies in the compact unit ball, a subsequence converges,
  and the ratio of two far-apart terms tends to `1`. Hence `m^{p-1}` tends to `m†` along a
  subsequence (`exists_pow_pred_tendsto_star`) — the only form in which an inverse is ever used.
* **The positive orbit span is a Lie algebra** (Section C). The real span of the positive orbit
  directions `Ad(m)(-iH)`, `m ∈ posReach`, and the phase direction, is `Ad(posReach)`-invariant and
  closed; conjugation by `m†` preserves it as a limit of conjugations by `m^{p-1}`
  (`adStar_mem_posSpan`); so the one-parameter groups `e^{t Ad(m)(-iH)} = m e^{-itH} m†` preserve it
  (`exp_posDir_conj_mem_posSpan`), and the round-fifty derivative step makes it a Lie subalgebra
  (`bracket_mem_posSpan`, `posLie`) containing the control Lie algebra, hence every skew-Hermitian
  matrix when `𝔏 ⊇ su(D)` (`skew_mem_posSpan`).
* **A word with spanning prefixes** (Sections D, E). Greedily choosing `A_1, …, A_n ∈ posReach` so
  that the directions `Ad(A_1 ⋯ A_j)(-iH)` span the positive orbit span
  (`exists_nested_spanning`), the word `A_1 e^{-it_1H} ⋯ A_n e^{-it_nH}` (`wordMap`) has strict
  derivative `h ↦ (Σ_j h_j Ad(A_1 ⋯ A_j)(-iH)) · B` at `t = 0`, `B = A_1 ⋯ A_n`
  (`wordMap_hasStrictFDerivAt`).
* **A neighbourhood of `B`, then of `1`, then everything** (Sections F, G). With a phase factor and
  a Hermitian complement the word map is a local diffeomorphism at `0` onto a neighbourhood of `B`
  (`psiW`, the round-fifty `Ψ` with the word in place of the product of orbit exponentials), and a
  unitary in the image has zero Hermitian part, so `posReach` is a neighbourhood of `B`
  (`posReach_mem_nhds_totalProd`). A submonoid of the unitary group that is a neighbourhood of one
  of its elements is a neighbourhood of `1` (`nhds_one_of_nhds_mem`, by recurrence), and a
  submonoid containing the phases that is a neighbourhood of `1` is everything
  (`eq_top_of_nhds_one`: a symmetric neighbourhood generates an open, hence clopen, subgroup of the
  connected unitary group, and the subgroup it generates is the submonoid it generates). Hence
  `posReach_eq_top` and `universalReachability_of_lieRank_positive`.
* **The theory-level consequence** (Section H). `control_of_lieRank`: Lie-rank richness alone gives
  full composite unitary control. Inverse accessibility is then derived
  (`inverseAccessibility_of_lieRank`), and the package `OIPlusPos` — implementation locality,
  elementary transition richness, embedded observation, with **no dagger stability** — is
  equivalent to exact finite endomorphic operational QM on every nonempty finite carrier
  (`carrier_general_oiPlusPos`).

**Not claimed.** Anything about non-compact or infinite-dimensional groups; that `HControl` is
necessary for positive reachability; the minimal elementary repertoire; anything about context
stability given generation. The analytic inputs are those of round fifty — the strict derivative
of the matrix exponential and the inverse-function theorem — plus compactness of the closed unit
ball of the finite-dimensional matrix space.
-/

namespace OIBridge
namespace PositiveReachability

open Complex Matrix ControlLie MonoidalCompletion ReachabilitySeam OrbitReachability
open Filter Topology
open scoped ComplexOrder Matrix.Norms.L2Operator

attribute [local instance 100] LieRing.ofAssociativeRing

variable {S : Type} [Fintype S] [DecidableEq S] {G : Type}

/-! ### Section A — the positive reachable monoid -/

section Monoid

/-- **THE POSITIVE REACHABLE MONOID**: finite words in the flows, the controls and the phases,
with no inverses. -/
noncomputable def posReach (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    Submonoid (unitary (Matrix S S ℂ)) :=
  Submonoid.closure (generators H U)

theorem flow_mem_posReach {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H) (t : ℝ) :
    (⟨flow H t, flow_mem_unitary H hH t⟩ : unitary (Matrix S S ℂ)) ∈ posReach H U :=
  Submonoid.subset_closure (Or.inl (Or.inl ⟨t, rfl⟩))

theorem control_mem_posReach (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) (g : G)
    (hg : U g ∈ unitary (Matrix S S ℂ)) :
    (⟨U g, hg⟩ : unitary (Matrix S S ℂ)) ∈ posReach H U :=
  Submonoid.subset_closure (Or.inl (Or.inr ⟨g, rfl⟩))

theorem phase_mem_posReach (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) {lam : ℂ} (h : ‖lam‖ = 1) :
    (⟨lam • (1 : Matrix S S ℂ), smul_one_mem_unitary h⟩ : unitary (Matrix S S ℂ)) ∈ posReach H U :=
  Submonoid.subset_closure (Or.inr ⟨lam, h, rfl⟩)

set_option maxHeartbeats 800000 in
/-- **POSITIVE WORDS ARE AVAILABLE** by composition alone. -/
theorem avail_of_mem_posReach (H : Matrix S S ℂ) (U : G → Matrix S S ℂ)
    (avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop)
    (hmul : ∀ V W : Matrix S S ℂ, avail 1 (fun _ => conjChannel V)
      → avail 1 (fun _ => conjChannel W) → avail 1 (fun _ => conjChannel (V * W)))
    (hone : avail 1 (fun _ => conjChannel (1 : Matrix S S ℂ)))
    (hflow : ∀ t : ℝ, avail 1 (fun _ => conjChannel (flow H t)))
    (hctrl : ∀ g : G, avail 1 (fun _ => conjChannel (U g)))
    (x : unitary (Matrix S S ℂ)) (hx : x ∈ posReach H U) :
    avail 1 (fun _ => conjChannel (x : Matrix S S ℂ)) := by
  induction hx using Submonoid.closure_induction with
  | mem x hx =>
    rcases hx with (⟨t, hx⟩ | ⟨g, hx⟩) | ⟨lam, hlam, hx⟩
    · rw [hx]; exact hflow t
    · rw [hx]; exact hctrl g
    · rw [hx, conjChannel_smul hlam]; exact hone
  | one => rw [OneMemClass.coe_one]; exact hone
  | mul x y _ _ hx hy => rw [Submonoid.coe_mul]; exact hmul _ _ hx hy

end Monoid

/-! ### Section B — recurrence of the positive powers of a unitary -/

section Recurrence

variable [Nonempty S]

theorem coe_pow_mem_closedBall (B : unitary (Matrix S S ℂ)) (n : ℕ) :
    ((B ^ n : unitary (Matrix S S ℂ)) : Matrix S S ℂ) ∈ Metric.closedBall (0 : Matrix S S ℂ) 1 := by
  rw [mem_closedBall_zero_iff]
  exact (CStarRing.norm_coe_unitary (B ^ n)).le

/-- **THE POSITIVE POWERS OF A UNITARY RETURN TO THE IDENTITY**: along a subsequence
`p k ≥ 1`, `B ^ (p k) → 1`. -/
theorem exists_pow_tendsto_one (B : unitary (Matrix S S ℂ)) :
    ∃ p : ℕ → ℕ, (∀ k, 1 ≤ p k) ∧
      Tendsto (fun k => B ^ p k) atTop (𝓝 (1 : unitary (Matrix S S ℂ))) := by
  set x : ℕ → Matrix S S ℂ := fun n => ((B ^ n : unitary (Matrix S S ℂ)) : Matrix S S ℂ) with hxdef
  obtain ⟨L, -, φ, hφ, hlim⟩ :=
    (isCompact_closedBall (0 : Matrix S S ℂ) 1).tendsto_subseq (coe_pow_mem_closedBall B)
  have hlim' : Tendsto (fun k => x (φ (k + 1))) atTop (𝓝 L) :=
    hlim.comp (tendsto_add_atTop_nat 1)
  have hstar : Tendsto (fun k => star (x (φ k))) atTop (𝓝 (star L)) := hlim.star
  have hunit : ∀ k, star (x (φ k)) * x (φ k) = 1 := fun k => coe_conjTranspose_mul_self (B ^ φ k)
  have hL : star L * L = 1 := by
    refine tendsto_nhds_unique (hstar.mul hlim) ?_
    exact tendsto_const_nhds.congr fun k => (hunit k).symm
  have hL' : L * star L = 1 := mul_eq_one_comm.mp hL
  have hy : Tendsto (fun k => x (φ (k + 1)) * star (x (φ k))) atTop (𝓝 1) := by
    have := hlim'.mul hstar
    rwa [hL'] at this
  refine ⟨fun k => φ (k + 1) - φ k, fun k => Nat.sub_pos_of_lt (hφ (Nat.lt_succ_self k)), ?_⟩
  rw [tendsto_subtype_rng]
  refine hy.congr fun k => ?_
  show x (φ (k + 1)) * star (x (φ k))
    = ((B ^ (φ (k + 1) - φ k) : unitary (Matrix S S ℂ)) : Matrix S S ℂ)
  rw [pow_sub B (hφ (Nat.lt_succ_self k)).le, Submonoid.coe_mul, ← Unitary.star_eq_inv,
    Unitary.coe_star]

/-- **THE ADJOINT AS A LIMIT OF POSITIVE POWERS**: `B ^ (p k - 1) → B†`. -/
theorem exists_pow_pred_tendsto_star (B : unitary (Matrix S S ℂ)) :
    ∃ p : ℕ → ℕ, (∀ k, 1 ≤ p k) ∧
      Tendsto (fun k => ((B ^ (p k - 1) : unitary (Matrix S S ℂ)) : Matrix S S ℂ)) atTop
        (𝓝 (B : Matrix S S ℂ)ᴴ) := by
  obtain ⟨p, hp1, hp⟩ := exists_pow_tendsto_one B
  refine ⟨p, hp1, ?_⟩
  have h1 : Tendsto (fun k => ((B ^ p k : unitary (Matrix S S ℂ)) : Matrix S S ℂ)) atTop
      (𝓝 ((1 : unitary (Matrix S S ℂ)) : Matrix S S ℂ)) := tendsto_subtype_rng.mp hp
  have h2 := h1.const_mul ((B : Matrix S S ℂ)ᴴ)
  rw [OneMemClass.coe_one, Matrix.mul_one] at h2
  refine h2.congr fun k => ?_
  have hsplit : B ^ p k = B * B ^ (p k - 1) := by
    rw [← pow_succ', Nat.sub_add_cancel (hp1 k)]
  rw [hsplit, Submonoid.coe_mul, ← Matrix.mul_assoc, coe_conjTranspose_mul_self, Matrix.one_mul]

end Recurrence

/-! ### Section C — the positive orbit span is a Lie subalgebra -/

section Span

/-- The positive orbit directions `Ad(m)(-iH)`, `m ∈ posReach`, with the phase direction. -/
def posDirs (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) : Set (Matrix S S ℂ) :=
  {X | ∃ m : unitary (Matrix S S ℂ), m ∈ posReach H U ∧ X = orbitDir H m}
    ∪ {Complex.I • (1 : Matrix S S ℂ)}

theorem posDirs_skew {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H) {X : Matrix S S ℂ}
    (hX : X ∈ posDirs H U) : Xᴴ = -X := by
  rcases hX with ⟨m, _, rfl⟩ | hX
  · exact orbitDir_skew hH m
  · rw [Set.mem_singleton_iff] at hX
    rw [hX]
    exact phaseDir_skew

/-- Conjugation by a positive word permutes the positive orbit directions. -/
theorem ad_posDirs {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (m : unitary (Matrix S S ℂ))
    (hm : m ∈ posReach H U) {X : Matrix S S ℂ} (hX : X ∈ posDirs H U) :
    (m : Matrix S S ℂ) * X * (m : Matrix S S ℂ)ᴴ ∈ posDirs H U := by
  rcases hX with ⟨m', hm', rfl⟩ | hX
  · refine Or.inl ⟨m * m', mul_mem hm hm', ?_⟩
    simp only [orbitDir, Submonoid.coe_mul, Matrix.conjTranspose_mul, Matrix.mul_assoc]
  · rw [Set.mem_singleton_iff] at hX
    subst hX
    refine Or.inr ?_
    rw [Set.mem_singleton_iff, Matrix.mul_smul, Matrix.mul_one, Matrix.smul_mul,
      coe_mul_self_conjTranspose]

/-- The real span of the positive orbit directions. -/
noncomputable def posSpan (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    Submodule ℝ (Matrix S S ℂ) :=
  Submodule.span ℝ (posDirs H U)

theorem ad_mem_posSpan {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (m : unitary (Matrix S S ℂ))
    (hm : m ∈ posReach H U) {Y : Matrix S S ℂ} (hY : Y ∈ posSpan H U) :
    (m : Matrix S S ℂ) * Y * (m : Matrix S S ℂ)ᴴ ∈ posSpan H U := by
  induction hY using Submodule.span_induction with
  | mem X hX => exact Submodule.subset_span (ad_posDirs m hm hX)
  | zero => simp
  | add X Y _ _ hX hY =>
    rw [Matrix.mul_add, Matrix.add_mul]
    exact Submodule.add_mem _ hX hY
  | smul a X _ hX =>
    rw [Matrix.mul_smul, Matrix.smul_mul]
    exact Submodule.smul_mem _ a hX

theorem posSpan_closed (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    IsClosed ((posSpan H U : Submodule ℝ (Matrix S S ℂ)) : Set (Matrix S S ℂ)) :=
  Submodule.closed_of_finiteDimensional _

/-- **CONJUGATION BY THE ADJOINT OF A POSITIVE WORD PRESERVES THE SPAN**: `m†` is the limit of
the positive powers `m^{p-1}`, each of which is a positive word, and the span is closed. -/
theorem adStar_mem_posSpan [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (m : unitary (Matrix S S ℂ)) (hm : m ∈ posReach H U) {Y : Matrix S S ℂ}
    (hY : Y ∈ posSpan H U) :
    (m : Matrix S S ℂ)ᴴ * Y * (m : Matrix S S ℂ) ∈ posSpan H U := by
  obtain ⟨p, -, hp⟩ := exists_pow_pred_tendsto_star m
  have hmem : ∀ k, ((m ^ (p k - 1) : unitary (Matrix S S ℂ)) : Matrix S S ℂ) * Y
      * ((m ^ (p k - 1) : unitary (Matrix S S ℂ)) : Matrix S S ℂ)ᴴ ∈ posSpan H U :=
    fun k => ad_mem_posSpan _ (pow_mem hm _) hY
  have hlim : Tendsto (fun k => ((m ^ (p k - 1) : unitary (Matrix S S ℂ)) : Matrix S S ℂ) * Y
      * star ((m ^ (p k - 1) : unitary (Matrix S S ℂ)) : Matrix S S ℂ)) atTop
      (𝓝 ((m : Matrix S S ℂ)ᴴ * Y * star ((m : Matrix S S ℂ)ᴴ))) :=
    (hp.mul tendsto_const_nhds).mul hp.star
  rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_conjTranspose] at hlim
  exact (posSpan_closed H U).mem_of_tendsto hlim (Filter.Eventually.of_forall hmem)

/-- **THE ONE-PARAMETER GROUP OF A POSITIVE ORBIT DIRECTION PRESERVES THE SPAN**:
`e^{t Ad(m)(-iH)} = m e^{-itH} m†`, and `m e^{-itH}` is a positive word. -/
theorem exp_posDir_conj_mem_posSpan [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (hH : Hᴴ = H) {X : Matrix S S ℂ} (hX : X ∈ posDirs H U) {Y : Matrix S S ℂ}
    (hY : Y ∈ posSpan H U) (t : ℝ) :
    NormedSpace.exp (t • X) * Y * NormedSpace.exp ((-t) • X) ∈ posSpan H U := by
  rcases hX with ⟨m, hm, rfl⟩ | hX
  · rw [exp_neg_smul_eq_conjTranspose (orbitDir_skew hH m)]
    have he : NormedSpace.exp (t • orbitDir H m)
        = (m : Matrix S S ℂ) * flow H t * (m : Matrix S S ℂ)ᴴ := by
      rw [orbitDir, ← Matrix.smul_mul, ← Matrix.mul_smul, real_smul_neg_I_smul,
        unitary_exp_conj _ _ (coe_mul_self_conjTranspose m)]
      rfl
    rw [he]
    have h1 := adStar_mem_posSpan m hm hY
    have hmf : m * ⟨flow H t, flow_mem_unitary H hH t⟩ ∈ posReach H U :=
      mul_mem hm (flow_mem_posReach hH t)
    have h2 := ad_mem_posSpan _ hmf h1
    convert h2 using 1
    simp only [Submonoid.coe_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
      Matrix.mul_assoc]
  · rw [Set.mem_singleton_iff] at hX
    subst hX
    rw [exp_phaseDir_eq, exp_phaseDir_eq, Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul,
      Matrix.mul_one, smul_smul, ← NormedSpace.exp_add]
    have h0 : ((-t : ℝ) : ℂ) * Complex.I + (t : ℂ) * Complex.I = 0 := by
      push_cast
      ring
    rw [h0, NormedSpace.exp_zero, one_smul]
    exact hY

/-- **THE DERIVATIVE STEP**, as in round fifty: for a positive orbit direction `X` and `Y` in the
span, `[X, Y]` lies in the span. -/
theorem bracket_mem_posSpan [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    {X : Matrix S S ℂ} (hX : X ∈ posDirs H U) {Y : Matrix S S ℂ} (hY : Y ∈ posSpan H U) :
    X * Y - Y * X ∈ posSpan H U := by
  set γ : ℝ → Matrix S S ℂ :=
    fun t => NormedSpace.exp (t • X) * Y * NormedSpace.exp ((-t) • X) with hγdef
  have hγ : ∀ t, γ t ∈ posSpan H U := fun t => exp_posDir_conj_mem_posSpan hH hX hY t
  have hd : HasDerivAt γ (X * Y - Y * X) 0 := by
    have h1 : HasDerivAt (fun t : ℝ => NormedSpace.exp (t • X))
        (NormedSpace.exp ((0 : ℝ) • X) * X) 0 := hasDerivAt_exp_smul_const X 0
    have h2 : HasDerivAt (fun t : ℝ => NormedSpace.exp ((-t) • X))
        ((-1 : ℝ) • (NormedSpace.exp ((-(0 : ℝ)) • X) * X)) 0 :=
      (hasDerivAt_exp_smul_const X (-(0 : ℝ))).scomp 0 (hasDerivAt_neg 0)
    have h12 := (h1.mul (hasDerivAt_const (0 : ℝ) Y)).mul h2
    refine h12.congr_deriv ?_
    simp [zero_smul, NormedSpace.exp_zero, sub_eq_add_neg]
  have hslope := hasDerivAt_iff_tendsto_slope.mp hd
  refine (posSpan_closed H U).mem_of_tendsto hslope (Filter.Eventually.of_forall fun t => ?_)
  rw [slope_def_module]
  exact Submodule.smul_mem _ _ (Submodule.sub_mem _ (hγ t) (hγ 0))

/-- **THE POSITIVE ORBIT SPAN AS A LIE SUBALGEBRA.** -/
noncomputable def posLie [Nonempty S] (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) (hH : Hᴴ = H) :
    LieSubalgebra ℝ (Matrix S S ℂ) :=
  { posSpan H U with
    lie_mem' := fun {X Y} hX hY => by
      show X * Y - Y * X ∈ posSpan H U
      induction hX using Submodule.span_induction with
      | mem X hX => exact bracket_mem_posSpan hH hX hY
      | zero => simp
      | add X₁ X₂ _ _ h1 h2 =>
        have := Submodule.add_mem _ h1 h2
        convert this using 1
        noncomm_ring
      | smul a X _ h =>
        have := Submodule.smul_mem _ a h
        convert this using 1
        rw [Matrix.smul_mul, Matrix.mul_smul, smul_sub] }

theorem mem_posLie_iff [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    (X : Matrix S S ℂ) : X ∈ posLie H U hH ↔ X ∈ posSpan H U := Iff.rfl

/-- Every round-nineteen generator is a positive orbit direction: `U_g` is a positive word. -/
theorem controlGenerators_subset_posDirs {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (hU : ∀ g, (U g)ᴴ * U g = 1) : controlGenerators H U ⊆ posDirs H U := by
  rintro A ⟨g, rfl⟩
  refine Or.inl ⟨⟨U g, mem_unitary_of_conjTranspose_mul (hU g)⟩,
    control_mem_posReach H U g _, ?_⟩
  simp only [orbitDir, Matrix.mul_smul, Matrix.smul_mul]

theorem controlLie_le_posLie [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    (hU : ∀ g, (U g)ᴴ * U g = 1) : controlLie H U ≤ posLie H U hH :=
  LieSubalgebra.lieSpan_le.mpr fun _ hA =>
    Submodule.subset_span (controlGenerators_subset_posDirs hU hA)

/-- **EVERY SKEW-HERMITIAN MATRIX IS IN THE POSITIVE ORBIT SPAN** when `𝔏 ⊇ su(D)`. -/
theorem skew_mem_posSpan [Nonempty S] {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    (hU : ∀ g, (U g)ᴴ * U g = 1) (hLie : HControl H U) {A : Matrix S S ℂ} (hA : Aᴴ = -A) :
    A ∈ posSpan H U := by
  have hD : (Fintype.card S : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  set c : ℂ := A.trace / Fintype.card S with hc
  have htr : star A.trace = -A.trace := by
    rw [← Matrix.trace_conjTranspose, hA, Matrix.trace_neg]
  have hcs : star c = -c := by
    rw [hc, star_div₀, htr, Complex.star_def, map_natCast, neg_div]
  have hA0 : (A - c • (1 : Matrix S S ℂ))ᴴ = -(A - c • (1 : Matrix S S ℂ)) := by
    rw [Matrix.conjTranspose_sub, hA, Matrix.conjTranspose_smul, Matrix.conjTranspose_one, hcs,
      neg_smul, neg_sub_neg, neg_sub]
  have htr0 : (A - c • (1 : Matrix S S ℂ)).trace = 0 := by
    rw [Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one, smul_eq_mul, hc,
      div_mul_cancel₀ _ hD, sub_self]
  have h1 : A - c • (1 : Matrix S S ℂ) ∈ posSpan H U :=
    (mem_posLie_iff hH _).mp (controlLie_le_posLie hH hU (hLie _ ⟨hA0, htr0⟩))
  have h2 : c • (1 : Matrix S S ℂ) ∈ posSpan H U := by
    have hre : c.re = 0 := by
      have := congrArg Complex.re hcs
      rw [Complex.star_def, Complex.conj_re, Complex.neg_re] at this
      linarith
    have hci : c • (1 : Matrix S S ℂ) = (c.im : ℝ) • (Complex.I • (1 : Matrix S S ℂ)) := by
      rw [← smul_assoc, Complex.real_smul]
      congr 1
      apply Complex.ext <;> simp [hre]
    rw [hci]
    exact Submodule.smul_mem _ _ (Submodule.subset_span (Or.inr rfl))
  have := Submodule.add_mem _ h1 h2
  simpa using this

end Span

/-! ### Section D — conjugation as a linear automorphism, and the greedy prefixes -/

section Greedy

/-- Conjugation by a unitary, `X ↦ P X P†`, as a real-linear automorphism. -/
def adEquiv (P : unitary (Matrix S S ℂ)) : Matrix S S ℂ ≃ₗ[ℝ] Matrix S S ℂ where
  toFun X := (P : Matrix S S ℂ) * X * (P : Matrix S S ℂ)ᴴ
  invFun X := (P : Matrix S S ℂ)ᴴ * X * (P : Matrix S S ℂ)
  map_add' X Y := by rw [Matrix.mul_add, Matrix.add_mul]
  map_smul' c X := by
    rw [Matrix.mul_smul, Matrix.smul_mul]
    rfl
  left_inv X := by
    simp only [Matrix.mul_assoc]
    rw [coe_conjTranspose_mul_self, Matrix.mul_one, ← Matrix.mul_assoc,
      coe_conjTranspose_mul_self, Matrix.one_mul]
  right_inv X := by
    simp only [Matrix.mul_assoc]
    rw [coe_mul_self_conjTranspose, Matrix.mul_one, ← Matrix.mul_assoc,
      coe_mul_self_conjTranspose, Matrix.one_mul]

@[simp] theorem adEquiv_apply (P : unitary (Matrix S S ℂ)) (X : Matrix S S ℂ) :
    adEquiv P X = (P : Matrix S S ℂ) * X * (P : Matrix S S ℂ)ᴴ := rfl

/-- The positive orbit directions without the phase direction. -/
def posDirs₀ (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) : Set (Matrix S S ℂ) :=
  {X | ∃ m : unitary (Matrix S S ℂ), m ∈ posReach H U ∧ X = orbitDir H m}

/-- Their real span. -/
noncomputable def posSpan₀ (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    Submodule ℝ (Matrix S S ℂ) :=
  Submodule.span ℝ (posDirs₀ H U)

theorem posSpan_eq_sup (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    posSpan H U = posSpan₀ H U ⊔ Submodule.span ℝ {Complex.I • (1 : Matrix S S ℂ)} := by
  unfold posSpan posDirs posSpan₀ posDirs₀
  rw [Submodule.span_union]

theorem orbitDir_mul (H : Matrix S S ℂ) (P m : unitary (Matrix S S ℂ)) :
    orbitDir H (P * m) = adEquiv P (orbitDir H m) := by
  simp only [orbitDir, adEquiv_apply, Submonoid.coe_mul, Matrix.conjTranspose_mul, Matrix.mul_assoc]

theorem map_adEquiv_posSpan₀_le {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (P : unitary (Matrix S S ℂ)) (hP : P ∈ posReach H U) :
    (posSpan₀ H U).map (adEquiv P : Matrix S S ℂ →ₗ[ℝ] Matrix S S ℂ) ≤ posSpan₀ H U := by
  rw [posSpan₀, Submodule.map_span_le]
  rintro X ⟨m, hm, rfl⟩
  refine Submodule.subset_span ⟨P * m, mul_mem hP hm, ?_⟩
  rw [orbitDir_mul]
  rfl

/-- **THE SPAN IS `Ad(posReach)`-INVARIANT AS A WHOLE**: the image is contained in the span and has
the same dimension. -/
theorem map_adEquiv_posSpan₀ {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (P : unitary (Matrix S S ℂ)) (hP : P ∈ posReach H U) :
    (posSpan₀ H U).map (adEquiv P : Matrix S S ℂ →ₗ[ℝ] Matrix S S ℂ) = posSpan₀ H U :=
  Submodule.eq_of_le_of_finrank_eq (map_adEquiv_posSpan₀_le P hP)
    (LinearEquiv.finrank_map_eq (adEquiv P) _)

/-- If the span is not inside `W`, some direction `Ad(P m)(-iH)` with `m ∈ posReach` is not. -/
theorem exists_dir_notMem {H : Matrix S S ℂ} {U : G → Matrix S S ℂ}
    (P : unitary (Matrix S S ℂ)) (hP : P ∈ posReach H U) {W : Submodule ℝ (Matrix S S ℂ)}
    (hW : ¬ posSpan₀ H U ≤ W) :
    ∃ m : unitary (Matrix S S ℂ), m ∈ posReach H U ∧ orbitDir H (P * m) ∉ W := by
  by_contra h
  push Not at h
  apply hW
  rw [← map_adEquiv_posSpan₀ P hP, posSpan₀, Submodule.map_span_le]
  rintro X ⟨m, hm, rfl⟩
  have := h m hm
  rwa [orbitDir_mul] at this

/-- The prefix products `A_0 A_1 ⋯ A_j` of a tuple of unitaries. -/
def prefixProd : (n : ℕ) → (Fin n → unitary (Matrix S S ℂ)) → Fin n → unitary (Matrix S S ℂ)
  | 0, _, j => j.elim0
  | n + 1, A, j => Fin.cases (A 0) (fun j' => A 0 * prefixProd n (fun i => A i.succ) j') j

@[simp] theorem prefixProd_zero (n : ℕ) (A : Fin (n + 1) → unitary (Matrix S S ℂ)) :
    prefixProd (n + 1) A 0 = A 0 := by
  simp [prefixProd]

@[simp] theorem prefixProd_succ (n : ℕ) (A : Fin (n + 1) → unitary (Matrix S S ℂ)) (j : Fin n) :
    prefixProd (n + 1) A j.succ = A 0 * prefixProd n (fun i => A i.succ) j := by
  simp [prefixProd]

theorem prefixProd_mem {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} :
    ∀ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)), (∀ j, A j ∈ posReach H U) →
      ∀ j, prefixProd n A j ∈ posReach H U := by
  intro n
  induction n with
  | zero => intro A _ j; exact j.elim0
  | succ n ih =>
    intro A hA j
    refine Fin.cases ?_ (fun j' => ?_) j
    · rw [prefixProd_zero]; exact hA 0
    · rw [prefixProd_succ]; exact mul_mem (hA 0) (ih _ (fun i => hA i.succ) j')

/-- **GREEDY PREFIXES.** Starting from any positive word `P` and any subspace `W` of the span, a
tuple `A` of positive words can be chosen so that `W` together with the directions of the nested
prefixes `P A_0 ⋯ A_j` spans the whole positive orbit span. Induction on the codimension. -/
theorem exists_nested_spanning (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) :
    ∀ (d : ℕ) (P : unitary (Matrix S S ℂ)), P ∈ posReach H U →
      ∀ W : Submodule ℝ (Matrix S S ℂ), W ≤ posSpan₀ H U →
        Module.finrank ℝ W + d = Module.finrank ℝ (posSpan₀ H U) →
        ∃ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)), (∀ j, A j ∈ posReach H U) ∧
          W ⊔ Submodule.span ℝ (Set.range fun j => orbitDir H (P * prefixProd n A j))
            = posSpan₀ H U := by
  intro d
  induction d with
  | zero =>
    intro P _ W hW hd
    refine ⟨0, fun j => j.elim0, fun j => j.elim0, ?_⟩
    have hWeq : W = posSpan₀ H U := Submodule.eq_of_le_of_finrank_eq hW (by simpa using hd)
    have hr : Set.range (fun j : Fin 0 => orbitDir H (P * prefixProd 0 (fun j => j.elim0) j)) = ∅ :=
      Set.range_eq_empty _
    rw [hr, Submodule.span_empty, sup_bot_eq, hWeq]
  | succ d ih =>
    intro P hP W hW hd
    have hlt : ¬ posSpan₀ H U ≤ W := by
      intro hle
      have := Submodule.finrank_mono hle
      omega
    obtain ⟨m, hm, hnot⟩ := exists_dir_notMem P hP hlt
    set v := orbitDir H (P * m) with hv
    have hv0 : v ≠ 0 := fun h0 => hnot (h0 ▸ W.zero_mem)
    have hvS : v ∈ posSpan₀ H U := Submodule.subset_span ⟨P * m, mul_mem hP hm, rfl⟩
    have hW'le : W ⊔ Submodule.span ℝ {v} ≤ posSpan₀ H U :=
      sup_le hW ((Submodule.span_singleton_le_iff_mem v _).mpr hvS)
    have hdisj : Disjoint W (Submodule.span ℝ {v}) :=
      (Submodule.disjoint_span_singleton' hv0).mpr hnot
    have hrank : Module.finrank ℝ (W ⊔ Submodule.span ℝ {v} : Submodule ℝ (Matrix S S ℂ))
        = Module.finrank ℝ W + 1 := by
      have h := Submodule.finrank_sup_add_finrank_inf_eq W (Submodule.span ℝ {v})
      rw [hdisj.eq_bot, finrank_bot, add_zero, finrank_span_singleton hv0] at h
      exact h
    obtain ⟨n, A, hA, hspan⟩ := ih (P * m) (mul_mem hP hm) _ hW'le (by rw [hrank]; omega)
    refine ⟨n + 1, Fin.cons m A, ?_, ?_⟩
    · intro j
      refine Fin.cases ?_ (fun j' => ?_) j
      · simpa using hm
      · simpa using hA j'
    · have hrange : Set.range (fun j => orbitDir H (P * prefixProd (n + 1) (Fin.cons m A) j))
          = insert v (Set.range fun j => orbitDir H (P * m * prefixProd n A j)) := by
        ext X
        simp only [Set.mem_range, Set.mem_insert_iff, Fin.exists_fin_succ, prefixProd_zero,
          prefixProd_succ, Fin.cons_zero, Fin.cons_succ, mul_assoc, hv]
        exact or_congr eq_comm Iff.rfl
      rw [hrange, Submodule.span_insert, ← sup_assoc, hspan]

end Greedy

/-! ### Section E — the word map and its strict derivative -/

section Word

/-- The word `A_0 e^{t_0 X} A_1 e^{t_1 X} ⋯ A_{n-1} e^{t_{n-1} X}`. -/
noncomputable def wordMap (X : Matrix S S ℂ) :
    (n : ℕ) → (Fin n → unitary (Matrix S S ℂ)) → (Fin n → ℝ) → Matrix S S ℂ
  | 0, _, _ => 1
  | n + 1, A, t =>
    (A 0 : Matrix S S ℂ) * NormedSpace.exp (t 0 • X)
      * wordMap X n (fun i => A i.succ) (fun i => t i.succ)

/-- The product `A_0 A_1 ⋯ A_{n-1}`. -/
def totalProd : (n : ℕ) → (Fin n → unitary (Matrix S S ℂ)) → unitary (Matrix S S ℂ)
  | 0, _ => 1
  | n + 1, A => A 0 * totalProd n (fun i => A i.succ)

theorem totalProd_mem {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} :
    ∀ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)), (∀ j, A j ∈ posReach H U) →
      totalProd n A ∈ posReach H U := by
  intro n
  induction n with
  | zero => intro _ _; exact one_mem _
  | succ n ih => intro A hA; exact mul_mem (hA 0) (ih _ fun i => hA i.succ)

theorem wordMap_zero (X : Matrix S S ℂ) :
    ∀ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)),
      wordMap X n A 0 = (totalProd n A : Matrix S S ℂ) := by
  intro n
  induction n with
  | zero => intro A; rfl
  | succ n ih =>
    intro A
    show (A 0 : Matrix S S ℂ) * NormedSpace.exp ((0 : Fin (n + 1) → ℝ) 0 • X)
      * wordMap X n (fun i => A i.succ) (fun i => (0 : Fin (n + 1) → ℝ) i.succ)
      = ((A 0 * totalProd n fun i => A i.succ : unitary (Matrix S S ℂ)) : Matrix S S ℂ)
    have h : (fun i : Fin n => (0 : Fin (n + 1) → ℝ) i.succ) = 0 := rfl
    rw [h, ih, Pi.zero_apply, zero_smul, NormedSpace.exp_zero, Matrix.mul_one, Submonoid.coe_mul]

/-- **THE WORD IS A POSITIVE WORD** for every parameter, with `X = -iH`. -/
theorem wordMap_mem_posReach {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H) :
    ∀ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)), (∀ j, A j ∈ posReach H U) →
      ∀ t : Fin n → ℝ, ∃ P ∈ posReach H U,
        (P : Matrix S S ℂ) = wordMap ((-Complex.I) • H) n A t := by
  intro n
  induction n with
  | zero => intro _ _ _; exact ⟨1, one_mem _, rfl⟩
  | succ n ih =>
    intro A hA t
    obtain ⟨P', hP', hPe⟩ := ih (fun i => A i.succ) (fun i => hA i.succ) (fun i => t i.succ)
    refine ⟨A 0 * ⟨flow H (t 0), flow_mem_unitary H hH (t 0)⟩ * P',
      mul_mem (mul_mem (hA 0) (flow_mem_posReach hH (t 0))) hP', ?_⟩
    show (A 0 : Matrix S S ℂ) * flow H (t 0) * (P' : Matrix S S ℂ) = _
    rw [hPe]
    show _ = (A 0 : Matrix S S ℂ) * NormedSpace.exp (t 0 • ((-Complex.I) • H)) * _
    rw [real_smul_neg_I_smul]
    rfl

/-- The directions of a word: `Ad(A_0 ⋯ A_j)(X)`. -/
noncomputable def wordDirs (X : Matrix S S ℂ) (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)) :
    Fin n → Matrix S S ℂ :=
  fun j => adEquiv (prefixProd n A j) X

/-- `h ↦ (Σ_j h_j D_j) · B`. -/
noncomputable def dirMapR (n : ℕ) (D : Fin n → Matrix S S ℂ) (B : Matrix S S ℂ) :
    (Fin n → ℝ) →L[ℝ] Matrix S S ℂ :=
  ((ContinuousLinearMap.mul ℝ (Matrix S S ℂ)).flip B).comp (dirMap n D)

theorem dirMapR_apply (n : ℕ) (D : Fin n → Matrix S S ℂ) (B : Matrix S S ℂ) (h : Fin n → ℝ) :
    dirMapR n D B h = (∑ j, h j • D j) * B := by
  simp [dirMapR, dirMap_apply, Finset.sum_mul]

theorem coe_conjTranspose_mul_self_mul (P : unitary (Matrix S S ℂ)) (M : Matrix S S ℂ) :
    (P : Matrix S S ℂ)ᴴ * ((P : Matrix S S ℂ) * M) = M := by
  rw [← Matrix.mul_assoc, coe_conjTranspose_mul_self, Matrix.one_mul]

/-- **THE STRICT DERIVATIVE OF THE WORD MAP AT `0`** is `h ↦ (Σ_j h_j Ad(A_0 ⋯ A_j)(X)) · B`. -/
theorem wordMap_hasStrictFDerivAt (X : Matrix S S ℂ) :
    ∀ (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)),
      HasStrictFDerivAt (wordMap X n A)
        (dirMapR n (wordDirs X n A) (totalProd n A : Matrix S S ℂ)) 0 := by
  intro n
  induction n with
  | zero =>
    intro A
    have h : dirMapR 0 (wordDirs X 0 A) (totalProd 0 A : Matrix S S ℂ) = 0 := by
      apply ContinuousLinearMap.ext
      intro v
      simp [dirMapR_apply]
    rw [h]
    show HasStrictFDerivAt (fun _ : Fin 0 → ℝ => (1 : Matrix S S ℂ)) 0 0
    exact hasStrictFDerivAt_const 1 0
  | succ n ih =>
    intro A
    let tail : (Fin (n + 1) → ℝ) →L[ℝ] (Fin n → ℝ) :=
      ContinuousLinearMap.pi fun j => ContinuousLinearMap.proj (R := ℝ) (φ := fun _ => ℝ) j.succ
    have he : HasStrictFDerivAt (fun t : Fin (n + 1) → ℝ => NormedSpace.exp (t 0 • X))
        ((ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ)
          (NormedSpace.exp (((0 : Fin (n + 1) → ℝ) 0) • X) * X)).comp
          (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin (n + 1) => ℝ) 0)) 0 := by
      have h1 := (hasStrictDerivAt_exp_smul_const X ((0 : Fin (n + 1) → ℝ) 0)).hasStrictFDerivAt
      exact h1.comp (0 : Fin (n + 1) → ℝ)
        (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin (n + 1) => ℝ) 0).hasStrictFDerivAt
    have ha := he.const_mul (A 0 : Matrix S S ℂ)
    have hb : HasStrictFDerivAt
        (fun t : Fin (n + 1) → ℝ => wordMap X n (fun j => A j.succ) (fun j => t j.succ))
        ((dirMapR n (wordDirs X n fun j => A j.succ)
          (totalProd n fun j => A j.succ : Matrix S S ℂ)).comp tail) 0 :=
      HasStrictFDerivAt.comp (0 : Fin (n + 1) → ℝ) (ih (fun j => A j.succ))
        tail.hasStrictFDerivAt
    have h := ha.mul' hb
    show HasStrictFDerivAt
      (fun t : Fin (n + 1) → ℝ =>
        (A 0 : Matrix S S ℂ) * NormedSpace.exp (t 0 • X)
          * wordMap X n (fun j => A j.succ) (fun j => t j.succ))
      (dirMapR (n + 1) (wordDirs X (n + 1) A) (totalProd (n + 1) A : Matrix S S ℂ)) 0
    refine h.congr_fderiv ?_
    apply ContinuousLinearMap.ext
    intro v
    have hb0 : wordMap X n (fun j => A j.succ) (fun _ => (0 : ℝ))
        = (totalProd n fun j => A j.succ : Matrix S S ℂ) := wordMap_zero X n _
    simp only [_root_.add_apply, ContinuousLinearMap.comp_apply,
      _root_.smul_apply, ContinuousLinearMap.smulRight_apply,
      ContinuousLinearMap.proj_apply, one_apply_eq_self, dirMapR_apply,
      Fin.sum_univ_succ, wordDirs, prefixProd_zero, prefixProd_succ, adEquiv_apply, totalProd,
      Submonoid.coe_mul, Pi.zero_apply, zero_smul, NormedSpace.exp_zero, Matrix.one_mul,
      Matrix.mul_one, hb0, tail, ContinuousLinearMap.coe_pi', MulOpposite.smul_eq_mul_unop,
      MulOpposite.unop_op, Matrix.add_mul, Finset.sum_mul, Finset.mul_sum,
      Matrix.smul_mul, Matrix.mul_smul, Matrix.mul_assoc, Matrix.conjTranspose_mul,
      coe_conjTranspose_mul_self_mul, smul_eq_mul]
    abel

end Word

/-! ### Section F — the map `Ψ` and a neighbourhood of `B` in the positive monoid -/

section Local

variable [Nonempty S]

omit [Fintype S] [DecidableEq S] [Nonempty S] in
/-- A variant of the round-fifty surjectivity lemma with the spanning hypothesis stated directly. -/
theorem psiDeriv_surjective_of_skew (n : ℕ) (X : Fin n → Matrix S S ℂ)
    (hspan : ∀ M : Matrix S S ℂ, Mᴴ = -M → M ∈ Submodule.span ℝ (Set.range X)) :
    LinearMap.range (psiDeriv n X : ((Fin n → ℝ) × (Fin n → ℝ)) →ₗ[ℝ] Matrix S S ℂ) = ⊤ := by
  rw [LinearMap.range_eq_top]
  intro M₀
  set A : Matrix S S ℂ := (1 / 2 : ℝ) • (M₀ - M₀ᴴ) with hAdef
  set B : Matrix S S ℂ := (-Complex.I) • ((1 / 2 : ℝ) • (M₀ + M₀ᴴ)) with hBdef
  have hA : Aᴴ = -A := by
    rw [hAdef, Matrix.conjTranspose_smul, star_trivial, Matrix.conjTranspose_sub,
      Matrix.conjTranspose_conjTranspose, ← smul_neg, neg_sub]
  have hB : Bᴴ = -B := by
    rw [hBdef, Matrix.conjTranspose_smul, Matrix.conjTranspose_smul, star_neg, Complex.star_def,
      Complex.conj_I, star_trivial, Matrix.conjTranspose_add, Matrix.conjTranspose_conjTranspose,
      neg_neg, neg_smul, neg_neg, add_comm]
  have hAB : A + Complex.I • B = M₀ := by
    rw [hBdef, hAdef, smul_smul, mul_neg, Complex.I_mul_I, neg_neg, one_smul, ← smul_add,
      sub_add_add_cancel, ← two_smul ℝ M₀, smul_smul]
    norm_num
  obtain ⟨h, hh⟩ := (Submodule.mem_span_range_iff_exists_fun ℝ).mp (hspan A hA)
  obtain ⟨k, hk⟩ := (Submodule.mem_span_range_iff_exists_fun ℝ).mp (hspan B hB)
  refine ⟨(h, k), ?_⟩
  show dirMap n X h + hermMap n X k = M₀
  rw [dirMap_apply, hermMap_apply, hh, ← hAB]
  congr 1
  rw [← hk, Finset.smul_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [smul_comm]

/-- `Ψ(a, k) = e^{K(k)} · e^{a_0 i} · word(tail a)`, with the directions `(i·1, D)`: the first
component carries the phase and the word, the second the Hermitian complement, as in round fifty. -/
noncomputable def psiW (X : Matrix S S ℂ) (n : ℕ) (D : Fin n → Matrix S S ℂ)
    (A : Fin n → unitary (Matrix S S ℂ)) (p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ)) :
    Matrix S S ℂ :=
  NormedSpace.exp (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2)
    * (NormedSpace.exp (p.1 0 • (Complex.I • (1 : Matrix S S ℂ)))
      * wordMap X n A fun j => p.1 j.succ)

omit [Nonempty S] in
theorem psiW_zero (X : Matrix S S ℂ) (n : ℕ) (D : Fin n → Matrix S S ℂ)
    (A : Fin n → unitary (Matrix S S ℂ)) : psiW X n D A 0 = (totalProd n A : Matrix S S ℂ) := by
  simp only [psiW, Prod.fst_zero, Prod.snd_zero, map_zero, NormedSpace.exp_zero, Pi.zero_apply,
    zero_smul, Matrix.one_mul]
  exact wordMap_zero X n A

/-- The candidate derivative of `Ψ` at `0`: the round-fifty derivative, right-multiplied by `B`. -/
noncomputable def psiDerivW (n : ℕ) (D : Fin n → Matrix S S ℂ) (B : Matrix S S ℂ) :
    ((Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ)) →L[ℝ] Matrix S S ℂ :=
  ((ContinuousLinearMap.mul ℝ (Matrix S S ℂ)).flip B).comp
    (psiDeriv (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D))

omit [Nonempty S] in
theorem exp_phase_hasStrictFDerivAt (n : ℕ) :
    HasStrictFDerivAt
      (fun a : Fin (n + 1) → ℝ => NormedSpace.exp (a 0 • (Complex.I • (1 : Matrix S S ℂ))))
      ((ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ)
        (NormedSpace.exp (((0 : Fin (n + 1) → ℝ) 0) • (Complex.I • (1 : Matrix S S ℂ)))
          * (Complex.I • (1 : Matrix S S ℂ)))).comp
        (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin (n + 1) => ℝ) 0)) 0 := by
  have h1 := (hasStrictDerivAt_exp_smul_const (Complex.I • (1 : Matrix S S ℂ))
    ((0 : Fin (n + 1) → ℝ) 0)).hasStrictFDerivAt
  exact h1.comp (0 : Fin (n + 1) → ℝ)
    (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin (n + 1) => ℝ) 0).hasStrictFDerivAt

omit [Nonempty S] in
/-- **THE STRICT DERIVATIVE OF `Ψ` AT `0`.** -/
theorem psiW_hasStrictFDerivAt (X : Matrix S S ℂ) (n : ℕ) (A : Fin n → unitary (Matrix S S ℂ)) :
    HasStrictFDerivAt (psiW X n (wordDirs X n A) A)
      (psiDerivW n (wordDirs X n A) (totalProd n A : Matrix S S ℂ)) 0 := by
  set D := wordDirs X n A
  set B : Matrix S S ℂ := (totalProd n A : Matrix S S ℂ)
  let tail : (Fin (n + 1) → ℝ) →L[ℝ] (Fin n → ℝ) :=
    ContinuousLinearMap.pi fun j => ContinuousLinearMap.proj (R := ℝ) (φ := fun _ => ℝ) j.succ
  -- the Hermitian factor
  have hK : HasStrictFDerivAt
      (fun p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ) =>
        NormedSpace.exp (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2))
      ((1 : Matrix S S ℂ →L[ℝ] Matrix S S ℂ).comp
        ((hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D)).comp
          (ContinuousLinearMap.snd ℝ _ _))) 0 := by
    have he : HasStrictFDerivAt NormedSpace.exp (1 : Matrix S S ℂ →L[ℝ] Matrix S S ℂ)
        (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D)
          (ContinuousLinearMap.snd ℝ (Fin (n + 1) → ℝ) (Fin (n + 1) → ℝ) 0)) := by
      rw [map_zero, map_zero]
      exact hasStrictFDerivAt_exp_zero (𝕂 := ℝ)
    exact he.comp (0 : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ))
      ((hermMap (n + 1) _).hasStrictFDerivAt.comp _ hasStrictFDerivAt_snd)
  -- the phase factor
  have hph : HasStrictFDerivAt
      (fun p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ) =>
        NormedSpace.exp (p.1 0 • (Complex.I • (1 : Matrix S S ℂ))))
      (((ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ)
        (NormedSpace.exp (((0 : Fin (n + 1) → ℝ) 0) • (Complex.I • (1 : Matrix S S ℂ)))
          * (Complex.I • (1 : Matrix S S ℂ)))).comp
        (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin (n + 1) => ℝ) 0)).comp
        (ContinuousLinearMap.fst ℝ (Fin (n + 1) → ℝ) (Fin (n + 1) → ℝ))) 0 :=
    HasStrictFDerivAt.comp
      (g := fun a : Fin (n + 1) → ℝ => NormedSpace.exp (a 0 • (Complex.I • (1 : Matrix S S ℂ))))
      (f := Prod.fst) (0 : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ))
      (exp_phase_hasStrictFDerivAt n) hasStrictFDerivAt_fst
  -- the word factor
  have hw : HasStrictFDerivAt
      (fun p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ) => wordMap X n A fun j => p.1 j.succ)
      ((dirMapR n D B).comp (tail.comp (ContinuousLinearMap.fst ℝ _ _))) 0 :=
    (wordMap_hasStrictFDerivAt X n A).comp (0 : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ))
      (tail.hasStrictFDerivAt.comp _ hasStrictFDerivAt_fst)
  have h := hK.mul' (hph.mul' hw)
  show HasStrictFDerivAt (psiW X n D A) (psiDerivW n D B) 0
  refine h.congr_fderiv ?_
  apply ContinuousLinearMap.ext
  intro p
  have hb0 : wordMap X n A (fun _ => (0 : ℝ)) = B := wordMap_zero X n A
  simp only [psiDerivW, psiDeriv, _root_.add_apply, ContinuousLinearMap.comp_apply,
    _root_.smul_apply, ContinuousLinearMap.smulRight_apply,
    ContinuousLinearMap.proj_apply, one_apply_eq_self, ContinuousLinearMap.coe_fst',
    ContinuousLinearMap.coe_snd', ContinuousLinearMap.flip_apply, ContinuousLinearMap.mul_apply',
    Pi.mul_apply, dirMapR_apply, dirMap_apply, hermMap_apply, Fin.sum_univ_succ, Fin.cons_zero,
    Fin.cons_succ, Prod.fst_zero, Prod.snd_zero, Pi.zero_apply, zero_smul, map_zero,
    NormedSpace.exp_zero, Matrix.one_mul, one_smul, hb0, tail,
    ContinuousLinearMap.coe_pi', MulOpposite.smul_eq_mul_unop, MulOpposite.unop_op,
    Matrix.add_mul, Finset.sum_mul, Matrix.smul_mul]
  abel

/-- The range of `psiDerivW` is everything when the directions span the skew-Hermitian
matrices: right multiplication by the unitary `B` is onto. -/
theorem psiDerivW_surjective (n : ℕ) (D : Fin n → Matrix S S ℂ) (B : unitary (Matrix S S ℂ))
    (hspan : ∀ M : Matrix S S ℂ, Mᴴ = -M →
      M ∈ Submodule.span ℝ (Set.range (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D))) :
    LinearMap.range (psiDerivW n D (B : Matrix S S ℂ) :
      ((Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ)) →ₗ[ℝ] Matrix S S ℂ) = ⊤ := by
  rw [LinearMap.range_eq_top]
  intro M
  have hinner := psiDeriv_surjective_of_skew (n + 1) _ hspan
  rw [LinearMap.range_eq_top] at hinner
  obtain ⟨p, hp⟩ := hinner (M * (B : Matrix S S ℂ)ᴴ)
  refine ⟨p, ?_⟩
  show (psiDeriv (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p) * (B : Matrix S S ℂ) = M
  rw [show (psiDeriv (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p)
      = M * (B : Matrix S S ℂ)ᴴ from hp, Matrix.mul_assoc, coe_conjTranspose_mul_self,
    Matrix.mul_one]

/-- The phase exponential is a unit phase. -/
theorem exp_phase_norm (a : ℝ) : ‖NormedSpace.exp ((a : ℂ) * Complex.I)‖ = 1 := by
  rw [← Complex.exp_eq_exp_ℂ]
  exact Complex.norm_exp_ofReal_mul_I a

omit [Nonempty S] in
/-- **`Ψ` LANDS IN THE POSITIVE MONOID** for every parameter, with the Hermitian factor removed:
the phase times the word is a positive word. -/
theorem phase_word_mem_posReach {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H) (n : ℕ)
    (A : Fin n → unitary (Matrix S S ℂ)) (hA : ∀ j, A j ∈ posReach H U)
    (p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ)) :
    ∃ Q ∈ posReach H U, (Q : Matrix S S ℂ)
      = NormedSpace.exp (p.1 0 • (Complex.I • (1 : Matrix S S ℂ)))
        * wordMap ((-Complex.I) • H) n A fun j => p.1 j.succ := by
  obtain ⟨P, hP, hPe⟩ := wordMap_mem_posReach hH n A hA fun j => p.1 j.succ
  refine ⟨⟨_, smul_one_mem_unitary (exp_phase_norm (p.1 0))⟩ * P,
    mul_mem (phase_mem_posReach H U (exp_phase_norm (p.1 0))) hP, ?_⟩
  rw [Submonoid.coe_mul, hPe, exp_phaseDir_eq]

/-- **THE POSITIVE MONOID IS A NEIGHBOURHOOD OF THE PRODUCT OF A SPANNING WORD.** The inverse-function
step of round fifty, with `Ψ` mapping a neighbourhood of `0` onto a neighbourhood of `B`; a
unitary `u = e^{K} Q` in the image, with `Q` a positive word, forces `K = 0`. -/
theorem posReach_mem_nhds_totalProd {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    (hU : ∀ g, (U g)ᴴ * U g = 1) (hLie : HControl H U) (n : ℕ)
    (A : Fin n → unitary (Matrix S S ℂ)) (hA : ∀ j, A j ∈ posReach H U)
    (hspan : Submodule.span ℝ (Set.range (wordDirs ((-Complex.I) • H) n A)) = posSpan₀ H U) :
    ((posReach H U : Submonoid (unitary (Matrix S S ℂ))) : Set (unitary (Matrix S S ℂ)))
      ∈ 𝓝 (totalProd n A) := by
  set X : Matrix S S ℂ := (-Complex.I) • H with hXdef
  set D := wordDirs X n A with hDdef
  set B := totalProd n A with hBdef
  -- the directions with the phase span every skew-Hermitian matrix
  have hDskew : ∀ j, (D j)ᴴ = -(D j) := by
    intro j
    show (adEquiv (prefixProd n A j) X)ᴴ = -(adEquiv (prefixProd n A j) X)
    have := orbitDir_skew hH (prefixProd n A j)
    simpa [orbitDir, adEquiv_apply, hXdef] using this
  have hplus : ∀ i, ((Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D : Fin (n + 1) → Matrix S S ℂ) i)ᴴ
      = -((Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D : Fin (n + 1) → Matrix S S ℂ) i) := by
    intro i
    cases i using Fin.cases with
    | zero => simp only [Fin.cons_zero]; exact phaseDir_skew
    | succ j => simp only [Fin.cons_succ]; exact hDskew j
  have hspan' : ∀ M : Matrix S S ℂ, Mᴴ = -M →
      M ∈ Submodule.span ℝ (Set.range (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D)) := by
    intro M hM
    have h1 := skew_mem_posSpan hH hU hLie hM
    rw [posSpan_eq_sup, ← hspan, Fin.range_cons, Submodule.span_insert] at *
    rw [sup_comm] at h1
    exact h1
  -- the inverse-function step
  obtain ⟨W, hW, hWinj⟩ := exists_exp_injOn_nhds (S := S)
  have h0W : (0 : Matrix S S ℂ) ∈ W := mem_of_mem_nhds hW
  let f : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ) → Matrix S S ℂ :=
    fun p => (2 : ℝ) • hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2
  have hf : Continuous f :=
    ((hermMap (n + 1) _).continuous.comp continuous_snd).const_smul (2 : ℝ)
  have hf0 : f 0 = 0 := by simp [f]
  have hB : f ⁻¹' W ∈ 𝓝 (0 : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ)) :=
    hf.continuousAt.preimage_mem_nhds (by rw [hf0]; exact hW)
  have hmap := (psiW_hasStrictFDerivAt X n A).map_nhds_eq_of_surj
    (psiDerivW_surjective n D B hspan')
  have himg : psiW X n D A '' (f ⁻¹' W) ∈ 𝓝 (B : Matrix S S ℂ) := by
    rw [← psiW_zero X n D A, ← hmap]
    exact Filter.image_mem_map hB
  have hpre : (Subtype.val ⁻¹' (psiW X n D A '' (f ⁻¹' W)) : Set (unitary (Matrix S S ℂ)))
      ∈ 𝓝 B :=
    continuous_subtype_val.continuousAt.preimage_mem_nhds (by simpa using himg)
  refine Filter.mem_of_superset hpre ?_
  rintro u ⟨p, hp, hpu⟩
  obtain ⟨Q, hQ, hQe⟩ := phase_word_mem_posReach hH n A hA p
  have hK : (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2)ᴴ
      = hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2 :=
    hermMap_conjTranspose hplus p.2
  have hEeq : NormedSpace.exp (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2)
      = ((u * star Q : unitary (Matrix S S ℂ)) : Matrix S S ℂ) := by
    rw [Submonoid.coe_mul, Unitary.coe_star, Matrix.star_eq_conjTranspose, ← hpu, hQe]
    show _ = NormedSpace.exp _ * (_ * _) * (_ * _)ᴴ
    rw [Matrix.mul_assoc, ← hQe, coe_mul_self_conjTranspose, Matrix.mul_one]
  have h1 : (NormedSpace.exp (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2))ᴴ
      * NormedSpace.exp (hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2) = 1 := by
    rw [hEeq]
    exact coe_conjTranspose_mul_self _
  rw [← Matrix.exp_conjTranspose, hK, ← Matrix.exp_add_of_commute _ _ (Commute.refl _),
    ← two_smul ℝ (hermMap (n + 1) _ p.2)] at h1
  have hfp : f p = 0 := hWinj hp h0W (by rw [NormedSpace.exp_zero]; exact h1)
  have hK0 : hermMap (n + 1) (Fin.cons (Complex.I • (1 : Matrix S S ℂ)) D) p.2 = 0 := by
    have := hfp
    simp only [f] at this
    exact (smul_eq_zero.mp this).resolve_left two_ne_zero
  have hu : (u : Matrix S S ℂ) = (Q : Matrix S S ℂ) := by
    rw [← hpu, psiW, hK0, NormedSpace.exp_zero, Matrix.one_mul, hQe]
  rw [show u = Q from Subtype.ext hu]
  exact hQ

end Local

/-! ### Section G — from a neighbourhood of `B` to everything -/

section Global

variable [Nonempty S]

omit [Nonempty S] in
/-- Inversion on the unitary group is the adjoint, hence continuous. -/
theorem continuous_unitary_inv :
    Continuous (fun w : unitary (Matrix S S ℂ) => w⁻¹) := by
  refine continuous_induced_rng.mpr ?_
  have h : (Subtype.val ∘ fun w : unitary (Matrix S S ℂ) => w⁻¹)
      = fun w : unitary (Matrix S S ℂ) => star (w : Matrix S S ℂ) := by
    funext w
    simp only [Function.comp_apply, ← Unitary.star_eq_inv, Unitary.coe_star]
  rw [h]
  exact continuous_star.comp continuous_subtype_val

/-- **A SUBMONOID OF THE UNITARY GROUP THAT IS A NEIGHBOURHOOD OF ONE OF ITS ELEMENTS IS A
NEIGHBOURHOOD OF `1`**: for `v` near `1`, a positive power `B^k` lands where `v B^{-k} B` is in the
monoid, and `v = (v B^{-k} B) B^{k-1}`. -/
theorem nhds_one_of_nhds_mem (M : Submonoid (unitary (Matrix S S ℂ)))
    {B : unitary (Matrix S S ℂ)} (hB : B ∈ M)
    (hN : (M : Set (unitary (Matrix S S ℂ))) ∈ 𝓝 B) :
    (M : Set (unitary (Matrix S S ℂ))) ∈ 𝓝 (1 : unitary (Matrix S S ℂ)) := by
  set N := interior (M : Set (unitary (Matrix S S ℂ))) with hNdef
  have hNopen : IsOpen N := isOpen_interior
  have hBN : B ∈ N := mem_interior_iff_mem_nhds.mpr hN
  set V : Set (unitary (Matrix S S ℂ)) := (fun w => w * B) ⁻¹' N with hVdef
  have hVopen : IsOpen V := hNopen.preimage (continuous_id.mul continuous_const)
  have h1V : (1 : unitary (Matrix S S ℂ)) ∈ V := by
    show (1 : unitary (Matrix S S ℂ)) * B ∈ N
    rwa [one_mul]
  refine Filter.mem_of_superset (hVopen.mem_nhds h1V) fun v hv => ?_
  set O : Set (unitary (Matrix S S ℂ)) := (fun w => v * w⁻¹) ⁻¹' V with hOdef
  have hOopen : IsOpen O := hVopen.preimage (continuous_const.mul continuous_unitary_inv)
  have h1O : (1 : unitary (Matrix S S ℂ)) ∈ O := by
    show v * (1 : unitary (Matrix S S ℂ))⁻¹ ∈ V
    rwa [inv_one, mul_one]
  obtain ⟨p, hp1, hp⟩ := exists_pow_tendsto_one B
  obtain ⟨k, hk⟩ := (hp.eventually_mem (hOopen.mem_nhds h1O)).exists
  have hvk : v * (B ^ p k)⁻¹ * B ∈ N := hk
  have hsplit : v = (v * (B ^ p k)⁻¹ * B) * B ^ (p k - 1) := by
    rw [mul_assoc, ← pow_succ', Nat.sub_add_cancel (hp1 k), inv_mul_cancel_right]
  rw [hsplit]
  exact mul_mem (interior_subset hvk) (pow_mem hB _)

omit [Nonempty S] in
/-- **A SUBMONOID CONTAINING THE PHASES THAT IS A NEIGHBOURHOOD OF `1` IS EVERYTHING**: a symmetric
neighbourhood of `1` generates an open, hence clopen, subgroup, which contains the identity
component of the connected unitary group; the subgroup it generates is the submonoid it
generates, hence lies in `M`; and every unitary is a phase times an element of that component. -/
theorem eq_top_of_nhds_one (M : Submonoid (unitary (Matrix S S ℂ)))
    (hph : ∀ lam : ℂ, ∀ h : ‖lam‖ = 1,
      (⟨lam • (1 : Matrix S S ℂ), smul_one_mem_unitary h⟩ : unitary (Matrix S S ℂ)) ∈ M)
    (hV : (M : Set (unitary (Matrix S S ℂ))) ∈ 𝓝 (1 : unitary (Matrix S S ℂ))) :
    ∀ u : unitary (Matrix S S ℂ), u ∈ M := by
  set N := interior (M : Set (unitary (Matrix S S ℂ))) with hNdef
  have hNopen : IsOpen N := isOpen_interior
  have h1N : (1 : unitary (Matrix S S ℂ)) ∈ N := mem_interior_iff_mem_nhds.mpr hV
  set V' : Set (unitary (Matrix S S ℂ)) := N ∩ (fun w => w⁻¹) ⁻¹' N with hV'def
  have hV'open : IsOpen V' := hNopen.inter (hNopen.preimage continuous_unitary_inv)
  have h1V' : (1 : unitary (Matrix S S ℂ)) ∈ V' := ⟨h1N, by show (1 : unitary _)⁻¹ ∈ N; rwa [inv_one]⟩
  have hV'inv : V'⁻¹ = V' := by
    ext w
    simp only [Set.mem_inv, hV'def, Set.mem_inter_iff, Set.mem_preimage, inv_inv]
    exact and_comm
  have hV'M : V' ⊆ (M : Set (unitary (Matrix S S ℂ))) := fun w hw => interior_subset hw.1
  set K : Subgroup (unitary (Matrix S S ℂ)) := Subgroup.closure V' with hKdef
  have hKM : ∀ w, w ∈ K → w ∈ M := by
    intro w hw
    have h1 : w ∈ (K.toSubmonoid : Submonoid (unitary (Matrix S S ℂ))) := hw
    rw [hKdef, Subgroup.closure_toSubmonoid, hV'inv, Set.union_self] at h1
    exact Submonoid.closure_le.mpr hV'M h1
  have hKnhds : (K : Set (unitary (Matrix S S ℂ))) ∈ 𝓝 (1 : unitary (Matrix S S ℂ)) :=
    Filter.mem_of_superset (hV'open.mem_nhds h1V') Subgroup.subset_closure
  have hopen : IsOpen (K : Set (unitary (Matrix S S ℂ))) := Subgroup.isOpen_of_mem_nhds K hKnhds
  have hclopen : IsClopen (K : Set (unitary (Matrix S S ℂ))) :=
    ⟨Subgroup.isClosed_of_isOpen _ hopen, hopen⟩
  intro u
  obtain ⟨lam, w, hlam, hj, hu⟩ := exists_phase_joined u
  have hw : w ∈ K :=
    IsClopen.connectedComponent_subset hclopen (one_mem _) (pathComponent_subset_component _ hj)
  have hu' : u = ⟨lam • (1 : Matrix S S ℂ), smul_one_mem_unitary hlam⟩ * w := by
    ext
    simp [hu]
  rw [hu']
  exact mul_mem (hph lam hlam) (hKM w hw)

/-- **EVERY UNITARY IS A POSITIVE WORD** in the flows, the controls and the phases, when
`𝔏 ⊇ su(D)`. -/
theorem posReach_eq_top {H : Matrix S S ℂ} {U : G → Matrix S S ℂ} (hH : Hᴴ = H)
    (hU : ∀ g, (U g)ᴴ * U g = 1) (hLie : HControl H U) :
    ∀ u : unitary (Matrix S S ℂ), u ∈ posReach H U := by
  obtain ⟨n, A, hA, hspan⟩ := exists_nested_spanning H U (Module.finrank ℝ (posSpan₀ H U)) 1
    (one_mem _) ⊥ bot_le (by simp)
  have hdirs : (fun j => orbitDir H (1 * prefixProd n A j)) = wordDirs ((-Complex.I) • H) n A := by
    funext j
    simp [wordDirs, adEquiv_apply, orbitDir]
  rw [hdirs, bot_sup_eq] at hspan
  have hN := posReach_mem_nhds_totalProd hH hU hLie n A hA hspan
  have h1 := nhds_one_of_nhds_mem (posReach H U) (totalProd_mem n A hA) hN
  exact eq_top_of_nhds_one (posReach H U) (fun lam h => phase_mem_posReach H U h) h1

end Global

set_option maxHeartbeats 800000 in
/-- **UNIVERSAL UNITARY REACHABILITY FROM THE LIE-RANK CONDITION, WITH NO INVERSE CLAUSE.** The
round-fifty conclusion with the `hstar` hypothesis removed. -/
theorem universalReachability_of_lieRank_positive (H : Matrix S S ℂ)
    (U : G → Matrix S S ℂ) (hH : Hᴴ = H) (hU : ∀ g, (U g)ᴴ * U g = 1) (hLie : HControl H U)
    (avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop)
    (hmul : ∀ V W : Matrix S S ℂ, avail 1 (fun _ => conjChannel V)
      → avail 1 (fun _ => conjChannel W) → avail 1 (fun _ => conjChannel (V * W)))
    (hone : avail 1 (fun _ => conjChannel (1 : Matrix S S ℂ)))
    (hflow : ∀ t : ℝ, avail 1 (fun _ => conjChannel (flow H t)))
    (hctrl : ∀ g : G, avail 1 (fun _ => conjChannel (U g))) :
    UniversalUnitaryReachability avail := by
  intro V hV
  rcases isEmpty_or_nonempty S with hS | hS
  · have hV1 : V = 1 := by
      ext i j
      exact (IsEmpty.false i).elim
    rw [hV1]
    exact hone
  · have hmem := posReach_eq_top hH hU hLie ⟨V, mem_unitary_of_conjTranspose_mul hV⟩
    exact avail_of_mem_posReach H U avail hmul hone hflow hctrl
      ⟨V, mem_unitary_of_conjTranspose_mul hV⟩ hmem

/-! ### Section H — the theory-level consequence: dagger stability leaves the package -/

section Theory

open OperationalAssembly AncillaClosure OIHierarchyGeneral MicroReversibility InterventionLocality
open PrimitiveSource LieRankSource GeneralCarrier PhysicalCharacterization LevelOneSeam

variable {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A)

/-- **LIE-RANK RICHNESS ALONE GIVES FULL COMPOSITE UNITARY CONTROL**: the inverse clause of
reversible richness is not consumed. -/
theorem control_of_lieRank (h : LieRankRichness T) : HasCompositeUnitaryControl T := by
  intro n V hV
  obtain ⟨G, H, U, hH, hU, hLie, hflow, hctrl⟩ := h n
  let avail : ∀ m : ℕ, (Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ]
      Matrix (A × Fin n) (A × Fin n) ℂ) → Prop :=
    fun m F => ∀ i : Fin m, T.availExt n Unit (fun _ => F i)
  have hreach : UniversalUnitaryReachability avail :=
    universalReachability_of_lieRank_positive H U hH hU hLie avail
      (fun V W hV hW i => by
        have := availExt_comp_unit T n _ _ (hW i) (hV i)
        rwa [conjChannel_mul_general] at this)
      (fun _ => by
        have := hflow 0
        rwa [OIHierarchy.flow_zero] at this)
      (fun t _ => hflow t) (fun g _ => hctrl g)
  exact hreach V hV 0

/-- **INVERSE ACCESSIBILITY IS DERIVED** from Lie-rank richness on a well-formed theory. -/
theorem inverseAccessibility_of_lieRank [Nonempty A] (hwf : WellFormed T) (h : LieRankRichness T) :
    InverseAccessibility T :=
  (reversibleRichness_of_control T hwf (control_of_lieRank T h)).1

/-- **THE PACKAGE WITHOUT DAGGER STABILITY**: implementation locality, elementary transition
richness, embedded observation. -/
def OIPlusPos : Prop :=
  ImplementationLocality T ∧ ElementaryTransitionRichness T ∧ EmbeddedObservation T

variable [Nonempty A]

theorem qm_of_oiPlusPos (h : OIPlusPos T) : ExactAllFiniteEndomorphicQuantumOps T := by
  obtain ⟨hloc, helem, hemb⟩ := h
  have hwf : WellFormed T :=
    ⟨validity_of_implementationLocality hloc, systemToLevelOne_of_embeddedObservation hemb⟩
  rw [exactAll_iff_substantive T hwf]
  exact ⟨(observationalIndependence_iff_inert T).mp
      (observationalIndependence_of_implementationLocality hloc),
    control_of_lieRank T (lieRank_of_elementary T helem), closure_of_embeddedObservation hemb⟩

theorem oiPlusPos_of_qm (h : ExactAllFiniteEndomorphicQuantumOps T) : OIPlusPos T :=
  ⟨implementationLocality_of_qm T h, elementary_of_control T (physical_of_exactAll T h).2.2.1,
    embeddedObservation_of_qm T h⟩

/-- **THE PACKAGE WITHOUT DAGGER STABILITY ⟺ FINITE OPERATIONAL QM**, on any nonempty finite
carrier. -/
theorem oiPlusPos_iff_qm : OIPlusPos T ↔ ExactAllFiniteEndomorphicQuantumOps T :=
  ⟨qm_of_oiPlusPos T, oiPlusPos_of_qm T⟩

omit [Nonempty A] in
theorem oiPlusPos_of_oiPlusElem (h : OIPlusElem T) : OIPlusPos T :=
  ⟨implementationLocality_of_reversible h.1, h.2.1, h.2.2⟩

theorem oiPlusPos_iff_oiPlusElem : OIPlusPos T ↔ OIPlusElem T := by
  rw [oiPlusPos_iff_qm, oiPlusElem_iff_qm]

end Theory

/-- **THE CARRIER-GENERAL STATEMENT**, quantified over the carrier. -/
theorem carrier_general_oiPlusPos :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A]
      (T : OperationalAssembly.FiniteOperationalTheory A),
      OIPlusPos T ↔ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T :=
  fun _ _ _ _ T => oiPlusPos_iff_qm T

#print axioms avail_of_mem_posReach
#print axioms exists_pow_tendsto_one
#print axioms exists_pow_pred_tendsto_star
#print axioms adStar_mem_posSpan
#print axioms exp_posDir_conj_mem_posSpan
#print axioms bracket_mem_posSpan
#print axioms controlLie_le_posLie
#print axioms skew_mem_posSpan
#print axioms map_adEquiv_posSpan₀
#print axioms exists_nested_spanning
#print axioms wordMap_mem_posReach
#print axioms wordMap_hasStrictFDerivAt
#print axioms psiW_hasStrictFDerivAt
#print axioms psiDerivW_surjective
#print axioms posReach_mem_nhds_totalProd
#print axioms nhds_one_of_nhds_mem
#print axioms eq_top_of_nhds_one
#print axioms posReach_eq_top
#print axioms universalReachability_of_lieRank_positive
#print axioms control_of_lieRank
#print axioms inverseAccessibility_of_lieRank
#print axioms oiPlusPos_iff_qm
#print axioms oiPlusPos_iff_oiPlusElem
#print axioms carrier_general_oiPlusPos

end PositiveReachability
end OIBridge
