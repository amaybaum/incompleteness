# Changes from revision 4 to revision 5

Revision 4, `novelty-v4/AUDIT.md` (sha256 `34764346…f616`), is
unchanged.

**Sources.**
- `main` moved from `c91bf5dd` to `8dc36d55`, which lands #920, #921,
  #922 and #910.
- PR #919 (head `240e31e8`) was read but has not landed.
- The two accepted literature studies are folded in:
  - `lit-blackhole/LITERATURE-v2.md`, sha256 `c7475d09…ce0d`;
  - `lit-correspondence/LITERATURE-v2.md`, sha256 `005cfe94…1c26`.

1. **Foundation restated (§2, C4).**
   - S ⟺ D ⟺ Q_fb is presented as a representation-equivalence theorem,
     not a characterization of non-Markovianity, as Main:98–99 now
     states it.
   - The old core display is classed WITHDRAWN (C4-old).
   - The (ii) ⟺ (iii) "characterization theorem", still in Main §3.4,
     the Explainer and book B.7, is C12 (REFRAMING, near-definitional).
2. **New class scheme (§0.4).**
   - The classes are NOVEL-CANDIDATE, KNOWN, PARTLY KNOWN, REFRAMING and
     WITHDRAWN. They replace v4's (a)–(d).
   - Every comparator carries FT, REC or NR (§0.2). Anything resting on
     REC or NR is PROVISIONAL.
3. **Classes changed by the literature (FT).**
   - C6 → KNOWN (B26 Eq. (50); SCH Thm 2).
   - C7 → KNOWN (BB; B23 footnote 5; B25 §3.5; PI).
   - C8 → KNOWN (BD Prop. 1; DO3 v3 is concurrent).
   - C2 → KNOWN (B25 p. 12; B23 §4.3; B26 §4).
   - C1, C1′ → PARTLY KNOWN (EG Props. 13, 16; LPW Prop. 1.5).
   - C5 → PARTLY KNOWN (GO Lemma 6 and footnote 8).
   - C8-D → PARTLY KNOWN (EG Props. 11–12; BD).
   - C4 → PARTLY KNOWN; the packaging part is PROVISIONAL (Milz and
     Strasberg not read).
   - C13 and C14 → REFRAMING, PROVISIONAL (Rutten and Hardy 2004 not
     read).
4. **C8-R carried forward** as NOVEL-CANDIDATE, "novelty unverified", per
   the owner's direction, with a §A.31 skeptical reading and the
   uncovered search areas named.
5. **C15 left unclassified.** No literature was examined and there is no
   internal audit. v4 had it as "(c), pending".
6. **C16 split** into C16a–e and C16-S against #920.
   - The Page-time formula and β > 1 are KNOWN (Page 2013 Eq. (8); Page
     2005 Eqs. (5)–(10)).
   - The QES-match, island-realization and GSL-proof claims are
     WITHDRAWN.
   - The mirrors were checked by grep.
7. **Fidelity table (§4).**
   - F1, F2, F2b, F9 and the F11 header are resolved.
   - F6 is narrowed.
   - F14–F20 are carried from LC §9. The identifiers are not renumbered.
   - F8 was refreshed by a corpus grep. It notes that Main names the
     Koopman operator (Main:728, :742) but cites no Koopman source.
8. **F13 kept separate (§6) and not resolved.** LC §7's findings are
   recorded as input, and the decision is left to the owner.
9. **Reading list (§5)** re-prioritized by what each item gates:
   - P1 (gates C8-R and C8-D): realization theory, automata and symbolic
     dynamics, and divisibility/revival forward citations;
   - P2 (C4 packaging and related work);
   - P3 (REFRAMING attributions);
   - P4 (black holes).
10. **Novelty statement (§7)** amended:
    - "representation equivalence; Markov included";
    - credit to Egri et al. and Barandes for the components;
    - credit to Buscemi–Datta for the dichotomy's (B) mechanism.

**Line-citation corrections made before finalizing:**
- the XOR remark is at Main:606;
- the QES-agreement sentence is at ch07:147;
- F10 concerns Main:62 only, since Main:272 uses Birkhoff–von Neumann
  correctly.

***

# Revision 5, r1 → r2

r1 is kept unchanged:
- `AUDIT-r1.md`, sha256 `ef9d475c…787a`;
- `CHANGES-r1.md`, sha256 `93f442dd…40af`.

The review applied is `revnov5/REVIEW.md` (BLOCK, wording only), cited as
`Rv5:N`. Each finding was re-verified before it was applied, against
`a411bf46`, against `ebf98d83` for the base, and against the reviewers'
`pdftotext` extractions.

**Blocking findings**

1. **XOR example (Rv5:1).** Re-tagged "concurrent: DO3 v3 App. A".
   - Verified: "XOR" is absent from DO1 and DO2, and
     `review4_probes.py` is first added at `e6c21398` (2026-08-11), lines
     6–8.
   - Class: KNOWN, PROVISIONAL. Prior candidates, both NR: Feller 1959
     [from memory] and Milz et al. 2019 = Main [10].
   - Both are added to §5 P3.6.
2. **"Machine-checked" (Rv5:2).** The §7 sentence now scopes it to the
   joint law, and says in the sentence that the time-$t$ identification
   is not formalized, as Main:99 does.
3. **FT basis (Rv5:3).**
   - §0.4 now applies the PROVISIONAL rule uniformly, with no textbook
     exemption; for textbook facts PROVISIONAL concerns the attribution
     only. Marked PROVISIONAL:
     - C9, C10, C11, C16e;
     - the "not located" parts of C1 and C5.
   - (e) is now "not classified" (an interpretation).
   - §7's evidence paragraph lists the PROVISIONAL items.
4. **C8-R (Rv5:4).** The owner's label is kept.
   - The candidate is scoped to the two-sided characterization.
   - EG Props. 16–18 (Prop. 18 on p. 35), restricted to one period with
     a clock and zero-prior root padding, are named as the sufficiency
     construction [FT; presence-checked], so sufficiency is PARTLY
     KNOWN.
   - Necessity is folklore.
   - Point 4 is added to the §A.31 reading.
   - The §7 novelty sentence now credits Egri et al. for the realization
     half.
5. **Base (Rv5:5).** Re-based to `a411bf46`.
   - Verified: only Explainer changed; its blob `a6d4cb2b` equals
     `240e31e8`; the line count is 1064 on both sides.
   - Updated: §0.1, the §1 table, §3 (e), §6 and the title block.
   - **Beyond the review:** `main` has since moved to `ebf98d83` (#911,
     #917, research records only). `papers/`, `book/`, the Lean modules
     and the census are unchanged, so every citation still holds. #917's
     black-hole records were not read; C16-S cites them as pending.

**Required findings**

6. **C12 sites (Rv5:6).**
   - Added: Main:212, :680; Explainer:378; Substratum:111, :126;
     appendix-b:455.
   - New F-notes:
     - F24: GR:20, "C1–C4 necessary as well as sufficient";
     - F25: glossary:39 / FULL:6659, "central result … four conditions";
     - F26: Explainer:378's self-narration.
   - Substratum:126's conflation of C12 with C10-B is noted.
7. **F8 and new F-notes (Rv5:7).**
   - "What Main does cite" is added: [4, 5] at Main:121; [4, 5, 9, 10]
     at :149; [4, 5, 7, 9] at :194; 't Hooft [1]; Spekkens named at :550;
     Hardy 2001 [51].
   - New F-notes:
     - F21: Main:332 cites BLP to [3, 4], and BLP has no entry;
     - F22: Main:149's "equivalent" contradicts :121 and :332.
   - C8 "Needed" now asks for a classical source at Main:121.
   - **Beyond the review:**
     - r1's F8 line "no citation of BLP" was too broad. BLP is named at
       Explainer:148, ch01:101 / FULL:445 ("[9]"), ch18:78 and
       FULL:4896, but `book/bibliography.md` has no BLP entry. F21 is
       extended to the book.
     - Explainer:148 and ch01:101 / FULL:445 assert the same
       "P-indivisibility is equivalent to information backflow". F22
       lists them as §A.25 sites.
8. **C8 credit (Rv5:8).**
   - Credited: Blackwell–Sherman–Stein (BD p. 4, ref. [3]) and Cohen et
     al. LAA 1993 (PI p. 14, ref. [26]), both [secondary] and
     presence-checked; BD for the divisibility form.
   - The §7 sentence now credits the contraction property, citing
     Cohen et al. and Buscemi–Datta. A bullet says to cite BD alone
     until Cohen et al. is read.
   - Both are added to §5 P1.3.
9. **(e) mirrors (Rv5:9).** F23: GR:20(ii) and ch07:46 lack the
   canonical-measure scope.
   - #919's description already names them as a separate correction.
   - Per the coordinator, they are within the manuscript-consistency
     PR's scope. That PR was not read.

**Nits**

10. **C4.** The three-way form is cited at Main:16–18, :526–530 and
    :580(1). Main:98–99 is S⟺D with the Q_fb route for ⊇.
11. **C5.** The König 1916 route [from memory] is noted. The "not
    located" part is PROVISIONAL; König is added to §5 P3.5.
12. **C16-S** is now "not classified", the same rule as C15.
13. **C12** no longer says "since #922 no longer the core". It now says
    Main:99 names the core, (ii)⟺(iii) was not the displayed core at
    `c91bf5dd` either, and glossary:39 still calls it the central
    result.
14. **Dating.**
    - C6 keeps LC §0.1's "bounds, not proves" caveat; SCH is prior
      regardless.
    - C1 now carries the EG dating. Verified: `process_dilation_probes.py`
      is first added at `64c95fee` (2026-08-10). Main.md at `6fc02988`
      (file then at the repository root) and at `bbf28c64` has no
      "process dilation" or "ledger".
15. **FT definition.**
    - FT is redefined as "the cited passage, read in the full-text
      document". BI, GO and LPW are partial reads; SC Def. 5 and EG
      Example 3 are noted.
    - C16a's Page quote is marked as a paraphrase.
16. **Reading list and README.**
    - §5 now tags venue/year details [from memory] or [secondary].
    - Added: Feller 1959; Milz et al. 2019; Cohen et al. 1993;
      Blackwell 1953; RHP [4, 5]; BJA [9]; König 1916; Berman–Plemmons
      (optional); Elfving 1937 and Kingman 1962 (optional).
    - F27: `book/README.md:64` omits H-scramble.

**Not changed.** Every FT-based KNOWN or PARTLY KNOWN class, the C16
split, F1–F20, F13's separation and C8-R's owner label. The review
confirmed all of these.

**Disagreements with the review.** None on substance. Two points go
beyond it (items 5 and 7 above): the further base move to `ebf98d83`,
and the book and Explainer BLP sites.

***

# Revision 5, r2 → r3 (nits only)

r2 is kept unchanged as `AUDIT-r2.md` (sha256 `df39e2f9…4b93`).

The re-check applied is `revnov5/RECHECK-r2.md` (ACCEPT WITH NITS),
cited as `Rc2:Nn`. Each nit was verified at `origin/main` `ebf98d83`
before it was applied. Draft PRs #925 (`75a99444`) and #926 (`26e365d7`)
were fetched read-only and diffed against `ebf98d83`.

- **N1 (C1 dating).** The C1 dating now says "no process-dilation or
  history-ledger text". Verified: `bbf28c64:papers/Main.md:394` has
  "ledger" in the unrelated posit ledger.
- **N2 (§7).** The novelty sentence cites Buscemi–Datta alone, "in the
  divisibility form". Cohen et al. and Blackwell stay pending (§5 P1.3).
- **N3 (§7).** "Adapts" is replaced by "is an instance of the
  time-indexed construction of Egri et al. (Props. 16–18), packaged as
  one bijection". The realizing class is named: one finite permutation
  with a hidden prior shared by all roots. A bullet says no provenance is
  asserted.
- **N4 (C1′).** C1′'s "not located" remainder is marked PROVISIONAL, and
  C1′ is added to §7's evidence paragraph.
- **N5 (F21).**
  - Added: appendix-b:96 / FULL:5883 (consistent with Main:332) and
    Explainer:624.
  - Added: the ch01 numeric-citation mismatch. ch01 cites [2] at :32,
    [8] at :85 and [9] at :101 against the author-year bibliography;
    under Main's numbering [9] is Bylicka–Johansson–Acín (Main:792).
- **N6 (F23).**
  - Added: ch01:79 and :83, their FULL mirrors, and Main:86's
    "(§1.3 Remark)" pointer, all verified at `ebf98d83`.
  - Status recorded: #926 scopes ch01:77–83, ch07:46 and GR:20(ii), with
    their FULL mirrors; #925 points Main:86 and :522 at §1.2's Remark.
    Both are drafts, not merged.
- **N7 (Explainer standing).** Recorded in §0.1:
  - the current status note at Explainer:3–8 (superseded and frozen);
  - #926's replacement text, verified at `26e365d7`;
  - that the Explainer is superseded and is not a drafting source for
    the introductory paper;
  - that the Explainer sites are for the owner's decision.
- **N8 (C3).** Milz et al. 2020 and Strasberg–García Díaz 2019 are tagged
  "venue [from memory]".
- **Open draft PRs (§1, new block).** The status of #925 and #926 is
  recorded, together with what neither fixes:
  - GR:20's "necessary as well as sufficient" (F24);
  - glossary:39 / FULL:6659 (F25);
  - the F21/F22 sites;
  - the ch01 numeric mismatch;
  - `book/README.md:64` (F27).

**Beyond the message.**
- The diff shows #925 also changes the lines of F3, F4, F5 (Main:608,
  :690), F6 (Main:580(2)), F10 (Main:62) and F12 (Main:167). This is
  recorded as status only, since those changes are not merged and were
  not reviewed.
- #925 does not change Main:212, :680, :149 or :332.

**No classification changed.**
