# Native affine-source controller for the two-sign phase code

Research checkpoint. The fixed symmetric 512 family contains two pointwise
native witnesses. No nonlinear initial seed prior is needed for this local
controller. Separate-author review is pending.

## Physical source specification and result

Use the same original-time depth-nine preparation as reset_v9 and preserve
all its original sources and public banks. Keep W=111, Q,C,G unchanged.
Let delta=a XOR b, with a,b initially specified apparatus bits. Prepare

| Source | Original-time position | Triple |
| --- | --- | --- |
| J | (0,S,S+154) | (u XOR b,a,u XOR a) |
| Kplus | (1,S,S+153) | (delta,0,delta) |
| Kminus | (-1,S,S+153) | (delta,delta,delta) |

All field values are affine functions of u,a,b. None contains unknown x or
a copy of the later y. The two K payloads can also be swapped.
For every native x,u,mY,mR and masks (a,b)=00,10,11, the unchanged rule gives

    q8 at R+8 = (0,y,0),
    q9 at R+9 = (0,y XOR a,y XOR b),  y=x XOR u.

Thus one physical two-slice phase contains a fixed raw encoding of the
three signs Y,X,R: previous q8.B is Y, current q9.B is X and current q9.D
is R. The complete designated cells are `(0,Y,0)` and `(0,X,R)`, common
across old input/seed/mask histories at fixed signs. This is not three
same-current-slice public readout ports, and no previous-slice access rule
is adopted. The remaining apparatus fields are not declared erased.

The native interaction of initially affine sources supplies the nonlinear
seed processing missing from the single-J truth table. It is not obtained
by computing that table externally and inserting a nonlinear J at time zero,
nor by splicing a desired triple into a later native slice.

## Finite search and exact calculation

The first fixed 64 family used one Kplus. None met the whole accepted-mask
target; the best candidates missed 8 of 48 accepted input/history rows. Some
introduced selector-mask dependence, which is retained in the results.
The sole subsequent extension added Kminus with an independent constant
triple coefficient: exactly 512 candidates C,Vplus,Vminus. The initial
source formula was fixed beforehand:

    J=(u XOR a,a,u XOR a) XOR delta*C,
    Kplus=delta*Vplus, Kminus=delta*Vminus.

Exactly two candidates pass every accepted row: (C,Vplus,Vminus)=(4,5,7)
and (4,7,5), using code4A+2B+D. Neither gives the prescribed raw output on
failure pattern01. Every mask and failed pattern remains in the retained
32,768-row output table, encoded by one hexadecimal digit per triple.

The K sources break x reflection, so the upper evaluator keeps signed x
and only uses the surviving y reflection. It evolves Q,C,G,J,Kplus,Kminus
as one coupled cluster. Its strip budget is 18; the retained triangular-strip
period argument gives 12*840^18, exactly dividing actual P. The proof does
not depend on x reflection: same-layer transverse states update in parallel,
each by an eight-state permutation driven by lower layers. The unchanged
lower W/origin front uses reset_v9's exact two-layer reduction. Upper and
lower sources cannot interact before R; all final collisions are then
evolved together in the full native diamond.

The controls pass before verdicts:

- 4,730,880 scalar-lane comparisons of the signed upper strip with direct
 native recursion at bounded coordinates;
- 9,240 comparisons with the independently retained axis-only evaluator;
- preservation of all 4,096 single-K rows inside the symmetric family;
- pointwise preservation of native q7 and q8;
- the equal-mask positive control a=b, where both K sources vanish;
- 32,768 complete input/history/seed rows, including all selector masks.

The controls are bit-packed exact integer computations. The large scalar
counts describe covered lanes, not millions of separate long simulations.
The written period theorem justifies the astronomical time reduction;
small-coordinate checks validate the new evaluator rather than replace it.

## Geometry and retained physical failures

J,Kplus,Kminus all have distance N=R+9 from q9. Each K is distance N+1
from q8, so cannot alter its R+8 read. Their current initial positions are
outside every inspected earlier ready ball and match none of the 1,479
retained source positions. Their x coordinates ±1 differ from all six
old public-bank rays' fixed x coordinates 0,±T,4T. They occupy boundary
exceptions in the existing q9 preparation, not new zero pins on the bank.
Distances to each lower signal source and W are at least 2R, preserving the
pre-R separation required by the lower/upper initialization.

Pattern01 is never a target-success mask. Its actual q9 fields for these
witnesses are `(u,y,x(1 XOR u))`; they retain old information. They are
explicitly recorded, not overwritten by a chosen quantum failure state.
A terminal no-offered-carrier convention, a herald law, or further access to
these fields must be supplied by the complete instrument contract.

## Interventions and remaining limits

The construction is still a native-family phase code. Replacing only q8.B
by arbitrary p while keeping its real preceding state produces 24 mismatches
among 48 accepted rows for each p, for each witness. For example x=0,u=1,
a=b=0,p=0 gives q9=111 instead of 000. The actual native q8 value is preserved
and used by the update, but q8 alone is not an arbitrary reusable input socket.
The surrounding history correlations remain part of the native interface.

This checkpoint supplies local simultaneous phase information. It does not
supply the calibrated mask sampler/herald, fair z, a joint public/failure
law, same-tick Y access, arbitrary next-stage closure, full target coverage
or OI–QM equivalence. Freshness of a,b relative to previous informative
records is an explicit resource obligation. No premise or access change is
adopted.

## Replay

From this directory in the retained tree:

```sh
python3 checks.py > /tmp/oi-controller-single.json
cmp /tmp/oi-controller-single.json single-result.json
python3 checks.py --symmetric > /tmp/oi-controller-symmetric.json
cmp /tmp/oi-controller-symmetric.json symmetric-result.json
```

Both commands also pass with `-O`, byte-identically. The symmetric run checks
its single-K subset against retained `single-result.json`. PROVENANCE.json
pins all inherited inputs; SHA256SUMS covers this checkpoint. No special
workflow, F/E designation, merge or external certification was performed.
