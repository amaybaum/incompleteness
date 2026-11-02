# Actual-sign autonomous feedback: a masked two-tick echo

Research calculation from `edf8aa44e3fad2067f15b3af0cb897b571881623`.
The tested construction is two ordinary native ticks from the actual
q10.A=s phase, with the existing v14 fewest-seed preparation unchanged.
The decision rule is: a clean raw sign echo requires the returned current
A field to equal s for every admissible complement value. All fields and
terminal microscopic branches remain in the calculation. No read, write,
controller source, preparation change or later transport route is added.

**Result: MASKED_RAW_ECHO.** There is an exact native return of the sign
plus a12-bit neighboring mask. A free original-time triple makes the whole
returned current triple uniform under the stated independent-uniform-key
prior. This rejects the clean raw echo construction. It does not exclude
an encoded or distributed gate, or establish a reusable measurement.

## Exact native stencil and the actual sign

Set t=L+1 and q=q10=(0,S,78). Write C(v)=U_t(v), P(v)=U_(t-1)(v), and
let E be the six signed coordinate unit vectors. Retain the whole rule

    N(v)=P(v) XOR h(XOR_(e in E) C(v+e)),
    R(q)=C(q) XOR h(XOR_(e in E) N(q+e)),
    h(A,B,D)=(B,D,A XOR BD).

N is the actual first intermediate slice and R(q)=U_(L+3)(q). For the A
field, h(x).A=x.B and h(x).B=x.D imply

    R(q).A = C(q).A
       XOR XOR_(e in E) P(q+e).B
       XOR XOR_(e in E) C(q+2e).D.

In the double neighbor sum, C(q).D occurs six times and each off-axis
distance-two site occurs twice; these cancel over XOR. Each of the six
axial distance-two sites occurs once. This proves the identity for arbitrary
dirty fields, with the old-local term retained and without linearizing h.

For the retained law E_source=(1,1 XOR mY,1),
N_source=(mY,1,1 XOR mY), the actual table gives C(q).A=s on all48 accepted
old sign/context rows. Thus the returned A is s XOR M, where M is the
displayed12-bit parity. The12 bits need not be independent. This is an
autonomous microscopic feedback path, but a masked return is not a clean
operand delivered to an available gate.

## A free original cell certifies the mask

Fix T=185, P0=12*840^185, S=P0+185, R_time=S+68,
L=R_time+9, and the unchanged torus. To avoid confusing the prior slice
P(v) with the enormous programme constant, that constant is P0 here.
Take the original-time **current-slice** triple

    kappa = U_0(k),  k=(0,S+L+3,78).

The existing geometry gives:

| Check | Exact result |
| --- | --- |
| Distance k to q | L+3 |
| Minimum distance minus declared ready radius | 2 |
| Earliest arrival at any of the eight public ports | L+81, at port5 |
| Distance to q9 minus the stipulated V-read time L+2 | 2 |
| Old source inventory | k is absent from all1479 positions |
| Added E/N, selector/reset sources and public bank lines | k matches none |

At time t=L+1, k can affect exactly one of the six current outer sites
in M: q+2e_y. Its distance to that site is L+1. It affects none of the
other five outer sites, none of the six previous-neighbor fields at time
L, and neither q10 nor q8 at time L+1. Old q9 and the stipulated V read
are also unaffected. These are finite-speed exclusions; the checker uses
the primary route geometry and the retained inventory. Completeness of
that preparation/readiness/access inventory remains an explicit hypothesis.

The unique straight first-arrival path to q+2e_y makes its whole triple a
permutation of kappa for every fixed complementary original configuration.
At each step, the old-local and other-neighbor terms are source-independent,
so the response is a composition of XOR translations and h. Its D field
therefore takes each bit four times as kappa ranges over all eight values.
The mask parity, and hence the returned A, cannot be constant across this
free triple. This already refutes a pointwise clean echo under an arbitrary
free complement; no probability assumption is needed for that exclusion.

The same unique-axis argument at the later endpoint q and time L+3 gives
R(q)=phi_c(kappa), where phi_c permutes all eight triples. If the inherited
prior satisfies Pr(kappa=k0 | C0=c)=1/8, with C0 collecting **all** other
original variables, then R(q) is uniform conditional on C0. Uniformity is
not inferred from a late-slice marginal. Pinning this key would change the
preparation; it is not adopted as an actuator repair.

## Joint state, records and failures

The local outgoing two-slice pair is (R(q),N(q)). N(q) is independent of
kappa by finite speed. The whole permitted record through prospective
H=L+79 is also kappa-independent: the first port arrival is L+81, and
the stipulated old q9/V reads are too early. Let that record be W=w(C0).
On any positive-mass enabled branch the exact local joint law is

    Law(R(q),N(q) | C0=c) = Uniform(8) x delta_(N_c(q)).

This does not imply the pair is independent of s: its previous field
N_c(q) may carry correlations with s. It proves that the new current
triple adds no information about any C0 operand, including s, even when
earlier records and the previous local slice are retained. It does not
make private q10 a permitted read.

The full outgoing microscopic cut remains G_(L+3)(C0,kappa), with all
neighboring B/D fields, masks and apparatus. On a fixed-c branch with
current outcome r, its conditional value is

    G_(L+3)(c,phi_c^(-1)(r)).

The full cut retains the key by native invertibility. No independence or
reset of that cut follows from the uniform current marginal. No closed
next-stage operational boundary or acceptance flag has been established.

All64 old source rows, including the16 mask01 rows, enter the bounded
microscopic stencil controls. An earlier terminal branch stays terminal:
microscopic evolution is mathematically defined, but no read is attempted
and no carrier is offered. The48/16 row counts and finite dirty fixtures
are not physical success/failure probabilities. Existing other failure
flags remain in W; conditioning is only on positive-mass branches.

## Controls and reproduction

From the continuous-substates directory:

    python3 -I -B native_sign_echo_probe.py
    python3 -I -B -O native_sign_echo_probe.py

Both produce byte-identical structured PASS data and verdict
MASKED_RAW_ECHO:1024 exact two-tick patch worlds,96 accepted-phase dirty
families and32 terminal microscopic families; no new reads or offered
reusable carriers. Each complete output triple runs through all eight
values while the previous local triple stays fixed. The12-bit identity
holds throughout. The actual q10/old-q9 tables and original source inventory
are read in place with their hashes checked. The script imports no earlier
engine. Dirty phase fixtures check the universal stencil algebra; they
are not a replay of the astronomical preparation or its joint carrier law.

Controls include the full native h truth table, a nonvacuous old-local
term comparison, and fixed-key versus variable-key output differences.
Wrong-key-depth, nonlinear-term, old-local-term and table-pin mutations
are rejected normally and with optimization. The arbitrary-background
first-arrival proof and uniform-key hypothesis, rather than finite fixture
extrapolation, support the general conditional statement.

Source anchors under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:
`shared_v12/INTERFACE-CONTRACT.md` (actual rule, resources, failures),
`native_route_v13/checks.py:geometry` (ready/source/bank declarations),
`native_decode_v14/REPORT.md` (actual fewest-seed law),
`native_v11/REPORT.md` (arbitrary-background axial permutation),
`history_v9/REPORT.md` (prior and its joint-state limits), and
`native_vread_v15/REPORT.md` (access and inventory scope).

Independent review is pending. The bounded construction has not supplied
the requested physical actuator. The next useful witness needs an actual
native interaction accepting a specified encoded carrier, with a sourced
way to handle its masks and a boundary a further stage can consume. An
inverse-coordinate definition alone does not implement that interaction.
Track A, manuscripts and prior accepted results are unchanged. No F/E,
special workflow, readiness or merge action is part of this checkpoint.
