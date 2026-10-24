# Preregistration: a bounded native instrument under the report18 rule

> Written before any construction code or computation for this investigation. Exploratory research record; it
> adopts no premise. Rules are fixed here; expected numbers are not.

## Fixed rule and scope

- **Dynamics.** The report18 update on a cubic torus: U' = H(SU) ⊕ U_old, with U = (A, B, D),
  H(a, b, d) = (b, d, a ⊕ bd), and S the six-neighbour XOR. It is used unchanged.
- **Preparation menu.** The eight report13 preparations P_w for w ∈ {±X, ±Y, ±Z, ±R}, with R = (4/5, 3/5, 0).
- **Read settings.** The menu axes a ∈ {X, Y, Z, R}. Outcome o ∈ {0, 1}, with 1 meaning "+a".
- **Instrument.** It must state four ingredients explicitly:
  1. **prepared distributions:** P_w as an exact law over initial lattice states, including every readiness pin,
     copy correlation and ancilla, with its entropy and readiness cost;
  2. **herald and clock records:** the attempt and failure records, and the tick at which each accessible register
     is read;
  3. **side-register access:** every accessible register, stated as a list. Everything else is inaccessible by
     stipulation, and that stipulation is part of the interface;
  4. **outgoing state:** the register that carries the post-measurement system, and its law.
- **What may be supplied.** Supplied ingredients (an ideal herald flag, a biased bit resource, the external tick
  count) may be used if each is named as supplied. Anything called native must be computed under the fixed rule.

## Questions and decision rules

All probabilities are exact rationals. A record law is a finite atomic measure on the stated accessible record.

- **Q1. Identities, single read.** For each setting a, the complete accessible-record laws K_w satisfy the four
  report13 identities at every record atom:
  - K_X + K_−X = K_Y + K_−Y = K_Z + K_−Z = K_R + K_−R;
  - 5(K_R − K_−R) = 4(K_X − K_−X) + 3(K_Y − K_−Y).

  **Holds exactly** if every identity is zero at every atom. **Fails** otherwise. A failure reports the exact TV
  between report13's witness mixtures A = 13/16 P_R + 3/16 P_−R and B = 1/2 P_X + 3/8 P_Y + 1/16 P_Z + 1/16 P_−Z.
- **Q2. Identities, two sequential reads** (a, then c, for all 16 ordered setting pairs). The rule is as in Q1, on
  the complete record of both reads.
- **Q3. Born values.**
  - A single read gives P(o = 1 | w, a) = (1 + a·w)/2.
  - The second read, given the first outcome o, gives P(o' = 1) = (1 + s·a·c)/2, with s = +1 if o = 1 and s = −1
    if o = 0.
  - Exact equality, or not. This is reported separately: the identities do not imply Born values, and a control
    shows this.
- **Q4. Closure.** Conditional on the complete accessible record of a read with setting a and outcome o (and a
  successful re-preparation herald), the outgoing register's exact law equals the prepared law of P_{s·a}, jointly
  over all its components.
  - **Closure holds** on exact equality.
  - **Closure given the record fails** if the outgoing law conditional on the accessible record differs from it.
- **Q5. Native realization.**
  - **Check.** The record and outgoing registers are computed by the fixed rule on a full torus. The readiness pins
    are stated. Every unpinned, non-prepared bit is filled with each of two dense seeded backgrounds. For every
    assignment of the instrument's input bits, the accessible registers at the read tick must equal the
    register-level map exactly.
  - **Holds** on exact equality in every case. Dense backgrounds are an implementation check; background
    independence itself rests on the causal-cone argument.
- **Q6. Access widening.** The most informative variation: which widened accesses break Q1, Q2 or Q4, with exact
  TVs. The accesses tested:
  - (a) the prepared hidden components not read;
  - (b) the fresh re-preparation bits;
  - (c) the record site read at later ticks, natively, with the readiness extended so that later reads stay
    deterministic in the prepared bits;
  - (d) a herald whose acceptance depends on w.

## Controls (each must be green before any verdict is printed)

- **C-QM (positive).** The exact quantum record law for the same protocols, from the density matrices, satisfies
  all four identities. This checks the identity checker against a known case.
- **C-RANK.** The 4 × 8 matrix of (1, w) has rank 4, and the four relations span its null space.
- **C-ND (negative).** A non-disturbing instrument, whose outgoing register is the unchanged prepared register,
  must fail Q2 (sequential identities) for some setting pair. Otherwise the sequential test is vacuous.
- **C-HER (negative).** A herald whose acceptance probability depends on w must fail Q1.
- **C-AFF (scope).** An affine but non-Born read law must pass the identities. That shows the identities do not test
  Born values, which is why Q3 is separate.
- **C-NAT.** In the native realization, releasing one readiness pin in a device cone to 1 must change some
  accessible register value for some input. Otherwise the native check is vacuous.

## Reporting

- **Verdict text.** It is generated by the checker from measurements, printed only if every control is green.
- **Negative results.** Any is acceptable and is reported as found.
- **Bounded compute.** If a native enumeration would exceed bounded compute, the partial state is reported instead.
- **Depth-first.** The smallest instrument with all four ingredients is built first. Then the most informative
  variation, Q6. Each branch's check and verdict is recorded in REPORT.md.
