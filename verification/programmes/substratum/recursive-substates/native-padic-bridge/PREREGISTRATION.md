# SUBSTATE-2 / NATIVE-PADIC-1 — preregistered source test

**Active research-only** under issue #1010 / draft PR #1011.
This document is committed before running its new exact tests.
No manuscript edits, new physical premises or acceptance designations.

## Question and exact native reference

Does extending the **actual OI scalar cubic two-slice wave rule**
from finite alphabets to compatible residue rings of size 2^n
allow finer digits to influence a fixed coarse digit readout,
without modifying the microscopic update?

The existing C reference is
papers/oi_lattice_code/trace_out_fractional/wave_eqn.c.
For each site v of the periodic cubic torus,
\[
 x_{t+1}(v)=\sum_{w\sim v}x_t(w)-x_{t-1}(v)
 \pmod {2^n}.
\]
The oriented neighbor sum has six terms (including periodic
multiplicities); the full two-slice update is reversible.
The normalized alpha=1/3 real observer operator in SM §4.1
is separate and is NOT asserted to equal this native rule.

## Preregistered theorem and controls

1. **Congruence (theorem target).** For m<n, reduction modulo 2^m
   commutes with the step, inverse and all iterations of the
   native integer-coefficient wave rule. Therefore two initial
   microscopic pairs with equal low-m digits have identical
   future low-m *passive* observations. This is an all-state
   algebraic statement, not a claim derived from finite testing.
2. **Exact test range.** Periodic L=3 cube, 27 sites,
   q=2^n, n=1,...,6. Fix twelve deterministic input
   preparations including zero, unit/all-one, coordinate
   polynomials, delta and seeded arithmetic families.
   For every m<n, compare the reduced 2-slice evolution
   with direct low-q evolution across 16 forward and
   16 inverse steps. Every stage checks full-state inverse.
   This is a finite regression, NOT exhaustive over q^54.
3. **Nonvacuous positive-control mutation.** Define an
   explicitly **non-native** reversible update that adds
   bit1 of the current origin field to the next origin field:
   \[
   x_{t+1}(0)\leftarrow x_{t+1}(0)
    +\mathrm{bit}_1(x_t(0))\pmod {2^n}.
   \]
   Since the current slice is retained, the corresponding
   two-slice map still has an explicit inverse. At n>=2,
   a pair of initial states differing only in bit1
   at the origin must yield different *low-bit* outgoing
   values there. This is an added scale coupling, NOT
   a native OI interaction or QM prediction.
4. **Observation/horizon controls.** Read out the lowest
   current-field bit at the origin and, separately, all
   low-m bits of the full two-slice state. Lower levels
   inherit their own recurrence/memory; no deep digit
   backflow can create new low-bit laws under the passive
   congruence readout. Do not infer a common exact
   infinite-carrier recurrence period from finite q.
5. **Scope limits.** Do not rule out noncongruence readouts,
   nonlinear observer interventions, the native-Y nonlinear
   triple rule, or other derived scale couplings. Preserve
   the finite-horizon S⇔D⇔Qfb representation,
   readback/C4, boundary-entropy, gauge-action, locality
   and full QM operational sourcing as independent gates.

**Decision:** ACCEPT this narrow no-backflow result only if the
general reduction argument and every numerical control hold
and the mutated reversible positive control fails reduction
as predicted. Otherwise REVISE. Even ACCEPT cannot promote
substate fractality, quantum coherence or Yang–Mills action.
