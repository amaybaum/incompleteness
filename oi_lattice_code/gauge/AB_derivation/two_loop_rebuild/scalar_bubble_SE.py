"""
scalar_bubble_SE.py — Scalar bubble SE contribution in raw-integrand units,
matching the normalization used by vector_SE_insertion.py and
seagull_SE_insertion.py.

Integrand:
  δ(bubble)^S_μ(q, p=0) = 8m · cos²(q_μ) · Σ_f^S(q) · [1/D² − 4 s_μ²/D³]

Reuses Σ_f^S from seagull_SE_insertion.compute_scalar_Sigma_f.
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
from seagull_SE_insertion import compute_scalar_Sigma_f


def compute_scalar_bubble_SE(N, m, pi_s_val=None, Sigma_S=None):
    """δ(bubble)^S contribution at p=0, summed over μ, averaged over q."""
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    if Sigma_S is None:
        Sigma_S = compute_scalar_Sigma_f(N, m, pi_s_val)

    q_grid = build_grid(N)
    sq = np.sin(q_grid)
    D_q = (sq ** 2).sum(axis=-1) + m ** 2
    mask = D_q > 1e-10
    D_q_safe = np.where(mask, D_q, 1.0)

    total = 0.0
    for mu in range(4):
        cos2_qmu = np.cos(q_grid[..., mu]) ** 2
        sqmu_sq = sq[..., mu] ** 2
        bracket = 1.0 / (D_q_safe ** 2) - 4 * sqmu_sq / (D_q_safe ** 3)
        integrand = 8.0 * m * cos2_qmu * Sigma_S * bracket * mask
        total += integrand.mean()

    return total


def main():
    print("=" * 72)
    print("Scalar bubble SE in raw-integrand units")
    print("=" * 72)
    print()

    for N, m in [(6, 0.05), (6, 0.10), (8, 0.05), (8, 0.10)]:
        t0 = time.time()
        pi_s = compute_pi_s(N, m)
        Sigma_S = compute_scalar_Sigma_f(N, m, pi_s)
        val = compute_scalar_bubble_SE(N, m, pi_s, Sigma_S)
        dt = time.time() - t0
        print(f"N={N}, m={m}: Π_s={pi_s:.4f}, scalar bubble SE = {val:+.5e}  [{dt:.1f}s]")


if __name__ == "__main__":
    main()
