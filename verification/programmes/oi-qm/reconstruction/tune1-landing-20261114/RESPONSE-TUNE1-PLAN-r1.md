# Response to the independent review r1 of the TUNE-1 landing plan (#1236)

Dispositions of `REVIEW-TUNE1-PLAN-r1.md` (ACCEPT WITH CHANGES, of the plan at `00d1861a`). Every
finding is applied in place, using the review's replacement text wherever it gives one. Nothing else
changes: no scientific conclusion, no input record, and no classification of either record. "LP",
"S3A", "SSRC" and "NP" are `LANDING-PLAN.md`, `STATUS-STEP3A.md`, `STATUS-SOURCING.md` and
`NOTES-PLAN.md`; their line numbers are those of r2, the revision these dispositions produce. The
review's line numbers are those of `00d1861a`. Paper-only; no computation on any OI rule.

## Blocking

| Finding | Disposition | Where (r2) | Diff summary |
|---|---|---|---|
| B1 | Applied as given. Neither STATUS note cites `LANDING-PLAN.md` or `NOTES-PLAN.md`. | S3A:3, :162–167, :182 (option text moved into the Dependencies row), :224, :227, :243, :248; SSRC:3, :177–179, :208, :234, :248; LP:425, :427–428 | "(`LANDING-PLAN.md` §5)" → "(the TUNE-1 preservation package, #1236 comment 6873565446)"; the two-gap sentence moved into each note (S3A with the review's text; SSRC with "(F-S2; AW-SRC-2, SRC:342–345)"); the §6 tracing citations replaced by "this note's Dependencies table"; the OQ-1 and OQ-2 citations replaced by the review's wording, with the two options for the objects file stated in S3A's Dependencies row; "Together" parentheses deleted; "(`LANDING-PLAN.md` §1, G2)" → "at packaging"; LP §6.3 gains the plan-files row, and LP's closing sentence names the remaining conditions. The S10 rows are added to both Dependencies tables (S10 below). |
| B2 | Applied as given. | S3A:59–84; SSRC:49–77 | Both "Claim supported by this record" sentences replaced verbatim by the review's text, carrying every hypothesis and scope limit it lists. |
| B3 | Applied as given. | S3A:93–100; SSRC:84, :191 | S3A's "Used but not stated" bullet replaced by the review's three-way typing (run repetition not stated; MP-0a-type supply unsourced; MP-0b-type complete history an imported convention, 3A:501) with the note on the sourcing unit's typing; SSRC's MP-0b hypothesis replaced by the review's text; SSRC's C6 row adds that Step 3A types the same history differently and each typing is that record's own. |

## Should-fix

| Finding | Disposition | Where (r2) | Diff summary |
|---|---|---|---|
| S1 | Applied as given. | LP:154–161, :214–215; S3A:175 | OA3:323 → OA3:323–326 (R1, O5 and the D1 recheck; OA3:813, :820, :823); OA3:415 → OA3:415–416 (R2, OA3:814); the D1 recheck is stated as listed in the change map, not graded by name in #1284; OA3:801 dropped; S3A's wording "delta-review text that the OA-3 status note grades exploratory". |
| S2 | Applied as given, with one added sentence marking the inferred grades. | LP:203, :207, :209, :212–213, :218–219; S3A:174 | Column renamed "Grade after #1284, or nearest graded result"; Corollary E1, setup, measure typing/target/R5 and OA-1 D1–D4 cells replaced by the review's text; a sentence after the table states that entries marked "the plan's inference", "not graded separately" or "definitions" are the plan's reading; S3A's OA row says "partially verified where the OA `STATUS.md` notes grade it, or else part of a partially verified record". |
| S3 | Applied as given. | SSRC:192; LP:136, :402 | The C9 narrowing now anchors on OA1:106–107, :522, :603; NPS1:85 is a related concern; REC C9 is context. C6 kept, with B3's note. |
| S4 | Applied as given. | LP:272–274; SSRC:162–170, :198 | LP: "reads SRC only as off-`main` context" → uses SRC as off-`main` support for its attributed comparison and conditional resource statements (NA `ASSESSMENT.md`:163; review 5897621232). SSRC: #1278 moved out of "Current evidence" into a "Related governance record (provenance, not evidence for this stop)" bullet ending with the review's text; its Dependencies row names both #1278 reviews and the use. |
| S5 | Applied as given. | SSRC:7–9; LP:249 | "not a minimum-cost proof" replaced by the scope 5892912253 gives. |
| S6 | Applied as given. | LP:134, :248; SSRC:43 | "excluded under μ-G" → "an unconditional supply excluded under μ-G (Lemma P-1); heralding is the only route there, at F-S2's cost for `r_O` and unavailable for the program blocks before use (SRC:244–246)". |
| S7 | Applied as given. | LP:457–468; S3A:231–252; SSRC:237–255 | Tables and bullet lists headed by item 8's five conditions; "landing checks and tracing" folded into the third; "explicit rationale" and "separate owner merge decision" merged as the fifth; historical authorization moved below as "Authority (provenance)"; LP's C2 sentence replaced by the review's text. |
| S8 | Applied with the Bell precedent's resolution ("in this note as landed"), with no placeholder. | S3A:231–235, :248–251, :256–258; SSRC:237–241, :248–252, :259–261; LP:68 (v′), :69 (G3) | Review and merge clauses read "In this note as landed, no package-level review [or merge decision] is recorded … quoted in the forward note added after landing"; each Basis adds the reading R-b sentence; LP G2 adds (v′) restating each Basis against the adopted item 8; LP G3 adds the forward note naming the reviewed package head, its reviews and the merge commit. |
| S9 | Applied as given. | LP:67, :68 (i), :420; S3A:186; SSRC:200 | G1 "Required before G2 for the notes as drafted"; G2 (i) "after G1"; LP §6.3 and both notes' #1283/#1284 rows state that #1283 is adopted and #1284 landed before the notes land. |
| S10 | Applied as given. | LP:68 (iv), :351–355, :386, :406, :482; S3A:180; SSRC:194 | LP §5.5 adds the review's paragraph on `9f7d2612` and `221754fc`; §6.1 and §6.2 add rows; G2 (iv) adds the existence check; §8 item 7 names both ids; both notes' Dependencies tables add the rows. |
| S11 | Applied. | S3A:209–219; SSRC:217–223 | S3A adds bullets for 3A:43, :186, the `REVIEW-STEP3A.md` citations at 3A:7, :10, :1052, :1076, :1106, :1154, and the reviewed-copy identifiers at 3A:5, :8–9. SSRC adds bullets for the tag definitions at SRC:88–90 and the [R-off] tags on Step 3A citations at SRC:101, :123, :129, :143, :157, :174, :280, :294, :326, :340 (each checked to carry the tag). |
| S12 | Applied as given. | SSRC:92–93; S3A:103–105; LP:164–166; NP OQ-3 | [R] premise lines added (SSRC: OBS Lemma P-1, OA-1 D1–D5 and D7; S3A: OA-2 E(a), OA-1 D5, P's D1–D7); LP §2.3 and OQ-3 name OBS. |
| S13 | Applied. | LP:39; NP:35–40 (sources read) | BL re-pinned at `3859c3ef`; the Bell plan's corrected Landing section and gate rows were read there and followed (S8, S7). |
| S14 | Applied as given. | SSRC:108–111 | Two Limitations bullets added (memory (e); spatial copies). |
| S15 | Applied as given. | NP OQ-1; S3A:243–247; LP:438 | The OQ-1 recommendation is the review's text; S3A and LP state that non-authorship is not established on the record. |

## Nits

| Finding | Disposition | Where (r2) | Diff summary |
|---|---|---|---|
| N1 | Applied. | NP:9 | "eleven" → "twelve". |
| N2 | Applied. | LP:76–77 | REC-1 cites 3A on 19 lines at r9 `3a3aa146` (checked); r7:215 and :217 kept as examples. |
| N3 | Applied as given. | LP:108; S3A:53 | Layer "[R] (Lemma A-T (a), (b); OA-2 E(a); OA-1 D5); the L5.6 reading [W], 3A:692". |
| N4 | Applied as given. | SSRC:152 | The μ-R row dropped; the review's sentence added below the table. |
| N5 | Applied. | LP:337–341 | #1265's abbreviation of five never-committed working-copy ids stated as the direct precedent. |
| N6 | Applied as given. | LP:258–259; SSRC:177–179 | "inside the schema" → the full schema description. |
| N7 | Applied. | S3A:148, :165–166 | "or an exhibited member" moved from the resolving-evidence cell to the gap paragraph, with the distinction the review states. |
| N8 | Applied as given. | LP:69 | Board changes remain unauthorized unless the owner authorizes them. |
| N9 | Applied (said so). | S3A:177 | The W1-1 row states the blob difference and that nothing turns on it. |
| N10 | Applied as given. | LP:134, :137 | "main" → "package; main" for SRC's N3.1 and N3.4 readings. |

## Owner-question recommendations

`NOTES-PLAN.md`'s owner questions now give the writer's recommendation and the review's side by side.
The writer adopts the review's recommendation on OQ-1, OQ-3 and OQ-4; the others agree.

**OQ-9 wording.** The review asks the note to name "the seventh-item wording" as drawing on the second
guidance message. 3A's seven qualifying items (3A:913–931) do not cite the message; item 5
(3A:921–922) cites T2(d), which does. S3A:183 therefore names T2(d) (3A:866), §5 item 5 and the
interference-versus-tables entries (Nodes A.5–D.5; 3A:819–824), which carry item 2 of that message.

## Checks

At the revised working tree: `tools/claims_check.py`, `tools/staleness_check.py`, `tools/voice_check.py`
and `tools/artifact_placement_check.py` report OK; `tools/legacy_records_check.py` reports 303 records
intact; the SC-42 integration check matches `sc42-integration-result.json` byte for byte with the
revised files included. No barred path term appears in this directory.

## Confirmation r2

Dispositions of `CONFIRM-TUNE1-PLAN-r2.md` (ACCEPT WITH CHANGES (minor), of the plan at `7c34657d`).
Each item is applied in place with the confirmation's replacement text verbatim, except where noted.
Line numbers are those of r3, the revision these dispositions produce. Nothing else changes.

| Item | Disposition | Where (r3) | Diff summary |
|---|---|---|---|
| C1 | Applied verbatim; the objects-file row is reworded to record the decision. | S3A:182, :186; SSRC:200; LP:68 (v′) | The #1283/#1284 Dependencies rows read "Landing requires #1283's adoption and #1284's landing first (gates G0 and G1); at packaging this row and the Basis line are restated against the adopted text and the landed notes." The confirmation gives no text for the objects-file row; it now states that the row records the owner's §A.42 item 3 decision taken at packaging (old and new blob where abbreviated, or the exception record), in place of the two options. G2 (v′) restates all three rows, with the confirmation's text. |
| C2 | Applied verbatim. | LP:438, :439 | The plan's non-author review cell names `REVIEW-TUNE1-PLAN-r1.md`, the response and this confirmation; the ChatGPT cell reads "**pending**: ChatGPT exact-head review of the plan; the package head needs its own at G2". |
| C3 | Applied verbatim. | NP:56, :63–66, :67–70, :73 | Decisions 1, 4, 5 and 6 restated to r2's content: #1284 required first; the C6 and C9 anchors; grades or nearest graded result, with OA3:323–326 and :415–416; #1278 "neither closes nor narrows Gap P". |
| C4 | Applied verbatim. | S3A:183; LP:389; NP:143–145 | The second-message passages are listed as T2(d) (3A:866), §5 item 5 (3A:921–922), §3.0's reading (3A:519–522), T1's reported item (3A:819–823) and Nodes A.5–D.5 (3A:583–588, :658, :696, :751); NP's reviewer line adds the parenthesis on r1's wording. |
| C5 | Applied verbatim. | SSRC:158–159 | "within the searches the record states, the corpus names it only as …". |
| C6 | Applied verbatim. | S3A:244; SSRC:248 | The third condition bullet adds "the landing checks are run at the package head (G2 (vi))" before "In this note as landed". |
| C7 | Applied verbatim. | S3A:3; SSRC:3; LP:68 (iii) | Headers read "Status note for the TUNE-1 preservation package (#1236 comment 6873565446)"; G2 (iii) adds "with the headers stated as landed". |
| C8 | Applied verbatim. | LP:421 | The §6.3 #1278 row names reviews 5897621232 and 5898054706. |

Checks at the revised working tree: claims, staleness, voice and artifact placement OK; legacy records
303 intact; SC-42 byte-equal to `sc42-integration-result.json`; no barred path term in this directory.
