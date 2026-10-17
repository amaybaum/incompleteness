# Reconstruction round GEOM-ODD-1 — does a relatively strictly convex, drivable token body of odd chart dimension at least five carry a native gate: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from `research/equivalence` (head `424aa33b`): `NOTES-E16.md` §3 with RESULTS rows
R-E16.1–R-E16.5, and `NOTES-E20.md` (S0, S0-b; "work in progress, deferred …; unverified; no result row") with its
probe runs `experiments/e20_odd_bodies.run1.*`, `.run2.*`; `NOTES-E21.md` does not bear on this residual. No design
module, probe or `controls.py` exists for it yet; the statement surface below is proposed and is fixed only by design
runs before `F`. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is
not a designation.

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
artifact, `verification/ROADMAP.md`, landed kernel module or other round's record changes under any outcome.**

## What the round is

**The residual** (R-E16.5, OPEN): "with K∞-Geom added (`SingletonFaces` or `RelStrictConvex`), does a drivable,
non-ellipsoidal token body of odd chart dimension `≥ 5` carry a native gate?" Its inputs: R-E16.1 (CONJECTURE, written
proof, exact instances) — for any body, `relC`, an invertible gate and an involution `N`, `N z = −z`, give
`(d + 1) tr H = (tr H)²`, so `tr H = 0` and `d` is odd (necessary, not sufficient); `not_even_of_relC`
(RelcSelectParity.lean:354) states it for `eball d`, reading the ball only through `toOp_actT`
(CompositeDimension.lean:464). R-E16.2 (CONJECTURE, [W] + [L]): a drive excludes `d = 1` (`not_drivable_Icc`,
KInfFoundations.lean:529) and gives the ellipsoid at `d = 3`. R-E16.3 (CONJECTURE): Ω_h (`d = 7`) meets every pair-level
clause and fails K∞-Geom.

**The gate form for a general body.** `IsNot Ω z N` (CompositeDimension.lean:210) and `NativeGate Ω z N G` (:218,
positivity in `maxCone Ω`, :186) are defined for every body; `dim_of_nativeGate` (:2723), `dim_of_ctrlGate`
(RelcSelectBlock.lean:739) and `dim_of_nativeGateOf` (K1Bridge.lean:128, which also takes K∞-Trans) are stated for
`eball d` and do not apply. K∞-Geom is tested as `RelStrictConvex Ω` (KInfFoundations.lean:144), which gives
`SingletonFaces Ω avail` (:139) for every family (:590); the converse needs supporting-effect completeness (:575).

**What E20 recorded, and no more** (HP-equivalence-17: "May not be assumed: any E20 or E21 conclusion"). Both runs end
`VERDICT NOT RENDERED -- failing: ['C4']`, the positive control `eball 3` `UNDECIDED(iterations)`; a debugging pass, not
a recorded run, corrected S0-b's diagnosis (margin `6.24·10⁻³`, violations ~`10⁻²`; LOG). Recorded: SF1 the count for
seven sector members; SF2 every member with `k ≥ 2` fails both forms of K∞-Geom on exact witnesses (the midpoint of two
pure sector-0 states is a boundary state; the proper effect `t₀` is certain on both); SF3 the `(3; 3, 3, 3)` gate meets
frame, `relT`, `relC` on all 144 basis tables, `G² = 1`, and `posFwd` on 26 exact product pairs; C2 66 exact midpoints
of Ω⋆⁵ strictly inside; C3 `dim F` 48 (`eball 3`), 288 (`eball 5`, Ω⋆⁵); C4 `eball 5`, Ω⋆⁵ `FEASIBLE(pool)` under
`posFwd` alone (float). Run 2's diagnostics, outside the verdict: both float candidates violate `posFwd` off the pool
(minima `−5.1·10⁻²`, `−5.5·10⁻¹`) and `posInv` on it (`−16.9`, `−33.4`).

**Consequences.** (1) The sector family is no search space for a countermodel: SF2's argument places every member with
`k ≥ 2` outside both forms of K∞-Geom and `k = 1` members are balls; it is the countercontrol that makes the K∞-Geom
check load-bearing (Ω_h carries a gate and fails it). (2) `posFwd` alone cannot see the ball's exclusion: `gSq_sep`
(RelcSelectSqueeze.lean:465) gives an exact map of `W 5` with the frame, `GateRel` and `posFwd`, failing `posInv`
(`gSq_not_posInv`, :451), for `n5 = diag(1, 1, −1, −1, −1)` and `z5` (ParityNot.lean:570, :573); E20's `eball 5` pair is
the image of `(z5, n5)` under the transposition of coordinates 3 and 5 [W], so E20's outcome B′ was unreachable. (3) The
linear layer does not decide: `gRev k` meets the frame and both relations on `eball (2k + 1)` (`gateRel_gRev`,
OddChar.lean:172) and fails `posFwd` for `k ≥ 1` (`not_posFwd_gRev`, :287). RELC-SELECT-1's C5 construction is one
`d = 5` witness, not a family: "`nC5` is a witness construction for this countermodel; it is not PARITY-NOT-1's `n5` …
and the balanced case is not decided" (its result note at `D`; two homogeneous signs `+1`, four `−1`). (4) Neither
direction is ready: no argument for strictly convex non-balls exists (DIM-1's block reduction reads the ball through
`corner_form` and `lor_cornerMap`, CompositeDimension.lean:1805, :1870), and no strictly convex candidate has exact
evidence for both positivity clauses. So the round is an exact-layer search, kernel follow-up only on a hit.

**An observation written in this draft (in no record; design item 1).** By R-E16.1 `N` has `(d + 1)/2` eigenvalues `−1`,
so `det N = (−1)^((d+1)/2)`, `−1` for `d ≡ 1 (mod 4)`, while a member of a drive's flow (a continuous one-parameter
group) has linear part of positive determinant: for `d = 5, 9, …` the gate's `N` is conjugate to no drive's NOT
(`nflip`, `d = 3`, and Ω_h's `N`, `d = 7`, have determinant `+1`). The probe records this per body.

- **Q-SECT (exact).** Do the probed sector members place as SF1–SF3 state, Ω_h's gate included?
- **Q-BODY (exact; one cell per search body `B`).** With `B`'s frozen `(z, N)`: does the frozen generator return a gate
  the exact verifier accepts (`HIT`), a frozen exclusion method an exact certificate (`EXCLUDED`), or neither?

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

## The exact layer (probe `verification/lean/geom_odd1_probe.py`, shard `probes_geomodd1`)

**Bodies.** `Ω_R(p, q; n) = {(X, S) ∈ ℝⁿ × ℝ : |S| ≤ 1, ‖X‖^(p+q) ≤ (1 + S)^p (1 − S)^q}`, chart dimension `D = n + 1`;
`Ω_R(1, 2; 4)` is E20's Ω⋆⁵, `Ω_R(1, 1; n)` is `eball (n + 1)`. Search set (proposed): `n ∈ {4, 6}`,
`(p, q) ∈ {(1, 2), (1, 3), (2, 3)}`, bodies `R12D5 … R23D7`; frozen pair: `N` fixes `S`, is `+1` on `X₁ … X_{(n−2)/2}`
and `−1` on the other `X`, `z = e_{n/2}` (E20's at `n = 4`). Controls: `eball 3` with `(z3, nflip)`; Ω_h with E16b's
`(z, N, G)`; `eball 5`, `eball 7` with the family's pair (`ne_five_of_nativeGate`, `ne_seven_of_nativeGate`,
CompositeDimension.lean:2736, :2741).
**Pools (exact).** States: rings `S = (t^(p+q) − 1)/(t^(p+q) + 1)`, `‖X‖ = 2t^p/(1 + t^(p+q))`, `t` rational, directions
on rational unit spheres; poles; interior points. Effects: supporting effects at pooled boundary points, certified on
the whole body by the weighted AM–GM bound `r(S) ≤ (p s^q (1 + S) + q s^(−p) (1 − S))/(p + q)`, tight at the ring point
for `s = 1/t`. A disjoint holdout pool, from a second frozen seed, is read by the verifier only. **Generator** (float,
pinned versions, seeds, caps) proposes `G`. **Verifier** (standard library, `Fraction`; calls nothing in the generator):
VL `G ∈ F` exactly (frame on the corner pairs; `relT`, `relC` on every basis table); VI the exact inverse; VP `posFwd`,
`posInv` `≥ 0` on every quadruple of both pools; VE every pool effect certified; VG `RelStrictConvex` on exact
midpoints, an SF2-type witness where it fails; VD the drive's fields at exact angles, `det N`, and whether `N` is
conjugate to the drive's NOT; VN six exact meridian points on no conic; VX `Entangling` (read by no rule).
**Controls.** C-POS: the parsed `cnot` and Ω_h's gate pass VL, VI, VP. C-NEG: `gSq`, `gSq.symm`, `gRev 2`, `gRev 3`
(transported to the family's pair) pass VL and fail VP; no generator candidate on `eball 5`, `eball 7` passes VP; VN
fails on both. C-SECT: Ω_h passes VL, VI, VP and fails VG. C-GEN: the generator on `eball 3`, Ω_h (read by no rule).
Countercontrols, each failing as stated: XG1 "`gSq` passes VP on `eball 5`"; XG2 "the identity meets the frame"; XG3
"Ω_h is relatively strictly convex at the probed midpoint"; XG4 "`(1 + z·x)/2` is a certified effect on `R12D5`" (it is
`41/40` at `X = (21/20)e₂`, `S = −1/3`). R: the shard runs the probe twice; outputs byte-identical.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Token | Rule |
|---|---|---|
| Q-SECT | `GEOM-ODD-SECTORS-OUTSIDE-GEOM` | the probe at `E`, run with `python3 -I`, prints PASS for SC1 (the count, seven members), SC2 (both K∞-Geom forms fail on exact witnesses, every member with `k ≥ 2`) and SC3 (Ω_h's and `(3; 3, 3, 3)`'s gates pass VL, `G² = 1` and VP on the exact product pool); XG3 fails as stated; R identical |
| Q-SECT | `GEOM-ODD-SECTORS-NOT-ESTABLISHED` | otherwise (no countermodel token: a member passing VG is a harness failure) |
| Q-BODY `B` | `GEOM-ODD-HIT-B` | C-POS, C-NEG, C-SECT print PASS, XG1–XG4 fail as stated, R identical, and for `B` a recorded rational `G` passes VL, VI, VP, VE, and `B` passes VG, VD (fields) and VN |
| Q-BODY `B` | `GEOM-ODD-EXCLUDED-B` | the same controls, and the frozen exclusion method prints an exactly verified certificate for `B`, for `eball 5` and for `eball 7`; struck before `F` if no method is frozen (design item 3) |
| Q-BODY `B` | `GEOM-ODD-UNDECIDED-B` | otherwise |

No rule reads another cell's outcome. `GEOM-ODD-1-READ` when the seven cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading, per token. SECTORS-OUTSIDE-GEOM: the probed sector members meet the count and fail relative strict
> convexity and full-effect singleton faces on exact witnesses; two carry gates meeting the linear clauses exactly and
> positivity on exact pools. HIT-B: for B with its frozen (z, N), an exact gate meets the frame and both relations on
> every basis table and both positivity clauses on the frozen exact pools, and B is relatively strictly convex on exact
> instances, meets the drive's fields at exact angles and is no ellipsoid by an exact conic test: a candidate for a
> kernel round. EXCLUDED-B: for B and its frozen (z, N), no linear equivalence of W D meets the native-gate clauses.

> Non-inference rule: this round does not show that OI supplies K∞-Geom, a drive, a NOT, a native gate or a token body
> of any shape; K∞-Geom is an open premise, entering only as a property of the probed bodies. A HIT is positivity on
> finitely many products and effects, not a native gate and not a countermodel; an EXCLUDED concerns one body with one
> (z, N). No outcome decides whether K∞-Geom with a drive and a native gate forces an ellipsoid or excludes chart
> dimension five or more. The count is necessary, not sufficient. The probe is not a Lean kernel proof.

**Premises this round does not source:** K∞-Geom (`RelStrictConvex`, `SingletonFaces`), `ElementaryDrivability`,
`IsNot`, `NativeGate`, the token body (K∞-Stage), and any identification of the gate's NOT with the drive's NOT.

## The controls (in `controls.py`)

- **S1 surface**: the probe blob at `E` is the frozen one and prints its frozen parameters. Mutations, each failing with
  its code: `posInv` dropped from VP (C-NEG fails on `gSq`); VE dropped (XG4 passes); VG dropped (C-SECT fails); the
  holdout pool dropped; a seventh body.
- **S2 resolution**: every cited name resolves at `D` to its line; `IsNot` has exactly the fields `unit invol preserves
  flips`, `NativeGate` exactly `frame posFwd posInv relT relC`; `cnot`, `gSq`, `gRev` are parsed from `D`, not re-typed.
- **S3 load-bearing**: C-POS (acceptance is attainable); C-NEG (each positivity clause is seen on exact kernel non-gates
  that pass the linear layer; VN is seen to fail); C-SECT (VG decides on a body carrying a gate); XG1–XG4; R.
- **S4 phrases** (header, result note): "OI supplies", "K∞-Geom is sourced", "forces an ellipsoid", "excludes d ≥ 5",
  "the residual is closed", "native gate exists" and "countermodel" (of a HIT), "kernel proof of" (for the probe),
  "design module", "not for merge". **V**: the seven tokens by the rules above. **G**: the governed paths above.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| no search body is run by the harness before `F` (E20's float runs of Ω⋆⁵ are prior and cited) | `C0`: the design runs cited in this file name control bodies only |
| the controls and the probe are the frozen ones, and replay | `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E`; `C3`: shard `probes_geomodd1` green with R identical, the aggregate job green |
| a HIT is not an artifact of thin pools or invalid effects | C-NEG, XG1, the VE lines and XG4 in the probe output at `E` |
| the change stays inside the governed paths; no manuscript changes | `C6`: `git diff --no-renames --name-status D E`; `C5` (G); `C4`: the release gate at `E` passing every step |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` |

## Design work required before F

1. Check the determinant observation (its written step; exact instances `d = 1 … 11`). Owner choice: must a HIT's `N`
   be conjugate to the drive's NOT? If so, `D = 5` is excluded a priori and the search set moves to `D ∈ {7, 11}`.
2. Build the probe from E20's run-2 harness (blob `ec95a697…`), re-deriving every E20 fact used, and add `posInv`, the
   holdout pool, VE (E20 checked its effects on pooled states only), VD, VN and the kernel gates parsed at `D`.
3. Choose a generator coupling `G` and `G⁻¹` (E20's cutting plane imposes `posFwd` alone): the involutive ansatz
   `G² = 1`, under which `posInv` is `posFwd`; an ansatz equivariant under the stabiliser of `(z, N)`; or sequential
   linearization. Freeze an exclusion method or strike `EXCLUDED`: none exists at `D` or on the research branch, and no
   general-body form of DIM-1's corner reduction is written. Owner choice: `Entangling` recorded only, or read by HIT.
4. Fix the search set, `t`-sets, seeds, pool sizes, caps, pinned `numpy`/`scipy` versions (as `probes_a42_*` pin theirs)
   and the time budget; classify each body's `(z, N)` pairs up to symmetry, or keep each cell relative to its pair;
   write `controls.py` with its self-test; run the harness on the controls only; build and dispatch the tree (`C0`).

## Stages and outcomes

Stages as KT4-PREM-1 (C1 `controls.py`; S1 the probe and the shard; S2 the result note = candidate `E`).
**`GEOM-ODD-1-READ`**: `controls.py check E --freeze F` OK, seven tokens printed, the exact-head run at `E` green on
every job. **`GEOM-ODD-1-HALTED`**: anything else (`S12`). A HIT's kernel follow-up is a new native round. No outcome
sources a premise or edits the ROADMAP or a manuscript; correctness bands unchanged (consistency axis).

