# Native actuation: transported phase coordinates and the missing physical gate

Research checkpoint from input `580048383de9ad0883c43f44fe19bad8c46ddf98`.
This fixes a mathematical carrier coordinate at the proposed observation cut
and tests the local native coupling needed to use a sign. It does **not**
establish an observer-accessible carrier, an available actuator, or reuse.
The native source, prior, readiness, public banks and access declarations
are unchanged. The later horizon remains the prospective H=L+79.

## 1. A fixed carrier coordinate, with its access boundary

Write F for the complete native update on two slices, C_t=(U_t,U_(t-1)).
Its inverse is local:

    F^(-1)(V,W) = (W, V XOR h(neighbor-XOR W)),
    h(A,B,D) = (B,D,A XOR BD).

Use the actual q9=(0,S,77), q8=(0,S,76), q10=(0,S,78). At the old cut L+2,
define the **raw phase coordinate**

    chi_(L+2)(C) = (p,Q8,Q10),
    p = U_(L+2)(q9) XOR h(XOR_(w~q9) U_(L+1)(w)),
    Q8 = U_(L+1)(q8), Q10 = U_(L+1)(q10).

Keep all nine raw bits, rather than discarding old failure fields or q10's
B/D fields. On the retained accepted old phase p=(0,s,r_old). This is the
seven-site inverse already proved in the native sources, with the pool
fields retained. Its meaning is fixed by the earlier phase, not by a new
fit to the port5 outcome.

At the fixed new cut set

    chi_H(C_H) = chi_(L+2)(F^(-77)(C_H)).

This is a single deterministic function of the actual two-slice state,
common to every preparation/sign/context branch. It invokes no historical
record or private-background-dependent choice of decoder. Native
invertibility proves that it gives the actual earlier raw tuple on every
trajectory. An induction through the inverse recurrence bounds its input
footprint by current-slice radius77 and previous-slice radius78 about q9:
recovering U_L requires those radii; recovering U_(L+1) at adjacent q8/q10
fits the same bounds. These are sufficient dependency bounds, not a claim
that every site has a noncancelling influence.

This construction pins a **transported mathematical coordinate**. It is not
a physical decoding circuit or a declared read: most of this footprint is
private, and neither the old access declaration nor prospective port5
reading grants those fields. Transporting an old label by inverse dynamics
also does not prove that a subsequent native stage can accept it as a
reusable input. A time-indexed inverse encoding alone provides no new
measurement dynamics.

The source distinction matters. Native A supplies a conditional six-bit
fresh pool and an optional additional fair F9 triple. The route-v13/v14
variant supplying q10.A=s replaces the optional F10 factor by a ready pin.
chi_H is defined for both raw states, but the latter does **not** acquire
Native A's uniform pool, acceptance law or quantum target by using the same
coordinate names. Their actual joint distributions must remain separate.
On earlier terminal failures the raw microscopic coordinate still exists;
there is no attempted new read or offered carrier.

## 2. Exact local control identities

For the complete next-site update V=p XOR h(sigma), with sigma the XOR of
all six actual neighbors, direct algebra gives

    h(sigma XOR (s,0,0)) XOR h(sigma) = (0,0,s),
    h(sigma XOR (0,s,0)) XOR h(sigma) = (s,0,s*sigma.D),
    h(sigma XOR (0,0,s)) XOR h(sigma) = (0,s,s*sigma.B).

Thus an isolated A-field difference produces an exact D-field translation
at this site, independent of the dirty background. B- and D-field
differences also couple to residual fields. This is a positive algebraic
control for the **actual native rule**, not a physically supplied XOR write.
Producing that isolated A-field difference, while preserving the other
required inputs on the actual source support, is the actuator obligation.
The differing neighbor itself and all other outgoing sites remain part of
the physical output; a clean difference at one site is not a full carrier
or apparatus reset certificate. Nor does a D translation of a uniform raw
triple by itself give an informative measurement.

The old-local term p cannot be omitted. In the actual fewest-seed v14 law,
E=(1,1 XOR mY,1), N=(mY,1,1 XOR mY), q10.A=s while
p=(0,s,s XOR a XOR b). At the old one-tick stage write eta for the XOR of
the other five neighbors and sigma=q10 XOR eta. Then

    V.D = a XOR b XOR eta.A
          XOR (q10.B XOR eta.B)*(q10.D XOR eta.D).

The explicit s in q10.A cancels the s in p.D. The residual q10.B/D fields
and actual eta still matter. This exact identity is about that old stage,
not a derived operation at H.

The retained native tables allow a further diagnostic. For each of the24
accepted known-seed contexts, compare s=0 and s=1 with the same allowed E/N
law. The complete raw q10 XORs and **formal** output XORs at equal eta are:

| q10 XOR (code4A+2B+D) | Contexts | Possible V XORs as equal eta varies |
| --- | ---: | --- |
| 4 | 8 | 2 |
| 5 | 4 | 0,1 |
| 6 | 10 | 6,7 |
| 7 | 2 | 4,5 |

In16 contexts, changing the source sign changes q10.B or D as well as A.
Even in the eight pure-A cases, p changes too, so the formal output is a
B flip, not the isolated-input D flip above. These are unweighted context
counts, not native failure probabilities. Holding eta equal is a symbolic
local-coordinate test: the actual eta_0 and eta_1 can differ under the two
source preparations. Consequently this table neither computes the native
joint output law nor excludes a source-correlated useful gate. It shows
exactly why q10.A=s alone cannot certify that gate.

## 3. Source audit and next constructive obligation

Anchors are under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:

| Retained source | Available result | Remaining operation needed here |
| --- | --- | --- |
| shared_v12/INTERFACE-CONTRACT.md; native_x_v12/REPORT.md | Actual phase inverse; Native A's specified resources and abstract target | Physical decoding/acceptance and a reusable boundary |
| branch_v10/local-controller/REPORT.md | Native affine-source sign code in its original family | Not an arbitrary reusable input socket; not late record feedback |
| native_gate_v13/REPORT.md | Actual old-sign/pool products in seven small families | Actual-scale operand delivery and complete pointer/carrier law |
| native_route_v13/REPORT.md; native_decode_v14/REPORT.md | Actual-scale private q10.A=s for selected affine initial laws | Process the whole triple; preserve its actual source law |
| native_vread_v15/REPORT.md; CURRENT-HANDOFF.md | Declared reads and the one-tick masked-stage obstruction | No read of q10, private inverse footprint, or late write is supplied |

The old whole-q9 record already supplies s to the observer on its declared
phase. None of the listed declarations specifies a native record-to-local-
field feedback map at H. Setting a private field to s, adding a fresh
controller, pinning masks, changing the E/N law according to a later record,
or executing the inverse as a read would therefore be a new candidate
resource/operation. This audit adopts none of them. This is a statement
about the listed contracts, not a no-go for autonomous native feedback,
another sourced layout, or OI generally.

The next constructive unit must exhibit a concrete native subcircuit or
autonomous interaction delivering the actual s to a declared operand, with
its original-time sources and admissible inputs fixed. It must then compute
the complete record/output kernel and return a boundary accepted by another
native stage. If it uses chi_H, it must physically implement the relevant
encoding/decoding; if it uses another carrier, it must justify its fixed
dictionary from that source. Full raw records, outcome-dependent flags,
failures, carrier fields and residual apparatus must remain accounted for.
Only then is a two-setting comparison well posed. No longer route is tested
here, and no integration with Track A's distinct scalar torus model follows.

## 4. Reproduction and limits

From the continuous-substates directory run:

    python3 -I -B native_actuation_boundary_probe.py
    python3 -I -B -O native_actuation_boundary_probe.py

Both print identical structured PASS data:128 full p/sigma/sign local
translation controls;35 small whole-native-world transported-coordinate
controls;24 accepted actual-table contexts,192 formal background cases;
eight old terminal-mask contexts rejected before a table read; histogram
8/4/10/2 as above. The two retained input tables are read in place and
their raw-table SHA256 pins are checked. The probe imports no earlier
engine. It uses exact integers and explicit checks active under -O.

The fixed-cut pullback and local identities have general algebraic proofs
above. Small worlds test the implementation; they do not certify access,
the actual H-cut distribution, the native joint eta law, failure measures,
quantum measurement, or reuse. Deliberate local-rule, old-term, terminal-
guard and input-table mutations must fail in normal and optimized execution.
Independent review of this checkpoint is pending. Earlier accepted results
and manuscripts are unchanged; no F/E, special dispatch or merge follows.
