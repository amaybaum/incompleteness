# Independent review of v2 and the native history sidecar

24 October 2026. Reviewer thread of the authorized parallel native-Y continuation.
Read-only on prior artifacts and the repository; files written only in this review
folder. No premise adoption or certification. Broader transport-proof review stays
open.

## Verdict

**ACCEPT within scope** the two total reversible interface maps and the v2
obstruction for the relaxed twenty-entry boundary-control family. An independent
implementation derives the reported full output formula and the stronger
pointwise invariant `y=1 => A=1 and B XOR D=x`.

**ACCEPT within scope** the newly found native history sidecar: at relative site
`s=(0,-1,2)` and tick `R+1`, its full triple is `(0,1 XOR y,x)`. It has a blank
prefix through R under the retained ready-cone model. This locates an actual
native x register near the endpoint; it does not yet implement the normalization
gate or make an earlier-time register a freely accessible simultaneous control.

No blocker was found in these narrowly stated results. They are not a native Y
reset, a complete composition proof, or a closure of the general transport audit.

## 1. Independent check method and limits

`checks.py` imports no author code and reads no author data. It uses:

- a literal eight-element H permutation table with a different scalar encoding;
- a separately written near-front recurrence implementation and explicit orbit
  closure, including the phase;
- 560 comparisons to memoized direct three-dimensional native recursion;
- a popcount/factorial-valuation test for multinomial parity;
- a memoized backward polynomial evaluation of the last native stencil, rather
  than the author's forward shrinking-ball or packed truth-table loop;
- variable names tied to geometric sites, with no author source-index ordering;
- a separate set-based Boolean-polynomial representation.

The shared mathematical starting point remains the previously accepted
single-pulse recurrence and original source reduction. The reviewer checked the
local recurrence against the native stencil and direct tests, but did not rerun
the original compiler, all 1,479 source entries, reservoir independence proof,
or every baseline artifact. No claim to replace that wider review is made.

The actual pulse periods are 720 and 84; the huge R has residues 253 and 1. These
are exact finite-state evaluations, not a simulation of the astronomical number
of physical ticks.

## 2. Interface maps

The reported maps F and G and their explicit inverses are permutations on all
sixteen bit strings. On the native input they have the claimed outputs:

    F(y,y,1 XOR xy,0)=(0,0,y,xy),
    G(x,y,y,1 XOR xy)=(x,0,0,y).

Recycling F's auxiliary bit by XOR with xy is valid when x and y remain retained
physical controls. It does not erase unknown information from the global state.
The claim is only logical reversibility; public availability of a historical
record by itself does not implement native storage or control.

## 3. Scope of the twenty-entry relaxation

A new source `(a,b,z)`, z in {1,2}, on the radius-(R+2) boundary about q2=(0,0,2)
satisfies `|a|+|b|=R+z`. Its distance to qY is `R+2z`, and to the upper pulse
`(0,0,R)` is 2R. Thus it neither changes qY at R nor meets the upper pulse before
R. Before the collision all relevant lower first arrivals rotate the same pure
field, so their mutual superposition at first arrival is valid.

For a site v in the radius-two R-2 slice, triangle inequality gives
`dist(source,v)>=R`, excluding any new contribution. For the radius-three R-1
slice, arrival requires equality in both triangle bounds: v lies three steps
along a shortest path from q2 toward the source. Since source z is 1 or 2, the
only possible vertical coordinates are v_z=1 or 2. Hence the support is contained
in `z=1, |a|+|b|=2` or `z=2, |a|+|b|=3`, exactly the claimed twenty entries.
At the actual phase R-1, initial B pulses still occupy B.

This proves containment for every source position in the stated planes; it is
not inferred from a finite scan. The independent checker additionally enumerates
2,640 complete source positions for modest radii as a diagnostic of this geometric
argument. Allowing all twenty entries independently is a safe relaxation for a
negative result; it requires no proof that all settings are compatible with the
full old apparatus.

## 4. Exact polynomial and obstruction

Define k as the XOR of the four axial controls on z=1, and l as the XOR of the
twelve controls on z=2. The independent stencil yields

    A=y,
    B=y XOR uk XOR l,
    D=1 XOR xy XOR u(1 XOR x)k XOR yl,
    y=x XOR u.

All old selector-mask variables cancel. Substitution `u=1 XOR x` gives
`A=1` and `B XOR D=x`. This is pointwise in the controls, so history-dependent
or randomized settings do not remove the distinction between x histories at
y=1. No Y-only full-triple encoding exists in this class. This includes the
suggested canonical and fixed-extra-field codes.

It remains permissible for a later instrument to consume y while carrying x
metadata: x was already public. The obstruction does not make that metadata a
privacy leak and does not exclude the direct-reset avenue.

## 5. Native history sidecar

The same independent stencil gives at s=(0,-1,2), tick R+1:

    U_(R+1)(s)=(0,1 XOR y,x).

Every original lower source is at least R+1 away. The upper source has distance
R-1, but its transverse first-arrival value there is zero at the actual phase;
the R slice is zero by parity. Earlier slices are outside its light cone.
Consequently this entire sidecar prefix through R is blank, within the inherited
ready-cone assumptions. Its later appearance need not reveal the future Y sample
before the first instrument's R boundary.

A diagnostic replacement of qY's D field by p at tick R does not affect the
sidecar at R+1: their distance is three. The sidecar still contains the native
`1 XOR y`, not `1 XOR p`. This is not a diagnostic operand route for its B field.
Its D field is nevertheless the genuine earlier x, and q2's A at R+2 remains p.
Both facts are verified symbolically for every selector-mask value.

The sidecar occupies the earlier slice of the phase state at R+2, at a neighboring
spatial site. The native update does not permit arbitrary reads or gates between
such registers. A construction using it must prove the actual stencil, timing,
side fields, full prefix and any additional initial resources.

## 6. Shared acceptance conditions for the four avenues

A combined handoff should state separately which of these are met:

1. The actual incoming operand is used; diagnostic replacements are tests, not
   native operations or a license to reload the input.
2. Every clean cell, prior correlation and source is specified at the common
   initial time. A conditional clean-input gadget is not automatically embedded
   in the actual populated q2 neighborhood.
3. Retained information remains in the reversible global phase state. Known
   public history is distinguished from secret input or future reset samples.
4. Prefix records are checked at their declared times, not only terminal bits.
   A new readable site cannot silently release u before the first boundary.
5. New sources and readiness pins preserve existing fair frontier resources;
   enlarged observation windows need a joint rather than per-port proof.
6. A reset claim includes fresh conditional resources, native herald behavior,
   explicit failures, the full outgoing carrier, and history-conditioned law.
7. Terminal X alone is insufficient to validate 5:3:2 Y calibration. Retain the
   terminal R diagnostic and full outgoing-distribution test.
8. Cross-avenue integration requires one compatible initial prior, geometry and
   timeline. Algebraic identities from separate apparatuses cannot be composed
   by assumption.

## Replay

    python3 parallel_v3/review/checks.py
    python3 -O parallel_v3/review/checks.py
    python3 parallel_v3/review/sidecar_check.py
    python3 -O parallel_v3/review/sidecar_check.py

Both scripts use the standard library only, write no files and make no network
calls. `sidecar_check.py` imports only this review's own checker. Normal and
optimized outputs are retained alongside the scripts. INPUT-HASHES.json records
reviewed author bytes; these hashes do not assert independent verification of
every statement in those inputs.

## 7. Additional review: auxiliary extractor and attempted splice

**ACCEPT conditional native gadget.** Independently computed three-dimensional
causal recursion confirms the five-tick gadget with Q at the origin and fixed
current sources `eB` at `(0,1,-1)`, `111` at `(1,1,-2)`, and `eB` at `(8,2,0)`.
The full output at `(3,2,0)`, tick 5 is `(0,A,0)` for all eight arbitrary
Q=(A,B,D), and the target prefix is blank. Thus this gadget extracts actual A,
not only a B field that agrees with A on the original three-code domain.
All sources lie on the target's radius-five first-arrival boundary.

The author additionally checks a complete periodic lattice and inverse; the
reviewer's own checker verifies the finite causal law independently rather than
relying on that test. The native update is globally invertible, so extraction
into one cell does not erase the remaining input information globally.

**Actual splice remains blocked.** The clean previous slice required by this
gadget is not supplied by translating it to q2 at R+2. At q2+e_x, time R+1, the
actual whole triple is `(0,1 XOR u XOR mY,mY)`, generally nonzero. Independent
symbolic dynamics verifies this value. Independently inserting old value eB at
the corresponding required-blank site changes the gadget output for Q=001 from
000 to 010. This is a genuine dirty-socket counterexample. It does not rule out
an adjusted gadget that explicitly accounts for the populated phase.

## 8. Additional review: direct-reset building block and information law

**ACCEPT conditional native mixer.** For two initially separated sources Q and
`(a,0,0)` at axial separation 2L and a receiver midway, first arrival at time L
with L a multiple of 12 gives

    H(H^-1(Q) XOR H^-1(a,0,0)) = (A XOR a,B,D XOR aB).

The two-ended arrangement at receivers ±L with seeds at ±2L has no cross-seed
arrival before L. Independent direct three-dimensional recursion checks both
full output triples and their blank prefixes for all 32 Q/a/b choices at L=12.
The identity supplies the general first-arrival case for L=0 mod12; the clean
cones and localized initial input remain explicit hypotheses.

**ACCEPT only as a candidate tagged information contract.** A separate reviewer
checker enumerates all four x,y histories and all 64 second-stage seed states,
then all 2,048 composed seed states for each earlier x. It reproduces the 5:3:2
conditional plane weights, success 5/16, failure 11/16, and composed success
25/256 with every failed branch retained. These are abstract supplied-resource
composition calculations, not an integrated native X→Y run.

**Unchanged strict common raw-carrier criterion is not satisfied.** On y=1,
whole raw supports for x=0 and x=1 are disjoint, so conditional TV is one. The
encoded target signs have the same law, but the raw carrier still encodes the
old history. On each complete X/R output cell at y=1, `A XOR D=x`. No new secret
is leaked by this old public tag, but a history-independent common raw encoding
has not been achieved. The parent's `integration/REPORT.md` explicitly preserves
this failure and adopts no encoding relaxation; that wording is consistent.

The new herald compiler and its full source-layout realization are outside the
review completed in this section unless a later addendum names their exact
reviewed scope. No compiler acceptance should be inferred from the mixer or
probability-law checks.

## 9. Additional review: third outward step

**ACCEPT local actual-parameter formula under the inherited source reduction and
specified extended ready cone.** The reviewer wrote a separate signed-transverse
strip implementation. It stores all signed (a,b) positions instead of identifying
symmetric representatives and uses an increasing-lag, increasing-lookahead sweep
instead of the author's recursive lower-strip advance.

For `V_n(l,a,b)=U_(n+l)(a,b,n)`, direct substitution gives

    V_n(l)=V_n(l-2) XOR H(V_(n-1)(l) XOR V_(n+1)(l-2)
                                  XOR four transverse V_n(l-1) terms).

The future lower-lag terms are determined in earlier lag stages. The retained
region `l+|a|+|b|<=6` is closed under these dependencies: transverse motion changes
lag by -1 and distance by at most +1; future lookahead consumes two units of
lag budget. Zero values outside the first-arrival cone or wrong parity are
explicit. This yields an exact finite recurrence, not a large-n extrapolation.

The independent strip agrees with 792 direct-native values at small n, reproduces
full orbit returns of 3600 and 2940 for the two upper pulses, and obtains actual
R remainder 253 in each. A separate polynomial evaluation of the four native
updates then reproduces, for every selector-mask assignment,

    U_(R+3)(qY+3e_z)=(u,xu,u).

With the diagnostic replacement qY.D=p at time R, it also reproduces

    (u OR (x XOR p), x XOR p XOR up XOR uxp, u(x XOR p)).

The native triple is not itself a Y-only carrier: when u=0, both x values give
000 despite different y=x XOR u. This third outward step does not retain a raw
Y operand by itself. History-assisted decoding remains a separate construction.
The review verifies the new strip and local formula, not an independent audit
of every global source/readiness/frontier extension used to embed it.

## Additional replay commands

    python3 parallel_v3/review/gadgets_check.py
    python3 -O parallel_v3/review/gadgets_check.py
    python3 parallel_v3/review/contract_check.py
    python3 -O parallel_v3/review/contract_check.py
    python3 parallel_v3/review/geometry_check.py
    python3 -O parallel_v3/review/geometry_check.py

All scripts are standalone within this review folder and standard-library-only.
Imports between the review scripts print earlier checks again; this is intentional
and is not counted as additional independent evidence. Retained outputs identify
exactly which checks ran.

## 10. Addendum: source-defined native herald and standalone geometry

**ACCEPT the concrete source-defined herald under its stated prepared-cone
hypotheses.** `herald_check.py` does not import the compiler and does not execute
or compare against the compiled register word. It reads the actual 7,832 affine
source entries and independently checks their wing positions, fields, source
uniqueness, six-bit affine masks, and rank-five seed dependence.

For tick k at axis position x=L-k-1, a source on one wing contributes from
initial index x+j precisely when the binomial coefficient C(k,j) is odd. Lucas
parity means j ranges over the bit subsets of k. The reviewer directly XORs
those source masks, rotates their pure field by H^k, and applies the actual H
axis update. This uses shortest-path sums rather than the author's successive
Pascal-row recurrence. The source-wing geometry keeps differently occupied
fields separated until the axis: opposing y wings meet only on y=0, and the z
wing meets the y wings only on the axis. All are first arrivals, so the old local
and unarrived terms vanish as required.

The full 2,700-step calculation on all 32 seed assignments produces exactly
`(0,G,0)` with acceptance counts 5,3,2,0 and success 10/32. The independent checker
also verifies every listed source against all five proposed receivers: intended
sources are on the appropriate radius-L boundary, every foreign source is
outside, and an arbitrary previous input at the origin cannot reach any endpoint.
The pure-D Z field returns unchanged since L is a multiple of 12. Blank prefixes
follow from the stated initially empty interior cones and boundary-only sources.

This verifies the concrete herald/source geometry without requiring trust in
the compiler's implementation. It is not a proof of that compiler for arbitrary
programs, nor a complete simulation of the large three-dimensional lattice.
Most importantly, the geometry belongs to the standalone apparatus with a
localized initial Q; it does not supply the late-q2 socket or old-frontier
compatibility required by the actual continuation.

    python3 parallel_v3/review/herald_check.py
    python3 -O parallel_v3/review/herald_check.py

This final checker reads the sibling `direct_reset/herald.json`; the other five
review scripts are self-contained within the review folder. None writes files
or makes network calls. Both normal and optimized outputs are retained.

## Final review matrix

| Claim | Review result | Explicit boundary |
|---|---|---|
| v2 reversible interface F/G | ACCEPT | Abstract gates/control access |
| v2 twenty-entry obstruction | ACCEPT | Stated plane-source family only |
| Native x sidecar at R+1 | ACCEPT | Earlier-slice value, no gate integration |
| Five-tick A extractor | ACCEPT conditional native gadget | Clean initial socket; actual splice counterexample |
| Direct native mixers/fanout | ACCEPT conditional native gadget | Standalone first-arrival cones |
| Concrete 2700-tick herald/source geometry | ACCEPT conditional native construction | Specific source list, no general compiler certification |
| Tagged full-carrier law and explicit failures | ACCEPT candidate information contract | Not unchanged common raw-carrier criterion |
| Strict common raw-carrier independence | FAIL for proposed tagged candidate | Conditional TV1 across x at y=1 |
| Third outward actual-parameter formula | ACCEPT local recurrence calculation | Inherited source reduction/extended cone assumed |
| Complete native reusable X→Y reset | OPEN | Actual two-slice integration, common carrier and joint records |
| General transport-proof audit | OPEN | Not replaced by these scoped checks |
