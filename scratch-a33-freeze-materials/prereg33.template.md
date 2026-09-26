# Track B act 33 — the isometry group of the normalized single-carrier space: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39:
- one pull request from `D`, with the control plane drafted on it;
- execution after the owner designates `F`;
- as the round's protocol record, a receipt on which `tools/v3_verifier.py --verify-round` must
  print `VERDICT  HOLDS`.

> **THE CLAUSE, carried at this mention — the control plane.**
@@CLAUSE_Q@@

## The declarations

```v3-round
round A33
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/
record AM verification/receipts/A33.json
execution A verification/lean-mathlib/OIBridge/OrbitIsometryGroup.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

The record directory holds three files: this preregistration, the round's frozen controls
`controls.py`, and the result note. The receipt path is `verification/receipts/A33.json`. Every
other path the round changes is an execution path listed above. The guard,
`verification/lean/edge_rigidity_probe.py`, is not governed and is not changed: at `E` it is byte
for byte `D`'s, and `controls.py` checks that it is.

`ROADMAP.md` changes only on a decided outcome, and only as this file freezes: by the `P0` sentence
for the case, appended to the cell.

## The objects

- **`D`** = `@@D@@`: act 32's receipt commit `Q` and the head of `main` after act 32's landing. It
  is certified by push run 36251492248: all three jobs green, the guard 91 PASS and 0 FAIL, and the
  release gate 21 of 21 with `v3-receipts` holding on eight receipts. Every measurement here was
  taken at `D`.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`** — the last reconciliation: first parent `main` when it is built, second parent `E`.
- **`Q`** — the receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/A33.json`.

No other round runs beside A33 at this freeze. Should one land first, its movement of `main`
enters A33 only by reconciliation after `E`, with each row taken from the round that owns it.

***

## The hazards, stated before anything else

**Hazard 1 — two signs, one of them free.** On each circle an isometry acts by `w ↦ λ w` or
`w ↦ λ w̄`. The phase `λ ∈ {1, −1}` is not a free choice: it is fixed by where the circle's two
shared points go, so it is a function of the induced action on the incidence graph. The
conjugation bit `ε` is free, one per circle. Over each of the 72 incidence automorphisms there are
therefore exactly `2⁹` isometries, not `2⁹` phases times `2⁹` bits. The frozen normal form carries
the phase as the sign in front of the parameter and the bit as the choice between `z` and
`star z`, and the classification is stated as a bijection with pairs (incidence automorphism,
nine bits) — `72 · 2⁹ = 36864`.

**Hazard 2 — the completeness gap.** A group can be found without being shown complete. The
pre-freeze computations below found the same 36864 maps by two independent routes, but neither
route proves that *every* surjective isometry has the normal form: one assumes the form, the other
counts only the maps that preserve a finite marked set. The frozen theorems close the gap in three
steps, each a required statement: every surjective isometry permutes the nine circles (`A33-1`);
on each circle it has the form `w ↦ λ w^{±1}` with `λ` a unit (`A33-2`, first part); the unit `λ`
is `±1` (`A33-2`, second part). Only then does the count become a theorem.

**Hazard 3 — the finite-union step.** That a circle in the image lies on one of the nine is not
"a circle meets a circle in at most two points" alone. The step is: the image of circle `r` under
an affine isometry is a circle contained in the union of the nine; if it differed from every one
of them, it would meet each in at most two points and so contain at most eighteen points,
against its infinitely many. The freeze states the step so that its proof cannot silently assume
what it shows.

**Hazard 4 — classes, not encodings.** The classification is stated at the level of the
normalized set — the feature vectors of act 26's `normalizedSet` and act 26's surjective-isometry
predicate on it — and not at the level of tuples. A tuple-level statement would risk freezing
uniqueness of a representation rather than uniqueness of the induced map. Act 32's tuple-level
hypotheses reach this round only through act 26's bridge, as a realization surface.

**Hazard 5 — the group law by import.** The structure `C₂⁹ ⋊ Aut(K₃,₃)` is frozen as an explicit
law on pairs — the identity, the composition `ε''ᵣ = ε'ᵣ · ε_{σ'(r)}` with `σ'` the edge action
of the second factor, and uniqueness — and not as a Mathlib `SemidirectProduct`. The isomorphism
with the abstract semidirect product is a corollary in prose. No library import decides this round.

**Hazard 6 — the old family's place.** Act 25's four-shape family is not the group. It is a
subgroup of index 16, and the frozen statement of its place is exact: its intersection with the
kernel of the incidence action is the set of conjugation patterns whose degree parities at the six
shared points are all equal; the family maps onto the incidence automorphisms; and each fibre of
the family over an incidence automorphism is a coset of that intersection. The index follows.
No cohomological reading is frozen.

**Hazard 7 — negative controls at the decisive layer.** A control that fails only because a map
is not well defined on the shared points tests representation compatibility, not rigidity. The two
frozen negative controls reach the two halves of the theorem: a normal-form candidate with the
phase `i` on the Fourier circle breaks one exact cross-circle distance (`27/16 ≠ 39/32`), which
kills the continuous parameter; and a circle permutation that sends the non-meeting pair `(0, 3)`,
at squared distance at least `3/2`, to the meeting pair `(1, 3)`, which shares a point, kills every
permutation outside `Aut(K₃,₃)`.

**Hazard 8 — history.** Act 25 recorded `ISO3-UNDECIDED`, act 26 recorded `A26-2-UNDECIDED`, and
act 32 recorded `A32-NOT-RIGID`. All three stand as recorded. A decided outcome here settles the
group, and is stated as "the surjective isometries of the normalized space at the frozen
single-carrier configuration are classified", never as a revision of an earlier round's verdict.

**Hazard 9 — vocabulary.** An isometry of the normalized space is not a symmetry, the group is not
a symmetry group of anything physical, and the finite family is not a group adopted as physical.
None is written as the other.

***

## Provenance

The following are consumed as frozen declarations and frozen theorems, never re-proved and never
paraphrased:

- **act 12 and act 17** — `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`;
- **act 21**, `OrbitLawRigidityTwisted.lean` — `realizable_of_gramPhaseEquiv`;
- **act 23**, `OrbitLawGaps.lean` — `hadamard_z_admissible`;
- **act 24**, `OrbitGeometrySelector.lean`:
  - `mixedTriple`, `mixedTriple_gauge`, `mixedTriple_star` and `dist_eq_norm_toLp`;
  - `coord_le_dist`, `fourier_dist_le`, `geo1_class_invariant` and `geo1_equiv_of_zero_single`;
  - the frozen distance equation;
- **act 25**, `OrbitGeometryIsometries.lean`:
  - `iso1_single_carrier` and `iso2_classes_single`;
  - `mixedTriple_relabel2`, `mixedTriple_transpose` and `fibreGram_unique`;
  - `relabel2_isometry`, `conj_isometry` and `relabel2_realizable`;
  - the four generators and the four-shape conclusion;
- **act 26**, `OrbitGeometryRigidity.lean`:
  - `featureVec`, `normalizedSet` and `IsSurjIsometryOn`, the three definitions this round's
    statements are made of;
  - `featureVec_gauge`, `gramPhaseEquiv_of_featureVec_eq`, `featureVec_mem_normalizedSet`,
    `relabelled_fourier_mem_normalizedSet` and `normalizedSet_eq_iUnion`;
  - `bridge_of_tuple_isometry` and `tuple_isometry_of_bridge`;
  - `eqOn_affineSpan_of_agree`, `exists_affineIsometryEquiv_of_isSurjIsometryOn` and
    `a26_0_affine_extension`;
  - `a26_1_circle_count` with its nine circles `R`, and `rigid_motion_of_tuple_isometry`;
- **act 32**, `OrbitIsometryClassification.lean`:
  - `a32_shared_fourier_star`, `a32_shared_coord_inj`, `a32_shared_fourier_inj`;
  - `a32_shared_pair`, `a32_shared_classify` and `a32_control_overlap`;
  - `a32_shared_exists`, `a32_shared_isometry` and `a32_shared_separation`;
  - `a32_shared_relabel` and `a32_shared_star_mul_self`;
  - `a32_not_rigid`.

## Locating controls — at `D`

@@LOCATING@@

@@BLOBS@@

The names this round introduces return nothing from `git grep -l` at `D`: `OrbitIsometryGroup`,
`act-33`, `A33-` and `a33_`.

***

## Why this round exists

Act 32 exhibited one surjective isometry of the normalized space outside act 25's four-shape
family, and so showed the family incomplete. It did not say what the group is. Before the
classification of act 31's dynamical nonuniqueness can be compared with any geometric freedom, the
geometric freedom at the single carrier must be known completely: the group, its order, its
structure, and the place of the old family in it. This round freezes that classification as one
target with three outcomes, and states the group as an explicit law on pairs.

### What was measured before this freeze, recorded as the freeze's reading and not as a finding

Every quantity below was computed exactly, in rational or Gaussian-rational arithmetic, from the
landed act-26 relabellings and the landed feature map; the scripts are kept off the repository.

- **The nine circles.** Each of act 26's nine relabelled Fourier circles is, in feature
  coordinates, `c₀ + c₁ w + c₋₁ w̄` — a round circle of radius `√(3/8)`, with the distance within a
  circle `d² = (3/4)(1 − cos(t − u))`. The cross-circle inner products have two exact forms: for
  two circles that meet, `Re⟨f_r(t), f_s(u)⟩ = (5 ± 3 cos t)(5 ± 3 cos u)/64`; for two that do
  not, `5/32 ± (3/32) cos t cos u`. No cross-circle term in `sin t` occurs anywhere.
- **The incidences.** There are 18 incidences, found by an exact congruence solver and, as a
  check, by brute force over the 24th roots of unity: six points each on three circles, each
  circle through two of them at `w = 1` and `w = −1`. With the six points as vertices and the nine
  circles as edges, the incidence graph is `K₃,₃`. The six points are act 26's "six points, two per
  circle". The frozen vertex tables `v₁`, `v₂` record, for each circle, which vertex it meets at
  `w = 1` and which at `w = −1`.
- **Two derivations of the group.** (A) Assuming the normal form circle `r ↦ σ(r)`,
  `w ↦ λ_r w^{ε_r}`, the coefficient identities of the inner products were solved exactly by Smith
  normal form: 72 circle permutations `σ` survive, no continuous family survives, `λ_r ∈ {1, −1}`
  only, and 36864 maps result. (B) Without any circle structure, every automorphism of the exact
  24-point metric space of the circle points at `w ∈ {1, i, −1, −i}` was found by backtracking on
  the distance matrix alone: 36864, every one of which extends to an isometry carrying the
  normalized set onto itself. The two sets of maps agree element by element.
- **The structure.** The kernel of the action on circles is `C₂⁹`, generated by the nine
  single-circle conjugations, which are independent because no cross-circle inner product has a
  `sin·sin` term. The 72 circle permutations are exactly the edge actions of `Aut(K₃,₃)`, all of
  which are realized. Over each circle permutation there is exactly one phase vector `λ`, given by
  the vertex rule: `λ_r = 1` exactly when the induced vertex map carries the `w = 1` endpoint of
  circle `r` to the `w = 1` endpoint of `σ(r)`. The group is therefore the set of pairs (vertex
  automorphism, nine bits), with the composition law `ε''_r = ε'_r · ε_{σ'(r)}`, which was checked
  on 3000 random pairs; it is `C₂⁹ ⋊ Aut(K₃,₃)`, of order 36864, transitive on the nine circles
  (stabilizer of order 8) and on the six points (stabilizer of order 12). One chosen lift for each
  of the 72 incidence automorphisms forms a complement of the kernel.
- **The old family.** Act 25's four shapes over the 576 relabelling pairs give 2304 distinct maps
  on the 24 points, all in the group, closed under composition: a subgroup of index 16. It meets
  the kernel in 32 elements — exactly the conjugation patterns whose degree parities at the six
  vertices are all equal, the span of the six perfect matchings of `K₃,₃` — and it maps onto all 72
  incidence automorphisms. Act 32's witness, the conjugation of the Fourier circle alone, has odd
  degree parity at exactly its two endpoints and so lies outside the family.
- **The controls.** The identity, global conjugation and act 32's witness lie in the group, the
  witness outside the family. The phase-`i` candidate on the Fourier circle changes the distance
  from `f₀(−1)` to `f₄(i)` (`27/16`) against that from `f₀(i)` to `f₄(i)` (`39/32`). Circles 0
  and 3 do not meet and stay at squared distance at least `3/2`; circles 1 and 3 share the point
  `f₁(1) = f₃(1)`.

None of this is a finding of the round. The route below is the freeze's reading of how the frozen
theorems are reached; the theorems themselves decide.

***

## The configuration, FROZEN — act 26's, unchanged

- The visible family `Γ₀ = Matrix.of (fun _ _ => 1/4)`, bound by hypothesis in every statement.
- The ancilla `Fin 1` and the anchor `0`, act 12's single carrier.
- The normalized space: act 26's `normalizedSet Γ₀`, the feature vectors of the realizable tuples,
  in act 24's ambient Euclidean space with its real structure, and act 26's surjective-isometry
  predicate `IsSurjIsometryOn (normalizedSet Γ₀)`.
- Act 26's nine circles, as the frozen table `R`, and the point `pt r z` of circle `r` at the unit
  parameter `z`, bound by `let` in every statement that uses them.
- The six shared points as the frozen tables `v₁`, `v₂ : Fin 9 → Fin 6`.

***

## The frozen propositions — the exact Lean text

### The module header, FROZEN

The module `verification/lean-mathlib/OIBridge/OrbitIsometryGroup.lean` opens with exactly
`import OIBridge.OrbitGeometryRigidity`, its docstring, `namespace OIBridge`,
`namespace OrbitIsometryGroup`, and the one `open`:

```lean
@@OPEN@@
```

It carries no definition of any kind, no `variable`, no second `open` and no second `import`; every
theorem is followed by its `#print axioms` line. Each statement below is declared
`theorem NAME :` with no binder before the colon, and statements are compared after collapsing
whitespace. The `let`-bound tables inside a statement are part of the statement.

### `P_R` — the classification

```lean
@@P_R@@
```

### `P_N` — its negation

```lean
@@P_N@@
```

`P_N` is `P_R`'s negation pushed through the outer connectives: the first disjunct negates the
existence-and-uniqueness clause, the second the realization clause. `controls.py` rebuilds both
from the shared components and rejects any drift.

### `A33-1` — circle preservation, required under `A33-CLASSIFIED`

`B1`, `a33_shared_circles`:

```lean
@@B1@@
```

### `A33-2` — the normal form on a circle, and the signs, required under `A33-CLASSIFIED`

`B2`, `a33_shared_form`:

```lean
@@B2@@
```

`B3`, `a33_shared_signs`:

```lean
@@B3@@
```

### `A33-3` — the group law in coordinates, required under `A33-CLASSIFIED`

`COMP`, `a33_shared_composition` — the composition of two isometries in normal form is in normal
form, with the product vertex automorphism and the bits `ε''_r = (ε'_r = ε_{σ'(r)})`:

```lean
@@COMP@@
```

`C_ID`, `a33_shared_identity` — the identity is the normal form of the trivial pair:

```lean
@@C_ID@@
```

`ORDER`, `a33_shared_order` — the incidence automorphisms number 72:

```lean
@@ORDER@@
```

Its four corollaries, `a33_c_transitive_circles`, `a33_c_stabilizer_circle`,
`a33_c_transitive_points` and `a33_c_stabilizer_point`, required under `A33-CLASSIFIED`:

```lean
@@TRANS_C@@
```

```lean
@@STAB_C@@
```

```lean
@@TRANS_V@@
```

```lean
@@STAB_V@@
```

### `A33-4` — the old family, required under `A33-CLASSIFIED`

`FAM_K`, `a33_shared_family_kernel` — an element of the kernel lies in act 25's family exactly when
its degree parities at the six shared points are all equal:

```lean
@@FAM_K@@
```

`FAM_COUNT`, `a33_shared_family_count`:

```lean
@@FAM_COUNT@@
```

`FAM_COSET`, `a33_shared_family_coset` — over one vertex automorphism, the family's fibre is a
coset of the kernel intersection:

```lean
@@FAM_COSET@@
```

`FAM_ONTO`, `a33_shared_family_onto` — the family maps onto the incidence automorphisms:

```lean
@@FAM_ONTO@@
```

### The controls, required under both decided labels

`C_CONJ`, `a33_control_conjugation` — global conjugation is a surjective isometry with the normal
form of the trivial automorphism and all bits set to conjugate:

```lean
@@C_CONJ@@
```

`C_A32`, `a33_control_a32` — act 32's witness is a surjective isometry outside the family, with
the normal form of the trivial automorphism and one bit:

```lean
@@C_A32@@
```

`C_PHASE`, `a33_control_phase` — the phase `i` on the Fourier circle breaks one cross-circle
distance:

```lean
@@C_PHASE@@
```

`C_INCID`, `a33_control_incidence` — circles 0 and 3 stay apart, circles 1 and 3 meet, and no
surjective isometry carries circle 0 onto circle 1 while carrying circle 3 onto itself:

```lean
@@C_INCID@@
```

### The theorems, FROZEN by name and statement form

| role | theorem | statement |
| --- | --- | --- |
| `A33-CLASSIFIED` | `a33_classified` | `P_R` |
| `A33-NOT-CLASSIFIED` | `a33_not_classified` | `P_N` |
| corollary, required in every case | `a33_c_exclusive` | `(P_N) → ¬ (P_R)` |
| `A33-1`, required under `A33-CLASSIFIED` | `a33_shared_circles` | `B1` |
| `A33-2`, required under `A33-CLASSIFIED` | `a33_shared_form` | `B2` |
| `A33-2`, required under `A33-CLASSIFIED` | `a33_shared_signs` | `B3` |
| `A33-3`, required under `A33-CLASSIFIED` | `a33_shared_composition` | `COMP` |
| `A33-3`, required under `A33-CLASSIFIED` | `a33_shared_identity` | `C_ID` |
| `A33-3`, required under `A33-CLASSIFIED` | `a33_shared_order` | `ORDER` |
| `A33-3` corollary, required under `A33-CLASSIFIED` | `a33_c_transitive_circles` | `TRANS_C` |
| `A33-3` corollary, required under `A33-CLASSIFIED` | `a33_c_stabilizer_circle` | `STAB_C` |
| `A33-3` corollary, required under `A33-CLASSIFIED` | `a33_c_transitive_points` | `TRANS_V` |
| `A33-3` corollary, required under `A33-CLASSIFIED` | `a33_c_stabilizer_point` | `STAB_V` |
| `A33-4`, required under `A33-CLASSIFIED` | `a33_shared_family_kernel` | `FAM_K` |
| `A33-4`, required under `A33-CLASSIFIED` | `a33_shared_family_count` | `FAM_COUNT` |
| `A33-4`, required under `A33-CLASSIFIED` | `a33_shared_family_coset` | `FAM_COSET` |
| `A33-4`, required under `A33-CLASSIFIED` | `a33_shared_family_onto` | `FAM_ONTO` |
| control, required under both decided labels | `a33_control_conjugation` | `C_CONJ` |
| control, required under both decided labels | `a33_control_a32` | `C_A32` |
| control, required under both decided labels | `a33_control_phase` | `C_PHASE` |
| control, required under both decided labels | `a33_control_incidence` | `C_INCID` |

A module with neither verdict theorem reports `A33-UNDECIDED`, and a module with both is a failure
of the round. Every other theorem is named `a33_shared_…`, and every theorem is followed by its
`#print axioms` line.

### Pre-freeze evidence — design evidence, not attestation

These runs were made before this freeze, on disposable branches from `D` that are never landed.
Each is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design
evidence** recorded here: none is a `check-run` attestation, and no predicate of the round reads
them.

The elaboration file is `verification/lean-mathlib/OIBridge/OrbitIsometryGroup.lean` on those
branches. Under the frozen header it carries `#check` commands and nothing else.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36257341185 | `4c4155da7ccc2cf47d63bfe2ce7d8c4cba7f0ff2` | twenty candidate propositions in an earlier organisation, plus two library probes, wired directly after `OrbitIsometryClassification`, with a disposable census family | red at the `Mathlib bridge` build for one reason: the `⋊[φ]` notation of the `SemidirectProduct` probe is not in the kernel's import closure. The other 21 `#check`s elaborate; the kernel check and the numerical probes are green |
| 36257659584 | `cff3c1560f4c0fc09aba2c8af06e9f00e0fc0cd7` | the same, with the probe's own `import Mathlib.GroupTheory.SemidirectProduct` and one coset text corrected | all three jobs green. All 22 `#check`s elaborate, both probes included. The release gate passes all 21 steps with eight receipts holding |
| @@RUN3@@ | `baf76aa327a8cea603fc1fff9516a0effc006be1` | **the twenty frozen propositions of this file**, exactly as frozen, in their final organisation, and nothing else | @@RUN3_OUTCOME@@ |
| 36258147032 | `8d2e3b9b14b99e6397a3533d9cf326e8820cf061` | **the countercontrol**: the head of the second run with one deliberate defect, an extra argument to `pt` in `P_R`'s normal form | red, as required. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/OrbitIsometryGroup.lean:29:57: Application type mismatch`, at that argument; the kernel check is green |

The countercontrol shows that the elaboration check has force: an ill-typed frozen statement fails
the build at its own line, and nothing else fails. The `SemidirectProduct` probe is recorded for
what it shows about the library and is not part of the freeze; no frozen statement imports it.

***

## The question, FROZEN — one target

### `A33` — the isometry group at the single carrier

**At the frozen single-carrier configuration, is every surjective isometry of the normalized
space determined by, and realized from, an automorphism of the circles' incidence graph `K₃,₃`
together with nine conjugation bits — that is, is the isometry group exactly `C₂⁹ ⋊ Aut(K₃,₃)`?**

The answer is reported as one of three labels:
- `A33-CLASSIFIED`, the theorem `P_R`;
- `A33-NOT-CLASSIFIED`, the theorem `P_N`;
- `A33-UNDECIDED`.

***

## The controls

| role | object | what it is for |
| --- | --- | --- |
| identity | `a33_shared_identity` | the trivial pair is the identity's normal form |
| global conjugation | `a33_control_conjugation` | an old-family member of full conjugation lies in the group with the expected pair |
| act 32's witness | `a33_control_a32` | the one-circle conjugation lies in the group and outside the family, with the expected pair |
| continuous-parameter kill | `a33_control_phase` | a phase other than `±1` breaks an exact cross-circle distance |
| discrete-permutation kill | `a33_control_incidence` | a circle permutation outside `Aut(K₃,₃)` breaks an incidence obligation |
| duality | `a33_c_exclusive` and `controls.py` | the two verdicts cannot both be earned |

***

## The route, recorded as the freeze's reading and not as a finding

1. **`A33-1`, circle preservation.** By `a26_0_affine_extension`, a surjective isometry `f` of the
   normalized set agrees on it with an affine isometry `g` of the ambient space with its real
   structure, and `g` carries the set onto itself. For each circle `r`, the map
   `z ↦ g (pt r z)` is `A + B Re z + C Im z` for fixed vectors `A`, `B`, `C`, and every one of its
   values lies on one of the nine circles. Membership of a point on circle `s` is a finite set of
   equations each of which, along this curve, is a Laurent polynomial of degree at most two in `z`;
   such an equation either holds for every unit `z` or for at most four. Thirty-seven distinct unit
   parameters therefore put at least five on one circle `s`, and the equations of `s` then hold
   identically: `g` carries circle `r` into circle `s`. The same for `g⁻¹` and the fact that two
   distinct circles of the nine share at most one point give equality.
2. **`A33-2`, the form and the signs.** With `g (pt r z) = pt s (w z)`, the parameter `w z` is
   `α + β Re z + γ Im z`, of modulus one for every unit `z`; the coefficient identities force
   `α = 0`, `|β| = 1` and `γ = ± i β`, so `w z = β z` or `β z̄`. The unit `β` is the parameter of
   the image of a shared point, and the shared points of circle `s` sit at `±1`; the exact
   intersection data (`a32_control_overlap`'s method, at each pair) give `β ∈ {1, −1}`.
3. **`A33-3`, the classification.** Existence of the pair: the circle permutation and the signs
   induce a well-defined map of the six shared points, which is an automorphism of `K₃,₃`; the bit
   of each circle is read at `z = i`. Uniqueness: the normal form prescribes `f` on every point of
   the set, and the pair is read back from `f`'s values at `pt r 1` and `pt r i`. Realization:
   for each pair, the map defined by the normal form preserves every distance, by the exact
   inner-product identities of the reading above, and is onto. The composition law and the
   identity follow by evaluating the normal forms. The count 72 and the four corollaries are
   decided by the kernel over the 720 permutations of six points.
4. **`A33-4`, the old family.** Each of the 2304 family members acts on the 24 marked points by an
   explicit pair; the 32 kernel members are exactly the parity-uniform patterns; the fibres are
   cosets because the family is a subgroup containing the kernel intersection; and the family
   maps onto the incidence automorphisms because its circle action is all of `Aut(K₃,₃)`. The
   kernel decides the finite parts; act 32's `a32_shared_separation` method reads each shape at
   test classes.
5. **The controls.** `C_CONJ` and `C_A32` from `a32_shared_exists`, `a32_shared_isometry` and
   `a32_shared_separation`'s method; `C_PHASE` by exact evaluation of two distances; `C_INCID` by
   the exact inner-product bound, the shared point, and the argument that an isometry carrying
   circle 0 onto circle 1 and circle 3 onto itself would carry two points at positive distance to
   one point.
6. **`a33_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

No route to `A33-NOT-CLASSIFIED` is expected. The freeze's reading is that `P_R` holds.

### The route-authorization matrix, FROZEN

Authorized for every theorem without further mention: the declarations and theorems listed under
Provenance, Mathlib, and this round's own shared lemmas. **A helper needed but absent from this list
is a deviation, recorded against the row it departs from and not repaired.**

| theorem | may NOT consume |
| --- | --- |
| every `a33_shared_…` and every `a33_c_…` other than `a33_c_exclusive` | either verdict theorem; `a33_c_exclusive` |
| every `a33_control_…` | either verdict theorem; `a33_c_exclusive` |
| `a33_not_classified` | `a33_shared_circles`, `a33_shared_form`, `a33_shared_signs` |
| `a33_c_exclusive` | either verdict theorem |

***

## The preregistered prediction

| target | prediction | strength | recorded reason |
| --- | --- | --- | --- |
| `A33` | `A33-CLASSIFIED` | **very high** | two independent exact computations give the same 36864 maps and the same structure; the three completeness steps are elementary; every frozen statement elaborates |

**Every decided outcome is an allowed outcome.** A prediction that misses is recorded as missed.

***

## The outcomes, each with its FROZEN post-round sentence

### `A33-CLASSIFIED`

> @@S_C@@

### `A33-NOT-CLASSIFIED`

> @@S_NC@@

### `A33-UNDECIDED`

> @@S_X@@

### The corollary, REQUIRED

`a33_c_exclusive : (P_N) → ¬ (P_R)` is required in every case.

### The outcome table

The result note carries exactly one line `**Outcome:** \`LABEL\`` for its label.

| row | outcome |
| --- | --- |
| 1 | `A33-CLASSIFIED` |
| 2 | `A33-NOT-CLASSIFIED` |
| 3 | `A33-UNDECIDED` |

***

## The `P0` row, per case

At `D`, the `P0` cell of `verification/ROADMAP.md` ends with act 32's sentence and its standing
clause:

> @@P0_END_D@@

**On a decided outcome**, this round's sentence for the case is appended once after that standing
clause, followed by its own standing clause:
- **`A33-CLASSIFIED`:**

  > @@P0_C@@ @@P0_STAND33@@

- **`A33-NOT-CLASSIFIED`:**

  > @@P0_NC@@ @@P0_STAND33@@

**On `A33-UNDECIDED`** the cell is not touched.

The expected `ROADMAP.md` at `E` is `D`'s with that sentence appended, or `D`'s unchanged, byte for
byte. Rehearsed at `D`, the two decided cells give these blobs:
- `@@ROAD_C@@` (`A33-CLASSIFIED`);
- `@@ROAD_NC@@` (`A33-NOT-CLASSIFIED`).

The guard run locally at `D` against each rehearsed cell reports 91 PASS and 0 FAIL, the tags in
`D`'s order; the guard is not changed by this round.

***

## What no outcome licenses

- **No outcome revises act 25's `ISO3-UNDECIDED`, act 26's `A26-2-UNDECIDED` or act 32's
  `A32-NOT-RIGID`.** Those are the verdicts those rounds recorded, and they stand.
- **No outcome is written as "the symmetries of the space are this group".** The isometry group of
  the normalized space is a mathematical invariant of a mathematical object; it is not adopted as
  a symmetry group, a principle or a law.
- **No outcome reports anything at the product configuration**, and none compares this group with
  act 31's nonuniqueness. That comparison needs the product-space geometry first, and is not this
  round's.
- **No outcome reports anything about transition families or dynamics**, and none closes `P0`,
  which stays `OPEN`.
- **The group is not called canonical, physical or fundamental.**

## Non-doings

This round does not do any of the following:
- define anything, or restate any rung or declaration;
- read any configuration but the one frozen;
- edit any closed round's record;
- edit the guard;
- write any manuscript file;
- import any Mathlib module into the frozen module beyond what `OrbitGeometryRigidity` imports.

**Deriving or recognising quantum evolution is explicitly out of scope.**

## Definition budget

**Zero.** The module carries no definition of any kind, as `controls.py` checks; the tables `R`,
`pt`, `v₁` and `v₂` are `let`-bound inside each statement that uses them.

## Evidence level

**2** — Lean theorems, kernel-checked, every named result printing its axioms, each within `propext`,
`Classical.choice` and `Quot.sound`.

***

## `controls.py` — the round's own contracts, FROZEN

`verification/programmes/oi-qm/track-b/act-33-orbit-isometry-group/controls.py`, blob
**`@@CONTROLS_BLOB@@`**, is written before `F` and added by the execution with exactly this blob.
- It imports nothing from the repository and changes nothing.
- It reads `D` and the commit under check through `git`.
- It embeds every frozen text it compares against.

`controls.py check <commit>` fails unless all of the following hold:

- **The duality and the single source.**
  - The frozen `P_R` is the conjunction of the frozen existence-and-uniqueness clause and the
    frozen realization clause, and `P_N` the disjunction of their negations, rebuilt from the
    shared components.
  - Every other statement carries the one head, the one normal-form text, the one incidence
    condition, the one family text, the one parity text and the one circle text, verbatim, in
    the frozen multiplicities.
- **The module**:
  - begins with the frozen import and carries the one frozen `open`;
  - has no forbidden command or token;
  - has a `#print axioms` line for every theorem;
  - uses only the frozen names or `a33_shared_…`;
  - gives each frozen theorem its frozen statement, the statement ending at the `:=` that opens
    its proof and not at a `let` inside it;
  - has at most one verdict theorem, and `a33_c_exclusive`;
  - carries the statements the earned label requires.
- **The result note** carries:
  - the outcome line once;
  - the earned label's frozen sentence once, and no other label's;
  - THE CLAUSE's mention once, with the complete clause following it;
  - by name, the statements the label requires.
- **`ROADMAP.md`** is byte-identical to `D`'s with the frozen sentence for the case appended, or to
  `D`'s.
- **The guard** is byte-identical to `D`'s.
- **The census** is `D`'s with exactly one family appended, last, for `OrbitIsometryGroup`:
  `kernel-only`, no manuscript anchor, and its note naming the label and no other.
- **`OIBridge.lean`** is `D`'s with `import OIBridge.OrbitIsometryGroup` inserted directly after
  `import OIBridge.OrbitIsometryClassification`.
- **The paths** changed from `D` are exactly these:
  - added: the three record files and the module;
  - modified: `OIBridge.lean` and the census;
  - modified on a decided outcome only: `ROADMAP.md`.

`controls.py --self-test` also does four things:
- it checks the constants against this preregistration, beside it;
- it checks the duality and single source of the frozen texts, together with @@N_DMUTS@@ duality
  mutations, each of which must be rejected;
- it builds a synthetic execution for each of the three rows and requires every one to hold;
- it applies @@N_MUTS@@ mutation controls, each of which must fail with its named code.

Run at `D` beside this file, it prints:

@@SELFTEST@@

***

## The execution

**Before any commit**, the executor verifies this file's blob at `F` (`C1`). Then come linear
commits from `F`, each with one parent:

1. **Stage 1 — the module and the controls.**
   - `controls.py` with its frozen blob.
   - The module with the frozen header and its shared lemmas. On the route to `A33-CLASSIFIED`
     these include `A33-1` to `A33-4` and the four controls.
   - The import line.

   No verdict theorem and no corollary.
2. **Stage 2 — the verdict.** `a33_classified` or `a33_not_classified`, or neither, and
   `a33_c_exclusive`.
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
- **A verdict that cannot be obtained** is reported `A33-UNDECIDED`, with the step named. In that
  case `ROADMAP.md` is not touched.
- **A decided label whose required statements are not all proved** is not reported; it is
  `A33-UNDECIDED` with the missing statement named. A verdict prints only over green controls.
- **A freeze failure** is not `UNDECIDED` mathematics, and it is not repaired by changing the target.
  It is either of these:
  - a frozen proposition that is ill-typed or cannot be stated as frozen;
  - a required statement or control that is false as frozen when the route through it is taken.

  The round then halts under the specification's `S12`, with the result note naming the statement.
- **A round that cannot otherwise reach a green `E`** also halts under `S12`.
