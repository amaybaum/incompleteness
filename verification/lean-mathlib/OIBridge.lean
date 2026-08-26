/-
  OIBridge.lean — ROADMAP §A1, the averaging identity.

  This is the ONE classical bridge the zero-import layer defers. `OI_Gauge_Certificates.lean`
  kernel-checks the character sums 72 / 288 / 144 over the 24-element cubic rotation group,
  and `OI_Regulator_Symmetry.lean` the sums 384 / 192 over the hypercubic and native groups,
  but neither can divide by the group order to obtain a *dimension*: that step is the
  classical identity

      |G| · dim (fixed subspace)  =  Σ_g χ(g)

  which needs a field, a module, and the trace of a projection — finite-dimensional linear
  algebra, not finite arithmetic. Hence this file, and hence its separate directory: it is
  the only part of the verification layer that depends on Mathlib. The four core proof files
  remain self-contained with zero imports, and are checked by their own gate.

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

/-- The averaging projector is the group average of the representation. -/
theorem averageMap_eq (ρ : Representation k G V) :
    ρ.averageMap = ⅟(Fintype.card G : k) • ∑ g : G, ρ g := by
  simp [Representation.averageMap, GroupAlgebra.average, map_smul, map_sum]

/-- **§A1 — the averaging identity.** For a finite group acting on a finite-dimensional
space over a field in which `|G|` is invertible, the order of the group times the dimension
of the invariant subspace equals the sum of the character over the group.

This is what turns the kernel-checked sums of the core layer into dimensions:
`72 = 24 · 3`, `288 = 24 · 12`, `144 = 24 · 6`, and `384 = 384 · 1` against `192 = 96 · 2`. -/
theorem card_mul_finrank_invariants (ρ : Representation k G V) :
    (Fintype.card G : k) * (Module.finrank k (invariants ρ) : k) = ∑ g : G, ρ.character g := by
  have hproj : trace k V ρ.averageMap = (Module.finrank k (invariants ρ) : k) :=
    (isProj_averageMap ρ).trace
  have htr : trace k V ρ.averageMap = ⅟(Fintype.card G : k) * ∑ g : G, ρ.character g := by
    rw [averageMap_eq ρ, map_smul, map_sum]
    simp [Representation.character, smul_eq_mul]
  rw [← hproj, htr, ← mul_assoc, mul_invOf_self, one_mul]

/-- The identity in the form the counting layer uses it: the dimension is the character sum
divided by the group order. -/
theorem finrank_invariants (ρ : Representation k G V) :
    (Module.finrank k (invariants ρ) : k)
      = ⅟(Fintype.card G : k) * ∑ g : G, ρ.character g := by
  rw [← card_mul_finrank_invariants ρ, ← mul_assoc, invOf_mul_self, one_mul]

end OIBridge
