# Reversible acceptance and complete pointer contract

24 October 2026. Research under #912, starting from
`fe8f0363c99064038763a20e4cef9051f1ac7408`. Native source and phase
hypotheses are those of #910 Native A, author
`f24a57a7c23cc1818c04265cec7604f8bc2f410d`. No observer access, native
compilation, operational map or premise is adopted. #885 is read-only.

## Fixed question and construction class

Can an explicit NOT/CNOT/Toffoli circuit, acting on the actual seven-site
phase wires as logical inputs, reversibly write the intended acceptance
bit into a whole public three-bit pointer while returning all its temporary
workspace to its initial state and preserving the complete selected carrier
law? This is an abstract gate-level positive control and a specification
for native compilation, not a claim of available native gates.

The immutable input is current V plus its six previous neighbors, with
Q8=(b0,b1,b2), Q10=(b3,b4,b5). Compute

    s=V.B XOR XOR(previous neighbor.D),
    a=b1 XOR s, b=b5 XOR s, K=b0+2*b2+4*b3,
    A=[K<n(a,b)], n(00,01,10,11)=(5,0,4,1).

Use the disjoint Boolean partition

    A=(not b and not k2)
      XOR (not a and not b and k2 and not k1 and not k0)
      XOR (a and b and not k2 and not k1 and not k0).

Compute/copy/uncompute uses only explicitly listed elementary reversible
gates. Count every clean bit, initially fair padding bit and gate tick.
Store A in the pointer B wire; its A/D wires are two separately preloaded
fair bits. Internal workspace is not publicly accessible under this candidate
contract. It remains part of the complete physical state and is restored.
The raw pointer is read at every elementary gate tick, including prefix,
copy and uncomputation. All gate counts and exposure times are fixed, and
no branch-dependent stopping is permitted.

## Frozen decision rule and controls

A positive result requires all of the following, with explicit failures
before any successful verdict:

1. Every input of the relevant exact Boolean truth table agrees with the
   independently evaluated threshold comparison; the gate list has an
   explicit inverse on arbitrary full register states.
2. Initially clean workspace is restored and every phase input is restored.
   Elementary decomposition of each multiple-control gate is independently
   checked, including a broken-control mutant.
3. On the Native A conditional source law, compare every whole raw pointer
   history jointly with old records, flags and outgoing selected carrier.
   Retain all rejected physical states and all zero-mass target cells;
   earlier terminal failures never offer a carrier.
4. An independent non-gate kernel evaluation gives the same accepted 5:4:1
   carrier, fair Z and success/failure law. Every accepted raw-pointer
   posterior has the stipulated positive X-state decoder.
5. Workspace or pool-key exposure, padding reuse across two accepted
   operations, omitted uncomputation and an unrelated correct-rate flag are
   countercontrols. Quantify the actual leak or error without presuming
   every mutant must produce a nonpositive decoder.
6. A delayed-coupling control must detect a changed carrier if uncontrolled
   dynamics alters it during the circuit: storage/isolation is an explicit
   supplied gate-level assumption, not inferred from reversibility.

The checker uses Python standard-library exact integers and fractions;
normal and optimized output must match deterministic result.json. Written
conditional proofs are separate from exhaustive bounded checks. Sources,
command, hashes and open native delay/access/clock/availability obligations
are retained. No full A1/A2 equivalence, universal native no-go, merge,
special dispatch or formal certification follows.
