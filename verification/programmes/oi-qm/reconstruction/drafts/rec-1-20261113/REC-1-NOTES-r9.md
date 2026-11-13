# REC-1 notes (r9): §6 rows for the revision-line and C12 references; P5 wording

Companion to `REC-1-r9.md`. Paper-only: reading only; no computation, no script on any OI rule, no
Lean, no new premise adopted, no result, verdict, classification or proof changed. P0 stays O-U
(`REC-1-P0-r3.md`, unchanged). `REC-1-r8.md` is unchanged.

**Objects.**
- Base: `REC-1-r8.md`, git blob `615b7de8e49cbfca963d57625859b02f75c37e9c`, added at `4b81298f` on
  branch `research/rec-1-1169-20261113` (draft PR #1268) and byte-identical at the branch head
  `2a9f10bab2b7047f8bcc7b03bf8744f22efb066e`. 463 lines, sha256
  `7d123ae207047874cce96d8da404151d818fefb977719f16f9503c331fa479e3`.
- Revision: `REC-1-r9.md`, 497 lines, sha256
  `c0a99912f66d735081cee8c04db22800dd25fae1f12861371cac02f6c1548c86`, git blob `945b7982`.

**Authority.** Owner decision, #1268 c.6863418087 (`amaybaum`, 2026-11-13T19:58:15Z): "Authorize
both (Recommended)". Its items: "(a) Add §A.42 item 8 provenance rows for the off-`main` references
in the revision lines, from r2 to r8, and for C12. These rows record provenance only; they do not
treat the review records as new proof support." "(b) Correct the stale P5 wording at r8:367. P0 was
authorized at #1169 c.6854241002, and no other unit was. §5 item 1's OBL-SP-wide "not authorized" is
accurate and stays unchanged." (Emphasis removed.) For P5's wording the owner chose "Name both
(Recommended)" (`amaybaum`, 2026-11-13, given in the Claude Code session; recorded at #1268
c.6863753317, 2026-11-13T20:14:06Z), resolving §4 point 1. The items come from the ChatGPT exact-head review
5896999901 of r8 at `2a9f10ba` (`amaybaum`, 2026-11-13T19:41:57Z), "Before integration" items 1 and
2. The proposed row and the replacement text are those of `REC-1-REVIEW-r8.md` finding 4 (a) and
(b); the proposed row is split there into one row per reference (change 3).

## 1. Changes

Each change below changes no result, verdict, classification, proof, control, decision rule or
bearing. §5 item 1 is unchanged.

### Change 1: title

- **r8 line:** 1. **r9 line:** 1.
- **Old text:** `# REC-1 (r8): embedded-operations reconciliation of the OI→QM results (paper-only draft)`
- **New text:** `# REC-1 (r9): embedded-operations reconciliation of the OI→QM results (paper-only draft)`
- **Reason:** revision label.

### Change 2: Revision paragraph

- **r8 line:** 18. **r9 lines:** 18–22. r8:3–17 are unchanged at r9:3–17.
- **Old text (r8:18):** `` `f0757fdb`) are brought into agreement with it, as listed in `REC-1-NOTES-r8.md`. ``
- **New text (r9:18–22):** the same sentence, followed by "r9 applies the owner's decision
  "Authorize both (Recommended)" (#1268 c.6863418087, `amaybaum`, 2026-11-13T19:58:15Z) on the two
  items of the ChatGPT review of r8 (#1268 review 5896999901, r8 at `2a9f10ba`): §6 lists each
  reference to content off `main` in the revision lines and in C12, and P5 names the authorized
  units, as listed in `REC-1-NOTES-r9.md`."
- **Reason:** the header convention every revision since r2 follows; the owner decision is quoted
  with its author and time (§A.42 item 7). Its four off-`main` references have rows in §6
  (r9:489–492).

### Change 3 (item (a)): §6 rows

- **r8 line:** inserted after r8:460 (the r1 row), before r8:461 (blank) and r8:462–463 (the closing
  paragraph, unchanged at r9:496–497).
- **r9 lines:** 465–494 (30 rows).
- **Old text:** none.
- **New text (r9:465–494):**

```
| `REC-1-RESPONSE-r1.md` (last written at `b39e40ff`) | revision line (header), r2 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-REVIEW-r2.md`, the re-check of r2 (last written at `94816172`) | revision line (header), r3 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-r2.md` at `b39e40ff` (blob `59f862d9`) | revision line (header), r3 | Provenance: identifies the revision reviewed. |
| `REC-1-RESPONSE-r2.md` (last written at `1fd0c241`) | revision line (header), r3 | Provenance: revision history; no result, classification or reading here rests on it. |
| #1268 review 5890763675 (ChatGPT, posted by `amaybaum`, 2026-11-13T12:12:46Z, at `1fd0c241`) | revision line (header), r4 | Provenance: of the changes it asked for, H-xiv rests on Main:724 and OA2:102–104 on `main` and is carried as a hypothesis, C8's wording rests on OA1:103–105 on `main`, and the P0 implementation checks are preregistered requirements, not results; no result rests on the review. |
| `REC-1-r3.md` at `1fd0c241` (blob `b93d3e45`) | revision line (header), r4 | Provenance: identifies the revision reviewed. |
| The owner's choice of repair, "(a) Explicit hypothesis (Recommended)", recorded at #1268 c.6852814589 (`amaybaum`, 2026-11-13T12:24:56Z) | revision line (header), r4 | Governance provenance, quoted. H-xiv is carried as a hypothesis; nothing is adopted. |
| `REC-1-RESPONSE-r3.md` (last written at `d5496ba8`) | revision line (header), r4 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-CONFIRM-r4.md`, the confirmation of r4 (last written at `d5496ba8`) | revision line (header), r5 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-r4.md` at `c73e855f` (blob `177778cd`) | revision line (header), r5 | Provenance: identifies the revision reviewed. |
| `REC-1-RESPONSE-r4.md` (last written at `d5496ba8`) | revision line (header), r5 | Provenance: revision history; no result, classification or reading here rests on it. |
| #1268 review 5890968976 (ChatGPT, posted by `amaybaum`, 2026-11-13T12:27:37Z, at `6de32c95`) | revision line (header), r6 | Provenance: the three P0 outcomes it asked for are preregistered decision rules of §4, not results; no result rests on the review. |
| `REC-1-r5.md` at `6de32c95` (blob `6f85a38f`) | revision line (header), r6 | Provenance: identifies the revision reviewed. |
| The owner's decision "Proceed with all (Recommended)", recorded at #1268 c.6853268285 (`amaybaum`, 2026-11-13T12:43:15Z) | revision line (header), r6 | Governance provenance, quoted. |
| `REC-1-RESPONSE-r5.md` (last written at `1ab6371b`) | revision line (header), r6 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-CONFIRM-r6.md`, the confirmation of r6 (last written at `f0757fdb`) | revision line (header), r7 | Provenance: revision history; no result, classification or reading here rests on it. |
| `REC-1-r6.md` at `1ab6371b` (blob `6febde7a`) | revision line (header), r7 | Provenance: identifies the revision reviewed. |
| `REC-1-RESPONSE-r6.md` (last written at `f0757fdb`) | revision line (header), r7 | Provenance: revision history; no result, classification or reading here rests on it. |
| #1268 c.6860582570 (owner decision, quoted with author and time) | revision line (header), r8 | Governance provenance, quoted. |
| #1268 review 5892912758 (ChatGPT, posted by `amaybaum`, 2026-11-13T14:39:31Z, at `cd38655c`) | revision line (header), r8 | Provenance: the reading of the record class in §4 rests on OA2:502 and OA3:120–123, :474–475 on `main`; no result rests on the review. |
| `REC-1-P0-r3.md` at `cd38655c` (blob `611a4d9a`) | revision line (header), r8 | Provenance: names the record the review examined; no result of it is used here. |
| `REC-1-r7.md` at `f0757fdb` (blob `f1ffac0e`), lines :287–290, :299–300, :320–321 | revision line (header), r8 | Provenance: locates the passages r8 changed. |
| `REC-1-NOTES-r8.md` (last written at `4b81298f`) | revision line (header), r8 | Provenance: revision history; no result, classification or reading here rests on it. |
| #1268 review 5890763675, cited in C12 | C12 | Provenance: C12 states in full the two points it takes from the review (a later setting written by φ from an earlier record of the response-relevant variable; correlation created by conditioning), and the review gives no further derivation; the procedure class they rely on is OA2:102–104 on `main`. H-xiv is carried as a hypothesis, so no result rests on the review. |
| #1268 c.6863418087 (owner decision, quoted with author and time) | revision line (header), r9 | Governance provenance, quoted. |
| #1268 review 5896999901 (ChatGPT, posted by `amaybaum`, 2026-11-13T19:41:57Z, at `2a9f10ba`) | revision line (header), r9 | Provenance: it names the two items r9 applies; P5's statement rests on #1169 c.6854241002 and c.6863414487, not on the review. |
| `REC-1-r8.md` at `2a9f10ba` (blob `615b7de8`) | revision line (header), r9 | Provenance: identifies the revision reviewed. |
| `REC-1-NOTES-r9.md` | revision line (header), r9 | Provenance: revision history; no result, classification or reading here rests on it. |
| #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z): "REC-1 P0 (supporting; #1268, REC-1 r7 §4)" | P5 | Governance provenance, quoted. |
| #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z): "C3 check (SQ3). A bounded, paper-only check of the actual R-lin update with (xiii)." | P5 | Governance provenance, quoted. |
```

- **Reason:** §A.42 item 8 requires every off-`main` reference to be traced to the claim it is
  attached to. r8's §6 had a row for the r1 references only (r8:460, unchanged). The rows cover the
  references of the r2–r8 revision sentences (r9:465–487), the C12 citation (r9:488), the
  references the r9 revision sentence adds (r9:489–492), and the two citations change 4 adds to P5
  (r9:493–494). The last two groups are needed so that r9 does not open the gap it closes.

### Change 4 (item (b)): P5

- **r8 line:** 367. **r9 line:** 371.
- **Old text:** `- P5. Owner authorization of a paper-only unit; none exists.`
- **New text:** `` - P5. Owner authorization of a paper-only unit: P0 is authorized by #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z), and the C3 check of the R-lin update with (xiii) by #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z); no other unit is authorized. ``
  (the wording of §4 point 1, verbatim, as the owner chose).
- **Reason:** r7's P5 was written at `f0757fdb` (2026-11-13T12:42:13Z), before #1169 c.6854241002
  (2026-11-13T13:24:47Z) authorized "REC-1 P0 (supporting; #1268, REC-1 r7 §4)"; r8 carried it
  unchanged and was stale for P0. #1169 c.6863414487 (2026-11-13T19:58:05Z) also authorizes, paper-only,
  the C3 check of the R-lin update with (xiii), the follow-up review 5892912758 proposes for P0's C3
  gap. `REC-1-REVIEW-r8.md` finding 4 (b) names P0 alone; the owner chose "Name both (Recommended)"
  (`amaybaum`, 2026-11-13, given in session; recorded at #1268 c.6863753317, 2026-11-13T20:14:06Z), so P5 names both authorizations and states that no other
  unit is authorized. The quotations of both are in §6 (r9:493–494). The Revision sentence's
  description of P5 (r9:21–22) reads "names the authorized units" to match.

## 2. Classification of each added reference

Each reference was classified on its own, by reading the claim that cites it and what that claim
uses. "Revision sentence" means the sentence of the header's Revision paragraph for that revision;
each such sentence states how the revision was produced and supports no result, classification or
reading of the record. Every commit named below is an ancestor of `2a9f10ba` and not of `main`
(`git merge-base --is-ancestor`); every blob named was checked at its commit and is unchanged at
`2a9f10ba`; each file "last written at" a commit has no later change on the branch (`git log`).

| r9 row | Reference | Citing claim | What the claim uses | Classification |
|---|---|---|---|---|
| 465 | `REC-1-RESPONSE-r1.md` | r2 sentence | where the dispositions are | Provenance |
| 466 | `REC-1-REVIEW-r2.md` ("the re-check of r2"; header "focused re-check by the r1 reviewer") | r3 sentence | which review r3 answers | Provenance |
| 467 | `REC-1-r2.md` at `b39e40ff` | r3 sentence | the reviewed object | Provenance |
| 468 | `REC-1-RESPONSE-r2.md` | r3 sentence | where the dispositions are | Provenance |
| 469 | #1268 review 5890763675 | r4 sentence | which review r4 answers. The changes it asked for rest on Main:724, OA2:102–104 (H-xiv, carried as a hypothesis) and OA1:103–105 (C8) on `main`, as `REC-1-RESPONSE-r3.md` records; the P0 implementation checks are preregistered requirements | Provenance |
| 470 | `REC-1-r3.md` at `1fd0c241` (added at `94816172`, unchanged at `1fd0c241`) | r4 sentence | the reviewed object | Provenance |
| 471 | the owner's repair choice, "(a) Explicit hypothesis (Recommended)" | r4 sentence | the governance fact that the owner chose the repair | Governance provenance, quoted (§A.42 item 7). The r4 sentence names no author or time; the row gives the GitHub record, #1268 c.6852814589 (`amaybaum`, 2026-11-13T12:24:56Z), which `REC-1-RESPONSE-r3.md` corroborates ("as relayed by the coordinator"). Nothing is adopted: H-xiv is a hypothesis |
| 472 | `REC-1-RESPONSE-r3.md` | r4 sentence | where the dispositions are | Provenance |
| 473 | `REC-1-CONFIRM-r4.md` ("the confirmation of r4") | r5 sentence | which review r5 answers | Provenance |
| 474 | `REC-1-r4.md` at `c73e855f` | r5 sentence | the reviewed object | Provenance |
| 475 | `REC-1-RESPONSE-r4.md` | r5 sentence | where the dispositions are | Provenance |
| 476 | #1268 review 5890968976 | r6 sentence | which review r6 answers. What it asked for, P0's three outcomes, are decision rules fixed in advance, not results | Provenance |
| 477 | `REC-1-r5.md` at `6de32c95` (added at `d5496ba8`, unchanged at `6de32c95`) | r6 sentence | the reviewed object | Provenance |
| 478 | owner decision "Proceed with all (Recommended)" | r6 sentence | the governance fact | Governance provenance, quoted. The r6 sentence names no author or time; the row gives the GitHub record, #1268 c.6853268285 (`amaybaum`, 2026-11-13T12:43:15Z) |
| 479 | `REC-1-RESPONSE-r5.md` | r6 sentence | where the disposition is | Provenance |
| 480 | `REC-1-CONFIRM-r6.md` ("the confirmation of r6") | r7 sentence | which review r7 answers | Provenance |
| 481 | `REC-1-r6.md` at `1ab6371b` | r7 sentence | the reviewed object | Provenance |
| 482 | `REC-1-RESPONSE-r6.md` | r7 sentence | where the dispositions are | Provenance |
| 483 | #1268 c.6860582570 | r8 sentence | the governance fact that the owner kept the literal reading | Governance provenance, quoted with author and time in the sentence |
| 484 | #1268 review 5892912758 | r8 sentence | which review the decision answers. The reading added to §4 in r8 (r9:301–307) is marked [W, REC-1; unreviewed] and cites OA2:502, OA3:120–123, :474–475 on `main` only | Provenance |
| 485 | `REC-1-P0-r3.md` at `cd38655c` | r8 sentence | the object of review 5892912758. No body passage of r9 cites P0-r3 or uses its N3, N4 or outcome | Provenance |
| 486 | `REC-1-r7.md` at `f0757fdb`, :287–290, :299–300, :320–321 | r8 sentence | location of the passages r8 changed | Provenance |
| 487 | `REC-1-NOTES-r8.md` | r8 sentence | where the change list is | Provenance |
| 488 | #1268 review 5890763675 | C12 (r9:231) | C12's sentence "It is not a consequence of C11 or of φ" cites the review for two points: a deterministic update can make a later setting depend on an earlier record of the response-relevant variable, and conditioning can create correlation. C12 states both in full; the review states the same two points and gives no further derivation (read at review 5890763675, paragraph "Required clarification"). The procedure class the points use is OA2:102–104 on `main` ("written by `φ` from records (feedback)"; "heralds (conditioning on held records)"). No result rests on the sentence: H-xiv is carried as a hypothesis, which needs no proof that it is underivable | Provenance |
| 489 | #1268 c.6863418087 | r9 sentence | the governance fact | Governance provenance, quoted with author and time in the sentence |
| 490 | #1268 review 5896999901 | r9 sentence | which review r9 answers. P5's statement rests on #1169 c.6854241002 and c.6863414487, not on the review | Provenance |
| 491 | `REC-1-r8.md` at `2a9f10ba` (blob `615b7de8`, added at `4b81298f`) | r9 sentence | the reviewed object | Provenance |
| 492 | `REC-1-NOTES-r9.md` | r9 sentence | where the change list is | Provenance |
| 493 | #1169 c.6854241002 | P5 | P5's statement that P0 is authorized uses the comment's content: it is the owner record of that authorization | Governance provenance, quoted (§A.42 item 7), as r8:456 classifies the §1 authority records. It is the source of a governance statement, not support for any scientific claim |
| 494 | #1169 c.6863414487 | P5 | P5's statement that the C3 check of the R-lin update with (xiii) is authorized uses the comment's content: it is the owner record of that authorization (item 1 of its decisions, "All three are authorized, paper-only") | Governance provenance, quoted (§A.42 item 7). It is the source of a governance statement, not support for any scientific claim |

No reference added in §6 is support on `main` or support off `main`. Rows 471, 478, 483, 489, 493 and 494
are owner records that a governance statement of the record uses as its source; §A.42 item 7 provides
for them by quotation with author and time, and none of them supports a result. The closing paragraph
of §6 (r9:496–497) is unchanged and still applies to the rows of r9:440–455 that classify a reference as support off `main`.

## 3. Checks

- `REC-1-r8.md` at `2a9f10ba` hashes to blob `615b7de8`, and r9 was built from those bytes.
- Every commit cited in the new rows resolves (`git rev-parse --verify`) and is on the branch, not
  on `main`. Every review and comment id was read through the GitHub API, and the author and time
  given match it.
- Register: the added lines contain none of "formerly", "no longer", "is now", "current form",
  "corrected", "withdrawn", "earlier revision", "should not", "reader", "now settled", "as redefined".
  The only runs of four or more capitals are file names in code spans.
- §5 item 1 (r9:414–419, "authorization: not authorized") is byte-identical to r8:410–415.

## 4. Open points for the reviewer

1. **P5's second clause and the C3 check (resolved).** #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z)
   authorizes, paper-only, the "C3 check (SQ3). A bounded, paper-only check of the actual R-lin
   update with (xiii)", frozen with "H-xiv, D₀, H-AR, C-PM, every herald and failure record, and the
   full timing convention"; c.6863418087 repeats that it "is also authorized now". This is the
   follow-up review 5892912758 proposes for P0's C3 gap. If it counts as a paper-only unit in P5's
   sense, "no other unit is authorized" (r9:371) is inaccurate when written; if it is read as a
   separate unit outside OBL-SP's P5, the clause holds. The text of
   `REC-1-REVIEW-r8.md` finding 4 (b) names P0 alone. A wording that holds under both readings is:
   `` - P5. Owner authorization of a paper-only unit: P0 is authorized by #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z), and the C3 check of the R-lin update with (xiii) by #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z); no other unit is authorized. ``
   Resolved by the owner's choice "Name both (Recommended)" (`amaybaum`, 2026-11-13, given in
   session; recorded at #1268 c.6863753317, 2026-11-13T20:14:06Z): r9:371 carries this wording, and
   r9:494 is the §6 row for c.6863414487.
2. **Owner decisions in the r4 and r6 sentences.** Both quote or describe an owner decision without
   author and time. The rows (r9:471, :478) supply the GitHub records. Each record postdates the
   revision commit it governs (r4 `c73e855f` 12:20:45Z, record 12:24:56Z; r6 `1ab6371b` 12:40:02Z,
   record 12:43:15Z), since the decisions were given in session and recorded afterwards. The
   sentences themselves are unchanged.
3. **C12's non-derivation sentence** carries no [W, REC-1] marker, and its two points are stated,
   not proved, in C12 and in the review. No result rests on it (row 488). Unchanged here.
4. **Grouped rows already in r8.** r8:456 (three #1169 comments) and r8:460 (PR, commit and review)
   each group references under one classification. Both are unchanged and outside items (a) and (b).
5. **Line ranges in the r8 sentence.** It cites r7:287–290; the changed lines are r7:289–290 within
   the bullet r7:287–293 (`REC-1-NOTES-r8.md` change 1). Row 486 copies the citation as made.

## 5. Diff size

`diff -u` of r8 against r9: 4 hunks, 3 lines removed, 37 lines added (r8 463 lines, r9 497 lines;
67 lines of unified diff with headers). Hunk 1 is the title, hunk 2 the Revision paragraph, hunk 3
P5, hunk 4 the 30 rows of §6. No other line differs.

## 6. Full diff, r8 against r9

```diff
--- REC-1-r8.md
+++ REC-1-r9.md
@@ -1,4 +1,4 @@
-# REC-1 (r8): embedded-operations reconciliation of the OI→QM results (paper-only draft)
+# REC-1 (r9): embedded-operations reconciliation of the OI→QM results (paper-only draft)
 
 **Revision.** r2 applies the required changes RC-1 to RC-16 of the independent review of r1
 (draft PR #1268, r1 at `d7f7aac1`), with the dispositions in `REC-1-RESPONSE-r1.md`. Each cited source line was
@@ -15,7 +15,11 @@
 "Adopt L; write r8 fix (Recommended)" (#1268 c.6860582570, `amaybaum`, 2026-11-13T17:47:34Z), which
 answers the ChatGPT review 5892912758 of `REC-1-P0-r3.md` at `cd38655c`: the record class of OBL-SP
 keeps its literal reading, and the three passages of §4 at r7:287–290, :299–300 and :320–321 (r7 at
-`f0757fdb`) are brought into agreement with it, as listed in `REC-1-NOTES-r8.md`.
+`f0757fdb`) are brought into agreement with it, as listed in `REC-1-NOTES-r8.md`. r9 applies the
+owner's decision "Authorize both (Recommended)" (#1268 c.6863418087, `amaybaum`,
+2026-11-13T19:58:15Z) on the two items of the ChatGPT review of r8 (#1268 review 5896999901, r8 at
+`2a9f10ba`): §6 lists each reference to content off `main` in the revision lines and in C12, and P5
+names the authorized units, as listed in `REC-1-NOTES-r9.md`.
 
 ## 1. Header
 
@@ -364,7 +368,7 @@
   O-V is reported; (vi) P2's label is checked on a known quantum-realizable contextual fragment
   (labelled O-Q) and on a fragment with no quantum model under P2 (labelled O-SQ), both fixed before
   the attempt.
-- P5. Owner authorization of a paper-only unit; none exists.
+- P5. Owner authorization of a paper-only unit: P0 is authorized by #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z), and the C3 check of the R-lin update with (xiii) by #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z); no other unit is authorized.
 
 *Rival outcomes (fixed in advance).*
 - O-C (classical): simplex-embeddable for every rule of the class, every law in `D_0`, every H-AR
@@ -458,6 +462,36 @@
 | #1143 body (2026-11-09 reformulation) | framing; row 12; §5 item 5 | Provenance. |
 | #1169 comments of 2026-11-12 (c.6834439001 to c.6835700002) | read for status of the OA records | Provenance; the status used is the one in each `STATUS.md` on `main`. |
 | Draft PR #1268, r1 at `d7f7aac1`, and its r1 review | revision line (header) | Provenance. |
+| `REC-1-RESPONSE-r1.md` (last written at `b39e40ff`) | revision line (header), r2 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-REVIEW-r2.md`, the re-check of r2 (last written at `94816172`) | revision line (header), r3 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-r2.md` at `b39e40ff` (blob `59f862d9`) | revision line (header), r3 | Provenance: identifies the revision reviewed. |
+| `REC-1-RESPONSE-r2.md` (last written at `1fd0c241`) | revision line (header), r3 | Provenance: revision history; no result, classification or reading here rests on it. |
+| #1268 review 5890763675 (ChatGPT, posted by `amaybaum`, 2026-11-13T12:12:46Z, at `1fd0c241`) | revision line (header), r4 | Provenance: of the changes it asked for, H-xiv rests on Main:724 and OA2:102–104 on `main` and is carried as a hypothesis, C8's wording rests on OA1:103–105 on `main`, and the P0 implementation checks are preregistered requirements, not results; no result rests on the review. |
+| `REC-1-r3.md` at `1fd0c241` (blob `b93d3e45`) | revision line (header), r4 | Provenance: identifies the revision reviewed. |
+| The owner's choice of repair, "(a) Explicit hypothesis (Recommended)", recorded at #1268 c.6852814589 (`amaybaum`, 2026-11-13T12:24:56Z) | revision line (header), r4 | Governance provenance, quoted. H-xiv is carried as a hypothesis; nothing is adopted. |
+| `REC-1-RESPONSE-r3.md` (last written at `d5496ba8`) | revision line (header), r4 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-CONFIRM-r4.md`, the confirmation of r4 (last written at `d5496ba8`) | revision line (header), r5 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-r4.md` at `c73e855f` (blob `177778cd`) | revision line (header), r5 | Provenance: identifies the revision reviewed. |
+| `REC-1-RESPONSE-r4.md` (last written at `d5496ba8`) | revision line (header), r5 | Provenance: revision history; no result, classification or reading here rests on it. |
+| #1268 review 5890968976 (ChatGPT, posted by `amaybaum`, 2026-11-13T12:27:37Z, at `6de32c95`) | revision line (header), r6 | Provenance: the three P0 outcomes it asked for are preregistered decision rules of §4, not results; no result rests on the review. |
+| `REC-1-r5.md` at `6de32c95` (blob `6f85a38f`) | revision line (header), r6 | Provenance: identifies the revision reviewed. |
+| The owner's decision "Proceed with all (Recommended)", recorded at #1268 c.6853268285 (`amaybaum`, 2026-11-13T12:43:15Z) | revision line (header), r6 | Governance provenance, quoted. |
+| `REC-1-RESPONSE-r5.md` (last written at `1ab6371b`) | revision line (header), r6 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-CONFIRM-r6.md`, the confirmation of r6 (last written at `f0757fdb`) | revision line (header), r7 | Provenance: revision history; no result, classification or reading here rests on it. |
+| `REC-1-r6.md` at `1ab6371b` (blob `6febde7a`) | revision line (header), r7 | Provenance: identifies the revision reviewed. |
+| `REC-1-RESPONSE-r6.md` (last written at `f0757fdb`) | revision line (header), r7 | Provenance: revision history; no result, classification or reading here rests on it. |
+| #1268 c.6860582570 (owner decision, quoted with author and time) | revision line (header), r8 | Governance provenance, quoted. |
+| #1268 review 5892912758 (ChatGPT, posted by `amaybaum`, 2026-11-13T14:39:31Z, at `cd38655c`) | revision line (header), r8 | Provenance: the reading of the record class in §4 rests on OA2:502 and OA3:120–123, :474–475 on `main`; no result rests on the review. |
+| `REC-1-P0-r3.md` at `cd38655c` (blob `611a4d9a`) | revision line (header), r8 | Provenance: names the record the review examined; no result of it is used here. |
+| `REC-1-r7.md` at `f0757fdb` (blob `f1ffac0e`), lines :287–290, :299–300, :320–321 | revision line (header), r8 | Provenance: locates the passages r8 changed. |
+| `REC-1-NOTES-r8.md` (last written at `4b81298f`) | revision line (header), r8 | Provenance: revision history; no result, classification or reading here rests on it. |
+| #1268 review 5890763675, cited in C12 | C12 | Provenance: C12 states in full the two points it takes from the review (a later setting written by φ from an earlier record of the response-relevant variable; correlation created by conditioning), and the review gives no further derivation; the procedure class they rely on is OA2:102–104 on `main`. H-xiv is carried as a hypothesis, so no result rests on the review. |
+| #1268 c.6863418087 (owner decision, quoted with author and time) | revision line (header), r9 | Governance provenance, quoted. |
+| #1268 review 5896999901 (ChatGPT, posted by `amaybaum`, 2026-11-13T19:41:57Z, at `2a9f10ba`) | revision line (header), r9 | Provenance: it names the two items r9 applies; P5's statement rests on #1169 c.6854241002 and c.6863414487, not on the review. |
+| `REC-1-r8.md` at `2a9f10ba` (blob `615b7de8`) | revision line (header), r9 | Provenance: identifies the revision reviewed. |
+| `REC-1-NOTES-r9.md` | revision line (header), r9 | Provenance: revision history; no result, classification or reading here rests on it. |
+| #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z): "REC-1 P0 (supporting; #1268, REC-1 r7 §4)" | P5 | Governance provenance, quoted. |
+| #1169 c.6863414487 (`amaybaum`, 2026-11-13T19:58:05Z): "C3 check (SQ3). A bounded, paper-only check of the actual R-lin update with (xiii)." | P5 | Governance provenance, quoted. |
 
 This record does not land on `main` while any support off `main` remains; before landing, each such
 row is closed by landing its source or narrowed (§A.42 items 2, 8).
```
