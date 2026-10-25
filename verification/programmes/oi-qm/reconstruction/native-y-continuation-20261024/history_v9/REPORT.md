# Conditional public-history law for the workspace-assisted Y route

Research checkpoint based on #910 at
`f264dff4eacae84959b4a4419be204fb8c31c9e3`. This is a written conditional
theorem with exact bounded controls, not a new native reset or a Lean
certificate. The initial readiness, independent frontier prior, access
restriction and clock remain the supplied assumptions of the candidate.

## Result

The W source can change later old-port backgrounds without invalidating the
chronological frontier argument. With the explicitly retained independent
bank below, the complete old public noise word through R+8 is jointly
uniform, independent of all bank-complement variables, including the input,
old apparatus seeds, informative deadline outputs, and the clean q8 endpoint.
The result holds before conditioning on either success or failure, and hence
on every nonzero-probability informative-record branch.

This resolves the W-background question for the seven old public ports and
the stated endpoint. It does not establish independence of an entire outgoing
two-slice neighborhood, close a reusable interface, or construct the required
5:3:2 post-Y reset. The distinction matters because the next native operation
reads a neighborhood and an old local slice, rather than only q8.

## Fixed dynamics, ports and bank

The native update is

    U_(t+1)(v) = U_(t-1)(v) XOR H(XOR_(w~v) U_t(w)),
    H(A,B,D) = (B,D,A XOR B D).

H permutes the eight triples. Keep T=185, P=12*840^185, S=T+P,
d=68, R=S+d and L=R+8. The seven public ports and first informative deadlines
are, in same-tick order:

| i | Port p_i | Deadline a_i |
| --- | --- | --- |
| 0 | (0,T,0) | T |
| 1 | (0,0,-8T) | T |
| 2 | (T,P,0) | S |
| 3 | (-T,P,0) | S |
| 4 | (4T,P,0) | S |
| 5 | (0,S,0) | S |
| 6 | (12R,0,0) | R |

Use the inherited torus side 64R+64T+1. Since L<=2R, it is sufficiently
large that all the causal distances and axial paths used here have no
wrap-around shortcut; the proof uses the corresponding integer coordinates.

Their full raw triples are exposed at every tick through L under the fixed
access convention. Their prefixes before a_i are the inherited blanks;
at a_i the original informative records are retained, including both heralds
and every failure combination. For each integer a_i<t<=L reserve one initial
current triple at

    f_0(t) = (0,T-t,0),
    f_1(t) = (0,0,-8T-t),
    f_i(t) = p_i + t e_y,  i=2,3,4,5,
    f_6(t) = (12R-t,0,0).

Every one of these triples is independent and uniform conditional on the
complementary initial configuration and readiness. They are present initially;
none is inserted during evolution. The bank contains 2P+6d+56 triples, or
6P+18d+168 bits. The post-R extension contributes 168 bits, of which 21 extend
the prior R+7 window. This states the required supplied resource, not its
physical derivation or a newly adopted premise.

The W route fixes h=(0,-76,76), W=111; its other added sources are
Q=(0,S,S+136), C=(0,S,S+150), and G=(0,S,S+152). G has payload 011 for u=0
and 101 for u=1. The endpoint is q8=(0,S,76) at L. The current ready ball is
B_L(q8), with previous ready ball B_(L-1)(q8), preserving the named source
exceptions and inherited preparations.

## Actual geometry and unchanged informative records

Every bank block lies at axial distance t from its own port. It reaches no
other public port before t. The only equal-time cross-edges are 2 to 5 and
3 to 5; both respect the table's ordering. All other cross-arrivals are later
and therefore contribute only already-earlier bank variables.

The bank families are pairwise disjoint. In particular the two collinear
Y-axis rays do not overlap: f_0 lies at negative y, whereas f_5 has y>2S.
The remote herald ray has x>=11R-8, separate from old-port families and the
herald's x>=12R source program. None equals W, Q, C or G. The other encoded
sources lie in their inherited ready cones, which all bank coordinates avoid.
The checker tests every family/cone inequality on each exact piecewise-affine
segment, not just on an arbitrary sample of the enormous interval.

Useful exact q8 slacks are

    distance(f_i(t),q8)-L = t-a_i,              i=0,2,3,5,
    distance(f_1(t),q8)-L = t+8T,
    distance(f_4(t),q8)-L = t+2T-P,
    distance(f_6(t),q8)-L = 12R-t.

All are strictly positive over their stated intervals. Thus neither the
added current pins nor the previous pins consume any bank coordinate, and
q8 at L depends only on the complement. The same check covers the inherited
ready cones and the earlier outward ready balls.

W's distance to every old public port exceeds its informative deadline,
so the inherited blank prefixes and deadline records are unchanged. W can
arrive later during a noise stream; that changes its background, which the
following proof explicitly allows. The Q/C/G sources are also excluded from
the earlier informative-record cones by their already checked source geometry.
The argument does not require their later backgrounds to remain unchanged.

## Joint chronological permutation proof

Let C denote every initial variable except the reserved bank, including any
correlations among old seeds, source payloads, input and readiness. Fix C.
Order bank/output blocks by increasing t and then by increasing port index.
No later block can reach an earlier output. At an equal time, the only cross
edges have the direction already given above.

Consider one block f_i(t). Its path of length t to p_i is the unique straight
axial path. At each step along it, only the immediately preceding path vertex
can depend on this block: any other neighbor has insufficient time for the
required displacement, and the old-local slice is two ticks too early.
Consequently that step is an XOR translation, followed by H, followed by an
XOR translation, as a function of the new triple. Each is a permutation.
This statement permits arbitrary fixed dense background, including all
W-dependent changes and all previously conditioned frontier variables.

Each diagonal output block is therefore a permutation of its own input
triple for every fixed earlier block and C. Chronological inversion recovers
one bank triple at a time from the raw output word. The whole bank-to-noise
map is bijective. If N is the concatenation of all post-deadline raw noise
triples, then for every admissible C=c,

    Pr(N=n | C=c) = 8^(-(2P+6d+56)).

The informative deadline record D, both flags, and q8 at L are functions of C.
Averaging the last identity over any chosen complement distribution gives
joint independence of N and those variables; conditioning on a nonzero-mass
value of D or either flag preserves it. No failures are removed, and no
assumption of separate marginal independence replaces this joint argument.
If a designated clean Y endpoint is additionally read, that endpoint is also
a function of C; the same conditional statement applies to that record.

This proof establishes the noise refinement directly from the native local
rule and geometry. The predecessor's informative deadline/transport law is
still inherited; this calculation does not independently reconstruct its
astronomical transport endpoint or the calibrated input distribution.

## What follows for resources, and what does not

Existing u is an already-used seed. Heralding and the Y outcome can bias or
reveal it. The conclusion is only that adding N causes no further posterior
update beyond the informative record D:

    Pr(C in A | D,N) = Pr(C in A | D)

for measurable events A and positive conditioning events. It does not say
that u is a fresh fair resource after measurement.

For a prospective resource A that is initially independent of the old
variables and informative record, remains free under readiness, and is part
of the bank complement, N cannot destroy that independence. Such a resource
retains its stipulated law conditional on D,N and prior heralds. Its actual
coordinates, independence and non-use by D must still be verified for the
next sampler; this report supplies no unspecified fresh resource.

The proof's endpoint exclusion does not cover a whole subsequent boundary.
For example M1=(0,-1,0) is an old bank coordinate, with its first own-port
record at T+1, and its distance to q7=(0,S,75) equals L. Thus geometric
exclusion of old bank information already fails for that neighbor's current
slice at L. This is not an actual dependence witness: the isolated M1
first-front multinomial coefficient cancels since (S+1) AND 75 is nonzero.
A coupled-boundary calculation is required. Full boundary independence is
neither asserted nor inferred from the q8 law.

## Exact controls and replay

`checks.py` is self-contained and uses Python integer arithmetic. It checks
actual astronomical-parameter geometry by complete piecewise-affine
breakpoint analysis, including all ready-cone exclusions and the exact edge
set. Independent direct evaluation of the nonlinear native update verifies
all eight possible new triples in 28 dense-background axial cases. It also
enumerates 64 assignments in each of two same-tick two-port blocks, retaining
the real forward cross-arrival and checking a whole-block bijection.

The same two-port computation detects both negative controls: pinning one
reserved triple (a readiness overlap) and assigning the same triple to both
positions (a shared resource). Each has at most eight attainable output
pairs instead of 64. These countercontrols demonstrate why the independent,
unpinned bank hypothesis cannot be omitted.

Run `python3 checks.py` and `python3 -O checks.py`; both outputs must equal
`results.json` byte for byte. `SHA256SUMS` covers the delivered files. The
small retained source excerpts identify the original access/bank formula;
no external file or earlier scratchpad is needed to replay these controls.
The short-distance recursion tests the local proof mechanism, while the
all-index written proof and exact actual geometry establish the stated
conditional extension. No finite test is represented as a simulation of
all L native ticks.
