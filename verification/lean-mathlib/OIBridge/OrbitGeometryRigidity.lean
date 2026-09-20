import OIBridge.OrbitGeometryIsometries

/-!
# Act 26 — the circle-gluing rigidity of the normalized space: the restricted Euclidean metric and the mandatory affine extension, the census of the relabelled Fourier circles, a gated classification of the surjective isometries or a kernel-certified isometry outside the family, and the prefix-constrained corollary

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity/preregistration.md`,
blob `521b63ccde0056453f42035ba9d7970be66cf6f9`, from `main` at
`e0be0ab6dca7b6661a008a9f5e1f3a29ea736003` — the certified merge commit of that control plane, the
round's mandated execution base `B`, whose frozen blob this execution verified as its first act.

## What this round is

A **gated round**: four targets frozen together — `A26-0` the restricted ambient Euclidean metric on
the normalized space and the mandatory affine-extension theorem, `A26-1` the census of the relabelled
Fourier circles of act 25's description, `A26-2` the classification of the surjective isometries of
the normalized space or a kernel-certified isometry outside act 25's family, `A26-3` the
prefix-constrained corollary for transition families — executed in the fixed order
`A26-0` → `A26-1` → `A26-2` → `A26-3`, each later target opened only as the freeze's gate names, with
one verdict commit per executed target.

**The definition budget is three, and a list.** This module introduces exactly the three definitions
the freeze displays — `featureVec`, `normalizedSet`, `IsSurjIsometryOn` — each with its frozen
statement, and no other declaration of any kind. The invariant family is act 24's `mixedTriple`,
consumed; the geometry is act 24's frozen equation, bound as a hypothesis wherever a statement names
`d`, and carried onto the ambient space by act 24's `dist_eq_norm_toLp`; the metric of the
normalized space is the restricted ambient Euclidean metric of
`EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))` and never a path metric; the
four generators of the family and the four-shape conclusion are act 25's, written out by their
frozen formulas in every statement that names them; every rung is act 21's declaration consumed;
act 23's Fourier matrix is the lambda its merged statements carry. Every other object is the merged
record's own, consumed unmodified at merged strength. **A merged statement is not enlarged by being
consumed.**

**This module's first commit carries the three definitions and Section A only** — the shared lemmas
that answer no target by themselves: the unfolding of the feature embedding, act 24's distance as
the ambient distance of feature vectors, equal feature vectors for equivalent tuples and the
converse on realizable tuples at the single carrier, membership of realizable tuples and of the
relabelled Fourier tuples in the normalized set with the union equality as act 25's description
restated, and the bridge between tuple-level and set-level surjective isometries in both directions.
**No lemma of this commit decides whether any relabelled Fourier circle coincides with the Fourier
circle**, and none states anything about an affine extension or about any isometry's membership in
the family. Each verdict enters in its own later commit, in the frozen order.

**The `A26-0` commit carries Section B**: the polarization identity, the linear-isometry extension
from a set to the whole space, and `a26_0_affine_extension` with the frozen statement's three
conjuncts — the affine extension of a map preserving distances on a set, uniqueness on the affine
hull of the set and nowhere else, and the instantiation at the normalized set with the set carried
onto itself. It decides nothing about the circles, the census or the family.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 26 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
namespace OrbitGeometryRigidity

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries

open scoped InnerProductSpace

/-! ### The three budgeted definitions, each with its frozen statement -/

/-- **(D1) the feature embedding.** The feature vector of a tuple, as the point of act 24's ambient
Euclidean space `EuclideanSpace ℂ ((V × V × V) × (V × V × V))` that act 24's `dist_eq_norm_toLp`
names. -/
def featureVec {V : Type} [Fintype V] [DecidableEq V] (G : V → Matrix V V ℂ) :
    EuclideanSpace ℂ ((V × V × V) × (V × V × V)) :=
  WithLp.toLp 2 (mixedTriple G)

/-- **(D2) the normalized set.** The set of feature vectors of the realizable tuples at the
single-carrier configuration, a subset of the ambient space carrying its restricted metric. -/
def normalizedSet (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) :
    Set (EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))) :=
  {x | ∃ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G ∧ featureVec G = x}

/-- **(D3) the surjective-isometry predicate.** A map of the ambient space that carries `S` into
`S`, onto `S`, and preserves distances between points of `S`; nothing is asked of it off `S`. -/
def IsSurjIsometryOn {E : Type} [MetricSpace E] (S : Set E) (f : E → E) : Prop :=
  (∀ x ∈ S, f x ∈ S) ∧ (∀ y ∈ S, ∃ x ∈ S, f x = y) ∧ ∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y

/-! ### Section A — the shared lemmas, before any verdict

None of these is a verdict of any target, and none decides a coincidence of circles or states an
extension. -/

variable {V : Type} [Fintype V] [DecidableEq V]

/-- **The unfolding of the feature embedding**: its underlying function is act 24's feature map. -/
theorem featureVec_ofLp (G : V → Matrix V V ℂ) : (featureVec G).ofLp = mixedTriple G := rfl

/-- **Act 24's distance is the ambient distance of feature vectors** — `dist_eq_norm_toLp`
restated: the metric of this round is the restricted ambient Euclidean metric. -/
theorem dist_featureVec (d : (V → Matrix V V ℂ) → (V → Matrix V V ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (G H : V → Matrix V V ℂ) : d G H = dist (featureVec G) (featureVec H) := by
  rw [dist_eq_norm]; exact dist_eq_norm_toLp d hd G H

/-- **Equivalent tuples have equal feature vectors** — act 24's `mixedTriple_gauge` carried onto the
ambient space. -/
theorem featureVec_gauge {G H : V → Matrix V V ℂ} (h : GramPhaseEquiv G H) :
    featureVec G = featureVec H := by
  unfold featureVec; rw [mixedTriple_gauge h]

/-- **Equal feature vectors of realizable tuples at the single carrier are equivalent** — act 24's
`geo1_separation_single` carried onto the ambient space. -/
theorem gramPhaseEquiv_of_featureVec_eq (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (hG : RealizableGram (Fin 1) Γ₀ G) (hH : RealizableGram (Fin 1) Γ₀ H)
    (h : featureVec G = featureVec H) : GramPhaseEquiv G H :=
  geo1_separation_single Γ₀ hΓ₀ G H hG hH (congrArg WithLp.ofLp h)

/-- **A realizable tuple's feature vector lies in the normalized set.** -/
theorem featureVec_mem_normalizedSet {Γ₀ : Matrix (Fin 4) (Fin 4) ℝ}
    {G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ} (hG : RealizableGram (Fin 1) Γ₀ G) :
    featureVec G ∈ normalizedSet Γ₀ :=
  ⟨G, hG, rfl⟩

/-- **The relabelled Fourier tuples lie in the normalized set** — act 25's `iso2_classes_single` (b)
read through the embedding; a statement about membership and about no coincidence. -/
theorem relabelled_fourier_mem_normalizedSet (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) (π τ : Equiv.Perm (Fin 4)) (z : ℂ)
    (hz : star z * z = 1) :
    featureVec (fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))
          (π i)).submatrix τ τ) ∈ normalizedSet Γ₀ :=
  featureVec_mem_normalizedSet ((iso2_classes_single Γ₀ hΓ₀).2 π τ z hz)

/-- **The normalized set is exactly the union of the relabelled Fourier circles** — act 25's
`iso2_classes_single`, both directions, read through the embedding. It says which points the set
has; it says nothing about which of the circles coincide. -/
theorem normalizedSet_eq_iUnion (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    normalizedSet Γ₀ = ⋃ (π : Equiv.Perm (Fin 4)) (τ : Equiv.Perm (Fin 4)),
      {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (fun i =>
        (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
          (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1))
            (π i)).submatrix τ τ)} := by
  ext x
  constructor
  · rintro ⟨G, hG, rfl⟩
    obtain ⟨π, τ, z, hz, hequiv⟩ := (iso2_classes_single Γ₀ hΓ₀).1 G hG
    refine Set.mem_iUnion.2 ⟨π, Set.mem_iUnion.2 ⟨τ, z, hz, ?_⟩⟩
    exact featureVec_gauge hequiv
  · intro hx
    obtain ⟨π, hπ⟩ := Set.mem_iUnion.1 hx
    obtain ⟨τ, z, hz, rfl⟩ := Set.mem_iUnion.1 hπ
    exact relabelled_fourier_mem_normalizedSet Γ₀ hΓ₀ π τ z hz

/-! #### The bridge — tuple-level surjective isometries and set-level ones, in both directions

Act 25's three hypotheses on a map `φ` of tuples — realizability preserved, surjectivity on classes,
isometry on realizable tuples, with `d` bound to act 24's equation — and `IsSurjIsometryOn
(normalizedSet Γ₀)` on a map `f` of the ambient space carry each other: `φ` induces an `f` agreeing
with it on feature vectors, and `f` induces a `φ`. The passage uses act 24's separation and gauge
invariance and `Classical.choice`, and nothing about any isometry's form. -/

/-- **Two realizable tuples with equal feature vectors have images with equal feature vectors**
under a map with act 25's three hypotheses: the images are at distance `0` by isometry, hence
equivalent by act 24's `geo1_equiv_of_zero_single`, hence equal in feature by gauge invariance. -/
theorem featureVec_image_eq (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
    (h1 : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
    (h3 : ∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H →
      d (φ G) (φ H) = d G H)
    {G H : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (hG : RealizableGram (Fin 1) Γ₀ G) (hH : RealizableGram (Fin 1) Γ₀ H)
    (h : featureVec G = featureVec H) : featureVec (φ G) = featureVec (φ H) := by
  have hzero : d (φ G) (φ H) = 0 := by
    rw [h3 G H hG hH, dist_featureVec d hd, h, dist_self]
  exact featureVec_gauge (geo1_equiv_of_zero_single Γ₀ hΓ₀ d hd (φ G) (φ H) (h1 G hG) (h1 H hH) hzero)

open Classical in
/-- **The bridge, tuples to the set**: a map `φ` on tuples with act 25's three hypotheses induces a
map `f` of the ambient space with `IsSurjIsometryOn (normalizedSet Γ₀) f` and
`f (featureVec G) = featureVec (φ G)` on every realizable `G`. -/
theorem bridge_of_tuple_isometry (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
    (h1 : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
    (h2 : ∀ H, RealizableGram (Fin 1) Γ₀ H →
      ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
    (h3 : ∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H →
      d (φ G) (φ H) = d G H) :
    ∃ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))
        → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
      IsSurjIsometryOn (normalizedSet Γ₀) f
        ∧ ∀ G, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (φ G) := by
  let f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))
      → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) :=
    fun x => if hx : x ∈ normalizedSet Γ₀ then featureVec (φ (Classical.choose hx)) else x
  have hf : ∀ G, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (φ G) := by
    intro G hG
    have hmem : featureVec G ∈ normalizedSet Γ₀ := featureVec_mem_normalizedSet hG
    simp only [f, dif_pos hmem]
    obtain ⟨hG', hfeat⟩ := Classical.choose_spec hmem
    exact featureVec_image_eq Γ₀ hΓ₀ d hd φ h1 h3 hG' hG hfeat
  refine ⟨f, ⟨?_, ?_, ?_⟩, hf⟩
  · rintro x ⟨G, hG, rfl⟩
    rw [hf G hG]
    exact featureVec_mem_normalizedSet (h1 G hG)
  · rintro y ⟨H, hH, rfl⟩
    obtain ⟨G, hG, hequiv⟩ := h2 H hH
    exact ⟨featureVec G, featureVec_mem_normalizedSet hG, by rw [hf G hG]; exact featureVec_gauge hequiv⟩
  · rintro x ⟨G, hG, rfl⟩ y ⟨H, hH, rfl⟩
    rw [hf G hG, hf H hH, ← dist_featureVec d hd, ← dist_featureVec d hd]
    exact h3 G H hG hH

open Classical in
/-- **The bridge, the set to tuples**: a map `f` of the ambient space with
`IsSurjIsometryOn (normalizedSet Γ₀) f` induces a map `φ` on tuples with act 25's three hypotheses
and `featureVec (φ G) = f (featureVec G)` on every realizable `G`. -/
theorem tuple_isometry_of_bridge (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (d : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → ℝ)
    (hd : d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2))
    (f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))
        → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)))
    (hf : IsSurjIsometryOn (normalizedSet Γ₀) f) :
    ∃ φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
        ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H →
            ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
        ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H →
            d (φ G) (φ H) = d G H)
        ∧ ∀ G, RealizableGram (Fin 1) Γ₀ G → featureVec (φ G) = f (featureVec G) := by
  obtain ⟨hinto, honto, hdist⟩ := hf
  let φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun G => if hG : RealizableGram (Fin 1) Γ₀ G
      then Classical.choose (hinto (featureVec G) (featureVec_mem_normalizedSet hG)) else G
  have hφ : ∀ G (hG : RealizableGram (Fin 1) Γ₀ G),
      RealizableGram (Fin 1) Γ₀ (φ G) ∧ featureVec (φ G) = f (featureVec G) := by
    intro G hG
    simp only [φ, dif_pos hG]
    exact Classical.choose_spec (hinto (featureVec G) (featureVec_mem_normalizedSet hG))
  refine ⟨φ, fun G hG => (hφ G hG).1, ?_, ?_, fun G hG => (hφ G hG).2⟩
  · intro H hH
    obtain ⟨x, ⟨G, hG, rfl⟩, hfx⟩ := honto (featureVec H) (featureVec_mem_normalizedSet hH)
    refine ⟨G, hG, gramPhaseEquiv_of_featureVec_eq Γ₀ hΓ₀ (hφ G hG).1 hH ?_⟩
    rw [(hφ G hG).2, hfx]
  · intro G H hG hH
    rw [dist_featureVec d hd, dist_featureVec d hd, (hφ G hG).2, (hφ H hH).2]
    exact hdist _ (featureVec_mem_normalizedSet hG) _ (featureVec_mem_normalizedSet hH)

/-! ### Section B — `A26-0`: the extension layer, then the verdict

The polarization identity on a distance-preserving map, the linear-isometry extension from a set to
the whole space through a basis of its span, and the three conjuncts of the frozen statement — the
affine extension, uniqueness on the affine hull only, and the instantiation at the normalized set
with the set carried onto itself. The hypothesis on the map is distance preservation on the set and
nothing else. -/

section Extension

variable {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **Polarization on a distance-preserving map**: distances between points of `S` fix the real
inner products of the differences from any base point of `S`. -/
theorem inner_sub_eq_of_dist_eq {S : Set E} {f : E → E}
    (hf : ∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y)
    {p x y : E} (hp : p ∈ S) (hx : x ∈ S) (hy : y ∈ S) :
    ⟪f x - f p, f y - f p⟫_ℝ = ⟪x - p, y - p⟫_ℝ := by
  rw [real_inner_eq_norm_mul_self_add_norm_mul_self_sub_norm_sub_mul_self_div_two,
    real_inner_eq_norm_mul_self_add_norm_mul_self_sub_norm_sub_mul_self_div_two]
  have h1 : ‖f x - f p‖ = ‖x - p‖ := by
    rw [← dist_eq_norm, ← dist_eq_norm]; exact hf x hx p hp
  have h2 : ‖f y - f p‖ = ‖y - p‖ := by
    rw [← dist_eq_norm, ← dist_eq_norm]; exact hf y hy p hp
  have h3 : ‖f x - f p - (f y - f p)‖ = ‖x - p - (y - p)‖ := by
    rw [sub_sub_sub_cancel_right, sub_sub_sub_cancel_right, ← dist_eq_norm, ← dist_eq_norm]
    exact hf x hx y hy
  rw [h1, h2, h3]

/-- **The linear-isometry extension**: a map of `E` preserving real inner products between points
of a set `T` agrees on `T` with a linear isometric automorphism of `E`. No linearity, continuity or
compactness is assumed; the map is only known on `T`. -/
theorem exists_linearIsometryEquiv_of_inner_eq [FiniteDimensional ℝ E] (T : Set E) (φ : E → E)
    (hφ : ∀ u ∈ T, ∀ v ∈ T, ⟪φ u, φ v⟫_ℝ = ⟪u, v⟫_ℝ) :
    ∃ L : E ≃ₗᵢ[ℝ] E, ∀ u ∈ T, L u = φ u := by
  obtain ⟨b, hbT, hspan, hli⟩ := exists_linearIndependent ℝ T
  -- the span of the independent subset, with its basis
  let W : Submodule ℝ E := Submodule.span ℝ (Set.range (Subtype.val : b → E))
  have hWb : W = Submodule.span ℝ b := by
    simp only [W, Subtype.range_val]
  let B : Module.Basis b ℝ W := Module.Basis.span hli
  have hB : ∀ i : b, ((B i : W) : E) = (i : E) := fun i =>
    congrArg Subtype.val (Module.Basis.span_apply hli i)
  -- the linear map on the span sending each basis vector to its image
  let L₀ : W →ₗ[ℝ] E := B.constr ℝ (fun i : b => φ (i : E))
  have hL₀ : ∀ i : b, L₀ (B i) = φ (i : E) := fun i => Module.Basis.constr_basis B ℝ _ i
  -- inner products are preserved on the span: bilinear in each argument, checked on the basis
  have hinner : ∀ x y : W, ⟪L₀ x, L₀ y⟫_ℝ = ⟪(x : E), (y : E)⟫_ℝ := by
    let Bl : W →ₗ[ℝ] W →ₗ[ℝ] ℝ := LinearMap.mk₂ ℝ (fun x y : W => ⟪L₀ x, L₀ y⟫_ℝ)
      (fun x₁ x₂ y => by rw [map_add, inner_add_left])
      (fun c x y => by rw [map_smul, real_inner_smul_left, smul_eq_mul])
      (fun x y₁ y₂ => by rw [map_add, inner_add_right])
      (fun c x y => by rw [map_smul, real_inner_smul_right, smul_eq_mul])
    let Bl' : W →ₗ[ℝ] W →ₗ[ℝ] ℝ := LinearMap.mk₂ ℝ (fun x y : W => ⟪(x : E), (y : E)⟫_ℝ)
      (fun x₁ x₂ y => by rw [Submodule.coe_add, inner_add_left])
      (fun c x y => by rw [Submodule.coe_smul, real_inner_smul_left, smul_eq_mul])
      (fun x y₁ y₂ => by rw [Submodule.coe_add, inner_add_right])
      (fun c x y => by rw [Submodule.coe_smul, real_inner_smul_right, smul_eq_mul])
    have hBl : Bl = Bl' := by
      refine LinearMap.ext_basis B B (fun i j => ?_)
      simp only [Bl, Bl', LinearMap.mk₂_apply, hL₀, hB]
      exact hφ _ (hbT i.2) _ (hbT j.2)
    intro x y
    have := LinearMap.congr_fun₂ hBl x y
    simpa only [Bl, Bl', LinearMap.mk₂_apply] using this
  -- the isometry on the span, its extension to `E`, and the automorphism
  let li : W →ₗᵢ[ℝ] E := LinearMap.isometryOfInner L₀ hinner
  let lext : E →ₗᵢ[ℝ] E := li.extend
  let L : E ≃ₗᵢ[ℝ] E := lext.toLinearIsometryEquiv rfl
  refine ⟨L, fun u hu => ?_⟩
  -- `u` lies in the span
  have huW : u ∈ W := by
    rw [hWb, hspan]; exact Submodule.subset_span hu
  have hLu : L u = L₀ ⟨u, huW⟩ := by
    show lext.toLinearIsometryEquiv rfl u = L₀ ⟨u, huW⟩
    rw [LinearIsometry.coe_toLinearIsometryEquiv]
    exact li.extend_apply ⟨u, huW⟩
  rw [hLu]
  -- `L₀ ⟨u, _⟩ = φ u`: the two vectors have equal inner products against `φ u` and equal norms
  have hcross : ⟪L₀ ⟨u, huW⟩, φ u⟫_ℝ = ⟪u, u⟫_ℝ := by
    let ℓ₁ : W →ₗ[ℝ] ℝ := (innerₛₗ ℝ (φ u)).comp L₀
    let ℓ₂ : W →ₗ[ℝ] ℝ := (innerₛₗ ℝ u).comp W.subtype
    have hℓ : ℓ₁ = ℓ₂ := by
      refine Module.Basis.ext B (fun i => ?_)
      simp only [ℓ₁, ℓ₂, LinearMap.comp_apply, innerₛₗ_apply_apply, Submodule.subtype_apply, hL₀, hB]
      rw [real_inner_comm, hφ _ (hbT i.2) _ hu, real_inner_comm]
    have := LinearMap.congr_fun hℓ ⟨u, huW⟩
    simp only [ℓ₁, ℓ₂, LinearMap.comp_apply, innerₛₗ_apply_apply, Submodule.subtype_apply] at this
    rw [real_inner_comm]
    exact this
  have hnorm : ‖L₀ ⟨u, huW⟩ - φ u‖ ^ 2 = 0 := by
    rw [norm_sub_sq_real, ← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq, hinner,
      hφ u hu u hu, hcross]
    ring
  have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hnorm
  exact sub_eq_zero.1 (norm_eq_zero.1 this)

/-- **(i) the affine-isometry extension**: a map of `E` preserving distances between points of a
set `S` agrees on `S` with an affine isometric automorphism of `E`. The hypothesis on the map is
distance preservation on `S` and nothing else. -/
theorem exists_affineIsometryEquiv_of_dist_eq [FiniteDimensional ℝ E] (S : Set E) (f : E → E)
    (hf : ∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y) :
    ∃ g : E ≃ᵃⁱ[ℝ] E, ∀ x ∈ S, g x = f x := by
  rcases S.eq_empty_or_nonempty with hS | ⟨p, hp⟩
  · exact ⟨AffineIsometryEquiv.refl ℝ E, fun x hx => by rw [hS] at hx; exact absurd hx (Set.notMem_empty x)⟩
  -- translate `p` to the origin on both sides; the translated map preserves inner products
  let T : Set E := (fun x => x - p) '' S
  let φ : E → E := fun v => f (v + p) - f p
  have hφ : ∀ u ∈ T, ∀ v ∈ T, ⟪φ u, φ v⟫_ℝ = ⟪u, v⟫_ℝ := by
    rintro _ ⟨x, hx, rfl⟩ _ ⟨y, hy, rfl⟩
    simp only [φ, sub_add_cancel]
    exact inner_sub_eq_of_dist_eq hf hp hx hy
  obtain ⟨L, hL⟩ := exists_linearIsometryEquiv_of_inner_eq T φ hφ
  -- the rigid motion `x ↦ L (x - p) + f p`
  let g : E ≃ᵃⁱ[ℝ] E := (AffineIsometryEquiv.constVAdd ℝ E (-p)).trans
    (L.toAffineIsometryEquiv.trans (AffineIsometryEquiv.constVAdd ℝ E (f p)))
  refine ⟨g, fun x hx => ?_⟩
  have hg : g x = f p + L (-p + x) := by
    simp only [g, AffineIsometryEquiv.coe_trans, Function.comp_apply,
      AffineIsometryEquiv.coe_constVAdd, LinearIsometryEquiv.coe_toAffineIsometryEquiv, vadd_eq_add]
  rw [hg, neg_add_eq_sub, hL (x - p) ⟨x, hx, rfl⟩]
  simp only [φ, sub_add_cancel, add_sub_cancel]

/-- **(ii) uniqueness on the affine hull**: two affine maps agreeing with `f` on `S` agree on
`affineSpan ℝ S`, and nothing is asserted off it. -/
theorem eqOn_affineSpan_of_agree (S : Set E) (f : E → E) (g g' : E →ᵃ[ℝ] E)
    (hg : ∀ x ∈ S, g x = f x) (hg' : ∀ x ∈ S, g' x = f x) :
    ∀ x ∈ affineSpan ℝ S, g x = g' x :=
  fun x hx => AffineMap.eqOn_affineSpan (fun y hy => by rw [hg y hy, hg' y hy]) hx

/-- **(iii) the surjective case carries the set onto itself**: a surjective isometry of `S` in the
sense of (D3) agrees on `S` with an affine isometric automorphism `g` of `E`, and `g '' S = S`. -/
theorem exists_affineIsometryEquiv_of_isSurjIsometryOn [FiniteDimensional ℝ E] (S : Set E)
    (f : E → E) (hf : IsSurjIsometryOn S f) :
    ∃ g : E ≃ᵃⁱ[ℝ] E, (∀ x ∈ S, g x = f x) ∧ g '' S = S := by
  obtain ⟨hinto, honto, hdist⟩ := hf
  obtain ⟨g, hg⟩ := exists_affineIsometryEquiv_of_dist_eq S f hdist
  refine ⟨g, hg, ?_⟩
  rw [Set.image_congr hg]
  ext y
  constructor
  · rintro ⟨x, hx, rfl⟩
    exact hinto x hx
  · intro hy
    obtain ⟨x, hx, hfx⟩ := honto y hy
    exact ⟨x, hx, hfx⟩

end Extension

/-! ### `A26-0` — the verdict: the restricted metric and the mandatory affine extension -/

/-- **`A26-0`, the affine-extension theorem, three separate conjuncts.** (i) For every real
inner-product space `E` with `[FiniteDimensional ℝ E]`, every `S : Set E` and every `f : E → E`
preserving distances between points of `S`, there is `g : E ≃ᵃⁱ[ℝ] E` with `∀ x ∈ S, g x = f x`.
(ii) Under the same hypotheses, any two affine maps `g g' : E →ᵃ[ℝ] E` agreeing with `f` on `S`
agree on `affineSpan ℝ S`; uniqueness is asserted on the affine hull and nowhere else. (iii) The
instantiation: for every `f` with `IsSurjIsometryOn (normalizedSet Γ₀) f` at `Γ₀ ≡ ¼`, there is
`g` over the ambient space with its real structure with `∀ x ∈ normalizedSet Γ₀, g x = f x` and
`g '' normalizedSet Γ₀ = normalizedSet Γ₀`. The hypothesis on `f` in (i) and (ii) is distance
preservation on `S` and nothing else: no continuity, affinity, linearity, compactness of `S` or
surjectivity of `f` enters. -/
theorem a26_0_affine_extension :
    (∀ (E : Type) [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
        (S : Set E) (f : E → E), (∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y) →
        ∃ g : E ≃ᵃⁱ[ℝ] E, ∀ x ∈ S, g x = f x)
    ∧ (∀ (E : Type) [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
        (S : Set E) (f : E → E), (∀ x ∈ S, ∀ y ∈ S, dist (f x) (f y) = dist x y) →
        ∀ g g' : E →ᵃ[ℝ] E, (∀ x ∈ S, g x = f x) → (∀ x ∈ S, g' x = f x) →
        ∀ x ∈ affineSpan ℝ S, g x = g' x)
    ∧ (∀ Γ₀ : Matrix (Fin 4) (Fin 4) ℝ, Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
        ∀ f : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))
            → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
          IsSurjIsometryOn (normalizedSet Γ₀) f →
          ∃ g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))
              ≃ᵃⁱ[ℝ] EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)),
            (∀ x ∈ normalizedSet Γ₀, g x = f x) ∧ g '' normalizedSet Γ₀ = normalizedSet Γ₀) := by
  refine ⟨?_, ?_, ?_⟩
  · intro E _ _ _ S f hf
    exact exists_affineIsometryEquiv_of_dist_eq S f hf
  · intro E _ _ _ S f _ g g' hg hg'
    exact eqOn_affineSpan_of_agree S f g g' hg hg'
  · intro Γ₀ _ f hf
    exact exists_affineIsometryEquiv_of_isSurjIsometryOn (normalizedSet Γ₀) f hf

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms featureVec_ofLp
#print axioms dist_featureVec
#print axioms featureVec_gauge
#print axioms gramPhaseEquiv_of_featureVec_eq
#print axioms featureVec_mem_normalizedSet
#print axioms relabelled_fourier_mem_normalizedSet
#print axioms normalizedSet_eq_iUnion
#print axioms featureVec_image_eq
#print axioms bridge_of_tuple_isometry
#print axioms tuple_isometry_of_bridge
#print axioms inner_sub_eq_of_dist_eq
#print axioms exists_linearIsometryEquiv_of_inner_eq
#print axioms exists_affineIsometryEquiv_of_dist_eq
#print axioms eqOn_affineSpan_of_agree
#print axioms exists_affineIsometryEquiv_of_isSurjIsometryOn
#print axioms a26_0_affine_extension

end OrbitGeometryRigidity
end OIBridge
