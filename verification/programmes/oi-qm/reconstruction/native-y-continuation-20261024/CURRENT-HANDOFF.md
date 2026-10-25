# Native instruments: current research handoff

24 October 2026. This continuation retains the actual masked phase and adds
two scoped native tests, an explicit logical acceptance specification, an
exact reset-resource audit and an executed finite-menu approximation. These
are research results on #910, #911 and #912. No physical premise, access rule,
operational map, native gate availability or full equivalence is adopted.
#885 is read-only for this effort; #913 retains the wider open gates.

The owner-accepted programme synthesis remains
`2d555f17c23bea31d32b3f5eb4c49d245b413a76`. The separately observed #885
draft is `fd18205b47649ff4bd43857b908f6f646941e89f`; it is not substituted
for that accepted baseline. Its retained-evidence and commissioned independent
transport-review gates remain distinct from these separate-agent internal
reviews. No new owner acceptance or formal certification is inferred.

## Retained actual phase

Keep T=185, P=12*840^185, S=P+185, R=S+68 and L=R+9=P+262 and the
unchanged torus. Native A, author
`f24a57a7c23cc1818c04265cec7604f8bc2f410d`, retains initial independent
triples F8/F10 and adds F9 at (-(L+2),S,77). At phase L+2, current
q9=V and its six previous neighbors give a fixed local inverse of oldP:

    oldP=V XOR H(XOR six previous neighbors),
    s=V.B XOR XOR six previous-neighbor D bits.

The previous Q8/Q10 cells still contain the actual six-bit pool. Conditional
on the other initial variables, (Q8,Q10,M) and (Q8,Q10,V) are uniform on 512
values. A single whole-V read is harmless within the retained contract.
The inverse is a coordinate map, not an available observer read or native
unmasking gate. Continuous q9 access and later joint histories remain open.

The intended acceptance is A=[K<n(Y XOR s,Rsign XOR s)] with thresholds
(5,0,4,1). It gives success5/16 and accepted post-X mask weights5:4:1,
with fair Z. Parent failures remain terminal. Native dynamics has not yet
implemented this correlated acceptance flag or a reusable outgoing interface.

## New native nonlinear and pointer result

`native_gate_v13/`, author
`8ae927163c0fa340b312d634fc352df73753314f`, evolves seven small original-time
families, not the actual huge-L boundary. All 28,672 native worlds retain
the complete rule, dirty backgrounds and a sole old-input source. Actual
fields contain nonlinear products of the old sign with actual pool operands.
On its attained P=(0,s,1) sector, writing E,B,D for the respective XORs
of Q8,Q10,M, the physical current D field is

    V.D=1 XOR E XOR D XOR B*D XOR s*B.

This includes s*Q8.B and hence a real old-sign/new-Y product. Other terms
remain physical masks. It is not an isolated available Toffoli or flag gate.

None of the 525 tested radius-two terminal pointers at three post-pool ticks
computes A, even with arbitrary Boolean relabelling; their complete same-site
prefixes also fail. The prepared-shape P.A=0 sector is checked separately.
The best terminal comparison error is 5/32 and best prepared prefix error
37/256. These are source-ensemble classification errors, not OI-wide or
quantum A2 error floors. Distributed circuits, later times, other layouts
and actual-L availability are outside the exclusion. Separate-engine review
is retained under `native_gate_v13/review/`.

## New actual-scale second-front route

`native_route_v13/`, author
`753fe4f69392ca940754489468e8c8235f6aa583`, changes Native B's q10-ready
source variant by adding E=(0,-78,78). It preserves old q9 at L and retains
the original-time source, readiness, bank and informative-record checks.
It does not inherit Native A's optional uniform F10 pool unchanged.

The coupled lower first front and unchanged upper/collision dynamics give
an exact 4096-row q10 table at the actual scale, using proved period bounds.
E=000 reproduces the old 512 rows. The new E removes the previous universal
single-cell sign loss:32 common injective raw X pairs become compatible
across the 24 known accepted contexts. Nevertheless, no jointly affine initial
E/N controller selects one. All 16 surviving affine E candidates require a
nonaffine known-seed N law; explicit four-context affine-relation violations
are retained. No nonlinear control is inserted silently into the initial prior.

This is a raw-binary/affine-source obstruction in that geometry; fixed
redundant q10 readouts are decided in the next section. Changed layouts and
weaker operational instruments are not excluded. Separate review is
retained under `native_route_v13/review/`.

## Fixed q10 readouts of the same table

`native_decode_v14/`, author `7f843073d9245635d5b2bbeb0cfdc9f42dc7db0a`,
plan `36213be6354ef15442b4f3040ecdb511fd0b5641`, decides every nonconstant
Boolean readout of the whole q10 triple, common to the 24 accepted
contexts, against all 2^36 jointly affine known-seed E/N laws on the
retained 4096-row table. 78 of 254 readouts decode s exactly on all 48
accepted rows (7464 laws). The single field q10.A equals s under 1456 laws;
one such law depends on mY alone: E=(1,1 XOR mY,1), N=(mY,1,1 XOR mY).
Eight of the fourteen nonconstant degree-one readouts succeed; q10.B,
q10.D and A XOR B XOR D, and their complements, have no law.
Two independent exact solvers agree on every solution set, with planted,
brute-force, raw-pair reproduction and sign-erased controls.

So, under the affine source contract, the q10 cell at L+1 carries s in its
single field A for suitable laws. The separate review shows that s is
not singled out: for each affine function f of the known seeds, some law gives
q10.A = x XOR f(k), so the table carries the old input x with a law-chosen
seed offset. q10 is a private cell under Native A, not a permitted read, and
no read operation, post-read carrier law or reusable interface is modelled.
Post hoc: no affine law has E identically 000; B and D jointly carry s in
every q10.A law (B alone is s-free in 8 laws, per the separate review); a fresh bit on the E
constants pads q10.A but never hides s in the whole triple given the seeds.
No native stage that consumes q10.A while tolerating B and D, no Y operand,
acceptance flag or joint history/carrier law follows. Separate review is
retained under `native_decode_v14/review/`.

## One native tick into the whole-V read

`native_vread_v15/` (plan `ead2c38842222786c68551484b708c19f29c83ab`,
committed before computation; head `ca7d06de349e83cbfa253cbd4887b7708a0705cc`;
separate review retained under its `review/`) tests the cheapest native stage
from q10.A towards a permitted read: one tick from q10 at L+1 into Native A's
single whole-V read at L+2, applied to the native_route_v13 geometry as a
hybrid test case, with neither contract adopted. Result:
`NEGATIVE_FOR_CONSTRUCTION`. Two of the five non-q10 key cells of q9 at L+2,
the -x key (-(L+2),S,77) and the +y key (0,S+(L+2),77), are free complement
variables that no permitted record through L+2 depends on, and V is a
permutation of each, so no fixed readout of V equals s for every complement
value. Under a uniform free key V is uniform and independent of q10.A, s,
the seeds and every other permitted record through L+2. Delivery through
this read needs those keys known, by pinning (a preparation change) or by
reading their q9 neighbours (an access change); neither is adopted. The -y
key also reaches public port 0 at distance 341; recovering it from that
record is not computed.

The classification is conditional on the declared ready-cone, source and
bank inventory shared with native_route_v13 being complete; a separate
enumeration from the primary declarations in the separate review agrees.
Multi-tick routes, other layouts, readiness extensions, Native A's own pool,
the acceptance predicate and A1/A2 are untested; this is no OI-wide no-go.

## Explicit acceptance specification and the native delay gap

#912 author `1cb224db6c17e083849a0f82768e991beac39399`, under
`composition_flag_v6/`, gives an 89-gate NOT/CNOT/Toffoli compute/copy/uncompute
circuit on the actual21 logical phase wires. Seven clean temporaries,
one clean flag bit and two fair pointer fields give31 core register bits.
The logical phase and workspace are restored. The complete90-sample whole
pointer prefix, accepted carrier, old record, failures and zero cells have
the correct conditional joint law. An optional explicit recording dilation
uses 270 additional clean bits and 359 total logical ticks.

Logical storage, gate access, clock and workspace isolation are supplied.
They are not an implementation in the native H lattice. Under a hypothetical
serial one-gate/native-tick alignment from L+2, the core finishes L+91;
F8 can reach an old receiver at L+77 and F10/F9 at L+79. The unchanged-prefix
causal proof therefore does not cover that duration. This is a required joint
history/carrier audit, not proof of leakage or a native runtime lower bound.
The recorded dilation would extend that hypothetical deadline to L+361.

Extra private-key/workspace access and uncontrolled native delay have explicit
failing controls. Reusing unused pointer pads only violates the chosen
independent-noise reference; a changed correlated-noise contract is separate.

## Exact and approximate architecture paths

#911 keeps the credited KS sphere model as a supplied mathematical comparison.
The new `a1_reset_v6/` fixed-vector reuse audit, author
`41992cc0b7f8901195f70ff47b34f1a0ed5eba5e`, finds Z+ then X then Z gives
final Z+2/3 instead of 1/2, complete-record TV1/6. This preserves Montina's
original two-time result. Supplied independent-pair renewal repairs the
record/state law; the continuous-resource gap remains explicit.

The new `a2_efficiency_v6/`, author
`bff7b58d951babd4064b60699281ee0a7f3e9f45`, executes a 1536-label finite
geometric controller. For its declared menu and total h=3 horizon, one fixed
positive input/output decoder has complete record/state CQ error at most
17239332625914280559/230584300921369395200 <0.074764. It uses 96 initial
fair bits plus clock/word, tables, blank registers and retained workspace.
This narrower certificate does not replace the old broader all-menu theorem.
Both new architecture paths have accepting separate-agent internal reviews.

## Next gate and verification scope

Construct a source-compatible native gate or cheaper distributed predicate,
deliver the actual operands, preserve/re-encode the carrier throughout its
latency, and prove its full physical pointer/history law. The small native
product, the q10.A sign delivery and the logical acceptance circuit are
distinct pieces; none alone supplies their missing native connection. A
concrete next test is a native stage taking q10.A to a cleaned operand
while its s-carrying B and D fields are accounted for; the one-tick route
into the whole-V read is excluded for its construction (`native_vread_v15/`),
and recovering its -y key from the permitted port-0 record is untested.

`python3 replay.py --latest` checks the four reviewed v13 native groups and
the v14 fixed-readout author group normally and with -O, Python compilation
and the full manifest. The driver retains 58 groups; the preceding 53
scientific groups are unchanged and are not freshly rerun. Four current #911 groups and two #912 groups
are checked separately. CHECKPOINT-CHECKS.json records measured scope.
No full-suite, Lean or exact-head attestation is claimed. Wider calibration,
initialization/access, arbitrary-depth/menu, composites/Bell and full A1/A2
reconstruction remain open. No unattended work, dispatch, merge or branch
deletion is scheduled.
