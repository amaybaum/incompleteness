# Coordinated affine apparatus sources: a fixed-class carrier-preservation test

Research input: accepted apparatus baseline
`529bc5bebe099a3ec5f60b08bd525714731f4c65`. Independent review of this new
unit is pending. Retain the full-ball preparation, original source locations,
native dynamics, access menu and complement/bank priors. No parity-only
preparation, extra source, late write or nonlinear initial payload is adopted.

The bounded question is whether two original-time programmes from the
**retained fixed512 controller family**, with affine E/N source compensation,
can preserve the existing incoming42-bit carrier preparation context by
context. This is one specified family, not all coordinated native apparatus.
The source-program choices are candidate apparatus preparations; a physical
procedure selecting them is not inferred from assigning their coefficients.

**Result:** only the original programme survives this fixed-class test.
The other old-phase-compatible controller changes the whole triple encoded
in the incoming packet. Restoring it would require a nonaffine N payload.
This excludes a second matched-input programme in this class, not every
coordinated encoding, a seed-averaged operational preparation, or OI generally.

## Fixed programme family and necessary incoming-carrier condition

Use the existing original current source sites

    J=(0,S,S+154), Kplus=(1,S,S+153), Kminus=(-1,S,S+153),
    E=(0,-78,78), N=(0,S,S+156).

Let delta=a XOR b. The earlier fixed512 controller family has constant
triple coefficients C,Vplus,Vminus, with payloads

    J=(u XOR a,a,u XOR a) XOR delta*C,
    Kplus=delta*Vplus, Kminus=delta*Vminus.

Each programme is initially affine in its known seeds. The complete retained
old-q9 table has exactly two coefficient arrangements preserving all64 raw
old-q9 rows: (4,5,7) and (4,7,5), using code4A+2B+D. Their terminal rows
are included. E/N cannot affect that earlier q9 record, by the retained
first-arrival geometry. Other sources, ready pins, banks and residual fields
are fixed. In particular the K sites are existing source exceptions; no
cell in the full prepared ball is newly freed.

Programme0 is the current v14 law, with (C,Vplus,Vminus)=(4,5,7) and

    E0=(1,1 XOR mY,1), N0=(mY,1,1 XOR mY).

Programme1 first swaps the two existing K payloads, keeping J and all other
resources fixed. Its proposed rescue permits arbitrary affine E(k),N(k)
in the existing known seeds k=(u,mY,mR,a,b). Neither may depend on unknown x.
This enlarges the *tested compensation family* beyond the current v14
coefficients, without adopting a different source law or new resource.
There is no nonlinear original-time source controller hidden in the test.

Let Q=U_(L+1)(q10), q10=(0,S,78). For the incoming packet K_(L+3),
the unchanged native rule gives the fixed whole-triple coordinate

    Q = U_(L+3)(q10) XOR h(XOR_(w~q10) U_(L+2)(w)).

It uses only fields inside the42-bit packet and the same function for both
programmes. It is a mathematical coordinate, not an observer read or decoder
permission. Therefore the same incoming packet law at each fixed source
context must have the same Q law. This is a necessary condition, not a
sufficient packet-preparation or reuse certificate. At the prepared source
contexts Q is deterministic under the retained actual-scale reduction.
Different Q values imply disjoint conditional packet supports there,
irrespective of the complement distribution.

## The source swap changes the incoming preparation

With E0,N0 unchanged, the swap changes Q on16 of64 microscopic rows:
eight continuing and eight terminal rows. These are context counts, not
failure probabilities. The whole old q9 record is equal in both programmes
on all64 rows. Thus old-record equality does not establish incoming-packet
equality.

For example, (x,u,mY,mR,a,b)=(0,0,0,1,1,0) is continuing. Both old q9
records are010, but Q changes from110 to101. Its A sign is unchanged in
this example; the B/D difference already changes the full packet support.
Discarding those residual fields would conceal the failed input condition.

## A four-context obstruction to every affine E/N rescue

For each of24 continuing known-seed contexts k, exhaust all64 E/N payload
pairs. Require **the whole original Q triple for both possible x**, with
one E/N choice independent of x. Exactly two pairs survive per context.
The following four contexts suffice; targets are ordered by s=x XOR u XOR a:

| k=(u,mY,mR,a,b) | Target Q for s=0,1 | All allowed (Ecode,Ncode) | Forced N.B |
| --- | --- | --- | --- |
| (0,0,0,0,0) | (3,7) | (5,2), (7,3) | 1 |
| (0,0,0,1,0) | (0,5) | (5,6), (7,3) | 1 |
| (0,0,1,0,0) | (3,7) | (5,2), (7,3) | 1 |
| (0,0,1,1,0) | (2,6) | (5,5), (7,4) | 0 |

The affine feature vectors (1,u,mY,mR,a,b) XOR to zero across these four
contexts. Consequently any affine N.B must XOR to zero as well. The forced
values XOR to1, a contradiction. On this subcube N.B would have to equal
1 XOR mR*a. Even allowing **arbitrary** E choices at each context does not
remove the forced N.B values. An affine N compensation is impossible.
All24 contexts separately admit compensation, so the obstruction concerns
the permitted functional form, not absence of a native response at a row.
Inserting the required nonlinear payload at time0 would change the
preparation resource; no such insertion is made.

For completeness, apply the same whole-Q test with the original (4,5,7)
controller. Each context again has two native E/N choices. Encode six
affine output fields by36 coefficients and each context's binary choice
by one additional bit. The144 GF(2) equations have60 unknowns and rank60.
Their unique solution is the current law: field coefficient masks
(E.A,E.B,E.D,N.A,N.B,N.D)=(1,5,1,4,1,5), with feature order
(1,u,mY,mR,a,b). The actual solution is replayed against every equation.
The corresponding swapped-controller system is inconsistent, independently
agreeing with the four-context contradiction. Since only the two earlier
controllers preserve the specified old phase, no second programme in this
fixed512-plus-affine-E/N class preserves both that phase and the whole Q.
This is an exact finite computational result with a short algebraic
obstruction, not a classification of every initial affine source layout.

## Records, failures, outgoing state and evidence limits

The probe retains the entire old q9 triple and all64 source rows, including
the16 terminal microscopic rows. It uses terminal Q fields only as private
diagnostics, never as attempted reads or offered carriers. Existing terminal
no-read/no-offer conventions, recorded prefixes, flags and timing remain.
There is no new herald, acceptance probability or failure distribution.

The imported native evaluator includes old-local terms, all six neighbors
and the original coupled lower/upper sources. Its only experimental change
is swapping the two K payloads; no cold background, reset or private write
is inserted. Native source correlations and residual fields remain physical
state. A complete controlled record/outgoing-environment kernel is not
supplied: this candidate already fails the necessary matched-input condition.
The accepted passive kernel is unchanged. No reuse, available setting pair,
quantum measurement or equality of full surrounding environments follows.

From this directory run:

    python3 -I -B native_coordinated_apparatus_probe.py
    python3 -I -B -O native_coordinated_apparatus_probe.py

The probe pins and imports the credited native_route_v13 engine; it is an
author calculation using that retained evaluator, not an independent native
implementation. It reproduces all4096 original q10 rows, checks the old q9
record for8192 native programme/E/N rows and validates1536 swapped upper-strip
scalar lanes against direct native recursion at bounded coordinates. Existing
upper/lower period proofs justify the actual astronomical parameter reduction;
payload swapping changes neither strip budget nor period. Eight independent
finite periodic native worlds check the whole-Q packet inverse. Exhaustive
1536 E/N pair tests, both binary-domain linear systems and the four-context
identity decide the new conclusion. These controls are exact; they are not
an astronomical replay, new Lean certificate or independent acceptance.
Two planted linear-system controls also check a known affine family with
six free coefficients and reject a single nonaffine corner. Normal/optimized
output must agree, with verdict `UNIQUE_PROGRAM_IN_FIXED_AFFINE_CLASS`.
Five focused mutation classes reject with VOID/exit2 in both modes: omitted
terminal old records, erased B/D carrier fields, a single unknown-input
branch, removal of the affine constant and an inverted obstruction test.

Sources: branch_v10/local-controller report/table and programme formula;
native_route_v13 evaluator, source/first-arrival geometry and period proof;
native_decode_v14 current E/N law; accepted encoded-packet and stochastic-
kernel definitions. The existing full-ball and source-inventory hypotheses
remain in force. The two already accepted apparatus checkpoints are unchanged.

The remaining construction needs a different coordinated native programme
outside this fixed coefficient family, with a sourced control procedure and
the same complete incoming-packet constraint. A nonlinear native computation
could be investigated; preloading its answer at an original source is not
that computation. No new preparation, parity relaxation, scientific claim
upgrade, manuscript edit, F/E, special dispatch, readiness or merge is adopted.
