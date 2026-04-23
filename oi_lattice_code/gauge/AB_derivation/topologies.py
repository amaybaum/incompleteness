"""
topologies.py — Dirac loop traces for the three topologies contributing to
Γ_3^{μνρ,abc}(p_1, p_2, p_3) in S_eff at cubic order in A.

Each topology function returns a complex scalar J_D (the Dirac+momentum integral
WITHOUT color factors). Color is applied at the Γ_3 assembly level in gamma3.py.

Memory-efficient: G_0 = (1/D)·𝟙_4 is scalar-in-Dirac, so Tr[G·V_1·G·V_2·...·G·V_n]
factors as (∏ 1/D_i) × Tr_Dirac[V_1·V_2·...·V_n].  We compute the Dirac matrix
chain and trace inline, avoiding large 4×4 propagator arrays.

Conventions:
  - p_i are lattice 4-momenta with p_1 + p_2 + p_3 = 0.
  - μ_i are Lorentz indices in {0, 1, 2, 3}.
  - External leg i has the composite V_i at fermion input momentum k + Σ_{j<i} p_j.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from vertices import (
    lattice_momenta, D_scalar,
    DdagD_1, DdagD_2, DdagD_3, DdagD_2_antisym,
)


def J_triangle(k, p1, p2, p3, mu1, mu2, mu3, m):
    """
    Triangle topology Dirac trace, with vertex ordering (1 → 2 → 3) around loop.
    Returns complex scalar.

    Formula:
      J = (1/N^4) · Σ_k  (1/(D(k) · D(k+p_1) · D(k+p_1+p_2)))
                         · Tr_Dirac[ DD1(k;p_1,μ_1) · DD1(k+p_1;p_2,μ_2)
                                      · DD1(k+p_1+p_2;p_3,μ_3) ]

    Accepts k = array (N^4, 4) of fermion momenta. Returns complex scalar.

    NOTE: DD1 includes a factor of (i·g_0); so three DD1's contribute (i·g_0)^3.
    We track g_0 external. The "i^3 = -i" factor is already in the returned value.
    """
    N4 = k.shape[0]
    D0 = D_scalar(k, m)
    D1 = D_scalar(k + p1, m)
    D2 = D_scalar(k + p1 + p2, m)
    # ( D(k+p_1+p_2+p_3) = D(k) by momentum conservation; that's where the loop closes. )

    V1 = DdagD_1(k, p1, mu1, m)             # at fermion input k
    V2 = DdagD_1(k + p1, p2, mu2, m)        # at k + p_1
    V3 = DdagD_1(k + p1 + p2, p3, mu3, m)   # at k + p_1 + p_2

    # Matrix chain V1·V2·V3, then trace:
    V12 = np.einsum('...ij,...jk->...ik', V1, V2)
    V123 = np.einsum('...ij,...jk->...ik', V12, V3)
    tr_chain = np.trace(V123, axis1=-2, axis2=-1)  # (N^4,) complex

    integrand = tr_chain / (D0 * D1 * D2)
    return np.sum(integrand) / N4


def J_double_tad(k, p_on_1, p_on_2a, p_on_2b, mu_1, mu_2a, mu_2b, m):
    """
    Double-tadpole topology with one external leg (p_on_1, mu_1) on (D†D)^(1)
    and two external legs (p_on_2a, mu_2a), (p_on_2b, mu_2b) on (D†D)^(2).

    Uses the SYMMETRIC-color part of (D†D)^(2) (multiplying {T,T}/2).
    For the antisymmetric-color part (multiplying [T,T]/2 = i·f·T), see
    J_double_tad_antisym.

    Returns complex scalar. Computes:
      (1/N^4) Σ_k (1/(D(k)·D(k+p_on_1))) · Tr[DD1(k;p_on_1,mu_1) · DD2_sym(k+p_on_1; p_on_2a,p_on_2b, mu_2a,mu_2b)]

    Caller sums this over the 3 possible "which leg on D^(1)" assignments.
    """
    N4 = k.shape[0]
    D0 = D_scalar(k, m)
    D1 = D_scalar(k + p_on_1, m)

    V1 = DdagD_1(k, p_on_1, mu_1, m)
    V2 = DdagD_2(k + p_on_1, p_on_2a, p_on_2b, mu_2a, mu_2b, m)

    V12 = np.einsum('...ij,...jk->...ik', V1, V2)
    tr_chain = np.trace(V12, axis1=-2, axis2=-1)
    integrand = tr_chain / (D0 * D1)
    return np.sum(integrand) / N4


def J_double_tad_antisym(k, p_on_1, p_on_2a, p_on_2b, mu_1, mu_2a, mu_2b, m):
    """
    Double-tadpole topology, ANTISYMMETRIC-color part of (D†D)^(2):
    Uses DdagD_2_antisym (multiplying [T^a,T^b]/2 = i·f^{abc}·T^c/2).

    Color trace: Tr_color[T^{a_1} · [T^{a_2a}, T^{a_2b}]/2]
               = (1/2)·(i/2) f^{a_2a a_2b c}·δ^{a_1 c}·(1/2)    [using Tr(T^aT^b)=δ^{ab}/2]
               Wait:  = (i/2) f^{a_2a a_2b c} · Tr[T^{a_1} T^c]
                    = (i/2) f^{a_2a a_2b c} · (1/2) δ^{a_1 c}
                    = (i/4) f^{a_2a a_2b a_1}
                    = (i/4) f^{a_1 a_2a a_2b}    (cyclic invariance of f)

    So the contribution of this topology to Γ_3's f^{abc} coefficient,
    with the leg-on-DD1 carrying color index a_1 = a (first external),
    is the same sign/magnitude prefactor as the sym-dtad contribution to
    d^{abc}-coefficient (which picks up Tr[T^a{T^b,T^c}/2] = d^{abc}/4),
    except the "d/4" is replaced by "i·f/4".

    Caller sums over the 3 "which leg on D^(1)" choices.
    """
    N4 = k.shape[0]
    D0 = D_scalar(k, m)
    D1 = D_scalar(k + p_on_1, m)

    V1 = DdagD_1(k, p_on_1, mu_1, m)
    V2 = DdagD_2_antisym(k + p_on_1, p_on_2a, p_on_2b, mu_2a, mu_2b, m)

    V12 = np.einsum('...ij,...jk->...ik', V1, V2)
    tr_chain = np.trace(V12, axis1=-2, axis2=-1)
    integrand = tr_chain / (D0 * D1)
    return np.sum(integrand) / N4


def J_triple_tad(k, p1, p2, p3, mu1, mu2, mu3, m):
    """
    Triple-tadpole topology: single (D†D)^(3) insertion, one G_0 closing the loop.

    Returns complex scalar. Computes:
      (1/N^4) Σ_k (1/D(k)) · Tr[DD3(k; p_1, p_2, p_3, mu_1, mu_2, mu_3)]

    By single-link δ-functions in D^(3) and D^(2), this is NONZERO only if
    the three Lorentz indices allow at least one of the terms in (D†D)^(3)
    to survive. Practically:
      - D_0^† · D^(3) and D^(3) · D_0 terms: require μ_1 = μ_2 = μ_3.
      - D^(1) · D^(2) and D^(2) · D^(1) terms: require μ of the D^(2) legs to match.
    """
    N4 = k.shape[0]
    D0 = D_scalar(k, m)

    V3 = DdagD_3(k, p1, p2, p3, mu1, mu2, mu3, m)
    tr_V3 = np.trace(V3, axis1=-2, axis2=-1)
    integrand = tr_V3 / D0
    return np.sum(integrand) / N4


# ============================================================
# Self-test
# ============================================================
if __name__ == "__main__":
    print("=== topologies.py self-test ===")
    N, m = 16, 0.05
    k = lattice_momenta(N)
    print(f"Lattice: N={N}, m={m}, k.shape={k.shape}")
    print()

    # A simple test momentum configuration: p_1, p_2, p_3 = three lattice momenta
    # summing to zero (mod 2π).
    # Choose all three in direction 0 for clean testing.
    p1 = np.array([2*np.pi/N, 0, 0, 0])    # (1, 0, 0, 0)/N * 2π
    p2 = np.array([2*np.pi/N, 0, 0, 0])
    p3 = -(p1 + p2)

    print(f"Test momenta (direction-0):")
    print(f"  p_1 = {p1}")
    print(f"  p_2 = {p2}")
    print(f"  p_3 = {p3}")
    print()

    # Case A: all μ = 0 — all three topologies contribute.
    print("--- All μ = 0 ---")
    J_tri = J_triangle(k, p1, p2, p3, 0, 0, 0, m)
    J_dtad = sum(
        [
            J_double_tad(k, p1, p2, p3, 0, 0, 0, m),  # leg 1 on D^(1); legs 2, 3 on D^(2)
            J_double_tad(k, p2, p1, p3, 0, 0, 0, m),  # leg 2 on D^(1); legs 1, 3 on D^(2)
            J_double_tad(k, p3, p1, p2, 0, 0, 0, m),  # leg 3 on D^(1); legs 1, 2 on D^(2)
        ]
    )
    J_ttad = J_triple_tad(k, p1, p2, p3, 0, 0, 0, m)
    print(f"  J_triangle        = {J_tri:.6f}")
    print(f"  J_double_tad (sum over 3)  = {J_dtad:.6f}")
    print(f"  J_triple_tad      = {J_ttad:.6f}")
    print()

    # Case B: μ = (0, 1, 2) — only triangle should contribute.
    print("--- μ = (0, 1, 2) — only triangle should be nonzero ---")
    J_tri_B = J_triangle(k, p1, p2, p3, 0, 1, 2, m)
    J_dtad_B = sum(
        [
            J_double_tad(k, p1, p2, p3, 0, 1, 2, m),  # D^(2) legs (μ=1, μ=2) — δ fails
            J_double_tad(k, p2, p1, p3, 1, 0, 2, m),  # D^(2) legs (μ=0, μ=2) — δ fails
            J_double_tad(k, p3, p1, p2, 2, 0, 1, m),  # D^(2) legs (μ=0, μ=1) — δ fails
        ]
    )
    J_ttad_B = J_triple_tad(k, p1, p2, p3, 0, 1, 2, m)
    print(f"  J_triangle        = {J_tri_B:.6f}")
    print(f"  J_double_tad (sum)= {J_dtad_B:.6f}  (expect 0: D^(2) has δ_{{μν}})")
    print(f"  J_triple_tad      = {J_ttad_B:.6f}  (expect 0)")
    print()

    # Case C: Furry-like — compare J_triangle(p_1,p_2,p_3) vs J_triangle(p_1,p_3,p_2).
    # For vector-like naive-Γ fermion, Furry says: J_132 = -J_123 (same magnitude, opposite sign).
    print("--- Triangle ordering test: J(1,2,3) vs J(1,3,2), μ=(0,0,0) ---")
    # Choose asymmetric momenta for a non-trivial test
    q1 = np.array([2*np.pi/N, 0, 0, 0])
    q2 = np.array([0, 2*np.pi/N, 0, 0])
    q3 = -(q1 + q2)
    J_123 = J_triangle(k, q1, q2, q3, 0, 0, 0, m)
    J_132 = J_triangle(k, q1, q3, q2, 0, 0, 0, m)
    print(f"  J(1,2,3) = {J_123:.6e}")
    print(f"  J(1,3,2) = {J_132:.6e}")
    print(f"  sum      = {J_123 + J_132:.6e}  (Furry: expect 0 for vector fermion)")
    print(f"  diff     = {J_123 - J_132:.6e}")
