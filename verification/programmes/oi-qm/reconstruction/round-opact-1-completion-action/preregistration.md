# Reconstruction round OPACT-1 — completion-valued operation data and the action they induce on the completed body: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen surface, the controls, the evidence ledger, the stages and the outcomes below are fixed; the predicted
execution tree is recorded before `F`.

```v3-round
round OPACT-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-opact-1-completion-action/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-opact-1-completion-action/
record AM verification/receipts/OPACT-1.json
execution A verification/lean-mathlib/OIBridge/CompletionAction.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/OPACT-1.json`. Every other path the round changes is an execution path listed
above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, and no other round's record
change under any outcome.**

## The objects

- **`D`** = `254ad0a7f19b3cf6f6ce28e1a7b955f18e4337e4`, the head of `main` after `CMP-1` landed (push run
  37005559751, every job green; the act 42 exclusion matrix skipped on push). The owner designated it as this round's
  base.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file. The drafting
  lineage is linear on the first-parent chain from `D`, and every commit of it changes only this file. `F`'s own
  identity is recorded outside this file, at its exact-head run.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

### The theorem and the premise it exposes

The round proves a bridge: a **completion-valued operation datum** that satisfies **AffineRespect** induces an affine
action on the completed body of `StageCompletion`, read in the chart of a body of finite rank; the action is unique,
preserves the completed body, composes, and, with an inverse datum, is an affine equivalence with `PreservesBody` in
the sense of `OrbitGeneration`.

The round does **not** prove that any operation exists. The operation datum is the premise the round exposes:

- `OpDatum D` carries each stage preparation to a point of the completed body;
- `AffineRespect T`: every finite affine relation among preparation vectors holds among the images,
  `∑ cₓ = 0` and `∑ cₓ • prepVec x = 0` imply `∑ cₓ • τ x = 0`;
- `StateRespect T`: preparations with equal preparation vectors have equal images.

`AffineRespect` implies `StateRespect`; `StateRespect` does not imply `AffineRespect`. The witness is a one-stage
system with three preparations reading `0`, `1/2` and `1`, and the datum exchanging the first preparation and the
midpoint: preparation vectors are pairwise distinct, so it respects states, and it breaks the relation
`x₀ − 2 x_m + x₂ = 0`. `AffineRespect` is the condition under which the induced action exists (EU) and the condition an
affine action forces (NEC), proved as two separate theorems. `StateRespect` occurs in no load-bearing statement.

Inverse availability (`Undoes` in both directions) and finite rank (`FiniteRank`, CMP-1's named predicate) enter as
hypotheses where they are used; neither is sourced here.

### In scope

1. `CompletionAction`, a new module carrying the definitions, theorems and the separation countermodel above.
2. The census family entry for the module, `kernel-only`, carried by no manuscript, inserted directly after the landed
   `CMP-1` family ("the stage completion …").
3. The import line `import OIBridge.CompletionAction`, inserted directly after the landed line
   `import OIBridge.StageCompletion`.

### Frozen out

The existence of any physical operation; a drive, a flow or any one-parameter group of operations; phase or Clifford
generators and any concrete gate; boundary transitivity and K∞-R; the invariant inner product; any dimension
statement; ellipsoid or ball structure; SC∞; closure of `stageEffects` under any operation; the countability
argument for flows; the finite-dimensional duality between the state and effect pictures; any manuscript or roadmap
edit.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement or hypothesis without a new preregistration revision and new design theorem identity.

The design theorem identity is the statement surface of `CompletionAction` embedded in `controls.py` (blob
`7a622a8b10a2349ab92d62557b5e4591e7920935`). It consists of:

- the preamble (imports, namespaces, `open`);
- every context line (`variable`, `open`, `namespace`, `section`, `end`), in order;
- the 62 declarations, in order and by kind;
- every theorem's signature up to `:=`;
- every definition and structure, whole;
- the 16 `#print axioms` lines.

The reference module is blob `8bcab4a5d1d98acdbc18bdba1fbddb43f370ed0c` (`claude/opact1-dev` at `4781824c`). A
repair may change proofs only. `OIBridge.lean` is `D`'s with `import OIBridge.CompletionAction` inserted directly
after `import OIBridge.StageCompletion` (blob `5b4b669dd10ce257d6ef67ca5aca69890339448a`). The census is `D`'s with
one family, embedded in `controls.py`, inserted directly after the CMP-1 family (blob
`f9de143ecb08d839d9e50a379d29a73987ebd982`). The census family carries this round's name and note; the family on the
design branch, written before the round existed, is not the frozen one.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| REL | `stateRespect_of_affineRespect` | `AffineRespect T → StateRespect T` |
| SEP | `midOp_stateRespect`, `midOp_not_affineRespect` | `StateRespect midOp`; `¬ AffineRespect midOp` |
| EXT | `exists_affine_of_relations` | a family `u` satisfying every finite affine relation of a family `v` is the image of `v` under an affine map |
| CHART | `exists_completionChart` | `(body D).Nonempty → FiniteRank (body D) → Nonempty (CompletionChart D)` |
| SPAN | `chartBody_subset`, `affineSpan_gen` | the chart body lies in the closed convex hull of the chart generators, and the generators affinely span the chart |
| EU | `existsUnique_induced` | `AffineRespect T →` exactly one affine map `Φ` of the chart with `Φ (gen C x) = coordsOf C (T.τ x)` |
| NEC | `affineRespect_of_induced` | an affine map of the chart with those values forces `AffineRespect T` |
| BODY | `induced_mem` | `AffineRespect T →` the induced map carries `chartBody C` into itself |
| COMP | `induced_after` | the map induced by `S` after `T` is the composite of the induced maps |
| INV | `comp_eq_id`, `preservesBody_inducedEquiv` | with `Undoes C S T hS` and `Undoes C T S hT`, the induced map is an affine equivalence `e` with `PreservesBody (chartBody C) {e}` |
| EFF | `isEffectOn_pullback` | a stage effect read after the induced map is an effect on `chartBody C` |
| core | `opact1_core` | REL, SEP, CHART, EU, NEC, BODY, INV |

The verdict bundles seven rows; COMP, EFF, EXT and SPAN are frozen surface with axiom prints outside the verdict.

### Semantic guards (in `controls.py`)

- **S1, premise strength.** Every load-bearing theorem and construction of the action (`gen_relation`,
  `exists_induced`, `existsUnique_induced`, `induced`, `induced_gen`, `induced_mem`, `after`, `comp_gen`,
  `affineRespect_after`, `induced_after`, `Undoes`, `comp_eq_id`, `inducedEquiv`, `inducedEquiv_apply`,
  `inducedEquiv_symm_apply`, `preservesBody_inducedEquiv`, `isEffectOn_pullback`) carries `AffineRespect` among its
  hypotheses and never `StateRespect`. `exists_affine_of_relations` carries its affine-relation hypothesis.
  `StateRespect` occurs only in its definition, in `stateRespect_of_affineRespect`, in `midOp_stateRespect` and twice
  in the verdict.
- **S2, separation.** `midOp_stateRespect : StateRespect midOp` and `midOp_not_affineRespect : ¬ AffineRespect midOp`
  are stated exactly and printed; the verdict carries `StateRespect midOp ∧ ¬ AffineRespect midOp` and
  `AffineRespect T → StateRespect T`.
- **S3, structure.** `inducedEquiv`, `inducedEquiv_symm_apply` and `preservesBody_inducedEquiv` carry both
  `(hST : Undoes C S T hS)` and `(hTS : Undoes C T S hT)`; no theorem concludes `PreservesBody` without them.
  `exists_completionChart` carries `(hne : (body D).Nonempty)` and `(hfr : FiniteRank (body D))`; the verdict carries
  the chart clause under both, and each of its four chart-level clauses quantifies a `CompletionChart`.
- **S4, downstream neutrality.** No declaration name, conclusion or line of code mentions a drive, a flow or a
  one-parameter group of operations, transitivity, an invariant inner product, a dimension, a ball or an ellipsoid,
  SC∞, countability, a concrete gate or phase, or `stageEffects`; the only concrete `OpDatum` is the countermodel
  `midOp`.
- **S5, header.** The header carries "Nothing here supplies an operation datum, a flow, transitivity, an invariant
  inner product, a dimension or a ball, and nothing uses SC∞."

`controls.py`:
- is blob `7a622a8b10a2349ab92d62557b5e4591e7920935` (SHA-256
  `0af3c86b16e3b760326a8863a0eb01936289d3f8cb85645e0c6d5c28e17850d6`, 706 lines), held on the disposable branch
  `claude/opact1-controls` at `d5cfa1d2`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 27 checks. Its 15 mutation controls each fail with their named code:
  - a removed declaration (N1), a changed binder context (N2), a `sorry` (N3);
  - `AffineRespect` replaced by `StateRespect` in body preservation, the affine-relation hypothesis removed from the
    extension theorem, and a load-bearing theorem stated under `StateRespect` (S1, three times);
  - the separation witness weakened to `¬ StateRespect midOp` (S2);
  - inverse availability dropped from `PreservesBody`, and `FiniteRank` removed from the chart theorem (S3, twice);
  - a one-parameter group of operations, a `stageEffects` closure claim, and a concrete operation datum (S4, three
    times);
  - the disclaimer dropped (S5);
  - a dropped import line; a changed census status.
- `controls.py check <commit> --freeze F` runs P, N1–N3, S1–S5, I, C and F.

## Downstream design constraints

Recorded for the rounds that will consume this bridge (DRIVE and the effect-generation round P2). They are
constraints on those rounds' freezes, not claims of this round, and nothing in this round's surface states them.

1. A continuous downstream drive acts on the completed body. It is not required to map completed states back to stage
   preparations, or completed effects back to `stageEffects`.
2. The available-effect family of P2 is a family of completed effects; closure of `stageEffects` under a continuous
   group is not a premise any later freeze may preregister.
3. Operations sourced later are delivered with `AffineRespect` (or a premise from which it follows), not with
   `StateRespect` alone.
4. Continuity of a flow is stated in the chart of a body of finite rank.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`. The kernel build,
the axiom report and the controls' text checks do not substitute for one another. The exact-head run on `F` attests
the frozen control plane and this preregistration only; no row is discharged at `F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| respect conditions | `stateRespect_of_affineRespect`, `midOp_stateRespect`, `midOp_not_affineRespect` | built at `E`; printed axioms within `[propext, Classical.choice, Quot.sound]` | N2, S1, S2 |
| affine extension | `sum_smul_affine`, `exists_affine_of_relations` | as above | N2, S1 |
| chart | `exists_completionChart`, `chartBody_subset`, `affineSpan_gen` | as above | N2, S3 |
| induced action | `existsUnique_induced`, `affineRespect_of_induced`, `induced_mem` | as above | N2, S1 |
| composition | `induced_after`, `comp_eq_id` | as above | N2, S1 |
| reversibility | `preservesBody_inducedEquiv` | as above | N2, S1, S3 |
| effect pullback | `isEffectOn_pullback` | as above | N2, S1, S4 |
| verdict | `opact1_core` | as above | S1–S5 |

## Design evidence

These runs are design evidence, not attestations. For each I read the Mathlib bridge job.

- **Run 37011255825** (`claude/opact1-dev`, `7cbb923a`): the bridge failed with seven errors — a conjunction expected
  where `simp` left an equation, an unknown lemma name for applying a sum of affine maps, and five evaluation failures
  in the countermodel. The run completed with the bridge job failed.
- **Run 37011853989** (`601ff5c5`, repair 1): 13 of the 16 printed axiom sets standard; the two countermodel theorems
  and the verdict failed. Repair 1 proved the kernel inclusion by components, applied the affine map definitionally,
  and re-indexed the countermodel to the readings `0`, `1/2`, `1` (the definitions `midStage` and `midSwap`).
- **Run 37012251866** (`213f00cb`, repair 2): 14 of 16 standard; one type ascription failed in
  `midOp_stateRespect`. Repair 2 named the relation coefficients.
- **Run 37013353037** (`4781824c`, repair 3): completed with conclusion success; every one of its 32 jobs succeeded.
  The Mathlib bridge (job 110858169641) built `OIBridge.CompletionAction` with each of the 16 `#print axioms` lines
  reporting exactly `[propext, Classical.choice, Quot.sound]`, and its release gate passed every step (`lean-axioms`
  5491 named results, no `sorryAx`; 303 legacy records intact; 25 receipts hold). This module is the reference blob
  `8bcab4a5`.
- Across the four commits no theorem statement changed; `OpDatum`, `StateRespect`, `AffineRespect`,
  `CompletionChart` and every substantive statement are unchanged. Repair 1 changed the two countermodel definitions;
  repairs 2 and 3 only added helper definitions and lemmas.

### The predicted execution tree

- **`ca2daeeb61efe6e2d87d000dc493109777d8d65b`** (`claude/opact1-predicted`, a single-parent child of `D`) is the
  execution tree less the result note. Its files and blobs:
  - this preregistration in its frozen revision `07266ae7`, blob `611547b3`;
  - `controls.py`, blob `7a622a8b`;
  - `CompletionAction.lean`, blob `8bcab4a5`;
  - `OIBridge.lean`, blob `5b4b669d`;
  - the census, blob `f9de143e`.
- `delta(D, ca2daeeb)` is exactly those five paths: the record directory's two files and the three execution paths.
  It adds no drive, flow or effect-generation module, and no file other than these.
- At that commit `controls.py check ca2daeeb`, run from the tree's own frozen `controls.py`, passes all 14 checks.
- **Run 37018873171** (`workflow_dispatch` on `ca2daeeb`) completed with conclusion success; every one of its 32 jobs
  succeeded. The Mathlib bridge (job 110876494408) built `OIBridge.CompletionAction` with each of the 16 frozen
  `#print axioms` lines reporting exactly `[propext, Classical.choice, Quot.sound]`, and its release gate passed every
  step (`lean-axioms` 5491 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 25 receipts
  hold).

These runs are design evidence, not attestations.

## Stages

1. **C1** adds `controls.py`, blob `7a622a8b`, to the record directory. Acceptance: the blob is the frozen blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change proofs only; each passes `controls.py check` at its commit. A failure
   that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   and the exact-head run at `E` has every job green.

## Outcomes

- **`OPACT-1-COMPLETION-ACTION-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`, and the exact-head
  run at `E` is green on every job, the Mathlib bridge building `CompletionAction` with every frozen `#print axioms`
  reporting a subset of `[propext, Classical.choice, Quot.sound]` and the release gate passing. The result note
  states that the round proves the completion action of an operation datum under `AffineRespect` and does not source
  any operation, and that `StateRespect` is strictly weaker.
- **`OPACT-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome sources an operation, a flow, transitivity, an invariant inner product, a dimension or a ball, or claims
closure of `stageEffects` under any operation.
