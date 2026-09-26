# Track B act 32 — single-carrier normalized-space isometry classification: PREREGISTRATION DRAFT

**Status: DRAFTING, not frozen.** This file opens a native V3 round from the certified Act 30 receipt commit.
No commit on this branch is `F` until the owner explicitly designates one. No execution is authorized
by the existence of this draft or its pull request.

```v3-round
round A32
kind non-sealing
record-directory verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/
record AM verification/receipts/A32.json
execution A verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean
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

Act 26 left A26-2 undecided at the single-carrier configuration. Its first positive-route step is
already kernel-proved: a tuple isometry satisfying the frozen hypotheses extends to a rigid motion
of the ambient Euclidean feature space carrying the normalized set onto itself. The route stopped at
the finite marked-set/classification step; no isometry outside the frozen finite family was exhibited.

This round is intended to close that exact classification problem, without changing the domain,
metric, quotient or generator family:

1. **RIGID:** prove every surjective isometry of the normalized space satisfying the exact act-26
   hypotheses belongs, on realizable classes, to the frozen finite family; or
2. **NOT-RIGID:** exhibit a kernel-certified isometry satisfying those hypotheses together with the
   separation required to place it outside that family.

If the rigidity alternative is earned, a separately frozen gated corollary may then ask the
prefix-constrained transition-family consequence that act 26 left NOT-EXECUTED. The corollary is
not part of execution unless its gate is explicitly frozen and opened.

## Intended provenance

This round may consume the exact landed statements it needs from acts 24–26, including act 26's
affine-extension theorem, nine-circle census and `rigid_motion_of_tuple_isometry`.

The final freeze must replace the old failed marked-set route with a fully specified route (or a
specified counterexample route), and must freeze exact Lean propositions, controls, outcome labels,
hazards and route authorization before F is designated.

## Parallelism boundary

A32 is intentionally independent of A31. It is single-carrier and consumes no product-admission or
off-locus-uniqueness result from A31. A later movement of `main` does not rewrite F..E; it is handled
only by reconciliation after E.

No isometry or finite family is adopted as physical by any outcome of this round. No continuity,
time composition, generator, or dynamics claim is part of this draft.
