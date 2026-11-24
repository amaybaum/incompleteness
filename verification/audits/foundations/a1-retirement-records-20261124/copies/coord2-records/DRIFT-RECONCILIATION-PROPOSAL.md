# A1 plan: reconciliation proposal for `main` drift after the scientific base (DRAFT, for review)

Status: proposal only, prepared under the owner decision of 2026-11-23 ("treat the §A.49 merge as a
real baseline change; do not suppress the drift failure or silently update the baseline; prepare a
separately reviewable reconciliation proposal; classify `.claude/settings.json`"). It changes no
plan, record or baseline, and authorizes nothing.

## Measured facts (read-only, local repository)

- Scientific base `H` = `53c6601a10419b6b333cc992474272501ab542af`; frozen plan `P` =
  `4c79be642ca631573f06b444903be75ec4f5e2b6`; current `main` `M` =
  `4fb2c1eed350edf95da2b316abcca93717246589`.
- `H` is on `M`'s first-parent chain; two first-parent commits lie between them:
  - `413b0bb8` Merge #1543 (A1-EXIT trial workflow);
  - `4fb2c1ee` Merge #1552 (AGENTS.md §A.49 and `.claude/settings.json`).
- Paths changed from `H` to `M` (3): `.claude/settings.json` (added, 7 lines),
  `.github/workflows/a1exit-trial-verify.yml` (modified, +6/-5), `AGENTS.md` (modified, +32).
- Of the 44 files the plan's `edits.json` ledgers, exactly one changed: `AGENTS.md`. No `papers/` or
  `book/` path changed.
- The plan's only AGENTS.md splice, D296, has its `old` text exactly once in both `H` and `M`, at the
  same byte offset (2305, line 37). The 32 added lines are appended after the last section; no
  byte before them changed.

## Classification proposed for each side change

| Path | Changed by | Proposed class | Tool outcome without a record |
|---|---|---|---|
| `AGENTS.md` | #1552 | ledgered path, append-only change outside every splice span: base drift to reconcile | FAIL `base-drift` (correct; not to be suppressed) |
| `.claude/settings.json` | #1552 | side change, tooling configuration, not ledgered, not corpus | REVIEW `side-change-unclassified` |
| `.github/workflows/a1exit-trial-verify.yml` | #1543 | side change, trial workflow (an example class named in the design, sec. 13.1) | REVIEW `side-change-unclassified` |

## Options for `AGENTS.md` (owner choice)

1. **Re-base at the plan amendment (recommended).** The exception-free route already amends and
   re-freezes the plan. At that point the ledger base for `AGENTS.md` is re-resolved to the blob at
   the new freeze's `main`, D296 is re-verified there (its `old` text is unique and unchanged), and
   the ledger records the new `base_sha256` with the reason (the §A.49 append). The drift then
   disappears because the base is updated openly, under review, not silently.
2. **Reconciliation record at landing.** Keep `H` as the base and, at landing, write a reconciliation
   record (design sec. 13.3) showing that `L`'s `AGENTS.md` equals `M`'s bytes with D296 applied at
   the translated offset. Sec. 13.3 allows this only for side changes the freeze could not foresee;
   this one is known now, so option 2 fits poorly if the freeze happens after today.
3. **Do nothing.** The landing check FAILs `base-drift` and the retirement cannot land. Not viable.

Either option needs the ownership chain: a written record, an independent non-author review that
re-derives the facts above from git objects, and the owner's authorization naming the record's path
and blob sha256.

## Proposed side-change class records

- `tooling-config`: `.claude/settings.json`. Reason: a tool configuration file, read by Claude Code
  only, outside the corpus and the ledger.
- `trial-workflow`: `.github/workflows/a1exit-trial-verify.yml`. Reason: the A1-EXIT trial workflow
  itself (#1543), outside the corpus and the ledger.

Each is a record under the ownership chain, frozen with the amended plan.

## What this proposal does not do

It amends no plan, writes no record into the repository, changes no baseline, and runs nothing.
The checks that measure these facts at the moment of the freeze are the tool's own (RT-L2 and the
four-tree roles); the figures here are a preview.
