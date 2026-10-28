# Foundational source reconciliation: #982 and #992

This candidate applies #992's ancillary/regress correction to #982's source
checkpoint `20ca05fe9e7e460de29e08f7a21029042fa45b12`, then repairs the
concrete propagation findings in `initial-scientific-review.md`. The independent
review of the initial combined source accepted #992's narrow correction and
requested the further repairs below. `initial-provenance-review.md` records its
separate preservation/publication verdict. These initial verdicts concern
`a2be1e4573662d1331f2560ea06c2d8ed10bcd73`, not acceptance of a later tree.

## Mathematical scope and preservation

- Keep the exact six-link decomposition, conditional generic condensate
  stabilizer, constructive correlated central quotient and faithful selected
  charged-family image distinct. The physical action, light spectrum and
  global bundle/line data retain their stated premises.
- Preserve SM Theorem 15's complete fixed-family anomaly classification,
  including the exceptional neutral-Q branch, compact-charge strengthening,
  and separate numerical normalization. Align dependent summaries and the
  book's B.5.1 statement with the family and normalization its proof uses.
- Align Methodology's summaries with the open physical selector/classification,
  conditional operational identifiability result and known-model record-fibre
  theorem. Proper embedding alone supplies no universal state-opacity or
  whole-system computational-size theorem.
- Preserve Theorem 23, Theorem 24, Proposition 24.2's full word-trace/spanning
  premises and both Lean directions, and written Propositions 24.3–24.5.
  The new balanced-word operator argument explicitly extends Pair C's
  restricted obstruction to nonempty infinite ancillary spaces. That extension
  is written mathematics; the existing Lean certificate remains finite-carrier.

`preservation-check.json` records all 134 canonical entries and unchanged proof
grades. The only changed canonical fingerprint is SM Theorem 10: its final
hypercharge sentence now inherits Theorem 15's actual family/branch premises.
Its three-degenerate-sector result and GAP grade are retained. No Lean module,
frozen native record, receipt, registry or SC-44/45 provenance record is edited.
The earlier 49-file source-review manifest remains historical; the new source
is pinned separately in `candidate-inputs.json`.

## Reproduction and publications

The independent exact operator/anomaly/swap controls use explicit failure guards:

```sh
python -I -B verification/audits/manuscript/foundational-release-20261028/pairC-and-scope-controls.py
python -I -O -B verification/audits/manuscript/foundational-release-20261028/pairC-and-scope-controls.py
```

Both outputs must equal `pairC-and-scope-results.json`. These finite controls
supplement the written proofs and do not create kernel certificates.

Canonical regeneration uses `sh ./build.sh SM Substratum Explainer Methodology Juno`
and `sh ./build.sh --book`. `publication-check.json` records source/TeX/PDF
hashes, matching source stamps, page counts, the explicit text-density extractor,
selected rendered pages and page-bound checks. Final builds report zero missing
glyphs. The initial failed Substratum build exposed an unsupported prime glyph;
the source now uses ordinary prose for the primed example and was rebuilt.

Coverage, Lean/manuscript census, architecture and whitespace checks pass locally.
The V3 self-test passes; its corpus has 137 expected outcomes and three historical
vectors undecidable in the shallow checkout. The legacy-record commit check is
also undecidable locally. Full-history, compiler and release-suite outcomes must
come from the actual candidate's CI, not these bounded checks or earlier receipts.

The intended landing is #982 against main, with #980/#981 preserved as separate
provenance records. Final independent review and exact-head CI remain separate
gates. No merge, special workflow dispatch or native F/E designation is authorized.

## Focused follow-up after c0844bd

The second scientific review accepted the main repairs and requested five residual
summary corrections in Explainer, Methodology and the Appendix B overview.
`scientific-review-c0844bd.md` preserves that REVISE verdict;
`provenance-review-c0844bd.md` preserves the separate scoped provenance ACCEPT.
The follow-up aligns those passages with representation availability, selected
family/action inputs, scalar coupling versus condensate, and data-restricted
identification. No canonical theorem, grade, Lean source or recovered proof changes.
Explainer, Methodology and the book were regenerated with zero missing glyphs;
the current publication identities are recorded above. Final acceptance and CI
still apply to the resulting head.

## Independent acceptance of the reconciled scientific source

Both independent follow-up reviews accept source head
`d10a01a59e55684cf7fb09e519c3bc65798526d0`, tree
`d8ab8b94a1eec79dee14b1a4951af7331a99b742`, within their stated scopes.
The scientific review closes R1–R4 and preserves the strongest results; the
provenance/publication review verifies all 87 input identities, the 134 canonical
entries, protected source and publication/mirror consistency. Their reports are
retained as `scientific-acceptance-d10a01a.*` and
`provenance-acceptance-d10a01a.*`. These are source/provenance verdicts, not
physical-correctness, compiler, full-history or merge attestations.

The following record-only increment adds those verdicts and this explanation;
no manuscript, publication, theorem, grade, Lean source, control or existing
review report changes. The input manifest refreshes only this README digest;
its scientific and publication inputs remain exactly those accepted at d10a01a.
The actual landing head still requires CI and explicit owner approval.

## Classical attribution follow-up to 20f818f

The attribution-only follow-up adds Specht–Wiegmann attribution at Proposition
24.2, and the original Schützenberger/Carlyle–Paz/Fliess lineage at Proposition
24.3 alongside its existing Berstel–Reutenauer and Thon–Jaeger references.
The proposition statements and complete proof blocks are byte-identical to
20f818f. The spanning premise and all Lean witnesses remain as stated; no
no-spanning theorem is newly claimed as kernel-certified.

Substratum alone is regenerated through the canonical build (54 pages, zero
missing glyphs). `attribution-check.json` records unchanged theorem/proof hashes
and the current publication checks. The input manifest refreshes the changed
Substratum artifacts and audit records. Earlier acceptance reports remain
scoped to their pinned snapshots; this citation edit does not broaden their
scientific scope. Fresh candidate CI and exact-SHA owner approval are required.
