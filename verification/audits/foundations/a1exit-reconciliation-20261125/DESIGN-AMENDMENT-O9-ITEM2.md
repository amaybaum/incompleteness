# Ledger coverage tool: bounded design amendment for O-9 and the item-2 records (draft r2, unreviewed)

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

**r2.** This revision answers the independent review of r1 (`0fa0bc808cf70a05105c9dada7e407caba9b2ade`, REJECT, findings
B1-B6 and two item-2 controls). Its answers are adopted: an explicit class pin that names a path decides it; D1-D4 were
not sufficient; misuse stops the run. Section G maps each finding to its change.

## A. Change 1 (O-9): the plan's record directory on `M`

### A.1 Problem

Design sec. 13.1 classifies each side change between `H` and `M` only by an exact class pin, or as a class record the
configuration pins. The amended plan merges its pull request into `main` before the landing `L`, so every file of the
plan's record directory is a side change on `M`. The configuration, its review record and `PREREG.md` cannot be pinned
by any class record frozen at `F` without a hash cycle, and no record written after `F` is used (Stage A, Appendix A,
V2). Without a further rule the landing check is REVIEW_REQUIRED `side-change-unclassified` and cannot pass.

### A.2 Terms

`F` is the run's admitted plan commit (`--freeze`, admission sec. 6.3). `P` is the configuration's path in `F` (the
path `--config F:P` names) and `D` the directory part of `P`. An entry is a non-tree entry of a commit's tree with its
mode, as `GitRepo.entries` lists it: regular files (`100644`, `100755`), symbolic links (`120000`) and submodules
(`160000`). `E_F` and `E_M` are the entries strictly inside `D` (paths beginning with `D` followed by `/`) at `F` and at
`M`.

### A.3 Directory authority (replaces r1's D1)

The rule is active only for a directory the tool itself authorizes, independently of any configuration. The tool's
pinned code carries one constant, the tuple of authorized record directories, which for this revision is exactly

```
('verification/audits/foundations/a1exit-deletion-20261121',)
```

`D` must equal one member by string equality. The constant is part of the tool's files, so it is fixed by the tool's
review and landing and pinned by every configuration's `tool.files` (execution identity, sec. 6.3); no configuration,
record or command-line argument can add to it. Changing it is a tool revision.

### A.4 Further constraints on `D`

Evaluated once per run, from `H`, `F`, `M` and the configuration, before any side change is classified. If any
condition of A.3 or A.4 fails, the run stops with ERROR `CONFIG_INCONSISTENT` naming the condition; no path is classified
by the rule.

- **D2.** No entry inside `D` exists at `H`: the rule covers only a directory the plan itself introduces.
- **D3.** No ledgered path, no corpus path (the configuration's `corpus.patterns`), no path under a prefix of any
  side-change class the configuration references, and no path under `.github/` lies inside `D`, at `F` or at `M`.
- **D4.** `F`'s tree holds `P` and the file of record pins inside `D` (sec. 6.3 admission already requires this; it is
  restated so that the rule's directory is the admitted plan's directory).
- **D5.** No side-change class the configuration references uses the class id `record-directory`, which is reserved for
  this rule; a class record that defines it is ERROR `CONFIG_INCONSISTENT`.

r1's D1 (a minimum of three components) is dropped: A.3 supersedes it.

### A.5 Directory completeness (new)

The rule does not depend on the `H`-to-`M` side-change scan to find the directory's files. When the rule is active, the
tool compares `E_F` and `E_M` path by path over their union:

- a path whose entries at `F` and `M` are both regular files, with the same mode and the same blob id, and whose bytes
  at `M` have the same sha256 as at `F`, is **equal**;
- every other path is **unequal**, with its reason: `absent at M` (in `E_F` only), `absent at F` (in `E_M` only),
  `differs from F` (both regular, blob or mode differs), or `not a regular file` (a symbolic link or submodule at `F` or
  `M`).

Entry types are checked from the entries before any bytes are read, so a symbolic link or submodule never reaches a
byte read and never raises. Each unequal path is an item REVIEW_REQUIRED `side-change-unclassified` naming the path and
its reason, whether or not the `H`-to-`M` scan lists it. Because `E_F` and `E_M` are enumerated directly, a file of `F`
deleted on `M` is reported even though it exists at neither `H` nor `M`.

### A.6 Classification of side changes inside `D`

For a side change `p` found by the existing `H`-to-`M` scan (sec. 13.1), the existing classifier is applied first, and
its result is one of three outcomes:

| Existing classifier outcome | `record-directory` rule |
|---|---|
| a class pin names `p` and matches `M`, or `p` is a class record the configuration pins | not applied; the existing class stands |
| a class pin names `p` but differs from `M`, or `p` is a pinned class record whose sha256 differs | not applied; `side-change-unclassified` stands, naming the class |
| no class pin names `p` and `p` is not a pinned class record | applied |

Where applied, `p` is classified `record-directory` exactly when the rule is active, `p` is inside `D`, no component of
`p` is empty, `.` or `..`, and A.5 finds `p` equal. Otherwise `p` stays `side-change-unclassified` with A.5's reason (or
`outside the record directory`). A ledgered or corpus path is `base-drift` before any classification (sec. 13.1); by D3
none lies inside `D`, and the rule is in any case evaluated only after that test.

### A.7 Where it applies

The rule and the completeness check of A.5 are one function, called with the same context (`F`, `D`, the authority
check and D2-D5) by both places that classify side changes:

- the `M` role of `execution` (sec. 13.1; item 14's candidate and landing commands and the RT-L2 safeguard);
- condition R11 of a reconciliation record (sec. 13.3, `engine/reconcile.py`), which enumerates side changes on its
  own. R11 holds only if every side change it enumerates is classified and A.5 finds no unequal path.

Without `--freeze` (control-harness runs without a stand-in `F`) the rule is inactive and A.5 is not evaluated; the
directory's files are then `side-change-unclassified`, as today. The `record-dir` delegation class for `X` and `C`
(sec. 7.3) and the landing composition (sec. 13.1) are unchanged.

### A.8 Output

Each side change classified by the rule is listed with `class: "record-directory"`, its first-parent commit, and its
mode, blob id and sha256 at `F` and at `M`. The result records `D`, the authority match, the outcomes of D2-D5, and A.5's
counts (paths equal, paths unequal by reason).

### A.9 Controls (preregistered)

Synthetic engine controls, each a separate case, with `F` and `M` built by the synthetic fixture and the authorized
directory of A.3 used as `D` unless the case says otherwise:

| Id | Case | Expected |
|---|---|---|
| O9-1 | every entry of `D` at `M` equal to `F` | each `record-directory`; A.5 no unequal path; no `side-change-unclassified` |
| O9-2 | one file in `D` modified on `M` after `F` | that file `side-change-unclassified` (`differs from F`); the others `record-directory` |
| O9-3 | a file added in `D` on `M`, absent at `F` | `side-change-unclassified` (`absent at F`) |
| O9-4 | a file of `F` in `D` deleted on `M` (absent at `H` and `M`) | `side-change-unclassified` (`absent at M`), reported by A.5 although the `H`-to-`M` scan does not list it |
| O9-5 | a path outside `D` whose blob at `M` equals its blob at `F` | `side-change-unclassified` (`outside the record directory`) |
| O9-6 | a sibling path `D-x/f` sharing `D` as a string prefix, equal at `F` and `M` | `side-change-unclassified` |
| O9-7 | the clean-path predicate applied to paths with a `.`, `..` or empty component | each refused (tested on the predicate, since git trees do not normally carry such names; the fixture builds one with a raw tree object if its reader admits it) |
| O9-8 | in `D`: the same blob with a mode change (`100644` to `100755`); a symbolic link at `M` where `F` has a regular file of the same bytes; a submodule entry at `M` | each `side-change-unclassified` (`differs from F`, `not a regular file`, `not a regular file`); no exception |
| O9-9 | a ledgered path, and separately a corpus path, inside `D` | ERROR `CONFIG_INCONSISTENT` (D3) |
| O9-10 | a configuration in the root directory | ERROR `CONFIG_INCONSISTENT` (authority) |
| O9-11 | a path inside `D` that exists at `H` | ERROR `CONFIG_INCONSISTENT` (D2) |
| O9-12 | `D` holding a path under a side-change class prefix, and separately a path under `.github/` | ERROR `CONFIG_INCONSISTENT` (D3) |
| O9-13 | a path in `D`, equal at `F` and `M`, that a class names with a pin differing from `M` | `side-change-unclassified` naming the class (A.6 row 2); not `record-directory` |
| O9-14 | no `--freeze` | the rule inactive; files in `D` `side-change-unclassified`; A.5 not evaluated |
| O9-15 | a reconciliation record, `M` with `D` equal to `F` | R11 holds |
| O9-16 | a configuration in a newly introduced, unrelated directory (four components, absent at `H`, holding the configuration and a file of record pins, no ledgered, corpus, class or `.github/` path) | ERROR `CONFIG_INCONSISTENT` (authority): D2-D4 hold, A.3 fails |
| O9-17 | a class record defining class id `record-directory` | ERROR `CONFIG_INCONSISTENT` (D5) |
| O9-18 | a reconciliation record, `M` with one file of `D` modified after `F` | R11 fails |
| O9-19 | a reconciliation record, `M` with one file of `F`'s `D` deleted | R11 fails (A.5) |
| O9-20 | a reconciliation record, `M` with a file of `D` equal to `F`, but the run's `D` not authorized | ERROR `CONFIG_INCONSISTENT` (authority) before R11 is evaluated |

Real-tree control (A1 control runner, beside RT-L2):

| Id | Case | Expected |
|---|---|---|
| RT-O9 | the predicted `M`: `main` plus the tool landing plus the plan's record directory as it stands at the stand-in `F` | the control computes the expected set independently from the stand-in `F`'s tree: every entry inside `D`, with its mode, blob id and sha256. It requires the run's `record-directory` entries to equal that set exactly (no path missing, none extra, modes and hashes equal), A.5 no unequal path, no `side-change-unclassified`, and RT-L2 still PASS |

### A.10 Mutation controls

Each mutant is listed with the control that distinguishes it and both expected results.

| Mutant | Change | Distinguishing control | Correct implementation | Mutant |
|---|---|---|---|---|
| O9-m1 | A.5 omitted: only the `H`-to-`M` scan is used | O9-4 | `absent at M` reported | nothing reported; landing classified clean |
| O9-m2 | the prefix test without the trailing `/` | O9-6 | `D-x/f` unclassified | `D-x/f` `record-directory` |
| O9-m3 | D2 removed | O9-11 | ERROR `CONFIG_INCONSISTENT` | the run proceeds |
| O9-m4 | the authority check (A.3) removed | O9-16 | ERROR `CONFIG_INCONSISTENT` | the run proceeds, the unrelated directory's files `record-directory` |
| O9-m5 | mode not compared | O9-8 (mode case) | `differs from F` | `record-directory` |
| O9-m6 | the blob at `M` compared with `H` instead of `F` | O9-1 | `record-directory` | `side-change-unclassified` (`H` holds no such entry) |
| O9-m7 | D3 removed | O9-12 | ERROR `CONFIG_INCONSISTENT` | the run proceeds |
| O9-m8 | the clean-path test removed | O9-7 | each path refused | each path accepted |
| O9-m9 | A.6 row 2 bypassed: the rule applied when a class pin names `p` but differs | O9-13 | `side-change-unclassified` naming the class | `record-directory` |
| O9-m10 | entry type not checked before reading bytes | O9-8 (symbolic link and submodule cases) | `not a regular file`, no exception | an exception (`*-group-error`) or a wrong class |
| O9-m11 | R11 uses the classifier without A.5 | O9-19 | R11 fails | R11 holds |
| O9-m12 | D5 removed | O9-17 | ERROR `CONFIG_INCONSISTENT` | the class record's `record-directory` class accepted |

r1's mutants "accept a path absent at both `F` and `M`" and "rule evaluated before the `base-drift` test" are withdrawn
as equivalent under this design: a path absent at both is never enumerated by A.5 and, inside `D`, never by the
`H`-to-`M` scan (D2); and D3 excludes every ledgered and corpus path from `D`, so the order of the `base-drift` test and
the rule cannot change an outcome. O9-m1 and O9-m7 replace them.

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
ERROR `SOURCE_CHANGED` (fail-closed, as for `hp.json`). Both files are required to exist. One may hold an empty list when
item 2 needs no record of its kind; it then still carries its `record_id`, and its review, which the review chain binds
to that `record_id` when the item list is empty, states that the list is empty and why.

The tool routes by schema, not by file name. A file of the wrong schema under either name is admitted only if the
configuration references it and its review passes; its review checks that each file holds its named kind.

### B.4 Controls (preregistered)

| Id | Case | Expected |
|---|---|---|
| I2-1 | the `item2-coverage` arm's command, read from the workflow file by the conformance controls (which already read that file) | exactly the existing arguments followed by the two `--classify` arguments of B.2, every expansion quoted; a new control, since no existing control checks an arm's text |
| I2-2 | a meaning-context adjudication supplied through `context-adjudications.json`, matching both context hashes of a meaning-context site | that site PASS (sec. 4.1 row 2), as K10 |
| I2-3 | `context-adjudications.json` absent at `F` | ERROR `SOURCE_CHANGED` |
| I2-4 | `hit-classifications.json` present but not referenced by the configuration | `record-invalid`; the hit stays REVIEW_REQUIRED |
| I2-5 | a referenced record without a valid review | `record-invalid` |
| I2-6 | an empty `entries` list with its `record_id`, referenced, with a valid review bound to that `record_id` | admitted; no site resolved by it; the same file without `record_id`, or without a review, `record-invalid` |
| I2-7 | a hit classification supplied through `hit-classifications.json`, matching a hit outside any HP region by its line sha256 | that hit resolved as the classification states; without the record, the same hit REVIEW_REQUIRED |
| I2-8 | an indicator adjudication supplied through `context-adjudications.json`, matching both context hashes and both structure hashes of a LIST or TABLE site | the `context-structure-changed` item resolved (sec. 4.1 row 3); without it, REVIEW_REQUIRED `context-structure-changed` |

## C. Pins and records that change

The implementation of this amendment changes:

- tool files: the side-change classification (`engine/reconcile.py`, `engine/execution.py`, and the call sites that
  pass `F`, `D` and the authority), the constant of A.3, the controls (`engine/controls_engine.py`,
  `adapters/a1_controls.py`, `adapters/conformance_controls.py`) and the mutation set;
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
class (sec. 7.3), reconciliation records other than R11's side-change enumeration (sec. 13.3), the landing composition
(sec. 13.1), every other workflow arm, the command-line interface, the HP, context and hit-classification schemas, and
the acceptance predicate. The `H`-to-`M` side-change scan outside `D` keeps its present form, including its use of blob
entries only; A.5 applies inside `D` alone.

## F. Questions for the reviewer and the owner

1. A.3 places the directory authority in the tool's pinned code as an exact constant. The alternative is a check in
   the pinned workflow that refuses a configuration outside the authorized directory; it would guard only runs of that
   workflow, while the constant guards every run of the tool. The design takes the constant.
2. A.5's reasons, and the choice that every unequal path in `D` is REVIEW_REQUIRED `side-change-unclassified` (as for
   other side changes) rather than a FAIL.

## G. Changes from r1, by review finding

| Finding | Change |
|---|---|
| Q1-Q3 | adopted: an explicit class pin decides (A.6); D1-D4 insufficient (A.3); misuse stops the run (A.4) |
| B1 | A.5: `E_F` and `E_M` compared directly, so deletions on `M` are reported; used by both callers (A.7); O9-4, O9-19, O9-m1, O9-m11 |
| B2 | A.3: an exact authorized directory in the tool's pinned code, independent of the configuration; r1's D1 dropped; O9-16, O9-20, O9-m4 |
| B3 | A.6: the three outcomes of the existing classifier; D5 reserves `record-directory`; O9-13, O9-17, O9-m9, O9-m12 |
| B4 | A.2 and A.5: mode-aware entries, type checked before any read; O9-8 gains the submodule case; O9-m10 |
| B5 | A.10: a distinguishing control for each mutant, with both results; two equivalent mutants withdrawn; mutants added for the clean path, pin bypass, authority and enumeration |
| B6 | A.7: one function and context for both callers; O9-18 to O9-20 |
| Item 2 | I2-6 states the empty record's `record_id` and review; I2-7 (hit classification) and I2-8 (indicator adjudication) added |
| RT-O9 | the expected set computed independently from the stand-in `F`, compared exactly with modes and hashes |
