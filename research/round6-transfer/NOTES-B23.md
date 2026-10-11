# NOTES-B23 — the O14 channel candidate against the bridge's construction (narrowed)

Scope in this batch (S0-b; owner's narrowing): the Lean fixes and one design build of the existing module
`OIBridge/BridgeChannelTransfer.lean` on `dev-bridge/r6-channel-transfer`. No new theorem, no exact checker, no
further dispatch. DEFERRED to round 7: the exact-check plan and its controls, the placement question beyond B22's
channel-form verdict, and S6-SURFACE.

**Question.** Does the module, as fixed, build: `bridge_channel_half` (closed `K`, (T^ch)_𝓘, the repeat-until-success
witness `AvailableChannelApproximation 𝓘 zPh` and `J` available ⇒ invariance under `actT R_z(θ₀)` and `actT J`), its
self-dual variant, the transfer lemmas and the restated identified-state-space lemma?

**Productivity test (§A.31).** A gem only if the build turns the module's statements from UNBUILT into [D] and exposes
or rules out a hidden premise of the route (beyond the explicit (T^ch), closedness and the witness). A green build of
statements whose hypotheses are already explicit is CONFIRMING, not a gem.

## S0 — predictions, written 2026-10-11 15:39 UTC before the dispatch

Module at `fd364020` (sha256 `c9909973…e96d`), branch tree = `16e75fbe` + the three E19 modules + this module.

- **Build:** success. Risk sites named in advance: `rw [← he]` matching the coercion of `amplRefL (Fin 2) Φ`;
  `Filter.Eventually.of_forall`; the closing `rfl` of `channelTransfer_conjChannel` after `rw`.
- **`#print axioms`:** 7 lines for this module, each `[propext, Classical.choice, Quot.sound]` —
  `channelTransfer_conjChannel`, `unitaryTransfer_of_channelTransfer`, `channelTransfer_of_identified_stateSpace`,
  `channelTransfer_Q3`, `transfer_of_channelApproximation`, `bridge_channel_half`, `bridge_channel_half_of_selfDual`.
  The other design modules print as in their green runs (38124442150, 38134245361).
- **`lean-axioms`:** OK, 6136 named results (6129 without this module — L's 5860 plus 269 distinct short names of
  the eleven carried design modules — plus 7), no `sorryAx`.
- **Release gate:** red only at `lean-manuscript`, 12 problems (the twelve design modules without a census
  disposition); every other step PASS. Workflow: one failure (Mathlib bridge, at the gate), every other job success.
- **Not predicted to change any label:** a green build makes the module's statements [D]; every hypothesis stays
  explicit — (T^ch)_𝓘 introduced, the witness [W] + [X] (O14-T9), closedness from H3 in the variant.
