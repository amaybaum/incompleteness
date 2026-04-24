"""
vertex_correction.py — Path B, Step 5: 1-loop vertex correction contribution
to the 2-loop gauge self-energy.

Derivation in PATH_B_STEP_5.md. Corrected vertex at p=0:

  V^(1,1)_μ(q,q) = A_μ(q) · 𝟙 + Σ_α B_μ,α(q) · γ_α

with A, B computed as inner-k integrals. Then:

  δ(bubble)^vtx_μ(q) = 2·ig cos(q_μ)/D_q² · [8im s_{q,μ} A_μ + 4 D_q B_μ,μ - 8 s_{q,μ}(B_μ·s_q)]

Cost: O(N^8). At N=8 ~ 10-30s.
"""
import numpy as np
import os
import sys
import warnings
import time

warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from vector_SE_insertion import build_grid


def compute_vertex_correction_AB(N, m, mu_ext, pi_s_val=None):
    """Compute A_μ(q) and B_{μ,α}(q) for external Lorentz index mu_ext.
    
    Returns:
        A: (N,N,N,N) complex array (has factor i)
        B: (N,N,N,N,4) real array
    
    The integral is over inner loop momentum k.
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    
    q_grid = build_grid(N)
    k_grid = build_grid(N)
    
    khat2 = ((2 * np.sin(k_grid / 2)) ** 2).sum(axis=-1)
    mask_k = khat2 > 1e-10
    khat2_safe = np.where(mask_k, khat2, 1.0)
    
    # For each q, inner integral over k
    q_flat = q_grid.reshape(-1, 4)
    A_mu = np.zeros(q_grid.shape[:-1])  # Will store imag part (factor 2im)
    B_mu = np.zeros(q_grid.shape)       # (N,N,N,N,4) for α = 0,1,2,3
    
    for iq, q in enumerate(q_flat):
        # q - k (fermion internal momentum)
        q_minus_k = q[None,None,None,None,:] - k_grid
        s1 = np.sin(q_minus_k)
        s1_sq = s1 ** 2
        D1 = s1_sq.sum(axis=-1) + m ** 2
        mask_D = D1 > 1e-10
        D1_safe = np.where(mask_D, D1, 1.0)
        
        # cos factors
        # Inner vertices: cos((q - k/2)_ν) for ν = 0,1,2,3
        q_minus_k_half = q[None,None,None,None,:] - k_grid / 2
        cos_inner = np.cos(q_minus_k_half)  # (N,N,N,N,4)
        cos_inner_sq = cos_inner ** 2        # C_α(q,k) for each α
        C_sum = cos_inner_sq.sum(axis=-1)     # C(q,k) = Σ_ν cos²
        
        # Middle vertex: cos((q-k)_mu_ext)
        cos_mu = np.cos(q_minus_k[..., mu_ext])  # (N,N,N,N)
        
        # Common denominator factor
        denom = D1_safe ** 2 * khat2_safe * pi_s_val
        mask = mask_D & mask_k
        base_factor = np.where(mask, cos_mu / denom, 0.0)  # (N,N,N,N)
        
        # A_μ: coefficient of 𝟙
        # A_μ(q) = ⟨2m s_{1,μ} C(q,k) · base_factor⟩_k  (I dropped 'i' factor, track separately)
        s1_mu = s1[..., mu_ext]  # (N,N,N,N)
        A_val = (2 * m * s1_mu * C_sum * base_factor).mean()
        
        # B_{μ,μ}: coefficient of γ_μ (α = mu_ext)
        # [-4 s_{1,μ}² C_μ + 2 s_{1,μ}² C + 2 D_1 C_μ - D_1 C] · base_factor
        C_mu = cos_inner_sq[..., mu_ext]
        B_mu_bracket = (
            -4 * s1_mu ** 2 * C_mu 
            + 2 * s1_mu ** 2 * C_sum
            + 2 * D1 * C_mu
            - D1 * C_sum
        )
        B_mu_val = (B_mu_bracket * base_factor).mean()
        
        # B_{μ,α} for α ≠ μ
        B_alpha = np.zeros(4)
        B_alpha[mu_ext] = B_mu_val
        for alpha in range(4):
            if alpha == mu_ext:
                continue
            s1_alpha = s1[..., alpha]
            C_alpha = cos_inner_sq[..., alpha]
            bracket_alpha = (
                -4 * s1_mu * s1_alpha * C_alpha
                + 2 * s1_mu * s1_alpha * C_sum
            )
            B_alpha[alpha] = (bracket_alpha * base_factor).mean()
        
        iq_multi = np.unravel_index(iq, (N, N, N, N))
        A_mu[iq_multi] = A_val  # Store the REAL scalar coefficient (i factor tracked later)
        B_mu[iq_multi[0], iq_multi[1], iq_multi[2], iq_multi[3], :] = B_alpha
    
    return A_mu, B_mu


def compute_vertex_correction_contribution(N, m, pi_s_val=None):
    """Full δ(bubble)^vtx contribution summed over μ, integrated over q."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    
    q_grid = build_grid(N)
    sq = np.sin(q_grid)
    D_q = (sq ** 2).sum(axis=-1) + m ** 2
    mask = D_q > 1e-10
    D_q_safe = np.where(mask, D_q, 1.0)
    
    total = 0.0
    for mu_ext in range(4):
        print(f"  computing μ={mu_ext} ...", flush=True)
        t0 = time.time()
        A_mu, B_mu = compute_vertex_correction_AB(N, m, mu_ext, pi_s_val)
        print(f"    AB loop {time.time()-t0:.1f}s", flush=True)
        
        cos2_qmu = np.cos(q_grid[..., mu_ext]) ** 2
        sqmu = sq[..., mu_ext]
        B_dot_sq = (B_mu * sq).sum(axis=-1)  # (N,N,N,N)
        B_mu_mu = B_mu[..., mu_ext]
        
        # Trace formula:
        #  Tr[V^(1,1) S γ_μ S] = [8im s_{q,μ} A + 4 D_q B_{μ,μ} - 8 s_{q,μ}(B·s_q)] / D_q²
        # The factor 8im · A has 'i' — when combined with ig outside and cos(q_μ):
        #   2 · ig cos(q_μ) · 8im s_{q,μ} A_μ / D_q² → -16 g m · cos(q_μ) s_{q,μ} A_μ / D_q²
        # Rest (real-valued):
        #   2 · ig cos(q_μ) · (4 D_q B_μ,μ - 8 s_{q,μ} B·s_q) / D_q²
        # The 'i' from outside ig gets absorbed into the overall sign in Euclidean conversion.
        # For comparison with bubble-V and seagull-V which were "raw" (with 'i' stripped
        # via same conversion), I'll track the REAL piece.
        
        # Real piece (B coefficient) — comparable to bubble/seagull real parts:
        # 2 · cos(q_μ) · cos(q_μ) · (4 D_q B_μ,μ - 8 s_{q,μ} B·s_q) / D_q²
        # where the outer cos(q_μ) comes from the outer bubble's SECOND vertex factor.
        # But session p/q code had cos²(q_μ) baked into the bubble structure.
        # For the vertex-corrected bubble, one vertex is V^(1,1) (already has its cos
        # in the A, B integrals) and the other is tree-level (with its cos(q_μ)).
        # So the outer factor is cos(q_μ), not cos²(q_μ).
        
        # Real-valued integrand (the 8im A piece is purely mass-like, I'll track it
        # separately below):
        real_bracket = 4 * D_q * B_mu_mu - 8 * sqmu * B_dot_sq
        integrand_real = 2 * np.cos(q_grid[..., mu_ext]) * real_bracket / (D_q_safe ** 2) * mask
        
        # Imaginary-paired mass-like piece (from A):
        mass_bracket = -16 * m * np.cos(q_grid[..., mu_ext]) * sqmu * A_mu
        integrand_mass = mass_bracket / (D_q_safe ** 2) * mask
        
        contrib_real = integrand_real.mean()
        contrib_mass = integrand_mass.mean()
        
        print(f"    μ={mu_ext}: real part = {contrib_real:+.5e}, mass part = {contrib_mass:+.5e}")
        total += contrib_real + contrib_mass
    
    return total


def main():
    print("=" * 72)
    print("Path B Step 5: Vertex correction numerical test")
    print("=" * 72)
    print()
    print("Ward-identity prediction: vertex ≈ -(bubble-SE + seagull-SE)")
    print("Bubble+seagull vector at N=8, m=0.05: -0.183")
    print("Expected vertex at N=8, m=0.05: ~ +0.18 (opposite sign)")
    print()
    
    for N, m in [(6, 0.05), (8, 0.05)]:
        print(f"--- N = {N}, m = {m} ---")
        t0 = time.time()
        pi_s = compute_pi_s(N, m)
        print(f"  Π_s = {pi_s:.4f}")
        val = compute_vertex_correction_contribution(N, m, pi_s)
        dt = time.time() - t0
        print(f"  TOTAL vertex correction: {val:+.5e}")
        print(f"  [total {dt:.1f}s]")
        print()


if __name__ == "__main__":
    main()
