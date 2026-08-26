# Verifying

## Requirements

- Lean 4 (any recent release; the proof files are self-contained — no Mathlib, no lake
  project, zero imports).
- Python 3 with NumPy (SciPy additionally for `gauge_certificates_probe.py`).

## Kernel check

    cd verification/lean
    lean OI_Gauge_Certificates.lean && lean OI_Structural_Core.lean \
      && lean OI_Staggered_Relations.lean && lean OI_Regulator_Symmetry.lean

A clean exit is the certificate. The files use only core tactics (`calc`, `rw`, `decide`,
structural induction); `decide` targets are integer identities over explicitly generated
finite actions — the 24-element cubic rotation group, and the 384- and 96-element signed
permutation groups of the regulator sector.

## Numerical probes

    python3 gauge_certificates_probe.py       # G1–G6
    python3 structural_core_probe.py          # R1–R6
    python3 staggered_relations_probe.py      # S1–S6
    python3 structural_chain_probe.py         # C1–C5
    python3 representation_bridge_probe.py    # B1–B7, and B5b

Every line prints `PASS` with the verified content — 31 in total. The probes are
self-contained and deterministic (fixed seeds); integer-identity claims are checked in exact
int64 or rational arithmetic, not floating point.

## Continuous checking

`.github/workflows/verify.yml` runs the kernel check and all five probes on every change to
`verification/`. Each proof file is checked separately and the failures are summed, so a
rejection in one file does not hide the state of the others. The kernel verdict is
version-relative: the workflow installs `leanprover/lean4:stable` and reports the resolved
version in its own log, which is the version any given run certifies.

## Release checklist

- [ ] All four `lean` commands exit cleanly.
- [ ] All five probes print their full PASS sets.

Status: both layers pass in CI. A green run certifies the toolchain that run resolved, and
nothing about any other.
