# Independent review of REC-1 r8 (forward fix of three r7 passages under the literal L reading)

**Verdict: ACCEPT.** None of the required changes falls within the owner's three-passage scope.
Exactly the three r7 passages that contradict the L reading are corrected, and each correction is
right. The added L-reading sentence is correctly cited, and its inference holds. The diff contains
nothing else, and NOTES-r8 describes it exactly. Two of the writer's flagged issues, (a) and (b),
are separate items for the owner. Neither needs a fix inside this revision. Flagged issues (c) and
(d) need no action.

**Object.** Branch `research/rec-1-1169-20261113`, fetched by name with full history. Head
`4b81298f6f21268b03642ee5709861a6695ff8a8`, a single-parent child of `cd38655c`. I reviewed it in a
detached worktree and confirmed HEAD. The directory is
`verification/programmes/oi-qm/reconstruction/drafts/rec-1-20261113/`.

**Authority read.** I read #1268 c.6860582570 (`amaybaum`, 2026-11-13T17:47:34Z, "Adopt L; write r8
fix (Recommended)") and #1268 review 5892912758 (at `cd38655c`). I also read #1169 c.6854241002
(`amaybaum`, 2026-11-13T13:24:47Z, the P0 authorization), REC-1-P0-r3.md (§6, N3, N4, N7) and
REC-1-P0-CONFIRM-r3.md. For the sources at `c3b5f37a` on `main`, I checked that the OA2 blob is
`8f8ddf73` and the OA3 blob is `0a36fd05`.

**Checks run** (from the worktree root, at the head):
- `tools/claims_check.py`: OK.
- `tools/staleness_check.py`: OK (13 matched).
- `tools/voice_check.py`: OK.
- `tools/artifact_placement_check.py`: OK (self-test passed).
- `tools/legacy_records_check.py 4b81298f…`: 303 records intact.

All exit 0.

***

## Findings

### 1. The three passages: complete and correct [no defect]

- **Evidence.** I searched REC-1-r7.md for `compos`, `retent`, `retain`, `partial`, `residual`,
  `herald`, `held-at-use`, `noncomposable` and `refine`.
  - Only three hits place heralds that cannot be composed, or a residual named by herald retention,
    inside OBL-SP's own content:
    - r7:289–290 (open-content bullet);
    - r7:299–300 ("herald-retention residual");
    - r7:320–321 (P0 prerequisite example).
  - These are the three passages that P0-r3 §6 names and that the owner decision targets.
- **The other hits are consistent with L:**
  - r7:255–256, the clause L reads;
  - r7:285 and :288–289, the prefix-length cases;
  - r7:293 and :311, the herald typing carried as a scope hypothesis;
  - r7:333–334, "residual investigation", conditional on exhibited preparations;
  - r7:352, control (iii), which depends on the typing and not on retention;
  - r7:363–366, where "other … record classes (C6, C7)" already places partial-retention observers
    outside the class;
  - row 16, where "partial" refers to OA-1 D8 records, which are unrelated;
  - rows 14, 28, 29, C5–C7, §3.1 and §3.2, general interface statements that are not about OBL-SP's
    class.
- **The corrections.**
  - **r8:291–303.** The noncomposable item is removed from the open-content list. The typing fact is
    kept with its citations, and the L reading and the scope sentence are added. "This residual"
    keeps its antecedent.
  - **r8:309–310.** The residual is now named as "the preparations P0 lists as outside the coset
    form". This matches r8:291–292 and r8:329–331.
  - **r8:330.** The example is deleted, and the instruction to record out-of-form preparations is
    kept.

  None of the corrections changes a decision rule, outcome, control or bearing.
- **Fix.** None.

### 2. The added L-reading sentence: citations correct, inference valid [no defect; one remark]

- **Citations (OA2, OA3 at `c3b5f37a`).**
  - OA2:502 is the (H4) row: "Within the horizon, the held record at the latest read determines
    every earlier available read." OA2:804 confirms the nested form: "the held record is the `V`
    history up to the horizon".
  - OA3:120–123 is the (V-ii-H) definition: "heralded composites `e∘π` (herald at earlier ticks, then
    read) are available subnormalized effects".
  - OA3:474–475 says that under held-at-use herald typing "that class is itself retention-type".
- **Inference.** Each branch implies full retention.
  - (H4) gives full retention in `V` directly.
  - (V-ii-H) quantifies over herald ticks: any earlier ticks, then a read. Under held-at-use typing
    (OA3:411–414, cited in the preceding sentence as OA3:410–416), every such herald must be held at
    the read. So every read of the horizon is retained in `V`.

  It follows that no earlier herald's record is unheld at use. So heralds that are noncomposable
  for that reason cannot arise. The step is one direction only: class ⇒ full retention. The
  sentence "Observers that retain only some reads are not in the class" is its contrapositive. No
  converse and no equivalence is claimed (§A.34). This matches P0-r3 N3, the review's "implies full
  retention", and owner item 3.
- **Remark (Info, no fix).** OA3:474–475 alone says only "retention-type". The "every read" strength
  comes from OA3:120–123's quantification together with the held-at-use typing, and the sentence
  cites both. Full retention is sufficient for the conclusion, not necessary. P0-r3 N3 shows that at
  a fixed use time, heralds compose for any H-AR observer. The "so" in r8:301 asserts only the
  sufficient direction, which is valid.
- **Fix.** None.

### 3. Scope of the diff; NOTES fidelity [no defect]

- **Evidence.**
  - `git diff --stat cd38655c 4b81298f` adds exactly two files, `REC-1-r8.md` and `REC-1-NOTES-r8.md`.
  - `REC-1-r7.md` is unchanged: blob `f1ffac0e…` both at `f0757fdb` and at the head.
  - `diff -u REC-1-r7.md REC-1-r8.md` has 4 hunks, 8 lines removed, 17 added and 60 lines in all:
    the title, the Revision sentence, changes 1 and 2 (one hunk), and change 3.
  - r7:291–293 are byte-identical to r8:294–296.
  - No result, verdict, classification, proof or control changed.
- **NOTES checks.**
  - NOTES-r8's embedded diff matches the actual diff line for line.
  - The sha256 values are correct: r7 `c25ec1ff…`, r8 `7d123ae2…`.
  - The r8 blob is `615b7de8`, as stated.
  - The line counts (454 and 463) are correct.
  - Every r7 and r8 line reference in NOTES §1–§4 resolves to the text it describes, including
    r7:254–256, :288–289, :307–309, :311, :333–334, :352, :358 and :366, and r8:293, :309–310,
    :330 and :367.
- **Fix.** None.

### 4. The writer's four flagged issues

**(a) No §6 row for the Revision sentence's references.** Severity: Low.
- **Location.** r8:14–18; §6 at r8:427–463.
- **Evidence.** The new Revision sentence cites four references: #1268 c.6860582570, review
  5892912758, `REC-1-P0-r3.md` at `cd38655c`, and r7 at `f0757fdb`. Under §A.42 item 8 each one is
  provenance.
  - The added §4 sentence rests on OA2:502 and OA3:120–123, :474–475, which are on `main`.
  - The owner decision is quoted with its author and time (§A.42 item 7).
  - P0-r3 is not used as support.

  The gap predates r8. §6 already lacks rows for the r2–r7 Revision-line references (reviews
  5890763675 and 5890968976; `b39e40ff`, `1fd0c241`, `c73e855f`, `6de32c95`, `1ab6371b`) and for
  the C12 citation of review 5890763675. Only the r1 row (r8:460) exists. Item 8 applies before a
  record lands, and r8:462–463 already bars landing while gaps remain.
- **Disposition.** This is a separate item for the owner, not a fix within the three-passage scope.
  Close it before landing, together with the earlier Revision-line references.
- **Proposed row**, if the owner widens the scope:
  `| #1268 c.6860582570 (owner decision, quoted); #1268 reviews 5890763675, 5890968976, 5892912758; REC-1-r2…r7 and REC-1-P0-r3.md at their cited commits on this branch | revision line (header); C12 | Provenance; no claim rests on them (the §4 reading rests on OA2:502, OA3:120–123, :474–475 on main). |`

**(b) P5 and §5 item 1 say "not authorized".** Severity: Low.
- **Location.** r8:367; r8:410–415.
- **Evidence.**
  - P5 reads "Owner authorization of a paper-only unit; none exists."
  - r7 was committed at `f0757fdb` (2026-11-13T12:42:13Z), before #1169 c.6854241002
    (2026-11-13T13:24:47Z) authorized "REC-1 P0 (supporting; #1268, REC-1 r7 §4)". So r7's P5 was
    accurate when it was written.
  - r8 was committed at 17:53:45Z and carries the same sentence, which is stale for P0.
  - §5 item 1 ("authorization: not authorized") proposes an Issue record for OBL-SP as a whole.
    c.6854241002 authorizes only the P0 unit, so item 1 remains accurate.
  - Neither passage contradicts the L reading.
- **Disposition.** This is a separate item for the owner. Correcting it widens r8 beyond the owner's
  three-passage scope. §5 item 1 needs no change.
- **Exact text, if authorized.** Replace r8:367
  `- P5. Owner authorization of a paper-only unit; none exists.` with
  `- P5. Owner authorization of a paper-only unit: P0 is authorized by #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z); no other unit is authorized.`

**(c) "heralds on prefixes of several lengths" is kept.** Severity: none.
- **Location.** r8:291–293.
- **Evidence.**
  - P0-r3 N4 places these preparations inside the coset form. They are padded to `t_p` and refined
    by `J*`, and N3 shows that `J*` exists for every H-AR observer, retaining or not. So the finding
    does not depend on the L reading, and the passage does not contradict L.
  - The bullet is conditional on a P0 pass ("If P0 passes on that fragment"), and P0 is O-U. The
    anticipation is therefore not triggered.
  - Rewriting it from P0's result would import an outcome into the preregistration.
- **Disposition.** Keep it, as the writer did. Whether to reconcile the preregistered anticipation
  with P0-r3 N4 is a separate question for the owner, if it is ever needed.

**(d) The added reading is itself unreviewed.** Severity: none.
- **Location.** r8:297–303.
- **Evidence.**
  - The sentence is labelled [W, REC-1; unreviewed], which is accurate before this review.
  - It is not used as a premise of any established claim (§A.46 item 7).
  - Finding 2 checks it and finds it correct.
- **Disposition.** No fix within scope. The label can stay until the owner accepts the review and
  the ChatGPT exact-head review is complete. Changing it then is a later revision, not part of r8.

### 5. Register and process [no defect; one cosmetic note]

- **No self-narration in the r8 body.** The 17 added lines contain none of these phrases: "formerly",
  "no longer", "is now", "current form", "corrected", "withdrawn", "earlier revision", "should not",
  "reader". They also contain no ALL-CAPS emphasis.
- **The Revision paragraph** (r8:14–18) follows the header convention this record has used for every
  revision since r2. It is a status statement in the record's own idiom. It is not body prose.
- **No new premise.** The added sentence states the reading the owner adopted for an existing clause.
- **Directions.** The two directions are kept separate (finding 2).
- **Barred path strings.** None appear in r8 or NOTES-r8.
- **Cosmetic note (Info, no fix).**
  - r8:293 is a short source line, "grows. This".
  - r8:310 and r8:330 are over-long source lines.
  - All three render as continuous text, NOTES acknowledges r8:293, and r7 already has long lines
    (for example r7:285 and :311).
