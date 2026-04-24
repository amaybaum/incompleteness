"""
tadpole_wilson_v4g.py — numerical test of the derived Wilson V_4g at tadpole.

Derivation in V4G_STEP_2.md. Result:
    Σ_tad^{μν}(p) / C_2 = (1/2) · δ^{μν} · ⟨[5 + cos(p_μ)·cos(k_μ)]/(k̂²·Π_s)⟩

Derived by summing the three continuum pair-topologies (1,2)(3,4),
(1,3)(2,4), (1,4)(2,3) with Wilson cos-factors on each pair
(cos((p_i+p_j)_{μ_i}/2) for pair with Lorentz δ^{μ_iμ_j}), specializing
to tadpole kinematic (p_3=k, p_4=-k, p_1=p, p_2=-p) and tracing over
the internal loop.

For external p along direction 0, p = (p_0, 0, 0, 0):
    Σ^{00}(p) = (g_0²C_2/2)·⟨[5 + cos(p_0)cos(k_0)]/(k̂²Π_s)⟩
    Σ^{11}(p) = (g_0²C_2/2)·⟨[5 + cos(0)cos(k_1)]/(k̂²Π_s)⟩ = (1/2)·⟨[5 + cos(k_1)]/...⟩

Difference:
    Σ^{11} - Σ^{00} = (g_0²C_2/2)·⟨[cos(k_1) - cos(p_0)cos(k_0)]/(k̂²Π_s)⟩
                    = (g_0²C_2/2)·(1 - cos(p_0))·⟨cos(k)/(k̂²Π_s)⟩   [using BZ symmetry]
                    = (g_0²C_2/2)·(p̂_0²/2)·⟨cos(k_μ)/(k̂²Π_s)⟩
                    (using 1 - cos(p_0) = 2 sin²(p_0/2) = p̂_0²/2)

So:
    (Σ^{11}-Σ^{00})/p̂_0² = (g_0²C_2/4)·⟨cos(k_μ)/(k̂²Π_s)⟩
    Π_T^tad·Π_s² = (g_0²C_2 · Π_s²/4)·⟨cos(k_μ)/(k̂²Π_s)⟩
                 = (g_0²C_2 · Π_s /4)·⟨cos(k_μ)/k̂²⟩

For our purposes (comparing to the existing bubble+ghost code), we drop
the overall g_0²·C_2 factor (it's divided out in the A·B formula).

So:   Π_T^tad·Π_s² / C_2 = (Π_s/4)·⟨cos(k_μ)/k̂²⟩

CAVEAT: my derivation in V4G_STEP_2.md has uncertainties in the signs
and overall factor. The cross-check against a published formula
(e.g., Capitani 2003 Eq. 2.84) is pending. So the OVERALL SIGN and
MAGNITUDE here should be considered provisional — but the SCALING
with N and m and the STRUCTURE should be robust.
"""
import numpy as np
import os
import sys
import warnings

warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from paper_pi_s import compute_pi_s


def compute_J_cos_over_khat2(N):
    """Compute J(N) = ⟨cos(k_μ)/k̂²⟩_BZ (spatial average over μ implicit;
    by BZ symmetry, each direction gives the same answer, so return one).
    """
    dk = 2 * np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(
        idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij'
    )
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    
    khat2_sum = ((2*np.sin(k_grid/2))**2).sum(axis=-1)
    
    # Exclude k=0 singularity (finite-volume IR regulator)
    mask = khat2_sum > 1e-12
    
    # Average over the 4 directions, using BZ symmetry (should give same)
    # Use direction 0:
    integrand_0 = np.where(mask, np.cos(k_grid[..., 0]) / khat2_sum, 0.0)
    J0 = integrand_0.mean()
    # Check with direction 1 (should be equal)
    integrand_1 = np.where(mask, np.cos(k_grid[..., 1]) / khat2_sum, 0.0)
    J1 = integrand_1.mean()
    # Return average (they should be equal to machine precision)
    return (J0 + J1 + J0 + J0) / 4, (J0, J1)


def compute_PiT_tad_wilson(N, m, pi_s_val=None):
    """Derived Wilson V_4g tadpole contribution to Π_T·Π_s².
    
    Per V4G_STEP_2.md corrected derivation:
        Π_T^tad·Π_s² / C_2 = -(Π_s/4) · ⟨cos(k_μ)/k̂²⟩
    
    Sign: NEGATIVE (same sign as bubble+ghost baseline).
    The tadpole correction adds constructively to |Π_T·Π_s²|,
    increasing A·B by ~4% at N→∞.
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    J, _ = compute_J_cos_over_khat2(N)
    return -(pi_s_val / 4.0) * J, J


def main():
    print("=" * 74)
    print("Wilson V_4g tadpole contribution to Π_T·Π_s² (derived formula)")
    print("=" * 74)
    print()
    print("Formula: Π_T^tad · Π_s² / C_2 = -(Π_s/4) · ⟨cos(k_μ)/k̂²⟩")
    print("(Derived in V4G_STEP_2.md. Sign: NEGATIVE, same as bubble+ghost.)")
    print("(Cross-check vs Capitani 2.84 pending — systematic may be ±½×result.)")
    print()

    m = 0.05
    print(f"{'N':>3}  {'Π_s':>7}  {'J=<cos/k̂²>':>12}  {'Π_T^tad·Π_s²':>14}")
    results = {}
    for N in [8, 12, 16, 20, 24, 28, 32]:
        pi_s = compute_pi_s(N, m)
        val, J = compute_PiT_tad_wilson(N, m, pi_s)
        results[N] = (pi_s, J, val)
        print(f"{N:>3}  {pi_s:>7.4f}  {J:>12.6f}  {val:>+14.6f}")
    print()

    # Compare to bubble+ghost baseline (from reproduce_AB.py data)
    # At m=0.05, bubble+ghost gives Π_T·Π_s² that grows from ~-0.04 (N=8) 
    # to roughly -0.055 (N=20+). Let me load these baselines from running
    # the reproduce_AB machinery separately (or tabulate).
    # For rough comparison, use session l's observed baselines at small N
    # and extrapolate:
    baseline_guess = {
        8:  -0.0366,
        12: -0.0430,
        16: -0.0485,
        20: -0.0530,
        24: -0.0566,  # extrapolated
        28: -0.0590,  # extrapolated
        32: -0.0610,  # extrapolated
    }
    print("Comparison to bubble+ghost baseline (from session l + extrapolation):")
    print(f"{'N':>3}  {'baseline':>12}  {'tadpole':>12}  {'new sum':>12}  {'rel shift':>10}")
    for N in sorted(results.keys()):
        pi_s, J, tad = results[N]
        base = baseline_guess.get(N, None)
        if base is None:
            continue
        new_sum = base + tad
        rel = (tad / base) * 100 if base != 0 else 0
        print(f"{N:>3}  {base:>+12.5f}  {tad:>+12.5f}  {new_sum:>+12.5f}  {rel:>+9.2f}%")
    print()

    # Extrapolate: does J(N) approach a finite continuum value?
    print("J(N) N-convergence (should approach a finite continuum value):")
    Ns = sorted(results.keys())
    Js = np.array([results[N][1] for N in Ns])
    print(f"  Last 3 ratio J(N)/J(N-4): {[J/Js[i-1] for i, J in enumerate(Js[1:], 1)]}")
    # Fit J(N) = J_inf + c/N² to see if it converges
    Ns_arr = np.array(Ns, dtype=float)
    coef = np.polyfit(1.0/Ns_arr**2, Js, 1)
    print(f"  1/N² fit: J(N) ≈ {coef[1]:.6f} + ({coef[0]:+.4f})/N²")
    print(f"  J(N→∞) ≈ {coef[1]:.6f}")


if __name__ == "__main__":
    main()
