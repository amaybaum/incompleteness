# Track B act 41 — partition structures, index maps and factorization classes: the Diţă censuses of acts 36 to 40 under every index map: PREREGISTRATION

**Status: control plane of a native round, local draft; no-theorem exact-computation correction
round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 41 computes statements about the Diţă structures of act 34's certified rational stratum point and of the
> exact families through it that acts 36 to 40 studied, and adopts none of them as anything but mathematics. It
> fixes four terms — partition structure, alignment, index map and factorization class — and measures, under the
> reading acts 36 to 40 froze, in which an index map is a full pair of bijections of the product with the carrier,
> the counts, loci and hulls those acts measured at one alignment per partition structure. It revises no recorded
> verdict and edits no record: every theorem of acts 36 to 40 stands, and their records stand as recorded. It adds
> and changes no mathematical declaration; every statement it makes is exact arithmetic replayed in CI, and the
> current surfaces it corrects are generated from its measurements. No outcome censuses the exponent matrices with
> entries in `{0, 1}`, decides the minimality of any support, or classifies any family other than those of acts 36
> to 40. No hull, family, factorization, isometry, carrier, group or principle gains physical status by appearing
> here, and nothing here derives, recognises or approaches quantum evolution.

## The declarations

```v3-round
round A41
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-41-index-map-semantics/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-41-index-map-semantics/
record AM verification/receipts/A41.json
execution A verification/lean/dita_index_map_probe.py
execution A verification/lean/dita_index_map_independent.py
execution A verification/lean/dita_index_map_hulls.py
execution M .github/workflows/verify.yml
execution M verification/lean/dita_hierarchy_probe.py
execution M verification/lean/dita_arc_exclusivity_probe.py
execution M verification/lean/dita_local_escape_probe.py
execution M verification/lean/dita_torus_probe.py
execution M verification/lean/dita_torus_locus_probe.py
execution M verification/lean-mathlib/OIBridge/DitaHierarchy.lean
execution M verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean
execution M verification/lean-mathlib/OIBridge/DitaLocalEscape.lean
execution M verification/lean-mathlib/OIBridge/DitaTorusLocus.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds four files: this preregistration, the round's frozen controls
`controls.py`, the measurement file `measurements.json`, and the result note. The receipt path is
`verification/receipts/A41.json`. Every other path the round changes is an execution path listed
above, and changes only as frozen below. The guard, `verification/lean/edge_rigidity_probe.py`, is
not governed and is not changed: at `E` it is byte for byte `D`'s.

**No mathematical declaration is added or changed.** The four Lean paths are governed for their
module docstrings alone: at `E` each module is `D`'s outside the leading `/-! … -/` block, byte for
byte, so the `lean-axioms` count at `E` is `D`'s, 5251. The five earlier probes are governed for
their check labels, section titles, docstrings and success text alone: at `E` each parses to the
same syntax tree as `D`'s except at the string constants listed in the frozen edit ledger, so each
performs the same computation and asserts the same values.

## The objects

- **`D`** = `78ea3c39004e97aad027ee6153051c6d372bdd55`: the head of `main` after act 40's landing,
  `A40-LOCUS-CLASSIFIED`, receipt `verification/receipts/A40.json`; its parents are act 40's base
  `b271b1df` and act 40's receipt commit `d31306d6`. It is certified by push run 36483043836: all
  nine jobs green, the release gate passing all 21 steps with sixteen receipts holding and the 303
  legacy records intact, `lean-axioms` at 5251 named results and no sorry, and the guard
  `ALL CHECKS PASS`. Every measurement here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A41.json`.

No other governed round runs beside A41 at this freeze. Should one land first, its movement of
`main` enters A41 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — five counts, never interchanged.** Every count this round states is one of five
different quantities, and each is named as what it is wherever it is stated (the definitions are
frozen below):

- a **partition-structure count** — orientation, shape, column blocks and row classes;
- an **alignment count** — the valid alignments of a partition structure: which row of each row class
  carries each label;
- a **realizing-index-map count** — pairs `(eR, eC)` of bijections, act 36's datum;
- a **factorization-class count** — orbits of realizing triples (orientation, partition structure,
  alignment) under a group whose action is frozen (Definition 6), always named with the count;
- a **partition-orbit count** — orbits of admitted partition structures under the same group, always
  named with the count.

At `SIG` the last two differ by a factor of seven, so the word "class" is never used bare: it occurs only
in the fixed compounds *row class*, *factorization class* and *realizable class*, and "structure" alone is
never used for a count. A hull count (Definition 7) is a sixth quantity and is never read off any of the
five. Act 37's "nine classes" are named, wherever they are cited, as **the nine partition orbits of its
sorted-alignment restriction** — not as an earlier value of either count above.

**Hazard 2 — a correction of readings, not a reopening.** Act 36's kernel quantifies over arbitrary
bijections `eR eC : α × β ≃ Fin 4 × Fin 4`, and its frozen sentence says "any bijections of the
product with the carrier for rows and for columns". Acts 37 to 40 say "no other index maps at all",
"no index maps whatever" and "any shape, index map or orientation", and none of them redefines the
term. Their exhaustive searches fixed one alignment per partition structure — the sorted one —
without their frozen texts saying so: an implementation restriction, not part of the frozen
mathematics. This round measures each affected count, locus and hull as the frozen quantifier
reads. The kernel theorems of acts 36 to 40 concern named index maps and stand; the verdict labels
stand; the records stand as recorded and are not edited.

**Hazard 3 — one layer.** Every statement of this round is exact arithmetic replayed in CI. It is
not kernel-certified, and nothing in the result note or the surfaces says it is. Where a measured
statement asserts a factorization the kernels of acts 36 to 40 do not prove, the probe exhibits it
by exact reconstruction, and the statement names that layer.

**Hazard 4 — the verdict is generated from measurements.** The values measured before this freeze
are recorded as the freeze's reading and are **not** pass conditions (§A.29). What is frozen is what
is measured, how, by which two independent computations, and how their agreement is decided. The
result note and every corrected surface are generated from the values measured at `E` by frozen
templates; no value in them is typed by hand.

**Hazard 5 — strict and relaxed kept apart.** Every quantity is measured strictly and up to
diagonal equivalence (act 38's Hazard 5) and reported in both notions separately. Act 37's frozen
claim is strict; a relaxed measurement along its arc is stated as its own proposition and never
read into act 37's.

**Hazard 6 — the sorted enumeration is a control.** The sorted-alignment computation of acts 36 to
40 is rerun only to reproduce the values those rounds recorded, as a control of the implementation.
It is evidence for no statement of this round. The earlier probes keep their computations as
sorted-alignment regression controls; their labels and success text are corrected so that they no
longer present that restricted enumeration as exhaustive, and this round's probe carries the
all-alignment statements (§A.30: remove the assertion, keep the derivation).

**Hazard 7 — hulls are counted by a frozen equality.** Many realizing index maps parameterize the
same hull. A hull count is a count of hulls under Definition 7's equality, never a count of
parametrizations, and every property of a hull — tangent dimension, the linearized and second-order
unitarity conditions — is checked on every distinct hull, not carried over from act 36's.

**Hazard 8 — scope.** Excluded, as statements, as dependencies and as readings of the outcome: the
census of exponent matrices with entries in `{0, 1}`; the minimality of any support; any family other
than act 36's arc `SIG ∘ u^W`, act 38's arc `SIG ∘ u^E` and act 39's `H3`; the realizable classes of the product
normalized set and its isometries; and anything physical.

**Hazard 9 — history and the live registry.** Acts 36 to 40 recorded `A36-HIERARCHY`,
`A37-EXCLUSIVITY-PROVED`, `A38-NON-DITA-WITNESS-PROVED`, `A39-REALIZABLE-PROVED` and
`A40-LOCUS-CLASSIFIED`. All stand as recorded. The census registry is a live registry: its entries
for those acts keep their outcome labels and their account of what each round measured, and gain the
current count under the frozen reading, attributed to this round; nothing in them states that an
earlier round measured what it did not.

**Hazard 10 — vocabulary.** A partition structure is not an index map, an alignment is not a
relabelling of `SIG`, a factorization class is not a partition orbit, a hull is not a
parametrization, a stabilizer is not a symmetry of anything physical, and none is written as the
other. Act 37's "class — a pair of index maps" names what this round calls a realizing index map at the
sorted alignment, up to `R(m, n)`; act 37's "nine classes" are the nine partition orbits of its
sorted-alignment restriction under the full stabilizer (Definition 6, item iii).

***

## Provenance

Consumed as frozen objects, carried verbatim and never paraphrased:

- **act 40's probe**, blob `4b718e79f3800369855b6a9f0fc734ed2d59df4b`: its head — act 38's probe head,
  with act 36's exact Gaussian rationals, partition search and stabilizer, act 37's monomial calculus
  and act 38's pieces — its flat calculus and its partition-candidate enumeration;
- **act 36's probe**, blob `f19b757908ca1810df2b85de58c378819be621ef`: its points `P = SIG ∘ u₆₀^W`
  and `Pu(u₅)`, its gauge, `DF`, second-order form `Q`, circle directions and gauge reduction;
- **act 36's kernel**, `DitaHierarchy.lean`, blob `490a5db0f2141210fc0c08d49b44246d6ad949f8` — only
  as the text that fixes the meaning of an index map (Hazard 2), at line 143 and its instances at
  lines 160, 407, 454, 734, 736, 794, 796, 840 and 842, each `(eR eC : α × β ≃ Fin 4 × Fin 4)`.

## Locating controls — at `D`

| file at `D` | blob |
| --- | --- |
| `verification/lean/dita_hierarchy_probe.py` | `f19b757908ca1810df2b85de58c378819be621ef` |
| `verification/lean/dita_arc_exclusivity_probe.py` | `87bc3822ea255b42a56d25d206302e8603a40237` |
| `verification/lean/dita_local_escape_probe.py` | `00be96c384f63efaaa52995d38704428404b0497` |
| `verification/lean/dita_torus_probe.py` | `4405655907e1e508e0ce72b3335c905b0abcaf8d` |
| `verification/lean/dita_torus_locus_probe.py` | `4b718e79f3800369855b6a9f0fc734ed2d59df4b` |
| `verification/lean-mathlib/OIBridge/DitaHierarchy.lean` | `490a5db0f2141210fc0c08d49b44246d6ad949f8` |
| `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean` | `a967e8819e123517b92c142a3d28cc854e131333` |
| `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` | `07b15006f35d330e7f711e2353c070b187bb55a0` |
| `verification/lean-mathlib/OIBridge/DitaTorusLocus.lean` | `829146f6eff2b99aab54d7e5e9292b0ecfb33d8d` |
| `verification/lean-manuscript-census.json` | `f6810cb3bdbe4a35ccac3884a5b3e2a865c7422d` |
| `verification/ROADMAP.md` | `145251197bede7d2bbd0c5a2605c7827e1b042fa` |
| `.github/workflows/verify.yml` | `08586b8ecf334ba68e217e0e21af953e30466914` |
| `verification/lean/edge_rigidity_probe.py` | `d28e9b3cf2093984a1c453892204b9932a685b2e` |

The names this round introduces return nothing from `git grep -l` at `D`: `act-41`, `A41-`,
`dita_index_map` and `probes_a41`.

### The claim-surface census at `D`

Every non-record occurrence at `D` of a statement that depends on the sorted-alignment census, with
its kind and its disposition. Records — everything under `verification/programmes/`,
`verification/receipts/`, and the files `verification/infrastructure/legacy-records.json` lists — are
excluded and not edited.

The full census — 138 rows over nine files, each with its exact text at `D`, its kind and its proposed
replacement — is carried as the appendix of this file and is the source of the surface ledger. By kind:

| kind | rows | meaning |
| --- | --- | --- |
| absolute, false under the frozen reading | 10 | "the complete census", "the eight / nine other classes", "the eighteen structures", "exactly one `2 × 8` structure per orientation at `u = −1`" |
| absolute, true in content, certified by a one-alignment search | 8 | re-attributed to exact computation over every index map, this round's probe |
| sorted-only count or verdict presented without scope | 85 | re-scoped to "at the sorted alignment"; the computation kept as a regression control |
| surviving unchanged | 28 | proportionality-only statements, named-map statements, kernel statements |
| a round's frozen `P0` sentence, quoted in the `P0` cell | 7 | five re-scoped as above, two unchanged |

Nothing outside the five earlier probes, the five Diţă modules, the census registry, `ROADMAP.md` and the
workflow's job names carries act 36 to 40 content; `verification/README.md`, `tools/`, `papers/` and `book/`
carry none. One check value is correct only as a sorted value — act 40's "every nonempty locus is cut out by
coordinate characters" — and is re-scoped with its label. One component of a landed act 38 check is vacuous
(`any(… for x in [])`, constantly `False`, at `dita_local_escape_probe.py` line 541); see the owner's decision
recorded with the ledger.

***

## Why this round exists

The exhaustive Diţă searches of acts 36 to 40 enumerate column blocks and row classes and then test
the factorization conditions at one index map per partition structure: the rows of each row class taken
in sorted order, so that the row labelled `a` in one row class is matched with the row labelled `a` in
every other row class by sorting. A Diţă form fixes that matching, and other matchings of the same
partition structure can pass where the sorted one fails. Recomputations over every alignment, made
after act 40's landing, found this at the stratum point, at act 38's `u = −1`, in act 40's census of
loci and in act 36's hull count, while act 37's strict exclusivity, act 38's exceptional set and act
40's five-face union were reproduced. This round measures all of it under the frozen reading, with
two independent computations, and corrects the current surfaces from the measurement.

### Measurements at `D` — the freeze's reading, not pass conditions

Computed at `D` in exact arithmetic from the frozen probe objects, with the scripts kept off the
repository. The probe decides; none of these values is a condition of any label.

Two computations were run at `D`: the production path (act 40's candidate enumeration and flat calculus,
each candidate's conditions factorized by row class, loci as unions over alignments) and the independent path
(act 36's partition search on the numeric matrix, alignments counted by a pruned matching search with factor
unitarity). **They agree at every point both computed** — `SIG`, `Pu(−1)`, `P`, `Pu(u₅)` and `Hu(−1)` — in both
notions, and the production path's exceptional sets and loci are consistent with the independent path's counts
at the other points below; the comparison at all forty-two named test cases is the probe's section 9.

| where | notion | partition structures, per orientation by shape `4 × 4` / `8 × 2` / `2 × 8` | valid alignments | recorded at the sorted alignment |
| --- | --- | --- | --- | --- |
| `SIG` | strict and relaxed | 20: 5 / 2 / 3 | 976: `k1` 8, `k2` 64, `k3` 8, `k4` 8, `k5` 8; `e1`, `e2` 4 each; `t1`, `t2`, `t3` 128 each — per orientation | 18: 4 / 2 / 3 |
| `Pu(−1)` | strict | 2: 0 / 0 / 1, act 36's frozen partition | 256 | 2 |
| `Pu(−1)` | relaxed | 20, those of `SIG` | 976 | 2 (act 37's claim is strict) |
| `P`, `Pu(u₅)` | strict and relaxed | 2: 0 / 0 / 1, act 36's frozen partition | 256, all 128 per orientation | 2 |
| `Hu(−1)` | strict and relaxed | 4: 1 / 0 / 1 — `M_COL`, `M_ROW`, and a `4 × 4` partition that is `k4` moved by the row exchange `7 ↔ 15` and the column exchange `2 ↔ 8`, in each orientation | 272: 128 per `2 × 8`, 8 per `4 × 4` | 2 |
| act 38's twenty Gaussian-rational candidate points on `Hu` | strict and relaxed | 20 at `u = 1`, 4 at `u = −1`, none at the other eighteen | — | the same points |

- **Factorization classes at `SIG`** (Definition 6), both notions: 976 realizing triples, closed under the
  stabilizer; **70** factorization classes under the full stabilizer (orbit sizes from 2 to 64) and
  **140** under the transpose-free subgroup; **10** partition orbits under the full stabilizer, each a
  partition structure with its transpose, and **20** under the transpose-free subgroup. Act 37's "nine
  classes" are the nine partition orbits of its sorted-alignment restriction under the full stabilizer.
- **The fibres of `π`**: enumerated on the carriers of four, six and eight points, shapes `2 × 2`, `2 × 3`,
  `3 × 2`, `2 × 4` and `4 × 2`: every fibre has exactly `|R(m, n)|` elements, and every partition has
  `(m!)^(n−1)` alignments.
- **Act 37's arc** (production path): strictly, the frozen `2 × 8` partition structure per orientation holds
  identically and the only exceptional point is `u = 1`; up to diagonal equivalence the exceptional points are
  `u = 1` and `u = −1`.
- **Act 40's family**: 46 partition candidates; **43** nonempty loci, strictly and relaxed, strict equal to
  relaxed for all 46; **21** distinct flats, of which four are the points `u₁ = ±z⁻², u₂ = 1, u₃ = ±1`; the
  maximal flats exactly the five faces. At act 40's seventeen exact points the independent path counts
  `[0, 0, 1, 1, 2, 0, 1, 1, 0, 4, 8, 5, 20, 4, 20, 20, 4]` admitted partition structures, strictly and relaxed
  alike, with valid alignments `[0, 0, 128, 128, 256, 0, 128, 128, 0, 272, 596, 576, 976, 272, 976, 976, 272]`;
  act 40's sorted control recorded `[0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4]`.
- **Act 36's `4 × 4` hulls**: over every valid alignment of the ten admitted `4 × 4` partition structures (five per orientation) and every circle choice, **31168 parametrizations**, of which 492 lie at the sorted alignments; they give **3896 distinct hulls as matrix families** and **3896 distinct hulls modulo the gauge** under Definition 7 — two counts, measured separately; whether the map sending a matrix-family hull to its hull modulo the gauge is a bijection is a separate boolean the probe measures, and no correspondence is asserted beyond it — and the 492 sorted parametrizations give 492 distinct hulls in each sense. Every one of the 3896 has tangent dimension **14** modulo the gauge, every generator in `ker DF`, and `D²F` vanishing on every pair of its generators; the rank of their combined tangent span modulo the gauge, recomputed, is **49**, the whole defect; and `W` lies in **none** of their tangent spaces. Distinct generator sets number 3896 as well, so at `D` no two parametrizations with different generator sets span the same hull. The exact comparison took 9692 seconds locally under contention; the probe buckets by a reduction modulo a large prime before the exact comparison, and the second equality test runs within buckets.

***

## The definitions, FROZEN

**Definition 1 — shape and orientation.** A shape is `(m, n) ∈ {(4, 4), (8, 2), (2, 8)}`. A
structure of `H` in the **column form** is one of `H`; in the **row form** it is one of `Hᵀ`. The
orientation is part of every object defined below.

**Definition 2 — partition structure.** A partition structure of shape `(m, n)` in a form is a
partition of the sixteen columns (of `H`, or of `Hᵀ` in the row form) into `m` **blocks** of `n` and a
partition of the sixteen rows into `n` **row classes** of `m`, as unordered sets of unordered sets.

**Definition 3 — alignment.** An alignment of a partition structure is a partition of the rows into
`m` **threads**, each meeting every row class in exactly one row. A partition structure has
`(m!)^(n−1)` alignments.

**Definition 4 — index map and its projection.** An index map of shape `(m, n)` is a pair
`(eR, eC)` of bijections `Fin m × Fin n ≃ Fin 16`, for the rows and the columns: act 36's datum with
`α = Fin m`, `β = Fin n`. Its **projection** is the deterministic map

`π(eR, eC) = (form, {eC({c} × Fin n)}_c, {eR(Fin m × {b})}_b, {eR({a} × Fin n)}_a)`,

its partition structure and its alignment. The group `R(m, n) = S_m × S_n × S_m × (S_n)^m`, relabelling
`a`, `b`, `c` and, within each block, `d`, acts on index maps and preserves `π`. **Every fibre of `π`
over a (partition structure, alignment) pair has exactly `|R(m, n)| = m! · n! · m! · (n!)^m` elements**:
a row map is fixed by the order of the row classes and the order of the threads, because a thread meets
a row class in exactly one row, and a column map by the order of the blocks and the order within each. The
probe checks this by exhaustive enumeration on small carriers and at `SIG` (section 1); it is not
assumed.

**Definition 5 — realizing.** `H` admits a **strict** Diţă form at `(eR, eC)` when
`H[eR(a, b), eC(c, d)] = X[a, c] · D[c, b] · Y_c[b, d]` for a flat unitary `X`, flat unitary `Y_c` and
unit twists `D` (act 36's `dita`, column form; the row form is the same statement for `Hᵀ`); a
**relaxed** one when `D₁ · H · D₂` does, for unit diagonals `D₁`, `D₂`. Whether `(eR, eC)` realizes
`H` depends only on `π(eR, eC)`; the probe checks it at literal index maps (section 1). An alignment is
**valid** when the index maps over it realize `H`. A partition structure is **admitted** when some
alignment of it is valid. For a family, a partition structure's **locus** is the union over its
alignments of the parameters at which that alignment is valid.

**Definition 6 — factorization classes, partition orbits and the frozen group action.** The acted-on set is the set of
realizing triples `(orientation, partition structure, alignment)` of `SIG` — equivalently, realizing
index maps modulo `R(m, n)`. The group is act 36's certified stabilizer of `SIG` in `G_ext`, of order
1024, each element given by its position map on the 256 entries: a row permutation `ρ`, a column
permutation `κ` and a transposition flag `τ`, with position `(i, j)` sent to `(ρ(i), κ(j))` when `τ = 0`
and to `(κ(j), ρ(i))` when `τ = 1` (the conjugation flag moves no index and is not part of the
action). An element acts on a triple by mapping every index set through `κ` if it is a set of columns
of `H` and through `ρ` if it is a set of rows of `H` — in the column form blocks are column sets and
row classes and threads row sets; in the row form the reverse — and, when `τ = 1`, by exchanging the
orientation. Four counts are reported, each with its group:
- (i) **factorization classes under the full stabilizer**: orbits of realizing triples, a structure
  identified with its transpose;
- (ii) **factorization classes under the transpose-free subgroup**, of order 512: orbits of
  realizing triples with the orientation kept separate;
- (iii) **partition orbits under the full stabilizer**: orbits of admitted partition structures, a
  partition structure identified with its transpose;
- (iv) **partition orbits under the transpose-free subgroup**.

Act 37 counted (iii) at the sorted alignment and called the orbits its "classes".

The probe checks that the set of realizing triples is closed under the action, in each notion.

**Definition 7 — a `4 × 4` hull and its equality.** For a realizing `4 × 4` index map at `SIG` and a
choice of Fourier circle through `X` and through each `Y_c` (act 36's circle directions), the hull is
the family `SIG ∘ ∏_k t_k^{v_k}` over its twenty-one generating exponent vectors `v_k` (one for `X`,
four for the `Y_c`, sixteen twists), `t_k` units. As a set of matrices it is the image of a torus
homomorphism and is determined by the rational span of the `v_k`; modulo the gauge, by that span
plus the gauge. **Two hulls are equal as matrix families when their generator spans are equal, and
equal modulo the gauge when their spans plus the gauge are equal**, both decided exactly by reduced
row-echelon form over the rationals. A hull's tangent space modulo the gauge is its span plus the gauge,
modulo the gauge.

***

## The measured propositions — what is measured, and how

No proposition fixes a value. Each names the quantity, the notions, the two computations that must
agree, and the probe section. The result note states the values measured at `E`.

**`A41-0` — the reading, FROZEN and not computed.** The census quantifiers of acts 36 to 40 range over
index maps in the sense of Definition 4. A Diţă structure "of some shape, index map and orientation"
is admitted by `H` exactly when some alignment of some partition structure is valid for `H`.

**`A41-36` — act 36's points and hulls.** At `P` and at `Pu(u₅)`, per form and shape, strictly and
relaxed: the partition candidates, the admitted partition structures, the valid alignments of each and
the realizing index maps; that is, the full-index-map census behind act 36's "no `4 × 4` and no
`8 × 2` factorization, exactly one `2 × 8`". At `SIG`, for shape `4 × 4`: the partition structures, the
valid alignments of each, the realizing index maps, the factorization classes and partition orbits (i)–(iv); then the hulls
of Definition 7 over every valid alignment and circle choice: the number of parametrizations, the
number of distinct hulls as matrix families and, separately, modulo the gauge, whether the map from
the first to the second is a bijection, the tangent dimension modulo the
gauge of every distinct hull, whether every generator of every distinct hull lies in `ker DF` and
`D²F` vanishes on every pair of its generators, the rank of the combined tangent span modulo the
gauge, recomputed, and the number of distinct hulls whose tangent contains `W`.

**`A41-37a` — the census of the stratum point.** At `SIG`, per form and shape, strictly and relaxed:
partition candidates, admitted partition structures, valid alignments of each, realizing index maps,
and the factorization classes and partition orbits (i)–(iv), with closure under the stabilizer.

**`A41-37b` — act 37's arc, strictly.** Along `Pu u = SIG ∘ u^W`, strictly: the admitted partition
structures identically on the arc, with the valid alignments of each; the strict exceptional set; and,
at every exceptional point, the admitted partition structures and their alignments.

**`A41-37c` — act 37's arc, up to diagonal equivalence, a separate statement.** The same quantities
relaxed. Stated as its own proposition; not part of act 37's claim.

**`A41-38` — act 38's arc.** Along `Hu u = SIG ∘ u^E`, strictly and relaxed: the exceptional set; the
parameters at which each admitted partition structure of `SIG` is admitted along the arc; at every
exceptional point the admitted partition structures and their alignments, with each identified, where
it is one, as the image of a partition structure of `SIG` under the row exchange `7 ↔ 15`, the column
exchange `2 ↔ 8` or both; and whether any partition candidate's locus contains the arc — the
condition for `E` to lie in a first-order Diţă subspace under some alignment.

**`A41-40` — act 39's family.** For `H3`, strictly and relaxed: the partition candidates; each
candidate's locus as the union over its alignments; the number of nonempty loci; whether the strict and
relaxed loci agree candidate by candidate; the distinct flats, split into those cut out by coordinate
characters and the others; the maximal flats; and the admitted partition structures and their
alignments at `(1, 1, 1)` and `(−1, −1, −1)`.

### Agreement — the two independent computations

Every proposition is computed twice, by code paths that share no function beyond act 36's exact
Gaussian arithmetic and the definition of `H`:

- **the production computation** — act 40's partition-candidate enumeration and flat calculus, with
  each candidate's conditions factorized by row class (each rank-one condition involves one row class and
  the reference row class only), giving loci as unions of flats over alignments;
- **the independent computation** — at every named test case below: act 36's
  exhaustive partition search on the numeric matrix, then every alignment enumerated by its own loop,
  then the factorization tested by exact reconstruction with factor unitarity. It uses neither the flat
  calculus, nor act 40's candidate enumeration, nor any canonical form of the production path.

**The forty-two named test cases**, each a (role, family, parameter) triple: `SIG`; `Pu(−1)`, `P`,
`Pu(u₅)`; `Hu(−1)`; act 40's seventeen exact points; and act 38's twenty Gaussian-rational candidate points.
They are forty-two roles, not forty-two distinct matrices: `SIG` occurs three times (as itself, as act 40's
`(1, 1, 1)` and as act 38's `u = 1`) and `Hu(−1)` three times (as itself, as act 40's `(−1, −1, −1)` and
as act 38's `u = −1`), so the cases carry thirty-eight distinct matrices. The duplicates are kept as
cross-controls: both role labels are preserved, and the probe checks that the matrices of coinciding
cases are equal entry by entry and that every path returns the same result for each of them.
**Agreement** holds when, at every test case and in each notion, the two computations give the same set of admitted partition structures with
the same number of valid alignments for each. For the factorization classes, the orbit enumeration is
checked against an independent count by Burnside's lemma, the average number of fixed triples. For the
hulls, the distinct count by reduced echelon forms is checked against an independent count in which
two hulls are equal exactly when the rank of their joint span equals the rank of each.

***

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze on a disposable branch from exactly `D` that is never landed
and from which no `F` is cut. The run is a `workflow_dispatch` run whose `head_sha` is the commit named;
it is design evidence recorded here, not a `check-run` attestation, and no predicate of the round reads
it.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36542154102 | `34efa117c80ab13c789e0282fc9b3abfdc3fb807` on `claude/a41-predicted`, three linear commits from exactly `D` | **the predicted execution tree less the result note**: a draft of this file (differing from its final text only in the four blob fields and this row); `controls.py` `000a901a04851c621f38f653b9efa8c0d7dd8331`; the three probes `d539fe5f660b198aa944e17984718c0d9106f3b5`, `e7645da5ffec1c21cbdde90763dd1e9e01a14d48`, `a74fb7cc3546907e42dc3e1f7837bbde546d32e9`; the workflow `d9e372f1dc4ba5b45031d5b7f5d87dc78fd6d854` (`D`'s with the frozen edit); `measurements.json` as measured at `D`; and the eleven surfaces rendered from it by the ledger | all twelve jobs green: the `Mathlib bridge` (16 min 23 s) with the release gate passing all 21 steps, `lean-axioms` at 5251 named results and no sorry, sixteen receipts holding and the 303 legacy records intact; `Numerical probes / A41 production` (2 min 26 s), `/ A41 independent` (6 min 27 s) and `/ A41 hulls` (15 min 35 s), each ending `OK -- REPLAYED`; the A36, A38 and A40 shards green on the relabelled earlier probes, act 38's with the bugfix; the guard `ALL CHECKS PASS`; the aggregate `Numerical probes` reading success from all nine shards |

Locally, on the same tree: the three probes replay `measurements.json` elementwise; the guard's output is
byte-identical to its output at `D`; `controls.py --self-test` passes with 21 mutation controls each
detected; and `controls.py check` on a local-only synthetic result note returns `OK` with the label
`A41-CENSUS-CORRECTED`. The hull shard finishes before the bridge build and is not on the critical path;
the topology is frozen as three shards.

***

## The exact-computation layer — the frozen probes

The two computations are separate files, which import nothing from each other; the hull census is a third:

- **`verification/lean/dita_index_map_probe.py`**, blob **`d539fe5f660b198aa944e17984718c0d9106f3b5`** — the production path and the
  round's controls: sections 0 to 8, 10 and 11 below;
- **`verification/lean/dita_index_map_independent.py`**, blob **`e7645da5ffec1c21cbdde90763dd1e9e01a14d48`** — the independent path,
  section 9: act 36's partition search on the numeric matrix, its own alignment-matching count with factor
  unitarity, at the forty-two named test cases.

Each is written before `F` and added at stage 1 with exactly its blob. Both use Python integers and
fractions for every value, no floating point, and each prints its measured values and one canonical JSON
object of them, normalized — each admitted partition structure as sorted tuples with its orientation, shape
and valid-alignment count, per test case and notion — so that the two outputs are comparable without either
consuming the other's candidate list, canonical form or output.

**Topology.** Three shards from the outset, each required by the aggregate `Numerical probes` job and
wired as act 40's shard was: the production path, the independent path, and the hull census of section 4,
which is a third file, `verification/lean/dita_index_map_hulls.py`, blob **`a74fb7cc3546907e42dc3e1f7837bbde546d32e9`**, because its exact
recount took 2 h 40 min locally. No shard is split further: in the disposable predicted-tree run the hull shard finished before the bridge
build (pre-freeze evidence above).

**Agreement and the label.** At stage 1 each shard prints its JSON. The execution commits both, verbatim
from the stage-1 logs, as `measurements.json` — one object per path. From stage 2 on, each shard also
replays: its fresh JSON must equal its own object in `measurements.json` elementwise, or the shard ends
`FAILED` (§A.26's deterministic replay). The agreement test and the label are a frozen function of
`measurements.json` alone, `controls.py agree`, run in `controls.py check E`: it compares the two objects at
every test case and notion, and checks the invariants each path records (the fibre sizes, closure under the
stabilizer, the Burnside count, the two hull-equality tests). Each shard ends with exactly one of:

- `dita_index_map_…: OK -- MEASURED` (stage 1) or `OK -- REPLAYED` (from stage 2) — every control of that
  shard green;
- `dita_index_map_…: FAILED …`, exit 1 — a control red, or a replay mismatch.

**0. Act 40's head, replayed**: the stabilizer, order 1024; the flat calculus self-test; the 46
partition candidates.

**1. The index-map calculus.** `|R(m, n)|` and `(m!)^(n−1)` for the three shapes. On the carriers of
four and six points, every index map of shapes `2 × 2`, `2 × 3` and `3 × 2` enumerated and projected,
every fibre of `π` of size `|R(m, n)|`. At `SIG`, for every admitted partition structure, forty literal
index maps drawn by a seeded generator from fibres over valid alignments and forty from fibres over
invalid ones: `SIG` reconstructed exactly as `X · D · Y` at each of the first and at none of the
second.

**2. The sorted control** — the landed values, reproduced from the sorted alignment only: act 37's
eighteen at `SIG`, `(5, 4)`, `(3, 2)`, `(3, 3)`, nine orbits; act 38's one `2 × 8` per orientation at
`u = −1`; act 40's 16 empty and 30 nonempty loci, all coordinate, 18 at `(1, 1, 1)`, 2 at
`(−1, −1, −1)`; act 36's 492 hull parametrizations. A red section 2 ends the probe `FAILED` before any
other value is compared.

**3.** `A41-37a`. **4.** `A41-36`. **5.** `A41-37b` and `A41-37c`. **6.** `A41-38`. **7.** `A41-40`.

**8. Exact reconstruction** of every admitted partition structure that the sorted control lacks, at
one valid alignment each, in each notion where it is admitted, from flat unitary factors and unit
twists — with the unit diagonals exhibited in the relaxed notion — entry by entry.

**9. The independent computation** at the forty-two named test cases, and the agreement test.

**10. The exchange identities**, as controls: `H3(−u₁, u₂, u₃)` is `H3(u₁, u₂, u₃)` with rows 7 and 15
exchanged, and `H3(u₁, u₂, −u₃)` is it with columns 2 and 8 exchanged, at fifteen exact points; and the
production loci of the `−1` faces are the images of those of the `+1` faces under the exchanges.

**11. Countercontrols**: a partial alignment rule — sorted in every row class but one — fed to the
production path must disagree with the independent computation at `SIG`; and act 40's perturbed
pieces, one entry of `C` cleared, classified under every alignment, must give a union different from
the five faces.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the sorted control | section 2 | the implementation reproduces every landed sorted value before any other value is read |
| the fibres of `π` | section 1 | the realizing-index-map count is the alignment count times `|R(m, n)|`, checked by enumeration, not assumed |
| literal index maps | section 1 | realizing depends on the projection alone, checked by reconstruction at literal index maps |
| exact reconstruction | section 8 | every added partition structure is exhibited with flat unitary factors |
| the independent computation | section 9 | the production path is checked by a path sharing no candidate generator or canonical form |
| the stabilizer | section 3 | the realizing triples are closed under the frozen action (§A.21); orbits checked by Burnside's lemma |
| the hull equality | section 4 | the distinct-hull count checked by a second equality test |
| the exchanges | section 10 | the `−1` faces are the exchange images of the `+1` faces |
| the flat calculus | section 0 | act 40's self-test, replayed |
| wrong inputs are detected | section 11 | a partial alignment rule and a perturbed family each give a detectable difference |
| agreement | `controls.py agree` | the label is a frozen function of the replayed `measurements.json`; neither path reads the other |
| the duplicate test cases | sections 9 and 3–7 | coinciding cases carry equal matrices and every path returns one result for them |

***

## The surfaces — corrected forward from the measurement

Each edit is frozen as a splice of `D`'s file: its span, the hash of the old text, a template for the
new text whose slots are filled only from `measurements.json`, and the reason. Where a template's
wording depends on a structural fact — an identification, an equality of loci — the probe measures that
fact as a boolean and the template selects between frozen alternatives; no wording is chosen by hand.
`controls.py` renders every splice from `measurements.json` and checks each surface at `E` against the
rendering.

The ledger is the replacement column of the claim-surface census (appendix), each row a splice of `D`'s
file with the old text's hash, a new text that is fixed where the correction is a re-scoping and a template
where it states a measured value, and the census row id as its reason. It is finalized in the controls phase,
from this census, before `F`. Its rows fall in five kinds:
- **the five earlier probes, string constants**: check labels, section titles, docstrings and success text,
  re-scoped to "at the sorted alignment" and pointing to this round's probes for the all-alignment
  statements;
- **one semantic bugfix, the only non-string change to an earlier probe**: at
  `dita_local_escape_probe.py` line 541, the tuple element `any(x[2] == GEN_ONE for x in [])` — which iterates
  an empty list and is constantly `False`, a vacuous control component — and its matching expected `False`
  are removed, with the label re-scoped (census row L21). The four remaining components carry the check:
  the two condition checks show `M_COL` and `M_ROW` are not admitted generically, and the two
  `admitted_points(…) == {−1}` checks show their isolation, including exclusion at `u = 1`;
- **the four Diţă modules**: docstring splices, fixed text (census rows LH2, LA1, LA2, LE1–LE3, LL2);
- **the census registry**: the notes and names of the families for acts 36, 37, 38 and 40, keeping each
  outcome label and each account of what the round measured, and adding the current value under the frozen
  reading, attributed to this round;
- **`ROADMAP.md`**: the five `P0`-cell statements that reproduce at `D` the frozen `P0` sentences of acts
  36, 37, 38 and 40 (rows R2–R5, R7), corrected in place; the two future-direction phrases (R9, R10); and
  this round's `P0` sentence and standing clause, appended once.

**The live `P0` cell and the historical records.** `ROADMAP.md` is a live status surface: after this round
its corrected paragraphs are the current `P0` statement, with act 41 as their evidentiary provenance, and they
are not described anywhere as the frozen sentences of acts 36 to 40. Those frozen sentences stay recoverable
verbatim from the rounds' preregistrations and result notes, which this round does not touch, and from git
history (§A.27, §A.30: an incorrect assertion is corrected in place, not qualified beneath).

**Preservation, checked by `controls.py check E`.** For each of the five earlier probes, the syntax trees at
`D` and `E` are equal once the ledger's string constants are masked, **except for exactly one enumerated
non-string difference, the bugfix above**, which is compared node for node against its ledger entry; any
other non-string difference fails the check. Every historical file of acts 36 to 40 — their record
directories and the receipts `A36.json` to `A40.json` — is byte-identical at `E` to `D`, file by file, and
only the ledger's spans of the live surfaces move.

## Kernel additions — considered and not made

Two kernel additions were considered: the fifth `4 × 4` factorization of `SIG`, and the exchange
identities carrying act 40's `+1` faces to its `−1` faces. No frozen proposition needs either: every
corrected statement is a count, locus or hull of the exact-computation layer that acts 36 to 40
assigned to their probes, and every new existence claim is exhibited by exact reconstruction. The
kernel statements of acts 36 to 40 concern named index maps and are unaffected.

***

## The question, FROZEN — one target

### `A41` — the censuses of acts 36 to 40 under every index map

**Under the frozen reading of an index map, what are the partition-structure, alignment,
realizing-index-map, factorization-class and partition-orbit counts, the loci and the hulls that acts 36 to 40 measured
at one alignment per partition structure?** The answer is the values measured at `E`, reported as one
of three labels:

- `A41-CENSUS-CORRECTED` — every control green and the two computations in agreement: the result note
  and the corrected surfaces are generated from the measured values;
- `A41-CENSUS-DIVERGES` — every control green, and the two computations disagree, or a frozen
  invariant fails (the fibre sizes, closure under the stabilizer, the Burnside count, the two hull
  equality tests, the duplicate test cases): the result note reports both sets of values and names the disagreement; no surface is
  edited, since neither value is certified;
- `A41-UNDECIDED` — a control red in either shard, a replay mismatch, or a shard not run to completion at
  `E`: no value is reported as measured.

The label is `controls.py agree` applied to `measurements.json`, with both shards `OK -- REPLAYED` at `E`:
agreement and every invariant holding gives `A41-CENSUS-CORRECTED`, anything else with both shards green
`A41-CENSUS-DIVERGES`, and a shard not green `A41-UNDECIDED`.

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A41` | `A41-CENSUS-CORRECTED` | **very high** | the production and independent computations were run at `D` and agreed at every point computed; the headline values were also reproduced by two research computations sharing no code with either |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence template

Each sentence is a template: `{slot}` is a measured value named in the slot table below, written in words below one
hundred and in digits from one hundred; `[[a | b : flag]]` is `a` when the measured boolean `flag` holds and `b`
otherwise. `controls.py` renders the sentence for the label from `measurements.json` and checks the result note's
sentence against the rendering; the same renderer fills the ledger's templates.

### `A41-CENSUS-CORRECTED`

> At the frozen product configuration, under the reading of an index map that acts 36 to 40 froze — a pair of bijections of the product with the carrier, fixing the alignment of the rows across row classes as well as the partition — the Diţă censuses those acts measured at one alignment per partition structure are, by the round's exact computation in two independent paths and not by the kernel, as follows. At the certified rational stratum point: {sig.partitions} partition structures, {sig.per_form} per orientation, with {sig.alignments} valid alignments, [[the same strictly and up to diagonal equivalence | differing between the strict and relaxed notions : sig.strict_eq_relaxed]]; {sig.classes_full} factorization classes and {sig.porbits_full} partition orbits under the stabilizer with transposition, and {sig.classes_tfree} and {sig.porbits_tfree} under its transpose-free subgroup; act 37's nine are the {sig.sorted_porbits} partition orbits of its sorted-alignment restriction of {sig.sorted_partitions} partition structures. Its `4 × 4` hulls: {hull.params} parametrizations, {hull.distinct_mat} distinct hulls as matrix families and {hull.distinct_gauge} modulo the gauge, of tangent dimension {hull.dims} modulo the gauge, [[each inside the linearized and second-order unitarity conditions | not all inside the unitarity conditions : hull.dF_ok]], their tangents spanning {hull.span} dimensions modulo the gauge, and act 36's line `W` in {hull.W_in} of them; act 36's {hull.sorted_params} are the parametrizations at the sorted alignments. Along act 36's arc, strictly: [[exactly the frozen `2 × 8` partition structure per orientation at every unit other than `u = 1` | not only the frozen `2 × 8` partition structure away from `u = 1` : w.exclusive]], with exceptional set {w.exc_strict}; up to diagonal equivalence, in a separate statement, exceptional set {w.exc_relaxed}, with {w.m1_relaxed} partition structures at `u = −1`. At act 36's points `P` and `Pu(u₅)`: [[no `4 × 4` and no `8 × 2` partition structure | a `4 × 4` or `8 × 2` partition structure : p.no_44_82]] under any alignment, and {p.p28} `2 × 8` partition structure per orientation, under {p.alignments} of its alignments. Along act 38's arc: exceptional set {e.exc_strict} strictly and {e.exc_relaxed} up to diagonal equivalence, with {e.m1} partition structures at `u = −1`[[, two of them obtained from act 37's `k4` by the row exchange `7 ↔ 15` and the column exchange `2 ↔ 8` | : e.m1_k4_exchanged]]. For act 39's family: {h3.candidates} partition candidates, {h3.nonempty} with nonempty loci, [[strict and relaxed loci equal for every candidate | strict and relaxed loci not equal for every candidate : h3.strict_eq_relaxed]], {h3.noncoord} of the loci's flats off the coordinate characters, and maximal flats {h3.maximal}[[, act 40's five faces | : h3.five_faces]]. The kernels of acts 36 to 40 concern named index maps and stand, and every verdict of those rounds stands as recorded. This is a statement about the frozen mathematical objects; it censuses no exponent matrices, decides no minimality, concerns no family other than those of acts 36 to 40, and adopts no family, factorization or isometry as a symmetry, a principle or a law.

### `A41-CENSUS-DIVERGES`

> At the frozen product configuration, under the reading of an index map that acts 36 to 40 froze, the round's two independent exact computations of the Diţă censuses of acts 36 to 40 disagree, or a frozen invariant fails, every control green: {note.disagreements}. Both sets of values are recorded in the result note; no current surface is corrected from them. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.

### `A41-UNDECIDED`

> A control of the round's probes was red at `E`, or a probe did not run to completion: {note.failing}. No value is reported as measured.

### The `P0` sentence

On `A41-CENSUS-CORRECTED` this round's `P0` sentence and standing clause are appended once to the `P0` cell, as the
ledger's `append` entry freezes them (appendix B).

## What no outcome licenses

- **No outcome revises a verdict of acts 36 to 40**, edits their records, or states that their kernels
  proved less than they did.
- **No outcome adds or changes a mathematical declaration**, or states that any measured count is
  kernel-certified.
- **No outcome merges the counts**: partition structures, alignments, realizing index maps,
  factorization classes and hulls are each reported as themselves, the group named with every factorization-class
  and partition-orbit count.
- **No outcome folds a relaxed fact into a strict claim**, in either direction.
- **No outcome censuses exponent matrices, decides a support minimality or classifies another family.**
- **No outcome classifies the product normalized set or its isometries, selects a law or closes `P0`.**

## Non-doings

No record of acts 36 to 40 is touched; no Lean statement, proof or `#print axioms` line changes; no
check value or computation of an earlier probe changes; no guard clause, seal record or certificate is
created; no disposable branch is landed.

## Evidence level

Exact computation, replayed in CI, by two independent paths: exact Gaussian-rational arithmetic, an
exact monomial calculus and an exact calculus of flats. Not kernel-certified.

***

## `controls.py` — the round's own contracts, FROZEN

`controls.py`, blob `000a901a04851c621f38f653b9efa8c0d7dd8331`, is written before `F` and added at stage 1. `controls.py
--self-test` checks that every template and splice has one source, and that each check below fails on a
named mutation. `controls.py check E` checks, at `E`:
- the governed set: `git diff --no-renames --name-status D E` lists exactly the frozen paths for the
  label;
- the two probes' blobs; the workflow is `D`'s with the frozen edit; the guard is `D`'s;
- the five earlier probes: syntax trees equal to `D`'s with the ledger's string constants masked, except
  the one enumerated bugfix, compared node for node with its ledger entry; the constants equal to the
  ledger's text;
- every historical file of acts 36 to 40 — their record directories and `verification/receipts/A36.json` to
  `A40.json` — byte-identical to `D`'s;
- the four modules: `D`'s outside the leading docstring block, and the docstring equal to the ledger's
  rendering;
- the census registry and `ROADMAP.md`: equal to the ledger's rendering from `measurements.json` on
  `A41-CENSUS-CORRECTED`, and to `D`'s otherwise;
- `measurements.json`: canonical, one object per path, and `controls.py agree` on it giving the label;
- the result note: exactly one outcome line with that label, both shards' final lines verbatim, the
  post-round sentence equal to its rendering, no bare "structures" count, and "class" only in the compounds
  *row class*, *factorization class* and *realizable class*.

***

## The execution

1. **`C1`**: the preregistration at `F` has its frozen blob, verified before the first execution commit.
2. **Stage 1** — `controls.py`, the two probes, the workflow edit. The exact-head run shows every job
   green, each A41 shard `OK -- MEASURED`, and `lean-axioms` at 5251. The two canonical JSON objects from
   that run are the measurement.
3. **Stage 2** — `measurements.json` as the stage-1 run printed it, and, when `controls.py agree` gives
   agreement, every surface of the ledger rendered from it. The exact-head run shows every job green, each
   A41 shard `OK -- REPLAYED`, the `Mathlib bridge` rebuilt with `lean-axioms` 5251, the earlier
   probes' shards green with their values unchanged, and the release gate 21 of 21.
4. **The result note** — candidate `E`, generated from `measurements.json`; `controls.py check E` must
   print OK; the dispatch at `E` is `E`'s `check-run` attestation.
5. Receipt, reconciliation and landing as §A.39 orders, each on owner direction.

### Invariants and their checkpoints

| invariant asserted | checkpoint that measures it |
| --- | --- |
| no mathematical declaration changes | `controls.py check E`: modules equal to `D`'s outside the docstring; `lean-axioms` 5251 at stages 1 and 2 and at `E` |
| no earlier probe's computation changes | `controls.py check E`: masked syntax trees equal; the shards green at every stage |
| no record of acts 36 to 40 changes | `legacy-records` and `v3-receipts` at every stage; the governed-set check |
| the sorted enumeration is a control only | section 2 precedes every other section; a red section 2 ends the production shard `FAILED` |
| every count names its kind, every factorization-class and partition-orbit count its group, and "class" never occurs bare | `controls.py check E` on the result note and the rendered surfaces |
| the historical records of acts 36 to 40 byte-identical; only the ledger's live spans move | `controls.py check E`, file by file against `D` |
| the one non-string change to an earlier probe is the enumerated bugfix | `controls.py check E`: masked syntax-tree comparison with one enumerated exception |
| the two paths independent | the two probe files import nothing from each other; `controls.py check E` parses their imports |
| strict and relaxed kept apart | every value keyed by notion in `measurements.json`; separate template slots |
| surfaces generated, not typed | `controls.py check E` renders every splice and sentence from `measurements.json` |
| the measurement replays | each shard at stage 2 and at `E` requires equality with its object in `measurements.json` |
| the guard unchanged | `controls.py check E`: guard blob `d28e9b3c…` |
| the verdict generated from measurements | the label is `controls.py agree` on the replayed `measurements.json`; the result note's label is checked against it |


***

## Appendix A — the claim-surface census at `D`, in full

All text below was read from git objects at D41 = `78ea3c39004e97aad027ee6153051c6d372bdd55`. Nothing in the
repository was modified.

## Scope and method

- **In scope:** every file not under `verification/programmes/`, `verification/receipts/`,
  `verification/seals/`, `verification/certificates/`, and not listed in
  `verification/infrastructure/legacy-records.json` (none of the files below is listed there).
- **Search:** `git grep` at D41 for `Diţă|Diță|Dita|dita_|SIG|index map|eighteen|support 48|three-parameter|census`
  and for `A3[6-9]-|A40-|a3[6-9]_|a40_|exceptional set|five faces|DitaHierarchy|DitaArc|DitaLocal|DitaTorus`.
  The only non-record files carrying act 36–40 content are the five probes, the five Lean modules (plus
  their `import` lines in `OIBridge.lean`), `verification/lean-manuscript-census.json`,
  `verification/ROADMAP.md` and `.github/workflows/verify.yml`. The remaining hits were checked and are
  unrelated. `verification/README.md` has four "eighteen" hits, all about seals and contracts.
  `papers/GR.md` has one "eighteen" hit, which is unrelated. `tools/`, `papers/` and `book/` contain no
  Diţă content.
- **Probes:** every docstring, comment, section title, check label and OK line was read. The Lean modules
  contain comments only in their module headers (checked with a block-comment scan; there are no `--` or
  `/--` comments).

### Kinds

| code | meaning |
| --- | --- |
| **a** | Absolute claim that is false under all alignments. |
| **a\*** | Absolute claim whose content holds under all alignments but which says it was certified by a probe that tested one alignment. The certification it cites does not exist at D41. |
| **b≠** | Sorted-only count or verdict presented without scope; the all-alignment value differs. |
| **b=** | Sorted-only computation presented as exhaustive; the value happens to equal the all-alignment value. |
| **b?** | Sorted-only computation presented without scope; the supplied all-alignment table does not give this value. |
| **c** | Survives unchanged; the reason is stated. |
| **d** | Text in the ROADMAP P0 cell that reproduces a round's frozen P0 sentence verbatim. Verified: each act-36…40 segment of the cell appears word for word in that act's `preregistration.md`. |

"Sorted alignment" means one index map per partition structure: the rows of each class in sorted order,
i.e. `row[(a,b)] = rows[b][a]` in `dita_orientations`, `structures`, `conditions`,
`conditions_E`, `relaxed_at_point` and act 40's `conditions`. Proportionality candidates (column
partition plus row classes) do not depend on the alignment. Rank-one, relaxed rank-one, factor
unitarity, loci and hulls do.

**Replacement convention.** The replacements use "at the sorted alignment" or "with the rows of each class in
sorted order", with no revision-history words and no capitals. Where a sentence's content survives and it
cites all-index-map certification (kind a\*), the replacement cites "exact computation over every index
map". That wording is supported only once the all-alignment search is itself part of the
exact-computation layer, for example as the act-41 probe; the replacement must cite that probe. Until then
the only supported text is the sorted-scoped fallback that is also given.

### Independent sanity check (in memory, no files written)

I executed the act-38 probe head from the D41 blob and ran an all-alignment rank-one + factor-unitarity
test with class 0's alignment fixed; a simultaneous relabelling of `a` across all classes permutes the rows
of `X` only. Results:

- At SIG, 4×4: all 5 candidates admit an exact alignment in each orientation, with 8, 64, 8, 8 and 8 of the
  13824 relative alignments exact. k5 is the fifth candidate, whose sorted alignment fails. 2×8: 3 of 3,
  with every one of the 128 alignments exact.
- At H(−1) = SIG∘(−1)^E, the single 4×4 candidate is exact in each orientation (8 alignments), and so is the
  single 2×8 candidate. This gives **one 2×8 and one 4×4 structure per orientation**, which matches the
  supplied "4 (two 2×8 plus two 4×4)".
- The 4×4 partition at H(−1) is **not** any of SIG's five 4×4 candidates, and in particular it is not k5. So
  on act 38's arc, k5 is not even a proportionality candidate at u = −1. Together with the surviving
  exceptional set {1, −1}, k5 is admitted along that arc only at u = 1. The replacements below still speak
  only of named classes and do not rely on this.
- For m = 2 (2×8) every alignment gives the same verdict, so all 2×8 statements are alignment-free.

***

## Summary count by kind

| file | a | a\* | b≠ | b= | b? | c | d | total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `verification/lean/dita_hierarchy_probe.py` | 0 | 0 | 4 | 2 | 3 | 2 | 0 | 11 |
| `verification/lean/dita_arc_exclusivity_probe.py` | 0 | 0 | 6 | 9 | 14 | 3 | 0 | 32 |
| `verification/lean/dita_local_escape_probe.py` | 0 | 0 | 12 | 5 | 9 | 5 | 0 | 31 |
| `verification/lean/dita_torus_probe.py` | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 3 |
| `verification/lean/dita_torus_locus_probe.py` | 0 | 0 | 7 | 2 | 6 | 4 | 0 | 19 |
| `verification/lean-mathlib/OIBridge/Dita*.lean` (5 modules) + `OIBridge.lean` | 3 | 4 | 0 | 0 | 0 | 4 | 0 | 11 |
| `verification/lean-manuscript-census.json` | 5 | 4 | 1 | 2 | 1 | 6 | 0 | 19 |
| `verification/ROADMAP.md` | 2 | 0 | 0 | 0 | 0 | 2 | 7 | 11 |
| `.github/workflows/verify.yml` | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| **total** | **10** | **8** | **30** | **20** | **35** | **28** | **7** | **138** |

Rolled up to the four requested kinds, there are **(a) 18** rows: 10 are false and 8 are true in content
but cite a certification that does not exist. There are **(b) 85** rows: 30 whose value differs, 20 whose
value coincides and 35 with no supplied all-alignment value. There are **(c) 28** and **(d) 7**. Five (d)
rows need a change: R2, R3, R4, R5 and R7, which is A40's attribution clause. Two need none: R1, A36's
kernel sentence, and R6, A39.

***

## Replay: would a label-only edit pass `tools/probe_replay_check.py` against the D41 blob?

**What the tool compares** (`tools/probe_replay_check.py` at D41, lines 20–39):

```python
CHECK = re.compile(r'^  (PASS|FAIL)  .*$')
SUMMARY = re.compile(r'^\w+: (OK|FAILED)')
...
out = [l for l in log.split('\n') if CHECK.match(l)]
out += [l for l in log.split('\n') if SUMMARY.match(l)]
...
if x != y: diffs.append((i, x, y))
```

- It keeps each **entire** check line and the **entire** summary line, and compares them in order with
  exact string equality.
- All five probes print checks as `'  %s  %-70s %s' % ('PASS'|'FAIL', name, got)`. The label is
  therefore part of every compared line. In `dita_hierarchy_probe.py` the first definition, with width 58,
  is shadowed at line 153 before any call.
- The OK lines (`dita_…_probe: OK -- …`) match `SUMMARY` and are compared in full.
- The tool does **not** compare section titles (`== … ==`), timing lines (`  (Ns)`), docstrings or
  comments, because none of them is printed as a PASS/FAIL or summary line.

| probe | check call sites | check labels / OK line needing change | label-only edit passes replay vs D41? |
| --- | --- | --- | --- |
| `dita_hierarchy_probe.py` | 36 (the loop renders 12 lines at l.314, 4 at l.317 and 6 at l.319) | yes: l.314, 319, 439, 469, 470, 472 and the OK line | **No.** Every relabelled line and the OK line produce `DIFF`; the tool prints FAILED. |
| `dita_arc_exclusivity_probe.py` | 33 | yes: many labels and the OK line | **No** |
| `dita_local_escape_probe.py` | 44 | yes: many labels and the OK line | **No** |
| `dita_torus_probe.py` | 15 | none; only docstrings need change | **Yes.** Docstring edits are not printed. |
| `dita_torus_locus_probe.py` | 22 | yes: many labels and the OK line | **No** |

The tool cannot tell a label change from a value change, and its self-test rejects both. A label-only
round therefore cannot use it unmodified as the equality control. One option is a label-insensitive
comparison, which checks for each `DIFF` pair that the verdict and the `got` field are identical. For
labels of at most 70 characters, `got` starts at column 79 (2 + 4 + 2 + 70 + 1). For longer labels,
`got` starts after the label, so the label map must be applied first. Another option is to replay the
D41 blob with its labels substituted by the new ones and then require zero diffs. Section-title,
docstring and comment edits are invisible to the tool as it stands.

**Check values that encode more than their label.** No check value hard-codes an all-index-map assertion.
Every value is either an output of the sorted search or a computation over a named list (`CLASSES`,
`M_COL`, `M_ROW`, `WIT`), so every value remains valid as a sorted-alignment regression value. Four points
nevertheless need flagging:

1. **Act 40, l.646 (value `True`: every nonempty locus is coordinate).** This is the one value that is
   *false* under all alignments (four non-coordinate points). It is correct only as a sorted regression
   value.
2. **Controls that share the defect.** Act 37 l.517, act 38 l.560 and act 40 l.731/748 compare the
   numeric sorted search with the symbolic sorted search. Act 40's section 7 is titled "an independent
   control". Both sides use the same `rows[b][a]` convention, so none of these controls can detect the
   alignment dependence. At (1,1,1) and (−1,−1,−1), act 40's control values (18, 2) are the defective
   counts.
3. **Equivariance controls too weak to catch it.** The sorted alignment is not equivariant under the
   stabilizer. Act 37 l.555 and act 38 l.618 transport only P, H(−1) and H(u5), where the transported
   sorted search happens to agree. Transporting SIG's k3/k5 pair would have exposed k5.
4. **Vacuous component in act 38, l.541.** The first element `any(x[2] == GEN_ONE for x in [])` iterates
   an empty list and is constantly `False`. The generic-u non-admission is carried by components 2–3.
   This defect is unrelated to alignment, but it is a vacuous control component under a label that claims
   it.

***

## `verification/lean/dita_hierarchy_probe.py` (act 36)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| H1 | 256 | `print('== 2. Diţă factorizations by exhaustive search over block structures ==')` | b≠ | The section contains SIG's 4×4 control (4 exact; 5 over all alignments). | `print('== 2. Diţă factorizations by exhaustive search over block structures, the rows of each class in sorted order ==')` |
| H2 | 314 | `'%s-Diţă %dx%d at %s: (candidates, exact factorizations)'` (12 rendered lines: column/row × 4x4, 8x2, 2x8 × P, Pu(u5); values (1, 0), (1, 0), (1, 1)) | b= | P survives (supplied). Pu(u5) survives by act 37's strict exceptional set {1}, since u5 ≠ 1. | `'%s-Diţă %dx%d at %s: (candidates, exact at the sorted alignment)'` |
| H3 | 317 | `'%s-Diţă 2x8 at %s: the frozen blocks and row classes'` | c | A partition-level statement. The 2×8 verdict is alignment-free (m = 2). | — |
| H4 | 319 | `'%s-Diţă %dx%d at SIG = Pu(1): (candidates, exact factorizations) (control)'` (values 4x4 (5, 4), 8x2 (3, 2), 2x8 (3, 3)) | b≠ | 4x4 is (5, 5) over all alignments; 8x2 and 2x8 are unchanged. | `'%s-Diţă %dx%d at SIG = Pu(1): (candidates, exact at the sorted alignment) (control)'` |
| H5 | 353 | `print('== 4. every 4x4 Diţă hull through SIG: orientations, factor circles, exact integrability, the span ==')` | b≠ | The k5 hulls are absent, and so are hulls at other exact alignments of k1–k4 (8, 64, 8, 8 alignments exact). | `print('== 4. the 4x4 Diţă hulls through SIG at the sorted alignment: orientations, factor circles, exact integrability, the span ==')` |
| H6 | 439 | `'4x4 Diţă hulls through SIG (orientations × circle choices)'` → 492 | b? | Being recounted. | `'4x4 Diţă hulls through SIG at the sorted alignment (orientations × circle choices)'` |
| H7 | 469 | `'every hull tangent in ker DF and D²F vanishing exactly on every hull (failures)'` → 0 | b? | The k5 hulls and the other alignments were not tested. | `'every sorted-alignment hull tangent in ker DF and D²F vanishing exactly on every sorted-alignment hull (failures)'` |
| H8 | 470 | `'every hull tangent has dimension 14 mod gauge'` → [14] | b? | Same as H7. | `'every sorted-alignment hull tangent has dimension 14 mod gauge'` |
| H9 | 472 | `'the span of all 4x4 hull tangents mod gauge equals the defect'` → 49 | b= | Survives. The sorted subset already spans 49 = dim ker DF − 31, which bounds any set of hull tangents. | `'the span of the sorted-alignment 4x4 hull tangents mod gauge equals the defect'` |
| H10 | 646 | `'dita_hierarchy_probe: OK -- P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has its 4x4 factorizations; W is an exact straight line at SIG; the 492 4x4 hulls through SIG span the 49-dimensional defect space; the stabilizer …'` | b≠ | "the 492 4x4 hulls" is presented as the complete set. The P / Pu(u5) clause coincides with the all-alignment result. | `'dita_hierarchy_probe: OK -- with the rows of each class in sorted order, P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has four exact 4x4 factorizations of five candidates per orientation; W is an exact straight line at SIG; the 492 sorted-alignment 4x4 hulls through SIG span the 49-dimensional defect space; the stabilizer …'` (tail unchanged) |
| H11 | 322, 581 and sections 1, 3, 5, 6 | `'== 3. the first-order census at SIG: …'`, `'== 6. the second-order form and the obstruction census =='`, and the defect, T_c/T_r, stabilizer and sector checks | c | "census" there means the first- and second-order defect census. It is alignment-free (fixed-pairing T_c/T_r, the stabilizer). | — |

The module docstring (l.1–15) contains no census claim (c; not counted separately).

## `verification/lean/dita_arc_exclusivity_probe.py` (act 37)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| X1 | 7–8 | `Its first part is act 36's probe head, verbatim, for the shared objects and act 36's exhaustive structure search.` | b? | The search is exhaustive over partitions but tests one alignment. | `Its first part is act 36's probe head, verbatim, for the shared objects and act 36's structure search, exhaustive over column blocks and row classes and testing each at the sorted alignment (the rows of each class in sorted order).` |
| X2 | 294–297 | `"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials: …` | b? | Same as X1. | `"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the rank-one condition at the sorted alignment, on a matrix of monomials: …` |
| X3 | 343 | `print('== 1. the census: every Diţă structure of the stratum point, and its classes modulo the stabilizer ==')` | b≠ | 18/9 sorted versus 20/10. | `print('== 1. the census at the sorted alignment: the Diţă structures of the stratum point with the rows of each class in sorted order, and their classes modulo the stabilizer ==')` |
| X4 | 362 | `'exact structures of SIG by shape and form: 4x4, 8x2, 2x8, each column and row'` → (4, 4, 2, 2, 3, 3) | b≠ | (5, 5, 2, 2, 3, 3) | `'exact structures of SIG at the sorted alignment by shape and form: 4x4, 8x2, 2x8, each column and row'` |
| X5 | 363 | `'every structure reconstructs SIG exactly from its factors, with trivial twist'` | b? | k5 was not tested. | `'every sorted-alignment structure reconstructs SIG exactly from its factors, with trivial twist'` |
| X6 | 364 | `'the column-form and row-form structures coincide as index sets (SIG symmetric)'` | b? | Same as X5. | `'the column-form and row-form sorted-alignment structures coincide as index sets (SIG symmetric)'` |
| X7 | 390 | `'the stabilizer (order 1024, with transposition) permutes the 18 structures; orbit count and sizes'` → (9, [2]\*9) | b≠ | 10 classes of 2 | `'the stabilizer (order 1024, with transposition) permutes the 18 sorted-alignment structures; orbit count and sizes'` |
| X8 | 391 | `'each orbit pairs a structure with its own transpose and identifies nothing else'` | b? | This is over the 18 sorted structures only. | `'each orbit of the sorted-alignment structures pairs a structure with its own transpose and identifies nothing else'` |
| X9 | 393 | `'the frozen 2x8 class is one orbit: column and row forms of the frozen blocks and classes'` | c | A named class; 2×8 is alignment-free. | — |
| X10 | 395 | `'the other classes: four 4x4, two 8x2, two 2x8'` | b≠ | Over all alignments there are five 4×4 classes. | `'the other classes at the sorted alignment: four 4x4, two 8x2, two 2x8'` |
| X11 | 406 | `'P admits exactly the frozen class (column form; the row form is the same by symmetry)'` | b= | Survives (supplied). | `'at the sorted alignment P admits exactly the frozen class (column form; the row form is the same by symmetry)'` |
| X12 | 407 | `'Pu(u5) admits exactly the frozen class'` | b= | Survives by the strict exceptional set {1}. | `'at the sorted alignment Pu(u5) admits exactly the frozen class'` |
| X13 | 410 | `print('== 3. the generic arc point, and the obstruction monomial of each other class ==')` | b? | "each other class" means the eight sorted classes; k5 was not tested. | `print('== 3. the generic arc point, and the obstruction monomial of each other sorted-alignment class ==')` |
| X14 | 412 | `'structures at a generic u (u a free symbol): (candidates, exact) by shape'` → ((1, 0), (1, 0), (1, 1)) | b= | Survives: a generic exact 4×4 or 8×2 would contradict the strict exceptional set {1}. | `'structures at a generic u (u a free symbol): (candidates, exact at the sorted alignment) by shape'` |
| X15 | 413 | `'the one exact generic structure is the frozen 2x8 class'` | b= | Same as X14. | `'the one exact generic structure at the sorted alignment is the frozen 2x8 class'` |
| X16 | 435 | `'each other class imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'` | b? | The eight named classes only. | `'each of the eight other sorted-alignment classes imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'` |
| X17 | 455 | `'the kernel witness identity of each other class is forced by its Diţă form, has rational entries and exponent sums {0, 1}'` | b? | The eight named classes (`k1 … t3`). | `'the kernel witness identity of each of the eight named other classes is forced by its Diţă form, has rational entries and exponent sums {0, 1}'` |
| X18 | 458 | `print('== 4. the candidate exceptional set: every point where an extra proportionality or the rank-one condition of a generic candidate appears ==')` | b? | `E_rank` uses the sorted rank-one condition. The all-alignment candidate set is not supplied. | `print('== 4. the candidate exceptional set: every point where an extra proportionality, or the sorted-alignment rank-one condition of a generic candidate, appears ==')` |
| X19 | 491 | `'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at u = 1 only'` | b? | Same as X18. | `'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at the sorted alignment at u = 1 only'` |
| X20 | 493 | `'the candidate exceptional set, exactly (twenty points)'` | b? | Same as X18. | `'the candidate exceptional set of the sorted-alignment calculus, exactly (twenty points)'` |
| X21 | 497 | `print('== 5. the exhaustive search at every candidate point: the exact exceptional set ==')` | b= | {1} survives. | `print('== 5. the search at the sorted alignment at every candidate point: the exceptional set at the sorted alignment ==')` |
| X22 | 502 | `'at u = 1 the search returns the eighteen structures: (candidates, exact) by shape'` → ((5, 4), (3, 2), (3, 3)) | b≠ | 4x4 (5, 5); 20 structures | `'at u = 1 the search at the sorted alignment returns eighteen structures: (candidates, exact) by shape'` |
| X23 | 503 | `'at u = -1 the proportionality candidates are those of u = 1, but only the frozen class is exact'` | b= | Survives ({1} strict). | `'at u = -1 the proportionality candidates are those of u = 1, but at the sorted alignment only the frozen class is exact'` |
| X24 | 504 | `'at every candidate point other than u = 1, exactly the frozen class is admitted'` | b= | Same as X23. | `'at every candidate point other than u = 1, exactly the frozen class is admitted at the sorted alignment'` |
| X25 | 505 | `'THE EXACT EXCEPTIONAL SET IS {1}: outside the candidates the structure is the generic one, at the candidates the search decides'` | b= | {1} survives. The label also uses capitals for emphasis. | `'the exceptional set at the sorted alignment is {1}: outside the candidates the structure is the generic one, at the candidates the search decides'` |
| X26 | 517 | `'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates'` | b? | Both sides use the sorted alignment, so this is not a control on alignment. | `'the numeric search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates, both at the sorted alignment'` |
| X27 | 518 (comment), 538 | `# genuine deformations: each other class, …` / `'a genuine deformation inside each other class (one twist phase u5): unitary, off SIG, and found by the search in its own class'` → [(True, True, True)]\*8 | b? | The eight named classes. | `'a genuine deformation inside each of the eight other sorted-alignment classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` (comment: `# genuine deformations: each of the eight other sorted-alignment classes, …`) |
| X28 | 555 | `'the membership classifier commutes with three stabilizer elements (product, transposed, conjugating): the transported frozen class is the one structure found'` | b= | Survives (P). | `'… : the transported frozen class is the one structure found at the sorted alignment'` |
| X29 | 556–560 | the perturbed-index-map controls | c | Named maps only; a 2×8 statement. | — |
| X30 | 215 | `print("== 0. act 36's stabilizer of SIG in G_ext, replayed for the census ==")` | c | The stabilizer does not depend on the alignment. | — |
| X31 | 245–252 | the comment `# … A Dita structure (column blocks, row classes) is admitted at u iff finitely many monomial equations hold: the row proportionality on every block and the rank-one condition on the block ratios. …` | b? | "admitted iff" holds for a *given index map*. A structure given as (column blocks, row classes) needs the alignment too. | `# … A Dita structure (column blocks, row classes, and an alignment of the rows within classes) is admitted at u iff finitely many monomial equations hold: …` |
| X32 | 566 | `'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG the eighteen Diţă structures form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes is admitted only where u = 1, the candidate exceptional set of the monomial calculus has twenty points, and the exhaustive search at each of them finds only the frozen class away from u = 1: the exact exceptional set is {1}'` | b≠ | 18/9 and "eight other" are sorted counts; {1} coincides. | `'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG, with the rows of each class in sorted order, the eighteen Diţă structures found form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes found is admitted only where u = 1, the candidate exceptional set of the sorted-alignment monomial calculus has twenty points, and the search at the sorted alignment at each of them finds only the frozen class away from u = 1: the exceptional set at the sorted alignment is {1}'` |

## `verification/lean/dita_local_escape_probe.py` (act 38)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| L1 | 7–8 | `Its first part is act 37's probe head, verbatim: act 36's objects and exhaustive structure search, act 36's stabilizer, and act 37's monomial calculus.` | b? | Same as X1. | `… act 36's objects and structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment), act 36's stabilizer, and act 37's monomial calculus.` |
| L2 | 294 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| L3 | 407 | `print('== 2. class exclusions: the eighteen census structures, each admitted only at u = 1 ==')` | b≠ | The census has 20 structures. The checks cover the 18 named ones. | `print('== 2. class exclusions: the eighteen structures of the sorted-alignment census, each admitted only at u = 1 ==')` |
| L4 | 414 | `"act 37's census replayed: the nine column-form structures of SIG are exactly the frozen classes' index sets"` | b≠ | 10 column-form structures | `"act 37's sorted-alignment census replayed: the nine column-form structures of SIG at the sorted alignment are exactly the frozen classes' index sets"` |
| L5 | 415 | `'the row-form structures are the same index sets (SIG symmetric)'` | b? | This is the sorted row-form set. | `'the row-form structures at the sorted alignment are the same index sets (SIG symmetric)'` |
| L6 | 446 | `'each of the eighteen structures imposes non-identity conditions, all of the form u^k = 1 with trivial constant part'` | b? | The eighteen named structures. | `'each of the eighteen named structures imposes non-identity conditions, all of the form u^k = 1 with trivial constant part'` |
| L7 | 447, 448, 469, 470 | the per-structure counts, "admitted at u = 1 alone", "rational constants for seventeen of the eighteen", "the one non-rational witness" | c | These are computations over the named list `CLASSES` and carry no census claim once L3/L6 are scoped. | — |
| L8 | 473, 475, 547 | `'== 3. all-index exhaustion: at a generic u no index maps whatever pass the proportionality test =='`; `(0, 0)` at generic u; `'at generic u: no candidates at all (section 3), …'` | c | Proportionality does not depend on the alignment, so zero candidates means no structure at any index map. | — |
| L9 | 478 | `print('== 4. the exceptional set: every point at which any structure could appear, decided by the exhaustive search ==')` | b= | The first half survives: the candidate set comes from proportionality alone and is complete. The "exhaustive search" part is sorted. | `print('== 4. the exceptional set: every point at which any structure could appear, decided by the search at the sorted alignment ==')` |
| L10 | 499, 500 | `'the candidate exceptional set, exactly (forty points), both forms together'`; `'twenty of the candidates are Gaussian rational, …'` | c | `E_all` here is `E_cand` only (proportionality), which does not depend on the alignment. | — |
| L11 | 513 | `'at u = 1 the search returns the eighteen structures: (candidates, exact) by form and shape'` → (5, 4), (3, 2), (3, 3) | b≠ | 4x4 is (5, 5) per form. | `'at u = 1 the search at the sorted alignment returns eighteen structures: (candidates, exact) by form and shape'` |
| L12 | 514 | `'at u = -1 exactly one 2x8 structure per form is admitted: (candidates, exact) by form and shape'` → 4x4 (1, 0) | b≠ | Over all alignments, 4x4 is (1, 1) per form and there are four structures (verified above). | `'at u = -1 the search at the sorted alignment admits exactly one 2x8 structure per form: (candidates, exact) by form and shape'` |
| L13 | 517 | `'the two structures at u = -1: index maps outside the census, blocks by column parity in the column form'` | b≠ | There are four structures at −1. "Outside the census" survives, because every 2×8 structure of SIG is exact at every alignment. | `'the two 2x8 structures at u = -1: index maps outside the census, blocks by column parity in the column form'` |
| L14 | 518 | `'THE EXACT EXCEPTIONAL SET IS {1, -1}: the units at which some index maps admit a Diţă form of H(u) in some orientation'` | b= | {1, −1} survives. The label also uses capitals for emphasis. | `'the exceptional set at the sorted alignment is {1, -1}: the units at which a sorted-alignment index map admits a Diţă form of H(u) in some orientation'` |
| L15 | 519 | `'and the same up to diagonal equivalence: the units at which a proportionality candidate satisfies the relaxed rank-one condition'` | b= | Same as L14. | `'and the same up to diagonal equivalence: the units at which a proportionality candidate satisfies the relaxed rank-one condition at the sorted alignment'` |
| L16 | 520 | `'at u = 1 and u = -1 the relaxed structures are the strict ones'` | b? | The supplied table establishes strict = relaxed for act 40 only. | `'at u = 1 and u = -1 the relaxed structures at the sorted alignment are the strict ones'` |
| L17 | 523 | `print('== 5. sharpness: the structures at u = 1 and u = -1 are certified by exact reconstruction ==')` | b≠ | The two 4×4 structures at −1 and k5 at 1 are not reconstructed. | `print('== 5. sharpness: the nine census classes at u = 1 and the two 2x8 structures at u = -1 are certified by exact reconstruction ==')` |
| L18 | 538 | `'at u = -1: H(-1) is reconstructed exactly … at the column-form maps, and H(-1)^T at the row-form maps'` | c | Named maps (M_COL, M_ROW). | — |
| L19 | 539 | `'at u = -1 the numeric exhaustive search with factor unitarity finds exactly these two structures and nothing of the other shapes'` | b≠ | Over all alignments it also finds one 4×4 per form. | `'at u = -1 the numeric search at the sorted alignment, with factor unitarity, finds exactly these two structures and nothing of the other shapes'` |
| L20 | 540 | `'at u = 1: SIG is reconstructed exactly at every one of the nine census structures, and H(1) = SIG'` | b≠ | The census has ten classes. | `'at u = 1: SIG is reconstructed exactly at every one of the nine sorted-alignment census classes, and H(1) = SIG'` |
| L21 | 541 | `'the structures at u = -1 are not admitted at generic u nor at u = 1 (the exceptional structures are isolated)'` | b≠ | Only M_COL/M_ROW are checked. Component 1 (`any(… for x in [])`) is vacuous. | `'the two 2x8 structures at u = -1 are not admitted at generic u nor at u = 1 (they are isolated)'` |
| L22 | 546 | `'the set of units at which H(u) admits any Diţă structure, of any shape, index map or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}; every other unit is a realizable non-Diţă point'` | b= | {1, −1} survives, but this computation tested one index map per structure. | `'at the sorted alignment, the set of units at which H(u) admits a Diţă structure, of any shape or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}'` |
| L23 | 560 | `'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twenty Gaussian-rational candidates, both forms'` | b? | Both sides are sorted. | `'the numeric search (with factor unitarity) agrees with the symbolic one at all twenty Gaussian-rational candidates, both forms, both at the sorted alignment'` |
| L24 | 577 | `'a genuine deformation inside each of the nine classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` | b? | The nine named classes. | `'a genuine deformation inside each of the nine sorted-alignment census classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'` |
| L25 | 578–581 | `# … the transported matrices at u = -1 and u5 are searched directly, as act 37's control does: two structures at u = -1 (one per orientation), none at u5` | b≠ | Four at −1 | `# … searched directly at the sorted alignment, as act 37's control does: two structures at u = -1 (one per orientation), none at u5` |
| L26 | 618 | `'… the transported matrices admit exactly two structures at u = -1 and none at u5'` | b≠ | Four at −1 | `'the exponent matrix transported by three stabilizer elements (product, transposed, conjugating) is straight and admits no candidate at generic u; at the sorted alignment the transported matrices admit exactly two structures at u = -1 and none at u5'` |
| L27 | 628 | `'the three pieces and their pairwise sums are straight lines, each admitting some census structure identically; the triple admits none (interpretation: three Diţă directions whose sum is not Diţă)'` | b? | The lists cover the 18 named structures; k5 was not tested. "The triple admits none" survives absolutely because of L8. | `'the three pieces and their pairwise sums are straight lines, each admitting some structure of the sorted-alignment census identically; the triple admits none (interpretation: three Diţă directions whose sum is not Diţă)'` |
| L28 | 630 | `"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure (control of the classifier)"` | b= | Survives: an identically admitted structure would contradict {1} strict. | `"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure of the sorted-alignment census (control of the classifier)"` |
| L29 | 693 | `'the witness exponent matrix is tangent (it is straight) and lies in none of the eighteen subspaces, while the tangent space is the sum of all eighteen: the obstruction is nonlinear compatibility, not a missing tangent direction'` | b? | The value 80 survives. Whether E lies in k5's subspace is not computed. | `'the witness exponent matrix is tangent (it is straight) and lies in none of the eighteen named structures\' subspaces, while the tangent space is the sum of those eighteen: the obstruction is nonlinear compatibility, not a missing tangent direction'` |
| L30 | 692, 687, section 8 title | per-class tangent dimensions; the tangent-space rank | c | Named classes; alignment-free. | — |
| L31 | 699 | `'dita_local_escape_probe: OK -- … each of the eighteen census structures is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation'` | b≠ | "eighteen census structures" is a sorted count. {1, −1} coincides. | `'dita_local_escape_probe: OK -- along the arc H(u) = SIG o u^E through the certified stratum point, E = A + B + C the frozen exponent matrix: H(u) is a complex Hadamard matrix at every unit u; each of the eighteen structures of the sorted-alignment census is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the search at the sorted alignment at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: at the sorted alignment, for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape or orientation'` |

## `verification/lean/dita_torus_probe.py` (act 39)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| T1 | 5–6 | `Its first part is act 38's probe head, verbatim: act 36's objects and exhaustive structure search, act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.` | b? | Same as X1. The search is carried but not used by any act-39 check. | `… act 36's objects and structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment), act 36's stabilizer, …` |
| T2 | 291 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| T3 | all checks, l.212 section 0, OK line l.462–465 | realizability, joint level sets, subfamilies, countercontrol | c | No Diţă-structure claim. Act 39 states that it says nothing about Diţă loci. | — |

The act-39 edits are docstring-only, so this probe passes `probe_replay_check` against D41.

## `verification/lean/dita_torus_locus_probe.py` (act 40)

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| Y1 | 5–7 | `Its first part is act 38's probe head, verbatim: act 36's objects, exhaustive structure search and stabilizer, …` | b? | Same as X1. | `… act 36's objects, structure search (exhaustive over column blocks and row classes, each tested at the sorted alignment) and stabilizer, …` |
| Y2 | 287 | `"""the exhaustive Dita structure search (act 36's, section 2) …` | b? | Same as X2. | Same replacement as X2. |
| Y3 | 523 | `# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe` | b≠ | 18 versus 20 at SIG; four structures at −1 | `# ---- act 37's sorted-alignment census of SIG's Dita structures and act 38's two 2x8 exceptional index maps, verbatim from act 38's probe` |
| Y4 | 544–545, 636, 638, 639 | `"""every (orientation, shape, column blocks, row classes) whose within-class pairs have, on every block, a common point of their proportionality loci; a structure admitted anywhere on T^3 is among them …"""`; `'== 2. completeness: every Dita structure admitted anywhere is among the enumerated candidates =='`; 13/5/5 per orientation; 46 | c | The candidates come from proportionality only, which is alignment-free, and the set is complete. | — |
| Y5 | 642 | `print('== 3. locus exactness: each candidate strictly and up to diagonal equivalence ==')` | b? | Each candidate's locus is computed at one alignment. | `print('== 3. locus exactness: each candidate at the sorted alignment, strictly and up to diagonal equivalence ==')` |
| Y6 | 644 | `'the relaxed locus equals the strict locus for every candidate'` | b= | Survives (supplied). | `'the relaxed locus equals the strict locus for every candidate at the sorted alignment'` |
| Y7 | 645 | `'empty and nonempty strict loci'` → (16, 30) | b≠ | (3, 43) | `'empty and nonempty strict loci at the sorted alignment'` |
| Y8 | 646 | `'every nonempty locus is cut out by coordinate characters u_k = +-1 alone'` → True | b≠ | **False** over all alignments: four loci are non-coordinate points inside faces. This is the one value that inverts. | `'every nonempty sorted-alignment locus is cut out by coordinate characters u_k = +-1 alone'` |
| Y9 | 649 | `print('== 4. union reduction: the union of the loci is five coordinate 2-subtori ==')` | b= | The five-face union survives. | `print('== 4. union reduction: the union of the sorted-alignment loci is five coordinate 2-subtori ==')` |
| Y10 | 651, 652, 658 | `'the maximal loci'`; `'every nonempty locus lies in one of them, and each of them is itself a locus'`; the diagonal restriction | c | The maximal loci and the containments are unchanged: the four extra loci are points inside faces, and each face is still a locus. | — |
| Y11 | 663 | `'at (1, 1, 1): eighteen structures, exactly act 37 census in both orientations'` → (18, True) | b≠ | 20 | `'at (1, 1, 1) at the sorted alignment: eighteen structures, exactly act 37 census in both orientations'` |
| Y12 | 664 | `'at (-1, -1, -1): one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'` | b≠ | 4 | `'at (-1, -1, -1) at the sorted alignment: one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'` |
| Y13 | 666, 679, 682, 727, 728 | the absent face u2 = −1, the +1 faces as act 39 subfamilies, the kernel-layer title, the whole-face factorizations | c | The union is unchanged; these are named structures. | — |
| Y14 | 704 | `'for each of the twenty named structures (the census in both orientations, M_COL, M_ROW), single four-position witnesses …'` | b? | The named list is correct, but "the census" means the sorted census, and "twenty" collides with the all-alignment census count of 20. | `'for each of the twenty named structures (the sorted-alignment census in both orientations, M_COL, M_ROW), single four-position witnesses …'` |
| Y15 | 731 | `print('== 7. an independent control: act 36\'s exhaustive structure search, with factor unitarity, at exact points ==')` | b? | This control is not independent of the loci with respect to alignment, since both use `rows[b][a]`. | `print('== 7. a control: act 36\'s structure search at the sorted alignment, with factor unitarity, at exact points ==')` |
| Y16 | 748 | `'at seventeen exact points (two generic, the five faces, two absent directions, three lines, five special points) the search finds exactly the predicted structures'` → counts [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4] | b≠ | At least (1,1,1) → 20 and (−1,−1,−1) → 4. The other counts are not supplied. | `'at seventeen exact points (…) the search at the sorted alignment finds exactly the predicted sorted-alignment structures'` |
| Y17 | 755 | `'the classifier applied to the perturbed pieces: candidates, nonempty loci and the union, which collapses to the one face where C drops out'` → (30, 23, ['u3 = 1'], True) | b? | 23 is a sorted count. The all-alignment count is not supplied. | `'the classifier at the sorted alignment applied to the perturbed pieces: candidates, nonempty loci and the union, which collapses to the one face where C drops out'` |
| Y18 | 761–765 | `'dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the 30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1'` | b≠ | 30 → 43. The five-face conclusion coincides. | `'dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted anywhere is among 46 enumerated candidates; their strict and relaxed loci at the sorted alignment are computed exactly and agree; the union of the 30 nonempty sorted-alignment loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so at the sorted alignment H3 admits a Dita structure of some shape and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1'` |
| Y19 | 208 | `print("== 0. act 36's stabilizer of SIG in G_ext, replayed for the census ==")` | c | The stabilizer does not depend on the alignment. | — |

***

## Lean modules — `verification/lean-mathlib/OIBridge/` (module-header comments only)

| id | file:line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| LH1 | `DitaHierarchy.lean:6–13` | `…an outer factor on α, inner factors on β, a twist, and any bijections of α × β with the product carrier for rows and for columns — realizable for flat unitary factors and unit twists; …` | c | A kernel statement over any bijections. | — |
| LH2 | `DitaHierarchy.lean:14–16` | ``The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either orientation under any relabelling: the `4 × 4` hierarchy is locally insufficient at the stratum, and the first escaping family belongs to the `2 × 8` construction.`` | a\* | The content survives (supplied), but act 36's layer tested one alignment. | Unchanged once the all-alignment search is a probe of the layer. Otherwise: ``Exact computation over every index map shows that `P` admits no `4 × 4` Diţă factorization of either orientation: …`` (the rest unchanged, citing that computation) |
| LA1 | `DitaArcExclusivity.lean:11–13` | ``and, for each of the eight other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two `2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — that a Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.`` | a | "Complete census" is false: there are nine other classes (five 4×4). | ``and, for each of eight named other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two `2 × 8` — that a Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.`` |
| LA2 | `DitaArcExclusivity.lean:13–15` | ``The exact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps whatever admit a Diţă form of `Pu u` but the frozen class's.`` | a\* | The content survives ({1} strict). Act 37's probe tested one alignment. | ``Exact computation over every index map carries the exhaustive complement: at every unit `u ≠ 1`, no index maps whatever admit a Diţă form of `Pu u` but the frozen class's.`` |
| LE1 | `DitaLocalEscape.lean:10–14` | ``that for each of the nine Diţă factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a realizable matrix admitting none of the eighteen forms.`` | a | "Complete census" is false: there are ten classes. "The eighteen forms" then reads as all forms; the kernel corollary is about the named ones. | ``that for each of nine named Diţă factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8` — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a realizable matrix admitting none of their eighteen forms.`` |
| LE2 | `DitaLocalEscape.lean:14–15` | ``The exact-computation layer carries the exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,`` | a\* | The content survives ({1, −1}). | ``Exact computation over every index map carries the exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,`` |
| LE3 | `DitaLocalEscape.lean:16` | ``and at `u = −1` exactly one `2 × 8` structure per orientation does.`` | a | False: at u = −1 there is one 2×8 and one 4×4 structure per orientation (four in all; verified above). | ``and at `u = −1` exactly one `2 × 8` and one `4 × 4` structure per orientation do.`` |
| LT1 | `DitaTorus.lean:12–13` | ``It says nothing about which points of the torus admit a Diţă structure.`` | c | No dependency. | — |
| LL1 | `DitaTorusLocus.lean:11–13` | ``For each of twenty named index maps — act 37's nine classes in both orientations and act 38's two maps `M_COL` and `M_ROW` — a strict Diţă form of `H3` at that map forces the named coordinate equations.`` | c | A kernel statement over named maps. "Act 37's nine classes" is a reference to named classes. | — (optional: "act 37's nine named classes") |
| LL2 | `DitaTorusLocus.lean:13–15` | ``The module does not state that the five faces exhaust the points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.`` | a\* | The content survives (five faces). The round's probe tested one alignment. | ``… that converse, over every shape, index map and orientation and up to diagonal equivalence, is certified by exact computation over every index map, not by the kernel.`` |
| LK | `OIBridge.lean:220–225` | `import OIBridge.Dita…` | c | Import lines only. | — |

## `verification/lean-manuscript-census.json` (the five families; "name" and "note")

| id | line | exact text | kind | all-alignment status / reason | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| J1 | 1212 (A36 name) | `the Diţă factorization hierarchy at the product-embedded stratum — Diţă's construction over any factorization of the sixteen-point carrier realizable in both forms, its 2 × 8 and 8 × 2 instances, an exact 2 × 8 family through the certified rational stratum point, and a named point of it off the stratum (act 36, Track B)` | c | Kernel content only. | — |
| J2 | 1218 (A36 note) | `the exhaustive block-structure searches, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding the known factorizations of the stratum point;` | a\* | The point values survive. The searches are not exhaustive over index maps, and "the known factorizations" are 4 of 5 4×4 per orientation. | `the block-structure searches with the rows of each class in sorted order, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding four of the five 4 × 4 factorizations of the stratum point in each orientation;` |
| J3 | 1218 | `the 492 4 × 4 Diţă hulls through the stratum point spanning its 49-dimensional defect at first order;` | b? | Being recounted; the span survives. | `the 492 4 × 4 Diţă hulls through the stratum point at the sorted alignment, spanning its 49-dimensional defect at first order;` |
| J4 | 1218 | `These are exact arithmetic replayed, not kernel-certified; by them the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.` | a\* | The conclusion survives (P admits no 4×4 at any index map), but a one-alignment search does not reach it. | `These are exact arithmetic replayed, not kernel-certified; by them, and by exact computation over every index map at the named point, the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.` |
| J5 | 1221 (A37 name) | `… and each of the eight other factorization classes of the stratum point admitted only at the base point (act 37, Track B)` | a | "The eight other" implies completeness; there are nine. | `… and each of eight named other factorization classes of the stratum point admitted only at the base point (act 37, Track B)` |
| J6 | 1227 (A37 note) | `and for each of the eight other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Pu u …` | a | "Complete census" is false. | `and for each of eight named other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8 — a Diţă form of Pu u …` |
| J7 | 1227 | `the census of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;` | b≠ | 20 in 10 | `the census, at the sorted alignment, of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;` |
| J8 | 1227 | `the generic arc point admitting exactly the frozen class; each other class obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of twenty exactly named points ζ z^s w^t;` | b= | The generic statement survives. "Each other class" means the eight named. The candidate set is sorted-derived. | `the generic arc point admitting exactly the frozen class; each of the eight named other classes obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of the sorted-alignment calculus, twenty exactly named points ζ z^s w^t;` |
| J9 | 1227 | `and the exhaustive search at each of them admitting only the frozen class away from u = 1, so that the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.` | a\* | The content survives ({1} strict). The cited probe tested one alignment. | `and the search at the sorted alignment at each of them admitting only the frozen class away from u = 1; by exact computation over every index map the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.` |
| J10 | 1230 (A38 name) | `… each of the nine factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of the eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)` | a | "The nine" implies completeness; there are ten. | `… each of nine named factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of their eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)` |
| J11 | 1236 (A38 note) | `for each of the nine Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Hu u …` | a | "Complete census" is false. | `for each of nine named Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8 — a Diţă form of Hu u …` |
| J12 | 1236 | `the eighteen exclusions and their forced witness identities; that at a generic u no index maps whatever pass the proportionality test in either orientation; the candidate exceptional set of forty exactly named points ζ z^s w^t` | c | Named exclusions. Proportionality and the candidate set do not depend on the alignment. | — |
| J13 | 1236 | `and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;` | a | "The two structures at u = −1" is false: there are four. The {1, −1} content survives but is cited to a one-alignment search (a\*). | `and the search at the sorted alignment at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two 2 × 8 structures at u = −1 certified by exact reconstruction; by exact computation over every index map the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;` |
| J14 | 1236 | `and the tangent space at SIG, of dimension 80, spanned by the eighteen first-order Diţă subspaces, so that the escape is a nonlinear compatibility obstruction.` | b= | The span (80) survives. "The eighteen" reads as all structures. | `and the tangent space at SIG, of dimension 80, spanned by the first-order subspaces of the eighteen named structures, so that the escape is a nonlinear compatibility obstruction.` |
| J15 | 1236 | `and every neighbourhood of SIG contains a realizable matrix admitting none of the eighteen forms (a38_c_local_escape)` | c | A kernel corollary over the named forms. It reads correctly once J11 names the classes. | — |
| J16 | 1239, 1245 (A39) | name; `Nothing is claimed about which points of the three-torus admit a Diţă structure, about the exponent matrices with entries in {0, 1}, about the minimality of support 48, …` | c | No dependency. | — |
| J17 | 1248 (A40 name) | `… are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation (act 40, Track B)` | c | The five faces survive. The name says "exact computation" without naming the round's probe. It is supported once the all-alignment computation exists. | — |
| J18 | 1254 (A40 note) | `The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by the round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard: 46 candidate structures contain every structure admitted anywhere, their strict and relaxed loci coincide, and the union of the 30 nonempty loci is exactly the five faces.` | a\* | The content survives. The round's probe is one-alignment, and "30 nonempty loci" is sorted (43 over all alignments). | `The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by exact computation over every index map; the round's probe verification/lean/dita_torus_locus_probe.py, run in its own shard, shows that 46 candidate structures contain every structure admitted anywhere and computes each candidate's strict and relaxed loci at the sorted alignment, which coincide and whose 30 nonempty members have the five faces as union.` |
| J19 | 1254 | `and at twenty named index maps — act 37's nine classes in both orientations and act 38's M_COL and M_ROW — a strict Diţă form of H3 forces the named coordinate equations` | c | Named maps. | — |

Families for acts 36–40 carry `"manuscript": []`, so no manuscript anchor depends on these notes.

## `verification/ROADMAP.md`

### P0 cell (line 63; each segment verified verbatim against its act's `preregistration.md`)

| id | round | exact text | kind | status | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| R1 | A36 | ``At the product configuration, Diţă's construction over every factorization of the sixteen-point carrier, in the column and the row form, is realizable for every choice of flat unitary factors, unit twist phases and row and column bijections; an exact one-parameter family of `2 × 8` column Diţă matrices runs through the certified rational stratum point, every member realizable, and its named point at `u₆₀ = (60+i)/(60−i)` is a realizable class off the stratum;`` | d | Kernel content survives. | No change. |
| R2 | A36 | ``and, by the round's exact-computation probe, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;`` | d | The content survives (supplied). The attribution is to a one-alignment probe. | ``and, by exact computation over every index map, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;`` |
| R3 | A37 | ``and, by the kernel for the eight other factorization classes of the stratum point and by the round's exact-computation probe for every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;`` | d | "The eight other" implies completeness (there are nine). The attribution is to a one-alignment probe. The conclusion survives. | ``and, by the kernel for eight named other factorization classes of the stratum point and by exact computation over every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;`` |
| R4 | A38 | ``each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:`` | d | "The nine" implies completeness (there are ten). The attribution is to a one-alignment probe. {1, −1} survives. | ``each of nine named Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by exact computation over every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:`` |
| R5 | A38 | `The tangent space at the stratum point is spanned by the eighteen Diţă tangent subspaces, so the escape is a nonlinear compatibility obstruction and not a missing tangent direction.` | d | The span survives. "The eighteen" reads as all structures. | `The tangent space at the stratum point is spanned by the Diţă tangent subspaces of the eighteen named structures, so the escape is a nonlinear compatibility obstruction and not a missing tangent direction.` |
| R6 | A39 | ``For act 38's three exponent pieces `A`, `B`, `C`, the three-parameter family … is realizable at every point of the three-torus, by the kernel, …; Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, …`` | d | No dependency. | No change. |
| R7 | A40 | ``For act 39's three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, the points of the three-torus at which it admits a Diţă structure, of any shape, index map and orientation and up to diagonal equivalence, are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.`` | d | The five faces survive. The attribution is to a one-alignment probe. | ``… and the exclusions at twenty named index maps by the kernel, and the converse over every index map by exact computation.`` |

The standing clauses after each sentence ("Nothing here classifies …", "The census of exponent matrices …
support 48 stay open …") do not depend on the census.

### Future-direction sections

| id | line | exact text | kind | status | proposed replacement |
| --- | --- | --- | --- | --- | --- |
| R9 | 1195–1196 | `and for the classification of each against the eighteen Diţă structures of the point: which lie identically in some structure and which in none.` | a | The point has twenty structures in ten classes. | `and for the classification of each against the Diţă structures of the point: which lie identically in some structure and which in none.` |
| R10 | 1210–1211 | `Whether a straight line through the certified stratum point that lies identically in none of the eighteen Diţă structures can have smaller support, …` | a | Same as R9. | `Whether a straight line through the certified stratum point that lies identically in none of the Diţă structures of the point can have smaller support, …` |
| R11 | 1224–1226 | `` Act 38's probe records, as a control of its classifier and not as a theorem, that `A`, `B`, `C` and their pairwise sums are straight lines each lying identically in some Diţă structure of the point while `A + B + C` lies in none.`` | c | "Lies in some" holds via named structures. "A + B + C lies in none" holds at every index map, because at generic u there are no proportionality candidates (L8). | — |
| R12 | 1215 | `which does not presuppose the full census` | c | This refers to the straight-line census. | — |

## Other in-scope files

| file | occurrence | kind | reason |
| --- | --- | --- | --- |
| `.github/workflows/verify.yml:213–269` | job names `Numerical probes / A36 hierarchy`, `… / A38 escape`, `… / A40 locus`; step `A40 Dita-locus probe`; no comments | c | Neutral names with no census claim. |
| `verification/README.md`, `tools/`, `papers/`, `book/` | no Diţă content ("eighteen" hits concern seals, contracts and primes) | — | Not counted. |

***

## Notes for the correction round

- Each **b≠ / b= / b?** probe row is a change to a label, title, docstring or OK line. No check *value*
  changes, so each computation remains a sorted-alignment regression control. The exception is Y8, whose
  value is correct only as a sorted value. None of these label changes is replay-neutral under
  `tools/probe_replay_check.py` as written (see the replay section).
- The **a\*** rows all cite "the round's exact-computation probe" or "the exhaustive search" for a
  conclusion that holds over every index map. Each needs the all-alignment search to exist as a cited
  artifact. The replacements name it generically ("exact computation over every index map") and must be
  tied to that probe when it lands. Without it, the only supported wording is the sorted scope, and
  LH2, R2 and J4 would then lose the "locally insufficient" conclusion.
- **LE3 and J13** carry the only outright false statement of a count outside the probes (two structures
  at u = −1, versus four). **LA1, LE1, J5, J6, J10, J11, R3, R4, R9 and R10** carry "complete census",
  "the eight / nine classes" or "the eighteen structures" as a completeness claim.
- The two 4×4 structures at u = −1 on act 38's arc have a partition that is none of SIG's five 4×4
  candidates. They are new classes, not k5. k5 is not a proportionality candidate at u = −1.


***

## Appendix B — the edit ledger, FROZEN

Each entry is a splice of `D`'s file at `path`: the text `old`, which occurs exactly once there, is replaced by the rendering of `new`. `controls.py` carries the same ledger as data and its self-test checks that every `old` and `new` below is carried verbatim here.

### `H12` — `verification/lean/dita_hierarchy_probe.py` — docstring

module docstring: scope of the searches and the pointer to act 41's probes (new row; the census counts the docstring as c)

```text
Its first part is act 35's probe head, verbatim, for the shared objects.

```

```text
Its first part is act 35's probe head, verbatim, for the shared objects.
Its Diţă searches test each partition structure at the sorted alignment (the rows of each row class in sorted
order); the censuses over every index map are act 41's probes verification/lean/dita_index_map_probe.py,
verification/lean/dita_index_map_independent.py and
verification/lean/dita_index_map_hulls.py.

```

### `H1` — `verification/lean/dita_hierarchy_probe.py` — string

census H1: section title re-scoped to the sorted alignment

```text
print('== 2. Diţă factorizations by exhaustive search over block structures ==')
```

```text
print('== 2. Diţă factorizations by exhaustive search over block structures, the rows of each row class in sorted order ==')
```

### `H2` — `verification/lean/dita_hierarchy_probe.py` — string

census H2: check label re-scoped

```text
at %s: (candidates, exact factorizations)'
```

```text
at %s: (candidates, exact at the sorted alignment)'
```

### `H4` — `verification/lean/dita_hierarchy_probe.py` — string

census H4: check label re-scoped; SIG has five admitted 4x4 partition structures per orientation under every index map

```text
at SIG = Pu(1): (candidates, exact factorizations) (control)'
```

```text
at SIG = Pu(1): (candidates, exact at the sorted alignment) (control)'
```

### `H5` — `verification/lean/dita_hierarchy_probe.py` — string

census H5: section title re-scoped

```text
print('== 4. every 4x4 Diţă hull through SIG: orientations,
```

```text
print('== 4. the 4x4 Diţă hulls through SIG at the sorted alignment: orientations,
```

### `H6` — `verification/lean/dita_hierarchy_probe.py` — string

census H6: label re-scoped; the value counts parametrizations (Hazard 7)

```text
'4x4 Diţă hulls through SIG (orientations × circle choices)'
```

```text
'4x4 Diţă hull parametrizations through SIG at the sorted alignment (orientations × circle choices)'
```

### `H7` — `verification/lean/dita_hierarchy_probe.py` — string

census H7: label re-scoped

```text
'every hull tangent in ker DF and D²F vanishing exactly on every hull (failures)'
```

```text
'every sorted-alignment hull tangent in ker DF and D²F vanishing exactly on every sorted-alignment hull (failures)'
```

### `H8` — `verification/lean/dita_hierarchy_probe.py` — string

census H8: label re-scoped

```text
'every hull tangent has dimension 14 mod gauge'
```

```text
'every sorted-alignment hull tangent has dimension 14 mod gauge'
```

### `H9` — `verification/lean/dita_hierarchy_probe.py` — string

census H9: label re-scoped

```text
'the span of all 4x4 hull tangents mod gauge equals the defect'
```

```text
'the span of the sorted-alignment 4x4 hull tangents mod gauge equals the defect'
```

### `H10` — `verification/lean/dita_hierarchy_probe.py` — string

census H10: success text re-scoped (tail unchanged)

```text
print('dita_hierarchy_probe: OK -- P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has its 4x4 factorizations; W is an exact straight line at SIG; the 492 4x4 hulls through SIG span
```

```text
print('dita_hierarchy_probe: OK -- with the rows of each row class in sorted order, P = SIG∘u60^W and Pu(u5), both of defect 37, admit no 4x4 and no 8x2 Diţă factorization of either orientation at any block structure and exactly one 2x8 per orientation, while SIG = Pu(1) has four exact 4x4 factorizations of five candidates per orientation; W is an exact straight line at SIG; the 492 sorted-alignment 4x4 hull parametrizations through SIG span
```

### `X1` — `verification/lean/dita_arc_exclusivity_probe.py` — docstring

census X1: module docstring re-scoped, with the pointer to act 41's probes

```text
act 36's exhaustive structure search.

```

```text
act 36's structure search, exhaustive over column blocks and row classes and testing each partition structure at the
sorted alignment (the rows of each row class in sorted order). The censuses over every index map are act 41's probes
verification/lean/dita_index_map_probe.py and verification/lean/dita_index_map_independent.py.

```

### `X31` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X31: comment; admission is decided for a given alignment (comment only, invisible to ast)

```text
# structure (column blocks, row classes) is admitted at u iff
```

```text
# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at
# u iff
```

### `X2` — `verification/lean/dita_arc_exclusivity_probe.py` — docstring

census X2: search docstring re-scoped

```text
"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials:
```

```text
"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the
    rank-one condition at the sorted alignment, on a matrix of monomials:
```

### `X3` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X3: section title re-scoped; act 37's classes are partition orbits (Hazard 10)

```text
print('== 1. the census: every Diţă structure of the stratum point, and its classes modulo the stabilizer ==')
```

```text
print('== 1. the census at the sorted alignment: the Diţă partition structures of the stratum point with the rows of each row class in sorted order, and their partition orbits under the stabilizer ==')
```

### `X4` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X4: label re-scoped

```text
'exact structures of SIG by shape and form: 4x4, 8x2, 2x8, each column and row'
```

```text
'exact partition structures of SIG at the sorted alignment by shape and form: 4x4, 8x2, 2x8, each column and row'
```

### `X5` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X5: label re-scoped

```text
'every structure reconstructs SIG exactly from its factors, with trivial twist'
```

```text
'every sorted-alignment partition structure reconstructs SIG exactly from its factors, with trivial twist'
```

### `X6` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X6: label re-scoped

```text
'the column-form and row-form structures coincide as index sets (SIG symmetric)'
```

```text
'the column-form and row-form sorted-alignment partition structures coincide as index sets (SIG symmetric)'
```

### `X7` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X7: label re-scoped

```text
'the stabilizer (order 1024, with transposition) permutes the 18 structures; orbit count and sizes'
```

```text
'the stabilizer (order 1024, with transposition) permutes the 18 partition structures admitted at the sorted alignment; partition-orbit count and sizes'
```

### `X8` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X8: label re-scoped

```text
'each orbit pairs a structure with its own transpose and identifies nothing else'
```

```text
'each partition orbit of the sorted-alignment restriction pairs a partition structure with its own transpose and identifies nothing else'
```

### `X10` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X10: label re-scoped; the eight are partition orbits of the sorted-alignment restriction

```text
'the other classes: four 4x4, two 8x2, two 2x8'
```

```text
'the other partition orbits of the sorted-alignment restriction: four 4x4, two 8x2, two 2x8'
```

### `X11` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X11: label re-scoped

```text
'P admits exactly the frozen class (column form; the row form is the same by symmetry)'
```

```text
'at the sorted alignment P admits exactly the frozen 2x8 partition structure (column form; the row form is the same by symmetry)'
```

### `X12` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X12: label re-scoped

```text
'Pu(u5) admits exactly the frozen class'
```

```text
'at the sorted alignment Pu(u5) admits exactly the frozen 2x8 partition structure'
```

### `X13` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X13: section title re-scoped

```text
print('== 3. the generic arc point, and the obstruction monomial of each other class ==')
```

```text
print('== 3. the generic arc point, and the obstruction monomial of each other named index map of the sorted-alignment census ==')
```

### `X14` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X14: label re-scoped

```text
'structures at a generic u (u a free symbol): (candidates, exact) by shape'
```

```text
'partition structures at a generic u (u a free symbol): (candidates, exact at the sorted alignment) by shape'
```

### `X15` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X15: label re-scoped

```text
'the one exact generic structure is the frozen 2x8 class'
```

```text
'the one exact generic partition structure at the sorted alignment is the frozen 2x8 partition structure'
```

### `X16` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X16: label names the eight index maps tested

```text
'each other class imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'
```

```text
'each of the eight other named index maps of the sorted-alignment census imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}'
```

### `X17` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X17: label names the eight index maps tested

```text
'the kernel witness identity of each other class is forced by its Diţă form,
```

```text
'the kernel witness identity of each of the eight other named index maps is forced by its Diţă form,
```

### `X18` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X18: section title re-scoped

```text
print('== 4. the candidate exceptional set: every point where an extra proportionality or the rank-one condition of a generic candidate appears ==')
```

```text
print('== 4. the candidate exceptional set: every point where an extra proportionality, or the sorted-alignment rank-one condition of a generic candidate, appears ==')
```

### `X19` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X19: label re-scoped

```text
'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at u = 1 only'
```

```text
'the generic 4x4 and 8x2 candidates satisfy the rank-one condition at the sorted alignment at u = 1 only'
```

### `X20` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X20: label re-scoped

```text
'the candidate exceptional set, exactly (twenty points)'
```

```text
'the candidate exceptional set of the sorted-alignment calculus, exactly (twenty points)'
```

### `X21` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X21: section title re-scoped

```text
print('== 5. the exhaustive search at every candidate point: the exact exceptional set ==')
```

```text
print('== 5. the search at the sorted alignment at every candidate point: the exceptional set at the sorted alignment ==')
```

### `X22` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X22: label re-scoped

```text
'at u = 1 the search returns the eighteen structures: (candidates, exact) by shape'
```

```text
'at u = 1 the search at the sorted alignment returns eighteen partition structures: (candidates, exact) by shape'
```

### `X23` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X23: label re-scoped

```text
'at u = -1 the proportionality candidates are those of u = 1, but only the frozen class is exact'
```

```text
'at u = -1 the proportionality candidates are those of u = 1, but at the sorted alignment only the frozen 2x8 partition structure is exact'
```

### `X24` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X24: label re-scoped

```text
'at every candidate point other than u = 1, exactly the frozen class is admitted'
```

```text
'at every candidate point other than u = 1, exactly the frozen 2x8 partition structure is admitted at the sorted alignment'
```

### `X25` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X25: label re-scoped, capitals removed

```text
'THE EXACT EXCEPTIONAL SET IS {1}: outside the candidates the structure is the generic one, at the candidates the search decides'
```

```text
'the exceptional set at the sorted alignment is {1}: outside the candidates the partition structure is the generic one, at the candidates the search decides'
```

### `X26` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X26: label re-scoped; both sides share the alignment rule

```text
'the numeric exhaustive search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates'
```

```text
'the numeric search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates, both at the sorted alignment'
```

### `X27c` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X27 (comment): names the eight index maps

```text
# genuine deformations: each other class, with one twist phase moved off 1, is a point of that class's hull off SIG
```

```text
# genuine deformations: each of the eight other named index maps, with one twist phase moved off 1, gives a point of its hull off SIG
```

### `X27` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X27: label names the eight index maps

```text
'a genuine deformation inside each other class (one twist phase u5): unitary, off SIG, and found by the search in its own class'
```

```text
'a genuine deformation at each of the eight other named index maps (one twist phase u5): unitary, off SIG, and found by the search at the sorted alignment at its own partition structure'
```

### `X28` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X28: label re-scoped

```text
the transported frozen class is the one structure found'
```

```text
the transported frozen 2x8 partition structure is the one found at the sorted alignment'
```

### `X32` — `verification/lean/dita_arc_exclusivity_probe.py` — string

census X32: success text re-scoped

```text
'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG the eighteen Diţă structures form nine classes modulo the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 class persists identically, each of the eight other classes is admitted only where u = 1, the candidate exceptional set of the monomial calculus has twenty points, and the exhaustive search at each of them finds only the frozen class away from u = 1: the exact exceptional set is {1}'
```

```text
'dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG, with the rows of each row class in sorted order, the eighteen Diţă partition structures found form nine partition orbits under the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 partition structure persists identically, each of the eight other named index maps is admitted only where u = 1, the candidate exceptional set of the sorted-alignment monomial calculus has twenty points, and the search at the sorted alignment at each of them finds only the frozen 2x8 partition structure away from u = 1: the exceptional set at the sorted alignment is {1}'
```

### `L1` — `verification/lean/dita_local_escape_probe.py` — docstring

census L1: module docstring re-scoped, with the pointer to act 41's probes

```text
act 36's objects and exhaustive
structure search, act 36's stabilizer, and act 37's monomial calculus.

```

```text
act 36's objects and structure search
(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment), act 36's
stabilizer, and act 37's monomial calculus. The censuses over every index map are act 41's probes
verification/lean/dita_index_map_probe.py and verification/lean/dita_index_map_independent.py.

```

### `L32` — `verification/lean/dita_local_escape_probe.py` — string

mirror of census X31 in the verbatim head (comment only, invisible to ast)

```text
# structure (column blocks, row classes) is admitted at u iff
```

```text
# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at
# u iff
```

### `L2` — `verification/lean/dita_local_escape_probe.py` — docstring

census L2: search docstring re-scoped

```text
"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials:
```

```text
"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the
    rank-one condition at the sorted alignment, on a matrix of monomials:
```

### `L3` — `verification/lean/dita_local_escape_probe.py` — string

census L3: section title re-scoped

```text
print('== 2. class exclusions: the eighteen census structures, each admitted only at u = 1 ==')
```

```text
print('== 2. named exclusions: the eighteen named index maps of the sorted-alignment census, each admitted only at u = 1 ==')
```

### `L4` — `verification/lean/dita_local_escape_probe.py` — string

census L4: label re-scoped

```text
"act 37's census replayed: the nine column-form structures of SIG are exactly the frozen classes' index sets"
```

```text
"act 37's census replayed at the sorted alignment: the nine column-form partition structures of SIG admitted there are exactly the index sets of act 37's nine named index maps"
```

### `L5` — `verification/lean/dita_local_escape_probe.py` — string

census L5: label re-scoped

```text
'the row-form structures are the same index sets (SIG symmetric)'
```

```text
'the row-form partition structures at the sorted alignment are the same index sets (SIG symmetric)'
```

### `L6` — `verification/lean/dita_local_escape_probe.py` — string

census L6: label names the eighteen index maps

```text
'each of the eighteen structures imposes non-identity conditions,
```

```text
'each of the eighteen named index maps imposes non-identity conditions,
```

### `L9` — `verification/lean/dita_local_escape_probe.py` — string

census L9: section title re-scoped

```text
print('== 4. the exceptional set: every point at which any structure could appear, decided by the exhaustive search ==')
```

```text
print('== 4. the exceptional set: every point at which any partition structure could appear, decided by the search at the sorted alignment ==')
```

### `L11` — `verification/lean/dita_local_escape_probe.py` — string

census L11: label re-scoped

```text
'at u = 1 the search returns the eighteen structures: (candidates, exact) by form and shape'
```

```text
'at u = 1 the search at the sorted alignment returns eighteen partition structures: (candidates, exact) by form and shape'
```

### `L12` — `verification/lean/dita_local_escape_probe.py` — string

census L12: label re-scoped

```text
'at u = -1 exactly one 2x8 structure per form is admitted: (candidates, exact) by form and shape'
```

```text
'at u = -1 the search at the sorted alignment admits exactly one 2x8 partition structure per form: (candidates, exact) by form and shape'
```

### `L13` — `verification/lean/dita_local_escape_probe.py` — string

census L13: label re-scoped

```text
'the two structures at u = -1: index maps outside the census, blocks by column parity in the column form'
```

```text
'the two 2x8 partition structures found at u = -1 at the sorted alignment: index maps outside the sorted-alignment census of SIG, blocks by column parity in the column form'
```

### `L14` — `verification/lean/dita_local_escape_probe.py` — string

census L14: label re-scoped, capitals removed

```text
'THE EXACT EXCEPTIONAL SET IS {1, -1}: the units at which some index maps admit a Diţă form of H(u) in some orientation'
```

```text
'the exceptional set at the sorted alignment is {1, -1}: the units at which a sorted-alignment index map admits a Diţă form of H(u) in some orientation'
```

### `L15` — `verification/lean/dita_local_escape_probe.py` — string

census L15: label re-scoped

```text
satisfies the relaxed rank-one condition'
```

```text
satisfies the relaxed rank-one condition at the sorted alignment'
```

### `L16` — `verification/lean/dita_local_escape_probe.py` — string

census L16: label re-scoped

```text
'at u = 1 and u = -1 the relaxed structures are the strict ones'
```

```text
'at u = 1 and u = -1 the relaxed partition structures at the sorted alignment are the strict ones'
```

### `L17` — `verification/lean/dita_local_escape_probe.py` — string

census L17: section title names what is reconstructed

```text
print('== 5. sharpness: the structures at u = 1 and u = -1 are certified by exact reconstruction ==')
```

```text
print('== 5. sharpness: the nine named index maps of the sorted-alignment census at u = 1 and the two 2x8 index maps M_COL, M_ROW at u = -1 are certified by exact reconstruction ==')
```

### `L19` — `verification/lean/dita_local_escape_probe.py` — string

census L19: label re-scoped

```text
'at u = -1 the numeric exhaustive search with factor unitarity finds exactly these two structures and nothing of the other shapes'
```

```text
'at u = -1 the numeric search at the sorted alignment, with factor unitarity, finds exactly these two partition structures and nothing of the other shapes'
```

### `L20` — `verification/lean/dita_local_escape_probe.py` — string

census L20: label re-scoped

```text
'at u = 1: SIG is reconstructed exactly at every one of the nine census structures, and H(1) = SIG'
```

```text
'at u = 1: SIG is reconstructed exactly at every one of the nine named index maps of the sorted-alignment census, and H(1) = SIG'
```

### `L21` — `verification/lean/dita_local_escape_probe.py` — bugfix

census L21: label re-scoped; the vacuous first component any(... for x in []) and its expected False removed (owner decision)

```text
check('the structures at u = -1 are not admitted at generic u nor at u = 1 (the exceptional structures are isolated)', (any(x[2] == GEN_ONE for x in []) , all(x[2] == GEN_ONE for x in conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)), all(x[2] == GEN_ONE for x in conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)), admitted_points(conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)) == frozenset([PT_MINUS]), admitted_points(conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)) == frozenset([PT_MINUS])), (False, False, False, True, True))
```

```text
check('M_COL and M_ROW, the two 2x8 index maps at u = -1, are admitted neither at generic u nor at u = 1 (they are isolated)', (all(x[2] == GEN_ONE for x in conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)), all(x[2] == GEN_ONE for x in conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)), admitted_points(conditions_E(EE, 2, 8, M_COL[0], M_COL[1], False)) == frozenset([PT_MINUS]), admitted_points(conditions_E(ET, 2, 8, M_ROW[0], M_ROW[1], False)) == frozenset([PT_MINUS])), (False, False, True, True))
```

### `L22` — `verification/lean/dita_local_escape_probe.py` — string

census L22: label re-scoped

```text
'the set of units at which H(u) admits any Diţă structure, of any shape, index map or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}; every other unit is a realizable non-Diţă point'
```

```text
'at the sorted alignment, the set of units at which H(u) admits a Diţă structure, of any shape or orientation, strictly or up to diagonal equivalence, is exactly {1, -1}'
```

### `L23` — `verification/lean/dita_local_escape_probe.py` — string

census L23: label re-scoped

```text
at all twenty Gaussian-rational candidates, both forms'
```

```text
at all twenty Gaussian-rational candidates, both forms, both at the sorted alignment'
```

### `L24` — `verification/lean/dita_local_escape_probe.py` — string

census L24: label names the nine index maps

```text
'a genuine deformation inside each of the nine classes (one twist phase u5): unitary, off SIG, and found by the search in its own class'
```

```text
'a genuine deformation at each of the nine named index maps of the sorted-alignment census (one twist phase u5): unitary, off SIG, and found by the search at the sorted alignment at its own partition structure'
```

### `L25` — `verification/lean/dita_local_escape_probe.py` — string

census L25: comment re-scoped (comment only, invisible to ast)

```text
# searched directly, as act 37's control does: two structures at u = -1 (one per orientation), none at u5
```

```text
# searched directly at the sorted alignment, as act 37's control does: two 2x8 partition structures at u = -1 (one per
# orientation), none at u5
```

### `L26` — `verification/lean/dita_local_escape_probe.py` — string

census L26: label re-scoped

```text
the transported matrices admit exactly two structures at u = -1 and none at u5'
```

```text
at the sorted alignment the transported matrices admit exactly two partition structures at u = -1 and none at u5'
```

### `L27` — `verification/lean/dita_local_escape_probe.py` — string

census L27: label re-scoped

```text
each admitting some census structure identically;
```

```text
each admitting some named index map of the sorted-alignment census identically;
```

### `L28` — `verification/lean/dita_local_escape_probe.py` — string

census L28: label re-scoped

```text
"act 37's arc W is straight and identically in the frozen 2x8 class t1 in both orientations and in no other structure (control of the classifier)"
```

```text
"act 37's arc W is straight and identically admitted at the frozen 2x8 index map t1 in both orientations and at no other named index map of the sorted-alignment census (control of the classifier)"
```

### `L29` — `verification/lean/dita_local_escape_probe.py` — string

census L29: label names the eighteen index maps

```text
lies in none of the eighteen subspaces, while the tangent space is the sum of all eighteen:
```

```text
lies in none of the eighteen subspaces of the named index maps, while the tangent space is the sum of those eighteen:
```

### `L31` — `verification/lean/dita_local_escape_probe.py` — string

census L31: success text re-scoped

```text
each of the eighteen census structures is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation'
```

```text
each of the eighteen named index maps of the sorted-alignment census is admitted only at u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the search at the sorted alignment at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: at the sorted alignment, for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape or orientation'
```

### `T1` — `verification/lean/dita_torus_probe.py` — docstring

census T1: module docstring re-scoped

```text
act 36's
objects and exhaustive structure search, act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.

```

```text
act 36's
objects and structure search (exhaustive over column blocks and row classes, each partition structure tested at the
sorted alignment), act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.

```

### `T4` — `verification/lean/dita_torus_probe.py` — string

mirror of census X31 in the verbatim head (comment only, invisible to ast)

```text
# structure (column blocks, row classes) is admitted at u iff
```

```text
# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at
# u iff
```

### `T2` — `verification/lean/dita_torus_probe.py` — docstring

census T2: search docstring re-scoped

```text
"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials:
```

```text
"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the
    rank-one condition at the sorted alignment, on a matrix of monomials:
```

### `Y1` — `verification/lean/dita_torus_locus_probe.py` — docstring

census Y1: module docstring re-scoped, with the pointer to act 41's probes

```text
act 36's objects, exhaustive structure search and stabilizer, act 37's monomial calculus and act 38's
pieces. It asserts the preregistered values and exits 1 on any mismatch; it certifies nothing beyond the arithmetic it replays.

```

```text
act 36's objects, structure search
(exhaustive over column blocks and row classes, each partition structure tested at the sorted alignment) and
stabilizer, act 37's monomial calculus and act 38's pieces. It asserts the preregistered values and exits 1 on any
mismatch; it certifies nothing beyond the arithmetic it replays. The loci over every index map are act 41's probes
verification/lean/dita_index_map_probe.py and verification/lean/dita_index_map_independent.py.

```

### `Y20` — `verification/lean/dita_torus_locus_probe.py` — string

mirror of census X31 in the verbatim head (comment only, invisible to ast)

```text
# structure (column blocks, row classes) is admitted at u iff
```

```text
# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at
# u iff
```

### `Y2` — `verification/lean/dita_torus_locus_probe.py` — docstring

census Y2: search docstring re-scoped

```text
"""the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials:
```

```text
"""the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the
    rank-one condition at the sorted alignment, on a matrix of monomials:
```

### `Y3` — `verification/lean/dita_torus_locus_probe.py` — string

census Y3: comment re-scoped (comment only, invisible to ast)

```text
# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe
```

```text
# ---- act 37's sorted-alignment census of SIG's Dita partition structures and act 38's two 2x8 exceptional index maps,
# verbatim from act 38's probe
```

### `Y5` — `verification/lean/dita_torus_locus_probe.py` — string

census Y5: section title re-scoped

```text
print('== 3. locus exactness: each candidate strictly and up to diagonal equivalence ==')
```

```text
print('== 3. locus exactness: each candidate at the sorted alignment, strictly and up to diagonal equivalence ==')
```

### `Y6` — `verification/lean/dita_torus_locus_probe.py` — string

census Y6: label re-scoped

```text
'the relaxed locus equals the strict locus for every candidate'
```

```text
'the relaxed locus equals the strict locus for every candidate at the sorted alignment'
```

### `Y7` — `verification/lean/dita_torus_locus_probe.py` — string

census Y7: label re-scoped

```text
'empty and nonempty strict loci'
```

```text
'empty and nonempty strict loci at the sorted alignment'
```

### `Y8` — `verification/lean/dita_torus_locus_probe.py` — string

census Y8: label re-scoped; the value holds only at the sorted alignment

```text
'every nonempty locus is cut out by coordinate characters u_k = +-1 alone'
```

```text
'every nonempty sorted-alignment locus is cut out by coordinate characters u_k = +-1 alone'
```

### `Y9` — `verification/lean/dita_torus_locus_probe.py` — string

census Y9: section title re-scoped

```text
print('== 4. union reduction: the union of the loci is five coordinate 2-subtori ==')
```

```text
print('== 4. union reduction: the union of the sorted-alignment loci is five coordinate 2-subtori ==')
```

### `Y11` — `verification/lean/dita_torus_locus_probe.py` — string

census Y11: label re-scoped

```text
'at (1, 1, 1): eighteen structures, exactly act 37 census in both orientations'
```

```text
'at (1, 1, 1) at the sorted alignment: eighteen partition structures, exactly act 37 census in both orientations'
```

### `Y12` — `verification/lean/dita_torus_locus_probe.py` — string

census Y12: label re-scoped

```text
'at (-1, -1, -1): one 2 x 8 structure per orientation, act 38 M_COL and M_ROW'
```

```text
'at (-1, -1, -1) at the sorted alignment: one 2 x 8 partition structure per orientation, act 38 M_COL and M_ROW'
```

### `Y14` — `verification/lean/dita_torus_locus_probe.py` — string

census Y14: label names the twenty index maps

```text
'for each of the twenty named structures (the census in both orientations, M_COL, M_ROW),
```

```text
'for each of the twenty named index maps (the sorted-alignment census of act 37 in both orientations, M_COL, M_ROW),
```

### `Y15` — `verification/lean/dita_torus_locus_probe.py` — string

census Y15: section title re-scoped; not independent of the loci in alignment

```text
print('== 7. an independent control: act 36\'s exhaustive structure search, with factor unitarity, at exact points ==')
```

```text
print('== 7. a control: act 36\'s structure search at the sorted alignment, with factor unitarity, at exact points ==')
```

### `Y16` — `verification/lean/dita_torus_locus_probe.py` — string

census Y16: label re-scoped

```text
the search finds exactly the predicted structures'
```

```text
the search at the sorted alignment finds exactly the predicted sorted-alignment partition structures'
```

### `Y17` — `verification/lean/dita_torus_locus_probe.py` — string

census Y17: label re-scoped

```text
'the classifier applied to the perturbed pieces:
```

```text
'the classifier at the sorted alignment applied to the perturbed pieces:
```

### `Y18` — `verification/lean/dita_torus_locus_probe.py` — string

census Y18: success text re-scoped

```text
print('dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted '
      'anywhere is among 46 enumerated candidates; their strict and relaxed loci are computed exactly and agree; the union of the '
      '30 nonempty loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, u3 = 1, u3 = -1; so H3 admits a Dita '
      'structure of some shape, index map and orientation, including up to diagonal equivalence, exactly when u1 = +-1 or u2 = 1 '
      'or u3 = +-1')
```

```text
print('dita_torus_locus_probe: OK -- for H3(u1, u2, u3) = SIG o u1^A u2^B u3^C on the three-torus: every Dita structure admitted '
      'anywhere is among 46 enumerated candidates; their strict and relaxed loci at the sorted alignment are computed exactly and '
      'agree; the union of the 30 nonempty sorted-alignment loci is exactly the five coordinate 2-subtori u1 = 1, u1 = -1, u2 = 1, '
      'u3 = 1, u3 = -1; so at the sorted alignment H3 admits a Dita structure of some shape and orientation, including up to '
      'diagonal equivalence, exactly when u1 = +-1 or u2 = 1 or u3 = +-1')
```

### `LH2` — `verification/lean-mathlib/OIBridge/DitaHierarchy.lean` — docstring

census LH2: the verdict under the flag p.no_44_82, attributed to exact computation over every index map (act 41)

```text
The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either
orientation under any relabelling: the `4 × 4` hierarchy is locally insufficient at the stratum,
and the first escaping family belongs to the `2 × 8` construction.
```

```text
[[Exact computation over every index map (act 41) shows that `P` admits no `4 × 4` Diţă
factorization of either orientation: the `4 × 4` hierarchy is locally insufficient at the stratum,
and the first escaping family belongs to the `2 × 8` construction. | Exact computation over every index map
(act 41) finds a `4 × 4` or `8 × 2` Diţă factorization at `P` or at the family's point `u = (3+4i)/5`,
strictly or up to diagonal equivalence, with {p.p44} `4 × 4` and {p.p82} `8 × 2` partition structures per
orientation at `P`, strictly. : p.no_44_82]]
```

### `LA1` — `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean` — docstring

census LA1: removes the completeness claim; the classes are named

```text
and, for each of the eight other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two
`2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — that a
Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`.
```

```text
and, for each of eight other named factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two
`2 × 8` — that a Diţă form of `Pu u` at its named index maps, in either orientation, forces `u = 1`.
```

### `LA2` — `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean` — docstring

census LA2: the complement under the flag w.exclusive, attributed to act 41

```text
The
exact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps
whatever admit a Diţă form of `Pu u` but the frozen class's.
```

```text
[[Exact
computation over every index map (act 41) carries the exhaustive complement: at every unit `u ≠ 1`, no
index maps whatever admit a Diţă form of `Pu u` but those of the frozen `2 × 8` partition structure. | Exact
computation over every index map (act 41) finds the arc not exclusive to the frozen `2 × 8` partition
structure away from `u = 1`, strictly; its strict exceptional set is `{w.exc_strict}`. : w.exclusive]]
```

### `LE1` — `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` — docstring

census LE1: removes the completeness claim; the classes and forms are named

```text
that for each of the nine Diţă factorization
classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's
Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either
orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a
realizable matrix admitting none of the eighteen forms.
```

```text
that for each of nine named Diţă factorization
classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8` — a Diţă form of `Hu u` at its named index
maps, in either orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG`
contains a realizable matrix admitting none of their eighteen forms.
```

### `LE2` — `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` — docstring

census LE2: the complement re-attributed to exact computation over every index map (act 41); the exceptional set from the measurement

```text
 The exact-computation layer carries the
exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,
```

```text

Exact computation over every index map (act 41) carries the exhaustive complement: at every unit
`u ∉ {e.exc_strict}`, no index maps whatever admit a Diţă form of `Hu u`,
```

### `LE3` — `verification/lean-mathlib/OIBridge/DitaLocalEscape.lean` — docstring

census LE3: the count at u = −1 from the measurement (one 2 × 8 per orientation is false under every index map)

```text

and at `u = −1` exactly one `2 × 8` structure per orientation does.
```

```text

and at `u = −1` exactly {e.m1} partition structures do, the two orientations together[[, among them in each
orientation a `4 × 4` partition structure, the image of the partition structure of act 37's `k4` under the row
exchange `7 ↔ 15` and the column exchange `2 ↔ 8` | : e.m1_k4_exchanged]].
```

### `LL1` — `verification/lean-mathlib/OIBridge/DitaTorusLocus.lean` — docstring

census LL1 (c, edited by owner direction): act 37's nine classes named as the kernel's named index maps

```text
act
37's nine classes in both orientations and act 38's two maps `M_COL`
```

```text
the nine
named index maps of act 37's sorted-alignment census, in both orientations, and act 38's two
maps `M_COL`
```

### `LL2` — `verification/lean-mathlib/OIBridge/DitaTorusLocus.lean` — docstring

census LL2: the converse under the flag h3.five_faces, attributed to acts 40 and 41

```text
The module does not state that the five faces exhaust the
points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to
diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.
```

```text
[[The module does not state that the five faces exhaust the
points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to
diagonal equivalence, is certified by exact computation over every index map (acts 40 and 41), not by the
kernel. | The module does not state which points outside the five faces admit a Diţă structure: exact
computation over every index map (act 41), not the kernel, finds the union of the loci, over every shape,
index map and orientation and up to diagonal equivalence, to be the flats {h3.maximal}. : h3.five_faces]]
```

### `J2` — `verification/lean-manuscript-census.json` — registry

census J2: act 36's searches scoped to the sorted alignment; the stratum point's 4 × 4 count from act 41

```text
the exhaustive block-structure searches, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding the known factorizations of the stratum point;
```

```text
the block-structure searches with the rows of each row class in sorted order, which find no 4 × 4 and no 8 × 2 Diţă factorization of either orientation at either point and exactly one 2 × 8 factorization of each orientation, while finding four 4 × 4 partition structures of the stratum point in each orientation, of the {sig.p44} that exact computation over every index map (act 41) admits;
```

### `J3` — `verification/lean-manuscript-census.json` — registry

census J3: act 36's count scoped as parametrizations at the sorted alignment; act 41's hull counts, matrix-family and modulo-gauge, stated separately

```text
the 492 4 × 4 Diţă hulls through the stratum point spanning its 49-dimensional defect at first order;
```

```text
the 492 4 × 4 Diţă hull parametrizations through the stratum point at the sorted alignment, whose tangents span its 49-dimensional defect at first order, while over every valid alignment exact computation over every index map (act 41) finds {hull.params} parametrizations, {hull.distinct_mat} distinct 4 × 4 hulls as matrix families and, counted separately, {hull.distinct_gauge} distinct 4 × 4 hulls modulo the gauge, with tangent dimensions modulo the gauge in {hull.dims}, [[every distinct hull inside the linearized and second-order unitarity conditions | not every distinct hull inside the linearized and second-order unitarity conditions : hull.dF_ok]], and their tangents spanning {hull.span} dimensions;
```

### `J4` — `verification/lean-manuscript-census.json` — registry

census J4: the conclusion under the flag p.no_44_82, attributed to act 41

```text
These are exact arithmetic replayed, not kernel-certified; by them the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction.
```

```text
These are exact arithmetic replayed, not kernel-certified. [[By exact computation over every index map (act 41), both points admit no 4 × 4 and no 8 × 2 Diţă factorization of either orientation, strictly or up to diagonal equivalence, and, strictly, {p.partitions} partition structures each, all of shape 2 × 8, so the 4 × 4 Diţă hierarchy is locally insufficient at the certified stratum point, and the first escaping family belongs to the 2 × 8 construction. | Exact computation over every index map (act 41) finds a 4 × 4 or 8 × 2 Diţă factorization at one of the two points, strictly or up to diagonal equivalence, with {p.p44} 4 × 4 and {p.p82} 8 × 2 partition structures per orientation at the named point, strictly. : p.no_44_82]]
```

### `J5` — `verification/lean-manuscript-census.json` — registry

census J5: removes the completeness reading

```text
and each of the eight other factorization classes of the stratum point admitted only at the base point (act 37, Track B)
```

```text
and each of eight other named factorization classes of the stratum point admitted only at the base point (act 37, Track B)
```

### `J6` — `verification/lean-manuscript-census.json` — registry

census J6: removes the completeness claim

```text
and for each of the eight other factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Pu u at that class's index maps
```

```text
and for each of eight other named factorization classes of the stratum point — four 4 × 4, two 8 × 2 and two 2 × 8 — a Diţă form of Pu u at its named index maps
```

### `J7` — `verification/lean-manuscript-census.json` — registry

census J7: act 37's census scoped; act 41's counts from the measurement

```text
the census of eighteen Diţă structures of the stratum point in nine classes modulo the stabilizer of order 1024 with transposition;
```

```text
the census, at the sorted alignment, of eighteen Diţă partition structures of the stratum point in nine partition orbits under the stabilizer of order 1024 with transposition, where exact computation over every index map (act 41) finds {sig.partitions} partition structures, forming {sig.porbits_full} partition orbits and {sig.classes_full} factorization classes under that stabilizer;
```

### `J8` — `verification/lean-manuscript-census.json` — registry

census J8: scoped; the eight are named

```text
the generic arc point admitting exactly the frozen class; each other class obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of twenty exactly named points ζ z^s w^t;
```

```text
the generic arc point admitting exactly the frozen 2 × 8 partition structure; each of the eight other named index maps obstructed by monomial conditions u^k = 1, k = ±1; the candidate exceptional set of the sorted-alignment calculus, twenty exactly named points ζ z^s w^t;
```

### `J9` — `verification/lean-manuscript-census.json` — registry

census J9: act 37's search scoped; the exceptional sets from act 41's measurement

```text
and the exhaustive search at each of them admitting only the frozen class away from u = 1, so that the exceptional set is exactly {1} and, for every unit u ≠ 1, the arc point is a Diţă matrix for the frozen 2 × 8 class and its transpose orientation and for no other index maps at all.
```

```text
and the search at the sorted alignment at each of them admitting only the frozen 2 × 8 partition structure away from u = 1. By exact computation over every index map (act 41) the strict exceptional set is exactly {w.exc_strict} and [[for every unit u ≠ 1 the arc point is a Diţă matrix for the frozen 2 × 8 partition structure in its two orientations and for no other index maps at all | the arc is not exclusive to the frozen 2 × 8 partition structure : w.exclusive]]; up to diagonal equivalence, as a separate statement, the exceptional set is {w.exc_relaxed}.
```

### `J10` — `verification/lean-manuscript-census.json` — registry

census J10: removes the completeness reading

```text
each of the nine factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of the eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)
```

```text
each of nine named factorization classes of the stratum point admitted along it only at the base point, and realizable matrices in none of their eighteen Diţă forms in every neighbourhood of SIG (act 38, Track B)
```

### `J11` — `verification/lean-manuscript-census.json` — registry

census J11: removes the completeness claim

```text
for each of the nine Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of Hu u at that class's index maps
```

```text
for each of nine named Diţă factorization classes of the stratum point — four 4 × 4, two 8 × 2 and three 2 × 8 — a Diţă form of Hu u at its named index maps
```

### `J13` — `verification/lean-manuscript-census.json` — registry

census J13: act 38's search scoped; the exceptional set under the flag e.exc_is_pm1 and the count at u = −1 from act 41's measurement

```text
and the exhaustive search at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two structures at u = −1 certified by exact reconstruction; so that the exceptional set is exactly {1, −1} and, for every unit u outside it, the arc point admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences;
```

```text
and the search at the sorted alignment at each of them, finding a Diţă structure at u = 1 and at u = −1 only, strictly and up to diagonal equivalence, with the two 2 × 8 partition structures it finds at u = −1 certified by exact reconstruction; by exact computation over every index map (act 41) the arc point admits no Diţă structure of any admissible shape, index map or orientation at any unit [[outside {1, −1}, strictly or up to the allowed diagonal equivalences | outside {e.exc_strict} strictly, and none up to the allowed diagonal equivalences at any unit outside {e.exc_relaxed} : e.exc_is_pm1]], with {e.m1} partition structures at u = −1;
```

### `J14` — `verification/lean-manuscript-census.json` — registry

census J14: the eighteen are named

```text
spanned by the eighteen first-order Diţă subspaces,
```

```text
spanned by the first-order Diţă subspaces of the eighteen named index maps,
```

### `J17` — `verification/lean-manuscript-census.json` — registry

census J17 (c, edited by owner direction): the converse attributed to acts 40 and 41, the verdict under the flag h3.five_faces

```text
are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation (act 40, Track B)
```

```text
[[are the five faces u₁ = ±1, u₂ = 1, u₃ = ±1: explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, the converse by exact computation over every index map (acts 40 and 41) | include the five faces u₁ = ±1, u₂ = 1, u₃ = ±1, with explicit factorizations on each whole face and exclusions at twenty named index maps in the kernel, and by exact computation over every index map (act 41) form the union of the flats {h3.maximal} : h3.five_faces]] (act 40, Track B)
```

### `J18` — `verification/lean-manuscript-census.json` — registry

census J18: act 40's probe scoped to the sorted alignment; the converse under the flag h3.five_faces, attributed to acts 40 and 41

```text
The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — is certified by the round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard: 46 candidate structures contain every structure admitted anywhere, their strict and relaxed loci coincide, and the union of the 30 nonempty loci is exactly the five faces.
```

```text
The round's exact-computation probe verification/lean/dita_torus_locus_probe.py, run in its own shard, shows that 46 partition candidates contain every Diţă structure admitted anywhere and computes each candidate's strict and relaxed loci at the sorted alignment, which coincide and whose 30 nonempty members have the five faces as union. The converse — that no other point admits a Diţă structure of any shape, index map or orientation, strictly or up to diagonal equivalence — [[is certified by exact computation over every index map (acts 40 and 41), act 40's enumeration supplying the candidates and act 41 their loci under every alignment | fails under exact computation over every index map (act 41), which finds the flats {h3.maximal} as the union of the loci : h3.five_faces]]: {h3.candidates} partition candidates, {h3.nonempty} of them with nonempty loci, [[strict and relaxed loci equal for every candidate | strict and relaxed loci differing : h3.strict_eq_relaxed]], and {h3.noncoord} of the loci's {h3.flats} distinct flats off the coordinate characters.
```

### `J19` — `verification/lean-manuscript-census.json` — registry

census J19 (c, edited by owner direction): act 37's nine classes named as the kernel's named index maps

```text
act 37's nine classes in both orientations and act 38's M_COL and M_ROW
```

```text
the nine named index maps of act 37's sorted-alignment census, in both orientations, and act 38's M_COL and M_ROW
```

### `R2` — `verification/ROADMAP.md` — roadmap

census R2: the P0 verdict under the flag p.no_44_82, attributed to act 41

```text
and, by the round's exact-computation probe, that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy;
```

```text
and, [[by exact computation over every index map (act 41), that point, of defect 37, admits no `4 × 4` Diţă factorization of either orientation at any block structure, so the `4 × 4` Diţă hierarchy is locally insufficient at the certified stratum point, act 35's open modulus being answered negatively for the `4 × 4` hulls and re-posed for the hierarchy | by exact computation over every index map (act 41), that point, of defect 37, or the family's point at `u₅ = (3+4i)/5` admits a `4 × 4` or `8 × 2` Diţă factorization, strictly or up to diagonal equivalence, with {p.p44} `4 × 4` and {p.p82} `8 × 2` partition structures per orientation at the named point, strictly : p.no_44_82]];
```

### `R3` — `verification/ROADMAP.md` — roadmap

census R3: completeness reading removed; the exceptional set from act 41's measurement

```text
by the kernel for the eight other factorization classes of the stratum point and by the round's exact-computation probe for every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class;
```

```text
by the kernel for eight other named factorization classes of the stratum point and by exact computation over every other index map (act 41), [[no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{w.exc_strict}`, and the arc is exclusive to its `2 × 8` partition structure | the exceptional set of the arc is `{w.exc_strict}`, and the arc is not exclusive to its `2 × 8` partition structure : w.exclusive]];
```

### `R4` — `verification/ROADMAP.md` — roadmap

census R4: completeness reading removed; the exceptional set under the flag e.exc_is_pm1, from act 41's measurement

```text
each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence:
```

```text
each of nine named Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by exact computation over every other index map (act 41), the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter [[outside `{1, −1}`, strictly or up to diagonal equivalence | outside `{e.exc_strict}` strictly, or outside `{e.exc_relaxed}` up to diagonal equivalence : e.exc_is_pm1]]:
```

### `R5` — `verification/ROADMAP.md` — roadmap

census R5: the eighteen are named

```text
spanned by the eighteen Diţă tangent subspaces,
```

```text
spanned by the Diţă tangent subspaces of the eighteen named index maps,
```

### `R7` — `verification/ROADMAP.md` — roadmap

census R7: the P0 verdict under the flag h3.five_faces; the converse attributed to acts 40 and 41

```text
are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.
```

```text
[[are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse by exact computation over every index map (acts 40 and 41). | include the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`, with the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and, by exact computation over every index map (act 41), form the union of the flats {h3.maximal}. : h3.five_faces]]
```

### `R9` — `verification/ROADMAP.md` — roadmap

census R9: removes the completeness reading

```text
for the classification of each against the
eighteen Diţă structures of the point:
```

```text
for the classification of each against the
Diţă structures of the point:
```

### `R10` — `verification/ROADMAP.md` — roadmap

census R10: removes the completeness reading

```text
none of the eighteen Diţă structures can have smaller
```

```text
none of the Diţă structures of the point can have smaller
```

### `R-A41` — `verification/ROADMAP.md` — append

this round's P0 sentence template and standing clause, appended once after act 40's standing clause

```text
no family other than act 39's is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle. |
```

```text
no family other than act 39's is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle. Under the reading of an index map that acts 36 to 40 froze, a pair of bijections that fixes the alignment of the rows across row classes, act 41's exact computation in two independent paths gives: {sig.partitions} Diţă partition structures at the certified rational stratum point, forming {sig.porbits_full} partition orbits and {sig.classes_full} factorization classes under its stabilizer; act 37's arc [[exclusive to its `2 × 8` partition structure away from `u = 1`, strictly | not exclusive to its `2 × 8` partition structure : w.exclusive]]; act 38's exceptional set {e.exc_strict}, with {e.m1} partition structures at `u = −1`; and act 39's family admitting a Diţă structure [[exactly on act 40's five faces | on the flats {h3.maximal} : h3.five_faces]], through {h3.nonempty} nonempty candidate loci. The verdicts and kernels of acts 36 to 40 stand. The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, no family other than those of acts 36 to 40 is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any realizable class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle. |
```


***

## Appendix C — the measurement slots


Templates use `{slot}` for a measured value and `[[text if true | text if false : flag]]` for a measured
boolean. Numbers are rendered by one frozen function: words below one hundred ("twenty", "forty-three"),
digits from one hundred ("976", "3896"). Sets are rendered as `{1}`, `{1, −1}`. Values measured at D41 are
given for orientation only; they are not pass conditions.

| slot | meaning | value at D41 |
| --- | --- | --- |
| `sig.partitions` | admitted partition structures at SIG, both orientations, strict | 20 |
| `sig.per_form` | per orientation | 10 |
| `sig.p44` / `sig.p82` / `sig.p28` | per orientation by shape | 5 / 2 / 3 |
| `sig.alignments` | valid alignments at SIG, both orientations | 976 |
| `sig.classes_full` | factorization classes, full stabilizer | 70 |
| `sig.classes_tfree` | factorization classes, transpose-free subgroup | 140 |
| `sig.porbits_full` | partition orbits, full stabilizer | 10 |
| `sig.porbits_tfree` | partition orbits, transpose-free subgroup | 20 |
| `sig.strict_eq_relaxed` | flag: strict and relaxed censuses at SIG equal | true |
| `sig.sorted_partitions` / `sig.sorted_porbits` | the sorted-alignment values (act 37's) | 18 / 9 |
| `hull.params` | 4×4 hull parametrizations, all alignments | 31168 |
| `hull.sorted_params` | at the sorted alignments | 492 |
| `hull.distinct_mat` | distinct hulls as matrix families | 3896 |
| `hull.distinct_gauge` | distinct hulls modulo the gauge | 3896 |
| `hull.bijection` | flag: the map matrix-family hull → hull modulo gauge is a bijection | (measured) |
| `hull.dims` | tangent dimensions modulo gauge, as a set | {14} |
| `hull.dF_ok` | flag: every generator in ker DF and D²F vanishing on every generator pair, every distinct hull | true |
| `hull.span` | rank of combined tangent span modulo gauge | 49 |
| `hull.W_in` | distinct hulls whose tangent contains W | 0 |
| `p.partitions` | admitted partition structures at P and at Pu(u5), each | 2 |
| `p.p44` / `p.p82` / `p.p28` | per orientation | 0 / 0 / 1 |
| `p.alignments` | valid alignments of the 2×8 at P, per orientation | 128 |
| `p.no_44_82` | flag: at `P` and at `Pu(u5)`, no 4×4 and no 8×2 partition structure under any alignment, strictly and relaxed | true |
| `w.exclusive` | flag: strictly, only the frozen 2×8 partition per orientation away from u = 1 | true |
| `w.exc_strict` / `w.exc_relaxed` | exceptional sets of act 37's arc | {1} / {1, −1} |
| `w.at1` / `w.m1_strict` / `w.m1_relaxed` | partition structures at u = 1, at u = −1 strict, relaxed | 20 / 2 / 20 |
| `e.exc_strict` / `e.exc_relaxed` | exceptional sets of act 38's arc | {1, −1} / {1, −1} |
| `e.m1` | partition structures at u = −1 | 4 |
| `e.exc_is_pm1` | flag: act 38's exceptional set is {1, −1}, strictly and relaxed | true |
| `e.m1_k4_exchanged` | flag: the 4×4 ones are k4 moved by rows 7↔15 and columns 2↔8 | true |
| `e.sig_only_at_1` | flag: every SIG partition structure admitted along act 38's arc only at u = 1 | true |
| `h3.candidates` | partition candidates of H3 | 46 |
| `h3.nonempty` | nonempty loci (union over alignments), strict | 43 |
| `h3.strict_eq_relaxed` | flag: strict locus = relaxed locus for every candidate | true |
| `h3.flats` / `h3.noncoord` | distinct flats / those not cut out by coordinate characters | 21 / 4 |
| `h3.five_faces` | flag: maximal flats are exactly act 40's five faces | true |
| `h3.maximal` | the maximal flats, as rendered strings (rendered comma-separated) | the five faces: `u1 = −1`, `u1 = 1`, `u2 = 1`, `u3 = −1`, `u3 = 1` |
| `h3.at_one` / `h3.at_mone` | partition structures at (1,1,1) / (−1,−1,−1) | 20 / 4 |
| `h3.sorted_nonempty` | the sorted-alignment value (act 40's) | 30 |
