**Planning status** (AGENTS.md §A.45)
- **Parent programme:** #1169 (OI–QM equivalence).
- **Related work:**
  - #945: repair or narrow the finite-precision ε-realization step at Main:556.
  - #1210: one shared OI mechanism across quantum phenomena.
  - #1211: the Substratum → SM → QM bridge audit.
- **Tier:** Foundational. This is the owner's ranking, 2026-11-09.
- **Readiness:** ready for unit 1.
- **Authorization:** paper-only unit 1, as recorded in the first comment. Nothing else is authorized.
- **Writer / reviewer:** the coordinating Claude Code session writes. A fresh independent reviewer reviews.
- **Status source:** the reviewed unit records once they exist. Scientific status lives in proofs and records on `main`, never in this Issue (§A.45 rule 1).

## Central question

Can one mechanism derived from OI approximate the complete accessible predictions of quantum mechanics to arbitrary finite precision? The mechanism uses finite deterministic dynamics and independently justified observer access. The approximation must hold consistently across preparation, measurement, adaptive choices and repeated composition.

This question is distinct from #1169's exact question. That question asks whether OI can generate the full quantum operational structure without importing it.

## Levels

| Level | Requirement |
| --- | --- |
| A: finite-horizon statistical approximation | Any specified finite quantum experiment's observable law is reproduced within ε. |
| B: uniform operational approximation | One reusable mechanism and rule family approximates a whole specified class of experiments, including adaptive measurement and composition. |

Level B is the main target. A preloaded table of quantum predictions could satisfy Level A without explaining anything.

The investigation must state four things explicitly:
- accuracy bounds;
- resource scaling;
- shared preparations and transformations;
- failure records.

Any dependence on ε, the horizon or memory is declared in advance.

## Unit 1 (paper-only)

Unit 1 asks five questions:
1. Do Main's existing approximation results meet Level A? Answer this with #945's finding: the exact-arithmetic theorems (:544, :576) and the density corollary (:578) survive, but the finite-b constants are unproved.
2. What prevents Level B?
3. What is the smallest missing operational property?
4. Is continuous coherent mixing still necessary for the approximate target?
5. Which dependencies are shared with #1169, #945, #1210 and #1211, and which are independent? Each is recorded as proved, conditional, disproved or open, with its carrier and assumptions.

The deliverable is a dependency matrix and an assessment, followed by a fresh independent review of the full text. A review ACCEPT does not authorize computation, new physical premises, a manuscript change or a merge.

## Boundaries

- Do not duplicate #945's repair work. Cite it.
- Do not alter #1169's exact-equivalence conditions, or the ongoing reviews.
- Introduce no assumption chosen because it reproduces quantum predictions (§A.29).
