# Introduction paper: working draft (WIP, under review)

`Introduction.md` is the working draft of the Introduction paper, written from `../design/OUTLINE-r4.md` at `main`
`687e885b`. It is not a manuscript: it lives here, not under `papers/`, until it passes independent scientific and
editorial review and the owner accepts it. `DRAFT-NOTES.md` maps the outline to the draft, lists the departures from
r4, and lists every `OWNER` marker (decisions pending) and `VERIFY` marker (bibliography entries to check).
`probe/swap_memory.py` is the numerical check behind the draft's correction of the r4 card-table clause.

The repository's default build gives 20 pages; with one-inch margins, 14 (page format is an open owner decision).

## Reviews of this draft (r1)

- `review/scientific/REVIEW.md`: independent scientific review, ACCEPT WITH CHANGES. It confirms the draft's
  correction of the r4 card-table clause by an exact check (`review/scientific/probe/card_exact.py` and its output):
  the no-classical-memory result of Main:702 holds for the swap with an initialized hidden slot; with the card game's
  uniform independent burn card the identity two-step map decomposes through classical memory. It finds one false
  statement and six other required changes, and checks the bibliography against Crossref and arXiv records
  (`probe/crossref.py`).
- `review/editorial/REVIEW.md`: independent editorial review, ACCEPT WITH CHANGES (rendering, register, definitions,
  notation, structure, bibliography form, and a cut list to reach 15 pages in the default format;
  `scripts/cutprobe*.py` are its cut probes).

`Introduction-r2.md` (with `DRAFT-NOTES-r2.md` and `CHANGES-r2.md`) applies both reviews: 15 pages in the
repository's default build, no dropped glyphs, `voice_check` and `claims_check` pass. Its owner markers list the
decisions still open; the paper does not land while any R11 site is uncorrected or the §A.42 expected result is not
retained.

## Re-checks of r2, and r3

- `review/scientific/RECHECK-r2.md`: BLOCK (narrow). Four required replacements: §6.4(5) stated the framework's
  adopted Bell branch as a necessity; §6.3 drew its conclusion before the imported unboundedness premise; §5.4 dropped
  BH-01's scope limit on GR Thm A.7; two steps were labelled "proved on paper" that Main gives no written proof of.
  Also seven nits and four erratum nits (E1–E4).
- `review/editorial/RECHECK-r2.md`: ACCEPT WITH NITS, with an overfull-box analysis.

`Introduction-r3.md` (with `CHANGES-r3.md`) applies R2-1 to R2-4 verbatim, the nits, and the owner decisions of
2026-10-26: the title, a Contributions paragraph that claims no new theorem or physical result, two raw LaTeX lines
that change layout only, and the conservative handling of D1–D3. 15 pages in the default build, no overfull boxes,
no dropped glyphs. `CHANGES-r3.md` records where r3 departs from a reviewer's suggested text and why. The R11
markers, the §A.42 retention marker and five VERIFY markers still gate landing. `../design/ERRATUM-r4.md` applies
E1–E4.

## Re-checks of r3, and r4

- `review/scientific/RECHECK-r3.md`: ACCEPT WITH NITS. It confirms R2-1 to R2-4, and confirms r3's departure from the
  suggested N2 text: routed readback implies history-level (C4), and the converse fails on a kernel carrier, so no
  step from history-level (C4) to the routed form is proved.
- `review/editorial/RECHECK-r3.md`: ACCEPT WITH NITS. The two raw lines change layout only; the extracted text is
  identical with and without them. It found that `lean_manuscript_census` checks only `(kernel: …)` parentheticals,
  which this paper does not use, and checked the 28 Lean identifiers and Appendix A line numbers directly.

`Introduction-r4.md` (with `CHANGES-r4.md`) applies those nits. It is 16 pages in the default build: §1–§7 end on
p. 12, and the code note, Appendix A and the references take pp. 13–16. There are no overfull boxes and no dropped
glyphs. The title hyphenation on p. 1 is an open owner decision.

Confirmation re-checks of r4: `review/scientific/RECHECK-r4.md` and `review/editorial/RECHECK-r4.md`, both ACCEPT
WITH NITS, all nits optional. Layout options are recorded there for the final layout pass: the 16th page, which a
smaller font in the approved raw group recovers with identical text, and the orphaned last line of §4's lead
sentence. Landing remains gated by the R11/R12 markers (a separate, reviewed manuscript-consistency change), the
§A.42 retention of the Lean axiom-check expected result, the five VERIFY markers, and a direct re-check of the Lean
identifiers at landing, since the census tool does not cover this paper.


## Draft r5: one idea, two consequences

`Introduction-r5.md` is written from design r7 (`../design/OUTLINE-r7.md`; its confirmation re-check
`../design/review/r6/RECHECK-r7.md`: ACCEPT WITH NITS). It follows the owner's narrowing of 2026-10-26:
- quantum emergence is the central thesis;
- the cosmological constant and black-hole information are the two applications, each stated as not a
  demonstrated resolution;
- derivations are cited, not re-derived.

Main text is 12.0 pages in the default build (17 in total with the appendices and references), with no overfull
boxes and no dropped glyphs. `voice_check`, `claims_check` and `duplicate_check` pass, and all 28 Lean identifiers
resolve. `CHANGES-r5.md` maps every paragraph to its outline item and source, and lists the ten places (F1–F10) that
go beyond reviewed text. `scripts/build_r5.py` assembles the draft and asserts that every carried r4 sentence is
verbatim. Independent scientific and editorial reviews are in progress. r4 stays the accepted earlier draft.

## Reviews of r5, and r6

- `review/scientific/REVIEW-r5.md`: ACCEPT WITH CHANGES. Two one-line changes. Both applications keep every
  conditional, and nothing reads as a resolution. The black-hole section matches #936's accepted corrections. F7's
  "with measurement independence kept" is confirmed.
- `review/editorial/REVIEW-r5.md`: ACCEPT WITH CHANGES. It checks definitions before use, symbols in §4–§5, flow and
  length, and confirms the two raw lines change layout only.

`Introduction-r6.md` (with `CHANGES-r6.md`) applies both reviews. Science governs content and the editorial review
governs presentation; each overlap is recorded. `scripts/build_r6.py` generates it from r5 by exact-once replacements.
Main text is 11.73 pages, with no overfull boxes and no dropped glyphs, and the checks pass. Confirmation re-checks of
r6 are in progress.

## Re-checks of r6, and r7

Both confirmation re-checks of r6 (`review/scientific/RECHECK-r6.md`, `review/editorial/RECHECK-r6.md`) returned
ACCEPT WITH NITS. `Introduction-r7.md` applies four of those nits as exact single replacements (`CHANGES-r7.md`):
- an operational-QM qualifier in §1.2;
- the gravitational operator in §4 named generally;
- a comma;
- a term used before its definition.

The confirmation of the four-line diff (`review/scientific/RECHECK-r7.md`) is ACCEPT, with no changes.
`Introduction-r7.md` is the accepted draft. It does not land as `papers/Introduction.md` until these gates clear:
- the black-hole corrections (#936) have merged;
- the §A.42 expected result of the Lean check is retained;
- Weinberg 1989 is read first-hand;
- the VERIFY markers are resolved;
- the owner's layout choices (title hyphenation; the raw group's scope) are made;
- the Lean identifiers are re-checked directly at landing.

## Reference check, and r8

`review/references/FINDINGS.md` is a first-hand check of every VERIFY-marked citation r7 keeps.
- **Supported, with no wording change needed:** six (BBS24, Cal26, EvEMU11, KP14, tH14, Vol06). The Har04 sentence is
  supported through Mon08.
- **Unreachable, VERIFY kept:** four (CT06, Har04 itself, Sha79, Weinberg 1989). The Weinberg landing gate stays
  open.

The source PDFs are third-party and not committed.

`Introduction-r8.md` (with `CHANGES-r8.md`; generated from r7 by `scripts/build_r8.py`) aligns §5 with #936, merged
as `17b830bc`, and follows the owner's direction of 2026-10-26. §5 leads with conservation versus operationally
accessible recovery. The Page-curve calculation is one conditional supporting paragraph, in main's merged wording,
listing its open conditions:
- H-scramble;
- H-decouple;
- Theorem A.8's full-product-space scope, which removes the energy constraint;
- the time-average-only form;
- dependence on the covariant field equations.

All six R11 markers are removed, since every site they named is corrected on main. Main text is 11.73 pages. A
scientific confirmation of r8 is in progress.

`review/scientific/RECHECK-r8.md`: ACCEPT WITH NITS. `Introduction-r9.md` (with `CHANGES-r9.md`) applies the three
nits:
- the Page value is stated up to Theorem A.8's correction term;
- a referent is restored for §6.2 item 4;
- six VERIFY markers are cleared by the first-hand reading.

Three VERIFY markers remain, for unreachable sources. Its confirmation (`review/scientific/RECHECK-r9.md`) is ACCEPT. `Introduction-r9.md` is the accepted draft. Before
it lands as `papers/Introduction.md`:
- Weinberg 1989 must be read first-hand (owner gate);
- the §A.42 expected result of the Lean check must be retained;
- the owner must make the layout choices (title hyphenation; the scope of the raw group);
- the Lean identifiers must be re-checked directly at landing.

The three remaining VERIFY markers (CT06, Har04, Sha79) record sources that are unreachable from this environment.

## r10 and r11: publication readiness

`Introduction-r10.md` (with `CHANGES-r10.md`; generated from r9 by `scripts/build_r10.py`) applies the owner's
publication-readiness decisions of 2026-10-26:
- **Title:** a pandoc title block replaces the `#` heading. The title sets on three lines with no hyphen, so the
  title-hyphenation decision is resolved.
- **Length:** five trims of repetition, transitions and nonessential explanation (T1–T5), each listed with its old
  and new text. They keep the main text within 12 pages.
- **Weinberg 1989:** the owner gate becomes a VERIFY marker stating that the source is not read first-hand.

Its re-check, `review/scientific/RECHECK-r10.md`, is ACCEPT WITH NITS.

`Introduction-r11.md` (with `CHANGES-r11.md`; generated from r10 by `scripts/build_r11.py`) applies those nits:
- **T3** is reverted.
- **T4** is kept, and its reversal of the r2 editorial fix (F10) is recorded.
- **The Weinberg marker** reads "only after the source is read and checked". On the owner's decision of 2026-10-26
  ("Keep as landing gate") it also states that it gates landing: the paper does not land until Weinberg 1989 is read
  first-hand and checked.

It also states the Lean evidence:
- The §A.42 expected result of the Lean check is retained at `papers/introduction_repro/` (main `17b830bc`).
- The Conventions and the code note cite that commit, the toolchain (Lean 4.33.0, Mathlib v4.33.0), the build and
  release-gate recipe, and the retained result.
- Both §A.42 OWNER markers are removed.
- One commit is used throughout: the Conventions, the code note, Appendix A's line numbers and the Corpus entry all
  name `17b830bc`. Every corpus pointer the paper cites was checked there, and none moved (`CHANGES-r11.md`).

r11 measures 17 pages, 11.82 of them main text, with no overfull boxes and no dropped glyphs.

**Current markers:**
- No OWNER markers.
- Four VERIFY markers: CT06, Har04, Sha79 and Weinberg 1989. Each records a source that has not been read
  first-hand. The Weinberg marker is an open landing gate; the other three do not gate landing.

**Owner decision (amaybaum, 2026-10-26), on the "decision 2" wording:** "Accept 'machine-checked' with its existing
restricted definition. It must refer only to statements actually formalized and checked, not to the entire physical
theory or its empirical interpretation." r11 defines it in the Conventions paragraph as checked in Lean 4/Mathlib at
`17b830bc` by the stated recipe, for the declarations in Appendix A; the final scientific review checks every use
against that scope.

**Before the draft lands as `papers/Introduction.md`:**
- **open landing gate (owner, 2026-10-26):** a copy of Weinberg 1989 must be supplied and read first-hand and
  checked;
- the final scientific review;
- the direct check of the Lean identifiers at the landing commit.
- `papers/introduction_repro/`, the paper's expected Lean result, reaches `main` no later than the paper (§A.42
  item 2).

`review/scientific/RECHECK-r11.md` is the independent re-check of r11 and of `papers/introduction_repro/`: ACCEPT WITH
NITS for both. The package's two required fixes are applied: the recipe's comparison names the file by its path from
the repository root, and the cache statement says that `lake exe cache get` still fetches Mathlib's prebuilt files.
The recipe also states its prerequisites. The expected result no longer lists line positions in the CI log
(§A.42 item 4), and its comparison still holds against the job's extracted text with the sources at `17b830bc`.

## Final scientific review of r11, and r12

`review/scientific/FINAL-REVIEW-r11.md` is the final scientific review of r11. Its verdict is REVISE (minimal), with
two blocking findings and eight nits:
- **B1:** Theorem 4 was stated without the structural hypotheses of the kernel's `FiniteOperationalTheory`.
- **B2:** the corpus pin `17b830bc` predates #937, so at that commit [GR] contradicts §4 on Λ.

`Introduction-r12.md` (with `CHANGES-r12.md`; generated from r11 by `scripts/build_r12.py`) applies all ten findings:
- **B1:** Theorem 4's setup now lists every field of the structure, checked against `OperationalAssembly.lean:594`.
- **B2:** the corpus is repinned to `main` `c967d6a9`. Every cited pointer was checked there, and none moved. The Lean
  pins stay at `17b830bc`, because the Lean tree, `tools/`, `papers/Main.md` and the black-hole programme are
  identical between the two commits.
- **N1–N8:** applied, including [HKLP24], which was read first-hand, for the imported unboundedness, and the release
  archive's exclusion of the black-hole computations.

One page-budget trim, §6.1's repeated closing sentence, keeps the main text at 11.90 pages. Like r11, r12 has no
overfull boxes and no dropped glyphs.

**Before the draft lands as `papers/Introduction.md`:**
- **open landing gate (owner, 2026-10-26):** Weinberg 1989 must be supplied and read first-hand and checked;
- the confirmation of r12 against the final review;
- the direct check of the Lean identifiers at the landing commit;
- `papers/introduction_repro/` reaches `main` no later than the paper.
