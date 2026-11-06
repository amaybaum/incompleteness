# Gate B3: reversible read-and-exchange candidate

**Standing:** bounded paper-only assessment of one proposed interaction. Mathematical behavior and physical availability are separate questions. The same qubit dictionary/target and B1/B2 controls are retained. No native quantum reconstruction is presumed.

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
