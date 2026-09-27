# Track B act 34 — the product-embedded stratum: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #754. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A34.json`, and on the pull request.

- **`D`** — `a2f3d8209dba3133424f2609b2763a49a73c2174`, the head of `main` after act 33's landing
  and the roadmap restatement of #753.
- **`F`** — `f307515877a19ad137920824b7d19e74026fb738`, whose only parent is `D` and which adds the
  preregistration alone, blob `c388649116167055427f015ea2e6603a10b6d4a4`. Its `check-run` attestation
  is run 36297607823; the owner's designation is comment 5853089525 on #754.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A34-STRATIFIED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A34` | `A34-STRATIFIED`, theorem `a34_stratified` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a34_c_exclusive` and the eighteen statements required under this label:
- `A34-1`: `a34_shared_factor` and `a34_shared_inner`;
- `A34-2`: `a34_shared_cover`, `a34_shared_point`, `a34_shared_circle_left`,
  `a34_shared_circle_right`, `a34_shared_apart` and `a34_shared_count`;
- `A34-3`: `a34_shared_tensor` and `a34_shared_swap`;
- `A34-5`: `a34_shared_fibre`, `a34_shared_pairing` and `a34_shared_local`, with the corollary
  `a34_c_normal_form`;
- `A34-4`: `a34_control_proper`;
- the three controls `a34_control_product`, `a34_control_bits` and `a34_control_square`.

***

## The frozen post-round sentence

> At the frozen product configuration, the five-part product-stratum package holds, at evidence level 2: the feature map of a product tuple is the coordinatewise product of the factors' feature maps under the index pairing, so inner products of product feature vectors multiply; the product-embedded stratum is the union of the eighty-one tori, the products of pairs of act 26's nine relabelled Fourier circles, two tori meeting in a single point when both index pairs are adjacent in the incidence graph `K₃,₃`, in a shared circle when one index agrees and the other pair is adjacent, and not at all otherwise; act 33's group acts on the stratum factorwise by surjective isometries, and the factor exchange is a surjective isometry; the stratum is a proper subset of the product normalized set, by an exhibited realizable class with entries in the fourth roots of unity; and every surjective isometry of the stratum that factorizes through two single-carrier maps has both factors surjective isometries of the single-carrier normalized space, hence in act 33's group with unique normal forms. This is a statement about the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law, and it does not classify the isometries of the stratum or of the product normalized set.

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `tup r z` is the relabelled Fourier tuple of circle
`r` at the unit parameter `z`, `pt r z` its feature vector, `X ⊠ Y` the product tuple
`(X ⊠ Y) i j k = X i.1 j.1 k.1 · Y i.2 j.2 k.2`, `S` the stratum, `tor r s` the torus of the pair
`(r, s)`, `adj` the adjacency of two circles in the incidence graph `K₃,₃` and `μ r r'` the parameter
on circle `r` of the vertex it shares with circle `r'`.

**`A34-1`, `a34_shared_factor` and `a34_shared_inner`.** A coordinate of the feature map is a
product of three fibre entries; for a product tuple each entry is a product of an entry of `X` and
an entry of `Y`, and the six factors regroup (`a34_shared_fact`). The inner product of two feature
vectors is the sum over the product index of conjugate times value; reindexed by the pairing
`I₁₆ ≃ I₄ × I₄` (`Fintype.sum_equiv`) it is the double sum that `Finset.sum_mul_sum` folds into the
product of the two single-carrier inner products (`a34_shared_inner_core`).

**The metric of the stratum.** A realizable tuple's feature vector has norm one: with the dilation
of `sh1_sufficiency` every fibre entry is `star u_j · u_k` with `‖u_j‖² = ¼`, so every entry has
modulus `¼` (`a34_shared_entry_norm`), every coordinate modulus `1/64`, and the `4096` squared
moduli sum to one (`a34_shared_norm_sq_one`, `a34_shared_norm_one`, `a34_shared_inner_self`). The
inner product of the feature vectors of two tuples with Hermitian fibres is real: the involution
`((a, b, c), (d, e, f)) ↦ ((a, c, b), (e, d, f))` of the index set carries each coordinate to its
conjugate, so the sum equals its own conjugate (`a34_shared_real`). With
`dist² = ‖x‖² + ‖y‖² − 2 re⟨x, y⟩` (`a34_shared_dist_inner`) these give the squared distance of two
points of the stratum as `2 − 2·re⟨X, Z⟩·re⟨Y, W⟩` (`a34_shared_stratum_dist`), the real part of a
single-carrier inner product as `1 − dist²/2` (`a34_shared_re_of_dist`), and, fixing one realizable
factor, the exact reduction of the stratum distance to the single-carrier distance
(`a34_shared_fibre_core`).

**`A34-5`, `a34_shared_pairing`.** For realizable `Y` the coordinate at `((0,0,0),(0,0,0))` is
`(¼)³` by the diagonal condition (`a34_shared_diag_coord`); comparing the factorization at the
indices paired with it recovers `featureVec X` from `featureVec (X ⊠ Y)` coordinatewise, and
symmetrically `featureVec Y` (`a34_shared_pair_core`). Two products of feature-vector-equal factors
have equal feature vectors (`a34_shared_prod_congr`).

**`A34-2`, the tori.** Every relabelled Fourier tuple is realizable (`a34_shared_tup_real`, from act
25's `iso2_classes_single` circle by circle). The stratum is the union of the eighty-one tori
because a realizable single-carrier feature vector lies on one of the nine circles both ways
(`a33_shared_mem`; `a34_shared_cover_core`). Two points of circles `r`, `r'` coincide only as act
33's pairwise tables allow: for adjacent circles only at the shared vertex, whose parameters `μ r r'`
and `μ r' r` the tables `v₁`, `v₂` name (`a34_shared_meet_core`, from the thirty-six
`a33_shared_meet_…` lemmas over the eighty-one pairs), and the shared vertex is one point
(`a34_shared_vertex_core`, from `a33_shared_vertex`); for distinct non-adjacent circles never
(`a34_shared_apart_core`, from the thirty-six `a33_shared_apart_…` lemmas). Through the injectivity
of the pairing, two tori meet in the product of the two intersections: a single point when both
index pairs are adjacent (`a34_shared_point_core`), a shared circle when one index agrees and the
other pair is adjacent (`a34_shared_circle_left_core`, `a34_shared_circle_right_core`), and not at
all otherwise (`a34_shared_apart_tori_core`). The counts `1296` and `648` of ordered pairs of tori
meeting in a point and sharing a circle are decided by the kernel over the `6561` ordered pairs of
index pairs (`a34_shared_count`).

**`A34-3`, the action.** For surjective isometries `f`, `g` of the single-carrier normalized set, the
map of the ambient space that sends `featureVec (X ⊠ Y)` to `featureVec (X' ⊠ Y')`, with
`featureVec X' = f (featureVec X)` and `featureVec Y' = g (featureVec Y)` chosen classically and the
identity off the stratum, is well defined by the injectivity of the pairing, carries the stratum
onto itself because `f` and `g` are onto, and preserves the stratum's distances because they are
determined by the single-carrier distances through `a34_shared_stratum_dist` and
`a34_shared_re_of_dist` (`a34_shared_tensor_core`). The factor exchange is the same construction
with `(X, Y) ↦ (Y, X)`, isometric because the product of the two real parts commutes
(`a34_shared_swap_core`).

**`A34-5`, `a34_shared_local` and `a34_c_normal_form`.** Given `F` a surjective isometry of the
stratum with `F (featureVec (X ⊠ Y)) = featureVec (Φ₁ X ⊠ Φ₂ Y)` and realizable outputs, the map
`X ↦ Φ₁ X` is isometric on feature vectors of realizable tuples: fixing the second factor at a
realizable `Y₀`, the fibre reduction turns `dist (featureVec (Φ₁ X)) (featureVec (Φ₁ X'))` into a
stratum distance of two images under `F`, which `F` preserves, and back into
`dist (featureVec X) (featureVec X')`. The induced map `f` on the normalized set, chosen classically
and the identity elsewhere, is therefore well defined and isometric; it maps into the set by the
realizability of `Φ₁ X`, and onto it because `F` is onto the stratum and the pairing is injective.
Symmetrically for `g` with the first factor fixed (`a34_shared_local_core`). The corollary applies
`a33_classified` to `f` and to `g`.

**`A34-4`, `a34_control_proper`.** The witness matrix `H`, the Diţă twist of `F₄(i) ⊗ F₄(i)` whose
column blocks alternate `F₄(i)` and `F₄(−i)`, is the anchored block of the dilation
`U (p, a) (q, b) = H p q` over the one-element ancilla; `U` is unitary because the sixteen column
sums `∑ᵢ star (H i j) · H i k` are `δ_{jk}`, each column decided by direct evaluation
(`a34_shared_unit_col_…`), and `∑ₐ ‖U (i, a) (j, a₀)‖² = ‖H i j‖² = 1/16` is the product visible
family; so the tuple is realizable by act 12's `sh1_necessity`. It is the product of no two tuples:
every product has a paired feature matrix of rank one, so the `2 × 2` minor at the frozen four
indices vanishes for products by the factorization, while for the witness it is `−2i · 4⁻¹²`, by
direct evaluation.

**The controls.**
- `a34_control_product`: the untwisted tuple is `tup 0 i ⊠ tup 0 i` entrywise.
- `a34_control_bits`: circles `0` and `4` share the vertex at the parameter `1`
  (`a34_shared_vertex_core`), so the two products with the second factor `tup 3 i` coincide; the
  second-factor conjugation moves the point, since the pairing is injective and `z ↦ pt 3 z` is
  (`a34_shared_pt_inj`, from the nine `a33_shared_inj_…` lemmas).
- `a34_control_square`: with the second factor fixed the two stratum distances are the two
  single-carrier distances `dist (pt 0 (−1)) (pt 0 1)` and `dist (pt 0 i) (pt 0 1)`, which
  `a33_shared_cross` evaluates through the nine tables `a34_shared_N_0_0_…` of circle `0` against
  itself, decided by the kernel: `3/2` against `3/4`.

**`a34_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries eighty-two theorems, each followed by its `#print axioms`
line; 10 of them are decided by the kernel.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a34_shared_…`, `a34_c_…` other than `a34_c_exclusive`, or
`a34_control_…` consumes a verdict theorem or `a34_c_exclusive`, and `a34_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's module among
them — and it records a helper absent from that list as a deviation against the row it departs
from, not repaired. The following landed theorems, absent from the Provenance list, are consumed by shared lemmas — every one against the first row of the matrix, and none by a verdict theorem, a control or `a34_c_exclusive` directly:

| helper | landed in | consumed by |
| --- | --- | --- |
| `fibreGram_apply` | `TwoSidedGauge.lean` | `a34_shared_entry_norm`, `a34_shared_proper_core`, `a34_shared_product_core` |
| `iso2_classes_single` | `OrbitGeometryIsometries.lean` | `a34_shared_tup_real`, `a34_shared_product_core` |

Each is a landed, kernel-checked theorem of the modules the frozen import closes over; none is
re-proved or paraphrased. They are recorded here as the freeze requires and change no statement.

***

## The `P0` cell and the guard

On `A34-STRATIFIED` this round's sentence and its standing clause are appended once after act 33's
standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`57a2381ba243c8dd3905ad867accbc65311e55bb`, the blob rehearsed for this case before the freeze.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `c388649116167055427f015ea2e6603a10b6d4a4`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `f60ddfa87fc4621f49fe714706b468787cafc017` at stage 1.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 8 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 72 mutation controls fail as required` and
    `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on nine receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A34-STRATIFIED`, less this note:
  - added: the preregistration, `controls.py` and the module;
  - modified: `OIBridge.lean`, the census and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

The proofs were developed on a disposable branch from `F`, never landed: branch `claude/a34-dev`,
dispatch runs 36299395269, 36299880442 and 36300473449 red at the `Mathlib bridge` build (the last
of them on one open goal, the closing arithmetic of `a34_control_bits`); 36300803198 green there,
every theorem printing `propext`, `Classical.choice` and `Quot.sound`, on the module that stage 2
carries up to its docstring and the position of the verdict and corollary; and 36301205489 green
there on that module byte for byte. The disposable branch's workflow also printed a compact list of
the build's diagnostics after the build step, a change to that branch's workflow alone, and its
census carried a disposable family for the module; neither is part of the freeze.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

- The two helpers recorded above under the route-authorization matrix: `fibreGram_apply`, act 12's
  unfolding of a fibre-Gram entry, and act 25's `iso2_classes_single`, both landed and both inside
  the frozen import closure, consumed by shared lemmas only.
- `a34_control_proper` is proved through act 12's `sh1_necessity` from an admissible dilation whose
  anchored block is the witness matrix, rather than by verifying the four realizability conditions
  one by one as the route's step 6 sketched; the route names `sh1_necessity` among its ingredients
  and the statement is unchanged.
- `a34_shared_vertex_core`, the shared vertex of two adjacent circles as one point, is proved from
  act 33's twelve incidence equalities `a33_shared_inc_…` composed pairwise, since
  `a33_shared_vertex` states the implication from a coincidence to the vertex condition and not its
  converse. The Provenance list names the whole of act 33's module, so this is a choice within the
  authorized set and not a deviation.

None otherwise against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
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
