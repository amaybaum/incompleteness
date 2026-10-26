# Alternative remote fanout: source-direction and odd-cycle obstructions

Research result, not a new reset. A bounded alternative to the late-q8 fork
tries to reconstruct y=x XOR u from the original unknown x wave and apparatus
seed u at several remote outputs simultaneously. The apparent positive seed
direction violates an old informative-record cone. The safe opposite direction
has an exact order-three obstruction to a common full raw output law for y.
These results close only the fourteen-endpoint family stated below.

## Candidate and original-source geometry

Keep T=185, P=12*840^185, S=T+P, R=S+68 and the existing W=111 source at
(0,-76,76). Set L=R+9. The examined endpoints are

    p_delta = (10,S-delta,67+delta),  delta=11,...,24.

They lie on the time-L first fronts of the original input source (0,x,0)
at the origin and W. Each proposed current ready ball has radius L and each
previous ready ball radius L-1, retaining the sources. The unknown previous
input at the origin lies outside every previous ready ball. No unknown x
is copied or preloaded into the new apparatus.

All 1,479 retained original source entries were checked against all fourteen
endpoints. Only the original input origin is at distance at most L, at equality;
every other original source lies strictly outside. All four selector-mask
sources, the original positive/negative upper pulses, C, G and the later J
source also lie outside. Old remote herald/Z programs are separated by their
x coordinates. This is the actual retained source geometry, not an isolated
origin surrogate. The seven full frontier families through L are outside
every new current ready ball, by exact affine-distance bounds. Existing
source exceptions remain preserved and no reserved frontier bit is pinned.

The fixed native rule is H(A,B,D)=(B,D,A XOR BD), with the old-local XOR term.
On a first front the old-local slice and positive-direction neighbors have
not yet arrived. The origin and W waves nevertheless interact with each
other, so their separate pulses cannot be superposed.

## Exact coupled strip and the enormous time

Write F(r,j,k) for the native field at (r,j,76+k), time r+j+76+k, with only
the origin/W sources in its dependency cone. For j>=0, r,k>=0,

    F(r,j,k) = H(F(r-1,j,k) XOR F(r,j-1,k) XOR F(r,j,k-1)).

The r=-1 term is zero. The k=-1 boundary is the origin-only first front:
H^(r+j+75)(0,x,0) times the binary multinomial parity for (r,j,75).
The j=-1 initial boundary is the W-only first front:
H^(r+75+k)(111) times the parity for (r,75,k).
These parity rules mean pairwise-disjoint binary digits, not real-valued
superposition. Every nonlinear collision in the finite strip is retained.

The relevant strip is 0<=r<=10, 0<=k<=15: 176 triple variables. Its external
forcing has period 384=lcm(128,12). Each one-step strip update is triangular
in increasing r+k, with a permutation of eight values on each diagonal.
The same holds for a 384-step block. Inductively, a triangular permutation
on N eight-valued coordinates has order dividing 840^N: after the lower
coordinates repeat, at most a factor lcm(1,...,8)=840 restores the next one.
Hence 384*840^176 is a sufficient sequence period. The actual P is divisible
by this integer, checked exactly, so j=P+185-delta reduces to 185-delta.
This is a written exact periodicity argument, not an extrapolation from a
smaller substitute P. It makes no minimal-period assertion.

Without an additional masking source, only delta13,17,21 distinguish x:

| delta | Full output for x=0 | Full output for x=1 |
| --- | --- | --- |
| 13 | 000 | 101 |
| 17 | 000 | 111 |
| 21 | 000 | 101 |

All eleven other endpoints give 000 for both inputs. This by itself cannot
produce y=x XOR u, nor any fresh post-Y distribution.

## Why the tempting positive direction is invalid

A source at B_plus=p_delta+L e_x would first interact with the origin/W front
at the final tick. Its two seed-dependent payloads can algebraically translate
the distinguishable input pair into a fixed XOR code. However, its distance
to the old selector-Z public port (4T,P,0) is S-401, so it can arrive **401
ticks before the informative deadline S**. It conflicts with that earlier
ready/record cone. The isolated final-collision formula is consequently not
an accepted native extension of the existing apparatus. No positive result
from this invalid geometry is retained as a construction.

## The safe direction and its actual collision

Instead put B_minus=p_delta-L e_x. These sources are outside every old
informative deadline cone and cannot change earlier q8. They do not coincide
with the old bank: their x coordinate is below -T, whereas the old ray x
coordinates are 0, +/-T, 4T or positive near 12R. Different delta sources
are at distance L+2|delta_i-delta_j| from each other's endpoints and so do
not couple to the other new outputs by L.

This direction is not a final-tick collision. It meets the origin/W front at
x=0, time L-10, and then undergoes eleven coupled native updates. For a seed
payload b, its exact axis recurrence is

    C_-1 = H^(L-11)(b),
    C_s = H(C_(s-1) XOR F(s,j-1,k) XOR F(s,j,k-1)), s=0,...,10,

with j=S-delta and k=delta-9. The off-axis terms cannot yet depend on b,
because b has a unique straight first-arrival path. Its full output is C_10.
For each fixed x this is a permutation A_x of the eight possible payloads.

All sixteen payload/input cases are evaluated at every endpoint. For the
relative permutation A_0^-1 A_1, every cycle has length one or three. At the
three informative endpoints the cycle type is 3+3+1+1; at the other eleven
it is the identity. None has a two-cycle. Thus no two apparatus payloads,
selected by u XOR mask, give two distinct common full-triple codes for
x XOR u XOR mask. A checker positive control with a genuine XOR translation
finds all four expected code pairs, so the absence is not a vacuous search.

## Stronger full-law obstruction in this family

The result also excludes repairing these endpoints by randomly mixing
payloads, correlating their seeds, or adding a herald depending only on those
apparatus seeds and u. Let A_x be the simultaneous response permutation on
all selected endpoint payloads. Cross-exclusion makes it the product of the
individual A_x maps, so T=A_0^-1 A_1 has T^3=id. Let nu_0,nu_1 be arbitrary
accepted payload laws for u=0,1, independent of unknown x. Allow arbitrary
correlation among the payloads; a seed-only herald just changes these laws.

For full raw output laws to depend only on y=x XOR u, the four histories
would require

    A_0 nu_0 = A_1 nu_1 = mu_0,
    A_1 nu_0 = A_0 nu_1 = mu_1.

Applying A_0^-1 gives nu_0=T nu_1 and nu_1=T nu_0, hence T^2 nu_0=nu_0.
Since T^3=id, this implies T nu_0=nu_0 and therefore mu_0=mu_1. The two Y
outcomes cannot be distinguished by any fixed decoder of the entire offered
output. A separate independent Z sample cannot cure this, since it adds an
identity factor. The statement concerns full raw laws, not only one decoded
marginal. An input-coupled herald, other sources, endpoints or dynamics are
outside this result; no general reset impossibility is claimed.

## Actual-q8 operand boundary

Every examined endpoint is farther than one lattice step from q8 at R+8.
Changing only q8's observed Y component at that time therefore cannot affect
these outputs at L=R+9. This avenue deliberately reconstructs the native
relation x XOR u from the original source and would fail a demanded late-q8
operand intervention even if its other problems were removed. It must not be
presented as a reusable q8 socket. The unchanged target or its acceptance
rule is not relaxed by considering this alternative.

## Evidence and next wall

`PLAN.md` records the initial three-endpoint family, the finite extension to
fourteen after its failures, and the source-direction correction. The final
checker reports 20,706 inherited-source comparisons, 98 full frontier-family
exclusions, every payload table/cycle and exact P divisibility. Its separate
direct six-neighbor native recursion checks 3,072 scalar cases at bounded
coordinates, including all W values, all new payloads and arbitrary previous
input triples. It matches the coupled recurrence and detects 768 failures of
the false last-tick-collision shortcut. Blank prefixes are checked there;
actual-parameter blank prefixes follow from the proved first-arrival cones.
Normal and optimized replays match `results.json` byte-for-byte.

The next construction must change this explicit remote family, use a genuinely
input-coupled mechanism, or continue with the actual q8/q9 two-slice interface.
This result does not constrain those alternatives. No calibrated reset,
new herald, native full-carrier output, target extension or premise is adopted.

## Provenance and replay

The existing source census is
`parallel_v3/history_control/SOURCE-GEOMETRY.json` under the #910 native-Y
continuation namespace, SHA-256
`2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d`.
The checker verifies that hash and imports no previous evaluator. The original
input/selector/upper/W source coordinates are the retained native geometry;
the remote source programs are excluded by their entire coordinate ranges.

From the retained `layout_v10` directory run `python3 checks.py` and
`python3 -O checks.py`; both must match `results.json`. An explicit
`--geometry path` can point at the same hash-pinned census in a sparse copy.
This is exact finite computation plus written geometry/group arguments,
not Lean certification, a dispatch attestation or a full-equivalence result.
