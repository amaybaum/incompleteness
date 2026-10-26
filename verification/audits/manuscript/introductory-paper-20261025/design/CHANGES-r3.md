# Changes in revision 3 of the paper design

**Inputs and files**
- **Applies:**
  - `paper/review/RECHECK-r2.md` (BLOCK, wording only): RC-1 by option (b), RC-2, RC-3, n1 and n2;
  - the owner's decision of 2026-10-26, as relayed by the coordinator: the paper replaces the
    Explainer.
- **Kept unchanged:** revision 2 (sha256 prefixes: `OUTLINE-r2.md` `3e86f8f05bc5d229`,
  `CONTRIBUTION-r2.md` `ac5f8282d0dcf9db`, `SOURCES-r2.md` `8efec275489d3f8f`, `CHANGES-r2.md`
  `33e6c18ab0321188`) and revision 1.
- **New:** `OUTLINE-r3.md`, `CONTRIBUTION-r3.md`, `SOURCES-r3.md`, this file, and the scratch check
  `probe/cards.py`.
- **Repository:** no file changed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.

**Verified at `687e885b` before applying:**
- ch07:126 sentence 1 is byte-identical to FULL:2003.
- GR:869 still reads "invokes only Popescu-Short-Winter [29] … with no replica trick, no
  ergodicity assumption".
- ch18:148 and FULL:4968 both read "Its Page time is a mass-independent fraction of the
  evaporation time".
- BH02 `MANUSCRIPT-AUDIT.md:70–73` reads "contradicts (definite configuration, aligned split)",
  and :256–259 reads "contradicts Theorem A.8 as stated".
- :78 reads "supports, understated", and :108 is the "conditions" item for ch07.

## Re-check items

| Item | Change |
|---|---|
| RC-1, option (b) | The variant is renamed "BH-01-conflict-free". ch07:126 sentence 1 / FULL:2003 and GR:869 are added, with BH02 MANUSCRIPT-AUDIT:70–73 and :256–259 cited: to R11; to decision 1(a)'s "correct first" list, for every scope that carries §7-h (recommended, Alt-L, Alt-X and the variant); and to the §7 paragraph and the variant row of OUTLINE-r3. Decision 1(a) also states **option (ii)**, which drops §7-h as well and so the H-scramble finding, as the owner's alternative. The variant row says plainly that it is not free of corpus conflict |
| RC-2 | The variant row and decision 1(a) state what the contribution paragraph's black-hole sentence and §10 carry: §7-b, §7-h and §7-i under the variant; §7-b and §7-i under option (ii). CONTRIBUTION-r3 gives the replacement sentence for each case, and §10 says the same |
| RC-3 | Decision 2, CONTRIBUTION-r3's Lean paragraph (formerly r2:58–60), R6 and UNTRACED-4 now say that any statement that the cited declarations are checked in Lean at a commit is an enduring certification claim under §A.42. An expected result is retained beside the paper in every case, or the commit is shown to lie in a covered archive. The owner chooses only the word |
| n1 | R12 adds ch18:148 / FULL:4968, "a mass-independent fraction", which omits the constant-coefficient condition. This is the "conditions" category, BH02 MANUSCRIPT-AUDIT:108 |
| n2 | The §7 paragraph of OUTLINE-r3 (formerly r2:195) now lists the §7-h conflicts. It also records that §7-g (ch07:126 s3, "supports, understated", MANUSCRIPT-AUDIT:78) and §7-i (ch07:137–143, GR:855–865) agree with the live text |

## Owner decision 7 (replace the Explainer), applied

- **OUTLINE-r3: new section "Replacement objective".**
  - It assesses the outline against the replacement role. The outline fits the role. The deliberate
    gap is the wider-programme overview (ħ, cosmology, the SM sector), which is left to Main and the
    Book.
  - It maps the sections onto the owner's six parts, with an "absorb from the Explainer
    (candidates only)" column driven by paper/explainer/REVIEW.md §2.
    - The candidates are: the summary-table form, rebuilt as Appendix A from Main:710–722; a
      technical-register version of the quantum-weirdness walkthrough; and an FAQ-style "what it
      does not say" list.
    - The D-gauge double-difference display is marked **not** a candidate: it is Main §3.1 content
      (Main:232–238), and phase-locking is out of scope.
    - The lineage survey and the decompression section are marked not candidates.
  - It maps each of REVIEW.md §3's eleven stale items to how the outline avoids it.
  - Sections that do not fit one part: §9 (cross-cutting, after part 6), §10 and the references.
    §6 is split between parts 3 and 6.
- **Card table (ch01 §1.11) added as §5-h, in corrected form.**
  - The game is the swap map $\varphi(x,h)=(h,x)$ (Main:286, :702). The odds are 1/2, 1 and 1/2,
    so the game is P-indivisible.
  - **New finding** (scratch `probe/cards.py`, exact, 16 cases): the peek line's 1/2 holds only if
    the re-burn overwrites the burn card, which holds the stored record (rules A and C). If the peek
    replaces only the revealed hole card, the answer is 1 (rule B). ch01:271 and :280 leave the
    rule unspecified.
  - The following are not carried:
    - the C1–C4 "card form" mapping, which is loose: its three modifications are bijectivity, C1–C3
      and an intervention rule, while C4 is the readback;
    - "quantum, not classical, statistics" (ch01:269);
    - the "interference term" and "phase" sentences (ch01:282, :284);
    - the unistochasticity sentence (ch01:286), which is in tension with Main:270 and Main:204;
    - the cat paragraphs.
  - The scope is stated: a classical toy whose one-step channel is entanglement-breaking, with no
    Bell violation.
  - Added risk R23. The ch01 sites themselves are a book matter for the owner, outside the paper.
- **Budget.** It stays at 14.25 pp: §5 2.25 pp (+0.5), §2 0.75 pp, §9 0.5 pp.
- **Other additions.** R24, the replacement-scope risk. CONTRIBUTION-r3 (a) items 7–8 and non-claims
  12–13. Decision 7 is marked decided, with retirement kept as a separate change.

## Not adopted, or observations

- **ch07:126 sentence 2.** "corrections that vanish exponentially in the dimension of the larger
  subsystem" is also live, and BH02 MANUSCRIPT-AUDIT (second-sentence item at :74–76) marks it
  "contradicts (C5)". The paper does not carry BH-02 C5, so it is not an R11 site for the paper.
  It is recorded here for the owner's correction list. No change was made to the r3 decision
  lists for it.
- Nothing from the re-check was left unapplied.

## Final owner-decision list (SOURCES-r3)

1. **Scope:** recommended, Alt-L or Alt-X. (a) Per scope, either correct the R11 sites first or
   choose a variant:
   - the sites: ch07:110, ch07:159–161, GR:811 and, for §7-h, ch07:126 s1 and GR:869, all with
     their FULL mirrors;
   - option (i), the BH-01-conflict-free variant, which still needs ch07:126 s1 and GR:869
     corrected;
   - option (ii), which drops §7-h as well.

   (b) The worked example.
2. **Wording of the Lean-check claim.** Retention is required in every case.
3. **Provenance of the design inputs.**
4. **Census registration and anchors.**
5. **A separate check of GR:226's box.**
6. **Page format and Appendix A scope.**
7. **The Explainer:** decided (replace). What remains is the separate retirement change and the
   content-migration audit for the absorption candidates.

**Flagged:** the title (R1), now weightier. The ch01 §1.11 card-table sites (R23) are a book
matter.
