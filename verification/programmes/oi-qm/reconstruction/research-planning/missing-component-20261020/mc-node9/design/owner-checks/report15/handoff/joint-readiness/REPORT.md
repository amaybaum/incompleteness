# Joint readiness, past-record freshness, and detector reuse

Independent read-only investigation, 2026-10-23. This continues
`OI_rule_census_handoff_v1.zip`, SHA-256
`8705f2b267734cd3baf81a6d05d791106364a940979df9bbf43878ef81feeead`.
No repository edits, commits, comments, pushes or workflow launches were made.
The C-SPH-1 numerical checkpoint remains closed.

## What this establishes

A single explicitly conditioned ensemble supports both the first nonlinear
detector write and bounded source freshness, even after conditioning on all
earlier source and detector records at the same port. That closes the
separate-ensembles gap for the *first* write of the three-field candidate.

The same update does not automatically implement that write again on each
tick. Its second raw detector bit has error probability exactly 1/2 under
local readiness, or 4095/8192 when the entire detector starts blank. The latter
is verified by two distinct exact calculations. At every even tick there is
a structural lower bound of 1/4 for the repeated raw AND task under the stated
ensemble. Restricting reads to odd ticks also has a concrete counterexample.

These are results about a particular source/gate candidate. They are neither
a quantum-equivalence verdict nor an impossibility theorem for delayed
detectors, different observation maps, or OI. The earlier handoff only claimed
an elementary gate slice, not repeated detector correctness; the present
investigation tests whether that slice extends to a reusable detector.

An explicit revised local map does preserve the raw product on repeated calls.
It is obtained by conjugating three independent linear waves, and needs a
different, correlated readiness condition. Its full bounded port-record law
is derived below. This is an engineered gate construction: the same procedure
works for every two-input Boolean function, so it is not a selection argument
for quantum probabilities.

## Fixed dynamics and observation window

Use binary fields A, B, D on a cubic torus, side L > 2K, with K >= 2. Let S
be XOR over the six nearest neighbors. The update is unchanged:

    A(t+1) = S A(t) XOR A(t-1)
    B(t+1) = S B(t) XOR B(t-1)
    D(t+1) = S D(t) XOR S(A(t)B(t)) XOR D(t-1).

Multiplication is pointwise Boolean AND. This is a center-free, cubic-invariant
local second-order map with inverse (c,n) -> (n XOR F(c),c). A and B do not
receive feedback from D. The initial prior is uniform counting on the full
two-time phase space, not an energy shell.

Fix a port o and its neighbor e=o+e_x. A call is a passive reading; calls do not
alter the update. Define H_t=A_o(t), M_t=B_o(t), Z_t=D_o(t). For the freshness
theorem the observer may see the whole prefix (H_s,M_s,Z_s), s<t, or any
function of it, plus the initial readiness record. Call times may depend on
that prefix and independent protocol randomness. They must be chosen before
the current reading and be strictly increasing; rereading the same tick is
not a new sample. There is only one fixed port in this theorem.

The intended reusable gate tested here is Z_t=H_t M_t. It is a minimal
nonlinear detector task, not the projected-area emission law. AND-NOT has
the same even-tick obstruction because it has the same quadratic term.

The index t is a native update count in the mathematical model. No physical
clock register, calibrated time, or autonomous scheduling mechanism is derived
by naming this index.

## One shared readiness event

At one fixed initial time, with no preceding observation history, condition
on the following 22 bits being zero:

| registers | number |
|---|---:|
| A_o(-1), A_o(0), B_o(-1), B_o(0) | 4 |
| A_j(0), B_j(0) for the five neighbors j other than e | 10 |
| D_o(-1), D_o(0), and D_j(0) at all six neighbors | 8 |

Call this event E. Its probability is 2^-22 = 1/4194304 under the prior.
All unmentioned bits remain independent and fair. In particular a=A_e(0)
and b=B_e(0) are free. Direct substitution gives

    (H_1,M_1,Z_1) = (a,b,ab).

This is the same ensemble for both the source and the first gate. Nothing
fresh is inserted afterward. E singles out a prepared direction; it does not
derive rotationally invariant source statistics.

For a stronger detector control, replace the eight D constraints by
D(-1)=D(0)=0 everywhere on the finite torus. Call this E_blank. Its probability
is 2^-(14+2L^3). The same source prior and first gate remain. Blanking only the
needed initial detector light cone would give the same bounded records.

These are *readiness events*, not a derived mechanism that prepares them.
Recognizing E at one fixed time is an explicitly supplied observation rule.
Waiting until E first occurs, while retaining previous failed checks, is a
different conditioning problem and is not covered. Nor is an external swap
with clean registers being silently counted as part of this native update.

## Freshness theorem with nonlinear detector history

For each t=1,...,K, put

    F_t=A_{o+t e_x}(0), G_t=B_{o+t e_x}(0).

Neither readiness event constrains these variables. They are independent fair
bits, independent of all other initial bits. The unique extreme path gives

    H_t = F_t XOR R_t,    M_t = G_t XOR Q_t,

where R_t and Q_t do not contain F_t or G_t. Every port record at an earlier
time s<t depends only on the radius-s initial cone. It therefore contains
neither F_t nor G_t. The no-wrap condition prevents a shorter periodic path.

Condition on all initial bits except F_t,G_t. Every earlier record, readiness
record and predictable call decision is then fixed, while H_t,M_t remain an
independent uniform pair. Averaging the other initial bits proves

    P(H_t=h,M_t=m | E, all earlier port records) = 1/4.

The same holds for E_blank and for any coarser earlier record. Thus adaptive
passive calls at this port obtain fresh source pairs *before current-event
selection*, despite nonlinear earlier detector records. The proof does not
require those earlier detector records to be linear functions.

The argument also applies to other causal detector updates of radius at most
one, provided the source equations remain unchanged and readiness leaves the
specified frontier bits independent. It does not establish access closure:
observing the six source neighbors at time t-1, together with the port at t-2,
determines the next source pair exactly. That is a positive countercontrol,
with TV 3/4 from the uniform pair once those readings are given.

Including the current detector bit is also a different statement. Here
Z_1=1 forces (H_1,M_1)=(1,1). The source pair after that selection has TV 3/4
from uniform. Past-record freshness does not imply mark independence from a
same-tick herald.

## Exact complete law through two ticks

At tick 1 the four triples (0,0,0), (0,1,0), (1,0,0), (1,1,1) each have
probability 1/4. Under E, an unprepared detector bit D_{2e_x}(0) occurs in Z_2
with coefficient one. It is independent of the entire source history and of
Z_1. Consequently (H_2,M_2,Z_2) is uniform on eight triples, independent of
the first triple. The second AND write therefore has error exactly 1/2.

This could have been just insufficient detector preparation. E_blank tests
that explanation and still fails. Write, for the six signed neighbors j,

    U_j=A_{2j}(0), V_j=B_{2j}(0),
    R_j=A_j(1), Q_j=B_j(1).

Here 2j denotes the axial site twice as far from the port. Conditional on the
current source fields, each R_j and Q_j contains its own independent previous
neighbor bit. Therefore U,V,R,Q are independent uniform six-bit vectors.
The twelve shared diagonal sites cancel in the sums because each is counted
twice. The native equations reduce exactly to

    H_2 = parity(R),    M_2 = parity(Q),
    Z_2 = U dot V XOR R dot Q.

The first triple uses different source variables, so it is independent of
this second triple. The entire two-tick record law is thus the product of
the first-tick table above and the following table:

| (H_2,M_2) | P(pair,Z_2=0) | P(pair,Z_2=1) |
|:---:|:---:|:---:|
| (0,0) | 1025/8192 | 1023/8192 |
| (0,1) | 1/8 | 1/8 |
| (1,0) | 1/8 | 1/8 |
| (1,1) | 1/8 | 1/8 |

It follows that

    P(Z_2 != H_2 M_2 | E_blank) = 4095/8192.

Independent verification expands the actual local recurrence as a Boolean
polynomial. The error is a bilinear form in the A and B initial variables,
with matrix rank 12 over F2. For a rank-r bilinear form of independent fair
vectors, averaging one vector gives mean sign 2^-r, hence probability of one
(1-2^-r)/2. At r=12 this gives the same 4095/8192.

Thus the defect remains with ideal initial detector blanking. It is not
explained by resource reuse or loss of source freshness. The dynamics mixes
several product contributions instead of repeating the isolated first gate.

## Structural even-tick obstruction; odd-tick control

The detector at time t is at most bilinear in the initial A and B fields,
plus a linear contribution from its own initial field. Consider the coefficient
c_t of F_t G_t in Z_t. The unique extreme path in the D propagation contributes
c_(t-1); the product forcing at the extreme neighbor contributes one. The
two-step-old D term cannot reach the frontier. Therefore

    c_1=1,    c_t=c_(t-1) XOR 1,    c_t=t mod 2.

At even t, after fixing every other initial bit, Z_t is affine in F_t,G_t,
while H_t M_t has quadratic coefficient one. An affine Boolean function of
two bits disagrees with AND (including shifted inputs) on one or three of
the four inputs. Consequently every even-time call, chosen using only past
records, has raw AND error at least 1/4. This holds for E and E_blank; it is
not a bound after filtering on the current detector outcome.

The bound is attained on a simple conditional slice: start A and B with only
their respective free bits at (t,0,0), all other fields zero. At even t the
source pair is those two bits and the detector bit is zero. The checker
replays this at t=2,4,6,8.

Odd ticks do not solve the general task. With all previous fields and D zero,
put one A bit at (-3,0,0) and one B bit at (0,-3,0). This satisfies readiness.
At the port the first four triples, t=0,1,2,3, are

    (0,0,0), (0,0,0), (0,0,0), (1,1,0).

The two pulses are six edges apart. Their supports cannot meet before tick 3,
so no product can yet have reached the detector. This is a deterministic
odd-tick failure. A gate with an explicitly specified later latency is a
different target; no impossibility claim for it is made here.

## Unscreened herald control

Dropping the ten source-neighbor zero constraints makes the first write the
dot product of two independent six-bit neighbor vectors. Exact enumeration
gives P(Z_1=1)=63/128 and P(H_1=1 | Z_1=1)=32/63. Thus even without enforcing
the isolated AND slice, this detector does not automatically provide an
independent herald and mark. This is a selection-bias control, not a witness
against quantum preparation equivalence: no quantum preparation menu has
been defined for this candidate.

## A working local repair, with changed dynamics and readiness

The original failure does not require abandoning reversible local dynamics.
Start with independent linear wave fields A, B, C, and change coordinates
pointwise at both phase times by

    D = C XOR AB,    equivalently C = D XOR AB.

This coordinate change is an involutive finite bijection. Conjugating the
three-wave phase map by it produces the following autonomous local rule:

    A' = SA XOR A_old
    B' = SB XOR B_old
    D' = SD XOR D_old XOR S(AB) XOR (SA)(SB)
         XOR (SA)B_old XOR (SB)A_old.

All current fields on the right are at neighboring sites, and all old fields
are at the target site. The rule is cubic-invariant, translation-invariant
and radius one as a phase-space update. It is bijective by conjugacy, with
inverse G composed with the inverse three-wave map composed with G.

This is a changed model. In particular D' now couples to old A and B, so it
is outside the earlier strict componentwise form F(current) XOR same-field-old.
It is still a local finite reversible phase map. No claim is made that OI
selects this coupling or its coordinate interpretation.

Direct algebra gives, at every site and for arbitrary initial data,

    C' = D' XOR A'B' = SC XOR C_old.

Therefore the readiness condition C(-1)=C(0)=0 is invariant, and on it

    D_i(t)=A_i(t)B_i(t) for every site and every time.

This is a raw register identity under the revised update, not a claim that
an observer externally decoding A and B has written D. It tracks the product;
it does not latch the first success or keep a persistent event history.

The revised readiness event E_product imposes C(-1)=C(0)=0 everywhere and
A_o(-1)=A_o(0)=B_o(-1)=B_o(0)=0. It does not impose the five-neighbor source
zeros or the original blank-D condition. Under uniform full-phase counting,
its probability is 2^-(2L^3+4). For every source configuration satisfying the
four port constraints there is exactly one allowed two-time D configuration.
Thus the source distribution remains exactly uniform on those constraints.
In the (A,B,C) coordinates the resource is a clean C field; in the raw
coordinates it is the supplied correlation D=AB on both initial slices.

No autonomous process creating or verifying this event has been derived.
In particular, repeatedly searching for readiness and recording all failed
attempts is not licensed by the fixed-initial-time calculation. The corrected
model has exchanged the original detector failure for explicit changed dynamics
and a stronger readiness requirement, not obtained those resources for free.

## Complete bounded record law of the repaired gate

Conditional on E_product, the source frontier theorem applies to A and B.
At the port D_t=H_t M_t, so its past adds no information beyond past source
values. For any K with L>2K, the entire port record is exactly

    P((H_t,M_t,Z_t)=(h_t,m_t,z_t), t=1,...,K)
       = 4^-K product_t 1{z_t=h_t m_t}.

Predictable passive calls select fresh triples from this process. Reading
only Z gives iid Bernoulli(1/4) bits; the first positive reading among k
consecutive calls has probability (3/4)^(k-1)/4, and m failures have probability
(3/4)^m. These are native update-count records under the supplied interface,
not a derivation of a physical clock or crossing-time distribution. If Z is
used as a herald, the contemporaneous H,M pair is (1,1) on success; independent
emission marks or an angular distribution are not thereby supplied.

The record law is exact for this gate and window. It is not the four
preparation-equivalence identities: there are no X/Y/Z/R stations, carrier
states or quantum readout axes in this construction yet.

## Why the repair does not select a physical measurement law

Replace AB by any Boolean function g(A,B) and set D=C XOR g(A,B). The same
conjugacy gives a local reversible update and the invariant clean condition
D=g(A,B). All 16 two-input Boolean functions pass an explicit finite check.
Thus local reversibility, cubic spatial symmetry, uniform counting and this
form of readiness do not pick AND from that family, much less the
projected-area angular law. The chosen predicate has been put into the update
and the initial correlation. This makes the repair a useful calibration
construction, but not an OI derivation of measurement physics.

## Verification and next decision

The standard-library checker uses exact sets, integers, fractions and binary
matrix elimination. It checks symbolic frontier coefficients and exclusion
from past records through tick 6; all 1024 assignments of a ten-variable
initial slice by a separate direct L=9 torus update; history-conditioned
uniformity on that slice; the full second-tick law and independent error rank;
blank-detector pulse witnesses; and both access/selection countercontrols.
The slice enumeration is a control of the proof and implementation, not an
enumeration of the full phase space. The theorem itself covers any finite
no-wrap horizon under its stated assumptions.

For the repaired map, an exact polynomial identity checks the full 21-variable
cubic stencil. All 4096 phase states on a separate two-site graph have a
unique image and correct inverse; all 256 clean-source phase choices track
the raw product through eight ticks. Sixteen full cubic-lattice phases, half
with nonzero C, agree with an independently evolved C wave over eight ticks.
The dirty-C control produces a raw-product error, confirming that readiness
matters. All 16 Boolean predicates track under their respective conjugated
maps. These finite checks accompany the all-time conjugacy proof.

The final checker completed normally. A copy in a separate temporary directory
then reproduced its stdout byte for byte, both normally and with Python -O.
All checks remain enabled under -O; no floating-point arithmetic is used.

The next substantive target is the physical choice of emission/readout law
and a native preparation/clock mechanism, using this repaired gate as a
calibration control. Further tuning of gate truth tables would not resolve
that selection problem. A proposed apparatus must name how it creates its
ready correlations, what timing and failure records remain visible, and why
its carrier coupling produces the required angular law.

There is still no station-indexed emission kernel here, so the four
complete-record preparation identities cannot yet be evaluated. No quantum
probability, native clock, angular law, reset, access closure, energy-shell
preparation, or composite behavior has been derived. The results separate
joint source freshness, repeated gate computation, and physical law selection:
the first two can be made compatible conditionally; the third remains open.
