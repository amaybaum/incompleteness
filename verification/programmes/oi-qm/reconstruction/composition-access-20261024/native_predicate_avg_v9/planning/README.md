# NP-AVG-1 planning (Issue #929) — WIP / UNVERIFIED, not frozen

Planning drafts for NP-AVG-1: does `native_predicate_v8`'s negative depend on the pointwise background convention?
Nothing here is a preregistration, a result or an authorization. No checker exists and nothing has been computed on
the question. The branch is based on #912's head `2af1d5d5`, which contains v8 at `fc452ea8`.

## Files

- `PLAN-r1.md`: first draft, the object of `review/REVIEW.md` (ACCEPT WITH CHANGES: 13 required changes, 9 owner
  decisions).
- `PLAN-r2.md` and `CHANGES-r2.md`: the revision applying every required change, with the mapping from each review
  item to the section that addresses it. Owner decisions O1–O9 stay open, each carrying the review's recommendation.
- `NOTES.md`: the drafter's sources (blob ids and line references) and every place where #929 had to be
  interpreted.
- `review/REVIEW.md`: the independent pre-freeze review of r1. `review/toy/` holds its toy checks of the three exact
  reductions L1–L3, which hold for v8's rule.
- `review/RECHECK-r2.md`: the re-check of r2. Verdict: BLOCK for freeze, on the owner's nonredundancy requirement.
  - The mechanical revision is accepted, with five remaining gaps (IC2, I1/I2, Z0, L2c, IM1).
  - Under full averaging, masking collapses almost every record (L3), which then fails the law; under the
    frame-conditioned convention a collapsed record reduces to v8's pointwise law. So most outcome classes are
    forced or restate v8, and only the "tie" residue could be informative.
  - Recommended next step: a two-stage plan. Stage 0 writes up the collapse argument and runs a preregistered
    geometry-only enumeration of every record's L3 closure; Stage 1 runs the law machinery only on a non-empty
    residue.
- `stage0/STAGE0-PLAN.md` and `stage0/STAGE0-NOTES.md`: the Stage 0 draft (owner-approved drafting, 2026-10-26), a
  geometry-only preregistration of the masking structure. Not reviewed, not frozen; the enumeration is not authorized.
  `stage0/design/` holds the cheap design controls the owner approved (configuration combinatorics, and toy
  geometries only; nothing computed on v8's class), with their outputs.
