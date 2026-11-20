# EOI classification-audit package r3: preserved bytes

`eoi-audit/PACKAGE.md` is the consolidated EOI retrospective classification-audit package, revision
r3, preserved byte for byte because a record on `main` cites it by SHA-256. Preservation adopts no
premise, promotes no claim and changes no status; no correction in the package is adopted by its
presence here (§A.46 items 1 and 3).

| File | SHA-256 | Blob | Bytes |
| --- | --- | --- | --- |
| `eoi-audit/PACKAGE.md` | `33075f9f2e4df52cf87536ebcb8c8c931f89960e3a067af30c182587f3109b74` | `8e5808e559cf03fd22b1beb5293902741ba148e4` | 49831 |

`sha256sum eoi-audit/PACKAGE.md` reproduces the SHA-256, and `git hash-object` the blob.

**Citation on `main`.** `verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/preregistration.md`,
lines 124 and 884–885, names `PACKAGE.md` r3 by the full SHA-256 above; the round's record is frozen
and is not edited. Its §A.42 item 8 table classifies the package as provenance for the question's
wording; precondition 1 of `F` takes it as an input by hash. These bytes make that hash resolvable
from `main`.

**Source.** Closed draft PR #1270 (retired to #1428), branch `research/recovered-1169-20261113`, head
`4cd3987118399b8f9ab8fcaaf36a96fd366ec762`, same path. That branch recovered the file from session
storage (original location `eoi-audit/PACKAGE.md`, 2026-11-08); its `README.md` and `FILES.tsv` record
the recovery.

**Status as recorded.** Model-written and model-reviewed, not human verification: r2 was reviewed
ACCEPT, and r3 applies that review's non-blocking items (package §1). Owner acceptance, quoted in
#1169 comment 6726546702 (posted under `amaybaum`, 2026-11-08T20:14:25Z): "accept the consolidated
audit package (PACKAGE r3, 33075f9f) as the reconciled findings without adopting any correction".

**Authority.** Owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7029588625, item 4): "#1270
(closed, retired to #1428): selectively preserve the evidence that `main` cites by hash, the EOI
PACKAGE r3, through a new PR. The original 75-file package is not landed."

**Reading the file.** Its relative names (`AUDIT-C1.md` to `AUDIT-C5.md`, `REVIEW-*.md`,
`../gate/GATE-DRAFT.md`, earlier package revisions) refer to its original directory layout. Those
files are not preserved here; they remain on #1270's branch, and the package's own §10 classifies
them as support off `main` for its findings. The only full commit id in the file, `5ce4f98e…`, is an
ancestor of `main`.
