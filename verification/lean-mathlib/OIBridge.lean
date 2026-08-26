/-
  OIBridge.lean — ROADMAP §A1/§A5, in the form the counting layer consumes.

  `OI_Gauge_Certificates.lean` kernel-checks the character sums 72 / 288 / 144 over the
  24-element cubic rotation group, and `OI_Regulator_Symmetry.lean` the sums 384 / 192 over
  the hypercubic and native groups. Neither can divide by the group order to obtain a
  *dimension*: that step needs a field, a module, and the trace of a projection —
  finite-dimensional linear algebra, not finite arithmetic. Hence this file, and hence its
  separate directory: it is the only part of the verification layer that depends on Mathlib.
  The five core proof files remain self-contained with zero imports and keep their own gate.

  What this file contributes is narrower than it first appears. **Mathlib already proves both
  identities** — the averaging identity as `card_inv_mul_sum_char_eq_finrank`, and the
  equivariant-map dimension formula as `card_inv_mul_sum_char_mul_char_eq_finrank`. All that
  is added here is the restatement with the group order cleared to the left, which is the
  shape the kernel-checked integer sums are in. See the note before the first theorem.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.RepresentationTheory.Invariants
import Mathlib.RepresentationTheory.Character
import Mathlib.LinearAlgebra.Trace

namespace OIBridge

open LinearMap Representation

/- `Module.Finite k V` is retained deliberately, and Lean's unused-variable linter is
correspondingly silenced here rather than the hypothesis dropped. The identity does hold
without it, but only degenerately: for a module that is not finite and free both
`Module.finrank` and `LinearMap.trace` take junk values of zero, so the statement reduces to
`0 = 0` and asserts nothing. Finite-dimensionality is what makes it a theorem about
dimensions, which is the only reading the counting layer can use. -/
set_option linter.unusedSectionVars false

variable {k G V : Type*} [Field k] [Group G] [Fintype G]
  [AddCommGroup V] [Module k V] [Module.Finite k V]
  [Invertible (Fintype.card G : k)]

/-! ### The averaging identity is Mathlib's, not this file's

An earlier version of this file proved

    (Fintype.card G) * finrank k (invariants ρ) = ∑ g, ρ.character g

from `isProj_averageMap` and `LinearMap.IsProj.trace`, and the roadmap described it as the one
classical identity the layer had to supply. That was wrong: Mathlib already carries exactly
this result, by exactly that proof, as

    Representation.card_inv_mul_sum_char_eq_finrank :
      (Nat.card G : k)⁻¹ * ∑ g : G, ρ.character g = finrank k (invariants ρ)

in `Mathlib/RepresentationTheory/Character.lean`. The reconstruction was sound but redundant —
the pieces were checked and the assembled statement was not. What follows therefore *derives*
the multiplied form from Mathlib's, rather than reproving it, so the file states only what it
actually adds: the identity in the shape the counting layer consumes, with the group order on
the left instead of an inverse on the right. -/

/-- **§A1, restated.** The group order times the dimension of the invariant subspace equals
the character sum. This is `Representation.card_inv_mul_sum_char_eq_finrank` with the
inverse cleared, which is the form the kernel-checked sums of the core layer are in:
`72 = 24 · 3`, `288 = 24 · 12`, `144 = 24 · 6`, `384 = 384 · 1` against `192 = 96 · 2`. -/
theorem card_mul_finrank_invariants (ρ : Representation k G V) :
    (Fintype.card G : k) * (Module.finrank k (invariants ρ) : k) = ∑ g : G, ρ.character g := by
  have hcard : (Nat.card G : k) = (Fintype.card G : k) := by
    rw [Nat.card_eq_fintype_card]
  have h := ρ.card_inv_mul_sum_char_eq_finrank
  rw [hcard] at h
  rw [← h, ← mul_assoc, mul_inv_cancel₀, one_mul]
  exact Invertible.ne_zero _

/-- The dimension of the space of equivariant maps, which is what the counting layer's
`72 / 288 / 144` actually measure. Mathlib supplies this too — it is the engine behind §A5
and §B1, and no part of it needed building here. -/
theorem finrank_intertwiners {W : Type*} [AddCommGroup W] [Module k W] [Module.Finite k W]
    (ρ : Representation k G V) (σ : Representation k G W) :
    (Fintype.card G : k) * (Module.finrank k (IntertwiningMap ρ σ) : k)
      = ∑ g : G, σ.character g * ρ.character g⁻¹ := by
  have hcard : (Nat.card G : k) = (Fintype.card G : k) := by
    rw [Nat.card_eq_fintype_card]
  have h := Representation.card_inv_mul_sum_char_mul_char_eq_finrank ρ σ
  rw [hcard] at h
  rw [← h, ← mul_assoc, mul_inv_cancel₀, one_mul]
  exact Invertible.ne_zero _

end OIBridge
