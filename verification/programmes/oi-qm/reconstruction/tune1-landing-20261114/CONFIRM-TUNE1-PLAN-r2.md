# Focused confirmation r2: TUNE-1 landing plan (#1236)

**Object.** Branch `records/tune1-landing-plan-1236-20261114` at
`7c34657d92850a29bc64ca9a74e52cf4a85090c8`, which equals the remote head (`git ls-remote`). Its
parent `75c8df16` adds review r1. I read the diff from `00d1861a` for `LANDING-PLAN.md` (LP),
`STATUS-STEP3A.md` (S3A), `STATUS-SOURCING.md` (SSRC) and `NOTES-PLAN.md` (NP), together with
`RESPONSE-TUNE1-PLAN-r1.md`. I also read both STATUS notes in full. Line numbers are at `7c34657d`.

**Reviewer.** The author of review r1. Read-only. No computation on any OI rule, and no write to
the repository or the host. This confirmation is not verification (§A.46 item 7), and it authorizes
nothing.

**Review file.** `REVIEW-TUNE1-PLAN-r1.md` at `75c8df16` is byte-identical to the review as
written (`cmp`), and `7c34657d` leaves it unchanged.

## Verdict: ACCEPT WITH CHANGES (minor)

All 28 findings of r1 are applied at the lines the response cites: B1–B3, S1–S15 and N1–N10. The
OQ-9 deviation is right; it corrects an error in r1's wording. Nothing blocks.

Four should-fix items remain, C1–C4:
- C1 and C2 come from the revision itself.
- C3 is a stale passage in NP that the revision did not propagate to.
- C4 concerns the line references in the OQ-9 listing.

There are also four nits, C5–C8.

***

## 1. Resolution of each finding

| Finding | Resolved? | Checked at |
|---|---|---|
| B1 | Yes; see §3. | S3A:3, :162–167, :182, :224–252; SSRC:3, :175–179, :208, :234–255; LP:425–428 |
| B2 | Yes; see §4. | S3A:59–84; SSRC:49–77 |
| B3 | Yes; see §4. | S3A:93–100; SSRC:84, :191 |
| S1 | Yes. 323–326 and 415–416 are given, with the change-map lines. OA3:801 is dropped. The D1 recheck item is stated as listed in the change map but not named by #1284. | LP:155–161, :214–215; S3A:175 |
| S2 | Yes. The column is renamed. Inferred grades are marked, and LP:218–219 states that they are the plan's reading. | LP:203–219; S3A:174 |
| S3 | Yes in LP and SSRC. NP's decision 4 is stale (C3). | SSRC:192; LP:136, :402 |
| S4 | Yes. #1278 is moved out of "Current evidence". | LP:272–274; SSRC:162–169, :198 |
| S5 | Yes. The phrase "minimum-cost" no longer appears in the directory. | SSRC:7–9; LP:249 |
| S6 | Yes. | LP:134, :248; SSRC:43, :62 |
| S7 | Yes. The tables are organized by the five conditions, and authority is recorded as provenance. | LP:457–470; S3A:234–252; SSRC:240–255 |
| S8 | Yes. Both notes read "in this note as landed". G2 (v′) and the G3 forward note are added. The STATUS notes contain no `<…>` placeholder. One residual tension is C1. | LP:68–69; S3A:231–258; SSRC:236–261 |
| S9 | Yes in LP. NP's decision 1 is stale (C3), and LP §7 has a related stale cell (C2). | LP:67–68, :420 |
| S10 | Yes. | LP:68 (iv), :351–355, :386, :406, :482; S3A:180; SSRC:194 |
| S11 | Yes. Every listed line carries what the bullet says. The ten SRC tag lines are exactly the [R-off] tags on 3A citations: line 143 carries both a 3A tag and a REC tag, and the bullet is scoped to Step 3A citations. | S3A:209–218; SSRC:217–222 |
| S12 | Yes. | S3A:103–105; SSRC:92–93; LP:164–166; NP OQ-3 |
| S13 | Yes. | LP:39; NP:35–38 |
| S14 | Yes. | SSRC:108–111 |
| S15 | Yes. | NP:88–100; S3A:240–245; LP:438 |
| N1–N10 | Yes, each at the line the response cites. I checked N2's count of 19 `3A:` lines at r9. | as listed in the response |

## 2. The OQ-9 deviation

**Accepted.** In r1 I asked the note to name "the seventh-item wording". That was wrong. 3A's seven
qualifying items (3A:913–931) do not cite the second guidance message. Item 5 (3A:921–922) cites
T2(d), and T2(d) cites the message at 3A:866 ("owner guidance, second message, item 1, relay only").
The writer's listing is right in substance. Its line references need tightening (C4).

## 3. B1: are the STATUS notes self-contained?

Yes. In S3A and SSRC at `7c34657d`, a search for `LANDING-PLAN`, `NOTES-PLAN`, `OQ-`,
`REVIEW-TUNE1`, `RESPONSE-TUNE1`, `tune1-landing` and `<` followed by a letter returns no hit.

The two-gap reasoning is now stated in each note: S3A:160–166 and SSRC:175–179. The SSRC version
cites F-S2 and AW-SRC-2 on SRC:342–345. The tracing is in each note's own Dependencies table.

LP:425 adds the plan-files row, and LP:427–428 corrects the closing sentence. The occurrences of
"This plan authorizes no work" (S3A:127; SSRC:122) refer to the remediation plan, as in #1284's
notes. They do not cite the landing plan.

## 4. B2 and B3: hypotheses and ledger typing

**B2.** S3A:59–84 and SSRC:49–77 are my r1 replacement text verbatim. I re-read each against its
source.

S3A against 3A:
- the four classes and their hypotheses: 3A:212–215 and :1010–1013;
- "in the records read": 3A:1054–1058;
- the groups as re-read: 3A:413–420;
- the E(b) hypotheses (3A:579, :591–597) and "if that result holds" (3A:924);
- (SP) undecided, and T1 open at [L] level: 3A:597–606;
- B and the exchange rows outside E(b), and D unclassified: 3A:662, :771–774.

SSRC against SRC:
- the definition of TC-A: SRC:105–116, :139;
- "in the order (a)–(f)": SRC:146–147;
- the three measure clauses: SRC:239–255 and :282–287, with N3.1's unconditional reading as in
  5892912253;
- the search scope: SRC:403–407;
- the schema and "necessary only": SRC:330–345, matching 5892912253's wording;
- F-S1's proviso: SRC:207–209;
- (e): SRC:380–381.

**B3.** S3A:93–100 now matches 3A:1014–1016, :501 and F-3A-3 (3A:987–989). SSRC:84 and :191 state
the other record's typing and keep each record's own.

## 5. New text: anything wrong or stronger than its source?

Nothing in the revision is stronger than its source. Four should-fix items need attention, C1–C4,
and there are four nits, C5–C8.

**C1 (should-fix). As landed, S3A:186 and SSRC:200 contradict their own Basis lines.** The
Dependencies rows state "#1283 is adopted and #1284 is landed before this note lands". The Basis
lines say the basis "is open until #1283 is adopted. Until then reading R-b is in force" (S3A:230–234;
SSRC:236–240). After G0, the Basis line is false; before G0, the Dependencies row is. G2 (v′)
restates only the Basis. S3A:182 has the same problem: it still offers options (a) and (b), where the
landed note must record the decision taken.

*Replacement* for S3A:186 and SSRC:200: "Landing requires #1283's adoption and #1284's landing
first (gates G0 and G1); at packaging this row and the Basis line are restated against the adopted
text and the landed notes."

*Replacement* for LP:68 (v′): "each Basis line, the #1283/#1284 Dependencies row and, in the Step 3A
note, the objects-file row restated against the adopted item 8, the landed #1284 notes and the §A.42
item 3 decision, quoting the adoption record".

**C2 (should-fix). LP:438, last column, still shows the plan's non-author review as pending.** It
reads "**pending**: one independent non-author review of the complete plan". That review is
`REVIEW-TUNE1-PLAN-r1.md` at `75c8df16`, and this file is its confirmation. LP:439's "after the
non-author review" is now satisfied.

*Replacement* for the LP:438 cell: "`REVIEW-TUNE1-PLAN-r1.md` (`75c8df16`): ACCEPT WITH CHANGES; all
findings applied at `7c34657d` (`RESPONSE-TUNE1-PLAN-r1.md`); `CONFIRM-TUNE1-PLAN-r2.md`: ACCEPT WITH
CHANGES (minor)". For the LP:439 cell: "**pending**: ChatGPT exact-head review of the plan; the
package head needs its own at G2".

**C3 (should-fix). NP's "Decisions taken in the plan" predate the revision.** Four entries still
describe r1:
- NP:56 says "#1284 recommended next", against S9.
- NP:64–66 says C6 and C9 were narrowed "to the content on `main` (OA1:563–564; NPS1:85)", against
  S3.
- NP:67–69 says "graded as #1284 grades it" and gives "one line each … (OA3:323, :415)", against S1
  and S2.
- NP:72–73 says #1278 "leaves Gap P open for TC-A", where the notes now say "neither closes nor
  narrows".

*Replacement* for the four entries:
- NP:56: "#1284 next, required before the package for the notes as drafted".
- NP:65: "(OA1:563–564 for C6; OA1:106–107, :522 and :603 for C9, with NPS1:85 as a related
  concern)".
- NP:67–69: "Each OA statement the records use is graded as #1284 grades it or, where #1284 gives no
  grade, by the nearest graded result, marked as the plan's inference. None is known-invalid. Two cited
  OA-3 ranges contain delta-review text graded exploratory (OA3:323–326, :415–416); neither carries a
  TUNE-1 conclusion, and the notes say so."
- NP:72–73: "it concerns the binary SM ring and neither closes nor narrows Gap P for TC-A".

**C4 (should-fix). S3A:183's line references mix two passages and miss one.**
- "Nodes A.5–D.5; 3A:819–824" pairs node names with lines that belong to T1's reporting item
  "*Interference versus tables*", which runs 3A:819–823.
- The nodes are at 3A:583–588, :658, :696 and :751.
- 3A:519–522 also draws on the message: the persistent-incompleteness reading in §3.0, "That meets
  item 1 of the second guidance". No classification rests on it.

*Replacement* for the S3A:183 cell: "Provenance: not on #1236. T2(d) (3A:866), §5 item 5
(3A:921–922), which cites T2(d), §3.0's persistent-incompleteness reading (3A:519–522), T1's
reported interference-versus-tables item (3A:819–823) and Nodes A.5–D.5 (3A:583–588, :658, :696,
:751) draw on it; no classification does."

In LP:389, column 2, replace "T2(d); interference versus tables (A.5 and the like)" with the same
list. In NP:143–144 (reviewer side), add: "(r1's 'seventh-item wording' was an error; the
confirmation accepts the writer's list)".

**C5 (nit). SSRC:158–159 states the corpus negative without its scope.** It says "the corpus names it
only as …". The claim at SSRC:67 scopes the same negative. *Replacement:* "within the searches the
record states, the corpus names it only as …".

**C6 (nit). The third condition bullet says nothing about the landing checks.** At S3A:240–245 and
SSRC:245–248 the bullet names the reviews and the tracing but not the checks. r1's draft had "package
checks pending". *Replacement:* append "the landing checks are run at the package head (G2 (vi))"
before "In this note as landed".

**C7 (nit). The header lines need restating at packaging.** S3A:3 and SSRC:3 read "Draft for the
TUNE-1 package (the TUNE-1 preservation package, …)", which repeats itself, and "Draft" must not
survive landing. *Replacement:* in each note, write "Status note for the TUNE-1 preservation package
(#1236 comment 6873565446)". Add to LP:68 (iii): "with the headers stated as landed".

**C8 (nit). LP §6.3 (LP:416–425) lacks a row for review 5897621232,** which SSRC:168 and :198 now
cite. *Replacement:* in the #1278 row, write "#1278 at `d8b74527`, reviews 5897621232 and 5898054706,
…".

## 6. Owner-question recommendations in NP

They are recorded faithfully at NP:88–152. Each OQ gives the writer's line and the reviewer's line,
and the reviewer lines match r1's recommendations. The writer adopts the review on OQ-1, OQ-3 and
OQ-4, and the two sides agree on the rest. The only discrepancy is r1's own wording error on OQ-9,
which is handled by C4's added parenthesis. I add no new recommendation. OQ-9 now stands as: leave it
as provenance, with the note listing the passages in C4's replacement.
