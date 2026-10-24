# States and dynamics: current research handoff

24 October 2026. #911 records two distinct mathematical paths: an exact
single-qubit architecture comparison and a finite approximation with explicit
error/resources. Neither is an adopted OI operational map, native availability
proof, probability-selection principle or full equivalence. #885 is read-only
for this effort. A1 and A2 keep separate targets and verdicts.

## Exact architecture comparison

`history-architecture-v5/`, author
`51d8956100cf76d24b6810f1853c9f714f596c35`, is a credited positive control
using the known Kochen-Specker qubit sphere model. The accepting separate-agent
internal review is retained at `988d090d0901f9369b644bda4361ea1af003073e`.

The hidden point lambda lies on the unit sphere. A pure preparation n has
density (n dot lambda)_+/pi; measurement reports sign(a dot lambda), rotations
move lambda geometrically, and a fresh reset prepares the measured eigenstate
density. A fixed moment decoder is positive on the specified mixture cone.
An independent hemisphere integral gives the Born law. The model represents
every one-qubit state and unitary rotation, and its finite adaptive rank-one
projective records/outgoing states agree jointly with the quantum reference.

It passes the earlier rational non-Clifford test without giving the apparatus
an unknown preparation label. Its hidden input distributions differ from
the old eight-sign encoding, so the old distinguishability obstruction does
not transfer. The model and its quantum reproduction are prior work; novelty
is not claimed. The report and review derive the interface and controls anew.

The continuum prior, exact rotation/reset primitives, independent initial
uniforms, blank registers, fixed clock and private-memory isolation are
supplied assumptions. The reversible dilation retains old information but
does not implement it under the native lattice rule. Reset, workspace, seed
access and timing controls show that the restrictions are load-bearing.
General POVMs/instruments, native sourcing and composites remain open.

## Finite A2 controller and fixed-decoder bound

`finite-a2-v5/`, revised author
`dbfaa3c68003bfd5335353829c18cf6f21d300c4`, discretizes the same geometric
interface for specified finite rational preparation, rotation and projective
menus and one total budget of h adaptive operations. Six cube-face grids give
N=6M^2 labels; rational integer weights and fixed B-bit CDF samplers avoid
tables of quantum protocol answers. The actual finite controller uses its
hidden index, stored rotation word and declared setting, not an external
unknown preparation label.

One inward moment decoder is positive on the preparation/reset/rotation
phase cones. With the report's explicit kappa and chi, the complete public
record plus decoded outgoing state differs from the quantum protocol begun
at the decoded input by at most

    min(1,h*kappa+2chi)
      <= min(1,(52h+300)/M+(8h+48)/2^W+(h+6)(6M^2-1)/2^B).

This is a written uniform bound, not extrapolation from small-grid tests.
At clock t only h-t operations remain; measurement clears the word but does
not reset the clock or reserved-bit budget. All (h+1)B random bits are supplied
initially, with dyadic preparation-mixture bits counted separately.

The conservative h=3, epsilon=0.1 certificate uses M=13680, W=12, B=39:
156 initially fair bits and 1,122,854,400 grid labels, plus deterministic
tables, clock, word and retained workspace costs. The large grid is not
executed and efficiency is not claimed. A fixed padded finite-circuit clock
is supplied; the Python evaluator is not constant-time native hardware.

The separate review checks the geometry/floor/CDF bounds, positive decoder,
branchwise CQ proof, initial-decoding correction and clock/word scope.
Its independent implementation matches the author on 128 adaptive cases
and 672 leaf records, exhausts 1,024 small-sampler seeds, detects reuse,
adaptive-choice, insufficient-bank and access/timing controls, and verifies
three nonvacuous symbolic resource certificates. Clipped bounds on tiny smoke
grids can be vacuous and are not represented as proof of the asymptotic law.

## Cross-track calibration and common-code bridge

The integration probe `native-code-bridge-v6/`, author
`0449d85910aed0f838b629ee683061ce9960cc2d`, relates the native targets to
the geometric model directly. For post-X and post-Y eigenstate preparations,
the sphere's X/Y/R/Z sign projection gives exactly the native 5:4:1 and
5:3:2 full code measures with fair Z. This is a state-calibration relation;
no underlying sphere or native operation lift is inferred.

A common autonomous twelve-code input interface is still too coarse for a
broader read. Its +X/+Y source pair has TV 1/2 while the rational direction
(3/5,-4/5,0) has quantum record TV 7/10. A common independent continuation
therefore has worst-pair record error at least 1/10, attained by an explicit
stochastic pair control. The continuous model resolves points within the
same code cell and implements the read. This conditional bound does not
exclude the actual native full boundary, past/phase tags or response memory;
all such information must be included before applying data processing.

The useful bridge constraint is explicit: keeping only the selected signs
cannot establish universal autonomous operation coverage. Additional physical
response information or a changed/larger encoding is needed. No general
OI/A2 bound, full-channel minimax or kernel/native lift is claimed. Separate
review is retained with the bridge package.

## Retained obstructions and next gates

The earlier eight-sign 1/15 and product-section 2/15 pair bounds remain valid
for their own maps, input priors and common-controller contracts. Neither is
a general OI/A2 bound. The earlier almost-sure sampler audit also remains
unchanged: a mathematical source or representation alone is not physical
operation availability.

The next architecture gate is the bridge from actual native carriers,
resources and permitted reads to an operational interface with this coverage.
The cosine prior, reset, settings/clock and private-access restrictions still
need a physical source or explicitly justified added condition. The finite
A2 result is conditional reproduction, not Emergence or full A2 reconstruction.
Composites, Bell structure, general instruments and full A1 coverage remain
separate obligations.

All six new author/reviewer groups replay normally and with -O against
retained structured output. Proofs, finite checks, internal review and
formal certification remain distinct. No full suite, Lean certificate or
exact-head CI attestation is claimed. #910 owns native construction, #912
composition/access, and [#913](https://github.com/amaybaum/incompleteness/issues/913)
the broader inactive gates. No merge, dispatch or F/E designation follows.
