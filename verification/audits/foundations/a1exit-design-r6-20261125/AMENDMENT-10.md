# r6 amendment 10: the `revision` of a review read by the post-freeze route (draft r1)

**Owner decision.** amaybaum, in the coordinating session, 2026-11-27, recorded at #1577 comment 7222646181.
The owner's instruction, verbatim: "Approved". It approves the proposal put to the owner in the same session,
quoted:

> I'd record it as a narrowly scoped Amendment 10 to S-2 S2.3, adopted the same way as Amendment 9, with a focused independent review. If you reply **"Approved as suggested"**, I'll draft option A on that basis.

Option A, as proposed: "Post-freeze route only: `revision` must equal REV's single parent (the record base M, or
M0 on a predicted M). The reviewed bytes are checked in REV's tree."

**Status.** Draft r1, recording the approved option. It changes nothing else in r6, its amendments 1 to 9, or
the staging supplements S-1 and S-2. Adoption authorizes no merge, dispatch, freeze or trial.

**Goal link (AGENTS.md sec. A.47).** A1 retirement (#1477). It decides which commit a review read by the
post-freeze route binds as its `revision`, so that the RT-L2 release check and any post-freeze record can be
reviewed at all.

## 1. The contradiction

S-2 S2.3 keeps S-1 sec. 3's acceptance and roots for `revision` unchanged. S-1 sec. 3 requires `revision` to be
"a commit id that is reachable, through any parent, from the root the review is read from, and whose tree holds
`reviewed.path` at a regular mode with bytes hashing to `reviewed.blob_sha256`", with root "`REV` for a review
read by the post-freeze route". The adopted route makes that unsatisfiable:

- R6.RECON.2 (a) and R6.RECON.21 require the reconciliation record to name the run's `M`, and R6.RECON.21 binds
  its blob ids to `M`. A commit id fixes its tree and all its ancestors, so no commit in `M`'s history (or in
  `M0`'s, on a predicted `M`) can hold bytes that name `M`. The record therefore first appears in `REV`.
- R6.RECON.2 (c) gives `REV` exactly one parent, the record base, and a tree equal to it except for files added
  inside reconciliation directories; (d) puts the review in `REV`'s tree. `REV` cannot be the review's own
  `revision`, since the review's bytes would then have to contain `REV`'s id.

So no review read by the post-freeze route, including the review the RT-L2 release check reads (R6.RECON.21),
can satisfy S-2 S2.5's record lint. No adopted text resolves this: S1-REVISION-POST-F covers custody and
finding reviews read from effective `M` only.

## 2. The change

S-2 S2.3, `revision` item: the post-freeze root is replaced. The item reads:

> - `revision`: the commit the reviewer read, with S-1 §3's acceptance and roots unchanged (`F` in chain
>   record lint; effective `M`, or `F` and `REV` where the walk reaches them, for detection and finding lookups;
>   effective `M` for a custody review), except on the post-freeze route (R6.RECON.2, R6.RECON.21): there
>   `revision` must equal the record base, the single parent of `REV` (the run's `M`, or `M0` named by
>   `--record-base` on a predicted `M`), and `reviewed.path` must be read from `REV`'s tree at a regular mode
>   with bytes hashing to `reviewed.blob_sha256`.

The same replacement applies to S-1 sec. 3's list of roots, and the r13 table row `review.record` `revision`
(S-2 sec. 5, "Row `revision` kept (S-1 §3)") carries this acceptance for the post-freeze route.

What it keeps and tightens:

- The threat S-1 sec. 3 addresses is a review written after `F` bound to a context it cannot name. Here the
  `revision` is exactly one commit that exists before `REV` and that the review can name. That is narrower than
  "any commit reachable from the root".
- The exact bytes stay bound: `reviewed.blob_sha256` must match the bytes in `REV`'s tree, and R6.RECON.2 (c)
  limits `REV` to the record base plus files added inside reconciliation directories.
- The roots and acceptance for chain record lint (`F`), detection and finding lookups, and custody reviews are
  unchanged. A detection review found in `REV` that reviews a record first added in `REV` is not on the
  post-freeze route; it still fails `revision` and is a form failure that still blocks (S-2 S2.5), as now.

## 3. Controls

Added to S-2 sec. 7. Each runs through the real record lint on the post-freeze route:

| Control | Case | Expected |
|---|---|---|
| A10-REV-BASE | `revision` equals the record base `M`; the reviewed bytes are in `REV`'s tree | the record is admitted |
| A10-REV-ANCESTOR | `revision` is `F`, or another ancestor of the record base | counts as no review; the record is FAIL `record-invalid` |
| A10-REV-SELF | `revision` names a commit other than the record base that holds the reviewed bytes (for example a sibling of `REV` with the same tree) | counts as no review |
| A10-REV-PREDICTED | predicted `M` with `--record-base M0`: `revision` is `M0`; then the predicted `M`'s id | `M0` is admitted; the predicted `M`'s id counts as no review |
| A10-REV-BYTES | `revision` equals the record base, but the bytes at `reviewed.path` in `REV`'s tree do not hash to `reviewed.blob_sha256` | counts as no review |
| A10-REV-MUTANT | a mutant that replaces equality with reachability from `REV` | A10-REV-ANCESTOR fails under the mutant |

S1-POS and S1-REVISION-MISMATCH (chain record lint at `F`) and S1-REVISION-POST-F (custody and finding reviews
from effective `M`) keep their cases and outcomes. The RT-L2 release check's `revision` check (S-2 S2.5 lint,
inlined in the gate) applies this acceptance to the review it reads.

## 4. Generator

No expectation row changes: the new controls are recorded under their own case ids by the tool revision. If an
expectation row is later needed for them, it is added by a generator-amendment10, as for earlier amendments.
