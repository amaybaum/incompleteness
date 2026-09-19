import OIBridge.OrbitLawGaps
import OIBridge.OrbitLawRigidityTwisted
import OIBridge.OrbitLawNaturalityFactorization

/-!
# Act 24 — the orbit-geometry selector audit: complete phase invariants on the per-slice orbit space, the geometry they induce, its controls, the record's laws against it, and a gated rigidity attempt

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-24-orbit-geometry-selector/preregistration.md`,
blob `3b61d6c90fe3f05bbf5e791f74d7106e9be2f94a`, from `main` at
`d0fcdbc03c4b828d630f677253cf0914f451b63d` — the certified merge commit of that control plane, the
round's mandated execution base `B`, whose frozen blob this execution verified as its first act.

## What this round is

A **gated round**: four targets frozen together — `GEO1` the mixed-triple feature map and the
geometry it induces, `GEO2` its three controls, `GEO3` the record's twelve transition families
against it, `GEO4` a bounded rigidity attempt with five implication cells — executed in the fixed
order `GEO1` → `GEO2` → `GEO3` → `GEO4`, each later target opened only if the earlier ones reach
the label the freeze's gate names, with one verdict commit per executed target.

**The definition budget is one.** This module introduces exactly one top-level definition,
`mixedTriple`, with the body the freeze displays; everything else — the geometry, the isometry
proposition, every rung as act 21's declaration consumed, the twelve families, the Fourier family,
the sequence and its rotation — is a bound variable pinned by an equation in the statement that
needs it. Every other object is the merged record's own, consumed unmodified at merged strength —
act 12's `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `gramPhaseEquiv_cross_invariant`,
`sh1_sufficiency`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`; act 13's
`WeakAnchorStabilizer`; act 18's `ProperAt` and `PropagatesFrom`; act 20's `RelabelTransition`
and `TwistedNatural`; act 21's ladder declarations and product-embedding results; act 22's
`Φ_swap`; act 23's four families and its shared lemmas. **A merged statement is not enlarged by
being consumed.**

**This module's first commit carries Section A only** — the one definition and the shared lemmas
that answer no target by themselves: the invariance of every coordinate of the feature map under
act 12's phase action, the coordinate bound on the induced distance, the cross-invariant
coordinates, the entry and coordinate bounds on the Fourier family at a unit parameter with its
feature norm, the two distance identities of the Pythagorean sequence, the sixteen cross-invariants
of `G(Hᵢ)`, and the coordinatewise conjugation identity. Each verdict enters in its own later
commit, in the frozen order.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 24 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
namespace OrbitGeometrySelector

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps

/-! ### Section A — the one definition and the shared lemmas, before any verdict

None of these is a verdict of any target, and none names any of the twelve families. -/

variable {V : Type}

/-- **THE MIXED-TRIPLE FEATURE MAP** — the one budgeted definition of act 24. A coordinate is
three fibre labels `(i₁, i₂, i₃)` and three matrix indices `(j₁, j₂, j₃)`, and its value is the
product of three Gram entries around the closed walk `j₁ → j₂ → j₃ → j₁`, each factor read in its
own fibre: `G i₁ j₁ j₂ * G i₂ j₂ j₃ * G i₃ j₃ j₁`. Repeated indices are allowed: at `(j, j, j)` the
value is a product of diagonal entries, at `(j, j, k)` with one fibre it carries the squared
modulus of an entry, and at `(i₁, i₁, i₀)` with labels `(i₁, i₀, i₁)` it is the diagonal times act
12's cross-invariant at the fibre pair `(i₀, i₁)`. The body is the one the freeze displays, and the
guard pins it verbatim. -/
def mixedTriple (G : V → Matrix V V ℂ) : (V × V × V) × (V × V × V) → ℂ :=
  fun p => G p.1.1 p.2.1 p.2.2.1 * G p.1.2.1 p.2.2.1 p.2.2.2 * G p.1.2.2 p.2.2.2 p.2.1

variable [Fintype V] [DecidableEq V]

omit [Fintype V] [DecidableEq V] in
/-- **Every coordinate is invariant under act 12's phase action**: under
`H i j k = star (c j) * G i j k * c k` each factor of a coordinate picks up `star (c jₐ) … c j_b`,
and around the closed walk every `c j` meets its own `star`. -/
theorem mixedTriple_gauge {G H : V → Matrix V V ℂ} (h : GramPhaseEquiv G H) :
    mixedTriple H = mixedTriple G := by
  obtain ⟨c, hc, hH⟩ := h
  have u : ∀ j, c j * star (c j) = 1 := fun j => by
    rw [mul_comm, star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  funext p
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, hH]
  calc star (c j₁) * G i₁ j₁ j₂ * c j₂ * (star (c j₂) * G i₂ j₂ j₃ * c j₃)
        * (star (c j₃) * G i₃ j₃ j₁ * c j₁)
      = (G i₁ j₁ j₂ * G i₂ j₂ j₃ * G i₃ j₃ j₁)
          * ((c j₁ * star (c j₁)) * (c j₂ * star (c j₂)) * (c j₃ * star (c j₃))) := by ring
    _ = G i₁ j₁ j₂ * G i₂ j₂ j₃ * G i₃ j₃ j₁ := by rw [u, u, u]; ring

omit [Fintype V] [DecidableEq V] in
/-- **The cross-invariant coordinate**: at the coordinate `((i₁, i₀, i₁), (i₁, i₁, i₀))` the
feature map reads the diagonal entry `G i₁ i₁ i₁` times act 12's cross-invariant
`G i₀ i₁ i₀ * G i₁ i₀ i₁` at the fibre pair `(i₀, i₁)`. -/
theorem mixedTriple_cross (G : V → Matrix V V ℂ) (i₀ i₁ : V) :
    mixedTriple G ((i₁, i₀, i₁), (i₁, i₁, i₀)) = G i₁ i₁ i₁ * (G i₀ i₁ i₀ * G i₁ i₀ i₁) := by
  simp only [mixedTriple]
  ring

omit [Fintype V] [DecidableEq V] in
/-- **The coordinatewise conjugation identity**: the feature map of the entrywise conjugate is the
entrywise conjugate of the feature map. -/
theorem mixedTriple_star (G : V → Matrix V V ℂ) (p : (V × V × V) × (V × V × V)) :
    mixedTriple (fun i => Matrix.of fun j k => star (G i j k)) p = star (mixedTriple G p) := by
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, Matrix.of_apply, star_mul']

omit [DecidableEq V] in
/-- **The coordinate bound**: a coordinate of a Euclidean vector is bounded by its norm, so every
coordinate difference of two feature vectors is bounded by the induced distance, which is bound
here by the frozen equation. -/
theorem coord_le_dist (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) (p : (V × V × V) × (V × V × V)) :
    ‖mixedTriple G p - mixedTriple H p‖ ≤ d G H := by
  subst hd
  calc ‖mixedTriple G p - mixedTriple H p‖
      = Real.sqrt (‖mixedTriple G p - mixedTriple H p‖ ^ 2) :=
        (Real.sqrt_sq (norm_nonneg _)).symm
    _ ≤ Real.sqrt (∑ q, ‖mixedTriple G q - mixedTriple H q‖ ^ 2) :=
        Real.sqrt_le_sqrt (Finset.single_le_sum
          (f := fun q => ‖mixedTriple G q - mixedTriple H q‖ ^ 2)
          (fun q _ => sq_nonneg _) (Finset.mem_univ p))

/-- **The two distance identities of the Pythagorean sequence**, `zs n = (n + i)/(n − i)`:
`‖zs n − 1‖ ^ 2 = 4 / (n² + 1)` and `‖zs (n+1) − zs n‖ ^ 2 = 4 / ((n² + 1)((n+1)² + 1))`. -/
theorem zseq_dist (zs : ℕ → ℂ)
    (hzs : zs = fun n : ℕ => Complex.mk (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1))
      (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1))) :
    (∀ n : ℕ, ‖zs n - 1‖ ^ 2 = 4 / ((n : ℝ) ^ 2 + 1))
      ∧ ∀ n : ℕ, ‖zs (n + 1) - zs n‖ ^ 2
          = 4 / (((n : ℝ) ^ 2 + 1) * (((n : ℝ) + 1) ^ 2 + 1)) := by
  subst hzs
  have hpos : ∀ n : ℕ, (0 : ℝ) < (n : ℝ) ^ 2 + 1 := fun n => by positivity
  refine ⟨fun n => ?_, fun n => ?_⟩
  · rw [Complex.sq_norm, Complex.normSq_apply]
    have := hpos n
    simp only [Complex.sub_re, Complex.sub_im, Complex.one_re, Complex.one_im]
    field_simp
    ring
  · rw [Complex.sq_norm, Complex.normSq_apply]
    have h1 := hpos n
    have h2 := hpos (n + 1)
    simp only [Complex.sub_re, Complex.sub_im, Nat.cast_add, Nat.cast_one]
    field_simp
    ring

/-- **The sixteen cross-invariants of `G(Hᵢ)`** at every ordered fibre pair lie in
`{1/16, i/16}`: the diagonal pairs give the squared diagonal `1/16`, and the off-diagonal pairs
give `1/16` or `i/16` as act 21's `hadamard_entries` reads three of them. -/
theorem hadamard_i_cross_all (Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
    (hHᵢ : Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
        1, -Complex.I, -1, Complex.I] p.1 q.1)) :
    ∀ i₀ i₁ : Fin 4,
      FibreGram (0 : Fin 1) Hᵢ i₀ i₁ i₀ * FibreGram (0 : Fin 1) Hᵢ i₁ i₀ i₁ = 1 / 16
        ∨ FibreGram (0 : Fin 1) Hᵢ i₀ i₁ i₀ * FibreGram (0 : Fin 1) Hᵢ i₁ i₀ i₁
          = Complex.I / 16 := by
  subst hHᵢ
  intro i₀ i₁
  fin_cases i₀ <;> fin_cases i₁ <;>
    simp [fibreGram_apply, Complex.ext_iff] <;> norm_num

/-- **The cross-invariant of `G(H₁)` at every ordered fibre pair is `1/16`.** -/
theorem hadamard_one_cross_all (H₁ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
    (hH₁ : H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) :
    ∀ i₀ i₁ : Fin 4,
      FibreGram (0 : Fin 1) H₁ i₀ i₁ i₀ * FibreGram (0 : Fin 1) H₁ i₁ i₀ i₁ = 1 / 16 := by
  subst hH₁
  intro i₀ i₁
  fin_cases i₀ <;> fin_cases i₁ <;> simp [fibreGram_apply] <;> norm_num

/-- **The `(0,2)` cross-invariant of the Fourier family is parameter-free**: the rows `0` and `2`
of `H(z)` carry no `z`, so `F(z) 0 2 0 * F(z) 2 0 2 = 1/16` for every `z`. -/
theorem fibreGram_z_cross02 (z : ℂ) :
    FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) 0 2 0
      * FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) 2 0 2
      = 1 / 16 := by
  simp [fibreGram_apply]
  norm_num

/-- A unit parameter has norm one. -/
theorem norm_one_of_star_mul (z : ℂ) (hz : star z * z = 1) : ‖z‖ = 1 := by
  have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← star_mul_self_eq_norm_sq, hz]
  have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
  exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2

/-- The closing step of the entry bound: a difference that is `± (z' − z) / 4`, `± star (z' − z) / 4`
or `0` has norm at most `‖z' − z‖ / 4`. -/
theorem entry_bound_aux (z z' E : ℂ)
    (h : E * 4 = z' - z ∨ E * 4 = z - z' ∨ E * 4 = star (z' - z) ∨ E * 4 = star (z - z')
      ∨ E = 0) :
    ‖E‖ ≤ ‖z' - z‖ / 4 := by
  have h4 : ‖E‖ = ‖E * 4‖ / 4 := by
    rw [norm_mul]; norm_num
  rcases h with h | h | h | h | h
  · rw [h4, h]
  · rw [h4, h, ← norm_neg, neg_sub]
  · rw [h4, h, norm_star]
  · rw [h4, h, norm_star, ← norm_neg, neg_sub]
  · rw [h]; simp; positivity

/-- **Every entry of the Fourier family's fibre-Gram tuple at a unit parameter has modulus `¼`.** -/
theorem fourier_entry_norm (z : ℂ) (hz : star z * z = 1) (i j k : Fin 4) :
    ‖FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i j k‖
      = 1 / 4 := by
  have hn := norm_one_of_star_mul z hz
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [fibreGram_apply, norm_neg, hn] <;> norm_num

/-- **The entry bound on the Fourier family**: at unit parameters `z`, `z'`, every entry of
`F(z') − F(z)` has modulus at most `‖z' − z‖ / 4`; each entry of `F(z)` is one of `±¼`, `±z/4`,
`±star z/4`, the `z`-dependence cancelling where `z` pairs with `star z`. -/
theorem fourier_entry_diff (z z' : ℂ) (hz : star z * z = 1) (hz' : star z' * z' = 1)
    (i j k : Fin 4) :
    ‖FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1)) i j k
      - FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) i j k‖
      ≤ ‖z' - z‖ / 4 := by
  have hz1 : (starRingEnd ℂ) z * z = 1 := hz
  have hz1' : (starRingEnd ℂ) z' * z' = 1 := hz'
  apply entry_bound_aux
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [fibreGram_apply] <;>
    first
      | (left; ring1)
      | (right; left; ring1)
      | (right; right; left; ring1)
      | (right; right; right; left; ring1)
      | (right; right; right; right; linear_combination (1 / 4 : ℂ) * hz1' - (1 / 4 : ℂ) * hz1)
      | (right; right; right; right; linear_combination (-1 / 4 : ℂ) * hz1' + (1 / 4 : ℂ) * hz1)

/-- **The coordinate bound on the Fourier family**: at unit parameters every coordinate of
`Ψ (F(z')) − Ψ (F(z))` has modulus at most `3 ‖z' − z‖ / 64`, by the three-term product rule with
two factors of modulus `¼` and one entry difference of modulus at most `‖z' − z‖ / 4`. -/
theorem fourier_coord_diff (z z' : ℂ) (hz : star z * z = 1) (hz' : star z' * z' = 1)
    (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) :
    ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1))) p
      - mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p‖
      ≤ 3 * ‖z' - z‖ / 64 := by
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple]
  set F := FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
    (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) with hF
  set F' := FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
    (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1)) with hF'
  have na : ∀ i j k, ‖F i j k‖ = 1 / 4 := fun i j k => fourier_entry_norm z hz i j k
  have na' : ∀ i j k, ‖F' i j k‖ = 1 / 4 := fun i j k => fourier_entry_norm z' hz' i j k
  have nd : ∀ i j k, ‖F' i j k - F i j k‖ ≤ ‖z' - z‖ / 4 :=
    fun i j k => fourier_entry_diff z z' hz hz' i j k
  have e : F' i₁ j₁ j₂ * F' i₂ j₂ j₃ * F' i₃ j₃ j₁ - F i₁ j₁ j₂ * F i₂ j₂ j₃ * F i₃ j₃ j₁
      = (F' i₁ j₁ j₂ - F i₁ j₁ j₂) * F' i₂ j₂ j₃ * F' i₃ j₃ j₁
        + F i₁ j₁ j₂ * (F' i₂ j₂ j₃ - F i₂ j₂ j₃) * F' i₃ j₃ j₁
        + F i₁ j₁ j₂ * F i₂ j₂ j₃ * (F' i₃ j₃ j₁ - F i₃ j₃ j₁) := by ring
  rw [e]
  have hδ : 0 ≤ ‖z' - z‖ := norm_nonneg _
  calc ‖(F' i₁ j₁ j₂ - F i₁ j₁ j₂) * F' i₂ j₂ j₃ * F' i₃ j₃ j₁
        + F i₁ j₁ j₂ * (F' i₂ j₂ j₃ - F i₂ j₂ j₃) * F' i₃ j₃ j₁
        + F i₁ j₁ j₂ * F i₂ j₂ j₃ * (F' i₃ j₃ j₁ - F i₃ j₃ j₁)‖
      ≤ ‖(F' i₁ j₁ j₂ - F i₁ j₁ j₂) * F' i₂ j₂ j₃ * F' i₃ j₃ j₁‖
        + ‖F i₁ j₁ j₂ * (F' i₂ j₂ j₃ - F i₂ j₂ j₃) * F' i₃ j₃ j₁‖
        + ‖F i₁ j₁ j₂ * F i₂ j₂ j₃ * (F' i₃ j₃ j₁ - F i₃ j₃ j₁)‖ := norm_add₃_le
    _ = ‖F' i₁ j₁ j₂ - F i₁ j₁ j₂‖ * (1 / 4) * (1 / 4)
        + (1 / 4) * ‖F' i₂ j₂ j₃ - F i₂ j₂ j₃‖ * (1 / 4)
        + (1 / 4) * (1 / 4) * ‖F' i₃ j₃ j₁ - F i₃ j₃ j₁‖ := by
        simp only [norm_mul, na, na']
    _ ≤ (‖z' - z‖ / 4) * (1 / 4) * (1 / 4) + (1 / 4) * (‖z' - z‖ / 4) * (1 / 4)
        + (1 / 4) * (1 / 4) * (‖z' - z‖ / 4) := by
        have h1 := nd i₁ j₁ j₂
        have h2 := nd i₂ j₂ j₃
        have h3 := nd i₃ j₃ j₁
        nlinarith [norm_nonneg (F' i₁ j₁ j₂ - F i₁ j₁ j₂), norm_nonneg (F' i₂ j₂ j₃ - F i₂ j₂ j₃),
          norm_nonneg (F' i₃ j₃ j₁ - F i₃ j₃ j₁)]
    _ = 3 * ‖z' - z‖ / 64 := by ring

/-- **The feature norm of the Fourier family at a unit parameter is one**: every one of the `4096`
coordinates has modulus `1/64`, so the summed squared moduli equal `1` and their square root is
`1`. -/
theorem fourier_feature_norm (z : ℂ) (hz : star z * z = 1) :
    (∑ p, ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p‖ ^ 2)
        = 1
      ∧ Real.sqrt (∑ p, ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p‖ ^ 2)
        = 1 := by
  have h : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4),
      ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p‖ ^ 2
        = 1 / 4096 := by
    intro p
    obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
    simp only [mixedTriple, norm_mul, fourier_entry_norm z hz]
    norm_num
  have hsum : (∑ p, ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p‖ ^ 2)
        = 1 := by
    simp only [h, Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin,
      nsmul_eq_mul]
    norm_num
  exact ⟨hsum, by rw [hsum, Real.sqrt_one]⟩

/-! ### Section B — `GEO1`: completeness of the mixed triples, and the metric they induce

The conjuncts of the freeze's `GEO1`, each proved separately and assembled in `geo1_triple_metric`:
(i) invariance at every carrier; (ii) separation at every carrier under Hermitian fibres, equal
diagonals and a base-star support hypothesis, by the based gauge fixing; (iii) its instantiation on
the realizable tuples at the two frozen configurations, the support discharged from act 12's
sufficiency at `|A| = 1`; (iv) the metric properties of the induced distance, which is the
Euclidean norm of the feature difference; (v) class-invariance in both arguments; (vi-a) and
(vi-b) the two directions of the zero set, kept apart. The geometry is bound by the frozen
equation in every statement that names it. -/

omit [Fintype V] [DecidableEq V] in
/-- **`GEO1` (ii) — the based gauge fixing.** With Hermitian fibres on both sides, equal diagonals
and no vanishing entry on the base star `G j₀ j₀ ·`, equal feature vectors force a phase
equivalence: the coordinate `((j₀, j₀, j₀), (j₀, j₀, j))` gives `‖G j₀ j₀ j‖ = ‖H j₀ j₀ j‖`, so
`c j := H j₀ j₀ j / G j₀ j₀ j` has modulus one, and the based triangle `((j₀, i, j₀), (j₀, j, k))`
gives `H i j k = star (c j) * G i j k * c k`. -/
theorem geo1_separation_star (j₀ : V) (G H : V → Matrix V V ℂ)
    (hG : ∀ i, (G i).IsHermitian) (hH : ∀ i, (H i).IsHermitian)
    (hdiag : ∀ i j, G i j j = H i j j) (hsupp : ∀ j, G j₀ j₀ j ≠ 0)
    (hΨ : mixedTriple G = mixedTriple H) : GramPhaseEquiv G H := by
  have hGs : ∀ j, G j₀ j j₀ = star (G j₀ j₀ j) := fun j => ((hG j₀).apply j j₀).symm
  have hHs : ∀ j, H j₀ j j₀ = star (H j₀ j₀ j) := fun j => ((hH j₀).apply j j₀).symm
  -- the modulus step
  have hsq : ∀ j, star (G j₀ j₀ j) * G j₀ j₀ j = star (H j₀ j₀ j) * H j₀ j₀ j := by
    intro j
    have e := congrFun hΨ ((j₀, j₀, j₀), (j₀, j₀, j))
    simp only [mixedTriple] at e
    rw [hGs j, hHs j, hdiag j₀ j₀] at e
    have hδ : H j₀ j₀ j₀ ≠ 0 := by rw [← hdiag]; exact hsupp j₀
    have e' : H j₀ j₀ j₀ * (star (G j₀ j₀ j) * G j₀ j₀ j)
        = H j₀ j₀ j₀ * (star (H j₀ j₀ j) * H j₀ j₀ j) := by
      linear_combination e
    exact mul_left_cancel₀ hδ e'
  have hnorm : ∀ j, ‖H j₀ j₀ j‖ = ‖G j₀ j₀ j‖ := by
    intro j
    have e := hsq j
    rw [star_mul_self_eq_norm_sq, star_mul_self_eq_norm_sq] at e
    have e2 : ‖G j₀ j₀ j‖ ^ 2 = ‖H j₀ j₀ j‖ ^ 2 := by exact_mod_cast e
    exact ((pow_left_inj₀ (norm_nonneg _) (norm_nonneg _) two_ne_zero).mp e2).symm
  refine ⟨fun j => H j₀ j₀ j / G j₀ j₀ j, fun j => ?_, fun i j k => ?_⟩
  · rw [norm_div, hnorm, div_self (norm_ne_zero_iff.mpr (hsupp j))]
  · have e := congrFun hΨ ((j₀, i, j₀), (j₀, j, k))
    simp only [mixedTriple] at e
    rw [hGs, hHs] at e
    have hgj := hsupp j
    have hgk := hsupp k
    have hgk' : star (G j₀ j₀ k) ≠ 0 := star_ne_zero.mpr hgk
    have hgj' : star (G j₀ j₀ j) ≠ 0 := star_ne_zero.mpr hgj
    have h0 : (G j₀ j₀ j * star (G j₀ j₀ k))
        * (star (H j₀ j₀ j) * G i j k * H j₀ j₀ k - H i j k * (star (G j₀ j₀ j) * G j₀ j₀ k))
        = 0 := by
      linear_combination (star (H j₀ j₀ j) * H j₀ j₀ k) * e
        - (H i j k * star (G j₀ j₀ k) * G j₀ j₀ k) * hsq j
        - (H i j k * star (H j₀ j₀ j) * H j₀ j₀ j) * hsq k
    rcases mul_eq_zero.mp h0 with h1 | h1
    · exact absurd h1 (mul_ne_zero hgj hgk')
    · have h2 : star (H j₀ j₀ j) * G i j k * H j₀ j₀ k
          = H i j k * (star (G j₀ j₀ j) * G j₀ j₀ k) := sub_eq_zero.mp h1
      rw [star_div₀, div_mul_eq_mul_div, div_mul_div_comm, eq_div_iff (mul_ne_zero hgj' hgk)]
      exact h2.symm

/-- **The full-support fact at `|A| = 1`.** For a realizable tuple over a one-element ancilla with
a nowhere-vanishing visible family, act 12's sufficiency gives `G i j k = star (U (i,a) (j,a₀)) *
U (i,a) (k,a₀)` with `‖U (i,a) (j,a₀)‖ ^ 2 = Γ i j ≠ 0`, so no entry of `G` vanishes. -/
theorem realizable_entry_ne_zero {A : Type} [Fintype A] [DecidableEq A]
    (hA : Fintype.card A = 1) (Γ : Matrix V V ℝ) (hΓ : ∀ i j, Γ i j ≠ 0)
    (G : V → Matrix V V ℂ) (hG : RealizableGram A Γ G) (i j k : V) : G i j k ≠ 0 := by
  obtain ⟨x, hx⟩ := Fintype.card_eq_one_iff.mp hA
  obtain ⟨U, hU, hFU⟩ := sh1_sufficiency x hG
  have hsingle : ∀ f : A → ℂ, ∑ a, f a = f x :=
    fun f => Finset.sum_eq_single x (fun b _ hb => absurd (hx b) hb)
      (fun h => absurd (Finset.mem_univ x) h)
  have hsingleR : ∀ f : A → ℝ, ∑ a, f a = f x :=
    fun f => Finset.sum_eq_single x (fun b _ hb => absurd (hx b) hb)
      (fun h => absurd (Finset.mem_univ x) h)
  rw [← hFU, fibreGram_apply, hsingle]
  have h1 := hU.2 i j
  have h2 := hU.2 i k
  rw [hsingleR] at h1 h2
  apply mul_ne_zero
  · apply star_ne_zero.mpr
    intro h0
    apply hΓ i j
    rw [h1, h0]; simp
  · intro h0
    apply hΓ i k
    rw [h2, h0]; simp

/-- **`GEO1` (iii) at the single-carrier configuration**: realizable tuples at `Γ₀ ≡ ¼`,
`A = Fin 1` have Hermitian fibres, the diagonal `Γ₀` and no vanishing entry, so (ii) applies at
`j₀ = 0`. -/
theorem geo1_separation_single (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
    (hG : RealizableGram (Fin 1) Γ₀ G) (hH : RealizableGram (Fin 1) Γ₀ H)
    (hΨ : mixedTriple G = mixedTriple H) : GramPhaseEquiv G H := by
  have hΓ : ∀ i j, Γ₀ i j ≠ 0 := fun i j => by rw [hΓ₀]; simp
  refine geo1_separation_star 0 G H (fun i => (hG.1 i).1) (fun i => (hH.1 i).1)
    (fun i j => by rw [hG.2.2.2 i j, hH.2.2.2 i j]) (fun j => ?_) hΨ
  exact realizable_entry_ne_zero (by simp) Γ₀ hΓ G hG 0 0 j

/-- **`GEO1` (iii) at the product configuration**: realizable tuples at `Γ ≡ 1/16 = Γ₀ ⊗ Γ₀`,
`A = Fin 1 × Fin 1` have Hermitian fibres, the diagonal `Γ` and no vanishing entry, so (ii)
applies at `j₀ = (0, 0)`. -/
theorem geo1_separation_product (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
    (hΓ : Γ = Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
    (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
    (hG : RealizableGram (Fin 1 × Fin 1) Γ G) (hH : RealizableGram (Fin 1 × Fin 1) Γ H)
    (hΨ : mixedTriple G = mixedTriple H) : GramPhaseEquiv G H := by
  have hΓne : ∀ i j, Γ i j ≠ 0 := fun i j => by rw [hΓ, hΓ₀]; simp
  refine geo1_separation_star ((0 : Fin 4), (0 : Fin 4)) G H (fun i => (hG.1 i).1)
    (fun i => (hH.1 i).1) (fun i j => by rw [hG.2.2.2 i j, hH.2.2.2 i j]) (fun j => ?_) hΨ
  exact realizable_entry_ne_zero (by simp) Γ hΓne G hG _ _ j

omit [DecidableEq V] in
/-- **The induced distance is the Euclidean norm of the feature difference.** -/
theorem dist_eq_norm_toLp (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) :
    d G H = ‖(WithLp.toLp 2 (mixedTriple G) : EuclideanSpace ℂ ((V × V × V) × (V × V × V)))
      - WithLp.toLp 2 (mixedTriple H)‖ := by
  subst hd
  rw [EuclideanSpace.norm_eq]
  rfl

omit [DecidableEq V] in
/-- **`GEO1` (iv) — the metric properties**: nonnegativity, vanishing on the diagonal, symmetry
and the triangle inequality, those of a Euclidean norm. -/
theorem geo1_metric_props (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) :
    (∀ G H, 0 ≤ d G H) ∧ (∀ G, d G G = 0) ∧ (∀ G H, d G H = d H G)
      ∧ ∀ G H K, d G K ≤ d G H + d H K := by
  have e := dist_eq_norm_toLp d hd
  refine ⟨fun G H => ?_, fun G => ?_, fun G H => ?_, fun G H K => ?_⟩
  · rw [e]; exact norm_nonneg _
  · rw [e, sub_self, norm_zero]
  · rw [e, e, norm_sub_rev]
  · rw [e, e, e]
    calc ‖(WithLp.toLp 2 (mixedTriple G) : EuclideanSpace ℂ ((V × V × V) × (V × V × V)))
          - WithLp.toLp 2 (mixedTriple K)‖
        = ‖((WithLp.toLp 2 (mixedTriple G) : EuclideanSpace ℂ ((V × V × V) × (V × V × V)))
            - WithLp.toLp 2 (mixedTriple H))
          + (WithLp.toLp 2 (mixedTriple H) - WithLp.toLp 2 (mixedTriple K))‖ := by
          rw [sub_add_sub_cancel]
      _ ≤ _ := norm_add_le _ _

omit [DecidableEq V] in
/-- **`GEO1` (v) — class-invariance in both arguments**, from the coordinate invariance. -/
theorem geo1_class_invariant (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G G' H H' : V → Matrix V V ℂ) (hG : GramPhaseEquiv G G') (hH : GramPhaseEquiv H H') :
    d G H = d G' H' := by
  subst hd
  simp only [mixedTriple_gauge hG, mixedTriple_gauge hH]

omit [DecidableEq V] in
/-- **`GEO1` (vi-b) — the distance vanishes on phase-equivalent pairs.** -/
theorem geo1_zero_of_equiv (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) (h : GramPhaseEquiv G H) : d G H = 0 := by
  subst hd
  simp only [mixedTriple_gauge h, sub_self, norm_zero, ne_eq, OfNat.ofNat_ne_zero,
    not_false_eq_true, zero_pow, Finset.sum_const_zero, Real.sqrt_zero]

omit [DecidableEq V] in
/-- A vanishing distance forces equal feature vectors. -/
theorem features_eq_of_dist_zero (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) (h : d G H = 0) : mixedTriple G = mixedTriple H := by
  rw [dist_eq_norm_toLp d hd, norm_eq_zero, sub_eq_zero] at h
  exact congrArg WithLp.ofLp h

/-- **`GEO1` (vi-a) at the single-carrier configuration**: a vanishing distance between
realizable tuples forces phase equivalence. -/
theorem geo1_equiv_of_zero_single (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
    (hG : RealizableGram (Fin 1) Γ₀ G) (hH : RealizableGram (Fin 1) Γ₀ H) (h : d G H = 0) :
    GramPhaseEquiv G H :=
  geo1_separation_single Γ₀ hΓ₀ G H hG hH (features_eq_of_dist_zero d hd G H h)

/-- **`GEO1` (vi-a) at the product configuration.** -/
theorem geo1_equiv_of_zero_product (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
    (hΓ : Γ = Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
    (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
      → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
    (hG : RealizableGram (Fin 1 × Fin 1) Γ G) (hH : RealizableGram (Fin 1 × Fin 1) Γ H)
    (h : d G H = 0) : GramPhaseEquiv G H :=
  geo1_separation_product Γ₀ hΓ₀ Γ hΓ G H hG hH (features_eq_of_dist_zero d hd G H h)

/-- **`GEO1` — the verdict theorem**, the conjuncts (i)–(vi-b) of the freeze assembled: (i)
invariance at every carrier; (ii) separation at every carrier under Hermitian fibres, equal
diagonals and base-star support; (iii) separation on the realizable tuples at the single-carrier
and the product configuration; (iv) the metric properties; (v) class-invariance in both arguments;
(vi-a) a vanishing distance between realizable tuples at either configuration forces phase
equivalence; (vi-b) phase-equivalent tuples are at distance zero. The two directions of the zero
set are separate conjuncts. -/
theorem geo1_triple_metric :
    (∀ (W : Type) [Fintype W] [DecidableEq W] (G H : W → Matrix W W ℂ),
        GramPhaseEquiv G H → mixedTriple G = mixedTriple H)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W] (j₀ : W) (G H : W → Matrix W W ℂ),
        (∀ i, (G i).IsHermitian) → (∀ i, (H i).IsHermitian) → (∀ i j, G i j j = H i j j)
          → (∀ j, G j₀ j₀ j ≠ 0) → mixedTriple G = mixedTriple H → GramPhaseEquiv G H)
    ∧ (∀ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
        ∀ G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
          RealizableGram (Fin 1) Γ₀ H → mixedTriple G = mixedTriple H → GramPhaseEquiv G H)
    ∧ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
        Γ = (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        ∀ G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
          RealizableGram (Fin 1 × Fin 1) Γ G → RealizableGram (Fin 1 × Fin 1) Γ H →
          mixedTriple G = mixedTriple H → GramPhaseEquiv G H)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        (∀ G H, 0 ≤ d G H) ∧ (∀ G, d G G = 0) ∧ (∀ G H, d G H = d H G)
          ∧ ∀ G H K, d G K ≤ d G H + d H K)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ G G' H H', GramPhaseEquiv G G' → GramPhaseEquiv H H' → d G H = d G' H')
    ∧ (∀ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
        ∀ d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ,
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H →
          d G H = 0 → GramPhaseEquiv G H)
    ∧ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),
        Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
        Γ = (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        ∀ d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
          → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ,
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ G H, RealizableGram (Fin 1 × Fin 1) Γ G → RealizableGram (Fin 1 × Fin 1) Γ H →
          d G H = 0 → GramPhaseEquiv G H)
    ∧ (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ G H, GramPhaseEquiv G H → d G H = 0) := by
  refine ⟨fun W _ _ G H h => (mixedTriple_gauge h).symm,
    fun W _ _ j₀ G H hG hH hdiag hsupp hΨ => geo1_separation_star j₀ G H hG hH hdiag hsupp hΨ,
    fun Γ₀ hΓ₀ G H hG hH hΨ => geo1_separation_single Γ₀ hΓ₀ G H hG hH hΨ,
    fun Γ₀ Γ hΓ₀ hΓ G H hG hH hΨ => geo1_separation_product Γ₀ hΓ₀ Γ hΓ G H hG hH hΨ,
    fun W _ _ d hd => geo1_metric_props d hd,
    fun W _ _ d hd G G' H H' hG hH => geo1_class_invariant d hd G G' H H' hG hH,
    fun Γ₀ hΓ₀ d hd G H hG hH h => geo1_equiv_of_zero_single Γ₀ hΓ₀ d hd G H hG hH h,
    fun Γ₀ Γ hΓ₀ hΓ d hd G H hG hH h => geo1_equiv_of_zero_product Γ₀ hΓ₀ Γ hΓ d hd G H hG hH h,
    fun W _ _ d hd G H h => geo1_zero_of_equiv d hd G H h⟩

omit [Fintype V] [DecidableEq V] in
/-- **`GEO1-T`, the continuity half of the observation sub-question**: the feature map is
continuous, each coordinate being a product of three entries. The compactness half is not
attempted here. -/
theorem mixedTriple_continuous : Continuous (fun G : V → Matrix V V ℂ => mixedTriple G) := by
  apply continuous_pi
  intro p
  simp only [mixedTriple]
  fun_prop

/-! ### Section C — `GEO2`: the three controls

(a) every carrier relabelling is an exact isometry of the induced distance, the relabelling acting
on the feature map by a permutation of the index set; (b) act 12's two-sided gauge acts trivially,
by `fibreGram_left_mul` and `fibreGram_mul_weak_apply` and `GEO1` (vi-b); (c) the feature map
carries the product embedding to the tensor product of the factors' feature vectors, entry by
entry, so that the distance between two products with a common second factor is the factors'
distance scaled exactly by the common factor's feature norm. -/

omit [Fintype V] [DecidableEq V] in
/-- A relabelling acts on the feature map by the induced permutation of the index set. -/
theorem mixedTriple_relabel (σ : Equiv.Perm V) (G : V → Matrix V V ℂ)
    (p : (V × V × V) × (V × V × V)) :
    mixedTriple (RelabelTransition σ G) p
      = mixedTriple G (((σ p.1.1, σ p.1.2.1, σ p.1.2.2), (σ p.2.1, σ p.2.2.1, σ p.2.2.2))) := by
  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p
  simp only [mixedTriple, RelabelTransition, Matrix.submatrix_apply]

omit [DecidableEq V] in
/-- **`GEO2` (a) — every carrier relabelling is an exact isometry.** -/
theorem geo2_relabel_isometry (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (σ : Equiv.Perm V) (G H : V → Matrix V V ℂ) :
    d (RelabelTransition σ G) (RelabelTransition σ H) = d G H := by
  subst hd
  simp only [mixedTriple_relabel]
  congr 1
  exact Equiv.sum_comp ((σ.prodCongr (σ.prodCongr σ)).prodCongr (σ.prodCongr (σ.prodCongr σ)))
    (fun q => ‖mixedTriple G q - mixedTriple H q‖ ^ 2)

/-- **`GEO2` (b) — act 12's two-sided gauge acts trivially**: `L * U * K` for `L` in the left fibre
group and `K` a weak anchored stabilizer has fibre-Gram tuple phase-equivalent to `U`'s, so the two
are at distance zero. -/
theorem geo2_twoSided_trivial {A : Type} [Fintype A] [DecidableEq A] (a₀ : A)
    (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (U L K : Matrix (V × A) (V × A) ℂ) (hL : LeftFibreGroup L) (hK : WeakAnchorStabilizer a₀ K) :
    d (FibreGram a₀ (L * U * K)) (FibreGram a₀ U) = 0 := by
  obtain ⟨hKu, c, hc⟩ := hK
  have hnorm : ∀ j, ‖c j‖ = 1 := fun j => weak_anchor_coeff_norm_one hKu hc j
  have hequiv : GramPhaseEquiv (FibreGram a₀ (L * U * K)) (FibreGram a₀ U) := by
    refine ⟨fun j => star (c j), fun j => by rw [norm_star, hnorm], fun i j k => ?_⟩
    rw [fibreGram_mul_weak_apply hc, fibreGram_left_mul hL, star_star]
    have hj : c j * star (c j) = 1 := by
      rw [mul_comm, star_mul_self_eq_norm_sq, hnorm, one_pow, Complex.ofReal_one]
    have hk : star (c k) * c k = 1 := by
      rw [star_mul_self_eq_norm_sq, hnorm, one_pow, Complex.ofReal_one]
    calc FibreGram a₀ U i j k
        = FibreGram a₀ U i j k * ((c j * star (c j)) * (star (c k) * c k)) := by
          rw [hj, hk, one_mul, mul_one]
      _ = c j * (star (c j) * FibreGram a₀ U i j k * c k) * star (c k) := by ring
  exact geo1_zero_of_equiv d hd _ _ hequiv

/-- **`GEO2` (c), the identity**: a coordinate of the product carrier's feature map is the product
of the factors' coordinates, entry by entry. -/
theorem mixedTriple_product {V₁ V₂ : Type} (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ)
    (a₁ a₂ a₃ j₁ j₂ j₃ : V₁) (b₁ b₂ b₃ k₁ k₂ k₃ : V₂) :
    mixedTriple (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
        (((a₁, b₁), (a₂, b₂), (a₃, b₃)), ((j₁, k₁), (j₂, k₂), (j₃, k₃)))
      = mixedTriple X ((a₁, a₂, a₃), (j₁, j₂, j₃)) * mixedTriple Y ((b₁, b₂, b₃), (k₁, k₂, k₃)) := by
  simp only [mixedTriple, Matrix.of_apply]
  ring

/-- **`GEO2` (c), the consequence**: the distance between two products with a common second factor
is the factors' distance scaled exactly by the common factor's feature norm. -/
theorem geo2_product_tensor {V₁ V₂ : Type} [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
    (d₁ : (V₁ → Matrix V₁ V₁ ℂ) → (V₁ → Matrix V₁ V₁ ℂ) → ℝ)
    (hd₁ : d₁ = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (d : (V₁ × V₂ → Matrix (V₁ × V₂) (V₁ × V₂) ℂ) → (V₁ × V₂ → Matrix (V₁ × V₂) (V₁ × V₂) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (X X' : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ) :
    d (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
        (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X' i.1 j.1 k.1 * Y i.2 j.2 k.2)
      = d₁ X X' * Real.sqrt (∑ q, ‖mixedTriple Y q‖ ^ 2) := by
  subst hd hd₁
  -- the index bijection between product-carrier coordinates and pairs of factor coordinates
  let E : ((V₁ × V₂) × (V₁ × V₂) × (V₁ × V₂)) × ((V₁ × V₂) × (V₁ × V₂) × (V₁ × V₂))
      ≃ ((V₁ × V₁ × V₁) × (V₁ × V₁ × V₁)) × ((V₂ × V₂ × V₂) × (V₂ × V₂ × V₂)) :=
    { toFun := fun p => (((p.1.1.1, p.1.2.1.1, p.1.2.2.1), (p.2.1.1, p.2.2.1.1, p.2.2.2.1)),
        ((p.1.1.2, p.1.2.1.2, p.1.2.2.2), (p.2.1.2, p.2.2.1.2, p.2.2.2.2)))
      invFun := fun q => (((q.1.1.1, q.2.1.1), (q.1.1.2.1, q.2.1.2.1), (q.1.1.2.2, q.2.1.2.2)),
        ((q.1.2.1, q.2.2.1), (q.1.2.2.1, q.2.2.2.1), (q.1.2.2.2, q.2.2.2.2)))
      left_inv := fun _ => rfl
      right_inv := fun _ => rfl }
  have hsum : (∑ p, ‖mixedTriple (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
        X i.1 j.1 k.1 * Y i.2 j.2 k.2) p
        - mixedTriple (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
        X' i.1 j.1 k.1 * Y i.2 j.2 k.2) p‖ ^ 2)
      = (∑ q, ‖mixedTriple X q - mixedTriple X' q‖ ^ 2) * ∑ q, ‖mixedTriple Y q‖ ^ 2 := by
    rw [Finset.sum_mul_sum, ← Fintype.sum_prod_type']
    refine Fintype.sum_equiv E _ _ (fun p => ?_)
    obtain ⟨⟨⟨a₁, b₁⟩, ⟨a₂, b₂⟩, ⟨a₃, b₃⟩⟩, ⟨⟨j₁, k₁⟩, ⟨j₂, k₂⟩, ⟨j₃, k₃⟩⟩⟩ := p
    simp only [E, Equiv.coe_fn_mk]
    rw [mixedTriple_product, mixedTriple_product, ← sub_mul, norm_mul, mul_pow]
  beta_reduce
  rw [hsum, Real.sqrt_mul (Finset.sum_nonneg (fun q _ => sq_nonneg _))]

/-- **`GEO2` — the verdict theorem**: the three controls assembled. -/
theorem geo2_controls :
    (∀ (W : Type) [Fintype W] [DecidableEq W]
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ (σ : Equiv.Perm W) (G H : W → Matrix W W ℂ),
          d (RelabelTransition σ G) (RelabelTransition σ H) = d G H)
    ∧ (∀ (W A : Type) [Fintype W] [DecidableEq W] [Fintype A] [DecidableEq A] (a₀ : A)
        (d : (W → Matrix W W ℂ) → (W → Matrix W W ℂ) → ℝ),
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ (U L K : Matrix (W × A) (W × A) ℂ), LeftFibreGroup L → WeakAnchorStabilizer a₀ K →
          d (FibreGram a₀ (L * U * K)) (FibreGram a₀ U) = 0)
    ∧ (∀ (V₁ V₂ : Type) (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ)
        (a₁ a₂ a₃ j₁ j₂ j₃ : V₁) (b₁ b₂ b₃ k₁ k₂ k₃ : V₂),
        mixedTriple (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
            (((a₁, b₁), (a₂, b₂), (a₃, b₃)), ((j₁, k₁), (j₂, k₂), (j₃, k₃)))
          = mixedTriple X ((a₁, a₂, a₃), (j₁, j₂, j₃))
            * mixedTriple Y ((b₁, b₂, b₃), (k₁, k₂, k₃)))
    ∧ (∀ (V₁ V₂ : Type) [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
        (d₁ : (V₁ → Matrix V₁ V₁ ℂ) → (V₁ → Matrix V₁ V₁ ℂ) → ℝ),
        d₁ = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ d : (V₁ × V₂ → Matrix (V₁ × V₂) (V₁ × V₂) ℂ)
          → (V₁ × V₂ → Matrix (V₁ × V₂) (V₁ × V₂) ℂ) → ℝ,
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ (X X' : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ),
          d (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
              (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X' i.1 j.1 k.1 * Y i.2 j.2 k.2)
            = d₁ X X' * Real.sqrt (∑ q, ‖mixedTriple Y q‖ ^ 2)) :=
  ⟨fun _ _ _ d hd σ G H => geo2_relabel_isometry d hd σ G H,
    fun _ _ _ _ _ _ a₀ d hd U L K hL hK => geo2_twoSided_trivial a₀ d hd U L K hL hK,
    fun _ _ X Y a₁ a₂ a₃ j₁ j₂ j₃ b₁ b₂ b₃ k₁ k₂ k₃ =>
      mixedTriple_product X Y a₁ a₂ a₃ j₁ j₂ j₃ b₁ b₂ b₃ k₁ k₂ k₃,
    fun _ _ _ _ _ _ d₁ hd₁ d hd X X' Y => geo2_product_tensor d₁ hd₁ d hd X X' Y⟩

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms mixedTriple_gauge
#print axioms mixedTriple_cross
#print axioms mixedTriple_star
#print axioms coord_le_dist
#print axioms zseq_dist
#print axioms hadamard_i_cross_all
#print axioms hadamard_one_cross_all
#print axioms fibreGram_z_cross02
#print axioms norm_one_of_star_mul
#print axioms entry_bound_aux
#print axioms fourier_entry_norm
#print axioms fourier_entry_diff
#print axioms fourier_coord_diff
#print axioms fourier_feature_norm
#print axioms geo1_separation_star
#print axioms realizable_entry_ne_zero
#print axioms geo1_separation_single
#print axioms geo1_separation_product
#print axioms dist_eq_norm_toLp
#print axioms geo1_metric_props
#print axioms geo1_class_invariant
#print axioms geo1_zero_of_equiv
#print axioms features_eq_of_dist_zero
#print axioms geo1_equiv_of_zero_single
#print axioms geo1_equiv_of_zero_product
#print axioms geo1_triple_metric
#print axioms mixedTriple_continuous
#print axioms mixedTriple_relabel
#print axioms geo2_relabel_isometry
#print axioms geo2_twoSided_trivial
#print axioms mixedTriple_product
#print axioms geo2_product_tensor
#print axioms geo2_controls

end OrbitGeometrySelector
end OIBridge
