/-
  OIBridge/ReferenceSufficiency.lean — exact system QM, full composite unitary control and
  parallel reference extension force composite quantum soundness.

  ROUND THIRTY-SIX. Round thirty-five identified parallel reference extension as the
  compositional property the round-34 countermodel lacks. This round proves it is the missing
  condition, and builds the theory that has it.

      ┌──────────────────────────────────────────────────────────────────────────────┐
      │  `krausSoundExt_of_sound_control_refext` (hext : FiniteIsometryExtensionSF Unit) │
      │      KrausSound T ∧ HasCompositeUnitaryControl T                              │
      │        ∧ HasParallelReferenceExtension T  ⟹  KrausSoundExt T ;                │
      │  `krausSoundExt_of_exact_control_refext`: the round-36 form with               │
      │      ExactFiniteEndomorphicQuantumOps T in place of KrausSound T, a corollary; │
      │  `fullQuantum_parallelReferenceExtension`, `parallelReferenceExtension_satisfiable`: │
      │      the full quantum theory has all three, and is composite-sound.           │
      └──────────────────────────────────────────────────────────────────────────────┘

  ROUND THIRTY-SEVEN, OPENING CLEANUP (STRENGTHENED IN ROUND THIRTY-SEVEN). The round-36
  proof used exactness only through its soundness half, so the antecedent is now
  `KrausSound T`; the exact form is an immediate corollary via `exact_iff_sound_and_full`.
  System COMPLETENESS (`HasFullFiniteEndomorphicInstruments`) is not an ingredient of
  composite soundness.

  PART ONE, A CORRECTION FIRST. `KrausSoundExt` as stated in round twenty-seven quantified
  over ancilla level ZERO, where the structure's own `readout_avail 0` makes an available
  family with the empty outcome type, for which no Kraus family exists. The predicate was
  unsatisfiable (`krausSoundExtAllLevels_unsatisfiable`, in `CompositeSoundness.lean`) and
  is now stated at levels `n + 1`. Every earlier `¬ KrausSoundExt` result is re-proved
  against the corrected predicate with the same level-two witness; nothing about those
  witnesses changes, and `countermodel_witness_level_two` records the witness-level content
  independently of any predicate.

  THE ONE EXTERNAL INGREDIENT: boundary item 2. Preparing the maximally entangled test state
  and rotating a bad direction into a readable basis block both need "every unit vector is a
  column of some unitary". That is finite isometry extension with a ONE-DIMENSIONAL source,
  and it is derived from the already-declared interface `FiniteIsometryExtensionSF` at the
  carrier `Unit` by explicit reindexing (`unitVectorRotation_of_isometryExtension`), so the
  accounting is honest: no fifth item, and item 2 consumed exactly where it is used.

  THE PROOF. Take an available composite family `F` at level `n + 1`. Two obligations give
  `IsKrausFamily F` through the now-internal factorization:

  (i) EACH BRANCH IS CP (`branch_cp`). Reference extension makes `id_S ⊗ F a` available on
  the larger carrier `Fin 2 × Fin (M + 1)`, `M + 1 = 2·|S|·(n+1)`, via the explicit
  reindexing `refIdx`. From the pure seed and control, the normalized reindexed `|Ω_S⟩` is a
  reachable preparation evaluated at `|0⟩⟨0|`; the extended branch turns it into the
  reindexed Choi matrix; a second unitary rotates any test direction `w` into the basis
  vector `(0, 0)`; the native readout at level `0` and the discard read off the quadratic
  form `⟨w, J w⟩/|S|` as the `(0,0)` entry of a VISIBLE-SYSTEM branch output on the
  positive input `|0⟩⟨0|`. Exact system QM makes that branch CP, hence its output PSD,
  hence the entry nonnegative — for every unit `w`, so for every `w`. Both failure modes
  are handled at once: a non-Hermitian Choi matrix has a non-real quadratic form somewhere,
  a Hermitian one with a negative direction has a negative one, and "all forms nonnegative
  in the complex order" gives Hermitian by polarization (`isHermitian_of_forms_real`) and
  then PSD (`posSemidef_of_forms_nonneg`). No case split is hidden.

  (ii) AGGREGATE TRACE (`aggregate_trace`). Every unit vector on `S` is a reachable pure
  preparation; exactness forces trace conservation of the discarded family on it; the
  discard is trace-transparent; so the linear functional `X ↦ Σ_a tr(F a X) − tr X`
  vanishes on every dyad, and a functional vanishing on dyads vanishes
  (`linear_functional_zero_of_dyads`, by the explicit polarization identity
  `two_single_eq_dyads`). No reference extension is needed for this half.

  THE POSITIVE INSTANCE. `fullQuantum` has `avail` = the Kraus families and `availExt` = the
  CP, aggregate-trace-preserving families at every level, with round thirty-four's
  reference-tested preparations. It is exactly quantum on the system, has every composite
  unitary, is composite-sound, and HAS parallel reference extension: the spectator extension
  of a Kraus form is the conjugation family by the reindexed `1 ⊗ K_i`
  (`withSpectator_conjChannel`), and the trace is carried through the reference diagonal.

  WHAT IS AND IS NOT CLAIMED. Proved: for a qubit system, exact visible QM + full unitary
  control + parallel reference extension ⟹ composite Kraus SOUNDNESS, against boundary item
  2 only; and the conjunction is satisfiable. NOT claimed: composite COMPLETENESS (that every
  Kraus family on every composite is available), so the equation "full finite QM = exact
  visible QM + unitary control + parallel spectator consistency" is established in its
  soundness direction only, and the file says so. NOT claimed: that OI itself implies
  parallel reference extension — that is round thirty-seven's question. No structure field
  is added.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ReferenceExtension

namespace OIBridge
namespace ReferenceSufficiency

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open OperationalRigidity DimensionalObstruction DimensionalCountermodel HiddenCoherence
open ReferenceExtension BoundaryAudit

open scoped ComplexOrder

/-! ### Section A — unit-vector rotation, from finite isometry extension at `Unit` -/

section Rotation

/-- **UNIT-VECTOR ROTATION**: every unit vector is the prescribed column of some unitary. -/
def UnitVectorRotation (C : Type*) [Fintype C] [DecidableEq C] : Prop :=
  ∀ ψ : C → ℂ, star ψ ⬝ᵥ ψ = 1 → ∀ c : C,
    ∃ U : Matrix C C ℂ, Uᴴ * U = 1 ∧ (fun p => U p c) = ψ

theorem dotProduct_reindex {m n : Type*} [Fintype m] [Fintype n] (e : m ≃ n) (v w : n → ℂ) :
    star (v ∘ e) ⬝ᵥ (w ∘ e) = star v ⬝ᵥ w := by
  simp only [dotProduct, Pi.star_apply, Function.comp]
  exact Fintype.sum_equiv e _ _ fun _ => rfl

/-- The reindexing `Unit × Fin (2n+2) ≃ Fin 2 × Fin (n+1)`. -/
def unitIdx (n : ℕ) : Unit × Fin (2 * n + 1 + 1) ≃ Fin 2 × Fin (n + 1) :=
  (Equiv.punitProd _).trans ((finCongr (by ring)).trans finProdFinEquiv.symm)

/-- **ROTATION FROM BOUNDARY ITEM 2.** Finite isometry extension with a one-dimensional
source, reindexed onto the composite carrier. -/
theorem unitVectorRotation_of_isometryExtension (hext : FiniteIsometryExtensionSF Unit)
    (n : ℕ) : UnitVectorRotation (Fin 2 × Fin (n + 1)) := by
  intro ψ hψ c
  set e := unitIdx n with he
  let V : Matrix (Unit × Fin (2 * n + 1 + 1)) Unit ℂ := Matrix.of fun p _ => ψ (e p)
  have hV : Vᴴ * V = 1 := by
    ext ⟨⟩ ⟨⟩
    rw [Matrix.mul_apply, Matrix.one_apply_eq]
    have : ∑ p, Vᴴ () p * V p () = star (ψ ∘ e) ⬝ᵥ (ψ ∘ e) := by
      simp only [dotProduct, Matrix.conjTranspose_apply, Pi.star_apply, Function.comp, V,
        Matrix.of_apply]
    rw [this, dotProduct_reindex, hψ]
  obtain ⟨U₀, hU₀, hUE⟩ := hext (2 * n + 1) (e.symm c).2 V hV
  have hcol : ∀ p, U₀ p (e.symm c) = ψ (e p) := by
    intro p
    have h := congrFun (congrFun hUE p) ()
    rw [Matrix.mul_apply, Finset.sum_eq_single (e.symm c)] at h
    · rw [Esf, Matrix.of_apply, if_pos rfl, if_pos (Subsingleton.elim _ _), mul_one] at h
      rw [h]
      rfl
    · intro b _ hb
      rw [Esf, Matrix.of_apply]
      by_cases h2 : b.2 = (e.symm c).2
      · rw [if_pos h2, if_neg, mul_zero]
        intro h1
        exact hb (Prod.ext (h1.trans (Subsingleton.elim _ _)) h2)
      · rw [if_neg h2, mul_zero]
    · intro h
      exact absurd (Finset.mem_univ _) h
  refine ⟨Matrix.reindex e e U₀, ?_, ?_⟩
  · rw [Matrix.conjTranspose_reindex, Matrix.reindex_apply, Matrix.reindex_apply,
      Matrix.submatrix_mul_equiv, hU₀, Matrix.submatrix_one_equiv]
  · funext p
    rw [Matrix.reindex_apply, Matrix.submatrix_apply, hcol, Equiv.apply_symm_apply]

end Rotation

/-! ### Section B — reachable pure preparations -/

section Reach

theorem tensorOf_single_single {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B]
    [DecidableEq B] (a : A) (b : B) :
    tensorOf (Matrix.single a a (1 : ℂ)) (Matrix.single b b (1 : ℂ))
      = Matrix.vecMulVec (Pi.single (a, b) 1) (star (Pi.single (a, b) 1)) := by
  ext ⟨x, y⟩ ⟨z, w⟩
  simp only [tensorOf_apply, single_entry, Matrix.vecMulVec_apply, Pi.star_apply,
    Pi.single_apply, Prod.mk.injEq, star_ite_one_zero, @eq_comm A a x, @eq_comm A a z,
    @eq_comm B b y, @eq_comm B b w]
  by_cases h1 : x = a <;> by_cases h2 : y = b <;> by_cases h3 : z = a <;> by_cases h4 : w = b <;>
    simp [h1, h2, h3, h4]

theorem conj_vecMulVec {C : Type*} [Fintype C] (U : Matrix C C ℂ) (v : C → ℂ) :
    U * Matrix.vecMulVec v (star v) * Uᴴ
      = Matrix.vecMulVec (U *ᵥ v) (star (U *ᵥ v)) := by
  rw [Matrix.mul_vecMulVec, Matrix.vecMulVec_mul, Matrix.star_mulVec]

theorem mulVec_single_col {C : Type*} [Fintype C] [DecidableEq C] (U : Matrix C C ℂ) (c : C) :
    U *ᵥ Pi.single c 1 = fun p => U p c := by
  funext p
  simp [Matrix.mulVec, dotProduct, Pi.single_apply]

/-- **EVERY UNIT VECTOR IS A REACHABLE PURE PREPARATION**, evaluated at `|0⟩⟨0|`: the pure
seed (derived from control) followed by a rotation. -/
theorem pureState_reachable (T : FiniteOperationalTheory (Fin 2))
    (hctrl : HasCompositeUnitaryControl T) {n : ℕ}
    (hrot : UnitVectorRotation (Fin 2 × Fin (n + 1))) (ψ : Fin 2 × Fin (n + 1) → ℂ)
    (hψ : star ψ ⬝ᵥ ψ = 1) :
    ∃ P : Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ,
      T.prepAvail (n + 1) P ∧ P (Matrix.single 0 0 1) = Matrix.vecMulVec ψ (star ψ) := by
  obtain ⟨U, hU, hcol⟩ := hrot ψ hψ (0, 0)
  refine ⟨(conjChannel U).comp (pureAttach (n + 1) 0), ?_, ?_⟩
  · exact T.prepAvail_post (n + 1) _ _
      (pureSeedPrep_available_of_swap T n 0 fun k => compositeControl_hasSwapControl T hctrl (n + 1) k 0)
      (hctrl (n + 1) U hU)
  · show U * pureAttach (n + 1) 0 (Matrix.single 0 0 1) * Uᴴ = _
    rw [pureAttach_apply, tensorOf_single_single, conj_vecMulVec, mulVec_single_col, hcol]

end Reach

/-! ### Section C — system soundness on a general outcome type

ROUND THIRTY-SEVEN, OPENING CLEANUP. The round-36 proof used exactness only through its
soundness half (`(hex _ _).mp`). The primitive statement is therefore taken from `KrausSound`,
and the exact form is an immediate corollary via `exact_iff_sound_and_full`. -/

section Sound

/-- Every available visible-system family on any finite outcome type is branchwise CP and
aggregate trace preserving, from `KrausSound` alone (coarse-graining to `Fin (card O)`). -/
theorem sound_avail_cp_tp (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) {O : Type} [Fintype O] [DecidableEq O]
    (D : O → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ) (hD : T.avail O D) :
    (∀ a, IsCompletelyPositive (D a)) ∧ ∀ X, ∑ a, ((D a) X).trace = X.trace := by
  let f : O ≃ Fin (Fintype.card O) := Fintype.equivFin O
  have hco := T.avail_coarse O (Fin (Fintype.card O)) D f hD
  have hD' : ∀ a, (∑ j ∈ Finset.univ.filter (fun j => f j = f a), D j) = D a := by
    intro a
    have hfil : Finset.univ.filter (fun j => f j = f a) = {a} := by
      ext j
      simp [f.injective.eq_iff]
    rw [hfil, Finset.sum_singleton]
  have hK := (isKrausFamily_iff _).mpr (hsound _ _ hco)
  refine ⟨fun a => ?_, fun X => ?_⟩
  · have := krausFamily_cp hK (f a)
    rwa [hD' a] at this
  · obtain ⟨m, K, out, hnorm, hKF⟩ := hsound _ _ hco
    have htr := instrumentBranch_trace K out hnorm X
    rw [← hKF] at htr
    rw [← htr]
    refine (Fintype.sum_equiv f _ _ fun a => ?_).symm.symm
    simp only [hD' a]

/-- The round-36 form, now a corollary: exactness supplies soundness. -/
theorem exact_avail_cp_tp (T : FiniteOperationalTheory (Fin 2))
    (hex : ExactFiniteEndomorphicQuantumOps T) {O : Type} [Fintype O] [DecidableEq O]
    (D : O → Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ) (hD : T.avail O D) :
    (∀ a, IsCompletelyPositive (D a)) ∧ ∀ X, ∑ a, ((D a) X).trace = X.trace :=
  sound_avail_cp_tp T ((exact_iff_sound_and_full T).mp hex).1 D hD

/-- A completely positive map carries positive semidefinite matrices to positive
semidefinite matrices. -/
theorem cp_apply_posSemidef {S : Type*} [Fintype S] [DecidableEq S]
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : IsCompletelyPositive Φ) {M : Matrix S S ℂ}
    (hM : M.PosSemidef) : (Φ M).PosSemidef :=
  positive_of_twoPositive (cp_referencePositive (Fin 2) Φ h) hM

end Sound

/-! ### Section D — polarization -/

section Polarization

variable {S : Type*} [Fintype S] [DecidableEq S]

theorem star_I : star Complex.I = -Complex.I := by simp

/-- **THE POLARIZATION IDENTITY** for matrix units, as an identity of matrices. -/
theorem two_single_eq_dyads (i j : S) :
    (2 : ℂ) • Matrix.single i j (1 : ℂ)
      = (Matrix.vecMulVec (Pi.single i 1 + Pi.single j 1) (star (Pi.single i 1 + Pi.single j 1))
          - Matrix.vecMulVec (Pi.single i 1) (star (Pi.single i 1))
          - Matrix.vecMulVec (Pi.single j 1) (star (Pi.single j 1)))
        + Complex.I • (Matrix.vecMulVec (Pi.single i 1 + Complex.I • Pi.single j 1)
            (star (Pi.single i 1 + Complex.I • Pi.single j 1))
          - Matrix.vecMulVec (Pi.single i 1) (star (Pi.single i 1))
          - Matrix.vecMulVec (Pi.single j 1) (star (Pi.single j 1))) := by
  ext x y
  simp only [Matrix.smul_apply, single_entry, Matrix.add_apply, Matrix.sub_apply,
    Matrix.vecMulVec_apply, Pi.star_apply, star_add, star_smul, Pi.add_apply, Pi.smul_apply,
    Pi.single_apply, star_ite_one_zero, star_I, smul_eq_mul, ite_and_one_zero,
    @eq_comm S i x, @eq_comm S j y]
  generalize (if x = i then (1 : ℂ) else 0) = p
  generalize (if x = j then (1 : ℂ) else 0) = q
  generalize (if y = i then (1 : ℂ) else 0) = r
  generalize (if y = j then (1 : ℂ) else 0) = s
  linear_combination (p * s + s * q * Complex.I - q * r) * Complex.I_sq

/-- **A LINEAR FUNCTIONAL VANISHING ON EVERY DYAD VANISHES.** -/
theorem linear_functional_zero_of_dyads (L : Matrix S S ℂ →ₗ[ℂ] ℂ)
    (h : ∀ u : S → ℂ, L (Matrix.vecMulVec u (star u)) = 0) (X : Matrix S S ℂ) : L X = 0 := by
  have hunit : ∀ i j : S, L (Matrix.single i j 1) = 0 := by
    intro i j
    have h2 := congrArg L (two_single_eq_dyads i j)
    simp only [map_smul, map_add, map_sub, h, sub_zero, smul_zero, add_zero, smul_eq_mul,
      mul_zero, zero_add] at h2
    exact (mul_eq_zero.mp h2).resolve_left two_ne_zero
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  rw [map_sum]
  refine Finset.sum_eq_zero fun i _ => ?_
  rw [map_sum]
  refine Finset.sum_eq_zero fun j _ => ?_
  rw [single_eq_smul, map_smul, hunit, smul_zero]

theorem trace_mul_vecMulVec (J : Matrix S S ℂ) (v : S → ℂ) :
    (J * Matrix.vecMulVec v (star v)).trace = star v ⬝ᵥ (J *ᵥ v) := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.vecMulVec_apply,
    Pi.star_apply, dotProduct, Matrix.mulVec, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => ?_
  ring

theorem star_form (J : Matrix S S ℂ) (v : S → ℂ) :
    star (star v ⬝ᵥ (J *ᵥ v)) = star v ⬝ᵥ (Jᴴ *ᵥ v) := by
  rw [star_dotProduct, star_star, Matrix.star_mulVec, ← Matrix.dotProduct_mulVec]

/-- **HERMITIAN FROM REAL FORMS**: a matrix all of whose quadratic forms are real is
Hermitian, by polarization. -/
theorem isHermitian_of_forms_real (J : Matrix S S ℂ)
    (h : ∀ v, star (star v ⬝ᵥ (J *ᵥ v)) = star v ⬝ᵥ (J *ᵥ v)) : J.IsHermitian := by
  let L : Matrix S S ℂ →ₗ[ℂ] ℂ :=
    (Matrix.traceLinearMap S ℂ ℂ).comp (LinearMap.mulLeft ℂ (J - Jᴴ))
  have hL : ∀ u, L (Matrix.vecMulVec u (star u)) = 0 := by
    intro u
    show (((J - Jᴴ) * Matrix.vecMulVec u (star u))).trace = 0
    rw [Matrix.sub_mul, Matrix.trace_sub, trace_mul_vecMulVec, trace_mul_vecMulVec,
      ← star_form, h u, sub_self]
  have hent : ∀ i j, (J - Jᴴ) i j = 0 := by
    intro i j
    have this : ((J - Jᴴ) * Matrix.single j i 1).trace = 0 :=
      linear_functional_zero_of_dyads L hL (Matrix.single j i 1)
    rwa [Matrix.trace_mul_single, MulOpposite.op_one, one_smul] at this
  show Jᴴ = J
  ext i j
  have := hent i j
  rw [Matrix.sub_apply, sub_eq_zero] at this
  exact this.symm

/-- **PSD FROM NONNEGATIVE FORMS**, in the complex order: no separate Hermitian hypothesis. -/
theorem posSemidef_of_forms_nonneg (J : Matrix S S ℂ)
    (h : ∀ v, (0 : ℂ) ≤ star v ⬝ᵥ (J *ᵥ v)) : J.PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg (isHermitian_of_forms_real J fun v => ?_) h
  have him := (Complex.le_def.mp (h v)).2
  rw [Complex.zero_im] at him
  exact Complex.conj_eq_iff_im.mpr him.symm

theorem nonneg_of_real_mul_nonneg {r : ℝ} (hr : 0 < r) {z : ℂ} (h : (0 : ℂ) ≤ (r : ℂ) * z) :
    (0 : ℂ) ≤ z := by
  rw [Complex.le_def, Complex.re_ofReal_mul, Complex.im_ofReal_mul, Complex.zero_re,
    Complex.zero_im] at h
  rw [Complex.le_def, Complex.zero_re, Complex.zero_im]
  refine ⟨(mul_nonneg_iff_of_pos_left hr).mp h.1, ?_⟩
  rcases mul_eq_zero.mp h.2.symm with h0 | h0
  · exact absurd h0 hr.ne'
  · exact h0.symm

end Polarization

/-! ### Section E — the quadratic form read off through the visible qubit -/

section Readoff

theorem conj_diag_entry {C : Type*} [Fintype C] (W Y : Matrix C C ℂ) (p : C) :
    (Wᴴ * Y * W) p p = star (fun x => W x p) ⬝ᵥ (Y *ᵥ fun x => W x p) := by
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, dotProduct, Matrix.mulVec,
    Pi.star_apply, Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => ?_
  ring

theorem form_reindex {m n : Type*} [Fintype m] [Fintype n] (e : m ≃ n) (J : Matrix m m ℂ)
    (w : m → ℂ) :
    star (w ∘ e.symm) ⬝ᵥ (Matrix.reindex e e J *ᵥ (w ∘ e.symm)) = star w ⬝ᵥ (J *ᵥ w) := by
  simp only [dotProduct, Matrix.mulVec, Pi.star_apply, Function.comp, Matrix.reindex_apply,
    Matrix.submatrix_apply]
  apply Fintype.sum_equiv e.symm
  intro x
  congr 1
  apply Fintype.sum_equiv e.symm
  intro y
  rfl

theorem vecMulVec_comp_symm {m n : Type*} (e : m ≃ n) (w : m → ℂ) :
    Matrix.vecMulVec (w ∘ e.symm) (star (w ∘ e.symm))
      = Matrix.reindex e e (Matrix.vecMulVec w (star w)) := by
  ext p q
  rfl

theorem dotProduct_star_self_real {C : Type*} [Fintype C] (v : C → ℂ) :
    star v ⬝ᵥ v = (((star v ⬝ᵥ v).re : ℝ) : ℂ) := by
  refine Complex.ext (by simp) ?_
  simp only [Complex.ofReal_im, dotProduct, Pi.star_apply, Complex.im_sum]
  exact Finset.sum_eq_zero fun i _ => by
    rw [Complex.star_def, Complex.mul_im, Complex.conj_re, Complex.conj_im]
    ring

theorem dotProduct_star_self_pos {C : Type*} [Fintype C] {v : C → ℂ} (hv : v ≠ 0) :
    0 < (star v ⬝ᵥ v).re := by
  have hnn : ∀ i, 0 ≤ (star (v i) * v i).re := fun i => by
    rw [Complex.star_def, ← Complex.normSq_eq_conj_mul_self, Complex.ofReal_re]
    exact Complex.normSq_nonneg _
  obtain ⟨i, hi⟩ : ∃ i, v i ≠ 0 := Function.ne_iff.mp hv
  have hpos : 0 < (star (v i) * v i).re := by
    rw [Complex.star_def, ← Complex.normSq_eq_conj_mul_self, Complex.ofReal_re]
    exact Complex.normSq_pos.mpr hi
  rw [dotProduct, Complex.re_sum]
  exact Finset.sum_pos' (fun j _ => hnn j) ⟨i, Finset.mem_univ _, hpos⟩

/-- Scaling a vector scales its quadratic form by the squared modulus. -/
theorem form_real_smul {C : Type*} [Fintype C] (r : ℝ) (J : Matrix C C ℂ) (v : C → ℂ) :
    star ((r : ℂ) • v) ⬝ᵥ (J *ᵥ ((r : ℂ) • v)) = ((r * r : ℝ) : ℂ) * (star v ⬝ᵥ (J *ᵥ v)) := by
  rw [star_smul, Matrix.mulVec_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul,
    Complex.star_def, Complex.conj_ofReal]
  push_cast
  ring

/-- **NONNEGATIVE ON UNIT VECTORS IS NONNEGATIVE EVERYWHERE.** -/
theorem forms_nonneg_of_unit {C : Type*} [Fintype C] (J : Matrix C C ℂ)
    (h : ∀ w : C → ℂ, star w ⬝ᵥ w = 1 → (0 : ℂ) ≤ star w ⬝ᵥ (J *ᵥ w)) (v : C → ℂ) :
    (0 : ℂ) ≤ star v ⬝ᵥ (J *ᵥ v) := by
  by_cases hv : v = 0
  · subst hv
    simp
  · set nv : ℝ := (star v ⬝ᵥ v).re with hnv
    have hpos : 0 < nv := dotProduct_star_self_pos hv
    have hsq : 0 < Real.sqrt nv := Real.sqrt_pos.mpr hpos
    set r : ℝ := (Real.sqrt nv)⁻¹ with hr
    have hrpos : 0 < r := inv_pos.mpr hsq
    have hunit : star ((r : ℂ) • v) ⬝ᵥ ((r : ℂ) • v) = 1 := by
      rw [star_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul, Complex.star_def,
        Complex.conj_ofReal, dotProduct_star_self_real v, ← hnv, ← Complex.ofReal_mul,
        ← Complex.ofReal_mul, hr, ← Complex.ofReal_one]
      congr 1
      rw [← mul_assoc, ← mul_inv, Real.mul_self_sqrt hpos.le, inv_mul_cancel₀ hpos.ne']
    have := h _ hunit
    rw [form_real_smul] at this
    exact nonneg_of_real_mul_nonneg (mul_pos hrpos hrpos) this

end Readoff

/-! ### Section F — each branch is completely positive -/

section BranchCP

/-- The reindexing `S × (Fin 2 × Fin (n+1)) ≃ Fin 2 × Fin (2·|S|·(n+1))` for
`S = Fin 2 × Fin (n+1)`: keep the system qubit, pack the reference with the ancilla. -/
def refIdx (n : ℕ) :
    (Fin 2 × Fin (n + 1)) × (Fin 2 × Fin (n + 1)) ≃ Fin 2 × Fin (2 * n * n + 4 * n + 1 + 1) :=
  (Equiv.prodAssoc _ _ _).symm.trans
    ((Equiv.prodCongr (Equiv.prodComm _ _) (Equiv.refl _)).trans
      ((Equiv.prodAssoc _ _ _).trans (Equiv.prodCongr (Equiv.refl _)
        ((Equiv.prodCongr finProdFinEquiv (Equiv.refl _)).trans
          (finProdFinEquiv.trans (finCongr (by ring)))))))

theorem card_S (n : ℕ) : (Fintype.card (Fin 2 × Fin (n + 1)) : ℂ) = ((2 * (n + 1) : ℕ) : ℂ) := by
  simp

/-- **EACH AVAILABLE BRANCH IS COMPLETELY POSITIVE**, from system soundness, control,
rotation and parallel reference extension. -/
theorem branch_cp (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T)
    (hpar : HasParallelReferenceExtension T)
    (hrot : ∀ m, UnitVectorRotation (Fin 2 × Fin (m + 1))) {n : ℕ} {O : Type} [Fintype O]
    [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ)
    (hF : T.availExt (n + 1) O F) (a : O) : IsCompletelyPositive (F a) := by
  set M := 2 * n * n + 4 * n + 1 with hM
  set e := refIdx n with he
  -- the extended family is available at level M + 1
  have hG := hpar (Fin 2 × Fin (n + 1)) (n + 1) (M + 1) e O F hF
  show (choiMatrix (F a)).PosSemidef
  refine posSemidef_of_forms_nonneg _ (forms_nonneg_of_unit _ fun w hw => ?_)
  -- the normalized maximally entangled preparation on the big carrier
  have hcard : (0 : ℝ) < (Fintype.card (Fin 2 × Fin (n + 1)) : ℝ) := by
    exact_mod_cast Fintype.card_pos
  set d : ℝ := ((Fintype.card (Fin 2 × Fin (n + 1)) : ℕ) : ℝ) with hd
  set r : ℝ := (Real.sqrt d)⁻¹ with hr
  set ψ : Fin 2 × Fin (M + 1) → ℂ :=
    (r : ℂ) • ((maxEntVec (S := Fin 2 × Fin (n + 1))) ∘ e.symm) with hψ
  have hΩnorm : star ((maxEntVec (S := Fin 2 × Fin (n + 1))) ∘ e.symm)
      ⬝ᵥ ((maxEntVec (S := Fin 2 × Fin (n + 1))) ∘ e.symm) = (d : ℂ) := by
    rw [dotProduct_reindex e.symm, maxEntVec_norm, hd]
    norm_cast
  have hψunit : star ψ ⬝ᵥ ψ = 1 := by
    rw [hψ, star_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul,
      Complex.star_def, Complex.conj_ofReal, hΩnorm, ← Complex.ofReal_mul, ← Complex.ofReal_mul,
      ← Complex.ofReal_one]
    congr 1
    rw [hr, ← mul_assoc, ← mul_inv, Real.mul_self_sqrt hcard.le, inv_mul_cancel₀ hcard.ne']
  obtain ⟨P, hP, hP0⟩ := pureState_reachable T hctrl (hrot M) ψ hψunit
  -- the rotation of the test direction
  set ŵ : Fin 2 × Fin (M + 1) → ℂ := w ∘ e.symm with hŵ
  have hŵunit : star ŵ ⬝ᵥ ŵ = 1 := by rw [hŵ, dotProduct_reindex, hw]
  obtain ⟨W, hW, hWcol⟩ := hrot M ŵ hŵunit (0, 0)
  have hU₂ : (Wᴴ)ᴴ * Wᴴ = 1 := by rw [Matrix.conjTranspose_conjTranspose]; exact mul_eq_one_comm.mp hW
  -- the available composite family: extend, rotate, read out
  have h1 := T.availExt_bind (M + 1) O Unit (fun a => withSpectator (Fin 2 × Fin (n + 1)) e (F a))
    (fun _ _ => conjChannel Wᴴ) hG (fun _ => hctrl (M + 1) Wᴴ hU₂)
  have h2 := T.availExt_bind (M + 1) (O × Unit) (Fin (M + 1)) _
    (fun _ k => T.readout (M + 1) k) h1 (fun _ => T.readout_avail (M + 1))
  have h3 := T.prepAvail_discard (M + 1) P _ _ hP h2
  obtain ⟨hcp, -⟩ := sound_avail_cp_tp T hsound _ h3
  -- the branch at outcome ((a, ()), 0) on the input |0⟩⟨0|
  have hρ0 : (Matrix.single (0 : Fin 2) 0 (1 : ℂ)).PosSemidef := by
    have : Matrix.single (0 : Fin 2) 0 (1 : ℂ)
        = Matrix.vecMulVec (Pi.single 0 1) (star (Pi.single (0 : Fin 2) 1)) := by
      ext x y
      simp only [single_entry, Matrix.vecMulVec_apply, Pi.star_apply, Pi.single_apply]
      by_cases hx : x = 0 <;> by_cases hy : y = 0 <;> simp [hx, hy, eq_comm]
    rw [this]
    exact Matrix.posSemidef_vecMulVec_self_star _
  have hout := (cp_apply_posSemidef (hcp ((a, ()), (0 : Fin (M + 1)))) hρ0).diag_nonneg (i := 0)
  -- compute that entry
  have hY : withSpectator (Fin 2 × Fin (n + 1)) e (F a) (P (Matrix.single 0 0 1))
      = ((d⁻¹ : ℝ) : ℂ) • Matrix.reindex e e (choiMatrix (F a)) := by
    rw [hP0, hψ, star_smul, Matrix.smul_vecMulVec, Matrix.vecMulVec_smul, smul_smul, map_smul,
      vecMulVec_comp_symm, withSpectator_reindex, ← choiMatrix_eq_amplRef,
      Complex.star_def, Complex.conj_ofReal, ← Complex.ofReal_mul, hr, ← mul_inv,
      Real.mul_self_sqrt hcard.le]
  have hentry : (discardWith (M + 1) P
      ((T.readout (M + 1) 0).comp ((conjChannel Wᴴ).comp
        (withSpectator (Fin 2 × Fin (n + 1)) e (F a)))) (Matrix.single 0 0 1)) 0 0
      = ((d⁻¹ : ℝ) : ℂ) * (star w ⬝ᵥ (choiMatrix (F a) *ᵥ w)) := by
    show ptraceAnc (M + 1) ((T.readout (M + 1) 0)
      ((conjChannel Wᴴ) (withSpectator (Fin 2 × Fin (n + 1)) e (F a)
        (P (Matrix.single 0 0 1))))) 0 0 = _
    rw [readout_is_localLuders, ptraceAnc_localLuders, Matrix.of_apply, hY]
    show (Wᴴ * (((d⁻¹ : ℝ) : ℂ) • Matrix.reindex e e (choiMatrix (F a))) * (Wᴴ)ᴴ) (0, 0) (0, 0)
      = _
    rw [Matrix.conjTranspose_conjTranspose, Matrix.mul_smul, Matrix.smul_mul, Matrix.smul_apply,
      conj_diag_entry, hWcol, hŵ, form_reindex, smul_eq_mul]
  rw [hentry] at hout
  exact nonneg_of_real_mul_nonneg (inv_pos.mpr hcard) hout

end BranchCP

/-! ### Section G — the aggregate trace -/

section Trace

theorem trace_vecMulVec_star {C : Type*} [Fintype C] (w : C → ℂ) :
    (Matrix.vecMulVec w (star w)).trace = star w ⬝ᵥ w := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.vecMulVec_apply, Pi.star_apply, dotProduct]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- **AGGREGATE TRACE PRESERVATION**, from system soundness, control and rotation alone. -/
theorem aggregate_trace (T : FiniteOperationalTheory (Fin 2))
    (hsound : KrausSound T) (hctrl : HasCompositeUnitaryControl T) {n : ℕ}
    (hrot : UnitVectorRotation (Fin 2 × Fin (n + 1))) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ →ₗ[ℂ]
      Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ)
    (hF : T.availExt (n + 1) O F) (X : Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ) :
    ∑ a, ((F a) X).trace = X.trace := by
  let L : Matrix (Fin 2 × Fin (n + 1)) (Fin 2 × Fin (n + 1)) ℂ →ₗ[ℂ] ℂ :=
    (∑ a, (Matrix.traceLinearMap _ ℂ ℂ).comp (F a)) - Matrix.traceLinearMap _ ℂ ℂ
  have hLapply : ∀ Y, L Y = ∑ a, ((F a) Y).trace - Y.trace := by
    intro Y
    simp [L, LinearMap.sum_apply]
  -- on unit dyads, by reachability and system soundness
  have hunit : ∀ w, star w ⬝ᵥ w = 1 → L (Matrix.vecMulVec w (star w)) = 0 := by
    intro w hw
    obtain ⟨P, hP, hP0⟩ := pureState_reachable T hctrl hrot w hw
    have hD := T.prepAvail_discard (n + 1) P O F hP hF
    obtain ⟨-, htr⟩ := sound_avail_cp_tp T hsound _ hD
    have h0 := htr (Matrix.single 0 0 1)
    rw [Finset.sum_congr rfl fun a _ => discardWith_trace (n + 1) P (F a) _, hP0,
      Matrix.trace_single_eq_same] at h0
    rw [hLapply, h0, trace_vecMulVec_star, hw, sub_self]
  -- hence on every dyad, by scaling
  have hdyad : ∀ u, L (Matrix.vecMulVec u (star u)) = 0 := by
    intro u
    by_cases hu : u = 0
    · subst hu
      simp
    · set nu : ℝ := (star u ⬝ᵥ u).re with hnu
      have hpos : 0 < nu := dotProduct_star_self_pos hu
      set r : ℝ := (Real.sqrt nu)⁻¹ with hr
      have hrpos : 0 < r := inv_pos.mpr (Real.sqrt_pos.mpr hpos)
      have hw : star ((r : ℂ) • u) ⬝ᵥ ((r : ℂ) • u) = 1 := by
        rw [star_smul, smul_dotProduct, dotProduct_smul, smul_eq_mul, smul_eq_mul,
          Complex.star_def, Complex.conj_ofReal, dotProduct_star_self_real u, ← hnu,
          ← Complex.ofReal_mul, ← Complex.ofReal_mul, hr, ← Complex.ofReal_one]
        congr 1
        rw [← mul_assoc, ← mul_inv, Real.mul_self_sqrt hpos.le, inv_mul_cancel₀ hpos.ne']
      have h1 := hunit _ hw
      rw [star_smul, Matrix.smul_vecMulVec, Matrix.vecMulVec_smul, smul_smul, map_smul,
        smul_eq_mul, Complex.star_def, Complex.conj_ofReal] at h1
      rcases mul_eq_zero.mp h1 with h0 | h0
      · exfalso
        have : ((r : ℂ) * r) = ((r * r : ℝ) : ℂ) := by push_cast; ring
        rw [this] at h0
        exact (mul_pos hrpos hrpos).ne' (Complex.ofReal_eq_zero.mp h0)
      · exact h0
  have := linear_functional_zero_of_dyads L hdyad X
  rw [hLapply, sub_eq_zero] at this
  exact this

end Trace

/-! ### Section H — the sufficiency theorem -/

/-- **THE SUFFICIENCY THEOREM (ROUND-37 FORM).** System Kraus SOUNDNESS, full composite
unitary control and parallel reference extension force composite Kraus soundness, against
boundary item 2 (finite isometry extension at a one-dimensional source). System completeness
is not used anywhere in the proof. -/
theorem krausSoundExt_of_sound_control_refext (T : FiniteOperationalTheory (Fin 2))
    (hext : FiniteIsometryExtensionSF Unit) (hsound : KrausSound T)
    (hctrl : HasCompositeUnitaryControl T) (hpar : HasParallelReferenceExtension T) :
    KrausSoundExt T := by
  intro n O _ _ F hF
  have hrot : ∀ m, UnitVectorRotation (Fin 2 × Fin (m + 1)) :=
    unitVectorRotation_of_isometryExtension hext
  exact isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F
    (fun a => branch_cp T hsound hctrl hpar hrot F hF a)
    (aggregate_trace T hsound hctrl (hrot n) F hF)

/-- **THE ROUND-36 STATEMENT, NOW A COROLLARY.** Exact system QM supplies system soundness,
and nothing more of it is used. -/
theorem krausSoundExt_of_exact_control_refext (T : FiniteOperationalTheory (Fin 2))
    (hext : FiniteIsometryExtensionSF Unit) (hex : ExactFiniteEndomorphicQuantumOps T)
    (hctrl : HasCompositeUnitaryControl T) (hpar : HasParallelReferenceExtension T) :
    KrausSoundExt T :=
  krausSoundExt_of_sound_control_refext T hext ((exact_iff_sound_and_full T).mp hex).1
    hctrl hpar

/-- The round-34 witness at level two, stated without any predicate. -/
theorem countermodel_witness_level_two :
    countermodel.availExt 2 Unit (fun _ => reduction2 (Fin 2 × Fin 2))
      ∧ ¬ IsKrausFamily (fun _ : Unit => reduction2 (Fin 2 × Fin 2)) :=
  ⟨countermodel_reduction2_available, fun h => reduction2_not_cp (krausFamily_cp h ())⟩

/-! ### Section I — the full quantum theory has parallel reference extension -/

section Full

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- **THE COMPOSITE SECTOR OF THE FULL THEORY**: completely positive branches, trace
preserved in aggregate. -/
def IsCPInstrument {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (∀ a, IsCompletelyPositive (F a)) ∧ ∀ X, ∑ a, ((F a) X).trace = X.trace

theorem cp_sum {ι : Type*} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (h : ∀ i ∈ s, IsCompletelyPositive (Φ i)) : IsCompletelyPositive (∑ i ∈ s, Φ i) := by
  show (choiMatrix _).PosSemidef
  rw [choiMatrix_finsum]
  exact CompositeSoundness.posSemidef_sum _ _ fun i hi => h i hi

theorem refBlockR_amplRef {R S' : Type*} [Fintype R] [DecidableEq R] [Fintype S'] [DecidableEq S']
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (R × S) (R × S) ℂ) (i j : R) :
    refBlockR (amplRef R Φ M) i j = Φ (refBlockR M i j) := by
  ext k l
  rfl

theorem amplRef_comp {R S' S'' : Type*} [Fintype R] [DecidableEq R] [Fintype S'] [DecidableEq S']
    [Fintype S''] [DecidableEq S''] (Φ : Matrix S' S' ℂ →ₗ[ℂ] Matrix S'' S'' ℂ)
    (Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (M : Matrix (R × S) (R × S) ℂ) :
    amplRef R (Φ.comp Ψ) M = amplRef R Φ (amplRef R Ψ M) := by
  ext p q
  show Φ (Ψ (refBlockR M p.1 q.1)) p.2 q.2 = Φ (refBlockR (amplRef R Ψ M) p.1 q.1) p.2 q.2
  rw [refBlockR_amplRef]

theorem cp_comp {Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (hΦ : IsCompletelyPositive Φ)
    (hΨ : IsCompletelyPositive Ψ) : IsCompletelyPositive (Φ.comp Ψ) := by
  refine referencePositive_self_cp _ fun M hM => ?_
  rw [amplRef_comp]
  exact cp_referencePositive S Φ hΦ _ (cp_referencePositive S Ψ hΨ _ hM)

theorem conjChannel_cp' (V : Matrix S S ℂ) : IsCompletelyPositive (conjChannel V) :=
  conjChannel_cp V

end Full

section FullTheory

theorem localLuders_eq_conjChannel {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B]
    [DecidableEq B] (k : B) :
    localLuders (A := A) k
      = conjChannel (Matrix.diagonal fun r : A × B => if r.2 = k then (1 : ℂ) else 0) := by
  refine LinearMap.ext fun X => ?_
  ext ⟨a, b⟩ ⟨c, d⟩
  let D : Matrix (A × B) (A × B) ℂ := Matrix.diagonal fun r => if r.2 = k then (1 : ℂ) else 0
  show localLuders k X (a, b) (c, d) = (D * X * Dᴴ) (a, b) (c, d)
  rw [localLuders_apply, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    Pi.star_apply, star_ite_one_zero]
  by_cases hb : b = k <;> by_cases hd : d = k <;> simp [hb, hd]

theorem localLuders_cp {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]
    (k : B) : IsCompletelyPositive (localLuders (A := A) k) := by
  rw [localLuders_eq_conjChannel]
  exact conjChannel_cp _

/-- **THE FULL QUANTUM THEORY** on a qubit: Kraus families on the system, CP aggregate-trace-
preserving families on every composite, reference-tested preparations. -/
noncomputable def fullQuantum : FiniteOperationalTheory (Fin 2) where
  avail := fun _ _ _ F => IsKrausFamily F
  availExt := fun _ _ _ _ F => IsCPInstrument F
  avail_id := scalarAvail_isKraus
    ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
      rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f hF
    exact isKrausFamily_coarse hF f
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨h2, htr⟩
    refine ⟨fun a' => cp_sum _ _ fun j _ => h2 j, fun X => ?_⟩
    rw [Finset.sum_congr rfl fun a' _ => by rw [LinearMap.sum_apply, Matrix.trace_sum],
      Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x))
        (fun j => ((F j) X).trace)]
    exact htr X
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨hF2, hFtr⟩ hG
    refine ⟨fun c => cp_comp ((hG c.1).1 c.2) (hF2 c.1), fun X => ?_⟩
    rw [Fintype.sum_prod_type]
    show ∑ a, ∑ b, ((G a b) ((F a) X)).trace = X.trace
    rw [Finset.sum_congr rfl fun a _ => (hG a).2 ((F a) X)]
    exact hFtr X
  prepAvail := fun n P => RefTestedPrep n P
  prepAvail_uniform := fun n =>
    ⟨uniformAttach_trace (n + 1) n.succ_ne_zero,
      amplR_uniformAttach_posSemidef (Matrix.posSemidef_vecMulVec_self_star _) _⟩
  prepAvail_post := by
    rintro n P Φ ⟨hPtr, hPpsd⟩ ⟨hΦ2, hΦtr⟩
    refine ⟨fun ρ => ?_, ?_⟩
    · show (Φ (P ρ)).trace = ρ.trace
      have h := hΦtr (P ρ)
      rw [Fintype.sum_unique] at h
      rw [h, hPtr]
    · rw [amplR_comp]
      exact cp_referencePositive (Fin 2) _ (hΦ2 ()) _ hPpsd
  readout := fun _ k => localLuders k
  readout_avail := fun n => ⟨fun k => localLuders_cp k, localLuders_trace_sum⟩
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hPtr, hPpsd⟩ ⟨hF2, hFtr⟩
    refine isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) _
      (fun a => ?_) (fun X => ?_)
    · show (choiMatrix (discardWith n P (F a))).PosSemidef
      rw [choiMatrix_eq_ampl2, ← amplR_eq_ampl2, discardWith, amplR_comp, amplR_comp]
      exact amplR_ptraceAncL_posSemidef (cp_referencePositive (Fin 2) _ (hF2 a) _ hPpsd)
    · rw [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) X, hFtr (P X), hPtr X]

theorem fullQuantum_exact : ExactFiniteEndomorphicQuantumOps fullQuantum :=
  fun _ F => isKrausFamily_iff F

theorem fullQuantum_control : HasCompositeUnitaryControl fullQuantum :=
  fun _ U hU => ⟨fun _ => conjChannel_cp U, fun X => by
    rw [Fintype.sum_unique]
    exact conjChannel_trace U hU X⟩

/-- **THE FULL THEORY IS COMPOSITE-SOUND.** -/
theorem fullQuantum_krausSoundExt : KrausSoundExt fullQuantum :=
  fun _ _ _ _ F ⟨hcp, htr⟩ =>
    isKrausFamily_of_cp_of_factorization (psdFactorization_discharged _) F hcp htr

section Spectator

variable {A : Type*} [Fintype A] [DecidableEq A] {R : Type*} [Fintype R] [DecidableEq R]
  {n m : ℕ}

theorem reindex_mul {l l' : Type*} [Fintype l] [Fintype l'] (e : l ≃ l')
    (X Y : Matrix l l ℂ) :
    Matrix.reindex e e (X * Y) = Matrix.reindex e e X * Matrix.reindex e e Y := by
  rw [Matrix.reindex_apply, Matrix.reindex_apply, Matrix.reindex_apply,
    Matrix.submatrix_mul_equiv]

/-- **THE SPECTATOR EXTENSION OF A CONJUGATION** is the conjugation by the reindexed `1 ⊗ V`. -/
theorem withSpectator_conjChannel (e : R × (A × Fin n) ≃ A × Fin m) (V : Matrix (A × Fin n) (A × Fin n) ℂ) :
    withSpectator R e (conjChannel V)
      = conjChannel (Matrix.reindex e e (tensorOf (1 : Matrix R R ℂ) V)) := by
  refine LinearMap.ext fun X => ?_
  rw [withSpectator_apply, amplRef_conjChannel]
  show Matrix.reindex e e (tensorOf 1 V * Matrix.reindex e.symm e.symm X * (tensorOf 1 V)ᴴ)
    = Matrix.reindex e e (tensorOf 1 V) * X * (Matrix.reindex e e (tensorOf 1 V))ᴴ
  rw [reindex_mul, reindex_mul, Matrix.conjTranspose_reindex, ← Matrix.reindex_symm,
    Equiv.apply_symm_apply]

theorem withSpectator_sum (e : R × (A × Fin n) ≃ A × Fin m) {ι : Type*} (s : Finset ι)
    (Φ : ι → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    withSpectator R e (∑ i ∈ s, Φ i) = ∑ i ∈ s, withSpectator R e (Φ i) := by
  refine LinearMap.ext fun X => ?_
  rw [withSpectator_apply, LinearMap.sum_apply]
  simp only [withSpectator_apply, amplRef_sum_map]
  ext p q
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply, Matrix.sum_apply]

/-- **CP IS PRESERVED BY SPECTATOR EXTENSION.** -/
theorem withSpectator_cp (e : R × (A × Fin n) ≃ A × Fin m)
    {Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (h : IsCompletelyPositive Φ) : IsCompletelyPositive (withSpectator R e Φ) := by
  have h' : (choiMatrix Φ).PosSemidef := h
  obtain ⟨B, hB⟩ := psdFactorization_discharged _ _ h'
  rw [kraus_of_choi_factor Φ B hB, withSpectator_sum]
  exact cp_sum _ _ fun i _ => by rw [withSpectator_conjChannel]; exact conjChannel_cp _

theorem trace_reindex {l l' : Type*} [Fintype l] [Fintype l'] (e : l ≃ l') (Y : Matrix l l ℂ) :
    (Matrix.reindex e e Y).trace = Y.trace := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.reindex_apply, Matrix.submatrix_apply]
  exact Fintype.sum_equiv e.symm _ _ fun _ => rfl

theorem trace_amplRef {S S' : Type*} [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S']
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ) (X : Matrix (R × S) (R × S) ℂ) :
    (amplRef R Φ X).trace = ∑ i, (Φ (refBlockR X i i)).trace := by
  simp only [Matrix.trace, Matrix.diag_apply, amplRef, Matrix.of_apply, Fintype.sum_prod_type]

theorem trace_eq_sum_refBlockR {S : Type*} [Fintype S] [DecidableEq S]
    (X : Matrix (R × S) (R × S) ℂ) : X.trace = ∑ i, (refBlockR X i i).trace := by
  simp only [Matrix.trace, Matrix.diag_apply, refBlockR, Matrix.of_apply, Fintype.sum_prod_type]

end Spectator

/-- **THE FULL THEORY HAS PARALLEL REFERENCE EXTENSION.** -/
theorem fullQuantum_parallelReferenceExtension : HasParallelReferenceExtension fullQuantum := by
  intro R _ _ n m e O _ _ F ⟨hcp, htr⟩
  refine ⟨fun a => withSpectator_cp e (hcp a), fun X => ?_⟩
  simp only [withSpectator_apply, trace_reindex, trace_amplRef]
  rw [Finset.sum_comm]
  rw [Finset.sum_congr rfl fun i _ => htr (refBlockR (Matrix.reindex e.symm e.symm X) i i),
    ← trace_eq_sum_refBlockR, trace_reindex e.symm]

/-- **THE CONJUNCTION IS SATISFIABLE**, and satisfied by a composite-sound theory. -/
theorem parallelReferenceExtension_satisfiable :
    ∃ T : FiniteOperationalTheory (Fin 2),
      ExactFiniteEndomorphicQuantumOps T ∧ HasCompositeUnitaryControl T
        ∧ HasParallelReferenceExtension T ∧ KrausSoundExt T :=
  ⟨fullQuantum, fullQuantum_exact, fullQuantum_control, fullQuantum_parallelReferenceExtension,
    fullQuantum_krausSoundExt⟩

end FullTheory

#print axioms unitVectorRotation_of_isometryExtension
#print axioms pureState_reachable
#print axioms sound_avail_cp_tp
#print axioms exact_avail_cp_tp
#print axioms cp_apply_posSemidef
#print axioms two_single_eq_dyads
#print axioms linear_functional_zero_of_dyads
#print axioms isHermitian_of_forms_real
#print axioms posSemidef_of_forms_nonneg
#print axioms forms_nonneg_of_unit
#print axioms branch_cp
#print axioms aggregate_trace
#print axioms krausSoundExt_of_sound_control_refext
#print axioms krausSoundExt_of_exact_control_refext
#print axioms countermodel_witness_level_two
#print axioms cp_comp
#print axioms localLuders_cp
#print axioms fullQuantum_exact
#print axioms fullQuantum_control
#print axioms fullQuantum_krausSoundExt
#print axioms withSpectator_conjChannel
#print axioms withSpectator_cp
#print axioms fullQuantum_parallelReferenceExtension
#print axioms parallelReferenceExtension_satisfiable

end ReferenceSufficiency
end OIBridge
