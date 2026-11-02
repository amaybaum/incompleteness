# Native nonlinear compensation: a local computation and its carrier limit

Research input: accepted `89cbceead97d124e6d351d2e5f1c6cabee4586d7`.
Independent review of this unit is pending. Keep the full-ball preparation,
source positions, native rule, record access and environment assumptions.
This is a bounded candidate within the previously permitted affine E/N
source family. Its proposed N payload differs from the accepted default;
that default and its scientific checkpoint remain unchanged.

**Result:** the actual source cluster computes the required bit
`1 XOR mR*a` in J.B after two native ticks, using affine initial payloads.
Its full A/D output is explicit. This supplies a conditional native local
computation, but the tested programme changes the whole incoming-carrier
coordinate Q in every continuing source row. Correct delivery and matched
carrier preparation are therefore unestablished. Computing the necessary
bit alone does not implement the compensation.

## Physical sources and exact two-tick computation

Use existing current source sites J=(0,S,S+154), N=(0,S,S+156),
G=(0,S,S+152), Kplus=(1,S,S+153), Kminus=(-1,S,S+153).
Write delta=a XOR b. Keep the original J and G payloads and either retained
K orientation:

    c=J=(u XOR b,a,u XOR a), g=G=(u,1 XOR u,1),
    {kplus,kminus}={(delta,0,delta),(delta,delta,delta)}.

The candidate N payload is

    n=N=(0,0,u XOR a XOR mR).

All these initial fields are affine functions of permitted known apparatus
seeds. No unknown x copy or nonlinear answer is inserted. The original E
payload remains E0=(1,1 XOR mY,1). The local computation is the same for
both K orientations; this does not itself provide distinct operations.

Let q=q10=(0,S,78), with L=S+77. Distance(J,q)=L-1, so the entire initial
current radius-two cone needed for U2(J) lies in the retained full current
ball B_(L+1)(q). Its previous radius-one cone lies in B_L(q).
The prepared previous fields there are zero. Exactly J,G,N,Kplus,Kminus
are named current-source exceptions inside the local cone; none of the1479
compiled old sources or public-bank cells lies there. All other current
fields in this cone have their existing zero pins. Exterior fields remain
in the original environment and can affect later stages.

Write h(A,B,D)=(B,D,A XOR BD). At time1 the six J neighbors have values

    h(c XOR kplus), h(c XOR kminus), h(c), h(c),
    h(c XOR n), h(c XOR g XOR kplus XOR kminus).

Their full XOR enters the unchanged rule, including the old-local term c:

    U2(J) = c XOR h(h(c XOR kplus) XOR h(c XOR kminus)
                   XOR h(c XOR n) XOR h(c XOR g XOR kplus XOR kminus)).

The two equal transverse h(c) terms cancel in that XOR. Substitution gives
the complete output, with m=mR:

    U2(J) = (1 XOR a XOR b XOR m,
             1 XOR a*m,
             m XOR u XOR u*a XOR u*a*m),
    U1(J) = (0,0,0).

This identity holds for every u,a,b,m and both K orientations. The source
program is affine, while the computed B field has the genuine degree-two
monomial a*m. The D field also contains a degree-three term. These residual
fields and the neighboring physical state are retained. The identity is
derived from the complete prepared local cone, including G and both K
sources, rather than an isolated ideal gate supplied to the observer.

## Timing and the delivery condition

The product is computed at time2 on the original N-to-q10 axial front:

    distance(N,J)=2,
    2+distance(J,q10)=L+1.

A path is therefore causally timely for the q10 cut. This equality is a
transport bound, not a certificate that the computed B bit reaches the
required operand with its other fields and correlations suitable for use.
The subsequent native evolution processes the entire source cluster and
environment. It does not insert U2(J).B as a freely assigned source N.B
at original time0, or let a private decoder clean that field.

The earlier obstruction constrains an **initial** N.B on a particular
subcube. The present computed field is at a different site and time.
Identical bit formulas do not identify their physical interfaces. A native
circuit must implement that connection and preserve the incoming carrier.

## Whole-carrier test of this concrete programme

Compare the default programme (K coefficients5,7 with E0,N0) with the
candidate (K coefficients7,5, E0 and the affine N above). All other source
data and full-ball pins stay fixed. The old whole-q9 record remains equal,
including its terminal rows. E/N cannot affect q9 by its time L, since
both are at distance L+2 from it.

For the actual q10 output Q=U_(L+1)(q10), the retained table covers every
E/N value. The swapped response can also be reconstructed by x reflection:

    Qswap(x,u,mY,mR,a,b,E,N)=Qbase(x,u,mR,mY,a,b,E,N).

This identity holds inside q10's deadline cone. The paired K sources and
paired +/-T selectors exchange; numeric E/N values are held fixed. Other
contributing named sources and the only reachable compiled source, the
origin, are x-invariant. The replaced F10 pin and its reflected prepared
cell are zero. The asymmetric4T source, remote sources and bank rays cannot
reach that cone. No reflection or equality of the complete global
environment is asserted.

Using the candidate Ecode=7-2*mY and Ncode=u XOR a XOR mR gives a different
Q from the default on **all64 source rows:48 continuing,16 terminal**.
These are exact microscopic context counts, not a failure probability.
For (x,u,mY,mR,a,b)=(0,0,0,0,0,0), default Q is011 and candidate Q is110.

The incoming42-bit packet at L+3 contains the fixed whole-triple coordinate

    Q=U_(L+3)(q10) XOR h(XOR_(w~q10) U_(L+2)(w)).

Hence these differing deterministic Q values give different conditional
incoming-packet supports at the same source context. The candidate fails
the matched-input test, even though its earlier native computation works.
The comparison is context by context; a separately justified coarser or
seed-averaged operational preparation is outside this test. Encoded
correlations or other native compensation circuits are not ruled out.

## Controls, records and remaining stages

Run from this directory:

    python3 -I -B native_nonlinear_compensation_probe.py
    python3 -I -B -O native_nonlinear_compensation_probe.py

The probe reads pinned primary source positions and affine payload formulas
as data. Its separate scalar native recursion checks all32 local source/
orientation contexts and reconstructs the complete output polynomials by
an exact Boolean Mobius transform. Every initial field has degree at most1;
J.B has monomials1 and a*m. Removing native nonlinearity changes20 worlds;
omitting the old-local term changes28. Giant-integer cone/source/bank
checks justify the local prepared inputs. The full4096-row reflection
reconstruction matches the accepted swapped-table digest, and all64
candidate Q rows, old q9 records and terminal diagnostics are retained.
These are author controls, not independent acceptance, an astronomical
native replay or a new Lean certificate.
Normal/optimized outputs agree. Six focused mutation classes reject with
VOID/exit2 in both modes: nonlinear initial preloading, omitted old-local
term, omitted G source, erased residual D field, wrong response reflection
and omitted terminal rows.

The complete raw records, flags, timing and earlier terminal convention
remain unchanged. Private terminal Q values are diagnostic fields, not
attempted reads or offered carriers. No new herald, failure law, private
write/read or reset is supplied. The exterior environment remains the full
native pushforward of the original state; no independent-bath or erased-
workspace assumption follows from computing one field. A local two-slice
center is not a closed apparatus boundary: neighboring outgoing fields can
depend on the original complement. No complete measurement/output kernel,
physical selection procedure, repeatable interaction or reuse is claimed.

This closes the local-computation subproblem for the stated candidate.
The remaining construction must deliver a nonlinear result into a concrete
native interaction while preserving the complete incoming packet and its
relevant correlations. More passive evolution or a symbolic substitution
of the computed bit cannot establish that interface. Source anchors are
native_seed_v12's full-ball preparation, native_vread_v15's named geometry,
native_route_v13's source formulas and retained response table, and the
accepted coordinated-source/whole-packet analysis. Their existing source-
inventory and preparation hypotheses remain in force. No manuscript or
physics claim upgrade, special dispatch, F/E, readiness or merge follows.
