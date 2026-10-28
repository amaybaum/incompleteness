# Independent provenance/publication re-review — c0844bd

Remote candidate: `c0844bd287a3bcc04b75f79db140af1c75e70d90`.
Reviewed local content-equivalent commit: `4db4af644428edab4d32985e4e2176842f963f40`.
Exact tree of both: `e903fec01889defd8111706b499d8c34f9970850`.

**Verdict: ACCEPT for scoped provenance, preservation and publication consistency.** No blocker was found within this scope. This is not scientific release acceptance or merge approval. The parallel scientific review's remaining propagation findings prevent release of this snapshot and require another reviewed candidate.

## Independently verified remote identity and landing target

The GitHub raw Git commit API identifies c0844bd with exactly the reviewed tree and one parent, `20ca05fe9e7e460de29e08f7a21029042fa45b12`. The remote is therefore a forward source correction rather than a merge of #992, #980 or #981. The #992 Chapter 3 correction is byte-identical to its a2be source; its separate provenance survives.

The GitHub PR API confirms #982 is open, draft, unmerged and now targets main at `0d917665d32287e5d0ce649012175f2c7bf75b09`. Its current synthetic PR merge is `81b902fe2357b05b5298d70b00e2efc28636ddc3`, with that main SHA and c0844bd as ordered parents. The raw Git API confirms the synthetic merge tree is exactly e903fec. Thus the current ordinary PR checkout content is the independently reviewed source tree.

Both workflow runs 40754356592 and 40754357095 identify c0844bd, PR #982 and main in their structured metadata. At inspection the former was in progress and the latter queued; neither had a conclusion. No passed CI, compiler or release-gate outcome is claimed here.

## Source identity and preservation

- All 83 candidate-input manifest SHA256 values match the reviewed files.
- Relative to both the prior #982 head 20ca05fe and the initial combined #992 snapshot a2be1e45, all 134 canonical entries remain and every kernel grade is unchanged. The sole canonical fingerprint change is SM:T-10, from c1774f68700254d6 to 6f0103db17cb9dc1. Its GAP grade remains; the changed clause scopes its hypercharge consequence to the actual fixed-family classification rather than removing the three-sector result.
- All ten specifically protected recovered endpoints retain fingerprints and grades: SM:T-3, SM:P-14a, SM:T-15, SM:P-15a; Substratum:T-23, T-24, P-24.2, P-24.3, P-24.4 and P-24.5. The finite-carrier Lean P24.2 remains K3, while the written predictive/record-fibre results remain GAP without new Lean certification.
- All inspected protected paths are unchanged relative to 20ca05fe: complete Lean and Mathlib source directories, Lean/manuscript registry, infrastructure and receipts, SC44-lemma-24-1 and SC45-generator-soundness tracks. There is no workflow change in the reconciliation delta.
- The earlier 49-file source-review manifest is preserved unchanged as historical evidence. Fourteen current files differ from that snapshot, as expected from the forward source correction; the new PR description and audit explicitly avoid claiming the old 49 hashes still match.

## Publications and mirrors

For SM, Substratum, Explainer, Methodology, Juno and the book, every recorded Markdown, TeX and PDF hash matches the committed artifact. All six source stamps match; their page counts and exact PyMuPDF stripped-character medians reproduce the new publication-check record. Page counts are respectively 147, 53, 68, 47, 22 and 548.

All twelve paper TeX source stamps match their own current Markdown sources. All 28 book content files, including bibliography, have zero missing nonblank lines when checked in order against FULL; the maintained mirror checker independently reports zero missing lines.

The publication record lists 18 selected rendered pages. All 19 query phrases occur on their recorded PDF pages, and a fresh automated scan of all six PDFs finds zero word boxes outside page bounds under the recorded one-point tolerance. This is publication/text/layout consistency; I did not independently repeat the author's visual examination of rendered pages or its canonical builds.

The old #992 publication-check remains a historical 547-page snapshot, and the new 548-page record correctly applies to this new tree. Its changed hashes do not invalidate the earlier snapshot's evidence.

## New operator controls and evidence boundary

The exact integer/rational control script was replayed once normally and once with Python optimization. Both exited zero, were byte-identical, and exactly matched the retained JSON. The operator products, exceptional/standard anomaly coefficients and finite sanity checks therefore reproduce.

The infinite-ancilla extension is explicitly written operator mathematics in Substratum:288–290. The unchanged Lean certificate remains finite-carrier; neither the source nor the new audit represents the finite matrix calculation as a universal infinite-dimensional kernel proof. The script's swap-fibre/dimension checks are small sanity examples, not substitutes for the existing general written proofs.

## Limits and outstanding gates

The source/provenance observations above survive only while the exact tree is unchanged. The scientific review's residual B1–B3 sites require further source and publication updates, followed by fresh manifests and scoped re-review. The full-history legacy/V3 gates and complete compiler/release suite remain CI obligations because the local checkout is shallow. The current main-targeted synthetic merge tree matches this candidate, but green CI and explicit owner approval are still required before any eventual merge.
