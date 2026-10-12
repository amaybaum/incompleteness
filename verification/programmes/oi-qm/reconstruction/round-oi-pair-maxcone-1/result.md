# OI-PAIR-MAXCONE-1 — conditional pair-cone theorem

Outcome: OI-PAIR-MAXCONE-1-PROVED

For a set of two-token tables containing every product state of eball 3 and closed under addition and nonnegative scaling, the maxCone upper bound together with CNOT and full rotation/cyclic invariance implies K=Q3. The upper inclusion uses maxCone and block invariance; the lower uses products and cone closure. Available sharp product tests suffice for the upper bound. These conditional statements use neither self-duality nor closedness nor an assumed ReachPure witness.

The block and generator equivalences have separate witnesses: blockInvariant_of_eq_Q3 / pairCone_eq_Q3_of_block_maxCone, and driveInvariant_of_eq_Q3 / pairCone_eq_Q3_of_drive_maxCone. The physical state/test identification, product preparation and cone realization, validity of product tests on the actual pair, enough available tests, and preservation by the gate and full rotation/cyclic actions retain their source obligations. A one-angle or channel-limit route retains its own closure assumptions.

The finite controls do not show that OI implies QM. Nothing here sources H3; neither physical sourcing nor full-model independence is labelled kernel-certified. The 118 reached rows and 68 NOT REACHED rows remain distinct; the latter are unresolved. Arbitrary finite-carrier reconstruction and the full operation/instrument correspondence remain open.

Exact controls: MAXCONE-EXACT: PASS; 2743 finite exact checks
The checker uses Q(i), replay is byte-identical, and its three mutations are rejected. Finite witnesses are not universal proofs. Density states fail scaling; the rank-three-excluded PSD family fails addition; the expanded kappa family fails a product test; the zero cone fails product inclusion; the separable family fails CNOT invariance. Whole-family statements have written proofs in the preregistration at their stated scope.

Design evidence: core 4d7d71d6, run 38205087980, 13 standard axiom reports; sharp-test refinement bbcdbab5, run 38205760341, 16 standard axiom reports. Both Build steps succeeded and their release gates failed only the seven unregistered design modules' census. Predictive execution evidence is recorded in the preregistration. The execution includes the matching proof bodies, truthful conditional headers, the kernel-only registry family, the exact checker and control shard. Six E19 dependency bodies are unchanged; the new MaxCone proof body is unchanged from the measured refinement.

F: ef486aa48c445db2264d7a7f8b22520af743e4a9
F workflow run: 38245407074
S1: b6fc7139659227b3f8170e0e8926945791976276
S1 workflow run: 38250344438

The execution's sixteen named MaxCone axiom reports must be standard, with no sorryAx, and all required host checks must be green before E designation. The owner's E designation and its exact-head workflow attestation are recorded outside this result note and in the receipt. The proof is conditional mathematics; this package supplies no unconditional reconstruction or full-model independence result.
