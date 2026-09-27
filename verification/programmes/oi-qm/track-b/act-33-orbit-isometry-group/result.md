# Track B act 33 — the isometry group of the normalized single-carrier space: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #752. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A33.json`, and on the pull request.

- **`D`** — `db82376dfc0e2ae561ec541fd0d3a915f082beda`, act 32's receipt commit `Q`, the head of
  `main` after act 32's landing.
- **`F`** — `d5126a3d61f78ab38e3cca0ee7f744ce645d7196`, whose only parent is `D` and which adds the
  preregistration alone, blob `c36574d20c6d0b6397b0f25bf7479b95ff6fbae1`. Its `check-run` attestation
  is run 36258860788.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A33-CLASSIFIED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A33` | `A33-CLASSIFIED`, theorem `a33_classified` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a33_c_exclusive` and the eighteen statements required under this label:
- `A33-1`: `a33_shared_circles`;
- `A33-2`: `a33_shared_form` and `a33_shared_signs`;
- `A33-3`: `a33_shared_composition`, `a33_shared_identity` and `a33_shared_order`, with the four
  corollaries `a33_c_transitive_circles`, `a33_c_stabilizer_circle`, `a33_c_transitive_points` and
  `a33_c_stabilizer_point`;
- `A33-4`: `a33_shared_family_kernel`, `a33_shared_family_count`, `a33_shared_family_coset` and
  `a33_shared_family_onto`;
- the four controls `a33_control_conjugation`, `a33_control_a32`, `a33_control_phase` and
  `a33_control_incidence`.

***

## The frozen post-round sentence

> At the frozen single-carrier configuration, the surjective isometries of the normalized space are classified, at evidence level 2: every such map carries each of act 26's nine relabelled Fourier circles onto one of them, acts on each circle by `w ↦ λ w` or `w ↦ λ w̄` with `λ ∈ {1, −1}` fixed by its action on the two shared points of that circle, and is determined by the automorphism it induces on the incidence graph `K₃,₃` of the six shared points together with nine independent conjugation bits; every such pair is realized, the composition law is `ε''ᵣ = ε'ᵣ · ε_{σ'(r)}`, and there are exactly `72 · 2⁹ = 36864` surjective isometries. Act 25's four-shape family is a subgroup of index 16, meeting the kernel of the incidence action exactly in the conjugation patterns whose degree parities at the six shared points are uniform. This is a classification of the isometries of the frozen mathematical object; it adopts no isometry as a symmetry, a principle or a law.

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `pt r z` is the point of circle `r` at the unit
parameter `z`, `v₁ r` and `v₂ r` are its two shared points, at the parameters `1` and `−1`, and a
pair `(ν, ε)` is the normal form of `f` when `ν` is a permutation of the six shared points carrying
every circle's pair of shared points to a circle's pair, and `f (pt r z)` is `pt s (λ z)` or
`pt s (λ z̄)` according to `ε r`, with `s` the circle of the image pair and `λ = ±1` according to
whether the pair is carried in order or reversed.

**Coordinates on the circles.** Every coordinate of the feature map at a relabelled Fourier point is
`(1/64) · c · z̄ᵃ · zᵇ` with `c ∈ {±1}` and `a, b ∈ {0, …, 3}` read from the relabelling; the
exponent and sign tables are decided by the kernel over the four pairs of the nine circles
(`a33_shared_coord`). From them: the inner product of two points on circles `r` and `s` is a Laurent
polynomial in their parameters of degree at most two (`a33_shared_cross`), the points of one circle
at two parameters are at squared distance `(3/64) |z − w|²`, and two distinct circles meet only at
shared points, at the parameters the frozen tables `v₁`, `v₂` name: the seventy-two pairwise tables
`a33_shared_apart_…` and `a33_shared_meet_…` and the twelve incidence facts `a33_shared_inc_…` are
decided by the kernel, and `a33_shared_census` collects them.

**`A33-1`, `a33_shared_circles`.** By `a26_0_affine_extension`, a surjective isometry `f` of the
normalized set agrees on it with an affine isometry `g` of the ambient space carrying the set onto
itself. Along a circle `r`, the map `z ↦ g (pt r z)` is `A + B Re z + C Im z` for fixed vectors. The
membership of such a value on a circle `s` is a system of coordinate equations, each a Laurent
polynomial of degree at most two in `z` along the curve; an equation of that degree that holds at
five distinct unit parameters holds at all of them (`a33_shared_vanish`, through the Vandermonde
argument in `a33_shared_affine_coord`). The unit circle being infinite while the circles are nine,
some circle `s` receives infinitely many parameters of `r` (`a33_shared_into`), so `g` carries circle
`r` into circle `s`; the same for the inverse and the meeting data give equality.

**`A33-2`, `a33_shared_form` and `a33_shared_signs`.** With `g (pt r z) = pt s (w z)`, the parameter
`w z` is `α + β Re z + γ Im z` and has modulus one for every unit `z`; the coefficient identities
force `α = 0`, `|β| = 1` and `γ = ±iβ`, so `w z = β z` or `β z̄` (`a33_shared_circle_map`,
`a33_shared_unit_form`). The image of a shared point of `r` is a shared point of `s`, so `β` is the
parameter of a shared point and `β ∈ {1, −1}` (`a33_shared_signs`, through the per-circle incidence
partners).

**`A33-3`, the group.**
- *Existence and uniqueness of the normal form* (`a33_shared_exists_nf`, `a33_shared_nf_unique`).
  The circle permutation `σ` and the signs induce a well-defined map `ν` of the six shared points,
  bijective because `σ` is; its incidence condition is read from the two shared points of each
  circle, and the bit `ε r` from the image of `pt r i`. Uniqueness: the normal form prescribes `f` on
  every point of the set, and `ν`, `ε` are read back from the values at `pt r 1`, `pt r (−1)` and
  `pt r i` (`a33_shared_two_points`, `a33_shared_all_vertices`, `a33_shared_pt_inj_gen`).
- *Realization* (`a33_shared_real`). The seventy-two automorphisms of `K₃,₃` are the words of length
  at most eight in three generators, the relabellings `(1, (2 3))`, `(1, (1 2))` and the transpose
  (`a33_shared_aut_words`, decided by the kernel); each generator is realized by a surjective
  isometry with the expected normal form (`a33_shared_gen_0` to `a33_shared_gen_7`, through
  `relabel2_isometry`, `transpose_isometry` and `conj_isometry` lifted to the feature space by
  `bridge_of_tuple_isometry`), and words compose (`a33_shared_word8`). The kernel of the incidence
  action is realized by a nine-step induction on the circles, each step composing with the
  conjugation of one circle (`a33_shared_kernel_real`). The conjugation of circle 0 alone,
  `a33_shared_c0`, is the map that sends `pt 0 z` to `pt 0 z̄` and fixes every other point of the
  set; it is a surjective isometry because the points of circle 0 at `z` and `w` are at squared
  distance `(3/8) |z − w|²` (`a33_shared_chord0`), and because for each other circle `s` a word in
  the family's generators conjugates circle 0 and fixes circle `s` pointwise, so that its isometry
  carries the pair `(pt 0 z, pt s w)` to `(pt 0 z̄, pt s w)` (`a33_shared_conj_dist`, through
  `a33_shared_word8`). The conjugation of circle `r` is its conjugate by the relabelling that
  carries circle 0 to circle `r` (`a33_shared_conj_real`).
- *The identity, the composition law, the order and the four corollaries* follow by evaluating
  normal forms (`a33_shared_identity`, `a33_shared_composition`) and by kernel decisions over the
  seven hundred and twenty permutations of six points (`a33_shared_order`, `a33_c_transitive_circles`,
  `a33_c_stabilizer_circle`, `a33_c_transitive_points`, `a33_c_stabilizer_point`).
- **`a33_classified`** is `a33_shared_exists_nf`, `a33_shared_nf_unique` and `a33_shared_real`
  assembled.

**`A33-4`, the old family.** Every member of act 25's family agrees on the normalized set with a
shape: a row relabelling among twenty-four, a column relabelling among twenty-four, an optional
transpose and an optional conjugation, 2304 in all; and each shape is a word in the eight generators (`a33_shared_shape_word`,
`a33_shared_word_shape`, with the row and column words decided by the kernel). The kernel members
are exactly the thirty-two parity-uniform patterns (`a33_shared_family_kernel`, the shape parities
decided by the kernel in `a33_shared_shape_parity` and `a33_shared_kernel_shapes`), and the
parity-uniform patterns number thirty-two (`a33_shared_family_count`, decided by the kernel); the family is closed under composition and
contains the kernel intersection, so its fibres over the automorphisms are cosets
(`a33_shared_family_coset`); and its circle action is all of `Aut(K₃,₃)` (`a33_shared_family_onto`,
through `a33_shared_aut_shapes`).

**The controls.**
- `a33_control_conjugation`: the kernel realization at the all-false pattern is a surjective
  isometry with the pair `(1, every circle conjugated)`.
- `a33_control_a32`: act 32's witness lies in the group with the pair `(1, conjugate circle 0 only)`
  and outside the family, since that pattern is not parity-uniform (`a33_shared_not_parity_0`).
- `a33_control_phase`: multiplying the parameter of circle 0 at `i` by the phase `i` changes its
  distance to the point of circle 4 at `i`, by direct evaluation of the two distances.
- `a33_control_incidence`: every point of circle 0 is at distance at least one from every point of
  circle 3, circles 1 and 3 share their point at `1`, and no surjective isometry carries circle 0
  onto circle 1 and circle 3 onto itself, since it would carry a point of circle 0 and a point of
  circle 3 to that one shared point.

**`a33_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries three hundred and fifty-four theorems, each followed by its `#print axioms`
line; 52 of them are decided by the kernel.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a33_shared_…`, `a33_c_…` other than `a33_c_exclusive`, or
`a33_control_…` consumes a verdict theorem or `a33_c_exclusive`, and `a33_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance, and it records a helper absent
from that list as a deviation against the row it departs from, not repaired. The following landed
theorems, absent from the Provenance list, are consumed by shared lemmas — every one against the
first row of the matrix, and none by a verdict theorem, a control or `a33_c_exclusive` directly:

| helper | landed in | consumed by |
| --- | --- | --- |
| `conj_dilation` | `OrbitGeometryIsometries.lean` | `a33_shared_conj_F` |
| `conj_relabel2` | `OrbitGeometryIsometries.lean` | `a33_shared_gen_7`, `a33_shared_rel_CR` |
| `dist_featureVec` | `OrbitGeometryRigidity.lean` | `a33_shared_chord` |
| `featureVec_ofLp` | `OrbitGeometryRigidity.lean` | `a33_shared_feature_ext`, `a33_shared_ext_pt`, `a33_shared_affine_coord`, `a33_shared_into` |
| `iso1_family_acts` | `OrbitGeometryIsometries.lean` | `a33_shared_T_iso`, `a33_shared_rel_TR`, `a33_shared_rel_TC` |
| `realizable_conj` | `OrbitGeometrySelector.lean` | `a33_shared_C_iso`, `a33_shared_gen_7`, `a33_shared_rel_TC`, `a33_shared_rel_CR` |
| `relabel2_dilation` | `OrbitGeometryIsometries.lean` | `a33_shared_T_circle` |
| `relabel2_gramPhaseEquiv` | `OrbitGeometryIsometries.lean` | `a33_shared_stab_dsd_one`, `a33_shared_stab_one_dsd`, `a33_shared_gen_0`, `a33_shared_gen_1`, `a33_shared_gen_3`, `a33_shared_gen_4`, `a33_shared_gen_5`, `a33_shared_gen_6` |
| `relabel2_relabel2` | `OrbitGeometryIsometries.lean` | `a33_shared_rel_RR` |
| `sh1_sufficiency` | `TwoSidedGauge.lean` | `a33_shared_T_iso`, `a33_shared_T_invol`, `a33_shared_family_shape`, `a33_shared_rel_TR`, `a33_shared_rel_TC` |
| `stab_col_double` | `OrbitGeometryRigidity.lean` | `a33_shared_stab_one_dbl`, `a33_shared_stab_one_dsd` |
| `stab_col_swap13` | `OrbitGeometryRigidity.lean` | `a33_shared_stab_one_s13`, `a33_shared_stab_one_dsd` |
| `stab_row_double` | `OrbitGeometryRigidity.lean` | `a33_shared_stab_dbl_one`, `a33_shared_stab_dsd_one` |
| `stab_row_swap13` | `OrbitGeometryRigidity.lean` | `a33_shared_stab_s13_one`, `a33_shared_stab_dsd_one` |
| `transpose_admissible` | `OrbitGeometryIsometries.lean` | `a33_shared_T_iso`, `a33_shared_T_invol`, `a33_shared_shape_family`, `a33_shared_family_shape`, `a33_shared_rel_TR`, `a33_shared_rel_TC` |
| `transpose_isometry` | `OrbitGeometryIsometries.lean` | `a33_shared_T_iso` |
| `transpose_single_valued` | `OrbitGeometryIsometries.lean` | `a33_shared_T_iso` |

Each is a landed, kernel-checked theorem of the modules the frozen import closes over; none is
re-proved or paraphrased. They are recorded here as the freeze requires and change no statement.

***

## The `P0` cell and the guard

On `A33-CLASSIFIED` this round's sentence and its standing clause are appended once after act 32's
standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`aa98c620d859c1e07ef013d76fbf82d0203284ef`, the blob rehearsed for this case before the freeze.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `c36574d20c6d0b6397b0f25bf7479b95ff6fbae1`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `7f67ac4346f543f5fb9d0677572942d64d2cd709` at stage 1.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 7 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 64 mutation controls fail as required` and
    `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on eight receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A33-CLASSIFIED`, less this note:
  - added: the preregistration, `controls.py` and the module;
  - modified: `OIBridge.lean`, the census and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

The proofs were developed on a disposable branch from `F`, never landed: branch `claude/a33-dev`,
dispatch runs 36260031181, 36260347617, 36260577722, 36261156494, 36262031899, 36263052349, 36263793447, 36264819945, 36265488073, 36266295674, 36266554482, 36267279783, 36268604860, 36269594164, 36270236955, 36270907147, 36271548391, 36272252074, 36273233977 and 36273967096 red at the `Mathlib bridge` build; 36274601997 green there, every theorem printing `propext`, `Classical.choice` and `Quot.sound`, on the module that stage 2 carries up to its docstring and the position of the verdict and corollary; and 36275377264 green there on that module byte for byte. From run 36273233977 the disposable branch's workflow also printed a compact list of the build's diagnostics after the build step, a change to that branch's workflow alone. These runs are design evidence and not attestations.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

- **Act 32's theorems are outside the frozen import closure.** The Provenance list names act 32's
  `a32_shared_exists`, `a32_shared_isometry` and `a32_shared_separation`, and the route's step 5
  takes the controls `C_CONJ` and `C_A32` from them; but the frozen header imports
  `OIBridge.OrbitGeometryRigidity` alone, act 26's module, which act 32's module imports and which
  therefore does not contain it. No frozen statement is affected: the witness of act 32 that the
  route consumed, the conjugation of the Fourier circle alone, is constructed inside the round as
  `a33_shared_c0` from the round's own circle geometry and word isometries, as described above,
  and `a33_control_a32` and `a33_control_conjugation` are proved from it with their frozen
  statements. Act 32's theorems are consumed nowhere.
- The helpers recorded above under the route-authorization matrix.

None otherwise against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 33 classifies the surjective isometries of the frozen normalized single-carrier space, and adopts
> none. The group obtained is the isometry group of a mathematical object, a finite union of circles
> in a Euclidean space; its elements are not thereby physical symmetries, transformation laws,
> dynamics, time reversals, antiunitary operations or principles of nature, and its order and
> structure are facts about that object and about nothing else. A `CLASSIFIED` verdict settles that
> frozen isometry problem, and a `NOT-CLASSIFIED` verdict exhibits its failure. Neither verdict
> selects a physical law or closes `P0`. No isometry, carrier, family, group or principle gains
> physical status by appearing in this classification, and nothing here derives, recognises or
> approaches quantum evolution.
