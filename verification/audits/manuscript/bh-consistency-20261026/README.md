# Black-hole statements in the book and GR: consistency audit and correction

The records behind the manuscript-consistency change that corrects the book's and GR's black-hole statements to the
strength of their support. The change was made separately from the Introduction paper (#918), as the owner directed on
2026-10-26.

- `FINDINGS.md`: the read-only investigation of each site against its support at `main` `687e885b`.
- `REVIEW.md`: its independent review, which confirmed the nine errors, reclassified GR Theorem A.9, found a gap in
  Theorem A.7's proof, and listed missed sites.
- `CHANGE-NOTE.md`: the change itself, site by site, with the defaults applied for the owner's open decisions, build
  and check results, and re-grep counts.
- `DIFF-REVIEW.md`: the independent review of the diff. It also settles by exact algebra that Theorem A.8's value
  holds only when the energy shell is the full product space; that error is left to a separate change.
- `probes/`: the investigator's and reviewer's exact checks (evaporation timescales, Page's mean entropy, the Page-time
  fraction for a mass-dependent emission coefficient), with outputs where they were kept.

Paths written `S/…` refer to the session's scratch directory, which is not part of the repository.
