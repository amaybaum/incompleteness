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
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.GroupTheory.Perm.Fin

namespace OIBridge

open LinearMap Representation

/- `Module.Finite k V` is retained deliberately, and Lean's unused-variable linter is
correspondingly silenced here rather than the hypothesis dropped. The identity does hold
without it, but only degenerately: for a module that is not finite and free both
`Module.finrank` and `LinearMap.trace` take junk values of zero, so the statement reduces to
`0 = 0` and asserts nothing. Finite-dimensionality is what makes it a theorem about
dimensions, which is the only reading the counting layer can use. -/
set_option linter.unusedSectionVars false

/- The group order is written `Nat.card G`, matching the Mathlib statements these derive
from. `Fintype.card` would read more naturally beside the core layer's integer sums, but the
two are different *instances* of `Invertible` even though they are propositionally equal, and
carrying the mismatch would mean converting at every use site for no gain. -/
variable {k G V : Type*} [Field k] [Group G] [Fintype G]
  [AddCommGroup V] [Module k V] [Module.Finite k V]
  [Invertible (Nat.card G : k)]

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
    (Nat.card G : k) * (Module.finrank k (invariants ρ) : k) = ∑ g : G, ρ.character g := by
  rw [← ρ.card_inv_mul_sum_char_eq_finrank, ← mul_assoc, mul_inv_cancel₀, one_mul]
  exact Invertible.ne_zero _

/-- The dimension of the space of equivariant maps, which is what the counting layer's
`72 / 288 / 144` actually measure. Mathlib supplies this too — it is the engine behind §A5
and §B1, and no part of it needed building here. -/
theorem finrank_intertwiners {W : Type*} [AddCommGroup W] [Module k W] [Module.Finite k W]
    (ρ : Representation k G V) (σ : Representation k G W) :
    (Nat.card G : k) * (Module.finrank k (IntertwiningMap ρ σ) : k)
      = ∑ g : G, σ.character g * ρ.character g⁻¹ := by
  rw [← Representation.card_inv_mul_sum_char_mul_char_eq_finrank ρ σ, ← mul_assoc,
    mul_inv_cancel₀, one_mul]
  exact Invertible.ne_zero _



/-! ## §A10 — the cubic representation, and §A5/§B1 read off it

The counting layer's `72 / 288 / 144` are integer sums over a list of signed permutation
records. To make them *dimensions* they must be sums over a genuine `Representation`, which
is what this section supplies.

The model is the classical one. The rotation group of the cube is `S₄`, acting on the four
body diagonals, and the six faces — equivalently the six directed links — are the six
two-element subsets of those four diagonals. So `V₆` is the permutation representation of
`Equiv.Perm (Fin 4)` on `{s : Finset (Fin 4) // s.card = 2}`.

Two things make this cheap. `Equiv.Perm (Fin 4)` is already a group of order 24, so no
subgroup or closure computation is needed. And `Matrix.trace_permutation` already states that
the trace of a permutation matrix is its fixed-point count, so the character needs no new
theory — it is a finite count, and the sums over the group are decidable.

The identification with the cubic character is not asserted here: it is checked in
`representation_bridge_probe.py`, which compares the two character multisets element by
element. -/

namespace Cubic

open Equiv

/-- The six faces of the cube, as two-element subsets of the four body diagonals. -/
abbrev Face := {s : Finset (Fin 4) // s.card = 2}

instance : DecidableEq Face := Subtype.instDecidableEq

theorem card_face : Fintype.card Face = 6 := by decide

/-- A permutation of the diagonals permutes the faces. -/
def act (g : Perm (Fin 4)) : Perm Face :=
  Equiv.subtypeEquiv g.finsetCongr (by
    intro s
    simp [Equiv.finsetCongr_apply, Finset.card_map])

@[simp] theorem act_coe (g : Perm (Fin 4)) (s : Face) :
    ((act g s) : Finset (Fin 4)) = s.1.map g.toEmbedding := rfl

/-- The face action as a group homomorphism. -/
def actHom : Perm (Fin 4) →* Perm Face where
  toFun := act
  map_one' := by
    ext s x
    simp [act_coe]
  map_mul' g h := by
    ext s x
    simp [act_coe, Finset.mem_map, Perm.mul_apply]
    constructor
    · rintro ⟨a, ha, rfl⟩; exact ⟨h a, ⟨a, ha, rfl⟩, rfl⟩
    · rintro ⟨b, ⟨a, ha, rfl⟩, rfl⟩; exact ⟨a, ha, rfl⟩

/-- The permutation representation of `S₄` on the six faces — this is `V₆`. -/
noncomputable def rho : Representation ℚ (Perm (Fin 4)) (Face → ℚ) where
  toFun g := (Equiv.Perm.permMatrix ℚ (actHom g⁻¹)).toLin'
  map_one' := by
    ext v x
    simp [Matrix.toLin'_apply, Matrix.permMatrix_mulVec, Function.comp]
  map_mul' g h := by
    ext v x
    simp [Matrix.toLin'_apply, Matrix.permMatrix_mulVec, Function.comp, mul_inv_rev,
      map_mul, Perm.mul_apply]

/-- The number of faces fixed by `g`, as a decidable count. It is phrased on `g⁻¹` to match
`rho`, which uses the inverse to get the homomorphism direction right; summed over the whole
group the distinction is immaterial, and keeping it here avoids an inverse-juggling step in
the character lemma. -/
def fixCount (g : Perm (Fin 4)) : ℕ :=
  (Finset.univ.filter (fun s : Face => actHom g⁻¹ s = s)).card

/-- The character of `V₆` is the fixed-face count. This is `Matrix.trace_permutation` — the
trace of a permutation matrix is the number of points it fixes — which Mathlib already
supplies, so no new trace theory is needed here. -/
theorem character_eq_fixCount (g : Perm (Fin 4)) :
    rho.character g = (fixCount g : ℚ) := by
  have hset : (Function.fixedPoints (actHom g⁻¹)).toFinset
      = Finset.univ.filter (fun s : Face => actHom g⁻¹ s = s) := by
    ext s
    simp [Function.fixedPoints, Function.IsFixedPt]
  simp only [Representation.character, rho, MonoidHom.coe_mk, OneHom.coe_mk,
    Matrix.trace_toLin'_eq, Matrix.trace_permutation, fixCount,
    Set.ncard_eq_toFinset_card', hset]

/-- `Σ χ² = 72` — the same integer the zero-import layer kernel-checks, now over a genuine
representation. -/
theorem sum_char_sq : ∑ g : Perm (Fin 4), (fixCount g) * (fixCount g) = 72 := by decide

end Cubic

end OIBridge
