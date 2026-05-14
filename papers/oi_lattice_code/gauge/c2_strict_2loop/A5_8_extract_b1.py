"""
A5_8_extract_b1.py — sum all 9 topologies, scan m_reg, extract
log-divergence coefficient, compare to b_1 = (34/3) C_A^2 = 11.333.

Strategy:
  At fixed N (largest feasible), compute Π_T_total(m_reg) = sum of all topologies.
  Fit Π_T_total(m_reg) = a + b · log(1/m_reg) + c · m_reg^2 + ...
  The coefficient `b` should match b_1.

  At finite N, finite-volume effects modify this — but for N large enough,
  log slope should approach textbook value.
"""
import numpy as np
import time
import sys, os

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from T1a_kite import compute_PiT_kite
from T1b_vertex_correction import compute_PiT_vertex_correction
from T1c_V4g_bubble import compute_PiT_V4g_bubble
from T1d_V4g_tadpole import compute_PiT_V4g_tadpole
# T1e: Π_T = 0 structurally
# G_d: Π_T = 0 structurally

from G_b_ghost_vertex_correction import compute_PiT_ghost_vertex_correction
from G_a_ghost_square import compute_PiT_G_a
from G_c_ghost_triangle import compute_PiT_G_c


def total_PiT(N, m_reg, verbose=False):
    """Sum Π_T over all 9 topologies (5 gluon + 4 ghost). Per C_A^2."""
    contribs = {}
    if verbose:
        print(f"  Computing all 9 topologies at N={N}, m_reg={m_reg:.3f}...")

    t0 = time.time()
    pi_T_T1a, _ = compute_PiT_kite(N, m_reg)
    contribs['T1a'] = pi_T_T1a
    if verbose: print(f"    T1a: {pi_T_T1a:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    pi_T_T1b, _ = compute_PiT_vertex_correction(N, m_reg)
    contribs['T1b'] = pi_T_T1b
    if verbose: print(f"    T1b: {pi_T_T1b:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    pi_T_T1c, _ = compute_PiT_V4g_bubble(N, m_reg)
    contribs['T1c'] = pi_T_T1c
    if verbose: print(f"    T1c: {pi_T_T1c:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    pi_T_T1d, _ = compute_PiT_V4g_tadpole(N, m_reg)
    contribs['T1d'] = pi_T_T1d
    if verbose: print(f"    T1d: {pi_T_T1d:+.4e}  [{time.time()-t0:.1f}s]")

    contribs['T1e'] = 0.0   # structural

    t0 = time.time()
    pi_T_Gb, _ = compute_PiT_ghost_vertex_correction(N, m_reg)
    contribs['G_b'] = pi_T_Gb
    if verbose: print(f"    G_b: {pi_T_Gb:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    pi_T_Ga, _ = compute_PiT_G_a(N, m_reg)
    contribs['G_a'] = pi_T_Ga
    if verbose: print(f"    G_a: {pi_T_Ga:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    pi_T_Gc, _ = compute_PiT_G_c(N, m_reg)
    contribs['G_c'] = pi_T_Gc
    if verbose: print(f"    G_c: {pi_T_Gc:+.4e}  [{time.time()-t0:.1f}s]")

    contribs['G_d'] = 0.0   # structural

    total = sum(contribs.values())
    return total, contribs


def m_scan(N=6, m_list=None):
    if m_list is None:
        m_list = [0.4, 0.3, 0.25, 0.2, 0.15, 0.12, 0.1]

    print(f"\n{'='*72}")
    print(f"=== A5.8: All-topology Π_T vs m_reg at N={N} ===")
    print(f"{'='*72}\n")

    print(f"{'m_reg':>8}  {'log(1/m)':>10}  {'T1a+T1b+T1c+T1d':>17}  {'G_a+G_b+G_c':>14}  {'TOTAL':>13}")

    results = []
    for m in m_list:
        total, contribs = total_PiT(N, m, verbose=False)
        gluon_sub = contribs['T1a'] + contribs['T1b'] + contribs['T1c'] + contribs['T1d']
        ghost_sub = contribs['G_a'] + contribs['G_b'] + contribs['G_c']
        log_m = np.log(1.0/m)
        results.append((m, total, gluon_sub, ghost_sub, log_m))
        print(f"  {m:.3f}  {log_m:>10.4f}  {gluon_sub:>+17.4e}  {ghost_sub:>+14.4e}  {total:>+13.4e}")

    # Linear fit: total ≈ a + b * log(1/m_reg)  for small m
    arr = np.array(results)
    m_vals = arr[:, 0]
    total_vals = arr[:, 1]
    log_vals = arr[:, 4]

    # Use only smaller m for cleaner asymptotic regime
    mask = m_vals <= 0.2
    if mask.sum() >= 2:
        slope, intercept = np.polyfit(log_vals[mask], total_vals[mask], 1)
        print(f"\n--- Linear fit Π_T = a + b · log(1/m_reg) for m ≤ 0.2 ---")
        print(f"  Slope (b)     = {slope:+.4f}  (per C_A²)")
        print(f"  Intercept (a) = {intercept:+.4f}")
        print(f"\n  Expected b_1 = (34/3) C_A² = 11.3333  (textbook standard QCD)")
        print(f"  Ratio slope / b_1 = {slope/11.3333:+.4f}")
        print(f"  Sign of slope: {'POSITIVE' if slope > 0 else 'NEGATIVE'}")

    return results


if __name__ == "__main__":
    print("\n*** Extract b_1 from sum of all 9 topologies ***\n")
    print("This is a small-N quick estimate. For convergent b_1 extraction,")
    print("would need N → ∞ extrapolation also.\n")

    # Single N at first; if time permits, we can do N → ∞
    results = m_scan(N=4)
