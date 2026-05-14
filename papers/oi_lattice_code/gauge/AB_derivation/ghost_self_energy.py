"""
ghost_self_energy.py — Faddeev–Popov ghost bubble contribution to Σ^{μν}(p).

In covariant (Feynman) gauge with standard FP ghosts, the ghost bubble gives:

    Σ_{ghost}^{μν}(p) = -(-1)^ghost · C_2(adj) · ∫ d⁴k V_gh^μ(p,k) V_gh^ν(-p,-k-p)
                                                   × D_gh(k) · D_gh(k+p)

Ghost-gluon vertex:  V_gh^μ(p_gluon, q_ghost) = q^μ (outgoing ghost momentum)
Ghost propagator:  D_gh(k) = 1/k̂²  (NOT induced — standard pure-gauge propagator)
Minus sign from closed ghost loop: (-1)^ghost

Collecting: Σ_{gh}^{μν}(p) = -C_2 · Σ_k [(-k̂^μ)(p̂+k̂)^ν] / (k̂² · (p̂+k̂)²)
                           = +C_2 · Σ_k [k̂^μ(p̂+k̂)^ν] / (k̂² · (p̂+k̂)²)

Two remarks on sign/convention:
- I'm using k̂_μ = 2 sin(k_μ/2) for the ghost-gluon vertex momentum factor on
  the lattice (this is standard for Wilson-action ghost vertices in Feynman gauge).
- The overall sign convention matches the way Π_T of the sum bubble+ghost gives
  the physical running in standard QCD.

Open question for OI framework: is the ghost propagator ALSO induced (i.e.,
1/(k̂²·Π_s_ghost(k))), or standard (1/k̂²)? The paper doesn't say. Try standard
first; if the sum bubble+ghost doesn't come out gauge-invariant (Ward), the
ghost may need to be induced too.
"""
import numpy as np
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from paper_pi_s import compute_pi_s
from bubble_at_finite_p import compute_bubble_at_p


def compute_ghost_sigma_at_p(N, p_ext, use_induced=False, pi_s_val=None, m=None):
    """Ghost-loop contribution to Σ^{μν}(p_ext) / C_2.
    
    Returns the 4x4 matrix Σ_{ghost}^{μν} / C_2.
    use_induced: if True, ghost propagator 1/(k̂²·Π_s); else standard 1/k̂².
    """
    if use_induced and pi_s_val is None:
        if m is None:
            raise ValueError("Need m for induced ghost with Π_s")
        pi_s_val = compute_pi_s(N, m)
    
    dk = 2*np.pi / N
    vol = 1.0 / N**4
    idx = np.arange(N)
    idx_shifted = np.where(idx > N//2, idx - N, idx)
    I0, I1, I2, I3 = np.meshgrid(idx_shifted, idx_shifted, idx_shifted, idx_shifted, indexing='ij')
    k_grid = np.stack([I0*dk, I1*dk, I2*dk, I3*dk], axis=-1)
    k_flat = k_grid.reshape(-1, 4)
    
    # Lattice momenta on ghost legs
    khat = 2*np.sin(k_flat/2)    # (Npts, 4)
    pk = p_ext[np.newaxis, :] + k_flat
    pkhat = 2*np.sin(pk/2)
    
    khat2_sum = (khat**2).sum(axis=-1)
    pkhat2_sum = (pkhat**2).sum(axis=-1)
    
    if use_induced:
        D_k = np.where(khat2_sum > 1e-12, 1.0 / (khat2_sum * pi_s_val), 0.0)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / (pkhat2_sum * pi_s_val), 0.0)
    else:
        D_k = np.where(khat2_sum > 1e-12, 1.0 / khat2_sum, 0.0)
        D_pk = np.where(pkhat2_sum > 1e-12, 1.0 / pkhat2_sum, 0.0)
    
    # Σ_gh^{μν} = +C_2 · Σ_k  k̂^μ · (p̂+k̂)^ν · D_k · D_pk
    # Integrand per k: khat[k,μ] · pkhat[k,ν] · D_k[k] · D_pk[k]
    integrand = khat[:, :, np.newaxis] * pkhat[:, np.newaxis, :] * (D_k * D_pk)[:, np.newaxis, np.newaxis]
    Sigma_gh = integrand.sum(axis=0) * vol
    
    return Sigma_gh


if __name__ == "__main__":
    print("=== Ghost-loop contribution to Σ^{μν}(p) ===\n")
    m = 0.05
    
    for N in [8, 12]:
        kappa = 2*np.pi / N
        pi_s = compute_pi_s(N, m)
        print(f"\n--- N={N}, m={m}, Π_s={pi_s:.4f}, κ={kappa:.4f} ---\n")
        
        print(f"Scan p_ext = λ · κ · ê_0 for λ = 0, 1, 2, 3")
        print(f"Using STANDARD (non-induced) ghost propagator 1/k̂²\n")
        
        gh_standard = {}
        bub_results = {}
        for lam in [0, 1, 2, 3]:
            p_ext = lam * kappa * np.array([1, 0, 0, 0])
            
            t0 = time.time()
            Sigma_gh = compute_ghost_sigma_at_p(N, p_ext, use_induced=False)
            Sigma_bub, _ = compute_bubble_at_p(N, m, p_ext, pi_s_val=pi_s)
            dt = time.time() - t0
            
            gh_standard[lam] = Sigma_gh
            bub_results[lam] = Sigma_bub
            
            total = Sigma_gh + Sigma_bub
            print(f"  λ={lam}: [bubble] Σ^{{00}}={Sigma_bub[0,0]:+.4e} Σ^{{11}}={Sigma_bub[1,1]:+.4e}   "
                  f"[ghost] Σ^{{00}}={Sigma_gh[0,0]:+.4e} Σ^{{11}}={Sigma_gh[1,1]:+.4e}", flush=True)
            print(f"         [sum]    Σ^{{00}}={total[0,0]:+.4e} Σ^{{11}}={total[1,1]:+.4e}  (Σ^{{11}}-Σ^{{00}})={total[1,1]-total[0,0]:+.4e}")
        
        # Extract Π from (Σ^{11} - Σ^{00})/p̂² at each λ
        print(f"\n  Extracted (Σ^{{11}}-Σ^{{00}})/p̂² · Π_s² (SHOULD BE STABLE across λ if gauge-invariant):")
        for lam in [1, 2, 3]:
            p_0 = lam * kappa
            p2_lat = (2*np.sin(p_0/2))**2
            total = gh_standard[lam] + bub_results[lam]
            diff = total[1,1] - total[0,0]
            PiT_times_Pis2 = (diff / p2_lat) * pi_s**2
            # Also bubble-only and ghost-only for comparison
            bub_only = (bub_results[lam][1,1] - bub_results[lam][0,0]) / p2_lat * pi_s**2
            gh_only = (gh_standard[lam][1,1] - gh_standard[lam][0,0]) / p2_lat * pi_s**2
            print(f"  λ={lam} p̂²={p2_lat:.5f}:  bubble·Π_s²={bub_only:+.4e}  ghost·Π_s²={gh_only:+.4e}  sum·Π_s²={PiT_times_Pis2:+.4e}")
