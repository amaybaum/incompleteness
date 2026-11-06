# Gate B3: reversible read-and-exchange candidate

**Standing:** bounded paper-only source assessment of one proposed interaction; the conditional calculations do not establish native availability. Mathematical behavior and physical availability are separate questions. The same qubit dictionary/target and B1/B2 controls are retained. No native quantum reconstruction is presumed.

**Scope provenance:** #1031 c.6691265564. Inputs are the accepted B1/B2 records at `6fb6d3b5119c28304efe7d62fdf2021e220b30ef`; source snapshot main `f49b768709d262a05471895cec703b31aff19b57`. This is a hand-derived candidate assessment, not a frozen native round or a blinded experiment. The old records remain unchanged.

## 1. Fixed physical proposal and its status

The proposed architecture is detector-controlled packet routing: a detector bit selects one calibrated reference carrier for the outgoing port, while the incoming carrier is kept in the selected reference slot. This motivates a reversible read-and-reprepare interaction. It is not evidence that native OI supplies that interaction, its calibrated references or its probability law.

Use B1's nonzero real mode carrier, represented by z in C^2. Each of two detector slots j has two nonzero reference carriers A_(j,0), A_(j,1), one seed q_j in (0,1), and one ready record bit r_j=0. Prepare A_(j,0)=e_2 and A_(j,1)=e_1. The two seeds have one common atomless law mu and are independently prepared. The signal initially is e_1. All these uncontrolled preparations and the ready/public records are held fixed across loaded settings.

Retain B2's *posited* sensor t(z)=|z_1|^2/(|z_1|^2+|z_2|^2), and define b(z,q)=1[q<t(z)]. The candidate interaction D_j is one common map:

1. Copy the sensor predicate into the ready bit: r'_j = r_j XOR b(z,q_j).
2. Controlled by the resulting r'_j, exchange the complete signal carrier z with A_(j,r'_j). Leave the seed, other reference, other records and program unchanged.

The exchange stores the old signal; it does not erase it or clone an unknown state. Conditional output states must be derived from this map and the ready-reference preparation. A quantum projection/update is not an additional native opcode.

Treat D as the proposed coupled operation with public record access after the complete interaction. Whether a physical implementation inseparably links the readable record to that exchange is an explicit source/access obligation. If a readable copy-only operation can be isolated or the exchange disabled, B2's negative control remains a physically available procedure; it cannot be discarded from a full interface.

## 2. Fixed experiment family and quantum comparator

Use the common-duration B1 drive U_theta=exp(i theta X), with 0<=theta<=pi/2, from the same initial signal. The one-read protocol is U_theta followed by D_1. The two-read protocol adds U_phi and D_2, with -pi/2<=phi<=pi/2. Zero phi still uses its full-duration program. Both slots use the same D rule and fresh apparatus resources.

The comparator is the same density assignment rho_z=z z^*/(z^* z), the corresponding unitary channels, and the binary basis instrument I_b(rho)=P_b rho P_b, where P_1=|e_1><e_1| and P_0=|e_2><e_2|. B2's calibration proof already identifies that instrument for a fixed C^2 comparison; no target is being changed to fit a result.

A common autonomous realization, actual loading/prefix independence, resource accounting, and repeated passive readback of the first public bit are required. Specify its finite window; no unlimited lifetime or unbounded protocol supply is presumed.

## 3. Controls and ordered assessment

Keep these controls fixed:
- B1's I/-I sign-readout obstruction in any richer interface where that sensor is available.
- B2's copy-only detector, as the exchange-disabled comparison. Its known sequential failure is retained.
- Uniform seed law as the conditional numerical benchmark, and B2's symmetric density 6q(1-q) as the competing ensemble.
- Both deterministic port calibrations, the balanced theta=pi/4 case and the off-centre theta=pi/3 case.
- phi=0 (repeatability) and phi=-theta (the second-read interference/backaction comparison).

Assess in this order, preserving each evidence layer:
1. Trace inherited real-carrier/control assumptions and the first *new* physical requirement: availability of the record-conditioned exchange and its coupled record-access semantics. Missing physical support stops a native-success claim.
2. Derive bijectivity and the conditional signal/reservoir state from D, with its preparation assumptions explicit.
3. Derive one- and two-record probabilities from the same loaded law and compare with the same instrument. Matching a calibrated table is not physical sourcing.
4. Check record persistence/freshness and resource exhaustion. A retention failure belongs to #1032; other failures are routed only after checking their existing accountable homes.
5. List remaining assumptions and both-direction/full-interface obligations. A source gap is not a universal no-go, and a conditional component is not full equivalence.

Possible outcomes are a sourced component within the stated scope, a conditional mathematical component with an identified first physical gap, a mathematical mismatch, or a precise inconclusive/source result. Separate-agent review must inspect the pushed result. No source premise is adopted merely to rescue a desired outcome. The unit includes no code/Lean, simulation, physical experiment, manuscript change, native F/E/dispatch or research merge.

## 4. State change and reversibility from the interaction

Write C_j for the sensor XOR and S_(r'_j) for the controlled exchange. On the full register space, C_j is its own inverse: it changes only r_j, not the predicate inputs. The exchange is also its own inverse when controlled by the unchanged output bit. To invert D_j, first undo the exchange using that output bit; the old signal is then restored, so the original sensor predicate can be recomputed to undo the XOR. This works for arbitrary old record values and nonready reference values, not just the prepared protocol slice.

On the ready slice r_j=0, A_(j,0)=e_2 and A_(j,1)=e_1, the produced bit is b=b(z,q_j). The actual outgoing signal is e_1 for b=1 and e_2 for b=0. The selected reference slot contains the entire old z. Conditional on a positive-probability outcome, the outgoing signal therefore has density P_b. This state change is a consequence of exchanging with the supplied ready carrier; a projective native opcode has not been inserted.

The map preserves the sum of squared amplitudes of the signal and selected reference, while storing the old signal information. This is an algebraic property of the proposed routing, not a derivation of a native Hamiltonian or an energy-selection law. Its availability and the ready references remain physical inputs.

## 5. One common world, loading and finite record window

Use the autonomous world

    (R^4 minus {0})^5 x (0,1)^2 x {0,1}^2 x [-1,1]^48 x Z_64.

The five nonzero carriers are the signal and four references. The other fields are two seeds, two record bits, two 24-coefficient drive programs and the clock. Initially the clock is zero. The actual loaded uncontrolled law is the same point signal, four ready references, product seed law mu x mu, ready-zero records and a noise-free controller for every theta/phi. Only isolated program fields differ.

At clocks 0–23 apply B1's U_theta drive word to the signal; at clock 24 apply D_1; at clocks 25–48 apply the U_phi word; at clock 49 apply D_2; at clocks 50–63 leave these data idle. Each drive opcode is invertible and preserves nonzero signal vectors. Each D_j preserves the nonzero-carrier product domain. Given the new clock, the previous opcode is known, so the inverse rules above define a bijective common world update.

D_j is the proposed *coupled available operation*. Its mathematical factorization does not prove separately selectable copy/exchange operations or public access halfway through an actual physical implementation. A native implementation must justify that access/latency contract. The model makes no physical timing claim merely by assigning an abstract opcode.

The first public bit is valid after step 25; the second after step 50. No subsequent opcode in this first cycle changes the first bit, and idle readback changes neither bit. The one-read protocol ends after D_1; it has exactly the prefix of the two-read procedure, with the unused future program/seed/reference fields isolated. The same native operation label always denotes the same D rule.

The second seed and references retain their fresh preparation conditional on the first record because only the first slot's independent resources have entered the first interaction. Neither seed law nor incoming preparation is changed to fit phi or an outcome. This is a specified loaded-state/resource condition, not a theorem about bare OI.

Each detector consumes its ready reference bank and leaves old data in the reservoir. No reservoir return-coupling occurs in the declared experiment menu. Later cycles or more measurements need fresh banks or an accounted preparation/reset mechanism. This finite window does not establish unbounded resource supply or physical O-RET.

## 6. Derived record laws and the same instrument

Let F(t)=mu((0,t)), with F(0)=0 and F(1)=1. B2 already derives the first outcome weights

    p_1(theta)=F(cos(theta)^2),    p_0(theta)=1-p_1(theta).

After the first outcome, section 4 gives the actual signal e_b. B1's following U_phi word therefore presents the second detector with normalized first-port signal

    t_1(phi)=cos(phi)^2,    t_0(phi)=sin(phi)^2.

The fresh second seed keeps law mu. Consequently the complete two-record law is

    P(b,1)=p_b(theta) F(t_b(phi)),
    P(b,0)=p_b(theta) [1-F(t_b(phi))].

This follows from the exchange, fixed preparations and common dynamics. No quantum state-update law was used to compute it.

For the uniform benchmark F(t)=t, rows b=1,0 and columns c=1,0 give

    [[cos(theta)^2 cos(phi)^2, cos(theta)^2 sin(phi)^2],
     [sin(theta)^2 sin(phi)^2, sin(theta)^2 cos(phi)^2]].

These are exactly the traces of the same fixed quantum sequence I_c after U_phi after I_b after U_theta, from P_1. The first unnormalized outgoing branch is p_b(theta) P_b = P_b rho_theta P_b. Zero-probability branches are zero operators; conditional normalized states are compared only on positive-probability branches.

More generally, if an incoming ensemble nu and an independent uniform detector seed are physically supplied, put rho_nu=integral rho_z dnu. This one operation returns branch weight tr(P_b rho_nu) and outgoing basis state P_b, so its decoded unnormalized branch is P_b rho_nu P_b, independent of the ensemble decomposition. This algebra does not establish that every such ensemble is preparable, or supply all instruments/composites.

At phi=0 the two records agree with certainty; at the balanced preparation their two nonzero joint probabilities are 1/2. With phi=-theta, the derived table retains the first measurement's conditional disturbance before the inverse drive. These are genuine two-read comparisons, not a new density dictionary or a different instrument on each use.

## 7. Retained controls and prior mathematics

With the exchange disabled, the same fresh-seed sensor leaves the signal unchanged. Its two-read law is p_b(theta) times the response at U_phi U_theta e_1. At phi=0 and theta=pi/4 it has the B2 product table with all entries 1/4, not the repeatable target table. At phi=-theta its second first-port record is certain. The exchange therefore makes a substantive difference to the conditional signal behavior.

For the competing B2 density 6q(1-q), the exchange still sets the outgoing signal to the recorded basis carrier, and phi=0 remains repeatable. The first probability at theta=pi/3 is nevertheless F(1/4)=5/32 rather than 1/4. A conditional state-update mechanism does not select the detector measure or repair its numerical law.

B1's sign-readout control is unchanged. A richer interface that can inspect a global sign, read old reservoir carriers, or isolate a readable copy-only operation has additional procedures whose laws must also be accounted for. They cannot be removed by a post hoc decoder or by declaring this smaller menu to be the full Gate A target.

**Reuse rather than a new reset theorem.** The maintained record

    verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/history-architecture-v5/REPORT.md

already derives a supplied single-qubit projective/unitary interface, fresh re-preparation and a global reversible dilation retaining old carrier/seed information. Its companion review checks that proof and its explicit resource/access boundaries. The record credits the known Kochen-Specker model via Ruebeck–Lillystone–Emerson. Its all-finite-depth result is explicitly an abstract positive architecture control, not native availability, measure selection or a full instrument/composite reconstruction.

This assessment reads that construction/proof as prior mathematics; it does not replay its historical computations or claim novelty for reversible re-preparation. Sections 4–6 only check the present, narrower amplitude-routing candidate and its fixed controls. The source question concerns physical availability and access, not the absence of an abstract reversible reset construction.

## 8. First source gate and accountable homes

The conditional calculations do not supply a map from the actual two-slice/lattice state, controls and observer to D_j and its public record. The source trace keeps two levels explicit:

1. **Inherited native-source gap:** B1's real coherent carrier, exact controls and continuum loading remain unsourced. The present real-carrier world is not asserted to satisfy the finite-alphabet native substratum axioms or establish a nonempty full Gate A realization class.
2. **First new B3 physical requirement:** a physically available record-conditioned carrier exchange with the stated coupled public-record access. The traced sources do not derive this particular detector/selector/routing interaction from the native wave rule. Conditional on the inherited idealization, this is the first new gate at which a native-success claim stops.

The first new gate belongs to **#866, O-SET/O-REC**, preserving its existing dependencies and writer. Ready-reference preparation and fresh supply are **#1147** obligations. Seed/reference-measure selection remains **#1059**. Physical retention/access failures belong to **#1032**; none is proved here, and the ideal finite persistence calculation does not discharge O-RET. These pointers route work; they establish no physical premise or new authorization.

| Resource/claim | What is derived here | What remains physical |
|---|---|---|
| D_j interaction | An explicit global bijection and inverse; old signal is retained | Actual carrier mapping, detector-conditioned exchange and calibrated coupling availability |
| Outgoing signal | The selected ready reference becomes the signal, hence P_b | Native preparation of those references and fresh resources, not a late outcome-dependent replacement of the incoming ensemble |
| Numerical probabilities | General F law; uniform benchmark matches the fixed target | B2's quadratic sensor and physical seed/reference measure are still assumed |
| Public record | The bit is unchanged through the named finite window | Readability, completion latency and inseparable coupling to the exchange need physical justification |
| Reservoir | The old signal is stored, not erased | Source the observer's access restrictions and non-returning isolation; arbitrary future access is not proved harmless |
| Repeated instrument | Conditional one/two-read agreement with the same instrument | This does not source all instruments, preparations, controls, composites or compatible unbounded finite resources |

The source `verification/programmes/substratum/continuous-substates/native-link-sourcing-gate.md` distinguishes the actual reversible two-slice wave update from an added reversible link/pointer/backaction toy. The latter's logical consistency does not supply the former's physical detector. The existing GeneralCarrier/MinimalRepertoire and OperationalAssembly results similarly retain their stated interface/control hypotheses; they do not by themselves construct this physical coupling.

Main's finite-law representation and separately posited maximum-entropy/counting premise are preserved. That premise does not alone identify this detector's continuous coordinate, reference measure, preparation or conditional routing. This is a gap for the named candidate and traced inputs, not a proof that no native implementation can exist.

## 9. Outcome and remaining two-way work

The source verdict is **UNSOURCED at the inherited and first new physical gates**. The ideal interaction conditionally produces the required state change and fixed one/two-read statistics, so the remaining obstacle is not a missing abstract reset theorem. The record does not classify the candidate as a physically sourced quantum measurement or promote a new native principle.

A full two-way result would still need physical preparations, the detector measure, an available coupled interaction and its complete access boundary; every required quantum instrument and composite operation; compatible finite resources for arbitrary finite/adaptive protocols; and a single correspondence covering all allowed native procedures without excess records. Neither direction of Gate A's whole-model theorem follows from this one interaction. The earlier B1/B2 limitations remain in force.

This bounded assessment stops its positive physical claim at the first source gate and routes that requirement to the existing home. It adopts no physical premise to rescue a desired comparison. All calculations are hand derivations. No scientific code, CAS, simulation, physical experiment, Lean build, manuscript edit, native F/E/dispatch or research merge was performed for this unit; ordinary repository CI is a separate consistency check.
