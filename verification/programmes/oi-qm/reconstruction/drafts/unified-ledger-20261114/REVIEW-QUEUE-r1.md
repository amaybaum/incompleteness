ACCEPT WITH CHANGES

# Independent review of QUEUE-PROPOSAL-r1

This review is read-only and paper-only. `QUEUE-PROPOSAL-r1.md` was confirmed byte-identical to its copy
on PR #1292 at `155e60d3`. Manuscript lines were read at `main` `dfeec843`, and planning records were
read through the GitHub API on 2026-11-14. No file other than this review was written. No computation
was run, nothing was posted, and no label or board was touched.

References of the form "Q:n" are lines of `QUEUE-PROPOSAL-r1.md`.

## Summary

- The three parts are kept apart, each names the authorization it would need, and no manuscript text is
  drafted.
- The MC passages and mirrors check out at source, including D8's second mirror at FULL:2896.
- Nothing promotes QCD or a downstream branch.
- S-A indeed has no planning row on GitHub.
- RO-2 needs correcting:
  - the proposal says its start needs "nothing but an owner authorization", but no writer is recorded
    for QB5(a) execution;
  - "decisive" overstates a rule whose outcome classes include the residual class (C);
  - the criteria behind the ranking have no source.
- The proposal still lists ledger r5 as unreviewed, although its review and the owner's acceptance are
  both recorded.

## Should-fix

**S1. RO-2 needs more than an owner authorization to start.** (Q:296, Q:343, Q:348–349)

The proposal says RO-2 is the only unit "whose start needs nothing but an owner authorization", that
execution is "by its designated writer", and that "Nothing else is recorded as missing". §A.45 rule 3
(`AGENTS.md`:1225 onward) requires four things before work starts:
- readiness;
- a recorded owner authorization;
- a designated writer;
- no conflicting writer.

No writer is recorded for QB5(a) execution:
- the only writer designation on #873 is for unit 1 (comment 6859687612: "Claude is the writer, and
  one slot runs alongside the Bell-first units");
- comment 6859060590 says a start "needs an explicit scope/writer/slot authorization under §A.45".

Replace the sentences with: "Needed before it can start: a recorded owner execution authorization on
#873, a designated writer, and a check that no other active writer works on the same branch or
question." Change the matching words at Q:296.

**S2. "Decisive" overstates what QB5(a) can deliver.** (Q:287, Q:295, Q:345)

The frozen rule (`G3-QB5A-PREREG-r4.md` at `8dd0de90`, §8.3) ends in one of three outcomes:
- (A) or (B), when one kind of formalization survives;
- **(C) "otherwise"**, with a stated residual.

The two earlier G3 units each returned (C): #873 comments 6865179466 and 6872004336. What the rule
guarantees is a rule-determined verdict, not a decision of the question.

Restate the claim as: "a frozen, independently reviewed decision rule with green controls, whose
verdict is one of (A), (B) or (C), with (C) the residual class". Keep its comparative standing among
the units at that.

**S3. The ranking criteria and their order have no source.** (Q:281–301, Q:320)

- Q:281 reads "Criteria, in the order given: (1) … (2) … (3)", but no record cited in the proposal gives
  these criteria or their order.
- The relayed guidance says that the emphasis "is not a predetermined ranking" and that the evidence
  decides the order (Q:38–41).
- Ranking RO-1 first "because criterion 1 was given first" (Q:297) therefore lets an unsourced ordering
  do the work that the guidance assigns to the evidence.
- RO-1 is also called the "widest reach among startable units" (Q:320). On the proposal's own account it
  is not startable: its readiness is undetermined, it is not authorized, S-A has no planning row and no
  writer is designated (Q:324–328).

Either cite where the criteria come from, or state that they are the drafter's. Then present RO-1 and
RO-2 as the owner's choice between reach and readiness, without a default order. Q:301 already says
this, and §3.2 should match it. Replace "startable" with "for which a next unit can be specified".

**S4. Ledger r5 is no longer unreviewed.** (Q:11, Q:224, Q:234)

- `REVIEW-r5.md` (ACCEPT) was preserved at `de29ccd8` (committed 14:44Z). That is before the proposal's
  commit `155e60d3` (14:50:14Z).
- The owner accepted r5 on #914 in comment 6879158095 (2026-11-14T14:50:47Z): "Yes, I accept ledger r5".

Update the input line, remove LC-0, and adjust Part 2's proposed order.

## Nits

- **N1. RO-2: cite the latest execution record.** Besides comment 6872998421, cite #873 comment
  6875553420 (2026-11-14T09:57:14Z). It is the latest #873 record: "the QB5(a) preregistration stays
  frozen at `8dd0de90`, and its execution is not authorized".
- **N2. RO-2: say which readiness is quoted.** The "ready" quoted for RO-2 is the readiness of #873 as a
  whole (its body block). It is not a row for QB5(a) execution.
- **N3. Owner question 5.** #1074 was closed on 2026-11-03T16:49:08Z, state_reason `completed`. That is
  after comment 6600178826, which pointed to it. The #873 body block is therefore the live record. Say
  so, and narrow the question accordingly.
- **N4. MC-5 table (Q:185–194).** The header has five columns, but the rows F-22 to D11 have six (a
  passage-B column). Add the column to the header.
- **N5. D2 (Q:173).** `papers/Introduction.md`:179 also cites [Substratum §3.2], as :145 does. Add it to
  the sites.
- **N6. RO-1 (Q:298, Q:321–322).** State that RO-1 adds no prerequisite to #1060, #868 or #1143. The
  sentence "no sector or Bell-set test can be decisive before C is stated" can be read as one, contrary
  to #914 comment 6878200172. §3.0 already says this for already-authorized work.
- **N7. RO-6 (Q:291, Q:399–400).** The #914 body records O-IF-SELECT's authorization as "paper-only",
  alongside "blocked: no qualifying candidate". Quote both.
- **N8. The relayed guidance (Q:38–41).** It is paraphrased. Quote it with author and time once its
  record exists, as was done for audit r4.

## The six checks

1. **Structure.** Met. Parts 1–3 are separate, and each closes with the authorization it needs (Q:212,
   Q:237, Q:430). Every planning change is marked "(proposal)", and §3.3 repeats that none takes effect
   without a recorded owner decision.
2. **MC.**
   - **No manuscript text.** None is drafted. The "Minimal correction" cells name defects, not wording
     (Q:64–65).
   - **Passages and classes.** The paired passages and classes match ledger r5 §F.1 and audit r4 §3,
     where this reviewer checked them at source earlier: F-3, F-17, F-18, F-21, F-24, F-31 to F-36, D1
     and D7–D10.
   - **D8.** `book/ch10-chemistry.md`:88 matches FULL:2896 by exact line, and :86 matches FULL:2894. The
     ledger lists only :2894 (`LEDGER-r5.md` §F.1 D8 row). The claim is correct.
   - **Mirror lines.** All 23 FULL mirror lines the proposal gives were checked by exact line match, and
     all match: 5062, 5253, 5343, 5263, 5265, 5167, 5669–5682, 5655, 5659, 5193, 5615, 5594, 5610, 5714,
     5235, 2886–2888, 5503, 5325, 5620, 5391 and 5341.
   - **Companion papers.** `papers/Medicine.md` and `papers/Bioinformatics.md` exist on `main`, so
     F-34's "to check" note is apt.
3. **RO.** Every move names its obligation and ledger rows, its prerequisites, readiness and
   authorization, its next unit and why it ranks where it does. The exceptions are the writer gap (S1),
   the overstatement of decisiveness (S2) and the unsourced criteria (S3).

   The quoted records were checked at source, and all are accurate:
   - **#873:** body block (Tier High (provisional); Prerequisites none recorded; Readiness ready;
     Authorization not authorized); comments 6872004336, 6872277416, 6872827835, 6872959810,
     6872998421 and 6600178826.
   - **#1169:** body (MECH-1 row; "Claude is paused as a writer"); comments 6714000230, 6714078965,
     6876591512, 6877981234 and 6878199016.
   - **Other Issues:** #868 comment 6874036684; #1007 body; #1060 body; #1063 body; #1143 body and
     comment 6863602000; #1211 body and comment 6742071797; #872 body and comment 6526240419; #914 body
     (O-IF-SELECT) and comments 6877420015 and 6878200172.

   **What GitHub records for QB5(a):**
   - **QB5(a) authorized, paper-only:** comment 6872004336 (2026-11-14T04:53Z) records "QB5 | Authorize
     (a) — the F4-versus-F5 source audit, paper-only", and "may proceed once its decision rule passes
     independent preregistration review".
   - **Final check:** comment 6872959810 (06:15Z) reports ACCEPT FOR FREEZE at `8dd0de90`, with "All
     controls are green".
   - **F designated:** comment 6872998421 (06:18Z) quotes the owner: "I designate 8dd0de90 as F;
     execution needs separate authorization". It adds "Execution is not authorized. No inventory row is
     classified and no source analysis starts until a separate owner authorization is recorded here."
   - **Latest record:** comment 6875553420 (09:57Z) reads "stays frozen at `8dd0de90`, and its execution
     is not authorized".
   - **Later records:** none. #873 has 12 comments, and none authorizes execution.
   - **Branch state:** the #1275 branch head is `14d25977`, which adds only `CONFIRM-QB5A-PREREG-r4b.md`
     after F.
   - **F's full SHA** is `8dd0de905c9a381b9095dd05c01eb00ffdaa0ccf`. The coordinator's `8dc36d55` is an
     unrelated commit, the merge of #922 on 2026-10-25.

   The proposal keeps readiness and authorization apart: it says "execution not authorized" at Q:271,
   Q:287 and Q:336–340. S1 and S2 concern what else RO-2 needs, and how strongly it is described.
4. **No promotion.** Met.
   - RO-7 to RO-10 are kept "below the shared gaps" with no tier or readiness change.
   - §3.3 proposes no change to #1063.
   - #1063's recorded tier (Exploratory) and readiness are quoted correctly.
   - The emphasis is called "not execution order" (Q:299–300).
   - Already authorized Bell, gravity and mechanism work is excluded from gating (Q:260–277).

   S3 is the one place where an ordering is applied without its source.
5. **S-A.** The claim is confirmed.
   - **#1169 body:** no "S-A" occurrence.
   - **#1169 comments:** all 229 were read. S-A is named only in comment 6877981234, as "Kept separate
     from S-A, closure within C", and it has no row in that comment's table.
   - **#914:** among its 76 comments (75 when the proposal was drafted), S-A is named only in comment
     6878200172.

   There is no planning row for S-A, so the proposal to add one (Q:330) is apt.
6. **Sources.**
   - The owner quotations are verbatim.
   - The `AGENTS.md` line references are right: 317, 553, 1209, 1225, 1263 and 1278.
   - The issue states are correct.
   - The exceptions are S3 (unsourced criteria), S4 (stale review state) and the overstatements in S1
     and S2.
