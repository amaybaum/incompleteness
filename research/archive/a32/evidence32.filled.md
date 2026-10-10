These runs were made before this freeze, on disposable branches from `D` that are never landed. Each
is a `workflow_dispatch` run whose `head_sha` is the commit named. They are **design evidence**
recorded here: none is a `check-run` attestation, and no predicate of the round reads them.

**The ten texts and the corollary.** The elaboration file is
`verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean`, blob `fd5bc69b5dedd824937d44ce6a1097066cbcc936`. Under
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
| 36244774129 | `55c72286ab31641a4a5908c7946794318cbb8e03` | the elaboration file, the retired guard (blob `d28e9b3cf2093984a1c453892204b9932a685b2e`) and the `A32-NOT-RIGID` cell (`ROADMAP.md` blob `2496ee6fad349e6d07a7dcb2fd335a8701fc0723`) | all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order. The release gate passes all 21 steps |
| 36244775311 | `120e6de20271ed67cf12b90cf0ab3e55124078a7` | the same, with the `A32-RIGID` cell (`ROADMAP.md` blob `4d64cdde5987016541390e9beac29affd5050942`) | all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order. The release gate passes all 21 steps |

Those two heads carry the cells as drafted before the final wording of this round's standing clause
(`ROADMAP.md` blobs `2496ee6fad349e6d07a7dcb2fd335a8701fc0723` and `4d64cdde5987016541390e9beac29affd5050942`). The frozen cells differ from them only in that
clause, and have blobs `ebe80f84eadb7c48e0e566f8501887e291b0ca9f` and `30f7f80f7c155752242a7d09eb9f3bbd64268ece`. The guard reads none of the text
this round appends. The local guard matrix below is run against the frozen cells.

**The native lifecycle, rehearsed locally.** Three executions were built in scratch worktrees and
never pushed, one per row. Each is a `D → F → E → Λ → Q` chain:
- `F` is this file.
- `E` is one execution commit. It carries `controls.py`, a synthetic module with the frozen
  statements (never compiled), the census family, the import line, the result note, and the surfaces
  for its row.
- `Λ` is a `--no-ff` merge of `E` into `D`.
- `Q` adds the receipt built by `tools/v3_receipt.py`, with placeholder attestations.

In all three cases:
- `controls.py check E` prints `controls: check OK`;
- `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`;
- `--receipts Q` prints `RECEIPTS  7 receipt(s), all hold`;
- `tools/legacy_records_check.py Q` prints `LEGACY  303 record(s) in 75 closed namespace(s), all intact`.

The paths changed from `D` to `E` number eight on the two decided rows and six on `A32-UNDECIDED`,
where the guard and `ROADMAP.md` are untouched. Each run matches the frozen set.

The scripts that produced this evidence, none of which is landed:

| script | SHA-256 |
| --- | --- |
| `gen_props32.py` | `57b99c06ca9307a1406b886356f970fd3dca52fa146a13d249ab178a3d090033` |
| `gen_elab32.py` | `1d64011593a4f67f5d9a3654802b6d01c54b99c0e3026feb262d8b79a1c90127` |
| `gen_sep32.py` | `53eb5bdd81be2bcfc4ed3ca85b562b7607ded8e1a8cf7398e1b74e130fe6f523` |
| `build_retire32.py` | `8bcb3941f2a91a244d49c5f3004ce3a2f82464a460e170124ad2be0234de87e8` |
| `p0_32.py` | `ad9a31edde7b96cf0086dcc2834676d350c1ad5e60bfffdc826ab3675b864b03` |
| `ctlcheck.py` | `973f36355f80552c826a6539d201cd84c9e3fc1e7a7649146f7f3614b9a86226` |
| `sepenc.py` | `223ed53fb3e45edb5f5e18d57bb06a65e535ce4201b238ac4e3ea019c679e4d8` |
| `sim_a32.py` | `be916b0087c6e38878e06a4d5c141776e15c0ce9a10c9e534ec4bec633097f05` |
