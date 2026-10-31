# Asymmetric native delivery: escape of one obstruction, failure of the full input

Research input: independently accepted and CI-green
`6aa0ed0361124285dc8337f5c0602df26bf2301e`. This new unit is unreviewed.
The reference incoming carrier remains the original v14 programme with
E0,N0 and K coefficients (5,7). The accepted local-computation candidate
was not substituted as the reference preparation.

**Result:** two asymmetric programmes preserve the complete local nonlinear
computation and fix the balanced interface's common counterexample.
They nevertheless change Q on 40 and 43 of 48 continuing source contexts.
The complete matched-input gate therefore fails for both. Breaking the
previous cancellation is useful, but is not sufficient for valid delivery.
No measurement-output, herald or reuse stage is attempted.

## One focused asymmetric family

Keep the same native rule, full-ball pins, source sites and seed/complement/
bank priors. Use the previous candidate's affine source N=(0,0,u XOR a XOR mR),
the unchanged E0=(1,1 XOR mY,1), J=(u XOR b,a,u XOR a), G=(u,1 XOR u,1).
At the two existing K sites propose independent constant offsets p and r:

    Kplus=(delta,delta,delta) XOR p,
    Kminus=(delta,0,delta) XOR r,  delta=a XOR b,
    p,r in {0,...,7},  code=4A+2B+D.

Each programme is affine in the known initial seeds. There is no nonlinear
initial preload, new source position, late write/reset or unprepared cold
apparatus. These remain explicit candidate initial source laws. Affinity
does not establish a physical procedure for selecting or preparing them;
no new preparation dependency is adopted as an available resource.

First require preservation of the complete computed J output for every
u,a,b,m=mR:

    U2(J)=(1 XOR a XOR b XOR m, 1 XOR a*m,
           m XOR u XOR u*a XOR u*a*m).

The same five prepared local sources and previous-zero cone used at 4632c3c7
determine this calculation. Offsets alter values only at the existing K
exceptions; all full-ball pins and exterior inputs remain as before.

## Exact classification preserving the local computation

The complete two-tick native cone gives the following change of J.B:

    Delta B=(1 XOR u)*(p.D XOR r.D) XOR delta*r.D
             XOR (1 XOR delta)*(p.B XOR r.B)
             XOR p.B*r.D XOR r.B*p.D.

The A offsets cancel in this expression. For Delta B to vanish for every
u and delta, its coefficients require

    p.D=r.D=d,  p.B XOR r.B=d.

The constant term then vanishes too. The neighbor-XOR A/B components are
unchanged, so these conditions preserve **all three** J output fields,
including the cubic D residual, not merely the product bit. The A offsets
are free. Exactly 16 of 64 offset pairs qualify; 12 are unequal and 4 are the
already balanced constant-shift cases. Exhaustive native local recursion
over all 64 pairs and 16 local contexts agrees with this algebraic criterion.

## Early screen: the previous witness is genuinely overcome

Evaluate the 16 qualifying programmes first at the previous common context
(x,u,mY,mR,a,b)=(0,0,0,0,0,0). The reference has whole old-q9=000 and Q=011.
Only two offset pairs reproduce both there:

| (p,r) codes | Physical offsets | Old q9 | Q |
| --- | --- | --- | --- |
| (3,5) | (011,101) | 000 | 011 |
| (5,3) | (101,011) | 000 | 011 |

The zero-shift nonlinear candidate instead has Q=110. Unequal K values
break the reflection symmetry used by the balanced obstruction; the native
response changes on the central plane. These source-dependent native
responses are not conditioning on a random label. Both programmes still
have the original computed J triple in every local source context.

This early agreement is only a necessary screen. It is not acceptance of
the full incoming 42-bit preparation or its relevant correlations. The 14
other local-computation-preserving pairs are rejected at this context;
only these two proceed to the full source-context comparison.

## Complete source-context gate: both survivors fail

The unchanged native evaluator evolves the two surviving programmes for
all 64 original source rows. The 48 continuing/16 terminal labels are those
of the reference protocol; the candidate may not redefine them to discard
unmatched rows. The results are:

| Offsets | Q changes, continuing / all | Whole-q9 changes, continuing / all |
| --- | --- | --- |
| (3,5) | 40/48; 56/64 | 44/48; 60/64 |
| (5,3) | 43/48; 56/64 | 36/48; 52/64 |

For the continuing context (x,u,mY,mR,a,b)=(0,0,0,0,1,0), reference Q=101,
whereas the two candidates give 111 and 010 respectively. The fixed incoming
packet coordinate remains

    Q=U_(L+1)(q10)=U_(L+3)(q10)
                     XOR h(XOR_(w~q10) U_(L+2)(w)).

Thus each deterministic Q mismatch already proves different conditional
full-packet supports. This rejects the complete incoming-carrier gate;
it does not accept a carrier merely because a visible record or one bit
matches. Equality of Q alone would not establish the complete packet law.
The comparison is contextwise; a differently justified coarse or averaged
preparation is outside this test. The counts are microscopic contexts,
not failure probabilities or a newly derived heralding distribution.

## Native controls and evidence boundaries

From this directory:

    python3 -I -B native_asymmetric_delivery_probe.py
    python3 -I -B -O native_asymmetric_delivery_probe.py

The probe pins the retained native_route_v13 source and response tables.
It reads the original affine payload formulas as data. Separate scalar
local recursion supplies 1024 source/offset cases and verifies the general
Delta B formula and 16-pair classification with every residual field kept.

For the actual-scale response it imports the credited native evaluator,
packing one independent bit lane per explicit source programme/context.
The native rule, source positions, lower front and period reduction are
unchanged. The reference 64 rows reproduce retained q10 data; the early
reference and zero-shift rows reproduce the known Q=011/110 controls.
Whole-q9 fields are separately checked by readdressing the general
controller table to identical physical J/K payloads, with auxiliary delta=1.
No E/N change reaches old q9 by its time L. Across reference, early screen
and survivors, 209 native source rows have 1672 upper-strip/direct-recursion
scalar-lane controls. The inherited period proof, rather than finite short
replay alone, supports the astronomical time reduction.

All64 rows for each survivor retain their full raw Q and old-q9 fields,
including terminal diagnostics. They are not attempted post-terminal reads
or offered carriers. Original record/flag/timing conventions remain, and
actual altered raw fields are not hidden in new labels or a success filter.
No new failure law, observer access, reset or physical setting-selection
procedure is supplied. The environment remains the native pushforward of
the original state, with its correlations retained. No controlled output/
environment kernel or reusable stage is claimed after the input gate fails.

Normal and optimized execution return identical complete results. Eight
mutation classes reject with VOID/exit 2 in both modes: wrong local
classification, nonlinear initial preload, erased asymmetric offset, changed
reference N, omitted terminal contexts, omitted unknown-input branch,
acceptance after the early screen alone, and erased Q fields.

These are author exact controls, a local algebraic classification and an
audited native reduction, not independent acceptance or a new Lean proof.
The original source-inventory and full-ball preparation hypotheses remain
in force. The asymmetric constants get past the identified symmetric
counterexample, but this entire constant-offset class still fails the full
programme requirement. Further source coordination needs its own native
construction and complete input proof. No manuscript/physics claim upgrade,
special dispatch, F/E designation, readiness change or merge follows.
