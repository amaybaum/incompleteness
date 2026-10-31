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

***

# Revision 5, r3 → r4 (re-base and first-hand literature reading)

**What r4 starts from.**
- r3 is kept unchanged as `AUDIT-r3.md` (sha256 `6dae22ac…99f9`), copied
  from branch `draft/oi-introductory-paper-20261025` at `3fcf210f`.
- The owner approved r4 ("Proceed with the re-base and publication to
  #918").
- r4 has had no separate review.

**1. Re-base to `origin/main` `83d1da1b`** (§0.1, §1, §4).
- **Merges covered.** #925 (`8b5e8681`), #926 (`c1cade86`), #927
  (`03eb1395`) and #928 (`83d1da1b`, a CI workflow only).
- **How it was checked.** Every F-note site was read at `a411bf46` and at
  `83d1da1b`. Each fix is attributed to a commit on the merge's
  second-parent history.
- **Line maps** are stated in §0.1. Explainer is −5 after line 8; ch01 is
  +2 after line 83; FULL is +2, +4 or +6 by range. Main, GR, ch07,
  appendix-b, glossary, Substratum and README are unchanged.
- **Unchanged kernel inputs.** No kernel module, census,
  `arc-b-rooted-classification/result.md` or `oi_lattice_code/` file
  changed after `a411bf46`.
- **Fidelity-note status:**
  - **Fixed:** F6, F10, F12, F21, F22, F23, F24, F25, F27.
  - **Changed, with part still open:**
    - F3: the $e^{-i\hat H}$ remark at Main:532;
    - F4: the title, Main:2;
    - F5: Explainer:373;
    - F8: only BLP is now cited.
  - **Open:** F7, F14–F20, F26.
  - **Kept separate:** F13. Its sites are unchanged; the Explainer ones
    are renumbered :282, :1015.
- **F28 added.** Main:332 cites [4] for "monotonicity of system-plus-ancilla
  distinguishability characterizes CP-divisibility".
  - Introduced by `6250782a` (#927).
  - RHP 2010 gives an entanglement witness and a Choi-norm criterion. The
    distinguishability characterization is BJA [9] (bijective maps), or
    BD.
  - A correction PR was then being prepared. It landed as #930 (see "r4
    re-check" below).
- **C12 sites restated.** Main:608 now carries the reduction and "neither
  is formalized". GR:20 and the glossary are fixed. Explainer:373 (F5,
  F26) and Substratum:126 (the C12/C10-B conflation) stay open.
- **Other §3 updates from the re-base:**
  - C5's Internal (F10 fixed);
  - C9's Internal (F12 fixed);
  - C10-B (F6 fixed);
  - (e)'s mirrors (F23 fixed; F4's title open);
  - C16d's propagation list (FULL renumbered; F27 fixed).

**2. First-hand full-text reading** (§0.2, §8; new class FT-r4).
- **What was read.** 19 open documents: arXiv, plus two free-access
  Cambridge Core publisher PDFs. Each is identified by URL and sha256,
  with the PDF page and quoted passage.
- **Not retained.** No PDF or extraction is retained.
- **Unread primary texts.** Each is listed with its reason (§0.2):
  - bot challenge: Project Euclid (Blackwell; Feller and Heller, on the
    same host, not attempted) and SciELO (van Kampen 1998);
  - HTTP 403: ScienceDirect (Cohen et al., Rabin, Carlyle);
  - paywall: Anderson, Vidyasagar, Davis, Bennett, Fine, König;
  - book: Paz, Kallenberg, Breuer–Petruccione, Parzen, van Kampen,
    Cover–Thomas.
- **Bibliographic upgrades.** Blackwell 1953, Cohen et al. 1993, Feller
  1959, Heller 1965 and König 1916 are now [REC, Crossref]; their content
  is still unread.

**3. Classification changes.**
- **XOR example: KNOWN, PROVISIONAL → KNOWN (FT-r4).**
  - RHP 2014 (Main [5]) Eq. (15), p. 7, is the same process up to
    relabelling the final bit.
  - Capela et al. 2019, p. 6, give the four-time parity version.
  - Milz et al. 2019 (Main [10]) is not a source for it.
  - Feller 1959 is unread (not attempted; same host as Blackwell's bot
    challenge), and the first statement of the example is unverified.
- **C3: REFRAMING, PROVISIONAL → REFRAMING (FT-r4)**, from
  Strasberg–García Díaz, p. 2, Eq. (3).
- **C8: KNOWN.** Its evidence now includes RHP 2014 Thm 2.4 (p. 8), the
  classical divisibility form, in Main's own [5].
  - The r3 "Needed" item asking Main:121 for a classical source is
    withdrawn, since [5] is one.
  - Cohen et al. and Blackwell become optional.
- **C4: PARTLY KNOWN; packaging part still PROVISIONAL**, now on one named
  area (the comb-realization theorem).
  - Milz et al. 2020 and Strasberg 2019 were read.
  - They study Kolmogorov consistency of projective records, a different
    question. Neither states S ⊆ $Q_{\mathrm{fb}}$.
- **C5: PARTLY KNOWN.** The construction is now FT-r4 (Johnson, Dulmage
  and Mendelsohn 1960, p. 4).
  - The rationality of the weights is this audit's one-line inference.
  - An explicit statement is still unlocated, and stays PROVISIONAL.
- **C8-R: NOVEL-CANDIDATE, novelty unverified, no priority sentence.
  Unchanged.**
  - P1.3 is read.
  - P1.1 and P1.2 are read only in open surveys (Monràs–Winter; Ohta;
    Antonelli et al.). Their primary texts are unread.
  - The gate is narrowed to P1.1 and P1.2 in primary text, plus BD's
    forward citations.
- **C8-D: PARTLY KNOWN, PROVISIONAL. Unchanged.** RHP 2014 Thm 2.4 is
  added for (B). No recurrence-forced dichotomy was found.
- **C1, C1′: unchanged.** Their decisive sources are paywalled or books.

**4. §7 wording.**
- **Divisibility credit.** "in the divisibility form of Buscemi and Datta
  2016" becomes "in its divisibility form (Rivas, Huelga and Plenio 2014,
  Thm 2.4; Buscemi and Datta 2016)". This supersedes Rc2:N2.
- **C8-R stated as a candidate.** It is stated explicitly as a candidate,
  not a novelty claim. The admissible "not located" wording is scoped to
  the literature actually read.
- **Correct versus original.** A table of correctness against originality
  is added (also §0.4 and the header).
- **Related work** gains the FT-r4 sources.

**5. §5 restated.** Items read in r4 are marked read, and each unread
primary text carries its reason. New item: the quantum-comb realization
theorem (P2.1). P3.6 (XOR) is satisfied for attribution.

**Unresolved:**
- the P1.1 and P1.2 primary texts and BD's forward citations (C8-R gate);
- Cohen et al. and Blackwell (optional);
- the comb-realization theorem (C4);
- König 1916 (C5);
- Feller 1959 and who first stated the XOR example;
- Fine, Bennett and Kallenberg (C1, C1′);
- #917's records (C16-S).

## r4 re-check applied (`revnov5/RECHECK-r4.md`, ACCEPT WITH NITS)

The re-check is cited as `Rc4:Rn` and `Rc4:Nn`. It is retained as
`review/RECHECK-r4.md`. Every item was verified at `origin/main`
`52e2db40` before it was applied.

**Re-base to `52e2db40`.**
- #916 (`61930e90`) changes only `tools/citation_roles_check.py` and
  `tools/release_gate.py`.
- #930 (`52e2db40`, commit `4c5554ce`) changes Main:332, Main:606,
  appendix-b:96 and FULL:5885, one line each, with their `.tex`/`.pdf`.
- The §0.1 blob table now gives Main `d59e5b5f8735`, appendix-b
  `d963a1c4698b` and FULL `5b94af0bd743`. Every other blob is unchanged
  from `83d1da1b`.
- Line numbering is unchanged.

**R1, F28.**
- §4 marks F28 **fixed** by #930. The fix:
  - Main:332 now attributes the entanglement witness to [4] and the
    distinguishability characterization to [9], "for bijective
    (invertible) dynamical maps on $\mathbb{C}^d$ … a
    $(d+1)$-dimensional ancilla". This was checked against BJA's abstract
    and p. 1.
  - The mirror at appendix-b:96 / FULL:5885 is restricted to bijective
    maps, and its pointer is corrected from "[Main §3.4]" to
    "[Main §3.2]". Main:332 lies in §3.2, Main:258–353.
- r4's "carry no misattribution of their own" is corrected. It missed the
  mirror's missing scope and wrong pointer.
- The XOR "Needed" item records #930's addition at Main:606: "up to
  flipping the final bit, the process of [5], Eq. (15)".
- §1 gains rows for #916 and #930. The README is updated.

**R2, the parent `README.md`.** "Findings carried forward" and
"Unresolved literature and scope questions" are updated item by item,
each verified at `52e2db40`:
- Main:98's bare form: fixed by #922. Main:98–99 now reads "that is
  $S \iff D$, Markov laws included".
- The `S_imp_D` / `RevReal` docstring item: resolved by #922. Main:500
  scopes the prior independence as "not formalized", and
  `Equivalence.lean`'s docstring says so too.
- Explainer:120's dark-energy splice: removed by #919. It is present at
  `a411bf46^1` and absent at `a411bf46`.
- The D-gauge migration: done by #921. appendix-b:432 and :444 carry
  "Bohr frequencies and the D-gauge classification" and Theorem B.7.5c.
- Page time: by #920, ch07:137–143 states 0.646 as the β = 1 value of
  $1-(\beta/(1+\beta))^{3/2}$. GR:863 and ch07:143 give "β ≈ 1.485 and
  t_P ≈ 0.538 t_evap" from Page [60]. The numeric 1.485 was not
  re-checked against Page here.
- C8: classified KNOWN.
- F3–F9: pointed to `novelty-v5/AUDIT.md` §4.
- The other items are kept, with their current status.

**Nits.**
- **N1, page indices.** RHP 2010's Fig. 1 and "no longer constrained" are
  on PDF p. 1. Milz 2020's Thm 4 statement is on p. 20, and its proof
  sentence on p. 21. Corrected in C4, F28 and §8.
- **N2, Feller and Heller.** Both are now "not attempted (same host as
  Blackwell 1953's bot challenge)", consistently in §0.2, C8-R, §3 XOR,
  §5, the README and the r4 section above.
- **N3, F29.** Added under C12 as a candidate owner F-note, with a
  candidate row in §4. The phrase "containing a memory witness" was
  found at glossary:39, FULL:6661 and GR:20 only. Explainer:353 and :373
  use "per/each finite accessible horizon", so the re-check's mention of
  them is narrowed.
- **N4, the C8 row.** It now qualifies "kernel" as matrix and routed
  levels, with the step from history-level (C4) in prose.
- **N5, venues.** Crossref records were read for Strasberg–García Díaz
  (PRA 100, 022120), Milz et al. (PRX 10, 041049), Capela et al. (PRR 2,
  013350) and Milz–Modi (PRX Quantum 2, 030201). All are now [REC].
- **N6, Egri.** The parenthetical is replaced. No "Egri" occurs; the
  case-insensitive hits are substrings of "integrity".
- **N7, F28's scope defect.** F28 now names both defects: the citation
  and the missing bijective scope.

**No classification changed.**
