import OIBridge.StrictNaturalLift

/-!
# Act 28: the shared lemmas at the product configuration

The configuration is act 21's product configuration, unchanged: carrier
`Fin 4 × Fin 4` of sixteen elements, ancilla `Fin 1 × Fin 1` of one element,
anchor `((0 : Fin 1), (0 : Fin 1))`, factor visible matrix `Γ₀` with entries
`1 / 4`, product visible family the pointwise product with entries `1 / 16`,
and ordered decomposition `Equiv.refl (Fin 4 × Fin 4)`.

Every predicate is consumed from the pinned modules. This module introduces no
top-level definition.

The initial module commit contains shared lemmas only, together with the
sub-question `A28-R` on factor recovery, which is not a verdict of any target
and enters no label. The targets are executed in their separately ordered
verdict commits.

The two normalizations are distinct and are never conflated: a tuple realizable
at the product visible family has every entry of modulus `1 / 16`, while an
admissible dilation for it has anchor-column entries of modulus `1 / 4`. A
factor's own diagonal is `1 / 4`.
-/

namespace OIBridge
namespace ProductLocusFreedom

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps OrbitGeometryIsometries

/-! ### Section A — the shared lemmas, before any verdict -/

/-- The entry of a pointwise product tuple, written out. Consumed everywhere the product
embedding appears, so that no statement has to unfold it inline. -/
theorem a28_shared_product_entry
    (G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i j k : Fin 4 × Fin 4) :
    (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) i j k
      = G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2 := rfl

/-- **A factor's diagonal is `1 / 4`.** For a tuple realizable at the factor visible matrix, the
diagonal entry at any pair of indices is the visible entry, which is `1 / 4` and not `1 / 16`. -/
theorem a28_shared_factor_diagonal
    {G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G) (i j : Fin 4) :
    G i j j = ((1 / 4 : ℝ) : ℂ) := by
  simpa using h.2.2.2 i j

/-- A factor's diagonal entry is nonzero, which is the hypothesis act 23's marginal lemma needs. -/
theorem a28_shared_factor_diagonal_ne_zero
    {G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G) (i j : Fin 4) :
    G i j j ≠ 0 := by
  rw [a28_shared_factor_diagonal h i j]
  norm_num

/-- **The product's diagonal is `1 / 16`.** The pointwise product of two tuples realizable at the
factor visible matrix has diagonal entries `1 / 16`, the product visible family's entries. This is
the second of the two normalizations and is stated apart from the first. -/
theorem a28_shared_product_diagonal
    {G₁ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h₁ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₁)
    (h₂ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₂)
    (i j : Fin 4 × Fin 4) :
    (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) i j j = ((1 / 16 : ℝ) : ℂ) := by
  show G₁ i.1 j.1 j.1 * G₂ i.2 j.2 j.2 = ((1 / 16 : ℝ) : ℂ)
  rw [a28_shared_factor_diagonal h₁, a28_shared_factor_diagonal h₂]
  norm_num

/-! ### Section B — `A28-R`, factor recovery at the level of classes

Equality of product tuples is not what the route needs: the route reads a product tuple up to
`GramPhaseEquiv`, so what it needs is recovery of each factor's class from the product's class.
The sub-question is reported in two parts. The first is act 23's theorem, consumed and not
re-derived. The second has no analogue in the record at the execution base and is proved here.

Neither part is a verdict of any target, and both enter no label. -/

/-- **`A28-R`, first part — consumed from act 23, not re-derived.** Act 23's
`gramPhaseEquiv_fst_of_product` specialized to this configuration: a phase equivalence of two
product tuples whose second factors are realizable restricts to a phase equivalence of the first
factors. The nonzero-diagonal hypothesis act 23's lemma requires is met because a factor's diagonal
is `1 / 4`. -/
theorem a28_r_fst
    {G₁ G₁' G₂ G₂' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h₂ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₂)
    (h₂' : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₂')
    (h : GramPhaseEquiv
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁' i.1 j.1 k.1 * G₂' i.2 j.2 k.2)) :
    GramPhaseEquiv G₁ G₁' :=
  gramPhaseEquiv_fst_of_product (m := (0 : Fin 4))
    (by rw [a28_shared_factor_diagonal h₂, a28_shared_factor_diagonal h₂'])
    (a28_shared_factor_diagonal_ne_zero h₂ 0 0) h

/-- **`A28-R`, second part — this round's obligation, with no analogue at the execution base.**
The same statement with the factors exchanged: a phase equivalence of two product tuples whose
first factors are realizable restricts to a phase equivalence of the second factors, with the
phases `c₂ j₂ := c (m, j₂)`. Reading the equivalence at the matrix indices `(m, j₂)`, `(m, k₂)` in
the fibre `(m, i₂)` gives
`G₁' m m m * G₂' i₂ j₂ k₂ = star (c (m, j₂)) * (G₁ m m m * G₂ i₂ j₂ k₂) * c (m, k₂)`, and the first
factors' diagonal entries, equal and nonzero, cancel. -/
theorem a28_r_snd
    {G₁ G₁' G₂ G₂' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h₁ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₁)
    (h₁' : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₁')
    (h : GramPhaseEquiv
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁' i.1 j.1 k.1 * G₂' i.2 j.2 k.2)) :
    GramPhaseEquiv G₂ G₂' := by
  obtain ⟨c, hc, hG⟩ := h
  refine ⟨fun j => c ((0 : Fin 4), j), fun j => hc ((0 : Fin 4), j), fun i j k => ?_⟩
  have e := hG ((0 : Fin 4), i) ((0 : Fin 4), j) ((0 : Fin 4), k)
  simp only [Matrix.of_apply] at e
  have hd : G₁ (0 : Fin 4) (0 : Fin 4) (0 : Fin 4) = G₁' (0 : Fin 4) (0 : Fin 4) (0 : Fin 4) := by
    rw [a28_shared_factor_diagonal h₁, a28_shared_factor_diagonal h₁']
  have hm : G₁ (0 : Fin 4) (0 : Fin 4) (0 : Fin 4) ≠ 0 :=
    a28_shared_factor_diagonal_ne_zero h₁ 0 0
  rw [← hd] at e
  have e' : G₁ (0 : Fin 4) (0 : Fin 4) (0 : Fin 4) * G₂' i j k
      = G₁ (0 : Fin 4) (0 : Fin 4) (0 : Fin 4)
        * (star (c ((0 : Fin 4), j)) * G₂ i j k * c ((0 : Fin 4), k)) := by
    rw [e]; ring
  exact mul_left_cancel₀ hm e'

/-- **`A28-R`, both parts together.** A phase equivalence of product tuples whose factors are all
realizable restricts to a phase equivalence in each factor separately. This is the form the route
consumes; it is a statement about classes and says nothing about equality of tuples. -/
theorem a28_r_recovery
    {G₁ G₁' G₂ G₂' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (h₁ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₁)
    (h₁' : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₁')
    (h₂ : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₂)
    (h₂' : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) G₂')
    (h : GramPhaseEquiv
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        G₁' i.1 j.1 k.1 * G₂' i.2 j.2 k.2)) :
    GramPhaseEquiv G₁ G₁' ∧ GramPhaseEquiv G₂ G₂' :=
  ⟨a28_r_fst h₂ h₂' h, a28_r_snd h₁ h₁' h⟩

end ProductLocusFreedom
end OIBridge
