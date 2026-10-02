# Reconstruction round CMP-1 — the stage completion, SC∞ and the binary visible scope: PREREGISTRATION

**Status: drafting.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted on its
pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
Sections marked *to be frozen* are completed before `F` from the design runs recorded below.

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
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
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
- **ELEM-bin**, `ElemBinary D`: every stage carries a binary visible test and the forward maps carry the visible
  outcomes to the visible outcomes. Under ELEM-bin the visible test is a test on the whole completion body, without
  SC∞; with SC∞ a sharp visible pair is perfectly distinguishable by the two visible coordinates.
- **Finite rank and the chart.** `FiniteRank Ω`: the affine span of the body is finite-dimensional. A nonempty body of
  finite rank has an injective affine chart from coordinates whose range is its affine span — the input that
  `OrbitNormalization.hypotheses_restrict` takes.
- **Controls.** A two-stage system violating SC∞ in which two common upper stages give different values; and the
  constant classical-bit tower, on which SC∞, ELEM-bin and the sharp completion seed all hold.

### The elementary scope: what is and is not defined

The elementary scope ELEM has two clauses. Only the first is defined here.

- **ELEM-bin** (defined): a binary visible alphabet carried through the stages.
- **ELEM-vis** (not defined here): the body is read on the visible factor alone — every available effect is a visible
  readout after an available transformation, with no ancilla or hidden readout. Stating it needs available
  transformations, which the field-neutral vocabulary does not have. It stays a named open clause and is not baked
  into any theorem of this round; no theorem here assumes or concludes it.

### In scope

1. `StageCompletion`, a new module carrying the definitions, theorems and controls above.
2. The census family entry for the module, `kernel-only`, carried by no manuscript, inserted directly after the landed
   `OG-1` family ("conditional orbit-generation infrastructure …").
3. The import line `import OIBridge.StageCompletion`, inserted directly after the landed line
   `import OIBridge.OrbitNormalization`.

### Frozen out

Any source of SC∞, ELEM-bin, ELEM-vis or finite rank in an OI construction; the drive and its operational form; V4′;
P2 beyond the stage-effect family; any ball, ellipsoid, transitivity or dimension statement; compactness of the
completion body; any manuscript or roadmap edit.

## The declarations, the controls, the stages and the outcomes

*To be frozen* from the design runs: the module text (its declaration list with frozen statements and definitions),
the `controls.py` blob and its checks, the execution stages and their acceptance, and the outcome labels with their
mechanical rule.
