# CONFIRM-QB5A-PREREG-r4b: final edit check of G3 QB5(a) r4 at `8dd0de90`

**Verdict: ACCEPT FOR FREEZE** at head **`8dd0de905c9a381b9095dd05c01eb00ffdaa0ccf`**, on branch
`research/g3-offset-873-20261113`.

- CF4-1 to CF4-5 are applied verbatim, and nothing else in the preregistration changed.
- No control is affected.
- The file is consistent: no pending marker remains, every owner quotation still matches #873
  c.6872827835 exactly, and the freeze bullet names the acceptance chain correctly.
- CF3-1 and CF3-2 are present unchanged at this head.

This check is the last link in that chain, so `8dd0de90` is the head to post on #873 for the owner's
designation of F.

**Target.** Head `8dd0de905c9a381b9095dd05c01eb00ffdaa0ccf`, fetched by branch name. Its parent `692a0e7f` adds
`CONFIRM-QB5A-PREREG-r4.md`, byte-identical to the check I issued (`cmp`). Head `8dd0de90` edits
`qb5a/G3-QB5A-PREREG-r4.md` (1351 lines, "r4:n" below) and `NOTES-QB5A-r4.md`. "r4 at `3607d5f9`" is the
previously checked state.

**Method.** I compared `git diff 3607d5f9 8dd0de90 -- qb5a/G3-QB5A-PREREG-r4.md` hunk by hunk against my
replacement texts in CONFIRM-QB5A-PREREG-r4 §4. I checked consistency across the whole file and re-checked
the quotations against #873 c.6872827835 by exact string match over the line-joined text. No
classification, no prediction, no computation on OI rules, and nothing written to the repository.

***

## 1. CF4-1 to CF4-5: applied verbatim (11 hunks)

| Item | Where at `8dd0de90` | Check |
|---|---|---|
| CF4-1 (1), the §8.2 sensitivity: RV and computations (i)–(iii), with both labels | r4:776–788 | verbatim |
| CF4-1 (2), §2.2's "carries the QB7(a) sensitivity." | r4:197 | verbatim |
| CF4-1 (3), X-10's checkpoint | the X-10 cell | verbatim |
| CF4-1 (4), Q-7's row | the Q-7 row | verbatim |
| CF4-1 (5), §15 OQ-1 "Text applied" | r4:1247–1248 | verbatim |
| CF4-2 (1), the §6.3 label scope | r4:679–680 | verbatim |
| CF4-2 (2), §16 | r4:1348–1349 | verbatim |
| CF4-3, the §14.1 line | r4:1196–1197 | verbatim |
| CF4-4, the freeze bullet and its four sub-bullets | r4:1198–1204 | verbatim |
| CF4-5, §8.5 (v)'s mirror rule | r4:859–861 | verbatim |
| CF4-5, the record time 2026-11-14T06:05:54Z | r4:37 and r4:1234 | verbatim |

The diff has exactly 11 hunks, and each maps to a row above. No other line of the preregistration changed.

**The §15 OQ-1 alternative left unchanged** (r4:1253, "Delete §8.2's sensitivity line."). This is
acceptable.

- It is marked "not adopted; record only".
- §14.1 now makes any change to an applied answer a new revision (r4:1196–1197), so the alternative cannot be
  applied as it stands.
- Its wording records the alternative as it was put to the owner.

***

## 2. Controls

The CF4-1 edits govern only what is reported beside a verdict. They define three recomputations and their
labels, and they change no rejecting predicate, aggregation, carve, GRT clause, branch, sort or outcome
rule. No rule-level control reads the QB7(a) sensitivity, X-10 or the labels:

- RC-P, RC-N, X1–X12, W-a, W-c, W-e, TC-U, TC-K and TX-1 to TX-13 are unaffected;
- W-b and W-d remain consistency checks by design.

CF4-2 adds reporting text only, and CF4-3 to CF4-5 are bookkeeping, a restatement of a rule property, and a
timestamp.

Every control therefore stands as last re-run by hand, in CONFIRM-QB5A-PREREG-r3 §2 and
CONFIRM-QB5A-PREREG-r4 §1: **all green**.

***

## 3. Consistency of the whole file

- **"pending."** It survives only at r4:38, where the history describes the replaced markers ("in place of
  the pending marker"), and at r4:259, inside a quoted corpus phrase. No marker remains.
- **"sensitivity line."** It survives at r4:345–346 (Group P), r4:1102 (Q-1b), r4:1214 and :1216 (§14.2) and
  r4:1253 (the record-only alternative). These are the separate sensitivity lines for non-decisive rows and
  deviations, plus the record-only alternative already discussed. None of them refers to the replaced QB7(a)
  text.
- **Quotations.** All eleven match c.6872827835 exactly:
  - the owner's confirmation sentence;
  - the OQ-1 to OQ-5 and OQ-7 decisions;
  - OQ-6's "Already answered; no new decision.";
  - the OQ-2 and OQ-7 qualifications;
  - the confirmation's freeze sentences.
- **The freeze bullet** (r4:1198–1204) names the acceptance chain correctly:
  - REVIEW-QB5A-PREREG-r2, the full round on the rule and its controls, which is the decision's "complete r2
    rule and its controls";
  - CONFIRM-QB5A-PREREG-r3;
  - the check of r4 that returns ACCEPT FOR FREEZE on the head it names. That is this check, which also
    confirms CF3-1 and CF3-2 at this head, as the owner's confirmation requires.

  CONFIRM-QB5A-PREREG-r4, the intermediate check at `3607d5f9`, is the one whose required edits this check
  verifies. F is `8dd0de905c9a381b9095dd05c01eb00ffdaa0ccf`.
- **CF3-1 and CF3-2.** I-SYM (r4:130–132), §6's opening, the Group P sentence, the A3x bullet and X-4 are
  unchanged since CONFIRM-QB5A-PREREG-r4 §1 confirmed them verbatim.
- **X-3.** At this head, the unit's directory holds only control-plane files (preregistration, notes,
  responses, reviews and checks). No execution file exists, as X-3 requires of F.
- **One observation, no change required.** X-10's new checkpoint says "The reviewer recomputes them (X-21)",
  but X-21's own text names only Stage 3 and the headline. X-10's sentence fully states the obligation, so
  the cross-reference is a pointer, not a gap.

***

## 4. Verdict

**ACCEPT FOR FREEZE** at **`8dd0de905c9a381b9095dd05c01eb00ffdaa0ccf`**.

The acceptance chain the freeze bullet names is now complete:

- REVIEW-QB5A-PREREG-r2;
- CONFIRM-QB5A-PREREG-r3;
- CONFIRM-QB5A-PREREG-r4, whose required edits are verified here;
- this check.

The head is ready for the owner's designation as F on #873. Under §14.1 no inventory row is classified
before that designation. Under §14.3, any later change is an amendment in its own file, never an edit of
this preregistration.

No inventory passage is classified here, and no expected outcome is stated. No manuscript change is
proposed, and no premise is adopted.
