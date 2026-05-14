"""
G_b_ghost_vertex_correction.py — 1PI 2-loop standard-QCD
G_b "ghost vertex correction" topology

Ghost analog of T1b vertex correction. Inner V_3-V_4 doubled gluon
lines are replaced by V_ghg-V_ghg with doubled GHOST lines (closed
ghost loop).

Topology:

    p ──→ V_1 (V_3g) ──── L1 ──── V_2 (V_3g) ──→ p     (outer gluon)
            │                       │
           L2 (gluon)              L3 (gluon)
            │                       │
            V_3 (V_ghg) ────g₁ ────  V_4 (V_ghg)
                       ────g₂────
                  (closed ghost loop g₁, g₂)

Key features:
- 2 V_3g (external) + 2 V_ghg (inner, where ghost loop terminates)
- 5 internal lines: 3 gluon (L1 outer, L2 V_1-V_3, L3 V_2-V_4) + 2 ghost
- 1 closed ghost loop (g₁ + g₂ doubled-line cycle V_3 ↔ V_4)
- Sign: -1 from closed ghost loop

Color factor: C_A^2 (verified numerically). Same as T1a, T1b.

V_ghg vertex factor (per ghost_self_energy.py convention):
  V_gh^μ(p_gluon, q_ghost) = q^μ
  where q is the OUTGOING ghost momentum, μ is the gluon Lorentz index.
  Lattice version: q̂^μ = 2 sin(q_μ/2).

Momentum routing (analog of T1b):
  L1 (V_1 → V_2): k_1
  L2 (V_1 → V_3): p - k_1
  L3 (V_2 → V_4): -(p - k_1) = k_1 - p   [equal magnitude, opposite direction]
  g₁ (V_3 → V_4): k_2
  g₂ (V_4 → V_3): p - k_1 - k_2          [outgoing at V_4]

Vertex calls:
  V_1: V_3g_ym(p, -k_1, k_1-p), Lorentz (ν, α, β)
  V_2: V_3g_ym(-p, k_1, p-k_1), Lorentz (μ, α, γ)
  V_3 (V_ghg): gluon Lorentz β, outgoing-ghost-momentum k_2
              → vertex factor k̂_2^β
  V_4 (V_ghg): gluon Lorentz γ, outgoing-ghost-momentum (p-k_1-k_2)
              → vertex factor (p̂ - k̂_1 - k̂_2)^γ
  Note: lattice momentum factors q̂_μ = 2 sin(q_μ/2) — these are
  applied to the SUM of momenta (not on each individually).

Symmetry factor: 1/2 (V_1 ↔ V_2 reflection)
Ghost loop sign: -1

Convention: standard ghost propagator D_gh(k) = 1/k̂². Same as
ghost_self_energy.py (use_induced=False).

Cost: O(N^8) brute-force, sliced like T1b.
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


# Color factor in units of C_A^2: 1.0 (same as T1a, T1b)
G_B_COLOR_OVER_CA2 = 1.0


def lattice_prop_ghost(k_arr, eps=1e-12):
    """Standard ghost propagator on the lattice: 1/k̂² (no IR mass term —
    the ghost propagator in pure gauge theory is exactly 1/k̂²; lattice
    IR is regulated by the BZ structure for nonzero p_ext).

    For numerical safety we set 1/0 → 0 at the zero-mode."""
    khat = 2 * np.sin(k_arr / 2)
    khat2 = (khat ** 2).sum(axis=-1)
    return np.where(khat2 > eps, 1.0 / khat2, 0.0)


def lattice_prop_gluon(k_arr, m_reg):
    """Wilson gluon propagator: 1/(k̂² + m²)."""
    khat = 2 * np.sin(k_arr / 2)
    return 1.0 / ((khat ** 2).sum(axis=-1) + m_reg ** 2)


def ghost_vertex_correction_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_G_b(p_ext) per C_A^2 (G_b ghost vertex correction).

    Returns the 4×4 Σ^{μν} per C_A^2 (with the closed-ghost-loop -1
    sign already applied).

    Cost: O(N^8) brute-force. Outer loop k_2, inner vectorize k_1.
    """
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_arr = np.asarray(p_ext, dtype=float)

    # ---- Pre-compute V_1, V_2 (depend on k_1 only) ----
    p1_V1 = np.tile(p_arr, (Npts, 1))
    p2_V1 = -k_grid                           # -k_1
    p3_V1 = k_grid - p_arr[np.newaxis, :]     # k_1 - p
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)         # (Npts, 4, 4, 4) [ν, α, β]

    p1_V2 = np.tile(-p_arr, (Npts, 1))
    p2_V2 = k_grid                            # k_1
    p3_V2 = p_arr[np.newaxis, :] - k_grid     # p - k_1
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)         # (Npts, 4, 4, 4) [μ, α, γ]

    # Gluon propagators (function of k_1 only)
    D_k1 = lattice_prop_gluon(k_grid, m_reg)
    D_pmk1 = lattice_prop_gluon(p_arr[np.newaxis, :] - k_grid, m_reg)
    weight_outer = D_k1 * D_pmk1 * D_pmk1     # (Npts,) — D(k_1) D²(p-k_1)

    # Pre-compute U[k_1, ν, μ, β, γ] = sum_α V_1[k_1, ν, α, β] · V_2[k_1, μ, α, γ]
    # This is the "α-contracted V_1·V_2" — k_2-independent.
    # Cost: O(N^4 · 4^4) = small.
    U = np.einsum('kvab,kmag->kvmbg', V_1, V_2)            # (Npts, 4, 4, 4, 4) [ν, μ, β, γ]

    # ---- Outer loop over k_2 ----
    Sigma_accum = np.zeros((4, 4))    # [ν, μ]

    if verbose:
        print(f"  G_b: looping k_2 over {Npts} points (N={N})")

    for k2_idx in range(Npts):
        k2 = k_grid[k2_idx]

        # Ghost momenta and vertex factors at this k_2 slice:
        # g_1 (V_3 → V_4): momentum k_2 (k_2-fixed) → V_3 vertex factor k̂_2^β
        # g_2 (V_4 → V_3): momentum p - k_1 - k_2 (depends on k_1) → V_4 factor q̂^γ
        khat_2 = 2 * np.sin(k2 / 2)    # (4,) — k̂_2 for V_3 vertex factor

        # Ghost momenta with k_1 dependence
        q_g2 = p_arr[np.newaxis, :] - k_grid - k2[np.newaxis, :]     # (Npts, 4) — momentum at g_2
        qhat_g2 = 2 * np.sin(q_g2 / 2)                                # (Npts, 4) — V_4 vertex factor

        # Ghost propagators
        D_gh_k2 = lattice_prop_ghost(k2[np.newaxis, :])               # scalar for k_2
        D_gh_q = lattice_prop_ghost(q_g2)                              # (Npts,) for k_1 array

        # Total weight per k_1 (with k_2 fixed):
        # gluon[k_1] · gluon[p-k_1]² · ghost[k_2] · ghost[q]
        weight_k1 = weight_outer * D_gh_k2 * D_gh_q                    # (Npts,)

        # Numerator (Lorentz): U[k_1, ν, μ, β, γ] · k̂_2^β · q̂_g2[k_1, γ]
        # Sum over β, γ:
        # numer[k_1, ν, μ] = sum_β k̂_2^β · sum_γ U[k_1, ν, μ, β, γ] · q̂_g2[k_1, γ]
        # Reduce: einsum('kvmbg, b, kg -> kvm', U, khat_2, qhat_g2)
        numer = np.einsum('kvmbg,b,kg->kvm', U, khat_2, qhat_g2)       # (Npts, 4, 4)

        # Accumulate sum over k_1
        Sigma_accum += np.einsum('k,kvm->vm', weight_k1, numer)

    # Apply integration measure (1/N^4)^2, symmetry factor 1/2, ghost-loop sign -1
    Sigma = Sigma_accum * (1.0 / N**4)**2 * 0.5 * (-1.0)

    # Return Σ^{μν} = Σ^{ν μ}.T (consistent with T1a, T1b convention)
    return Sigma.T


def compute_PiT_ghost_vertex_correction(N, m_reg, verbose=False):
    """Extract Π_T from G_b at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing G_b ghost vertex correction at N={N}, m_reg={m_reg}")
    Sigma = ghost_vertex_correction_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_color_coefficient():
    """Verify G_b color factor = C_A^2 by direct f-symbol contraction."""
    from colors import f_abc
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0
    # G_b color tensor:
    #   sum_{c_outer, c_3, c_4, c_g1, c_g2}
    #     f^{a c_outer c_3} f^{b c_outer c_4} · f^{c_3 c_g1 c_g2} · f^{c_4 c_g1 c_g2}
    # Inner: f^{c_3 c_g1 c_g2} f^{c_4 c_g1 c_g2} sum c_g1, c_g2 = C_A · δ^{c_3 c_4}
    # → G_b_color = C_A · sum f^{a c_outer c_3} f^{b c_outer c_3} = C_A · C_A · δ^{ab} = C_A^2 · δ^{ab}
    G_b_color = C_A * np.einsum('aij,bij->ab', F, F)
    diag_avg = np.mean(np.diag(G_b_color))
    off_max = np.max(np.abs(G_b_color - diag_avg * np.eye(8)))
    print(f"=== G_b ghost vertex correction color verification (SU(3)) ===")
    print(f"  Color factor: {diag_avg:.6f} = {diag_avg/C_A**2:.4f} · C_A^2  "
          f"(expected 1.0 · C_A^2 = {C_A**2:.4f})")
    print(f"  δ^ab off-diag max: {off_max:.2e}")
    pass1 = abs(diag_avg / C_A**2 - G_B_COLOR_OVER_CA2) < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 78)
    print("=== G_b ghost vertex correction Π_T (per C_A^2) — O(N^8) brute force ===")
    print("=== Sign includes -1 from closed ghost loop ===")
    print("=" * 78)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'Σ^00':>13} {'Σ^11':>13} {'time':>8}")
    for N in [4, 6]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_ghost_vertex_correction(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** G_b ghost vertex correction, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficient()
    run_small_N_scan()
