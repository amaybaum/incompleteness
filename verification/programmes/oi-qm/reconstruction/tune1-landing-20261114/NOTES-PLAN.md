# Notes on the TUNE-1 landing plan (#1236)

Writer's notes for `LANDING-PLAN.md`: what was read, what was decided, and what is left to the owner.
Paper-only. No computation on any OI rule, commit, push or post was made in writing the plan.

## Sources read

**Owner and governance records, read first-hand through the host API.**
- #1236: all eleven comments, including c.6846408321 and c.6846442383 (Step 3A authorization and
  guidance), c.6847314661 (r3), c.6847882040 (Step 3A kept as draft; header wording left for a status
  note) and c.6873565446 (this plan's authorization, with the owner's acceptance of #1278).
- #1267: body and ChatGPT review 5887947616.
- #1272: body, checkpoint comment c.6855189619 and ChatGPT review 5892912253.
- #1278: body, the relayed non-author review 5897621232 and ChatGPT review 5898054706.
- #1284: body and ChatGPT review 5900793856.
- #1283: body (review trail, R6, C2).
- #1147: body (O-RDY planning status).

**Records, read with `git show <commit>:<path>`.**
- At `8228b3c2`: `TUNE-1-STEP3A-r3.md` in full; `TUNE-1-STEP3A-OBJECTS.md` in full;
  `TUNE-1-STEP3A-REVIEW.md` headings, verdicts, §§4, 5, 7, 8, 9, the recheck head and the r3 review and
  confirmation; `TUNE-1-STEP3A.md` lines 1–8, 425–428, 545–547, 608–611.
- At `c539a60c`: `TUNE-1-SOURCING-r2.md` in full; `OBJECTS.md`, `NOTES-r2.md`, `CONFIRM-r2.md` head and
  tail; `REVIEW-r1.md` §0 and §§8–9.
- At `6e2d1ee8` (#1284): the OA-1, OA-2 and OA-3 status notes in full or in the sections cited; the
  NPS1 and NIS2 notes' support and verification sections; `git diff c3b5f37a 6e2d1ee8` on the OA notes.
- On `main` at `c3b5f37a`: OA-2 r4 lines 96–118, 155–190, 495–610, 740–752; OA-3 r4 lines 1–20,
  120–128, 223–230, 294–300, 383–416, 455–476, 720–730, 801, 809–825; OA-1 r5 D1–D8 headings and lines
  520–524, 554–566, 650–658; `REVIEW-OA-2.md`:20–45; `DELTA-REVIEW-OA-3-r3.md` and `-r4.md` edit lists;
  `oa-1-20261112/OBJECTS.md` and #1265's commit `739595fa` (the substitution precedent).
- At `d8b74527`: NA `ASSESSMENT.md` by search for TUNE-1, #1272, O-RDY, ready and verdict lines;
  `EVIDENCE.md` §4 head.
- At REC-1 `9f7d2612` and `3a3aa146`: `REC-1-r7.md` lines 1–30 and 205–226; the C-rows of `REC-1-r9.md`;
  `REC-1-P0-r3.md` head and section list.
- At `ed61696d` (#1285): `LANDING-PLAN.md`, `STATUS-LADDER.md` and `NOTES-PLAN.md` in full, as the
  format precedent.
- At `f57e576a` (#1283): the §A.46 diff from `c3b5f37a`.

**Checks of identity.** All input branch heads equal the heads in the brief (`git ls-remote`); `main`
is `c3b5f37a`. Blob ids and SHA-256 values in `LANDING-PLAN.md` §5 were computed from the objects; for
3A they equal the "committed" columns of `TUNE-1-STEP3A-OBJECTS.md`, and for SRC the reviewed-sha256
column of `OBJECTS.md` for every file unchanged by the nit. `papers/Main.md`, `papers/SM.md` and the
TUNE-1 Step 1–2 directory are byte-identical at `080cd2be`, `62bdc2cf` and `c3b5f37a`. OA-1 r5 and
OA-3 r4 are the same blobs at `2d064a71` and `c3b5f37a`; OA-2 r4 differs on lines 65 and 958 only.
Reachability of the five full working-copy ids in `TUNE-1-STEP3A-OBJECTS.md` was checked with
`git log --all --find-object`: none is reachable from any ref. Searches of `main` for `#1267`, `#1272`,
`TUNE-1-STEP3A` and `tune-1-sourcing` found no incoming reference; searches of both input diffs for
#1274, #1285 and their paths found none.

## Decisions taken in the plan

1. **Order.** #1283 adoption first; #1284 recommended next, so that the status notes cite the OA grades
   on `main`; then one TUNE-1 package with Step 3A before the sourcing unit (`LANDING-PLAN.md` §1).
   #1274 and #1285 are not upstream; REC-1 and #1278 are downstream.
2. **One package, two records, both whole and byte-identical.** Both are small, every review cites
   their earlier revisions by line, and the sourcing unit cites Step 3A as support.
3. **Status-note names.** Step 3A's note is `TUNE-1-STEP3A-STATUS.md`, because its directory also holds
   the Step 1–2 records, which the note does not cover. The sourcing unit's note is `STATUS.md` in its
   own directory.
4. **REC-1 rows narrowed, not landed.** SRC uses REC-1 r7 as support off `main` in two rows (C6, C9).
   Each is narrowed in `STATUS-SOURCING.md` to the content on `main` (OA1:563–564; NPS1:85) with the REC
   wording as context; no SRC verdict changes.
5. **OA grades.** Each OA statement the records use is graded as #1284 grades it. None is
   known-invalid. Two cited OA-3 ranges contain one line each that #1284 grades exploratory (OA3:323,
   :415); neither carries a TUNE-1 conclusion, and the notes say so.
6. **Two gaps.** Gap S (no specified member) and Gap P (O-RDY) are stated side by side with their scope,
   kind, closing evidence and accountable Issue; L5.4 is recorded as a third, mathematical, open item.
   #1278 is cited for Gap P with its scope: it concerns the binary SM ring and leaves Gap P open for
   TC-A.
7. **Known-invalid in the review trails.** Step 3A r1:546 (C-POS-1 "passes T1") is graded known-invalid
   under T1's own definition, as the Bell precedent grades r1 statements a review shows false. The
   other r1 corrections of both records are recorded as overstatements, not refutations.
8. **Definitions.** The status notes use #1284's one-line definitions of "partially verified" and
   "exploratory", and the Bell precedent's definitions of "independently verified" and
   "known-invalid".
9. **No full id of a missing object** is written in these files: the five working-copy ids are given by
   their first eight characters only.

## Open owner questions

- **OQ-1. Step 3A's non-author review.** `TUNE-1-STEP3A-REVIEW.md` names its reviewer "Independent
  internal review (same model family)" and does not state non-authorship in those words; the sourcing
  review states it explicitly. Does it meet #1283 item 8's "independent non-author review", or does
  Step 3A need a further non-author review? Related: Step 3A's productivity verdict is "gem,
  BORDERLINE", and part of its stop-condition finding restates Step 2; does it meet item 8's
  "substantive, nonredundant result"? Recommendation: yes on both, recorded as the owner's finding.
- **OQ-2. §A.42 item 3 for `TUNE-1-STEP3A-OBJECTS.md`.** Five full ids name working copies that were
  never committed. (a) Abbreviate them to 8 characters at packaging as a recorded substitution in a
  bookkeeping file, as #1265 did (recommended); (b) land unchanged under a recorded owner exception.
- **OQ-3. TUNE-1 Steps 1–2.** They landed by #1237 before item 8 was drafted, have no status note on
  `main`, and are not in #1284's batch 1. Both records rest on them as [R]. Should they be reconciled in
  a later batch under #1236? This plan does not do it.
- **OQ-4. Order of #1284 and the TUNE-1 package.** Land #1284 first (recommended), or land the package
  first with the OA grades cited as provenance (`LANDING-PLAN.md` §3.4).
- **OQ-5. REC-1 rows.** Accept closure of SRC's two REC-1 support rows by narrowing in the status note
  (recommended), or require REC-1 (#1268) to land first.
- **OQ-6. PR descriptions.** #1267's body still reads "Result (not yet reviewed by ChatGPT)" and
  "Next step: ChatGPT review at the exact head"; #1272's ends with "Next: a focused confirmation of r2,
  then ChatGPT review". Append a current status to each, without rewriting the history, as was done for
  #1273 and #1278.
- **OQ-7. Planning status.** #1236's planning block and #1147 do not record the two records' review
  state or this plan. G3 updates them after a landing; earlier updates would need an owner decision
  (§A.45 rule 3 maintenance).
- **OQ-8. Status-note placement for Step 3A.** `TUNE-1-STEP3A-STATUS.md` beside the Step 3A files
  (recommended), or a subdirectory for Step 3A.
- **OQ-9. Second guidance message.** 3A quotes a second owner guidance message that is on the
  coordinator's relay only (3A:139–150). No classification rests on it. Record it on #1236, or leave it
  as provenance (recommended).
- **OQ-10. This plan directory.** The status notes move into their record directories at packaging;
  this directory stays on its branch as a planning record (recommended), or lands as provenance.
- **OQ-11. Mode.** One pull request; merge commits of `8228b3c2` and `c539a60c`; landing by merge
  commit (recommended).

## Not done

- No review of the plan; the owner's authorization provides for one independent non-author review,
  then ChatGPT's exact-head review.
- No CI run; no change to any PR description, Issue, branch or board.
- REC-1 beyond its cited rows and P0's head, NA's `EVIDENCE.md` beyond §4, and the Step 3A review's
  §§0–3 and 6 were not read in full.
- No re-derivation of any result in either record; the grades restate the evidence the records and
  their reviews state.
