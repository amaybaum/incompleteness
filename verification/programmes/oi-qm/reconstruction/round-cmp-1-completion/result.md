# Reconstruction round CMP-1 — the stage completion, SC∞ and the binary visible scope: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #782.

- **`D`** — `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, the head of `main` after `OG-1` landed, certified by push
  run 36973928206.
- **`F`** — `f81050617142bc1c9bc26c4e78e96cafbe00b7df`, parent `69c960bc42aaacecdaadafb05b6c970d2acf6ec6`;
  `delta(D, F)` is the preregistration alone, blob `6c0ec8e203ce069e63c5a54fac1679852488310a`. Its exact-head
  `workflow_dispatch` run 36983545819 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `CMP-1-COMPLETION-INTERFACE-PROVED`

In the kernel, in the field-neutral vocabulary of `KInfFoundations`, with SC∞ (`SCInf`), the binary-visible condition
(`BinaryVisible`) and finite rank (`FiniteRank`) stated as named propositions and proved for no OI construction:

- **directed stages and the completion value** (`val_eq_at`): for a directed system of finite stages with forward
  maps carrying the unit to the unit, the completion value of a stage effect at a stage preparation is read at a
  chosen common upper stage; under SC∞ it equals the value read at any common upper stage;
- **the effect-family interface** (`stageEffects_isEffectOn`, `coord_unit_eq_one`): on the completion body, the closed
  convex hull of the preparation vectors in `ℓ^∞` over the stage effects, the coordinate functional of every stage
  effect is an effect and every unit coordinate equals one, with no premise;
- **the completion seed** (`sharpSeed_completion`, `boundary_completion`): under SC∞, a stage effect with value one at
  one stage preparation and zero at another is a sharp seed on the completion body, and its certain state is a
  boundary state;
- **ELEM-bin** (`visible_test_completion`, `perfectlyDistinguishable_visible`): under `BinaryVisible`, the two visible
  coordinates of every stage sum to one on the whole completion body, without SC∞; with SC∞ as well, a sharp visible
  pair is perfectly distinguishable by them;
- **finite rank** (`exists_chart_of_finiteRank`): a nonempty body of finite rank has an injective affine chart from
  coordinates whose range is its affine span, the input of `OrbitNormalization.hypotheses_restrict`;
- **controls** (`not_scInf_bad`, `bad_values_differ`, `bitTower_scInf`, `bitTower_binaryVisible`,
  `bitTower_sharpSeed`): on a two-stage system SC∞ fails and two common upper stages give the values 1 and 1/2; on the
  constant classical-bit tower SC∞ and `BinaryVisible` hold and the visible outcome is a sharp seed on the completion;

joined in the verdict `cmp1_core`.

`BinaryVisible` is necessary, not sufficient, for the eventual elementary-system condition. ELEM-vis, the body read
on the visible factor alone with no ancilla or hidden readout, is a deferred operational requirement and is not
formalized. The full elementary-system scope is not defined by this round, and no declaration is named `ELEM`. SC∞ is
defined, not sourced: the round derives neither SC∞, nor `BinaryVisible`, nor finite rank from any OI construction. It
claims no ball, ellipsoid, transitivity, dimension, drive or V4′, no compactness of the completion body, and it edits
no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `f8105061` | the preregistration | 36983545819 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5439, as at `D` |
| `C1` = `6c96d568` | stage C1: `controls.py`, blob `b5b27f1a` | none required | `controls.py --self-test`: `controls: OK -- 23 checks` |
| `S1` = `ed7078e8abb7373db2b7bf623d15fe813d0b7998` | stage S1: `StageCompletion` blob `4df7bc6d`, the import line, the census family | 36987454767 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `e2c4fe60`
outside the preregistration, and contains nothing of the sibling round `IIP-1`. `controls.py check S1 --freeze F`
prints `controls: OK -- 16 checks`.

Run 36987454767 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check (job 110775621953), the Mathlib bridge (job 110775622188), the 29 numerical-probe shards (act 42's
  dispatch-only exclusion shards included) and the probe aggregate (job 110783787939) each concluded `success`;
- the Mathlib bridge built `OIBridge.StageCompletion` (3618 build jobs);
- each of the 15 frozen `#print axioms` lines of `StageCompletion` reports `[propext, Classical.choice, Quot.sound]`;
- the release gate passed all 21 steps: `lean-axioms` 5454 named results, the 5439 at `D` and the 15 new
  prints, no `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 23 receipts
  holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| well-definedness | `val_eq_at`, `val_same_stage` | proved; controls N2, S4 |
| stage-effect interface | `coord_isEffectOn`, `stageEffects_isEffectOn`, `coord_unit_eq_one` | proved; control N2 |
| completion seed | `sharpSeed_completion`, `boundary_completion` | proved; controls N2, S4 |
| ELEM-bin | `visible_test_completion`, `perfectlyDistinguishable_visible` | proved; controls S2, S4 |
| finite rank | `exists_chart_of_finiteRank` | proved; controls N2, S4 |
| controls | `not_scInf_bad`, `bad_values_differ`, `bitTower_scInf`, `bitTower_sharpSeed` | proved; control S4 |
| verdict | `cmp1_core` | proved; controls S1–S5 |

| part of the elementary-system scope | status |
| --- | --- |
| ELEM-bin | formalized as `BinaryVisible`; proved and used |
| ELEM-vis | deferred operational requirement; not formalized |
| the full scope ELEM | not defined; the bare name is reserved |

## A misattributed identifier in the preregistration

The preregistration's paragraph on the predicted execution tree lists its contents as "this preregistration in its
frozen revision `69c960bc`, `controls.py` blob `b5b27f1a`, the module blob `4df7bc6d`, `OIBridge.lean` blob
`699baa41` and the census family". Blob `699baa41` is the preregistration at `69c960bc`, not `OIBridge.lean`; the
`OIBridge.lean` of the predicted execution tree, and of `S1`, is blob `2a5a0dc5`, which is `D`'s with exactly the
frozen import line (control I). The sentence is descriptive design evidence, and no stage acceptance reads it; the
preregistration is left as frozen.

## Design evidence

The design runs before `F` are recorded in the preregistration, ending with the reference blob `4df7bc6d` and the
predicted execution tree `e2c4fe60` with run 36980774530 (all 32 jobs `success`). They are design evidence, not
attestations, and the pull-request runs on this branch are not attestations.

## What stays open

A source of SC∞, of `BinaryVisible` and of finite rank in an OI construction; ELEM-vis and the full elementary-system
scope, which need available transformations; compactness of the completion body; the drive, boundary transitivity,
dimension three and V4′.
