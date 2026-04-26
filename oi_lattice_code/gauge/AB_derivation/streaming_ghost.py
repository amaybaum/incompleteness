"""
Streaming version of compute_ghost_sigma_at_p. Same memory pattern fix.
"""
import numpy as np
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s


def compute_ghost_sigma_streaming(N, p_ext, use_induced=False, pi_s_val=None, m=None, batch_size=None):
    """Memory-efficient ghost self-energy. Returns 4x4 matrix."""
    if use_induced and pi_s_val is None:
        if m is None:
            raise ValueError("Need m for induced ghost")
        pi_s_val = compute_pi_s(N, m)
    
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
        i0 = flat_idx // (N**3)
        i1 = (flat_idx // (N**2)) % N
        i2 = (flat_idx // N) % N
        i3 = flat_idx % N
        k_chunk = np.stack([
            idx_shifted[i0], idx_shifted[i1], idx_shifted[i2], idx_shifted[i3],
        ], axis=-1).astype(float) * dk
        
        khat = 2*np.sin(k_chunk/2)
        pk = p_ext[np.newaxis, :] + k_chunk
        pkhat = 2*np.sin(pk/2)
        
        khat2_sum = (khat**2).sum(axis=-1)
        pkhat2_sum = (pkhat**2).sum(axis=-1)
        
        if use_induced:
            D_k = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)
            D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / (pkhat2_sum * pi_s_val), 0.0)
        else:
            D_k = np.where(khat2_sum > 1e-12, 1.0 / khat2_sum, 0.0)
            D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / pkhat2_sum, 0.0)
        
        # integrand[k, μ, ν] = khat[k, μ] · pkhat[k, ν] · D_k[k] · D_pk[k]
        weight = D_k * D_pk  # (chunk,)
        # Use einsum to accumulate without materializing the full chunk integrand
        Sigma_gh += np.einsum('km,kn,k->mn', khat, pkhat, weight) * vol
    
    return Sigma_gh
