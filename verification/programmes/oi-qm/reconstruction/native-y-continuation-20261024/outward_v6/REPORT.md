# Exact outward-port scan: a new qY readout, not yet q2 reuse

24 October 2026. Author-checked native geometry result; independent review
pending. Repository read-only. This is the unmodified straight-outward scan;
no extra correction source is included in the result.

## Result and diagnostic distinction

At the actual giant parameters, the seventh outward endpoint has

    q7=qY+7e_z, N7=R+7,
    U_(R+7)(q7)=(0,u,y),  y=x XOR u.

With only qY.D at tickR replaced by arbitrary diagnostic p, the complete
endpoint is exactly

    (x(1 XOR u)(1 XOR p), x(1 XOR p) XOR up, p).

All selector masks cancel. Thus D is a genuine raw transfer of the original
qY operand. A is zero on native inputs; B retains u, which is determined by
the already-public x and designated Y outcome. There is no additional secret
metadata at that terminal boundary, but this is not a Y-only full socket.
The four native codes are000,011,001,010 and retain all four x/y histories.

**This is not established as transfer of q2's actual A register.** A separate
diagnostic replaces only q2.A at R+2 by p2, preserving its other native fields.
At q7 that yields

    (x XOR xu XOR p2 XOR up2,
     x XOR p2,
     x XOR xu XOR p2 XOR xp2 XOR xup2).

For example x=1,u=0,p2=0 gives D=1. No later endpoint in the tested range k3..12
has any raw field or complement equal to p2 uniformly. q7 can obtain the
original operand through the existing wave; its truth table must not be sold
as a reusable q2-output-to-input interface.

## Exact method and hypotheses

Keep T=185, P=12*840^185, S=T+P, d=68, R=S+d. For k1..12 append the initial
current ready ball B_(R+k)(qk) and previous ball B_(R+k-1)(qk), qk=qY+k e_z,
preserving all old sources and prior readiness constraints. No mid-run
cleaning or inserted resource is used. Only newly unconstrained coordinates
are pinned. The same four lower B sources are on the boundary, and each is
at distance2R from the upper pulse. All1,479 inherited source positions are
checked for every k. Only the unknown origin lies on the inherited-source
boundary; the others are outside. The old previous input and opposite pulse
are excluded. Here d+k<T throughout, so the old-source exclusion range is
satisfied. The remote herald/Z blocks remain excluded by x separation.

At R-1 compute the ball of radius k+1 around qk; at R-2 use radius k. Lower
sources are absent or precisely on their first-arrival boundary, using exact
multinomial no-carry parity at the actual giant coordinates. No lower source
is replaced by a behind-front isolated approximation. Upper/lower interaction
is impossible before R. Then apply k+1 complete native updates on shrinking
balls through R+k. All six neighbours and the old local term are retained.

The upper single-pulse values fit the closed radial strip

    W_n(ell,a,b)=U_(n+ell)(a,b,n),
    a>=b>=0, a+b<=ell, a+b+ell<=2k, ell-a-b even.

Budget L=2k is sufficient for every needed pre-collision value. L24 has only
252 triples. The advance is triangular in ell with diagonal permutations of
an eight-state triple; H^12=I and every triple permutation has exponent
dividing840. Induction gives the global identity exponent12*840^L. Since
L<=24<185, actual P is a multiple. Thus the upper values may be evaluated at
reduced axial n'=253-v_z and reduced times251/252, retaining the transverse
coordinates. n' stays positive. This is an exact global-period argument,
not extrapolation from small phase matching.

The implementation evaluates increasing lag layer first, then axial n, so
future lower-layer values are already available. It computes about67,000
packed two-u triples at the largest budget. No giant orbit search or large
torus simulation is used. All full endpoint truth tables are packed over the
32 x,u,mY,mR,p assignments. The initial qY code is checked before the diagnostic
changes only its D field. Native runs are the p=x XOR u lanes.

## Native endpoint table

Entries are whole triples; columns follow(x,u)=00,01,10,11. The table is
independent of both selector masks.

| k | 00 | 01 | 10 | 11 | Raw qY operand field |
|---|---|---|---|---|---|
| 1 | 110 | 101 | 110 | 101 | none |
| 2 | 001 | 111 | 110 | 001 | A=p |
| 3 | 000 | 101 | 000 | 111 | none |
| 4 | 111 | 110 | 000 | 110 | none |
| 5 | 011 | 100 | 101 | 100 | none |
| 6 | 101 | 101 | 001 | 000 | none |
| 7 | 000 | 011 | 001 | 010 | D=p |
| 8 | 010 | 010 | 111 | 111 | none |
| 9 | 101 | 110 | 101 | 001 | none |
| 10 | 001 | 101 | 000 | 011 | none |
| 11 | 100 | 001 | 101 | 111 | none |
| 12 | 010 | 011 | 111 | 101 | none |

The endpoint-only census tests72 raw-field/complement candidates against all
32 diagnostic assignments. Only q2.A and q7.D pass. None of these twelve
whole triples depends on y alone. This does not exclude other locations,
extra controls, larger gadgets, or later times; it is not a general no-go.

## Access and resources

Each extra receiver first sees the upper pulse at R-k, with H^(R-k)(u,0,1).
Because H is bijective this distinguishes u before the old X-instrument
boundary. In particular the q7 prefix is(u,u,1) at R-7. Keep the new receiver
private until its designated read under the existing supplied access rule.
No native shutter or clock is supplied.

Inherited public frontier families stay outside each new cold cone: their
slacks are positive j or k_index, or larger inherited offsets. The checker
instantiates the exact distance formulas; the all-index statement follows
from their linear inequalities. If all seven old public ports remain exposed
through R+k, the inherited joint-frontier theorem requires21k additional
initially independent fair bits beyond R. At q7 that is147 bits (105 beyond
the depth-two window); at q12 it is252. This avenue checks geometry and reuses
the inherited joint-frontier theorem, without re-proving the full record law.
The ready-region cost is the initial new-ball set difference; no optimal cost
claim is made. Existing herald probabilities and failure branches are unchanged.
No second reset or new successful carrier is asserted.

## Checks and limits

`checks.py` verifies4,536 direct spatial-recursion comparisons of upper-strip
values, actual-P divisibility, all17,748 old-source/k cases, complete strip
coverage, inherited k1/k2/k3 full diagnostic formulas, the new k7 formula,
384 diagnostic endpoints,192 native endpoints, mask cancellation, both operand
censuses, and the q2-intervention counterexample. Normal and -O outputs match.
All checks use explicit exceptions. The new period calculation inherits the
triangular-strip theorem developed in six_source_v5_geometry; it is not an
independent review of that theorem. Source geometry is hash-verified unchanged. Replay first uses the packaged
`../parallel_v3/history_control/SOURCE-GEOMETRY.json`, then an isolated sibling
SOURCE-GEOMETRY.json fallback. The source table is not duplicated in the
scan payload manifest.

Run `python3 /path/to/outward_v6_geometry/checks.py` and repeat with `-O`.
No network or file writes occur during replay. No native reset, global access
closure, joint-record certification, new premise, or universal QM claim follows.
