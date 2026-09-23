# Verifier architecture round V3-1 — the one-pull-request lifecycle, commit-local chronology and the round receipt: RESULT

Executed from the certified merge of this round's control plane and from nothing else. The
execution's first act verified this round's preregistration blob at that base.

- **`B` (mandated execution base)** — `a99fd3438c0fdd4396e5f9d64321136d130e31e0`, parents
  `D` = `b9388cfb5d05ac30349fe7e489c320979d9d135b` and the control plane's reviewed head; push run
  35908925726, all five jobs green, the control-plane base check in mode `B` over 13 rows and 3
  frozen blobs with no failure
- **Freeze blob at `B`** — `3c2d3b399308f3b09499a20d7d73886ab3556601` at
  `verification/infrastructure/round-v3-1-architecture/preregistration.md`, verified before any
  edit
- **Shape** — non-sealing under §A.37, `E` → `L`, no `P`; no guard clause, manifest record, round
  certificate or attestation (reading `R3`)
- **Status** — COMPLETE: every target reached its passing outcome

| target | outcome | predicted |
|---|---|---|
| `V31-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `V31-1` | `ARCHITECTURE-COMPLETE` | `ARCHITECTURE-COMPLETE`, strong |
| `V31-2` | `CHRONOLOGY-COMMIT-LOCAL` | `CHRONOLOGY-COMMIT-LOCAL`, strong |
| `V31-3` | `RECEIPT-COMPLETE` | `RECEIPT-COMPLETE`, moderate |
| `V31-4` | `SUBJECT-BOUND` | `SUBJECT-BOUND`, strong |
| `V31-5` | `DETERMINISTIC` | `DETERMINISTIC`, strong |
| `V31-6` | `DRIFT-TOLERANT` | `DRIFT-TOLERANT`, moderate |
| `V31-7` | `SEALING-UNIFIED` | `SEALING-UNIFIED`, strong |
| `V31-8` | `HALT-REPRESENTED` | `HALT-REPRESENTED`, moderate |
| `V31-9` | `STATUS-CORRECTED` | `STATUS-CORRECTED`, strong |
| `V31-10` | `SPECIFICATION-ONLY` | `SPECIFICATION-ONLY`, strong |

The specification is `verification/infrastructure/v3/architecture.md`. It is not operative:
§A.37 governs every round until a later round activates V3.

***

## `V31-0` — the base: BASE-HOLDS

The execution branch was created at `B` exactly. The preregistration at `B` has the frozen blob.
The control-plane self-test and lint self-test pass, and `--mode B` at `B` passes 13 rows and 3
frozen blobs with no failure. Each row's command was also run directly: the `D` rows 5 of 5 at `D`,
the `D->B` rows 2 of 2, the `B` rows 6 of 6.

***

## `V31-1` — the specification: ARCHITECTURE-COMPLETE

The document carries the invariant verbatim at its head; one section headed with each of `S1` to
`S13`, each exactly once; a traceability table of thirteen rows; the lifecycle as eight states and
eight transitions; the receipt's encoding, field table and closed reason codes; the worked examples;
and four canonical example receipts.

On review, no settlement is weakened, omitted or contradicted. The document adds precision in these
places, each consistent with the settlement it refines:

- **`S3`** — `delta(F, E)` must be authorized under `S7`, and no commit of `F..E` changes a
  control-plane file.
- **`S4`** — the receipt is one JSON object with unique keys, and a key outside the field table is
  invalid; object ids take the width `object_format` fixes; the round id matches
  `[A-Z0-9]+(-[A-Z0-9]+)*`; the closed reason codes are exactly `halted-before-certification` and
  `no-execution-commits`; attestation objects have four fixed keys, with a minimum set per status.
- **`S7`** — the status `T` counts as `M` for authorization.
- **`S9`** — `D` lies on `LB`'s first-parent chain, the commit-local fact by which a verifier knows
  `LB` is later `main` than `D`; conditions 2 and 3 compare path **states** (mode and object id, or
  absence), which is stricter than the blob comparison of the frozen text.
- **`S12`** — the result note must be present at `W` and at `Λ`, and `W`'s parent must be a listed
  candidate; when no execution commits exist, a record-only commit on `F` carrying the result note
  takes the place of `W`.

***

## `V31-2` — chronology: CHRONOLOGY-COMMIT-LOCAL

Every transition of the lifecycle lists its inputs, and each input is a commit, tree, blob, the
declared block at `F` or the receipt at a named commit. None is a branch, a remote-tracking ref, a
host payload, the working tree, a fetch or the time. Publication, the one operation that reads the
tip of `main`, is stated as an operation and not as a predicate. `MC1`, `MC4` and `MC8` returned
their predicted verdicts on both cases (below).

***

## `V31-3` — the receipt: RECEIPT-COMPLETE

Every `S4` field is defined with its type and encoding, its subject, and its rule in each of the
three status columns; the reason codes are closed. The four canonical example receipts — complete
non-sealing, complete sealing after one base movement, halted with execution commits, halted
without — satisfy their columns under the model's receipt rules. `MC9` returned its predicted
verdict on all twelve cases.

***

## `V31-4` — subjects: SUBJECT-BOUND

Every receipt field names its subject in the field table, and every lifecycle predicate names the
commits it reads. `MC5` returned its predicted verdicts: an assertion certified at `E` was unchanged
after a later commit added a file it counts, while the same assertion evaluated on the working tree
changed — the `CV-2` failure mode, reproduced as a countercase and excluded by `S6`.

***

## `V31-5` — the formats: DETERMINISTIC

Every worked example was derived twice, by parsing `git diff-tree -r --raw --no-renames --no-abbrev
-z` as `S8` prescribes and independently from `git ls-tree -r -z` of the two trees, and the two
derivations were byte-identical in every case:

| delta | statuses | digest |
|---|---|---|
| `2c6a4373e7a6` → `56b253976e11` | `A` | `1a89deb9f260da4bbf53a91b959acbb4ab8bbc99740a7d949c6133c55e815f4e` |
| `f9a99fdf4b3b` → `14b9d991c325` | `A`, `M` | `6b3b05a0bba80ccb325e7a9fd875ecb9392d2ad3642edb538c2eab34b8f7b2be` |
| `d3212b0ea09b` → `50938dffc320` | `D` | `54e4a5f90e6eb789f88be9f4d8ccb6c8d6de6ebc5946dcde5f12b1e0351b0eee` |
| scratch, a path with LF and UTF-8 bytes | `A`, `M` | `61e4a51182e953b8cd90fe5b95031af5f531744fa5c7a75e865d460da87c36cd` |

The scratch delta's bytes were identical under `core.quotePath` true and false. For `S7`, the set
G1 declared in two orders gave one digest,
`e8bbfdef7908f026af80b86520349aa377d6963d98a995799aaf83d36251e946`; the set G2 gave
`9781ab0207e9d09d8f5f6f5bee3acd117f6743b568f25f619987ef6fae79489d` and resolved nested directory
entries by longest match; and fourteen invalid blocks, one per rejection rule, were each rejected.

***

## `V31-6` — landing under base movement: DRIFT-TOLERANT

`MC2` and `MC3` returned their predicted verdicts on both cases, and their mutation controls fired.
With `main` moved after `Q` was built, the non-force update failed and left `main` untouched; a second
reconciliation and receipt commit were appended; the retry fast-forwarded `main` to the new `Q`; `E`
was unchanged; the final receipt verified, listing both reconciliations. A host merge commit was
rejected as a publication, and a reconciliation on a base not descending from `D` was rejected. A
governed conflict resolution listed in `resolved_paths` was accepted; an ungoverned path added by a
reconciliation, and a governed path changed without being listed, were each rejected.

***

## `V31-7` — sealing: SEALING-UNIFIED

Sealing and non-sealing rounds share the lifecycle and every commit position and differ only in
`seal`; the document defines no pin commit. `MC7` returned its predicted verdicts on both cases.

***

## `V31-8` — halted rounds: HALT-REPRESENTED

Both halted example receipts satisfy their columns with no `e`, and the document states `S12`'s
three-part semantics. `MC6` returned its predicted verdicts: a halted round with a withdrawal was
accepted, its landing delta carrying only `record` paths and its execution commits reachable from
`Q`; a halted receipt claiming `e`, a withdrawal leaving a file added during execution, a withdrawal
removing the result note, and a landing publishing an `execution` path were each rejected.

***

## `V31-9` — the status correction: STATUS-CORRECTED

In `verification/README.md`'s `CV-1` paragraph, the frozen span is replaced by the frozen sentence,
reflowed to the paragraph's width. Whitespace-normalized, the paragraph equals the paragraph at `B`
under exactly that substitution; it is the only one of the file's 125 paragraphs that differs, and
neither "one certificate per round" nor "one record per round that has topology" remains.

***

## `V31-10` — scope: SPECIFICATION-ONLY

`git diff --name-status B E`:

| status | path |
|---|---|
| `M` | `verification/README.md` |
| `A` | `verification/infrastructure/round-v3-1-architecture/result.md` |
| `A` | `verification/infrastructure/v3/architecture.md` |

Nothing is deleted, and nothing under `tools/`, `.github/`, the Lean trees, `verification/seals/`,
`verification/certificates/`, `verification/programmes/`, `verification/audits/`, `papers/`,
`book/` or `AGENTS.md` changes. At `E` the guard gives `ALL CHECKS PASS`, 105 PASS and 0 FAIL, with
`D`'s verdict map; the verifier is authoritative OK; the release gate passes.

***

## The model check

A throwaway model of the settlements ran over temporary repositories. Its code is in no tracked file.
Each scenario ran its passing case and its countercase; for `MC2`, `MC3` and `MC4` the model was also
run with the corresponding check removed, and each countercase then passed that check.

| scenario | cases | as predicted |
|---|---|---|
| `MC1` unrelated ref churn | 3 | 3 |
| `MC2` base drift | 9 | 9 |
| `MC3` smuggled change | 5 | 5 |
| `MC4` rewritten execution | 5 | 5 |
| `MC5` historical subject | 2 | 2 |
| `MC6` halted round | 7 | 7 |
| `MC7` sealing unified | 4 | 4 |
| `MC8` freeze anchor | 3 | 3 |
| `MC9` receipt presence | 12 | 12 |
| total | 50 | 50 |

Two countercases are caught by more than one rule: a merge from later `main` inside `F..E` fails both
the linearity of `F..E` and the authorization of `delta(F, E)`; a reconciliation on a base not
descending from `D` fails both the first-parent condition and `S9`'s first condition. The mutation
controls show that each named rule fires on its own.

The model confirms the settlements as the model reads them (hazard `H4`); its pass is not evidence
that a future verifier is correct.

***

## Discrepancies

- **An extra commit.** The frozen stage table allots one commit to each of stages 1 to 4. Before the
  result note, the release gate's duplicate check found the heading "Canonical bytes" twice in the
  specification, under `S7` and `S8`. A fifth commit renamed the two subsections; no normative text
  changed. The commits after `B` are therefore five: the specification, the worked examples, the
  status correction, the heading fix, and this note, which is `E`.
- **A commit message.** The stage-2 commit message says the `S12` result-note rule and the
  halted-without-execution record commit were added in stage 2. They were added in the stage-1
  commit, before its checkpoint, when writing the model exposed that `S12`'s "the result note
  survives" had no checkable form.

***

## Chronology

The execution's commits after `B` are five, each a single-parent child of its predecessor, the first
a child of `B`. The branch absorbed no later `main`; there was no merge, rebase, amend or force-push,
and nothing was pushed before `E`. `V3-1` carries no mechanical chronology control of its own
(reading `R3`); this record and exact-head review stand in its place.
