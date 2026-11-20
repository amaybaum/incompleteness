# UNIV-2: the native controlled turn in the published rounded rule

**Standing.** Author record of a paper-only unit (AGENTS.md §A.31, depth-first form). It has not
been reviewed by a non-author. It adopts no premise and edits no manuscript, Lean module or
registry. Small exact computations only (§7).

- **Authorization.** Owner `amaybaum`,
  [#1169 c.7031779559](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7031779559),
  2026-11-20T05:57:03Z, item 3 (quoted in `PREREG.md`). Not authorized: "an unrestricted
  universality search, manuscript edits, Lean, premise adoption or an automatic merge."
- **Goal link (§A.47), as preregistered.** Serves #866: whether the block UNIV-1 found missing in
  Q exists within the stated bounds, or is excluded for a stated class. That block is off-line
  transfer with the line sector restored. Unchanged: A1 OPEN/UNADOPTED; physical measurement
  sourcing NOT PASSED.
- **Accountable Issues.** #866, #1169. Predecessor: UNIV-1 (U1),
  `verification/programmes/oi-qm/reconstruction/univ-1-20261119/RESULT.md` (PR #1432).
- **Preregistration chain.** `PREREG.md` at `69bdc440` was pushed before any search. Amendments
  A01 (`80121d45`) and A02 (`785b1705`) were pushed before any control or family run; they are in
  `amendments/`. Snapshot `D`: `main` at `c2460ca5f`.
- **Productivity test (fixed in advance).** The unit is a gem iff it gives (i) a verified native
  controlled turn meeting all requirements, or (ii) a proved obstruction for a stated class. A
  bounded not-found is a recorded negative, not a gem.

| Label | Meaning |
|---|---|
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/univ2_checks.py` (integer or rational arithmetic) |
| [S] | bounded exhaustive search in the same file (`--search`); evidence about the searched set only |
| [R] | research record on `main` (U1), not independently established |

***

## 0. Summary

1. **Verdict: not found within bounds.** Every control is green (§2). Across the four
   preregistered families there are 52 436 gadgets, each at 4 phases of line B: 209 744 junction
   configurations. Of these, 2 720 are quiescent without input (R1). Every one of the 2 720 emits
   radiation outside the junction neighbourhood once the signal arrives (first failing requirement
   R3), and none reaches the output test [S, X1]. This is a bounded negative for the families of
   §3 only. It is not an obstruction.
2. **Analytic branch.**
   - A1: the two components evolve independently in Q [W, EC]. The restriction of the search to
     the signal component therefore loses nothing.
   - A2: no star-local conserved density on the alphabets `{−1,0,1}` and `{−2,…,2}` is nontrivial,
     whether exactly conserved or sign-alternating [EC]. The same template finds the quadratic
     energy of the linear update (countercontrol). So no direction charge of that template
     obstructs a turn.
   - A3: the reflection exchanging A and B, composed with time reversal, maps turns to turns. It
     forbids nothing [W].
   - No obstruction is proved.
3. **Productivity: not a gem.** Neither (i) nor (ii) holds; the unit is a recorded negative.
4. **First unresolved requirement.** R3 (restoration without radiation) fails for every gadget
   that passes R1. The unit stops there. R2 (transfer onto B) was never reached by a gadget that
   also met R1 and R3.
5. **Scope notes.** UNIV-1's negative results are preserved and extended within these bounds.
   Every configuration here is a designed initial condition; nothing is claimed about native
   preparation.

***

## 1. Object and requirements (as frozen)

Q is the rounded rule at `q = 2^16` on `ℤ³`, run as RZ on the background `c = 2^15` (U1 Lemma
2.1, one direction). Lines carry the W2 background, with period 4 in time. The input is the W2
defect: an adjacent `(+1,+1)` pair of A's background is flipped, 8 sites from the junction. The
requirements R1–R8 are those of PREREG §2 and A01. In short:
- R1: quiescence without input;
- R2: an outgoing glider on far B;
- R3: restoration to the post-transit reference `N(t)` outside far B, with no radiation outside
  lines ∪ `R⁺`;
- R4: continuation for 60 further ticks;
- R5: a second signal 12 sites behind, processed identically;
- R6: genuine transfer;
- R7: exact backward run;
- R8: the embedding window, and a re-run in Q.

**K0 [EC] (A01 item 1).** The W2 signal is a localized defect: within the first 60 ticks it
differs from the background on at most three sites, moves at speed 1/3, and leaves the line in
the *same* phase `N(t)`. PREREG's parenthesis "`−N(t)`" was a misreading of U1 E2. U1 E2's
relation `y(t+3) = −shift y(t)` negates the background too. A01 corrected it before any search.
K0b: on a straight ring the defect is a glider with `(p, s) = (6, 2)`, which is the same relation
seen without the negation. The check as first written expected `(3, 1)`. That was an error in the
check's statement, corrected before the search was run; the measured value is reported.

***

## 2. Controls (all green)

| Id | Outcome | Evidence |
|---|---|---|
| K0, K0b | W2 defect moves toward the junction at speed 1/3; behind it the line is `N(t)`; ring glider `(6, 2)` | [EC] |
| N1 | J1 plain corner without input: quiescent only for B phase 1 (the phase that continues A's pattern round the corner); phases 0, 2, 3 fail R1 | [EC] |
| N2 | dead end (no B): fail, first at R3 (radiation at `t = 37`; U1 E6) | [EC] |
| N3 | signal launched 60 sites out (A02), no arrival by `T₁`: fail at every phase (R2 "no output on B" at phase 1; R1 elsewhere) | [EC] |
| N4 | linear member `L_{2^16, 3^{−1}}`, same initial states: fail at every phase (R1: off-line sites adjacent to a line receive `±3^{−1} mod 2^16` at once) | [EC] |
| P1 | lattice billiard with one fixed 90° mirror: **pass** | [EC] |
| P1b | the same without the mirror: fail (R3) | [EC] |
| P2 | U1's collision turn with a supplied constant particle: fail, first at R1 (the constant particle moves without input) | [EC] |
| prefilter | agrees with the classifier on 100 seeded candidates per family; post hoc, on all 2 720 quiescent gadgets (X1) | [EC] |

The decision logic is the same for the controls and the search (`classify_rz`; for P1, P1b and P2,
`classify_generic`, which applies the same order R1, R3-radiation, R2, R3, R5, R7). P1's generic
path does not test R4 or R8, which have no analogue there.

***

## 3. Search [S]

| Family | Geometry, gadget | Gadgets | Quiescent (R1), by B phase 0/1/2/3 | Radiation-free to `T₁` | Passing |
|---|---|---|---|---|---|
| F1 | J1, 6 in-plane sites, values `{−2,…,2}` | 15 625 | 0 / 28 / 12 / 0 | 0 | 0 |
| F2 | J1, ≤ 3 of the 24 sites of `R`, values `±1` | 17 345 | 102 / 822 / 369 / 24 | 0 | 0 |
| F3-J2 | offset junction, ≤ 2 of 38 sites, values `±1, ±2` | 11 401 | 8 / 450 / 482 / 8 | 0 | 0 |
| F3-J3 | step junction, ≤ 2 of 32 sites, values `±1, ±2` | 8 065 | 0 / 6 / 403 / 6 | 0 | 0 |

Counts are asserted equal to the preregistered formulae. `T₁ = 120`, signal launched at distance
8, box margin checked every tick (so each box orbit is the `ℤ³` orbit until the first escape). The
first escape is classified post hoc, which changes no verdict. It lies in the row beside A (signal
scattered back along A's neighbours), in the row beside B, or off the lines; the split depends on
family and phase (printed by the checks). Every first escape occurs after `t = 24`, when the signal
(launched 8 sites away, speed 1/3) is within two sites of the junction. One instance [EC D1]: in the J1 plain corner at phase 1,
the inner-corner site `(−1,1,0)` is kicked at `t = 28`, when its two line neighbours carry equal
values, and a disturbance then runs along the row `(−1, y, 0)` beside B at one site per tick,
leaving `R⁺` at `t = 30`. This is U1's inner-corner mechanism (U1 §3, Turn) observed directly. It
is one instance, not a general law.

**What this does and does not show.** No gadget in these four families is a controlled turn. All
gadgets that are quiescent fail in the same way: the junction radiates when the signal arrives.
The families are small: at most 6 gadget sites, ternary or quinary values, three junction shapes,
one signal type, one launch phase. Bigger gadgets, other launch phases, other signal types, or
transient values beyond the alphabet are not covered.

***

## 4. Analytic branch

**A1 (components) [W, EC].** In Q, `x_{t+1}(i)` depends only on `x_t(j)` for `j ∼ i` and on
`x_{t−1}(i)`. Neighbours have opposite parity. So the set `{(i, t) : parity(i) + t even}` is closed
under the dependency, and so is its complement. The two components are two independent orbits
interleaved on one lattice. The check perturbs the other component at random and finds the signal
component unchanged for 12 ticks, in Q mod `2^16`. Consequence: gadget values in the other
component cannot affect whether a signal-component turn occurs. They can only affect R8 and their
own quiescence. Restricting the search to the signal component loses no generality for R1–R7.

**A2 (star-local conserved densities) [EC].**
- *Template.* `E = Σ_fresh ψ_F + Σ_old ψ_O + Σ_bonds φ_{d,±}(fresh, old)`, with direction- and
  orientation-dependent bond terms. The change of `E` in one update is assigned to the updated
  site's star. The fresh-site term `ψ_O − ψ_F` is split equally over a site's six bonds. Requiring
  the star change to vanish on every admissible star gives a linear system: each solution is a
  quantity conserved by every orbit that stays in the alphabet. The system is solved over ℚ:
  elimination modulo a prime, rational reconstruction, then exact verification of every equation.
  Since the nullity over ℚ is at most the nullity mod p, the verified lift is the exact solution
  space.
- *Results.* Solution spaces: 22 (`{−1,0,1}`, conserved); 21 (`{−1,0,1}`, sign-alternating); 36
  and 35 (`{−2,…,2}`). In every case each solution is the zero functional modulo constants: on 300
  random configurations of a `6³` torus the evaluation rank is 0.
- *Countercontrol.* The same template and test on the linear update `v' = s − v` finds one
  nontrivial solution, the quadratic energy.
- *Scope.* This excludes every conserved quantity of this template, and with it any direction
  charge of this form. It does not exclude conserved quantities that are not star-local (those
  whose star change is a nonzero divergence), wider templates, or invariants that are not
  conserved quantities.

**A3 (symmetry) [W].** Let `σ(x, y, z) = (−y, −x, z)`. It preserves site parity, commutes with
RZ, and maps J1's A onto B ∪ {corner} and B into A. Time reversal `(y_{t−1}, y_t) ↦ (y_t, y_{t−1})`
maps orbits to reversed orbits. Suppose a turn A → B exists for a gadget `g`. Reversing it gives
a signal entering on B and leaving on A, and `σ` maps that to a turn A → B for the gadget `σ(g)`,
time-reversed, provided the background phases match. Turns therefore come in pairs, and A3
forbids none.

**Verdict, analytic branch.** No obstruction. The productivity route (ii) is not met.

***

## 5. Productivity verdict and classification

- **(i) a verified native controlled turn: not met.** No gadget passes R3.
- **(ii) a proved obstruction for a stated class: not met.** A2 excludes only a template of
  conserved quantities; it is not an obstruction to turning.
- **Recorded negative.** Not found within the bounds of §3, over green controls.

| Item | Class |
|---|---|
| F1–F3: no turn; all 2 720 quiescent gadgets radiate | record-only bounded negative |
| A2: no nontrivial star-local conserved density (two alphabets, both signs) | NEW at this scope (author; awaiting review), negative |
| A1 component independence in Q | ELABORATING (immediate from the update; makes U1's search restriction lossless) |
| K0: W2 is a localized defect; same-phase background behind it | ELABORATING (U1 E2) |
| A3 | CONFIRMING (no constraint) |

**Pressure test (§A.31).**
1. The negative verdict rests on a strict R3: any value outside lines ∪ `R⁺` fails, even
   temporarily. A turn with bounded transient excursions beyond ℓ∞ distance 2 of the junction
   would be missed.
2. The launch phase is fixed by the signal position (arrival time mod 4 fixed). A gadget that
   turns only at another arrival phase would be missed.
3. The cross-check sample was dominated by R1 failures; X1 closes that gap for the cases that
   matter (every quiescent gadget, classifier and prefilter agree).
4. A2's negative concerns one template; it says nothing about whether turning is possible.

**Assumption-watch.**
- *AW-UNIV-3 (junction radiation).* At every junction tested, the step from one line direction to
  another passes through a site with two active line neighbours. When the signal arrives, that site
  is kicked and the disturbance leaves the line sector. A construction will need either a gadget
  that absorbs this kick and returns, which none of up to 3 sites (J1) or 2 sites (J2, J3) does, or
  a signal that does not create equal neighbour values at the junction.

**Fixed point.** One pass. The NEW item is negative (A2). The §A.31 fixed point is not reached.

***

## 6. What review must check; limits

- The requirement tests in `classify_rz` against PREREG §2 and A01 items 1–3. In particular:
  - the post-transit reference `N(t)` (K0);
  - the transplant test for R2 (far B copied onto a ring carrying B's background at `T₁`);
  - R5's common `(p, s)`.
- That the prefilter applies the same R1 and R3 conditions as the classifier (A01 item 5; X1).
- A2: the star decomposition, and in particular the split of the fresh-site term over six bonds;
  the exact-lift argument; and that the evaluation test detects nontrivial functionals (the
  countercontrol A2c).
- A1's dependency argument; A3's composition of reflection and time reversal.
- The controls' required outcomes: P1 and P1b are a designed calibration rule; N3's respecification
  is in A02.
- The deviations: K0b's expected value corrected before the search (§1). A first `--search` run
  was stopped during F1 without its results being read, to add the per-stage counts; the counts
  were then extended with the post hoc check X1, and the reported numbers come from the final full
  run.
- Not done: no Lean; no literature re-read; no search beyond §3; no other signal types, launch
  phases, non-uniform backgrounds or larger gadgets.

***

## 7. Exact checks

`checks/univ2_checks.py`, run from this directory:
- `python3 -I checks/univ2_checks.py` (a few seconds): A1, K0, K0b, N2–N4, P1, P1b, P2, D1, A2
  on `{−1,0,1}`, A2c.
- `python3 -I checks/univ2_checks.py --search` (about 20 minutes on one core): in addition, A2 on
  `{−2,…,2}`, F1–F3 with completeness and cross-check, and X1.

The exit status is 0 iff every check holds; the final full run reports 24/24. Arithmetic is
integer or rational throughout; numpy arrays are `int32`/`int64`, and `|y| < 2^15` is checked at
every tick.
