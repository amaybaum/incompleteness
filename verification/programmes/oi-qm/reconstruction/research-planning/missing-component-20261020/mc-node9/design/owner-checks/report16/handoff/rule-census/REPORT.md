# Exact three-tick census and a multi-field escape

Independent read-only investigation, 2026-10-23. Exploratory finite mathematics;
no preregistered QM acceptance test. No repository modification or communication.
This does not reopen the closed C-SPH-1 numerical checkpoint.

## Result

In the binary scalar, cubic-invariant, center-free nearest-neighbor
second-order class, the following requirements select the linear XOR wave:

1. Zero background is quiescent.
2. One isolated current positive bit, with zero previous field, produces a bit
   at each of its six neighbors on the next tick.
3. Under the uniform full-phase prior, conditional on the port's two initial
   values being zero, its next three values are independent fair bits.

This is an exhaustive statement about 1024 local forces, supported by an exact
light-cone reduction and two independent integer enumeration paths. It is not
a no-go theorem for OI, other alphabets, vector fields, longer-range rules,
nonlinear observation, approximate freshness, or other initial ensembles.
Requirement 2 is only a one-tick pulse response, not a stable particle or a
ballistic carrier. Requirement 3 is not implied by reversibility.

A three-component triangular update avoids the scalar obstruction at the
level of equations: two fields remain linear sources and a third can write
an AND-type raw detector bit. The separate source and gate checks do not yet
establish a common prepared apparatus or its joint public-record law.

## Precisely defined finite class

Let the lattice be a cubic torus of side L >= 7, and work over F2:

    u_i(t+1) = f(u_{i-e_x}(t), u_{i+e_x}(t),
                 u_{i-e_y}(t), u_{i+e_y}(t),
                 u_{i-e_z}(t), u_{i+e_z}(t)) XOR u_i(t-1).

Every force gives a reversible phase map (p,c) -> (c,F(c) XOR p), with inverse
(c,n) -> (n XOR F(c),c). This algebra does not require linearity.

The force is invariant under the 48 signed coordinate permutations of the
cube. If n_k counts opposite pairs occupied by k bits, the ten orbits, in
the code order used here, are:

| index | (n0,n1,n2) | size |
|---:|:---:|---:|
| 0 | (0,0,3) | 1 |
| 1 | (0,1,2) | 6 |
| 2 | (0,2,1) | 12 |
| 3 | (0,3,0) | 8 |
| 4 | (1,0,2) | 3 |
| 5 | (1,1,1) | 12 |
| 6 | (1,2,0) | 12 |
| 7 | (2,0,1) | 3 |
| 8 | (2,1,0) | 6 |
| 9 | (3,0,0) | 1 |

Bit i of a rule's integer code is its value on orbit i. These are local orbit
codes, not Wolfram codes. Independent explicit signed-permutation enumeration
checks that the occupancy labels give exactly the group orbits.

Quiescence is f(0)=0; the pulse response is f(e_j)=1. Fairness of the first
port value requires exactly 32 ones in the 64-entry truth table. These three
conditions leave precisely six rules. One is parity (298); the others all
have algebraic degree four.

## Three-tick law: proof of the finite reduction

Condition u_0(-1)=u_0(0)=0 in the uniform product distribution on the full
previous/current fields. Write h_t=u_0(t), and let A be the six current
neighbors. Then h1=f(A).

Conditional on the entire current field and the previous root value, every
non-root u_j(1) is independently masked by its own fair previous bit. Thus
all those u_j(1) are iid fair and independent of the current field. The root
u_0(1) is the fixed function f(A).

The six odd-distance neighbors at time 1 determine h2. They are independent
of A and the even-distance time-1 variables used for h3. Since f is balanced,
h2 is fair and independent of (h1,h3). This uses the local parity structure
of the radius-three cone; no global bipartiteness of an odd torus is assumed.

There are 18 distinct even radius-two sites other than the root: six axial
sites 2e_j (with signed e_j) and twelve shared diagonals. Denote their time-1
bits by B. They and A are 24 independent fair bits. Define

    G_j(B,h) = f(the six time-1 neighbors of neighbor j,
                 with the root bit set to h).
    h3 = f(A XOR G(B,f(A))) XOR f(A).

This is the entire needed probability space. It is derived from the full
phase prior, not a replacement assumption about independent emitted symbols.

The Python path sums over 12 shared bits, using independence of each of the
six private axial bits to sum a subcube. It employs the autocorrelation count

    C(g) = #{A : f(A)=0 and f(A XOR g)=0}.

Balance implies this also counts {A : f(A)=1 and f(A XOR g)=1}.
Consequently the same C gives the numerator of P(h1=h,h3=0) for either h.
The independent C++ path enumerates all 2^18 B and all 64 A, directly
evaluating h1 and h3 without autocorrelation or subcube summation.

## Exact results

The table's TV is between the three-bit port law and three iid fair bits.
It equals the TV for (h1,h3), because h2 is an independent fair bit.
If p_h=P(h1=h,h3=0), it is |p_0-1/4|+|p_1-1/4|.

| code | degree | distance from XOR truth table | p_0 | p_1 | TV |
|---:|---:|---:|:---:|:---:|:---:|
| 298 | 1 | 0 | 1/4 | 1/4 | 0 |
| 440 | 4 | 12 | 32507/131072 | 135895/524288 | 5867/524288 |
| 270 | 4 | 24 | 8339/32768 | 8259/32768 | 107/16384 |
| 330 | 4 | 24 | 8259/32768 | 8339/32768 | 107/16384 |
| 412 | 4 | 36 | 1/4 | 131513/524288 | 441/524288 |
| 472 | 4 | 36 | 29907/131072 | 146359/524288 | 26731/524288 |

The smallest nonlinear defect in this finite class is 441/524288, about
0.00084114. It is not an error floor for other architectures or a claim that
bounded approximate equivalence is impossible. Every nonlinear candidate has
an explicit two-input AND slice, allowing fixed other inputs and input/output
bit complements. Their failure is therefore a freshness failure, not an
absence of elementary nonlinear gate capability.

For the surviving XOR rule, the established frontier argument gives iid port
values throughout any no-wrap horizon, conditional on the initial port pair.
For the present classification only the first three are needed.

## Additional controls and the amplitude-flip question

Each candidate is also checked against actual updates on an L=7 cubic torus:
24 deterministic full phases per rule reproduce the transformed-cone h1/h3
formula. These are identity spot checks, not the probability enumeration.

An isolated positive pulse produces six next-tick deviations for all six
candidates. On the uniform-one background, an isolated hole produces six
deviations for 270, 298, 330 and zero for 412, 440, 472. Thus passing the
positive pulse test does not imply passing the complementary-background test.
Even passing both pulse tests does not establish general amplitude-flip
covariance: 270 and 330 still fail that property.

For the full binary second-order rule, simultaneous flipping of all old and
current bits commutes with evolution exactly when f(complement(x))=f(x).
Among the six balanced pulse-responsive rules, only XOR satisfies this.
This is a separate conditional selector; it is not used to exclude the other
five in the three-tick census.

Pinned manuscript context:
[SM §2.7 and §§3–4.1](https://github.com/amaybaum/incompleteness/blob/e982b346347f1fd319769c39c6c2d8772cc86ab7/papers/SM.md)
discusses amplitude-shift/scale gauge and labels its structural status open;
§3 gives the second-order inverse; §4.1 explicitly classifies the linear
nearest-neighbor branch and distinguishes functional center independence
from statistical independence. We do not promote amplitude-flip covariance
to an established OI axiom. Nor does this computation establish priority
relative to the cellular-automaton literature.

## Explicit escape: three fields, one reversible update

Let A,B,D be binary fields on the same cubic lattice, and let S denote XOR
over the six neighboring sites. Define the time-independent local update

    A(t+1) = S A(t) XOR A(t-1)
    B(t+1) = S B(t) XOR B(t-1)
    D(t+1) = S D(t) XOR S(A(t) B(t)) XOR D(t-1),

where AB is pointwise Boolean multiplication. This vector-valued force is
center-free, nearest-neighbor, translation-invariant and cubic-invariant.
Its phase map is bijective by the same second-order inverse. The full site
alphabet now has eight states, not two; the field components are distinguished
and coupled asymmetrically. OI has not selected this architecture or coupling.

A and B evolve independently of D. Under the uniform full-phase product prior,
their source-only laws are exactly those of the previously proved linear wave,
including the bounded frontier freshness result with source-port readiness.
An isolated A pulse spreads on its first tick, and if B and D are initially
zero they remain zero while A evolves. There is no detector-to-source feedback
in this deliberately triangular construction.

For an elementary gate, prepare D's old target and current neighbors to zero,
put A_j=a and B_j=1-b at one neighbor j, and make all other neighbor products
zero. Then the next raw detector bit is D_target=a(1-b). This reproduces the
small crossing predicate that cannot be an affine raw-bit read of the purely
linear system. A two-site version of the same force has all 4096 phase states
enumerated, a unique image and correct inverse for each, and truth table
[0,0,1,0] in input order (a,b)=(0,0),(0,1),(1,0),(1,1).

These are deliberately separate claims about different preparations. The
uniform source ensemble is not the prepared gate ensemble. The inverse and
raw gate do not supply the preparation dynamics, a persistent latch, a clock,
an angular emission law, a reset, or access closure. Source-only freshness
does not automatically extend to conditioning on detector records. This is
an algebraic escape and a concrete next candidate, not a native apparatus pass.

## Next investigation

Stop searching the enumerated scalar class for an exact nonlinear source/gate
combination. The complete census already answers that restricted question.
Investigate the vector candidate's *joint* preparation and readout instead:

1. Specify a bounded physical readiness operation and native detector/clock
   registers, including what the observer can inspect and when.
2. Derive the conditional law of the source and detector together after that
   readiness operation and adaptive calls. Do not import fresh random symbols
   or infer the result from source marginals.
3. State the emission/readout map and test the four complete-record relations
   from the joint-record handoff, including failures, waiting counts, time and
   final reads. Those remain the operational target; the present census does
   not evaluate them.

An engineered gate may help construct a model, but it cannot by itself explain
why OI selects the projected-area law or which physical records are inaccessible.
No full-equivalence claim follows from this handoff.

## Reproduction record

The Python checker was run normally and with -O, then copied to a separate
temporary directory and replayed in both modes. All four stdout streams were
byte-identical. Its explicit checks stay active with -O. The C++ executable
independently enumerated all 2^24 cone assignments for each of the six rules;
every integer count agrees exactly with the Python fractions. The archive
contains both sources and both expected outputs, plus a checksum manifest.
No floating-point arithmetic is used in either checker.

All probabilistic conclusions here use the stated uniform full-phase prior.
No energy-shell typicality theorem or energy-conserving apparatus construction
is supplied.
