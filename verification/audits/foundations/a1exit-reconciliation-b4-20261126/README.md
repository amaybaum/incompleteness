# A1 sequencing safeguard: drafted reconciliation and side-change class records (unreviewed)

Status: **unreviewed drafts.** Neither record has an independent review record. Under design r6 neither may be used
by any run until a non-author reviewer re-derives it from the git object store and writes an `oi-review-record/1`
naming its exact blob (R6.REC.2, R6.REC.6). RT-L2 is never PASS on a drafted record (R6.RECON.21); these drafts
release nothing.

Authority. Owner decision B4 (`amaybaum`, 2026-11-26T04:39:58Z; #1169 comment 7182798225), quoted: "B4 | Approved.
Draft the two required records on a separate branch and obtain independent review." The records are those that
design r6 (`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md`) requires for OBL-13 and OBL-14:
a reviewed reconciliation record for `AGENTS.md` bound to the run's `H`, `M` and `C` blobs, and side-change class
records for the unclassified side changes on `main` (sec. 20 R6.TREE.5, sec. 23 R6.RECON.1 and R6.RECON.21,
R6.EVID.8). Records strengthen no claim (R6.PLACE.9).

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169), the exception-free verification route; these records decide only
whether RT-L2 can be released for the tool's landing.

Placement. Outside the tool's landing paths (`tools/`, the tool's audit directory
`verification/audits/foundations/ledger-coverage-tool-20261123/`, `.github/workflows/ledger-coverage.yml`), as
R6.RECON.21 and R6.EVID.8 require: the run names them from a commit outside those paths, and they reach `main` in a
commit after the tool's landing commit.

## Files

| Path | Schema | sha256 |
|---|---|---|
| `records/reconciliation-agents-md.json` | `oi-reconciliation/1` | 331c06740385fc25bd131edb7c93496a240fe9844c9d8a085593a024497aefd9 |
| `records/side-change-classes-m0.json` | `oi-side-change-classes/1` | e422fc5c441f58fd536188fa8a9f7c3a58c8e5e7d9c94779df23dee96cdc4af2 |

## Bindings

- `H` = 53c6601a10419b6b333cc992474272501ab542af (R6.NOTE.2); the ledger and edit list are the pinned control
  inputs of R6.EVID.8 (blobs ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e and ec384fdfbc12937b860e2f226355e8c5d94820a5).
- `M0` = e8271d9d64e51cc6eb69a53ea2f5b80d490503a4, the head of pull request #1580: `main` at
  02b8e20839d4700de721f8427b3fe9f3c746b71f plus the revert of the merge of #1560, which restores the nine ledgered
  manuscript files that #1560 changed to their blobs at `H` (owner direction, `amaybaum`, 2026-11-26T04:52:48Z; #1169
  comment 7182986451). Every blob pin and every value of the `AGENTS.md` entry is taken at `M0`. If #1580 lands as a
  merge commit, or `main` moves before the run, the run's `M` descends from a commit other than `M0`; the records
  then hold only if every pinned blob and every `AGENTS.md` value is unchanged there, which the reviewer checks. The run's `M` is the predicted `M` (`M0` plus the tool's landing
  paths); the tool's landing touches no ledgered path (R6.PLACE.8), so the `AGENTS.md` values are the same there.
  The reconciliation record leaves `M` and `X` null: their ids exist only once the tool candidate and the `X_rep`
  builder exist. Naming them needs a superseding record of the same lineage with its own review.
- `C` = `X` = `X_rep` (R6.EVID.8): the record's `x` is the `AGENTS.md` blob of every conforming candidate, `H`'s
  bytes with splice D296 applied (sha256 equal to the ledger's `expected_sha256`).
- A different `M0` changes the class pins and possibly the `AGENTS.md` values; the records then need to be re-derived
  and reviewed again.

## What the records do not cover

At `M0`, `AGENTS.md` is the only ledgered or corpus path that differs from `H`. The paths of the tool's landing are
classified by the tool-landing class record, not here. The records themselves, their review records and this file
are not classified by any record here once they reach `main`.
