# Avenue A: a conditional native raw-A extractor

24 October 2026. Repository read-only. New author result for the parallel
native-Y continuation; no new premise adoption or full-instrument claim.

## Outcome

A five-tick gadget of the unchanged lattice rule transfers an arbitrary raw
A operand into a clean whole-cell code `(0,A,0)`. It accepts every input triple,
not only the three native-Y codes. Its input appears at one initial site; its
three constant sources and ready workspace are independent of that input.
The complete receiver prefix is blank. Global reversibility retains the
unreturned information elsewhere in the two-slice phase.

This is a genuine native gadget **conditional on a supplied localized input
socket and initially clean finite workspace**. It is not yet a native loading
construction from the actual late q2 phase. The proposed direct splice has a
specific dirty previous-slice coordinate, so that gap cannot be hidden by
relabeling the encounter time as a fresh initialization.

## Exact construction

Use the unchanged rule

    U_(t+1)(v) = U_(t-1)(v) XOR H(XOR of its six neighbours at t),
    H(A,B,D) = (B,D,A XOR BD).

The following coordinates are local gadget coordinates, not absolute coordinates
of the existing giant apparatus. At the gadget's tick zero, set:

| Site | Current triple |
|---|---|
| (0,0,0) | Q=(A,B,D), arbitrary and unknown |
| (0,1,-1) | 010 |
| (1,1,-2) | 111 |
| (8,2,0) | 010 |

Let the receiver be r=(3,2,0). Set every other current coordinate in the
Manhattan ball B_5(r) to zero, and every previous-slice coordinate in B_4(r)
to zero. All exterior coordinates can be arbitrary. In particular, the old
triple at the unknown input site is outside B_4(r) and is not silently erased.
Take a sufficiently large torus with no wrapping in these cones; L=15 is used
in the complete-lattice checks.

Then, for every Q:

    U_t(r)=000 for 0<=t<5,
    U_5(r)=(0,A,0).

On Q=(y,y,1 XOR xy), the output is exactly `(0,y,0)`. Replacing only the input
A by diagnostic p, while keeping B and D fixed, produces `(0,p,0)` for every
assignment. There is no reliance on the native coincidence A=B. The intervention
is a test, not an operation performed in native runs.

The clean operand is in B, which is the incoming operand field used by the
older localized X-reset construction. This observation does not by itself
compose that reset: its timing, prior, workspace and remaining fields still
need a joint construction.

## Proof and finite certificate

All four current sources lie exactly on the receiver's radius-five boundary.
The previous slice inside radius four is zero. Finite speed makes the receiver
prefix blank and reduces the first-arrival calculation to an inward sweep of
successive Manhattan shells. At each shell, only outward neighbours can have
received a source; inward neighbours, the older local slice and all other
contributions are still zero at the relevant first-arrival time.

First omit the correcting source at (8,2,0). The eight-input Boolean certificate
for the two other constant sources gives, immediately before the receiver's
last H:

    XOR of arriving neighbours = (1,0,A),
    receiver = H(1,0,A) = (0,A,1).

`checks.py` computes this twice: once by the original three-dimensional,
second-order recursion, and once by a separate first-arrival shell sweep. It
exhausts all eight triples Q, so the displayed identity is independent of B,D.
This small exhaustive truth table, together with the exact finite-speed
reduction, is a complete finite certificate of this conditional statement.
It is not a Lean formalization.

The correcting source (8,2,0) is distance ten from each other nonzero source.
It therefore cannot interact with them before tick five, and its unique axial
shortest path reaches the receiver at that tick. Before the last H it contributes

    H^4(010)=100.

This flips `(1,0,A)` to `(0,0,A)`, giving the claimed `(0,A,0)`.

No input copy is prepared. The unknown Q occurs once. The full global update
is reversible, with inverse

    U_(t-1)(v)=U_(t+1)(v) XOR H(XOR of its six neighbours at t).

Consequently extracting one component into a clean receiver does not erase the
other components. They remain distinguishable in the rest of the complete
phase. The check reverses all five full-torus steps and recovers every initial
bit. This does not identify a single reusable garbage register or show that
the workspace returns to its initial ready state. A reusable device needs
that additional accounting.

## Resource and record scope

The current and previous ready balls have 231 and 129 sites. There are 1080 raw
bits in those two-slice regions, of which three are the free unknown Q. Thus
this construction fixes 1077 apparatus bits, including its three constant
triples. These constraints are independent of Q. No optimality, preparation
mechanism, thermodynamic interpretation or fair-frontier compatibility is
claimed.

The theorem exposes the whole receiver triple at every tick through five.
That word contains only the selected A at the endpoint, with a blank prefix.
It does not control other spatial probes, other instruments' public ports,
the receiver after five, or an outgoing multi-sign carrier. No clock, shutter,
indefinite access closure or reset herald is supplied here.

## Concrete late-loading obstruction

A direct translation of this gadget to the existing raw-Y input q2 at encounter
time R+2 would place its receiver at q2+(3,2,0), at time R+7. Its old-slice
readiness requires the triple at q2+(1,0,0), time R+1, to be zero: that point
is distance four from the proposed receiver.

The retained actual-parameter native-Y calculation instead gives, for all
sixteen x,u,mY,mR assignments,

    U_(R+1)(q2+e_x)=(0,1 XOR u XOR mY,mY).

It is zero only when mY=0 and u=1. Conditioning on this late event would
restrict the reset sample u; it is not an input-independent clean socket.
It is not permissible simply to blank the triple during evolution.

A controlled dirty-socket test shows why this hypothesis matters. With raw
Q=001, the clean gadget outputs 000. Change only the old triple at (1,0,0)
to 010 and it outputs 010 instead. The actual native history x=u=mY=mR=0 has
precisely that raw Q and that dirty old neighbour. The test leaves all other
gadget coordinates clean; it is not a simulation of the full actual late
apparatus, and does not prove that every possible enlarged integration fails.
It proves that this conditional gadget cannot be spliced by ignoring its
readiness hypotheses.

The actual sidecar carrying x, found by the history-control avenue, may be
useful in a different coupled design. No such correction is included here.

## A discriminating rejected shortcut

There is an even smaller two-tick identity: Q at the origin and constant 001
at (2,0,0), with its own clean ready cone, produce `(0,B,0)` at (1,1,0). Indeed,

    H(H(Q XOR 001) XOR H(Q) XOR H(001)) = (0,B,0).

This agrees with y on every unmodified native code because A=B=y. It fails
the A-only diagnostic when A and B differ. The checker retains that failure
as a countercontrol. The five-tick construction was chosen because it transfers
the actual A operand, not merely a correlated native copy.

## Checks and reproduction

Run from any working directory:

    python3 parallel_v3/aux_routing/checks.py
    python3 -O parallel_v3/aux_routing/checks.py

Normal and optimized outputs are byte-identical. Checks use the standard library:

- All eight Q inputs: exact original-rule recursion versus shell calculation;
  blank prefix; complete endpoint triple and uncorrected-stage certificate.
- Four native histories and eight A-only diagnostic interventions.
- Source distances, one occurrence of unknown Q and exact readiness count.
- Complete 15^3 periodic lattices under two dense exterior assignments, all eight
  packed Q values, every receiver tick, and exact reversal of the full phase.
- All sixteen actual old-neighbour formulas, using the retained giant-deadline
  recurrence; the concrete dirty-socket countercontrol.
- The two-tick B-copy rejected by the actual-A diagnostic.

The copied `core_from_v1.py` is byte-identical to the accepted handoff core;
its hash is recorded in PROVENANCE.json. It is used only for the actual late
neighbour calculation. The five-tick construction and two native simulation
implementations do not use that imported core.

The gadget was found by an exploratory short source search. No external
preregistration, independent acceptance, minimum-resource theorem or global
composition certification is claimed. C++ search source is retained for
provenance; replay and acceptance do not require a C++ compiler.

## Next test

Treat the five-tick gadget as a concrete loading target, not as a finished
reset interface. Either construct its ready input phase from the actual q2
history without changing the allowed prior, or synthesize a tolerant variant
using the actual nearby phase—including the native x sidecar. Any successful
integration must preserve the earlier instrument's record law and reserved
frontier resources, and still supply the native Y reset and its full joint law.
