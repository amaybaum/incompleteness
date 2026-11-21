# NATIVE-UNIV, phase 2: paper work on P3, P1-Q2 and the bounded-breach question (plan)

**Standing.** Writer's plan, committed before any of the derivations it governs. Paper only: no
computation beyond replaying the exact checks already on the base branch. Stacked on the
reviewed head `2572854b` of #1489 (record
`verification/programmes/oi-qm/reconstruction/native-univ-feasibility-20261121/`, cited as F1
below). F1 is unchanged here.

**Authorization.** Owner `amaybaum`,
[#1169 c.7064767045](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064767045)
(2026-11-21): research, proof exploration, planning and preregistration are authorized. Computational
experiments, CI dispatches, manuscript changes, merges and the adoption of new physical assumptions
are not. The same post lists "the computational runs of #1489's P1–P3" as still restricted, and the
coordinator's reading recorded there treats a paper-only proof attempt such as P3 as proof
exploration. The earlier decision
[#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074)
item 3(b) states that constructing or testing a new universal model needs step-2 authorization.
P1-Q2's paper design is carried out here as proof exploration. Whether a completed paper design
counts as "constructing" under item 3(b) is left to the owner (NOTE §6).

## Questions (depth-first, in this order)

1. **B (Q, the decisive question of F1 §4).** Given F1's Lemma NU2, does a bounded breach that heals
   without radiation exist for Q = `R_{2^16}` on `ℤ³` at a uniform background, for finite
   configurations and for configurations with infinite lines? Or is it excluded, and for which class?
2. **P3, as preregistered** (F1 `plans/P3-PREREG.md`): stage S1, then S2. Each stage ends proved,
   refuted or open, with the point where the attempt stopped.
3. **P1-Q2, as preregistered** (F1 `plans/P1-PREREG.md` §1): a paper design, with encoding,
   simulation construction and correctness argument, for simulating Morita–Ueno Model 1 by a
   narrow-class staggered involution rule. Otherwise a named obstruction.

## Productivity test (fixed now)

The phase is a gem iff at least one of the following holds:
- (i) a written proof at [W] of a statement strictly stronger than F1's NU2, MQ1 and MQ2, which
  constrains a controlled transfer in Q or exposes a hidden assumption in F1's decisive question;
- (ii) P3 stage S1 or S2 proved, or refuted by an explicit exact certificate obtained by hand;
- (iii) for P1-Q2, a complete paper design (encoding, construction and correctness argument), or
  a proved obstruction to one.

Restating NU2, MQ1–MQ3 or F1's questions in other words is a non-gem.

## Skepticism rule (§A.31)

Any branch favourable to the framework gets maximum skepticism. That covers a bounded breach that
heals, a refutation of S, and a positive P1-Q2 design. A positive P1-Q2 design is a comparison
model only: it says nothing about `R_q`
([#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074):
"A universal rule that shares OI's mathematical update form does not establish universality of
OI's actual native rule").

## Computation

None is run. A computation that would be decisive is written as a preregistration and stops
there.
