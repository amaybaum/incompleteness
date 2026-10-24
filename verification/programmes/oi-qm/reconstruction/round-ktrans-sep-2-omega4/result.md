# Reconstruction round KTRANS-SEP-2 — Ω₄, a convex body in ℝ⁴ with the named kernel properties on which no body-preserving family is boundary transitive: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #905. This note is stage S2, candidate `E`. The
owner designates `E` (§A.39); the designation is recorded on #905 and in the receipt.

- **`D`**: `48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29`, the head of `main` after #895. Its push run is 39766586077
  (`evidence/d-push-run.json`).
- **`F`**: `6b2ad388a30af21135dd0600a2773f57b57352d5`. `delta(D, F)` is the preregistration alone, blob
  `8a9751677675c172cd75e3bd880b4183ac730017`. The owner designated `F` in comment 6382448786 on #905.
  - Its exact-head `workflow_dispatch` run is 40077741127, attempt 1. It concluded `success` with all 38 jobs
    successful (`evidence/f-run/results.json`). It attests the control plane only: `F`'s tree carries no module.
- **Stages**, each a single-parent child of the one before:
  - C1, `06b0eae14002d4a89c5dc481d302cb52255fbb9d`: `controls.py` (blob `73f356565ce1402b37da80a5d18dddd556df23c5`),
    the pinned evidence files and `evidence/f-run/results.json`.
  - S1, `a9337346bc507441558daec60cb72ca77513484e`: the module (blob `ba7431915e7ab6e8f7bdfb6ab980f16067e9331b`), the
    probe (blob `19e19f28fa7644de0bcc3089a354317310de3e41`), the import line, the census family and the six workflow
    splices. Its exact-head `workflow_dispatch` run is 40089555298, attempt 1. It concluded `success` with all 39 jobs
    successful; in the Mathlib bridge job, `Build`, `Release gate`, L0, L and A concluded `success` and M `skipped`.
    No repair stage was needed.
  - S2: this note.

## The cells

The cells and their rules are frozen in the preregistration (*The decision rules*). Each token below is the one
`controls.py verdict E --freeze F --run-api RUN --jobs-api JOBS` prints, where `RUN` and `JOBS` are the runs and jobs
API answers of the exact-head run at `E`; control V checks this note against them. The module and probe bytes at
`E` are S1's, which read positive in run 40089555298.

- Q-NONELL: KTRANS-SEP-NONELLIPSOID-PROVED. Control S1 holds for `not_affine_eball_omega4`; the module elaborates,
  and its fifteen `#print axioms` reports are each within `[propext, Classical.choice, Quot.sound]`.
- Q-CEX: KTRANS-SEP-COUNTEREXAMPLE-PROVED. Control S1 holds for `omega4`, `not_affine_eball_omega4`,
  `not_boundaryTransitive_omega4`, `not_denseBoundaryOrbit_omega4` and `kinfTrans_separation`, with the same step
  conclusions.
- Q-EXACT: KTRANS-SEP-INSTANCES-EXACT. The probe blob at `E`, run by `controls.py` with `python3 -I -B` under sympy
  `1.14.0`, prints the frozen output (sha256 `d6f6d298d3ed57081f4e81bef267771fc81d8083a111c0414a69216c772a2940`), and
  X1–X3 and CX1–CX4 hold.

## The earned reading

Earned reading: Omega4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} is compact, convex and has nonempty interior,
satisfies ElementaryDrivability, carries the sharp seed seed4, and is RelStrictConvex and CentrallySymmetric about 0;
no body-preserving family of affine equivalences of R^4 is BoundaryTransitive or has a DenseBoundaryOrbit on Omega4
(kinfTrans_separation). Omega4 is therefore a counterexample to the implication from these properties, for
body-preserving families, to BoundaryTransitive and to DenseBoundaryOrbit.

## The non-inference rule

Non-inference rule: the round concerns Omega4 alone, in R^4. It states nothing about other compact convex bodies,
about chart dimension 3, about K-infinity-Stage, K-infinity-Act, K-infinity-V4 or K-infinity-Copy, about the
composite, or about which bodies OI supplies. The Euclidean 4-ball is countercontrol CX1: the kernel gives it a sharp
seed (sharpEff_sharpSeed) and a body-preserving boundary-transitive family (preservesBody_fullAut,
boundaryTransitive_fullAut), and CX1 checks its drive maps, central symmetry and strict midpoints at finitely many
exact states; the kernel has no ElementaryDrivability (eball 4) or RelStrictConvex (eball 4) theorem, so CX1 is a
finite exact check, not a theorem. Drivability fails on the interval [-1, 1] (not_drivable_Icc), and nothing is stated
for dimension 2. RelStrictConvex is the form in which the kernel gives singleton faces for every effect family; it is
not a frozen statement of K-infinity-Geom. Supporting-effect completeness of the full effects on Omega4 is an exact
identity with a written step, not a kernel theorem of this round. The exact layer is an exact computation, not a Lean
kernel proof.

The round changes no manuscript, no built artifact, no `verification/ROADMAP.md`, no landed kernel module and no other
round's record. K∞-Trans stays open.
