"""
paper_pi_s.py — Paper's 1-loop staggered VP Π_s(0), from their formula.
    Π_s(0) = ∫d⁴q [cos²(q_μ)/D(q) - cos²(q_μ)·sin²(q_μ)/D(q)²]
    D(q) = Σ_ν sin²(q_ν) + m²
    spatial μ = 1,2,3 (average)
Target: Π_s(0) → 0.3084 as N → ∞, giving 1/α_0 = 6·Π_s·4π = 23.25.
"""
import numpy as np


def compute_pi_s(N, m):
    """Return scalar Π_s(0) at N^4 grid, fermion mass m."""
    dk = 2*np.pi/N
    idx = np.arange(N)
    I0, I1, I2, I3 = np.meshgrid(idx, idx, idx, idx, indexing='ij')
    q = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    sin2 = np.sin(q)**2
    cos2 = np.cos(q)**2
    D = sin2.sum(axis=-1) + m**2
    contribs = []
    for mu in [1, 2, 3]:
        contribs.append((cos2[..., mu]/D - cos2[..., mu]*sin2[..., mu]/D**2).mean())
    return np.mean(contribs)


if __name__ == "__main__":
    print(f"{'N':>4} {'m':>7} {'Π_s(0)':>10} {'1/α_0':>8}")
    for N in [12, 16, 20, 24]:
        for m in [0.05, 0.01]:
            pi_s = compute_pi_s(N, m)
            print(f"{N:>4}  {m:>.3f}  {pi_s:>10.5f}  {6*pi_s*4*np.pi:>8.3f}")
