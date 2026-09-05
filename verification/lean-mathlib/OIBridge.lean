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
import OIBridge.Averaging
import Mathlib.RepresentationTheory.Invariants
import Mathlib.RepresentationTheory.Character
import Mathlib.RepresentationTheory.Subrepresentation
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.GroupTheory.Perm.Fin

-- The lake library's root is this file, so a module the root does not import is never built and
-- never gated. `OIBridge.CombRealization` carries b446's saturated-class lemma and
-- `OIBridge.EquivalenceChain` carries b448's Tier-1 closures from Main §2.3, §3.1 and §3.2,
-- `OIBridge.FiniteEntropy` the finite Shannon layer Mathlib does not have,
-- `OIBridge.HiddenMemory` the unavoidable-hidden-predictive-memory theorem,
-- `OIBridge.Equivalence` the finite-horizon stochastic/reversible/unitary equivalence,
-- `OIBridge.C3Necessity` the C3 capacity theorem, `OIBridge.CanonicalMeasure` Lemma 3's
-- selected measure, `OIBridge.Finiteness` Lemma 1's conditional finiteness, and `OIBridge.CubicIsotropy`
-- [SM] Corollary 1a, and `OIBridge.IdempotentTrace` the trace-of-restriction lemma
-- Theorem 7 was blocked on, `OIBridge.FactorUniqueness` the factor-uniqueness lemma
-- [Structure] Proposition 9.7a was blocked on and `OIBridge.KrausUniqueness` that
-- proposition itself and `OIBridge.StinespringUniqueness` its dilation counterpart 9.7b,
-- `OIBridge.WeylTwirl` the symplectic layer of [Main]'s separability threshold and
-- `OIBridge.Separability` its entanglement layer and `OIBridge.WeylLift` the
-- multiplicative lift and the character projectors that carry both its directions,
-- `OIBridge.BoundaryRank` [Main] Lemma 1, `OIBridge.Reciprocity` [SM] Theorem 19, `OIBridge.GaugeDimension` [SM] Theorem 16,
-- `OIBridge.BohrFrequency` [GR]'s Bohr-frequency completeness,
-- `OIBridge.TasteBranching` [SM] Theorem 8,
-- `OIBridge.Irreducibility` the implication from the
-- endomorphism dimension to irreducibility that Mathlib carries only for algebraically
-- closed fields, `OIBridge.LinkDecomposition` that theorem's six-link
-- decomposition and `OIBridge.QuarterTurn` the cubic rotation group it decomposes under;
-- none has anything
-- to do with the representation theory below. The imports are here for exactly one reason, and
-- that reason is the gate — `coverage_check.py` enforces it.
import OIBridge.CombRealization
import OIBridge.EquivalenceChain
import OIBridge.FiniteEntropy
import OIBridge.HiddenMemory
import OIBridge.Equivalence
import OIBridge.C3Necessity
import OIBridge.CanonicalMeasure
import OIBridge.Finiteness
import OIBridge.CubicIsotropy
import OIBridge.FactorUniqueness
import OIBridge.IdempotentTrace
import OIBridge.Irreducibility
import OIBridge.KrausUniqueness
import OIBridge.StinespringUniqueness
import OIBridge.Separability
import OIBridge.WeylTwirl
import OIBridge.WeylLift
import OIBridge.BoundaryRank
import OIBridge.Reciprocity
import OIBridge.GaugeDimension
import OIBridge.BohrFrequency
import OIBridge.FrequencyMatching
import OIBridge.PiccardBridge
import OIBridge.TasteBranching
import OIBridge.EdgeRigidity
import OIBridge.HomometricSix
import OIBridge.HomometricKill
import OIBridge.CongruentReconstruction
import OIBridge.TurnpikeScopeTransfer
import OIBridge.AntiunitaryInvariance
import OIBridge.ThermalOrientation
import OIBridge.ShellAssignment
import OIBridge.CoherentLift
import OIBridge.TwoByTwoNoGo
import OIBridge.AccessibleAlgebra
import OIBridge.OperationalRigidity
import OIBridge.JordanClassification
import OIBridge.OrientationSelection
import OIBridge.OrientationClosure
import OIBridge.CycleFibreHull
import OIBridge.DynamicsGlue
import OIBridge.DomainGlue
import OIBridge.ObservabilityQuotient
import OIBridge.PassiveQuotient
import OIBridge.ControlledQuotient
import OIBridge.CoherentExtension
import OIBridge.ProjectiveAction
import OIBridge.ControlLie
import OIBridge.InstrumentDilation
import OIBridge.Purification
import OIBridge.BranchSelector
import OIBridge.IndependenceCensus
import OIBridge.MonoidalCompletion
import OIBridge.OperationalAssembly
import OIBridge.StinespringAssembly
import OIBridge.KrausSoundness
import OIBridge.CompositeSoundness
import OIBridge.HiddenCoherence
import OIBridge.AncillaInterference
import OIBridge.PartialTranspose
import OIBridge.FactorExchange
import OIBridge.DimensionalObstruction
import OIBridge.DimensionalCountermodel
import OIBridge.BoundaryAudit
import OIBridge.ReferenceExtension
import OIBridge.ReferenceSufficiency
import OIBridge.SpectatorBridge
import OIBridge.AncillaClosure
import OIBridge.ClosureObstruction
import OIBridge.CompositionalIndependence
import OIBridge.OIRealization
import OIBridge.OperationalValidity
import OIBridge.LevelOneSeam
import OIBridge.PhysicalCharacterization
import OIBridge.DiagonalTheory
import OIBridge.RankGapTheory
import OIBridge.IsometryExtension
import OIBridge.GeneralCarrier
import OIBridge.UhlmannUniqueness
import OIBridge.ReachabilitySeam
import OIBridge.OrbitReachability
import OIBridge.SubstantiveCensus
import OIBridge.CompletedOI
import OIBridge.CarrierGeneralOIPlus
import OIBridge.EmbeddedObservation
import OIBridge.ImplementationLocality
import OIBridge.MicroscopicReversibility
import OIBridge.LieRankSource
import OIBridge.SubstratumSource
import OIBridge.SubstratumInterface
import OIBridge.ReadWriteControl
import OIBridge.StructuralClosure
import OIBridge.TypedCompletion
import OIBridge.RegionLimit
import OIBridge.RegionTower
import OIBridge.QuasilocalAlgebra
import OIBridge.QuasilocalCharacterization
import OIBridge.InstrumentCompletion
import OIBridge.InstrumentAvailability
import OIBridge.SecondOrderCircuit
import OIBridge.SecondOrderLayer
import OIBridge.SwapLayer
import OIBridge.SecondOrderDrive
import OIBridge.LinkDecomposition
import OIBridge.QuarterTurn
import OIBridge.PassiveObservation
import OIBridge.CentralObservation
import OIBridge.PassiveIndependence
import OIBridge.InternalObserver
import OIBridge.LevelOneRecursion
import OIBridge.PositiveReachability
import OIBridge.TypedPositive
import OIBridge.MinimalRepertoire

namespace OIBridge

open LinearMap Representation

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
    simp [Function.comp]
  map_mul' g h := by
    ext v x
    simp [Function.comp, mul_inv_rev, map_mul]

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

/-! ## The two-subset model is NOT the six-link representation

**A defect in this section, found by formalizing [SM] Theorem 7, and recorded here rather than
repaired in passing.**

`Cubic.rho` is the permutation representation of `S₄` on the six two-element subsets of the four
body diagonals, and its header describes those as "the six faces of the cube". They are not. A face
of the cube contains one endpoint of every body diagonal, so it determines no two-element subset of
them; the six two-element subsets are the six pairs of opposite EDGES.

The consequence is exactly the failure mode a multiplicity count cannot see. Both representations
have character multiset `{6, 2×9, 0×14}`, so comparing multisets — which is what
`representation_bridge_probe.py` did, and all that the "identification is checked in the probe"
note ever claimed — cannot tell them apart. As CLASS FUNCTIONS they differ:

    class            E   8C₃  3C₂  6C₂'  6C₄
    two-subsets      6    0    2    2     0     =  A₁ ⊕ E ⊕ T₂
    six links        6    0    2    0     2     =  A₁ ⊕ E ⊕ T₁   ([SM] Theorem 7's proof line)

so `Cubic.rho` carries `T₂` where the six links carry `T₁` — the two three-dimensional irreducibles,
swapped. `char_two_subset_ne_link` below states the discrepancy as a theorem so it cannot be
mislaid again.

The six links are instead the coset space `S₄/C₄`: the stabilizer of `+e₃` in the rotation group is
the four-fold rotation about that axis. This section's own note records the coset action as an
"earlier candidate control, rejected because it has the same character and so discriminates
nothing" — the same multiset collision, read the wrong way round. It is the correct model, and
`OIBridge/QuarterTurn.lean` now builds it: `S₄` acting by conjugation on its six four-cycles, whose
fixed-link character `character_gate` computes to be exactly `(6, 0, 2, 0, 2)`.

WHAT FOLLOWS IS THEREFORE NOT THE ROTATION ACTION ON THE COORDINATE LINKS. `faceEquivLink` is a
complement-preserving bijection of six-element sets and `linkHom` is a faithful action of `S₄` by
symmetries of the link set — both true as stated — but the action it transports is the two-subset
one, so it realizes `T₂` and not `T₁`. It is kept because it is correct as stated and because the
padding lemmas around it are reusable; it does NOT close the A10 face/link debt, and nothing here
should be read as the six-link representation of [SM] Theorem 7. -/

namespace LinkJoin

open Equiv OIBridge.LinkDecomposition

/-- The face opposite to a given one. -/
def op (F : Cubic.Face) : Cubic.Face :=
  ⟨F.1ᶜ, by rw [Finset.card_compl, F.2]; rfl⟩

/-- The six faces as the six links: outward normals, with opposite faces antipodal. -/
def faceToLink (F : Cubic.Face) : Link :=
  if 0 ∈ F.1 then
    (if 1 ∈ F.1 then (0, false) else if 2 ∈ F.1 then (1, false) else (2, false))
  else
    (if 1 ∈ F.1 then (if 2 ∈ F.1 then (2, true) else (1, true)) else (0, true))

/-- Its inverse, given explicitly so the equivalence stays computable and `decide` can run. -/
def linkToFace (l : Link) : Cubic.Face :=
  if l.1 = 0 then (if l.2 then ⟨{2, 3}, by decide⟩ else ⟨{0, 1}, by decide⟩)
  else if l.1 = 1 then (if l.2 then ⟨{1, 3}, by decide⟩ else ⟨{0, 2}, by decide⟩)
  else (if l.2 then ⟨{1, 2}, by decide⟩ else ⟨{0, 3}, by decide⟩)

/-- **The six faces are the six links.** -/
def faceEquivLink : Cubic.Face ≃ Link :=
  ⟨faceToLink, linkToFace, by decide, by decide⟩

/-- **The equivalence is complement-preserving**: opposite faces are antipodal links. This is the
property the whole join turns on. -/
theorem faceEquivLink_op (F : Cubic.Face) : faceEquivLink (op F) = anti (faceEquivLink F) := by
  revert F; decide

/-- The face action commutes with taking the opposite face, because a bijection of the four
diagonals commutes with complementation. -/
theorem act_op (g : Perm (Fin 4)) (F : Cubic.Face) :
    Cubic.act g (op F) = op (Cubic.act g F) := by
  refine Subtype.ext ?_
  show (F.1ᶜ).map g.toEmbedding = (F.1.map g.toEmbedding)ᶜ
  ext x
  simp only [Finset.mem_map, Finset.mem_compl, Equiv.coe_toEmbedding]
  constructor
  · rintro ⟨a, ha, rfl⟩ hc
    obtain ⟨b, hb, hbx⟩ := hc
    exact ha (by rwa [← g.injective hbx])
  · intro hx
    refine ⟨g.symm x, fun hc => hx ⟨g.symm x, hc, by simp⟩, by simp⟩

/-- The two-subset action, transported to the link set. A faithful action of `S₄` of order 24 by
symmetries of the link set — but the TWO-SUBSET one, realizing `T₂`, not the rotation action on the
coordinate links. See the section header. -/
def linkHom : Perm (Fin 4) →* Perm Link where
  toFun g := (faceEquivLink.symm.trans (Cubic.actHom g)).trans faceEquivLink
  map_one' := by
    refine Equiv.ext fun l => ?_
    simp [map_one]
  map_mul' g h := by
    refine Equiv.ext fun l => ?_
    simp [map_mul, Equiv.Perm.mul_apply]

theorem linkHom_apply (g : Perm (Fin 4)) (l : Link) :
    linkHom g l = faceEquivLink (Cubic.act g (faceEquivLink.symm l)) := rfl

/-- **Every rotation is a symmetry of the link set.** Complement-preservation of the bijection plus
`act_op` gives it directly, with no enumeration over the group. This is what makes
`LinkDecomposition`'s three projectors invariant under the genuine `S₄` action. -/
theorem sym_linkHom (g : Perm (Fin 4)) : Sym (linkHom g) := by
  intro l
  have hl : faceEquivLink.symm (anti l) = op (faceEquivLink.symm l) := by
    refine faceEquivLink.injective ?_
    rw [Equiv.apply_symm_apply, faceEquivLink_op, Equiv.apply_symm_apply]
  rw [linkHom_apply, linkHom_apply, hl, act_op, faceEquivLink_op]

/- The face action of `S₄` is faithful, decided over the 576 pairs. The recursion limit is raised
for the same reason as elsewhere in this file: it bounds the evaluator's depth, not the trusted
base, and `native_decide` is deliberately never used in this project. -/
set_option maxRecDepth 40000 in
theorem act_injective : Function.Injective Cubic.act := by decide

/-- The action is faithful, so its image really is a 24-element group of link symmetries. -/
theorem linkHom_injective : Function.Injective linkHom := by
  intro g h hgh
  refine act_injective (Equiv.ext fun F => faceEquivLink.injective ?_)
  have := congrArg (fun σ => σ (faceEquivLink F)) hgh
  simpa [linkHom_apply, Equiv.symm_apply_apply] using this

/-! ### The transported representation

`permOp` acts by precomposition and so reverses composition order (`LinkDecomposition.permOp_mul`),
so the representation carries the INVERSE. That orientation is explicit rather than implicit: every
character here satisfies `χ(g⁻¹) = χ(g)`, so every numeric consequence would come out right even
with the orientation wrong, and only a pointwise statement would notice.

This is the two-subset representation read on the link set, `A₁ ⊕ E ⊕ T₂`. The decomposition
machinery below applies to it verbatim — the projectors do not know which action they commute with
— but the three-dimensional summand here is `T₂`. -/

/-- The transported representation. NOT [SM] Theorem 7's `V₆`; see the section header. -/
noncomputable def rhoLink : Representation ℚ (Perm (Fin 4)) LV where
  toFun g := permOp (linkHom g⁻¹)
  map_one' := by rw [inv_one, map_one, permOp_one]; rfl
  map_mul' g h := by
    rw [mul_inv_rev, map_mul, permOp_mul]
    rfl

theorem rhoLink_apply (g : Perm (Fin 4)) : rhoLink g = permOp (linkHom g⁻¹) := rfl

/-- Its character is the fixed-link count, through `trace_permOp`. -/
theorem character_rhoLink (g : Perm (Fin 4)) :
    rhoLink.character g
      = ((Finset.univ.filter fun l => linkHom g⁻¹ l = l).card : ℚ) := by
  rw [Representation.character, rhoLink_apply, trace_permOp]

/-- The three projectors commute with the representation, so all three images are
SUBREPRESENTATIONS and not merely invariant subspaces of a monoid action. -/
theorem rhoLink_comm_PT (g : Perm (Fin 4)) : rhoLink g ∘ₗ PT = PT ∘ₗ rhoLink g :=
  permOp_comp_PT (sym_linkHom g⁻¹)

theorem rhoLink_comm_PE (g : Perm (Fin 4)) : rhoLink g ∘ₗ PE = PE ∘ₗ rhoLink g :=
  permOp_comp_PE (sym_linkHom g⁻¹)

theorem rhoLink_comm_PA (g : Perm (Fin 4)) : rhoLink g ∘ₗ PA = PA ∘ₗ rhoLink g :=
  permOp_comp_PA (linkHom g⁻¹)

/-- **The character of a summand is the restricted trace**, through
`IdempotentTrace.trace_restrict_range`. This is the join between the infrastructure lemma and the
representation: the left side is a genuine character of a subrepresentation, the right side is
computable from fixed-point counts by `charOn_PT` and `charOn_PA`. -/
theorem character_restrict_PT (g : Perm (Fin 4)) :
    LinearMap.trace ℚ (LinearMap.range PT)
        ((rhoLink g).restrict (IdempotentTrace.mapsTo_range (rhoLink_comm_PT g)))
      = charOn PT (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PT_idem (rhoLink_comm_PT g)

theorem character_restrict_PE (g : Perm (Fin 4)) :
    LinearMap.trace ℚ (LinearMap.range PE)
        ((rhoLink g).restrict (IdempotentTrace.mapsTo_range (rhoLink_comm_PE g)))
      = charOn PE (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PE_idem (rhoLink_comm_PE g)

theorem character_restrict_PA (g : Perm (Fin 4)) :
    LinearMap.trace ℚ (LinearMap.range PA)
        ((rhoLink g).restrict (IdempotentTrace.mapsTo_range (rhoLink_comm_PA g)))
      = charOn PA (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PA_comp_PA (rhoLink_comm_PA g)

/-- The one-dimensional summand is the TRIVIAL representation `A₁`: its character is constantly
one, at every rotation. -/
theorem character_PA_eq_one (g : Perm (Fin 4)) :
    LinearMap.trace ℚ (LinearMap.range PA)
        ((rhoLink g).restrict (IdempotentTrace.mapsTo_range (rhoLink_comm_PA g))) = 1 := by
  rw [character_restrict_PA, charOn_PA]

/-- The three characters sum to the character of `V₆`, at every rotation. -/
theorem character_sum (g : Perm (Fin 4)) :
    charOn PT (linkHom g⁻¹) + charOn PE (linkHom g⁻¹) + charOn PA (linkHom g⁻¹)
      = rhoLink.character g := by
  rw [Representation.character, rhoLink_apply, charOn_sum]

/-! ### The three summands as honest subrepresentations

Up to here the three images were invariant submodules and the "characters" were restricted traces.
Mathlib's `Subrepresentation` bundles the submodule with its invariance and `toRepresentation`
turns it into a genuine `Representation` whose action is exactly that restricted map — so the join
theorems below are statements about `Representation.character`, not about a trace that resembles
one. This also makes `finrank_intertwiners` applicable to the summands directly, which is what the
irreducibility step needs. -/

/-- The three-dimensional summand, as a subrepresentation. -/
noncomputable def Tsub : Subrepresentation rhoLink where
  toSubmodule := LinearMap.range PT
  apply_mem_toSubmodule g _ hv := IdempotentTrace.mapsTo_range (rhoLink_comm_PT g) _ hv

/-- The two-dimensional summand. -/
noncomputable def Esub : Subrepresentation rhoLink where
  toSubmodule := LinearMap.range PE
  apply_mem_toSubmodule g _ hv := IdempotentTrace.mapsTo_range (rhoLink_comm_PE g) _ hv

/-- The one-dimensional summand. -/
noncomputable def Asub : Subrepresentation rhoLink where
  toSubmodule := LinearMap.range PA
  apply_mem_toSubmodule g _ hv := IdempotentTrace.mapsTo_range (rhoLink_comm_PA g) _ hv

noncomputable def rhoT : Representation ℚ (Perm (Fin 4)) Tsub.toSubmodule := Tsub.toRepresentation
noncomputable def rhoE : Representation ℚ (Perm (Fin 4)) Esub.toSubmodule := Esub.toRepresentation
noncomputable def rhoA : Representation ℚ (Perm (Fin 4)) Asub.toSubmodule := Asub.toRepresentation

/-- **The join, at the level of characters of representations.** Each summand's character is
`charOn`, which `charOn_PT` and `charOn_PA` compute from fixed-point counts. The bridge from the
left side to the right is `IdempotentTrace.trace_restrict_range`. -/
theorem character_rhoT (g : Perm (Fin 4)) : rhoT.character g = charOn PT (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PT_idem (rhoLink_comm_PT g)

theorem character_rhoE (g : Perm (Fin 4)) : rhoE.character g = charOn PE (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PE_idem (rhoLink_comm_PE g)

theorem character_rhoA (g : Perm (Fin 4)) : rhoA.character g = charOn PA (linkHom g⁻¹) :=
  IdempotentTrace.trace_restrict_range PA_comp_PA (rhoLink_comm_PA g)

/-- **The one-dimensional summand is the trivial representation `A₁`**, now as a statement about a
representation's character rather than a restricted trace. -/
theorem character_rhoA_eq_one (g : Perm (Fin 4)) : rhoA.character g = 1 := by
  rw [character_rhoA, charOn_PA]

/-- The three characters decompose the character of `V₆`. -/
theorem character_rhoLink_eq_sum (g : Perm (Fin 4)) :
    rhoLink.character g = rhoT.character g + rhoE.character g + rhoA.character g := by
  rw [character_rhoT, character_rhoE, character_rhoA, character_sum]

/-! ### The discrepancy, as a theorem

Stated so it cannot be mislaid again: the two-subset character and the six-link character of [SM]
Theorem 7's proof line agree in multiset and differ as class functions, at the transpositions and
the four-fold rotations. -/

/-- Fixed two-element subsets of the four diagonals: the character of `Cubic.rho`, and of the
action transported to the links. -/
def fixTwoSub (g : Perm (Fin 4)) : ℕ := (Finset.univ.filter fun l => linkHom g l = l).card

/-- **The character of `V₆`**: `6` at the identity, `0` on `8C₃`, `2` on `3C₂`, `0` on `6C₂'`, `2`
on `6C₄`, which is [SM] Theorem 7's own proof line.

No longer a transcription. `OIBridge.QuarterTurn.character_gate` proves it is the fixed-link
character of the cubic rotation action, built there from conjugation on the six quarter turns. -/
abbrev chiLinkTable : Perm (Fin 4) → ℤ := QuarterTurn.chiLink

set_option maxRecDepth 40000 in
/-- **`Cubic.rho` is not the six-link representation.** The transposition `(0 1)` is a `6C₂'`
rotation, where the manuscript's character is `0` and the two-subset character is `2`; the
four-fold class is the mirror image. -/
theorem char_two_subset_ne_link :
    ∃ g : Perm (Fin 4), (fixTwoSub g : ℤ) ≠ chiLinkTable g := by
  refine ⟨Equiv.swap 0 1, ?_⟩
  decide

/-! ### Why the previous evidence could not have caught this

Three permanent regression controls. The two characters agree as MULTISETS, and they agree on the
aggregate power sums this bridge reports — so neither the old multiset comparison nor the character
sums `72` and `288` could ever have distinguished them. The two classes where they differ, `6C₂'`
and `6C₄`, both have six elements, so the contributions simply trade places. -/

set_option maxRecDepth 100000 in
/-- The two characters take the same values with the same multiplicities. This is exactly what
`representation_bridge_probe.py` compared, and it is why that comparison was silent. -/
theorem char_multiset_collision :
    (Finset.univ.val.map fun g : Perm (Fin 4) => (fixTwoSub g : ℤ))
      = (Finset.univ.val.map fun g : Perm (Fin 4) => chiLinkTable g) := by decide

set_option maxRecDepth 100000 in
/-- The `Σχ² = 72` certificate cannot distinguish them either. -/
theorem sum_sq_collision :
    (∑ g : Perm (Fin 4), (fixTwoSub g : ℤ) ^ 2) = 72 ∧
      (∑ g : Perm (Fin 4), chiLinkTable g ^ 2) = 72 := by
  refine ⟨by decide, by decide⟩

set_option maxRecDepth 100000 in
/-- Nor can `Σχ³ = 288`. -/
theorem sum_cube_collision :
    (∑ g : Perm (Fin 4), (fixTwoSub g : ℤ) ^ 3) = 288 ∧
      (∑ g : Perm (Fin 4), chiLinkTable g ^ 3) = 288 := by
  refine ⟨by decide, by decide⟩

/-! ### What these proofs rest on -/

#print axioms LinkJoin.char_two_subset_ne_link
#print axioms LinkJoin.char_multiset_collision
#print axioms LinkJoin.sum_sq_collision
#print axioms LinkJoin.sum_cube_collision
#print axioms LinkJoin.faceEquivLink_op
#print axioms LinkJoin.act_op
#print axioms LinkJoin.sym_linkHom
#print axioms LinkJoin.act_injective
#print axioms LinkJoin.linkHom_injective
#print axioms LinkJoin.character_rhoLink
#print axioms LinkJoin.rhoLink_comm_PT
#print axioms LinkJoin.character_restrict_PT
#print axioms LinkJoin.character_PA_eq_one
#print axioms LinkJoin.character_sum
#print axioms LinkJoin.character_rhoT
#print axioms LinkJoin.character_rhoE
#print axioms LinkJoin.character_rhoA
#print axioms LinkJoin.character_rhoA_eq_one
#print axioms LinkJoin.character_rhoLink_eq_sum

end LinkJoin


end OIBridge
