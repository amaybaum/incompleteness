# Independent review r1: Bell support and ladder landing plan (#868)

**Object.** Branch `records/bell-landing-plan-868-20261114` at `ed61696db174c7e0a17be2fd8359c9fa8cb2c983`
(single commit on `main` = `c3b5f37a`), directory
`verification/programmes/oi-qm/reconstruction/bell-landing-20261114/`: `LANDING-PLAN.md` (LP),
`STATUS-BS.md` (SBS), `STATUS-SB-L3.md` (SL3), `STATUS-LADDER.md` (SLD), `NOTES-PLAN.md` (NP).
"LP:n" etc. are lines of those files at `ed61696d`.

**Reviewer.** A model reviewer that did not write the plan, the STATUS notes or any input record.
Paper-only: no computation on any OI rule, no probe replay, no CI, no write to the repository or
host. This review is not verification (§A.46 item 7) and authorizes nothing.

**Inputs read at their stated heads** (`git show <sha>:<path>`): BS `BELL-SCOPE-UNIT1.md` @ `e1534b08`
(blob `5814e479`); SB `SUBSTATE-BRIDGE-UNIT1.md` @ `86a413c8` (blob `9ff0f077`) and its r1 @
`b94b283a`; SB probe S5 @ `86a413c8`; QH `Q868H-UNIT1.md` @ `ffc9cda4` (blob `ebf5215b`), lines
60–100, 205–220; all twelve ladder files @ `d8e4f80e` (r3 in full, REVIEW-r1 lines 130–140 and
270–335, NOTES-r3, OBJECTS); OC `NEW-RESULTS.md` (blob `b0e930ab`) §5 and §7, `STATUS.md`,
`DEPENDENCIES.md`, `PROVENANCE.md` §4 @ `fef94857`; the §A.46 diff `c3b5f37a..f57e576a` (#1283); the
OA-2 STATUS note @ `6e2d1ee8` (#1284) as format precedent; `papers/Main.md` @ `c3b5f37a` (blob
`0db17597`) lines 42, 97, 360–427, 480–486, 516–518, 546–562, 652, 724; on-`main` records OA1, OA2,
T1, PPS, `Equivalence.lean`, `observer-interface-source.md`:199 at their cited lines.
**Owner and review records read first-hand through the host API:** #868 comments 6791565399,
6791606126, 6794392080, 6853568040, 6854708572, 6873193841; #1169 comments 6854728636, 6855167580,
6865177667, 6865680499, 6872828604; #1283 body; PR reviews 5857227567, 5857981727 (#1231),
5858000929, 5859960068 (#1232), 5891666660, 5897397957 (#1269), 5892919040 (#1273), 5901837851
(#1274); the current descriptions of #1273 and #1231. The owner's further requirement of 2026-11-14
and the statement that ladder r3 "is accepted as a conditional paper result, not as a native OI
Bell mechanism" were taken as quoted in the brief.

***

## Verdict: ACCEPT WITH CHANGES

The plan is careful, its dependency order is the owner's, and almost every file:line mapping I
opened says what the plan says it says. Blob ids, SHA-256 values and line counts of all sixteen
byte-identical files are correct. #1274 does carry every N4 statement the ladder uses, at N4's
own scope. The plan's L3 and Theorem N/N′ scope results are right: directed (Sep) needs L3, and
the (MI\*) branch needs the composition with BS:190. The #1269 determination holds: QH is not
load-bearing. Two blocking defects must be fixed before the plan is executed. (B1) The landed
STATUS notes cite this planning directory, which the plan keeps off `main`. That reference is
missing from the plan's own §A.42 item 8 tracing. (B2) SLD's scoped-claim sentence drops
hypotheses of the controlling condition. There are also fourteen should-fix findings and eleven
nits. None of them changes a scientific conclusion of an input.

***

## Findings

### Blocking

**B1. The landed STATUS notes cite off-`main` planning files, and §6.3's tracing omits them.**
SBS:3, :185, :196–197; SLD:3, :165, :187; SL3:3, :6, :25, :147–148, :153 cite `LANDING-PLAN.md`
(§1, §2.5, §5, §5.2) and `NOTES-PLAN.md` (OQ-2, OQ-3, OQ-7). Under NP OQ-11 (recommended) and
LP:409, this directory stays on its branch. Two of these citations carry substance:
- SL3:25 rests the N′ extension on LP §2.5.
- SLD:150–160 restate LP §2.5's N4 scope analysis.

LP:464–475 (§6.3) does not list these references. LP:475 then states that "No reference other
than LD:300's stage-7 sentence is a gap at landing", which is false as composed (§A.42 item 8).

*Replacement.* Make the notes self-contained and drop every pointer to the plan directory.
- In SBS:3, SLD:3 and SL3:3, replace "(`LANDING-PLAN.md` §5)" / "(`LANDING-PLAN.md` §5.2)" with
  "(the Bell support and ladder package, #868 comment 6873193841, option (1))".
- Replace "owner question OQ-2 of `NOTES-PLAN.md`" (SBS:196–197, SL3:147–148) with "an owner
  decision on whether a ChatGPT exact-head review also meets the non-author-review condition is
  required". Treat OQ-7 (SL3:153) the same way.
- SL3:6: delete the sentence "It is drafted for landing form (B) … a different note is needed."
- SL3:25: replace "(`LANDING-PLAN.md` §2.5)" with the one-line justification itself: "Theorem N′'s
  proof uses only step 1 and steps 3–4 (BS:190), so step 1's directed reading (S:169) carries to
  it."
- SLD:165, :187: replace with "re-measured at the package head".
- Add a row to LP §6.3: "`LANDING-PLAN.md`, `NOTES-PLAN.md` (this branch) | none after the
  replacements above | provenance". Alternatively, land the plan directory as provenance and
  revise OQ-11 accordingly.

**B2. SLD's scoped claim drops hypotheses of the controlling condition (conditional → less
conditional).** SLD:60–63 says that "directed separation in the actual coupling graph together with
measurement independence for the response-complete pre-setting variable forces it for the whole
finite menu and complete local histories". The source conjunction (LD:56–62) also requires:
- (D) and (F);
- (Gen) with disjoint generator regions;
- (Rec);
- every-run outputs with a fixed local failure rule;
- a finite menu with every pair jointly admissible;
- no postselection.

BS Theorem N/N′ (BS:161–162, :186) needs all of them. Under #1283 item 8 this quoted sentence is
the record's "scoped result" that becomes a surviving claim, so it must carry every condition
(Code Review Rules, claim/evidence boundary; §A.46 item 7). The same applies to the AL clause at
SLD:63–66, which omits (AL1)'s finite abelian site groups and (AL3)'s "every pair of positive
probability".

*Replacement* for SLD:60–63: "…directed separation in the actual coupling graph together with
measurement independence for the response-complete pre-setting variable forces it for the whole
finite menu and complete local histories, given one deterministic map on a finite site-factorized
space, settings read from disjoint generator regions, complete local record windows, every-run
outputs with a fixed local failure rule, a finite menu with every pair jointly admissible and no
postselection (Bell-scope Theorem N/N′, with SB L3 for the directed form);". For SLD:63–64, insert
"for finite abelian site groups," before "coset-uniform run laws", and "with every setting pair of
positive probability" after "cell-valued settings".

### Should-fix

**S1. Main:360 is not the specific support for the measurement-dependent part of LD:104.** At LP:102,
LP:176 (Result cell), LP:209–212, LP:439 and SLD:152–155, the plan says the measurement-dependent
branch "rests on Main:360". Main:360's witness is "globally coupled setting-dependent hidden
dynamics". That construction keeps measurement independence and breaks parameter independence:
BS:107 lists it as C10, "unrestricted global coupling". So it is not a measurement-dependent
witness. For the measurement-dependent branch:
- PR reachability is the ladder's own check 2, `φ_0` with `μ_MD` (LD:150–153) [A].
- "No selector supplied" rests on Main:360's general sentence ("Bare finite OI representability is
  too broad to select the quantum Bell set") and on Main:416, which records option (b) as "recorded,
  not adopted" with only a cost bound.
- Both are corpus-status statements, not a selector exclusion.

*Replacement* for SLD:153–155: "For that branch, PR reachability is the record's own check 2
(LD:150–153) [A], and the absence of a selector rests on Main:360's general statement that bare
finite OI representability does not select the quantum Bell set and on Main:416, which records
measurement dependence as not adopted [P]; neither N4 nor Main:360's construction, which keeps
measurement independence, addresses that branch." Make the same change in LP:102 (layer "A; P",
source "LD:150–153; Main:360 (general sentence), :416"), in the LP:176 Result cell, in LP:209–212
and in LP:439.

**S2. LP §2.5 misses one N4 use.** LD:284 ("…supply complete-history no-signalling … and supply a
selector. None is supplied.") is an unattributed N4 statement for an update outside (vii), which is
route B with measurement independence kept. It matches OC:509. *Replacement:* add a row to the
LP:174–178 table: "LD:284 (§5, escape requirements): 'and supply a selector. None is supplied.' |
OC:509 'not supplied' | route B, measurement independence kept | Matches." Mention it in SLD's
"N4 at its carried scope" paragraph.

**S3. The QH stage-7 sentence: the classification it receives is not "narrowing".** Three records
bear on this:
- REVIEW-r1 C13 (REVIEW-r1:321–322) required the ladder to classify QH:68–97 as "**support off
  `main`: gap** for the stage-7 illustration".
- ChatGPT 5892919040 requires that BS, SB and QH, being off `main`, "must remain labelled".
- The owner's #1169 c.6865177667 OQ-2/OQ-3 says "Do not write narrowing revisions just to unblock
  integration". c.6873193841 then allows #1269 to "remain explicitly identified as non-load-bearing
  context".

The sentence at LD:104 asserts QH's result ("The native encoded U′ composite reaches the
non-quantum table SWAP/2"). It drops QH's own conditions: QC FAIL "with NNB carried" (QH:68), and
SWAP/2 via P2 through H-PREP (QH:85–86), both supplied posits (QH:212, :215). Under §A.42 item 8 a
reference whose content the sentence uses cannot become provenance by relabelling. SLD:171–175 says
only "The sentence is context, not a result of the record". That understates the off-`main`
dependence and is not a narrowing of the claim.

*Replacement* for SLD:171–175: "Line 104, 'The native encoded U′ composite reaches the non-quantum
table SWAP/2 (QH:68–97) [D]', reports a result of Q-868-H r3 (#1269 at `ffc9cda4`), which is off
`main`. That result is conditional there on NNB and on the supplied posits P2 and H-PREP, is
model-reviewed and is not verified from `main`. It is non-load-bearing context (#868 comment
6873193841): stage 7's classification rests on Main:360, Main:416, check 2 and N4, and does not
use it. The clause 'which is Bell-local over Pauli-axis product tests [A]' is the record's own
observation about the SWAP/2 table." At LP:345–351 and LP:443, replace "gap closed by narrowing"
with "support off `main`, landed as owner-identified non-load-bearing context". Put to the owner
(OQ-6) whether the merge decision should also record it under §A.42 item 8's final sentence, as a
named claim left unsupported. That route is the cleanest under c.6865177667.

**S4. LP §6 has a review-status cycle that the plan does not resolve.** The STATUS notes record
their own package's review and merge as pending or absent: SBS:197, :200, :204–206; SLD:196–197,
:201, :205; SL3:146, :151, :157–158. G2(vi) then reviews the head that carries these lines. Updating
them after review moves the head off the reviewed commit. Leaving them makes them stale on `main`,
the same defect the notes list for LD:3–6 and BS:3–5. G3 (LP:54) updates Issues only.
*Replacement:* phrase each such line at the package head ("At the package head `<sha>`, no
package-level review or merge decision is recorded; the merge decision is quoted in the forward
note of step G3."). Extend G3 to "a forward note in each STATUS.md quoting the owner's merge record
with its author and time (§A.42 item 7), followed by a focused exact-head check, as for #1269
(review 5897397957)". G1 needs the same step: review 5901837851 accepted `fef94857`. G1(i) edits
OC's `STATUS.md` after that review, so add "(i′) a focused exact-head review of the edited head" to
LP:52.

**S5. The §7 standard is borrowed from the reconciliation sentence, which does not govern new
landings.** At LP:483–485 the C2 sentence ("record-specific verification shows its applicable
preservation conditions met") is quoted as the standard. That sentence applies only to
pre-adoption records reconciled under item 8 (#1283 body, C2; c.6872828604: "This applies to the
nine #1284 records"). New landings must meet all five bullets of item 8 in full, with no
"applicable" relaxation. "Historical authorization" (LP:496) is a reconciliation clause and not an
item-8 condition for a new landing. *Replacement* for LP:483–485: "For records landed after
adoption, #1283 item 8 requires every one of its five conditions. The table checks each condition
record by record. The historical-authorization row is recorded as provenance; it is a condition
only for pre-adoption records under the reconciliation sentence." Make the matching change in the
"Record-specific check of the draft's conditions" lead-ins (SBS:190–191, SL3:142, SLD:191).

**S6. LP §2.3 and SBS:199–200 say BS and L3 "close" OC's gaps E2 and D2.** In OC, D2 and E2 are
already closed by narrowing: OC `DEPENDENCIES.md`:23, :26 ("Narrowed"), with N2 "conditional on
L3" (OC:507) and SLL's exclusion consequence conditional on L2 and Theorem N (OC:537–542, :559).
Landing BS and L3 puts the named conditions on `main` at a model-reviewed layer. It does not make
OC's statements unconditional, and SLL's consequence still needs L2 (gap D3, not landed). Saying
"closes" invites exactly the silent promotion the owner excluded. *Replacement* for LP:129–130:
"**BS** puts on `main` the Theorem N on which OC's narrowed row E2 is conditioned; **L3** puts on
`main` the argument on which OC's narrowed row D2 (N2's necessity) is conditioned. OC's statements
stay conditional as written, and SLL's exclusion consequence still needs SB L2 (gap D3)." Any
forward note under OQ-13 must keep OC's "conditional on L3" and "conditional on L2 and Theorem N"
wording.

**S7. The SB-L3 extract's composition is under-specified and undercounts its additions.** LP:397
and SL3:16–20 list "one marked change" and "one marked addition". The planned file also adds a pin
block, a hypotheses paragraph from BS §3.1–3.2 and a support-layer paragraph, none of which is in
S:167–171. The verbatim lines also carry references that do not resolve in an extract:
- the heading tag "[A; X S5]" (S:167) and the sentence "S5 checks 300 random response tables …
  `|CHSH| ≤ 2` in each" (S:169), a computational claim whose script does not land;
- "B1's static bit" (S:171), a model on `main` under `verification/programmes/substratum/`;
- "§6" (S:171), SB's provenance section, which is not carried;
- "Theorem N" and "Bell-scope's (Sep)", which resolve to the landed BS.

*Replacement* for LP:397's Content cell: "S:167–171 copied verbatim and fenced as a quotation. Every
non-verbatim line is marked as an addition: the pin block; hypotheses from BS §3.1–3.2; a
resolution table for the in-text references (Main:364 → Main:362; Theorem N and (Sep) → BS @
`e1534b08`; B1 → its record on `main`; SB §6 → provenance; S5 → provenance, not support, because
S5's response tables already factorize and its check cannot fail); the N′ composition (BS:190);
the support-layer paragraph." SL3:16–20 needs the same correction.

**S8. SL3:60–62 restates S:171's consequence without its conditions.** The restatement says "a
shared static or autonomously evolving substate cannot by itself produce a Bell violation".
Review 5858000929 accepted the common-cause point "under MI". L3 inherits Theorem N's (F), finite
`V` and finite `S_i`, so "however deep" (S:171) holds for every finite depth only. An infinite
tower needs SB L2 (measurable λ), which is not carried (OC gap D3). *Replacement* for SL3:60–62:
"Consequence stated with it (S:171), under the same hypotheses: with (MI) for Ω (or (MI\*)) and
directed (Sep), a shared static or autonomously evolving substate of any finite depth cannot by
itself produce a Bell violation; infinite towers need SB L2, which is not carried (#1274 gap D3).
Parameter independence fails only through a directed path generator → factor → record (requirement
N2 of route A, carried by #1274 conditional on L3)."

**S9. Whole-record BS lands more than the owner's named component, and OQ-5 does not say so.**
c.6873193841 names "BS Theorem N and N′ (#1231)" and asks the plan to trace "#1231 (Theorem N/N′ and
§4)". The #1273 description appended on 2026-11-14 says the package carries "BS Theorem N/N′ and §4".
LP:56 and NP OQ-5 land the whole record, which also includes:
- Lemma G;
- NBA and the verdicts;
- §5's consequences for #1216 and #1169;
- §6's scored candidate principles;
- F1/F2, which are now stale.

For SB the plan argues the opposite way and extracts L3 to keep results "outside the owner's
option-(c) set" off `main` (LP:272–273). Whole-record landing is defensible: it keeps the line
citations and the review trail, and item 8 preserves records, not theorems. But it must be an
explicit owner choice. *Replacement* for NP OQ-5: "…Whole record (recommended). This lands Lemma
G, NBA, §5 and §6, beyond the components named in c.6873193841, each with its own STATUS row
(SBS:121–132). Alternatively, land an extract of Theorem N/N′ and §4." After the owner decides,
update the appended status of #1273.

**S10. SBS does not flag the probe's authorization question.** SBS:38–40 quotes the
writer-assignment option text "no runs", and SBS:129 and LP:367–371 treat `generic_bell_checks.py`
as support on `main` for the [X] tags. NP OQ-8(a) raises the conflict, but the landed note is
silent. *Replacement:* add to SBS "Limitations": "The probe was run under a writer assignment whose
option text reads 'no runs' (#868 comment 6791606126). Its [X] checks are support only once the
owner ratifies the run as covered, as #868 comment 6853568040 did for Q-868-H's probes. Until
then they are provenance and the results they tag rest on the arguments [A] alone." Mirror this in
the "Probe checks G1–G7" row (SBS:129).

**S11. L3's load-bearing use is narrower than LP §2.4 says.** LP:143–145 says L3 "is cited at
stage 3 (LD:100) and check 4 (LD:155–156)". As LP:190 itself shows, check 4 meets symmetrized
(Sep), so L3 is not needed there. Stage 3's NOT FORCED rests on `φ_0` with `μ_MD`, which meets
(Sep) in both forms, so L3 is not needed there either. The only load-bearing use is the
controlling conjunction with directed (Sep): LD:56–62, and stage 5 through "the conjunction of §0"
(LD:102). *Replacement* for LP:143–145: "L3 is load-bearing only for the controlling condition
(LD:56–62) and stage 5, which uses it (LD:102). At stage 3 (LD:100) and check 4 (LD:155–156) it is
cited, but those verdicts also hold with symmetrized (Sep)." SLD:139 and SL3:137–139
("Together") need the same correction.

**S12. LP §1 G0 and SBS:189–190 understate R-b.** The ruling (#1169 c.6865680499, Q1) says that,
until adoption, "a landing that meets none of the existing conditions needs an explicit, recorded
owner exception". LP:51 says "no record in this plan has a landing basis". That is accurate only
if no owner exception is recorded. *Replacement* for LP:51: "…Until then reading R-b stays in
force: a record in this plan can land only under an explicit, recorded owner exception, and the
owner's order (c.6873193841) defers landing until adoption." SBS:189–190 needs the same change.

**S13. The STATUS notes' superseded-line lists miss the evidence-tag definitions.** After landing,
LD:37–39 ("**D** draft off `main`"; "**A** hand derivation in this file, unreviewed") and BS:21–24
("**D** draft off `main`"; "**A** derivation in this file, unreviewed") no longer describe the
landed objects. LD's [D] tags at LD:64, :80, :100, :102–104 point to BS and SB L3, which are then on
`main`, except QH, which stays off. LP:61–62 states the layer mapping ([D] → [W]-type), but no note
records it. *Replacement:* add to SLD "Superseded lines": "Lines 37–39: [D] items that land with
this package (Bell-scope, SB L3) and the carried #1274 items read as research records on `main`,
model-reviewed and not verified (§A.46 item 7); [A] items have been reviewed as listed above. QH
remains [D]." Add the analogous entry for BS:21–24 to SBS.

**S14. LP §2.5's L3 row omits a fact that supports the review coverage it claims.** The L3
paragraph is byte-identical between r1 (`b94b283a`, lines 153–157) and r2 (`86a413c8`, lines
167–171). So review 5858000929's remark, made at r1, covers the accepted text. Review 5859960068
does not mention L3. *Replacement:* add to LP:182–183 and SL3:35–36: "S:167–171 is unchanged from
r1 (`b94b283a`, lines 153–157), so the r1 review's remark applies to the accepted text; the r2
re-review 5859960068 does not address L3."

### Nits

- **N1.** SBS:104, SLD:103, SL3:91: "This plan authorizes no work" now reads as if it meant the
  landing plan. Quote the ruling as #1284 does: "A remediation plan does not authorize new work"
  (#1169 c.6865680499).
- **N2.** The exogenous theorem's range: LP:93 and LD use Main:364–389 (theorem through □), while
  SBS:155 and :193 use Main:364–391. Use one range, Main:364–389.
- **N3.** LP:192–195 lists only three of the five required fixes of 5857227567. Add "among others
  (CF⇒MI one direction; the O2 window)".
- **N4.** LP:182: "Review 5858000929 accepted the point 'under MI'". The review says the
  common-cause observation "is also correct under MI". Quote that instead.
- **N5.** SLD:162 heading "Source drift from `c3b5f37a` to `main` (`c3b5f37a`)". Write "Source
  drift (pin `c3b5f37a`; re-measured at the package head)".
- **N6.** SBS:129 "17 PASS lines": the `.out` has 17 check lines and a final `ALL PASS` (18 lines
  contain "PASS"). Write "17 checks PASS, ALL PASS".
- **N7.** LP §2.5's Theorem N′ composition: say explicitly that the marked addition derives nothing
  beyond S:169 combined with BS:190. N′'s proof consists of step 1 plus steps 3–4, so the addition
  is a composition of two cited statements, not a new argument. Its "exploratory" grade at SL3:107
  is conservative and acceptable.
- **N8.** LP:113: "RC's `D_0` is a name only" is correct. Add that OA1:556–558 is the support.
- **N9.** SBS's claim sentence (SBS:68–69): "also on full histories" omits the one-product-extractor
  condition (BS:347–349). SBS:85–86 states it, so this is a nit. Append "(one product extractor
  with the Tsirelson box as the target's pushforward)".
- **N10.** BS:421–422 ("Nothing in this file lands; if it ever does, the gaps marked here must close
  first") becomes historical on landing. List it under SBS "Superseded lines", noting that its
  one gap, the probe, lands.
- **N11.** NP:39–42 records identity checks done by the writer. Note in NP that the blob and SHA-256
  values were independently re-derived here and match, for all sixteen files and for SB's blob
  `9ff0f077` / SHA-256 `662b9cba…48fd`.

***

## Check-by-check results

**1. Statement-level trace.** Every file:line in LP §2.1–§2.2 that I opened says what LP says it
says. The opened lines were:
- LD:49–51, :53–62, :78–83, :95–104, :145–156, :172–177, :187–263, :269–284, :298–304;
- BS:139–157, :159–196, :232–244, :292–294, :317–355, :419–441;
- S:28, :153, :157, :163, :167–171, :175, :177–181, :189–190, :220, :263, :272, :340–342, :356;
- OC:485, :490–494, :504–516, :555–559, :629–641; OC `STATUS.md`:86–95, :161–164; OC
  `DEPENDENCIES.md`:22–28;
- Main:42, :97, :360, :362, :364, :389, :412, :414, :416, :427, :480–486, :516–518, :546–552, :562,
  :652, :724;
- `Equivalence.lean`:245, :294, :422, :462, :466–468 (blob `9513665b`);
- OA1:103–105, :111–112, :176–178, :556–558 (`5a16b213`); OA2:606–613 (`8f8ddf73`); T1:56, :73–76
  (`a9cbc675`); PPS:134–145 (`9123157c`); Substratum:131–133; `observer-interface-source.md`:199.

Layers are right except at stage 7's measurement-dependent row (S1). The on-`main` / OC / package
labels are right, with two exceptions: the STATUS notes' own references (B1), and the QH sentence
(S3).

**2. The owner's scope check.**
- *N4 statements the ladder uses.* There are four:
  - LD:104: "no selector is supplied (SB N4, SB:190)";
  - LD:271: "bounds CHSH by `2√2` and reaches it (SB N4)";
  - LD:284: "and supply a selector. None is supplied." (unattributed; S2);
  - LD:299: the item-8 gap row.

  #1274 carries N4 at OC:509, verbatim against S:190: "| **N4** | every route, for agreement with
  the quantum set | A selector: the mechanism yields CHSH in `(2, 2√2]` and not more | channel +
  pad alone is the PR box [X S4] | not supplied; Main:360 records the same over-generation for the
  unrestricted construction |". The only change is Main:362 → Main:360 (Δ1). The [X S4] arithmetic
  is hand-checked at OC:511–514. N4's scope is routes A/B/C with measurement independence kept: OC:485
  copies S:175, and OC:557 states "MI throughout". The "not supplied" status is stated at OC:516. So
  #1274 carries every N4 statement at N4's scope; the claim does not rest on #1274 merely being
  expected to land. The plan's G1-dependence (LP:476–477) is stated correctly.
- *LD:104's measurement-dependent part rests on Main:360.* Only partly correct. Main:360's general
  sentence applies. Its construction keeps measurement independence. Reachability in the
  measurement-dependent branch is LD's check 2 (S1).
- *LD:271's "and reaches it" is the ladder's own addition.* Correct. N4 requires CHSH in
  `(2, 2√2]`; attainment of 2√2 is not in N4 at either head. The addition is a settlement criterion
  and changes no classification.
- *L3 (S:167–171) and the need for a Theorem N′ extension.* Correct. S:169 names Theorem N only.
  The ladder's (MI\*) branch with directed (Sep) (LD:59–60) needs the composition with BS:190
  ("Step 1 does not use (GI)"). The composition is valid: N′'s proof is step 1 plus steps 3–4, and
  the shared factor's content is part of Ω ⊂ λ\*. It is a composition, not a new argument (N7). The
  review narrowings are respected: 5858000929's "correct under MI", and 5857981727's "conservative
  sufficient screening test … does not weaken Theorem N/N′". The one gap is S8's restatement.
- *Theorem N/N′ (BS:159–178, :185–196).* Every ladder use is within the accepted scope:
  - the bound for "any MI Bell-local family" (BS:320–327);
  - optimality over Bell-local tables, with no use of attainment in 𝒞_sep or of the rationality
    aside;
  - per-run use with fresh generators (BS:292–294);
  - contraction with one product extractor (BS:347–353).

  The re-review's narrowings (six-site witness "logical sharpness only"; F1/F2 reported, not
  repaired; MI a posit) are not contradicted anywhere in LD or the notes.

**3. Dependency order and cycles.** There is no logical cycle:
- L3 → BS step 1 → Main:362.
- LD → BS, L3 and OC (routes, N3, N4).
- OC uses L3 and Theorem N only as named conditions (OC `DEPENDENCIES.md`:23, :26), so OC lands
  first without support from the package.

Nothing the ladder or BS uses rests on content that is not on `main`, not in #1274 and not in the
package, apart from three items:
- QH (S3);
- REC-1 / RC (provenance, LD:301);
- S5 (provenance).

There is a process cycle: STATUS lines that state their own pending review and merge (S4). The
claim that directed (Sep) needs L3 is correct: BS's (Sep) uses the symmetrized distance (BS:140,
:150). Its load-bearing site is narrower than stated (S11). "S5 cannot fail, so it is provenance"
is correct. S5 (`generic_substate_checks.py`:241–259) draws `h_A(m, l, a)` and `h_B(m, l, b)` with
setting-independent weights. That is a local hidden-variable model by construction, so `|CHSH| ≤ 2`
holds identically. The check tests Bell's bound for such models, not L3's directed-cone step. As a
control it is vacuous, which is a further reason not to cite it as support. The carried text must
say so (S7).

**4. #1269.** QH is non-load-bearing. Stage 7's UNDETERMINED needs no positive witness. Stage 4's
NOT FORCED rests on `φ_0`/`μ_MD`. BS uses a QH r2a session copy as "Provenance only" (BS:437). SB
does not cite QH. The proposed handling is not a change to the accepted text, because the text
stays byte-identical. As worded, though, it relabels a used reference rather than narrowing the
claim, and it drops QH's conditions. S3 gives the corrected wording and the owner route.

**5. Package composition.** All sixteen blob ids, SHA-256 values and line counts in LP §5.1 and
SBS:12–17 match the objects at `e1534b08` and `d8e4f80e`. The ladder's values match `OBJECTS.md`,
which records no substitution. The probe's SHA-256 matches BS:300. Each branch adds only its own
directory:
- `cac5d264..e1534b08`: four files;
- `c3b5f37a..d8e4f80e`: twelve files.

So the merges are conflict-free as stated. No landing file contains a local path or working-area
name. The SB-L3 extract is not yet written; the specification needs S7. I found no silent
promotion in the composition itself. The two promotion risks lie in wording: S6 (OC's conditional
rows) and B2/S8 (dropped conditions).

**6. STATUS notes.** The verification-status vocabulary matches #1284's definitions. The two added
definitions are consistent with §A.46 items 1 and 7. Hypotheses, limitations, accountable Issues
(#868 for BS and LD; #1169 for L3) and remediation rows are present for every retained result.
"Landing basis open until #1283 is adopted" is stated in all three notes (subject to S12). The
conditional-paper-result status is preserved (SLD:7–8, LP:217–218). Statements stronger than their
sources: B2 (SLD claim), S8 (SL3 consequence), S1 (Main:360 attribution), N9 (minor).

**7. Governance.**
- §A.42 item 2: QH content (S3); S5 (S7).
- §A.42 item 5: QH correctly not preserved.
- §A.42 item 8: tracing incomplete for the notes' own references (B1).
- §A.45: no authorization is claimed. G3 is correctly limited to planning-status maintenance.
- §A.46: items 4 and 6 are applied correctly; item 1's "preserved, not established" is stated in
  each note.
- #1283 item 8: the conditions are tabulated correctly. The C2 sentence is misapplied to new
  records (S5).
- The review-condition gap is stated correctly: BS has ChatGPT reviews only (5857227567,
  5857981727). L3 has the r1 ChatGPT remark (5858000929), the BS re-review's note (5857981727), and
  a citation check in REVIEW-r1:138, which did not re-derive L3. The carried `SB-L3.md` and its N′
  addition have had no review.
- Both review clauses are met for LD: REVIEW-r1, CONFIRM-r2, CONFIRM-r3 and 5892919040 at
  `d8e4f80e`.

***

## Owner questions OQ-1 to OQ-15: recommendations

| OQ | Recommendation |
|---|---|
| OQ-1 | Agree. Adopt #1283 first, then re-check LP §7 and each note's condition list against the adopted text. If the adopted text keeps the reconciliation sentence, do not apply it to these new records (S5). |
| OQ-2 | Separate non-author review, as recommended. Item 8 names two reviews conjunctively. For BS it should be a full review of r2, because 5857981727 was a focused closure of five findings and was the only reader of N′ and the six-site member. For SB L3 it should review the written `SB-L3.md` with its N′ composition. |
| OQ-3 | (B), the carried extract, as recommended, with S7's composition rules. Form (A) would land results outside c.6855167580's set at stale pins. |
| OQ-4 | Leave D3 open under #1169, as recommended. The ladder does not use L2 or class (a)3. Note in SL3 that L3's "however deep" stops at finite depth without L2 (S8). |
| OQ-5 | Whole record, as recommended, but ask it as an explicit choice that lands content beyond "Theorem N and N′" (S9). |
| OQ-6 | Land the ladder text unchanged, with SLD stating the QH sentence as off-`main`, conditional and non-load-bearing (S3 wording). Have the merge decision record it under §A.42 item 8's final sentence as a named claim left unsupported. Do not write r4, given c.6865177667 ("Do not write narrowing revisions just to unblock integration"). Do not preserve #1269 for this sentence. |
| OQ-7 | Required before G2. c.6854728636 step 5 asks for a current owner decision replacing the unlocated 2026-11-11 approval. c.6873193841 is planning-only, so it does not replace it. Fold it into the G2 merge decision, worded to cover the L3 extract explicitly. |
| OQ-8 | (a) Ask the owner to ratify the BS probe as covered (precedent: c.6853568040). Otherwise the [X] tags are provenance and SBS says so (S10). (b) Authorize the replay with the landing as a package check. It is generic, deterministic and encodes no OI rule, and §A.42 item 1 asks a computational claim to name a command and expected result reproducible from `main`. |
| OQ-9 | S5 as provenance, as recommended, marked as such inside `SB-L3.md` (S7). |
| OQ-10 | Land the NOTES as review trail, as recommended. SLD already lists NOTES-r3:1 as superseded. |
| OQ-11 | Keep the plan directory off `main` only after B1's replacements remove every reference to it from the landed notes. Otherwise land it as provenance. |
| OQ-12 | One pull request, merge commits of `e1534b08` and `d8e4f80e`, landing by merge commit, as recommended. |
| OQ-13 | Add the forward note in the package rather than leaving a stale status surface. Keep OC's conditional wording (S6), and add nothing that changes OC's status. |
| OQ-14 | Record in SLD without r4, as recommended, with S1's corrected attribution and S2's added use. |
| OQ-15 | Append a current status to #1231's description, as recommended (it still says "unreviewed" and calls the bound "tight" without scope). After OQ-3 and OQ-5, also append to #1232 and update #1273's appended status. |
