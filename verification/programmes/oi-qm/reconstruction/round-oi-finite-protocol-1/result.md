# OI-FINITE-PROTOCOL-1 — finite stopped protocol from primitive resources

Outcome: OI-FINITE-PROTOCOL-1-PROVED

Every finite stopped-channel depth is InstAvail from Architecture and explicit circuit/reset/correction memberships, using the existing readout, op, bind, coarse and discard rules. The uniformly mixed ancilla is reset inside the protocol. The balanced circuit's corrected branches and all-depth stopped formula are proved for every input matrix. No available approximation sequence is a premise.

Spectator availability additionally requires ContextStable and LabelInvariant. Primitive memberships, convergence, availability of a limiting drive, physical state/test identification and validity or preservation of an arbitrary pair cone remain separate obligations. K2 remains open, K3 remains conditional, and arbitrary finite-carrier reconstruction and the full operation/instrument correspondence retain their existing obligations. This package does not establish unconditional OI reconstruction or full-model independence.

Exact controls: FINITE-PROTOCOL: PASS; 10 groups; 36 stopped matrix-unit cases
Arithmetic is in Q(i). Replay is byte-identical, stderr is empty and exit code is zero. Removing reset, removing correction and continuing after success each disagrees with the intended map on the 0,1 matrix unit. These finite controls do not prove the universal theorem.

The adopted module is kernel-only and imports only existing main ImplementationLocality and Mathlib tactics. Its proof body is unchanged from the measured #810 design head 708153423ffb5ea4fe27663654431650b5a2e48a. Historical design measurements and new predictive evidence are recorded separately in the preregistration; neither is an F/E attestation.

F: 1f17f1a631d5b8a57c1b70f5965c6e032e9873da
F workflow run: 38245409846
S1: 031a32bd5fc054004ee3ea6ed0faa79aa2451a4b
S1 workflow run: 38250404107

Successful Build and fourteen standard named axiom reports without sorryAx are required, alongside all-green exact-head host checks before E designation. Owner E designation and host attestations are recorded in the receipt. Local content controls do not certify host facts.
