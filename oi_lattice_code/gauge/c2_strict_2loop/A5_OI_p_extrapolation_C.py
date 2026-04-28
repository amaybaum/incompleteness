"""
A5_OI_p_extrapolation_C.py — C-accelerated p-extrapolation per N for substratum c_2

Same logic as A5_OI_p_extrapolation.py, but uses C binaries for the O(N^8) topologies
via the c_topology_wrapper module.

Speedup at N=6: ~7x overall (3.3s vs 22s for all 9 at one p_ext).
At N=8: ~22s for kite alone (in C); estimated ~30s for all 9 at one p_ext.
At N=10: estimated ~3 min for all 9 at one p_ext.

Per-N totals (3 lambda values per p-extrapolation):
  N=6: ~10s
  N=8: ~90s
  N=10: ~9 min — feasible only in batch
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
from c_topology_wrapper import compute_all_sigmas_at_p_C

# Per-topology induced prop count (gluon + ghost)
N_INDUCED_PROPS = {
    'T1a': 5, 'T1b': 5, 'T1c': 4, 'T1d': 4, 'T1e': 3,
    'G_a': 5, 'G_b': 5, 'G_c': 5, 'G_d': 4,
}


def extract_PiT_at_p(sigma_4x4, p_ext):
    p_arr = np.asarray(p_ext, dtype=float)
    p_0 = p_arr[0]
    if abs(p_0) < 1e-12:
        return np.nan
    p2_lat = (2 * np.sin(p_0 / 2))**2
    return (sigma_4x4[1, 1] - sigma_4x4[0, 0]) / p2_lat


def total_OI_PiT_at_p(sigmas_dict, p_ext, pi_s):
    """Combine all 9 topologies into induced Π_T·Π_s²."""
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
    coef = np.polyfit(p2_lats, Pi_values, 1)
    return coef[1], coef[0]


def p_extrapolate_at_N(N, m_reg, m_f, lambdas=(1, 2, 3), verbose=False):
    pi_s = compute_pi_s(N, m_f)
    if verbose:
        print(f"\n  N={N}, m_reg={m_reg}, m_f={m_f}, Π_s={pi_s:.4f}")

    kappa = 2 * np.pi / N
    p2_lats = []
    PiT_PiS2_vals = []
    per_lambda_contribs = []

    for lam in lambdas:
        p_ext = lam * kappa * np.array([1.0, 0.0, 0.0, 0.0])
        if verbose:
            print(f"  λ={lam}: p_0={p_ext[0]:.4f}")
        t_lam = time.time()
        sigmas, _timings = compute_all_sigmas_at_p_C(N, p_ext, m_reg, verbose=verbose)
        total_PiT_PiS2, contribs = total_OI_PiT_at_p(sigmas, p_ext, pi_s)
        per_lambda_contribs.append(contribs)
        p2_lat = (2 * np.sin(p_ext[0] / 2))**2
        p2_lats.append(p2_lat)
        PiT_PiS2_vals.append(total_PiT_PiS2)
        if verbose:
            print(f"    p̂²={p2_lat:.4f}, Π_T·Π_s²={total_PiT_PiS2:+.5e}  [{time.time()-t_lam:.1f}s]")

    p2_lats = np.array(p2_lats)
    PiT_PiS2_vals = np.array(PiT_PiS2_vals)
    intercept, slope = small_p_fit(p2_lats, PiT_PiS2_vals)

    if verbose:
        print(f"  Linear fit: intercept = {intercept:+.5e}, slope = {slope:+.5e}")

    return {
        'intercept': intercept, 'slope': slope, 'pi_s': pi_s,
        'p2_lats': p2_lats, 'vals': PiT_PiS2_vals,
        'per_lambda': per_lambda_contribs,
    }


def shanks(values):
    out = []
    for i in range(1, len(values) - 1):
        num = values[i+1] * values[i-1] - values[i]**2
        denom = values[i+1] - 2*values[i] + values[i-1]
        if abs(denom) > 1e-12:
            out.append(num / denom)
    return out


def extrapolate_to_infty(intercepts):
    Ns = sorted(intercepts.keys())
    vals = np.array([intercepts[n] for n in Ns])
    print(f"\n--- N→∞ extrapolation of c_2(N) ---")
    print(f"  Sequence: N = {Ns}")
    print(f"  Values:   {[f'{v:+.4e}' for v in vals]}")
    if len(Ns) >= 3:
        Ns_arr = np.array(Ns, dtype=float)
        coef = np.polyfit(1.0 / Ns_arr[-3:]**2, vals[-3:], 1)
        print(f"  1/N² fit (last 3): c_2(∞) = {coef[1]:+.4e}")
    if len(vals) >= 3:
        s1 = shanks(vals.tolist())
        if s1: print(f"  Shanks-1: {[f'{v:+.4e}' for v in s1]}")
        s2 = shanks(s1) if len(s1) >= 3 else []
        if s2: print(f"  Shanks-2: {[f'{v:+.4e}' for v in s2]}")


def run_N_scan(N_list, m_reg=0.2, m_f=0.05, lambdas=(1, 2, 3), verbose=False):
    print(f"\n{'='*72}")
    print(f"=== C-accelerated: m_reg={m_reg}, m_f={m_f} ===")
    print(f"{'='*72}\n")
    print(f"{'N':>3}  {'Π_s(0)':>8}  {'p²→0 intercept':>17}  {'slope':>13}  {'time':>8}")
    print("-" * 65)
    intercepts = {}
    for N in N_list:
        t_N = time.time()
        result = p_extrapolate_at_N(N, m_reg, m_f, lambdas, verbose=verbose)
        dt = time.time() - t_N
        intercepts[N] = result['intercept']
        print(f"{N:>3}  {result['pi_s']:>8.4f}  {result['intercept']:>+17.5e}  "
              f"{result['slope']:>+13.4e}  {dt:>7.1f}s",
              flush=True)
    return intercepts


if __name__ == "__main__":
    print("\n*** C-accelerated p-extrapolation ***\n")

    # Quick test at N=6 first
    intercepts = run_N_scan(N_list=[6], m_reg=0.2, m_f=0.05, lambdas=(1, 2, 3), verbose=True)
    print(f"\nN=6 intercept: {intercepts[6]:+.5e}")
