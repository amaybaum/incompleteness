ACCEPT

# Focused confirmation review of QUEUE-PROPOSAL-r2

This review is read-only and paper-only. `QUEUE-PROPOSAL-r2.md` and `RESPONSE-QUEUE-r1.md` were confirmed
byte-identical to their copies on PR #1292 at `fd937e57`. `diff QUEUE-PROPOSAL-r1.md
QUEUE-PROPOSAL-r2.md` was read in full. Owner records were read through the GitHub API on 2026-11-14,
and the QB5(a) preregistration was read at `8dd0de90`. No other file was written, no computation was
run, and nothing was posted or relabelled.

## The coordinator's five checks

**1. RO-2 (QB5(a)): confirmed.**
- **Freeze and execution.** RO-2 quotes:
  - the freeze at `8dd0de90` (#873 comment 6872998421), with its "Execution is not authorized …"
    sentence;
  - the latest record (#873 comment 6875553420, 09:57:14Z): "stays frozen at `8dd0de90`, and its
    execution is not authorized".
- **Writer.** RO-2 states "**No designated writer is recorded for execution.**". It cites the only
  writer designation on #873, comment 6859687612, which is for unit 1. That matches the 12 #873 comments
  this reviewer read.
- **Outcome classes.** Each of (A), (B) and (C) is stated. The wording matches `G3-QB5A-PREREG-r4.md`
  at `8dd0de90`:
  - §8.3 item 3: "surviving" means Admissible or Undetermined;
  - §8.3 item 4: the robustness rule;
  - §8.4: the headline is (C) unless every cell agrees;
  - §1.1: the verdict is conditional on Reading G, case β and N5-G;
  - §12: the productivity test, where a restated baseline is a coherence check;
  - X-2 (`c3b5f37a`): the snapshot check.

  The two earlier units each returned (C), and the cited comments 6865179466 and 6872004336 say so.
- **Readiness and authorization are kept apart.**
  - "Decisive" is removed.
  - The #873 "ready" is labelled as the Issue's readiness, "no row records the readiness of QB5(a)
    execution".
  - §3.3 says "readiness is not authorization (§A.45 rule 3)".
  - No passage presents readiness as permission to start.

**2. RO-1 and RO-2: confirmed.**
- §3.1 says "The evidence therefore gives no order between RO-1 and RO-2 … the choice between them is
  the owner's".
- §3.2 opens with "RO-1 and RO-2 (owner's choice; no default order)".
- Owner question 3 is restated to match.

**3. Ranking criteria: confirmed.**
- **The owner's guidance.** #914 comment 6879221928 (`amaybaum`, 2026-11-14T14:55:05Z) was read
  through the API. The quotation in r2's header is verbatim. §3.1 takes the per-move requirements from
  it, and the emphasis from comment 6878200172 as "not a predetermined ranking".
- **The drafter's criteria.** The three comparison criteria are labelled "the drafter's own", from the
  coordinator's brief and given no order by any owner record.
- **Reasons per move.** Each move gives its own reason for outranking the moves below it.
- **"Startable".** It is replaced as asked.

**4. Ledger r5: confirmed.**
- The inputs cite `REVIEW-r5.md` (ACCEPT) and #914 comment 6879158095, verbatim ("Yes, I accept ledger
  r5"), at `de29ccd8`. They also quote the acceptance's scope.
- LC-0 is removed, and the remaining identifiers are not renumbered.
- Part 2's order and its authorization paragraph are adjusted.
- Treating LC-1 and LC-7, a revision of an accepted record, as an owner question is a justified
  narrowing, since the acceptance "authorizes nothing further".

**5. Other dispositions: confirmed.**
- **N1–N8.**
  - N3: #1074 closed 2026-11-03T16:49:08Z, `completed`, after comment 6600178826.
  - N5: `papers/Introduction.md`:179 cites "[Main §3.3; Substratum §3.2]".
  - N7: the O-IF-SELECT authorization quote matches the #914 body.
  - N4: the MC-5 table now has six columns in its header and in every row.
  - N1, N2, N6 and N8 are applied as described.
- **Scope of the changes.** Nothing else changed:
  - the header and inputs;
  - D2 and the MC-5 header in Part 1;
  - LC-0 and the order and authorization paragraphs in Part 2;
  - §3.0's gravity and emphasis lines, §3.1, the RO-1 to RO-6 reasons and needs, §3.3's closing
    paragraph, owner questions 2, 3 and 5, and the off-`main` table in Part 3.
- **Separation and planning attributes.**
  - The three parts stay separate.
  - The five §3.3 planning proposals are unchanged and still marked "(proposal)".
  - No manuscript wording, tier or queue item changes.
  - Nothing promotes QCD or another downstream branch.

## Optional nit

RO-2's "Why it ranks with RO-1" says its start needs "only an authorization and a writer". Its "Needed
before it can start" line adds the conflicting-writer check, so that line is the complete statement.
The earlier sentence can say "an authorization, a writer and the conflicting-writer check". This does
not affect acceptance.
