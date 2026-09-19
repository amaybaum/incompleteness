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

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms mixedTriple_relabel2
#print axioms fibreGram_unique
#print axioms mixedTriple_transpose
#print axioms rows_phase
#print axioms transpose_admissible
#print axioms antipodal
#print axioms dephase
#print axioms fourier_entry_monomial

end OrbitGeometryIsometries
end OIBridge
