# Reconstruction round K2-GUARD-1 — two interface facts of the composite route: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The two questions, the two decision rules, the non-inference rule, the frozen surface, the controls, the evidence
ledger, the stages and the outcomes below are fixed; the predicted execution tree is recorded before `F`.

```v3-round
round K2-GUARD-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k2-guard-1-interface/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k2-guard-1-interface/
record AM verification/receipts/K2-GUARD-1.json
execution A verification/lean-mathlib/OIBridge/K2Guard.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

The record directory holds this preregistration, the round's frozen controls `controls.py` and the result note. The
receipt path is `verification/receipts/K2-GUARD-1.json`. Every other path the round changes is an execution path
listed above. **No manuscript, no built artifact, `verification/ROADMAP.md`, the workflow, no probe and no other
round's record change under any outcome.**

## The objects

- **`D`** = `8daf2bc0ad9c4fe4e9ae422b3a9a010a80ab9e53`, the head of `main` after the ROADMAP change #799 landed (merge
  of `4906c06a`; the push run 37457928970 at `D` succeeded, the act 42 exclusion matrix skipped on push).
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

Two independent questions about the composite route at the elementary ball, each read from the kernel statements by
its own frozen decision rule. Neither rule reads the other's statements, and neither outcome depends on the other.

- **Q-ORIENTATION.** Take the candidate-cone family of two copies of `eball 3`: the sets `K` of joint vectors with
  every product state of the ball in `K` and `K ⊆ maxCone (eball 3)` (`CandidateCone`). This is the family the
  read-only K2 thread identified between the product states and DIM-1's maximal cone; the convex cones between the
  minimal and the maximal cone are members of it. Is any member invariant under both DIM-1's gate `cnot` and the
  reflection `reflY = diag(1, −1, 1)` acting on the second copy alone (`actT reflY`)?
- **Q-ENTANGLING.** Does DIM-1's dimension selector, and K1-BRIDGE-1's relative selector, give `d = 3` with `2 ≤ d` in
  place of the entangling clause?

The earned reading of a positive Q-ORIENTATION cell is only this: a composite route that admits the named gate `cnot`
and chooses its cone from the frozen candidate family cannot also admit the one-copy reflection `reflY` as a
reversible symmetry. The earned reading of a positive Q-ENTANGLING cell is only this: the entangling clause is
sufficient to exclude `d = 1` under DIM-1's hypotheses, and the dimension conclusion consumes only `2 ≤ d`.

### The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-ORIENTATION | `K2-ORIENTATION-OBSTRUCTION-PROVED` | all of: `reflY` is the linear map `x ↦ (i ↦ ![1, −1, 1] i * x i)`; `CandidateCone K` is `(∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)`; a theorem `no_candidateCone_cnot_reflY` whose explicit binders are exactly `(hK : CandidateCone K) (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K)` with conclusion `False`; and every orientation control below is a theorem with its frozen conclusion |
| Q-ORIENTATION | `K2-ORIENTATION-NOT-ESTABLISHED` | otherwise |
| Q-ENTANGLING | `K1-ENTANGLING-WEAKENED` | all of: a theorem `three_of_nativeGate_of_two_le` whose explicit binders are exactly `(hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)` with conclusion `d = 3`; a theorem `three_of_nativeGateOf_of_two_le` whose explicit binders are exactly `(hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)`, OG-1's four hypotheses, `(hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)` with conclusion `d = 3`; neither statement mentions `Entangling`; and the control `two_le_load_bearing` with its frozen conclusion |
| Q-ENTANGLING | `K1-ENTANGLING-NOT-WEAKENED` | otherwise |

The round's outcome is `K2-GUARD-1-READ` when both cells are assigned, each by its own rule. The design runs below
already exhibit a module read by these rules as `K2-ORIENTATION-OBSTRUCTION-PROVED` and `K1-ENTANGLING-WEAKENED`; the
rules, not that reading, are what this file freezes, and the cells at `E` are those `controls.py verdict E` prints.

### The orientation controls (frozen conclusions)

The obstruction must come from the joint invariance requirement, not from an empty family or a malformed gate. The
controls are exactly what the K2 thread's exact probe certifies, stated in the kernel:

| Control | Theorem | Frozen conclusion |
|---|---|---|
| the gate is DIM-1's native gate | `nativeGate_cnot` (landed), in the verdict | `NativeGate (eball 3) z3 nflip cnot` |
| `reflY` is a body map of the ball and a reflection | `reflY_mem_eball`, `det_reflY` | `reflY x ∈ eball 3`; `LinearMap.det reflY = -1` |
| `nflip` is a rotation | `det_nflip` | `LinearMap.det nflip = 1` |
| a `cnot`-invariant candidate cone exists | `candidateCone_cnotOrbit`, `cnot_mem_cnotOrbit` | `CandidateCone cnotOrbit`; `cnot ω ∈ cnotOrbit` (the products with their `cnot` images) |
| a `reflY`-invariant candidate cone exists | `candidateCone_productSet`, `reflY_mem_productSet` | `CandidateCone productSet`; `actT reflY ω ∈ productSet` (the products) |
| the chain and its value | `chain_eq`, `chain_value` | `cnot (actT reflY (cnot (prodState xplus z3))) = chainW`; the product of the sharp effects along `−e₁` and `−e₃` on `chainW` is `−1/2` |
| the rotation control | `rotation_chain_value` | with `nflip` in place of `reflY` the same value is `0` |

The `cnot`-invariant member `cnotOrbit` is the `cnot`-orbit of the product states; it is the generating set of the
K2 thread's cone `C_H` restricted to `cnot`, not `C_H` itself, which this round does not state.

### The non-inference rule (frozen)

> This round does not derive local tomography; does not identify the physical composite cone; does not derive the
> product-test structure; does not source K∞-Act; does not source a continuous or dense family of reversible
> operations; does not adopt a topological closure of the available operations; does not derive K∞-Copy; does not
> show that every theory excludes one-copy reflections; does not derive `2 ≤ d` from OI; does not discharge K2; and
> does not alter H-Bell. It states no implication from `2 ≤ d` to the entangling clause and no equivalence between
> them.

After this round the dimension path reads `NativeGateOf` with `2 ≤ d` gives `d = 3`; where `2 ≤ d` comes from remains
open. The result note states each cell in the words of its row, and both earned readings above, and nothing stronger.

### In scope
- the module `OIBridge/K2Guard.lean` with the statement surface of §"The frozen surface";
- its import line in `OIBridge.lean` and its family in `lean-manuscript-census.json`;
- `controls.py` and the result note.

### Frozen out
- any statement about a cone other than the frozen candidate family, about a gate other than `cnot`, or about a local
  map other than `reflY` and `nflip`; any statement that a cone is the physical one;
- any source of `2 ≤ d`, of a local action, of a dense or continuous family of reversible operations, of a closure, of
  K∞-Copy, and any statement that OI supplies them;
- a limit closure, a drive or flow, a complex or matrix representation of the state space, the qubit's operator effects;
- any edit to `CompositeDimension`, `EffectSpace`, `K1Bridge`, `CompositeInterface`, a manuscript,
  `verification/ROADMAP.md`, the DIM-1, EFF-1 or K1-BRIDGE-1 records, or any other round's record.

## The frozen surface

**Design-run rule:** compilation failures may cause implementation repairs, but no repair may strengthen or weaken a
frozen theorem statement, definition or hypothesis without a new preregistration revision and new design theorem
identity.

The design theorem identity is the statement surface of `K2Guard` embedded in `controls.py` (blob
`d33086bb5560ed979f808ab2ec953f364dacd21d`): the preamble (the import, namespaces, `open` lines, `variable {d : ℕ}`), the context blocks in
order, the 46 declarations in order and by kind, every theorem's signature up to `:=`, every definition whole, and the
19 `#print axioms` lines. The reference module is blob `ec8ba57b178561c81b082404ceb02241ada1fe1e`. A repair may change theorem proofs only.
`OIBridge.lean` is `D`'s with `import OIBridge.K2Guard` inserted directly after `import OIBridge.K1Bridge`. The census
is `D`'s with one family, embedded in `controls.py`, inserted directly after the K1-BRIDGE-1 family (modules
`["K1Bridge"]`), in `D`'s two-space JSON layout.

### The principal statements

| Row | Identifier | Statement |
|---|---|---|
| REFL | `reflY`, `reflY_mem_eball`, `det_reflY`, `det_nflip` | `reflY x = (i ↦ ![1, −1, 1] i * x i)`; it maps `eball 3` into itself; `LinearMap.det reflY = −1`; `LinearMap.det nflip = 1` |
| FAMILY | `CandidateCone` | `(∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)` |
| CHAIN | `chain_eq`, `chain_value` | `cnot (actT reflY (cnot (prodState xplus z3))) = chainW`; `prodEffVal (sharpEff ![-1, 0, 0]) (sharpEff ![0, 0, -1]) chainW = -1 / 2` |
| Q-ORIENTATION | `no_candidateCone_cnot_reflY` | `CandidateCone K → (∀ ω ∈ K, cnot ω ∈ K) → (∀ ω ∈ K, actT reflY ω ∈ K) → False`, proved through `chain_eq` and `chain_value` |
| CTL-A | `prodState_mem_maxCone`, `candidateCone_productSet`, `reflY_mem_productSet`, `candidateCone_cnotOrbit`, `cnot_mem_cnotOrbit`, `rotation_chain_value` | product states lie in the maximal cone; the two non-vacuity families; the rotation value `0` |
| Q-ENTANGLING | `three_of_nativeGate_of_two_le`, `three_of_nativeGateOf_of_two_le` | `2 ≤ d`, `IsNot`, `NativeGate` give `d = 3`, through `dim_of_nativeGate`; `2 ≤ d`, effect soundness, the four hypotheses, `IsNot`, `NativeGateOf` give `d = 3`, through `dim_of_nativeGateOf` |
| SUFF | `two_le_of_entangling` | `IsNot`, `NativeGate`, `Entangling` give `2 ≤ d`, through `three_of_nativeGate`; no converse is stated |
| CTL-B | `two_le_load_bearing`, `two_le_satisfiable` | `IsNot (eball 1) z1 neg1 ∧ NativeGate (eball 1) z1 neg1 cnot1 ∧ ¬ (2 ≤ 1)`; `2 ≤ 3 ∧ IsNot (eball 3) z3 nflip ∧ NativeGate (eball 3) z3 nflip cnot` |
| verdicts | `k2guard_orientation`, `k2guard_entangling` | each cell's theorem with its controls, separately |

### Semantic guards (in `controls.py`)

Each lists the mutation controls `--self-test` drives through it, every one of which must fail with the named code.

- **S1 obstruction.** `reflY`, `CandidateCone`, `productSet`, `cnotOrbit`, `idW`, `chainW`, `rotW`, `rotChainW` are the
  frozen texts whole; the obstruction has exactly the frozen explicit binders and conclusion `False` and its proof
  names `chain_eq` and `chain_value`. Mutations: the reflection replaced by a rotation; the family narrowed by an extra
  condition; an extra hypothesis on the obstruction; the obstruction proved without the chain.
- **S2 controls.** Every orientation control is a printed theorem with its frozen conclusion, and the orientation
  verdict has its frozen conclusion. Mutations: the rotation control weakened to `≤ 0`; the determinant control
  dropped from the verdict.
- **S3 selectors.** The two selectors with exactly the frozen explicit binders and conclusion `d = 3`, their proofs
  naming `dim_of_nativeGate` and `dim_of_nativeGateOf`, neither mentioning `Entangling`; `two_le_of_entangling` with
  its frozen statement and no other theorem concluding `2 ≤ d`; the two selector controls with their frozen
  conclusions. Mutations: the entangling clause added to the selector; `2 ≤ d` dropped; the relative selector with
  `0 < d` only; a second theorem concluding `2 ≤ d`.
- **S4 premises.** No theorem concludes `Entangling`, `NativeGateOf`, `EffectsOn`, `SharpSeed`, `PreservesBody`,
  `BoundaryTransitive` or `SeedOrbitAvailable` (in the entangling verdict they occur only as antecedents);
  `NativeGate`, `IsNot` and `CandidateCone` are concluded only by the named controls and the verdicts. Mutations: the
  entangling clause concluded from `2 ≤ d`; a native gate concluded for a hypothesis-bound gate.
- **S5 reuse.** No declaration has the name of a landed object it reads; the only import is `OIBridge.K1Bridge`.
  Mutations: `maxCone` re-declared; a second import.
- **S6 neutral.** No complex, conjugate-transpose, positive-semidefinite, trace, qubit, Bloch, Pauli, density, drive,
  flow, limit, closure, dense-subgroup, tensor-product, Hilbert, mixing-closure or unit-span token. Mutations: a
  complex scalar; a closure.
- **S7 phrases.** The module header and, at a commit carrying it, the result note contain none of the frozen phrases
  (among them "OI supplies", "derived from OI", "local tomography is derived", "physical cone is identified",
  "reflections are physically forbidden", "K2 is discharged", "K∞-Act is sourced", "2 ≤ d implies entangl",
  "equivalent to the entangling", "all composites must preserve orientation", "qubit"; case-insensitive,
  whitespace-normalized). Mutation: "The physical cone is identified." in the header; a note with "reflections are
  physically forbidden" (and a neutral note passes).
- **S8 scope.** The selector section §E mentions no dimension-three object; `2 ≤ d` occurs only in §E, §F and the
  verdicts. Mutations: a dimension-three object in §E; `2 ≤ d` in §A.
- **S9 count.** Exactly the 19 frozen `#print axioms` lines, in order and distinct. Mutations: an extra print; a
  duplicated print.
- **V verdicts.** Each cell yields one outcome by its own rule; at a commit carrying the result note, the note contains
  exactly the two computed tokens and no other. Controls: the reflection replaced by a rotation reads
  `K2-ORIENTATION-NOT-ESTABLISHED` and leaves the entangling cell `K1-ENTANGLING-WEAKENED`; the entangling clause in
  the selector reads `K1-ENTANGLING-NOT-WEAKENED` and leaves the orientation cell `K2-ORIENTATION-OBSTRUCTION-PROVED`;
  the relative selector concluding only `d ∈ {1, 3}` reads `K1-ENTANGLING-NOT-WEAKENED`; a weakened non-vacuity
  control reads `K2-ORIENTATION-NOT-ESTABLISHED`; the note-token reader finds exactly the stated tokens.
- **N1–N3** as K1-BRIDGE-1. **I, C** as K1-BRIDGE-1, with the import after `OIBridge.K1Bridge` and the family after
  K1-BRIDGE-1's.

`controls.py`:
- is blob `d33086bb5560ed979f808ab2ec953f364dacd21d` (1036 lines), generated from the reference tree by `gen_controls.py`;
- was frozen, and this revision committed, before any outcome of the predicted execution tree was read;
- `--self-test` passes 53 checks.

### Count facts

- the module carries **19** frozen `#print axioms` lines (S9) and 46 declarations;
- none of the 19 short names occurs at `D`, so the prints add 19 names to `lean_axiom_check`'s count;
- at `D` the release gate's `lean-axioms` step reports 5743 named results.

## Evidence ledger

Each row is discharged at `E` by the exact-head run at `E` and by `controls.py check E --freeze F`.

| Row | Kernel identifiers | Evidence required at `E` | Control |
|---|---|---|---|
| reflection | `reflY_mem_eball`, `det_reflY`, `det_nflip` | built; axioms within `[propext, Classical.choice, Quot.sound]` | S1, S2 |
| chain | `chain_eq`, `chain_value`, `rotation_chain_value` | as above | S1, S2 |
| obstruction | `no_candidateCone_cnot_reflY` | as above | S1, V |
| non-vacuity | `prodState_mem_maxCone`, `candidateCone_productSet`, `reflY_mem_productSet`, `candidateCone_cnotOrbit`, `cnot_mem_cnotOrbit` | as above | S2, S4 |
| selectors | `three_of_nativeGate_of_two_le`, `three_of_nativeGateOf_of_two_le`, `two_le_of_entangling` | as above | S3, V |
| selector controls | `two_le_load_bearing`, `two_le_satisfiable` | as above | S3, S4 |
| verdicts | `k2guard_orientation`, `k2guard_entangling` | as above | S2, S4, V |
| count | the 19 prints | each within the three axioms; `lean-axioms` passes | S9 |

## Design evidence

Design runs (`workflow_dispatch`; the Mathlib bridge job and the release gate read):

| Run | Branch, commit | Workflow run | Result |
|---|---|---|---|
| 1 | `claude/k2g-dev` `5c394c8f` (from `D`: an earlier text of the module, blob `fc4c137c`, with tactic fallbacks in seven proofs; the import after `K1Bridge`; the census family after K1-BRIDGE-1's) | 37467680750 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112282733126) built the module with each of the 19 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`; release gate PASS (`lean-axioms` 5762, 36 receipts hold); the only module warnings were unused-tactic warnings on the fallbacks; repair history only, not cited for the frozen implementation |
| 2 | `claude/k2g-dev` `7e6e35fa` (module blob `a18f972b`: run 1's text with each tactic fallback collapsed to one branch) | 37468315829 | **failed**: the Mathlib bridge (job 112284902370) left an arithmetic goal unsolved in `chain_value` and in `rotation_chain_value`, where the collapse dropped a needed `norm_num` step, so four prints carried `sorryAx`; the other 31 jobs succeeded; repair history only |
| 3 | `claude/k2g-dev` `02537aef` (module blob `ec8ba57b`: run 2's text with the `norm_num` step restored in those two proofs; the import after `K1Bridge`; the census family after K1-BRIDGE-1's) | 37471469288 | **green**: all 32 jobs `success`; the Mathlib bridge (job 112295768337) built the module with each of the 19 `#print axioms` lines within `[propext, Classical.choice, Quot.sound]`, with no warning in the module; release gate PASS (`lean-axioms` 5762, no `sorryAx`; `lean-manuscript` OK; 303 legacy records intact; 36 receipts hold); the Lean kernel check (job 112295768399) and the probe aggregate (job 112302549748) succeeded |

No statement or definition changed between the three runs; runs 1 and 2 are repair history and anchor nothing in this freeze. Run 3 is the design evidence for the frozen implementation, and the execution blobs of §"The frozen surface" are those of run 3.

Statement-level choices recorded as frozen: the family is the set family of the K2 thread's T5, with no convexity or
closedness, so the obstruction covers every convex cone between the minimal and the maximal cone; the reflection acts
on the second copy through DIM-1's `actT`; the witness effects are EFF-1's sharp effects along `−e₁` and `−e₃`; the
relative selector carries K1-BRIDGE-1's binder names, with the gate named `T`; `2 ≤ d` replaces K1-BRIDGE-1's `0 < d`
in the relative selector.

### The predicted execution tree

- **`01d973717a35aa01733e11aad57f3fc661a2d7b2`** (`claude/k2g-predicted`, a single-parent child of `D`) is the execution tree less the result
  note. Its files and blobs:
  - this preregistration in its drafting revision, blob `ed565b45616f73f8a6e70f54aa4ba68e955065c8`, which differs from the revision at `F`
    only in this section;
  - `controls.py`, blob `d33086bb5560ed979f808ab2ec953f364dacd21d`;
  - `K2Guard.lean`, blob `ec8ba57b178561c81b082404ceb02241ada1fe1e`;
  - `OIBridge.lean`, blob `58d7ecaeb47dfe25992afeb3cea85f6faf92a05b`;
  - the census, blob `05be8369fcb8e6578ac991a7b56ca6b492318f9e`.
- `delta(D, 01d97371)` is exactly those five paths: the record directory's two files and the three execution
  paths.
- At that commit `controls.py check 01d97371`, run from the tree's own frozen `controls.py`, passes all 19
  checks, and `controls.py verdict 01d97371` prints exactly `K2-ORIENTATION-OBSTRUCTION-PROVED` for the orientation
  cell and `K1-ENTANGLING-WEAKENED` for the entangling cell.
- **Run 37473592066** (`workflow_dispatch` on `01d97371`, attempt 1) completed with conclusion success; every one of
  its 32 jobs succeeded. The Mathlib bridge (job 112303125909) built `OIBridge.K2Guard` with each of the 19 frozen
  `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` and no warning in the module, and its release
  gate passed every step (`lean-axioms` 5762 named results, no `sorryAx`; `lean-manuscript` OK; 303 legacy records
  intact; 36 receipts hold); the Lean kernel check (job 112303126113) and the probe aggregate (job 112311051465)
  succeeded. Its facts agree with design run 3 at `02537aef`.

The predicted tree is a sibling of `F` on `D`, not an ancestor of `F`; it and these runs are design evidence, not
attestations.

## Stages

1. **C1** adds `controls.py`, blob `d33086bb5560ed979f808ab2ec953f364dacd21d`, to the record directory. Acceptance: the blob is the frozen
   blob.
2. **S1** adds the module, the import line and the census family in one commit. Acceptance:
   - `controls.py check S1 --freeze F` passes;
   - the exact-head run at S1 has every job green, the Mathlib bridge building the module with every printed axiom set
     within `[propext, Classical.choice, Quot.sound]` and the release gate passing.
3. **Repairs**, if the build at S1 fails, change theorem proofs only; each passes `controls.py check` at its commit. A
   failure that a proof-only repair cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F` passes
   (the result note included in S7 and V) and the exact-head run at `E` has every job green.

## Outcomes

- **`K2-GUARD-1-READ`** — `controls.py check E --freeze F` prints `controls: OK`, `controls.py verdict E` prints exactly
  one outcome for each cell, and the exact-head run at `E` is green on every job, the Mathlib bridge building
  `K2Guard` with every frozen `#print axioms` reporting a subset of `[propext, Classical.choice, Quot.sound]` and the
  release gate passing. The result note states each cell as its row words it, the two earned readings, and the
  non-inference rule.
- **`K2-GUARD-1-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names
  the failing check or job.

No outcome sources any hypothesis, edits the ROADMAP, or identifies the physical composite cone. Correctness bands are
unchanged by either outcome: the round is consistency-axis work.
