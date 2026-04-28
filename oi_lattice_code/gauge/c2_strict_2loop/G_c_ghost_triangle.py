"""
G_c_ghost_triangle.py — 1PI 2-loop standard-QCD G_c
"ghost-triangle" topology.

Structure:
  V_3g (1 ext at one end, 2 internal gluon legs)
    │ L_A (gluon)            │ L_B (gluon)
    ▼                         ▼
  V_ghg_A ────g_AB──────► V_ghg_B
    ▲                         │
    │                         ▼
    └────g_CA─── V_ghg_C ──g_BC─┐
                  │              │
                  ▼ (other ext)

Closed ghost triangle V_ghg_A → V_ghg_B → V_ghg_C → V_ghg_A.

Momentum routing (loop vars k_1 = L_A momentum, k_2 = g_CA momentum):
  L_A (V_3g → V_ghg_A): k_1   (gluon)
  L_B (V_3g → V_ghg_B): p - k_1   (gluon)
  g_AB (V_ghg_A → V_ghg_B): k_1 + k_2   (ghost)
  g_BC (V_ghg_B → V_ghg_C): p + k_2   (ghost)
  g_CA (V_ghg_C → V_ghg_A): k_2   (ghost)

External: p enters at V_3g (Lorentz μ), exits at V_ghg_C (Lorentz ν, via its
gluon leg as the OTHER external gluon).

Vertex factors:
  V_3g (V_3g_ym kinematic):  (p, -k_1, k_1 - p) → indices (μ, α, β)
  V_ghg_A:  q_out = g_AB momentum = k_1 + k_2 → factor (k_1+k_2)̂^α
  V_ghg_B:  q_out = g_BC momentum = p + k_2   → factor (p+k_2)̂^β
  V_ghg_C:  q_out = g_CA momentum = k_2       → factor k_2̂^ν

Lorentz numerator:
  N^{μν}(p; k_1, k_2) = V_3g[μ, α, β] · (k_1+k_2)̂^α · (p+k_2)̂^β · k_2̂^ν

Propagators (5 total):
  D_gluon(k_1) · D_gluon(p-k_1) · D_gh(k_1+k_2) · D_gh(p+k_2) · D_gh(k_2)

Color: 0.5 · C_A^2 (verified numerically)
Symmetry: 1/2 (V_ghg_A ↔ V_ghg_B reflection / ghost-loop orientation reversal)
Ghost-loop sign: -1

Cost: O(N^8) brute force, sliced (k_2 outer, k_1 vectorized).
"""
import numpy as np
import os, sys, time

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from T1a_kite import build_V3g_kinematic, lattice_grid


G_C_COLOR_OVER_CA2 = 0.5


def lattice_prop_ghost(k_arr, eps=1e-12):
    khat = 2 * np.sin(k_arr / 2)
    khat2 = (khat ** 2).sum(axis=-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(khat2 > eps, 1.0 / khat2, 0.0)


def lattice_prop_gluon(k_arr, m_reg):
    khat = 2 * np.sin(k_arr / 2)
    return 1.0 / ((khat ** 2).sum(axis=-1) + m_reg ** 2)


def ghost_triangle_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_G_c(p_ext) per C_A^2.

    Cost: O(N^8) brute force; outer loop k_2, inner vectorize k_1.
    """
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_arr = np.asarray(p_ext, dtype=float)

    # ---- Pre-compute V_3g (k_2-independent, depends on k_1 only) ----
    p1_V3g = np.tile(p_arr, (Npts, 1))
    p2_V3g = -k_grid                              # -k_1
    p3_V3g = k_grid - p_arr[np.newaxis, :]        # k_1 - p
    V_3g_kin = build_V3g_kinematic(p1_V3g, p2_V3g, p3_V3g)   # (Npts, 4, 4, 4) [μ, α, β]

    # k_1-only weights (gluon props on L_A, L_B)
    D_LA = lattice_prop_gluon(k_grid, m_reg)
    D_LB = lattice_prop_gluon(p_arr[np.newaxis, :] - k_grid, m_reg)
    weight_k1_glue = D_LA * D_LB                 # (Npts,)

    Sigma_accum = np.zeros((4, 4))   # [μ, ν]

    if verbose:
        print(f"  G_c: looping k_2 over {Npts} points (N={N})")

    for k2_idx in range(Npts):
        k2 = k_grid[k2_idx]

        # k_2-only quantities (constant in inner k_1 loop)
        khat_k2 = 2 * np.sin(k2 / 2)              # (4,) — k̂_2 for V_ghg_C
        p_plus_k2 = p_arr + k2
        khat_pk2 = 2 * np.sin(p_plus_k2 / 2)      # (4,) — (p+k_2)̂ for V_ghg_B
        D_gh_pk2 = lattice_prop_ghost(p_plus_k2[np.newaxis, :])[0]   # scalar
        D_gh_k2 = lattice_prop_ghost(k2[np.newaxis, :])[0]            # scalar

        # k_1-dependent (with k_2 fixed):
        k_1_plus_k_2 = k_grid + k2[np.newaxis, :]                     # (Npts, 4)
        khat_k1pk2 = 2 * np.sin(k_1_plus_k_2 / 2)                     # (Npts, 4)
        D_gh_k1pk2 = lattice_prop_ghost(k_1_plus_k_2)                 # (Npts,)

        # Total weight per k_1
        weight_k1 = weight_k1_glue * D_gh_k1pk2 * D_gh_pk2 * D_gh_k2  # (Npts,)

        # Lorentz numerator:
        # N^{μν}(k_1, k_2) = V_3g[k_1, μ, α, β] · (k_1+k_2)̂^α · (p+k_2)̂^β · k_2̂^ν
        #
        # Step 1: contract α with (k_1+k_2)̂^α  →  V_3g_pa[k_1, μ, β] = sum_α V_3g[μ,α,β] (k_1+k_2)̂^α
        V3g_pa = np.einsum('kmab,ka->kmb', V_3g_kin, khat_k1pk2)      # (Npts, 4, 4) [μ, β]

        # Step 2: contract β with (p+k_2)̂^β  →  V3g_pap[k_1, μ] = sum_β V3g_pa[μ,β] · (p+k_2)̂^β
        V3g_pap = np.einsum('kmb,b->km', V3g_pa, khat_pk2)            # (Npts, 4) [μ]

        # Step 3: numerator[k_1, μ, ν] = V3g_pap[μ] · k_2̂^ν
        numer = np.einsum('km,n->kmn', V3g_pap, khat_k2)              # (Npts, 4, 4)

        # Sum over k_1 with weight
        Sigma_accum += np.einsum('k,kmn->mn', weight_k1, numer)

    Sigma = Sigma_accum * (1.0 / N**4)**2 * 0.5 * (-1.0)
    return Sigma


def compute_PiT_G_c(N, m_reg, verbose=False):
    """Extract Π_T from G_c at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing G_c at N={N}, m_reg={m_reg}")
    Sigma = ghost_triangle_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_color_coefficient():
    from colors import f_abc
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0
    G_c_color = np.einsum('aij,ikl,jlm,bmk->ab', F, F, F, F)
    diag_avg = np.mean(np.diag(G_c_color))
    off_max = np.max(np.abs(G_c_color - diag_avg * np.eye(8)))
    expected = G_C_COLOR_OVER_CA2 * C_A**2
    print(f"=== G_c ghost-triangle color verification (SU(3)) ===")
    print(f"  Color factor: {diag_avg:.6f} = {diag_avg/C_A**2:.4f} · C_A^2  "
          f"(expected {expected/C_A**2:.4f} · C_A^2 = {expected:.4f})")
    print(f"  δ^ab off-diag max: {off_max:.2e}")
    pass1 = abs(diag_avg / C_A**2 - G_C_COLOR_OVER_CA2) < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 78)
    print("=== G_c ghost-triangle Π_T (per C_A^2) — O(N^8) brute force ===")
    print("=== Sign includes -1 from closed ghost loop ===")
    print("=" * 78)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'Σ^00':>13} {'Σ^11':>13} {'time':>8}")
    for N in [4, 6]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_G_c(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** G_c ghost-triangle, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficient()
    run_small_N_scan()
