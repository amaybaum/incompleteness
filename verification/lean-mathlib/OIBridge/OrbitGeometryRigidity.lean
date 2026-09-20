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

end OrbitGeometryRigidity
end OIBridge
