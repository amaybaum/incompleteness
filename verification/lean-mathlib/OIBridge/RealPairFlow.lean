import OIBridge.StateMixingCoupling

/-!
# The real pair-flow reduction audit — a continuous orthogonal pair action forces the datum

The preregistered pass of `REAL-PAIR-FLOW-AUDIT.md`, read under its scope amendment. Nothing here
is named "C5"; the rotation form is never assumed; no continuity necessity is claimed.

* T1, the principle: a real pair flow is a family of real two-by-two matrices with identity,
  group law, continuity, real orthogonality and nontriviality (`PairFlow`); `transport n M` is its
  sourcing map to level `n`, the ancilla a spectator.
* T2, the reduction: the determinant is one everywhere (`pairFlow_det_one`), every value is a
  rotation of the plane (`pairFlow_form`), the local angle is additive and, by continuity and
  density, linear (`pairFlow_rate`), the rate is nonzero, and the flow supplies the mixing datum at
  every angle after reparameterizing time (`pairFlow_supplies_mixImage`).
* T3, the composition: a class with the stabilities, the stated access, the phase gates and the
  transports of a pair flow generates the closure and exact finite operational quantum mechanics
  (`qm_of_pairFlowSourced`); the concrete pair-flow class equals the construction audit's class
  (`flowR_eq_mixC`) and its theory is quantum mechanics (`pairFlowTheory_qm`).
* T4, the countercontrols: the shear and the boost satisfy every hypothesis but orthogonality and
  contain no datum outside `πℤ`; the constant identity satisfies every hypothesis but
  nontriviality and transports to the identity.
-/

namespace OIBridge
namespace RealPairFlow

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open PolarizationClosure CoherentContinuumSource StateMixingCoupling Set

/-! ### Section A — T1: the principle and its transport -/

section Principle

/-- **THE PRINCIPLE**: a nontrivial continuous one-parameter real orthogonal action on one
distinguishable pair. The rotation form is not part of the definition. -/
structure PairFlow where
  A : ℝ → Matrix (Fin 2) (Fin 2) ℝ
  zero : A 0 = 1
  add : ∀ s t : ℝ, A (s + t) = A s * A t
  cont : Continuous A
  orth : ∀ t : ℝ, (A t)ᵀ * A t = 1
  nontrivial : ∃ t : ℝ, A t ≠ 1

/-- **THE SOURCING MAP AT LEVEL `n`**: the real matrix on the site factor, cast to `ℂ`, the
identity on the ancilla factor. -/
def transport (n : ℕ) (M : Matrix (Fin 2) (Fin 2) ℝ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  Matrix.of fun p q => if p.2 = q.2 then (M p.1 q.1 : ℂ) else 0

end Principle

/-! ### Section B — T2: the reduction -/

section Reduction

/-- The real rotation of the plane, the conclusion of the reduction. -/
noncomputable def rotR (θ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![Real.cos θ, -Real.sin θ; Real.sin θ, Real.cos θ]

theorem rotR_mul (θ θ' : ℝ) : rotR θ * rotR θ' = rotR (θ + θ') := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rotR, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_add, Real.sin_add] <;> ring

theorem rotR_zero : rotR 0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rotR]

theorem rotR_pow (θ : ℝ) : ∀ k : ℕ, rotR θ ^ k = rotR (k * θ) := by
  intro k
  induction k with
  | zero => simp [rotR_zero]
  | succ k ih => rw [pow_succ, ih, rotR_mul]; push_cast; ring_nf

theorem transport_rotR (n : ℕ) (θ : ℝ) : transport n (rotR θ) = mixImage n θ := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [transport, Matrix.of_apply, mixImage_apply]
  by_cases hk : k = l
  · subst hk
    fin_cases x <;> fin_cases y <;> simp [rotR, StateMixingCoupling.rot]
  · simp [hk]

/-- **ROTATIONS ARE INJECTIVE ON SMALL ANGLES**: equal rotations with one angle below `π/2` and the
other below `π` in absolute value have equal angles. -/
theorem rotR_inj_small {x y : ℝ} (hx : |x| < Real.pi / 2) (hy : |y| < Real.pi) (h : rotR x = rotR y) :
    x = y := by
  have hcos : Real.cos x = Real.cos y := by
    have := congrFun (congrFun h 0) 0; simpa [rotR] using this
  have hsin : Real.sin x = Real.sin y := by
    have := congrFun (congrFun h 1) 0; simpa [rotR] using this
  have hE : Complex.exp ((x : ℂ) * Complex.I) = Complex.exp ((y : ℂ) * Complex.I) := by
    rw [Complex.exp_mul_I, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
      ← Complex.ofReal_cos, ← Complex.ofReal_sin, hcos, hsin]
  rw [Complex.exp_eq_exp_iff_exists_int] at hE
  obtain ⟨k, hk⟩ := hE
  have hxy : (x : ℂ) = y + k * (2 * Real.pi) := by
    have : (x : ℂ) * Complex.I = (y + k * (2 * Real.pi)) * Complex.I := by
      rw [hk]; ring
    exact mul_right_cancel₀ Complex.I_ne_zero this
  have hr : x = y + k * (2 * Real.pi) := by exact_mod_cast hxy
  have hpi := Real.pi_pos
  obtain ⟨hx1, hx2⟩ := abs_lt.mp hx
  obtain ⟨hy1, hy2⟩ := abs_lt.mp hy
  have hk1 : (k : ℝ) < 1 := by nlinarith
  have hk2 : (-1 : ℝ) < k := by nlinarith
  have hk0 : k = 0 := by
    have h1 : k < 1 := by exact_mod_cast hk1
    have h2 : -1 < k := by exact_mod_cast hk2
    omega
  subst hk0
  simpa using hr

variable (F : PairFlow)

/-- The orthogonality relations on the entries. -/
theorem PairFlow.pairFlow_orth_entries (t : ℝ) :
    F.A t 0 0 ^ 2 + F.A t 1 0 ^ 2 = 1 ∧ F.A t 0 1 ^ 2 + F.A t 1 1 ^ 2 = 1
      ∧ F.A t 0 0 * F.A t 0 1 + F.A t 1 0 * F.A t 1 1 = 0 := by
  have h00 := congrFun (congrFun (F.orth t) 0) 0
  have h11 := congrFun (congrFun (F.orth t) 1) 1
  have h01 := congrFun (congrFun (F.orth t) 0) 1
  simp only [Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_two, Matrix.one_apply] at h00 h11 h01
  simp at h00 h11 h01
  refine ⟨by nlinarith [h00], by nlinarith [h11], by linarith [h01]⟩

theorem PairFlow.pairFlow_det_sq (t : ℝ) : (F.A t).det ^ 2 = 1 := by
  have := congrArg Matrix.det (F.orth t)
  rw [Matrix.det_mul, Matrix.det_transpose, Matrix.det_one] at this
  nlinarith [this]

/-- **THE DETERMINANT IS ONE EVERYWHERE**: continuous, valued in `±1`, one at zero, on the
connected line. -/
theorem PairFlow.pairFlow_det_one (t : ℝ) : (F.A t).det = 1 := by
  have hsq := F.pairFlow_det_sq
  have hcont : Continuous fun s => (F.A s).det := F.cont.matrix_det
  by_contra h
  have h1 : (F.A t).det = -1 := by
    have := hsq t
    have : ((F.A t).det - 1) * ((F.A t).det + 1) = 0 := by linear_combination this
    rcases mul_eq_zero.mp this with h' | h'
    · exact absurd (by linear_combination h') h
    · linear_combination h'
  have h0 : (F.A 0).det = 1 := by rw [F.zero, Matrix.det_one]
  have hmem : (0 : ℝ) ∈ Set.uIcc ((fun s => (F.A s).det) 0) ((fun s => (F.A s).det) t) := by
    simp only [h0, h1]
    rw [Set.mem_uIcc]
    right
    constructor <;> norm_num
  obtain ⟨s, -, hs⟩ := intermediate_value_uIcc hcont.continuousOn hmem
  have := hsq s
  simp only at hs
  rw [hs] at this
  norm_num at this

/-- **EVERY VALUE IS A ROTATION OF THE PLANE**, in the form `[[a, −c], [c, a]]`. -/
theorem PairFlow.pairFlow_form (t : ℝ) :
    F.A t = !![F.A t 0 0, -(F.A t 1 0); F.A t 1 0, F.A t 0 0] := by
  obtain ⟨h1, -, h2⟩ := F.pairFlow_orth_entries t
  have hdet := F.pairFlow_det_one t
  rw [Matrix.det_fin_two] at hdet
  have hd : F.A t 1 1 = F.A t 0 0 := by
    linear_combination (-(F.A t 1 1)) * h1 + F.A t 0 0 * hdet + F.A t 1 0 * h2
  have hb : F.A t 0 1 = -(F.A t 1 0) := by
    linear_combination (-(F.A t 0 1)) * h1 - F.A t 1 0 * hdet + F.A t 0 0 * h2
  ext i j
  fin_cases i <;> fin_cases j <;> simp [hd, hb]

/-- The local angle: the arcsine of the moved entry. -/
noncomputable def PairFlow.ang (t : ℝ) : ℝ := Real.arcsin (F.A t 1 0)

theorem PairFlow.pairFlow_abs_lt_one {t : ℝ} (ht : 0 < F.A t 0 0) : |F.A t 1 0| < 1 := by
  obtain ⟨h1, -, -⟩ := F.pairFlow_orth_entries t
  have : F.A t 1 0 ^ 2 < 1 := by nlinarith
  rw [← sq_lt_one_iff_abs_lt_one]
  exact this

/-- **ON THE POSITIVE-COSINE REGION THE VALUE IS THE ROTATION BY THE LOCAL ANGLE.** -/
theorem PairFlow.pairFlow_eq_rotR_ang {t : ℝ} (ht : 0 < F.A t 0 0) : F.A t = rotR (F.ang t) := by
  obtain ⟨h1, -, -⟩ := F.pairFlow_orth_entries t
  have hc := abs_lt.mp (F.pairFlow_abs_lt_one ht)
  have hsin : Real.sin (F.ang t) = F.A t 1 0 := Real.sin_arcsin hc.1.le hc.2.le
  have hcos : Real.cos (F.ang t) = F.A t 0 0 := by
    rw [PairFlow.ang, Real.cos_arcsin]
    have : 1 - F.A t 1 0 ^ 2 = F.A t 0 0 ^ 2 := by linear_combination (-1 : ℝ) * h1
    rw [this, Real.sqrt_sq ht.le]
  rw [F.pairFlow_form t]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rotR, hsin, hcos]

theorem PairFlow.pairFlow_ang_abs_lt {t : ℝ} (ht : 0 < F.A t 0 0) : |F.ang t| < Real.pi / 2 := by
  have hc := abs_lt.mp (F.pairFlow_abs_lt_one ht)
  rw [abs_lt]
  exact ⟨Real.neg_pi_div_two_lt_arcsin.mpr hc.1, Real.arcsin_lt_pi_div_two.mpr hc.2⟩

/-- **THE POSITIVE-COSINE REGION CONTAINS AN INTERVAL AROUND ZERO**, by continuity. -/
theorem PairFlow.pairFlow_exists_eps : ∃ ε : ℝ, 0 < ε ∧ ∀ t : ℝ, |t| < ε → 0 < F.A t 0 0 := by
  have hc : Continuous fun s => F.A s 0 0 := F.cont.matrix_elem 0 0
  have h0 : (fun s => F.A s 0 0) 0 = 1 := by simp [F.zero]
  obtain ⟨δ, hδ, hδ'⟩ := Metric.continuousAt_iff.mp hc.continuousAt 1 one_pos
  refine ⟨δ, hδ, fun t ht => ?_⟩
  have := hδ' (by rw [Real.dist_eq, sub_zero]; exact ht)
  have h0' : F.A 0 0 0 = 1 := by simp [F.zero]
  rw [h0', Real.dist_eq] at this
  have := (abs_lt.mp this).1
  linarith

/-- The inverse is the transpose: `A (−t) = (A t)ᵀ`. -/
theorem PairFlow.pairFlow_neg (t : ℝ) : F.A (-t) = (F.A t)ᵀ := by
  have h1 : F.A t * F.A (-t) = 1 := by rw [← F.add, add_neg_cancel, F.zero]
  calc F.A (-t) = ((F.A t)ᵀ * F.A t) * F.A (-t) := by rw [F.orth, Matrix.one_mul]
    _ = (F.A t)ᵀ * (F.A t * F.A (-t)) := by rw [Matrix.mul_assoc]
    _ = (F.A t)ᵀ := by rw [h1, Matrix.mul_one]

theorem PairFlow.pairFlow_ang_neg {t : ℝ} : F.ang (-t) = -F.ang t := by
  have : F.A (-t) 1 0 = -(F.A t 1 0) := by
    rw [F.pairFlow_neg, Matrix.transpose_apply]
    have := congrFun (congrFun (F.pairFlow_form t) 0) 1
    simpa using this
  rw [PairFlow.ang, PairFlow.ang, this, Real.arcsin_neg]

theorem PairFlow.pairFlow_ang_zero : F.ang 0 = 0 := by
  simp [PairFlow.ang, F.zero]

theorem PairFlow.pairFlow_pow (x : ℝ) : ∀ k : ℕ, F.A (k * x) = F.A x ^ k := by
  intro k
  induction k with
  | zero => simp [F.zero]
  | succ k ih => rw [pow_succ, ← ih, ← F.add]; push_cast; ring_nf

/-- **THE LOCAL ANGLE IS ADDITIVE ON THE HALF-INTERVAL**, by the group law and the injectivity of
rotations on small angles. -/
theorem PairFlow.pairFlow_ang_add {ε : ℝ} (hε : ∀ t : ℝ, |t| < ε → 0 < F.A t 0 0) {s t : ℝ}
    (hs : |s| < ε / 2) (ht : |t| < ε / 2) : F.ang (s + t) = F.ang s + F.ang t := by
  have hs' : 0 < F.A s 0 0 := hε s (by linarith [abs_nonneg s])
  have ht' : 0 < F.A t 0 0 := hε t (by linarith [abs_nonneg t])
  have hst' : 0 < F.A (s + t) 0 0 := hε (s + t) (by
    calc |s + t| ≤ |s| + |t| := abs_add_le _ _
      _ < ε := by linarith)
  have h : rotR (F.ang (s + t)) = rotR (F.ang s + F.ang t) := by
    rw [← rotR_mul, ← F.pairFlow_eq_rotR_ang hs', ← F.pairFlow_eq_rotR_ang ht',
      ← F.pairFlow_eq_rotR_ang hst', F.add]
  refine rotR_inj_small (F.pairFlow_ang_abs_lt hst') ?_ h
  have h1 := abs_lt.mp (F.pairFlow_ang_abs_lt hs')
  have h2 := abs_lt.mp (F.pairFlow_ang_abs_lt ht')
  rw [abs_lt]
  constructor <;> linarith

theorem PairFlow.pairFlow_ang_nsmul {ε : ℝ} (hε : ∀ t : ℝ, |t| < ε → 0 < F.A t 0 0) {x : ℝ}
    (hx : |x| < ε / 2) : ∀ k : ℕ, |(k : ℝ) * x| < ε / 2 → F.ang (k * x) = k * F.ang x := by
  intro k
  induction k with
  | zero => intro _; simp [F.pairFlow_ang_zero]
  | succ k ih =>
    intro hk
    have hkx : |(k : ℝ) * x| < ε / 2 := by
      calc |(k : ℝ) * x| = k * |x| := by rw [abs_mul, Nat.abs_cast]
        _ ≤ (k + 1) * |x| := by nlinarith [abs_nonneg x]
        _ = |((k + 1 : ℕ) : ℝ) * x| := by rw [abs_mul, Nat.abs_cast]; push_cast; ring
        _ < ε / 2 := hk
    have : ((k + 1 : ℕ) : ℝ) * x = k * x + x := by push_cast; ring
    rw [this, F.pairFlow_ang_add hε hkx hx, ih hkx]
    push_cast; ring

theorem PairFlow.pairFlow_ang_zsmul {ε : ℝ} (hε : ∀ t : ℝ, |t| < ε → 0 < F.A t 0 0) {x : ℝ}
    (hx : |x| < ε / 2) (m : ℤ) (hm : |(m : ℝ) * x| < ε / 2) : F.ang (m * x) = m * F.ang x := by
  rcases le_or_gt 0 m with h | h
  · obtain ⟨k, rfl⟩ := Int.eq_ofNat_of_zero_le h
    have := F.pairFlow_ang_nsmul hε hx k (by simpa using hm)
    simpa using this
  · obtain ⟨k, hk⟩ : ∃ k : ℕ, m = -(k : ℤ) := ⟨m.natAbs, by omega⟩
    subst hk
    have hm' : |(k : ℝ) * x| < ε / 2 := by
      have := hm; push_cast at this; rwa [neg_mul, abs_neg] at this
    have := F.pairFlow_ang_nsmul hε hx k hm'
    push_cast
    rw [neg_mul, F.pairFlow_ang_neg, this]
    ring

/-- The continuity of the local angle. -/
theorem PairFlow.pairFlow_ang_continuous : Continuous F.ang :=
  Real.continuous_arcsin.comp (F.cont.matrix_elem 1 0)

/-- **THE LOCAL ANGLE IS LINEAR ON A CLOSED INTERVAL AROUND ZERO**: additive on rational multiples
of the interval's endpoint, and continuous, so linear by density. -/
theorem PairFlow.pairFlow_ang_linear {ε : ℝ} (hε0 : 0 < ε) (hε : ∀ t : ℝ, |t| < ε → 0 < F.A t 0 0) :
    ∃ ω : ℝ, ∀ t : ℝ, |t| ≤ ε / 4 → F.ang t = ω * t := by
  set η : ℝ := ε / 4 with hη
  have hη0 : 0 < η := by rw [hη]; linarith
  have hηlt : |η| < ε / 2 := by rw [abs_of_pos hη0, hη]; linarith
  refine ⟨F.ang η / η, ?_⟩
  -- the clamped functions
  let clamp : ℝ → ℝ := fun t => max (-η) (min η t)
  have hclamp_cont : Continuous clamp := continuous_const.max (continuous_const.min continuous_id)
  have hclamp_abs : ∀ t, |clamp t| ≤ η := by
    intro t
    rw [abs_le]
    constructor
    · exact le_max_left _ _
    · exact max_le (by linarith) (min_le_left _ _)
  have hclamp_eq : ∀ t, |t| ≤ η → clamp t = t := by
    intro t ht
    obtain ⟨h1, h2⟩ := abs_le.mp ht
    simp only [clamp]
    rw [min_eq_right h2, max_eq_right h1]
  let f : ℝ → ℝ := fun t => F.ang (clamp t)
  let g : ℝ → ℝ := fun t => F.ang η / η * clamp t
  have hf : Continuous f := F.pairFlow_ang_continuous.comp hclamp_cont
  have hg : Continuous g := continuous_const.mul hclamp_cont
  -- agreement on the rational multiples of `η`
  have hdense : Dense (Set.range fun q : ℚ => (q : ℝ) * η) := by
    have hsurj : Function.Surjective fun x : ℝ => x * η := fun y => ⟨y / η, by field_simp⟩
    have hd : DenseRange ((fun x : ℝ => x * η) ∘ ((↑) : ℚ → ℝ)) :=
      hsurj.denseRange.comp Rat.denseRange_cast (continuous_id.mul continuous_const)
    exact hd
  have hvalue : ∀ q : ℚ, |(q : ℝ)| ≤ 1 → F.ang ((q : ℝ) * η) = F.ang η / η * ((q : ℝ) * η) := by
    intro q hq
    have hden : (0 : ℝ) < q.den := by exact_mod_cast q.den_pos
    set x : ℝ := η / q.den with hx
    have hx0 : 0 < x := div_pos hη0 hden
    have hxlt : |x| < ε / 2 := by
      rw [abs_of_pos hx0, hx]
      calc η / q.den ≤ η / 1 := by gcongr; exact_mod_cast q.den_pos
        _ = η := div_one η
        _ < ε / 2 := by rw [hη]; linarith
    have hnum : (q : ℝ) = q.num / q.den := by exact_mod_cast (Rat.num_div_den q).symm
    have hqη : (q : ℝ) * η = (q.num : ℝ) * x := by
      rw [hnum, hx]
      field_simp
    have hηx : η = (q.den : ℝ) * x := by rw [hx]; field_simp
    have h1 : F.ang η = q.den * F.ang x := by
      have := F.pairFlow_ang_nsmul hε hxlt q.den (by rw [← hηx]; exact hηlt)
      rwa [← hηx] at this
    have h2 : F.ang ((q.num : ℝ) * x) = q.num * F.ang x := by
      apply F.pairFlow_ang_zsmul hε hxlt
      rw [← hqη, abs_mul, abs_of_pos hη0]
      calc |(q : ℝ)| * η ≤ 1 * η := by gcongr
        _ = η := one_mul η
        _ < ε / 2 := by rw [hη]; linarith
    rw [hqη, h2, h1]
    have hxne : x ≠ 0 := hx0.ne'
    have hdne : (q.den : ℝ) ≠ 0 := hden.ne'
    rw [hηx]
    field_simp
  have heq : Set.EqOn f g (Set.range fun q : ℚ => (q : ℝ) * η) := by
    rintro _ ⟨q, rfl⟩
    simp only [f, g]
    rcases le_or_gt |(q : ℝ)| 1 with hq | hq
    · have hc : clamp ((q : ℝ) * η) = (q : ℝ) * η := by
        apply hclamp_eq
        rw [abs_mul, abs_of_pos hη0]
        calc |(q : ℝ)| * η ≤ 1 * η := by gcongr
          _ = η := one_mul η
      rw [hc]
      exact hvalue q hq
    · rcases le_or_gt 0 (q : ℝ) with hq0 | hq0
      · have hq1 : 1 < (q : ℝ) := by rwa [abs_of_nonneg hq0] at hq
        have hc : clamp ((q : ℝ) * η) = η := by
          simp only [clamp]
          rw [min_eq_left (by nlinarith), max_eq_right (by linarith)]
        rw [hc]
        field_simp
      · have hq1 : (q : ℝ) < -1 := by rw [abs_of_neg hq0] at hq; linarith
        have hc : clamp ((q : ℝ) * η) = -η := by
          simp only [clamp]
          rw [min_eq_right (by nlinarith), max_eq_left (by nlinarith)]
        rw [hc, F.pairFlow_ang_neg]
        field_simp
  have hfg : f = g := hf.ext_on hdense hg heq
  intro t ht
  have := congrFun hfg t
  simp only [f, g] at this
  rwa [hclamp_eq t ht] at this

/-- **T2 — THE REDUCTION**: a real pair flow is a rotation family at a nonzero rate. -/
theorem PairFlow.pairFlow_rate : ∃ ω : ℝ, ω ≠ 0 ∧ ∀ t : ℝ, F.A t = rotR (ω * t) := by
  obtain ⟨ε, hε0, hε⟩ := F.pairFlow_exists_eps
  obtain ⟨ω, hω⟩ := F.pairFlow_ang_linear hε0 hε
  have hall : ∀ t : ℝ, F.A t = rotR (ω * t) := by
    intro t
    obtain ⟨n, hn⟩ := exists_nat_ge (|t| / (ε / 4))
    set m : ℕ := n + 1 with hm
    have hm0 : (0 : ℝ) < m := by rw [hm]; positivity
    have hsmall : |t / m| ≤ ε / 4 := by
      rw [abs_div, abs_of_pos hm0, div_le_iff₀ hm0]
      have : |t| ≤ ε / 4 * n := by
        rwa [div_le_iff₀ (by linarith : (0 : ℝ) < ε / 4), mul_comm] at hn
      rw [hm]; push_cast
      nlinarith
    have hpos : 0 < F.A (t / m) 0 0 := hε _ (by
      have := hsmall
      linarith [abs_nonneg (t / m)])
    have hlin : F.ang (t / m) = ω * (t / m) := hω _ hsmall
    have ht : t = (m : ℝ) * (t / m) := by field_simp
    calc F.A t = F.A ((m : ℝ) * (t / m)) := by rw [← ht]
      _ = F.A (t / m) ^ m := F.pairFlow_pow _ m
      _ = rotR (F.ang (t / m)) ^ m := by rw [F.pairFlow_eq_rotR_ang hpos]
      _ = rotR (m * (ω * (t / m))) := by rw [rotR_pow, hlin]
      _ = rotR (ω * t) := by congr 1; field_simp
  refine ⟨ω, ?_, hall⟩
  rintro rfl
  obtain ⟨t, ht⟩ := F.nontrivial
  apply ht
  rw [hall t, zero_mul, rotR_zero]

/-- **THE SUPPLY**: after reparameterizing time, the transport of a pair flow is the mixing datum
at every level and angle. -/
theorem PairFlow.pairFlow_supplies_mixImage (n : ℕ) (θ : ℝ) :
    ∃ t : ℝ, transport n (F.A t) = mixImage n θ := by
  obtain ⟨ω, hω, hall⟩ := F.pairFlow_rate
  refine ⟨θ / ω, ?_⟩
  rw [hall, mul_div_cancel₀ θ hω, transport_rotR]

end Reduction

/-! ### Section C — T3: the composition with the construction audit -/

section Composition

variable (F : PairFlow)

/-- **THE CLASS-LEVEL ENDPOINT FOR A SOURCED PAIR FLOW**, under the construction audit's scope
amendment: architecture, the three stabilities, the stated access, the phase gates and the
transports of a pair flow at every level and time give the closure and exact finite operational
quantum mechanics on the two-valued alphabet. -/
theorem qm_of_pairFlowSourced {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hl : LabelInvariant 𝓘) (hd : DaggerStable 𝓘) (hc : ContextStable 𝓘)
    (hperm : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), permClass T K → 𝓘 T K)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p))
    (hflow : ∀ (n : ℕ) (t : ℝ), 𝓘 (Fin 2 × Fin n) (transport n (F.A t))) :
    DerivedOI (genTheory 𝓘 arch (Fin 2))
      ∧ ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2)) := by
  refine qm_of_mixSourced arch hl hd hc hperm hph fun n θ => ?_
  obtain ⟨t, ht⟩ := F.pairFlow_supplies_mixImage n θ
  rw [← ht]
  exact hflow n t

/-- **THE PAIR-FLOW CLASS**: the stated access and the transports of one pair flow at every level
and time, closed under the architecture operations and relabelling. -/
inductive FlowR (F : PairFlow) : ∀ (T : Type) [Fintype T] [DecidableEq T], Matrix T T ℂ → Prop
  | perm {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : permClass T K) : FlowR F T K
  | phase (n : ℕ) (p : Fin 2 × Fin n) : FlowR F (Fin 2 × Fin n) (phaseGate p)
  | flow (n : ℕ) (t : ℝ) : FlowR F (Fin 2 × Fin n) (transport n (F.A t))
  | mul {T : Type} [Fintype T] [DecidableEq T] (K L : Matrix T T ℂ) :
      FlowR F T K → FlowR F T L → FlowR F T (K * L)
  | smul {T : Type} [Fintype T] [DecidableEq T] (a : ℂ) (K : Matrix T T ℂ) (ha : ‖a‖ ≤ 1) :
      FlowR F T K → FlowR F T (a • K)
  | proj {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (k : Fin m) :
      FlowR F (T × Fin m) (Matrix.diagonal fun r => if r.2 = k then 1 else 0)
  | block {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (K : Matrix (T × Fin m) (T × Fin m) ℂ)
      (f e : Fin m) : FlowR F (T × Fin m) K → FlowR F T (ancBlock K f e)
  | relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T')
      (K : Matrix T T ℂ) : FlowR F T K → FlowR F T' (Matrix.reindex e e K)

theorem flowR_arch : Architecture (FlowR F) where
  one := fun T _ _ => FlowR.perm 1 (permClass_arch.one T)
  mul := fun _ _ _ K L hK hL => FlowR.mul K L hK hL
  smul := fun _ _ _ a K ha hK => FlowR.smul a K ha hK
  proj := fun _ _ _ m k => FlowR.proj m k
  block := fun _ _ _ m K f e hK => FlowR.block m K f e hK

theorem flowR_labelInvariant : LabelInvariant (FlowR F) :=
  fun _ _ _ _ _ _ e K h => FlowR.relabel e K h

/-- **THE PAIR-FLOW CLASS IS THE CONSTRUCTION AUDIT'S CLASS**: the transports of the flow are the
datum at the reparameterized angles, and conversely. -/
theorem flowR_eq_mixC : FlowR F = MixC := by
  obtain ⟨ω, hω, hall⟩ := F.pairFlow_rate
  funext T _ _ K
  apply propext
  constructor
  · intro h
    induction h with
    | perm K h => exact MixR.perm K h
    | phase n p => exact MixR.phase n p
    | flow n t => rw [hall, transport_rotR]; exact mixC_mix n _
    | mul K L _ _ ihK ihL => exact MixR.mul K L ihK ihL
    | smul a K ha _ ih => exact MixR.smul a K ha ih
    | proj m k => exact MixR.proj m k
    | block m K f e _ ih => exact MixR.block m K f e ih
    | relabel e K _ ih => exact MixR.relabel e K ih
  · intro h
    induction h with
    | perm K h => exact FlowR.perm K h
    | phase n p => exact FlowR.phase n p
    | mix n θ _ =>
      have : mixImage n θ = transport n (F.A (θ / ω)) := by
        rw [hall, mul_div_cancel₀ θ hω, transport_rotR]
      rw [this]; exact FlowR.flow n _
    | mul K L _ _ ihK ihL => exact FlowR.mul K L ihK ihL
    | smul a K ha _ ih => exact FlowR.smul a K ha ih
    | proj m k => exact FlowR.proj m k
    | block m K f e _ ih => exact FlowR.block m K f e ih
    | relabel e K _ ih => exact FlowR.relabel e K ih

theorem flowR_daggerStable : DaggerStable (FlowR F) := by
  rw [flowR_eq_mixC]; exact mixC_daggerStable

theorem flowR_contextStable : ContextStable (FlowR F) := by
  rw [flowR_eq_mixC]; exact mixC_contextStable

/-- **THE PAIR-FLOW THEORY**: the stated access with one pair flow, closed. -/
noncomputable def pairFlowTheory (S : Type) [Fintype S] [DecidableEq S] : FiniteOperationalTheory S :=
  genTheory (FlowR F) (flowR_arch F) S

/-- **T3 — THE PAIR-FLOW THEORY SATISFIES THE CLOSURE AND IS QUANTUM MECHANICS.** -/
theorem pairFlowTheory_endpoint :
    DerivedOI (pairFlowTheory F (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (pairFlowTheory F (Fin 2)) :=
  qm_of_pairFlowSourced F (flowR_arch F) (flowR_labelInvariant F) (flowR_daggerStable F)
    (flowR_contextStable F) (fun _ _ _ K h => FlowR.perm K h) (fun n p => FlowR.phase n p)
    (fun n t => FlowR.flow n t)

theorem pairFlowTheory_qm : ExactAllFiniteEndomorphicQuantumOps (pairFlowTheory F (Fin 2)) :=
  (pairFlowTheory_endpoint F).2

end Composition

/-! ### Section D — T4: the countercontrols -/

section Countercontrols

/-- The shear: identity, group law, continuity, determinant one, nontriviality, no orthogonality. -/
def shearFlow (t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := !![1, t; 0, 1]

/-- The boost: identity, group law, continuity, determinant one, nontriviality, no orthogonality. -/
noncomputable def boostFlow (t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![Real.cosh t, Real.sinh t; Real.sinh t, Real.cosh t]

/-- The constant identity: every hypothesis but nontriviality. -/
def constFlow (_ : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := 1

theorem shearFlow_zero : shearFlow 0 = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [shearFlow]

theorem shearFlow_add (s t : ℝ) : shearFlow (s + t) = shearFlow s * shearFlow t := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [shearFlow, Matrix.mul_apply, Fin.sum_univ_two, add_comm]

theorem shearFlow_continuous : Continuous shearFlow := by
  refine continuous_matrix fun i j => ?_
  fin_cases i <;> fin_cases j <;> simp [shearFlow] <;> fun_prop

theorem shearFlow_det_one (t : ℝ) : (shearFlow t).det = 1 := by
  simp [shearFlow, Matrix.det_fin_two_of]

theorem shearFlow_not_orth {t : ℝ} (ht : t ≠ 0) : (shearFlow t)ᵀ * shearFlow t ≠ 1 := by
  intro h
  have := congrFun (congrFun h 0) 1
  simp [shearFlow, Matrix.mul_apply, Fin.sum_univ_two] at this
  exact ht this

/-- **THE SHEAR CONTAINS NO DATUM OUTSIDE `πℤ`**: its moved entry vanishes. -/
theorem shearFlow_ne_rotR {θ : ℝ} (hθ : Real.sin θ ≠ 0) (t : ℝ) : shearFlow t ≠ rotR θ := by
  intro h
  have := congrFun (congrFun h 1) 0
  simp [shearFlow, rotR] at this
  exact hθ this.symm

/-- **THE SHEAR SATISFIES EVERY HYPOTHESIS BUT ORTHOGONALITY**, with determinant one throughout:
measure preservation alone, and continuity with reversibility alone, are insufficient. -/
theorem shearFlow_all_but_orth :
    shearFlow 0 = 1 ∧ (∀ s t : ℝ, shearFlow (s + t) = shearFlow s * shearFlow t)
      ∧ Continuous shearFlow ∧ (∀ t : ℝ, (shearFlow t).det = 1) ∧ (∃ t : ℝ, shearFlow t ≠ 1)
      ∧ ¬ (∀ t : ℝ, (shearFlow t)ᵀ * shearFlow t = 1) :=
  ⟨shearFlow_zero, shearFlow_add, shearFlow_continuous, shearFlow_det_one,
    ⟨1, fun h => by
      have := congrFun (congrFun h 0) 1
      simp [shearFlow] at this⟩,
    fun h => shearFlow_not_orth one_ne_zero (h 1)⟩

theorem boostFlow_zero : boostFlow 0 = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [boostFlow]

theorem boostFlow_add (s t : ℝ) : boostFlow (s + t) = boostFlow s * boostFlow t := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [boostFlow, Matrix.mul_apply, Fin.sum_univ_two, Real.cosh_add, Real.sinh_add] <;> ring

theorem boostFlow_continuous : Continuous boostFlow := by
  refine continuous_matrix fun i j => ?_
  fin_cases i <;> fin_cases j <;> simp [boostFlow] <;> fun_prop

theorem boostFlow_det_one (t : ℝ) : (boostFlow t).det = 1 := by
  simp only [boostFlow, Matrix.det_fin_two_of]
  have := Real.cosh_sq_sub_sinh_sq t
  linear_combination this

theorem boostFlow_not_orth {t : ℝ} (ht : Real.sinh t ≠ 0) : (boostFlow t)ᵀ * boostFlow t ≠ 1 := by
  intro h
  have h00 := congrFun (congrFun h 0) 0
  simp [boostFlow, Matrix.mul_apply, Fin.sum_univ_two] at h00
  -- `cosh² + sinh² = 1` with `cosh² − sinh² = 1` forces `sinh t = 0`
  have h1 := Real.cosh_sq_sub_sinh_sq t
  have hs : Real.sinh t ^ 2 = 0 := by nlinarith [h00, h1]
  exact ht (pow_eq_zero_iff two_ne_zero |>.mp hs)

/-- **THE BOOST CONTAINS NO DATUM OUTSIDE `πℤ`**: matching a rotation forces `sin θ = 0`. -/
theorem boostFlow_ne_rotR {θ : ℝ} (hθ : Real.sin θ ≠ 0) (t : ℝ) : boostFlow t ≠ rotR θ := by
  intro h
  have h00 := congrFun (congrFun h 0) 0
  have h10 := congrFun (congrFun h 1) 0
  simp [boostFlow, rotR] at h00 h10
  have h1 := Real.cosh_sq_sub_sinh_sq t
  have h2 := Real.cos_sq_add_sin_sq θ
  rw [h00, h10] at h1
  have : Real.sin θ ^ 2 = 0 := by linarith
  exact hθ (pow_eq_zero_iff two_ne_zero |>.mp this)

theorem sinh_one_pos : 0 < Real.sinh 1 := by
  rw [Real.sinh_eq]
  have := Real.exp_lt_exp.mpr (show (-1 : ℝ) < 1 by norm_num)
  linarith

theorem boostFlow_all_but_orth :
    boostFlow 0 = 1 ∧ (∀ s t : ℝ, boostFlow (s + t) = boostFlow s * boostFlow t)
      ∧ Continuous boostFlow ∧ (∀ t : ℝ, (boostFlow t).det = 1) ∧ (∃ t : ℝ, boostFlow t ≠ 1)
      ∧ ¬ (∀ t : ℝ, (boostFlow t)ᵀ * boostFlow t = 1) :=
  ⟨boostFlow_zero, boostFlow_add, boostFlow_continuous, boostFlow_det_one,
    ⟨1, fun h => by
      have := congrFun (congrFun h 1) 0
      simp [boostFlow] at this
      exact sinh_one_pos.ne' this⟩,
    fun h => boostFlow_not_orth sinh_one_pos.ne' (h 1)⟩

theorem constFlow_all_but_nontrivial :
    constFlow 0 = 1 ∧ (∀ s t : ℝ, constFlow (s + t) = constFlow s * constFlow t)
      ∧ Continuous constFlow ∧ (∀ t : ℝ, (constFlow t)ᵀ * constFlow t = 1)
      ∧ ¬ (∃ t : ℝ, constFlow t ≠ 1) :=
  ⟨rfl, fun _ _ => by simp [constFlow], continuous_const, fun _ => by simp [constFlow],
    fun ⟨_, h⟩ => h rfl⟩

/-- **THE CONSTANT IDENTITY TRANSPORTS TO THE IDENTITY**, so its closure with the stated access is
the no-datum replacement of the construction audit. -/
theorem constFlow_transport (n : ℕ) (t : ℝ) : transport n (constFlow t) = 1 := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [transport, constFlow, Matrix.of_apply, Matrix.one_apply, Prod.mk.injEq]
  by_cases hk : k = l <;> by_cases hx : x = y <;> simp [hk, hx]

end Countercontrols

end RealPairFlow
end OIBridge

#print axioms OIBridge.RealPairFlow.rotR_inj_small
#print axioms OIBridge.RealPairFlow.transport_rotR
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_det_one
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_form
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_eq_rotR_ang
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_exists_eps
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_ang_add
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_ang_linear
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_rate
#print axioms OIBridge.RealPairFlow.PairFlow.pairFlow_supplies_mixImage
#print axioms OIBridge.RealPairFlow.qm_of_pairFlowSourced
#print axioms OIBridge.RealPairFlow.flowR_eq_mixC
#print axioms OIBridge.RealPairFlow.pairFlowTheory_endpoint
#print axioms OIBridge.RealPairFlow.pairFlowTheory_qm
#print axioms OIBridge.RealPairFlow.shearFlow_all_but_orth
#print axioms OIBridge.RealPairFlow.shearFlow_ne_rotR
#print axioms OIBridge.RealPairFlow.boostFlow_all_but_orth
#print axioms OIBridge.RealPairFlow.boostFlow_ne_rotR
#print axioms OIBridge.RealPairFlow.constFlow_all_but_nontrivial
#print axioms OIBridge.RealPairFlow.constFlow_transport
