# Preregistration: composition lemma for raw AND aggregation under the report18 rule

Written 2026-10-23 before any search in this directory. Exploratory research; no repository writes.

## Fixed dynamics (unchanged)
U(t+1) = H(S U(t)) xor U(t-1), U = (A,B,D), H(a,b,d) = (b, d, a xor bd), S = XOR of the six nearest neighbours,
cubic torus or infinite lattice. No change of rule, field order or interface during a run.

## What counts as a composition lemma (decision rule)
A **builder** B(n) is an explicit algorithm, stated in REPORT.md before held-out testing, that for every n >= n0
outputs: the initial positions, slice (current/previous) and field of each of the n independent inputs; every affine
copy (position, slice, field, which input); the receiver site; the deadline T(n). It must also state closed forms
for T(n), the copy count m(n) and the receiver-cone constraint count
C(n) = 3[v(T) + v(T-1)] - (number of input and copy slots) + m(n), with v(r) = |L1 ball of radius r|.

The builder **succeeds** iff, for every n used during discovery AND for each preregistered held-out size, all of:
1. On the zero-background lattice (finite box larger than the receiver cone), the receiver's raw D register at T(n)
   equals AND_n for all 2^n inputs, and its algebraic degree (Moebius transform of the truth table) is n.
2. On two dense full-torus backgrounds (every bit outside the pinned receiver cone uniformly random, seeded), with
   current B_T and previous B_(T-1) pinned to zero except input and copy slots, the same holds.
3. A countercontrol is non-vacuous: removing one copy (if m(n) > 0) or releasing one pinned bit in the cone to 1
   makes the output wrong for some input.

**Held-out sizes, fixed now: n = 9 and n = 12.** They are not run, and no layout at these sizes is inspected, until
the builder is written down in REPORT.md. Discovery may use any n <= 8 (and n = 10, 11 are also excluded from
discovery). If the builder needs n0 > 9, the held-out sizes become n = 12 and n = 13 instead; this substitution is
the only permitted change and must be stated.

If no builder is found, the outcome is a negative result with the wall characterised: the deepest branch reached,
its explicit check and the reason it stopped. A finite search failure is not an obstruction theorem.

## Verdict generation
Verdict lines are printed by the checker from measured truth tables and only if every control in its run is green.
