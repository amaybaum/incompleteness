# Reconstruction round CMP-1 — the stage completion, SC∞ and the binary visible scope: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round CMP-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-cmp-1-completion/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-cmp-1-completion/
record AM verification/receipts/CMP-1.json
execution A verification/lean-mathlib/OIBridge/StageCompletion.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/CMP-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, and no other round's record
change under any outcome.**

## The objects

- **`D`** = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, the head of `main` after `OG-1` landed (push run
  36973928206, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as the common
  base of this wave.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file. The drafting
  lineage is linear on the first-parent chain: `D` → `0ee9e531` (initial draft) → `69c960bc` (the frozen
  surface, controls and evidence ledger, committed before any outcome of the predicted execution tree was read) → `F`
  (this revision, which adds the predicted execution tree). Every commit of the lineage changes only this file.
  `F`'s own identity is recorded outside this file, at its exact-head run.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them. A sibling round of this wave
  (`IIP-1`, pull request #781) is drafted from the same `D`; whichever lands second reconciles against the `main` the
  first produced.

## What the round is

The completion, body and effect-family interface that the orbit route consumes, made precise in the field-neutral
vocabulary of `KInfFoundations`, with every premise a named proposition and none sourced. It does not depend on any
geometry result.

- **Directed stages.** A directed system of `FiniteStage`s with functorial forward maps on effects and preparations
  that carry the unit to the unit.
- **SC∞**, `SCInf D`: every forward map carries the probability table. A named predicate, not a structure field, so
  that it can fail.
- **The completion body.** The completion value of a stage effect at a stage preparation is read at a chosen common
  upper stage; under SC∞ it is the value read at any common upper stage. The preparation vectors live in `ℓ^∞` over
  the stage effects, and the body is the closed convex hull of the preparation vectors.
- **The effect-family interface.** The coordinate functionals of all stage effects. Every one is an effect on the
  completion body with no premise; the unit coordinates equal one on it.
- **The sharp seed on the completion.** Under SC∞, a stage effect certain at one stage preparation and zero at another
  is a sharp seed (`OrbitGeneration.SharpSeed`) on the completion body, and its certain state is a boundary state.
- **The binary-visible condition**, `BinaryVisible D` (ELEM-bin): every stage carries a binary visible test and the
  forward maps carry the visible outcomes to the visible outcomes. Under it the visible test is a test on the whole
  completion body, without SC∞; with SC∞ a sharp visible pair is perfectly distinguishable by the two visible
  coordinates.
- **Finite rank and the chart.** `FiniteRank Ω`: the affine span of the body is finite-dimensional. A nonempty body of
  finite rank has an injective affine chart from coordinates whose range is its affine span — the input that
  `OrbitNormalization.hypotheses_restrict` takes.
- **Controls.** A two-stage system violating SC∞ in which two common upper stages give different values; and the
  constant classical-bit tower, on which SC∞, ELEM-bin and the sharp completion seed all hold.

### The elementary-system scope

| part | status in CMP-1 |
|---|---|
| ELEM-bin, a binary visible alphabet carried through the stages | formalized as `BinaryVisible`, and proved and used here |
| ELEM-vis, the body read on the visible factor alone, with no ancilla or hidden readout | a deferred operational requirement; not formalized in CMP-1 |
| the full elementary-system scope ELEM | not defined by this round |

`BinaryVisible` is necessary, not sufficient, for the eventual elementary-system condition. Stating the visible-factor
requirement needs available transformations, which the field-neutral vocabulary does not have. The bare name ELEM is
reserved for a later operational round that can express the whole scope; no declaration of this round is named
`ELEM`, and the result note states that `BinaryVisible` is necessary but not sufficient.

### In scope

1. `StageCompletion`, a new module carrying the definitions, theorems and controls above.
2. The census family entry for the module, `kernel-only`, carried by no manuscript, inserted directly after the landed
   `OG-1` family ("conditional orbit-generation infrastructure …").
3. The import line `import OIBridge.StageCompletion`, inserted directly after the landed line
   `import OIBridge.OrbitNormalization`.

### Frozen out

Any source of SC∞, `BinaryVisible` or finite rank in an OI construction; any formalization of ELEM-vis or of the full
elementary-system scope; the drive and its operational form; V4′;
P2 beyond the stage-effect family; any ball, ellipsoid, transitivity or dimension statement; compactness of the
completion body; any manuscript or roadmap edit.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

The design theorem identity is the statement surface of `StageCompletion` embedded in `controls.py` (blob
`b5b27f1a45805f1c0b5b2cc03b9370ba30d1d598`). It consists of:

- the preamble (imports, namespaces, `open`);
- every context line (`variable`, `open`, `namespace`, `attribute`, `end`), in order;
- the 53 declarations, in order and by kind;
- every theorem's signature up to `:=`;
- every definition, abbreviation and structure, whole;
- the 15 `#print axioms` lines.

The reference module is blob `4df7bc6da9d6294128a99913eab7f8cf80d17202` (`claude/cmp1-dev` at `1172187c`). A
repair may change proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.StageCompletion` inserted directly
after `import OIBridge.OrbitNormalization`. The census is `D`'s with one family, embedded in `controls.py`, inserted
directly after the OG-1 family. Both insertions are placed relative to the landed baseline only.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| WD | `val_eq_at` | `SCInf D →` the completion value of `a` at `x` equals the table value at any common upper stage `k` |
| EFF | `stageEffects_isEffectOn` | every member of `stageEffects D` is an effect on `body D`, with no premise |
| UNIT | `coord_unit_eq_one` | the unit coordinate of every stage equals one on `body D`, with no premise |
| SEED | `sharpSeed_completion`, `boundary_completion` | `SCInf D →` a stage effect with value 1 at `x1` and 0 at `x0` gives `SharpSeed (body D) (coord D ⟨i, e⟩)`, and its certain state is a boundary state |
| VIS | `visible_test_completion` | `BinaryVisible D →` the two visible coordinates sum to one on `body D`, without SC∞ |
| PD | `perfectlyDistinguishable_visible` | with SC∞ and `BinaryVisible D`, a sharp visible pair is perfectly distinguishable on `body D` by the two visible coordinates |
| RANK | `exists_chart_of_finiteRank` | a nonempty `Ω` with `FiniteRank Ω` has an injective chart `w ↦ L w + p0` whose range is `affineSpan ℝ Ω` |
| CTRL | `not_scInf_bad`, `bad_values_differ`, `bitTower_scInf`, `bitTower_sharpSeed` | SC∞ fails on `badD` and two common upper stages give the values 1 and 1/2; on the constant bit tower SC∞ holds and the visible outcome is a sharp seed on the completion |
| core | `cmp1_core` | EFF, SEED, VIS, RANK, `¬ SCInf badD`, and the bit-tower control |

### The elementary-system scope, mechanically

| part | status in CMP-1 | how the controls enforce it |
|---|---|---|
| ELEM-bin | formalized as the structure `BinaryVisible`, proved and used | S2 |
| ELEM-vis | a deferred operational requirement, not formalized | S3 |
| the full elementary-system scope ELEM | not defined; the bare name is reserved | S1, S2, S5 |

### Semantic guards (in `controls.py`)

- **S1, no ELEM.** No declaration is named bare `ELEM` (or `Elem`, `elem`).
- **S2, ELEM-bin.** `BinaryVisible` is a structure. Its docstring and the module header state that it is necessary,
  not sufficient, for the elementary-system scope. The header states that the visible-factor requirement is not
  formalized here and that the name ELEM is reserved.
- **S3, ELEM-vis.** No declaration formalizes the visible-factor requirement (`ElemVis`, `VisibleFactor`,
  `NoAncilla`, …).
- **S4, SC∞ named, not sourced.** `SCInf` is a `def`, and `DirectedStages` carries no consistency field. No theorem
  concludes `SCInf`, `BinaryVisible` or `FiniteRank` without it among its hypotheses, except the named controls on
  `bitTower` and `badD`. In the verdict SC∞ appears only as a hypothesis (`SCInf D →`) or as those controls.
- **S5, scope.** No declaration name, theorem conclusion or header claim concerns a ball, an ellipsoid, transitivity,
  a drive, a dimension or V4′. The header carries "nothing defines the full elementary-system scope".

`controls.py`:
- is blob `b5b27f1a45805f1c0b5b2cc03b9370ba30d1d598` (SHA-256
  `1c11c549f5c67fe4a21eae5ccaab2f674e1f9a1e15ac623941db7c6b80c4898a`, 616 lines), held on the disposable branch
  `claude/cmp1-controls` at `61cd2793`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 23 checks. Its 11 mutation controls each fail with their named code:
  - a removed declaration (N1);
  - a changed binder context (N2);
  - a `sorry` (N3);
  - a bare `ELEM` declaration (S1);
  - the not-sufficient qualifier dropped (S2);
  - a visible-factor definition (S3);
  - SC∞ made a structure field, and SC∞ concluded for every system (S4, twice);
  - a ball claim (S5);
  - a dropped import line;
  - a changed census status.
- `controls.py check <commit> --freeze F` runs P, N1–N3, S1–S5, I, C and F.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`. The kernel build,
the axiom report and the controls' text checks do not substitute for one another. The exact-head run on `F` attests
the frozen control plane and this preregistration only; no row is discharged at `F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| well-definedness | `val_eq_at`, `val_same_stage` | built at `E`; printed axioms within `[propext, Classical.choice, Quot.sound]` | N2, S4 |
| stage-effect interface | `coord_isEffectOn`, `stageEffects_isEffectOn`, `coord_unit_eq_one` | as above | N2 |
| completion seed | `sharpSeed_completion`, `boundary_completion` | as above | N2, S4 |
| ELEM-bin | `visible_test_completion`, `perfectlyDistinguishable_visible` | as above | S2, S4 |
| finite rank | `exists_chart_of_finiteRank` | as above | N2, S4 |
| controls | `not_scInf_bad`, `bad_values_differ`, `bitTower_scInf`, `bitTower_sharpSeed` | as above | S4 |
| verdict | `cmp1_core` | as above | S1–S5 |

## Design evidence

These runs are design evidence, not attestations. For each I read the Mathlib bridge job only.

- **Run 36976697797** (`claude/cmp1-dev`, `8ef0820d`): the bridge failed with 17 elaboration errors — the sigma
  labels not unfolding (`Label` and `Prep` made `abbrev`), scalar multiplication in three convexity proofs, a
  finite-dimensionality instance through `set`, a `decide` on `Bool` order, and the bit-tower table facts and index
  typing. The run was then cancelled.
- **Run 36977252772** (`607bd51d`, repair 1): Mathlib bridge job green.
- **Run 36978262990** (`1172187c`): Mathlib bridge job green on the owner-directed scope — the structure renamed
  `BinaryVisible`, with the necessary-not-sufficient statement and the ELEM reservation. Its log shows each of the 15
  `#print axioms` lines reporting exactly `[propext, Classical.choice, Quot.sound]`, `lean-axioms` 5454 named results
  with no `sorryAx`, and the release gate passing. This module is the reference blob `4df7bc6d`.

### The predicted execution tree

- **`e2c4fe608fa39deec05281d9fd7098f925a8ba35`** (`claude/cmp1-predicted`, a single-parent child of `D`) is the
  execution tree less the result note: this preregistration in its frozen revision `69c960bc`, `controls.py` blob
  `b5b27f1a`, the module blob `4df7bc6d`, `OIBridge.lean` blob `699baa41` and the census family. It contains nothing
  of the sibling round's module (`InvariantInnerProduct`), import or census family.
- At that commit `controls.py check e2c4fe60`, run from the tree's own frozen `controls.py`, passes all 14 checks.
- **Run 36980774530** (`workflow_dispatch` on `e2c4fe60`) completed with conclusion success; every one of its 32 jobs
  succeeded. The Mathlib bridge (job 110754562826) built `OIBridge.StageCompletion` with each of the 15 frozen `#print
  axioms` lines reporting exactly `[propext, Classical.choice, Quot.sound]`, and its release gate passed every step
  (`lean-axioms` 5454 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 23 receipts hold).

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `b5b27f1a`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`CMP-1-COMPLETION-INTERFACE-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the
  exact-head run at `E` is green on every job, the Mathlib bridge building `StageCompletion` with every frozen
  `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The
  result note states that `BinaryVisible` is necessary but not sufficient for the eventual elementary-system
  condition, that ELEM-vis is deferred and unformalized, and that SC∞ is defined, not sourced.
- **`CMP-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources SC∞, `BinaryVisible` or finite rank, or claims to define the full elementary-system scope.
