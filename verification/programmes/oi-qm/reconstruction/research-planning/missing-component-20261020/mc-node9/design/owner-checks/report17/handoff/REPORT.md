# Prepared priors and the native readiness-flag boundary

Exploratory read-only handoff, 2026-10-23. No repository edits, commits, comments,
pushes or workflows. No new premise is adopted. The existing reports remain
unchanged. This note follows the independently reviewed report16 at 280cf250.

## Result and scope

The bounded stopping proof extends to nonuniform prepared priors under explicit
branchwise frontier-independence and record conditions. However, there is a
structural obstacle to the proposed next construction under the unchanged
three-field update: every individual raw output bit has Boolean algebraic degree
at most two in the initial raw bits, at every predetermined time. It cannot
compute the conjunction of three or more freely varying readiness tests into
one raw flag, even with input-independent prepared ancillas and arbitrarily
long evolution. On an eight-input three-bit subcube, any randomized such test
has worst-case error at least 1/8.

This is a restricted detector obstruction, not a no-go for OI, arbitrary local
reversible dynamics, every prepared ensemble, or distributed record protocols.
It explains why repeatedly running the working AND construction does not by
itself supply a composable logic network under this exact update.

## 1. Report16 reconciliation

I read the coordinator review at:
https://github.com/amaybaum/incompleteness/blob/280cf250/verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/owner-checks/report16/REVIEW.md

The accepted rule census and stopping theorem require no change. Three wording
distinctions matter for the continuation:

1. Finding 3 says 2^-117 bounds the difference between conditioning on E_w and
   W=w at K=3. The S3 table already contains the sharper correct expression.
   For w=1 the full-state TV is exactly 2^-117. For w=2 it is exactly
   2^-117 + 2^-174 - 2^-234, which is slightly larger than 2^-117.
   A simple common upper bound is 2^-117 + 2^-174.
2. That equality concerns the full conditioned microstate distributions.
   A projected record has distance at most that amount. In particular the
   payload/source/receiver record proved in report16 has distance exactly zero
   between the two conditionings, after aligning the observation windows.
3. Finding 1's wording about the census should retain the successive filters:
   quiescence, pulse response and balance leave six scalar rules; exact
   three-tick freshness then selects XOR. The P1 table already states this.

For item 1, let A={W=w} subset E_w. The TV between P(.|A) and P(.|E_w)
is 1-P(A)/P(E_w), with equality witnessed by E_w\A. Substitute the ranks
268,385,442,502. Projection can only decrease TV. None of these minor
corrections changes the accepted theorem or any saved numerical result.

## 2. Prepared-prior extension with complete record conditions

Fix a candidate successful start w. Split the initial state into reserved
frontier bits Z_w in {0,1}^(2+3K) and all remaining degrees of freedom Y_w,
including any initially present controller, clock or ancillary resources.
The partition may differ with w. Sufficient assumptions are:

1. P(Z_w=z,Y_w=y)=2^(-(2+3K)) P(Y_w=y).
2. The event W=w and the entire preparatory record H up to the start are
   functions of Y_w alone on that branch.
3. For every y compatible with that branch, the map from Z_w to the payloads
   and future source word is a bijection onto all 2^(2+3K) values. The receiver
   record is the same specified function of the payloads as before.

Then, for every positive-probability (w,h),

    P(payload=a,b, source=z | W=w,H=h) = (1/4) 8^(-K).

Proof: condition on Y_w=y. The event/record does not select Z_w, which stays
uniform. A bijection preserves that uniform distribution, independently of y.
Average over y conditioned on (w,h). The complement's distribution can be
arbitrarily nonuniform or correlated internally. The statement is branchwise;
there is no assumption that a single common set of frontier variables works
for all possible starts simultaneously.

The original readiness-flag-only interface meets the measurability and
bijection conditions by the frontier geometry in the stopping handoff. The
prepared-prior extension follows if its initial law meets condition 1 for each
branch of positive probability. Any new physical detector changes the record
and potentially the dynamics: conditions 2 and 3 must be re-established.

Merely leaving frontier bits unmodified is insufficient. A reversible copy
(Z,R)->(Z,R XOR Z) with a blank R leaves a fair Z unchanged but reveals it
completely when R is exposed. What is needed is conditional uniformity after
all preparatory records, not just uniform marginal bits before preparation.

Checks below test the finite probability mechanism with exact weighted counts
and strongly nonuniform complement laws. They are not a physical construction
of the additional controller or a new simulation of report16's 48 geometries.

## 3. Algebraic degree of the exact repaired rule

All operations are over F_2. On any fixed finite cubic torus, S is the XOR of
the six nearest neighbors. The raw rule is

    A' = SA + A_old
    B' = SB + B_old
    D' = SD + D_old + S(AB) + (SA)(SB) + (SA)B_old + (SB)A_old.

Set C=D+AB on each initial/current phase slice. Then A,B,C obey independent
linear second-order waves U'=SU+U_old. Denote their linear propagators from
the two initial slices by L_t and M_t. At any time t>=0,

    A_t = L_t A_0 + M_t A_-1,
    B_t = L_t B_0 + M_t B_-1,
    C_t = L_t(D_0+A_0 B_0) + M_t(D_-1+A_-1 B_-1),
    D_t = C_t + A_t B_t.

Every A/B output coordinate is linear in the initial raw bits, and every D
coordinate has degree at most two. This is exact for every t and finite torus,
including after wrap-around. S can be any fixed linear neighbor operator for
this degree conclusion; the spatial geometry is not the obstruction.

Fixing any prepared raw bits to constants cannot raise algebraic degree.
Nor can affine copying/encoding of free input bits into the initial raw state,
or an affine readout of the final raw bits. For input-independent randomized
resources, condition on the resource seed; each deterministic output function
still has degree at most two. A predetermined deadline may depend on that
independent seed, but not be chosen by an additional nonlinear decoder of the
input-dependent trajectory.

## 4. Raw readiness-flag no-go

Suppose J>=3 raw snapshot bits x_1,...,x_J can vary independently, all other
raw initial bits are fixed independently of them, and readiness is

    E(x)=1 iff x_1=...=x_J=0.

Its unique Boolean algebraic normal form is product_i (1+x_i), of degree J.
No degree-at-most-two raw output can equal E on this full input domain.

For the original E_K, one can already restrict to three tested initial bits:
current A at (-1,0,0), current B at (1,0,0), and current D at the receiver,
with K=3. Fix every other tested readiness bit to zero, and hold all remaining
bits independent of these inputs. E_K on that subcube is exactly three-bit
zero detection. The third Boolean difference of E_K is one; that of every
raw output at every fixed time is zero. This three-bit restriction proves the
obstruction without treating J_K=268 as an optimal readiness cost.

Thus the unchanged rule cannot write an exact, universally valid single raw
flag for that snapshot into a clean register at a specified later tick.
More clean bits, more lattice sites and a longer runtime do not defeat this
particular degree bound. They may be useful for other specifications.

This does not contradict native two-input AND: its degree is two. It also
does not contradict the 16-predicate construction on two inputs. What fails
is the inference that composing native-looking AND episodes under this same
global conjugate-linear update supplies arbitrary higher-degree computation.
Any such composition must introduce an additional intervention, nonlinear
encoding/readout, restricted input promise, or a changed update.

## 5. Random resources and the 1/8 lower bound

On the above three-bit subcube, an exact readiness truth table has odd parity
over its eight input assignments. Every degree-at-most-two truth table has
even parity, so it makes at least one error. Condition on any input-independent
resource seed and apply this argument. Averaging over the eight inputs and
then over seeds gives average error at least 1/8. Consequently some input has
error probability at least 1/8.

This is a worst-case-input guarantee. It is not a lower bound on error under
a highly concentrated prepared input law, and it does not address a protocol
that aborts or uses an input-dependent stopping decoder. A seed correlated
with the input falls outside the premise and must have its preparation counted.

The 1/8 bound is sharp in the abstract class of all randomized quadratic
functions: flip each of the eight readiness truth-table entries in turn.
Every resulting table is quadratic, and the uniform mixture errs with
probability 1/8 at each input. This is not a claim that all eight functions
are physically implementable by one choice of this wave apparatus.

## 6. Checks and scope of the next target

flag_checks.py is standard-library only and stdout-only. It checks:

* all 128 three-variable quadratic truth tables: their Hamming distances from
  readiness are {1:8,3:56,5:56,7:8};
* readiness degree J for J=1,...,12 and the abstract randomized tightness;
* the direct raw rule on the actual 25^3 torus, across all eight three-bit
  input assignments and three fixed backgrounds, through tick 4: 45
  whole-field third differences vanish;
* a positive control where the raw receiver D computes two-input AND at tick 1;
* exact weighted-count prepared-prior tests for K=1,2,3 and the copying leak;
* the strict correction to the w=2 total-variation ceiling.

The all-time theorem follows from the displayed conjugacy, not the finite
time tests. No native clock or general detector is constructed here. In
particular this is not a proof that the wave rule cannot carry a clock signal.

The next choice is substantive: retain this rule and specify a distributed
record/limited-domain detector with a justified decoding interface, or search
for a different native reversible update that supports composable computation
while preserving the required source law. The former must account for who
performs the conjunction; the latter needs a new freshness proof. Neither
choice derives the angular emission law, which remains a separate obligation.
