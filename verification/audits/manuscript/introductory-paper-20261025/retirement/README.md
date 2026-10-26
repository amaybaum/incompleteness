# Explainer retirement: content-migration audit and retirement plan

**Status: plan, independently reviewed.** Owner decision (2026-10-26): the Introduction paper replaces
`papers/Explainer.md`, which is retired as a legacy document preserved for provenance. The retirement is approved
conditional on independent review and acceptance of the Introduction; nothing here changes a file outside this
directory.

- `MIGRATION-r3.md` and `RETIREMENT-r3.md`: the plan in force.
  - Migration: no Explainer content needs migrating into the Introduction, Main or the book. `Main.md:66` is
    repointed to Substratum §6.2.
  - Retirement: after the Introduction's acceptance, one PR with two commits (C1 the Introduction, C2 the
    retirement). C2 moves the file to `papers/legacy/Explainer.md` with a superseded notice, leaves a redirect stub at
    `papers/Explainer.md`, and makes every dependent change in the same commit.
  - §2.5 (historical reproducibility): no receipt, seal, certificate or record is rewritten, and old paths in
    immutable records stay as written.
- Earlier revisions, each the object of the review named:
  - `MIGRATION.md`, `RETIREMENT.md` (r1): `review/REVIEW.md`, ACCEPT WITH CHANGES.
  - `*-r2.md`: `review/RECHECK-r2.md`, ACCEPT WITH NITS.
  - `*-r3.md` apply those nits and nothing else.
- `CHANGES-r2.md`, `CHANGES-r3.md`: the change notes.
- `review/probes/count.py`: the reviewer's counting helper. The reviewer's working copies of
  `verification/lean/edge_rigidity_probe.py` and `tools/v3_verifier.py`, and the dry-run trees, are not retained;
  they are copies of files at `main` `687e885b`.

In every file here the absolute scratch-directory prefix is written `S`. The records' `S/paper/mainwt` is a
checkout of `main` `687e885b`.
