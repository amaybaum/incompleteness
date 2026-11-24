# DESIGN-v5.5.8: changes against DESIGN-v5.5.3

## Input and scope

Inputs, sha256 verified before use and after writing (all unchanged):

- `DESIGN-v5.5.3.md` (frozen): 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379
- `DESIGN-v5.5.7.md` (draft): 0a7efa040af44c4bf1e09b3ba026eb6e2a1a0fecc413516a0c2fcbc629504f6f
- `CHANGES-v5.5.7.md`: 41df071e1df2922cfbb950c72f380b9e861f8de5c54864480cd1a5e8d08b6dfa
- `review-v5.5.7/review.md`: 761585bbbb6be90fd374152d4a6b08455a765170bc87cd9fe7ca875291792c2b

v5.5.8 is a draft amendment of v5.5.3 implementing the owner decisions DI-1 (option B) and DI-2
(option A, narrow). It is authoritative only after an independent review returns ACCEPT and the
owner adopts it. It supersedes the v5.5.7 draft. It is v5.5.7 plus exactly the review's
corrections for findings B-3 (new row TR70) and B-4 (new row LN12) of `review-v5.5.7/review.md`
sec. 3, the row clarifications of its non-blocking findings N-1 (TR69), N-2 (TR60) and N-3 (TR68),
the consequential control ranges, and the status line and version label. No design rule text
changes: relative to v5.5.7 only these rows, the control ranges, the version label and the status
line differ (checked by script, `work-v558/scope.py`). The review's other non-blocking findings
(review-v5.5.6 N8-N12 and review-v5.5.5 N2-N6, which it says still apply) are not acted on.

New control ids in this revision: TR70 and LN12. Checked by word-bounded grep
(`grep -lwE 'TR70|LN12'`) over every `DESIGN*.md` and `CHANGES*.md` in the design directory: they
occur in no file other than v5.5.8 and this file (and in `review-v5.5.7/review.md`, which proposes
them). TR54-TR69 and LN1-LN11 keep the meaning they have in v5.5.7; TR60, TR68 and TR69 are
clarified within that meaning as N-1 to N-3 state. No id is reused.

The work was paper-only: no repository file, git or GitHub activity.

## Changes from v5.5.7 (`CHANGES-v5.5.8-from-v5.5.7.diff`, 6 hunks)

| # | v5.5.7 -> v5.5.8 hunk | Implements |
|---|---|---|
| a | `@@ -1,4 +1,4 @@` title "v5.5.7" -> "v5.5.8" | version label |
| b | `@@ -7,15 +7,15 @@` status bullet: v5.5.8, "It supersedes the v5.5.7 draft", controls "TR54-TR62, TR64-TR70" and "LN1-LN12", `CHANGES-v5.5.8.md` | status line; B-3, B-4 consequential |
| c | `@@ -2335,7 +2335,7 @@` TR60: "5555 designates an `F` frozen after the change" -> "5555 designates an `F` whose configuration authorization 5555 made after the change" | N-2 |
| d | `@@ -2343,8 +2343,9 @@` TR68: "Each case separately:" -> "Each case separately, with every other approval and review in it valid, so that each case isolates one defect:"; TR69: setup gains "; 5555 then designates `F'`", outcome gains "; admission of `F'`: ERROR"; new row TR70 directly after TR69 | N-3; N-1; B-3 |
| e | `@@ -2579,6 +2580,7 @@` new row LN12 directly after LN11 | B-4 |
| f | `@@ -3142,4 +3144,4 @@` S13: "LN1-LN11" -> "LN1-LN12", "TR1-TR69" -> "TR1-TR70" | B-3, B-4 consequential |

### Where the review's text was not placed verbatim

- **B-3, TR70 and B-4, LN12:** each table row is a string-equal copy of the review's row (the
  single line inside its ```` ```text ```` fence), placed directly after TR69 and LN11 respectively
  (checked by script, `work-v558/apply.py` and `work-v558/verify.py`).
- **Consequential ranges:** placed as the review states them ("TR54-TR62, TR64-TR70" and
  "LN1-LN12" in the status bullet; "LN1-LN12" and "TR1-TR70" in S13).
- **N-1 (TR69), non-verbatim in placement:** the review's suggested text "then 5555 designates
  `F'`; admission of `F'`: ERROR" is split across the row's two columns: the setup column gains
  "; 5555 then designates `F'`" and the outcome column gains "; admission of `F'`: ERROR". The
  existing setup and refusal reason are unchanged.
- **N-2 (TR60):** "frozen after the change" is replaced by the review's words "whose configuration
  authorization 5555 made after the change", verbatim.
- **N-3 (TR68), non-verbatim:** the review gives no text; the row gains, after "Each case
  separately", the words ", with every other approval and review in it valid, so that each case
  isolates one defect". Cases and outcome are unchanged.
- **Status line:** only the version label, "It supersedes the v5.5.7 draft.", the two control
  ranges and the name of this file change in the existing bullet.

## Complete amendment relative to v5.5.3 (`CHANGES-v5.5.8.diff`, 14 hunks)

`diff -u DESIGN-v5.5.3.md DESIGN-v5.5.8.md`; 3027 -> 3147 lines. For each hunk, the old and new
text below are the whole contiguous span of lines from the first to the last changed line of the
hunk, including unchanged lines between changes, copied from the two files (checked by script:
each block occurs verbatim, as whole contiguous lines, in its file). For an insertion the location
names the anchor.

| # | Hunk header | Location | Decision / correction |
|---|---|---|---|
| 1 | `@@ -1,4 +1,4 @@` | title | both (version label) |
| 2 | `@@ -7,6 +7,16 @@` | Status and authority, new bullet after the first bullet | both (status line); control ranges per review-v5.5.4 C4, review-v5.5.5 C7, review-v5.5.6 C9 and review-v5.5.7 B-3, B-4 |
| 3 | `@@ -1230,6 +1240,27 @@` | 6.3, "What the tool checks", after the `supersedes` bullet | DI-2; predecessor clause per review-v5.5.4 C2 (B2) and review-v5.5.5 C6(a) (F2) |
| 4 | `@@ -1265,7 +1296,9 @@` | 6.3, authority record `A`, field `supersedes` | DI-2 |
| 5 | `@@ -1285,6 +1318,50 @@` | 6.3, after "The forms", new paragraph "Owner at creation" | DI-1; "Owner authorizations" bullet per review-v5.5.4 C1 (B1, B2) and review-v5.5.5 C6(b) (F2) |
| 6 | `@@ -1335,8 +1412,10 @@` | 6.3, "Authority changes", approval and owner-id-change bullets | DI-1 |
| 7 | `@@ -1375,7 +1454,8 @@` | 6.3, "The freeze ledger", N3 bullet, author requirement | DI-1 |
| 8 | `@@ -1408,7 +1488,9 @@` | 6.3, Admission point 3 | DI-1 |
| 9 | `@@ -1420,23 +1502,30 @@` | 6.3, Admission points 4 to 7 | DI-1; cross-reference per review-v5.5.4 N3; point 5 refusal per review-v5.5.5 C5 (F1); point 7 per review-v5.5.4 C3 (B1) |
| 10 | `@@ -1451,8 +1540,9 @@` | 6.3, "The admission snapshot" | DI-1 (consequence) |
| 11 | `@@ -1477,7 +1567,8 @@` | 6.3, "Residual trust assumptions", first bullet | DI-1 (consequence) |
| 12 | `@@ -2238,6 +2329,23 @@` | 10.4, after TR53 | DI-1; TR63 DI-2; TR65 review-v5.5.4 C4 (B1); TR66, TR67 review-v5.5.5 C7 (F3); TR54, TR60, TR61 outcomes review-v5.5.6 C8 (B-1, N7); TR68, TR69 review-v5.5.6 C9 (B-2); TR69 second designation review-v5.5.7 N-1; TR60 wording review-v5.5.7 N-2; TR68 wording review-v5.5.7 N-3; TR70 review-v5.5.7 B-3 |
| 13 | `@@ -2461,6 +2569,18 @@` | 13.2, after S4a | DI-2; LN9 review-v5.5.4 C4 (B2, DI-1); LN10 review-v5.5.4 C4; LN11 review-v5.5.5 C6(c) (F2); LN12 review-v5.5.7 B-4 |
| 14 | `@@ -3024,4 +3144,4 @@` | 16.8, S13 acceptance list | DI-1, DI-2 (consequence); review-v5.5.4 C4, review-v5.5.5 C7, review-v5.5.6 C9, review-v5.5.7 B-3, B-4 |

### Hunk 1: title

Header `@@ -1,4 +1,4 @@`. Decision / correction: both (version label).

Summary: Title: "design v5.5.3" becomes "design v5.5.8".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
# Commit-independent ledger and terminology verification tool: design v5.5.3
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
# Commit-independent ledger and terminology verification tool: design v5.5.8
````

### Hunk 2: Status and authority, new bullet after the first bullet

Header `@@ -7,6 +7,16 @@`. Decision / correction: both (status line); control ranges per review-v5.5.4 C4, review-v5.5.5 C7, review-v5.5.6 C9 and review-v5.5.7 B-3, B-4.

Summary: Status line: v5.5.8 is a draft amendment of v5.5.3 implementing DI-1 and DI-2, authoritative only after independent ACCEPT and owner adoption, superseding the v5.5.7 draft; names its controls (TR54-TR62, TR64-TR70; LN1-LN12, TR63).

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
- **v5.5.8 is a draft amendment of the frozen v5.5.3.** It is authoritative only after an
  independent review returns ACCEPT and the owner adopts it; until then the frozen design is v5.5.3
  (sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379). It supersedes the
  v5.5.7 draft. It implements only
  two owner decisions of 2026-11-23 on the design issues of the fourth Stage 1 review
  (`review-stage1-r4/review.md`, sec. 7): DI-1, option B, the owner identity of a comment (sec. 6.3,
  "Owner at creation"; controls TR54-TR62, TR64-TR70); and DI-2, option A in its narrow form, the
  lineage of a superseding record (sec. 6.3, record lint and the field `supersedes` of `A`;
  controls LN1-LN12 and TR63). Nothing else changes. `CHANGES-v5.5.8.md` lists every changed
  passage.
````

### Hunk 3: 6.3, "What the tool checks", after the `supersedes` bullet

Header `@@ -1230,6 +1240,27 @@`. Decision / correction: DI-2; predecessor clause per review-v5.5.4 C2 (B2) and review-v5.5.5 C6(a) (F2).

Summary: New lint bullet defining lineage as `record_id` (`config_id` for the configuration), its immutability, the record-invalid cases (no valid `record_id`, unrelated chain, predecessor failing the lint, cycle, fork, two heads in one run), and what counts as id reuse; each authorization the predecessor's lint requires, a widening review's included, is checked as "Owner at creation" states for a predecessor, not against the configuration's owner.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
- **lineage (DI-2)**, for every record kind that carries `supersedes`. A record's lineage is its
  `record_id`, a non-empty string at the record's top level; for the configuration it is its
  `config_id` (sec. 16.2). `record_id` is immutable within a lineage: a superseding record has the
  same kind, schema and `record_id` as the record it names. Sharing a `record_id` within one lineage
  is not reuse of an id; a `record_id` carried by two records that do not lie on one `supersedes`
  chain is. Each of the following is FAIL `record-invalid`:
  - a record without a valid `record_id` (missing, empty or not a string) that supersedes another
    record or is named by a `supersedes`;
  - a `supersedes` naming a record whose kind, schema or `record_id` differs (an unrelated chain),
    at any step of the chain;
  - a `supersedes` naming a predecessor that does not itself pass this lint, read from the object
    store at or before `F` and verified independently of the superseding record (its own review
    and authorization, each authorization its lint requires, a widening review's included,
    checked as "Owner at creation" states for a predecessor,
    in place of the comparison with the configuration's owner);
  - a cycle in a `supersedes` chain;
  - ambiguous ancestry: two records superseding the same predecessor, among the records in the
    audit directory and the plan's record directory at `F` and the records the run reads; or a
    lineage with two heads used in one run, a head being a record of the lineage that no other
    record the run reads (the records the configuration references and every record their chains
    name) supersedes;
````

### Hunk 4: 6.3, authority record `A`, field `supersedes`

Header `@@ -1265,7 +1296,9 @@`. Decision / correction: DI-2.

Summary: `A`'s lineage is its fixed path; its `supersedes` must name the preceding version of `A` on `main`'s first-parent chain, otherwise admission refuses.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first.
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first. `A` carries no
  `record_id`: its lineage is its fixed path. `supersedes` must name the version of `A` that
  precedes it on `main`'s first-parent chain, at the same path; otherwise admission refuses (DI-2).
````

### Hunk 5: 6.3, after "The forms", new paragraph "Owner at creation"

Header `@@ -1285,6 +1318,50 @@`. Decision / correction: DI-1; "Owner authorizations" bullet per review-v5.5.4 C1 (B1, B2) and review-v5.5.5 C6(b) (F2).

Summary: Defines version in force, owner comment, owner change; withdrawals; designations; approvals; owner authorizations (owner at its `time`, owner under the governing `A`, no owner change between its `time` and the admission; each authorization of a predecessor, a widening review's included, needs only owner at its `time`); first `A` and owner-id change; completed actions.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
**Owner at creation (DI-1, owner decision of 2026-11-23).** A comment never acquires authority
merely because its author becomes the owner later, or becomes the owner again.

- **Definitions.** The version of `A` *in force* at a time `t` is the latest version of `A` whose
  landing merge on `main`'s first-parent chain has a host merge time strictly before `t`. An *owner
  comment* is a comment whose author numeric id equals the `owner.id` of the version in force at the
  comment's creation time; a comment created when no version was in force is not one. An *owner
  change* is the merge on `main` of a version of `A` whose `owner.id` differs from that of the
  version it replaces.
- **Withdrawals and revocations.** A withdrawal, and the revoking half of a supersession (the
  withdrawal of `F`), counts if it is an owner comment. It stays effective after any later owner
  change.
- **Designations.** A designation, and the designating half of a supersession (the designation of
  `F2`), counts only if it is an owner comment, its author numeric id equals the `owner.id` of the
  authority record governing the admission, and no owner change merged between its creation and the
  admission. After an owner change, the round is designated again by the owner in force. A
  supersession recorded in the freeze ledger or in a committed snapshot only revokes; it never
  designates (sec. 6.3, "The freeze ledger").
- **Approvals.** An `oi-authority/1 approve` comment and an `oi-freeze-ledger/1 append` comment
  count only if each is an owner comment, its author numeric id equals the `owner.id` of the
  authority record governing the evaluation, and no owner change merged between its creation and
  the merge it authorizes. An owner change away and back does not restore an earlier approval. The
  authority record governing the evaluation is, for an authority change, the version it replaces;
  for a freeze-ledger change, the version in force at its merge, or `main`'s current `A` for an
  append not yet merged.
- **Owner authorizations.** An `oi-owner-authorization/1` record counts for a record the run uses
  only if the version of `A` in force at its `time` has `owner.id` equal to its `owner`, its `owner`
  equals the `owner.id` of the authority record governing the admission, and no owner change merged
  between its `time` and the admission. Each authorization of a predecessor named by a
  `supersedes`, a widening review's included, is a completed action: it counts if the version of
  `A` in force at its `time` has `owner.id` equal to its `owner`.
- **The first `A` and an owner-id change.** The approval of the first `A`, and the new id's approval
  of an owner-id change, are by the id the new `A` pins, which is not yet the owner. Each is
  authenticated as that id (sec. 6.3, "Authority changes"), not as an owner comment. It must still
  be created before the merge it authorizes, with no owner change merged between its creation and
  that merge. The previous id's approval of an owner-id change is an approval under the rule above.
- **Completed actions.** An authority change or a freeze-ledger change merged on `main`'s
  first-parent chain is completed. It stays valid if its approvals counted under these rules at its
  merge, and a later owner change never invalidates it. An acceptance landing merged on `main` is
  completed; the admission its snapshot records stands, and the events it appended bind under
  reconciliation. A designation is not completed for a later admission: each admission evaluates it
  under the rule above against the authority record governing that admission. A withdrawal, and the
  revoking half of a supersession, bind from their creation.

````

### Hunk 6: 6.3, "Authority changes", approval and owner-id-change bullets

Header `@@ -1335,8 +1412,10 @@`. Decision / correction: DI-1.

Summary: The approval must also count under "Owner at creation"; the new id's approval in an owner-id change is authenticated as that paragraph states.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  lands the new `A`. The merge alone authorizes nothing.
- **An owner-id change** also needs the same approval from the new id, in a separate comment.
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
  lands the new `A`. The merge alone authorizes nothing. It must also count as an approval under
  "Owner at creation" above.
- **An owner-id change** also needs the same approval from the new id, in a separate comment. That
  approval is authenticated as "Owner at creation" states for the new id.
````

### Hunk 7: 6.3, "The freeze ledger", N3 bullet, author requirement

Header `@@ -1375,7 +1454,8 @@`. Decision / correction: DI-1.

Summary: "authored by numeric owner id `A.owner.id`" becomes "an owner comment that counts as an approval under Owner at creation".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  - be authored by numeric owner id `A.owner.id` (7273571);
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
  - be an owner comment that counts as an approval under "Owner at creation" above (for A1, numeric
    owner id 7273571);
````

### Hunk 8: 6.3, Admission point 3

Header `@@ -1408,7 +1488,9 @@`. Decision / correction: DI-1.

Summary: Point 3 reads edit status for comments by `A.owner.id` and for every owner comment at creation, and records the version of `A` in force at each comment's creation.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
   `A.owner.id`, relevant or not, the tool reads its edit status (REST `updated_at`; GraphQL
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
   `A.owner.id`, and every owner comment as "Owner at creation" defines it (in this point and point
   4, each of them is meant by "an owner comment"), relevant or not, the tool reads the version of
   `A` in force at its creation and its edit status (REST `updated_at`; GraphQL
````

### Hunk 9: 6.3, Admission points 4 to 7

Header `@@ -1420,23 +1502,30 @@`. Decision / correction: DI-1; cross-reference per review-v5.5.4 N3; point 5 refusal per review-v5.5.5 C5 (F1); point 7 per review-v5.5.4 C3 (B1).

Summary: Point 4 parses the owner comments of point 3; point 5 does not process a form or half of a supersession that does not count under "Owner at creation"; point 5's supersession item cross-refers to the rule that a recorded supersession only revokes; point 5's refusal "naming a commit never designated" treats a designation that was an owner comment at its creation as having designated its commit, even if not processed; point 7: every authorization record the run uses must also count under "Owner at creation" (FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED` for the configuration's own). In v5.5.5 points 4-5 and point 7 were two hunks; the C5 lines join them into one.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
4. **Forms.** The owner comments whose first line begins with `oi-freeze/` are parsed by the forms
   above. A malformed or unknown-version line refuses.
5. **Deterministic state.** The forms for this plan and round, together with the bound events of the
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id:
   - a designation of `F` makes `F` designated;
   - a withdrawal of `F` makes it withdrawn;
   - a supersession of `F` by `F2` withdraws `F` and designates `F2`.

   The run's `F` is admitted only if, at the end, it is the one designated commit of the round. Any
   of the following refuses: two live designations; a withdrawal or supersession naming a commit
   never designated; a designation of a withdrawn commit; any other conflict.
6. **The pin table.** `F`'s PREREG pin table is read from `F`'s tree, at `pin_table_path`. Its
   content is authenticated by the owner's designation of exactly `F`. The retirement configuration
   and its review record and owner authorization are admitted only if listed there with their
   sha256. Files beside the configuration are never admitted.
7. **The owner field.** `retirement.owner` must equal `A.owner.id`, and so must the owner of the
   configuration's authorization record.
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
4. **Forms.** The owner comments of point 3 whose first line begins with `oi-freeze/` are parsed
   by the forms
   above. A malformed or unknown-version line refuses.
5. **Deterministic state.** The forms for this plan and round, together with the bound events of the
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id.
   A form, or half of a supersession, that does not count under "Owner at creation" is not processed:
   - a designation of `F` makes `F` designated;
   - a withdrawal of `F` makes it withdrawn;
   - a supersession of `F` by `F2` withdraws `F` and designates `F2` (a supersession recorded in the
     freeze ledger or in a committed snapshot only revokes: "Owner at creation", "Designations").

   The run's `F` is admitted only if, at the end, it is the one designated commit of the round. Any
   of the following refuses: two live designations; a withdrawal or supersession naming a commit
   never designated (for this test, a designation that was an owner comment at its creation has
   designated its commit, even if it is not processed); a designation of a withdrawn commit; any
   other conflict.
6. **The pin table.** `F`'s PREREG pin table is read from `F`'s tree, at `pin_table_path`. Its
   content is authenticated by the owner's designation of exactly `F`. The retirement configuration
   and its review record and owner authorization are admitted only if listed there with their
   sha256. Files beside the configuration are never admitted.
7. **The owner field.** `retirement.owner` must equal `A.owner.id`, and so must the owner of the
   configuration's authorization record. Every authorization record the run uses must also count
   under "Owner at creation" above; otherwise FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED`
   for the configuration's own.
````

### Hunk 10: 6.3, "The admission snapshot"

Header `@@ -1451,8 +1540,9 @@`. Decision / correction: DI-1 (consequence).

Summary: The snapshot records every comment of point 3, with the blob of the version of `A` in force at its creation.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
- for every owner comment: id, author numeric id, creation time, edit status, hidden state, full
  first line and body sha256;
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
- for every comment of admission point 3: id, author numeric id, creation time, the blob sha256 of
  the version of `A` in force at its creation, edit status, hidden state, full first line and body
  sha256;
````

### Hunk 11: 6.3, "Residual trust assumptions", first bullet

Header `@@ -1477,7 +1567,8 @@`. Decision / correction: DI-1 (consequence).

Summary: Adds a pull request's merge time to the trusted host attestations.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  merged-by id; and a comment's immutable id, numeric author id, creation time, edit history,
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
  merged-by id and merge time; and a comment's immutable id, numeric author id, creation time,
  edit history,
````

### Hunk 12: 10.4, after TR53

Header `@@ -2238,6 +2329,23 @@`. Decision / correction: DI-1; TR63 DI-2; TR65 review-v5.5.4 C4 (B1); TR66, TR67 review-v5.5.5 C7 (F3); TR54, TR60, TR61 outcomes review-v5.5.6 C8 (B-1, N7); TR68, TR69 review-v5.5.6 C9 (B-2); TR69 second designation review-v5.5.7 N-1; TR60 wording review-v5.5.7 N-2; TR68 wording review-v5.5.7 N-3; TR70 review-v5.5.7 B-3.

Summary: New controls TR54-TR70: D1 (TR54), D2 (TR55), D3 (TR56), L5 (TR57), L6 (TR58), A->B->A designation (TR59), completed actions (TR60), former-owner supersession (TR61), owner-id change (TR62), `A.supersedes` (TR63), non-owner `A` change (TR64), authorization records analogue of D3/L5 with one positive (TR65), a non-owner's withdrawal not processed and a former owner's withdrawal effective (TR66), point 3 for a former owner's edited comment and its unedited positive (TR67), pre-signed or away-and-back approvals of `A` changes (TR68), a future owner's designation not counting as having designated for the C5 test, discriminated by outcome through a later designation `F'` (TR69), a future owner's pre-ownership supersession not processed in either half (TR70); the second cases of TR54 and TR61 state the point-5 (control harness) outcome and the full-chain ERROR `CONFIG_UNREVIEWED` at point 7, TR60's `F` has a configuration authorization 5555 made after the change, and TR68 states that every other approval and review in each case is valid.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
| TR54 | (review probe D1) owner 4242 designates `F`; an owner change 4242 -> 5555 merges; no later designation. Separately, 5555 then designates `F` | the first: ERROR (missing designation; the former owner's designation does not count); the second: `F` is the one designated commit at point 5 (control harness); in a full chain, ERROR `CONFIG_UNREVIEWED` at point 7, since `F`'s configuration authorization predates the owner change and `F` must be re-frozen | Owner at creation (DI-1) |
| TR55 | (D2) 4242 designates and then withdraws `F`, the withdrawal not in the freeze ledger; 4242 -> 5555; 5555 designates `F` | ERROR (designation of a withdrawn commit: the withdrawal, an owner comment at its creation, binds after the owner change) | DI-1 |
| TR56 | (D3) 5555 designates `F` while 4242 is the owner; then 4242 -> 5555; no later designation | ERROR (missing designation: the comment is not an owner comment) | DI-1 |
| TR57 | (L5) a freeze-ledger change whose `oi-authority/1 approve` and `oi-freeze-ledger/1 append` comments 4242 created before 4242 -> 5555 -> 4242, merged after the change back; each ledger route separately | the change is refused (an owner change merged between the approvals' creation and the merge): an acceptance landing carrying it does not merge, and a ledger on `main` carrying it makes every later admission refuse | DI-1 |
| TR58 | (L6) 5555 creates both approval comments of a freeze-ledger change while 4242 is the owner; 4242 -> 5555; the change merged under 5555; each ledger route separately | refused as in TR57 (the approvals are not owner comments) | DI-1 |
| TR59 | 4242 designates `F`; 4242 -> 5555 -> 4242; no later designation | ERROR (missing designation: an owner change merged between the designation's creation and the admission) | DI-1 |
| TR60 | (positive) a freeze-ledger append approved by 4242 and merged while 4242 is the owner; later an owner change 4242 -> 5555 approved by both ids; 5555 designates an `F` whose configuration authorization 5555 made after the change | the earlier append and the authority chain verify (completed actions); `F` admitted | DI-1 |
| TR61 | 4242 designates `F` and then supersedes it by `F2` in the thread, not in the ledger; 4242 -> 5555. Separately, 5555 then designates `F2` | admission of `F`: ERROR (`F` withdrawn) in both; admission of `F2`: ERROR (missing designation) in the first; in the second, `F2` is the one designated commit at point 5 (control harness), and in a full chain ERROR `CONFIG_UNREVIEWED` at point 7 as in TR54 | DI-1 |
| TR62 | an owner-id change 4242 -> 5555 approved by 4242 and by 5555, both created before the merge; separately, 5555's approval created after the merge | the first: the change verifies (5555's approval is authenticated as the id the new `A` pins); the second: ERROR | DI-1; authority changes |
| TR63 | an `A` on `main` whose `supersedes` names a blob other than the version of `A` preceding it on `main`'s first-parent chain; separately, names null while a version precedes it | ERROR `CONFIG_UNREVIEWED` in both | DI-2 (`A`) |
| TR64 | (positive) a freeze-ledger change whose approvals 4242 created before a merged change of `A` that keeps `owner.id` 4242 (for example a changed engine pin), merged after it | the approvals count (no owner change); the change verifies | DI-1 |
| TR65 | (authorization analogue of D3 and L5) an authorization record whose `time` falls while 4242 is owner and whose `owner` is 5555; 4242 -> 5555; 5555 designates `F`, whose configuration uses it. Separately, 4242's authorization with `time` before 4242 -> 5555 -> 4242. Separately (positive), 5555's authorization with `time` after 4242 -> 5555 | the first two: ERROR `CONFIG_UNREVIEWED` for the configuration's authorization, FAIL `record-invalid` for any other record's; the third: admitted | DI-1 |
| TR66 | 4242 designates `F`; 5555 posts `oi-freeze/1 withdraw` of `F` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness). Separately, the withdrawal posted by 4242 before the change | the first: `F` is the one designated commit at point 5 (the withdrawal is not an owner comment and is not processed); the second: ERROR (designation of a withdrawn commit) | DI-1 |
| TR67 | a comment without a form, created by 4242 while owner; 4242 -> 5555; the comment then edited by 4242 into a first line beginning `oi-freeze/`. Separately, the same comment left unedited | the first: ERROR (point 3); the second: no refusal from point 3 or 4 | DI-1, point 3 |
| TR68 | V1 (owner 4242) -> V2 (owner 5555) is an owner change. Each case separately, with every other approval and review in it valid, so that each case isolates one defect: an `A` change V2 -> V3 keeping 5555, whose previous-id approval (`from=<sha256 of V2>`) 5555 created while V1 was in force; an `A` change V3 -> V4 after V2 -> V3 (5555 -> 4242), whose previous-id approval 4242 created while V1 was in force; an owner-id change V2 -> V3 (5555 -> 6666), whose new-id approval 6666 created before V1 -> V2 merged | ERROR in each case: the change does not take effect, and every later admission refuses | DI-1; authority changes |
| TR69 | 5555 designates `F` while 4242 is the owner; 4242 -> 5555; 5555 withdraws `F`; 5555 then designates `F'` | ERROR (a withdrawal naming a commit never designated: the designation was not an owner comment at its creation); admission of `F'`: ERROR | DI-1, point 5 |
| TR70 | 4242 designates `F`; 5555 posts `oi-freeze/1 supersede` of `F` by `F2` while 4242 is the owner; 4242 -> 5555; 5555 designates `F` (control harness) | `F` is the one designated commit at point 5 (the supersession is not an owner comment; neither half is processed) | DI-1, point 5 |
````

### Hunk 13: 13.2, after S4a

Header `@@ -2461,6 +2569,18 @@`. Decision / correction: DI-2; LN9 review-v5.5.4 C4 (B2, DI-1); LN10 review-v5.5.4 C4; LN11 review-v5.5.5 C6(c) (F2); LN12 review-v5.5.7 B-4.

Summary: New controls LN1-LN12: E6 (LN1), positive (LN2), missing `record_id` (LN3), predecessor failing lint (LN4), cycle (LN5), fork (LN6), two heads (LN7), unrelated chain (LN8), predecessor authorized by a former owner (LN9), `supersedes: null` without `record_id` stays usable (LN10), predecessor's widening review authorized by a former owner, allow-rule and configuration lineages (LN11), predecessor's widening review authorized by a future owner or by no authorization record (LN12).

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
| LN1 | (review probe E6) a record superseding a record of the same kind and schema, present at `F`, with another `record_id`; for each kind of S4a (`config_id` for the configuration) | FAIL `record-invalid` for each kind (DI-2) |
| LN2 | (positive) a record superseding a record of the same kind, schema and `record_id` that itself passes the lint | no `record-invalid`; the run uses the superseding record (DI-2) |
| LN3 | a superseding record whose `record_id` is missing, empty or not a string; separately, a valid superseding record whose predecessor lacks a valid `record_id` | FAIL `record-invalid` in each case (DI-2) |
| LN4 | a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict not `accept`; separately, no authorization) | FAIL `record-invalid` for the superseding record in each case (DI-2) |
| LN5 | a `supersedes` cycle of two records, and a self-supersession, in a synthetic in-memory store that resolves each named `{path, blob_sha256}` to the given record without rehashing (a hash cycle cannot be built from real objects) | FAIL `record-invalid` in both; the chain walk terminates (DI-2) |
| LN6 | two records of one lineage superseding the same predecessor, both in the audit directory at `F`, only one referenced by the configuration | FAIL `record-invalid` (ambiguous ancestry) (DI-2) |
| LN7 | two records with one `record_id` and kind, each with `supersedes: null` (separately, two chains from one first record that diverge), both read in one run | FAIL `record-invalid` (two heads) (DI-2) |
| LN8 | a three-record chain whose middle record has another `record_id` (separately, another schema of the same kind) | FAIL `record-invalid` (unrelated chain) (DI-2) |
| LN9 | a predecessor R1 authorized by 4242 while owner; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run. Separately, R1's authorization `time` before 4242 was owner | the first: no `record-invalid`, the run uses R2; the second: FAIL `record-invalid` | DI-1, DI-2 |
| LN10 | (positive) a record with `supersedes: null` and no `record_id`, named by no `supersedes` | no `record-invalid` | DI-2 |
| LN11 | an allow rule R1 widening R0, R1's widening review authorized by 4242 while owner in an authorization record separate from R1's own; 4242 -> 5555; R2 superseding R1, reviewed and authorized by 5555, used by the run; separately, the same for a configuration lineage | no `record-invalid`; the run uses R2, in both | DI-1, DI-2 |
| LN12 | as LN11 for an allow rule, each case separately: R1's widening review listed only by an authorization record with `owner` 5555 whose `time` falls while 4242 is the owner; R1's widening review listed by no authorization record | FAIL `record-invalid` for the superseding record R2 in each case | DI-1, DI-2 |
````

### Hunk 14: 16.8, S13 acceptance list

Header `@@ -3024,4 +3144,4 @@`. Decision / correction: DI-1, DI-2 (consequence); review-v5.5.4 C4, review-v5.5.5 C7, review-v5.5.6 C9, review-v5.5.7 B-3, B-4.

Summary: "S4a," gains "LN1-LN12,"; "TR1-TR53" becomes "TR1-TR70".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, S11-57a-d, S11-58a-k, G9, TR1-TR53, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````

New text (contiguous lines of DESIGN-v5.5.8.md):

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, LN1-LN12, S11-57a-d, S11-58a-k, G9, TR1-TR70, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````
