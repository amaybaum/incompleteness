"""
Streaming version of bubble_standard_qcd, ghost_standard_qcd, and compute_Pi_T_qcd.
"""
import numpy as np
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from streaming_bubble import _build_V3g_chunk


def bubble_standard_qcd_streaming(N, p_ext, m_reg=None, batch_size=None):
    """Memory-efficient bubble with standard 1/k̂² propagator."""
    dk = 2*np.pi / N
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
        
        # Vertices
        # The qcd_crosscheck uses build_V3g_at_external_p_v2 (same shifted-BZ form).
        # First vertex V_3g(p, k, -p-k); but the qcd code's first vertex has
        # NO sign flip on p_ext for the first vertex. Looking at v2: p1=p_ext, p2=k_flat, p3=-(p_ext+k_flat).
        # Looking at the V build in line 60: p1=p_ext, mk=-(p_ext+k). So V is V_3g(p, k, -(p+k)).
        V = _build_V3g_chunk(p_ext, k_chunk, -(p_ext + k_chunk))
        # Second vertex V_3g(-p, -k, p+k):
        V2 = _build_V3g_chunk(-p_ext, -k_chunk, p_ext + k_chunk)
        VV = np.einsum('kmab,knab->kmn', V, V2)
        
        khat2_sum = ((2*np.sin(k_chunk/2))**2).sum(axis=-1)
        pkhat2_sum = ((2*np.sin((p_ext + k_chunk)/2))**2).sum(axis=-1)
        if m_reg is not None:
            D_k = 1.0 / (khat2_sum + m_reg**2)
            D_pk = 1.0 / (pkhat2_sum + m_reg**2)
        else:
            D_k = np.where(khat2_sum > 1e-12, 1.0/khat2_sum, 0.0)
            D_pk = np.where(pkhat2_sum > 1e-12, 1.0/pkhat2_sum, 0.0)
        weight = D_k * D_pk * vol
        Sigma += 0.5 * np.einsum('k,kmn->mn', weight, VV)
    return Sigma


def ghost_standard_qcd_streaming(N, p_ext, m_reg=None, batch_size=None):
    """Memory-efficient ghost with standard 1/k̂² propagator."""
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    Npts = N**4
    if batch_size is None:
        batch_size = min(50000, max(1000, Npts // 64))
    
    Sigma_gh = np.zeros((4, 4), dtype=float)
    for start in range(0, Npts, batch_size):
        end = min(start + batch_size, Npts)
        flat_idx = np.arange(start, end)
        i0 = flat_idx // (N**3); i1 = (flat_idx // (N**2)) % N
        i2 = (flat_idx // N) % N; i3 = flat_idx % N
        k_chunk = np.stack([
            idx_shifted[i0], idx_shifted[i1], idx_shifted[i2], idx_shifted[i3],
        ], axis=-1).astype(float) * dk
        
        khat = 2*np.sin(k_chunk/2)
        pkhat = 2*np.sin((p_ext + k_chunk)/2)
        khat2_sum = (khat**2).sum(axis=-1)
        pkhat2_sum = (pkhat**2).sum(axis=-1)
        if m_reg is not None:
            D_k = 1.0 / (khat2_sum + m_reg**2)
            D_pk = 1.0 / (pkhat2_sum + m_reg**2)
        else:
            D_k = np.where(khat2_sum > 1e-12, 1.0/khat2_sum, 0.0)
            D_pk = np.where(pkhat2_sum > 1e-12, 1.0/pkhat2_sum, 0.0)
        weight = D_k * D_pk
        Sigma_gh += np.einsum('km,kn,k->mn', khat, pkhat, weight) * vol
    return Sigma_gh


def compute_Pi_T_qcd_streaming(N, m_reg, batch_size=None):
    """Streaming version of compute_Pi_T_qcd."""
    kappa = 2*np.pi / N
    p_ext = kappa * np.array([1, 0, 0, 0])
    Sigma_b = bubble_standard_qcd_streaming(N, p_ext, m_reg=m_reg, batch_size=batch_size)
    Sigma_g = ghost_standard_qcd_streaming(N, p_ext, m_reg=m_reg, batch_size=batch_size)
    Sigma = Sigma_b + Sigma_g
    p_0 = p_ext[0]
    p2_lat = (2*np.sin(p_0/2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    Pi_T_bub = (Sigma_b[1, 1] - Sigma_b[0, 0]) / p2_lat
    Pi_T_gh = (Sigma_g[1, 1] - Sigma_g[0, 0]) / p2_lat
    return Pi_T, Pi_T_bub, Pi_T_gh
