# From record tests to a detector interaction

Exploratory read-only handoff v1, 2026-10-23. No repository edits, commits,
comments, or workflow launches. This is not a C-SPH-1 rerun or a new apparatus
acceptance test. The new nonlinear rules below are diagnostic candidates, not
adopted OI premises or proposed manuscript corrections.

## 1. Corrections to the review's wording

I read review13 and its checker at
[`e982b346347f1fd319769c39c6c2d8772cc86ab7`](https://github.com/amaybaum/incompleteness/commit/e982b346347f1fd319769c39c6c2d8772cc86ab7),
under `owner-checks/report13/` in the mc-node9 design tree. The numerical
confirmation supports the prior handoff. Three scope refinements are needed.

First, the fourth preparation identity does not fail ONLY in the joint
clock/read record. The reported time-blind TV 0.00063982 is already nonzero.
The clock amplifies the failure to 0.04377046 for the original frames.

Second, J2 does not establish failure on every read axis. The checker combines
the failures with `fourth_fails |= bad`, which asks whether any axis fails.
Independent integer-coordinate enumeration of its alternative frames gives:

| Read axis | Nonzero fourth-relation residuals, positive-read timestamp atoms |
| --- | --- |
| X | 245 / 245 |
| Y | 245 / 245 |
| Z | 0 / 245 |
| R | 245 / 245 |

These are n=15 results. The negative-read residual has the opposite sign; the
common failure mass contributes zero. For Z reads, X, Y and R emissions all
have a symmetric transverse Z projection conditional on the timestamp, so the
fourth relation vanishes identically. Z-preparation columns have zero
coefficient in that relation. The correct statement is that the three
antipodal identities hold throughout the tested family, while the fourth
fails for some protocols in that family.

Third, two tested transverse frames establish robustness to those choices,
not a universal frame theorem. The next section supplies a universal but much
weaker bound for the same exact-clock model.

I did not rerun the coordinator's full J1-J5 program. The checks here target
these distinctions and the next dynamical step; the prior handoff remains
unchanged.

## 2. A witness for every transverse frame of R

Keep the rotated-source candidate and the same reference-equivalent mixtures

\[
 A=\tfrac{13}{16}R^++\tfrac3{16}R^-,\qquad
 B=\tfrac12X^++\tfrac38Y^++\tfrac1{16}Z^++\tfrac1{16}Z^-.
\]

Keep X,Y,Z frames as in either the handoff or review13; both choices have
unbiased transverse X reads. Allow ANY orthonormal transverse frame for R,
including irrational frames. The X component of the R carrier, up to a
positive common scale, is

\[
 W=\tfrac45 S_x+bS_y+cS_z,\qquad b^2+c^2=\tfrac9{25}.
\]

Consider the public timestamp T=1/(5n). In a successful trial T=D/(5S_x),
with 1<=S_x<=n and integer D>=1. This timestamp forces S_x=n and D=1.
Conditional on it, S_y and S_z remain independent sums of n fair signs.
The transverse part Z=bS_y+cS_z has mean zero and variance 9n/25.

The one-sided second-moment bound gives

\[
 \Pr(W\leq0\mid T=1/(5n))
 \leq \frac{9}{16n+9}.
\]

For completeness, this bound follows by applying Markov's inequality to
(Z-h)^2 on Z<=-a, then choosing h=Var(Z)/a, with a=4n/5. No Gaussian
approximation or numerical optimization is used.

For A, its R+ component alone therefore contributes at least
(13/16)[1-9/(16n+9)] to the conditional positive-read probability. The R-
component contributes a nonnegative amount. B's conditional positive-read
probability is exactly 3/4. Hence

\[
 \Pr_A(X+\mid T)-\Pr_B(X+\mid T)
 \geq \frac{4n-27}{4(16n+9)}>0\quad(n\text{ odd},\ n\geq7).
\]

This lower bound does not require a convention for zero projections in the R
frame: it uses only strictly positive R+ projections and discards all R-
contributions. Any tie treatment that preserves the strict-sign outcomes
leaves the bound valid.

To retain failed attempts, let
C_n=sum_{x>0} 5x binom(n,(n+x)/2), p=C_n/(M 2^n), and c_m=1-(1-p)^m.
The first successful timestamp equals 1/(5n) with probability c_m/C_n,
identically for every station. Therefore the complete-record event
"success by attempt m, T=1/(5n), terminal X read positive" has probability gap

\[
 \Delta\geq \frac{c_m}{C_n}\frac{4n-27}{4(16n+9)}.
\]

At n=63, m=256, this is at least 3.703827556461e-22. The conditional bound is
25/452. The very small unconditional number is essential: this proves a
nonzero exact-clock distinction for every R frame, NOT a universal 0.044
distance or an asymptotic error floor. It does not obstruct bounded finite-
precision equivalence; nor does it apply when the exact timestamp is unavailable.

The checker verifies timestamp isolation by direct depth enumeration,
computes the full-record bound with exact fractions, and tests the conditional
bound on twelve rational-frame/size controls. The all-frame statement rests
on the variance proof, not on that finite sample.

## 3. A boundary for the fixed linear wave as a detector

The next target cannot be reduced to another source marginal. I tested the
literal proposal to store the crossing decision in a raw detector field bit.

Specify the class carefully: a fixed linear F_2 wave update, an affine
encoding of independent input bits, input-independent ready ancillas, and a
raw bit or affine functional read at a predetermined tick. Every such output
is affine in the input bits, however large the lattice or how many ticks are
used. A fixed clock phase and clean registers do not change this fact.

The smallest crossing instance already exceeds that class. Take n=1,
S_x=2a-1 and D=1+8b, with a,b in {0,1} and M=16. The crossing flag is

\[
 h(a,b)=1_{0<D\leq5S_x}=a(1-b).
\]

Its truth table in order 00,01,10,11 is (0,0,1,0). The XOR of those four
values is one, whereas any affine Boolean function has rectangle XOR zero.
Thus no affine raw-bit output can implement it exactly. Exhausting all eight
affine functions confirms that each misses at least one of the four inputs.

This is NOT a no-go theorem for an OI observer, an arbitrary coarse-graining,
or all finite reversible dynamics. A nonlinear partition of an unchanged
two-bit register, "the pair equals (1,0)", reports the same predicate. That
is a valid mathematical countercontrol to an overbroad claim. It does not
show a physical detector writing a protected result. Nonlinear input
encodings, input-dependent stopping/read selection, and nonlinear state-
dependent dynamics also lie outside the stated affine class.

Consequently the missing step has two possible forms: derive an effective
nonlinear physical interaction, or derive a physical observation map whose
nonlinear partition and accessible registers are justified. The affine
obstruction alone does not choose between them.

This distinction matches the source texts at the review13 snapshot:
[SM §4.1](https://github.com/amaybaum/incompleteness/blob/e982b346347f1fd319769c39c6c2d8772cc86ab7/papers/SM.md#41-observer-level-propagation-and-the-lattice-klein--gordon-branch)
classifies the linear nearest-neighbor branch, while SM §3 permits a broader
state-dependent second-order form. No claim is made here that all of that
broader class is affine.

## 4. Nonlinear reversible countercontrols

Reversibility itself is no obstacle to writing the predicate. For any force f,
the binary second-order update

\[
 \Phi(p,c)=(c,f(c)\oplus p),\qquad
 \Phi^{-1}(c,d)=(d\oplus f(c),c)
\]

is a bijection on the complete phase space. With three current variables
(a,b,r), choose f=(0,0,ab). A ready old detector bit zero writes ab on the
next tick. Complementing the b input produces the crossing flag above.
The checker verifies both inverse identities on all 64 phase states and the
four ready inputs. This toy does not latch a permanent record: with those
constant ready controls its detector returns to zero at tick three.

Such reversible logical constructions are standard, not an OI prediction;
see Fredkin and Toffoli,
[Conservative Logic, primary paper](https://www.cs.princeton.edu/courses/archive/fall05/frs119/papers/fredkin_toffoli82.pdf).
The question is which physical interaction the substratum selects.

A spatially symmetric example makes the source obligation visible. At each
cubic site set f to the XOR of all fifteen pair products of its six neighbor
bits. This is center-free, nearest-neighbor and cubic-invariant. With only
two nonzero neighbor inputs it writes their AND. But under independent fair
neighbor bits and old port fixed to zero,

\[
 \Pr(\text{next port}=1)
 =\frac{\binom62+\binom63+\binom66}{64}=\frac9{16},
\]

instead of 1/2. The old uniform-source lemma cannot simply be reused after
changing the dynamics. Uniform counting on the entire phase space is still
invariant; it is the readiness-conditioned distribution that changed.

## 5. A balanced nonlinear candidate, and its propagation failure

The preceding bias is not inevitable for nonlinear rules. Define opposite-
neighbor parities P_x,P_y,P_z, and let

\[
 f_M=P_xP_y\oplus P_yP_z\oplus P_zP_x.
\]

This is majority of the three pair parities. The second-order update with
f_M is again an explicit finite bijection, nearest-neighbor, center-free,
translation-invariant and cubic-invariant. It is nonlinear and therefore
outside the original fixed linear-wave branch. Choosing P_x=a,P_y=1-b,P_z=0
writes the crossing flag. These are specified rules, not a derivation that
OI chooses them.

There is a positive resource result: with uniform full phase-space counting,
one port's next TWO bits are independent fair bits conditional on its two
initial values. More generally this follows for any balanced Boolean local
force on a simple center-free graph:

1. The first output is balanced in its independent current neighbor bits.
2. Conditional on the entire current field and the old port value, each
   neighbor's next value is its known force XOR its own independent old bit.
   Thus all these next-neighbor values are independent and fair.
3. Applying the balanced force to them makes the port's second future bit
   fair even conditional on the first output. Conditioning on any positive-
   probability readiness event involving only the initial port pair also works.

This is a two-tick result under the full product prior, not the previous
arbitrary-horizon frontier lemma, a history-conditioned extension, or an
energy-shell statement. The checker exhausts all 64 input translations of
the six-neighbor truth table as a control for the balance step.

The candidate fails a different elementary control. Start with zero previous
field and a single one in the current field. Every site sees at most one
nonzero pair parity, so f_M vanishes everywhere. The next field is zero; the
following field is the original isolated bit. It repeats this two-cycle
without outward propagation. On an actual 5-by-5-by-5 torus the populations
at ticks 1..4 are (0,1,0,1); the original linear force produces six neighboring
ones on tick one.

This rules out f_M as a drop-in replacement preserving that isolated-pulse
behavior. It is not a proof that every excitation or perturbation on a random
background fails to propagate. No clock, ballistic carrier, protected memory,
or angular emission law has been obtained from it.

## 6. Research consequence and verification

The investigation has reached a dynamical compatibility question. A proposed
interaction must support the needed detector operation, retain the relevant
source law under readiness, and supply the intended carrier propagation. Each
must be checked under the SAME update and prior before importing the four
record identities as a final test. Separate existence proofs for a source,
a gate, and a clock do not compose automatically.

There is no completed native instrument in this handoff. The two nonlinear
examples expose distinct failures and one limited positive freshness theorem.
The viable next work is a specified interaction or physical observation map
that meets those obligations, followed by its full joint-record law and access
analysis. Neither nonlinear rule is adopted merely because it can compute a
crossing bit. Numerical refinement of C-SPH-1 remains closed.

`detector_boundary_checks.py` is standard-library-only, deterministic, has no
file writes or network calls, and uses explicit failure exceptions. All
finite counts, identities, and inequalities are exact; decimals summarize
exact fractions. The analytical frame and freshness arguments are written
proofs with finite controls, not kernel-certified theorems. Separate normal
and -O runs reproduce the included stdout byte for byte.
