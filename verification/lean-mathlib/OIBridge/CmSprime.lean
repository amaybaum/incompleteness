/-
  OIBridge/CmSprime.lean — design module of the research thread `research/countermodels` (round 4,
  node C17). Not adopted, not certified, not a round: a disposable dev branch. Theorem S′ of the
  thread's NOTES-C11 (finite form) as kernel statements.

  SETTING. `n` is a finite index type (`ℂⁿ`; the thread's case is `Fin 2 × Fin 2`, i.e. `ℂ⁴`).
  Matrices carry the trace pairing `pr A B = Re tr(A B)`; `Q` is the set of positive semidefinite
  matrices (`Matrix.PosSemidef`). For vectors, `ip a b = a† b` and `qf M x = Re (x† M x)`.
    * `defect c h = 1 − c · h h†` is a rank-one defect (`h† h = 1`, `c ∈ (1, 2]` in the theorems).
    * `surgery d = {q + Σ_k t_k d_k : q ⪰ 0, pr q (d j) ≥ 0 for every j, every t_k ≥ 0}` is the
      surgery cone `K(Z) = (Q ∩ Z*) + cone Z` of a finite family `d : ι → Matrix n n ℂ`.
    * `dualH S = {Y Hermitian : pr X Y ≥ 0 for every X ∈ S}` is the dual cone inside the Hermitian
      matrices.
  The open cap of `defect c h` is `{v : |v|² < c |⟨h|v⟩|²}` (exactly where `v† d v < 0`); its open
  co-cap is `{v : (c − 1)|v|² < c |⟨h|v⟩|²}`.

  THE STATEMENTS, in the words of the thread's NOTES.
    * `theorem_Sprime` (§G) — THEOREM S′, finite form. Let `d k = defect (c k) (h k)` for `k` in a
      finite type `ι`, every `h k` a unit vector, every `c k ∈ (1, 2]` with `c k < card n`
      (automatic on `ℂ⁴`), every pairing `pr (d j) (d k) ≥ 0`, and (CC): for every ordered pair
      `j ≠ k` with `pr (d j) (d k) > 0` the open cap of `d j` lies in the open co-cap of `d k`. Then
      `surgery d = dualH (surgery d)` — K(Z) is self-dual — and `surgery d` is closed.
    * `theorem_Sprime_C4` (§H) — THEOREM S′ exactly as NOTES-C11 states it, on `ℂ⁴`
      (`n = Fin 2 × Fin 2`): unit `h k`, `c k ∈ (1, 2]`, `pr (d j) (d k) ≥ 0` for all `j, k`, and
      (CC) as above; then K(Z) is closed and self-dual. No further hypothesis.
    * `theorem_Sprime_ineq` (§H) — the same theorem with (CC) in the inequality form
      `(√(c_j − 1) + √(c_k − 1))² ≤ c_j c_k |⟨h_j|h_k⟩|²`. Only the implication "inequality ⇒ cap
      inside co-cap" (`cap_subset_cocap`) is proved; its converse is not claimed.
    * `pr_defect_defect` (§H) — `pr (d j) (d k) = card n − c_j − c_k + c_j c_k |⟨h_j|h_k⟩|²` for
      unit `h_j, h_k`; on `ℂ⁴` with `c ≤ 2` the pairing is therefore nonnegative.
    * `twoDefect` (§H) — the sufficiency half of the thread's pair theorem C12-P (NOTES-C12): on
      `ℂ⁴`, for `c 0, c 1 ∈ (1, 2]` and unit `h 0, h 1`, if `pr (d 0) (d 1) = 0` or
      `(√(c 0 − 1) + √(c 1 − 1))² ≤ c 0 c 1 |⟨h 0|h 1⟩|²`, then K({d 0, d 1}) is self-dual and
      closed. The pairing `pr (d 0) (d 1) ≥ 0` is derived, not assumed.
    * `control_single_defect` (§I) — non-vacuity: the single defect `1 − (3/2)|e⟩⟨e|` on `ℂ⁴`
      (eigenvalue `−1/2`) satisfies the hypotheses, so its surgery cone is self-dual and closed.
  The engine is `selfDual_of_local` (§F): for a finite family of Hermitian `d k` with
  `pr 1 (d k) > 0`, pairwise nonnegative pairings, and the local condition "if `u† d_j u < 0` then
  `d_k` is positive definite on `u^⊥` whenever `k = j` or `pr (d k) (d j) > 0`", `surgery d` is
  self-dual and closed. Its proof uses Farkas for the PSD cone cut by finitely many half-spaces
  (§C, `exists_psd_sub`: every `y` pairing nonnegatively with `Q ∩ Z*` lies in `Q + cone Z`; the
  one-constraint lemma iterated over a finset, and the kernel's PSD self-duality
  `JordanClassification.psd_iff_trace_nonneg`), a decomposition of least total weight on a compact
  set of weights (§E, `exists_decomp`), the kernel's factorization
  `BoundaryAudit.psdFactorization_discharged`, and a local lemma (§D, `exists_qf_add_nonneg`:
  `q ⪰ 0` and `D` positive on the null vectors of `q` give `q + εD ⪰ 0` for some `ε > 0`).

  Not claimed: compact (infinite) defect sets; the necessity of (CC); anything about OI's composite
  cone (this is cone geometry); kernel certification (design run only).

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.JordanClassification
import OIBridge.BoundaryAudit
import OIBridge.ReferenceSufficiency
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.Matrix.Hermitian
import Mathlib.Topology.Instances.Matrix
import Mathlib.Topology.MetricSpace.ProperSpace
import Mathlib.Topology.Order.Compact
import Mathlib.Analysis.Normed.Group.Bounded

namespace OIBridge
namespace CmSprime

open Matrix
open scoped ComplexOrder

noncomputable section

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ### §A — definitions -/

/-- The trace pairing `pr A B = Re tr(A B)`. -/
def pr (A B : Matrix n n ℂ) : ℝ := (Matrix.trace (A * B)).re

/-- The inner product `ip a b = a† b`. -/
def ip (a b : n → ℂ) : ℂ := star a ⬝ᵥ b

/-- The real quadratic form `qf M x = Re (x† M x)`. -/
def qf (M : Matrix n n ℂ) (x : n → ℂ) : ℝ := (star x ⬝ᵥ (M *ᵥ x)).re

/-- The rank-one defect `1 − c · h h†`. -/
def defect (c : ℝ) (h : n → ℂ) : Matrix n n ℂ := 1 - (c : ℂ) • Matrix.vecMulVec h (star h)

/-- The dual of a set of matrices inside the Hermitian matrices, under the trace pairing. -/
def dualH (S : Set (Matrix n n ℂ)) : Set (Matrix n n ℂ) :=
  {Y | Y.IsHermitian ∧ ∀ X ∈ S, 0 ≤ pr X Y}

/-- The surgery cone `K(Z) = (Q ∩ Z*) + cone Z` of a finite family `d`. -/
def surgery {ι : Type*} [Fintype ι] (d : ι → Matrix n n ℂ) : Set (Matrix n n ℂ) :=
  {A | ∃ q : Matrix n n ℂ, ∃ t : ι → ℝ, q.PosSemidef ∧ (∀ j, 0 ≤ pr q (d j)) ∧
    (∀ k, 0 ≤ t k) ∧ A = q + ∑ k, (t k : ℂ) • d k}

/-! ### §B — the pairing, the forms and the defects -/

theorem pr_comm (A B : Matrix n n ℂ) : pr A B = pr B A := by
  unfold pr
  rw [Matrix.trace_mul_comm]

theorem pr_add_left (A A' B : Matrix n n ℂ) : pr (A + A') B = pr A B + pr A' B := by
  unfold pr
  rw [Matrix.add_mul, Matrix.trace_add, Complex.add_re]

theorem pr_add_right (A B B' : Matrix n n ℂ) : pr A (B + B') = pr A B + pr A B' := by
  unfold pr
  rw [Matrix.mul_add, Matrix.trace_add, Complex.add_re]

theorem pr_sub_right (A B B' : Matrix n n ℂ) : pr A (B - B') = pr A B - pr A B' := by
  unfold pr
  rw [Matrix.mul_sub, Matrix.trace_sub, Complex.sub_re]

theorem pr_sub_left (A A' B : Matrix n n ℂ) : pr (A - A') B = pr A B - pr A' B := by
  unfold pr
  rw [Matrix.sub_mul, Matrix.trace_sub, Complex.sub_re]

theorem pr_smul_left (r : ℝ) (A B : Matrix n n ℂ) : pr ((r : ℂ) • A) B = r * pr A B := by
  unfold pr
  rw [Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, Complex.re_ofReal_mul]

theorem pr_smul_right (r : ℝ) (A B : Matrix n n ℂ) : pr A ((r : ℂ) • B) = r * pr A B := by
  unfold pr
  rw [Matrix.mul_smul, Matrix.trace_smul, smul_eq_mul, Complex.re_ofReal_mul]

theorem pr_sum_left {ι : Type*} (s : Finset ι) (f : ι → Matrix n n ℂ) (B : Matrix n n ℂ) :
    pr (∑ k ∈ s, f k) B = ∑ k ∈ s, pr (f k) B := by
  unfold pr
  rw [Finset.sum_mul, Matrix.trace_sum, Complex.re_sum]

theorem pr_sum_right {ι : Type*} (s : Finset ι) (A : Matrix n n ℂ) (f : ι → Matrix n n ℂ) :
    pr A (∑ k ∈ s, f k) = ∑ k ∈ s, pr A (f k) := by
  unfold pr
  rw [Finset.mul_sum, Matrix.trace_sum, Complex.re_sum]

theorem pr_zero_left (B : Matrix n n ℂ) : pr 0 B = 0 := by
  unfold pr
  rw [zero_mul, Matrix.trace_zero, Complex.zero_re]

/-- A real number is self-adjoint in `ℂ`. -/
theorem star_ofReal' (r : ℝ) : star (r : ℂ) = (r : ℂ) := by
  rw [Complex.star_def, Complex.conj_ofReal]

theorem isSelfAdjoint_ofReal (r : ℝ) : IsSelfAdjoint (r : ℂ) :=
  star_ofReal' r

theorem star_mul_self_eq (z : ℂ) : star z * z = (Complex.normSq z : ℂ) := by
  rw [Complex.star_def, ← Complex.normSq_eq_conj_mul_self]

/-- The trace of a product of two Hermitian matrices is real. -/
theorem trace_mul_real {A B : Matrix n n ℂ} (hA : A.IsHermitian) (hB : B.IsHermitian) :
    (((Matrix.trace (A * B)).re : ℝ) : ℂ) = Matrix.trace (A * B) := by
  rw [← Complex.conj_eq_iff_re, starRingEnd_apply, ← Matrix.trace_conjTranspose,
    Matrix.conjTranspose_mul, hA.eq, hB.eq, Matrix.trace_mul_comm]

theorem defect_isHermitian (c : ℝ) (h : n → ℂ) : (defect c h).IsHermitian := by
  unfold defect
  exact Matrix.isHermitian_one.sub
    ((Matrix.posSemidef_vecMulVec_self_star h).isHermitian.smul (isSelfAdjoint_ofReal c))

theorem isHermitian_sum_smul {ι : Type*} [Fintype ι] (d : ι → Matrix n n ℂ)
    (hd : ∀ k, (d k).IsHermitian) (t : ι → ℝ) : (∑ k, (t k : ℂ) • d k).IsHermitian :=
  Matrix.isHermitian_iff_isSelfAdjoint.mpr (isSelfAdjoint_sum Finset.univ fun k _ =>
    Matrix.isHermitian_iff_isSelfAdjoint.mp ((hd k).smul (isSelfAdjoint_ofReal (t k))))

theorem qf_zero (M : Matrix n n ℂ) : qf M 0 = 0 := by
  unfold qf
  rw [Matrix.mulVec_zero, dotProduct_zero, Complex.zero_re]

theorem qf_nonneg_of_psd {M : Matrix n n ℂ} (hM : M.PosSemidef) (x : n → ℂ) : 0 ≤ qf M x :=
  (Complex.nonneg_iff.mp (hM.dotProduct_mulVec_nonneg x)).1

theorem psd_of_qf {M : Matrix n n ℂ} (hM : M.IsHermitian) (h : ∀ x, 0 ≤ qf M x) :
    M.PosSemidef := by
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg hM fun x => ?_
  have him : (star x ⬝ᵥ (M *ᵥ x)).im = 0 := by
    have h1 := hM.im_star_dotProduct_mulVec_self x
    rwa [RCLike.im_to_complex] at h1
  rw [Complex.nonneg_iff]
  exact ⟨h x, him.symm⟩

theorem pr_psd_psd {A B : Matrix n n ℂ} (hA : A.PosSemidef) (hB : B.PosSemidef) : 0 ≤ pr A B :=
  (Complex.nonneg_iff.mp (OperationalRigidity.psd_trace_mul_nonneg hA hB)).1

theorem pr_self_nonneg {D : Matrix n n ℂ} (hD : D.IsHermitian) : 0 ≤ pr D D := by
  have h1 := Matrix.posSemidef_self_mul_conjTranspose D
  rw [hD.eq] at h1
  exact (Complex.nonneg_iff.mp h1.trace_nonneg).1

/-- A Hermitian matrix pairing nonnegatively with every positive semidefinite matrix is positive
semidefinite (the kernel's PSD self-duality, JordanClassification.lean:84). -/
theorem psd_of_pr {M : Matrix n n ℂ} (hM : M.IsHermitian)
    (h : ∀ X : Matrix n n ℂ, X.PosSemidef → 0 ≤ pr X M) : M.PosSemidef := by
  rw [JordanClassification.psd_iff_trace_nonneg hM]
  intro X hX
  rw [Matrix.trace_mul_comm, ← trace_mul_real hX.isHermitian hM]
  exact Complex.zero_le_real.mpr (h X hX)

theorem pr_one_defect (c : ℝ) (h : n → ℂ) (hh : star h ⬝ᵥ h = 1) :
    pr 1 (defect c h) = (Fintype.card n : ℝ) - c := by
  unfold pr defect
  rw [one_mul, Matrix.trace_sub, Matrix.trace_one, Matrix.trace_smul, Matrix.trace_vecMulVec,
    dotProduct_comm, hh, smul_eq_mul, mul_one, Complex.sub_re, Complex.natCast_re,
    Complex.ofReal_re]

theorem vecMulVec_mulVec' (u v w : n → ℂ) : Matrix.vecMulVec u v *ᵥ w = (v ⬝ᵥ w) • u := by
  ext i
  simp [Matrix.vecMulVec, Matrix.mulVec, dotProduct, Finset.mul_sum, mul_comm, mul_left_comm]

theorem ip_zero_left (b : n → ℂ) : ip 0 b = 0 := by
  unfold ip
  rw [star_zero, zero_dotProduct]

theorem ip_zero_right (a : n → ℂ) : ip a 0 = 0 := by
  unfold ip
  rw [dotProduct_zero]

theorem ip_sub_left (a a' b : n → ℂ) : ip (a - a') b = ip a b - ip a' b := by
  unfold ip
  rw [star_sub, sub_dotProduct]

theorem ip_sub_right (a b b' : n → ℂ) : ip a (b - b') = ip a b - ip a b' := by
  unfold ip
  rw [dotProduct_sub]

theorem ip_smul_left (c : ℂ) (a b : n → ℂ) : ip (c • a) b = star c * ip a b := by
  unfold ip
  rw [star_smul, smul_dotProduct, smul_eq_mul]

theorem ip_smul_right (c : ℂ) (a b : n → ℂ) : ip a (c • b) = c * ip a b := by
  unfold ip
  rw [dotProduct_smul, smul_eq_mul]

theorem ip_swap (a b : n → ℂ) : ip b a = star (ip a b) := by
  unfold ip
  exact Matrix.star_dotProduct b a

theorem normSq_ip_swap (a b : n → ℂ) : Complex.normSq (ip b a) = Complex.normSq (ip a b) := by
  rw [ip_swap a b, Complex.star_def, Complex.normSq_conj]

theorem normSq_dot_swap (a b : n → ℂ) :
    Complex.normSq (star b ⬝ᵥ a) = Complex.normSq (star a ⬝ᵥ b) :=
  normSq_ip_swap a b

theorem ip_self_ofReal (a : n → ℂ) : ip a a = (((ip a a).re : ℝ) : ℂ) :=
  ReferenceSufficiency.dotProduct_star_self_real a

theorem ip_self_re_pos {a : n → ℂ} (ha : a ≠ 0) : 0 < (ip a a).re :=
  ReferenceSufficiency.dotProduct_star_self_pos ha

theorem ip_self_re_nonneg (a : n → ℂ) : 0 ≤ (ip a a).re := by
  by_cases ha : a = 0
  · rw [ha, ip_zero_left, Complex.zero_re]
  · exact (ip_self_re_pos ha).le

/-- The quadratic form of a defect: `v† (1 − c h h†) v = |v|² − c |⟨h|v⟩|²`. -/
theorem qf_defect (c : ℝ) (h v : n → ℂ) :
    qf (defect c h) v = (ip v v).re - c * Complex.normSq (ip h v) := by
  have hmul : defect c h *ᵥ v = v - ((c : ℂ) * ip h v) • h := by
    unfold defect ip
    rw [Matrix.sub_mulVec, Matrix.one_mulVec, Matrix.smul_mulVec, vecMulVec_mulVec', smul_smul]
  have h1 : star v ⬝ᵥ h = star (ip h v) := Matrix.star_dotProduct v h
  have h2 : ip h v * star (ip h v) = (Complex.normSq (ip h v) : ℂ) := by
    rw [Complex.star_def, Complex.mul_conj]
  show (star v ⬝ᵥ (defect c h *ᵥ v)).re = (star v ⬝ᵥ v).re - c * Complex.normSq (ip h v)
  rw [hmul, dotProduct_sub, dotProduct_smul, smul_eq_mul, Complex.sub_re, h1, mul_assoc, h2,
    Complex.re_ofReal_mul, Complex.ofReal_re]

/-- The quadratic form of `y − Σ_k t_k d_k`. -/
theorem qf_sub_sum {ι : Type*} [Fintype ι] (y : Matrix n n ℂ) (d : ι → Matrix n n ℂ)
    (t : ι → ℝ) (v : n → ℂ) :
    qf (y - ∑ k, (t k : ℂ) • d k) v = qf y v - ∑ k, t k * qf (d k) v := by
  unfold qf
  rw [Matrix.sub_mulVec, Matrix.sum_mulVec, dotProduct_sub, dotProduct_sum, Complex.sub_re,
    Complex.re_sum]
  congr 1
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Matrix.smul_mulVec, dotProduct_smul, smul_eq_mul, Complex.re_ofReal_mul]

theorem qf_real_smul (M : Matrix n n ℂ) (r : ℝ) (x : n → ℂ) :
    qf M ((r : ℂ) • x) = r * r * qf M x := by
  unfold qf
  rw [ReferenceSufficiency.form_real_smul, Complex.re_ofReal_mul]

theorem continuous_qf (M : Matrix n n ℂ) : Continuous (qf M) := by
  have h1 : Continuous fun x : n → ℂ => M *ᵥ x := continuous_const.matrix_mulVec continuous_id
  have h2 : Continuous fun x : n → ℂ => star x ⬝ᵥ (M *ᵥ x) := continuous_star.dotProduct h1
  exact Complex.continuous_re.comp h2

/-- The quadratic form of `B Bᴴ` is the squared length of `Bᴴ x`. -/
theorem qf_mul_conjTranspose (B : Matrix n n ℂ) (x : n → ℂ) :
    qf (B * Bᴴ) x = (star (Bᴴ *ᵥ x) ⬝ᵥ (Bᴴ *ᵥ x)).re := by
  unfold qf
  rw [← Matrix.mulVec_mulVec, Matrix.dotProduct_mulVec (star x) B (Bᴴ *ᵥ x),
    Matrix.mulVec_conjTranspose B x, star_star (star x ᵥ* B)]

/-- The trace pairing of `B Bᴴ` with `D` is the sum of the quadratic forms of `D` on the columns. -/
theorem pr_mul_conjTranspose (B D : Matrix n n ℂ) :
    pr (B * Bᴴ) D = ∑ m, qf D (fun i => B i m) := by
  have hdec : B * Bᴴ = ∑ m, Matrix.vecMulVec (fun i => B i m) (star fun i => B i m) := by
    ext i j
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.sum_apply,
      Matrix.vecMulVec_apply, Pi.star_apply]
  rw [pr_comm, hdec, pr_sum_right]
  refine Finset.sum_congr rfl fun m _ => ?_
  unfold pr qf
  rw [JordanClassification.trace_mul_vecMulVec]

/-! ### §C — Farkas for a cone cut by finitely many half-spaces -/

/-- The ratios `g x / ℓ x` over the points of `P` with `ℓ x > 0`. -/
def ratioSet {V : Type*} (P : V → Prop) (g ℓ : V → ℝ) : Set ℝ :=
  {r | ∃ x, P x ∧ 0 < ℓ x ∧ r = g x / ℓ x}

/-- **One constraint.** On a convex cone `P` (closed under nonnegative combinations, for `g` and
`ℓ`) with a point where `ℓ > 0`, if `g ≥ 0` wherever `ℓ ≥ 0`, then `g ≥ σ ℓ` on `P` for some
`σ ≥ 0`. -/
theorem farkas_one {V : Type*} (P : V → Prop) (g ℓ : V → ℝ)
    (hcomb : ∀ x x', P x → P x' → ∀ a b : ℝ, 0 ≤ a → 0 ≤ b →
      ∃ z, P z ∧ g z = a * g x + b * g x' ∧ ℓ z = a * ℓ x + b * ℓ x')
    (x₀ : V) (hx₀ : P x₀) (hℓ₀ : 0 < ℓ x₀)
    (hyp : ∀ x, P x → 0 ≤ ℓ x → 0 ≤ g x) :
    ∃ σ : ℝ, 0 ≤ σ ∧ ∀ x, P x → σ * ℓ x ≤ g x := by
  have hlow : ∀ r ∈ ratioSet P g ℓ, (0 : ℝ) ≤ r := by
    rintro r ⟨x, hx, hl, rfl⟩
    exact div_nonneg (hyp x hx hl.le) hl.le
  have hne : (ratioSet P g ℓ).Nonempty := ⟨g x₀ / ℓ x₀, x₀, hx₀, hℓ₀, rfl⟩
  have hbdd : BddBelow (ratioSet P g ℓ) := ⟨0, hlow⟩
  refine ⟨sInf (ratioSet P g ℓ), le_csInf hne hlow, fun x hx => ?_⟩
  rcases lt_trichotomy (ℓ x) 0 with hneg | hzero | hpos
  · have hle : g x / ℓ x ≤ sInf (ratioSet P g ℓ) := by
      refine le_csInf hne ?_
      rintro r ⟨x', hx', hl', rfl⟩
      obtain ⟨z, hz, hgz, hlz⟩ := hcomb x x' hx hx' (ℓ x') (-ℓ x) hl'.le (by linarith)
      have hz0 : 0 ≤ ℓ z := le_of_eq (by rw [hlz]; ring)
      have hg0 : 0 ≤ ℓ x' * g x + -ℓ x * g x' := by
        have h1 := hyp z hz hz0
        rwa [hgz] at h1
      rw [div_le_iff_of_neg hneg, div_mul_eq_mul_div, div_le_iff₀ hl']
      linarith
    exact (div_le_iff_of_neg hneg).mp hle
  · rw [hzero, mul_zero]
    exact hyp x hx hzero.ge
  · exact (le_div_iff₀ hpos).mp (csInf_le hbdd ⟨x, hx, hpos, rfl⟩)

/-- **Finitely many constraints.** The one-constraint lemma iterated over a finset. -/
theorem farkas_finset {V ι : Type*} [DecidableEq ι] (P : V → Prop) (ℓ : ι → V → ℝ)
    (s : Finset ι) : ∀ g : V → ℝ,
      (∀ x x', P x → P x' → ∀ a b : ℝ, 0 ≤ a → 0 ≤ b → ∃ z, P z ∧
        g z = a * g x + b * g x' ∧ ∀ k, ℓ k z = a * ℓ k x + b * ℓ k x') →
      (∃ x₀, P x₀ ∧ ∀ k ∈ s, 0 < ℓ k x₀) →
      (∀ x, P x → (∀ k ∈ s, 0 ≤ ℓ k x) → 0 ≤ g x) →
      ∃ t : ι → ℝ, (∀ k, 0 ≤ t k) ∧ ∀ x, P x → ∑ k ∈ s, t k * ℓ k x ≤ g x := by
  induction s using Finset.induction_on with
  | empty =>
    intro g _ _ hyp
    refine ⟨fun _ => 0, fun _ => le_refl 0, fun x hx => ?_⟩
    rw [Finset.sum_empty]
    exact hyp x hx fun k hk => absurd hk (Finset.notMem_empty k)
  | insert a s ha ih =>
    intro g hcomb hslater hyp
    obtain ⟨x₀, hx₀, hpos⟩ := hslater
    obtain ⟨σ, hσ, hσg⟩ := farkas_one (fun x => P x ∧ ∀ k ∈ s, 0 ≤ ℓ k x) g (ℓ a)
      (fun x x' hx hx' a' b' ha' hb' => by
        obtain ⟨z, hz, hgz, hlz⟩ := hcomb x x' hx.1 hx'.1 a' b' ha' hb'
        refine ⟨z, ⟨hz, fun k hk => ?_⟩, hgz, hlz a⟩
        rw [hlz k]
        exact add_nonneg (mul_nonneg ha' (hx.2 k hk)) (mul_nonneg hb' (hx'.2 k hk)))
      x₀ ⟨hx₀, fun k hk => (hpos k (Finset.mem_insert_of_mem hk)).le⟩
      (hpos a (Finset.mem_insert_self a s))
      (fun x hx hla => hyp x hx.1 fun k hk => by
        rcases Finset.mem_insert.mp hk with hka | hk'
        · rw [hka]
          exact hla
        · exact hx.2 k hk')
    obtain ⟨t, ht, htg⟩ := ih (fun x => g x - σ * ℓ a x)
      (fun x x' hx hx' a' b' ha' hb' => by
        obtain ⟨z, hz, hgz, hlz⟩ := hcomb x x' hx hx' a' b' ha' hb'
        refine ⟨z, hz, ?_, hlz⟩
        show g z - σ * ℓ a z = a' * (g x - σ * ℓ a x) + b' * (g x' - σ * ℓ a x')
        rw [hgz, hlz a]
        ring)
      ⟨x₀, hx₀, fun k hk => hpos k (Finset.mem_insert_of_mem hk)⟩
      (fun x hx hks => by
        show 0 ≤ g x - σ * ℓ a x
        have h1 : σ * ℓ a x ≤ g x := hσg x ⟨hx, hks⟩
        linarith)
    refine ⟨Function.update t a σ, fun k => ?_, fun x hx => ?_⟩
    · by_cases hka : k = a
      · rw [hka, Function.update_self]
        exact hσ
      · rw [Function.update_of_ne hka]
        exact ht k
    · rw [Finset.sum_insert ha, Function.update_self]
      have hs : ∑ k ∈ s, Function.update t a σ k * ℓ k x = ∑ k ∈ s, t k * ℓ k x :=
        Finset.sum_congr rfl fun k hk => by
          have hka : k ≠ a := fun h => ha (h ▸ hk)
          rw [Function.update_of_ne hka]
      rw [hs]
      have h1 : ∑ k ∈ s, t k * ℓ k x ≤ g x - σ * ℓ a x := htg x hx
      linarith

/-- **`(Q ∩ Z*)* ⊆ Q + cone Z`.** A Hermitian `y` pairing nonnegatively with every positive
semidefinite `x` with `pr x (d k) ≥ 0` for all `k` is `y = z + Σ s_k d_k` with `z ⪰ 0`, `s ≥ 0`. -/
theorem exists_psd_sub {ι : Type*} [Fintype ι] [DecidableEq ι] (d : ι → Matrix n n ℂ)
    (hd : ∀ k, (d k).IsHermitian) (htr : ∀ k, 0 < pr 1 (d k)) {y : Matrix n n ℂ}
    (hy : y.IsHermitian)
    (hdual : ∀ x : Matrix n n ℂ, x.PosSemidef → (∀ k, 0 ≤ pr x (d k)) → 0 ≤ pr x y) :
    ∃ s : ι → ℝ, (∀ k, 0 ≤ s k) ∧ (y - ∑ k, (s k : ℂ) • d k).PosSemidef := by
  have hcomb : ∀ x x' : Matrix n n ℂ, x.PosSemidef → x'.PosSemidef → ∀ a b : ℝ, 0 ≤ a → 0 ≤ b →
      ∃ z : Matrix n n ℂ, z.PosSemidef ∧ pr z y = a * pr x y + b * pr x' y ∧
        ∀ k, pr z (d k) = a * pr x (d k) + b * pr x' (d k) := by
    intro x x' hx hx' a b ha hb
    refine ⟨(a : ℂ) • x + (b : ℂ) • x',
      (hx.smul (Complex.zero_le_real.mpr ha)).add (hx'.smul (Complex.zero_le_real.mpr hb)), ?_,
      fun k => ?_⟩
    · rw [pr_add_left, pr_smul_left, pr_smul_left]
    · rw [pr_add_left, pr_smul_left, pr_smul_left]
  obtain ⟨s, hs, hsg⟩ := farkas_finset (fun x : Matrix n n ℂ => x.PosSemidef)
    (fun k x => pr x (d k)) Finset.univ (fun x => pr x y) hcomb
    ⟨1, Matrix.PosSemidef.one, fun k _ => htr k⟩
    (fun x hx hk => hdual x hx fun k => hk k (Finset.mem_univ k))
  refine ⟨s, hs, ?_⟩
  refine psd_of_pr (hy.sub (isHermitian_sum_smul d hd s)) fun X hX => ?_
  have h1 : ∑ k, s k * pr X (d k) ≤ pr X y := hsg X hX
  rw [pr_sub_right, pr_sum_right]
  simp only [pr_smul_right]
  linarith

/-! ### §D — the local lemma -/

set_option maxHeartbeats 800000 in
/-- **Local lemma.** If `q ⪰ 0` (as a form) and `D` is positive on every nonzero null vector of `q`,
then `q + εD ⪰ 0` (as a form) for some `ε > 0`. Compactness of the unit sphere. -/
theorem exists_qf_add_nonneg (q D : Matrix n n ℂ) (hq : ∀ x, 0 ≤ qf q x)
    (hpos : ∀ x : n → ℂ, x ≠ 0 → qf q x = 0 → 0 < qf D x) :
    ∃ ε : ℝ, 0 < ε ∧ ∀ x, 0 ≤ qf q x + ε * qf D x := by
  have hS : IsCompact (Metric.sphere (0 : n → ℂ) 1) := isCompact_sphere 0 1
  have hA : IsCompact (Metric.sphere (0 : n → ℂ) 1 ∩ {x | qf D x ≤ 0}) :=
    hS.inter_right (isClosed_le (continuous_qf D) continuous_const)
  obtain ⟨m, hm, hmA⟩ := hA.exists_forall_le' (continuous_qf q).continuousOn (a := 0)
    (fun x hx => by
      have hx0 : x ≠ 0 := by
        intro h0
        have h1 : ‖x‖ = 1 := mem_sphere_zero_iff_norm.mp hx.1
        rw [h0, norm_zero] at h1
        exact zero_ne_one h1
      rcases (hq x).lt_or_eq with h | h
      · exact h
      · exact absurd (show qf D x ≤ 0 from hx.2) (not_le.mpr (hpos x hx0 h.symm)))
  obtain ⟨C, hC⟩ := hS.exists_bound_of_continuousOn (continuous_qf D).continuousOn
  have hC1 : 0 < |C| + 1 := by positivity
  obtain ⟨ε, hεdef⟩ : ∃ ε : ℝ, ε = m / (|C| + 1) := ⟨_, rfl⟩
  have hεpos : 0 < ε := by rw [hεdef]; exact div_pos hm hC1
  have hεC : ε * |C| ≤ m := by
    rw [hεdef, div_mul_eq_mul_div, div_le_iff₀ hC1]
    linarith [hm.le]
  have hunit : ∀ x ∈ Metric.sphere (0 : n → ℂ) 1, 0 ≤ qf q x + ε * qf D x := by
    intro x hx
    by_cases hd : qf D x ≤ 0
    · have h1 : m ≤ qf q x := hmA x ⟨hx, hd⟩
      have h3 : ‖qf D x‖ ≤ C := hC x hx
      rw [Real.norm_eq_abs] at h3
      have h4 := neg_abs_le (qf D x)
      have h5 := le_abs_self C
      have h2 : -|C| ≤ qf D x := by linarith
      have h6 : ε * -|C| ≤ ε * qf D x := mul_le_mul_of_nonneg_left h2 hεpos.le
      linarith
    · push_neg at hd
      have h1 := mul_pos hεpos hd
      have h2 := hq x
      linarith
  refine ⟨ε, hεpos, fun x => ?_⟩
  by_cases hx : x = 0
  · have h0 : qf q x + ε * qf D x = 0 := by
      rw [hx, qf_zero, qf_zero, mul_zero, add_zero]
    exact le_of_eq h0.symm
  · have hnx : 0 < ‖x‖ := norm_pos_iff.mpr hx
    have hmem : ((‖x‖⁻¹ : ℝ) : ℂ) • x ∈ Metric.sphere (0 : n → ℂ) 1 := by
      rw [mem_sphere_zero_iff_norm, norm_smul, Complex.norm_real, Real.norm_eq_abs,
        abs_of_pos (inv_pos.mpr hnx), inv_mul_cancel₀ hnx.ne']
    have h1 := hunit _ hmem
    rw [qf_real_smul, qf_real_smul] at h1
    have h2 : 0 < ‖x‖⁻¹ * ‖x‖⁻¹ := mul_pos (inv_pos.mpr hnx) (inv_pos.mpr hnx)
    by_contra hneg
    push_neg at hneg
    have h3 := mul_neg_of_pos_of_neg h2 hneg
    linarith

/-! ### §E — the decomposition of least total weight -/

/-- Decrease the `k`-th weight by `ε`. -/
def decW {ι : Type*} [DecidableEq ι] (t : ι → ℝ) (k : ι) (ε : ℝ) (l : ι) : ℝ :=
  if l = k then t l - ε else t l

theorem sum_decW_mul {ι : Type*} [Fintype ι] [DecidableEq ι] (t a : ι → ℝ) (k : ι) (ε : ℝ) :
    ∑ l, decW t k ε l * a l = ∑ l, t l * a l - ε * a k := by
  have h : ∀ l, decW t k ε l * a l = t l * a l - (if l = k then ε * a l else 0) := by
    intro l
    unfold decW
    split_ifs with hl
    · ring
    · ring
  rw [Finset.sum_congr rfl fun l _ => h l, Finset.sum_sub_distrib,
    Finset.sum_ite_eq' Finset.univ k, if_pos (Finset.mem_univ k)]

theorem sum_decW {ι : Type*} [Fintype ι] [DecidableEq ι] (t : ι → ℝ) (k : ι) (ε : ℝ) :
    ∑ l, decW t k ε l = ∑ l, t l - ε := by
  have h : ∀ l, decW t k ε l = t l - (if l = k then ε else 0) := by
    intro l
    unfold decW
    split_ifs with hl
    · ring
    · ring
  rw [Finset.sum_congr rfl fun l _ => h l, Finset.sum_sub_distrib,
    Finset.sum_ite_eq' Finset.univ k, if_pos (Finset.mem_univ k)]

/-- The feasible weights: `t ≥ 0` with `y − Σ t_k d_k ⪰ 0` (as a form). -/
def feas {ι : Type*} [Fintype ι] (y : Matrix n n ℂ) (d : ι → Matrix n n ℂ) : Set (ι → ℝ) :=
  (⋂ k, {t : ι → ℝ | 0 ≤ t k}) ∩ ⋂ v : n → ℂ, {t | 0 ≤ qf y v - ∑ k, t k * qf (d k) v}

theorem mem_feas {ι : Type*} [Fintype ι] {y : Matrix n n ℂ} {d : ι → Matrix n n ℂ}
    {t : ι → ℝ} :
    t ∈ feas y d ↔ (∀ k, 0 ≤ t k) ∧ ∀ v, 0 ≤ qf y v - ∑ k, t k * qf (d k) v := by
  simp only [feas, Set.mem_inter_iff, Set.mem_iInter, Set.mem_setOf_eq]

theorem isClosed_feas {ι : Type*} [Fintype ι] (y : Matrix n n ℂ) (d : ι → Matrix n n ℂ) :
    IsClosed (feas y d) := by
  have h1 : IsClosed (⋂ k, {t : ι → ℝ | 0 ≤ t k}) :=
    isClosed_iInter fun k => isClosed_le continuous_const (continuous_apply k)
  have h2 : IsClosed (⋂ v : n → ℂ, {t : ι → ℝ | 0 ≤ qf y v - ∑ k, t k * qf (d k) v}) :=
    isClosed_iInter fun v => isClosed_le continuous_const
      (continuous_const.sub (continuous_finsetSum _ fun k _ =>
        (continuous_apply k).mul continuous_const))
  exact h1.inter h2

theorem feas_subset {ι : Type*} [Fintype ι] {y : Matrix n n ℂ} (hy : y.IsHermitian)
    {d : ι → Matrix n n ℂ} (hd : ∀ k, (d k).IsHermitian) (htr : ∀ k, 0 < pr 1 (d k)) :
    feas y d ⊆ Set.pi Set.univ (fun k => Set.Icc 0 (pr 1 y / pr 1 (d k))) := by
  intro t ht
  obtain ⟨ht0, htv⟩ := mem_feas.mp ht
  have hpsd : (y - ∑ k, (t k : ℂ) • d k).PosSemidef :=
    psd_of_qf (hy.sub (isHermitian_sum_smul d hd t)) fun v => by
      rw [qf_sub_sum]
      exact htv v
  have htr0 : 0 ≤ pr 1 (y - ∑ k, (t k : ℂ) • d k) := pr_psd_psd Matrix.PosSemidef.one hpsd
  rw [pr_sub_right, pr_sum_right] at htr0
  simp only [pr_smul_right] at htr0
  rw [Set.mem_univ_pi]
  intro k
  refine ⟨ht0 k, ?_⟩
  rw [le_div_iff₀ (htr k)]
  have hle : t k * pr 1 (d k) ≤ ∑ l, t l * pr 1 (d l) :=
    Finset.single_le_sum (fun l _ => mul_nonneg (ht0 l) (htr l).le) (Finset.mem_univ k)
  linarith

theorem isCompact_feas {ι : Type*} [Fintype ι] {y : Matrix n n ℂ} (hy : y.IsHermitian)
    {d : ι → Matrix n n ℂ} (hd : ∀ k, (d k).IsHermitian) (htr : ∀ k, 0 < pr 1 (d k)) :
    IsCompact (feas y d) := by
  have hbox : IsCompact (Set.pi Set.univ (fun k : ι => Set.Icc (0 : ℝ) (pr 1 y / pr 1 (d k)))) :=
    isCompact_univ_pi fun _ => isCompact_Icc
  exact hbox.of_isClosed_subset (isClosed_feas y d) (feas_subset hy hd htr)

set_option maxHeartbeats 800000 in
/-- **The decomposition.** Under the local condition, every `y ∈ (Q + cone Z) ∩ Z*` is
`q + Σ t_k d_k` with `q ⪰ 0`, `q ∈ Z*`, `t ≥ 0` (a decomposition of least total weight). -/
theorem exists_decomp {ι : Type*} [Fintype ι] [DecidableEq ι] (d : ι → Matrix n n ℂ)
    (hd : ∀ k, (d k).IsHermitian) (htr : ∀ k, 0 < pr 1 (d k))
    (hpair : ∀ j k, 0 ≤ pr (d j) (d k))
    (hloc : ∀ j k, (k = j ∨ 0 < pr (d k) (d j)) → ∀ u : n → ℂ, qf (d j) u < 0 →
      ∀ x : n → ℂ, x ≠ 0 → star u ⬝ᵥ x = 0 → 0 < qf (d k) x)
    {y : Matrix n n ℂ} (hy : y.IsHermitian) (hyd : ∀ j, 0 ≤ pr y (d j))
    {s : ι → ℝ} (hs : ∀ k, 0 ≤ s k) (hys : (y - ∑ k, (s k : ℂ) • d k).PosSemidef) :
    ∃ t : ι → ℝ, (∀ k, 0 ≤ t k) ∧ (y - ∑ k, (t k : ℂ) • d k).PosSemidef ∧
      ∀ j, 0 ≤ pr (y - ∑ k, (t k : ℂ) • d k) (d j) := by
  have hsF : s ∈ feas y d := mem_feas.mpr ⟨hs, fun v => by
    have h1 := qf_nonneg_of_psd hys v
    rwa [qf_sub_sum] at h1⟩
  have hcont : Continuous fun t : ι → ℝ => ∑ l, t l :=
    continuous_finsetSum Finset.univ fun l _ => continuous_apply l
  obtain ⟨t, htF, hmin⟩ := (isCompact_feas hy hd htr).exists_isMinOn ⟨s, hsF⟩ hcont.continuousOn
  obtain ⟨ht0, htv⟩ := mem_feas.mp htF
  have hqH : (y - ∑ k, (t k : ℂ) • d k).IsHermitian := hy.sub (isHermitian_sum_smul d hd t)
  have hqv : ∀ v, 0 ≤ qf (y - ∑ k, (t k : ℂ) • d k) v := fun v => by
    rw [qf_sub_sum]
    exact htv v
  have hq : (y - ∑ k, (t k : ℂ) • d k).PosSemidef := psd_of_qf hqH hqv
  refine ⟨t, ht0, hq, fun j => ?_⟩
  by_contra hneg
  push_neg at hneg
  -- a column `u` of a factor `B` of `q` in the cap of `d j`
  obtain ⟨B, hB⟩ := BoundaryAudit.psdFactorization_discharged n (y - ∑ k, (t k : ℂ) • d k) hq
  have hsum : pr (y - ∑ k, (t k : ℂ) • d k) (d j) = ∑ m, qf (d j) (fun i => B i m) := by
    rw [hB, pr_mul_conjTranspose]
  obtain ⟨m, hm⟩ : ∃ m, qf (d j) (fun i => B i m) < 0 := by
    by_contra hall
    push_neg at hall
    have h1 : 0 ≤ ∑ m, qf (d j) (fun i => B i m) := Finset.sum_nonneg fun m _ => hall m
    linarith
  -- the null vectors of `q` are orthogonal to `u`
  have hker : ∀ x : n → ℂ, qf (y - ∑ k, (t k : ℂ) • d k) x = 0 →
      star (fun i => B i m) ⬝ᵥ x = 0 := by
    intro x hx
    rw [hB, qf_mul_conjTranspose] at hx
    have h2 : Bᴴ *ᵥ x = 0 := by
      by_contra hne
      have h3 := ReferenceSufficiency.dotProduct_star_self_pos hne
      linarith
    have h3 : (Bᴴ *ᵥ x) m = star (fun i => B i m) ⬝ᵥ x := by
      simp only [Matrix.mulVec, dotProduct, Matrix.conjTranspose_apply, Pi.star_apply]
    rw [← h3, h2, Pi.zero_apply]
  -- a weight that can be decreased
  obtain ⟨k, htk, hkj⟩ : ∃ k, 0 < t k ∧ (k = j ∨ 0 < pr (d k) (d j)) := by
    rcases (ht0 j).lt_or_eq with htj | htj
    · exact ⟨j, htj, Or.inl rfl⟩
    · have hyj : 0 ≤ pr y (d j) := hyd j
      have hy_eq : y = (y - ∑ k, (t k : ℂ) • d k) + ∑ k, (t k : ℂ) • d k := by
        rw [sub_add_cancel]
      rw [hy_eq, pr_add_left, pr_sum_left] at hyj
      simp only [pr_smul_left] at hyj
      have hpos : 0 < ∑ k, t k * pr (d k) (d j) := by linarith
      obtain ⟨k, hk⟩ : ∃ k, 0 < t k * pr (d k) (d j) := by
        by_contra hall
        push_neg at hall
        have h1 : ∑ k, t k * pr (d k) (d j) ≤ 0 := Finset.sum_nonpos fun k _ => hall k
        linarith
      refine ⟨k, ?_, Or.inr ?_⟩
      · rcases (ht0 k).lt_or_eq with h | h
        · exact h
        · rw [← h, zero_mul] at hk
          exact absurd hk (lt_irrefl 0)
      · rcases (hpair k j).lt_or_eq with h | h
        · exact h
        · rw [← h, mul_zero] at hk
          exact absurd hk (lt_irrefl 0)
  -- the local lemma
  obtain ⟨ε, hε, hεq⟩ := exists_qf_add_nonneg (y - ∑ k, (t k : ℂ) • d k) (d k) hqv
    (fun x hx hqx => hloc j k hkj (fun i => B i m) hm x hx (hker x hqx))
  obtain ⟨ε', hε'pos, hε'ε, hε't⟩ : ∃ ε' : ℝ, 0 < ε' ∧ ε' ≤ ε ∧ ε' ≤ t k :=
    ⟨min ε (t k), lt_min hε htk, min_le_left _ _, min_le_right _ _⟩
  -- the decreased weight is feasible and has smaller total weight
  have hdecF : decW t k ε' ∈ feas y d := by
    refine mem_feas.mpr ⟨fun l => ?_, fun v => ?_⟩
    · unfold decW
      split_ifs with hl
      · rw [hl]
        linarith
      · exact ht0 l
    · rw [show ∑ l, decW t k ε' l * qf (d l) v = ∑ l, t l * qf (d l) v - ε' * qf (d k) v from
        sum_decW_mul t (fun l => qf (d l) v) k ε']
      have h1 : qf (y - ∑ k, (t k : ℂ) • d k) v = qf y v - ∑ l, t l * qf (d l) v :=
        qf_sub_sum _ _ _ _
      have h2 := hεq v
      have h3 := hqv v
      rcases le_or_gt 0 (qf (d k) v) with h5 | h5
      · have h6 := mul_nonneg hε'pos.le h5
        linarith
      · have h6 : ε * qf (d k) v ≤ ε' * qf (d k) v := mul_le_mul_of_nonpos_right hε'ε h5.le
        linarith
  have hlt : ∑ l, t l ≤ ∑ l, decW t k ε' l := isMinOn_iff.mp hmin _ hdecF
  rw [sum_decW] at hlt
  linarith

/-! ### §F — the engine: self-duality from the local condition -/

theorem mem_surgery_single {ι : Type*} [Fintype ι] [DecidableEq ι] (d : ι → Matrix n n ℂ)
    (j : ι) : d j ∈ surgery d := by
  obtain ⟨t, ht⟩ : ∃ t : ι → ℝ, t = (Pi.single j (1 : ℝ) : ι → ℝ) := ⟨_, rfl⟩
  have htj : t j = 1 := by
    rw [ht, Pi.single_eq_same]
  have htk : ∀ k, k ≠ j → t k = 0 := fun k hk => by
    rw [ht, Pi.single_eq_of_ne hk]
  have hsum : ∑ k, (t k : ℂ) • d k = d j := by
    rw [Finset.sum_eq_single j]
    · rw [htj, Complex.ofReal_one, one_smul]
    · intro k _ hk
      rw [htk k hk, Complex.ofReal_zero, zero_smul]
    · intro h
      exact absurd (Finset.mem_univ j) h
  refine ⟨0, t, Matrix.PosSemidef.zero, fun k => le_of_eq (pr_zero_left (d k)).symm,
    fun k => ?_, ?_⟩
  · by_cases hk : k = j
    · rw [hk, htj]
      exact zero_le_one
    · exact le_of_eq (htk k hk).symm
  · rw [zero_add, hsum]

theorem isClosed_dualH (S : Set (Matrix n n ℂ)) : IsClosed (dualH S) := by
  have h1 : dualH S = {B : Matrix n n ℂ | Bᴴ = B} ∩ ⋂ A ∈ S, {B : Matrix n n ℂ | 0 ≤ pr A B} := by
    ext B
    simp only [dualH, Set.mem_setOf_eq, Set.mem_inter_iff, Set.mem_iInter, Matrix.IsHermitian]
  have hH : IsClosed {B : Matrix n n ℂ | Bᴴ = B} :=
    isClosed_eq continuous_id.matrix_conjTranspose continuous_id
  have hP : IsClosed (⋂ A ∈ S, {B : Matrix n n ℂ | 0 ≤ pr A B}) := by
    refine isClosed_biInter fun A _ => isClosed_le continuous_const ?_
    have h2 : Continuous fun B : Matrix n n ℂ => A * B := continuous_const.matrix_mul continuous_id
    exact Complex.continuous_re.comp h2.matrix_trace
  rw [h1]
  exact hH.inter hP

set_option maxHeartbeats 800000 in
/-- **The engine.** For a finite family of Hermitian `d k` with `pr 1 (d k) > 0` and pairwise
nonnegative pairings, the local condition ("if `u† d_j u < 0` then `d_k` is positive definite on
`u^⊥` whenever `k = j` or `pr (d k) (d j) > 0`") makes `surgery d` self-dual and closed. -/
theorem selfDual_of_local {ι : Type*} [Fintype ι] [DecidableEq ι] (d : ι → Matrix n n ℂ)
    (hd : ∀ k, (d k).IsHermitian) (htr : ∀ k, 0 < pr 1 (d k))
    (hpair : ∀ j k, 0 ≤ pr (d j) (d k))
    (hloc : ∀ j k, (k = j ∨ 0 < pr (d k) (d j)) → ∀ u : n → ℂ, qf (d j) u < 0 →
      ∀ x : n → ℂ, x ≠ 0 → star u ⬝ᵥ x = 0 → 0 < qf (d k) x) :
    surgery d = dualH (surgery d) ∧ IsClosed (surgery d) := by
  have hK : surgery d = dualH (surgery d) := by
    apply Set.Subset.antisymm
    · intro A hA
      obtain ⟨q, t, hq, hqd, ht, rfl⟩ := hA
      refine ⟨hq.isHermitian.add (isHermitian_sum_smul d hd t), ?_⟩
      intro B hB
      obtain ⟨q', t', hq', hq'd, ht', rfl⟩ := hB
      have e1 : pr q' (q + ∑ k, (t k : ℂ) • d k) = pr q' q + ∑ k, t k * pr q' (d k) := by
        rw [pr_add_right, pr_sum_right,
          Finset.sum_congr rfl fun k _ => pr_smul_right (t k) q' (d k)]
      have e2 : ∀ l, pr ((t' l : ℂ) • d l) (q + ∑ k, (t k : ℂ) • d k) =
          t' l * (pr (d l) q + ∑ k, t k * pr (d l) (d k)) := by
        intro l
        rw [pr_smul_left, pr_add_right, pr_sum_right,
          Finset.sum_congr rfl fun k _ => pr_smul_right (t k) (d l) (d k)]
      rw [pr_add_left, pr_sum_left, e1, Finset.sum_congr rfl fun l _ => e2 l]
      have h1 : 0 ≤ pr q' q := pr_psd_psd hq' hq
      have h2 : 0 ≤ ∑ k, t k * pr q' (d k) :=
        Finset.sum_nonneg fun k _ => mul_nonneg (ht k) (hq'd k)
      have h3 : 0 ≤ ∑ l, t' l * (pr (d l) q + ∑ k, t k * pr (d l) (d k)) :=
        Finset.sum_nonneg fun l _ => mul_nonneg (ht' l)
          (add_nonneg (le_of_le_of_eq (hqd l) (pr_comm _ _))
            (Finset.sum_nonneg fun k _ => mul_nonneg (ht k) (hpair l k)))
      exact add_nonneg (add_nonneg h1 h2) h3
    · intro y hy
      obtain ⟨hyH, hyK⟩ := hy
      have hdual : ∀ x : Matrix n n ℂ, x.PosSemidef → (∀ k, 0 ≤ pr x (d k)) → 0 ≤ pr x y :=
        fun x hx hxk => hyK x ⟨x, 0, hx, hxk, fun _ => le_refl 0, by simp⟩
      obtain ⟨s, hs, hys⟩ := exists_psd_sub d hd htr hyH hdual
      have hyd : ∀ j, 0 ≤ pr y (d j) := fun j =>
        le_of_le_of_eq (hyK (d j) (mem_surgery_single d j)) (pr_comm _ _)
      obtain ⟨t, ht, hq, hqd⟩ := exists_decomp d hd htr hpair hloc hyH hyd hs hys
      exact ⟨y - ∑ k, (t k : ℂ) • d k, t, hq, hqd, ht, by rw [sub_add_cancel]⟩
  refine ⟨hK, ?_⟩
  rw [hK]
  exact isClosed_dualH _

/-! ### §G — Theorem S′ for rank-one defects -/

set_option maxHeartbeats 800000 in
/-- **Bessel** for two orthogonal nonzero vectors `u ⊥ x`:
`|⟨u|h⟩|² |x|² + |⟨x|h⟩|² |u|² ≤ |h|² |u|² |x|²`. -/
theorem bessel_two {u x : n → ℂ} (hu : u ≠ 0) (hx : x ≠ 0) (hux : ip u x = 0) (h : n → ℂ) :
    Complex.normSq (ip u h) * (ip x x).re + Complex.normSq (ip x h) * (ip u u).re
      ≤ (ip h h).re * (ip u u).re * (ip x x).re := by
  obtain ⟨U, hU⟩ : ∃ U : ℝ, ip u u = (U : ℂ) := ⟨_, ip_self_ofReal u⟩
  obtain ⟨X, hX⟩ : ∃ X : ℝ, ip x x = (X : ℂ) := ⟨_, ip_self_ofReal x⟩
  obtain ⟨H, hH⟩ : ∃ H : ℝ, ip h h = (H : ℂ) := ⟨_, ip_self_ofReal h⟩
  obtain ⟨a, ha⟩ : ∃ a : ℂ, ip u h = a := ⟨_, rfl⟩
  obtain ⟨b, hb⟩ : ∃ b : ℂ, ip x h = b := ⟨_, rfl⟩
  have hUpos : 0 < U := by
    have h1 := ip_self_re_pos hu
    rwa [hU, Complex.ofReal_re] at h1
  have hXpos : 0 < X := by
    have h1 := ip_self_re_pos hx
    rwa [hX, Complex.ofReal_re] at h1
  have hxu : ip x u = 0 := by rw [ip_swap, hux, star_zero]
  obtain ⟨w, hw⟩ : ∃ w : n → ℂ, w = ((U * X : ℝ) : ℂ) • h - ((X : ℂ) * a) • u - ((U : ℂ) * b) • x :=
    ⟨_, rfl⟩
  have hwu : ip w u = 0 := by
    rw [hw, ip_sub_left, ip_sub_left, ip_smul_left, ip_smul_left, ip_smul_left, ip_swap u h, ha,
      hU, hxu, Complex.ofReal_mul]
    simp only [star_mul', star_ofReal']
    ring
  have hwx : ip w x = 0 := by
    rw [hw, ip_sub_left, ip_sub_left, ip_smul_left, ip_smul_left, ip_smul_left, ip_swap x h, hb,
      hux, hX, Complex.ofReal_mul]
    simp only [star_mul', star_ofReal']
    ring
  have hwh : ip w h = ((U * X * H - X * Complex.normSq a - U * Complex.normSq b : ℝ) : ℂ) := by
    have e1 : (X : ℂ) * star a * a = X * (Complex.normSq a : ℂ) := by
      rw [mul_assoc, star_mul_self_eq]
    have e2 : (U : ℂ) * star b * b = U * (Complex.normSq b : ℂ) := by
      rw [mul_assoc, star_mul_self_eq]
    rw [hw, ip_sub_left, ip_sub_left, ip_smul_left, ip_smul_left, ip_smul_left, hH, ha, hb]
    simp only [star_mul', star_ofReal']
    rw [e1, e2]
    first
      | (push_cast; ring)
      | push_cast
  have hww : ip w w = ((U * X : ℝ) : ℂ) * ip w h := by
    have h1 : ip w w = ip w (((U * X : ℝ) : ℂ) • h - ((X : ℂ) * a) • u - ((U : ℂ) * b) • x) := by
      rw [← hw]
    rw [h1, ip_sub_right, ip_sub_right, ip_smul_right, ip_smul_right, ip_smul_right, hwu, hwx,
      mul_zero, mul_zero, sub_zero, sub_zero]
  have hre : 0 ≤ (ip w w).re := ip_self_re_nonneg w
  rw [hww, hwh, ← Complex.ofReal_mul, Complex.ofReal_re] at hre
  have hUX : 0 < U * X := mul_pos hUpos hXpos
  have hY : 0 ≤ U * X * H - X * Complex.normSq a - U * Complex.normSq b := by
    by_contra hneg
    push_neg at hneg
    have h1 := mul_neg_of_pos_of_neg hUX hneg
    linarith
  rw [ha, hb, hU, hX, hH]
  simp only [Complex.ofReal_re]
  linarith

/-- On the orthogonal complement of a vector `u` of the open co-cap of `defect c h`, the defect is
positive definite. -/
theorem qf_defect_pos_of_perp {c : ℝ} {h u x : n → ℂ} (hh : ip h h = 1) (hc : 1 < c)
    (hu : u ≠ 0) (hx : x ≠ 0) (hux : ip u x = 0)
    (hco : (c - 1) * (ip u u).re < c * Complex.normSq (ip h u)) :
    0 < qf (defect c h) x := by
  have hb := bessel_two hu hx hux h
  have hH1 : (ip h h).re = 1 := by rw [hh, Complex.one_re]
  rw [hH1, normSq_ip_swap h u, normSq_ip_swap h x] at hb
  have hU : 0 < (ip u u).re := ip_self_re_pos hu
  have hX : 0 < (ip x x).re := ip_self_re_pos hx
  have h1 : c * (Complex.normSq (ip h x) * (ip u u).re) ≤
      c * ((ip u u).re * (ip x x).re - Complex.normSq (ip h u) * (ip x x).re) :=
    mul_le_mul_of_nonneg_left (by linarith) (by linarith)
  have h2 : (c - 1) * (ip u u).re * (ip x x).re < c * Complex.normSq (ip h u) * (ip x x).re :=
    mul_lt_mul_of_pos_right hco hX
  have h3 : c * Complex.normSq (ip h x) * (ip u u).re < (ip x x).re * (ip u u).re := by
    linarith
  have h4 : c * Complex.normSq (ip h x) < (ip x x).re := lt_of_mul_lt_mul_right h3 hU.le
  rw [qf_defect]
  linarith

/-- **Theorem S′** (finite form). -/
theorem theorem_Sprime {ι : Type*} [Fintype ι] [DecidableEq ι] (c : ι → ℝ) (h : ι → n → ℂ)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hcard : ∀ k, c k < Fintype.card n)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      ∀ v : n → ℂ, (star v ⬝ᵥ v).re < c j * Complex.normSq (star (h j) ⬝ᵥ v) →
        (c k - 1) * (star v ⬝ᵥ v).re < c k * Complex.normSq (star (h k) ⬝ᵥ v)) :
    surgery (fun k => defect (c k) (h k)) = dualH (surgery (fun k => defect (c k) (h k))) ∧
      IsClosed (surgery (fun k => defect (c k) (h k))) := by
  have hloc : ∀ j k, (k = j ∨ 0 < pr (defect (c k) (h k)) (defect (c j) (h j))) →
      ∀ u : n → ℂ, qf (defect (c j) (h j)) u < 0 →
      ∀ x : n → ℂ, x ≠ 0 → star u ⬝ᵥ x = 0 → 0 < qf (defect (c k) (h k)) x := by
    intro j k hkj u hu x hx hux
    have hu0 : u ≠ 0 := by
      intro h0
      rw [h0, qf_zero] at hu
      exact lt_irrefl 0 hu
    have hcap : (ip u u).re < c j * Complex.normSq (ip (h j) u) := by
      rw [qf_defect] at hu
      linarith
    have hco : (c k - 1) * (ip u u).re < c k * Complex.normSq (ip (h k) u) := by
      by_cases hkj' : k = j
      · rw [hkj']
        have hU := ip_self_re_nonneg u
        linarith [mul_nonneg (sub_nonneg.mpr (hc j).2) hU]
      · rcases hkj with hkj | hkj
        · exact absurd hkj hkj'
        · exact hCC j k (Ne.symm hkj') (lt_of_lt_of_eq hkj (pr_comm _ _)) u hcap
    exact qf_defect_pos_of_perp (hunit k) (hc k).1 hu0 hx hux hco
  exact selfDual_of_local (fun k => defect (c k) (h k)) (fun k => defect_isHermitian _ _)
    (fun k => show 0 < pr 1 (defect (c k) (h k)) by
      rw [pr_one_defect _ _ (hunit k)]
      linarith [hcard k])
    hpair hloc

/-! ### §H — condition (CC) in inequality form; the two-defect case -/

/-- The component of `v` orthogonal to a unit vector `h`. -/
theorem ip_perp {h : n → ℂ} (hh : ip h h = 1) (v : n → ℂ) : ip h (v - (ip h v) • h) = 0 := by
  rw [ip_sub_right, ip_smul_right, hh, mul_one, sub_self]

theorem ip_perp_self {h : n → ℂ} (hh : ip h h = 1) (v : n → ℂ) :
    (ip (v - (ip h v) • h) (v - (ip h v) • h)).re = (ip v v).re - Complex.normSq (ip h v) := by
  have h1 : ip (v - (ip h v) • h) h = 0 := by
    rw [ip_swap h (v - (ip h v) • h), ip_perp hh v, star_zero]
  have h2 : ip (v - (ip h v) • h) (v - (ip h v) • h) = ip (v - (ip h v) • h) v := by
    conv_lhs => rw [ip_sub_right, ip_smul_right]
    rw [h1, mul_zero, sub_zero]
  rw [h2, ip_sub_left, ip_smul_left, Complex.sub_re, star_mul_self_eq, Complex.ofReal_re]

set_option maxHeartbeats 800000 in
/-- **The real core of (CC).** With `A = |⟨h|v⟩|`, `G = |⟨h'|h⟩|`, `b = |⟨h'|v⟩|`, `V = |v|²`:
the open cap of `1 − c h h†` lies in the open co-cap of `1 − c' h' h'†` when
`(√(c − 1) + √(c' − 1))² ≤ c c' G²`. -/
theorem capcocap_real {c c' A G b V : ℝ} (hc : 1 < c ∧ c ≤ 2) (hc' : 1 < c' ∧ c' ≤ 2)
    (hA : 0 ≤ A) (hG : 0 ≤ G) (hG1 : G ≤ 1) (hV : 0 < V)
    (hcap : V < c * A ^ 2) (hgram : (b - A * G) ^ 2 ≤ (1 - G ^ 2) * (V - A ^ 2))
    (hCC : (Real.sqrt (c - 1) + Real.sqrt (c' - 1)) ^ 2 ≤ c * c' * G ^ 2) :
    (c' - 1) * V < c' * b ^ 2 := by
  obtain ⟨hc1, hc2⟩ := hc
  obtain ⟨hc1', hc2'⟩ := hc'
  obtain ⟨R, hR0, hR2, hRdef⟩ : ∃ R : ℝ, 0 ≤ R ∧ R ^ 2 = c - 1 ∧ R = Real.sqrt (c - 1) :=
    ⟨Real.sqrt (c - 1), Real.sqrt_nonneg _, Real.sq_sqrt (by linarith), rfl⟩
  obtain ⟨R', hR'0, hR'2, hR'def⟩ :
      ∃ R' : ℝ, 0 ≤ R' ∧ R' ^ 2 = c' - 1 ∧ R' = Real.sqrt (c' - 1) :=
    ⟨Real.sqrt (c' - 1), Real.sqrt_nonneg _, Real.sq_sqrt (by linarith), rfl⟩
  obtain ⟨K, hK0, hK2⟩ : ∃ K : ℝ, 0 < K ∧ K ^ 2 = c :=
    ⟨Real.sqrt c, Real.sqrt_pos.mpr (by linarith), Real.sq_sqrt (by linarith)⟩
  obtain ⟨K', hK'0, hK'2⟩ : ∃ K' : ℝ, 0 < K' ∧ K' ^ 2 = c' :=
    ⟨Real.sqrt c', Real.sqrt_pos.mpr (by linarith), Real.sq_sqrt (by linarith)⟩
  obtain ⟨p, hp0, hp2⟩ : ∃ p : ℝ, 0 < p ∧ p ^ 2 = V :=
    ⟨Real.sqrt V, Real.sqrt_pos.mpr hV, Real.sq_sqrt hV.le⟩
  rw [← hRdef, ← hR'def] at hCC
  have hRpos : 0 < R := by
    rw [hRdef]
    exact Real.sqrt_pos.mpr (by linarith)
  have hR1 : R ≤ 1 :=
    le_of_pow_le_pow_left₀ two_ne_zero zero_le_one (by rw [one_pow, hR2]; linarith)
  have hR'1 : R' ≤ 1 :=
    le_of_pow_le_pow_left₀ two_ne_zero zero_le_one (by rw [one_pow, hR'2]; linarith)
  -- the cap and (CC) without squares
  have hKA : 0 ≤ K * A := mul_nonneg hK0.le hA
  have hcap' : p < K * A := by
    have h1 : p ^ 2 < (K * A) ^ 2 := by
      rw [mul_pow, hK2, hp2]
      exact hcap
    exact lt_of_pow_lt_pow_left₀ 2 hKA h1
  have hKKG : 0 ≤ K * K' * G := mul_nonneg (mul_nonneg hK0.le hK'0.le) hG
  have hCC' : R + R' ≤ K * K' * G := by
    have h1 : (R + R') ^ 2 ≤ (K * K' * G) ^ 2 := by
      rw [mul_pow, mul_pow, hK2, hK'2]
      exact hCC
    exact le_of_pow_le_pow_left₀ two_ne_zero hKKG h1
  -- (P1) `R' p < K' A G`
  have hRR' : R * R' ≤ 1 := by
    have h1 := mul_le_mul hR1 hR'1 hR'0 zero_le_one
    linarith
  have h2 : c * R' ≤ R + R' := by
    have hc_eq : c = R ^ 2 + 1 := by linarith
    rw [hc_eq]
    have h3 := mul_le_mul_of_nonneg_left hRR' hRpos.le
    linarith
  have hP1 : R' * p < K' * A * G := by
    have h1 : p * (R + R') < (K * A) * (K * K' * G) :=
      calc p * (R + R') < (K * A) * (R + R') := mul_lt_mul_of_pos_right hcap' (by linarith)
        _ ≤ (K * A) * (K * K' * G) := mul_le_mul_of_nonneg_left hCC' hKA
    have h3 : (K * A) * (K * K' * G) = c * (K' * A * G) := by
      rw [← hK2]
      ring
    have h4 : c * (R' * p) ≤ p * (R + R') := by
      have h6 := mul_le_mul_of_nonneg_right h2 hp0.le
      linarith
    have h5 : c * (R' * p) < c * (K' * A * G) := by linarith
    exact lt_of_mul_lt_mul_left h5 (by linarith)
  -- (P2) `K'² (1 − G²)(p² − A²) < (K' A G − R' p)²`
  have hKR' : K * R' ≤ K' := by
    have h1 : (K * R') ^ 2 ≤ K' ^ 2 := by
      rw [mul_pow, hK2, hR'2, hK'2]
      have h3 := mul_le_mul_of_nonneg_left (show c' - 1 ≤ 1 by linarith)
        (show (0 : ℝ) ≤ c - 1 by linarith)
      linarith
    exact le_of_pow_le_pow_left₀ two_ne_zero hK'0.le h1
  have e1 : 0 < K * A - p := by linarith
  have e2 : 0 < K * K' * A + K' * p - 2 * K * R' * p * G := by
    have h5 : 0 < K' * (K * A - p) := mul_pos hK'0 e1
    have h6 : K * R' * G ≤ K' :=
      le_trans (mul_le_of_le_one_right (mul_nonneg hK0.le hR'0) hG1) hKR'
    have h7 : 0 ≤ p * (K' - K * R' * G) := mul_nonneg hp0.le (by linarith)
    linarith
  have e3 : 0 ≤ K * K' * G - R - R' := by linarith
  have e4 : 0 < K * K' * G + R - R' := by linarith
  have hid : K ^ 2 * ((K' * A * G - R' * p) ^ 2 - K' ^ 2 * (1 - G ^ 2) * (p ^ 2 - A ^ 2)) =
      K' * (K * A - p) * (K * K' * A + K' * p - 2 * K * R' * p * G) +
        p ^ 2 * (K * K' * G - R - R') * (K * K' * G + R - R') := by
    have e5 : K ^ 2 = 1 + R ^ 2 := by linarith
    have e6 : K' ^ 2 = 1 + R' ^ 2 := by linarith
    linear_combination (-p ^ 2 * (K' ^ 2 - R' ^ 2)) * e5 + (-R ^ 2 * p ^ 2) * e6
  have hT1 : 0 < K' * (K * A - p) * (K * K' * A + K' * p - 2 * K * R' * p * G) :=
    mul_pos (mul_pos hK'0 e1) e2
  have hT2 : 0 ≤ p ^ 2 * (K * K' * G - R - R') * (K * K' * G + R - R') :=
    mul_nonneg (mul_nonneg (sq_nonneg p) e3) e4.le
  have h8 : 0 < K ^ 2 * ((K' * A * G - R' * p) ^ 2 - K' ^ 2 * (1 - G ^ 2) * (p ^ 2 - A ^ 2)) := by
    rw [hid]
    linarith
  have h9 : 0 < (K' * A * G - R' * p) ^ 2 - K' ^ 2 * (1 - G ^ 2) * (p ^ 2 - A ^ 2) :=
    pos_of_mul_pos_right h8 (sq_nonneg K)
  -- conclusion
  rw [← hp2] at hgram ⊢
  have h10 : K' ^ 2 * (b - A * G) ^ 2 ≤ K' ^ 2 * ((1 - G ^ 2) * (p ^ 2 - A ^ 2)) :=
    mul_le_mul_of_nonneg_left hgram (sq_nonneg K')
  have h11 : (K' * A * G - K' * b) ^ 2 < (K' * A * G - R' * p) ^ 2 := by
    have h12 : (K' * A * G - K' * b) ^ 2 = K' ^ 2 * (b - A * G) ^ 2 := by ring
    rw [h12]
    linarith
  have h13 : R' * p < K' * b := by
    by_contra hcon
    push_neg at hcon
    have h14 : K' * A * G - R' * p ≤ K' * A * G - K' * b := by linarith
    have h15 : (K' * A * G - R' * p) ^ 2 ≤ (K' * A * G - K' * b) ^ 2 :=
      pow_le_pow_left₀ (by linarith) h14 2
    linarith
  have h16 : (R' * p) ^ 2 < (K' * b) ^ 2 :=
    pow_lt_pow_left₀ h13 (mul_nonneg hR'0 hp0.le) two_ne_zero
  rw [mul_pow, mul_pow, hR'2, hK'2] at h16
  linarith

set_option maxHeartbeats 800000 in
/-- **(CC) in inequality form gives cap inside co-cap**: for unit `h, h'` and `c, c' ∈ (1, 2]` with
`(√(c − 1) + √(c' − 1))² ≤ c c' |⟨h|h'⟩|²`, every `v` with `|v|² < c |⟨h|v⟩|²` has
`(c' − 1)|v|² < c' |⟨h'|v⟩|²`. -/
theorem cap_subset_cocap {c c' : ℝ} {h h' : n → ℂ} (hh : ip h h = 1) (hh' : ip h' h' = 1)
    (hc : 1 < c ∧ c ≤ 2) (hc' : 1 < c' ∧ c' ≤ 2)
    (hCC : (Real.sqrt (c - 1) + Real.sqrt (c' - 1)) ^ 2 ≤ c * c' * Complex.normSq (ip h h'))
    (v : n → ℂ) (hcap : (ip v v).re < c * Complex.normSq (ip h v)) :
    (c' - 1) * (ip v v).re < c' * Complex.normSq (ip h' v) := by
  have hv : v ≠ 0 := by
    intro h0
    rw [h0, ip_zero_left, ip_zero_right, Complex.zero_re, Complex.normSq_zero, mul_zero] at hcap
    exact lt_irrefl 0 hcap
  have hh0 : h ≠ 0 := by
    intro h0
    rw [h0, ip_zero_left] at hh
    exact zero_ne_one hh
  have hperp : ip h (v - (ip h v) • h) = 0 := ip_perp hh v
  have hW : (ip (v - (ip h v) • h) (v - (ip h v) • h)).re =
      (ip v v).re - Complex.normSq (ip h v) := ip_perp_self hh v
  have hdiff : ip h' v - ip h v * ip h' h = ip h' (v - (ip h v) • h) := by
    rw [ip_sub_right, ip_smul_right]
  have hG1sq : Complex.normSq (ip h' h) ≤ 1 := by
    have h1 := ip_self_re_nonneg (h' - (ip h h') • h)
    rw [ip_perp_self hh h', hh', Complex.one_re] at h1
    rw [← normSq_ip_swap h' h]
    linarith
  have hbessel : Complex.normSq (ip h' (v - (ip h v) • h)) ≤
      (1 - Complex.normSq (ip h' h)) * ((ip v v).re - Complex.normSq (ip h v)) := by
    by_cases hw0 : v - (ip h v) • h = 0
    · have h1 : (ip v v).re - Complex.normSq (ip h v) = 0 := by
        rw [← hW, hw0, ip_zero_left, Complex.zero_re]
      have h2 : Complex.normSq (ip h' (v - (ip h v) • h)) = 0 := by
        rw [hw0, ip_zero_right, Complex.normSq_zero]
      exact le_of_eq (by rw [h1, h2, mul_zero])
    · have hb := bessel_two hh0 hw0 hperp h'
      have e1 : (ip h h).re = 1 := by rw [hh, Complex.one_re]
      have e2 : (ip h' h').re = 1 := by rw [hh', Complex.one_re]
      rw [e1, e2, hW, normSq_ip_swap h' (v - (ip h v) • h), normSq_ip_swap h' h] at hb
      linarith [hb]
  have hG1 : ‖ip h' h‖ ≤ 1 := by
    refine le_of_pow_le_pow_left₀ two_ne_zero zero_le_one ?_
    rw [one_pow, Complex.sq_norm]
    exact hG1sq
  have hgram : (‖ip h' v‖ - ‖ip h v‖ * ‖ip h' h‖) ^ 2 ≤
      (1 - ‖ip h' h‖ ^ 2) * ((ip v v).re - ‖ip h v‖ ^ 2) := by
    have h1 : |‖ip h' v‖ - ‖ip h v * ip h' h‖| ≤ ‖ip h' v - ip h v * ip h' h‖ :=
      abs_norm_sub_norm_le _ _
    rw [norm_mul, hdiff] at h1
    have h2 : (‖ip h' v‖ - ‖ip h v‖ * ‖ip h' h‖) ^ 2 ≤ ‖ip h' (v - (ip h v) • h)‖ ^ 2 := by
      rw [← sq_abs (‖ip h' v‖ - ‖ip h v‖ * ‖ip h' h‖)]
      exact pow_le_pow_left₀ (abs_nonneg _) h1 2
    calc (‖ip h' v‖ - ‖ip h v‖ * ‖ip h' h‖) ^ 2 ≤ ‖ip h' (v - (ip h v) • h)‖ ^ 2 := h2
      _ = Complex.normSq (ip h' (v - (ip h v) • h)) := Complex.sq_norm _
      _ ≤ (1 - Complex.normSq (ip h' h)) * ((ip v v).re - Complex.normSq (ip h v)) := hbessel
      _ = (1 - ‖ip h' h‖ ^ 2) * ((ip v v).re - ‖ip h v‖ ^ 2) := by
        rw [Complex.sq_norm, Complex.sq_norm]
  have hCC' : (Real.sqrt (c - 1) + Real.sqrt (c' - 1)) ^ 2 ≤ c * c' * ‖ip h' h‖ ^ 2 := by
    rw [Complex.sq_norm, ← normSq_ip_swap h' h]
    exact hCC
  have hcap' : (ip v v).re < c * ‖ip h v‖ ^ 2 := by
    rw [Complex.sq_norm]
    exact hcap
  have hfin := capcocap_real hc hc' (norm_nonneg _) (norm_nonneg _) hG1 (ip_self_re_pos hv)
    hcap' hgram hCC'
  rw [Complex.sq_norm] at hfin
  exact hfin

/-- **Theorem S′ with (CC) in inequality form.** -/
theorem theorem_Sprime_ineq {ι : Type*} [Fintype ι] [DecidableEq ι] (c : ι → ℝ)
    (h : ι → n → ℂ)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hcard : ∀ k, c k < Fintype.card n)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      (Real.sqrt (c j - 1) + Real.sqrt (c k - 1)) ^ 2 ≤
        c j * c k * Complex.normSq (star (h j) ⬝ᵥ h k)) :
    surgery (fun k => defect (c k) (h k)) = dualH (surgery (fun k => defect (c k) (h k))) ∧
      IsClosed (surgery (fun k => defect (c k) (h k))) :=
  theorem_Sprime c h hunit hc hcard hpair fun j k hjk hp v hv =>
    cap_subset_cocap (hunit j) (hunit k) (hc j) (hc k) (hCC j k hjk hp) v hv

/-- **Theorem S′ on `ℂ⁴`**, in the words of the thread's NOTES-C11: unit `h k`, `c k ∈ (1, 2]`,
nonnegative pairings and (CC) give a closed self-dual surgery cone (the hypothesis `c k < card n`
of `theorem_Sprime` is automatic here). -/
theorem theorem_Sprime_C4 {ι : Type*} [Fintype ι] [DecidableEq ι] (c : ι → ℝ)
    (h : ι → Fin 2 × Fin 2 → ℂ)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hpair : ∀ j k, 0 ≤ pr (defect (c j) (h j)) (defect (c k) (h k)))
    (hCC : ∀ j k, j ≠ k → 0 < pr (defect (c j) (h j)) (defect (c k) (h k)) →
      ∀ v : Fin 2 × Fin 2 → ℂ, (star v ⬝ᵥ v).re < c j * Complex.normSq (star (h j) ⬝ᵥ v) →
        (c k - 1) * (star v ⬝ᵥ v).re < c k * Complex.normSq (star (h k) ⬝ᵥ v)) :
    surgery (fun k => defect (c k) (h k)) = dualH (surgery (fun k => defect (c k) (h k))) ∧
      IsClosed (surgery (fun k => defect (c k) (h k))) := by
  have h4 : (Fintype.card (Fin 2 × Fin 2) : ℝ) = 4 := by norm_num [Fintype.card_prod]
  refine theorem_Sprime c h hunit hc (fun k => ?_) hpair hCC
  rw [h4]
  linarith [(hc k).2]

/-- The pairing of a rank-one projector with a matrix: `tr(v v† D) = v† D v`. -/
theorem pr_vecMulVec (D : Matrix n n ℂ) (v : n → ℂ) :
    pr (Matrix.vecMulVec v (star v)) D = qf D v := by
  rw [pr_comm]
  unfold pr qf
  rw [JordanClassification.trace_mul_vecMulVec]

/-- The pairing of two rank-one defects:
`tr((1 − c h h†)(1 − c' h' h'†)) = card n − c − c' + c c' |⟨h|h'⟩|²` for unit `h, h'`. -/
theorem pr_defect_defect (c c' : ℝ) (h h' : n → ℂ) (hh : ip h h = 1) (hh' : ip h' h' = 1) :
    pr (defect c h) (defect c' h') =
      (Fintype.card n : ℝ) - c - c' + c * c' * Complex.normSq (ip h h') := by
  have e1 : defect c h = 1 - (c : ℂ) • Matrix.vecMulVec h (star h) := rfl
  rw [e1, pr_sub_left, pr_smul_left, pr_one_defect c' h' hh', pr_vecMulVec, qf_defect, hh,
    Complex.one_re, normSq_ip_swap h h']
  ring

/-- **The two-defect case on `ℂ⁴`** — the sufficiency half of the pair theorem C12-P: for
`c 0, c 1 ∈ (1, 2]` and unit `h 0, h 1`, if `pr (d 0) (d 1) = 0` or
`(√(c 0 − 1) + √(c 1 − 1))² ≤ c 0 c 1 |⟨h 0|h 1⟩|²`, then K({d 0, d 1}) is self-dual and closed. The
pairing `pr (d 0) (d 1) ≥ 0` is derived (`pr_defect_defect`), not assumed. -/
theorem twoDefect (c : Fin 2 → ℝ) (h : Fin 2 → Fin 2 × Fin 2 → ℂ)
    (hunit : ∀ k, star (h k) ⬝ᵥ h k = 1)
    (hc : ∀ k, 1 < c k ∧ c k ≤ 2)
    (hCC : pr (defect (c 0) (h 0)) (defect (c 1) (h 1)) = 0 ∨
      (Real.sqrt (c 0 - 1) + Real.sqrt (c 1 - 1)) ^ 2 ≤
        c 0 * c 1 * Complex.normSq (star (h 0) ⬝ᵥ h 1)) :
    surgery (fun k => defect (c k) (h k)) = dualH (surgery (fun k => defect (c k) (h k))) ∧
      IsClosed (surgery (fun k => defect (c k) (h k))) := by
  have h4 : (Fintype.card (Fin 2 × Fin 2) : ℝ) = 4 := by norm_num [Fintype.card_prod]
  have hpair : 0 ≤ pr (defect (c 0) (h 0)) (defect (c 1) (h 1)) := by
    rw [pr_defect_defect (c 0) (c 1) (h 0) (h 1) (hunit 0) (hunit 1), h4]
    have hs := Complex.normSq_nonneg (ip (h 0) (h 1))
    have h5 : 0 ≤ c 0 * c 1 * Complex.normSq (ip (h 0) (h 1)) :=
      mul_nonneg (mul_nonneg (by linarith [(hc 0).1]) (by linarith [(hc 1).1])) hs
    linarith [(hc 0).2, (hc 1).2]
  refine theorem_Sprime_ineq c h hunit hc (fun k => ?_) ?_ ?_
  · rw [h4]
    linarith [(hc k).2]
  · refine Fin.forall_fin_two.mpr ⟨Fin.forall_fin_two.mpr ⟨?_, hpair⟩,
      Fin.forall_fin_two.mpr ⟨?_, ?_⟩⟩
    · exact pr_self_nonneg (defect_isHermitian _ _)
    · exact le_of_le_of_eq hpair (pr_comm _ _)
    · exact pr_self_nonneg (defect_isHermitian _ _)
  · refine Fin.forall_fin_two.mpr ⟨Fin.forall_fin_two.mpr ⟨fun h00 => absurd rfl h00,
      fun _ hp => hCC.resolve_left hp.ne'⟩,
      Fin.forall_fin_two.mpr ⟨fun _ hp => ?_, fun h11 => absurd rfl h11⟩⟩
    rw [add_comm, mul_comm (c 1) (c 0), normSq_dot_swap (h 0) (h 1)]
    exact hCC.resolve_left (lt_of_lt_of_eq hp (pr_comm _ _)).ne'

/-! ### §I — control -/

/-- **Non-vacuity control.** The single defect `1 − (3/2)|e⟩⟨e|` on `ℂ⁴` (`e` the first basis
vector; eigenvalue `−1/2`) satisfies the hypotheses of Theorem S′: its surgery cone is self-dual
and closed. -/
theorem control_single_defect :
    surgery (fun _ : Unit => defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ))) =
        dualH (surgery (fun _ : Unit =>
          defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ)))) ∧
      IsClosed (surgery (fun _ : Unit =>
        defect (3 / 2) (Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ)))) :=
  theorem_Sprime (fun _ => 3 / 2) (fun _ => Pi.single ((0 : Fin 2), (0 : Fin 2)) (1 : ℂ))
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

#print axioms OIBridge.CmSprime.pr
#print axioms OIBridge.CmSprime.ip
#print axioms OIBridge.CmSprime.qf
#print axioms OIBridge.CmSprime.defect
#print axioms OIBridge.CmSprime.dualH
#print axioms OIBridge.CmSprime.surgery
#print axioms OIBridge.CmSprime.pr_comm
#print axioms OIBridge.CmSprime.pr_add_left
#print axioms OIBridge.CmSprime.pr_add_right
#print axioms OIBridge.CmSprime.pr_sub_right
#print axioms OIBridge.CmSprime.pr_sub_left
#print axioms OIBridge.CmSprime.pr_smul_left
#print axioms OIBridge.CmSprime.pr_smul_right
#print axioms OIBridge.CmSprime.pr_sum_left
#print axioms OIBridge.CmSprime.pr_sum_right
#print axioms OIBridge.CmSprime.pr_zero_left
#print axioms OIBridge.CmSprime.star_ofReal'
#print axioms OIBridge.CmSprime.isSelfAdjoint_ofReal
#print axioms OIBridge.CmSprime.star_mul_self_eq
#print axioms OIBridge.CmSprime.trace_mul_real
#print axioms OIBridge.CmSprime.defect_isHermitian
#print axioms OIBridge.CmSprime.isHermitian_sum_smul
#print axioms OIBridge.CmSprime.qf_zero
#print axioms OIBridge.CmSprime.qf_nonneg_of_psd
#print axioms OIBridge.CmSprime.psd_of_qf
#print axioms OIBridge.CmSprime.pr_psd_psd
#print axioms OIBridge.CmSprime.pr_self_nonneg
#print axioms OIBridge.CmSprime.psd_of_pr
#print axioms OIBridge.CmSprime.pr_one_defect
#print axioms OIBridge.CmSprime.vecMulVec_mulVec'
#print axioms OIBridge.CmSprime.ip_zero_left
#print axioms OIBridge.CmSprime.ip_zero_right
#print axioms OIBridge.CmSprime.ip_sub_left
#print axioms OIBridge.CmSprime.ip_sub_right
#print axioms OIBridge.CmSprime.ip_smul_left
#print axioms OIBridge.CmSprime.ip_smul_right
#print axioms OIBridge.CmSprime.ip_swap
#print axioms OIBridge.CmSprime.normSq_ip_swap
#print axioms OIBridge.CmSprime.normSq_dot_swap
#print axioms OIBridge.CmSprime.ip_self_ofReal
#print axioms OIBridge.CmSprime.ip_self_re_pos
#print axioms OIBridge.CmSprime.ip_self_re_nonneg
#print axioms OIBridge.CmSprime.qf_defect
#print axioms OIBridge.CmSprime.qf_sub_sum
#print axioms OIBridge.CmSprime.qf_real_smul
#print axioms OIBridge.CmSprime.continuous_qf
#print axioms OIBridge.CmSprime.qf_mul_conjTranspose
#print axioms OIBridge.CmSprime.pr_mul_conjTranspose
#print axioms OIBridge.CmSprime.ratioSet
#print axioms OIBridge.CmSprime.farkas_one
#print axioms OIBridge.CmSprime.farkas_finset
#print axioms OIBridge.CmSprime.exists_psd_sub
#print axioms OIBridge.CmSprime.exists_qf_add_nonneg
#print axioms OIBridge.CmSprime.decW
#print axioms OIBridge.CmSprime.sum_decW_mul
#print axioms OIBridge.CmSprime.sum_decW
#print axioms OIBridge.CmSprime.feas
#print axioms OIBridge.CmSprime.mem_feas
#print axioms OIBridge.CmSprime.isClosed_feas
#print axioms OIBridge.CmSprime.feas_subset
#print axioms OIBridge.CmSprime.isCompact_feas
#print axioms OIBridge.CmSprime.exists_decomp
#print axioms OIBridge.CmSprime.mem_surgery_single
#print axioms OIBridge.CmSprime.isClosed_dualH
#print axioms OIBridge.CmSprime.selfDual_of_local
#print axioms OIBridge.CmSprime.bessel_two
#print axioms OIBridge.CmSprime.qf_defect_pos_of_perp
#print axioms OIBridge.CmSprime.theorem_Sprime
#print axioms OIBridge.CmSprime.ip_perp
#print axioms OIBridge.CmSprime.ip_perp_self
#print axioms OIBridge.CmSprime.capcocap_real
#print axioms OIBridge.CmSprime.cap_subset_cocap
#print axioms OIBridge.CmSprime.theorem_Sprime_ineq
#print axioms OIBridge.CmSprime.theorem_Sprime_C4
#print axioms OIBridge.CmSprime.pr_vecMulVec
#print axioms OIBridge.CmSprime.pr_defect_defect
#print axioms OIBridge.CmSprime.twoDefect
#print axioms OIBridge.CmSprime.control_single_defect
