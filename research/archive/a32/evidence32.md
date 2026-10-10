These runs were made before this freeze, on disposable branches from `D` that are never landed. Each
is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design evidence**
recorded here: none is a `check-run` attestation, and no predicate of the round reads them.

**The ten texts and the corollary.** The elaboration file is
`verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean`, blob `@@ELAB_BLOB@@`. Under
the frozen header it carries eleven `#check` commands and nothing else: the ten propositions frozen
above, each verbatim, and the corollary form `(P_N) → ¬ (P_R)`.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36241719499 | `9bbbde0d86b936e73287d2574431bde8b2c203fd` | the elaboration file, its import line directly after `OrbitGeometryRigidity`, a disposable census family | red at the numerical probes only. The guard's `R7-NLV` fails its wiring check, because the import split `R7-NLV`'s pinned adjacency of `OrbitGeometryRigidity` and `StrictNaturalLift`. The `Mathlib bridge` build and the release gate are green |
| 36243196377 | `ea8f9edd73ca9fc8076c0978983babcd94969961` | the same, with the import moved directly after `StrictNaturalLift` | all three jobs green. The `Mathlib bridge` build prints the eleven `#check` results and no error. The release gate passes all 21 steps |
| 36243198088 | `f521d8d4f6cc851a5872d2f474242e7e5710294c` | **the countercontrol**: the elaboration file with one deliberate defect, the first shape of `P_R` written `.submatrix τ` with one index | red, as required. The Lean kernel check and the numerical probes are green. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/OrbitIsometryClassification.lean:29:47: Type mismatch`, at that shape |

The countercontrol shows that the elaboration check has force: an ill-typed frozen statement fails
the build at its own line, and nothing else fails.

**The separation, rehearsed in the kernel.** The rehearsal module proves the frozen `S_SEP` by the
strategy recorded in the route. It has 28 theorems:
- entry and value lemmas for the Fourier tuple at `i` and `−i`;
- the conversions of the conjugated and transposed shapes;
- four core lemmas and eight bridge lemmas;
- four exponent tables over all 576 pairs;
- `S_SEP` itself.

| run | head | outcome |
| --- | --- | --- |
| 36244347747 | `43e3b7b52186593fe8ec3c2ac3f8ebbe103cdd10` | red. The four tables, proved by `decide`, reach the elaborator's limit of 200000 heartbeats in `whnf`. The designated-circle bridges fail on an unparenthesized test class. Everything else compiles, including the 64-case entry lemmas |
| 36244571105 | `bcf6ee799b42e0b0c49ffeeb3370dd0723b6a2f0` | all three jobs green. The tables are proved by `decide +kernel`. `Built OIBridge.OrbitIsometryClassification (23s)`. All 28 theorems print only `propext`, `Classical.choice` and `Quot.sound`. The release gate passes all 21 steps |

The strategy is not frozen. This evidence shows only that `S_SEP` as frozen is provable in the
kernel, in a time the build tolerates.

**The retired guard and the corrected cells, exercised in CI.**

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| @@RUN_NR@@ | `55c72286ab31641a4a5908c7946794318cbb8e03` | the elaboration file, the retired guard (blob `@@GUARD_BLOB_RETIRED@@`) and the `A32-NOT-RIGID` cell (`ROADMAP.md` blob `@@ROAD_NR@@`) | @@OUT_NR@@ |
| @@RUN_R@@ | `120e6de20271ed67cf12b90cf0ab3e55124078a7` | the same, with the `A32-RIGID` cell (`ROADMAP.md` blob `@@ROAD_R@@`) | @@OUT_R@@ |

Those two heads carry the cells as drafted before the final wording of this round's standing clause
(`ROADMAP.md` blobs `@@ROAD_NR@@` and `@@ROAD_R@@`). The frozen cells differ from them only in that
clause, and have blobs `@@ROAD_NR_FROZEN@@` and `@@ROAD_R_FROZEN@@`. The guard reads none of the text
this round appends. The local guard matrix below is run against the frozen cells.

**The native lifecycle, rehearsed locally.** Three executions were built in scratch worktrees and
never pushed, one per row. Each is a `D → F → E → Λ → Q` chain:
- `F` is this file.
- `E` is one execution commit. It carries `controls.py`, a synthetic module with the frozen
  statements (never compiled), the census family, the import line, the result note, and the surfaces
  for its row.
- `Λ` is a `--no-ff` merge of `E` into `D`.
- `Q` adds the receipt built by `tools/v3_receipt.py`, with placeholder attestations.

@@SIMS@@

The scripts that produced this evidence, none of which is landed:

| script | SHA-256 |
| --- | --- |
@@SCRIPTS@@
