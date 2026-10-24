# Fixed readouts of the q10 cell under jointly affine known-seed sources

Research checkpoint, 24 October 2026. Plan committed on #910 at
`36213be6354ef15442b4f3040ecdb511fd0b5641`, before computation, on base
`94a4e6ccf18845af6c2d37cd797da1082f575d65`. Input is the retained two-front
q10 table of `native_route_v13/`, author
`753fe4f69392ca940754489468e8c8235f6aa583`, digest
`b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc`, which
the separate-engine review under `native_route_v13/review/` reproduced.
No native evolution is recomputed; the large-time reduction, source and
bank geometry and history scope are those of that reviewed pair.
The separate review of this checkpoint is retained under `review/`; statements
taken from its computation are marked as such.

## Result

`native_route_v13` excluded a common two-symbol raw q10 code for the old
sign s=x XOR u XOR a under jointly affine known-seed payloads E(k),N(k),
k=(u,mY,mR,a,b), on the 24 accepted contexts. The preregistered wider
class allows any fixed Boolean readout D of the whole q10 triple, common to
all accepted contexts. Under the preregistered rule the verdict is positive.

- Of the 254 nonconstant readouts, 78 decode s exactly on all 48 accepted
  (s,k) rows for at least one of the 2^36 jointly affine laws. The total
  number of (readout, law) solutions is 7464.
- Of the fourteen nonconstant degree-one readouts, eight succeed. The single
  raw field q10.A equals s under 1456 laws, and equals NOT s under 912
  further laws. The parities A XOR B (384 laws), its complement (424),
  A XOR D (24), its complement (16), B XOR D (8) and its complement (4) also
  succeed. The six others have no law: q10.B, q10.D and A XOR B XOR D, and
  their complements.
- The remaining positive readouts have degree two (29) or three (41).

Thus, under the affine source contract, the q10 cell at L+1 carries s in its
single field A for suitable laws, when the code is read at a fixed field
rather than as a fixed whole triple. q10 is a lattice cell, not a permitted
read (see *Scope*). The exclusion of `native_route_v13` holds for its own
class: no law gives a two-symbol whole-triple code.

s is not singled out. A separate computation in the separate review of this checkpoint
(`review/round1/`), not this checkpoint's checker, shows that for each of the
64 affine functions f of the known seeds k there exist jointly affine laws
with q10.A = x XOR f(k) on all accepted rows (512 to 2016 laws for each f);
the law depends on f, and no single law serves every f. s is the case
f = u XOR a, and q10.A = x holds under 992 laws. What the table shows is the
old input x carried into the field A, with a seed offset chosen by the
law.

One law for q10.A=s, of the fewest seed dependences (mY alone), is

    E = (1, 1 XOR mY, 1),   N = (mY, 1, 1 XOR mY),

that is, Ecode=7 and Ncode=3 when mY=0, and Ecode=5 and Ncode=6 when
mY=1. The checker evaluates every one of the 7464 laws directly against
the 48 native table rows; this one is
`fewest_seed_law_field_coefficients_EA_EB_ED_NA_NB_ND=[1,5,1,4,1,5]` in
the degree-one block of result.json.

## Structure of the solutions (post hoc, outside the decision rule)

These descriptions were computed after the verdict and do not enter it.

- **No affine law with E identically 000.**
  The E=000 subtable equals Native B's single-N table, so in that geometry
  no fixed q10 readout decodes s under affine N, in agreement with Native
  B's loss on the accepted branch u=0, a=b=1. Forty solutions have constant
  E, none has constant N, and none has both constant.
- **Redundancy is large.** Every solution uses at least six distinct
  (s, raw code) values across the contexts (16 laws use six, 680 use
  seven, 6768 use all eight). The q10 triple therefore carries known-seed
  information beside s.
- **The B and D fields jointly carry s.** For no q10.A law are B and D
  jointly independent of s on every context. This check reads the pair
  jointly; the separate review finds B alone independent of s in 8 q10.A
  laws, and D alone dependent on s on at least four contexts in every q10.A
  law.
- **A fresh-bit pad on q10.A.** In 512 pairs, a q10.A=s law and a
  q10.A=NOT s law differ only in constant coefficients: in 256 pairs the
  E.B constant, in 256 all three E constants. Driving that constant by one
  independent initial fair bit c would give q10.A = s XOR c. In none of
  these pairs does the whole triple hide s given the known seeds: the
  number of contexts on which the two-c multisets of raw codes agree for
  s=0 and s=1 is zero (256 pairs) or four of 24 (256 pairs).
- **Known-seed readout.** The diagnostic allowing the readout to depend on
  k succeeds with constant sources E=001, N=000, using six distinct raw
  (s=0, s=1) pairs over the contexts. That readout is a nonlinear
  known-seed computation after q10 and is not counted as fixed delivery.

## Controls

Every control raises before any verdict text is written.

1. **Input pins.** The SHA-256 of `native_route_v13/result.json` and of
   its review result, the recorded table digest, a recomputed digest of the
   table string, and the review's independent digest all agree.
2. **Planted positive control.** A synthetic table plants a full-rank law
   for readout q10.A. Both solvers count 1489 solutions, the solution sets
   agree, and the planted law is among them.
3. **Brute force.** On the real table with features restricted to (1,u)
   and to (1,u,a), all 4096 and 262144 maps are enumerated directly. There
   are no readout solutions; the known-seed diagnostic has 2560 and 143360
   maps; both solvers agree with every count. Because the readout counts
   there are zero, a third run, added beyond the plan, plants a (1,u,a) law
   in a synthetic table. Its brute force gives 818 solutions over 64
   readouts and 149568 diagnostic maps, again equal to both solvers.
4. **Reproduction of the retained raw-pair decision.** With singleton
   readout classes for all 56 ordered injective pairs, the E-first solver
   reproduces every per-pair count retained by `native_route_v13`: 16 affine
   E maps over 8 pairs and no joint law. Both primary solvers also give zero
   joint laws for every pair.
5. **Sign-erased countercontrol.** Replacing the s=1 rows by the s=0 rows
   gives zero for every readout and for the diagnostic, in both solvers.
   This holds by construction, since no readout can separate s once the
   rows agree; it checks the solvers' bookkeeping, not the result.
6. **Solver agreement.** Solver A eliminates two source fields at a time
   over bit sets of affine coefficient pairs; solver B backtracks over a
   greedy affine basis of the context features and determines the other
   contexts linearly. For each of the 254 readouts they agree on the count
   and on the complete solution set. Every solution is checked directly
   against the table. Both solvers agree on the diagnostic decision.

Two mutants were run outside the package: removing solver B's
determined-context test, and reading the table with x=s XOR u. Both stop at
control 2.

## Scope

This is a table-level statement about one cell, q10 at L+1, in the fixed
two-front geometry of `native_route_v13`, with affine payloads in the known
old seeds and the accepted old contexts. It is exact and exhaustive within
that class. It does not show:

- a clean operand: the B and D fields jointly depend on s and on the seeds,
  and native dynamics acts on the whole triple through H(A,B,D)=(B,D,A XOR BD).
  No native stage that consumes q10.A while tolerating B and D is tested;
- a permitted read: Native A allows a single whole-V (q9) read at L+2, and
  under Native A q10 is a private pool cell. No current access rule permits
  reading q10 at any tick. Reading q10.A would need a new access rule and the
  affine known-seed contract, neither of which is adopted;
- a read operation or a post-read law: no read, post-read evolution, or
  complete public-record and outgoing-carrier law is modelled. After q10.A,
  the remaining fields stay correlated with s given the seeds, an untested
  leak or disturbance hazard;
- delivery of the earlier sign specifically, as distinct from the old input
  x with a law-chosen seed offset;
- masking: a fresh bit on the E constants pads q10.A, but the triple still
  reveals s given the seeds in every tested pair;
- that the seed-dependent payloads are an admissible preparation, beyond
  the affine known-seed contract `native_route_v13` states;
- the Y operand, the acceptance predicate, the joint delayed public-history
  and carrier law, a reusable interface, or Native A's six-bit pool, which
  this source variant does not inherit;
- anything about other layouts, multi-cell or multi-time readouts,
  distribution-level instruments or OI generally.

## Replay

    python3 checks.py
    python3 -O checks.py

Both outputs must equal result.json byte for byte. Standard library only,
exact integers; one run takes about seventy seconds. The checker reads the
pinned `native_route_v13/result.json` and its review result as data and
imports no earlier engine. SHA256SUMS covers the other five curated files.
No dispatch, push, merge, F/E designation or #885 write is part of this
checkpoint.
