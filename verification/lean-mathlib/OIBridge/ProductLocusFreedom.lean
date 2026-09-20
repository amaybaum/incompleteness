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

The two normalizations are distinct and are never conflated. What this module
proves about them is the **diagonal values**: a factor's diagonal is `1 / 4` at
its own visible matrix, and the pointwise product's diagonal is `1 / 16` at the
product visible family. The general entry-modulus statement for a realizable
tuple and the anchor-column modulus statement for an admissible dilation are
**not proved here and are not used**.

**Route deviation, recorded and not repaired.** The proof of `a28_s_proper`
consumes three results the freeze's route-authorization matrix does not list in
`A28-S`'s row: act 21's `witness_supply` and `realizable_relabel`, and act 27's
`a27_shared_fibreGram_entry`. The freeze requires an unlisted consumption to be
recorded as a deviation rather than cured by editing the freeze, which is
immutable. The matrix is therefore **not** reported as honoured without
qualification; the result note carries this deviation with the row it departs
from.
-/

namespace OIBridge
namespace ProductLocusFreedom

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps OrbitGeometryIsometries
  StrictNaturalLift

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

/-! ### Section C — `A28-S`, the properness of the product locus at the level of classes

The locus is a set of **classes**: those having a realizable product representative, together with
every tuple equivalent to such a product. A tuple that is not literally a pointwise product does
not show that its class lies outside the locus, and no argument of that shape appears here.

What is proved is a necessary condition on membership, and then its failure at an exhibited
realizable tuple. The necessary condition is that one family of entries does not depend on the
first carrier index of the fibre, and it holds for every tuple in the class of a product because
the phase function of act 12's equivalence depends on the matrix indices and not on the fibre
index. -/

/-- **The necessary condition for lying in the product locus.** If a tuple is equivalent to the
pointwise product of two tuples realizable at the factor visible matrix, then its entries at
matrix indices sharing a first coordinate do not depend on the first coordinate of the fibre
index. The first factor contributes only its diagonal there, which the factor visible matrix fixes
at `1 / 4`, and act 12's phase function depends on the matrix indices alone. -/
theorem a28_s_locus_first_index
    {X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (hX : RealizableGram (Fin 1) (Matrix.of fun _ _ : Fin 4 => (1 / 4 : ℝ)) X)
    {G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ}
    (h : GramPhaseEquiv
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        X i.1 j.1 k.1 * Y i.2 j.2 k.2) G)
    (i₁ i₁' i₂ j₁ j₂ k₂ : Fin 4) :
    G (i₁, i₂) (j₁, j₂) (j₁, k₂) = G (i₁', i₂) (j₁, j₂) (j₁, k₂) := by
  obtain ⟨c, _, hG⟩ := h
  have e := hG (i₁, i₂) (j₁, j₂) (j₁, k₂)
  have e' := hG (i₁', i₂) (j₁, j₂) (j₁, k₂)
  simp only [Matrix.of_apply] at e e'
  rw [e, e', a28_shared_factor_diagonal hX i₁ j₁, a28_shared_factor_diagonal hX i₁' j₁]

/-- **`A28-S` — `A28-S-PROPER`.** At the frozen product configuration there is a tuple realizable
at the product visible family whose class contains **no** pointwise product of two tuples
realizable at the factor visible matrix.

The witness is act 21's product tuple `G(H₁) ⊠ G(Hᵢ)` relabelled by the carrier transposition that
exchanges `(0, 1)` and `(1, 0)`, which is not a product permutation. Realizability is act 21's
`product_realizable` followed by act 21's `realizable_relabel`, the product visible family being
constant and so invariant under every carrier permutation. Membership in the locus fails by
`a28_s_locus_first_index` read at the fibres `(0, 1)` and `(1, 1)` with matrix indices `(2, 0)` and
`(2, 1)`: the relabelling sends the first fibre to `(1, 0)` and fixes the second, leaving the two
entries `1 / 16` and `I / 16`, which differ.

This is a statement about that class at that configuration. It does not describe the locus, does
not count classes, and says nothing about any other configuration. -/
theorem a28_s_proper :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
      (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ RealizableGram (Fin 1 × Fin 1)
            (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G
        ∧ ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y →
              ¬ GramPhaseEquiv
                  (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                    X i.1 j.1 k.1 * Y i.2 j.2 k.2) G := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, _, hΓ₀, hH₁, hHᵢ, _, hadm₁, hadmᵢ, _, _, _, _, _, _, _⟩ := witness_supply
  set τ : Equiv.Perm (Fin 4 × Fin 4) :=
    Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) with hτ
  set X : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ := FibreGram (0 : Fin 1) H₁ with hXdef
  set Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ := FibreGram (0 : Fin 1) Hᵢ with hYdef
  set P : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ :=
    fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
      X i.1 j.1 k.1 * Y i.2 j.2 k.2 with hPdef
  -- the product tuple is realizable at the product visible family
  obtain ⟨U, hUadm, hUgram⟩ := product_realizable hadm₁ hadmᵢ
  have hPreal : RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) P := by
    have := sh1_necessity hUadm
    rwa [hUgram] at this
  -- the product visible family is constant, so every carrier permutation fixes it
  have hΓinv : ∀ i j : Fin 4 × Fin 4,
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (τ i) (τ j)
        = (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) i j := by
    intro i j
    simp [hΓ₀]
  refine ⟨Γ₀, RelabelTransition τ P, hΓ₀,
    realizable_relabel ((0 : Fin 1), (0 : Fin 1)) τ hΓinv hPreal, ?_⟩
  intro X' Y' hX' _ hequiv
  rw [hΓ₀] at hX'
  -- the necessary condition, read at the two fibres
  have hfix := a28_s_locus_first_index hX' hequiv 0 1 1 2 0 1
  -- the relabelling moves the first fibre and fixes the second
  have h01 : τ ((0 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), (0 : Fin 4)) := by
    rw [hτ]; exact Equiv.swap_apply_left _ _
  have h11 : τ ((1 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), (1 : Fin 4)) := by
    rw [hτ]
    refine Equiv.swap_apply_of_ne_of_ne ?_ ?_ <;> simp [Prod.ext_iff]
  have h20 : τ ((2 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), (0 : Fin 4)) := by
    rw [hτ]
    refine Equiv.swap_apply_of_ne_of_ne ?_ ?_ <;> simp [Prod.ext_iff]
  have h21 : τ ((2 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), (1 : Fin 4)) := by
    rw [hτ]
    refine Equiv.swap_apply_of_ne_of_ne ?_ ?_ <;> simp [Prod.ext_iff]
  -- the two entries, computed
  have hX122 : X 1 2 2 = 1 / 4 := by
    rw [hXdef, a27_shared_fibreGram_entry, hH₁]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY001 : Y 0 0 1 = 1 / 4 := by
    rw [hYdef, a27_shared_fibreGram_entry, hHᵢ]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  have hY101 : Y 1 0 1 = Complex.I / 4 := by
    rw [hYdef, a27_shared_fibreGram_entry, hHᵢ]
    norm_num [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
      Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, Complex.ext_iff]
  rw [RelabelTransition, RelabelTransition] at hfix
  simp only [Matrix.submatrix_apply, h01, h11, h20, h21, hPdef, Matrix.of_apply] at hfix
  rw [hX122, hY001, hY101] at hfix
  norm_num [Complex.ext_iff] at hfix

end ProductLocusFreedom
end OIBridge
