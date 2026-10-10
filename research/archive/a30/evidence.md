Run before this freeze, on disposable branches that are never landed, from `D`. Each run is a
`workflow_dispatch` run whose `head_sha` is the commit named. These runs are **design evidence**
recorded here; none is a `check-run` attestation, and no predicate of the round reads them.

**The seven texts.** The elaboration file is
`verification/lean-mathlib/OIBridge/ProductStrictLift.lean` at `17de29c27ed43d7f105aa8518451d8ed61c59937`,
blob `016e542872383b296bb0255d8e9ff1561d36fbcc`. Under the frozen header it carries seven `#check`
commands and nothing else:
- `P_S`, `P_T`, `P_N` and `P_0`, each verbatim as frozen above;
- the three corollary forms, `(P_S) → (P_T) → (P_N)`, `(P_N) → (P_0)` and `(P_0) → (P_N)`, each with
  the frozen texts substituted.

It carries no theorem, no proof and no verdict. Its census family and import line exist only on that
branch.

| run | head | what the head carries | outcome |
| --- | --- | --- | --- |
| 36222012214 | `17de29c27ed43d7f105aa8518451d8ed61c59937` | the elaboration file, its import line, a disposable census family | all three jobs green. `Built OIBridge.ProductStrictLift` prints exactly seven `#check` results, at lines 19, 37, 86, 126, 172, 275 and 359, and no error or warning. The release gate passes all 21 steps, `lean-axioms` and `lean-manuscript` among them |
| 36222326658 | `0004afc9360117ba61523b72854de1aaf63705f0` | the above, the retired guard (blob `@@GUARD_BLOB_RETIRED@@`) and the `A30-0-ADMITS` cell (`ROADMAP.md` blob `@@ROADMAP_BLOB_ADMITS@@`) | all three jobs green. The guard reports 91 PASS and 0 FAIL, its verdict map `D`'s tag for tag and in order; its diff from `D` is 12 lines added and 133 removed |
| 36222347638 | `62ad3a5f9320fcea6ccd7d0ac08a8ded17c7e30f` | the same, with the `A30-0-RESTRICTS` cell (`ROADMAP.md` blob `@@ROADMAP_BLOB_RESTRICTS@@`) | all three jobs green, with the same guard verdict map |
| 36222335508 | `6c30c61369dfa7245f080533099813b233e07d8b` | **the countercontrol**: the elaboration file (blob `d64cce4f28d733ad3bd70b843c2dec9251f46159`) with one deliberate defect, `TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL Ψ` in `P_N`, one induced map too few | red, as required. The Lean kernel check and the numerical probes are green. The `Mathlib bridge` build fails with exactly one source error, `OIBridge/ProductStrictLift.lean:123:12: Application type mismatch`, on `TwistedNatural (0, 0) αL Ψ`, and `OIBridge.ProductStrictLift` is the only target that logs a failure |

The countercontrol shows that the elaboration check has force: an ill-typed frozen statement fails
the build, at its own line, and nothing else does.

**The native lifecycle, rehearsed locally.** Three executions were built in scratch worktrees and never
pushed, one per `P0` case:
- `A30-0-ADMITS`, on row 1;
- `A30-0-RESTRICTS`, on row 3;
- `A30-0-UNDECIDED`, on row 7.

Each is a `D → F → E → Λ → Q` chain.
- `F` is this file.
- `E` is one execution commit. It carries `controls.py`, a synthetic module with the frozen
  statements (never compiled), the census family, the import line, the result note and the surfaces
  for its case.
- `Λ` is a `--no-ff` merge of `E` into `D`.
- `Q` adds the receipt built by `tools/v3_receipt.py`, with placeholder attestations.

In all three cases:
- `controls.py check E` prints `controls: check OK`;
- `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`;
- `--receipts Q` prints `RECEIPTS  6 receipt(s), all hold`;
- `tools/legacy_records_check.py Q` prints `LEGACY  303 record(s) in 75 closed namespace(s), all intact`.

The paths changed from `D` to `E` are eight on the two decided cases and six on `A30-0-UNDECIDED`,
where the guard and `ROADMAP.md` are untouched. Each run matches the frozen set.

The scripts that produced this evidence, none of which is landed:

| script | SHA-256 |
| --- | --- |
| `gen_props.py` (the four proposition texts and the header) | `f80524b8e1a9012c6d6c62476cc5e73094d2d5bada62063c5d8c68ffa5671556` |
| `gen_elab.py` (the elaboration file from those texts) | `47df8d639997b5ae78f95720d49bddd0bff3294a49d32613fc8869d140cd1263` |
| `build_retire.py` (the ledger and the retired guard, from the guard at `D`) | `f0803262aa1e4c6632b9e22128c76e41faf79cfdea871eb2a705053546666979` |
| `guard_matrix.sh` (the local guard matrix below) | `c79cc22e110146f8c4ef1a60530bde136e96d91915fef040e5ac8c95733abce1` |
| `sim_a30.py` (the lifecycle rehearsal) | `9c98ccaaad3bd178001d463016da7242e408c03dd132ad2da763fb8aed48575a` |
