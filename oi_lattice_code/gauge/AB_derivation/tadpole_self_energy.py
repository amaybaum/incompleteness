"""
Addendum to yang_mills_lattice.py — the continuum YM 4-gluon vertex.

Standard form (Peskin & Schroeder eq. 16.6 or equivalent):

V_{4g}^{a_1 a_2 a_3 a_4, μ_1 μ_2 μ_3 μ_4}(p_1, p_2, p_3, p_4) = -i g² · [
    f^{a_1 a_2 e} f^{a_3 a_4 e} · (δ^{μ_1 μ_3} δ^{μ_2 μ_4} - δ^{μ_1 μ_4} δ^{μ_2 μ_3})
  + f^{a_1 a_3 e} f^{a_2 a_4 e} · (δ^{μ_1 μ_2} δ^{μ_3 μ_4} - δ^{μ_1 μ_4} δ^{μ_2 μ_3})
  + f^{a_1 a_4 e} f^{a_3 a_2 e} · (δ^{μ_1 μ_3} δ^{μ_2 μ_4} - δ^{μ_1 μ_2} δ^{μ_3 μ_4})
]

Continuum V_4g is MOMENTUM-INDEPENDENT (no p_i dependence in the tensor).
Lattice corrections (Wilson action to 4th order in g A) bring cos/sin factors;
these are formally a²-suppressed and can be added as refinement later.

For the TADPOLE at external (p_1, p_2) = 0 and internal (p_3, p_4) = (k, -k),
I contract legs 3,4 with the Feynman-gauge propagator (δ^{cd} · δ^{μ_3 μ_4} /(k̂² Π_s)):

  Σ^{ab, μν}_tad(0) = (1/2) · Σ_k V_{4g}^{ab cc, μν ρρ}(0,0,k,-k) / (k̂² Π_s)
                                   ↑ sum over internal color c and Lorentz ρ (α)

Color contractions (c=d summed):
  Structure 1: f^{abe}f^{cce} = 0
  Structure 2: f^{ace}f^{bce} → N δ^{ab}  (SU(N) adjoint C_2 = N)
  Structure 3: f^{ade}f^{bce} → N δ^{ab} (same)

Lorentz contractions (ρ=σ summed):
  Structure 1: Σ_α (δ^{μα}δ^{να} - δ^{μα}δ^{να}) = 0
  Structure 2: Σ_α (δ^{μν}·1 - δ^{μα}δ^{να}) = 4δ^{μν} - δ^{μν} = 3 δ^{μν}
  Structure 3: Σ_α (δ^{μν}·1 - δ^{μα}δ^{να}) = 3 δ^{μν}

Color+Lorentz combined:  2 · N · 3 δ^{ab}δ^{μν} = 6N δ^{ab} δ^{μν}

So:
  Σ^{ab, μν}_tad(0) = (-i g²) · 6 · C_2(adj) · δ^{ab} δ^{μν} · (1/2) · ∫ d⁴k / (k̂² Π_s)
                   = -3i g² · C_2 · δ^{ab} δ^{μν} · I_tad

where I_tad = ∫ d⁴k / (k̂²(k) · Π_s) — the standard 1-loop lattice tadpole
integral with induced propagator.

IMPORTANT: factor conventions. The "-i" is Minkowski; in Euclidean (which the
rest of our code uses) this becomes real. Let me track this at the end of
the session when combining diagrams; for now, compute magnitudes and structure.
"""
import numpy as np
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s


def compute_tadpole_sigma(N, m, pi_s_val=None):
    """Tadpole contribution to 2-loop gauge self-energy at p=0, per C_2.
    
    Uses continuum V_4g (momentum-independent). Lattice corrections TODO.
    
    Returns (Σ_tad/C_2) as a 4×4 matrix (should be ∝ δ^{μν} by symmetry).
    """
    if pi_s_val is None:
        pi_s_val = compute_pi_s(N, m)
    dk = 2 * np.pi / N
    vol = 1.0 / N**4   # lattice measure (in units of 1/(2π)^4: see note)
    # 
    # Actually the volume factor: ∫ d⁴k/(2π)⁴ → (2π/N)⁴/(2π)⁴ · sum = 1/N⁴ · sum.
    # So discrete mean (k) is equivalent to (2π)⁻⁴ ∫ d⁴k.

    # Physical BZ (-π, π]: shift indices > N/2 down by N
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    
    # Induced gauge propagator D_ind(k) = 1/(k̂² · Π_s)
    khat2 = (2 * np.sin(k_flat / 2))**2
    khat2_sum = khat2.sum(axis=-1)
    D_ind = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)
    
    # I_tad = mean of D_ind (since volume factor folded into the mean)
    I_tad = D_ind.mean()
    
    # Σ_tad^{μν}/C_2 = 3 · δ^{μν} · I_tad · (1/2 loop factor)
    # Actually the 1/2 is already in the bubble; for tadpole with 4-gluon
    # at one vertex, there is NO 1/2 symmetry factor from the loop
    # (distinct from the bubble where two 3-gluon vertices are symmetric).
    # Wait no — the tadpole has just one vertex with 4 legs, but the gauge
    # loop closure gives Bose symmetry on the 3,4 leg pair. The symmetry
    # factor is 1/2 for identical bosons in the loop.
    # 
    # Actually: the Wick contraction of two gluon fields at 4-gluon vertex
    # has a 1/2 for the pair. So the 1/2 IS there. Let me include it.
    
    # Full tadpole per C_2, ignoring overall i factor:
    # Σ_tad^{μν}/C_2 = (1/2) · 6 · δ^{μν} · I_tad = 3 · δ^{μν} · I_tad
    Sigma_tad = 3.0 * I_tad * np.eye(4)
    
    return Sigma_tad, pi_s_val, I_tad


if __name__ == "__main__":
    print("=== Tadpole diagram Σ^{μν}_tad(p=0) (continuum V_4g, leading-order) ===\n")
    m = 0.05
    print(f"fermion mass m = {m}\n")
    print(f"{'N':>4}  {'Π_s(0)':>8}  {'I_tad':>10}  {'Σ_tad/C_2 (diag)':>18}  {'Σ_tad·Π_s²':>12}")
    print("-" * 75)
    tad_results = {}
    for N in [6, 8, 10, 12, 16]:
        t0 = time.time()
        pi_s = compute_pi_s(N, m)
        Sigma_tad, _, I_tad = compute_tadpole_sigma(N, m, pi_s_val=pi_s)
        dt = time.time() - t0
        # diagonal value
        sig = Sigma_tad[0, 0]
        sig_pi2 = sig * pi_s**2
        print(f"{N:>4}  {pi_s:>8.4f}  {I_tad:>10.4f}  {sig:>18.5e}  {sig_pi2:>12.4e}  [{dt:.1f}s]", flush=True)
        tad_results[N] = (sig, pi_s, I_tad)
