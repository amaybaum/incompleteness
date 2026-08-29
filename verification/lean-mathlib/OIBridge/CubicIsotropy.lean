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

  THREE LAYERS, kept separate so that no one of them can stand in for another.

  * ALGEBRAIC CORE. `Sym²(ℝ³)^{O_h}` is one-dimensional: every `O_h`-invariant symmetric bilinear
    form on ℝ³ is a multiple of `δ`. This is the "forbids anisotropy" content and it is pure
    invariant theory — no analysis, no moments, no kernel.
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

/-! ### The analytic bridge and the quartic refinement are NOT proved here

Recorded, not glossed. Clauses (i) and (ii) of the corollary each need an analytic step this file
does not carry, and the coverage ledger records both as this entry's delta rather than letting the
algebraic core stand in for the whole corollary:

* (i) `o(|k|²)`. With weights `K i` at displacements `v i` and symbol `∑ᵢ K i cos⟨v i, k⟩`, two
  Taylor bounds do the work and they do different jobs. `|cos t − 1 + t²/2| ≤ t²` holds for every
  `t` and supplies the DOMINATING function, uniform in the index — this is what the finite second
  moment makes summable. `|cos t − 1 + t²/2| ≤ (5/96)·t⁴` holds for `|t| ≤ 1` and supplies the
  POINTWISE limit at each fixed index. Dominated convergence for series then gives the remainder.
  Neither bound can be traded for the other, and that is exactly why the second moment buys
  `o(|k|²)` and nothing sharper.
* (ii) `O(|k|⁴)`. A finite fourth absolute moment dominates the quartic Taylor remainder directly.

What IS proved here is the algebraic core — the content the corollary's title names — together with
the quartic countercontrol. The companion probe checks both analytic clauses numerically, and
checks the separation that motivated the manuscript repair: a kernel with finite second moment and
infinite fourth moment whose remainder is not `O(|k|⁴)`.

-/

/-! ### What these proofs rest on -/

#print axioms ohInvariant_eq_scalar
#print axioms ohInvariant_scalar
#print axioms ohInvariant_iff
#print axioms quadratic_isotropic
#print axioms quartic_ohInvariant
#print axioms quartic_not_isotropic

end CubicIsotropy

end OIBridge
