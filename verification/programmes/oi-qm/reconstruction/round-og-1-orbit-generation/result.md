# Reconstruction round OG-1 — conditional orbit-generation infrastructure: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #780.

- **`D`** — `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`, the head of `main` after `CI-PERF-1` landed, certified by push
  run 36896981080.
- **`F`** — `0ae3e44ea096b567c4e0339fa642de73ec9d3a80`, parent `99c917eeac1b2b589b08738222c1b80bf3c9fa00`;
  `delta(D, F)` is the preregistration alone, blob `5daa80844f941749c53217f645fac7a8aa9e6fd1`. Its exact-head
  `workflow_dispatch` run 36964248550 concluded `success` with all 32 jobs succeeded, its `check-run` attestation; the
  owner designated `F`. That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `OG-1-INFRASTRUCTURE-PROVED`

> Given the stated seed/effect, drive, dimension and V4′ hypotheses, the normalized 3-ball route reaches the existing
> Lorentz bridge; the normalization and generated-action steps themselves require no additional physical premise.

In the kernel, over real normed spaces, with the named hypotheses P1 `SharpSeed`, V4′ `SeedOrbitAvailable`, K∞-R
`BoundaryTransitive` and the body premise `PreservesBody` stated as propositions and proved for no physical family:

- **the conditional orbit-generation route** (`OrbitGeneration`): on `ball3`, `PreservesBody`, P1 and K∞-R give
  `seedOrbit G r = directionalFamily` (`seedOrbit_ball3_eq`), and with V4′ the family reaches
  `NativeGateBall.lorentz_of_effects` at `p = 3` (`lorentz_of_available`);
- **G-AUT under words**: `PreservesBody` for a set of affine automorphisms gives `PreservesBody` for the subgroup it
  generates, with no further premise (`preservesBody_words`, `preservesBody_driveWords`);
- **normalization and transport**: the four named hypotheses move together, with body, seed, automorphisms and
  available effects transported jointly, along an affine coordinate change (`hypotheses_tr`) and along an injective
  affine chart of the body's affine span (`hypotheses_restrict`, with `affineSpan_preserved`); for a body carried onto
  `ball3` by `T` the seed orbit is the directional family read through `T` (`seedOrbit_eq_of_normalization`), and the
  Lorentz bridge holds for the transported effects (`lorentz_of_normalization`); the hypothesis `T '' Ω = ball3` is
  assumed, not derived;
- **3-ball transitivity**: the words of the control drive `ball3Drive` act transitively on the boundary of `ball3`
  (`boundaryTransitive_ball3Drive`), so the route applies to it (`seedOrbit_ball3Drive`);
- **the 4-ball countercontrol**: the closed unit ball of `EuclideanSpace ℝ (Fin 4)` is boundary-transitive under its
  linear isometries (`boundaryTransitive_ball4`, `finrank_E4`), so boundary transitivity does not select dimension three;
- **B1 and B5**: `flow 0` is the identity whenever `flow` is additive (`flow_zero_of_add`), and a body each of whose
  points has a finite orbit under the body's affine automorphisms admits no elementary drive
  (`isEmpty_drivability_of_finite_orbits`);

joined in the verdict `og1_infrastructure_core`.

The round sources none of its hypotheses. It does not derive stage consistency (SC∞), the drive, dimension three, V4′,
ELEM or the ellipsoid theorem from any OI construction; B6 is excluded; it contains nothing of K2, TR, CAR or SCL; and
it is not a proof that OI implies the one-system theorem or that OI is equivalent to complex quantum mechanics. It
edits no manuscript and no roadmap row.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `0ae3e44e` | the preregistration | 36964248550 | `success`, all 32 jobs; release gate 21 of 21, `lean-axioms` 5355, as at `D` |
| `C1` = `99a5112b` | stage C1: `controls.py`, blob `6a700bd7` | none required | `controls.py --self-test`: `controls: OK -- 30 checks` |
| `S1` = `9723513076df976c60c26b6523be7e97f8fec6c3` | stage S1: `OrbitGeneration` blob `0673321f`, `OrbitNormalization` blob `ea397e69`, the two import lines, the census family | 36966428820 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `S1`'s tree equals that of the predicted execution tree `dc340fb5`
outside the preregistration. `controls.py check S1 --freeze F` prints `controls: OK -- 18 checks`.

Run 36966428820 is a `workflow_dispatch` run whose `head_sha` is `S1`, run to completion with no job cancelled:

- the Lean kernel check, the Mathlib bridge, the 29 numerical-probe shards (act 42's dispatch-only exclusion shards
  included) and the probe aggregate each concluded `success`;
- the Mathlib bridge built `OIBridge.OrbitGeneration` and `OIBridge.OrbitNormalization` (3616 build jobs);
- each of the 64 `#print axioms` lines of `OrbitGeneration` and the 20 frozen lines of `OrbitNormalization` reports
  `[propext, Classical.choice, Quot.sound]`;
- the release gate passed all 21 steps: `lean-axioms` 5439 named results, the 5355 at `D` and the 84 new prints, no
  `sorryAx`; `lean-manuscript` OK with the new census family; 303 legacy records intact; 22 receipts holding.

## The evidence ledger at `S1`

| row | kernel identifiers | status |
| --- | --- | --- |
| L continuity | `OrbitGeneration`, blob `0673321f`; import-suffix SHA-256 `843c68c1…` | proved; control L |
| G-AUT word closure | `preservesBody_words`, `preservesBody_driveWords` | proved; control S3 |
| normalization | `hypotheses_tr`, `isBoundaryState_tr`, `seedOrbit_eq_of_normalization`, `lorentz_of_normalization`, `affineSpan_preserved`, `isBoundaryState_restrict`, `chart_restrictEquiv`, `hypotheses_restrict` | proved; control S4 |
| 3-ball transitivity | `boundaryTransitive_ball3Drive`, `seedOrbit_ball3Drive`, `euler_apply_pole`, `exists_euler_angles` | proved |
| 4-ball countercontrol | `boundaryTransitive_ball4`, `isBoundaryState_closedBall_iff`, `finrank_E4`, `preservesBody_isom4` | proved; controls S1, S2 |
| B1 | `flow_zero_of_add` | proved |
| B5 | `isEmpty_drivability_of_finite_orbits` | proved |
| B6 | none | excluded |
| verdict | `og1_infrastructure_core` | proved |

## Design evidence

The design runs before `F` are recorded in the preregistration: run 36961561241 (one proof error, `le_or_lt`), the
proof-only repair to blob `ea397e69` inside the frozen surface, run 36962242718 (Mathlib bridge job green) and the
predicted execution tree `dc340fb5` with run 36962546092 (all 32 jobs `success`). They are design evidence, not
attestations, and the pull-request runs on this branch are not attestations.

## What stays open

The hypotheses the route takes as inputs: a source for the sharp seed (P1), for the drive and its boundary
transitivity on the completion body (K∞-R), for seed-orbit availability (V4′), for dimension three, for the ellipsoid
normalization `T '' Ω = ball3`, for stage consistency (SC∞) and for ELEM; B6; and the K2, TR, CAR and SCL layer.
