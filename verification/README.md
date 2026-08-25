# verification/ — the additive proof-verification layer (owner-directed, b404)

This directory holds machine-checkable verification artifacts for the OI framework,
beginning with the LEAN-FULL Lean 4 audit (`lean/`). It is strictly additive to the
published 3.0.0 artifact set: `lean/MANIFEST-baseline-3.0.0.sha256` records every
pre-existing file's hash, and the session-transfer probes re-verify that set byte-identical
each round. Entry gate for the Lean program: `cd lean && lean OI_B397_Pilot.lean`.
