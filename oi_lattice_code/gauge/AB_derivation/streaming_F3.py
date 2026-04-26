"""
Memory-efficient OI bubble with c_F3 · F³ vertex correction.

Combines the Wilson-plaquette 3-gluon kernel with the continuum F³
kernel (weighted by c_F3) and streams the loop momentum in chunks.
"""
import numpy as np
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from streaming_ghost import compute_ghost_sigma_streaming
from p_extrapolation import small_p_fit


def _build_V3g_with_F3_chunk(p1v, p2v, p3v, c_F3):
    """Build K_total = K_YM_lat + c_F3 · K_F3_cont for a chunk.

    p1v: (4,) — external scalar momentum (the "first" leg)
    p2v: (chunk, 4) — second leg
    p3v: (chunk, 4) — third leg
    Returns (chunk, 4, 4, 4) — V[k, μ, α, β].
    """
    chunk = p2v.shape[0]

    # Wilson piece
    p1h = 2*np.sin(p1v/2)
    p2h = 2*np.sin(p2v/2)
    p3h = 2*np.sin(p3v/2)
    cos1h = np.cos(p1v/2)
    cos2h = np.cos(p2v/2)
    cos3h = np.cos(p3v/2)

    V = np.zeros((chunk, 4, 4, 4), dtype=float)
    for mu in range(4):
        for al in range(4):
            for be in range(4):
                val = np.zeros(chunk)
                if mu == al:
                    val += cos3h[:, mu] * (p1h[be] - p2h[:, be])
                if al == be:
                    val += cos1h[al] * (p2h[:, mu] - p3h[:, mu])
                if be == mu:
                    val += cos2h[:, be] * (p3h[:, al] - p1h[al])
                V[:, mu, al, be] = val

    # F³ piece (continuum form)
    if c_F3 != 0.0:
        p1_dot_p2 = np.einsum('j,kj->k', p1v, p2v)
        p1_dot_p3 = np.einsum('j,kj->k', p1v, p3v)
        p2_dot_p3 = np.einsum('kj,kj->k', p2v, p3v)
        dlt = np.eye(4)
        for m1 in range(4):
            for m2 in range(4):
                for m3 in range(4):
                    t = np.zeros(chunk)
                    t += p1v[m3] * p2v[:, m1] * p3v[:, m2]
                    t -= p1_dot_p3 * p2v[:, m1] * dlt[m2, m3]
                    t -= p2_dot_p3 * p1v[m3] * dlt[m1, m2]
                    t += p1_dot_p3 * p2v[:, m3] * dlt[m1, m2]
                    t -= p1_dot_p2 * p3v[:, m2] * dlt[m1, m3]
                    t += p1_dot_p2 * p3v[:, m1] * dlt[m2, m3]
                    t += p2_dot_p3 * p1v[m2] * dlt[m1, m3]
                    t -= p1v[m2] * p2v[:, m3] * p3v[:, m1]
                    V[:, m1, m2, m3] += c_F3 * t
    return V


def compute_bubble_with_F3_streaming(N, m, p_ext, c_F3, pi_s_val=None, batch_size=None):
    """Streaming version of compute_bubble_at_p_with_F3."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    dk = 2*np.pi/N
    vol = 1.0 / N**4
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    Npts = N**4

    if batch_size is None:
        batch_size = min(50000, max(1000, Npts // 64))

    Sigma = np.zeros((4, 4), dtype=float)
    for start in range(0, Npts, batch_size):
        end = min(start + batch_size, Npts)
        flat_idx = np.arange(start, end)
        i0 = flat_idx // (N**3); i1 = (flat_idx // (N**2)) % N
        i2 = (flat_idx // N) % N; i3 = flat_idx % N
        k_chunk = np.stack([
            idx_shifted[i0], idx_shifted[i1], idx_shifted[i2], idx_shifted[i3],
        ], axis=-1).astype(float) * dk

        # First vertex: V_3g(p_ext, k, -(p+k))
        mk = -(p_ext + k_chunk)
        V = _build_V3g_with_F3_chunk(p_ext, k_chunk, mk, c_F3)

        # Second vertex: V_3g(-p_ext, -k, p+k)
        V2 = _build_V3g_with_F3_chunk(-p_ext, -k_chunk, p_ext + k_chunk, c_F3)

        VV = np.einsum('kmab,knab->kmn', V, V2)

        khat2_sum = ((2*np.sin(k_chunk/2))**2).sum(axis=-1)
        D_k = np.where(khat2_sum > 1e-12, 1.0/(khat2_sum * pi_s_val), 0.0)
        pkhat2_sum = ((2*np.sin((p_ext + k_chunk)/2))**2).sum(axis=-1)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0/(pkhat2_sum * pi_s_val), 0.0)

        weight = D_k * D_pk * vol
        Sigma += 0.5 * np.einsum('k,kmn->mn', weight, VV)

    return Sigma, pi_s_val


def compute_PiT_Pi_s2_at_N_streaming(N, m, c_F3, pi_s, lambda_vals=(1, 2, 3), batch_size=None):
    """Compute Π_T·Π_s² at p²→0 by linear fit, with F³ correction."""
    kappa = 2*np.pi/N
    p2_lats = []
    PiT_vals = []
    for lam in lambda_vals:
        p_ext = lam * kappa * np.array([1, 0, 0, 0])
        Sigma_bub, _ = compute_bubble_with_F3_streaming(N, m, p_ext, c_F3, pi_s_val=pi_s, batch_size=batch_size)
        Sigma_gh = compute_ghost_sigma_streaming(N, p_ext, use_induced=True, pi_s_val=pi_s, m=m, batch_size=batch_size)
        Sigma = Sigma_bub + Sigma_gh
        p_0 = lam * kappa
        p2_lat = (2*np.sin(p_0/2))**2
        PiT = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
        p2_lats.append(p2_lat)
        PiT_vals.append(PiT)
    a, b = small_p_fit(np.array(p2_lats), np.array(PiT_vals))
    return a * pi_s**2
