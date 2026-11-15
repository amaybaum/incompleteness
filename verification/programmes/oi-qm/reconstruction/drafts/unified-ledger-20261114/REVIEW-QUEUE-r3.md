ACCEPT WITH CHANGES

# Focused review of QUEUE-PROPOSAL-r3 (grouping by Issue)

This review is read-only and paper-only. `QUEUE-PROPOSAL-r3.md` and `RESPONSE-QUEUE-r2.md` were
confirmed byte-identical to their copies on PR #1292 at `2ac8190e`. Parts 1–3 were compared with r2 by
`diff`, and Part A was read in full. Fourteen assigned Issues were read at source through the GitHub
API: #1055, #1234, #1049, #1245, #1062, #1028, #1058, #1142, #1190, #1238, #1244, #1029, #1015 and #970.
So were the comments r3 cites. Merge state was checked on `main` (`dfeec843`). No other file was
written, no computation was run, and nothing was posted or relabelled.

References "Q3:n" are lines of `QUEUE-PROPOSAL-r3.md`.

## Summary

- The regrouping preserves every r2 item, and most assignments fit their Issues.
- #1028 is a sound home for the remaining corrections.
- The rules on readiness, ranking and tiers are unchanged.

Three things need correcting:
- **#1244's two vehicles have already landed.** The Structure:179 draft and the A/4 older-sites sweep
  were both merged on 2026-11-12. r3 treats them as open, so F-17 (:179), G-2 and T-4, and owner
  questions 3 and 4, rest on a stale record.
- **RO-2 changed in substance.** It now calls (C) the "likeliest-looking" outcome. The response does not
  disclose this, and the record does not support it.
- **RO-3's ranking borrows #1055's readiness.** #1055's "ready" applies to its own question, and the
  inventory is only proposed for #1055.

## Should-fix

**S1. The Structure:179 draft and the A/4 sweep have landed.** (Q3:345–355, Q3:556–557, Q3:894–899)

r3 says #1244 "holds the authorized paper-only Structure:179 correction draft" and "an authorized
sweep". It proposes adding T-4 and G-2 to the sweep, and asks whether the :179 draft "also take[s]"
F-17. Both were merged before `dfeec843`:

- **The :179 draft.** PR #1261, "Structure §2.4: A/4 moved out of the OI-distinguishing row", was merged
  at 2026-11-12T18:40:51Z (merge `0ebf90db`; commit `54e509bd` is on `main`). At `dfeec843`,
  Structure:179 no longer lists A/4. The level-placement defect F-17 records (dark sector at G3 × D,
  against :191–192) is still there.
- **The sweep.** PR #1262, "A/4 older-sites sweep", was merged at 2026-11-12T19:18:05Z (merge
  `fba459cb`). Its PR body reports "**(b) Unconditional mode count or geometry: 0.** No conditions were
  added." So the owner's rule was applied and the sweep is closed.
- **#1244's body.** Its status note ("own authorized paper-only correction draft, not a merge") predates
  both merges. r3 quotes it as current.

Correct as follows:
- F-17 (:179), G-2 and T-4 each need a new correction unit, on #1244 or in #1028. Neither vehicle can
  take them now.
- Owner question 3 becomes: "a new unit for F-17 at :179".
- Owner question 4 should say that the merged sweep applied the "no conditions added to unconditional
  mode-count" rule and left GR:12 as it is. G-2 therefore asks whether to revisit an applied owner rule.
- §1.6's "one authorized draft on a line listed here" (Q3:556–557) is to be removed.
- Optionally, record the stale #1244 note as a sourced fact for the owner, as was done for #873.

**S2. RO-2 now predicts its outcome, and the response does not say so.** (Q3:750–751)

r2 said "its verdict may be the residual class (C)". r3 says "its likeliest-looking outcome class on
the record so far is the residual (C)".
- The change is not listed in `RESPONSE-QUEUE-r2.md`, including its "Changes beyond the request" section.
- It is not supported. The two earlier units answered different questions under different rules.
- The preregistration "states no expected outcome" (`G3-QB5A-PREREG-r4.md`:6 at `8dd0de90`), and a
  queue proposal should not supply one.

Restore r2's wording.

**S3. RO-3 borrows #1055's readiness.** (Q3:669–670; §3.1 table)

"RO-3 now sits at a ready Issue (#1055), as RO-2 does (#873)" uses #1055's recorded "ready". That
readiness belongs to #1055's own question: recovering the two consumers of A1 without A1, with fixed
controls (#1055 body). The exactness inventory is only proposed as #1055's next unit (PC/RO-3, a
(proposal)).

State this as r2 did for #873 (REVIEW-QUEUE-r1 N2): "#1055's readiness is for its recorded question; no
row records the readiness of the inventory". Keep the ranking reason "its scope is not frozen", which
needs no readiness claim.

## Nits

- **N1. D1 in #1028.** #1028 comment 6628572816 lists ch19:20 under CON-04, a cosmological-constant
  "dissolution" stated without its G3 condition. That is not D1's defect, the heading against its own
  entries. Say "the same line, under CON-04", so that one unit handles both.
- **N2. #1238's fit is partial.** #1238's scope is the "QM is / is derived from embedded observation"
  wording. S-1 (its GR half), S-17 ("every concept") and K-5 ("the fundamental laws") go beyond that.
  Note this in owner question 2, or place S-17 and K-5 in #1028.
- **N3. Items split across two Issues.** F-3 and F-17 are each split by clause. Their parts appear once
  each, under different Issues. Say so in A.0, so that "exactly one Issue" reads as one Issue per part.
- **N4. #1062's fit is partial.** #1062 asks whether a native rule produces a persistent observer. U-2
  asks whether typical bijections admit one. r3 says "closest" and keeps it as owner question 16. That is
  adequate.

## The six checks

1. **Nothing lost: confirmed, apart from S2 and S3.** Every r2 item appears in Part A:
   - the MC items: MC-1 to MC-5, D2, D4, the F-12 row and F-10;
   - LC-1 to LC-8;
   - RO-1 to RO-10;
   - the planning changes, as PC-1 to PC-3 and the assignments.

   Each part appears under one Issue (N3). The detail of Parts 1–3 is unchanged except for:
   - the Issue references;
   - RO-3's and RO-4's recorded planning (now from #1055, #1234 and #1049);
   - PC-3's wording;
   - the RO-2 sentence in S2.
2. **Fit.** Each Issue was read at source.
   - **Fits:**
     - #914 (LC; O-IF-SELECT for M1);
     - #1169 (S-J, EXACT, S-A);
     - #873 (QB5(a) is tracked there: comments 6872998421 and 6875553420);
     - #1055 (A1-necessity, a strong match for the carrier inventory);
     - #1234 (its item 6 is Q2's premise question, and its item 2 is D4's unswept book sites);
     - #1049 (A5 selection: paper-only, ready, with a designated writer);
     - #1211;
     - #1245 (W1 is tracked there; its body says "No new investigation … is authorized yet");
     - #1063;
     - #1058 (same anchor, SM:468);
     - #1142 (D5 is its item 1, and GR:410 itself carries the "relax" sentence of its item 2);
     - #1190 (Chapter 18; coordination owner Codex);
     - #1029 (comment 6581824083 flags the stale H-Bell pointers for "a separate approved referencing
       unit");
     - #1015 (finiteness wording, per #1238 comment 6804055462).
   - **Partial fits:** #1238 (N2) and #1062 (N4).
   - **Not fitting as stated:** #1244 (S1).
   - **Quotations.** All quoted planning blocks and comments were found verbatim.
3. **#1028: confirmed as the better home.**
   - Its body "holds the scientific and status corrections".
   - Its working rules match §A.25, §A.27 and §A.30.
   - It authorizes "units authorized one by one".
   - Comment 6658037322 shows it taking reassigned items.
   - Its own sites (Complexity:206, Substratum:56, Explainer:930, Main:744) do not collide with these
     items.

   Option A avoids a new Issue, in line with the owner's direction. The caveat that it widens the
   2026-11-01 disposition is stated, and Option B is a fair fallback.
4. **The new SM-flavour Issue: justified.** No open Issue carries flavour derivations. #970 is the only
   plausible alternative ("Advance the scientific claims exposed … by the Introduction/full-corpus audit,
   after the source corrections are made accurate"). It is tied to another audit and is offered to the
   owner as the alternative. RO-7 stays below the shared gaps.
5. **Owner questions.**
   - **#1190.** The overlaps are accurate: appendix-a:70 is #1190's WP3-34/WP8-10, and SM:1118 is
     WP3-33 (comment 6713826444).
   - **#1244.** The overlaps are inaccurate, as S1 explains.
6. **Unchanged rules: confirmed.**
   - Readiness is never presented as authorization. Every "Authorization needed" cell names what §A.45
     rule 3 requires.
   - RO-1 and RO-2 have "no default order".
   - The order of the Part A groups "is not a ranking".
   - "No tier change is proposed".
   - Every assignment is marked (proposal), on the correct ground that it widens an Issue's scope.
   - The grouping direction is labelled as having no GitHub record. None was found on #914 after
     14:55:05Z.
