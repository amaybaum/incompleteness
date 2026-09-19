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

end OrbitGeometrySelector
end OIBridge
