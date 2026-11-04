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
`delayed_history_v7/` and `native_predicate_v8/` and `CURRENT-HANDOFF.md` are
not on `main`; they are on #912's branch at `2af1d5d5`. Of `README.md`'s replay
commands, only the first two (`checks.py | cmp - RESULT.json` and
`review/independent_checks.py | cmp - independent-result.json`) read only
files that are on `main`.

`REPORT.md` states its own review status: "Separate-author review remains
pending."

`review/` holds the review record of this package, copied byte-identically
from #912's branch at `2af1d5d5`:

| File | Blob |
| --- | --- |
| `review/REVIEW.md` | `eceb7060ad337baa2e2161f6e9e0ba58d0c2ac2e` |
| `review/SHA256SUMS` | `c9a27deaba09519aa5a4e50dac3a79cf9574d7ae` |
| `review/independent-result.json` | `01cd98056d3d5b0f60fa6d16595d3ee01a3ef1a0` |
| `review/independent_checks.py` | `fb0aac3f4f2a1ea83bdd18d02abe9e84e9729c09` |

`review/REVIEW.md`, added in commit `5b57321a39525ccd486560628a10ecedefb8dc65`,
is headed "Separate-author review" and returns "ACCEPT within the stated
conditional theorem and finite toy-control scope" for author commit
`a7f22c38503c710f91567628658ed627172cecdf`, whose `REPORT.md`, `checks.py` and
`RESULT.json` have the same blobs as the copies here. It was committed from the
author's account and names no reviewer. It is an author-posted record, not an
independently authenticated review, and it does not make `REPORT.md`'s theorem
independently reviewed. `review/independent_checks.py` uses the Python standard
library only and reads no file; its stated replay command is `README.md`'s
second.

## Records on `main` that use this package

MR-1's frozen preregistration
(`../measurement-record-formation/preregistration.md`, §2.2) lists #912 under
"Off `main` (provenance only; §A.42 item 2)". That classification is too broad.
MR-1 uses #912's content as support:

- Proposition B2 ("proved on paper from #912's proof", :307–319) uses
  `REPORT.md`'s contract (1) (:9–32), the conditional theorem with its
  induction proof (:34–55), and the freshness condition (:57–69). #912's
  proof covers randomized controllers under its own condition (:48–53);
  whether B2's weaker condition (MR-1:311) suffices is open (#1088 comment
  6636314963).
- MR-1:48, N6 (:112–114), T5 and §5.6 (:493, :514) and outcome rows 3.2 and
  3.3 (:632–633) use the same contract and the finite controls in `checks.py`
  and `RESULT.json`.
- `Res` (MR-1:152) uses the freshness condition, and AW-MR3 (MR-1:399) uses
  the access countercontrol in `checks.py` and `RESULT.json`.

The supporting files are those in the table above, with the same blobs as at
`2af1d5d5`. None of these uses needs the #885 context that `REPORT.md` cites
at :105–110. This note corrects the evidence classification only: B2's
statement and its stated status are unchanged, and the preregistration is not
edited.
