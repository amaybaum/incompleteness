# Owner's third note: the two Origin targets (received 2026-10-10; input for the later Origin audit, not for U/X)

Verbatim mathematical content:
- Rung 1 refined: a non-ones-fixing operation is necessary (instAvail_unitary_fixes_ones) but not sufficient:
  Z = diag(1, −1) moves the all-ones ray yet creates no coherence from a basis-diagonal state and turns no diagonal
  measurement into a coherence-sensitive one. The appropriate target is a physically sourced, discrete, NON-MONOMIAL
  coherent mixer together with its permitted preparation, reuse and readout protocol.
- Operational test: |0⟩ —H→ |+⟩ —H→ |0⟩ with probability 1; with complete path dephasing between the mixers, 1/2.
  A full spatial fringe additionally needs a position-dependent relative phase or equivalent screen dynamics.
- Discrete Origin: derive an accessible coherent mixer from the substratum without assuming the desired quantum
  operation; establish an exact interference witness with the available preparations and measurements.
- Continuous Origin: derive the continuously driven transition of the minimal repertoire; `oiPlusMin_iff_qm` then
  supplies the complete finite operational theory under the other stated hypotheses.
- The first is deliberately weaker; success there establishes neither the second nor a unique selection of quantum
  theory over classical constructions. Methodological requirement for both: the operation must be derived from OI's
  substratum, not introduced through an interface already containing the desired coherence.
- No alteration to U or X; the distinction belongs in the later Origin audit.

Coordinator's confirmations (exact, trivial): H-sandwich P(0) = 1, with dephasing 1/2; Z(1,1)ᵀ = (1,−1) and Z fixes
diagonal states. Corpus anchor: the landed interference witness has exactly this sandwich form —
`HasAncillaQubitInterference T := T.prepAvail 2 (pureAttach 2 0) ∧ T.availExt 2 Unit (fun _ => conjChannel (ancMix A))`
(AncillaInterference.lean:161–163), with `mix_seed` (:172) and `interference_branch` (:239) [K]; the stated
configuration-level access cannot supply the mixer (`permClass_onesFixing` PhaseSource.lean:79 +
`instAvail_unitary_fixes_ones` InstrumentRealization.lean:398). The non-monomial criterion matches S2's class `𝒞_mono`
(frame-monomial operations create no coherence in the frame basis).
