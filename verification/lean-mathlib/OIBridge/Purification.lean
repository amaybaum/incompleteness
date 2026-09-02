/-
  OIBridge/Purification.lean — the H-pure-seed reduction (uniform ancilla + rank-one
  readout + feed-forward derives the pure seed) and finite-dimensional purification.

  PHASE THREE, ROUND TWENTY-ONE. Round twenty exhibited H-pure-seed as load-bearing:
  the uniform hidden state alone cannot supply state preparation. This file asks the
  sharper question the owner posed — does NATIVE SELECTIVE READOUT + FEED-FORWARD
  already derive H-pure-seed? — and answers it affirmatively at the kernel level,
  which reduces the round-twenty four-principle endpoint toward three.

  §A — THE SEED FROM READOUT + FEED-FORWARD. `branch_project`: the Lüders branch update
  `P_k ρ P_k = ρ_kk · P_k` on a rank-one basis projector. `mixed_branch_is_pure`: the
  uniform ancilla `I/m` selectively read at `k` gives `P_k (I/m) P_k = (1/m) P_k`, a
  pure state up to normalization. `readout_feedforward_reset`: with outcome-dependent
  reversible controls `R_k` rotating `|k⟩ ↦ |s₀⟩`, the no-postselection sum

      Σ_k R_k (P_k ρ P_k) R_k†  =  Tr(ρ) · |s₀⟩⟨s₀|

  is exactly the reset channel — state preparation, feed-forward, no postselection.
  `uniform_readout_feedforward_seed`: at `ρ = I/m` this is `|s₀⟩⟨s₀|`, the pure seed.

      ┌────────────────────────────────────────────────────────────────────┐
      │  Does native selective readout + feed-forward derive H-pure-seed?   │
      │  YES — uniform ancilla + rank-one Lüders readout + reversible        │
      │  feed-forward prepares |s₀⟩⟨s₀|. So H-pure-seed is NOT an           │
      │  independent bridge, PROVIDED the rank-one selective readout is      │
      │  itself operationally licensed (`luders_selector_cp` gives its       │
      │  form; whether OI licenses it is the remaining guard).               │
      └────────────────────────────────────────────────────────────────────┘

  `luders_selector_cp`: the branch update `X ↦ P_k X P_k` realizes the rank-one
  classical selector `Φ(E_ss) = δ_ks E_kk` — the epistemic guard is exactly whether
  this coherent (Lüders) branch update is bare-OI-licensed, not a new freedom.

  §B — PURIFICATION. `purification_partialTrace`: for any amplitude matrix `A`, the
  vectorized pure state `|Ψ_A⟩ = Σ_ij A_ij |i⟩|j⟩` purifies `A Aᴴ`:

      Tr_E |Ψ_A⟩⟨Ψ_A|  =  A Aᴴ.

  `purification_of_factorization`: hence any `ρ = A Aᴴ` has a pure purification (and
  every PSD `ρ` factorizes as `A Aᴴ` by the standard finite square-root, isolated as
  the factorization hypothesis; SINCE ROUND THIRTY-FOUR that hypothesis is dischargeable
  inside the kernel by `psdFactorization_of_spectral`, and `BoundaryAudit.lean` records the
  discharged form `purification_unconditional` — the conditional theorem is kept as the
  local architecture). Purifier uniqueness `A Aᴴ = B Bᴴ ⟹ B = A U` for a
  unitary `U` is the standard finite Schmidt/Uhlmann theorem, recorded as the cited
  external result rather than reproved. [DISCHARGED IN ROUND FORTY-EIGHT for every finite
  `S`, `E`: `UhlmannUniqueness.rightUnitary_of_gram`, with `purifier_uniqueness` the
  purification form; the statement above is kept as provenance.]

  THE ENDPOINT REDUCTION. If the Lüders branch update is OI-licensed, H-pure-seed
  collapses and the four named endpoint conditions become three: H-functor, H-tensor,
  and sufficient composite Lie rank.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.InstrumentDilation

namespace OIBridge
namespace Purification

open Complex Matrix InstrumentDilation
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

/-! ### Section A — the seed from readout + feed-forward -/

section Readout

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- The rank-one basis projector `P_k = |k⟩⟨k|`. -/
def rankOneProj (k : ι) : Matrix ι ι ℂ := Matrix.single k k 1

/-- **THE LÜDERS BRANCH UPDATE.** Projecting onto a rank-one basis state gives the
population times the projector: `P_k ρ P_k = ρ_kk · P_k`. -/
theorem branch_project (ρ : Matrix ι ι ℂ) (k : ι) :
    rankOneProj k * ρ * rankOneProj k = ρ k k • rankOneProj k := by
  ext i j
  simp only [rankOneProj]
  by_cases hi : i = k <;> by_cases hj : j = k <;>
    simp [hi, hj, Matrix.smul_apply,
      Matrix.mul_single_apply_same, Matrix.single_mul_apply_same,
      Matrix.mul_single_apply_of_ne, Matrix.single_mul_apply_of_ne, Ne.symm]

/-- **THE MIXED BRANCH IS PURE.** Reading the uniform ancilla `I/m` selectively at
outcome `k` gives `(1/m)·P_k`, a rank-one (pure) state up to normalization. -/
theorem mixed_branch_is_pure [Nonempty ι] (k : ι) :
    rankOneProj k * ((Fintype.card ι : ℂ)⁻¹ • (1 : Matrix ι ι ℂ)) * rankOneProj k
      = (Fintype.card ι : ℂ)⁻¹ • rankOneProj k := by
  rw [branch_project, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one]

omit [DecidableEq ι] in
/-- The trace as a sum of diagonal populations. -/
theorem trace_eq_sum_diag (ρ : Matrix ι ι ℂ) : Matrix.trace ρ = ∑ k, ρ k k := rfl

/-- **READOUT + FEED-FORWARD IS RESET.** With outcome-dependent reversible controls
`R_k` rotating `|k⟩ ↦ |s₀⟩`, summing the fed-forward branch post-states over all
outcomes — no postselection — is exactly the reset (state-preparation) channel. -/
theorem readout_feedforward_reset (ρ : Matrix ι ι ℂ) (R : ι → Matrix ι ι ℂ) (s₀ : ι)
    (hR : ∀ k, R k * rankOneProj k * (R k)ᴴ = rankOneProj s₀) :
    (∑ k, R k * (rankOneProj k * ρ * rankOneProj k) * (R k)ᴴ)
      = InstrumentDilation.resetChannel s₀ ρ := by
  have hterm : ∀ k, R k * (rankOneProj k * ρ * rankOneProj k) * (R k)ᴴ
      = ρ k k • rankOneProj s₀ := by
    intro k
    rw [branch_project, Matrix.mul_smul, Matrix.smul_mul, hR]
  rw [Finset.sum_congr rfl fun k _ => hterm k, ← Finset.sum_smul,
    InstrumentDilation.resetChannel, rankOneProj, trace_eq_sum_diag]

/-- **THE PURE SEED, DERIVED.** At the uniform input `ρ = I/m`, readout + feed-forward
yields `|s₀⟩⟨s₀|`: the pure ancilla seed is prepared from the uniform hidden state by
selective rank-one readout and reversible feed-forward alone. -/
theorem uniform_readout_feedforward_seed [Nonempty ι] (R : ι → Matrix ι ι ℂ) (s₀ : ι)
    (hR : ∀ k, R k * rankOneProj k * (R k)ᴴ = rankOneProj s₀) :
    (∑ k, R k * (rankOneProj k * ((Fintype.card ι : ℂ)⁻¹ • (1 : Matrix ι ι ℂ))
        * rankOneProj k) * (R k)ᴴ)
      = rankOneProj s₀ := by
  have hm : (Fintype.card ι : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  rw [readout_feedforward_reset _ R s₀ hR, InstrumentDilation.resetChannel, rankOneProj]
  rw [show Matrix.trace ((Fintype.card ι : ℂ)⁻¹ • (1 : Matrix ι ι ℂ)) = 1 from by
    rw [Matrix.trace_smul, Matrix.trace_one, smul_eq_mul, inv_mul_cancel₀ hm], one_smul]

/-- **THE LÜDERS SELECTOR.** The branch update `X ↦ P_k X P_k` realizes the rank-one
classical selector `Φ(E_ss) = δ_ks E_kk`: it is the coherent form of the OI branch
outcome, and whether bare OI licenses THIS update is the remaining epistemic guard. -/
theorem luders_selector_cp (k s : ι) :
    rankOneProj k * Matrix.single s s 1 * rankOneProj k
      = if s = k then rankOneProj k else 0 := by
  rw [branch_project, Matrix.single_apply]
  by_cases h : s = k
  · rw [if_pos ⟨h, h⟩, if_pos h, one_smul]
  · rw [if_neg (fun hh => h hh.1), if_neg h, zero_smul]

end Readout

/-! ### Section B — finite-dimensional purification -/

section Purify

variable {S E : Type*} [Fintype S] [DecidableEq S] [Fintype E] [DecidableEq E]

/-- The vectorized pure state `|Ψ_A⟩ = Σ_ij A_ij |i⟩ ⊗ |j⟩`. -/
def purifVec (A : Matrix S E ℂ) : S × E → ℂ := fun p => A p.1 p.2

/-- The partial trace over the second (environment) factor. -/
def ptraceB (M : Matrix (S × E) (S × E) ℂ) : Matrix S S ℂ :=
  Matrix.of fun s t => ∑ e, M (s, e) (t, e)

omit [Fintype S] [DecidableEq S] [DecidableEq E] in
/-- **PURIFICATION.** For any amplitude matrix `A`, the vectorized pure state purifies
`A Aᴴ`: tracing out the environment of `|Ψ_A⟩⟨Ψ_A|` returns `A Aᴴ`. -/
theorem purification_partialTrace (A : Matrix S E ℂ) :
    ptraceB (Matrix.vecMulVec (purifVec A) (star (purifVec A))) = A * Aᴴ := by
  ext s t
  rw [ptraceB, Matrix.of_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [Matrix.vecMulVec_apply, purifVec, Pi.star_apply, purifVec, Complex.star_def,
    Matrix.conjTranspose_apply, Complex.star_def]

omit [Fintype S] [DecidableEq S] [DecidableEq E] in
/-- **PURIFICATION EXISTS.** Any `ρ = A Aᴴ` has the pure purification `|Ψ_A⟩`; every
PSD `ρ` factorizes this way by the standard finite square-root. -/
theorem purification_of_factorization (A : Matrix S E ℂ) (ρ : Matrix S S ℂ)
    (hρ : ρ = A * Aᴴ) :
    ptraceB (Matrix.vecMulVec (purifVec A) (star (purifVec A))) = ρ := by
  rw [purification_partialTrace, hρ]

end Purify

#print axioms rankOneProj
#print axioms branch_project
#print axioms mixed_branch_is_pure
#print axioms trace_eq_sum_diag
#print axioms readout_feedforward_reset
#print axioms uniform_readout_feedforward_seed
#print axioms luders_selector_cp
#print axioms purification_partialTrace
#print axioms purification_of_factorization

end Purification
end OIBridge
