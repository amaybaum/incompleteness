/-
  OIBridge/Irreducibility.lean — irreducibility from the endomorphism dimension, over a field that
  is NOT algebraically closed.

      ρ semisimple, ρ ≠ 0, dim_k End_G(ρ) = 1  ⟹  ρ irreducible.

  WHY THIS FILE EXISTS SEPARATELY. Mathlib has the converse — `IsIrreducible.
  finrank_intertwiningMap_self` gives `dim End = 1` from irreducibility — but it carries
  `[IsAlgClosed k]`, which is exactly the hypothesis this corpus must not use: [SM] Theorem 7's
  three summands are irreducible over ℚ, and over ℚ Schur's lemma gives only a division algebra,
  not the base field. The direction needed here is the other one, and it does not need the field
  closed at all: it needs Maschke, which is available over ℚ because 24 is invertible there.

  WHAT WAS MISSING, precisely. `dim_k End_G(ρ) = 1` is not on its own a statement about
  subrepresentations; the implication to irreducibility is where Maschke enters, and until this
  file that implication was prose. `Averaging.finrank_intertwiners` supplies the dimension and
  nothing more.

  THE PROOF. Maschke gives every subrepresentation `σ` an invariant complement `τ`. The projection
  onto `σ` along `τ` is then equivariant — it is `ρ g`-natural because both summands are invariant —
  so it is an element of `End_G(ρ)`. With `dim = 1` and `1 ≠ 0`, that endomorphism is `c • 1` for a
  single scalar `c`. It is the identity on `σ` and zero on `τ`, so a nonzero vector in `σ` forces
  `c = 1` and a nonzero vector in `τ` forces `c = 0`. They cannot both exist: one of the two
  summands is zero, which is to say `σ` is `⊥` or `⊤`.

  Idempotence is never used. The two evaluations are enough, which keeps the argument free of the
  projector algebra and applicable to any semisimple representation.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.RepresentationTheory.Maschke
import Mathlib.RepresentationTheory.Irreducible
import Mathlib.RepresentationTheory.Semisimple
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

namespace OIBridge

namespace Irreducibility

open Representation

/- Two of the statements below are pure lattice or linear algebra and do not use the finiteness of
the group or the invertibility of its order. Keeping them under the same section variables is
deliberate — they exist only to serve the theorem that does need both — so the unused-variable
linter is silenced rather than the file split. -/
set_option linter.unusedSectionVars false

variable {k G V : Type*} [Field k] [Group G] [Finite G]
  [AddCommGroup V] [Module k V] [NeZero (Nat.card G : k)]

/-! ### Maschke, instantiated

Mathlib proves Maschke's theorem as a statement about `k[G]`-modules and supplies the transfer to
subrepresentations. Neither is restated here; what follows only names the composite, because the
implication below is the thing that was missing and the semisimplicity is not. -/

/-- **Maschke for representations.** Every subrepresentation has an invariant complement, whenever
the group order is nonzero in the field. This is Mathlib's `IsSemisimpleModule` instance for
`k[G]`-modules, carried across `isSemisimpleRepresentation_iff_isSemisimpleModule_asModule`. -/
theorem complementedLattice (ρ : Representation k G V) :
    ComplementedLattice (Subrepresentation ρ) :=
  (isSemisimpleRepresentation_iff_isSemisimpleModule_asModule ρ).2 inferInstance

/-- Complementation of subrepresentations is complementation of the underlying submodules: `⊓`, `⊔`,
`⊥` and `⊤` all commute with `toSubmodule`. -/
theorem isCompl_toSubmodule {ρ : Representation k G V} {σ τ : Subrepresentation ρ}
    (h : IsCompl σ τ) : IsCompl σ.toSubmodule τ.toSubmodule := by
  constructor
  · rw [disjoint_iff]
    exact congrArg Subrepresentation.toSubmodule (disjoint_iff.1 h.disjoint)
  · rw [codisjoint_iff]
    exact congrArg Subrepresentation.toSubmodule (codisjoint_iff.1 h.codisjoint)

/-! ### The projection onto an invariant summand

The projection of a direct-sum decomposition is equivariant as soon as BOTH summands are invariant:
`ρ g` moves the `σ`-part to the `σ`-part and the `τ`-part to the `τ`-part, so it commutes with
"keep the `σ`-part". This is where Maschke's complement is used, and the only place. -/

/-- The linear projection onto `σ` along `τ`. -/
noncomputable def projMap {ρ : Representation k G V} {σ τ : Subrepresentation ρ}
    (h : IsCompl σ τ) : V →ₗ[k] V :=
  σ.toSubmodule.projection τ.toSubmodule (isCompl_toSubmodule h)

theorem projMap_left {ρ : Representation k G V} {σ τ : Subrepresentation ρ} (h : IsCompl σ τ)
    {x : V} (hx : x ∈ σ.toSubmodule) : projMap h x = x :=
  Submodule.projection_apply_of_mem_left (isCompl_toSubmodule h) hx

theorem projMap_right {ρ : Representation k G V} {σ τ : Subrepresentation ρ} (h : IsCompl σ τ)
    {x : V} (hx : x ∈ τ.toSubmodule) : projMap h x = 0 :=
  Submodule.projection_apply_of_mem_right (isCompl_toSubmodule h) hx

theorem projMap_equivariant {ρ : Representation k G V} {σ τ : Subrepresentation ρ}
    (h : IsCompl σ τ) (g : G) (v : V) : projMap h (ρ g v) = ρ g (projMap h v) := by
  obtain ⟨a, ha, b, hb, rfl⟩ : ∃ a ∈ σ.toSubmodule, ∃ b ∈ τ.toSubmodule, a + b = v :=
    Submodule.mem_sup.1 (by rw [(isCompl_toSubmodule h).sup_eq_top]; trivial)
  rw [map_add, map_add, map_add, projMap_left h ha, projMap_right h hb, add_zero,
    projMap_left h (σ.apply_mem_toSubmodule g ha),
    projMap_right h (τ.apply_mem_toSubmodule g hb), add_zero]

/-- The projection, as an element of `End_G(ρ)`. -/
noncomputable def proj {ρ : Representation k G V} {σ τ : Subrepresentation ρ} (h : IsCompl σ τ) :
    IntertwiningMap ρ ρ :=
  (projMap h).intertwiningMap_of_isIntertwiningMap ρ ρ (projMap_equivariant h)

@[simp] theorem proj_apply {ρ : Representation k G V} {σ τ : Subrepresentation ρ}
    (h : IsCompl σ τ) (v : V) : proj h v = projMap h v := rfl

/-! ### The implication -/

/-- The identity intertwiner is not zero, on a representation that is not zero. -/
theorem one_ne_zero_intertwiners [Nontrivial V] (ρ : Representation k G V) :
    (1 : IntertwiningMap ρ ρ) ≠ 0 := by
  obtain ⟨v, hv⟩ := exists_ne (0 : V)
  intro h
  exact hv (congrArg (fun f : IntertwiningMap ρ ρ => f v) h)

/-- **Irreducibility from the endomorphism dimension, over any field in which `|G| ≠ 0`.**

This is the implication [SM] Theorem 7 needs and Mathlib does not carry in this direction: the
statement Mathlib has, `IsIrreducible.finrank_intertwiningMap_self`, goes the other way and assumes
the field algebraically closed. Here `k` need only make the group order invertible, which is what
makes the conclusion available over ℚ. -/
theorem isIrreducible_of_finrank_intertwiners_eq_one [Nontrivial V] (ρ : Representation k G V)
    (h : Module.finrank k (IntertwiningMap ρ ρ) = 1) : IsIrreducible ρ := by
  have hcl := complementedLattice ρ
  -- a subrepresentation is `⊥` exactly when its submodule is
  have hbot : ∀ σ : Subrepresentation ρ, σ = ⊥ ↔ σ.toSubmodule = ⊥ :=
    fun σ => ⟨fun hσ => by rw [hσ]; rfl,
      fun hσ => Subrepresentation.toSubmodule_injective (by rw [hσ]; rfl)⟩
  -- `⊥ ≠ ⊤`, because the representation is not zero
  have hbt : (⊥ : Subrepresentation ρ) ≠ ⊤ := fun hb =>
    (bot_ne_top : (⊥ : Submodule k V) ≠ ⊤)
      (congrArg Subrepresentation.toSubmodule hb)
  have : Nontrivial (Subrepresentation ρ) := ⟨⟨⊥, ⊤, hbt⟩⟩
  -- every intertwiner is a scalar multiple of the identity
  have hspan : ∀ f : IntertwiningMap ρ ρ, ∃ c : k, c • (1 : IntertwiningMap ρ ρ) = f :=
    (finrank_eq_one_iff_of_nonzero' (1 : IntertwiningMap ρ ρ)
      (one_ne_zero_intertwiners ρ)).1 h
  refine ⟨fun σ => ?_⟩
  obtain ⟨τ, hτ⟩ := hcl.exists_isCompl σ
  obtain ⟨c, hc⟩ := hspan (proj hτ)
  have hval : ∀ v : V, c • v = projMap hτ v :=
    fun v => congrArg (fun f : IntertwiningMap ρ ρ => f v) hc
  -- a nonzero vector in `σ` forces `c = 1`; a nonzero vector in `τ` forces `c = 0`
  have hσ : σ ≠ ⊥ → c = 1 := by
    intro hne
    obtain ⟨x, hx, hx0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot
      (fun hb => hne ((hbot σ).2 hb))
    have hxx := (hval x).trans (projMap_left hτ hx)
    have hz : (c - 1) • x = 0 := by rw [sub_smul, one_smul, hxx, sub_self]
    rcases smul_eq_zero.1 hz with hcz | hxz
    · exact sub_eq_zero.1 hcz
    · exact absurd hxz hx0
  have hτ0 : τ ≠ ⊥ → c = 0 := by
    intro hne
    obtain ⟨y, hy, hy0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot
      (fun hb => hne ((hbot τ).2 hb))
    rcases smul_eq_zero.1 ((hval y).trans (projMap_right hτ hy)) with hcz | hyz
    · exact hcz
    · exact absurd hyz hy0
  by_cases hs : σ = ⊥
  · exact Or.inl hs
  · refine Or.inr ?_
    have hzero : τ = ⊥ := by
      by_contra ht
      exact one_ne_zero ((hσ hs).symm.trans (hτ0 ht))
    have hsup := hτ.sup_eq_top
    rw [hzero, sup_bot_eq] at hsup
    exact hsup

/-! ### What these proofs rest on -/

#print axioms complementedLattice
#print axioms isCompl_toSubmodule
#print axioms projMap_equivariant
#print axioms one_ne_zero_intertwiners
#print axioms isIrreducible_of_finrank_intertwiners_eq_one

end Irreducibility

end OIBridge
