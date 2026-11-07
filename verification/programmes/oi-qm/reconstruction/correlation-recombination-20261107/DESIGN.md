# Native recombination of two hidden contributions

**Paper-only conditional source screen.** Accountable #866; parent #1169;
guiding draft #1173. [Owner activation](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6702826574)
covers one candidate, its physical preparation/access audit, full output
and continuation, classical controls and independent review. Review status
is recorded on the PR. Source snapshot:
`f49b768709d262a05471895cec703b31aff19b57`; preceding accepted head:
`e597b1e8d9f77a9d4818da8d0317d34f40aff13a`.

**Result.** In the existing finite reference wave rule, two individually
uniform hidden inputs can have a correlation that the native interaction
turns into a definite receiver value. Neither input is first read. The
complete state supports the next two native ticks, including return of
the same value to the receiver's current field. This is an exact
**conditional classical correlation effect**. Its correlated preparation,
ready region and laboratory access are not physically supplied by this
calculation, so it is not an available instrument or a quantum-coherence
result. The first source gate is the preparation operation in §5.

The point is to separate two questions: whether the native update can use
a hidden relation without a separate decoding device, and whether the
required preparation and observation protocol can be physically realized.
Direct hidden-memory readout is not made a requirement of #866.

## 1. One fixed native recombination and observation window

Use the finite reference branch on Lambda=(Z/LZ)^3, L>=9, alphabet F2.
Let A be the six-neighbor adjacency sum and use

    Phi(u,v) = (A u-v,u),
    Phi^-1(a,b) = (b,A b-a).

The minus signs retain the source convention; in F2 subtraction is XOR.
The coefficient one is the retained reference update, not a coefficient
derived from signal speed or a substitution for SM's normalized real lift.
No nonlinear Native A source law, B3 real-valued control, new graph edge
or measurement opcode is inserted. The packed C program is not executed;
its wave_step and wave_step_inverse equations are the source.

Choose receiver o=0 and inputs s+=e_x, s-=-e_x. Opposite nearest neighbors
give two paths to the same existing receiving sum, with reflection symmetry
and equal latency. This motivates the geometry before the output comparison.
L>=9 keeps the radius-three ball and walks through three ticks free of
wrap effects; no claim about arbitrary small tori is used.

The declared receiver sees its **whole two-slice local coordinate**

    R_t = (u_t(o),u_(t-1)(o)).

The registered experiment begins at t=0 and reads at t=0,1,2,3.
This is the same type of mathematical local receiver as the preceding
finite-wave source assessment. It is not a construction of a complete
embedded apparatus or proof that its clock/read interaction is available.
All earlier *registered receiver* data here are R_0. No arbitrary earlier
history or preparation log is erased or asserted equal. If a real
apparatus exposes the preparation label to this receiver, that record
must be included and the claimed common prefix rechecked (§5).

Reads in this reference law are passive projections of the evolving state.
A physically interacting detector is a further source obligation; it
cannot inherit this passive law without justification.

## 2. Correlated input laws and the exact preparation burden

Let B_r be the graph-distance ball of radius r about o. For b in {0,1},
define a mathematical conditional preparation mu_b as follows:

- draw Z uniformly from F2;
- set u(s+)=Z and u(s-)=Z XOR b;
- set u(x)=0 for x in B_3 other than s+,s-;
- set v(x)=0 for x in B_2;
- keep all remaining original coordinates C under one common law nu,
  independent of Z and b.

For the concrete baseline below, nu is the product-counting law on that
complement. No zero condition is imposed outside these two balls.
The remaining state is retained and continues to evolve.

For either b, each input alone is uniform. The joint input laws differ:

| b | Input pairs, each with probability 1/2 | R_0 |
| --- | --- | --- |
| 0 | (0,0), (1,1) | (0,0) |
| 1 | (0,1), (1,0) | (0,0) |

The encoded variable is the joint parity b. This is ordinary classical
correlation, not a phase or off-diagonal amplitude. Calling the two
contributions paths does not turn them into exclusive particle paths.

These distributions are legitimate conditional laws, but the source audit
does **not** establish both as available preparations on one apparatus.
Let nu_0 be uniform counting on the complete finite two-slice space.
Let E_b require the displayed zeros and u(s+) XOR u(s-)=b. Then

    mu_b = nu_0(. | E_b).

There are 63 current sites in B_3 and 25 previous sites in B_2:
the cubic distance shells have sizes 1,6,18,38. Thus 61+25=86 bits
are pinned to zero, and the two remaining bits obey one parity constraint.
Consequently

    nu_0(E_b)=2^-87.

Conditioning first on the common visible root R_0=(0,0) leaves event
mass 2^-85 within that rooted baseline. The two visible pins have then
already been counted.

This is a cost of conditioning in the chosen mathematical baseline,
**not** an apparatus success probability or a supplied herald. No
physical test of the hidden event E_b is available merely because the
conditional law exists. The source must account for generating the
correlation and the ready region, discarded information, failed attempts
and any accessible preparation records.

## 3. Native recombination and a subsequent usable state

The unchanged update gives, on the complete fields,

    u_1 = A u-v,
    u_2 = (A^2-I)u-A v,
    u_3 = (A^3-2A)u-(A^2-I)v.                  (1)

For every C and Z in mu_b's support, the receiver values are

    u_0(o)=0,   u_1(o)=b,   u_2(o)=0,   u_3(o)=b.

Proof: only s+ and s- contribute to the first neighbor sum, and v(o)=0,
so u_1(o)=Z+(Z XOR b)=b in F2. There is no two-step walk from either
nearest neighbor to o in this unwrapped local geometry. The other
current coordinates in B_2 and previous coordinates in B_1 vanish,
giving u_2(o)=0.

For u_3, a nearest neighbor reaches o by fifteen length-three walks:
three using only the x axis, and six for each of the other two axes.
Subtracting the two one-step contributions in A^3-2A leaves coefficient
13, which is one in F2. All other relevant u and v coordinates vanish.
Outside C cannot enter before this deadline because its current support
is outside B_3 and previous support outside B_2. This proves the third
value without extrapolating from a numerical simulation.

The complete receiver history is therefore

| Tick | Whole receiver R_t |
| --- | --- |
| 0 | (0,0) |
| 1 | (b,0) |
| 2 | (0,b) |
| 3 | (b,0) |

The native gate acts on the two physical input fields. It does not first
read Z, store an observer's estimate of it, or condition an operation on
a privately decoded bit. Even after all four receiver records, Z is
still fair conditional on b. The relation has become observable without
identifying either hidden input individually in this window.

The output at tick one is the actual two-slice state Phi(u,v).
It is already a valid input to the same Phi, so the next two operations
are native iterations, with no reset or state repair. At tick two the
previous coordinate still carries b; the current coordinate's zero
must not be called erasure. Tick three returns b to the current field.
This is a bounded continuation result, not an independent new
measurement, an apparatus reset, or arbitrary-depth composability.

## 4. Joint records, outgoing world and unselected mass

Write w_b(Z,C) for the full initial configuration above, and

    h_b=((0,0),(b,0),(0,b),(b,0)),
    G_b(Z,C)=Phi^3(w_b(Z,C)).

Then the complete joint law under the hypothetical preparation is

    Law(R_0,R_1,R_2,R_3,W_3 | preparation b)
      = (1/2) sum_(z in F2) integral
          delta_[(h_b,G_b(z,c))] d nu(c).            (2)

Equation (1) explicitly gives both fields of W_3=(u_3,u_2).
Equation (2) retains every outside field, residual input and correlation.
It does not replace the outgoing state by a chosen quantum state.
Reversibility preserves the original field information globally; it
grants no public inverse read. No independence between the full outgoing
world and the record is asserted.

There is no evolution failure on E_b: Phi is total and bijective.
There is also no implemented loader/herald, so a physical preparation
failure law cannot be claimed. To keep selection accounting explicit, let
F(w) be the actual full record/state pair obtained by the same passive
schedule from any initial w. With p=2^-87, the unconditioned law is

    F_#nu_0 = p F_#mu_b
                + (1-p) F_#nu_0(. | E_b^c).         (3)

The complement is retained as its exact deterministic pushforward,
not discarded and renormalized into a success claim. E_b is an analytical
partition here, not an available acceptance flag. If a later apparatus
has aborts or terminal failures, their mass and no-read/no-offer behavior
must be supplied by that apparatus. This calculation restarts no terminal
branch of Native A or any other experiment.

The ready region is bounded by the chosen three-tick causal cone.
Beyond this window the exterior can enter; (1)–(3) grant no unlimited
quiet environment or fresh independent resources. The evolved phase is
not certified to belong to the same ready/correlation preparation family
for another independently selected input.

## 5. Physical-source verdict and common-prior boundary

Main and the rooted observer-family audit already provide a visible
projection, a selected counting baseline and structured realization laws.
None of those positive results is withdrawn.

However, at the *same* visible root R_0=(0,0), mu_0 and mu_1 have
different hidden distributions. They are not two visible-root choices
under the single common hidden prior of one rooted realization.
Using a different admissible realization datum does not implement a
selectable preparation on one fixed physical experiment.

The first missing construction is therefore a physical source/preparer
that realizes these two correlations and the 86 ready pins, using one
declared underlying law, resources and complete records. The original
point-pulse calculation supplies no such loader, and neither does
conditioning on E_b. An upstream preparation label b must not be silently
made available as a receiver outcome or hidden from a receiver that can
actually access it. Equality of this paper's R_0 is conditional on the
declared receiver cut and protocol start, not proof of equality of all
records of an unspecified laboratory apparatus.

This is the existing H-PREP distinction: in-realization conditioning is
defined, while identification with a laboratory preparation is open
(#866 D-OB7/D-OB8). The present E_b also involves hidden coordinates,
so it cannot be passed off as merely conditioning on this observer's
existing record. A physical generator, or a separately justified prior
selection mechanism, must do that work.

Physical access and a read that preserves the needed correlations remain
further gates. The equations specify a mathematically available projection
and passive continuation; they do not derive the detector interaction,
record storage or clock. A true read could alter the joint state.

**Stop: conditional recombination, physical preparation/access unsourced
for this candidate.** This is not a theorem that no native mechanism can
provide them. No hidden event filter, private write, new prior selection
principle, ready reservoir or alternate candidate is adopted.

## 6. Controls and the quantum question

**Remove the correlation, keeping the individual inputs fair.** Keep the
same ready region and complement, but draw the two inputs independently.
Let T be their parity. T is fair, and (1) gives exactly h_T. Both putative
b labels have the same complete output law. This controls the claim that
the effect comes from the joint input relation rather than either
single-input marginal. It is a mathematical countercontrol, not a
physically supplied decorrelator or a new experiment.

**Classical memory passes.** The original candidate itself is a reversible
classical field calculation. It produces an informative first record and
a repeated later record. Therefore those properties do not establish
quantum coherence across a read. They also do not constitute an O-RET
counted pass under #1032's separate criteria.

**Dephasing leaves this candidate unchanged.** In the ordinary permutation
representation of the complete finite configurations, mu_b is a diagonal
density matrix. A permutation maps a diagonal matrix to a diagonal
matrix, and a computational-basis record conditions only diagonal entries.
Formal dephasing in that basis at any of these stages changes no state or
record law. This is an algebraic diagnostic, not a claimed native
dephasing operation. The effect constructed here uses classical
correlations, not coherence in that representation.

**Retain the stronger source results at their scope.** Main §3.2 does prove
a one-step non-entanglement-breaking criterion for the specified linear
lattice realization with an initially uncorrelated maximally mixed hidden
sector. That channel result is not negated here. It does not turn this
different, prepared diagonal family into a sourced coherent preparation,
or provide a multi-time physical instrument.

The existing observation-context protocol also correctly retains
classical coherent waves as a positive interference control: a fringe
alone is not quantum completion. Its fixed-path/no-interference control
concerns subnormalized particle-path counts; the XOR of two field values
here is not such a count and is not a refutation of that class.
No Born table, phase control, noncommuting instrument menu or composite
law has been derived by this example.

#866 owns the preparation and usable interaction/access source gate.
#1032 retains the separate obligation of physically preserving coherence
across a read; the passive classical continuation here does not discharge
it. #1143 retains the quantum distinguishing test. Neither direction of
#1169's full equivalence target is closed or weakened.

## 7. Source roles and review boundary

All source paths are at the main snapshot above unless noted.

| Source | Role |
| --- | --- |
| papers/SM.md §4.1; papers/oi_lattice_code/trace_out_fractional/wave_eqn.c | Exact finite reference rule and inverse; no use of the C header's obsolete coefficient-selection claim |
| papers/Main.md §§1.2, 3.2, 3.4 | Observer/measure data, conditional laws, diagonal-preservation and one-step channel scope |
| verification/audits/operational/rooted-observer-family-sourcing/result.md, Q2–Q7 | Common hidden prior per realization, legitimate visible roots and structured priors; not a correlated-input loader |
| observer-access-20261106/ASSESSMENT.md in this guiding PR | Earlier finite receiver and point-pulse source assessment; unchanged |
| verification/programmes/substratum/continuous-substates/observation-context-protocol.md | Classical-wave comparison boundaries and physical availability gate |
| verification/audits/foundations/phase-source-audit.md; verification/audits/operational/instrument-realization-audit.md | Phase availability and whole-instrument provenance; no free recombination of abstract branches |
| #866 c.6649267203 | Owner H-PREP decision provenance only, not a scientific proof |

The search covered the maintained papers, foundation/operational audits
and retained native actuation, source and recombination records. The
decisive claim here is proved in §§2–4 from the written rule; no pending
computational verdict or Issue status is used as a premise. The proposed
preparation is explicitly conditional, so it is not presented as newly
established physics merely because its coordinates exist.

Independent review must check the three-tick algebra and walk count,
same-marginal/common-prefix qualification, conditioning mass, complete
state and complement accounting, common-prior/source distinction and
classical/dephasing controls. No new code, scientific computation,
simulation, enumeration, Lean run or physical test was performed.
Ordinary draft-PR CI is repository verification. There is no premise
adoption, manuscript change, freeze, special dispatch or merge.
