# Track B act 36 — the Diţă factorization hierarchy at the product-embedded stratum: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 36 proves statements about Diţă's construction over the factorizations of the sixteen-point carrier at
> act 29's product configuration, about an exact one-parameter family of realizable classes through act 34's
> certified rational stratum point, and about one named point of that family, and adopts none of them as
> anything but mathematics. The hulls of the hierarchy are mathematical objects, images of explicit
> parametrizations in a Euclidean space; their realizability, the membership of the family in the `2 × 8`
> hull, and the position of the named point off the stratum are facts about those objects and about nothing
> else. A `HIERARCHY` verdict settles the frozen package, and a `NOT-HIERARCHY` verdict exhibits the failure
> of a named part; the exact-computation layer, and not the kernel, carries the statement that the named
> point admits no `4 × 4` Diţă factorization of either orientation, so that the `4 × 4` Diţă hierarchy is
> locally insufficient at the stratum; and both verdicts leave open whether every realizable class near the
> stratum lies in some Diţă hull of some factorization, which the round records as open and does not decide,
> and both leave the product normalized set unclassified. Neither verdict establishes that any admissible
> transition law is covariant under any isometry, selects a physical law or closes `P0`. No hull, family,
> factorization, isometry, carrier, group or principle gains physical status by appearing here, and nothing
> here derives, recognises or approaches quantum evolution.

## The declarations

```v3-round
round A36
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-36-dita-hierarchy/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-36-dita-hierarchy/
record AM verification/receipts/A36.json
execution A verification/lean-mathlib/OIBridge/DitaHierarchy.lean
execution A verification/lean/dita_hierarchy_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A36.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is. The workflow changes by one token: the round's
probe is appended to the list the `Numerical probes` job runs, and `controls.py` checks that the
workflow at `E` is `D`'s with exactly that token inserted.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell. The roadmap's section *The residual deformation space at the
product stratum*, landed at `D`, is not edited by this round.

## The objects

- **`D`** = `8b33e25fcb7e5b464cbfc605f61f7d40e5825784`: the head of `main` after the documentation
  landing of pull request #756, itself after act 35's landing `b6b899e6…`. It is certified by push
  run 36318313840: all three jobs green, the release gate 21 of 21 with `v3-receipts` holding on
  eleven receipts, `lean-axioms` 4766 named results with no sorry, the guard 91 PASS and 0 FAIL,
  and the `Numerical probes` job green with act 35's probe reporting its `OK` line. Every
  measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A36.json`.

No other round runs beside A36 at this freeze. Should one land first, its movement of `main`
enters A36 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — the negative statement is local, exact, and the probe's.** What the exact-computation
layer establishes is that one named point, `P = SIG ∘ u₆₀^W` of defect 37, and one further point of
the same line, `Pu u₅`, admit no `4 × 4` Diţă factorization of either orientation at any block
structure, and no `8 × 2` factorization, while each admits exactly one `2 × 8` factorization of each
orientation. The sentence this licenses is that **the `4 × 4` Diţă hierarchy is locally insufficient
at the certified stratum point**: a continuous `2 × 8` Diţă deformation passes through the product
point and, at its named point, lies in no `4 × 4` hull, so the family lies in no `4 × 4` hull. It is
not a statement about a neighbourhood, not a statement about Diţă's construction as such, and never
written as "Diţă geometry is insufficient". The kernel proves the family's `2 × 8` membership and the
point realizable and off the stratum; it proves nothing negative about factorizations.

**Hazard 2 — the hierarchy is not exhausted.** That the first escaping family belongs to the `2 × 8`
construction is a statement about `P` and the family through it. Whether every realizable class
near the stratum lies in some Diţă hull of some factorization of the sixteen-point carrier is
**open**; the round records it and does not decide it, and a `HIERARCHY` verdict is not evidence
that the hierarchy exhausts anything. The failure of the `4 × 4` hulls is not converted into a
claim that the `2 × 8` hulls, or the hierarchy, succeed.

**Hazard 3 — two verification layers, kept apart.** The theorems of the module are kernel-checked
and print their axioms: the general construction's realizability, its `2 × 8` and `8 × 2` instances,
the family's membership in the `2 × 8` hull with its realizability, the named point's position off
the stratum, and the stratum control. The defect values, the factorization searches, the first-order
census, the `4 × 4` hulls through the stratum point and their span, the stabilizer and its sectors,
and the second-order certificates are exact integer and Gaussian-rational arithmetic replayed by the
frozen probe `verification/lean/dita_hierarchy_probe.py`, run by the `Numerical probes` job at every
execution commit from stage 1 on, and so at `E`. The probe's statements are exact but not
kernel-certified; the result note, the census family and the `P0` sentence name the layer of every
claim, and no claim of one layer is written as a claim of the other.

**Hazard 4 — what the factorization search enumerates.** A column Diţă factorization
`H[(a,b),(c,d)] = X[a,c]·D[c,b]·Y_c[b,d]` with `m` outer and `n` inner indices, up to row and
column bijections, partitions the columns into `m` blocks of `n` on each of which the rows fall
into `n` proportionality classes of `m` rows, the classes being the same on every block. The probe
enumerates every such block structure of the point — every `n`-subset of columns on which the rows
fall into classes of exactly `m`, every partition of the columns into such subsets, and the row
classes they induce — and, for each, reconstructs the factors canonically up to the gauge and tests
the rank-one condition and the flat unitarity of every factor exactly. "Candidates" counts the
block structures that pass the proportionality test; "exact factorizations" counts those whose
reconstructed factors are flat unitaries satisfying the rank-one condition. The row form is the
same search on the transpose. The search is exhaustive over the structures a factorization must
induce, so a count of zero is a proof, in exact arithmetic, that no factorization of that shape
exists at that point.

**Hazard 5 — the defect is a linearized quantity at a point.** It bounds from above the dimension
of any family of realizable classes through the point; 49 at the stratum point and 37 at `P` are
values at those points, and "generic" is not asserted of either.

**Hazard 6 — the second-order census is about named directions relative to the fixed-pairing
hulls, and the obstruction certificate is direction-dependent.** The stabilizer sectors of
dimensions 8, 8, 4, 2 and 1 are exact common eigenspaces of the class sums on the residual
`R = ker DF / (gauge + T)`, `T` the tangents of act 35's two fixed-pairing hulls. "Quadratically
obstructed by certificate" means that for a direction `v`, `B(v, v)` lies outside the linear span of
`B(v, T)` and `B(T, T)` in the cokernel, so no correction in `T` cancels the second-order term; it is
a sufficient certificate of obstruction at that direction and nothing else. The probe tests it at
three pseudo-random integer combinations of each sector's basis, from a fixed seed, and asserts it
at all three for each 8-dimensional sector; it also asserts that the certificate **fails** at every
one of the eight structured basis vectors of each 8-dimensional sector, since a direction absorbed
by a hull through the point, or any direction whose `B(v, v)` the span happens to contain, cannot
carry it. The pre-freeze design run of a first draft, which tested one structured integer
combination per sector, found the certificate failing there, which is how the dependence was
caught. The statement frozen is therefore that generic directions of the two 8-dimensional sectors
are obstructed by the certificate, not that every direction is. "Extended by an explicit row-hull
correction" means that a correction `t ∈ T_r` with `B(v + t, v + t) = 0` exists and is exhibited at
the tested direction. Neither is the existence or non-existence of a curve of realizable classes,
except where a straight line is shown exact, and neither is a statement relative to the hulls of
the other orientations.

**Hazard 7 — the `4 × 4` hulls through the stratum point span the defect at first order only.** The
492 hulls, their common tangent dimension 14 and their span 49 are first-order statements at
`SIG`; they do not say the hulls fill a neighbourhood, and `P` shows a realizable class near `SIG`
in none of them.

**Hazard 8 — the frozen line is not the measurement's direction.** The pre-freeze measurement
found its straight lines from the extended sector directions and named a point of defect 33 on one
of them. The frozen exponent matrix `W`, supported on the even row-blocks and even column-blocks
with the entries `[b = 1] + [d = 1]`, was chosen afterwards for its exponents `0, 1, 2`; the probe
asserts of it exactly that it lies in `ker DF` and is an exact straight line, and of `P` and of the
second point `Pu u₅`, `u₅ = (3+4i)/5`, that their defect is 37 and their factorization counts are
those frozen below. Whether `W` lies in the four-dimensional sector is not asserted. The measurement's
direction and its point of defect 33 are design evidence and are not the frozen ones.

**Hazard 9 — history.** Act 35 recorded `A35-DITA-STRATIFIED` with its open modulus, act 34
`A34-STRATIFIED`, act 33 `A33-CLASSIFIED`, act 32 `A32-NOT-RIGID`, act 29 to act 31 their
product-configuration verdicts. All stand as recorded. A decided outcome here is stated as a fact
about the construction, the family and the named point, and answers act 35's open modulus for the
`4 × 4` hulls only, re-posing it for the hierarchy; it is never a revision of an earlier round's
verdict.

**Hazard 10 — vocabulary.** A hull is a family of classes, a factorization is a way of writing a
matrix, an isometry is not a symmetry, the group acting is not a symmetry group of anything
physical, covariance under it is a hypothesis this round does not assert of any law, and none is
written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `sh1_sufficiency`, `fibreGram_apply`, `fibreGram_diag`,
  `posSemidef_factor_of_rank_le`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and
  `gramPhaseEquiv_trans`;
- **act 18**, `IntermediateCrossTimeStructure.lean` — `prod_mem_unitaryGroup` and `prod_admissible`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `realizable_of_gramPhaseEquiv`, `product_cross`,
  `relabel_product`, `relabel_one`, `vpart_unitary`, `product_realizable` and
  `product_separations`;
- **act 23**, `OrbitLawGaps.lean` — `hadamard_z_admissible`;
- **act 24**, `OrbitGeometrySelector.lean` — `mixedTriple`, `mixedTriple_gauge`, `mixedTriple_star`,
  `coord_le_dist`, `geo1_separation_star`, `realizable_entry_ne_zero`, `geo1_separation_single`
  and `dist_eq_norm_toLp`;
- **act 25**, `OrbitGeometryIsometries.lean` — `mixedTriple_relabel2`, `mixedTriple_transpose`,
  `fibreGram_unique`, `relabel2_realizable`, `relabel2_gramPhaseEquiv`, `relabel2_isometry`,
  `conj_isometry`, `transpose_admissible`, `transpose_unitary`, `transpose_descends` and
  `transpose_isometry`;
- **act 26**, `OrbitGeometryRigidity.lean` — `featureVec`, `normalizedSet` and `IsSurjIsometryOn`;
  `featureVec_ofLp`, `dist_featureVec`, `featureVec_gauge`, `gramPhaseEquiv_of_featureVec_eq`,
  `featureVec_mem_normalizedSet`, `relabelled_fourier_mem_normalizedSet` and
  `normalizedSet_eq_iUnion`;
- **act 33**, `OrbitIsometryGroup.lean` — the whole module as landed at `D`;
- **act 34**, `ProductStratum.lean` — the whole module as landed at `D`, in particular
  `a34_shared_entry_norm`, `a34_shared_hermitian`, `a34_shared_diag_coord`, `a34_control_product`,
  `a34_shared_product_core` and `a34_stratified`;
- **act 35**, `DitaHull.lean` — the whole module as landed at `D`: `a35_dita_stratified`,
  `a35_c_exclusive`, every `a35_control_…` and every `a35_shared_…` theorem. In particular
  `a35_shared_f4_flat`, `a35_shared_dita_unitary`, `a35_shared_dita_norm`, `a35_shared_pad_unitary`,
  `a35_shared_gram_realizable`, `a35_shared_hull_core`, `a35_shared_hull_t_core`,
  `a35_shared_sigma_core`, `a35_shared_cross_core`, `a35_shared_diag_core`, `a35_shared_untw_core`,
  `a35_shared_unit_of_norm`, `a35_shared_norm_of_unit`, `a35_shared_star_mul`, `a35_shared_half`,
  `a35_shared_cross`, `a35_shared_hull`, `a35_shared_hull_t` and `a35_control_untwisted`;
- **Mathlib** — `Fin.divNat`, `Fin.modNat`, `finProdFinEquiv`, `Equiv.symm`, `Fintype.card`,
  `Matrix.unitaryGroup`, `Matrix.mem_unitaryGroup_iff`, `Matrix.mem_unitaryGroup_iff'`,
  `Matrix.submatrix`, `Matrix.submatrix_mul_equiv`, `Matrix.transpose`, `Fintype.sum_prod_type`,
  `Fintype.sum_equiv`, `Finset` and the algebra of `ℂ`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `a35_shared_f4_flat`, `a35_shared_dita_unitary`, `a35_shared_dita_norm`, `a35_shared_pad_unitary`, `a35_shared_gram_realizable` | `verification/lean-mathlib/OIBridge/DitaHull.lean` | 70, 84, 115, 122, 140 |
| `a35_shared_hull_core`, `a35_shared_hull_t_core`, `a35_shared_sigma_core`, `a35_shared_cross_core`, `a35_shared_diag_core`, `a35_shared_untw_core` | `the same file` | 160, 173, 207, 236, 248, 386 |
| `a35_shared_unit_of_norm`, `a35_shared_norm_of_unit`, `a35_shared_star_mul`, `a35_shared_half` | `the same file` | 35, 41, 28, 60 |
| `a35_shared_hull`, `a35_shared_hull_t`, `a35_shared_cross`, `a35_control_untwisted`, `a35_dita_stratified`, `a35_c_exclusive` | `the same file` | 583, 612, 703, 953, 981, 1023 |
| `a34_shared_entry_norm`, `a34_shared_hermitian`, `a34_shared_diag_coord`, `a34_control_product`, `a34_shared_product_core`, `a34_stratified` | `verification/lean-mathlib/OIBridge/ProductStratum.lean` | 81, 141, 174, 1451, 984, 1514 |
| `featureVec`, `normalizedSet`, `featureVec_gauge`, `featureVec_mem_normalizedSet` | `verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean` | 99, 105, 133, 147 |
| `transpose_unitary`, `relabel2_realizable` | `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean` | 357, 273 |
| `vpart_unitary`, `product_realizable` | `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | 993, 1015 |
| `hadamard_z_admissible` | `verification/lean-mathlib/OIBridge/OrbitLawGaps.lean` | 116 |
| `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `fibreGram_apply`, `sh1_necessity`, `sh1_sufficiency` | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | 95, 102, 108, 115, 168, 1070 |
| `AdmissibleDilationAt` | `verification/lean-mathlib/OIBridge/DilationChoice.lean` | 134 |

| file at `D` | blob |
| --- | --- |
| `DitaHull.lean` | `5404decfe03ddced08aa4143a549601766fc9785` |
| `ProductStratum.lean` | `36c4f450a116934082a57b5cb65d1f9133c750bd` |
| `OrbitGeometryRigidity.lean` | `3e15384196203939d348f2a313a873818ec4b684` |
| `OrbitGeometryIsometries.lean` | `954fbddaa7511713a26c316b3b2e0f29497e81d2` |
| `OrbitLawRigidityTwisted.lean` | `860daac4eb20dbe92c35c2b3ca7aaa1ed798e7b8` |
| `OrbitLawGaps.lean` | `5ed0dad78d87314dfd9e1a8ec241f479ded1e3e1` |
| `TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/lean-mathlib/OIBridge.lean` | `bf97092908df96b2c271c22ee4b7cd2877f39547` |
| `verification/lean-manuscript-census.json` | `094a5dfff295bbd6b9ccbd9b6c64a1b8004e1313` |
| `verification/ROADMAP.md` | `ebaf8abd4b9552e11dfcd54af63d523f13a2b0e1` |
| `verification/lean/edge_rigidity_probe.py` | `d28e9b3cf2093984a1c453892204b9932a685b2e` |
| `verification/lean/dita_defect_probe.py` | `99f98ca79b0089d15cf9babb9ca965e88598cfa6` |
| `.github/workflows/verify.yml` | `c9aba8033c7b05d3c3446a530e576fd81313ac6a` |

The names this round introduces return nothing from `git grep -l` at `D`: `DitaHierarchy`,
`act-36`, `A36-`, `a36_` and `dita_hierarchy`.

***

## Why this round exists

Act 35 placed the product-embedded stratum inside the column and row Diţă hulls at the fixed
pairing and left an open modulus with its countercontrol: at the certified rational stratum point
the defect is 49 and the two hulls' tangents span 26, so 23 first-order directions were unaccounted
for, and whether the relabelled hulls exhaust the realizable classes near the stratum was recorded
open. The measurement that followed, at `D`, took the residual apart. It found that the `4 × 4`
Diţă hulls through the point in every orientation — fixed, swapped, mixed and parity — span the
whole defect at first order, so the residual of act 35 is a fixed-pairing artefact at first order;
that the stabilizer of the point splits the residual into five sectors, two of them quadratically
obstructed relative to the fixed-pairing hulls by an exact cokernel certificate and three
extendable; that the extensions of the extendable sectors are exact straight lines of realizable
classes lying in none of the `4 × 4` hulls; and that an exact point on such a line, realizable and
off the stratum, admits no `4 × 4` Diţă factorization of either orientation at any block structure
while admitting exactly one `2 × 8` factorization. Act 35's open modulus is thereby answered in the
negative for the `4 × 4` hulls and re-posed for the hierarchy of Diţă's construction over the
factorizations of the sixteen-point carrier. This round freezes what the measurement established
exactly — the general construction's realizability, an exact family through the stratum point
inside the `2 × 8` hull, the named point off the stratum, and the probe's exact counts — and
records the hierarchy's exhaustion as open, so that the next round can be scoped around the
hierarchy instead of around the `4 × 4` hulls.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from act 35's frozen probe objects at the certified
rational stratum point `SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, in the phase
coordinates `θ ∈ ℝ²⁵⁶`, `F(θ) = (H ∘ e^{iθ})(H ∘ e^{iθ})* − 16·I`; exact arithmetic where "exact" is
stated, floating point with a tolerance otherwise; the scripts are kept off the repository except
the frozen probe.

- **First order, exact.** `rank DF = 176`; `dim ker DF = 80`; the gauge of row and column phases
  has rank 31; the defect `Def = ker DF / gauge` is 49; act 35's two fixed-pairing hulls have
  tangents `T_c`, `T_r` of dimension 14 each modulo the gauge, meeting in the stratum's two circle
  directions, spanning 26; the residual `R = ker DF / (gauge + T)` is 23; the cokernel of `DF` is
  64.
- **Second order, exact.** The form `B : Sym²(Def) → coker DF`, the class of `−½ D²F`, descends to
  `Def` (its value on gauge times kernel is zero) and vanishes exactly on `Sym²(T_c)` and on
  `Sym²(T_r)`, so each fixed-pairing hull integrates; its rank on `Sym²(Def)` is 47.
- **The stabilizer of the point in `G_ext`**, exact on exponent and phase data: order 1024 — the
  product relabellings fixing each factor up to phases, the conjugation with the column swap
  `1 ↔ 3` in each factor, and the transpose; no factor exchange, `z ≠ w` — with 112 conjugacy
  classes. On `R` it has isotypic sectors of dimensions 8, 8, 4, 2 and 1, exact common eigenspaces
  of the class sums.
- **Every `4 × 4` Diţă orientation through the point**, by the exhaustive block-structure search:
  five column and five row block structures pass the proportionality test, four of each are exact
  factorizations — the fixed pairing, the swapped pairing, a mixed regrouping, and a parity
  regrouping whose five factors are real `4 × 4` Hadamard matrices with three Fourier circles
  through each, so that it carries `3⁵ = 243` hulls per form. In all **492** hulls, each of tangent
  dimension 14 modulo the gauge, every tangent in `ker DF` with `D²F` vanishing exactly on it, and
  the span of all their tangents modulo the gauge is **49**, the whole defect.
- **The sectors' fates relative to `T`**, exact: the two 8-dimensional sectors are not isotropic
  under `B` and are quadratically obstructed at random directions, by the certificate
  `B(v, v) ∉ span{B(v, T), B(T, T)}`, which fails at their structured basis vectors (Hazard 6); the
  4-, 2- and 1-dimensional sectors are isotropic and extend, with an explicit correction `t ∈ T_r`
  giving `B(v + t, v + t) = 0`. The 1- and 2-dimensional sectors lie in every parity `4 × 4` hull;
  the 4-dimensional sector lies in no single `4 × 4` hull.
- **Straight lines.** The second-order extensions of the extendable sectors were found to be exact
  straight lines — every level-set sum of the `c_k` over `k ↦ w_ik − w_jk` vanishes, all 120 pairs
  — lying in none of the 492 hull tangents; a Gauss–Newton continuation confirmed them numerically
  against hull, generic and obstructed controls. On one of them, at `u = (60+i)/(60−i)`, an exact
  unimodular Hadamard matrix of defect 33 admitted no `4 × 4` Diţă factorization of either
  orientation at any block structure and exactly one `2 × 8` factorization; the same at two further
  points. The frozen line `W` of this round, chosen for its exponents, and its point `P` of defect
  37 are described under the exact-computation layer; the measurement's point is not frozen.
- **Diţă factorizations of every shape** at the stratum point, exact: `2 × 8`, three block
  structures per form, all exact; `8 × 2`, three per form, two exact; `4 × 4`, five per form, four
  exact.
- **The quadratic closure.** The quadrics on `Def` vanishing on all 492 hull tangents form a space
  of dimension 527, counted modulo a prime, and the 47 quadrics of `B` lie inside it; the
  second-order cone of `B` is not the quadratic closure of the hull union. This and the
  representation of the stabilizer on the cokernel are design evidence, not frozen.
- **What was not found.** No clean quadratic coupling law between the sectors and `T`: the
  couplings are dense, the image of `B` has commutant dimension 27 under the transpose-free
  stabilizer, and the mode-coupling analogy of the roadmap's note gains no support from this
  point's tensor.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems and the probe decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- Act 35's frozen head, verbatim: act 34's tables and objects, then `Γ`, `N`, `gram`, `fl`, `dita`,
  `ditaT`, `Δc`, `Δr` and `F4`.
- This round's objects, `let`-bound after it: Diţă's construction `dg X Y D` over any index types
  `α`, `β`, with `X : Matrix α α ℂ`, `Y : α → Matrix β β ℂ`, `D : α → β → ℂ`, and its row form
  `dgT`; flatness `flg X` of a unitary on a finite type with every entry of squared modulus one over
  the cardinality; the frozen index maps `r28`, `c28` of the product carrier onto `Fin 2 × Fin 8`
  — a row `(a, b)` to `(a div 2, 4·(a mod 2) + b)`, a column `(c, d)` to `(c mod 2, 4·(c div 2) + d)`
  — and `r82`, `c82` onto `Fin 8 × Fin 2` — a row `(a, b)` to `(2·a + b div 2, b mod 2)`, a column
  `(c, d)` to `(2·c + d div 2, d mod 2)` — with the instances `dita28`, `dita82` of the construction
  read back onto the product carrier through them; the parameters `z`, `w`; the stratum point
  `SIG = F4 z ⊗ F4 w`; the exponent matrix `Wt`, equal to `[b = 1] + [d = 1]` on the entries with
  `a` and `c` even and to zero elsewhere; the family `Pu u = SIG ∘ u^{Wt}`; the unit
  `u₆₀ = 3599/3601 + (120/3601)·i = (60+i)/(60−i)`; and the named point `P = Pu u₆₀`.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/DitaHierarchy.lean` opens with exactly
`import OIBridge.DitaHull`, its docstring, `namespace OIBridge`, `namespace DitaHierarchy`, and
the one `open`:

```lean
open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull

```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement. Every statement's
head is act 35's frozen head followed by this round's objects, and `controls.py` checks the head
against act 35's text byte for byte.

### `P_R` — the package

The conjunction, over one head, of `HULLG`, `HULLGT`, `LINE` and `POINT`:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)))
  ∧ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)))
  ∧ (∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N)
  ∧ (star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256)
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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ¬ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm)))
  ∨ ¬ (∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm)))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N)
  ∨ ¬ (star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256)
```

`P_N` is `P_R`'s negation pushed through the outer conjunction. `controls.py` rebuilds both from the
shared components and rejects any drift.

### `A36-1` — the construction over any factorization is realizable, required under `A36-HIERARCHY`

`HULLG`, `a36_shared_hull_g` — for any finite index types `α`, `β`, any bijections `eR`, `eC` of
`α × β` with the product carrier, any flat unitary `X` on `α`, flat unitaries `Y c` on `β` and unit
twists `D`, the column construction read back onto the product carrier is unitary, has every entry
of modulus `1/4`, and its tuple is realizable at the product configuration:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dg X Y D).submatrix eR.symm eC.symm))
```

`HULLGT`, `a36_shared_hull_gt` — the row construction likewise:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c d, ‖E c d‖ = 1) →
    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram ((dgT X Y E).submatrix eR.symm eC.symm))
```

### `A36-1` instances — the `2 × 8` and `8 × 2` column instances, required under both decided labels

`HULL28`, `a36_control_hull28` — the column construction with a `2 × 2` outer factor, two `8 × 8`
inner factors and a `2 × 8` twist, read back through `r28`, `c28`:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita28 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita28 X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita28 X Y D))
```

`HULL82`, `a36_control_hull82` — with an `8 × 8` outer factor, eight `2 × 2` inner factors and an
`8 × 2` twist, read back through `r82`, `c82`:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →
    dita82 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita82 X Y D i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (dita82 X Y D))
```

### `A36-2` — the family through the stratum point lies in the `2 × 8` hull, required under `A36-HIERARCHY`

`LINE`, `a36_shared_line` — for every unit `u`, `Pu u` is a `2 × 8` column Diţă matrix at the frozen
index maps with flat unitary factors and unit twists, its tuple is realizable, and its feature
vector lies in the product normalized set:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  ∀ u : ℂ, star u * u = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N
```

### `A36-3` — the named point is off the stratum, required under `A36-HIERARCHY`

`POINT`, `a36_shared_point` — `u₆₀` is a unit; `P` is realizable and in the product normalized
set; its feature vector is off the stratum; and its same-row-block, same-column-in-block cross
ratio at `(a, b, b', c, c', d) = (0, 0, 1, 0, 1, 0)` is `u₆₀ / 256`:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  star u₆₀ * u₆₀ = 1 ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S
  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256
```

### The control, required under both decided labels

`ONE`, `a36_control_stratum` — the family at `u = 1` is the stratum point, which lies on the
stratum:

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
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  Pu 1 = SIG ∧ featureVec (gram SIG) ∈ S
```

### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A36-HIERARCHY` | `a36_hierarchy` | `P_R` |
| `A36-NOT-HIERARCHY` | `a36_not_hierarchy` | `P_N` |
| corollary, required in every case | `a36_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A36-1`, required under `A36-HIERARCHY` | `a36_shared_hull_g` | `HULLG` |
| `A36-1`, required under `A36-HIERARCHY` | `a36_shared_hull_gt` | `HULLGT` |
| `A36-1` instance, required under both decided labels | `a36_control_hull28` | `HULL28` |
| `A36-1` instance, required under both decided labels | `a36_control_hull82` | `HULL82` |
| `A36-2`, required under `A36-HIERARCHY` | `a36_shared_line` | `LINE` |
| `A36-3`, required under `A36-HIERARCHY` | `a36_shared_point` | `POINT` |
| control, required under both decided labels | `a36_control_stratum` | `ONE` |

A module with neither verdict theorem reports `A36-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a36_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The elaboration file is `verification/lean-mathlib/OIBridge/DitaHierarchy.lean` on those branches.
Under the frozen header it carries `#check` commands and nothing else; the branches also carry a
disposable census family for the module and, on the probe's design head, the frozen probe wired
into the workflow, none of which is part of the freeze except the probe and its wiring.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36330185755 | `8fb7e1ed82d48c8bbc1de7622095058e4987016a` | **the nine frozen propositions and the corollary of this file** as ten `#check` commands under the frozen header, wired directly after `DitaHull`, with a disposable census family; the flatness predicate `flg` written with an anonymous binder | the `Mathlib bridge` build is red with one error, `Unknown identifier α` at the `flg` lambda, whose implicit type argument is inaccessible to an anonymous binder; the kernel check is green |
| 36330499550 | `ae1e671754c75583ff6c3b00e849bb055ce5d628` | the same head with `flg` written with the explicit binders `{α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ)`, the text frozen in this file | all three jobs green: all ten `#check`s elaborate and no error is reported; the release gate passes all 21 steps with eleven receipts holding; the kernel check is green; the probes job runs `D`'s list and is green |
| 36331117696 | `0a5c2f52119e6a1ad64dbb22cebcffadc842ac8c` | **the countercontrol**: the previous head with one deliberate defect, an extra argument to `dg` in `P_R`'s `HULLG` conjunct | red, as required. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/DitaHierarchy.lean:69:14: Application type mismatch`, at that argument, and nothing else fails in the build; the kernel check is green; the probes job runs `D`'s list and is green |
| 36331629574 | `3641125e17fb0b439c02d6a60a991158fc70ee9f` | the elaboration head with a first draft of the probe, blob `c95dbde5019b8f5942e22d033054ee8f5e8769db`, wired into the `Numerical probes` job by the one token: sections 1 to 6 as frozen below, without the `u = 1` identity control and the second point of the line, and with the sector certificate tested at one structured integer combination per sector | the `Mathlib bridge` build and the kernel check are green; the probes job is red at exactly one check, the sector fates: the certificate **fails** at the structured combination of each 8-dimensional sector, `(8, False, False, None)` against the expected `(8, False, True, None)`, while every other check of the six sections passes, 44 `PASS` and 1 `FAIL`. The failure is the direction dependence of Hazard 6, not a change in the mathematics: at random directions the certificate holds, at structured ones it fails |
| 36331881958 | `2f9707a16757f110b7244fe4b48cd96593f69b44` | the same with the `u = 1` identity control and the second point `Pu u₅` added, blob `8bae58ccb008249c9e2844167de2a56a06ee2e6b` | the `Mathlib bridge` build and the kernel check are green; the probes job is red at exactly the same check and for the same reason, the sector fates at the structured combination, `(8, False, False, None)` twice, with every other check passing, 55 `PASS` and 1 `FAIL`: the `u = 1` identity, the second point `Pu u₅` with its defect 37 and its six searches with the frozen `2 × 8` structure all pass |
| 36333554801 | `350030824c21456dfb680c5ee8d64121530b48b1` | the elaboration head with the **frozen probe** (blob as frozen below): the second draft with the sector certificate tested at three seeded pseudo-random directions per sector and its direction dependence asserted at the basis vectors | all three jobs green; the probe reports 57 `PASS` and no `FAIL` and ends with its `OK` line — the design run of the probe as frozen |

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_hierarchy_probe.py`, blob **`b3d144988a9678deac69a738b6459f32230371b0`**, is written before `F` and
added by the execution at stage 1 with exactly this blob, and `.github/workflows/verify.yml` at `E`
is `D`'s with the token `dita_hierarchy` appended to the list the `Numerical probes` job runs, so
that the job runs it at every execution commit from stage 1 on, and so at `E`. `F` carries this
file alone and no probe; the runs at `F` exercise the probes job at `D`'s list. The probe's design
run before `F` is recorded in the runs table above. It uses Python integers, fractions and
Gaussian rationals for every value it asserts, `numpy` only inside the floating-point eigenvalue
step that proposes the integer eigenvalues of the class sums, each of which is then verified by an
exact nullspace, Python's `random` at the fixed seed 363 for the generic directions of section 6,
and it exits 1 on any mismatch with the values frozen here. Its statements are
exact arithmetic replayed; they are not kernel-certified, and the result note names them as this
layer's.

**1. The certified point, the named point and the exact line.** `SIG` is unitary; `u₆₀` is a unit;
`P = SIG ∘ u₆₀^W` is unitary; `rank DF = 176` and the defect of `SIG` is **49**; the defect of `P` is
**37**; `W` is an exact straight line at `SIG` — every level-set sum of the `c_k` over
`k ↦ W_ik − W_jk` vanishes, all 120 pairs — and a one-entry perturbation of `W` is not (control);
`W` lies in `ker DF`; the family at `u = 1` is `SIG` entrywise (control); `u₅ = (3+4i)/5` is a unit and
the second frozen point `Pu u₅` is unitary, with defect **37**; the cross-ratio identity of act 35 is
violated by `P` at **384** ordered sites
`(a, b, b', c, c', d)` with `b ≠ b'`, `c ≠ c'`; and the value at `(0, 0, 1, 0, 1, 0)` is `u₆₀` in the
probe's unimodular scaling, `u₆₀ / 256` in the frozen normalization.

**2. Diţă factorizations by exhaustive search over block structures** (Hazard 4), as
`(candidates, exact factorizations)`, at the named point `P`, at the second point `Pu u₅` of the
frozen line, and at the stratum point `SIG = Pu 1`, where the same search must find the known
factorizations:

| shape | form | at `P` | at `Pu u₅` | at `SIG = Pu 1` (control) |
| --- | --- | --- | --- | --- |
| `4 × 4` | column | (1, 0) | (1, 0) | (5, 4) |
| `4 × 4` | row | (1, 0) | (1, 0) | (5, 4) |
| `8 × 2` | column | (1, 0) | (1, 0) | (3, 2) |
| `8 × 2` | row | (1, 0) | (1, 0) | (3, 2) |
| `2 × 8` | column | (1, 1) | (1, 1) | (3, 3) |
| `2 × 8` | row | (1, 1) | (1, 1) | (3, 3) |

The one `2 × 8` factorization of `P`, and of `Pu u₅`, in each form has the column blocks
`(0, 1, 2, 3, 8, 9, 10, 11)`, `(4, 5, 6, 7, 12, 13, 14, 15)` and the row classes
`(0, 8), (1, 9), …, (7, 15)`, the blocks by the parity of `c` and the classes by `(a mod 2, b)`,
which is the structure the frozen index maps `r28`, `c28` read.

**3. The first-order census at `SIG`**, exact: `dim ker DF = 80`; gauge rank 31; `T_c`, `T_r` and
`T_c + T_r` of dimensions 14, 14, 26 modulo the gauge; `R = ker DF / (gauge + T)` of dimension
**23**; `coker DF` of dimension **64**.

**4. Every `4 × 4` Diţă hull through `SIG`**: the exact factorizations of the block-structure search
in both forms, each factor replaced by every Fourier circle through it modulo the gauge and the
sign, give **492** hulls; every hull tangent lies in `ker DF` and `D²F` vanishes exactly on every
hull (0 failures); every hull tangent has dimension 14 modulo the gauge; and the span of all of
them modulo the gauge is **49**, the defect.

**5. The stabilizer of `SIG` in `G_ext` and the residual sectors**: the factor stabilizer products
are 256 for each of the four operations without factor exchange and 0 with it; the order is
**1024**; the conjugacy classes number **112**; the exact coordinate solver reconstructs a
transported basis vector (control); `gauge + T` is stabilizer-invariant; and the isotypic sectors of
`R`, exact common eigenspaces of the class sums, have dimensions **8, 8, 4, 2, 1** and are invariant
under every class sum.

**6. The second-order form and the obstruction census**: `B(gauge, ker DF) = 0` in the cokernel;
`D²F` vanishes exactly on `Sym²(T_c)` and on `Sym²(T_r)`; the rank of `B` on `Sym²(Def)` is **47**;
and the sector fates `(dim, isotropic, at three seeded pseudo-random directions: (obstructed by
certificate, extended by an explicit row-hull correction))` are `(8, no, [(yes, –)] × 3)`,
`(8, no, [(yes, –)] × 3)`, `(4, yes, [(no, yes)] × 3)`, `(2, yes, [(no, yes)] × 3)`,
`(1, yes, [(no, yes)] × 3)`, with the seed 363 and integer weights in `[−3, 3]`; and the certificate
fails at every one of the eight structured basis vectors of each 8-dimensional sector, **8 of 8**
and **8 of 8** (Hazard 6).

The probe reports 57 `PASS` and no `FAIL`, runs in about 13 to 28 minutes, and ends
with the line `dita_hierarchy_probe: OK …` on success, which the result note carries verbatim, and
`dita_hierarchy_probe: FAILED …` with the failing checks otherwise.

***

## The question, FROZEN — one target

### `A36` — the Diţă factorization hierarchy at the stratum

**At act 29's product configuration, is Diţă's construction over any factorization of the
sixteen-point carrier, in the column and the row form, realizable for every choice of flat unitary
factors, unit twist phases and row and column bijections; does the family `SIG ∘ u^W` through the
certified rational stratum point lie, at every unit `u`, in the `2 × 8` column Diţă hull at the
frozen index maps, realizable in the product normalized set; and is its named point at
`u₆₀ = (60+i)/(60−i)` realizable, in the product normalized set and off the stratum, with the
frozen cross-ratio value — while, under every decided label, the `2 × 8` and `8 × 2` instances are
realizable and the family at `u = 1` is the stratum point on the stratum?**

The answer is reported as one of three labels:
- `A36-HIERARCHY`, the theorem `P_R`;
- `A36-NOT-HIERARCHY`, the theorem `P_N`;
- `A36-UNDECIDED`.

Beside the label, the exact-computation layer's statement stands or falls with the probe: green,
it establishes that `P` admits no `4 × 4` Diţă factorization of either orientation at any block
structure, so that the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum
point; red at `E`, the round halts.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the instances | `a36_control_hull28`, `a36_control_hull82` | the general construction at the two shapes the probe searches, required whichever label is earned |
| the stratum is reached | `a36_control_stratum` | the family at `u = 1` is the stratum point, so the twist is what leaves the stratum |
| the point is off the stratum | `a36_shared_point` | the cross-ratio value `u₆₀ / 256 ≠ 1 / 256` against act 35's identity on the stratum |
| the `4 × 4` insufficiency | the probe's `(1, 0)` counts at `P` | no `4 × 4` factorization of either orientation at any block structure |
| the search is not vacuous | the probe's counts at `SIG = Pu 1` | the same search finds the known factorizations of the stratum point, the family's point at `u = 1`: `(5, 4)`, `(3, 2)`, `(3, 3)` |
| the certificate is not specific to `u₆₀` | the probe's counts at `Pu u₅`, `u₅ = (3+4i)/5` | a second point of the frozen line, of defect 37, with the same counts and the same `2 × 8` structure |
| the line is exact | the probe's straight-line check and its one-entry control | `W` is a straight line and a perturbation of it is not |
| the first-order account | the probe's 492 hulls and span 49 | the `4 × 4` hulls through `SIG` span the defect at first order |
| the probe's own controls | the coordinate-solver check, the invariance checks, the `B(gauge, ·) = 0` check | the exact linear algebra behaves as stated |
| the certificate is not vacuous in either direction | the isotropic sectors' `no`, and the 8 of 8 basis-vector failures | the same code returns `no` where an extension exists and where the direction is structured, and `yes` at the seeded generic directions of the 8-dimensional sectors |
| duality | `a36_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`HULLG`, `HULLGT`.** Unitarity of `dg X Y D` on `α × β` by `Matrix.mem_unitaryGroup_iff` and
   the row sums: for rows `(a,b)`, `(a',b')` the sum over `(c,d)` splits through
   `Fintype.sum_prod_type` into `Σ_c X[a,c]·conj X[a',c]·D[c,b]·conj D[c,b']·Σ_d Y_c[b,d]·conj Y_c[b',d]`;
   the inner sum is `δ_{bb'}` by the unitarity of `Y_c`, then `|D[c,b]|² = 1` and the outer sum is
   `δ_{aa'}` by the unitarity of `X` — act 35's `a35_shared_dita_unitary` at general types. The
   submatrix by the bijections `eR.symm`, `eC.symm` is unitary by `Matrix.submatrix_mul_equiv` and
   `Fintype.sum_equiv`. Every entry has squared modulus `1/card α · 1 · 1/card β = 1/16`, since
   `card (α × β) = 16` from the bijection, so modulus `1/4`. Realizability by act 35's
   `a35_shared_gram_realizable` applied to the read-back matrix. `HULLGT` by the same computation
   on the row form, or from `HULLG` through act 25's `transpose_unitary`.
2. **`HULL28`, `HULL82`.** Instances of `HULLG`: `r28` and `c28` are bijections
   `Fin 4 × Fin 4 ≃ Fin 2 × Fin 8`, inverse to `(h, k) ↦ (2·h + k div 4, k mod 4)` for rows and
   `(l, k) ↦ (2·(k div 4) + l, k mod 4)` for columns; likewise `r82`, `c82`; the instance is
   `HULLG` at those equivalences with `dita28 X Y D = (dg X Y D).submatrix eR.symm eC.symm`
   entrywise.
3. **`LINE`.** The nested form: with `a = 2·a_hi + a_lo`, `c = 2·c_hi + c_lo`,
   `F4 z [a, c] = ½·(−1)^{a_hi·c_lo + a_lo·c_hi}·z^{a_lo·c_lo}`, so
   `Pu u [(a,b),(c,d)] = ½·(−1)^{a_hi·c_lo} · ½·(−1)^{a_lo·c_hi}·z^{a_lo·c_lo}·F4' w [b, d] · u^{[a_lo = 0][c_lo = 0]([b = 1] + [d = 1])}`,
   `F4'` the unscaled Fourier matrix. The witnesses: the outer factor
   `X = ((1 + i)/2) · [[1, 1], [1, −1]]`, a flat unitary on `Fin 2` with Gaussian-rational entries;
   the inner factors `Y_{c_lo}` on `Fin 8`, indexed by `(a_lo, b)` for rows and `(c_hi, d)` for
   columns, `Y_0 [(a_lo,b),(c_hi,d)] = ((1 + i)/4) · (−1)^{a_lo·c_hi} · F4' w [b, d] · u^{[a_lo = 0]([b = 1] + [d = 1])}`
   and `Y_1 [(a_lo,b),(c_hi,d)] = ((1 + i)/4) · (−1)^{a_lo·c_hi} · z^{a_lo} · F4' w [b, d]`, flat
   unitaries on `Fin 8` for every unit `u` — each is a `2 × 4` row-Diţă form of `F4' w` with the
   sign matrix `[[1, 1], [1, −1]]` outside and the twists `u^{[b = 1] + [d = 1]}`, `z^{a_lo}`
   inside, so its unitarity is the same block computation, with `star u * u = 1` and
   `star z * z = 1` closing the cross terms; and the constant twist `D c b = −i`, so that
   `X · D · Y` carries the scalar `((1 + i)/2)·(−i)·((1 + i)/4) = 1/4`. The identity
   `Pu u = dita28 X Y D` is entrywise by `ext` over the 256 index pairs and `ring` in `z`, `w`, `u`
   and `Complex.I`. Realizability and membership in `N` by `HULL28` and the definition of `N`.
4. **`POINT`.** `star u₆₀ * u₆₀ = 1` by `Complex.ext_iff` and `norm_num`
   (`3599² + 120² = 3601²`). Realizability and membership by `LINE` at `u₆₀`. Non-membership in `S`
   from act 35's `a35_shared_cross`: on every stratum point the cross-ratio product at
   `(0, 0, 1, 0, 1, 0)` equals `1/256`, while on `P` it equals `u₆₀/256 ≠ 1/256` because `u₆₀ ≠ 1`.
   The value by evaluation: the four entries of `P` involved, at `((0,0),(0,0))`, `((0,0),(1,0))`,
   `((0,1),(1,0))` and `((0,1),(0,0))`, each lie in the first row of `F4 z` or of `F4 w` and so
   equal `1/4` times a power of `u₆₀`; the only nonzero exponent among the four is
   `Wt (0,1) (0,0) = 1`, so the product of the two `gram` factors is `(1/4)⁴ · u₆₀ = u₆₀ / 256`, by
   `simp` and `ring`.
5. **`ONE`.** `Pu 1 = SIG` by `ext` and `one_pow`; `featureVec (gram SIG) ∈ S` as act 35's
   `a35_shared_untw_core` did for `F₄(i) ⊗ F₄(i)`: `F4 z` and `F4 w` are flat unitaries by
   `a35_shared_f4_flat`, their tuples are realizable by act 23's `hadamard_z_admissible` with act
   12's `sh1_necessity`, and `gram SIG` is the product tuple of the two entrywise.
6. **`a36_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

No route to `A36-NOT-HIERARCHY` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a36_shared_…` and every `a36_c_…` other than `a36_c_exclusive` | either verdict theorem; `a36_c_exclusive` |
| every `a36_control_…` | either verdict theorem; `a36_c_exclusive` |
| `a36_not_hierarchy` | `a36_shared_hull_g`, `a36_shared_hull_gt`, `a36_shared_line`, `a36_shared_point` |
| `a36_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A36` | `A36-HIERARCHY` | **very high** | the general construction's unitarity is act 35's block computation at general types; the instances are its specializations; the family's nested form was verified entrywise in exact arithmetic before the freeze and its factors are explicit flat unitaries; the point's cross-ratio value was computed exactly; every frozen statement elaborates |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A36-HIERARCHY`

> At the frozen product configuration, the Diţă-hierarchy package holds, at evidence level 2: Diţă's construction over any factorization of the sixteen-point carrier — an outer flat unitary factor on the first index set, inner flat unitary factors on the second, unit twist phases, and any bijections of the product with the carrier for rows and for columns — is unitary, flat and realizable, in the column form and in the row form, with the `2 × 8` and `8 × 2` column instances at the frozen index maps stated concretely; through the certified rational stratum point runs an exact one-parameter family `SIG ∘ u^W`, `W` the frozen exponent matrix, whose every member at a unit `u` is a `2 × 8` column Diţă matrix at the frozen index maps and is realizable in the product normalized set; and the named point `P = SIG ∘ u₆₀^W` at `u₆₀ = (60+i)/(60−i)` is realizable, lies in the product normalized set and off the product-embedded stratum, its same-row-block, same-column-in-block cross ratio at `(0,0,1,0,1,0)` being `u₆₀/256` and not `1/256`. Beside the package, required under both decided labels: the `2 × 8` and `8 × 2` instances are realizable, and the family at `u = 1` is the stratum point itself, which lies on the stratum. By the round's exact-computation probe, and not by the kernel: the named point has defect 37; it admits no `4 × 4` Diţă factorization of either orientation at any block structure and no `8 × 2` factorization of either orientation, and admits exactly one `2 × 8` factorization of each orientation, the frozen one; so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the `2 × 8` construction. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law, it does not classify the product normalized set, and it does not decide whether every realizable class near the stratum lies in some Diţă hull of some factorization: the exhaustion of the hierarchy is open.

### `A36-NOT-HIERARCHY`

> At the frozen product configuration, the Diţă-hierarchy package fails, at evidence level 2: the realizability of the general construction in one of its two forms, the membership of the family in the `2 × 8` hull with its realizability, or the position of the named point off the stratum with its realizability is false, and the witness is exhibited in the kernel; the `2 × 8` and `8 × 2` instances and the stratum control hold. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.

### `A36-UNDECIDED`

> Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it.

### The corollary, REQUIRED

`a36_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, and the probe's
summary line `dita_hierarchy_probe: OK …` from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `A36-HIERARCHY` |
| 2 | `A36-NOT-HIERARCHY` |
| 3 | `A36-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 35's sentence and its standing
clause:

> At the product configuration, two explicit families of realizable classes, the column and row Diţă hulls, contain the product-embedded stratum, are realizable for every choice of flat unitary factors and unit twist phases, and carry infinitely many classes through every stratum point that no finite set of maps identifies; act 34's properness witness is a column relabelling of a stratum point, so stratum membership is not an invariant of the isometry classes of the product normalized set; and, by the round's exact-computation probe, at the certified rational stratum point the defect, the dimension of the solution space of the linearized unitarity constraints modulo phases and an upper bound on the dimension of any family of realizable classes through the point, is 49, while the tangent span of the two fixed-pairing hulls has rank 26, so those two tangent spaces do not exhaust the defect space; whether the relabelled hulls exhaust the realizable classes near the stratum is an open modulus, recorded and not decided. Nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, isometry or family is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A36-HIERARCHY`:**

  > At the product configuration, Diţă's construction over every factorization of the sixteen-point carrier, in the column and the row form, is realizable for every choice of flat unitary factors, unit twist phases and row and column bijections; an exact one-parameter family of `2 × 8` column Diţă matrices runs through the certified rational stratum point, every member realizable, and its named point at `u₆₀ = (60+i)/(60−i)` is a realizable class off the stratum; and, by the round's exact-computation probe, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy; whether every realizable class near the stratum lies in some Diţă hull of some factorization is open, recorded and not decided. Nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

- **`A36-NOT-HIERARCHY`:**

  > At the product configuration, the Diţă-hierarchy package fails at a named part, by a witness exhibited in the kernel, while the `2 × 8` and `8 × 2` instances and the stratum control hold. Nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On `A36-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `a02be0964a982abe2b9fd5082e2844927d3ab690` (`A36-HIERARCHY`);
- `f7dc269279238136101df197df7f57d0cc3a9c51` (`A36-NOT-HIERARCHY`).

The guard run locally at `D` against each rehearsed cell reports 91 PASS and 0 FAIL, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 35's `A35-DITA-STRATIFIED`, act 34's `A34-STRATIFIED`, act 33's
  `A33-CLASSIFIED`, act 32's `A32-NOT-RIGID` or any verdict of acts 28 to 31.** Those are the
  verdicts those rounds recorded, and they stand; act 35's open modulus is answered here for the
  `4 × 4` hulls by a fact about a named point, and re-posed for the hierarchy.
- **No outcome decides whether the hierarchy exhausts the realizable classes near the stratum.**
  Whether every realizable class near the stratum lies in some Diţă hull of some factorization is
  recorded open.
- **No outcome says anything about Diţă's construction beyond the frozen statements**: not that
  it is insufficient, not that it is sufficient, and never "Diţă geometry is insufficient"; what is
  established is that the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum
  point, by the probe.
- **No outcome classifies the classes of the product normalized set or its isometries.**
- **No outcome reports anything about transition families or dynamics.** Nothing here establishes
  that any admissible law is covariant under any isometry or reaches any class, and none closes
  `P0`, which stays `OPEN`.
- **No hull, family, factorization, isometry, group or covariance is called canonical, physical or
  fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard, or the roadmap's section on the residual deformation space;
- write any manuscript file;
- change the workflow beyond the one token that wires the probe;
- import any Mathlib module into the frozen module beyond what `DitaHull` imports.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; act 35's tables and
this round's objects `dg`, `dgT`, `flg`, `r28`, `c28`, `dita28`, `r82`, `c82`, `dita82`, `z`, `w`,
`SIG`, `Wt`, `Pu`, `u₆₀` and `P` are `let`-bound inside each statement that uses them.

## Evidence level

**2** for the module — Lean theorems, kernel-checked, every named result printing its axioms, each
within `propext`, `Classical.choice` and `Quot.sound`. The probe's statements are exact arithmetic
replayed in CI, a separate layer named as such wherever they are cited.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-36-dita-hierarchy/controls.py`, blob
**`292faff95a9e082b4fae8fb193db34ef7745d665`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction, over the frozen head, of the four package texts, and
    `P_N` the disjunction of their negations, rebuilt from the shared components.
  - Every other statement carries the one head verbatim; the head is act 35's frozen head, byte
    for byte, followed by this round's objects.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a36_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a36_c_exclusive`;
  - carries the statements the earned label requires.
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires;
  - the probe's summary line.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen sentence for the case appended, or to
  `D`'s.
- **The guard** is byte-identical to `D`'s.
- **The probe** has its frozen blob, and **the workflow** is `D`'s with the one token inserted.
- **The census** is `D`'s with exactly one family appended, last, for `DitaHierarchy`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.DitaHierarchy` inserted directly after
  `import OIBridge.DitaHull`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files, the module and the probe;
  - modified: `OIBridge.lean`, the census and the workflow;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with 8 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies 62 mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 8 duality mutations fail as required
controls: 3 rows hold as frozen, 62 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module, the controls and the probe.**
   - `controls.py` with its frozen blob.
   - The probe with its frozen blob, and the workflow token that wires it.
   - The module with the frozen header and its shared lemmas. On the route to
     `A36-HIERARCHY` these include `A36-1` with its instances, `A36-2`, `A36-3` and the control.
   - The import line.

   No verdict theorem and no corollary `a36_c_exclusive`.
2. **Stage 2 — the verdict.** `a36_hierarchy` or `a36_not_hierarchy`, or neither, and
   `a36_c_exclusive`.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last. On a decided
   outcome only, the `P0` sentence for the case.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from
   the run at `E`'s predecessor and is confirmed by the run at `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build
fails is followed by a fixing commit, never rewritten. The label is read from the module at `E`.
Proofs may be developed first on a disposable branch from `F`, never landed; such runs are design
evidence and the result note names them.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one and runs green | `C3`: the probe's blob at stage 1 and at `E`; the `Numerical probes` job green at every execution commit and at `E` with the probe's `OK` line in its log |
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
- **A verdict that cannot be obtained** is reported `A36-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A36-UNDECIDED` with the missing statement named. A verdict prints only over green controls,
  the probe among them.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is any of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken —
    in particular `HULL28`, `HULL82` or `ONE` false as frozen, which no label absorbs;
  - the probe red at `E` with the frozen blob.

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
