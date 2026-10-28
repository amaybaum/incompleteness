# Independent provenance and publication review — initial combined source

Reviewed immutable commit: `a2be1e4573662d1331f2560ea06c2d8ed10bcd73`.
Tree: `d8e95e610452fe018851fe14553c97a703c7db5b`.
Parent: `20ca05fe9e7e460de29e08f7a21029042fa45b12`.

Verdict: **ACCEPT for scoped provenance, preservation and publication-consistency review.** No blocker was found within this scope. This verdict does not supersede the separate scientific review, certify the unexecuted full-history release gates, or authorize merge. A later changed candidate requires its own manifest and review.

## Preservation and provenance

The combined commit is a single-parent child of the held #982 checkpoint. Its six-file delta consists only of Chapter 3, FULL Markdown/TeX/PDF, and two new #992 audit files. There are no Lean, ledger, registry, frozen record, receipt or control-plane changes in that delta. Comparing current ledger with `f39b8d360bdba4bc460992fc770b9bd13c286ced` finds all 133 earlier entries, identical fingerprints and identical kernel grades; only `SUBSTRATUM:P-24.5` is added. Comparing #992 with its direct parent finds the complete ledger and census byte-identical.

Current retained grades and scope:

- P24.2 remains K3 with both directional Lean witnesses and full block-word/spanning premises. The named witnesses exist in the committed WordTraceSufficiency and SemigroupTransfer modules. This was a source check, not a fresh compiler run.
- T23 and T24 remain GAP. P24.3–P24.5 remain GAP with checks=[] and written-proof/finite-control support explicitly distinguished from kernel proof.
- The original SC-44/45 record directories survive. The #992 commit neither merges nor rewrites #980/#981. Their review branches are separate provenance; the integrated source remains the intended eventual landing vehicle.
- The 49-file hidden-state source-review manifest matches 47 current files. The two intentional differences are Chapter 3 and FULL Markdown, exactly the #992 source correction. Its historical acceptance remains evidence for its original snapshot. Do not claim all 49 files remain unchanged at this combined head; record the two-file delta and new independent review separately.
- The historical publication/review records are snapshot-scoped. Earlier counts and pending-CI statements in preserved chronological sections do not constitute current release acceptance.

## Independently executed bounded checks

1. The SC44/45 lexical preview guard passes with zero issues. It remains lexical, not a scientific theorem checker.
2. An isolated normal-Python replay of the exact committed SC45 checker exits 0 and matches the retained structured result: 5,808 hidden-only coherent cases; 1,416 fibre-dependent population cases; 160 decoupled ancillary cases; 16 preserving/8 violating full-state relabellings; six detected countercontrols. This independent replay is finite evidence, not a universal theorem. Optimized replay is wired into ordinary CI; I did not repeat a local mutation campaign.
3. All 28 book content files including bibliography have their nonblank lines in FULL in order; the maintained mirror checker also reports zero missing lines.
4. #992 publication-check MD/TeX/PDF hashes match the committed bytes. The book TeX source stamp matches FULL Markdown. Every one of the twelve committed paper TeX source stamps matches its own Markdown source.
5. The committed book PDF has 547 pages, contains the new ancillary wording, and lacks the old “below a certain depth” phrase. Its recorded median 2,976 is exactly reproduced by median(len(page.get_text().strip())) using PyMuPDF. Poppler pdftotext -layout gives 3,053 because its spacing convention differs; this is not a contradictory measurement. Future evidence should state its extractor convention.
6. No frozen-record, receipt, seal, certificate, legacy-record-manifest or AGENTS.md difference was found between current main snapshot `0d917665d32287e5d0ce649012175f2c7bf75b09` and this candidate under those inspected paths.

## Publication and landing requirements

All six workflow files were inspected. For a fast-forward update of the existing `corpus/sc44-sc45-reconciliation-preview` ref from 20ca05f to this candidate, the changed paths match none of the path-filtered push research workflows. `verify.yml` has unrestricted pull_request and push only on main; ordinary PR synchronization therefore starts verification. Evidence replay and PE-01 are dispatch-only. No governed launch is implied by this push. A newly created branch has different GitHub push diff semantics and should be assessed separately.

PR #982 is presently based on #980's branch `corpus/sc44-lemma241-core`, not main. Merging that PR without retargeting would update #980's branch rather than main. Before release approval, retarget #982 to corrected main (or prepare a separately reviewed equivalent landing), inspect its actual main diff including all inherited SC-44 changes, and rerun the exact resulting CI/review. Keep #980/#981 as provenance records; closing them without merge is appropriate only after an approved integrated landing.

This checkout is shallow and backed by a shared object store. Full-history/isolated recovery gates, complete Lean/Mathlib compilation and release-suite execution belong in CI. This review did not infer their outcomes from old receipts, text scans, or missing local history.

## Review scope limit

This report checks preservation, evidence identities, replay wiring, publication consistency and landing mechanics. The parallel scientific reviewer is responsible for residual unsupported gauge/branch/regress claims and proof adequacy. Their concrete findings take precedence over this scoped acceptance for release readiness.
