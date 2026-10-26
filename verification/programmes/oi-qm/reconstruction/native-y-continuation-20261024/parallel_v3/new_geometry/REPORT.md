# Avenue 4: an exact third outward step and a bounded geometry census

24 October 2026. Repository-read-only research. Author result for independent
review, not a certification or a universal impossibility result. Files in this
folder are the only files modified by this avenue.

## Outcome

Extending the same compatible initial outward workspace by one more cell gives
an exact actual-scale endpoint at q3=qY+3e_z, tick R+3:

    U_(R+3)(q3)=(u,xu,u),   y=x XOR u.

It is not a clean Y socket, and it does not retain the actual incoming operand
as a raw field under the stronger diagnostic intervention. Merely taking the
next straight outward step therefore does not solve the interface problem.

The proof extends the previously reviewed bounded-lag calculation. A new
13-triple finite recurrence has pulse-orbit periods 3600 for u=0 and 2940 for
u=1. At the actual astronomical deadline R, both remainders are 253. There is
no extrapolation from a small torus or from R modulo 12.

A bounded census over the entire shrinking diamond used in the proof finds
only the already known qY.D and q2.A as raw p fields (or complements), across
all input and selector-mask assignments. This is a census of 96 site-times,
not a no-go for other positions, later times, new controls, or larger gadgets.

## 1. General radial-strip recurrence

For a lone initial pulse Q at the origin and zero previous slice, set

    W_n(ell,a,b)=U_(n+ell)(a,b,n).

By cubic reflection/swap symmetry use a>=b>=0. For the present application keep
exactly the indices

    a+b <= ell,  a+b+ell <= 6,  ell-a-b even.

There are thirteen triples. A value with wrong parity or outside the light cone
is zero. Substitution in the unchanged six-neighbour native rule gives, for
n>=1,

    W_n(ell,a,b) = W_n(ell-2,a,b) XOR H(
        W_(n-1)(ell,a,b) XOR W_(n+1)(ell-2,a,b)
        XOR W_n(ell-1,a-1,b) XOR W_n(ell-1,a+1,b)
        XOR W_n(ell-1,a,b-1) XOR W_n(ell-1,a,b+1)).

Negative transverse indices are reflected. Equal reflected neighbours cancel;
none is discarded individually. The initial n=0 strip is computed directly at
ticks0..6, not guessed from an asymptotic recurrence.

To advance from n to n+1, compute increasing ell. The apparently future strip
at n+2 has ell reduced by two; it is already determined by applying the same
advance to the lower layers just computed. The index set is closed under these
dependencies. This is a finite triangular algorithm, not an implicit equation.

It is also a bijection on its entire 39-bit strip-state space. At each index,
all dependencies except the old same-index triple are fixed by lower layers,
and H is a permutation. The inverse recovers that old triple by applying
H^-1(A,B,D)=(D XOR AB,A,B) and XORing the other terms. The executable inverse
checks arbitrary strip states, not only physical pulse orbits.

Enumeration from Q=(0,0,1) returns for the first time after3600 steps; from
Q=(1,0,1) after2940. The listed states are distinct and the final step returns
to the first. Thus the initial orbit has no transient and lookup by remainder
is exact. This does not assert these periods for all strip states.

## 2. Actual geometry and initial resources

Keep T=185, P=12*840^185, S=T+P, d=68, R=S+d and the native update unchanged.
Coordinates below are relative to qY unless explicitly stated.

Add the initial current-slice ready ball of radius R+3 around q3=(0,0,3), and
the previous-slice ball of radius R+2. Preserve every existing source and old
ready constraint. This extends the accepted depth-two ready region. These are
initial conditions; there is no mid-run cleaning or new randomness insertion.

The four relevant lower B-field sources are

    (0,-S,-d): x
    (0, S,-d): mY XOR mR
    (T, P,-d): mY
    (-T,P,-d): mR.

Each is at distance R+3 from q3 and distance2R from the upper pulse at(0,0,R).
The frozen list of1,479 original sources again has only the unknown origin
input on the new receiver's boundary. Other old sources are outside. The old
previous-slice input, opposite reset pulse and remote herald/Z source blocks
remain excluded.

The earlier public frontier families remain outside the enlarged ready region.
For example, in absolute coordinates the X selector frontier(0,2S+k,0) has
distance R+3+k from q3, for every k>=1. The other inherited families have the
same or a positive larger slack, as in the depth-two proof. The checks evaluate
the explicit formulas at representative positive indices; the general claim
uses those linear inequalities, not sampling alone.

At slice R-1 the required backward ball has radius4; at R-2 it has radius3.
Every lower contribution there is zero or exactly on its first-arrival front:
triangle inequality gives distance at least the slice tick. Lower/upper source
separation2R excludes interaction before R. Lower contributions therefore use
exact multinomial no-carry parity and the single-field rotation. Upper-pulse
values are exactly the thirteen strip entries above, at appropriate n.
Four native updates on shrinking balls of radii3,2,1,0 now compute the endpoint.

The exact added pin set is the new current/previous ball union minus the old
prepared union, retaining all source exceptions. No optimized or numeric global
readiness cost is claimed. If the seven old public ports remain exposed from
R+2 through R+3, the inherited finite-window extension requires another21
initially independent fair bits (63 beyond the window ending atR). This avenue
uses the inherited joint-frontier theorem; it does not re-prove that theorem.

## 3. Complete diagnostic and native laws

In the diagnostic only, replace qY.D at tickR by p, retaining qY.A=x and qY.B=1.
For every x,u,mY,mR,p assignment, the full new endpoint is

    (u OR (x XOR p),
     x XOR p XOR up XOR uxp,
     u(x XOR p)).

The masks cancel. The ordinary native run uses p=y=x XOR u, yielding
`(u,xu,u)`. The diagnostic replacement is never applied in native evolution.
The entire retained second-step q2 result is unchanged.

For example, native histories(x,u)=(0,0) and(1,1) both have y=0 but give q3 codes
000 and111. Thus q3 is not a Y-only encoding. Its A field equalsu natively;
x XOR A agrees withy on that native domain, but that history-dependent formula
does not recover arbitrary diagnosticp. It cannot be counted as a new raw-Y
transfer merely because the unaltered truth table agrees.

This lack of a clean socket is not a terminal privacy failure. Given already
publicx and the designated Y outcome y, u=x XOR y and the whole q3 triple is
determined. It does not disclose an additional hidden variable at that boundary.

The earlier prefix is still informative. q3 first receives the upper pulse at
R-3, with triple H^(R-3)(u,0,1)=(u,1,u). Thus exposing q3 from the start leaks
the future sample before the earlier X-instrument boundary. Keep it private
under the existing supplied delayed-access convention. With the inherited5/16
success probability and fair conditionalu, the corresponding leak witness has
weight5/32 including failure. There is no native shutter or clock here.

No new reset or success event has been built; inherited failures remain failures.
Nothing here licenses a second successful carrier or changes the old herald law.

## 4. Bounded search and checks

The shrinking diamond has63+25+7+1=96 site-times at ticksR throughR+3. Across
all32 x,u,mY,mR,p assignments, search all three fields and their complements.
Only these are uniformlyp:

| Relative tick | Relative position | Field | Complement |
|---|---|---|---|
| 0 | (0,0,0) | D | no |
| 2 | (0,0,2) | A | no |

Neither full triple is a Y-only socket. The census examines576 field/complement
candidates. It does not search arbitrary local decoders, other initial controls,
or the entire forward cone.

`checks.py` also verifies:

- 936 direct three-dimensional recurrence comparisons: all8 pulse triples,
  n=0..8, all13 strip entries;
- 512 inverse identities on256 arbitrary finite strip states;
- minimal period certificates3600/2940 and exact giant remainders;
- all1,479 source positions and the relevant exclusions;
- all32 complete diagnostic endpoints and the unchanged q2 endpoint;
- all16 native input/mask endpoints and the early prefix;
- counterexamples to interpreting q3 as rawp or as cleanY.

Normal and Python -O runs have identical output, and all acceptance checks use
explicit exceptions. This avenue derives the radial-strip recurrence separately
from the old special formulas. Its local endpoint assembly and the copied
first-arrival helpers reuse the accepted proof structure; it is not an
independent audit of every inherited transport or access claim.

## 5. Integration consequence and next work

The longer straight-outward path does not supply the needed interface. The new
strip recurrence is reusable for bounded extra-lag calculations and provides a
way to test further actual-scale geometries without relying on small phases.
It can be enlarged with a larger closed index set, but orbit periods and work
must be checked anew; no unrestricted-depth result follows.

Other tracks' history sidecar or auxiliary gadgets may still work. In particular,
this does not evaluate the whole future causal cone of the sidecar: destinations
closer to the lower sources may require lower-source lag corrections, whereas
this straight-outward proof needs only their first-arrival fronts. A cold
isolated-gadget premise cannot be inserted into that cone without proof.

No new physical premise, normalization, native reset, or universal obstruction
is claimed. Exact-QM reconstruction and finite-precision OI retain their separate
status. Broader transport-proof review remains open.

## Replay and provenance

Run from any directory:

    python3 /path/to/new_geometry/checks.py
    python3 -O /path/to/new_geometry/checks.py

The checker needs only the Python standard library and files in this folder.
It prints to stdout, makes no network requests, and does not modify files.
`inherited_core.py` and SOURCE-GEOMETRY.json were copied byte-for-byte from the
accepted depth-two handoff. PROVENANCE.json gives their digests. Development
included a discarded over-large strip search and a fixed index-budget bug;
the final recurrence was checked against direct dynamics after that correction.
The discarded exploratory script is not part of the replay set.
