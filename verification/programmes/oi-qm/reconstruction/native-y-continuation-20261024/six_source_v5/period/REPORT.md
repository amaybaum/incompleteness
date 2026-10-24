# Exact giant-delay reduction for the lower origin/M2 cluster

Author derivation and bounded controls, 24 October 2026. This note scrutinizes
the proposed active-parity preparation in `junction_v4/REPORT.md`. It proves an
exact reduction needed for the six-source calculation; it does not itself
evaluate or certify the six-source endpoint. Repository read-only.

## Main conclusion

The proposed giant-delay shortcut is valid for the lower two-source cluster.
The nonlinear interaction of `(0,x,0)` at the origin with arbitrary `M2` at
`(0,-2,0)` is retained. One may shift the axial y coordinate and time together
by

    P=12*840^185

on the two pre-selector-collision slices required by the target cone. No
small-parameter extrapolation, isolated-pulse superposition, or replacement of
M2 by zero is needed. A global identity exponent of the finite radial-strip
map proves the shift exactly.

The required budget is at most142; the proposed conservative budget144 is
valid, and P is divisible by its proven identity exponent `12*840^144`.
The relevant reduced axial coordinates are positive (at least112), so the
shift stays in the forward region where the strip recurrence applies.

## 1. Geometry and decomposition

Use T=185, P as above, S=T+P, d=68, R=S+68,

    s=(0,S-1,70),   N=S+71=R+3.

To start native evolution at tick S, retain the two slices:

- t=S-1 in the L1 ball of radius72 centered at s;
- t=S-2 in the L1 ball of radius71 centered at s.

The smaller old slice is sufficient because the first next slice at S is
needed only on the radius71 ball. An unnecessarily larger old ball may be
used, but its index budget should be checked separately.

Before S the origin cannot interact with any of the three selector controls:
their source distances from the origin are2S, and from M2 are2S+2. At the
first slice every selector contribution is zero or exactly on its first-arrival
front, because its distance to s is N. On the second slice all three controls
are still absent. Although selector fronts can meet each other elsewhere
before S, within this target cone their contributions remain in the same
single rotating B-field subspace, on which H is linear. Their first-arrival
path-parity contributions can therefore be added at S-1.

The origin/M2 cluster is a different matter. Its sources are separated by two
and interact already at tick1. That cluster must be computed together. The
period argument below applies to that entire nonlinear two-source evolution.
It does not apply independently to each source and then add their answers.

## 2. Closed triangular radial strip

For the two-source cluster alone with zero previous slice, define

    W_n(ell,a,b)=U_(n+ell)(a,n,b),

with a>=b>=0 after transverse reflection and interchange. The cluster is
symmetric in its x and z transverse coordinates; no reflection in the axial y
coordinate is assumed. Both initial sources lie on the y axis at y<=0.
For n>=0, values with ell<a+b or odd ell-a-b vanish by finite speed and parity.

For a chosen even budget L, retain the finite index set

    I_L={(ell,a,b): a>=b>=0, a+b<=ell,
                        ell+a+b<=L, ell-a-b even}.

For n>=1, the full native rule yields

    W_n(ell,a,b)=W_n(ell-2,a,b) XOR H(
       W_(n-1)(ell,a,b) XOR W_(n+1)(ell-2,a,b)
       XOR W_n(ell-1,a-1,b) XOR W_n(ell-1,a+1,b)
       XOR W_n(ell-1,a,b-1) XOR W_n(ell-1,a,b+1)).

Negative transverse indices are reflected. Duplicate reflected neighbours
cancel as an XOR pair. Every nonzero dependency lies within the index budget.
The recurrence is valid irrespective of the nonlinear dipole interaction near
y=-1; that interaction is already encoded in the n=0 initial strip.

To obtain W_(n+1) from W_n, process increasing ell. Each future W_(n+2) term
has layer ell-2 and is computed by advancing the already obtained lower layers.
All transverse dependencies have layer ell-1. Consequently each new coordinate
has the form

    new_i = a_i(lower old layers) XOR H(old_i XOR b_i(lower old layers)).

Coordinates within the same ell layer do not depend on each other. Thus the
advance F_L is a triangular permutation on the whole abstract finite strip,
not just on physical dipole strips. The copied `strip.py` also contains an
explicit inverse, as checked in the earlier depth-three work.

## 3. Universal identity exponent

At layer ell=0 the sole coordinate evolves by H, and H^12 is identity.
Suppose the submap on all layers below ell has global identity exponent Q.
After Q steps those lower layers return for every initial lower state.
Conditional on that lower state, each coordinate of the ell layer has undergone
some permutation of its eight possible triples. Its identity exponent divides

    lcm(1,2,3,4,5,6,7,8)=840.

The same 840 works simultaneously for every coordinate and every lower state.
Therefore Q*840 is a global identity exponent on layers through ell. Induction
gives the conservative bound

    F_L^(12*840^L)=identity.

This is an exponent bound, not an assertion that any physical orbit has that
minimal period. It does not require enumerating the large strip or its cycles.
For L=144 the actual P is an integer multiple of the bound, because185>=144.
Hence, for every n>=0 and every physical origin/M2 strip,

    W_(n+P)=W_n.

The argument tolerates arbitrary M2 and x. It depends only on the strip closure,
triangular dependence, and the finite triple permutation exponent.

## 4. Exact index budget for the two slices

Write a point in the target ball as

    (dx,S-1+dy,70+dz),   |dx|+|dy|+|dz|<=radius,
    j=-1+dy, n=S+j, n'=T+j.

At time t=S+c, ell=c-j. Let a,b be the sorted absolute transverse coordinates
|dx|,|70+dz|. For the S-1 slice, radius72 and c=-1, so any nonzero strip entry
has

    ell+a+b<=142,   n'>=112.

For the required S-2 old slice, radius71 and c=-2, the bounds are140 and113.
Both are strictly within L=144 and remain forward of n=0 after subtracting P.
Therefore at every required location,

    U_(S+c)^cluster(dx,S+j,z)
      = U_(T+c)^cluster(dx,T+j,z).

Only286 active-parity locations on the first slice and71 on the second can be
nonzero from the cluster. All have origin-front lag0 or2. The exact reduced
times are184 and183. This yields a bounded computation rather than simulating
S ticks or constructing the L144 state explicitly.

The calculation at reduced time must still use both initial sources. In
particular M2's vanishing isolated first-arrival coefficient at the final s
is not a license to delete M2 from the nonlinear cluster calculation.

## 5. Proposed exact six-source algorithm

1. Evaluate the lower two-source cluster at the357 potentially nonzero reduced
   locations just specified, keeping all16 x/M2 assignments if convenient.
   Direct memoized native recursion may prune using both source light cones;
   it must preserve all six neighbours and the old local term. The strip proof
   justifies the time/axial shift, not a simplified local update.
2. At the actual S-1 slice, add the three selector first-arrival contributions
   using exact multinomial parity at their actual large coordinates. Do not
   substitute a smaller P in those coefficients without a separate proof.
3. Evolve the resulting lower-only data through the finite shrinking cone to
   R-2 and R-1. This retains origin/selector and M2/selector interactions from
   their first possible meetings, including those at S and S+1.
4. The upper source is at distance2R from the origin and every selector, and
   2R+2 from M2. It cannot interact with the lower cluster before R. Add its
   exact isolated-pulse values on R-2/R-1 using the appropriate already-proved
   bounded-lag recurrence, checking its complete displacement coverage.
5. Apply the full native rule for the final four ticks through N=R+3. Check
   the actual operand intervention as a diagnostic only, all M2 assignments,
   the complete raw endpoint, and all inherited masks.

Steps3-5 require their own exact coverage checks and endpoint results. No
favorable output is asserted here. In particular retaining the M2 resource
in the initial prescription does not prove independence of a new carrier from
the old public record; joint-law verification remains a separate obligation.

## 6. Bounded controls

`checks.py` uses no network and prints only to stdout. It verifies:

- 1,872 direct two-source native-recursion comparisons with the strip map:
  all16 x/M2 inputs, n0..8, all13 entries of L6;
- the complete512-state abstract L2 strip permutation, with each orbit length
  dividing12*840^2 (observed lengths1,3,4,6,8,9,12,16,18,24,30,45,48);
- every one of40,320 permutations of eight triples has exponent dividing840;
- H^12=identity and exact giant-P divisibility by12*840^144;
- exhaustive geometry of the two small target-centered balls, including the
  index budgets, positive reduced coordinates, and nonzero counts286/71;
- a nonlinear countercontrol: with x=1 and M2=001, the value at(0,-1,0),tick1
  is H((0,1,0) XOR001), which differs from the sum of the isolated evolutions.

These are bounded controls of the symbolic all-L induction, not an enumeration
of the enormous L144 state space. No large computation was used. Normal and
Python -O runs have byte-identical output and explicit failure checks.

## Files and limitations

`strip.py` is copied from the prior depth-three recurrence implementation;
its exact hash is in PROVENANCE.json. The new checker has its own independent
two-source direct evaluator. The theorem is new mathematical scrutiny of the
parent's proposed period shortcut; the source reduction and active-parity
preparation are inherited from junction_v4 and are not re-proved in full here.

Run `python3 /path/to/six_source_v5_geometry/checks.py` and repeat with `-O`.
This avenue makes no repository mutation, premise adoption, native-reset claim,
or general claim against OI or its finite-precision programme.
