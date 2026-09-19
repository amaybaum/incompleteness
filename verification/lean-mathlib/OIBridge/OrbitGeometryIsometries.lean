import OIBridge.OrbitGeometrySelector

/-!
# Act 25 — the orbit-geometry isometries: the normalized realizable quotient, the finite family that acts on it, the internal description of its classes at the single carrier, a gated classification of its surjective isometries, and the prefix-constrained corollary

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-25-orbit-geometry-isometries/preregistration.md`,
blob `f4892f64e1667244fc262a01fb46b27f9b1ba1ba`, from `main` at
`dd3bd2e726e0fb3bccd96df9c46a532119a9ee97` — the certified merge commit of that control plane, the
round's mandated execution base `B`, whose frozen blob this execution verified as its first act.

## What this round is

A **gated round**: four targets frozen together — `ISO1` the normalized space and the finite family
that acts on it, `ISO2` the internal description of the realizable classes at the single-carrier
configuration, `ISO3` the classification of the surjective isometries of the normalized space,
`ISO4` the prefix-constrained corollary for transition families — executed in the fixed order
`ISO1` → `ISO2` → `ISO3` → `ISO4`, each later target opened only if the earlier ones reach the
label the freeze's gate names, with one verdict commit per executed target.

**The definition budget is zero.** This module introduces no definition of any kind. The invariant
family is act 24's `mixedTriple`, consumed; the geometry is act 24's frozen equation, bound as a
hypothesis wherever a statement names it; the four generators of the family — the independent
relabellings `fun i => (G (π i)).submatrix τ τ`, the entrywise conjugation
`fun i => Matrix.of fun j k => star (G i j k)`, and the dilation transpose, the relation
`∃ U, AdmissibleDilationAt Γ a₀ U ∧ FibreGram a₀ U = G ∧ GramPhaseEquiv G' (FibreGram a₀ Uᵀ)` —
are written out by their frozen formulas in every statement that names them; every rung is act 21's
declaration consumed; act 23's Fourier matrix is the lambda its merged statements carry. Every other
object is the merged record's own, consumed unmodified at merged strength. **A merged statement is
not enlarged by being consumed.**

**This module's first commit carries Section A only** — the shared lemmas that answer no target by
themselves: the coordinate identity of an independent relabelling, the fibre-Gram entry at a
one-element ancilla, the coordinate identity of the dilation transpose, the row-phase lemma, the
admissibility of the transpose, the unit-modulus identity with its antipodal consequence, the
dephasing of a single-carrier dilation, and the entries of the Fourier tuple as monomials. Each
verdict enters in its own later commit, in the frozen order.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 25 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

**Act 7's boundary is carried at every use of the visible family**: act 7's `D4b` came back negative
— Source A supplies no general map carrying the relative candidate on the dilated carrier back to
`V` — and the readback is the repository's own, frozen by act 7's readback amendment.
-/

namespace OIBridge
namespace OrbitGeometryIsometries

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector

/-! ### Section A — the shared lemmas, before any verdict

None of these is a verdict of any target. No definition is introduced. -/

variable {V : Type} [Fintype V] [DecidableEq V]

omit [Fintype V] [DecidableEq V] in
/-- **The coordinate identity of an independent relabelling**: the feature map of
`fun i => (G (π i)).submatrix τ τ` at a coordinate is the feature map of `G` at the coordinate with
the fibre labels moved by `π` and the matrix indices by `τ`. -/
theorem mixedTriple_relabel2 (π τ : Equiv.Perm V) (G : V → Matrix V V ℂ)
    (p : (V × V × V) × (V × V × V)) :
    mixedTriple (fun i => (G (π i)).submatrix τ τ) p
      = mixedTriple G (((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2))) := by
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] in
/-- **The fibre-Gram entry at a one-element ancilla**: with `x` the unique element of `A`, the
sum in `fibreGram_apply` has one term. -/
theorem fibreGram_unique {A : Type} [Fintype A] (x : A) (hx : ∀ y : A, y = x) (a₀ : A)
    (U : Matrix (V × A) (V × A) ℂ) (i j k : V) :
    FibreGram a₀ U i j k = star (U (i, x) (j, a₀)) * U (i, x) (k, a₀) := by
  rw [fibreGram_apply]
  exact Finset.sum_eq_single x (fun b _ hb => absurd (hx b) hb)
    (fun h => absurd (Finset.mem_univ x) h)

omit [Fintype V] [DecidableEq V] in
/-- **The coordinate identity of the dilation transpose** at a one-element ancilla: a coordinate of
the feature map of `FibreGram a₀ Uᵀ` is the conjugate of a coordinate of the feature map of
`FibreGram a₀ U`, at the index with the fibre labels and the matrix indices exchanged and the
matrix-index triple rotated: `((i₁, i₂, i₃), (j₁, j₂, j₃)) ↦ ((j₂, j₃, j₁), (i₁, i₂, i₃))`. -/
theorem mixedTriple_transpose {A : Type} [Fintype A] (x : A) (hx : ∀ y : A, y = x) (a₀ : A)
    (U : Matrix (V × A) (V × A) ℂ) (p : (V × V × V) × (V × V × V)) :
    mixedTriple (FibreGram a₀ Uᵀ) p
      = star (mixedTriple (FibreGram a₀ U) ((p.2.2.1, p.2.2.2, p.2.1), p.1)) := by
  obtain rfl := hx a₀
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, fibreGram_unique a₀ hx a₀, Matrix.transpose_apply, star_mul', star_star]
  ring

omit [Fintype V] [DecidableEq V] in
/-- **The row-phase lemma**: two vectors with no vanishing entry and the same rank-one Gram data
differ by one unit-modulus factor. -/
theorem rows_phase (u u' : V → ℂ) (h : ∀ j k, star (u j) * u k = star (u' j) * u' k)
    (hne : ∀ j, u j ≠ 0) : ∃ e : ℂ, ‖e‖ = 1 ∧ ∀ j, u' j = e * u j := by
  rcases isEmpty_or_nonempty V with hV | ⟨⟨j₀⟩⟩
  · exact ⟨1, by simp, fun j => (hV.false j).elim⟩
  have hnorm : ‖u' j₀‖ = ‖u j₀‖ := by
    have e := h j₀ j₀
    rw [star_mul_self_eq_norm_sq, star_mul_self_eq_norm_sq] at e
    have e2 : ‖u j₀‖ ^ 2 = ‖u' j₀‖ ^ 2 := by exact_mod_cast e
    exact ((pow_left_inj₀ (norm_nonneg _) (norm_nonneg _) two_ne_zero).mp e2).symm
  refine ⟨u' j₀ / u j₀, ?_, fun k => ?_⟩
  · rw [norm_div, hnorm, div_self (norm_ne_zero_iff.mpr (hne j₀))]
  · have key : u' k * u j₀ = u' j₀ * u k := by
      apply mul_left_cancel₀ (star_ne_zero.mpr (hne j₀))
      linear_combination (u' k) * h j₀ j₀ - (u' j₀) * h j₀ k
    rw [div_mul_eq_mul_div, eq_div_iff (hne j₀)]
    exact key

/-- **The transpose of an admissible dilation is admissible** at a one-element ancilla and a
symmetric visible family: `Uᵀ` is unitary, and its anchored moduli are those of `U` with the two
indices exchanged. -/
theorem transpose_admissible {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (hΓ : ∀ i j, Γ i j = Γ j i) (a₀ : A)
    (U : Matrix (V × A) (V × A) ℂ) (hU : AdmissibleDilationAt Γ a₀ U) :
    AdmissibleDilationAt Γ a₀ Uᵀ := by
  obtain rfl := hx a₀
  refine ⟨?_, fun i j => ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.transpose_conjTranspose,
      ← Matrix.conjTranspose_transpose, ← Matrix.transpose_mul, ← Matrix.star_eq_conjTranspose,
      Matrix.mem_unitaryGroup_iff'.mp hU.1, Matrix.transpose_one]
  · have hsingle : ∀ f : A → ℝ, ∑ a, f a = f a₀ :=
      fun f => Finset.sum_eq_single a₀ (fun b _ hb => absurd (hx b) hb)
        (fun h => absurd (Finset.mem_univ a₀) h)
    have e := hU.2 j i
    rw [hsingle] at e
    rw [hsingle, Matrix.transpose_apply, hΓ]
    exact e

omit [Fintype V] [DecidableEq V] in
/-- **The unit-modulus identity and its antipodal consequence**: four unit-modulus numbers summing
to zero, one of them `1`, form two antipodal pairs — one of `a + b`, `b + c`, `c + a` vanishes and
the remaining number is `−1`. -/
theorem antipodal (a b c : ℂ) (ha : star a * a = 1) (hb : star b * b = 1) (hc : star c * c = 1)
    (h : 1 + a + b + c = 0) :
    (a + b = 0 ∧ c = -1) ∨ (b + c = 0 ∧ a = -1) ∨ (c + a = 0 ∧ b = -1) := by
  have hs : 1 + star a + star b + star c = 0 := by
    have := congrArg star h
    simpa using this
  have h2 : a * b * c + b * c + a * c + a * b = 0 := by
    linear_combination (a * b * c) * hs - (b * c) * ha - (a * c) * hb - (a * b) * hc
  have h3 : (a + b) * (b + c) * (c + a) = 0 := by
    linear_combination (a * b + b * c + c * a) * h - h2
  rcases mul_eq_zero.mp h3 with h4 | h4
  · rcases mul_eq_zero.mp h4 with h5 | h5
    · exact Or.inl ⟨h5, by linear_combination h - h5⟩
    · exact Or.inr (Or.inl ⟨h5, by linear_combination h - h5⟩)
  · exact Or.inr (Or.inr ⟨h4, by linear_combination h - h4⟩)

/-- **Dephasing a single-carrier dilation.** For `U` admissible at `Γ₀ ≡ ¼` with anchor `0`, the
matrix `K i j := 2 * star (r i) * star (c j) * U (i, 0) (j, 0)` with the unit phases
`r i := 2 * U (i, 0) (0, 0)` and `c j := 4 * star (U (0, 0) (0, 0)) * U (0, 0) (j, 0)` has
unit-modulus entries, first row and first column `1`, pairwise orthogonal rows, and the fibre-Gram
tuple of `U` is act 12's action by the phases `c` on the tuple `star (K i j) * K i k / 4`. -/
theorem dephase (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (K : Matrix (Fin 4) (Fin 4) ℂ) (r c : Fin 4 → ℂ)
    (hr : r = fun i => 2 * U (i, 0) (0, 0))
    (hc : c = fun j => 4 * star (U (0, 0) (0, 0)) * U (0, 0) (j, 0))
    (hK : K = fun i j => 2 * star (r i) * star (c j) * U (i, 0) (j, 0)) :
    (∀ i j, star (K i j) * K i j = 1) ∧ (∀ i, K i 0 = 1) ∧ (∀ j, K 0 j = 1)
      ∧ (∀ i i', i ≠ i' → ∑ j, K i j * star (K i' j) = 0)
      ∧ (∀ j, ‖c j‖ = 1) ∧ (∀ i, ‖r i‖ = 1)
      ∧ (∀ i j k, FibreGram (0 : Fin 1) U i j k = star (c j) * (star (K i j) * K i k / 4) * c k) := by
  -- the moduli of the entries of `U`
  have hmod : ∀ i j, star (U (i, 0) (j, 0)) * U (i, 0) (j, 0) = 1 / 4 := by
    intro i j
    have e := hU.2 i j
    rw [hΓ₀, Matrix.of_apply, Fin.sum_univ_one] at e
    rw [star_mul_self_eq_norm_sq, ← e]
    push_cast
    ring
  have hmod' : ∀ i j, U (i, 0) (j, 0) * star (U (i, 0) (j, 0)) = 1 / 4 := fun i j => by
    rw [mul_comm]; exact hmod i j
  -- the row orthonormality of `U`, read at the anchored slots
  have horth : ∀ i i', i ≠ i' → ∑ j, U (i, 0) (j, 0) * star (U (i', 0) (j, 0)) = 0 := by
    intro i i' hii'
    have e := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU.1) (i, 0)) (i', 0)
    rw [Matrix.one_apply_ne (by simp [Prod.ext_iff, hii'])] at e
    simp only [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_one,
      Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply] at e
    exact e
  have hrn : ∀ i, star (r i) * r i = 1 := by
    intro i; rw [hr]; simp only [star_mul', star_ofNat]
    linear_combination 4 * hmod i 0
  have hcn : ∀ j, star (c j) * c j = 1 := by
    intro j; rw [hc]; simp only [star_mul', star_ofNat, star_star]
    linear_combination (16 * (star (U (0, 0) (j, 0)) * U (0, 0) (j, 0))) * hmod' 0 0
      + 4 * hmod 0 j
  refine ⟨fun i j => ?_, fun i => ?_, fun j => ?_, fun i i' hii' => ?_, fun j => ?_, fun i => ?_,
    fun i j k => ?_⟩
  · rw [hK]; simp only [star_mul', star_ofNat, star_star]
    linear_combination (4 * (star (r i) * r i) * (star (c j) * c j)) * hmod i j
      + (star (r i) * r i) * hcn j + hrn i
  · rw [hK, hr, hc]; simp only [star_mul', star_ofNat, star_star]
    linear_combination (16 * (U (0, 0) (0, 0) * star (U (0, 0) (0, 0)))) * hmod i 0
      + 4 * hmod' 0 0
  · rw [hK, hr, hc]; simp only [star_mul', star_ofNat, star_star]
    linear_combination (16 * (star (U (0, 0) (j, 0)) * U (0, 0) (j, 0))) * hmod 0 0
      + 4 * hmod 0 j
  · rw [hK]
    have : ∀ j, (2 * star (r i) * star (c j) * U (i, 0) (j, 0))
        * star (2 * star (r i') * star (c j) * U (i', 0) (j, 0))
        = (4 * star (r i) * r i') * (U (i, 0) (j, 0) * star (U (i', 0) (j, 0))) := by
      intro j
      simp only [star_mul', star_ofNat, star_star]
      linear_combination (4 * star (r i) * r i' * (U (i, 0) (j, 0) * star (U (i', 0) (j, 0))))
        * hcn j
    simp only [this, ← Finset.mul_sum, horth i i' hii', mul_zero]
  · have := hcn j
    rw [star_mul_self_eq_norm_sq] at this
    have h2 : ‖c j‖ ^ 2 = 1 := by exact_mod_cast this
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg _) two_ne_zero).mp h2
  · have := hrn i
    rw [star_mul_self_eq_norm_sq] at this
    have h2 : ‖r i‖ ^ 2 = 1 := by exact_mod_cast this
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg _) two_ne_zero).mp h2
  · rw [fibreGram_apply, Fin.sum_univ_one, hK]
    simp only [star_mul', star_ofNat, star_star]
    linear_combination
      (-(star (U (i, 0) (j, 0)) * U (i, 0) (k, 0) * (star (c j) * c j) * (star (c k) * c k))) * hrn i
      - (star (U (i, 0) (j, 0)) * U (i, 0) (k, 0) * (star (c k) * c k)) * hcn j
      - (star (U (i, 0) (j, 0)) * U (i, 0) (k, 0)) * hcn k

/-- **The entries of the Fourier tuple are monomials**: at a unit parameter, every entry of
`FibreGram 0 (H z)` is one of `±¼`, `±z/4`, `±star z/4`. -/
theorem fourier_entry_monomial (z : ℂ) (hz : star z * z = 1) (i j k : Fin 4) :
    FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i j k
      ∈ ({1 / 4, -(1 / 4), z / 4, -(z / 4), star z / 4, -(star z / 4)} : Set ℂ) := by
  have hz2 : (starRingEnd ℂ) z * z = 1 := hz
  have hz2' : z * (starRingEnd ℂ) z = 1 := by rw [mul_comm]; exact hz
  rw [fibreGram_apply, Fin.sum_univ_one]
  simp only [Matrix.of_apply, Set.mem_insert_iff, Set.mem_singleton_iff, Complex.star_def]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [map_mul, map_neg, map_ofNat] <;>
    first
      | (left; ring1)
      | (right; left; ring1)
      | (right; right; left; ring1)
      | (right; right; right; left; ring1)
      | (right; right; right; right; left; ring1)
      | (right; right; right; right; right; ring1)
      | (left; linear_combination (1 / 4 : ℂ) * hz2)
      | (left; linear_combination (-1 / 4 : ℂ) * hz2)
      | (right; left; linear_combination (1 / 4 : ℂ) * hz2)

/-! ### Section B — `ISO1`: the normalized space and the family that acts on it

The normalized space is the realizable quotient carried onto its feature image by act 24's
`geo1_triple_metric`; nothing is defined for it. Each generator is written by its frozen formula.
The dilation transpose is the relation `∃ U, AdmissibleDilationAt Γ a₀ U ∧ FibreGram a₀ U = G ∧
GramPhaseEquiv G' (FibreGram a₀ Uᵀ)`; its totality is act 12's `sh1_sufficiency`, and its
single-valuedness on classes and its descent are proved here. -/

open scoped ComplexOrder in
/-- **`ISO1` (i) — an independent relabelling preserves realizability at a constant visible
family**: positive semidefiniteness and rank are invariant under a submatrix by a permutation, the
relabelled fibres sum to the relabelled identity, and the diagonal is the constant. -/
theorem relabel2_realizable {A : Type} [Fintype A] (Γ : Matrix V V ℝ)
    (hΓ : ∀ i j i' j', Γ i j = Γ i' j') (π τ : Equiv.Perm V) (G : V → Matrix V V ℂ)
    (hG : RealizableGram A Γ G) : RealizableGram A Γ (fun i => (G (π i)).submatrix τ τ) := by
  refine ⟨fun i => (hG.1 (π i)).submatrix τ, fun i => ?_, ?_, fun i j => ?_⟩
  · rw [Matrix.rank_submatrix]; exact hG.2.1 (π i)
  · ext j k
    have h1 := congrFun (congrFun hG.2.2.1 (τ j)) (τ k)
    rw [Matrix.sum_apply] at h1
    rw [Matrix.sum_apply]
    simp only [Matrix.submatrix_apply]
    rw [Equiv.sum_comp π (fun i => G i (τ j) (τ k)), h1]
    simp [Matrix.one_apply, τ.injective.eq_iff]
  · simp only [Matrix.submatrix_apply]
    rw [hG.2.2.2 (π i) (τ j), hΓ (π i) (τ j) i j]

omit [Fintype V] [DecidableEq V] in
/-- **`ISO1` (ii) — an independent relabelling descends to classes**, with the phases `c ∘ τ`. -/
theorem relabel2_gramPhaseEquiv (π τ : Equiv.Perm V) {G G' : V → Matrix V V ℂ}
    (h : GramPhaseEquiv G G') :
    GramPhaseEquiv (fun i => (G (π i)).submatrix τ τ) (fun i => (G' (π i)).submatrix τ τ) := by
  obtain ⟨c, hc, hG⟩ := h
  exact ⟨fun j => c (τ j), fun j => hc (τ j), fun i j k => by
    simp only [Matrix.submatrix_apply]; exact hG (π i) (τ j) (τ k)⟩

omit [DecidableEq V] in
/-- **`ISO1` (iii) — an independent relabelling is an exact isometry**: the sum is reindexed along
the bijection `(π, π, π) × (τ, τ, τ)` of the index set. -/
theorem relabel2_isometry (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (π τ : Equiv.Perm V) (G H : V → Matrix V V ℂ) :
    d (fun i => (G (π i)).submatrix τ τ) (fun i => (H (π i)).submatrix τ τ) = d G H := by
  subst hd
  simp only [mixedTriple_relabel2]
  congr 1
  exact Equiv.sum_comp ((π.prodCongr (π.prodCongr π)).prodCongr (τ.prodCongr (τ.prodCongr τ)))
    (fun q => ‖mixedTriple G q - mixedTriple H q‖ ^ 2)

omit [DecidableEq V] in
/-- **`ISO1` (iv) — the entrywise conjugation is an exact isometry at every carrier**, from act
24's coordinatewise conjugation identity. -/
theorem conj_isometry (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) :
    d (fun i => Matrix.of fun j k => star (G i j k)) (fun i => Matrix.of fun j k => star (H i j k))
      = d G H := by
  subst hd
  have key : ∀ p, ‖mixedTriple (fun i => Matrix.of fun j k => star (G i j k)) p
      - mixedTriple (fun i => Matrix.of fun j k => star (H i j k)) p‖
      = ‖mixedTriple G p - mixedTriple H p‖ := fun p => by
    rw [mixedTriple_star, mixedTriple_star, ← star_sub, norm_star]
  simp only [key]

/-- **The transpose is single-valued on classes**: two admissible dilations of one realizable tuple
at a one-element ancilla differ row by row by unit phases, so their transposes' fibre-Gram tuples
are phase-equivalent. -/
theorem transpose_single_valued {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (hΓ : ∀ i j, Γ i j ≠ 0) (a₀ : A) (U U' : Matrix (V × A) (V × A) ℂ)
    (hU : AdmissibleDilationAt Γ a₀ U) (_hU' : AdmissibleDilationAt Γ a₀ U')
    (h : FibreGram a₀ U = FibreGram a₀ U') :
    GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ) := by
  obtain rfl := hx a₀
  have hsingle : ∀ f : A → ℝ, ∑ a, f a = f a₀ :=
    fun f => Finset.sum_eq_single a₀ (fun b _ hb => absurd (hx b) hb)
      (fun h => absurd (Finset.mem_univ a₀) h)
  have hne : ∀ i j, U (i, a₀) (j, a₀) ≠ 0 := by
    intro i j h0
    have e := hU.2 i j
    rw [hsingle, h0] at e
    simp at e
    exact hΓ i j e
  have hrow : ∀ i, ∃ e : ℂ, ‖e‖ = 1 ∧ ∀ j, U' (i, a₀) (j, a₀) = e * U (i, a₀) (j, a₀) := by
    intro i
    refine rows_phase (fun j => U (i, a₀) (j, a₀)) (fun j => U' (i, a₀) (j, a₀)) (fun j k => ?_)
      (fun j => hne i j)
    have e := congrFun (congrFun (congrFun h i) j) k
    rw [fibreGram_unique a₀ hx, fibreGram_unique a₀ hx] at e
    exact e
  choose e he using hrow
  refine ⟨e, fun j => (he j).1, fun i j k => ?_⟩
  rw [fibreGram_unique a₀ hx, fibreGram_unique a₀ hx]
  simp only [Matrix.transpose_apply, (he j).2, (he k).2, star_mul']
  ring

/-- The transpose of a unitary matrix is unitary. -/
theorem transpose_unitary {n : Type} [Fintype n] [DecidableEq n] {U : Matrix n n ℂ}
    (hU : U ∈ Matrix.unitaryGroup n ℂ) : Uᵀ ∈ Matrix.unitaryGroup n ℂ := by
  rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.transpose_conjTranspose,
    ← Matrix.conjTranspose_transpose, ← Matrix.transpose_mul, ← Matrix.star_eq_conjTranspose,
    Matrix.mem_unitaryGroup_iff'.mp hU, Matrix.transpose_one]

/-- **The transpose descends to classes**: an admissible dilation of a phase-equivalent tuple is
the dilation multiplied by the diagonal of the phases, and its transpose has the same fibre-Gram
tuple as the transposed dilation. -/
theorem transpose_descends {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (a₀ : A) (U : Matrix (V × A) (V × A) ℂ) (hU : AdmissibleDilationAt Γ a₀ U)
    (G' : V → Matrix V V ℂ) (h : GramPhaseEquiv (FibreGram a₀ U) G') :
    ∃ U' : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U' ∧ FibreGram a₀ U' = G'
      ∧ GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ) := by
  obtain rfl := hx a₀
  obtain ⟨c, hc, hG'⟩ := h
  have hcu : ∀ j, c j * star (c j) = 1 := fun j => by
    rw [mul_comm, star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  have hcu' : ∀ j, star (c j) * c j = 1 := fun j => by rw [mul_comm]; exact hcu j
  refine ⟨U * Matrix.diagonal (fun p : V × A => c p.1), ⟨?_, fun i j => ?_⟩, ?_, ?_⟩
  · -- unitary: the product of `U` with a diagonal unitary
    have hD : Matrix.diagonal (fun p : V × A => c p.1) ∈ Matrix.unitaryGroup (V × A) ℂ := by
      rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.diagonal_conjTranspose,
        Matrix.diagonal_mul_diagonal]
      ext p q
      simp only [Matrix.diagonal_apply, Matrix.one_apply, Pi.star_apply]
      split_ifs with hpq
      · exact hcu p.1
      · rfl
    exact Submonoid.mul_mem _ hU.1 hD
  · rw [hU.2 i j]
    congr 1; ext a
    rw [Matrix.mul_diagonal, norm_mul, hc, mul_one]
  · funext i; ext j k
    rw [fibreGram_unique a₀ hx, hG', fibreGram_unique a₀ hx]
    simp only [Matrix.mul_diagonal, star_mul']
    ring
  · have : FibreGram a₀ (U * Matrix.diagonal (fun p : V × A => c p.1))ᵀ = FibreGram a₀ Uᵀ := by
      funext i; ext j k
      rw [fibreGram_unique a₀ hx, fibreGram_unique a₀ hx]
      simp only [Matrix.transpose_apply, Matrix.mul_diagonal, star_mul']
      linear_combination (star (U (j, a₀) (i, a₀)) * U (k, a₀) (i, a₀)) * hcu' i
    rw [this]
    exact gramPhaseEquiv_refl _

omit [DecidableEq V] in
/-- **`ISO1` (ix) — the transpose is an exact isometry on dilations**: the sum is reindexed along
the bijection `((i₁, i₂, i₃), (j₁, j₂, j₃)) ↦ ((j₂, j₃, j₁), (i₁, i₂, i₃))` and the conjugation
preserves every norm. -/
theorem transpose_isometry {A : Type} [Fintype A] (x : A) (hx : ∀ y : A, y = x) (a₀ : A)
    (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (U U' : Matrix (V × A) (V × A) ℂ) :
    d (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ) = d (FibreGram a₀ U) (FibreGram a₀ U') := by
  subst hd
  have key : ∀ p, ‖mixedTriple (FibreGram a₀ Uᵀ) p - mixedTriple (FibreGram a₀ U'ᵀ) p‖
      = ‖mixedTriple (FibreGram a₀ U) ((p.2.2.1, p.2.2.2, p.2.1), p.1)
          - mixedTriple (FibreGram a₀ U') ((p.2.2.1, p.2.2.2, p.2.1), p.1)‖ := fun p => by
    rw [mixedTriple_transpose x hx, mixedTriple_transpose x hx, ← star_sub, norm_star]
  simp only [key]
  congr 1
  exact Equiv.sum_comp
    { toFun := fun p : (V × V × V) × (V × V × V) => ((p.2.2.1, p.2.2.2, p.2.1), p.1)
      invFun := fun q => (q.2, (q.1.2.2, q.1.1, q.1.2.1))
      left_inv := fun p => rfl
      right_inv := fun q => rfl }
    (fun q => ‖mixedTriple (FibreGram a₀ U) q - mixedTriple (FibreGram a₀ U') q‖ ^ 2)

/-- **The relabelled dilation**: the submatrix of an admissible dilation by `π` on the rows' carrier
index and `τ` on the columns' carrier index is admissible at a constant visible family, its
fibre-Gram tuple is the `(π, τ)`-relabelling, and its transpose's fibre-Gram tuple is the
`(τ, π)`-relabelling of the transposed dilation's. -/
theorem relabel2_dilation {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (hΓ : ∀ i j i' j', Γ i j = Γ i' j') (a₀ : A) (π τ : Equiv.Perm V)
    (U : Matrix (V × A) (V × A) ℂ) (hU : AdmissibleDilationAt Γ a₀ U) :
    AdmissibleDilationAt Γ a₀ (U.submatrix (Prod.map π id) (Prod.map τ id))
      ∧ FibreGram a₀ (U.submatrix (Prod.map π id) (Prod.map τ id))
          = (fun i => (FibreGram a₀ U (π i)).submatrix τ τ)
      ∧ FibreGram a₀ (U.submatrix (Prod.map π id) (Prod.map τ id))ᵀ
          = (fun i => (FibreGram a₀ Uᵀ (τ i)).submatrix π π) := by
  obtain rfl := hx a₀
  refine ⟨⟨?_, fun i j => ?_⟩, ?_, ?_⟩
  · have e₁ : (Prod.map π id : V × A → V × A) = (π.prodCongr (Equiv.refl A)) := rfl
    have e₂ : (Prod.map τ id : V × A → V × A) = (τ.prodCongr (Equiv.refl A)) := rfl
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.conjTranspose_submatrix,
      e₁, e₂, Matrix.submatrix_mul_equiv, ← Matrix.star_eq_conjTranspose,
      Matrix.mem_unitaryGroup_iff.mp hU.1, Matrix.submatrix_one_equiv]
  · rw [hΓ i j (π i) (τ j), hU.2 (π i) (τ j)]
    rfl
  · funext i; ext j k
    simp only [Matrix.submatrix_apply, fibreGram_unique a₀ hx, Prod.map_apply, id]
  · funext i; ext j k
    simp only [Matrix.submatrix_apply, Matrix.transpose_apply, fibreGram_unique a₀ hx,
      Prod.map_apply, id]

/-- **The conjugated dilation**: the entrywise conjugate of an admissible dilation is admissible,
its fibre-Gram tuple is the conjugation of the original's, and its transpose's fibre-Gram tuple is
the conjugation of the transposed dilation's. -/
theorem conj_dilation {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (a₀ : A) (U : Matrix (V × A) (V × A) ℂ) (hU : AdmissibleDilationAt Γ a₀ U) :
    AdmissibleDilationAt Γ a₀ (U.map star)
      ∧ FibreGram a₀ (U.map star) = (fun i => Matrix.of fun j k => star (FibreGram a₀ U i j k))
      ∧ FibreGram a₀ (U.map star)ᵀ
          = (fun i => Matrix.of fun j k => star (FibreGram a₀ Uᵀ i j k)) := by
  obtain rfl := hx a₀
  refine ⟨⟨?_, fun i j => ?_⟩, ?_, ?_⟩
  · -- `U.map star = (star U)ᵀ`, the transpose of the unitary `star U`
    have h1 : U.map star = (star U)ᵀ := by
      rw [Matrix.star_eq_conjTranspose]; exact (Matrix.conjTranspose_transpose U).symm
    rw [h1]
    exact transpose_unitary (Unitary.star_mem hU.1)
  · rw [hU.2 i j]
    congr 1; ext a
    rw [Matrix.map_apply, norm_star]
  · funext i; ext j k
    simp only [Matrix.of_apply, fibreGram_unique a₀ hx, Matrix.map_apply, star_mul', star_star]
  · funext i; ext j k
    simp only [Matrix.of_apply, fibreGram_unique a₀ hx, Matrix.map_apply, Matrix.transpose_apply,
      star_mul', star_star]

omit [Fintype V] [DecidableEq V] in
/-- **Relation (v) — the conjugation commutes with every independent relabelling**, exactly. -/
theorem conj_relabel2 (π τ : Equiv.Perm V) (G : V → Matrix V V ℂ) :
    (fun i => Matrix.of fun j k => star ((fun i => (G (π i)).submatrix τ τ) i j k))
      = fun i => ((fun i => Matrix.of fun j k => star (G i j k)) (π i)).submatrix τ τ := by
  funext i; ext j k
  simp only [Matrix.of_apply, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] in
/-- **Relation (vi) — two independent relabellings compose to one**, `(π.trans π', τ.trans τ')`,
exactly. -/
theorem relabel2_relabel2 (π τ π' τ' : Equiv.Perm V) (G : V → Matrix V V ℂ) :
    (fun i => ((fun i => (G (π' i)).submatrix τ' τ') (π i)).submatrix τ τ)
      = fun i => (G ((π.trans π') i)).submatrix (τ.trans τ') (τ.trans τ') := by
  funext i; ext j k
  simp only [Matrix.submatrix_apply, Equiv.trans_apply]

/-- **The four-shape normal form for every word in the generators.** A word is a list of generator
tokens — an independent relabelling `(π, τ)`, the conjugation, or the transpose — and a tuple `H`
is reached from `G` by the word when a chain of tuples realizes each token in order by its frozen
formula, the transpose through an admissible dilation. For a realizable `G`, every tuple so reached
is phase-equivalent to one of the four shapes applied to `G` — a relabelling, a relabelling composed
with conjugation, a relabelling composed with the transpose, or a relabelling composed with both —
the transpose shapes read through every admissible dilation of `G`. Proved by induction on the word
from the six relations, descent and realizability preservation; no definition is introduced. -/
theorem iso1_word_normal_form {A : Type} [Fintype A] [DecidableEq A] (x : A) (hx : ∀ y : A, y = x)
    (Γ : Matrix V V ℝ) (hΓ : ∀ i j i' j', Γ i j = Γ i' j') (hΓne : ∀ i j, Γ i j ≠ 0) (a₀ : A)
    (w : List ((Equiv.Perm V × Equiv.Perm V) ⊕ (Unit ⊕ Unit))) (G H : V → Matrix V V ℂ)
    (hG : RealizableGram A Γ G)
    (hw : ∃ c : ℕ → (V → Matrix V V ℂ), c 0 = G ∧ c w.length = H ∧
      ∀ (n : ℕ) (hn : n < w.length),
        match w[n]'hn with
        | Sum.inl ⟨π, τ⟩ => c (n + 1) = fun i => (c n (π i)).submatrix τ τ
        | Sum.inr (Sum.inl _) => c (n + 1) = fun i => Matrix.of fun j k => star (c n i j k)
        | Sum.inr (Sum.inr _) => ∃ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U
            ∧ FibreGram a₀ U = c n ∧ GramPhaseEquiv (c (n + 1)) (FibreGram a₀ Uᵀ)) :
    ∃ π τ : Equiv.Perm V,
        GramPhaseEquiv H (fun i => (G (π i)).submatrix τ τ)
      ∨ GramPhaseEquiv H (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k))
      ∨ (∀ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ U = G →
          GramPhaseEquiv H (fun i => (FibreGram a₀ Uᵀ (π i)).submatrix τ τ))
      ∨ (∀ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ U = G →
          GramPhaseEquiv H (fun i => Matrix.of fun j k =>
            star ((FibreGram a₀ Uᵀ (π i)).submatrix τ τ j k))) := by
  have hΓs : ∀ i j, Γ i j = Γ j i := fun i j => hΓ i j j i
  induction w generalizing G with
  | nil =>
    obtain ⟨c, h0, hl, -⟩ := hw
    simp only [List.length_nil] at hl
    refine ⟨1, 1, Or.inl ?_⟩
    rw [← hl, h0]
    have e : (fun i => (G ((1 : Equiv.Perm V) i)).submatrix (1 : Equiv.Perm V) (1 : Equiv.Perm V))
        = G := by
      ext i j k; simp [Matrix.submatrix_apply]
    rw [e]
    exact gramPhaseEquiv_refl G
  | cons g w' ih =>
    obtain ⟨c, h0, hl, hstep⟩ := hw
    have hK := hstep 0 (by simp)
    simp only [List.getElem_cons_zero] at hK
    have hchain : ∃ c' : ℕ → (V → Matrix V V ℂ), c' 0 = c 1 ∧ c' w'.length = H ∧
        ∀ (n : ℕ) (hn : n < w'.length),
          match w'[n]'hn with
          | Sum.inl ⟨π, τ⟩ => c' (n + 1) = fun i => (c' n (π i)).submatrix τ τ
          | Sum.inr (Sum.inl _) => c' (n + 1) = fun i => Matrix.of fun j k => star (c' n i j k)
          | Sum.inr (Sum.inr _) => ∃ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U
              ∧ FibreGram a₀ U = c' n ∧ GramPhaseEquiv (c' (n + 1)) (FibreGram a₀ Uᵀ) :=
      ⟨fun n => c (n + 1), rfl, by simpa [List.length_cons] using hl, fun n hn => by
        have h := hstep (n + 1) (by simpa [List.length_cons] using Nat.succ_lt_succ hn)
        simpa [List.getElem_cons_succ] using h⟩
    rcases g with ⟨π', τ'⟩ | ⟨⟨⟩⟩ | ⟨⟨⟩⟩
    · -- the first token is an independent relabelling
      simp only [h0] at hK
      have hKr : RealizableGram A Γ (c 1) := by
        rw [hK]; exact relabel2_realizable Γ hΓ π' τ' G hG
      obtain ⟨π, τ, hsh⟩ := ih (c 1) hKr hchain
      rcases hsh with h1 | h2 | h3 | h4
      · refine ⟨π.trans π', τ.trans τ', Or.inl ?_⟩
        convert h1 using 2
        ext i j; simp [hK, Matrix.submatrix_apply, Equiv.trans_apply]
      · refine ⟨π.trans π', τ.trans τ', Or.inr (Or.inl ?_)⟩
        convert h2 using 2
        ext i j; simp [hK, Matrix.submatrix_apply, Matrix.of_apply, Equiv.trans_apply]
      · refine ⟨π.trans τ', τ.trans π', Or.inr (Or.inr (Or.inl fun U hU hFU => ?_))⟩
        obtain ⟨hU₁, hF₁, hFT₁⟩ := relabel2_dilation x hx Γ hΓ a₀ π' τ' U hU
        have h := h3 _ hU₁ (by rw [hF₁, hFU, hK])
        rw [hFT₁] at h
        convert h using 2
        ext i j; simp [Matrix.submatrix_apply, Equiv.trans_apply]
      · refine ⟨π.trans τ', τ.trans π', Or.inr (Or.inr (Or.inr fun U hU hFU => ?_))⟩
        obtain ⟨hU₁, hF₁, hFT₁⟩ := relabel2_dilation x hx Γ hΓ a₀ π' τ' U hU
        have h := h4 _ hU₁ (by rw [hF₁, hFU, hK])
        rw [hFT₁] at h
        convert h using 2
        ext i j; simp [Matrix.submatrix_apply, Matrix.of_apply, Equiv.trans_apply]
    · -- the first token is the conjugation
      simp only [h0] at hK
      have hKr : RealizableGram A Γ (c 1) := by
        rw [hK]; exact realizable_conj Γ G hG
      obtain ⟨π, τ, hsh⟩ := ih (c 1) hKr hchain
      rcases hsh with h1 | h2 | h3 | h4
      · refine ⟨π, τ, Or.inr (Or.inl ?_)⟩
        convert h1 using 2
        ext i j; simp [hK, Matrix.submatrix_apply, Matrix.of_apply]
      · refine ⟨π, τ, Or.inl ?_⟩
        convert h2 using 2
        ext i j; simp [hK, Matrix.submatrix_apply, Matrix.of_apply]
      · refine ⟨π, τ, Or.inr (Or.inr (Or.inr fun U hU hFU => ?_))⟩
        obtain ⟨hU₃, hF₃, hFT₃⟩ := conj_dilation x hx Γ a₀ U hU
        have h := h3 _ hU₃ (by rw [hF₃, hFU, hK])
        rw [hFT₃] at h
        convert h using 2
        ext i j; simp [Matrix.submatrix_apply, Matrix.of_apply]
      · refine ⟨π, τ, Or.inr (Or.inr (Or.inl fun U hU hFU => ?_))⟩
        obtain ⟨hU₃, hF₃, hFT₃⟩ := conj_dilation x hx Γ a₀ U hU
        have h := h4 _ hU₃ (by rw [hF₃, hFU, hK])
        rw [hFT₃] at h
        convert h using 2
        ext i j; simp [Matrix.submatrix_apply, Matrix.of_apply]
    · -- the first token is the transpose, taken through an admissible dilation `U₀` of `G`
      obtain ⟨U₀, hU₀, hFU₀, hK1⟩ := hK
      rw [h0] at hFU₀
      have hT₀ := transpose_admissible x hx Γ hΓs a₀ U₀ hU₀
      obtain ⟨U₂, hU₂, hF₂, hE₂⟩ :=
        transpose_descends x hx Γ a₀ U₀ᵀ hT₀ (c 1) (gramPhaseEquiv_symm hK1)
      rw [Matrix.transpose_transpose, hFU₀] at hE₂
      have hKr : RealizableGram A Γ (c 1) := by
        rw [← hF₂]; exact sh1_necessity hU₂
      obtain ⟨π, τ, hsh⟩ := ih (c 1) hKr hchain
      -- for every dilation `U` of `G`, `c 1` is phase-equivalent to `FibreGram a₀ Uᵀ`
      have hc1 : ∀ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ U = G →
          GramPhaseEquiv (c 1) (FibreGram a₀ Uᵀ) := fun U hU hFU =>
        gramPhaseEquiv_trans hK1
          (transpose_single_valued x hx Γ hΓne a₀ U₀ U hU₀ hU (hFU₀.trans hFU.symm))
      rcases hsh with h1 | h2 | h3 | h4
      · refine ⟨π, τ, Or.inr (Or.inr (Or.inl fun U hU hFU => ?_))⟩
        exact gramPhaseEquiv_trans h1 (relabel2_gramPhaseEquiv π τ (hc1 U hU hFU))
      · refine ⟨π, τ, Or.inr (Or.inr (Or.inr fun U hU hFU => ?_))⟩
        exact gramPhaseEquiv_trans h2 (conj_gramPhaseEquiv (relabel2_gramPhaseEquiv π τ (hc1 U hU hFU)))
      · refine ⟨π, τ, Or.inl ?_⟩
        exact gramPhaseEquiv_trans (h3 U₂ hU₂ hF₂)
          (relabel2_gramPhaseEquiv π τ (gramPhaseEquiv_symm hE₂))
      · refine ⟨π, τ, Or.inr (Or.inl ?_)⟩
        exact gramPhaseEquiv_trans (h4 U₂ hU₂ hF₂)
          (conj_gramPhaseEquiv (relabel2_gramPhaseEquiv π τ (gramPhaseEquiv_symm hE₂)))

/-! #### The assembled verdict theorem of `ISO1` -/

/-- **`ISO1` — the verdict theorem**, the conjuncts (i)–(x) of the freeze at an arbitrary finite
carrier, a one-element ancilla and a constant symmetric visible family with no vanishing entry:
(i) the independent relabellings preserve realizability, (ii) descend, (iii) are isometries; (iv)
the conjugation is an isometry; (v) the transpose of an admissible dilation is admissible; (vi)
every realizable tuple has an admissible dilation; (vii) two dilations of one tuple have
phase-equivalent transposed fibre-Gram tuples; (viii) a dilation of a phase-equivalent tuple
exists whose transposed fibre-Gram tuple is phase-equivalent; (ix) the transpose is an isometry;
(x) the six relations of the normal form — `T ∘ (π, τ) = (τ, π) ∘ T`, `T ∘ C = C ∘ T`,
`T ∘ T = id`, `C ∘ C = id`, `C ∘ (π, τ) = (π, τ) ∘ C`, `(π, τ) ∘ (π', τ') = (π.trans π', τ.trans
τ')` — each on classes, the transpose written by its relation; and, as the sixteenth conjunct,
the four-shape normal form for every word in the generators, `iso1_word_normal_form`. -/
theorem iso1_family_acts :
    (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] (Γ : Matrix W W ℝ),
        (∀ i j i' j', Γ i j = Γ i' j') → ∀ (π τ : Equiv.Perm W) (G : W → Matrix W W ℂ),
        RealizableGram A Γ G → RealizableGram A Γ (fun i => (G (π i)).submatrix τ τ))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (π τ : Equiv.Perm W) (G G' : W → Matrix W W ℂ),
        GramPhaseEquiv G G' →
        GramPhaseEquiv (fun i => (G (π i)).submatrix τ τ) (fun i => (G' (π i)).submatrix τ τ))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ (π τ : Equiv.Perm W) (G H : W → Matrix W W ℂ),
        d (fun i => (G (π i)).submatrix τ τ) (fun i => (H (π i)).submatrix τ τ) = d G H)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ G H : W → Matrix W W ℂ,
        d (fun i => Matrix.of fun j k => star (G i j k))
          (fun i => Matrix.of fun j k => star (H i j k)) = d G H)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j, Γ i j = Γ j i) →
        ∀ (a₀ : A) (U : Matrix (W × A) (W × A) ℂ),
        AdmissibleDilationAt Γ a₀ U → AdmissibleDilationAt Γ a₀ Uᵀ)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A]
        (Γ : Matrix W W ℝ) (a₀ : A) (G : W → Matrix W W ℂ), RealizableGram A Γ G →
        ∃ U : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U ∧ FibreGram a₀ U = G)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j, Γ i j ≠ 0) →
        ∀ (a₀ : A) (U U' : Matrix (W × A) (W × A) ℂ),
        AdmissibleDilationAt Γ a₀ U → AdmissibleDilationAt Γ a₀ U' →
        FibreGram a₀ U = FibreGram a₀ U' →
        GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ) (a₀ : A) (U : Matrix (W × A) (W × A) ℂ),
        AdmissibleDilationAt Γ a₀ U → ∀ G' : W → Matrix W W ℂ,
        GramPhaseEquiv (FibreGram a₀ U) G' →
        ∃ U' : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U' ∧ FibreGram a₀ U' = G'
          ∧ GramPhaseEquiv (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A],
        Fintype.card A = 1 → ∀ (a₀ : A) (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ U U' : Matrix (W × A) (W × A) ℂ,
        d (FibreGram a₀ Uᵀ) (FibreGram a₀ U'ᵀ) = d (FibreGram a₀ U) (FibreGram a₀ U'))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j i' j', Γ i j = Γ i' j') →
        (∀ i j, Γ i j ≠ 0) → ∀ (a₀ : A) (π τ : Equiv.Perm W) (U : Matrix (W × A) (W × A) ℂ),
        AdmissibleDilationAt Γ a₀ U → ∀ U'' : Matrix (W × A) (W × A) ℂ,
        AdmissibleDilationAt Γ a₀ U'' →
        FibreGram a₀ U'' = (fun i => (FibreGram a₀ U (π i)).submatrix τ τ) →
        GramPhaseEquiv (FibreGram a₀ U''ᵀ) (fun i => (FibreGram a₀ Uᵀ (τ i)).submatrix π π))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j, Γ i j ≠ 0) →
        ∀ (a₀ : A) (U : Matrix (W × A) (W × A) ℂ), AdmissibleDilationAt Γ a₀ U →
        ∀ U'' : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U'' →
        FibreGram a₀ U'' = (fun i => Matrix.of fun j k => star (FibreGram a₀ U i j k)) →
        GramPhaseEquiv (FibreGram a₀ U''ᵀ)
          (fun i => Matrix.of fun j k => star (FibreGram a₀ Uᵀ i j k)))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j, Γ i j = Γ j i) → (∀ i j, Γ i j ≠ 0) →
        ∀ (a₀ : A) (U : Matrix (W × A) (W × A) ℂ), AdmissibleDilationAt Γ a₀ U →
        ∀ U'' : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U'' →
        FibreGram a₀ U'' = FibreGram a₀ Uᵀ →
        GramPhaseEquiv (FibreGram a₀ U''ᵀ) (FibreGram a₀ U))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (G : W → Matrix W W ℂ),
        (fun i => Matrix.of fun j k =>
          star ((fun i => Matrix.of fun j k => star (G i j k)) i j k)) = G)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (π τ : Equiv.Perm W) (G : W → Matrix W W ℂ),
        (fun i => Matrix.of fun j k => star ((fun i => (G (π i)).submatrix τ τ) i j k))
          = fun i => ((fun i => Matrix.of fun j k => star (G i j k)) (π i)).submatrix τ τ)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (π τ π' τ' : Equiv.Perm W)
        (G : W → Matrix W W ℂ),
        (fun i => ((fun i => (G (π' i)).submatrix τ' τ') (π i)).submatrix τ τ)
          = fun i => (G ((π.trans π') i)).submatrix (τ.trans τ') (τ.trans τ'))
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (A : Type) [Fintype A] [DecidableEq A],
        Fintype.card A = 1 → ∀ (Γ : Matrix W W ℝ), (∀ i j i' j', Γ i j = Γ i' j') →
        (∀ i j, Γ i j ≠ 0) → ∀ (a₀ : A) (w : List ((Equiv.Perm W × Equiv.Perm W) ⊕ (Unit ⊕ Unit)))
        (G H : W → Matrix W W ℂ), RealizableGram A Γ G →
        (∃ c : ℕ → (W → Matrix W W ℂ), c 0 = G ∧ c w.length = H ∧
          ∀ (n : ℕ) (hn : n < w.length),
            match w[n]'hn with
            | Sum.inl ⟨π, τ⟩ => c (n + 1) = fun i => (c n (π i)).submatrix τ τ
            | Sum.inr (Sum.inl _) => c (n + 1) = fun i => Matrix.of fun j k => star (c n i j k)
            | Sum.inr (Sum.inr _) => ∃ U : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U
                ∧ FibreGram a₀ U = c n ∧ GramPhaseEquiv (c (n + 1)) (FibreGram a₀ Uᵀ)) →
        ∃ π τ : Equiv.Perm W,
            GramPhaseEquiv H (fun i => (G (π i)).submatrix τ τ)
          ∨ GramPhaseEquiv H (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k))
          ∨ (∀ U : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ U = G →
              GramPhaseEquiv H (fun i => (FibreGram a₀ Uᵀ (π i)).submatrix τ τ))
          ∨ (∀ U : Matrix (W × A) (W × A) ℂ, AdmissibleDilationAt Γ a₀ U → FibreGram a₀ U = G →
              GramPhaseEquiv H (fun i => Matrix.of fun j k =>
                star ((FibreGram a₀ Uᵀ (π i)).submatrix τ τ j k)))) := by
  refine ⟨fun W _ _ A _ Γ hΓ π τ G hG => relabel2_realizable Γ hΓ π τ G hG,
    fun W _ _ π τ G G' h => relabel2_gramPhaseEquiv π τ h,
    fun W _ _ d hd π τ G H => relabel2_isometry d hd π τ G H,
    fun W _ _ d hd G H => conj_isometry d hd G H,
    fun W _ _ A _ _ hA Γ hΓ a₀ U hU => ?_,
    fun W _ _ A _ _ Γ a₀ G hG => sh1_sufficiency a₀ hG,
    fun W _ _ A _ _ hA Γ hΓ a₀ U U' hU hU' h => ?_,
    fun W _ _ A _ _ hA Γ a₀ U hU G' h => ?_,
    fun W _ _ A _ hA a₀ d hd U U' => ?_,
    fun W _ _ A _ _ hA Γ hΓ hΓne a₀ π τ U hU U'' hU'' h => ?_,
    fun W _ _ A _ _ hA Γ hΓne a₀ U hU U'' hU'' h => ?_,
    fun W _ _ A _ _ hA Γ hΓs hΓne a₀ U hU U'' hU'' h => ?_,
    fun W _ _ G => conj_conj G,
    fun W _ _ π τ G => conj_relabel2 π τ G,
    fun W _ _ π τ π' τ' G => relabel2_relabel2 π τ π' τ' G,
    fun W _ _ A _ _ hA Γ hΓ hΓne a₀ w G H hG hw => ?_⟩
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    exact transpose_admissible x hx Γ hΓ a₀ U hU
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    exact transpose_single_valued x hx Γ hΓ a₀ U U' hU hU' h
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    exact transpose_descends x hx Γ a₀ U hU G' h
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    exact transpose_isometry x hx a₀ d hd U U'
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    obtain ⟨hW, hF, hFT⟩ := relabel2_dilation x hx Γ hΓ a₀ π τ U hU
    rw [← hFT]
    exact transpose_single_valued x hx Γ hΓne a₀ U'' _ hU'' hW (h.trans hF.symm)
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    obtain ⟨hW, hF, hFT⟩ := conj_dilation x hx Γ a₀ U hU
    rw [← hFT]
    exact transpose_single_valued x hx Γ hΓne a₀ U'' _ hU'' hW (h.trans hF.symm)
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    have hT := transpose_admissible x hx Γ hΓs a₀ U hU
    have := transpose_single_valued x hx Γ hΓne a₀ U'' Uᵀ hU'' hT h
    rw [Matrix.transpose_transpose] at this
    exact this
  · obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
    exact iso1_word_normal_form x hx Γ hΓ hΓne a₀ w G H hG hw

/-- **`ISO1` (xi) at the single-carrier configuration**: the hypotheses of every conjunct of
`iso1_family_acts` are discharged at `V = Fin 4`, `A = Fin 1`, `Γ₀ ≡ ¼`, and the action facts
are restated there. -/
theorem iso1_single_carrier (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    (∀ (π τ : Equiv.Perm (Fin 4)) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (fun i => (G (π i)).submatrix τ τ))
    ∧ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
        RealizableGram (Fin 1) Γ₀ (fun i => Matrix.of fun j k => star (G i j k)))
    ∧ (∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) Uᵀ ∧ RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) Uᵀ))
    ∧ (∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
        ∃ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
          AdmissibleDilationAt Γ₀ (0 : Fin 1) U ∧ FibreGram (0 : Fin 1) U = G)
    ∧ (∀ U U' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
        AdmissibleDilationAt Γ₀ (0 : Fin 1) U → AdmissibleDilationAt Γ₀ (0 : Fin 1) U' →
        FibreGram (0 : Fin 1) U = FibreGram (0 : Fin 1) U' →
        GramPhaseEquiv (FibreGram (0 : Fin 1) Uᵀ) (FibreGram (0 : Fin 1) U'ᵀ))
    ∧ (∀ d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ,
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        (∀ (π τ : Equiv.Perm (Fin 4)) (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
          d (fun i => (G (π i)).submatrix τ τ) (fun i => (H (π i)).submatrix τ τ) = d G H)
        ∧ (∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
          d (fun i => Matrix.of fun j k => star (G i j k))
            (fun i => Matrix.of fun j k => star (H i j k)) = d G H)
        ∧ (∀ U U' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
          d (FibreGram (0 : Fin 1) Uᵀ) (FibreGram (0 : Fin 1) U'ᵀ)
            = d (FibreGram (0 : Fin 1) U) (FibreGram (0 : Fin 1) U'))) := by
  have hc : ∀ i j i' j', Γ₀ i j = Γ₀ i' j' := fun i j i' j' => by rw [hΓ₀]; rfl
  have hs : ∀ i j, Γ₀ i j = Γ₀ j i := fun i j => hc i j j i
  have hne : ∀ i j, Γ₀ i j ≠ 0 := fun i j => by rw [hΓ₀]; simp
  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  refine ⟨fun π τ G hG => relabel2_realizable Γ₀ hc π τ G hG,
    fun G hG => realizable_conj Γ₀ G hG, fun U hU => ⟨transpose_admissible 0 hx Γ₀ hs 0 U hU,
      sh1_necessity (transpose_admissible 0 hx Γ₀ hs 0 U hU)⟩,
    fun G hG => sh1_sufficiency 0 hG,
    fun U U' hU hU' h => transpose_single_valued 0 hx Γ₀ hne 0 U U' hU hU' h,
    fun d hd => ⟨fun π τ G H => relabel2_isometry d hd π τ G H,
      fun G H => conj_isometry d hd G H, fun U U' => transpose_isometry 0 hx 0 d hd U U'⟩⟩

/-- **`ISO1` (xi) at the product configuration**: the same at `V = Fin 4 × Fin 4`,
`A = Fin 1 × Fin 1`, `Γ ≡ 1/16 = Γ₀ ⊗ Γ₀`, anchor `(0, 0)`. -/
theorem iso1_product_carrier (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
    (hΓ : Γ = Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) :
    (∀ (π τ : Equiv.Perm (Fin 4 × Fin 4)) (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
        RealizableGram (Fin 1 × Fin 1) Γ G →
        RealizableGram (Fin 1 × Fin 1) Γ (fun i => (G (π i)).submatrix τ τ))
    ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
        RealizableGram (Fin 1 × Fin 1) Γ G →
        RealizableGram (Fin 1 × Fin 1) Γ (fun i => Matrix.of fun j k => star (G i j k)))
    ∧ (∀ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
        AdmissibleDilationAt Γ ((0 : Fin 1), (0 : Fin 1)) U →
        AdmissibleDilationAt Γ ((0 : Fin 1), (0 : Fin 1)) Uᵀ
          ∧ RealizableGram (Fin 1 × Fin 1) Γ (FibreGram ((0 : Fin 1), (0 : Fin 1)) Uᵀ))
    ∧ (∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
        RealizableGram (Fin 1 × Fin 1) Γ G →
        ∃ U : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
          AdmissibleDilationAt Γ ((0 : Fin 1), (0 : Fin 1)) U
            ∧ FibreGram ((0 : Fin 1), (0 : Fin 1)) U = G)
    ∧ (∀ U U' : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
        AdmissibleDilationAt Γ ((0 : Fin 1), (0 : Fin 1)) U →
        AdmissibleDilationAt Γ ((0 : Fin 1), (0 : Fin 1)) U' →
        FibreGram ((0 : Fin 1), (0 : Fin 1)) U = FibreGram ((0 : Fin 1), (0 : Fin 1)) U' →
        GramPhaseEquiv (FibreGram ((0 : Fin 1), (0 : Fin 1)) Uᵀ)
          (FibreGram ((0 : Fin 1), (0 : Fin 1)) U'ᵀ))
    ∧ (∀ d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
          → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ,
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        (∀ (π τ : Equiv.Perm (Fin 4 × Fin 4))
          (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          d (fun i => (G (π i)).submatrix τ τ) (fun i => (H (π i)).submatrix τ τ) = d G H)
        ∧ (∀ G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
          d (fun i => Matrix.of fun j k => star (G i j k))
            (fun i => Matrix.of fun j k => star (H i j k)) = d G H)
        ∧ (∀ U U' : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
          d (FibreGram ((0 : Fin 1), (0 : Fin 1)) Uᵀ) (FibreGram ((0 : Fin 1), (0 : Fin 1)) U'ᵀ)
            = d (FibreGram ((0 : Fin 1), (0 : Fin 1)) U)
                (FibreGram ((0 : Fin 1), (0 : Fin 1)) U'))) := by
  have hc : ∀ i j i' j', Γ i j = Γ i' j' := fun i j i' j' => by rw [hΓ, hΓ₀]; rfl
  have hs : ∀ i j, Γ i j = Γ j i := fun i j => hc i j j i
  have hne : ∀ i j, Γ i j ≠ 0 := fun i j => by rw [hΓ, hΓ₀]; simp
  have hx : ∀ y : Fin 1 × Fin 1, y = ((0 : Fin 1), (0 : Fin 1)) := fun y => Subsingleton.elim _ _
  refine ⟨fun π τ G hG => relabel2_realizable Γ hc π τ G hG,
    fun G hG => realizable_conj Γ G hG, fun U hU => ⟨transpose_admissible _ hx Γ hs _ U hU,
      sh1_necessity (transpose_admissible _ hx Γ hs _ U hU)⟩,
    fun G hG => sh1_sufficiency _ hG,
    fun U U' hU hU' h => transpose_single_valued _ hx Γ hne _ U U' hU hU' h,
    fun d hd => ⟨fun π τ G H => relabel2_isometry d hd π τ G H,
      fun G H => conj_isometry d hd G H, fun U U' => transpose_isometry _ hx _ d hd U U'⟩⟩

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms mixedTriple_relabel2
#print axioms fibreGram_unique
#print axioms mixedTriple_transpose
#print axioms rows_phase
#print axioms transpose_admissible
#print axioms antipodal
#print axioms dephase
#print axioms fourier_entry_monomial
#print axioms relabel2_realizable
#print axioms relabel2_gramPhaseEquiv
#print axioms relabel2_isometry
#print axioms conj_isometry
#print axioms transpose_single_valued
#print axioms transpose_unitary
#print axioms transpose_descends
#print axioms transpose_isometry
#print axioms relabel2_dilation
#print axioms conj_dilation
#print axioms conj_relabel2
#print axioms relabel2_relabel2
#print axioms iso1_word_normal_form
#print axioms iso1_family_acts
#print axioms iso1_single_carrier
#print axioms iso1_product_carrier

end OrbitGeometryIsometries
end OIBridge
