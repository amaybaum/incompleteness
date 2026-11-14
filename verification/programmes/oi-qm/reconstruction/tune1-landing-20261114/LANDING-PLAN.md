# Landing plan: TUNE-1 Step 3A and sourcing records (#1236)

**Paper-only plan. It authorizes nothing, changes no scientific conclusion, adopts no premise and
merges nothing.** It traces the retained conclusions of TUNE-1 Step 3A r3 (#1267) and the TUNE-1
sourcing unit r2 (#1272) to their sources, classifies every reference they make to content off
`main`, records the effect of the #1284 reconciliation on the OA-1/OA-2/OA-3 statements they cite,
keeps the two records' gaps apart, and states the composition of one TUNE-1 preservation package.
The draft status notes in this directory (`STATUS-STEP3A.md`, `STATUS-SOURCING.md`) are written to
this plan; `NOTES-PLAN.md` records sources, decisions and open owner questions.

- **Authority.** #1236 comment 6873565446 (`amaybaum`, 2026-11-14T07:07:09Z), recording the owner's
  message verbatim: "Choose (b) for evidence preservation, while keeping TUNE-1 scientifically paused
  under (c)." "I authorize a paper-only landing plan for #1267 and #1272, following the Bell
  package's preservation approach." The plan is to give each record its own STATUS note, trace all
  off-`main` dependencies "including OA-1/2/3, and check whether #1284's reconciliation affects their
  status", distinguish "Step 3A's candidate-specification gap from #1272's physical sourcing gap",
  "Establish the integration requirements under §A.46, conditional on #1283's adoption", and
  "Receive one independent non-author review before returning for ChatGPT's exact-head review." Its
  boundaries: "Keep TUNE-1 paused scientifically. Do not authorize Step 3B, a new candidate search,
  or a G_SM computation until a physically justified O-RDY resource exists and the relevant
  candidate class is adequately specified." "No merge, new premise, experiment or board change is
  authorized."
- **Accountable Issues.** #1236 (TUNE-1; both records). #1147 (O-RDY, the physical sourcing gap) and
  #866 (native apparatus sourcing, the owner's stated first priority) for the sourcing gap. #1169
  (OA-1/OA-2/OA-3, REC-1).
- **Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`, unchanged when this plan was
  written. "Main:n" is line n of `papers/Main.md` at that commit (blob `0db17597`). Input heads, each
  equal to its remote branch head when read:

  | Label | PR | Branch | Head | Principal file (blob) |
  |---|---|---|---|---|
  | 3A | #1267 | `research/tune1-step3a-1236-20261113` | `8228b3c24e17a17f324b6779b53b04ad296b4308` | `TUNE-1-STEP3A-r3.md` (`7bbec04d`) |
  | SRC | #1272 | `research/tune1-sourcing-1236-20261113` | `c539a60c5081540be033e07aa4f141caa1d0014b` | `TUNE-1-SOURCING-r2.md` (`35c5c116`) |
  | RCN | #1284 | `records/reconcile-1265-oq10-20261113` | `6e2d1ee8b1a30416ba23755c1c7b74d5dd9cd87f` | nine `STATUS.md` notes |
  | A46 | #1283 | `policy/a46-amendment-oq10-20261113` | `f57e576a87fe65399d9f2db2e532abf2378e3ad0` | `AGENTS.md` §A.46 draft |
  | NA | #1278 | `research/codex-native-apparatus-20261113` | `d8b745274a0be4fba4fc8232c2ec5b6a85aeda99` | `ASSESSMENT.md` (`a6661de9`) |
  | REC | #1268 | `research/rec-1-1169-20261113` | `3a3aa1465244565b9645e234e300d6ec191717a0` | `REC-1-r7.md` (`f1ffac0e`), as SRC cites it at `9f7d2612` |
  | OC | #1274 | `research/optc-1230-1232-20261113` | `fef9485712fe0b2c72416bfc900654ff64e7453d` | not cited by 3A or SRC |
  | BL | #1285 | `records/bell-landing-plan-868-20261114` | `ed61696db174c7e0a17be2fd8359c9fa8cb2c983` | format precedent |

  "3A:n" and "SRC:n" are lines of the principal files at those heads. "…" is
  `verification/programmes/oi-qm/reconstruction`. OA1, OA2, OA3 are `…/oa-1-20261112/OA-1-REPORT-r5.md`
  (blob `5a16b213`), `…/oa-2-20261112/OA-2-REPORT-r4.md` (`8f8ddf73`) and
  `…/oa-3-20261112/OA-3-REPORT-r4.md` (`0a36fd05`) on `main`. P, AF, S3, S4, T1 are the TUNE-1 Step 1–2
  files in `…/drafts/tune-1-20261111/` on `main`, as both records define them.
- **Base of 3A.** #1267 branches from `62bdc2cf`, an ancestor of `main`. 3A pins `080cd2be` and
  checks its citations at `62bdc2cf`. `papers/Main.md` (`0db17597`), `papers/SM.md` (`a5202371`) and
  the TUNE-1 Step 1–2 directory are byte-identical at `080cd2be`, `62bdc2cf` and `c3b5f37a`, so every
  Main, SM and Step 1–2 line 3A cites holds at `c3b5f37a`.

**Evidence tags** (as in the inputs). [K] Lean statement on `main`, read, not rebuilt; [P] manuscript
on `main`; [R] research record on `main`, not independently established (§A.46 item 7); [R-off]
research record off `main`; [W] a paper derivation or reading in the cited record; [L] literature,
context only.

**Scientific standing.** TUNE-1 is paused scientifically (c.6873565446). Preserving these records is
not progress toward a native mechanism: no candidate class is specified, no physically justified
O-RDY resource exists, and nothing in this plan changes either.

***

## 1. Dependency order and gates

| Step | Object | Gate (each needs its own recorded owner decision where marked) | Why it comes here |
|---|---|---|---|
| G0 | #1283, §A.46 item 8 | Owner adoption decision; the adoption line's placeholders filled from it; merge (owner). Until then reading R-b stays in force, and neither record has a landing basis (§8). | Item 8 is the landing basis used below. If the adopted text differs from `f57e576a`, the condition tables of §8 are re-checked against it. |
| G1 | #1284, reconciliation of OA-1/OA-2/OA-3 and six other notes | (i) the Basis lines restated after G0 (#1284 open question 6); (ii) record-specific verification of each applicable item 8 condition, record by record, as C2 requires (#1283 c.6872828604); (iii) exact-head CI; (iv) owner merge decision; (v) merge commit. | Recommended before G2, not strictly required: both TUNE-1 status notes grade the OA statements they rely on by #1284's grades (§3). If G2 lands first, those grades are provenance on a branch and the notes cite the OA records' own labels instead (§3.4; NOTES-PLAN OQ-4). No TUNE-1 statement changes either way. |
| G2 | TUNE-1 package (§5) | (i) branch from `main` after G1 (or after G0 if G1 has not landed); (ii) merge commits of `8228b3c2` (3A) then `c539a60c` (SRC); (iii) one commit adding the two status notes; (iv) the §A.42 item 3 decision on `TUNE-1-STEP3A-OBJECTS.md` (§5.5); (v) source drift re-measured against the `main` of that day and the notes re-pinned; (vi) checks (§5.6); (vii) reviews: a non-author review of the two status notes, then a ChatGPT exact-head review of the package head; (viii) owner merge decision; (ix) merge commit. | SRC cites 3A as support off `main` (SRC:429, :434); landing both in one merge closes those rows. 3A cites nothing in SRC. |
| G3 | After G2 | Planning-status updates on #1236 and #1147 under §A.45 rule 3 maintenance, citing the owner's merge record. | Records the landed state; changes no scientific status and no readiness or authorization. |

**Not upstream.** #1274 and #1285: neither record cites them, and neither cites 3A or SRC (searched
both diffs and `main` for the PR numbers, branch names and file names). REC-1 (#1268): SRC cites
REC-1 r7 in six rows; the two rows that use REC content as support are closed by narrowing (§6.2), so
REC-1 need not land first (NOTES-PLAN OQ-5).

**Downstream.** REC-1 r7 cites 3A (REC r7:215, :217, as `3A:279–282, :413–420`, `3A:501` [R-off]);
#1278's assessment cites SRC at `c539a60c` and `890fe3dd` for its comparison and resource statements
(NA `ASSESSMENT.md`:61, :112–116, :163). Their integration obligations for those references close
when G2 lands. Neither is a gate for G2.

**No promotion.** Landing changes no evidence layer. 3A's [W] and SRC's [W, here] items stay paper
derivations, model-reviewed, not verified (§A.46 item 7; #1283 item 8: "landing a record does not
change its evidence layer"). No manuscript statement changes.

***

## 2. Statement-level trace

"Where": **main** = on `main` at `c3b5f37a` (the OA reports came from #1265, merged there); **package**
= lands in G2 from #1267 or #1272; **off** = in another PR's branch (REC-1, #1268) and not landing.
Every 3A line below is at `8228b3c2` and every SRC line at `c539a60c`.

### 2.1 Step 3A r3 (3A)

| Retained conclusion | Source statement (file:line @ head) | Layer | Where |
|---|---|---|---|
| Stop condition met: no INCONCLUSIVE class has fully specified dynamics, preparation and readout; a specification gap, not a quantum failure and not a negative result about any class | 3A:896–908; summary 3A:194–196 | [W] record reading | package |
| | no member exhibited: P:1011–1016; S3:196–229; S4:485–497, :595–614, :668–674 | [R] | main |
| | the reviewer's search confirming it: `TUNE-1-STEP3A-REVIEW.md`:355–359 | review | package |
| No candidate qualifies for Step 3B | 3A:910–911; owner gate #1236 c.6846442383 | [W] on [R] | package |
| Every class stays INCONCLUSIVE (not excluded, not shown to survive) | 3A:481–483, :907–908; S3:213–229; S4:595–614, :654–674 | [R] (Step 2 [W], reviewed under Step 2's gates) | main |
| Contents of a qualifying candidate (seven items) | 3A:913–931 | [W] | package |
| Classification A–D: primary **underspecified**, secondary **lacks a sourced apparatus** | 3A:210–218; ledger 3A:485–506; A.7 :628–632, B.7 :665–668, C.7 :707–710, D.7 :771–774 | [W] on [R] (P, AF, S3, S4) and [P] (Main:724) | package; main |
| Conditional: init members of A and C with (SP) are classical-only in their prepare–measure fragment; without (SP), preparation-noncontextual, and whether that excludes T1 is open at [L] level | 3A:212, :214, :591–606, :698–706 (hypothesis match [W]) | [W] match on [R] | package |
| | OA-2 Theorem E(b) and verdict N2.4, OA2:522–560; (SP) halves OA2:534, :542–544; measure table OA2:746, :750 | [R], partially verified (§3) | main |
| B and exchange rows outside Theorem E(b) | 3A:660–668; OA2:173, :501 | [W] reading on [R] | package; main |
| D: no result excludes or classicalizes it | 3A:753–774; OA2:674, :765, :775–779; Corollary E1 OA2:577–600 | [W] on [R] | package; main |
| Control is translation-only for R-lin under every law | 3A:566–571, :690–694; Lemma A-T S3:62–68, :79–85; OA2:525–527; OA1:523 | [R] | main |
| F-3A-1 (ELABORATING): law change leaves R-lin control translation-only | 3A:963–968 | [W]; [R] | package |
| F-3A-2 (ELABORATING): run repetition used but not stated | 3A:969–986, :494 | [W] | package |
| | AF:283–287; P:174–175; T1:249, :1625, :1696; OA1:556–562; Main:443–449, :498, :742–758 | [R]; [P] | main |
| F-3A-3 to F-3A-6 | 3A:987–997 | [W] on [R] | package |
| T1, the approximate single-qubit test with the L4 escape audit | 3A:783–837; P:439–486, :603–623, :842–849; AF:80–298; S3:276–289; S4:487–491, :519–523 | restatement of [R] | package; main |
| T2, a proposal for the owner, not an authorized test | 3A:839–880 | proposal; claims no result | package |
| | its controls: `𝔊_K` OA2:381–490; OA-3 Theorem S OA3:294–347 | [R] (Theorem S: see §3.2) | main |
| §2A framing: inclusion, access and control distinguished; reachable versus definable; Level A and Level B; preparation as derivation; "embeddedness plus incomplete observation does not by itself select quantum mechanics" | 3A:246–458 (conclusion :405–409) | framing; [W] reading of [P] and [R] | package |
| | Main:26, :28, :42, :58, :60, :360, :414, :427, :431, :496, :554, :562, :580, :582; SM:104; OA2:381–490, :550–556, :769; OA3:138–141 | [P]; [R] | main |
| §2A.6: no classification, verdict or Step 3B answer changes | 3A:411–439 | [W] | package |
| §2A.6: NL-C applies to any per-round gate setting on a bounded cell set, designated or emergent | 3A:433–439; S4:423–462, :697 | [R] | main |
| Pressure tests: D is not "viable"; incompleteness in form only; L5.6 is no escape; A/C classification is not a negative result | 3A:937–957 | [W] | package |

### 2.2 Sourcing r2 (SRC)

| Retained conclusion | Source statement (file:line @ head) | Layer | Where |
|---|---|---|---|
| Verdict STOP AT MISSING INGREDIENT, at part (b): the ready resource | SRC:14–21, :364–386 | [W] on [R] and [P] | package |
| Candidate TC-A: R-lin, `𝓛_fin`, initial-condition mode, `D_0`-form law, heralded witnesses, unbounded `|C_n|` | SRC:100–129 | [W] selection | package |
| | candidate A of 3A (3A:212, :531–632) | [W] | package (3A) |
| | P:85–89, :123–125, :131–133, :184–199; S3:58–60, :196–214; S4:668–674; OA1:556–558; Main:58 | [R]; [P] | main |
| Selection: every other class adds an unadopted hypothesis first | SRC:161–183 (N0) | [W] on [R] | package; main (P:90–129, :155–167; OA1:111, :183, :522; #1236 c.6817129920) |
| NL-C applies at every interface of TC-A; the FAIL-CLASS family condition is not met; this is compliance, not escape | SRC:185–224 (N1) | [W] on [R] | package |
| | S4:423–474, :641–650, :697–698; OA1:111–114, :176–208 | [R] | main |
| Part (a) premise-relative; (c) mechanism derived (translation form only), content blocked with (b); (d) read rule imported; (e) MP-0b convention only; (f) growth unsourced | SRC:137–149 | [W] on [R], [P] | package; main |
| (b) excluded under μ-G (Lemma P-1) | SRC:239–246 (N3.1); OBS:529–545; OA1:145–160, :147, :522 | [R] | main |
| (b) not supplied unconditionally under μ-O; conditional route open | SRC:247–251 (N3.2) | [W, here] | package |
| (b) under μ-R undecided | SRC:252–255 (N3.3); NPS1:85; REC r7:220 (C9) | [W]; [R]; [R-off] (narrowed, §6.2) | package; main; off |
| (b) covered only by unadopted MP-0a or open H-PREP | SRC:256–263 (N3.4); Main:58; OA1:556–562; OBS:893–901 | [R]; [P] | main |
| No native producer on `main` for R-lin, within the searches made | SRC:264–275 (N3.5), :403–407; OBS:100, :121; NPS1:14, :88; NIS2:132; Main:443–449, :742 | [R] (NPS1, NIS2: partially verified, binary ring, §3.3); [P] | main |
| N3.6 / F-S5: spatial copies give independent runs, given a supply per copy | SRC:276–281, :352–353 | [W, here] | package |
| F-S1: NL-C's counting covers gates of `m` rounds with `m + 1 ≤ L`; gates of `L` or more rounds open | SRC:200–210, :321–329 | [W, here] | package |
| F-S2: at least `(K + 1) log_q((1−4ε)/(4ε))` known `q`-ary cells per run; under μ-G probability at most `(4ε/(1−4ε))^{K+1}`; with `D` known cells per run, `ε ≥ 1/(4(1 + q^{D/(K+1)}))`; necessity only, inside the initial-condition schema | SRC:330–345 | [W, here] arithmetic on NL-C′ (S4:464–474 [R]) | package |
| F-S3: the stop coincides with OA-1 gap 1, O-RDY, and the first stops of NPS1 and NIS2 for another rule | SRC:346–349 | [W] on [R] | package; main |
| F-S4: under μ-O only orbit-constant cells are unconditionally known | SRC:350–351 | [W, here] | package |
| Member specification and L5.4 are open and are not the stop | SRC:146–149, :289–297, :383–384 | [W] | package |
| Step 3B not eligible | SRC:385–386 | [W] | package |

### 2.3 Dependencies and facts the input records do not state

- **OA reports are on `main`.** 3A cites OA-1 r5, OA-2 r4 and OA-3 r4 at `2d064a71` as off `main`
  (3A:29–33). `2d064a71` is an ancestor of `c3b5f37a`. OA-1 r5 (`5a16b213`) and OA-3 r4 (`0a36fd05`)
  are the same blobs. OA-2 r4 is `9a6e3682` at `2d064a71` and `8f8ddf73` on `main`; the two differ on
  lines 65 and 958 only (#1265's recorded substitution, `…/oa-2-20261112/OBJECTS.md`), neither of
  which 3A or SRC cites. Every OA line both records cite resolves on `main` unchanged.
- **Cited ranges that contain text graded exploratory.** 3A cites OA3:294–347 (Theorem S) and
  OA3:394–416 (N4.1). OA3:323 (N3 proof step 1, the C-PM coin weight) and OA3:415 (N4.1, the
  ensemble-conditioning sub-bullet) are delta-review text that #1284 grades exploratory
  (`…/oa-3-20261112/STATUS.md` at RCN, results table; OA3:801, :809–823). 3A uses Theorem S as
  context and as a T2 control expectation (3A:618–623, :879–880), and uses N4.1's held-at-use
  branch (3A:607–610), not the ensemble branch. No 3A classification rests on either line.
- **TUNE-1 Steps 1–2 carry no status note on `main`.** Both records rest on Step 2 results (Lemma A-T,
  FC-1, Lemma I, NL-C, NL-C′, the class definitions) as [R]. Those records landed by #1237's merge
  (`c03a5764`) before §A.46 item 8 was drafted and are not in #1284's batch 1 (NOTES-PLAN OQ-3).
- **SRC's [R] inputs in #1284's batch.** NPS1 and NIS2 (`native-preparation-source-1-20261110`,
  `native-interaction-source-2-20261110`) are graded partially verified in #1284, bounded to the
  selected binary SM ring. SRC uses their stop lines only as confirming context for another rule
  (F-S3), so the grading changes nothing in SRC.
- **REC-1 P0 bears on 3A's open (SP) item.** 3A:613–617 records the reviewer's remark that (SP) for
  coset-uniform laws "may resolve cheaply". REC-1 P0 r3 on #1268's branch addresses the coset-space
  model; it is off `main`, unreviewed by ChatGPT, and not used here or by either record (SRC:297
  names it as separately authorized). No 3A classification is re-read through it.
- **Full ids of working copies in `TUNE-1-STEP3A-OBJECTS.md`.** The file names five reviewed
  working-copy blobs by full 40-character id (`4a6c1127`, `17076ef7`, `65217dc0`, `4a9c9aa6`,
  `3910f411`, given here abbreviated). None is reachable from any ref of the repository; these copies
  were never committed. §A.42 item 3 requires a full id in a governed record to name an object that
  exists in the repository when the record lands (§5.5).
- **#1278 reads both SRC objects.** NA compares the confirmed SRC at `890fe3dd` (paper blob `20ee9b04`)
  with the head `c539a60c` (`35c5c116`) and states that the only paper delta is the cosmetic nit
  (NA `ASSESSMENT.md`:114). `git diff 890fe3dd c539a60c` agrees: SRC:3–6, `RESPONSE-r1.md`:3–4, a new
  section in `OBJECTS.md` and the added `CONFIRM-r2.md`.

***

## 3. OA-1/OA-2/OA-3: status before and after #1284, and the effect on TUNE-1

### 3.1 The two states

| Note | On `main` at `c3b5f37a` (before #1284) | At RCN `6e2d1ee8` (after #1284) |
|---|---|---|
| OA-1 `STATUS.md` (`39222596` → `0df3793a`) | "What the record establishes"; Basis "§A.46 item 2: the record supports the claim above" | "What the record supports, and at what strength"; every result partially verified; D8 exploratory; known-invalid none stated; Basis open until the §A.46 amendment is adopted or an owner exception is recorded |
| OA-2 `STATUS.md` (`7945ac8a` → `ebd60f78`) | as OA-1 | every result partially verified; known-invalid: r1's Proposition B second clause and Corollary B′, and r1's class-N reason, kept as review trail; contested, not graded known-invalid: the gap paragraph r4:566–567 (OA-3 N4); Basis open as OA-1 |
| OA-3 `STATUS.md` (`9b1f6f5a` → `0c52ad57`) | as OA-1 | every result partially verified; delta-review-supplied edits and the three `G_SM` design proposals exploratory; known-invalid none stated; Basis open as OA-1 |

#1284's grades restate each note's own evidence; it changes no OA report (ChatGPT review 5900793856 at
`6e2d1ee8`: "ACCEPT as a nine-file, status-only governance reconciliation, conditional on the separate
§A.46 amendment/owner exception for the landing basis").

### 3.2 Each OA statement the TUNE-1 records use

| OA statement | Used by | Grade after #1284 | Known-invalid, contested or exploratory part? | Effect on the TUNE-1 use |
|---|---|---|---|---|
| OA-2 Theorem E(b) and verdict N2.4 (OA2:522–560) | 3A conditional groups of A and C; §2A.5; F-3A-1, F-3A-3; SRC N4 (context) | partially verified; conditional on (H1), H-AR, (H3), (H4), (SP), (xiv) | No. It uses Proposition B(ii) (⇐), which holds for every law (OA2:746); the r1 false clause is the measurement-noncontextuality clause that r4 replaces | None. The groups stay conditional on E(b)'s hypotheses and on 3A's [W] hypothesis match; "WIP, off `main`" (3A:956, :1002) reads as "research record on `main`, partially verified, not established" |
| OA-2 Theorem E(a), measure table (OA2:525–527, :746, :750) | 3A A.4, C.4, C.6 | partially verified | No | None |
| OA-2 Corollary E1 (OA2:577–604) | 3A D.6; §6 | partially verified (as E(b)) | No. The contested gap paragraph lies in OA2:562–575 (r4:566–567), outside the cited range | None |
| OA-2 `𝔊_K` (OA2:381–490, :769) | 3A §2A.5, D.6, T2 controls | partially verified; conditional on C-PM′, C-PM and a uniform bath under μ-G | No | None |
| OA-2 setup (OA2:102–104, :173, :499, :501) | 3A A.6, B.6, C.6 | partially verified | No | None |
| OA-1 gap 1, MP-0a, MP-0b (OA1:522, :556–566) | 3A §3.0, §2A.4, F-3A-2; SRC (b), (e), N3.4, F-S3 | partially verified; gap 1 conditional on μ-G; [W] items reviewed only by a model of the author's family (OA1:656) | No | None. MP-0a and MP-0b stay named, unadopted |
| OA-1 gap 2, D5, D7 (OA1:176–208, :523) | 3A A.4, C.4; SRC (c), N1.4, N1.5 | partially verified | No | None |
| OA-1 D1–D4 (OA1:141–175) | SRC N3.1, N3.2, (e) | partially verified | No. D8 (exploratory) is outside the cited range; OA1:174 names it only | None |
| OA-1 typing of measures, §4.2 target, R5 (OA1:96–110, :437–446, :488–512) | 3A §3.0, A.6 | partially verified | No | None |
| OA-3 Lemma OBS, Theorem S, scope (OA3:223–268, :294–347, :383–386) | 3A A.4, A.6, §2A.6, T2 control row | partially verified; Theorem S conditional on MP-0b or (V-ii-H), heralds, a stage of at least `2(L−2)` and (PT) | Yes: OA3:323 lies in Theorem S's proof and is exploratory | None on a classification: 3A states that Lemma OBS and Theorem S do not apply to its candidates as stated; the T2 control row "classical-reducible [R-off]" rests on Theorem S, a partially verified result whose proof step 1 includes exploratory text, and T2 is an unadopted proposal |
| OA-3 N4.1, N4.3 (OA3:120–127, :394–416, :455–476) | 3A A.6 (herald typing; (H4) replaceable) | partially verified; conditional on (H1), H-AR, (H3), (xiv), (SP) | Yes: OA3:415 is exploratory | None: 3A uses the held-at-use branch, met by D4/MP-0b "by convention [W reading]" |
| OA-3 quotation of MECH-2 (OA3:138–141) | 3A §2A.2 | partially verified ([R] record) | No | None |

**Result.** No statement either record uses is graded known-invalid in #1284. Two cited ranges contain
lines graded exploratory, and neither line carries a TUNE-1 conclusion. #1284 changes the label of
every OA input from off-`main` WIP research to a partially verified research record on `main` whose
landing basis is open; it changes no TUNE-1 classification, verdict or gap.

### 3.3 Other #1284 notes the records rely on

NPS1 and NIS2 (§2.3): partially verified, bounded to the binary SM ring; SRC's F-S3 uses them as
confirming context. W1-1: 3A records "No bearing found" (3A:1047–1049). The PREP-MIN and WAVE-SIGN
notes are not cited.

### 3.4 If G2 lands before G1

The status notes then cite each OA statement with the record's own labels on `main` ([W], [RW],
"reviewed only by a same-family model", OA1:656; "unreviewed" delta-review text, OA3:7–9) and the
#1284 grades as provenance at `6e2d1ee8`. Once G1 lands, the notes' rows are re-pointed to the
landed notes as a correction in place.

***

## 4. The two gaps, kept apart

| | **Gap S: candidate specification (Step 3A)** | **Gap P: physical sourcing, O-RDY (#1272)** |
|---|---|---|
| What is missing | A concrete member of any INCONCLUSIVE class: the generating rule `n ↦ (O_n, C_n, τ_n, r_{O,n}, layout_n)`, `n(ε, K)`, the target with `L` and `c₀`, the encoder with its D6(b) classes and `G(ε, K)` (3A:913–931) | A native producer, inside the joint dynamics, of known-value cells for `r_{O,n}` and the program blocks, renewed every run, at least `(K + 1) log_q((1−4ε)/(4ε))` `q`-ary cells per run within TUNE-1's initial-condition schema (SRC:374–379, F-S2) |
| Kind | Definitional: the classes are existentially quantified in every Step 2 record and no member is exhibited (3A:902–905) | Physical: the first part of TC-A not shown to follow from OI's stated premises (SRC:146–149) |
| Scope | All four classes A–D | TC-A (R-lin, init mode, `𝓛_fin`, `D_0` law); by AW-SRC-2, any candidate inside the initial-condition schema inherits it at least at the F-S2 rate |
| Measure dependence | None | Excluded under μ-G; not supplied unconditionally under μ-O, conditional route open; undecided under μ-R (SRC:282–287) |
| What it is not | Not a quantum failure; not an exclusion (3A:907–908) | Not an OI-wide no-go; not a minimum-cost proof (review 5892912253: "a sourcing stop, not an OI-wide no-go") |
| Would close it | A submission meeting 3A §5's seven items | A physically justified ready resource; the corpus names only the unadopted MP-0a, the open H-PREP and the open obligation O-RDY |
| Accountable Issue | #1236 | #1147 (O-RDY); #866 (native apparatus sourcing) |
| Authorization | A new candidate search is not authorized (c.6873565446) | Not authorized under #1147 (`not authorized`); #866 is the owner's first priority |

**Why they are distinct.** SRC places the member specification and L5.4 outside its stop:
"Not physical ingredients, and still open. The member specification (encoder, layout, `O_n`, `C_n`,
`τ`) and L5.4. Neither is the stop." (SRC:383–384). Supplying O-RDY would leave Gap S open, since no
member would yet be exhibited; exhibiting a member inside the schema would leave Gap P open, since by
F-S2 and AW-SRC-2 it inherits the ready resource. 3A's secondary group **lacks a sourced apparatus**
(3A:493, :505, :628) lists unsourced ingredients of every class; SRC identifies the first of them for
one candidate as a precise physical stop and links two of 3A's listed items by necessity (F-S2). That
link narrows Gap P; it does not merge it with Gap S.

**A third open item, neither gap.** L5.4, whether label translations under a coset-uniform law can
meet Q3′, Q4, Q5′, Q6′ with heralded witnesses, is a mathematical question the owner left open
("Record and leave", S4:12). It is not a physical ingredient (SRC:141) and not a specification item.

**#1278 on Gap P.** The owner accepted #1278's bounded source assessment (c.6873565446: "It found no
physically supplied O-RDY mechanism. Physical source remains NOT PASSED."). ChatGPT review 5898054706
at `d8b74527`: "**Physical source NOT PASSED**. No new apparatus candidate, quantum operation, OI→QM
equivalence, impossibility theorem, or native producer follows." NA's assessment concerns the binary
SM ring branch (G_SM/SMR), not R-lin (NA `ASSESSMENT.md`:38), and reads SRC only as off-`main`
context (NA `ASSESSMENT.md`:61, :116). Its bearing on Gap P is that no physically supplied ready
producer is identified in the corpus for either rule; it does not close or narrow Gap P for TC-A. Both
owner conditions for resuming TUNE-1 stay unmet: no physically justified O-RDY resource exists, and
no candidate class is adequately specified.

***

## 5. Package composition

### 5.1 3A, byte-identical, by merge of `8228b3c2`

Directory `…/drafts/tune-1-20261111/` (the Step 1–2 directory on `main`; no file name collides).
Commits: `b923fa7f` (r1, review, r2; parent `62bdc2cf`), `8228b3c2` (r3, extended review).

| File | Blob | SHA-256 | Lines |
|---|---|---|---|
| `TUNE-1-STEP3A.md` (r1) | `b20524f31d3c1706948b9529bbe5a0fe259eb0dc` | `ef63ccb9e5b217ddb24332be73a3fd99f020f51f7c59f2dc2db30727f5a754f0` | 699 |
| `TUNE-1-STEP3A-r2.md` | `313a76e35f65c8ced2791d22c0570d559b882db4` | `9d04f3a4ecaf8991cded6e5126f04f58987bb92a11c1680891ce6177425f07e7` | 872 |
| `TUNE-1-STEP3A-r3.md` | `7bbec04d7bee91673c3241e78a289bba28fb1ea5` | `8b44fe4f9ca2e31a1dfec5a8c485eb1547e8ccd4961c7f79cb614d886d89b385` | 1157 |
| `TUNE-1-STEP3A-REVIEW.md` | `49a5d52a65817d07b24a2dfb114671ab19bde6e0` | `3401e3fae1bf8027e9997f5addae99cee68c2f451ffe88a71f0b2282f41fb83b` | 797 |
| `TUNE-1-STEP3A-OBJECTS.md` | `ed2501e395579a792d1f5ca951273901ba42d0b8` | `3b6a596a14ba2da36ac57791af4201768d2e84af72935f0a5b45e4b5701b8368` | 22 |

The committed blobs of r1, r2, r3 and REVIEW equal the "Committed blob" and "Committed SHA-256"
columns of `TUNE-1-STEP3A-OBJECTS.md`. r1 and r2 land because the review and r3 cite their lines.

### 5.2 SRC, byte-identical, by merge of `c539a60c`

Directory `…/drafts/tune-1-sourcing-20261113/` (new). Commits: `890fe3dd` (r1, review, r2; parent
`c3b5f37a`), `c539a60c` (confirmation, cosmetic nit).

| File | Blob | SHA-256 | Lines |
|---|---|---|---|
| `TUNE-1-SOURCING-r1.md` | `e21299f97c022c724b85f02d714b4644d0f8d87d` | `5d1d96fc37a9ae003e5c829fd4907240800a26d0a42c6568d8f204860b168d0b` | 409 |
| `TUNE-1-SOURCING-r2.md` | `35c5c116c017ed03a2eacfbeccfed457bae4649b` | `c0e53684daedfa32e62bf6af26f8b778916c230baa4ac5d76a09e77ded9cb758` | 442 |
| `REVIEW-r1.md` | `723476883724472189a27c54364d7ddd94545375` | `d9c9f7d22d4bcda20b30c8c9268dab30b4be191fb9d39831ff126b0fdd702bd2` | 361 |
| `RESPONSE-r1.md` | `66c38e4fdc0d80e4fa94138ae6e04317c4b5c925` | `a3c216695c37df29b7fc1ed205278fad5d574264c17009d3458d2be923cce0c6` | 33 |
| `CONFIRM-r2.md` | `558ddc7776bc1d5115e86c449cf27f4ec1d8c8f8` | `2071bcbf287c049b6ea3f6d028912913a46730e684639f1ec88544f012857ab5` | 106 |
| `NOTES-r1.md` | `5ac597e96cd8177f833f8d4b86a879c19ee77480` | `e96229a247caec1ba6ef466af61b37fb9383d6405ae6659f6082385d3e1b1de3` | 32 |
| `NOTES-r2.md` | `a1af11feef801638cb56bd4d19687d660a70ac11` | `49f6531833c3da79fb3a35e659144abf5b96eea53e9e2d89056a0b79145bae75` | 36 |
| `OBJECTS.md` | `233937b37f735416fce58525e1c7cc21d82fc0e7` | `0503e94e60981adf5c2ee39396a41bb11bcf01441f2e470e77b7b5d59ed73954` | 16 |

`TUNE-1-SOURCING-r2.md` and `RESPONSE-r1.md` differ from the confirmed objects at `890fe3dd`
(`20ee9b04`, `3f25dd28`) by the cosmetic nit `OBJECTS.md` records; their "reviewed sha256" column
refers to the earlier bytes, as it states. All eight land: the review, response and confirmation
cite r1, r2 and the notes by line.

### 5.3 New files written in G2

| Planned path | Content | Source |
|---|---|---|
| `…/drafts/tune-1-20261111/TUNE-1-STEP3A-STATUS.md` | from `STATUS-STEP3A.md` here | this plan |
| `…/drafts/tune-1-sourcing-20261113/STATUS.md` | from `STATUS-SOURCING.md` here | this plan |

The Step 3A note is named for the Step 3A files, because the directory also holds the Step 1–2
records, which it does not cover (NOTES-PLAN OQ-3, OQ-8).

### 5.4 Not in the package

REC-1 (#1268) and REC-1 P0; #1278's three files; this plan directory, which stays on its branch as a
planning record (NOTES-PLAN OQ-10); a status note for TUNE-1 Steps 1–2 (OQ-3).

### 5.5 `TUNE-1-STEP3A-OBJECTS.md` and §A.42 item 3

The five full working-copy ids (§2.3) name no object in the repository. #1265 met the same rule by a
recorded substitution: the reviewed blobs were in that PR's history, and the committed review files
abbreviated the full ids to 8 characters (`739595fa`, recorded in each directory's `OBJECTS.md`).
Here the reviewed copies were never committed, and the ids sit in the objects file itself. Options
for the owner (NOTES-PLAN OQ-2):
- **(a)** at packaging, abbreviate the five ids in `TUNE-1-STEP3A-OBJECTS.md` to 8 characters as a
  recorded substitution, stated in `TUNE-1-STEP3A-STATUS.md` with the old and new blob of the objects
  file; the reviewed SHA-256 values stay full, so each reviewed copy remains identified by content;
  no line of r1, r2, r3 or REVIEW changes;
- **(b)** land the objects file unchanged under a recorded owner exception to §A.42 item 3 for those
  five ids.
Recommendation: (a). It changes a bookkeeping file only, keeps every line number, and follows #1265.

### 5.6 Mode and checks

- **Mode.** One pull request; merge commits of `8228b3c2` and `c539a60c` into a branch from `main`
  (new files only, so no conflict is expected); one commit adding §5.3 (and, under OQ-2 (a), the
  substitution); landing by merge commit, so `b923fa7f`, `8228b3c2`, `890fe3dd` and `c539a60c`, which
  the reviews name, stay ancestors of `main` (§A.42 items 2–3).
- **Checks at the package head.** `tools/claims_check.py`, `tools/staleness_check.py`,
  `tools/voice_check.py`, `tools/artifact_placement_check.py`, `python3 tools/legacy_records_check.py
  <head>`, the SC-42 integration check with its `cmp` against `sc42-integration-result.json`, and
  exact-head CI. Both PRs report SC-42, claims and placement passing at their heads (#1267 body;
  #1272 body and c.6855189619); they are re-run on the combined head. Neither record has a probe or
  a computation to replay.

***

## 6. §A.42 item 8: every off-`main` reference, classified at package landing

Classification after G2. "Package" means the content lands in the same merge.

### 6.1 References made by 3A

| Reference | Attached to | Classification at landing |
|---|---|---|
| OA-1 r5, OA-2 r4, OA-3 r4 at `2d064a71` (3A:29–33, every [R-off] tag) | conditional groups of A and C; §2A; §3.0; A.4–A.6, C.6, D.6; T2 controls | **support on `main`**: `2d064a71` is an ancestor of `main`; OA-1 and OA-3 the same blobs; OA-2 differs on lines 65 and 958, which 3A does not cite. Each statement carries #1284's grade (§3.2) |
| W1-1 r4 at `2d064a71` | §9 inventory, "no bearing" | provenance |
| `DELTA-REVIEW-OA-3-r4.md` (3A:1050–1051) | not read beyond its existence | provenance |
| commits `080cd2be`, `62bdc2cf`, `59557ee8` | pins | on `main` (ancestors) |
| commits `b923fa7f`, `8228b3c2` | review objects | on `main` once merged by merge commit |
| `.r3-pre-review.md` (3A:8, :1125) | the pre-review text the r3 confirmation compared against | provenance: not retained; the confirmation's verdict rests on the committed r3 and its diff map (REVIEW:754–797); the ChatGPT review is of the committed blob |
| reviewed working copies, by full id in `TUNE-1-STEP3A-OBJECTS.md` | identity of reviewed bytes | provenance; their full ids are a §A.42 item 3 gap (§5.5) |
| session paths written `working/…` (REVIEW:3, :396, :403, :508, :527; 3A:1068) | reviewer and writer disclosure | provenance |
| #1236 c.6846408321, c.6846442383, c.6847314661, c.6828822665, c.6816189419, c.6817129920 | authority, guidance, framing | governance provenance, quoted in 3A |
| second guidance message, relay only (3A:139–150) | T2(d); interference versus tables (A.5 and the like) | provenance: not on #1236; no classification rests on it (A.5, B.5, C.5, D.5 read "not shown either way"); T2 is a proposal (NOTES-PLAN OQ-9) |
| [L] items (Spekkens 2005, 2009; Schmid et al. 2021) | T2; A.6 | provenance; no verdict rests on them |
| review 5887947616 | ChatGPT exact-head review | review provenance |

### 6.2 References made by SRC (its own table, SRC:419–442, re-classified at landing)

| Reference | Attached to | Classification at landing |
|---|---|---|
| 3A at `8228b3c2`: candidate A, statement (i) formulation, "no member exhibited" (3A:896–905) | §1; N0.3; N4 | **support on `main`** (package); blob `7bbec04d` unchanged |
| 3A:493, :501, :505, :794–805, :436–439, :969–986 | F-S2, (e), §1, F-S1, N3.6 | provenance, as SRC classifies them; the content used is on `main` |
| REC r7 at `9f7d2612` (§0 safeguards, three-way separation) | §0 | governance and scope provenance; the separation is the owner's safeguard (#1169 c.6848268369) |
| REC:215 (C4) | N1.4 | support on `main`: OA1:111–114, Main:42 |
| REC:217 (C6), the status word "undetermined" for MP-0b | (e) | **support off `main`: gap closed by narrowing** in `STATUS-SOURCING.md`: (e)'s marking "named hypothesis MP-0b only" rests on OA1:563–564 ("MP-0b … interface convention"); the parenthesis "status undetermined" is REC-1's classification, context, not a result of SRC |
| REC:220 (C9) | N3.3 | **support off `main`: gap closed by narrowing**: N3.3 reaches no verdict ("Undecided; no source"); the circularity concern is also on `main` at NPS1:85; the REC quotation is context |
| REC:222 (C11) | (b), N3.4 | support on `main`: OA1:556–562 ("Missing premises", MP-0a, "Hard to vary? No"), Main:58, and §A.45 rule 5 (a new premise is judged under §A.29); the wording "new §A.29 premise if selected" is REC-1's |
| REC:223 (C12), H-xiv | (c) | provenance for the name; the hypothesis used is H-μ (P:145) and (xiv) (Main:724) |
| REC-1 P0 (SRC:297; NOTES-r2 item 7) | N4 context | provenance |
| commits `890fe3dd`, `c539a60c` | review objects | on `main` once merged by merge commit |
| #1169 c.6854241002, c.6848268369, c.6854774010; #1236 c.6817129920, c.6828822665; #866 c.6765161496; #1147 body; #914 c.6563412926 (NOTES-r2) | authority, safeguards, obligation name | governance and planning provenance, quoted |
| reviews 5892912253 | ChatGPT exact-head review | review provenance |

The REC rows are re-checked at REC-1 r9 (`3a3aa146`): rows C4, C6, C9, C11 and C12 are byte-identical
in r9 at lines 223, 225, 228, 230 and 231. If REC-1 lands later, the two narrowed rows may be
re-pointed to it as a correction in place.

### 6.3 References made by the two status notes

| Reference | Classification at landing |
|---|---|
| #1283 at `f57e576a` | provenance until adopted; the Basis then cites the adopted §A.46 on `main` |
| #1284 at `6e2d1ee8` | provenance until G1 lands; then support on `main` for the grades quoted |
| #1278 at `d8b74527`, review 5898054706, the owner's acceptance in c.6873565446 | governance provenance for the statement that physical source is not passed; Gap P's open status rests on OBS:100, :121, NPS1:14, NIS2:132 and SRC itself on `main` |
| #1236 c.6873565446, c.6847882040 | governance provenance, quoted |
| reviews 5887947616, 5892912253 | review provenance |
| owner comments quoted in the notes | governance provenance |

No reference is a gap at landing once the two REC rows are narrowed and §5.5 is decided.

***

## 7. Review-condition status

#1283 item 8 requires "an independent non-author review and a ChatGPT exact-head review".

| | 3A | SRC | The two status notes and this plan |
|---|---|---|---|
| Non-author review | `TUNE-1-STEP3A-REVIEW.md`: review of r1, ACCEPT WITH CHANGES (R1–R7, m1–m4, R8); recheck of r2, ACCEPT; review of r3 (§2A), ACCEPT WITH CHANGES (E1–E7, n1–n4); confirmation of r3, ACCEPT. The file names its reviewer "Independent internal review (same model family)" (REVIEW:6) and does not state non-authorship in those words (NOTES-PLAN OQ-1) | `REVIEW-r1.md`: "Fresh non-author reviewer (not the writer of this unit, Step 3A, or REC-1)", ACCEPT WITH CHANGES (R1–R6, m1–m10); `CONFIRM-r2.md` at `890fe3dd`: CONFIRMED, one cosmetic nit | **pending**: one independent non-author review of the complete plan (c.6873565446) |
| ChatGPT exact-head review | 5887947616 at `8228b3c2`: "ACCEPT WITH SCOPE QUALIFICATIONS"; nonblocking: the r3 header "awaiting confirmation" | 5892912253 at `c539a60c`: "ACCEPT (bounded paper-only sourcing result)" | **pending**: after the non-author review; the package head needs its own at G2 |
| Bytes reviewed versus bytes landed | ChatGPT reviewed the committed blobs; the non-author reviews read working copies that differ only by the recorded `working` substitution (OBJECTS) | the non-author confirmation covers `890fe3dd`; the delta to `c539a60c` is the cosmetic nit, covered by the ChatGPT exact-head review | — |

The ChatGPT review of 3A also states: "#1267 remains DRAFT / NOT FOR MERGE" and "Accepted OA records on
#1265 remain off main until separately integrated" (both written before #1265's merge at
`c3b5f37a`). SRC's review: "Any eventual landing needs its own dependency/CI/integration gate."

***

## 8. Integration requirements under §A.46 (conditional on #1283's adoption)

Every requirement below is stated against #1283 at `f57e576a` and lapses or changes with the adopted
text.

1. **Item 2 basis.** Neither record supports an established claim, carries a computation, or is
   needed by a record on `main` (searched: no file on `main` cites #1267, #1272 or their file names).
   The only basis is "when item 8 preserves it". Before adoption no basis exists; under reading R-b a
   landing would need a recorded owner exception (#1169 c.6865680499).
2. **Item 8 conditions, record by record** (record-specific verification, as C2 requires of the
   reconciliation and as this plan applies to new records):

   | Condition | 3A | SRC |
   |---|---|---|
   | substantive, nonredundant result (may be conditional, negative or inconclusive) | met: the conditional classification under OA-2 Theorem E(b) with both (SP) halves, F-3A-2 (run repetition), T1 with the L4 audit, the Step 3B gate answer and §2A; its own productivity verdict is "gem, BORDERLINE" (3A:999–1002), and the specification gap restates S3:206–211 and S4:485–497 (OQ-1) | met: the TC-A stop, F-S1 and F-S2 (no equivalent on `main`; productivity "gem (ELABORATING)", SRC:355–360) |
   | scope and evidence limits documented | met in 3A §§5–8 and `STATUS-STEP3A.md` | met in SRC §§4–5 and `STATUS-SOURCING.md` |
   | non-author review and ChatGPT exact-head review | ChatGPT met; non-author met subject to OQ-1 | met |
   | landing checks and §A.42 item 8 tracing | tracing: §6; item 3: §5.5 pending; checks pending at the package head | tracing: §6 (two rows narrowed); checks pending |
   | accountable Issue, verification status, remediation plan | #1236; `STATUS-STEP3A.md` | #1236 (O-RDY under #1147); `STATUS-SOURCING.md` |
   | explicit rationale | c.6873565446: "This preserves accepted research without falsely treating preservation as progress toward a native mechanism."; SRC and REC-1 cite it | as 3A; #1278 cites it |
   | separate owner merge decision | **not recorded** | **not recorded** |
   | historical authorization | #1236 c.6846408321, c.6846442383, c.6847314661 | #1169 c.6854241002, item 1 |
3. **Item 1.** Neither record presents an established claim, and landing establishes none. Each note
   states "preserved, not established".
4. **Item 4.** Each note states the verification status of every result (independently verified,
   partially verified, exploratory, known-invalid) and a remediation row per gap: current evidence,
   missing verification, accountable Issue, resolving evidence or decision. A remediation plan
   authorizes no work.
5. **Item 7.** Both records use [R] premises (Step 2 results, OA-1/OA-2/OA-3, OBS, NPS1, NIS2) as named
   conditions, not as verified premises; the notes carry them as such. No refuted statement is used
   (§3.2).
6. **Item 6.** After landing, the scoped results become surviving claims for item 6 and §A.42 item 5,
   and they add incoming citations to OA-1, OA-2, OA-3 and the Step 1–2 records that any later
   removal audit must check.
7. **§A.42.** Item 2: every reviewed commit lands as an ancestor (merge commit). Item 3: §5.5. Item 5:
   necessity is the owner's preservation decision and item 8's surviving-claim rule. Item 8: §6.
8. **§A.28.** The package adds two status notes and no other new file; this plan directory does not
   land (OQ-10).
9. **§A.45.** Integration needs its own recorded owner authorization; G3's planning updates record
   existing decisions only.

***

## 9. What this plan does not do

It commits, pushes and posts nothing; edits no input record, manuscript or frozen record; runs no
computation on any OI rule; authorizes no Step 3B, candidate search or `G_SM` computation; and changes
no review verdict, classification or gap of either record. TUNE-1 stays scientifically paused.
