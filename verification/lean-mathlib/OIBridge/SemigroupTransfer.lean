import OIBridge.StinespringUniqueness
import OIBridge.UhlmannUniqueness
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

/-!
# Substratum Lemma 24.1 — the semigroup-transfer step

Executed under the frozen control plane
`verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md`, blob
`b8168df9ed1acff21eb89e84487b43470124f845`, from `main` at
`c46e1606d4cafe2720afd69dc06c667eb0f1acff` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## What this round tests

Lemma 24.1's step (2): that equality of the **uniform-prior channel family**
`Φ_t(ρ) = Tr_H[U^t (ρ ⊗ 𝟙/m) U^{-t}]` for every `t` fixes the dilating unitary `U` up to a hidden
conjugation `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`. Every target is stated in the completeness-relevant
direction — from equal families to a conjugating `W` — and every negative is earned by a trace
certificate proved in the kernel, never by a failed search over `W`.

## The targets and where they land

* **`ST0`** — `familyAt_single` (the block-trace form `Φ_t(E_{ab})_{cd} = (1/m)·Tr[(U^t)_{ca}((U^t)_{db})ᴴ]`),
  `familyAt_eq_stinespringChannel` and `purifiedIsometry_apply` (the purification: `Φ_t` is the
  pure-reference family of `U^t ⊗ 𝟙` with reference `Ω = m^{-1/2} Σ_h |h⟩|h⟩`), and
  `ST0c_cyclic_iff` (GNS cyclicity of the reference subspace **iff** `HiddenCommutantTrivial U`,
  through the commutant computation `eq_oneKron_of_comm`/`slice_comm` and the projection lemma
  `starProjection_comm`).
* **`ST1`** — `readingA_perTime`: equal families give, **for each `t` separately**, a unitary
  `W_t` on `ℂ^{H × H}` with `X'_t = X_t W_t`, by `ST0(b)` and `rightUnitary_of_gram`. The
  existential sits inside the `∀ t`; no constancy or product form follows.
  **`ST1′`** — `familyAt_hiddenConjugate`: hidden conjugation preserves the family at every `t`.
* **`ST2`** — `ST2_pairA`, **negative**: Pair A on `ℤ₂ × ℤ₂` has equal families and no hidden
  unitary relates it (block-trace certificate `2 ≠ 0`), and is absorbed by generator (i)'s
  visible part, `φ̂' = (X ⊗ 𝟙) φ̂ (X ⊗ 𝟙)`.
* **`ST3`** — `ST3_pairC`, **negative**: Pair C on `ℤ₂ × ℤ₃` has both hidden commutants trivial,
  equal families, non-trivial visible statistics, and **no unitary whatsoever** relates it
  (`Tr φ̂ = 2 ≠ 0 = Tr φ̂'`).
* **`ST4`** — `ST4_pairC`, **negative**: Pair C is not related by `P_σ ⊗ W` after any decoupled
  enlargement by unitaries on any finite non-empty `D`, by the balanced word
  `U₀₀U₁₀U₀₁U₀₀ᴴU₀₁ᴴU₁₀ᴴ` under both visible relabellings, the enlargement lemma
  `trace_wordEval_enlarge` and the relabelling lemma `trace_wordEval_conj`.
* **`ST5`** — necessity at level 2 (`trace_wordEval_hiddenConjugate`: hidden conjugation
  preserves every word trace); **sufficiency is not attempted here** — the trace-form kernel
  argument and the unitary implementation of a trace-preserving `*`-isomorphism between
  `*`-subalgebras of `M_m(ℂ)` are not carried by Mathlib or the corpus, and the frozen fallback
  applies.

## Discipline

Six top-level definitions, the six frozen slots: `familyAt`, `HiddenCommutantTrivial`,
`HiddenConjugate`, `visibleBlock`, `wordEval` (slot 5, fired), `enlarge` (slot 6, fired). The
witness permutations are local notations for explicit products of transpositions, pinned by
`U = φ.permMatrix ℂ` inside the statements; no witness, `W`, carrier, word or enlargement is a
top-level definition. `krausMap`, `krausMap_single`, `stinespringChannel`, `krausOf`,
`channel_eq_krausMap` and `rightUnitary_of_gram` are consumed unmodified; act 7's
`permMatrix_apply_eq` is re-proved locally as `permMatrix_entry` so that no Track B module is
imported. The module carries no unproved declaration, no added axioms, and no kernel-bypassing
decision procedure; every named result prints only `[propext, Classical.choice, Quot.sound]`.

Nothing here says the four generator families fail to exhaust `𝒢_sub`, and nothing says they do:
the present completeness proof route remains conditional, and repairing it needs stronger
multi-time data — such as `ST5`'s full word-trace hypothesis — or a different argument.
-/

namespace OIBridge
namespace SemigroupTransfer

set_option autoImplicit false
set_option linter.unusedSectionVars false

open Matrix Finset KrausUniqueness StinespringUniqueness UhlmannUniqueness
open scoped Kronecker ComplexConjugate

variable {V H : Type} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]

/-! ### Section A — the six budget slots (four needed, two conditional)

The carrier is `V × H` with `V` the visible and `H` the hidden factor; a dilation datum is a
matrix `U` on it (unitarity is a hypothesis where a statement needs it). -/

/-- **Slot 4.** The `m × m` visible block `U_{vw} = (⟨v| ⊗ 𝟙) U (|w⟩ ⊗ 𝟙)`. -/
def visibleBlock (U : Matrix (V × H) (V × H) ℂ) (v w : V) : Matrix H H ℂ :=
  Matrix.of fun h h' => U (v, h) (w, h')

/-- **Slot 1.** The uniform-prior family at time `t`: `Φ_t(ρ) = Tr_H[U^t (ρ ⊗ 𝟙/m) U^{-t}]`, written
as the `m²`-member Kraus map with operators `(U^t)(·, h)(·, h')` indexed by `H × H` and the scalar
`1/m` in front. Its block-trace form is `familyAt_single`, its purification
`familyAt_eq_stinespringChannel`. -/
noncomputable def familyAt (U : Matrix (V × H) (V × H) ℂ) (t : ℕ) (ρ : Matrix V V ℂ) :
    Matrix V V ℂ :=
  ((Fintype.card H : ℂ)⁻¹) •
    krausMap (fun p : H × H => Matrix.of fun a b => (U ^ t) (a, p.1) (b, p.2)) ρ

/-- **Slot 2.** The operative cyclicity predicate: every hidden operator commuting with `U` is a
scalar. -/
def HiddenCommutantTrivial (U : Matrix (V × H) (V × H) ℂ) : Prop :=
  ∀ Y : Matrix H H ℂ, ((1 : Matrix V V ℂ) ⊗ₖ Y) * U = U * ((1 : Matrix V V ℂ) ⊗ₖ Y) →
    ∃ c : ℂ, Y = c • (1 : Matrix H H ℂ)

/-- **Slot 3.** Hidden conjugation: `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` for a unitary `W` on the hidden
factor. -/
def HiddenConjugate (U U' : Matrix (V × H) (V × H) ℂ) : Prop :=
  ∃ W : Matrix H H ℂ, Wᴴ * W = 1 ∧
    U' = ((1 : Matrix V V ℂ) ⊗ₖ W) * U * ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ

/-- **Slot 5 (conditional, fired).** A block word is a list of letters `(v, w, plain?)`; its value
is the ordered product of the blocks `U_{vw}` (plain letter) and `U_{vw}ᴴ` (adjoint letter). -/
def wordEval (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool)) : Matrix H H ℂ :=
  (w.map fun l => if l.2.2 then visibleBlock U l.1 l.2.1 else (visibleBlock U l.1 l.2.1)ᴴ).prod

/-- **Slot 6 (conditional, fired).** Decoupled enlargement `U ⊗ δ`, re-indexed onto the carrier
`V × (H × D)` so that `H × D` is the enlarged hidden factor. -/
def enlarge {D : Type} [Fintype D] [DecidableEq D] (U : Matrix (V × H) (V × H) ℂ)
    (δ : Matrix D D ℂ) : Matrix (V × (H × D)) (V × (H × D)) ℂ :=
  (U ⊗ₖ δ).reindex (Equiv.prodAssoc V H D) (Equiv.prodAssoc V H D)

/-- The net power of a word: plain letters count `+1`, adjoint letters `-1`. A word is
*balanced* when this is `0`. (A statement-level abbreviation is not used; the expression is
written out where it is needed.) -/
theorem enlarge_apply {D : Type} [Fintype D] [DecidableEq D] (U : Matrix (V × H) (V × H) ℂ)
    (δ : Matrix D D ℂ) (a b : V) (h k : H) (d d' : D) :
    enlarge U δ (a, (h, d)) (b, (k, d')) = U (a, h) (b, k) * δ d d' := by
  simp [enlarge, reindex_apply, submatrix_apply]

@[simp] theorem visibleBlock_apply (U : Matrix (V × H) (V × H) ℂ) (v w : V) (h h' : H) :
    visibleBlock U v w h h' = U (v, h) (w, h') := rfl

theorem visibleBlock_enlarge {D : Type} [Fintype D] [DecidableEq D]
    (U : Matrix (V × H) (V × H) ℂ) (δ : Matrix D D ℂ) (v w : V) :
    visibleBlock (enlarge U δ) v w = visibleBlock U v w ⊗ₖ δ := by
  ext ⟨h, d⟩ ⟨k, d'⟩
  simp [enlarge_apply]

/-! ### Section B — `ST0(b)`: the block-trace form of the family -/

/-- **`ST0(b)`.** `Φ_t(E_{ab})_{cd} = (1/m) · Tr[(U^t)_{ca} ((U^t)_{db})ᴴ]`. -/
theorem familyAt_single (U : Matrix (V × H) (V × H) ℂ) (t : ℕ) (a b c d : V) :
    familyAt U t (Matrix.single a b 1) c d
      = (Fintype.card H : ℂ)⁻¹ *
          trace (visibleBlock (U ^ t) c a * (visibleBlock (U ^ t) d b)ᴴ) := by
  unfold familyAt
  rw [Matrix.smul_apply, krausMap_single, smul_eq_mul]
  congr 1
  simp only [trace, diag_apply, mul_apply, conjTranspose_apply, visibleBlock_apply, of_apply,
    Fintype.sum_prod_type]
  rfl

/-- The synthesis Gram entry of the amplitude matrix is the same block trace. -/
theorem amplitude_gram_entry (U : Matrix (V × H) (V × H) ℂ) (t : ℕ) (a b c d : V) :
    ((Matrix.of fun (q : V × V) (p : H × H) => (U ^ t) (q.1, p.1) (q.2, p.2)) *
        (Matrix.of fun (q : V × V) (p : H × H) => (U ^ t) (q.1, p.1) (q.2, p.2))ᴴ) (a, b) (c, d)
      = trace (visibleBlock (U ^ t) a b * (visibleBlock (U ^ t) c d)ᴴ) := by
  simp only [trace, diag_apply, mul_apply, conjTranspose_apply, visibleBlock_apply, of_apply,
    Fintype.sum_prod_type]

/-! ### Section C — `ST0(a)`: the purification -/

/-- The Kraus family of a matrix-defined dilation reads off the matrix. -/
theorem krausOf_toEuclideanLin {e : Type} [Fintype e] [DecidableEq e]
    (M : Matrix (V × e) V ℂ) (i : e) (a b : V) :
    krausOf (Matrix.toEuclideanLin M) i a b = M (a, i) b := by
  simp [krausOf, vmat, Matrix.toLpLin_apply]

/-- Scaling every Kraus operator by `c` scales the map by `|c|²`. -/
theorem krausMap_smul {I : Type} [Fintype I] (c : ℂ) (A : I → Matrix V V ℂ) (ρ : Matrix V V ℂ) :
    krausMap (fun i => c • A i) ρ = (star c * c) • krausMap A ρ := by
  simp only [krausMap, conjTranspose_smul, Finset.smul_sum, smul_mul_assoc, mul_smul_comm,
    smul_smul]

theorem sqrt_scalar_sq (m : ℕ) :
    star (((Real.sqrt m : ℝ) : ℂ)⁻¹) * (((Real.sqrt m : ℝ) : ℂ)⁻¹) = (m : ℂ)⁻¹ := by
  rw [Complex.star_def, ← Complex.ofReal_inv, Complex.conj_ofReal, ← Complex.ofReal_mul,
    ← mul_inv, Real.mul_self_sqrt (Nat.cast_nonneg m), Complex.ofReal_inv, Complex.ofReal_natCast]

/-- **`ST0(a)`, the isometry.** The purified isometry `V_t ψ = (U^t ⊗ 𝟙)(ψ ⊗ Ω)` with
`Ω = m^{-1/2} Σ_h |h⟩|h⟩`, written on the carrier `V × (H × H')`: the matrix
`m^{-1/2} (U^t)(a, h)(b, h')` applied to `ψ` is `U^t ⊗ 𝟙_{H'}` applied to `ψ ⊗ Ω`. -/
theorem purifiedIsometry_apply (U : Matrix (V × H) (V × H) ℂ) (t : ℕ)
    (ψ : EuclideanSpace ℂ V) (p : V × (H × H)) :
    Matrix.toEuclideanLin (Matrix.of fun (p : V × (H × H)) (b : V) =>
        (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) * (U ^ t) (p.1, p.2.1) (b, p.2.2)) ψ p
      = (enlarge (U ^ t) (1 : Matrix H H ℂ) *ᵥ fun q : V × (H × H) =>
          ψ q.1 * ((((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) *
            (1 : Matrix H H ℂ) q.2.1 q.2.2)) p := by
  obtain ⟨a, h, h'⟩ := p
  simp only [Matrix.toLpLin_apply, WithLp.ofLp_toLp, mulVec, dotProduct, of_apply,
    Fintype.sum_prod_type, enlarge_apply, one_apply]
  simp only [mul_ite, ite_mul, mul_one, mul_zero, zero_mul, Finset.sum_ite_eq, Finset.mem_univ,
    if_true]
  exact Finset.sum_congr rfl fun b _ => by ring

/-- **`ST0(a)`, the channel.** The uniform-prior family is the pure-reference family of the purified
isometry: `Φ_t = stinespringChannel V_t` in the merged module's sense, for every `t`. -/
theorem familyAt_eq_stinespringChannel (U : Matrix (V × H) (V × H) ℂ) (t : ℕ) :
    familyAt U t = stinespringChannel (Matrix.toEuclideanLin
      (Matrix.of fun (p : V × (H × H)) (b : V) =>
        (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) * (U ^ t) (p.1, p.2.1) (b, p.2.2))) := by
  rw [channel_eq_krausMap]
  funext ρ
  have hk : krausOf (Matrix.toEuclideanLin (Matrix.of fun (p : V × (H × H)) (b : V) =>
        (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) * (U ^ t) (p.1, p.2.1) (b, p.2.2)))
      = fun i : H × H => (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) •
          (Matrix.of fun a b => (U ^ t) (a, i.1) (b, i.2)) := by
    funext i
    ext a b
    simp [krausOf_toEuclideanLin]
  rw [hk, krausMap_smul, sqrt_scalar_sq, familyAt]

/-! ### Section D — `ST1` (Reading A, per time) and `ST1′` (the soundness control) -/

/-- **`ST1` — Reading A from the merged inputs, per time.** If the families agree at every `t`,
then **for each `t` separately** there is a unitary `W_t` on the purified environment `ℂ^{H × H}`
with `X'_t = X_t W_t`, `X_t` the amplitude matrix `m^{-1/2} (U^t)(a, h)(b, h')` of the Kraus family
of `Φ_t`. The existential is inside the `∀ t`: nothing here makes `W_t` constant in `t` or of the
product form `W ⊗ W̄`, and `ST3` below exhibits a pair on which no single hidden `W` exists. -/
theorem readingA_perTime [Nonempty H] (U U' : Matrix (V × H) (V × H) ℂ)
    (hfam : ∀ t, familyAt U t = familyAt U' t) (t : ℕ) :
    ∃ W : Matrix (H × H) (H × H) ℂ, Wᴴ * W = 1 ∧
      (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) •
          (Matrix.of fun (q : V × V) (p : H × H) => (U' ^ t) (q.1, p.1) (q.2, p.2))
        = ((((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) •
            (Matrix.of fun (q : V × V) (p : H × H) => (U ^ t) (q.1, p.1) (q.2, p.2))) * W := by
  apply rightUnitary_of_gram
  rw [conjTranspose_smul, conjTranspose_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
    Matrix.mul_smul]
  refine congrArg (_ • ·) (congrArg (_ • ·) ?_)
  ext ⟨a, b⟩ ⟨c, d⟩
  rw [amplitude_gram_entry, amplitude_gram_entry]
  have hm : (Fintype.card H : ℂ)⁻¹ ≠ 0 := by
    exact inv_ne_zero (Nat.cast_ne_zero.2 Fintype.card_ne_zero)
  have h := congrFun (congrFun (congrFun (hfam t) (Matrix.single b d 1)) a) c
  rw [familyAt_single, familyAt_single] at h
  exact mul_left_cancel₀ hm h

/-- Conjugation by `G` with `Gᴴ G = 1` passes through powers. -/
theorem conj_pow {n : Type} [Fintype n] [DecidableEq n] (G U : Matrix n n ℂ) (hG : Gᴴ * G = 1)
    (t : ℕ) : (G * U * Gᴴ) ^ t = G * U ^ t * Gᴴ := by
  induction t with
  | zero =>
    rw [pow_zero, pow_zero, mul_one]
    exact (mul_eq_one_comm.1 hG).symm
  | succ t ih =>
    rw [pow_succ, ih, pow_succ]
    calc G * U ^ t * Gᴴ * (G * U * Gᴴ) = G * U ^ t * (Gᴴ * G) * (U * Gᴴ) := by
          simp only [Matrix.mul_assoc]
      _ = G * (U ^ t * U) * Gᴴ := by rw [hG, Matrix.mul_one]; simp only [Matrix.mul_assoc]

/-- The hidden Kronecker factor of a unitary is unitary. -/
theorem hiddenKron_unitary (W : Matrix H H ℂ) (hW : Wᴴ * W = 1) :
    ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ * ((1 : Matrix V V ℂ) ⊗ₖ W) = 1 := by
  rw [conjTranspose_kronecker, ← mul_kronecker_mul, conjTranspose_one, Matrix.one_mul, hW,
    one_kronecker_one]

/-- **Kraus mixing by a unitary leaves the map unchanged.** -/
theorem krausMap_mix {I : Type} [Fintype I] [DecidableEq I] (M : Matrix I I ℂ) (hM : Mᴴ * M = 1)
    (A : I → Matrix V V ℂ) (ρ : Matrix V V ℂ) :
    krausMap (fun p => ∑ q, M p q • A q) ρ = krausMap A ρ := by
  have key : ∀ q q' : I, ∑ p, star (M p q') * M p q = if q' = q then (1 : ℂ) else 0 := by
    intro q q'
    have := congrFun (congrFun hM q') q
    simpa only [mul_apply, conjTranspose_apply, one_apply] using this
  have expand : ∀ p, (∑ q, M p q • A q) * ρ * (∑ q', M p q' • A q')ᴴ
      = ∑ q', ∑ q, (star (M p q') * M p q) • (A q * ρ * (A q')ᴴ) := by
    intro p
    simp only [conjTranspose_sum, conjTranspose_smul, Finset.sum_mul, Finset.mul_sum,
      smul_mul_assoc, mul_smul_comm, Finset.smul_sum, smul_smul]
  unfold krausMap
  simp_rw [expand]
  calc ∑ p, ∑ q', ∑ q, (star (M p q') * M p q) • (A q * ρ * (A q')ᴴ)
      = ∑ q', ∑ q, (∑ p, star (M p q') * M p q) • (A q * ρ * (A q')ᴴ) := by
        rw [Finset.sum_comm]
        refine Finset.sum_congr rfl fun q' _ => ?_
        rw [Finset.sum_comm]
        refine Finset.sum_congr rfl fun q _ => ?_
        rw [Finset.sum_smul]
    _ = ∑ q, A q * ρ * (A q)ᴴ := by
        simp only [key, ite_smul, one_smul, zero_smul, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- The product mixing matrix `W ⊗ W̄` on `H × H` is unitary when `W` is. -/
theorem mixing_unitary (W : Matrix H H ℂ) (hW : Wᴴ * W = 1) :
    (Matrix.of fun p q : H × H => W p.1 q.1 * star (W p.2 q.2))ᴴ *
      (Matrix.of fun p q : H × H => W p.1 q.1 * star (W p.2 q.2)) = 1 := by
  have key : ∀ i j, ∑ p, star (W p i) * W p j = if i = j then (1 : ℂ) else 0 := fun i j => by
    have := congrFun (congrFun hW i) j
    simpa [mul_apply, conjTranspose_apply, one_apply] using this
  ext ⟨i, i'⟩ ⟨j, j'⟩
  simp only [mul_apply, conjTranspose_apply, of_apply, Fintype.sum_prod_type, one_apply,
    Prod.mk.injEq]
  calc ∑ p, ∑ p', star (W p i * star (W p' i')) * (W p j * star (W p' j'))
      = ∑ p, ∑ p', (star (W p i) * W p j) * (W p' i' * star (W p' j')) := by
        refine Finset.sum_congr rfl fun p _ => Finset.sum_congr rfl fun p' _ => ?_
        simp only [star_mul, star_star]; ring
    _ = (∑ p, star (W p i) * W p j) * (∑ p', W p' i' * star (W p' j')) := by
        rw [Finset.sum_mul_sum]
    _ = (∑ p, star (W p i) * W p j) * star (∑ p', star (W p' i') * W p' j') := by
        congr 1
        rw [star_sum]
        refine Finset.sum_congr rfl fun p' _ => ?_
        rw [star_mul, star_star, mul_comm]
    _ = (if i = j ∧ i' = j' then 1 else 0) := by
        rw [key, key]
        by_cases h1 : i = j <;> by_cases h2 : i' = j' <;> simp [h1, h2]

/-- Left multiplication by `𝟙 ⊗ W`, entrywise. -/
theorem hiddenKron_mul_apply (W : Matrix H H ℂ) (U : Matrix (V × H) (V × H) ℂ) (a : V) (h : H)
    (s : V × H) : (((1 : Matrix V V ℂ) ⊗ₖ W) * U) (a, h) s = ∑ k, W h k * U (a, k) s := by
  simp only [mul_apply, kronecker_apply, one_apply, Fintype.sum_prod_type_right, ite_mul, one_mul,
    zero_mul, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- Right multiplication by `(𝟙 ⊗ W)ᴴ`, entrywise. -/
theorem mul_hiddenKron_conjTranspose_apply (W : Matrix H H ℂ) (M : Matrix (V × H) (V × H) ℂ)
    (r : V × H) (b : V) (h : H) :
    (M * ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ) r (b, h) = ∑ k, M r (b, k) * star (W h k) := by
  rw [conjTranspose_kronecker, conjTranspose_one]
  simp only [mul_apply, kronecker_apply, one_apply, conjTranspose_apply,
    Fintype.sum_prod_type_right, ite_mul, mul_ite, one_mul, zero_mul, mul_zero, Finset.sum_ite_eq',
    Finset.mem_univ, if_true]

/-- The visible-block Kraus family of a hidden conjugate is the `W ⊗ W̄` mixing of the original. -/
theorem kraus_hiddenConjugate (U : Matrix (V × H) (V × H) ℂ) (W : Matrix H H ℂ) (p : H × H) :
    (Matrix.of fun a b => (((1 : Matrix V V ℂ) ⊗ₖ W) * U * ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ)
        (a, p.1) (b, p.2))
      = ∑ q : H × H, (W p.1 q.1 * star (W p.2 q.2)) •
          (Matrix.of fun a b => U (a, q.1) (b, q.2)) := by
  ext a b
  simp only [of_apply, Matrix.sum_apply, Matrix.smul_apply, smul_eq_mul,
    mul_hiddenKron_conjTranspose_apply, hiddenKron_mul_apply, Fintype.sum_prod_type,
    Finset.sum_mul]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun h _ => Finset.sum_congr rfl fun h' _ => by ring

/-- **`ST1′` — the soundness control.** Hidden conjugation preserves the family at every `t`. -/
theorem familyAt_hiddenConjugate (U : Matrix (V × H) (V × H) ℂ) (W : Matrix H H ℂ)
    (hW : Wᴴ * W = 1) (t : ℕ) :
    familyAt (((1 : Matrix V V ℂ) ⊗ₖ W) * U * ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ) t = familyAt U t := by
  funext ρ
  unfold familyAt
  rw [conj_pow _ _ (hiddenKron_unitary W hW)]
  congr 1
  have := krausMap_mix (V := V) (Matrix.of fun p q : H × H => W p.1 q.1 * star (W p.2 q.2))
    (mixing_unitary W hW) (fun q : H × H => Matrix.of fun a b => (U ^ t) (a, q.1) (b, q.2)) ρ
  simp only [of_apply] at this
  rw [← this]
  congr 1
  funext p
  exact kraus_hiddenConjugate (U ^ t) W p

theorem hiddenConjugate_family {U U' : Matrix (V × H) (V × H) ℂ} (h : HiddenConjugate U U') :
    ∀ t, familyAt U' t = familyAt U t := by
  obtain ⟨W, hW, rfl⟩ := h
  exact familyAt_hiddenConjugate U W hW

/-! ### Section E — words under relabelling, hidden conjugation and decoupled enlargement

The general lemmas behind `ST4` and `ST5`: a word's value transforms by a sandwich under
`P_σ ⊗ W`, so its trace is invariant under hidden conjugation and relabels under `σ`; and under
decoupled enlargement a balanced word's trace scales by `|D|`. -/

/-- Act 7's entry formula for a permutation matrix, re-proved locally: `P_σ p q = [q = σ p]`. -/
theorem permMatrix_entry {n : Type} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n) (p q : n) :
    σ.permMatrix ℂ p q = if q = σ p then 1 else 0 := by
  simp only [Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, Option.mem_def,
    Option.some.injEq]
  exact if_congr eq_comm rfl rfl

/-- The visible block of `(P_σ ⊗ W) U (P_σ ⊗ W)ᴴ` is `W U_{σv, σw} Wᴴ`. -/
theorem visibleBlock_conj (σ : Equiv.Perm V) (W : Matrix H H ℂ) (U : Matrix (V × H) (V × H) ℂ)
    (v w : V) :
    visibleBlock ((σ.permMatrix ℂ ⊗ₖ W) * U * (σ.permMatrix ℂ ⊗ₖ W)ᴴ) v w
      = W * visibleBlock U (σ v) (σ w) * Wᴴ := by
  ext h k
  rw [conjTranspose_kronecker, Matrix.conjTranspose_permMatrix]
  simp only [visibleBlock_apply, mul_apply, kronecker_apply, conjTranspose_apply, permMatrix_entry,
    Equiv.Perm.inv_def, Equiv.eq_symm_apply, Fintype.sum_prod_type_right, ite_mul, mul_ite,
    one_mul, zero_mul, mul_zero, Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq,
    Finset.sum_ite_eq', Finset.mem_univ, if_true, Finset.sum_mul]

/-- The sandwich is multiplicative when `Wᴴ W = 1`. -/
theorem sandwich_mul (W : Matrix H H ℂ) (hW : Wᴴ * W = 1) (A B : Matrix H H ℂ) :
    (W * A * Wᴴ) * (W * B * Wᴴ) = W * (A * B) * Wᴴ := by
  calc (W * A * Wᴴ) * (W * B * Wᴴ) = W * A * (Wᴴ * W) * (B * Wᴴ) := by
        simp only [Matrix.mul_assoc]
    _ = W * (A * B) * Wᴴ := by rw [hW, Matrix.mul_one]; simp only [Matrix.mul_assoc]

/-- **Words transform by a sandwich and a relabelling.** -/
theorem wordEval_conj (σ : Equiv.Perm V) (W : Matrix H H ℂ) (hW : Wᴴ * W = 1)
    (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool)) :
    wordEval ((σ.permMatrix ℂ ⊗ₖ W) * U * (σ.permMatrix ℂ ⊗ₖ W)ᴴ) w
      = W * wordEval U (w.map fun l => (σ l.1, σ l.2.1, l.2.2)) * Wᴴ := by
  induction w with
  | nil =>
    simp only [wordEval, List.map_nil, List.prod_nil, Matrix.mul_one]
    exact (mul_eq_one_comm.1 hW).symm
  | cons l w ih =>
    simp only [wordEval, List.map_cons, List.prod_cons] at ih ⊢
    rw [ih, visibleBlock_conj]
    by_cases hl : l.2.2
    · simp only [hl, ↓reduceIte, sandwich_mul W hW]
    · have e : (W * visibleBlock U (σ l.1) (σ l.2.1) * Wᴴ)ᴴ
          = W * (visibleBlock U (σ l.1) (σ l.2.1))ᴴ * Wᴴ := by
        rw [conjTranspose_mul, conjTranspose_mul, conjTranspose_conjTranspose, Matrix.mul_assoc]
      simp only [hl, Bool.false_eq_true, ↓reduceIte, e, sandwich_mul W hW]

/-- **Word traces are invariant under hidden conjugation and relabel under `σ`.** -/
theorem trace_wordEval_conj (σ : Equiv.Perm V) (W : Matrix H H ℂ) (hW : Wᴴ * W = 1)
    (U : Matrix (V × H) (V × H) ℂ) (w : List (V × V × Bool)) :
    trace (wordEval ((σ.permMatrix ℂ ⊗ₖ W) * U * (σ.permMatrix ℂ ⊗ₖ W)ᴴ) w)
      = trace (wordEval U (w.map fun l => (σ l.1, σ l.2.1, l.2.2))) := by
  rw [wordEval_conj σ W hW, trace_mul_cycle, hW, Matrix.one_mul]

/-- The word value of a decoupled enlargement is the word value tensored with the `δ`-word. -/
theorem wordEval_enlarge {D : Type} [Fintype D] [DecidableEq D] (U : Matrix (V × H) (V × H) ℂ)
    (δ : Matrix D D ℂ) (w : List (V × V × Bool)) :
    wordEval (enlarge U δ) w = wordEval U w ⊗ₖ (w.map fun l => if l.2.2 then δ else δᴴ).prod := by
  induction w with
  | nil => simp only [wordEval, List.map_nil, List.prod_nil, one_kronecker_one]
  | cons l w ih =>
    simp only [wordEval, List.map_cons, List.prod_cons] at ih ⊢
    rw [ih, visibleBlock_enlarge]
    by_cases hl : l.2.2
    · simp only [hl, ↓reduceIte, mul_kronecker_mul]
    · simp only [hl, Bool.false_eq_true, ↓reduceIte, conjTranspose_kronecker, mul_kronecker_mul]

/-- **A balanced `δ`-word is `1` for unitary `δ`**: equal numbers of `δ` and `δᴴ` cancel in any
order, because the product is `δ^{net}` in the unit group and the net power is `0`. -/
theorem deltaWord_balanced {D : Type} [Fintype D] [DecidableEq D] (δ : Matrix D D ℂ)
    (hδ : δᴴ * δ = 1) (w : List (V × V × Bool))
    (hw : (w.map fun l => if l.2.2 then (1 : ℤ) else -1).sum = 0) :
    (w.map fun l => if l.2.2 then δ else δᴴ).prod = 1 := by
  have hδ' : δ * δᴴ = 1 := mul_eq_one_comm.1 hδ
  let u : (Matrix D D ℂ)ˣ := ⟨δ, δᴴ, hδ', hδ⟩
  have hl : ∀ l : V × V × Bool, (if l.2.2 then δ else δᴴ)
      = ((u ^ (if l.2.2 then (1 : ℤ) else -1) : (Matrix D D ℂ)ˣ) : Matrix D D ℂ) := by
    intro l
    by_cases h : l.2.2
    · simp only [h, ↓reduceIte, zpow_one]; rfl
    · simp only [h, Bool.false_eq_true, ↓reduceIte, _root_.zpow_neg, zpow_one]; rfl
  have hprod : ∀ (w : List (V × V × Bool)),
      (w.map fun l => u ^ (if l.2.2 then (1 : ℤ) else -1)).prod
        = u ^ (w.map fun l => if l.2.2 then (1 : ℤ) else -1).sum := by
    intro w
    induction w with
    | nil => simp
    | cons a w ih => rw [List.map_cons, List.prod_cons, List.map_cons, List.sum_cons, ih, _root_.zpow_add]
  have key := List.prod_hom (w.map fun l => u ^ (if l.2.2 then (1 : ℤ) else -1))
    (Units.coeHom (Matrix D D ℂ))
  rw [List.map_map, hprod, hw, zpow_zero] at key
  simp only [Function.comp_def, Units.coeHom_apply, Units.val_one] at key
  rw [← key]
  congr 1
  exact List.map_congr_left fun l _ => hl l

/-- **The enlargement lemma.** For a balanced word and unitary `δ`,
`Tr[w(U ⊗ δ)] = |D| · Tr[w(U)]`. -/
theorem trace_wordEval_enlarge {D : Type} [Fintype D] [DecidableEq D]
    (U : Matrix (V × H) (V × H) ℂ) (δ : Matrix D D ℂ) (hδ : δᴴ * δ = 1)
    (w : List (V × V × Bool)) (hw : (w.map fun l => if l.2.2 then (1 : ℤ) else -1).sum = 0) :
    trace (wordEval (enlarge U δ) w) = (Fintype.card D : ℂ) * trace (wordEval U w) := by
  rw [wordEval_enlarge, trace_kronecker, deltaWord_balanced δ hδ w hw, trace_one, mul_comm]

/-! ### Section F — `ST5`, the necessity direction: hidden conjugation preserves every word trace -/

/-- **`ST5`, necessity.** Hidden conjugation preserves every block-word trace — balanced or not. -/
theorem trace_wordEval_hiddenConjugate {U U' : Matrix (V × H) (V × H) ℂ}
    (h : HiddenConjugate U U') (w : List (V × V × Bool)) :
    trace (wordEval U' w) = trace (wordEval U w) := by
  obtain ⟨W, hW, rfl⟩ := h
  have := trace_wordEval_conj (1 : Equiv.Perm V) W hW U w
  simpa [Matrix.permMatrix_one] using this

/-! ### Section G — involutions and the family of a permutation dilation -/

theorem pow_involution {n : Type} [Fintype n] [DecidableEq n] (U : Matrix n n ℂ) (hU : U * U = 1)
    (t : ℕ) : U ^ t = if Even t then 1 else U := by
  induction t with
  | zero => simp
  | succ t ih =>
    rw [pow_succ, ih]
    by_cases ht : Even t
    · simp [ht, Nat.even_add_one]
    · simp [ht, Nat.even_add_one, hU]

/-- Two involutive dilations with the same time-one map have the same family. -/
theorem familyAt_involution_eq {U U' : Matrix (V × H) (V × H) ℂ} (hU : U * U = 1)
    (hU' : U' * U' = 1) (h1 : familyAt U 1 = familyAt U' 1) (t : ℕ) :
    familyAt U t = familyAt U' t := by
  by_cases ht : Even t
  · unfold familyAt
    rw [pow_involution U hU, pow_involution U' hU', if_pos ht, if_pos ht]
  · have e : ∀ X : Matrix (V × H) (V × H) ℂ, X * X = 1 → familyAt X t = familyAt X 1 := by
      intro X hX
      unfold familyAt
      rw [pow_involution X hX, if_neg ht, pow_one]
    rw [e U hU, e U' hU', h1]

theorem permMatrix_mul_self {n : Type} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n)
    (h : σ * σ = 1) : σ.permMatrix ℂ * σ.permMatrix ℂ = 1 := by
  rw [← Matrix.permMatrix_mul, h, Matrix.permMatrix_one]

theorem permMatrix_conjTranspose_self {n : Type} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n)
    (h : σ * σ = 1) : (σ.permMatrix ℂ)ᴴ = σ.permMatrix ℂ := by
  rw [Matrix.conjTranspose_permMatrix, inv_eq_of_mul_eq_one_right h]

/-- The Kraus map is linear in `ρ`: its value is determined by the matrix units. -/
theorem krausMap_expand {I : Type} [Fintype I] (A : I → Matrix V V ℂ) (ρ : Matrix V V ℂ) :
    krausMap A ρ = ∑ a, ∑ b, ρ a b • krausMap A (Matrix.single a b 1) := by
  conv_lhs => rw [Matrix.matrix_eq_sum_single ρ]
  simp only [krausMap, Finset.mul_sum, Finset.sum_mul, Finset.smul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun i _ => ?_
  have hs : Matrix.single a b (ρ a b) = ρ a b • Matrix.single a b 1 := by
    rw [Matrix.smul_single, smul_eq_mul, mul_one]
  rw [hs, Matrix.mul_smul, Matrix.smul_mul]

theorem familyAt_expand (U : Matrix (V × H) (V × H) ℂ) (t : ℕ) (ρ : Matrix V V ℂ) :
    familyAt U t ρ = ∑ a, ∑ b, ρ a b • familyAt U t (Matrix.single a b 1) := by
  unfold familyAt
  rw [krausMap_expand, Finset.smul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [smul_comm]

/-- **Family equality is equality of the sorted balanced word traces**: two dilations have the same
family at `t` as soon as the block traces `Tr[(U^t)_{ca}((U^t)_{db})ᴴ]` agree. -/
theorem familyAt_eq_of_blockTraces {U U' : Matrix (V × H) (V × H) ℂ} (t : ℕ)
    (h : ∀ a b c d, trace (visibleBlock (U ^ t) c a * (visibleBlock (U ^ t) d b)ᴴ)
      = trace (visibleBlock (U' ^ t) c a * (visibleBlock (U' ^ t) d b)ᴴ)) :
    familyAt U t = familyAt U' t := by
  funext ρ
  rw [familyAt_expand, familyAt_expand]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  congr 1
  ext c d
  rw [familyAt_single, familyAt_single, h]

/-! ### Section H — the hidden commutant of a permutation dilation, entrywise -/

theorem hiddenKron_mul_permMatrix (φ : Equiv.Perm (V × H)) (Y : Matrix H H ℂ) (v : V) (h : H)
    (q : V × H) :
    (((1 : Matrix V V ℂ) ⊗ₖ Y) * φ.permMatrix ℂ) (v, h) q
      = if (φ.symm q).1 = v then Y h (φ.symm q).2 else 0 := by
  rw [hiddenKron_mul_apply]
  simp only [permMatrix_entry, ← Equiv.symm_apply_eq, Prod.ext_iff, ite_and, mul_ite, mul_one,
    mul_zero, Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true]

theorem permMatrix_mul_hiddenKron (φ : Equiv.Perm (V × H)) (Y : Matrix H H ℂ) (p : V × H) (w : V)
    (k : H) :
    (φ.permMatrix ℂ * ((1 : Matrix V V ℂ) ⊗ₖ Y)) p (w, k)
      = if (φ p).1 = w then Y (φ p).2 k else 0 := by
  simp only [mul_apply, permMatrix_entry, kroneckerMap_apply, one_apply, ite_mul, one_mul,
    zero_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]

/-- Trace of a visible block is invariant under hidden conjugation (the `ST2` certificate). -/
theorem trace_visibleBlock_hiddenConjugate (U : Matrix (V × H) (V × H) ℂ) (W : Matrix H H ℂ)
    (hW : Wᴴ * W = 1) (v w : V) :
    trace (visibleBlock (((1 : Matrix V V ℂ) ⊗ₖ W) * U * ((1 : Matrix V V ℂ) ⊗ₖ W)ᴴ) v w)
      = trace (visibleBlock U v w) := by
  have := visibleBlock_conj (1 : Equiv.Perm V) W U v w
  rw [Matrix.permMatrix_one] at this
  rw [this, trace_mul_cycle, hW, Matrix.one_mul]
  rfl

/-! ### Section I — the witness pairs

The witnesses are **not** top-level definitions: each permutation is a local notation for an
explicit product of transpositions, pinned by an equation `U = φ.permMatrix ℂ` inside the statement
that needs it. -/

/-- Pair A, `φ(v, h) = (v, h ⊕ v)` on `ℤ₂ × ℤ₂`: the transposition `(1,0) ↔ (1,1)`. -/
local notation "φA" => (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))
/-- Pair A, `φ'(v, h) = (v, h ⊕ v ⊕ 1)`: the transposition `(0,0) ↔ (0,1)`. -/
local notation "φA'" => (Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)))
/-- Pair C, `φ`: `(0,2) ↔ (1,0)` and `(1,1) ↔ (1,2)`, fixing `(0,0)` and `(0,1)`. -/
local notation "φC" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) *
  Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)))
/-- Pair C, `φ'`: `φ` composed with the additional transposition `(0,0) ↔ (0,1)`. -/
local notation "φC'" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) *
  Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)) *
  Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)))

/-- The visible blocks of Pair A. -/
theorem pairA_blocks :
    visibleBlock (Equiv.Perm.permMatrix ℂ φA) 0 0 = !![1, 0; 0, 1] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA) 0 1 = !![0, 0; 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA) 1 0 = !![0, 0; 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA) 1 1 = !![0, 1; 1, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA') 0 0 = !![0, 1; 1, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA') 0 1 = !![0, 0; 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA') 1 0 = !![0, 0; 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φA') 1 1 = !![1, 0; 0, 1] := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (ext i j; fin_cases i <;> fin_cases j <;> simp [Equiv.swap_apply_def])

/-- The visible blocks of Pair C. -/
theorem pairC_blocks :
    visibleBlock (Equiv.Perm.permMatrix ℂ φC) 0 0 = !![1, 0, 0; 0, 1, 0; 0, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC) 0 1 = !![0, 0, 0; 0, 0, 0; 1, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC) 1 0 = !![0, 0, 1; 0, 0, 0; 0, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC) 1 1 = !![0, 0, 0; 0, 0, 1; 0, 1, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC') 0 0 = !![0, 1, 0; 1, 0, 0; 0, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC') 0 1 = !![0, 0, 0; 0, 0, 0; 1, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC') 1 0 = !![0, 0, 1; 0, 0, 0; 0, 0, 0] ∧
    visibleBlock (Equiv.Perm.permMatrix ℂ φC') 1 1 = !![0, 0, 0; 0, 0, 1; 0, 1, 0] := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (ext i j; fin_cases i <;> fin_cases j <;> simp only [visibleBlock_apply, permMatrix_entry] <;>
      simp [Equiv.swap_apply_def])

/-- Adjoints of the `0/1` block literals that occur. -/
theorem adj_literals :
    (!![1, 0; 0, 1] : Matrix (Fin 2) (Fin 2) ℂ)ᴴ = !![1, 0; 0, 1] ∧
    (!![0, 0; 0, 0] : Matrix (Fin 2) (Fin 2) ℂ)ᴴ = !![0, 0; 0, 0] ∧
    (!![0, 1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ)ᴴ = !![0, 1; 1, 0] ∧
    (!![1, 0, 0; 0, 1, 0; 0, 0, 0] : Matrix (Fin 3) (Fin 3) ℂ)ᴴ = !![1, 0, 0; 0, 1, 0; 0, 0, 0] ∧
    (!![0, 0, 0; 0, 0, 0; 1, 0, 0] : Matrix (Fin 3) (Fin 3) ℂ)ᴴ = !![0, 0, 1; 0, 0, 0; 0, 0, 0] ∧
    (!![0, 0, 1; 0, 0, 0; 0, 0, 0] : Matrix (Fin 3) (Fin 3) ℂ)ᴴ = !![0, 0, 0; 0, 0, 0; 1, 0, 0] ∧
    (!![0, 0, 0; 0, 0, 1; 0, 1, 0] : Matrix (Fin 3) (Fin 3) ℂ)ᴴ = !![0, 0, 0; 0, 0, 1; 0, 1, 0] ∧
    (!![0, 1, 0; 1, 0, 0; 0, 0, 0] : Matrix (Fin 3) (Fin 3) ℂ)ᴴ = !![0, 1, 0; 1, 0, 0; 0, 0, 0] := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (ext i j; fin_cases i <;> fin_cases j <;> simp [conjTranspose_apply])

/-! ### Section J — `ST2`: Reading B as literally stated, refuted on Pair A -/

/-- **`ST2` — NEGATIVE.** Pair A: equal families at every `t` (both are involutions with the same
dephasing time-one map), yet **no hidden unitary** conjugates one to the other — the `(0,0)` block
of `φ̂` is `𝟙` and that of `φ̂'` is `X`, and hidden conjugation preserves each block's trace
(`2 ≠ 0`). The pair **is** absorbed by generator (i)'s visible part: `φ̂' = (X ⊗ 𝟙) φ̂ (X ⊗ 𝟙)`, the
last conjunct. Reachable cyclicity `𝒞_B = 𝒞_H` holds on every permutation instance by definition
(the uniform prior has full support), so this is step (2)'s literal conclusion failing on a
two-qubit substratum pair; exhaustiveness is untouched by this pair. -/
theorem ST2_pairA :
    ∃ U U' : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ,
      U = Equiv.Perm.permMatrix ℂ φA ∧ U' = Equiv.Perm.permMatrix ℂ φA' ∧ Uᴴ * U = 1 ∧ U'ᴴ * U' = 1 ∧
      (∀ t, familyAt U t = familyAt U' t) ∧
      ¬ HiddenConjugate U U' ∧
      U' = ((Equiv.swap (0 : Fin 2) 1).permMatrix ℂ ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) ℂ)) * U *
        ((Equiv.swap (0 : Fin 2) 1).permMatrix ℂ ⊗ₖ (1 : Matrix (Fin 2) (Fin 2) ℂ))ᴴ := by
  obtain ⟨b00, b01, b10, b11, c00, c01, c10, c11⟩ := pairA_blocks
  obtain ⟨a1, a0, aX, -, -, -, -, -⟩ := adj_literals
  have hA : φA * φA = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have hA' : φA' * φA' = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have hU : (Equiv.Perm.permMatrix ℂ φA) * (Equiv.Perm.permMatrix ℂ φA) = 1 := permMatrix_mul_self _ hA
  have hU' : (Equiv.Perm.permMatrix ℂ φA') * (Equiv.Perm.permMatrix ℂ φA') = 1 := permMatrix_mul_self _ hA'
  refine ⟨Equiv.Perm.permMatrix ℂ φA, Equiv.Perm.permMatrix ℂ φA', rfl, rfl, ?_, ?_, ?_, ?_, ?_⟩
  · rw [permMatrix_conjTranspose_self _ hA]; exact hU
  · rw [permMatrix_conjTranspose_self _ hA']; exact hU'
  · refine familyAt_involution_eq hU hU' ?_
    refine familyAt_eq_of_blockTraces 1 ?_
    simp only [pow_one, Fin.forall_fin_two, b00, b01, b10, b11, c00, c01, c10, c11, a1, a0, aX]
    simp only [Matrix.mul_fin_two, Matrix.trace_fin_two_of]
    norm_num
  · rintro ⟨W, hW, hU'⟩
    have h := trace_visibleBlock_hiddenConjugate (Equiv.Perm.permMatrix ℂ φA) W hW 0 0
    rw [← hU', c00, b00, Matrix.trace_fin_two_of, Matrix.trace_fin_two_of] at h
    norm_num at h
  · ext ⟨v, h⟩ ⟨w, k⟩
    have e := congrFun (congrFun (visibleBlock_conj (Equiv.swap (0 : Fin 2) 1)
      (1 : Matrix (Fin 2) (Fin 2) ℂ) (Equiv.Perm.permMatrix ℂ φA) v w) h) k
    rw [Matrix.one_mul, conjTranspose_one, Matrix.mul_one] at e
    simp only [visibleBlock_apply] at e
    rw [e]
    fin_cases v <;> fin_cases h <;> fin_cases w <;> fin_cases k <;>
      simp [Equiv.swap_apply_def]

/-! ### Section K — `ST3`: Reading B under GNS cyclicity, refuted on Pair C -/

/-- The hidden commutant of Pair C's `φ̂` is trivial: explicit elimination on the `3 × 3` unknown. -/
theorem pairC_hct : HiddenCommutantTrivial (Equiv.Perm.permMatrix ℂ φC) := by
  intro Y hY
  have h := fun (v : Fin 2) (h : Fin 3) (w : Fin 2) (k : Fin 3) =>
    congrFun (congrFun hY (v, h)) (w, k)
  simp only [hiddenKron_mul_permMatrix, permMatrix_mul_hiddenKron] at h
  have hs : Equiv.symm φC = φC := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have v00 : φC ((0 : Fin 2), (0 : Fin 3)) = (0, 0) := by decide
  have v01 : φC ((0 : Fin 2), (1 : Fin 3)) = (0, 1) := by decide
  have v02 : φC ((0 : Fin 2), (2 : Fin 3)) = (1, 0) := by decide
  have v10 : φC ((1 : Fin 2), (0 : Fin 3)) = (0, 2) := by decide
  have v11 : φC ((1 : Fin 2), (1 : Fin 3)) = (1, 2) := by decide
  have v12 : φC ((1 : Fin 2), (2 : Fin 3)) = (1, 1) := by decide
  have e1 := h 0 0 1 0
  have e2 := h 0 1 1 0
  have e3 := h 0 2 0 0
  have e4 := h 0 2 0 1
  have e5 := h 1 0 1 2
  have e6 := h 1 1 0 2
  have e7 := h 0 2 1 0
  have e8 := h 1 1 1 2
  simp +decide only [hs, v00, v01, v02, v10, v11, v12, ↓reduceIte] at e1 e2 e3 e4 e5 e6 e7 e8
  refine ⟨Y 0 0, ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [e1, e2, e3, e4, e5, e6, e7, e8]

/-- The hidden commutant of Pair C's `φ̂'` is trivial. -/
theorem pairC'_hct : HiddenCommutantTrivial (Equiv.Perm.permMatrix ℂ φC') := by
  intro Y hY
  have h := fun (v : Fin 2) (h : Fin 3) (w : Fin 2) (k : Fin 3) =>
    congrFun (congrFun hY (v, h)) (w, k)
  simp only [hiddenKron_mul_permMatrix, permMatrix_mul_hiddenKron] at h
  have hs : Equiv.symm φC' = φC' := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have v00 : φC' ((0 : Fin 2), (0 : Fin 3)) = (0, 1) := by decide
  have v01 : φC' ((0 : Fin 2), (1 : Fin 3)) = (0, 0) := by decide
  have v02 : φC' ((0 : Fin 2), (2 : Fin 3)) = (1, 0) := by decide
  have v10 : φC' ((1 : Fin 2), (0 : Fin 3)) = (0, 2) := by decide
  have v11 : φC' ((1 : Fin 2), (1 : Fin 3)) = (1, 2) := by decide
  have v12 : φC' ((1 : Fin 2), (2 : Fin 3)) = (1, 1) := by decide
  have e1 := h 0 0 1 0
  have e2 := h 0 1 1 0
  have e3 := h 0 2 0 0
  have e4 := h 0 2 0 1
  have e5 := h 1 0 1 2
  have e6 := h 1 1 0 2
  have e7 := h 0 2 1 0
  have e8 := h 1 1 1 2
  simp +decide only [hs, v00, v01, v02, v10, v11, v12, ↓reduceIte] at e1 e2 e3 e4 e5 e6 e7 e8
  refine ⟨Y 0 0, ?_⟩
  ext i j
  fin_cases i <;> fin_cases j <;> simp [e1, e2, e3, e4, e5, e6, e7, e8]

/-- Pair C has the same family at every `t`. -/
theorem pairC_family (t : ℕ) : familyAt (Equiv.Perm.permMatrix ℂ φC) t = familyAt (Equiv.Perm.permMatrix ℂ φC') t := by
  obtain ⟨b00, b01, b10, b11, c00, c01, c10, c11⟩ := pairC_blocks
  obtain ⟨-, -, -, d1, d2, d3, d4, d5⟩ := adj_literals
  have hC : φC * φC = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have hC' : φC' * φC' = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  refine familyAt_involution_eq (permMatrix_mul_self _ hC) (permMatrix_mul_self _ hC') ?_ t
  refine familyAt_eq_of_blockTraces 1 ?_
  simp only [pow_one, Fin.forall_fin_two, b00, b01, b10, b11, c00, c01, c10, c11, d1, d2, d3, d4, d5]
  simp only [Matrix.mul_fin_three, Matrix.trace_fin_three_of]
  norm_num

/-- **`ST3` — NEGATIVE.** Pair C: both hidden commutants trivial (`pairC_hct`, `pairC'_hct`),
equal families at every `t` (`pairC_family`), non-trivial visible statistics (the time-one map
sends `E_{00}` to `diag(2/3, 1/3)`), and **no unitary whatsoever** — hidden, visible, or arbitrary
— conjugates one to the other, because `Tr φ̂ = 2 ≠ 0 = Tr φ̂'` and the trace is invariant under
every unitary conjugation. -/
theorem ST3_pairC :
    ∃ U U' : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ,
      U = Equiv.Perm.permMatrix ℂ φC ∧ U' = Equiv.Perm.permMatrix ℂ φC' ∧ Uᴴ * U = 1 ∧ U'ᴴ * U' = 1 ∧
      HiddenCommutantTrivial U ∧ HiddenCommutantTrivial U' ∧
      (∀ t, familyAt U t = familyAt U' t) ∧
      (∀ G : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ, Gᴴ * G = 1 → U' ≠ G * U * Gᴴ) ∧
      trace U = 2 ∧ trace U' = 0 ∧
      familyAt U 1 (Matrix.single 0 0 1) 0 0 = 2 / 3 ∧
      familyAt U 1 (Matrix.single 0 0 1) 1 1 = 1 / 3 := by
  obtain ⟨b00, b01, b10, b11, c00, c01, c10, c11⟩ := pairC_blocks
  obtain ⟨-, -, -, d1, d2, d3, d4, d5⟩ := adj_literals
  have hC : φC * φC = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have hC' : φC' * φC' = 1 := by
    refine Equiv.ext fun p => ?_; obtain ⟨v, h⟩ := p; fin_cases v <;> fin_cases h <;> decide
  have tU : trace (Equiv.Perm.permMatrix ℂ φC) = 2 := by
    simp only [Matrix.trace, Matrix.diag_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Fin.sum_univ_three, permMatrix_entry]
    simp [Equiv.swap_apply_def]
    norm_num
  have tU' : trace (Equiv.Perm.permMatrix ℂ φC') = 0 := by
    simp only [Matrix.trace, Matrix.diag_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Fin.sum_univ_three, permMatrix_entry]
    simp [Equiv.swap_apply_def]
  refine ⟨Equiv.Perm.permMatrix ℂ φC, Equiv.Perm.permMatrix ℂ φC', rfl, rfl, ?_, ?_, pairC_hct, pairC'_hct,
    pairC_family, ?_, tU, tU', ?_, ?_⟩
  · rw [permMatrix_conjTranspose_self _ hC]; exact permMatrix_mul_self _ hC
  · rw [permMatrix_conjTranspose_self _ hC']; exact permMatrix_mul_self _ hC'
  · intro G hG heq
    have h := congrArg trace heq
    rw [trace_mul_cycle, hG, Matrix.one_mul, tU, tU'] at h
    norm_num at h
  · rw [familyAt_single, pow_one, b00, d1]
    simp only [Matrix.mul_fin_three, Matrix.trace_fin_three_of, Fintype.card_fin]
    norm_num
  · rw [familyAt_single, pow_one, b10, d3]
    simp only [Matrix.mul_fin_three, Matrix.trace_fin_three_of, Fintype.card_fin]
    norm_num

/-! ### Section L — `ST4`: the (i)+(iii) orbit, refuted on Pair C by a balanced word -/

/-- The three word-trace values the `ST4` certificate uses. `w₀ = U₀₀ U₁₀ U₀₁ U₀₀ᴴ U₀₁ᴴ U₁₀ᴴ` and
`w₁` its relabelling under the visible swap. -/
theorem pairC_wordTraces :
    trace (wordEval (Equiv.Perm.permMatrix ℂ φC)
      [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
       (0, 0, false), (0, 1, false), (1, 0, false)]) = 1 ∧
    trace (wordEval (Equiv.Perm.permMatrix ℂ φC')
      [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
       (0, 0, false), (0, 1, false), (1, 0, false)]) = 0 ∧
    trace (wordEval (Equiv.Perm.permMatrix ℂ φC')
      [((1 : Fin 2), (1 : Fin 2), true), (0, 1, true), (1, 0, true),
       (1, 1, false), (1, 0, false), (0, 1, false)]) = 0 := by
  obtain ⟨b00, b01, b10, b11, c00, c01, c10, c11⟩ := pairC_blocks
  obtain ⟨-, -, -, d1, d2, d3, d4, d5⟩ := adj_literals
  refine ⟨?_, ?_, ?_⟩ <;>
    (simp only [wordEval, List.map_cons, List.map_nil, List.prod_cons, List.prod_nil, ↓reduceIte,
      Bool.false_eq_true, b00, b01, b10, c00, c01, c10, c11, d1, d2, d3, d4, d5, Matrix.mul_one]
     simp only [Matrix.mul_fin_three, Matrix.trace_fin_three_of]
     norm_num)

/-- **`ST4` — NEGATIVE.** Pair C is not related by `P_σ ⊗ W` for any visible permutation `σ`,
any hidden unitary `W` on `ℂ^{H × D}`, after any decoupled enlargement by unitaries `δ, δ'` on any
finite non-empty `D`: the balanced word `w₀` (or its swap-relabelling `w₁`) has trace `|D| · 1` on
one side and `|D| · 0` on the other, by the enlargement lemma `trace_wordEval_enlarge` and the
relabelling lemma `trace_wordEval_conj`. The deep-sector model is the frozen exact product
`U ⊗ δ` with a decoupled factor of equal total size on both sides. -/
theorem ST4_pairC :
    ∃ U U' : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ,
      U = Equiv.Perm.permMatrix ℂ φC ∧ U' = Equiv.Perm.permMatrix ℂ φC' ∧
      HiddenCommutantTrivial U ∧ HiddenCommutantTrivial U' ∧
      (∀ t, familyAt U t = familyAt U' t) ∧
      ∀ (D : Type) [Fintype D] [DecidableEq D] [Nonempty D] (δ δ' : Matrix D D ℂ)
        (σ : Equiv.Perm (Fin 2)) (W : Matrix (Fin 3 × D) (Fin 3 × D) ℂ),
        δᴴ * δ = 1 → δ'ᴴ * δ' = 1 → Wᴴ * W = 1 →
        enlarge U' δ' ≠ (σ.permMatrix ℂ ⊗ₖ W) * enlarge U δ * (σ.permMatrix ℂ ⊗ₖ W)ᴴ := by
  obtain ⟨t1, t2, t3⟩ := pairC_wordTraces
  refine ⟨Equiv.Perm.permMatrix ℂ φC, Equiv.Perm.permMatrix ℂ φC', rfl, rfl, pairC_hct, pairC'_hct, pairC_family, ?_⟩
  intro D _ _ _ δ δ' σ W hδ hδ' hW heq
  have hD : (Fintype.card D : ℂ) ≠ 0 := Nat.cast_ne_zero.2 Fintype.card_ne_zero
  have hσ : ∀ σ : Equiv.Perm (Fin 2), σ = 1 ∨ σ = Equiv.swap 0 1 := by decide
  rcases hσ σ with rfl | rfl
  · have h := congrArg (fun M => trace (wordEval M
      [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
       (0, 0, false), (0, 1, false), (1, 0, false)])) heq
    simp only at h
    rw [trace_wordEval_enlarge _ δ' hδ' _ (by decide), trace_wordEval_conj 1 W hW] at h
    have hmap : ([((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
        (0, 0, false), (0, 1, false), (1, 0, false)].map
          fun l : Fin 2 × Fin 2 × Bool => ((1 : Equiv.Perm (Fin 2)) l.1,
            (1 : Equiv.Perm (Fin 2)) l.2.1, l.2.2))
        = [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
           (0, 0, false), (0, 1, false), (1, 0, false)] := by decide
    rw [hmap, trace_wordEval_enlarge _ δ hδ _ (by decide), t1, t2, mul_zero, mul_one] at h
    exact hD h.symm
  · have h := congrArg (fun M => trace (wordEval M
      [((1 : Fin 2), (1 : Fin 2), true), (0, 1, true), (1, 0, true),
       (1, 1, false), (1, 0, false), (0, 1, false)])) heq
    simp only at h
    rw [trace_wordEval_enlarge _ δ' hδ' _ (by decide), trace_wordEval_conj _ W hW] at h
    have hmap : ([((1 : Fin 2), (1 : Fin 2), true), (0, 1, true), (1, 0, true),
        (1, 1, false), (1, 0, false), (0, 1, false)].map
          fun l : Fin 2 × Fin 2 × Bool => ((Equiv.swap (0 : Fin 2) 1) l.1,
            (Equiv.swap (0 : Fin 2) 1) l.2.1, l.2.2))
        = [((0 : Fin 2), (0 : Fin 2), true), (1, 0, true), (0, 1, true),
           (0, 0, false), (0, 1, false), (1, 0, false)] := by decide
    rw [hmap, trace_wordEval_enlarge _ δ hδ _ (by decide), t1, t3, mul_zero, mul_one] at h
    exact hD h.symm

/-! ### Section M — `ST0(c)`: GNS cyclicity is trivial hidden commutant

The purified carrier is `V × (H × H')` with `H' = H`; the dilation acts as `U ⊗ 𝟙_{H'}`
(`enlarge U 1`), the visible algebra as `X ⊗ 𝟙`, and the reference vectors are `ψ ⊗ Ω` with
`Ω = m^{-1/2} Σ_h |h⟩|h⟩`. Cyclicity is stated as: every subspace containing every `ψ ⊗ Ω` and
invariant under `X ⊗ 𝟙`, `U ⊗ 𝟙` and `(U ⊗ 𝟙)ᴴ` is everything. The proof runs through the
commutant of the generating set — the reference is cyclic for the generated `*`-algebra iff it is
separating for that commutant (`starProjection_comm` supplies the non-trivial half) — and computes
the commutant as `𝟙 ⊗ Z` with every primed slice of `Z` in the hidden commutant of `U`. -/

/-- The reference vector `ψ ⊗ Ω` on the carrier `V × (H × H')`. -/
local notation "refVec " ψ:arg => (fun q : V × (H × H) =>
  ψ (Prod.fst q) * ((((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) *
    (1 : Matrix H H ℂ) (Prod.fst (Prod.snd q)) (Prod.snd (Prod.snd q))))

theorem mul_hiddenKron_apply {E : Type} [Fintype E] [DecidableEq E] (Y : Matrix E E ℂ)
    (M : Matrix (V × E) (V × E) ℂ) (r : V × E) (b : V) (k : E) :
    (M * ((1 : Matrix V V ℂ) ⊗ₖ Y)) r (b, k) = ∑ l, M r (b, l) * Y l k := by
  simp only [mul_apply, kronecker_apply, one_apply, Fintype.sum_prod_type_right, ite_mul, mul_ite,
    one_mul, zero_mul, mul_zero, Finset.sum_ite_eq', Finset.mem_univ, if_true]

theorem mul_singleKron_apply {E : Type} [Fintype E] [DecidableEq E]
    (T : Matrix (V × E) (V × E) ℂ) (a b c d : V) (r s : E) :
    (T * (Matrix.single a b (1 : ℂ) ⊗ₖ (1 : Matrix E E ℂ))) (c, r) (d, s)
      = if b = d then T (c, r) (a, s) else 0 := by
  simp only [mul_apply, kronecker_apply, Matrix.single_apply, one_apply,
    Fintype.sum_prod_type_right, ite_and, mul_ite, mul_one, mul_zero, Finset.sum_ite_irrel,
    Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true]

theorem singleKron_mul_apply {E : Type} [Fintype E] [DecidableEq E]
    (T : Matrix (V × E) (V × E) ℂ) (a b c d : V) (r s : E) :
    ((Matrix.single a b (1 : ℂ) ⊗ₖ (1 : Matrix E E ℂ)) * T) (c, r) (d, s)
      = if a = c then T (b, r) (d, s) else 0 := by
  simp only [mul_apply, kronecker_apply, Matrix.single_apply, one_apply,
    Fintype.sum_prod_type_right, ite_and, ite_mul, one_mul, zero_mul, Finset.sum_ite_irrel,
    Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- **The commutant of `B(ℋ_V) ⊗ 𝟙` is `𝟙 ⊗ B`.** -/
theorem eq_oneKron_of_comm {E : Type} [Fintype E] [DecidableEq E] [Nonempty V]
    (T : Matrix (V × E) (V × E) ℂ)
    (hT : ∀ X : Matrix V V ℂ, T * (X ⊗ₖ (1 : Matrix E E ℂ)) = (X ⊗ₖ 1) * T) :
    T = (1 : Matrix V V ℂ) ⊗ₖ
      (Matrix.of fun r s => T (Classical.arbitrary V, r) (Classical.arbitrary V, s)) := by
  have key : ∀ a b c d r s, (if b = d then T (c, r) (a, s) else 0)
      = if a = c then T (b, r) (d, s) else 0 := fun a b c d r s => by
    have := congrFun (congrFun (hT (Matrix.single a b 1)) (c, r)) (d, s)
    rwa [mul_singleKron_apply, singleKron_mul_apply] at this
  ext ⟨c, r⟩ ⟨d, s⟩
  simp only [kronecker_apply, one_apply, of_apply]
  by_cases hcd : c = d
  · subst hcd
    have h := key c (Classical.arbitrary V) c (Classical.arbitrary V) r s
    simpa using h
  · have h := key c c c d r s
    simp only [hcd, if_false, if_true] at h ⊢
    rw [zero_mul]
    try exact h.symm

/-- A primed slice of a `𝟙 ⊗ Z` commuting with `U ⊗ 𝟙_{H'}` commutes with `U`. -/
theorem slice_comm (U : Matrix (V × H) (V × H) ℂ) (Z : Matrix (H × H) (H × H) ℂ)
    (hZ : ((1 : Matrix V V ℂ) ⊗ₖ Z) * enlarge U (1 : Matrix H H ℂ)
      = enlarge U 1 * ((1 : Matrix V V ℂ) ⊗ₖ Z)) (h' k' : H) :
    ((1 : Matrix V V ℂ) ⊗ₖ (Matrix.of fun h l => Z (h, h') (l, k'))) * U
      = U * ((1 : Matrix V V ℂ) ⊗ₖ (Matrix.of fun h l => Z (h, h') (l, k'))) := by
  ext ⟨a, h⟩ ⟨b, k⟩
  have e := congrFun (congrFun hZ (a, (h, h'))) (b, (k, k'))
  simp only [mul_apply, kronecker_apply, one_apply, enlarge_apply, Fintype.sum_prod_type,
    ite_mul, mul_ite, one_mul, zero_mul, mul_zero, mul_one, Finset.sum_ite_irrel,
    Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true] at e
  rw [hiddenKron_mul_apply, mul_hiddenKron_apply]
  simpa only [of_apply] using e

/-- `𝟙 ⊗ (Y ⊗ B)` commutes with `U ⊗ 𝟙_{H'}` whenever `𝟙 ⊗ Y` commutes with `U`. -/
theorem hiddenKron_comm_enlarge (U : Matrix (V × H) (V × H) ℂ) (Y B : Matrix H H ℂ)
    (hY : ((1 : Matrix V V ℂ) ⊗ₖ Y) * U = U * ((1 : Matrix V V ℂ) ⊗ₖ Y)) :
    ((1 : Matrix V V ℂ) ⊗ₖ (Y ⊗ₖ B)) * enlarge U (1 : Matrix H H ℂ)
      = enlarge U 1 * ((1 : Matrix V V ℂ) ⊗ₖ (Y ⊗ₖ B)) := by
  ext ⟨a, h, h'⟩ ⟨b, k, k'⟩
  have e := congrFun (congrFun hY (a, h)) (b, k)
  rw [hiddenKron_mul_apply, mul_hiddenKron_apply] at e
  simp only [mul_apply, kronecker_apply, one_apply, enlarge_apply, Fintype.sum_prod_type,
    ite_mul, mul_ite, one_mul, zero_mul, mul_zero, mul_one, Finset.sum_ite_irrel,
    Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  calc ∑ l, Y h l * B h' k' * U (a, l) (b, k) = B h' k' * ∑ l, Y h l * U (a, l) (b, k) := by
        rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun l _ => by ring
    _ = B h' k' * ∑ l, U (a, h) (b, l) * Y l k := by rw [e]
    _ = ∑ l, U (a, h) (b, l) * (Y l k * B h' k') := by
        rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun l _ => by ring

/-- `U ⊗ 𝟙_{H'}` is unitary when `U` is. -/
theorem enlarge_unitary (U : Matrix (V × H) (V × H) ℂ) (hU : Uᴴ * U = 1) :
    (enlarge U (1 : Matrix H H ℂ))ᴴ * enlarge U 1 = 1 := by
  unfold enlarge
  rw [conjTranspose_reindex, ← Matrix.coe_reindexAlgEquiv ℂ ℂ (Equiv.prodAssoc V H H), ← map_mul,
    conjTranspose_kronecker, ← mul_kronecker_mul, hU, conjTranspose_one, Matrix.one_mul,
    one_kronecker_one, map_one]

/-- **Trivial hidden commutant makes the reference separating for the commutant.** -/
theorem separating_of_hct [Nonempty V] [Nonempty H] (U : Matrix (V × H) (V × H) ℂ)
    (hU : HiddenCommutantTrivial U) (T : Matrix (V × (H × H)) (V × (H × H)) ℂ)
    (hX : ∀ X : Matrix V V ℂ, T * (X ⊗ₖ (1 : Matrix (H × H) (H × H) ℂ)) = (X ⊗ₖ 1) * T)
    (hT : T * enlarge U (1 : Matrix H H ℂ) = enlarge U 1 * T)
    (hΩ : ∀ ψ : V → ℂ, T *ᵥ (refVec ψ) = 0) : T = 0 := by
  obtain ⟨Z, rfl⟩ : ∃ Z, T = (1 : Matrix V V ℂ) ⊗ₖ Z := ⟨_, eq_oneKron_of_comm T hX⟩
  have hc : ∀ h' k', ∃ c : ℂ, ∀ h l, Z (h, h') (l, k') = if h = l then c else 0 := by
    intro h' k'
    obtain ⟨c, hc⟩ := hU _ (slice_comm U Z hT h' k')
    refine ⟨c, fun h l => ?_⟩
    have := congrFun (congrFun hc h) l
    simpa [Matrix.smul_apply, one_apply] using this
  choose c hc using hc
  have hm : (((Real.sqrt (Fintype.card H) : ℝ) : ℂ)⁻¹) ≠ 0 := by
    have : (0 : ℝ) < Real.sqrt (Fintype.card H) :=
      Real.sqrt_pos.2 (Nat.cast_pos.2 Fintype.card_pos)
    exact inv_ne_zero (by exact_mod_cast this.ne')
  have hzero : ∀ h h', c h' h = 0 := by
    intro h h'
    have := congrFun (hΩ (Pi.single (Classical.arbitrary V) 1)) (Classical.arbitrary V, (h, h'))
    simp only [mulVec, dotProduct, Fintype.sum_prod_type, kronecker_apply, one_apply, hc,
      Pi.single_apply, Pi.zero_apply, ite_mul, mul_ite, one_mul, zero_mul, mul_zero, mul_one,
      Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq',
      Finset.mem_univ, if_true] at this
    rcases mul_eq_zero.1 this with h0 | h0 <;> first | exact h0 | exact absurd h0 hm
  ext ⟨a, h, h'⟩ ⟨b, l, k'⟩
  simp [hc, hzero]

theorem one_kronecker_sub (A B : Matrix (H × H) (H × H) ℂ) :
    (1 : Matrix V V ℂ) ⊗ₖ (A - B) = (1 : Matrix V V ℂ) ⊗ₖ A - (1 : Matrix V V ℂ) ⊗ₖ B := by
  ext ⟨a, p⟩ ⟨b, q⟩
  simp [mul_sub]

/-- **A non-scalar hidden commutant element makes the reference non-separating**: the converse. -/
theorem hct_of_separating [Nonempty V] [Nonempty H] (U : Matrix (V × H) (V × H) ℂ)
    (hsep : ∀ T : Matrix (V × (H × H)) (V × (H × H)) ℂ,
      (∀ X : Matrix V V ℂ, T * (X ⊗ₖ (1 : Matrix (H × H) (H × H) ℂ)) = (X ⊗ₖ 1) * T) →
      T * enlarge U (1 : Matrix H H ℂ) = enlarge U 1 * T →
      (∀ ψ : V → ℂ, T *ᵥ (refVec ψ) = 0) → T = 0) :
    HiddenCommutantTrivial U := by
  intro Y hY
  have hT := hsep ((1 : Matrix V V ℂ) ⊗ₖ (Y ⊗ₖ (1 : Matrix H H ℂ) - (1 : Matrix H H ℂ) ⊗ₖ Yᵀ))
    (fun X => by
      rw [← mul_kronecker_mul, ← mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one,
        Matrix.one_mul, Matrix.mul_one])
    (by
      rw [one_kronecker_sub, Matrix.sub_mul, Matrix.mul_sub, hiddenKron_comm_enlarge U Y 1 hY,
        hiddenKron_comm_enlarge U 1 Yᵀ (by rw [one_kronecker_one, Matrix.one_mul, Matrix.mul_one])])
    (fun ψ => by
      funext ⟨a, h, h'⟩
      simp only [mulVec, dotProduct, Fintype.sum_prod_type, kronecker_apply, one_apply,
        Matrix.sub_apply, transpose_apply, Pi.zero_apply, ite_mul, mul_ite, one_mul, zero_mul,
        mul_zero, mul_one, sub_mul, Finset.sum_sub_distrib, Finset.sum_ite_irrel,
        Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ, if_true]
      ring)
  refine ⟨Y (Classical.arbitrary H) (Classical.arbitrary H), ?_⟩
  ext h h'
  have e := congrFun (congrFun hT (Classical.arbitrary V, (h, Classical.arbitrary H)))
    (Classical.arbitrary V, (h', Classical.arbitrary H))
  simp only [kronecker_apply, one_apply, Matrix.sub_apply, transpose_apply, Matrix.zero_apply,
    if_true, one_mul, mul_one] at e
  simp only [Matrix.smul_apply, one_apply, smul_eq_mul]
  by_cases hh : h = h'
  · subst hh
    simp only [if_true, mul_one]
    exact sub_eq_zero.1 (by simpa using e)
  · simp only [hh, if_false, mul_zero]
    simpa [hh] using e

/-- **The orthogonal projection onto a subspace invariant under `A` and `A†` commutes with `A`.** -/
theorem starProjection_comm {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [FiniteDimensional ℂ E] (M : Submodule ℂ E) [M.HasOrthogonalProjection] (A : E →ₗ[ℂ] E)
    (hA : ∀ x ∈ M, A x ∈ M) (hA' : ∀ x ∈ M, LinearMap.adjoint A x ∈ M) (x : E) :
    M.starProjection (A x) = A (M.starProjection x) := by
  have hx : x = M.starProjection x + (x - M.starProjection x) := (add_sub_cancel _ _).symm
  have h1 : M.starProjection (A (M.starProjection x)) = A (M.starProjection x) :=
    Submodule.starProjection_eq_self_iff.2 (hA _ (Submodule.starProjection_apply_mem M x))
  have h2 : M.starProjection (A (x - M.starProjection x)) = 0 := by
    refine (Submodule.starProjection_apply_eq_zero_iff M).2 ?_
    intro u hu
    rw [← LinearMap.adjoint_inner_left]
    exact Submodule.inner_right_of_mem_orthogonal (hA' u hu)
      (Submodule.sub_starProjection_mem_orthogonal x)
  conv_lhs => rw [hx]
  rw [map_add, map_add, h1, h2, add_zero]

/-- **`ST0(c)`.** For unitary `U`, the hidden commutant is trivial **iff** the reference subspace
`{ψ ⊗ Ω}` is cyclic for the `*`-algebra generated by `B(ℋ_V) ⊗ 𝟙` and `U ⊗ 𝟙_{H'}` — stated as:
every subspace containing every `ψ ⊗ Ω` and invariant under `X ⊗ 𝟙`, `U ⊗ 𝟙` and `(U ⊗ 𝟙)ᴴ` is
the whole space. -/
theorem ST0c_cyclic_iff [Nonempty V] [Nonempty H] (U : Matrix (V × H) (V × H) ℂ)
    (hU : Uᴴ * U = 1) :
    HiddenCommutantTrivial U ↔
      ∀ M : Submodule ℂ (EuclideanSpace ℂ (V × (H × H))),
        (∀ ψ : V → ℂ, WithLp.toLp 2 (refVec ψ) ∈ M) →
        (∀ X : Matrix V V ℂ, ∀ x ∈ M,
          Matrix.toEuclideanLin (X ⊗ₖ (1 : Matrix (H × H) (H × H) ℂ)) x ∈ M) →
        (∀ x ∈ M, Matrix.toEuclideanLin (enlarge U (1 : Matrix H H ℂ)) x ∈ M) →
        (∀ x ∈ M, Matrix.toEuclideanLin (enlarge U (1 : Matrix H H ℂ))ᴴ x ∈ M) → M = ⊤ := by
  have hŨ : (enlarge U (1 : Matrix H H ℂ))ᴴ * enlarge U 1 = 1 := enlarge_unitary U hU
  have hŨ' : enlarge U (1 : Matrix H H ℂ) * (enlarge U 1)ᴴ = 1 := mul_eq_one_comm.1 hŨ
  constructor
  · intro hct M hΩ hX hŨM hŨM'
    have : CompleteSpace M := FiniteDimensional.complete ℂ M
    let L : EuclideanSpace ℂ (V × (H × H)) →ₗ[ℂ] EuclideanSpace ℂ (V × (H × H)) :=
      LinearMap.id - (M.starProjection : EuclideanSpace ℂ (V × (H × H)) →L[ℂ] _).toLinearMap
    have hL : ∀ x, L x = x - M.starProjection x := fun x => rfl
    obtain ⟨T, hTL⟩ : ∃ T : Matrix (V × (H × H)) (V × (H × H)) ℂ, Matrix.toEuclideanLin T = L :=
      ⟨Matrix.toEuclideanLin.symm L, LinearEquiv.apply_symm_apply _ _⟩
    have comm : ∀ A : Matrix (V × (H × H)) (V × (H × H)) ℂ,
        (∀ x ∈ M, Matrix.toEuclideanLin A x ∈ M) →
        (∀ x ∈ M, Matrix.toEuclideanLin Aᴴ x ∈ M) → T * A = A * T := by
      intro A h1 h2
      refine Matrix.toEuclideanLin.injective ?_
      rw [Matrix.toLpLin_mul_same, Matrix.toLpLin_mul_same, hTL]
      refine LinearMap.ext fun x => ?_
      simp only [LinearMap.comp_apply, hL, map_sub]
      rw [starProjection_comm M (Matrix.toEuclideanLin A) h1
        (by rwa [← Matrix.toEuclideanLin_conjTranspose_eq_adjoint])]
    have hT := separating_of_hct U hct T
      (fun X => comm _ (hX X) (by rw [conjTranspose_kronecker, conjTranspose_one]; exact hX Xᴴ))
      (comm _ hŨM hŨM')
      (fun ψ => by
        have := congrArg (fun f => f (WithLp.toLp 2 (refVec ψ))) hTL
        simp only [Matrix.toLpLin_toLp, Matrix.toLin'_apply, hL] at this
        rw [Submodule.starProjection_eq_self_iff.2 (hΩ ψ), sub_self] at this
        exact (WithLp.toLp_eq_zero 2).1 this)
    rw [hT, map_zero] at hTL
    refine Submodule.eq_top_iff'.2 fun x => ?_
    have := congrArg (fun f => f x) hTL
    simp only [LinearMap.zero_apply, hL] at this
    exact Submodule.starProjection_eq_self_iff.1 (sub_eq_zero.1 this.symm).symm
  · intro hcyc
    refine hct_of_separating U fun T hX hT hΩ => ?_
    have hT' : T * (enlarge U (1 : Matrix H H ℂ))ᴴ = (enlarge U 1)ᴴ * T := by
      calc T * (enlarge U (1 : Matrix H H ℂ))ᴴ
          = (enlarge U 1)ᴴ * enlarge U 1 * T * (enlarge U 1)ᴴ := by rw [hŨ, Matrix.one_mul]
        _ = (enlarge U 1)ᴴ * (T * enlarge U 1) * (enlarge U 1)ᴴ := by
          rw [hT]; simp only [Matrix.mul_assoc]
        _ = (enlarge U 1)ᴴ * T * (enlarge U 1 * (enlarge U 1)ᴴ) := by
          simp only [Matrix.mul_assoc]
        _ = (enlarge U 1)ᴴ * T := by rw [hŨ', Matrix.mul_one]
    have hM := hcyc (LinearMap.ker (Matrix.toEuclideanLin T))
      (fun ψ => by
        rw [LinearMap.mem_ker, Matrix.toLpLin_toLp, Matrix.toLin'_apply, hΩ ψ]; rfl)
      (fun X x hx => by
        rw [LinearMap.mem_ker, ← LinearMap.comp_apply, ← Matrix.toLpLin_mul_same, hX X,
          Matrix.toLpLin_mul_same, LinearMap.comp_apply, LinearMap.mem_ker.1 hx, map_zero])
      (fun x hx => by
        rw [LinearMap.mem_ker, ← LinearMap.comp_apply, ← Matrix.toLpLin_mul_same, hT,
          Matrix.toLpLin_mul_same, LinearMap.comp_apply, LinearMap.mem_ker.1 hx, map_zero])
      (fun x hx => by
        rw [LinearMap.mem_ker, ← LinearMap.comp_apply, ← Matrix.toLpLin_mul_same, hT',
          Matrix.toLpLin_mul_same, LinearMap.comp_apply, LinearMap.mem_ker.1 hx, map_zero])
    exact (LinearEquiv.map_eq_zero_iff _).1 (LinearMap.ker_eq_top.1 hM)

end SemigroupTransfer
end OIBridge

#print axioms OIBridge.SemigroupTransfer.enlarge_apply
#print axioms OIBridge.SemigroupTransfer.visibleBlock_apply
#print axioms OIBridge.SemigroupTransfer.visibleBlock_enlarge
#print axioms OIBridge.SemigroupTransfer.familyAt_single
#print axioms OIBridge.SemigroupTransfer.amplitude_gram_entry
#print axioms OIBridge.SemigroupTransfer.krausOf_toEuclideanLin
#print axioms OIBridge.SemigroupTransfer.krausMap_smul
#print axioms OIBridge.SemigroupTransfer.sqrt_scalar_sq
#print axioms OIBridge.SemigroupTransfer.purifiedIsometry_apply
#print axioms OIBridge.SemigroupTransfer.familyAt_eq_stinespringChannel
#print axioms OIBridge.SemigroupTransfer.readingA_perTime
#print axioms OIBridge.SemigroupTransfer.conj_pow
#print axioms OIBridge.SemigroupTransfer.hiddenKron_unitary
#print axioms OIBridge.SemigroupTransfer.krausMap_mix
#print axioms OIBridge.SemigroupTransfer.mixing_unitary
#print axioms OIBridge.SemigroupTransfer.hiddenKron_mul_apply
#print axioms OIBridge.SemigroupTransfer.mul_hiddenKron_conjTranspose_apply
#print axioms OIBridge.SemigroupTransfer.kraus_hiddenConjugate
#print axioms OIBridge.SemigroupTransfer.familyAt_hiddenConjugate
#print axioms OIBridge.SemigroupTransfer.hiddenConjugate_family
#print axioms OIBridge.SemigroupTransfer.permMatrix_entry
#print axioms OIBridge.SemigroupTransfer.visibleBlock_conj
#print axioms OIBridge.SemigroupTransfer.sandwich_mul
#print axioms OIBridge.SemigroupTransfer.wordEval_conj
#print axioms OIBridge.SemigroupTransfer.trace_wordEval_conj
#print axioms OIBridge.SemigroupTransfer.wordEval_enlarge
#print axioms OIBridge.SemigroupTransfer.deltaWord_balanced
#print axioms OIBridge.SemigroupTransfer.trace_wordEval_enlarge
#print axioms OIBridge.SemigroupTransfer.trace_wordEval_hiddenConjugate
#print axioms OIBridge.SemigroupTransfer.pow_involution
#print axioms OIBridge.SemigroupTransfer.familyAt_involution_eq
#print axioms OIBridge.SemigroupTransfer.permMatrix_mul_self
#print axioms OIBridge.SemigroupTransfer.permMatrix_conjTranspose_self
#print axioms OIBridge.SemigroupTransfer.krausMap_expand
#print axioms OIBridge.SemigroupTransfer.familyAt_expand
#print axioms OIBridge.SemigroupTransfer.familyAt_eq_of_blockTraces
#print axioms OIBridge.SemigroupTransfer.hiddenKron_mul_permMatrix
#print axioms OIBridge.SemigroupTransfer.permMatrix_mul_hiddenKron
#print axioms OIBridge.SemigroupTransfer.trace_visibleBlock_hiddenConjugate
#print axioms OIBridge.SemigroupTransfer.pairA_blocks
#print axioms OIBridge.SemigroupTransfer.pairC_blocks
#print axioms OIBridge.SemigroupTransfer.adj_literals
#print axioms OIBridge.SemigroupTransfer.ST2_pairA
#print axioms OIBridge.SemigroupTransfer.pairC_hct
#print axioms OIBridge.SemigroupTransfer.pairC'_hct
#print axioms OIBridge.SemigroupTransfer.pairC_family
#print axioms OIBridge.SemigroupTransfer.ST3_pairC
#print axioms OIBridge.SemigroupTransfer.pairC_wordTraces
#print axioms OIBridge.SemigroupTransfer.ST4_pairC
#print axioms OIBridge.SemigroupTransfer.mul_hiddenKron_apply
#print axioms OIBridge.SemigroupTransfer.mul_singleKron_apply
#print axioms OIBridge.SemigroupTransfer.singleKron_mul_apply
#print axioms OIBridge.SemigroupTransfer.eq_oneKron_of_comm
#print axioms OIBridge.SemigroupTransfer.slice_comm
#print axioms OIBridge.SemigroupTransfer.hiddenKron_comm_enlarge
#print axioms OIBridge.SemigroupTransfer.enlarge_unitary
#print axioms OIBridge.SemigroupTransfer.separating_of_hct
#print axioms OIBridge.SemigroupTransfer.one_kronecker_sub
#print axioms OIBridge.SemigroupTransfer.hct_of_separating
#print axioms OIBridge.SemigroupTransfer.starProjection_comm
#print axioms OIBridge.SemigroupTransfer.ST0c_cyclic_iff
