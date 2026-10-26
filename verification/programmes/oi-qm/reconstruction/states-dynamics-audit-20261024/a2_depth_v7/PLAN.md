# Depth extension of the per-slot fresh-block finite controller

24 October 2026. Research only, under guiding draft #911, beginning at
`70a8d97f54e4f00e729e9ff73fd94a81852d3dab`. #885 is read-only. No native
availability, physical premise, access rule or full-equivalence claim is adopted.

## Question

`a2_efficiency_v6/` certifies the M=16, W=16, B=24 geometric controller for a
declared menu and total horizon h=3. Its handoff leaves arbitrary depth open
and says longer horizons need recertification. Can that controller, or any
controller in its resource class, be recertified at every depth with fixed
resources? The class: after each read, the next carrier is drawn from a fresh
independent block of at most B fair bits reserved for that slot, and responses
are deterministic functions of the carrier, retained word and setting.

## Witness protocol and computations

The protocol lies inside the declared menu: prepare X+, then read a, X, a,
X, ... for h reads, with no rotations or stops. In quantum theory every read
agrees in sign with the preceding pole with probability 4/5. The tested
extension keeps the executed grid and reserves one more fresh B-bit block per
slot, as the existing allocation rule does; nothing else changes.

1. Rebuild the executed grid and CDF counts with exact integers, without
   importing the earlier checker. Compute the exact agreement probabilities
   A (reset at +-a, read X) and B (reset at +-X, read a), each sign computed
   directly rather than assumed by antipodal symmetry. Count zero responses.
2. Exact complete-record total variation T(h) on this protocol for h=1..64,
   and at powers of two up to 2048 as long as the whole run stays within
   twenty minutes of CPU. T is nondecreasing in h by data processing; locate
   the first exact crossing of 1/10 by bisection over exact evaluations when
   it lies in the executed range, otherwise report that it was not reached.
3. A certified bound for every h. With per-read discrepancies d_t, squared
   Hellinger per read is at least d_t^2/4, so T(h)>=1-prod(1-d_t^2/4)
   >=S/(1+S), S=sum d_t^2/4; maximal coupling gives T(h)<=sum d_t.
   Check that every exact T(h) lies inside this bracket.
4. Class statement. In the class, every conditional agreement probability
   after the first read is k/2^B, hence differs from 4/5 by at least
   dist(4/5,2^-B Z). Derive that distance in closed form and verify it
   exactly for B=1..64. Deduce the depth beyond which T exceeds 1/2 for
   B=24, and the necessary growth condition on slot-dependent B_t.
5. Sufficiency at sampler level: a per-slot nearest-dyadic Bernoulli sampler
   with B_t=B0+2*ceil(log2 t) has T(h)<=sum d_t, bounded for all h.

## Decision rule

- If A=B=4/5 exactly, report no obstruction from this protocol.
- Otherwise, over green controls, report that this controller extension has
  no depth-uniform complete-record bound below 1 on the declared menu, with
  the exact first depths and certified depths computed above.
- The class verdict is printed only if the closed-form distance is verified
  and positive for every tested B. All verdict text is generated from the
  measured values.

## Controls

- Positive control: a source with exact agreement law 4/5 gives T(h)=0 and
  a zero lower bound; a brute-force enumeration of all 2^h records of the
  actual seeded controller agrees with the closed-form count formula for h<=12.
- Countercontrol: a pooled-bank sampler that decodes one N-bit integer by
  exact adaptive arithmetic coding of the quantum conditional law (N=24h).
  Its conditional laws are not confined to 2^-24 Z, and its exact T(h) for
  h<=12 must lie below 2^(h-1-N). This shows the per-slot freshness hypothesis
  is load-bearing. That sampler stores the conditional probability and is not
  a geometric controller.
- Sign control: antipodal pairs are computed and compared, not assumed.
- Consistency: per-read discrepancies are at most the retained kappa, and
  T(3) is at most the retained certified bound 3*kappa+2*chi.

## Scope fixed in advance

A negative result covers this controller's natural slot extension and the
per-slot fresh-block class on this protocol only. It is not a bound on
total randomness, on pooled or continuous resources, on per-read error, or
on OI. The h=3 certificate is not affected. The literature fact that
infinite products of nonidentical Bernoulli laws separate (Kakutani 1948) is
credited; no novelty is claimed for it. Deliverables follow the branch
convention: PLAN.md, REPORT.md, checks.py, result.json, PROVENANCE.json,
SHA256SUMS, with byte-identical normal and -O replay. No Git push,
dispatch, F/E designation, merge or #885 write is included.
