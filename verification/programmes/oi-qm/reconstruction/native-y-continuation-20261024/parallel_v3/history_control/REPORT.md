# Native history sidecar: x is already adjacent to the arriving Y operand

24 October 2026. Avenue 2 of the owner-authorized parallel native-Y investigation.
Repository read-only. No new preparation or access premise is adopted.

## Main result

The earlier public X bit does not have to be brought back from the old stationary
public port merely to supply a nearby logical control. The accepted depth-two
outward construction already creates a native sidecar:

    s = qY + (0,-1,2),
    U_(R+1)(s) = (0, 1 XOR y, x),    y=x XOR u.

Its complete raw prefix is zero through tick R. At phase time R+2, the lattice
therefore contains both:

- the previous-slice D bit x at s;
- the current-slice raw A bit y at q2=qY+(0,0,2), one spatial step away.

This is an actual native location/time result with the inherited initial
resources. It is not an externally retained classical record, an initialized
copy of unknown x, or a new memory assumption. It removes a long-distance
transport obligation from one possible implementation route for G.

It does **not** implement G, provide persistent storage, or justify exposing the
sidecar indefinitely. At R+2 the sidecar's current triple has a new dependency
on the old input phase and on initially free frontier symbols.

## Exact local proof

Use the unchanged native rule

    U_(t+1)(v)=U_(t-1)(v) XOR H(XOR of six neighbours),
    H(A,B,D)=(B,D,A XOR BD),

and the actual parameters T=185, P=12*840^185, S=T+P, d=68, R=S+d.
Coordinates below are relative to qY=(0,S,d).

At tick R, the six neighbours of s=(0,-1,2) are:

| Relative site | Entire raw triple |
|---|---|
| (0,-1,1) | (x,1,y) |
| (0,-1,3) | (0,1 XOR u,0) |
| (0,0,2) | (0,u,1) |
| (0,-2,2) | (0,0,0) |
| (1,-1,2) | (0,0,0) |
| (-1,-1,2) | (0,0,0) |

These follow by evaluating the already retained exact pre-interaction recurrence
and one ordinary native update. They hold for every old selector-mask assignment.
The old local slice U_(R-1)(s) is zero. The neighbour XOR is `(x,0,1 XOR y)`, so
one further ordinary update gives

    U_(R+1)(s)=H(x,0,1 XOR y)=(0,1 XOR y,x).

All values lie inside the accepted q2 backward diamond; no new initial cold
region, seed, mirror correlation, or source is required. In particular this
result consumes no old independent frontier coordinates.

### Prefix and diagnostic scope

The upper pulse is at distance R-1 from s. Its first-arrival multiplicity is
that of displacements `(1,R-2)`, namely R-1, which is even. Its first possible
arrival cancels. Every lower boundary source is at distance at least R+1, so
none can arrive earlier. At tick R the local current-source spacetime parity
is wrong; the old previous-slice input first reaches s only at R+2. The inherited
ready cone excludes all other earlier effects. Thus the entire sidecar prefix
through R is zero.

A diagnostic replacement of the original qY D operand by p at tick R cannot
reach s at R+1: their distance is three and only one tick elapses. The sidecar
remains `(0,1 XOR native_y,x)`, while the accepted q2 diagnostic has A=p.
Consequently the sidecar B bit must not be silently substituted for the actual
arriving p. Its D bit supplies x independently of that diagnostic.

The new sidecar can remain private. Making it an additional public port or
changing the Y observation boundary requires a declared protocol and joint-law
check; no such change is made here. Its blank prefix is a useful property, not
an access-closure theorem or a native clock.

## A precise next-tick memory boundary

In absolute coordinates s=(0,S-1,d+2). At tick R+2:

- the old previous-slice input triple g at the origin is at distance R+1 and
  can first arrive at this tick;
- the old current-slice frontier M1=(0,-1,0) is at distance R+2 and can first
  arrive at this tick as well.

The frozen 1,479-entry source table has only the current origin x source inside
the sidecar's radius-(R+2) current cone. That source and the relevant current
selector/pulse sources belong to the opposite spacetime parity sector. Remote
herald/private-Z sources remain outside by the inherited x-separation bound.

A useful exact countercontrol is to set the *nuisance coordinates in the queried
spacetime parity sector* to zero within this enlarged causal cone, retaining g.
This is an explicitly conditioned or modified complement for a counterexample,
not the accepted independent-fair-complement law and not a new preparation.
The other parity sector can retain the full original apparatus unchanged.
Then the sidecar's next current triple is exactly

    U_(R+2)(s)=H^(R+1)(g)=H²(g).

The first equality is the single-pulse first-arrival law: `(S-1)&(d+2)=0`
makes the shortest-path count odd. The second uses R+1=2 modulo12. H² is a
permutation of all eight old triples. Therefore the native sidecar result does
not imply that the next current D bit still stores x, or that a continued raw
read is harmless for every complement.

Conversely, in the separate countercontrol g=0 with only M1 varied in that
sector, the output is `H^(R+2)(M1)=H³(M1)`, also a permutation. The frontier
really can affect the next read. Neither countercontrol proves an unconditional
leak under the original prior, nor proves that M1 masks the whole enlarged
joint record. Such masking must account for M1's prior use in old public
records and cannot be inferred from a marginal uniformity check.

The logical x control is present in the *previous* slice at phase time R+2,
even though the *current* slice at the same location may already have these
additional dependencies. Global second-order phase availability and persistent
readable storage are distinct claims.

## Consequence for native G integration

The logical target is still

    G(x,A,B,D)=(x,B XOR A,D XOR1 XOR xA,A).

The next potentially useful native update is at s,t=R+3. Its old-slice term is
the proved `(0,1 XOR y,x)`, and its current-neighbour sum includes q2's raw
`(y,y,1 XOR xy)`. This gives a concrete adjacent two-slice starting point.
However, the other five current neighbours and their old-input/frontier
influences have not been computed here. Treating them as zero or freely
programmable would be invalid. An actual R+3 calculation also reaches lower
sources behind their first-arrival fronts; the q2 three-step proof cannot be
extended by simply retaining its first-arrival-only lower formula.

This avenue therefore advances from an unspecified historical-memory task to
an explicit local phase-integration task. It does not claim the latter solved.
The auxiliary-register and direct-reset avenues can use this sidecar theorem
only with their own timing, source, and joint-record compatibility checks.

## Checks and review status

`checks.py` uses the standard library, writes no files, and keeps all checks
active under Python -O. It checks:

- all16 x,u,mY,mR assignments, all32 operand diagnostics, the six-neighbour
  table and the sidecar update;
- exact distances, actual parity, blank-prefix conditions, and source geometry;
- all1479 old source positions at the next-tick boundary;
- both eight-state first-arrival countercontrols and actual H phases;
- 240 independent direct-recursion previous-pulse cases, including dense
  backgrounds in the opposite spacetime sector.

The local native-sidecar part reuses the handoff's `core.py`; this is disclosed
in PROVENANCE.json and is not a new independent proof of that inherited
recurrence. The parallel independent reviewer separately confirmed the sidecar,
blank prefix and diagnostic distinction with a fresh symbolic stencil. Their
review report, not this author report, controls that review's exact scope.
The wider transport-proof review remains open.

Run from any working directory:

    python3 /path/to/history_control/checks.py
    python3 -O /path/to/history_control/checks.py

Normal and optimized outputs are byte-identical and retained beside the checker.
