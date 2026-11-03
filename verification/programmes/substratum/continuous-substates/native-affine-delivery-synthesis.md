# Known-seed affine delivery: an empty-domain obstruction

Research input: independently accepted, CI-green `94ad6e50`. This new
construction is author-verified and awaits independent scientific review.
It changes no manuscript, theorem grade, source inventory or native rule.

**Result:** neither arbitrary known-seed affine K offsets nor their extension
by an affine payload at the existing E source can satisfy the prescribed
complete local computation and contextwise old-q9/Q gates. A single continuing
known-seed context has no admissible source value, even before affine
coefficient relations are imposed. This is an exact finite constraint
obstruction for the specified family, not a general native-control no-go.

## Fixed family and decision rule

Retain the full-ball pins, both original slices, source positions, known-seed
restrictions, complement/bank priors, and the original reference preparation.
Let k=(u,mY,mR,a,b), with unknown x excluded from every apparatus source law.
Write codes as 4A+2B+D and delta=a XOR b. The candidate has

    N=(0,0,u XOR a XOR mR),
    J=(u XOR b,a,u XOR a), G=(u,1 XOR u,1),
    Kplus=(delta,delta,delta) XOR p(k),
    Kminus=(delta,0,delta) XOR r(k).

Each of the six offset bits is an arbitrary affine function of the five
known seeds: 36 coefficient bits with feature order (1,u,mY,mR,a,b).
Stage K keeps E=E0=(1,1 XOR mY,1). The bounded coordinated extension permits
all three E bits to be affine in the same seeds, for 54 coefficient bits
in total. E is the existing on-plane source (0,-78,78); N/J/G and all other
source laws stay fixed. No new source, nonlinear preload, private write,
reset, cold apparatus or preparation resource is introduced or adopted.
These are proposed initial laws, not a demonstrated physical setting switch.

For every one of 32 known contexts enumerate all 64 p/r values, requiring
the actual complete native two-tick J output

    (1 XOR a XOR b XOR mR, 1 XOR a*mR,
     mR XOR u XOR u*a XOR u*a*mR).

Then require the complete reference old-q9 triple and Q for both x values,
using the **same** p/r/E values. Keep all original contexts; the eight
terminal known contexts (16 microscopic x branches) remain private raw
diagnostics, never attempted post-terminal reads or offered carriers.

The constant-offset classification from the preceding unit is not imposed
pointwise: offsets may now vary with k. The scalar native recursion gives
40 locally preserving pairs at each k, including choices excluded by the
earlier uniform classification. Its B-difference identity independently
checks these full-triple equality decisions; A/D fields are retained.

The decision rule is exact Boolean constraint elimination. At each k the
native gates define a finite domain D(k) of admissible source values. Any
global affine coefficient assignment must evaluate to an element of D(k).
If some D(k) is empty, the conjunction of constraints is UNSAT. Otherwise
cross-context coefficient solving is still required; nonempty domains do
not certify an affine programme, full incoming carrier or measurement.
No floating point, heuristic optimizer or external SAT package is used.

## Explicit continuing-context certificate

At k=(0,0,0,0,0), the two reference targets, ordered by x=0,1, are

    whole old-q9 = (000,011), Q = (011,111).

There are 40 complete-local-J-preserving p/r pairs. Exactly 12 also preserve
both whole old-q9 targets. Exhausting all eight E values for each gives:

| All remaining (p,r) pairs | E required for x=0 | E required for x=1 | Common E |
| --- | --- | --- | --- |
| (t,t), t=0,...,7 | 6 | 3 | none |
| (1,5), (5,1) | 0 | 3 | none |
| (3,5), (5,3) | 7 | 6 | none |

Every row exhausts the complete native Q triple, not just its sign. The
first-arrival E action is a permutation on all eight triples, so these
individual requirements are unique. None is a common control for both x
values. Thus the 96 possible p/r/E combinations (192 microscopic worlds)
at this context contain no permissible value. Even arbitrary nonlinear
functions of the **known** seeds cannot remedy an empty domain at one fixed
k. In particular neither affine source family can work. This stronger
functional-form conclusion retains the same fixed N/J/G, source geometry,
local-computation and contextwise input requirements.

Allowing E to depend on private unknown x removes this pointwise obstruction:
each branch individually has an E compensation. That is a deliberately
unauthorized countercontrol, not a solution or newly granted preparation.
It explains why separately fitting the two unknown inputs would be invalid.

The full enumeration confirms 27/32 empty known-context domains for K-only
(20/24 continuing), and 22/32 for K plus E (17/24 continuing). The one
continuing certificate above already suffices. These are context counts,
not probabilities or physical failure rates. The contradiction does not
depend on imposing a terminal Q constraint.

## Native calculation and meaningful controls

From this directory run:

    python3 -I -B native_affine_delivery_synthesis.py
    python3 -I -B -O native_affine_delivery_synthesis.py

The probe pins and credits the accepted asymmetric helper, original native
engine and retained q9/Q tables. It imports the native engine with one
independent bit lane per explicit source world. The extension makes the
existing original E payload explicit in lower-row expansion; the rule,
positions, old-local term, six neighbors, strip budget and period reduction
are unchanged. All 512 original-K/N0/E response worlds reproduce the
retained Q table exactly. Whole old-q9 is separately checked by readdressing
the retained general controller table to identical physical J/K payloads;
the original E arrival cannot change that earlier record.

There are 2048 pointwise local cases and 4160 candidate native worlds after
local-J/old-record elimination, all eight E choices and both unknown inputs
included. Across baseline and candidates there are 37376 scalar-lane
upper-strip/direct-recursion comparisons. There are 520 complete eight-value
E-permutation controls. Removing the same-E restriction in a diagnostic
relaxation makes every pointwise context nonempty; this does not solve any
affine coefficient or operational problem. Verdicts are generated from
measured finite domains only after these controls pass.

Actual-scale evaluation relies on the inherited written upper/lower period
proofs. This is an author exact calculation using the credited reducer,
not an independent all-row implementation or a new Lean theorem. Normal
and optimized execution must return identical structured results.

Both modes agree. Seven focused mutation classes reject with VOID/exit 2
in both modes: omitted unknown input, omitted terminal contexts, imposing
the uniform constant classification pointwise, choosing different E values
for the two inputs, erased Q fields, altered reference N, and a bad helper
pin. The E-choice mutant is rejected by replaying the same proposed value
against both actual native outputs, rather than accepting a union of matches.

## Carrier and physical limits

Q remains the fixed mathematical coordinate of the incoming 42-bit packet:

    Q=U_(L+1)(q10)=U_(L+3)(q10)
                       XOR h(XOR_(w~q10) U_(L+2)(w)).

Unequal deterministic Q at a fixed source context precludes identical
conditional packet supports. Q equality would only be necessary: a survivor
would still require complete packet distributions and relevant correlations,
earlier raw records/flags/timing, the outgoing environment, permitted access,
physical selection and reuse checks. None is inferred from domain solving.
The input gate fails here; no controlled measurement output, new failure
law, instrument/environment kernel, interference or reusable stage is tested.
Residual B/D fields and native environmental correlations are not discarded.

This unit exhausts K offsets with fixed N/J/G and the specified existing-E
extension. It does not exhaust coordinated changes to J/G/N or other source
geometry, a differently justified coarse preparation, or native OI dynamics.
Further coordination needs a separate bounded construction and full input
proof. Accepted checkpoints remain in history; the PR stays research-only,
draft and unmerged. No manuscript/main change, claim promotion, special
dispatch, F/E designation or readiness action follows.
