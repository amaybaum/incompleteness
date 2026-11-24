# DESIGN-v5.5.10: changes against DESIGN-v5.5.9

## Input and scope

Inputs, sha256 verified before use (unchanged by this work):

- `DESIGN-v5.5.9.md` (adopted, authoritative): cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9
- `coord2-gitrest/FEASIBILITY.md` (read-only feasibility report): f1bb95c782e5c11123cba3b2b22c68bce6d7b19a3e088de06ace1596db916b91

v5.5.10 is a draft amendment of the adopted v5.5.9 implementing the owner decisions of 2026-11-24
on the tool's host sources, called HS-1 to HS-7 here, and nothing else. It is authoritative only
after an independent review returns ACCEPT and the owner adopts it. Implementation is not
authorized. The work was paper-only: no repository file, commit, push, GitHub write, GraphQL call or
CI run. The S1 tool at `coord2-impl-wt` (443e871f) was read for reference only.

The owner decision, verbatim (owner amaybaum, 2026-11-24, as relayed by the coordinating session;
no comment id held by this writer):

> "Approve drafting v5.5.10 and proceeding to independent design review, with the following decisions:
> 1. Adopt hash-verified local git for repository history and REST for GitHub metadata.
> 2. Select option G. Preserve the existing comment-edit-history requirements. Restrict GraphQL to information unavailable through REST.
> 3. Fail closed whenever required edit history is missing, unreadable, incomplete or unverifiable. Never silently skip an unreadable revision.
> 4. Reject shallow and partial clones unless their completeness for all required objects can be independently established. Ignore replace and graft mechanisms.
> 5. Do not rely on `updated_at` as proof that a comment has never been edited.
> 6. Investigate deleted comments separately. Explicitly distinguish what GitHub exposes from what cannot be reconstructed. Do not claim complete historical coverage without evidence.
> 7. Measure the actual API budget and verify the remaining GraphQL behavior during a separately authorized CI validation stage.
> Implementation is not yet authorized. Submit v5.5.10 for independent review before adoption."
> "The guiding principle: simplify the implementation without weakening the verification guarantees. GraphQL should be a narrow dependency, not the foundation of the tool."

HS-n is decision n. New identifiers: HS-1 to HS-7, TR71-TR85, HV1-HV10, sec. 10.5, sec. 15 items
7-9. Checked by word-bounded grep (`grep -rlwE 'TR7[1-9]|TR8[0-5]|HV([1-9]|10)|HS-[1-7]'`) over
every `*.md` in the design directory and its subdirectories: they occur only in `DESIGN-v5.5.10.md`
and this file. No identifier is renumbered or reused.

## Size

`CHANGES-v5.5.10-from-v5.5.9.diff` (`diff -u DESIGN-v5.5.9.md DESIGN-v5.5.10.md`): 21 hunks, 40 lines
removed, 210 lines added (250 changed lines); 3152 -> 3322 lines. Control rows compared by script
(every table row whose first cell is a control id, in both files): changed TR25, TR35 and the S13
row; none removed; added TR71-TR85 and HV1-HV10. Built by exact, once-only string replacements
(`work-v5510/apply.py`, each replacement asserted to match exactly once).

## Changes (v5.5.9 line numbers)

| # | Hunk (new file) | v5.5.9 lines | Location | Change | Decision |
|---|---|---|---|---|---|
| 1 | `@@ -1,4 +1,4 @@` | 1 | title | "v5.5.9" -> "v5.5.10" | version label |
| 2 | `@@ -7,6 +7,29 @@` | before 10 | Status and authority | new first amendment bullet: scope, sections changed, the seven decisions summarized, "Implementation is not authorized by it" | all (status line) |
| 3 | `@@ -251,6 +274,7 @@` | after 253 | 0.2 table | new row mapping HS-1 to HS-7 to sections and controls | all (traceability) |
| 4 | `@@ -795,7 +819,8 @@` | 798-799 | sec. 5, acceptance predicate, consumer bullet | "from the host API" -> "from the host's REST API and its own full local object store read as trust-root point 2 of sec. 6.3 states (HS-1)"; the five sub-bullets unchanged | HS-1 |
| 5 | `@@ -854,7 +879,7 @@` | 857 | sec. 5, integrity errors | "an unresolvable object" gains "or one that does not hash to its id (sec. 6.3, trust root point 2)" | HS-1, HS-4 |
| 6 | `@@ -1369,22 +1394,59 @@` | 1372-1373 | 6.3, trust root lead | "from the host API" -> "from the host ... from the host's REST API, and from a local git object store each of whose objects is bound by its hash to an id the host reported" | HS-1 |
| 6 | (same hunk) | 1375-1376 | trust root point 1 | the run record is read "from the host's REST API" | HS-1 |
| 6 | (same hunk) | 1380-1384 | trust root point 2 | "through the host API," removed (line rewrapped, otherwise unchanged); new paragraph "Repository history from a verified local object store": anchors (`main`'s id read once per admission from REST, `head_sha`), per-object hash verification, refs never consulted, replace refs, grafts, `shallow` file and commit-graph never applied, chain to a root, ancestry from parsed parents, shallow and partial stores refused by marker with no on-demand fetch, anchors absent refuse, entries unchanged, same reader for all other git reads (integrity error outside admission), the object-id assumption | HS-1, HS-4 |
| 6 | (same hunk) | 1387 | trust root point 3 | "read by the host API at that `head_sha`" -> "read at that `head_sha` from the verified store of point 2" | HS-1 |
| 7 | `@@ -1422,8 +1484,12 @@` | 1425-1426 | authority changes, merge bullet | the merge record is the host's REST pull-request record whose merge commit is the landing commit, merged into `main` of the attested repository; none or more than one refuses; its merge time is the one "Owner at creation" uses. The provenance sentence unchanged | HS-1 |
| 8 | `@@ -1485,19 +1551,32 @@` | after 1486 | freeze ledger, residual | new paragraph "What the host exposes (HS-6)": the REST listing and count cover only existing comments; no REST deletion event type; GraphQL `CommentDeletedEvent` documented, its completeness and author id not established, not read; a deleted comment's id, body and form not reconstructible; open investigation; no complete coverage claimed. The v5.5.9 paragraph is unchanged | HS-6 |
| 8 | (same hunk) | 1492-1494 | admission point 2 | read from the REST listing; the count is the REST issue record's; ids unique; fields listed (id, node id, author numeric id and login, creation time, `updated_at`, body, `minimized`); "a repeated id" refuses | HS-1, HS-2 |
| 8 | (same hunk) | 1497-1500 | admission point 3, lead | the parenthetical source list (REST `updated_at`; GraphQL `lastEditedAt`, `userContentEdits`) replaced by "as stated below"; the four refusal bullets unchanged | HS-2 |
| 9 | `@@ -1505,6 +1584,30 @@` | after 1506 | admission point 3 | new paragraphs: "Edit history" (GraphQL for edit history only; every owner comment whatever its `updated_at`; fields; batches of at most 100 node ids; revision content is `diff`; the refusal list: request failure, error, rate limit, partial result, missing/null/duplicate/foreign/non-comment node, absent fields, `totalCount` above the revisions returned, null or absent `diff`, set `deletedAt`; no revision skipped); "Edited" (unedited only if all three signals say so; any one makes it edited; `updated_at` can add a signal, never remove one); "Hidden state" (REST `minimized`; only `null` is not hidden; object is hidden; absent or other value refuses) | HS-2, HS-3, HS-5 |
| 10 | `@@ -1533,9 +1636,9 @@` | 1536-1538 | admission point 9 | "cannot reach the host API" -> "cannot reach the host's REST or GraphQL API or has no full local object store (point 2)"; rewrapped | HS-1 |
| 11 | `@@ -1543,11 +1646,13 @@` | after 1545; 1548-1550 | admission snapshot | new field: `main`'s commit id as reported; "edit status" spelled out (GraphQL `lastEditedAt`, `totalCount`, sha256 of each revision's content, REST `updated_at`, the edited flag) and "hidden state" (the REST `minimized` value as read) | HS-1, HS-2, HS-5 |
| 12 | `@@ -1570,19 +1675,26 @@` | 1573-1577 | residual trust, first bullet | split by API: REST (run record, `main`'s head id, merge commit, merged-by id and merge time, comment id, author id, creation time, `updated_at`, body, hidden state, listing completeness of existing comments) and GraphQL (edit history and its count); new bullet "Git object ids": file contents and history bound to host-reported ids by hash, resting on SHA-1 collision resistance; the local store not trusted | HS-1, HS-2 |
| 12 | (same hunk) | 1583-1585 | residual trust, deletion bullet | "or if the host reports deletions" -> "the tool reads no deletion events (HS-6)"; adds that a form a deleted comment carried is also a residual | HS-6 |
| 13 | `@@ -1888,7 +2000,8 @@` | 1890-1891 | 7.2, native clones | adds "no `--filter`" and "the clone is refused if shallow or partial, as sec. 6.3 trust root point 2 states" | HS-4 |
| 14 | `@@ -1905,7 +2018,7 @@` | 1908 | 7.2, host-run classes | "the host's API" -> "the host's REST API" | HS-1 |
| 15 | `@@ -2305,7 +2418,7 @@` | 2308 | TR25 | expectation re-sourced (see below) | HS-1 |
| 16 | `@@ -2315,7 +2428,7 @@` | 2318 | TR35 | expectation sentence added (see below) | HS-6 |
| 17 | `@@ -2351,6 +2464,21 @@` | after 2353 | 10.4 table | new rows TR71-TR85, directly after TR70 | HS-1 to HS-5 |
| 18 | `@@ -2374,6 +2502,30 @@` | after 2375 | new sec. 10.5 | real-host validation stage, HV1-HV10 | HS-7 |
| 19 | `@@ -2814,9 +2966,10 @@` | 2817-2819 | sec. 15 item 1 | HS-1 to HS-7 added to the decisions held without comment id; rewrapped | all (provenance) |
| 20 | `@@ -2835,6 +2988,23 @@` | after 2837 | sec. 15 | new items 7 (validation), 8 (host behaviour not yet observed), 9 (deleted-comment investigation) | HS-6, HS-7 |
| 21 | `@@ -3149,4 +3319,4 @@` | 3152 | S13 acceptance | "TR1-TR70" -> "TR1-TR85"; adds "no admission on the real host is claimed before HV1-HV10 pass in the separately authorized stage of sec. 10.5" | HS-7 |

## Changed control expectations

Every other control row is byte-identical to v5.5.9 (checked by script).

- **TR25.** v5.5.9: "refused: only `main` of the attested repository, through the host API |
  trust root point 2". v5.5.10: "refused: only `main` of the attested repository, at the head id
  the host's REST API reports, read from the verified store of point 2 | trust root point 2
  (HS-1)". The outcome (refused) is unchanged; only the source named in it changes.
- **TR35.** v5.5.9's expectation is kept verbatim, and one sentence is added: "The tool reads no
  deletion events until the owner adopts a rule from the investigation of sec. 15 item 9, so on the
  host in use the first branch applies (HS-6)". See flag F1.
- **S13** (acceptance of the implementation step, not a control): TR1-TR70 -> TR1-TR85; the
  real-host claim gated on HV1-HV10.

Expectations unchanged but now read through new sources (no text change): TR11, TR31, TR33, TR34,
TR42, TR47 and TR67 (edit signal and edit contents: GraphQL edit history for every owner comment,
united with the REST `updated_at` signal); TR19, TR31 and TR47, hidden cases (REST `minimized`);
TR21 (REST listing and count); TR23, TR40, TR41 and TR62 (REST merge record); TR26, TR27, TR28,
TR29, TR48-TR53 and TR63 (verified local store).

New controls: TR71 replace ref; TR72 graft; TR73 commit-graph; TR74 shallow; TR75 partial; TR76
corrupt object; TR77 chain not reaching a root, anchors absent; TR78 null or absent `diff`, set
`deletedAt`; TR79 incomplete edit history; TR80 GraphQL failure, error, rate limit, node mismatch;
TR81 unrecognized `minimized`; TR82 `updated_at` as an added signal only (both directions); TR83
duplicate comment id hiding an omission; TR84 merge record not a pull request into `main`; TR85
lint: GraphQL used only for edit history. Real-host stage: HV1-HV10.

## Preserved guarantees

Per guarantee of v5.5.9, why v5.5.10 does not weaken it.

1. **The trust root is outside `A`, the caller and `F` (points 1-4).** The anchors are host
   reports: `main`'s commit id and the run record, both REST. Every byte read from git is bound to
   an anchor by recomputing object ids along commit parents and tree entries, so the local store,
   which the caller or the job could alter, contributes no trust: a substituted or corrupted object
   refuses (TR76), and the store's refs are never read. In v5.5.9 the host served the same content
   under the same ids; the object-id assumption, which v5.5.9 left implicit in "the content of files
   at a commit", is stated in the residual list (flag F3).
2. **"Every change to `A` on `main`" and every freeze-ledger version.** The chain must reach a root,
   parents come only from verified commit content, and replace refs, grafts, the `shallow` file and
   commit-graph files are ignored (TR71-TR73, TR77). A shallow or partial store refuses by its
   marker even when complete (TR74, TR75), and no object is fetched on demand. A store therefore
   cannot hide a version of `A` or of the ledger, which the host API's history listing also could
   not; the feasibility prototype reproduced the REST reader's 60 versions of `AGENTS.md` field by
   field (FEASIBILITY sec. 5).
3. **Execution identity and K7.** The tree listing at `head_sha` is complete because it comes from
   verified tree objects; non-regular entries refuse as before; `head_sha` must lie on `main`'s
   chain. TR28, TR29 and TR48-TR53 are unchanged.
4. **Merge provenance and "in force".** The facts are those v5.5.9 already took from the host
   (merged-by id, merge time), now named as the REST pull-request record, with a refusal for a
   missing or ambiguous record (TR84).
5. **Thread completeness (point 2).** Unchanged, and stricter: ids must be unique (TR83).
6. **Edit history (point 3; A-D2, V4, R-D2).** All four refusal bullets are unchanged. The edit
   history is read for every owner comment, not only for those `updated_at` marks, so `updated_at`
   never filters what is read (HS-5). An edit signal from any source makes a comment edited, so a
   source that misses an edit cannot clear it (TR82). Every way the history can be unreadable or
   incomplete refuses, including a revision with a null `diff`, which closes the S1 reader's silent
   skip (`host.py:332`; TR78-TR80).
7. **Hidden state.** Only an explicit `null` passes; every other value refuses (TR81). The source
   moves from GraphQL `isMinimized` (the S1 reader's choice; v5.5.9 names no source for the hidden
   state) to REST `minimized`, as HS-2 requires. Both are host attestations, which v5.5.9 already
   trusts (flag F2).
8. **Withdrawal integrity (freeze ledger, R-D2).** Unchanged: ledger and snapshot events bind;
   designations must be in the thread. The deletion residual is stated more precisely (flag F1).
9. **Acceptance predicate and consumer.** The consumer repeats the same points from the same kinds
   of source as the tool. No item of the predicate is removed.
10. **Offline replay.** Unchanged in what it decides; its git reads use the verified reader.
11. **Native clones (sec. 7.2).** Stricter: no `--filter`, and shallow or partial clones refused.
12. **Local runs never reach `"chain"`.** Unchanged, and a run without a full local store is added
    to the cases that cannot.
13. **Real-host claim.** Nothing is claimed on the real host until HV1-HV10 pass (sec. 10.5); TR5
    and TR48 stay `NOT RUN` there until then.

## Points where a decision meets an existing guarantee (flagged, not resolved)

- **F1. Deletion events (HS-6 against v5.5.9's conditional rule).** v5.5.9 says a deleted withdrawal
  is undetectable "unless the host exposes deletion events for the thread. If it does, any deletion
  of an owner comment refuses", and TR35 expects ERROR "on a host that reports deletions". The
  host's GraphQL schema documents `CommentDeletedEvent`. If that rule is read as already requiring
  the tool to read those events, then v5.5.10, which reads none pending the investigation HS-6
  orders, weakens it; if it is read as conditional on evidence that the events are complete, it does
  not. v5.5.10 keeps the v5.5.9 sentence and TR35's expectation verbatim, adds that the tool reads no
  deletion events until an owner rule, and removes "or if the host reports deletions" from the
  residual-trust bullet as no longer describing the tool. Which reading governs is for the owner and
  the review. The S1 reader reads no deletion events either (`deletion_events` returns `None`).
- **F2. Hidden state from REST.** HS-2 restricts GraphQL to what REST lacks, and REST has
  `minimized`. Its non-null form is documented only; no minimized comment exists in the repository
  (FEASIBILITY sec. 2). If the host reported `null` for a minimized comment, point 3 could not see
  it. The fail-closed rule cannot cover an omission. HV10 tests it and needs an authorized write.
- **F3. Object-id assumption.** File contents and history are bound to the host's ids by SHA-1 over
  an untrusted store. v5.5.9 trusted the host's API for the content directly. The two are argued
  equivalent (the host and git's transfer apply collision-detecting SHA-1), and the assumption is
  stated as a residual rather than left implicit. A reviewer may judge whether the statement adds a
  trust assumption.
- **F4. Revision content.** v5.5.9 requires "the content of each recorded edit". v5.5.10 takes a
  revision's content to be GraphQL `diff`. If `diff` is not the full content of the revision, the
  requirement cannot be met through GraphQL at all; HV4 and HV8 test this, and failure returns the
  design to the owner. No rule is relaxed in that case.
- **F5. Revisions the host omits.** A revision deleted from an edit history and omitted from
  `totalCount` would be invisible; the same held in v5.5.9. HV9 tests it (needs a write).
- **F6. Scope of HS-4.** The verified reader is applied to every git read the tool makes, including
  ops A-D and the replay, not only to the reads that moved from the host API, because HS-4 ("Ignore
  replace and graft mechanisms") is unqualified and a replace ref in the job's store could otherwise
  alter what op C reads at `X` while its commit and tree ids still check. This is a strengthening;
  the review may judge it beyond the minimum.

## Open items

1. The real-host validation stage (sec. 10.5) needs its own owner authorization; HV8-HV10 need
   writes on a dedicated test issue, authorized separately.
2. The job token's REST and GraphQL budgets (HV1, HV2): measurable only in CI. The documented
   figures (1,000 REST requests and 1,000 GraphQL points per hour per repository for the job token)
   are not used as references.
3. The `nodes(ids:)` batch cap of 100 is from memory, not verified (HV3).
4. Whether `UserContentEdit` has `deletedAt`, and whether `diff` is nullable and is the full
   revision (HV4, HV6, HV8, HV9).
5. Whether every edit changes REST `updated_at`; whether minimizing or pinning does. The tool does
   not rely on it (HS-5); HV5 and HV8 record it.
6. The non-null form of REST `minimized` (HV7, HV10).
7. The deleted-comment investigation (sec. 15 item 9; HS-6), including `CommentDeletedEvent`'s
   fields, completeness and author identification, and F1.
8. The decision records HS-1 to HS-7 are held without comment id (sec. 15 item 1).
9. Implementation of v5.5.10 is not authorized.
