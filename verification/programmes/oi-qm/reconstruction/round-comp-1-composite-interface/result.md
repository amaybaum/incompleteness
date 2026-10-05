# Reconstruction round COMP-1 — the weak field-neutral composite interface: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #789.

- **`D`** — `00ee70a60cf59d421c0056619709459d704fae99`, the head of `main` after round ORD-1 landed, certified by push
  run 37260494801.
- **`F`** — `082c5dfc8cc93687e17ebbb79ced59022a182199`, parent `7a203cf5bc5dca8cf4965a3a62425bf8f8c2faf8`;
  `delta(D, F)` is the preregistration alone, blob `fb8d4180fe5fc9a27827f1697eaf4fa4aca35123`. Its exact-head
  `workflow_dispatch` run 37264389776 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F` (comment 5989065347). That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `COMP-1-INTERFACE-PROVED`

The round types the composite of two bodies as a structure over an arbitrary real carrier with local tomography as its
one premise field, and proves the laws of attachment, discard, joint reversible action, sharp readout and no-signalling
on products without that premise.

In the kernel, for two factor bodies `ΩA ⊆ (Fin dA → ℝ)` and `ΩB ⊆ (Fin dB → ℝ)` and a real normed carrier `V`:

- **the three layers** (`ProductData`, `PreComposite`, `Composite`, `LocallyTomographic`): product data are a
  bi-affine product-state map and a bilinear product-effect pairing with `prodEff e f (prodState x y) = e x * f y`; a
  pre-composite adds a convex body containing the product states on which every product of effects is an effect and the
  unit pairing is one; a composite adds the single field `lt`, that two states of the body agreeing on every product of
  effects are equal;
- **the operations as definitions** (`attach`, `margA`, `condA`, `readout`, `JointReversible`, `minBody`,
  `maxBody`): attachment of a register state, discard in chart coordinates, the conditional state, the sharp register
  readout, joint reversible action as body preservation, and the minimal and maximal bodies;
- **the laws L1–L11 over the pre-composite** (`margA_prodState`, `margA_attach`, `eff_margA`, `margA_mem`,
  `readout_sum`, `isEffectOn_readout`, `sum_eq_unitEff_of_affineSpan`, `readout_prodState`, `readout_attach`,
  `condA_mem`, `condA_prodState`, `jointReversible_words`, `isEffectOn_readout_seedTransport`, `minBody_subset`,
  `subset_maxBody`): the marginal of a product is its factor and attach-then-discard is the identity; pairing with the
  marginal is the unit pairing; the marginal and the conditional state of a composite state lie in a compact convex
  factor body; a sharp readout is a two-outcome test, reads the register on products and is certain after attaching the
  matching register state; no signalling on products; reversible actions compose; the body lies between the minimal and
  the maximal body. None of these consumes `lt`;
- **the separation clause** (`Composite.pairing_injective`): on a composite the table of product-effect values
  determines the state, the one statement that consumes `lt`;
- **the extremal pre-composites** (`minPre`, `maxPre`): the minimal and maximal bodies of any product data;
- **the instances** (`bitComposite`, `ball3MinComposite`, `ball3MaxComposite`): the classical bit and bit, and two
  copies of `ball3` with the minimal and the maximal body, on the coordinate model `Fin (dA + 1) → Fin (dB + 1) → ℝ`, in
  which the product pairing separates points and local tomography is a theorem of that model (`modelData_ext`,
  `prodEff_eq_of_eff_eq`);
- **the padding control** (`paddedPre`, `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre`, and their
  ball-pair forms): for any pre-composite with nonempty body, the padded pre-composite on `V × ℝ` satisfies every other
  field and is not locally tomographic, so no composite extends it, and `lt` is independent of the other eight fields;

joined in the verdict `comp1_core`.

Local tomography is a premise of the structure and is concluded of no pre-composite; composite existence is concluded
only for the three named instances. A later round that needs local tomography of a composite it constructs proves it
for that composite or carries it as an explicit hypothesis; nothing here establishes it for any other composite. The
round constructs no composite larger than the minimal body from any source, sources no local tomography, and does not
identify the quantum composite. It states no gate relation, common NOT, dimension, transitivity, order, drive or
availability, types no stage-level product of two towers, and uses no complex, matrix, Kronecker or tensor-product
primitive. It edits no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `082c5dfc` | the preregistration | 37264389776 | `success`, all 32 jobs; release gate PASS, `lean-axioms` 5552, as at `D` |
| `C1` = `199e05cf` | stage C1: `controls.py`, blob `38f1898a` | none required | `controls.py --self-test`: `controls: OK -- 36 checks` |
| `S1` = `70ce2632f41c2558443bd59cdce9c62ffd5331df` | stage S1: `CompositeInterface` blob `91567f53`, the import line (`OIBridge.lean` blob `b1a8b89a`), the census family (blob `ba36fdd4`) | 37271337107 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `8e294cb4`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 20 checks`.

Run 37271337107 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check (job 111638791719), the Mathlib bridge (job 111638791701), the 29 numerical-probe shards (act
  42's dispatch-only exclusion shards included) and the probe aggregate (job 111642971554) each concluded `success`;
- the Mathlib bridge built `OIBridge.CompositeInterface` (3631 build jobs);
- each of the 64 frozen `#print axioms` lines of `CompositeInterface` reports `[propext, Classical.choice, Quot.sound]`;
- the release gate passed every step: `lean-axioms` 5616 named results, the 5552 at `D` and the 64 new prints, no
  `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 31 receipts holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| chart vocabulary | `isEffectOn_unitEff`, `isEffectOn_unitEff_sub`, `affine_sum_apply`, `affine_eval`, `affine_expand`, `boundedAffine_of_isCompact`, `exists_effect_rescale`, `exists_effect_neg` | proved; control N2 |
| structures | `ProductData`, `PreComposite`, `Composite`, `LocallyTomographic`, `SharpReadout` | elaborated; controls S3, S6 |
| operations | `attach`, `margA`, `condA`, `readout`, `JointReversible`, `minBody`, `maxBody`, `attach_combo`, `margA_combo`, `prodEff_expand`, `eff_condA` | proved; control S5 |
| laws | `margA_prodState`, `margA_attach`, `eff_margA`, `margA_mem`, `readout_sum`, `isEffectOn_readout`, `sum_eq_unitEff_of_affineSpan`, `readout_prodState`, `readout_attach`, `condA_mem`, `condA_prodState`, `jointReversible_words`, `isEffectOn_readout_seedTransport`, `minBody_subset`, `subset_maxBody`, `nonempty_of` | proved; controls S5, S7, S8 |
| separation | `Composite.pairing_injective` | proved; controls S2, S7 |
| extremal bodies | `isEffectOn_minBody`, `unit_eq_one_minBody`, `minPre`, `maxBody_convex`, `isEffectOn_maxBody`, `maxPre` | proved; control S3 |
| model | `Model.hom_zero` … `Model.modelData_ext` (18 prints), `prodEff_eq_of_eff_eq`, `Model.minComposite`, `Model.maxComposite` | proved; controls S2, S4 |
| instances | `simplex_isCompact`, `zero_mem_ball3`, `vec10_mem_simplex`, `bitComposite`, `ball3MinComposite`, `ball3MaxComposite`, `bitComposite_nonempty`, `ball3MinComposite_nonempty`, `ball3Min_subset_ball3Max` | proved; control S9 |
| padding | `padEff_apply`, `paddedPre`, `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre`, `paddedBall3`, `not_locallyTomographic_paddedBall3`, `no_composite_over_paddedBall3` | proved; controls S2, S9 |
| verdict | `comp1_core` | proved; controls S2, S4 |

## Design evidence

The design runs before `F` are recorded in the preregistration: run 37261154814 on `claude/comp1-dev3` `d8e6d384`
from `D` and the predicted execution tree `8e294cb4` with run 37262395333 (all 32 jobs `success` in each); runs
37234667174, 37235206086 and 37236372977 on TRB-1's landing are the module's repair history. They are design evidence,
not attestations, and the pull-request runs on this branch are not attestations.

## What stays open

A source of a composite larger than the minimal body; local tomography of any composite built from the observer's own
stage towers; the stage-level product of two towers and its completion; readout with state update; a nonlocal
reversible action and a common NOT on a composite; the dimension selector.
