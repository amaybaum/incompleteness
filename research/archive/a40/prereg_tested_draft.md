# Track B act 40 — the Diţă locus of the three-parameter family through the product-embedded stratum point: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
> Act 40 proves and computes statements about act 39's three-parameter family through act 34's certified rational
> stratum point, and adopts none of them as anything but mathematics. A `LOCUS-CLASSIFIED` verdict settles which
> points of the three-torus admit a Diţă structure of the family, in two layers named separately: the kernel proves
> the explicit factorizations on the five faces and the exclusions at twenty named index maps, and the round's
> exact-computation probe certifies that no other point admits one. A `LOCUS-FAILS` verdict exhibits a failure of
> the kernel layer in the kernel. Neither verdict censuses the exponent matrices with entries in `{0, 1}`, decides
> whether support 48 is minimal or says anything about a family other than act 39's; both leave the product
> normalized set unclassified. Neither verdict establishes that any admissible transition law is covariant under
> any isometry, selects a physical law or closes `P0`. No hull, family, factorization, isometry, carrier, group or
> principle gains physical status by appearing here, and nothing here derives, recognises or approaches quantum
> evolution.

## The declarations

```v3-round
round A40
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-40-dita-locus/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-40-dita-locus/
record AM verification/receipts/A40.json
execution A verification/lean-mathlib/OIBridge/DitaTorusLocus.lean
execution A verification/lean/dita_torus_locus_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A40.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is.

The workflow changes by one frozen edit in five places: the round's probe runs in a shard of its
own, `probes_a40`, `Numerical probes / A40 locus`, inserted before the foundations shard, and the
aggregate `Numerical probes` job, the required check, lists it in its `needs`, reads its result into
its environment, echoes it and tests it for `success`. `controls.py` checks that the workflow at `E`
is `D`'s with exactly that edit. The placement was measured before this freeze (below): the probe
alone takes about eighty-five seconds of CI time, so a shard of its own keeps each round's probe
separately attributable and leaves act 38's shard as it was measured; either placement stays off
the critical path, which is the `Mathlib bridge` build.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell. The entries the roadmap records at `D` as separate future
directions — among them the census of exponent matrices with entries in `{0, 1}`, the minimality of
support 48 and the three-parameter family — are not edited by this round.

## The objects

- **`D`** = `b271b1dfe5a145d360c7c9433c81bfdf24ba0743`: the head of `main` after act 39's landing,
  `A39-REALIZABLE-PROVED`, receipt `verification/receipts/A39.json`; its parents are act 39's base
  `08a7707d` and act 39's receipt commit `e0a9f12b`. It is certified by push run 36423085812: all
  eight jobs green, the release gate passing with fifteen receipts holding and the 303 legacy
  records intact, the `Mathlib bridge` build green with `lean-axioms` at 5052 named results and no
  sorry, the guard `ALL CHECKS PASS`, and act 39's probe reporting its `OK` line. Every measurement
  here was taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A40.json`.

No other round runs beside A40 at this freeze. Should one land first, its movement of `main`
enters A40 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — one target, two layers, never merged.** The round's target is an equivalence:
`H3 u₁ u₂ u₃` admits a Diţă structure — of some shape, index map and orientation, strictly or up
to diagonal equivalence — exactly when `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1` or `u₃ = −1`. Its two
directions are certified by two different layers, and each is named as its own (§A.34):

- **the if-direction, in the kernel**: `A40-1`, five theorems, one per face, each an explicit
  strict Diţă factorization of `H3` or its transpose at **every** point of the face, with the shape,
  index map, orientation and factors named. No point sample and no single-point fallback stands in
  for a face;
- **the only-if direction, by exact computation**: the round's probe enumerates every structure
  admitted at any point of the torus among forty-six candidates, computes each candidate's strict
  and relaxed loci exactly, and reduces their union to the five faces. This is exhaustive exact
  arithmetic replayed in CI; it is **not** kernel-certified, and nothing in the result note or the
  surfaces says it is.

The kernel's second part, `A40-2`, is **not** the converse. It proves, for twenty named index maps,
that a strict Diţă form of `H3` at that map forces the named coordinate equations. It concerns
twenty maps, not every map; strict forms, not forms up to diagonal equivalence; and it makes no
claim that the twenty exhaust anything. The probe's exhaustion does not consume it, and it does not
stand in for the probe.

The kernel layer is frozen as one package, `P_R`, the conjunction of the twenty-five statements of
`A40-1` and `A40-2`; its name `a40_locus_kernel` says what it is. The round's label
`A40-LOCUS-CLASSIFIED` is earned only by `P_R` in the kernel **and** the probe green at `E`.

**Hazard 2 — strict and relaxed.** Every kernel statement is about the strict form
`H3 = dita X Y D` (or its transpose) with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`.
Diagonal equivalence enters only through the probe, in act 38's **relaxed** form (act 38's Hazard 5):
a Diţă form of `D₁ · H3 · D₂`, with unit diagonals, exists at some index maps exactly when the rows
of every class are proportional on every block and the block ratios satisfy the rank-one condition
up to a row-dependent factor, `λ(a,b,c) / λ(a,0,c)` independent of `c`; the strict form is the case
of a trivial factor. The probe computes the relaxed locus of each candidate by that condition and
finds it equal to the strict one. The faces' factorizations are strict, so they witness the relaxed form as well; the exclusions
are strict, and their relaxed counterparts are the probe's.

**Hazard 3 — two censuses, never confused.** Two different objects carry the word census in this
programme, and only one appears here:
- **act 37's census of the stratum point** — the eighteen Diţă structures of `SIG = H3 1 1 1`, act
  37's nine classes in both orientations. It appears as a **control**: the probe finds exactly those
  eighteen at `(1, 1, 1)`, and the kernel's twenty named maps include them;
- **the census of exponent matrices with entries in `{0, 1}`** — the roadmap's future enumeration of
  straight lines through the stratum point. It is **excluded**: no count, enumeration or
  classification of such matrices is claimed, used or computed, and no control depends on it.

**Hazard 4 — scope.** Excluded from the round, as statements, as dependencies and as readings of its
outcome:
- **the `{0, 1}` census**, beyond act 37's census of the stratum point in its role as a control;
- **support-48 minimality** — nothing is claimed about whether a realizable non-Diţă line through
  `SIG` with smaller support exists;
- **every family other than `H3`** — act 39's family, with act 38's pieces `A`, `B`, `C`, is the only
  object classified; no subfamily, perturbation or other exponent choice is classified, and the
  probe's countercontrol, which perturbs `C`, is a control of the classifier and not a statement
  about the perturbed family;
- **anything physical** — no family, factorization, isometry or locus gains physical status.

**Hazard 5 — the controls are controls.** The diagonal restriction `{1, −1}`, act 39's pair-face
level-set counts, act 37's census at `(1, 1, 1)`, act 38's `M_COL` and `M_ROW` at `(−1, −1, −1)`,
the absent face `u₂ = −1` and the probe's perturbed-`C` countercontrol are checked by the probe as
controls; none is a conclusion of the round.

**Hazard 6 — history.** Act 39 recorded `A39-REALIZABLE-PROVED`, act 38
`A38-NON-DITA-WITNESS-PROVED`, act 37 `A37-EXCLUSIVITY-PROVED`, act 36 `A36-HIERARCHY`, act 35
`A35-DITA-STRATIFIED`, act 34 `A34-STRATIFIED`, act 33 `A33-CLASSIFIED`, act 32 `A32-NOT-RIGID`,
acts 29 to 31 their product-configuration verdicts. All stand as recorded. A decided outcome here
extends act 38's diagonal exclusion to a classification of the whole torus of act 39's family, and
is never a revision of an earlier round's verdict.

**Hazard 7 — vocabulary.** A class is a pair of index maps, a family is a map from a torus to
matrices, a locus is a subset of the torus, a realizable matrix is a flat unitary on the carrier, an
isometry is not a symmetry, and none is written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 39**, `DitaTorus.lean` — its head, carrying act 38's head, and its objects `Ea`, `Eb`, `Ec`
  and `H3`, which this round carries verbatim; its theorems `a39_shared_unitary_core` and
  `a39_shared_flat_core`;
- **act 36**, `DitaHierarchy.lean` — `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_div` and
  `a36_shared_mod`;
- `OrbitGeometryIsometries.lean` — `transpose_unitary`;
- **act 38** — its maps `M_COL` and `M_ROW`, as act 38's probe records them, carried here as this
  round's `let`-bound objects `rmc`, `cmc`, `ditamc`, `rmr`, `cmr`, `ditamr`; no theorem of act 38
  is consumed by a proof;
- **Mathlib** — `Matrix.of`, `Matrix.of_apply`, `Matrix.unitaryGroup`,
  `Matrix.mem_unitaryGroup_iff`, `Matrix.mul_apply`, `Matrix.one_apply`, `Matrix.star_apply`,
  `Matrix.transpose_apply`, `Matrix.transpose_transpose`, `Matrix.cons_val_zero`,
  `Matrix.cons_val_one`, `Matrix.head_cons`, `Fintype.sum_prod_type`, `Fin.sum_univ_two`,
  `Fin.sum_univ_four`, `Fin.sum_univ_eight`, `Finset.sum_congr`, `Finset.mul_sum`,
  `Finset.sum_neg_distrib`, the star, norm and field lemmas of `ℂ` (`Complex.I_sq`,
  `Complex.star_def`, `Complex.ext`, `Complex.ext_iff`, `Complex.norm_I`, `Complex.normSq_apply`,
  `Complex.sq_norm` and their kin), and the tactics `fin_cases`, `simp`, `decide`, `ring`,
  `linear_combination`, `field_simp`, `norm_num`, `generalize` and `ext`.

## Locating controls — at `D`

| what | where | line |
| --- | --- | --- |
| `a39_shared_unitary_core`, `a39_shared_flat_core` | `verification/lean-mathlib/OIBridge/DitaTorus.lean` | 1644, 1654 |
| `a36_shared_z_unit`, `a36_shared_w_unit`, `a36_shared_div`, `a36_shared_mod` | `verification/lean-mathlib/OIBridge/DitaHierarchy.lean` | 44, 49, 59, 64 |
| `transpose_unitary` | `verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean` | 357 |

| file at `D` | blob |
| --- | --- |
| `DitaTorus.lean` | `486670e44350ce832f876e33d8cea541f19757ec` |
| `DitaLocalEscape.lean` | `07b15006f35d330e7f711e2353c070b187bb55a0` |
| `DitaHierarchy.lean` | `490a5db0f2141210fc0c08d49b44246d6ad949f8` |
| `OrbitGeometryIsometries.lean` | `954fbddaa7511713a26c316b3b2e0f29497e81d2` |
| `verification/lean-mathlib/OIBridge.lean` | `bb2fd8b27d3f2e4a2657b3aa640c9bbab314137b` |
| `verification/lean-manuscript-census.json` | `2dc14a330e247521f1835fe64f4413717eebbaed` |
| `verification/ROADMAP.md` | `f282da132c49711b2ac48127b74be66994f5382c` |
| `verification/lean/edge_rigidity_probe.py` | `d28e9b3cf2093984a1c453892204b9932a685b2e` |
| `verification/lean/dita_torus_probe.py` | `4405655907e1e508e0ce72b3335c905b0abcaf8d` |
| `.github/workflows/verify.yml` | `6c62b6574fc9db4c2be1cf38a690d3a6e425bd3d` |

The names this round introduces return nothing from `git grep -l` at `D`: `DitaTorusLocus`,
`act-40`, `A40-`, `a40_` and `dita_torus_locus`.

***

## Why this round exists

Act 38 proved that its arc, the diagonal `u₁ = u₂ = u₃ = u` of the three-parameter family, admits
no Diţă structure off `u ∈ {1, −1}`, and act 39 proved the whole family `H3` realizable on the
three-torus. Act 39 left open, and the roadmap records as the family's structural question, which
points of the torus admit a Diţă structure, of which shape and index map. This round freezes the
answer measured before it: the five coordinate faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`, and nothing
else — in particular not the face `u₂ = −1`.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed at `D` from act 38's and act 39's frozen probe objects, in exact
arithmetic; the scripts are kept off the repository except the frozen probe.

- **The flat calculus.** A point set of the torus cut out by characters `u^k = i^p z^q w^r` is a
  flat, stored in canonical Hermite normal form; the calculus — canonical form, meet, containment,
  emptiness and explicit points — is embedded in the probe and self-tested there (section 1).
- **Completeness.** A Diţă structure admitted at `u` makes the rows of each class proportional on
  every column block and rows of different classes not, so each pair of rows in a class has a
  proportionality locus on each block containing `u`. Enumerating, block by block, the partitions
  of the rows into cliques whose pair loci share a point, and per partition the exact covers of the
  columns by blocks with a common point, finds **46** candidate structures: 13, 5 and 5 of shapes
  `4 × 4`, `8 × 2` and `2 × 8` in each orientation. Every structure admitted anywhere is among
  them. A second method — closing the 320 pair-block loci under intersection, 9944 flats, and
  searching every containment pattern — returns the identical 46; it took about 737 seconds
  against 16, and it is recorded as design evidence, not frozen.
- **Locus exactness.** For each candidate the strict locus (the factor equations exactly) and the
  relaxed locus (act 38's form up to unit diagonal rescalings) are computed as flats: they coincide for every
  candidate; **16** are empty and **30** nonempty; every nonempty locus is cut out by coordinate
  characters `u_k = ±1` alone.
- **Union reduction.** The maximal nonempty loci are exactly the five faces; every nonempty locus
  lies in one of them and each face is itself a locus.
- **Factorizations on the whole face.** On each face, `X = ((1+i)/2) · [[1, 1], [1, −1]]`,
  `D ≡ 2/(1+i)² = −i` and `Y_c = (1+i) · (the class-representative rows of H3 on block c)`; the ratio
  of each class's second row to its representative is the `2 × 2` Fourier sign pattern on every
  block, so the identity holds entry by entry with the free units living only in `Y`, and the
  unitarity of `Y_c` follows from that of `H3` and the partner-row relations.
- **The named exclusions.** For each of the twenty named structures, single four-position witnesses
  `H i j · H i' j' = H i j' · H i' j` with coordinate characters generate its proportionality locus
  exactly.
- **The controls** — the diagonal, act 37's census, `M_COL` and `M_ROW`, the absent face, act 39's
  pair faces and the countercontrol — as frozen in the probe below.
- **Runtime.** The whole probe, single-threaded: about 141 seconds locally and 85 seconds in CI,
  peak resident memory 33 MB.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems and the probe decide.

***

## The configuration, FROZEN — act 29's product configuration over act 26's single carrier

- Act 39's frozen head, verbatim: act 38's head — act 36's head, act 37's row map, column map and
  Diţă form for each of the eight classes other than act 36's frozen one, act 38's `Ew` and `Hu` —
  followed by act 39's `Ea`, `Eb`, `Ec` and `H3`.
- This round's objects, `let`-bound after it: act 38's two `2 × 8` maps, column form `M_COL` and
  row form `M_ROW`, each with its Diţă form:

```lean
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
```

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/DitaTorusLocus.lean` opens with exactly
`import OIBridge.DitaTorus`, its docstring, `namespace OIBridge`, `namespace DitaTorusLocus`, and
the one `open`:

```lean
open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull DitaHierarchy DitaArcExclusivity DitaLocalEscape DitaTorus
```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement.

### The head, FROZEN

Every frozen statement is **the head followed by its body**, with nothing between them. The head is
act 39's frozen head followed by this round's objects; `controls.py` checks act 39's part against
act 39's text byte for byte, and checks that every statement begins with the head and carries its
own body once and no other kernel statement's body.

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
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
```

### `P_R` — the kernel layer

The head, then:

```lean
  (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∧ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∧ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∧ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∧ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1)
```

### `P_N` — its negation

The head, then:

```lean
  ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D)
  ∨ ¬ (∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D)
  ∨ ¬ (∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1)
  ∨ ¬ (∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1)
```

`P_N` is `P_R`'s negation: the conjunction of the twenty-five kernel statements becomes the disjunction of
their negations. `controls.py` rebuilds both from the shared components and rejects any drift.

### `A40-1` — the five faces, required under `A40-LOCUS-CLASSIFIED`

`FACE_1p`, `a40_shared_face_1p` — at every point of the face `u₁ = 1`, `H3` is a strict Diţă product `ditat2 X Y D` (act 37's class `t2`, column form), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:

```lean
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D
```

`FACE_1m`, `a40_shared_face_1m` — at every point of the face `u₁ = −1`, `H3` is a strict Diţă product `ditamc X Y D` (act 38's `M_COL`, column form), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:

```lean
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D
```

`FACE_2p`, `a40_shared_face_2p` — at every point of the face `u₂ = 1`, `H3` is a strict Diţă product `dita28 X Y D` (act 36's frozen `2 × 8` class, column form), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:

```lean
  ∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D
```

`FACE_3p`, `a40_shared_face_3p` — at every point of the face `u₃ = 1`, `H3` is the transpose `(dita28 X Y D)ᵀ` of a strict Diţă product (act 36's frozen `2 × 8` class, row form), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:

```lean
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ
```

`FACE_3m`, `a40_shared_face_3m` — at every point of the face `u₃ = −1`, `H3` is the transpose `(ditamr X Y D)ᵀ` of a strict Diţă product (act 38's `M_ROW`, row form), with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. The head, then:

```lean
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ
```


### `A40-2` — the twenty named exclusions, required under `A40-LOCUS-CLASSIFIED`

| theorem | index map | strict Diţă form | forces |
| --- | --- | --- | --- |
| `a40_shared_excl_k1_c` | act 37's class `k1` | `ditak1 X Y D` | `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_k1_r` | act 37's class `k1` | `(ditak1 X Y D)ᵀ` | `u₁ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_k2_c` | act 37's class `k2` | `ditak2 X Y D` | `u₂ = 1` |
| `a40_shared_excl_k2_r` | act 37's class `k2` | `(ditak2 X Y D)ᵀ` | `u₂ = 1` |
| `a40_shared_excl_k3_c` | act 37's class `k3` | `ditak3 X Y D` | `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_k3_r` | act 37's class `k3` | `(ditak3 X Y D)ᵀ` | `u₁ = 1` ∧ `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_k4_c` | act 37's class `k4` | `ditak4 X Y D` | `u₁ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_k4_r` | act 37's class `k4` | `(ditak4 X Y D)ᵀ` | `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_e1_c` | act 37's class `e1` | `ditae1 X Y D` | `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_e1_r` | act 37's class `e1` | `(ditae1 X Y D)ᵀ` | `u₁ = 1` |
| `a40_shared_excl_e2_c` | act 37's class `e2` | `ditae2 X Y D` | `u₃ = 1` |
| `a40_shared_excl_e2_r` | act 37's class `e2` | `(ditae2 X Y D)ᵀ` | `u₂ = 1` |
| `a40_shared_excl_t1_c` | act 36's frozen `2 × 8` class | `dita28 X Y D` | `u₂ = 1` |
| `a40_shared_excl_t1_r` | act 36's frozen `2 × 8` class | `(dita28 X Y D)ᵀ` | `u₃ = 1` |
| `a40_shared_excl_t2_c` | act 37's class `t2` | `ditat2 X Y D` | `u₁ = 1` |
| `a40_shared_excl_t2_r` | act 37's class `t2` | `(ditat2 X Y D)ᵀ` | `u₂ = 1` ∧ `u₃ = 1` |
| `a40_shared_excl_t3_c` | act 37's class `t3` | `ditat3 X Y D` | `u₁ = 1` ∧ `u₂ = 1` |
| `a40_shared_excl_t3_r` | act 37's class `t3` | `(ditat3 X Y D)ᵀ` | `u₂ = 1` |
| `a40_shared_excl_mc_c` | act 38's `M_COL` | `ditamc X Y D` | `u₁ = -1` |
| `a40_shared_excl_mr_r` | act 38's `M_ROW` | `(ditamr X Y D)ᵀ` | `u₃ = -1` |

`EXCL_k1_c`, `a40_shared_excl_k1_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1
```

`EXCL_k1_r`, `a40_shared_excl_k1_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1
```

`EXCL_k2_c`, `a40_shared_excl_k2_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1
```

`EXCL_k2_r`, `a40_shared_excl_k2_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1
```

`EXCL_k3_c`, `a40_shared_excl_k3_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1
```

`EXCL_k3_r`, `a40_shared_excl_k3_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1
```

`EXCL_k4_c`, `a40_shared_excl_k4_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1
```

`EXCL_k4_r`, `a40_shared_excl_k4_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1
```

`EXCL_e1_c`, `a40_shared_excl_e1_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1
```

`EXCL_e1_r`, `a40_shared_excl_e1_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1
```

`EXCL_e2_c`, `a40_shared_excl_e2_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1
```

`EXCL_e2_r`, `a40_shared_excl_e2_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1
```

`EXCL_t1_c`, `a40_shared_excl_t1_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1
```

`EXCL_t1_r`, `a40_shared_excl_t1_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1
```

`EXCL_t2_c`, `a40_shared_excl_t2_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1
```

`EXCL_t2_r`, `a40_shared_excl_t2_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1
```

`EXCL_t3_c`, `a40_shared_excl_t3_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1
```

`EXCL_t3_r`, `a40_shared_excl_t3_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1
```

`EXCL_mc_c`, `a40_shared_excl_mc_c`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1
```

`EXCL_mr_r`, `a40_shared_excl_mr_r`. The head, then:

```lean
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1
```


### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A40-LOCUS-CLASSIFIED` | `a40_locus_kernel` | `P_R` |
| `A40-LOCUS-FAILS` | `a40_not_locus_kernel` | `P_N` |
| corollary, required in every case | `a40_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A40-1`, required under `A40-LOCUS-CLASSIFIED` | `a40_shared_face_1p`, `a40_shared_face_1m`, `a40_shared_face_2p`, `a40_shared_face_3p`, `a40_shared_face_3m` | `FACE_1p`, `FACE_1m`, `FACE_2p`, `FACE_3p`, `FACE_3m` |
| `A40-2`, required under `A40-LOCUS-CLASSIFIED` | the twenty `a40_shared_excl_…` of the table above | `EXCL_…` |

A module with neither verdict theorem reports `A40-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a40_shared_…`, and every theorem is followed by its
`#print axioms` line.

### The frozen surfaces and the reference implementation

**Frozen**, and checked by `controls.py` at `E`: the head; the twenty-five statement texts and the
package structure of `P_R` and `P_N`; the theorem names and roles; the corollary; the module's one
import, one `open`, namespaces and zero definitions; the `#print axioms` line of every theorem; the
route-authorization matrix below; the probe blob, the workflow edit and every surface edit.

**Not frozen: the proofs.** The **reference implementation** of the module is blob
**`829146f6eff2b99aab54d7e5e9292b0ecfb33d8d`**. It carries 199 theorems: the twenty-seven frozen statements with their proofs,
and 172 further shared lemmas. It is the module proved on the design branch — blob
`0d42d28e992f0b056d8341e17b0c768933e39f18`, all 199 theorems clean — with exactly two changes: its
docstring, which there read *design draft* and here states the module's two-layer scope, and the
name of the verdict theorem, `a40_locus_kernel` for the design's `a40_classified`, at its
declaration and its `#print axioms` line. No statement, proof or other command differs. The
execution adds the reference implementation. A proof-only repair — a change to proofs or to shared
lemmas that leaves every frozen surface above unchanged — is permitted as a later linear commit
before `E`; the result note names the reference blob and the module's blob at `E`, and, if they
differ, states the departure from the reference implementation and justifies it, which
`controls.py` checks.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them. The design module is `verification/lean-mathlib/OIBridge/DitaTorusLocus.lean` on those
branches, wired after `DitaTorus` with a disposable census family.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36430858292 … 36450535104 | `a2357372` … `5eec100c` | eleven design iterations of the module: a first form with every `Y` written out literally (the bridge build took 56 minutes before failing), then one generic factorization lemma per structure, the exclusions by four-position witnesses, and repairs of the block unitarity, the value of `D` and the row identities | red, each diagnosed from the axiom audit; the twenty exclusions and forty face-relation lemmas clean from the fifth iteration on |
| 36451750208 | `f34feea0bae1cd3d28a83755cfd6cd8d4dbb019d` | the module in design form: every row identity by a definitional `show` to its class representative and one scalar lemma | all eight jobs green: 199 of 199 theorems within `propext`, `Classical.choice` and `Quot.sound`; the release gate's `lean-axioms` at 5251 named results, no sorry; the `Mathlib bridge` build 12 minutes cold |
| 36450749717 | `7dacbc0f0ef478ff026835fe52e3894fcabe4000` | **the countercontrol** on the preceding iteration's module: the proof of the face `u₂ = 1` run at `u₂ = −1`, and in the exclusion at `k1`, column form, the two witness values flipped | red, with exactly the predicted differential against that iteration: the four partner relations 0 to 3 of the face and the `k1` exclusion newly red; relations 4 to 7 and the other nineteen exclusions clean |
| 36452360434 | `c3821642f90c442dca898bc7a94709ac9f7472b7` | **the countercontrol** on the green design module, the same two perturbations | red, as predicted before the run from the probe's exact calculus and the module's dependency closure: **exactly nine** of 199 theorems carry `sorryAx` — the face's partner relations 0 to 3, its core and frozen theorem, the `k1` exclusion's core and frozen theorem, and the verdict — and the other 190 are clean |
| 36453414586 | `d6d95cdaab8001b17d1028abebb4e5baf5cf57f5` | the module in its frozen form, blob `0d42d28e992f0b056d8341e17b0c768933e39f18`: no linter option, one `#print axioms` per theorem | all eight jobs green: the release gate's `lean-axioms` at 5251 named results and no sorry, and each of the 114 axiom lines of this module within the retrieved log window `[propext, Classical.choice, Quot.sound]`; fifteen receipts holding, the legacy records intact |
| 36453264799 | `97a8805fd3d503b1710aa997d2fa5f9e5f8b349d` | `D` with the probe, blob `3905ae21445d6ba6221d96325b3ace18dbf0b777`, alone in a shard of its own under `/usr/bin/time` | all jobs green; the probe reports 22 `PASS`, no `FAIL`, and its `OK` line, in 1 minute 24.6 seconds of wall time, 84.5 seconds of user time, peak resident memory 33 MB |
| @@PREDICTED_RUN@@ |

The frozen probe differs from the measured blob `3905ae21` in one line, the title of its section 7,
which there read *numeric* for a search that uses exact Gaussian rationals throughout. The
repository's replay control, `tools/probe_replay_check.py 97a8805f verification/lean/dita_torus_locus_probe.py`,
run locally on a tree carrying the frozen blob, reports `OK -- 23 lines compared, 0 difference(s)`:
the two blobs print the same 22 check lines, with the same values in the same order, and the same
summary line.

***

## The exact-computation layer — the frozen probe

`verification/lean/dita_torus_locus_probe.py`, blob **`4b718e79f3800369855b6a9f0fc734ed2d59df4b`**, is written before `F` and
added by the execution at stage 1 with exactly this blob, and `.github/workflows/verify.yml` at `E`
is `D`'s with the frozen edit that runs it in its own shard, so that the shard runs the probe at
every execution commit from stage 1 on, and so at `E`. `F` carries this file alone and no probe; the
runs at `F` exercise the workflow at `D`. Its first part is act 38's probe head verbatim — act 36's
exact Gaussian rationals, structure search and stabilizer, act 37's monomial calculus and act 38's
pieces — and it uses Python integers and fractions for every value it asserts, no floating point
anywhere, and exits 1 on any mismatch with the values frozen here. Its statements are exact
arithmetic replayed; they are not kernel-certified, and the result note names them as this
layer's.

**0. Act 36's stabilizer, replayed**: factor stabilizer products 256 for each of the four
operations without factor exchange and 0 with it; the order **1024**.

**1. The flat calculus, self-tested.** On random character systems: the canonical form idempotent
and independent of generator order, every generator holding; the meet symmetric and associative,
contained in both arguments, and equal to `F` exactly when `G` contains `F`. On hand systems:
`u₁² = z` with `u₁⁴ = z³` empty and with `u₁⁴ = z²` satisfiable, `u₁u₂ = −1` with `u₁u₂ = 1` empty,
two presentations of one flat equal, a derived character holding and a wrong one not, and
`u₁² = 1` containing `u₁ = 1` and not conversely. Explicit points reconstructed on the unit-pivot
flats among 3000 random systems satisfy every original equation exactly, and moving `u₁` off a
flat that constrains it is detected.

**2. Completeness** — the only-if layer's first part: **46** candidate structures, 13, 5 and 5 of
shapes `4 × 4`, `8 × 2` and `2 × 8` in each orientation; every structure admitted at any point of
the torus is among them.

**3. Locus exactness** — the only-if layer's second part: for every candidate the relaxed locus
equals the strict locus; **16** empty and **30** nonempty; every nonempty locus is cut out by
coordinate characters `u_k = ±1` alone.

**4. Union reduction** — the only-if layer's conclusion: the maximal loci are exactly `u₁ = −1`,
`u₁ = 1`, `u₂ = 1`, `u₃ = −1`, `u₃ = 1`; every nonempty locus lies in one of them, and each is
itself a locus.

**5. Controls.** The union restricted to the diagonal is the two points `u = 1` and `u = −1`, act
38's exceptional set. At `(1, 1, 1)`, exactly eighteen structures, act 37's census of the stratum
point in both orientations. At `(−1, −1, −1)`, one `2 × 8` structure per orientation, act 38's
`M_COL` and `M_ROW`. **The absent face `u₂ = −1`**, a negative control: contained in no locus, and
its intersection with the union is the union of its intersections with the other four faces, each
of dimension 1. The three `+1` faces are act 39's pair subfamilies `(B, C)`, `(A, C)` and `(A, B)`,
with act 39's joint level-set counts **480, 440 and 424**, none failing.

**6. The kernel layer, replayed.** For each of the twenty named structures, single four-position
witnesses with coordinate characters generate its proportionality locus exactly, which contains its
strict locus; the whole-face factorizations hold at three Gaussian-rational points of each face, 15
in all, with `X` and every `Y_c` flat unitary and `|D| = 1`; and the factor identities
`(1+i)/2 · (1+i)/4 · 2/(1+i)² = 1/4`, `|(1+i)/2|² = 1/2`, `|(1+i)/4|² = 1/8`, `2/(1+i)² = −i`. These
replay the kernel's objects at points; they do not stand in for the kernel.

**7. An independent control**: act 36's exhaustive structure search, with factor unitarity, run
directly on `H3` at seventeen exact points — two generic, the five faces, two absent directions,
three lines, five special points — finds exactly the structures the loci predict there:
**0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4**. This search does not use the flat calculus
or the candidate enumeration.

**8. A countercontrol**: the classifier applied to act 38's pieces with the entry of `C` at row 1,
column 2 cleared finds **30** candidates and **23** nonempty loci, and the union collapses to the one
face `u₃ = 1`, where `C` drops out.

The probe reports 22 `PASS` and no `FAIL`, runs in about a minute and a half in CI, and ends
with the line `dita_torus_locus_probe: OK …` on success, which the result note carries verbatim,
and `dita_torus_locus_probe: FAILED …` with the failing checks otherwise.

***

## The question, FROZEN — one target

### `A40` — the Diţă locus of the three-parameter family

**For act 39's family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum
point: at which points `(u₁, u₂, u₃)` of the three-torus does `H3 u₁ u₂ u₃` admit a Diţă structure,
of some shape, index map and orientation, strictly or up to diagonal equivalence? The frozen answer
is: exactly when `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1` or `u₃ = −1`.**

The two directions, each with its own witness:

| direction | statement | witness | layer |
| --- | --- | --- | --- |
| if | on each face, at every point, `H3` or its transpose is a strict Diţă product of a named structure | `a40_shared_face_1p`, `a40_shared_face_1m`, `a40_shared_face_2p`, `a40_shared_face_3p`, `a40_shared_face_3m` | kernel, evidence level 2 |
| only if | off the five faces no structure of any shape, index map or orientation is admitted, strictly or up to diagonal equivalence | the probe's sections 2, 3 and 4 | exact computation, replayed in CI |
| beside the only-if | at twenty named index maps, a strict form forces the named coordinate equations | the twenty `a40_shared_excl_…` | kernel, evidence level 2 |

The answer is reported as one of three labels:
- `A40-LOCUS-CLASSIFIED`, the theorem `P_R` in the kernel with the probe green at `E`;
- `A40-LOCUS-FAILS`, the theorem `P_N`;
- `A40-UNDECIDED`.

The probe is not a label: green at `E`, it certifies the only-if layer; red at `E`, the round halts
as a freeze failure.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| the diagonal | the probe's section 5 | the classification restricted to act 38's arc gives act 38's exceptional set `{1, −1}` |
| act 37's census of the stratum point | the probe's section 5 | exactly the eighteen structures of `SIG` at `(1, 1, 1)` |
| act 38's maps | the probe's section 5 | exactly `M_COL` and `M_ROW` at `(−1, −1, −1)` |
| the absent face | the probe's section 5 | `u₂ = −1` lies in no locus; a face the answer omits is checked to be omitted |
| act 39's pair faces | the probe's section 5 | the three `+1` faces reproduce act 39's level-set counts 480, 440 and 424 |
| an independent search | the probe's section 7 | act 36's structure search, without the flat calculus, agrees at seventeen exact points |
| a wrong family is classified differently | the probe's section 8 | one entry of `C` cleared: 30 candidates, 23 loci, one face |
| the flat calculus | the probe's section 1 | canonicalization, meet, containment, emptiness and reconstruction on random and hand systems |
| duality | `a40_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

The kernel countercontrol — the absent face run through a face's proof and one exclusion's values
flipped, with exactly nine predicted theorems red — is pre-freeze design evidence, recorded above;
it is not rerun by the execution.

***

## The route, recorded as the freeze's reading and not as a finding

1. **The scalars.** `star x = x⁻¹` and `x ≠ 0` for units; `1 + i ≠ 0`; `2/(1+i)² = −i`, by
   `linear_combination` with `i² = −1`, so `‖D‖ = 1`; `(1+i)/2 · s · 2/(1+i)² · ((1+i) · m) = s · m`
   (`a40_shared_scal`); `X` flat unitary.
2. **`A40-1`.** For each of the four structures — act 37's `t2`, act 38's `M_COL`, act 36's `2 × 8`
   class, act 38's `M_ROW` — one generic lemma (`a40_shared_gen_…`): for any flat unitary `M` whose
   partner rows equal the block sign pattern times their class representatives, `M` is the Diţă
   product of `X`, `D` and `Y_c = (1+i) · M(representative rows on block c)`. Its row identities are
   sixteen lemmas, each a definitional `show` to the class representative and the scalar lemma; the
   unitarity of `Y_c` follows from the rows of `M` split by block. Each face then applies the
   generic lemma to `H3` at the face value, or to its transpose, with act 39's unitarity and
   flatness at the face and eight partner relations evaluated entry by entry.
3. **`A40-2`.** For each named map: from a strict Diţă form of `H3`, the four-position identity
   `H i j · H i' j' = H i j' · H i' j` at a witness, each entry evaluated to a monomial, reduces to
   `C · (u − v) = 0` with `C ≠ 0` a product of units, so `u = v`.
4. **`P_R`**: the twenty-five, assembled; **`a40_c_exclusive`**: `P_N` is the negation of `P_R`.

No route to `A40-LOCUS-FAILS` is expected. The freeze's reading is that `P_R` holds and the probe is
green.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a40_shared_…` | either verdict theorem; `a40_c_exclusive` |
| `a40_not_locus_kernel` | any theorem of `A40-1` or `A40-2` |
| `a40_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A40` | `A40-LOCUS-CLASSIFIED` | **very high** | the design module was compiled green on a disposable branch before the freeze, all 199 theorems within the three axioms, differing from the reference implementation only in its docstring and the verdict's name; its countercontrol failed exactly as predicted; and the frozen probe was run green at `D` |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A40-LOCUS-CLASSIFIED`

> At the frozen product configuration, the Diţă locus of act 39's three-parameter family is classified, in two layers named separately: for `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, `H3 u₁ u₂ u₃` admits a Diţă structure — of some shape, index map and orientation, strictly or up to diagonal equivalence — exactly when `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1` or `u₃ = −1`. The if-direction is proved in the kernel, at evidence level 2: at every point of each of the five faces, `H3` or its transpose is an explicit strict Diţă product of a named shape and index map with flat unitary factors. The kernel also proves, for each of twenty named index maps — act 37's nine classes in both orientations and act 38's `M_COL` and `M_ROW` — that a strict Diţă form of `H3` at that map forces its named coordinate equations. The only-if direction, over every shape, index map and orientation, and the agreement of the strict locus with the locus up to diagonal equivalence, are certified by the round's exact-computation probe and not by the kernel: forty-six candidate structures contain every structure admitted anywhere, the strict and relaxed loci of each coincide, the thirty nonempty loci are cut out by coordinate characters alone, and their union is exactly the five faces. This is a statement about the frozen mathematical objects; it censuses no exponent matrices, decides no minimality, concerns no family other than `H3`, and adopts no family, factorization or isometry as a symmetry, a principle or a law.

### `A40-LOCUS-FAILS`

> At the frozen product configuration, the kernel layer of the Diţă-locus classification fails, at evidence level 2: at some point of one of the five faces `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` admits no strict Diţă product of the frozen shape and index map, or at one of the twenty named index maps a strict Diţă form of `H3` holds off its named coordinate equations, and the witness is exhibited in the kernel. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.

### `A40-UNDECIDED`

> Neither the kernel layer nor its negation was obtained. The step at which the proof stopped is named, with what would settle it.

### The corollary, REQUIRED

`a40_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label, and the probe's
summary line `dita_torus_locus_probe: OK …` from the run at `E`.

| row | outcome |
| --- | --- |
| 1 | `A40-LOCUS-CLASSIFIED` |
| 2 | `A40-LOCUS-FAILS` |
| 3 | `A40-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 39's sentence and its standing
clause:

> For act 38's three exponent pieces `A`, `B`, `C`, the three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point is realizable at every point of the three-torus, by the kernel, with the joint level-set cancellation certified exactly by the round's probe; the family passes through the stratum point and its diagonal is act 38's arc. Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, act 38's diagonal exclusion is not carried to the generic point of the family, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A40-LOCUS-CLASSIFIED`:**

  > For act 39's three-parameter family `SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point, the points of the three-torus at which it admits a Diţă structure, of any shape, index map and orientation and up to diagonal equivalence, are exactly the five faces `u₁ = ±1`, `u₂ = 1`, `u₃ = ±1`: the explicit factorizations on the whole of each face and the exclusions at twenty named index maps by the kernel, and the converse over every index map by the round's exact-computation probe.

- **`A40-LOCUS-FAILS`:**

  > For act 39's three-parameter family through the certified rational stratum point, the kernel layer of the frozen Diţă-locus classification fails, by a witness exhibited in the kernel.

- the standing clause, after either:

  > The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open, no family other than act 39's is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle.

**On `A40-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `145251197bede7d2bbd0c5a2605c7827e1b042fa` (`A40-LOCUS-CLASSIFIED`);
- `c06b8078b921ade7cf78a5f9c64923d4ff66b164` (`A40-LOCUS-FAILS`).

The guard run locally at `D` against each rehearsed cell reports `ALL CHECKS PASS`, its output
byte-identical to its output at `D`; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 39's `A39-REALIZABLE-PROVED`, act 38's `A38-NON-DITA-WITNESS-PROVED` or
  any earlier verdict.**
- **No outcome says the kernel proves the only-if direction.** Its twenty exclusions concern twenty
  named maps in strict form; the exhaustion over every map and the relaxed forms are the probe's.
- **No outcome counts, classifies or minimizes exponent matrices.** Nothing is claimed about the
  exponent matrices with entries in `{0, 1}`, about the minimality of support 48, or about the
  orbits of such matrices; each stays the separate direction the roadmap records. Act 37's census
  of the stratum point appears as a control only.
- **No outcome classifies any family other than act 39's `H3`**, nor any subfamily as a family of its
  own, nor the perturbed pieces of the countercontrol.
- **No outcome classifies the classes of the product normalized set or its isometries.**
- **No outcome reports anything about transition families or dynamics.** Nothing here establishes
  that any admissible law is covariant under any isometry or reaches any class, and none closes
  `P0`, which stays `OPEN`.
- **No family, factorization, locus, class, isometry, group or covariance is called canonical,
  physical or fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard, or the roadmap's recorded directions;
- write any manuscript file;
- change the workflow beyond the frozen edit that adds the probe's shard;
- import any Mathlib module into the module beyond what `DitaTorus` imports;
- enumerate, count or classify exponent matrices.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; act 39's head and
this round's `rmc`, `cmc`, `ditamc`, `rmr`, `cmr` and `ditamr` are `let`-bound inside each statement
that uses them.

## Evidence level

**2** for the kernel layer — Lean theorems, kernel-checked, every named result printing its axioms,
each within `propext`, `Classical.choice` and `Quot.sound`. The probe's statements, among them the
only-if direction, are exact arithmetic replayed in CI, a separate layer named as such wherever
they are cited; the classification is certified by the two together and by neither alone.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-40-dita-locus/controls.py`, blob
**`d3821d5d1c88dc057e64be3635cbc3bcc749188c`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction of the twenty-five kernel statements over the frozen head,
    and `P_N` the disjunction of their negations, rebuilt from the shared components.
  - Every statement carries the one head; each kernel statement carries its own body once and no
    other kernel statement's; the head is act 39's frozen head, byte for byte, followed by this
    round's objects.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a40_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a40_c_exclusive`;
  - carries the statements the earned label requires;
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires;
  - the probe's summary line;
  - the reference implementation's blob and the module's blob at `E`, in backticks, and, if they
    differ, the words *departure from the reference implementation*.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen sentence for the case appended, or to
  `D`'s.
- **The guard** is byte-identical to `D`'s.
- **The probe** has its frozen blob, and **the workflow** is `D`'s with the frozen edit.
- **The census** is `D`'s with exactly one family appended, last, for `DitaTorusLocus`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.DitaTorusLocus` inserted directly after
  `import OIBridge.DitaTorus`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files, the module and the probe;
  - modified: `OIBridge.lean`, the census and the workflow;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it: the head, every proposition as
  the head followed by its body, the sentences, the clause, the `P0` texts, the blobs and the
  theorem names;
- it checks the duality and single source of the frozen texts, together with 14 duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies 75 mutation controls, each of which must fail with its named code, and checks that a
  reported proof-only departure from the reference implementation holds.

Run at `D` beside this file, it prints:

```text
controls: the two verdict propositions are duals and every shared text has one source; 14 duality mutations fail as required
controls: 3 rows hold as frozen, 75 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the controls, the probe and the module's shared lemmas.**
   - `controls.py` with its frozen blob.
   - The probe with its frozen blob, and the frozen workflow edit that runs it in its own shard.
   - The module: the reference implementation without the verdict theorem and the corollary, each
     with its `#print axioms` line — the 197 shared theorems, among them `A40-1` and `A40-2`.
   - The import line.
2. **Stage 2 — the verdict.** `a40_locus_kernel` and `a40_c_exclusive`, making the module the
   reference implementation; or, if it cannot be obtained, neither verdict.
3. **Stage 3 — the surfaces.** The census family, `kernel-only`, appended last. On a decided
   outcome only, the `P0` sentence for the case.
4. **The result note** `result.md`, whose commit is `E`; it carries the probe's summary line from
   the run at `E`'s predecessor and is confirmed by the run at `E`.

**Lean is run in CI only** (`AGENTS.md` §A.40), and so is the probe as a CI job. A stage whose build
fails is followed by a fixing commit, never rewritten, and a fix may touch proofs only. The label is
read from the module at `E`.

### Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| the probe is the frozen one and runs green in its own shard | `C3`: the probe's blob at stage 1 and at `E`; the `Numerical probes / A40 locus` shard green at every execution commit and at `E` with the probe's `OK` line in its log, and the aggregate `Numerical probes` job green |
| the module's frozen surfaces hold, and any departure from the reference implementation is reported | `C9`: `controls.py check E` — the statements and grammar, and the note's two blobs and departure statement |
| every verdict statement is kernel-checked, within the three axioms | `C8`: the dispatch run at `E`, the `Mathlib bridge` build and the release gate's `lean-axioms` step |
| the statements, duality, corollary and outcome grammar hold | `C9`: `controls.py check E` prints `controls: check OK` |
| the surfaces are exactly the frozen ones for the case, and the guard is untouched | `C9` |
| the guard stays green | `C8`: `ALL CHECKS PASS`, its output as at `D` |
| the change stays inside the governed paths | `C7`: `git diff --no-renames --name-status D E`; `C9` |
| the native receipts hold | `C6` at every stage commit; `C10` at `Q`: `--verify-round Q` prints `VERDICT  HOLDS` |
| the legacy records are untouched | `C6`: `legacy_records_check.py` at every stage commit and at `Q` |

### The status rule for the round

The label is the measurement, read off the module at `E`. If `C1` fails the round does not begin.

- **A proof-implementation failure with the frozen surfaces unchanged** is repaired by later linear
  commits before `E`, and reported in the result note as a departure from the reference
  implementation.
- **A verdict that cannot be obtained** is reported `A40-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A40-UNDECIDED` with the missing statement named. A verdict prints only over green controls,
  the probe among them.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target
  or any frozen surface. It is any of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement that is false as frozen when the route through it is taken, or that no
    proof-only repair can bring within the three axioms;
  - the probe red at `E` with the frozen blob — in particular a candidate count other than 46, a
    strict locus differing from its relaxed locus, a union other than the five faces, or a control
    failing.

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
