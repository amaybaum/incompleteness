# A32 pre-freeze research: classifying the single-carrier normalized-space isometries

Read-only research at `origin/main` = `d61c6c5409db201e3c25abbf3ec0ecce1f530684`. The local branch
`main` is stale at `b9388cf`; `d61c6c5` is its descendant and is the head of the working tree.
Draft: `origin/claude/a32-orbit-isometry-classification` at `c20b0706`, which adds only the
preregistration draft. **Every computation here ran outside the kernel. It is exploration and
certifies nothing.** Scripts are in this directory: `circles.py`, `groups.py`, `members.py`,
`cover.py`, `cover_i.py`, `pairagree.py`, `phases.py`, `offc0.py`, `hull.py`, `cutspace.py`, plus
the three abandoned invariant probes `bilinear.py`, `trilinear.py` and `kappa.py`.

## 1. The frozen A26-2 object

Source: act 26 preregistration (blob `521b63cc…`), `verification/programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity/preregistration.md`.

- **Question** (L545–549): "At the single-carrier configuration, is every surjective isometry of
  the normalized space — every map on realizable tuples that preserves realizability, is surjective
  on classes and preserves the distance on realizable tuples — equal on classes to a member of act
  25's finite family, and if not, which kernel-certified map lies outside it, separated from every
  member on which exhibited class?"
- **Target statement** (L1180–1184): "for every `φ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 →
  Matrix (Fin 4) (Fin 4) ℂ)` satisfying the three hypotheses … the four-shape conclusion … **This is
  act 25's `ISO3` proposition, verbatim.**"
- **Hypotheses** (L671–675):
  ```
  (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))
    ∧ (∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)
    ∧ (∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)
  ```
  with `Γ₀ = Matrix.of (fun _ _ => (1/4 : ℝ))` and
  `d = fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)`.
- **The four-shape conclusion (the family)** (L697–710). It asks for **one** `π τ` that serves every `G`:
  ```
  ∃ π τ : Equiv.Perm (Fin 4),
      (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
    ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
          GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
    ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G →
          GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
    ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
          FibreGram (0 : Fin 1) U = G →
          GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))
  ```
  The generators are (L690–694): **(R)** `G ↦ fun i => (G (π i)).submatrix τ τ`; **(C)**
  `G ↦ fun i => Matrix.of fun j k => star (G i j k)`; **(T)** the dilation transpose, a relation
  through `AdmissibleDilationAt` and `FibreGram … Uᵀ`. That gives 576 × 4 = 2304 words, and they
  act on the union as 2304 distinct maps (§3).
- **The domain.** From `OrbitGeometryRigidity.lean` (blob `3e153841…`):
  - `featureVec` (L99–101) is `WithLp.toLp 2 (mixedTriple G)` in
    `EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))`.
  - `normalizedSet Γ₀` (L105–107) is the set of feature vectors of realizable tuples.
  - `IsSurjIsometryOn` (L111–112) is the set-level predicate.
  - The metric is the restricted ambient Euclidean metric (L609–621 of the preregistration).
  - The quotient is act 12's `GramPhaseEquiv` alone.
  - `mixedTriple G ((i₁,i₂,i₃),(j₁,j₂,j₃)) = G i₁ j₁ j₂ * G i₂ j₂ j₃ * G i₃ j₃ j₁`
    (`OrbitGeometrySelector.lean` L79–80).
- **The frozen negative form is unattainable.** The frozen `NOT-RIGID` witness (L1189–1192, L1304–1312)
  asks for one exhibited realizable `G` at which all four disjuncts fail for every `π τ`. Act 26's
  DF3 (result L1011–1016) found that no such class exists for any isometry: §19 item 5 says every
  per-circle map is realized by some member. A32 must therefore freeze the negation of the
  four-shape conclusion, where the separating class may depend on the member.

## 2. What act 26 proved, and where it stopped

Outcome vector (result L10): `A26-0-EXTENDS · A26-1-SEVERAL · A26-2-UNDECIDED · A26-3-NOT-EXECUTED`.

- `a26_0_affine_extension` (L444–458) has three conjuncts:
  - (i) Every map that preserves distances on a set `S ⊆ E`, with `E` finite-dimensional and real, agrees on `S` with some `E ≃ᵃⁱ[ℝ] E`.
  - (ii) Uniqueness holds on `affineSpan ℝ S`.
  - (iii) At `Γ₀ ≡ ¼`, every `f` with `IsSurjIsometryOn (normalizedSet Γ₀) f` has such a `g` with `g '' normalizedSet Γ₀ = normalizedSet Γ₀`.
- `rigid_motion_of_tuple_isometry` (L2309–2325) takes `φ` with h1–h3 and gives
  `∃ g : E ≃ᵃⁱ[ℝ] E, (∀ G, Realizable G → g (featureVec G) = featureVec (φ G)) ∧ g '' normalizedSet Γ₀ = normalizedSet Γ₀`.
- `a26_1_circle_census` (L508–518) is the `SEVERAL` branch.
- `a26_1_circle_count` (L2160–2288) gives nine circles `R = {1, swap 2 3, swap 1 2}²`. It states
  that the nine are pairwise non-coincident through `nc_0…nc_71`, and that every `(π,τ)`-circle
  equals one of them, through `perm_decomp` (L620) and `pred_stab` (L2134). The stabilizer is `P × P`.
- The stabilizer generators are `stab_row_swap13` (L556), `stab_col_swap13` (L568),
  `stab_row_double` (L581) and `stab_col_double` (L602). For the last two, the relabelled tuple
  is equivalent to `F(star z)`.
- Shared lemmas: `bridge_of_tuple_isometry` (L213), `tuple_isometry_of_bridge` (L251),
  `normalizedSet_eq_iUnion` (L165), `featureVec_gauge` (L133) and `dist_featureVec` (L126).
- **The stop** (result L478). Step 2, the marked set, was "not obtained". There are six classes on
  two circles, two on each circle at the parameters ±1, and "two points fix a circle's isometries
  only up to the reflection through them". What would settle it: "a kernel proof that every rigid
  motion carrying the normalized set onto itself is determined by finite data the set itself marks,
  or a different route".
- **The observation** (result §19 item 4, L949–958): "the isometries of the union of the nine
  circles number 36864, against 2304 for the action of act 25's family … the reflection of any
  single circle through its two marked points, the identity on the other eight, preserves every
  distance of the union … and is the action of no member of the family."

## 3. The mathematics (independent exact recomputation)

**Setup.** A realizable tuple at `A = Fin 1` is `G_i[j,k] = conj(U_ij) U_ik`, where `U` is a
complex Hadamard matrix divided by 2. Classes are taken modulo column phases. Every class is
`(π,τ)F(z)`, a point of the Fourier family `F4^(1)`. Each coordinate of `(π,τ)F(z)` is `S z^m/64`
with `S = ±1` and `m ∈ {-1,0,1}`. The exponent range is proved combinatorially: the exponent of the
Fourier matrix entry `M_ij` is `e_i e_j` with `e = (0,1,0,1)`, and a closed walk gives a total
exponent `Σ e_{i_k} δ_k` with the `δ` in `{-1,0,1}` summing to 0. The consequence is that each
circle is a round circle:

`x_r(e^{iθ}) = c_r + a_r cos θ + i b_r sin θ`

- `c_r`, `a_r` and `b_r` are real integer vectors over 64, with `|a_r|² = |b_r|² = 1536/64²`, so the radius² is 3/8.
- Centres and cosines lie in the real-coordinate subspace, and sines in the imaginary one.

**Exact facts** (`circles.py`, `hull.py`):

- The Gram matrix of the nine sine vectors is `1536·I`, so they are mutually orthogonal.
- The real rank of the centre differences together with the cosines is 5.
- The imaginary rank is 9, so the affine hull has **dimension 14**. This matches act 26's recorded observation.
- The six marked classes each lie on 3 circles. With the circles as edges they form **K₃,₃**,
  which is bipartite and 3-regular (`cutspace.py`).

**The normalized space.** It is K₃,₃ in ℝ⁵, with each edge replaced by a round circle through its
two endpoints. Each circle bulges into its own orthogonal direction `i b_r`.

**The isometry group** (`groups.py`). Every isometry permutes the circles, fixes the set of marked
points and extends affinely (A26-0). It is therefore a circle permutation σ, with signs
`z ↦ ±z^{±1}` on each circle, that preserves the Gram data of `{c_r − c_0, a_r, b_r}`.

- There are 72 pairs `(σ, ε)` (the automorphism group of K₃,₃), times 2⁹ free sine flips: **36864**.
- The family image on the union (a 42-point sample, faithful) has order **2304** = 72 · 32.
- The family's pure flips form a 5-dimensional binary code: the span of the rows and columns of
  the 3×3 grid of circles `r = (row coset, column coset)`.
- A single-circle flip is not in that code.

**The candidate.** `φ` is conjugation on the Fourier circle C₀ and the identity elsewhere.

- It **is an isometry.** Proof 1: sine orthogonality gives `|x−y|²` invariant under `θ → −θ` on one circle.
- Proof 2, which is kernel-friendly: φ agrees with a family **relabelling** on `C₀ ∪ C_r` for every `r ≠ 0`
  (`pairagree.py`, exact at the symbol level for all z and w). Four relabellings suffice:

  | member | (π, τ) | on C₀ | fixes circles | phases |
  | --- | --- | --- | --- | --- |
  | gA | `(1, (swap 0 3).trans (swap 1 2))` | acts as z̄ | 1, 4, 7 | constant |
  | gB | `(1, (swap 0 1).trans (swap 2 3))` | as z̄ (= `stab_col_double`) | 2, 5, 8 | constant |
  | gC | `((swap 0 3).trans (swap 1 2), 1)` | as z̄ | 3, 4, 5 | C₀: `![1,-star z,-1,star z]`; circle 3: `![1,-1,1,-1]` |
  | gD | `((swap 0 1).trans (swap 2 3), 1)` | as z̄ (= `stab_row_double`) | 6, 7, 8 | C₀: `![1,star z,-1,-star z]`; circle 6: `![1,-1,1,-1]` |

  Here "phases constant" means `(1,1,1,1)` (`phases.py`). Hence `d(φG, φH) = d(g_r G, g_r H) = d(G, H)`.
- Float control: the distance defect is 1.3e-14. Countercontrol: a quarter-turn of C₀ alone gives a defect of 0.85.
- **φ is outside the family.** It was checked exactly over all 2304 words: every word disagrees
  with φ at some class and coordinate (`cover.py`, assert passed). Separation also succeeds with
  every test class at the exact parameter z = i (`cover_i.py`). The greedy covers use
  (test circle, coordinate) pairs, 15 in total:
  - Shape 1 (6 pairs): (6, ((1,0,1),(0,1,3))), (1, ((0,2,3),(2,3,3))), (2, ((2,2,3),(1,3,2))),
    (5, ((1,3,3),(3,0,1))), (8, ((1,3,2),(2,1,3))), (0, ((1,3,2),(2,0,3))).
  - Shape 2 (5 pairs): (6, ((1,0,1),(0,1,3))), (1, ((0,2,3),(2,3,3))), (0, ((1,1,0),(2,1,1))),
    (8, ((1,3,2),(2,1,3))), (3, ((3,3,1),(2,3,3))).
  - Shape 3 (2 pairs): (4, ((0,3,0),(1,2,1))), (1, ((2,3,2),(1,1,2))).
  - Shape 4 (2 pairs): (3, ((0,3,0),(1,3,1))), (6, ((1,0,1),(0,1,3))).
  - Test classes `rF(i)` for r ≠ 0 are off C₀, witnessed by a C₀-constant coordinate such as
    `((0,0,1),(0,0,2))` (`offc0.py`).
- **Global invariants cannot separate.** Coordinate-permutation-invariant forms (bilinear, trilinear,
  slot-twisted) do not separate φ (`bilinear.py`, `trilinear.py`, `kappa.py`: zero hits). The reason
  is that global conjugation is itself the index reversal of the walk. Separation is therefore
  inherently member-by-member, a finite check.

**Prediction: NOT-RIGID, high.** RIGID is false at this configuration, and no RIGID proof exists.

## 4. Routes

**NOT-RIGID route (recommended).** It consumes:

- `iso2_classes_single` (Isometries L1081), `iso1_single_carrier` (L770: conj realizability,
  relabel/conj isometry, ∃U), `mixedTriple_relabel2` (L72), `mixedTriple_transpose` (L94),
  `fibreGram_unique` (L82), `relabel2_relabel2` (L488) and `relabel2_gramPhaseEquiv` (L290).
- `mixedTriple_gauge` (Selector L88) and `geo1_separation_single` (L412).
- `gramPhaseEquiv_refl/symm/trans` (GramTrajectorySelection L141/146/162).
- `hadamard_z_admissible` (OrbitLawGaps L116).
- From Rigidity: `stab_row_double` (L581), `stab_col_double` (L602), `a26_1_circle_count` (L2160),
  `perm_decomp` (L620), `pred_stab` (L2134), `featureVec_gauge` (L133) and `dist_featureVec` (L126).

The steps:

- N1. `conj F(z) = F(star z)` exactly, by `fin_cases`.
- N2. h1 and h2 from `iso1_single_carrier` (2), N1 and the class-invariance of the branch.
- N3. h3 has three cases: both points on C₀ (`conj_isometry`), neither (trivial), and the cross case.
  The cross case takes H ~ rF(w) with r ∈ R \ {(1,1)} (count (iii)), then applies the pair-agreement member for r:
  2 new C₀ lemmas (gA, gC), 8 fix lemmas and relabel isometry.
- N4. Separation. Push `¬`. For each shape and each π τ, take a test class and a coordinate from
  the cover above, using `mixedTriple_relabel2`/`_transpose` and `mixedTriple_gauge`.
  - Option (a): `decide` over `Perm (Fin 4)²`, with an integer/ZMod-4 exponent encoding of the values at z = i.
  - Option (b): `fin_cases π <;> fin_cases τ` with `first | …` over the cover and `norm_num [Complex.ext_iff]`, the idiom of the `nc_*` lemmas.
  - Option (c): reduce to `P×P` through `perm_decomp`, `pred_stab` and the `nc_*` witnesses, then run 64 cases per shape.
  - Hazard: kernel time.

**RIGID route.** None exists: the proposition is false. A frozen RIGID route (rigid motion,
circle permutation, per-circle signs, enumeration) would reach 36864 ≠ 2304 at enumeration.

**Blobs at main.**

| module | blob |
| --- | --- |
| OrbitGeometryRigidity | `3e15384196203939d348f2a313a873818ec4b684` |
| OrbitGeometryIsometries | `954fbddaa7511713a26c316b3b2e0f29497e81d2` |
| OrbitGeometrySelector | `ce9d1aa05dfdedfb5cac171cfe6379681942195f` |
| OrbitLawGaps | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| TwoSidedGauge | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| GramTrajectorySelection | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| DilationChoice | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| OIBridge.lean (import L215) | `7a6aaa6cd4011d03932a0c65fe622e6fc521b2c8` |
| census json | `97436abcb04df23a821a33e5bba463122647378e` |
| ROADMAP | `e6779380f858bcb905fc9877ed2f11bf5de75c95` |
| act-26 result | `76ebf0ffa512ce2e53868e529d42fbf9895a39d8` |

## 5. Name freedom at d61c6c5

`git grep -l` returns **zero hits** for each of `OrbitIsometryClassification`, `act-32`, `A32-`,
`a32_` and `A32`. The only occurrence is the draft preregistration on the A32 branch itself.
