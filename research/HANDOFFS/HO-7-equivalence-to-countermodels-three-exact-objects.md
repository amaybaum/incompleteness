# HO-7 (v1) — equivalence → countermodels: three exact objects

**From** `research/equivalence` (nodes E2, E3). **To** `research/countermodels`. Version 1, 2026-10-10.

## Statement

1. **Ω₄ = {(x, s) ∈ ℝ³ × ℝ : |x|⁴ + s⁴ ≤ 1}.** Drivable (flow `R_z ⊕ 1`, `J = cyc3 ⊕ 1`), with a sharp seed, relatively
   strictly convex, supporting-effect complete for its full effects, centrally symmetric — and no set of its affine
   automorphisms is boundary transitive or has a dense boundary orbit (its `x₁ = x₂ = 0` section is not an ellipse). A
   countermodel to deriving K∞-Trans from every other single-system seam together (K∞-Drive, K∞-Seed, K∞-V4 with
   `G = Aut` and full effects, K∞-Geom, capacity ≤ 2).
   Label: CONJECTURE (complete written proof with exact checks): [X] `e2_drive_trans` 10/10,
   `VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS`; [W] W1–W4; [K] TransitiveBody.lean:602, DenseOrbit.lean:174 (contrapositive),
   KInfFoundations.lean:590, :632.
2. **The swapped gate** `actT s ∘ cnot ∘ actT s`, `s` the exchange of the first two axes: two-NOT native-gate data with
   `NT = diag(−1, 1, −1) ≠ nflip`, and also a one-NOT native gate with `NT` on both sides. So distinct-NOT data need not
   be a new gate; the J/K maps at `d = 5, 7` have no one-NOT reading with either NOT.
   Label: CONJECTURE (exact instances): [X] `e2_copy_conj` run 2 13/13, `VERDICT TYPE-COVARIANCE-CONSISTENT` (run 1
   kept, two countercontrol expectations refuted); [D] `EqvSeamsControl.lean` (run 38083519826).
3. **The class "every matrix at sizes 2^k, unit-disk diagonal matrices elsewhere":** `Architecture`, `LabelInvariant`,
   `DaggerStable`, drivable on every `Fin (2^k)`, not drivable on `Fin 3`, and not `ContextStable` — the countermodel
   showing `ContextStable` load-bearing for the descent of drivability.
   Label: CONJECTURE: [X] `e3_compress` K2 + [W] closure arguments.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `8c67c7fbe22ca817858dc6711c413f7a5e3d45db` |
| proposal | `research/equivalence/handoff-proposals/HP-3-countermodels-thread.md`, sha256 `a42fae1925a973189b32c26c20a361975709eb66a266474238b3b9222ab68b7f` |
| results rows | `research/equivalence/RESULTS.md` R-E2.3, R-E2.5, R-E3.3 |
| scripts, outputs | `e2_drive_trans.py` (sha256 prefix `394850c87d98be40`), `.out` (`d5b6fce9fb00d471`); `e2_copy_conj.py` (`c28e1b97b3ec51cb`), `.out` (`a5b9d6e4f897ad16`); `e3_compress.py` (`18c3aa1b95e82773`), `.out` (`f4b93781c20574a4`) |
| coordinator audit | replays byte-identical (3/3); `indep_checkE.py` X1: the central section `x⁴ + s⁴ = 1` of Ω₄ has curvature 0 at its four axis points (controls: circle 1, ellipse 2 and 1/4), so Ω₄ is not an affine image of a ball — with the certified TransitiveBody.lean:602 and DenseOrbit.lean:174 this is the negative half of item 1; X2: convexity (Hessian of `|x|⁴` is `4|x|²I + 8xxᵀ`), central symmetry, `R_z(t)` and `cyc3` preserve Ω₄, `cyc3 R_z cyc3⁻¹ = R_x`, `R_x(π) = nflip` — CONFIRMED, replay identical |

## What the receiving thread may assume

The three objects at their labels, as exact countermodels usable in its own classifications (Ω₄ for the single-system
analogue of extreme-ray transitivity T, NOTES-C3 §6; the swapped gate and the `2^k` class as reference instances).

## What it may not assume

- that item 1's positive properties (drivability, seed, V4, Geom, capacity) are certified — they are the source
  thread's exact record; only the two cited ball theorems are kernel theorems;
- that these objects bear on the pair cone directly: Ω₄ is a single-system body, not a composite.

## Receipt

The receiving thread copies this file into `research/countermodels/inbox/` with a commit naming `HO-7 v1` and records
in its `LOG.md` whether and how it relies on it.
