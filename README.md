# Session handoff, 2026-10-17 (temporary; not evidence; never merge)

This parentless branch, `tmp/session-handoff-20261017`, carries a working session's state to the next session. It
shares no history with `main`. It is never merged and adopts nothing:
- nothing here is a record of any round, receipt or certificate;
- nothing here is cited by a frozen record;
- nothing here is adopted as data.

Where it holds copies of evidence, those copies are for recovery only; the authoritative statements are where the
records say. It is public, like every branch of this repository.

**Start with `HANDOFF.md`.** It covers the state of every open thread, the owner's decisions and standing constraints,
what is pending, and how to restore the preserved objects.

| Path | What it is |
| --- | --- |
| `HANDOFF.md` | the state and next steps |
| `records/` | the owner's decisions, incident records, the cleanup ledger, the archiver pilot's evaluation and design, and the accepted tranche-2 inventory |
| `preservation/` | git bundles and a pack holding commits and objects that are on no `main` ref, with digests (see `HANDOFF.md` §6) |
| `wip/` | unreviewed working material: the off-main design prototype's code, the F2 census checks, the hvalid scripts, the #829 import-bridge experiment drafts, R2-B's memo, the research-track notes, the artifact validator's local evidence, and patches of uncommitted local edits |
| `SHA256SUMS` | the sha256 of every file on this branch |
