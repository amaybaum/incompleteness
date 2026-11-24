# Independent review: DESIGN-v5.5.10 (owner decisions HS-1 to HS-7, 2026-11-24)

Reviewer: independent, non-author. Review only. No repository write, commit, push, GitHub write,
GraphQL call or CI run. Host facts were checked only against GitHub's published documentation
(docs.github.com, fetched 2026-11-24; extracts under `evidence/`).

Verdict: **REJECT** (two blocking findings, B1 and B2; each has a small textual fix, listed below).
With B1 and B2 fixed as proposed, and nothing else changed, I would expect ACCEPT-WITH-NITS.

## 0. Inputs verified

| Object | sha256 | Result |
|---|---|---|
| DESIGN-v5.5.10.md | fae222cd5caab23cec5a80bfa9d0db083efad8311e3985cd7b553bec87748e0c | matches |
| CHANGES-v5.5.10.md | 942e8c9e93cd24f32ff3ca4d651532bb5d4e683a6b6b07dd88d6fcc3fd586530 | matches |
| CHANGES-v5.5.10-from-v5.5.9.diff | 0feaa2435e28751942576954a5d6443d0140d724e29926d8041d8b2c182b1889 | matches |
| DESIGN-v5.5.9.md (base, adopted) | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | matches |
| coord2-gitrest/FEASIBILITY.md | f1bb95c782e5c11123cba3b2b22c68bce6d7b19a3e088de06ace1596db916b91 | matches |

`diff -u DESIGN-v5.5.9.md DESIGN-v5.5.10.md` regenerated here is byte-identical to the supplied
diff (`cmp`, including the header lines). 21 hunks, 40 removed and 210 added lines, 3152 -> 3322
lines: as the change note states.

## 1. Blocking findings

### B1. Deletion events: v5.5.10 drops a refusal that v5.5.9 prescribes on this host (flag F1)

**v5.5.9 text** (sec. 6.3, freeze ledger, "The residual"): a deleted withdrawal "cannot be detected,
unless the host exposes deletion events for the thread. If it does, any deletion of an owner
comment refuses." Residual-trust bullet: "A deletion is detected only for events already in the
freeze ledger or in a committed snapshot, or if the host reports deletions." TR35: "On a host that
reports deletions: ERROR". When v5.5 introduced this rule, whether the host exposes deletion events
was listed as unknown (CHANGES-v5.5.md sec. 4).

**Host fact (verified against the published schema, `evidence/graphql-schema-extract.txt`).**
GitHub's GraphQL schema has `type CommentDeletedEvent` (`actor`, `createdAt`, `databaseId`,
`deletedCommentAuthor: Actor`, `id`) and lists it in `union IssueTimelineItems` (with the item type
`COMMENT_DELETED_EVENT`). So the host does expose deletion events for an issue thread, and v5.5.9's
condition "the host exposes deletion events for the thread" holds on the host in use. The S1 code
already carries the hook (`authority.py:617`, `deleted = host.deletion_events(...)`, refuse if any);
only the reader returns `None`.

**What v5.5.10 does.** It adds "the tool does not read it under this design ... Until the owner
adopts a rule from it, the tool reads no deletion events", appends to TR35 "so on the host in use
the first branch applies", deletes "or if the host reports deletions" from the residual-trust
bullet, and confines GraphQL to the edit history ("the only fact the tool reads through the host's
GraphQL API"; TR85 makes any other GraphQL query a lint FAIL). On GitHub, an owner comment deleted
and reported by a `CommentDeletedEvent` refuses under v5.5.9 and is admitted under v5.5.10. That
is a removed refusal, against the guiding principle and against the status bullet's own claim that
"no control expectation is relaxed".

**Why the draft's reason does not carry.** The draft defers because the events' completeness and
author identification are "not established". Completeness matters only for a claim that no
deletion happened; v5.5.9's rule uses an observed event as a refusal, which is monotone: reading the
events can add refusals and can never admit anything v5.5.10 would refuse. An event whose deleted
comment's author cannot be identified by numeric id can be made to refuse (fail closed), which is
what HS-3's spirit and v5.5.9's "any deletion of an owner comment refuses" both point to. Nor do
the decisions require the deferral: HS-2 restricts GraphQL to information unavailable through REST,
and deletion events are unavailable through REST (FEASIBILITY sec. 2; the draft itself says so), so
HS-2 permits reading them; HS-6 asks for a separate investigation and for no unsupported claim of
complete coverage, and neither is touched by refusing on reported events. The confinement "GraphQL
for the edit history only" is narrower than HS-2.

**Smallest fix (faithful to v5.5.9 and HS-2/HS-6).**
1. In "What the host exposes (HS-6)", replace "and the tool does not read it under this design" and
   "Until the owner adopts a rule from it, the tool reads no deletion events, and no complete
   historical coverage of a thread is claimed." by: the tool reads the thread's
   `CommentDeletedEvent` items through GraphQL (the issue's timeline items of that type, every page,
   with the failure list of the edit-history read applied: request failure, error, rate limit,
   partial result, missing fields); any event whose deleted comment's author is, or cannot be shown
   not to be, an owner id refuses (the author's numeric id is read from `deletedCommentAuthor` as a
   `User`; an absent, null or non-`User` author refuses); the absence of events establishes
   nothing, the residual stands, and no complete historical coverage is claimed.
2. Edit history paragraph: "The edit history is the only fact ..." -> "The edit history and the
   thread's deletion events are the only facts ...". TR85: allow that second query.
3. Residual-trust bullet: restore "or if the host reports deletions" (or "or reported by the
   host's deletion events (HS-6)").
4. TR35: drop the appended sentence; add a TR row (next free id, TR86) for a reported deletion of an
   owner comment, and of a comment with an unidentifiable author: ERROR; and an HV row checking that
   a deletion on the test issue is reported (needs the separately authorized write).
5. Sec. 15 item 9: the investigation concerns completeness (whether the residual can be narrowed),
   not whether to read the events.

**Alternative.** If the owner intends HS-6 to suspend v5.5.9's deletion rule until the
investigation, that is a relaxation which only the owner can make; the design must then cite it as
an owner decision with its wording, and the status bullet's "no control expectation is relaxed"
must go. The writer could not make that choice, and flagged it correctly. Note for the owner: the
v5.5.9 rule refuses permanently once any owner comment of an authorized thread has ever been
deleted, which may matter for #1169; that is a consequence of the adopted rule, not of the fix.

### B2. An edit signal with no revision returned is not refused (HS-3)

**Counterexample (paper walk of v5.5.10 sec. 6.3, admission point 3).** An owner comment whose
current body carries no form (for example `noted.`); REST `minimized: null`, `updated_at` later than
`created_at`; GraphQL `lastEditedAt` set, `userContentEdits { totalCount: 0, nodes: [] }`.

- "Edited (HS-5)": edited (two signals).
- Bullet 1 (form carried and edited): no form, does not apply.
- Bullet 2 (history ever contained a form): the history is empty, so no.
- Bullet 3 (hidden): no.
- Bullet 4 (edit status cannot be read), as specified by "Edit history (HS-2, HS-3)": the request
  succeeded, the node matched, both fields are present, revisions returned (0) equal `totalCount`
  (0), no revision has a null `diff` or a set `deletedAt`. Not triggered.

The comment is admitted. The host itself reports that the comment was edited and returns none of
its earlier content; if that content was `oi-freeze/1 withdraw ...`, the TR33 guarantee (a
withdrawal edited out refuses) is lost silently. HS-3 requires failing closed "whenever required
edit history is missing ... or unverifiable", and the history is required here for bullet 2. The
same gap exists in the S1 reader (`host.py:335` computes `edited` but `authority.py:127-132` tests
the form only against `edits`), so it is not a regression from S1; it is an incomplete
implementation of HS-3, which this amendment claims to implement. HV5 checks only
"`lastEditedAt` null implies `totalCount` 0", not the converse.

**Smallest fix.** Add to the refusal list of "Edit history (HS-2, HS-3)": "- the comment is edited
in the sense below while no revision is returned (`totalCount` 0)." Add the case to TR79 (new in
this draft, so extending it is not a renumbering): "separately, `lastEditedAt` set, or `updated_at`
different from `created_at`, with `totalCount` 0, on a comment carrying no form: ERROR". Add to HV5:
"and `lastEditedAt` set implies `totalCount` above 0; the comments where an edit signal holds with
`totalCount` 0 are recorded". Liveness note for the owner: if HV5 finds `updated_at` changing
without an edit (for example on pinning, which REST exposes as `pin`), non-form owner comments so
marked would refuse; narrowing the rule to the GraphQL signal alone would then be an owner decision
on HV5's evidence, not a default.

## 2. Nits and open items (not blocking)

- **N1 (F3 wording).** "That binding rests on the collision resistance of ... SHA-1" names a
  property SHA-1 is known not to have. The binding needs second-preimage resistance against objects
  the host already holds, plus the host's refusal of objects that collision-detecting SHA-1 flags
  (which is what stops a chosen collision pair being planted on the host). Suggested: "rests on
  SHA-1's second-preimage resistance, and on the host's and git's refusal of objects that
  collision-detecting SHA-1 flags". No change of substance.
- **N2. Revisions over 100.** GraphQL connections take `first`/`last` of 1-100 (documented,
  `evidence/gql-limits-extract.txt`). The design does not say that `userContentEdits` is paginated;
  a comment with more than 100 revisions therefore refuses through "fewer revisions than
  `totalCount`". Fail-closed; state either pagination or the refusal.
- **N3. `nodes(ids:)` cap.** The documented limits page states the connection bound and a 500,000
  node limit, and no cap for `nodes(ids:)` (0 occurrences; extract). The cap of 100 remains
  unverified, as the draft says; HV3 covers it, and an over-cap batch errors and refuses.
- **N4. `main` moving after checkout.** The anchor is read from REST after the CI checkout; if
  `main` advanced meanwhile, the anchor is absent and the admission refuses ("no object is fetched
  on demand"). Fail-closed, but a liveness trap; the workflow (not the reader) can fetch the exact
  anchor id by full id before admission, and the objects are still hash-verified. Worth a sentence
  in sec. 7.2 or an open item.
- **N5. Entry types for `A`, the ledger, review records and snapshots.** v5.5.9 read these through
  the host's contents API, which is documented to follow a symlink to a regular file in the
  repository; the local reader reads a symlink's blob as the link text. The "Entries" bullet says
  only that the reader changes nothing about accepted entries, and K7's non-regular-entry rule
  covers only `tools/ledger_coverage/` at `head_sha`. State that these records are read only from
  regular-file entries (`100644`/`100755`) and that any other entry refuses. Stricter, not weaker.
- **N6. Alternates.** Sec. 7.2 bars alternates for native clones; the trust-root store is silent.
  Integrity is unaffected (every object is hash-verified), so this is only hermeticity; optional.
- **N7. "Item 7" label.** Sec. 15 item 6 is labelled "**Item 7.**" (P's item 7), and sec. 15 now has
  its own item 7. The new cross-references say "sec. 15 item 9", which is unambiguous; cosmetic.
- **N8. HV for deletions.** If B1's fix is taken, add an HV row (write) for a reported deletion.

## 3. Per-decision map

| Decision | Implemented by (v5.5.10) | Exactly / more / less |
|---|---|---|
| HS-1 git for history, REST for metadata | consumer bullet (sec. 5); integrity errors; trust-root lead and points 1-3; "Repository history from a verified local object store"; merge-record bullet (REST PR record); admission 2 (REST listing); admission 9; snapshot (`main`'s id); residual trust (REST/GraphQL split, git object ids); sec. 7.2 host-run classes; TR25, TR76, TR77, TR83, TR84 | exact |
| HS-2 option G; keep edit-history requirements; GraphQL only for what REST lacks | admission 3: the four v5.5.9 bullets kept verbatim; "Edit history" (batched `nodes(ids:)`); hidden state from REST `minimized`; TR81, TR85 | edit-history rules kept; GraphQL confinement is **narrower** than HS-2 (excludes deletion events, which REST lacks), see B1 |
| HS-3 fail closed on missing/unreadable/incomplete/unverifiable history | "Edit history" refusal list; no revision skipped; TR78-TR80 | **less**: an edit signal with no revision returned is not refused (B2) |
| HS-4 reject shallow/partial unless completeness established; ignore replace/graft | "Each object verified", "Replace and graft mechanisms ignored", "chain reaches a root", "Shallow and partial stores refused", "Anchors absent", "Other reads"; sec. 7.2 `--filter`; TR71-TR75, TR77 | exact; "no other means of establishing completeness" is within the decision's permission; extension to every git read is F6 |
| HS-5 `updated_at` never proof of no edit | "whatever its `updated_at`"; "Edited (HS-5)"; TR82 | exact |
| HS-6 investigate deletions separately; exposed vs unreconstructible; no unsupported coverage claim | "What the host exposes (HS-6)"; residual-trust bullet; sec. 15 item 9; TR35 | distinction and no-claim: exact; but it also **stops reading** events v5.5.9 required, which HS-6 does not order (B1) |
| HS-7 budget and GraphQL behaviour measured in a separately authorized CI stage | sec. 10.5 HV1-HV10; sec. 15 items 7-8; S13 gate | exact (see sec. 6 below) |

## 4. Row comparison (reproduced independently)

Script `rowcmp.py` (here): every table row whose first cell is an identifier, in both files,
compared as text. Base 323 keyed rows, draft 348; duplicate keys (table headers such as `Id`,
`LIST`, `TABLE`, and `Z9h`) are the same 9 in both. Also compared as sorted multisets of all such
lines (`comm -3`).

- removed: none;
- changed: **TR25, TR35, S13** (only);
- added: TR71-TR85, HV1-HV10 (and the sec. 10.5 header row);
- every other TR, X, S, G, K, R, WB, Z, Y, N, LN, RT and HV-free row: byte-identical.

This equals the change note's statement. Assessment of the three changed rows:

- **TR25**: outcome unchanged (refused); source re-named. Not weaker.
- **TR35**: text kept, sentence appended that pins the first branch on the host in use. Weaker in
  effect on GitHub (B1).
- **S13**: TR1-TR70 -> TR1-TR85, plus the real-host gate. Stricter.

Rows whose text is unchanged but whose source moves (TR11, TR19, TR21, TR23, TR26-TR29, TR31,
TR33, TR34, TR40-TR42, TR47-TR53, TR62, TR63, TR67): I checked each against the new source rules;
each keeps its outcome, with TR33 subject to B2 when the host omits the revisions.

## 5. Trust root and integrity of the local store (question 3)

Sound, apart from N1's wording:

- **Anchors** are host reports only (`main`'s id once per admission, `head_sha`); no ref of the store
  is read. Every object is requested by id and its id recomputed; parents and trees are parsed from
  verified content, so chain, tree entries and blobs are bound to the anchors by the Merkle
  structure. A corrupted or substituted object refuses (TR76; the feasibility controls showed
  `git cat-file -p` printing a corrupted loose blob that the reader refuses).
- **Replace refs / grafts / commit-graph**: ignored by construction (raw content parsed; replacement
  disabled); TR71-TR73 expect equality with the clean store, which distinguishes "ignored" from
  "refused by hash mismatch". A replace ref left active would be caught by the hash check anyway.
- **Root reachability**: required; a missing parent refuses; a `shallow` file refuses by marker even
  when complete, which is stricter than needed (completeness is already enforced by reaching a root)
  but is what HS-4 orders.
- **Partial**: refused by markers; even a missed marker would only allow a lazy fetch whose object
  is still hash-verified, so integrity does not depend on marker detection.
- **Partial or short CI checkout**: `actions/checkout`'s default depth 1 yields a shallow store and
  refuses; a missing anchor refuses (N4). No counterexample admits a store that lacks an object.
- **Non-regular entries**: unchanged at K7; N5 for the other records.
- **SHA-1**: I could not construct a substitution that does not need a SHA-1 second preimage of an
  object the host holds, or a collision pair accepted by the host's collision detection.

## 6. REST and GraphQL rules (question 4): verified vs inferred

Verified against published docs (extracts in `evidence/`):

- `UserContentEdit` has `deletedAt: DateTime`, `deletedBy: Actor`, `diff: String` (nullable), and
  `diff` is described as "A summary of the changes for this edit" (so F4 is a real risk, and
  HV4/HV8 are needed before any real-host claim).
- `IssueComment` has `lastEditedAt: DateTime` (nullable), `userContentEdits` (connection),
  `isMinimized: Boolean!`.
- `Query.nodes(ids: [ID!]!): [Node]!`; no documented cap on `ids`; connections take `first`/`last`
  1-100; 500,000-node limit; 10-second timeout.
- `CommentDeletedEvent` exists, is an `IssueTimelineItems` member, carries `deletedCommentAuthor:
  Actor` (an `Actor`, so the numeric id needs a `User` fragment; I did not verify that it is
  populated).
- REST issue comment: `minimized` is `null` or an object `{reason}` ("Minimized Issue Comment"); it
  is **not** in the documented `required` list (`id, node_id, html_url, issue_url, user, url,
  created_at, updated_at`), so an absent field is possible by the schema; v5.5.10 refuses on it
  (correct, fail-closed; HV7 measures liveness).

Inferred, not verified: that `diff` is the full revision body; that a revision deleted from a
history keeps a node with null `diff`/set `deletedAt`; that REST `node_id` equals the GraphQL `id`
for old comments (legacy vs new global id formats; HV3 checks "the same node id", and a mismatch
refuses); that `updated_at` changes on every edit (not relied on).

Fail-closed review of each rule:

- REST listing: page error, count mismatch, repeated id (TR83) refuse. A deletion lowers listing
  and count together and is not seen (stated).
- Merge record: none or more than one PR with that merge commit into `main` refuses (TR84); this
  is stricter than v5.5.9's unspecified matching and also covers ledger versions, which v5.5.9
  already routed through the same procedure.
- GraphQL edit history: every listed failure refuses; no fallback to REST (TR80). Gap: B2. Minor:
  N2.
- Hidden state: only `null` passes. The omission case (a minimized comment reported as `null`) is
  not detectable by any rule and is gated by HV10.

## 7. Flag verdicts

- **F1** (deletion events): v5.5.9 does require reading them where the host exposes them, and the
  published GraphQL schema shows GitHub does; deferral is a weakening. **Blocking (B1)**; minimal
  faithful text in B1, or an explicit owner relaxation.
- **F2** (hidden state from REST `minimized` only): accepted. HS-2 orders it; REST `minimized` is
  documented (null or object). The omission risk equals trusting GraphQL `isMinimized` and is a
  host attestation already in the residual list; HV10 gates it.
- **F3** (SHA-1 residual): accepted; not a new assumption of substance, it makes explicit what
  v5.5.9 left implicit. Wording per N1.
- **F4** (`diff` as full content): accepted with HV4/HV8 as the gate; the documented description
  ("A summary of the changes") makes this a live question, correctly routed back to the owner on
  failure with no rule relaxed.
- **F5** (revisions omitted from `totalCount`): accepted; identical exposure in v5.5.9; HV9 tests it.
  Related but distinct: B2 (a revision count of 0 against an edit signal is detectable and must
  refuse).
- **F6** (verified reader for every git read): accepted as consistent with HS-4's unqualified
  wording and harmless to integrity. Owner note: it makes ops A-D and the replay refuse in shallow
  or partial clones, including local partial clones that §A.40 otherwise encourages; narrowing it to
  admission reads would be an owner choice and would not weaken any v5.5.9 guarantee.

## 8. Validation stage (question 7)

Sec. 10.5 is stated as outside this design's adoption and outside the implementation step, under
its own owner authorization; HV8-HV10 are marked "(write)" and need a separately authorized test
issue (sec. 10.5 lead and sec. 15 item 7). Decision rules are fixed, figures measured, not preset;
a failing item returns the design to the owner with no rule relaxed. It gates every real-host
claim: TR5 and TR48 `NOT RUN` on the real host, no result presented for acceptance under sec. 5,
and S13 carries the same gate. Correct. Additions: HV5's converse (B2) and a deletion HV (B1/N8).

## 9. Minimum change, identifiers, register (question 8)

- Every hunk maps to HS-1 to HS-7 or to the version and status lines; nothing unrelated is bundled.
- New identifiers TR71-TR85, HV1-HV10, HS-1 to HS-7, sec. 10.5, sec. 15 items 7-9: word-bounded
  grep over every `*.md` of the design directory finds them only in DESIGN-v5.5.10.md and
  CHANGES-v5.5.10.md; none existed in v5.5.9; nothing renumbered or reused.
- Added lines: capitalized words are only `REST`, `ERROR`, `FAIL`, `CONFIG_UNREVIEWED`, `ACCEPT`,
  `CHANGES` (acronyms, outcome codes, a verdict label and a file name); no revision-history or
  reader-instruction phrases found.

## 10. Files

- `review.md` (this file), `rowcmp.py` (row comparison),
  `evidence/graphql-schema-extract.txt`, `evidence/rest-minimized-extract.txt`,
  `evidence/gql-limits-extract.txt` (each records its source URL and the sha256 of the fetched page).
- `MANIFEST.sha256` covers them.
