"""
A5_OI_p_extrapolation.py — extract Π_T_OI(p²→0) intercept
at each N by p-extrapolation, using the same pattern as the LO p_extrapolation.py.

For each (N, m_reg, m_f):
  1. Compute Σ^{μν}_total(p_ext) at multiple p_ext = λ·κ·ê_0, λ ∈ {1, 2, 3}
     where κ = 2π/N is the smallest lattice momentum.
  2. At each λ, extract Π_T(p) = (Σ^{11} - Σ^{00}) / p̂² per C_A².
  3. Rescale by 1/Π_s^n_induced per topology, sum, and multiply by Π_s²
     (LO-convention "Π_T·Π_s²" quantity) to get a single value per λ.
  4. Linear fit Π_T·Π_s²(p²) = a + b·p², extract intercept a as the
     "p²→0 OI Π_T" at this N.

The output sequence {a(N)} is the input to N→∞ extrapolation (1/N² + Shanks)
for the c_2 estimate.

Cost: ~3× the single-(N, p_ext) cost. At N=6, ~3×3s = ~10s/(N, m_f).
"""
import numpy as np
import time
import sys
import os

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from paper_pi_s import compute_pi_s

from T1a_kite import kite_sigma
from T1b_vertex_correction import vertex_correction_sigma
from T1c_V4g_bubble import V4g_bubble_sigma
from T1d_V4g_tadpole import V4g_tadpole_sigma
from T1e_V4g_triple_line import V4g_triple_line_sigma
from G_a_ghost_square import ghost_square_sigma
from G_b_ghost_vertex_correction import ghost_vertex_correction_sigma
from G_c_ghost_triangle import ghost_triangle_sigma
from G_d_V4g_ghost_bubble import V4g_ghost_bubble_sigma

# Per-topology number of induced internal propagators (gluon + ghost).
N_INDUCED_PROPS = {
    'T1a': 5, 'T1b': 5, 'T1c': 4, 'T1d': 4, 'T1e': 3,
    'G_a': 5, 'G_b': 5, 'G_c': 5, 'G_d': 4,
}


def compute_all_sigmas_at_p(N, p_ext, m_reg, verbose=False):
    """Compute the 4×4 Σ^{μν} per C_A² for every topology at this (N, p_ext, m_reg).

    Returns dict keyed by 'T1a'..'G_d' with each value being a 4×4 matrix.
    Note these are STANDARD-QCD Σ values (not yet rescaled to substratum).
    """
    sigmas = {}
    t0 = time.time()
    sigmas['T1a'] = kite_sigma(N, p_ext, m_reg)
    if verbose: print(f"      T1a: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['T1b'] = vertex_correction_sigma(N, p_ext, m_reg)
    if verbose: print(f"      T1b: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['T1c'] = V4g_bubble_sigma(N, p_ext, m_reg)
    if verbose: print(f"      T1c: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['T1d'] = V4g_tadpole_sigma(N, p_ext, m_reg)
    if verbose: print(f"      T1d: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['T1e'] = V4g_triple_line_sigma(N, p_ext, m_reg)
    if verbose: print(f"      T1e: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['G_a'] = ghost_square_sigma(N, p_ext, m_reg)
    if verbose: print(f"      G_a: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['G_b'] = ghost_vertex_correction_sigma(N, p_ext, m_reg)
    if verbose: print(f"      G_b: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['G_c'] = ghost_triangle_sigma(N, p_ext, m_reg)
    if verbose: print(f"      G_c: {time.time()-t0:.1f}s")

    t0 = time.time()
    sigmas['G_d'] = V4g_ghost_bubble_sigma(N, p_ext, m_reg)
    if verbose: print(f"      G_d: {time.time()-t0:.1f}s")

    return sigmas


def extract_PiT_at_p(sigma_4x4, p_ext):
    """Extract Π_T = (Σ^{11} - Σ^{00})/p̂² for p_ext along ê_0."""
    p_0 = p_ext[0]
    if abs(p_0) < 1e-12:
        return np.nan
    p2_lat = (2 * np.sin(p_0 / 2))**2
    return (sigma_4x4[1, 1] - sigma_4x4[0, 0]) / p2_lat


def total_OI_PiT_at_p(sigmas_dict, p_ext, pi_s):
    """Combine all 9 topologies into induced Π_T·Π_s² at this p_ext.

    Each topology's Π_T (per C_A²) is rescaled by (1/Π_s)^n_induced
    where n_induced = #gluon + #ghost props. Then sum, multiply by Π_s²
    to match LO convention.
    """
    inv_pi_s = 1.0 / pi_s
    total_OI = 0.0
    contribs_OI = {}
    for k, sigma in sigmas_dict.items():
        pi_T_std = extract_PiT_at_p(sigma, p_ext)
        if np.isnan(pi_T_std):
            contribs_OI[k] = 0.0
            continue
        n = N_INDUCED_PROPS[k]
        contrib = pi_T_std * (inv_pi_s ** n)
        contribs_OI[k] = contrib
        total_OI += contrib

    return total_OI * pi_s**2, contribs_OI


def small_p_fit(p2_lats, Pi_values):
    """Linear fit Π(p²) ≈ a + b·p². Return (a, b)."""
    coef = np.polyfit(p2_lats, Pi_values, 1)
    return coef[1], coef[0]   # intercept (a), slope (b)


def p_extrapolate_at_N(N, m_reg, m_f, lambdas=(1, 2, 3), verbose=False):
    """Extract p²→0 intercept of Π_T_OI·Π_s² at this (N, m_reg, m_f)."""
    pi_s = compute_pi_s(N, m_f)
    inv_pi_s = 1.0 / pi_s
    if verbose:
        print(f"\n  N={N}, m_reg={m_reg}, m_f={m_f}, Π_s={pi_s:.4f}, 1/Π_s={inv_pi_s:.4f}")

    kappa = 2 * np.pi / N
    p2_lats = []
    PiT_PiS2_vals = []

    for lam in lambdas:
        p_ext = lam * kappa * np.array([1.0, 0.0, 0.0, 0.0])
        if verbose:
            print(f"  λ={lam}: p_0 = {p_ext[0]:.4f}")
        t_lam = time.time()
        sigmas = compute_all_sigmas_at_p(N, p_ext, m_reg, verbose=verbose)
        total_PiT_PiS2, _ = total_OI_PiT_at_p(sigmas, p_ext, pi_s)
        p2_lat = (2 * np.sin(p_ext[0] / 2))**2
        p2_lats.append(p2_lat)
        PiT_PiS2_vals.append(total_PiT_PiS2)
        if verbose:
            print(f"    p̂² = {p2_lat:.4f}, Π_T·Π_s² = {total_PiT_PiS2:+.5e}  [{time.time()-t_lam:.1f}s]")

    p2_lats = np.array(p2_lats)
    PiT_PiS2_vals = np.array(PiT_PiS2_vals)
    intercept, slope = small_p_fit(p2_lats, PiT_PiS2_vals)

    if verbose:
        print(f"  Linear fit: intercept = {intercept:+.5e}, slope = {slope:+.5e}")

    return intercept, slope, p2_lats, PiT_PiS2_vals, pi_s


def run_N_scan(N_list=(6,), m_reg=0.2, m_f=0.05, lambdas=(1, 2, 3), verbose=False):
    """Scan over N, extract p²→0 intercept at each N."""
    print(f"\n{'='*78}")
    print(f"=== p-extrapolation per N (m_reg={m_reg}, m_f={m_f}) ===")
    print(f"{'='*78}\n")
    print(f"  Lambdas = {lambdas} (p_ext = λ·κ·ê_0, κ = 2π/N)")
    print(f"  Each (N, λ) computes 9 topologies; 3λ values per N for fit.\n")

    print(f"{'N':>3}  {'Π_s(0)':>8}  {'p²→0 intercept':>17}  {'slope':>13}  {'time':>8}")
    print("-" * 65)

    intercepts = {}
    for N in N_list:
        t_N = time.time()
        intercept, slope, _, _, pi_s = p_extrapolate_at_N(N, m_reg, m_f, lambdas, verbose=verbose)
        dt = time.time() - t_N
        intercepts[N] = intercept
        print(f"{N:>3}  {pi_s:>8.4f}  {intercept:>+17.5e}  {slope:>+13.4e}  {dt:>7.1f}s",
              flush=True)

    return intercepts


def shanks(values):
    """Shanks acceleration (per reproduce_AB.py)."""
    out = []
    for i in range(1, len(values) - 1):
        num = values[i+1] * values[i-1] - values[i]**2
        denom = values[i+1] - 2*values[i] + values[i-1]
        if abs(denom) > 1e-12:
            out.append(num / denom)
    return out


def extrapolate_to_infty(intercepts):
    """Apply 1/N² fit and Shanks acceleration to extract N→∞ value."""
    Ns = sorted(intercepts.keys())
    vals = np.array([intercepts[n] for n in Ns])

    print(f"\n--- N→∞ extrapolation of c_2(N) sequence ---")
    print(f"  Sequence: N = {Ns}")
    print(f"  Values:   {[f'{v:+.4e}' for v in vals]}")

    if len(Ns) >= 3:
        Ns_arr = np.array(Ns, dtype=float)
        # Use last 3 points for 1/N² fit
        coef = np.polyfit(1.0 / Ns_arr[-3:]**2, vals[-3:], 1)
        print(f"  1/N² fit (last 3): c_2(∞) = {coef[1]:+.4e}, slope = {coef[0]:+.4e}")

    s1 = shanks(vals.tolist())
    s2 = shanks(s1) if len(s1) >= 3 else []
    if s1: print(f"  Shanks-1: {[f'{v:+.4e}' for v in s1]}")
    if s2: print(f"  Shanks-2: {[f'{v:+.4e}' for v in s2]}")


if __name__ == "__main__":
    print("\n*** p-extrapolation per N for substratum c_2 ***\n")

    # First-pass: small N to validate the wrapper. N=6 gives ~3 × ~5s = ~15s
    intercepts = run_N_scan(N_list=[6], m_reg=0.2, m_f=0.05, lambdas=(1, 2, 3), verbose=True)

    print(f"\n*** Final intercept at N=6: {list(intercepts.values())[0]:+.5e} ***")
    print(f"\n  OI prediction for c_2/C_A² = -128 (with A·B = 48)")
    print(f"  Ratio at N=6: {list(intercepts.values())[0] / (-128):+.5e}")
    print(f"  (Expect strong finite-N suppression, just as LO had A·B(N=8) = 0.8 vs 48)")
