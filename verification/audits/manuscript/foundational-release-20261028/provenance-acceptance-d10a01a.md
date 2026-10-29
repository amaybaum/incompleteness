# Independent incremental provenance/publication review — d10a01a

Remote candidate: `d10a01a59e55684cf7fb09e519c3bc65798526d0`.
Local content-equivalent commit: `d6f8961a6489ef3872c1033d0cd73f2911234ec5`.
Exact tree: `d8ab8b94a1eec79dee14b1a4951af7331a99b742`.
Prior reviewed source: remote c0844bd / local 4db4af64, tree e903fec.

**Verdict: ACCEPT for the incremental provenance, preservation and publication scope. No blocker found.** This is not a merge authorization, compiler attestation or broad scientific acceptance. The scientific reviewer separately evaluates the five residual source sites and their R1–R4 closure.

## Remote identity and review scope

The raw Git commit API independently confirms the candidate's exact SHA/tree and sole parent c0844bd287a3bcc04b75f79db140af1c75e70d90. The PR API confirms #982 still targets main at 0d917665d32287e5d0ce649012175f2c7bf75b09, remains draft, and is unmerged. Its synthetic merge c8c0b6eb88c0e7147ae1ba5fc5f55e768a702724 has ordered parents main and d10a01a and exactly the reviewed d8ab8b94 tree. Ordinary PR checkout therefore uses this source content.

The source increment contains only the two named Explainer paragraphs, two named Methodology paragraphs and Appendix B's B.6 summary with the identical FULL change. The other delta consists of their regenerated TeX/PDF and current audit/review/manifest updates. There is no added theorem, changed proof grade or altered Lean proof.

## Preservation checks

- All 87 current candidate-input SHA256 values match.
- The full coverage ledger is byte-identical to c0844bd: all 134 canonical statements, their fingerprints, grades and evidence entries survive unchanged.
- Complete Lean/Mathlib directories, census registry, infrastructure, receipts, SC44/SC45 and other original corpus-audit tracks, the #992 source audit, hidden-state audit, and workflow files are unchanged from c0844bd.
- Initial scientific REVISE and provenance reports are unchanged. The retained c0844bd provenance Markdown and JSON are byte-identical to my original review files; the separate c084 scientific report remains preserved.
- The exact operator controls/results and preservation-check record are unchanged. The prior independent normal/optimized replay remains evidence for precisely these same bytes; I did not repeat that campaign.

## Publication consistency

All six publication records still match their current Markdown, TeX and PDF hashes, TeX source stamps, page counts and stated PyMuPDF median conventions. For the changed publications the page counts are Explainer 68, Methodology 47 and book 548.

The three changed PDFs have zero detected out-of-page word boxes under the recorded one-point tolerance. Their five recorded source-query phrases occur on the recorded pages: Explainer 53–54, Methodology 41–42 and book 467. I verified text/page/layout consistency; the author's selected-page visual inspection and canonical rebuild are separate provenance.

All 28 book content files, including bibliography, have zero missing nonblank lines when matched in order against FULL. The maintained mirror checker also passes. The Appendix B/FULL correction therefore propagates exactly.

## Remaining release conditions

The fresh ordinary PR verify run 40756343045 was queued, with no conclusion, when inspected. Passing c0844bd runs remain evidence for that earlier source, not automatic verification of d10a01a. The final scientific verdict, actual candidate CI/compiler/release conclusions, and explicit owner approval of the resulting SHA remain required before merge. The shallow local repository still cannot substitute for CI's full-history checks.
