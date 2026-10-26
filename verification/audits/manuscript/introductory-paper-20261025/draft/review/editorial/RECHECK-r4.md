# Editorial re-check: Introduction r4 (confirmation)

- **Object:** `verification/audits/manuscript/introductory-paper-20261025/draft/Introduction-r4.md` on #918 at `ebd425c0`.
  - sha256 `5f9fdcc532747e263e111accbf2c78541043eb05c1c539975512d6183d0d68f6`, verified.
  - The diff from r3 touches 8 lines: 32, 114, 234, 241, 257–261 → 257, 289, 291 and 313. Appendix A is unchanged.
- **Read-only:** no repository file changed.
- **Build tree:** `S/paper/ed-review/tree4/`, a fresh `git archive` of `687e885b` with r4 at `papers/Introduction.md`.
- **Layout probes:** `S/paper/ed-review/r4/`.

## Verdict: ACCEPT WITH NITS

The eight changed lines are correctly applied, every check passes, and the main narrative is 12 pages. Two points need an owner decision:

- **Total length.** The paper now runs to 16 pages. One layout-only edit to an approved raw line brings it back to 15; see §1.
- **One wording choice in the new Contributions sentence.** See §2.

## 1. Build and length

**Build.** `sh ./build.sh Introduction` returns `build: OK`.

| Measure | Value |
|---|---|
| Pages | 16 |
| Overfull boxes | 0 |
| Missing characters | 0 |
| Median characters per page | 2,556 (drafter: 2,554) |

Words per page: 353 463 374 452 460 413 423 450 436 397 434 359 229 280 354 44.

**Layout.**
- §7 Conclusion ends on p. 12, so the main narrative is 12 pages. That is inside the owner's "about 12–15 pages of main narrative".
- The Code section and Appendix A are on p. 13, the References on pp. 14–16. Page 16 carries 44 words: [Sch21], [SGD19] and [Sha79].
- The drafter's report is confirmed. Since the owner's target is stated for the main narrative, 16 pages in total does not breach it.

**Can the 16th page be recovered by layout only?** Each variant below was built from r4 by the repository recipe. The text column records whether the extracted text matches r4's, ignoring whitespace, hyphens and page-number lines.

| Variant | Pages | Overfull | Text | Wording or raw change |
|---|---|---|---|---|
| r4 as is | 16 | 0 | — | — |
| Move the approved `\begingroup` line up to before "Code, data…" | 16 | 0 | identical | none |
| Move it up to before §7 | 16 | 0 | identical | none |
| Drop the `***` rule before §7 | 16 | 0 | identical | markup only |
| **Approved line `\begingroup\small\raggedright` → `\begingroup\footnotesize\raggedright`** | **15** | **0** | **identical** | **none; same two lines, one size command** |
| As above, plus drop the `***` rule before §4 | 15 | 0 | identical* | markup only; also fixes item 5 |

\* `cmp` reports two differences between the two builds. Both are extraction artifacts, not content changes:
- pdftotext reads the stacked fraction `\tfrac14` as "14" in one build and "41" in the other;
- the page number "9" is embedded in a word hyphenated across a page break.

The sorted word lists differ only in which line falls at a page top.

- **Answer: yes.** Changing `\small` to `\footnotesize` in the first approved raw line returns the paper to 15 pages, with 0 overfull boxes and identical text.
- No wording changes, and no third raw line is added. That size applies only to Appendix A and the References, about 8 pt in a 10 pt document, which is common for reference lists.
- Whether editing the content of an approved line still falls within the approval is the owner's call. The edit is layout only.

## 2. Line 32 (Contributions)

**My N-a wording** is applied verbatim: "It presents the established mathematical results of OI together, separates …, states …, and summarizes … within the scope stated in §5." The register is clean. The self-descriptive adjectives and the repeated "The paper … This paper" are gone.

**The added sentence** reads "The black-hole results of §5 are reported from unpublished repository computations [BHa; BHb] whose novelty has not been established."

- **Its content is right.** It resolves O-1: "no new … result" is no longer in tension with §5, whose results now carry their source status.
- **Register.** "whose novelty has not been established" reports the state of a literature search rather than a property of the results. It is the same family as r1's "literature … was not read" (F3a), though much milder and phrased as a status.
- **Admissibility.** It is admissible as a priority disclaimer, and the owner rule asks for no novelty claim.
- **Optional, more neutral form:** "The black-hole results of §5 are taken from unpublished repository computations [BHa; BHb], and no priority is claimed for them." This is a nit; it does not block.

## 3. Inline recipe (line 257)

- The recipe is now inline code in the sentence. It sets with 0 overfull boxes, and the Code section is no longer split across pages: all of it sits on p. 13.
- In the PDF the command breaks across a line at its internal space ("…by the recipe python3 / tools/lean_axiom_check.py --require-lake"). That is harmless: a copy from the PDF still yields the command with whitespace between the two tokens.
- No raw LaTeX is used. ✔

## 4. [BHa] and [BHb] (lines 289, 291)

- **[BHa]** reads "A. Maybaum, recovery from accessible records in finite reversible models, unpublished research record, internally reviewed; `bh01_access_v1/` …".
  - The drafter is right not to put a non-title in quotation marks; the record's actual title is "BH-01 access audit, v1: report".
  - As set, though, the unquoted, lower-case phrase reads like a sentence fragment, and it is inconsistent with [BHb]'s quoted title.
  - Nit: use the bracketed descriptive-title convention for untitled or retitled works, "[Report on recovery from accessible records in finite reversible models]". Or quote the actual title and accept "audit".
- **"Unpublished research record, internally reviewed"** (science T2) is source-status wording confined to the bibliography. It is acceptable there: science governs content, and §A.32 targets paper prose. ✔

## 5. Orphan "(§4.3)." at the top of p. 7

- Confirmed. It is a widow: the last line of §4's lead sentence ("…and the smallest realization of Theorem 3 (§4.3).") falls at the top of p. 7, directly above "4.1 A minimal model".
- **Fix without wording or raw LaTeX:** drop the `***` rule before "## 4. Illustrative examples". "(§4.3)." then ends p. 6 and p. 7 opens with §4.1. The text is identical apart from the extraction artifacts noted in §1, and the result is 16 pages, or 15 combined with the footnotesize change.
- **Cost:** one section boundary without the house `***` rule.
- **Alternative:** leave it. Any later edit before §4 will move the break anyway, so I recommend fixing it at the final layout pass, not now.

## 6. Checks re-run (tree4)

- **`voice_check`:** OK, 41 files scanned, r4 included.
- **`claims_check`:** OK.
- **`identcheck.py`** on r4:
  - 51 backticked tokens, of which 28 are distinct Lean identifiers, with **0 unresolved**;
  - 28 Appendix A identifier–module–line entries, with **0 mismatches**;
  - Equivalence.lean:466–468 are the three composition lines.
- **Census:** still vacuous for this paper (RECHECK-r3 §6). The direct check above is the evidence.

## 7. Other changed lines

- **114.** "[Main §1.3, the realization clause of (C4)]". Main:78 has "belong to this realization clause", so the target exists. ✔
- **234.** "…the gravitational continuum limit of the substratum's spatial coupling graph…". "Lattice" is gone, which resolves N-b. "Spatial coupling graph" is not defined in this paper, but it is self-explanatory enough for a single mention. Nit only.
- **241.** "each proved on paper or checked exhaustively at small size or by exact arithmetic". Clean register, and the disjunction is correct: the §5.1 counts are computations only. ✔
- **313.** The VERIFY comment is reworded and is not visible in the PDF. ✔

## Owner items carried

1. Total length of 16 pages. The main narrative is 12. Optional layout-only recovery: `\small` → `\footnotesize` in approved line 268 (§1).
2. Title hyphenation, unchanged from RECHECK-r3 §5.
3. Landing gates: 9 OWNER markers (R11 ×6, R12, decision 2 / retention, and retention §A.42) and 5 VERIFY markers (BBS24, Cal26, CT06, Har04, Sha79).
4. Re-run `identcheck.py` at landing, because the census does not cover this paper.
