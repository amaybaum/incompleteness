import OIBridge.PhaseSource
import OIBridge.FrozenSourcing

/-!
# SUBSTATE-2 unit F2-1, stage 2 — the fixed-statement control declarations

Research-only kernel controls for the preregistration
`verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/preregistration.md`
(frozen at `66eb48ca`) and its amendment `A★` (`amendments/A-star.md`, at `b86f0547`). The
statements of the nineteen declarations listed in `A★` §A★5 are copied verbatim from that
amendment; only the proofs and the auxiliary lemmas marked as such are added here.

The declarations decide predicates for the stage-2 *controls* only: the ones-bounded theory
predicate, the two consistency facts for the falsifier `rot` (it moves the all-ones ray and does
not preserve nonnegative entries, so a nonnegativity- or ones-bounded theory lacks it), the
ones-bounded property of the sourced and ones-fixing classes, the nonnegative class used for the
Koopman-compression control and its two invariants, the real-amplitude class that has `rot` and
lacks the quarter phase, and the full class as the positive control. No candidate interface is
treated here: stage 1 fixed none.

Not claimed: anything about a candidate F2 extension, a sourcing of `rot` or of the phases by OI,
a no-go for observer-level extensions, or any manuscript statement.
-/

namespace OIBridge
namespace F2CoherenceControls

open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion

/-! ### Auxiliary entry lemmas for `rot` (not among the fixed statements) -/

theorem rot_00 :
    DiagonalTheory.rot ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) = ((3 / 5 : ℝ) : ℂ) := by
  simp [DiagonalTheory.rot]

theorem rot_01 :
    DiagonalTheory.rot ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) = ((4 / 5 : ℝ) : ℂ) := by
  simp [DiagonalTheory.rot]

theorem rot_10 :
    DiagonalTheory.rot ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) = -((4 / 5 : ℝ) : ℂ) := by
  simp [DiagonalTheory.rot]

theorem rot_11 :
    DiagonalTheory.rot ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) = ((3 / 5 : ℝ) : ℂ) := by
  simp [DiagonalTheory.rot]

/-! ### The fixed statements of `A★` §A★5 -/

def OnesBounded {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 →
    T.availExt n Unit (fun _ => conjChannel U) →
      ∃ z : ℂ, U *ᵥ InstrumentRealization.ones (A × Fin n) = z • InstrumentRealization.ones (A × Fin n)

theorem rot_not_preservesNonneg :
    ¬ SubstratumInterfaceAudit.PreservesNonneg (conjChannel DiagonalTheory.rot) := by
  intro h
  have hX : ∀ p q : Fin 2 × Fin 1, (0 : ℂ) ≤
      (Matrix.diagonal fun r : Fin 2 × Fin 1 => if r.1 = 0 then (1 : ℂ) else 0) p q := by
    intro p q
    simp only [Matrix.diagonal_apply]
    split_ifs <;> first | exact zero_le_one | exact le_rfl
  have hval : (0 : ℂ) ≤ conjChannel DiagonalTheory.rot
      (Matrix.diagonal fun r : Fin 2 × Fin 1 => if r.1 = 0 then (1 : ℂ) else 0)
      ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) := h _ hX _ _
  have e : conjChannel DiagonalTheory.rot
      (Matrix.diagonal fun r : Fin 2 × Fin 1 => if r.1 = 0 then (1 : ℂ) else 0)
      ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
      = DiagonalTheory.rot ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
        * star (DiagonalTheory.rot ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))) := by
    simp [AncillaClosure.conjChannel_apply, Matrix.mul_apply, Matrix.mul_diagonal,
      Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two]
  rw [e, rot_00, rot_10, star_neg, Complex.star_def, Complex.conj_ofReal, mul_neg,
    ← Complex.ofReal_mul, ← Complex.ofReal_neg, Complex.zero_le_real] at hval
  norm_num at hval

theorem rot_moves_ones :
    ¬ ∃ z : ℂ, DiagonalTheory.rot *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = z • InstrumentRealization.ones (Fin 2 × Fin 1) := by
  rintro ⟨z, hz⟩
  have h0 := congrFun hz ((0 : Fin 2), (0 : Fin 1))
  have h1 := congrFun hz ((1 : Fin 2), (0 : Fin 1))
  first
  | (simp only [Matrix.mulVec, dotProduct, InstrumentRealization.ones_apply, mul_one,
        Pi.smul_apply, smul_eq_mul, Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_one]
        at h0 h1
     rw [rot_00, rot_01] at h0
     rw [rot_10, rot_11] at h1
     have h := congrArg Complex.re (h0.trans h1.symm)
     simp only [Complex.add_re, Complex.ofReal_re, Complex.neg_re] at h
     norm_num at h)
  | (have h := h0.trans h1.symm
     simp [Matrix.mulVec, dotProduct, InstrumentRealization.ones, Fintype.sum_prod_type,
       Fin.sum_univ_two, DiagonalTheory.rot] at h <;> norm_num at h)

theorem falsifierUnavailable_of_nonnegBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : FrozenSourcing.NonnegBounded T) : RouteB.FalsifierUnavailable T :=
  fun hav => rot_not_preservesNonneg (h 1 _ hav)

theorem falsifierUnavailable_of_onesBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : OnesBounded T) : RouteB.FalsifierUnavailable T :=
  fun hav => rot_moves_ones (h 1 DiagonalTheory.rot DiagonalTheory.rot_isometry hav)

theorem onesBounded_of_onesFixing {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hf : InstrumentRealization.OnesFixing 𝓘) {A : Type} [Fintype A] [DecidableEq A] :
    OnesBounded (InterventionLocality.genTheory 𝓘 arch A) :=
  fun _ _ hU hav => InstrumentRealization.instAvail_unitary_fixes_ones hf hU hav

theorem permTheory_onesBounded : OnesBounded (SubstratumInterfaceAudit.permTheory (Fin 2)) :=
  onesBounded_of_onesFixing SubstratumInterfaceAudit.permClass_arch PhaseSource.permClass_onesFixing

theorem onesTheory_falsifierUnavailable : RouteB.FalsifierUnavailable (FlowEndpoint.onesTheory (Fin 2)) :=
  falsifierUnavailable_of_onesBounded
    (onesBounded_of_onesFixing InstrumentRealization.onesClass_arch
      InstrumentRealization.isometry_fixes_ones)

def nonnegClass : InterventionLocality.ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℂ), ‖a‖ ≤ 1 ∧ (∀ i j, (0 : ℂ) ≤ M i j) ∧ K = a • M

theorem nonnegClass_arch : InterventionLocality.Architecture nonnegClass where
  one := fun S _ _ => by
    refine ⟨1, 1, norm_one.le, fun i j => ?_, (one_smul ℂ _).symm⟩
    rw [Matrix.one_apply]
    split_ifs <;> first | exact zero_le_one | exact le_rfl
  mul := fun S _ _ K L hK hL => by
    obtain ⟨a, M, ha, hM, rfl⟩ := hK
    obtain ⟨b, N, hb, hN, rfl⟩ := hL
    refine ⟨a * b, M * N, ?_, fun i j => ?_, ?_⟩
    · rw [norm_mul]
      exact mul_le_one₀ ha (norm_nonneg _) hb
    · rw [Matrix.mul_apply]
      exact Finset.sum_nonneg fun k _ => mul_nonneg (hM i k) (hN k j)
    · rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  smul := fun S _ _ c K hc hK => by
    obtain ⟨a, M, ha, hM, rfl⟩ := hK
    refine ⟨c * a, M, ?_, hM, by rw [smul_smul]⟩
    rw [norm_mul]
    exact mul_le_one₀ hc (norm_nonneg _) ha
  proj := fun S _ _ m k => by
    refine ⟨1, Matrix.diagonal fun r => if r.2 = k then 1 else 0, norm_one.le, fun i j => ?_,
      (one_smul ℂ _).symm⟩
    simp only [Matrix.diagonal_apply]
    split_ifs <;> first | exact zero_le_one | exact le_rfl
  block := fun S _ _ m K f e hK => by
    obtain ⟨a, M, ha, hM, rfl⟩ := hK
    exact ⟨a, AncillaClosure.ancBlock M f e, ha, fun i j => hM _ _, by ext i j; rfl⟩

/-- Auxiliary: a conjugation by a member of the nonnegative class preserves nonnegative entries. -/
theorem nonnegClass_conj_preservesNonneg {S : Type} [Fintype S] [DecidableEq S]
    {K : Matrix S S ℂ} (hK : nonnegClass S K) :
    SubstratumInterfaceAudit.PreservesNonneg (conjChannel K) := by
  obtain ⟨a, M, -, hM, rfl⟩ := hK
  intro X hX p q
  rw [AncillaClosure.conjChannel_apply, Matrix.mul_apply]
  refine Finset.sum_nonneg fun l _ => ?_
  rw [Matrix.mul_apply, Matrix.conjTranspose_apply, Finset.sum_mul]
  refine Finset.sum_nonneg fun k _ => ?_
  have hstar : star (M q l) = M q l := by
    rw [Complex.star_def, Complex.conj_eq_iff_im]
    exact (Complex.nonneg_iff.mp (hM q l)).2.symm
  have hpair : 0 ≤ (a • M) p k * star ((a • M) q l) := by
    rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul, star_mul', hstar,
      show a * M p k * (star a * M q l) = (a * star a) * (M p k * M q l) by ring,
      Complex.star_def, Complex.mul_conj]
    exact mul_nonneg (Complex.zero_le_real.mpr (Complex.normSq_nonneg a))
      (mul_nonneg (hM p k) (hM q l))
  calc (0 : ℂ) ≤ ((a • M) p k * star ((a • M) q l)) * X k l := mul_nonneg hpair (hX k l)
    _ = (a • M) p k * X k l * star ((a • M) q l) := by ring

theorem nonnegClass_nonnegBounded {A : Type} [Fintype A] [DecidableEq A] :
    FrozenSourcing.NonnegBounded (InterventionLocality.genTheory nonnegClass nonnegClass_arch A) := by
  intro n Φ hav
  obtain ⟨ι, _, K, hK, hadm⟩ := InterventionLocality.realized_of_instAvail nonnegClass_arch hav ()
  have hK' : Φ = ∑ i, conjChannel (K i) := hK
  rw [hK']
  exact SubstratumInterfaceAudit.preservesNonneg_sum _ _ fun i _ =>
    nonnegClass_conj_preservesNonneg (hadm i)

theorem nonnegClass_onesFixing : InstrumentRealization.OnesFixing nonnegClass := by
  intro S _ _ K hK hiso
  obtain ⟨a, M, -, hM, rfl⟩ := hK
  by_cases hS : Nonempty S
  swap
  · exact ⟨0, funext fun i => absurd ⟨i⟩ hS⟩
  obtain ⟨i₀⟩ := hS
  -- the nonnegative entries are real
  obtain ⟨N, hN0, rfl⟩ : ∃ N : Matrix S S ℝ, (∀ i j, 0 ≤ N i j)
      ∧ M = N.map (fun x : ℝ => (x : ℂ)) := by
    refine ⟨fun i j => (M i j).re, fun i j => (Complex.nonneg_iff.mp (hM i j)).1, ?_⟩
    ext i j
    apply Complex.ext
    · simp
    · simp [← (Complex.nonneg_iff.mp (hM i j)).2]
  have hKe : ∀ i j, (a • N.map (fun x : ℝ => (x : ℂ))) i j = a * (N i j : ℂ) := fun _ _ => rfl
  have hterm : ∀ i j k, star ((a • N.map (fun x : ℝ => (x : ℂ))) i j)
      * (a • N.map (fun x : ℝ => (x : ℂ))) i k
      = ((Complex.normSq a * (N i j * N i k) : ℝ) : ℂ) := by
    intro i j k
    rw [hKe, hKe, star_mul', Complex.star_def, Complex.conj_ofReal, Complex.ofReal_mul,
      Complex.ofReal_mul, ← Complex.mul_conj a]
    ring
  have hgram : ∀ j k, ((a • N.map (fun x : ℝ => (x : ℂ)))ᴴ
      * (a • N.map (fun x : ℝ => (x : ℂ)))) j k
      = ((Complex.normSq a * ∑ i, N i j * N i k : ℝ) : ℂ) := by
    intro j k
    rw [Matrix.mul_apply]
    simp only [Matrix.conjTranspose_apply]
    rw [Finset.sum_congr rfl fun i _ => hterm i j k, ← Complex.ofReal_sum, Finset.mul_sum]
  have hrow : ∀ i, Complex.normSq a * ∑ j, N i j * N i j = 1 := by
    intro i
    have hKK := mul_eq_one_comm.mp hiso
    have h1 := congrFun (congrFun hKK i) i
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at h1
    simp only [Matrix.conjTranspose_apply] at h1
    rw [Finset.sum_congr rfl fun j _ => (mul_comm _ _).trans (hterm i j j),
      ← Complex.ofReal_sum, ← Finset.mul_sum] at h1
    exact_mod_cast h1
  have hna : Complex.normSq a ≠ 0 := fun h0 => by
    have := hrow i₀
    rw [h0, zero_mul] at this
    exact zero_ne_one this
  have hoff : ∀ j k, j ≠ k → ∀ i, N i j * N i k = 0 := by
    intro j k hjk i
    have h1 := hgram j k
    rw [hiso, Matrix.one_apply_ne hjk] at h1
    have h2 : Complex.normSq a * ∑ i, N i j * N i k = 0 := by exact_mod_cast h1.symm
    have h3 := (mul_eq_zero.mp h2).resolve_left hna
    exact (Finset.sum_eq_zero_iff_of_nonneg fun i _ => mul_nonneg (hN0 i j) (hN0 i k)).mp h3 i
      (Finset.mem_univ _)
  have hcross : ∀ i, (∑ j, N i j) * (∑ j, N i j) = ∑ j, N i j * N i j := by
    intro i
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Finset.sum_eq_single j (fun k _ hkj => hoff j k (Ne.symm hkj) i)
      (fun h => absurd (Finset.mem_univ _) h)]
  have hs : ∀ i, ∑ j, N i j = ∑ j, N i₀ j := by
    intro i
    have hi : Complex.normSq a * ((∑ j, N i j) * (∑ j, N i j)) = 1 := by
      rw [hcross i]; exact hrow i
    have hi0 : Complex.normSq a * ((∑ j, N i₀ j) * (∑ j, N i₀ j)) = 1 := by
      rw [hcross i₀]; exact hrow i₀
    have hsq : (∑ j, N i j) ^ 2 = (∑ j, N i₀ j) ^ 2 := by
      rw [sq, sq]
      exact mul_left_cancel₀ hna (hi.trans hi0.symm)
    calc ∑ j, N i j = Real.sqrt ((∑ j, N i j) ^ 2) :=
          (Real.sqrt_sq (Finset.sum_nonneg fun j _ => hN0 i j)).symm
      _ = Real.sqrt ((∑ j, N i₀ j) ^ 2) := by rw [hsq]
      _ = ∑ j, N i₀ j := Real.sqrt_sq (Finset.sum_nonneg fun j _ => hN0 i₀ j)
  refine ⟨a * ((∑ j, N i₀ j : ℝ) : ℂ), funext fun i => ?_⟩
  simp only [Matrix.mulVec, dotProduct, InstrumentRealization.ones_apply, mul_one, Pi.smul_apply,
    smul_eq_mul, hKe]
  rw [← Finset.mul_sum, ← Complex.ofReal_sum, hs i]

def realClass : InterventionLocality.ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℝ), ‖a‖ ≤ 1 ∧ K = a • M.map (fun x => (x : ℂ))

/-- Auxiliary: the complexification of real matrices is multiplicative. -/
theorem map_ofReal_mul {S : Type} [Fintype S] [DecidableEq S] (M N : Matrix S S ℝ) :
    (M * N).map (fun x : ℝ => (x : ℂ)) = M.map (fun x : ℝ => (x : ℂ)) * N.map (fun x : ℝ => (x : ℂ)) := by
  first
  | exact Matrix.map_mul (f := Complex.ofRealHom)
  | (ext i j; simp [Matrix.mul_apply, Matrix.map_apply])

theorem realClass_arch : InterventionLocality.Architecture realClass where
  one := fun S _ _ => by
    refine ⟨1, 1, norm_one.le, ?_⟩
    rw [one_smul]
    first
    | rw [Matrix.map_one _ Complex.ofReal_zero Complex.ofReal_one]
    | (ext i j
       rw [Matrix.map_apply, Matrix.one_apply, Matrix.one_apply]
       split_ifs <;> simp)
  mul := fun S _ _ K L hK hL => by
    obtain ⟨a, M, ha, rfl⟩ := hK
    obtain ⟨b, N, hb, rfl⟩ := hL
    refine ⟨a * b, M * N, ?_, ?_⟩
    · rw [norm_mul]
      exact mul_le_one₀ ha (norm_nonneg _) hb
    · rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, map_ofReal_mul]
  smul := fun S _ _ c K hc hK => by
    obtain ⟨a, M, ha, rfl⟩ := hK
    refine ⟨c * a, M, ?_, by rw [smul_smul]⟩
    rw [norm_mul]
    exact mul_le_one₀ hc (norm_nonneg _) ha
  proj := fun S _ _ m k => by
    refine ⟨1, Matrix.diagonal fun r => if r.2 = k then (1 : ℝ) else 0, norm_one.le, ?_⟩
    rw [one_smul]
    ext i j
    simp only [Matrix.map_apply, Matrix.diagonal_apply]
    split_ifs <;> simp
  block := fun S _ _ m K f e hK => by
    obtain ⟨a, M, ha, rfl⟩ := hK
    exact ⟨a, AncillaClosure.ancBlock M f e, ha, by ext i j; rfl⟩

/-- Auxiliary: the real matrix whose complexification is `rot`. -/
noncomputable def rotR : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℝ :=
  Matrix.of fun p q =>
    if p.1 = 0 ∧ q.1 = 0 then (3 / 5 : ℝ) else if p.1 = 0 ∧ q.1 = 1 then (4 / 5 : ℝ)
      else if p.1 = 1 ∧ q.1 = 0 then -(4 / 5 : ℝ) else (3 / 5 : ℝ)

theorem realTheory_rot :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory realClass realClass_arch (Fin 2)) := by
  intro hf
  apply hf
  refine InterventionLocality.InstAvail.op DiagonalTheory.rot ⟨1, rotR, norm_one.le, ?_⟩
    DiagonalTheory.rot_isometry
  rw [one_smul]
  ext p q
  simp only [DiagonalTheory.rot, rotR, Matrix.map_apply, Matrix.of_apply]
  split_ifs <;> simp

theorem realTheory_not_phases :
    ¬ RouteB.PhasesAvailable (InterventionLocality.genTheory realClass realClass_arch (Fin 2)) := by
  intro hp
  have hav := hp 1 ((0 : Fin 2), (0 : Fin 1))
  obtain ⟨c, hc, b, M, -, hM⟩ :=
    MicroReversibility.exists_scaled_mem_of_instAvail_unitary realClass_arch hav
  have h0 : c * Complex.I = b * ((M ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) := by
    simpa [LieRankSource.phaseGate] using
      congrFun (congrFun hM ((0 : Fin 2), (0 : Fin 1))) ((0 : Fin 2), (0 : Fin 1))
  have h1 : c = b * ((M ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) := by
    simpa [LieRankSource.phaseGate] using
      congrFun (congrFun hM ((1 : Fin 2), (0 : Fin 1))) ((1 : Fin 2), (0 : Fin 1))
  have hb : b ≠ 0 := by
    rintro rfl
    rw [zero_mul] at h1
    exact hc h1
  have h2 : b * (((M ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) * Complex.I)
      = b * ((M ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) := by
    rw [← h0, h1]
    ring
  have h3 := mul_left_cancel₀ hb h2
  have h4 := congrArg Complex.im h3
  simp at h4
  rw [h4, Complex.ofReal_zero, mul_zero] at h1
  exact hc h1

theorem fullTheory_rot :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2)) :=
  fun hf => hf (InterventionLocality.genTheory_fullClass_control 1 DiagonalTheory.rot
    DiagonalTheory.rot_isometry)

theorem fullTheory_rotDagger :
    (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel DiagonalTheory.rotᴴ) := by
  have h : DiagonalTheory.rot * DiagonalTheory.rotᴴ = 1 :=
    mul_eq_one_comm.mp DiagonalTheory.rot_isometry
  exact InterventionLocality.genTheory_fullClass_control 1 _
    (by rw [Matrix.conjTranspose_conjTranspose]; exact h)

theorem fullTheory_phases :
    RouteB.PhasesAvailable (InterventionLocality.genTheory InterventionLocality.fullClass
      InterventionLocality.fullClass_arch (Fin 2)) :=
  RouteB.phasesAvailable_of_control InterventionLocality.genTheory_fullClass_control

#print axioms rot_not_preservesNonneg
#print axioms rot_moves_ones
#print axioms falsifierUnavailable_of_nonnegBounded
#print axioms falsifierUnavailable_of_onesBounded
#print axioms onesBounded_of_onesFixing
#print axioms permTheory_onesBounded
#print axioms onesTheory_falsifierUnavailable
#print axioms nonnegClass_arch
#print axioms nonnegClass_nonnegBounded
#print axioms nonnegClass_onesFixing
#print axioms realClass_arch
#print axioms realTheory_rot
#print axioms realTheory_not_phases
#print axioms fullTheory_rot
#print axioms fullTheory_rotDagger
#print axioms fullTheory_phases

end F2CoherenceControls
end OIBridge
