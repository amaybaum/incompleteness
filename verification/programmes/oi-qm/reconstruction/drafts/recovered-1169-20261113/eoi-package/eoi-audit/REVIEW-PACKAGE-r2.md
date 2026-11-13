# REVIEW-PACKAGE-r2: re-review of PACKAGE.md r2 against REVIEW-PACKAGE.md

- **Reviewed:** `PACKAGE.md` r2, sha256 `ef0612025c8ef044a4a6550538c956b4f4eed329627e34f194fecb2fabdeeec0` (407 lines). `P:n` = a line of r2.
- **Against:** `REVIEW-PACKAGE.md` (`e6ff5611…170761f`), `PACKAGE-r1.md` (`c8960f5c…a1ec91bd`, re-hashed), `PACKAGE-r2-DISPOSITIONS.md` (`d9149854…f94834`).
- **Method:**
  - full `diff PACKAGE-r1.md PACKAGE.md`; every table row that changed was compared;
  - guard lines re-read in `verification/lean/edge_rigidity_probe.py` at `5ce4f98e`;
  - #1188 and #1169 c.6723491138, c.6723585151 and c.6723571280 read via REST.
- **Read-only.** Model-written review; not human verification.

## Verdict: **ACCEPT**

- B1–B3 are closed, and no new hole was found.
- N1–N19 are applied faithfully; N20 needed no change.
- §8 is complete and non-redundant, apart from one small overlap (R2-N4).
- The two new #1169 comments close almost every "relayed chat" citation. The substitutions are listed in R2-N1. They are non-blocking for acceptance, but they should be made before the package is posted or cited by the M-ARC preregistration. One quotation must change its words as well as its citation, because r2 quotes the coordinator's paraphrase as if it were the owner's words.

***

## 1. Blocking findings of REVIEW-PACKAGE

**B1, closed.**
- **#1188 quotes are accurate.** P:244-245 matches the #1188 body. The ellipsis drops only "(`SubstratumInterfaceAudit.lean`): the access-model theory has no composite unitary control on every nonempty finite carrier." The step-3 quote at P:249 is verbatim.
- **"Citable" is supported.** "Citable per #1188" at P:221 is supported by the #1188 text: `substratumGen_not_control` is "a concrete theory with no hypothesis to fail, and it is citable in the manuscripts".
- **#1188 metadata (P:239) is correct:** amaybaum, 2026-11-07T21:44:12Z, 0 comments, open.
- **Guard ranges verified at `5ce4f98e`:**
  - `ok_sub = True` is at :3623.
  - The manuscript loop is at :3722-3726, over GR, Main, Substratum, SM and FULL, barring `SubstratumInterfaceAudit`, `permTheory`, `SourcedOI` and `obsTheory`.
  - The registry checks are at :3727-3729 (`kernel-only`, `manuscript == []`), and `check('R7-SUB', …)` is at :3751.
  - `ok_srcp = True` is at :4883.
  - The file list is at :4943-4945 (GR, Main, Substratum, SM, ch01, ch19, FULL, and the GR, Main and FULL `.tex`), and the token list starts at :4947. It includes `obsTheory` and `permTheory`, among others.
  - `check('R7-SRCP', …)` is at :4970.
  - The range ":4943-4947" (P:247) spans the file list, the read line and the start of the token list, which is accurate.
- **Placement in the package:**
  - The two-state item has moved into §3.5 (P:200-201) and is no longer listed as consistent.
  - K-4's anchor separates the citable theorem from the kernel-only one.
  - #1188's "frozen" wording appears both in the §4 preamble (P:212-213) and in §8 item 2 (P:346-347).

**B2, closed.**
- Main:684 is in K-1 (P:218).
- K-18 (P:235) states C5's reading-independent finding (C5:212-214). Its anchors and related sites match C5:204-205, 218-219 and 234-235. GR:20 is from C5:235.
- K-7 carries appendix-b:193 = FULL:5945, labelled "located" (P:224).

**B3, closed.**
- §1's standing note (P:21-43) quotes c.6723277401 and c.6723329527 with author and time; the quotes are verbatim.
- It also adds c.6723491138 (amaybaum, 15:40:41Z). Its five questions and its three-row table are verbatim.
- P:29's "every ARP investigation carries an assumption-dependence analysis" summarizes the comment's own implementation paragraph, which is the coordinator's text in that comment. It is not presented as owner words, which is acceptable.
- §6's heading keeps the r1 ranking text and states that the owner's order governs. Each item carries its ARP tag.
- Q-C2-1's precondition cites C2:757-758.
- The non-ARP items (Theorem W positivity, F-1) are marked as open.

## 2. Non-blocking findings N1–N19 of REVIEW-PACKAGE

All are applied, as checked against the diff and the sources:

| Finding | Where in r2 | Check |
|---|---|---|
| N1 | P:314 | Matches C2:746 and REVIEW-C2-r4 |
| N2 | P:284-291, P:65 | Labels correct; RP:51 cited correctly |
| N3 | P:80-82 | — |
| N4 | P:77-78 | — |
| N5 | P:95, P:162 | — |
| N6 | P:328-332 | Matches GATE:143-148 |
| N7 | P:220 | — |
| N8 | P:149, P:214, P:361 | — |
| N9 | P:232 | — |
| N10 | P:229 | — |
| N11 | P:213 | — |
| N12 | P:194-197; §9 at P:380-382 | Stated neutrally |
| N13 | P:198-199 | — |
| N14 | P:57-66 | Lists re-derived from the inventories; MQ-41's quote matches INV-MANUSCRIPT:60. r2 correctly omits INV-RECON 17 (PC-1, an L row), which my list had wrongly included |
| N15 | P:224, P:232 | — |
| N16 | §8 | Main:684 now appears only in item 5 |
| N17 | (a)–(f) | All present |
| N18 | P:270-272, P:280 | Matches C3:169-170 and 175-176; REVIEW-C3-r3:56-64 holds n1–n3 |
| N19 | §10 | — |

## 3. "Relayed chat, to be recorded": does citing the new comments close it?

**Yes, for every owner quotation the package makes except one.** Two parts are not closed:
- The owner's priority guide at BRIEF.md:43 (P:62) is not recorded on #1169. It is used only as a coverage label, so it can stay "relayed" as provenance.
- The outcome definitions at BRIEF-P2.md:12-19 (P:70) are the coordinator's brief. c.6723585151 records only the three labels, with elisions. That citation can stay as it is.

**R2-N1. Substitutions (non-blocking for acceptance; make them before posting or citing):**

1. **P:17-18.** Replace "(owner chat, relayed, BRIEF-P2.md:51)" with "(#1169 c.6723585151, amaybaum, 2026-11-08T15:49:15Z)". The quoted sentence is verbatim there.
2. **P:19, R-I1.** The quotation "Corrections change scope or interpretation, never silently discard a valid proof" is the coordinator's paraphrase in BRIEF-P2.md:45, not the owner's words.
   - Replace it with the verbatim text from c.6723585151: "Preserve all original mathematical findings. Audit corrections should modify their scope or interpretation, not silently discard valid proofs."
   - Cite "(#1169 c.6723585151)".
3. **P:37-42.**
   - Replace the header "*Owner chat, 2026-11-08, later (relayed by the coordinating session; not yet recorded on #1169):*" with "*#1169 c.6723571280* (amaybaum, 2026-11-08T15:47:58Z):". The two quoted sentences and the synthesis question are verbatim there.
   - Replace "Significance tiers, as relayed: (1) … (3) …" with the recorded table, verbatim: "An imported assumption causes an apparent obstruction | We identify an unnecessarily restrictive test"; "Removing that assumption yields a valid OI mechanism | We overcome a genuine obstruction in the tested model"; "The mechanism reproduces the required quantum predictions, measurements and composition | We advance toward operational equivalence". Add the owner's gloss: "The third is what ultimately matters. We cannot establish equivalence merely by escaping a no-go theorem."
   - Recommended: also quote the two safeguards, because they bear directly on §6 items 5 and 3:
     - "Q-C2-1: Establish reachable hidden laws before designing the executable test. A non-Clifford result must emerge from the dynamics, not be embedded in the definitions." This is the owner's form of the P:309-310 precondition.
     - "Q-C2-2: Require instance-specific witnesses. Distinguish genuine operational accessibility from an inability to certify it within a particular mathematical framework." This matches C2:785-786.
   - Recommended: also quote the witness principle, which bears on every outcome-3 and no-go reading: "failure to construct a witness is not proof that no witness exists, unless a theorem establishes that impossibility within a clearly stated scope."
4. **P:263.** Replace "later chat, relayed" with "c.6723571280".
5. **P:342.** Replace "(BRIEF-P2.md:51, relayed)" with "(c.6723585151)".
6. **P:363-364, §8 item 10.** The recording precondition is met for the EOI directions (c.6723585151) and the later chat (c.6723571280). Narrow the item to the remaining relayed item, BRIEF.md:43's priority guide, or drop the precondition and keep the posting question.
7. **§10, P:405 and P:407.**
   - Add c.6723585151 and c.6723571280 to the owner-records row. They are owner records of direction, and no scientific claim rests on them.
   - Reduce the "Owner chat relayed" row to BRIEF.md:43, which remains provenance as relayed.
   - Delete "no #1169 comment through 15:40Z records them".
8. **Gate pointer (§8 item 9, optional).** c.6723585151 also records verbatim the owner quotes the gate relies on (GATE:24-32 and 94-95, including R-I4 and "A proof that excludes such memory …"). GATE:24-25 and 238's recording precondition is therefore met.
   - c.6723585151 also records the coordinator's reply placing Act 45's separation at the exact-arithmetic probe layer. Headline 6 (P:89-92) is consistent with it.
   - The owner's R-I2 wording ("direct evidence that one-step agreement is insufficient for the broader equivalence claim") is satisfied at that layer.

## 4. Other non-blocking items (new in r2)

- **R2-N2. Coverage wording (P:60-61).** "the collections INV-RECON 7 and 8 beyond `two-mode-drive.md` (C1:193, 296) and 8.a (C2 §15)" can be read as listing 8.a as unclassified. C2 §15 classifies 8.a. *Fix:* "the collections INV-RECON 7 and 8, apart from `two-mode-drive.md` (C1:193, 296) and 8.a (C2 §15)".
- **R2-N3. §5 states the ARP-to-outcome-3 mapping as tracked; §8 item 6 asks the owner to decide it.** P:251 says "ARP-1 M-ARC addresses … M2D:853-854; ARP-3 Q-C2-2 addresses M2D:728-733", while P:356-357 asks whether to record it. The mapping is the consolidator's inference; it is consistent with C3:165 and C2:771. *Fix:* "would address (subject to §8 item 6)".
- **R2-N4. Small overlap in §8.** Item 7 covers "the items listed in §1", and that list includes the Theorem W pointer (P:65), which item 6 also covers. *Fix:* exclude it from item 7's scope, or say "(Theorem W: item 6)".

## 5. §8 completeness

Items 1–10 cover every decision the audits, the gate and this review raise:
- acceptance as the reconciled findings, and as the M-ARC freeze input;
- K-1–K-18, with the #1188 constraint, source-audit's route, the two-state sites, FULL:522 and K-18;
- ROADMAP;
- the C5 readings;
- the §3.5 differences;
- the follow-ups, under the ARP;
- coverage and the C4 scope;
- the §A.42 gaps;
- the gate;
- posting.

No decision is duplicated, apart from R2-N4. Each item names its object and the choice the owner must make.
