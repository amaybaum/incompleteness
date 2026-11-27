# A1 staging amendment r2, supplement S11-2a: binding to the configuration admitted at F (paper draft)

**Status.** Draft for independent review and the owner's adoption. It amends the paragraph "S11-2a
evidence" of `AMENDMENT.md` in this directory (staging amendment r2 at
`a251b1b39846e75c73b08fdc06fd6ff1ff8dd1f6`), replacing its requirement that both invocations use
"the same reviewed config pin" with a binding to the configuration admitted at `F`. Everything else
in r2 stands. Adoption, implementation, staging, freeze and execution keep their separate gates.

**Authority.** Owner decision (amaybaum, received 2026-11-27, coordinating session; recorded at
#1169 comment 7207734407, 2026-11-27T01:59:03Z), item 7, quoted:

> Approve the S11-2a binding to the configuration admitted at F, using its exact path, commit F and SHA-256 from F's pin table. Require the both-arms substitution negative control. Authorize drafting and independent review of the staging r2 amendment before adoption.

**Goal link (AGENTS.md §A.47).** Serves the admissible Item 2 check of A1 retirement (#1169). It
would decide whether S11-2a's two runs are bound to the reviewed configuration rather than only to
each other.

## 1. The defect

The gate's S11-2a baseline (`_s11_unmutated_result` in `tools/ledger_coverage/gate/control_gate.py`
at `7db52f380f1e51d4af52b84f0a7e728827ac5a60`) requires the two results' `config` objects to be equal
and both argv to name `--check item2`. Its own comment records the gap: no source names the expected
configuration path and digest, so a configuration substituted in both runs alike passes.

## 2. The binding

**S11-2a configuration binding.** S11-2a has a countable baseline only if both of its runs, the
coverage run at exact `E` and the coverage run at its planted child, are bound to one configuration
`(F, P, S)` that the gate derives without reading either run's result or argv:

1. **`F`** is the gate's `--freeze` argument, a full 40-hexadecimal commit id read through the
   repository's git objects (`--repo`). It comes from the dispatch input `freeze` of the pinned
   workflow (`.github/workflows/ledger-coverage.yml`), the candidate `F` whose exact-head run is
   being attested (AGENTS.md §A.39; R6.REC.16). At `7db52f38` the suite job's `control gate` step
   passes neither `--freeze` nor `--config`; this amendment adds exactly
   `--freeze "${{ inputs.freeze }}" --config "${{ inputs.config }}"` to that step's `control_gate.py`
   invocation, a frozen workflow edit. The gate does not take `F` from a result, an argv, a manifest
   or a commit message.
2. **`P`** is the gate's `--config` argument, from the dispatch input `config`: the configuration's
   path in `F`'s tree (the same argument the TR5 release check reads).
3. **`S`** is the SHA-256 that `F`'s pin table lists for `P`. The pin table is the one R6.REC.16 step 2
   derives: in the regular file `PREREG.md` in `P`'s directory of `F`'s tree, the last subsection whose
   heading matches `^### \d+\.\d+ Record pins\b`, whose rows are `` | `<file>` | `<sha256>` | ``. The
   row naming `P`'s file name must be the only such row, and its SHA-256 a 64-hexadecimal string. The
   blob at `P` in `F`'s tree must be a regular file (mode `100644` or `100755`) whose bytes hash to `S`.

Then each of the two runs must satisfy, independently of the other:
- its argv carries exactly one `--config`, whose operand is exactly `F:P`;
- its result's `config.commit` equals `F`, `config.path` equals `P`, and `config.blob_sha256` equals
  `S`.

The existing conditions (both argv name `--check item2`, equal argv apart from `--commit`, equal
`config` and `profiles`, the approved profile pins, the exact mutation, E pinned by R6.NOTE.1, the
recomputed outcome and exit file) remain.

**Fail closed.** A missing or malformed `--freeze` or `--config`, a missing `PREREG.md`, no `Record
pins` subsection, no row or more than one row for `P`, a malformed row, a blob at `P` that is absent,
not regular or not hashing to `S`, or either run failing either condition leaves S11-2a with no
countable baseline: the gate refuses it with `raw-evidence-missing`, as for the existing ITEM2-CHECK
refusals. An unreadable git object is a gate failure, never a pass.

**What the gate reads.** The gate arguments `--freeze` and `--config`, set from the workflow's
dispatch inputs `freeze` and `config`; through `--repo`, the commit
`F`, its tree, the blob at `P` and the `PREREG.md` beside it; and, from the retained S11-2a evidence,
each case's argv and result file. It reads no other source for `F`, `P` or `S`.

## 3. Controls

Added to the ITEM2-CHECK cases of `tools/ledger_coverage/adapters/staging_controls.py`; each is a
specification until implemented.

| Id | Setup | Expected |
|---|---|---|
| S11-2a-BIND-POS | Both runs name `--config F:P`; both results carry `config` `{commit: F, path: P, blob_sha256: S}`; `F`'s pin table lists `P` with `S` and the blob hashes to `S` | GATE_HOLDS for S11-2a |
| S11-2a-BOTH-ARMS-SUBST (required negative) | Both runs, argv and results alike, name another configuration `P'` (or `F':P`, or the same path with digest `S'`) consistently with each other, so the existing equality checks pass | GATE_FAIL with `raw-evidence-missing` for S11-2a |
| S11-2a-ONE-ARM-SUBST | Only the mutated run names another configuration | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-PIN-MISMATCH | The pin table lists `P` with a SHA-256 other than the blob's | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-PIN-EARLIER-SUBSECTION | `P` is listed only in an earlier `Record pins` subsection, not the last (as R6.REC.16 and EI4 (c)) | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-NO-FREEZE | The gate runs without `--freeze`, or without `--config` | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-WRONG-FREEZE | `--freeze` names a commit whose pin table lists a different configuration, which both runs use | GATE_FAIL with `raw-evidence-missing` |

The both-arms control is the one the existing equality cannot detect; the others confirm that each
element of `(F, P, S)` is read from its stated source.

## 4. Open question for the owner

**OQ-S1.** Must the gate's `--freeze` equal the commit under check (`--commit`, which in the exact-head
run at candidate `F` is `F` itself)? Recommended default: yes for the exact-head attestation run, so
the dispatcher cannot name an unrelated `F`; the suite job's other controls already read the
configuration at `$GITHUB_SHA`, so equality matches the existing job; the alternative accepts any `--freeze` whose pin table
admits the configuration, leaving the choice of `F` to review of the dispatch inputs.

## 5. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7207734407, item 7 | authority, quoted above | provenance |
| `AMENDMENT.md` at `a251b1b39846e75c73b08fdc06fd6ff1ff8dd1f6` | the paragraph amended | support off `main` (branch `tools/a1-ledger-coverage-r6`) |
| r13 R6.REC.16 at `5ad8837521de0a26734266a64f91548fd3dcff1e` | pin-table derivation | support on `main` (landed by #1604) |
| `control_gate.py`, `staging_controls.py`, `ledger-coverage.yml` at `7db52f380f1e51d4af52b84f0a7e728827ac5a60` | current behaviour and gate inputs | provenance (PR #1577) |
