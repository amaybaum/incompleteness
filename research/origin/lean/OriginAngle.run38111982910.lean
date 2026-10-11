import OIBridge.DiscreteCompletion
import Mathlib.Data.Fintype.Pigeonhole

/-!
# Origin angle — design module of the research thread `research/origin` (round 4, O12)

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It states, in the kernel's vocabulary, the angle hypothesis "`rot α` is not a Clifford
element" for the level-one clause of `DenseUnitaryControl`, decides the hypothesis's two controls,
and reduces the level-one statement under it to two inputs named here.

* **The predicate** (`RotClifford`, `rotClifford_iff`): conjugation by `rot α` carries the Pauli
  set into itself exactly when `α` is an integer multiple of `π/4`.
* **Weaker than the kernel's hypothesis** (`not_rotClifford_of_irrational`,
  `not_rotClifford_pi_div_eight`, `not_irrational_pi_div_eight`, `rotClifford_weaker`): every angle
  with `α/π` irrational satisfies it, and so does `π/8`, with `α/π` rational.
* **The level-one clause** (`LevelOneClause`, `Gen2Dense`, `levelOneClause_of_dense`,
  `blockOf_gen2_mem`, `levelOneClause_of_gen2Dense`): density of the level-one group up to phase
  gives the clause in every theory with the closure and the gate.
* **The Clifford angles reduce to `π/4`** (`mixR_mix_nat`, `mixR_mix_int`, `mixR_of_int_mul`,
  `availExt_of_int_mul`, `levelOneClause_of_int_mul`, `levelOneClause_pi_div_four_of_rotClifford`,
  `availExt_pi_div_four_le_pi_div_eight`): the class at `k * β` lies in the class at `β`, so
  availability at every level, and the level-one clause, pass from `k * β` to `β`.
* **The level-one group** (`Gen2FiniteUpToScalar`, `gen2Finite_of_rotClifford`, `gen2_pow`,
  `pow_scalar_of_eq`, `exists_pow_scalar`, `not_gen2Finite_of_irrational`): finite up to scalar at
  every Clifford angle; not finite up to scalar at an angle with `α/π` irrational.
* **The positive instance** (`wordW`, `gen2_wordW`, `wordW_sq`, `cheb`, `wordW_pow`, `oddPair`,
  `oddPair_spec`, `oddPair_odd`, `cheb_succ_ne_zero`, `not_gen2Finite_pi_div_eight`): at `π/8` the
  word `rot (π/8) * rx (π/8)` has determinant one and trace `1 + √2/2`; its powers are
  `p (k+1) • W - p k • 1` for a Chebyshev sequence `p` with `√2 ^ k * p (k+1) = x + y √2` and `x`
  odd, so no power is a scalar and the level-one group at `π/8` is not finite up to scalar.
* **The statement and its controls** (`AngleWeakenedLevelOne`, `RationalDensityInput`,
  `BalancedFailureInput`, `angleWeakened_of_rational`, `AngleSufficesLevelOne`,
  `angleSuffices_of_irrational`, `angleSuffices_iff`, `not_angleSuffices_pi_div_four`,
  `control_countermodel`, `control_positive`, `o12_core`): given density at the rational angles
  where `rot α` is not a Clifford element, the weakened hypothesis gives the level-one clause in
  every theory with the closure and the gate; given in addition that the clause fails at `π/4`,
  the gate at `α` suffices for the clause in every such theory exactly when `rot α` is not a
  Clifford element.
-/

namespace OIBridge
namespace OriginAngle

open scoped Matrix
open scoped Matrix.Norms.L2Operator
open DiscreteCompletion

/-! ### Section A — the predicate -/

section Predicate

/-- **`rot α` IS A CLIFFORD ELEMENT**: conjugation by it carries the Pauli set into itself. -/
def RotClifford (α : ℝ) : Prop :=
  ∀ P ∈ Pauli, StateMixingCoupling.rot α * P * (StateMixingCoupling.rot α)ᴴ ∈ Pauli

theorem pauliBase_entry_mul (q : Fin 4) : pauliBase q 0 0 * pauliBase q 0 1 = 0 := by
  fin_cases q <;> simp [pauliBase, X2, Y2, Z2]

/-- Every element of the Pauli set is diagonal or off-diagonal. -/
theorem pauli_entry_mul {P : Matrix (Fin 2) (Fin 2) ℂ} (h : P ∈ Pauli) : P 0 0 * P 0 1 = 0 := by
  obtain ⟨k, q, rfl⟩ := mem_pauli.mp h
  rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul, mul_mul_mul_comm,
    pauliBase_entry_mul, mul_zero]

theorem rotZ_apply_00 (α : ℝ) :
    (StateMixingCoupling.rot α * Z2 * (StateMixingCoupling.rot α)ᴴ) 0 0
      = ((Real.cos α ^ 2 - Real.sin α ^ 2 : ℝ) : ℂ) := by
  rw [StateMixingCoupling.rot_conjTranspose]
  simp [StateMixingCoupling.rot, Z2, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_neg,
    Real.sin_neg] <;> ring

theorem rotZ_apply_01 (α : ℝ) :
    (StateMixingCoupling.rot α * Z2 * (StateMixingCoupling.rot α)ᴴ) 0 1
      = ((2 * Real.sin α * Real.cos α : ℝ) : ℂ) := by
  rw [StateMixingCoupling.rot_conjTranspose]
  simp [StateMixingCoupling.rot, Z2, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_neg,
    Real.sin_neg] <;> ring

/-- **THE CLIFFORD ANGLES**: `rot α` is a Clifford element exactly when `α` is an integer
multiple of `π/4`. -/
theorem rotClifford_iff (α : ℝ) : RotClifford α ↔ ∃ k : ℤ, α = k * (Real.pi / 4) := by
  constructor
  · intro h
    have h0 := pauli_entry_mul (h Z2 Z2_mem_pauli)
    rw [rotZ_apply_00, rotZ_apply_01] at h0
    have h0' : (Real.cos α ^ 2 - Real.sin α ^ 2) * (2 * Real.sin α * Real.cos α) = 0 := by
      exact_mod_cast h0
    have h4 : Real.sin (4 * α) = 0 := by
      have e1 := Real.sin_two_mul (2 * α)
      have e2 := Real.sin_two_mul α
      have e3 := Real.cos_two_mul α
      have hcs := Real.cos_sq_add_sin_sq α
      rw [show (2 : ℝ) * (2 * α) = 4 * α by ring] at e1
      rw [e1, e2, e3]
      linear_combination 2 * h0' + 4 * Real.sin α * Real.cos α * hcs
    obtain ⟨n, hn⟩ := Real.sin_eq_zero_iff.mp h4
    exact ⟨n, by linear_combination (-1 / 4 : ℝ) * hn⟩
  · rintro ⟨k, rfl⟩
    exact fun P hP => Gen2.pauli_conj (Gen2.rot_int (Real.pi / 4) k) P hP

/-- **THE COUNTERMODEL'S ANGLE IS EXCLUDED** by the hypothesis. -/
theorem rotClifford_pi_div_four : RotClifford (Real.pi / 4) :=
  (rotClifford_iff _).mpr ⟨1, by rw [Int.cast_one, one_mul]⟩

/-- At `π/8` the echo of the kernel's all-level route (`echo_identity`) isolates `rot (2 * (π/8))`,
which is a Clifford element. -/
theorem echo_angle_rotClifford : RotClifford (2 * (Real.pi / 8)) :=
  (rotClifford_iff _).mpr ⟨1, by push_cast; ring⟩

/-- **THE KERNEL'S HYPOTHESIS IMPLIES THE WEAKENED ONE.** -/
theorem not_rotClifford_of_irrational {α : ℝ} (hα : Irrational (α / Real.pi)) :
    ¬ RotClifford α := by
  rw [rotClifford_iff]
  rintro ⟨k, rfl⟩
  apply hα.ne_rat ((k : ℚ) / 4)
  rw [div_eq_iff Real.pi_ne_zero]
  push_cast
  ring

/-- **THE POSITIVE INSTANCE SATISFIES THE WEAKENED HYPOTHESIS.** -/
theorem not_rotClifford_pi_div_eight : ¬ RotClifford (Real.pi / 8) := by
  rw [rotClifford_iff]
  rintro ⟨k, hk⟩
  have h2 : ((2 * k - 1 : ℤ) : ℝ) * Real.pi = 0 := by
    push_cast
    linear_combination (-8 : ℝ) * hk
  rcases mul_eq_zero.mp h2 with h | h
  · have h' : (2 * k - 1 : ℤ) = 0 := by exact_mod_cast h
    omega
  · exact Real.pi_ne_zero h

/-- **AND NOT THE KERNEL'S**: `(π/8)/π` is rational. -/
theorem not_irrational_pi_div_eight : ¬ Irrational (Real.pi / 8 / Real.pi) := by
  intro h
  apply h.ne_rat (1 / 8)
  rw [div_eq_iff Real.pi_ne_zero]
  push_cast
  ring

/-- **THE WEAKENED HYPOTHESIS IS STRICTLY WEAKER** than the kernel's. -/
theorem rotClifford_weaker :
    (∀ α : ℝ, Irrational (α / Real.pi) → ¬ RotClifford α) ∧
      ∃ α : ℝ, ¬ RotClifford α ∧ ¬ Irrational (α / Real.pi) :=
  ⟨fun _ hα => not_rotClifford_of_irrational hα,
    ⟨Real.pi / 8, not_rotClifford_pi_div_eight, not_irrational_pi_div_eight⟩⟩

end Predicate

/-! ### Section B — the level-one clause -/

section LevelOne

/-- **THE LEVEL-ONE CLAUSE** of `DenseUnitaryControl`: its case `n = 1`. -/
def LevelOneClause (T : OperationalAssembly.FiniteOperationalTheory (Fin 2)) : Prop :=
  ∀ (U : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ), Uᴴ * U = 1 →
    ∀ ε : ℝ, 0 < ε → ∃ (V : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ) (c : ℂ),
      Vᴴ * V = 1 ∧ ‖c‖ = 1 ∧ T.availExt 1 Unit (fun _ => MonoidalCompletion.conjChannel V) ∧
        ‖U - c • V‖ < ε

theorem levelOneClause_of_dense {T : OperationalAssembly.FiniteOperationalTheory (Fin 2)}
    (h : DenseUnitaryControl T) : LevelOneClause T :=
  h 1

/-- **DENSITY OF THE LEVEL-ONE GROUP UP TO PHASE**, placed at level one. -/
def Gen2Dense (β : ℝ) : Prop :=
  ∀ (U : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ), Uᴴ * U = 1 → ∀ ε : ℝ, 0 < ε →
    ∃ (G : Matrix (Fin 2) (Fin 2) ℂ) (c : ℂ), Gen2 β G ∧ ‖c‖ = 1 ∧
      ‖U - c • blockOf (0 : Fin 1) G‖ < ε

/-- **THE LEVEL-ONE GROUP IS AVAILABLE AT LEVEL ONE** under the closure and the gate. -/
theorem blockOf_gen2_mem (T : OperationalAssembly.FiniteOperationalTheory (Fin 2))
    (hd : RouteB.DerivedOI T) {α : ℝ} (hg : FixedGateSourced α T) {G : Matrix (Fin 2) (Fin 2) ℂ}
    (h : Gen2 α G) : blockOf (0 : Fin 1) G ∈ availSet T 1 := by
  have R := blockRepertoire_levelOne T hd hg
  induction h with
  | one => rw [blockOf_one]; exact R.one_mem
  | rot => exact R.rot_mem
  | phase => exact R.phase_mem
  | swap => exact R.swap_mem
  | mul _ _ hA hB => rw [blockOf_mul]; exact R.mul_mem hA hB

/-- **DENSITY OF THE LEVEL-ONE GROUP GIVES THE LEVEL-ONE CLAUSE** in every theory with the closure
and the gate. -/
theorem levelOneClause_of_gen2Dense (T : OperationalAssembly.FiniteOperationalTheory (Fin 2))
    (hd : RouteB.DerivedOI T) {α : ℝ} (hg : FixedGateSourced α T) (h : Gen2Dense α) :
    LevelOneClause T := by
  intro U hU ε hε
  obtain ⟨G, c, hG, hc, hlt⟩ := h U hU ε hε
  exact ⟨blockOf (0 : Fin 1) G, c, blockOf_unitary (0 : Fin 1) hG.unitary, hc,
    (mem_availSet T).mp (blockOf_gen2_mem T hd hg hG), hlt⟩

end LevelOne

/-! ### Section C — the Clifford angles reduce to `π/4` -/

section Reduction

theorem mixR_mix_nat (β : ℝ) (n : ℕ) :
    ∀ k : ℕ, StateMixingCoupling.MixR {β} (Fin 2 × Fin n) (StateMixingCoupling.mixImage n (k * β))
  | 0 => by
      simpa [StateMixingCoupling.mixImage_zero] using
        (StateMixingCoupling.mixR_arch {β}).one (Fin 2 × Fin n)
  | k + 1 => by
      have h := StateMixingCoupling.MixR.mul _ _ (mixR_mix_nat β n k)
        (StateMixingCoupling.MixR.mix n β (Set.mem_singleton β))
      rwa [StateMixingCoupling.mixImage_mul,
        show (k : ℝ) * β + β = ((k + 1 : ℕ) : ℝ) * β by push_cast; ring] at h

theorem mixR_mix_int (β : ℝ) (n : ℕ) (k : ℤ) :
    StateMixingCoupling.MixR {β} (Fin 2 × Fin n) (StateMixingCoupling.mixImage n (k * β)) := by
  obtain ⟨m, hm | hm⟩ := Int.eq_nat_or_neg k
  · subst hm
    exact_mod_cast mixR_mix_nat β n m
  · subst hm
    have hP : StateMixingCoupling.MixR {β} (Fin 2 × Fin n)
        (CoherentLift.permMatrix (LiftAudit.levelPerm (Equiv.swap (0 : Fin 2) 1) n)) :=
      StateMixingCoupling.MixR.perm _ (SubstratumInterfaceAudit.permClass_permMatrix _)
    have h := StateMixingCoupling.MixR.mul _ _
      (StateMixingCoupling.MixR.mul _ _ hP (mixR_mix_nat β n m)) hP
    rw [mixImage_neg_eq_conj] at h
    rw [Int.cast_neg, Int.cast_natCast, neg_mul]
    exact h

/-- **THE CLASS AT `k * β` LIES IN THE CLASS AT `β`.** -/
theorem mixR_of_int_mul (β : ℝ) (k : ℤ) :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      StateMixingCoupling.MixR {(k : ℝ) * β} S K → StateMixingCoupling.MixR {β} S K := by
  intro S _ _ K h
  induction h with
  | perm K h => exact StateMixingCoupling.MixR.perm K h
  | phase n p => exact StateMixingCoupling.MixR.phase n p
  | mix n θ hθ =>
    rw [Set.mem_singleton_iff] at hθ
    subst hθ
    exact mixR_mix_int β n k
  | mul K L _ _ ihK ihL => exact StateMixingCoupling.MixR.mul K L ihK ihL
  | smul a K ha _ ih => exact StateMixingCoupling.MixR.smul a K ha ih
  | proj m j => exact StateMixingCoupling.MixR.proj m j
  | block m K f e _ ih => exact StateMixingCoupling.MixR.block m K f e ih
  | relabel e K _ ih => exact StateMixingCoupling.MixR.relabel e K ih

/-- **AVAILABILITY PASSES FROM `k * β` TO `β`**, at every level and for every family. -/
theorem availExt_of_int_mul (β : ℝ) (k : ℤ) (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (h : (fixedGateTheory ((k : ℝ) * β)).availExt n O F) : (fixedGateTheory β).availExt n O F :=
  InterventionLocality.instAvail_mono (mixR_of_int_mul β k) h

theorem levelOneClause_of_int_mul {β : ℝ} (k : ℤ)
    (h : LevelOneClause (fixedGateTheory ((k : ℝ) * β))) : LevelOneClause (fixedGateTheory β) := by
  intro U hU ε hε
  obtain ⟨V, c, hV, hc, hA, hlt⟩ := h U hU ε hε
  exact ⟨V, c, hV, hc, availExt_of_int_mul β k 1 hA, hlt⟩

/-- **AT EVERY CLIFFORD ANGLE THE LEVEL-ONE CLAUSE IMPLIES THE CLAUSE AT `π/4`.** -/
theorem levelOneClause_pi_div_four_of_rotClifford {α : ℝ} (hα : RotClifford α)
    (h : LevelOneClause (fixedGateTheory α)) : LevelOneClause (fixedGateTheory (Real.pi / 4)) := by
  obtain ⟨k, rfl⟩ := (rotClifford_iff α).mp hα
  exact levelOneClause_of_int_mul k h

/-- **THE POSITIVE INSTANCE CONTAINS THE COUNTERMODEL**: availability at `π/4` is availability at
`π/8`, at every level. -/
theorem availExt_pi_div_four_le_pi_div_eight (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ →ₗ[ℂ] Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ}
    (h : (fixedGateTheory (Real.pi / 4)).availExt n O F) :
    (fixedGateTheory (Real.pi / 8)).availExt n O F := by
  have e : Real.pi / 4 = ((2 : ℤ) : ℝ) * (Real.pi / 8) := by push_cast; ring
  rw [e] at h
  exact availExt_of_int_mul (Real.pi / 8) 2 n h

end Reduction

/-! ### Section D — the level-one group: finite up to scalar exactly where decided -/

section Group

/-- **THE LEVEL-ONE GROUP IS FINITE UP TO SCALAR**, in the shape of the kernel's T3. -/
def Gen2FiniteUpToScalar (β : ℝ) : Prop :=
  ∃ D : Set (Matrix (Fin 2) (Fin 2) ℂ), D.Finite ∧
    ∀ G, Gen2 β G → ∃ (c : ℂ) (M : Matrix (Fin 2) (Fin 2) ℂ), M ∈ D ∧ G = c • M

/-- **AT EVERY CLIFFORD ANGLE THE LEVEL-ONE GROUP IS FINITE UP TO SCALAR.** -/
theorem gen2Finite_of_rotClifford {α : ℝ} (h : RotClifford α) : Gen2FiniteUpToScalar α := by
  obtain ⟨k, rfl⟩ := (rotClifford_iff α).mp h
  exact gen2_multiple_finite_upToScalar k

theorem gen2_pow {β : ℝ} {W : Matrix (Fin 2) (Fin 2) ℂ} (h : Gen2 β W) :
    ∀ k : ℕ, Gen2 β (W ^ k)
  | 0 => by rw [pow_zero]; exact Gen2.one
  | k + 1 => by rw [pow_succ]; exact Gen2.mul (gen2_pow h k) h

/-- Two powers proportional to one matrix: their quotient power is a scalar. -/
theorem pow_scalar_of_eq {W : Matrix (Fin 2) (Fin 2) ℂ} {i j : ℕ} (hij : i < j)
    (hu : (W ^ i)ᴴ * W ^ i = 1) {ci cj : ℂ} {M : Matrix (Fin 2) (Fin 2) ℂ}
    (hi : W ^ i = ci • M) (hj : W ^ j = cj • M) :
    ∃ c : ℂ, W ^ (j - i) = c • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  have hu' : W ^ i * (W ^ i)ᴴ = 1 := mul_eq_one_comm.mp hu
  have hci : ci ≠ 0 := by
    rintro rfl
    rw [zero_smul] at hi
    rw [hi, Matrix.mul_zero] at hu
    exact zero_ne_one hu
  refine ⟨cj * ci⁻¹, ?_⟩
  have hM : M = ci⁻¹ • W ^ i := by rw [hi, smul_smul, inv_mul_cancel₀ hci, one_smul]
  have key : W ^ (j - i) * W ^ i = (cj * ci⁻¹) • W ^ i := by
    rw [← pow_add, Nat.sub_add_cancel hij.le, hj, hM, smul_smul]
  calc W ^ (j - i) = W ^ (j - i) * (W ^ i * (W ^ i)ᴴ) := by rw [hu', Matrix.mul_one]
    _ = (W ^ (j - i) * W ^ i) * (W ^ i)ᴴ := by rw [Matrix.mul_assoc]
    _ = ((cj * ci⁻¹) • W ^ i) * (W ^ i)ᴴ := by rw [key]
    _ = (cj * ci⁻¹) • (W ^ i * (W ^ i)ᴴ) := by rw [Matrix.smul_mul]
    _ = (cj * ci⁻¹) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by rw [hu']

/-- **IN A GROUP FINITE UP TO SCALAR EVERY ELEMENT HAS A SCALAR POWER**, by pigeonhole. -/
theorem exists_pow_scalar {β : ℝ} (hfin : Gen2FiniteUpToScalar β) {W : Matrix (Fin 2) (Fin 2) ℂ}
    (hW : Gen2 β W) : ∃ m : ℕ, 0 < m ∧ ∃ c : ℂ, W ^ m = c • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  obtain ⟨D, hD, h⟩ := hfin
  have hfinD : Finite D := hD.to_subtype
  have hpow : ∀ k : ℕ, ∃ (c : ℂ) (M : Matrix (Fin 2) (Fin 2) ℂ), M ∈ D ∧ W ^ k = c • M :=
    fun k => h _ (gen2_pow hW k)
  choose c M hM hcM using hpow
  obtain ⟨i, j, hij, hfij⟩ :=
    Finite.exists_ne_map_eq_of_infinite (fun k : ℕ => (⟨M k, hM k⟩ : D))
  have hMij : M i = M j := congrArg Subtype.val hfij
  rcases lt_or_gt_of_ne hij with hlt | hlt
  · have hj' : W ^ j = c j • M i := by rw [hcM j, hMij]
    obtain ⟨c', hc'⟩ := pow_scalar_of_eq hlt (gen2_pow hW i).unitary (hcM i) hj'
    exact ⟨j - i, Nat.sub_pos_of_lt hlt, c', hc'⟩
  · have hi' : W ^ i = c i • M j := by rw [hcM i, hMij]
    obtain ⟨c', hc'⟩ := pow_scalar_of_eq hlt (gen2_pow hW j).unitary (hcM j) hi'
    exact ⟨i - j, Nat.sub_pos_of_lt hlt, c', hc'⟩

/-- **AT AN IRRATIONAL ANGLE THE LEVEL-ONE GROUP IS NOT FINITE UP TO SCALAR.** -/
theorem not_gen2Finite_of_irrational {α : ℝ} (hα : Irrational (α / Real.pi)) :
    ¬ Gen2FiniteUpToScalar α := by
  intro hfin
  obtain ⟨m, hm, c, hc⟩ := exists_pow_scalar hfin (Gen2.rot (β := α))
  rw [rot_pow] at hc
  have h10 := congrFun (congrFun hc 1) 0
  rw [StateMixingCoupling.rot_apply_10, Matrix.smul_apply,
    Matrix.one_apply_ne (show (1 : Fin 2) ≠ 0 by decide), smul_zero] at h10
  have hsin : Real.sin ((m : ℝ) * α) = 0 := Complex.ofReal_eq_zero.mp h10
  obtain ⟨n, hn⟩ := Real.sin_eq_zero_iff.mp hsin
  have hm0 : (m : ℝ) ≠ 0 := by exact_mod_cast hm.ne'
  apply hα.ne_rat ((n : ℚ) / m)
  rw [div_eq_iff Real.pi_ne_zero]
  push_cast
  rw [div_mul_eq_mul_div, eq_div_iff hm0]
  linear_combination (-1 : ℝ) * hn

end Group

/-! ### Section E — the positive instance `π/8`: a word of infinite order -/

section PiDivEight

/-- **THE WORD**: the datum, then its quarter-phase conjugate. -/
noncomputable def wordW (β : ℝ) : Matrix (Fin 2) (Fin 2) ℂ := StateMixingCoupling.rot β * rx β

theorem gen2_wordW (β : ℝ) : Gen2 β (wordW β) := by
  show Gen2 β (StateMixingCoupling.rot β * rx β)
  rw [← rx_eq_conj, S2_conjTranspose_eq_cube]
  exact Gen2.mul Gen2.rot (Gen2.mul (Gen2.mul Gen2.phase Gen2.rot)
    (Gen2.mul (Gen2.mul Gen2.phase Gen2.phase) Gen2.phase))

theorem rot_det (β : ℝ) : (StateMixingCoupling.rot β).det = 1 := by
  have h : ((Real.cos β : ℂ)) ^ 2 + ((Real.sin β : ℂ)) ^ 2 = 1 := by
    exact_mod_cast Real.cos_sq_add_sin_sq β
  simp only [StateMixingCoupling.rot, Matrix.det_fin_two_of]
  linear_combination h

theorem rx_det (β : ℝ) : (rx β).det = 1 := by
  have h : ((Real.cos β : ℂ)) ^ 2 + ((Real.sin β : ℂ)) ^ 2 = 1 := by
    exact_mod_cast Real.cos_sq_add_sin_sq β
  simp only [rx, Matrix.det_fin_two_of]
  linear_combination h - ((Real.sin β : ℂ)) ^ 2 * Complex.I_sq

theorem wordW_det (β : ℝ) : (wordW β).det = 1 := by
  show (StateMixingCoupling.rot β * rx β).det = 1
  rw [Matrix.det_mul, rot_det, rx_det, one_mul]

theorem wordW_trace (β : ℝ) : (wordW β).trace = ((2 * Real.cos β ^ 2 : ℝ) : ℂ) := by
  rw [Matrix.trace_fin_two]
  simp [wordW, StateMixingCoupling.rot, rx, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

theorem wordW_apply_01 (β : ℝ) :
    wordW β 0 1 = ((Real.cos β * Real.sin β : ℝ) : ℂ) * (Complex.I - 1) := by
  simp [wordW, StateMixingCoupling.rot, rx, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

theorem wordW_apply_01_ne_zero : wordW (Real.pi / 8) 0 1 ≠ 0 := by
  rw [wordW_apply_01]
  have hc : 0 < Real.cos (Real.pi / 8) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩
  have hs : 0 < Real.sin (Real.pi / 8) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [Real.pi_pos]) (by linarith [Real.pi_pos])
  have hcs : ((Real.cos (Real.pi / 8) * Real.sin (Real.pi / 8) : ℝ) : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (mul_pos hc hs).ne'
  have hI : Complex.I - 1 ≠ 0 := by
    intro h
    have h' := congrArg Complex.re h
    simp at h'
  exact mul_ne_zero hcs hI

theorem two_cos_sq_pi_div_eight : 2 * Real.cos (Real.pi / 8) ^ 2 = 1 + Real.sqrt 2 / 2 := by
  rw [Real.cos_sq, show (2 : ℝ) * (Real.pi / 8) = Real.pi / 4 by ring, Real.cos_pi_div_four]
  ring

theorem wordW_trace_pi_div_eight :
    (wordW (Real.pi / 8)).trace = ((1 + Real.sqrt 2 / 2 : ℝ) : ℂ) := by
  rw [wordW_trace, two_cos_sq_pi_div_eight]

/-- Cayley–Hamilton on two-by-two matrices. -/
theorem mul_self_fin_two (A : Matrix (Fin 2) (Fin 2) ℂ) :
    A * A = A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.det_fin_two] <;> ring

theorem wordW_sq : wordW (Real.pi / 8) * wordW (Real.pi / 8)
    = ((1 + Real.sqrt 2 / 2 : ℝ) : ℂ) • wordW (Real.pi / 8) - 1 := by
  rw [mul_self_fin_two, wordW_trace_pi_div_eight, wordW_det, one_smul]

/-- The Chebyshev pairs `(p k, p (k+1))` of the trace `1 + √2/2`. -/
noncomputable def chebPair : ℕ → ℝ × ℝ
  | 0 => (0, 1)
  | k + 1 => ((chebPair k).2, (1 + Real.sqrt 2 / 2) * (chebPair k).2 - (chebPair k).1)

/-- The Chebyshev sequence `p`: `p 0 = 0`, `p 1 = 1`, `p (k+2) = (1 + √2/2) p (k+1) - p k`. -/
noncomputable def cheb (k : ℕ) : ℝ := (chebPair k).1

theorem cheb_zero : cheb 0 = 0 := rfl

theorem cheb_one : cheb 1 = 1 := rfl

theorem cheb_succ_succ (k : ℕ) :
    cheb (k + 1 + 1) = (1 + Real.sqrt 2 / 2) * cheb (k + 1) - cheb k := rfl

/-- **THE POWERS OF THE WORD** at `π/8`. -/
theorem wordW_pow (k : ℕ) : wordW (Real.pi / 8) ^ (k + 1)
    = (cheb (k + 1) : ℂ) • wordW (Real.pi / 8) - (cheb k : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  induction k with
  | zero =>
    show wordW (Real.pi / 8) ^ 1
      = (cheb 1 : ℂ) • wordW (Real.pi / 8) - (cheb 0 : ℂ) • (1 : Matrix (Fin 2) (Fin 2) ℂ)
    rw [pow_one, cheb_one, cheb_zero, Complex.ofReal_one, Complex.ofReal_zero, one_smul, zero_smul,
      sub_zero]
  | succ k ih =>
    rw [pow_succ, ih, cheb_succ_succ, Matrix.sub_mul, Matrix.smul_mul, Matrix.smul_mul,
      Matrix.one_mul, wordW_sq]
    ext i j
    simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul]
    push_cast
    ring

/-- The integer pairs `((x (k+1), y (k+1)), (x (k+2), y (k+2)))`. -/
def oddPair : ℕ → (ℤ × ℤ) × (ℤ × ℤ)
  | 0 => ((1, 0), (1, 1))
  | k + 1 => ((oddPair k).2, ((oddPair k).2.1 + 2 * (oddPair k).2.2 - 2 * (oddPair k).1.1,
      (oddPair k).2.1 + (oddPair k).2.2 - 2 * (oddPair k).1.2))

/-- **THE SCALED SEQUENCE IN `ℤ[√2]`**: `√2 ^ k * p (k+1) = x (k+1) + y (k+1) √2`. -/
theorem oddPair_spec (k : ℕ) :
    Real.sqrt 2 ^ k * cheb (k + 1) = ((oddPair k).1.1 : ℝ) + ((oddPair k).1.2 : ℝ) * Real.sqrt 2 ∧
      Real.sqrt 2 ^ (k + 1) * cheb (k + 1 + 1)
        = ((oddPair k).2.1 : ℝ) + ((oddPair k).2.2 : ℝ) * Real.sqrt 2 := by
  have hs : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  induction k with
  | zero =>
    refine ⟨?_, ?_⟩
    · show Real.sqrt 2 ^ 0 * 1 = ((1 : ℤ) : ℝ) + ((0 : ℤ) : ℝ) * Real.sqrt 2
      push_cast
      ring
    · show Real.sqrt 2 ^ (0 + 1) * ((1 + Real.sqrt 2 / 2) * 1 - 0)
          = ((1 : ℤ) : ℝ) + ((1 : ℤ) : ℝ) * Real.sqrt 2
      push_cast
      linear_combination (1 / 2 : ℝ) * hs
  | succ k ih =>
    obtain ⟨h1, h2⟩ := ih
    refine ⟨h2, ?_⟩
    show Real.sqrt 2 ^ (k + 1 + 1) * cheb (k + 1 + 1 + 1)
        = (((oddPair k).2.1 + 2 * (oddPair k).2.2 - 2 * (oddPair k).1.1 : ℤ) : ℝ)
          + (((oddPair k).2.1 + (oddPair k).2.2 - 2 * (oddPair k).1.2 : ℤ) : ℝ) * Real.sqrt 2
    rw [cheb_succ_succ (k + 1)]
    push_cast
    linear_combination (Real.sqrt 2 + Real.sqrt 2 * Real.sqrt 2 / 2) * h2
      - Real.sqrt 2 * Real.sqrt 2 * h1
      + (((oddPair k).2.2 : ℝ) + ((oddPair k).2.1 : ℝ) / 2 - ((oddPair k).1.1 : ℝ)
        + (((oddPair k).2.2 : ℝ) / 2 - ((oddPair k).1.2 : ℝ)) * Real.sqrt 2) * hs

/-- **THE TWO-ADIC PARITY**: the integer part `x` is odd at every step. -/
theorem oddPair_odd (k : ℕ) : (oddPair k).1.1 % 2 = 1 ∧ (oddPair k).2.1 % 2 = 1 := by
  induction k with
  | zero => exact ⟨by decide, by decide⟩
  | succ k ih =>
    obtain ⟨h1, h2⟩ := ih
    refine ⟨h2, ?_⟩
    show ((oddPair k).2.1 + 2 * (oddPair k).2.2 - 2 * (oddPair k).1.1) % 2 = 1
    omega

/-- **THE CHEBYSEQUENCE NEVER VANISHES** after its first term. -/
theorem cheb_succ_ne_zero (k : ℕ) : cheb (k + 1) ≠ 0 := by
  intro h
  have hA := (oddPair_spec k).1
  rw [h, mul_zero] at hA
  have hx := (oddPair_odd k).1
  by_cases hy : (oddPair k).1.2 = 0
  · rw [hy, Int.cast_zero, zero_mul, add_zero] at hA
    have h0 : (oddPair k).1.1 = 0 := by exact_mod_cast hA.symm
    omega
  · have hyR : ((oddPair k).1.2 : ℝ) ≠ 0 := by exact_mod_cast hy
    apply irrational_sqrt_two.ne_rat (-((oddPair k).1.1 : ℚ) / ((oddPair k).1.2 : ℚ))
    push_cast
    rw [eq_div_iff hyR]
    linear_combination (-1 : ℝ) * hA

/-- **AT `π/8` THE LEVEL-ONE GROUP IS NOT FINITE UP TO SCALAR**: no power of the word is a scalar. -/
theorem not_gen2Finite_pi_div_eight : ¬ Gen2FiniteUpToScalar (Real.pi / 8) := by
  intro hfin
  obtain ⟨m, hm, c, hc⟩ := exists_pow_scalar hfin (gen2_wordW (Real.pi / 8))
  obtain ⟨k, rfl⟩ : ∃ k, m = k + 1 := ⟨m - 1, by omega⟩
  rw [wordW_pow k] at hc
  have h01 := congrFun (congrFun hc 0) 1
  simp only [Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul,
    Matrix.one_apply_ne (show (0 : Fin 2) ≠ 1 by decide), mul_zero, sub_zero] at h01
  rcases mul_eq_zero.mp h01 with h | h
  · exact cheb_succ_ne_zero k (Complex.ofReal_eq_zero.mp h)
  · exact wordW_apply_01_ne_zero h

end PiDivEight

/-! ### Section F — the statement, its inputs and its two controls -/

section Statement

/-- **THE WEAKENED HYPOTHESIS AT LEVEL ONE, AS A STATEMENT**: in every theory with the closure and
the gate at an angle at which `rot α` is not a Clifford element, the level-one clause holds. -/
def AngleWeakenedLevelOne : Prop :=
  ∀ (T : OperationalAssembly.FiniteOperationalTheory (Fin 2)) (α : ℝ), RouteB.DerivedOI T →
    FixedGateSourced α T → ¬ RotClifford α → LevelOneClause T

/-- **THE INPUT AT THE RATIONAL ANGLES**: the level-one group is dense up to phase at every angle
with `α/π` rational at which `rot α` is not a Clifford element. -/
def RationalDensityInput : Prop :=
  ∀ α : ℝ, ¬ RotClifford α → ¬ Irrational (α / Real.pi) → Gen2Dense α

/-- **THE INPUT AT THE BALANCED ANGLE**: the level-one clause fails in the canonical theory at
`π/4`. -/
def BalancedFailureInput : Prop :=
  ¬ LevelOneClause (fixedGateTheory (Real.pi / 4))

/-- **THE GATE AT `α` SUFFICES AT LEVEL ONE**, in every theory with the closure. -/
def AngleSufficesLevelOne (α : ℝ) : Prop :=
  ∀ T : OperationalAssembly.FiniteOperationalTheory (Fin 2), RouteB.DerivedOI T →
    FixedGateSourced α T → LevelOneClause T

/-- At an angle with `α/π` irrational the gate suffices: the kernel's `levelOne_dense`. -/
theorem angleSuffices_of_irrational {α : ℝ} (hα : Irrational (α / Real.pi)) :
    AngleSufficesLevelOne α :=
  fun T hd hg => levelOne_dense T hd hα hg

/-- **THE WEAKENED STATEMENT FROM THE RATIONAL INPUT.** -/
theorem angleWeakened_of_rational (hR : RationalDensityInput) : AngleWeakenedLevelOne := by
  intro T α hd hg hc
  by_cases hα : Irrational (α / Real.pi)
  · exact levelOne_dense T hd hα hg
  · exact levelOneClause_of_gen2Dense T hd hg (hR α hc hα)

/-- **THE COUNTERMODEL**: if the clause fails at `π/4`, the gate at `π/4` does not suffice. -/
theorem not_angleSuffices_pi_div_four (hB : BalancedFailureInput) :
    ¬ AngleSufficesLevelOne (Real.pi / 4) :=
  fun h => hB (h _ (fixedGateTheory_derivedOI _) (fixedGateTheory_fixedGateSourced _))

/-- **THE ANGLE CONDITION AT LEVEL ONE, ONE DIRECTION AT A TIME**: from the rational input, the
weakened hypothesis suffices; from the balanced input, through the reduction of every Clifford
angle to `π/4`, it is necessary. -/
theorem angleSuffices_iff (hR : RationalDensityInput) (hB : BalancedFailureInput) (α : ℝ) :
    AngleSufficesLevelOne α ↔ ¬ RotClifford α := by
  constructor
  · intro h hc
    exact hB (levelOneClause_pi_div_four_of_rotClifford hc
      (h _ (fixedGateTheory_derivedOI α) (fixedGateTheory_fixedGateSourced α)))
  · intro hc T hd hg
    exact angleWeakened_of_rational hR T α hd hg hc

/-- **CONTROL ONE, THE COUNTERMODEL `fixedGateTheory (π/4)`**: it has the closure and the gate, its
angle is excluded by the weakened hypothesis, its level-one group is finite up to scalar, and every
Clifford angle reduces to it at level one. -/
theorem control_countermodel :
    RouteB.DerivedOI (fixedGateTheory (Real.pi / 4)) ∧
      FixedGateSourced (Real.pi / 4) (fixedGateTheory (Real.pi / 4)) ∧
      RotClifford (Real.pi / 4) ∧ Gen2FiniteUpToScalar (Real.pi / 4) ∧
      (∀ α : ℝ, RotClifford α → LevelOneClause (fixedGateTheory α) →
        LevelOneClause (fixedGateTheory (Real.pi / 4))) :=
  ⟨fixedGateTheory_derivedOI _, fixedGateTheory_fixedGateSourced _, rotClifford_pi_div_four,
    gen2Finite_of_rotClifford rotClifford_pi_div_four,
    fun _ hc h => levelOneClause_pi_div_four_of_rotClifford hc h⟩

/-- **CONTROL TWO, THE POSITIVE INSTANCE `π/8`**: it has the closure and the gate, satisfies the
weakened hypothesis but not the kernel's, its level-one group is not finite up to scalar, and the
kernel's echo at `π/8` isolates a Clifford element. -/
theorem control_positive :
    RouteB.DerivedOI (fixedGateTheory (Real.pi / 8)) ∧
      FixedGateSourced (Real.pi / 8) (fixedGateTheory (Real.pi / 8)) ∧
      ¬ RotClifford (Real.pi / 8) ∧ ¬ Irrational (Real.pi / 8 / Real.pi) ∧
      ¬ Gen2FiniteUpToScalar (Real.pi / 8) ∧ RotClifford (2 * (Real.pi / 8)) :=
  ⟨fixedGateTheory_derivedOI _, fixedGateTheory_fixedGateSourced _, not_rotClifford_pi_div_eight,
    not_irrational_pi_div_eight, not_gen2Finite_pi_div_eight, echo_angle_rotClifford⟩

/-- **THE MODULE'S CORE.** -/
theorem o12_core :
    (∀ α : ℝ, RotClifford α ↔ ∃ k : ℤ, α = k * (Real.pi / 4)) ∧
      (∀ α : ℝ, Irrational (α / Real.pi) → AngleSufficesLevelOne α) ∧
      (RationalDensityInput → AngleWeakenedLevelOne) ∧
      (RationalDensityInput → BalancedFailureInput →
        ∀ α : ℝ, AngleSufficesLevelOne α ↔ ¬ RotClifford α) ∧
      (∀ α : ℝ, RotClifford α → Gen2FiniteUpToScalar α) ∧
      (∀ α : ℝ, Irrational (α / Real.pi) → ¬ Gen2FiniteUpToScalar α) ∧
      ¬ Gen2FiniteUpToScalar (Real.pi / 8) :=
  ⟨rotClifford_iff, fun _ hα => angleSuffices_of_irrational hα, angleWeakened_of_rational,
    fun hR hB α => angleSuffices_iff hR hB α, fun _ h => gen2Finite_of_rotClifford h,
    fun _ hα => not_gen2Finite_of_irrational hα, not_gen2Finite_pi_div_eight⟩

end Statement

#print axioms pauliBase_entry_mul
#print axioms pauli_entry_mul
#print axioms rotZ_apply_00
#print axioms rotZ_apply_01
#print axioms rotClifford_iff
#print axioms rotClifford_pi_div_four
#print axioms echo_angle_rotClifford
#print axioms not_rotClifford_of_irrational
#print axioms not_rotClifford_pi_div_eight
#print axioms not_irrational_pi_div_eight
#print axioms rotClifford_weaker
#print axioms levelOneClause_of_dense
#print axioms blockOf_gen2_mem
#print axioms levelOneClause_of_gen2Dense
#print axioms mixR_mix_nat
#print axioms mixR_mix_int
#print axioms mixR_of_int_mul
#print axioms availExt_of_int_mul
#print axioms levelOneClause_of_int_mul
#print axioms levelOneClause_pi_div_four_of_rotClifford
#print axioms availExt_pi_div_four_le_pi_div_eight
#print axioms gen2Finite_of_rotClifford
#print axioms gen2_pow
#print axioms pow_scalar_of_eq
#print axioms exists_pow_scalar
#print axioms not_gen2Finite_of_irrational
#print axioms gen2_wordW
#print axioms rot_det
#print axioms rx_det
#print axioms wordW_det
#print axioms wordW_trace
#print axioms wordW_apply_01
#print axioms wordW_apply_01_ne_zero
#print axioms two_cos_sq_pi_div_eight
#print axioms wordW_trace_pi_div_eight
#print axioms mul_self_fin_two
#print axioms wordW_sq
#print axioms cheb_zero
#print axioms cheb_one
#print axioms cheb_succ_succ
#print axioms wordW_pow
#print axioms oddPair_spec
#print axioms oddPair_odd
#print axioms cheb_succ_ne_zero
#print axioms not_gen2Finite_pi_div_eight
#print axioms angleSuffices_of_irrational
#print axioms angleWeakened_of_rational
#print axioms not_angleSuffices_pi_div_four
#print axioms angleSuffices_iff
#print axioms control_countermodel
#print axioms control_positive
#print axioms o12_core

end OriginAngle
end OIBridge
