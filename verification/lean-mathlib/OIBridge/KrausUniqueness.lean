/-
  OIBridge/KrausUniqueness.lean — [Structure] Proposition 9.7a.

      Φ(ρ) = Σ A_i ρ A_i*  =  Σ B_j ρ B_j*,  both families LINEARLY INDEPENDENT
        ⟹  a unique unitary W with  B = A ∘ W,  and  |I| = |J|.

  THE CONSUMER, and only that. The mathematics of uniqueness lives in `OIBridge.FactorUniqueness`,
  where it is a statement about two injective maps into a common space with the same `X X*` and has
  no channel in it. This file does the four joins that turn that into the manuscript's proposition:
  the synthesis maps, their Gram operator, the reduction of channel equality to Gram equality, and
  the orientation.

  NO CHOI LAYER, and no positivity. The reduction is pointwise and elementary: evaluating the
  channel at the matrix unit `E_{bd}` and reading off entry `(a,c)` gives

      [Σ_i A_i E_{bd} A_i*]_{ac} = Σ_i A_i(a,b) · conj (A_i(c,d)),

  which is exactly the `((a,b),(c,d))` entry of the synthesis Gram operator `X X*`. So channel
  equality on the matrix units IS Gram equality, entry by entry. No Choi theorem, no complete
  positivity, no spectral theorem and no positive-semidefinite library appears anywhere — `X X*`
  is positive, but positivity is never used, which is why it is called the synthesis GRAM operator
  here and not "the positive operator".

  THE ORIENTATION IS A THEOREM, not a comment. `Y = X W` in the column convention reads
  `B_j = Σ_i W_ij A_i`, while the manuscript writes `B_j = Σ_i U_ji A_i`. The two differ by a
  transpose, and `krausMatrix_eq_transpose` records it in the kernel so the index order cannot
  drift silently — every character in this corpus is symmetric under inversion, and an orientation
  error of exactly this kind has cost this project a round before.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FactorUniqueness
import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Matrix.Basis

namespace OIBridge

namespace KrausUniqueness

set_option autoImplicit false

/- Several statements below use only part of the section's typeclass assumptions -- `krausMap_single`
never sums over the index type, `krausMatrix_eq_transpose` never touches the matrices. They are kept
under the shared variables because they exist only to serve `proposition_9_7a`, which uses all of
them, so the linter is silenced rather than the file fragmented. -/
set_option linter.unusedSectionVars false

open LinearMap Matrix Finset

variable {n I J : Type*} [Fintype n] [DecidableEq n]
  [Fintype I] [DecidableEq I] [Fintype J] [DecidableEq J]

local notation "⟪" x ", " y "⟫" => inner ℂ x y

/-! ### 1. The channel and the synthesis map

`krausMap` is kept purely algebraic — a finite sum of `A ρ A*` — because nothing below needs it to
be a channel. Trace preservation, complete positivity and the Choi correspondence play no role. -/

/-- The map a Kraus family generates. -/
def krausMap (A : I → Matrix n n ℂ) (ρ : Matrix n n ℂ) : Matrix n n ℂ :=
  ∑ i, A i * ρ * (A i)ᴴ

/-- **The synthesis map.** `e_i ↦ vec (A i)`, where `vec M (a, b) = M a b`. Its injectivity is
exactly linear independence of the family. -/
def synth (A : I → Matrix n n ℂ) : EuclideanSpace ℂ I →ₗ[ℂ] EuclideanSpace ℂ (n × n) where
  toFun v := WithLp.toLp 2 fun p => ∑ i, v i * A i p.1 p.2
  map_add' v w := by
    refine (WithLp.ext_iff 2).2 (funext fun p => ?_)
    simp [add_mul, Finset.sum_add_distrib]
  map_smul' c v := by
    refine (WithLp.ext_iff 2).2 (funext fun p => ?_)
    simp [Finset.mul_sum, mul_assoc]

@[simp] theorem synth_apply (A : I → Matrix n n ℂ) (v : EuclideanSpace ℂ I) (p : n × n) :
    synth A v p = ∑ i, v i * A i p.1 p.2 := rfl

/-- The analysis map, shown next to be the adjoint of `synth`. -/
def analysis (A : I → Matrix n n ℂ) : EuclideanSpace ℂ (n × n) →ₗ[ℂ] EuclideanSpace ℂ I where
  toFun u := WithLp.toLp 2 fun i => ∑ p : n × n, (starRingEnd ℂ) (A i p.1 p.2) * u p
  map_add' u w := by
    refine (WithLp.ext_iff 2).2 (funext fun i => ?_)
    simp [mul_add, Finset.sum_add_distrib]
  map_smul' c u := by
    refine (WithLp.ext_iff 2).2 (funext fun i => ?_)
    simp [Finset.mul_sum]
    exact Finset.sum_congr rfl fun p _ => by ring

@[simp] theorem analysis_apply (A : I → Matrix n n ℂ) (u : EuclideanSpace ℂ (n × n)) (i : I) :
    analysis A u i = ∑ p : n × n, (starRingEnd ℂ) (A i p.1 p.2) * u p := rfl

/-- **The analysis map is the adjoint.** Proved from `eq_adjoint_iff`, so the identification is a
theorem about inner products and not a definitional coincidence. -/
theorem adjoint_synth (A : I → Matrix n n ℂ) : adjoint (synth A) = analysis A := by
  refine ((eq_adjoint_iff (analysis A) (synth A)).2 fun u y => ?_).symm
  simp only [PiLp.inner_apply, RCLike.inner_apply, analysis_apply, synth_apply, map_sum, map_mul,
    RingHomCompTriple.comp_apply, RingHom.id_apply, Finset.sum_mul, Finset.mul_sum]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun p _ => Finset.sum_congr rfl fun i _ => by ring

/-! ### 2. The Gram entry

One computation, with all four indices explicit. This is the only place the adjoint is unfolded. -/

/-- **The synthesis Gram operator, entry by entry.** -/
theorem gram_entry (A : I → Matrix n n ℂ) (u : EuclideanSpace ℂ (n × n)) (p : n × n) :
    (synth A ∘ₗ adjoint (synth A)) u p
      = ∑ q : n × n, (∑ i, A i p.1 p.2 * (starRingEnd ℂ) (A i q.1 q.2)) * u q := by
  rw [LinearMap.comp_apply, adjoint_synth, synth_apply]
  simp only [analysis_apply, Finset.sum_mul]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun q _ => Finset.sum_congr rfl fun i _ => by ring

/-! ### 3. Channel equality is Gram equality

Evaluate at the matrix unit `E_{bd}` and read off entry `(a, c)`. That single evaluation delivers
every coefficient of the Gram operator, which is why no Choi theorem is needed. -/

/-- **The pointwise identity the whole reduction turns on.** -/
theorem krausMap_single (A : I → Matrix n n ℂ) (a b c d : n) :
    krausMap A (Matrix.single b d 1) a c = ∑ i, A i a b * (starRingEnd ℂ) (A i c d) := by
  rw [krausMap, Matrix.sum_apply]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.mul_apply, Finset.sum_eq_single d]
  · rw [Matrix.mul_single_apply_same, Matrix.conjTranspose_apply]
    simp
  · intro x _ hx
    simp [Matrix.mul_apply, Matrix.single, Ne.symm hx]
  · intro hc
    exact absurd (Finset.mem_univ d) hc

/-- **The join.** Equal channels have equal synthesis Gram operators. -/
theorem synth_gram_eq_of_krausMap_eq {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    (h : krausMap A = krausMap B) :
    synth A ∘ₗ adjoint (synth A) = synth B ∘ₗ adjoint (synth B) := by
  have hentry : ∀ a b c d : n,
      (∑ i, A i a b * (starRingEnd ℂ) (A i c d)) = ∑ j, B j a b * (starRingEnd ℂ) (B j c d) := by
    intro a b c d
    rw [← krausMap_single A a b c d, ← krausMap_single B a b c d, h]
  refine LinearMap.ext fun u => (WithLp.ext_iff 2).2 (funext fun p => ?_)
  rw [gram_entry, gram_entry]
  exact Finset.sum_congr rfl fun q _ => by rw [hentry p.1 p.2 q.1 q.2]

/-! ### 4. Independence is injectivity, and the theorem -/

/-- **Linear independence of the family is injectivity of its synthesis map.** -/
theorem synth_injective_of_linearIndependent {A : I → Matrix n n ℂ}
    (hA : LinearIndependent ℂ A) : Function.Injective (synth A) := by
  rw [← LinearMap.ker_eq_bot, Submodule.eq_bot_iff]
  intro v hv
  have hcoef : ∀ i, v i = 0 := by
    refine Fintype.linearIndependent_iff.1 hA (fun i => v i) ?_
    refine Matrix.ext fun a b => ?_
    have := congrArg (fun w : EuclideanSpace ℂ (n × n) => w (a, b)) (LinearMap.mem_ker.1 hv)
    simpa [Matrix.sum_apply] using this
  refine (WithLp.ext_iff 2).2 (funext fun i => ?_)
  simpa using hcoef i

/-- **[Structure] Proposition 9.7a.** Two linearly independent Kraus families of the same map are
related by a unique unitary on the coefficient space.

The coefficient spaces are indexed by unrelated types `I` and `J`. That `|I| = |J|` follows is the
content of `card_eq` below, and stating it as a conclusion rather than a hypothesis is the point of
`FactorUniqueness` keeping its two index types apart. -/
theorem kraus_uniqueness {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    (hA : LinearIndependent ℂ A) (hB : LinearIndependent ℂ B) (h : krausMap A = krausMap B) :
    ∃! W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I,
      synth A ∘ₗ W = synth B ∧ adjoint W ∘ₗ W = LinearMap.id ∧
        W ∘ₗ adjoint W = LinearMap.id :=
  FactorUniqueness.existsUnique_unitary_factor (synth_injective_of_linearIndependent hA)
    (synth_injective_of_linearIndependent hB) (synth_gram_eq_of_krausMap_eq h)

/-- **Equal cardinality is a consequence.** -/
theorem card_eq {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    (hA : LinearIndependent ℂ A) (hB : LinearIndependent ℂ B) (h : krausMap A = krausMap B) :
    Fintype.card J = Fintype.card I := by
  have := FactorUniqueness.finrank_eq (synth_injective_of_linearIndependent hA)
    (synth_injective_of_linearIndependent hB) (synth_gram_eq_of_krausMap_eq h)
  simpa using this

/-! ### The orientation

`Y = X W` in the column convention is `B_j = Σ_i W_ij A_i`; the manuscript writes
`B_j = Σ_i U_ji A_i`. `U` is the TRANSPOSE of the factor's column matrix, and that is recorded here
as a theorem rather than as a remark. -/

/-- The factor's matrix in the column convention: column `j` is the image of `e_j`. -/
noncomputable def factorMatrix (W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I) : Matrix I J ℂ :=
  fun i j => W (EuclideanSpace.single j 1) i

/-- The manuscript's Kraus-mixing matrix, in the convention `B_j = Σ_i U_ji A_i`. -/
noncomputable def krausMatrix (W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I) : Matrix J I ℂ :=
  fun j i => W (EuclideanSpace.single j 1) i

/-- **The orientation guard.** The manuscript's `U` is the transpose of the factor's column
matrix. -/
theorem krausMatrix_eq_transpose (W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I) :
    krausMatrix W = (factorMatrix W)ᵀ := rfl

/-- **The Kraus relation in the manuscript's index order.** -/
theorem kraus_relation {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    {W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I} (hW : synth A ∘ₗ W = synth B) (j : J) :
    B j = ∑ i, krausMatrix W j i • A i := by
  refine Matrix.ext fun a b => ?_
  have hj := congrArg (fun g : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ (n × n) =>
    g (EuclideanSpace.single j 1) (a, b)) hW
  simp only [LinearMap.comp_apply, synth_apply] at hj
  rw [Matrix.sum_apply]
  simp only [krausMatrix, Matrix.smul_apply, smul_eq_mul]
  rw [hj]
  simp [PiLp.single_apply, Finset.sum_ite_eq']

/-- **The same relation in the column convention**, so that the two orders sit side by side and the
transpose is visible rather than inferred. -/
theorem kraus_relation_column {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    {W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I} (hW : synth A ∘ₗ W = synth B) (j : J) :
    B j = ∑ i, factorMatrix W i j • A i :=
  kraus_relation hW j

/-- **The mixing matrix is unitary**, in the manuscript's index order: the rows of `U` are
orthonormal, which is `U Uᴴ = 1`. -/
theorem krausMatrix_mul_conjTranspose {W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I}
    (hW : adjoint W ∘ₗ W = LinearMap.id) :
    krausMatrix W * (krausMatrix W)ᴴ = 1 := by
  refine Matrix.ext fun j j' => ?_
  have hpt : adjoint W (W (EuclideanSpace.single j' 1)) = EuclideanSpace.single j' 1 :=
    congrArg (fun g : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ J =>
      g (EuclideanSpace.single j' 1)) hW
  have hiso : ⟪W (EuclideanSpace.single j' 1), W (EuclideanSpace.single j 1)⟫
      = ⟪(EuclideanSpace.single j' 1 : EuclideanSpace ℂ J), EuclideanSpace.single j 1⟫ := by
    rw [← adjoint_inner_left W (EuclideanSpace.single j 1) (W (EuclideanSpace.single j' 1)), hpt]
  rw [EuclideanSpace.inner_single_left] at hiso
  simp only [map_one, one_mul, PiLp.single_apply, PiLp.inner_apply,
    RCLike.inner_apply] at hiso
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, krausMatrix, Matrix.one_apply,
    RCLike.star_def]
  rw [hiso]
  by_cases hjj : j = j' <;> simp [hjj, eq_comm]

/-! ### Proposition 9.7a

The four joins assembled: independence is injectivity, channel equality is Gram equality, the
factor theorem supplies the unitary, and the orientation is the transpose. -/

/-- **[Structure] Proposition 9.7a, assembled.**

Two linearly independent Kraus families of the same map have equal cardinality and are related by a
unique unitary; in the manuscript's index order `B_j = Σ_i U_ji A_i` with `U Uᴴ = 1`, and `U` is the
TRANSPOSE of the factor's column matrix. -/
theorem proposition_9_7a {A : I → Matrix n n ℂ} {B : J → Matrix n n ℂ}
    (hA : LinearIndependent ℂ A) (hB : LinearIndependent ℂ B) (h : krausMap A = krausMap B) :
    Fintype.card J = Fintype.card I ∧
    (∃! W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I,
      synth A ∘ₗ W = synth B ∧ adjoint W ∘ₗ W = LinearMap.id ∧
        W ∘ₗ adjoint W = LinearMap.id) ∧
    (∀ W : EuclideanSpace ℂ J →ₗ[ℂ] EuclideanSpace ℂ I, synth A ∘ₗ W = synth B →
      adjoint W ∘ₗ W = LinearMap.id →
        (∀ j, B j = ∑ i, krausMatrix W j i • A i) ∧
        krausMatrix W * (krausMatrix W)ᴴ = 1 ∧
        krausMatrix W = (factorMatrix W)ᵀ) :=
  ⟨card_eq hA hB h, kraus_uniqueness hA hB h,
   fun W hWf hWu => ⟨kraus_relation hWf, krausMatrix_mul_conjTranspose hWu,
     krausMatrix_eq_transpose W⟩⟩

/-! ### What these proofs rest on -/

#print axioms adjoint_synth
#print axioms gram_entry
#print axioms krausMap_single
#print axioms synth_gram_eq_of_krausMap_eq
#print axioms synth_injective_of_linearIndependent
#print axioms kraus_uniqueness
#print axioms card_eq
#print axioms krausMatrix_eq_transpose
#print axioms kraus_relation
#print axioms krausMatrix_mul_conjTranspose
#print axioms proposition_9_7a

end KrausUniqueness

end OIBridge
