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
glyphs. The title hyphenation on p. 1 is an open owner decision. Confirmation re-checks of r4 are in progress.

