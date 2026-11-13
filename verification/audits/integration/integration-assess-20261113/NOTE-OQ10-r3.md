# OQ-10: the #1265 landing practice and §A.46 items 1, 2 and 4 (r3)

**Standing.** Paper-only note for an owner ruling, written under #1169 c.6865177667 (`amaybaum`,
2026-11-13T21:19:31Z), OQ-10: "a short paper-only note on how the #1265 landing practice relates to
§A.46 items 1, 2 and 4, for an owner ruling. The note is not a waiver and does not edit AGENTS.md."
It grants no waiver or merge authority, chooses no reading, and changes no record or status.
r2 applies the findings of CONFIRM-OQ10 (ACCEPT WITH CHANGES, F1–F12).

**Pins.** `main` = `c3b5f37a` (the #1265 merge). Assessment r2, its review and confirmation:
`verification/audits/integration/integration-assess-20261113/` at `c7ce4f28` (IA2, REVIEW-r1,
CONFIRM-r2). ChatGPT review 5898122286 on #1279 at `c7ce4f28`.

## 1. The rules (AGENTS.md at `c3b5f37a`, verbatim)

> 1. **Established claims.** A claim is presented as established only when it can be verified from
> `main` and its evidence meets the verification standard for its kind (§A.42; the Code Review
> Rules, "Keep verification layers distinct"). A claim landed under an owner exception to §A.42
> item 2 (§A.42 item 8) is not established.
>
> 2. **What lands.** Research evidence may land on `main` when an established claim needs it, or when
> it is needed for reproducibility or to support records already on `main`, even if its programme
> is unfinished; its provenance, assumptions, status and limitations are stated accurately. Work
> that meets none of these conditions stays on its branch, tracked by its guiding pull request or
> Issue (§A.43). §A.42 item 5 and §A.28 govern what is added; item 6 governs removal.
>
> 4. **Unverified claims on `main`.** A claim on `main` whose verification is incomplete has a stated
> status, an accountable Issue and a remediation plan; a status label alone does not resolve a
> verification gap. Its record distinguishes independently verified, partially verified,
> exploratory and known-invalid results, in the record or, for a frozen record, in a mutable record
> on `main` that cites it; a status that contradicts the frozen record's own conclusion is a
> correction under item 5 (§A.42 item 6; §A.45 rule 1).

**History of item 2.** §A.46 was adopted 2026-11-04 ("Adopted 2026-11-04 by owner decision, after a
proposed removal of partially verified research records from `main` was found to break records on
`main` that depend on them. Amended the same day …"). Its first text (`0ad4bd0f`) let research
evidence "be kept on `main` whether or not its programme is complete". The conditions of item 2
entered with `be616ffc`; its "Work that meets none of these conditions …" sentence took its
present form in `e10a9ba2`. The #1097 PR
description, which merged them, marks that sentence "**For the owner to confirm:** this sentence comes
from the coordinator's proposal, which the owner approved. A reviewer suggested deleting it as an
addition; it is kept, reworded to match §A.43." The conditions follow the owner's adjustments
quoted in that description ("New research evidence may also land when it is needed for
reproducibility or to support existing records …"), given after the owner's concern "I am
concerned that Rule 2 will lead to more issues where main will contain unverified data." #1097 was
merged by `amaybaum` and has no comments; §A.46 was amended again the same day by owner decision
(`ab6211d7`, #1103), leaving item 2 unchanged.

Item 6, which item 2 names for removal, reads in part: "Removal of research evidence from `main` is
never automatic." … "Verified evidence, including verified negative and conditional results, is
kept on `main`. For other material that has not met the verification standard for its specific
claims, the normal proposed disposition is removal from the current tree *if the audit establishes
that it is unnecessary*: no surviving claim depends on it; …"

## 2. The practice (#1265, merged as `c3b5f37a`)

- **Owner record.** #1265 c.6846206075 (`amaybaum`, 2026-11-13T06:44:20Z): "Prepare after sequence
  (Recommended)" … "a landing package for this PR will be prepared, following the batch-1 pattern:
  one status note per unit (OA-1 r5, OA-2 r4, OA-3 r4, W1-1 r4) naming the claim it supports; an
  independent review; a ChatGPT ACCEPT at the exact head; green CI. It then lands only after a
  separate owner merge decision, as a merge commit."
- **Merge.** #1265 c.6848447181 (`amaybaum`, 2026-11-13T08:54:09Z): owner decision "Merge now
  (Recommended)"; "What landed: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4, as research records on their
  stated scope. No claim is promoted." ChatGPT review 5888322900 at the head `a965818e`: "ACCEPT for
  bounded evidence retention on `main` … **not** a new scientific proof, an upgrade of any [W]/[R]
  finding, human or kernel verification". The PR body reads "Not for merge" and "Landing: not
  authorized" and names head `2d064a71`, before the merged head; the merge decision is c.6848447181.
- **Stated basis.** Each of the four `STATUS.md` notes (`oi-qm/reconstruction/oa-{1,2,3}-20261112/`,
  `physical-realization/w1-1-20261112/`) states, in its "Landing" section: "**Basis.** §A.46 item 2: the record supports the claim
  above, at the strength stated. No record on `main` depends on it at `62bdc2cf`. The accountable
  Issue is #1169" (#1245 for W1-1). Each gives a "Claim supported by this record" in quotation, closing
  with its evidence layer (OA-1 to OA-3: "paper-level research findings: …; not adopted; no
  manuscript claim affected"; W1-1: "paper-level hand derivations with independent AI-agent reviews,
  not machine-checked; … no manuscript claim affected").
- **Batch-1 contrast.** The batch-1 notes the owner record points to state a different basis: "An
  established claim needs the record (§A.46 item 2): the claim above" (for example
  `native-preparation-source-1-20261110/STATUS.md`:87).

## 3. Mapping

| §A.46 clause | #1265 practice | Relation |
|---|---|---|
| 2: "an established claim needs it" | Not invoked; the notes say "not adopted", and the merge record "No claim is promoted" | differs (batch-1 invoked it) |
| 2: "needed for reproducibility" | Not invoked; paper-only, no computation | differs |
| 2: "to support records already on `main`" | Each note: "No record on `main` depends on it at `62bdc2cf`". OA-2 and OA-3 cite OA-1 r4 and OA-2 r3/r4, but these landed in the same merge, not already on `main` | differs |
| 2: "provenance, assumptions, status and limitations are stated accurately" | Accepted blob and SHA-256, review trail, authority quoted with author and time, item 8 table, source drift, superseded lines, evidence tags, "Not established"/"Open" lists; independent confirmation and ChatGPT 5888322900 checked them | meets; exceeds in form (drift, superseded lines, `OBJECTS.md`) |
| 2: "§A.42 item 5 and §A.28 govern what is added" (§A.42 item 5: "Only what a surviving claim needs is retained.") | Not cited in the four notes | met on R-a if the record's own scoped claim is the surviving claim; otherwise as row 1 |
| 2: "Work that meets none of these conditions stays on its branch …" | Landed on the basis "supports the claim above" | differs, unless that basis is read into one of the three conditions (§4) |
| 4: stated status | "paper-level research findings, … not adopted", evidence tags [W], [RW], [P], [K], [R] (OA-1 to OA-3; W1-1 states its layers in words) | meets |
| 4: accountable Issue | #1169 (OA-1–3), #1245 (W1-1), in each note | meets |
| 4: remediation plan | No remediation entry in the four notes; open items are listed as "Open" or "Not established" without a plan. A text search of the bodies of #1169 and #1245 finds none, nor does any comment on either Issue that names OA-1 to OA-3 or W1-1 | differs |
| 4: four-way split | Expressed by evidence tags and "Not established"/"Open" lists, not in the four named categories; no known-invalid result is stated | differs in form |
| 1: landing does not establish | "not adopted", "No claim is promoted", "bounded evidence retention". The section heading in all four notes reads "What the record establishes"; for #1274's proposed note, REVIEW-r1 F7 renamed the same heading "What the record supports, and at what strength" | meets in substance; differs in one heading |

The assessment's proposed #1274 note (IA2 §4 step 1) adds "Verification status (§A.46 item 4)" and
"Remediation, per gap (accountable Issue #1169)"; it therefore exceeds the #1265 notes on item 4.
Its steps 2–7 do not list a remediation entry.

## 4. Readings

- **(R-a) Own-claim support.** Item 2's "needed … to support records already on `main`" covers a
  record that lands as the evidence for its own scoped claim, stated in a status note landing with
  it, provided item 4's apparatus is present. The reading takes "already on `main`" to include a
  record landing in the same merge; on it, item 2's "Work that meets none of these conditions …"
  sentence excludes only work with no status note stating a claim. §A.42 item 8 closes a support gap
  "no later than the record lands", by landing the content the claim needs, so support landing in
  the same merge as its dependent is contemplated there; it does not supply the dependent record's
  own basis. A variant reads "needed for reproducibility" as reproducibility of the record's own
  result (the "reproducibility basis" of review 5898122286).
- **(R-b) Exclusive conditions.** Item 2's three conditions are exclusive, and a #1265-style landing
  needs a recorded owner exception per record. Item 2 names no exception procedure; the only owner
  exception §A.46 names is §A.42 item 8's, which concerns off-`main` support and leaves the claim not
  established (item 1).
- **(R-b′) Merge decision as the exception.** A variant of R-b takes the recorded owner merge
  decision each landing already needs (§A.45 rule 7, "**Integrate:** reviewed work enters `main`
  with its scientific scope preserved") as that exception, where the decision says so; the #1265
  merge record (c.6848447181) names no exception.
- **(R-c) Amendment.** §A.46 is amended to state the practice. That needs separate owner approval
  and is not proposed here.
- **(R-d) First clause through item 1.** The scoped claim, at its stated strength, is an
  established claim once on `main`, so item 2's first condition applies (the batch-1 wording; the
  form in which IA2 §6 puts the question it refers to OQ-10). It turns on whether independent model
  review of a paper derivation meets item 1's "verification standard for its kind"; review 5895564670 on #1274
  states "An ACCEPT by a model is not independent mathematical verification (§A.46)"; §A.46 item 7
  requires independent validation of each material premise of an established claim, and the OA-1,
  OA-2 and OA-3 claims state that they rest "partly on research records not independently
  established".

Review 5898122286 states the constraint common to all of them: "precedent alone is not a blanket
waiver of §A.46. Accepting the planning packet does not choose that basis."

**Consequences for the nine candidates** (dispositions from IA2 §0, §3 and §5; "gates" are IA2
§4's other conditions: item 8 gaps, reviews, CI, a separate owner merge decision):

| PR | IA2 | R-a | R-b | R-d |
|---|---|---|---|---|
| #1274 | ready after `STATUS.md` | lands after gates; note already specifies item 4 | needs an exception | qualifies only if model-reviewed [A] arguments meet item 1; its off-`main` inputs are named conditions |
| #1275 | wait (unit 2(a), OQ-6) | lands after gates | needs an exception | as #1274; no item 8 gap for unit 1; unit 2(a) not yet traced (IA2 §3), under option (a) |
| #1269 | wait for preparation (SC-42, two gaps) | lands after gates | needs an exception | only after the BRIDGE-UNIT1 and QPHEN r5 gaps are landed or narrowed to named hypotheses |
| #1268 | wait (#1267, #1214 gaps) | lands after gates | needs an exception | as #1269, for #1267 and #1214 |
| #1272 | wait (#1268, #1267) | lands after gates | needs an exception | as #1269 |
| #1273 | wait (#1231, #1232, #1269) | lands after gates | needs an exception | as #1269 |
| #1276 | wait, last | lands after gates; ranking per OQ-11 | needs an exception | as #1269 |
| #1271 | stays on branch | stays (item 8 gap; option (c)); "would qualify" per IA2 §3 | stays | stays |
| #1270 | split: qc22 stays; QPHEN waits for #1219 except four files; EOI per OQ-8 | as IA2 | each part needs an exception; qc22 stays (§A.42 item 5) | as R-b, since no part has a reviewed claim |

Under R-c, until an amendment is approved the nine stand under whichever of R-a, R-b, R-b′ or R-d
governs the present text; after one, they stand under its terms. Under R-d, if model review does not meet
item 1, the column reduces to R-b. Under R-b′, the R-b column reads: lands after gates, with
the exception recorded in the merge decision. Item 4 applies to any landed claim whose
verification is incomplete, whatever its basis: IA2 specifies its remediation entry and
verification-status split only for #1274 (§4 step 1); steps 2–7 list neither (owner question 2).

Two further consequences fall outside the nine. Under R-b, R-b′ or R-d, the "Basis" lines of the
four #1265 notes (and, under R-b or R-b′, of the batch-1 notes) name a basis the text would not provide; item 6
makes no removal automatic ("Removal of research evidence from `main` is never automatic") and, for
material that has not met the verification standard for its specific claims, makes "the normal
proposed disposition … removal from the current tree *if the audit establishes that it is
unnecessary*", after that audit and separate owner authorization; a mutable note is corrected in
place (§A.27, §A.30). Under R-d, if model review meets item 1 and, for OA-1 to OA-3, their [R] premises are independently validated (item 7), those records are verified evidence, which item 6 keeps on `main`.

Under any reading, IA2 §6 records that #1268's AW-P0-2 bears on OA-2 E(b) step 4 and OA-3 N4.3 step 4, which
are now on `main`; if that finding were accepted into their status notes, the #1268 evidence for it
would be "needed … to support records already on `main`" on the literal text. No such acceptance is
recorded, and IA2 does not use it as a basis.

## 5. The owner question

1. For a model-reviewed, paper-only research record that no established claim and no record already
   on `main` needs, which basis does §A.46 item 2 as it stands provide: R-a (support of its own
   scoped claim, with item 4's apparatus), R-d (its scoped claim counts as established under
   item 1), or none, so that each landing needs a recorded owner exception (R-b), and, if so, may
   the recorded owner merge decision itself be that exception (R-b′)? Or is the practice to be
   written into §A.46 by a separately approved amendment (R-c)?
2. Whatever the answer, does item 4's remediation plan apply to such a record's status note? The
   four #1265 notes carry a status and an accountable Issue but no remediation entry.
3. Does the ruling apply to the "Basis" lines of records already on `main` (the four #1265 notes and
   the batch-1 notes), or only to later landings? Under R-b or R-b′, the four #1265 records, being
   model-reviewed and needed by no established claim, fall within item 6's audit, whose normal
   proposed disposition for material that has not met the verification standard is removal if the
   audit establishes that it is unnecessary. Under R-a, whether a record's own scoped claim is a
   "surviving claim" for that audit is the question of the §A.42 item 5 row in §3. Under R-d with model review meeting item 1, and item 7's validation of OA-1 to OA-3's [R] premises, item 6 keeps them as verified evidence.

No recommendation follows from the text alone: R-a and R-d each make item 2's "Work that meets
none of these conditions …" sentence satisfiable by the landing itself, and R-b rests on that
sentence.
