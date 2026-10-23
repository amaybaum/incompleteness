# Reconstruction round PRESERVE-INDUCT-1 — conditional preservation by protocol induction: RESULT

Run under `AGENTS.md` §A.39 as a native round, controlled from #880. This note is stage 3, candidate `E`. `E` is not
designated.

- **`D`**: `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`.
- **`F`**: `46781818f8d8da53153dbe62c9e88c61488960ff`, a single-parent child of `D` that adds only the
  preregistration.
  - Its exact-head `workflow_dispatch` run is 39263818996, attempt 1. It concluded `success`, all 37 jobs succeeded,
    and it is `F`'s `check-run` attestation. It attests the control plane only: `F`'s tree holds none of the round's
    execution files.
  - The owner designated `F` in comment 6270966165 on #880, created 2026-10-19T15:31:13Z. The comment records the
    designation and states that execution needs a separate owner authorization. `evidence/f-run/designation.json`
    holds the comment as read on 2026-10-23.
- **Shape**: non-sealing, in three stages, each a single-parent child of the one before.
  - Stage 1: `controls.py` (blob `208801fc`), `evidence/predicted-tree/results.json` and `evidence/f-run/`.
  - Stage 2: the core module (blob `a40464f5`), the instance module (blob `13b786c7`), the probe (blob `0333a734`)
    and the independent check (blob `b2e3f178`); `verify.yml` with the six frozen splices; the two import lines; the
    two census families.
  - Stage 3: this note.

## The cells

The three cells and their rules are frozen in the preregistration (*Decision rules and earned reading* and *Verdict*):

| Cell | Positive token |
|---|---|
| Q-CORE | `PRESERVE-INDUCT-CORE-PROVED` |
| Q-COR | `PRESERVE-INDUCT-COROLLARIES-PROVED` |
| Q-EXACT | `PRESERVE-INDUCT-EXACT-CHECKED` |

The tokens are printed by `controls.py verdict E --freeze F --axioms <E's exact-head bridge log>`.
- Q-CORE and Q-COR read the ten axiom reports from the block of the bridge job's final step, bound to `E` by its
  marker line.
- Q-EXACT runs the probe and the independent check at their frozen blobs.
- The round outcome `PRESERVE-INDUCT-1-READ` also requires the fourteen static controls of
  `controls.py check E --freeze F`, and the exact-head run at `E` green on every job.

This note is part of `E`, so it records none of these measurements and no cell token. They are recorded in `E`'s
retained expected result (§A.42 item 2) and in the receipt's candidate entry for `E`.

## What `E` carries

The core module, `OIBridge/PreservationInduction.lean`, states for an independently specified carrier cone family
`C` and any implementation class:
- `instAvail_preserves`: if `C` has zero membership and addition closure, the primitive steps and native readout
  preserve it, uniform attachment sends `C_S` into `C_(S×Fin m)` and ancilla discard sends it back, then every branch
  of every `InstAvail` family preserves `C_S`;
- `instAvail_sum_preserves`: the same for the sum of the unnormalized branches;
- `instAvail_spectator_preserves` and `instAvail_transport_preserves`: the headline applied through
  `instAvail_spectator` and `instAvail_transport`, with exactly the context and label hypotheses displayed. Transport
  preserves the cone assigned to the destination carrier; it does not identify that cone with a reindexing of the
  original one.

The instance module, `OIBridge/PreservationInductionInstances.lean`, establishes the premises for the positive
semidefinite cone on every finite carrier with any inventory (`quantum_instAvail`), and for the nonnegative diagonal
cone with the monomial inventory and its reindexed register readouts (`classical_instAvail`,
`classical_native_readout`).

These are statements of the frozen surface. Whether `E` proves them within `[propext, Classical.choice, Quot.sound]`
is read from `E`'s exact-head run, as above.

The probe and the independent check at `E` are the frozen blobs. They interpret every constructor on the same five
inputs: one with exact SymPy 1.14.0 matrices, the other with standard-library rational arithmetic. Each must reach
the frozen manifest digest, and the probe must reject its eight mutation runs. These are finite exact computations,
not universal statements.

## Design evidence

The preregistration pins the expected result of the predicted-tree run 39250136990, retained as
`evidence/predicted-tree/results.json`. That run built, at the predicted tree `9c5c0431`, the module, probe and
independent-check blobs frozen at `F`.
- Every job succeeded (38 jobs).
- The build succeeded, and the release gate passed 22 of 22 steps.
- `OIBridge.lean`'s 19 reports, the core's 4 and the instance module's 6 lie within
  `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`, `Lean.ofReduceBool` or `sorry` marker in the lines
  read.

The run is evidence for the predicted tree, not a `check-run` attestation of `F` or `E`. It stands in for no check
the preregistration assigns to `E`. The two historical research builds stay attributed provenance, as the
preregistration's retention rows record. This round establishes their axiom reports again at `E` and does not verify
those builds retroactively.

## The non-inference rule, as frozen

> Non-inference rule: the theorem sources no primitive preservation, context stability, label/cone covariance,
> state-space identification, flow, gate, test validity or quantum inclusion. It does not close K2 or P0 and is not a
> substitute for the bridge audit's physical-source and disguise tests. It supplies no part of the extension that the
> `P1 — F2` row lists as open (ROADMAP :1125–1129 at D): the compatible state transformations named there are assumed
> by the `op`, `readout`, attachment and discard premises.

**Premises this round does not source:**
- additive closure, primitive preservation, uniform-attachment preservation and ancilla-discard preservation for any
  physical cone;
- context stability and label invariance of a physical inventory;
- a finite list of concrete physical operators generating the implementation class.

The inventory constrains which cones can satisfy the premises: `fullClass` admits every isometry, and the diagonal
cone fails its `op` premise under an admitted Hadamard conjugation (`COUNTER-HADAMARD`, `I-HADAMARD`). That belongs to
the assumption audit and does not count toward sourcing compatibility.

The earned reading is the preregistration's. It applies only under `PRESERVE-INDUCT-1-READ` with all three cells
positive.

## Execution notes

- **Blob identity.** The five frozen blobs are present at stage 2 (`controls.py` from stage 1), checked with
  `git rev-parse`. No frozen blob differs, and no proof, probe or control was repaired.
- **The tested tree.** Stage 2's seven execution files are byte-identical to those of the predicted tree `9c5c0431`.
  Stage 2's tree differs from that tree in `controls.py`, present here at its frozen blob, in the preregistration,
  which is the version at `F`, and in the evidence files. `E` adds this note.
- **The predicted-tree file.** `evidence/predicted-tree/results.json` was rebuilt from the run's served bridge-job log
  (job 118051638340), using `D`'s own `build_archive.py` `results_for` and `extract_result.py`.
  - The served text is the last 5000 of 38750 lines, sha256
    `5a949a72baca02c037bb0a2b086de34877df43ed3f7e9eb4b80516b3af0c31d9`.
  - The rebuild is byte-identical to the pin: 13625 bytes, sha256
    `d3508cad6339a5c32d0359868ab460d57d6550f45df4167878ff0164e8ae86fb`.
- **`F`'s run record.** `evidence/f-run/results.json` is read from the served window of the bridge job's log (job
  118098114324): the last 5000 of its 38705 lines, original lines 33706–38705, sha256
  `00c471ed22cc859b2da4bc852a668dac9ad115d059613bac0943d9769bf8b5b8`.
  - In that window the build succeeded, the release gate passed 22 of 22 steps, and `OIBridge.lean`'s 19 axiom
    reports are complete and within the three axioms. Both adopted modules are absent at `F` with no report, and no
    failure marker appears.
  - `index.json` lists the reports and failure markers of original lines 1–33705 as missing.
- **Legacy records.** The round changes no file listed in `verification/infrastructure/legacy-records.json`.

**Scope.** The round adds:
- two kernel modules;
- one probe and one independent check;
- two census families (`kernel-only`, no manuscript);
- two import lines;
- one workflow shard, and a final step in the bridge job.

It changes no landed module, manuscript, built artifact, `verification/ROADMAP.md`, evidence-archive file or other
round's record. K2, P0 and F2 remain open. Correctness bands are unchanged (consistency axis).
