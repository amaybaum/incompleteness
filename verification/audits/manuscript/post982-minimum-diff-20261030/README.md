# Post-#982 manuscript minimum-diff audit

**Status: ACTIVE / PARTIAL, research-only.** This is a measured comparison and
a bounded, evidence-first review of surviving source edits, not certification
that every hunk is minimal. It changes no scientific statement or manuscript.
The minimum-change standard is `AGENTS.md` §A.25. The earlier per-hunk
minimization is `verification/audits/manuscript/pr982-minimization-20261028/`.

## Immutable comparison and measured result (2026-10-30)

- **Before PR #982:** `0d917665d32287e5d0ce649012175f2c7bf75b09`.
- **#982 merged:** `dffe1945989f60632c75b2b3e2e96afad2af8509`.
- **#994 minimization merged:** `986dab5aabbbd419467109e0b9604c8f19901688`.
- **Latest-main audit snapshot / this branch's base:** `6e219231483bb404c0d055ab9a447278422a597e`.

Using GitHub's `compare_commits` per-file line statistics, with
`papers/*.md` and `book/*.md` at the top level (including FULL.md,
excluding nested auxiliary text), the following are **net source diffs**
against the pre-#982 baseline. They are not gross historical edit counts:

| Comparison | Commits after baseline | All changed files | Source + | Source − |
| --- | ---: | ---: | ---: | ---: |
| Pre-#982 → #982 merge | 81 | 202 | 1,116 | 1,037 |
| Pre-#982 → post-#994 | 87 | 201 | 497 | 424 |
| Post-#994 → current main | 57 | 105 | 449 | 416 |
| Pre-#982 → current main | 144 | 263 | 711 | 673 |

The last row is a **net** tree diff; it need not equal the sum of intermediate
diffs, because edits were reverted, changed again or overlapped. Generated
TeX/PDF and audits dominate the all-files count and must not be mistaken for
independent manuscript-content changes. A smaller diff is evidence that the
large #982 change was reduced; it is **not**, alone, proof of minimality.

Reproduction:
- [original #982 merge comparison](https://github.com/amaybaum/incompleteness/compare/0d917665d32287e5d0ce649012175f2c7bf75b09...dffe1945989f60632c75b2b3e2e96afad2af8509)
- [post-#994 comparison](https://github.com/amaybaum/incompleteness/compare/0d917665d32287e5d0ce649012175f2c7bf75b09...986dab5aabbbd419467109e0b9604c8f19901688)
- [after-#994 diff](https://github.com/amaybaum/incompleteness/compare/986dab5aabbbd419467109e0b9604c8f19901688...6e219231483bb404c0d055ab9a447278422a597e)
- [net source comparison](https://github.com/amaybaum/incompleteness/compare/0d917665d32287e5d0ce649012175f2c7bf75b09...6e219231483bb404c0d055ab9a447278422a597e)

## Existing audited changes, and the precise evidentiary limits

The #994 retained `reports/{substratum,structure,sm,companions,book}.md`
contain old/minimal text classifications and findings. This audit **reuses
those reports; it does not reclassify their already accepted corrections by
editorial preference**. Representative findings with concrete proof anchors:

| Correction cluster | Why prior wording needed a fix | Support and surviving constraint | Status here |
| --- | --- | --- | --- |
| Theorem 24 / Lemma 24.1 | Claimed exhaustive fixed-interface equivalence without valid semigroup transfer | `ST3_pairC` counterexample; only proved families/invariances, completeness open (#994, Substratum §4) | Retain correction |
| Hidden-state identifiability | Claimed hidden state intrinsically unrecoverable | Swap example and record-fibre criterion P24.5; distinguish causally unreachable from recoverable (#994) | Retain correction |
| SM chirality | Unrestricted iff was too broad | `scalar_center_chiral_iff` in its named opposite-parity/no-2-torsion scope (#994) | Retain correction |
| Dimension / graph generality | Gromov-based claim about all bounded-degree graphs was unsupported | A4 supplies finite periodic lattice/rank; empirical filters select d=3 only under their continuum premises (#995) | Retain correction |
| Gauge and hypercharge | Commutant, full physical-carrier derivation and uniqueness overclaimed | H-link/H-cust; specified matter action; nonzero-quark-doublet-hypercharge branch (#994/#995) | Retain correction |
| Regress and decoupled ancilla | All-interface observational indistinguishability was overclaimed | Scoped coherent-channel product-ancilla statement under independently prepared normalized ancilla and decoupled dynamics (#998) | Retain scoped claim; review exact hypotheses |
| Recurrence and chaos | Poincaré recurrence was used for common-time return; integrability/ergodicity extrapolation was overbroad | Finite-order return distinct from general Hamiltonian recurrence; bounded numerical chaos claims (#999) | Retain correction; check surviving mirrors |
| Bell/operational completion | Bell-local premises and five operational conditions were not sufficiently explicit | One-step local interventions and readouts; open physical sourcing of complex matrix/tensor kinematics (#1000) | Retain correction; check whether each propagated edit is necessary |

These are evidence maps, **not independent reproofs** of the cited Lean,
paper or numerical claims. Verification of exact retained hypotheses and
the independent assessment of the post-#994 hunk set are pending.

## Directly reproduced surviving inconsistency (separate correction)

`book/ch02-substratum.md:106` is **byte-identical at this paragraph**
between the pre-#982 baseline and current main:

1. It correctly says T invariance gives `θ∈{0,π}` and does not determine
   the physical `barθ`.
2. It then says the QCD theta angle is **exactly zero** from the
   substratum's T symmetry.

These assertions conflict within a paragraph. The detailed controlling
source `papers/SM.md` §§5.2–5.3 (Theorems 18 and 21) instead retains
`θ=0` or `π` and an open `barθ=θ+arg det(Y_u Y_d)` question.

**Disposition:** confirmed pre-existing source defect, not attributable
to #982. Tracked in [issue #1004](https://github.com/amaybaum/incompleteness/issues/1004).
Do not use it to justify rewriting additional passages. Fix it in a
separate minimal correction, with the chapter's FULL mirror and only
necessary regenerated book artifacts. This audit PR makes no such edit.

## Outstanding minimum-change review (not yet certified)

The #994 reports stop at their reviewed commit. Later #995, #998, #999
and #1000 correction PRs introduce further changes. The highest priority
*net* source surfaces for an independent hunk-by-hunk pass are:

- `papers/Main.md` (33 added/33 deleted net source lines): chiefly
  finite recurrence, Bell locality and operational-completion scope.
- `papers/Methodology.md` (54/54) and `papers/Explainer.md` (39/39):
  broad summaries must inherit exact source hypotheses without replacing
  correct exposition for style.
- `papers/SM.md` (63/45): period/continuum, integrability and
  physical gauge/carrier dependencies need theorem- and proof-level checks.
- `book/ch02-substratum.md` (45/47),
  `book/ch03-structural-realism.md` (43/43) and
  `book/ch18-beyond.md` (23/16): correct only claims the source
  establishes and retain valid older wording.
- `book/The-Incompleteness-of-Observation-FULL.md` (244/235):
  treated as a mirror, **not as independent scientific edits**.

Parenthesized numbers are additions/deletions for the direct
pre-#982 → snapshot compare, not post-#994 counts.

For **every surviving substantive hunk**, the next reviewer should
produce the following row before issuing a complete verdict:

| Required field | Acceptance standard |
| --- | --- |
| Path + original/new line range | Both statements reproduced from pinned blobs |
| Finding that triggered change | Exact false claim, invalid proof, wrong status or stale mirror |
| Authoritative evidence | Theorem/Lean declaration, exact counterexample, control or primary citation |
| Minimal patch | Smallest accurate correction retaining valid proofs and voice |
| Scope | Core/source edit versus necessary downstream propagation; identify generated mirrors |
| Disposition | REQUIRED / EXCESS-RESTORE / NEW-RESULT-REVIEW / UNDECIDED (with named gap) |

An uncertain scientific correction is **not** restored speculatively.
No additional manuscript text is changed without an evidenced disposition
and a separate authorization for the corresponding minimum patch.
Retained new propositions supported by their own proofs are not
automatically “unnecessary” because they were absent before #982.

## Controls, independence and release boundary

- Verify current HEAD against this pinned snapshot before doing a
  diff-to-main review; record any main movement instead of silently
  changing the comparison endpoints.
- Independently verify sampled claims in their original source and
  correlate any changed status with `verification/coverage/LEDGER.json`,
  Lean/manuscript census and verification results; do not substitute
  a green CI badge for scientific proof.
- Search `papers/*.md`, `book/*.md` and the FULL mirror for status
  synonyms; maintain legitimate non-target phrases and preserve
  independent positive results.
- Require an exact-head recheck of all diffs/claims being certified and
  review of reviewer-generated hunk dispositions. The earlier #994
  acceptance cannot certify later #995/#998/#999/#1000 edits.
- Current-main CI `verify` was successful at `6e219231483bb404c0d055ab9a447278422a597e`
  ([run 40956463456](https://github.com/amaybaum/incompleteness/actions/runs/40956463456)).
  This establishes a successful *check run*, not a minimum-diff verdict,
  a physical correctness result or independent review of this file.
- **No manuscript, TeX/PDF, Lean, CI workflow, or assertion status is
  modified in this research increment.** No branch merge, release,
  special workflow dispatch, native freeze or source restoration is
  authorized by the existence of this audit record.

**Present verdict:** `PARTIAL / MINIMUM-DIFF NOT CERTIFIED`.
The already reviewed #994 minimization and later correction evidence
justify retaining their explicitly supported corrections. A complete
post-#994 hunk classification is the remaining acceptance condition.


## 2026-10-30 follow-up: post-#997 hunk reviews (not independently certified)

The main source endpoint advanced to `f6989a27815c4d715223eebf2859422c1231e3f8` after #997. Rather than silently rewriting this original fixed-snapshot audit, the added `POST997-CHECKPOINT.md` pins new measurements and the complete 370-hunk inventory across 32 maintained source files (the FULL book is a mirror). The `PR-PROVENANCE-370.md` crosswalk records 324 exact new-text matches in the five correction PRs and 46 explicit manual provenance routes, not an independent proof of minimality. Source-scope workpapers for Main 33, SM 32, Methodology 35 and book Chapter 3's 30 hunks give 130 preliminary author-side dispositions: 125 scientific/status changes supported by earlier scoped reviews and 5 wording questions. The other 227 substantive hunk records need individual review. All 13 horizontal-rule changes are **required** under the Pandoc safety rule in AGENTS.md; [issue #1006](https://github.com/amaybaum/incompleteness/issues/1006) was closed as an invalid attempt to revert them. The pre-existing strong-CP contradiction remains independently tracked as [issue #1004](https://github.com/amaybaum/incompleteness/issues/1004).

**Status remains PARTIAL / MINIMUM-DIFF NOT CERTIFIED.** These audit files are additions only: they do not edit manuscripts, regenerated outputs, Lean, coverage/grade records or CI. Current-head success only verifies the checks, not scientific judgment. The independent hunk-by-hunk minimum-scope reviewer and an owner's exact-SHA authorization remain required for merging #1005; #918 stays held.
