# A1 retirement working records: preservation copies (2026-11-24)

**These files are preservation copies, not byte-identical original evidence.** They are cleaned copies
of the coordinating session's local working records for the A1 retirement: the ledger coverage tool's
designs, implementation records and independent reviews, the A1 plan amendment proposal and its
reviews, the Q10 disposition, the SM.md:1394 reading, and the texts prepared for GitHub records.

- Status: preserved by owner decision (amaybaum, 2026-11-24, coordinating session): "preserve cleaned
  copies on a separate records branch, with a complete hash-mapping manifest. Do not introduce an
  exception to the repository's rules. ... A cleaned copy must never be presented as byte-identical
  original evidence."
- This branch is for preservation only. It is not a pull request, it establishes no claim, it accepts
  no implementation, and it is not to be merged without a separate owner decision.
- The tool implementation itself is on branch `tools/ledger-coverage-20261123` at
  `4f4a9d58fd0bf41289a4904c9b39c00c711c9093` (correction 2), accepted by the owner on 2026-11-24 within the
  limits stated in the CI validation section below; it is not on `main`.

## What the copies are

`copies/<path>` holds the copy of the local record `<path>`. `MANIFEST.json` lists, for every file,
its relative path, the SHA-256 and size of the local original, the SHA-256 and size of the copy,
whether the two are byte-identical, and the transformations applied with their counts.

The transformations are mechanical text substitutions only (`MANIFEST.json`, key `transformations`):
local absolute paths are replaced by placeholders (`<records>`, `<repo>`, `<write-state>`, `<tmp>`),
the local name of the session working directory is replaced by `workspace`, and the commit-identity
e-mail address is replaced by a placeholder. No scientific content, review verdict, test result or
owner decision was changed. Scripts among the copies may not run as copied, because their paths were
replaced.

**Hash references.** Every SHA-256 quoted inside a record refers to the local original of the file it
names, never to its copy here. The `original_sha256` column maps each original to its copy; a record
that is byte-identical to its original (`byte_identical: true`) has the same hash in both columns.

## Selection

The records copied are the text records (`.md`, `.json`, `.sha256`, `.diff`, `.patch`, `.py`, `.txt`,
`.yml`, `.sh`, each at most 512 KiB) at the top two levels of the record directories
`coord2-ledgertool-design`, `coord2-a1-amend`, `coord2-q10`, `coord2-sm1394` and `coord2-records`,
excluding working directories (`work*`); the staged configuration `staging-3184c7f9` and the edit diffs
`diffs-r5` in full; and the session handoff. Not copied: raw run outputs, logs, mutation outputs,
probe trees and copies of repository trees, which are regenerable or not needed by a surviving
record; the final review of `3184c7f9`, still in progress; and the paused OI-COMP-BENCH records.

## Batch 2 (2026-11-24): correction 2, its review and the CI validation build

`copies-2/` and `MANIFEST-2.json` add, by the same mechanical method and transformations, the records made after
batch 1: the final review of correction 1 (`review-corr1/`), the correction 2 writer's record, checkpoint, local
suite results (`impl-v6.0e/logs/corr2/full/`) and staged configuration (`staging-4f4a9d58/`), the correction 2
review (`review-corr2/`), the CI validation build record and workflow copy (`ci-validation/`), the owner decision
records for correction 2 and the A1 plan reconciliation obligations, the texts of the #1169 record comments, both
session handoffs, and the then-current `impl-v6.0e/MANIFEST.sha256` and `CORRECTION-1.md`. A file present in both
batches is copied as it stood at each batch; `MANIFEST-2.json` gives the original hash at batch 2. Batch 1 is
unchanged. These are preservation copies, not byte-identical original evidence.

## CI validation evidence (2026-11-24): run 45465948636

`ci-run-45465948636/artifact.zip` is the evidence artifact `ledger-coverage-suite-ci-evidence` (artifact id
14963596973) of the disposable CI validation run 45465948636, copied byte for byte, not cleaned: its SHA-256,
`08b0da5d620dfae04136fbc1db0deb5c829a185eec62ec3a5d1f18ba2ab3eb15`, equals the digest GitHub reports for the
artifact. Before commit it was scanned for tokens, keys, signed URLs, e-mail and IP addresses and local paths, with
no hit; nothing is redacted. Its `ci-results.json` (schema `ledger-coverage-suite-ci/1`) lists the SHA-256 of
every other file in it, and all 99 match.

- Run: workflow `.github/workflows/ledger-coverage-suite-ci.yml` (blob `0b26004f29852164301836f2e81be2abc43d077d`,
  SHA-256 `13176a4d1ed91b1b2f6e2445380f57bf79006072ccbfb48d55dcd6d90b65f513`), push event, attempt 1, on branch
  `ci/ledger-coverage-suite-4f4a9d58` at CI commit `52f7e56a1d2397a607a3a0126fb153062f9846fc`, whose single
  parent is the tool commit `4f4a9d58fd0bf41289a4904c9b39c00c711c9093`; `main` was
  `9deb69568d8231210c7f39cb65be943dea566371` throughout; staged configuration SHA-256
  `5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0`, as expected. Runner ubuntu-24.04, Python
  3.12.3, 4 CPUs, 16 GB.
- Result: every job step succeeded and every step verdict passed under the decision rules fixed in the workflow
  header. Self-test 86 of 86 controls passed, its result byte-identical to the local run's; synthetic 36 passed;
  conformance all PASS except NOT RUN for TR5 and G-A1; A1 conformance all PASS; A1 controls all PASS except NOT
  RUN for RT-T (exit 1, as its rule requires); the no-main check exited 2 (usage); Y8 PASS; mutation 82 killed,
  7 survived, 1 not applied (U01), the survivors exactly the local run's seven; the Lean build exited 0 with the
  worktree unchanged; the release gate exited 0.
- Owner decision (amaybaum, 2026-11-24, coordinating session): "Accept the verification tool at exact commit
  4f4a9d58, based on its independent implementation reviews and successful pre-landing CI validation, run
  45465948636. Acceptance is limited to the capabilities actually verified. Preserve the deferred-check list, the
  self-test mutation-testing limitation, the relative-mode release-gate qualification and the unpinned Lean
  installer observation."
- Limitations, which the acceptance does not cover:
  - Deferred to post-landing validation: TR5, G-A1 and EI14 (EI14 reports PASS in the conformance step; its validation by a real dispatch of
    the pinned workflow is deferred). Not runnable
    before landing: RT-T, TR45 op-C, real REST reads from GitHub, the sec. 16.7 double run and EI15 real dispatch.
    Y8 ran through the tool's built-in engine, not against the GitHub API. Real GitHub API reads are not validated.
  - The self-test detects little on its own: of 90 mutants, one (cache:K05) failed any self-test control, and none
    was killed by the self-test alone. The substantive detection is in the conformance, synthetic and A1 controls.
  - The release gate ran in relative mode only (no `--label` given), so its baseline check was not absolute.
  - The Lean toolchain installer was fetched from an unpinned source (elan master), as in `verify.yml`.

## Tool landing (2026-11-24): pull request #1557

The tool landed on `main` by merge `e2e2a623265187a28ebec604ab8bcc672742888f` (first parent `main`
`9deb69568d8231210c7f39cb65be943dea566371`, second parent `bb620ec653cfbed986785d9810cf2372906c9b73`, tree
`1d325e0c8c8f1b35dd75e72bea6466a2eb636379`, as approved by the owner). `bb620ec6` is a single-parent child of the
accepted `4f4a9d58` that adds the owner's sec. A.42 item 8 decision for ESC-1 to ESC-4 to the tool's audit README and
re-pins that README in `records/side-change-classes-v1.json`; no executable file changed. Pre-merge `verify` run
45496121210 and post-merge `verify` run 45497989649 on the merge both succeeded (26 jobs passed; the A42 exclusion job
is skipped by design except on `workflow_dispatch`).

`tool-landing-20261124/` holds:
- `review-readme-delta.md`: the independent check of `bb620ec6` (ACCEPT-WITH-NITS), reproduced in ASCII with the
  reviewer's scratch path replaced by `<scratch>`.
- `rt-l2/`: the result files (`a1-controls.json`) of three local runs of the A1 control runner, groups `exec`,
  `trees` and `k1`, on a full clone with `--main 9deb6956`: `A-old-old` (tool `4f4a9d58`, staged configuration
  SHA-256 `5072a3b0...`), 22 of 22 PASS; `B-new-old` (tool `bb620ec6`, the same configuration), 21 FAIL, the
  countercontrol (the class record no longer matches the configuration's pin); `C-new-new` (tool `bb620ec6`, the
  configuration with its two pins of the class record changed from `81af5033...` to `4b28d3d2...`, SHA-256
  `2bc78c3a...`), 22 of 22 PASS including RT-L2. Local runs: checks, not CI attestations. In `B-new-old` six
  occurrences of the local scratch path in error text are replaced by `<scratch>` (original SHA-256
  `7e083bf535d51fda417185351224c3f109ff095ae1db22d7022043a0eb0a69e6`); the other two are byte-identical to their
  originals.

Open after landing: the staged configuration's pin of the class record must change from `81af5033...` to
`4b28d3d2...` in the A1 plan reconciliation; ESC-1 to ESC-4 stay open under the landing exception until the A1 plan
amendment resolves them; post-landing validation (TR5, G-A1, EI14, real REST reads) needs its own authorization.
