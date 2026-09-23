# Equivalence strengthening roadmap — 2026-09-05

> **Historical charter.** This is the charter as it entered the repository from the session
> transfer, kept verbatim below. It is reconciled with, and superseded by,
> `COMPLETION-ASSUMPTION-AUDIT.md`: the package this charter calls current is the round-41
> five-condition statement, every row of its ledger is settled in the kernel with a witness, and
> the most compressed package currently recorded is `OIPlusElem` (`carrier_general_oiPlusElem`).
> Read the audit note first; do not restart the five rows from here.

## Objective

Make the left-hand side of the exact finite OI↔QM characterization smaller and more primitive while preserving a true necessary-and-sufficient theorem.

## Current exact package

`WellFormed = CompositeOperationalValidity ∧ SystemToLevelOne`

`SubstantiveCompletion = InertSpectatorCompositionality ∧ HasCompositeUnitaryControl ∧ IteratedAncillaClosure`

Under `WellFormed`, exact finite operational QM iff `SubstantiveCompletion`.

## Why OI-N is not another equivalence axiom

N4 proves passive incompleteness on a nontrivial full matrix carrier for every theory. Therefore it is intrinsic to the observable algebra and cannot discriminate the quantum-completion conditions or OICore. Adding it to the equivalence left side would not strengthen the characterization.

## Five-assumption audit ledger

| assumption | first derivation route to test | required countercontrol if derivation fails |
|---|---|---|
| `SystemToLevelOne` | EmbeddedObservation / observer recursion / level-one closure | theory with embedded-like observer structure but no system→level-one seam |
| `IteratedAncillaClosure` | observer recursion + repeated record/ancilla embedding | finite closure at first level but failure under iteration |
| `InertSpectatorCompositionality` | implementation locality / spectator independence | existing 2-positive/non-CP style models or a sharpened spectator-failure theory |
| `CompositeOperationalValidity` | locality + operational closure, kept distinct from CP | well-formed maps/composition with invalid composite operational action |
| `HasCompositeUnitaryControl` | elementary transition richness + reversible richness + composition | monomial/read-write/control theory showing finite reversible richness without continuous off-diagonal reachability |

Each line must end as DERIVED or INDEPENDENT. No semantic relabelling counts as derivation.

## Priority

Start with `SystemToLevelOne` and `IteratedAncillaClosure`; they are most plausibly downstream of embedded observation/recursion. Then spectator compositionality and composite validity. Attack full composite unitary control last because it is the dominant quantum-selecting assumption and the easiest place to smuggle the answer into a definition.

## Desired endpoint

A theorem of the form

`PrimitiveObserverAxioms T <=> ExactFiniteOperationalQM T`

where `PrimitiveObserverAxioms` is visibly weaker and more physical than the present completion package, and every implication is kernel-witnessed.

## Later strengthening

Only after the primitive package is minimized: formalize the whole process structure and seek a structure-preserving equivalence between completed OI processes and finite-dimensional QM processes. Do not claim categorical/dagger equivalence before the objects, morphisms, tensor, discard, instruments, classical outcomes and any dagger are explicitly defined and both directions witnessed.
