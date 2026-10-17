# Conditional affine respect from label duals

**Status: Written conditional interface supplied; formal certification and physical source remain open.**
This umbrella note is research/design, not a native control plane or F candidate.
Planning snapshot: main `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

## First research update (2026-10-13)

[The separate interface argument](https://github.com/amaybaum/incompleteness/blob/476651fed70017543345bd784de95ead9f193ccf/verification/programmes/oi-qm/reconstruction/preservation-induction-design/affine-respect-interface.md) evaluates each affine relation against jointly separating output tests with affine preparation pullbacks. It includes a StateRespect-without-AffineRespect separation. No Lean certificate or source for the physical test inventory is supplied.

## Current gap

The equivalence ledger identifies affineRespect_of_labelDual as a small conditional formalization for K∞-Act. PR #827 mentions the label-dual route as background but does not propose this theorem.

- CompletionAction supplies OpDatum, AffineRespect, StateRespect and the induced affine-map machinery.
- The theorem and its label-dual definition are proposed work, not existing adopted declarations under this name.
- Even a proof would not supply the physical reversible operation family or the label-dual hypothesis.

## Research question and proposed work

Does a precisely stated label-dual hypothesis make an OpDatum preserve all finite affine relations among preparation vectors?

- [ ] Resolve the source argument and formulate the minimal label-dual condition in landed stage/completion vocabulary.
- [ ] Prove the implication by evaluating affine relations against the transported test labels, displaying every quantifier and closure assumption.
- [ ] Check how it can serve the protocol-tower or K∞-Act interface without assuming AffineRespect as its own input.

## Controls and evidence obligations

- [ ] A positive instance with an explicitly supplied label-dual witness.
- [ ] The existing StateRespect-without-AffineRespect separation, so the weaker condition is not silently substituted.
- [ ] An independently checked failure or correctly labelled unresolved case when the required test/label hypothesis is absent.

## First review milestone

A small design module with a precise conditional statement, controls and standard axiom reports, before drafting a native certification round.

Before any execution, select the exact scope, source assumptions, controls and
decision rule. If this becomes a native round, prepare its concrete control
plane and follow AGENTS §A.39, including the owner's exact F designation.
No native round is designated or executed by opening this placeholder.
Computational conclusions require green controls; universal claims need
written arguments or kernel proofs at their stated evidence level.

## Related records and dependencies

- [Protocol tower draft](https://github.com/amaybaum/incompleteness/pull/827)
- [Equivalence ledger](https://github.com/amaybaum/incompleteness/blob/424aa33bf16c5160c00e6f6aea974d00c0d745dd/research/equivalence/LEDGER.md)

This note tracks the broader agenda alongside the linked research evidence. Existing theorem and manuscript
classifications, ROADMAP rows, adopted modules, CI workflows and historical
round records retain their current authority. Later work should be recorded
forward, with its own scope and provenance.
