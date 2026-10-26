# Native Y reset: exact q7 interface and the next outward tick

Research only, consistency axis. The corrected native q7 code remains `(0,0,y)`.
This checkpoint supplies its actual incoming neighborhood and excludes a specific
immediate continuation: one further outward tick, with one added initial
apparatus boundary triple depending only on u, cannot produce any common
full-triple encoding of y. It also cannot be a history-independent q7 input
socket. No general native reset impossibility is claimed.

The fixed #885 target is an outgoing carrier decoding to
`(y XOR a,y,y XOR b,z)`, with `ab=00,10,11` in ratio `5:3:2` and fresh fair z,
conditional on every earlier outcome and herald, including every failure branch.
No part of that reset distribution is constructed here.

## Actual native interface

Use XOR arithmetic. `T=185`, `P=12*840^185`, `S=P+185`, `d=68`, `R=S+d`,
`N=R+7`, and `q7=qY+7e_z`. Coordinates below are relative to qY. The preparation
is the existing current ball `B_N(q7)` and previous ball `B_(N-1)(q7)`, preserving
the original sources, upper pulse `Q=(u,0,1)`, and correction `C=(u,0,u)` at
`f=(0,S,S+2d+14)`. The native signal is `y=x XOR u`.

The old local triple at time N−2 is **111**, not blank. At time N−1 the six
incoming neighbors are exactly:

| Neighbor relative to qY | Native triple |
| --- | --- |
| `(-1,0,7)` | `(1 XOR u,1,u*mR)` |
| `(1,0,7)` | `(1 XOR u,1,u*mY)` |
| `(0,-1,7)` | `(1 XOR u,1,x*u)` |
| `(0,1,7)` | `(1 XOR u,1,u*(mY XOR mR))` |
| `(0,0,6)` | `(1 XOR x,0,1 XOR x*u)` |
| `(0,0,8)` | `(1 XOR u,1,0)` |

Their XOR is `(y,1,1)`; the native update gives
`111 XOR H(y,1,1)=(0,0,y)`. Selector-mask and input history remain in the
neighbors even though they cancel at the readout. `results.json` retains the
actual old and incoming triples for all 32 qY.D interventions and all 32
separate q2.A interventions. The latter still fails raw late-input transfer.

The q7 prefix at R−7 remains `(u,u,1)`, hence private under the supplied delayed
access rule. The earlier signal and history have not been erased.

## The next cone is not prepared by the endpoint result

Let `q8=q7+e_z` and `g=f+2e_z=q7+(N+2)e_z`. A current initial triple G at g has
first-arrival distances N+2 to q7, N+1 to q8, and N to q9. It therefore cannot
change q7 through N or its incoming neighborhood. It lies outside all 15 old
ready regions and is farther than N+1 from all their receiver centers. It changes
none of those receiver histories through N+1. It overwrites no inherited source
or protected frontier source.

The q7 ready prescription leaves g outside its specified ball. For each fixed
original qY diagnostic row, all eight choices of G map bijectively to the eight
q8 triples at N+1. Thus the adopted q7 preparation alone does not determine the
next outward endpoint. This is an explicit family of compatible initial
completions, not an argument that arbitrary dynamics must fail.

## Explicit initial-only extension and obstruction

The tested extension enlarges readiness to current `B_(N+1)(q8)` and previous
`B_N(q8)`, preserving the four lower sources, Q, C, and G, and setting remaining
unspecified entries in those balls to zero. It contains the adopted q7 ready
balls. All 1,479 inherited source entries were checked: only the original input
is on the new boundary and none is in its interior. The four lower sources are
on its boundary. The previous input, opposite pulse, remote blocks and protected
frontier rays are excluded, with `d+8<T`. C and G are explicit exceptions to the
new blank prescription. This is a candidate initial preparation, not a midrun
cleaning operation or a silently adopted resource.

The nonlinear Q/C/G cluster is computed together; isolated pulse superposition
is not used. In inward axial coordinates its sources are at `0,-14,-16`. The
relevant upper neighbor q9 at N has actual `(n,t)=(P+244,P+260)` and lag 16.
The triangular strip exponent `12*840^16` divides actual P, so the exact query
reduces to `(244,260)`. This uses the previously established strip-period lemma;
this checkpoint checks its divisibility and bounded native controls, not an
independent general proof of the inherited lemma. Lower-front values retain
actual giant-coordinate no-carry parity, followed by the full native collision
diamond.

Write `(alpha,beta,gamma)` for the change at q9,N relative to G=000. This change
depends only on u and G. At q8,N−1 the actual old triple is `(1 XOR u,1,0)`.
For a separate intervention replacing only q7.D at N by p7, with its actual
native past retained, the resulting first two q8 fields are

`A = x XOR beta`,

`B = 1 XOR x XOR u XOR x*u XOR p7 XOR gamma`.

The complete third-field formula and all 256 rows are checked by `probe.py`.
In particular A retains x for every G(u), so the whole triple cannot depend
only on the free p7. A clean cell at one time is not a supplied cold socket.

For the native family `p7=y=x XOR u`, these become

`A = x XOR beta(u)`, `B = 1 XOR x*u XOR gamma(u)`.

For B to depend only on y, comparing the two y=0 histories requires
`gamma(1)=1 XOR gamma(0)`. Comparing the two y=1 histories instead requires
`gamma(1)=gamma(0)`. This contradiction excludes **every common native two-code
encoding** obtainable from this one-source, one-tick family, even if the code is
not stipulated in advance. It is stronger than failure of `(0,y,0)` alone.
The exhaustive 64-pair G(0),G(1) test confirms both this native obstruction and
the arbitrary-q7-input obstruction. Other directions, multiple new sources,
longer routing and alternative workspaces remain open.

For G=000 the native q8 values, ordered `(x,u)=00,01,10,11`, are
`010,011,111,101`; they exhibit the retained history directly.

## Resources, controls and scope

All preparation is at initial time. A candidate G(u) uses the existing apparatus
seed and would add no unknown-input copy or independent fair seed. No such G
solves this routing family. No freshness of candidate reset resources is
inferred. The old seven-port public window through R+8 would require 168
preloaded independent fair bits beyond R, 21 beyond the q7 window, under the
inherited joint-frontier theorem. The ready-region extension may change later
backgrounds, so that theorem concerns the joint public law; only the isolated
change of G is proved not to affect those old receiver histories pointwise.
No new public-access mechanism, reset herald, success rate, or carrier decoder
is provided. The first reset's existing success and failure branches are not
reclassified by this result.

`PROBE-PLAN.md` predates the first computation. `SECOND-PROBE-PLAN.md` records
the broader two-code decision rule before its evaluation. Verdicts are generated
only after all controls pass and read structured data. Controls include 9,120
scalar direct full-tripole comparisons, 560 independent G=0 dipole comparisons,
actual-period divisibility, 1,479 source exclusions, 64 exact q7 incoming
interfaces, 768 extension diagnostic rows, all 32 endpoint permutations, and
both 64-pair encoding tests. Normal and optimized executions are byte-identical.
The exploratory mask-free shorthand for the neighbor table was rejected by its
all-row control; the table above retains the selector masks and passes.

Replay from this directory:

```sh
python probe.py > replay.json
python -O probe.py > replay-O.json
cmp replay.json replay-O.json
cmp replay.json results.json
```

`checks-summary.json` gives compact structured findings and the result digest;
`results.json` is compact full evidence (about 46 KB). The two inherited Python
modules are byte-pinned copies of the prior exact model; the source geometry is
read from the packaged sibling history-control directory, with digest checking,
or the original scratch outward directory. `SHA256SUMS` lists the checkpoint
payload. No formal certification, full instrument law, or OI-to-QM equivalence
is asserted.
