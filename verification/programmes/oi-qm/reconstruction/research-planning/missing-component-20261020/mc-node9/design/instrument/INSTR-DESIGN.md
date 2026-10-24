# D6 instrument benchmark: one qubit, a finite menu, complete instruments

> **DRAFT — NOT FROZEN.** Design evidence for the candidate benchmark (`../benchmark/BENCH-DESIGN.md`, D6). Not part of
> model A's closure test, and not a C5 candidate. Owner specification of 2026-10-22.

## Specification

- **Menu.** Sharp binary measurements X, Y, Z and R, the axis (4/5, 3/5, 0) used in report 10.
- **Preparations.** The eight menu eigenstates, plus r± = ±(1/2, 1/2, 0), the two preparations that exposed the
  earlier failures.
- **Candidate format.** A finite outcome-labelled kernel:
  - hidden states;
  - a preparation distribution for each label;
  - for every measurement and hidden state, a list of (outcome, next hidden state, probability).

  The outcome and the state update are declared together. Retained outcomes sit in an explicit record register, and
  feedback reads only that register.
- **Quantum reference.** Bloch calculus: P(+ | r, n) = (1 + n·r)/2, with post-measurement state ±n. Every quantity is
  rational.

## Gates (owner review, 2026-10-22), applied before any test

- **VALIDITY.** Every preparation distribution, and every kernel reachable from the declared preparations under the
  menu and the declared extra reads, must have nonnegative exact probabilities summing to 1 and outcomes in {0, 1}.
  Otherwise the model prints **INVALID**, and its behavioural scores are not reported.
- **COVERAGE.** The mandatory preparations are all ten, and the mandatory menu is X, Y, Z, R.
  - A model may not shrink either.
  - A countercontrol or restricted control declaring a subset is scored on that subset, and its row states k/10 and
    the menu used.
  - Empty coverage is refused.
  - Only a VALID 10/10 PPPP row on the full menu can accept a candidate.

## Tests (`instr_bench.py`, exact)

| Test | Content |
|---|---|
| T1 | First read: every preparation and every menu measurement match the reference |
| T2 | Repetition: m then m gives equal outcomes with probability 1 |
| T3 | Switching, retained outcomes and feedback: every fixed sequence of length ≤ 3 gives the reference joint distribution. Along each outcome path an adaptive strategy applies one fixed sequence, so this covers every adaptive strategy of depth ≤ 3 |
| T5 | Preparation equivalence, complete and depth-free (owner reviews): every mixture equivalence among the ten fixed laws must be exactly unobservable. The (1, r) columns have rank 4, so a basis of six relations covers all equivalences by linearity (checked exactly). Unobservability means the signed hidden-law difference annihilates the outcome-functional span: normalization, closed under the transpose of every outcome-labelled kernel over the reachable states, extra and discard reads included. This decides equivalence at every finite depth, adaptive protocols included, for a fully specified finite model. Declared contextual procedures enter one augmented preparation matrix with the ten base laws, and its whole null space is checked against the same span, so cross-family equivalences are covered. Undeclared operations and unbounded extensions are not certified |
| T4 | Extra accessible reads: with the candidate's declared extra reads added, the optimal adaptive discrimination of depth ≤ 3 between any two preparations does not exceed the quantum trace distance \|r₁ − r₂\|/2. It is computed by exact recursion over unnormalized hidden-state measures and compared on squares |

## Controls and results

| Model | Role | Gate and coverage | T1 T2 T3 T4 T5 | Deciding witness |
|---|---|---|---|---|
| Quantum reference | reference | VALID 10/10, XYZR | P P P P P | — |
| Label + seed deterministic dilation | positive control (imports QM rules) | VALID 10/10, XYZR | P P P P P | — |
| Correct first read, no state update | countercontrol | VALID 10/10, XYZR | P F F F F | X then X on Y+; X+ vs Y+ separated by 7/8 > √2/2; Z-mix vs X-mix by 3/4 |
| R collapses to the X eigenstate | countercontrol | VALID 10/10, XYZR | P F F P P | R repetition on X+ fails with probability 1/10 |
| Correct instruments plus an accessible label read | countercontrol | VALID 10/10, XYZR | P P P F F | X+ vs r₊ separated by 1 > √2/4; XY-mix vs r₊ by 1 |
| Triple-correlation encoding (report 10) | partial countercontrol | VALID **2/10**, XYZR | P F F F – | R repetition fails with probability 51/200; X then Y on r₊; r± separated by 1 > 1/√2 |
| Negative weights that cancel (owner mutation) | gate countercontrol | **INVALID** | not reported | its statistics match the reference on all 840 sequence–preparation pairs, so only the gate catches it |
| No preparations declared (owner mutation) | gate countercontrol | **COVERAGE** refused | not reported | — |
| Procedure tag readable through a discard read | T5 countercontrol | VALID 10/10, XYZR | P P P P F | passes T1–T4; the declared Z-mix vs X-mix procedures are separated |
| Detector read biased on R± (owner) | T5 countercontrol | VALID 10/10, XYZR | P P P P F | P(D = 1) = 51/100 on R±, ½ otherwise; passes T1–T4 at depth 3; caught by basis relation 3 (X-mix = R-mix). The earlier three-relation T5 missed it |
| Tag separating ordinary preparations from declared procedures (owner) | T5 countercontrol | VALID 10/10, XYZR | P P P P F | ordinary r₊ vs the declared r₊ procedure are perfectly separated; caught only by the augmented null space. The previous within-family T5 passed it (checked) |
| Fresh-card instrument (owner) | restricted positive control | VALID **4/10**, menu XY | P P P P P | reading one coordinate replaces the other with a fresh card value, a counted resource |

- **The validity gate also explores procedure laws**, which are T5's hidden states.
- **Functional-span sanity check.** The span is 4 for the quantum reference and the dilation, which is the qubit's effect-space dimension, and 3 for the fresh-card control.
- **Positive control.** The label + seed dilation reproduces the reference exactly. Its purpose is to show that the
  checker accepts correct sequential behaviour. It is not a reconstruction or a candidate.
- **Correction to my declared expectations.** My first table was wrong in two places:
  - for the no-collapse model, which also fails T4: repeated undisturbed reads amplify discrimination;
  - for the triple-correlation model, which also fails T2: its noisy R read cannot repeat.

  In both cases the checker's verdicts are correct on analysis. The table was corrected after the first run and is
  disclosed here.
- **Exactness bug, fixed before recording.** An empty measure made V₀ return a float. Every gap is now asserted to
  be a Fraction.

## First-read obstruction for the four-state card preparations (owner review)

- **Setting.** Keep the card preparations X±, Y±: uniform on the two cards with that coordinate fixed.
- **Bound.** No response on the cards implements R. X+ and Y− are at total-variation distance ½, so
  P(R+ | X+) − P(R+ | Y−) ≤ ½. The quantum values are 9/10 and 1/5, a gap of 7/10.
- **Exact optimum.** Per card, the conditions force b ≥ 4/5 − 2ε and b ≤ 2/5 + 2ε for the card (+, −). So the
  minimum worst-case error is ε = 1/10, and the response (1, 3/5, 2/5, 0) attains it (`card_R_obstruction`).
- **Decision.** Do not search for a better R update while these preparation distributions are kept. The first read
  rules it out, whatever the update rule.
- **Relation to earlier results.** It is the measurement-side form of the diamond obstruction of reports 3 and 4:
  the card preparations are K₁ line states.

## Scope

- **Depth.** Bounded at 3. A PASS is evidence at that depth only.
- **Composite structure.** Not covered: no ancillas, no composites, no discard of a subsystem. Heralding enters only
  as conditioning on recorded outcomes.
- **Lattice origin.** None of these models comes from OI's lattice.
- **The research question it prepares.** Can independently specified OI dynamics generate these preparation, readout
  and update rules, while no additional accessible operation exposes more than the quantum trace distance allows?
