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
- `review/STAGE0-REVIEW.md` and `review/toy0/`: the independent review of the Stage 0 draft (ACCEPT WITH CHANGES; L3′
  sound; required changes R1–R9) and its toy checks.
- `stage0/r2/`: the Stage 0 revision applying R1–R9 and the owner decisions of 2026-10-26 (S6 approved as a labelled
  proof-check; global closure bound included, larger searches deferred; symmetry reduction with the corrected control;
  the five named works checked before any novelty claim), with the owner's three safeguards (soundness,
  completeness, non-vacuity). `stage0/code/` holds the production closure and the independent reference code;
  `stage0/design-r2/` the regenerated design evidence and `RUN-MANIFEST`. Everything ran on toy, planted and
  small-window instances and S6's carrier structure only; nothing on v8's configuration class. Unreviewed, not frozen.

- `review/STAGE0-RECHECK-r2.md`: the independent review of Stage 0 r2 (ACCEPT WITH CHANGES, R1–R9 and S11; not a
  clean accept, so no freeze).
- `stage0/r3/`: the Stage 0 revision applying the r2 review and the owner decisions of 2026-10-26:
  - **Two-layer freeze.** Layer 1, the scientific specification, is the object to be frozen. Layer 2 (the production
    enumerator, controls, configuration hashes and execution certificate) is finalized only after Layer 1 passes
    independent review.
  - **Per-direction check.** It is a required control, not a diagnostic. A mutant blind in one direction leaves every
    aggregate count unchanged; it is caught by the per-direction control and missed by the aggregate check.

  `stage0/code-r3/` is design-evidence code, not frozen. `stage0/design-r3/` holds the regenerated evidence, its
  `RUN-MANIFEST` and the retained stdout/stderr of every step. Everything ran on toy, planted and small-window
  instances; nothing ran on v8's configuration class, and the v8 enumeration is not authorized. Under independent
  review; not frozen.
- `review/STAGE0-RECHECK-r3.md`: the independent review of Stage 0 r3 (ACCEPT WITH CHANGES; RC1–RC10, all bounded
  text edits, so not a clean accept and no freeze), with the reviewer's mutants and probes in `review/toy-r3/`. Every
  cheap control replayed byte for byte, and the quick mutant campaign matched its recorded hash.
- `stage0/r4/`: the Stage 0 revision applying the r3 review's RC1–RC10 and nits, and the owner decisions of
  2026-10-26:
  - O-a: the r3→r4 diff is reviewed independently, and the freeze follows only a clean acceptance;
  - O-b: an outcome-neutral S1b/S1c trigger, Rule T in §12, preregistered before any S1 result;
  - O-c: PO6 is restored in full;
  - O-d: the new planted families and mutants run on toy instances only.

  `stage0/code-r4/` is design-evidence code, and `stage0/design-r4/` holds the regenerated evidence with its
  `RUN-MANIFEST` and retained outputs.
  - Every control passes.
  - The configuration-based v8 refusal is exercised 13 ways.
  - The quick mutant campaign catches all 16 mutants at their named case. These include decision-level mutants and
    the B-type, G and Φ-adjacent planted families.
  - The toy demonstration's limits are disclosed in plan §9.

  Nothing ran on v8's class. The v8 enumeration is not authorized, and the full campaign belongs in CI.
