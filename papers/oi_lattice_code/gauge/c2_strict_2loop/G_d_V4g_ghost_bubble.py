"""
G_d_V4g_ghost_bubble.py — 1PI 2-loop standard-QCD
G_d "V_4g + ghost-bubble" topology

Topology:

    p ──→ V_4g (2 ext + 2 internal gluons) ──→ -p
              │                │
              k_1, σ_4g (ρ)    -k_1, σ_4g (σ)
              │                │
              V_ghg_A ════ g_1, g_2 ════ V_ghg_B
                  (closed ghost loop)

- 1 V_4g (external attachment + 2 internal gluons to V_ghg's)
- 2 V_ghg (ghost-loop vertices)
- 4 internal lines: 2 gluons (V_4g ↔ V_ghg) + 2 ghosts (V_ghg ↔ V_ghg doubled)
- 1 closed ghost loop

Color: 2 · C_A^2 (channels 2 + 3 of V_4g, channel 1 vanishes by f-antisymmetry
under c=d contraction; ghost-bubble color contraction adds another C_A factor).

Lorentz structure: Sum of channels 2 and 3 of V_4g, contracted with V_ghg
factors (k_1-k_2)̂^ρ at A and k_2̂^σ at B, gives:

  N^{μν}(k_1) = ∑_{k_2} D_gh(k_2) D_gh(k_1-k_2) ·
                [2 δ^{μν} (k_1-k_2)̂·k_2̂  -  (k_1-k_2)̂^μ k_2̂^ν  -  (k_1-k_2)̂^ν k_2̂^μ]

The inner sub-integral is a convolution in k_2; we exploit FFT to compute
it for all k_1 simultaneously in O(N^4 log N), giving total cost O(N^4 log N).

Symmetry factor: 1/2 (V_ghg_A ↔ V_ghg_B reflection)
Ghost-loop sign: -1 explicit

V_ghg vertex convention: V_gh^μ = q_out^μ where q is the outgoing ghost
momentum; lattice version q̂^μ = 2 sin(q_μ/2). Same as ghost_self_energy.py.

V_4g convention: continuum (momentum-independent), per T1c precedent.
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


# Total color coefficient in units of C_A^2
G_D_COLOR_OVER_CA2 = 2.0      # Channels 2 and 3 each contribute C_A^2; total 2 C_A^2


def lattice_prop_ghost(k_arr, eps=1e-12):
    """Standard ghost propagator on the lattice: 1/k̂² (no IR mass term)."""
    khat = 2 * np.sin(k_arr / 2)
    khat2 = (khat ** 2).sum(axis=-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(khat2 > eps, 1.0 / khat2, 0.0)


def compute_J_tensor_FFT(N):
    """Compute J^{ρσ}(k_1) for all k_1 using FFT.

    J^{ρσ}(k_1) = ∑_{k_2} D_gh(k_2) D_gh(k_1-k_2) · (k_1-k_2)̂^ρ · k_2̂^σ
                = (g^ρ * g^σ)(k_1)
    where g^ρ(k) = k̂^ρ · D_gh(k) and * denotes convolution in BZ.

    Using the convolution theorem:
        J^{ρσ}(k_1) = N^4 · IFFT[ FFT(g^ρ) · FFT(g^σ) ](k_1)

    Returns:
        J_tensor: shape (N, N, N, N, 4, 4) with J_tensor[k1, ρ, σ] = J^{ρσ}(k_1).
        Note: J^{ρσ} is NOT symmetric in (ρ ↔ σ) in general.
    """
    # Build g^ρ(k) = k̂^ρ · D_gh(k) for ρ = 0..3
    k_grid_4d = lattice_grid_4d(N)    # (N, N, N, N, 4)
    khat_4d = 2 * np.sin(k_grid_4d / 2)           # (N, N, N, N, 4)
    khat2_4d = (khat_4d ** 2).sum(axis=-1)        # (N, N, N, N)
    with np.errstate(divide='ignore', invalid='ignore'):
        D_gh_4d = np.where(khat2_4d > 1e-12, 1.0 / khat2_4d, 0.0)   # (N, N, N, N)

    # g^ρ(k) = k̂^ρ · D_gh(k), shape (N, N, N, N, 4)
    g_k = khat_4d * D_gh_4d[..., np.newaxis]      # broadcast D_gh: (N, N, N, N, 4)

    # FFT each g^ρ to position space: tilde_g^ρ(x) = FFT(g^ρ)(x)
    tilde_g_x = np.fft.fftn(g_k, axes=(0, 1, 2, 3))   # (N, N, N, N, 4)

    # Convolution J^{ρσ}(k_1) = N^4 · IFFT[ tilde_g^ρ(x) · tilde_g^σ(x) ]
    # Compute outer product tilde_g^ρ(x) · tilde_g^σ(x) for each x, shape (N,N,N,N,4,4)
    tilde_g_outer = tilde_g_x[..., :, np.newaxis] * tilde_g_x[..., np.newaxis, :]  # (N,N,N,N,4,4)

    # Inverse FFT
    J_tensor = np.fft.ifftn(tilde_g_outer, axes=(0, 1, 2, 3)) * N**4 / N**4
    # Note: np.fft.ifftn already includes 1/N^4 normalization; we want sum_x not average,
    # so we need to multiply by N^4 to undo this. But we also need the 1/N^4 from BZ measure
    # for the original convolution. Net: J = IFFT(...) (with FFT/IFFT both unnormalized
    # would give *N^4; with numpy's normalized convention, IFFT is /N^4 and FFT is *1, so
    # to get the convolution sum without measure we multiply IFFT by N^4).

    # The result should be real (since g^ρ is real and conv of real is real)
    J_tensor = np.real(J_tensor)
    return J_tensor    # (N, N, N, N, 4, 4)


def lattice_grid_4d(N):
    """Return BZ grid as (N, N, N, N, 4) tensor of momenta."""
    dk = 2 * np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N // 2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted,
                                  indexing='ij')
    return np.stack([I0 * dk, I1 * dk, I2 * dk, I3 * dk], axis=-1).astype(float)


def V4g_ghost_bubble_sigma(N, p_ext, m_reg, verbose=False):
    """Compute Σ^{μν}_G_d(p_ext) per C_A^2.

    Cost: O(N^4 log N) via FFT for inner ghost-bubble.
    """
    # Step 1: compute the ghost-bubble J^{ρσ}(k_1) at all k_1 via FFT
    if verbose:
        t0 = time.time()
    J_tensor = compute_J_tensor_FFT(N)    # (N, N, N, N, 4, 4)
    if verbose:
        print(f"  FFT J-tensor in {time.time() - t0:.3f}s")

    # Step 2: outer integral over k_1
    k_grid_4d = lattice_grid_4d(N)         # (N, N, N, N, 4)
    khat_4d = 2 * np.sin(k_grid_4d / 2)
    khat2_sum = (khat_4d ** 2).sum(axis=-1)
    D_k1_4d = 1.0 / (khat2_sum + m_reg ** 2)   # (N, N, N, N)
    D_k1_squared = D_k1_4d ** 2                 # gluon prop squared (D(k_1) · D(-k_1))

    # Numerator structure:
    # N^{μν}(k_1) = 2 δ^{μν} · Tr(J(k_1)) - J^{μν}(k_1) - J^{νμ}(k_1)
    Tr_J = np.einsum('...ii', J_tensor)          # (N, N, N, N)
    J_sym = J_tensor + J_tensor.swapaxes(-2, -1)  # (N,N,N,N,4,4) — J + J^T

    delta = np.eye(4)
    # 2 δ^{μν} · Tr_J(k_1) - J_sym^{μν}(k_1)
    # Construct via broadcasting:
    N_kin = 2.0 * Tr_J[..., np.newaxis, np.newaxis] * delta[np.newaxis, np.newaxis, np.newaxis, np.newaxis, :, :] - J_sym

    # Σ^{μν}/C_A² = -1/2 · (1/N^4) · sum_{k_1} D(k_1)² · N_kin^{μν}(k_1)
    # Note: J already has the (1/N^4) factor for the inner k_2 sum (FFT convention).
    # Wait, let me check: J = IFFT(FFT · FFT). Numpy's IFFT divides by N^4; FFT does NOT.
    # So J_tensor[k_1] = (1/N^4) · sum_x FFT(g^ρ)(x) FFT(g^σ)(x) · exp(...)
    # = (1/N^4) · sum_x [sum_{k_2} g^ρ(k_2) e^{i k_2 x}] [sum_{k_3} g^σ(k_3) e^{i k_3 x}] e^{-i k_1 x}
    # = (1/N^4) · sum_{k_2, k_3} g^ρ(k_2) g^σ(k_3) sum_x e^{i (k_2 + k_3 - k_1) x}
    # = sum_{k_2, k_3} g^ρ(k_2) g^σ(k_3) · δ_{k_2 + k_3 = k_1}
    # = sum_{k_2} g^ρ(k_2) · g^σ(k_1 - k_2)
    # ✓ This is exactly the convolution (no 1/N^4 measure).

    # The integration measure for the k_2 sum should be (1/N^4); so J above is missing it.
    # Hmm wait: the sum sum_{k_2} D D (k_1-k_2)^ρ k_2^σ is what we want, NOT (1/N^4) sum.
    # We apply the measure when we write the final integral.
    #
    # OK so J_tensor as computed = sum_{k_2} (without measure).
    # Then Σ^{μν} = (sym=1/2) · (-1) · (1/N^4)^2 · sum_{k_1, k_2} ... = (1/2)(-1)(1/N^4)^2 sum_{k_1} D² · J(k_1) · numerator_factor
    # And we apply (1/N^4)^2 once outside.

    pre_factor = -0.5 * (1.0 / N**4)**2
    Sigma = pre_factor * np.einsum('ijkl,ijklmn->mn', D_k1_squared, N_kin)
    return Sigma


def compute_PiT_G_d(N, m_reg, verbose=False):
    """Extract Π_T from G_d at smallest lattice p along ê_0."""
    kappa = 2 * np.pi / N
    p_ext = kappa * np.array([1.0, 0.0, 0.0, 0.0])
    if verbose:
        print(f"  Computing G_d at N={N}, m_reg={m_reg}")
    Sigma = V4g_ghost_bubble_sigma(N, p_ext, m_reg, verbose=verbose)
    p_0 = p_ext[0]
    p2_lat = (2 * np.sin(p_0 / 2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    return Pi_T, Sigma


def verify_color_coefficient():
    """Verify G_d color factor = 2 · C_A^2."""
    from colors import f_abc
    F = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                F[a, b, c] = f_abc(a + 1, b + 1, c + 1)
    C_A = 3.0

    # G_d color: V_4g_color * ghost_bubble_color, with c_A=c_B contracted
    #
    # Channel 1 (a,b)(c,d): f^{abe}f^{cde}, c=d → 0
    # Channel 2 (a,c)(b,d): f^{ace}f^{bde}, c=d=c': sum_{c',e} f^{ac'e}f^{bc'e} = C_A δ^{ab}
    # Channel 3 (a,d)(b,c): f^{ade}f^{bce}, c=d=c': sum f^{ac'e}f^{bc'e} = C_A δ^{ab}
    # Ghost-bubble color: f^{c c_g1 c_g2} f^{d c_g1 c_g2} sum c_g1, c_g2 = C_A δ^{cd}
    # → V_4g·(c=d)·ghost_bubble = (0 + C_A δ^{ab} + C_A δ^{ab}) · C_A = 2 C_A^2 δ^{ab}

    ch_1_contracted = np.einsum('abe,ffe->ab', F, F)  # f^{abe} f^{cce}, sum c=f
    # Above: f^{ffe} for f=summed-c, but it's a self-contraction over f. Let me redo:
    ch_1_contracted = np.einsum('abe,cce->ab', F, F)  # = 0
    ch_2_contracted = np.einsum('ace,bce->ab', F, F)  # = C_A δ^{ab}
    ch_3_contracted = np.einsum('ace,bce->ab', F, F)  # same form via c_A=c_B=c
    G_d_color = (ch_1_contracted + ch_2_contracted + ch_3_contracted) * C_A
    diag_avg = np.mean(np.diag(G_d_color))
    off_max = np.max(np.abs(G_d_color - diag_avg * np.eye(8)))
    expected = 2.0 * C_A**2
    print(f"=== G_d V_4g + ghost-bubble color verification (SU(3)) ===")
    print(f"  Color factor: {diag_avg:.6f} = {diag_avg/C_A**2:.4f} · C_A^2  "
          f"(expected {expected/C_A**2:.4f} · C_A^2 = {expected:.4f})")
    print(f"  δ^ab off-diag max: {off_max:.2e}")
    pass1 = abs(diag_avg / C_A**2 - G_D_COLOR_OVER_CA2) < 1e-10
    print(f"  {'PASS' if pass1 else 'FAIL'}\n")
    return pass1


def run_small_N_scan():
    print("=" * 78)
    print("=== G_d V_4g + ghost-bubble Π_T (per C_A^2) — O(N^4 log N) FFT ===")
    print("=== Sign includes -1 from closed ghost loop ===")
    print("=" * 78)
    print(f"\n{'N':>3} {'m_reg':>8} {'Pi_T':>14} {'Σ^00':>13} {'Σ^11':>13} {'time':>8}")
    for N in [4, 6, 10, 16, 20]:
        for m_reg in [0.3, 0.2, 0.1]:
            t0 = time.time()
            Pi_T, Sigma = compute_PiT_G_d(N, m_reg, verbose=False)
            dt = time.time() - t0
            print(f"{N:>3} {m_reg:>8.3f} {Pi_T:>+14.6e} "
                  f"{Sigma[0,0]:>+13.4e} {Sigma[1,1]:>+13.4e} {dt:>7.3f}s",
                  flush=True)
        print()


if __name__ == "__main__":
    print("\n*** G_d V_4g + ghost-bubble, standard-QCD pure-YM at 2-loop ***\n")
    verify_color_coefficient()
    run_small_N_scan()
