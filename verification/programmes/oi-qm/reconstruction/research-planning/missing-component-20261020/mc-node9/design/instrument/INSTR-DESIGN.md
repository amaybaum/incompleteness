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

## Tests (`instr_bench.py`, exact)

| Test | Content |
|---|---|
| T1 | First read: every preparation and every menu measurement match the reference |
| T2 | Repetition: m then m gives equal outcomes with probability 1 |
| T3 | Switching, retained outcomes and feedback: every fixed sequence of length ≤ 3 gives the reference joint distribution. Along each outcome path an adaptive strategy applies one fixed sequence, so this covers every adaptive strategy of depth ≤ 3 |
| T4 | Extra accessible reads: with the candidate's declared extra reads added, the optimal adaptive discrimination of depth ≤ 3 between any two preparations does not exceed the quantum trace distance \|r₁ − r₂\|/2. It is computed by exact recursion over unnormalized hidden-state measures and compared on squares |

## Controls and results

| Model | Role | T1 T2 T3 T4 | Deciding witness |
|---|---|---|---|
| Quantum reference | reference | P P P P | — |
| Label + seed deterministic dilation | positive control (imports QM rules) | P P P P | — |
| Correct first read, no state update | countercontrol | P F F F | X then X on Y+; X+ vs Y+ separated by 7/8 > √2/2 |
| R collapses to the X eigenstate | countercontrol | P F F P | R repetition on X+ fails with probability 1/10 |
| Correct instruments plus an accessible label read | countercontrol | P P P F | X+ vs r₊ separated by 1 > √2/4 |
| Triple-correlation encoding (report 10) | countercontrol | P F F F | R repetition fails with probability 51/200; X then Y on r₊; r± separated by 1 > 1/√2 |

- **Positive control.** The label + seed dilation reproduces the reference exactly. Its purpose is to show that the
  checker accepts correct sequential behaviour. It is not a reconstruction or a candidate.
- **Correction to my declared expectations.** My first table was wrong in two places:
  - for the no-collapse model, which also fails T4: repeated undisturbed reads amplify discrimination;
  - for the triple-correlation model, which also fails T2: its noisy R read cannot repeat.

  In both cases the checker's verdicts are correct on analysis. The table was corrected after the first run and is
  disclosed here.
- **Exactness bug, fixed before recording.** An empty measure made V₀ return a float. Every gap is now asserted to
  be a Fraction.

## Scope

- **Depth.** Bounded at 3. A PASS is evidence at that depth only.
- **Composite structure.** Not covered: no ancillas, no composites, no discard of a subsystem. Heralding enters only
  as conditioning on recorded outcomes.
- **Lattice origin.** None of these models comes from OI's lattice.
- **The research question it prepares.** Can independently specified OI dynamics generate these preparation, readout
  and update rules, while no additional accessible operation exposes more than the quantum trace distance allows?
