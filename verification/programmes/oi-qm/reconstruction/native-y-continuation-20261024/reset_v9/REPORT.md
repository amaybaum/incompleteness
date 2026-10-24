# Native q8 boundary and an affine-seed masked route to q9

Research checkpoint, 24 October 2026. Source: #910 at
`f264dff4eacae84959b4a4419be204fb8c31c9e3`. The bounded continuation supplies
one physical masked-sign route on the retained native family. It does not
supply the full post-Y reset or an arbitrary late-input socket.

## Result

Retain reset_v8's W=111 and G=(u,1 XOR u,1), giving q8=(0,y,0) at R+8,
where y=x XOR u. Extend the original initial ready region to the current
radius-(R+9) and previous radius-(R+8) balls about q9=(0,S,d+9), d=68.
Preserve every inherited source, W,Q,C,G. Add one current initial source:

    position (0,S,S+2d+18), payload J=(u XOR a,a,u XOR a).

Here a is a prospective new independent fair apparatus bit, specified at the
original initial time. J is affine in u,a and contains no unknown x, no copy
of the later y and no late-time intervention. The unchanged native rule gives

    U_(R+9)(q9)=(0,y XOR a,y XOR a).

This fixed encoding is common to all retained native x,u and selector masks.
The earlier q7 and q8 values are unchanged. Conditional on a being fair given
the complete relevant history, this is a fair masked sign; that conditional
freshness and the joint public-history law are separate obligations. The
identity itself holds pointwise for both a values. There is no simultaneous
outgoing Y branch: the known q8 value is at an earlier time.

The affine source formula is a deduction from the preregistered common-code
census, not a retroactively preregistered target. The census has eight common
ordered code pairs; selecting (000,011) and (011,000) yields the formula.
The prescribed clean-A, clean-B and standalone mixer targets all fail in
this one-source, one-tick family. There is no common injective full-triple
encoding of an arbitrary bit substituted into q8.B with its past retained.

## Actual boundary creating q8

Offsets below are relative to q8. Six incoming cells are at R+7, old local
at R+6. Set F(m)=(u XOR m,1 XOR m,1 XOR u XOR m XOR um).

| Incoming offset | Exact native triple |
| --- | --- |
| -e_x | F(mR) |
| +e_x | F(mY) |
| -e_y | (x XOR u XOR xu,0,1) |
| +e_y | F(mY XOR mR) |
| -e_z | (0,0,x XOR u) |
| +e_z | (1 XOR u,u,1 XOR u) |
| Old local value | (1 XOR u,1,0) |

All sixteen input/mask assignments are retained and scalar-update checked.
This is not a cold neighborhood. It is the boundary creating q8, not the
complete future state around q8 at R+8. That larger two-slice state can be
correlated with exposed frontier records. The q9 calculation keeps its actual
causal boundary; it does not replace q8 by a standalone input. The result
also retains the old-local and six incoming cells creating masked q9 for
all 32 x,u,mY,mR,a assignments.

## Exact coupled front and giant-delay reduction

W reaches exactly two points in the new q9 backward diamond at R-1:
(0,S-9,76) and (0,S-10,77); it reaches none in the R-2 slice. Define
F0(j) at (0,j,76), time j+76, and F1(j) at (0,j,77), time j+77. Then

    F0(0)=H(H^75(0,x,0) XOR H^75(1,1,1)),
    F1(0)=H(F0(0)),
    F0(j)=H(F0(j-1) XOR [j AND 75=0] H^(j+75)(0,x,0)),
    F1(j)=H(F1(j-1) XOR F0(j)).

For F1(0), the W-only -y predecessor has parity binom(76,1)=0 mod 2.
At subsequent first-front points, the old local and other four neighbors
are unreached; -y and -z give the displayed terms. These are coupled native
recurrences, not superposition of independently evolved pulses.

F0's forcing is 384-periodic, giving a sufficient period 384*840. Over that
period F1 is periodically driven and its block map is an eight-state
permutation. Thus 384*840^2 is a sufficient joint period. Actual
P=12*840^185 is divisible by it, so the needed indices P+176 and P+175
reduce exactly to 176 and 175. Direct native recursion checks both layers
at j=0 through 8. Finite block controls additionally find F0's 384-step map
is identity for all eight starting triples and both x values; this stronger
fact is not needed for the larger sufficient bound.

Q,C,G,J occupy upper axial offsets 0,14,16,18. Their joint nonlinear strip
has budget 18. The retained strip-period lemma gives 12*840^18, dividing P.
The new four-source evaluator checks 6,000 small-coordinate scalar entries
against direct native recursion. All subsequent interactions are kept in
the complete q9 collision diamond.

## Initial preparation, access and next obligation

The new initial balls contain the old depth-eight balls. Preserved sources
are exempt from zero pins. All 1,479 retained source positions lie on or
outside the new current boundary; J overwrites none. The inherited previous
unknown at the origin lies outside the new previous ball. Six specified
outward frontier rays move strictly farther away from q9, so their
nonzero-index bank sources stay outside this endpoint cone. In particular
M1=(0,-1,0) has distance R+10 from q9, exceeding its R+9 deadline. M1 can
nevertheless occur in the full future neighborhood of q8.

Signal sources and q9 have even spacetime parity. The native update
preserves t+x+y+z mod 2 since all predecessor terms share the output parity.
This sanity check does not remove the other component from the full boundary.
J cannot reach q8 before R+10. The new calculation reproduces qY,q7,q8 and
every q8 incoming cell above; preservation is measured explicitly.

The standalone direct-reset compiler uses a cold initial Q and a synchronized
first-arrival mixer M_a(A,B,D)=(A XOR a,B,D XOR aB). Applying it directly
at late q8 would omit the actual nonzero old-local value and dirty neighbors.
The present family rejects its target M_a(0,y,0)=(a,y,ay). No translated
cold apparatus or compiler was installed.

The positive route supplies one sign mixed with a preloaded bit. It does not
produce separate X,R masks with conditional weights 5:3:2, fair z, native
heralds, failure branches, retained information or a reusable output encoding.
A next construction must create those outputs from the actual native signal
and prove their joint law. No source freshness, access restriction, physical
premise or calibration is silently derived here.

## Replay

From this directory in the retained tree:

```sh
python3 checks.py > /tmp/oi-reset-v9.json
cmp /tmp/oi-reset-v9.json result.json
python3 -O checks.py > /tmp/oi-reset-v9-O.json
cmp /tmp/oi-reset-v9-O.json result.json
sha256sum -c SHA256SUMS
```

Only stdlib and sibling reset_v8/reset_v7 evaluators and source geometry are
needed. PROVENANCE.json pins the inputs. Normal/-O outputs are identical;
controls raise before verdicts. New checks cover 512 diagnostic rows,
16 q8 boundary rows and 32 masked-q9 boundary rows. No Lean certificate,
special dispatch, F/E designation, manuscript change or full equivalence
is claimed. Separate-author review is pending.
