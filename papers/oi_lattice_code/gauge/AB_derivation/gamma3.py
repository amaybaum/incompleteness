"""
gamma3.py — Assemble Γ_3^{μνρ,abc}(p_1, p_2, p_3) from the three topologies.

Derived structure (for vector-like naive-Γ fermion loop, per Furry + parity):

  d^{abc} coefficient:
    (N_f/4) · [-(J_tri_123 + J_tri_132) + (J_dtad_1 + J_dtad_2 + J_dtad_3) - J_ttad]
    (All three integrals individually vanish → d^{abc} coefficient = 0.)

  f^{abc} coefficient:
    -(i · N_f / 4) · (J_tri_123 - J_tri_132)
    (Triangle's antisymmetric part. Nonzero — drives the c_1 coefficient.)

Full vertex at specific color:
    Γ_3^{μνρ,abc}(p_1,p_2,p_3) = d^{abc}·[d-coeff] + f^{abc}·[f-coeff]
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from vertices import lattice_momenta
from topologies import J_triangle, J_double_tad, J_triple_tad, J_double_tad_antisym


def compute_J_all(k, p1, p2, p3, mu1, mu2, mu3, m):
    """
    Compute all Dirac loop integrals for a given external momentum and
    Lorentz index configuration. Returns a dict.
    """
    return {
        'tri_123': J_triangle(k, p1, p2, p3, mu1, mu2, mu3, m),
        'tri_132': J_triangle(k, p1, p3, p2, mu1, mu3, mu2, m),
        'dtad_1' : J_double_tad(k, p1, p2, p3, mu1, mu2, mu3, m),
        'dtad_2' : J_double_tad(k, p2, p1, p3, mu2, mu1, mu3, m),
        'dtad_3' : J_double_tad(k, p3, p1, p2, mu3, mu1, mu2, m),
        # Antisymmetric-color piece of DD2: contributes to f^{abc} channel
        'dtad_antisym_1': J_double_tad_antisym(k, p1, p2, p3, mu1, mu2, mu3, m),
        'dtad_antisym_2': J_double_tad_antisym(k, p2, p1, p3, mu2, mu1, mu3, m),
        'dtad_antisym_3': J_double_tad_antisym(k, p3, p1, p2, mu3, mu1, mu2, m),
        'ttad'   : J_triple_tad(k, p1, p2, p3, mu1, mu2, mu3, m),
    }


def gamma3_coefficients(k, p1, p2, p3, mu1, mu2, mu3, m, N_f=1):
    """
    Compute (d_coeff, f_coeff) such that:
      Γ_3^{μνρ,abc}(p_1,p_2,p_3) = d^{abc}·d_coeff + f^{abc}·f_coeff

    f_coeff has TWO contributions:
      (a) Triangle: captures the "Furry-antisymmetric" part of Tr[T^a T^b T^c]
          → -(i·N_f/4)·(J_tri_123 − J_tri_132)
      (b) Antisym-double-tad: from antisymmetric color [T,T]/2 in DD2
          → +(i·N_f/4)·(J_dtad_antisym_1 + J_dtad_antisym_2 + J_dtad_antisym_3)

    The triple-tadpole has only fully-symmetric color → no f-channel contribution.

    Returns: (d_coeff, f_coeff, J_dict).
    """
    J = compute_J_all(k, p1, p2, p3, mu1, mu2, mu3, m)

    # d^{abc} coefficient (expected ≈ 0 by Furry + parity in the vector-like limit):
    d_coeff = (N_f / 4.0) * (
        -(J['tri_123'] + J['tri_132'])
        + (J['dtad_1'] + J['dtad_2'] + J['dtad_3'])
        - J['ttad']
    )
    # f^{abc} coefficient (physical):
    #   - Triangle: from Tr[T^a T^b T^c] antisym part. Sign comes from color trace
    #     (i f^{abc}) and topology prefactor (-N_f/3), giving overall (-i·N_f/4).
    #   - Antisym-dtad: Tr[T^a · [T^b,T^c]/2] = (i/4) f^{abc}. Topology prefactor
    #     +N_f (from +N_f · Tr[G·DD1·G·DD2] in S_eff), and the factor 4 in sym-dtad
    #     that accompanies d^{abc}/4 is NOT here (since antisym color trace gives
    #     (i/4)f directly). So contribution = +N_f · (i/4) · J_dtad_antisym_i,
    #     summed over 3 leg choices.
    #
    # Wait: need to match normalizations. For sym-dtad, contribution to d_coeff is
    # (N_f/4)·J_dtad_i. This means the topology contributes "raw integral J_dtad"
    # carrying coefficient (N_f/4) × (color factor d^{abc}/4)^{-1} × d^{abc}. Hmm,
    # think of the "/4" as coming from the COLOR TRACE of the sym-dtad topology,
    # Tr[T^a{T^b,T^c}/2] = d^{abc}/4. So the topology's contribution to S_eff has
    # Dirac × color_trace = J_dtad × (d^{abc}/4).  The overall (N_f) multiplies this.
    # d_coeff contribution = N_f · J_dtad · (1/4) = (N_f/4) · J_dtad.   ✓
    #
    # Similarly for antisym-dtad: color_trace = (i/4) f^{abc}. So:
    # f_coeff contribution = N_f · J_dtad_antisym_i · (i/4) = (i·N_f/4) · J_dtad_antisym_i
    f_coeff = -(1j * N_f / 4.0) * (J['tri_123'] - J['tri_132']) \
              + (1j * N_f / 4.0) * (J['dtad_antisym_1'] + J['dtad_antisym_2'] + J['dtad_antisym_3'])

    return d_coeff, f_coeff, J


def gamma3_at_color(k, p1, p2, p3, mu1, mu2, mu3, a, b, c, m, N_f=1):
    """Evaluate Γ_3^{μνρ}(p_1,p_2,p_3) at specific color indices. Complex scalar."""
    from colors import d_abc, f_abc
    d_c, f_c, _ = gamma3_coefficients(k, p1, p2, p3, mu1, mu2, mu3, m, N_f)
    return d_abc(a, b, c) * d_c + f_abc(a, b, c) * f_c


# ============================================================
# Sanity tests
# ============================================================
if __name__ == "__main__":
    from colors import d_abc, f_abc

    N, m, N_f = 16, 0.05, 1
    k = lattice_momenta(N)
    print(f"=== Γ_3 assembler sanity test at N={N}, m={m}, N_f={N_f} ===\n")

    # Asymmetric test momenta
    p1 = np.array([2*np.pi/N,  0,           0, 0])
    p2 = np.array([0,           2*np.pi/N,  0, 0])
    p3 = -(p1 + p2)
    print(f"p_1 = {p1}")
    print(f"p_2 = {p2}")
    print(f"p_3 = {p3}\n")

    # -----------------------------------------------------------
    # TEST 1: Furry + parity decomposition at μ=(0,0,0)
    # -----------------------------------------------------------
    print("--- Test 1: Furry + parity decomposition, μ=(0,0,0) ---")
    d_c, f_c, J = gamma3_coefficients(k, p1, p2, p3, 0, 0, 0, m, N_f)
    print(f"  J_tri_123 = {J['tri_123']:+.6e}")
    print(f"  J_tri_132 = {J['tri_132']:+.6e}")
    print(f"  sum       = {J['tri_123'] + J['tri_132']:+.3e}  (Furry → 0)")
    print(f"  diff      = {J['tri_123'] - J['tri_132']:+.6e}  (physical)")
    print(f"  J_dtad_1  = {J['dtad_1']:+.3e}  (parity → 0)")
    print(f"  J_dtad_2  = {J['dtad_2']:+.3e}")
    print(f"  J_dtad_3  = {J['dtad_3']:+.3e}")
    print(f"  J_ttad    = {J['ttad']:+.3e}  (parity → 0)")
    print(f"\n  d_coeff   = {d_c:+.3e}  (expect ≈ 0)")
    print(f"  f_coeff   = {f_c:+.6e}  (physical, imaginary)")
    print()

    # -----------------------------------------------------------
    # TEST 2: Γ_3 at (a,b,c)=(1,1,8) [pure d-channel: d_118=1/√3, f_118=0]
    # -----------------------------------------------------------
    print("--- Test 2: Γ_3 at (a,b,c)=(1,1,8) — pure d-channel, expect ≈ 0 ---")
    g118_000 = gamma3_at_color(k, p1, p2, p3, 0, 0, 0, 1, 1, 8, m, N_f)
    g118_012 = gamma3_at_color(k, p1, p2, p3, 0, 1, 2, 1, 1, 8, m, N_f)
    g118_001 = gamma3_at_color(k, p1, p2, p3, 0, 0, 1, 1, 1, 8, m, N_f)
    print(f"  Γ_3^(0,0,0) at (1,1,8) = {g118_000:+.3e}  (d-only, expect 0)")
    print(f"  Γ_3^(0,1,2) at (1,1,8) = {g118_012:+.3e}  (d-only, expect 0)")
    print(f"  Γ_3^(0,0,1) at (1,1,8) = {g118_001:+.3e}  (d-only, expect 0)")
    print()

    # -----------------------------------------------------------
    # TEST 3: Γ_3 at (a,b,c)=(1,2,3) [pure f-channel: d_123=0, f_123=1]
    # -----------------------------------------------------------
    print("--- Test 3: Γ_3 at (a,b,c)=(1,2,3) — pure f-channel, expect ≠ 0 ---")
    g123_000 = gamma3_at_color(k, p1, p2, p3, 0, 0, 0, 1, 2, 3, m, N_f)
    g123_012 = gamma3_at_color(k, p1, p2, p3, 0, 1, 2, 1, 2, 3, m, N_f)
    g123_001 = gamma3_at_color(k, p1, p2, p3, 0, 0, 1, 1, 2, 3, m, N_f)
    print(f"  Γ_3^(0,0,0) at (1,2,3) = {g123_000:+.6e}  (all-same μ)")
    print(f"  Γ_3^(0,1,2) at (1,2,3) = {g123_012:+.6e}  (all-distinct μ)")
    print(f"  Γ_3^(0,0,1) at (1,2,3) = {g123_001:+.6e}  (μ_1=μ_2)")
    print()

    # -----------------------------------------------------------
    # TEST 4: Bose symmetry at (1,2,3) — swap (p1,μ1,a) ↔ (p2,μ2,b)
    # Under this swap, f_{abc} → f_{bac} = -f_{abc}, so Γ_3 should flip sign
    # if the kinematic part (J_tri_123 - J_tri_132) is totally ANTIsymmetric.
    # Concretely: g_swap / g_orig should = -1.
    # -----------------------------------------------------------
    print("--- Test 4: Bose symmetry under (p_1,μ_1,a) ↔ (p_2,μ_2,b) ---")
    # Original: (p_1, μ=0, a=1), (p_2, μ=1, b=2), (p_3, μ=2, c=3)
    g_orig = gamma3_at_color(k, p1, p2, p3, 0, 1, 2, 1, 2, 3, m, N_f)
    # Swap legs 1 ↔ 2: (p_2, μ=1, a=2), (p_1, μ=0, b=1), (p_3, μ=2, c=3)
    #   so now p1→p2, p2→p1, μ1→1, μ2→0, (a,b,c)=(2,1,3)
    g_swap = gamma3_at_color(k, p2, p1, p3, 1, 0, 2, 2, 1, 3, m, N_f)
    print(f"  Γ_3 original (leg order 1,2,3)  = {g_orig:+.6e}")
    print(f"  Γ_3 swapped  (leg order 2,1,3)  = {g_swap:+.6e}")
    print(f"  ratio swap/orig = {g_swap/g_orig if abs(g_orig)>1e-14 else 'N/A'}")
    print(f"  (Bose: Γ_3 symmetric under full (p,μ,a) permutation → ratio = +1)")
    print()

    # -----------------------------------------------------------
    # TEST 5: Low-p scaling — Γ_3 ~ O(p^3) in IR
    # Scale all momenta by λ < 1 and check (for a few λ values)
    # -----------------------------------------------------------
    print("--- Test 5: Low-p scaling check (expect Γ_3 ~ p^3) ---")
    q1 = np.array([2*np.pi/N, 0, 0, 0])
    q2 = np.array([0, 2*np.pi/N, 0, 0])
    q3 = -(q1 + q2)
    for scale in [1, 2, 3, 4]:
        sp1 = scale * q1
        sp2 = scale * q2
        sp3 = -(sp1 + sp2)
        # sp must be lattice momenta: multiples of 2π/N. Scale by integer ensures this.
        g = gamma3_at_color(k, sp1, sp2, sp3, 0, 1, 2, 1, 2, 3, m, N_f)
        # |Γ_3| / |p|^3 should be ~ constant for small p
        p_norm = np.sqrt(np.sum(sp1**2))   # roughly |p_1|
        print(f"  scale={scale}, |p_1|={p_norm:.4f}, Γ_3 = {g:+.6e},  Γ_3/|p|^3 = {g/p_norm**3:+.4e}")
