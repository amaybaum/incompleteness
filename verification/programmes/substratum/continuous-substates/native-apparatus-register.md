# A previous-shell apparatus register: native coupling and a preparation obstruction

Research input and accepted selector baseline:
`53bf7ac8d56dfeacbc23cfa5d37604be6ccc6ae8`. This is a separate bounded
construction attempt inside SUBSTATE-1, not a revision of that acceptance.
Independent review of this unit is pending. The objective remains two
physically selectable native interactions on the same prepared42-bit packet.
No new source, pin, read, reset, preparation or physical operation is adopted.

## Candidate and bounded decision rule

Keep the native rule, actual v14 source law and accepted original-key prior.
Write q=(0,S,78), tau=L+3, and K_tau for both complete slices on B1(q).
Fix the apparatus location r=q+2e_y outside that packet. The simplest clean
program pair would have **identical complete current slices U_tau**, and
identical previous slices except for U_(tau-1)(r).A, which differs by1.
This specifies the same entire incoming packet pointwise, not merely its
marginal. Other B/D fields, the surrounding current slice and old-local
terms are held equal in this candidate. It is a proposed pair of native
initial preparations, not an authorized write into an evolved slice.

The decision rule is to test, in order: (1) an actual change in the native
interaction; (2) compatibility of both clean program states with the original
preparation; (3) physical selection and complete output admissibility.
A failed source check blocks this candidate; a difference of native outputs
alone cannot pass the gate. The tests retain the existing packet dictionary,
all residual fields, failures and environment. A hypothetical apparatus that
changes other fields belongs to a different candidate.

**Outcome:** the clean pair has a nonzero, background-independent native
effect, but its two states cannot both come from the specified preparation.
This establishes a preparation obstruction for this one-register design,
not a sourcing no-go for coordinated apparatus encodings or OI generally.

## Exact native coupling, with the complete residual output

For h(A,B,D)=(B,D,A XOR BD),

    h(z XOR (1,0,0)) XOR h(z) = (0,0,1).

Evolve each complete cut with the unchanged second-order native rule.
At tau+1 the only current-field difference is an A flip at r; the entire
previous slice is unchanged. K_(tau+1) is consequently identical.
At tau+2 the current difference consists of D flips at **all six neighbors
of r**, and the previous-slice difference is still the A flip at r.
Only r-e_y=q+e_y lies in B1(q). Thus the outgoing42-bit packet differs in
exactly that boundary D bit, with the other41 bits unchanged. Five further
current D flips and one previous A flip remain in the environment. No
residual B/D field or outgoing apparatus bit has been erased.

This is an exact difference of two native evolutions, for arbitrary dirty
backgrounds. It supplies a real microscopic coupling conditional on the
clean program states existing. It does not yet supply a preparation or a
physical way for the embedded observer to select those states.

## Pulling the clean register back to the actual sources

Invert the same native rule:

    U_(t-1)(v) = U_(t+1)(v) XOR h(XOR_(w~v) U_t(w)).

Start from the proposed cut pair. Its initial difference is at r in
U_(tau-1). On the outermost backward axial front, the old-local term and
the other five neighbors have not yet been reached. Each backward step
therefore applies h with XOR translations to the differing triple.
Since h is bijective, that front difference cannot vanish, in any fixed
background. The path along -e_y is unique. At original time0 it reaches

    k = r-(tau-1)e_y = q-L e_y = (0,-77,78).

Both preparations would have to differ at this original **current** cell.
But its distance from q is L, strictly inside the q10 ready ball of radius
L+1. It is not one of the1479 old sources or the four added source sites;
in particular it is one cell inside the added E source at (0,-78,78).
The retained preparation fixes this cell, so the proposed pair is
incompatible with that preparation. This is a pointwise obstruction,
independent of the complement probability law or a proposed readout.

The same check in each of the six lattice directions uses r=q+2d and
k=q-Ld. Every such forced cell has ready margin -1 and no source exception.
The torus is too large for wrapping to shorten these axial fronts.
This excludes only the stated clean single-register pair. Extra correlated
apparatus changes could cancel the backward front; they must be constructed
and checked rather than assumed absent or assumed available.

## Operational kernel, records, environment and failures

The accepted passive kernel remains valid. In its two-step window, any
change of the complementary original law C that preserves the fixed source
family and the conditional product-uniform law of its28 future triples
still gives the same packet/raw-record formula at each fixed input and
positive-mass past. A setting in C alone cannot distinguish those kernels.
This follows from the accepted source-by-source triangular bijection;
it is not a new universal theorem about all apparatus or access menus.
The source compatibility test above fails before any admissible controlled
kernel or selection procedure for this register pair has been established.

Equal packet marginals alone would also be an insufficient rejection of
physical control. A native local countercontrol makes the distinction
explicit: for independently uniform p and z, compare

    Y_a = p XOR h(z XOR (a,0,0)).

Each Y_a is uniform, while the two complete joint laws (p,z,Y_a) have
disjoint supports, hence TV1. The mask p,z is retained as a mathematical
reference in this control, not granted as a new observer read or adopted
as the actual packet-environment prior. A physical later interaction might
use such correlations; no private inverse is supplied here. Neither the
equal passive marginals nor this countercontrol proves a selectable gate.

All existing raw public triples, flags and timing stay in the record W.
The nearby r and packet fields remain private. No register read, new flag,
success filter or probability of physical success is defined. On earlier
terminal branches there is no attempted apparatus read or offered carrier;
already recorded data remain, and the microscopic fields continue evolving.
For a valid apparatus the outgoing state must be the full native
pushforward, including the five exterior D changes and previous A change
in this calculation, with no reset. Because no admissible pair was sourced,
consumption by a subsequent native stage is not an operational reuse result.
Native evolution of a hypothetical cut by itself does not pass that gate.

## Reproduction, evidence and next construction

From this directory:

    python3 -I -B native_apparatus_register_probe.py
    python3 -I -B -O native_apparatus_register_probe.py

The deterministic probe checks the actual1479-source inventory by its
retained hash, the enormous-parameter readiness geometry and all six
directions. Independent of the source engines, it recursively evolves
dirty complete local native cones in both time directions. Forward tests
check the incoming/first/second packets and all changes in a radius-four
patch containing the full two-step support. Backward first-arrival tests
vary each complete register triple through all eight values. The forward
rule is also checked on the reconstructed negative-time fields; three
independently indexed finite periodic two-slice inverse roundtrips pass.
These are
bounded implementation controls for the written all-background proof,
not astronomical-scale simulations or Lean certification. Explicit runtime
checks remain active with optimization. A local full-joint countercontrol
and terminal no-read check prevent marginal-only or post-failure acceptance.
Normal/optimized output is identical:36 forward native worlds,288 backward
native worlds, six actual-scale pinned-cell witnesses and three periodic
inverse roundtrips, with verdict `CLEAN_REGISTER_PAIR_VIOLATES_PREPARATION`.
Six focused mutation classes reject with VOID/exit2 in both modes: dropped
forward old-local term, dropped backward old-local term, displaced backward
front, wrong outgoing field, marginalized dirty mask, and post-terminal read.

Sources are the retained shared_v12 interface, native_route_v13 geometry,
native_vread_v15 preparation/access inventory, the accepted conditional
packet-kernel proof and the accepted selector report. The preparation
obstruction is conditional on the declared source/ready inventory being
complete, as in those sources. It does not change their accepted scopes.

The constructive next obligation is a **coordinated original-time apparatus
encoding** whose two settings preserve the input42-bit carrier and the
fixed ready/source conditions while producing an actual native coupling.
It must avoid the forced pinned-cell change demonstrated here, provide a
physical selection procedure, and retain the full packet/environment and
record kernel for reuse. A single cut-time register toggle, a mathematical
pullback without the source check, or another random label cannot supply it.
No manuscript change, claim upgrade, F/E designation, special dispatch,
readiness change or merge follows from this unit.
