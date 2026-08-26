# Verifying

## Requirements

- Lean 4 (any recent release; the five core proof files are self-contained — no Mathlib, no
  lake project, zero imports).
- For the bridge only: `elan`/`lake` and network access, to fetch mathlib4 `v4.33.0` and its
  build cache. Nothing in the core check needs this, and the two are kept separable on purpose.
- Python 3 with NumPy (SciPy additionally for `gauge_certificates_probe.py`).

## Kernel check

    cd verification/lean
    lean OI_Gauge_Certificates.lean && lean OI_Structural_Core.lean \
      && lean OI_Staggered_Relations.lean && lean OI_Regulator_Symmetry.lean \
      && lean OI_Structural_Chain.lean

A clean exit is the certificate. The files use only core tactics (`calc`, `rw`, `decide`,
structural induction); `decide` targets are integer identities over explicitly generated
finite actions — the 24-element cubic rotation group, the 384- and 96-element signed
permutation groups of the regulator sector, and the 48-element group of the cubic quadratic
invariant.

## Mathlib bridge

    cd verification/lean-mathlib
    lake exe cache get && lake build

Separate project, separate pinned toolchain, separate verdict. It carries the two statements
that contain the word *dimension* — the averaging identity and the equivariant-map dimension
formula, both derived from Mathlib rather than reproved — and the transport of the cubic data
onto a `Representation` that turns the core layer's `72` into `dim Hom_G(V₆, V₆) = 3`.

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

`.github/workflows/verify.yml` runs on every change to `verification/`, in **three independent
jobs**: the zero-import kernel check, the Mathlib bridge, and the probes. They are independent
on purpose — a breakage in the bridge, which depends on a large external library, can never be
mistaken for a verdict on the self-contained files, and vice versa. Within the kernel job each
proof file is checked separately and the failures are summed, so a rejection in one file does
not hide the state of the others.

**The two kernel verdicts are version-relative, and to different versions.** The core job
installs `leanprover/lean4:stable` and reports the resolved version in its own log; the bridge
job is pinned to `leanprover/lean4:v4.33.0`, matching the Mathlib tag it requires. A green run
certifies those toolchains and nothing about any other.

## Release checklist

- [ ] All five `lean` commands exit cleanly.
- [ ] All five probes print their full PASS sets.
- [ ] The bridge builds: `cd verification/lean-mathlib && lake exe cache get && lake build`.

Status: all three jobs pass in CI.
