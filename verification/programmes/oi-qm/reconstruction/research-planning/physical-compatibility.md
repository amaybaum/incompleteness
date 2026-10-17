# Physical compatibility: spectrality source and preservation implication

**Status: Bounded spectrality screen complete; the general implication remains open.**
This umbrella note is research/design, not a native control plane or F candidate.
Planning snapshot: main `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

## First research update (2026-10-13)

[The research result](../spectrality-preservation-research/result.md) proves local preservation for coPSD and rejects a CNOT-tilted model because it fails the retained product domain. The exact implementations pass 109 and 112 controls. This resolves one model family; it neither proves SP ⇒ preservation on the common domain nor supplies SP physically.

## Current gap

The bridge audit exhibits uniformly available operations that fail to preserve two independently given cones. Spectrality excludes both fixtures through static state/test arguments, but its physical OI source and its implication to preservation are unresolved.

- PR #820 contains the bridge witnesses and the spectrality candidate screen at research commit 1d4606b2. Its written exclusions do not prove SP ⇒ preservation.
- PR #831 proposes conditional preservation by induction from primitive preservation, attachment/discard and cone-closure assumptions. It does not supply those assumptions physically.

## Research question and proposed work

Can an independently motivated physical premise establish state–operation compatibility without restating the preservation target or defining states by operational reachability?

- [ ] Prove or refute SP ⇒ preservation by the uniformly guaranteed stopped maps under the common domain; state the third-axis and J-conjugate obligations separately.
- [ ] Audit the stronger H3/CNOT lane for assumptions that already force Q3 inclusion or equality; retain the common-domain test against both fixtures.
- [ ] Investigate the physical source of SP or another independently stated candidate at its actual carrier and evidence level, keeping a proposed extra postulate distinct from an OI derivation.

## Controls and evidence obligations

- [ ] Both K_B and K(Z_F), with their complete applicable premise ledgers and uniform availability licences.
- [ ] Quantum PSD and classical diagonal positive comparisons; an exclusion of every model cannot earn a source derivation.
- [ ] The disguise test, including the closed-cone stopped-map/rotation-flow equivalence, and rejection of fullClass-only replacement witnesses or reachable-state definitions.

## First review milestone

A reviewed implication or exact countermodel, together with a source ledger naming every extra premise. A physical source is earned only when the independent justification and every cross-level bridge are supplied.

Before any execution, select the exact scope, source assumptions, controls and
decision rule. If this becomes a native round, prepare its concrete control
plane and follow AGENTS §A.39, including the owner's exact F designation.
No native round is designated or executed by opening this placeholder.
Computational conclusions require green controls; universal claims need
written arguments or kernel proofs at their stated evidence level.

## Related records and dependencies

- [Bridge and spectrality research](https://github.com/amaybaum/incompleteness/pull/820)
- [Conditional preservation draft](https://github.com/amaybaum/incompleteness/pull/831)

This note tracks the broader agenda alongside the linked research evidence. Existing theorem and manuscript
classifications, ROADMAP rows, adopted modules, CI workflows and historical
round records retain their current authority. Later work should be recorded
forward, with its own scope and provenance.
