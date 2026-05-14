"""
bubble_at_finite_p.py — compute Σ^{μν}_bubble(p) at small nonzero p.

At p=0, Σ^{μν}(0) is the gauge-violating "gluon mass" quadratic divergence,
not a physical observable. The physically meaningful quantity is the transverse
part of Σ at small p:
    Σ^{μν}(p) = (δ^{μν} p² - p^μ p^ν) · Π_T(p²) + [longitudinal/mass]
    
Π_T(p²) at p²→0 gives the wavefunction renormalization contribution to 1/α.

We compute bubble only here (not the full gauge-invariant sum). Even the bubble
alone has a nonzero Π_T(p²) piece, and scanning a few p's lets us separate it
from the gauge-violating Σ(0).

Method:
1. Compute Σ^{μν}_bubble(p) for p = λ · p_ref with p_ref = (1,0,0,0)·κ.
2. Extract Σ^{00} (longitudinal with p in 0-direction) and Σ^{11} (transverse).
3. Expand: Σ^{00}(p) = Σ(0) + p² · A_L, Σ^{11}(p) = Σ(0) + p² · A_T.
4. A_T - A_L gives the transverse-minus-longitudinal piece, which is related to Π_T.
"""
import numpy as np
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from yang_mills_lattice import V_3g_ym


def build_V3g_at_external_p(N, p_ext):
    """Build V_3g(p_ext, k, -p_ext-k)^{μαβ} for all k on N^4 grid.
    
    Returns (Npts, 4, 4, 4) array: vertex kinematic at external momentum p_ext
    and loop momenta k, -p_ext-k.
    """
    dk = 2*np.pi / N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    Npts = k_flat.shape[0]
    
    # Loop momenta: p_2 = k, p_3 = -(p_ext + k)
    # Note: on the lattice, -(p_ext + k) must be mod-reduced to BZ (-π, π]
    # But our momentum variables are continuous (not indexed), so just compute as is.
    
    V = np.zeros((Npts, 4, 4, 4), dtype=float)
    mk = -(p_ext[np.newaxis, :] + k_flat)  # shape (Npts, 4)

    # Evaluate V_3g per-point: slower but clean. For N=16 this is 65k × 64 = 4M evals.
    # The V_3g_ym function is scalar; vectorize manually.
    # 
    # K_{3g}^{μ_1 μ_2 μ_3}(p_1, p_2, p_3) = 
    #   δ^{μ_1 μ_2} cos((p_3)_{μ_1}/2) · (p̂_1 - p̂_2)^{μ_3}
    # + δ^{μ_2 μ_3} cos((p_1)_{μ_2}/2) · (p̂_2 - p̂_3)^{μ_1}
    # + δ^{μ_3 μ_1} cos((p_2)_{μ_3}/2) · (p̂_3 - p̂_1)^{μ_2}
    p1 = p_ext  # shape (4,)
    p1h = 2*np.sin(p1/2)                          # (4,)
    p2h = 2*np.sin(k_flat/2)                      # (Npts, 4)
    p3h = 2*np.sin(mk/2)                          # (Npts, 4)
    cos1h = np.cos(p1/2)                          # (4,)
    cos2h = np.cos(k_flat/2)                      # (Npts, 4)
    cos3h = np.cos(mk/2)                          # (Npts, 4)

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


def compute_bubble_at_p(N, m, p_ext, pi_s_val=None):
    """Compute Σ^{μν}_bubble(p_ext) / C_2."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    
    V, k_flat = build_V3g_at_external_p(N, p_ext)
    Npts = V.shape[0]
    
    # Second vertex: V_3g(-p_ext, -k, p_ext+k)^{ναβ}
    # Build analogously — just flip signs of external momenta
    V2, _ = build_V3g_at_external_p(N, -p_ext)
    # Second vertex momenta are -k (on the opposite loop line) and (p_ext+k)
    # But my build_V3g_at_external_p only takes external p_ext, uses k_flat for loop
    # To get V(-p_ext, -k, p+k): need to build with flipped loop momenta too
    # 
    # Actually for the bubble, the vertices are related by Bose symmetry:
    # V_3g(-p, -k, p+k; ν, α, β) corresponds to swapping legs 2 and 3 of
    # V_3g(-p, p+k, -k; ν, β, α), and Bose antisymmetry says the latter = -V(-p, k, -p-k; ν, β, α)
    # 
    # Simpler: just rebuild with -p_ext and different loop variable
    # 
    # Actually the bubble has incoming external momenta p and -p. The second vertex
    # carries -p externally. The loop momenta entering the two vertices are (k, -p-k)
    # and (-k, p+k). Both vertices should have the same Bose structure.
    # 
    # For my code: V2 should be V_3g(-p, -k, p+k; ν, α, β). 
    # Using the SAME k_flat sign convention. Let me build explicitly.
    
    # Rebuild V2 directly:
    V2 = np.zeros((Npts, 4, 4, 4), dtype=float)
    p1_2 = -p_ext
    p2_2 = -k_flat   # loop momentum coming in with - sign
    p3_2 = p_ext[np.newaxis, :] + k_flat
    p1h_2 = 2*np.sin(p1_2/2)
    p2h_2 = 2*np.sin(p2_2/2)
    p3h_2 = 2*np.sin(p3_2/2)
    cos1h_2 = np.cos(p1_2/2)
    cos2h_2 = np.cos(p2_2/2)
    cos3h_2 = np.cos(p3_2/2)
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

    # Induced gauge propagators on loop lines at momenta k and (p+k)
    khat2 = (2*np.sin(k_flat/2))**2
    khat2_sum = khat2.sum(axis=-1)
    D_k = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)
    
    pkh = (p_ext + k_flat)
    pkhat2 = (2*np.sin(pkh/2))**2
    pkhat2_sum = pkhat2.sum(axis=-1)
    D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / (pkhat2_sum * pi_s_val), 0.0)
    
    # Feynman gauge: propagators scalar, contract α, β between V and V2:
    VV = np.einsum('kmab,knab->kmn', V, V2)  # (Npts, 4, 4)
    weight = D_k * D_pk * vol   # MISSING vol factor was a bug — fixed
    # Symmetry factor 1/2 for identical bosons in loop
    Sigma = 0.5 * np.einsum('k,kmn->mn', weight, VV)
    
    return Sigma, pi_s_val


if __name__ == "__main__":
    print("=== Bubble self-energy Σ^{μν}_bubble(p) scan at small p ===\n")
    m = 0.05
    
    for N in [8, 12]:
        kappa = 2*np.pi / N
        pi_s = compute_pi_s(N, m)
        print(f"\n--- N={N}, m={m}, Π_s={pi_s:.4f}, κ={kappa:.4f} ---")
        print(f"  Scan p_ext = λ · κ · ê_0 for λ = 0, 1, 2, 3")
        print(f"  {'λ':>3}  {'Σ^{00}':>14}  {'Σ^{11}':>14}  {'Σ^{01}':>14}")
        results = {}
        for lam in [0, 1, 2, 3]:
            p_ext = lam * kappa * np.array([1, 0, 0, 0])
            t0 = time.time()
            Sigma, _ = compute_bubble_at_p(N, m, p_ext, pi_s_val=pi_s)
            dt = time.time() - t0
            results[lam] = Sigma
            print(f"  {lam:>3}  {Sigma[0,0]:+.6e}  {Sigma[1,1]:+.6e}  {Sigma[0,1]:+.6e}  [{dt:.1f}s]", flush=True)
        
        # Extract: at p=λκ along x_0, the physical Σ structure:
        # Σ^{μν}(p) = (p² δ^{μν} - p^μ p^ν) Π_T(p²) + [gauge-violating mass term]
        # 
        # With p=(p_0, 0, 0, 0):
        # Σ^{00} = (p₀² · 1 - p₀²) Π_T + mass = 0·Π_T + mass = mass
        # Σ^{11} = (p₀² · 1 - 0) Π_T + mass = p₀² Π_T + mass
        # So: (Σ^{11}(p) - Σ^{00}(p)) / p² = Π_T(p²)  — clean extraction!
        
        print(f"\n  Transverse Π_T = [Σ^{{11}}(p) - Σ^{{00}}(p)] / p² at m={m}:")
        sig0 = results[0]
        for lam in [1, 2, 3]:
            sig = results[lam]
            p_0 = lam * kappa
            p2_lat = (2*np.sin(p_0/2))**2  # p̂² for p = (p_0, 0, 0, 0)
            diff_00 = sig[0, 0] - sig0[0, 0]
            diff_11 = sig[1, 1] - sig0[1, 1]
            # Use p̂² (lattice momentum squared), not continuum p²
            PiT = (sig[1, 1] - sig[0, 0]) / p2_lat
            PiT_pi2 = PiT * pi_s**2
            print(f"  λ={lam}  p_0={p_0:.4f}  p̂²={p2_lat:.5f}  Σ^{{11}}-Σ^{{00}}={sig[1,1]-sig[0,0]:+.4e}  Π_T·Π_s²={PiT_pi2:+.4e}")
