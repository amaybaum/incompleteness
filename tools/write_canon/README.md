# write_canon

A research and implementation tool (WRITE-CANON-1, authorized on #1169, comment 7080958038) for
automated Issue comments on this repository. It does not replace the existing comment helpers.

```sh
python3 -I tools/write_canon/write_canon.py check BODY.md [--stored STORED.md] [--online]
python3 -I tools/write_canon/write_canon.py post ISSUE BODY.md --receipt RECEIPT.json
python3 -I -m unittest discover -s tools/write_canon
```

`check` writes nothing to GitHub. It reports three separate results: integrity (hashes, forbidden
characters and, with `--stored`, byte identity with the normalized body), link validity, and the
construct inventory. A byte match establishes the first only. `post` makes one
`gh api -X POST repos/amaybaum/incompleteness/issues/<n>/comments` call and verifies the stored
comment afterwards; detection follows the write and does not prevent it. Its lock, `HALT` and
`PENDING` markers live in `~/.write-canon/`; a human clears a marker after reviewing it. The design,
tests and acceptance criteria are in `PLAN.md`.

**Limits.** The scanner accepts only the constructs listed in `PLAN.md` and fails closed on the
rest. It does not inventory GitHub's own autolinking of `#123` references or commit-like hex
strings, and it does not check the targets of Issue and comment links. Offline, a blob link to
another repository is unverified and fails, and `post` refuses it. A blob link to this repository
is checked for its commit and path in the local object store, and its commit must be reachable from
a local `refs/remotes/origin/*` ref; those refs are as of the last fetch and may lag GitHub, and
anyone with write access to the local repository can forge them. Only `check --online` asks
GitHub itself: for each blob link it settles whether GitHub serves that path at that commit for
that repository.

The lock and markers are local to one account on one machine: a post from another account or
machine does not see them. As a cheap guard across them, `post` reads the Issue's comments from
the last seven days (one read-only GET, `per_page=100`) and refuses if any body equals the
normalized source, or if the listing is incomplete. The guard catches exact copies only: an
earlier post of the same source that the write path altered, such as one whose U+00A0 was stored
as U+0020, does not equal the normalized source and is not caught.

The receipt is created with a hard link so that it never replaces a file. On a filesystem without
hard links, a post that was written and verified therefore halts with "receipt not written".

**Fixtures** are captures of real bodies: the #1169 Issue body as submitted and as stored with its
link destinations wrapped in backticks (the stored capture ends in one newline more than the
normalized body), the blob-link round trip on #1548 (comment 7080042581) and the #1548 receipt
(comment 7080894635). Before committing, they were scanned for secrets, e-mail addresses and local
paths. In the #1169 pair, sixteen agent names written like home-directory paths were renamed,
keeping their length, and one closing keyword before an Issue number was reworded (`close` to
`shut`, one byte shorter); neither change alters a construct or a link.
