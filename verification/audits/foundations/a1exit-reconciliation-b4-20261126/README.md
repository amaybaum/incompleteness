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
- 2026-11-26T08:28:18Z, comment 7186638587: item 4, "Authorize the two proposed classes." (the five generated and
  result files with the corresponding rebuilt PDFs when available; the eight claims-checker files) "Pin each path
  individually. Do not use wildcard classifications that automatically admit future files. Require independent
  review of the class records."; item 5, the probe re-run is authorized for the B4 reviewer; item 6, "Start the `/2`
  records in their own lineage. Preserve the two `/1` drafts byte-for-byte as historical, unreviewed evidence."

Rules applied: design r6 as amended by amendments 3 and 4
(`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md`, `AMENDMENT-3.md` and `AMENDMENT-4.md` at
939a79c2e3da55cb87bd15467c0f6e9207bb1140): R6.RECON.1 to R6.RECON.5, R6.RECON.15,
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
| `records/reconciliation-b4-v2-r2.json` | `oi-reconciliation/2` | a1exit-reconciliation-b4 | `records/reconciliation-b4-v2.json` | b7418b408589fc70652f626a2c504e49edb35bbaa2706461cc7f2ed0b1473c84 |
| `records/side-change-classes-r4.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | `records/side-change-classes-r3.json` | d041ecf2d98ea6a7fe11b4000e8a1dbce733f50f8a0f61927ff69fbddcb5bb01 |

The first six are earlier drafts, byte copies of the records on the branch `records/a1-b4-r3-20261126` at
78c048c67451807615fe61354d0b36ace6e15f60, unchanged; the last two supersede them.

- `side-change-classes-r4.json` supersedes `side-change-classes-r3.json` in the same lineage. It keeps the eight
  classes, every pin re-derived at `M0`, and adds the two classes the owner approved.
- `reconciliation-b4-v2-r2.json` supersedes `reconciliation-b4-v2.json`: the `papers/SM.md` entry is re-derived at
  `M0` after #1589; the other ten entries are unchanged.
- The `/2` records form their own lineage (owner decision, item 6). The two `oi-reconciliation/1` drafts are kept
  byte-for-byte as historical, unreviewed evidence and carry no current authority. Their exclusion follows the
  adopted schema rules, not an exemption: R6.REC.7 admits a `supersedes` only between records of the same kind, schema
  and `record_id`, and the scanned set of R6.RECON.2 (d) holds only `oi-reconciliation/2` records, so no run reads
  them.
- R6.REC.7 requires a predecessor to pass record lint with its own review: each superseding record here is usable only
  when it and every predecessor on its chain have accepting reviews.

## Bindings

- `H` = 53c6601a10419b6b333cc992474272501ab542af. The retirement ledger and edit list are the pinned control inputs of
  R6.EVID.8 (blobs ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e and ec384fdfbc12937b860e2f226355e8c5d94820a5), 44 paths.
- `M0` = c31d739c02911faaa9612824c48977b39717de05, `main` after the merges of #1563 and #1589. The run's `M` is the predicted
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
| `papers/SM.md` | 9 (9 / 0), retained site D032 | 9, sentence | the same three and c31d739c0 (#1589) | no-effect (names D034, D389, D390, D391) |
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

Scientific effect (writer's drafts). The manuscript changes of #1582 reapply the reviewed corrections of #1560 (the
Chandrasekaran-Longo-Penington-Witten construction and the status of quantum statistics); `AGENTS.md`'s changes are
procedural sections; the probe change adds conditions on the redesigned claims checker to the R7-FWD guard. No changed
range lies within three lines of a planned edit. `papers/Main.md` names D012 as the nearest planned edit in meaning
(the corrected sentence on Witten's renormalized entropy precedes it), with a `no-effect` draft.

`papers/SM.md` also carries #1589, which replaces the undefined "six structural properties" (line 1394) by "the
assumptions of the local spatial and gauge construction (§2.3)". The structural predictions' scope then refers to the
list in §2.3, whose phrase "a set S, finite under A1" D034 edits to "a set S". The entry names D034, and D389, D390 and
D391 (which keep a finite scope where the counting measure is used), with a `no-effect` draft; whether every listed
structural prediction holds without a finite S is the question the review must decide, and this is the least certain
of the drafts.

For the probe, R6.RECON.25 requires the check re-run at the composed blob `l`. The owner authorized that re-run for the
B4 reviewer (item 5); the writer did not run it, so the verdict is null and the entry does not meet R6.RECON.25's form
until a superseding record carries the verdict the re-run establishes. Each changed line of the five chapter files is
present verbatim in the FULL book at `M0`.

## Side-change accounting, `H..M0`

227 changed paths (207 added, 20 modified), all regular files (mode 100644), from 18 first-parent commits. The changed
paths are computed from the full recursive trees at `H` and `M0` and checked equal to `git diff --no-renames
--name-only -z H M0`; for each path the first-parent commits that change its tree entry are listed.

| Disposition | Paths |
|---|---|
| ledgered drift, covered by `reconciliation-b4-v2-r2.json` | 11 |
| classes of `side-change-classes-r4.json` (as in the table below) | 157 |
| tool-landing domain (added by #1557; replaced by the tool's landing files in the predicted `M`) | 54 |
| no existing class, left for the owner | 5 |

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
| `generated-manuscript-artefacts-witten` | 6 | exactly `book/The-Incompleteness-of-Observation-FULL.tex`, `papers/Main.tex`, `papers/SM.tex`, `papers/Substratum.tex`, `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` (4c3ad0796, 38f018c0c, eb3a69f40; `SM.tex` also c31d739c0) and `papers/SM.pdf` (c31d739c0, #1589) |
| `claims-checker-r4` | 8 | exactly `tools/claims_check_r4.py`, `tools/claims_check_r4_controls.json`, `tools/claims_check_r4_gap.json`, `tools/claims_check_r4_test.py`, `tools/proof_census.py`, `tools/release_gate.py`, `verification/infrastructure/claims-check/licences.json`, `verification/infrastructure/claims-check/reviews.json`, all b6c6b80bb (#1578) |

Each pin binds one path to its blob at `M0`; the first eight classes' pins equal their predecessors'. No class has a
prefix. The rebuilt PDFs of `Main`, `Substratum` and the FULL book are not on `main` and are not pinned; once they land
they are side changes that need a superseding class record pinning their blobs.

Paths fitting no class, left for the owner (5), all added by 83e08bd9a (#1563, the OI-string bridge audit):

| Path | Blob at `M0` |
|---|---|
| `verification/audits/foundations/oi-string-bridge-1556-20261125/CHANGES-r2.md` | 78038646d28ebdcd0e8d38f7a2b0d0ee7cb6de09 |
| `verification/audits/foundations/oi-string-bridge-1556-20261125/CHANGES-r3.md` | 0f4741f2fff2e54de3ee4b4d68c34e16f47d8213 |
| `verification/audits/foundations/oi-string-bridge-1556-20261125/REPORT-r2.md` | 06e1df958fe18d10f662b7deb78573a936d43e92 |
| `verification/audits/foundations/oi-string-bridge-1556-20261125/REPORT-r3.md` | 82b7542398deb4af1f972917df32804cf601d793 |
| `verification/audits/foundations/oi-string-bridge-1556-20261125/REPORT.md` | 2ba953693220962883d2d41a39f3ae8456e912d4 |

In the predicted `M` two further paths fit no class here: the tool's own records
`verification/audits/foundations/ledger-coverage-tool-20261123/records/side-change-classes-v1.json` and `-v2.json`,
under the tool-landing prefix and not listed by the tool-landing class record.

While any of these paths is unclassified, RC11 fails for every entry of the reconciliation record, and every drifted
path stays `base-drift`.

## What the records do not cover

The records in this directory, and their review records, are not side changes of a run that reads them from a record
commit whose single parent is the run's record base (R6.RECON.2 (c)). Once they reach `main` they are side changes of
later runs, classified by a class record landed after them (amendment 1, part C).
