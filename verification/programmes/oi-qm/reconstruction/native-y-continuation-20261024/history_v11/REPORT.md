# Eight-port public-history extension after the post-Y phase

Research continuation from #910 at
`71d291297d0a662cbb9377ab48eef7aa4b839e77`. This is a written conditional
finite-horizon theorem with exact geometry and bounded native controls. It
adds no native measurement or physical source of the independent resources.

## Result and supplied resource

For every fixed integer 1<=Delta<=L, the old seven raw public streams and
the new remote herald stream admit an explicit chronological independent
frontier bank through H=L+Delta. The full specified noise word has

    B_H = 6P+18d+189+24Delta

bits and is uniform conditional on its initial-bank complement. In
particular the future tail after L has 24Delta bits and remains uniform
conditional on the complete retained public past through L and all
bank-complement variables. The prepared selected phase and informative
heralds are such complement functions. The actual future physical carrier
or its neighborhood need not be complement functions.

The initial bank triples are supplied independently and uniformly conditional
on the complementary initial configuration and readiness. They are present
at the original initial time, with none inserted during evolution. This is
an explicit resource extension of the candidate. Independence, access and
the clock remain supplied assumptions rather than derived physical laws.

## Ports and source coordinates

Keep T=185, P=12*840^185, S=T+P, d=68, R=S+d, L=R+9 and the enlarged
no-wrap torus side 256L+64T+1. Retain these ports and informative deadlines:

| i | Port p_i | Deadline a_i | Initial current frontier f_i(t) |
| --- | --- | --- | --- |
| 0 | (0,T,0) | T | (0,T-t,0) |
| 1 | (0,0,-8T) | T | (0,0,-8T-t) |
| 2 | (T,P,0) | S | (T,P+t,0) |
| 3 | (-T,P,0) | S | (-T,P+t,0) |
| 4 | (4T,P,0) | S | (4T,P+t,0) |
| 5 | (0,S,0) | S | (0,S+t,0) |
| 6 | (12R,0,0) | R | (12R-t,0,0) |
| 7 | (48L,0,0) | L | (48L+t,0,0) |

Reserve each triple for a_i<t<=H. For old ports these are the same source
rays already used through L. For port 7 the prior prefix is blank and its
whole raw informative record at L is (0,G,0). Its frontier sources begin
strictly after L and do not affect that record. The z port remains private
under the retained convention; exposing it later is another interface task.

At L the old bank has 3[2(L-T)+4(L-S)+(L-R)] bits, equal to
6P+18d+189. Extending each of seven streams contributes 21Delta bits and
the new herald stream contributes 3Delta more. This counts shared source
seeds only where they actually occur; the six herald/local-mask/z seeds
are bank-complement variables, not newly redrawn bank bits.

## Exact geometry for the whole window

Every f_i(t) is at axial distance t from its own port. For each port j,
distance(f_i(t),p_j)-t is piecewise affine in t. Its minimum over the entire
integer interval is attained at an endpoint or an absolute-value breakpoint.
The checker evaluates all such breakpoints at the maximal H=2L; this covers
every smaller declared Delta. It verifies no arrival at another public port
before t. The only equal-time cross-edges are 2->5 and 3->5, consistent with
the displayed ordering. The new herald adds no same-time cross-edge.

Solving equality of the affine rays in all coordinates checks all 28 family
pairs for distinctness. The two collinear herald rays lie in disjoint x
intervals. The old collinear y rays remain on disjoint sides of their ports.
For different axes, the unique possible intersection parameters must both
lie in their reserved intervals, which the check excludes.

All 192 family/ready-cone pairs are excluded by the same exact minimization.
The 24 enclosing current ready balls include all eight informative ports,
the original selected-read sources, original outgoing endpoint and remote z,
all outward local phases through q9, and the new private z receiver. The
previous ready balls are smaller at the same original centers, so exclusion
from these current balls also protects them. The local source exceptions
origin, W, Q, C, G, J, Kplus and Kminus are separately checked. The large
herald and old source programs lie in their respective ready balls; their
potentially enormous source lists need not be materialized to exclude them.

The bank is outside the original-time dependence cones of previous q8 at
L-1, current q9 at L, current remote z and new informative G at L. Thus the
entire retained selected phase and the informative branch record through L
are bank-complement functions. This is not a claim about their enlarged
future dependence cones. Source/ready/target coordinate spans remain less
than half the specified torus side, and 2H is less than the side, preserving
the integer distances and unique own-port axial shortest paths.

## Chronological inversion and conditioning on the past

Fix every initial variable except the bank; call that fixed complement C.
Order input/output blocks by increasing t and then increasing i. No later
input reaches an earlier output. Same-tick cross-influence respects this
ordering, so all other influencing bank inputs are already earlier.

Along a bank triple's unique length-t axial path to its own output, only
the preceding axial vertex can depend on that triple at each first-arrival
step. The other five neighbors and the local previous slice are too early
to depend on it. For fixed earlier inputs and C the step therefore acts as

    v -> alpha XOR H(v XOR beta),

where alpha and beta may contain arbitrary dirty background. H permutes all
eight triples, so the step and its composition are permutations. Starting
with the first output, invert these diagonal permutations sequentially. This
gives a bijection from the whole independent bank to the entire noise word.

Consequently, for each admissible C=c and each complete raw noise word n,

    Pr(N_H=n | C=c) = 2^(-B_H).

Write N_H=(N_L,N_tail), where N_L is the old seven-stream word through L.
Uniformity of the whole word gives product uniformity of these coordinates.
For any compatible informative record D and any nonzero-probability past,

    Pr(N_tail=w | C=c, D, N_L=n) = 2^(-24Delta).

Here D is a function of C and includes the informative old/new heralds and
allowed selected-phase records. This formula explicitly conditions on the
already exposed old noise; it does not call the entire word fresh after
part of it has been observed. Averaging over c preserves the tail law.
Earlier terminal failures remain in D and never restart an offered carrier.

The future raw-noise factor can therefore be adjoined to any retained
selected-phase/branch law without changing that law. It cannot be adjoined
independently to a future carrier that already uses the same bank. Its
joint law with every newly read response-relevant field must be established.

## Bounded controls, scope and replay

The self-contained checker imports no predecessor engine. Direct nonlinear
six-neighbor recursion retains the previous local slice in two dense
backgrounds and evaluates four chronological bank blocks: a same-time old
two-port cross-arrival and two consecutive future-herald blocks. All 8,192
assignments give full bijections, with 1,170 conditional diagonal permutation
checks. The future-herald source preserves the whole earlier herald prefix.

Pinned or duplicated source triples reduce support from 4,096 to 512 and
are detected. An extra read of a reserved private bank triple gives a joint
support of 8 with its later output, where independence would require 64.
That control demonstrates why changing access changes the history theorem.
These short native controls validate the local mechanism; the all-index
argument and exact astronomical geometry carry the actual stated window.

Run `python3 checks.py` and `python3 -O checks.py` from this directory; both
must equal `result.json` byte for byte. The proof depends on the stated
finite-speed/first-front native rule, explicit bank prior and retained
access convention. New instrument sources, new public ports, exposed private
fields, changed readiness or horizons beyond 2L need new audits. A reusable
native reset, access closure, calibrated probability selection, A1 coverage
and general A2 bounds remain open. No formal certification is claimed.
