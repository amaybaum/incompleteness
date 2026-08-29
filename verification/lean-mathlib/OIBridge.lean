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

-- The lake library's root is this file, so a module the root does not import is never built and
-- never gated. `OIBridge.CombRealization` carries b446's saturated-class lemma and
-- `OIBridge.EquivalenceChain` carries b448's Tier-1 closures from Main §2.3, §3.1 and §3.2,
-- `OIBridge.FiniteEntropy` the finite Shannon layer Mathlib does not have, and
-- `OIBridge.HiddenMemory` the unavoidable-hidden-predictive-memory theorem; none has anything to
-- do with the representation theory below. The imports are here for exactly one reason, and that
-- reason is the gate — `coverage_check.py` enforces it.
import OIBridge.CombRealization
import OIBridge.EquivalenceChain
import OIBridge.FiniteEntropy
import OIBridge.HiddenMemory

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

/-! ## §A10 — the cubic representation, and §A5's first quotient read off it

The counting layer's `72` is an integer sum over a list of signed permutation records. To make
it a *dimension* it must be a sum over a genuine `Representation`, which is what this section
supplies.

The model is the classical one: the rotation group of the cube is `S₄` acting on the four body
diagonals, and the six faces are the six two-element subsets of those diagonals. So `V₆` is the
permutation representation of `Equiv.Perm (Fin 4)` on `{s : Finset (Fin 4) // s.card = 2}`.

Two things make this cheap, and both are already in Mathlib. `Equiv.Perm (Fin 4)` is a group of
order 24 outright, so no subgroup or closure computation is needed. And `Matrix.trace_permutation`
states that the trace of a permutation matrix is its fixed-point count, so the character needs no
new trace theory — it is a finite count, and the sums over the group are decidable.

The identification with the cubic character is **not asserted here**. It is checked in
`representation_bridge_probe.py` (label B4) by comparing the two character multisets element by
element — `χ = 6` once, `2` nine times, `0` fourteen times — with a countercontrol. Note that an
earlier candidate control, the coset action on `S₄/C₄`, was rejected because it has the *same*
character and so discriminates nothing. -/

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
  -- Both obligations are settled at the level of the underlying `Finset`, never at the level
  -- of its elements. Descending further — `ext s x` — unfolds membership through
  -- `Finset.mem_map_equiv` and then into the raw `Multiset`, where the goal is stated in terms
  -- of `Quot.lift` and stops being an inductive datatype `rcases` can take apart. `Subtype.ext`
  -- followed by `Finset.map_refl` / `Finset.map_map` closes both without that descent.
  map_one' := by
    refine Equiv.ext fun s => Subtype.ext ?_
    show s.1.map (Equiv.refl (Fin 4)).toEmbedding = s.1
    rw [Equiv.refl_toEmbedding, Finset.map_refl]
  map_mul' g h := by
    refine Equiv.ext fun s => Subtype.ext ?_
    show s.1.map (g * h).toEmbedding = (s.1.map h.toEmbedding).map g.toEmbedding
    rw [Finset.map_map]
    rfl

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

/-- The faces fixed by `g`, as a `Finset`. Phrased on `g⁻¹` to match `rho`, which carries the
inverse to get the homomorphism direction right; summed over the whole group the distinction is
immaterial, and keeping it here avoids an inverse-juggling step in the character lemma. -/
def fixed (g : Perm (Fin 4)) : Finset Face :=
  Finset.univ.filter fun s => actHom g⁻¹ s = s

/-- The number of faces fixed by `g`. -/
def fixCount (g : Perm (Fin 4)) : ℕ := (fixed g).card

/-- **The character of `V₆` is the fixed-face count.** This is `Matrix.trace_permutation` — the
trace of a permutation matrix is the number of points it fixes — so no new trace theory is
needed.

The one delicate step is the last. `trace_permutation` delivers a `Set.ncard` of a fixed-point
*set*, and routing that through `Set.ncard_eq_toFinset_card'` fails: that lemma selects a
`Fintype` instance which `Set.mem_toFinset` then does not match, leaving the membership goal
stuck. The route taken instead is the one Mathlib's own proof of `trace_permutation` uses —
exhibit the set as a **coerced `Finset`** and finish with `Set.ncard_coe_finset`, which carries
no `Fintype` instance at all, so the mismatch cannot arise. -/
theorem character_eq_fixCount (g : Perm (Fin 4)) :
    rho.character g = (fixCount g : ℚ) := by
  have hset : Function.fixedPoints (actHom g⁻¹) = (fixed g : Set Face) := by
    ext s
    simp [fixed, Function.fixedPoints, Function.IsFixedPt]
  simp only [Representation.character, rho, MonoidHom.coe_mk, OneHom.coe_mk,
    Matrix.trace_toLin'_eq, Matrix.trace_permutation, hset, Set.ncard_coe_finset, fixCount]

/- The two sums below are decided by evaluation over the 24 permutations, each filtering the
six faces. The recursion limit is raised for the same reason as in the core layer: it is a
bound on the evaluator's depth, not a soundness knob, and `native_decide` is deliberately not
used anywhere in this project — it would put the Lean compiler in the trusted base. -/
set_option maxRecDepth 8000 in
/-- `Σ_g χ(g) · χ(g⁻¹) = 72` — the same integer the zero-import layer kernel-checks, now over a
genuine representation. The inverse is carried through the computation rather than removed by a
lemma; that a permutation and its inverse fix the same faces is then a fact the evaluator uses,
not one this file has to state. -/
theorem sum_char_sq : ∑ g : Perm (Fin 4), fixCount g * fixCount g⁻¹ = 72 := by decide

set_option maxRecDepth 8000 in
/-- `Σ_g χ(g) = 24`. `S₄` is transitive on the six faces, so Burnside gives one orbit. -/
theorem sum_char : ∑ g : Perm (Fin 4), fixCount g = 24 := by decide

/-- The group order, in the `Nat.card` spelling the bridge theorems use. -/
theorem card_group : Nat.card (Perm (Fin 4)) = 24 := by
  rw [Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]
  rfl

/- `noncomputable` because `Nat.card` is: it is defined through `Nat.card = Nat.card` on a
possibly-infinite type and carries no executable content. The instance is only ever used to
divide inside `ℚ`, never evaluated, so this costs nothing. -/
noncomputable instance : Invertible ((Nat.card (Perm (Fin 4)) : ℚ)) :=
  invertibleOfNonzero (by rw [card_group]; norm_num)

/-- The character sum of the equivariant-map formula, in `ℚ`. -/
theorem sum_character_sq_rat :
    ∑ g : Perm (Fin 4), rho.character g * rho.character g⁻¹ = (72 : ℚ) := by
  have h : ∀ g : Perm (Fin 4), rho.character g * rho.character g⁻¹
      = ((fixCount g * fixCount g⁻¹ : ℕ) : ℚ) := by
    intro g; rw [character_eq_fixCount, character_eq_fixCount, Nat.cast_mul]
  rw [Finset.sum_congr rfl fun g _ => h g, ← Nat.cast_sum, sum_char_sq]
  norm_num

/-- The character sum of the averaging identity, in `ℚ`. -/
theorem sum_character_rat : ∑ g : Perm (Fin 4), rho.character g = (24 : ℚ) := by
  rw [Finset.sum_congr rfl fun g _ => character_eq_fixCount g, ← Nat.cast_sum, sum_char]
  norm_num

/-! ### §A5, first quotient: `72 / 24 = 3` as a dimension

This is the step the counting layer could not take. `finrank_intertwiners` divides the character
sum by the group order inside a field, and what comes out is a `Module.finrank` — the commutant
of `V₆` really is three-dimensional, not merely the quotient of two integers.

The mirror reaches the same 3 by a route that uses no character theory at all: it solves
`g K = K g` over all 24 elements and takes the null space. Deriving the Lean target from the
averaging identity alone would have been circular, since that identity is exactly what this file
supplies; the direct computation is the independent check, and a proper subgroup gives 12. -/

/-- **§A5.** `dim Hom_G(V₆, V₆) = 3`. The commutant of the cubic action on `V₆` is
three-dimensional — the statement `OI_Structural_Core.lean`'s `kernel_equivariant` needs in
order to say that `K_m` lies in a space of dimension 3, and which no amount of finite
arithmetic could reach. -/
theorem finrank_commutant : Module.finrank ℚ (IntertwiningMap rho rho) = 3 := by
  have h := finrank_intertwiners rho rho
  rw [sum_character_sq_rat, card_group] at h
  have h3 : ((Module.finrank ℚ (IntertwiningMap rho rho) : ℚ)) = 3 := by
    push_cast at h ⊢
    linarith
  exact_mod_cast h3

/-- **§A5.** `dim V₆^G = 1` — the invariant subspace is the constants. -/
theorem finrank_invariants : Module.finrank ℚ (invariants rho) = 1 := by
  have h := card_mul_finrank_invariants rho
  rw [sum_character_rat, card_group] at h
  have h1 : ((Module.finrank ℚ (invariants rho) : ℚ)) = 1 := by
    push_cast at h ⊢
    linarith
  exact_mod_cast h1

/-! ### §A5, second quotient: `288 / 24 = 12` as a dimension

`End(V₆)` needs no construction here. Mathlib's `Representation.linHom` already builds the
conjugation action `K ↦ ρ g ∘ K ∘ ρ g⁻¹`, and `char_linHom` already gives its character as
`χ(g⁻¹) · χ(g)`. So the counting layer's `288` transports exactly the way `72` did, and the
only new content is one decidable sum.

This is where a scope claim made when A10 landed has to be corrected. It said both remaining
quotients were "mechanical given the pattern A10 establishes". That is true of `End(V₆)` and
**not** of the broken 22-dimensional sector — see the note at the end of this section. -/

/-- The conjugation action on `End(V₆)`, 36-dimensional. -/
noncomputable def rhoEnd : Representation ℚ (Perm (Fin 4)) ((Face → ℚ) →ₗ[ℚ] (Face → ℚ)) :=
  rho.linHom rho

set_option maxRecDepth 8000 in
/-- `Σ_g χ_End(g) · χ(g⁻¹) = 288`, written with the inverses in exactly the shape
`finrank_intertwiners` produces so that the evaluator, not a lemma, supplies
`χ(g⁻¹) = χ(g)`. -/
theorem sum_char_end :
    ∑ g : Perm (Fin 4), fixCount g⁻¹ * fixCount g * fixCount g⁻¹ = 288 := by decide

/-- The same sum in `ℚ`, with the character of `End(V₆)` expanded by `char_linHom`. -/
theorem sum_character_end_rat :
    ∑ g : Perm (Fin 4), rhoEnd.character g * rho.character g⁻¹ = (288 : ℚ) := by
  have h : ∀ g : Perm (Fin 4), rhoEnd.character g * rho.character g⁻¹
      = ((fixCount g⁻¹ * fixCount g * fixCount g⁻¹ : ℕ) : ℚ) := by
    -- Two rewrites, not three: `rw` instantiates on the first match and then rewrites every
    -- occurrence of *that* instance, so the first pass takes both `χ(g⁻¹)` factors together.
    intro g
    rw [rhoEnd, Representation.char_linHom, character_eq_fixCount, character_eq_fixCount]
    push_cast
    ring
  rw [Finset.sum_congr rfl fun g _ => h g, ← Nat.cast_sum, sum_char_end]
  norm_num

/-- **§A5.** `dim Hom_G(V₆, End V₆) = 12`. The mirror reaches the same 12 without any character
theory, by an exact `GF(p)` rank on the 216-unknown intertwiner system; imposing equivariance
for a single generator instead of the whole group leaves 112, so the number is cut out by the
cubic symmetry and is not an artifact of the construction. -/
theorem finrank_hom_end : Module.finrank ℚ (IntertwiningMap rho rhoEnd) = 12 := by
  have h := finrank_intertwiners rho rhoEnd
  rw [sum_character_end_rat, card_group] at h
  have h12 : ((Module.finrank ℚ (IntertwiningMap rho rhoEnd) : ℚ)) = 12 := by
    push_cast at h ⊢
    linarith
  exact_mod_cast h12

/-! ### §B1 — the corollary the structural core could not state

`OI_Structural_Core.lean`'s `kernel_equivariant` says `K_m` commutes with every `R_g`, in an
abstract ring and with no notion of dimension available. What the manuscript wants next is that
`K_m` therefore lies in a space of dimension `72 / 24 = 3`. That sentence cannot be written in
the zero-import layer at all, and it is why it lives here.

The hypothesis is written in **composition form**, `K ∘ₗ ρ g = ρ g ∘ₗ K`, for two reasons. It is
*definitionally* the `isIntertwining'` field, so the bundling is a structure literal with no
constructor call and no argument-order to get wrong. And it is the closer reading of
`MZ.kernel_equivariant`, which is an operator identity in a ring rather than a pointwise
statement about vectors. This formulation comes from the parallel thread's b423 candidate and is
better than the pointwise one this file carried first. -/

/-- Bundle a cubic-equivariant linear kernel as an intertwining endomorphism. The hypothesis is
the concrete linear-map reading of `MZ.kernel_equivariant`. -/
def kernelIntertwiner (K : (Face → ℚ) →ₗ[ℚ] (Face → ℚ))
    (hK : ∀ g : Perm (Fin 4), K ∘ₗ rho g = rho g ∘ₗ K) : IntertwiningMap rho rho where
  toLinearMap := K
  isIntertwining' := hK

@[simp] theorem kernelIntertwiner_toLinearMap (K : (Face → ℚ) →ₗ[ℚ] (Face → ℚ))
    (hK : ∀ g : Perm (Fin 4), K ∘ₗ rho g = rho g ∘ₗ K) :
    (kernelIntertwiner K hK).toLinearMap = K := rfl

/-- **§B1.** Every memory kernel satisfying the cubic equivariance equation lies in a *fixed*
three-dimensional operator space. This is the Mathlib-side join to the zero-import theorem
`MZ.kernel_equivariant`; no numerical hypothesis is added here, and no new count — the dimension
is `finrank_commutant`, already proved above.

Stated this way rather than as bare membership because the physical content is the confinement,
not the classification: the cubic symmetry does not merely reduce the parameter count, it pins
every admissible kernel into one three-dimensional space. -/
theorem equivariant_kernel_lives_in_finrank_three (K : (Face → ℚ) →ₗ[ℚ] (Face → ℚ))
    (hK : ∀ g : Perm (Fin 4), K ∘ₗ rho g = rho g ∘ₗ K) :
    ∃ Kρ : IntertwiningMap rho rho,
      Kρ.toLinearMap = K ∧ Module.finrank ℚ (IntertwiningMap rho rho) = 3 :=
  ⟨kernelIntertwiner K hK, rfl, finrank_commutant⟩

/-! ### §A5-B22 — open, and *not* the same kind of step

The remaining quotient, `144 / 24 = 6`, is `dim Hom_G(V₆, B₂₂)`, and `B₂₂` has no object in this
file to be the target of. It has to be built first, and that is a construction rather than
plumbing — which is the correction to the earlier "both are mechanical" claim.

What makes the target canonical is an intrinsic split found in the mirror. Every face has an
opposite face (its set-theoretic complement), so the six faces form three complement pairs, and
that gives an `S₄`-invariant decomposition

    V₆ = T₃ ⊕ E₂ ⊕ A₁

into functions odd under complementation (3), even functions whose three pair-values sum to
zero (2), and constants (1). The broken sector is then exactly the off-diagonal part of
`End(V₆)`:

    B₂₂ = Hom(E,T) ⊕ Hom(T,E) ⊕ Hom(A,T) ⊕ Hom(T,A) ⊕ Hom(A,E) ⊕ Hom(E,A)

of dimension `6+6+3+3+2+2 = 22`, with character `2(χ_T χ_E + χ_T χ_A + χ_E χ_A)` — which is
precisely the zero-import layer's `chiBrk`. The Mathlib pieces for it all exist
(`Subrepresentation.toRepresentation`, `linHom`, and representation products), so the route is
clear; the work is in describing the three submodules to Lean without friction, and it is a
round of its own. The mirror already certifies the answer: an exact rank on the 132-unknown
system gives 6, with a one-generator control at 68. -/

end Cubic

end OIBridge
