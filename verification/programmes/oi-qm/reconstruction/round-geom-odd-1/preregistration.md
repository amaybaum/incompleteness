# Reconstruction round GEOM-ODD-1 — does a relatively strictly convex, drivable token body of odd chart dimension at least five carry a native gate: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`, revised under the owner's decision on PR #830 (comment 6254707076: keep the drive-NOT identification, no
outcome that rules a gate out, a controls-only preflight first). It is built from `research/equivalence` (head `424aa33b`):
`NOTES-E16.md` §3 with RESULTS rows R-E16.1–R-E16.5, and `NOTES-E20.md` (S0, S0-b; "work in progress, deferred …;
unverified; no result row") with its probe runs `experiments/e20_odd_bodies.run1.*`, `.run2.*`; `NOTES-E21.md` does
not bear on this residual. Those files are provenance: every fact the design uses from them is re-derived by the
preflight or the probe. The preflight's code exists on a staging branch (below); no probe or `controls.py` exists yet.
Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round GEOM-ODD-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-geom-odd-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-geom-odd-1/
record AM verification/receipts/GEOM-ODD-1.json
execution A verification/lean/geom_odd1_probe.py
execution M .github/workflows/verify.yml
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory; **no manuscript, built
artifact, `verification/ROADMAP.md`, landed kernel module or other round's record changes under any outcome.** Every
citation below is a coordinate at `main` `501331f58e856019173d7246a8c4de7d4aec752d`; the kernel files cited and
round RELC-SELECT-1's records are identical at `D` and at `main`.

## What the round is

**The residual** (R-E16.5, OPEN): "with K∞-Geom added (`SingletonFaces` or `RelStrictConvex`), does a drivable,
non-ellipsoidal token body of odd chart dimension `≥ 5` carry a native gate?" Its inputs: R-E16.1 (CONJECTURE, written
proof, exact instances) — for any body, `relC`, an invertible gate and an involution `N`, `N z = −z`, give
`(d + 1) tr H = (tr H)²` for `H = homMap N` on `HVec d = ℝ^(d+1)`, so `tr H = 0` and `d` is odd (necessary, not
sufficient); `not_even_of_relC` (RelcSelectParity.lean:354) states it for `eball d`, through the balance
`finrank_plus_eq_finrank_minus_relC` (:329) of `H`'s eigenspaces (CompositeDimension.lean:257), reading the ball only
through `toOp_actT` (CompositeDimension.lean:464). R-E16.2 (CONJECTURE, [W] + [L]): a drive excludes `d = 1`
(`not_drivable_Icc`, KInfFoundations.lean:529) and gives the ellipsoid at `d = 3`. R-E16.3 (CONJECTURE): Ω_h (`d = 7`)
meets every pair-level clause and fails K∞-Geom.

**The gate form for a general body.** `IsNot Ω z N` (CompositeDimension.lean:210) and `NativeGate Ω z N G` (:218,
positivity in `maxCone Ω`, :186) are defined for every body; `dim_of_nativeGate` (:2723), `dim_of_ctrlGate`
(RelcSelectBlock.lean:739) and `dim_of_nativeGateOf` (K1Bridge.lean:128, which also takes K∞-Trans) are stated for
`eball d` and do not apply. K∞-Geom is tested as `RelStrictConvex Ω` (KInfFoundations.lean:144), which gives
`SingletonFaces Ω avail` (:139) for every family (:590); the converse needs supporting-effect completeness (:575).

**What E20 recorded, and no more** (its handoff state, HP-equivalence-17 on the research branch: "May not be assumed:
any E20 or E21 conclusion"). Both runs end `VERDICT NOT RENDERED -- failing: ['C4']`, the positive control `eball 3`
`UNDECIDED(iterations)`; a debugging pass, not a recorded run, corrected S0-b's diagnosis (margin `6.24·10⁻³`,
violations ~`10⁻²`; LOG). Recorded: SF1 the count for seven sector members; SF2 every member with `k ≥ 2` fails both
forms of K∞-Geom on exact witnesses (the midpoint of two pure sector-0 states is a boundary state; the proper effect
`t₀` is certain on both); SF3 the `(3; 3, 3, 3)` gate meets frame, `relT`, `relC` on all 144 basis tables, `G² = 1`,
and `posFwd` on 26 exact product pairs; C2 66 exact midpoints of Ω⋆⁵ strictly inside; C3 `dim F` 48 (`eball 3`), 288
(`eball 5`, Ω⋆⁵); C4 `eball 5`, Ω⋆⁵ `FEASIBLE(pool)` under `posFwd` alone (float). Run 2's diagnostics, outside the
verdict: both float candidates violate `posFwd` off the pool (minima `−5.1·10⁻²`, `−5.5·10⁻¹`) and `posInv` on it
(`−16.9`, `−33.4`).

**Consequences.** (1) The sector family is no search space for a countermodel: SF2's argument places every member with
`k ≥ 2` outside both forms of K∞-Geom and `k = 1` members are balls; it is the countercontrol that makes the K∞-Geom
check load-bearing (Ω_h carries a gate and fails it). (2) `posFwd` alone cannot see the ball's lack of a gate:
`gSq_sep` (RelcSelectSqueeze.lean:465) gives an exact map of `W 5` with the frame, `GateRel` and `posFwd`, failing
`posInv` (`gSq_not_posInv`, :451), for `n5 = diag(1, 1, −1, −1, −1)` and `z5` (ParityNot.lean:570, :573); E20's
`eball 5` pair is the image of `(z5, n5)` under the transposition of coordinates 3 and 5 [W], so E20's outcome B′ was
unreachable. No certificate built on `posFwd` alone can rule a gate out, and none using `posInv` is written, so this
round has no outcome that rules a gate out. (3) The linear layer does not decide: `gRev k` meets the frame and both
relations on `eball (2k + 1)` (`gateRel_gRev`, OddChar.lean:172) and fails `posFwd` for `k ≥ 1` (`not_posFwd_gRev`,
:287). RELC-SELECT-1's C5 construction is one `d = 5` witness, not a family: "`nC5` is a witness construction for this
countermodel; it is not PARITY-NOT-1's `n5` …" (its result.md:45–46; two homogeneous signs `+1`, four `−1`). (4) Neither
direction is ready: no argument for strictly convex non-balls exists (DIM-1's block reduction reads the ball through
`corner_form` and `lor_cornerMap`, CompositeDimension.lean:1805, :1870), and no strictly convex candidate has exact
evidence for both positivity clauses. So the round is an exact-layer search, kernel follow-up only on a hit.

**The drive-NOT identification, and the dimensions it leaves.** This design requires a HIT's `N` to be the drive's NOT,
`ElementaryDrivability.N = flow t₀` (KInfFoundations.lean:279; the structure :264), up to an affine conjugation. That
is a restriction of the design, chosen to keep the question the owner posed; it is not a theorem about geometry or
about native gates, and ROADMAP.md:68's "one common NOT" (one `N` in both copies' relations, as `NativeGate` states it)
does not imply it. Under three stated assumptions it leaves only `d ≡ 3 (mod 4)`:

- (i) the count: `H = homMap N` has `(d + 1)/2` eigenvalues `−1`, so `N` has `(d + 1)/2` eigenvalues `−1` and
  `(d − 1)/2` eigenvalues `+1` on the chart and `det N = (−1)^((d+1)/2)` (a kernel theorem for `eball d`; R-E16.1's
  written argument for other bodies);
- (ii) the body has nonempty interior, so an affine map involutive on it is involutive on the chart;
- (iii) the identification itself.

The flow is continuous with `flow 0` the identity, so the determinant of `flow t`'s linear part is a continuous,
nowhere-zero function of `t` equal to `1` at `0`, hence positive; by (ii) `flow t₀` is an involution, so its
determinant is `+1`. By (iii) `det N = +1`, so `(d + 1)/2` is even. Exact instances: `nflip` (`d = 3`), Ω_h's
`1 ⊕ nflip ⊕ nflip` (`d = 7`) and the family's pair at `n = 6` have determinant `+1`; `n5` and the family's pair at
`n = 4` (`d = 5`) have `−1`. The first eligible dimension is therefore 7, then 11. **This first attempt is
dimension 7 only**; dimension 11 is outside it.

- **Q-SECT (exact).** Do the probed sector members place as SF1–SF3 state, Ω_h's gate included?
- **Q-BODY (exact; one cell per search body `B`).** With `B`'s frozen `(z, N)`: does the frozen generator return a gate
  the exact verifier accepts (`HIT`), or not within the frozen cap (`UNDECIDED`)?

## The proposed statement surface

No kernel module is added. The probe also encodes `Entangling`, `cnot`, `z3`, `nflip` (CompositeDimension.lean:229,
:775, :793, :797), `ElementaryDrivability` (KInfFoundations.lean:264), `eball` (TransitiveBody.lean:518), `gSq`
(RelcSelectSqueeze.lean:154), `nK`, `gRev` (OddChar.lean:56, :62). A later round's target (not frozen, not built, no
written proof; with `dim_of_nativeGate` it needs a transport of `IsNot`, `NativeGate` along affine maps, absent at `D`):

```lean
theorem odd_geom_drive_gate_ellipsoid (hd : 5 ≤ d) (hc : IsCompact Ω) (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) (hG : RelStrictConvex Ω) (hD : Nonempty (ElementaryDrivability Ω))
    (hN : IsNot Ω z N) (hT : NativeGate Ω z N T) : ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d
```

## The controls-only preflight (before any dimension-7 work; design evidence)

Run before anything else, in CI, by dispatch only. **It runs no search body** (`C0`).

- **Files.** On the staging branch, in this record directory under `preflight/`:
  - `controls_verify.py` (sha256 `e6f3fcbc518bf3f58a4bc55f4d9bd22ee567a3a8d6d3ec98ae1437aa77ea0763`), the exact
    verifier: standard library, `Fraction`, imports nothing from the generator;
  - `controls_gen.py` (sha256 `df7e640c271c2f597744a14811fe3afab17fd79f64367d1542a70ee48d56b855`), the generator:
    numpy 2.4.6 and scipy 1.17.1 (HiGHS), told `z`, `N` and pool A, never a gate;
  - `run_control.py` (sha256 `3faa0fdfbe4b3d8c2da37ed99420cb5f459c5ffc704600e0ccc362dc526006b9`), the capped driver.

  The workflow is `.github/workflows/geom-odd-1-controls.yml` (sha256
  `41fc9da266d4b0990023995a5b3ea3754912e6a2a09935c7afce000cdab9bde1`) on the staging branch only.
- **Controls.** `eball3`: `eball 3`, `(z3, nflip)` parsed from the kernel, reference gate the parsed `cnot`. `omegah`:
  E16b's Ω_h, `z = (0, e₃, 0)`, `N = 1 ⊕ nflip ⊕ nflip`, reference gate `(Φ ⊗ Φ)(cnot on every sector block)(Φ ⊗ Φ)⁻¹`.
  Pools: pure states and sharp effects from rational unit vectors, two disjoint seeded draws, A (the generator's) and B
  (the holdout, read by the verifier only).
- **Generator.** `F` solved exactly (the free pattern of `relT`, `relC` and the frame); `posFwd` on pool A by
  constraint generation; G and H = G⁻¹ sought in `F` by multi-start alternating L1 minimisation of `|GH − 1|` over the
  `posFwd` polytope; a converged point rounded to a rational `G ∈ F`.
- **Exact verification.** VS pooled states in the body; VE pooled effects certified on the whole body (the ball's
  effect inequalities; for Ω_h, the convex hull of its two sector balls, so per sector); VL the frame, `relT`, `relC`
  as matrix identities; VI an exact inverse; VP `posFwd` and `posInv` on every quadruple of pools A and B. Equality
  with the reference gate is recorded and decides nothing: `cnot ∘ (Z-rotation on the control)` is a distinct gate
  meeting every clause. The verifier's own controls run first (`--self-test`) and must pass: each reference gate passes;
  the identity fails the frame; `ref ∘ (1 ⊗ K₂)` fails `posFwd` only and `ref ∘ (1 ⊗ K_{1/2})` fails `posInv` only (`K_s`
  scales the chart coordinates orthogonal to the corner line by `s`); a non-effect fails VE; an outside state fails VS.
- **Cap.** 1200 s wall clock per control, covering pool emission, generation and verification, measured by
  `run_control.py` on a monotonic clock (the generator is killed at the cap less a 240 s verification reserve, the
  verifier at the cap), with `timeout --signal=KILL 1260` and the job's `timeout-minutes: 30` as backstops. The two
  controls run as two jobs.
- **Rule.** A control passes iff the verifier prints `PASS` on the generator's candidate within its cap. If either
  control fails, the round parks: no dimension-7 attempt and no `F`. Both results are retained (§A.42 below) and their
  sha256 pinned in this file before any further design step.

**If both pass**, the next step is a dimension-7 feasibility design, written then and not here: the search bodies at
`n = 6` only, a dispatch-only shard of `verify.yml` (`if: github.event_name == 'workflow_dispatch'`, as the A42
exclusion shards run), and a frozen wall-clock cap per body, a timeout reading `UNDECIDED-B`. Its cost measurements use
the dimension-7 controls (Ω_h, `eball 7`) only, keeping `C0`.

## The exact layer (probe `verification/lean/geom_odd1_probe.py`, shard `probes_geomodd1`, dispatch only)

**Bodies.** `Ω_R(p, q; n) = {(X, S) ∈ ℝⁿ × ℝ : |S| ≤ 1, ‖X‖^(p+q) ≤ (1 + S)^p (1 − S)^q}`, chart dimension `D = n + 1`;
`Ω_R(1, 2; 4)` is E20's Ω⋆⁵, `Ω_R(1, 1; n)` is `eball (n + 1)`. Search set (proposed): `n = 6`,
`(p, q) ∈ {(1, 2), (1, 3), (2, 3)}`, bodies `R12D7`, `R13D7`, `R23D7`; frozen pair: `N` fixes `S`, is `+1` on `X₁, X₂`
and `−1` on `X₃ … X₆`, `z = e₃`. Its drive: the simultaneous rotation of the planes `(X₃, X₄)` and `(X₅, X₆)`, whose
member at `t₀ = π` is `N`. Controls: the preflight's two, with their verifier self-test; `eball 7` with the family's
pair (`ne_seven_of_nativeGate`, CompositeDimension.lean:2741).
**Pools (exact).** States: rings `S = (t^(p+q) − 1)/(t^(p+q) + 1)`, `‖X‖ = 2t^p/(1 + t^(p+q))`, `t` rational, directions
on rational unit spheres; poles; interior points. Effects: supporting effects at pooled boundary points, certified on
the whole body by the weighted AM–GM bound `r(S) ≤ (p s^q (1 + S) + q s^(−p) (1 − S))/(p + q)`, tight at the ring point
for `s = 1/t`. A disjoint holdout pool, from a second frozen seed, is read by the verifier only. **Generator** (float,
pinned versions, seeds, caps) proposes `G`. **Verifier** (standard library, `Fraction`; calls nothing in the generator):
VL `G ∈ F` exactly (frame on the corner pairs; `relT`, `relC` on every basis table); VI the exact inverse; VP `posFwd`,
`posInv` `≥ 0` on every quadruple of both pools; VE every pool effect certified; VG `RelStrictConvex` on exact
midpoints, an SF2-type witness where it fails; VD the drive's fields at exact angles and `det N = +1`; VN six exact
meridian points on no conic; VX `Entangling` (read by no rule).
**Controls.** C-POS: the parsed `cnot` and Ω_h's gate pass VL, VI, VP, and the generator recovers an accepted gate on
each within the preflight's cap. C-NEG: `gSq`, `gSq.symm` (on `eball 5`, the kernel's exact countercontrol for `posInv`),
`gRev 3` (transported to the family's pair on `eball 7`) and the two squeezed reference gates pass VL and fail VP as the
preflight states; no generator candidate on `eball 7` passes VP; VN fails on `eball 7`. C-SECT: Ω_h passes VL, VI, VP
and fails VG. Countercontrols, each failing as stated: XG1 "`gSq` passes VP on `eball 5`"; XG2 "the identity meets the
frame"; XG3 "Ω_h is relatively strictly convex at the probed midpoint"; XG4 "`(1 + z·x)/2` is a certified effect on
`R12D7`" (it is `41/40` at `X = (21/20)e₃`, `S = −1/3`, a state as `(21/20)³ = 9261/8000 ≤ 32/27`); XG5 "the drive with
the `(X₁, S)` plane in place of `(X₃, X₄)` preserves `R12D7`". R: the shard runs the probe twice; outputs
byte-identical.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Token | Rule |
|---|---|---|
| Q-SECT | `GEOM-ODD-SECTORS-OUTSIDE-GEOM` | the probe at `E`, run with `python3 -I`, prints PASS for SC1 (the count, seven members), SC2 (both K∞-Geom forms fail on exact witnesses, every member with `k ≥ 2`) and SC3 (Ω_h's and `(3; 3, 3, 3)`'s gates pass VL, `G² = 1` and VP on the exact product pool); XG3 fails as stated; R identical |
| Q-SECT | `GEOM-ODD-SECTORS-NOT-ESTABLISHED` | otherwise (no countermodel token: a member passing VG is a harness failure) |
| Q-BODY `B` | `GEOM-ODD-HIT-B` | C-POS, C-NEG, C-SECT print PASS, XG1–XG5 fail as stated, R identical, and for `B` a recorded rational `G` passes VL, VI, VP, VE, and `B` passes VG, VD and VN |
| Q-BODY `B` | `GEOM-ODD-UNDECIDED-B` | otherwise, including a generator that reaches its frozen cap |

No rule reads another cell's outcome. `GEOM-ODD-1-READ` when the four cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`. A verdict over a failed control is void and the round halts.

## What each positive token credits, and its countercontrol

| Token | Credited clause | Countercontrol (the reading fails without it) |
|---|---|---|
| `SECTORS-OUTSIDE-GEOM` | SC2's exact witnesses | XG3: Ω_h, which carries a gate, is not relatively strictly convex |
| | SC3's positivity | the squeezed Ω_h gates (VP fails on each in turn) |
| `HIT-B` | VP `posInv` | `gSq` on `eball 5` and `ref ∘ (1 ⊗ K_{1/2})` pass VL and `posFwd` and fail `posInv` |
| | VP `posFwd` | `gRev 3`, `ref ∘ (1 ⊗ K₂)` |
| | VL frame | XG2 |
| | VE | XG4 |
| | VG | C-SECT, XG3 |
| | VD | XG5 |
| | VN | `eball 7`, an ellipsoid, fails VN |
| | the generator's recovery | the preflight's two controls |

The count (SC1) is necessary, not sufficient, and credits no reading. `UNDECIDED-B` and `SECTORS-NOT-ESTABLISHED` are
not positive tokens.

## The earned reading and the non-inference rule (frozen)

> Earned reading, per token. SECTORS-OUTSIDE-GEOM: the probed sector members meet the count and fail relative strict
> convexity and full-effect singleton faces on exact witnesses; two carry gates meeting the linear clauses exactly and
> positivity on exact pools. HIT-B: for B with its frozen (z, N), an exact gate meets the frame and both relations on
> every basis table and both positivity clauses on the frozen exact pools, and B is relatively strictly convex on exact
> instances, meets the drive's fields at exact angles and is no ellipsoid by an exact conic test: a candidate for a
> kernel round. UNDECIDED-B: within the frozen cap and over green controls, the generator returned no gate the verifier
> accepts; nothing about B follows.

> Non-inference rule: this round does not show that OI supplies K∞-Geom, a drive, a NOT, a native gate or a token body
> of any shape; K∞-Geom is an open premise, entering only as a property of the probed bodies. A HIT is positivity on
> finitely many products and effects, not a native gate and not a countermodel, and stays relative to its pools. A
> timeout over green controls supports UNDECIDED only. No outcome decides whether K∞-Geom with a drive and a native gate
> forces an ellipsoid or rules out chart dimension five or more. The restriction to `d ≡ 3 (mod 4)` is this design's,
> under assumptions (i)–(iii). The count is necessary, not sufficient. The probe is not a Lean kernel proof.

**Premises this round does not source:** K∞-Geom (`RelStrictConvex`, `SingletonFaces`), `ElementaryDrivability`,
`IsNot`, `NativeGate`, the token body (K∞-Stage), and the identification of the gate's NOT with the drive's NOT.

## The controls (in `controls.py`)

- **S1 surface**: the probe blob at `E` is the frozen one and prints its frozen parameters. Mutations, each failing with
  its code: `posInv` dropped from VP (C-NEG fails on `gSq`); VE dropped (XG4 passes); VG dropped (C-SECT fails); the
  holdout pool dropped; a fourth body; a body at `n = 4` or `n = 10`; the cap removed.
- **S2 resolution**: every cited name resolves at `D` to its line; `IsNot` has exactly the fields `unit invol preserves
  flips`, `NativeGate` exactly `frame posFwd posInv relT relC`; `cnot`, `gSq`, `gRev` are parsed from `D`, not re-typed;
  the preflight files have the sha256 pinned above.
- **S3 load-bearing**: C-POS (acceptance is attainable and recovered); C-NEG (each positivity clause is seen on exact
  non-gates that pass the linear layer; VN is seen to fail); C-SECT (VG decides on a body carrying a gate); XG1–XG5; R.
- **S4 phrases** (header, result note): "OI supplies", "K∞-Geom is sourced", "forces an ellipsoid", "rules out d ≥ 5",
  "no gate exists", "the residual is closed", "native gate exists" and "countermodel" (of a HIT), "kernel proof of"
  (for the probe), "design module", "not for merge". **V**: the four tokens by the rules above. **G**: the governed
  paths above.

## Evidence retention (§A.42)

Expected-result JSON only (deterministic fields; the run, job and digest of the text read), under `evidence/` in the
record directory, outside `amendments/`; no raw log.

- `evidence/preflight-eball3.json`, `evidence/preflight-omegah.json`: each control's `result-*.json` and `verify-*.json`
  from the dispatched run's artifacts, with the candidate's sha256, the commit dispatched and the recipe (dispatch of
  `geom-odd-1-controls.yml` at that commit). Pinned by sha256 in this file before any dimension-7 design.
- The dimension-7 design runs and `F`'s exact-head run: committed by the first execution commit, the design runs
  pinned here before `F`.
- `E`'s exact-head run: an evidence-retention pull request to `main` before the reconciliation; the receipt's
  candidate entry for `E` names its digest.
- If the round parks, no execution commit exists to carry the preflight evidence; how it reaches `main` is an owner
  decision recorded on the guiding pull request.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| no search body is run by the harness before `F` (E20's float runs of Ω⋆⁵ are prior and cited) | `C0`: the preflight and design runs cited in this file name control bodies only |
| the preflight run is of the pinned files, and both controls passed within their caps | `C8`: the four sha256 pins above against the dispatched commit's blobs; the two retained results with `outcome: PASS`, `cap_seconds: 1200` |
| the controls and the probe are the frozen ones, and replay | `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E`; `C3`: shard `probes_geomodd1` green on the dispatch run at `E` with R identical, the aggregate job green |
| the shard runs only on dispatch, under its frozen cap | `C9`: the shard's `if:` and `timeout` lines in `verify.yml` at `E` |
| a HIT is not an artifact of thin pools or invalid effects | C-NEG, XG1, the VE lines and XG4 in the probe output at `E` |
| the change stays inside the governed paths; no manuscript changes | `C6`: `git diff --no-renames --name-status D E`; `C5` (G); `C4`: the release gate at `E` passing every step |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` |

## Design work required before F

1. Dispatch the controls-only preflight on a disposable branch; retain and pin its two results. If either control
   fails, the round parks here.
2. If both pass: write the dimension-7 feasibility design (above) and measure its cost on the dimension-7 controls.
3. Build the probe from E20's run-2 harness (sha256 `ec95a697…`, git blob `34485203`), re-deriving every E20 fact used,
   and add `posInv`, the holdout pool, VE (E20 checked its effects on pooled states only), VD, VN, the preflight's
   verifier and the kernel gates parsed at `D`. Owner choice: `Entangling` recorded only, or read by HIT.
4. Fix the `t`-sets, seeds, pool sizes, caps and pinned `numpy`/`scipy` versions (as `probes_a42_*` pin theirs);
   classify each body's `(z, N)` pairs up to symmetry, or keep each cell relative to its pair; write `controls.py` with
   its self-test; build and dispatch the tree (`C0`).

## Stages and outcomes

Stages as KT4-PREM-1 (C1 `controls.py`; S1 the probe and the shard; S2 the result note = candidate `E`).
**`GEOM-ODD-1-READ`**: `controls.py check E --freeze F` OK, four tokens printed, the exact-head run at `E` green on
every job. **`GEOM-ODD-1-HALTED`**: anything else (`S12`). A HIT's kernel follow-up is a new native round. No outcome
sources a premise or edits the ROADMAP or a manuscript; correctness bands unchanged (consistency axis).
