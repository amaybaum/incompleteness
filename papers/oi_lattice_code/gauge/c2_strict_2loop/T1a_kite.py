"""
T1a_kite.py — 1PI 2-loop standard-QCD kite topology

Implements the T1a "kite" topology for the standard-QCD pure-YM gluon
self-energy at 2 loops (NLO).

References:
  - qcd_crosscheck.py (LO 1-loop analog, architectural template)
  - bubble_at_finite_p.py (finite-p extraction methodology)
  - yang_mills_lattice.py (V_3g_ym Wilson vertex)

Topology :

    Vertices: V_L, V_T, V_R, V_B (all V_3g_ym).
    External p enters at V_L (Lorentz ν), exits at V_R (Lorentz μ).

    5 internal lines (with momentum direction):
      L1: V_L → V_T, momentum k1, Lorentz α
      L2: V_T → V_R, momentum k1 - k2, Lorentz γ
      L3: V_L → V_B, momentum p - k1, Lorentz β
      L4: V_B → V_R, momentum p - k1 + k2, Lorentz δ
      L5: V_T → V_B, momentum k2, Lorentz ε

    Color factor: C_A^2  (  standard f-symbol reduction).
    Symmetry factor: 1/2 (top-bottom V_T ↔ V_B reflection).

Integral form:

    Σ^{μν}_T1a(p) = (1/2) · C_A^2 · (1/N^4)^2 · Σ_{k1,k2 ∈ BZ}
                    K^{μν}(p, k1, k2) · D(k1)·D(k1-k2)·D(p-k1)·D(p-k1+k2)·D(k2)

with K^{μν} = Σ_{α,β,γ,δ,ε} V_L^{ναβ}(p, -k1, k1-p)
                          · V_T^{αγε}(k1, k2-k1, -k2)
                          · V_R^{μγδ}(-p, k1-k2, p-k1+k2)
                          · V_B^{βδε}(p-k1, k1-k2-p, k2)

and D(q) = 1 / (Σ_μ (2 sin(q_μ/2))^2 + m_reg^2) — bare 1/k̂² with IR regulator.

Implementation strategy:
  - Outer loop over k2 (N^4 slices)
  - Inner: vectorize over k1 grid (N^4 points)
  - Per slice: build 4 V_3g tensors over k1 grid, contract Lorentz indices,
    accumulate Σ^{μν}.
  - Memory: O(N^4) per slice. Time: O(N^8).
  - At N=6, N^8 = 1.68e6 grid points · O(1) ops per Lorentz contraction ~
    seconds. At N=8, N^8 = 1.68e7 ~ minutes.

Π_T extraction (per bubble_at_finite_p.py methodology):
  With external p = (p_0, 0, 0, 0):
    Σ^{μν} = (δ^{μν} p^2 - p^μ p^ν) Π_T + [gauge-violating mass term]
    Σ^{00} = 0·Π_T + mass = Σ(0)
    Σ^{11} = p_0^2 · Π_T + mass = p_0^2 Π_T + Σ(0)
  Hence:
    Π_T = (Σ^{11} - Σ^{00}) / p̂_0^2

The textbook 2-loop pure-YM result (continuum, Feynman-gauge,
MS-bar-like):
    Π_T^{(2L),YM}(p^2) ~ -(b_1 / (16π^2)^2) · log^2(...) per (g^2)^2 · C_A^2
    with b_1 = (34/3) C_A^2 in the standard normalization.

T1a alone is one of ~12-14 1PI topologies; it is NOT expected to recover
b_1 by itself, but should:
  (a) give a finite Π_T at finite N (modulo IR regulator)
  (b) have the correct sign (same as overall b_1 contribution)
  (c) be of order C_A^2 / (16π^2)^2 in absolute magnitude
  (d) approach a finite continuum limit as N → ∞ at fixed m_reg

This module's success criterion is (a)-(d). The "fraction of b_1"
comparison only becomes meaningful after T1b-T1e and ghost analogs are
also implemented.
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


def build_V3g_kinematic(p1_grid, p2_grid, p3_grid):
    """Build V_3g_ym tensor as (Npts, 4, 4, 4) given three momentum-grids.

    Each pi_grid has shape (Npts, 4) — i.e., for each grid point we have
    a 4-vector momentum.
    Returns V[npt, mu1, mu2, mu3] = K_{3g}^{μ_1 μ_2 μ_3}(p_1, p_2, p_3)
    using the Wilson-action form (yang_mills_lattice.V_3g_ym).
    """
    Npts = p1_grid.shape[0]
    p1h = 2 * np.sin(p1_grid / 2)  # (Npts, 4)
    p2h = 2 * np.sin(p2_grid / 2)
    p3h = 2 * np.sin(p3_grid / 2)
    cos1h = np.cos(p1_grid / 2)
    cos2h = np.cos(p2_grid / 2)
    cos3h = np.cos(p3_grid / 2)

    V = np.zeros((Npts, 4, 4, 4), dtype=float)
    for mu1 in range(4):
        for mu2 in range(4):
            for mu3 in range(4):
                val = np.zeros(Npts)
                # δ^{μ1 μ2} cos(p3_{μ1}/2) (p1h - p2h)^{μ3}
                if mu1 == mu2:
                    val += cos3h[:, mu1] * (p1h[:, mu3] - p2h[:, mu3])
                # δ^{μ2 μ3} cos(p1_{μ2}/2) (p2h - p3h)^{μ1}
                if mu2 == mu3:
                    val += cos1h[:, mu2] * (p2h[:, mu1] - p3h[:, mu1])
                # δ^{μ3 μ1} cos(p2_{μ3}/2) (p3h - p1h)^{μ2}
                if mu3 == mu1:
                    val += cos2h[:, mu3] * (p3h[:, mu2] - p1h[:, mu2])
                V[:, mu1, mu2, mu3] = val
    return V


def lattice_grid(N):
    """Return BZ-shifted lattice momentum grid as (N^4, 4) array."""
    dk = 2 * np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N // 2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0 * dk, I1 * dk, I2 * dk, I3 * dk], axis=-1)
    return k_grid.reshape(-1, 4)


def lattice_prop(q_grid, m_reg):
    """Lattice propagator 1/(k̂² + m_reg²) on a momentum grid (Npts, 4)."""
    qhat2_sum = (2 * np.sin(q_grid / 2))**2
    qhat2_sum = qhat2_sum.sum(axis=-1)
    return 1.0 / (qhat2_sum + m_reg**2)


def kite_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_T1a(p_ext) (kite contribution to gluon self-energy) /(C_A^2).

    Uses Wilson V_3g_ym at each vertex, bare 1/k̂² propagators
    with IR regulator m_reg.

    Returns Σ^{μν} as a 4×4 numpy array (dimensionless × C_A^2).

    Computational cost: O(N^8) operations, O(N^4) memory.
    """
    k1_grid = lattice_grid(N)              # (N^4, 4)
    Npts = k1_grid.shape[0]
    p_ext_arr = np.asarray(p_ext, dtype=float)

    # V_L is fixed across the k2 loop (depends only on k1, p):
    # V_L vertex: V_3g_ym(p_ext, -k1, k1-p_ext) with Lorentz (ν, α, β)
    p1_VL = np.tile(p_ext_arr, (Npts, 1))     # (Npts, 4): p_ext repeated
    p2_VL = -k1_grid                          # -k1 incoming at V_L
    p3_VL = k1_grid - p_ext_arr[np.newaxis, :]  # k1-p incoming at V_L
    V_L = build_V3g_kinematic(p1_VL, p2_VL, p3_VL)  # (Npts, 4, 4, 4) [ν, α, β]

    # D(k1) and D(p-k1) propagators (k2-independent)
    D_k1 = lattice_prop(k1_grid, m_reg)                # (Npts,)
    D_pk1 = lattice_prop(p_ext_arr[np.newaxis, :] - k1_grid, m_reg)  # D(p-k1)

    # Outer loop over k2: accumulate Σ^{μν}
    Sigma = np.zeros((4, 4), dtype=float)
    inv_vol2 = (1.0 / N**4)**2  # (1/N^4)^2 measure for double sum

    t_start = time.time()
    for k2_idx in range(Npts):
        k2 = k1_grid[k2_idx]  # (4,) — fix k2 for this slice

        # V_T vertex: V_3g_ym(k1, k2-k1, -k2) with Lorentz (α, γ, ε)
        p1_VT = k1_grid                              # +k1 incoming
        p2_VT = k2[np.newaxis, :] - k1_grid          # k2-k1 incoming
        p3_VT = np.tile(-k2, (Npts, 1))              # -k2 incoming
        V_T = build_V3g_kinematic(p1_VT, p2_VT, p3_VT)  # (Npts, 4, 4, 4) [α, γ, ε]

        # V_R vertex: V_3g_ym(-p, k1-k2, p-k1+k2) with Lorentz (μ, γ, δ)
        p1_VR = np.tile(-p_ext_arr, (Npts, 1))
        p2_VR = k1_grid - k2[np.newaxis, :]
        p3_VR = p_ext_arr[np.newaxis, :] - k1_grid + k2[np.newaxis, :]
        V_R = build_V3g_kinematic(p1_VR, p2_VR, p3_VR)  # (Npts, 4, 4, 4) [μ, γ, δ]

        # V_B vertex: V_3g_ym(p-k1, k1-k2-p, k2) with Lorentz (β, δ, ε)
        p1_VB = p_ext_arr[np.newaxis, :] - k1_grid
        p2_VB = k1_grid - k2[np.newaxis, :] - p_ext_arr[np.newaxis, :]
        p3_VB = np.tile(k2, (Npts, 1))
        V_B = build_V3g_kinematic(p1_VB, p2_VB, p3_VB)  # (Npts, 4, 4, 4) [β, δ, ε]

        # Propagators (k2-dependent ones)
        D_k2 = lattice_prop(k2[np.newaxis, :], m_reg)[0]                   # scalar (k2 fixed)
        D_k1mk2 = lattice_prop(k1_grid - k2[np.newaxis, :], m_reg)         # D(k1-k2)
        D_pk1pk2 = lattice_prop(p_ext_arr[np.newaxis, :] - k1_grid + k2[np.newaxis, :], m_reg)  # D(p-k1+k2)

        # Combined propagator weight (over k1 grid, with k2 fixed)
        prop_weight = D_k1 * D_k1mk2 * D_pk1 * D_pk1pk2 * D_k2  # (Npts,)

        # Lorentz contraction:
        #   K^{μν}(p, k1, k2) = Σ_{α,β,γ,δ,ε}
        #     V_L[ν,α,β] V_T[α,γ,ε] V_R[μ,γ,δ] V_B[β,δ,ε]
        #
        # Two intermediate einsums (α and δ summed first):
        #   VLVT[k1, ν, β, γ, ε] = Σ_α V_L[k1,ν,α,β] V_T[k1,α,γ,ε]
        #   VRVB[k1, μ, γ, β, ε] = Σ_δ V_R[k1,μ,γ,δ] V_B[k1,β,δ,ε]
        # Then final sum over (k1, β, γ, ε) with prop_weight via einsum.
        # Cache einsum paths on first iter (otherwise path computation cost
        # dominates; einsum with cached path is faster than naive matmul
        # reshape due to transpose-copy overhead).
        if k2_idx == 0:
            _path_VLVT = np.einsum_path('kvab,kage->kvbge', V_L, V_T, optimize='optimal')[0]
            _path_VRVB = np.einsum_path('kmgd,kbde->kmgbe', V_R, V_B, optimize='optimal')[0]

        VLVT = np.einsum('kvab,kage->kvbge', V_L, V_T, optimize=_path_VLVT)
        VRVB = np.einsum('kmgd,kbde->kmgbe', V_R, V_B, optimize=_path_VRVB)

        if k2_idx == 0:
            _path_final = np.einsum_path('k,kvbge,kmgbe->mv',
                                         prop_weight, VLVT, VRVB,
                                         optimize='optimal')[0]
        # Σ^{μν} += slice contribution via cached-path einsum
        Sigma += np.einsum('k,kvbge,kmgbe->mv',
                           prop_weight, VLVT, VRVB,
                           optimize=_path_final)

        if verbose and (k2_idx % max(1, Npts // 8) == 0 or k2_idx == Npts - 1):
            dt = time.time() - t_start
            frac = (k2_idx + 1) / Npts
            eta = dt * (1 - frac) / frac if frac > 0 else 0
            print(f"    [k2 {k2_idx+1}/{Npts} = {100*frac:.1f}%]  elapsed {dt:.1f}s  ETA {eta:.1f}s", flush=True)

    # Apply symmetry factor 1/2 and double-integration measure
    Sigma *= 0.5 * inv_vol2
    return Sigma


def compute_PiT_kite(N, m_reg, verbose=False):
    """Extract Π_T from T1a kite at smallest lattice p along ê_0.

    Π_T per C_A^2 from the kite alone (sub-piece of full 1PI 2-loop SE).
    """
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])

    if verbose:
        print(f"  Computing T1a kite Σ^{{μν}}(p) at N={N}, m_reg={m_reg}, p_ext={p_ext}")
    Sigma = kite_sigma(N, p_ext, m_reg, verbose=verbose)

    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2  # phat^2 for p along ê_0

    # Π_T = (Σ^{11} - Σ^{00}) / phat^2  (cancels gauge-violating mass)
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


# ============================================================
# Sanity tests and small-N runs
# ============================================================

def test_V3g_grid_consistency(N=4):
    """Sanity: build_V3g_kinematic on a grid should agree with V_3g_ym scalar."""
    print(f"=== build_V3g_kinematic vs V_3g_ym scalar (N={N}) ===")
    np.random.seed(42)
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_ext = (2 * np.pi / N) * np.array([1.0, 0.0, 0.0, 0.0])

    p1 = np.tile(p_ext, (Npts, 1))
    p2 = -k_grid
    p3 = k_grid - p_ext[np.newaxis, :]
    V = build_V3g_kinematic(p1, p2, p3)  # shape (Npts, 4, 4, 4)

    # Spot-check at a few random points
    test_idx = [0, Npts // 4, Npts // 2, Npts - 1]
    max_err = 0.0
    for idx in test_idx:
        p1_i, p2_i, p3_i = p1[idx], p2[idx], p3[idx]
        for mu1 in range(4):
            for mu2 in range(4):
                for mu3 in range(4):
                    expected = V_3g_ym(p1_i, p2_i, p3_i, mu1, mu2, mu3)
                    got = V[idx, mu1, mu2, mu3]
                    err = abs(expected - got)
                    if err > max_err:
                        max_err = err
    print(f"  Max abs error across {len(test_idx)} points × 64 indices: {max_err:.2e}")
    assert max_err < 1e-12, "build_V3g_kinematic disagrees with V_3g_ym scalar!"
    print(f"  PASS\n")


def run_small_N_scan():
    """Run T1a kite at N = 4, 6, 8 with several m_reg values, report Π_T."""
    print("=" * 70)
    print("=== T1a kite contribution to Π_T (per C_A^2) at finite N ===")
    print("=" * 70)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'Sigma^00':>14} {'Sigma^11':>14} {'time':>9}")

    for N in [4, 6, 8]:
        for m_reg in [0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_kite(N, m_reg, verbose=(N >= 8))
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+14.6e} {Sigma[1,1]:>+14.6e} {dt:>8.1f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** T1a kite topology, standard-QCD pure-YM at 2-loop ***\n")
    test_V3g_grid_consistency(N=4)
    run_small_N_scan()
