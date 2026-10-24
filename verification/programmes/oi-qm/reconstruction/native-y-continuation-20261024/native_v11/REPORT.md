# One-tick native continuation requires an initial boundary contract

Research result on #910's retained preparation at
`71d291297d0a662cbb9377ab48eef7aa4b839e77`. Separate-author review pending.
This probe finds a concrete missing boundary condition for naive one-tick
reuse. It does not construct a native X instrument or exclude a fuller one.

## Result and scope

Keep T=185, P=12*840^185, S=P+185, R=S+68 and L=R+9. The retained success
phase has previous q8=(0,Y,0) at (0,S,76) and current q9=(0,X,Rsign) at
(0,S,77), plus the remote Z and herald fields. Every old source, bank and
ready region is retained. Rsign denotes the carrier sign, distinct from the
time constant R.

The selected phase and the complete permitted public record through L do
not determine the next current q8 or outward q10=(0,S,78) at L+1 when the
outside-ready initial complement is allowed to vary. Two actual
original-time current cells witness this:

| Initial cell | Next target | Own arrival | Distance to q9 | Cross-target arrival |
| --- | --- | --- | --- | --- |
| f8=(-(L+1),S,76) | q8 | L+1 | L+2 | L+3 |
| f10=(-(L+1),S,78) | q10 | L+1 | L+2 | L+3 |

Both cells are outside all 24 declared current ready regions, hence also
outside their smaller previous ready regions. Neither coincides with any
of the 1,479 inherited finite sources, the local W/Q/C/G/J/K sources, any
of the seven old public-bank rays, or the old/new remote source programs.
Every named ready-center and every old/new public receiver is at distance
strictly greater than L. Thus changing either initial triple changes no
permitted earlier public record, terminal flag, selected carrier field or
success/failure mass through L. This includes the new herald at +48L.

The tight old-public-port slacks are L+77 and L+79, at ports3 and5, for
f8 and f10 respectively. These are literal cone exclusions; no noise-bank
compensation is used to conceal an earlier record change. The no-wrap
torus already specified by herald_v10 remains sufficient.

For each fixed choice of all other initial variables, varying the two
current triples gives **all 64 ordered pairs of next q8/q10 triples**,
while retaining the same earlier record and prepared selected phase.
If these two nuisance triples are independent uniform initial resources
conditional on the remaining initial state, the two next cells are jointly
uniform conditional on that remainder and the entire earlier record:

    Pr(U_(L+1)(q8)=v, U_(L+1)(q10)=w | remainder) = 1/64.

They are consequently independent of the earlier X when that is conditioned
on, and neither current triple by itself supplies the required X-eigenstate
carrier. The previous q9 slice still retains X in the full second-order
phase; this result does not show that X has been erased or cannot be reused
with a more complete native interface.

The outside-ready qualification matters. The source preparation specifies
ready balls and bank/source exceptions. The history proof fixes every
initial variable outside its bank as a complement and remains valid for any
complement distribution (history_v9/REPORT.md, “Joint chronological
permutation proof”). The earlier sidecar report explicitly distinguishes
the independent-fair nuisance complement from a modified zero complement.
If a narrower application fixes f8 and f10, for example by a globally sparse
zero prescription, this particular variation is unavailable. Its additional
initial constraint must be retained in the next-stage contract. No result
here contradicts a calculation on that narrower initial family.

## Native proof in arbitrary background

For a source f and target p at axial distance n=L+1, there is one shortest
native path. At step j on that path, the old local term is two ticks too
early to depend on the source triple. Among the six current predecessor
neighbors, only the immediately previous path vertex can depend on it;
the other five have distance j+1 from f but time j-1. The response therefore
has the form

    w -> old_j XOR H(w XOR other_j),

where old_j and other_j are fixed after the other initial variables are
fixed. XOR translations and H are permutations on all eight triples.
Composition proves the exact eight-to-eight response at any finite n,
including n=L+1. It permits dense nonlinear backgrounds and does not use
isolated-pulse superposition or a large-period reduction. Since f8 cannot
reach q10 by L+1, and f10 cannot reach q8, the two response maps are separate.
Their product is the stated 64-to-64 bijection. The argument works for all
earlier success and failure branches because the new sources affect none
of their records before the cut.

## Initial extension and retained bank

A next-stage calculation must either retain these outside-ready degrees of
freedom in its full incoming measure, or specify additional original-time
preparation. To determine both queried cells it suffices to specify current
initial B_(L+1)(q8) union B_(L+1)(q10), and previous initial B_L(q8) union
B_L(q10), preserving existing source and bank exceptions. These cover the
old q9 balls. They are dependencies to specify, not a claim that the actual
next output becomes clean or independent after adding zero pins.

A return-q8 blank extension must not overwrite M1=(0,-1,0), whose distance
to q8 is L, or M2=(0,-2,0), whose distance is L+1. Both are reserved old
noise-bank cells. M1 is in the opposite spacetime component; geometric
inclusion is not an actual influence witness, and no leak is claimed from
an isolated-front calculation. The outward q10 ball excludes M1 and M2,
at distances L+2 and L+3, respectively. This favors checking an explicitly
prepared outward continuation before attempting a return through the used
bank. It supplies no right to erase either bank or splice in late readiness.

## Controls and replay

The first positive-x candidate is rejected: (L+1,S,76) has distance L-478
from old public port4, so it would alter the retained noise history. The
negative-x witnesses above pass all actual geometry checks.

Independent scalar full-three-dimensional recursion checks the axial
response at distances1..6 in three different two-slice backgrounds,
including nonzero nonlinear backgrounds. All 18 families, 504 path/output
comparisons and 3,024 fixed-background comparisons pass. There are 88
nonvacuum responses different from H^n, showing the controls do not silently
assume a blank path. The huge-time conclusion is the written unique-path
proof, not extrapolation from these small checks. Exact geometry checks
cover 2,958 source comparisons, 48 ready exclusions and the complete bank
ray intervals via coordinate inequalities.

Run `python3 checks.py --source-root <retained-native-root>` and compare its
stdout with result.json; repeat with `python3 -O`. Normal and optimized
outputs are byte-identical. PROVENANCE.json pins the immutable inherited
source records. No external validation, Lean certificate, native reset,
unrestricted depth, full A1 equivalence or A2 error guarantee is claimed.
