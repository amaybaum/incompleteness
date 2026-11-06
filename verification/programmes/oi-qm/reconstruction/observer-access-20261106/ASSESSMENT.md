# Preparation and readout from one local receiving interaction

**WIP / UNVERIFIED — paper-only source assessment.**
Accountable issue #866; whole-model objective #1169; guiding draft #1173.
[Owner scope](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6695164378).
Main source snapshot: `f49b768709d262a05471895cec703b31aff19b57`.
The preceding bridge paper and B1/B2/B3 stay unchanged.

## Candidate and physical motivation

Screen one local receiving site coupled to an adjacent signal site by the
existing finite two-slice nearest-neighbor reference wave rule,

    f_(t+1)(i) = sum_(j adjacent i) f_t(j) - f_(t-1)(i) mod q.

Use a three-dimensional periodic cubic graph with side length L at least 5,
alphabet Z/qZ with q at least 2, one neighboring pair s,d, and the complete
current/previous field as the world state. The candidate interaction is the
existing bidirectional graph coupling. It is chosen because it already
transfers neighbor information under the declared reference dynamics, without
adding a quantum measurement instruction or replacing the finite rule by its
real/complex observer-level lift.

A proposed local observer has both time-slice coordinates at d. This is a
declared mathematical observer choice, whose laboratory interpretation must
be sourced; a component hidden from that observer cannot simply be erased
from the world. A fixed report of its visible data is a separate interface
choice. No available record or later read may be dropped to obtain agreement.

## Questions and controls

Trace the sources of three assumptions: exact laboratory preparation,
selectable composed control, and readable sign/other discriminating output.
Keep a mathematical initial condition separate from a preparation mechanism;
keep a visible-coordinate map separate from a physical detector and persistent
record. Main's conditional law and selected measure are to be read on their
actual scope, including the open laboratory-preparation bridge.

For this one receiver derive the native update, its dependence on the signal
and other incoming fields, the full local two-slice output, and the carrier's
state change. Compare a known incoming background with a hidden randomized
background under explicitly stated laws. Account for any later access to
that background and for the actual unmodified subsequent dynamics.

The inherited benchmarks are B3's fixed qubit-instrument histories and the
bridge paper's perfect-distinguishability test. State which native procedures,
preparation laws and fixed labels are required even to apply them. A finite
classical copy, complete masking, or a new report relabelling is not itself
a full quantum reconstruction.

## Source and stopping boundary

Read Main, Substratum, SM, the formal operational interface and the relevant
retained coupling/access/preparation research. Reuse existing mathematics.
The observer-probability work on #1110 retains its writer and files.
Its H-PREP ruling is an open hypothesis, not an available loading mechanism.

If a required preparation/access restriction or physical realization map has
no source in the assessed branch, name the exact missing input and stop this
candidate. No replacement candidate, fitted law, inaccessible-reservoir
assumption or altered quantum target is introduced to rescue a comparison.
Any conditional hand calculation must carry all of its input assumptions.

The completed paper will receive independent review at its pushed exact head.
This checkpoint is not a scientific execution preregistration, freeze or
authorization to run a model. No new code, CAS, simulation, enumeration,
Lean build, physical experiment, manuscript change, premise adoption or merge
is part of the unit. Ordinary automatic PR CI is separate.
