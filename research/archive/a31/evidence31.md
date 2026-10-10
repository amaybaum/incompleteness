Run before this freeze, on disposable branches that are never landed, from `D`. Each run is a
`workflow_dispatch` run whose `head_sha` is the commit named. These runs are **design evidence**
recorded here; none is a `check-run` attestation, and no predicate of the round reads them.

The elaboration file is `verification/lean-mathlib/OIBridge/ProductOffLocusUniqueness.lean` at
`8bc262ddbe0c36a1ff822c8229b7b4aefdd8ee9b`, blob `d06391d2859ce4385ac88780426b10e4f95b2285`. Under the
frozen header it carries six `#check` commands and nothing else: `P_N`, `P_U`, `S_W`, `S_TAU` and
`S_PRE`, each verbatim as frozen above, and the corollary form `(P_N) → ¬ (P_U)`. It carries no
theorem, proof or verdict; its census family and import line exist only on that branch.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36235746157 | `8bc262ddbe0c36a1ff822c8229b7b4aefdd8ee9b` | the elaboration file, its import line, a disposable census family | all three jobs green; `Built OIBridge.ProductOffLocusUniqueness` prints exactly six `#check` results, at lines 19, 82, 145, 169, 190 and 231, and no error or warning; the release gate passes all 21 steps |
| 36236002553 | `a5015f6a6b4ace5cc1a694b535bd7e8bf29ac3a2` | the above with the `A31-1-NONUNIQUE` cell (`ROADMAP.md` blob `4b04375e8fd88c268dd39608d1b3c145a36f07b9`) | all three jobs green |
| 36236013813 | `867bf901037d2fba895d8fbfdd14d949f6e82ee2` | the above with the `A31-1-UNIQUE` cell (`ROADMAP.md` blob `2940548f782c29f24d2fcc7c0b465d778f20c1c1`) | all three jobs green |
| 36235747207 | `743caf402767cb2df213b122498a93646641d53a` | **the countercontrol**: the elaboration file (blob `ad0d7fd5eabb294a24e1d42a78b0c9984e65a955`) with one deliberate defect, the second law applied without its time index in `P_U` | red, as required: the Lean kernel check and the numerical probes are green, and the `Mathlib bridge` build fails with exactly one source error, `OIBridge/ProductOffLocusUniqueness.lean:142:35: Application type mismatch`, `OIBridge.ProductOffLocusUniqueness` being the only target that logs a failure |

Locally at `D`, the guard with either decided cell reports 91 PASS and 0 FAIL with `D`'s verdict map.

**The native lifecycle, rehearsed locally.** Three executions were built in scratch worktrees and never
pushed, one per outcome. Each is a `D → F → E → Λ → Q` chain:
- `F` is this file;
- `E` is one execution commit carrying `controls.py`, a synthetic module with the frozen statements
  (never compiled), the census family, the import line, the result note and the `P0` cell for its case;
- `Λ` is a `--no-ff` merge of `E` into `D`;
- `Q` adds the receipt built by `tools/v3_receipt.py`, with placeholder attestations.

In all three cases:
- `controls.py check E` prints `controls: check OK`;
- `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`;
- `--receipts Q` prints `RECEIPTS  7 receipt(s), all hold`;
- `tools/legacy_records_check.py Q` prints `LEGACY  303 record(s) in 75 closed namespace(s), all intact`.

The paths changed from `D` to `E` are seven on the two decided outcomes and six on `A31-1-UNDECIDED`.

| script (not landed) | SHA-256 |
| --- | --- |
| `gen_props31.py` (the frozen texts, from act 30's components) | `7ac59387917e4e96039466b8b1eecf23a8a2ba47995c6059b1ebb8496a632147` |
| `gen_elab31.py` (the elaboration file and its countercontrol) | `d398be2198425630a532b0b73499718194f04b6eceb742c2cf178351c39e82f8` |
| `sim_a31.py` (the lifecycle rehearsal) | `fd24ce34ce6049165706fcc8df210d9b72053e618fcb139f8467392e375d04ac` |
