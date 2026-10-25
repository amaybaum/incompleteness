# Composition and access: current research handoff

This directory holds a conditional finite-depth composition theorem and its
applications to the native constructions of
`../native-y-continuation-20261024/`. Its results are internally reviewed
research. None establishes a native gate, native storage, an observer-access
rule, a reusable instrument or full OI-to-QM equivalence. `README.md` lists
the packages, their plans and reviews, the replay commands and the
provenance of the inputs.

## Explicit logical acceptance circuit

`composition_flag_v6/`, author `1cb224db6c17e083849a0f82768e991beac39399`,
has an accepting separate-engine internal review retained beside it. It is a
conditional compiler target, not an implemented native gate, adopted observer
access or full quantum instrument.

The inputs are the actual 21 phase wires: current V and its six previous
native neighbours, including Q8 and Q10. The fixed local inverse supplies s.
The circuit computes A=[K<n(Y XOR s,R XOR s)] for thresholds (5,0,4,1) with
NOT, CNOT and Toffoli gates, copies A into the public flag B, then
uncomputes the temporary wires. Every phase bit and all seven clean
temporary bits are restored.

The core has 89 logical ticks: 30 Toffoli, 36 NOT and 23 CNOT. Its 31
register bits are the existing 21, seven clean temporaries, one clean flag
and two initially fair unused pointer fields. This chosen three-field public
channel is read at every tick. Its complete 90-sample prefix is
(padA,0,padD) through tick 44 and (padA,A,padD) from tick 45. All branches
have the same schedule.

An optional explicit 90-sample record-bank dilation uses 270 additional
clean bits and 270 copying CNOTs: 301 register bits, 359 logical ticks and a
360-sample whole-pointer prefix. The added copies retain, rather than erase,
the public record. These are explicit upper bounds, not minimal costs or
native or autonomous clock implementations.

## Conditional complete law

Native A's inherited initial-source theorem makes (Q8,Q10,M) uniform on 512
values conditional on the remaining initial variables. OldP=p and the XOR of
the other three neighbours are then fixed; V=p XOR H(sum of neighbours).
The circuit's full raw pointer history, V, old record and selected carrier
are checked jointly, with all rejected physical fields, zero cells and
parent terminal guards. Every accepted whole-record posterior has the
correct 5:4:1 post-X mask law, fair Z and the positive X-state decoder.

The checker exhausts 32,768 conditional phase worlds, 131,072 padded worlds,
65,536 selected cells and 1,024 valid accepted raw-record posteriors. Gate
truth tables, arbitrary-dirty global inverses, optional recording and a
separate threshold and kernel engine are additional controls. The written
bijection and conditional-kernel proofs are separate from the bounded
enumeration and from the inherited actual-scale source theorem.

## What the circuit assumes

Logical phase storage, scheduled gates, pointer coupling, a fixed clock and
workspace isolation are supplied. The evolving native field has not been
shown to implement them. Native masks and garbage are physical state;
uncomputing them later does not remove an earlier public leak.

The countercontrols show that revealing the private M or key fields gives
negative fixed-decoder posteriors (minimum determinant −1/18), and revealing
the temporary a gives determinant −1/4. Omitting uncomputation fails the
chosen clean-workspace boundary. A flag with the right rate but independent
of the pool has complete offered-carrier error 1/8. Reusing unused pads
gives TV 3/4 against the chosen independent-noise reference only; a
separately specified correlated public-noise convention can remain
admissible.

A small original-time native one-tick control changes the old sign and the
pool code if the same phase formula is reused after uncontrolled evolution,
so logical input restoration proves no native storage theorem. A
hypothetical serial one-gate-per-native-tick core from L+2 finishes at L+91,
after F8's first old-receiver arrival at L+77 and F10/F9's at L+79; the
optional recorded dilation would finish at L+361. Neither timing is an
established native runtime or a lower bound for a parallel compiler.

## Delayed old-port history for the frozen carrier

`delayed_history_v7/` (plan `d72ea524586b84e285c4723bf47a377df3ecb8a9`,
committed before computation; reviewed head
`656502989dd34ef64ba63d54328e13966517444b`; separate reviews under its
`review/`) treats those arrivals for the frozen logical v6 carrier within the
same hypothetical serial alignment. Conditional on the Native A source
contract, the supplied `history_v11` bank and G priors, v6's isolated logical
storage and v6's candidate access contract with the eight old ports added,
the complete public record through any L < H <= 2L is distributed jointly
with the outgoing selected carrier as the v6 law tensored with an
independent uniform tail of 24(H−L) bits. The public record is the eight raw
port streams, the old whole-q9 record, the single whole-V record and the
pointer prefix; Q8, Q10, M, the other neighbours, the pool and the phase and
workspace wires are private.

At actual L this is a written conditional corollary of exact integer
geometry (no tail triple reaches a carrier site-time, minimum slack 76; G
reaches no port by L+2; both horizons lie within 2L) and the inherited
Native A and `history_v11` results. The exhaustive check of the complete
joint law, cell by cell with zero cells, is a scaled control (n=3, k=2) and
does not establish the actual-L statement: there G reaches a single port,
whereas at actual L F8 and F10/F9 each reach ports 3 and 5 at the same tick,
and its horizon, 8, exceeds 2n. Tail triples first reach the carrier sites
from L+77, so a natively stored carrier could depend on them; in the scaled
control, q8 left to native dynamics does. The result concerns the joint
record law only: it adopts no observer-access rule or access closure and
establishes no native storage, arbitrary composition or reusable measurement
instrument.

## Passive native readout as the acceptance flag

`native_predicate_v8/` (plan `631bec0ca55eacbf6a7cf7e72d72c673dfe430da`,
committed before computation; reviewed head
`fc452ea825b986a3babab5d110626e0019c39847`; separate reviews under its
`review/`) tests passive readout, the cheapest form of a native predicate
replacing the circuit's flag, in class C(4, 16): v6's public contract with
the pointer replaced by the whole raw triples of any set of native
site-times within Manhattan distance 4 of q9, read through L+17, with no
gate, pad or added source, and any predicate of that record as the flag.
Conditional on the complement C0, the complete v6 law requires the record to
split every V value's 64 worlds into exactly two blocks, one with exactly
the accepted target counts (20 worlds) and one with exactly the rejected
target counts (44). In the scaled control (n = 6, sixteen dirty old-success
families, 3,225 read site-times each) no read set gives such a split for any
V value in any family: `NEGATIVE_FOR_CONSTRUCTION` for that class, in the
scaled control. There the operands are delivered; once G arrives a native
cell almost always carries more than one bit of pool information given V.

This does not exclude native predicates with fresh pads, prepared sources, a
different source family or gates, larger regions or later reads, a law that
holds only on average over private backgrounds (with fresh pads, one open
branch, since conditioning on C0 is what stops background bits acting as
fair pads), or a predicate at actual L in its actual background. It adopts
no access rule and leaves the carrier in v6's supplied logical storage.

## Earlier packages

The top-level conditional composition theorem, `native-x-v2/`,
`tagged-post-y-v3/`, `native-phase-v4/` and `native-coupling-v5/` state
their results and scope in their own `REPORT.md`; `README.md` indexes them.
v6 builds on v5's conditional code/metadata law.

## Open gates

The next gate is native compilation or a cheaper native predicate, for
example a native readout masked by fresh pads, with actual operand delivery,
a preserved or re-encoded carrier, full pointer metadata and complete delayed
history for a natively stored carrier. Native construction is in
`../native-y-continuation-20261024/` (#910); general instruments,
composites and Bell, and full A1/A2 reconstruction are tracked in Issue
#913.
