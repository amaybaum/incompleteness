# A1 sequencing safeguard: reconciliation and side-change class records (unreviewed)

Status: **unreviewed drafts.** No record in this directory has an independent review record. None may be used by any
run until a non-author reviewer re-derives it from the git object store and writes an `oi-review-record/1` naming its
exact blob (R6.REC.2, R6.REC.6). RT-L2 is never PASS on a drafted record (R6.RECON.21). Every `scientific_effect` in
the reconciliation record is the writer's draft, not a review; the independent review judges each one (R6.RECON.25).
Records strengthen no claim (R6.PLACE.9).

Authority (owner `amaybaum`, coordinating session, recorded on #1169):

- 2026-11-26T04:39:58Z, comment 7182798225: "B4 | Approved. Draft the two required records on a separate branch and
  obtain independent review."
- 2026-11-26T04:52:48Z, comment 7182986451: "M and X commit identifiers | Complete them when the actual commits exist,
  using independently reviewed superseding records." and "In-place record edits | Correct them using the required
  supersession procedure, preserving history."
- 2026-11-26T05:53:39Z, comment 7183914927: "F2 — Unclassified side changes | Complete the B4 side-change
  classification records. Every changed path must be accounted for. Do not introduce a blanket exemption."
- 2026-11-26T06:34:32Z, comment 7184569981: "No more reverts merely to satisfy the A1 ledger." and "detected drift
  should trigger a reconciliation assessment, not an automatic revert."
- 2026-11-26T07:31:59Z, comment 7185562871, item 1: "Rebuilding the B4 records using `oi-reconciliation/2`, covering
  every drifted ledger path."

Rules applied: design r6 as amended by amendment 3
(`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md` and `AMENDMENT-3.md` at
38c6ef53c059ce1277293eee7dc036495f4d5f66, adopted subject to exact-head CI): R6.RECON.1 to R6.RECON.5, R6.RECON.15,
R6.RECON.16, R6.RECON.22, R6.RECON.24 to R6.RECON.26, R6.TREE.4 to R6.TREE.8, R6.REC.7.

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169), the exception-free verification route; these records decide only
whether RT-L2 and RT-O9 can be released for the tool's landing.

Placement: a reconciliation directory (R6.RECON.1), under `verification/audits/`, outside the tool-landing prefixes
(`tools/ledger_coverage/`, `verification/audits/foundations/ledger-coverage-tool-20261123/`), the exact path
`.github/workflows/ledger-coverage.yml` and the plan's record directory
(`verification/audits/foundations/a1exit-deletion-20261121/`), holding no ledgered or corpus path.

## Files

| Path | Schema | `record_id` | `supersedes` | sha256 |
|---|---|---|---|---|
| `records/reconciliation-agents-md.json` | `oi-reconciliation/1` | a1exit-reconciliation-agents-md | none | 331c06740385fc25bd131edb7c93496a240fe9844c9d8a085593a024497aefd9 |
| `records/reconciliation-agents-md-r2.json` | `oi-reconciliation/1` | a1exit-reconciliation-agents-md | `records/reconciliation-agents-md.json` | cf14d6a948d37927290b0fcd8c43ccc8c79e38bcc8af145f25d31f5e5c288bb1 |
| `records/side-change-classes-m0.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | none | e422fc5c441f58fd536188fa8a9f7c3a58c8e5e7d9c94779df23dee96cdc4af2 |
| `records/side-change-classes-r2.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | `records/side-change-classes-m0.json` | fbc1ceddea1d5ef2811745bb39f8cdbfe7c30a2f41503927d019f56b96f45929 |
| `records/reconciliation-b4-v2.json` | `oi-reconciliation/2` | a1exit-reconciliation-b4 | none | 82caebb9a95e2fa237082b191cbeba157b03fc3a3793400ccf09a34405beff35 |
| `records/side-change-classes-r3.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | `records/side-change-classes-r2.json` | 1fc2bba2b5815bd79c69302acf13a6391eb326a03f062947c8fadf44cfb8f03c |

The first four are earlier drafts, byte copies of the records on the branch `records/a1-b4-rebuild-20261126` at
13eeca7085453a702bbbf00c11b8b52077c94ced, unchanged.

- `side-change-classes-r3.json` supersedes `side-change-classes-r2.json` in the same lineage.
- `reconciliation-b4-v2.json` starts a new lineage. R6.REC.7 admits a `supersedes` only between records of the same
  kind, schema and `record_id`, so an `oi-reconciliation/2` record cannot supersede the `oi-reconciliation/1` drafts.
  Those drafts stay unchanged and are not used: under amendment 3 the scanned set of R6.RECON.2 (d) holds only
  `oi-reconciliation/2` records, and both drafts name a null `M`, so neither is counted by R6.RECON.2 (e).
- R6.REC.7 requires a predecessor to pass record lint with its own review. `side-change-classes-r3.json` is therefore
  usable only when it and both its predecessors have accepting reviews.

## Bindings

- `H` = 53c6601a10419b6b333cc992474272501ab542af. The retirement ledger and edit list are the pinned control inputs of
  R6.EVID.8 (blobs ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e and ec384fdfbc12937b860e2f226355e8c5d94820a5), 44 paths.
- `M0` = eb3a69f402e9dcbe50f47e916b45c2b72772553b, `main` after the merge of #1582. The run's `M` is the predicted
  `M`, `M0` plus the tool's landing paths (R6.RECON.21); the tool's landing touches no ledgered path (R6.PLACE.8).
- `M` and `X` are null in the reconciliation record, to be completed by a superseding record of the same lineage with
  its own review. Each entry's `x` is the path's blob in every conforming candidate (`H` with all of the path's splices
  applied), whose sha256 equals the ledger's `expected_sha256`.

## Reconciliation record: one entry per drifted ledger path

Eleven of the 44 ledger paths differ between `H` and `M0`; each has one entry, with its own `ledger_binding`, splices,
protected ranges and `scientific_effect`.

| Path | Splices (identity / offset) | RC14 windows | Commits on `H..M0` | Writer's verdict |
|---|---|---|---|---|
| `AGENTS.md` | 1 (1 / 0) | 1, line | 4fb2c1eed, 8e9b83341, 9deb69568, 03fed3f5a | no-effect |
| `verification/lean/edge_rigidity_probe.py` | 17 (2 / 15) | 17, line | b6c6b80bb (#1578) | null: re-run not made |
| `papers/Main.md` | 25 (16 / 9) | 25, sentence | 4c3ad0796, 38f018c0c, eb3a69f40 | no-effect |
| `papers/SM.md` | 9 (9 / 0), retained site D032 | 9, sentence | the same three | no-effect |
| `papers/Substratum.md` | 31 (31 / 0) | 31, sentence | the same three | no-effect |
| `book/The-Incompleteness-of-Observation-FULL.md` | 83 (9 / 74) | 83, sentence | the same three | no-effect |
| `book/appendix-c-objections.md` | 15 (15 / 0) | 15, sentence | the same three | no-effect |
| `book/ch01-observation.md` | 7 (7 / 0) | 7, sentence | the same three | no-effect |
| `book/ch07-gravity.md` | 2 (2 / 0) | 2, sentence | the same three | no-effect |
| `book/ch09-universality.md` | 10 (10 / 0) | 10, sentence | the same three | no-effect |
| `book/ch18-beyond.md` | 1 (1 / 0) | 1, sentence | the same three | no-effect |

The three commits are the merges of #1560, #1580 (its temporary revert) and #1582 (its reapplication).

RC14 windows. For each splice, the window at `H` runs from the start of the first line overlapping the splice's span
to the end of the last such line; for a corpus path it is widened to every line of each splitter-v2 sentence
(abbreviations of the staged configuration) that overlaps it, at line granularity. Each of the 201 windows occurs
exactly once at `M0`, at the splice's translated offset less its distance from the window's start, and the line of the
retained site D032 (`papers/SM.md`, line 22 at `H`) occurs exactly once at `M0`. No conflict was found, so no entry
is in category 2 and no `resolutions` are needed.

Scientific effect (writer's drafts). The manuscript changes reapply the reviewed corrections of #1560 (the
Chandrasekaran-Longo-Penington-Witten construction and the status of quantum statistics); `AGENTS.md`'s changes are
procedural sections; the probe change adds conditions on the redesigned claims checker to the R7-FWD guard. No changed
range lies within three lines of a planned edit. `papers/Main.md` names D012 as the nearest planned edit in meaning (the
corrected sentence on Witten's renormalized entropy precedes it), with a `no-effect` draft. For the probe,
R6.RECON.25 requires the check re-run at the composed blob `l`; it was not run in this rebuild, so the verdict is left
null for the review, and the entry does not meet R6.RECON.25's form until a superseding record carries the verdict
established by that re-run. Each changed line of the five chapter files is present verbatim in the FULL book at `M0`.

## Side-change accounting, `H..M0`

221 changed paths (202 added, 19 modified), all regular files (mode 100644), from 16 first-parent commits. The changed
paths are computed from the full recursive trees at `H` and `M0` and checked equal to `git diff --no-renames
--name-only -z H M0`; for each path the first-parent commits that change its tree entry are listed.

| Disposition | Paths |
|---|---|
| ledgered drift, covered by `reconciliation-b4-v2.json` | 11 |
| classes of `side-change-classes-r3.json` (as in the table below) | 143 |
| tool-landing domain (added by #1557; replaced by the tool's landing files in the predicted `M`) | 54 |
| no existing class, left for the owner | 13 |

| Class | Paths | Rule |
|---|---|---|
| `m0-tool-configuration` | 1 | `.claude/settings.json` exactly, added by 4fb2c1eed (#1552) |
| `m0-trial-workflow` | 1 | `.github/workflows/a1exit-trial-verify.yml` exactly, changed by 413b0bb88 (#1543) |
| `m0-pdf-build-workflow` | 1 | `.github/workflows/pdf-build.yml` exactly, added by 02b8e2083 (#1576) |
| `m0-design-r6-record` | 34 | every path under `verification/audits/foundations/a1exit-design-r6-20261125/`, added by 3e7363330 (#1575) |
| `m0-claims-check-redesign-record` | 78 | every path under `verification/audits/infrastructure/claims-check-redesign-20261125/`, added by 5ebba1a27 (#1567) |
| `m0-research-record-1564` | 10 | every path under `verification/programmes/gravity/h-bd-1245-20261125/`, added by 6c970356c (#1564) |
| `m0-research-record-1562` | 9 | every path under `verification/programmes/oi-qm/interface/obs-emerge-1062-20261125/`, added by 503847ad6 (#1562) |
| `m0-research-record-1561` | 9 | every path under `verification/programmes/substratum/a5-linear-affine-20261104/reassess-1049-20261125/`, added by 5a39aa543 (#1561) |

Each pin binds one path to its blob at `M0`; every pin equals its predecessor's. No class has a prefix.

Paths fitting no existing class, left for the owner (13):

| Path | Status | Commits | Blob at `M0` | Nature |
|---|---|---|---|---|
| `book/The-Incompleteness-of-Observation-FULL.tex` | M | 4c3ad0796, 38f018c0c, eb3a69f40 | 5299761c54aae6781688a625da0014e6b0f69150 | generated from the restored FULL book |
| `papers/Main.tex` | M | the same three | 637f6b081da78704d1c522b9b5ca01b1e6744d6f | generated from `papers/Main.md` |
| `papers/SM.tex` | M | the same three | 398a84ac8e2b7cb5b61a53f11196244e2e165beb | generated from `papers/SM.md` |
| `papers/Substratum.tex` | M | the same three | 04a6830b29e74703daf2e537d0060a548615fc75 | generated from `papers/Substratum.md` |
| `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` | M | the same three | d07842a4235af2b68cc12b8d7462f6c6967f6d6d | integration result changed with the corrections |
| `tools/claims_check_r4.py` | A | b6c6b80bb (#1578) | 745e2a3d887351672fdd05881d5d55b8f3720525 | redesigned claims checker |
| `tools/claims_check_r4_controls.json` | A | b6c6b80bb | 1e4a0e7cb2c9513d2934a67e301a5f8d484d0f7b | its controls |
| `tools/claims_check_r4_gap.json` | A | b6c6b80bb | 3dd14f1abd1565e19391319d17c4ea42a3574e5a | its gap record |
| `tools/claims_check_r4_test.py` | A | b6c6b80bb | 19bba6a7848ac30ab957556f0077af2c0ee08115 | its tests |
| `tools/proof_census.py` | M | b6c6b80bb | d841770e490c3f609de192d91b4b2192198ff742 | changed with the checker |
| `tools/release_gate.py` | M | b6c6b80bb | 9c11f64f063eaf2e53467c5f66b7558e47a244e9 | gate runs the checker report-only |
| `verification/infrastructure/claims-check/licences.json` | A | b6c6b80bb | 00ee67fbd5bc446587735210732c903059199f03 | checker licences |
| `verification/infrastructure/claims-check/reviews.json` | A | b6c6b80bb | e7e2365b79afd5056a342be8843f7a4bced178c6 | checker review records |

In the predicted `M` two further paths fit no class here: the tool's own records
`verification/audits/foundations/ledger-coverage-tool-20261123/records/side-change-classes-v1.json` and `-v2.json`,
under the tool-landing prefix and not listed by the tool-landing class record.

While any of these paths is unclassified, RC11 fails for every entry of the reconciliation record, and every drifted
path stays `base-drift`.

## What the records do not cover

The records in this directory, and their review records, are not side changes of a run that reads them from a record
commit whose single parent is the run's record base (R6.RECON.2 (c)). Once they reach `main` they are side changes of
later runs, classified by a class record landed after them (amendment 1, part C).
