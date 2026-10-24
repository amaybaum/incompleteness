# Simultaneous phase-carrier control: a finite reduction

Research on #910, source `3f440c59660d7255aa8a727ff8b5de8289004f80`.
The real native phase at N=R+9 contains previous q8=(0,y,0) and current
q9. This is one two-slice physical boundary, not three same-tick public ports.
No access to the previous field is adopted here.

## Required two-sign control

The actual q9 table admits the desired current triple
`q9=(0,y XOR a,y XOR b)` while retaining the earlier q8 value, with these
unique initial-J values:

| a,b | J when u=0 | J when u=1 |
| --- | --- | --- |
| 00 | 000 | 101 |
| 01 | 110 | 000 |
| 10 | 010 | 001 |
| 11 | 111 | 010 |

Thus the desired phase encoding of (X,Y,R) has a finite seed-control target.
This is a pointwise deduction from the checked native table. The nonlinear
J preparation is not supplied by the existing affine apparatus sources and
is not adopted as a new initial resource.

For all four mask patterns, the unique J truth table has Boolean degree 3.
Writing products as AND and sums as XOR, its components are

    J.A=u + ua + b + uab,
    J.B=a + ua + b + ub + ab,
    J.D=u + ub + ab + uab.

Only patterns 00,10,11 are needed on the calibrated success branch. On those
patterns ab=b, so a degree 2 extension suffices:

    J=(u + b + u(a+b), a + u(a+b), u+b).

No choice is made for physical failed-run behavior by this algebraic
extension. A native implementation must retain failures and its actual raw
output. Neither a nonlinear truth table nor this simplification is a native
seed-only preprocessor.

## Exact obstruction for one affine upper source

Exhaustive evaluation of all 4096 maps
`J=c XOR u*cu XOR a*ca XOR b*cb`, with four arbitrary three-bit constants,
finds 32 whose raw q9 outputs are common across old u for every a,b. None
provides three distinct raw mask codes on 00,10,11, even when01 is left
unconstrained. At most two distinct accepted mask codes occur.

There is also a short structural reason. For fixed u,x, J maps bijectively
to the full q9 triple. The eight common native code pairs split into four
groups, each containing two pairs, according to delta=J1 XOR J0. An affine
J has a fixed u coefficient delta. It can therefore use at most two common
code pairs, regardless of its affine dependence on a,b. Adding coefficients
of old selector masks cannot repair this: bijectivity forces those
coefficients to vanish if the raw output is to remain independent of them.

The actual one-mask route J=(u XOR a,a,u XOR a) is a positive control and
passes. This excludes only one affine initial-J source for the stated full
raw phase-code target; it does not exclude native nonlinear processing of
initially affine seed sources, or a richer interface.

## Shallow spatial fork: safe control geometry, coupled backgrounds

At N=S+77, consider targets A=(-1,S,76), B=(0,S-1,76), C=(0,S,77)
and new extreme sources (-S-78,S,76), (0,-78,76), (0,S,S+154).
Each source is distance N from its own target and N+2 from both others.
The A/B sources lie outside all inspected earlier ready balls by at least 2;
C is the existing J boundary source. The corresponding positive-x extreme
source fails an old ready-ball check by 401, and is rejected.

These distances do not supply the output laws. At A, the old R selector
source arrives at N-2 and its first two frontier coordinates at N-1,N.
At B, the origin and W already arrive at N-2. Hence the reset_v9
first-front-only initializer cannot be reused for those targets. It would
omit coupled background and bank contributions. A valid spatial probe must
retain those sources and justify a new exact bounded-lag reduction.

The cheaper next native candidate is to implement the required seed
nonlinearity using an additional first-front source near J. The next probe
will state its finite family before calculation and will keep all native
cross-interactions. Same-tick Y readout, calibrated masks/heralds, fair z,
access closure, complete failures and the joint public law remain open.

## Replay

`python3 checks.py` and `python3 -O checks.py` reproduce `result.json`.
The only computation input is the retained actual reset_v9 result table,
whose checksum is verified. Results use integer arithmetic; controls raise
before verdicts. No surrogate probability distribution, late readiness,
unknown-input copy, physical premise or full-reset claim is introduced.
