# PLANAR-TURN: exact search for a confined controlled transfer in Q (preregistration; not run)

**Standing.** A full preregistration, written under `PLAN.md` and chosen in `DESIGN.md`. It is
not run. Execution needs separate owner authorization
([#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306);
[c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480)
item 6). Before any run, this file is frozen by a commit that is an ancestor of the first
execution commit. Any change after that is made by a recorded amendment.

## 1. Object, class and hypotheses

- **Rule.** Q = `R_{2^16}` on `ℤ³`. It is run as RZ around `c = 2^15` (U1 Lemma 2.1; `|y| < 2^15`
  asserted at every tick). Every positive is re-run in Q mod `2^16` on representatives.
- **Lines.** Lines lie in the plane `z = 0` and carry U1's W2 background. The signal is the W2
  defect of U2 K0, launched on A toward the junction.
- **Geometries.** U2's planar junctions:
  - J1 corner: A = `{(x,0,0) : x ≤ 0}`, B = `{(0,y,0) : y ≥ 1}`;
  - J2 offset: A as in J1, B = `{(1,y,0) : y ≥ 1}`.
- **Gadget sites `K_r`.** The non-line sites of the plane `z = 0` within ℓ∞ distance `r` of the
  junction core. The core is `{(0,0,0)}` for J1 and `{(0,0,0), (1,1,0)}` for J2.
- **Gadget values.** One ternary value per site of `K_r`, in the signal component (U2's
  convention). The other component is held at 0.
- **Region.** `D = cl₂(A ∪ B ∪ K_r)`, which is planar (NU6(c)).
- **Class `𝒞`, three stages.**

  | Stage | Geometry, radius | Sites | Gadgets |
  |---|---|---|---|
  | 1 | J1, `r = 1` | 6 | `3^6` (replication of a subset of U2 F1) |
  | 2 | J2, `r = 1` | 10 | `3^10` |
  | 3 | J1, `r = 2` | 20 | every quiescent gadget (§3) |

  Each gadget is crossed with every B spatial phase (4) and every launch offset (4), which gives
  each arrival phase mod 4.
- **H1:** some member of `𝒞` realizes a controlled transfer (§2, outcome T).
- **H0 for `𝒞`:** none does.

By NU6(c), every planar transit confined in such a `D` is ternary at every tick. So `𝒞` is the set
of all planar confined junctions of these geometries and radii, with W2 signals.

## 2. Per-case outcomes (exact)

Each case receives exactly one outcome. Notation: `N(t)` is the no-input orbit; `S(t)` the signal
orbit; `ref(t)` the post-transit reference (the background on lines, the gadget's quiescent
orbit, with the same phase as `N(t)`; U2 K0). "Far B" is the set of sites of B at distance ≥ 8 from
the core.

- **Q-FAIL (not quiescent).** `N` is not confined, or `N(4) ≠ N(0)`. Exact.
- **BREACH.** In `S`, some site of `∂D` takes a current value outside `{−1, 0, 1}` at some tick
  `t ≤ T_max`. This is exact radiation at `t + 1` (NU4). The first breach tick and site are recorded.
- **T (transfer certified).** At some tick `T ≤ T_max`:
  - (i) `S(T)` equals `ref(T)` at every site outside far B;
  - (ii) on far B, `S(T)` equals the background plus one W2 glider whose window lies at distance
    `> 6 + w` from the core (`w` = glider window) and moves away from the core. This is checked
    by running the glider alone on a straight ring, as in U1 E1/E2, and comparing;
  - (iii) no breach up to `T`.

  Then the configuration for every `t ≥ T` is the superposition of `ref(t)` and the receding glider:
  - they are separated by more than the radius-1 light cone of one glider period;
  - `ref` is quiescent (Q-FAIL excluded), and the glider is exact on an infinite line (U1 E1/E2
    induction);
  - so the orbit stays confined in `D` for all time. Exact.
- **T-STATEFUL.** As T, but (i) holds with the gadget in a *different* quiescent state `g′`, which
  itself passes Q-FAIL's test. The lines are restored. Exact. This is reported separately.
- **R6-NULL.** A transfer whose output does not depend on the input: T or T-STATEFUL also occurs
  in the run with the signal launched *away* from the junction. Excluded from H1.
- **U (undetermined).** None of the above by `T_max = 2000` ticks.

## 3. Search procedure (frozen)

- **Stages 1–2.** Brute force over every ternary gadget. R1 (Q-FAIL) is tested first, on the
  no-input orbit over 4 ticks plus confinement.
- **Stage 3.** Exact enumeration of the quiescent gadgets by backtracking over the sites of
  `K_2`, in a fixed order. A partial assignment is pruned as soon as a site whose whole
  neighbourhood is assigned violates the 4-periodicity of `N` or the confinement of `∂D`. Its
  completeness is checked by control K6.
- **Each quiescent gadget.** Run `S` for every B phase and launch offset that it is quiescent
  for. Pruned at the first exact outcome.
- **Box.** Lines of length 200 on each side; a planar box with margin 3; the third dimension
  `|z| ≤ 2`. A breach (in particular any value off the plane) ends the case before any wrap-around
  can matter, because the margin exceeds one tick of propagation. This is asserted.

## 4. Controls and countercontrols (run first; any failure voids the verdict)

| Id | Kind | Requirement |
|---|---|---|
| K1 | positive control on Q itself | collinear junction (B continues A along `e₁`), empty gadget: outcome T at every launch offset. This exercises the T certificate on the native rule |
| K2 | positive control, classifier | U2's bent-line oracle O1 (the line rule run along A → corner → B, off-path held at 0): outcome T. U2's O2 (B cut off): no T |
| K3 | countercontrol | J1 plain corner, empty gadget, B phase 1: BREACH, at the tick and site of U2 D1 (`t = 28`, the inner-corner kick) |
| K4 | countercontrol | dead end (A only): BREACH (U2 N2) |
| K5 | countercontrol | the linear member `L_{2^16, 3^{−1}}`, same initial states: no T (U2 N4) |
| K6 | completeness of the stage-3 enumeration | on `K_1` of J1, backtracking returns exactly the quiescent set found by brute force in stage 1 |
| K7 | NU4 consistency | in every BREACH case, the next tick has a non-background value outside `D` and none before. A violation is an implementation error and voids the run |
| K8 | replication | at U2's launch offset, the stage-1 quiescent set equals the ternary subset of U2 F1's quiescent set, recomputed with the functions of U2's `checks/univ2_checks.py` on `main` |
| K9 | signal-away | for every T or T-STATEFUL case, the signal-away run is executed (R6) |

## 5. Decision rule (fixed now; verdict text generated from the counts)

- If any control fails: **VOID**; no verdict.
- If at least one case is T or T-STATEFUL, is not R6-NULL, and holds when re-run in Q mod `2^16`:
  **H1 supported**. The cases are listed, with their certificates, and the T and T-STATEFUL
  counts are reported separately.
- Else, if every case is Q-FAIL, BREACH or R6-NULL: **H0 for `𝒞`**, exact.
- Else (some cases U, no H1): **INCONCLUSIVE**, with the U count and the stage of each U case.

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| Preregistration before the run | this file's commit is an ancestor of the first execution commit; the execution changes nothing in this directory except new result files |
| Enumeration complete | stage 1: `3^6` cases; stage 2: `3^10`; stage 3: K6. All asserted |
| Exact arithmetic within the embedding | integer arrays; `|y| < 2^15` asserted each tick; every positive re-run in Q mod `2^16` |
| BREACH is exact radiation | K7 |
| The T certificate is exact | asserted separation `> 6 + w`; glider certified on a ring as in U1 E1/E2; K1 and K2 |
| No wrap-around | the margin assertion of §3; any off-plane value is a breach first |
| Component restriction is lossless for transfer | cited (U2 A1, F1 NU1); the other component asserted 0 at every tick |
| Determinism | a replay is byte-identical |
| Controls precede the verdict | the verdict is printed only after K1–K9 hold |

## 7. Cost class (§A.40)

- **Stages 1–2.** Bounded: 729 + 59 049 gadgets. Most are pruned at R1 within 4 ticks; the
  quiescent ones run to at most 2000 ticks on a planar box. Minutes to an hour on one core.
- **Stage 3.** CI: the backtracking enumeration, then the signal runs, sharded by B phase and
  launch offset in a matrix.
- **Authorization.** Both need it (§A.43 item 4 for the dispatch).

## 8. What it would and would not establish

- **Would:**
  - *H1:* an exact native controlled transfer in Q. This is the missing block of U1 (N), at the
    standing of an exact computation plus the written certificate argument.
  - *H0:* the exact absence of controlled transfers among *all* planar confined junctions of the
    stated geometries and radii with W2 signals. That holds for every gadget value, not only
    ternary ones, because of NU6(c).
  - *INCONCLUSIVE:* the U cases, which identify where confined ringing occurs.
- **Would not:**
  - universality of Q, even under H1: gate, fan-out, composition, and an encoding with a
    correctness argument under Definition U are still needed;
  - anything about non-planar regions, larger radii, J3, other signal types or other backgrounds;
  - native preparation of the designed lines and gadgets (Goal C);
  - BQP capability or any quantum operation;
  - anything about NU8 or other comparison rules.
