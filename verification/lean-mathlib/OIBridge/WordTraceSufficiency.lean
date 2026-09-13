import OIBridge.SemigroupTransfer
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Isomorphisms
import Mathlib.LinearAlgebra.Finsupp.LinearCombination
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

/-!
# Substratum Lemma 24.1A — `ST5` sufficiency: equal block-word traces and hidden conjugation

Executed under the frozen control plane
`verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md`, blob
`98cfcfdc0e74ffe0186c502517a842bfeb25d351`, from `main` at
`baadea2638019b335d96c892590491a6fb420936` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## What this round tests

The Lemma 24.1 round (`OIBridge/SemigroupTransfer.lean`) proved that hidden conjugation
`U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` preserves every block-word trace (`trace_wordEval_hiddenConjugate`) and
left the converse — **sufficiency** — UNDECIDED. This round is sufficiency only: does equality
of all block-word traces `Tr[wordEval U w] = Tr[wordEval U' w]` force a single hidden unitary
conjugation? Every statement is in the completeness-relevant direction, from equal traces to an
exhibited conjugating `W`, on the merged block alphabet (`wordEval`, `Matrix.trace` on `M_m(ℂ)`
unnormalised), whose definitions are reused and not redefined.

## The targets and where they land

* **`WT0`** — necessity is consumed as the merged `trace_wordEval_hiddenConjugate` and not
  re-proved; `WT0b_pairC_not_wordTracesEqual` records that the `ST3` pair is excluded from the
  hypothesis by the merged word certificate `pairC_wordTraces`; `WT0c_positive_control` exhibits
  the hidden transposition `1 ↔ 2` of `ℤ₃` on `φ̂_C`, with `Wᴴ W = 1`, `HiddenConjugate`,
  `U' ≠ U` and `WordTracesEqual` as conjuncts.
* **`WT1`** — `WT1_transfer`: the trace-form kernel step. Under `WordTracesEqual U U'` the map
  `w(U) ↦ w(U')` extends to the linear map `transferMap U U' h` on the word span `𝒲(U)`, well
  defined because equal word traces make the two Gram forms `Tr[w₁(·)ᴴ w₂(·)]` agree
  (`gram_eq_of_wordTracesEqual`) and `Tr[Aᴴ A] = 0` forces `A = 0`; it is injective, unital,
  multiplicative, `*`-preserving, trace-preserving, with range `𝒲(U')`. No unitarity hypothesis.
* **`WT2-gen`** — `WT2gen_hiddenConjugate`: on the spanning class `BlockSpanning U`,
  `BlockSpanning U'` (word span equal to all of `M_m(ℂ)`, two-sided as frozen), word-trace
  equality gives `HiddenConjugate U U'`, by the matrix-unit construction
  `exists_unitary_of_starMul`: `e_{ij} := φ(E_{ij})` are matrix units, `ξ` is a nonzero column
  of the projection `e_{oo}`, `W` has columns `e_{jo} ξ` normalised, `Wᴴ W = 1`, and
  `W E_{ij} Wᴴ = e_{ij}`. The construction consumes `BlockSpanning U` alone, so the one-sided
  form `WT2gen_oneSided` is proved directly and is the permitted strengthening; the two-sided
  statement, derived from it with its second spanning hypothesis carried unused, is what the
  label attaches to. Independently, `BlockSpanning U'` follows from `BlockSpanning U` by
  injectivity and dimension (`blockSpanning_of_wordTracesEqual`).
* **`WT2`** (all unitary pairs) is **not reached** in this module: the general case needs the
  spatial structure of the `*`-subalgebra `𝒲(U)` of `M_m(ℂ)` — its decomposition into simple
  summands with multiplicities, the unitary equivalence of equal-multiplicity representations —
  which neither Mathlib at the pin nor the corpus carries. Nothing here is stated above the
  spanning class.
* **`WT3`** — `WT3_spanning` and `WT3_spanning_iff`: sufficiency, and the biconditional
  `HiddenConjugate U U' ↔ WordTracesEqual U U'`, on the spanning class and no higher, the
  reverse direction being the consumed necessity. Unitarity of `U, U'` is not used and is not
  carried.
* **`WT4`** — `WT4_finite_spanning_family`: a finite family of words spans `𝒲(U)`, from
  finite-dimensionality; no word-length bound is claimed.

## Discipline

Five of the six frozen slots: `wordStar` (slot 1), `wordSpan` (slot 2), `WordTracesEqual`
(slot 3, fired), `BlockSpanning` (slot 4, fired), `transferMap` (slot 5, fired); slot 6, an
implementing-unitary abbreviation, is unused — every `W` is a bound variable inside a proof or
an existential pinned by an equation. Pair C's permutations and the hidden transposition are
local notation, not declarations. The module carries no unproved declaration, no added
postulate, and no kernel-bypassing decision procedure; every named result prints only
`[propext, Classical.choice, Quot.sound]`.

Nothing here says Lemma 24.1 is repaired, nothing says the four generator families are complete
or incomplete, and nothing says the manuscripts' route is restored: whether the reconstruction
framework supplies the block-word trace data is round 24.1B, named and not begun.
-/

namespace OIBridge
namespace WordTraceSufficiency

set_option autoImplicit false
set_option linter.unusedSectionVars false

open Matrix Finset SemigroupTransfer
open scoped Kronecker ComplexConjugate ComplexOrder

variable {V H : Type} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-! ### Section A — the budget slots (two needed, three conditional fired, one unused) -/

/-- **Slot 1.** The adjoint word: `w` reversed with every flag flipped, so that
`wordEval U (wordStar w) = (wordEval U w)ᴴ`. -/
def wordStar (w : List (V × V × Bool)) : List (V × V × Bool) :=
  (w.map fun l => (l.1, l.2.1, !l.2.2)).reverse

/-- **Slot 2.** The word span `𝒲(U) = span_ℂ { wordEval U w : w }`, a subspace of `M_m(ℂ)`. -/
@[reducible] def wordSpan (U : Matrix (V × H) (V × H) ℂ) : Submodule ℂ (Matrix H H ℂ) :=
  Submodule.span ℂ (Set.range (wordEval U))

/-- **Slot 3 (conditional, fired).** Word-trace equality, the hypothesis of sufficiency. -/
def WordTracesEqual (U U' : Matrix (V × H) (V × H) ℂ) : Prop :=
  ∀ w : List (V × V × Bool), trace (wordEval U w) = trace (wordEval U' w)

/-- **Slot 4 (conditional, fired).** The spanning hypothesis: `𝒲(U) = M_m(ℂ)`. -/
def BlockSpanning (U : Matrix (V × H) (V × H) ℂ) : Prop :=
  wordSpan U = ⊤

/-! ### Section B — words: concatenation, the empty word, letters, the adjoint word -/

theorem wordEval_nil (U : Matrix (V × H) (V × H) ℂ) : wordEval U [] = 1 := by
  simp [wordEval]

theorem wordEval_append (U : Matrix (V × H) (V × H) ℂ) (w₁ w₂ : List (V × V × Bool)) :
    wordEval U (w₁ ++ w₂) = wordEval U w₁ * wordEval U w₂ := by
  simp only [wordEval, List.map_append, List.prod_append]

/-- A visible block is the value of the one-letter plain word. -/
theorem visibleBlock_eq_wordEval (U : Matrix (V × H) (V × H) ℂ) (v w : V) :
    visibleBlock U v w = wordEval U [(v, w, true)] := by
  simp [wordEval]

theorem wordStar_cons (l : V × V × Bool) (w : List (V × V × Bool)) :
    wordStar (l :: w) = wordStar w ++ [(l.1, l.2.1, !l.2.2)] := by
  simp [wordStar]

/-- **The adjoint word evaluates to the adjoint.** -/
theorem wordEval_wordStar (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool)) :
    wordEval U (wordStar w) = (wordEval U w)ᴴ := by
  induction w with
  | nil => simp [wordStar, wordEval]
  | cons l w ih =>
    rw [wordStar_cons, wordEval_append, ih]
    simp only [wordEval, List.map_cons, List.prod_cons, List.map_nil, List.prod_nil,
      Matrix.mul_one, conjTranspose_mul]
    congr 1
    by_cases hl : l.2.2
    · simp [hl]
    · simp [hl]

/-! ### Section C — the word span: `1`, the blocks, products and adjoints -/

theorem wordEval_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool)) :
    wordEval U w ∈ wordSpan U :=
  Submodule.subset_span ⟨w, rfl⟩

theorem one_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) : (1 : Matrix H H ℂ) ∈ wordSpan U := by
  rw [← wordEval_nil U]
  exact wordEval_mem_wordSpan U []

theorem visibleBlock_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) (v w : V) :
    visibleBlock U v w ∈ wordSpan U := by
  rw [visibleBlock_eq_wordEval]
  exact wordEval_mem_wordSpan U _

theorem wordEval_mul_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool))
    {y : Matrix H H ℂ} (hy : y ∈ wordSpan U) : wordEval U w * y ∈ wordSpan U := by
  induction hy using Submodule.span_induction with
  | mem y hy =>
    obtain ⟨w', rfl⟩ := hy
    rw [← wordEval_append]
    exact wordEval_mem_wordSpan U _
  | zero => rw [mul_zero]; exact zero_mem _
  | add y z _ _ hy hz => rw [mul_add]; exact add_mem hy hz
  | smul c y _ hy => rw [mul_smul_comm]; exact Submodule.smul_mem _ _ hy

/-- **`𝒲(U)` is closed under multiplication.** -/
theorem mul_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) {x y : Matrix H H ℂ}
    (hx : x ∈ wordSpan U) (hy : y ∈ wordSpan U) : x * y ∈ wordSpan U := by
  induction hx using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, rfl⟩ := hx
    exact wordEval_mul_mem_wordSpan U w hy
  | zero => rw [zero_mul]; exact zero_mem _
  | add x z _ _ hx hz => rw [add_mul]; exact add_mem hx hz
  | smul c x _ hx => rw [smul_mul_assoc]; exact Submodule.smul_mem _ _ hx

/-- **`𝒲(U)` is closed under the adjoint.** -/
theorem conjTranspose_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ) {x : Matrix H H ℂ}
    (hx : x ∈ wordSpan U) : xᴴ ∈ wordSpan U := by
  induction hx using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, rfl⟩ := hx
    rw [← wordEval_wordStar]
    exact wordEval_mem_wordSpan U _
  | zero => rw [conjTranspose_zero]; exact zero_mem _
  | add x z _ _ hx hz => rw [conjTranspose_add]; exact add_mem hx hz
  | smul c x _ hx => rw [conjTranspose_smul]; exact Submodule.smul_mem _ _ hx

/-- Every element of `𝒲(U)` is a finite linear combination of word values. -/
theorem exists_linearCombination (U : Matrix (V × H) (V × H) ℂ) {x : Matrix H H ℂ}
    (hx : x ∈ wordSpan U) :
    ∃ c : List (V × V × Bool) →₀ ℂ, Finsupp.linearCombination ℂ (wordEval U) c = x := by
  rw [wordSpan, ← Finsupp.range_linearCombination] at hx
  exact LinearMap.mem_range.1 hx

theorem linearCombination_mem_wordSpan (U : Matrix (V × H) (V × H) ℂ)
    (c : List (V × V × Bool) →₀ ℂ) :
    Finsupp.linearCombination ℂ (wordEval U) c ∈ wordSpan U := by
  rw [wordSpan, ← Finsupp.range_linearCombination]
  exact LinearMap.mem_range_self _ c

/-! ### Section D — the trace form on word values, and the kernel step of `WT1`

`⟨A, B⟩ := Tr[Aᴴ B]` on `M_m(ℂ)`; on linear combinations of word values it expands into word
traces of `w₁* ++ w₂`, so `WordTracesEqual` makes the two Gram forms agree. -/

/-- The Gram form of two word combinations is a double sum of word traces. -/
theorem trace_linearCombination_gram (U : Matrix (V × H) (V × H) ℂ)
    (c d : List (V × V × Bool) →₀ ℂ) :
    trace ((Finsupp.linearCombination ℂ (wordEval U) c)ᴴ *
        Finsupp.linearCombination ℂ (wordEval U) d)
      = c.sum fun w a => d.sum fun w' b =>
          star a * (b * trace (wordEval U (wordStar w ++ w'))) := by
  simp only [Finsupp.linearCombination_apply, Finsupp.sum, conjTranspose_sum, conjTranspose_smul,
    Finset.sum_mul, Finset.mul_sum, trace_sum, smul_mul_assoc, mul_smul_comm, trace_smul,
    smul_eq_mul, wordEval_append, wordEval_wordStar]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun w _ => Finset.sum_congr rfl fun w' _ => by ring

/-- **Equal word traces make the two Gram forms agree.** -/
theorem gram_eq_of_wordTracesEqual {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    (c d : List (V × V × Bool) →₀ ℂ) :
    trace ((Finsupp.linearCombination ℂ (wordEval U) c)ᴴ *
        Finsupp.linearCombination ℂ (wordEval U) d)
      = trace ((Finsupp.linearCombination ℂ (wordEval U') c)ᴴ *
          Finsupp.linearCombination ℂ (wordEval U') d) := by
  rw [trace_linearCombination_gram, trace_linearCombination_gram]
  refine Finsupp.sum_congr fun w _ => Finsupp.sum_congr fun w' _ => ?_
  rw [h]

/-- **The kernel step.** A vanishing word combination for `U` vanishes for `U'`, by positive
definiteness of the trace form: `Tr[Aᴴ A] = 0` forces `A = 0`. -/
theorem linearCombination_eq_zero_of_wordTracesEqual {U U' : Matrix (V × H) (V × H) ℂ}
    (h : WordTracesEqual U U') (c : List (V × V × Bool) →₀ ℂ)
    (hc : Finsupp.linearCombination ℂ (wordEval U) c = 0) :
    Finsupp.linearCombination ℂ (wordEval U') c = 0 := by
  rw [← Matrix.trace_conjTranspose_mul_self_eq_zero_iff, ← gram_eq_of_wordTracesEqual h, hc,
    conjTranspose_zero, mul_zero, trace_zero]

theorem ker_linearCombination_le {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U') :
    LinearMap.ker (Finsupp.linearCombination ℂ (wordEval U))
      ≤ LinearMap.ker (Finsupp.linearCombination ℂ (wordEval U')) := fun c hc => by
  rw [LinearMap.mem_ker] at hc ⊢
  exact linearCombination_eq_zero_of_wordTracesEqual h c hc

/-! ### Section E — `WT1`: the induced map on the word span and its seven properties -/

/-- **Slot 5 (conditional, fired).** The induced map `φ : 𝒲(U) →ₗ[ℂ] M_m(ℂ)`, `w(U) ↦ w(U')`,
extended linearly: the word combination of `U'` factored through the quotient of the coefficient
space by the kernel of the word combination of `U`, which `WordTracesEqual` makes legitimate. -/
noncomputable def transferMap (U U' : Matrix (V × H) (V × H) ℂ) (h : WordTracesEqual U U') :
    wordSpan U →ₗ[ℂ] Matrix H H ℂ :=
  (LinearMap.ker (Finsupp.linearCombination ℂ (wordEval U))).liftQ
      (Finsupp.linearCombination ℂ (wordEval U')) (ker_linearCombination_le h) ∘ₗ
    (Finsupp.linearCombination ℂ (wordEval U)).quotKerEquivRange.symm.toLinearMap ∘ₗ
    (LinearEquiv.ofEq (wordSpan U)
      (LinearMap.range (Finsupp.linearCombination ℂ (wordEval U)))
      (Finsupp.range_linearCombination ℂ (v := wordEval U)).symm).toLinearMap

/-- The induced map on a word combination is the same combination of `U'`-words. -/
theorem transferMap_linearCombination {U U' : Matrix (V × H) (V × H) ℂ}
    (h : WordTracesEqual U U') (c : List (V × V × Bool) →₀ ℂ)
    (hc : Finsupp.linearCombination ℂ (wordEval U) c ∈ wordSpan U) :
    transferMap U U' h ⟨Finsupp.linearCombination ℂ (wordEval U) c, hc⟩
      = Finsupp.linearCombination ℂ (wordEval U') c := by
  unfold transferMap
  simp only [LinearMap.comp_apply, LinearEquiv.coe_coe]
  have e : LinearEquiv.ofEq (wordSpan U)
      (LinearMap.range (Finsupp.linearCombination ℂ (wordEval U)))
      (Finsupp.range_linearCombination ℂ (v := wordEval U)).symm
        ⟨Finsupp.linearCombination ℂ (wordEval U) c, hc⟩
      = ⟨Finsupp.linearCombination ℂ (wordEval U) c, LinearMap.mem_range_self _ c⟩ :=
    Subtype.ext (LinearEquiv.coe_ofEq_apply _ _)
  rw [e, LinearMap.quotKerEquivRange_symm_apply_image, Submodule.mkQ_apply, Submodule.liftQ_apply]

theorem transferMap_apply_of_eq {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    {x : Matrix H H ℂ} (hx : x ∈ wordSpan U) (c : List (V × V × Bool) →₀ ℂ)
    (hc : Finsupp.linearCombination ℂ (wordEval U) c = x) :
    transferMap U U' h ⟨x, hx⟩ = Finsupp.linearCombination ℂ (wordEval U') c := by
  subst hc
  exact transferMap_linearCombination h c hx

/-- **`WT1`(i)** — the induced map sends `w(U)` to `w(U')`. -/
theorem transferMap_wordEval {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    (w : List (V × V × Bool)) (hw : wordEval U w ∈ wordSpan U) :
    transferMap U U' h ⟨wordEval U w, hw⟩ = wordEval U' w := by
  rw [transferMap_apply_of_eq h hw (Finsupp.single w 1)
    (by rw [Finsupp.linearCombination_single, one_smul]), Finsupp.linearCombination_single,
    one_smul]

/-- **`WT1`(ii)** — the range is `𝒲(U')`. -/
theorem transferMap_range {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U') :
    LinearMap.range (transferMap U U' h) = wordSpan U' := by
  apply le_antisymm
  · rintro _ ⟨⟨x, hx⟩, rfl⟩
    obtain ⟨c, rfl⟩ := exists_linearCombination U hx
    rw [transferMap_linearCombination]
    exact linearCombination_mem_wordSpan U' c
  · rw [wordSpan]
    refine Submodule.span_le.2 ?_
    rintro _ ⟨w, rfl⟩
    exact ⟨⟨wordEval U w, wordEval_mem_wordSpan U w⟩, transferMap_wordEval h w _⟩

/-- **`WT1`(iv)** — unital. -/
theorem transferMap_one {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U') :
    transferMap U U' h ⟨1, one_mem_wordSpan U⟩ = 1 := by
  rw [transferMap_apply_of_eq h _ (Finsupp.single [] 1)
    (by rw [Finsupp.linearCombination_single, one_smul, wordEval_nil]),
    Finsupp.linearCombination_single, one_smul, wordEval_nil]

/-- **`WT1`(vii)** — trace-preserving. -/
theorem transferMap_trace {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    (x : wordSpan U) : trace (transferMap U U' h x) = trace (x : Matrix H H ℂ) := by
  obtain ⟨x, hx⟩ := x
  obtain ⟨c, rfl⟩ := exists_linearCombination U hx
  rw [transferMap_linearCombination]
  simp only [Finsupp.linearCombination_apply, Finsupp.sum, trace_sum, trace_smul]
  exact Finset.sum_congr rfl fun w _ => by rw [h w]

/-- Left multiplication by a word value passes through the induced map. -/
theorem transferMap_wordEval_mul {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    (w : List (V × V × Bool)) {y : Matrix H H ℂ} (hy : y ∈ wordSpan U)
    (hwy : wordEval U w * y ∈ wordSpan U) :
    transferMap U U' h ⟨wordEval U w * y, hwy⟩
      = wordEval U' w * transferMap U U' h ⟨y, hy⟩ := by
  induction hy using Submodule.span_induction with
  | mem y hy =>
    obtain ⟨w', rfl⟩ := hy
    rw [transferMap_wordEval, transferMap_apply_of_eq h hwy (Finsupp.single (w ++ w') 1)
      (by rw [Finsupp.linearCombination_single, one_smul, wordEval_append]),
      Finsupp.linearCombination_single, one_smul, wordEval_append]
  | zero =>
    have e : (⟨wordEval U w * 0, hwy⟩ : wordSpan U) = 0 := Subtype.ext (mul_zero _)
    rw [e, map_zero]
    show (0 : Matrix H H ℂ) = wordEval U' w * transferMap U U' h 0
    rw [map_zero, mul_zero]
  | add y z hy hz ihy ihz =>
    have e : (⟨wordEval U w * (y + z), hwy⟩ : wordSpan U)
        = ⟨wordEval U w * y, wordEval_mul_mem_wordSpan U w hy⟩
          + ⟨wordEval U w * z, wordEval_mul_mem_wordSpan U w hz⟩ :=
      Subtype.ext (mul_add _ _ _)
    have e' : (⟨y + z, add_mem hy hz⟩ : wordSpan U) = ⟨y, hy⟩ + ⟨z, hz⟩ := rfl
    rw [e, map_add, ihy _, ihz _, e', map_add, mul_add]
  | smul a y hy ih =>
    have e : (⟨wordEval U w * (a • y), hwy⟩ : wordSpan U)
        = a • ⟨wordEval U w * y, wordEval_mul_mem_wordSpan U w hy⟩ :=
      Subtype.ext (mul_smul_comm _ _ _)
    have e' : (⟨a • y, Submodule.smul_mem _ a hy⟩ : wordSpan U) = a • ⟨y, hy⟩ := rfl
    rw [e, map_smul, ih _, e', map_smul, mul_smul_comm]

/-- **`WT1`(v)** — multiplicative. -/
theorem transferMap_mul {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    {x y : Matrix H H ℂ} (hx : x ∈ wordSpan U) (hy : y ∈ wordSpan U)
    (hxy : x * y ∈ wordSpan U) :
    transferMap U U' h ⟨x * y, hxy⟩ = transferMap U U' h ⟨x, hx⟩ * transferMap U U' h ⟨y, hy⟩ := by
  induction hx using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, rfl⟩ := hx
    rw [transferMap_wordEval_mul h w hy, transferMap_wordEval]
  | zero =>
    have e : (⟨0 * y, hxy⟩ : wordSpan U) = 0 := Subtype.ext (zero_mul _)
    rw [e, map_zero]
    show (0 : Matrix H H ℂ) = transferMap U U' h 0 * transferMap U U' h ⟨y, hy⟩
    rw [map_zero, zero_mul]
  | add x z hx hz ihx ihz =>
    have e : (⟨(x + z) * y, hxy⟩ : wordSpan U)
        = ⟨x * y, mul_mem_wordSpan U hx hy⟩ + ⟨z * y, mul_mem_wordSpan U hz hy⟩ :=
      Subtype.ext (add_mul _ _ _)
    have e' : (⟨x + z, add_mem hx hz⟩ : wordSpan U) = ⟨x, hx⟩ + ⟨z, hz⟩ := rfl
    rw [e, map_add, ihx _, ihz _, e', map_add, add_mul]
  | smul a x hx ih =>
    have e : (⟨(a • x) * y, hxy⟩ : wordSpan U) = a • ⟨x * y, mul_mem_wordSpan U hx hy⟩ :=
      Subtype.ext (smul_mul_assoc _ _ _)
    have e' : (⟨a • x, Submodule.smul_mem _ a hx⟩ : wordSpan U) = a • ⟨x, hx⟩ := rfl
    rw [e, map_smul, ih _, e', map_smul, smul_mul_assoc]

/-- **`WT1`(vi)** — `*`-preserving. -/
theorem transferMap_conjTranspose {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U')
    {x : Matrix H H ℂ} (hx : x ∈ wordSpan U) (hx' : xᴴ ∈ wordSpan U) :
    transferMap U U' h ⟨xᴴ, hx'⟩ = (transferMap U U' h ⟨x, hx⟩)ᴴ := by
  induction hx using Submodule.span_induction with
  | mem x hx =>
    obtain ⟨w, rfl⟩ := hx
    rw [transferMap_wordEval, transferMap_apply_of_eq h hx' (Finsupp.single (wordStar w) 1)
      (by rw [Finsupp.linearCombination_single, one_smul, wordEval_wordStar]),
      Finsupp.linearCombination_single, one_smul, wordEval_wordStar]
  | zero =>
    have e : (⟨(0 : Matrix H H ℂ)ᴴ, hx'⟩ : wordSpan U) = 0 := Subtype.ext conjTranspose_zero
    rw [e, map_zero]
    show (0 : Matrix H H ℂ) = (transferMap U U' h 0)ᴴ
    rw [map_zero, conjTranspose_zero]
  | add x z hx hz ihx ihz =>
    have e : (⟨(x + z)ᴴ, hx'⟩ : wordSpan U)
        = ⟨xᴴ, conjTranspose_mem_wordSpan U hx⟩ + ⟨zᴴ, conjTranspose_mem_wordSpan U hz⟩ :=
      Subtype.ext (conjTranspose_add _ _)
    have e' : (⟨x + z, add_mem hx hz⟩ : wordSpan U) = ⟨x, hx⟩ + ⟨z, hz⟩ := rfl
    rw [e, map_add, ihx _, ihz _, e', map_add, conjTranspose_add]
  | smul a x hx ih =>
    have e : (⟨(a • x)ᴴ, hx'⟩ : wordSpan U) = star a • ⟨xᴴ, conjTranspose_mem_wordSpan U hx⟩ :=
      Subtype.ext (conjTranspose_smul _ _)
    have e' : (⟨a • x, Submodule.smul_mem _ a hx⟩ : wordSpan U) = a • ⟨x, hx⟩ := rfl
    rw [e, map_smul, ih _, e', map_smul, conjTranspose_smul]

/-- **`WT1`(iii)** — injective: `Tr[xᴴ x] = Tr[φ(x)ᴴ φ(x)]` by the `*`, product and trace
properties, so `φ(x) = 0` forces `x = 0`. -/
theorem transferMap_injective {U U' : Matrix (V × H) (V × H) ℂ} (h : WordTracesEqual U U') :
    Function.Injective (transferMap U U' h) := by
  rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
  rintro ⟨x, hx⟩ h0
  have key : trace (xᴴ * x)
      = trace ((transferMap U U' h ⟨x, hx⟩)ᴴ * transferMap U U' h ⟨x, hx⟩) := by
    rw [← transferMap_conjTranspose h hx (conjTranspose_mem_wordSpan U hx),
      ← transferMap_mul h (conjTranspose_mem_wordSpan U hx) hx
        (mul_mem_wordSpan U (conjTranspose_mem_wordSpan U hx) hx)]
    exact (transferMap_trace h
      ⟨xᴴ * x, mul_mem_wordSpan U (conjTranspose_mem_wordSpan U hx) hx⟩).symm
  rw [h0, conjTranspose_zero, mul_zero, trace_zero] at key
  exact Subtype.ext (Matrix.trace_conjTranspose_mul_self_eq_zero_iff.1 key)

/-- **`WT1` — the trace-form kernel step, assembled.** For `U, U'` with equal word traces there is
a linear map `φ : 𝒲(U) →ₗ[ℂ] M_m(ℂ)` with `φ(w(U)) = w(U')` for every word, range `𝒲(U')`,
injective, unital, multiplicative, `*`-preserving and trace-preserving. No unitarity hypothesis. -/
theorem WT1_transfer (U U' : Matrix (V × H) (V × H) ℂ) (h : WordTracesEqual U U') :
    ∃ φ : wordSpan U →ₗ[ℂ] Matrix H H ℂ,
      (∀ (w : List (V × V × Bool)) (hw : wordEval U w ∈ wordSpan U),
        φ ⟨wordEval U w, hw⟩ = wordEval U' w) ∧
      LinearMap.range φ = wordSpan U' ∧
      Function.Injective φ ∧
      φ ⟨1, one_mem_wordSpan U⟩ = 1 ∧
      (∀ (x y : Matrix H H ℂ) (hx : x ∈ wordSpan U) (hy : y ∈ wordSpan U)
        (hxy : x * y ∈ wordSpan U), φ ⟨x * y, hxy⟩ = φ ⟨x, hx⟩ * φ ⟨y, hy⟩) ∧
      (∀ (x : Matrix H H ℂ) (hx : x ∈ wordSpan U) (hx' : xᴴ ∈ wordSpan U),
        φ ⟨xᴴ, hx'⟩ = (φ ⟨x, hx⟩)ᴴ) ∧
      (∀ x : wordSpan U, trace (φ x) = trace (x : Matrix H H ℂ)) :=
  ⟨transferMap U U' h, transferMap_wordEval h, transferMap_range h, transferMap_injective h,
    transferMap_one h, fun _ _ hx hy hxy => transferMap_mul h hx hy hxy,
    fun _ hx hx' => transferMap_conjTranspose h hx hx', transferMap_trace h⟩

/-! ### Section F — the matrix-unit construction: a multiplicative `*`-map of `M_m(ℂ)` that is
injective is conjugation by a unitary

With `e_{ij} := ψ(E_{ij})`: the `e_{ij}` are matrix units, `e_{oo}` is a nonzero orthogonal
projection, `ξ` is a nonzero column of it (so `e_{oo} ξ = ξ`), `W₀` has columns `e_{jo} ξ`,
`W₀ᴴ W₀ = ‖ξ‖² 𝟙`, `W := ‖ξ‖⁻¹ W₀` is unitary, `W E_{ij} = e_{ij} W`, hence `W E_{ij} Wᴴ = e_{ij}`
and `ψ = Ad W` by linearity. Finite matrix algebra only. -/

theorem single_mul_single_ite (i j k l : H) :
    Matrix.single i j (1 : ℂ) * Matrix.single k l 1 = if j = k then Matrix.single i l 1 else 0 := by
  by_cases hjk : j = k
  · subst hjk
    rw [if_pos rfl, Matrix.single_mul_single_same, mul_one]
  · rw [if_neg hjk]
    simp [hjk]

theorem conjTranspose_single_one (i j : H) :
    (Matrix.single i j (1 : ℂ))ᴴ = Matrix.single j i 1 := by
  ext a b
  simp only [conjTranspose_apply, Matrix.single, of_apply]
  by_cases h1 : i = b <;> by_cases h2 : j = a <;> simp [h1, h2]

/-- **The matrix-unit construction.** -/
theorem exists_unitary_of_starMul (ψ : Matrix H H ℂ →ₗ[ℂ] Matrix H H ℂ)
    (hmul : ∀ x y, ψ (x * y) = ψ x * ψ y) (hstar : ∀ x, ψ xᴴ = (ψ x)ᴴ)
    (hinj : Function.Injective ψ) :
    ∃ W : Matrix H H ℂ, Wᴴ * W = 1 ∧ ∀ x, ψ x = W * x * Wᴴ := by
  rcases isEmpty_or_nonempty H with hH | hH
  · exact ⟨1, Subsingleton.elim _ _, fun _ => Subsingleton.elim _ _⟩
  obtain ⟨o⟩ := hH
  -- the images of the matrix units
  set e : H → H → Matrix H H ℂ := fun i j => ψ (Matrix.single i j 1) with he
  have hee : ∀ i j k l, e i j * e k l = if j = k then e i l else 0 := by
    intro i j k l
    simp only [he]
    rw [← hmul, single_mul_single_ite]
    by_cases hjk : j = k
    · simp [hjk]
    · simp [hjk]
  have hestar : ∀ i j, (e i j)ᴴ = e j i := by
    intro i j
    simp only [he]
    rw [← hstar, conjTranspose_single_one]
  -- `e o o` is nonzero, so it has a nonzero column `v`, fixed by `e o o`
  have hne : e o o ≠ 0 := by
    intro h0
    have h1 : Matrix.single o o (1 : ℂ) = 0 := hinj (by rw [map_zero]; exact h0)
    have h2 := congrFun (congrFun h1 o) o
    simp at h2
  obtain ⟨k, hk⟩ : ∃ k, (fun i => e o o i k) ≠ 0 := by
    by_contra hall
    apply hne
    ext i k
    exact congrFun (Classical.byContradiction fun hk => hall ⟨k, hk⟩) i
  set v : H → ℂ := fun i => e o o i k with hv
  have hvfix : e o o *ᵥ v = v := by
    ext i
    have := congrFun (congrFun (hee o o o o) i) k
    rw [if_pos rfl, mul_apply] at this
    simpa only [mulVec, dotProduct, hv] using this
  -- the norm of `v`
  set s : ℝ := ∑ i, Complex.normSq (v i) with hs_def
  have hs : 0 < s := by
    obtain ⟨i, hi⟩ : ∃ i, v i ≠ 0 := by
      by_contra hall
      exact hk (funext fun i => Classical.byContradiction fun hi => hall ⟨i, hi⟩)
    exact Finset.sum_pos' (fun _ _ => Complex.normSq_nonneg _)
      ⟨i, Finset.mem_univ _, Complex.normSq_pos.2 hi⟩
  have hsv : star v ⬝ᵥ v = (s : ℂ) := by
    simp only [dotProduct, Pi.star_apply, hs_def, Complex.ofReal_sum,
      Complex.normSq_eq_conj_mul_self, Complex.star_def]
  -- `W₀`, with columns `e j o *ᵥ v`
  set W₀ : Matrix H H ℂ := Matrix.of fun i j => (e j o *ᵥ v) i with hW₀
  have colW : ∀ (M : Matrix H H ℂ) a b, (M * W₀) a b = ((M * e b o) *ᵥ v) a := by
    intro M a b
    rw [← mulVec_mulVec]
    rfl
  have hgram : W₀ᴴ * W₀ = (s : ℂ) • (1 : Matrix H H ℂ) := by
    ext i j
    have e1 : (W₀ᴴ * W₀) i j = star (e i o *ᵥ v) ⬝ᵥ (e j o *ᵥ v) := by
      simp only [mul_apply, conjTranspose_apply, hW₀, of_apply, dotProduct, Pi.star_apply]
    rw [e1, star_mulVec, dotProduct_mulVec, vecMul_vecMul, ← dotProduct_mulVec, hestar, hee]
    by_cases hij : i = j
    · subst hij
      simp [hvfix, hsv]
    · simp [hij]
  have hint : ∀ i j, W₀ * Matrix.single i j 1 = e i j * W₀ := by
    intro i j
    ext a b
    rw [colW, hee]
    by_cases hjb : j = b
    · subst hjb
      rw [if_pos rfl, Matrix.mul_single_apply_same, mul_one]
      rfl
    · rw [if_neg hjb, Matrix.mul_single_apply_of_ne _ _ _ _ _ (Ne.symm hjb), zero_mulVec]
      rfl
  -- the normalised `W`
  set c : ℂ := ((Real.sqrt s : ℝ) : ℂ)⁻¹ with hc_def
  have hc : star c * c = ((s⁻¹ : ℝ) : ℂ) := by
    rw [hc_def, Complex.star_def, ← Complex.ofReal_inv, Complex.conj_ofReal, ← Complex.ofReal_mul,
      ← mul_inv, Real.mul_self_sqrt hs.le]
  set W : Matrix H H ℂ := c • W₀ with hW_def
  have hWW : Wᴴ * W = 1 := by
    rw [hW_def, conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, hgram, smul_smul, smul_smul,
      hc, ← Complex.ofReal_mul, inv_mul_cancel₀ hs.ne', Complex.ofReal_one, one_smul]
  have hWint : ∀ i j, W * Matrix.single i j 1 = e i j * W := by
    intro i j
    rw [hW_def, Matrix.smul_mul, Matrix.mul_smul, hint]
  have hunit : ∀ i j, W * Matrix.single i j 1 * Wᴴ = e i j := by
    intro i j
    rw [hWint, Matrix.mul_assoc, mul_eq_one_comm.1 hWW, Matrix.mul_one]
  refine ⟨W, hWW, fun x => ?_⟩
  have hx : x = ∑ i, ∑ j, x i j • Matrix.single i j (1 : ℂ) := by
    conv_lhs => rw [Matrix.matrix_eq_sum_single x]
    simp only [Matrix.smul_single, smul_eq_mul, mul_one]
  rw [hx]
  simp only [map_sum, map_smul, Matrix.sum_mul, Matrix.mul_sum, Matrix.smul_mul, Matrix.mul_smul,
    hunit, he]

/-! ### Section G — `WT2-gen` and `WT3` on the spanning class -/

/-- **`WT2-gen`, one-sided form — the construction.** If the word span of `U` is all of
`M_m(ℂ)` and the word traces agree, then `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` for a unitary `W`, built by
the matrix-unit construction from `φ(E_{ij})`. Only `BlockSpanning U` is consumed: `φ` is then a
multiplicative, `*`-preserving, injective linear map of all of `M_m(ℂ)`, which is all
`exists_unitary_of_starMul` needs. No unitarity hypothesis on `U, U'` is needed. -/
theorem WT2gen_oneSided (U U' : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U)
    (h : WordTracesEqual U U') : HiddenConjugate U U' := by
  have hmem : ∀ x : Matrix H H ℂ, x ∈ wordSpan U := fun x => hU ▸ Submodule.mem_top
  let ψ : Matrix H H ℂ →ₗ[ℂ] Matrix H H ℂ :=
    transferMap U U' h ∘ₗ (LinearEquiv.ofTop (wordSpan U) hU).symm.toLinearMap
  have hψ : ∀ x (hx : x ∈ wordSpan U), ψ x = transferMap U U' h ⟨x, hx⟩ := fun x hx => by
    simp only [ψ, LinearMap.comp_apply, LinearEquiv.coe_coe]
    congr 1
  obtain ⟨W, hW, hWx⟩ := exists_unitary_of_starMul ψ
    (fun x y => by
      rw [hψ _ (hmem _), hψ _ (hmem _), hψ _ (hmem _)]
      exact transferMap_mul h (hmem x) (hmem y) (hmem _))
    (fun x => by
      rw [hψ _ (hmem _), hψ _ (hmem _)]
      exact transferMap_conjTranspose h (hmem x) (hmem _))
    (by
      intro x y hxy
      rw [hψ _ (hmem _), hψ _ (hmem _)] at hxy
      exact congrArg Subtype.val (transferMap_injective h hxy))
  have hb : ∀ v w, visibleBlock U' v w = W * visibleBlock U v w * Wᴴ := by
    intro v w
    rw [← hWx, hψ _ (hmem _), transferMap_apply_of_eq h _ (Finsupp.single [(v, w, true)] 1)
      (by rw [Finsupp.linearCombination_single, one_smul, visibleBlock_eq_wordEval]),
      Finsupp.linearCombination_single, one_smul, visibleBlock_eq_wordEval]
  refine ⟨W, hW, ?_⟩
  ext ⟨v, k⟩ ⟨w, l⟩
  have e := congrFun (congrFun (visibleBlock_conj (1 : Equiv.Perm V) W U v w) k) l
  simp only [Matrix.permMatrix_one, Equiv.Perm.coe_one, id_eq] at e
  rw [← hb] at e
  exact e.symm

set_option linter.unusedVariables false in
/-- **`WT2-gen` — unitary implementation on the spanning class, two-sided as frozen**: if the
word spans of `U` and `U'` are both all of `M_m(ℂ)` and the word traces agree, then
`HiddenConjugate U U'`. This is the statement the label attaches to; its second spanning
hypothesis is carried because the freeze states the two-sided form, and the proof does not use
it (`WT2gen_oneSided` is the strengthening). -/
theorem WT2gen_hiddenConjugate (U U' : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U)
    (hU' : BlockSpanning U') (h : WordTracesEqual U U') : HiddenConjugate U U' :=
  WT2gen_oneSided U U' hU h

/-- **`BlockSpanning U'` follows from `BlockSpanning U`** and word-trace equality: the induced map
is injective from the `m²`-dimensional `𝒲(U)` into `M_m(ℂ)` with range `𝒲(U')`. -/
theorem blockSpanning_of_wordTracesEqual {U U' : Matrix (V × H) (V × H) ℂ}
    (hU : BlockSpanning U) (h : WordTracesEqual U U') : BlockSpanning U' := by
  unfold BlockSpanning at hU ⊢
  rw [← transferMap_range h]
  apply Submodule.eq_top_of_finrank_eq
  rw [LinearMap.finrank_range_of_inj (transferMap_injective h), hU, finrank_top]

/-- **`WT3` — sufficiency on the spanning class**, stated with the inline quantifier of the
freeze: on every finite carrier `V × H`, for `U, U'` whose word spans are all of `M_m(ℂ)`,
`(∀ w, Tr[wordEval U w] = Tr[wordEval U' w]) → HiddenConjugate U U'`. Unitarity of `U, U'` is not
used and is not carried. -/
theorem WT3_spanning (U U' : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U)
    (hU' : BlockSpanning U') :
    (∀ w : List (V × V × Bool), trace (wordEval U w) = trace (wordEval U' w)) →
      HiddenConjugate U U' :=
  fun h => WT2gen_hiddenConjugate U U' hU hU' h

/-- **`WT3`, the biconditional on the spanning class**: hidden conjugation **iff** equal word
traces, the reverse direction being the consumed necessity `trace_wordEval_hiddenConjugate`. -/
theorem WT3_spanning_iff (U U' : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U)
    (hU' : BlockSpanning U') : HiddenConjugate U U' ↔ WordTracesEqual U U' :=
  ⟨fun hc w => (trace_wordEval_hiddenConjugate hc w).symm, WT2gen_hiddenConjugate U U' hU hU'⟩

/-! ### Section H — `WT4`: a finite spanning family of words -/

/-- **`WT4`.** Some finite family of words spans `𝒲(U)`: a linearly independent subfamily of the
word values spanning the same subspace is finite, since `M_m(ℂ)` is finite-dimensional. No bound
on word length is claimed. -/
theorem WT4_finite_spanning_family (U : Matrix (V × H) (V × H) ℂ) :
    ∃ S : Finset (List (V × V × Bool)), Submodule.span ℂ (wordEval U '' ↑S) = wordSpan U := by
  classical
  obtain ⟨b, hb, hspan, hli⟩ := exists_linearIndependent ℂ (Set.range (wordEval U))
  have hfin : b.Finite := hli.set_finite_of_isNoetherian
  have hsub : ↑hfin.toFinset ⊆ wordEval U '' Set.univ := by
    rw [Set.Finite.coe_toFinset, Set.image_univ]
    exact hb
  obtain ⟨S, -, hS⟩ := Finset.subset_set_image_iff.1 hsub
  refine ⟨S, ?_⟩
  rw [← Finset.coe_image, hS, Set.Finite.coe_toFinset, hspan]

/-! ### Section I — `WT0`: the controls

Pair C's permutations are the merged ones, restated as local notation (syntax, not declarations),
and every witness is pinned by an equation inside the statement that needs it. -/

/-- Pair C, `φ`: `(0,2) ↔ (1,0)` and `(1,1) ↔ (1,2)`, fixing `(0,0)` and `(0,1)`. -/
local notation "φC" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) *
  Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)))
/-- Pair C, `φ'`: `φ` composed with the additional transposition `(0,0) ↔ (0,1)`. -/
local notation "φC'" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) *
  Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)) *
  Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)))
/-- The hidden transposition `1 ↔ 2` of `ℤ₃`. -/
local notation "τ" => (Equiv.swap (1 : Fin 3) 2)

/-- **`WT0(b)`.** The `ST3` pair is excluded from the hypothesis of sufficiency: its word traces
differ on the merged length-six word `U₀₀ U₁₀ U₀₁ U₀₀ᴴ U₀₁ᴴ U₁₀ᴴ` (`1` on `φ̂_C`, `0` on `φ̂_C'`,
by `pairC_wordTraces`). -/
theorem WT0b_pairC_not_wordTracesEqual :
    ∃ U U' : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ,
      U = Equiv.Perm.permMatrix ℂ φC ∧ U' = Equiv.Perm.permMatrix ℂ φC' ∧
      ¬ WordTracesEqual U U' := by
  obtain ⟨t1, t2, -⟩ := pairC_wordTraces
  refine ⟨_, _, rfl, rfl, fun h => ?_⟩
  have := h [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
    (0, 0, false), (0, 1, false), (1, 0, false)]
  rw [t1, t2] at this
  exact one_ne_zero this

/-- The permutation matrix of the hidden transposition. -/
theorem tau_permMatrix :
    Equiv.Perm.permMatrix ℂ τ = !![1, 0, 0; 0, 0, 1; 0, 1, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Equiv.swap_apply_def]

/-- **`WT0(c)` — the positive control with the conjugation exhibited.** `U = φ̂_C`,
`W = P_{(1 2)}` the permutation unitary of the hidden transposition, `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`:
`Wᴴ W = 1`, `HiddenConjugate U U'`, `U' ≠ U` (the `(0,1)` block moves), and
`WordTracesEqual U U'` by the consumed necessity. -/
theorem WT0c_positive_control :
    ∃ (U U' : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ) (W : Matrix (Fin 3) (Fin 3) ℂ),
      U = Equiv.Perm.permMatrix ℂ φC ∧ W = Equiv.Perm.permMatrix ℂ τ ∧
      U' = ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ W) * U * ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ W)ᴴ ∧
      Wᴴ * W = 1 ∧ HiddenConjugate U U' ∧ U' ≠ U ∧ WordTracesEqual U U' := by
  have hτ : τ * τ = 1 := Equiv.swap_mul_self _ _
  have hWs : (Equiv.Perm.permMatrix ℂ τ)ᴴ = Equiv.Perm.permMatrix ℂ τ :=
    permMatrix_conjTranspose_self _ hτ
  have hW : (Equiv.Perm.permMatrix ℂ τ)ᴴ * Equiv.Perm.permMatrix ℂ τ = 1 := by
    rw [hWs]; exact permMatrix_mul_self _ hτ
  have hconj : HiddenConjugate (Equiv.Perm.permMatrix ℂ φC)
      (((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ Equiv.Perm.permMatrix ℂ τ) * Equiv.Perm.permMatrix ℂ φC *
        ((1 : Matrix (Fin 2) (Fin 2) ℂ) ⊗ₖ Equiv.Perm.permMatrix ℂ τ)ᴴ) :=
    ⟨_, hW, rfl⟩
  refine ⟨_, _, _, rfl, rfl, rfl, hW, hconj, ?_,
    fun w => (trace_wordEval_hiddenConjugate hconj w).symm⟩
  intro heq
  obtain ⟨-, b01, -, -, -, -, -, -⟩ := pairC_blocks
  have e := visibleBlock_conj (1 : Equiv.Perm (Fin 2)) (Equiv.Perm.permMatrix ℂ τ)
    (Equiv.Perm.permMatrix ℂ φC) 0 1
  rw [Matrix.permMatrix_one, heq, hWs] at e
  simp only [Equiv.Perm.coe_one, id_eq, b01, tau_permMatrix] at e
  have := congrFun (congrFun e 1) 0
  simp at this

end WordTraceSufficiency
end OIBridge

#print axioms OIBridge.WordTraceSufficiency.wordEval_nil
#print axioms OIBridge.WordTraceSufficiency.wordEval_append
#print axioms OIBridge.WordTraceSufficiency.visibleBlock_eq_wordEval
#print axioms OIBridge.WordTraceSufficiency.wordStar_cons
#print axioms OIBridge.WordTraceSufficiency.wordEval_wordStar
#print axioms OIBridge.WordTraceSufficiency.wordEval_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.one_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.visibleBlock_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.wordEval_mul_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.mul_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.conjTranspose_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.exists_linearCombination
#print axioms OIBridge.WordTraceSufficiency.linearCombination_mem_wordSpan
#print axioms OIBridge.WordTraceSufficiency.trace_linearCombination_gram
#print axioms OIBridge.WordTraceSufficiency.gram_eq_of_wordTracesEqual
#print axioms OIBridge.WordTraceSufficiency.linearCombination_eq_zero_of_wordTracesEqual
#print axioms OIBridge.WordTraceSufficiency.ker_linearCombination_le
#print axioms OIBridge.WordTraceSufficiency.transferMap_linearCombination
#print axioms OIBridge.WordTraceSufficiency.transferMap_apply_of_eq
#print axioms OIBridge.WordTraceSufficiency.transferMap_wordEval
#print axioms OIBridge.WordTraceSufficiency.transferMap_range
#print axioms OIBridge.WordTraceSufficiency.transferMap_one
#print axioms OIBridge.WordTraceSufficiency.transferMap_trace
#print axioms OIBridge.WordTraceSufficiency.transferMap_wordEval_mul
#print axioms OIBridge.WordTraceSufficiency.transferMap_mul
#print axioms OIBridge.WordTraceSufficiency.transferMap_conjTranspose
#print axioms OIBridge.WordTraceSufficiency.transferMap_injective
#print axioms OIBridge.WordTraceSufficiency.WT1_transfer
#print axioms OIBridge.WordTraceSufficiency.single_mul_single_ite
#print axioms OIBridge.WordTraceSufficiency.conjTranspose_single_one
#print axioms OIBridge.WordTraceSufficiency.exists_unitary_of_starMul
#print axioms OIBridge.WordTraceSufficiency.WT2gen_oneSided
#print axioms OIBridge.WordTraceSufficiency.WT2gen_hiddenConjugate
#print axioms OIBridge.WordTraceSufficiency.blockSpanning_of_wordTracesEqual
#print axioms OIBridge.WordTraceSufficiency.WT3_spanning
#print axioms OIBridge.WordTraceSufficiency.WT3_spanning_iff
#print axioms OIBridge.WordTraceSufficiency.WT4_finite_spanning_family
#print axioms OIBridge.WordTraceSufficiency.WT0b_pairC_not_wordTracesEqual
#print axioms OIBridge.WordTraceSufficiency.tau_permMatrix
#print axioms OIBridge.WordTraceSufficiency.WT0c_positive_control
