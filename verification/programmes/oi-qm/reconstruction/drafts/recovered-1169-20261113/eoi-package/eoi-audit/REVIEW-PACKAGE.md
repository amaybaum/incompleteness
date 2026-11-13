# REVIEW-PACKAGE: independent adversarial review of the EOI decision package

- **Reviewed:** `PACKAGE.md`, sha256 `c8960f5ca8f060859d7873bea61af37cc98cc525fdc4bacdfa3b04e4a1ec91bd` (re-hashed before review; 321 lines). `P:n` = line `n` of that file.
- **Inputs re-hashed and matching the package's table:** AUDIT-C1 `8aaa7518…`, AUDIT-C2 `54699d91…`, AUDIT-C3 `d143754b…`, AUDIT-C5 `65f844f0…`, `../gate/GATE-DRAFT.md` `a5d42f92…`. `C1:n` etc. as in the package.
- **Snapshot:** read at `5ce4f98e`; `origin/main` = `2cd49dc0`. Read-only: no repo edit, push, GitHub write or computation. GitHub REST reads only (#1188, #1169 comments, #1193, #1203–#1206).
- **Model-written review.** Not human verification.

## Verdict: **ACCEPT WITH CHANGES**

The package is a faithful consolidation in the large: every per-cluster table row I checked carries the outcome, class and evidence layer its accepted audit gives, the headlines do not upgrade any result, no replacement wording is drafted, and the frozen-status statements check out. Three blocking items remain. Each is a short addition, not a restructuring: an existing owner decision that constrains K-4 and contradicts a "minor" label (B1); three omissions from the §4 corrections list (B2); and a standing note that the owner's sequential programme now governs §6/§8 and that the package is an input to M-ARC's freeze (B3).

***

## 1. Blocking findings

**B1. A recorded owner decision and an active guard constrain K-4 and the "two-state" item; the package omits both.** P:51-53, P:168-169, P:184, P:201-205, P:284.
- **Source.** #1188 (open; read via REST) records: "Guards R7-SUB and R7-SRCP keep these [`permTheory_not_control` / `obs_not_control`] kernel-only. Owner decision: keep those guards, and do not broaden the two-state result into a universal claim without further proof." Guard `R7-SUB` (`verification/lean/edge_rigidity_probe.py`, the block ending at `check('R7-SUB', …)`, ~:3700-3751 at `5ce4f98e`) fails if `papers/GR.md`, `papers/Main.md`, `papers/Substratum.md`, `papers/SM.md` or FULL contains `permTheory`, `obsTheory`, `SourcedOI` or `SubstratumInterfaceAudit`, and requires the family registered `kernel-only` with `manuscript == []`.
- **Effect on the package.**
  - K-4's anchor names `permTheory_not_control` (P:184), and headline 4 says the content "survives at kernel level on … `permTheory_not_control` (every carrier)" (P:52). The science is right (C2:191-196), but the owner is not told that a manuscript correction cannot cite that theorem without changing a guard the owner decided to keep.
  - P:168-169 lists "missing 'two-state' qualifier at Main:216, 354, 776 is minor (C2:198-203; C5:272-277)" as a *consistent overlap*. C2 rests "minor" on an "unstated kernel corollary … (auditor, paper)". #1188's owner decision requires "further proof" before the two-state result is broadened. That is a disagreement between C2 and a recorded owner decision, not a consistent overlap.
  - #1188's own proposed round shape (step 3) already includes "Repoint the manuscript citations (GR:260, Main:590)", which partly answers P:284 (item 3).
  - #1188 calls "several of the records above" frozen, "which only a native round can correct"; the package (P:175-176, P:286) follows C2 that `source-audit.md` is not legacy-listed and only self-declared frozen. I confirmed it is absent from `legacy-records.json` and has a post-freeze entry (:191, :211). The difference bears on P:286 and should be stated.
- **Fix.** In §5's #1188 bullet, quote the owner decision with its source; in K-4's anchor cell, add "(kernel-only under R7-SUB; owner decision in #1188)"; move the two-state bullet out of "consistent overlaps" into §3.5 as C2 vs the #1188 owner decision; in §8 item 3, note #1188's step 3 and the guard; in §8 item 5, note #1188's "frozen" wording against the legacy-records check.

**B2. The §4 corrections list misses three items that the accepted audits support, so §8 item 2 (P:283) would not reach them.**
1. **Main:684 dropped from K-1.** C1 lists Main:684 among the MQ-02 over-reading texts (C1:174-178; C1 summary item 7, C1:651), and the package's own C1 table carries it (P:84). K-1's sites (P:181) list Main:68, 206, 682, 776 only. It appears elsewhere only as an owner-judgement or §3.5 item (P:159, P:287, P:289). *Fix:* add Main:684 to K-1 (or a separate K row), marked "C1 over-read; C5 owner judgement, §3.5".
2. **C5-5's unsupported parenthetical has no K row.** C5's finding 1, "262's parenthetical has no support in the corpus" (C5:212-214), holds on either reading; only the contradiction call is reading-dependent (C5:224-232). The package carries it in the C5 table (P:149) and asks only which reading governs (P:287). Under the Code Review Rules an unsupported claim may not stay presented as established, so it is a correction candidate in its own right. C5 also names Main:718, GR:589 (with FULL:5852, 6176) as downstream genericity statements (C5:218-219, 234-235). *Fix:* add a K row for Main:262 (no mirrors, C5:234), with the related sites listed as related.
3. **GR:134 has an unlisted book mirror.** K-7 (P:187) lists GR:134 for TB-BA's "determines" over-read (C1:555-559) with no book site. `book/appendix-b-derivations.md:193` = FULL:5945 (byte-identical pair, checked) reads "Since `T_ij(t)` determines the emergent quantum description, and …". *Fix:* add "appendix-b:193 = FULL:5945 (located, not audited)" to K-7.

The book-mirror pairs the package gives are otherwise exact: I checked 35 `chNN:n = FULL:m` pairs at `5ce4f98e` (preface, ch00, ch01, ch02, ch07, ch09, ch14, ch18, ch19, appendix-b, appendix-c), and all are byte-identical. The "located, not audited" FULL:522 = ch01:187 claim in K-6 (P:186) is accurate: the paragraph states the carried-ancilla separation with no evidence layer ("can separate") and ends "none of it makes embedded observation and quantum mechanics inequivalent". One range is mislabelled; see N9.

**B3. The package's standing and §6/§8 predate the owner's ARP authorization, and that authorization makes the package a freeze input.** P:14-16, P:216, P:292-293.
- #1169 c.6723277401 (amaybaum, 2026-11-08T15:21Z) authorizes, as one sequential programme, M-ARC → Q-C2-1 → Q-C2-2 → drive-phase check. It states that "the C2 re-review and consolidated classification-audit findings must be incorporated before M-ARC's freeze". c.6723329527 (15:25Z) keeps owner designation of each F and E.
- Consequences the package should state, without rewriting §6:
  - P:14-16 "No correction, follow-up or investigation is authorized" is no longer true for those four follow-ups. Manuscript corrections remain unauthorized.
  - §6's ranking (P:216) differs from the owner's order. Q-C2-1 is ranked 5 with "*Check:* none named" (P:256), yet it is now authorized second. Its preregistration must first supply what C2 says is missing, a characterization of the reachable law set `L` (C2:757-758). The package should flag this as a precondition, not a rank.
  - Item 2 (Theorem W positivity) and item 6 (F-1) are not in the ARP. They remain open owner decisions, and item 2 is also an unassigned hand-off (N2).
  - §8 item 9 (P:292-293) is answered for four items. What remains open is items 2 and 6, and the question of whether this package, once accepted, is the version incorporated before M-ARC's freeze.
- **Fix.** Add a short standing paragraph to §1 citing both comments with author and time; annotate §6's heading and §8 item 9 to match. Do not change the ranking text.

***

## 2. Non-blocking findings

**Fidelity (strength, outcome, class, layer)**

- **N1. Q-C2-1, "Closed already" is stronger than the audit's word.** P:256-257 says "Closed already: … the dyadic unconditioned sub-case (reviewer, paper; integer control for m ≤ 5 only)". The audit calls it a "**Closable sub-case**" (C2:746). *Fix:* use "closable sub-case (reviewer, paper; descent for every m, integer control for m ≤ 5 only)". REVIEW-C2-r4 §1 item 3 supports the parenthetical.
- **N2. §6 item 2 (Theorem W positivity) is an unclassified hand-off, ranked by assertion.** P:231-236.
  - C3 routes it as "a MECH-1-cluster check" (C3:410-411, 568-570). MECH-1 sits in C2 (C2 §14), which does not take it up. So no accepted audit classifies it.
  - "*Rank:* plausibly one exact check" is the consolidator's estimate; no audit gives it. The "*Would show*" sentence (P:234-235) is also the consolidator's.
  - The provenance-only r2 control already reports a non-positive full-support law at `q = 3` (C3:413-414). If that holds, the open item is landing and controlling that witness, not a new search, and the rank should say so.
  - *Fix:* label item 2 "C3 pointer, not taken up by C2", mark the rank and the would-show as consolidator reasoning, and add the item to the coverage note (P:32-35) and to §8.
- **N3. Headline 3's MQ-13 clause conflates C1's two points.** P:49-50: "`hc` and a swaps-and-phases step are missing from the GR:262 box". C1 has (a) a swaps-and-phases step that is *unformalized* (the kernel assumes full `DrivesElementary` in `hd`), and (b) `hc` missing from the GR:262 box, GR:264 and Main:590 (C1:353-355). *Fix:* "(a) an unformalized swaps-and-phases step; (b) `hc` missing from the GR:262 box, GR:264 and Main:590".
- **N4. Headline 2's class is ambiguous.** P:46 "Class imported" follows the sentence about `oi_alone_not_qm`. C1's class "imported" belongs to MQ-02's emergence claim (C1:169), while C2 classes the theorem itself n.a. (MQ-16, C2:302; P:108). *Fix:* "MQ-02 class imported; the theorem itself n.a. (MQ-16)".
- **N5. Headline 7 and the Lemma Q(iii) row omit C3's counter-reading.** C3 grades Lemma Q(iii) 2, and also states that on apparatus-1's P2 (AP1:297-299) the outcome would be 1 (C3:262-264). *Fix:* add "(1 on AP1's P2 reading, C3:262-264)" at P:62 and P:129.
- **N6. §7 drops the gate's G0 labels.** P:271-272 reports EOI-NEG for P-CONTROL, P-OBS, M-INACC-1 and MECH-2 without the labels the gate attaches: *within its class* for P-CONTROL and P-OBS, *idealization-dependent* for M-INACC-1, and *restricted by H-LIFT* plus the undecided M2D:728 item for MECH-2 (GATE:143-148). *Fix:* carry the labels.
- **N7. K-3 omits C1's mild MQ-12 over-reads.** C1:323-324 lists GR:232-236 and GR:252 (mild). K-3's sites (P:183) do not include them. *Fix:* add them, marked mild.
- **N8. L3B provenance item drops "3A".** C2's PV-1 reads "L3B's R_LL and 3A inputs are off-repository" (C2:844); P:295-296 names only R_LL. Also, L3B is a native round with receipt `verification/receipts/L3B.json`, so its record is immutable under G13. Any closure is a new round, or a mutable record citing it (§A.42 item 6). *Fix:* add "3A" and the route.
- **N9. Range mislabel.** K-15 (P:195) writes "ch18:64 = FULL:4868-4876". FULL:4868-4876 corresponds to ch18:64-72 (checked line by line). *Fix:* "ch18:64-72 = FULL:4868-4876".
- **N10. K-12 omits C5-2's adjacent site.** C5 names "Adjacent softer form: FULL:3714 / ch14:50 'unitary evolution under the reduced Hamiltonian'" (C5:84-86; also C5:57-58). *Fix:* list it as related under K-12, or note that it is in K-11's paragraph.
- **N11. Frozen-status sentence is broader than checked.** P:176-177: "The reconstruction records … are not in `legacy-records.json`, and no receipt names them". `reconstruction/round-bg-1-integer-classification` is legacy-listed. Many `reconstruction/round-*` directories are receipt-governed (BG-2, BG-3, CMP-1, COMP-1, DIM-1, EFF-1, IIP-1, K1-*, KINF-*, KT4-PREM-1, KTOKEN-MAXCONE-1, KTRANS-*). The statement is true of the records the package cites (M1D, M2D, QA, AP1, FB, MI-*, states-dynamics, oi-qm-ext-1), of PROG and of `oi-qm/amendments/amendment-1.md`, all of which I checked. *Fix:* "the cited reconstruction records".

**§3.5 disagreements**

- **N12. The H-LIFT entry omits the record's own identification and the gate's label.** P:162-163, P:313-314.
  - M2D:319-321 defines H-LIFT and adds "This is FB's common-lift condition H-C, stated for the identification". The ledger at M2D:776 classes it "Modelling condition (FB H-C)". The record therefore identifies H-LIFT with H-C, as C3's AW-C3-5 groups them. C2's separation, "H-LIFT supplied by enlargement; H-C a genuine exclusion" (C2:565-572, 831-835), is a reading against that sentence, and C2:567 quotes M2D:319-321 without it.
  - The gate labels MECH-2 "restricted by H-LIFT" (GATE:148) while also saying "H-LIFT is not a memoryless-environment assumption" (GATE:167).
  - The disagreement is real and three-way. §9's merged "Common lift" marker (P:313-314) puts C2's reading first. *Fix:* cite M2D:319-321 and M2D:776 in §3.5, add the gate's label, and state §9's marker neutrally.
- **N13. A possible further difference.** C3 routes M2D:728-729 to MECH-2 "scoped at M2D:109-113" (C3:221-222). C2 gives the same lines outcome 3 because the sentence lacks those qualifiers (C2:586-593), and the gate agrees it is undecided (GATE:148). P:168 lists this as a consistent overlap. It is probably a difference of emphasis, not of verdict, but "consistent" should say "C3 routes; C2 decides".
- **Checked and real:** FULL:690 (C1:180 vs C5:105-110), Main:684 (C1:178 vs C5:337-340), common realization (C1:100, 406, 653 vs C5:367-369; Main:598 is a continuum ε-net theorem, which supports C5's reading over C1's "only per finite menu"), Intro:129 and Main:674 (different sentences or clauses, as stated).

**Coverage**

- **N14. The coverage note lists only the H gaps, and "no C4 cluster input" is unexplained.** P:32-35.
  - MQ-22 (INV-MANUSCRIPT:41), MQ-30 (:49), MQ-09 (:28; C1:178 and C5:337-340 only) and INV-RECON 7.a-7.c (:33-35) are correctly identified as unclassified H items. No audit names `whole-model-bridge`, `measurement-exchange` or `two-system-interface`; C3:158-160 mentions E-AR only as AP1's motivation.
  - Unclassified at M priority, which the owner assigned to measurement and Born-rule results (BRIEF.md): MQ-04, -05, -06, -08, -10, -19, -26, -38, -39, -41 (MQ-41: "QM used as a premise of the foundation"), and INV-RECON 7.d, 7.e, 8.b, 9, 11-13, 15-22, 29, 36, 37, 39, 44, 45, 49, 51, 53, 54. INV-RECON 10, 14, 23, 24 and 52 are covered by C3 and C5.
  - Also unclassified: the Theorem W positivity hand-off (N2), and a candidate paraphrase of Sub:389's "derived rather than fundamental" at FULL:832 = ch02:198 ("They produce derived rather than fundamental structures"), which carries a representation qualifier later in the paragraph. That one is the owner's call.
  - *Fix:* state what C4 was scoped to, or that M-priority items were out of scope, and list the unclassified M items. §8 item 10 then covers them.
- **N15. Sub:137's interference clause.** C1 flags Sub:137, "record persistence is required for the non-Markovian returns that produce quantum interference" (C1:416), under K-7. It belongs to the C5-7 memory→interference family (AW-C5-d) but is absent from K-15's sweep list. *Fix:* cross-reference it in K-15.

**§8, owner decisions**

- **N16. Redundant entries.**
  - Main:684 appears in both item 6 and item 7.
  - Item 8 (K-6, FULL:522) and item 5 (source-audit, K-4's frozen site) are sub-cases of item 2.
  - *Fix:* merge them, or say "within item 2".
- **N17. Missing entries.**
  - (a) The #1188 constraint (B1).
  - (b) C5-5's unsupported parenthetical as a correction, not only as a reading (B2).
  - (c) The C4 scope and the unclassified M items (N14).
  - (d) The Theorem W hand-off (N2).
  - (e) Under §A.46 item 4, each outcome-3 claim on `main` (M2D:728-733, M2D:853-854) needs an accountable Issue. The ARP items on #1169 now serve for those M-ARC and Q-C2-2 address, which should be stated.
  - (f) Whether the package is posted to #1169, and with which provenance table (N19).

**§6 follow-ups (otherwise faithful)**

- **N18.** M-ARC matches C3:165-215, with REVIEW-C3-r3's optional n1-n3 applied and the deviation disclosed (P:25, P:218-230). Owner c.6723277401 preserves "the specified exact F₂ span-membership test on 7- and 9-cell rings, its four outcome labels … and the requirement for green controls at both sizes", which matches.
  - Because the package now feeds M-ARC's freeze, two points need care:
    - The n1-n3 text exists only in the package, not in the accepted audit. The preregistration should cite REVIEW-C3-r3 for it.
    - The package omits the initial state (every `V` site a P2 ready cell with known 0, or 1 through H-PREP; every `H` site a source cell) and variant I's definition (C3:168-176). It cites C3:165-215, which suffices only if the preregistration reads the audit.
  - Q-C2-2 (P:237-245) and the drive-phase check (P:246-252) are stated as C2:771-788 and C1:659-665 fix them, with the gaps flagged ("no further controls stated"; "No rule is preregistered"). Item 5 has no "*Rank:*" line (P:253-259).

**Provenance (§A.42 item 8)**

- **N19. The package has no reference table; the gate's has one (GATE:225-238).** If the package is posted, classify:
  - **Support off `main`:** AUDIT-C1/C2/C3/C5, every REVIEW-*.md and GATE-DRAFT.md (scratchpad; they support every finding in the package); `REVIEW-C3-r3:32` (P:230); the reviewer's `rv4/agl.py` control behind Q-C2-1 (via C2:763); the `q = 3` control (P:234, already marked provenance); the gate's PCD/PMD/POD pins `cc453774…`, `7d707bb5…`, `83eca7cd…` (present locally, not ancestors of `origin/main`, checked); S1B r5 (scratchpad); composition-access P1 (C5's gap); L3B's R_LL and 3A inputs.
  - **Support on `main`:** MC1 at `41a42cb9`, now an ancestor of `origin/main` (checked). The gate's §7 gap (GATE:232) is therefore closed at the pinned commit itself, and DESIGN.md differs from the pin only at line 758, a row the gate does not cite (checked; P:29-31 is correct). Also the #1188 vacuity record at QA DESIGN.md:864-866, MI-D:585, 619, MI-R:613 and FB RESULT.md:187 (checked).
  - **Provenance or responsibility:** #1188, #1193, #1203-#1206 as identifiers. Assigning a gap to #1188 is responsibility, not retention (§A.42 item 8).
  - **Owner direction:** the quotes at P:15-17 (BRIEF-P2.md:45, 51) are a chat relay. I found no #1169 comment through 15:25Z that records R-I1-R-I4 or "No manuscript corrections …". The gate already requires quoting from a #1169 record with author and time before posting (GATE:24-25, 238). The package should adopt the same condition.
- **N20.** #1169 c.6714136234 is titled "MECH-1: owner review guidance" (amaybaum, 2026-11-07T22:55Z); MI-D:25 calls it "the earlier owner addendum". The package's "owner addendum" (P:206) follows MI-D and is acceptable. It is support on `main` via MID:25-29, as GATE:236 says.

***

## 3. Spot-checks performed (all confirmed unless listed above)

**Against the audits (every package table row):**
- C1 table: 18 of 18 rows (MQ-01, -02, -03, -11, -12, -13, -27, -28, -29, -32, -42, PROG, TI-B, TI-C, TB-BA, TB-01, TB-06, M2/M3).
- C2 table: 16 of 16 rows.
- C3 table: 13 of 13 rows.
- C5 table: 9 of 9 rows.
- All 11 headline bullets. Defects: N3, N4, N5 only.

**Against the repository at `5ce4f98e`:**
- *Lean:* `oi_alone_not_qm` GeneralCarrier.lean:160-163; `realizesSealedOICore_of_control` OIRealization.lean:252-258; `finite_horizon_equivalence` Equivalence.lean:462-468; `control_of_phaseFree` MinimalRepertoire.lean:529, 559; `substratum_plus_control_qm` StructuralClosure.lean:414-417 (anonymous `ExtendsSubstratum` binder); `diagGen_not_control` LieRankSource.lean:146 (`Fin 2`); ReachabilitySeam.lean:71-72 ("NOT claimed … `HControl` is necessary"); `padData_rooted` OperationalSourcing.lean:476.
- *Papers:* GR:222 box; GR:288 OI_Q scope; GR:450; Main:582 ("enters as the instrument data"); Main:598; Main:646 tags "(exact computation)" and "(kernel: `padData_rooted`)"; Main:674; Intro:129; Comp:100.
- *Records:* AP1:338-343, 547; QA:499-501, 649-650, 799; M2D:319-321, 346-347, 728-733, 776, 853-854; MI-A1:59-70; M1D:120, 473-474, 763-766, 931; CURRENT-HANDOFF.md:77-80; two-mode-drive.md:54, 145-147; PROG:40; ROADMAP:1-6, 48-52 (frozen header); source-audit.md:191, 199-200, 211.
- *Status files:* `legacy-records.json` (arc-b result.md listed; ROADMAP, PROG, `oi-qm/amendments/amendment-1.md`, source-audit, act-45 and the cited reconstruction records not listed); receipts A45 and L3B present.
- *Snapshot drift:* `git diff 5ce4f98e origin/main` touches only MC1 DESIGN.md.
- *Book mirrors:* 35 `chNN = FULL` pairs; corpus grep of 28 over-read phrases, which found the B2.3 mirror and the N14 candidate.

**Reviews:** final verdicts of REVIEW-C1-r2, C2-r4, C3-r3, C5-r2 and REVIEW-GATE-r3 as the package states. The AUDIT-C2 r4→final and AUDIT-C5 r2→final diffs are exactly the stated fixes. GATE L69 and L76-79 equal R3-B1 and R3-B2 verbatim.

## 4. What does not need changing

- No replacement wording is drafted anywhere in §4 or §6.
- ROADMAP's frozen status (§A.36) and the mutable-record route (§A.42 item 6) are correct.
- Act 45 is stated at both layers per R-I2, with the kernel anchor.
- The #1188 credit for `ReadWriteSourced` vacuity and its main-record sites is correct. B1 adds what #1188 also records.
- The disagreements in §3.5 are presented, not resolved, as they should be.
