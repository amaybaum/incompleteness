# Track B act 34 — the product-embedded stratum: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 34 proves five statements about the product-embedded stratum of act 29's product configuration, the
> feature vectors of the products of two realizable single-carrier tuples, and adopts none of them as
> anything but mathematics. The stratum is a mathematical object, a finite union of tori in a Euclidean
> space; its incidence structure, the action on it and the restriction it places on factorized
> surjective isometries are facts about that object and about nothing else. A `STRATIFIED` verdict
> settles the frozen five-part package, and a `NOT-STRATIFIED` verdict exhibits the failure of a named
> part; both leave the full product normalized set, which the round proves strictly larger than the
> stratum, unclassified. Neither verdict establishes that any admissible transition law is covariant
> under the stratum's isometries, selects a physical law or closes `P0`. No isometry, carrier, family,
> group or principle gains physical status by appearing here, and nothing here derives, recognises or
> approaches quantum evolution.

## The declarations

```v3-round
round A34
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-34-product-stratum/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-34-product-stratum/
record AM verification/receipts/A34.json
execution A verification/lean-mathlib/OIBridge/ProductStratum.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A34.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell.

## The objects

- **`D`** = `a2f3d8209dba3133424f2609b2763a49a73c2174`: the head of `main` after act 33's landing and
  the roadmap restatement of #753. It is certified by push run 36294382443: all three jobs green.
  Act 33's landing, `e4ca527292f11d4a4c74e463637c64eaa45474c3`, is certified by push run
  36292921173: the guard 91 PASS and 0 FAIL, the release gate 21 of 21 with `v3-receipts` holding on
  nine receipts. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A34.json`.

No other round runs beside A34 at this freeze. Should one land first, its movement of `main`
enters A34 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — the object.** The stratum `S`, the feature vectors of the products `X ⊠ Y` of two
realizable single-carrier tuples, is not the product normalized set, the feature vectors of every
tuple realizable at the product configuration. The pre-freeze computation found realizable
product-carrier classes off the stratum, and `A34-4` freezes one of them as an exact witness. Every
statement of this round is about `S`; none is about the product normalized set, and a verdict
here classifies nothing on the larger set. The freeze names `S` in every statement by its defining
formula, `let`-bound, and never by a definition.

**Hazard 2 — nine circles are not the analogue.** The product carrier does not carry nine circles
meeting in six points. It carries eighty-one tori, the products of pairs of circles, and their
incidence is the product of the two `K₃,₃` incidences: two tori share a circle when one index agrees
and the other pair is adjacent, a single point when both pairs are adjacent, and nothing otherwise.
The uncoloured circle-adjacency graph alone, the Cartesian square of the rook's graph `K₃ □ K₃`,
admits automorphisms mixing the two factors; the point-adjacency colouring excludes them. `A34-2`
freezes the coloured census, with the disjoint cases as countercontrols.

**Hazard 3 — reversibility is not surjectivity of the factors.** Act 21's `Reversible` is defined on
the whole admissible product orbit space: its surjectivity conjunct yields, for a target class, some
admissible preimage, which by Hazard 1 may lie off the stratum, where `FactorizesOnProduct` says
nothing. So `Reversible` cannot supply the surjectivity of the factor maps that `A34-5` needs.
`A34-5` therefore takes as hypothesis a surjective isometry of the stratum itself, at the feature
level, that factorizes through two single-carrier tuple maps with realizable outputs; nothing
about transition families, laws or dynamics is assumed, and the round does not claim that any
admissible law satisfies the hypothesis.

**Hazard 4 — the fibre reduction is exact only on unit vectors.** Fixing one tensor factor reduces
the stratum distance to the single-carrier distance because a realizable tuple's feature vector has
norm one. `A34-5`'s `FIBRE` statement carries realizability of the fixed factor as its hypothesis;
without it the identity is false in general.

**Hazard 5 — the corollary's normal forms are act 33's, verbatim.** `a34_c_normal_form` carries act
33's frozen normal-form text, with `f` and with `g`, and `controls.py` checks that the text is
byte-identical to act 33's `NF_UNIQ` component. The corollary consumes `a33_classified` and proves
nothing of act 33's over again.

**Hazard 6 — the witness is an explicit matrix, not an existence claim.** `A34-4` names its witness
in the statement: the Diţă twist of `F₄(i) ⊗ F₄(i)` whose column blocks alternate `F₄(i)` and
`F₄(−i)`, with entries in the fourth roots of unity scaled by `1/4`. Realizability is proved of that
matrix, and non-membership in the stratum through one explicit `2 × 2` minor of the paired feature
matrix, exact over the Gaussian rationals. The untwisted matrix is the control: it lies on the
stratum, as the product of two Fourier tuples.

**Hazard 7 — the package is not a classification.** `A34-STRATIFIED` means the five-part package
holds. It does not mean that the wreath action of act 33's group is the whole isometry group of the
stratum; that classification is not posed here, and nothing in this file licenses it. A later act
may pose it, after the off-stratum classes are described.

**Hazard 8 — history.** Act 33 recorded `A33-CLASSIFIED`, act 32 `A32-NOT-RIGID`, act 29 to act 31
their product-configuration verdicts. All stand as recorded. A decided outcome here is stated as a
fact about the stratum, never as a revision of an earlier round's verdict.

**Hazard 9 — vocabulary.** An isometry of the stratum is not a symmetry, the group acting on it is
not a symmetry group of anything physical, covariance under it is a hypothesis this round does not
assert of any law, and none is written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `sh1_sufficiency`, `posSemidef_factor_of_rank_le`, `gramPhaseEquiv_refl`,
  `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`;
- **act 18**, `IntermediateCrossTimeStructure.lean` — `prod_mem_unitaryGroup` and `prod_admissible`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `Reversible` and `FactorizesOnProduct` as the
  declarations this round's hypotheses are distinguished from, `realizable_of_gramPhaseEquiv`,
  `witness_supply`, `product_cross`, `relabel_product`, `relabel_one`, `vpart_unitary`,
  `product_realizable` and `product_separations`;
- **act 23**, `OrbitLawGaps.lean` — `hadamard_z_admissible`;
- **act 24**, `OrbitGeometrySelector.lean` — `mixedTriple`, `mixedTriple_gauge`, `mixedTriple_star`,
  `coord_le_dist`, `geo1_separation_star`, `realizable_entry_ne_zero`, `geo1_separation_single`
  and `dist_eq_norm_toLp`;
- **act 25**, `OrbitGeometryIsometries.lean` — `mixedTriple_relabel2`, `fibreGram_unique`,
  `relabel2_realizable`, `relabel2_isometry` and `conj_isometry`;
- **act 26**, `OrbitGeometryRigidity.lean` — `featureVec`, `normalizedSet` and `IsSurjIsometryOn`,
  the three definitions this round's statements are made of; `featureVec_ofLp`, `dist_featureVec`,
  `featureVec_gauge`, `gramPhaseEquiv_of_featureVec_eq`, `featureVec_mem_normalizedSet`,
  `relabelled_fourier_mem_normalizedSet`, `normalizedSet_eq_iUnion`, `eqOn_affineSpan_of_agree`,
  `exists_affineIsometryEquiv_of_isSurjIsometryOn`, `a26_0_affine_extension` and
  `a26_1_circle_count`;
- **act 33**, `OrbitIsometryGroup.lean` — the whole module as landed at `D`: `a33_classified`,
  `a33_c_exclusive`, every `a33_c_…`, every `a33_control_…` and every `a33_shared_…` theorem. In
  particular `a33_shared_mem` (the normalized set is the union of the nine circles), the
  seventy-two `a33_shared_apart_…` and `a33_shared_meet_…` pairwise tables with `a33_shared_census`,
  `a33_shared_coord`, `a33_shared_cross`, `a33_shared_pt_inj`, `a33_shared_two_points`,
  `a33_shared_vertex`, `a33_shared_relabel_iso`, `a33_shared_iso_comp`, `a33_shared_real`,
  `a33_shared_nf_unique`, `a33_shared_exists_nf`, `a33_shared_dist_of_sq` and the unit lemmas
  `a33_shared_unit_…`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `featureVec`, `normalizedSet`, `IsSurjIsometryOn`, `featureVec_gauge` | `verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean` | 99, 105, 111, 133 |
| `gramPhaseEquiv_of_featureVec_eq`, `featureVec_mem_normalizedSet`, `relabelled_fourier_mem_normalizedSet`, `normalizedSet_eq_iUnion` | `the same file` | 139, 147, 154, 165 |
| `eqOn_affineSpan_of_agree`, `exists_affineIsometryEquiv_of_isSurjIsometryOn`, `a26_0_affine_extension`, `a26_1_circle_count` | `the same file` | 408, 415, 444, 2160 |
| `mixedTriple`, `mixedTriple_gauge`, `mixedTriple_star`, `coord_le_dist` | `verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean` | 79, 88, 114, 123 |
| `geo1_separation_star`, `realizable_entry_ne_zero`, `geo1_separation_single`, `dist_eq_norm_toLp` | `the same file` | 337, 385, 412, 439 |
| `mixedTriple_relabel2`, `fibreGram_unique`, `relabel2_realizable`, `relabel2_isometry`, `conj_isometry` | `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean` | 72, 82, 273, 300, 313 |
| `Reversible`, `FactorizesOnProduct`, `realizable_of_gramPhaseEquiv`, `witness_supply` | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | 123, 143, 355, 431 |
| `product_cross`, `relabel_product`, `relabel_one`, `vpart_unitary`, `product_realizable`, `product_separations` | `the same file` | 963, 975, 986, 993, 1015, 1093 |
| `prod_mem_unitaryGroup`, `prod_admissible` | `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | 851, 881 |
| `hadamard_z_admissible` | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | 116 |
| `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm`, `gramPhaseEquiv_trans` | `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | 141, 146, 162 |
| `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `sh1_necessity`, `posSemidef_factor_of_rank_le`, `sh1_sufficiency` | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | 95, 102, 108, 168, 1002, 1070 |
| `a33_shared_coord`, `a33_shared_order`, `a33_shared_cross`, `a33_shared_pt_inj` | `verification/lean-mathlib/OIBridge/OrbitIsometryGroup.lean` | 41, 69, 277, 400 |
| `a33_shared_apart_0_1` (the first of the pairwise tables), `a33_shared_mem`, `a33_shared_census`, `a33_shared_into` | `the same file` | 804, 2428, 2486, 2723 |
| `a33_shared_circles`, `a33_shared_form`, `a33_shared_signs`, `a33_shared_composition`, `a33_shared_relabel_iso` | `the same file` | 2915, 3019, 3059, 3284, 3348 |
| `a33_shared_dist_of_sq`, `a33_shared_real`, `a33_shared_two_points`, `a33_shared_nf_unique`, `a33_shared_vertex`, `a33_shared_exists_nf` | `the same file` | 5010, 5603, 5648, 5669, 5727, 5914 |
| `a33_classified`, `a33_c_exclusive` | `the same file` | 7102, 7135 |

| file at `D` | blob |
| --- | --- |
| `OrbitIsometryGroup.lean` | `f4215071b6bfb560626327626a71ea86aaf5b3fc` |
| `OrbitGeometryRigidity.lean` | `3e15384196203939d348f2a313a873818ec4b684` |
| `OrbitGeometryIsometries.lean` | `954fbddaa7511713a26c316b3b2e0f29497e81d2` |
| `OrbitGeometrySelector.lean` | `ce9d1aa05dfdedfb5cac171cfe6379681942195f` |
| `OrbitIsometryClassification.lean` | `98ed25c5b5c355d7c3929a32d656c729d2f678ea` |
| `OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge.lean` | `aed1598b29af06170c5577c78a491aafaa76987a` |
| `verification/lean-manuscript-census.json` | `30488574b02ac1a7b9201e541aa8e601a53ce2f7` |
| `verification/ROADMAP.md` | `32b4886983ce2e9026e3ec2afdc9f827f9d96801` |
| `verification/lean/edge_rigidity_probe.py` | `d28e9b3cf2093984a1c453892204b9932a685b2e` |

The names this round introduces return nothing from `git grep -l` at `D`: `ProductStratum`,
`act-34`, `A34-` and `a34_`.

***

## Why this round exists

Act 33 classified the isometries of the single-carrier normalized space: nine circles, six shared
points, the incidence graph `K₃,₃`, nine conjugation bits, a group of order 36864. The roadmap's
structural direction asks whether that geometry survives the product/composition layer on which
acts 28 to 30 compare the remaining dynamical freedom. The pre-freeze computation answered that the
naïve target, the same nine-circle object again, is the wrong one: the feature map factorizes
exactly on product tuples, so the geometry survives factorwise, as eighty-one tori with the product
incidence and the factorwise action of act 33's group, on a stratum that is a proper subset of the
product normalized set. This round freezes that finding as five statements, with the properness
witness among them so that a verdict on the stratum cannot be read as a verdict on the whole
product carrier, and adds the one statement that turns the geometry back toward `P0`: a surjective
isometry of the stratum that factorizes through two single-carrier maps has both factors in act
33's group.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from the landed act-26 relabellings, the landed feature map
and act 29's product configuration, in floating point where a tolerance is stated and exactly
otherwise; the scripts are kept off the repository.

- **The factorization.** With `(X ⊠ Y) i j k = X i.1 j.1 k.1 · Y i.2 j.2 k.2`, the feature vector of
  `X ⊠ Y` is, after pairing the factor indices, the tensor product of the feature vectors of `X`
  and `Y`; inner products multiply. Checked to `10⁻¹⁵` on random Fourier points. It is an identity of
  the coordinate formula: each of the three factors of a mixed-triple coordinate of the product is
  the product of the corresponding factors, one from each side.
- **The tori.** The stratum is the union over the eighty-one pairs `(r, s)` of the images of
  `(z, w) ↦ fv (tup r z ⊠ tup s w)`, each a product of two circles with the squared distance
  `2 − 2·⟨x, x'⟩·⟨y, y'⟩`, the single-carrier inner products being real (largest imaginary part
  `7·10⁻¹⁸` over eighty-one random pairs).
- **The incidence.** The nine circles meet pairwise in exactly one point when their `K₃,₃` edges share
  a vertex and never otherwise, eighteen meeting pairs and eighteen apart pairs at grid distance at
  least `√(3/2)`, six shared points each on three circles, at the parameters `±1`, as act 33's
  census states. The pairing `(x, y) ↦ x ⊗ y` is injective on pairs of circle points, the scalar of
  a rank-one factorization being fixed by the real positive coordinate `1/64` at any index
  `((a, a, a), (a, a, a))`, which every realizable tuple carries since its diagonal is `Γ₀`. Hence
  two tori meet in a single point when both index pairs are adjacent (648 unordered pairs), in a
  shared circle when one index agrees and the other pair is adjacent (324 unordered pairs), and not
  at all otherwise; thirty-six points lie on nine tori each and one hundred and eight shared circles
  on three each. The automorphisms of the coloured incidence structure inside
  `Aut(K₃ □ K₃ □ K₃ □ K₃) = S₃ ≀ S₄` number exactly `10368 = 72² · 2`, all of product-or-swap form;
  the uncoloured circle-adjacency alone admits the factor-mixing automorphisms.
- **The action.** For every tested pair of act 33 isometries (the identity, global conjugation, one
  single-circle conjugation, a family kernel element, two generators and mixed pairs),
  `(x, y) ↦ f x ⊗ g y` preserves the stratum's distances to `2·10⁻¹⁵`; the factor exchange is
  realized on ambient tuples by the relabelling `(i₁, i₂) ↦ (i₂, i₁)` of the product carrier.
- **A per-torus conjugation bit is not a map.** On the shared circle `{p} × circle s`, where `p` is
  the point circles `0` and `4` share at the parameter `1`, the tori `(0, s)` and `(4, s)` would send
  `(p, w)` to `(p, w̄)` and to `(p, w)`, distinct points; each factor's bits are functions of that
  factor's circle alone, eighteen bits, not eighty-one.
- **The properness witness.** The row tuple of the Fourier matrix of order sixteen, scaled to
  entries of modulus `1/4`, is realizable at the product configuration with a paired feature matrix
  of full tensor rank. The Diţă twist of `F₄(i) ⊗ F₄(i)` with column blocks `F₄(i), F₄(−i), F₄(i),
  F₄(−i)` is unitary with entries in `{±1, ±i}/4`, realizable, and its paired feature matrix has
  rank-one residual `0.866` in the Frobenius norm against `0` for the untwisted control; the residual
  stays at least `0.998` under thirty random relabellings of the product carrier. Exactly over the
  Gaussian integers, with the entries scaled by four, the `2 × 2` minor at rows `(2,0,2,0,2,2)`,
  `(2,3,2,1,3,3)` and columns `(1,0,2,0,2,3)`, `(0,3,2,3,0,3)` of the paired matrix, in the
  `(a₁ … f₁)`, `(a₂ … f₂)` indexing, is `−2i` for the twisted tuple and `0` for the control; twenty
  thousand random minors of the control all vanish.
- **The fibre reduction.** Fixing the second factor, the stratum distance between `(x, y)` and
  `(x', y)` equals the single-carrier distance between `x` and `x'` (largest deviation `3·10⁻¹⁴`);
  the countercontrol map that squares the parameter on circle `0`, tensored with the identity,
  changes stratum distances by up to `1.127`.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems themselves decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- The single-carrier visible family `Γ₀ = Matrix.of (fun _ _ => 1/4)`, bound by hypothesis in every
  statement; the ancilla `Fin 1` and the anchor `0`, act 12's single carrier; act 26's
  `normalizedSet Γ₀` and `IsSurjIsometryOn`.
- The product carrier `Fin 4 × Fin 4`, the ancilla `Fin 1 × Fin 1`, the visible family
  `Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2`, act 29's product configuration with the ordered
  decomposition `Equiv.refl`; the product embedding `prod X Y i = Matrix.of fun j k => X i.1 j.1 k.1
  * Y i.2 j.2 k.2`, act 21's inline form, `let`-bound.
- The stratum `S`, the set of `featureVec (prod X Y)` over realizable `X`, `Y`; the tori `tor r s`;
  act 26's nine circles as the table `R`, the tuple `tup r z` and the point `pt r z`; the six shared
  points as act 33's tables `v₁`, `v₂`; adjacency `adj` of two circles (distinct, sharing a vertex)
  and the meeting parameter `μ r r'` (`1` when the vertex `v₁ r` is shared, else `−1`), all
  `let`-bound in every statement that uses them.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/ProductStratum.lean` opens with exactly
`import OIBridge.OrbitIsometryGroup`, its docstring, `namespace OIBridge`,
`namespace ProductStratum`, and the one `open`:

```lean
open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup

```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement.

### `P_R` — the package

The conjunction, over one head, of the incidence census `INC` (five statements), the action `ACT`
(two statements) and the factorized-isometry statement `LOCAL`:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ((S = ⋃ (r : Fin 9) (s : Fin 9), tor r s)
  ∧ (∀ r r' s s' : Fin 9, adj r r' → adj s s' →
    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))})
  ∧ (∀ r s s' : Fin 9, adj s s' →
    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))})
  ∧ (∀ r r' s : Fin 9, adj r r' →
    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))})
  ∧ (∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →
    tor r s ∩ tor r' s' = ∅))
  ∧ ((∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →
    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →
        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y'))
  ∧ (∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)))
  ∧ (∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →
    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →
    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧
      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))
```

### `P_N` — its negation

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ¬ ((S = ⋃ (r : Fin 9) (s : Fin 9), tor r s)
  ∧ (∀ r r' s s' : Fin 9, adj r r' → adj s s' →
    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))})
  ∧ (∀ r s s' : Fin 9, adj s s' →
    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))})
  ∧ (∀ r r' s : Fin 9, adj r r' →
    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))})
  ∧ (∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →
    tor r s ∩ tor r' s' = ∅))
  ∨ ¬ ((∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →
    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →
        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y'))
  ∧ (∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)))
  ∨ ¬ (∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →
    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →
    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧
      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))
```

`P_N` is `P_R`'s negation pushed through the outer conjunction. `controls.py` rebuilds both from the
shared components and rejects any drift.

### `A34-1` — the product geometry, required under both decided labels

`FACT`, `a34_shared_factor` — the feature map of a product tuple is the coordinatewise product of
the factors' feature maps under the index pairing:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (p : ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))),
    mixedTriple (prod X Y) p = mixedTriple X ((p.1.1.1, p.1.2.1.1, p.1.2.2.1), (p.2.1.1, p.2.2.1.1, p.2.2.2.1)) * mixedTriple Y ((p.1.1.2, p.1.2.1.2, p.1.2.2.2), (p.2.1.2, p.2.2.1.2, p.2.2.2.2))
```

`INNER`, `a34_shared_inner` — inner products of product feature vectors multiply:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
    inner ℂ (featureVec (prod X Y)) (featureVec (prod X' Y')) = inner ℂ (featureVec X) (featureVec X') * inner ℂ (featureVec Y) (featureVec Y')
```

### `A34-2` — the tori and their incidence, required under `A34-STRATIFIED`

`COVER`, `a34_shared_cover`:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  S = ⋃ (r : Fin 9) (s : Fin 9), tor r s
```

`POINT`, `a34_shared_point` — two tori whose index pairs are both adjacent meet in one point:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ r r' s s' : Fin 9, adj r r' → adj s s' →
    tor r s ∩ tor r' s' = {featureVec (prod (tup r (μ r r')) (tup s (μ s s')))}
```

`CIRC_L`, `a34_shared_circle_left` — same first index, adjacent second indices: a shared circle:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ r s s' : Fin 9, adj s s' →
    tor r s ∩ tor r s' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s')))}
```

`CIRC_R`, `a34_shared_circle_right`:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ r r' s : Fin 9, adj r r' →
    tor r s ∩ tor r' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r')) (tup s w))}
```

`APART`, `a34_shared_apart` — a distinct non-adjacent index pair on either side: disjoint tori:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ r r' s s' : Fin 9, (r ≠ r' ∧ ¬ adj r r') ∨ (s ≠ s' ∧ ¬ adj s s') →
    tor r s ∩ tor r' s' = ∅
```

`COUNT`, `a34_shared_count` — the ordered pairs of tori meeting in a point number 1296 and those
sharing a circle 648, decided by the kernel over act 33's vertex tables:

```lean
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  (Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => (q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1)) ∧ (q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2)))).card = 1296
  ∧ (Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => (q.1.1 = q.2.1 ∧ (q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2))) ∨ (q.1.2 = q.2.2 ∧ (q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1))))).card = 648
```

### `A34-3` — the action, required under `A34-STRATIFIED`

`TENSOR`, `a34_shared_tensor` — two surjective isometries of the single-carrier normalized set act
on the stratum as a surjective isometry, factorwise:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g →
    ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
      ∀ X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →
        f (featureVec X) = featureVec X' → g (featureVec Y) = featureVec Y' → F (featureVec (prod X Y)) = featureVec (prod X' Y')
```

`SWAP`, `a34_shared_swap` — the factor exchange is a surjective isometry of the stratum:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∃ F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))), IsSurjIsometryOn S F ∧
    ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → F (featureVec (prod X Y)) = featureVec (prod Y X)
```

### `A34-5` — factorized surjective isometries, required under `A34-STRATIFIED`

`FIBRE`, `a34_shared_fibre` — fixing one realizable factor reduces the stratum distance to the
single-carrier distance:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (X X' Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ Y →
    dist (featureVec (prod X Y)) (featureVec (prod X' Y)) = dist (featureVec X) (featureVec X')
    ∧ dist (featureVec (prod Y X)) (featureVec (prod Y X')) = dist (featureVec X) (featureVec X')
```

`PAIR`, `a34_shared_pairing` — the pairing is injective on realizable factors:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (X Y X' Y' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ X' → RealizableGram (Fin 1) Γ₀ Y' →
    featureVec (prod X Y) = featureVec (prod X' Y') → featureVec X = featureVec X' ∧ featureVec Y = featureVec Y'
```

`LOCAL`, `a34_shared_local` — a surjective isometry of the stratum that factorizes through two
single-carrier tuple maps with realizable outputs induces two surjective isometries of the
single-carrier normalized set:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →
    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →
    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧
      ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)
```

`NFORM`, `a34_c_normal_form` — its corollary through `a33_classified`: each factor has a unique act
33 normal form:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  ∀ (F : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) → EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) (Φ₁ Φ₂ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)), IsSurjIsometryOn S F →
    (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → RealizableGram (Fin 1) Γ₀ (Φ₁ X) ∧ RealizableGram (Fin 1) Γ₀ (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →
    ∃ f g : EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧
      (∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X → RealizableGram (Fin 1) Γ₀ Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))
      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),
    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (if νε.2 r then z else star z))
    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        f (pt r z) = pt s (-(if νε.2 r then z else star z))))
      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),
    (∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))
    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →
        g (pt r z) = pt s (if νε.2 r then z else star z))
    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →
        g (pt r z) = pt s (-(if νε.2 r then z else star z))))
```

### `A34-4` — the stratum is proper, required under both decided labels

`PROPER`, `a34_control_proper` — the Diţă-twisted tuple is realizable at the product configuration
and is the product of no two tuples:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I); 1, -1, 1, -1; 1, -(if j.1.val % 2 = 0 then Complex.I else -Complex.I), -1, (if j.1.val % 2 = 0 then Complex.I else -Complex.I)] i.2 j.2
  RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)
  ∧ ∀ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, featureVec (prod X Y) ≠ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)
```

### The controls, required under both decided labels

`PRODUCT`, `a34_control_product` — the untwisted tuple lies on the stratum:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.1 j.1 * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] i.2 j.2
  ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k)
```

`BITS`, `a34_control_bits` — the shared point of circles `0` and `4` gives one point of two tori,
and the second-factor conjugation moves it:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  featureVec (prod (tup 0 1) (tup 3 Complex.I)) = featureVec (prod (tup 4 1) (tup 3 Complex.I))
  ∧ featureVec (prod (tup 0 1) (tup 3 Complex.I)) ≠ featureVec (prod (tup 0 1) (tup 3 (star Complex.I)))
```

`SQUARE`, `a34_control_square` — squaring the parameter on circle `0` with the second factor fixed
changes a stratum distance:

```lean
∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  dist (featureVec (prod (tup 0 (Complex.I * Complex.I)) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))
    ≠ dist (featureVec (prod (tup 0 Complex.I) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))
```

### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A34-STRATIFIED` | `a34_stratified` | `P_R` |
| `A34-NOT-STRATIFIED` | `a34_not_stratified` | `P_N` |
| corollary, required in every case | `a34_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A34-1`, required under both decided labels | `a34_shared_factor` | `FACT` |
| `A34-1`, required under both decided labels | `a34_shared_inner` | `INNER` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_cover` | `COVER` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_point` | `POINT` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_circle_left` | `CIRC_L` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_circle_right` | `CIRC_R` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_apart` | `APART` |
| `A34-2`, required under `A34-STRATIFIED` | `a34_shared_count` | `COUNT` |
| `A34-3`, required under `A34-STRATIFIED` | `a34_shared_tensor` | `TENSOR` |
| `A34-3`, required under `A34-STRATIFIED` | `a34_shared_swap` | `SWAP` |
| `A34-5`, required under `A34-STRATIFIED` | `a34_shared_fibre` | `FIBRE` |
| `A34-5`, required under `A34-STRATIFIED` | `a34_shared_pairing` | `PAIR` |
| `A34-5`, required under `A34-STRATIFIED` | `a34_shared_local` | `LOCAL` |
| `A34-5` corollary, required under `A34-STRATIFIED` | `a34_c_normal_form` | `NFORM` |
| `A34-4`, required under both decided labels | `a34_control_proper` | `PROPER` |
| control, required under both decided labels | `a34_control_product` | `PRODUCT` |
| control, required under both decided labels | `a34_control_bits` | `BITS` |
| control, required under both decided labels | `a34_control_square` | `SQUARE` |

A module with neither verdict theorem reports `A34-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a34_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The elaboration file is `verification/lean-mathlib/OIBridge/ProductStratum.lean` on those
branches. Under the frozen header it carries `#check` commands and nothing else; the branches also
carry a disposable census family for the module and a diagnostics step in their workflow, neither
of which is part of the freeze.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36296861494 | `d204841a6108a9fc85bfd6d372058f0d498e9804` | **the twenty frozen propositions and the corollary of this file**, exactly as frozen, as twenty-one `#check` commands under the frozen header, wired directly after `OrbitIsometryGroup`, with no census family | the `Mathlib bridge` build is green: all twenty-one `#check`s elaborate and no error is reported; the job is red only at the release gate's `lean-manuscript` step, the new module carrying no census family. The kernel check and the numerical probes are green |
| 36297196513 | `4ad2037476059119524c03356ce9aeeae736e0a0` | the same, with a disposable census family for the module | all three jobs green. All twenty-one `#check`s elaborate and no error is reported; the release gate passes all 21 steps with nine receipts holding |
| 36297226027 | `432820d0fc16832108bedfc751bfc1248f2cf7c1` | **the countercontrol**: the head of the second run with one deliberate defect, an extra argument to `tup` in `P_R`'s `POINT` conjunct | red, as required. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/ProductStratum.lean:37:61: Application type mismatch`, at that argument; the kernel check and the numerical probes are green |

The countercontrol shows that the elaboration check has force: an ill-typed frozen statement fails
the build at its own line, and nothing else fails. The disposable census family and the
diagnostics step are recorded for what they are and are not part of the freeze.

***

## The question, FROZEN — one target

### `A34` — the product-embedded stratum

**At act 29's product configuration, does act 33's geometry survive on the product-embedded
stratum factorwise — the eighty-one tori with the product of the two `K₃,₃` incidences, the
factorwise action of act 33's group with the factor exchange, and the restriction of every
factorized surjective isometry of the stratum to act 33's group on each factor — while the stratum
is a proper subset of the product normalized set?**

The answer is reported as one of three labels:
- `A34-STRATIFIED`, the theorem `P_R`;
- `A34-NOT-STRATIFIED`, the theorem `P_N`;
- `A34-UNDECIDED`.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the geometry | `a34_shared_factor`, `a34_shared_inner` | the exact identity every other statement rests on, required whichever label is earned |
| properness | `a34_control_proper` | the stratum is not the product normalized set, required whichever label is earned |
| the stratum is reached | `a34_control_product` | the untwisted witness is a product point, so `PROPER`'s twist is what leaves the stratum |
| incidence positive | `a34_control_bits` | a point of two tori through a shared point, and the conjugation that moves along the shared circle |
| non-isometric factor kill | `a34_control_square` | a factor map outside act 33's group breaks a stratum distance, so `LOCAL`'s hypothesis has force |
| incidence negative | the disjoint cases of `a34_shared_apart` | a non-adjacent pair on either side gives disjoint tori |
| duality | `a34_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`A34-1`.** `FACT` by unfolding `mixedTriple` and `prod`: each of the three factors of a
   coordinate of the product tuple is the product of the corresponding factors of `X` and `Y`, and
   the six-fold product regroups. `INNER` by the sum over the product index, which splits as the
   product of the two sums through `Fintype.sum_prod_type` after the index pairing.
2. **`A34-5`, `FIBRE` and `PAIR`.** A realizable tuple's feature vector has norm one: each entry of a
   fibre of a realizable tuple at `Γ₀ ≡ ¼` with ancilla `Fin 1` is `star u_j · u_k` with `|u_j|² = ¼`
   (`sh1_sufficiency` and `fibreGram_unique`, or `realizable_entry_ne_zero`'s method), so every
   coordinate has modulus `1/64` and the `4096` coordinates sum to one. `FIBRE` is then `INNER` with
   the fixed factor's inner product equal to one. `PAIR`: the coordinate `((a, a, a), (a, a, a))` of a
   realizable tuple is `(¼)³` by the diagonal condition; comparing `FACT` at indices paired with it
   gives `featureVec X = featureVec X'` coordinatewise, and symmetrically for `Y`.
3. **`A34-2`.** `COVER` from `a33_shared_mem` in both directions. `POINT`, `CIRC_L`, `CIRC_R`, `APART`
   from `PAIR` and act 33's pairwise tables: a point of `tor r s ∩ tor r' s'` is `fv (tup r z ⊠ tup s
   w) = fv (tup r' z' ⊠ tup s' w')`, so `pt r z = pt r' z'` and `pt s w = pt s' w'`, which
   `a33_shared_apart_…` excludes for a non-adjacent distinct pair and `a33_shared_meet_…` forces to
   the shared parameter for an adjacent pair, `a33_shared_vertex` naming the shared point; the
   converse inclusions are the definitions. `COUNT` is decided by the kernel over the `6561` ordered
   pairs of index pairs.
4. **`A34-3`.** `TENSOR`: define `F` on the ambient space to agree with `x ⊗ y ↦ f x ⊗ g y` on the
   stratum, choosing for each point of `S` a pair `(X, Y)` (`PAIR` makes the choice immaterial) and
   the identity off `S`; distances are preserved by `INNER` and the isometry of `f` and `g` on the
   single-carrier set, and `F` is onto `S` because `f` and `g` are. `SWAP` by the same construction
   with `(x, y) ↦ (y, x)`, or by `relabel_product` with the coordinate exchange and
   `relabel2_isometry`.
5. **`A34-5`, `LOCAL` and `NFORM`.** Define `f` on `normalizedSet Γ₀` by `featureVec X ↦ featureVec
   (Φ₁ X)` and the identity elsewhere. Well defined: if `featureVec X = featureVec X'` then, with any
   realizable `Y`, `FIBRE` gives `dist (fv (Φ₁ X ⊠ Φ₂ Y)) (fv (Φ₁ X' ⊠ Φ₂ Y)) = dist (F (fv (X ⊠ Y)))
   (F (fv (X' ⊠ Y))) = dist (fv (X ⊠ Y)) (fv (X' ⊠ Y)) = 0`, and `FIBRE` again reads off `featureVec
   (Φ₁ X) = featureVec (Φ₁ X')`. Isometric by the same identity; into the set by the realizability of
   `Φ₁ X`; onto because `F` is onto `S`: a target `fv X''` with any realizable `Y''` is `F` of some
   `fv (X ⊠ Y)`, whose image is `fv (Φ₁ X ⊠ Φ₂ Y)`, and `PAIR` gives `featureVec (Φ₁ X) = featureVec
   X''`. Symmetrically for `g`. `NFORM` applies `a33_classified` to `f` and to `g`.
6. **`A34-4` and the controls.** `PROPER`: realizability of the named tuple by `sh1_necessity`'s
   four conditions read directly — each fibre is a rank-one Hermitian outer product, the sum is
   `Hᴴ H = 1` by the unitarity of the Diţă product (each column block unitary, `prod_mem_unitaryGroup`
   or the sixteen-by-sixteen evaluation), the diagonal `|H i j|² = 1/16`; non-membership by `FACT`:
   every product tuple has a paired feature matrix of rank one, so the frozen `2 × 2` minor vanishes
   on products, while for the named tuple it is `−2i · 4⁻¹²`, by exact evaluation. `PRODUCT` with
   `X = Y = tup 0 Complex.I`, entrywise. `BITS` by `a33_shared_vertex` and `a33_shared_pt_inj`.
   `SQUARE` by `FIBRE` and act 33's within-circle distance `(3/4)(1 − cos)`, `3/2` against `3/4`.
7. **`a34_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

No route to `A34-NOT-STRATIFIED` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a34_shared_…` and every `a34_c_…` other than `a34_c_exclusive` | either verdict theorem; `a34_c_exclusive` |
| every `a34_control_…` | either verdict theorem; `a34_c_exclusive` |
| `a34_not_stratified` | `a34_shared_cover`, `a34_shared_point`, `a34_shared_tensor`, `a34_shared_local` |
| `a34_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A34` | `A34-STRATIFIED` | **very high** | the factorization is a coordinate identity; the incidence census follows from act 33's landed pairwise tables through the injectivity of the pairing; the action and the factorized-isometry statement are one-line consequences of the fibre reduction; the properness witness is an exact minor; every frozen statement elaborates |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A34-STRATIFIED`

> At the frozen product configuration, the five-part product-stratum package holds, at evidence level 2: the feature map of a product tuple is the coordinatewise product of the factors' feature maps under the index pairing, so inner products of product feature vectors multiply; the product-embedded stratum is the union of the eighty-one tori, the products of pairs of act 26's nine relabelled Fourier circles, two tori meeting in a single point when both index pairs are adjacent in the incidence graph `K₃,₃`, in a shared circle when one index agrees and the other pair is adjacent, and not at all otherwise; act 33's group acts on the stratum factorwise by surjective isometries, and the factor exchange is a surjective isometry; the stratum is a proper subset of the product normalized set, by an exhibited realizable class with entries in the fourth roots of unity; and every surjective isometry of the stratum that factorizes through two single-carrier maps has both factors surjective isometries of the single-carrier normalized space, hence in act 33's group with unique normal forms. This is a statement about the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law, and it does not classify the isometries of the stratum or of the product normalized set.

### `A34-NOT-STRATIFIED`

> At the frozen product configuration, the five-part product-stratum package fails, at evidence level 2: the incidence census of the eighty-one tori, the factorwise action of act 33's group with the factor exchange, or the restriction of factorized surjective isometries of the stratum to act 33's group is false, and the witness is exhibited in the kernel; the exact factorization of the feature map and the properness of the stratum hold. This is a statement about the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law.

### `A34-UNDECIDED`

> Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it.

### The corollary, REQUIRED

`a34_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label.

| row | outcome |
| --- | --- |
| 1 | `A34-STRATIFIED` |
| 2 | `A34-NOT-STRATIFIED` |
| 3 | `A34-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 33's sentence and its standing
clause:

> At the single-carrier configuration, the surjective isometries of the normalized space are classified: each permutes the nine relabelled Fourier circles by an automorphism of their incidence graph `K₃,₃` and conjugates the parameter on an arbitrary subset of the circles, 36864 in all, and act 25's four-shape family is a subgroup of index 16. `P0`'s threading part is untouched, no isometry of the normalized space is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A34-STRATIFIED`:**

  > At the product configuration, the feature map factorizes exactly on product tuples, the product-embedded stratum is the union of eighty-one tori whose incidence is the product of the two `K₃,₃` incidences, act 33's group acts on it factorwise together with the factor exchange, the stratum is a proper subset of the product normalized set by an exhibited realizable class, and every surjective isometry of the stratum that factorizes through two single-carrier maps has both factors in act 33's group: a finite geometric restriction conditional on stratum-isometry covariance. Nothing here establishes that any admissible law is covariant under the stratum's isometries or reaches the classes outside the stratum, `P0`'s threading part is untouched, no isometry of the stratum is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

- **`A34-NOT-STRATIFIED`:**

  > At the product configuration, the five-part product-stratum package fails at a named part, by a witness exhibited in the kernel, while the feature map factorizes exactly on product tuples and the stratum is a proper subset of the product normalized set by an exhibited realizable class. Nothing here establishes that any admissible law is covariant under the stratum's isometries or reaches the classes outside the stratum, `P0`'s threading part is untouched, no isometry of the stratum is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On `A34-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `57a2381ba243c8dd3905ad867accbc65311e55bb` (`A34-STRATIFIED`);
- `fc6a886b8cc20e078bc77a2028285903e9564fa5` (`A34-NOT-STRATIFIED`).

The guard run locally at `D` against each rehearsed cell reports 91 PASS and 0 FAIL, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 33's `A33-CLASSIFIED`, act 32's `A32-NOT-RIGID` or any verdict of acts
  28 to 31.** Those are the verdicts those rounds recorded, and they stand.
- **No outcome classifies the isometries of the stratum**, and none classifies the isometries of
  the product normalized set. `A34-STRATIFIED` says that act 33's group acts and that factorized
  surjective isometries have factors in it; it does not say that the wreath action is every
  isometry of the stratum.
- **No outcome says anything about the classes outside the stratum** beyond their existence, which
  `A34-4` proves. Their description is the precondition of any later global classification round
  and is not this round's.
- **No outcome reports anything about transition families or dynamics.** `A34-5` is conditional on
  stratum-isometry covariance stated at the feature level; nothing here establishes that any
  admissible law satisfies it, and none closes `P0`, which stays `OPEN`.
- **No isometry, group or covariance is called canonical, physical or fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard;
- write any manuscript file;
- import any Mathlib module into the frozen module beyond what `OrbitIsometryGroup` imports.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; the tables `R`,
`tup`, `pt`, `v₁`, `v₂`, `prod`, `S`, `tor`, `adj`, `μ` and the witness matrices `H` are `let`-bound
inside each statement that uses them.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within `propext`,
`Classical.choice` and `Quot.sound`.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-34-product-stratum/controls.py`, blob
**`f60ddfa87fc4621f49fe714706b468787cafc017`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction, over the frozen head, of the frozen `INC`, `ACT` and
    `LOCAL` texts, and `P_N` the disjunction of their negations, rebuilt from the shared components;
    `INC` is the conjunction of the five frozen incidence texts and `ACT` of the two frozen action
    texts.
  - Every other statement carries the one head (or the finite header), the one adjacency text, the
    one witness text and the one normal-form text, verbatim, in the frozen multiplicities; the
    corollary's normal-form text is act 33's `NF_UNIQ` component byte for byte.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a34_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a34_c_exclusive`;
  - carries the statements the earned label requires.
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen sentence for the case appended, or to
  `D`'s.
- **The guard** is byte-identical to `D`'s.
- **The census** is `D`'s with exactly one family appended, last, for `ProductStratum`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.ProductStratum` inserted directly after
  `import OIBridge.OrbitIsometryGroup`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files and the module;
  - modified: `OIBridge.lean` and the census;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 8 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies 72 mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 8 duality mutations fail as required
controls: 3 rows hold as frozen, 72 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module and the controls.**
   - `controls.py` with its frozen blob.
   - The module with the frozen header and its shared lemmas. On the route to `A34-STRATIFIED`
     these include `A34-1` to `A34-5`, the corollary `a34_c_normal_form` and the three controls.
   - The import line.

   No verdict theorem and no corollary `a34_c_exclusive`.
2. **Stage 2 — the verdict.** `a34_stratified` or `a34_not_stratified`, or neither, and
   `a34_c_exclusive`.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last. On a decided
   outcome only, the `P0` sentence for the case.
4. **The result note** `result.md`, whose commit is `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40). A stage whose build fails is followed by a fixing
commit, never rewritten. The label is read from the module at `E`. Proofs may be developed first on
a disposable branch from `F`, never landed; such runs are design evidence and the result note
names them.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the frozen propositions elaborate as frozen | before `F`: the elaboration runs above; at `E`: `C8`, every frozen theorem compiled under its statement |
| every verdict and control is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary, controls and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces are exactly the frozen ones for the case, and the guard is untouched | `C9` |
| the guard stays green | `C8`: 91 checks, all `PASS`, in `D`'s order |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen propositions unchanged** is repaired by later
  linear commits before `E`.
- **A verdict that cannot be obtained** is reported `A34-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A34-UNDECIDED` with the missing statement named. A verdict prints only over green controls.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is either of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken —
    in particular `A34-1` or `A34-4` false as frozen, which no label absorbs.

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
