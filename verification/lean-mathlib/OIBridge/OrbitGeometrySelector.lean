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

/-! ### Section D — `GEO3`: the twelve families against the geometry

Each family in its own subsection, pinned to the equation its merged verdict carries, tested at
its own configuration for the isometry proposition — `∀ t G H, RealizableGram A (Γ t) G →
RealizableGram A (Γ t) H → d (Φ t G) (Φ t H) = d G H` — with `d` bound to the frozen equation.
The helpers of this section are consequences of the shared lemmas and of `GEO2`. -/

/-- The induced distance between two members of the Fourier family at unit parameters is at most
`3 ‖z' − z‖`: every one of the `4096` coordinate differences is at most `3 ‖z' − z‖ / 64`. -/
theorem fourier_dist_le
    (d₁ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
    (hd₁ : d₁ = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (z z' : ℂ) (hz : star z * z = 1) (hz' : star z' * z' = 1) :
    d₁ (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)))
      (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1)))
      ≤ 3 * ‖z' - z‖ := by
  subst hd₁
  have hb : ∀ p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4),
      ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p
        - mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1))) p‖ ^ 2
        ≤ (3 * ‖z' - z‖ / 64) ^ 2 := fun p => by
    rw [norm_sub_rev]
    exact pow_le_pow_left₀ (norm_nonneg _) (fourier_coord_diff z z' hz hz' p) 2
  calc Real.sqrt (∑ p, ‖mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))) p
        - mixedTriple (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z', -1, -z'; 1, -1, 1, -1; 1, -z', -1, z'] p.1 q.1))) p‖ ^ 2)
      ≤ Real.sqrt (∑ _p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4),
          (3 * ‖z' - z‖ / 64) ^ 2) :=
        Real.sqrt_le_sqrt (Finset.sum_le_sum fun p _ => hb p)
    _ = 3 * ‖z' - z‖ := by
        simp only [Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin,
          nsmul_eq_mul]
        rw [show ((4 * (4 * 4) * (4 * (4 * 4)) : ℕ) : ℝ) * (3 * ‖z' - z‖ / 64) ^ 2
            = (3 * ‖z' - z‖) ^ 2 by push_cast; ring]
        exact Real.sqrt_sq (by positivity)

/-- The product embedding of two admissible single-carrier dilations' fibre-Gram tuples is
realizable at the product configuration, by act 21's `product_realizable` and act 12's
`sh1_necessity`. -/
theorem realizable_prod_of_adm (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    {U₁ U₂ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (h₁ : AdmissibleDilationAt Γ₀ (0 : Fin 1) U₁) (h₂ : AdmissibleDilationAt Γ₀ (0 : Fin 1) U₂) :
    RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) U₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) U₂ i.2 j.2 k.2) := by
  obtain ⟨U, hU, hF⟩ := product_realizable h₁ h₂
  rw [← hF]
  exact sh1_necessity hU

/-- The cross-invariant coordinate of a product tuple, factorwise. -/
theorem coord_cross_product {V₁ V₂ : Type} (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ)
    (a₀ a₁ : V₁) (b₀ b₁ : V₂) :
    mixedTriple (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
        (((a₁, b₁), (a₀, b₀), (a₁, b₁)), ((a₁, b₁), (a₁, b₁), (a₀, b₀)))
      = (X a₁ a₁ a₁ * Y b₁ b₁ b₁) * ((X a₀ a₁ a₀ * X a₁ a₀ a₁) * (Y b₀ b₁ b₀ * Y b₁ b₀ b₁)) := by
  simp only [mixedTriple, Matrix.of_apply]
  ring

/-- `‖i − 1‖ ≥ 1`. -/
theorem one_le_norm_I_sub_one : (1 : ℝ) ≤ ‖Complex.I - 1‖ := by
  rw [← Real.sqrt_one, ← Real.sqrt_sq (norm_nonneg (Complex.I - 1))]
  apply Real.sqrt_le_sqrt
  rw [Complex.sq_norm, Complex.normSq_apply]
  simp

/-! #### `ΦI` — the identity, at the single-carrier configuration -/

/-- **`ΦI` is an isometry.** -/
theorem geo3_phiI_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
          (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Γ₀) → Φ = (fun _ G => G) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ t) G →
          RealizableGram (Fin 1) (Γ t) H → d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ _ t G H _ _ => ?_⟩
  subst hΦ
  rfl

/-! #### `ΦP` — the relabelling by `σ = (2 3)`, at the single-carrier configuration -/

/-- **`ΦP` is an isometry**, by `GEO2` (a). -/
theorem geo3_phiP_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
          (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Γ₀) → Φ = (fun _ G => RelabelTransition (Equiv.swap (2 : Fin 4) 3) G) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ t) G →
          RealizableGram (Fin 1) (Γ t) H → d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ hd t G H _ _ => ?_⟩
  subst hΦ
  exact geo2_relabel_isometry d hd _ G H

/-! #### `ΦC` — the constant transition to `G(H₁)`, at the single-carrier configuration -/

/-- **`ΦC` is not an isometry**: `G(H₁)` and `G(Hᵢ)` are realizable and both sent to `G(H₁)`,
so the images are at distance `0` while the inputs differ at the cross-invariant coordinate
`((1, 0, 1), (1, 1, 0))`, values `1/64` and `i/64`. -/
theorem geo3_phiC_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
            (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
          Γ = (fun _ => Γ₀) → Φ = (fun _ _ => FibreGram (0 : Fin 1) H₁) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ t) G →
            RealizableGram (Fin 1) (Γ t) H → d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ d hΓ hΦ hd hI => ?_⟩
  have hG₁ : RealizableGram (Fin 1) (Γ 0) (FibreGram (0 : Fin 1) H₁) := by
    rw [hΓ]; exact sh1_necessity hadm₁
  have hGᵢ : RealizableGram (Fin 1) (Γ 0) (FibreGram (0 : Fin 1) Hᵢ) := by
    rw [hΓ]; exact sh1_necessity hadmᵢ
  have e := hI 0 _ _ hG₁ hGᵢ
  rw [hΦ] at e
  simp only at e
  rw [(geo1_metric_props d hd).2.1] at e
  have v1 : mixedTriple (FibreGram (0 : Fin 1) H₁) (((1, 0, 1), (1, 1, 0))) = 1 / 64 := by
    rw [hH₁]; simp [mixedTriple, fibreGram_apply]; norm_num
  have v2 : mixedTriple (FibreGram (0 : Fin 1) Hᵢ) (((1, 0, 1), (1, 1, 0))) = Complex.I / 64 := by
    rw [hHᵢ]; simp [mixedTriple, fibreGram_apply]
    linear_combination (-Complex.I / 64 : ℂ) * Complex.I_mul_I
  have hb := coord_le_dist d hd (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ)
    (((1, 0, 1), (1, 1, 0)))
  rw [v1, v2, ← e] at hb
  have hpos : 0 < ‖(1 : ℂ) / 64 - Complex.I / 64‖ := by
    rw [norm_pos_iff]
    intro h0
    have := congrArg Complex.im h0
    simp at this
  linarith

/-! #### `ΦT` — the time-dependent relabelling, at the single-carrier configuration -/

/-- **`ΦT` is an isometry**: at each `t` the map is the identity or the relabelling by `σ`. -/
theorem geo3_phiT_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
          (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Γ₀) →
        Φ = (fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ t) G →
          RealizableGram (Fin 1) (Γ t) H → d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ hd t G H _ _ => ?_⟩
  subst hΦ
  by_cases h : Even t
  · simp only [if_pos h]
  · simp only [if_neg h]
    exact geo2_relabel_isometry d hd _ G H

/-! #### `ΦPP` — the product relabelling `σ × σ`, at the product configuration -/

/-- **`ΦPP` is an isometry**, by `GEO2` (a). -/
theorem geo3_phiPP_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        Φ = (fun _ G => RelabelTransition
          (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) G) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
          d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ hd t G H _ _ => ?_⟩
  subst hΦ
  exact geo2_relabel_isometry d hd _ G H

/-! #### `Φ_swap` — the exchange of the two factors, at the product configuration -/

/-- **`Φ_swap` is an isometry**, by `GEO2` (a). -/
theorem geo3_phiSwap_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        Φ = (fun _ G => RelabelTransition (Equiv.prodComm (Fin 4) (Fin 4)) G) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
          d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ hd t G H _ _ => ?_⟩
  subst hΦ
  exact geo2_relabel_isometry d hd _ G H

/-! #### `Φ_conj` — the entrywise conjugation, at the product configuration -/

/-- **`Φ_conj` is an isometry**: the feature map of the conjugate is the conjugate of the feature
map, and conjugation preserves every coordinate norm. -/
theorem geo3_phiConj_isometry :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        Φ = (fun _ G => fun i => Matrix.of fun j k => star (G i j k)) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
          d (Φ t G) (Φ t H) = d G H := by
  refine ⟨_, rfl, fun Γ Φ d _ hΦ hd t G H _ _ => ?_⟩
  subst hΦ hd
  have key : ∀ p, ‖mixedTriple (fun i => Matrix.of fun j k => star (G i j k)) p
      - mixedTriple (fun i => Matrix.of fun j k => star (H i j k)) p‖
      = ‖mixedTriple G p - mixedTriple H p‖ := fun p => by
    rw [mixedTriple_star, mixedTriple_star, ← star_sub, norm_star]
  simp only [key]

/-! #### `Φ_PC` — the partial collapse, at the product configuration -/

open Classical in
/-- **`Φ_PC` is not an isometry**: `G(Hᵢ) ⊠ G(H₁)` and `G(H₁) ⊠ G(H₁)` are realizable and both
sent to `G(H₁) ⊠ G(H₁)`, so the images are at distance `0` while the inputs are inequivalent by
act 23's `gap_separations` and therefore at positive distance by `GEO1` (vi-a). -/
theorem geo3_phiPC_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
            (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G =>
            if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              then (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
              else G) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
            d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ d hΓ hΦ hd hI => ?_⟩
  obtain ⟨_, _, hsep, _, _⟩ := gap_separations H₁ Hᵢ hH₁ hHᵢ
  have hG : RealizableGram (Fin 1 × Fin 1) (Γ 0) (fun i : Fin 4 × Fin 4 =>
      Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) := by
    rw [hΓ]; exact realizable_prod_of_adm Γ₀ hadmᵢ hadm₁
  have hH : RealizableGram (Fin 1 × Fin 1) (Γ 0) (fun i : Fin 4 × Fin 4 =>
      Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) := by
    rw [hΓ]; exact realizable_prod_of_adm Γ₀ hadm₁ hadm₁
  have e := hI 0 _ _ hG hH
  rw [hΦ] at e
  simp only [if_pos (gramPhaseEquiv_refl _), if_neg hsep] at e
  rw [(geo1_metric_props d hd).2.1] at e
  have hequiv := geo1_equiv_of_zero_product Γ₀ hΓ₀ (Γ 0) (by rw [hΓ]) d hd _ _ hG hH e.symm
  exact hsep (gramPhaseEquiv_symm hequiv)

/-! #### `Φ_MD` — the merge-then-drop transition, at the product configuration -/

open Classical in
/-- **`Φ_MD` is not an isometry**: at `t = 0` its map collapses `[G(Hᵢ) ⊠ G(H₁)]` onto
`G(H₁) ⊠ G(H₁)` and fixes every other tuple, so the pair `G(Hᵢ) ⊠ G(H₁)`, `G(H₁) ⊠ G(H₁)` — both
realizable, both sent to `G(H₁) ⊠ G(H₁)`, inequivalent by act 23's `gap_separations` — refutes it
at `t = 0` through `GEO1` (vi-a). -/
theorem geo3_phiMD_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
            (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun t G =>
            if t = 0 then
              (if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                then (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                else G)
            else
              (if GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                  FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2)
                then (fun _ : Fin 4 × Fin 4 => (0 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
                else G)) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
            d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ d hΓ hΦ hd hI => ?_⟩
  obtain ⟨_, _, hsep, _, _⟩ := gap_separations H₁ Hᵢ hH₁ hHᵢ
  have hG : RealizableGram (Fin 1 × Fin 1) (Γ 0) (fun i : Fin 4 × Fin 4 =>
      Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) := by
    rw [hΓ]; exact realizable_prod_of_adm Γ₀ hadmᵢ hadm₁
  have hH : RealizableGram (Fin 1 × Fin 1) (Γ 0) (fun i : Fin 4 × Fin 4 =>
      Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) := by
    rw [hΓ]; exact realizable_prod_of_adm Γ₀ hadm₁ hadm₁
  have e := hI 0 _ _ hG hH
  rw [hΦ] at e
  simp only [if_true, if_pos (gramPhaseEquiv_refl _), if_neg hsep] at e
  rw [(geo1_metric_props d hd).2.1] at e
  have hequiv := geo1_equiv_of_zero_product Γ₀ hΓ₀ (Γ 0) (by rw [hΓ]) d hd _ _ hG hH e.symm
  exact hsep (gramPhaseEquiv_symm hequiv)

/-! #### `ΦCTRL` — the class-conditional relabelling of the second factor, at the product
configuration -/

open Classical in
/-- **`ΦCTRL` is not an isometry**, by the perturbation pair at `t = 0` and `N = 32768`:
`G := G(H₁) ⊠ G(Hᵢ)` fires and is sent to `G(H₁) ⊠ σG(Hᵢ)`; `H := F(zs N) ⊠ G(Hᵢ)` does not fire
(the marginal lemma and `zs N ≠ 1`) and is fixed. The inputs are at distance
`d (G(H₁)) (F(zs N)) ≤ 3 ‖zs N − 1‖ < 1/4096` by `GEO2` (c), the feature norm and the entry
bound; the images differ at the cross-invariant coordinate of the product pair `((0,0),(0,2))`
by `‖i − 1‖/4096 ≥ 1/4096`. -/
theorem geo3_phiCTRL_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
            (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
                ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                    FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
              then RelabelTransition
                (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G
              else G) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
            d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, d2, c1, c2, c3, c4, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ d hΓ hΦ hd hI => ?_⟩
  -- the pinned tuples and the single-carrier distance
  obtain ⟨G₁, hG₁⟩ : ∃ G₁, G₁ = FibreGram (0 : Fin 1) H₁ := ⟨_, rfl⟩
  obtain ⟨Gᵢ, hGᵢ⟩ : ∃ Gᵢ, Gᵢ = FibreGram (0 : Fin 1) Hᵢ := ⟨_, rfl⟩
  rw [← hG₁] at hΦ d1 c1
  rw [← hGᵢ] at d2 c3 r2
  obtain ⟨d₁, hd₁⟩ : ∃ d₁ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
      → ℝ, d₁ = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2) := ⟨_, rfl⟩
  -- the sequence, the index `N = 32768`, the perturbed member
  obtain ⟨zs, hzs⟩ : ∃ zs : ℕ → ℂ, zs = fun n : ℕ => Complex.mk
      (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1)) (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1)) := ⟨_, rfl⟩
  obtain ⟨hunit, -, -, hzne1, -⟩ := zseq_facts zs hzs
  obtain ⟨hdist1, -⟩ := zseq_dist zs hzs
  obtain ⟨z, hz⟩ : ∃ z, z = zs 32768 := ⟨_, rfl⟩
  have hzu : star z * z = 1 := by rw [hz]; exact hunit _
  have hzne : z ≠ 1 := by rw [hz]; exact hzne1 _
  have hzd : ‖z - 1‖ ^ 2 = 4 / ((32768 : ℝ) ^ 2 + 1) := by
    rw [hz]; have := hdist1 32768; push_cast at this; exact this
  obtain ⟨Fz, hFz⟩ : ∃ Fz, Fz = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) := ⟨_, rfl⟩
  have hadmz := hadamard_z_admissible Γ₀ hΓ₀ z hzu
  have hz000 : Fz 0 0 0 = 1 / 4 := by rw [hFz]; exact (fibreGram_z_entries z).1
  have hz01 : Fz 0 1 0 * Fz 1 0 1 = z / 16 := by rw [hFz]; exact (fibreGram_z_entries z).2
  have hIu : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  -- the pair
  obtain ⟨G, hGdef⟩ : ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      G = fun i => Matrix.of fun j k => G₁ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2 := ⟨_, rfl⟩
  obtain ⟨H, hHdef⟩ : ∃ H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      H = fun i => Matrix.of fun j k => Fz i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2 := ⟨_, rfl⟩
  have hG : RealizableGram (Fin 1 × Fin 1) (Γ 0) G := by
    rw [hΓ, hGdef, hG₁, hGᵢ]; exact realizable_prod_of_adm Γ₀ hadm₁ hadmᵢ
  have hH : RealizableGram (Fin 1 × Fin 1) (Γ 0) H := by
    rw [hΓ, hHdef, hFz, hGᵢ]; exact realizable_prod_of_adm Γ₀ hadmz hadmᵢ
  -- `G` fires, `H` does not
  have hfire : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
      ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) :=
    ⟨Gᵢ, by rw [hGᵢ]; exact sh1_necessity hadmᵢ, by rw [hGdef]; exact gramPhaseEquiv_refl _⟩
  have hnofire : ¬ ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
      ∧ GramPhaseEquiv H (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) := by
    rintro ⟨G₂, hG₂, h⟩
    rw [hHdef] at h
    have hd0 : Gᵢ 0 0 0 = G₂ 0 0 0 := by
      have h2 := hG₂.2.2.2 0 0
      rw [hΓ₀, Matrix.of_apply] at h2
      push_cast at h2
      rw [d2, h2]
    have hm : Gᵢ 0 0 0 ≠ 0 := by rw [d2]; norm_num
    have hc := gramPhaseEquiv_cross_invariant (gramPhaseEquiv_fst_of_product hd0 hm h) 0 1
    rw [c1, hz01] at hc
    exact hzne (by linear_combination (-16 : ℂ) * hc)
  -- the isometry equation on the pair
  have e : d (RelabelTransition
      (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G) H = d G H := by
    have e := hI 0 G H hG hH
    rw [hΦ] at e
    beta_reduce at e
    split_ifs at e
    exact e
  -- the upper bound on the inputs
  have hup : d G H = d₁ G₁ Fz := by
    rw [hGdef, hHdef, geo2_product_tensor d₁ hd₁ d hd, hGᵢ, hHᵢ,
      (fourier_feature_norm Complex.I hIu).2, mul_one]
  have hdz : d₁ G₁ Fz ≤ 3 * ‖z - 1‖ := by
    have := fourier_dist_le d₁ hd₁ 1 z (by simp) hzu
    rw [← hFz, ← hH₁, ← hG₁] at this
    exact this
  have hsmall : ‖z - 1‖ < 1 / 12288 := by
    norm_num at hzd
    nlinarith [hzd, norm_nonneg (z - 1)]
  -- the lower bound on the images, at the cross-invariant coordinate of `((0,0),(0,2))`
  have hσ222 : RelabelTransition (Equiv.swap (2 : Fin 4) 3) Gᵢ 2 2 2 = 1 / 4 := by
    rw [hGᵢ, hHᵢ]
    simp [RelabelTransition, fibreGram_apply, Matrix.submatrix_apply]
    linear_combination (-1 / 4 : ℂ) * Complex.I_mul_I
  have hi222 : Gᵢ 2 2 2 = 1 / 4 := by
    have h2 := (sh1_necessity hadmᵢ).2.2.2 2 2
    rw [hΓ₀, Matrix.of_apply, ← hGᵢ] at h2
    push_cast at h2
    exact h2
  have vG : mixedTriple (RelabelTransition
      (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G)
      ((((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4))),
        (((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
      = Complex.I / 4096 := by
    rw [hGdef, relabel_product, relabel_one, coord_cross_product, d1, r2, hσ222]
    ring
  have vH : mixedTriple H
      ((((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4))),
        (((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
      = 1 / 4096 := by
    rw [hHdef, coord_cross_product, hz000, c3, hi222]
    ring
  have hb := coord_le_dist d hd (RelabelTransition
      (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G) H
      ((((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4))),
        (((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
  rw [vG, vH, e, hup] at hb
  have hbig : 1 / 4096 ≤ ‖Complex.I / 4096 - 1 / 4096‖ := by
    rw [show Complex.I / 4096 - 1 / 4096 = (Complex.I - 1) / 4096 by ring, norm_div]
    have h4 : ‖(4096 : ℂ)‖ = 4096 := by simp
    rw [h4]
    linarith [one_le_norm_I_sub_one]
  linarith

/-! #### `Φ_SC` — the class-conditional relabelling of the first factor, at the product
configuration -/

open Classical in
/-- **`Φ_SC` is not an isometry**, by the perturbation pair at `t = 0` and `N = 32768`:
`G := G(Hᵢ) ⊠ G(H₁)` fires (first disjunct) and is sent to `σG(Hᵢ) ⊠ G(H₁)`;
`H := F(i · zs N) ⊠ G(H₁)` fires on neither disjunct (the marginal lemma, `hadamard_entries`'s
`r1`, and `zs N ≠ 1`) and is fixed. The inputs are at distance `d (G(Hᵢ)) (F(i · zs N)) ≤
3 ‖zs N − 1‖ < 1/4096`; the images differ at the cross-invariant coordinate of the product pair
`((0,0),(2,0))` by `‖i − 1‖/4096 ≥ 1/4096`, the first factor's invariant at `(0,2)` being
`z`-free. -/
theorem geo3_phiSC_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
            (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
                ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                      FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
                  ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                      RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ)
                        i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
              then RelabelTransition
                (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G
              else G) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
            d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, d2, c1, c2, c3, c4, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Γ Φ d hΓ hΦ hd hI => ?_⟩
  obtain ⟨G₁, hG₁⟩ : ∃ G₁, G₁ = FibreGram (0 : Fin 1) H₁ := ⟨_, rfl⟩
  obtain ⟨Gᵢ, hGᵢ⟩ : ∃ Gᵢ, Gᵢ = FibreGram (0 : Fin 1) Hᵢ := ⟨_, rfl⟩
  rw [← hG₁] at d1
  rw [← hGᵢ] at hΦ c2 r1 r2
  obtain ⟨d₁, hd₁⟩ : ∃ d₁ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
      → ℝ, d₁ = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2) := ⟨_, rfl⟩
  obtain ⟨zs, hzs⟩ : ∃ zs : ℕ → ℂ, zs = fun n : ℕ => Complex.mk
      (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1)) (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1)) := ⟨_, rfl⟩
  obtain ⟨hunit, -, -, hzne1, -⟩ := zseq_facts zs hzs
  obtain ⟨hdist1, -⟩ := zseq_dist zs hzs
  obtain ⟨z, hz⟩ : ∃ z, z = zs 32768 := ⟨_, rfl⟩
  have hzu : star z * z = 1 := by rw [hz]; exact hunit _
  have hzne : z ≠ 1 := by rw [hz]; exact hzne1 _
  have hzd : ‖z - 1‖ ^ 2 = 4 / ((32768 : ℝ) ^ 2 + 1) := by
    rw [hz]; have := hdist1 32768; push_cast at this; exact this
  have hIu : star Complex.I * Complex.I = 1 := by
    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]
  -- the rotated parameter `w = i · z`
  obtain ⟨w, hw⟩ : ∃ w, w = Complex.I * z := ⟨_, rfl⟩
  have hwu : star w * w = 1 := by
    rw [hw, star_mul', show star Complex.I * star z * (Complex.I * z)
      = (star Complex.I * Complex.I) * (star z * z) by ring, hIu, hzu, one_mul]
  have hwne : w ≠ Complex.I := by
    rw [hw]; intro h
    apply hzne
    have h' : Complex.I * z = Complex.I * 1 := by rw [mul_one]; exact h
    exact mul_left_cancel₀ Complex.I_ne_zero h'
  have hwd : ‖w - Complex.I‖ = ‖z - 1‖ := by
    rw [hw, show Complex.I * z - Complex.I = Complex.I * (z - 1) by ring, norm_mul,
      Complex.norm_I, one_mul]
  obtain ⟨Fw, hFw⟩ : ∃ Fw, Fw = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] p.1 q.1)) := ⟨_, rfl⟩
  have hadmw := hadamard_z_admissible Γ₀ hΓ₀ w hwu
  have hw01 : Fw 0 1 0 * Fw 1 0 1 = w / 16 := by rw [hFw]; exact (fibreGram_z_entries w).2
  have hw02 : Fw 0 2 0 * Fw 2 0 2 = 1 / 16 := by rw [hFw]; exact fibreGram_z_cross02 w
  have hw222 : Fw 2 2 2 = 1 / 4 := by
    have h2 := (sh1_necessity hadmw).2.2.2 2 2
    rw [hΓ₀, Matrix.of_apply, ← hFw] at h2
    push_cast at h2
    exact h2
  -- the pair
  obtain ⟨G, hGdef⟩ : ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      G = fun i => Matrix.of fun j k => Gᵢ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := ⟨_, rfl⟩
  obtain ⟨H, hHdef⟩ : ∃ H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      H = fun i => Matrix.of fun j k => Fw i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := ⟨_, rfl⟩
  have hG : RealizableGram (Fin 1 × Fin 1) (Γ 0) G := by
    rw [hΓ, hGdef, hG₁, hGᵢ]; exact realizable_prod_of_adm Γ₀ hadmᵢ hadm₁
  have hH : RealizableGram (Fin 1 × Fin 1) (Γ 0) H := by
    rw [hΓ, hHdef, hFw, hG₁]; exact realizable_prod_of_adm Γ₀ hadmw hadm₁
  -- `G` fires on the first disjunct; `H` fires on neither
  have hfire : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
      ∧ (GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
        ∨ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            RelabelTransition (Equiv.swap (2 : Fin 4) 3) Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) :=
    ⟨G₁, by rw [hG₁]; exact sh1_necessity hadm₁, Or.inl (by rw [hGdef]; exact gramPhaseEquiv_refl _)⟩
  have hnofire : ¬ ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
      ∧ (GramPhaseEquiv H (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
        ∨ GramPhaseEquiv H (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            RelabelTransition (Equiv.swap (2 : Fin 4) 3) Gᵢ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)) := by
    rintro ⟨G₂, hG₂, h⟩
    rw [hHdef] at h
    have hd0 : G₁ 0 0 0 = G₂ 0 0 0 := by
      have h2 := hG₂.2.2.2 0 0
      rw [hΓ₀, Matrix.of_apply] at h2
      push_cast at h2
      rw [d1, h2]
    have hm : G₁ 0 0 0 ≠ 0 := by rw [d1]; norm_num
    apply hwne
    rcases h with h | h
    · have hc := gramPhaseEquiv_cross_invariant (gramPhaseEquiv_fst_of_product hd0 hm h) 0 1
      rw [c2, hw01] at hc
      linear_combination (-16 : ℂ) * hc
    · have hc := gramPhaseEquiv_cross_invariant (gramPhaseEquiv_fst_of_product hd0 hm h) 0 1
      rw [r1, hw01] at hc
      linear_combination (-16 : ℂ) * hc
  -- the isometry equation on the pair
  have e : d (RelabelTransition
      (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G) H = d G H := by
    have e := hI 0 G H hG hH
    rw [hΦ] at e
    beta_reduce at e
    split_ifs at e
    exact e
  -- the upper bound on the inputs
  have hup : d G H = d₁ Gᵢ Fw := by
    rw [hGdef, hHdef, geo2_product_tensor d₁ hd₁ d hd, hG₁, hH₁,
      (fourier_feature_norm 1 (by simp)).2, mul_one]
  have hdz : d₁ Gᵢ Fw ≤ 3 * ‖z - 1‖ := by
    have := fourier_dist_le d₁ hd₁ Complex.I w hIu hwu
    rw [← hFw, ← hHᵢ, ← hGᵢ, hwd] at this
    exact this
  have hsmall : ‖z - 1‖ < 1 / 12288 := by
    norm_num at hzd
    nlinarith [hzd, norm_nonneg (z - 1)]
  -- the lower bound on the images, at the cross-invariant coordinate of `((0,0),(2,0))`
  have hσ222 : RelabelTransition (Equiv.swap (2 : Fin 4) 3) Gᵢ 2 2 2 = 1 / 4 := by
    rw [hGᵢ, hHᵢ]
    simp [RelabelTransition, fibreGram_apply, Matrix.submatrix_apply]
    linear_combination (-1 / 4 : ℂ) * Complex.I_mul_I
  have vG : mixedTriple (RelabelTransition
      (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G)
      ((((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))),
        (((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
      = Complex.I / 4096 := by
    rw [hGdef, relabel_product, relabel_one, coord_cross_product, d1, r2, hσ222]
    ring
  have vH : mixedTriple H
      ((((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))),
        (((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
      = 1 / 4096 := by
    rw [hHdef, coord_cross_product, hw02, hw222, d1]
    ring
  have hb := coord_le_dist d hd (RelabelTransition
      (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (1 : Equiv.Perm (Fin 4))) G) H
      ((((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))),
        (((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
  rw [vG, vH, e, hup] at hb
  have hbig : 1 / 4096 ≤ ‖Complex.I / 4096 - 1 / 4096‖ := by
    rw [show Complex.I / 4096 - 1 / 4096 = (Complex.I - 1) / 4096 by ring, norm_div]
    have h4 : ‖(4096 : ℂ)‖ = 4096 := by simp
    rw [h4]
    linarith [one_le_norm_I_sub_one]
  linarith

/-! #### `Φ_HS` — the Hilbert-hotel shift along the Fourier family, at the product configuration -/

open Classical in
/-- **`Φ_HS` is not an isometry**, by the shift argument: for `n ≥ 1` the family member `F n` is
sent to `F (n + 1)`, so an isometry would make `d (F n) (F (n + 1))` constant in `n ≥ 1`; but
`d (F 300) (F 301) ≤ 3 ‖zs 301 − zs 300‖ < 1/15000` by `GEO2` (c), the feature norm and the entry
bound, while `d (F 1) (F 2) ≥ ‖zs 2 − zs 1‖ / 4096 > 1/8192` at the cross-invariant coordinate
of the product pair `((0,0),(1,0))`. -/
theorem geo3_phiHS_not_isometry :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Hz : ℂ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (zs : ℕ → ℂ)
            (F : ℕ → Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
            (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
          Hz = (fun z => Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) →
          zs = (fun n : ℕ => Complex.mk (((n : ℝ) ^ 2 - 1) / ((n : ℝ) ^ 2 + 1))
            (2 * (n : ℝ) / ((n : ℝ) ^ 2 + 1))) →
          F = (fun n => fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) (Hz (zs n)) i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2) →
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if h : ∃ n, 1 ≤ n ∧ GramPhaseEquiv G (F n) then F (Nat.find h + 1) else G) →
          d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
          ¬ (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
            d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, d2, c1, c2, c3, c4, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, fun Hz zs F Γ Φ d hHz hzs hF hΓ hΦ hd hI => ?_⟩
  obtain ⟨hunit, -, hzinj, -, -⟩ := zseq_facts zs hzs
  obtain ⟨-, hdist2⟩ := zseq_dist zs hzs
  obtain ⟨d₁, hd₁⟩ : ∃ d₁ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
      → ℝ, d₁ = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2) := ⟨_, rfl⟩
  -- the family: admissibility, entries, realizability
  have hadmz : ∀ z : ℂ, star z * z = 1 → AdmissibleDilationAt Γ₀ (0 : Fin 1) (Hz z) := by
    intro z hz; rw [hHz]; exact hadamard_z_admissible Γ₀ hΓ₀ z hz
  have hcz : ∀ z : ℂ, FibreGram (0 : Fin 1) (Hz z) 1 0 1 * FibreGram (0 : Fin 1) (Hz z) 0 1 0
      = z / 16 := by
    intro z; rw [mul_comm, hHz]; exact (fibreGram_z_entries z).2
  have hcz' : ∀ z : ℂ, FibreGram (0 : Fin 1) (Hz z) 0 1 0 * FibreGram (0 : Fin 1) (Hz z) 1 0 1
      = z / 16 := by
    intro z; rw [hHz]; exact (fibreGram_z_entries z).2
  have hdz : ∀ n, FibreGram (0 : Fin 1) (Hz (zs n)) 1 1 1 = 1 / 4 := by
    intro n
    have h2 := (sh1_necessity (hadmz _ (hunit n))).2.2.2 1 1
    rw [hΓ₀, Matrix.of_apply] at h2
    push_cast at h2
    exact h2
  have hFn : ∀ n, F n = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
      FibreGram (0 : Fin 1) (Hz (zs n)) i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2 := by
    intro n; rw [hF]
  have hRF : ∀ n, RealizableGram (Fin 1 × Fin 1) (Γ 0) (F n) := by
    intro n
    rw [hΓ, hFn]
    exact realizable_prod_of_adm Γ₀ (hadmz _ (hunit n)) hadm₁
  -- the classes of the family are pairwise distinct
  have hFinj : ∀ n m, GramPhaseEquiv (F n) (F m) → n = m := by
    intro n m h
    have := gramPhaseEquiv_cross_invariant h ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    rw [hFn, hFn, product_cross, product_cross, hcz, hcz, d1] at this
    apply hzinj
    linear_combination (-256 : ℂ) * this
  -- the shift on the family
  have hshift : ∀ n, 1 ≤ n → Φ 0 (F n) = F (n + 1) := by
    intro n hn
    have hex : ∃ m, 1 ≤ m ∧ GramPhaseEquiv (F n) (F m) := ⟨n, hn, gramPhaseEquiv_refl _⟩
    rw [hΦ]
    beta_reduce
    rw [dif_pos hex]
    have hspec := Nat.find_spec hex
    rw [hFinj _ _ (gramPhaseEquiv_symm hspec.2)]
  -- an isometry makes the consecutive distances constant along the family
  have hstep : ∀ n, 1 ≤ n → d (F (n + 1)) (F (n + 2)) = d (F n) (F (n + 1)) := by
    intro n hn
    have e := hI 0 (F n) (F (n + 1)) (hRF n) (hRF (n + 1))
    rw [hshift n hn, hshift (n + 1) (by omega)] at e
    exact e
  have hconst : ∀ n, 1 ≤ n → d (F n) (F (n + 1)) = d (F 1) (F 2) := by
    intro n hn
    induction n, hn using Nat.le_induction with
    | base => rfl
    | succ k hk ih => rw [hstep k hk, ih]
  -- the upper bound at `n = 300`
  have hup : ∀ n, d (F n) (F (n + 1))
      = d₁ (FibreGram (0 : Fin 1) (Hz (zs n))) (FibreGram (0 : Fin 1) (Hz (zs (n + 1)))) := by
    intro n
    rw [hFn, hFn, geo2_product_tensor d₁ hd₁ d hd, hH₁, (fourier_feature_norm 1 (by simp)).2,
      mul_one]
  have hle : ∀ n, d₁ (FibreGram (0 : Fin 1) (Hz (zs n))) (FibreGram (0 : Fin 1) (Hz (zs (n + 1))))
      ≤ 3 * ‖zs (n + 1) - zs n‖ := by
    intro n
    rw [hHz]
    exact fourier_dist_le d₁ hd₁ (zs n) (zs (n + 1)) (hunit n) (hunit (n + 1))
  have h300 : d (F 300) (F 301) < 1 / 15000 := by
    rw [hup]
    have h1 := hle 300
    have h2 := hdist2 300
    push_cast at h2
    norm_num at h2
    have h3 : ‖zs 301 - zs 300‖ < 1 / 45000 := by nlinarith [h2, norm_nonneg (zs 301 - zs 300)]
    linarith
  -- the lower bound at `n = 1`, at the cross-invariant coordinate of `((0,0),(1,0))`
  have vF : ∀ n, mixedTriple (F n)
      ((((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4))),
        (((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
      = zs n / 4096 := by
    intro n
    rw [hFn, coord_cross_product, hcz', hdz, d1]
    ring
  have hb := coord_le_dist d hd (F 1) (F 2)
      ((((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4))),
        (((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))
  rw [vF, vF, show zs 1 / 4096 - zs 2 / 4096 = -((zs 2 - zs 1) / 4096) by ring, norm_neg,
    norm_div, show ‖(4096 : ℂ)‖ = 4096 by simp] at hb
  have h12 := hdist2 1
  push_cast at h12
  norm_num at h12
  have hlow : 1 / 2 < ‖zs 2 - zs 1‖ := by nlinarith [h12, norm_nonneg (zs 2 - zs 1)]
  have := hconst 300 (by norm_num)
  linarith

/-! ### Section E — `GEO4`: the implication cells and the rigidity attempt

The prefix through `L4d` is written out, in every statement, as the first seven conjuncts of act
21's `LadderConds`; `L5` is `FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1)
(Equiv.refl (Fin 4 × Fin 4)) (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ`; isometry is the displayed
proposition with `d` bound to the frozen equation. The witness cells `a1`, `a3`, `b₀` consume
act 23's `phiSC_corner`, act 22's `phiSwap_l5_restricts` and the `GEO3` verdicts; the universal
cell `a0` consumes `GEO1`. The lemmas of this section on the entrywise conjugation are the
conjuncts of the `b₀` witness, each a computation. -/

omit [Fintype V] [DecidableEq V] in
/-- On a tuple with Hermitian fibres the entrywise conjugate is the fibrewise transpose. -/
theorem conj_eq_transpose (G : V → Matrix V V ℂ) (h : ∀ i, (G i).IsHermitian) :
    (fun i => Matrix.of fun j k => star (G i j k)) = fun i => (G i)ᵀ := by
  funext i
  ext j k
  simp only [Matrix.of_apply, Matrix.transpose_apply]
  exact (h i).apply k j

open scoped ComplexOrder in
/-- **`L1` for the conjugation**: the entrywise conjugate of a realizable tuple is realizable —
the fibres are transposes of positive semidefinite matrices, of the same rank, summing to the
transpose of the identity, with the same diagonal. -/
theorem realizable_conj {A : Type} [Fintype A] (Γ : Matrix V V ℝ) (G : V → Matrix V V ℂ)
    (hG : RealizableGram A Γ G) :
    RealizableGram A Γ (fun i => Matrix.of fun j k => star (G i j k)) := by
  rw [conj_eq_transpose G fun i => (hG.1 i).1]
  refine ⟨fun i => (hG.1 i).transpose, fun i => ?_, ?_, fun i j => ?_⟩
  · rw [Matrix.rank_transpose]; exact hG.2.1 i
  · rw [← Matrix.transpose_sum, hG.2.2.1, Matrix.transpose_one]
  · exact hG.2.2.2 i j

omit [Fintype V] [DecidableEq V] in
/-- The conjugation is an involution on tuples. -/
theorem conj_conj (G : V → Matrix V V ℂ) :
    (fun i => Matrix.of fun j k =>
      star ((fun i => Matrix.of fun j k => star (G i j k)) i j k)) = G := by
  funext i; ext j k; simp

omit [Fintype V] [DecidableEq V] in
/-- **`L4d` for the conjugation**: it respects act 12's equivalence, with the conjugate phases. -/
theorem conj_gramPhaseEquiv {G G' : V → Matrix V V ℂ} (h : GramPhaseEquiv G G') :
    GramPhaseEquiv (fun i => Matrix.of fun j k => star (G i j k))
      (fun i => Matrix.of fun j k => star (G' i j k)) := by
  obtain ⟨c, hc, hG⟩ := h
  refine ⟨fun j => star (c j), fun j => by rw [norm_star]; exact hc j, fun i j k => ?_⟩
  simp only [Matrix.of_apply, star_star]
  rw [hG, star_mul, star_mul, star_star]
  ring

omit [Fintype V] [DecidableEq V] in
/-- The cross-invariant of the conjugate is the conjugate of the cross-invariant. -/
theorem conj_cross (G : V → Matrix V V ℂ) (i₀ i₁ : V) :
    (fun i => Matrix.of fun j k => star (G i j k)) i₀ i₁ i₀
        * (fun i => Matrix.of fun j k => star (G i j k)) i₁ i₀ i₁
      = star (G i₀ i₁ i₀ * G i₁ i₀ i₁) := by
  simp only [Matrix.of_apply, star_mul']

/-- The cross-invariant of a relabelled product tuple at a pair of product indices is a product of
a cross-invariant of each factor, at the relabelled indices. -/
theorem relabel_product_cross {V₁ V₂ : Type} (σ : Equiv.Perm (V₁ × V₂))
    (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ) (i₀ i₁ : V₁ × V₂) :
    RelabelTransition σ (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
          X i.1 j.1 k.1 * Y i.2 j.2 k.2) i₀ i₁ i₀
        * RelabelTransition σ (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
          X i.1 j.1 k.1 * Y i.2 j.2 k.2) i₁ i₀ i₁
      = (X (σ i₀).1 (σ i₁).1 (σ i₀).1 * X (σ i₁).1 (σ i₀).1 (σ i₁).1)
        * (Y (σ i₀).2 (σ i₁).2 (σ i₀).2 * Y (σ i₁).2 (σ i₀).2 (σ i₁).2) := by
  simp only [RelabelTransition, Matrix.submatrix_apply, Matrix.of_apply]
  ring

open scoped ComplexOrder in
/-- The fibre-Gram tuple of `H₁` has symmetric fibres, so its conjugate is itself. -/
theorem conj_fibreGram_one (H₁ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
    (hH₁ : H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)) :
    (fun i => Matrix.of fun j k => star (FibreGram (0 : Fin 1) H₁ i j k))
      = FibreGram (0 : Fin 1) H₁ := by
  rw [conj_eq_transpose _ fun i => (fibreGram_posSemidef (0 : Fin 1) H₁ i).1]
  subst hH₁
  funext i; ext j k
  simp only [Matrix.transpose_apply]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [fibreGram_apply]

open scoped ComplexOrder in
/-- The fibre-Gram tuple of the Fourier family at `z = −1` has symmetric fibres, so its conjugate
is itself. -/
theorem conj_fibreGram_negOne :
    (fun i => Matrix.of fun j k => star (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1 : ℂ), -1, -(-1 : ℂ); 1, -1, 1, -1;
          1, -(-1 : ℂ), -1, (-1 : ℂ)] p.1 q.1)) i j k))
      = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1 : ℂ), -1, -(-1 : ℂ); 1, -1, 1, -1;
          1, -(-1 : ℂ), -1, (-1 : ℂ)] p.1 q.1)) := by
  rw [conj_eq_transpose _ fun i => (fibreGram_posSemidef (0 : Fin 1) _ i).1]
  funext i; ext j k
  simp only [Matrix.transpose_apply]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [fibreGram_apply]

omit [Fintype V] [DecidableEq V] in
/-- The conjugate of a product tuple is the product of the conjugates, exactly. -/
theorem conj_product {V₁ V₂ : Type} (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ) :
    (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
        star ((fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
          i j k))
      = fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
          (fun i => Matrix.of fun j k => star (X i j k)) i.1 j.1 k.1
            * (fun i => Matrix.of fun j k => star (Y i j k)) i.2 j.2 k.2 := by
  funext i; ext j k
  simp only [Matrix.of_apply, star_mul']

/-! #### Cell `a0` — isometry implies injectivity on classes, universally -/

/-- **Cell `a0` holds**: at the product configuration, an isometry of the geometry on realizable
tuples is injective on realizable classes — equivalent images are at distance `0` by `GEO1` (vi-b),
so the inputs are at distance `0`, hence equivalent by `GEO1` (vi-a). -/
theorem geo4_a0_isometry_injective :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ))
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
          d (Φ t G) (Φ t H) = d G H) →
        ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
          RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) G' →
          GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G' := by
  refine ⟨_, rfl, fun Γ Φ d hΓ hd hI t G G' hG hG' h => ?_⟩
  have h0 : d (Φ t G) (Φ t G') = 0 := geo1_zero_of_equiv d hd _ _ h
  rw [hI t G G' hG hG'] at h0
  exact geo1_equiv_of_zero_product _ rfl (Γ t) (by rw [hΓ]) d hd G G' hG hG' h0

/-! #### Cell `a1` — the prefix with `L5` does not imply isometry: `Φ_SC` -/

open Classical in
/-- **Cell `a1`, `NOT-IMPLIES`**: `Φ_SC` satisfies the prefix through `L4d` and `L5` (act 23's
`phiSC_corner`) and is not an isometry (`GEO3`). -/
theorem geo4_a1_l5_not_implies_geo :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ¬ (∀ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            EvolvesTotally (Fin 1 × Fin 1) Γ Φ →
            PreservesAdmissible (Fin 1 × Fin 1) Γ Φ →
            (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀) →
            Reversible (Fin 1 × Fin 1) Γ Φ →
            (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) →
            FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ →
            ∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
              d (Φ t G) (Φ t H) = d G H) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hSC⟩ := phiSC_corner
  obtain ⟨Γ₀', H₁', Hᵢ', hΓ₀', hH₁', hHᵢ', hnot⟩ := geo3_phiSC_not_isometry
  subst hΓ₀ hH₁ hHᵢ hΓ₀' hH₁' hHᵢ'
  refine ⟨_, rfl, fun Γ d hΓ hd hall => ?_⟩
  obtain ⟨h1, h2, h3, h4, h5, h6, h7, h8, -⟩ := hSC Γ _ hΓ rfl
  exact hnot Γ _ d hΓ rfl hd (hall _ h1 h2 h3 h4 h5 h6 h7 h8)

/-! #### Cell `a3` — the prefix with isometry does not imply `L5`: `Φ_swap` -/

/-- **Cell `a3`, `NOT-IMPLIES`**: `Φ_swap` satisfies the prefix through `L4d` (act 22's
`phiSwap_l5_restricts`), is an isometry (`GEO3`), and does not factorize (the same act 22 result). -/
theorem geo4_a3_geo_not_implies_l5 :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ¬ (∀ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            EvolvesTotally (Fin 1 × Fin 1) Γ Φ →
            PreservesAdmissible (Fin 1 × Fin 1) Γ Φ →
            (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀) →
            Reversible (Fin 1 × Fin 1) Γ Φ →
            (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) →
            (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
              d (Φ t G) (Φ t H) = d G H) →
            FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hSW⟩ := phiSwap_l5_restricts
  obtain ⟨Γ₀', hΓ₀', hiso⟩ := geo3_phiSwap_isometry
  subst hΓ₀ hH₁ hHᵢ hΓ₀'
  refine ⟨_, rfl, fun Γ d hΓ hd hall => ?_⟩
  obtain ⟨h1, h2, h3, h4, h5, h6, h7, -, hnot⟩ := hSW Γ _ hΓ rfl
  exact hnot (hall _ h1 h2 h3 h4 h5 h6 h7 (hiso Γ _ d hΓ rfl hd))

/-! #### Cell `b₀` — the prefix with `L5` and isometry does not force a relabelling: `Φ_conj` -/

/-- **Cell `b₀`, `NOT-RIGID`**: the entrywise conjugation satisfies the prefix through `L4d`, `L5`
and isometry, and at `t = 0` sends the realizable class `[G(Hᵢ) ⊠ G(H₁)]` to a class no carrier
relabelling reaches: every cross-invariant of every relabelling of `G(Hᵢ) ⊠ G(H₁)` lies in
`{1/256, i/256}`, while the conjugate's cross-invariant at the product pair `((0,0),(1,0))` is
`−i/256`. -/
theorem geo4_b0_not_relabel_rigid :
    ∃ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
      ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
          (d : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
            → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → ℝ),
        Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
        d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →
        ¬ (∀ Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
            ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
            EvolvesTotally (Fin 1 × Fin 1) Γ Φ →
            PreservesAdmissible (Fin 1 × Fin 1) Γ Φ →
            (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀) →
            Reversible (Fin 1 × Fin 1) Γ Φ →
            (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) →
            FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ →
            (∀ t (G H : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              RealizableGram (Fin 1 × Fin 1) (Γ t) G → RealizableGram (Fin 1 × Fin 1) (Γ t) H →
              d (Φ t G) (Φ t H) = d G H) →
            ∀ t, ∃ σ : Equiv.Perm (Fin 4 × Fin 4),
              ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
                RealizableGram (Fin 1 × Fin 1) (Γ t) G →
                GramPhaseEquiv (Φ t G) (RelabelTransition σ G)) := by
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨d1, d2, c1, c2, c3, c4, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  have hcrossᵢ := hadamard_i_cross_all Hᵢ hHᵢ
  have hcross₁ := hadamard_one_cross_all H₁ hH₁
  obtain ⟨Γ₀', hΓ₀', hiso⟩ := geo3_phiConj_isometry
  refine ⟨Γ₀, hΓ₀, fun Γ d hΓ hd hall => ?_⟩
  have hiso' := hiso Γ (fun _ G => fun i => Matrix.of fun j k => star (G i j k)) d
    (by rw [hΓ, hΓ₀, hΓ₀']) rfl hd
  subst hΓ
  -- the conjugation as a map, its involution, its descent and its admissibility preservation
  obtain ⟨C, hC⟩ : ∃ C : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
      → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      C = fun G => fun i => Matrix.of fun j k => star (G i j k) := ⟨_, rfl⟩
  have hCC : ∀ G, C (C G) = G := fun G => by rw [hC]; exact conj_conj G
  have hCd : ∀ {G G'}, GramPhaseEquiv G G' → GramPhaseEquiv (C G) (C G') := fun h => by
    rw [hC]; exact conj_gramPhaseEquiv h
  have hCr : ∀ {G}, RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G →
      RealizableGram (Fin 1 × Fin 1)
        (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (C G) := fun h => by
    rw [hC]; exact realizable_conj _ _ h
  have hiter : ∀ G₀, RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G₀ →
      ∀ t, RealizableGram (Fin 1 × Fin 1)
        (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (C^[t] G₀) := by
    intro G₀ hG₀ t
    induction t with
    | zero => exact hG₀
    | succ n ih => rw [Function.iterate_succ_apply']; exact hCr ih
  have hlawiter : ∀ G₀ t, GramPhaseEquiv (C^[t + 1] G₀) (C (C^[t] G₀)) := by
    intro G₀ t
    rw [Function.iterate_succ_apply']
    exact gramPhaseEquiv_refl _
  -- the three named tuples: the two real ones, fixed exactly, and the non-solution
  obtain ⟨G₁, hG₁⟩ : ∃ G₁, G₁ = FibreGram (0 : Fin 1) H₁ := ⟨_, rfl⟩
  obtain ⟨Gᵢ, hGᵢ⟩ : ∃ Gᵢ, Gᵢ = FibreGram (0 : Fin 1) Hᵢ := ⟨_, rfl⟩
  obtain ⟨Gm, hGm⟩ : ∃ Gm, Gm = FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1 : ℂ), -1, -(-1 : ℂ); 1, -1, 1, -1;
        1, -(-1 : ℂ), -1, (-1 : ℂ)] p.1 q.1)) := ⟨_, rfl⟩
  rw [← hG₁] at d1 c1 hcross₁
  rw [← hGᵢ] at c2 hcrossᵢ
  have hadmm : AdmissibleDilationAt Γ₀ (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (-1 : ℂ), -1, -(-1 : ℂ); 1, -1, 1, -1;
        1, -(-1 : ℂ), -1, (-1 : ℂ)] p.1 q.1)) := hadamard_z_admissible Γ₀ hΓ₀ (-1) (by simp)
  have cm : Gm 0 1 0 * Gm 1 0 1 = (-1 : ℂ) / 16 := by rw [hGm]; exact (fibreGram_z_entries (-1)).2
  have hfix₁ : (fun i => Matrix.of fun j k => star (G₁ i j k)) = G₁ := by
    rw [hG₁]; exact conj_fibreGram_one H₁ hH₁
  have hfixm : (fun i => Matrix.of fun j k => star (Gm i j k)) = Gm := by
    rw [hGm]; exact conj_fibreGram_negOne
  have hfix₁' : ∀ i j k, star (G₁ i j k) = G₁ i j k := fun i j k => by
    have := congrFun (congrFun (congrFun hfix₁ i) j) k
    simpa using this
  have hfixm' : ∀ i j k, star (Gm i j k) = Gm i j k := fun i j k => by
    have := congrFun (congrFun (congrFun hfixm i) j) k
    simpa using this
  obtain ⟨P₁₁, hP₁₁⟩ : ∃ P : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      P = fun i => Matrix.of fun j k => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := ⟨_, rfl⟩
  obtain ⟨Pm₁, hPm₁⟩ : ∃ P : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      P = fun i => Matrix.of fun j k => Gm i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := ⟨_, rfl⟩
  obtain ⟨Pᵢ₁, hPᵢ₁⟩ : ∃ P : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      P = fun i => Matrix.of fun j k => Gᵢ i.1 j.1 k.1 * G₁ i.2 j.2 k.2 := ⟨_, rfl⟩
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) P₁₁ := by
    rw [hP₁₁, hG₁]; exact realizable_prod_of_adm Γ₀ hadm₁ hadm₁
  have hRm₁ : RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) Pm₁ := by
    rw [hPm₁, hGm, hG₁]; exact realizable_prod_of_adm Γ₀ hadmm hadm₁
  have hRᵢ₁ : RealizableGram (Fin 1 × Fin 1)
      (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) Pᵢ₁ := by
    rw [hPᵢ₁, hGᵢ, hG₁]; exact realizable_prod_of_adm Γ₀ hadmᵢ hadm₁
  have hCprod : ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      C (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
        = fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            (fun i => Matrix.of fun j k => star (X i j k)) i.1 j.1 k.1
              * (fun i => Matrix.of fun j k => star (Y i j k)) i.2 j.2 k.2 := by
    intro X Y; rw [hC]; exact conj_product X Y
  have hfix₁₁ : C P₁₁ = P₁₁ := by
    rw [hC, hP₁₁]
    funext i; ext j k
    simp [star_mul', hfix₁']
  have hfixm₁ : C Pm₁ = Pm₁ := by
    rw [hC, hPm₁]
    funext i; ext j k
    simp [star_mul', hfix₁', hfixm']
  -- the separations, through act 12's cross-invariant at ((0,0),(1,0))
  have s11m1 : ¬ GramPhaseEquiv P₁₁ Pm₁ := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [hP₁₁, hPm₁, product_cross, product_cross, cm, d1, c1] at this
    norm_num at this
  have si1C : ¬ GramPhaseEquiv Pᵢ₁ (C Pᵢ₁) := by
    intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [hC] at this
    rw [conj_cross, hPᵢ₁, product_cross, c2, d1] at this
    simp [Complex.ext_iff] at this
    norm_num at this
  -- the prefix, `L5` and isometry of the conjugation, then the relabelling clause refuted
  have hall' := hall (fun _ G => C G) ?_ ?_ ?_ ?_ ⟨C, fun _ => rfl⟩ ?_ (fun _ _ _ h => hCd h) ?_
    (by rw [hC]; exact hiso')
  · obtain ⟨σ, hσ⟩ := hall' 0
    have h := hσ Pᵢ₁ hRᵢ₁
    have hc := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [hC] at hc
    rw [conj_cross, hPᵢ₁, relabel_product_cross, product_cross, c2, d1,
      hcross₁ (σ ((0 : Fin 4), (0 : Fin 4))).2 (σ ((1 : Fin 4), (0 : Fin 4))).2] at hc
    rcases hcrossᵢ (σ ((0 : Fin 4), (0 : Fin 4))).1 (σ ((1 : Fin 4), (0 : Fin 4))).1 with hh | hh
      <;> rw [hh] at hc <;> (simp [Complex.ext_iff] at hc; try norm_num at hc)
  · -- ProperAt: two constant real solutions, inequivalent, and the constant non-solution
    refine ⟨fun _ => P₁₁, fun _ => Pm₁, fun _ => Pᵢ₁, fun _ => hR₁₁, fun _ => hRm₁, fun _ => hRᵢ₁,
      fun _ => by dsimp only; rw [hfix₁₁]; exact gramPhaseEquiv_refl _,
      fun _ => by dsimp only; rw [hfixm₁]; exact gramPhaseEquiv_refl _,
      fun h => s11m1 (h 0), fun h => si1C (h 0)⟩
  · -- PropagatesFrom: clause (i) from descent through act 21's ol1a_descent; clause (ii) at t = 1
    refine ⟨fun G₁' G₂' _ _ h₁ h₂ h0 =>
      (ol1a_descent ((0 : Fin 1), (0 : Fin 1))
        (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)
        (fun _ _ _ h => hCd h)).2.1 G₁' G₂' h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => Pm₁, le_rfl, fun _ => hR₁₁, fun _ => hRm₁,
      fun _ => by dsimp only; rw [hfix₁₁]; exact gramPhaseEquiv_refl _,
      fun _ => by dsimp only; rw [hfixm₁]; exact gramPhaseEquiv_refl _, s11m1⟩
  · -- L0
    exact fun G₀ hG₀ => ⟨fun t => C^[t] G₀, hiter G₀ hG₀, hlawiter G₀, gramPhaseEquiv_refl _⟩
  · -- L1
    exact fun _ _ hG => hCr hG
  · -- L3i and L3s
    refine ⟨fun _ G G' _ _ h => ?_, fun _ G' hG' => ⟨C G', hCr hG', ?_⟩⟩
    · have := hCd h
      rw [hCC, hCC] at this
      exact this
    · dsimp only
      rw [hCC]
      exact gramPhaseEquiv_refl _
  · -- L5, with both factor maps the single-carrier conjugation
    refine ⟨by simp, fun t i j => by simp [Matrix.of_apply], ?_⟩
    refine ⟨fun _ X => fun i => Matrix.of fun j k => star (X i j k),
      fun _ Y => fun i => Matrix.of fun j k => star (Y i j k), fun t X Y _ _ => ?_⟩
    simp only [Equiv.refl_apply]
    rw [hCprod]
    exact gramPhaseEquiv_refl _

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
#print axioms fourier_dist_le
#print axioms realizable_prod_of_adm
#print axioms coord_cross_product
#print axioms one_le_norm_I_sub_one
#print axioms geo3_phiI_isometry
#print axioms geo3_phiP_isometry
#print axioms geo3_phiC_not_isometry
#print axioms geo3_phiT_isometry
#print axioms geo3_phiPP_isometry
#print axioms geo3_phiSwap_isometry
#print axioms geo3_phiConj_isometry
#print axioms geo3_phiPC_not_isometry
#print axioms geo3_phiMD_not_isometry
#print axioms geo3_phiCTRL_not_isometry
#print axioms geo3_phiSC_not_isometry
#print axioms geo3_phiHS_not_isometry
#print axioms conj_eq_transpose
#print axioms realizable_conj
#print axioms conj_conj
#print axioms conj_gramPhaseEquiv
#print axioms conj_cross
#print axioms relabel_product_cross
#print axioms conj_fibreGram_one
#print axioms conj_fibreGram_negOne
#print axioms conj_product
#print axioms geo4_a0_isometry_injective
#print axioms geo4_a1_l5_not_implies_geo
#print axioms geo4_a3_geo_not_implies_l5
#print axioms geo4_b0_not_relabel_rigid

end OrbitGeometrySelector
end OIBridge
