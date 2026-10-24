# Conditional compatibility of source, bit transport, and detector logic

Independent read-only investigation, 2026-10-23. No repository changes,
comments, commits, pushes or workflow launches. This is exploratory finite
mathematics, not a preregistered quantum-equivalence acceptance test.

## Result and scope

The repaired three-field update from the preceding handoff supports, under
one explicit conditioned uniform prior:

1. Two separated, preloaded classical bits reaching a detector.
2. A raw detector bit equal to their AND when they meet.
3. A spatially separated source port producing independent fair symbols,
   even with the earlier records of both ports available.

The full bounded record law is derived below and checked exactly. Crucially,
the initial detector region is blank: the inputs' product is not preloaded.
The readiness event fixes raw bits to zero; it needs no hidden initial product
correlation in that region.

This meets the three functional requirements at the level of binary signals
in a deliberately chosen apparatus. It does not produce a localized particle,
an isotropic angular emitter, a physical clock, a measurement reset, or the
four quantum preparation identities. The update, ready resources and access
interface remain supplied. It is not an OI selection theorem.

## Report14 reconciliation

I read [report14 and its checker at 9d866686](https://github.com/amaybaum/incompleteness/tree/9d866686cdb7f65fb4e33e5328d3475dd553369d/verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/owner-checks/report14).
It reviews the older detector-boundary handoff. The later scalar census and
joint-readiness handoffs were not the subject of that review. This continuation
does not claim to have independently rerun all of report14's K1-K3 checks.

One evidentiary distinction in K4 matters. The code measures maximum toroidal
L1 distance from the origin; it does not test membership in the initial block.
Distance at most three alone would not prove confinement in {0,1}^3: for
example (-1,0,0) lies outside that block and has distance one. Nevertheless,
the actual majority rule has a stronger exact property than the probe asserts.

**Box-invariance theorem.** Suppose both initial fields of the second-order
pair-parity majority rule vanish outside a Cartesian box B. Then every future
field vanishes outside B.

**Proof.** At a site outside B, choose a coordinate lying outside its interval.
Neighbors displaced along the other two axes still lie outside B and are zero.
Only the opposite pair on the chosen axis can be nonzero. Majority of the
three pair parities therefore vanishes. The site's old bit is also zero, so
the next bit is zero. Induct on the two field slices. The argument also works
on a torus for a Cartesian product of coordinate subsets. QED.

The checker independently tests the 12 possible single-axis boundary patterns
and directly checks block membership in all 184 of the review's initial-pattern
cases through eight ticks. Thus finite zero-background excitations of this
rule cannot propagate beyond their initial bounding box at *any* time. This
does not cover perturbations on a nonzero random background.

Minor numerical wording: K1's saved output gives a largest ratio 0.0008206.
The table's phrase 'never exceeds 0.0008' should therefore read approximately
0.00082, or use an upper value such as 0.00083. This does not affect the
analytical bound or the user's approximately 0.1% summary.

## Why a spreading disturbance is not enough

Under a uniform source prior, flipping a free source bit is a permutation of
the ensemble. In the repaired model, the local operation

    A_j <- A_j XOR message,
    D_j <- D_j XOR (message AND B_j)

preserves C_j=D_j XOR A_jB_j. If it preserves the ready ensemble and the A bit
is otherwise uniform, both message choices induce the same post-encoding
distribution. Any subsequent deterministic full record, or adaptive record
with independent protocol randomness, then has identical laws: TV=0.

This can coexist with a nonzero pointwise disturbance moving through the
wave. Disturbance propagation alone is not information transport. The argument
does not cover a receiver with an accessible pre-encoding reference or a
different, nonuniform encoding. The construction below instead transports
preloaded bits against a specified quiet background, and explicitly compares
their receiver-record laws.

## One fixed update

Use binary fields A, B, D on a cubic torus. Let S be the XOR of the six nearest
neighbors, and 'old' the preceding field slice. Use the already specified repair:

    A' = SA XOR A_old
    B' = SB XOR B_old
    D' = SD XOR D_old XOR S(AB) XOR (SA)(SB)
         XOR (SA)B_old XOR (SB)A_old.

This is autonomous, translation-invariant, cubic-invariant and local with
radius one in phase space. It is outside the original narrower componentwise
form F(current) XOR same-field-old, because D' also uses old A and B.

Set C=D XOR AB at each site and phase time. This is an involutive coordinate
change. Direct substitution gives C'=SC XOR C_old. Hence the whole update
is conjugate to three independent linear waves, with an explicit inverse.
This is an engineered choice of update; no OI premise selects it here.

## One prior and one readiness event

Choose a horizon K>=1 and side L=8K+1. The receiver is o=(0,0,0), and the
source port is q=(4K,0,0). The two payload locations are

    p_A=(K,0,0),    p_B=(0,K,0).

Let B_r(x) be the lattice L1 ball of radius r. Begin with uniform product
counting over all raw A,B,D bits at times -1 and 0. Condition on E_K:

| Initial registers | Constraint |
|---|---|
| Current A on B_K(o) except p_A | zero |
| Current B on B_K(o) except p_B | zero |
| Current D on B_K(o) | zero |
| Previous A,B,D on B_(K-1)(o) | zero |
| Previous and current A,B,D at q | zero |

Every unlisted raw bit remains independent and fair. In particular
a=A_(p_A)(0) and b=B_(p_B)(0) are independent preloaded payload bits. Their
conditional values define the four input preparations. This is one ensemble
with two free payload coordinates, not a change of prior between gate, source
and transport tests. No fresh resources are inserted during evolution.

With v_r=|B_r|=(4r^3+6r^2+8r+3)/3, the event fixes

    J_K = 3(v_K+v_(K-1)) + 4

independent zero bits. Its probability is 2^-J_K; at K=3, J_K=268. The rarity
is not hidden: this is a conditional ready apparatus, not a demonstrated
efficient preparation process. The phase-space bits outside the listed regions
are still uniformly distributed, not silently replaced by a vacuum.

On the receiver's initial current cone, A and B can be nonzero only at two
different sites, so AB=0 everywhere there. D is zero as well. Therefore C=0
on that entire current cone and on the previous cone. No product ab has been
written into the initial detector region. Away from constrained coordinates,
the pointwise map (A,B,D) -> (A,B,C) preserves independent uniform counting.

Recognizing, preparing, or waiting for E_K is not derived. In particular,
recording failed readiness checks while waiting would require a new conditional
law. The payloads are preloaded; an autonomous injection mechanism accepting
externally chosen message bits has not been constructed.

## Carrier and detector proof

For t<K, neither payload lies in the receiver's radius-t initial cone. All
initial source values in that cone are zero. Thus A_o(t)=B_o(t)=0.

At t=K, the unique extreme path from p_A to o has coefficient one in the A
wave, and the corresponding path from p_B has coefficient one in B. All
other receiver-cone inputs were fixed zero. Consequently

    A_o(K)=a,    B_o(K)=b.

The C field is initially zero on the receiver's two-time cone, so locality
gives C_o(t)=0 throughout 0<=t<=K. Since D=C XOR AB, the receiver's record is

    (A_o(t),B_o(t),D_o(t)) = (0,0,0),  1<=t<K,
    (A_o(K),B_o(K),D_o(K)) = (a,b,ab).

The two payload sites are 2K edges apart. They need K ticks to meet, and the
revised detector combines the arriving inputs at that time. The original
S(AB)-forced detector instead gives (1,1,0) for a=b=1 at this deadline; the
checker catches this control.

Distinct payload preparations have disjoint full receiver-record supports,
so their TV distance is one when the receiver reads A and B as specified.
Reading only D gives exactly the AND truth table. These are operationally
distinguishable transported bits, rather than merely paired-state differences.
They are wave signals with a known first-arrival tick, not localized particles
with an isotropic velocity law.

Freeing even one additional A background bit at (-K,0,0) masks the terminal
A read by an independent fair XOR. For b=1 the whole receiver record through
K then has identical laws for a=0 and a=1. This countercontrol makes the ready
background's role explicit.

## Source freshness and the complete joint record

The initial radius-K cones of o and q are disjoint: their distance is 4K.
Near q, the transformed A,B,C initial law is uniform product, with only its
own initial port pair fixed to zero in each field. The extreme-path argument
gives three independent fair source symbols at every tick through K, jointly
over the whole window. Their initial cones are disjoint from the payload and
receiver cones, so this law is independent of a,b and all receiver records.

At q the observed raw triple is (A,B,D)=(A,B,C XOR AB), a pointwise bijection
of that fair triple. Therefore each raw source triple is uniform on eight
values, independently over time. Earlier nonlinear raw D records do not spoil
this fact. Predictable passive calls at strictly increasing times inherit
the same freshness. Calls do not alter the dynamics.

Define the complete record for this specified interface to consist of the
readiness flag followed by both port triples at each tick 1,...,K. Given
E_K and a,b, its probability is

    P(source word=z, receiver word=r | E_K,a,b)
       = 8^-K * 1{r=((0,0,0),...,(0,0,0),(a,b,ab))}.

Without conditioning on the payload, each of the 4*8^K admissible records
has probability 1/(4*8^K). For a complete initial readiness-test protocol,
one may declare that a failed E_K terminates with just a failure flag; this
adds that branch with probability 1-2^-J_K. This specified interface is not
an access-closure theorem, and it does not model repeated readiness attempts.

These ticks are mathematical update counts. No physical clock register or
calibrated time-to-length conversion is obtained by writing t in the record.

## Checks and research consequence

The standalone standard-library checker implements the raw revised update
directly on cubic tori, rather than calculating the detector by decoding AB.
For K=3 it exhausts all 2048 assignments of the two payloads and nine source
frontier bits on a fixed-remainder slice. All 512 source words occur exactly
once for each payload, and every receiver word is the stated one. This is
an exact implementation control; the proof, not this restricted slice,
establishes the law under all remaining uniform initial bits.

Independent horizon controls K=1,...,8 check pulse arrival, product readout,
cone separation and readiness counts. The original detector rule, the freed
background bit, and the uniform-flip encoding are explicit countercontrols.
The majority-rule boundary proof and membership checks are separate code paths.

The checker completed normally and was copied to a separate temporary
directory. Normal and -O replays both reproduce the included output byte for
byte. Every computation in the checker is discrete and exact.

The status can now be stated more precisely than 'no one rule does all three':
there is a chosen local reversible rule and a single explicit readiness-
conditioned prior supporting fresh symbols, transport of preloaded classical
bits, and a nonlinear raw detector output. This is a bounded compatibility
construction, not an unrestricted apparatus or an OI derivation of its premises.

As established in the preceding handoff, the same conjugacy method can encode
arbitrary Boolean predicates. The remaining substantive targets are therefore
physical law selection, native preparation and timing, a specified angular
emission/readout map, and its full accessible records. No station-indexed
quantum preparations are defined here, so the four preparation-equivalence
identities cannot yet be claimed or tested. Composite behavior remains outside
scope, and numerical refinement of C-SPH-1 remains closed.

Provenance: this uses the revised rule proved in
`OI_joint_readiness_handoff_v1.zip`, SHA-256
`72ab080972b8124a575ada927f16a452c084f0c02abd9a7964499e0ccb04b576`.
The source, outputs and all readiness conditions needed for the present
checks are included here; the checker does not load that earlier archive.
