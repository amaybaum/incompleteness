# Response to REVIEW-QUEUE-r1

**UNREVIEWED.** This file gives the disposition of each finding of `REVIEW-QUEUE-r1.md` (ACCEPT WITH
CHANGES) and of the coordinator's four items, as applied in `QUEUE-PROPOSAL-r2.md`.
`QUEUE-PROPOSAL-r1.md` is left unchanged. The work was read-only and paper-only. Nothing was
committed, pushed or posted. No manuscript wording, tier, readiness, authorization or queue item
changes. "r2 §n" means a section of `QUEUE-PROPOSAL-r2.md`.

## Should-fix

**S1. RO-2 needs more than an owner authorization.** Applied.
- r1's sentences are replaced, and none of them survives in r2:
  - "whose start needs nothing but an owner authorization";
  - "by its designated writer";
  - "Nothing else is recorded as missing".
- r2 §3.2 RO-2, "Needed before it can start", reads: a recorded owner execution authorization on #873,
  a designated writer, and a check that no other active writer works on the same branch or question
  (§A.45 rule 3). It adds the preregistration's own check X-2: whether `main` has moved from its
  source snapshot `c3b5f37a`.
- RO-2 also states "**No designated writer is recorded for execution.**" It cites #873 comment
  6859687612 as the only writer designation, which is for unit 1.
- The r2 §3.1 table has a column "Still needed under §A.45 rule 3" for every move.

**S2. "Decisive" overstates QB5(a).** Applied. The word is removed from RO-2.
- **The rule.** r2 §3.1 and §3.2 RO-2 use the review's wording: "a frozen, independently reviewed
  decision rule with green controls, whose verdict is one of (A), (B) or (C), with (C) the residual
  class".
- **Each outcome.** RO-2 now states what (A), (B) and (C) would show, from `G3-QB5A-PREREG-r4.md`
  §8.3–§8.4 at `8dd0de90`, read through the API:
  - (C) arises when both kinds of formalization remain, when neither does, or when an undetermined
    item decides;
  - it also arises from robustness (§8.3 item 4) and from disagreement across the grid (§8.4).
- **What no outcome shows.** RO-2 lists this:
  - every verdict holds only on Reading G, case β and N5-G;
  - conclusions are relative to the frozen list (OQ-2);
  - the audit is no independent physical verification (OQ-7);
  - "Physical source remains NOT PASSED; G3 remains (C)" (#873 comment 6872277416);
  - no outcome derives the field equation, and any outcome is a consistency result (§A.23);
  - under §12, a table that restates the baseline is a coherence check.
- **Earlier units.** RO-2 notes that units 2(a) and B_G each returned (C) (#873 comments 6865179466
  and 6872004336).
- **Standing among the units.** RO-2 is called the most fully specified move, not the most decisive.

**S3. The ranking criteria have no source.** Applied.
- **The owner's requirement.** r2 §3.1 takes the per-move requirements from #914 comment 6879221928,
  quoted verbatim in the r2 header with author and time. It takes the emphasis from #914 comment
  6878200172, quoted as "not a predetermined ranking".
- **The drafter's criteria.** The three comparison criteria are labelled the drafter's own. They come
  from the coordinator's task brief for r1, and no owner record gives them or their order.
- **RO-1 and RO-2.** They are presented as the owner's choice between reach and specification, with no
  default order (r2 §3.1, and the heading at the start of r2 §3.2).
- **"Startable".** It is replaced by "for which a next unit can be specified". RO-1's "Needed before it
  can start" is unchanged, so r2 does not call it startable.
- **Why each move outranks the others.** Each move in r2 §3.2 now says why it outranks the moves below
  it, as #914 comment 6879221928 requires.

**S4. Ledger r5 is reviewed and accepted.** Applied.
- **The input line.** It now cites `REVIEW-r5.md` (ACCEPT) and the owner's acceptance in #914 comment
  6879158095 (`amaybaum`, 2026-11-14T14:50:47Z), "Yes, I accept ledger r5", at `de29ccd8`. It also
  quotes the acceptance's scope.
- **LC-0.** It is removed. Identifiers are kept, and LC-1 to LC-8 are not renumbered.
- **Part 2's order.** It now starts at LC-1 and LC-7, described as "a ledger revision after the
  accepted r5", and LC-8 follows the naming of accountable Issues.
- **Authorization.** Part 2's authorization paragraph notes that the acceptance "authorizes nothing
  further" (6879158095: it does not "authorize a merge", nor change "tier, readiness or
  authorization"). r1 said LC-0, LC-1 and LC-7 appeared to fall inside the existing scope. r2 makes the
  coverage of a revision of the accepted record (LC-1, LC-7) part of the owner question as well. This
  is a narrowing that follows from S4.
- **Off-`main` table.** It now lists r5 as owner-accepted.

## Nits

- **N1.** Applied. RO-2 cites #873 comment 6875553420 (2026-11-14T09:57:14Z) as the latest record,
  with its words, beside comment 6872998421. §3.0's gravity bullet cites both.
- **N2.** Applied. RO-2 says the "ready" quoted is the readiness of #873 as a whole, and that no row
  records the readiness of QB5(a) execution.
- **N3.** Applied. #1074's closure was confirmed through the API: closed, `completed`,
  2026-11-03T16:49:08Z, after comment 6600178826 (09:37:45Z). Owner question 5 now says that the #873
  body block is the live record, and narrows the question to whether to note the stale pointer under
  §A.45 rule 3's maintenance clause. The RO-2 finding about #1074 is removed from the move itself.
- **N4.** Applied. The MC-5 header has six columns: ID, Passage A, Passage B, Class, What it waits for,
  Mirrors. The F-2 row, which had five cells, is split into passage A and passage B to match.
- **N5.** Applied. `papers/Introduction.md`:179 was checked at `dfeec843` ("[Main §3.3; Substratum
  §3.2]"). The D2 row now reads ":145 and :179 cite [Substratum §3.2]".
- **N6.** Applied. RO-1 has a "What it does not do" item: it adds no prerequisite to #1060, #868,
  #1143 or any other authorized unit, citing #914 comments 6878200172 and 6879221928. The r1 sentence
  "no sector or Bell-set test can be decisive before C is stated" is removed.
- **N7.** Applied. RO-6 quotes O-IF-SELECT's readiness and its authorization ("paper-only bounded
  source assessment completed …; construction remains at selection gate") from the #914 body.
- **N8.** Applied. The guidance's record now exists, #914 comment 6879221928 (`amaybaum`,
  2026-11-14T14:55:05Z), and is quoted verbatim in the r2 header in place of the paraphrase.

## The coordinator's items

1. **RO-2.** The coordinator's four points are met as follows:
   - **What GitHub says.** Frozen at `8dd0de90` (comment 6872998421) and execution not authorized
     (comment 6875553420), both quoted.
   - **The writer.** The missing §A.45 rule 3 element is added: no designated writer is recorded for
     execution.
   - **"Most decisive".** Revisited (S2), with what each of (A), (B) and (C) would and would not show.
   - **Readiness and authorization.** Kept apart. Execution needs the owner's separate, explicit
     authorization and a designated writer (r2 §3.2 RO-2; §3.3, last paragraph).
2. **Ranking criteria.** Sourced from #914 comment 6879221928 (quoted) and comment 6878200172. Where
   r2's criteria go beyond the owner's, they are labelled the drafter's own (S3).
3. **Ledger r5 status.** Every mention is updated (S4). The other occurrences of "r5" in r2 are row
   citations, the RO-5 reference to #1211's unit 1 "r5", and RO-2's "r5" items, all unaffected.
4. **Other findings.** All of S1–S4 and N1–N8 are applied. No finding was declined.

## Unchanged

- Parts 1 and 2 are unchanged except D2 (N5), the MC-5 table (N4) and Part 2's r5 changes (S4).
- The MC order is unchanged, and so are RO-3 to RO-10 and their proposals, apart from added
  "outranks" reasons.
- No tier change is proposed, and nothing promotes QCD or another downstream branch.
