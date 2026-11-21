# NATIVE-UNIV, phase 3: choosing the next native-universality test (plan)

**Standing.** Writer's plan, committed before the design and preregistration it governs. It is
design-level only. Authorization: owner `amaybaum`,
[#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306)
(Group B, native universality: "plan the next test"). New computations and implementation need their
own authorization ("New scientific execution stays behind its existing authorization gates"). The
selection standard is
[#1169 c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480)
item 6: identify "which computation closes a specific, decision-relevant scientific gap and can
distinguish competing hypotheses."

- **Base.** Stacked on `92cb2350`, the last reviewed head of #1499. Its record is `P2N`:
  `verification/programmes/oi-qm/reconstruction/native-univ-p2-20261121/`. F1 is
  `…/native-univ-feasibility-20261121/`. Both are unchanged here.
- **Object.** Q = `R_{2^16}` on `ℤ³`, OI's native rule at its working reference alphabet
  (#1169 c.7064226074 item 3.2). NU8 is a comparison model only, and it plays no part in this
  selection.

## Question

Which single test, among the candidates below, best distinguishes the competing hypotheses about
whether Q can realize a controlled interaction?
- (a) the bounded-breach question, given NU2–NU7;
- (b) P3 stage S1 (the spreading proof);
- (c) whether some Q gadget realizes a controlled interaction.

The hypotheses are:
- **H0:** no controlled transfer of a line signal exists in Q within a stated native class;
- **H1:** one exists.

For each candidate, state what it would decide, its cost class and its controls. Choose one and
preregister it in full. Do not run it.

## Productivity test (fixed now)

The phase is productive iff it yields a preregistration that meets all three conditions:
- its decision rule can return each of H1-supported, H0-for-the-stated-class and INCONCLUSIVE,
  and every outcome is generated from measurements;
- every requirement it tests is exact, not horizon-limited, or is stated as horizon-limited where
  it is;
- it has a positive control that drives the classifier to a pass, and countercontrols that fail.

If no candidate meets these conditions, the outcome is **INCONCLUSIVE (no decision-relevant test
identified)**, together with the reason. A comparison of candidates that ends without a full
preregistration is a non-gem.

## Constraints

- No computation, beyond replaying the existing exact checks.
- Each result carries (N)/(I) labels (#1169 c.7064843184) and Established / Assumed / Missing
  (#1169 c.7064859041).
- Phase-3 inputs are used where relevant, and none is assumed beyond its review standing.
  R-READ is treated as unresolved.
