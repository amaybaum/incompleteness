/-
  OIBridge/CmSprimeCompact.lean — design module of the research thread `research/countermodels`
  (round 5, node C22). Not adopted, not certified, not a round: a disposable dev branch.
  THEOREM S′ FOR COMPACT DEFECT FAMILIES (the thread's NOTES-C13 C13-S, stated with every hypothesis
  explicit), reduced to the finite form of `OIBridge/CmSprime.lean` (round 4, node C17) by finite-net
  approximation. `OIBridge/CmSprime.lean` is imported unchanged.

  SETTING (as in `CmSprime`). `n` a finite index type (`ℂⁿ`; the thread's case is `Fin 2 × Fin 2`);
  `pr A B = Re tr(A B)`; `Q` the positive semidefinite matrices; `defect c h = 1 − c · h h†`.
  A compact defect family is a continuous map `d : κ → Matrix n n ℂ` from a compact space `κ`
  (here `d k = defect (c k) (h k)` with `c : κ → ℝ`, `h : κ → n → ℂ` continuous).
    * `coneOf d = {Σ_{k ∈ s} t_k d_k : s a finset, t ≥ 0}` is the conic hull (finite combinations).
    * `surgeryC d = {q + z : q ⪰ 0, pr q (d k) ≥ 0 for every k, z ∈ closure (coneOf d)}` is the
      surgery cone with the CLOSED conic hull, `K(Z) = (Q ∩ Z*) + closed cone Z`.
      (That `coneOf d` is itself closed for a compact family — Carathéodory over a compact base not
      containing `0`, NOTES-C13 C13-S — is NOT stated here; it is the written remark that identifies
      `surgeryC d` with the thread's `K(Z) = (Q ∩ Z*) + cone Z`.)

  THE STATEMENTS.
    * `theorem_Sprime_compact` (§N) — for `[CompactSpace κ]`, `[Nonempty κ]`, `[Nonempty n]`,
      `Continuous c`, `Continuous h`, unit `h k`, `1 < c k ≤ 2`, `c k < card n`, pairwise
      nonnegative pairings `pr (d j) (d k) ≥ 0`, and (CC) in cap/co-cap form on every ordered pair
      `j ≠ k` of positive pairing: `surgeryC d = dualH (surgeryC d)` and `surgeryC d` is closed.
    * `theorem_Sprime_compact_ineq` (§N) — the same with (CC) in the inequality form
      `(√(c_j − 1) + √(c_k − 1))² ≤ c_j c_k |⟨h_j|h_k⟩|²` (through `CmSprime.cap_subset_cocap`).
    * `theorem_Sprime_compact_C4` (§N) — the `ℂ⁴` form, `c k < 4` automatic.
    * `surgeryC_subset_dualH` (§K) — `K ⊆ K*`: the four pairings, each carried to the closure of the
      conic hull by continuity (no compactness needed).
    * `dualH_subset_surgeryC_of_finite` (§M) — THE ENGINE, `K* ⊆ K`, for any continuous family on a
      compact space with Hermitian members, a uniform trace bound `τ ≤ tr (d k)`, a uniform entry
      bound, and the finite self-duality `surgery d_F = dualH (surgery d_F)` on EVERY finite
      subfamily `F` as a hypothesis (discharged by `CmSprime.theorem_Sprime` in §N). The new
      arguments over a compact base are exactly: (i) the pairing estimate `|pr q M| ≤ ε · card n · tr q`
      for `q ⪰ 0` and `M` with entries `≤ ε` (`abs_pr_le`, through the factorization `q = BB†` and
      Cauchy–Schwarz); (ii) for `y ∈ K*` and a finite ε-net `F` of the family, the shift `y + ηI`
      lies in the finite dual cone `(K_F)*` once `η ≥ ε · card n · tr(y)/τ`, so the finite theorem
      decomposes it (`hstep`); (iii) the limit along `ε → 0` in compact entry boxes (subsequences
      twice; PSD entries bounded by the trace, `norm_entry_le_pr_one`; conic-hull entries by
      `Md · tr z / τ`, `norm_entry_coneOf_le`), the PSD part closed (`isClosed_psd`), the dual
      conditions closed, the conic part landing in the closure. Not used: Farkas over a compact
      family, a least-weight decomposition over a compact family, a separation theorem,
      Carathéodory.
    * `surgery_subset_surgeryC` (§K) — the finite surgery of `CmSprime` lies in `surgeryC`
      (sanity: the two definitions agree on the finite-combination part).
    * `control_compact_single_defect` (§O) — non-vacuity: the compact family indexed by `Unit`
      with the single defect `1 − (3/2)|00⟩⟨00|` on `ℂ⁴` satisfies every hypothesis (the compact
      instance exercised exactly in the thread's preflight is the S2 circle of NOTES-C13, which is
      not formalized here: its (CC) over the whole circle is an exact identity in the parameter).

  Not claimed: closedness of `coneOf d` itself (Carathéodory); extremality of the defects; anything
  about OI's composite cone (this is cone geometry); kernel certification (design run only).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CmSprime
import Mathlib.Topology.Sequences
import Mathlib.Order.Filter.AtTopBot.Archimedean
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Algebra.Order.Chebyshev

namespace OIBridge
namespace CmSprime

open Matrix Filter Topology
open scoped ComplexOrder

noncomputable section

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ### §J — definitions: the conic hull and the surgery with the closed conic hull -/

/-- The conic hull of a family: finite nonnegative combinations `Σ_{k ∈ s} t_k d_k`. -/
def coneOf {κ : Type*} (d : κ → Matrix n n ℂ) : Set (Matrix n n ℂ) :=
  {z | ∃ (s : Finset κ) (t : s → ℝ), (∀ k, 0 ≤ t k) ∧ z = ∑ k, (t k : ℂ) • d (k : κ)}

/-- The surgery cone with the closed conic hull: `(Q ∩ Z*) + closure (cone Z)`. -/
def surgeryC {κ : Type*} (d : κ → Matrix n n ℂ) : Set (Matrix n n ℂ) :=
  {A | ∃ q z : Matrix n n ℂ, q.PosSemidef ∧ (∀ k, 0 ≤ pr q (d k)) ∧ z ∈ closure (coneOf d) ∧
    A = q + z}

/-- The entrywise box of radius `R`. -/
def box (R : ℝ) : Set (Matrix n n ℂ) :=
  Set.pi Set.univ fun _ : n => Set.pi Set.univ fun _ : n => Metric.closedBall (0 : ℂ) R

/-! ### §K — elementary facts: membership, Hermiticity, pairings, `K ⊆ K*` -/

theorem zero_mem_coneOf {κ : Type*} (d : κ → Matrix n n ℂ) : (0 : Matrix n n ℂ) ∈ coneOf d :=
  ⟨∅, fun _ => 0, fun _ => le_refl 0,
    (Finset.sum_eq_zero fun k _ => absurd k.2 (Finset.notMem_empty (k : κ))).symm⟩

theorem single_mem_coneOf {κ : Type*} [DecidableEq κ] (d : κ → Matrix n n ℂ) (k : κ) :
    d k ∈ coneOf d := by
  refine ⟨{k}, fun _ => 1, fun _ => zero_le_one, ?_⟩
  rw [Finset.sum_eq_single (⟨k, Finset.mem_singleton_self k⟩ : ({k} : Finset κ))
    (fun x _ hx => absurd (Subtype.ext (Finset.mem_singleton.mp x.2)) hx)
    (fun h => absurd (Finset.mem_univ _) h)]
  simp

theorem surgery_subset_surgeryC {ι : Type*} [Fintype ι] (d : ι → Matrix n n ℂ) :
    surgery d ⊆ surgeryC d := by
  intro A hA
  obtain ⟨q, t, hq, hqd, ht, rfl⟩ := hA
  exact ⟨q, _, hq, hqd, subset_closure ⟨Finset.univ, fun k => t k, fun k => ht k,
    (Finset.sum_coe_sort Finset.univ fun k => (t k : ℂ) • d k).symm⟩, rfl⟩

theorem coneOf_isHermitian {κ : Type*} (d : κ → Matrix n n ℂ) (hd : ∀ k, (d k).IsHermitian) :
    coneOf d ⊆ {M : Matrix n n ℂ | M.IsHermitian} := by
  rintro z ⟨s, t, _, rfl⟩
  exact isHermitian_sum_smul (fun k : s => d (k : κ)) (fun k => hd (k : κ)) t

theorem isClosed_isHermitian : IsClosed {M : Matrix n n ℂ | M.IsHermitian} := by
  show IsClosed {M : Matrix n n ℂ | Mᴴ = M}
  exact isClosed_eq continuous_id.matrix_conjTranspose continuous_id

theorem closure_coneOf_isHermitian {κ : Type*} (d : κ → Matrix n n ℂ)
    (hd : ∀ k, (d k).IsHermitian) {z : Matrix n n ℂ} (hz : z ∈ closure (coneOf d)) :
    z.IsHermitian :=
  closure_minimal (coneOf_isHermitian d hd) isClosed_isHermitian hz

theorem continuous_pr_left (B : Matrix n n ℂ) : Continuous fun A : Matrix n n ℂ => pr A B :=
  Complex.continuous_re.comp (continuous_id.matrix_mul continuous_const).matrix_trace

theorem continuous_pr_right (A : Matrix n n ℂ) : Continuous fun B : Matrix n n ℂ => pr A B :=
  Complex.continuous_re.comp (continuous_const.matrix_mul continuous_id).matrix_trace

theorem continuous_qf_matrix (x : n → ℂ) : Continuous fun M : Matrix n n ℂ => qf M x :=
  Complex.continuous_re.comp
    (continuous_const.dotProduct (continuous_id.matrix_mulVec continuous_const))

/-- The positive semidefinite matrices form a closed set. -/
theorem isClosed_psd : IsClosed {M : Matrix n n ℂ | M.PosSemidef} := by
  have h1 : {M : Matrix n n ℂ | M.PosSemidef} =
      {M : Matrix n n ℂ | M.IsHermitian} ∩ ⋂ x : n → ℂ, {M | 0 ≤ qf M x} := by
    ext M
    simp only [Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_iInter]
    constructor
    · intro hM
      exact ⟨hM.isHermitian, fun x => qf_nonneg_of_psd hM x⟩
    · rintro ⟨hH, hq⟩
      exact psd_of_qf hH hq
  rw [h1]
  exact isClosed_isHermitian.inter
    (isClosed_iInter fun x => isClosed_le continuous_const (continuous_qf_matrix x))

theorem pr_coneOf_nonneg {κ : Type*} (d : κ → Matrix n n ℂ) {q : Matrix n n ℂ}
    (hq : ∀ k, 0 ≤ pr q (d k)) {z : Matrix n n ℂ} (hz : z ∈ coneOf d) : 0 ≤ pr q z := by
  obtain ⟨s, t, ht, rfl⟩ := hz
  rw [pr_sum_right]
  refine Finset.sum_nonneg fun k _ => ?_
  rw [pr_smul_right]
  exact mul_nonneg (ht k) (hq (k : κ))

theorem pr_closure_coneOf_nonneg {κ : Type*} (d : κ → Matrix n n ℂ) {q : Matrix n n ℂ}
    (hq : ∀ k, 0 ≤ pr q (d k)) {z : Matrix n n ℂ} (hz : z ∈ closure (coneOf d)) : 0 ≤ pr q z :=
  closure_minimal (fun w hw => pr_coneOf_nonneg d hq hw)
    (isClosed_le continuous_const (continuous_pr_right q)) hz

theorem pr_coneOf_coneOf_nonneg {κ : Type*} (d : κ → Matrix n n ℂ)
    (hpair : ∀ j k, 0 ≤ pr (d j) (d k)) {z z' : Matrix n n ℂ} (hz : z ∈ coneOf d)
    (hz' : z' ∈ coneOf d) : 0 ≤ pr z' z := by
  obtain ⟨s, t, ht, rfl⟩ := hz
  obtain ⟨s', t', ht', rfl⟩ := hz'
  rw [pr_sum_left]
  refine Finset.sum_nonneg fun j _ => ?_
  rw [pr_smul_left, pr_sum_right]
  refine mul_nonneg (ht' j) (Finset.sum_nonneg fun k _ => ?_)
  rw [pr_smul_right]
  exact mul_nonneg (ht k) (hpair _ _)

theorem pr_closure_closure_nonneg {κ : Type*} (d : κ → Matrix n n ℂ)
    (hpair : ∀ j k, 0 ≤ pr (d j) (d k)) {z z' : Matrix n n ℂ} (hz : z ∈ closure (coneOf d))
    (hz' : z' ∈ closure (coneOf d)) : 0 ≤ pr z' z := by
  have step1 : ∀ w ∈ coneOf d, 0 ≤ pr w z := fun w hw =>
    closure_minimal (fun v hv => pr_coneOf_coneOf_nonneg d hpair hv hw)
      (isClosed_le continuous_const (continuous_pr_right w)) hz
  exact closure_minimal step1 (isClosed_le continuous_const (continuous_pr_left z)) hz'

theorem defect_mem_surgeryC {κ : Type*} [DecidableEq κ] (d : κ → Matrix n n ℂ) (k : κ) :
    d k ∈ surgeryC d :=
  ⟨0, d k, Matrix.PosSemidef.zero, fun j => le_of_eq (pr_zero_left (d j)).symm,
    subset_closure (single_mem_coneOf d k), (zero_add _).symm⟩

theorem one_mem_surgeryC {κ : Type*} (d : κ → Matrix n n ℂ) (h1 : ∀ k, 0 ≤ pr 1 (d k)) :
    (1 : Matrix n n ℂ) ∈ surgeryC d :=
  ⟨1, 0, Matrix.PosSemidef.one, h1, subset_closure (zero_mem_coneOf d), (add_zero _).symm⟩

/-- **`K ⊆ K*`** for the surgery with the closed conic hull: the four pairings, each carried to the
closure by continuity. -/
theorem surgeryC_subset_dualH {κ : Type*} (d : κ → Matrix n n ℂ) (hd : ∀ k, (d k).IsHermitian)
    (hpair : ∀ j k, 0 ≤ pr (d j) (d k)) : surgeryC d ⊆ dualH (surgeryC d) := by
  intro A hA
  obtain ⟨q, z, hq, hqd, hz, rfl⟩ := hA
  refine ⟨hq.isHermitian.add (closure_coneOf_isHermitian d hd hz), ?_⟩
  intro B hB
  obtain ⟨q', z', hq', hq'd, hz', rfl⟩ := hB
  rw [pr_add_left, pr_add_right, pr_add_right]
  have h1 : 0 ≤ pr q' q := pr_psd_psd hq' hq
  have h2 : 0 ≤ pr q' z := pr_closure_coneOf_nonneg d hq'd hz
  have h3 : 0 ≤ pr z' q := by
    rw [pr_comm]
    exact pr_closure_coneOf_nonneg d hqd hz'
  have h4 : 0 ≤ pr z' z := pr_closure_closure_nonneg d hpair hz hz'
  linarith

/-! ### §L — the quantitative estimates: entries and pairings -/

theorem pr_one_one : pr (1 : Matrix n n ℂ) 1 = Fintype.card n := by
  unfold pr
  rw [one_mul, Matrix.trace_one, Complex.natCast_re]

/-- `qf 1 v = Σ_a ‖v a‖²`. -/
theorem qf_one_eq_sum_sq (v : n → ℂ) : qf 1 v = ∑ a, ‖v a‖ ^ 2 := by
  unfold qf
  rw [Matrix.one_mulVec]
  simp only [dotProduct, Pi.star_apply, Complex.re_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [star_mul_self_eq, Complex.ofReal_re, Complex.normSq_eq_norm_sq]

/-- For `q = B Bᴴ`, `tr q = Σ_m Σ_a ‖B a m‖²`. -/
theorem pr_one_eq_sum_sq (B : Matrix n n ℂ) : pr (B * Bᴴ) 1 = ∑ m, ∑ a, ‖B a m‖ ^ 2 := by
  rw [pr_mul_conjTranspose]
  exact Finset.sum_congr rfl fun m _ => qf_one_eq_sum_sq _

/-- **Entries of a positive semidefinite matrix are bounded by its trace.** -/
theorem norm_entry_le_pr_one {q : Matrix n n ℂ} (hq : q.PosSemidef) (i j : n) :
    ‖q i j‖ ≤ pr q 1 := by
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged n q hq
  have hij : q i j = ∑ m, B i m * star (B j m) := by
    rw [hB]
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply]
  have htr : pr q 1 = ∑ m, ∑ a, ‖B a m‖ ^ 2 := by
    rw [hB, pr_one_eq_sum_sq]
  have hterm : ∀ m, ‖B i m‖ * ‖B j m‖ ≤ ∑ a, ‖B a m‖ ^ 2 := by
    intro m
    have h1 : ‖B i m‖ ^ 2 ≤ ∑ a, ‖B a m‖ ^ 2 :=
      Finset.single_le_sum (f := fun a => ‖B a m‖ ^ 2) (fun a _ => sq_nonneg _)
        (Finset.mem_univ i)
    have h2 : ‖B j m‖ ^ 2 ≤ ∑ a, ‖B a m‖ ^ 2 :=
      Finset.single_le_sum (f := fun a => ‖B a m‖ ^ 2) (fun a _ => sq_nonneg _)
        (Finset.mem_univ j)
    have h3 := two_mul_le_add_sq ‖B i m‖ ‖B j m‖
    linarith
  rw [hij, htr]
  calc ‖∑ m, B i m * star (B j m)‖ ≤ ∑ m, ‖B i m * star (B j m)‖ := norm_sum_le _ _
    _ = ∑ m, ‖B i m‖ * ‖B j m‖ := by simp only [norm_mul, norm_star]
    _ ≤ ∑ m, ∑ a, ‖B a m‖ ^ 2 := Finset.sum_le_sum fun m _ => hterm m

/-- `|qf M v| ≤ ε · card n · Σ_a ‖v a‖²` when every entry of `M` has norm at most `ε`. -/
theorem abs_qf_le {M : Matrix n n ℂ} {ε : ℝ} (hε : 0 ≤ ε) (hM : ∀ i j, ‖M i j‖ ≤ ε)
    (v : n → ℂ) : |qf M v| ≤ ε * Fintype.card n * ∑ a, ‖v a‖ ^ 2 := by
  have h1 : ‖star v ⬝ᵥ (M *ᵥ v)‖ ≤ ∑ a, ‖v a‖ * ∑ b, ε * ‖v b‖ := by
    have hrow : ∀ a, ‖∑ b, M a b * v b‖ ≤ ∑ b, ε * ‖v b‖ := fun a =>
      calc ‖∑ b, M a b * v b‖ ≤ ∑ b, ‖M a b * v b‖ := norm_sum_le _ _
        _ ≤ ∑ b, ε * ‖v b‖ := Finset.sum_le_sum fun b _ => by
            rw [norm_mul]
            exact mul_le_mul_of_nonneg_right (hM a b) (norm_nonneg _)
    calc ‖star v ⬝ᵥ (M *ᵥ v)‖ = ‖∑ a, star (v a) * ∑ b, M a b * v b‖ := by
          simp only [dotProduct, Matrix.mulVec, Pi.star_apply]
      _ ≤ ∑ a, ‖star (v a) * ∑ b, M a b * v b‖ := norm_sum_le _ _
      _ ≤ ∑ a, ‖v a‖ * ∑ b, ε * ‖v b‖ := Finset.sum_le_sum fun a _ => by
          rw [norm_mul, norm_star]
          exact mul_le_mul_of_nonneg_left (hrow a) (norm_nonneg _)
  have hS : ∑ a, ‖v a‖ * ∑ b, ε * ‖v b‖ = ε * (∑ a, ‖v a‖) ^ 2 := by
    rw [← Finset.mul_sum, ← Finset.sum_mul]
    ring
  have hCS : (∑ a, ‖v a‖) ^ 2 ≤ Fintype.card n * ∑ a, ‖v a‖ ^ 2 := by
    have h := sq_sum_le_card_mul_sum_sq (s := (Finset.univ : Finset n)) (f := fun a => ‖v a‖)
    rwa [Finset.card_univ] at h
  calc |qf M v| = |(star v ⬝ᵥ (M *ᵥ v)).re| := rfl
    _ ≤ ‖star v ⬝ᵥ (M *ᵥ v)‖ := Complex.abs_re_le_norm _
    _ ≤ ∑ a, ‖v a‖ * ∑ b, ε * ‖v b‖ := h1
    _ = ε * (∑ a, ‖v a‖) ^ 2 := hS
    _ ≤ ε * (Fintype.card n * ∑ a, ‖v a‖ ^ 2) := mul_le_mul_of_nonneg_left hCS hε
    _ = ε * Fintype.card n * ∑ a, ‖v a‖ ^ 2 := by ring

/-- **The pairing estimate.** For `q ⪰ 0` and `M` with entries of norm at most `ε`,
`|pr q M| ≤ ε · card n · tr q`. -/
theorem abs_pr_le {q : Matrix n n ℂ} (hq : q.PosSemidef) {M : Matrix n n ℂ} {ε : ℝ} (hε : 0 ≤ ε)
    (hM : ∀ i j, ‖M i j‖ ≤ ε) : |pr q M| ≤ ε * Fintype.card n * pr q 1 := by
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged n q hq
  have hcol : pr q M = ∑ m, qf M (fun i => B i m) := by
    rw [hB, pr_mul_conjTranspose]
  have htr : pr q 1 = ∑ m, ∑ a, ‖B a m‖ ^ 2 := by
    rw [hB, pr_one_eq_sum_sq]
  rw [hcol, htr]
  calc |∑ m, qf M (fun i => B i m)| ≤ ∑ m, |qf M (fun i => B i m)| :=
        Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ m, ε * Fintype.card n * ∑ a, ‖B a m‖ ^ 2 :=
        Finset.sum_le_sum fun m _ => abs_qf_le hε hM _
    _ = ε * Fintype.card n * ∑ m, ∑ a, ‖B a m‖ ^ 2 := (Finset.mul_sum _ _ _).symm

/-- Entries of a rank-one defect with a unit seed are bounded by `1 + c`. -/
theorem norm_entry_defect_le {c : ℝ} {h : n → ℂ} (hh : ip h h = 1) (hc : 0 ≤ c) (i j : n) :
    ‖defect c h i j‖ ≤ 1 + c := by
  have hsum : ∑ a, ‖h a‖ ^ 2 = 1 := by
    have h1 : (ip h h).re = ∑ a, ‖h a‖ ^ 2 := by
      unfold ip
      simp only [dotProduct, Pi.star_apply, Complex.re_sum]
      refine Finset.sum_congr rfl fun a _ => ?_
      rw [star_mul_self_eq, Complex.ofReal_re, Complex.normSq_eq_norm_sq]
    rw [← h1, hh, Complex.one_re]
  have hbound : ∀ a, ‖h a‖ ≤ 1 := fun a => by
    have h2 : ‖h a‖ ^ 2 ≤ 1 := by
      rw [← hsum]
      exact Finset.single_le_sum (f := fun a => ‖h a‖ ^ 2) (fun b _ => sq_nonneg _)
        (Finset.mem_univ a)
    exact le_of_pow_le_pow_left₀ two_ne_zero zero_le_one (by rw [one_pow]; exact h2)
  have hd : defect c h i j = (1 : Matrix n n ℂ) i j - (c : ℂ) * (h i * star (h j)) := by
    simp [defect, Matrix.sub_apply, Matrix.smul_apply, Matrix.vecMulVec_apply, smul_eq_mul]
  rw [hd]
  have h1 : ‖(1 : Matrix n n ℂ) i j‖ ≤ 1 := by
    rw [Matrix.one_apply]
    split_ifs <;> simp
  have h2 : ‖(c : ℂ) * (h i * star (h j))‖ ≤ c := by
    rw [norm_mul, norm_mul, norm_star, Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg hc]
    calc c * (‖h i‖ * ‖h j‖) ≤ c * (1 * 1) :=
          mul_le_mul_of_nonneg_left
            (mul_le_mul (hbound i) (hbound j) (norm_nonneg _) zero_le_one) hc
      _ = c := by ring
  calc ‖(1 : Matrix n n ℂ) i j - (c : ℂ) * (h i * star (h j))‖
      ≤ ‖(1 : Matrix n n ℂ) i j‖ + ‖(c : ℂ) * (h i * star (h j))‖ := norm_sub_le _ _
    _ ≤ 1 + c := add_le_add h1 h2

/-- Entries of a finite nonnegative combination: `‖z i j‖ · τ ≤ Md · tr z` when every
`‖d k i j‖ ≤ Md` and every `tr (d k) ≥ τ`. -/
theorem norm_entry_coneOf_le {κ : Type*} (d : κ → Matrix n n ℂ) {τ Md : ℝ} (hτ0 : 0 < τ)
    (hτ : ∀ k, τ ≤ pr 1 (d k)) (hMd0 : 0 ≤ Md) (hMd : ∀ k i j, ‖d k i j‖ ≤ Md)
    {z : Matrix n n ℂ} (hz : z ∈ coneOf d) (i j : n) : ‖z i j‖ * τ ≤ Md * pr 1 z := by
  obtain ⟨s, t, ht, rfl⟩ := hz
  have h1 : ‖(∑ k : s, (t k : ℂ) • d (k : κ)) i j‖ ≤ Md * ∑ k : s, t k := by
    rw [Matrix.sum_apply]
    calc ‖∑ k : s, ((t k : ℂ) • d (k : κ)) i j‖ ≤ ∑ k : s, ‖((t k : ℂ) • d (k : κ)) i j‖ :=
          norm_sum_le _ _
      _ ≤ ∑ k : s, t k * Md := Finset.sum_le_sum fun k _ => by
          rw [Matrix.smul_apply, norm_smul, Complex.norm_real, Real.norm_eq_abs,
            abs_of_nonneg (ht k)]
          exact mul_le_mul_of_nonneg_left (hMd (k : κ) i j) (ht k)
      _ = Md * ∑ k : s, t k := by
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun k _ => mul_comm _ _
  have h2 : τ * ∑ k : s, t k ≤ pr 1 (∑ k : s, (t k : ℂ) • d (k : κ)) := by
    rw [pr_sum_right, Finset.mul_sum]
    refine Finset.sum_le_sum fun k _ => ?_
    rw [pr_smul_right, mul_comm]
    exact mul_le_mul_of_nonneg_left (hτ (k : κ)) (ht k)
  calc ‖(∑ k : s, (t k : ℂ) • d (k : κ)) i j‖ * τ ≤ (Md * ∑ k : s, t k) * τ :=
        mul_le_mul_of_nonneg_right h1 hτ0.le
    _ = Md * (τ * ∑ k : s, t k) := by ring
    _ ≤ Md * pr 1 (∑ k : s, (t k : ℂ) • d (k : κ)) := mul_le_mul_of_nonneg_left h2 hMd0

/-! ### §M — compactness: finite nets, boxes, and the engine `K* ⊆ K` -/

/-- **Finite ε-nets** of a continuous family on a compact space (entrywise). -/
theorem exists_net {κ : Type*} [TopologicalSpace κ] [CompactSpace κ] (d : κ → Matrix n n ℂ)
    (hd : Continuous d) {ε : ℝ} (hε : 0 < ε) :
    ∃ F : Finset κ, ∀ k, ∃ k' ∈ F, ∀ i j, ‖d k i j - d k' i j‖ < ε := by
  have hcont : ∀ (k' : κ) (i j : n), Continuous fun k => ‖d k i j - d k' i j‖ :=
    fun k' i j => ((hd.matrix_elem i j).sub continuous_const).norm
  obtain ⟨F, hF⟩ := isCompact_univ.elim_finite_subcover
    (fun k' : κ => ⋂ i, ⋂ j, {k | ‖d k i j - d k' i j‖ < ε})
    (fun k' => isOpen_iInter_of_finite fun i => isOpen_iInter_of_finite fun j =>
      isOpen_lt (hcont k' i j) continuous_const)
    (fun k _ => Set.mem_iUnion.mpr ⟨k, Set.mem_iInter.mpr fun i => Set.mem_iInter.mpr fun j => by
      simp [hε]⟩)
  refine ⟨F, fun k => ?_⟩
  have hk := hF (Set.mem_univ k)
  rw [Set.mem_iUnion₂] at hk
  obtain ⟨k', hk'F, hk'⟩ := hk
  exact ⟨k', hk'F, fun i j => Set.mem_iInter.mp (Set.mem_iInter.mp hk' i) j⟩

theorem isCompact_box (R : ℝ) : IsCompact (box (n := n) R) :=
  isCompact_univ_pi fun _ => isCompact_univ_pi fun _ => isCompact_closedBall 0 R

theorem mem_box {R : ℝ} {M : Matrix n n ℂ} : M ∈ box R ↔ ∀ i j, ‖M i j‖ ≤ R := by
  simp only [box, Set.mem_univ_pi, Metric.mem_closedBall, dist_zero_right]

instance instFirstCountableTopologyMatrix : FirstCountableTopology (Matrix n n ℂ) :=
  inferInstanceAs (FirstCountableTopology (n → n → ℂ))

set_option maxHeartbeats 1600000 in
/-- **The engine: `K* ⊆ K` for a compact family**, from the finite self-duality of every finite
subfamily. For `y ∈ K*`, a finite `ε`-net `F` and the shift `y + ηI` with `η = ε · card n · tr(y)/τ`:
`y + ηI ∈ (K_F)* = K_F` by the pairing estimate, so `y + ηI = q_F + z_F`; along `ε → 0` the parts
stay in compact entry boxes, subsequences converge, and the limit decomposes `y`. -/
theorem dualH_subset_surgeryC_of_finite {κ : Type*} [TopologicalSpace κ] [CompactSpace κ]
    [Nonempty n] (d : κ → Matrix n n ℂ) (hd : ∀ k, (d k).IsHermitian) (hdc : Continuous d)
    {τ : ℝ} (hτ0 : 0 < τ) (hτ : ∀ k, τ ≤ pr 1 (d k))
    {Md : ℝ} (hMd0 : 0 ≤ Md) (hMd : ∀ k i j, ‖d k i j‖ ≤ Md)
    (hfin : ∀ F : Finset κ, surgery (fun k : F => d (k : κ)) =
      dualH (surgery (fun k : F => d (k : κ)))) :
    dualH (surgeryC d) ⊆ surgeryC d := by
  classical
  intro y hy
  obtain ⟨hyH, hyK⟩ := hy
  have hd0 : ∀ k, 0 ≤ pr 1 (d k) := fun k => le_trans hτ0.le (hτ k)
  have hyd : ∀ k, 0 ≤ pr (d k) y := fun k => hyK (d k) (defect_mem_surgeryC d k)
  have hy1 : 0 ≤ pr 1 y := hyK 1 (one_mem_surgeryC d hd0)
  have hcard : (0 : ℝ) < Fintype.card n := Nat.cast_pos.mpr Fintype.card_pos
  -- the sequences `η m → 0` and `ε m → 0`
  obtain ⟨η, hη⟩ : ∃ η : ℕ → ℝ, ∀ m, η m = ((m + 1 : ℕ) : ℝ)⁻¹ :=
    ⟨fun m => ((m + 1 : ℕ) : ℝ)⁻¹, fun _ => rfl⟩
  have hη_pos : ∀ m, 0 < η m := fun m => by
    rw [hη m]
    exact inv_pos.mpr (Nat.cast_pos.mpr (Nat.succ_pos m))
  have hη_le : ∀ m, η m ≤ 1 := fun m => by
    rw [hη m]
    exact inv_le_one_of_one_le₀ (Nat.one_le_cast.mpr (Nat.succ_le_succ (Nat.zero_le m)))
  have hη_lim : Tendsto η atTop (𝓝 0) := by
    rw [funext hη]
    exact ((tendsto_natCast_atTop_atTop (R := ℝ)).comp (tendsto_add_atTop_nat 1)).inv_tendsto_atTop
  obtain ⟨K, hK_def⟩ : ∃ K : ℝ, K = Fintype.card n * (pr 1 y + 1) := ⟨_, rfl⟩
  have hK : 0 < K := by
    rw [hK_def]
    exact mul_pos hcard (by linarith)
  obtain ⟨ε, hε⟩ : ∃ ε : ℕ → ℝ, ∀ m, ε m = η m * τ / K := ⟨fun m => η m * τ / K, fun _ => rfl⟩
  have hε_pos : ∀ m, 0 < ε m := fun m => by
    rw [hε m]
    exact div_pos (mul_pos (hη_pos m) hτ0) hK
  have hε_le : ∀ m, ε m * Fintype.card n * pr 1 y / τ ≤ η m := fun m => by
    have e : ε m * Fintype.card n * pr 1 y = η m * τ * (Fintype.card n * pr 1 y) / K := by
      rw [hε m]
      ring
    rw [e, div_div, div_le_iff₀ (mul_pos hK hτ0), hK_def]
    have h1 : 0 ≤ η m * τ := (mul_pos (hη_pos m) hτ0).le
    have h2 : (Fintype.card n : ℝ) * pr 1 y ≤ Fintype.card n * (pr 1 y + 1) :=
      mul_le_mul_of_nonneg_left (by linarith) hcard.le
    calc η m * τ * (Fintype.card n * pr 1 y) ≤ η m * τ * (Fintype.card n * (pr 1 y + 1)) :=
          mul_le_mul_of_nonneg_left h2 h1
      _ = η m * (Fintype.card n * (pr 1 y + 1) * τ) := by ring
  obtain ⟨R, hR_def⟩ : ∃ R : ℝ, R = pr 1 y + Fintype.card n := ⟨_, rfl⟩
  -- the key estimate on an ε-net
  have key : ∀ (e : ℝ), 0 < e → ∀ F : Finset κ,
      (∀ k, ∃ k' ∈ F, ∀ i j, ‖d k i j - d k' i j‖ < e) →
      ∀ q : Matrix n n ℂ, q.PosSemidef → (∀ k' ∈ F, 0 ≤ pr q (d k')) →
      ∀ k, -(e * Fintype.card n * pr q 1) ≤ pr q (d k) := by
    intro e he F hF q hq hqF k
    obtain ⟨k', hk'F, hk'⟩ := hF k
    have h1 : |pr q (d k - d k')| ≤ e * Fintype.card n * pr q 1 :=
      abs_pr_le hq he.le fun i j => by
        rw [Matrix.sub_apply]
        exact (hk' i j).le
    have h2 : pr q (d k) = pr q (d k') + pr q (d k - d k') := by
      rw [← pr_add_right]
      congr 1
      abel
    have h3 := hqF k' hk'F
    have h4 := (abs_le.mp h1).1
    linarith
  -- the shifted PSD member of `K`
  have shift_mem : ∀ (e : ℝ), 0 < e → ∀ F : Finset κ,
      (∀ k, ∃ k' ∈ F, ∀ i j, ‖d k i j - d k' i j‖ < e) →
      ∀ q : Matrix n n ℂ, q.PosSemidef → (∀ k' ∈ F, 0 ≤ pr q (d k')) →
      q + ((e * Fintype.card n * pr q 1 / τ : ℝ) : ℂ) • (1 : Matrix n n ℂ) ∈ surgeryC d := by
    intro e he F hF q hq hqF
    have hq1 : 0 ≤ pr q 1 := pr_psd_psd hq Matrix.PosSemidef.one
    have hδ : 0 ≤ e * Fintype.card n * pr q 1 / τ :=
      div_nonneg (mul_nonneg (mul_nonneg he.le hcard.le) hq1) hτ0.le
    refine ⟨q + ((e * Fintype.card n * pr q 1 / τ : ℝ) : ℂ) • (1 : Matrix n n ℂ), 0,
      hq.add (Matrix.PosSemidef.one.smul (Complex.zero_le_real.mpr hδ)), fun k => ?_,
      subset_closure (zero_mem_coneOf d), (add_zero _).symm⟩
    rw [pr_add_left, pr_smul_left]
    have h1 := key e he F hF q hq hqF k
    have h2 := hτ k
    have h3 : 0 ≤ e * Fintype.card n * pr q 1 := mul_nonneg (mul_nonneg he.le hcard.le) hq1
    have h4 : e * Fintype.card n * pr q 1 ≤ e * Fintype.card n * pr q 1 / τ * pr 1 (d k) := by
      rw [div_mul_eq_mul_div, le_div_iff₀ hτ0]
      exact mul_le_mul_of_nonneg_left h2 h3
    linarith
  -- one step: the finite decomposition of `y + η m · 1` with its bounds
  have hstep : ∀ m : ℕ, ∃ q z : Matrix n n ℂ, q.PosSemidef ∧
      (∀ k, -(ε m * Fintype.card n * R) ≤ pr q (d k)) ∧ z ∈ coneOf d ∧
      y + ((η m : ℝ) : ℂ) • (1 : Matrix n n ℂ) = q + z ∧
      (∀ i j, ‖q i j‖ ≤ R) ∧ (∀ i j, ‖z i j‖ ≤ Md * R / τ) := by
    intro m
    obtain ⟨F, hF⟩ := exists_net d hdc (hε_pos m)
    have hmem : y + ((η m : ℝ) : ℂ) • (1 : Matrix n n ℂ) ∈
        dualH (surgery fun k : F => d (k : κ)) := by
      refine ⟨hyH.add (Matrix.isHermitian_one.smul (isSelfAdjoint_ofReal _)), ?_⟩
      intro X hX
      obtain ⟨q, t, hq, hqd, ht, rfl⟩ := hX
      show 0 ≤ pr (q + ∑ k : F, (t k : ℂ) • d (k : κ)) (y + ((η m : ℝ) : ℂ) • (1 : Matrix n n ℂ))
      have e1 : pr (q + ∑ k : F, (t k : ℂ) • d (k : κ)) (y + ((η m : ℝ) : ℂ) • (1 : Matrix n n ℂ))
          = (pr q y + η m * pr q 1) + ∑ k : F, t k * (pr (d (k : κ)) y + η m * pr (d (k : κ)) 1) := by
        rw [pr_add_left, pr_add_right, pr_smul_right, pr_sum_left]
        congr 1
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [pr_smul_left, pr_add_right, pr_smul_right]
      rw [e1]
      have hqF : ∀ k' ∈ F, 0 ≤ pr q (d k') := fun k' hk' => hqd ⟨k', hk'⟩
      have hs := hyK _ (shift_mem (ε m) (hε_pos m) F hF q hq hqF)
      rw [pr_add_left, pr_smul_left] at hs
      have hq1 : 0 ≤ pr q 1 := pr_psd_psd hq Matrix.PosSemidef.one
      have hδy : ε m * Fintype.card n * pr q 1 / τ * pr 1 y ≤ η m * pr q 1 := by
        have e2 : ε m * Fintype.card n * pr q 1 / τ * pr 1 y =
            pr q 1 * (ε m * Fintype.card n * pr 1 y / τ) := by ring
        rw [e2, mul_comm (η m) (pr q 1)]
        exact mul_le_mul_of_nonneg_left (hε_le m) hq1
      have hA : 0 ≤ pr q y + η m * pr q 1 := by linarith
      have hB : 0 ≤ ∑ k : F, t k * (pr (d (k : κ)) y + η m * pr (d (k : κ)) 1) :=
        Finset.sum_nonneg fun k _ => mul_nonneg (ht k)
          (add_nonneg (hyd (k : κ)) (mul_nonneg (hη_pos m).le (by
            rw [pr_comm]
            exact hd0 (k : κ))))
      linarith
    rw [← hfin F] at hmem
    obtain ⟨q, t, hq, hqd, ht, hyeq⟩ := hmem
    have hqF : ∀ k' ∈ F, 0 ≤ pr q (d k') := fun k' hk' => hqd ⟨k', hk'⟩
    have hzc : (∑ k : F, (t k : ℂ) • d (k : κ)) ∈ coneOf d := ⟨F, t, ht, rfl⟩
    have hz0 : 0 ≤ pr 1 (∑ k : F, (t k : ℂ) • d (k : κ)) := pr_coneOf_nonneg d hd0 hzc
    have hq1 : 0 ≤ pr 1 q := pr_psd_psd Matrix.PosSemidef.one hq
    have htr : pr 1 y + η m * Fintype.card n = pr 1 q + pr 1 (∑ k : F, (t k : ℂ) • d (k : κ)) := by
      have h := congrArg (pr (1 : Matrix n n ℂ)) hyeq
      rw [pr_add_right, pr_smul_right, pr_one_one, pr_add_right] at h
      exact h
    have hηc : η m * Fintype.card n ≤ Fintype.card n := mul_le_of_le_one_left hcard.le (hη_le m)
    have hqR : pr 1 q ≤ R := by
      rw [hR_def]
      linarith
    have hzR : pr 1 (∑ k : F, (t k : ℂ) • d (k : κ)) ≤ R := by
      rw [hR_def]
      linarith
    refine ⟨q, ∑ k : F, (t k : ℂ) • d (k : κ), hq, fun k => ?_, hzc, hyeq, fun i j => ?_,
      fun i j => ?_⟩
    · have h1 := key (ε m) (hε_pos m) F hF q hq hqF k
      have h2 : ε m * Fintype.card n * pr q 1 ≤ ε m * Fintype.card n * R :=
        mul_le_mul_of_nonneg_left (by rw [pr_comm]; exact hqR)
          (mul_nonneg (hε_pos m).le hcard.le)
      linarith
    · exact le_trans (norm_entry_le_pr_one hq i j) (by rw [pr_comm]; exact hqR)
    · rw [le_div_iff₀ hτ0]
      exact le_trans (norm_entry_coneOf_le d hτ0 hτ hMd0 hMd hzc i j)
        (mul_le_mul_of_nonneg_left hzR hMd0)
  choose q z hq hqk hz hyeq hqB hzB using hstep
  -- subsequences in the compact boxes
  obtain ⟨q∞, -, φ₁, hφ₁, hq∞⟩ :=
    (isCompact_box (n := n) R).tendsto_subseq fun m => mem_box.mpr (hqB m)
  obtain ⟨z∞, -, φ₂, hφ₂, hz∞⟩ :=
    (isCompact_box (n := n) (Md * R / τ)).tendsto_subseq fun m => mem_box.mpr (hzB (φ₁ m))
  have hψ : Tendsto (fun m => φ₁ (φ₂ m)) atTop atTop := (hφ₁.comp hφ₂).tendsto_atTop
  have hq∞' : Tendsto (fun m => q (φ₁ (φ₂ m))) atTop (𝓝 q∞) := hq∞.comp hφ₂.tendsto_atTop
  have hz∞' : Tendsto (fun m => z (φ₁ (φ₂ m))) atTop (𝓝 z∞) := hz∞
  have hηψ : Tendsto (fun m => η (φ₁ (φ₂ m))) atTop (𝓝 0) := hη_lim.comp hψ
  have hεψ : Tendsto (fun m => ε (φ₁ (φ₂ m))) atTop (𝓝 0) := by
    have h := (hηψ.mul_const τ).div_const K
    rw [zero_mul, zero_div] at h
    have hfun : (fun m => ε (φ₁ (φ₂ m))) = fun m => η (φ₁ (φ₂ m)) * τ / K :=
      funext fun m => hε _
    rw [hfun]
    exact h
  -- the two limits of one sequence: `y = q∞ + z∞`
  have hlim1 : Tendsto (fun m => y + ((η (φ₁ (φ₂ m)) : ℝ) : ℂ) • (1 : Matrix n n ℂ)) atTop
      (𝓝 (q∞ + z∞)) :=
    (hq∞'.add hz∞').congr fun m => (hyeq (φ₁ (φ₂ m))).symm
  have hlim2 : Tendsto (fun m => y + ((η (φ₁ (φ₂ m)) : ℝ) : ℂ) • (1 : Matrix n n ℂ)) atTop
      (𝓝 y) := by
    have h0 : Tendsto (fun m => ((η (φ₁ (φ₂ m)) : ℝ) : ℂ)) atTop (𝓝 ((0 : ℝ) : ℂ)) :=
      (Complex.continuous_ofReal.tendsto 0).comp hηψ
    rw [Complex.ofReal_zero] at h0
    have h1 : Tendsto (fun m => y + ((η (φ₁ (φ₂ m)) : ℝ) : ℂ) • (1 : Matrix n n ℂ)) atTop
        (𝓝 (y + (0 : ℂ) • (1 : Matrix n n ℂ))) :=
      tendsto_const_nhds.add (h0.smul_const (1 : Matrix n n ℂ))
    rwa [zero_smul, add_zero] at h1
  have heq : q∞ + z∞ = y := tendsto_nhds_unique hlim1 hlim2
  refine ⟨q∞, z∞, ?_, ?_, ?_, heq.symm⟩
  · exact isClosed_psd.mem_of_tendsto hq∞' (Eventually.of_forall fun m => hq _)
  · intro k
    have hneg : Tendsto (fun m => -(ε (φ₁ (φ₂ m)) * Fintype.card n * R)) atTop (𝓝 0) := by
      have h := ((hεψ.mul_const (Fintype.card n : ℝ)).mul_const R).neg
      rwa [zero_mul, zero_mul, neg_zero] at h
    have hpr : Tendsto (fun m => pr (q (φ₁ (φ₂ m))) (d k)) atTop (𝓝 (pr q∞ (d k))) :=
      ((continuous_pr_left (d k)).tendsto q∞).comp hq∞'
    exact le_of_tendsto_of_tendsto' hneg hpr fun m => hqk _ k
  · exact mem_closure_of_tendsto hz∞' (Eventually.of_forall fun m => hz _)

/-! ### §N — Theorem S′ for compact defect families -/

/-- Continuity of the defect family from the continuity of `c` and of the seed map. -/
theorem continuous_defect_family {κ : Type*} [TopologicalSpace κ] {c : κ → ℝ} {h : κ → n → ℂ}
    (hc : Continuous c) (hh : Continuous h) : Continuous fun k => defect (c k) (h k) := by
  show Continuous fun k => (1 : Matrix n n ℂ) - (c k : ℂ) • Matrix.vecMulVec (h k) (star (h k))
  exact continuous_const.sub
    ((Complex.continuous_ofReal.comp hc).smul (hh.matrix_vecMulVec hh.star))

set_option maxHeartbeats 800000 in
/-- **Theorem S′ for a compact defect family.** Every hypothesis explicit: `κ` compact and
nonempty, `n` nonempty, `c` and the seed map continuous, unit seeds, `1 < c k ≤ 2`, `c k < card n`,
pairwise nonnegative pairings, (CC) in cap/co-cap form on every ordered pair `j ≠ k` of positive
pairing. Conclusion: the surgery with the closed conic hull is self-dual and closed. -/
theorem theorem_Sprime_compact {κ : Type*} [TopologicalSpace κ] [CompactSpace κ] [Nonempty κ]
    [DecidableEq κ] [Nonempty n] (c : κ → ℝ) (h : κ → n → ℂ)
    (hc_cont : Continuous c) (hh_cont : Continuous h)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hcard : ∀ k, c k < Fintype.card n)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      ∀ v : n → ℂ, (star v ⬝ᵥ v).re < c j * Complex.normSq (star (h j) ⬝ᵥ v) →
        (c k - 1) * (star v ⬝ᵥ v).re < c k * Complex.normSq (star (h k) ⬝ᵥ v)) :
    surgeryC (fun k => defect (c k) (h k)) = dualH (surgeryC (fun k => defect (c k) (h k))) ∧
      IsClosed (surgeryC (fun k => defect (c k) (h k))) := by
  have hd : ∀ k, (defect (c k) (h k)).IsHermitian := fun k => defect_isHermitian _ _
  have hdc : Continuous fun k => defect (c k) (h k) := continuous_defect_family hc_cont hh_cont
  obtain ⟨k₀, -, hk₀⟩ := isCompact_univ.exists_isMaxOn Set.univ_nonempty hc_cont.continuousOn
  have hτ0 : 0 < (Fintype.card n : ℝ) - c k₀ := by linarith [hcard k₀]
  have hτ : ∀ k, (Fintype.card n : ℝ) - c k₀ ≤ pr 1 (defect (c k) (h k)) := fun k => by
    rw [pr_one_defect _ _ (hunit k)]
    linarith [(isMaxOn_iff.mp hk₀) k (Set.mem_univ k)]
  have hMd : ∀ k i j, ‖defect (c k) (h k) i j‖ ≤ 3 := fun k i j =>
    le_trans (norm_entry_defect_le (hunit k) (by linarith [(hc k).1]) i j)
      (by linarith [(hc k).2])
  have hfin : ∀ F : Finset κ, surgery (fun k : F => defect (c (k : κ)) (h (k : κ))) =
      dualH (surgery (fun k : F => defect (c (k : κ)) (h (k : κ)))) := fun F =>
    (theorem_Sprime (fun k : F => c (k : κ)) (fun k : F => h (k : κ)) (fun k => hunit (k : κ))
      (fun k => hc (k : κ)) (fun k => hcard (k : κ)) (fun j k => hpair (j : κ) (k : κ))
      (fun j k hjk => hCC (j : κ) (k : κ) (fun e => hjk (Subtype.ext e)))).1
  have hK : surgeryC (fun k => defect (c k) (h k)) =
      dualH (surgeryC (fun k => defect (c k) (h k))) :=
    Set.Subset.antisymm (surgeryC_subset_dualH _ hd hpair)
      (dualH_subset_surgeryC_of_finite _ hd hdc hτ0 hτ (by norm_num : (0 : ℝ) ≤ 3) hMd hfin)
  refine ⟨hK, ?_⟩
  rw [hK]
  exact isClosed_dualH _

/-- **Theorem S′ for a compact family with (CC) in inequality form.** -/
theorem theorem_Sprime_compact_ineq {κ : Type*} [TopologicalSpace κ] [CompactSpace κ]
    [Nonempty κ] [DecidableEq κ] [Nonempty n] (c : κ → ℝ) (h : κ → n → ℂ)
    (hc_cont : Continuous c) (hh_cont : Continuous h)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hcard : ∀ k, c k < Fintype.card n)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      (Real.sqrt (c j - 1) + Real.sqrt (c k - 1)) ^ 2 ≤
        c j * c k * Complex.normSq (star (h j) ⬝ᵥ h k)) :
    surgeryC (fun k => defect (c k) (h k)) = dualH (surgeryC (fun k => defect (c k) (h k))) ∧
      IsClosed (surgeryC (fun k => defect (c k) (h k))) :=
  theorem_Sprime_compact c h hc_cont hh_cont hunit hc hcard hpair fun j k hjk hp v hv =>
    cap_subset_cocap (hunit j) (hunit k) (hc j) (hc k) (hCC j k hjk hp) v hv

/-- **Theorem S′ for a compact family on `ℂ⁴`** (`c k < 4` automatic). -/
theorem theorem_Sprime_compact_C4 {κ : Type*} [TopologicalSpace κ] [CompactSpace κ]
    [Nonempty κ] [DecidableEq κ] (c : κ → ℝ) (h : κ → Fin 2 × Fin 2 → ℂ)
    (hc_cont : Continuous c) (hh_cont : Continuous h)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      ∀ v : Fin 2 × Fin 2 → ℂ, (star v ⬝ᵥ v).re < c j * Complex.normSq (star (h j) ⬝ᵥ v) →
        (c k - 1) * (star v ⬝ᵥ v).re < c k * Complex.normSq (star (h k) ⬝ᵥ v)) :
    surgeryC (fun k => defect (c k) (h k)) = dualH (surgeryC (fun k => defect (c k) (h k))) ∧
      IsClosed (surgeryC (fun k => defect (c k) (h k))) := by
  have h4 : (Fintype.card (Fin 2 × Fin 2) : ℝ) = 4 := by norm_num [Fintype.card_prod]
  refine theorem_Sprime_compact c h hc_cont hh_cont hunit hc (fun k => ?_) hpair hCC
  rw [h4]
  linarith [(hc k).2]

/-! ### §O — control -/

/-- **Non-vacuity control.** The compact family indexed by `Unit` with the single defect
`1 − (3/2)|00⟩⟨00|` on `ℂ⁴` satisfies every hypothesis of `theorem_Sprime_compact`. -/
theorem control_compact_single_defect :
    surgeryC (fun _ : Unit => defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ))) =
        dualH (surgeryC (fun _ : Unit =>
          defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ)))) ∧
      IsClosed (surgeryC (fun _ : Unit =>
        defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ)))) :=
  theorem_Sprime_compact (fun _ => 3 / 2) (fun _ => Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ))
    continuous_const continuous_const
    (fun _ => by
      show star (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ)) ⬝ᵥ
        Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ) = 1
      rw [dotProduct_single, Pi.star_apply, Pi.single_eq_same, star_one, mul_one])
    (fun _ => ⟨by norm_num, by norm_num⟩)
    (fun _ => by norm_num [Fintype.card_prod])
    (fun _ _ => pr_self_nonneg (defect_isHermitian _ _))
    (fun j k hjk => absurd (Subsingleton.elim j k) hjk)

end

end CmSprime
end OIBridge

#print axioms OIBridge.CmSprime.coneOf
#print axioms OIBridge.CmSprime.surgeryC
#print axioms OIBridge.CmSprime.box
#print axioms OIBridge.CmSprime.zero_mem_coneOf
#print axioms OIBridge.CmSprime.single_mem_coneOf
#print axioms OIBridge.CmSprime.surgery_subset_surgeryC
#print axioms OIBridge.CmSprime.coneOf_isHermitian
#print axioms OIBridge.CmSprime.isClosed_isHermitian
#print axioms OIBridge.CmSprime.closure_coneOf_isHermitian
#print axioms OIBridge.CmSprime.continuous_pr_left
#print axioms OIBridge.CmSprime.continuous_pr_right
#print axioms OIBridge.CmSprime.continuous_qf_matrix
#print axioms OIBridge.CmSprime.isClosed_psd
#print axioms OIBridge.CmSprime.pr_coneOf_nonneg
#print axioms OIBridge.CmSprime.pr_closure_coneOf_nonneg
#print axioms OIBridge.CmSprime.pr_coneOf_coneOf_nonneg
#print axioms OIBridge.CmSprime.pr_closure_closure_nonneg
#print axioms OIBridge.CmSprime.defect_mem_surgeryC
#print axioms OIBridge.CmSprime.one_mem_surgeryC
#print axioms OIBridge.CmSprime.surgeryC_subset_dualH
#print axioms OIBridge.CmSprime.pr_one_one
#print axioms OIBridge.CmSprime.qf_one_eq_sum_sq
#print axioms OIBridge.CmSprime.pr_one_eq_sum_sq
#print axioms OIBridge.CmSprime.norm_entry_le_pr_one
#print axioms OIBridge.CmSprime.abs_qf_le
#print axioms OIBridge.CmSprime.abs_pr_le
#print axioms OIBridge.CmSprime.norm_entry_defect_le
#print axioms OIBridge.CmSprime.norm_entry_coneOf_le
#print axioms OIBridge.CmSprime.exists_net
#print axioms OIBridge.CmSprime.isCompact_box
#print axioms OIBridge.CmSprime.mem_box
#print axioms OIBridge.CmSprime.instFirstCountableTopologyMatrix
#print axioms OIBridge.CmSprime.dualH_subset_surgeryC_of_finite
#print axioms OIBridge.CmSprime.continuous_defect_family
#print axioms OIBridge.CmSprime.theorem_Sprime_compact
#print axioms OIBridge.CmSprime.theorem_Sprime_compact_ineq
#print axioms OIBridge.CmSprime.theorem_Sprime_compact_C4
#print axioms OIBridge.CmSprime.control_compact_single_defect
