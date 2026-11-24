# Three owner decisions after the fourth review (proposals; nothing adopted)

Frozen design: DESIGN-v5.5.3.md (99e9ce3a...3379). Review: review-stage1-r4/review.md (e21cf9d3...eae0).
Q1 needs no design change. Q2 and Q3 change the frozen design if option B is chosen.

## Q1. Ledger additions: which approvals?

Design text (sec. 6.3, "The freeze ledger", "How it changes"): "Every change lands through the
authority-change procedure, with an `oi-authority/1 approve` comment quoting the old and new ledger
blob hashes." N3 (same section) adds: "No append takes effect ... without its own explicit owner
approval comment" `oi-freeze-ledger/1 append ...` in the plan's thread. The authority-change
procedure includes: owner approval comment; an independent review record naming both blobs; a
pull-request merge into main with merged-by = previous owner id (provenance).

- **A (literal, recommended).** Every ledger change needs all of: the `oi-authority/1 approve`
  comment (authority thread), the N3 `oi-freeze-ledger/1 append` comment (plan thread, matching
  plan/round), an independent review record naming both ledger blobs, and a PR merge by the owner.
  No design change. Cost: one review record per ledger addition (including each acceptance landing).
- **B (lighter).** N3 comment plus PR merge by the owner; no `oi-authority/1` comment and no review
  record for ledger changes. Removes the duplication you mentioned, but contradicts the "How it
  changes" sentence, so it is a design change.

Recommendation: A. The two comments are not redundant in what they bind (the authority comment is in
the authority thread and binds the ledger blobs; N3 binds plan and round in the plan thread), and A
needs no amendment.

## Q2 (DI-1). Which owner identity counts for a comment?

Design text (admission point 3; forms): owner comments are those "whose author numeric id is
`A.owner.id`", where A is the authority record governing now. Effects shown by the review: D1 a
former owner's designation stops counting after an owner change; D2 a former owner's withdrawal
not yet in the ledger is ignored, so a withdrawn F can be re-designated; D3 comments the new owner
wrote before becoming owner count; L5/L6 the same for ledger approvals (an approval written by A
before A->B->A counts again).

- **A (keep the letter).** No change; D2, D3, L5, L6 remain as documented residuals.
- **B (in force at creation and now, recommended).** Replace "whose author numeric id is
  `A.owner.id`" by: "whose author numeric id equals the `owner.id` of the authority version in force
  when the comment was created (the latest version merged on `main` before its creation time)".
  Then:
  - a withdrawal, or the revoking half of a supersession, by the owner in force at its creation
    always binds (closes D2; fail-closed);
  - a designation or an approval counts only if its author was the owner at creation **and** is the
    owner of the authority record governing the admission (closes D3; D1 becomes an explicit
    re-designation after an owner change);
  - an approval counts only if no owner change merged between its creation and the merge it
    authorizes (closes L5/L6: an old approval cannot revive when the same id returns).
- **C (in force at creation only).** As B without the "and now" clause: designations by a former
  owner made while owner stay valid (D1 closed the other way). Weaker than B on the principle that a
  former owner retains no authority.

Recommendation: B. It is the reading of your F1 requirement ("a historical owner must not retain
indefinite authority"; "an old approval must not become authority ... merely because the owner id
matches again") and every change in it refuses more, never less.

## Q3 (DI-2). Lineage of a superseding record

Design text (sec. 6.3, record lint): `supersedes` must name a record "of the same kind, schema and
lineage". Lineage is defined only for the configuration (`config_id`). E6: a record superseding a
same-schema record with another `record_id` is accepted.

- **A (recommended).** Lineage is the record's `record_id` (`config_id` for the configuration): a
  superseding record must have the same kind, schema and `record_id` as the record it names. A record
  with no `record_id` cannot supersede or be superseded (record-invalid).
- **B.** Lineage is the record's path prefix in the audit or plan record directory. Weaker: paths are
  chosen by the writer and are not part of the reviewed content.
- **C.** No definition; E6 stays a documented gap.

Recommendation: A. It uses an existing reviewed field and is checkable from the object store alone.

## Effect on the work

Q1 A: implement with the K2 fix (small). Q2 B and Q3 A: a one-paragraph amendment to v5.5.3 each,
reviewed independently before implementation, then implemented and covered by the review's probes
(D1-D3, L5, L6, E6).
