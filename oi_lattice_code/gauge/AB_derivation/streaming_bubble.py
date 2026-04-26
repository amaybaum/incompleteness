"""
Memory-efficient OI gauge bubble at finite external momentum.

Streams the loop momentum k in chunks of `batch_size` lattice points
to keep peak memory bounded by O(batch_size × 64) rather than
O(N⁴ × 64). Functionally equivalent to the full materialized
computation; kept separate for clarity and so callers can pick the
implementation appropriate for their N.
"""
import numpy as np
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s


def _build_V3g_chunk(p_ext, k_chunk, mk_chunk):
    """Build V_3g(p_ext, k, mk)^{μ,α,β} for a chunk of (k, mk) pairs.
    
    Returns (chunk_size, 4, 4, 4) array.
    """
    chunk = k_chunk.shape[0]
    p1h = 2*np.sin(p_ext/2)             # (4,)
    p2h = 2*np.sin(k_chunk/2)           # (chunk, 4)
    p3h = 2*np.sin(mk_chunk/2)          # (chunk, 4)
    cos1h = np.cos(p_ext/2)             # (4,)
    cos2h = np.cos(k_chunk/2)           # (chunk, 4)
    cos3h = np.cos(mk_chunk/2)          # (chunk, 4)
    
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
    return V


def compute_bubble_at_p_streaming(N, m, p_ext, pi_s_val=None, batch_size=None):
    """Streaming version of compute_bubble_at_p.
    
    Returns (Sigma_munu, pi_s_val) where Sigma_munu is a 4x4 matrix.
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    
    # Generate the k-grid in shifted-BZ form (-π, π]
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    Npts = N**4
    
    if batch_size is None:
        # Choose batch to keep peak memory ~100 MB (allows for safety margin)
        batch_size = min(50000, max(1000, Npts // 64))
    
    # Accumulator for Σ^{μν}
    Sigma = np.zeros((4, 4), dtype=float)
    
    # Iterate over flat k index in batches
    for start in range(0, Npts, batch_size):
        end = min(start + batch_size, Npts)
        chunk_size = end - start
        
        # Generate this chunk's k_flat
        flat_idx = np.arange(start, end)
        # Convert flat to multi-index: i = i0 * N^3 + i1 * N^2 + i2 * N + i3
        i0 = flat_idx // (N**3)
        i1 = (flat_idx // (N**2)) % N
        i2 = (flat_idx // N) % N
        i3 = flat_idx % N
        # Map indices to shifted momenta
        k_chunk = np.stack([
            idx_shifted[i0],
            idx_shifted[i1],
            idx_shifted[i2],
            idx_shifted[i3],
        ], axis=-1).astype(float) * dk        # (chunk, 4)
        
        # Loop momenta: leg 2 = k, leg 3 = -(p_ext + k)
        mk_chunk = -(p_ext[np.newaxis, :] + k_chunk)
        
        # Build V at this chunk: V_3g(p_ext, k, mk)^{μαβ}
        V = _build_V3g_chunk(p_ext, k_chunk, mk_chunk)  # (chunk, 4, 4, 4)
        
        # Build V2: V_3g(-p_ext, -k, p_ext+k)^{ναβ}
        V2 = _build_V3g_chunk(-p_ext, -k_chunk, p_ext + k_chunk)  # (chunk, 4, 4, 4)
        
        # Contract α, β: VV^{kmn} = sum_{ab} V^{kmab} V2^{knab}
        VV = np.einsum('kmab,knab->kmn', V, V2)  # (chunk, 4, 4)
        
        # Propagators
        khat2 = (2*np.sin(k_chunk/2))**2
        khat2_sum = khat2.sum(axis=-1)
        D_k = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)
        
        pkh = p_ext + k_chunk
        pkhat2 = (2*np.sin(pkh/2))**2
        pkhat2_sum = pkhat2.sum(axis=-1)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / (pkhat2_sum * pi_s_val), 0.0)
        
        weight = D_k * D_pk * vol  # (chunk,)
        # Add this chunk's contribution: 0.5 * sum_k weight_k VV_k^{mn}
        Sigma += 0.5 * np.einsum('k,kmn->mn', weight, VV)
    
    return Sigma, pi_s_val
