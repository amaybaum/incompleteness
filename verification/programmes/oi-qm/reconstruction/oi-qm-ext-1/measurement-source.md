# OI-QM-EXT-1 Gate B2: detector probabilities and instrument boundary

**Standing:** bounded paper-only assessment, initially WIP / UNVERIFIED. Gate A's endpoint contract and the accepted Gate B1 component in this directory remain unchanged. This unit tests one additional detector mechanism; it does not assert a native OI reconstruction.

**Scope provenance:** owner authorization #1031 c.6689340754. The source snapshot is main `f49b768709d262a05471895cec703b31aff19b57`; the accepted B1 drafting input is `1ad356f7af86fc16d9e9826656bc1a3abd254cd5`. This is a prospective paper assessment protocol, not a native round, frozen execution or blinded experiment. No code, simulation or physical experiment is part of this unit.

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
