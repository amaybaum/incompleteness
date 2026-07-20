# main_repro — reproducibility package for "The Equivalence of Quantum Mechanics and Embedded Observation"

Scripts reproducing the numerical checks referenced in the paper. Python 3 + numpy only.
Each script prints explicit PASS/FAIL against the claim it verifies.

| Script | Paper claim | Expected output | Runtime |
|---|---|---|---|
| `minimal_model.py` | §2.4 minimal model: T(1,0), T(2,0)=I un-mixing, Λ(2,1) negativity ⇒ **P-indivisible**; process-tensor memory check P(x₂=0\|x₁=1,x₀=0)=1 vs 1/3 | ALL PASS (exact enumeration) | <1 s |
| `coboundary_nullspace.py` | Reconstruction lemma (ancilla-marginal form): linearized idempotency constraint has null space of dimension **exactly D−1** for generic Ĥ, across (n,mₐ)=(3,4),(2,3),(4,2),(3,3),(2,4) | ALL PASS (3 random Ĥ per case) | ~2 min |
| `mixing_battery.py` | Substratum chaotic-mixing diagnostics cited in the Bell section: spectral continuity (rounded H≈0.931 vs linear 0.126), thermalization (autocorr 0.019 vs 0.543), comparative cycle consolidation, orbit non-fragmentation | Matches archived RESULTS (journal §B.2.575, battery2) | ~3 min |
| `lyapunov_v3.py` | Two-trajectory Lyapunov: **λ_max > 0** on the realized rounded bijection (quantitative rate ensemble-dependent, as stated in the paper) | PASS, λ>0 all seeds, growth to saturation | ~1 min |

Provenance: `mixing_battery.py` = `battery2.py` (corrected version) and `lyapunov_v3.py` adapts
`b1_v3.py` from the research journal's archived kit (§B.2.575), with an auto-selected exponential
fit window replacing the hand-tuned one (the hand window assumed slow divergence and returns zero
points when divergence is fast; the measurement construction — map, perturbation δ=1 at q=2¹⁶,
cone-restricted circular RMS, seeds — is unchanged). The archived kit's honest caveat is preserved:
the qualitative chaos result (λ_max>0) is the paper's claim; the specific historical rate value is
spec-dependent and not claimed.

The visible-sector trace-out and cycle-structure C programs cited alongside these diagnostics live
in `../oi_lattice_code/trace_out_fractional/`.
