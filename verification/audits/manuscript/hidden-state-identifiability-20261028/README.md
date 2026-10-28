# Hidden-state identification: scoped correction and recovery

This increment follows published checkpoint
`f39b8d360bdba4bc460992fc770b9bd13c286ced`, whose Git tree is exactly the tree of
local recovery checkpoint `efa84ad90e3663fa2f5fdb036437f52a6b95fc54`.
It remains work in progress on draft PR #982. It is not publication acceptance,
a native-round F/E designation, or merge approval.

## Mathematical result and manuscript correction

A proper instantaneous readout does not establish permanent hidden-state
uncertainty. The reversible swap `(v,h) -> (h,v)` identifies all four initial
states from two retained visible readings, while its uniform visible law still
has one bit of conditional memory. A cyclic register generalizes this example
to an arbitrarily large hidden capacity, with zero posterior hidden uncertainty
after the identifying history has been retained.

New Substratum Proposition 24.5 gives the exact known-model criterion: a quantity
is identified by a positive-probability nonempty record precisely when it is
constant on that record's preparation-supported fibre. Under its permutation
and product-readout hypotheses, initial-state, current-state and current-hidden
identification share the singleton criterion. The whole-carrier bound
`max(1, |Omega|-1)` resolves passive future-trace classes; it is not a bound in
terms of a possibly non-invariant preparation support. Permanent ambiguity of
every possible passive record requires every nonempty restricted future class
to have at least two elements.

The written proof and independent controls support this proposition. Its ledger
status is **GAP**, with no Lean check claimed. All 133 pre-existing canonical
statement bodies and fingerprints are preserved. Memory capacity, predictive
memory, posterior opacity, and unknown-model predictive reconstruction remain
distinct claims. Physical preparation, record retention, interventions, coherent
instruments, physical model selection and a complete gauge relation are not
supplied by this theorem.

The corrected dependencies include Main's opening, Substratum, Explainer,
Structure, Computation, the corresponding book chapters, the glossary and FULL
mirror. Philosophical and AI summaries now respect the same record/interface
qualification; finite non-identifiability is not identified with Turing
undecidability.

## Independent review

`source-review.json` and `source-review.txt` accept the scoped corrected
candidate-v2, after the retained initial findings were addressed.
`source-review-manifest.json` pins its 49 reviewed scientific-source/control
files; SHA256:

`801b58fee69cf387e6495a6a44f5c509c3d61ac8342008c837ef818abfcb9a9d`.

Every pinned file was rechecked against the integrated working tree before
commit. This review excludes publication builds, CI, a Lean proof of P24.5 and
broader physical correctness. The separate Medicine readout-disturbance issue
noted in the review remains outside this correction.

## Executable evidence and CI compatibility

The maintained `independent_controls.py` checks 39,546 explicit predicates,
including 442 small permutation/readout models and 6,122 preparation supports.
It is now called by the existing architecture gate, alongside five fail-closed
manuscript invariants. `supplemental_controls.py` independently checks 6,076
boundary predicates. Normal and optimized executions agreed in the independent
review. The retained JSON outputs are finite controls, not universal kernel
proofs.

The published baseline's normal PR CI run `40689922980` passed Lean kernel and
Mathlib jobs but failed two validation jobs. This increment repairs both without
editing frozen round controls:

- Stinespring manuscript lint now checks the corrected finite-isometry scope,
  off-reference and non-minimal freedoms, and Proposition 24.2's full word-trace
  and spanning premises. It no longer requires the refuted semigroup-transfer
  assertion. The focused probe passes.
- The new SM3 census object is placed immediately before the historical final
  KTOKEN object, satisfying a frozen synthetic fixture's last-entry assumption.
  All 112 raw family objects, other metadata and the prior order excluding the
  new SM3 addition are unchanged. The unchanged frozen end-to-end mutation
  branch passes all 26 cases. See `registry-order-repair-receipt.json`.

These local repairs do not establish the outcome of the next normal PR CI run.
No special workflow was dispatched and no F/E attestation is claimed.

## Publication and bounded verification

All six affected publications were regenerated through the canonical `build.sh`:
Main (96 pages), Computation (22), Explainer (68), Structure (93), Substratum (53)
and the book (547). No missing glyphs were reported. The final TeX source stamps,
PDF hashes, page/text statistics and selected-page rendering results are in
`publication-statistics.json`. All 29 selected rendered pages were visually
inspected; no out-of-page word boxes were found.

`local-checks.json` records architecture (264 invariants, zero violations),
coverage (134 canonical statements), Python static compilation, tool self-tests
and the focused compatibility checks. The V3 corpus has 137 expected outcomes;
three historical vectors are explicitly **UNDECIDABLE** in the shallow checkout.
No local full-history, full Lean/Mathlib or release-suite result is claimed;
those remain CI work under AGENTS A.40. The independent review found all 28 book
content files' ordered nonblank lines in FULL.

Bounded reproduction commands, from the repository root:

```sh
python -I -B verification/audits/manuscript/hidden-state-identifiability-20261028/independent_controls.py
python -I -B verification/audits/manuscript/hidden-state-identifiability-20261028/supplemental_controls.py
python papers/oi_lattice_code/architecture_check.py
python tools/coverage_check.py
python verification/lean/stinespring_scope_probe.py
```

`publication_qa.py --root REPO --output SCRATCH_DIRECTORY` reproduces the
publication statistics and selected-page renders against the current PDFs.

## Follow-up: audit-census reconciliation after 344d066

At the published hidden-state head `344d066`, normal PR CI confirmed the Lean
kernel, Mathlib and KTOKEN jobs, and the Stinespring scope probe passed. Core B
then stopped at two census drifts. Both scientific qualifications were retained:
Structure §9 now has two qualified non-minimal-realization passages, and SM §8.3
uses a selected-family qualification instead of the book's older literal wording.

The census retains all 34 original pattern strings, records the second reviewed
Structure hit, and adds an exact SM requirement covering both the observer/branch
distinction and the conditional physical generation/chirality premises. The
existing book qualification remains required. The probe passes over all 42 scoped
manuscripts; four controlled mutations (an extra occurrence, either missing SM
qualification, and a missing book qualification) are each rejected. See
`audit-census-repair.json`. All 49 previously reviewed scientific-source hashes
still match; no manuscript, theorem, TeX or PDF changes are part of this repair.
The next normal PR CI result remains a separate gate.

## Follow-up: current publication guards after f420020

CI confirmed the census repair, then reached R7-AUDB and R7-A6P. Audit B still
required SM's superseded literal. Its replacement now requires the complete
selected-family and physical-premise qualification already guarded by the census;
all its other GR, book, C2/C4 and calibration checks are retained.

The A6 publication guard had five obsolete positive text contracts and a mutation
whose search text was absent. Its current contracts now preserve the recovered
stabilizer/quotient/charged-action distinctions, the link transformation law and
the scalar/commuting condition for literal fixed-link endpoint equality. The live
state-dependent overclaim mutation is rejected while its positive contracts remain
intact. All other A6 predicates, original mutation protections, frozen control
plane, legacy records, census prefix and historical pins are preserved.

Both isolated guard sections pass. Six Audit B qualification-removal mutations
are rejected; all 22 original A6 recorded conjunctions pass, and two extra
qualification-deletion controls are rejected. All 49 prior scientific-source
hashes still match. See `publication-guards-repair.json`. This maintains the
mutable downstream content guard; it does not amend or re-execute the old native
round, change its chronology, or claim historical execution acceptance. No
manuscript, theorem, Lean, TeX or PDF changed, and full next-head CI remains
required.
