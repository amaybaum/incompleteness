# Introduction draft r8: changes from r7 (black-hole alignment to #936)

## Inputs

- **Base:** r7, sha256 `3ef2725b…7cfd`; r7 is unchanged.
- **Main at `17b830bc`** (#936 merged; reviewed head `b862df75`, identical tree):
  - papers/GR.md App. A.5–A.7, which includes H-decouple, Thms A.7–A.9, "Proper energy shells" and the
    single-trajectory paragraph;
  - book ch07 §7.6, ch18 §18.5 and ch19.
- **#936 records:** `verification/audits/manuscript/bh-consistency-20261026/`, namely README, CHANGE-NOTE,
  A8-REVIEW and A8-RECHECK.
- **Reference check:** `S/refs/FINDINGS.md`.
- **Owner direction (2026-10-26):** lead with the distinction between preservation and accessible recovery, and
  keep the Page curve as a conditional result that does not carry the argument.

**Method.** `S/paper/draft/scripts5/build_r8.py` applies 10 edits to r7, each an exact, uniquely matching
replacement. Every sentence it does not touch is byte-identical to r7.

## Changes

| # | Where | Change | Source on main `17b830bc` |
|---|---|---|---|
| 1 | §5 | **Order.** The section now runs: the problem and the two questions, then the separation of conservation from accessible recovery (claim A), then the finite-model evidence [BHa], then a single Page-curve paragraph. The first three paragraphs are unchanged. r7's configuration-space paragraph moved into the Page paragraph as its setup, so the section's argument starts directly after the opening paragraph | — |
| 2 | §5 | **Page-curve material compressed.** r7's two Page paragraphs and the paragraph on the generalized second law (GSL), QES and islands become one paragraph | GR App. A.6–A.7 |
| 2a | | It opens: "The Page-curve calculation of [GR App. A] addresses recovery under its own conditions and is a conditional result [Book §7.6, §18.5]." | ch07:110 ("which the Page-curve derivation below addresses under its own conditions"); ch18:146 ("the Page curve at the emergent level is a conditional result") |
| 2b | | Result: for all but an exponentially negligible fraction of initial conditions, the full-cycle time average, at the bipartition of each stage held fixed, equals the Page value [Pag93; GR, Thms A.8–A.9] | GR A.8 statement and proof ("For all but an exponentially negligible fraction of initial conditions, … equals the Page value"); A.9 statement |
| 2c | | **H-scramble:** "the orbit ensemble equidistributes over quantum pure states on the shell"; it "fails for every bijection" acting on a definite initial configuration with an aligned bipartition; it is not established | GR A.8 proof: the H-scramble paragraph and "The same holds for every bijection" |
| 2d | | **H-decouple, by name:** "$B\cup R$ evolves with no coupling to $D$ or to the rest of the visible sector, $V\setminus R$, and its joint state is pure", over whole cycles; "timescale ordering does not supply it"; not established | GR App. A.7 setup, verbatim except that "the trans-cosmological sector" is dropped (the paragraph has just defined $D$) |
| 2e | | **Full-product-space scope of Thm A.8:** the whole configuration space is one energy shell; this "requires the energy to be constant there, so that energy conservation places no constraint on the orbit"; it "does not follow from the conservation of a Hamiltonian that takes more than one value there"; "an evaporating black hole whose radiation carries away its energy is in the proper-shell case", which is open, with the mean entropy shell-dependent and in general different from the Page value | GR "Proper energy shells" paragraph (A8-REVIEW fix A2a, as merged) |
| 2f | | **Time-average-only form:** "whether the entropy along a single trajectory follows the same curve is open" | GR, the paragraph after Thm A.9 |
| 2g | | Kept unchanged from r7: the covariant field equations (GR's dependency ladder); GSL not derived; QES agreement not established; islands correspondence conjectural; "not established"; "not resolved here" | r7 l.176 and l.178 |
| 3 | §5 | **Removed with the compression:** the clause "$t_{\rm evap}/\tau_B^D\ge10^{57}$ … [GR App. A.5; BHa, item F]" and its two symbol definitions. The point it supported, that timescale ordering does not supply the closure, is kept in GR's words. GR App. A.7 gives the numbers ($\sim10^{62}$ at $\Gamma\sim1$) | GR App. A.7 |
| 4 | §6.3 | "whether H-scramble and the closure condition hold, the Page value on the relevant shell" becomes "whether H-scramble and H-decouple hold, the Page value on a proper energy shell and along a single trajectory" | GR "Proper energy shells" (open); the paragraph after Thm A.9 (open) |
| 5 | abstract, §6.2 item 4, §6.4 | Text unchanged. Each already leads with the separation and states that the Page curve is not established and the problem is not resolved. Only the R11 markers are removed (item 6) | — |
| 6 | R11 markers | **All six removed:** abstract, §5 ×3, §6.2 item 4 and §6.4. Every site they named is corrected on `17b830bc`; see the next table | #936 |
| 7 | [BBS24] | "; arXiv:2310.01205v2" added. The VERIFY comment is unchanged (see Departures 3) | `S/refs/FINDINGS.md` (SUPPORTED; DOI matches) |

## R11 marker sites, checked at `17b830bc`

| Marker site (r7) | Named site (line at `687e885b`) | Text at `17b830bc` | Status |
|---|---|---|---|
| §5 claim A | ch07:110 / FULL | "resolves the paradox at the level of information preservation: … how much of that information an observer can recover from the radiation is a separate question, which bijectivity alone does not settle …" | corrected |
| | ch18:146 / FULL, s2 | "whether the radiation carries it is a separate question, which bijectivity alone does not settle"; "the Page curve at the emergent level is a conditional result" | corrected |
| | ch18:158 / FULL | "(the substratum preserves it, by bijectivity; whether the radiation carries it is the separate question of Chapter 7 §7.6)" | corrected |
| | ch07:159–161 / FULL (falsifier) | The empty falsifier is removed. "a measurement of the radiation alone therefore does not test the conservation claim, which rests on bijectivity as a premise" | corrected |
| §5 Page paragraphs | ch07:126 s1–2 / FULL | "does not use the gravitational path integral …"; Page's mean plus measure concentration; full-product-space scope with "places no energy constraint" | corrected |
| | GR:869 (now the A.7 QES remark) | "under H-scramble and H-decouple, with the full product space as the energy shell …, a cycle-averaged Page curve" | corrected |
| | ch18:146, ch19:334 (unconditional Page curve) | "a conditional result"; "Preserved; Page curve conditional" | corrected |
| | GR Thm A.8 shell scope | restricted to the full product space; the proper-shell case stated as open | corrected |
| §5 closure | GR:811 ("D is frozen on evaporation timescales") | replaced: A.5(i) freezes $D$ only for $t\ll\tau_B^D$, and **H-decouple** is defined | corrected; the label is now on main |
| abstract, §6.2 item 4, §6.4 | restatements of §5 | follow the §5 sites above | resolved with them |

**No R11 marker remains,** and no named site is uncorrected on main.

**Remaining owner and verify markers:**
- 3 OWNER markers: the Weinberg 1989 gate, unchanged, and the two §A.42 retention markers.
- 9 VERIFY markers, unchanged.

## Departures

1. **"A qualified supporting result" is not used verbatim.** In paper prose it is a self-assessment of the
   framework, which §A.32 excludes. The paragraph says the same thing in main's own words: it "addresses recovery
   under its own conditions and is a conditional result". This is the book's merged wording (ch07:110, ch18:146).
   If the owner wants the phrase itself, it can replace that clause.
2. **The $10^{57}$ timescale clause is dropped** for compression (change 3). GR App. A.7 keeps the numbers.
   [BHa, item F] is no longer cited in the text; [BHa] is still cited for the finite results.
3. **The [BBS24] VERIFY comment is left as it is** ("content not read in the audits"). The reference check has now
   read Def. 1 first-hand, so the owner or coordinator may update that comment. It was not changed here, because
   VERIFY entries are landing gates.
4. **The Lean commit stays at `687e885b`.** The Conventions and Code section still name `687e885b`. `lean/` and
   `lean-mathlib/` are identical at `17b830bc` (empty `git diff --stat`), so every cited declaration is unchanged.

## Build and checks

- **Build:** 17 pp; 0 overfull boxes; 0 missing glyphs; median 2,606 characters per page.
- **Main text:** abstract to §6.4 ends on p. 12 at line 36, the same position as r7. That is **11.73 pp** by the
  editorial measure; r7 measures 11.78.
- **Repository checks** on a fresh `git archive 17b830bc`, with r8 as `papers/Introduction.md`: `voice_check` (41
  files), `claims_check` and `duplicate_check` are OK.
- **Identifiers:** `identcheck.py` finds 28 identifiers, 0 unresolved and 0 mismatches.
- **Bibliography:** 38 keys, none uncited.
- **§A.32/§A.33 scan of the 4 added lines:** 0 phrase hits; the only all-caps word is VERIFY, inside a comment.
