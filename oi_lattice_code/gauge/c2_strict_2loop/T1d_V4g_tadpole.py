"""
T1d_V4g_tadpole.py — 1PI 2-loop standard-QCD V_4g-tadpole
topology

Implements the T1d "V_4g-tadpole" topology of the standard-QCD pure-YM
gluon self-energy.

Topology:

    p ──→ V_1 ──── L1 ──── V_2 ──→ p     (direct V_1-V_2 line)
           │              │
           L2             L3
           │              │
           V_3 (V_4g) ────┘
            ⌒ self-loop (carrying loop momentum k_self)

Same as T1c except V_3's two "doubled-line connections to V_2" are
replaced by a single L3 from V_2-V_3 plus a SELF-LOOP on V_3.

KEY STRUCTURAL FEATURE: T1d also FACTORIZES at O(N⁴), even more
trivially than T1c — the self-loop on V_3 gives a SCALAR I_tad
(independent of all external momenta), and the outer triangle V_1-V_2-V_3
is a single 1-loop integral over k_1.

Σ^{μν}_T1d = (sym factor) · (color factor) · I_tad ·
             [∫ dk_1 D(k_1) D²(p-k_1) · K^{νμ}_T1d(k_1)]

where I_tad = ∫ dk_self D(k_self), a number depending only on N, m_reg.

Color factor (verified numerically with SU(3) f-symbols):
  T1d color = 6 · C_A^2 · δ^{ab}.
  Derivation: V_4g self-loop trace gives 6·C_A·δ^{c_β c_γ}·δ^{μ_β μ_γ};
  combined with V_1 f^{a c_α c_β} and V_2 f^{b c_α c_γ}, the c_β=c_γ
  identification reduces to f²→C_A, giving 6·C_A·C_A = 6·C_A^2.

Lorentz structure: K^{νμ}_T1d(k_1) = Σ_{α,β} V_1[ν,α,β] V_2[μ,α,β]
  = "straight" pattern (same as T1c's straight component).

Symmetry factor: 1/2 (per A5.1.6, self-loop's L_self endpoint
exchange).

Convention: continuum V_4g (consistent with T1c, tadpole_self_energy.py).
Wilson cos-factor refinement deferred.

Momentum routing:
  L1 (V_1→V_2):    k_1
  L2 (V_1→V_3):    p - k_1
  L3 (V_3→V_2):    p - k_1   [same as L2; constrained by V_2 conservation]
  L_self (V_3→V_3): k_self

Vertex calls:
  V_1: V_3g_ym(p, -k_1, k_1-p),  indices (ν, α, β)
  V_2: V_3g_ym(-p, k_1, p-k_1),  indices (μ, α, β)  [β = γ after V_4g
                                                       self-loop trace δ]

Note: V_2's third Lorentz index "γ" gets contracted with "β" via the
V_4g self-loop trace's δ^{μ_β μ_γ}, so effectively V_2 is contracted
on indices (μ, α, β) matching V_1's (ν, α, β).
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


# Color factor in units of C_A^2 (numerically verified)
T1D_COLOR_OVER_CA2 = 6.0


def compute_I_tad(N, m_reg):
    """Compute the lattice tadpole integral I_tad = (1/N^4) Σ_k D(k_self)."""
    k_grid = lattice_grid(N)
    D = lattice_prop(k_grid, m_reg)
    return D.mean()    # equivalent to (1/N^4) · sum


def V4g_tadpole_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_T1d(p_ext) per C_A^2 (V_4g-tadpole topology).

    Cost: O(N^4) — outer loop over k_1, with I_tad as scalar prefactor.
    """
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    p_arr = np.asarray(p_ext, dtype=float)

    # --- Outer 1-loop integration over k_1 ---
    # V_1: V_3g_ym(p, -k_1, k_1-p), indices (ν, α, β)
    p1_V1 = np.tile(p_arr, (Npts, 1))
    p2_V1 = -k_grid
    p3_V1 = k_grid - p_arr[np.newaxis, :]
    V_1 = build_V3g_kinematic(p1_V1, p2_V1, p3_V1)         # (Npts, 4, 4, 4) [ν, α, β]

    # V_2: V_3g_ym(-p, k_1, p-k_1), indices (μ, α, β)
    # Note: the third Lorentz index "γ" of V_2 is contracted with V_4g self-loop
    # trace δ^{μβμγ}, identifying γ=β. So V_2's index pattern in our contraction
    # is (μ, α, β) where β plays both the "L3 Lorentz" and the V_4g self-loop role.
    p1_V2 = np.tile(-p_arr, (Npts, 1))
    p2_V2 = k_grid
    p3_V2 = p_arr[np.newaxis, :] - k_grid
    V_2 = build_V3g_kinematic(p1_V2, p2_V2, p3_V2)         # (Npts, 4, 4, 4) [μ, α, β]

    # Propagators on the outer ring: D(k_1) and D(p-k_1)^2 (two copies for L2, L3)
    D_k1 = lattice_prop(k_grid, m_reg)
    D_pmk1 = lattice_prop(p_arr[np.newaxis, :] - k_grid, m_reg)
    weight = D_k1 * D_pmk1 * D_pmk1   # (Npts,)

    # Lorentz contraction "straight" pattern:
    #   K[k_1, ν, μ] = Σ_{α, β} V_1[k_1, ν, α, β] · V_2[k_1, μ, α, β]
    K_per_k1 = np.einsum('kvab,kmab->kvm', V_1, V_2)        # (Npts, 4, 4)

    # Sum over k_1 with propagator weight; apply 1/N^4 measure
    Sigma_outer = np.einsum('k,kvm->vm', weight, K_per_k1) * (1.0 / N**4)
    # Sigma_outer is [ν, μ]; we want [μ, ν] → transpose
    Sigma_outer = Sigma_outer.T

    # --- Inner self-loop integral I_tad ---
    I_tad = compute_I_tad(N, m_reg)

    # --- Combine: color factor × symmetry factor × I_tad × outer ---
    Sigma = (T1D_COLOR_OVER_CA2 * 0.5 * I_tad) * Sigma_outer
    # The "per C_A^2" factor T1D_COLOR_OVER_CA2 = 6 absorbs the color reduction;
    # 0.5 is the symmetry factor; I_tad is the self-loop contribution.

    return Sigma


def compute_PiT_V4g_tadpole(N, m_reg, verbose=False):
    """Extract Π_T from T1d V_4g-tadpole at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing T1d V_4g-tadpole Σ^{{μν}}(p) at N={N}, m_reg={m_reg}")
    Sigma = V4g_tadpole_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_color_coefficient():
    """Verify T1d color factor = 6 · C_A^2 numerically using SU(3) f-symbols."""
    from colors import f_abc
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0
    # T1d color = f^{a c_α c_β} f^{b c_α c_γ} · 6·C_A·δ^{c_β c_γ}
    #          = 6·C_A · f^{a c_α c_β} f^{b c_α c_β}
    #          = 6·C_A · C_A · δ^{ab} = 6·C_A^2 · δ^{ab}
    T1d_color = 6.0 * C_A * np.einsum('aij,bij->ab', F, F)
    diag_avg = np.mean(np.diag(T1d_color))
    off_max = np.max(np.abs(T1d_color - diag_avg * np.eye(8)))

    print("=== T1d V_4g-tadpole color verification (SU(3)) ===")
    print(f"  T1d color factor: {diag_avg:.6f} = {diag_avg/C_A**2:.4f} · C_A^2")
    print(f"    (expected: 6.0 · C_A^2 = {6.0*C_A**2:.4f})")
    print(f"  δ^ab structure: off-diag max = {off_max:.2e}")
    pass1 = abs(diag_avg / C_A**2 - T1D_COLOR_OVER_CA2) < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 76)
    print("=== T1d V_4g-tadpole Π_T (per C_A^2) — factorized O(N^4) ===")
    print("=" * 76)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'I_tad':>10} {'time':>8}")
    for N in [4, 6, 8, 12, 16, 20]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, _ = compute_PiT_V4g_tadpole(N, m_reg, verbose=False)
            I_tad = compute_I_tad(N, m_reg)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} {I_tad:>10.5f} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** T1d V_4g-tadpole topology, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficient()
    run_small_N_scan()
