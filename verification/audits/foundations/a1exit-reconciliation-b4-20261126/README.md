# A1 sequencing safeguard: reconciliation and side-change class records (unreviewed)

Status: **unreviewed drafts.** No record in this directory has an independent review record. Under design r6 none
may be used by any run until a non-author reviewer re-derives it from the git object store and writes an
`oi-review-record/1` naming its exact blob (R6.REC.2, R6.REC.6). RT-L2 is never PASS on a drafted record
(R6.RECON.21); these drafts release nothing. Records strengthen no claim (R6.PLACE.9).

Authority (owner `amaybaum`, coordinating session, recorded on #1169):

- 2026-11-26T04:39:58Z, comment 7182798225: "B4 | Approved. Draft the two required records on a separate branch and
  obtain independent review."
- 2026-11-26T04:52:48Z, comment 7182986451: "M and X commit identifiers | Complete them when the actual commits exist,
  using independently reviewed superseding records." and "In-place record edits | Correct them using the required
  supersession procedure, preserving history."
- 2026-11-26T05:53:39Z, comment 7183914927: "F2 — Unclassified side changes | Complete the B4 side-change
  classification records. Every changed path must be accounted for. Do not introduce a blanket exemption." and, after
  the landing of #1580, "Then rebuild the B4 records against the resulting `main`."

The rules applied are those of design r6 (`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md`)
as amended by amendment 1 (pull request #1579, head 828de4be1e41c2fa1aef28b7a60ba307ac5b2182, awaiting the owner's
acceptance): sec. 20 R6.TREE.4 to R6.TREE.8, sec. 23 R6.RECON.1, R6.RECON.2 and R6.RECON.21, sec. 11 R6.REC.7, and
R6.EVID.8.

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169), the exception-free verification route; these records decide only
whether RT-L2 and RT-O9 can be released for the tool's landing.

Placement. This is a reconciliation directory (R6.RECON.1): under `verification/audits/`, outside every prefix of the
tool-landing class (`tools/ledger_coverage/`, `verification/audits/foundations/ledger-coverage-tool-20261123/`) and
the exact path `.github/workflows/ledger-coverage.yml`, outside the plan's record directory
(`verification/audits/foundations/a1exit-deletion-20261121/`), and holding no ledgered or corpus path.

## Files

| Path | Schema | `record_id` | `supersedes` | sha256 |
|---|---|---|---|---|
| `records/reconciliation-agents-md.json` | `oi-reconciliation/1` | a1exit-reconciliation-agents-md | none | 331c06740385fc25bd131edb7c93496a240fe9844c9d8a085593a024497aefd9 |
| `records/side-change-classes-m0.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | none | e422fc5c441f58fd536188fa8a9f7c3a58c8e5e7d9c94779df23dee96cdc4af2 |
| `records/reconciliation-agents-md-r2.json` | `oi-reconciliation/1` | a1exit-reconciliation-agents-md | `records/reconciliation-agents-md.json` | cf14d6a948d37927290b0fcd8c43ccc8c79e38bcc8af145f25d31f5e5c288bb1 |
| `records/side-change-classes-r2.json` | `oi-side-change-classes/1` | a1exit-side-change-classes-m0 | `records/side-change-classes-m0.json` | fbc1ceddea1d5ef2811745bb39f8cdbfe7c30a2f41503927d019f56b96f45929 |

The first two are the earlier drafts, bound to `M0` = e8271d9d64e51cc6eb69a53ea2f5b80d490503a4 (the head of #1580
before its merge). They are byte copies of the records drafted on the branch `records/a1-b4-20261126` at
a759980af1827758d3231551133f271e931e0487, unchanged, so that each `supersedes` names a record present at its path in
this tree (R6.REC.7, R6.RECON.2 (d)). The `-r2` records supersede them; nothing is edited in place.

Supersession and review. R6.REC.7 requires the predecessor named by a `supersedes` to pass record lint itself, with
its own review. Each `-r2` record therefore becomes usable only when both it and its predecessor have an accepting
`oi-review-record/1` by a non-author reviewer in this directory. A review of a predecessor judges it against its own
stated `M0`.

## Bindings

- `H` = 53c6601a10419b6b333cc992474272501ab542af. The retirement ledger and edit list are the pinned control inputs of
  R6.EVID.8 (blobs ba37c1cdb560cb5fceeeb2b46a3091c832b4a80e and ec384fdfbc12937b860e2f226355e8c5d94820a5).
- `M0` = 38f018c0c240df8a8bfa21d8a276dc6b65d98b6a, `main` after the merge of #1580. Its tree
  (7b51d43e6ee657dd873cd0fe7e17ce6828e9c308) equals the tree of the earlier `M0`, so every blob pin and every
  `AGENTS.md` value is the same at both; the first-parent commits on `H..M0` that change each pinned path are also the
  same. The run's `M` is the predicted `M`, `M0` plus the tool's landing paths (R6.RECON.21); the tool's landing
  touches no ledgered path (R6.PLACE.8).
- `C` = `X` = `X_rep` (R6.EVID.8). The reconciliation record leaves `M` and `X` null; they are completed by a further
  superseding record of the same lineage, with its own review, once those commits exist.

## Enumeration

The changed paths of `H..M0` are computed twice and compared: from the full recursive trees (`git ls-tree -r -z
--full-tree` at `H` and at `M0`, every entry whose mode, type or object differs) and from `git diff --no-renames
--name-only -z H M0`; the two lists are equal. `H` is on `M0`'s first-parent chain (`git rev-list --first-parent`).
For each path, the first-parent commits on `H..M0` that change its tree entry are listed. Every changed entry at `M0`
is a regular file (mode 100644).

RT-L2 and RT-O9 evaluate two further segments (the A1 controls at the tool revision
adb8fc4380b9ce7d7f2decbf0c1b7c211f550793): `H..Mp`, with `Mp` = `M0` plus the tool's landing files (63 paths under
the tool-landing domain at that revision), and `H..M9`, with `M9` = `Mp` plus the plan's record directory as a
stand-in `F` holds it (8 paths). Their changed paths are the 198 below, the 9 landing paths not on `M0`, and, for
`H..M9`, the 8 record-directory paths.

## Accounting

`H..M0`: 198 changed paths (196 added, 2 modified), changed by 14 first-parent commits.

| Disposition | Paths | Rule |
|---|---|---|
| ledgered drift, reconciled by `reconciliation-agents-md-r2.json` | 1 | `AGENTS.md`, a path of the retirement ledger (splice D296), changed by 4fb2c1eed, 8e9b83341, 9deb69568 and 03fed3f5a, all after the splice; RC1 to RC10 and RC12 re-derived at `M0` |
| class `m0-tool-configuration` | 1 | `.claude/settings.json` exactly, added by 4fb2c1eed (#1552) |
| class `m0-trial-workflow` | 1 | `.github/workflows/a1exit-trial-verify.yml` exactly, changed by 413b0bb88 (#1543) |
| class `m0-pdf-build-workflow` | 1 | `.github/workflows/pdf-build.yml` exactly, added by 02b8e2083 (#1576) |
| class `m0-design-r6-record` | 34 | every path under `verification/audits/foundations/a1exit-design-r6-20261125/`, all added by 3e7363330 (#1575) |
| class `m0-claims-check-redesign-record` | 78 | every path under `verification/audits/infrastructure/claims-check-redesign-20261125/`, all added by 5ebba1a27 (#1567) |
| class `m0-research-record-1564` | 10 | every path under `verification/programmes/gravity/h-bd-1245-20261125/`, all added by 6c970356c (#1564) |
| class `m0-research-record-1562` | 9 | every path under `verification/programmes/oi-qm/interface/obs-emerge-1062-20261125/`, all added by 503847ad6 (#1562) |
| class `m0-research-record-1561` | 9 | every path under `verification/programmes/substratum/a5-linear-affine-20261104/reassess-1049-20261125/`, all added by 5a39aa543 (#1561) |
| tool-landing domain | 54 | under `tools/ledger_coverage/`, `tools/ledger_coverage.py` or the tool's audit directory, added by e2e2a6232 (#1557); replaced by the tool's landing files in `Mp` (see below) |

Each class pin binds its path to the blob at `M0` and lists the commits that changed it; in each class the rule's
directory or exact path holds no changed path outside the class. No class has a prefix, and no entry stands for
more than one path. The class ids and reasons are those of the earlier record, which pinned the same 143 paths at the
same blobs.

`H..Mp` and `H..M9`: of the 63 tool-landing files, 60 are classified `tool-landing` by the tool's class record
(`side-change-classes-v3.json`, on the tool branch) and one, that record itself, `class-record`. The plan's 8
record-directory paths in `H..M9` are classified `record-directory` (R6.RDIR.10).

Paths fitting no existing class in this directory, left for the owner (2, both in `H..Mp` and `H..M9`):

| Path | Commit | Nature |
|---|---|---|
| `verification/audits/foundations/ledger-coverage-tool-20261123/records/side-change-classes-v1.json` | added on `main` by e2e2a6232 (#1557); same blob (de843294dbc46769eca5553739f1b296290534b2) at the tool revision | the first record of the tool-landing class's lineage, under the tool-landing prefix and not listed by `side-change-classes-v3.json` |
| `verification/audits/foundations/ledger-coverage-tool-20261123/records/side-change-classes-v2.json` | 6a6e200f3 on the tool branch, not on `main` (blob 8e01d90c05f06a1f8f36a0c00a75c88e7abb4455) | the second record of that lineage, likewise not listed |

Both belong to the tool-landing class, which is defined once, in the tool's own class record (R6.TREE.5); a class
here cannot define it again, and no class here describes them.

## What the records do not cover

The records in this directory, and their review records, are not side changes of a run that reads them from a record
commit whose single parent is the run's record base (R6.RECON.2 (c)). Once they reach `main` they are side changes of
later runs, classified by a class record landed after them (amendment 1, part C).
