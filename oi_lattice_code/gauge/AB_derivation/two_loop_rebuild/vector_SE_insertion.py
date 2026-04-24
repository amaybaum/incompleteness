"""
vector_SE_insertion.py — Vector Σ_f^V SE insertion contribution at p=0.

Formula:

  v_α(q) = Σ_ν ⟨cos²(q_ν+p_ν/2) · (2 s'_ν δ_{να} - s'_α) / (D' p̂² Π_s)⟩_p
         = 2 J^c(α, α; q) - Σ_ν J^c(α, ν; q)

  where J^c(α, β; q) = ⟨cos²(q_β+p_β/2) · sin(q+p)_α / (D(q+p) p̂² Π_s)⟩_p

Then:
  δ(bubble)^V_μ(q, 0) = (8i cos²(q_μ)/D_q³) · [(v·s_q)(D_q - 4s_{q,μ}²)
                                                + 2 D_q v_μ s_{q,μ}]

Integrating over q and summing over μ gives the contribution to
Σ_gauge(p=0), which (up to overall factors) gives δ_0^(SE,V).

Computational cost: O(N^8) (double loop, N^4 inner × N^4 outer).
"""
import numpy as np
import os
import sys
import warnings
import time

warnings.filterwarnings('ignore')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s


def build_grid(N):
    """Symmetric BZ grid: (N, N, N, N, 4) array of 4-momentum values."""
    dk = 2 * np.pi / N
    idx = np.arange(N)
    shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(shifted, shifted, shifted, shifted, indexing='ij')
    return np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)


def compute_vector_v(N, m, pi_s_val=None):
    """Compute v_α(q) for all q on N^4 lattice.

    Returns: (N, N, N, N, 4) array where [i, j, k, l, α] = v_α(q).
    
    Cost: O(N^8). At N=6: 1.7M ops. At N=8: 16M ops.
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)

    q_grid = build_grid(N)  # (N,N,N,N,4)
    p_grid = build_grid(N)  # (N,N,N,N,4)

    # Precompute p-dependent factors
    phat2 = ((2 * np.sin(p_grid / 2)) ** 2).sum(axis=-1)  # (N,N,N,N)
    phat2_Pi_s = phat2 * pi_s_val

    # For each q, compute v_α
    v = np.zeros(q_grid.shape)  # (N,N,N,N,4)

    # Flatten q for looping
    q_flat = q_grid.reshape(-1, 4)  # (N^4, 4)

    for iq, q in enumerate(q_flat):
        qp = q[None, None, None, None, :] + p_grid  # (N,N,N,N,4)

        sqp = np.sin(qp)      # sin(q+p)_α for each α (N,N,N,N,4)
        # Vertex factor: cos²(q_ν + p_ν/2)  (argument is q_ν + p_ν/2,
        # not (q_ν + p_ν)/2 — the momentum at the gluon vertex is the
        # average of incoming and outgoing fermion momenta.)
        cos2_q_plus_p_half = np.cos(q[None,None,None,None,:] + p_grid / 2) ** 2
        # (N,N,N,N,4) — last index is ν

        D_qp = (sqp ** 2).sum(axis=-1) + m ** 2  # (N,N,N,N)

        # For each α, compute J^c(α, β=ν; q) = ⟨cos²(q_ν+p_ν/2) · s'_α / (D' p̂² Π_s)⟩
        # J^c has TWO indices: α (where sin goes) and ν (where cos² goes)

        # mask k=0 singularity
        mask = phat2 > 1e-10
        safe_phat2_Pi_s = np.where(mask, phat2_Pi_s, 1.0)  # dummy for division
        base = np.where(mask, 1.0 / (D_qp * safe_phat2_Pi_s), 0.0)  # (N,N,N,N)

        # Now: J^c(α, ν; q) = mean over p of [cos²(q_ν+p_ν/2) · s'_α · base]
        # We can compute for all (α, ν) pairs via broadcasting:
        #   cos²[..., ν] * s'[..., α] · base[...]
        # Let me compute:
        # integrand_{α, ν} = cos2_q_plus_p_half[..., ν] * sqp[..., α] * base
        # Then J^c[α, ν] = mean of integrand over p.

        # Shape: cos2_q_plus_p_half is (N,N,N,N,4) [last axis = ν]
        #        sqp is (N,N,N,N,4) [last axis = α]
        # Combine: (N,N,N,N,4,4) array [..., α, ν]
        integrand_alpha_nu = (
            sqp[..., :, None]           # (..., 4, 1)
            * cos2_q_plus_p_half[..., None, :]  # (..., 1, 4)
            * base[..., None, None]     # (..., 1, 1)
        )  # shape (N,N,N,N,4_α, 4_ν)

        J_c = integrand_alpha_nu.mean(axis=(0, 1, 2, 3))  # (4_α, 4_ν)

        # v_α(q) = 2 J^c(α, α) - Σ_ν J^c(α, ν)
        diag = np.diag(J_c)  # J^c(α, α) for each α
        row_sum = J_c.sum(axis=1)  # Σ_ν J^c(α, ν) for each α
        v_q = 2 * diag - row_sum  # (4,)

        # Reshape q index back to (N,N,N,N,4)
        iq_multi = np.unravel_index(iq, (N, N, N, N))
        v[iq_multi[0], iq_multi[1], iq_multi[2], iq_multi[3], :] = v_q

    return v


def compute_SE_V_insertion_at_p0(N, m, pi_s_val=None):
    """Compute δ(bubble)^V contribution to Σ_gauge(p=0), summed over external μ."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)

    t0 = time.time()
    v = compute_vector_v(N, m, pi_s_val)
    dt1 = time.time() - t0
    print(f"  [v computed in {dt1:.1f}s]", flush=True)

    q_grid = build_grid(N)
    sq = np.sin(q_grid)  # (N,N,N,N,4)
    D_q = (sq ** 2).sum(axis=-1) + m ** 2  # (N,N,N,N)
    mask = D_q > 1e-10
    D_q_safe = np.where(mask, D_q, 1.0)

    # Compute δ(bubble)^V_μ(q, 0) for each μ, then sum over q and μ
    # Formula: (8 cos²(q_μ) / D_q³) · [(v·s_q)(D_q - 4 s_{q,μ}²) + 2 D_q v_μ s_{q,μ}]
    # (dropping the overall i factor as it goes into Minkowski-to-Euclidean conversion)

    v_dot_sq = (v * sq).sum(axis=-1)  # (N,N,N,N) = Σ_α v_α s_{q,α}

    total_by_mu = 0.0
    for mu in range(4):
        cos2_qmu = np.cos(q_grid[..., mu]) ** 2
        sqmu = sq[..., mu]  # (N,N,N,N)
        v_mu = v[..., mu]   # (N,N,N,N)

        integrand = (
            8.0 * cos2_qmu / (D_q_safe ** 3)
            * (v_dot_sq * (D_q - 4 * sqmu ** 2) + 2 * D_q * v_mu * sqmu)
        ) * mask

        total_by_mu += integrand.mean()

    dt2 = time.time() - t0 - dt1
    print(f"  [outer sum: {dt2:.1f}s]", flush=True)
    return total_by_mu


def main():
    print("=" * 72)
    print("Vector SE insertion numerical test")
    print("=" * 72)
    print()
    print("Formula: δ(bubble)^V(q, p=0) integrated over q, summed over μ")
    print()

    # Start with small N to verify implementation
    for N, m in [(4, 0.05), (4, 0.10), (6, 0.05), (6, 0.10)]:
        print(f"N = {N}, m = {m}:")
        pi_s = compute_pi_s(N, m)
        val = compute_SE_V_insertion_at_p0(N, m, pi_s)
        print(f"  Π_s = {pi_s:.4f}")
        print(f"  Raw SE-V integrand (summed over μ, averaged over q): {val:+.4e}")
        print()


if __name__ == "__main__":
    main()
