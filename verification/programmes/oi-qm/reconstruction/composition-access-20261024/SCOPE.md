# What of this package is on `main`

`README.md` and `SHA256SUMS` in this directory are byte-identical to #912's
commit `2af1d5d5b5fff4375e9fe9460f892c680ae99f0c` and are not edited. Of the
files `README.md` describes, these are on `main`:

| File | Blob |
| --- | --- |
| `README.md` | `0c0d8b259a42bf6ff8e2660356ef8aeeb7a0373e` |
| `REPORT.md` | `2f77fe2fbb15cdcf3f04656e1e215124137ac1a6` |
| `RESULT.json` | `c4fc742e253e57817469d7cf1fe43fe5f38e1389` |
| `SHA256SUMS` | `2e85c15a2cff649bdd39a3c40eca33bd3037a2a8` |
| `checks.py` | `8203bdcb4d5670862d02ed21c9f8b47b0b4c2e7d` |

`SHA256SUMS` lists the other four, and `sha256sum -c SHA256SUMS` from this
directory checks them. The packages `native-x-v2/`, `tagged-post-y-v3/`,
`native-phase-v4/`, `native-coupling-v5/`, `composition_flag_v6/`,
`delayed_history_v7/` and `native_predicate_v8/`, the directory `review/` and
`CURRENT-HANDOFF.md` are not on `main`; they are on #912's branch at
`2af1d5d5`. Of `README.md`'s replay commands, only the first
(`checks.py | cmp - RESULT.json`) reads only files that are on `main`.

The review status on `main` is that of `REPORT.md`: "Separate-author review
remains pending." No review record of this package is on `main`.

#912's branch at `2af1d5d5` also carries `review/REVIEW.md` (blob
`eceb7060ad337baa2e2161f6e9e0ba58d0c2ac2e`, added in commit
`5b57321a39525ccd486560628a10ecedefb8dc65`), headed "Separate-author review"
and returning "ACCEPT within the stated conditional theorem and finite
toy-control scope" for author commit `a7f22c38503c710f91567628658ed627172cecdf`.
It was committed from the author's account and names no reviewer. It is an
author-posted record, not an independently authenticated review, and it is not
on `main`.

## Records on `main` that use this package

MR-1's frozen preregistration
(`../measurement-record-formation/preregistration.md`, §2.2) lists #912 under
"Off `main` (provenance only; §A.42 item 2)". That classification is too broad.
MR-1 uses #912's content as support:

- Proposition B2 ("proved on paper from #912's proof", :307–319) uses
  `REPORT.md`'s contract (1) (:9–32), the conditional theorem with its
  induction proof and controller condition (:34–55), and the freshness
  condition (:57–69).
- MR-1:48, N6 (:112–114), T5 and §5.6 (:493, :514) and outcome rows 3.2 and
  3.3 (:632–633) use the same contract and the finite controls in `checks.py`
  and `RESULT.json`.

The supporting files are those in the table above, with the same blobs as at
`2af1d5d5`. None of these uses needs the #885 context that `REPORT.md` cites
at :105–110. This note corrects the evidence classification only: B2's
statement and its stated status are unchanged, and the preregistration is not
edited.
