# Phase 1 plan: post-A1 obstruction reassessment

Status: plan, committed before any analysis. Paper-only. WP-2, accountable to #1169 with #914.
Authorization: owner decision quoted at #1169 comment 7209026471 (amaybaum, received
2026-11-27, coordinating session): "Approved: Phase 1 post-A1 obstruction reassessment as scoped
above, paper-only under WP-2, accountable to #1169 with #914." No premise adoption, no scientific
computation, no Phase 2-4 execution.

Drafting snapshot D: origin/main at 13c05b4fe (branch research/phase1-post-a1-obstructions-20261127).

## Goal link

Item served: the #914 central bottleneck, that the finite-horizon theorem yields a representation
equivalence and not a physical mechanism, in the context of A1 retirement (#1169). What this work
decides for it: which established obstructions to native preparation, native persistent
observation and native coherent control survive independently of global finiteness (A1), which are
reopened by its retirement, and which candidate mechanisms should be tested first in Phase 2. It
does not decide whether any mechanism exists.

## Questions

Q1. Which established impossibility, no-go and ceiling results on `main` and in the named Issues
bear on native preparation, native persistent observation or native coherent control
(interference, continuous mixing, noncommuting transformations beyond a classical operational
ceiling)?

Q2. For each, does its proof use A1 (total/global finiteness of the substratum state space or of
the universe) or only local finiteness (finite per-site alphabet, finite coupling range, finite
light-cone / finite observer resources)? At which proof step does A1 enter, if it does?

Q3. For the reopened set: what physically motivated candidate mechanisms could fill the gap, and
which of them could discharge several dependencies at once?

Q4. Which candidate(s) should Phase 2 test first, and by which cheapest eliminating test?

Removing an obstruction (Q2) is kept distinct from establishing a mechanism (Q3, Q4): a reopened
obstruction is a necessary-condition change only.

## Inventory method (exact)

1. Read #914 (body and comments; dependency index), #866, #1507, #1509, #1461, #1062, #1210 and
   #1169 via `gh api` (read-only), and list every verification record, paper section and Lean
   module they cite.
2. Grep the corpus (`papers/*.md`, `book/*.md`, `verification/**`, `verification/lean*/**`) for
   the result families: "no-go", "ceiling", "impossib", "obstruction", "cannot", "classical
   operational", "CHSH", "Tsirelson", "interference", "noncommut", "preparation", "persistent",
   "recurrence", "Poincare", "permutation", "bijection", "reversib", "A1", "total finiteness",
   "finite state", "cycle", "periodic".
3. Admit a result to the inventory iff it is (a) stated on `main` or in a named Issue as proved,
   derived, or a computed negative result, and (b) bears on preparation, observation or coherent
   control. Conjectures and open questions are listed separately, not classified.
4. For each admitted result, locate its actual proof (paper section, Lean theorem, verification
   record) and read the proof steps; record the hypotheses used.
5. Reuse existing records' conclusions where their proof is located and read; do not recompute.
   Where only a status claim is found without a proof, record "proof not located" (unclear).

## Classification rule (outcome-neutral, fixed in advance)

For each result R with located proof P:

- **Surviving**: no step of P uses a hypothesis implied only by A1. Hypotheses that remain
  available after A1 retirement (local finiteness of alphabet, finite coupling range, determinism,
  bijectivity/reversibility of the update, linearity A5 where it is a separate posit, finite
  observer resources, finite measurement records) do not count as A1. R survives as stated
  (still conditional on its other hypotheses, which are listed).
- **A1-dependent (reopened)**: some step of P uses a property that follows from A1 and fails
  without it: finite global state space, hence eventual periodicity / exact recurrence of every
  orbit; finite-dimensional global Hilbert/permutation representation; pigeonhole over global
  configurations; counting arguments over the whole state space; finite cycle decomposition of the
  global bijection; compactness obtained from global finiteness. The step is named.
- **Unclear**: P not located, or P uses a property whose derivation from A1 vs local finiteness
  cannot be settled by reading (e.g. a finiteness hypothesis that could be either), or the result
  depends on a further result itself unclear. The undecided step is named.

Additional label for reopened results: whether the A1-free setting is known to *escape* the
obstruction (an explicit counterexample on `main` or in the literature) or merely *no longer
proved* (removal of proof, not refutation). Only the former is a reopening with evidence; the
latter is a reopened question.

Weakest-link rule: a result depending on an unclear lemma is unclear.

## Candidate ranking criteria (applied in this order, recorded per candidate)

1. Physical motivation: an independent reason (known physics or a minimal-substratum argument
   under §A.29) for the mechanism, not the need to fill the gap.
2. Required additional premises: number and strength of new posits (stated as candidates only,
   not adopted); fewer and weaker ranks higher.
3. Explanatory power across dependencies: how many of preparation / persistent observation /
   coherent control (and #914 edges) it would address at once.
4. Dependent Issues: which open Issues it bears on.
5. Cheapest decisive test: existence of a cheap test that could eliminate it; a candidate without
   any eliminating test ranks below one with such a test regardless of other criteria.

## Rejection criteria (any one rejects, with the reason recorded)

- Circularity: the mechanism presupposes the repertoire it is meant to generate (e.g. assumes
  native coherent control to derive it).
- Imported quantum structure: Hilbert-space amplitudes, Born rule, complex phases, noncommuting
  operators or tensor-product entanglement posited at the substratum level rather than derived.
- Encoded predetermined outcomes: the construction stores the quantum outcome statistics (or a
  table of them) in the substratum initial data or rule.
- Classical simulation encoded into the substratum: the substratum is engineered to run a
  simulation of quantum mechanics (a universal-computer embedding of QM) rather than a basic
  dynamics from which the repertoire follows.
- No eliminating test: a candidate that can be adjusted to fit any outcome (§A.29) is rejected.

## Stopping conditions (bounded)

- Inventory stops when every item cited by the eight named Issues and the records they cite has
  been classified, and two further grep passes surface no new admissible result.
- Candidate generation stops at the earlier of: at most 6 ranked candidates surviving the
  rejection criteria, or three consecutive candidate proposals that each fail a rejection
  criterion.
- No computation is run. If a classification needs a computation, it is marked unclear with the
  computation named as a Phase 2 item.
- The unit ends with REPORT.md (verification table per §A.46 item 4; §A.42 item 8 reference
  tracing) committed locally; no push and no GitHub writes. Independent review is outside this
  writer's role.
