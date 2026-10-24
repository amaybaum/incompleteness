# Native Y reset: actual q7 interface and one-step continuation

Research only, consistency axis. This is an initial probe plan, written before
the new computations. It starts from the corrected #910 q7 construction; no
generic cold socket, reset, decoder, fresh resource, or access rule is assumed.

## Fixed target and preparation

The #885 reset target is an outgoing carrier decoding to
`(y XOR a, y, y XOR b, z)`, with `ab=00,10,11` in ratio `5:3:2` and
fresh fair `z`, conditional on every earlier outcome and herald. The whole
public history, outgoing carrier and failures must be checked jointly.

Set `N=R+7`, `q7=qY+7 e_z`. The adopted initial q7 ready region is current
`B_N(q7)` and previous `B_(N-1)(q7)`, preserving the stated lower sources,
the upper pulse `Q=(u,0,1)`, and its correction `C=(u,0,u)` at
`f=q7+N e_z`. It produces the native endpoint `(0,0,y)` with `y=x XOR u`.
The informative earlier prefix stays private under the supplied delayed-access
rule. No preparation after initial time is permitted.

## Preregistered bounded probe and decision rule

1. Export the actual old local triple and six incoming triples that produce q7,
   for all 32 qY.D diagnostic rows and the separate q2.A diagnostic. Check the
   exact native recurrence and reproduce the clean native family. These are
   the known incoming two slices, not a cold neighborhood.
2. Test the next straight outward site `q8` at `N+1`. Audit whether its cone
   is determined by the adopted q7 preparation. A first-arrival initial triple
   at `g=q7+(N+2)e_z=f+2e_z` is a possible missing boundary resource.
   If its exact transfer is bijective while preserving the q7 prefix and
   original readouts, classify unqualified immediate continuation as
   underdetermined, scoped to this direction and this preparation.
3. Explicitly study one initial-only extension: current `B_(N+1)(q8)` and
   previous `B_N(q8)`, preserving all original sources and C, and leave only
   the triple G at g variable. Evaluate the full nonlinear Q/C/G upper
   cluster with the exact bounded-lag strip and actual giant-period shift;
   retain lower-source interactions in the local diamond. This extension is
   a tested candidate, not silently part of the adopted q7 construction.
4. Enumerate the eight G values independently for each apparatus seed u. A
   candidate immediate routing exists in this finite family only if a choice
   `G(u)` independent of unknown x and diagnostic input gives the common
   one-hop code `(0,y,0)` for both x values. Separately replace only q7.D at N
   by a free p7, keeping its actual native past, and require `(0,p7,0)` for
   every row for a reusable local routing claim. If no choice succeeds,
   report this finite-family obstruction, not a general native no-go.

Controls required before any verdict: exact inherited file digests; actual-P
period divisibility; direct native small-coordinate control of the full
multi-pulse strip; G=0 agreement with an independent Q/C evaluator;
first-arrival geometry and source/readiness exclusions; q7 and q2 inherited
diagnostics; the full final two-slice recurrence. Structured JSON records
measurements and verdicts. Normal and `python -O` runs must replay identically.

Even a successful routing probe does not establish the 5:3:2 sampler, fresh z,
conditional resource independence, a reset herald, or a joint instrument law.
Those require additional explicit native constructions.
