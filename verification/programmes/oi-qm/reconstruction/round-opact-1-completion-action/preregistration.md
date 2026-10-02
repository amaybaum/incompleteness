# Reconstruction round OPACT-1 — completion-valued operation data and the action they induce on the completed body: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
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


## Outcomes

To be fixed in the freeze revision.
