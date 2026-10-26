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

A confirmation of the four-line diff is in progress.
