"""
T1c_V4g_bubble.py — 1PI 2-loop standard-QCD V_4g-bubble
topology

Implements the T1c "V_4g-bubble" topology of the standard-QCD pure-YM
KEY STRUCTURAL INSIGHT — T1c FACTORIZES at O(N^4) (not O(N^8)):

  With continuum V_4g (momentum-independent), and the topology structure

      p ──→ V_1 ⇉ L1, L2 ⇉ V_4g ⇉ L3, L4 ⇉ V_2 ──→ p

  the integrand fully separates. No propagator carries both k_1 and k_2:
    D(L1) = D(k_1)        — k_2-independent
    D(L2) = D(p - k_1)    — k_2-independent
    D(L3) = D(k_2)        — k_1-independent
    D(L4) = D(-p - k_2)   — k_1-independent
  V_1 depends only on (p, k_1); V_2 depends only on (p, k_2);
  V_4g (continuum) has no momentum dependence.

  Σ^{μν}_T1c = (S/4) · sum_chans c_chan · sum_{k1, k2} prop · K_chan(k1, k2)
            = (S/4) · sum_chans c_chan · A_chan ⊗ B_chan
  where A_chan, B_chan are 1-loop integrals over k_1, k_2 separately.

  Cost: O(N^4) per side × 2 sides = trivially fast even at N=20+.

V_4g convention: continuum (per `tadpole_self_energy.py` precedent in the
existing codebase). Wilson V_4g cos-factor refinement is logged as a
Color factors (computed numerically using SU(3) f-symbols; verified
machine-precision δ^{ab} structure):
  Channel 1 (1,2)(3,4): coefficient 1.0 × C_A^2
  Channel 2 (1,3)(2,4): coefficient 0.5 × C_A^2
  Channel 3 (1,4)(3,2): coefficient 0.5 × C_A^2

Lorentz channel structures (Peskin Eq. 16.6 form):
  Ch1: (δ^{αγ}δ^{βδ} - δ^{αδ}δ^{βγ})
  Ch2: (δ^{αβ}δ^{γδ} - δ^{αδ}δ^{βγ})
  Ch3: (δ^{αγ}δ^{βδ} - δ^{αβ}δ^{γδ})

For our index assignment (V_4g indices α, β, γ, δ for legs L1, L2, L3, L4):
  K^{μν}_total = c_1 (Straight - Crossed)
              + c_2 (TraceA·TraceB - Crossed)
              + c_3 (Straight - TraceA·TraceB)
              = (c_1+c_3) Straight + (c_2-c_3) TraceA·TraceB - (c_1+c_2) Crossed
              = 1.5 C_A^2 · Straight + 0 · TraceA·TraceB - 1.5 C_A^2 · Crossed
              = (3/2) C_A^2 · (Straight - Crossed)

The TraceA·TraceB pieces cancel exactly between Ch2 and Ch3 — clean
simplification.

Symmetry factor: 1/4 (two doubled-line internal symmetries
L1↔L2 and L3↔L4, each contributing 1/2).

Topology :
  V_1 (V_3g): external p, internal L1, L2  → 3-valent
  V_2 (V_3g): external -p, internal L3, L4 → 3-valent
  V_3 (V_4g): internal L1, L2, L3, L4      → 4-valent
"""
import numpy as np
import os, sys, time

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from yang_mills_lattice import V_3g_ym
from T1a_kite import build_V3g_kinematic, lattice_grid, lattice_prop


# Color coefficients (computed numerically; see V4G_COLOR_DERIVATION below)
# Channel coefficients in units of C_A^2:
C1_OVER_CA2 = 1.0   # Channel (1,2)(3,4)
C2_OVER_CA2 = 0.5   # Channel (1,3)(2,4)
C3_OVER_CA2 = 0.5   # Channel (1,4)(3,2)


def V4g_bubble_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_T1c(p_ext) per C_A^2 (V_4g-bubble topology).

    Exploits the factorization: with continuum V_4g (no momentum
    dependence) and no k_1-k_2 coupling propagators, the integrand
    factorizes into separate k_1, k_2 1-loop integrals.

    Returns Σ^{μν} as a 4×4 numpy array (per C_A^2).

    Cost: O(N^4) — substantially faster than T1a, T1b which are O(N^8).
    """
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_arr = np.asarray(p_ext, dtype=float)

    # --- Side A (V_1 side, integrated over k_1) ---
    # V_1: V_3g_ym(p, -k1, k1-p), indices (ν, α, β) — Lorentz of L1, L2
    p1_V1 = np.tile(p_arr, (Npts, 1))
    p2_V1 = -k_grid                     # -k1
    p3_V1 = k_grid - p_arr[np.newaxis, :]  # k1-p
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)        # (Npts, 4, 4, 4) [ν, α, β]

    D_k = lattice_prop(k_grid, m_reg)                       # D(k1)
    D_pmk = lattice_prop(p_arr[np.newaxis, :] - k_grid, m_reg)  # D(p-k1)
    weight_A = D_k * D_pmk * (1.0 / N**4)                  # (1/N^4) · D(k1) · D(p-k1)

    # A^{ναβ} = (1/N^4) · sum_{k1} weight_A(k1) · V_1[k1, ν, α, β]
    A = np.einsum('k,kvab->vab', weight_A, V_1)             # (4, 4, 4) [ν, α, β]

    # --- Side B (V_2 side, integrated over k_2) ---
    # V_2: V_3g_ym(-p, -k2, p+k2), indices (μ, γ, δ) — Lorentz of L3, L4
    p1_V2 = np.tile(-p_arr, (Npts, 1))
    p2_V2 = -k_grid                                          # -k2
    p3_V2 = p_arr[np.newaxis, :] + k_grid                    # p+k2
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)           # (Npts, 4, 4, 4) [μ, γ, δ]

    D_k2 = lattice_prop(k_grid, m_reg)                        # D(k2) (same shape as D_k)
    D_ppk2 = lattice_prop(p_arr[np.newaxis, :] + k_grid, m_reg)  # D(p+k2)
    weight_B = D_k2 * D_ppk2 * (1.0 / N**4)

    # B^{μγδ} = (1/N^4) · sum_{k2} weight_B(k2) · V_2[k2, μ, γ, δ]
    B = np.einsum('k,kmgd->mgd', weight_B, V_2)              # (4, 4, 4) [μ, γ, δ]

    # --- Combine via the 3 V_4g channels ---
    #   Channel 1 ((1,2)(3,4)): δ^{αγ}δ^{βδ} - δ^{αδ}δ^{βγ}
    #     → straight - crossed where:
    #       straight^{νμ} = sum_{α,β} A[ν,α,β] B[μ,α,β]
    #       crossed^{νμ}  = sum_{α,β} A[ν,α,β] B[μ,β,α]
    straight = np.einsum('vab,mab->vm', A, B)        # (4, 4) [ν, μ]
    crossed  = np.einsum('vab,mba->vm', A, B)        # (4, 4) [ν, μ]

    #   Channel 2 ((1,3)(2,4)): δ^{αβ}δ^{γδ} - δ^{αδ}δ^{βγ}
    #     → trA·trB - crossed
    trA = np.einsum('vaa->v', A)                      # (4,) [ν]
    trB = np.einsum('mgg->m', B)                      # (4,) [μ]
    trAtrB = np.einsum('v,m->vm', trA, trB)           # (4, 4)

    # Combined with channel coefficients:
    #   K^{νμ} = c_1 (straight - crossed)
    #          + c_2 (trAtrB - crossed)
    #          + c_3 (straight - trAtrB)
    K_total = (C1_OVER_CA2 + C3_OVER_CA2) * straight \
            + (C2_OVER_CA2 - C3_OVER_CA2) * trAtrB \
            - (C1_OVER_CA2 + C2_OVER_CA2) * crossed
    # With c_1=1, c_2=0.5, c_3=0.5: K = 1.5*(straight - crossed)
    # The trAtrB term vanishes by exact cancellation.

    # K_total is in units of C_A^2 already. Apply symmetry factor 1/4.
    # K_total[ν, μ] is Σ^{νμ}; we want to return Σ^{μν} (matching T1a/T1b
    # convention). Transpose at the end.
    Sigma = (1.0 / 4.0) * K_total.T    # (4, 4) [μ, ν]

    return Sigma


def compute_PiT_V4g_bubble(N, m_reg, verbose=False):
    """Extract Π_T from T1c V_4g-bubble at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing T1c V_4g-bubble Σ^{{μν}}(p) at N={N}, m_reg={m_reg}")
    Sigma = V4g_bubble_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


# ============================================================
# Validation: cross-check color coefficients from f-symbols
# ============================================================

def verify_color_coefficients():
    """Verify the c_1, c_2, c_3 channel coefficients by direct
    f-symbol computation in SU(3)."""
    from colors import f_abc

    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0

    # Channel 1: F[a,c1,c2] F[b,c3,c4] F[c1,c2,e] F[c3,c4,e]
    C1 = np.einsum('aij,bkl,ije,kle->ab', F, F, F, F)
    c1 = np.mean(np.diag(C1))
    off1 = np.max(np.abs(C1 - c1 * np.eye(8)))

    # Channel 2: F[a,c1,c2] F[b,c3,c4] F[c1,c3,e] F[c2,c4,e]
    C2 = np.einsum('aij,bkl,ike,jle->ab', F, F, F, F)
    c2 = np.mean(np.diag(C2))
    off2 = np.max(np.abs(C2 - c2 * np.eye(8)))

    # Channel 3: F[a,c1,c2] F[b,c3,c4] F[c1,c4,e] F[c3,c2,e]
    C3 = np.einsum('aij,bkl,ile,kje->ab', F, F, F, F)
    c3 = np.mean(np.diag(C3))
    off3 = np.max(np.abs(C3 - c3 * np.eye(8)))

    print("=== T1c V_4g channel color coefficient verification (SU(3)) ===")
    print(f"  Channel 1: c_1 = {c1:.6f} = {c1/C_A**2:.4f} · C_A^2  (expected 1.0 · C_A^2)")
    print(f"             δ^ab structure: off-diag max = {off1:.2e}")
    print(f"  Channel 2: c_2 = {c2:.6f} = {c2/C_A**2:.4f} · C_A^2  (expected 0.5 · C_A^2)")
    print(f"             δ^ab structure: off-diag max = {off2:.2e}")
    print(f"  Channel 3: c_3 = {c3:.6f} = {c3/C_A**2:.4f} · C_A^2  (expected 0.5 · C_A^2)")
    print(f"             δ^ab structure: off-diag max = {off3:.2e}")

    pass1 = abs(c1/C_A**2 - C1_OVER_CA2) < 1e-10
    pass2 = abs(c2/C_A**2 - C2_OVER_CA2) < 1e-10
    pass3 = abs(c3/C_A**2 - C3_OVER_CA2) < 1e-10
    if pass1 and pass2 and pass3:
        print("  PASS: all channel coefficients match hard-coded values.\n")
    else:
        print("  FAIL: coefficient mismatch!\n")
    return pass1 and pass2 and pass3


# ============================================================
# Validation: brute-force vs factorized
# ============================================================

def test_factorization_correctness(N=4, m_reg=0.2):
    """Cross-check the factorized implementation against an explicit
    brute-force (k_1, k_2) double-sum reference. They must agree
    bit-identically (up to rounding) since the algebra is exact."""
    print(f"=== T1c factorization vs brute-force (N={N}, m_reg={m_reg}) ===")
    p_ext = (2 * np.pi / N) * np.array([1.0, 0.0, 0.0, 0.0])
    p_arr = p_ext

    # Method 1: factorized (production)
    Sigma_fact = V4g_bubble_sigma(N, p_ext, m_reg)

    # Method 2: brute-force double-sum
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]

    p1_V1 = np.tile(p_arr, (Npts, 1)); p2_V1 = -k_grid; p3_V1 = k_grid - p_arr[np.newaxis, :]
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)
    p1_V2 = np.tile(-p_arr, (Npts, 1)); p2_V2 = -k_grid; p3_V2 = p_arr[np.newaxis, :] + k_grid
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)

    D_k = lattice_prop(k_grid, m_reg)
    D_pmk = lattice_prop(p_arr[np.newaxis, :] - k_grid, m_reg)
    D_ppk = lattice_prop(p_arr[np.newaxis, :] + k_grid, m_reg)

    Sigma_brute = np.zeros((4, 4))
    for k2_idx in range(Npts):
        k2 = k_grid[k2_idx]
        D_k2_val = D_k[k2_idx]
        D_ppk2_val = D_ppk[k2_idx]
        # V_2 at this k2 only
        V2_slice = V_2[k2_idx]   # (4, 4, 4) [μ, γ, δ]
        # Compute the "straight" and "crossed" patterns at this slice
        # straight^{νμ}(k1) = sum V_1[k1, ν, α, β] · V2_slice[μ, α, β]
        s = np.einsum('kvab,mab->kvm', V_1, V2_slice)
        c = np.einsum('kvab,mba->kvm', V_1, V2_slice)
        trA = np.einsum('kvaa->kv', V_1)
        trB = np.einsum('maa->m', V2_slice)
        ttab = np.einsum('kv,m->kvm', trA, trB)
        # K^{νμ} per k1, k2-fixed
        K = (C1_OVER_CA2 + C3_OVER_CA2) * s + (C2_OVER_CA2 - C3_OVER_CA2) * ttab - (C1_OVER_CA2 + C2_OVER_CA2) * c
        # Propagator weight for this slice
        prop = D_k * D_pmk * D_k2_val * D_ppk2_val   # over k1
        Sigma_brute += np.einsum('k,kvm->vm', prop, K)
    Sigma_brute *= (1.0 / 4.0) * (1.0 / N**4)**2
    Sigma_brute = Sigma_brute.T   # transpose to [μ, ν]

    diff = np.max(np.abs(Sigma_fact - Sigma_brute))
    rel = diff / (np.max(np.abs(Sigma_fact)) + 1e-30)
    print(f"  Factorized result: Σ^{{μν}} max element = {np.max(np.abs(Sigma_fact)):.4e}")
    print(f"  Brute-force result: max element       = {np.max(np.abs(Sigma_brute)):.4e}")
    print(f"  Max abs diff: {diff:.2e}")
    print(f"  Max rel diff: {rel:.2e}")
    if rel < 1e-10:
        print("  PASS\n")
    else:
        print("  FAIL\n")
    return rel < 1e-10


def run_small_N_scan():
    print("=" * 76)
    print("=== T1c V_4g-bubble Π_T (per C_A^2) at finite N — factorized O(N^4) ===")
    print("=" * 76)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'S00':>13} {'S11':>13} {'time':>8}")
    for N in [4, 6, 8, 12, 16]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_V4g_bubble(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** T1c V_4g-bubble topology, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficients()
    test_factorization_correctness(N=4)
    run_small_N_scan()
