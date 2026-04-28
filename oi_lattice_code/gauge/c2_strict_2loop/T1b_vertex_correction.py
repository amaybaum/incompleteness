"""
T1b_vertex_correction.py — 1PI 2-loop standard-QCD
"vertex correction" / "tennis racket" topology

Implements the T1b topology for the standard-QCD pure-YM gluon
self-energy at 2 loops (NLO).

Architecture mirrors T1a_kite.py with two key differences:
  1. Different momentum routing (V_3-V_4 doubled inner line)
  2. V_1 and V_2 are k2-INDEPENDENT, so they can be built once outside
     the k2 outer loop — and the V_1·V_2 partial contraction
     (sum over Lorentz α) can also be precomputed. Significant
     efficiency improvement over T1a where only V_L was outside.

Topology :

    V_1 ──── L1 ──── V_2          (outer line)
     │              │
     L2             L3
     │              │
    V_3 ⇉ L4a/L4b ⇉ V_4          (inner sub-bubble: doubled line)

External: p in at V_1 (Lorentz ν), p out at V_2 (Lorentz μ).

5 internal lines:
  L1 (V_1→V_2): momentum k1, Lorentz α
  L2 (V_1→V_3): momentum p - k1, Lorentz β
  L3 (V_2→V_4): momentum k1 - p, Lorentz γ
  L4a (V_3→V_4): momentum k2, Lorentz δ
  L4b (V_3→V_4): momentum p - k1 - k2, Lorentz ε

Vertex calls (all-incoming convention):
  V_1: V_3g_ym(p, -k1, k1-p)              indices (ν, α, β)
  V_2: V_3g_ym(-p, k1, p-k1)               indices (μ, α, γ)
  V_3: V_3g_ym(p-k1, -k2, k1+k2-p)         indices (β, δ, ε)
  V_4: V_3g_ym(k1-p, k2, p-k1-k2)          indices (γ, δ, ε)

Kinematic numerator:
  K^{μν}(p, k1, k2) = Σ_{α,β,γ,δ,ε}
                       V_1^{ναβ} V_2^{μαγ} V_3^{βδε} V_4^{γδε}

Color factor: C_A^2 (same as T1a;)
Symmetry factor: 1/2 (per A5.1.6, reflection through V_1-V_2 line)
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

# Reuse helpers from T1a_kite where possible
from T1a_kite import build_V3g_kinematic, lattice_grid, lattice_prop


def vertex_correction_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_T1b(p_ext) per C_A^2 (vertex correction topology).

    Uses Wilson V_3g_ym at each of 4 vertices, bare 1/k̂² propagators
    with IR regulator m_reg.

    Returns Σ^{μν} as a 4×4 numpy array (dimensionless × C_A^2).

    Computational cost: O(N^8) operations, O(N^4) memory.
    Slightly faster than T1a kite due to k2-independent V_1·V_2 partial
    contraction precomputed outside the outer loop.
    """
    k1_grid = lattice_grid(N)
    Npts = k1_grid.shape[0]
    p_ext_arr = np.asarray(p_ext, dtype=float)

    # ---------- k2-INDEPENDENT pieces (precomputed) ----------
    # V_1: V_3g_ym(p, -k1, k1-p), indices (ν, α, β) — depends on k1 only
    p1_V1 = np.tile(p_ext_arr, (Npts, 1))
    p2_V1 = -k1_grid
    p3_V1 = k1_grid - p_ext_arr[np.newaxis, :]
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)        # (Npts, 4, 4, 4) [ν, α, β]

    # V_2: V_3g_ym(-p, k1, p-k1), indices (μ, α, γ) — depends on k1 only
    p1_V2 = np.tile(-p_ext_arr, (Npts, 1))
    p2_V2 = k1_grid
    p3_V2 = p_ext_arr[np.newaxis, :] - k1_grid
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)        # (Npts, 4, 4, 4) [μ, α, γ]

    # Pre-contract α (between V_1 and V_2):
    #   U[k1, ν, μ, β, γ] = Σ_α V_1[k1, ν, α, β] V_2[k1, μ, α, γ]
    # k2-independent — done once.
    U = np.einsum('kvab,kmag->kvmbg', V_1, V_2, optimize='optimal')   # (Npts, 4, 4, 4, 4)

    # k2-independent propagators
    D_k1 = lattice_prop(k1_grid, m_reg)                                  # D(k1)
    D_pmk1 = lattice_prop(p_ext_arr[np.newaxis, :] - k1_grid, m_reg)     # D(p-k1) for both L2, L3
    # The k2-independent prop weight for outer loop k1:
    prop_k1 = D_k1 * D_pmk1 * D_pmk1   # D(L1) * D(L2) * D(L3); L4a, L4b are k2-dependent

    # ---------- Outer loop over k2 ----------
    Sigma = np.zeros((4, 4), dtype=float)
    inv_vol2 = (1.0 / N**4)**2

    t_start = time.time()
    for k2_idx in range(Npts):
        k2 = k1_grid[k2_idx]

        # V_3: V_3g_ym(p-k1, -k2, k1+k2-p), indices (β, δ, ε)
        p1_V3 = p_ext_arr[np.newaxis, :] - k1_grid
        p2_V3 = np.tile(-k2, (Npts, 1))
        p3_V3 = k1_grid + k2[np.newaxis, :] - p_ext_arr[np.newaxis, :]
        V_3 = build_V3g_kinematic(p1_V3, p2_V3, p3_V3)    # (Npts, 4, 4, 4) [β, δ, ε]

        # V_4: V_3g_ym(k1-p, k2, p-k1-k2), indices (γ, δ, ε)
        p1_V4 = k1_grid - p_ext_arr[np.newaxis, :]
        p2_V4 = np.tile(k2, (Npts, 1))
        p3_V4 = p_ext_arr[np.newaxis, :] - k1_grid - k2[np.newaxis, :]
        V_4 = build_V3g_kinematic(p1_V4, p2_V4, p3_V4)    # (Npts, 4, 4, 4) [γ, δ, ε]

        # Contract over (δ, ε) — the doubled-line indices:
        #   W[k1, β, γ] = Σ_{δ, ε} V_3[k1, β, δ, ε] V_4[k1, γ, δ, ε]
        if k2_idx == 0:
            _path_W = np.einsum_path('kbde,kgde->kbg', V_3, V_4, optimize='optimal')[0]
        W = np.einsum('kbde,kgde->kbg', V_3, V_4, optimize=_path_W)    # (Npts, 4, 4)

        # k2-dependent propagators
        D_k2 = lattice_prop(k2[np.newaxis, :], m_reg)[0]  # scalar
        D_pmk1mk2 = lattice_prop(p_ext_arr[np.newaxis, :] - k1_grid - k2[np.newaxis, :], m_reg)

        # Combined propagator weight for this slice
        prop_total = prop_k1 * D_k2 * D_pmk1mk2          # (Npts,)

        # Final contraction: Σ^{μν} += Σ_{k1, β, γ} prop_total[k1] · U[k1,ν,μ,β,γ] · W[k1,β,γ]
        if k2_idx == 0:
            _path_final = np.einsum_path('k,kvmbg,kbg->mv',
                                         prop_total, U, W,
                                         optimize='optimal')[0]
        Sigma += np.einsum('k,kvmbg,kbg->mv',
                           prop_total, U, W,
                           optimize=_path_final)

        if verbose and (k2_idx % max(1, Npts // 8) == 0 or k2_idx == Npts - 1):
            dt = time.time() - t_start
            frac = (k2_idx + 1) / Npts
            eta = dt * (1 - frac) / frac if frac > 0 else 0
            print(f"    [k2 {k2_idx+1}/{Npts} = {100*frac:.1f}%]  elapsed {dt:.1f}s  ETA {eta:.1f}s", flush=True)

    # Apply symmetry factor 1/2 and double-integration measure
    Sigma *= 0.5 * inv_vol2
    return Sigma


def compute_PiT_vertex_correction(N, m_reg, verbose=False):
    """Extract Π_T from T1b vertex correction at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing T1b vertex-correction Σ^{{μν}}(p) at N={N}, m_reg={m_reg}")
    Sigma = vertex_correction_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


# ============================================================
# Sanity tests and small-N runs
# ============================================================

def test_against_explicit_einsum(N=4, m_reg=0.2):
    """Sanity: vertex_correction_sigma should agree with a pedestrian
    explicit re-implementation that uses different intermediate steps."""
    print(f"=== T1b consistency check at N={N}, m_reg={m_reg} ===")

    # Method 1: production version
    p_ext = (2 * np.pi / N) * np.array([1.0, 0.0, 0.0, 0.0])
    Sigma_prod = vertex_correction_sigma(N, p_ext, m_reg, verbose=False)

    # Method 2: alternative — full 4-vertex einsum (no precontracting)
    k1_grid = lattice_grid(N)
    Npts = k1_grid.shape[0]

    # Build all 4 vertices over (k1, k2) joint grid.
    # k2 outer; same as production but with explicit single-shot contraction per slice.
    p_arr = p_ext

    p1_V1 = np.tile(p_arr, (Npts, 1)); p2_V1 = -k1_grid; p3_V1 = k1_grid - p_arr[np.newaxis, :]
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)
    p1_V2 = np.tile(-p_arr, (Npts, 1)); p2_V2 = k1_grid; p3_V2 = p_arr[np.newaxis, :] - k1_grid
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)

    D_k1 = lattice_prop(k1_grid, m_reg)
    D_pmk1 = lattice_prop(p_arr[np.newaxis, :] - k1_grid, m_reg)

    Sigma_alt = np.zeros((4, 4))
    for k2_idx in range(Npts):
        k2 = k1_grid[k2_idx]
        p1_V3 = p_arr[np.newaxis, :] - k1_grid; p2_V3 = np.tile(-k2, (Npts, 1)); p3_V3 = k1_grid + k2[np.newaxis, :] - p_arr[np.newaxis, :]
        V_3 = build_V3g_kinematic(p1_V3, p2_V3, p3_V3)
        p1_V4 = k1_grid - p_arr[np.newaxis, :]; p2_V4 = np.tile(k2, (Npts, 1)); p3_V4 = p_arr[np.newaxis, :] - k1_grid - k2[np.newaxis, :]
        V_4 = build_V3g_kinematic(p1_V4, p2_V4, p3_V4)
        D_k2 = lattice_prop(k2[np.newaxis, :], m_reg)[0]
        D_pmk1mk2 = lattice_prop(p_arr[np.newaxis, :] - k1_grid - k2[np.newaxis, :], m_reg)
        prop = D_k1 * D_pmk1 * D_pmk1 * D_k2 * D_pmk1mk2
        # SINGLE einsum: K[k1, μ, ν] = sum_{α,β,γ,δ,ε} V_1[k1,ν,α,β] V_2[k1,μ,α,γ] V_3[k1,β,δ,ε] V_4[k1,γ,δ,ε]
        K = np.einsum('kvab,kmag,kbde,kgde->kmv', V_1, V_2, V_3, V_4, optimize='optimal')
        Sigma_alt += np.einsum('k,kmv->mv', prop, K)
    Sigma_alt *= 0.5 * (1.0 / N**4)**2

    diff = np.max(np.abs(Sigma_prod - Sigma_alt))
    rel_diff = diff / (np.max(np.abs(Sigma_prod)) + 1e-30)
    print(f"  max abs diff (prod vs alt): {diff:.2e}")
    print(f"  max rel diff: {rel_diff:.2e}")
    if rel_diff < 1e-10:
        print(f"  PASS\n")
    else:
        print(f"  FAIL\n")
    return rel_diff < 1e-10


def run_small_N_scan():
    print("=" * 76)
    print("=== T1b vertex-correction Π_T (per C_A^2) at finite N ===")
    print("=" * 76)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'S00':>13} {'S11':>13} {'time':>8}")
    for N in [4, 6]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_vertex_correction(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.1f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** T1b vertex-correction topology, standard-QCD pure-YM at 2-loop ***\n")
    test_against_explicit_einsum(N=4)
    run_small_N_scan()
