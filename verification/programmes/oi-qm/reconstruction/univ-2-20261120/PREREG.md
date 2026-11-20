# UNIV-2 preregistration: a native controlled turn in the published rounded rule

**Standing.** Preregistration of a paper-only unit (AGENTS.md §A.29, §A.31 depth-first form,
§A.41). Committed and pushed before any gadget search or invariant computation on Q is run. It
fixes requirements, search space, bounds, controls and the decision rule; it states no expected
result for the searched rule. The record adopts no premise and edits no manuscript, Lean module or
registry.

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7031779559](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7031779559),
  2026-11-20T05:57:03Z, item 3: "UNIV-2: a bounded, paper-only follow-up to UNIV-1 on the published
  nonlinear rule at q=2¹⁶." Target: "the smallest missing building block, a native controlled
  turn, meaning a transfer of a signal off its line that restores the original line sector."
  "Preregistered before any search: the gadget requirements, the search bounds and the negative
  controls." "Outcome: either an explicit construction or a rigorously scoped obstruction." "Tests:
  genuine transfer, reversibility, background restoration and repeatability." "Permitted: small
  exact computations." "Not authorized: an unrestricted universality search, manuscript edits,
  Lean, premise adoption or an automatic merge."
- **Goal link (§A.47).** Serves the measurement-source item (#866): it decides whether the block
  that UNIV-1 found missing for apparatus-side construction in Q (off-line transfer with the line
  sector restored) exists within the stated bounds, or is excluded for a stated class. Unchanged:
  A1 OPEN/UNADOPTED; physical measurement sourcing NOT PASSED.
- **Accountable Issues.** #866, #1169. Predecessor: UNIV-1
  (`verification/programmes/oi-qm/reconstruction/univ-1-20261119/RESULT.md`, PR #1432), cited
  below as U1.
- **Snapshot `D`.** `main` at `c2460ca5f` (the branch base).

***

## 1. Object

Q is the rounded rule `x_{t+1}(i) = ⌊(Σ_{j∼i} x_t(j) + 1)/3⌋ − x_{t−1}(i) mod 2^16` on `ℤ³`
(U1 §1). All constructions sit on the uniform background `c = 2^15` and are run in the integer rule
RZ, `y_{t+1}(i) = ⌊(Σ_{j∼i} y_t(j) + 1)/3⌋ − y_{t−1}(i)`, through U1 Lemma 2.1 (if `|y| < 2^15`
along the orbit, `c + y` is the Q-orbit; one direction only). Every check records `max |y|`. Any
candidate that passes in RZ is re-run in Q itself (mod `2^16`, on representatives) before it is
reported.

**Component.** Each site holds a current and a previous value. The search uses only the
*signal component*: the current slice on sites of parity `t` and the previous slice on sites of
parity `t + 1` (parity of `x + y + z`). The other component is set to 0 throughout. This is a
restriction of the search space. Whether it loses generality (the two components evolve
independently) is stated and proved in RESULT, not assumed here.

**Lines and signal.** A line is an axis-parallel finite segment carrying the W2 background of U1
(the staggered pattern; period 4 in time). The input signal is the W2 window of U1 (or its mirror
image, chosen so that it moves toward the junction), launched 8 sites from the junction end of
line A. Its motion on a straight line is checked as control K0 before any search.

***

## 2. Gadget requirements (all must hold)

Notation: `N(t)` is the no-input orbit (lines and gadget, no signal); `S(t)` the one-signal orbit;
`S₂(t)` the two-signal orbit. B is a line not parallel to A. "Far B" is the part of B at distance
`≥ 8` from the junction. The *post-transit reference* is the state a straight line of the same
type leaves behind its signal; for W2 this is `−N(t)` (U1 E2: `y(t+3) = −shift y(t)`), and for a
rule without such a sign flip it is `N(t)`.

| Id | Requirement | Operational test |
|---|---|---|
| R1 quiescence | without input, no output and nothing radiates | `N(4) = N(0)` exactly; every site outside lines ∪ gadget region `R` is 0 for `t ≤ 8` (then `N` is 4-periodic for all `t`) |
| R2 transfer | a signal entering on A exits as a signal on B | at the final time `T₁`, far B equals, up to translation along B, a straight-line reference orbit of the signal moving away from the junction |
| R3 restoration | A's sector, the gadget and near B return to background | at `T₁`, every site outside far B equals the post-transit reference; no value outside lines ∪ `R⁺` is ever nonzero (`R⁺`: sites within ℓ∞ distance 2 of the junction core) |
| R4 continuation | the exit signal keeps moving | from `T₁`, 60 further ticks: far B still matches the moving reference, and R3 still holds outside it |
| R5 repeatability | a second signal is processed the same way | a second signal launched 12 sites behind the first on A (36 ticks later; the background period 4 divides 36): at `T₂` every site outside far B equals the reference after two transits, and far B matches a straight-line two-signal reference |
| R6 genuine transfer | the output depends on the input | R1 (no input ⇒ no output) together with R2; and control N3 below (input that never reaches the junction ⇒ no output) |
| R7 reversibility | the gadget's operation is a bijection, run exactly | the backward rule (`y_{t−1} = G(Σ y_t) − y_{t+1}`) from the final state of `S` returns the initial state exactly; nothing reaches the box margin, so the box orbit is the `ℤ³` orbit |
| R8 embedding | the construction is in Q | `max |y| < 2^15` along every orbit used; the passing candidate is re-run in Q mod `2^16` and agrees |

Delay, sign and timing of the exit signal are free; only requirements R1–R8 are imposed. Phase
synchrony with the background (arrival time mod 4) is fixed by the launch position and is recorded,
not varied.

***

## 3. Search space and bounds

Junction geometries (A ends at `a`, B starts at `b`; lines at `z = 0` unless stated):

- **J1 corner:** A = `{(x,0,0) : −20 ≤ x ≤ 0}`, B = `{(0,y,0) : 1 ≤ y ≤ 44}`; core `{(0,0,0)}`.
- **J2 offset:** A as in J1, B = `{(1,y,0) : 1 ≤ y ≤ 44}`; core `{(0,0,0), (1,1,0)}`.
- **J3 step:** A as in J1, B = `{(0,y,1) : 0 ≤ y ≤ 44}`; core `{(0,0,0), (0,0,1)}`.

B carries the W2 background at each of its 4 spatial phases (a search parameter). The gadget region
`R` is the set of non-line sites within ℓ∞ distance 1 of the core. Gadget values are placed in the
signal component only.

| Family | Geometry | Gadget sites | Values | Size (× 4 B-phases) |
|---|---|---|---|---|
| F1 | J1 | the 6 in-plane sites of `R` | each in `{−2,…,2}` | 5^6 = 15 625 |
| F2 | J1 | at most 3 sites of `R` (24 sites) | nonzero values `±1` | 17 345 |
| F3 | J2, J3 | at most 2 sites of `R` | nonzero values in `{±1, ±2}` | per geometry `1 + 4·|R| + 16·C(|R|,2)` (geometry-dependent; counted by the code) |

Time horizon: `T₁ = 120` ticks for R2/R3, then R4 to `T₁ + 60`; R5 with `T₂ = T₁ + 36`. Box: a
periodic box with a margin of at least 2 sites around lines ∪ `R⁺`; any nonzero value in the
margin fails the candidate (R3) and so cannot wrap. Runs are pruned at the first failed test; the
order of tests is R1, then R2/R3 at `T₁`, then R4, R5, R7, R8.

Nothing beyond these families is searched (no unrestricted universality search).

***

## 4. Analytic branch: invariants that could obstruct a turn

Run before the gadget search; each item ends in a proof, an exact computation, or "not found":

- **A1 (component decoupling).** Whether the two components evolve independently, by inspection
  of the update; proof in RESULT.
- **A2 (star-local conserved densities).** Unknowns: site functions `ψ_F, ψ_O` (fresh/old
  sublattice) and oriented bond functions `φ_{d,±}` for `d = 1, 2, 3`, on the alphabet `{−1,0,1}`
  and then `{−2,…,2}`. Condition: for every star (an updated site and its six neighbours) whose
  updated value stays in the alphabet, the change of the density assigned to the star is zero.
  Solved exactly over ℚ (rational arithmetic). Any solution is a conserved quantity of every orbit
  that stays in the alphabet. If a solution distinguishes the e₁ and e₂ line directions on W2
  signals and its value on the initial state differs from its value on every state that R2–R3
  allow, that is an obstruction for orbits in that alphabet (any gadget size). Its proof, and the
  gadget-independence of the inequality, are written in RESULT; otherwise the result is "no
  star-local direction charge in this template".
- **A3 (symmetry).** Whether the diagonal reflection exchanging A and B, together with time
  reversal, forbids or constrains R2–R3.

***

## 5. Controls (run first; a failed control voids the verdict)

| Id | Control | Required outcome |
|---|---|---|
| K0 | straight W2 line: the launched signal moves toward the junction end; the straight-line references used by R2, R4 and R5 reproduce E2 of U1 | translation verified |
| N1 | no-input run of the J1 plain corner and of every candidate (R1 is applied to all) | no output on B |
| N2 | dead end: A alone, no B, empty gadget (U1 E6: a W2 signal at a segment end leaves the line sector) | classified fail |
| N3 | J1 plain corner with the signal launched on A moving away from the junction | classified fail (no output) |
| N4 | linear rule: the J1 plain-corner initial state run under `L_{2^16, 3^{−1}}` at background `c` (U1 Theorem L member; dispersive) | classified fail |
| P1 | positive control: a lattice billiard (four velocity channels per site, free streaming, and fixed mirror sites that rotate velocities by 90°, a reversible partitioned rule realizing Fredkin–Toffoli mirrors), a particle on a path meeting one mirror | classified pass (R1–R7; post-transit reference `N(t)`) |
| P2 | informative: the U1 billiard-ball block rule with a collision turn against a supplied constant particle (U1 F1) | classified fail on restoration (the constant particle is consumed); this shows that R3 has force |

The classifier (R1–R7 decision logic) is one function, shared by the controls and the search; the
rule-specific parts are the step function, the region masks, the post-transit reference and the
straight-line signal reference.

***

## 6. Decision rule and productivity test

The verdict is generated from the computed outcomes, over green controls only.

1. **Construction found:** some candidate passes R1–R8, with every control green. It is reported
   with its exact initial state, re-run in Q, and classified as a *designed* initial condition
   (no native preparation is claimed unless shown separately).
2. **Scoped obstruction proved:** the analytic branch yields an invariant with a written proof and
   an exact check, whose scope (alphabet, geometry, gadget class) is stated.
3. **Not found within bounds:** neither. This is a bounded negative for the families of §3 only,
   not an obstruction.

If a candidate passes some requirements and fails a later one, the unit stops at the first failed
requirement and names it (assignment constraint 3).

**Productivity test (fixed in advance).** The unit is a gem iff it gives (i) a verified native
controlled turn meeting R1–R8, or (ii) a proved obstruction for a stated class. A bounded
not-found is a recorded negative, not a gem.

**Invariant → checkpoint (§A.41).** Exact integer arithmetic: every array is `int64`/`int8` with
`max |y|` recorded (R8). Box equals `ℤ³` orbit: margin check (R3, R7). Classifier calibrated: N2,
N3, N4 fail and P1 passes (§5). Search completeness: the code prints the number of candidates per
family and asserts it equals the count of §3. Preregistration precedes search: this file's commit
is an ancestor of every search commit.

**Amendments.** Any change to §2–§6 after this commit is made in `amendments/`, committed before the
run it governs, and reported in RESULT.
