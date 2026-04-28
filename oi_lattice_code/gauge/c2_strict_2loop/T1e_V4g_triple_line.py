"""
T1e_V4g_triple_line.py — 1PI 2-loop standard-QCD V_4g-V_4g
"triple-line" topology

Implements the T1e topology of the standard-QCD pure-YM gluon
this is the unique S2 (0 V_3g + 2 V_4g) topology.

Topology (Mercedes / triple-line):

       p ──→ V_1 ╪╪╪ (3 internal lines L1, L2, L3) ╪╪╪ V_2 ──→ p

Both V_1 and V_2 are V_4g vertices, each with one external leg and 3
internal legs. The 3 internal lines all run V_1 → V_2 in parallel.

KEY ANALYTIC RESULT (continuum-V_4g convention):

  Π_T_T1e = 0 STRICTLY.

  The kinematic numerator K^{νμ} is independent of all loop momenta
  AND of external p (because continuum V_4g has no momentum dependence,
  and external p enters only through propagators). By 4D hypercubic
  symmetry, K^{νμ} ∝ δ^{νμ}. Therefore:

    Σ^{μν}_T1e = K_const · δ^{μν} · I_sunset(p)

  and Π_T = (Σ^{11} - Σ^{00})/p² = 0.

  T1e contributes only to the longitudinal/mass piece Σ^{00}, NOT to
  the transverse self-energy.

  Numerically verified: K^{νμ} = 27 · C_A^2 · δ^{νμ} (off-diagonals
  exactly zero, machine precision).

  Combined with symmetry factor 1/6:

    Σ^{μν}_T1e = (27/6) C_A^2 · δ^{μν} · I_sunset(p)
              = (9/2) C_A^2 · δ^{μν} · I_sunset(p)

  where I_sunset(p) = (1/N^4)^2 · Σ_{k1,k2} D(k1) D(k2) D(p-k1-k2).

Color decomposition (verified numerically with SU(3) f-symbols):
  9 channel-pair coefficients C_(i,j) (units of C_A^2):
                j=1    j=2    j=3
       i=1     1.0    0.5    0.5
       i=2     0.5    1.0   -0.5
       i=3     0.5   -0.5    1.0
  Sum = 4 · C_A^2.

Lorentz decomposition (each (i,j) gives K_(i,j)^{νμ} = c · δ^{νμ}):
                j=1    j=2    j=3
       i=1     +6     +3     +3
       i=2     +3     +6     -3
       i=3     +3     -3     +6
  Color × Lorentz combined: 27 · δ^{νμ}.

Symmetry factor: 1/3! = 1/6 (three indistinguishable parallel lines)
per A5.1.6.

Convention: continuum V_4g (consistent with T1c, T1d, A5.4 decision).
With Wilson V_4g cos-factor refinement, V_4g would acquire momentum
dependence and Π_T_T1e would be nonzero (a²-suppressed correction).
This is logged as a Implementation: I_sunset(p) computed via FFT in O(N^4 log N).
"""
import numpy as np
import os, sys, time

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')
AB_DIR = os.path.join(HERE, '..', 'AB_derivation')
sys.path.insert(0, HERE)
sys.path.insert(0, AB_DIR)

from T1a_kite import lattice_grid, lattice_prop


# Combined kinematic constant: K_const_T1e = 27 (units of C_A^2)
K_CONST_OVER_CA2 = 27.0
# Symmetry factor
SYMMETRY_FACTOR = 1.0 / 6.0


def compute_I_sunset_fft(N, p_ext, m_reg):
    """Compute I_sunset(p) = (1/N^4)^2 · Σ_{k1, k2} D(k1) D(k2) D(p-k1-k2)
    via FFT in O(N^4 log N).

    Uses the convolution identity:
      (D ★ D ★ D)(p) = N^8 · FFT[ iFFT(D)^3 ](p)
    where ★ is discrete convolution. With the (1/N^4)^2 measure:
      I_sunset(p) = (1/N^8) · (D ★ D ★ D)(p) = FFT[ iFFT(D)^3 ](p).
    """
    k_grid = lattice_grid(N)                        # (N^4, 4)
    D_flat = lattice_prop(k_grid, m_reg)             # (N^4,)
    D = D_flat.reshape((N, N, N, N))                 # 4D BZ array

    # iFFT to position space
    D_x = np.fft.ifftn(D)                            # complex; D_x is real if D is real
    # Cube in position space
    D_x_cubed = D_x ** 3
    # FFT back to momentum space
    I_sunset_full = np.fft.fftn(D_x_cubed).real      # (N, N, N, N)

    # Pick out the value at p = (p0, 0, 0, 0)  in lattice index (p_idx, 0, 0, 0)
    # p_ext is given as continuum momentum κ · n; n is the index.
    kappa = 2 * np.pi / N
    p_idx = tuple(int(round(p_ext[d] / kappa)) % N for d in range(4))
    return I_sunset_full[p_idx]


def compute_I_sunset_direct(N, p_ext, m_reg):
    """Direct (slow) double-sum reference for I_sunset, for FFT
    cross-validation. O(N^8) — only use for small N."""
    k_grid = lattice_grid(N)
    Npts = k_grid.shape[0]
    D = lattice_prop(k_grid, m_reg)
    p_arr = np.asarray(p_ext, dtype=float)
    total = 0.0
    for k1_idx in range(Npts):
        k1 = k_grid[k1_idx]
        # D(p - k1 - k2) for all k2
        D_third = lattice_prop(p_arr[np.newaxis, :] - k1[np.newaxis, :] - k_grid, m_reg)
        # Inner sum over k2
        total += D[k1_idx] * np.sum(D * D_third)
    return total / (N**4)**2


def V4g_triple_line_sigma(N, p_ext, m_reg):
    """Compute Σ^{μν}_T1e(p_ext) per C_A^2.

    Returns the full 4×4 Σ tensor. By analytical structure:
      Σ^{μν}_T1e = (sym × K_const) · δ^{μν} · I_sunset(p)
    """
    I_sunset = compute_I_sunset_fft(N, p_ext, m_reg)
    coef = SYMMETRY_FACTOR * K_CONST_OVER_CA2 * I_sunset
    return coef * np.eye(4)


def compute_PiT_V4g_triple_line(N, m_reg, verbose=False):
    """Extract Π_T from T1e at smallest lattice p along ê_0.

    Predicted: Π_T_T1e = 0 strictly (since Σ^{μν} ∝ δ^{μν})."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing T1e V_4g-V_4g triple-line Σ^{{μν}}(p) at N={N}, m_reg={m_reg}")
    Sigma = V4g_triple_line_sigma(N, p_ext, m_reg)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_K_constant():
    """Verify analytically that K^{νμ}_T1e = 27 · δ^{νμ} (units of C_A^2)
    by direct construction of the 9 channel-pair contributions."""
    from colors import f_abc

    # Color tensors
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0

    def build_V4g_color_tensor(ch):
        """T[a, c1, c2, c3] = color factor of V_4g channel ch with leg 1 = ext (a)."""
        T = np.zeros((8, 8, 8, 8))
        if ch == 1:
            # f^{a c1 e} f^{c2 c3 e}
            T[:] = np.einsum('ace,bce->abce', F, F)[..., 0:1].squeeze()  # placeholder
            # Direct loop is cleaner:
            for a in range(8):
                for c1 in range(8):
                    for c2 in range(8):
                        for c3 in range(8):
                            T[a, c1, c2, c3] = np.sum(F[a, c1, :] * F[c2, c3, :])
        elif ch == 2:
            for a in range(8):
                for c1 in range(8):
                    for c2 in range(8):
                        for c3 in range(8):
                            T[a, c1, c2, c3] = np.sum(F[a, c2, :] * F[c1, c3, :])
        elif ch == 3:
            for a in range(8):
                for c1 in range(8):
                    for c2 in range(8):
                        for c3 in range(8):
                            T[a, c1, c2, c3] = np.sum(F[a, c3, :] * F[c2, c1, :])
        return T

    def build_V4g_lorentz_tensor(ch):
        L = np.zeros((4, 4, 4, 4))
        for m1 in range(4):
            for m2 in range(4):
                for m3 in range(4):
                    for m4 in range(4):
                        if ch == 1:
                            L[m1, m2, m3, m4] = (m1 == m3) * (m2 == m4) - (m1 == m4) * (m2 == m3)
                        elif ch == 2:
                            L[m1, m2, m3, m4] = (m1 == m2) * (m3 == m4) - (m1 == m4) * (m2 == m3)
                        elif ch == 3:
                            L[m1, m2, m3, m4] = (m1 == m3) * (m2 == m4) - (m1 == m2) * (m3 == m4)
        return L

    T_chans = [build_V4g_color_tensor(c) for c in [1, 2, 3]]
    L_chans = [build_V4g_lorentz_tensor(c) for c in [1, 2, 3]]

    # 9 channel-pair contributions
    K_total = np.zeros((4, 4))
    color_matrix = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            # Color: contract the 3 internal color indices
            C_ij_full = np.einsum('aijk,bijk->ab', T_chans[i], T_chans[j])
            c_ij = np.mean(np.diag(C_ij_full)) / C_A**2
            color_matrix[i, j] = c_ij
            # Lorentz: contract the 3 internal Lorentz indices
            K_ij = np.einsum('vabc,mabc->vm', L_chans[i], L_chans[j])
            # Combine
            K_total += c_ij * K_ij

    K_diag = np.mean(np.diag(K_total))
    K_off = np.max(np.abs(K_total - K_diag * np.eye(4)))
    print("=== T1e V_4g-V_4g triple-line K^{νμ} verification ===")
    print(f"  Color matrix C_(i,j) (units of C_A^2):")
    for i in range(3):
        print(f"    [ {color_matrix[i,0]:>+5.2f}  {color_matrix[i,1]:>+5.2f}  {color_matrix[i,2]:>+5.2f} ]")
    print(f"  K^{{νμ}} diag: {K_diag:.4f} (expected {K_CONST_OVER_CA2:.4f})")
    print(f"  K^{{νμ}} off-diag max: {K_off:.2e} (expected 0)")
    pass1 = abs(K_diag - K_CONST_OVER_CA2) < 1e-10 and K_off < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}: K^{{νμ}} = {K_CONST_OVER_CA2} · δ^{{νμ}} confirmed.\n")
    return pass1


def test_fft_vs_direct(N=4, m_reg=0.2):
    """Cross-validate FFT-based I_sunset against direct double-sum."""
    print(f"=== T1e I_sunset FFT vs direct (N={N}, m_reg={m_reg}) ===")
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])

    t0 = time.time()
    I_fft = compute_I_sunset_fft(N, p_ext, m_reg)
    t_fft = time.time() - t0

    t0 = time.time()
    I_direct = compute_I_sunset_direct(N, p_ext, m_reg)
    t_direct = time.time() - t0

    rel_diff = abs(I_fft - I_direct) / abs(I_direct)
    print(f"  FFT:    {I_fft:>+14.8e}    ({t_fft:.4f}s)")
    print(f"  Direct: {I_direct:>+14.8e}    ({t_direct:.4f}s)")
    print(f"  Rel diff: {rel_diff:.2e}")
    pass1 = rel_diff < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 76)
    print("=== T1e V_4g-V_4g triple-line — Π_T predicted 0, Σ^{00} via FFT ===")
    print("=" * 76)
    print(f"\n{'N':>3} {'m_reg':>8} {'I_sunset(p)':>15} {'Σ^00':>13} {'Σ^11':>13} {'Pi_T':>14} {'time':>8}")
    for N in [4, 6, 8, 12, 16, 20]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_V4g_triple_line(N, m_reg, verbose=False)
            kappa = 2 * np.pi / N
            p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
            I_s = compute_I_sunset_fft(N, p_ext, m_reg)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {I_s:>+15.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} "
                  f"{Pi_T:>+14.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** T1e V_4g-V_4g triple-line topology, standard-QCD pure-YM at 2-loop ***\n")
    verify_K_constant()
    test_fft_vs_direct(N=4, m_reg=0.2)
    test_fft_vs_direct(N=6, m_reg=0.2)
    run_small_N_scan()
