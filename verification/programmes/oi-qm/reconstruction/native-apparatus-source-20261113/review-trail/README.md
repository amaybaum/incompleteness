# TUNE-1 sourcing unit: review trail

Historical review records of the TUNE-1 sourcing unit, whose r2 text, r1 review, r2 confirmation and
objects file are retained under `../support/tune-confirmed/` and `../support/tune-published/`. These
files change no claim, status or verdict of this directory or of any other record. They are not
support for the assessment in this directory; its uses of the sourcing unit are those
`../RETENTION.md` states.

**Source.** Draft PR #1272, branch `research/tune1-sourcing-1236-20261113`, head
`c539a60c5081540be033e07aa4f141caa1d0014b`, directory
`verification/programmes/oi-qm/reconstruction/drafts/tune-1-sourcing-20261113/`. Each file is a
byte-identical copy: `git hash-object` reproduces the blob listed.

**Authority.** Owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7029588625, item 4): "#1276
and #1272: preserve the review trails through narrow preservation PRs."

| File | Content | Blob | SHA-256 | Bytes |
| --- | --- | --- | --- | --- |
| `TUNE-1-SOURCING-r1.md` | sourcing unit r1, the object of `REVIEW-r1.md` | `e21299f97c022c724b85f02d714b4644d0f8d87d` | `5d1d96fc37a9ae003e5c829fd4907240800a26d0a42c6568d8f204860b168d0b` | 34160 |
| `NOTES-r1.md` | writer's notes, r1 | `5ac597e96cd8177f833f8d4b86a879c19ee77480` | `e96229a247caec1ba6ef466af61b37fb9383d6405ae6659f6082385d3e1b1de3` | 2823 |
| `RESPONSE-r1.md` | dispositions of the r1 review findings | `66c38e4fdc0d80e4fa94138ae6e04317c4b5c925` | `a3c216695c37df29b7fc1ed205278fad5d574264c17009d3458d2be923cce0c6` | 4446 |
| `NOTES-r2.md` | writer's notes, r2 | `a1af11feef801638cb56bd4d19687d660a70ac11` | `49f6531833c3da79fb3a35e659144abf5b96eea53e9e2d89056a0b79145bae75` | 3137 |

`TUNE-1-SOURCING-r2.md`, `REVIEW-r1.md`, `CONFIRM-r2.md` and `OBJECTS.md` from the same head are not
copied again: their blobs are the files under `../support/tune-published/`.

**Reading these files.** Relative names inside them refer to the original directory on #1272; the
files not in this directory are under `../support/tune-published/`. `RESPONSE-r1.md` here is the
version at the PR head, after the cosmetic nit of the r2 confirmation was applied; the reviewed
version's SHA-256 and the change are recorded in `../support/tune-published/OBJECTS.md`. Commits named
inside `TUNE-1-SOURCING-r1.md` that are not ancestors of `main` (`8228b3c2`, `9f7d2612`) are
provenance. The reviews are model reviews: evidence of review, not independent mathematical
verification.
