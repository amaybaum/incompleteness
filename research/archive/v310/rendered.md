# Verifier round V3-10 — the first native V3 round: PREREGISTRATION

**Status: control plane of a provisional V3 pilot.** This round runs under `AGENTS.md` §A.39, not
§A.37: one pull request from `D`, the control plane drafted on it, execution after the owner
designates `F`, and the round's protocol record a receipt checked by `tools/v3_verifier.py
--verify-round`. The owner's designation of `F` is the authorization §A.39 requires.

> **A deliberately small change run through the whole native lifecycle.** The execution corrects
> the end of `verification/README.md`, a stray duplicated line, and adds one paragraph describing
> the receipt builder and §A.39. What the round tests is `F` → `E` → reconciliation → `Q`, the
> receipt built by `tools/v3_receipt.py`, the attestations, and an ordinary landing.

## The declarations

```v3-round
round V3-10
kind non-sealing
record-directory verification/infrastructure/round-v3-10-native-pilot/
```

```v3-governed-paths
record AM verification/infrastructure/round-v3-10-native-pilot/
record AM verification/receipts/V3-10.json
execution M verification/README.md
```

The record directory holds this preregistration and the result note. The receipt path is
`verification/receipts/V3-10.json`. The one execution path is `verification/README.md`, which may
only be modified. Nothing else may change.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects):

- `D` = `92683262a67190d7468a31a0c2f1dfdbc391778e`, the certified head of `main` after `V3-9`'s
  landing (push run 36099602123, all six jobs green). The pull request begins here. Every
  measurement in this file was taken at `D`.
- `F` — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- `E` — the certified execution head, which the owner designates.
- `Λ` — the last reconciliation, a merge whose first parent `LB` is `main` when it is built and
  whose second parent is `E` (or a superseded receipt commit); it is built with `--no-ff` if
  `main` is still `D`.
- `Q` — the final receipt commit, a single-parent child of `Λ` that adds only
  `verification/receipts/V3-10.json`.

## Measurements at `D`

- **Name freedom.** `v3-10`, `round-v3-10`, `V310-`, `native-pilot` and `receipts/V3-10` occur
  nowhere in the tree at `D`; `V3-10` occurs once, in `V3-9`'s preregistration, which names this
  round in advance. Neither `verification/receipts/` nor `verification/v3-seals/` exists.
- **The execution path.** `verification/README.md` at `D` has blob
  `55aba15ba3cf57a1fc35232534b6eed810abd920`. Its last line is a stray copy of the tail of the line
  before it: the paragraph describing `tools/v3_verifier.py` ends
  ``exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.``,
  and the file's final line repeats that text with `as an ` prefixed.
- **The present machinery.** A preregistration without a `control-plane-preconditions` block
  passes `tools/control_plane_lint.py` and evaluates 0 rows in
  `tools/control_plane_base_check.py`, and the certificate verifier requires no `V2` certificate
  for a new round directory (`V3-9`'s `F4`, unchanged at `D`).
- **Rehearsal.** The whole lifecycle was run at `D` in a scratch worktree with placeholder
  attestation records: `F`, the two execution commits, a `--no-ff` reconciliation onto `D`, and a
  receipt commit built by `tools/v3_receipt.py`. `tools/v3_verifier.py --verify-round` printed
  `VERDICT  HOLDS` on it; the same receipt with its execution delta digest zeroed printed
  `VERDICT  FAILS`. The `README.md` blob after the execution change was
  `e8a5c383c638c75d30324e77739c38c17d583358`.

## The execution, FROZEN

The execution is two commits after `F`, each with one parent:

1. **`README.md`.** The two lines below, which are the last two lines of `verification/README.md`
   at `D`, are replaced by the second text, and nothing else in the file changes. The file's
   predicted blob afterwards is `e8a5c383c638c75d30324e77739c38c17d583358`.
2. **The result note**, `verification/infrastructure/round-v3-10-native-pilot/result.md`, which
   records what was measured up to `E`. This commit is `E`.

The lines at `D`:

```text
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
as an exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

Their replacement:

```text
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.

`tools/v3_receipt.py` builds a V3 receipt from a round's exact object ids and the attestation
records the host holds, deriving every repository fact with the verifier's own functions; it is a
builder, not a verifier (`infrastructure/round-v3-9-operationalization/`). A round the owner
authorizes as a provisional V3 pilot under `AGENTS.md` §A.39 runs in one pull request, its receipt
`receipts/<round>.json` is its protocol record, and `tools/v3_verifier.py --verify-round` must hold
on its receipt commit before the pull request lands.
```

## The lifecycle, in the order §A.39 fixes

1. **`F`.** The branch is held at the candidate `F` and the workflow is dispatched on it. The run
   whose `head_sha` is `F`, every job green, is `F`'s `check-run` attestation. The owner reviews
   this file and designates `F` in a comment on the pull request, which is `F`'s
   `owner-designation` attestation. No commit after `F` changes this file.
2. **Execution to `E`.** The two execution commits are pushed together. The branch is held at `E`
   and the workflow is dispatched on it; the run whose `head_sha` is `E`, every job green, is
   `E`'s `check-run` attestation, and the owner's designation of `E` its `owner-designation`.
3. **Reconciliation.** `Λ` is built with first parent the current tip of `main` and second
   parent `E`.
4. **`Q`.** `tools/v3_receipt.py --status complete` builds the receipt from `D`, `F`, `E`, `Λ`
   and the four attestation records, with no candidates and no resolved paths; `Q` adds it at
   `verification/receipts/V3-10.json`.
5. **Verification.** `tools/v3_verifier.py --verify-round Q` must print `VERDICT  HOLDS` before
   the pull request lands, and the verdict is recorded on the pull request.
6. **Landing.** The pull request lands through ordinary review and merge.

If `main` moves after `Q`, a further reconciliation onto the new tip, with second parent `Q`, and a
new receipt commit on it replace `Λ` and `Q` (`K3`, `K4`); the superseded receipt stays in history.

## Targets

| target | passing outcome | stop outcome |
|---|---|---|
| `V310-0` | `F-DESIGNATED` — the dispatched run on exactly `F` is green on every job, and the owner designates `F` | `F-NOT-DESIGNATED` |
| `V310-1` | `EXECUTED` — the two execution commits change exactly `verification/README.md`, by the frozen text, and add the result note; `README.md`'s blob is the predicted one | `EXECUTION-WRONG` |
| `V310-2` | `E-DESIGNATED` — the dispatched run on exactly `E` is green on every job, the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate passing with `V2` authoritative OK, the shadow job's self-test and 135-vector corpus; and the owner designates `E` | `E-NOT-DESIGNATED` |
| `V310-3` | `RECEIPT-HOLDS` — `Q` carries the receipt `tools/v3_receipt.py` builds, and `--verify-round Q` prints `VERDICT  HOLDS` | `RECEIPT-FAILS` |
| `V310-4` | `CONTROL-FAILS` — the same receipt with its execution delta digest zeroed, committed on `Λ` in a scratch clone, prints `VERDICT  FAILS` | `CONTROL-VOID` |
| `V310-5` | `AUTHORITY-UNCHANGED` — no workflow, gate, guard, verifier, builder, corpus, `AGENTS.md` or specification file changes; no seal, manifest record or certificate is written; `V1` and `V2` stay authoritative | `AUTHORITY-CHANGED` |

A stop outcome after `F` halts the round under §A.39's halt path: `W` or the record commit, a
reconciliation, a halted receipt carrying `F`'s attestations alone, and `--verify-round` holding on
it. A stop before `F` is designated closes the pull request unmerged.

## Predictions

Every target is predicted to reach its passing outcome, strongly: the lifecycle was rehearsed at
`D`, the builder reproduces every holding corpus receipt, and the change is one text replacement in
a file no guard reads.

## What the round does not do or license

1. It changes no rule: §A.37 stays the default for every other round, and `V1` and `V2` stay
   authoritative for this one too — the guard and the release gate run on the pull request as on
   any other.
2. It writes no `V2` certificate, guard clause, seal or manifest record; its receipt is its
   protocol record.
3. It licenses no sentence that V3 is the default, which is `V3-11`'s question.

## Readings, recorded rather than resolved

- **`R1` — the change.** A documentation correction was chosen so that the pilot tests the
  lifecycle, not the content. The stray line is a real defect: the `V3-5` to `V3-8` paragraph edits
  replaced the paragraph above it and left the duplicated tail behind.
- **`R2` — non-sealing.** A sealing pilot would test `G12` as well; one lifecycle at a time.
- **`R3` — no candidates.** No execution head other than `E` is measured, so the receipt lists
  none: the two execution commits are pushed together, and a pull-request run measures a synthetic
  merge, not a branch commit.
- **`R4` — the result note stops at `E`.** It is part of `E`, so it records what was measured up
  to `E`. The attestations for `E`, the reconciliation and the verdict on `Q` are recorded in the
  receipt and on the pull request.
