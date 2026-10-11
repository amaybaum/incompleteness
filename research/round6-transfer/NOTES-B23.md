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

Correction (appended 2026-10-11 15:34 UTC): the S0 heading's time "15:39 UTC" is wrong; the predictions were written at
15:33:40 UTC and committed at `f4597e46` before the dispatch (15:33:49 UTC, run 38151796092). Text unchanged.

## Run 38151796092 — result (recorded 2026-10-11 15:41:59 UTC)

Dispatch 1 of 1 at `fd364020`; Mathlib bridge job 114506598572: Build 15:37:57Z–15:40:39Z **failure**; Release gate
**skipped** (so neither `lean-axioms` nor `lean-manuscript` ran). Evidence: the job log through the GitHub job-log
tool, tail capped at 5000 lines (the log's last 5000 lines, sha256 `3e748d3e…4ffa` of the extracted text).

- **Errors** (the only three): `BridgeChannelTransfer.lean:100:13`, `:103:12`, `:105:9` — "failed to synthesize
  instance of type class PartialOrder ℂ", all in `channelTransfer_Q3` (the three `.PosSemidef` sites). Diagnosis:
  `Matrix.PosSemidef` over `ℂ` needs Mathlib's scoped `ComplexOrder`, which the module never opens
  (`BridgeConverge` has `open scoped ComplexOrder Matrix`). The defect is in `5d4b9833`'s text, untouched by the S0-b
  fixes; none of the three risk sites named in the S0 failed.
- **`#print axioms`** (7 of 7 reported): `channelTransfer_conjChannel`, `unitaryTransfer_of_channelTransfer`,
  `channelTransfer_of_identified_stateSpace`, `transfer_of_channelApproximation`, `bridge_channel_half`,
  `bridge_channel_half_of_selfDual` on `[propext, Classical.choice, Quot.sound]`; `channelTransfer_Q3` on
  `[propext, sorryAx, Classical.choice, Quot.sound]` (the error's elaboration placeholder).
- **Predictions scored.** Build success — REFUTED. Seven standard prints — REFUTED (six standard, one `sorryAx`).
  `lean-axioms` 6136 and the gate's 12 `lean-manuscript` problems — UNTESTED (step skipped).
- **Label.** B23-1 FAILED. A failed build makes nothing [D] (S0: [D] requires a recorded successful design build):
  the six statements that elaborated stay [W] with that elaboration recorded as evidence only.
- **Repair, not applied** (the owner's narrowing allows no further dispatch): add `open scoped ComplexOrder` to the
  module's opens. Proposed for round 7 as a logged amendment before any new dispatch; the failed text is kept as
  `lean/BridgeChannelTransfer.run38151796092.lean` (sha256 `c9909973…e96d`, equal to the dev blob at `fd364020`).
- **Productivity test.** Not a gem: the failure is an instance-scope defect, not a mathematical one, and exposes no
  premise of the route.
