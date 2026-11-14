# Independent review r1: TUNE-1 landing plan (#1236)

**Object.** Branch `records/tune1-landing-plan-1236-20261114` at
`00d1861a23be21bde1d9ea618ce7c3e627fa40e9` (one commit on `main` = `c3b5f37a`), directory
`verification/programmes/oi-qm/reconstruction/tune1-landing-20261114/`: `LANDING-PLAN.md` (LP),
`STATUS-STEP3A.md` (S3A), `STATUS-SOURCING.md` (SSRC) and `NOTES-PLAN.md` (NP). "LP:n" and the
others are lines of those files at `00d1861a`. "3A:n" is `TUNE-1-STEP3A-r3.md` at `8228b3c2`, "SRC:n"
is `TUNE-1-SOURCING-r2.md` at `c539a60c`, and OA1, OA2, OA3 are the OA reports on `main`, as in the
plan.

**Reviewer.** A model reviewer that wrote none of the plan, the STATUS notes or any input record.
Paper-only: no computation on any OI rule, no CI, no write to the repository or the host. This
review is not verification (§A.46 item 7), and it authorizes nothing.

**Read at their heads** (`git show <sha>:<path>`; each remote head checked with `git ls-remote`):
- 3A r3, r1 (lines 420–430 and 540–550), `TUNE-1-STEP3A-REVIEW.md` (headers, §§0, 5, 8, 9, 10, the
  recheck with its nit and commit confirmations, the r3 review and its confirmation) and
  `TUNE-1-STEP3A-OBJECTS.md`, all at `8228b3c2`.
- SRC r2 in full, `REVIEW-r1.md` (header, §0, R1–R6), `OBJECTS.md` and the `890fe3dd..c539a60c` diff.
- OA-1 r5, OA-2 r4 and OA-3 r4 on `main` at the ranges LP §3.2 lists, together with OA-3 r2
  and r3 and their diff. The three OA `STATUS.md` notes at `c3b5f37a` and at `6e2d1ee8`, with the
  `c3b5f37a..6e2d1ee8` stat.
- The OA reports and W1-1 r4 at `2d064a71`, compared with `main` by blob, and OA-2 r4 by `diff`.
- REC-1 r7 at `9f7d2612` (rows C1–C15 and every `3A:` citation) and r9 at `3a3aa146`.
- NA `ASSESSMENT.md` at `d8b74527`, lines 1–65, 108–120 and 158–166.
- The §A.46 diff `c3b5f37a..f57e576a`.
- The Bell plan at `3859c3ef`: `REVIEW-BELL-PLAN-r1.md` and `CONFIRM-BELL-PLAN-r2.md`.
- `papers/Main.md` lines 58 and 724, and OBS lines 100 and 121.

**Read first-hand through the host API:**
- all twelve comments on #1236, including c.6873565446;
- the #1147 body;
- #1267's body and review 5887947616; #1272's review 5892912253;
- #1278's reviews 5897621232 and 5898054706;
- #1284's body and review 5900793856.

**Identity checks.**
- All thirteen package blobs, SHA-256 values and line counts in LP §5.1–5.2 are correct.
- Each record branch adds exactly its listed files. The parentage is as LP states: `b923fa7f` has
  parent `62bdc2cf`, and `890fe3dd` has parent `c3b5f37a`.
- `62bdc2cf`, `080cd2be`, `2d064a71`, `59557ee8` and `c03a5764` are ancestors of `main`, and `main`
  is still `c3b5f37a`.
- `papers/Main.md` (`0db17597`), `papers/SM.md` (`a5202371`) and the Step 1–2 directory have no diff
  from `080cd2be` to `c3b5f37a`.
- OA-1 r5 (`5a16b213`) and OA-3 r4 (`0a36fd05`) are the same blobs at `2d064a71` and on `main`. OA-2
  r4 is `9a6e3682` → `8f8ddf73`, and `diff` shows lines 65 and 958 only.
- #1284's three OA note blobs are as LP §3.1 states.
- Of the full ids in `TUNE-1-STEP3A-OBJECTS.md`, the five reviewed working-copy ids are reachable
  from no ref (`git log --all --find-object`). `221754fc…`, the earlier committed REVIEW blob, is
  reachable only through `b923fa7f`.

***

## Verdict: ACCEPT WITH CHANGES

The plan has the right order (#1283, then #1284, then one package) and keeps TUNE-1 paused. It
does not present preservation as progress, and it keeps the two gaps apart for the right reason
(SRC:383–384). The traces I opened mostly say what the plan says. Three defects block execution:

- **B1.** The draft STATUS notes rest load-bearing statements on plan files that stay off `main`,
  and LP §6.3 does not trace those references. This is the defect the Bell review recorded as its
  B1.
- **B2.** Both scoped-claim sentences drop hypotheses that their records carry. This is the Bell
  review's B2.
- **B3.** S3A misstates Step 3A's own typing of the MP-0a-type and MP-0b-type ingredients.

There are also fifteen should-fix findings and ten nits. Several of them repeat defects that the
Bell plan corrected after the version this plan copied (S13). No finding changes a scientific
conclusion of either record.

***

## Findings

### Blocking

**B1. The STATUS notes cite off-`main` plan files for substance, and LP §6.3 omits those
references.** The plan keeps this directory off `main` (LP:323–324; NP OQ-10). The notes cite it
at these lines:
- S3A:3, :138, :186–187, :190, :201, :203;
- SSRC:3, :149, :177, :197, :207.

Three of these citations carry substance:
- S3A:138 and SSRC:149 rest "Neither gap closes the other" and "a specified member … would inherit
  O-RDY" on LP §4.
- S3A:203 and SSRC:207 rest the §A.42 item 8 tracing, which is a condition of #1283's item 8, on
  LP §6.

LP:398–409 lists neither plan file, so LP:409 ("No reference is a gap at landing …") is false as
composed (§A.42 item 8).

*Replacement.*
- S3A:3 and SSRC:3: replace "(`LANDING-PLAN.md` §5)" with "(the TUNE-1 preservation package, #1236
  comment 6873565446)".
- S3A:137–138, after "(O-RDY, #1147), which concerns the ready resource of one candidate": write
  "Supplying that resource would exhibit no member, and a member exhibited inside TUNE-1's
  initial-condition schema would still need it, at least at the sourcing unit's F-S2 rate. Neither
  gap closes the other."
- SSRC:148–149: replace "(`LANDING-PLAN.md` §4)" with "(F-S2; AW-SRC-2, SRC:342–345)".
- S3A:186–187 and SSRC:197: delete the parenthesis.
- S3A:190: replace "(`NOTES-PLAN.md` OQ-2)" with "recorded under Dependencies".
- S3A:201: replace "(`NOTES-PLAN.md` OQ-1)" with "an owner decision is required on whether
  that review meets item 8's non-author condition".
- S3A:203 and SSRC:207: replace "tracing in `LANDING-PLAN.md` §6" with "tracing in this note's
  Dependencies table". Both tables already carry every row LP §6.1–6.3 classifies, except the B1 and
  S10 rows below. Add those rows to them.
- SSRC:177: replace "(`LANDING-PLAN.md` §1, G2)" with "at packaging".
- Add a row to LP §6.3: "`LANDING-PLAN.md`, `NOTES-PLAN.md` (this branch) | none after the B1
  replacements | provenance".

**B2. Both scoped claims are less conditional than their records (conditional → less
conditional).** Under #1283 item 8, each sentence is the "scoped result" that becomes a surviving
claim, so it must carry every condition its record carries.

*S3A:59–68.* The sentence names no hypothesis of OA-2 Theorem E(b). It also omits the following:
- "if that result holds" (3A:924);
- that (SP) is undecided for TUNE-1 interfaces;
- that whether preparation-noncontextuality excludes T1 is open at literature level (3A:600–606);
- that B and the exchange rows lie outside E(b), and that D is unclassified;
- the record's own groups, primary **underspecified** and secondary **lacks a sourced
  apparatus**, read as in 3A:413–420;
- H-write for B and the exchange rows of C and D, and H-nl for D;
- the scope "in the records read" (3A:1054–1058).

*Replacement* for S3A:59–68: "**Claim supported by this record:** "None of the four classes TUNE-1
Step 2 left INCONCLUSIVE, each with `sup_n |C_n| = ∞`, has an exhibited member with fully specified
dynamics, preparation and readout in the records read, which are the Step 2 records that define the
classes. The four classes are:
- A, L5.4 in initial-condition mode;
- B, L5.4 and L5.5 in exchange mode under the named, unadopted H-write;
- C, L5.6;
- D, NL-A/NL-P for R-nl under the named, unadopted H-nl.

So none qualifies for Step 3B and none remains viable. This is a specification gap, not a quantum
failure and not a negative result about any class, and every class stays INCONCLUSIVE. Each class is
primarily underspecified. It is secondarily lacking a sourced apparatus, in the sense that its
preparation, control or readout is not shown derivable from the joint dynamics: the ready
configuration and program blocks, run repetition, the law of the unread world (H-μ) and the growth
of the control region have no physical source. H-write adds to this for B and for the exchange rows
of C and D, and for D the rule itself is unsourced. For R-lin, consider a specified
initial-condition member of A or C that meets OA-2 Theorem E(b)'s hypotheses (H1), H-AR, (H3),
(H4) and (xiv). If Theorem E(b) holds, that member has a simplex-embeddable prepare–measure fragment
under (SP), and a preparation-noncontextual one without (SP). In that reading H-μ plays (xiv), and
D4's complete history is the imported MP-0b-type convention. The match of TUNE-1's interface to
those hypotheses is the record's own reading. (SP) is undecided for TUNE-1 interfaces. Whether a
preparation-noncontextual model can meet T1 at small ε is open at literature level. B and the
exchange rows lie outside Theorem E(b), and no result classifies D. (Paper derivations and readings
on Step 2 results, which are paper derivations reviewed under Step 2's gates and not kernel-checked,
and on OA-1, OA-2 and OA-3 research records not independently established; model-reviewed by an
internal same-family reviewer and by ChatGPT; not independently verified; not adopted; no
manuscript claim affected.)""

*SSRC:48–58.* The sentence omits the following:
- the ledger posits of part (a) and the finite fixed alphabet;
- "in the order (a)–(f)" (SRC:146–147);
- that what is excluded under μ-G is an unconditional supply (5892912253: "ruled out as an
  unconditional ready source under uniform μ-G");
- the search scope of "named in the corpus only as" (SRC:403–407);
- the schema conditions of F-S2 (SRC:342–345), and that the bound is "necessary inside TUNE-1's
  initial-condition apparatus schema, not universal resource lower bounds or a sufficient apparatus
  construction" (5892912253);
- F-S1's proviso `m + 1 ≤ L`;
- (e)'s dependence on MP-0b;
- that the member specification and L5.4 stay open.

*Replacement* for SSRC:48–58: "**Claim supported by this record:** "Take candidate TC-A, defined as
follows:
- R-lin, `Φ_F(y, x) = (x, Ax − y)` over `ℤ/q` with `q` fixed;
- finite tori, one torus per precision;
- initial-condition mode, with no write outside `Φ_F`;
- a `D_0`-form initial law: designated known cells, and every other cell uniform and independent;
- heralded Q6′ witnesses;
- `sup_n |C_n| = ∞`.

Part (a) is taken relative to ledger items (ii) and (vii)–(xi) and (xiii) of Main:724. For TC-A,
NL-C, a Step 2 paper derivation, applies at every interface and is not escaped: TC-A meets NL-C′ by
letting `|C_n|` grow. In the order (a)–(f), the first part not shown to follow from OI's stated
premises is (b), the ready resource: a native producer of known-value cells for the ready
configuration and the program blocks, renewed for every run.
- Under the global counting measure, an unconditional supply of it is excluded.
- Under the orbit measure, no unconditional supply is given: only orbit-constant cells are
  unconditionally known, and the conditional route through held records is open.
- Under the record-compatible measure, the question is undecided.

Within the searches the record states, the corpus names this resource only as the unadopted MP-0a,
the open H-PREP and the open obligation O-RDY. Memory (e) rests on the same ingredient or on the
convention MP-0b. TUNE-1's initial-condition schema here has a finite alphabet, program blocks that
are translates of `C`, and `r_O` fixed on all of `O`. Within it, at least `(K + 1)
log_q((1−4ε)/(4ε))` known `q`-ary cells are necessary per run. That is a necessary condition only,
not a universal resource lower bound and not a sufficient apparatus construction. NL-C's counting
also covers gates of `m` rounds with `m + 1 ≤ L`; longer gates are open. TC-A's member
specification and L5.4 remain open. (Paper readings and hand derivations on research records not
independently established, model-reviewed by a non-author reviewer and by ChatGPT, not
independently verified; a bounded sourcing stop, not an OI-wide no-go; not adopted; no manuscript
claim affected.)""

**B3. S3A:77–78 misstates Step 3A's own ledger, and the two records' typings of MP-0b differ
without either note saying so.** S3A:77–78 puts "MP-0a-type ready supply and MP-0b-type complete
history (3A:1014–1016)" under "Used but not stated in TUNE-1's governing texts". The record's
ledger types the three items separately:
- run repetition is "not stated in TUNE-1's governing texts" (3A:1014);
- the MP-0a-type ready supply is "unsourced" (3A:1015);
- the MP-0b-type complete history is an "imported convention" (3A:1016; :501; F-3A-3, 3A:987–989).

The MP-0b typing is load-bearing. F-3A-3 places R-lin init members inside Theorem E(b)'s
hypothesis set because D4's complete history is that imported convention. SRC types MP-0b instead as
a "named hypothesis … interface convention; status undetermined" (SRC:143). SRC itself lists 3A:501's
"MP-0b typed as imported" as provenance (SRC:431), and SSRC:64–66 lists MP-0b as "named,
unadopted". Under the whole-framework rule ("Where documents differ … the difference is a finding
to propagate") each note keeps its own record's typing and names the other's.

*Replacement* for S3A:77–78: "- **Typed in the record's ledger (3A:1014–1016):**
  - run repetition, used but not stated in TUNE-1's governing texts (F-3A-2);
  - the MP-0a-type ready supply (`r_O` and the program blocks), unsourced;
  - the MP-0b-type complete history, an imported convention (3A:501). With it, R-lin
    initial-condition members meet Theorem E(b)'s hypotheses except (SP) (F-3A-3).

  The TUNE-1 sourcing unit types MP-0b as a named hypothesis, an interface convention (its part
  (e)). Each typing is that record's own."

In SSRC:64–66, replace "MP-0b (records held outside the observer)" with "MP-0b (the visible
history counts as held, outside `V`; an interface convention, OA1:563–564; Step 3A types the same
complete history as an imported convention, 3A:501)".

### Should-fix

**S1. The exploratory lines of OA-3 are wider than LP and S3A state.**

The first range is N3 proof step 1's weight bullet, OA3:323–326. It is r3:315–318, rewritten by three
delta-review items of `DELTA-REVIEW-OA-3-r3.md`:
- R1, the C-PM coin weight (OA3:813);
- O5, the removed "for the unheralded π" (OA3:820);
- "Recheck D1 (μ-G weight after R1 + O5)" (OA3:823).

The r2 → r3 diff touches all four lines. #1284's OA-3 note grades R1–R4, O1–O3 and O5 exploratory
(RCN OA-3 `STATUS.md` results table) and does not name the D1 recheck item.

The second range is the whole second sub-bullet of N4.1, OA3:415–416 (R2, OA3:814).

OA3:801, which LP:157 cites, is the change-map row of the reviewed recheck item E1, not a
delta-review edit.

*Replacement* at the following places:
- LP:155–157: write "OA3:323–326 (N3 proof step 1, the weight bullet: R1, O5 and the D1 recheck of
  `DELTA-REVIEW-OA-3-r3.md`, OA3:813, :820, :823) and OA3:415–416 (N4.1, the ensemble-conditioning
  sub-bullet: R2, OA3:814) are delta-review text. #1284 grades R1–R4, O1–O3 and O5 of that review
  exploratory (`…/oa-3-20261112/STATUS.md` at RCN, results table); the D1 recheck edit is listed in
  the same change map (OA3:809–823)".
- LP:210–211 and S3A:148: use the same line ranges.
- S3A:148: replace "graded exploratory in the OA-3 status note" with "delta-review text that the
  OA-3 status note grades exploratory".

**S2. LP §3.2's "Grade after #1284" column assigns grades that #1284 does not give.** #1284's OA-2
table grades N0, Theorem C, N2.3, Theorem E(b), Proposition B(ii) (⇒), class N and the [R]
statements. It does not grade Corollary E1. LP:203 calls Corollary E1 "partially verified (as
E(b))", but Corollary E1's generalized form holds "for any rule, affine or not" (OA2:585–586), which
goes beyond E(b). Several other rows grade definitions rather than graded results:
- the setup rows (LP:205);
- the typing of measures, the §4.2 target and R5 (LP:209);
- OA-1 D1, D3 and D4 (LP:208). #1284's OA-1 note grades only "Gap 1 … (D2 applied to N1-S)".

*Replacement.* In the column, for Corollary E1: "not graded separately in #1284; reviewed text of
r4 (OA2:577, F6, N4), so partially verified under #1284's definition". For the setup, measure-typing,
target and R5 rows: "definitions; not graded results". For OA-1 D1–D4: "D2 within gap 1, partially
verified, conditional on μ-G; D1, D3 and D4 not graded separately (reviewed r5 text)". Rename the
column "Grade after #1284, or nearest graded result".

**S3. The C9 narrowing points to on-`main` text that says something different; C6 is faithful.**

SSRC:162 and LP:386 say that "the same concern is on `main` at NPS1:85". NPS1:85 says that using a
ready record to supply readiness "may be circular", for the binary-ring bank. REC C9 says something
different: μ-R "presupposes 'the observer's records', whose formation is the question". The
on-`main` support for N3.3's "Undecided" lies elsewhere:
- OA1:106–107: μ-R is maximal entropy "compatible with the observer's records", posited through
  (iv);
- OA1:522 and :603: under μ-R, N1-S "is open".

The narrowing does not change SRC's claim, because N3.3 reaches no verdict. Only its on-`main`
anchor needs correcting.

C6's narrowing to OA1:563–564 is faithful: it keeps SRC's marking and drops REC's status word to
context. It should, however, carry B3's note on the differing typings.

*Replacement* for SSRC:162: "Support off `main`, closed by narrowing. N3.3 reaches no verdict
("Undecided; no source"). On `main`, μ-R is posited through (iv) as maximal entropy compatible with
the observer's records (OA1:106–107), and conditional preparation under it is open (OA1:522, :603).
NPS1:85 records a related circularity concern for record-supplied readiness. REC C9's reading is
context." Make the same change at LP:136 and :386.

**S4. #1278's use of SRC is misdescribed, and SSRC cites #1278 as current evidence.** LP:264–265
and SSRC:139–140 say that #1278 reads SRC "only as off-`main` context". NA `ASSESSMENT.md`:163 and
its non-author review 5897621232 say otherwise:
- NA:163 states that the #1272 text "is used only for the explicitly attributed comparison and
  conditional resource bounds";
- 5897621232 says that it "supplies expressly identified off-main support for the attributed
  comparison/resource statements".

So #1278 uses SRC as off-`main` support. LP:76–79 states this correctly. Separately, SSRC:134–140
lists #1278 and its review under "Current evidence" for O-RDY, although LP:404 classifies them as
governance provenance.

*Replacement* for LP:264–266: "…and uses SRC as off-`main` support only for its attributed
comparison and conditional resource statements; its own source stop rests on its `main` source
packet (NA `ASSESSMENT.md`:163; review 5897621232)."

For SSRC:134–140:
- keep "this record's stop, with OA-1 gap 1 (OA1:522), OBS:100, :121 and the first stops of NPS1
  and NIS2 for the binary SM ring (F-S3)" as the current evidence;
- move the #1278 sentences to a new bullet, "**Related governance record (provenance, not
  evidence for this stop):** …";
- end that bullet with "it concerns the binary SM ring branch, not R-lin, and neither closes nor
  narrows this gap for TC-A".

**S5. "Not a minimum-cost proof" is misattributed.** In LP:242 and SSRC:7–8 the phrase is credited to
the scope of 5892912253. The phrase is not in SRC or in 5892912253. It is from #1278's non-author
review (5897621232: "This is not a minimum-cost proof, a general no-go …"), which describes #1278.
5892912253 scopes SRC's bound as "necessary inside TUNE-1's initial-condition apparatus schema, not
universal resource lower bounds or a sufficient apparatus construction".

*Replacement* for SSRC:7–8: "Its stop is a sourcing stop, not an OI-wide no-go; its resource bound
is necessary inside TUNE-1's initial-condition schema, not a universal resource lower bound and not
a sufficient apparatus construction; it is not a native mechanism." In LP:242, replace "not a
minimum-cost proof" with "not a universal resource lower bound or a sufficient apparatus
construction (5892912253)".

**S6. Under μ-G, what is excluded is an unconditional supply.** LP:134 and :241 and SSRC:42 write
"excluded under μ-G" without saying what is excluded. SRC N3.1 says "No ready region exists under
μ-G", and SRC:246 adds that a herald is possible, at F-S2's cost for `r_O` and not at all for the
program blocks before use. 5892912253 reads this as "ruled out as an unconditional ready source", and
NA:116 adds that it is "not absence of individual ready microstates".

*Replacement:* "an unconditional supply excluded under μ-G (Lemma P-1); heralding is the only route
there, at F-S2's cost for `r_O` and unavailable for the program blocks before use (SRC:244–246)".

**S7. The item 8 condition tables add historical authorization as if it were a condition.** The
affected lines are LP:441–450, S3A:194–210 and SSRC:200–213. #1283's item 8 has five conditions
for a new preservation. "Historical authorization" and "record-specific verification" belong to
the reconciliation sentence for records that landed before adoption. This is the Bell review's S5.

*Replacement.* Head each table "Item 8's five conditions (all apply in full to a new landing)", and
merge "explicit rationale" with "separate owner merge decision" into the fifth row, as item 8 does.
Move "historical authorization" below the table as "Authority (provenance): …". In LP:438–439,
replace "as C2 requires of the reconciliation and as this plan applies to new records" with "applied
here condition by condition; the reconciliation sentence does not govern new landings".

**S8. As landed, the notes will state review and merge states that are already out of date.** The
following lines record states that the landing itself changes:
- S3A:199–202, :209; SSRC:204–206, :212 ("this note and the package head need the package's
  non-author and ChatGPT exact-head reviews"; "separate owner merge decision: not recorded");
- S3A:193–194; SSRC:199–200 ("the basis is open until #1283 is adopted"), although G0 makes
  adoption a precondition of G2.

This is the Bell review's S4 and its confirmation's C2.

*Replacement.*
- At each review clause: "in this note as landed, no package-level review or merge decision is
  recorded; they are quoted, with their commits, in the forward note added after landing".
- Add to LP G2 a step "(v′) restate each Basis line against the adopted item 8, quoting the adoption
  record".
- Add to LP G3: "a forward note in each STATUS note naming the reviewed package head, its reviews
  and the merge commit, as a correction in place".

**S9. G1 has to come before G2, as the notes are drafted.**
- S3A:126 and :147 and SSRC:164 cite grades ("partially verified") that exist only in #1284's
  notes at `6e2d1ee8`.
- At `c3b5f37a`, the OA notes still read "What the record establishes".

If G2 lands first, those citations are support off `main`. LP:67 calls G1 "recommended … not
strictly required", and LP §3.4 describes a fallback text, but neither note carries that fallback.

*Replacement* for LP:67, last cell: "Required before G2 for the notes as drafted. If the owner
orders G2 first, the notes are rewritten per §3.4, and that version is reviewed before G2."

**S10. §A.42 item 3 has two more ids to check, and LP §5.5 and §8 item 7 name neither.**
- SRC:82 carries the full commit `9f7d2612f39960a41188eae8f3753d9def8019e8`. It exists in the
  repository only on #1268's branch. After the C6 and C9 narrowings it is not offered as support,
  so item 3 holds while that branch exists.
- `221754fc…` in `TUNE-1-STEP3A-OBJECTS.md`:13 resolves from `main` only through `b923fa7f`.

*Replacement.* Add to LP §5.5: "SRC:82 names `9f7d2612…`, which is on #1268's branch only. At G2,
check that it exists. After the narrowings it supports no claim (§A.42 items 3, 5). `221754fc…`
resolves through `b923fa7f`, so the landing must be a merge commit." Add both rows to the
Dependencies tables of S3A and SSRC.

**S11. The superseded-line lists miss tag definitions and identifiers in the accepted texts.**

*S3A:166–182* omits the following:
- 3A:43: "[W] this writer's derivation or reading, unreviewed". The [W] items have been reviewed as
  listed.
- 3A:186: "an off-`main` result (OA-2 Theorem E(b))".
- 3A:7, :10, :1052, :1076, :1106 and :1154 cite `REVIEW-STEP3A.md`. The committed file is
  `TUNE-1-STEP3A-REVIEW.md` (OBJECTS:13, :22).
- 3A:5 gives r2's blob as `17076ef7` and 3A:8–9 gives r1's sha256 prefix as `914f2339…`. Both
  identify the reviewed working copies, not the committed `313a76e3` and `ef63ccb9…`
  (OBJECTS:11–12).

*SSRC:179–193* omits the following:
- SRC:89–90, "[W, here] … unreviewed", and the [R-off] definition at SRC:88 ("context only"), which no longer fits 3A;
- every "[R-off]" tag on a 3A citation, at SRC:101, :123, :129, :143, :157, :174, :280, :294, :326
  and :340. These read as [R] after landing.

*Replacement.* Add one bullet per item above, in the notes' existing form.

**S12. The hypothesis lists omit [R] premises the records use, and OBS has no status note.**
- SSRC:60–72 lists Step 2 results only. N3.1, N3.2 and F-S2 also use the following [R] premises:
  - OBS Lemma P-1 (OBS:529–545);
  - OA-1 D1–D3 (OA1:141–160), D4 (OA1:162–175), D5 and D7 (OA1:176–208).
- S3A:70–80 omits OA-2 Theorem E(a) and OA-1 D5, which S3A:53 relies on, and P's interface
  definitions D1–D7.
- OBS (`observer-interface-obsmu-20261104/`) has no `STATUS.md` on `main`, like Steps 1–2 (LP:160–162).

*Replacement.* Add to SSRC: "- **[R] premises:** OBS Lemma P-1; OA-1 D1–D5 and D7; carried as
named conditions, not verified premises (§A.46 item 7)." Add the corresponding line to S3A. Add OBS
to LP §2.3's third bullet and to OQ-3.

**S13. The Bell precedent is pinned before its review.** LP:39 and NP:35 pin #1285 at `ed61696d`.
That branch is now at `3859c3ef`, which carries the review, the response and the confirmation that
corrected B1, B2, S4, S5, S13 and C2. This plan reproduces each of those defects (B1, B2, S7, S8,
S11). *Replacement:* re-pin BL at `3859c3ef` and read `REVIEW-BELL-PLAN-r1.md` and
`CONFIRM-BELL-PLAN-r2.md`.

**S14. SSRC's Limitations section omits two of the ChatGPT review's scope qualifications.**
5892912253 states that "held records/memory remain unsourced" and that "Spatial copies supply
independent trials only given independent ready regions". SSRC:74–86 has neither.

*Replacement:* add the following bullets.
- "- Memory (e) is not sourced: it rests on the ready resource or on the convention MP-0b (SRC:143,
  :380–381; 5892912253)."
- "- Spatial copies give independent runs only given an independent ready region per copy
  (SRC:276–281; 5892912253)."

**S15. OQ-1's recommendation outruns the record.** `TUNE-1-STEP3A-REVIEW.md` never states that its
reviewer wrote none of Step 3A. Its review of r1 says only "Independent internal review (same model
family)" (REVIEW:6). The r2 recheck nits were "applied by the coordinator" (3A:1106). The r3 review
and its confirmation name no reviewer. Some passages are consistent with a separate agent but do not
establish one: "I cannot observe the writer's process" (REVIEW:505) and the commit confirmation
(REVIEW:527). Item 8's condition is non-authorship, not model family. A "yes", recorded as the
owner's finding, would rest on no record.

*Replacement* for the recommendation at NP:85–86: "Recommendation: the owner decides on a recorded
attestation, quoted in the note, of which agent wrote r1–r3 and which reviewed them. If none can be
given, a focused non-author confirmation of r3 against its review trail, paper-only, before G2.
'Substantive, nonredundant': yes."

### Nits

- **N1.** NP:9 says "all eleven comments". #1236 has twelve, the twelfth being c.6873565446.
- **N2.** LP:76–77: REC-1 r7 cites 3A at more lines than :215 and :217, namely r7:93, :120, :121,
  :144, :147, :150, :151 and :180. Cite REC-1's current head r9 (`3a3aa146`), which has 19 `3A:`
  citations.
- **N3.** LP:108 and S3A:53 give "[R]" for translation-only control "under every law". 3A:692
  tags the L5.6 extension "[W, reading of S3:79–85]". Write "[R] (Lemma A-T (a), (b); OA-2 E(a); OA-1
  D5); the L5.6 reading [W], 3A:692".
- **N4.** SSRC:121 uses the status "open; no verdict", which is outside #1284's four categories.
  Drop the row and add the sentence: "N3.3 (μ-R) reaches no verdict and is not a result of the
  record; it remains open under #1147."
- **N5.** LP:328–331 understates the #1265 precedent. #1265 also abbreviated five full ids of
  working copies that were never committed (`739595fa` message; OA-2 `STATUS.md` at RCN, row
  "Working-copy blob ids"). The precedent supports option (a) more directly than LP says.
- **N6.** LP:251 and SSRC:148: replace "inside the schema" with "inside TUNE-1's initial-condition
  schema (program blocks translates of `C`, `r_O` fixed on all of `O`)".
- **N7.** S3A:123: in the "Resolving evidence" cell, "an exhibited member" would close Gap S. It
  would not verify the scoped finding "no member is exhibited in the records read". Move it to the
  gap paragraph.
- **N8.** LP:69 (G3): add "Project board changes remain unauthorized (c.6873565446) unless the owner
  authorizes them."
- **N9.** S3A:150: W1-1 r4 is `34b1a16f` at `2d064a71` and `8bf64629` on `main` (#1265's
  substitution). The row is provenance, so nothing turns on this. Say so, or drop the commit.
- **N10.** LP:134 and :137: the "Where" cell reads "main" for statements that are SRC's own N3.1 and
  N3.4 readings. Write "package; main", as in the neighbouring rows.

***

## Check-by-check results

1. **Statement-level trace.** Every 3A and SRC line in LP §2.1–2.2 that I opened says what the plan
   says, with these exceptions:
   - the [W]/[R] layer of the L5.6 control row (N3);
   - "excluded under μ-G" (S6);
   - S3A's typing of MP-0a and MP-0b (B3).

   The on/off-`main` labels are right. The conclusions of 5887947616 and 5892912253 are quoted
   accurately in S3A:29–32 and SSRC:24–27. The scope qualifications are not all carried into the
   scoped claims (B2, S5, S14). 5887947616's point 4 is carried in substance by S3A:51: "secondarily
   LACK A SOURCED APPARATUS in the precise sense that preparation, control, repeatability and/or
   readout have not been derived from joint dynamics".
2. **OA-1/2/3.** The blob identity is confirmed, and so is the OA-2 r4 difference at lines 65 and
   958 only. Neither line is cited by either record. No statement either record uses is graded
   known-invalid by #1284. 3A uses Proposition B(ii) (⇐), the r4 replacement, not r1's false
   clause. The contested gap paragraph (OA2:562–575) lies outside every cited range. Two points need
   correcting:
   - the exploratory text in cited OA-3 ranges is OA3:323–326 and :415–416 (S1);
   - several §3.2 grades are inferred rather than #1284's own (S2).

   With those corrections, no TUNE-1 classification, verdict or gap changes. That agrees with LP:214–217.
3. **REC-1 narrowing.** Faithful in direction: neither narrowing strengthens SRC, and SRC's own §7
   asks for exactly this (SRC:425–426, :441–442). C6 is correct as drafted. C9 needs a different
   on-`main` anchor (S3). The rows are byte-identical between REC-1 r7 and r9 at the stated lines;
   I checked all five.
4. **Two gaps.** Distinct, and stated correctly. Gap S is definitional: no member exists in any
   record read (3A:896–908). Gap P is physical: the ready resource is unsourced (SRC:374–384). The
   F-S2 link narrows Gap P without merging the two. L5.4 is rightly kept apart from both. #1278
   is cited within its binary-ring scope, but its use of SRC is misdescribed (S4).
5. **Package composition.** Blob ids, SHA-256 values, line counts and file lists are correct for
   all thirteen files, and no other file is on either branch. The five working-copy ids are
   unresolvable. Two more full ids need an item 3 note (S10). Option (a) is sound (N5).
6. **STATUS notes.** Each check, against both notes:
   - Self-contained: no (B1).
   - Full hypotheses: no (B2, B3, S12).
   - #1284's status categories: yes, except N4.
   - Limitations: S3A yes; SSRC partly (S14).
   - Accountable Issue: yes. Remediation rows: yes.
   - Landing basis left open until #1283: yes, but it needs restating at G2 (S8).
   - All five item 8 conditions: yes, with the extra row of S7 and the open non-author question
     (S15).
   - No self-referential placeholders: yes. Statements that go stale on landing: yes (S8).
   - TUNE-1 paused, and preservation not presented as progress: yes (S3A:9–11, :214–217;
     SSRC:7–8, :217–220).
   - Nothing stronger than its source: no (B2, S5, S6).
7. **Governance.**
   - §A.42 items 2 and 8: tracing complete except for B1 and S10.
   - §A.42 item 3: S10.
   - §A.42 item 5: correctly conditional on #1283's surviving-claim rule.
   - §A.45: G3 is maintenance only (N8).
   - §A.46: items 1, 4, 6 and 7 are stated correctly. Item 2's basis is correctly absent until
     #1283 is adopted or an exception is recorded (LP:434–437).
   - Review conditions: SRC meets both. 3A meets the ChatGPT condition; its non-author condition
     is undetermined on the record (S15).

***

## Owner questions OQ-1 to OQ-11: recommendations

- **OQ-1 (Step 3A's non-author review; substantive result).** On non-authorship, do not record
  "yes" without a basis. The owner decides on a recorded attestation of which agent wrote r1–r3 and
  which reviewed them, quoted in S3A. Failing that, obtain a focused non-author confirmation of r3
  before G2 (S15). On substantive and nonredundant: yes. F-3A-1 to F-3A-3, the conditional
  classification, the seven qualifying items and T1 with the L4 audit go beyond Step 2's records.
  REC-1 r7 and r9 and SRC also cite 3A as a source.
- **OQ-2 (§A.42 item 3 for the objects file).** Option (a), abbreviation as a recorded substitution
  with the old and new blobs in S3A. The #1265 precedent is direct (N5). The package's non-author
  review checks the substitution byte for byte. Record `9f7d2612` and `221754fc` as in S10.
- **OQ-3 (Steps 1–2 without a status note).** Yes: a later reconciliation batch under #1236,
  covering the Step 1–2 records and naming OBS too (S12). It is not a gate for G2. Record it as a
  deferral naming its Issue (§A.45 rule 6), and once #1283 is adopted note that item 8's
  reconciliation clause applies to it.
- **OQ-4 (order of #1284 and the package).** Land #1284 first, and make it a hard precondition of
  the notes as drafted (S9).
- **OQ-5 (REC-1 rows).** Accept closure by narrowing, with the C9 anchor corrected (S3). Do not
  require REC-1 to land first.
- **OQ-6 (PR descriptions).** Append a dated current-status paragraph to #1267 and #1272 without
  rewriting their history, at packaging and only under owner authorization for host writes. It is
  not a landing condition.
- **OQ-7 (planning status).** Agree: update only at G3, after landing, as §A.45 maintenance. No
  earlier update.
- **OQ-8 (placement of the Step 3A note).** Agree: `TUNE-1-STEP3A-STATUS.md` beside the Step 3A
  files.
- **OQ-9 (second guidance message).** Agree: leave it as provenance. Have S3A state that T2(d)
  (3A:866) and the seventh-item wording draw on it, and that no classification does.
- **OQ-10 (plan directory).** Agree that it stays on its branch, on the condition that B1 is applied
  so that no landed note cites it.
- **OQ-11 (mode).** Agree: one pull request, merge commits of `8228b3c2` and then `c539a60c`, and
  landing by merge commit, never squash or rebase. Add the S10 existence check for `9f7d2612` at G2.
