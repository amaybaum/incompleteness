# main_repro — reproducibility package for "The Equivalence of Quantum Mechanics and Embedded Observation"

Scripts reproducing the numerical checks referenced in the paper. Python 3 + numpy only.
Each script prints explicit PASS/FAIL against the claim it verifies.

| Script | Paper claim | Expected output | Runtime |
|---|---|---|---|
| `minimal_model.py` | §2.4 six-hidden-state model: T(1,0), T(2,0)=I un-mixing, Λ(2,1) negativity ⇒ **P-indivisible**; process-tensor memory check P(x₂=0\|x₁=1,x₀=0)=1 vs 1/3 | ALL PASS (enumeration of all twelve states, floating point) | <1 s |
| `coboundary_nullspace.py` | Reconstruction lemma (ancilla-marginal form): linearized idempotency constraint has null space of dimension **exactly D−1** for generic Ĥ, across (n,mₐ)=(3,4),(2,3),(4,2),(3,3),(2,4) | ALL PASS (3 random Ĥ per case) | ~2 min |
| — | *the same claim in exact arithmetic*: `../oi_lattice_code/foundations/phaselock_probes.py` certifies ker = coboundary over GF(p²) at seven block structures, which is what carries the genericity argument of §3.4; the floating-point script above is its companion, not its evidence | ALL CHECKS PASS | ~5 s |
| `mixing_battery.py` | Rounded-candidate numerical diagnostics cited in the Bell section: spectral continuity (rounded H≈0.931 vs linear 0.126), thermalization (autocorr 0.019 vs 0.543), comparative cycle consolidation | Matches archived RESULTS (journal §B.2.575, battery2) | ~3 min |
| `lyapunov_v3.py` | Two-trajectory separation to saturation on the rounded candidate bijection; fitted slopes are window-dependent diagnostics, not Lyapunov exponents (SM §4.2) | PASS: separation to saturation on every seed | ~1 min |

Provenance: `mixing_battery.py` = `battery2.py` (corrected version) and `lyapunov_v3.py` adapts
`b1_v3.py` from the research journal's archived kit (§B.2.575), with an auto-selected exponential
fit window replacing the hand-tuned one (the hand window assumed slow divergence and returns zero
points when divergence is fast; the measurement construction — map, perturbation δ=1 at q=2¹⁶,
cone-restricted circular RMS, seeds — is unchanged). The rounded candidate's numerical chaos evidence comes from
`mixing_battery.py`'s diagnostics, not from these fitted slopes. The separation script's
PASS criterion is independent of the fitted slope: finite separation must start below
half the reference saturation scale and exceed it on every seed. These measurements
do not establish a positive Lyapunov exponent or mixing of the realized hidden sector.

The visible-sector trace-out and cycle-structure C programs cited alongside these diagnostics live
in `../oi_lattice_code/trace_out_fractional/`.

Ordinary PR CI runs the default separation diagnostic and its bounded no-perturbation
countercontrol in the existing Numerical probes / core B job. The commands are
`python3 -I -B papers/main_repro/lyapunov_v3.py` and the same command with
`--no-perturbation-control`. The countercontrol uses L=4, q=256 and 80 steps: its
identical twins must have zero separation and fail the saturation criterion on every
seed. Exit status is zero only when each command's stated condition holds; no fitted
slope is a success criterion. The control's PASS confirms the expected failure of
saturation, not a separation claim.
