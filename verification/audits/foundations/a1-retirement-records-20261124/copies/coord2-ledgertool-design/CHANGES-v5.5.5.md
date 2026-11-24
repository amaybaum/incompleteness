# DESIGN-v5.5.5: changes against DESIGN-v5.5.3

## Input and scope

Inputs, sha256 verified before use and after writing (all unchanged):

- `DESIGN-v5.5.3.md` (frozen): 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379
- `DESIGN-v5.5.4.md` (draft): 1ade8b8f43d6259c50ac9847c59e09ce71a645ba0cb8eabe7e1deb84bb4c5e34
- `CHANGES-v5.5.4.md`: 76d4a41312bd2f4df18f0c50251a4e4a89aa465c06e9bbce043815671953434c
- `review-v5.5.4/review.md`: 34927de86bdbed0d8e8cc8e4e2438f18bf001082153bfddb283781767c5f0842

v5.5.5 is a draft amendment of v5.5.3 implementing the owner decisions DI-1 (option B) and DI-2
(option A, narrow). It is authoritative only after an independent review returns ACCEPT and the
owner adopts it. It supersedes the v5.5.4 draft. It is v5.5.4 plus exactly the review's
corrections C1-C4 (sec. 5 of `review-v5.5.4/review.md`), a cross-reference for N3 in admission
point 5, and the status line and version label. Nothing else changes relative to v5.5.4.

New control ids: TR54-TR65 and LN1-LN10. Checked by word-bounded grep: TR65, LN9 and LN10 occur
in no `DESIGN*.md` or `CHANGES*.md` other than v5.5.5 and this file; TR54-TR64 and LN1-LN8 occur
only in v5.5.4 and its change list (the draft this one supersedes, same meaning). No id is reused.

The work was paper-only: no repository file, git or GitHub activity.

## Changes from v5.5.4 (`CHANGES-v5.5.5-from-v5.5.4.diff`, 9 hunks)

| # | v5.5.4 -> v5.5.5 hunk | Implements |
|---|---|---|
| a | `@@ -1,4 +1,4 @@` title "v5.5.4" -> "v5.5.5" | version label |
| b | `@@ -7,14 +7,15 @@` status bullet: v5.5.5, "It supersedes the v5.5.4 draft", controls "TR54-TR62, TR64 and TR65", "LN1-LN10 and TR63", `CHANGES-v5.5.5.md` | status line; C4 consequential |
| c | `@@ -1251,7 +1252,8 @@` lineage predecessor clause: authorization checked as "Owner at creation" states for a predecessor, in place of the configuration-owner comparison | C2 |
| d | `@@ -1340,6 +1342,12 @@` new "Owner authorizations" bullet after "Approvals" | C1 |
| e | `@@ -1501,7 +1509,8 @@` point 5 supersession item: cross-reference that a recorded supersession only revokes | N3 (cross-reference only) |
| f | `@@ -1511,7 +1520,9 @@` point 7: every authorization record must count under "Owner at creation" | C3 |
| g | `@@ -2326,6 +2337,7 @@` control TR65 after TR64 | C4 |
| h | `@@ -2557,6 +2569,8 @@` controls LN9, LN10 after LN8 | C4 |
| i | `@@ -3120,4 +3134,4 @@` S13: "LN1-LN8" -> "LN1-LN10", "TR1-TR64" -> "TR1-TR65" | C4 consequential |

### Where the review's text was not placed verbatim

- **C1, C4 (TR65, LN9, LN10):** placed verbatim.
- **C2, C3:** the words are verbatim; only the line breaks differ, because the replaced and
  appended text is wrapped at the document's line width and indentation (C2 inside a nested list
  item, C3 inside numbered point 7). C3's inline code spans (`record-invalid`, `CONFIG_UNREVIEWED`) are rendered with
  single backticks as in the rest of the document (the review's quoting wraps the appended text
  in backticks too, which cannot be nested).
- **N3:** the review gives no exact text. The added parenthesis is the minimal cross-reference:
  "(a supersession recorded in the freeze ledger or in a committed snapshot only revokes: "Owner
  at creation", "Designations")". No other wording in point 5 changes.
- **Status line:** "It supersedes the v5.5.4 draft." is inserted into the existing bullet, leaving
  one short line ("v5.5.4 draft. It implements only") rather than reflowing unchanged lines.

The review's N1, N2 (applied to this change list: every hunk below quotes whole contiguous lines),
N4 and N5 need no design text; none was added for them.

## Complete amendment relative to v5.5.3 (`CHANGES-v5.5.5.diff`, 15 hunks)

`diff -u DESIGN-v5.5.3.md DESIGN-v5.5.5.md`; 3027 -> 3137 lines. For each hunk, the old and new
text below are the whole contiguous span of lines from the first to the last changed line of the
hunk, including unchanged lines between changes, copied from the two files (checked by script:
each block occurs verbatim in its file). For an insertion the location names the anchor.

| # | Hunk header | Location | Decision / correction |
|---|---|---|---|
| 1 | `@@ -1,4 +1,4 @@` | title | both (version label) |
| 2 | `@@ -7,6 +7,16 @@` | Status and authority, new bullet after the first bullet | both (status line); control ranges per review C4 |
| 3 | `@@ -1230,6 +1240,26 @@` | 6.3, "What the tool checks", after the `supersedes` bullet | DI-2; predecessor clause per review C2 (B2) |
| 4 | `@@ -1265,7 +1295,9 @@` | 6.3, authority record `A`, field `supersedes` | DI-2 |
| 5 | `@@ -1285,6 +1317,50 @@` | 6.3, after "The forms", new paragraph "Owner at creation" | DI-1; "Owner authorizations" bullet per review C1 (B1, B2) |
| 6 | `@@ -1335,8 +1411,10 @@` | 6.3, "Authority changes", approval and owner-id-change bullets | DI-1 |
| 7 | `@@ -1375,7 +1453,8 @@` | 6.3, "The freeze ledger", N3 bullet, author requirement | DI-1 |
| 8 | `@@ -1408,7 +1487,9 @@` | 6.3, Admission point 3 | DI-1 |
| 9 | `@@ -1420,13 +1501,16 @@` | 6.3, Admission points 4 and 5 | DI-1; cross-reference per review N3 |
| 10 | `@@ -1436,7 +1520,9 @@` | 6.3, Admission point 7 | DI-1; review C3 (B1) |
| 11 | `@@ -1451,8 +1537,9 @@` | 6.3, "The admission snapshot" | DI-1 (consequence) |
| 12 | `@@ -1477,7 +1564,8 @@` | 6.3, "Residual trust assumptions", first bullet | DI-1 (consequence) |
| 13 | `@@ -2238,6 +2326,18 @@` | 10.4, after TR53 | DI-1; TR63 DI-2; TR65 review C4 (B1) |
| 14 | `@@ -2461,6 +2561,16 @@` | 13.2, after S4a | DI-2; LN9 review C4 (B2, DI-1); LN10 review C4 |
| 15 | `@@ -3024,4 +3134,4 @@` | 16.8, S13 acceptance list | DI-1, DI-2 (consequence); review C4 |

### Hunk 1: title

Header `@@ -1,4 +1,4 @@`. Decision / correction: both (version label).

Summary: Title: "design v5.5.3" becomes "design v5.5.5".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
# Commit-independent ledger and terminology verification tool: design v5.5.3
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
# Commit-independent ledger and terminology verification tool: design v5.5.5
````

### Hunk 2: Status and authority, new bullet after the first bullet

Header `@@ -7,6 +7,16 @@`. Decision / correction: both (status line); control ranges per review C4.

Summary: Status line: v5.5.5 is a draft amendment of v5.5.3 implementing DI-1 and DI-2, authoritative only after independent ACCEPT and owner adoption, superseding the v5.5.4 draft; names its controls (TR54-TR62, TR64, TR65; LN1-LN10, TR63).

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
- **v5.5.5 is a draft amendment of the frozen v5.5.3.** It is authoritative only after an
  independent review returns ACCEPT and the owner adopts it; until then the frozen design is v5.5.3
  (sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379). It supersedes the
  v5.5.4 draft. It implements only
  two owner decisions of 2026-11-23 on the design issues of the fourth Stage 1 review
  (`review-stage1-r4/review.md`, sec. 7): DI-1, option B, the owner identity of a comment (sec. 6.3,
  "Owner at creation"; controls TR54-TR62, TR64 and TR65); and DI-2, option A in its narrow form, the
  lineage of a superseding record (sec. 6.3, record lint and the field `supersedes` of `A`;
  controls LN1-LN10 and TR63). Nothing else changes. `CHANGES-v5.5.5.md` lists every changed
  passage.
````

### Hunk 3: 6.3, "What the tool checks", after the `supersedes` bullet

Header `@@ -1230,6 +1240,26 @@`. Decision / correction: DI-2; predecessor clause per review C2 (B2).

Summary: New lint bullet defining lineage as `record_id` (`config_id` for the configuration), its immutability, the record-invalid cases (no valid `record_id`, unrelated chain, predecessor failing the lint, cycle, fork, two heads in one run), and what counts as id reuse; the predecessor's authorization is checked as "Owner at creation" states for a predecessor, not against the configuration's owner.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.5.md):

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
    and authorization, the authorization checked as "Owner at creation" states for a predecessor,
    in place of the comparison with the configuration's owner);
  - a cycle in a `supersedes` chain;
  - ambiguous ancestry: two records superseding the same predecessor, among the records in the
    audit directory and the plan's record directory at `F` and the records the run reads; or a
    lineage with two heads used in one run, a head being a record of the lineage that no other
    record the run reads (the records the configuration references and every record their chains
    name) supersedes;
````

### Hunk 4: 6.3, authority record `A`, field `supersedes`

Header `@@ -1265,7 +1295,9 @@`. Decision / correction: DI-2.

Summary: `A`'s lineage is its fixed path; its `supersedes` must name the preceding version of `A` on `main`'s first-parent chain, otherwise admission refuses.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first.
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first. `A` carries no
  `record_id`: its lineage is its fixed path. `supersedes` must name the version of `A` that
  precedes it on `main`'s first-parent chain, at the same path; otherwise admission refuses (DI-2).
````

### Hunk 5: 6.3, after "The forms", new paragraph "Owner at creation"

Header `@@ -1285,6 +1317,50 @@`. Decision / correction: DI-1; "Owner authorizations" bullet per review C1 (B1, B2).

Summary: Defines version in force, owner comment, owner change; withdrawals; designations; approvals; owner authorizations (owner at its `time`, owner under the governing `A`, no owner change between its `time` and the admission; a predecessor's authorization needs only owner at its `time`); first `A` and owner-id change; completed actions.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.5.md):

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
  between its `time` and the admission. The authorization of a predecessor named by a `supersedes`
  is a completed action: it counts if the version of `A` in force at its `time` has `owner.id` equal
  to its `owner`.
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

Header `@@ -1335,8 +1411,10 @@`. Decision / correction: DI-1.

Summary: The approval must also count under "Owner at creation"; the new id's approval in an owner-id change is authenticated as that paragraph states.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  lands the new `A`. The merge alone authorizes nothing.
- **An owner-id change** also needs the same approval from the new id, in a separate comment.
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
  lands the new `A`. The merge alone authorizes nothing. It must also count as an approval under
  "Owner at creation" above.
- **An owner-id change** also needs the same approval from the new id, in a separate comment. That
  approval is authenticated as "Owner at creation" states for the new id.
````

### Hunk 7: 6.3, "The freeze ledger", N3 bullet, author requirement

Header `@@ -1375,7 +1453,8 @@`. Decision / correction: DI-1.

Summary: "authored by numeric owner id `A.owner.id`" becomes "an owner comment that counts as an approval under Owner at creation".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  - be authored by numeric owner id `A.owner.id` (7273571);
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
  - be an owner comment that counts as an approval under "Owner at creation" above (for A1, numeric
    owner id 7273571);
````

### Hunk 8: 6.3, Admission point 3

Header `@@ -1408,7 +1487,9 @@`. Decision / correction: DI-1.

Summary: Point 3 reads edit status for comments by `A.owner.id` and for every owner comment at creation, and records the version of `A` in force at each comment's creation.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
   `A.owner.id`, relevant or not, the tool reads its edit status (REST `updated_at`; GraphQL
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
   `A.owner.id`, and every owner comment as "Owner at creation" defines it (in this point and point
   4, each of them is meant by "an owner comment"), relevant or not, the tool reads the version of
   `A` in force at its creation and its edit status (REST `updated_at`; GraphQL
````

### Hunk 9: 6.3, Admission points 4 and 5

Header `@@ -1420,13 +1501,16 @@`. Decision / correction: DI-1; cross-reference per review N3.

Summary: Point 4 parses the owner comments of point 3; point 5 does not process a form or half of a supersession that does not count under "Owner at creation"; point 5's supersession item cross-refers to the rule that a recorded supersession only revokes.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
4. **Forms.** The owner comments whose first line begins with `oi-freeze/` are parsed by the forms
   above. A malformed or unknown-version line refuses.
5. **Deterministic state.** The forms for this plan and round, together with the bound events of the
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id:
   - a designation of `F` makes `F` designated;
   - a withdrawal of `F` makes it withdrawn;
   - a supersession of `F` by `F2` withdraws `F` and designates `F2`.
````

New text (contiguous lines of DESIGN-v5.5.5.md):

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
````

### Hunk 10: 6.3, Admission point 7

Header `@@ -1436,7 +1520,9 @@`. Decision / correction: DI-1; review C3 (B1).

Summary: Every authorization record the run uses must also count under "Owner at creation"; otherwise FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED` for the configuration's own.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
   configuration's authorization record.
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
   configuration's authorization record. Every authorization record the run uses must also count
   under "Owner at creation" above; otherwise FAIL `record-invalid`, or ERROR `CONFIG_UNREVIEWED`
   for the configuration's own.
````

### Hunk 11: 6.3, "The admission snapshot"

Header `@@ -1451,8 +1537,9 @@`. Decision / correction: DI-1 (consequence).

Summary: The snapshot records every comment of point 3, with the blob of the version of `A` in force at its creation.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
- for every owner comment: id, author numeric id, creation time, edit status, hidden state, full
  first line and body sha256;
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
- for every comment of admission point 3: id, author numeric id, creation time, the blob sha256 of
  the version of `A` in force at its creation, edit status, hidden state, full first line and body
  sha256;
````

### Hunk 12: 6.3, "Residual trust assumptions", first bullet

Header `@@ -1477,7 +1564,8 @@`. Decision / correction: DI-1 (consequence).

Summary: Adds a pull request's merge time to the trusted host attestations.

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
  merged-by id; and a comment's immutable id, numeric author id, creation time, edit history,
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
  merged-by id and merge time; and a comment's immutable id, numeric author id, creation time,
  edit history,
````

### Hunk 13: 10.4, after TR53

Header `@@ -2238,6 +2326,18 @@`. Decision / correction: DI-1; TR63 DI-2; TR65 review C4 (B1).

Summary: New controls TR54-TR65: D1 (TR54), D2 (TR55), D3 (TR56), L5 (TR57), L6 (TR58), A->B->A designation (TR59), completed actions (TR60), former-owner supersession (TR61), owner-id change (TR62), `A.supersedes` (TR63), non-owner `A` change (TR64), authorization records analogue of D3/L5 with one positive (TR65).

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
| TR54 | (review probe D1) owner 4242 designates `F`; an owner change 4242 -> 5555 merges; no later designation. Separately, 5555 then designates `F` | the first: ERROR (missing designation; the former owner's designation does not count); the second: `F` admitted as designated | Owner at creation (DI-1) |
| TR55 | (D2) 4242 designates and then withdraws `F`, the withdrawal not in the freeze ledger; 4242 -> 5555; 5555 designates `F` | ERROR (designation of a withdrawn commit: the withdrawal, an owner comment at its creation, binds after the owner change) | DI-1 |
| TR56 | (D3) 5555 designates `F` while 4242 is the owner; then 4242 -> 5555; no later designation | ERROR (missing designation: the comment is not an owner comment) | DI-1 |
| TR57 | (L5) a freeze-ledger change whose `oi-authority/1 approve` and `oi-freeze-ledger/1 append` comments 4242 created before 4242 -> 5555 -> 4242, merged after the change back; each ledger route separately | the change is refused (an owner change merged between the approvals' creation and the merge): an acceptance landing carrying it does not merge, and a ledger on `main` carrying it makes every later admission refuse | DI-1 |
| TR58 | (L6) 5555 creates both approval comments of a freeze-ledger change while 4242 is the owner; 4242 -> 5555; the change merged under 5555; each ledger route separately | refused as in TR57 (the approvals are not owner comments) | DI-1 |
| TR59 | 4242 designates `F`; 4242 -> 5555 -> 4242; no later designation | ERROR (missing designation: an owner change merged between the designation's creation and the admission) | DI-1 |
| TR60 | (positive) a freeze-ledger append approved by 4242 and merged while 4242 is the owner; later an owner change 4242 -> 5555 approved by both ids; 5555 designates `F` | the earlier append and the authority chain verify (completed actions); `F` admitted | DI-1 |
| TR61 | 4242 designates `F` and then supersedes it by `F2` in the thread, not in the ledger; 4242 -> 5555. Separately, 5555 then designates `F2` | admission of `F`: ERROR (`F` withdrawn) in both; admission of `F2`: ERROR (missing designation) in the first, admitted in the second | DI-1 |
| TR62 | an owner-id change 4242 -> 5555 approved by 4242 and by 5555, both created before the merge; separately, 5555's approval created after the merge | the first: the change verifies (5555's approval is authenticated as the id the new `A` pins); the second: ERROR | DI-1; authority changes |
| TR63 | an `A` on `main` whose `supersedes` names a blob other than the version of `A` preceding it on `main`'s first-parent chain; separately, names null while a version precedes it | ERROR `CONFIG_UNREVIEWED` in both | DI-2 (`A`) |
| TR64 | (positive) a freeze-ledger change whose approvals 4242 created before a merged change of `A` that keeps `owner.id` 4242 (for example a changed engine pin), merged after it | the approvals count (no owner change); the change verifies | DI-1 |
| TR65 | (authorization analogue of D3 and L5) an authorization record whose `time` falls while 4242 is owner and whose `owner` is 5555; 4242 -> 5555; 5555 designates `F`, whose configuration uses it. Separately, 4242's authorization with `time` before 4242 -> 5555 -> 4242. Separately (positive), 5555's authorization with `time` after 4242 -> 5555 | the first two: ERROR `CONFIG_UNREVIEWED` for the configuration's authorization, FAIL `record-invalid` for any other record's; the third: admitted | DI-1 |
````

### Hunk 14: 13.2, after S4a

Header `@@ -2461,6 +2561,16 @@`. Decision / correction: DI-2; LN9 review C4 (B2, DI-1); LN10 review C4.

Summary: New controls LN1-LN10: E6 (LN1), positive (LN2), missing `record_id` (LN3), predecessor failing lint (LN4), cycle (LN5), fork (LN6), two heads (LN7), unrelated chain (LN8), predecessor authorized by a former owner (LN9), `supersedes: null` without `record_id` stays usable (LN10).

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
(none: insertion only)
````

New text (contiguous lines of DESIGN-v5.5.5.md):

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
````

### Hunk 15: 16.8, S13 acceptance list

Header `@@ -3024,4 +3134,4 @@`. Decision / correction: DI-1, DI-2 (consequence); review C4.

Summary: "S4a," gains "LN1-LN10,"; "TR1-TR53" becomes "TR1-TR65".

Old text (contiguous lines of DESIGN-v5.5.3.md):

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, S11-57a-d, S11-58a-k, G9, TR1-TR53, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````

New text (contiguous lines of DESIGN-v5.5.5.md):

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, LN1-LN10, S11-57a-d, S11-58a-k, G9, TR1-TR65, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````
