# NATIVE-UNIV, round 4: the next proof step on R_q (plan)

**Standing.** Writer's plan, committed before the derivation it governs. The commit order
establishes the order of the commits only. Paper only: no computation, no implementation.

**Authorization.**
[#1169 c.7067281228](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7067281228),
track "Native universality: next proof step on R_q (PLANAR-TURN stage 1 stays blocked)". Design and
paper research only.

**Base and inputs.** Stacked on `81bb20bc`, the head of #1515 confirmed with nits; PLANAR-TURN is
`…/native-univ-p3-20261121/`.
- P2N (`…/native-univ-p2-20261121/`) at `36fef943`, with the owner-approved NU5 correction: for
  bent junctions `cl₂(lines ∪ R)` is an infinite sector, and the transfer criterion is
  leak-freeness relative to `lines ∪ R`.
- F1 (`…/native-univ-feasibility-20261121/`), with P3's preregistration `plans/P3-PREREG.md`.

NU8 is a comparison model only and is not used.

**Object.** Q = `R_{2^16}` on `ℤ³` at uniform backgrounds `c`. The family `R_q` is used only where a
statement is uniform in `q`.

## Question (depth-first)

1. **P3 stage S1** (F1 `plans/P3-PREREG.md`): every single-site seed `(a, b)` with
   `max(|a − c|, |b − c|) ≥ 2` has unbounded support. Prove or refute it. A refutation needs an
   explicit orbit with an exact periodicity certificate and an exhibited excursion (P3 §2).
2. **If S1 closes either way:** state what follows for the decisive question (the leak-free
   controlled transfer) and for PLANAR-TURN's class. In particular, say whether the result makes
   PLANAR-TURN's expected narrow H0 less decision-relevant.

## Productivity test (fixed now)

- **Gem iff one of the following:**
  - (i) S1 is proved;
  - (ii) S1 is refuted by an explicit orbit, given with every tick written out and with the
    certificate argument;
  - (iii) a structural theorem about Q's configuration dynamics, strictly stronger than NU2–NU7,
    that changes which class of gadgets a decisive test must cover.
- **INCONCLUSIVE** is an allowed outcome: the attempt stops with the step at which it stopped.
- **Non-gem:** a restatement.

## Rules

- **Layer.** Every result is a statement about Q's configuration dynamics (the ontic layer). None
  is stated at the layer of effects, instruments, accessible algebras or Born-form readouts. No
  operational claim is made.
- **Labels.** (N)/(I) by assumptions (#1169 c.7064843184), and Established / Assumed / Missing
  (c.7064859041).
- **Skepticism (§A.31).** A refutation of S1 is favourable to the framework: it would supply a
  non-spreading excursion. So it gets maximum skepticism:
  - every site and tick written out;
  - the odd symmetry of `G` checked;
  - the window of U1 Lemma 2.1 checked;
  - consistency with NU3 (the orbit's closed hull must have an in-range boundary at every tick).

  An exact re-run would be a computation. It is preregistered, not run.
