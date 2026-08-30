/-
  OIBridge/AntiunitaryInvariance.lean — no operational data distinguish the two branches.

  PHASE TWO, ITEM ONE. The two-branch theorem leaves exactly one non-gauge ambiguity, the
  antiunitary branch H ↦ −H̄. This file proves that NO enlargement of the operational data —
  arbitrary preparations, channels, adaptive multi-time instrument sequences, and effects —
  can remove it: transposing every object in a circuit simultaneously,

      ρ ↦ ρᵀ,   E ↦ Eᵀ,   𝒢 ↦ T ∘ 𝒢 ∘ T,

  preserves every circuit probability. The proof is two lines of structure: interior transposes
  cancel in composition (`run_transposeMap`), and the trace pairing is transpose-invariant
  (`pairing_transpose`). Adaptive sequences are covered in full generality because
  `circuit_invariance` quantifies over ARBITRARY functions on matrices and arbitrary lists —
  each fixed outcome branch of an adaptive strategy is one such list — and the outcome-string
  form is made explicit for instrument sequences (`string_invariance`).

  The transformation is not an artifact of allowing arbitrary maps: it sends legitimate quantum
  operations to legitimate quantum operations. On a Kraus channel `X ↦ Σ_k A_k X A_k†` it acts
  by conjugating every Kraus operator (`transposeMap_kraus`), preserving complete positivity by
  construction, and it preserves the normalization Σ_k A_k†A_k = 1 (`kraus_normalization`).
  Restricted to unitary evolution it is EXACTLY the second branch: the transpose-conjugated
  channel of `e^{−iHt}` is the channel of `e^{−i(−H̄)t}` (`unitary_channel_transpose` together
  with `BohrFrequency.reflect_conj`). So the antiunitary ambiguity is a global symmetry of the
  entire operational formalism — self-consistent gate-set tomography of any length sees
  nothing — and anything that removes it must be MORE than circuit data. The thermal
  orientation that does remove it is OIBridge/ThermalOrientation.lean.
-/
import OIBridge.BohrFrequency
import Mathlib.LinearAlgebra.Matrix.Trace

namespace OIBridge
namespace AntiunitaryInvariance

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The transpose conjugation of a matrix map: `T ∘ 𝒢 ∘ T`. -/
def transposeMap (g : Matrix n n ℂ → Matrix n n ℂ) : Matrix n n ℂ → Matrix n n ℂ :=
  fun X => (g Xᵀ)ᵀ

/-- Running a circuit: apply the channels in order. -/
def run (gs : List (Matrix n n ℂ → Matrix n n ℂ)) (ρ : Matrix n n ℂ) : Matrix n n ℂ :=
  gs.foldl (fun X g => g X) ρ

omit [Fintype n] [DecidableEq n] in
/-- Interior transposes cancel: the transposed circuit run on the transposed state is the
transpose of the original run. -/
theorem run_transposeMap (gs : List (Matrix n n ℂ → Matrix n n ℂ)) (ρ : Matrix n n ℂ) :
    run (gs.map transposeMap) ρᵀ = (run gs ρ)ᵀ := by
  induction gs generalizing ρ with
  | nil => rfl
  | cons g gs ih =>
      show run (gs.map transposeMap) (transposeMap g ρᵀ) = (run gs (g ρ))ᵀ
      rw [show transposeMap g ρᵀ = (g ρ)ᵀ by rw [transposeMap, Matrix.transpose_transpose]]
      exact ih (g ρ)

omit [DecidableEq n] in
/-- The trace pairing of effect and state is transpose-invariant. -/
theorem pairing_transpose (Ef X : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * Xᵀ) = Matrix.trace (Ef * X) := by
  rw [← Matrix.transpose_mul, Matrix.trace_transpose, Matrix.trace_mul_comm]

omit [DecidableEq n] in
/-- **NO CIRCUIT DISTINGUISHES THE BRANCHES.** Transposing the preparation, every channel, and
the effect simultaneously preserves every circuit probability — for ARBITRARY matrix maps and
arbitrary finite sequences, hence for every fixed outcome branch of any adaptive multi-time
strategy. More operational data of this kind cannot remove the antiunitary ambiguity. -/
theorem circuit_invariance (gs : List (Matrix n n ℂ → Matrix n n ℂ))
    (ρ Ef : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * run (gs.map transposeMap) ρᵀ) = Matrix.trace (Ef * run gs ρ) := by
  rw [run_transposeMap, pairing_transpose]

/-- Entrywise conjugation, the operator form the transformed channels take. -/
def conjOp (M : Matrix n n ℂ) : Matrix n n ℂ := M.map (starRingEnd ℂ)

omit [Fintype n] [DecidableEq n] in
lemma transpose_conjTranspose_eq (M : Matrix n n ℂ) : (Mᴴ)ᵀ = conjOp M := by
  ext i j
  simp [conjOp, Matrix.conjTranspose_apply, Matrix.transpose_apply, Matrix.map_apply]

omit [Fintype n] [DecidableEq n] in
lemma conjOp_conjTranspose (M : Matrix n n ℂ) : (conjOp M)ᴴ = Mᵀ := by
  ext i j
  simp [conjOp, Matrix.conjTranspose_apply, Matrix.transpose_apply, Matrix.map_apply]

/-- A Kraus channel. -/
def krausMap {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ) :
    Matrix n n ℂ → Matrix n n ℂ :=
  fun X => ∑ k, A k * X * (A k)ᴴ

omit [DecidableEq n] in
/-- The transpose conjugation of a Kraus channel is the Kraus channel of the entrywise
conjugates: the transformed operation is again completely positive by construction. -/
theorem transposeMap_kraus {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ) :
    transposeMap (krausMap A) = krausMap (fun k => conjOp (A k)) := by
  funext X
  rw [transposeMap, krausMap]
  rw [Matrix.transpose_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose,
    transpose_conjTranspose_eq, ← conjOp_conjTranspose, Matrix.mul_assoc]

/-- Conjugating the Kraus operators preserves the trace-preservation normalization. -/
theorem kraus_normalization {κ : Type*} [Fintype κ] (A : κ → Matrix n n ℂ)
    (h : ∑ k, (A k)ᴴ * A k = 1) :
    ∑ k, (conjOp (A k))ᴴ * conjOp (A k) = 1 := by
  have h1 : ∀ k, (conjOp (A k))ᴴ * conjOp (A k) = ((A k)ᴴ * A k)ᵀ := by
    intro k
    rw [conjOp_conjTranspose, ← transpose_conjTranspose_eq, ← Matrix.transpose_mul]
  rw [Finset.sum_congr rfl fun k _ => h1 k, ← Matrix.transpose_sum, h, Matrix.transpose_one]

omit [DecidableEq n] in
/-- The outcome-string form for instrument sequences: the probability of any fixed outcome
string of any adaptive instrument sequence is a single Kraus-string sandwich, and it is
invariant under conjugating every operator and transposing state and effect. -/
theorem string_invariance (As : List (Matrix n n ℂ)) (ρ Ef : Matrix n n ℂ) :
    Matrix.trace (Efᵀ * ((As.map conjOp).foldl (fun X A => A * X * Aᴴ) ρᵀ))
      = Matrix.trace (Ef * (As.foldl (fun X A => A * X * Aᴴ) ρ)) := by
  have key : ∀ (As : List (Matrix n n ℂ)) (ρ : Matrix n n ℂ),
      (As.map conjOp).foldl (fun X A => A * X * Aᴴ) ρᵀ
        = (As.foldl (fun X A => A * X * Aᴴ) ρ)ᵀ := by
    intro As
    induction As with
    | nil => intro ρ; rfl
    | cons A As ih =>
        intro ρ
        show (As.map conjOp).foldl (fun X A => A * X * Aᴴ) (conjOp A * ρᵀ * (conjOp A)ᴴ)
          = (As.foldl (fun X A => A * X * Aᴴ) (A * ρ * Aᴴ))ᵀ
        rw [show conjOp A * ρᵀ * (conjOp A)ᴴ = (A * ρ * Aᴴ)ᵀ by
          rw [conjOp_conjTranspose, ← transpose_conjTranspose_eq,
            Matrix.transpose_mul, Matrix.transpose_mul, Matrix.mul_assoc]]
        exact ih (A * ρ * Aᴴ)
  rw [key, pairing_transpose]

omit [DecidableEq n] in
/-- The transpose conjugation of the unitary channel of `U` is the unitary channel of `Ū`.
With `BohrFrequency.reflect_conj` — `Ū(t)` is the propagator of the reflected model
`(V̄, −E)` — this identifies the circuit symmetry, restricted to unitary evolution, as
exactly the second branch `H ↦ −H̄`. -/
theorem unitary_channel_transpose (U : Matrix n n ℂ) :
    transposeMap (fun X => U * X * Uᴴ) = fun X => conjOp U * X * (conjOp U)ᴴ := by
  funext X
  rw [transposeMap]
  rw [Matrix.transpose_mul, Matrix.transpose_mul, Matrix.transpose_transpose,
    transpose_conjTranspose_eq, ← conjOp_conjTranspose, Matrix.mul_assoc]

#print axioms run_transposeMap
#print axioms pairing_transpose
#print axioms circuit_invariance
#print axioms transposeMap_kraus
#print axioms kraus_normalization
#print axioms string_invariance
#print axioms unitary_channel_transpose

end AntiunitaryInvariance
end OIBridge
