# PLANAR-TURN: exact search for a leak-free controlled transfer in Q (preregistration; not run)

**Standing.** A full preregistration, written under `PLAN.md` and chosen in `DESIGN.md`. It is
not run. Execution needs separate owner authorization
([#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306);
[c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480)
item 6). Before any run, this file is frozen by a commit that is an ancestor of the first
execution commit; any later change is made by a recorded amendment. This revision answers review
[#1515 c.7066725317](https://github.com/amaybaum/incompleteness/pull/1515#issuecomment-7066725317)
(R1–R3, n1–n3).

## 1. Object, class and hypotheses

- **Rule.** Q = `R_{2^16}` on `ℤ³`, run as RZ around `c = 2^15` (U1 Lemma 2.1; `|y| < 2^15` asserted
  every tick). Every positive is re-run in Q mod `2^16`.
- **Lines and signal.** Lines lie in the plane `z = 0` and carry U1's W2 background. The signal is
  U2 K0's W2 defect, launched on A toward the junction at distance 8.
- **Geometries.**
  - J1 corner: A = `{(x,0,0) : x ≤ 0}`, B = `{(0,y,0) : y ≥ 1}`.
  - J2 offset: A as in J1, B = `{(1,y,0) : y ≥ 1}`.
- **Gadget sites `K_r`.** The non-line sites of `z = 0` within ℓ∞ distance `r` of the core:
  `{(0,0,0)}` for J1, `{(0,0,0),(1,1,0)}` for J2. Each carries one ternary value in the signal
  component; the other component is held at 0 (lossless for transfer: U2 A1, F1 NU1).
- **Allowed region (changed, R1).** `A_r = A ∪ B ∪ K_r`, U2's definitional region. It is finite
  near the junction and is **not** closed.
  - The closed hull `cl₂(A ∪ B ∪ K_r)` of a bent junction is not finite. For J1 the inner-corner
    site `(−1,1,0)` has neighbours `(−1,0,0) ∈ A` and `(0,1,0) ∈ B`, then `(−2,1,0)` has
    `(−2,0,0)` and `(−1,1,0)`, and so on. The closure fills the planar quadrant
    `{x ≤ −1, y ≥ 1, z = 0}`; J2's fills a sector likewise (reviewer's derivation, checked here).
  - Confinement in that sector would permit ternary disturbance throughout an infinite region.
    It is not used.
  - **Leak-freeness.** A run is *leak-free* when no site outside `A_r` ever differs from `c`.
    That is U2's R3 criterion with `R⁺` replaced by `K_r`.
- **Ternarity a fortiori.** If a run is leak-free, the support stays in `A_r ⊂ D := cl₂(A_r)`. So
  `D` is never breached (NU4′, ⇒), `D` is planar, `∂D = D`, and every value is ternary at every
  tick (NU6(c)). Ternary gadget values therefore lose nothing in this class.
- **Class `𝒞`** (no-input orbits that emit along a line, Q-EMIT, are excluded; §3).
  - Stage 1: J1, `r = 1` (6 sites).
  - Stage 2: J2, `r = 1` (10 sites).
  - Stage 3: J1, `r = 2` (20 sites).
  - In every stage: every ternary gadget whose no-input orbit is leak-free, *of any period*
    (changed, R3); every B spatial phase; every relative arrival phase (§3).
- **H1:** some member of `𝒞` realizes a leak-free controlled transfer (outcome T or T-STATEFUL,
  not R6-NULL).
- **H0 for `𝒞`:** none does.

## 2. Per-case outcomes

Notation: `N(t)` is the no-input orbit of a gadget `g` (period `P`); `S(t)` the signal orbit;
"far B" the sites of B at distance ≥ 8 from the core.

- **Q-LEAK.** `N` leaks. Exact (the first leaking tick and site are recorded). Excluded from `𝒞`.
- **LEAK.** In `S`, some site outside `A_r` differs from `c` at a tick `t ≤ T_max`. Exact. Its
  sub-cases are recorded: whether the site is in the sector `D ∖ A_r` (in-plane ternary spreading)
  or off the plane, and whether a breach of `D` occurred (NU4).
- **T (transfer, restored).** At some tick `T ≤ T_max`:
  - (i) on `K_r` and on A and on B outside far B, `S(T)` equals `N(T + δ)` for some
    `δ ∈ {0, 4, …, P − 4}`. The joint period `P` is a multiple of 4, since the lines are
    4-periodic, so `N(T + δ)` has the lines at their phase at `T`. A gadget that returns to its own
    orbit at another phase, with the lines in phase, is a different leak-free no-input orbit and is
    counted as T-STATEFUL;
  - (ii) on far B, `S(T)` is the background plus one W2 glider whose window lies at distance
    `> 6 + w` from the core and moves away, certified against a straight-ring reference
    (U1 E1/E2);
  - (iii) no LEAK up to `T`.

  Then for all `t ≥ T` the configuration is the superposition of `N(t + δ)` and the receding
  glider: they are separated by more than the light cone of one glider period, `N` is leak-free
  and periodic, and the glider is exact on an infinite line (U1 E1/E2). This is exact; the line-end
  handling of §3 makes the finite run equal the `ℤ³` run on every site that is checked.
- **T-STATEFUL.** As T, but in (i) the gadget equals a different leak-free no-input orbit `N′`
  (any period).
- **R6-NULL.** T or T-STATEFUL also occurs with the signal launched away from the junction.
  Excluded from H1.
- **U (undetermined).** None of the above by `T_max = 2000`. Examples are confined ringing,
  reflected signals still on the lines, or a gadget that has not returned.

## 3. Procedure, box and line ends (changed, R2)

- **No-input orbits (all stages; changed, R1′).** Let `Z_r` be the line sites within distance
  `r + 2` of the core (the near-line zone). For each gadget, run `N` and stop at the first of:
  - (a) **return:** the *full* simulated state equals its initial state at every site within the
    read zone (distance `L − t`), on `K_r` and on all line sites. This gives the exact period `P`;
  - (b) **Q-LEAK:** a site outside `A_r` leaves `c`;
  - (c) **Q-EMIT:** a line site outside `Z_r` differs from the background, so the no-input orbit
    emits along a line. This is exact and excluded from `𝒞`: R1 requires no output without input;
  - (d) **U:** the cap of `4 · 3^{|K_r| + |Z_r|}` ticks.

  Before (b) or (c), every value is ternary (NU6(c)), and the line sites outside `Z_r` are at the
  background. The state that can vary is the `K_r ∪ Z_r` values plus the line phase, a finite set,
  so the cap bounds the period of any orbit that reaches neither (b) nor (c). A return of the
  `K_r` values and phase alone is never used as a period.
  - Stage 3 enumerates the leak-free gadgets by backtracking over `K_2` (pruning on a leak in the
    one-tick neighbourhood of an assigned block), cross-checked by K6.
- **Arrival phases.** For a gadget of period `P`, start it at `N(s)` for every `s ∈ {0,…,P−1}`,
  with the signal at its fixed launch. This covers every phase of the gadget relative to the
  arrival.
- **Simulated set.** Only `A_r` and its one-site neighbourhood are simulated. Outside that set
  every value is `c` until the first LEAK tick, at which the case ends, so the update of this set
  is exact on `ℤ³` up to and including that tick.
- **Line ends.** Each line is truncated at length `L = 2 T_max + 16` from the core, with the W2
  background continued to its end. Influence moves at most one site per tick. So at every
  `t ≤ T_max`:
  - the sites within distance `L − t ≥ T_max + 16` of the core have the same values in the
    truncated and in the infinite-line run;
  - every deviation of either run from the background that originates at the core or at the
    signal lies within distance `8 + t` of the core;
  - every deviation originating at a truncated end lies within distance `t` of that end.

  LEAK detection, the T certificate and the U decision read only sites within distance `L − t`.
  Every quantity the outcomes use is therefore that of the infinite configuration. An end effect
  can create neither a false T nor a false LEAK, and so no false H0.
- **Background control at the ends.** A finite W2 segment is frozen (U1 E6). Control K11 checks
  that the truncated no-signal lines stay exactly periodic for `T_max` ticks. This is a
  consistency check only; exactness rests on the light-cone argument above.
- **Pruning.** Each case stops at its first exact outcome.

## 4. Controls and countercontrols (run first; any failure voids the verdict)

| Id | Kind | Requirement |
|---|---|---|
| K1 | positive control on Q | collinear junction (B continues A), empty gadget: T at every launch offset |
| K2 | positive control, classifier | U2's bent-line oracle O1: T. U2's O2 (B cut off): no T |
| K3 | countercontrol | J1 plain corner, empty gadget, B phase 1: LEAK, at any site. The first leaking site and tick are reported and compared with U2 D1 (the inner-corner kick at `t = 28`, then the row `x = −1` beside B); the comparison is informative |
| K4 | countercontrol | dead end (A only): LEAK (U2 N2) |
| K5 | countercontrol | linear member `L_{2^16, 3^{−1}}`, same initial states: no T (U2 N4) |
| K6 | completeness | on `K_1` of J1, the stage-3 backtracking returns exactly the leak-free set found by brute force in stage 1 |
| K7 | NU4 consistency | in every LEAK case where `D = cl₂(A_r)` is breached, the next tick has a value outside `D`; a violation voids the run |
| K8 | replication | at U2's launch offset, the period-4 part of the stage-1 leak-free set equals the ternary subset of U2 F1's quiescent set, recomputed with U2's `checks/univ2_checks.py` on `main` |
| K9 | signal-away | run for every T or T-STATEFUL case (R6) |
| K10 | sector control (n3), informative | the K3 run is also classified against the closed hull `D`, and the first breach tick of `D`, if any, is reported beside K3's first LEAK tick. A LEAK earlier than any breach shows that in-sector ternary spreading is caught by LEAK and would be missed by a breach-only test of `cl₂`. K10 does not void the run |
| K11 | line-end consistency | truncated W2 lines with no signal and no gadget stay exactly 4-periodic for `T_max` ticks |
| K12 | countercontrol for the period test (R1′) | the collinear geometry of K1 (B continues A along `e₁`), `r = 2`, empty gadget, treated as a no-input orbit. The U2 K0 defect has its whole window on line sites at distances 1–4 from the core, inside `Z_2`, and is oriented to move away from the core. By U1 Lemma 2.2 the off-line sites, including all of `K_2`, stay at `c`; the line background returns in phase at `t = 4`; the defect has moved about one site and is still inside `Z_2`. Two requirements: (i) the reduced test on (`K_r` values, phase) alone reports a return, period 4, at `t = 4`, which shows the false period is real; (ii) the full-state test reports no return at any tick before the defect leaves `Z_2`, and then Q-EMIT. Failure of (ii) at `t = 4` is exactly the error R1′ targets |

## 5. Decision rule (fixed now; the verdict text is generated from the counts)

- If any control fails: **VOID**.
- If at least one case is T or T-STATEFUL, is not R6-NULL, and holds when re-run in Q mod `2^16`:
  **H1 supported**, with the certificates. T and T-STATEFUL are reported separately.
- Else, if no case and no no-input orbit is U: **H0 for `𝒞`**, exact.
- Else: **INCONCLUSIVE**, with the U counts, split into no-input and signal cases, and their
  stages.

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| Preregistration before the run | this file's commit is an ancestor of the first execution commit; execution adds result files only |
| Enumeration complete | stage 1: `3^6`; stage 2: `3^10`; stage 3: K6 |
| Every no-input period included | the period is found by exact return; capped orbits are counted as U and enter the decision rule |
| The simulated set is exact on `ℤ³` | within the read zone (distance `L − t`), every value outside `A_r` and its neighbourhood is asserted `c` at every tick up to the first LEAK |
| Line ends cannot affect any checked site | `L = 2 T_max + 16` asserted; every check reads only sites within `L − t` of the core |
| Exact arithmetic | integer arrays; `|y| < 2^15` asserted; positives re-run in Q mod `2^16` |
| The T certificate is exact | separation `> 6 + w` asserted; ring-certified glider; K1, K2 |
| Breach implies radiation | K7 |
| No false no-input period | a period is accepted only on return of the full read-zone state, lines included; K12 |
| Determinism | a replay is byte-identical |
| Controls precede the verdict | the verdict is printed only after K1–K9, K11 and K12 hold (K10 is informative) |

## 7. Cost class (§A.40; n1)

- **Stage 1** (729 gadgets, no-input orbits of at most `4 · 3^6` ticks): bounded. Its cost is to be
  measured by a dry estimate once authorized, before stage 2 is scheduled.
- **Stages 2–3:** CI, sharded by B phase and gadget-phase offset.
- **Authorization.** Every stage needs it.

## 8. What it can decide (the owner's bar, c.7066602480 item 6)

- **H1:** an exact native leak-free controlled transfer in Q, U1's missing block. This is (N),
  at the standing of an exact computation plus the written certificate. It is decision-relevant:
  it would be the first native transfer block.
- **H0 for `𝒞`, which is narrow.** It means no leak-free controlled transfer among:
  - planar ternary gadgets on `K_r` with `r ≤ 2`, at J1 (both radii) and J2 (radius 1), whose
    no-input orbit is leak-free, returns exactly on the full read-zone state, and does not emit
    along a line (Q-LEAK and Q-EMIT gadgets are excluded);
  - W2 signals at a single launch distance, on the designed background `c = 2^15`;
  - every no-input period and every relative arrival phase.

  The allowed region is `lines ∪ K_r`, stricter than confinement in the closed sector. It says
  nothing about non-planar gadgets, larger radii, J3 or other junctions, W1 or other signals,
  other backgrounds, gadgets allowed to disturb a sector, or interactions other than a turn.
- **Stage 1 against U2 (n2).** Stage 1's gadgets are a subset of U2 F1's. A stage-1 H1 could come
  only from what U2 did not test: arrival phases other than U2's, or gadgets whose no-input period
  is not 4.
- **Expected value.** The most probable outcome, on the evidence of U1 and U2, is H0 for this
  small class. That would close only a narrow part of the gap. The owner may weigh this against
  the cost before authorizing.
- **Would not decide:** universality of Q even under H1, since gate, fan-out, composition and a
  Definition-U encoding and correctness argument are still needed; native preparation (Goal C);
  any quantum or BQP capability; anything about comparison rules.
