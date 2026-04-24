"""
seagull_SE_insertion.py — Path B, Step 4: scalar + vector SE insertions
on the SEAGULL topology (not bubble).

Derivations in PATH_B_STEP_4.md. Formulas at p=0:

  Scalar: δ(seagull)^S(q, μ) = -8m · cos²(q_μ) · s_μ²/D² · Σ_f^S(q)
  Vector: δ(seagull)^V(q, μ) = -4·cos²(q_μ)/D² · [D v_μ s_μ - 2(v·s_q) s_μ²]

Where:
  Σ_f^S(q) = m · Σ_ν ⟨cos²(q_ν + p_ν/2) / (D' p̂² Π_s)⟩_p
  v_α(q)   = 2 J^c(α, α; q) - Σ_ν J^c(α, ν; q)

Reuses v_α(q) computation from vector_SE_insertion.py.
"""
import numpy as np
import os
import sys
import warnings
import time

warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from vector_SE_insertion import build_grid, compute_vector_v


def compute_scalar_Sigma_f(N, m, pi_s_val=None):
    """Compute Σ_f^S(q) = m · Σ_ν ⟨cos²(q_ν + p_ν/2) / (D' p̂² Π_s)⟩_p
    for all q on N^4 lattice.
    
    Returns: (N, N, N, N) scalar array.
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    
    q_grid = build_grid(N)
    p_grid = build_grid(N)
    
    phat2 = ((2 * np.sin(p_grid / 2)) ** 2).sum(axis=-1)
    phat2_Pi_s = phat2 * pi_s_val
    
    Sigma_S = np.zeros(q_grid.shape[:-1])  # (N,N,N,N)
    q_flat = q_grid.reshape(-1, 4)
    
    for iq, q in enumerate(q_flat):
        qp = q[None, None, None, None, :] + p_grid
        sqp = np.sin(qp)
        D_qp = (sqp ** 2).sum(axis=-1) + m ** 2
        
        mask = phat2 > 1e-10
        base = np.where(mask, 1.0 / (D_qp * phat2_Pi_s), 0.0)
        
        # cos²(q_ν + p_ν/2) for each ν, summed
        cos2 = np.cos(q[None,None,None,None,:] + p_grid/2) ** 2  # (N,N,N,N,4)
        cos2_sum = cos2.sum(axis=-1)  # sum over ν
        
        integrand = cos2_sum * base
        Sigma_S_q = m * integrand.mean()
        
        iq_multi = np.unravel_index(iq, (N, N, N, N))
        Sigma_S[iq_multi] = Sigma_S_q
    
    return Sigma_S


def compute_seagull_SE_scalar(N, m, pi_s_val=None, Sigma_S=None):
    """δ(seagull)^S contribution at p=0: ∫ -8m cos²(q_μ) s_μ²/D² · Σ^S(q) dq."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    if Sigma_S is None:
        print("  [computing Σ_f^S ...]", flush=True)
        t0 = time.time()
        Sigma_S = compute_scalar_Sigma_f(N, m, pi_s_val)
        print(f"  [Σ_f^S done in {time.time()-t0:.1f}s]", flush=True)
    
    q_grid = build_grid(N)
    sq = np.sin(q_grid)
    D_q = (sq ** 2).sum(axis=-1) + m ** 2
    mask = D_q > 1e-10
    D_q_safe = np.where(mask, D_q, 1.0)
    
    total = 0.0
    for mu in range(4):
        cos2_qmu = np.cos(q_grid[..., mu]) ** 2
        sqmu_sq = sq[..., mu] ** 2
        integrand = -8.0 * m * cos2_qmu * sqmu_sq / (D_q_safe ** 2) * Sigma_S
        total += (integrand * mask).mean()
    
    return total


def compute_seagull_SE_vector(N, m, pi_s_val=None, v=None):
    """δ(seagull)^V contribution at p=0: ∫ -4 cos²(q_μ)/D² · [D v_μ s_μ - 2(v·s) s_μ²] dq."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    if v is None:
        print("  [computing v_α(q) ...]", flush=True)
        t0 = time.time()
        v = compute_vector_v(N, m, pi_s_val)
        print(f"  [v done in {time.time()-t0:.1f}s]", flush=True)
    
    q_grid = build_grid(N)
    sq = np.sin(q_grid)
    D_q = (sq ** 2).sum(axis=-1) + m ** 2
    mask = D_q > 1e-10
    D_q_safe = np.where(mask, D_q, 1.0)
    v_dot_sq = (v * sq).sum(axis=-1)
    
    total = 0.0
    for mu in range(4):
        cos2_qmu = np.cos(q_grid[..., mu]) ** 2
        sqmu = sq[..., mu]
        v_mu = v[..., mu]
        
        bracket = D_q * v_mu * sqmu - 2 * v_dot_sq * sqmu ** 2
        integrand = -4.0 * cos2_qmu / (D_q_safe ** 2) * bracket * mask
        total += integrand.mean()
    
    return total


def main():
    print("=" * 72)
    print("Path B Step 4: Seagull SE insertion (scalar + vector)")
    print("=" * 72)
    print()
    print("Formulas:")
    print("  δ(seagull)^S = -8m cos²(q_μ) s_μ²/D² · Σ_f^S(q)")
    print("  δ(seagull)^V = -4 cos²(q_μ)/D² · [D v_μ s_μ - 2(v·s) s_μ²]")
    print()
    
    for N, m in [(6, 0.05), (6, 0.10), (8, 0.05), (8, 0.10)]:
        print(f"--- N = {N}, m = {m} ---")
        t0 = time.time()
        pi_s = compute_pi_s(N, m)
        print(f"  Π_s = {pi_s:.4f}")
        
        Sigma_S = compute_scalar_Sigma_f(N, m, pi_s)
        v = compute_vector_v(N, m, pi_s)
        
        sc = compute_seagull_SE_scalar(N, m, pi_s, Sigma_S=Sigma_S)
        vc = compute_seagull_SE_vector(N, m, pi_s, v=v)
        
        dt = time.time() - t0
        print(f"  δ(seagull)^S raw = {sc:+.5e}")
        print(f"  δ(seagull)^V raw = {vc:+.5e}")
        print(f"  [total {dt:.1f}s]")
        print()


if __name__ == "__main__":
    main()
