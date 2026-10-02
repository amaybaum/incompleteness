# Reconstruction round IIP-1 — the invariant inner product of a convex body's affine automorphisms: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted on its
pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round IIP-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/
record AM verification/receipts/IIP-1.json
execution A verification/lean-mathlib/OIBridge/InvariantInnerProduct.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/IIP-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, and no other round's record
change under any outcome.**

## The objects

- **`D`** = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, the head of `main` after `OG-1` landed (push run
  36973928206, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as the common
  base of this wave.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them. A sibling round of this wave
  (`CMP-1`) is drafted from the same `D`; whichever lands second reconciles against the `main` the first produced.

## What the round is

A small, premise-free, reusable lemma: a common fixed point and a positive-definite invariant inner product for the
affine automorphisms of a compact convex body, stated on the translation space of the body's affine span.

The construction needs no compactness of any group and no Haar measure. For a compact body `Ω` with nonempty
interior in coordinates `Fin n → ℝ`, with Lebesgue measure:

- the change of variables along an affine automorphism `g` with `g '' Ω = Ω` forces `|det g| = 1`, so integrals
  over `Ω` are invariant under `g`;
- hence `g` fixes the centroid `c` of `Ω`;
- hence the second-moment matrix `S = ∫_Ω (x − c)(x − c)ᵀ` satisfies `A S Aᵀ = S` for the linear part `A` of `g`;
- `S` is symmetric and positive definite because `Ω` has interior, so `⟨u, v⟩ = uᵀ S⁻¹ v` is a positive-definite
  inner product preserved by every such `A`.

Through `OrbitNormalization`'s affine chart `w ↦ L w + p0` of the affine span (`chart`, `bodyR`), the restricted body
of a compact convex body has nonempty interior, and the restriction of every affine automorphism of the body fixes
the restricted centroid and preserves the restricted inner product.

### In scope

1. `InvariantInnerProduct`, a new module: the change of variables along an affine automorphism preserving `Ω`; the
   centroid and its fixedness; the second-moment form, its symmetry, positivity and transpose-invariance; the inverse
   matrix as the invariant inner product; the restriction to the translation space of the affine span, where the body
   has nonempty interior; and a control showing that the relative-span formulation is needed: a body contained in a
   proper affine subspace of the ambient space has a vanishing ambient second moment (the segment on the first axis of
   the plane is the named instance), so no positive-definite ambient inner product comes from a lower-dimensional
   body.
2. The census family entry for the module, `kernel-only`, carried by no manuscript, inserted directly after the
   landed `OG-1` family ("conditional orbit-generation infrastructure …").
3. The import line `import OIBridge.InvariantInnerProduct`, inserted directly after the landed line
   `import OIBridge.OrbitNormalization`.

### Frozen out

Any ellipsoid statement; any orthogonality of a drive's flow or `J`; any closure, density or finite-word statement
about rotation groups; boundary transitivity and K∞-R; any dimension statement; the drive and its source; V4′; SC∞
and the completion; any manuscript or roadmap edit. The round claims no compactness of the automorphism group and
uses none.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

The design theorem identity is the statement surface of `InvariantInnerProduct` embedded in `controls.py` (blob
`e3ab7c649ef6fca38fc04aa4b2b051e5e6b585a2`). It consists of:

- the preamble (imports, namespaces, `open`, `variable`);
- every context line (`variable`, `open`, `namespace`, `end`), in order;
- the 40 declarations, in order and by kind;
- every theorem's signature up to `:=`;
- every definition, whole;
- the 21 `#print axioms` lines.

The reference module is blob `282b32f8954365c72581aad7486300375283311e` (`claude/iip1-dev` at `91638f14`). A
repair may change proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.InvariantInnerProduct` inserted
directly after `import OIBridge.OrbitNormalization`. The census is `D`'s with one family, embedded in `controls.py`,
inserted directly after the OG-1 family. Both insertions are placed relative to the landed baseline only.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| CHV | `abs_det_eq_one`, `setIntegral_comp_eq` | for a measurable body of positive volume and an affine automorphism `g` with `g '' Ω = Ω`: `|det| = 1`, and `∫_Ω h ∘ g = ∫_Ω h` |
| CEN | `centroid_fixed` | for a compact body of positive volume, `g (centroid Ω) = centroid Ω` |
| MOM | `moment_pos`, `momentMatrix_conj` | with nonempty interior the second moment is positive definite; `A S Aᵀ = S` for the linear part `A` |
| IIP | `invariant_inner_product` | `IsCompact Ω → (interior Ω).Nonempty →` `invMatrix Ω` is symmetric and positive definite, and every `g` with `g '' Ω = Ω` fixes the centroid and preserves `⟨u, v⟩ = u ⬝ᵥ (invMatrix Ω *ᵥ v)` through `linMatrix g` |
| SPAN | `invariant_inner_product_span` | for a compact convex `Ω` in a finite-dimensional `V` and an injective chart `w ↦ L w + p0` whose range is `affineSpan ℝ Ω`: `bodyR L p0 Ω` is compact with nonempty interior, `invMatrix (bodyR L p0 Ω)` is symmetric and positive definite, and every restriction `g'` of every automorphism `g` of `Ω` fixes the restricted centroid and preserves the restricted inner product |
| NULL | `momentMatrix_eq_zero_of_subset` | `s ≠ ⊤ → Ω ⊆ s → momentMatrix Ω = 0` for an affine subspace `s` of the ambient space |
| SEG | `segment2_moment` | for the segment on the first axis of the plane, `momentMatrix segment2 = 0` and the off-line direction has zero second moment |
| core | `iip1_core` | IIP, its positivity clause, NULL and `momentMatrix segment2 = 0` |

**Ambient nullity versus relative nondegeneracy.** NULL and SEG are ambient statements: a body that lies in a proper
affine subspace of the coordinate space has a vanishing ambient second moment, so no positive-definite ambient form
comes from it. SPAN is the relative statement: on the translation space of the affine span, where the body has
nonempty interior, the second moment is positive definite. The controls forbid moving SPAN's conclusion from
`bodyR L p0 Ω` to the ambient `Ω`.

### Semantic guards (in `controls.py`)

- **S1, span.** `invariant_inner_product_span` has the injective chart of the affine span among its hypotheses, and
  its conclusion is about `bodyR L p0 Ω`: compactness, nonempty interior and `invMatrix` of the restricted body. It
  never mentions the ambient `Ω`'s moment or `invMatrix`.
- **S2, interior.** Every theorem other than SPAN and the verdict that concludes positivity of `moment` or
  `invMatrix` has a nonempty-interior hypothesis. The verdict states `IsCompact Ω → (interior Ω).Nonempty →` before
  each positivity or invariance clause.
- **S3, lower-dimensional controls.** `momentMatrix_eq_zero_of_null`, `momentMatrix_eq_zero_of_subset`,
  `volume_segment2` and `segment2_moment` are kernel theorems with axiom prints. NULL has exactly the hypotheses
  `s ≠ ⊤` and `Ω ⊆ s` and the conclusion `momentMatrix Ω = 0`. The verdict carries `momentMatrix segment2 = 0`, and no
  theorem concludes positivity of a form on `segment2`.
- **S4, scope.** No declaration name, theorem conclusion or header claim concerns an ellipsoid, transitivity, a
  rotation group, closure generation, a drive or a dimension. The header carries "No ellipsoid, no transitivity and no
  dimension is claimed."

`controls.py`:
- is blob `e3ab7c649ef6fca38fc04aa4b2b051e5e6b585a2` (SHA-256
  `dd5137788c595c3c827762bb32b9ee579373fdb56f141c9b286290de6df47fab`, 566 lines), held on the disposable branch
  `claude/iip1-controls` at `e3dedd8b`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 23 checks. Its 12 mutation controls each fail with their named code:
  - a removed declaration (N1);
  - a changed binder context (N2);
  - a `sorry` (N3);
  - the span theorem strengthened to the ambient body (S1);
  - positivity without interior, and the interior hypothesis dropped from `invMatrix_pos` (S2, twice);
  - the segment control removed, and positivity claimed for the segment (S3, twice);
  - an ellipsoid name, and a transitivity conclusion (S4, twice);
  - a dropped import line;
  - a changed census status.
- `controls.py check <commit> --freeze F` runs P, N1–N3, S1–S4, I, C and F.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`. The kernel build,
the axiom report and the controls' text checks do not substitute for one another. The exact-head run on `F` attests
the frozen control plane and this preregistration only; no row is discharged at `F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| change of variables | `affine_apply_eq`, `setIntegral_comp`, `abs_det_eq_one`, `setIntegral_comp_eq` | built at `E`; printed axioms within `[propext, Classical.choice, Quot.sound]` | N2 |
| centroid | `centroid_fixed` | as above | N2 |
| second moment | `moment_eq_dotProduct`, `moment_pos`, `momentMatrix_det_ne_zero`, `moment_transpose_invariant`, `momentMatrix_conj` | as above | N2, S2 |
| invariant inner product | `invMatrix_pos`, `invariant_inner_product` | as above | N2, S2 |
| affine span | `interior_bodyR_nonempty`, `isCompact_bodyR`, `image_bodyR_eq`, `invariant_inner_product_span` | as above | S1 |
| ambient nullity | `momentMatrix_eq_zero_of_null`, `momentMatrix_eq_zero_of_subset`, `volume_segment2`, `segment2_moment` | as above | S3 |
| verdict | `iip1_core` | as above | S2, S3, S4 |

## Design evidence

These runs are design evidence, not attestations. For each I read the Mathlib bridge job only.

- **Run 36975944833** (`claude/iip1-dev`, `8319d3a0`): the bridge failed with five errors — two missing imports, the
  precedence of `∑ k, … + c` in two statements, a `simp` unfolding of `mulVec`, and a missing `NullSingletonClass`
  instance for the point control. The run was then cancelled.
- **Run 36976365427** (`dd06c1f3`, repair 1): Mathlib bridge job green. The repair parenthesized the two sums as
  intended and replaced the point control by the origin in dimension at least one.
- **Run 36978265025** (`91638f14`): Mathlib bridge job green on the owner-directed scope — the lower-dimensional
  control (NULL, SEG) in place of the origin control. Its log shows each of the 21 `#print axioms` lines reporting
  exactly `[propext, Classical.choice, Quot.sound]`, `lean-axioms` 5460 named results with no `sorryAx`, and the
  release gate passing. This module is the reference blob `282b32f8`.

## Stages

1. **C1** adds `controls.py`, blob `e3ab7c64`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`IIP-1-INVARIANT-INNER-PRODUCT-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the
  exact-head run at `E` is green on every job, the Mathlib bridge building `InvariantInnerProduct` with every frozen
  `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The
  result note claims the invariant inner-product infrastructure on the translation space of the affine span and
  nothing more.
- **`IIP-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome claims an ellipsoid, a dimension, the generation or closure of a rotation group, or boundary transitivity.
