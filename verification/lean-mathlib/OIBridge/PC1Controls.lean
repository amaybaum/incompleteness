import OIBridge.F2CoherenceControls

namespace OIBridge
namespace PC1Controls

open scoped ComplexOrder
open OperationalAssembly MonoidalCompletion
open Matrix

/-!
# PC-1 stage 2 — the fixed-statement control declarations

Research-only kernel controls for the PC-1 preregistration
`verification/programmes/oi-qm/reconstruction/physical-coupling-pc1/preregistration.md` (frozen at
`948b30c1`), under its stage-2 amendment `amendments/PC-S2.md` (`4d2c4d56`) and the C13 correction
`amendments/PC-S2-C13.md` (`895e5c5b`). The header above and the fourteen statements of PC-S2
§S2-3 are copied verbatim; only the proofs and the auxiliary lemmas named `aux_*` are added.

They decide predicates for the stage-2 controls only:
- the diagonal gauge `diag(1, i)` carries `rot` into the ones-fixing class (finding PC-F1);
- no diagonal gauge makes a nonzero multiple of `rot` a scalar times a nonnegative matrix;
- nonnegativity- and ones-bounded two-state theories lack the level-one quarter phase;
- the permutation theory is ones-bounded on every carrier, and lacks both the level-one quarter
  phase and the gauged rotation;
- a class containing `rot` has the falsifier, while any architecture inside the real-amplitude
  class lacks the quarter phase.

No candidate interface is treated: stage 1 froze none. Not claimed: a sourcing of `rot` or of the
phases by OI, a no-go for observer-level extensions, or any manuscript statement.
-/

noncomputable def gaugeD : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ :=
  Matrix.diagonal fun p => if p.1 = 0 then 1 else Complex.I

theorem gaugeD_unitary : gaugeDᴴ * gaugeD = 1 := by
  rw [gaugeD, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  ext p
  first
    | (simp only [Pi.star_apply]
       split_ifs <;> simp [Complex.star_def, Complex.conj_I, Complex.I_mul_I])
    | (split_ifs <;> simp [Complex.star_def, Complex.conj_I, Complex.I_mul_I])
    | (by_cases hp : p.1 = 0 <;> simp [hp, Complex.star_def, Complex.conj_I, Complex.I_mul_I])

/-! ### Auxiliary entries of the gauged rotation (not among the fixed statements) -/

theorem aux_G00 :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      = (3 / 5 : ℂ) := by
  rw [gaugeD, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    F2CoherenceControls.rot_00]
  first
    | (simp [Complex.star_def]; done)
    | (simp [Complex.star_def] <;> ring)
    | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
    | (apply Complex.ext <;> norm_num [Complex.star_def])

theorem aux_G01 :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
      = (4 / 5 : ℂ) * Complex.I := by
  rw [gaugeD, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    F2CoherenceControls.rot_01]
  first
    | (simp [Complex.star_def]; done)
    | (simp [Complex.star_def] <;> ring)
    | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
    | (apply Complex.ext <;> norm_num [Complex.star_def])

theorem aux_G10 :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      = (4 / 5 : ℂ) * Complex.I := by
  rw [gaugeD, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    F2CoherenceControls.rot_10]
  first
    | (simp [Complex.star_def]; done)
    | (simp [Complex.star_def] <;> ring)
    | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
    | (apply Complex.ext <;> norm_num [Complex.star_def])

theorem aux_G11 :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
      = (3 / 5 : ℂ) := by
  rw [gaugeD, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    F2CoherenceControls.rot_11]
  first
    | (simp [Complex.star_def]; done)
    | (simp [Complex.star_def]
       linear_combination (-3 / 5 : ℂ) * Complex.I_sq)

theorem gauged_rot_fixes_ones :
    (gaugeDᴴ * DiagonalTheory.rot * gaugeD) *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) • InstrumentRealization.ones (Fin 2 × Fin 1) := by
  have e0 : ((gaugeDᴴ * DiagonalTheory.rot * gaugeD) *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1))
      ((0 : Fin 2), (0 : Fin 1)) = (3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I := by
    simp only [Matrix.mulVec, dotProduct, InstrumentRealization.ones_apply, _root_.mul_one,
      Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_one]
    rw [aux_G00, aux_G01]
  have e1 : ((gaugeDᴴ * DiagonalTheory.rot * gaugeD) *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1))
      ((1 : Fin 2), (0 : Fin 1)) = (4 / 5 : ℂ) * Complex.I + (3 / 5 : ℂ) := by
    simp only [Matrix.mulVec, dotProduct, InstrumentRealization.ones_apply, _root_.mul_one,
      Fintype.sum_prod_type, Fin.sum_univ_two, Fin.sum_univ_one]
    rw [aux_G10, aux_G11]
  funext p
  rcases p with ⟨x, i⟩
  rw [Subsingleton.elim i 0]
  revert x
  refine Fin.forall_fin_two.mpr ⟨?_, ?_⟩
  · rw [e0]
    simp only [Pi.smul_apply, smul_eq_mul, InstrumentRealization.ones_apply, _root_.mul_one]
  · rw [e1]
    simp only [Pi.smul_apply, smul_eq_mul, InstrumentRealization.ones_apply, _root_.mul_one]
    ring

/-! ### Auxiliary facts about the scalar `3/5 + (4/5) i` (not among the fixed statements) -/

theorem aux_zstar :
    ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) * star ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) = 1 := by
  first
    | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
    | (apply Complex.ext <;> norm_num [Complex.star_def])
    | (rw [Complex.star_def, Complex.mul_conj, Complex.normSq_apply]; norm_num)

theorem aux_norm : ‖(3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I‖ ≤ 1 := by
  have h : ‖(3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I‖ ^ 2 = 1 := by
    rw [Complex.sq_norm, Complex.normSq_apply]
    first
      | norm_num
      | (simp; norm_num)
      | simp
  nlinarith [norm_nonneg ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I)]

theorem gauged_rot_mem_onesClass :
    InstrumentRealization.onesClass (Fin 2 × Fin 1) (gaugeDᴴ * DiagonalTheory.rot * gaugeD) := by
  have hD' : gaugeD * gaugeDᴴ = 1 := _root_.mul_eq_one_comm.mp gaugeD_unitary
  have hG : (gaugeDᴴ * DiagonalTheory.rot * gaugeD)ᴴ * (gaugeDᴴ * DiagonalTheory.rot * gaugeD)
      = 1 := by
    simp only [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose, Matrix.mul_assoc]
    rw [← Matrix.mul_assoc gaugeD gaugeDᴴ, hD', Matrix.one_mul,
      ← Matrix.mul_assoc DiagonalTheory.rotᴴ DiagonalTheory.rot, DiagonalTheory.rot_isometry,
      Matrix.one_mul, gaugeD_unitary]
  have hz2 : star ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) * ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I)
      = 1 := by
    rw [_root_.mul_comm]
    exact aux_zstar
  have hW : (star ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I)
        • (gaugeDᴴ * DiagonalTheory.rot * gaugeD))ᴴ
      * (star ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) • (gaugeDᴴ * DiagonalTheory.rot * gaugeD))
      = 1 := by
    rw [Matrix.conjTranspose_smul, _root_.star_star, Matrix.smul_mul, Matrix.mul_smul,
      _root_.smul_smul, hG, aux_zstar, _root_.one_smul]
  have hWo : (star ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I)
        • (gaugeDᴴ * DiagonalTheory.rot * gaugeD)) *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = InstrumentRealization.ones (Fin 2 × Fin 1) := by
    first
      | rw [Matrix.smul_mulVec, gauged_rot_fixes_ones, _root_.smul_smul, hz2, _root_.one_smul]
      | rw [Matrix.smul_mulVec_assoc, gauged_rot_fixes_ones, _root_.smul_smul, hz2,
          _root_.one_smul]
  have hmem := InstrumentRealization.onesClass_of_unitary_ones hW hWo
  have hsm := InstrumentRealization.onesClass_arch.smul (Fin 2 × Fin 1)
    ((3 / 5 : ℂ) + (4 / 5 : ℂ) * Complex.I) _ aux_norm hmem
  rw [_root_.smul_smul, aux_zstar, _root_.one_smul] at hsm
  exact hsm

theorem scaled_rot_not_gauge_nonneg :
    ¬ ∃ (d : Fin 2 × Fin 1 → ℂ) (c a : ℂ) (M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ),
      c ≠ 0 ∧ (∀ p, ‖d p‖ = 1) ∧ (∀ i j, (0 : ℂ) ≤ M i j) ∧
        (Matrix.diagonal d)ᴴ * (c • DiagonalTheory.rot) * Matrix.diagonal d = a • M := by
  rintro ⟨d, c, a, M, hc, hd, hM, hE⟩
  -- the nonnegative entries are real
  obtain ⟨N, hN0, rfl⟩ : ∃ N : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℝ, (∀ i j, 0 ≤ N i j)
      ∧ M = N.map (fun x : ℝ => (x : ℂ)) := by
    refine ⟨fun i j => (M i j).re, fun i j => (Complex.nonneg_iff.mp (hM i j)).1, ?_⟩
    refine Matrix.ext fun i j => ?_
    show M i j = (((M i j).re : ℝ) : ℂ)
    apply Complex.ext
    · rw [Complex.ofReal_re]
    · rw [Complex.ofReal_im]
      exact (Complex.nonneg_iff.mp (hM i j)).2.symm
  have hent : ∀ p q, star (d p) * (c * DiagonalTheory.rot p q) * d q = a * ((N p q : ℝ) : ℂ) := by
    intro p q
    have h := congrFun (congrFun hE p) q
    rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
      Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul, Matrix.map_apply] at h
    exact h
  have hu : ∀ p, star (d p) * d p = 1 := by
    intro p
    rw [Complex.star_def, _root_.mul_comm, Complex.mul_conj, Complex.normSq_eq_norm_sq, hd p]
    norm_num
  have r3 : ((3 / 5 : ℝ) : ℂ) = (3 / 5 : ℂ) := by
    first
      | norm_num
      | (push_cast; ring)
      | simp
  have r4 : ((4 / 5 : ℝ) : ℂ) = (4 / 5 : ℂ) := by
    first
      | norm_num
      | (push_cast; ring)
      | simp
  have h00 := hent ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
  have h01 := hent ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
  have h10 := hent ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
  have h11 := hent ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
  rw [F2CoherenceControls.rot_00, r3] at h00
  rw [F2CoherenceControls.rot_01, r4] at h01
  rw [F2CoherenceControls.rot_10, r4] at h10
  rw [F2CoherenceControls.rot_11, r3] at h11
  have u0 := hu ((0 : Fin 2), (0 : Fin 1))
  have u1 := hu ((1 : Fin 2), (0 : Fin 1))
  have ha : a ≠ 0 := by
    rintro rfl
    have h3 : c * (3 / 5 : ℂ) = 0 := by
      linear_combination h00 - (3 / 5 * c) * u0
    rcases _root_.mul_eq_zero.mp h3 with h | h
    · exact hc h
    · norm_num at h
  -- the cross terms cancel: 9 · (4/5)(−4/5) + 16 · (3/5)(3/5) = 0
  have hzero : a ^ 2 * (9 * (((N ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)
      * ((N ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ))
      + 16 * (((N ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)
      * ((N ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ))) = 0 := by
    linear_combination
      (-9 * a * ((N ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)) * h01
      + (-9 * (star (d ((0 : Fin 2), (0 : Fin 1))) * (c * (4 / 5 : ℂ))
          * d ((1 : Fin 2), (0 : Fin 1)))) * h10
      + (-16 * a * ((N ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)) * h00
      + (-16 * (star (d ((0 : Fin 2), (0 : Fin 1))) * (c * (3 / 5 : ℂ))
          * d ((0 : Fin 2), (0 : Fin 1)))) * h11
  have hsum := (_root_.mul_eq_zero.mp hzero).resolve_left (_root_.pow_ne_zero 2 ha)
  have hr : 9 * (N ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
      * N ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)))
      + 16 * (N ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      * N ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))) = 0 := by
    exact_mod_cast hsum
  have hn : N ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      * N ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) = 0 := by
    nlinarith [_root_.mul_nonneg (hN0 ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)))
        (hN0 ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))),
      _root_.mul_nonneg (hN0 ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)))
        (hN0 ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)))]
  have hcc : c ^ 2 * (9 / 25 : ℂ) = a ^ 2
      * (((N ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)
        * ((N ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)) := by
    linear_combination
      (-(c ^ 2 * (9 / 25 : ℂ)) * (star (d ((1 : Fin 2), (0 : Fin 1))) * d ((1 : Fin 2), (0 : Fin 1))))
        * u0
      + (-(c ^ 2 * (9 / 25 : ℂ))) * u1
      + (star (d ((1 : Fin 2), (0 : Fin 1))) * (c * (3 / 5 : ℂ)) * d ((1 : Fin 2), (0 : Fin 1)))
        * h00
      + (a * ((N ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ)) * h11
  have h0c : c ^ 2 * (9 / 25 : ℂ) = 0 := by
    rw [hcc, ← Complex.ofReal_mul, hn, Complex.ofReal_zero, mul_zero]
  have hc2 : c ^ 2 = 0 := by
    linear_combination (25 / 9 : ℂ) * h0c
  first
    | exact hc ((pow_eq_zero_iff two_ne_zero).mp hc2)
    | exact hc (by simpa using hc2)
    | exact hc (pow_eq_zero hc2)

theorem not_p1_of_nonnegBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : FrozenSourcing.NonnegBounded T) :
    ¬ T.availExt 1 Unit (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)))) := by
  intro hav
  have hP := h 1 _ hav
  have hd := SubstratumInterfaceAudit.diagonal_nonneg_of_preservesNonneg
    (d := fun p : Fin 2 × Fin 1 => if ((0 : Fin 2), (0 : Fin 1)) = p then Complex.I else 1) hP
    ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
  have hne : ¬ (((0 : Fin 2), (0 : Fin 1)) = ((1 : Fin 2), (0 : Fin 1))) := by decide
  have hd' : (0 : ℂ) ≤ Complex.I := by
    first
      | simpa [hne] using hd
      | (simp only [if_true, hne, if_false, star_one, _root_.mul_one] at hd; exact hd)
  have h2 := (Complex.nonneg_iff.mp hd').2
  simp at h2

theorem not_p1_of_onesBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : F2CoherenceControls.OnesBounded T) :
    ¬ T.availExt 1 Unit (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)))) := by
  intro hav
  obtain ⟨z, hz⟩ := h 1 (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)))
    (LieRankSource.phaseGate_unitary _) hav
  exact PhaseSource.phaseGate_moves_ones (by simp) _ z hz

theorem permTheory_onesBounded_all {A : Type} [Fintype A] [DecidableEq A] :
    F2CoherenceControls.OnesBounded (SubstratumInterfaceAudit.permTheory A) :=
  F2CoherenceControls.onesBounded_of_onesFixing SubstratumInterfaceAudit.permClass_arch
    PhaseSource.permClass_onesFixing

theorem permTheory_not_p1 :
    ¬ (SubstratumInterfaceAudit.permTheory (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)))) :=
  not_p1_of_nonnegBounded FrozenSourcing.permTheory_nonnegBounded

theorem permTheory_not_gauged_rot :
    ¬ (SubstratumInterfaceAudit.permTheory (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (gaugeDᴴ * DiagonalTheory.rot * gaugeD)) := by
  intro hav
  have hP := FrozenSourcing.permTheory_nonnegBounded 1 _ hav
  have hX : ∀ p q : Fin 2 × Fin 1, (0 : ℂ) ≤
      (Matrix.diagonal fun r : Fin 2 × Fin 1 => if r.1 = 0 then (1 : ℂ) else 0) p q := by
    intro p q
    simp only [Matrix.diagonal_apply]
    split_ifs <;> first | exact zero_le_one | exact le_rfl
  have hval := hP _ hX ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
  have e : ∀ G : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ, conjChannel G
      (Matrix.diagonal fun r : Fin 2 × Fin 1 => if r.1 = 0 then (1 : ℂ) else 0)
      ((0 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
      = G ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
        * star (G ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))) := by
    intro G
    simp [AncillaClosure.conjChannel_apply, Matrix.mul_apply, Matrix.mul_diagonal,
      Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_two]
  rw [e, aux_G00, aux_G10] at hval
  have ev : (3 / 5 : ℂ) * star ((4 / 5 : ℂ) * Complex.I) = -(12 / 25 : ℂ) * Complex.I := by
    first
      | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
      | (apply Complex.ext <;> norm_num [Complex.star_def])
  rw [ev] at hval
  have h2 := (Complex.nonneg_iff.mp hval).2
  first
    | (norm_num at h2; done)
    | (simp at h2; done)
    | (simp at h2; norm_num at h2)

theorem falsifier_available_of_mem {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘) (h : 𝓘 (Fin 2 × Fin 1) DiagonalTheory.rot) :
    ¬ RouteB.FalsifierUnavailable (InterventionLocality.genTheory 𝓘 arch (Fin 2)) := by
  intro hf
  apply hf
  exact InterventionLocality.InstAvail.op DiagonalTheory.rot h DiagonalTheory.rot_isometry

theorem rot_mem_realClass : F2CoherenceControls.realClass (Fin 2 × Fin 1) DiagonalTheory.rot := by
  refine ⟨1, F2CoherenceControls.rotR, norm_one.le, ?_⟩
  rw [_root_.one_smul]
  ext p q
  simp only [DiagonalTheory.rot, F2CoherenceControls.rotR, Matrix.map_apply, Matrix.of_apply]
  split_ifs <;> simp

theorem realSubclass_not_p1 {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K →
      F2CoherenceControls.realClass S K) :
    ¬ (InterventionLocality.genTheory 𝓘 arch (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel (LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)))) := by
  intro hav
  obtain ⟨c, hc, hmem⟩ := MicroReversibility.exists_scaled_mem_of_instAvail_unitary arch hav
  obtain ⟨b, M, -, hM⟩ := hle _ _ hmem
  have hentry : ∀ p q, c * LieRankSource.phaseGate ((0 : Fin 2), (0 : Fin 1)) p q
      = b * ((M p q : ℝ) : ℂ) := by
    intro p q
    have h := congrFun (congrFun hM p) q
    rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul, Matrix.map_apply] at h
    exact h
  have hne : ¬ (((0 : Fin 2), (0 : Fin 1)) = ((1 : Fin 2), (0 : Fin 1))) := by decide
  have h0 : c * Complex.I = b * ((M ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) := by
    have h := hentry ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
    rw [LieRankSource.phaseGate, Matrix.diagonal_apply_eq, if_pos rfl] at h
    exact h
  have h1 : c = b * ((M ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1)) : ℝ) : ℂ) := by
    have h := hentry ((1 : Fin 2), (0 : Fin 1)) ((1 : Fin 2), (0 : Fin 1))
    rw [LieRankSource.phaseGate, Matrix.diagonal_apply_eq, if_neg hne, _root_.mul_one] at h
    exact h
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

theorem realSubclass_not_phases {𝓘 : InterventionLocality.ImplementationClass}
    (arch : InterventionLocality.Architecture 𝓘)
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K →
      F2CoherenceControls.realClass S K) :
    ¬ RouteB.PhasesAvailable (InterventionLocality.genTheory 𝓘 arch (Fin 2)) :=
  fun hp => realSubclass_not_p1 arch hle (hp 1 ((0 : Fin 2), (0 : Fin 1)))

end PC1Controls
end OIBridge

#print axioms OIBridge.PC1Controls.gaugeD_unitary
#print axioms OIBridge.PC1Controls.gauged_rot_fixes_ones
#print axioms OIBridge.PC1Controls.gauged_rot_mem_onesClass
#print axioms OIBridge.PC1Controls.scaled_rot_not_gauge_nonneg
#print axioms OIBridge.PC1Controls.not_p1_of_nonnegBounded
#print axioms OIBridge.PC1Controls.not_p1_of_onesBounded
#print axioms OIBridge.PC1Controls.permTheory_onesBounded_all
#print axioms OIBridge.PC1Controls.permTheory_not_p1
#print axioms OIBridge.PC1Controls.permTheory_not_gauged_rot
#print axioms OIBridge.PC1Controls.falsifier_available_of_mem
#print axioms OIBridge.PC1Controls.rot_mem_realClass
#print axioms OIBridge.PC1Controls.realSubclass_not_p1
#print axioms OIBridge.PC1Controls.realSubclass_not_phases
