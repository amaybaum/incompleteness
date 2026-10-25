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
