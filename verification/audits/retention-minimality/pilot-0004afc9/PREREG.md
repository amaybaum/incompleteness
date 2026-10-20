# Tranche-2 pilot — preregistered selection and classification rule

Fixed before the head's closure, citations or regeneration were measured.

## Inputs

- Archive: `verification/audits/evidence-retention/` at `main` `92de3143046b26d7fa2ce3b13ce3ea4b1e18a37a`
  (identical to baseline `D` `6fe84106e842465f086c9bf301c82781421c0bfd` for that directory).
- Object manifest blob `2ee4fbb95118115b4fb874b3c59c65e1b155aec9`; evidence manifest blob
  `191d16654d8b98d33e0ffe57c2986677d76e0b11`.

## Selection rule (S)

The pilot head is the first element of `objects/manifest.json`'s `objects` array, in array order, with
`tranche == 2`, `type == "commit"`, a non-empty `cited` list, and at least one `cited` location whose
`class` is a frozen record (`native-record` or a legacy/receipt class) given as `path:line`.

## Closure (C)

C(h) = the union of
1. h itself;
2. every manifest entry, stored or withheld, whose `needed_by` names h;
3. every retained commit that h's H4 history connectivity passes through (a `raw:connected` parent chain down
   to the tranche base), with *their* `needed_by` objects, reported separately as the history sub-closure;
4. for completeness, every object h's root tree names recursively, split into (a) retained in C, (b) reachable
   from the tranche base (not stored by the archive), (c) withheld.
Each entry is also tagged with the other cited commits that name it (shared objects).

## Two guarantees, kept apart

- **G-full** — the guarantee the archive states today: exact commit id, its full root tree restorable into a
  clone by `check_objects.py --materialize`, connectivity per H4, so that the head can be checked out and its
  recipe re-run.
- **G-claim** — a claim-specific reconstruction hypothesis: only what the surviving `file:line` claims assert
  (the commit's identity and the files whose content a claim states), e.g. in the archive's own
  `inclusion-proof` form. Adopting G-claim is not authorized; it is evaluated as a hypothesis only.

## Classification rule (K), applied per object, first matching clause wins

1. **redundant** — only if the object's exact bytes were regenerated from `main` `92de3143` by a route that does
   not pass through the archive's own stored copy, and compared byte-for-byte with the archive's stored content
   (decoded), and matched. Route used: the object id is present in a clone holding only `main`'s history, and,
   for objects the archive stores as plain blobs, it occurs in `main` at a path outside
   `verification/audits/evidence-retention/`; the bytes `git cat-file` returns there are compared with the
   archive file's decoded content. A newer green run, a similar file, or an unrun recipe never qualifies.
2. **required** — h itself (a cited commit id is checked only against that object; no other bytes carry the id),
   or an object a surviving claim's text asserts content of, or an object without which G-full fails for h.
3. **optional** — only with a demonstrated absence of any surviving claim *and* any in-force guarantee needing it.
   Not available under G-full for an object in C(h).
4. **undetermined** — anything whose necessity depends on a measurement not made (in particular: whether a claim's
   recipe can be re-run from a G-claim subset, which requires running that recipe on the subset).

The primary classification is K evaluated against G-full, the guarantee in force. A second column evaluates the
same objects against G-claim; there, objects outside the claim's assertion are **undetermined** unless the claim's
recipe was actually re-run from the subset and matched, which this pilot does not do if it exceeds the compute
bound.

## Controls (preregistered)

- **Live control:** an unmodified isolated disposable clone (`git clone --no-hardlinks --no-local`, no
  `--shared`, no alternates, no linked worktree), checked out at `92de3143`, runs
  `python3 -I -B .../check_objects.py`, `--reconstitute`, and `python3 -I -B .../check_retention.py`; all must
  pass. A control that cannot run (e.g. missing history) voids the verdict and is reported, not reinterpreted.
- **Negative control N1 (file omission):** in a second disposable clone, delete the stored file of one object
  classified required (a dependency object of h with no citation of its own). Pass criterion: `check_objects.py`
  exits non-zero and every failure line it prints refers to that object or that file, and the live control passes.
- **Negative control N2 (coordinated omission):** in a third disposable clone, delete that file *and* its manifest
  entry, as a narrowed archive would. Pass criterion: the archive's own checks exit non-zero with a failure
  attributable to the omission. If N2 passes the checks, that is recorded as a finding (the checker would not
  catch a coordinated omission of that object), not as evidence the object is unneeded.
