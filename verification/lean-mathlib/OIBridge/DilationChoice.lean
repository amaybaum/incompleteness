import OIBridge.ContinuousExtension
import Mathlib.LinearAlgebra.Matrix.Permutation

/-!
# Act 7 layer 2 — the dilation-choice test, at REDUCED STRENGTH

Executed under act 7's frozen preregistration (blob
`810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19`), its resumption control plane (blob
`3bb88717267a4adb45125b6277edae4e56c5cf26`), its resumption result (blob
`216cb9e65cda9b2f3b9777c2ecfcdf8d8bb58df0`) and **the readback amendment** (blob
`0e2c067a90ef9b8e3a4596299ff594bb6ba6807a`), which fixes `T3` to one anchored marginal readback.

**EVERY RESULT HERE IS BOUNDED BY THAT READBACK.** `D4b` came back negative: Source A supplies no
general map carrying the relative candidate on the dilated carrier back to `V`. The map used below is
**ours**, frozen in advance by the amendment, and so is the convention that the distinguished ancilla
configuration belongs to the dilation datum. A divergence exhibited here therefore says that two
admissible **anchored** dilations differ **under that map** — never that Source A's own visible
prediction is underdetermined, and never that a candidate-selection principle is required.

## The frozen map (`T3`)

    readback a₀ M i j  =  ∑ a, M (i, a) (j, a₀)

the direct extension of §3.4 p. 10's rooted marginalization — sum over the **output** ancilla, input
ancilla held at the anchor — to conditioning times other than `0`. It acts on the **(42)-type
stochastic candidate**, which the type enforces: `readback` takes a real matrix, so it can never be
applied to an amplitude or to a unitary.

## Why a divergence is available at all — the mechanism, stated plainly

`admissible_mul_of_fixes_anchor` is the whole engine. **The anchor reads only the `a₀`-columns**, so
right-multiplying an admissible dilation by any unitary that fixes those columns leaves admissibility
untouched — the rooted reproduction condition cannot see the change. But the relative candidate of
(39) p. 13 is built from `U(t ← 0) U†(t′ ← 0)`, and the **adjoint** brings the unread columns into
the anchored one. So the rooted data does not pin the relative candidate.

That same feature is why act 3's padding theorem does not reach this round (`D5a`). §3.4 anchors at
a **single** ancilla configuration, whereas `padData`/`uniformWeight` averages uniformly over the
whole ancilla; and `padData`'s Kronecker shape is not merely unnecessary here but **unavailable** on
either witness — `kronecker_admissible_isUnistochastic` proves a factorizing dilation can only be
admissible for a unistochastic visible slice, and both witnesses are off the direct branch.

## Structure

* **Section A** — `T3`, and the three structural controls the amendment specifies: `R-1` orientation
  and stochasticity, `R-2` agreement with §3.4 at the root, `R-3` equivariance under ancilla
  relabelling that carries the anchor.
* **Section B** — `T2`, the source-admissible dilation predicate, `D5a`'s shape control, and the
  anchor-column stability lemma that drives the exhibition.
* **Section C** — `T1`, the visible screen, in the contrapositive form the witnesses use, together
  with the `n = 2` sufficiency the freeze requires proved in-round so the screen is not over-read as
  a characterization.
* **Section D** — the two outcome propositions (`DC1`'s and `DC4`'s), and the permutation toolkit
  that makes the exhibitions arithmetic.
* **Section E** — `T4` witness A and the `DC1` exhibition on it.
* **Section F** — `T4` witness B and the `DC1` exhibition on it.
* **Section G** — `DC4` refuted on each witness separately, and the tie to act 8's frozen object.

**Witnesses and dilations are built inside the proofs that need them**, per act 3's lesson: there are
no top-level witness or dilation definitions, and the four definitions below are exactly act 7's
budget slots 1, 3, 4 and 5. Slots 2 and 6 are unused.
-/

namespace OIBridge
namespace DilationChoice

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — `T3`, the frozen readback, and its three structural controls -/

/-- **`T3` — THE FROZEN ANCHORED MARGINAL READBACK.**

    readback a₀ M i j = ∑ a, M (i, a) (j, a₀)

Hold the **input** ancilla at the dilation's distinguished configuration `a₀`; sum over the
**output** ancilla. This is §3.4 p. 10's rooted marginalization — "`Γ_ij(t ← 0) = ∑_{i′}
Γ̃_{(i,i′)(j,j′)}(t ← 0)`", for at least some choices of `j′` — extended to conditioning times other
than `0`. **The shape is Source A's; extending it off the root is ours**, per the readback amendment,
and every label below is bounded accordingly.

**It acts on the stochastic candidate, and the type says so**: the argument is a real matrix, so no
phase-sensitive operation can be smuggled in. -/
def readback (a₀ : A) (M : Matrix (V × A) (V × A) ℝ) : Matrix V V ℝ :=
  Matrix.of fun i j => ∑ a : A, M (i, a) (j, a₀)

omit [DecidableEq V] [DecidableEq A] in
/-- **`R-1` — ORIENTATION AND STOCHASTICITY.** The readback carries a column-stochastic matrix on the
dilated carrier to a column-stochastic matrix on `V`, in Source A's external orientation. Act 2's
`RT1` is what licenses moving between orientations and is consumed elsewhere, never re-proved. -/
theorem readback_isColStochastic {a₀ : A} {M : Matrix (V × A) (V × A) ℝ}
    (h : IsColStochastic M) : IsColStochastic (readback (V := V) a₀ M) := by
  refine ⟨fun i j => ?_, fun j => ?_⟩
  · exact Finset.sum_nonneg fun a _ => h.1 _ _
  · show (∑ i : V, ∑ a : A, M (i, a) (j, a₀)) = 1
    have hsum : (∑ p : V × A, M p (j, a₀)) = 1 := h.2 _
    rw [Fintype.sum_prod_type] at hsum
    exact hsum

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- **`R-3` — EQUIVARIANCE UNDER ANCILLA RELABELLING, CARRYING THE ANCHOR.** Relabelling the ancilla
along **any bijection of label sets** — the amendment's `σ : A → A′`, not merely a permutation of one
set — and carrying the anchor along leaves the readback unchanged.

**This says the map depends on the ancilla's structure and not on its names.** It does **NOT** say the
map is independent of *which* configuration is anchored, and it may not be read that way: the anchor
is a component of the dilation datum, and different anchors are different conventions. -/
theorem readback_relabel {A' : Type} [Fintype A] [Fintype A'] (σ : A ≃ A') (a₀ : A)
    (M : Matrix (V × A) (V × A) ℝ) :
    readback (V := V) (σ a₀)
        (M.submatrix (Prod.map id σ.symm) (Prod.map id σ.symm)) = readback a₀ M := by
  ext i j
  show (∑ a : A', M (i, σ.symm a) (j, σ.symm (σ a₀))) = ∑ a : A, M (i, a) (j, a₀)
  simp only [Equiv.symm_apply_apply]
  exact Equiv.sum_comp σ.symm (fun a => M (i, a) (j, a₀))

/-! ### Section B — `T2`, source admissibility of a dilation -/

/-- **`T2` — A SOURCE-ADMISSIBLE ANCHORED DILATION**, at one time.

Two clauses, and exactly two: the dilated operator is **unitary** (§3.4 p. 10's Stinespring output),
and it **reproduces the visible slice** under the frozen readback at the datum's anchor — §3.4 p. 10's
marginalization condition, written in the source's own form.

**The anchor `a₀` is a component of the datum**, per the readback amendment: it is a parameter here,
fixed before any candidate is evaluated, and never re-chosen afterwards. Source A selects no anchor
canonically, which is why the round compares **anchored** dilations and reports at reduced strength.

**Act 7's `D3` gap is NOT closed by this predicate.** Stinespring supplies pointwise existence only;
nothing here derives or selects a coherent time-indexed family, and this predicate is stated at one
time precisely because (39) p. 13 consumes two independent such choices. -/
def AdmissibleDilationAt (G : Matrix V V ℝ) (a₀ : A)
    (U : Matrix (V × A) (V × A) ℂ) : Prop :=
  U ∈ Matrix.unitaryGroup (V × A) ℂ ∧ ∀ i j, G i j = ∑ a : A, ‖U (i, a) (j, a₀)‖ ^ 2

/-- **`R-2` — AGREEMENT WITH §3.4 AT THE ROOT.** The frozen map computes exactly the marginalization
the source states, so an admissible dilation's rooted candidate reads back to the visible slice it
dilates.

**This is the load-bearing control for provenance**: the frozen map **coincides with Source A's own
readback wherever the source has one**, and departs from it only at the conditioning times where the
source supplies nothing. -/
theorem readback_of_admissible {G : Matrix V V ℝ} {a₀ : A}
    {U : Matrix (V × A) (V × A) ℂ} (h : AdmissibleDilationAt G a₀ U) :
    readback a₀ (Matrix.of fun p q => ‖U p q‖ ^ 2) = G := by
  ext i j
  exact (h.2 i j).symm

/-- **`D5a`'s SHAPE CONDITION, DECIDED BY A THEOREM RATHER THAN BY RESEMBLANCE.**

Act 3's `padData` fixes the dilated unitary to the **Kronecker product** `Q.U ⊗ₖ W` — the visible
dynamics tensored beside an ancilla dynamics. A dilation of that shape marginalizes to
`‖U i j‖² · ∑_a ‖W_{a,a₀}‖² = ‖U i j‖²`, because the anchored column of a unitary has unit norm. So
**a Kronecker-product dilation can only be admissible for a UNISTOCHASTIC visible slice.**

Both witnesses are off the direct branch — their Source-A-oriented slices are not unistochastic — so
`padData`'s shape is not merely unnecessary there but **unavailable**. That is `D5a`'s mismatch,
proved rather than asserted, and it is independent of any witness outcome.

§3.4 p. 10's Stinespring dilation asks only for a unitary on the enlarged carrier whose anchored
marginal reproduces the visible slice. **It never requires the unitary to factorize**, and the
witnesses below use dilations that do not. -/
theorem kronecker_admissible_isUnistochastic {G : Matrix V V ℝ} {a₀ : A}
    {U : Matrix V V ℂ} {W : Matrix A A ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ)
    (hW : W ∈ Matrix.unitaryGroup A ℂ)
    (h : AdmissibleDilationAt G a₀ (Matrix.kroneckerMap (· * ·) U W)) :
    IsUnistochastic G := by
  have hanc : (∑ a : A, ‖W a a₀‖ ^ 2) = 1 := by
    have h1 := Matrix.mem_unitaryGroup_iff'.1 hW
    have hjj := congrFun (congrFun h1 a₀) a₀
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at hjj
    have hterm : ∀ r : A, (star W) a₀ r * W r a₀ = ((‖W r a₀‖ ^ 2 : ℝ) : ℂ) := by
      intro r
      rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm, RCLike.star_def,
        Complex.mul_conj]
      norm_cast
      exact Complex.normSq_eq_norm_sq _
    rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hjj
    exact_mod_cast hjj
  refine ⟨U, hU, fun i j => ?_⟩
  have hgij := h.2 i j
  have hkron : ∀ a : A, ‖Matrix.kroneckerMap (· * ·) U W (i, a) (j, a₀)‖ ^ 2
      = ‖U i j‖ ^ 2 * ‖W a a₀‖ ^ 2 := by
    intro a
    rw [Matrix.kroneckerMap_apply, norm_mul, mul_pow]
  rw [hgij, Finset.sum_congr rfl fun a _ => hkron a, ← Finset.mul_sum, hanc, mul_one]

/-- **THE ANCHOR READS ONLY THE `a₀`-COLUMNS**, so right-multiplication by a unitary fixing those
columns preserves admissibility.

**This is the mechanism the exhibition runs on.** The rooted reproduction condition constrains the
columns `(j, a₀)` and nothing else; a unitary `P` that fixes each of them leaves every clause of
`T2` intact. The relative candidate of (39) p. 13 is built from `U(t ← 0) U†(t′ ← 0)`, and the
adjoint brings the **unconstrained** columns into the anchored one — which is why two dilations
indistinguishable at the root can differ on the relative candidate. -/
theorem admissible_mul_of_fixes_anchor {G : Matrix V V ℝ} {a₀ : A}
    {U P : Matrix (V × A) (V × A) ℂ} (hU : AdmissibleDilationAt G a₀ U)
    (hP : P ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hfix : ∀ p j, P p (j, a₀) = if p = (j, a₀) then 1 else 0) :
    AdmissibleDilationAt G a₀ (U * P) := by
  refine ⟨mul_mem hU.1 hP, fun i j => ?_⟩
  have key : ∀ p : V × A, (U * P) p (j, a₀) = U p (j, a₀) := by
    intro p
    rw [Matrix.mul_apply]
    rw [Finset.sum_congr rfl fun r (_ : r ∈ Finset.univ) => by rw [hfix r j]]
    simp
  simpa [key] using hU.2 i j

/-- **A PERMUTATION MATRIX IS UNITARY.** Proved from Mathlib's `conjTranspose_permMatrix` and
`permMatrix_mul` rather than by entrywise computation. -/
theorem permMatrix_mem_unitaryGroup {n : Type} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n) :
    σ.permMatrix ℂ ∈ Matrix.unitaryGroup n ℂ := by
  rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose,
    Matrix.conjTranspose_permMatrix]
  rw [← Matrix.permMatrix_mul]
  simp

/-! ### Section C — `T1`, the visible screen -/

/-- **`T1` — THE VISIBLE SCREEN, in the form the witnesses use.** A matrix that fails to be
column-stochastic cannot be unistochastic, so a `PPer` member whose Source-A-oriented slice is not
doubly stochastic is off the direct branch.

Act 6's structural lemma — Source A's own p. 11 observation, proved there rather than cited — is
consumed. Under `PPer` the row half is already carried, so the content is the **column** half. -/
theorem not_isUnistochastic_of_not_isColStochastic {M : Matrix V V ℝ}
    (h : ¬ IsColStochastic M) : ¬ IsUnistochastic M :=
  fun hu => h (unistochastic_isRowStochastic_and_isColStochastic hu).2

/-- **THE SCREEN IS NECESSARY AND NOT SUFFICIENT, AND AT `n = 2` THE TWO COINCIDE** — proved here
without external citation, as act 7's `T1` requires, so the screen is not over-read as a
characterization.

Every `2 × 2` doubly stochastic matrix has the form `[[a, 1-a], [1-a, a]]`, and is the entrywise
modulus-squared of the real orthogonal `[[√a, √(1-a)], [√(1-a), -√a]]`.

**At `n = 3` the inclusion is proper** — the unistochastic matrices are a proper subset of the
Birkhoff polytope. That is external literature, cited at act 1's evidence level 3 and **not proved
here**, and **nothing in this round's outcome rests on it**. -/
theorem isUnistochastic_two_of_symmetric {a : ℝ} (h0 : 0 ≤ a) (h1 : a ≤ 1) :
    IsUnistochastic (Matrix.of fun i j : Fin 2 => if i = j then a else 1 - a) := by
  have h1a : (0 : ℝ) ≤ 1 - a := by linarith
  refine ⟨Matrix.of fun i j => if i = j then (if i = 0 then (Real.sqrt a : ℂ)
      else (-(Real.sqrt a) : ℂ)) else ((Real.sqrt (1 - a) : ℝ) : ℂ), ?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    have hsa : ((Real.sqrt a : ℝ) : ℂ) * ((Real.sqrt a : ℝ) : ℂ) = ((a : ℝ) : ℂ) := by
      rw [← Complex.ofReal_mul, Real.mul_self_sqrt h0]
    have hsb : ((Real.sqrt (1 - a) : ℝ) : ℂ) * ((Real.sqrt (1 - a) : ℝ) : ℂ)
        = ((1 - a : ℝ) : ℂ) := by
      rw [← Complex.ofReal_mul, Real.mul_self_sqrt h1a]
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply,
        Complex.conj_ofReal, hsa, hsb] <;> ring
  · intro i j
    fin_cases i <;> fin_cases j <;> simp [Real.sq_sqrt h0, Real.sq_sqrt h1a]

/-! ### Section D — the two outcome propositions, and the permutation toolkit -/

/-- **`DC1`'s PROPOSITION** (act 7's budget slot 4) — two source-admissible anchored dilations of
one visible pair yield **different** visible candidates under the frozen readback.

The relative candidate is (39) p. 13's, `U(t ← 0) U†(t′ ← 0)`, read out through (42) p. 14 and then
through `T3`. **Existential**: one pair of dilation choices, one time pair, one anchor.

**Bounded by the frozen readback, and by the anchoring convention.** This proposition says the two
choices differ **under `R_{a₀}` on anchored dilations**. It does **not** say Source A's own visible
prediction is underdetermined, and it does **not** say a candidate-selection principle is required. -/
def MovesVisibleCandidate (G₂ G₁ : Matrix V V ℝ) (a₀ : A) : Prop :=
  ∃ U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ,
    AdmissibleDilationAt G₂ a₀ U₂ ∧ AdmissibleDilationAt G₁ a₀ U₁ ∧
      AdmissibleDilationAt G₂ a₀ U₂' ∧ AdmissibleDilationAt G₁ a₀ U₁' ∧
      readback a₀ (Matrix.of fun p q => ‖(U₂ * U₁ᴴ) p q‖ ^ 2)
        ≠ readback a₀ (Matrix.of fun p q => ‖(U₂' * U₁'ᴴ) p q‖ ^ 2)

/-- **`DC4`'s PROPOSITION** (slot 5) — visible invariance over **all** admissible anchored dilations
of one visible pair.

**`DC4` is reachable only by a theorem of this shape**, never by an unsuccessful search, and `DC3`
never upgrades to it. Stated here so that its refutation below is a refutation of the universal
statement and not of a paraphrase. -/
def VisibleInvariance (G₂ G₁ : Matrix V V ℝ) (a₀ : A) : Prop :=
  ∀ U₂ U₁ U₂' U₁' : Matrix (V × A) (V × A) ℂ,
    AdmissibleDilationAt G₂ a₀ U₂ → AdmissibleDilationAt G₁ a₀ U₁ →
      AdmissibleDilationAt G₂ a₀ U₂' → AdmissibleDilationAt G₁ a₀ U₁' →
        readback a₀ (Matrix.of fun p q => ‖(U₂ * U₁ᴴ) p q‖ ^ 2)
          = readback a₀ (Matrix.of fun p q => ‖(U₂' * U₁'ᴴ) p q‖ ^ 2)

/-- **`DC1` REFUTES `DC4`**, at the visible pair and anchor where it is exhibited — recorded
separately rather than left implicit, as act 6 recorded `not_directBranch` beside
`offDirectBranch`. -/
theorem not_visibleInvariance {G₂ G₁ : Matrix V V ℝ} {a₀ : A}
    (h : MovesVisibleCandidate G₂ G₁ a₀) : ¬ VisibleInvariance G₂ G₁ a₀ := by
  obtain ⟨U₂, U₁, U₂', U₁', h2, h1, h2', h1', hne⟩ := h
  exact fun hinv => hne (hinv U₂ U₁ U₂' U₁' h2 h1 h2' h1')

/-- The entry formula for a permutation matrix, in the form the exhibitions consume. -/
theorem permMatrix_apply_eq {n : Type} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n) (p q : n) :
    σ.permMatrix ℂ p q = if q = σ p then 1 else 0 := by
  simp only [Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, Option.mem_def,
    Option.some.injEq]
  exact if_congr eq_comm rfl rfl

omit [Fintype V] in
/-- **THE ANCHORED MARGINAL OF A PERMUTATION DILATION, IN CLOSED FORM.**

A permutation has exactly one preimage, so summing the indicator over the output ancilla collapses:
the anchored marginal at `(i, j)` is `1` precisely when the preimage of the anchored column lands in
the visible fibre over `i`. **This is what makes the exhibitions arithmetic rather than
combinatorial** — with a concrete permutation, both sides are single decidable equalities on the
dilated carrier. -/
theorem sum_indicator_perm (σ : Equiv.Perm (V × A)) (a₀ : A) (i j : V) :
    (∑ a : A, if ((j, a₀) : V × A) = σ (i, a) then (1 : ℝ) else 0)
      = if (σ.symm (j, a₀)).1 = i then 1 else 0 := by
  have hrw : ∀ a : A, (if ((j, a₀) : V × A) = σ (i, a) then (1 : ℝ) else 0)
      = if σ.symm (j, a₀) = (i, a) then (1 : ℝ) else 0 :=
    fun a => if_congr (Equiv.symm_apply_eq σ).symm rfl rfl
  rw [Finset.sum_congr rfl fun a (_ : a ∈ Finset.univ) => hrw a]
  by_cases hP : (σ.symm (j, a₀)).1 = i
  · rw [if_pos hP]
    have hfix : σ.symm (j, a₀) = (i, (σ.symm (j, a₀)).2) := Prod.ext_iff.mpr ⟨hP, rfl⟩
    have hsingle : (∑ a : A, if σ.symm (j, a₀) = (i, a) then (1 : ℝ) else 0)
        = if σ.symm (j, a₀) = (i, (σ.symm (j, a₀)).2) then (1 : ℝ) else 0 := by
      refine Finset.sum_eq_single (σ.symm (j, a₀)).2 (fun b _ hb => ?_)
        (fun h => absurd (Finset.mem_univ _) h)
      exact if_neg fun hcon => hb (Prod.ext_iff.mp hcon).2.symm
    rw [hsingle, if_pos hfix]
  · rw [if_neg hP]
    exact Finset.sum_eq_zero fun a _ => if_neg fun hcon => hP (Prod.ext_iff.mp hcon).1

/-- **A PERMUTATION DILATION IS ADMISSIBLE EXACTLY WHEN ITS ANCHORED COLUMNS MARGINALIZE RIGHT.**
Unitarity is free (`permMatrix_mem_unitaryGroup`), so the whole content is §3.4's rooted
marginalization, here in the closed form `sum_indicator_perm` supplies. -/
theorem admissible_permMatrix {G : Matrix V V ℝ} (a₀ : A) (σ : Equiv.Perm (V × A))
    (h : ∀ i j, G i j = if (σ.symm (j, a₀)).1 = i then (1 : ℝ) else 0) :
    AdmissibleDilationAt G a₀ (σ.permMatrix ℂ) := by
  refine ⟨permMatrix_mem_unitaryGroup σ, fun i j => ?_⟩
  rw [h i j, ← sum_indicator_perm σ a₀ i j]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [permMatrix_apply_eq]
  split <;> simp

/-- The frozen readback of a permutation dilation's visible candidate, in closed form. -/
theorem readback_permMatrix_apply (σ : Equiv.Perm (V × A)) (a₀ : A) (i j : V) :
    readback a₀ (Matrix.of fun p q => ‖σ.permMatrix ℂ p q‖ ^ 2) i j
      = if (σ.symm (j, a₀)).1 = i then (1 : ℝ) else 0 := by
  rw [← sum_indicator_perm σ a₀ i j]
  show (∑ a : A, ‖σ.permMatrix ℂ (i, a) (j, a₀)‖ ^ 2) = _
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [permMatrix_apply_eq]
  split <;> simp

/-! ### Section E — `T4` witness A, and the `DC1` exhibition on it -/

/-- **`T4` WITNESS A — LAWFUL, OFF THE DIRECT BRANCH, AND REALIZED.**

Act 6's merged family on `Fin 2`: the identity at even times, and at odd times the **rank-one**
collapsing slice `A = ![![1,0],![1,0]]`, which sends both configurations to the first.

All three obligations are discharged here rather than carried by the freeze: `PPer` membership,
off-directness through the `T1` screen, and a lift to a genuine `RootedRealization` through the
merged `pper_has_responseRealization`, as act 6 did. **Witness A is rank-one degenerate**, which is
why act 7 required a second, full-rank witness as well. -/
theorem witnessA_lawful :
    ∃ Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ,
      PPer Γ
        ∧ (∀ n, Γ n = if n % 2 = 0 then 1
              else Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0)
        ∧ ¬ IsUnistochastic (Γ 1)ᵀ
        ∧ ∃ (M : ℕ) (_ : 0 < M)
            (R : RootedRealization (Fin 2) (ResponseHidden (Fin 2) M)),
            ∀ t, rootedMap R t = Γ t := by
  classical
  obtain ⟨Γ, _, hpper, _, _, _, hfull⟩ :=
    screening_continuous_extension _ collapsingSlice_isRowStochastic
  refine ⟨Γ, hpper, hfull, ?_, pper_has_responseRealization hpper⟩
  exact collapsed_slice_not_unistochastic (by simpa using hfull 1)

/-- **`DC1` ON WITNESS A — THE DILATION CHOICE MOVES THE VISIBLE CANDIDATE**, under the frozen
readback, on anchored dilations.

Two source-admissible anchored dilations of the **same** visible pair, at the **same** anchor
`a₀ = 0`, whose relative candidates read back to **different** visible matrices: one to act 6's
collapsing slice in Source A's orientation, the other to the identity.

**Both dilations are permutations of the dilated carrier `Fin 2 × Fin 2`** — an ancilla of size
`N′ = 2 ≤ N² = 4`, dilated size `Ñ = 4 ≤ N³ = 8`, inside §3.4 p. 10's stated bounds — and **both
reproduce the visible slice at the same anchor**, so the divergence is not an artifact of varying
the anchor. It comes from the columns the anchor never reads, which the adjoint of (39) p. 13 brings
into view.

**WHAT THIS DOES AND DOES NOT SAY.** It says two admissible anchored dilations differ **under the
frozen readback `R_{a₀}`**. It does **not** say Source A's own visible prediction is underdetermined,
it does **not** establish that a candidate-selection principle is required, and the divergence could
still be an artifact of the map or of the anchoring convention rather than of the dilation freedom —
exactly the bound the readback amendment fixed in advance. -/
theorem witnessA_moves_visible_candidate :
    MovesVisibleCandidate (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
      (0 : Fin 2) := by
  have hone : AdmissibleDilationAt (1 : Matrix (Fin 2) (Fin 2) ℝ) (0 : Fin 2)
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) := by
    rw [show (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        = (1 : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ from (Matrix.permMatrix_one).symm]
    refine admissible_permMatrix _ _ fun i j => ?_
    fin_cases i <;> fin_cases j <;> simp +decide
  refine ⟨1, _, 1, _, hone,
    admissible_permMatrix (0 : Fin 2) (Equiv.prodComm (Fin 2) (Fin 2)) ?_, hone,
    admissible_permMatrix (0 : Fin 2)
      (Equiv.prodComm (Fin 2) (Fin 2) *
        Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))) ?_, ?_⟩
  · intro i j
    fin_cases i <;> fin_cases j <;> simp +decide [Matrix.transpose_apply]
  · intro i j
    fin_cases i <;> fin_cases j <;> simp +decide [Matrix.transpose_apply]
  · intro hEq
    have hcol : ∀ σ : Equiv.Perm (Fin 2 × Fin 2),
        ((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * (σ.permMatrix ℂ)ᴴ)
          = (σ⁻¹).permMatrix ℂ := by
      intro σ; rw [one_mul, Matrix.conjTranspose_permMatrix]
    rw [hcol, hcol] at hEq
    have h01 := congrFun (congrFun hEq 0) 1
    rw [readback_permMatrix_apply, readback_permMatrix_apply] at h01
    simp +decide at h01

/-- **THE SCREEN'S ROW HALF**, which is the one the witnesses actually use.

Act 6 recorded the orientation and corrected an earlier draft on it: transposing a row-stochastic
`Γ` makes `Γᵀ` column-stochastic automatically, so the half that can still fail on the external
object is the **row** half. Both contrapositives are available; this is the one both witnesses run
through. -/
theorem not_isUnistochastic_of_not_isRowStochastic {M : Matrix V V ℝ}
    (h : ¬ IsRowStochastic M) : ¬ IsUnistochastic M :=
  fun hu => h (unistochastic_isRowStochastic_and_isColStochastic hu).1

/-- Right-multiplication by a permutation matrix permutes columns. -/
theorem mul_permMatrix_apply (U : Matrix (V × A) (V × A) ℂ) (σ : Equiv.Perm (V × A))
    (p q : V × A) : (U * σ.permMatrix ℂ) p q = U p (σ.symm q) := by
  rw [Matrix.mul_apply]
  simp only [permMatrix_apply_eq]
  rw [Finset.sum_eq_single (σ.symm q) (fun r _ hr => ?_)
    (fun h => absurd (Finset.mem_univ _) h)]
  · rw [if_pos (by rw [Equiv.apply_symm_apply]), mul_one]
  · rw [if_neg, mul_zero]
    intro hcon
    exact hr (by rw [hcon, Equiv.symm_apply_apply])

/-! ### Section F — `T4` witness B, and the `DC1` exhibition on it -/

/-- Witness B's odd slice `B = ![![1, 0], ![1/2, 1/2]]` is row-stochastic, which is what act 8's
merged period-two construction consumes. -/
theorem witnessBSlice_isRowStochastic :
    IsRowStochastic (Matrix.of fun i j : Fin 2 =>
      if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2) := by
  constructor
  · intro i j
    show (0 : ℝ) ≤ if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2
    split <;> [split; skip] <;> norm_num
  · intro i
    fin_cases i <;> simp

/-- **WITNESS B IS OFF THE DIRECT BRANCH**, through the `T1` screen's row half on `Bᵀ`: the column
sums of `B` are `3/2` and `1/2`, so `Bᵀ` is not row-stochastic and therefore not unistochastic. -/
theorem witnessBSlice_transpose_not_isUnistochastic :
    ¬ IsUnistochastic (Matrix.of fun i j : Fin 2 =>
      if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2)ᵀ := by
  refine not_isUnistochastic_of_not_isRowStochastic fun hrow => ?_
  have h0 := hrow.2 0
  simp [Fin.sum_univ_two, Matrix.transpose_apply] at h0

/-- **`T4` WITNESS B — LAWFUL, FULL RANK, OFF THE DIRECT BRANCH, AND REALIZED.**

The period-two family whose odd slice is `B = ![![1, 0], ![1/2, 1/2]]`: rows summing to `1`,
**determinant `1/2` so full rank**, and column sums `3/2` and `1/2` so **not** doubly stochastic —
hence off the direct branch through the `T1` screen's row half on `Bᵀ`.

**Why a second witness at all.** Witness A is rank-one degenerate, so a dilation result on it alone
could be an artifact of rank collapse rather than a fact about the dilation. Witness B separates the
two, and act 7 required it for exactly that reason. **The two witnesses' results are reported
separately and never merged.**

All three obligations are discharged here and none is carried by the freeze: `PPer` membership (via
act 8's merged period-two construction, applied to `B`), off-directness, and the
`RootedRealization` lift. -/
theorem witnessB_lawful :
    ∃ Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ,
      PPer Γ
        ∧ (∀ n, Γ n = if n % 2 = 0 then 1
              else Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2)
        ∧ (Γ 1).det = 1 / 2
        ∧ ¬ IsUnistochastic (Γ 1)ᵀ
        ∧ ∃ (M : ℕ) (_ : 0 < M)
            (R : RootedRealization (Fin 2) (ResponseHidden (Fin 2) M)),
            ∀ t, rootedMap R t = Γ t := by
  classical
  obtain ⟨Γ, _, hpper, _, _, _, hfull⟩ :=
    screening_continuous_extension _ witnessBSlice_isRowStochastic
  have hone : Γ 1
      = (Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ) := by simpa using hfull 1
  refine ⟨Γ, hpper, hfull, ?_, ?_, pper_has_responseRealization hpper⟩
  · rw [hone, Matrix.det_fin_two]
    norm_num
  · rw [hone]
    exact witnessBSlice_transpose_not_isUnistochastic

/-- **WITNESS B ALSO MEETS §3.4's INPUT CONTRACT**, and that is established here rather than
inherited.

Act 7 stopped at **`DC2a`** because §3.4's inherited continuity condition (p. 4, after (5)) is
uninstantiated on an `ℕ`-indexed family. Act 8 lifted that stop for **its own** witness by exhibiting
a Source-A-admissible continuous extension, and `CE1` is **existential** — one witness, one
extension. It therefore says nothing about witness B, and is not restated here as though it did.

So witness B's contract standing is proved in-round, as a **second, independent existential
instance**, by applying act 8's two general merged lemmas — `screening_continuous_extension` and
`sourceAAdmissible_of_extends` — to `B`'s slice. **This is not `CE1` and does not extend `CE1`**: it
is a separate instance of the same construction, and neither statement is evidence for a
classification of the OI class.

Off-directness survives to the extension at act 8's frozen index `n = 1`, so the visible pair the
`DC1` exhibition below runs on is the pair of an admissible continuous family. -/
theorem witnessB_admissible_continuous_extension :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (Γhat : NNReal → Matrix (Fin 2) (Fin 2) ℝ),
      PPer Γ
        ∧ (∀ n, Γ n = if n % 2 = 0 then 1
              else Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2)
        ∧ Extends Γhat Γ
        ∧ SourceAAdmissible Γhat
        ∧ (∀ i j, Continuous fun t : NNReal => Γhat t i j)
        ∧ ¬ IsUnistochastic (Γhat (1 : NNReal))ᵀ := by
  classical
  obtain ⟨Γ, Γhat, hpper, hext, hcont, _, hfull⟩ :=
    screening_continuous_extension _ witnessBSlice_isRowStochastic
  refine ⟨Γ, Γhat, hpper, hfull, hext,
    sourceAAdmissible_of_extends hext hpper.1 hcont, hcont, ?_⟩
  have h1 : Γhat (1 : NNReal)
      = (Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ) := by
    have hcast : ((1 : ℕ) : NNReal) = (1 : NNReal) := by norm_num
    rw [← hcast, extends_apply hext 1]
    simpa using hfull 1
  rw [h1]
  exact witnessBSlice_transpose_not_isUnistochastic

/-- **`DC1` ON WITNESS B — THE DILATION CHOICE MOVES THE VISIBLE CANDIDATE ON A FULL-RANK
WITNESS TOO**, under the frozen readback, on anchored dilations.

The mechanism is `admissible_mul_of_fixes_anchor`, here doing the work it was stated for: the second
dilation is the first, right-multiplied by a permutation of the dilated carrier that **fixes every
anchored column**. Admissibility is therefore preserved exactly — the rooted reproduction condition
cannot see the change — while the adjoint in (39) p. 13 brings the unread columns into the anchored
one and the relative candidate moves.

**Witness B is full rank**, so this divergence is not an artifact of witness A's rank collapse. The
two results are reported separately, as act 7 requires, and neither is merged into the other.

**The same bound applies as on witness A**: this says two admissible anchored dilations differ under
the frozen readback `R_{a₀}` — not that Source A's visible prediction is underdetermined, and not
that a candidate-selection principle is required. -/
theorem witnessB_moves_visible_candidate :
    MovesVisibleCandidate (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) := by
  classical
  set s : ℝ := Real.sqrt (1 / 2) with hsdef
  have hs : (s : ℝ) * s = 1 / 2 := Real.mul_self_sqrt (by norm_num)
  have hs2 : (s : ℝ) ^ 2 = 1 / 2 := by rw [sq]; exact hs
  have hsC : ((s : ℝ) : ℂ) * ((s : ℝ) : ℂ) = ((1 / 2 : ℝ) : ℂ) := by
    rw [← Complex.ofReal_mul, hs]
  have hsq : ‖((s : ℝ) : ℂ)‖ ^ 2 = 1 / 2 := by
    have : ‖((s : ℝ) : ℂ)‖ = |s| := by simp
    rw [this, abs_of_nonneg (by rw [hsdef]; exact Real.sqrt_nonneg _), ← hs]
    ring
  obtain ⟨U, hU⟩ : ∃ U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      U = Matrix.of fun p q =>
        if p = (0, 0) then (if q = (0, 0) then 1 else 0)
        else if p = (0, 1) then
          (if q = (0, 1) then ((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else if p = (1, 0) then
          (if q = (0, 1) then -((s : ℝ) : ℂ) else if q = (1, 0) then ((s : ℝ) : ℂ) else 0)
        else (if q = (1, 1) then 1 else 0) := ⟨_, rfl⟩
  have hUunit : U ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [hU, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
        Matrix.conjTranspose_apply, Complex.conj_ofReal, hsC] <;>
      ring_nf
  have hUadm : AdmissibleDilationAt
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) U := by
    refine ⟨hUunit, fun i j => ?_⟩
    fin_cases i <;> fin_cases j <;>
      simp [hU, Fin.sum_univ_two, Matrix.transpose_apply, hs2]
  have hone : AdmissibleDilationAt (1 : Matrix (Fin 2) (Fin 2) ℝ) (0 : Fin 2)
      (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) := by
    rw [show (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        = (1 : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ from (Matrix.permMatrix_one).symm]
    refine admissible_permMatrix _ _ fun i j => ?_
    fin_cases i <;> fin_cases j <;> simp +decide
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
      = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro p j
    obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;>
      simp +decide [hρ]
  refine ⟨1, U, 1, U * ρ.permMatrix ℂ, hone, hUadm, hone,
    admissible_mul_of_fixes_anchor hUadm (permMatrix_mem_unitaryGroup ρ) hfix, ?_⟩
  intro hEq
  have h01 := congrFun (congrFun hEq 0) 1
  have hL : readback (0 : Fin 2)
      (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * Uᴴ) p q‖ ^ 2) 0 1
      = 1 / 2 := by
    show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) * Uᴴ)
      ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 1 / 2
    simp [one_mul, Matrix.conjTranspose_apply, hU, Fin.sum_univ_two, hs2]
  have hR : readback (0 : Fin 2)
      (Matrix.of fun p q => ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        * (U * ρ.permMatrix ℂ)ᴴ) p q‖ ^ 2) 0 1 = 0 := by
    show (∑ a : Fin 2, ‖((1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      * (U * ρ.permMatrix ℂ)ᴴ) ((0 : Fin 2), a) ((1 : Fin 2), (0 : Fin 2))‖ ^ 2) = 0
    simp only [one_mul, Matrix.conjTranspose_apply, mul_permMatrix_apply]
    simp +decide [hρ, hU, Fin.sum_univ_two, Equiv.swap_apply_def]
  rw [hL, hR] at h01
  norm_num at h01

/-! ### Section G — `DC4` refuted on each witness, and the tie to act 8's frozen object -/

/-- **`DC4` IS FALSE ON WITNESS A**, at that visible pair and anchor, under the frozen readback.

`DC4` was the universal statement `VisibleInvariance`, and act 7 required that it be reachable only
by a theorem of that shape. It is refuted here, not left unestablished. **The refutation inherits the
readback's bound exactly**: what fails is invariance of `R_{a₀}`-readbacks of (39)-type relative
candidates over admissible **anchored** dilations. Source A's own visible predictions are untouched,
and no candidate-selection principle is thereby shown to be required. -/
theorem dc4_refuted_witnessA :
    ¬ VisibleInvariance (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
      (0 : Fin 2) :=
  not_visibleInvariance witnessA_moves_visible_candidate

/-- **`DC4` IS FALSE ON WITNESS B TOO**, on a **full-rank** visible pair — so the refutation is not
an artifact of witness A's rank collapse.

**Reported separately from witness A and never merged with it**, as act 7 requires. The same bound
applies verbatim. -/
theorem dc4_refuted_witnessB :
    ¬ VisibleInvariance (1 : Matrix (Fin 2) (Fin 2) ℝ)
      ((Matrix.of fun i j => if i = 0 then (if j = 0 then (1 : ℝ) else 0) else 1 / 2 :
        Matrix (Fin 2) (Fin 2) ℝ))ᵀ (0 : Fin 2) :=
  not_visibleInvariance witnessB_moves_visible_candidate

/-- **THE TIE TO ACT 8'S FROZEN OBJECT** — the visible pair witness A's `DC1` exhibition runs on is
the very family act 8 carried to `CE1`.

Act 8 froze an off-direct `PPer` family on `Fin 2` with a Source-A-admissible continuous extension:
the identity at even times and act 6's collapsing slice at odd times. That is witness A's family,
entry for entry, so the dilation-choice divergence is exhibited **on an object already known to
survive the continuous-extension obligation** rather than on a fresh convenience.

**This conjunction adds no strength to either conjunct.** Act 8's `CE1` bound (the contract layer 1
transcribed is weak) and this round's readback bound both stand unchanged, and neither is evidence
for the other. Track I is not touched. -/
theorem dc1_runs_on_act8_frozen_object :
    (∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (Γhat : NNReal → Matrix (Fin 2) (Fin 2) ℝ),
        PPer Γ
          ∧ (∀ n, Γ n = if n % 2 = 0 then 1
              else Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0))
          ∧ Extends Γhat Γ
          ∧ SourceAAdmissible Γhat
          ∧ ¬ IsUnistochastic (Γhat (1 : NNReal))ᵀ)
      ∧ MovesVisibleCandidate (1 : Matrix (Fin 2) (Fin 2) ℝ)
          ((Matrix.of fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ)ᵀ
          (0 : Fin 2) := by
  refine ⟨?_, witnessA_moves_visible_candidate⟩
  obtain ⟨Γ, Γhat, hpper, hres, hext, hadm, _, hnu, _⟩ :=
    admissible_offDirect_continuous_extension
  exact ⟨Γ, Γhat, hpper, hres, hext, hadm, hnu⟩

end DilationChoice
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.DilationChoice.readback_isColStochastic
#print axioms OIBridge.DilationChoice.readback_relabel
#print axioms OIBridge.DilationChoice.readback_of_admissible
#print axioms OIBridge.DilationChoice.kronecker_admissible_isUnistochastic
#print axioms OIBridge.DilationChoice.admissible_mul_of_fixes_anchor
#print axioms OIBridge.DilationChoice.permMatrix_mem_unitaryGroup
#print axioms OIBridge.DilationChoice.not_isUnistochastic_of_not_isColStochastic
#print axioms OIBridge.DilationChoice.isUnistochastic_two_of_symmetric
#print axioms OIBridge.DilationChoice.not_visibleInvariance
#print axioms OIBridge.DilationChoice.permMatrix_apply_eq
#print axioms OIBridge.DilationChoice.sum_indicator_perm
#print axioms OIBridge.DilationChoice.admissible_permMatrix
#print axioms OIBridge.DilationChoice.readback_permMatrix_apply
#print axioms OIBridge.DilationChoice.witnessA_lawful
#print axioms OIBridge.DilationChoice.witnessA_moves_visible_candidate
#print axioms OIBridge.DilationChoice.not_isUnistochastic_of_not_isRowStochastic
#print axioms OIBridge.DilationChoice.mul_permMatrix_apply
#print axioms OIBridge.DilationChoice.witnessBSlice_isRowStochastic
#print axioms OIBridge.DilationChoice.witnessBSlice_transpose_not_isUnistochastic
#print axioms OIBridge.DilationChoice.witnessB_lawful
#print axioms OIBridge.DilationChoice.witnessB_admissible_continuous_extension
#print axioms OIBridge.DilationChoice.witnessB_moves_visible_candidate
#print axioms OIBridge.DilationChoice.dc4_refuted_witnessA
#print axioms OIBridge.DilationChoice.dc4_refuted_witnessB
#print axioms OIBridge.DilationChoice.dc1_runs_on_act8_frozen_object
