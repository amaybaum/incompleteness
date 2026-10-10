# Coordinator's pre-audit record for stage 5 (Q-EX-BRIDGE), written 2026-10-10 16:40Z, before threads D and C launch

Purpose: fix, before the threads run, what the coordinator has established exactly about the bridge question and
which kernel and manuscript anchors the protocol relies on, so that the later audit compares the threads' claims
against checks made without their code or conclusions. Script `preaudit_bridge.py` (`bc9caa20…`), run 3: 7/7
CONFIRMED, `PREAUDIT-BRIDGE-FIXED`; replay byte-identical. Run 1 (kept as `.run1.*`, 5/7) failed on two harness
choices of my own: B4 used the rotated Bell-type state itself as the witness, which is not in `Z_F*` (overlap
`cos²(1/6) > 1/2` with `f_(1,1)`), and B6c asserted the pairing of a product state with itself as 1 where the `ipW`
normalization gives 4. Run 2 (kept as `.run2.*`, 6/7) corrected the witness construction but transcribed the
Bell-type states from Z's formula `ψ_s = (1, s₁s₂, s₁, −s₂)/2`, which in the stage-3 convention (control index first)
labels the state of `z_{−s}`, not `z_s` (a labelling convention in Z's RESULT §1.1, consistent inside Z's own
scripts; recorded as wording for the stage-4 record, no result affected). Run 3 takes the states as the negative
eigenvectors of `pauliW(z_s)` and asserts the reproduction of `z_s` exactly.

## Facts fixed [X], with the written argument [W] they support
- **B1 (the native drive and J).** The drive about the NOT axis `x`, idle-extended on the control, closes with
  `cnot` to an abelian 2-torus (dimension 2; stage 4's S3 instance). `cyc3` carries `x` to `y`, and the two coordinate
  flows close with `cnot` to `su(2) ⊕ su(2)` (dimension 6). So (b) for the drive and `J` on one token gives S4-C,
  hence `K = Q3` by stage 4: `(b_DJ)` is a sufficient form.
- **B2 (J alone, with the NOT).** `cyc3` is a rotation of order 3 fixing (1,1,1); with `Rz(π)` it generates a finite
  group of order 12 (Y7's countercontrol). So `{NOT, J}` idle-extended is a finite extension of `G16`: EXOTIC-E by
  stage 4 (Y5, Z z4), never UNIQUE. `K(Z_F)` is not `J`-invariant: the unitary lift of `cyc3` carries `z_(1,1)` outside
  `Z_F`, and a pure state of `K(Z_F)` (pairings 1/4 with every defect) pairs −1/2 with the image, so the `{NOT, J}`
  countermodel is EBF existence, not the stage-3 cone.
- **B3 (a gate drive).** The gate's own flow `exp(−iθ P₁⊗P₋)` is diagonal in the product basis
  `(|0+⟩, |1−⟩, |0−⟩, |1+⟩)` with `CNOT` at `θ = π`: it lies in the 3-torus of product-diagonal unitaries, so stage 4's
  Z verdict for `⟨T³, G16⟩` (EXOTIC-E with seeds on the circles) covers candidate κ.
- **B4 (steering / conditional admissibility).** The drive image of `z_(1,1)` at angle 1/3 pairs ≥ 0 with 25 exact
  product effects (its conditional states stay admissible: it is in `maxCone`), yet the pure state
  `(f_(1,1) + e^{iφ} f_(1,−1))/√2` of `K(Z_F)` (overlaps 1/2, 1/2, 0, 0 with the Bell-type states) pairs
  `−sin(1/3)/2 < 0` with it. Steering-type principles (candidate θ) are satisfied by the image while the cone is not
  preserved: an INDEPENDENT route for θ, with `K(Z_F)` the countermodel.
- **B5 (the NOT level).** `relC` holds for `Ad(CNOT)` with the NOT `Ad(X)` on all 16 basis tables, so NOT-preservation
  on the control with gate preservation gives NOT-preservation on the target; `K(Z_F)` is invariant under both
  idle-extended NOTs. Any principle that delivers only the NOT's extension (candidate η) excludes nothing.
- **B6c (countercontrols).** The drive alone closes to dimension 2; the `J` group with `Rz(π)` is finite; a product
  state's conditional admissibility is trivial.

## Anchors verified to resolve at L (line printed and read)
`StructuralClosure.lean:183` (`StructurallyClosed`), `:316` (`substratumClass_structurallyClosed`), `:365`
(`quantumArchitecture_iff_drives_of_closed`, hypothesis `StructurallyClosed 𝓘`), `:408`
(`substratum_extension_quantum_iff_drives`); `LiftAudit.lean:112` (`LayerFlowExecutable`: `∀ n t`, the ancilla a
spectator through `levelPerm σ n`), `:200` (`substratumTheory_not_layerFlowExecutable`); `ExecSource.lean:129`
(`obs_not_layerFlowExecutable`); `ReadWriteControl.lean:174` (`readWriteSourced_not_qm`);
`ReferenceExtension.lean:447` (`HasParallelReferenceExtension`), `:507`
(`control_not_implies_parallelReferenceExtension`); `CompletedOI.lean:129`, `:131`, `:147`, `:506`;
`ImplementationLocality.lean:370` (`ImplementationLocality`, a `def`), `:957`
(`observationalIndependence_of_implementationLocality`); `DerivedQ3.lean:222`; `KInfFoundations.lean:264`
(`ElementaryDrivability`: flow, NOT = flow t₀, `J`, `J_off_axis`), `:449` (`ball3Drive`: flow = `rot3`, `J = cyc3`);
`CompositeDimension.lean:224–225` (`relT`, `relC`); `GR.md:228` (OI⁺-1), `:244` (implementation locality), `:256`
(substratum-source form), `:262` (layer-flow form); `Main.md:628` (dynamical causal separation), `:564–568` (OI⁺
layered formulation); `ROADMAP.md:1001–1005` (K2), `:1014–1022` (K∞); `EmbeddedObservation.lean` and
`SubstratumInterface.lean` present. The ledger records `EQ3-P-RESULT.md`, `EQ3-AUDIT.md`, `EQ5-SOURCE-RESULT.md`,
`EQ5-SOURCE-AUDIT.md` and `pt/S2/RESULT.md` are present for the threads.

## What this does not establish (for the audit to hold the threads to)
- Nothing here decides whether any principle at L below the OI⁺ layer yields L2 (spectator stability); the
  expectation from the record is INDEPENDENT for every certified premise and CONDITIONAL on an OI⁺-type clause, but
  the threads decide with their own derivations and countermodels.
- Nothing here decides whether `LayerFlowExecutable` at level 1 together with implementation locality gives every
  level in the kernel's own terms, or whether the extension's structural closure is a hypothesis or a construction;
  thread D reads the definitions.
- The field-neutral transcriptions of α–ε and ζ are the threads'; the pre-audit fixes only the pair-cone facts.
