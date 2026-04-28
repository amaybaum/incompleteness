"""
A5_OI_substratum.py — substratum-side (OI-induced)
calculation of c_2.

Strategy (constant-Π_s approximation):
  Replace each gluon propagator 1/(k̂² + m_reg²) with the OI-induced
  propagator 1/((k̂² + m_reg²) · Π_s(0)), where Π_s(0) is evaluated
  at the same lattice (N, m_f) used in the underlying staggered VP.

  Since Π_s(0) is k-independent (constant, leading-IR value), this
  is equivalent to multiplying each topology's Π_T by 1/Π_s^(n_gluon),
  where n_gluon is the number of internal gluon propagators in that
  topology.

  Ghost propagators kept STANDARD (1/k̂²) per the LO convention in
  ghost_self_energy.py (use_induced=False).

Gluon prop count per topology:
  T1a kite: 5 gluon
  T1b vertex correction: 5 gluon
  T1c V_4g-bubble: 4 gluon
  T1d V_4g-tadpole: 4 gluon (3 main + 1 self-loop)
  T1e V_4g-V_4g triple-line: 3 gluon (Π_T = 0 structurally)
  G_a ghost-square: 1 gluon (chord) + 4 ghost
  G_b ghost vertex correction: 3 gluon + 2 ghost
  G_c ghost-triangle: 2 gluon + 3 ghost
  G_d V_4g + ghost-bubble: 2 gluon + 2 ghost (Π_T = 0 structurally)

Expected substratum result (per OI prediction):
  c_2 = -A·B²/2
  With A=8, B=6: c_2 = -8·36/2 = -144
  Per C_A^2: c_2 / C_A^2 = -144/9 = -16.0
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

# Standard-QCD topology Π_T extractors:
from T1a_kite import compute_PiT_kite
from T1b_vertex_correction import compute_PiT_vertex_correction
from T1c_V4g_bubble import compute_PiT_V4g_bubble
from T1d_V4g_tadpole import compute_PiT_V4g_tadpole
from G_b_ghost_vertex_correction import compute_PiT_ghost_vertex_correction
from G_a_ghost_square import compute_PiT_G_a
from G_c_ghost_triangle import compute_PiT_G_c
# T1e and G_d structurally zero.


# Per the LO convention in p_extrapolation.py / reproduce_AB.py, BOTH gluon AND
# ghost are induced (use_induced=True for both). So the rescaling power is
# n_gluon + n_ghost (= number of internal propagators total).
N_INDUCED_PROPS = {
    'T1a': 5,    # 5 gluon + 0 ghost
    'T1b': 5,    # 5 gluon + 0 ghost
    'T1c': 4,    # 4 gluon + 0 ghost
    'T1d': 4,    # 4 gluon + 0 ghost
    'T1e': 3,    # 3 gluon + 0 ghost (Π_T = 0 anyway)
    'G_a': 5,    # 1 gluon + 4 ghost
    'G_b': 5,    # 3 gluon + 2 ghost
    'G_c': 5,    # 2 gluon + 3 ghost
    'G_d': 4,    # 2 gluon + 2 ghost (Π_T = 0 anyway)
}


def compute_OI_PiT_total(N, m_reg_gluon, m_f_substratum, verbose=False):
    """Compute substratum-side Π_T_total per C_A² at given (N, m_reg, m_f).

    m_reg_gluon: IR regulator on the gluon propagator (for the 2-loop gluon SE)
    m_f_substratum: fermion mass in the staggered VP that defines Π_s

    Returns: dict of per-topology induced Π_T plus 'TOTAL'.
    """
    # Step 1: compute Π_s(0) at substratum scale
    pi_s = compute_pi_s(N, m_f_substratum)
    inv_pi_s = 1.0 / pi_s

    if verbose:
        print(f"  Π_s(N={N}, m_f={m_f_substratum}) = {pi_s:.5f}; 1/Π_s = {inv_pi_s:.4f}")

    # Step 2: compute standard Π_T per topology
    contribs_std = {}
    if verbose:
        print(f"  Computing 7 brute-force topologies at N={N}, m_reg={m_reg_gluon}...")

    t0 = time.time()
    contribs_std['T1a'], _ = compute_PiT_kite(N, m_reg_gluon)
    if verbose: print(f"    T1a: {contribs_std['T1a']:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    contribs_std['T1b'], _ = compute_PiT_vertex_correction(N, m_reg_gluon)
    if verbose: print(f"    T1b: {contribs_std['T1b']:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    contribs_std['T1c'], _ = compute_PiT_V4g_bubble(N, m_reg_gluon)
    if verbose: print(f"    T1c: {contribs_std['T1c']:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    contribs_std['T1d'], _ = compute_PiT_V4g_tadpole(N, m_reg_gluon)
    if verbose: print(f"    T1d: {contribs_std['T1d']:+.4e}  [{time.time()-t0:.1f}s]")

    contribs_std['T1e'] = 0.0    # structural

    t0 = time.time()
    contribs_std['G_a'], _ = compute_PiT_G_a(N, m_reg_gluon)
    if verbose: print(f"    G_a: {contribs_std['G_a']:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    contribs_std['G_b'], _ = compute_PiT_ghost_vertex_correction(N, m_reg_gluon)
    if verbose: print(f"    G_b: {contribs_std['G_b']:+.4e}  [{time.time()-t0:.1f}s]")

    t0 = time.time()
    contribs_std['G_c'], _ = compute_PiT_G_c(N, m_reg_gluon)
    if verbose: print(f"    G_c: {contribs_std['G_c']:+.4e}  [{time.time()-t0:.1f}s]")

    contribs_std['G_d'] = 0.0    # structural

    # Step 3: rescale by 1/Π_s^n_induced per topology (gluon + ghost both induced)
    contribs_OI = {}
    for k, v in contribs_std.items():
        n = N_INDUCED_PROPS[k]
        contribs_OI[k] = v * (inv_pi_s ** n)

    contribs_OI['TOTAL'] = sum(v for k, v in contribs_OI.items() if k != 'TOTAL')
    contribs_OI['_pi_s'] = pi_s
    contribs_OI['_std_total'] = sum(contribs_std.values())

    # LO convention: report Π_T_OI · Π_s² (this is the "extract_PiT_times_pis2" quantity).
    # For NLO, the analog is Π_T_OI · Π_s^k for some k. The simplest analogous
    # quantity is Π_T_OI · Π_s² (matching LO normalization), which extracts the
    # "renormalized" Π_T at the OI scale.
    contribs_OI['TOTAL_times_PiS2'] = contribs_OI['TOTAL'] * pi_s**2

    return contribs_OI


def report_substratum(contribs_OI, label=""):
    """Print formatted report of substratum-side Π_T."""
    print(f"\n{'='*72}")
    print(f"=== Substratum (OI-induced) Π_T per C_A² {label} ===")
    print(f"{'='*72}\n")
    print(f"  Π_s(0) = {contribs_OI['_pi_s']:.5f}")
    print(f"  Standard total (for reference): {contribs_OI['_std_total']:+.4e}\n")

    print(f"{'Topology':<10}{'n_ind':>6}  {'Π_T_induced':>15}  {'1/Π_s^n':>10}")
    print("-" * 50)
    for k in ['T1a', 'T1b', 'T1c', 'T1d', 'T1e', 'G_a', 'G_b', 'G_c', 'G_d']:
        n = N_INDUCED_PROPS[k]
        scale = (1/contribs_OI['_pi_s'])**n
        v = contribs_OI[k]
        print(f"  {k:<8}{n:>6}  {v:>+15.4e}  {scale:>10.3f}")
    print("-" * 50)
    print(f"  {'TOTAL':<14}{contribs_OI['TOTAL']:>+15.4e}")
    print(f"  {'TOTAL · Π_s²':<14}{contribs_OI['TOTAL_times_PiS2']:>+15.4e}  ← LO-convention normalized")
    print()
    print(f"  OI prediction (per LO formula c_2 = -A·B²/2):")
    print(f"    With A·B = 48 (from prior LO derivation): c_2 = -1152")
    print(f"    Per C_A² (C_A=3): c_2/C_A² = -128")
    print(f"    With (A=8, B=6) decomposition: c_2 = -A·B²/2 = -144, per C_A²: -16")
    print(f"  Ratio TOTAL/(-128): {contribs_OI['TOTAL']/(-128.0):+.4f}")
    print(f"  Ratio TOTAL · Π_s²/(-128): {contribs_OI['TOTAL_times_PiS2']/(-128.0):+.4f}")


if __name__ == "__main__":
    print("\n*** Substratum-side (OI-induced) c_2 extraction ***\n")

    # Working point: N=6 (limited by O(N⁸) brute force), m_reg=0.2 (gluon IR),
    # m_f=0.1 (substratum fermion; gives Π_s closer to continuum)
    print("--- N=6, m_reg=0.2, m_f=0.1 ---")
    contribs = compute_OI_PiT_total(N=6, m_reg_gluon=0.2, m_f_substratum=0.1, verbose=True)
    report_substratum(contribs, label="(N=6, m_reg=0.2, m_f=0.1)")

    # Sensitivity check: vary m_f for substratum (Π_s changes)
    print("\n\n--- Substratum-mass sensitivity at N=6, m_reg=0.2 ---\n")
    print(f"{'m_f':>7} {'Π_s(0)':>10} {'TOTAL':>13} {'TOTAL·Π_s²':>13} {'×Π_s²/-128':>13}")
    for m_f in [0.2, 0.15, 0.1, 0.05]:
        contribs = compute_OI_PiT_total(N=6, m_reg_gluon=0.2, m_f_substratum=m_f, verbose=False)
        print(f"{m_f:>7.3f} {contribs['_pi_s']:>10.4f} {contribs['TOTAL']:>+13.4e} "
              f"{contribs['TOTAL_times_PiS2']:>+13.4e} {contribs['TOTAL_times_PiS2']/(-128.0):>+13.4f}")
