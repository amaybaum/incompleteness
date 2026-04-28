"""
G_a_ghost_square.py — 1PI 2-loop standard-QCD G_a "ghost-square"
topology (analog of T1a kite).

Topology: 4 V_ghg vertices arranged in a square + 1 internal gluon chord.
External momenta enter at V_L (Lorentz μ, color a) and V_R (Lorentz ν,
color b), via the V_ghg gluon legs at those vertices.

      V_L ───L1 (ghost)─── V_T
       │                    │
      L4 (ghost)         L5 (gluon chord)
       │                    │
      V_B ───L3 (ghost)─── V_R
       │
       └── L1 closes back through V_R via L3 (cycle V_L-V_T-V_R-V_B-V_L)

Wait, more precise: ghost cycle is V_L → V_T → V_R → V_B → V_L (4 ghosts L1, L2, L3, L4).
Chord L5 connects V_T ↔ V_B (gluon line, Feynman gauge δ^{σσ'}).

- 4 V_ghg + 1 ghost-cycle (L1, L2, L3, L4) + 1 gluon chord (L5)
- 5 internal lines, 4 vertices
- 1 closed ghost loop (4-cycle)

Momentum routing (with loop variables k_1 = L2 momentum, k_2 = chord L5 momentum):
  L1 (V_L → V_T): k_1 + k_2
  L2 (V_T → V_R): k_1
  L3 (V_R → V_B): k_1 - p
  L4 (V_B → V_L): k_1 + k_2 - p
  L5 (V_T → V_B chord): k_2

V_ghg vertex factors (V_gh^μ = outgoing-ghost-momentum^μ, lattice version 2 sin(q_μ/2)):
  V_L (gluon Lorentz μ, ghost out L1):     (k_1 + k_2)̂^μ
  V_T (gluon Lorentz σ, ghost out L2):     k_1̂^σ
  V_R (gluon Lorentz ν, ghost out L3):     (k_1 - p)̂^ν
  V_B (gluon Lorentz σ', ghost out L4):    (k_1 + k_2 - p)̂^σ'

Chord propagator: D_gluon(k_2) δ^{σσ'} → contracts σ = σ'.

Lorentz numerator:
  N^{μν}(p; k_1, k_2) = (k_1+k_2)̂^μ · (k_1-p)̂^ν · D_gluon(k_2) · [k_1̂ · (k_1+k_2-p)̂]

Color: 0.5 · C_A^2 (verified numerically via 4-vertex f^{...} contraction)

Symmetry factor: 1/2 (V_L ↔ V_R reflection, and possibly also V_T ↔ V_B chord-direction)
  We use 1/2 for V_L ↔ V_R only; if higher symmetry exists it would reduce further.

Ghost-loop sign: -1 (closed ghost loop)

Cost: O(N^8) brute force at small N. (FFT optimization possible.)
"""
import numpy as np
import os, sys, time

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from T1a_kite import lattice_grid


# Color coefficient in units of C_A^2
G_A_COLOR_OVER_CA2 = 0.5


def lattice_prop_ghost(k_arr, eps=1e-12):
    khat = 2 * np.sin(k_arr / 2)
    khat2 = (khat ** 2).sum(axis=-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(khat2 > eps, 1.0 / khat2, 0.0)


def lattice_prop_gluon(k_arr, m_reg):
    khat = 2 * np.sin(k_arr / 2)
    return 1.0 / ((khat ** 2).sum(axis=-1) + m_reg ** 2)


def ghost_square_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_G_a(p_ext) per C_A^2.

    Cost: O(N^8) brute force; outer loop k_2 (gluon chord momentum),
    inner vectorize k_1 (ghost cycle parameter).
    """
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_arr = np.asarray(p_ext, dtype=float)

    # ---- Pre-compute k_1-only quantities ----
    # k_1: shape (Npts, 4). Ghost props for L2 (k_1), L3 (k_1-p)
    khat_k1 = 2 * np.sin(k_grid / 2)                        # (Npts, 4) — k_1̂
    k1_minus_p = k_grid - p_arr[np.newaxis, :]
    khat_k1mp = 2 * np.sin(k1_minus_p / 2)                  # (Npts, 4) — (k_1-p)̂

    D_gh_k1 = lattice_prop_ghost(k_grid)                    # (Npts,) — D(L2)
    D_gh_k1mp = lattice_prop_ghost(k1_minus_p)              # (Npts,) — D(L3)

    weight_k1 = D_gh_k1 * D_gh_k1mp                         # (Npts,)

    # ---- Outer loop over k_2 (chord momentum) ----
    Sigma_accum = np.zeros((4, 4))   # [μ, ν]

    if verbose:
        print(f"  G_a: looping k_2 over {Npts} points (N={N})")

    for k2_idx in range(Npts):
        k2 = k_grid[k2_idx]

        # k_2 fixed: compute remaining quantities depending on (k_1, k_2)
        # L1 momentum: k_1 + k_2
        # L4 momentum: k_1 + k_2 - p
        k_1_plus_k_2 = k_grid + k2[np.newaxis, :]                    # (Npts, 4)
        khat_k1pk2 = 2 * np.sin(k_1_plus_k_2 / 2)                    # (Npts, 4)
        k_1_plus_k_2_minus_p = k_1_plus_k_2 - p_arr[np.newaxis, :]
        khat_k1pk2mp = 2 * np.sin(k_1_plus_k_2_minus_p / 2)          # (Npts, 4)

        D_gh_L1 = lattice_prop_ghost(k_1_plus_k_2)                   # (Npts,)
        D_gh_L4 = lattice_prop_ghost(k_1_plus_k_2_minus_p)           # (Npts,)
        D_gluon_k2 = lattice_prop_gluon(k2[np.newaxis, :], m_reg)[0] # scalar

        # Product weight per k_1
        weight = weight_k1 * D_gh_L1 * D_gh_L4 * D_gluon_k2          # (Npts,)

        # Lorentz numerator:
        # N^{μν} = (k_1+k_2)̂^μ · (k_1-p)̂^ν · [k_1̂ · (k_1+k_2-p)̂]
        # Compute scalar contraction k_1̂ · (k_1+k_2-p)̂ first
        k1_dot_L4 = np.einsum('ka,ka->k', khat_k1, khat_k1pk2mp)     # (Npts,)

        # Outer: (k_1+k_2)̂^μ · (k_1-p)̂^ν → outer product (Npts, 4, 4)
        outer_munu = np.einsum('km,kn->kmn', khat_k1pk2, khat_k1mp)  # (Npts, 4, 4)

        # Combine: weight · k1_dot_L4 · outer_munu, summed over k_1
        contrib = np.einsum('k,k,kmn->mn', weight, k1_dot_L4, outer_munu)
        Sigma_accum += contrib

    # Apply prefactors: (1/N^4)^2 · sym (1/2) · ghost-loop sign (-1)
    Sigma = Sigma_accum * (1.0 / N**4)**2 * 0.5 * (-1.0)
    return Sigma


def compute_PiT_G_a(N, m_reg, verbose=False):
    """Extract Π_T from G_a at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing G_a at N={N}, m_reg={m_reg}")
    Sigma = ghost_square_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_color_coefficient():
    """G_a color factor verification."""
    from colors import f_abc
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0
    G_a_color = np.einsum('aji,eik,bkl,elj->ab', F, F, F, F)
    diag_avg = np.mean(np.diag(G_a_color))
    off_max = np.max(np.abs(G_a_color - diag_avg * np.eye(8)))
    expected = G_A_COLOR_OVER_CA2 * C_A**2
    print(f"=== G_a ghost-square color verification (SU(3)) ===")
    print(f"  Color factor: {diag_avg:.6f} = {diag_avg/C_A**2:.4f} · C_A^2  "
          f"(expected {expected/C_A**2:.4f} · C_A^2 = {expected:.4f})")
    print(f"  δ^ab off-diag max: {off_max:.2e}")
    pass1 = abs(diag_avg / C_A**2 - G_A_COLOR_OVER_CA2) < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 78)
    print("=== G_a ghost-square Π_T (per C_A^2) — O(N^8) brute force ===")
    print("=== Sign includes -1 from closed ghost loop ===")
    print("=" * 78)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'Σ^00':>13} {'Σ^11':>13} {'time':>8}")
    for N in [4, 6]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_G_a(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** G_a ghost-square, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficient()
    run_small_N_scan()
