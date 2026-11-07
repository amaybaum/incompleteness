# OI-QM-EXT-1 Gate B2: detector probabilities and instrument boundary

**Standing:** bounded paper-only candidate assessment. Its mathematical statements are conditional on the explicit detector model; physical sourcing remains open. Gate A's endpoint contract and the accepted Gate B1 component in this directory remain unchanged. This unit tests one additional detector mechanism; it does not assert a native OI reconstruction.

**Scope provenance:** owner authorization #1031 c.6689340754. The source snapshot is main `f49b768709d262a05471895cec703b31aff19b57`; the accepted B1 drafting input is `1ad356f7af86fc16d9e9826656bc1a3abd254cd5`. Sections 1–3 specify the fixed paper assessment protocol, not a native round, frozen execution or blinded experiment. No code, simulation or physical experiment is part of this unit.

## 1. Fixed candidate and comparison

Reuse B1's real coordinates, complex amplitude `z=x+iy`, initial modes `z=e_1` and common-duration controls `U_theta=exp(i theta X)`. The test family is `0<=theta<=pi/2`, including both port calibrations and an interior mixing case. Preparation and detector variables are independent of the loaded program before interaction.

At the sampling endpoint define the **quadratic signal** `s_j=x_j^2+y_j^2` and `t=s_1/(s_1+s_2)`, on nonzero amplitudes. B1 conserves the sum at macro endpoints. Calling it physical energy or assuming a quadratic sensor response requires additional physical justification; neither follows from the complex notation.

Add two detector seed coordinates `q_1,q_2 in (0,1)`, with one common atomless law mu, independent and identically prepared, and two ready record bits `r_1=r_2=0`. The proposed detector opcode is the reversible copy

```text
(z,q_i,r_i) -> (z,q_i, r_i XOR 1[q_i<t(z)]).
```

The signal and seed are left unchanged. Quadratic sensing, normalization by total signal, this comparator coupling, seed preparation and access to only the declared records are **candidate additional resources**, not derived OI premises.

Use B1's twenty-four drive steps, then two identical detector opcodes with fresh cells at steps 25 and 26, followed by idle persistence until the end of the first controller cycle. The one-record marginal and the two-record protocol have the same preparation and physical prefix. The clock selects the fresh cell, not a different response rule or a setting-dependent distribution. A bijective autonomous realization and a finite readback window must be checked.

The proposed quantum comparison retains the standard fixed dictionary `rho_z=zz*/(z*z)`, the declared unitary channels, and one fixed two-outcome CP instrument on C^2 reused at both detector slots with fresh apparatus. Test its probabilities and sequential records, not just the density assignments. Arbitrary history-dependent decoders, a larger quantum carrier or a different instrument on each use are outside this comparison. No conclusion about all encodings follows from a failure here.

## 2. Ensemble controls and decision rules

Derive the record law for a general mu first. Fix two setting-independent ensemble controls:

- uniform seed law on (0,1), the calibrated benchmark;
- symmetric density `6q(1-q)`, a competing law with the same support and port-exchange symmetry.

The uniform benchmark is not evidence that OI prepares it. Inspect whether choosing this ensemble and response inserts the desired Born law as an assumption. A conditional match must remain labelled as such.

Check the complete predeclared theta family, not only its middle or calibration points. Require phase invariance, positive-rescaling invariance, port-exchange covariance where justified, calibration, source/setting independence, threshold conventions and genuine coupling through the declared detector.

For sequential comparison, use the same detector twice with the two independent seeds. First determine what any fixed CP instrument that matches the port-calibration protocols would have to do; then compare an interior mixing protocol's full joint law. This tests state disturbance and composition in addition to single-use frequencies.

Retain B1's I/-I sign-readout counterexample as a control. The intensity comparator is a distinct candidate access interface. It does not erase a physically available sign readout or establish a phase quotient for a richer native model.

The rival outcomes are:

1. A consistent conditional instrument on the stated family, with every physical input's source identified.
2. A conditional single-use match with a sequential/instrument failure.
3. Single-use probabilities not fixed by the declared physical premises, or a direct mismatch.
4. A source gap or inconclusive comparison with a precisely named missing input.

These outcomes can coexist on different evidence layers. A failure is scoped to this candidate/dictionary. A matching table does not establish Born selection, native physical availability, every quantum instrument or full Gate A equivalence.

## 3. Source and review obligations

Trace real modes/control back to B1's explicit unsourced resources; audit the new quadratic sensor, normalized coupling, seed measure/freshness, restricted access and any required measurement backaction separately. Consult Main's representation/measure boundary and #1059's maintained measure-source records. Do not repeat the existing GeneralCarrier/MinimalRepertoire characterization, reassign #1059/#1082 work or promote its assumptions to native facts.

The deliverable is a hand derivation or candidate-scoped gap with a source ledger in this file. A separate reviewer will inspect the pushed immutable result for noncircularity, the general probability law, the physical assumptions, retained controls and the exact sequential/CP scope. The existing guiding PR remains #1173. No manuscript, code/Lean, native freeze/dispatch or research merge is included.

## 4. Derived single-use law and what the uniform benchmark assumes

For the atomless seed law define F(t)=mu((0,t)), with F(0)=0 and F(1)=1. The fixed initial modes and B1's endpoint control give z_theta=(cos(theta), i sin(theta)), so t_theta=cos(theta)^2. Direct pushforward through the physical comparator, without a quantum probability postulate, gives

    p_1(theta) = F(cos(theta)^2),    p_0(theta) = 1 - F(cos(theta)^2).

The target basis measurement has probabilities cos(theta)^2 and sin(theta)^2 by the quantum comparator's definition.

**Fixed-comparator criterion, with both directions.** If mu is uniform in the specified physical detector coordinate, F(t)=t and the single-use probabilities match the target for every declared theta. Conversely, cos(theta)^2 ranges over the whole interval [0,1]; a match for every theta forces F(t)=t everywhere, which determines mu as the uniform law in that coordinate. This is necessity and sufficiency for this response function and test family only. It does not select that response, physical coordinate, reference measure or preparation law from OI.

For the competing symmetric density, direct integration gives

    F_B(t) = integral_0^t 6q(1-q) dq = 3t^2 - 2t^3.

The density is nonnegative, normalized and invariant under q -> 1-q. It gives the same deterministic port calibrations and the same balanced value F_B(1/2)=1/2. At theta=pi/3, however, t=1/4 and F_B(t)=5/32, whereas the target value is 1/4=8/32. Thus calibration, port symmetry and the balanced example do not fix the complete probability curve.

Both seed laws are held fixed across programs. The seed coordinates never change in the proposed dynamics, so their marginal invariance does not select between these laws. These are countermodels to a deduction from the *listed detector premises*, not countermodels asserted to satisfy every native OI physical premise.

The response already uses a quadratic, normalized signal. Uniform mu then converts that chosen signal into the desired numerical probability. This is a conditional implementation of a Born-shaped response, not a derivation of the quadratic exponent or its physical selection. Relabelling the seed coordinate can move a nonuniform density into the response function; the physically relevant assumption concerns their joint pushforward, not the word “uniform” alone.

## 5. Autonomy, access and controls

The autonomous world is (R^4 minus {0}) x (0,1)^2 x {0,1}^2 x [-1,1]^24 x Z_64: nonzero real modes, two seeds, two record bits, 24 coefficient fields and the clock. Initially ell=0. Every invertible T_k preserves the nonzero-mode domain, so the denominator defining t remains nonzero. Each drive opcode is B1's bijection; at clock 24 the first comparator copies into r_1, at clock 25 the identical comparator copies into r_2, and clocks 26 through 63 are idle. The list and seeds are fixed. Each XOR copy is its own inverse, because its predicate depends only on unchanged modes and seed. The previous clock determines the inverse opcode. The common clock-advance rule is therefore bijective. This proof establishes an ideal extended update, not the physical detector resources.

Initially, the joint uncontrolled law is the point mode preparation e_1 times mu times mu times the two ready-zero bits, with the same clock and controller-noise law for every theta. Loading may change only the isolated program coefficients. The detector sees the current modes and its selected fresh seed, not the angle label or future instructions. The one-record protocol ends after the first copy; its prefix agrees with the two-record protocol. Public records can be read passively during the remaining idle part of this cycle. Later cycles require new cells or an accounted reversible reset, not perpetual storage.

The comparator is invariant under z -> alpha z for every nonzero complex alpha, since both signals scale by |alpha|^2. This is an algebraic property of the declared sensor; it does not establish that those underlying states are physically gauge-equivalent. For symmetric mu, F(1-t)=1-F(t), so exchanging ports exchanges outcome probabilities. Threshold ties have measure zero by atomlessness; endpoint calibrations are deterministic.

For the B1 I/-I control, both endpoints have t=1 and the comparator records 1 in each. B1's sign sensor still records 1 versus 0. The two facts coexist because they concern different observation maps. If the sign sensor is physically available, the richer interface retains the original obstruction to the standard density dictionary. This detector calculation supplies no physical reason to discard it.

## 6. Sequential law and a fixed-instrument obstruction

The first record conditions q_1 but leaves the point signal z_theta unchanged. The fresh q_2 remains independent with law mu. Writing p=F(cos(theta)^2), the native joint probabilities, with rows r_1=1,0 and columns r_2=1,0, are therefore

    P_native = [[p^2, p(1-p)],
                [p(1-p), (1-p)^2]].

This calculation uses the declared fresh-product preparation and nondisturbing comparator, not a quantum state-update assumption.

### 6.1 What matching the calibration protocols forces

Let P_1=|e_1><e_1| and P_0=|e_2><e_2|. Suppose one fixed binary CP instrument (Phi_1,Phi_0) on C^2 matches all the named one- and two-record protocols, with the same instrument reused at both slots. Its effects E_b satisfy tr(Phi_b(rho))=tr(E_b rho), E_b>=0 and E_1+E_0=I. These are imported target-QM definitions.

The single-use port calibrations at theta=0 and theta=pi/2 give <e_1,E_1 e_1>=1 and <e_2,E_1 e_2>=0. Positivity forces the off-diagonal entries to vanish; hence E_1=P_1 and E_0=P_0.

Use the standard finite-dimensional Kraus representation of CP maps, another target-QM input. Since the sum of ||K_(1,a)e_2||^2 is zero, every outcome-1 Kraus operator kills e_2. Consequently

    Phi_1(rho) = rho_11 sigma_1,    sigma_1 = Phi_1(P_1),

where sigma_1 is a density matrix. Similarly Phi_0(rho)=rho_22 sigma_0, with sigma_0=Phi_0(P_0) a density matrix. Sharp effects alone have not yet fixed these output states.

Now use the **two-use** calibrations. For theta=0 the native history is (1,1) with certainty, so

    1 = tr(Phi_1(Phi_1(P_1))) = tr(P_1 sigma_1).

A positive trace-one matrix with this diagonal entry is P_1; hence sigma_1=P_1. The deterministic (0,0) history at theta=pi/2 likewise forces sigma_0=P_0. Therefore the only possible matching fixed instrument is the basis Luders instrument

    Phi_b(rho) = P_b rho P_b.

This output-state conclusion uses both sequential port calibrations. It is not inferred from sharp effects alone and is not a new characterization of operational QM.

### 6.2 The interior test

At theta=pi/4, the uniform benchmark has p=1/2. Both predeclared symmetric seed laws also have this value. The unchanged-signal, fresh-seed mechanism gives all four two-bit histories probability 1/4. The instrument forced above instead gives

    P_quantum = [[1/2, 0],
                 [0, 1/2]].

Thus the event r_1 != r_2 has native probability 1/2 and target probability zero. A single-use Born table does not repair the sequential record law.

The failure holds throughout the stated class of atomless seed laws for this fixed mechanism/comparison: if F(1/2) differs from 1/2, the single-use interior test already fails; if it equals 1/2, the two-use test fails as shown. Changing only mu cannot make every named protocol agree.

The claim is limited to the specified preparation/control family, unchanged-signal comparator, fresh independent seeds and one fixed C^2 instrument/density dictionary. It does not exclude a different detector coupling, physical apparatus memory, correlated seeds, a different state encoding, a larger quantum carrier or arbitrary record-law representations. Main's finite observable-law correspondence is preserved. Gate A's full target is unchanged and remains undischarged.

### 6.3 Physical meaning of the remaining instrument obligation

The proposed detector copies information but changes no signal coordinate. With fresh independent apparatus for the next identical operation, conditioning the first record cannot supply the target conditional signal statistics. A future physical mechanism must explain an appropriate outcome-dependent operational update or a different physically justified conditional apparatus/state architecture.

In a reversible world, an irreversible-looking projection cannot simply be inserted as the world map: the lost information and record correlations need an accounted environment. This assessment constructs no such repair and proves no unique or universally irreducible missing premise. It identifies a failure of the selected mechanism under its explicit assumptions.

## 7. Physical-assumption and source audit

| Input | What is actually supplied | Physical/source status |
|---|---|---|
| Real modes and exact signed controls | B1's explicit T_k update and finite forward program; its endpoint norm identity | Existing conditional component. Real-mode realization, isolation, exact continuum loading and control remain B1's unsourced extras |
| Quadratic normalized sensor | The chosen function t=(x_1^2+y_1^2)/sum_j(x_j^2+y_j^2) and comparator coupling | Posited detector response. The power two and normalization are already in the selected sensor, not derived from Main's finite-law theorem |
| Detector coordinate and seed measure | An atomless law mu in the specified q coordinate | Preparation/reference measure is an added datum. Uniformity is exactly the extra single-use matching condition for this comparator/family |
| Fresh independent cells | The loaded product law mu x mu and two ready record bits | Explicit preparation/isolation assumption. It yields the product joint law and is not supplied merely by naming a fresh helper |
| Restricted access | Only the declared detector records are read | Candidate interface, not a physically sourced phase quotient. B1's available sign sensor is not removed from a richer model |
| Unchanged signal during a copy | The stipulated reversible XOR opcode | An ideal detector assumption, responsible together with freshness for the sequential failure. No physical measurement-backaction mechanism is derived |
| CP instrument, trace and Kraus laws | The independently defined target comparator | Imported finite-dimensional QM structure, not an OI-derived probability or update rule |
| Full operational/composite resources | Nothing beyond this fixed one/two-record assessment | Gate A's all-preparation/instrument, adaptive-history and composite obligations remain open |

**Main's selection premise is preserved.** Main §1.2 Lemma 3 explicitly selects global finite counting measure by a maximal-entropy principle; it does not claim uniqueness from invariance alone. The following measure-as-realization-datum remark permits structured fixed hidden priors. This paper therefore does not say that the framework has no measure-selection premise. A physical map from that finite setting to this new continuous detector coordinate, its reference measure and its fresh preparation is still needed. Even a separately imposed maximum-entropy rule requires the physical reference/constraints before it can justify this detector's uniform law.

The maintained record `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`, §1 and its status/scope block, already distinguishes representation form from the numerical probabilities consuming a selected measure. It sources no physical measure and limits its non-invariance examples to the stated non-native finite bijections. That distinction is reused here; no new general measure-selection theorem or native-wave countermodel is claimed. The old #1082 assessment was read as context, not used as an off-main proof premise. Its writer and remaining #1059 obligations are unchanged.

The existing `OperationalAssembly.readout_is_localLuders` theorem (OperationalAssembly.lean:658, under `verification/lean-mathlib/OIBridge/`) derives its readout form from that interface's spectator-independence hypothesis. Our finite C^2 calibration argument is an explicit diagnostic for the chosen detector, not a substitute for that result or a physical sourcing of its interface. The GeneralCarrier/MinimalRepertoire results in Gate A/B1 are retained rather than reproved.

The cited Main passages and maintained measure record were checked in the source corpus; their relevant statements are unchanged at the source snapshot named above. These sources support their own explicit scopes. No claim here depends on treating a tracking Issue, author-posted verdict or WIP branch as an established mathematical premise.

## 8. Assessment outcome and limits

The hand derivation supplies:

1. The general single-use law F(cos(theta)^2), and the necessity/sufficiency of uniform seed law for a full-family Born match **given the chosen quadratic comparator**.
2. A symmetric alternative ensemble that passes endpoint/balanced controls but fails the full Born curve.
3. A complete two-record counterexample to any fixed C^2 CP instrument matching this unchanged-signal, fresh-seed mechanism under the stated calibration protocols and dictionary.

The outcome is a conditional one-shot implementation plus a candidate-scoped instrument obstruction and named physical-source gaps. It establishes neither native Born selection nor a native quantum measurement mechanism. The numerical-measure and instrument-update obligations are separate: imposing the former does not supply the latter. A successful reconstruction would still need a physically justified detector/preparation/access architecture and consistent conditional updates, in addition to B1's physical control inputs.

The quadratic-signal/CDF calculation and the Kraus/rank-one facts are elementary known mathematics; no novelty is claimed for them or for no-information-without-disturbance principles. Their role is to test this explicit candidate and expose where proposed physical inputs enter. Other mechanisms and encodings are not ruled out, and no universal irreducibility/minimality statement is made.

All derivations and controls in this assessment are on paper. No scientific code, CAS, numerical experiment, Lean build, simulation, physical test, manuscript edit or governed execution was performed. Ordinary repository CI and a separate exact-head review are distinct from physical sourcing or a full Gate A proof.
