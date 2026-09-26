# Track B act 31 — off-locus uniqueness after full product admission: PREREGISTRATION DRAFT

**Status: DRAFTING, not frozen.** This file opens a native V3 round from the certified Act 30 receipt commit.
No commit on this branch is `F` until the owner explicitly designates one. No execution is authorized
by the existence of this draft or its pull request.

```v3-round
round A31
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-31-off-locus-uniqueness/
record AM verification/receipts/A31.json
execution A verification/lean-mathlib/OIBridge/ProductOffLocusUniqueness.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
```

## D and V3 lifecycle

- **D** = `d61c6c5409db201e3c25abbf3ec0ecce1f530684`, Act 30's certified final receipt commit Q.
- **F** = not designated.
- Execution must remain linear from the designated F and must not absorb later `main` before E.
- If E is certified, reconciliation chooses the then-current later base as V3 S9 permits; Q then
  carries this round's receipt. Publication is outside the V3 predicates.

## Research task — draft scope

Act 29 froze A29-1 at one prescribed pair and did not execute it because A29-0 had not reached
ADMITS. Act 30 has now established full admission at the frozen product configuration, so that gate
is no longer the obstruction.

This round is intended to decide the exact residual question at act 29's fixed pair:

- first factor class bijection: the one induced by `Equiv.swap (2 : Fin 4) 3`;
- second factor class bijection: the identity;
- domain of comparison: realizable product tuples whose class lies outside the product locus.

The two intended outcomes are the same alternatives act 29 recorded:

1. **NONUNIQUE:** exhibit two eligible laws for that same prescribed pair and one off-locus
   realizable tuple on which their outputs are not `GramPhaseEquiv`; or
2. **UNIQUE:** prove that every two eligible laws for that same pair agree up to
   `GramPhaseEquiv` on every such off-locus realizable tuple.

Properness of the product locus is provenance/non-vacuity evidence only; by itself it proves neither
alternative.

## Intended provenance

This round may consume the exact landed statements it needs from:
- act 28 for the product locus and its properness witness;
- act 29 for the fixed pair and the original A29-1 scope;
- act 30 for A30-0-ADMITS and the existence of fully eligible families.

The final freeze must list every consumed theorem explicitly and freeze exact Lean propositions,
controls, outcome labels, hazards and route authorization before F is designated.

## Parallelism boundary

A31 is intentionally independent of A32. It reads no A32 object, result, receipt or control plane.
A later movement of `main` does not rewrite F..E; it is handled only by reconciliation after E.

No law is adopted as physical by any outcome of this round. No claim about quantum evolution,
continuity, a generator, or another configuration is part of this draft.
