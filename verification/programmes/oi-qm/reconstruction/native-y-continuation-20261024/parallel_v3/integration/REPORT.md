# Parent integration: tagged terminal contract and remaining junction

24 October 2026. Repository-read-only synthesis work. No new acceptance rule,
physical premise, or raw carrier encoding is adopted by this note.

## Exact candidate information contract

For a localized raw triple Q=(A,B,D), the proposed native mixer has polynomial
M_a(Q)=(A XOR a,B,D XOR aB). This is an involution on all eight triples.
On the actual code C=(y,y,1 XOR xy), its designated fresh sign is r=y XOR a,
and its complete cell is

    (r, y, 1 XOR xy XOR (y XOR r)y).

Every field is determined by public history (x,y) and that designated sign.
The cell does not reveal a further independent fresh seed at its terminal read.
Using two such mixers, a Y copy, and an independent Z gives an injective
history-indexed embedding E_(x,y)(j) of the four-sign target carrier j.

With independent fair a,b,z and uniform L in {0,...,7}, accept counts 5,3,2,0
on (a,b)=00,10,11,01. Then exactly

    P(success, raw=E_(x,y)(j) | x,y) = (5/16) mu_(Y,y)(j),
    P(failure, no carrier | x,y) = 11/16.

Each full X or R cell factors through its own sign plus public history. This
is stronger than checking only decoded X→Y→X statistics; the whole tagged
carrier and every failure are checked in tagged_contract.py.

The preceding X-reset herald has the same success5/16 and makes y fair given x.
Therefore the abstract two-reset success is25/256 conditional on the earlier x,
or125/2048 including the older independent5/8 predecessor. These are supplied-
resource composition calculations, not success rates of an integrated native
X→Y sequence. No prior failure is discarded.

## Strict common raw carrier does not yet pass

At y=1, the distributions of the entire raw output for x=0 and x=1 have disjoint
supports: total variation is1 on second success. The decoded target carriers
coincide. Public-history dependence is not a leak of new secret information,
but it is still dependence of the raw encoding on the earlier history.

Consequently this is a candidate history-indexed interface, not satisfaction
of the unchanged history-independent raw-carrier/reusable-socket criterion.
No relaxation of that criterion is adopted. The retained history must be
physically separated from the common carrier or subsequent native operations
must be shown to implement the required history-independent target law under
an explicitly accepted interface. A terminal decoding table alone cannot do so.

A simple countercontrol makes the distinction visible. The retained Y-cell tag
recovers x when y=1. A future operation that flips the R result conditional on
that tag changes its target agreement from4/5 to1/5 across histories, despite
the preceding correctly decoded reset. Thus closure under further native
operations remains a substantive obligation.

## Cross-track compatibility

The native history sidecar and third outward step use the inherited apparatus
with specified compatible outward readiness extensions. The five-tick extractor
and standalone direct-reset apparatus prove conditional native gadgets for a
localized arbitrary input at their own start time. Neither obtains that start
state from the actual populated q2 phase merely by naming it as an input.

In particular the proposed extractor's translated previous-slice ready cone
requires a zero at q2+e_x. Actual dynamics gives (0,1 XOR u XOR mY,mY) there
at R+1. A controlled dirty-neighbor example changes the extraction result.
This is a concrete failed splice, not a generic objection to all embeddings.

The positive local native gadgets and nearby x register narrow the next task:
construct one junction on the actual two-slice phase, specifying added resources
at the original initial time, preserving old fair frontiers, and proving the
complete record law through its deadline. A clean late workspace, a native
clock, a shutter, and joint independence are not inferred from terminal algebra.

## Checks

tagged_contract.py imports no construction or author code. It exhausts all
four x,y pairs, all64 second-reset resource states, and all2048 two-reset states
for each x, including failures. It checks mixer inverses, complete tagged laws,
per-cell information factoring, raw-history separation, terminal R calibration,
and a reuse countercontrol. It is an algebraic contract check, not a native
geometry or initialization proof.
