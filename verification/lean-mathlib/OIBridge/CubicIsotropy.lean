/-
  OIBridge/CubicIsotropy.lean — [SM] Corollary 1a, cubic symmetry forbids quadratic anisotropy.

      **Corollary 1a.** Suppose a scalar projected kernel is translation invariant and equivariant
      under the full cubic point group O_h.
      (i) If it has finite second absolute moment, then near k = 0 its Fourier symbol has the form
          K̂(k) = a − b|k|² + o(|k|²).
      (ii) If it has finite fourth absolute moment — in particular if it has finite range — the
          remainder sharpens to O(|k|⁴), and that quartic term need not be rotationally invariant.

  THE TWO CLAUSES ARE NOT INTERCHANGEABLE, and the split is why this file exists in this shape.
  A finite second moment gives the quadratic expansion with an `o(|k|²)` remainder and nothing
  better: a symmetric kernel can have finite second moment and infinite fourth moment, and its
  remainder is then nonanalytic between quadratic and quartic order. The manuscript previously
  stated the corollary with an `O(|k|⁴)` remainder under the second-moment hypothesis alone; the
  formalization is what surfaced that, and the statement above is the repaired one.

  FOUR LAYERS, kept separate so that no one of them can stand in for another.

  * ALGEBRAIC CORE. `Sym²(ℝ³)^{O_h}` is one-dimensional: every `O_h`-invariant symmetric bilinear
    form on ℝ³ is a multiple of `δ`. This is the "forbids anisotropy" content and it is pure
    invariant theory — no analysis, no moments, no kernel.
  * KERNEL TO MOMENT TENSOR. `O_h`-equivariance of the KERNEL gives `O_h`-invariance of its SECOND
    MOMENT `Q_ij = Σ_v K(v) v_i v_j`. Without this step the algebraic core would be a theorem about
    a hypothesis the corollary never states, so it is proved rather than left implicit. Inversion
    evenness belongs here too: it is what reduces the exponential symbol to a cosine series, and it
    is derived from the group rather than built into the definition.
  * ANALYTIC BRIDGE. A finite second absolute moment gives the quadratic expansion with an
    `o(|k|²)` remainder. This is where the moment hypothesis is consumed and it is the only place.
  * QUARTIC REFINEMENT. A finite fourth absolute moment sharpens the remainder to `O(|k|⁴)`.

  WHAT IS DELIBERATELY NOT PROVED. The quartic term is NOT rotationally invariant, and the
  companion probe exhibits `k₁⁴ + k₂⁴ + k₃⁴` — an `O_h`-invariant quartic form that is not a
  function of `|k|²` — as the witness. Nothing here derives exact rotational symmetry at any order
  beyond the quadratic, because it is false.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.InnerProductSpace.EuclideanDist
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Analysis.Normed.Group.Tannery
import Mathlib.LinearAlgebra.FiniteDimensional.Defs
import Mathlib.LinearAlgebra.Dimension.Finrank

namespace OIBridge

namespace CubicIsotropy

open Finset Real

set_option linter.unusedSectionVars false

/-! ### The cubic point group, acting on quadratic forms

`O_h` acting on ℝ³ is the group of signed coordinate permutations. Its action on a symmetric
bilinear form `Q` sends `Q i j` to `ε i · ε j · Q (σ i) (σ j)`. Nothing below needs the group
structure — only that the two families of generators, sign flips and coordinate permutations, both
fix `Q`, which is exactly what "equivariant under `O_h`" supplies. -/

/-- A sign assignment on the coordinate axes. -/
def IsSign (ε : Fin 3 → ℝ) : Prop := ∀ i, ε i = 1 ∨ ε i = -1

/-- `Q` is invariant under the full cubic point group: under every signed permutation of the
coordinate axes. -/
def OhInvariant (Q : Fin 3 → Fin 3 → ℝ) : Prop :=
  (∀ ε : Fin 3 → ℝ, IsSign ε → ∀ i j, ε i * ε j * Q i j = Q i j) ∧
    (∀ σ : Equiv.Perm (Fin 3), ∀ i j, Q (σ i) (σ j) = Q i j)

/-- The sign flip on axis `m`. -/
def flip (m : Fin 3) : Fin 3 → ℝ := fun i => if i = m then -1 else 1

theorem isSign_flip (m : Fin 3) : IsSign (flip m) := by
  intro i; unfold flip; split
  · exact Or.inr rfl
  · exact Or.inl rfl

/-- **The algebraic core.** Every `O_h`-invariant symmetric bilinear form on ℝ³ is a multiple of
`δ`: off-diagonal entries are killed by a single sign flip, and the diagonal entries are equated by
the coordinate permutations. This is the whole "forbids quadratic anisotropy" content, and it uses
no analysis whatever. -/
theorem ohInvariant_eq_scalar {Q : Fin 3 → Fin 3 → ℝ} (h : OhInvariant Q) :
    ∀ i j, Q i j = if i = j then Q 0 0 else 0 := by
  obtain ⟨hsign, hperm⟩ := h
  intro i j
  by_cases hij : i = j
  · subst hij
    rw [if_pos rfl]
    -- a permutation carrying `0` to `i` equates the diagonal entries
    have := hperm (Equiv.swap 0 i) 0 0
    simpa using this
  · rw [if_neg hij]
    -- flipping the sign of axis `i` alone negates `Q i j` for `j ≠ i`
    have hf := hsign (flip i) (isSign_flip i) i j
    have h1 : flip i i = -1 := by simp [flip]
    have h2 : flip i j = 1 := by simp [flip, Ne.symm hij]
    rw [h1, h2] at hf
    linarith

/-- The converse: `δ` scaled is `O_h`-invariant, so the invariant space is exactly a line and not
merely contained in one. -/
theorem ohInvariant_scalar (b : ℝ) :
    OhInvariant (fun i j => if i = j then b else 0) := by
  constructor
  · intro ε hε i j
    by_cases hij : i = j
    · subst hij
      rcases hε i with h | h <;> rw [h] <;> ring
    · simp [hij]
  · intro σ i j
    by_cases hij : i = j
    · subst hij; simp
    · simp [hij]

/-- **`dim Sym²(ℝ³)^{O_h} = 1`, in the form the counting layer states it.** An `O_h`-invariant
symmetric form is determined by one real number, and every real number occurs. -/
theorem ohInvariant_iff (Q : Fin 3 → Fin 3 → ℝ) :
    OhInvariant Q ↔ ∃ b : ℝ, Q = fun i j => if i = j then b else 0 := by
  constructor
  · intro h
    exact ⟨Q 0 0, funext fun i => funext fun j => ohInvariant_eq_scalar h i j⟩
  · rintro ⟨b, rfl⟩
    exact ohInvariant_scalar b

/-- The quadratic form an invariant `Q` defines is a multiple of `|k|²` — anisotropy at quadratic
order is impossible. -/
theorem quadratic_isotropic {Q : Fin 3 → Fin 3 → ℝ} (h : OhInvariant Q) (k : Fin 3 → ℝ) :
    ∑ i, ∑ j, Q i j * k i * k j = Q 0 0 * ∑ i, k i ^ 2 := by
  have hQ := ohInvariant_eq_scalar h
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Finset.sum_congr rfl fun j _ => by rw [hQ i j]]
  rw [Finset.sum_eq_single i]
  · simp [sq]; ring
  · intro j _ hj; simp [Ne.symm hj]
  · intro h'; exact absurd (Finset.mem_univ i) h'

/-! ### The quartic order is NOT isotropic

The manuscript is explicit that exact microscopic rotational symmetry is neither assumed nor
obtained, and this is the statement that keeps it honest: at quartic order there are `O_h`-invariant
forms that are not functions of `|k|²`. -/

/-- `k₁⁴ + k₂⁴ + k₃⁴` is invariant under every signed coordinate permutation. -/
theorem quartic_ohInvariant (σ : Equiv.Perm (Fin 3)) (ε : Fin 3 → ℝ) (hε : IsSign ε)
    (k : Fin 3 → ℝ) :
    ∑ i, (ε i * k (σ i)) ^ 4 = ∑ i, k i ^ 4 := by
  have hterm : ∀ i, (ε i * k (σ i)) ^ 4 = k (σ i) ^ 4 := by
    intro i
    rcases hε i with h | h <;> rw [h] <;> ring
  rw [Finset.sum_congr rfl fun i _ => hterm i]
  exact Fintype.sum_equiv σ _ _ fun i => rfl

/-- **The quartic invariant is not rotationally invariant.** Two vectors of the same length give it
different values, so no function of `|k|²` can equal it. This is why the corollary says the quartic
term need not be rotationally invariant, and why nothing above is claimed beyond quadratic order. -/
theorem quartic_not_isotropic :
    ∃ k k' : Fin 3 → ℝ, (∑ i, k i ^ 2) = (∑ i, k' i ^ 2) ∧ (∑ i, k i ^ 4) ≠ ∑ i, k' i ^ 4 := by
  refine ⟨![1, 0, 0], ![Real.sqrt 2 / 2, Real.sqrt 2 / 2, 0], ?_, ?_⟩
  · have h2 : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    simp [Fin.sum_univ_three]
    nlinarith [h2]
  · have h2 : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
    simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
      Matrix.cons_val_two, Matrix.tail_cons]
    intro hc
    nlinarith [h2, Real.sqrt_nonneg 2]

/-! ### The kernel on ℤ³, and the step from its symmetry to the moment tensor's

The algebraic core above starts at `OhInvariant Q`. The manuscript starts one step earlier, at a
translation-invariant kernel equivariant under `O_h`, and getting from there to here is a real step
that must not be left implicit: it is what turns a symmetry of the KERNEL into a symmetry of its
SECOND MOMENT TENSOR. Nothing in this section needs summability — the reindexings are bijections of
`ℤ³` and `tsum` is invariant under them whether or not the family converges. -/

/-- The lattice the kernel lives on. -/
abbrev Site := Fin 3 → ℤ

/-- A site as a real displacement vector. -/
def rvec (v : Site) : Fin 3 → ℝ := fun j => (v j : ℝ)

/-- `|k|²`. -/
def nsq (k : Fin 3 → ℝ) : ℝ := ∑ j, k j ^ 2

/-- `⟨x, k⟩`. -/
def dot (x k : Fin 3 → ℝ) : ℝ := ∑ j, x j * k j

theorem nsq_nonneg (k : Fin 3 → ℝ) : 0 ≤ nsq k :=
  Finset.sum_nonneg fun _ _ => sq_nonneg _

/-- Cauchy–Schwarz, in the form the Taylor bounds use. -/
theorem dot_sq_le (x k : Fin 3 → ℝ) : dot x k ^ 2 ≤ nsq x * nsq k :=
  Finset.sum_mul_sq_le_sq_mul_sq _ _ _

/-- **On the lattice, every nonzero displacement has length at least one.** This is what makes the
second moment control absolute summability, and it is false on ℝ³ — the hypothesis really is about
a lattice kernel. -/
theorem one_le_nsq_rvec {v : Site} (hv : v ≠ 0) : 1 ≤ nsq (rvec v) := by
  obtain ⟨j, hj⟩ : ∃ j, v j ≠ 0 := by
    by_contra hc
    exact hv (funext fun j => not_not.1 (fun h => hc ⟨j, h⟩))
  have hone : (1 : ℝ) ≤ rvec v j ^ 2 := by
    have : (1 : ℤ) ≤ v j ^ 2 := by
      rcases lt_or_gt_of_ne hj with h | h <;> nlinarith
    have := (Int.cast_le (R := ℝ)).2 this
    simpa [rvec] using this
  refine hone.trans (Finset.single_le_sum (f := fun j => rvec v j ^ 2) ?_ (Finset.mem_univ j))
  intro i _; exact sq_nonneg _

/-- Signed permutations act on the lattice: `O_h`. -/
def signEquiv (ε : Fin 3 → ℤ) (hε : ∀ j, ε j = 1 ∨ ε j = -1) : Site ≃ Site where
  toFun w := fun l => ε l * w l
  invFun w := fun l => ε l * w l
  left_inv w := by funext l; rcases hε l with h | h <;> simp [h]
  right_inv w := by funext l; rcases hε l with h | h <;> simp [h]

/-- **The manuscript's hypothesis**: the kernel is equivariant under the full cubic point group. -/
def KernelOh (K : Site → ℝ) : Prop :=
  ∀ (σ : Equiv.Perm (Fin 3)) (ε : Fin 3 → ℤ), (∀ j, ε j = 1 ∨ ε j = -1) →
    ∀ v : Site, K (fun j => ε j * v (σ j)) = K v

/-- Inversion evenness, which `O_h` contains: `K(−v) = K(v)`. It is what makes the Fourier symbol
real and reduces it to a cosine series. -/
theorem kernelOh_neg {K : Site → ℝ} (h : KernelOh K) (v : Site) : K (-v) = K v := by
  have hv : (-v : Site) = fun j => (-1 : ℤ) * v ((Equiv.refl (Fin 3)) j) := by funext j; simp
  rw [hv]
  exact h (Equiv.refl _) (fun _ => -1) (fun _ => Or.inr rfl) v

/-- The second-moment tensor of the kernel. -/
noncomputable def mom2 (K : Site → ℝ) (i j : Fin 3) : ℝ := ∑' v : Site, K v * rvec v i * rvec v j

/-- Off-diagonal moments vanish: a single sign flip negates them. -/
theorem mom2_offdiag {K : Site → ℝ} (h : KernelOh K) {i j : Fin 3} (hij : i ≠ j) :
    mom2 K i j = 0 := by
  classical
  set ε : Fin 3 → ℤ := fun l => if l = i then -1 else 1 with hε
  have hsign : ∀ l, ε l = 1 ∨ ε l = -1 := by
    intro l; simp only [hε]; split
    · exact Or.inr rfl
    · exact Or.inl rfl
  have hKe : ∀ w : Site, K (signEquiv ε hsign w) = K w := by
    intro w
    have := h (Equiv.refl _) ε hsign w
    simpa [signEquiv] using this
  have hkey : mom2 K i j = -mom2 K i j := by
    conv_lhs => rw [mom2, ← (signEquiv ε hsign).tsum_eq
      (fun v : Site => K v * rvec v i * rvec v j)]
    have hterm : ∀ w : Site,
        K (signEquiv ε hsign w) * rvec (signEquiv ε hsign w) i * rvec (signEquiv ε hsign w) j
          = -(K w * rvec w i * rvec w j) := by
      intro w
      have hi : rvec (signEquiv ε hsign w) i = -rvec w i := by
        simp [signEquiv, rvec, hε]
      have hj : rvec (signEquiv ε hsign w) j = rvec w j := by
        simp [signEquiv, rvec, hε, hij.symm]
      rw [hKe w, hi, hj]; ring
    rw [tsum_congr hterm, tsum_neg, mom2]
  linarith

/-- Diagonal moments agree: the coordinate permutations carry one axis to another. -/
theorem mom2_diag {K : Site → ℝ} (h : KernelOh K) (i : Fin 3) : mom2 K i i = mom2 K 0 0 := by
  classical
  set σ : Equiv.Perm (Fin 3) := Equiv.swap 0 i with hσ
  set e : Site ≃ Site := Equiv.arrowCongr σ (Equiv.refl ℤ) with he
  have hKe : ∀ w : Site, K (e w) = K w := by
    intro w
    have h1 := h σ.symm (fun _ => 1) (fun _ => Or.inl rfl) w
    have h2 : (e w) = fun j => (1 : ℤ) * w (σ.symm j) := by
      funext j; simp [he, Equiv.arrowCongr]
    rw [h2]; exact h1
  have hcoord : ∀ (w : Site) (l : Fin 3), rvec (e w) l = rvec w (σ.symm l) := by
    intro w l; simp [he, Equiv.arrowCongr, rvec]
  conv_lhs => rw [mom2, ← e.tsum_eq (fun v : Site => K v * rvec v i * rvec v i)]
  have hterm : ∀ w : Site, K (e w) * rvec (e w) i * rvec (e w) i
      = K w * rvec w 0 * rvec w 0 := by
    intro w
    rw [hKe w, hcoord w i]
    have hs : σ.symm i = 0 := by simp [hσ, Equiv.swap_apply_right]
    rw [hs]
  rw [tsum_congr hterm, ← mom2]

/-- **Kernel symmetry gives moment-tensor symmetry.** This is the step from the manuscript's
hypothesis to the algebraic core's, and it is where `O_h`-equivariance of the KERNEL becomes
`O_h`-invariance of its SECOND MOMENT. Without it the algebraic theorem would be about a hypothesis
the corollary never states. -/
theorem ohInvariant_mom2 {K : Site → ℝ} (h : KernelOh K) : OhInvariant (mom2 K) := by
  have hform : mom2 K = fun i j => if i = j then mom2 K 0 0 else 0 := by
    funext i j
    by_cases hij : i = j
    · subst hij; rw [if_pos rfl, mom2_diag h]
    · rw [if_neg hij, mom2_offdiag h hij]
  rw [hform]
  exact ohInvariant_scalar _

/-- **The moment tensor is isotropic.** Composing the previous step with the algebraic core: the
quadratic form of a cubic kernel's second moment is a multiple of `|k|²`, so quadratic anisotropy is
impossible. -/
theorem mom2_quadratic_isotropic {K : Site → ℝ} (h : KernelOh K) (k : Fin 3 → ℝ) :
    ∑ i, ∑ j, mom2 K i j * k i * k j = mom2 K 0 0 * nsq k :=
  quadratic_isotropic (ohInvariant_mom2 h) k

/-! ### The Fourier symbol, and why it is a cosine series

The manuscript's symbol is a lattice sum of complex exponentials. That it reduces to a cosine
series is a CONSEQUENCE of `O_h` containing the inversion, not a modelling choice, and it is proved
here rather than assumed. Absolute summability comes from the second moment for free on a lattice:
every nonzero displacement has length at least one. -/

/-- The Fourier symbol, as the manuscript writes it. -/
noncomputable def symbolC (K : Site → ℝ) (k : Fin 3 → ℝ) : ℂ :=
  ∑' v : Site, (K v : ℂ) * Complex.exp ((dot (rvec v) k : ℂ) * Complex.I)

/-- The symbol in cosine form. -/
noncomputable def symbol (K : Site → ℝ) (k : Fin 3 → ℝ) : ℝ :=
  ∑' v : Site, K v * Real.cos (dot (rvec v) k)

/-- **A finite second moment gives absolute summability, on a lattice.** Every nonzero displacement
has `|v|² ≥ 1`, so the second moment dominates the weights off the origin, and the origin is a
single point. This is false on ℝ³, which is why the hypothesis is about a lattice kernel. -/
theorem summable_abs_of_mom2 {K : Site → ℝ} (hM : Summable fun v => |K v| * nsq (rvec v)) :
    Summable fun v => |K v| := by
  classical
  have hfin : Summable fun v : Site => if v = 0 then |K 0| else 0 :=
    summable_of_ne_finset_zero (s := {0}) (by
      intro v hv
      rw [if_neg (by simpa using hv)])
  refine Summable.of_nonneg_of_le (fun v => abs_nonneg _) ?_ (hM.add hfin)
  intro v
  by_cases hv : v = 0
  · subst hv
    have h0 : (0 : ℝ) ≤ |K 0| * nsq (rvec 0) :=
      mul_nonneg (abs_nonneg _) (nsq_nonneg _)
    rw [if_pos rfl]
    linarith
  · have h1 := one_le_nsq_rvec hv
    have h2 : |K v| * 1 ≤ |K v| * nsq (rvec v) := mul_le_mul_of_nonneg_left h1 (abs_nonneg _)
    rw [if_neg hv]
    linarith [h2]

/-- Absolute summability transfers to any unit-modulus phase. -/
theorem summable_phase {K : Site → ℝ} (hK : Summable fun v => |K v|) (t : Site → ℝ) :
    Summable fun v : Site => (K v : ℂ) * Complex.exp ((t v : ℂ) * Complex.I) := by
  refine Summable.of_norm (hK.congr fun v => ?_)
  rw [norm_mul, Complex.norm_exp_ofReal_mul_I, mul_one, Complex.norm_real, Real.norm_eq_abs]

theorem summable_symbol {K : Site → ℝ} (hK : Summable fun v => |K v|) (k : Fin 3 → ℝ) :
    Summable fun v : Site => K v * Real.cos (dot (rvec v) k) := by
  refine Summable.of_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) (fun v => ?_) hK)
  rw [Real.norm_eq_abs, abs_mul]
  exact mul_le_of_le_one_right (abs_nonneg _) (Real.abs_cos_le_one _)

theorem dot_neg (v : Site) (k : Fin 3 → ℝ) : dot (rvec (-v)) k = -dot (rvec v) k := by
  simp [dot, rvec, ← Finset.sum_neg_distrib]

theorem exp_add_exp_neg (t : ℝ) :
    Complex.exp ((t : ℂ) * Complex.I) + Complex.exp (((-t : ℝ) : ℂ) * Complex.I)
      = 2 * ((Real.cos t : ℝ) : ℂ) := by
  have h1 : (((-t : ℝ)) : ℂ) = -(t : ℂ) := by push_cast; ring
  rw [h1, Complex.exp_mul_I, Complex.exp_mul_I, Complex.cos_neg, Complex.sin_neg,
    Complex.ofReal_cos]
  ring

/-- **The symbol is a cosine series**, because `O_h` contains the inversion. Pairing `v` with `−v`
turns the exponential sum into a cosine sum; the evenness `kernelOh_neg` is the only input, and it
is derived from the group rather than assumed. -/
theorem symbolC_eq_symbol {K : Site → ℝ} (h : KernelOh K) (hK : Summable fun v => |K v|)
    (k : Fin 3 → ℝ) : symbolC K k = (symbol K k : ℂ) := by
  have hrefl : symbolC K k
      = ∑' v : Site, (K v : ℂ) * Complex.exp (((-(dot (rvec v) k) : ℝ) : ℂ) * Complex.I) := by
    rw [symbolC, ← (Equiv.neg Site).tsum_eq
      (fun v : Site => (K v : ℂ) * Complex.exp ((dot (rvec v) k : ℂ) * Complex.I))]
    refine tsum_congr fun v => ?_
    have hv : (Equiv.neg Site) v = -v := rfl
    rw [hv, kernelOh_neg h, dot_neg]
  have key : symbolC K k + symbolC K k
      = ∑' v : Site, (K v : ℂ) * (2 * ((Real.cos (dot (rvec v) k) : ℝ) : ℂ)) := by
    nth_rewrite 2 [hrefl]
    rw [symbolC, ← Summable.tsum_add (summable_phase hK fun v => dot (rvec v) k)
      (summable_phase hK fun v => -(dot (rvec v) k))]
    exact tsum_congr fun v => by rw [← mul_add, exp_add_exp_neg]
  have hfin : ∑' v : Site, (K v : ℂ) * (2 * ((Real.cos (dot (rvec v) k) : ℝ) : ℂ))
      = 2 * ((symbol K k : ℝ) : ℂ) := by
    rw [symbol, Complex.ofReal_tsum, ← tsum_mul_left]
    exact tsum_congr fun v => by push_cast; ring
  rw [hfin] at key
  linear_combination key / 2

/-! ### The quadratic expansion

Two Taylor bounds do all the work, and they do different jobs. `|cos t − 1 + t²/2| ≤ t²/2` holds
for every `t` and supplies the DOMINATING function — this is what the second moment makes summable.
`|cos t − 1 + t²/2| ≤ t⁴/2`, also global, supplies the POINTWISE limit at each fixed displacement,
and separately gives clause (ii) outright once a fourth moment is available. Neither can be traded
for the other: the quartic bound is not summable against a second moment alone, which is exactly
the gap the repaired manuscript statement records. -/

/-- The uniform bound. `1 − cos t ∈ [0, t²/2]`, so the remainder sits in `[0, t²/2]` too. -/
theorem cos_rem_abs_le (t : ℝ) : |Real.cos t - 1 + t ^ 2 / 2| ≤ t ^ 2 / 2 := by
  have h1 : Real.cos t ≤ 1 := Real.cos_le_one t
  have h2 : 1 - t ^ 2 / 2 ≤ Real.cos t := Real.one_sub_sq_div_two_le_cos
  rw [abs_le]; constructor <;> linarith

/-- The quartic bound, global. Below `|t| = 1` it is Mathlib's Taylor estimate; above it the
uniform bound already suffices because `t² ≤ t⁴` there. -/
theorem cos_rem_abs_le_quartic (t : ℝ) : |Real.cos t - 1 + t ^ 2 / 2| ≤ t ^ 4 / 2 := by
  by_cases ht : |t| ≤ 1
  · have h := Real.cos_bound ht
    have habs : |t| ^ 4 = t ^ 4 := by rw [← abs_pow, abs_of_nonneg (by positivity)]
    have hq : |Real.cos t - 1 + t ^ 2 / 2| ≤ |t| ^ 4 * (5 / 96) := by
      calc |Real.cos t - 1 + t ^ 2 / 2| = |Real.cos t - (1 - t ^ 2 / 2)| := by ring_nf
        _ ≤ |t| ^ 4 * (5 / 96) := h
    rw [habs] at hq
    nlinarith [pow_nonneg (abs_nonneg t) 4, habs, sq_nonneg t, sq_nonneg (t ^ 2)]
  · rw [not_le] at ht
    have h1 : (1 : ℝ) ≤ t ^ 2 := by nlinarith [sq_abs t, abs_nonneg t]
    have h2 : t ^ 2 ≤ t ^ 4 := by nlinarith [sq_nonneg t]
    exact (cos_rem_abs_le t).trans (by linarith)

/-- `|x_i x_j| ≤ |x|²`, which is what makes the moment tensor's entries summable. -/
theorem abs_mul_le_nsq (x : Fin 3 → ℝ) (i j : Fin 3) : |x i * x j| ≤ nsq x := by
  have hi : x i ^ 2 ≤ nsq x :=
    Finset.single_le_sum (f := fun l => x l ^ 2) (fun _ _ => sq_nonneg _) (Finset.mem_univ i)
  have hj : x j ^ 2 ≤ nsq x :=
    Finset.single_le_sum (f := fun l => x l ^ 2) (fun _ _ => sq_nonneg _) (Finset.mem_univ j)
  have h1 : |x i * x j| ≤ (x i ^ 2 + x j ^ 2) / 2 := by
    rw [abs_mul]
    nlinarith [sq_nonneg (|x i| - |x j|), abs_nonneg (x i), abs_nonneg (x j), sq_abs (x i),
      sq_abs (x j)]
  linarith

/-- The remainder of the quadratic expansion of the symbol. -/
noncomputable def rem (K : Site → ℝ) (k : Fin 3 → ℝ) : ℝ :=
  ∑' v : Site, K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2)

theorem summable_remTerm {K : Site → ℝ} (hM : Summable fun v => |K v| * nsq (rvec v))
    (k : Fin 3 → ℝ) :
    Summable fun v : Site => K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2) := by
  refine Summable.of_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) (fun v => ?_)
    (hM.mul_right (nsq k / 2)))
  rw [Real.norm_eq_abs, abs_mul]
  have hb := cos_rem_abs_le (dot (rvec v) k)
  have hcs := dot_sq_le (rvec v) k
  have h1 : |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2| ≤ nsq (rvec v) * nsq k / 2 := by
    linarith
  calc |K v| * |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
      ≤ |K v| * (nsq (rvec v) * nsq k / 2) := mul_le_mul_of_nonneg_left h1 (abs_nonneg _)
    _ = |K v| * nsq (rvec v) * (nsq k / 2) := by ring

theorem summable_momTerm {K : Site → ℝ} (hM : Summable fun v => |K v| * nsq (rvec v))
    (i j : Fin 3) : Summable fun v : Site => K v * rvec v i * rvec v j := by
  refine Summable.of_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) (fun v => ?_) hM)
  rw [Real.norm_eq_abs, mul_assoc, abs_mul]
  exact mul_le_mul_of_nonneg_left (abs_mul_le_nsq (rvec v) i j) (abs_nonneg _)

/-- The second-order term of the symbol IS the moment tensor's quadratic form. -/
theorem tsum_dot_sq {K : Site → ℝ} (hM : Summable fun v => |K v| * nsq (rvec v))
    (k : Fin 3 → ℝ) :
    ∑' v : Site, K v * dot (rvec v) k ^ 2 = ∑ i, ∑ j, mom2 K i j * k i * k j := by
  have hexp : ∀ v : Site, K v * dot (rvec v) k ^ 2
      = ∑ i, ∑ j, K v * rvec v i * rvec v j * (k i * k j) := by
    intro v
    rw [dot, sq, Finset.sum_mul_sum]
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [tsum_congr hexp]
  rw [Summable.tsum_finsetSum (fun i _ =>
    summable_sum fun j _ => (summable_momTerm hM i j).mul_right _)]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Summable.tsum_finsetSum (fun j _ => (summable_momTerm hM i j).mul_right _)]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [tsum_mul_right, mom2]
  ring

/-- **The quadratic expansion.** The symbol is its value at zero, minus half the moment tensor's
quadratic form, plus the remainder. Nothing about the remainder's size is claimed here. -/
theorem symbol_expansion {K : Site → ℝ} (hK : Summable fun v => |K v|)
    (hM : Summable fun v => |K v| * nsq (rvec v)) (k : Fin 3 → ℝ) :
    symbol K k = (∑' v : Site, K v) - (1 / 2) * (∑ i, ∑ j, mom2 K i j * k i * k j) + rem K k := by
  have hsq : Summable fun v : Site => K v * dot (rvec v) k ^ 2 := by
    refine Summable.of_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) (fun v => ?_)
      (hM.mul_right (nsq k)))
    rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg (sq_nonneg (dot (rvec v) k))]
    have hcs := dot_sq_le (rvec v) k
    calc |K v| * dot (rvec v) k ^ 2 ≤ |K v| * (nsq (rvec v) * nsq k) :=
          mul_le_mul_of_nonneg_left hcs (abs_nonneg _)
      _ = |K v| * nsq (rvec v) * nsq k := by ring
  have hcos := summable_symbol hK k
  have hone : Summable fun v : Site => K v := hK.of_abs
  have hsplit : rem K k
      = symbol K k - (∑' v : Site, K v) + (1 / 2) * ∑' v : Site, K v * dot (rvec v) k ^ 2 := by
    have e1 : symbol K k - (∑' v : Site, K v)
        = ∑' v : Site, (K v * Real.cos (dot (rvec v) k) - K v) := (hcos.tsum_sub hone).symm
    have e2 : (1 / 2 : ℝ) * ∑' v : Site, K v * dot (rvec v) k ^ 2
        = ∑' v : Site, (1 / 2 : ℝ) * (K v * dot (rvec v) k ^ 2) := (tsum_mul_left).symm
    rw [rem, e1, e2, ← Summable.tsum_add (hcos.sub hone) (hsq.mul_left (1 / 2))]
    exact tsum_congr fun v => by ring
  rw [hsplit, tsum_dot_sq hM k]
  ring

/-! ### Clause (i): the `o(|k|²)` remainder

Dominated convergence for series. The dominating function is the second moment, uniform in the
displacement; the pointwise limit at each displacement is the quartic bound. -/

theorem nsq_eq_zero_iff (k : Fin 3 → ℝ) : nsq k = 0 ↔ k = 0 := by
  constructor
  · intro h
    funext j
    have := (Finset.sum_eq_zero_iff_of_nonneg (fun i _ => sq_nonneg (k i))).1 h j (Finset.mem_univ j)
    exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 this
  · rintro rfl; simp [nsq]

theorem continuous_nsq : Continuous (nsq : (Fin 3 → ℝ) → ℝ) := by
  unfold nsq; fun_prop

/-- **Clause (i).** With a finite second absolute moment, the remainder is `o(|k|²)`. -/
theorem rem_littleO {K : Site → ℝ} (hM : Summable fun v => |K v| * nsq (rvec v)) :
    Filter.Tendsto (fun k => rem K k / nsq k) (nhdsWithin 0 {(0 : Fin 3 → ℝ)}ᶜ) (nhds 0) := by
  set 𝓕 := nhdsWithin (0 : Fin 3 → ℝ) {(0 : Fin 3 → ℝ)}ᶜ with h𝓕
  have hne : ∀ᶠ k in 𝓕, nsq k ≠ 0 := by
    filter_upwards [self_mem_nhdsWithin] with k hk
    exact fun hc => hk ((nsq_eq_zero_iff k).1 hc)
  have hnsq0 : Filter.Tendsto (fun k : Fin 3 → ℝ => nsq k) 𝓕 (nhds 0) := by
    have : Filter.Tendsto (fun k : Fin 3 → ℝ => nsq k) (nhds 0) (nhds (nsq 0)) :=
      continuous_nsq.tendsto 0
    have h0 : nsq (0 : Fin 3 → ℝ) = 0 := by simp [nsq]
    rw [h0] at this
    exact this.mono_left nhdsWithin_le_nhds
  have key : Filter.Tendsto
      (fun k => ∑' v : Site,
        K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2) / nsq k)
      𝓕 (nhds (∑' _ : Site, (0 : ℝ))) := by
    refine tendsto_tsum_of_dominated_convergence (bound := fun v => |K v| * nsq (rvec v) / 2)
      (hM.div_const 2) ?_ ?_
    · intro v
      refine squeeze_zero_norm' ?_
        (by simpa using hnsq0.const_mul (|K v| * nsq (rvec v) ^ 2 / 2))
      filter_upwards [hne] with k hk
      have hpos : 0 < nsq k := lt_of_le_of_ne (nsq_nonneg k) (Ne.symm hk)
      have hq := cos_rem_abs_le_quartic (dot (rvec v) k)
      have hcs := dot_sq_le (rvec v) k
      have h4 : dot (rvec v) k ^ 4 ≤ (nsq (rvec v) * nsq k) ^ 2 := by
        have : (0 : ℝ) ≤ dot (rvec v) k ^ 2 := sq_nonneg _
        nlinarith [sq_nonneg (dot (rvec v) k), nsq_nonneg (rvec v), nsq_nonneg k]
      rw [Real.norm_eq_abs, abs_div, abs_mul, abs_of_pos hpos, div_le_iff₀ hpos]
      have hb : |K v| * |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
          ≤ |K v| * ((nsq (rvec v) * nsq k) ^ 2 / 2) := by
        refine mul_le_mul_of_nonneg_left (hq.trans ?_) (abs_nonneg _)
        linarith
      calc |K v| * |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
          ≤ |K v| * ((nsq (rvec v) * nsq k) ^ 2 / 2) := hb
        _ = |K v| * nsq (rvec v) ^ 2 / 2 * nsq k * nsq k := by ring
    · filter_upwards [hne] with k hk v
      have hpos : 0 < nsq k := lt_of_le_of_ne (nsq_nonneg k) (Ne.symm hk)
      have hb := cos_rem_abs_le (dot (rvec v) k)
      have hcs := dot_sq_le (rvec v) k
      rw [Real.norm_eq_abs, abs_div, abs_mul, abs_of_pos hpos, div_le_iff₀ hpos]
      have h1 : |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
          ≤ nsq (rvec v) * nsq k / 2 := by linarith
      calc |K v| * |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
          ≤ |K v| * (nsq (rvec v) * nsq k / 2) := mul_le_mul_of_nonneg_left h1 (abs_nonneg _)
        _ = |K v| * nsq (rvec v) / 2 * nsq k := by ring
  simp only [tsum_zero] at key
  refine key.congr fun k => ?_
  rw [rem, ← tsum_div_const]

/-! ### Clause (ii): the `O(|k|⁴)` remainder -/

/-- **Clause (ii).** With a finite fourth absolute moment the remainder is `O(|k|⁴)`, with an
explicit constant. This is the simpler clause: the quartic bound is global, so no limit is
involved. -/
theorem rem_bigO {K : Site → ℝ} (hM4 : Summable fun v => |K v| * nsq (rvec v) ^ 2) :
    ∀ k, |rem K k| ≤ (∑' v : Site, |K v| * nsq (rvec v) ^ 2) / 2 * nsq k ^ 2 := by
  intro k
  have hterm : ∀ v : Site,
      ‖K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2)‖
        ≤ |K v| * nsq (rvec v) ^ 2 * (nsq k ^ 2 / 2) := by
    intro v
    have hq := cos_rem_abs_le_quartic (dot (rvec v) k)
    have hcs := dot_sq_le (rvec v) k
    have h4 : dot (rvec v) k ^ 4 ≤ (nsq (rvec v) * nsq k) ^ 2 := by
      nlinarith [sq_nonneg (dot (rvec v) k), nsq_nonneg (rvec v), nsq_nonneg k]
    rw [Real.norm_eq_abs, abs_mul]
    have h1 : |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
        ≤ (nsq (rvec v) * nsq k) ^ 2 / 2 := by linarith
    calc |K v| * |Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2|
        ≤ |K v| * ((nsq (rvec v) * nsq k) ^ 2 / 2) := mul_le_mul_of_nonneg_left h1 (abs_nonneg _)
      _ = |K v| * nsq (rvec v) ^ 2 * (nsq k ^ 2 / 2) := by ring
  have hsum : Summable fun v : Site =>
      K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2) :=
    Summable.of_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) hterm
      (hM4.mul_right (nsq k ^ 2 / 2)))
  calc |rem K k| ≤ ∑' v : Site, ‖K v * (Real.cos (dot (rvec v) k) - 1 + dot (rvec v) k ^ 2 / 2)‖ :=
        norm_tsum_le_tsum_norm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) hterm
          (hM4.mul_right (nsq k ^ 2 / 2)))
    _ ≤ ∑' v : Site, |K v| * nsq (rvec v) ^ 2 * (nsq k ^ 2 / 2) :=
        Summable.tsum_le_tsum hterm (Summable.of_nonneg_of_le (fun v => norm_nonneg _) hterm
          (hM4.mul_right (nsq k ^ 2 / 2))) (hM4.mul_right _)
    _ = (∑' v : Site, |K v| * nsq (rvec v) ^ 2) / 2 * nsq k ^ 2 := by
        rw [tsum_mul_right]; ring

/-! ### The corollary

Both clauses, in the manuscript's repaired form, with the isotropy of the quadratic coefficient
supplied by the algebraic core and the non-rotational quartic term by `quartic_not_isotropic`. -/

/-- **Corollary 1a (cubic symmetry forbids quadratic anisotropy), [SM] §4.1, repaired.**

For a translation-invariant `O_h`-equivariant lattice kernel: the symbol is a cosine series; near
`k = 0` it is `a − b|k|² + R(k)` with `b` a single scalar — no anisotropy at quadratic order —
where (i) a finite second absolute moment makes `R(k) = o(|k|²)` and (ii) a finite fourth absolute
moment makes `R(k) = O(|k|⁴)`. The quartic term need not be rotationally invariant, by
`quartic_not_isotropic`. -/
theorem corollary_1a {K : Site → ℝ} (h : KernelOh K)
    (hM : Summable fun v => |K v| * nsq (rvec v)) :
    (∀ k, symbolC K k = (symbol K k : ℂ)) ∧
    (∀ k, symbol K k = (∑' v : Site, K v) - (mom2 K 0 0 / 2) * nsq k + rem K k) ∧
    Filter.Tendsto (fun k => rem K k / nsq k) (nhdsWithin 0 {(0 : Fin 3 → ℝ)}ᶜ) (nhds 0) ∧
    ((Summable fun v => |K v| * nsq (rvec v) ^ 2) →
      ∀ k, |rem K k| ≤ (∑' v : Site, |K v| * nsq (rvec v) ^ 2) / 2 * nsq k ^ 2) := by
  have hK := summable_abs_of_mom2 hM
  refine ⟨fun k => symbolC_eq_symbol h hK k, fun k => ?_, rem_littleO hM, fun hM4 => rem_bigO hM4⟩
  rw [symbol_expansion hK hM k, mom2_quadratic_isotropic h k]
  ring

/-! ### What these proofs rest on -/

#print axioms ohInvariant_eq_scalar
#print axioms ohInvariant_scalar
#print axioms ohInvariant_iff
#print axioms quadratic_isotropic
#print axioms quartic_ohInvariant
#print axioms quartic_not_isotropic
#print axioms one_le_nsq_rvec
#print axioms kernelOh_neg
#print axioms ohInvariant_mom2
#print axioms mom2_quadratic_isotropic
#print axioms summable_abs_of_mom2
#print axioms symbolC_eq_symbol
#print axioms symbol_expansion
#print axioms rem_littleO
#print axioms rem_bigO
#print axioms corollary_1a

end CubicIsotropy

end OIBridge
