# NATIVE-PADIC-1 — a precise no-backflow boundary for the existing OI wave rule

**Status:** research writer result, issue #1010 / draft PR #1011.
Preregistered before the computation in PREREGISTRATION.md.
The following all-state argument is exact algebra; the accompanying
finite regression is a separately controlled check. Neither one
proves that actual OI has p-adic or fractal hidden degrees of freedom.

## Microscopic source, not an invented new dynamical law

The existing native *scalar cubic wave reference* is
papers/oi_lattice_code/trace_out_fractional/wave_eqn.c:
\[
(x_{t+1})_v=\sum_{w\sim v}(x_t)_w-(x_{t-1})_v\pmod q,
\]
where the six oriented nearest-neighbor contributions are counted
with periodic multiplicity. A microscopic state is the ordered
pair (current field, previous field), and the next pair is
\[
W_q(x,y)=(A_q x-y,x).
\]
The inverse is explicitly
\[
W_q^{-1}(u,v)=(v,A_qv-u).
\]
This is the native formula considered in this test; the real-valued
normalized \(\alpha=1/3\) observer-level operator of SM §4.1 is **not**
silently substituted for the microscopic update.

To test a recursive candidate, choose alphabets
\(q_n=2^n\), with reduction homomorphisms
\(\rho_{n,m}:\mathbb Z/2^n\to\mathbb Z/2^m\)
for \(1\le m<n\). This is a **new choice of compatible
alphabet family**, not a theorem that the actual physical carrier
is \(\mathbb Z_2\).

## All-state mathematical no-backflow theorem

**Theorem (for this integer-coefficient rule and congruence
readouts).** Let \(\widehat\rho_{n,m}\) reduce each current and
previous site value modulo \(2^m\). Then for all full states,
\[
\widehat\rho_{n,m}\circ W_{2^n}
 =W_{2^m}\circ\widehat\rho_{n,m},
\quad
\widehat\rho_{n,m}\circ W_{2^n}^{-1}
 =W_{2^m}^{-1}\circ\widehat\rho_{n,m}.
\]
Hence all forward and backward iterates commute with reduction.
If two initial pairs have the same complete low-m projection,
their entire low-m trajectories agree **pointwise**. Their
observable histories under any readout factoring through
that projection are identical.

**Proof.** Reduction modulo \(2^m\) is an additive group
homomorphism. Every output site of \(A_qx\) is the same
finite sum of six input site values, with coefficient 1.
Thus \(\rho_{n,m}(A_{2^n}x)=A_{2^m}(\rho_{n,m}x)\).
The homomorphism preserves subtraction too. Apply this
identity to both coordinates of the explicit step and inverse
formula above; iterate by induction. The proof requires
neither a mixing prior nor a particular initial distribution. □

**Corollary (complete-record law).** If a finer-stage initial
probability has lower-stage marginal \(\mu_m\), the pushforward
probability of **every finite word** of congruence-visible records
is precisely the result obtained by evolving \(\mu_m\)
directly on the lower-stage dynamics. In particular, adding
higher independent Haar digits with the same lower-stage
Haar marginal changes **none** of the lower-digit
finite-time joint laws, accessible memory measures or
recurrence statements. This does not say such a low-level
process is Markov, P-indivisible or quantum: it inherits
whichever properties the chosen lower-level source has.

The inverse limit of these compatible steps is a
continuous reversible \(\mathbb Z_2\)-valued wave map on
the fixed finite cubic lattice. It still fails to provide
new low-digit backflow. Importantly, for any **fixed**
m, the quotient on the complete two-slice fields over
\(\mathbb Z/2^m\) is a finite permutation. Consequently
it has some positive common period \(P_m\), and every
low-m digit observable of the **infinite inverse-limit**
system has an exact common visible return at \(P_m\).
This does **not** imply that the full infinite hidden state
returns, nor one period working for all depths m.
A genuine unlimited-depth coupling mechanism would have
to break this passive factorization or change the
accessible observable class.

## Exact regression and nonvacuity control

The source native_padic_probe.py uses a periodic cubic
L=3 lattice with 27 sites. It tests q=2,4,8,16,32,64
and **12 fixed input preparations per q**. For each
m<n it checks full two-slice factorization at every
step of 16 forward and 16 inverse updates, and tests
paired preparations differing only in digits at or
above m, across the same forward horizon.

The independently executed arithmetic replica passed
**9,344 individual exact controls**. Expected structured
evidence is retained in RESULTS.json, with every
tested q and m recorded. The computation is not
exhaustive over the astronomically large q^54
full-state space. Its general theorem is the algebraic
commutation proof above.

**Positive mutation (outside native OI).** At one
distinguished site, add the second binary digit
of the current field as a **low-valued additive kick**
to the next field before storing the current slice:
\[
\widetilde W_q(x,y)=
(A_qx-y+e_0\,\mathrm{bit}_1(x_0),x).
\]
This update is still a bijection, since its inverse
recovers x from the retained second coordinate, then
recovers y from the first coordinate. However,
for q>=4, the all-zero source and a source differing
only by adding 2 at site 0 have the **same**
low-bit initial state and **different** low-bit
outgoing values at site 0. The exact tests check
both the reversible inverse and this factorization
failure. This positive control prevents a vacuous
test that would reject higher-to-lower influence
no matter which update is supplied.

**Crucial guard:** the positive mutation is **not**
derived from the OI cubic wave law, not the native-Y
nonlinear triple rule, not a physically available
observer intervention, not a QM instrument and not
a gauge-covariant Yang–Mills dynamics. It is only
a mathematical marker for the additional resource
a recursive physical model would need.

## Relationship to existing Lean results

The existing OIBridge.HydroSourceAudit module already
establishes the additivity of the native wave operator
and restrictions on additive coarse variables, under
its explicit hypotheses. This result is compatible:
the low-digit quotient is itself an additive coarse
factor and its dynamics close exactly.

NATIVE-PADIC-1's new contribution is the **particular
cross-q congruence obstruction** and the non-native
reversible positive control; it does not reprove or
replace the existing HydroSourceAudit theorem.
A new narrow Lean bridge can formalize the
reduction/intertwining calculation without claiming
a certified p-adic physical interpretation.

## Implications for recursive sub-states, quantum mechanics and Yang–Mills

This result rules out **one tempting shortcut**:
choose an infinite stack of ever finer binary digits
at every OI scalar site and retain the exact same
integer-coefficient wave step; hope that the additional
digits automatically generate new observer memory,
measurement-context dependence or gauge-field
dynamics. They cannot influence a fixed low-digit
readout under that unchanged rule.

This is not an impossibility result for recursive
fractal sub-states in general. It does **not** address:

- noncongruence/threshold observers that deliberately
  access deeper digits;
- physical interactions that mix levels, nonlinear
  native-Y constructions or a new sourced apparatus;
- continuous link variables with non-flat gauge
  curvature, Wilson-vs-squared action selection;
- the observer-level real wave lift,
  the 5 operational QM completion conditions,
  Bell causality, C4/readback, or physical boundary
  entropy from the full hidden tower.

**Verdict:** ACCEPT the narrow algebraic
NO-DEEP-TO-LOW-M PASSIVE BACKFLOW statement for the
specified modular cubic wave family, pending independent
review; the explicit reversible mutant is a
positive **non-native** control. **BLOCKED** on sourcing
a genuine scale-mixing mechanism and repeatable
public measurement interaction from the same OI
physics. No change to the manuscripts or publication
claim statuses is authorized.
