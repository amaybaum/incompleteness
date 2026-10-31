# Re-check: introductory-paper design, revision 2

- **Objects:** `S/paper/design/OUTLINE-r2.md`, `CONTRIBUTION-r2.md`, `SOURCES-r2.md`,
  `CHANGES-r2.md`, against `paper/review/REVIEW.md` and `main` `687e885b` (worktree
  `S/paper/mainwt`).
- **Read-only.** No repository file changed. Git commands ran with
  `-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: BLOCK (wording only)

Every required change of REVIEW.md (R-1 to R-8), every finding F9–F14 and every nit N1–N10 is
correctly applied. The not-adopted item is acceptable.

The block is for one of revision 2's new additions, the "conflict-free §7 variant", and for an
error of mine that it carries forward.
- The variant is presented to the owner as free of corpus conflict, and the reviewed BH-02
  manuscript audit contradicts that (RC-1, RC-2).
- Decision 2 offers a wording-only option that I proposed in REVIEW.md. It does not escape §A.42
  (RC-3).

Each fix below is a few lines of wording. No mathematics changes.

***

## 1. Required changes of REVIEW.md: all applied

| Change | Check | Result |
|---|---|---|
| R-1 (F1) | CONTRIBUTION-r2:35–37 carries the review's wording verbatim. It also appears in (a)4 (:75–76), in (b) §6-d (:102), in non-claim 2 (:120–123) and in R22 | applied |
| R-2 (F2) | OUTLINE-r2:166: "on the qubit … (`five_way_minimality`, `Fin 2`)", `oi_alone_not_qm` as a qubit countermodel, E2 carrier-general; :59–61 likewise | applied |
| R-3 (F3) | OUTLINE-r2:164 and SOURCES-r2:136 cite `gl2_strong_gauge_moves_relative_candidate` (:537) and `gl3_constant_gauge_preserves_relative` (:451). Re-read: gl3 is `(U t * K) * (U s * K)ᴴ = U t * (U s)ᴴ` for a constant unitary `K`, which matches "a constant deformation preserves the relative candidate". UNTRACED-1(a) is re-scoped (SOURCES-r2:172–184) | applied |
| R-4 (F4) | OUTLINE-r2:55 and SOURCES-r2:138 have the unconditional chain. `finiteIsometryExtensionSF_discharged` is at IsometryExtension:116 (verified) | applied |
| R-5 (F5) | CONTRIBUTION-r2:104, :105 and :108; OUTLINE-r2:179–184; SOURCES-r2:150–155. "known in kind (elementary)" is gone everywhere (grep) | applied |
| R-6 (F6) | SOURCES-r2:312 (R11), :213–221 (decision 1(a)); OUTLINE-r2:189–196 and :256 | applied, but see RC-1 |
| R-7 (F7) | OUTLINE-r2:182 and :185; CONTRIBUTION-r2:135–136; SOURCES-r2:313 (R12) | applied |
| R-8 (F8) | CONTRIBUTION-r2:146–151, verbatim; OUTLINE-r2:128 (§3-d excludes the Main:532 remark) | applied |

**F9–F14 and N1–N10** are applied as CHANGES-r2:44–70 says. Spot-checked:
- N2 (GR:721);
- N3 ("on the system and at every positive ancilla level");
- N6 ("up to flipping the final bit");
- N7 ("in a bijective instance"; 32 non-injective violators);
- N8 (post-plan intervals);
- N10 (`ee2d4e68`);
- the F14 caveats at OUTLINE-r2:150.

**F10 path correction: accepted.** The designer is right. The literature-study reviews are at
`S/revlitcorr/` and `S/revlitbh/` (verified with `ls`). The path I gave in REVIEW.md F10,
`S/introaudit/revlit*`, is wrong. The two studies themselves are under `S/introaudit/lit-*`, as
SOURCES-r2:33–35 says.

**Not adopted (exact CMI in `probe/examples.py`): acceptable.**
- The probe is a scratch re-check, part of the reviewed object, and not cited by the paper.
- The paper cites Main:178–196 and `review4_probes.py`.
- The caveat ("float; matrices exact") is recorded at SOURCES-r2 §5-f, which is what REVIEW.md F14
  offered as the alternative.

## 2. New additions

### RC-1 — The "conflict-free §7 variant" is not conflict-free (required)

OUTLINE-r2:259 says the variant (§7-a, §7-b, §7-g, §7-h, §7-i, §7-j) "agree[s] with ch07's and
GR's current conditional statements on H-scramble and β". SOURCES-r2:217 offers it to the owner as
the "drop" resolution of R11. But §7-h is BH-02 C6(a) and C6(b), and BH-02's own reviewed
manuscript audit finds two sentences contradicted by exactly those results. Both are still live at
`687e885b`:

- **ch07:126, sentence 1** (mirror FULL:2003): "The framework's derivation of the Page curve runs
  through the *combinatorial* structure of the bijection φ …".
  - The audit's verdict (`bh02_scramble_v1/MANUSCRIPT-AUDIT.md:70–73`): "**contradicts**
    (definite configuration, aligned split); otherwise **conditions** (C1, C2, C3, C6(b)): in
    Theorem A.8 the combinatorial structure supplies averaging bookkeeping, and the entropy value
    comes from H-scramble".
  - The audit was made at `809fac52`. The sentence is unchanged at `687e885b`; only its third
    sentence was rewritten.
- **GR:869** (Remark, QES comparison): "the cycle-typicality argument of Theorem A.8, which
  invokes only Popescu-Short-Winter [29] … with no replica trick, no ergodicity assumption …".
  - The audit's verdict (MANUSCRIPT-AUDIT:256–259): "**contradicts** Theorem A.8 as stated …,
    which requires H-scramble … one long cycle is ergodic on the shell and has S = 0 throughout
    (C1)".
  - The phrase is unchanged at `687e885b`.

So the variant still states (§7-h: "not through bijectivity or the cycle decomposition") what the
reviewed package says contradicts ch07:126/FULL:2003 and GR:869.

The same sites also bind the recommended scope and Alt-L, which carry §7-h. This is a gap in
R11 itself: the original design missed it, and so did my REVIEW.md F6, which looked only at the
BH-01 manuscript audit.

What does hold up:
- §7-g agrees with the live text. The audit marks ch07:126 sentence 3 "supports, understated"
  (MANUSCRIPT-AUDIT:78).
- §7-i agrees with the corrected ch07:137–143 and GR:855–865.

**Exact fix.** Choose one of the following.
- **(a)** Make the variant §7-a, §7-b, §7-g, §7-i, §7-j. That is, drop §7-h as well, and say
  plainly that the variant drops the H-scramble finding.
- **(b)** Keep §7-h. Then:
  - rename the variant "BH-01-conflict-free";
  - add to R11 (SOURCES-r2:312), to decision 1(a)'s "correct first" list (:213–216) and to
    OUTLINE-r2:188–196 the sites "ch07:126 sentence 1 / FULL:2003" and "GR:869 ('invokes only
    Popescu-Short-Winter … no ergodicity assumption')", citing BH02 MANUSCRIPT-AUDIT:70–73 and
    :256–259;
  - state that every scope carrying §7-h meets these two sites.

  In either case, add the two sites to R11 for the recommended scope and for Alt-L.

### RC-2 — Under the variant, the contribution paragraph and the conclusion still carry what the variant drops (required)

- The draft paragraph (CONTRIBUTION-r2:38–41) states §7-c ("global bijectivity neither implies nor
  is necessary for recovery"), and under fix (a) also §7-h ("the Page entropy enters … through a
  scrambling hypothesis").
- §10 (OUTLINE-r2:238) restates "§7-c and §7-h".

**Exact fix.** Add one line to the variant's row (OUTLINE-r2:259) and to decision 1(a):

> "Under this variant, the contribution paragraph's black-hole sentence and §10 carry only §7-b
> and §7-i (and §7-h under fix (b))."

### RC-3 — Decision 2's wording-only option does not escape §A.42 (required; it corrects my REVIEW.md)

SOURCES-r2:225–232 and CONTRIBUTION-r2:58–60 offer "checked in Lean 4/Mathlib at commit X by recipe
Y" as an alternative to retaining an expected result. I proposed that alternative (REVIEW.md F9,
owner decision 1). It is wrong as stated.
- §A.42's opening paragraph and item 1 bind the claim, whatever word carries it. An enduring
  certification claim on `main` ("this declaration is proved, with these axioms, at commit X")
  needs "the commit …, the result it expects, and the recipe", with the expected result held as a
  small structured file.
- Item 3 places that file, for a paper, beside the paper's code and data.
- Removing the word "machine-checked" does not remove the claim.

**Exact fix.** Restate decision 2 as follows.

> "Any statement that the cited declarations are checked in Lean at a commit is an enduring
> certification claim under §A.42. Before the paper lands, an expected result for that commit (build
> success, the gate verdict, each cited declaration's `#print axioms` set, with recipe and
> provenance) is retained beside the paper, or the commit is shown to fall inside an archive the
> `evidence-retention` step covers. The owner's choice is only the word: 'machine-checked', or
> 'checked in Lean 4/Mathlib at commit X by recipe Y'."

Make the same change at CONTRIBUTION-r2:58–60 ("Until then …") and in R6.

The page format (single column, about 550 words per page) and Appendix A's default of about 15
kernel rows introduce no overclaim, and their arithmetic holds: 12–15 pp ≈ 6,600–8,250 words, and
the full map would bring the total to about 15.25 pp. Alt-L now keeps §7-g, as required.

## 3. The seven owner decisions

| Decision | Fairly stated? |
|---|---|
| 1 Scope | Yes for the three scopes. (a)'s variant premise needs RC-1 and RC-2 |
| 2 "Machine-checked" | Needs RC-3: the either/or is a choice of word, not of retention |
| 3 Provenance | Yes (paths now correct) |
| 4 Census | Yes |
| 5 GR:226 | Yes, scoped as a check of GR |
| 6 Page format and Appendix A | Yes |
| 7 Explainer | Yes. The counts re-verify (`verification/README.md` 15; FULL, `book/bibliography.md` 1 each), and frozen records are marked as not correction targets |

## Nits

- **n1.** ch18:148 says the Page time "is a mass-independent fraction of the evaporation time" but
  does not state the constant mass-loss coefficient. §7-i states that an M-dependent coefficient
  moves the fraction. This is a "conditions"-level tension, the BH-02 audit's category for the
  same omission at ch07 (MANUSCRIPT-AUDIT:108). Add ch18:148 (mirror FULL:4968) to R12 as a
  propagation site.
- **n2.** OUTLINE-r2:195 says "§7-c itself contradicts ch07:110 / FULL:1987, and §7-f contradicts
  GR:811". After RC-1, add "and §7-h contradicts ch07:126 s1 / FULL:2003 and GR:869" (fix (b)), or
  record their removal (fix (a)).
