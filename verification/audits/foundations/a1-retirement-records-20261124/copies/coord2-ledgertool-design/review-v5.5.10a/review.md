# Independent review: DESIGN-v5.5.10a (bounded correction of v5.5.10)

Reviewer: independent, non-author. Review only. No repository write, commit, push, GitHub write,
GraphQL call or CI run. Host facts were checked only against GitHub's published documentation
(docs.github.com, fetched 2026-11-24; extracts with source URL and page sha256 under `evidence/`).

Verdict: **REJECT**, on one blocking finding (R1, a residual case of the B2 class). The fix is one
bullet, one TR79 case and one HV5 clause. Everything else in the correction is as decided and
strictly bounded, and no v5.5.9 guarantee is weakened. With R1 fixed as proposed, and nothing else
changed, I would expect ACCEPT-WITH-NITS.

## 0. Inputs verified

| Object | sha256 | Result |
|---|---|---|
| DESIGN-v5.5.10a.md (under review) | b7e45218d27a2ab2a36f6b3f837e07ea04f3df88d04120733e9487c0a3cf1ee2 | matches |
| CHANGES-v5.5.10a.md | fd86c11cd939d838a94a0626ebe1acc14424465378ec71d224bad304315d3ff3 | matches |
| CHANGES-v5.5.10a-from-v5.5.10.diff | 39732b40728244277c67c51e6c73c283fa7c74aa1fc9d575be0ef3472b9ee6dd | matches |
| CHANGES-v5.5.10a-from-v5.5.9.diff | 0cf26beea06c65a8e0919fa8db8b2066810ea17f1cba48316d8332360e477d4e | matches |
| DESIGN-v5.5.10.md (rejected draft) | fae222cd5caab23cec5a80bfa9d0db083efad8311e3985cd7b553bec87748e0c | matches |
| DESIGN-v5.5.9.md (adopted base) | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | matches |
| review-v5.5.10/review.md | 78dc33d3a99405cbb7150de77ad1550495643f4f3121f51795bd0312fc897a8c | matches |

Both diffs regenerated here with `diff -u` are byte-identical to the supplied files (`cmp`, header
lines included). Statistics as the change note states: from v5.5.10, 14 hunks, 38 removed, 98
added (3322 -> 3382 lines); from v5.5.9, 20 hunks, 40 removed, 270 added (3152 -> 3382).

## 1. Blocking finding

### R1. An edited owner comment whose only returned revisions equal its current text is admitted (owner item 2, HS-3)

**Counterexample (paper walk of v5.5.10a sec. 6.3, admission point 3).** An owner comment created
at `t0` as `oi-freeze/1 withdraw plan=<p> round=<r> commit=<F>` and edited at `t1` to `noted.`.
REST: body `noted.`, `updated_at` = `t1` != `created_at`, `minimized: null`. GraphQL:
`lastEditedAt: t1`, `userContentEdits { totalCount: 1, nodes: [{ diff: "noted.", editedAt: t1,
deletedAt: null }] }` (the host omits the pre-edit version; separately, the same with
`totalCount: 2` and two revisions both `noted.`).

- "Edited (HS-5)": edited (two signals).
- Bullet 1 (form carried and edited): no form now; does not apply.
- Bullet 2 (history ever contained a form): the only revision is `noted.`; no.
- Bullet 3 (hidden): no.
- Bullet 4, the refusal list of "Edit history": request, node and fields fine; revisions returned
  (1) equal `totalCount` (1); `diff` non-null, `deletedAt` unset; the new B2 bullet fires only for
  `totalCount` 0. Not triggered.

The comment is admitted, and the TR33 guarantee (a withdrawal edited out refuses) is lost silently,
exactly as in the prior review's B2.

**Why the earlier text is known to be unavailable.** The host reports an edit, and no returned
revision differs from the current body. That is the same evidence on which the accepted B2
correction refuses for `totalCount` 0 (there, too, the conclusion assumes an edit changes the
text). The design's own pass conditions fix the host model: HV4 requires the newest revision to
equal the current REST body, and HV8 requires that after one edit the newest revision holds the
new body and an earlier one the old body. Under that model every edited comment returns at least
two revisions, at least one of which differs from the current body; a response that does not is
missing a version. The design files this case under F4 ("Whether the revisions returned hold the
text of every earlier version is the feasibility question below"; CHANGES "B2 scope": "cannot be
decided from the response alone"). That is not so for this case: F4 asks whether `diff` is full
text; here `diff` is full text and a version is absent, which is decidable per comment from the
response and the REST body, both of which the tool already reads (the snapshot even records their
sha256). Owner item 2 ("Refuse admission when an owner comment is known to have been edited but its
required earlier text is unavailable") and HS-3 ("missing ... incomplete") cover it. It is not a
regression from v5.5.9, which specified nothing here; it is an incomplete implementation of owner
item 2.

**Smallest fix.**
1. Replace the B2 bullet of "Edit history" by: "- the comment is edited in the sense below while its
   earlier text is unavailable: no revision is returned, or no revision returned differs from the
   comment's current REST body. Whether the revisions returned hold the text of every earlier
   version is otherwise the feasibility question below (B2)."
2. TR79, append: "separately, `lastEditedAt` set with `totalCount` 1, its revision equal to the
   current body; separately, `totalCount` 2 with both revisions equal to the current body" (ERROR).
3. HV5, append: "and `lastEditedAt` set implies at least one revision differing from the current
   body; comments where it does not are recorded".

Liveness: a host that records an edit leaving the text unchanged would make such a comment refuse;
HV5's record surfaces it, and any narrowing is an owner decision on that evidence. An optional
stronger form, "fewer than two revisions returned", rests on HV8's model and is not needed for the
fix.

## 2. Nits and open items (not blocking)

- **R2. No control row for N5's new refusal.** N5 adds "a symlink, a submodule or any other entry
  at such a path refuses" for `A`, freeze-ledger versions, review records and committed snapshots;
  no TR row exercises it (TR51 covers only K7's permitted paths). Owner item 4 asks for the
  corresponding test rows. Fix: TR88, "`A` (separately, a freeze-ledger version, a review record,
  a committed snapshot) at a symlink entry; separately, a submodule entry: ERROR
  `CONFIG_UNREVIEWED` in each case". This adds coverage to a stricter rule and weakens nothing.
- **R3. `totalCount` under `itemTypes`.** The schema describes `IssueTimelineItemsConnection.totalCount`
  as "the total count of items in the connection" and `filteredCount` as the count "after applying
  `before` and `after` filters"; neither description says whether `itemTypes` is applied. If
  `totalCount` counts every timeline item, the equality rule refuses every admission on a thread
  with other items. That is fail-closed and HV11 detects it, but the stage would then return to the
  owner. Worth naming in sec. 15 item 8 as a host behaviour to observe.
- **R4. Token visibility.** GitHub's moderation docs: "Deleting a comment creates a timeline event
  that is visible to anyone with read access ... For anyone without write access, the timeline event
  is anonymized." The job token's permissions may therefore decide whether `deletedCommentAuthor`
  is populated. An anonymized author refuses (fail-closed), and HV11 runs with the job's own token,
  so this is covered; a sentence in sec. 15 item 8 would make the dependency visible.
- **R5. Issue identity of the deletion read.** The edit-history read is bound to the REST listing by
  node id; the deletion read names "the issue's timeline items" without saying how the issue is
  addressed. State that the issue is addressed by the node id of the host's REST record of that
  thread (`repository_id`, issue), and that a response for another node refuses. This closes a
  misaddressed read, which would see no events and refuse nothing.
- **R6. Coinciding threads.** If the plan's authorized thread and `A.authority_thread` are the same
  issue, "an event id repeats" could be read across the two reads and refuse every admission. Say
  that the thread is read once and repetition is checked per read.
- **R7. Earlier authority threads.** Only the current `A.authority_thread` is read for deletions.
  If an earlier version of `A` named another authority thread, deletions there are not read. Equal
  to v5.5.9 (whose rule concerned the authorized thread only); an open item, not a weakening.
- **R8. HV2 names only edit-history queries.** Its pass condition counts "the points the admission
  used", which includes the deletion reads, but the measured per-query cost names only the
  edit-history query. Add the deletion-event query.
- **R9. HV12 and self-deletion.** The docs state that deleting a comment creates a timeline event,
  without distinguishing deletion by the author. If the host emits no event when the owner deletes
  their own comment, HV12 fails and the stage returns to the owner. That is the correct strict
  outcome; it is noted so that the owner expects it.
- **R10. "the stage" in "Required earlier text".** In sec. 6.3 the phrase reads as the admission;
  say "the validation stage of sec. 10.5".
- **R11. The v5.5.10a decision record.** The status bullet does not quote the owner's v5.5.10a
  decision and sec. 15 item 1 lists HS-1 to HS-7 but not it. The v5.5.10 bullet quoted its
  decisions; consistency suggests the same here, or an addition to item 1.
- **R12. Cosmetic.** Two added lines exceed the wrap width (the "Deletion events" heading line and
  sec. 15 item 8). The v5.5.10 status bullet still lists TR35 among v5.5.10's changes, which is
  true of that draft and is superseded by the v5.5.10a bullet above it; no change needed.

## 3. Task A: hunk map against v5.5.10

| Hunk | Location | Item | Exact as decided |
|---|---|---|---|
| 1 `-1,4` | title | version label | yes |
| 2 `-7,6 +7,21` | status bullet for v5.5.10a | owner items 1-6 (records scope) | yes; R11 |
| 3 `-275,6 +290,7` | sec. 0.2 traceability row | bookkeeping for items 1-4 | yes |
| 4 `-1435,8 +1451,13` | trust root point 2: "Anchors absent" sentence; "Entries" | N4; N5 | yes; R2 (no row for N5) |
| 5 `-1556,11 +1577,14` | freeze ledger, "What the host exposes" | B1 (owner item 1: read, refuse, absence proves nothing) | yes |
| 6 `-1584,19 +1608,49` | admission point 3: GraphQL scope; N2 sentence; B2 bullet; "Required earlier text (F4)"; "Deletion events" | B1, N2, B2 (item 2), F4 (item 5) | B1, N2, F4 yes; B2 as proposed but incomplete (R1) |
| 7 `-1653,6 +1707,8` | admission snapshot: deletion events read | B1 (the snapshot records what the admission read, as for every other host fact) | yes; a necessary consequence, not an extra rule |
| 8 `-1680,21 +1736,21` | residual trust: GraphQL attests deletion events; SHA-1 wording; deletion bullet | B1; N1; B1 | yes |
| 9 `-2428,7 +2484,7` | TR35 | B1 | yes; byte-identical to v5.5.9 again |
| 10 `-2472,13 +2528,15` | TR79; TR85; TR86, TR87 | B2/N2; B1; B1 (item 4) | yes; R1 adds a TR79 case |
| 11 `-2506,8 +2564,8` | sec. 10.5 lead: HV12 a write | owner item 6 | yes |
| 12 `-2519,12 +2577,14` | HV5 converse; HV11; HV12 | B2; B1/N8 (item 4) | yes; R1 adds an HV5 clause |
| 13 `-2987,24 +3047,24` | sec. 15 items 6 (N7), 7 (HV12), 8 (F4, HV11/HV12), 9 (completeness only) | N7; item 6; item 5 and B1; B1 | yes |
| 14 `-3319,4 +3379,4` | S13: TR1-TR87, HV1-HV12 | owner item 4 | yes |

Every hunk maps to B1, B2, a nit, F4, the authorization item, the version label or the status and
traceability record. Nothing outside these items is changed.

**"All five reviewer nits."** The prior review's actionable nits are N1, N2, N4, N5 and N7: N3
proposes no change ("HV3 covers it"), N6 is marked optional, and N8 is conditional on B1's fix,
which owner item 4 (test rows and validation requirements) covers. Applying N1, N2, N4, N5, N7 and
covering N8 by HV12 is therefore a sound reading. Each is applied as the review proposed; N5's text
matches the proposal exactly, with R2 as the missing control.

## 4. Task B: rows and removed lines against v5.5.9 (adopted)

Script `rowdiff.py` (written for this review, not derived from the prior `rowcmp.py`): every table
line, keyed by first cell and occurrence index, plus a multiset comparison of all table lines.
Outputs in `evidence/rows-vs-v5.5.9.txt` and `evidence/rows-vs-v5.5.10.txt`.

Against v5.5.9: 564 -> 596 table lines; removed none; multiset: 2 lines only in v5.5.9 (TR25,
S13); added sec. 0.2 rows, TR71-TR87, HV1-HV12 and the sec. 10.5 header. (The key `Id#6` shows as
changed only because the new sec. 10.5 header shifts the occurrence index; the multiset confirms
no header row changed.) Against v5.5.10: changed TR35, TR79, TR85, HV5, S13; added TR86, TR87,
HV11, HV12 and one sec. 0.2 row; removed none. Both equal the change note.

| Row | vs v5.5.9 | Judgement |
|---|---|---|
| TR25 | source renamed (REST head id, verified store) | equal (outcome refused) |
| TR35 | byte-identical | equal; its second branch now applies through TR86 |
| S13 | TR1-TR70 -> TR1-TR87; HV1-HV12 gate added | stricter |
| TR71-TR87, HV1-HV12 | new | stricter (refusals or gates only); TR86 positive case is the non-owner author, which v5.5.9 also admits |
| every other TR, X, S, G, K, R, WB, Z, Y, N, LN, RT row | byte-identical | equal |

Removed or rewritten lines of the v5.5.9 diff (40), each judged:

- Title (1): label. Equal.
- Consumer verification (1): host API -> REST plus own hash-verified store. Equal under HS-1; adds
  the SHA-1 assumption, now stated (N1 wording is the correct property).
- Integrity errors, "an unresolvable object" (1): extended to hash mismatch. Stricter.
- Trust root lead, points 1-2 (9): sources changed; anchors from REST; objects hash-verified;
  replace/graft ignored; shallow/partial refused; chain to a root; regular-file entries (N5).
  Equal or stricter.
- Point 3 "read by the host API at that `head_sha`" (1): verified store. Equal.
- Merge record (2): unique REST PR record whose merge commit lands the version. Stricter.
- Admission point 2 (3): REST listing, unique ids added. Stricter.
- Admission point 3 lead (3): sources moved into "Edit history" and "Hidden state". Equal for edit
  history (every v5.5.9 bullet kept verbatim; the refusal list is stricter). Hidden state moves to
  REST `minimized` under HS-2: equal under the residual host trust, gated by HV7/HV10.
- Point 9 (3): also refuses without a full local store. Stricter.
- Snapshot (2): more fields. Stricter.
- Residual trust, host API bullet (4): split REST/GraphQL; deletion events added. Equal.
- Residual trust, deletion bullet (2): "or if the host reports deletions" kept, with a pointer;
  "and not reported by the host" narrows the residual to what is not reported; "any form a deleted
  comment carried" states an existing limit. Equal in behaviour, stricter in effect (events now
  read).
- Native clone (1): `--filter` barred, shallow/partial refused. Stricter.
- Host-run classes (1): REST named. Equal.
- TR25 (1), S13 (1): above.
- Sec. 15 item 1 (3), item 6 label (1): records and label. Equal.

No v5.5.9 guarantee is weakened. In particular the deletion rule is now enforced on the host in use
(v5.5.9's "If it does, any deletion of an owner comment refuses"), which v5.5.10 had dropped.

## 5. Task C: the deletion rule

**Rule as written.** Both threads; `CommentDeletedEvent` timeline items; pages of at most 100 until
no further page; batched; refusal on any read failure, count != `totalCount`, repeated event id,
absent/null/non-`User` author or absent numeric id, or an author id equal to the `owner.id` of any
version of `A` on `main`'s first-parent chain; non-owner author does not refuse; absence proves
nothing.

**Soundness and fail-closed behaviour.**
- Comparison set. An owner comment (sec. 6.3, "Owner at creation") has the `owner.id` of the
  version in force at its creation; every such version is on `main`'s first-parent chain, so
  "any version" is a superset, and point 3's "author is `A.owner.id`" population is included
  (the current `A` is on the chain). A pending id in an unmerged `A` is not an owner and its
  approvals do not count until merged. No owner comment escapes the set.
- Author identity. `deletedCommentAuthor: Actor`; the implementers of `Actor` are `User`, `Bot`,
  `Mannequin`, `Organization` and `EnterpriseUserAccount` (schema extract); only `User` passes, and
  `User.databaseId` is a nullable `Int`, whose absence refuses. A login match with another id is
  not the owner (consistent with point 3).
- Monotonicity. Reading events can only add refusals; nothing admitted by v5.5.9 on a host that
  reports deletions is refused less.
- Absence. Stated three times as establishing nothing; the residual and the no-coverage statement
  stand (owner item 1, HS-6).

**Counterexample search (host exposes the event).** I could not construct one: an exposed event
whose `deletedCommentAuthor` is the owner's `User` refuses by id; one that is not a `User` or lacks
an id refuses; a dropped page or duplicate refuses by count or id; a request error refuses. The
remaining routes need the host to misreport the author (residual host trust, now listed) or the
read to address the wrong issue (R5, a specification gap, not a reachable admission on a correct
implementation).

**Verified against the published schema and docs (`evidence/`):**
- `type CommentDeletedEvent implements Node` with `actor`, `createdAt`, `databaseId`,
  `deletedCommentAuthor: Actor` ("The user who authored the deleted comment."), `id`.
- It is a member of `union IssueTimelineItems` and of `PullRequestTimelineItems`;
  `enum IssueTimelineItemsItemType` has `COMMENT_DELETED_EVENT` ("Represents a 'comment_deleted'
  event on a given issue or pull request").
- `Issue.timelineItems(after, before, first, itemTypes, last, since, skip)`; `itemTypes` is
  documented as "Filter timeline items by type."
- `IssueTimelineItemsConnection` has `totalCount`, `filteredCount`, `pageCount`, `pageInfo`, `nodes`.
- Connections: `first`/`last` must be within 1-100 (limits page, same sha256 as the prior fetch).
- "Deleting a comment creates a timeline event ... For anyone without write access, the timeline
  event is anonymized" (moderation docs).
- REST: the timeline and issue-event-types pages contain no `comment_deleted` and no deletion event
  (0 occurrences), so "REST provides neither" holds at the level of the documentation, and HS-2
  permits the GraphQL read; owner item 1 orders it in any case.

**Inferred, not verified:** that `totalCount` honours `itemTypes` (R3); that `deletedCommentAuthor`
is populated for the job token (R4, HV11); that an event is emitted when an author deletes their own
comment (R9, HV12); that events are emitted for every deletion (completeness, sec. 15 item 9).

## 6. Task D: B2

Every case in which an edit signal holds and **no** revision is returned now refuses (bullet, TR79
cases 3-4, HV5 converse). The case of R1, in which revisions are returned but none differs from the
current body, is still admitted; that is the blocking finding. Other paths checked:
- `lastEditedAt` or `userContentEdits` absent, `deletedAt` set, null `diff`, count short, more than
  100 revisions: all refuse.
- Host omits every edit signal (no `lastEditedAt`, `totalCount` 0, `updated_at` = `created_at`):
  undetectable by any rule; residual, as stated (sec. 15 item 8).
- Host returns a revision list with a different, non-original earlier text: undetectable per
  comment; F4/F5, gated by HV4/HV8/HV9.

## 7. Task E: F4

"Required earlier text (F4)" states that the rules need the full text of every earlier version,
that `diff` is documented as "A summary of the changes for this edit" (verified in the schema),
that HV4 and HV8 test it, and that on failure "the stage fails and the design returns to the owner;
no rule of this section is relaxed and no other source is substituted". Sec. 15 item 8 names it an
unresolved feasibility risk with the same escalation. TR80 keeps "no fallback to REST", TR87 "no
fallback". No fallback source is introduced anywhere in the diff. Stop-and-escalate is explicit
(wording nit R10).

## 8. Task F: authorizations

Sec. 10.5 lead: the stage runs only under its own owner authorization; HV8-HV10 and HV12 need
writes on a dedicated test issue authorized separately; HV11 is a read. Sec. 15 item 7 says the
same. Until every item passes, no real-host admission is claimed: TR5 and TR48 `NOT RUN`, no result
presented for acceptance, S13 gated on HV1-HV12. The status bullet keeps implementation, the
validation stage and every test write separately authorized. Preserved.

## 9. Task G: identifiers and register

- New identifiers TR86, TR87, HV11, HV12: a word-bounded grep over every `*.md`, `*.py`, `*.json`
  and `*.diff` of the design directory finds them only in DESIGN-v5.5.10a.md, its two diffs,
  CHANGES-v5.5.10a.md and review-v5.5.10/review.md (which proposed TR86 with the same meaning);
  `git grep` in the repository at `556cfb08` finds none. TR79, TR85 and HV5 are extended within
  their meaning; nothing is renumbered or reused. R2 would take TR88 (unused).
- Added lines (98): capitalized tokens are `REST`, `ERROR`, `FAIL`, `ACCEPT`, `REJECT`, `CHANGES`
  (acronym, outcome codes, verdict labels, a file name). Revision-history wording appears only in the
  status bullet ("restored"), a status record of the design, not paper prose; §A.32/§A.33 govern
  `papers/` and are not engaged. No reader-instruction or self-assessment phrases.

## 10. Trust root after N4 and N5

- **N4.** The workflow fetches the anchor id by full id into the full store before admission. The
  tool still reads no ref and fetches nothing; every fetched object is hash-verified and parsed from
  content; a shallow store stays marked and refuses; if `main` moves between the workflow's fetch
  and the tool's REST read, the anchor is absent and the admission refuses (TR77). The fetch adds
  liveness and no trust.
- **N5.** Regular-file entries only (100644, 100755) for `A`, ledger versions, review records and
  snapshots; any other mode refuses. Stricter than v5.5.9's contents API, which follows a symlink.
- The rest of the prior argument (anchors, replace/graft/commit-graph ignored, chain to a root,
  partial stores, SHA-1 second preimage plus collision detection) is unchanged by v5.5.10a and
  re-checked here against the text: it holds.

## 11. Files

- `review.md` (this file);
- `rowdiff.py` (row comparison), `evidence/rows-vs-v5.5.9.txt`, `evidence/rows-vs-v5.5.10.txt`;
- `evidence/graphql-schema-extract.txt`, `evidence/docs-extract.txt` (source URLs and page sha256);
- `work/added.txt` (the 98 added lines scanned in sec. 9).

The regenerated diffs were byte-identical to the supplied ones and are not kept. `MANIFEST.sha256`
covers every file listed above.
