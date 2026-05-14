"""
p_extrapolation.py — For each N, compute (Σ^{11}-Σ^{00})/p̂² at multiple λ,
fit Π(p²) vs p² and extract the p²→0 limit. Then extrapolate across N.

This is the proper procedure for extracting A·B from lattice data.
"""
import numpy as np
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bubble_at_finite_p import compute_bubble_at_p
from ghost_self_energy import compute_ghost_sigma_at_p
from paper_pi_s import compute_pi_s


def compute_sum_at_p(N, m, p_ext, pi_s_val, use_induced_ghost=True):
    """Return Σ_bubble + Σ_ghost at p_ext. Returns 4x4 matrix per C_2."""
    Sigma_bub, _ = compute_bubble_at_p(N, m, p_ext, pi_s_val=pi_s_val)
    Sigma_gh = compute_ghost_sigma_at_p(N, p_ext, use_induced=use_induced_ghost,
                                         pi_s_val=pi_s_val, m=m)
    return Sigma_bub + Sigma_gh


def extract_PiT_times_pis2(Sigma, p_ext, pi_s):
    """Compute (Σ^{11} - Σ^{00})/p̂² · Π_s² given p_ext along direction 0."""
    p_0 = p_ext[0]
    if abs(p_0) < 1e-12:
        return np.nan
    p2_lat = (2*np.sin(p_0/2))**2
    return (Sigma[1, 1] - Sigma[0, 0]) / p2_lat * pi_s**2


def small_p_fit(p2_lats, Pi_values):
    """Fit Π(p²) ≈ a + b·p² and return a (the p²→0 limit)."""
    # Linear fit in p²
    coef = np.polyfit(p2_lats, Pi_values, 1)
    # a = intercept, b = slope
    return coef[1], coef[0]   # a (intercept), b (slope)


def main():
    m = 0.05
    results = {}
    print("Extracting p²→0 limit at each N:\n")
    
    for N in [6, 8, 12, 16, 20]:
        kappa = 2*np.pi / N
        pi_s = compute_pi_s(N, m)
        p2_lats = []
        Pi_vals = []
        t_tot = time.time()
        for lam in [1, 2, 3]:
            p_ext = lam * kappa * np.array([1, 0, 0, 0])
            Sigma = compute_sum_at_p(N, m, p_ext, pi_s_val=pi_s, use_induced_ghost=True)
            pi_t = extract_PiT_times_pis2(Sigma, p_ext, pi_s)
            p2_lat = (2*np.sin(p_ext[0]/2))**2
            p2_lats.append(p2_lat)
            Pi_vals.append(pi_t)
            print(f"  N={N} λ={lam}: p̂²={p2_lat:.4f}  Π_sum·Π_s²={pi_t:+.5e}", flush=True)
        dt = time.time() - t_tot
        # Extrapolate to p²=0
        p2_arr = np.array(p2_lats)
        Pi_arr = np.array(Pi_vals)
        intercept, slope = small_p_fit(p2_arr, Pi_arr)
        print(f"  N={N} fit: Π(p²=0)={intercept:+.5e}, slope={slope:+.5e}  [total {dt:.1f}s]")
        print()
        results[N] = {'intercept': intercept, 'slope': slope, 'p2': p2_arr, 'Pi': Pi_arr, 'pi_s': pi_s}
    
    # Now extrapolate intercepts to N→∞
    print("\n=== Cross-N extrapolation of Π(p²=0)·Π_s² ===")
    Ns = sorted(results.keys())
    intercepts = np.array([results[n]['intercept'] for n in Ns])
    print(f"{'N':>4}  {'Π(0)·Π_s²':>12}")
    for N, intr in zip(Ns, intercepts):
        print(f"{N:>4}  {intr:+.5e}")
    
    # Fit in 1/N² (common for lattice)
    Ns_arr = np.array(Ns, dtype=float)
    coef = np.polyfit(1.0/Ns_arr**2, intercepts, 1)
    print(f"\n1/N² extrapolation: Π(0, N→∞)·Π_s² = {coef[1]:+.5e}")
    print(f"                    slope in 1/N²  = {coef[0]:+.5e}")
    
    # Convert to an estimate of A·B
    # The formula: A·B = -(4π) * Π(0) ... we need to work out the exact normalization.
    # For now, report the extracted number and note the work-in-progress normalization.
    return results


if __name__ == "__main__":
    import warnings
    warnings.filterwarnings('ignore')
    main()
