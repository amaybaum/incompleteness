# UNIV-2: the native controlled turn in the published rounded rule

**Standing.** Author record of a paper-only unit (AGENTS.md §A.31, depth-first form). Independent
non-author review at `aecc64ef`: REVISE (minor). The revision `8866cf4a` answers its items B1, B2
and N1–N7. Re-review at `8866cf4a`: ACCEPT-WITH-NITS
([#1444 c.7033699598](https://github.com/amaybaum/incompleteness/pull/1444#issuecomment-7033699598));
its three text nits are fixed here.
It adopts no premise and edits no manuscript, Lean module or
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
  `amendments/`. Snapshot `D`: `main` at `c2460ca5f`. The claim that the preregistration preceded
  the search rests on the order of these three commits and the search commit `aecc64ef` (§A.42
  item 8: the claim uses the commits' ancestry). The pull request must therefore land by a merge
  commit that keeps them in `main`'s history; a squash or rebase landing would leave this claim
  without support on `main`.
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

1. **Verdict: not found within bounds.** Every control is green (§2). Across the three
   preregistered families (F3 on two geometries) there are 52 436 gadgets, each at 4 phases of line B: 209 744 junction
   configurations. Of these, 2 720 are quiescent without input (R1). Every one of the 2 720 emits
   radiation outside the junction neighbourhood once the signal arrives (first failing requirement
   R3), and none reaches the output test [S, X1]. This is a bounded negative for the families of
   §3 only. It is not an obstruction.
2. **Analytic branch.**
   - A1: the two components evolve independently in Q [W, EC]. The restriction of the search to
     the signal component therefore loses nothing.
   - A2: on the alphabets `{−1,0,1}` and `{−2,…,2}`, every density of the §4 template whose change
     vanishes star by star (fresh-site term split equally over the six bonds) is trivial, whether
     exactly conserved or sign-alternating [EC]. The same test finds the quadratic energy of the
     linear update (countercontrol). So no direction charge of that template, conserved star by
     star, obstructs a turn.
   - A3: the reflection exchanging A and B, composed with time reversal, maps a turn to a turn,
     provided the background phases match, the image gadget is quiescent at the matched phase, and
     the reversed signal has the input's type and arrival phase. It forbids nothing [W].
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
| O1 | bent-line oracle through `classify_rz`: the line rule run along A → corner → B as one path, off-path sites held at 0 (J1, B phase 1). R1–R7 pass (outgoing glider `(6, 2)`; R5 the same); first failure R8, since the oracle is not Q | [EC] |
| O2 | the same oracle with B cut off from the corner: first failure R2, "no output on B" | [EC] |
| P1 | lattice billiard with one fixed 90° mirror: **pass** | [EC] |
| P1b | the same without the mirror: fail (R3) | [EC] |
| P2 | U1's collision turn with a supplied constant particle: fail, first at R1 (the constant particle moves without input) | [EC] |
| prefilter | agrees with the classifier on 100 seeded candidates per family; post hoc, on all 2 720 quiescent gadgets (X1) | [EC] |

**Two classifier functions (deviation from PREREG §5, "one function").**
- *`classify_rz`* runs the search, K0, N1–N4 and the oracle pair O1/O2.
- *`classify_generic`* runs the lattice-billiard and billiard-ball controls P1, P1b and P2. It
  applies the same order (R1, R3-radiation, R2, R3, R5, R7), but it does not test R4 or R8, and its
  R2 test is rule-specific. So P1 calibrates the decision order, not `classify_rz` itself.
- *O1 and O2 calibrate `classify_rz` past R3.* O1 drives it through R1–R7 to a pass on a turning
  dynamics, and it fails only at R8. O2 shows that its R2 test reports no output when the transfer
  is cut.
- Before O1/O2 were added (review B1), no control drove `classify_rz` past R3.

***

## 3. Search [S]

| Family | Geometry, gadget | Gadgets | Quiescent (R1), by B phase 0/1/2/3 | Radiation-free to `T₁` | Passing |
|---|---|---|---|---|---|
| F1 | J1, 6 in-plane sites, values `{−2,…,2}` | 15 625 | 0 / 28 / 12 / 0 | 0 | 0 |
| F2 | J1, ≤ 3 of the 24 sites of `R`, values `±1` | 17 345 | 102 / 822 / 369 / 24 | 0 | 0 |
| F3-J2 | offset junction, ≤ 2 of 38 sites, values `±1, ±2` | 11 401 | 8 / 450 / 482 / 8 | 0 | 0 |
| F3-J3 | step junction, ≤ 2 of 32 sites, values `±1, ±2` | 8 065 | 0 / 6 / 403 / 6 | 0 | 0 |

Counts are asserted equal to the preregistered formulae. The checks also assert the quiescent
table, its total of 2 720 and the timing of the first escapes (X2, X3). `T₁ = 120`; the signal is
launched at distance 8.

**Box margin (deviation from PREREG §3, "at least 2 sites").** The margin beyond lines ∪ `R⁺` is 1
site in `z` (all geometries) and in `+x` for J2. It is 2 in `+x` for J1 and J3, 3 in `−x`, 2 in `−y`
(the box starts at `y = −4`; `R⁺` reaches `y = −2`), and 4 in `+y` beyond B's far end. This is harmless, for three reasons:
- A candidate fails at the first tick on which any value outside lines ∪ `R⁺` is nonzero.
- Every neighbour of a site in lines ∪ `R⁺` lies inside the box without wrapping. Up to that
  tick, every nonzero value lies in lines ∪ `R⁺`, so the box update equals the `ℤ³` update.
- A disturbance can reach a wrapped neighbour only by first appearing in the margin, and that
  fails the candidate.

The first escape is classified post hoc, which changes no verdict. It lies in the row beside A (signal
scattered back along A's neighbours), in the row beside B, or off the lines; the split depends on
family and phase (printed by the checks). Every first escape occurs after `t = 24`, when the signal
(launched 8 sites away, speed 1/3) is within two sites of the junction. One instance [EC D1]: in the J1 plain corner at phase 1,
the inner-corner site `(−1,1,0)` is kicked at `t = 28`. At that update its two line neighbours
`(−1,0,0)` and `(0,1,0)` carry equal nonzero values: both are `+1`, whereas without input they are
`−1` and `+1`, sum 0. After the kick, a disturbance then runs along the row `(−1, y, 0)` beside B at one site per tick,
leaving `R⁺` at `t = 30`. This is U1's inner-corner mechanism (U1 §3, Turn) observed directly. It
is one instance, not a general law.

**What this does and does not show.** No gadget in these families is a controlled turn. All
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

**A2 (densities conserved star by star) [EC].**
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
- *Scope.* The computation excludes every density of this template whose change vanishes star by
  star, with the fresh-site term split equally over the six bonds. With them go the direction
  charges of that form. It does not exclude:
  - densities of the same template that are conserved only because star changes cancel globally,
    for example under another split of the fresh-site term or through a nonzero divergence;
  - wider templates;
  - invariants that are not conserved quantities.

**A3 (symmetry) [W].** Let `σ(x, y, z) = (−y, −x, z)`. It preserves site parity, commutes with
RZ, and maps J1's A onto B ∪ {corner} and B into A. Time reversal `(y_{t−1}, y_t) ↦ (y_t, y_{t−1})`
maps orbits to reversed orbits. Suppose a turn A → B exists for a gadget `g`. Reversing it gives
a signal entering on B and leaving on A, and `σ` maps that to a turn A → B for the gadget `σ(g)`,
time-reversed. Four conditions must hold:
- the reflected background phases on A and B match those of the geometry;
- `σ(g)`, time-reversed, is quiescent at the matching phase;
- the reflected, time-reversed output signal has the input's type;
- it arrives at the input's arrival phase.

Under these conditions turns come in pairs. A3 forbids nothing in any case.

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
| A2: no nontrivial density of the template conserved star by star (two alphabets, both signs) | NEW at this scope (author; awaiting review), negative |
| A1 component independence in Q | ELABORATING (immediate from the update; makes U1's search restriction lossless) |
| K0: W2 is a localized defect; same-phase background behind it | ELABORATING (U1 E2) |
| A3 | CONFIRMING (no constraint) |

**Pressure test (§A.31).**
1. The negative verdict rests on a strict R3: any value outside lines ∪ `R⁺` fails, even
   temporarily. A turn with bounded transient excursions beyond ℓ∞ distance 2 of the junction
   would be missed.
2. The launch phase is fixed by the signal position (arrival time mod 4 fixed). A gadget that
   turns only at another arrival phase would be missed.
3. The cross-check sample was dominated by R1 failures. X1 closes that gap for the cases that
   matter: on every quiescent gadget, classifier and prefilter agree.
4. A2's negative concerns one template; it says nothing about whether turning is possible.
5. R4 and R8 are implemented more weakly than PREREG states.
   - R4 checks only the far-B glider and the restoration at `T₁ + 60`, without R2's 12-site
     window.
   - R8 re-runs only the one-signal orbit in Q, up to `T₁`. It records `max |y|` on the signal
     orbits but not on `N`.
   - No Q candidate reached either test; only the oracle O1 reached R8, which rejected it.
6. Far B is defined by `y ≥ 8`. For J2 the junction core contains `(1,1,0)`, so far B begins at
   distance 7 from the junction, not 8.

**Assumption-watch.**
- *AW-UNIV-3 (junction radiation; a hypothesis from one instance).*
  - *Observation.* In each junction geometry tested, a site off the lines has two line
    neighbours, one on each side of the bend. D1 shows, for the J1 plain corner only, that the
    arriving signal gives those two neighbours equal nonzero values; the site is kicked, and a
    disturbance leaves the line sector.
  - *Hypothesis.* This mechanism causes the radiation throughout the searched families. Beyond
    D1 it is untested: X1 records only where and when the first escape occurs.
  - *Consequence if it holds.* A construction needs either a gadget that absorbs the kick and
    returns to background, or a signal that does not create equal neighbour values at the
    junction. No gadget searched is such an absorber: the 6 in-plane J1 sites with values
    `{−2,…,2}` (F1), up to 3 of J1's 24 sites with values `±1` (F2), and up to 2 sites at J2 or J3
    with values `±1, ±2` (F3).

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
- The deviations:
  - K0b's expected value was corrected before the search (§1).
  - A first `--search` run was stopped during F1, without its results being read, to add the
    per-stage counts. The post hoc check X1 then extended those counts. The reported numbers come
    from the final full run.
  - The controls use two classifier functions; O1 and O2 were added after review (§2).
  - The box margin is 1 rather than 2 (§3).
  - R4 and R8 are implemented more weakly than PREREG states (§5, item 5).
  - For J2, far B begins at distance 7 (§5, item 6).
- The landing: by a merge commit that keeps the preregistration commits in `main`'s history
  (Standing).
- Not done: no Lean; no literature re-read; no search beyond §3; no other signal types, launch
  phases, non-uniform backgrounds or larger gadgets.

***

## 7. Exact checks

`checks/univ2_checks.py`, run from this directory:
- `python3 -I checks/univ2_checks.py` (a few seconds): A1, K0, K0b, N2–N4, P1, P1b, P2, O1, O2,
  D1, A2 on `{−1,0,1}`, A2c.
- `python3 -I checks/univ2_checks.py --search` (about 11 minutes on one core): in addition, A2 on
  `{−2,…,2}`, F1–F3 with completeness and cross-check, and the post hoc checks X1–X3.

The exit status is 0 iff every check holds; the final full run reports 28/28. Arithmetic is
integer or rational throughout; numpy arrays are `int32`/`int64`, and `|y| < 2^15` is checked at
every tick.
