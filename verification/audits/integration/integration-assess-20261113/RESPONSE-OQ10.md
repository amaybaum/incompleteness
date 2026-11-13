# RESPONSE-OQ10: dispositions of CONFIRM-OQ10 findings F1–F12

**Objects.** r1: `NOTE-OQ10.md`, unchanged, byte-identical to the reviewed blob on
`research/integration-assess-20261113` (checked by `diff` against `git show` at the fetched head
`dc673d62`). r2: `NOTE-OQ10-r2.md`. Every finding is applied; none is disputed. Two places go
beyond the review's replacement text, and are listed under "Additions".

**Facts re-checked before applying.** The #1097 body quotes the owner's adjustment ("New research
evidence may also land when it is needed for reproducibility or to support existing records …") and
concern; #1097 was merged by `amaybaum` with 0 comments; `ab6211d7` is authored by `amaybaum` and
reached `main` through the #1103 merge `fb117893`; §A.46 item 6 and §A.45 rule 7 ("**Integrate:**
…") read as quoted at `c3b5f37a`; review 5895564670 reads "An ACCEPT by a model is not independent
mathematical verification (§A.46)".

| Finding | Disposition | r2 location |
|---|---|---|
| F1 (Medium) | Applied, both parts of the primary fix: the closing clause on the #1097 mark is removed, and the four facts (owner adjustments, owner concern, merge by `amaybaum` with no comments, `ab6211d7`/#1103 leaving item 2 unchanged) are added to the history paragraph. | §1 history paragraph; closing sentence of §5 |
| F2 (Medium) | Applied: R-b′ added after R-b with the review's text; the R-b′ column consequence stated after the table; owner question 1 extended. Also carried into the R-c sentence and the "Basis"-lines paragraph. | §4 readings; paragraph after the table; §5 question 1 |
| F3 (Medium) | Applied: R-a cells for #1275–#1276 now read "lands after gates"; the R-a-only remediation sentence is replaced by the review's sentence on item 4 applying under every basis. | §4 table and paragraph after it |
| F4 (Medium) | Applied: item 6's operative clause quoted in the "Basis"-lines paragraph, with the R-d counterpart (verified evidence is kept). | §4 "Two further consequences"; §5 question 3 |
| F5 (Low) | Applied verbatim. | §4 R-d |
| F6 (Low) | Applied verbatim. | §4 R-d |
| F7 (Low) | Applied: "states, in its 'Landing' section"; per-unit evidence-layer quotes for OA-1–OA-3 and W1-1. | §2 "Stated basis" |
| F8 (Low) | Applied verbatim. | §3 item 4 status row |
| F9 (Low) | Applied: "last sentence" replaced at all three sites; new §3 row for item 2's actual last sentence (§A.42 item 5). The "Work that meets none …" row label gains "…" to mark the quotation as truncated. | §1, §4 R-a, §5 closing; §3 |
| F10 (Low) | Applied verbatim, appended to R-a before the reproducibility variant. | §4 R-a |
| F11 (Low) | Applied: "IA2 §0, §3 and §5"; #1275 R-d cell extended. The table header "IA2 §5" is shortened to "IA2" to match. | §4 table |
| F12 (Info) | Applied both optional fixes. The PR-body sentence also records that the body names head `2d064a71`, before the merged head. | §2 "Merge"; §3 remediation row |

**Additions beyond the review's text.**
1. F4: besides the §4 paragraph, §1 quotes item 6's opening sentence and its disposition clause
   after the item 2 history, because owner question 3 now depends on it and §1 is where the rules
   are quoted. §5 question 3 states the per-reading item 6 consequence (R-b/R-b′: within the audit;
   R-d with model review meeting item 1: kept).
2. §5 question 3 also states the R-a case: whether a record's own scoped claim is a "surviving claim"
   for item 6's audit, which is the same question as F9's §A.42 item 5 row. The review's F4 named
   only R-b and R-d; under R-a the records are also not verified in item 1's sense, so item 6's
   clause reaches them too unless their own claim counts as surviving. This is stated as a
   question, not answered.
3. A revision line in the standing paragraph names r2 and the review.

**Checks on r2.** No barred path string or the session-storage word; no recommendation; the R-a,
R-b, R-b′ and R-d consequences agree with IA2 §0, §3, §4 and §5 at `c7ce4f28`.

## Full r1 → r2 diff

```diff
--- NOTE-OQ10.md	2026-11-13 21:24:57.025290205 +0000
+++ NOTE-OQ10-r2.md	2026-11-13 21:34:08.216314540 +0000
@@ -1,9 +1,10 @@
-# OQ-10: the #1265 landing practice and §A.46 items 1, 2 and 4
+# OQ-10: the #1265 landing practice and §A.46 items 1, 2 and 4 (r2)
 
 **Standing.** Paper-only note for an owner ruling, written under #1169 c.6865177667 (`amaybaum`,
 2026-11-13T21:19:31Z), OQ-10: "a short paper-only note on how the #1265 landing practice relates to
 §A.46 items 1, 2 and 4, for an owner ruling. The note is not a waiver and does not edit AGENTS.md."
 It grants no waiver or merge authority, chooses no reading, and changes no record or status.
+r2 applies the findings of CONFIRM-OQ10 (ACCEPT WITH CHANGES, F1–F12).
 
 **Pins.** `main` = `c3b5f37a` (the #1265 merge). Assessment r2, its review and confirmation:
 `verification/audits/integration/integration-assess-20261113/` at `c7ce4f28` (IA2, REVIEW-r1,
@@ -33,10 +34,22 @@
 proposed removal of partially verified research records from `main` was found to break records on
 `main` that depend on them. Amended the same day …"). Its first text (`0ad4bd0f`) let research
 evidence "be kept on `main` whether or not its programme is complete". The conditions of item 2
-entered with `be616ffc`; its last sentence took its present form in `e10a9ba2`. The #1097 PR
+entered with `be616ffc`; its "Work that meets none of these conditions …" sentence took its
+present form in `e10a9ba2`. The #1097 PR
 description, which merged them, marks that sentence "**For the owner to confirm:** this sentence comes
 from the coordinator's proposal, which the owner approved. A reviewer suggested deleting it as an
-addition; it is kept, reworded to match §A.43."
+addition; it is kept, reworded to match §A.43." The conditions follow the owner's adjustments
+quoted in that description ("New research evidence may also land when it is needed for
+reproducibility or to support existing records …"), given after the owner's concern "I am
+concerned that Rule 2 will lead to more issues where main will contain unverified data." #1097 was
+merged by `amaybaum` and has no comments; §A.46 was amended again the same day by owner decision
+(`ab6211d7`, #1103), leaving item 2 unchanged.
+
+Item 6, which item 2 names for removal, reads in part: "Removal of research evidence from `main` is
+never automatic." … "Verified evidence, including verified negative and conditional results, is
+kept on `main`. For other material that has not met the verification standard for its specific
+claims, the normal proposed disposition is removal from the current tree *if the audit establishes
+that it is unnecessary*: no surviving claim depends on it; …"
 
 ## 2. The practice (#1265, merged as `c3b5f37a`)
 
@@ -49,13 +62,15 @@
   (Recommended)"; "What landed: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4, as research records on their
   stated scope. No claim is promoted." ChatGPT review 5888322900 at the head `a965818e`: "ACCEPT for
   bounded evidence retention on `main` … **not** a new scientific proof, an upgrade of any [W]/[R]
-  finding, human or kernel verification". The PR body at merge still read "Not for merge" and
-  "Landing: not authorized"; the merge decision is c.6848447181.
+  finding, human or kernel verification". The PR body reads "Not for merge" and "Landing: not
+  authorized" and names head `2d064a71`, before the merged head; the merge decision is c.6848447181.
 - **Stated basis.** Each of the four `STATUS.md` notes (`oi-qm/reconstruction/oa-{1,2,3}-20261112/`,
-  `physical-realization/w1-1-20261112/`) ends: "**Basis.** §A.46 item 2: the record supports the claim
+  `physical-realization/w1-1-20261112/`) states, in its "Landing" section: "**Basis.** §A.46 item 2: the record supports the claim
   above, at the strength stated. No record on `main` depends on it at `62bdc2cf`. The accountable
-  Issue is #1169" (#1245 for W1-1). Each gives a "Claim supported by this record" in quotation, with
-  its evidence layer ("paper-level research findings … not adopted; no manuscript claim affected").
+  Issue is #1169" (#1245 for W1-1). Each gives a "Claim supported by this record" in quotation, closing
+  with its evidence layer (OA-1 to OA-3: "paper-level research findings: …; not adopted; no
+  manuscript claim affected"; W1-1: "paper-level hand derivations with independent AI-agent reviews,
+  not machine-checked; … no manuscript claim affected").
 - **Batch-1 contrast.** The batch-1 notes the owner record points to state a different basis: "An
   established claim needs the record (§A.46 item 2): the claim above" (for example
   `native-preparation-source-1-20261110/STATUS.md`:87).
@@ -68,10 +83,11 @@
 | 2: "needed for reproducibility" | Not invoked; paper-only, no computation | differs |
 | 2: "to support records already on `main`" | Each note: "No record on `main` depends on it at `62bdc2cf`". OA-2 and OA-3 cite OA-1 r4 and OA-2 r3/r4, but these landed in the same merge, not already on `main` | differs |
 | 2: "provenance, assumptions, status and limitations are stated accurately" | Accepted blob and SHA-256, review trail, authority quoted with author and time, item 8 table, source drift, superseded lines, evidence tags, "Not established"/"Open" lists; independent confirmation and ChatGPT 5888322900 checked them | meets; exceeds in form (drift, superseded lines, `OBJECTS.md`) |
-| 2: "Work that meets none of these conditions stays on its branch" | Landed on the basis "supports the claim above" | differs, unless that basis is read into one of the three conditions (§4) |
-| 4: stated status | "paper-level research findings, … not adopted", evidence tags [W], [RW], [P], [K], [R] | meets |
+| 2: "§A.42 item 5 and §A.28 govern what is added" (§A.42 item 5: "Only what a surviving claim needs is retained.") | Not cited in the four notes | met on R-a if the record's own scoped claim is the surviving claim; otherwise as row 1 |
+| 2: "Work that meets none of these conditions stays on its branch …" | Landed on the basis "supports the claim above" | differs, unless that basis is read into one of the three conditions (§4) |
+| 4: stated status | "paper-level research findings, … not adopted", evidence tags [W], [RW], [P], [K], [R] (OA-1 to OA-3; W1-1 states its layers in words) | meets |
 | 4: accountable Issue | #1169 (OA-1–3), #1245 (W1-1), in each note | meets |
-| 4: remediation plan | No remediation entry in the four notes; open items are listed as "Open" or "Not established" without a plan. A text search of the bodies of #1169 and #1245 finds none (their comments were not searched) | differs |
+| 4: remediation plan | No remediation entry in the four notes; open items are listed as "Open" or "Not established" without a plan. A text search of the bodies of #1169 and #1245 finds none, nor does any comment on either Issue that names OA-1 to OA-3 or W1-1 | differs |
 | 4: four-way split | Expressed by evidence tags and "Not established"/"Open" lists, not in the four named categories; no known-invalid result is stated | differs in form |
 | 1: landing does not establish | "not adopted", "No claim is promoted", "bounded evidence retention". The section heading in all four notes reads "What the record establishes"; for #1274's proposed note, REVIEW-r1 F7 renamed the same heading "What the record supports, and at what strength" | meets in substance; differs in one heading |
 
@@ -84,48 +100,66 @@
 - **(R-a) Own-claim support.** Item 2's "needed … to support records already on `main`" covers a
   record that lands as the evidence for its own scoped claim, stated in a status note landing with
   it, provided item 4's apparatus is present. The reading takes "already on `main`" to include a
-  record landing in the same merge; on it, the last sentence of item 2 excludes only work with no
-  status note stating a claim. A variant reads "needed for reproducibility" as reproducibility of
-  the record's own result (the "reproducibility basis" of review 5898122286).
+  record landing in the same merge; on it, item 2's "Work that meets none of these conditions …"
+  sentence excludes only work with no status note stating a claim. §A.42 item 8 closes a support gap
+  "no later than the record lands", by landing the content the claim needs, so support landing in
+  the same merge as its dependent is contemplated there; it does not supply the dependent record's
+  own basis. A variant reads "needed for reproducibility" as reproducibility of the record's own
+  result (the "reproducibility basis" of review 5898122286).
 - **(R-b) Exclusive conditions.** Item 2's three conditions are exclusive, and a #1265-style landing
   needs a recorded owner exception per record. Item 2 names no exception procedure; the only owner
   exception §A.46 names is §A.42 item 8's, which concerns off-`main` support and leaves the claim not
   established (item 1).
+- **(R-b′) Merge decision as the exception.** A variant of R-b takes the recorded owner merge
+  decision each landing already needs (§A.45 rule 7, "**Integrate:** reviewed work enters `main`
+  with its scientific scope preserved") as that exception, where the decision says so; the #1265
+  merge record (c.6848447181) names no exception.
 - **(R-c) Amendment.** §A.46 is amended to state the practice. That needs separate owner approval
   and is not proposed here.
 - **(R-d) First clause through item 1.** The scoped claim, at its stated strength, is an
   established claim once on `main`, so item 2's first condition applies (the batch-1 wording; the
-  form in which IA2 §6 and OQ-10 put the question). It turns on whether independent model review of
-  a paper derivation meets item 1's "verification standard for its kind"; review 5895564670 on #1274
-  states that model ACCEPT is not verification, and §A.46 item 7 bars unverified premises.
+  form in which IA2 §6 puts the question it refers to OQ-10). It turns on whether independent model
+  review of a paper derivation meets item 1's "verification standard for its kind"; review 5895564670 on #1274
+  states "An ACCEPT by a model is not independent mathematical verification (§A.46)"; §A.46 item 7
+  requires independent validation of each material premise of an established claim, and the OA-1,
+  OA-2 and OA-3 claims state that they rest "partly on research records not independently
+  established".
 
 Review 5898122286 states the constraint common to all of them: "precedent alone is not a blanket
 waiver of §A.46. Accepting the planning packet does not choose that basis."
 
-**Consequences for the nine candidates** (dispositions from IA2 §5; "gates" are IA2 §4's other
-conditions: item 8 gaps, reviews, CI, a separate owner merge decision):
+**Consequences for the nine candidates** (dispositions from IA2 §0, §3 and §5; "gates" are IA2
+§4's other conditions: item 8 gaps, reviews, CI, a separate owner merge decision):
 
-| PR | IA2 §5 | R-a | R-b | R-d |
+| PR | IA2 | R-a | R-b | R-d |
 |---|---|---|---|---|
 | #1274 | ready after `STATUS.md` | lands after gates; note already specifies item 4 | needs an exception | qualifies only if model-reviewed [A] arguments meet item 1; its off-`main` inputs are named conditions |
-| #1275 | wait (unit 2(a), OQ-6) | lands after gates; status note needs a remediation entry | needs an exception | as #1274; no item 8 gap for unit 1 |
-| #1269 | wait for preparation (SC-42, two gaps) | as #1275 | needs an exception | only after the BRIDGE-UNIT1 and QPHEN r5 gaps are landed or narrowed to named hypotheses |
-| #1268 | wait (#1267, #1214 gaps) | as #1275 | needs an exception | as #1269, for #1267 and #1214 |
-| #1272 | wait (#1268, #1267) | as #1275 | needs an exception | as #1269 |
-| #1273 | wait (#1231, #1232, #1269) | as #1275 | needs an exception | as #1269 |
-| #1276 | wait, last | as #1275; ranking per OQ-11 | needs an exception | as #1269 |
+| #1275 | wait (unit 2(a), OQ-6) | lands after gates | needs an exception | as #1274; no item 8 gap for unit 1; unit 2(a) not yet traced (IA2 §3), under option (a) |
+| #1269 | wait for preparation (SC-42, two gaps) | lands after gates | needs an exception | only after the BRIDGE-UNIT1 and QPHEN r5 gaps are landed or narrowed to named hypotheses |
+| #1268 | wait (#1267, #1214 gaps) | lands after gates | needs an exception | as #1269, for #1267 and #1214 |
+| #1272 | wait (#1268, #1267) | lands after gates | needs an exception | as #1269 |
+| #1273 | wait (#1231, #1232, #1269) | lands after gates | needs an exception | as #1269 |
+| #1276 | wait, last | lands after gates; ranking per OQ-11 | needs an exception | as #1269 |
 | #1271 | stays on branch | stays (item 8 gap; option (c)); "would qualify" per IA2 §3 | stays | stays |
 | #1270 | split: qc22 stays; QPHEN waits for #1219 except four files; EOI per OQ-8 | as IA2 | each part needs an exception; qc22 stays (§A.42 item 5) | as R-b, since no part has a reviewed claim |
 
-Under R-c, until an amendment is approved the nine stand under whichever of R-a, R-b or R-d governs
-the present text; after one, they stand under its terms. Under R-d, if model review does not meet
-item 1, the column reduces to R-b. Under R-a, the remediation entry the assessment specifies only for
-#1274 would be needed in each status note.
-
-Two further consequences fall outside the nine. Under R-b or R-d, the "Basis" lines of the four
-#1265 notes (and, under R-b, of the batch-1 notes) name a basis the text would not provide; item 6
-makes no removal automatic, and a mutable note is corrected in place (§A.27, §A.30). Under any
-reading, IA2 §6 records that #1268's AW-P0-2 bears on OA-2 E(b) step 4 and OA-3 N4.3 step 4, which
+Under R-c, until an amendment is approved the nine stand under whichever of R-a, R-b, R-b′ or R-d
+governs the present text; after one, they stand under its terms. Under R-d, if model review does not meet
+item 1, the column reduces to R-b. Under R-b′, the R-b column reads: lands after gates, with
+the exception recorded in the merge decision. Item 4 applies to any landed claim whose
+verification is incomplete, whatever its basis: IA2 specifies its remediation entry and
+verification-status split only for #1274 (§4 step 1); steps 2–7 list neither (owner question 2).
+
+Two further consequences fall outside the nine. Under R-b, R-b′ or R-d, the "Basis" lines of the
+four #1265 notes (and, under R-b or R-b′, of the batch-1 notes) name a basis the text would not provide; item 6
+makes no removal automatic ("Removal of research evidence from `main` is never automatic") and, for
+material that has not met the verification standard for its specific claims, makes "the normal
+proposed disposition … removal from the current tree *if the audit establishes that it is
+unnecessary*", after that audit and separate owner authorization; a mutable note is corrected in
+place (§A.27, §A.30). Under R-d, if model review meets item 1, those records are verified evidence,
+which item 6 keeps on `main`.
+
+Under any reading, IA2 §6 records that #1268's AW-P0-2 bears on OA-2 E(b) step 4 and OA-3 N4.3 step 4, which
 are now on `main`; if that finding were accepted into their status notes, the #1268 evidence for it
 would be "needed … to support records already on `main`" on the literal text. No such acceptance is
 recorded, and IA2 does not use it as a basis.
@@ -135,13 +169,19 @@
 1. For a model-reviewed, paper-only research record that no established claim and no record already
    on `main` needs, which basis does §A.46 item 2 as it stands provide: R-a (support of its own
    scoped claim, with item 4's apparatus), R-d (its scoped claim counts as established under
-   item 1), or none, so that each landing needs a recorded owner exception (R-b)? Or is the practice
-   to be written into §A.46 by a separately approved amendment (R-c)?
+   item 1), or none, so that each landing needs a recorded owner exception (R-b), and, if so, may
+   the recorded owner merge decision itself be that exception (R-b′)? Or is the practice to be
+   written into §A.46 by a separately approved amendment (R-c)?
 2. Whatever the answer, does item 4's remediation plan apply to such a record's status note? The
    four #1265 notes carry a status and an accountable Issue but no remediation entry.
 3. Does the ruling apply to the "Basis" lines of records already on `main` (the four #1265 notes and
-   the batch-1 notes), or only to later landings?
-
-No recommendation follows from the text alone: R-a and R-d each make the last sentence of item 2
-satisfiable by the landing itself, and R-b rests on that sentence, which #1097 marked "For the owner to
-confirm" before it merged.
+   the batch-1 notes), or only to later landings? Under R-b or R-b′, the four #1265 records, being
+   model-reviewed and needed by no established claim, fall within item 6's audit, whose normal
+   proposed disposition for material that has not met the verification standard is removal if the
+   audit establishes that it is unnecessary. Under R-a, whether a record's own scoped claim is a
+   "surviving claim" for that audit is the question of the §A.42 item 5 row in §3. Under R-d with
+   model review meeting item 1, item 6 keeps them as verified evidence.
+
+No recommendation follows from the text alone: R-a and R-d each make item 2's "Work that meets
+none of these conditions …" sentence satisfiable by the landing itself, and R-b rests on that
+sentence.
```
