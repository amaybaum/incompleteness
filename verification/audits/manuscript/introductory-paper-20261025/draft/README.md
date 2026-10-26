# Introduction paper: working draft (WIP, unreviewed)

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

A revision applying both reviews is in preparation.

