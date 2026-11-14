# Notes on the TUNE-1 landing plan (#1236)

Writer's notes for `LANDING-PLAN.md`: what was read, what was decided, and what is left to the owner.
Paper-only. No computation on any OI rule, commit, push or post was made in writing the plan.

## Sources read

**Owner and governance records, read first-hand through the host API.**
- #1236: all twelve comments, including c.6846408321 and c.6846442383 (Step 3A authorization and
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
  format precedent; for r2, at `3859c3ef`, the Landing section of `STATUS-LADDER.md` and the gate rows
  of `LANDING-PLAN.md`, which carry the corrections of `REVIEW-BELL-PLAN-r1.md` and
  `CONFIRM-BELL-PLAN-r2.md`.
- For r2: `REVIEW-TUNE1-PLAN-r1.md` in this directory, in full; OA1:106–107, :603; OA3:323–326,
  :415–416; REC-1 r9's count of lines citing `3A:`.
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

Each question gives the writer's recommendation and, beside it, the recommendation of the independent
review (`REVIEW-TUNE1-PLAN-r1.md`, "Owner questions OQ-1 to OQ-11").

- **OQ-1. Step 3A's non-author review; substantive result.** `TUNE-1-STEP3A-REVIEW.md` names its
  reviewer only as "Independent internal review (same model family)" (REVIEW:6); the r2 recheck nits
  were "applied by the coordinator" (3A:1106), and the r3 review and its confirmation name no reviewer.
  The record does not establish which agent wrote r1–r3 and which reviewed them; the sourcing review
  states non-authorship explicitly. Does Step 3A meet #1283 item 8's "independent non-author review",
  and its "substantive, nonredundant result" (productivity "gem, BORDERLINE"; part of the stop
  finding restates Step 2)?
  - *Writer:* the owner decides on a recorded attestation, quoted in the note, of which agent wrote
    r1–r3 and which reviewed them. If none can be given, a focused non-author confirmation of r3
    against its review trail, paper-only, before G2. "Substantive, nonredundant": yes.
  - *Reviewer:* the same. Do not record "yes" on non-authorship without a basis; substantive and
    nonredundant: yes, since F-3A-1 to F-3A-3, the conditional classification, the seven qualifying
    items and T1 with the L4 audit go beyond Step 2's records, and REC-1 and SRC cite 3A as a source.
- **OQ-2. §A.42 item 3 for `TUNE-1-STEP3A-OBJECTS.md`.** Five full ids name working copies that were
  never committed. (a) Abbreviate them to 8 characters at packaging as a recorded substitution in a
  bookkeeping file, as #1265 did; (b) land unchanged under a recorded owner exception.
  - *Writer:* (a), and record `9f7d2612` and `221754fc` as in `LANDING-PLAN.md` §5.5.
  - *Reviewer:* (a), with the old and new blobs in the Step 3A note; the #1265 precedent is direct;
    the package's non-author review checks the substitution byte for byte; record `9f7d2612` and
    `221754fc` as in its S10.
- **OQ-3. TUNE-1 Steps 1–2 and OBS.** The Step 1–2 records landed by #1237 before item 8 was drafted,
  have no status note on `main`, and are not in #1284's batch 1; OBS
  (`observer-interface-obsmu-20261104/`) likewise has no status note. Both TUNE-1 records rest on
  them as [R]. Should they be reconciled in a later batch under #1236?
  - *Writer:* yes, as a later batch under #1236; not a gate for G2.
  - *Reviewer:* yes, a later reconciliation batch under #1236 covering the Step 1–2 records and OBS;
    not a gate for G2; record it as a deferral naming its Issue (§A.45 rule 6); once #1283 is adopted,
    item 8's reconciliation clause applies to it.
- **OQ-4. Order of #1284 and the TUNE-1 package.**
  - *Writer:* #1284 first, as a hard precondition of the notes as drafted (`LANDING-PLAN.md` §1, G1);
    if the owner orders the package first, the notes are rewritten per §3.4 and reviewed before G2.
  - *Reviewer:* the same.
- **OQ-5. REC-1 rows.** Accept closure of SRC's two REC-1 support rows by narrowing in the status
  note, or require REC-1 (#1268) to land first.
  - *Writer:* narrowing, with the C9 anchor on OA1:106–107, :522, :603.
  - *Reviewer:* the same; do not require REC-1 to land first.
- **OQ-6. PR descriptions.** #1267's body still reads "Result (not yet reviewed by ChatGPT)" and
  "Next step: ChatGPT review at the exact head"; #1272's ends with "Next: a focused confirmation of r2,
  then ChatGPT review".
  - *Writer:* append a current status to each, without rewriting the history, as was done for #1273
    and #1278.
  - *Reviewer:* append a dated current-status paragraph without rewriting history, at packaging and
    only under owner authorization for host writes; not a landing condition.
- **OQ-7. Planning status.** #1236's planning block and #1147 do not record the two records' review
  state or this plan.
  - *Writer:* update them at G3, after a landing, as §A.45 rule 3 maintenance; earlier updates would
    need an owner decision.
  - *Reviewer:* agree: update only at G3, after landing; no earlier update.
- **OQ-8. Status-note placement for Step 3A.**
  - *Writer:* `TUNE-1-STEP3A-STATUS.md` beside the Step 3A files, rather than a subdirectory.
  - *Reviewer:* agree.
- **OQ-9. Second guidance message.** 3A quotes a second owner guidance message that is on the
  coordinator's relay only (3A:139–150). No classification rests on it.
  - *Writer:* leave it as provenance; the Step 3A note states which passages draw on it (T2(d),
    3A:866; §5 item 5, 3A:921–922; the interference-versus-tables entries).
  - *Reviewer:* agree; have the note state that T2(d) (3A:866) and the seventh-item wording draw on
    it, and that no classification does.
- **OQ-10. This plan directory.**
  - *Writer:* it stays on its branch as a planning record; the status notes move into their record
    directories at packaging and cite neither plan file.
  - *Reviewer:* agree, on the condition that B1 is applied so that no landed note cites it.
- **OQ-11. Mode.**
  - *Writer:* one pull request; merge commits of `8228b3c2` and then `c539a60c`; landing by merge
    commit.
  - *Reviewer:* agree, never squash or rebase; add the existence check for `9f7d2612` at G2.

## Not done

- The independent non-author review of r1 is `REVIEW-TUNE1-PLAN-r1.md` (ACCEPT WITH CHANGES); its
  dispositions are in `RESPONSE-TUNE1-PLAN-r1.md`. ChatGPT's exact-head review follows.
- No CI run; no change to any PR description, Issue, branch or board.
- REC-1 beyond its cited rows and P0's head, NA's `EVIDENCE.md` beyond §4, and the Step 3A review's
  §§0–3 and 6 were not read in full.
- No re-derivation of any result in either record; the grades restate the evidence the records and
  their reviews state.
