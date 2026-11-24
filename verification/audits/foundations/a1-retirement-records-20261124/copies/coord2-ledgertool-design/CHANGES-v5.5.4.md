# DESIGN-v5.5.4: changes against DESIGN-v5.5.3

## Input and scope

The input is `DESIGN-v5.5.3.md`, sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379. I verified the hash before use and after
writing; the file is unchanged.

v5.5.4 is a draft amendment. It is authoritative only after an independent review returns ACCEPT
and the owner adopts it. It implements only the owner decisions of 2026-11-23 on the design issues
DI-1 (option B: owner identity of a comment) and DI-2 (option A, narrow: lineage of a superseding
record) of `review-stage1-r4/review.md`, sec. 7. Nothing else is changed: no rewording, reflowing
or renumbering elsewhere. Existing control ids are untouched; new ids are TR54-TR64 and LN1-LN8,
none of which occurs in any earlier design or change list.

The work was paper-only: nothing was written to the repository, git or GitHub.

## Changes

`diff -u DESIGN-v5.5.3.md DESIGN-v5.5.4.md` (saved as `CHANGES-v5.5.4.diff`) has 14 hunks. The
document grows from 3027 to 3123 lines.

| # | Hunk header | Location | Summary | Decision |
|---|---|---|---|---|
| 1 | `@@ -1,4 +1,4 @@` | title | Title: "design v5.5.3" becomes "design v5.5.4" | both (version label) |
| 2 | `@@ -7,6 +7,15 @@` | Status and authority, new bullet after the first bullet | Status line: v5.5.4 is a draft amendment, authoritative only after independent ACCEPT and owner adoption; names DI-1 and DI-2 and their controls | both (status line) |
| 3 | `@@ -1230,6 +1239,25 @@` | 6.3, "What the tool checks", after the `supersedes` bullet | New lint bullet defining lineage as `record_id` (`config_id` for the configuration), its immutability, the record-invalid cases (no valid `record_id`, unrelated chain, predecessor failing the lint, cycle, fork, two heads in one run), and what counts as id reuse | DI-2 |
| 4 | `@@ -1265,7 +1293,9 @@` | 6.3, authority record `A`, field `supersedes` | `A`'s lineage is its fixed path; its `supersedes` must name the preceding version of `A` on `main`'s first-parent chain, otherwise admission refuses | DI-2 |
| 5 | `@@ -1285,6 +1315,44 @@` | 6.3, after "The forms", new paragraph "Owner at creation" | Defines the version in force, owner comment and owner change; withdrawal/revoking half counts if an owner comment at creation and survives owner changes; designations and designating half need owner at creation, current governing owner and no owner change since; approvals need owner at creation, governing owner, no owner change before the merge; first-A and new-id exception; completed actions | DI-1 |
| 6 | `@@ -1335,8 +1403,10 @@` | 6.3, "Authority changes", approval and owner-id-change bullets | The approval must also count under "Owner at creation"; the new id's approval in an owner-id change is authenticated as that paragraph states | DI-1 |
| 7 | `@@ -1375,7 +1445,8 @@` | 6.3, "The freeze ledger", N3 bullet, author requirement | "authored by numeric owner id `A.owner.id`" becomes "an owner comment that counts as an approval under Owner at creation" | DI-1 |
| 8 | `@@ -1408,7 +1479,9 @@` | 6.3, Admission point 3 | Point 3 reads edit status for comments by `A.owner.id` and for every owner comment at creation (both called owner comments in points 3-4), and records the version of `A` in force at each comment's creation | DI-1 |
| 9 | `@@ -1420,10 +1493,12 @@` | 6.3, Admission points 4 and 5 | Point 4 parses the owner comments of point 3; point 5 does not process a form or half of a supersession that does not count under "Owner at creation" | DI-1 |
| 10 | `@@ -1451,8 +1526,9 @@` | 6.3, "The admission snapshot" | The snapshot records every comment of point 3, with the blob of the version of `A` in force at its creation | DI-1 (consequence) |
| 11 | `@@ -1477,7 +1553,8 @@` | 6.3, "Residual trust assumptions", first bullet | Adds a pull request's merge time to the trusted host attestations | DI-1 (consequence) |
| 12 | `@@ -2238,6 +2315,17 @@` | 10.4, after TR53 | New controls TR54-TR64: D1 (TR54), D2 (TR55), D3 (TR56), L5 (TR57), L6 (TR58), designation across A->B->A (TR59), completed actions (TR60), former-owner supersession (TR61), owner-id change (TR62), `A.supersedes` (TR63, DI-2), non-owner `A` change between approval and merge (TR64) | DI-1; TR63 DI-2 |
| 13 | `@@ -2461,6 +2549,14 @@` | 13.2, after S4a | New controls LN1-LN8: E6 (LN1), positive (LN2), missing `record_id` (LN3), predecessor failing lint (LN4), cycle (LN5), fork (LN6), two heads (LN7), unrelated multi-step chain (LN8) | DI-2 |
| 14 | `@@ -3024,4 +3120,4 @@` | 16.8, S13 acceptance list | "S4a," gains "LN1-LN8,"; "TR1-TR53" becomes "TR1-TR64" | DI-1, DI-2 (consequence) |

### Hunk 1: title

Header `@@ -1,4 +1,4 @@`. Decision: both (version label).

Old text:

````text
# Commit-independent ledger and terminology verification tool: design v5.5.3
````

New text:

````text
# Commit-independent ledger and terminology verification tool: design v5.5.4
````

### Hunk 2: Status and authority, new bullet after the first bullet

Header `@@ -7,6 +7,15 @@`. Decision: both (status line).

Old text:

````text
(none: insertion only)
````

New text:

````text
- **v5.5.4 is a draft amendment of the frozen v5.5.3.** It is authoritative only after an
  independent review returns ACCEPT and the owner adopts it; until then the frozen design is v5.5.3
  (sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379). It implements only
  two owner decisions of 2026-11-23 on the design issues of the fourth Stage 1 review
  (`review-stage1-r4/review.md`, sec. 7): DI-1, option B, the owner identity of a comment (sec. 6.3,
  "Owner at creation"; controls TR54-TR62 and TR64); and DI-2, option A in its narrow form, the
  lineage of a superseding record (sec. 6.3, record lint and the field `supersedes` of `A`;
  controls LN1-LN8 and TR63). Nothing else changes. `CHANGES-v5.5.4.md` lists every changed
  passage.
````

### Hunk 3: 6.3, "What the tool checks", after the `supersedes` bullet

Header `@@ -1230,6 +1239,25 @@`. Decision: DI-2.

Old text:

````text
(none: insertion only)
````

New text:

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
    and authorization);
  - a cycle in a `supersedes` chain;
  - ambiguous ancestry: two records superseding the same predecessor, among the records in the
    audit directory and the plan's record directory at `F` and the records the run reads; or a
    lineage with two heads used in one run, a head being a record of the lineage that no other
    record the run reads (the records the configuration references and every record their chains
    name) supersedes;
````

### Hunk 4: 6.3, authority record `A`, field `supersedes`

Header `@@ -1265,7 +1293,9 @@`. Decision: DI-2.

Old text:

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first.
````

New text:

````text
- `supersedes`: `{path, blob_sha256}` of the `A` it replaces, or null for the first. `A` carries no
  `record_id`: its lineage is its fixed path. `supersedes` must name the version of `A` that
  precedes it on `main`'s first-parent chain, at the same path; otherwise admission refuses (DI-2).
````

### Hunk 5: 6.3, after "The forms", new paragraph "Owner at creation"

Header `@@ -1285,6 +1315,44 @@`. Decision: DI-1.

Old text:

````text
(none: insertion only)
````

New text:

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

Header `@@ -1335,8 +1403,10 @@`. Decision: DI-1.

Old text:

````text
  lands the new `A`. The merge alone authorizes nothing.
- **An owner-id change** also needs the same approval from the new id, in a separate comment.
````

New text:

````text
  lands the new `A`. The merge alone authorizes nothing. It must also count as an approval under
  "Owner at creation" above.
- **An owner-id change** also needs the same approval from the new id, in a separate comment. That
  approval is authenticated as "Owner at creation" states for the new id.
````

### Hunk 7: 6.3, "The freeze ledger", N3 bullet, author requirement

Header `@@ -1375,7 +1445,8 @@`. Decision: DI-1.

Old text:

````text
  - be authored by numeric owner id `A.owner.id` (7273571);
````

New text:

````text
  - be an owner comment that counts as an approval under "Owner at creation" above (for A1, numeric
    owner id 7273571);
````

### Hunk 8: 6.3, Admission point 3

Header `@@ -1408,7 +1479,9 @@`. Decision: DI-1.

Old text:

````text
   `A.owner.id`, relevant or not, the tool reads its edit status (REST `updated_at`; GraphQL
````

New text:

````text
   `A.owner.id`, and every owner comment as "Owner at creation" defines it (in this point and point
   4, each of them is meant by "an owner comment"), relevant or not, the tool reads the version of
   `A` in force at its creation and its edit status (REST `updated_at`; GraphQL
````

### Hunk 9: 6.3, Admission points 4 and 5

Header `@@ -1420,10 +1493,12 @@`. Decision: DI-1.

Old text:

````text
4. **Forms.** The owner comments whose first line begins with `oi-freeze/` are parsed by the forms
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id:
````

New text:

````text
4. **Forms.** The owner comments of point 3 whose first line begins with `oi-freeze/` are parsed
   by the forms
   freeze ledger and committed snapshots, are processed in order of creation time, then comment id.
   A form, or half of a supersession, that does not count under "Owner at creation" is not processed:
````

### Hunk 10: 6.3, "The admission snapshot"

Header `@@ -1451,8 +1526,9 @@`. Decision: DI-1 (consequence).

Old text:

````text
- for every owner comment: id, author numeric id, creation time, edit status, hidden state, full
  first line and body sha256;
````

New text:

````text
- for every comment of admission point 3: id, author numeric id, creation time, the blob sha256 of
  the version of `A` in force at its creation, edit status, hidden state, full first line and body
  sha256;
````

### Hunk 11: 6.3, "Residual trust assumptions", first bullet

Header `@@ -1477,7 +1553,8 @@`. Decision: DI-1 (consequence).

Old text:

````text
  merged-by id; and a comment's immutable id, numeric author id, creation time, edit history,
````

New text:

````text
  merged-by id and merge time; and a comment's immutable id, numeric author id, creation time,
  edit history,
````

### Hunk 12: 10.4, after TR53

Header `@@ -2238,6 +2315,17 @@`. Decision: DI-1; TR63 DI-2.

Old text:

````text
(none: insertion only)
````

New text:

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
````

### Hunk 13: 13.2, after S4a

Header `@@ -2461,6 +2549,14 @@`. Decision: DI-2.

Old text:

````text
(none: insertion only)
````

New text:

````text
| LN1 | (review probe E6) a record superseding a record of the same kind and schema, present at `F`, with another `record_id`; for each kind of S4a (`config_id` for the configuration) | FAIL `record-invalid` for each kind (DI-2) |
| LN2 | (positive) a record superseding a record of the same kind, schema and `record_id` that itself passes the lint | no `record-invalid`; the run uses the superseding record (DI-2) |
| LN3 | a superseding record whose `record_id` is missing, empty or not a string; separately, a valid superseding record whose predecessor lacks a valid `record_id` | FAIL `record-invalid` in each case (DI-2) |
| LN4 | a predecessor of the same lineage that fails the lint itself (no review record; separately, a verdict not `accept`; separately, no authorization) | FAIL `record-invalid` for the superseding record in each case (DI-2) |
| LN5 | a `supersedes` cycle of two records, and a self-supersession, in a synthetic in-memory store that resolves each named `{path, blob_sha256}` to the given record without rehashing (a hash cycle cannot be built from real objects) | FAIL `record-invalid` in both; the chain walk terminates (DI-2) |
| LN6 | two records of one lineage superseding the same predecessor, both in the audit directory at `F`, only one referenced by the configuration | FAIL `record-invalid` (ambiguous ancestry) (DI-2) |
| LN7 | two records with one `record_id` and kind, each with `supersedes: null` (separately, two chains from one first record that diverge), both read in one run | FAIL `record-invalid` (two heads) (DI-2) |
| LN8 | a three-record chain whose middle record has another `record_id` (separately, another schema of the same kind) | FAIL `record-invalid` (unrelated chain) (DI-2) |
````

### Hunk 14: 16.8, S13 acceptance list

Header `@@ -3024,4 +3120,4 @@`. Decision: DI-1, DI-2 (consequence).

Old text:

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, S11-57a-d, S11-58a-k, G9, TR1-TR53, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````

New text:

````text
| S13 | Configuration loader and validator, adapter admission by blob, the A1 configuration, the synthetic configuration | Z1-Z8, Z9a-Z9h, Z10, Z11 and Y1-Y10 behave; N2-N18, R18, R19, S4a, LN1-LN8, S11-57a-d, S11-58a-k, G9, TR1-TR64, WB13-WB15, X11, TR1-TR5, G4-G8, R16, R17, A12r, WB1-WB12, S11-56 and K10 behave; every A1 control has the same outcome as specified in sec. 10-11 of this document; no engine source contains an A1 constant (Z9) |
````

## How the decisions map to the review's probes

| Probe | v5.5.3 behaviour (review r4) | v5.5.4 rule | Control |
|---|---|---|---|
| D1 | former owner's designation stops counting | unchanged in effect, now explicit: re-designation by the owner in force | TR54 |
| D2 | former owner's unledgered withdrawal ignored; `F` re-designated | the withdrawal is an owner comment at creation and binds; ERROR | TR55 |
| D3 | new owner's pre-ownership designation counts | not an owner comment; ERROR (missing designation) | TR56 |
| L5 | approval revived by 4242 -> 5555 -> 4242 | owner change between approval and merge; refused | TR57 |
| L6 | approval by 5555 written while 4242 was owner counts | not an owner comment; refused | TR58 |
| E6 | supersession across `record_id` accepted | unrelated lineage; FAIL `record-invalid` | LN1 |

K1 is not reopened: "Owner at creation" restates that a supersession recorded in the ledger or a
committed snapshot only revokes and never designates, and admission point 5 processes only halves of
a supersession that count under the new paragraph. A recorded event never counts as a designation.

## Ambiguities and resolutions

1. **Designations across A -> B -> A.** The decision's bullet for designations requires "owner when
   posted AND owner of the governing record". Read literally, a designation by 4242 made before
   4242 -> 5555 -> 4242 would count again. The decision's opening principle says a comment must not
   acquire authority because its author "regains ownership". I applied the principle: a designation
   counts only if no owner change merged between its creation and the admission (control TR59). This
   refuses more than the literal bullet. If the owner intends the literal reading, delete that clause
   and TR59.
2. **"Owner change" versus any change of `A`.** The approval-timing rule is stated as "ownership must
   not change". A change of `A` that keeps `owner.id` (for example an engine pin) therefore does not
   invalidate a pending approval (positive control TR64).
3. **"Completed" and the rules in force at a merge.** A merged authority or ledger change stays valid
   if its approvals counted under the v5.5.4 rules at its merge. No authority record or ledger has
   landed under any design version, so there is no history governed by earlier rules. I did not add a
   "rules in force at the merge" clause, which the tool could not evaluate (it does not know which
   design version was in force at a merge). If something lands before adoption, this needs an owner
   decision.
4. **Edit-status scope (admission point 3).** Defining "owner comment" by the owner at creation would
   exclude comments the current owner wrote before becoming the owner. To refuse no less than
   v5.5.3, point 3 checks both sets: comments by `A.owner.id` and every owner comment at creation.
   Only comments counting under "Owner at creation" are processed in point 5.
5. **First `A` and the new id in an owner-id change.** Neither approval can be an owner comment,
   because its author is not yet the owner. Both are authenticated as the id the new `A` pins, as
   v5.5.3 already provides. They must still precede the merge, with no owner change between
   (control TR62).
6. **Consequential edits outside the two rules.** The admission snapshot now records the comments of
   point 3 with the version of `A` in force at each comment's creation, and the residual-trust list
   names the host's merge time, which the new rule relies on. Both follow from DI-1. Without them the
   snapshot would not show how the rule was applied, and the list would omit a trusted attestation.
7. **`record_id` is not a v5.5.3 field.** Only the configuration has a lineage field (`config_id`).
   The decision names `record_id` as the lineage. I declared it once, in the sec. 6.3 lint, as a
   top-level non-empty string. It is required only of a record that supersedes or is superseded,
   which the decision's "cannot supersede or be superseded" wording implies. No per-kind schema list
   was edited. I judged this the minimal identification and not a broader schema change. If the
   reviewer disagrees, this is the point to stop.
8. **`A` carries `supersedes` but no `record_id`.** Its lineage is its fixed path, already fixed by
   v5.5.3. I added only that `A.supersedes` must name the preceding version on `main`'s first-parent
   chain (control TR63). Forks and cycles cannot occur on one first-parent chain at one path. The
   freeze ledger carries no `supersedes` and is unaffected.
9. **Detection domain for forks.** The decision rejects "two records superseding the same
   predecessor" without naming where the tool looks. I used the records in the audit directory and
   the plan's record directory at `F` together with the records the run reads. "Two heads" is
   limited to one run, as the decision states.
10. **Cycles.** With content-hash `supersedes` references, a cycle cannot be built from real objects.
    The rule is kept as the decision requires, and its control LN5 runs in a synthetic store that
    resolves references without rehashing.
11. **Out of scope, unchanged.** The owner field of authorization records (admission point 7 and the
    record lint) still compares against `A.owner.id`. DI-1 names only the four host comment forms,
    so I left this unchanged. In the probes D2, D3 and L6, the run stopped at point 7 only because of
    the synthetic configuration's owner.

## Verification

- The changes are textual. Each replacement was applied by a script that requires its old text to
  occur exactly once.
- `DESIGN-v5.5.3.md` keeps its sha256.
- Checked by grep: the new ids TR54-TR64 and LN1-LN8 occur in no earlier `DESIGN*.md` or
  `CHANGES*.md`.
- No implementation was changed, and no control was run.
