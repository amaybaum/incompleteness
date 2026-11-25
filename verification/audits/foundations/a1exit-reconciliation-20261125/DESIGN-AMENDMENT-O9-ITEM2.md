# Ledger coverage tool: bounded design amendment for O-9 and the item-2 records (draft, unreviewed)

Status: draft for independent review and owner adoption. It amends the adopted design v6.0e (sha256
`4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131`), as implemented on `main` at
`e2e2a623265187a28ebec604ab8bcc672742888f`, in two places only. Everything not stated here is unchanged.

Authorization (owner, amaybaum, 2026-11-25, coordinating session): "Authorize the Stage A review and the bounded tool
design as proposed. ... Limit the design amendment to O-9 and the item 2 record interfaces, including the proposed
controls, pinning and review requirements. Submit the completed design for independent review and owner adoption. Do
not begin implementation or Stage B." Started after the Stage A review's final ACCEPT, under the owner's instruction
"Accept V1 on the existing evidence and start the design" (amaybaum, 2026-11-25).

Goal link (sec. A.47): A1-EXIT (#1169). The amendment lets the tool decide the landing of the amended plan (O-9) and
read the records item 2 needs; it decides no scientific question and no record's content.

Basis: the Stage A findings, `verification/audits/foundations/a1exit-reconciliation-20261125/STAGE-A-FINDINGS.md` at
`68bab90e8f8c0cb060d318bfd17672833e3fe485`, sections 1 and 2 and Appendix A (V2), accepted by the independent review.

## A. Change 1 (O-9): the plan's record directory on `M`

### A.1 Problem

Design sec. 13.1 classifies each side change between `H` and `M` only by an exact class pin, or as a class record the
configuration pins. The amended plan merges its pull request into `main` before the landing `L`, so every file of the
plan's record directory is a side change on `M`. The configuration, its review record and `PREREG.md` cannot be pinned
by any class record frozen at `F` without a hash cycle, and no record written after `F` is used (Stage A, Appendix A,
V2). Without a further rule the landing check is REVIEW_REQUIRED `side-change-unclassified` and cannot pass.

### A.2 The rule

Let `F` be the run's admitted plan commit (`--freeze`, admission sec. 6.3), `P` the configuration's path in `F` (the
path `--config F:P` names) and `D` the directory part of `P`.

A side change `p` between `H` and `M` is classified `record-directory` exactly when all of the following hold:

1. **Inside `D`.** `p` begins with `D` followed by `/`. A path equal to `D`, or a path that merely shares a prefix
   with `D` (for example `D-x/...`), is not inside `D`.
2. **Clean path.** No component of `p` is empty, `.` or `..`.
3. **Present and equal at `F` and `M`.** `p` is a regular file (mode `100644` or `100755`) in both `F`'s tree and
   `M`'s tree, with the same mode, and its git blob id at `M` equals its git blob id at `F`; its sha256 at `M` equals its
   sha256 at `F`. A path absent from either tree, a symbolic link, a submodule entry or a mode change never satisfies
   this condition. Two absent blobs are never equal.
4. **Not ledgered or corpus.** `p` is not a ledgered path and not a corpus path. Such a side change is `base-drift`
   (sec. 13.1) before any classification is attempted, and this rule never applies to it.

The rule is evaluated after the existing routes (an exact class pin, or a class record the configuration pins) and
only for paths they leave unclassified. It never changes the classification of a path another route classifies, and it
never applies to `base-drift`.

So a file modified on `M` after `F`, a file added under `D` on `M` that `F` does not hold, and a file of `F` deleted on
`M` all stay REVIEW_REQUIRED `side-change-unclassified`, each naming the path and the reason (`differs from F`,
`absent at F`, `absent at M`).

### A.3 Constraints on `D` (misuse)

The rule is active only if `D` satisfies every condition below. These are evaluated once per run, from `H`, `F` and the
configuration, before any side change is classified. If any fails, the run stops with ERROR `CONFIG_INCONSISTENT`
naming the condition; no side change is classified by the rule.

- **D1.** `D` has at least three components, none of them empty, `.` or `..`. (The plan's directory,
  `verification/audits/foundations/a1exit-deletion-20261121`, has four.) A configuration at the repository root, or one
  directory down, cannot exempt broad parts of the tree.
- **D2.** No path inside `D` exists at `H`. The rule covers only a directory that the plan itself introduces; it can
  never exempt files that existed at the scientific base.
- **D3.** No ledgered path, no corpus path (the configuration's `corpus.patterns`), no path under a prefix of any
  side-change class the configuration references, and no path under `.github/` lies inside `D`, at `F` or at `M`.
- **D4.** `F`'s tree holds `P` at `D/` and the file of record pins beside it (sec. 6.3 admission already requires this;
  the condition is restated so that the rule's directory is the admitted plan's directory and no other).

The rule uses `F`, which every admitted run already names, and adds no pin. It therefore closes no hash cycle.

### A.4 Where it applies

The rule is part of the one side-change classification the tool uses: the `M` role of `execution` (sec. 13.1, used by
item 14's candidate and landing commands and by the RT-L2 sequencing safeguard) and the classified-side-change condition
R11 of a reconciliation record (sec. 13.3). Without `--freeze` (control-harness runs without a stand-in `F`) the rule is
inactive. The `record-dir` delegation class for `X` and `C` (sec. 7.3) and the landing composition (sec. 13.1) are
unchanged.

### A.5 Output

Each side change classified by the rule is listed with `class: "record-directory"`, its first-parent commit, and its
blob id and sha256 at `F` and at `M`. The run's result records `D` and the outcome of D1-D4.

### A.6 Controls (preregistered)

Synthetic engine controls, each a separate case, with `F` and `M` built by the synthetic fixture:

| Id | Case | Expected |
|---|---|---|
| O9-1 | every file under `D` at `M` equal to `F` (blob and mode) | each `record-directory`; no `side-change-unclassified` |
| O9-2 | one file under `D` modified on `M` after `F` | that file `side-change-unclassified` (`differs from F`); the others `record-directory` |
| O9-3 | a file added under `D` on `M`, absent at `F` | `side-change-unclassified` (`absent at F`) |
| O9-4 | a file of `F` under `D` deleted on `M` | `side-change-unclassified` (`absent at M`) |
| O9-5 | a path outside `D` whose blob at `M` equals its blob at `F` | `side-change-unclassified` (the rule does not apply) |
| O9-6 | a sibling path `D-x/f` sharing `D` as a string prefix, equal at `F` and `M` | `side-change-unclassified` |
| O9-7 | a path with a `.` or `..` component, or an empty component | not classified by the rule |
| O9-8 | the same blob with a mode change (`100644` to `100755`), and separately a symbolic link with equal target bytes | `side-change-unclassified` |
| O9-9 | a ledgered path, and separately a corpus path, placed inside `D` | ERROR `CONFIG_INCONSISTENT` (D3) |
| O9-10 | `D` with two components; `D` the repository root | ERROR `CONFIG_INCONSISTENT` (D1) |
| O9-11 | a path inside `D` that exists at `H` | ERROR `CONFIG_INCONSISTENT` (D2) |
| O9-12 | `D` holding a path under a side-change class prefix, and separately a path under `.github/` | ERROR `CONFIG_INCONSISTENT` (D3) |
| O9-13 | a path both pinned by a class and inside `D`, with the class pin differing from `M` | the class route's result stands: `side-change-unclassified` naming the class (the rule is not reached for a path whose class pin it names) |
| O9-14 | no `--freeze` | the rule inactive; files under `D` `side-change-unclassified` |
| O9-15 | a reconciliation record whose R11 lists a side change the rule classifies | R11 holds |

O9-13 fixes one reading: when a class lists `p` and its pin differs from `M`, the result is the class route's
`side-change-unclassified`, and the rule does not override a class that names the path. The reviewer is asked to
confirm or reject this reading.

Real-tree control (A1 control runner, beside RT-L2):

| Id | Case | Expected |
|---|---|---|
| RT-O9 | the predicted `M`: `main` plus the tool landing plus the plan's record directory as it stands at the stand-in `F` | every path under `D` `record-directory`; no `side-change-unclassified`; RT-L2 still PASS |

Mutation controls: the mutation set gains mutants that must each be killed:

| Mutant | Change | Killed by |
|---|---|---|
| O9-m1 | condition 3 accepts a path absent at both `F` and `M` | O9-4 |
| O9-m2 | condition 1 tests the prefix `D` without the trailing `/` | O9-6 |
| O9-m3 | D2 removed | O9-11 |
| O9-m4 | the rule evaluated before the `base-drift` test | O9-9 |
| O9-m5 | mode not compared | O9-8 |
| O9-m6 | blob at `M` compared with `H` instead of `F` | O9-2 |
| O9-m7 | D1 removed | O9-10 |
| O9-m8 | D3 removed | O9-12 |

## B. Change 2 (item 2): the context and hit-classification records

### B.1 Problem

Item 2's coverage command needs context adjudications (design sec. 3.5 and 4.4: the meaning-context cases on unchanged
sites, and the indicator cases, which use the same schema with structure hashes) and hit classifications for hits
outside HP regions (sec. 8.2). The workflow's `item2-coverage` arm passes only `hp.json` and the GR.md:58 record, so
these records cannot reach the command.

### B.2 The change

Workflow only. The `item2-coverage` arm of `.github/workflows/ledger-coverage.yml` gains two arguments, after its
existing ones:

```
--classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json"
```

where `$D` is the configuration's directory, as the arm already uses it for `ledger.json` and `hp.json`. No other arm
changes; no command-line option of the tool changes. `--classify` is already repeatable, and the tool already routes an
admitted record of schema `oi-context-adjudication/1` to the context collection and every other admitted record to the
hit classifications (`engine/cli.py:845-852`).

### B.3 The records

- `context-adjudications.json`: schema `oi-context-adjudication/1`, its adjudications under `entries`, covering both the
  meaning-context and the indicator (structure) adjudications item 2 needs.
- `hit-classifications.json`: schema `oi-hit-classification/1`, its classifications under `classifications`.

Each lies in the plan's record directory, is referenced by the configuration's `records` with its blob sha256, and has a
non-author review record, exactly as every other record the tool reads (sec. 6.3, ownership chain): a record not
referenced by the frozen configuration is never used (`record-invalid`), and a file absent at `F` stops the run with
ERROR `SOURCE_CHANGED` (fail-closed, as for `hp.json`). Both files are required to exist; one may hold an empty list when
item 2 needs no record of its kind, and that is stated in its review.

The tool routes by schema, not by file name. A file of the wrong schema under either name is admitted only if the
configuration references it and its review passes; its review checks that each file holds its named kind.

### B.4 Controls (preregistered)

| Id | Case | Expected |
|---|---|---|
| I2-1 | the `item2-coverage` arm's command, read from the workflow file by the conformance controls (which already read that file) | exactly the existing arguments followed by the two `--classify` arguments of B.2, every expansion quoted; a new control, since no existing control checks an arm's text |
| I2-2 | a context adjudication supplied through the second `--classify`, matching both hashes of a meaning-context site | that site PASS (sec. 4.1 row 2), as K10 |
| I2-3 | `context-adjudications.json` absent at `F` | ERROR `SOURCE_CHANGED` |
| I2-4 | `hit-classifications.json` present but not referenced by the configuration | `record-invalid`; the hit stays REVIEW_REQUIRED |
| I2-5 | a referenced record without a valid review | `record-invalid` |
| I2-6 | an empty `entries` list, referenced and reviewed | admitted; no site resolved by it |

## C. Pins and records that change

The implementation of this amendment changes:

- tool files: the side-change classification (`engine/reconcile.py`, `engine/execution.py`, and the call sites that
  pass `F` and `D`), the controls (`engine/controls_engine.py`, `adapters/a1_controls.py`, `adapters/conformance_controls.py`)
  and the mutation set;
- the workflow blob (B.2);
- the tool's audit directory: `controls.json` (the new rows), the README, and the tool-landing class record, which
  re-pins every changed path; the class record's own sha256 changes;
- the staged configuration (part of the A1 plan reconciliation, not of the tool landing): `tool.files`,
  `tool.workflow`, the class-record pin, and the new `records` entries of B.3.

## D. Validation and review

- Independent review of this amendment, then owner adoption.
- Implementation, then independent implementation review against this amendment.
- The tool's full local suite (self-test, purity, synthetic, conformance, A1 conformance and controls, mutation), then
  one disposable CI validation run of the exact implementation commit, as for correction 2. That run is a launch and
  needs the owner's approval.
- Merge to `main` by separate owner approval; the post-merge `verify` run.

## E. Not changed

Everything else in design v6.0e, including: admission and execution identity (sec. 6.3), the `record-dir` delegation
class (sec. 7.3), reconciliation records (sec. 13.3), the landing composition (sec. 13.1), every other workflow arm, the
command-line interface, the HP, context and hit-classification schemas, and the acceptance predicate.

## F. Questions for the reviewer and the owner

1. O9-13: a class that names a path decides it, even inside `D` (A.6).
2. D1's three-component minimum, and whether D1-D4 are sufficient against misuse.
3. Misuse stops the run (ERROR `CONFIG_INCONSISTENT`) rather than deactivating the rule silently.
