# b4: local-only commits (2026-10-17)

These are the 56 commits that existed only in this session's container on 2026-10-17. None is reachable from a host
ref (the 1,004 heads and pull heads listed at the time of the check), and none is in b1–b3,
`local-only-commits-20261017.bundle` or `offmain/exact-objects.pack`.

- **`local-only-supplement-56-20261017.bundle`:** 27 tip refs `refs/lo/<id>` (`heads.txt`), thin against the host's
  refs. `git bundle verify` succeeds in a repository holding the host's refs. With its base objects available,
  `index-pack --fix-thin` recovers all 56 commits (`commits.txt`).
- **The cited one:** `7de2d5496057c5784e67c146368a02cc31a10fb5`, "TRB-1 design: header without the ambient-norm
  identifier; census family name final", parent `6027be54`. It is the local tip of `claude/trb1-dev`; the host's
  `claude/trb1-dev` is at its parent. `round-trb-1-transitive-body/preregistration.md:110` and `:207` cite it as
  `7de2d549`. The off-main design listed it as unrecoverable, because the host refuses it and its survey clone did
  not hold it.
- **Scan:** 179 new blobs were scanned. There are no token, key or signed-URL matches and no e-mail addresses. The
  only identities not in main's history are the placeholders `r@x`, `s@x` and `sim@invalid`.

## Restoring (verified 2026-10-17 in a fresh clone)

The bundle is thin: its pack names 24 prerequisite commits instead of carrying them. Every one is reachable from
three host branches: `main` (22 of them), `claude/trb1-dev` at `6027be54` and `claude/comp1-dev` at `cb37b45b`.
A clone holding those three branches is enough; nothing else is needed.

```sh
git clone --bare --single-branch --branch main https://github.com/amaybaum/incompleteness r.git
cd r.git
git fetch origin '+refs/heads/claude/trb1-dev:refs/heads/claude/trb1-dev' \
                 '+refs/heads/claude/comp1-dev:refs/heads/claude/comp1-dev'
git bundle verify <path>/local-only-supplement-56-20261017.bundle
git fetch <path>/local-only-supplement-56-20261017.bundle 'refs/lo/*:refs/lo/*'
git fsck --connectivity-only --no-dangling
```

Result, in a new clone with no alternates (git 2.43.0; `main` at `49ba3297`, the two branches at the ids above):

- `git bundle verify` succeeds and the fetch writes the 27 refs of `heads.txt`, with the same ids.
- `git fsck --connectivity-only` is clean.
- The commits reachable from `refs/lo/*` and not from the three branches number 59. They are the 56 of
  `commits.txt`, plus `0004afc9`, `17de29c2` and `62ad3a5f`, which no host ref holds but which are in
  `offmain/exact-objects.pack` (`0004afc9` is also retained by the tranche-2 refresh).
- `7de2d5496057c5784e67c146368a02cc31a10fb5` is present: a commit with parent `6027be54` and the subject above.

If either branch moves or is deleted, its old head is still a prerequisite: fetch that id by full SHA, or restore it
from b1–b3 or `offmain/exact-objects.pack` before fetching the bundle.
