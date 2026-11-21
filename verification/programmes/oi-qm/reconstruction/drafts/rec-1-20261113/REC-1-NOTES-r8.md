# REC-1 notes (r8): the three r7 passages brought into agreement with the literal reading

Companion to `REC-1-r8.md`. Paper-only: reading and hand reasoning; no computation, no script on any
OI rule, no Lean, no new premise adopted, no result, verdict, classification or proof changed. P0
stays O-U (`REC-1-P0-r3.md`, unchanged). `REC-1-r7.md` is unchanged.

**Objects.**
- Base: `REC-1-r7.md`, git blob `f1ffac0e4a254536930acf2afd56e40c32597c51`, added at `f0757fdb` on
  branch `research/rec-1-1169-20261113` (draft PR #1268) and byte-identical at the branch head
  `cd38655c8c140577d1d5bb5fc3bfc0076553c9a9`. sha256
  `c25ec1ffd80f5e932abe624a43528d8717a4bd6e870e631878885f48404f8965`.
- Revision: `REC-1-r8.md`, 463 lines, sha256
  `7d123ae207047874cce96d8da404151d818fefb977719f16f9503c331fa479e3`, git blob `615b7de8`.

**Authority.** Owner decision, #1268 c.6860582570 (`amaybaum`, 2026-11-13T17:47:34Z): "Adopt L; write
r8 fix (Recommended)". Its items: "The literal L reading of the preregistered r7 class is kept. That
reading is "(H4) or (V-ii-H)" with held-at-use typing"; "A forward revision, REC-1-r8, will correct
the three r7 passages that contradict the L reading (the open-content and preparation passages that
presume noncomposable heralds). REC-1-r7 itself stays unchanged"; "Any B or partial-retention
extension is a separately scoped class for later. It is not a retroactive change to P0." (Emphasis
removed.) The question came from the ChatGPT exact-head review 5892912758 of P0 r3 at `cd38655c`
(`amaybaum`, 2026-11-13T14:39:31Z), paragraph "r7 ambiguity is real".

## 1. Which r7 passages contradict the L reading

The L reading: OBL-SP's record class is "(H4) or (V-ii-H)" (r7:255) with heralds held at use and
records formed inside `S` (r7:255–256). With its cited definitions, (H4) "the held record at the
latest read determines every earlier available read" (OA2:502), and (V-ii-H) makes every heralded
composite available (OA3:120–123), which under held-at-use typing is retention-type (OA3:474–475).
So read, every observer of the class retains every read of the horizon in `V` (P0 r3 N3 and §6; the
review: "implies full retention"). Under full retention, no admitted herald is unavailable for want
of a retained earlier herald record, so heralds that cannot be composed for that reason do not arise
inside the class.

A search of r7 for `compos`, `retent`, `retain`, `partial`, `residual` and `earlier herald` finds
three passages that place such heralds, or a residual defined by herald retention, inside OBL-SP's own
content. These are the three passages P0 r3 names (r7:287–290, :299–300, :320–321) and the review
counts. The count is three.

1. **r7:287–293 (the open-content bullet), at r7:289–290.** It lists among the preparations outside
   the coset form "heralds that cannot be composed because, under held-at-use typing, an earlier
   herald is available only if a record of it is formed inside `S`". Under L every earlier herald's
   record is held, so this item is empty within the class; listing it as open content presumes
   observers that retain only some reads.
2. **r7:298–300 (the ordering comparison with AW-OA2-1), at r7:299–300.** "a P0 pass narrows it to the
   herald-retention residual" names the post-pass residual by herald retention, which presumes
   heralds whose records are not retained.
3. **r7:317–322 (P0 prerequisite), at r7:320–321.** "such as heralds that cannot be composed under the
   fixed typing" gives as the example of out-of-form preparations the item that does not arise under L.

**Passages checked and not changed (no contradiction with L).**
- r7:254–256, the statement: it is the clause L reads literally.
- r7:288–289, "heralds on prefixes of several lengths, whose cosets refine as the prefix grows": it
  does not presume partial retention (under full retention every prefix is retained). P0 r3 N4 finds
  these preparations inside the coset form under every reading [W, P0; unreviewed as a whole]; that is
  a P0 finding, not a conflict with L, and importing it into the preregistration is outside this
  revision.
- r7:311 and r7:366 (herald typing C7 carried as a scope hypothesis; "other herald typings and record
  classes (C6, C7)" among the remaining routes): consistent with L; partial-retention observers fall
  under "other record classes".
- r7:352, control (iii): the (V-ii-U) shift artefact is excluded by the typing; independent of L.
- r7:333–334, the Out-of-form outcome, and r7:307–309, the mixed-case ordering sentence: they are
  conditional on preparations being exhibited and stay correct when the out-of-form list is empty.
- §3 rows C5–C7 and §3.2: general interface statements, not about OBL-SP's class.

## 2. Changes, passage by passage

Each change below changes no result, verdict, classification, proof or control. P0's three outcomes,
the ordering rule, P1–P5, the rival outcomes and their bearings are unchanged. No mathematics changed:
the only added content is the statement of the literal reading the owner decision keeps, and its
direct consequence that noncomposable heralds of the r7 kind do not arise within the class, marked
[W, REC-1; unreviewed] and resting on OA2:502 and OA3:120–123, :474–475 on `main` (`c3b5f37a`, blobs
`8f8ddf73`, `0a36fd05`, re-read for this revision).

### Change 1: the open-content bullet

- **r7 lines:** 289–290 replaced; new sentences added after r7:293. The bullet is r7:287–293.
- **r8 lines:** 293 (replacement) and 297–303 (added). The bullet is r8:291–303. r7:291–293 are
  byte-identical at r8:294–296.
- **Old text (r7:289–290):**
  > grows, and heralds that cannot be composed because, under held-at-use typing, an earlier herald is
  > available only if a record of it is formed inside `S` (C6, C7; OA3:410–416, :474–475). This
- **New text (r8:293):**
  > grows. This
- **New text (r8:297–303, after r7:293's "(C7)."):**
  > Under held-at-use typing an earlier herald is available only if a record of it is formed inside
  > `S` (C6, C7; OA3:410–416, :474–475). The record class of the statement is read literally with its
  > cited definitions ((H4), OA2:502; (V-ii-H), OA3:120–123, which under held-at-use typing is
  > retention-type, OA3:474–475): every observer of the class retains every read of the horizon in
  > `V`, so heralds that cannot be composed because an earlier herald's record is not held at use do
  > not arise within the class [W, REC-1; unreviewed]. Observers that retain only some reads are not in
  > the class; an extension of OBL-SP to them is a separately scoped class, not studied here.
- **Reason.** r7 listed noncomposable heralds as part of OBL-SP's open content, which contradicts the
  literal class (finding 1). The noncomposable item is removed from the list. The typing fact r7 gave
  as its reason is kept, with the same citations, followed by the literal reading and the scope
  sentence the owner decision requires (item 3: partial retention is a separate class). The added
  sentences are placed after r7:293 so that "This residual" keeps its antecedent (the out-of-form set)
  and r7:291–293 stay byte-identical. The short source line r8:293 renders as continuous text.
- **Mathematics.** None changed. The removed item is an anticipated example of out-of-form
  preparations, not a result; the added sentences state the adopted reading of the existing clause.

### Change 2: the ordering comparison with AW-OA2-1

- **r7 lines:** 299–300. **r8 lines:** 309–310.
- **Old text:**
  > `main` (S3:56–98, :196–207; OA2:522–576), and because a P0 pass narrows it to the herald-retention
  > residual, a subset of OBL-SP's own preparations. The ordering is by cost, not by the size of the
- **New text:**
  > `main` (S3:56–98, :196–207; OA2:522–576), and because a P0 pass narrows it to the preparations P0
  > lists as outside the coset form, a subset of OBL-SP's own preparations. The ordering is by cost, not by the size of the
- **Reason.** "herald-retention residual" names the residual by herald retention, which presumes
  partial retention (finding 2). The replacement names it as r7's own P0 prerequisite (r7:319–322) and
  the open-content bullet do: the preparations P0 lists as outside the coset form.
- **Mathematics.** None changed. The ordering argument (by cost; classes not nested) and its
  conclusion are unchanged.

### Change 3: the P0 prerequisite

- **r7 lines:** 320–321. **r8 line:** 330.
- **Old text:**
  > which preparations, if any, fall outside that form, such as heralds that cannot be composed
  > under the fixed typing. Once the in-form preparations pass the operational witness, only those listed preparations
- **New text:**
  > which preparations, if any, fall outside that form. Once the in-form preparations pass the operational witness, only those listed preparations
- **Reason.** The example given is the item that does not arise under L (finding 3). It is removed; the
  instruction to record any out-of-form preparations is kept.
- **Mathematics.** None changed. P0's decision rule, implementation checks and three outcomes are
  unchanged.

### Title and revision lines

- **r7:1 → r8:1.** "(r7)" → "(r8)".
- **r7:14 → r8:14–18.** r7:14 is extended by one Revision sentence:
  > r8 applies the owner's decision "Adopt L; write r8 fix (Recommended)" (#1268 c.6860582570,
  > `amaybaum`, 2026-11-13T17:47:34Z), which answers the ChatGPT review 5892912758 of `REC-1-P0-r3.md`
  > at `cd38655c`: the record class of OBL-SP keeps its literal reading, and the three passages of §4 at
  > r7:287–290, :299–300 and :320–321 (r7 at `f0757fdb`) are brought into agreement with it, as listed
  > in `REC-1-NOTES-r8.md`.

## 3. Diff size

`diff -u` of r7 against r8: 4 hunks, 8 lines removed, 17 lines added (r7 454 lines, r8 463 lines; 60
lines of unified diff). Hunk 1 is the title, hunk 2 the Revision sentence, hunk 3 changes 1 and 2
(one hunk, as they are 6 lines apart), hunk 4 change 3. No other line differs.

## 4. Open points for the reviewer

1. **§6 off-`main` table.** r8 does not add a row for the references in the new Revision sentence
   (#1268 c.6860582570; review 5892912758; `REC-1-P0-r3.md` at `cd38655c`; `REC-1-NOTES-r8.md`).
   Earlier revision-line references are covered only by the r1 row (r7:451). Each is provenance: the
   added sentence of change 1 rests on OA2:502 and OA3:120–123, :474–475 on `main`, and the owner
   decision is governance. A reviewer applying §A.42 item 8 may require a provenance row.
2. **Stale authorization wording, not a conflict with L.** P5 (r7:358; r8:367) reads "Owner authorization
   of a paper-only unit; none exists", and §5 item 1 reads "authorization: not authorized". P0 has
   since been authorized (#1169 c.6854241002, as P0 r3 records). Left unchanged, as outside the
   owner-scoped correction.
3. **The several-lengths item** (r7:288–289; r8:292–293) is kept as an anticipated out-of-form example.
   P0 r3 N4 places it inside the form [W, P0; unreviewed]; reconciling the preregistration with that
   finding is not part of this decision.
4. **Review status.** The added reading in change 1 is [W, REC-1; unreviewed]. It agrees with P0 r3 N3
   and with the review's "implies full retention", but neither is an independent review of r8. The
   owner comment names the next steps: an independent review, then the ChatGPT exact-head review.

## 5. Full diff, r7 against r8

```diff
--- REC-1-r7.md
+++ REC-1-r8.md
@@ -1,4 +1,4 @@
-# REC-1 (r7): embedded-operations reconciliation of the OI→QM results (paper-only draft)
+# REC-1 (r8): embedded-operations reconciliation of the OI→QM results (paper-only draft)
 
 **Revision.** r2 applies the required changes RC-1 to RC-16 of the independent review of r1
 (draft PR #1268, r1 at `d7f7aac1`), with the dispositions in `REC-1-RESPONSE-r1.md`. Each cited source line was
@@ -11,7 +11,11 @@
 `REC-1-RESPONSE-r4.md`. r6 applies the ChatGPT review of r5 (#1268 review 5890968976, r5 at
 `6de32c95`) under the owner's decision "Proceed with all (Recommended)", with the disposition in
 `REC-1-RESPONSE-r5.md`. r7 applies the required changes RC-r6-1 and RC-r6-2 of the confirmation of r6
-(r6 at `1ab6371b`), with the dispositions in `REC-1-RESPONSE-r6.md`.
+(r6 at `1ab6371b`), with the dispositions in `REC-1-RESPONSE-r6.md`. r8 applies the owner's decision
+"Adopt L; write r8 fix (Recommended)" (#1268 c.6860582570, `amaybaum`, 2026-11-13T17:47:34Z), which
+answers the ChatGPT review 5892912758 of `REC-1-P0-r3.md` at `cd38655c`: the record class of OBL-SP
+keeps its literal reading, and the three passages of §4 at r7:287–290, :299–300 and :320–321 (r7 at
+`f0757fdb`) are brought into agreement with it, as listed in `REC-1-NOTES-r8.md`.
 
 ## 1. Header
 
@@ -286,18 +290,24 @@
   accessible-effect or equivalence check fails or is unestablished, that fragment is O-U (P0).
 - If P0 passes on that fragment, OBL-SP's open content is the set of preparations that P0 lists as
   outside the coset form: heralds on prefixes of several lengths, whose cosets refine as the prefix
-  grows, and heralds that cannot be composed because, under held-at-use typing, an earlier herald is
-  available only if a record of it is formed inside `S` (C6, C7; OA3:410–416, :474–475). This
+  grows. This
   residual is the preparation-side route of OA-2 N2.1 (restricted preparations, OA2:75, :313–315)
   inside the native class. Its answer still separates O-C from the non-classical outcomes. Its
   bearing is conditional on the herald typing, which the stated premises do not fix (C7).
+  Under held-at-use typing an earlier herald is available only if a record of it is formed inside
+  `S` (C6, C7; OA3:410–416, :474–475). The record class of the statement is read literally with its
+  cited definitions ((H4), OA2:502; (V-ii-H), OA3:120–123, which under held-at-use typing is
+  retention-type, OA3:474–475): every observer of the class retains every read of the horizon in
+  `V`, so heralds that cannot be composed because an earlier herald's record is not held at use do
+  not arise within the class [W, REC-1; unreviewed]. Observers that retain only some reads are not in
+  the class; an extension of OBL-SP to them is a separately scoped class, not studied here.
 - Comparison with AW-OA2-1, non-additive observers (OA2:601–602, :626). It needs no new physical
   premise either: H-AR is a restriction the Definition does not impose (OA2:182–196), so dropping it
   removes a restriction and adds none. It is the read-side route of N2.1 (OA2:75) [W, REC-1]. The two classes
   are incomparable: OBL-SP drops (SP) and keeps H-AR; AW-OA2-1 drops H-AR and keeps (SP). OBL-SP is
   placed first because it has a cheapest decisive step (P0) whose inputs are [R] statements on
-  `main` (S3:56–98, :196–207; OA2:522–576), and because a P0 pass narrows it to the herald-retention
-  residual, a subset of OBL-SP's own preparations. The ordering is by cost, not by the size of the
+  `main` (S3:56–98, :196–207; OA2:522–576), and because a P0 pass narrows it to the preparations P0
+  lists as outside the coset form, a subset of OBL-SP's own preparations. The ordering is by cost, not by the size of the
   two classes, which are not nested. It is not placed first
   for an expected non-classical answer: S3:206–207 points to O-C on the main fragment.
 - Ordering rule, fixed in advance. If P0 passes for the whole class under the fixed typing (the
@@ -317,8 +327,7 @@
 - P0. Cheapest decisive step: decide whether, for every instance in the class, the reachable laws
   of `Z₀` are mixtures of uniform laws on the cosets of one subgroup, each coset reachable and
   determined by the held record, so that the coset-space model is a simplex embedding. Record
-  which preparations, if any, fall outside that form, such as heralds that cannot be composed
-  under the fixed typing. Once the in-form preparations pass the operational witness, only those listed preparations
+  which preparations, if any, fall outside that form. Once the in-form preparations pass the operational witness, only those listed preparations
   carry OBL-SP's open content. P0 is posed under H-xiv.
   Implementation checks (not results): the coset-space simplex witness uses accessible indicator
   effects in the C-PM class, excluding reads of preparation labels; that a coset is "determined by
```
