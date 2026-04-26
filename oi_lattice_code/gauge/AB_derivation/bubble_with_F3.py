"""
bubble_with_F3.py — bubble calculation with F³ dim-6 vertex correction.

Drop-in extension of bubble_at_finite_p.compute_bubble_at_p that replaces
the pure Wilson-plaquette 3-gluon vertex K_YM with

    K_total(p₁,p₂,p₃; μ₁,μ₂,μ₃) = K_YM_lat + c_F3 · K_F3_cont

where K_F3_cont is the continuum F³ kinematic tensor (f3_vertex.K_F3).
The F³ piece is O(a²) more UV-suppressed than the YM piece, so the
continuum form is adequate at small external momentum; more careful
lattice regularization of K_F3 is a refinement if needed.

This script:
  1. Reproduces A·B at c_F3 = 0 (baseline, expected ≈ 48.0).
  2. Sweeps c_F3 ∈ {−0.1, −0.034, 0, +0.034, +0.1} to extract ΔA·B / Δc_F3.
  3. Reports the F³ systematic estimate: |ΔA·B(c_F3 = −0.034)| / A·B₀.
"""
import numpy as np
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from yang_mills_lattice import V_3g_ym, p_hat
# Note: K_F3 is inlined below (lines 81-94 of original) rather than imported
from ghost_self_energy import compute_ghost_sigma_at_p
from p_extrapolation import extract_PiT_times_pis2, small_p_fit


def build_V3g_with_F3_at_external_p(N, p_ext, c_F3):
    """K_total = K_YM_lat(Wilson-plaquette) + c_F3 · K_F3_cont.

    Returns (Npts, 4, 4, 4) tensor V[k, μ, α, β] at external p_ext and
    loop momenta (k, -p_ext-k), where k ranges over the N^4 BZ grid.
    """
    dk = 2 * np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N // 2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0 * dk, I1 * dk, I2 * dk, I3 * dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    Npts = k_flat.shape[0]

    mk = -(p_ext[np.newaxis, :] + k_flat)  # (Npts, 4)

    # --- Wilson-plaquette piece K_YM_lat — existing code ---
    p1 = p_ext
    p1h = 2 * np.sin(p1 / 2)
    p2h = 2 * np.sin(k_flat / 2)
    p3h = 2 * np.sin(mk / 2)
    cos1h = np.cos(p1 / 2)
    cos2h = np.cos(k_flat / 2)
    cos3h = np.cos(mk / 2)

    V = np.zeros((Npts, 4, 4, 4), dtype=float)
    for mu in range(4):
        for al in range(4):
            for be in range(4):
                val = np.zeros(Npts)
                if mu == al:
                    val += cos3h[:, mu] * (p1h[be] - p2h[:, be])
                if al == be:
                    val += cos1h[al] * (p2h[:, mu] - p3h[:, mu])
                if be == mu:
                    val += cos2h[:, be] * (p3h[:, al] - p1h[al])
                V[:, mu, al, be] = val

    # --- F³ piece K_F3_cont — add with coefficient c_F3 ---
    if c_F3 != 0.0:
        # Vectorize the 8 terms of K_F3 over the Npts loop momenta.
        # p_1 = p_ext (scalar), p_2 = k_flat (Npts, 4), p_3 = mk (Npts, 4).
        p1v = p_ext
        p2v = k_flat
        p3v = mk
        p1_dot_p2 = np.einsum('j,kj->k', p1v, p2v)       # (Npts,)
        p1_dot_p3 = np.einsum('j,kj->k', p1v, p3v)       # (Npts,)
        p2_dot_p3 = np.einsum('kj,kj->k', p2v, p3v)      # (Npts,)
        dlt = np.eye(4)
        KF3 = np.zeros((Npts, 4, 4, 4), dtype=float)
        for m1 in range(4):
            for m2 in range(4):
                for m3 in range(4):
                    t = np.zeros(Npts)
                    t += p1v[m3] * p2v[:, m1] * p3v[:, m2]                     # (+++)
                    t -= p1_dot_p3 * p2v[:, m1] * dlt[m2, m3]                  # (++−)
                    t -= p2_dot_p3 * p1v[m3] * dlt[m1, m2]                     # (+−+)
                    t += p1_dot_p3 * p2v[:, m3] * dlt[m1, m2]                  # (+−−)
                    t -= p1_dot_p2 * p3v[:, m2] * dlt[m1, m3]                  # (−++)
                    t += p1_dot_p2 * p3v[:, m1] * dlt[m2, m3]                  # (−+−)
                    t += p2_dot_p3 * p1v[m2] * dlt[m1, m3]                     # (−−+)
                    t -= p1v[m2] * p2v[:, m3] * p3v[:, m1]                     # (−−−)
                    KF3[:, m1, m2, m3] = t
        V += c_F3 * KF3

    return V, k_flat


def compute_bubble_at_p_with_F3(N, m, p_ext, c_F3, pi_s_val=None):
    """Drop-in replacement for compute_bubble_at_p with F³ vertex correction."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    vol = 1.0 / N ** 4

    V, k_flat = build_V3g_with_F3_at_external_p(N, p_ext, c_F3)
    Npts = V.shape[0]

    # Second vertex: V_3g(-p_ext, -k, p_ext+k). Build directly with the
    # F³ piece included.
    V2, _ = build_V3g_with_F3_at_external_p(N, -p_ext, c_F3)
    # But build_V3g_with_F3_at_external_p uses loop variable k_flat consistent
    # with p_ext; for the second vertex we need to supply "-k, p_ext+k" as the
    # loop momenta. The original code handled this by manually constructing V2
    # with the appropriate (p1_2, p2_2, p3_2). Do the same here.
    mk = -(p_ext[np.newaxis, :] + k_flat)
    p1_2 = -p_ext
    p2_2 = -k_flat
    p3_2 = p_ext[np.newaxis, :] + k_flat

    # Wilson piece
    p1h_2 = 2 * np.sin(p1_2 / 2)
    p2h_2 = 2 * np.sin(p2_2 / 2)
    p3h_2 = 2 * np.sin(p3_2 / 2)
    cos1h_2 = np.cos(p1_2 / 2)
    cos2h_2 = np.cos(p2_2 / 2)
    cos3h_2 = np.cos(p3_2 / 2)

    V2 = np.zeros((Npts, 4, 4, 4), dtype=float)
    for mu in range(4):
        for al in range(4):
            for be in range(4):
                val = np.zeros(Npts)
                if mu == al:
                    val += cos3h_2[:, mu] * (p1h_2[be] - p2h_2[:, be])
                if al == be:
                    val += cos1h_2[al] * (p2h_2[:, mu] - p3h_2[:, mu])
                if be == mu:
                    val += cos2h_2[:, be] * (p3h_2[:, al] - p1h_2[al])
                V2[:, mu, al, be] = val

    # F³ piece for V2
    if c_F3 != 0.0:
        p1v = p1_2
        p2v = p2_2
        p3v = p3_2
        p1_dot_p2 = np.einsum('j,kj->k', p1v, p2v)
        p1_dot_p3 = np.einsum('j,kj->k', p1v, p3v)
        p2_dot_p3 = np.einsum('kj,kj->k', p2v, p3v)
        dlt = np.eye(4)
        KF3_2 = np.zeros((Npts, 4, 4, 4), dtype=float)
        for m1 in range(4):
            for m2 in range(4):
                for m3 in range(4):
                    t = np.zeros(Npts)
                    t += p1v[m3] * p2v[:, m1] * p3v[:, m2]
                    t -= p1_dot_p3 * p2v[:, m1] * dlt[m2, m3]
                    t -= p2_dot_p3 * p1v[m3] * dlt[m1, m2]
                    t += p1_dot_p3 * p2v[:, m3] * dlt[m1, m2]
                    t -= p1_dot_p2 * p3v[:, m2] * dlt[m1, m3]
                    t += p1_dot_p2 * p3v[:, m1] * dlt[m2, m3]
                    t += p2_dot_p3 * p1v[m2] * dlt[m1, m3]
                    t -= p1v[m2] * p2v[:, m3] * p3v[:, m1]
                    KF3_2[:, m1, m2, m3] = t
        V2 += c_F3 * KF3_2

    # Induced gauge propagators on loop lines
    khat2_sum = ((2 * np.sin(k_flat / 2)) ** 2).sum(axis=-1)
    D_k = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)

    pkh = p_ext + k_flat
    pkhat2_sum = ((2 * np.sin(pkh / 2)) ** 2).sum(axis=-1)
    D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / (pkhat2_sum * pi_s_val), 0.0)

    VV = np.einsum('kmab,knab->kmn', V, V2)
    weight = D_k * D_pk * vol
    Sigma = 0.5 * np.einsum('k,kmn->mn', weight, VV)

    return Sigma, pi_s_val


def compute_PiT_Pi_s2_at_N(N, m, c_F3, pi_s, use_induced_ghost=True,
                            lambda_vals=(1, 2, 3)):
    """For given (N, m, c_F3), compute Π_T·Π_s² at p²→0 by linear fit."""
    kappa = 2 * np.pi / N
    p2_lats = []
    PiT_vals = []
    for lam in lambda_vals:
        p_ext = lam * kappa * np.array([1, 0, 0, 0])
        Sigma_bub, _ = compute_bubble_at_p_with_F3(N, m, p_ext, c_F3, pi_s_val=pi_s)
        Sigma_gh = compute_ghost_sigma_at_p(N, p_ext, use_induced=use_induced_ghost,
                                             pi_s_val=pi_s, m=m)
        Sigma = Sigma_bub + Sigma_gh
        p_0 = lam * kappa
        p2_lat = (2 * np.sin(p_0 / 2)) ** 2
        PiT = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
        p2_lats.append(p2_lat)
        PiT_vals.append(PiT)
    # Linear fit Π(p²) = a + b·p², return intercept
    a, b = small_p_fit(np.array(p2_lats), np.array(PiT_vals))
    return a * pi_s ** 2


def main():
    print("=" * 72)
    print("F³ correction sweep: A·B(c_F3) at fixed N, m")
    print("=" * 72)
    print()
    print("Baseline (c_F3 = 0) should reproduce A·B ≈ 48.0 at N→∞.")
    print("Sweep around c_F3 ≈ −0.034 (a conservative upper-bound extraction).")
    print()
    print("The A·B-relevant output here is Π_T·Π_s²(N) ≈ b₀_capture(N) × 11/3 × N_c.")
    print("A·B is the convergent extrapolation of this sequence × π² (see reproduce_AB.py).")
    print()

    m = 0.05
    c_F3_values = [0.0, -0.034, -0.01, +0.034, +0.1]
    N_values = [8, 12, 16]   # budget: keep small for a sweep

    results = {}  # (N, c_F3) -> PiT_Pi_s2
    for N in N_values:
        pi_s = compute_pi_s(N, m)
        print(f"--- N = {N}, m = {m}, Π_s = {pi_s:.4f} ---")
        for c in c_F3_values:
            t0 = time.time()
            val = compute_PiT_Pi_s2_at_N(N, m, c, pi_s)
            dt = time.time() - t0
            results[(N, c)] = val
            print(f"  c_F3 = {c:+.4f}:  Π_T·Π_s² = {val:+.5f}  [{dt:.1f}s]", flush=True)
        print()

    # Summary table
    print("=" * 72)
    print("Summary: shift in Π_T·Π_s² induced by F³")
    print("=" * 72)
    print(f"{'N':>3}  " + "  ".join(f"{'c='+f'{c:+.3f}':>12}" for c in c_F3_values))
    for N in N_values:
        row = [f"{results[(N, c)]:>12.5f}" for c in c_F3_values]
        print(f"{N:>3}  " + "  ".join(row))

    # Relative shift from c_F3 = 0 to c_F3 = -0.034
    print()
    print("Relative shift at c_F3 = −0.034 vs c_F3 = 0:")
    for N in N_values:
        base = results[(N, 0.0)]
        shifted = results[(N, -0.034)]
        if abs(base) > 1e-12:
            pct = 100 * (shifted - base) / base
            print(f"  N={N}:  ΔΠ_T·Π_s² / Π_T·Π_s² = {pct:+.2f}%")


if __name__ == "__main__":
    main()
