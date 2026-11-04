# Balanced native delivery: a reflection-plane obstruction

Research input: accepted `4632c3c7d7c4e79ec16219fae35578468bf9d299`.
Independent review of this unit is pending. The reference carrier is still
the original v14 programme (C,Vplus,Vminus)=(4,5,7), E0,N0. The failed
nonlinear-computation candidate at4632c3c7 was not adopted as that reference.
Keep the full-ball pins, source positions, native rule, and known-seed and
complement/bank priors.

This unit tests a specific balanced source interface: preserve the native
local nonlinear computation while changing its later propagation through
the two existing K sources. Its **first gate** is the same complete incoming
42-bit packet preparation, context by context. A mismatch of the packet's
fixed whole-Q coordinate rejects this gate; agreement on that coordinate
alone would not accept the gate or its correlations.

**Result:** none of the16 proposed balanced programmes passes. The native
local product is retained, but a common continuing context has Q=110 for
every programme, versus reference Q=011. A reflection-plane argument
explains why equal paired K changes cannot correct this context. This
rejects this interface, not all native delivery mechanisms or OI generally.
No new measurement output, failure law or reusable stage is tested.

## Concrete source programmes and the local-computation invariant

Retain the candidate's existing source geometry and payloads

    J=(u XOR b,a,u XOR a), G=(u,1 XOR u,1),
    N=(0,0,u XOR a XOR mR), E=E0=(1,1 XOR mY,1).

Write delta=a XOR b. At the existing Kplus/Kminus sites prepare

    Kplus=(delta,delta,delta) XOR t(mR),
    Kminus=(delta,0,delta) XOR t(mR),
    t(mR)=W XOR mR*V,
    W,V in {000,010,100,110}.

These are16 fixed coefficient programmes. Every field is affine in known
seeds; no unknown x copy or nonlinear correction is inserted. They extend
the earlier constant-controller family by explicit constant and mR terms
at the same K sites. The proposed laws are candidate original-time source
preparations, not private writes at a later slice. Affinity does not by
itself derive a physical procedure selecting or preparing those laws.
Even granting these source laws, the carrier gate fails; no new preparation
resource or source dependency is adopted into the accepted model.

For h(A,B,D)=(B,D,A XOR BD), let kplus XOR kminus=(0,delta,0). Direct algebra
gives, for any dirty c and complete common shift t,

    h(c XOR kplus XOR t) XOR h(c XOR kminus XOR t)
      XOR h(c XOR kplus) XOR h(c XOR kminus)
        = (0,0,delta*t.D).

The two K shifts also cancel inside the other first-step neighbor sum.
Thus t.D=0 preserves the complete two-tick J output proved at4632c3c7:

    U2(J)=(1 XOR a XOR b XOR mR,
           1 XOR a*mR,
           mR XOR u XOR u*a XOR u*a*mR).

This is why the four zero-D triples are the chosen basis, rather than an
arbitrary source search. Both initial sources and all residual output
fields remain explicit. Native evolution of these fields, with every
old-local term and neighbor retained, supplies the tested interface.

## Matched-input test before measurement outputs

For q=q10 and incoming K_(L+3), the fixed identity remains

    Q=U_(L+1)(q)=U_(L+3)(q) XOR h(XOR_(w~q) U_(L+2)(w)).

Different deterministic Q values at the same source context therefore give
different conditional full-packet supports. The actual-scale native
calculation covers all64 source rows for every programme. The counts of
changed Q among the48 continuing rows are:

| W code / V code | 0 | 2 | 4 | 6 |
| --- | --- | --- | --- | --- |
| 0 | 48 | 46 | 46 | 46 |
| 2 | 46 | 48 | 46 | 46 |
| 4 | 42 | 42 | 44 | 42 |
| 6 | 44 | 44 | 44 | 46 |

Codes use4A+2B+D. All16 fail the required common incoming preparation.
These are microscopic context counts, not physical failure probabilities.
Matching a few rows does not define a new herald or permit discarding the
remaining rows. Some programmes also change earlier whole-q9 records;
those changes remain in the comparison rather than being hidden in labels.

The same continuing witness works for every W,V:

    (x,u,mY,mR,a,b)=(0,0,0,0,0,0),
    old whole q9=000 in both programmes,
    reference Q=011, candidate Q=110.

This already rejects the full42-bit input gate, including any proposed
agreement of its relevant correlations. It does not merely test the public
record or recovered sign. No new downstream record/output or reuse test is
attempted after this failure. The comparison remains contextwise; a
separately justified coarser preparation is outside the tested contract.

## Why equal mirrored sources cannot fix the common witness

Let Rx reflect x to -x. The native update commutes with this reflection.
If both initial slices are reflection symmetric, each later slice is also
symmetric. At a central-plane site p=(0,y,z), the two x-neighbors then
have equal triples, so their XOR cancels **before** h is applied. The
restricted plane evolves autonomously by the same second-order rule using
its four y/z neighbors. Consequently two reflection-symmetric initial
states agreeing on both central-plane slices have identical plane
trajectories, regardless of their different symmetric off-plane data.
This argument uses the full nonlinear rule, not linear superposition.

Apply the statement locally to q10's deadline cone in the witness context.
The full current radiusL+1 and previous radiusL are prepared. Of the1479
compiled sources, only the x-invariant origin can reach q10 by its deadline.
Relevant named sources on the plane are invariant. The paired +/-T
selector values are both zero. The K sources have the same value W because
delta=mR=0. The replaced F10 pin and its reflected prepared cell are zero.
All bank rays and the asymmetric4T/remote sources are outside the cone.
Thus the required reflection symmetry follows from this prepared context,
without imposing a new global symmetry on the arbitrary exterior.

Every balanced candidate has the same central-plane initial data as the
zero-shift nonlinear candidate, including its N=000. They therefore have
the same Q=110. The reference instead has N0=011 and Q=011. Equal paired
K changes cannot compensate that difference on the central plane. This
single-context obstruction also applies to any more general **common** K
payload shift in that sector, with all other source data fixed. It does
not cover unequal K changes, different on-plane controls or other layouts.
The proof concerns a finite causal cone, not equality or reflection of
the complete asymmetric environment.

## Reproduction, controls and limits

From this directory:

    python3 -I -B native_balanced_delivery_probe.py
    python3 -I -B -O native_balanced_delivery_probe.py

The probe imports the pinned retained native_route_v13 evaluator, repacking
its independent bit lanes to64 source contexts and changing only the
explicit original-time payload data. The native rule, coupled lower front,
source positions and time-period reduction are unchanged. The re-packed
reference reproduces all64 relevant retained q10/q9 rows. The zero-shift
candidate reproduces the accepted nonlinear response by the separately
established local-reflection table identity. These controls check the
adapter before the new programme results are used.

The16 programmes supply1024 native source rows,256 complete local-J field
checks and4096 modified upper-strip/direct-recursion scalar lanes. The128
paired-shift identity cases retain all triple components. A separate dense
periodic native update verifies588 central-plane site checks across three
dirty initial pairs and four time cuts; nonzero symmetric off-plane
differences remain. Three asymmetric A-field perturbations yield native
plane D flips, so the comparator can detect an actual coupling when the
symmetry hypothesis is broken. This is a mathematical native countercontrol,
not a newly available observer write or apparatus.

All64 rows include16 terminal microscopic contexts. Their raw source fields
are diagnostics, not attempted post-terminal reads or offered carriers.
The original complete raw records, flags and timing remain; no new success
filter or failure distribution is defined. Full environmental correlations
remain in the native pushforward. This unit does not calculate a controlled
output/environment kernel, because its incoming-carrier gate fails.

The counts are author exact controls supported by the reflection-plane
proof. They are not independent acceptance, a new Lean certificate or an
astronomical-scale direct replay. Source anchors are the retained full-ball
preparation, named-source and bank declarations, local nonlinear source
calculation, native_route_v13 period/evaluator, and whole-packet inverse.
Their original source-inventory and preparation hypotheses remain in force.
No extra source site, secret full-ball relaxation, late reset/write/read,
manuscript change, physics claim upgrade, special dispatch, F/E, readiness
or merge is adopted. An asymmetric or further coordinated native interface
must establish its own source compatibility and full input preservation.

Normal/optimized probe outputs agree. Six focused mutation classes reject
with VOID/exit2 in both modes: wrong paired-shift identity, asymmetric
source shift, nonlinear initial preloading, erased J.D residual, changed
reference N payload and a missing reflected neighbor in the plane control.
