# Track B act 32 — classification of the single-carrier surjective isometries: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #751. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A32.json`, and on the pull request.

- **`D`** — `d61c6c5409db201e3c25abbf3ec0ecce1f530684`, act 30's receipt commit `Q`, the head of
  `main` after act 30's landing.
- **`F`** — `11aabc9f3912833e20e45d8b7980b0f883fc255c`, whose only parent is `D` and which adds the
  preregistration alone, blob `bef375ff9ff1570b2566dbc451fb645cc35f35fd`. Its `check-run` attestation
  is run 36245656078.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A32-NOT-RIGID`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A32` | `A32-NOT-RIGID`, theorem `a32_not_rigid` | the same, very high |

The verdict theorem has the frozen statement `P_N` verbatim, compared after collapsing whitespace,
and so do the corollary `a32_c_exclusive` and the eight statements required under this label:
- the witness statements `a32_shared_exists`, `a32_shared_isometry` and `a32_shared_separation`;
- the five controls `a32_control_overlap`, `a32_control_moves`, `a32_control_global`,
  `a32_control_identity` and `a32_control_quarter`.

***

## The frozen post-round sentence

> At the frozen single-carrier configuration, the positive classification proposition posed as act 25's `ISO3` is false, at evidence level 2: a map that conjugates the Fourier parameter on the Fourier circle and fixes the class of every point of the other eight relabelled Fourier circles preserves realizability, is surjective on classes and preserves act 24's distance on realizable tuples, and for no pair of relabellings does it satisfy any of the four shapes. This is a statement about the frozen space and the frozen family; it adopts no isometry as a symmetry, a principle or a law, and it leaves act 25's and act 26's recorded verdicts as those rounds recorded them.

***

## The witness

The witness `φ` is any map satisfying the witness equations, and `a32_shared_exists` constructs one:
- on a tuple equivalent to the Fourier tuple at a unit parameter `z`, it returns the Fourier tuple at
  `star z`;
- on every other tuple it is the identity.

The parameter is chosen under `classical`. It is well defined because the coordinate
`((1, 0, 0), (0, 1, 0))` of the Fourier tuple at `z` is `z / 64`, so distinct unit parameters give
inequivalent tuples. The identity equations on the other eight circles hold at tuples that are also
on the Fourier circle because `a32_control_overlap` shows that such a tuple is fixed by conjugation.

***

## What was proved, and how

**`a32_control_overlap`.** For each of the eight circles one coordinate is read on both sides of the
equivalence. On circles 1, 2, 3 and 6 of act 26's list, that coordinate is `±1/64` on the Fourier
side and its negative on the other, so the two circles do not meet. On circles 4, 5, 7 and 8 it is
`±z/64` on the Fourier side and a real constant on the other, so `z` is real and conjugation fixes
the class.

**`a32_shared_isometry`.**
- **Classification of the realizable tuples.** Every realizable tuple lies on the Fourier circle or
  on one of the other eight, by `iso2_classes_single` and `a26_1_circle_count` (iii)
  (`a32_shared_classify`).
- **Realizability** is preserved by `hadamard_z_admissible`, `sh1_necessity` and
  `realizable_of_gramPhaseEquiv`.
- **Surjectivity** holds on the Fourier circle by conjugating the parameter back, and by the
  identity elsewhere.
- **The distance** is preserved in four cases, each read through `geo1_class_invariant`:
  - both tuples on the Fourier circle, by `a32_shared_fourier_star` and `conj_isometry`;
  - both off it, trivially;
  - one on it and one on another circle, by `relabel2_isometry` applied to a pair relabelling that
    conjugates the Fourier parameter and fixes every class of that circle (`a32_shared_pair`).
- **The pair relabellings.** Four relabellings are used: `((0 3)(1 2), 1)`, `((0 1)(2 3), 1)`,
  `(1, (0 3)(1 2))` and `(1, (0 1)(2 3))`. Each carries the Fourier tuple at `z` to the Fourier tuple
  at `star z` (`a32_shared_conj_A` to `a32_shared_conj_D`), and each of the eight circles is fixed
  pointwise on classes by one of them (`a32_shared_fix_1` to `a32_shared_fix_8`), all with explicit
  phases checked entrywise.

**`a32_shared_separation`.** For each pair of relabellings and each of the four shapes, a test class
on one of the nine circles at the parameter `i` is read through one coordinate. Through
`mixedTriple_relabel2`, `mixedTriple_transpose`, `mixedTriple_gauge` and, for the transpose shapes,
the dilation `iso1_single_carrier` supplies, every coordinate there is a power of `i` over `64`. Each
shape then reduces to a congruence of exponents mod 4, and the four exponent tables over all 576
pairs are decided by the kernel (`decide +kernel`).

**The other controls.**
- `a32_control_moves`: the Fourier class at `i` is sent to the class at `−i`, which differs from it
  by `a32_shared_fourier_inj`.
- `a32_control_global`: global conjugation satisfies the three hypotheses by `iso1_single_carrier`
  and `conj_isometry`, and the second shape at `(1, 1)`.
- `a32_control_identity`: the identity satisfies the three hypotheses and the first shape at
  `(1, 1)`.
- `a32_control_quarter`: the map sending the Fourier class at `z` to the Fourier class at `i z`,
  and fixing every other class, exists. It is not distance-preserving. Take the Fourier tuple at `1`,
  written on circle 4, and the point of circle 4 at `w₀ = (89999 + 600 i) / 90001`, which is off the
  Fourier circle. The first is moved to the Fourier tuple at `i` and the second is fixed. At the
  coordinate `((0, 0, 1), (3, 0, 0))` the images differ by `|−i/64 + 1/64|`, so by `coord_le_dist`
  their distance is at least `√2 / 64`. The original distance equals the distance between the
  Fourier tuples at `1` and `w₀`, by `relabel2_isometry`, and by `fourier_dist_le` it is at most
  `3 |w₀ − 1|`, where `|w₀ − 1|² = 4/90001`. Since `2/4096 > 36/90001`, the distance is not
  preserved.

**`a32_not_rigid`** follows the freeze's route, step 5, from `a32_shared_exists`,
`a32_shared_isometry` and `a32_shared_separation`.

**`a32_c_exclusive`**: `P_R` applied to `P_N`'s witness contradicts its `¬ FOUR`.

**Zero definitions.** The module carries fifty-six theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — honoured

Every helper the proofs consume is on the freeze's provenance list, or is Mathlib, or is one of this
round's own shared lemmas:
- acts 12 and 17: `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `AdmissibleDilationAt`,
  `sh1_necessity`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`;
- act 21: `realizable_of_gramPhaseEquiv`;
- act 23: `hadamard_z_admissible`;
- act 24: `mixedTriple`, `mixedTriple_gauge`, `coord_le_dist`, `fourier_dist_le` and
  `geo1_class_invariant`;
- act 25: `iso1_single_carrier`, `iso2_classes_single`, `mixedTriple_relabel2`,
  `mixedTriple_transpose`, `fibreGram_unique`, `relabel2_isometry` and `conj_isometry`;
- act 26: `a26_1_circle_count`.

Two general facts the proofs need and the provenance list does not carry are proved as the round's
own shared lemmas: the squared norm `star z * z = ‖z‖²` (`a32_shared_star_mul_self`), and that
relabelling both sides preserves `GramPhaseEquiv` (`a32_shared_relabel`).

Each theorem also keeps to its row:
- `a32_shared_exists`, `a32_shared_isometry`, `a32_shared_separation` and every `a32_control_…`
  consume neither verdict theorem nor `a32_c_exclusive`;
- `a32_c_exclusive` consumes neither verdict theorem.

No deviation is incurred.

***

## The `P0` cell and the guard

On `A32-NOT-RIGID` the stale clause is removed from act 25's and act 26's sentences in the `P0` cell
of `verification/ROADMAP.md`, and this round's sentence and its standing clause are appended once
after act 30's standing clause. The file's blob at `E` is `ebe80f84eadb7c48e0e566f8501887e291b0ca9f`,
the blob rehearsed for this case before the freeze.

The guard at `E` is the frozen ledger applied to `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The retired legs, by their ledger names, are
`ogc-road-read`, `ogc-p0-road-conjuncts`, `ogc-road-mut` and `ogc-description` for `R7-OGC`, and
`cgr-road-read`, `cgr-p0-road-conjuncts`, `cgr-road-mut` and `cgr-description` for `R7-CGR`. Both
checks keep their module, wiring, statement and mutation checks and the result-note conjuncts of
their `P0` predicates.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `bef375ff9ff1570b2566dbc451fb645cc35f35fd`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `43ba5c18bf2d0ca44fb97f074edeaf0c713a7074` at stage 1.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict propositions are duals and every shared text has one source; 9 duality
    mutations fail as required`, `controls: 3 rows hold as frozen, 54 mutation controls fail as
    required` and `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on six receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A32-NOT-RIGID`, less this note:
  - added: the preregistration, `controls.py` and the module;
  - modified: `OIBridge.lean`, the census, `ROADMAP.md` and the guard.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence for the executor and not
an attestation.

The proofs were developed on a disposable branch from `F`, never landed: branch `claude/a32-dev`,
dispatch runs 36247320536 and 36247897586 red at the `Mathlib bridge` build, and 36248241812 green
there on the module that stage 2 carries byte for byte, every theorem printing `propext`,
`Classical.choice` and `Quot.sound`. These runs are design evidence and not attestations.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 32 classifies the surjective isometries of the frozen normalized single-carrier space relative
> to the frozen four-shape family, and adopts none. A map satisfying the frozen isometry hypotheses
> is a mathematical isometry of that quotient space; it is not thereby a physical symmetry, a
> transformation law, a dynamics, a time reversal, an antiunitary operation or a principle of nature.
> A `RIGID` verdict classifies that frozen isometry problem, and a `NOT-RIGID` verdict exhibits a
> mathematical isometry outside the frozen family. Neither verdict selects a physical law or closes
> `P0`. No isometry, carrier, family or principle gains physical status by appearing in this
> classification, and nothing here derives, recognises or approaches quantum evolution.
