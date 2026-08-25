# Verifying

## Requirements

- Lean 4 (any recent release; the proof files are self-contained — no Mathlib, no lake
  project, zero imports).
- Python 3 with NumPy (SciPy additionally for `gauge_certificates_probe.py`).

## Kernel check

    cd verification/lean
    lean OI_Gauge_Certificates.lean && lean OI_Structural_Core.lean

A clean exit is the certificate. The files use only core tactics (`calc`, `rw`, `decide`,
structural induction); `decide` targets are small integer identities over an explicitly
generated 24-element action.

## Numerical probes

    python3 gauge_certificates_probe.py       # G1–G5
    python3 structural_core_probe.py          # R1–R6
    python3 structural_chain_probe.py         # C1–C5
    python3 representation_bridge_probe.py    # B1–B7

Every line prints `PASS` with the verified content. The probes are self-contained and
deterministic (fixed seeds); integer-identity claims are checked in exact int64 or
rational arithmetic, not floating point.

## Release checklist

- [ ] Both `lean` commands exit cleanly.
- [ ] All four probes print their full PASS sets.

Status: the numerical probes pass in the maintained environment; the kernel check is run
as part of tagging a release.
