"""
qcd_crosscheck.py — Validate the bubble+ghost machinery against standard QCD.

In standard QCD with Feynman gauge, the gluon self-energy at 1-loop from
bubble (gluon-bubble from 3-gluon) + tadpole (4-gluon tadpole) + ghost gives:

    Π_T(p²) = -(b_0/16π²) · g² · C_2 · log(Λ²/p²)  + finite  + counter-terms

where b_0 = 11/3 is the pure-YM 1-loop β coefficient. On the lattice with
cutoff Λ ~ π and IR regulator m (fermion mass or similar), we have:

    Π_T(p² → 0) ≈ -(11/3)/(16π²) · C_2 · log(π²/m²) + ...

at m=0.05:  log(π²/m²) = log(9.87/0.0025) = log(3948) ≈ 8.28
            Π_T_expected ≈ -(11/3)/(16π²) · 8.28 ≈ -0.232 · 8.28 ≈ -1.92

So I should find Π_T ≈ -2 per C_2 in my bubble+ghost code with STANDARD 1/k̂²
propagator (no Π_s).

If this works, the methodology is good and the remaining work is to bridge
conventions between my induced-theory number and paper's A·B.

Caveat: on lattice, the "log" term has a specific constant offset and
possibly different Λ conventions. We expect the SIGN and approximate magnitude
to match textbook, but not the precise coefficient to 3 decimals.
"""
import numpy as np
import os, sys, time, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from yang_mills_lattice import V_3g_ym


def build_V3g_at_external_p_v2(N, p_ext):
    """Build V_3g(p_ext, k, -p_ext-k)^{μαβ} for all k on N^4 grid."""
    dk = 2*np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    Npts = k_flat.shape[0]

    V = np.zeros((Npts, 4, 4, 4), dtype=float)
    mk = -(p_ext[np.newaxis, :] + k_flat)
    p1 = p_ext
    p1h = 2*np.sin(p1/2); p2h = 2*np.sin(k_flat/2); p3h = 2*np.sin(mk/2)
    cos1h = np.cos(p1/2); cos2h = np.cos(k_flat/2); cos3h = np.cos(mk/2)

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
    return V, k_flat


def bubble_standard_qcd(N, p_ext, m_reg=None):
    """Bubble with STANDARD 1/k̂² propagator (no Π_s) and IR regulator m_reg.
    
    m_reg: a small mass added to the denominator to regulate IR. 
    If None, just use 1/k̂² and rely on finite-lattice for regulator.
    """
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    V, k_flat = build_V3g_at_external_p_v2(N, p_ext)
    Npts = V.shape[0]
    # Second vertex V_3g(-p_ext, -k, p_ext+k)
    V2 = np.zeros_like(V)
    mk = -k_flat
    p3 = p_ext[np.newaxis, :] + k_flat
    p1 = -p_ext
    p1h = 2*np.sin(p1/2); p2h = 2*np.sin(mk/2); p3h = 2*np.sin(p3/2)
    cos1h = np.cos(p1/2); cos2h = np.cos(mk/2); cos3h = np.cos(p3/2)
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
                V2[:, mu, al, be] = val
    # Standard propagators
    khat2 = (2*np.sin(k_flat/2))**2
    khat2_sum = khat2.sum(axis=-1)
    pkh = p_ext + k_flat
    pkhat2 = (2*np.sin(pkh/2))**2
    pkhat2_sum = pkhat2.sum(axis=-1)
    
    if m_reg is not None:
        D_k = 1.0 / (khat2_sum + m_reg**2)
        D_pk = 1.0 / (pkhat2_sum + m_reg**2)
    else:
        D_k = np.where(khat2_sum > 1e-12, 1.0/khat2_sum, 0.0)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0/pkhat2_sum, 0.0)
    
    VV = np.einsum('kmab,knab->kmn', V, V2)
    weight = D_k * D_pk * vol
    Sigma = 0.5 * np.einsum('k,kmn->mn', weight, VV)
    return Sigma


def ghost_standard_qcd(N, p_ext, m_reg=None):
    """Standard ghost bubble with 1/k̂² propagators."""
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    khat = 2*np.sin(k_flat/2)
    pk = p_ext[np.newaxis, :] + k_flat
    pkhat = 2*np.sin(pk/2)
    khat2_sum = (khat**2).sum(axis=-1)
    pkhat2_sum = (pkhat**2).sum(axis=-1)
    if m_reg is not None:
        D_k = 1.0 / (khat2_sum + m_reg**2)
        D_pk = 1.0 / (pkhat2_sum + m_reg**2)
    else:
        D_k = np.where(khat2_sum > 1e-12, 1.0/khat2_sum, 0.0)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0/pkhat2_sum, 0.0)
    integrand = khat[:, :, np.newaxis] * pkhat[:, np.newaxis, :] * (D_k * D_pk)[:, np.newaxis, np.newaxis]
    Sigma_gh = integrand.sum(axis=0) * vol
    return Sigma_gh


def compute_Pi_T_qcd(N, m_reg):
    """Extract Π_T from bubble+ghost at smallest lattice p."""
    kappa = 2*np.pi / N
    p_ext = kappa * np.array([1, 0, 0, 0])  # minimum lattice p
    Sigma_b = bubble_standard_qcd(N, p_ext, m_reg=m_reg)
    Sigma_g = ghost_standard_qcd(N, p_ext, m_reg=m_reg)
    Sigma = Sigma_b + Sigma_g
    p_0 = p_ext[0]
    p2_lat = (2*np.sin(p_0/2))**2
    Pi_T = (Sigma[1, 1] - Sigma[0, 0]) / p2_lat
    Pi_T_bub = (Sigma_b[1, 1] - Sigma_b[0, 0]) / p2_lat
    Pi_T_gh = (Sigma_g[1, 1] - Sigma_g[0, 0]) / p2_lat
    return Pi_T, Pi_T_bub, Pi_T_gh


if __name__ == "__main__":
    print("=== QCD cross-check: bubble + ghost with standard 1/k̂² propagator ===\n")
    print("Expected: Π_T ≈ -(11/3)/(16π²) · log(π²/m²) ≈ -0.232 · log(3948/m²_factor)")
    print()
    # At various regulator masses m_reg, compute Π_T and compare
    print(f"{'N':>4}  {'m_reg':>8}  {'Π_T_bub':>10}  {'Π_T_gh':>10}  {'Π_T_sum':>10}  {'expected':>10}  {'ratio':>8}")
    for N in [8, 12, 16, 20]:
        for m_reg in [0.1, 0.05, 0.02]:
            t0 = time.time()
            Pi_T, Pi_T_bub, Pi_T_gh = compute_Pi_T_qcd(N, m_reg)
            dt = time.time() - t0
            # Textbook expected (schematic):
            log_factor = np.log(np.pi**2 / m_reg**2)
            Pi_T_exp = -(11/3) / (16*np.pi**2) * log_factor
            ratio = Pi_T / Pi_T_exp if abs(Pi_T_exp) > 1e-10 else np.nan
            print(f"{N:>4}  {m_reg:>8.3f}  {Pi_T_bub:+10.4f}  {Pi_T_gh:+10.4f}  {Pi_T:+10.4f}  {Pi_T_exp:+10.4f}  {ratio:>8.3f}  [{dt:.1f}s]", flush=True)
        print()
