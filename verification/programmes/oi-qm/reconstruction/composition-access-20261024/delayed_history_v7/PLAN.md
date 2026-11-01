# Delayed old-port history and the frozen acceptance carrier

24 October 2026. Research under #912, starting from
`588edce16926ae1a40d1f1e75fc1b5cfb7ccc55e`. Fixed before any computation.
Native A source geometry is author `f24a57a7c23cc1818c04265cec7604f8bc2f410d`;
its eight-port bank is `history_v11/` at the same commit. No observer access,
native compilation, storage, clock or premise is adopted. #885 is read-only.

## Fixed question

Under the hypothetical serial alignment of the `composition_flag_v6/` core
with native ticks L+2..L+91 (or the recorded dilation, L+2..L+361), F8 first
reaches old public port 5 at (0,S,0) at L+77, and F10/F9 at L+79. Is the
complete public record, namely the eight old raw port streams through the
horizon H, the old whole-q9 record, the single whole-V record and the whole
pointer prefix, jointly distributed with the outgoing selected carrier as
the v6 law tensored with an independent uniform tail?

Scope of the carrier: the v6 logical phase wires (q9 at L+2, its six
neighbors at L+1, old q9 at L), held in the supplied isolated logical
storage. The circuit does not act on the lattice. A natively evolving
carrier is outside the question and is probed only as a scope control.

## Candidate argument to be tested

Let C0 be every initial variable except G=(F8,F10,F9), the pointer pads and
the tail bank, the bank triples f_i(t) with max(a_i,L)<t<=H. If no tail
triple reaches any carrier site-time, the carrier record is a function of
(C0,G,pads). The history_v11 chronological inversion, applied with
complement (C0,G), makes the tail word a bijective image of the tail bank
for each fixed (C0,G). The old word through L is a function of C0 when G
reaches no port by L. Then the joint law factorizes for every H<=2L. This
argument is accepted only if the checks below pass.

## Decision rule

HOLDS_WITHIN_SCOPE requires every item:

1. Exact actual-L integer geometry. (g1) Every tail triple of all eight
   ports has distance strictly greater than the time of every carrier
   site-time, minimized exactly over t in (max(a_i,L),2L] at endpoints and
   breakpoints. (g2) Every G source is at distance greater than L+2 from all
   eight ports; the minimum offsets are recomputed. (g3) L+361<=2L.
2. A scaled exact native control on the infinite lattice with the complete
   nonlinear six-neighbor two-slice rule and dirty backgrounds: q9 at the
   origin, n=3 in place of L, offset k=2 in place of 76, port (0,0,-3), its
   bank ray (0,t,-3) for t>n-k-1, sources (-(n+1),0,-1),(-(n+1),0,1),
   (-(n+2),0,0). The enumerated tail is the bank at t=n+3..n+5, which
   covers both first G arrivals, with all 512 G values: 262,144 worlds per
   background. In every background family:
   (s1) port records through n+2 are constant;
   (s2) (Q8,Q10,M, tail records) takes all 262,144 values;
   (s3) for every complete public record, including pads, the accepted and
   rejected selected-cell counts equal the v6 target counts exactly, every
   accepted record on an old-success family has the positive X decoder,
   and an old-failure family offers no carrier.
3. Controls that must be green, or the verdict is void: (x1) an independent
   scalar sparse evaluator agrees with the bit-sliced evaluator on sampled
   worlds; (x2) the seven-site inverse recovers old q9 in every world;
   (x3) duplicating one tail triple must reduce the (pool, tail) support.

Countercontrols, quantified without presuming their outcome:

- (c1) Known tail: fix the tail bank and vary only G. Report whether the
  tail records depend on G, the complete record/carrier TV from the v6
  reference and the minimum accepted decoder determinant. The bank is
  called load-bearing only if that TV is positive.
- (c2) The duplicated-triple control's joint record/carrier TV.
- (c3) Native continuation: the q8 field left to native dynamics until the
  first tail arrival at n+5. Report the TV of its joint law with the tail
  records from the product of marginals. Frozen storage is called
  load-bearing only if that TV is positive.

NEGATIVE for this construction if (g1) fails at actual L, or if (s1)-(s3)
fail in the scaled control with all controls green. A scaled control does
not establish the actual-L statement; that rests on the written argument
and item 1.

Standard library only, exact integers and fractions, explicit exceptions.
Normal and -O output must equal result.json byte for byte. The tail bank is
the supplied history_v11 resource; its existence is not derived. No native
storage, compilation, clock, access closure, A1/A2 equivalence, dispatch,
F/E designation or merge follows.
