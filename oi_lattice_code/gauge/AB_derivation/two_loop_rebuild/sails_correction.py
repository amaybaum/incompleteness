"""
sails_correction.py — Sails (crossed-gluon) topology contribution to the
2-loop gauge self-energy.

Topology: fermion loop with 4 vertices in cyclic order E1(μ), I1(α),
E2(μ), I2(α). The internal gauge line "crosses" between external legs.

Integrand:
  δΠ^sails_μ(p=0) = -∫∫ cos(q_μ) cos((q+k)_μ) · Σ_α cos²((q+k/2)_α)
                       · Tr[γ_μ N(q) γ_α N(q+k) γ_μ N(q+k) γ_α N(q)]
                       / (D(q)² D(q+k)² k̂² Π_s)

Cost: O(N^8). Uses explicit 4x4 γ matrices for the 8-γ Dirac trace.
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


def setup_gamma_matrices():
    """4d Euclidean γ matrices satisfying {γ_μ, γ_ν} = 2 δ_{μν}.
    
    Representation: σ_x ⊗ σ_x,y,z and σ_y ⊗ 𝟙.
    Returns: (4, 4, 4) complex array — gamma[mu] is 4x4 Dirac matrix.
    """
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    
    gamma = np.zeros((4, 4, 4), dtype=complex)
    gamma[0] = np.kron(sx, sx)
    gamma[1] = np.kron(sx, sy)
    gamma[2] = np.kron(sx, sz)
    gamma[3] = np.kron(sy, I2)
    
    # Verify anticommutation {γ_μ, γ_ν} = 2 δ_{μν}
    for mu in range(4):
        for nu in range(4):
            anti = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            expected = 2 * (1 if mu == nu else 0) * np.eye(4, dtype=complex)
            assert np.allclose(anti, expected), f"γ_{mu}, γ_{nu} anticomm failed"
    
    return gamma


def compute_N_matrix_batch(s_values, m):
    """Compute N = iγ·s + m as 4x4 matrix for a batch of 4-vectors s.
    
    s_values: (..., 4) array of 4-vectors
    Returns: (..., 4, 4) complex array of 4x4 matrices.
    """
    gamma = setup_gamma_matrices()
    # i γ·s = i Σ_a s_a γ_a
    # shape broadcasts: s_values (..., 4) × gamma (4, 4, 4) → (..., 4, 4)
    igs = 1j * np.einsum('...a,aij->...ij', s_values, gamma)
    # Add m·𝟙
    I4 = np.eye(4, dtype=complex)
    shape = s_values.shape[:-1] + (4, 4)
    m_id = m * np.broadcast_to(I4, shape)
    return igs + m_id


def compute_sails(N, m, pi_s_val=None):
    """Full sails contribution δΠ^sails summed over μ, averaged over (q, k)."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    
    gamma = setup_gamma_matrices()
    
    q_grid = build_grid(N)  # (N, N, N, N, 4)
    k_grid = build_grid(N)  # (N, N, N, N, 4)
    
    # Precompute k-dependent quantities
    k_flat = k_grid.reshape(-1, 4)  # (N^4, 4)
    N_k = k_flat.shape[0]
    khat2 = ((2 * np.sin(k_flat / 2)) ** 2).sum(axis=-1)  # (N^4,)
    mask_k = khat2 > 1e-10
    khat2_safe = np.where(mask_k, khat2, 1.0)
    
    total = 0.0
    q_flat = q_grid.reshape(-1, 4)
    N_q_pts = q_flat.shape[0]
    
    print(f"  [Outer q-loop: {N_q_pts} points; inner k batched: {N_k} points per q]", flush=True)
    print(f"  [Total N^8 = {N_q_pts * N_k:,}]", flush=True)
    
    # Precompute N(q) for all q — used as outer fermion propagator
    sq_all = np.sin(q_grid)
    N_q_all = compute_N_matrix_batch(sq_all, m)  # (N, N, N, N, 4, 4)
    N_q_flat = N_q_all.reshape(-1, 4, 4)  # (N^4, 4, 4)
    
    D_q_all = (sq_all ** 2).sum(axis=-1) + m ** 2  # (N, N, N, N)
    D_q_flat = D_q_all.reshape(-1)
    mask_q = D_q_flat > 1e-10
    D_q_safe_flat = np.where(mask_q, D_q_flat, 1.0)
    
    cosq_flat = np.cos(q_flat)  # (N^4, 4) = cos(q_μ) for each μ
    
    t_start = time.time()
    report_every = max(1, N_q_pts // 10)
    
    for iq in range(N_q_pts):
        if iq > 0 and iq % report_every == 0:
            elapsed = time.time() - t_start
            frac = iq / N_q_pts
            total_est = elapsed / frac
            remaining = total_est - elapsed
            print(f"    q={iq}/{N_q_pts} ({100*frac:.0f}%), elapsed {elapsed:.0f}s, "
                  f"est remaining {remaining:.0f}s", flush=True)
        
        if not mask_q[iq]:
            continue
        
        q = q_flat[iq]
        N_q = N_q_flat[iq]  # (4, 4)
        D_q = D_q_safe_flat[iq]
        
        # q+k for all k (vectorized)
        qpk = q[None, :] + k_flat  # (N^4, 4)
        sqpk = np.sin(qpk)  # (N^4, 4)
        D_qpk = (sqpk ** 2).sum(axis=-1) + m ** 2  # (N^4,)
        mask_qpk = D_qpk > 1e-10
        D_qpk_safe = np.where(mask_qpk, D_qpk, 1.0)
        
        # N(q+k) batch: (N^4, 4, 4)
        N_qpk = compute_N_matrix_batch(sqpk, m)
        
        # Vertex factor cos((q+k)_μ) for all μ: (N^4, 4)
        cos_qpk = np.cos(qpk)  # (N^4, 4)
        
        # Vertex factor cos²((q + k/2)_α): (N^4, 4)
        cos_half = np.cos(q[None, :] + k_flat / 2)  # (N^4, 4)
        cos_half_sq = cos_half ** 2
        
        # Overall denominator: 1 / (D_q² D_qpk² k̂² Π_s)
        mask_all = mask_qpk & mask_k
        denom_safe = D_q ** 2 * D_qpk_safe ** 2 * khat2_safe * pi_s_val
        inv_denom = np.where(mask_all, 1.0 / denom_safe, 0.0)  # (N^4,)
        
        # Loop over μ, α (4x4 = 16 combinations)
        for mu in range(4):
            gamma_mu = gamma[mu]  # (4, 4)
            cosq_mu = cosq_flat[iq, mu]
            cos_qpk_mu = cos_qpk[:, mu]  # (N^4,)
            
            for alpha in range(4):
                gamma_alpha = gamma[alpha]  # (4, 4)
                cos_half_sq_alpha = cos_half_sq[:, alpha]  # (N^4,)
                
                # Build: γ_μ N γ_α N' γ_μ N' γ_α N for each k
                # Step 1: A = γ_μ @ N_q @ γ_α ← (4, 4) constant
                A = gamma_mu @ N_q @ gamma_alpha
                # Step 2: B = A @ N_qpk for each k ← (N^4, 4, 4)
                B = np.einsum('ij,kjl->kil', A, N_qpk)
                # Step 3: C = B @ γ_μ ← (N^4, 4, 4)
                C = np.einsum('kij,jl->kil', B, gamma_mu)
                # Step 4: D = C @ N_qpk ← (N^4, 4, 4)
                D_mat = np.einsum('kij,kjl->kil', C, N_qpk)
                # Step 5: E = D @ γ_α @ N_q ← (N^4, 4, 4) 
                # γ_α @ N_q is (4, 4) constant
                ga_Nq = gamma_alpha @ N_q  # (4, 4)
                E = np.einsum('kij,jl->kil', D_mat, ga_Nq)
                # Trace: (N^4,)
                trace = np.einsum('kii->k', E)
                # Trace must be real — take real part
                trace_real = np.real(trace)
                
                # Weight by vertex factors and denominators
                weight = cosq_mu * cos_qpk_mu * cos_half_sq_alpha * inv_denom
                contrib = (trace_real * weight).mean()  # mean over k
                total += contrib
    
    # Average over q (we summed q but haven't averaged)
    total /= N_q_pts
    
    return total


def main():
    print("=" * 72)
    print("Sails / crossed-gluon topology")
    print("=" * 72)
    print()
    print("Formula: δΠ^sails = -∫∫ cos(q_μ) cos((q+k)_μ) Σ_α cos²((q+k/2)_α)")
    print("                        · Tr[γ_μ N(q) γ_α N(q+k) γ_μ N(q+k) γ_α N(q)]")
    print("                        / (D(q)² D(q+k)² k̂² Π_s)")
    print()
    print("Computed with explicit 4x4 γ matrices (Hermitian Euclidean rep).")
    print()

    # Start with N=4 for correctness, then scale up
    for N, m in [(4, 0.05), (6, 0.05)]:
        print(f"--- N = {N}, m = {m} ---")
        t0 = time.time()
        pi_s = compute_pi_s(N, m)
        print(f"  Π_s = {pi_s:.4f}")
        val = compute_sails(N, m, pi_s)
        dt = time.time() - t0
        print(f"  Sails contribution (raw, summed over μ): {val:+.5e}")
        print(f"  [total {dt:.1f}s]")
        print()


if __name__ == "__main__":
    main()
