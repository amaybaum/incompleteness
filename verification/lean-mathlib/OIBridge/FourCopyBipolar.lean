/-
  OIBridge/FourCopyBipolar.lean — design (EQ4-F), not adopted: the bipolar theorem on the table
  carrier and the recurrence lemma. Every proof in this file is complete.

  * O30 (`isClosed_dualW`): dual cones are closed.
  * O33 (`dualW_dualW`): the bidual of a nonempty convex cone of tables is its closure. The
    separating functional of the Hahn–Banach theorem is represented by a table (`clm_eq_ipW`).
  * `bidual_of_adm`: an admissible closed pair cone is its own bidual.
  * (R) (`inv_mem_of_orth`): a linear equivalence of the tables that is orthogonal for the pairing
    and maps a closed set into itself also has its inverse map the set into itself. The proof is
    the recurrence of the orbit `Nⁿ ω` on a sphere of the pairing; it reads orthogonality,
    closedness and forward preservation, and nothing else. It removes inverse-gate preservation as
    a separate hypothesis wherever the pair cone is closed.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyCore
import Mathlib.Topology.MetricSpace.Sequences

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody
open Filter Topology

noncomputable section

/-! ### §A — closedness of dual cones -/

/-- **O30.** Dual cones are closed. -/
theorem isClosed_dualW (K : Set (W 3)) : IsClosed (dualW K) := by
  have h : dualW K = ⋂ X ∈ K, {E : W 3 | 0 ≤ ipW E X} := by
    ext E
    simp only [dualW, Set.mem_setOf_eq, Set.mem_iInter]
  rw [h]
  refine isClosed_biInter fun X _ => isClosed_le continuous_const ?_
  show Continuous fun E : W 3 => ∑ μ, ∑ ν, E μ ν * X μ ν
  exact continuous_finset_sum _ fun μ _ => continuous_finset_sum _ fun ν _ =>
    ((continuous_apply ν).comp (continuous_apply μ)).mul continuous_const

theorem subset_dualW_dualW (K : Set (W 3)) : K ⊆ dualW (dualW K) :=
  fun X hX => mem_dualW.2 fun E hE => mem_dualW.1 hE X hX

/-! ### §B — tables represent linear functionals -/

/-- The basis table with a single unit entry at `(μ, ν)`. -/
def unitW (μ ν : Fin (3 + 1)) : W 3 := fun μ' ν' => if μ' = μ ∧ ν' = ν then 1 else 0

set_option maxHeartbeats 1000000 in
theorem table_decomp (Y : W 3) : Y = ∑ μ, ∑ ν, Y μ ν • unitW μ ν := by
  funext μ' ν'
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, unitW]
  fin_cases μ' <;> fin_cases ν' <;> simp +decide [sum_univ_four']

/-- A continuous linear functional of the tables is the pairing with a table. -/
theorem clm_eq_ipW (f : W 3 →L[ℝ] ℝ) (Y : W 3) :
    f Y = ipW (fun μ ν => f (unitW μ ν)) Y := by
  conv_lhs => rw [table_decomp Y]
  simp only [map_sum, map_smul, smul_eq_mul, ipW]
  refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
  ring

theorem ipW_neg_left (E X : W 3) : ipW (-E) X = -ipW E X := by
  unfold ipW
  simp only [Pi.neg_apply, neg_mul, Finset.sum_neg_distrib]

/-! ### §C — O33: the bipolar theorem -/

theorem convex_of_cone {K : Set (W 3)} (hK : IsConvexCone K) : Convex ℝ K := by
  intro x hx y hy a b ha hb _
  exact hK.1 _ (hK.2 a ha x hx) _ (hK.2 b hb y hy)

theorem zero_mem_of_cone {K : Set (W 3)} (hK : IsConvexCone K) (hne : K.Nonempty) :
    (0 : W 3) ∈ K := by
  obtain ⟨y, hy⟩ := hne
  have h := hK.2 0 le_rfl y hy
  rwa [zero_smul] at h

/-- **O33.** The bidual of a nonempty convex cone of tables is its closure. -/
theorem dualW_dualW {K : Set (W 3)} (hK : IsConvexCone K) (hne : K.Nonempty) :
    dualW (dualW K) = closure K := by
  apply Set.Subset.antisymm
  · intro X hX
    by_contra hXK
    obtain ⟨f, u, hfu, hux⟩ :=
      geometric_hahn_banach_closed_point (convex_of_cone hK).closure isClosed_closure hXK
    have hu : 0 < u := by
      have h0 := hfu 0 (subset_closure (zero_mem_of_cone hK hne))
      rwa [map_zero] at h0
    have hle : ∀ Y ∈ K, f Y ≤ 0 := by
      intro Y hY
      by_contra hpos
      push_neg at hpos
      have ht : 0 ≤ u / f Y + 1 := add_nonneg (div_nonneg hu.le hpos.le) zero_le_one
      have hmem := hfu _ (subset_closure (hK.2 _ ht Y hY))
      rw [map_smul, smul_eq_mul, add_mul, div_mul_cancel₀ _ hpos.ne', one_mul] at hmem
      linarith
    obtain ⟨E0, hE0⟩ : ∃ E0 : W 3, E0 = fun μ ν => f (unitW μ ν) := ⟨_, rfl⟩
    have hE : -E0 ∈ dualW K := by
      refine mem_dualW.2 fun Y hY => ?_
      rw [ipW_neg_left, hE0, ← clm_eq_ipW]
      linarith [hle Y hY]
    have hX0 := mem_dualW.1 hX (-E0) hE
    rw [ipW_neg_left, hE0, ← clm_eq_ipW] at hX0
    linarith
  · exact closure_minimal (subset_dualW_dualW K) (isClosed_dualW _)

/-- An admissible closed pair cone is its own bidual. -/
theorem bidual_of_adm {K : Set (W 3)} (hK : PairAdm K) (hcl : IsClosed K) :
    dualW (dualW K) = K := by
  rw [dualW_dualW hK.2 ⟨prodState 0 0, hK.1.1 0 zero_mem_eball 0 zero_mem_eball⟩,
    hcl.closure_eq]

/-! ### §D — (R): the recurrence lemma -/

theorem sq_le_ipW_self (Z : W 3) (μ ν : Fin (3 + 1)) : Z μ ν ^ 2 ≤ ipW Z Z := by
  have h1 : Z μ ν * Z μ ν ≤ ∑ ν', Z μ ν' * Z μ ν' :=
    Finset.single_le_sum (f := fun ν' => Z μ ν' * Z μ ν')
      (fun ν' _ => mul_self_nonneg (Z μ ν')) (Finset.mem_univ ν)
  have h2 : ∑ ν', Z μ ν' * Z μ ν' ≤ ipW Z Z :=
    Finset.single_le_sum (f := fun μ' => ∑ ν', Z μ' ν' * Z μ' ν')
      (fun μ' _ => Finset.sum_nonneg fun ν' _ => mul_self_nonneg (Z μ' ν'))
      (Finset.mem_univ μ)
  rw [sq]
  exact h1.trans h2

theorem norm_le_sqrt_ipW (Z : W 3) : ‖Z‖ ≤ Real.sqrt (ipW Z Z) := by
  refine (pi_norm_le_iff_of_nonneg (Real.sqrt_nonneg _)).2 fun μ => ?_
  refine (pi_norm_le_iff_of_nonneg (Real.sqrt_nonneg _)).2 fun ν => ?_
  rw [Real.norm_eq_abs]
  exact Real.abs_le_sqrt (sq_le_ipW_self Z μ ν)

theorem ipW_self_le (Z : W 3) : ipW Z Z ≤ 16 * ‖Z‖ ^ 2 := by
  have hb : ∀ μ ν, Z μ ν * Z μ ν ≤ ‖Z‖ ^ 2 := by
    intro μ ν
    have h1 : |Z μ ν| ≤ ‖Z‖ := by
      rw [← Real.norm_eq_abs]
      exact (norm_le_pi_norm (Z μ) ν).trans (norm_le_pi_norm Z μ)
    rw [← abs_mul_abs_self, sq]
    exact mul_le_mul h1 h1 (abs_nonneg _) (norm_nonneg _)
  simp only [ipW, sum_univ_four']
  linarith [hb 0 0, hb 0 1, hb 0 2, hb 0 3, hb 1 0, hb 1 1, hb 1 2, hb 1 3,
    hb 2 0, hb 2 1, hb 2 2, hb 2 3, hb 3 0, hb 3 1, hb 3 2, hb 3 3]

/-- **(R) The recurrence lemma.** A linear equivalence of the tables that is orthogonal for the
pairing and maps a closed set into itself has its inverse map the set into itself. -/
theorem inv_mem_of_orth {N : W 3 ≃ₗ[ℝ] W 3} (hNo : ∀ E X, ipW (N E) (N X) = ipW E X)
    {K : Set (W 3)} (hcl : IsClosed K) (hgate : ∀ ω ∈ K, N ω ∈ K) :
    ∀ ω ∈ K, N.symm ω ∈ K := by
  intro ω hω
  have hD : ∀ X Y : W 3, ipW (N X - N Y) (N X - N Y) = ipW (X - Y) (X - Y) := fun X Y => by
    rw [← map_sub, hNo]
  have hDit : ∀ (n : ℕ) (X Y : W 3),
      ipW ((⇑N)^[n] X - (⇑N)^[n] Y) ((⇑N)^[n] X - (⇑N)^[n] Y) = ipW (X - Y) (X - Y) := by
    intro n
    induction n with
    | zero => intro X Y; rfl
    | succ n ih =>
      intro X Y
      rw [Function.iterate_succ_apply', Function.iterate_succ_apply', hD, ih]
  have hxK : ∀ n : ℕ, (⇑N)^[n] ω ∈ K := by
    intro n
    induction n with
    | zero => exact hω
    | succ n ih =>
      rw [Function.iterate_succ_apply']
      exact hgate _ ih
  have hball : ∀ n : ℕ, (⇑N)^[n] ω ∈ Metric.closedBall (0 : W 3) (Real.sqrt (ipW ω ω)) := by
    intro n
    have h := hDit n ω 0
    rw [Function.iterate_fixed (map_zero N) n, sub_zero, sub_zero] at h
    rw [Metric.mem_closedBall, dist_zero_right, ← h]
    exact norm_le_sqrt_ipW _
  obtain ⟨a, -, φ, hφ, hlim⟩ := tendsto_subseq_of_bounded Metric.isBounded_closedBall hball
  rw [← hcl.closure_eq, Metric.mem_closure_iff]
  intro ε hε
  obtain ⟨k0, hk0⟩ := Metric.cauchySeq_iff'.1 hlim.cauchySeq (ε / 4) (by linarith)
  have hd : dist ((⇑N)^[φ (k0 + 1)] ω) ((⇑N)^[φ k0] ω) < ε / 4 := by
    simpa using hk0 (k0 + 1) (Nat.le_succ k0)
  have hlt : φ k0 < φ (k0 + 1) := hφ (Nat.lt_succ_self k0)
  obtain ⟨m, hm⟩ : ∃ m, φ (k0 + 1) = φ k0 + (m + 1) := ⟨φ (k0 + 1) - φ k0 - 1, by omega⟩
  refine ⟨(⇑N)^[m] ω, hxK m, ?_⟩
  have hq : ipW (N.symm ω - (⇑N)^[m] ω) (N.symm ω - (⇑N)^[m] ω) =
      ipW ((⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω) ((⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω) := by
    rw [hm, Function.iterate_add_apply, hDit, Function.iterate_succ_apply', ← hD,
      N.apply_symm_apply]
  rw [dist_eq_norm]
  calc ‖N.symm ω - (⇑N)^[m] ω‖
      ≤ Real.sqrt (ipW (N.symm ω - (⇑N)^[m] ω) (N.symm ω - (⇑N)^[m] ω)) :=
        norm_le_sqrt_ipW _
    _ = Real.sqrt (ipW ((⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω)
          ((⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω)) := by rw [hq]
    _ ≤ Real.sqrt (16 * ‖(⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω‖ ^ 2) :=
        Real.sqrt_le_sqrt (ipW_self_le _)
    _ = 4 * ‖(⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω‖ := by
        rw [show (16 : ℝ) * ‖(⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω‖ ^ 2 =
            (4 * ‖(⇑N)^[φ k0] ω - (⇑N)^[φ (k0 + 1)] ω‖) ^ 2 by ring,
          Real.sqrt_sq (by positivity)]
    _ < ε := by
        rw [← dist_eq_norm, dist_comm]
        linarith

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.isClosed_dualW
#print axioms OIBridge.FourCopy.table_decomp
#print axioms OIBridge.FourCopy.clm_eq_ipW
#print axioms OIBridge.FourCopy.dualW_dualW
#print axioms OIBridge.FourCopy.bidual_of_adm
#print axioms OIBridge.FourCopy.norm_le_sqrt_ipW
#print axioms OIBridge.FourCopy.ipW_self_le
#print axioms OIBridge.FourCopy.inv_mem_of_orth
