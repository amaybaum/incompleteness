# DESIGN-v5.5.10a: bounded correction of DESIGN-v5.5.10

## Input and scope

Inputs, sha256 verified before use (unchanged by this work):

- `DESIGN-v5.5.10.md` (draft, base of this correction): fae222cd5caab23cec5a80bfa9d0db083efad8311e3985cd7b553bec87748e0c
- `review-v5.5.10/review.md` (independent review, REJECT on B1 and B2): 78dc33d3a99405cbb7150de77ad1550495643f4f3121f51795bd0312fc897a8c
- `DESIGN-v5.5.9.md` (adopted, authoritative): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9

The owner's decision, verbatim (owner amaybaum, 2026-11-24, as relayed by the coordinating
session; no comment id held by this writer):

> "Approve the bounded correction v5.5.10a.
> 1. B1: Select option (a). Restore the v5.5.9 deletion rule. Use batched GraphQL reads for deletion events, with fail-closed handling. Refuse admission if a deleted comment's author is the owner or cannot be established as a non-owner. Absence of exposed deletion events must not be presented as proof that no deletion occurred.
> 2. B2: Apply the proposed correction. Refuse admission when an owner comment is known to have been edited but its required earlier text is unavailable.
> 3. Apply all five reviewer nits.
> 4. Add the corresponding test rows and validation requirements.
> 5. Preserve F4 as an explicit unresolved feasibility risk. If GraphQL does not expose the full required historical text, stop and escalate rather than weaken the guarantee.
> 6. Preserve the separate authorization requirement for CI validation and all test writes.
> Submit v5.5.10a for independent exact-version review. Keep the amendment strictly bounded to these corrections."
> "The purpose of v5.5.10 is to make verification more efficient, not less strict." "If validation reveals that [#1169 contains a deleted owner comment], address it separately rather than weakening the verification tool preemptively."

"Owner item n" below is item n of this decision. The review lists eight nits (N1-N8). As the
coordinating session directed, N1, N2, N4, N5 and N7 are applied, and N8 is covered by owner item 4
(HV12). N3 (`nodes(ids:)` cap undocumented) and N6 (alternates in the trust-root store) are
observations; neither needs a statement, and neither changes the text.

Paper-only: no repository file, commit, push, GitHub write, GraphQL call or CI run. Built by exact,
once-only replacements (`work-v5510/apply_a.py`, 23 replacements, each asserted to match once).

New identifiers: TR86, TR87, HV11, HV12. A word-bounded grep over every `*.md` of the design
directory finds them only in `DESIGN-v5.5.10a.md`, this file and `review-v5.5.10/review.md`, which
proposes TR86. TR71-TR85 and HV1-HV10 keep their meaning; TR79, TR85 and HV5 are extended within
it. Nothing is renumbered or reused.

## Size

- `CHANGES-v5.5.10a-from-v5.5.10.diff`: 14 hunks, 38 lines removed, 98 added (136 changed lines);
  3322 -> 3382 lines.
- `CHANGES-v5.5.10a-from-v5.5.9.diff` (complete amendment of the adopted design): 20 hunks, 40
  removed, 270 added (310 changed lines); 3152 -> 3382 lines.

## Changes from v5.5.10 (v5.5.10 line numbers)

| # | Hunk | v5.5.10 lines | Location | Change | Source |
|---|---|---|---|---|---|
| 1 | `@@ -1,4 +1,4 @@` | 1 | title | "v5.5.10" -> "v5.5.10a" | version label |
| 2 | `@@ -7,6 +7,21 @@` | before 10 | Status and authority | new bullet: v5.5.10a, its review, what it corrects, N3/N6 unchanged, authorizations still separate | owner items 1-6 (status line) |
| 3 | `@@ -275,6 +290,7 @@` | after 277 | 0.2 table | new row for the review's B1, B2, nits and F4 | traceability |
| 4 | `@@ -1435,8 +1451,13 @@` | 1437 | trust root point 2, "Anchors absent" | the workflow fetches the exact anchor id by full id into the full store before admission; objects verified; the tool fetches nothing | N4 |
| 4 | (same hunk) | 1438-1439 | trust root point 2, "Entries" | `A`, freeze-ledger versions, review records and committed snapshots read only from regular-file entries; any other entry refuses; K7 unchanged | N5 |
| 5 | `@@ -1556,11 +1577,14 @@` | 1559-1563 | freeze ledger, "What the host exposes" | "and the tool does not read it" and "Until the owner adopts a rule ... reads no deletion events" replaced: the host exposes the events, so the v5.5.9 rule applies; the tool reads them and refuses (point 3); absence of events proves nothing; residual stands; completeness is the open investigation | B1; owner item 1 |
| 6 | `@@ -1584,19 +1608,49 @@` | 1587-1599 | admission point 3, "Edit history" | GraphQL limited to edit history and deletion events (both absent from REST); `userContentEdits` not paginated, >100 revisions refuse; new refusal: edited (HS-5 sense) with no revision returned (`totalCount` 0) | B1 (scope statement); N2; B2, owner item 2 |
| 6 | (same hunk) | after 1599 | admission point 3 | new paragraph "Required earlier text (F4)": the full earlier text is required; `diff` described by the schema as a summary; HV4/HV8; failure returns the design to the owner, no rule relaxed, no substitute source | owner item 5 |
| 6 | (same hunk) | after 1599 | admission point 3 | new paragraph "Deletion events": both threads read; `CommentDeletedEvent` timeline items, every page, batched; author numeric id via a `User` fragment; refusal on any read failure, count mismatch, repeated id, absent/null/non-`User` author or absent id, or an author id equal to the `owner.id` of any version of `A`; a non-owner author does not refuse; absence proves nothing | B1; owner item 1 |
| 7 | `@@ -1653,6 +1707,8 @@` | after 1655 | admission snapshot | new field: the deletion events read per thread (id, creation time, author id) and their count | B1 (record of what the admission observed) |
| 8 | `@@ -1680,21 +1736,21 @@` | 1682-1683 | residual trust, host APIs | the GraphQL API attests a thread's deletion events and their authors as well | B1 |
| 8 | (same hunk) | 1686-1688 | residual trust, git object ids | "collision resistance of ... SHA-1" -> "SHA-1's second-preimage resistance against the objects the host holds, and ... the host's and git's refusal of objects that collision-detecting SHA-1 flags" | N1 |
| 8 | (same hunk) | 1695-1697 | residual trust, deletion bullet | "the tool reads no deletion events" -> "or if the host reports deletions (admission point 3, "Deletion events")", the v5.5.9 wording restored with its pointer; the residual applies to a withdrawal "not reported by the host" | B1 |
| 9 | `@@ -2428,7 +2484,7 @@` | 2431 | TR35 | the sentence v5.5.10 appended is removed; the row is again byte-identical to v5.5.9 | B1 |
| 10 | `@@ -2472,13 +2528,15 @@` | 2475 | TR79 | extended: more than 100 revisions; `lastEditedAt` set with `totalCount` 0 on a comment with no form; `updated_at` differing with `totalCount` 0; ERROR in every case | B2, N2; owner item 4 |
| 10 | (same hunk) | 2481 | TR85 | the deletion-event read is permitted beside the edit-history read; both pass the lint | B1 |
| 10 | (same hunk) | after 2481 | new TR86 (deletion of an owner comment, of an earlier owner's, of an unidentifiable author: ERROR; non-owner author: no refusal) and TR87 (deletion-event read failures: ERROR) | B1; owner item 4 |
| 11 | `@@ -2506,8 +2564,8 @@` | 2509-2510 | sec. 10.5 lead | HV12 added to the write items needing separate authorization | owner item 6 |
| 12 | `@@ -2519,12 +2577,14 @@` | 2522 | HV5 | adds the converse: `lastEditedAt` set implies `totalCount` above 0; comments with an edit signal and `totalCount` 0 recorded | B2; owner item 4 |
| 12 | (same hunk) | after 2527 | new HV11 (read: deletion-event query on both threads; events equal `totalCount`; authors resolve to `User` with id; counts recorded; an owner-authored event is reported to the owner for separate handling, no rule change) and HV12 (write: a deleted owner test comment is reported with the owner's id) | B1, N8; owner items 4, 6 and the owner's note on #1169 |
| 13 | `@@ -2987,24 +3047,24 @@` | 2990 | sec. 15 item 6 | label "**Item 7.**" -> "**The plan's item 7.**" | N7 |
| 13 | (same hunk) | 2992-2993 | sec. 15 item 7 | HV12 added to the write items | owner item 6 |
| 13 | (same hunk) | 2997-2998 | sec. 15 item 8 | the `diff` question named an unresolved feasibility risk with its escalation; `deletedCommentAuthor` population (HV11, HV12) added | owner item 5; B1 |
| 13 | (same hunk) | 3001-3007 | sec. 15 item 9 | the investigation concerns completeness only; the tool reads and refuses on the events whatever its outcome | B1 |
| 14 | `@@ -3319,4 +3379,4 @@` | 3322 | S13 | TR1-TR85 -> TR1-TR87; HV1-HV10 -> HV1-HV12 | owner item 4 |

## Row changes

Compared by script (every table row whose first cell is a control id):

- against v5.5.10: changed TR35, TR79, TR85, HV5, S13; added TR86, TR87, HV11, HV12; none removed;
- against v5.5.9: changed TR25 and S13 only (TR35 is byte-identical to v5.5.9 again); added
  TR71-TR87 and HV1-HV12; none removed.

Expectation changes relative to v5.5.10, each stricter or restoring v5.5.9:

- **TR35**: the v5.5.10 appended sentence removed; v5.5.9's expectation restored verbatim, and on
  the host in use its second branch ("On a host that reports deletions: ERROR") applies through
  TR86.
- **TR79**: new cases added, ERROR in each.
- **TR85**: the deletion-event query no longer fails the lint. Relative to v5.5.10 this admits one
  more query; it is the query B1 and owner item 1 require. Relative to v5.5.9, which had no TR85,
  nothing is relaxed. Every other GraphQL query still fails.
- **HV5**: a further condition (the converse) must hold.
- **S13**: two more controls and two more HV items gate the step.

## Preserved guarantees (relative to v5.5.9)

The v5.5.10 change note's argument stands for everything this correction leaves unchanged. The
corrections affect these points:

1. **Deletion rule (v5.5.9 "The residual", TR35).** The v5.5.9 sentences stay verbatim, TR35 is
   byte-identical to v5.5.9, and the tool reads the deletion events the host exposes and refuses on
   any event whose author is, or cannot be shown not to be, an owner (TR86). Since a deleted
   comment's creation time is not exposed, "an owner" is decided against every version of `A`,
   which is at least as strict as "Owner at creation". Reading the events can only add refusals.
   Their absence is not taken as proof of anything, so the residual and the no-coverage statement
   remain. The status bullet's "no control expectation is relaxed" holds again.
2. **Edit history (A-D2, V4, R-D2; HS-3).** An edit signal with no revision returned refuses, which
   closes the review's counterexample: a withdrawal edited out of a comment with an empty history
   is no longer admitted. More than 100 revisions refuse explicitly. F4 is stated as a stop
   condition: if the host does not expose the full earlier text, the design returns to the owner,
   and no rule is relaxed.
3. **Object-id assumption.** Reworded to the property actually needed (N1). No change of substance.
4. **Anchors (N4).** The workflow fetching the exact anchor id is a liveness measure. Every fetched
   object is still hash-verified, and the tool still fetches nothing and refuses when an anchor is
   absent.
5. **Entries (N5).** Stricter: the records v5.5.9 read through the host's contents API, which
   follows a symlink, are read here only from regular-file entries.
6. **Authorizations (owner item 6).** The validation stage and every test write (HV8-HV10, HV12)
   remain separately authorized; no real-host admission is claimed before HV1-HV12 pass.

## Flags: points not implementable without weakening (not resolved)

None found in this correction. Two consequences for the owner, neither a weakening:

- **Liveness on #1169.** Under the restored rule, any reported deletion of a comment by any
  historical owner id in an authorized thread refuses every admission on that thread, permanently.
  HV11 measures whether #1169 or the authority thread has such an event; the owner directed that a
  finding there is handled separately and changes no rule.
- **B2 and `updated_at`.** If `updated_at` changes without an edit (for example on pinning), non-form
  owner comments so marked refuse when GraphQL returns no revision. HV5 records such comments.
  Narrowing the signal would be an owner decision on HV5's evidence; v5.5.10a makes none.
- **B2 scope.** The checkable case (edit signal, `totalCount` 0) refuses. Whether the revisions
  returned hold the text of every earlier version, including the original, cannot be decided from
  the response alone. It is the F4 question, tested by HV4 and HV8 under the stop-and-escalate rule.

## Open items

As in `CHANGES-v5.5.10.md`, with item 7 (the deleted-comment investigation) now about completeness
only, and with these added:

- whether `deletedCommentAuthor` is populated with a `User` and numeric id for real events (HV11,
  HV12);
- the number of deletion events in #1169 and the authority thread, and whether any names an owner
  id (HV11);
- F4: whether GraphQL `diff` is the full revision text (HV4, HV8). This is an unresolved
  feasibility risk; failure stops and escalates to the owner.
