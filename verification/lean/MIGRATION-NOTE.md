# Migration note (b404): the Lean verification layer's canonical home

Owner directive (b404): verification results are stored directly in the repo, not only in
the session transfer. This directory is the canonical, runnable home of the LEAN-FULL layer.

Provenance and byte-identity: `OI_B397_Pilot.lean`, `LEAN-PILOT-README.md`, and
`INVENTORY.md` are byte-identical copies of the b399/b403 round artifacts
(`probes_b399/OI_B397_Pilot.lean`, `probes_b399/LEAN-PILOT-README.md`,
`research/b403-leanfull-inventory-and-order.md`). `b399_lean_pilot_probe.py` differs from
its round original by exactly one documented change: the mirror's AL5 lint resolved the
Lean file at an absolute session path; the repo copy resolves it relative to this directory
(`os.path.dirname(os.path.abspath(__file__))`). No other bytes differ; the transfer
originals are retained unchanged for lineage.

Additivity proof: `MANIFEST-baseline-3.0.0.sha256` records the SHA-256 of every file in the
repo immediately before this layer was created; the b404 probe re-hashes that set and
asserts byte-identity. The published 3.0.0 artifact set is untouched; the freeze statement
is henceforth "published set byte-identical (manifest-proven) + verification layer
additive."

Gate: `lean OI_B397_Pilot.lean` in this directory (see LEAN-PILOT-README.md). L2 and later
LEAN-FULL files are authored here, behind the gate.
