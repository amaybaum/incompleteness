# Separate deduction: ninth-tick history and fresh-bit refinement

This deduction is authored during the separate review. It is additional to,
and not attributed to, the author checkpoint
`328b74b88eaeddc798bf4693af78a571bf429787`. The review verdict on that checkpoint
covers its pointwise masked route. This note applies the chronological proof
to its explicit new source and readiness.

Use the seven-port bank and fixed access convention in
`../../history_v9/REPORT.md`, with its last time changed from R+8 to L=R+9.
Keep the same initial-coordinate formula for each port and every tick after
its informative deadline. The bank now contains 2P+6d+63 triples, requiring
6P+18d+189 bits; 189 are after R and 21 are additional to the eighth-tick
history audit. These remain stipulated initial independent fair resources.

The current q9 ready ball has radius L; its previous ball has radius L-1.
The exact bank-to-q9 distance slack formulas are unchanged from the eighth
tick when q8,L8 are replaced by q9,L9: they are t-a_i for ports 0,2,3,5,
t+8T for port 1, t+2T-P for port 4, and 12R-t for port 6. Each is positive.
All inherited ready constraints are preserved and the new ball contains the
previous outward balls. The new source J=(0,S,S+154) is disjoint from every
bank family and belongs to the explicitly exempt current boundary. Thus the
added initial pins preserve the bank's freedom. No initial block is supplied
at a later time.

The same directed equal-time edges, 2 to 5 and 3 to 5, remain acyclic; all
other cross-arrivals are later. Unique axial first-arrival paths and the
permutation H give the same triangular bank-to-noise bijection for every
fixed complement C, including the new a-dependent J background. With N9 the
whole old noise word through L,

    Pr(N9=n | C) = 2^(-(6P+18d+189)).

Let D be the informative older record, including both heralds and any older
allowed Y outcome y. Assume a is independent fair at the original preparation,
independent of old variables and old frontier blocks, and that readiness
preserves that independent degree of freedom. The two values of a produce
distinct J payloads for every fixed u. J cannot reach any older informative
port by its deadline, q7 by R+7, or q8 by R+8. Therefore D,y do not depend on a.
The noise-word bijection implies a stays fair conditional on D,y,N9 even
though the old used seed u need not do so.

The reviewed pointwise route gives q9=(0,t,t), t=y XOR a. Consequently, for
either t in {0,1} and each nonzero-probability informative branch,

    Pr(N9=n, q9=(0,t,t) | D,y)
      = 2^(-(6P+18d+189)-1).

The conclusion holds on every prior herald/failure branch for which the
native-family pointwise input assumptions hold; it creates no offered carrier
on a previously terminal failure. It concerns the old seven full port
streams and this one terminal q9 read. The q9 prefix remains private under
the inherited access convention. No simultaneous outgoing y register, full
two-slice state independence, 5:3:2 sampling, new herald, or complete reset is
proved. Initial independence of a is an assumption whose physical sourcing
remains open, not an inference from its affine encoding.

`history_corollary.py` checks actual-parameter piecewise-affine distances,
source/deadline separation, the equal-time graph and the finite conditional
masked-sign law. Its normal and optimized outputs equal
`history-corollary-result.json`. The unbounded-size history statement rests
on the displayed chronological proof, not on finite enumeration.
