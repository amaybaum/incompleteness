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
   repository's git objects (`--repo`), and it must equal the commit under check: the gate's
   `--commit`, which defaults to the HEAD of `--repo`. This is a mechanical gate condition; in the
   exact-head run at candidate `F` (AGENTS.md §A.39) the commit under check is `F` itself. `F` comes
   from the dispatch input `freeze` of the pinned workflow (`.github/workflows/ledger-coverage.yml`).
   At `7db52f38` the suite job's `control gate` step passes neither `--freeze` nor `--config`; this
   amendment adds to that step, as a frozen workflow edit, the environment entries
   `F: ${{ inputs.freeze }}` and `CFG: ${{ inputs.config }}` and the arguments
   `--freeze "$F" --config "$CFG"` to its `control_gate.py` invocation, matching the quoting of the
   rest of the file. The gate does not take `F` from a result, an argv, a manifest or a commit message.
2. **`P`** is the gate's `--config` argument, from the dispatch input `config`. Its directory must be
   the admitted A1 record directory of R6.A1CFG.1, `verification/audits/foundations/a1exit-deletion-20261121`,
   held as a constant of the gate. The gate imports nothing from the tool to obtain it, as with
   `ITEM2_PROFILES`; a change to R6.A1CFG.1's tuple needs the same change to the gate constant.
3. **`S`** is the SHA-256 that `F`'s pin table lists for `P`. The pin table is the one R6.REC.16 step 2
   derives: in the regular file `PREREG.md` in `P`'s directory of `F`'s tree, the last subsection whose
   heading matches `^### \d+\.\d+ Record pins\b`, whose rows are `` | `<file>` | `<sha256>` | ``. The
   row naming `P`'s file name must be the only such row, and its SHA-256 a 64-hexadecimal string.
   Where `F`'s tree holds `P`, its entry must be a regular file (mode `100644` or `100755`) whose bytes
   hash to `S`.

Then each of the two runs must satisfy, independently of the other, conditions that the real runner
meets. `tools/ledger_coverage/adapters/a1_controls.py` with `--staged-config` runs on an in-memory
stand-in for `F`: a commit derived from the commit under check, whose single parent is that commit
and whose tree is its tree with the staged configuration at `P`. So:
- its result's `config.path` equals `P` and `config.blob_sha256` equals `S`;
- its argv carries exactly one `--config`, whose path component equals `P` and whose commit component
  equals `F` or names the stand-in, a commit whose single parent is the commit under check.

`F` is still bound: it is the commit whose pin table yields `S`, the commit under check, and the
stand-in's parent, and the configuration's bytes are bound to `S` through `config.blob_sha256`. The
runner is not amended. How the gate establishes that a named commit is the stand-in is open question
OQ-S2.

The existing conditions (both argv name `--check item2`, equal argv apart from `--commit`, equal
`config` and `profiles`, the approved profile pins, the exact mutation, E pinned by R6.NOTE.1, the
recomputed outcome and exit file) remain.

**Fail closed.** A missing or malformed `--freeze` or `--config`, a `--freeze` other than the commit
under check, a `P` outside the admitted record directory, a missing `PREREG.md`, no `Record pins`
subsection, no row or more than one row for `P`, a malformed row, a blob at `F:P` that is not regular
or does not hash to `S`, or either run failing either condition leaves S11-2a with no countable
baseline: the gate refuses it with `raw-evidence-missing`, as for the existing ITEM2-CHECK refusals.
An unreadable git object is a gate failure, never a pass.

**What the gate reads.** The gate arguments `--freeze`, `--config` and `--commit` (or the HEAD of
`--repo`), the first two set from the workflow's dispatch inputs `freeze` and `config`; its constant
admitted record directory; through `--repo`, the commit `F`, its tree, the entry at `P` and the
`PREREG.md` beside it; and, from the retained S11-2a evidence, each case's argv and result file. It
reads no other source for `F`, `P` or `S`.

## 3. Controls

Added to the ITEM2-CHECK cases of `tools/ledger_coverage/adapters/staging_controls.py`; each is a
specification until implemented.

| Id | Setup | Expected |
|---|---|---|
| S11-2a-BIND-POS | Built from the real runner's argv shape: the gate's `--freeze` and `--commit` are `F`; both runs name `--config <stand-in>:P`, where the stand-in's single parent is `F`; both results carry `config.path` `P` and `config.blob_sha256` `S`; `F`'s pin table lists `P` with `S` | GATE_HOLDS for S11-2a |
| S11-2a-BOTH-ARMS-SUBST (required negative) | Both runs, argv and results alike, name another configuration consistently with each other (another path `P'`, or the same path with digest `S'`), so the existing equality checks pass | GATE_FAIL with `raw-evidence-missing` for S11-2a |
| S11-2a-DECOY-CONFIG | `F`'s tree holds a second configuration in another directory, listed by the `PREREG.md` beside it; the gate's `--config` and both runs use it | GATE_FAIL with `raw-evidence-missing` (outside the admitted record directory) |
| S11-2a-ONE-ARM-SUBST | Only the mutated run names another configuration | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-PIN-MISMATCH | The pin table lists `P` with a SHA-256 other than the results' | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-PIN-EARLIER-SUBSECTION | `P` is listed only in an earlier `Record pins` subsection, not the last (as R6.REC.16 and EI4 (c)) | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-NO-FREEZE | The gate runs without `--freeze`, or without `--config` | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-WRONG-FREEZE | `--freeze` names a commit other than the commit under check, whose pin table lists the configuration both runs use | GATE_FAIL with `raw-evidence-missing` |
| S11-2a-STAND-IN-PARENT | Both runs name a stand-in whose parent is not the commit under check | GATE_FAIL with `raw-evidence-missing` |

The both-arms and decoy controls are the ones the existing equality cannot detect; the others
confirm that each element of `(F, P, S)` is read from its stated source.

## 4. Open questions for the owner

**OQ-S2.** How the gate establishes that an argv's commit component names the stand-in whose single
parent is the commit under check. The stand-in exists only in the runner's memory. Recommended
default: the S11-2a evidence retains, beside each case, the staged configuration's git blob id, and
the gate recomputes the stand-in's id by the derivation rule restated in the gate (as `ITEM2_PROFILES`
restates pins), from the commit under check, `P` and that blob id, whose bytes hash to `S`; this is an
evidence-retention change, not a runner change. Alternative: require literally `config.commit == F`
in both results, which needs a tool change so that a staged run records `F` rather than the
stand-in.

## 5. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7207734407, item 7 | authority, quoted above | provenance |
| `AMENDMENT.md` at `a251b1b39846e75c73b08fdc06fd6ff1ff8dd1f6` | the paragraph amended | support off `main`; it lands with #1577 |
| r13 R6.REC.16 at `5ad8837521de0a26734266a64f91548fd3dcff1e` | pin-table derivation | support on `main` (landed by #1604) |
| `control_gate.py`, `staging_controls.py`, `a1_controls.py`, `record_authority.py`, `ledger-coverage.yml` at `7db52f380f1e51d4af52b84f0a7e728827ac5a60` | current behaviour, the stand-in, the admitted record directory and gate inputs | provenance (PR #1577) |
| r13 R6.A1CFG.1 at `5ad8837521de0a26734266a64f91548fd3dcff1e` | the admitted record directory | support on `main` (landed by #1604) |
