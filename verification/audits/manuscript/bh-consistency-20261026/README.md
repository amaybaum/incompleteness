# Black-hole statements in the book and GR: consistency audit and correction

The records behind the manuscript-consistency change that corrects the book's and GR's black-hole statements to the
strength of their support. The change was made separately from the Introduction paper (#918), as the owner directed on
2026-10-26.

- `FINDINGS.md`: the read-only investigation of each site against its support at `main` `687e885b`.
- `REVIEW.md`: its independent review, which confirmed the nine errors, reclassified GR Theorem A.9, found a gap in
  Theorem A.7's proof, and listed missed sites.
- `CHANGE-NOTE.md`: the change itself, site by site, with the defaults applied for the owner's open decisions, build
  and check results, and re-grep counts.
- `DIFF-REVIEW.md`: the independent review of the diff. It also shows, by exact algebra, that Theorem A.8's value
  does not hold in general when the energy shell is a proper subspace; it holds when the shell is the full product
  space. On the owner's decision of 2026-10-26 the change restricts A.8 to the full product space and states the proper-shell version as open (`CHANGE-NOTE.md` §7).
- `DIFF-RECHECK.md`: the confirmation re-check of the applied review (ACCEPT WITH NITS; the nits are in these
  records).
- `A8-REVIEW.md`: the independent review of the Theorem A.8 restriction (BLOCK, narrowly, on the physical interpretation; the three fixes it gives are applied, see `CHANGE-NOTE.md` §8).
- `A8-RECHECK.md`: the verbatim check of those fixes (ACCEPT); the owner's three questions on the restriction are all answered yes.
- `probes/`: the investigator's and reviewer's exact checks (evaporation timescales, Page's mean entropy, the Page-time
  fraction for a mass-dependent emission coefficient), with outputs where they were kept.

Relative paths such as `paper/r11/…`, `r11/rev/…` and `bhfix/…` refer to the session's scratch directory, which is not
part of the repository; the reviewer's `r11/rev/{evap,page,r12}.py` are committed as
`probes/review-{evap,page,r12}.py`.
