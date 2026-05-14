"""
yang_mills_lattice.py — Wilson-action lattice YM n-gluon vertices.

The Wilson plaquette action is:
    S_W = (2/g_0²) Σ_{plaq} [1 - (1/N) Re Tr U_plaq]
where U_plaq is the path-ordered product around a 1x1 plaquette.

Expanding U_μ(x) = exp(i g_0 A_μ(x + μ̂/2)) and symmetrizing to the mid-link
gives the familiar lattice gauge action in terms of the gauge potentials
A_μ. Expanded to n-th order in g_0 A, one gets the n-gluon vertex.

Standard references:
  Rothe, "Lattice Gauge Theories", Chapter 3
  Capitani, "Lattice perturbation theory", Phys. Rep. 382 (2003), Eq. (2.80)+

The continuum limit is the standard YM 3-gluon vertex
    V_{3g}^{abc,μνρ}(p_1,p_2,p_3) = -i g_0 f^{abc} [
        δ^{μν}(p_1-p_2)^ρ + δ^{νρ}(p_2-p_3)^μ + δ^{ρμ}(p_3-p_1)^ν ]
with lattice corrections p → p_hat (where p_hat_μ = 2 sin(p_μ/2)) and
cos-factors on the non-delta indices.

LATTICE FORM (Wilson action, following Capitani Eq. 2.83):

V_{3g}^{abc, μνρ}(p_1, p_2, p_3) = -i g_0 f^{abc} · K_{3g}^{μνρ}(p_1, p_2, p_3)

where K_{3g} is an explicit kinematic tensor. At zero lattice spacing, it
reduces to the continuum δ(p_1-p_2)^ρ + cyclic.

Explicit form (standard convention — see Capitani 2.83 or Weisz):

    K_{3g}^{μνρ}(p_1,p_2,p_3)
        = δ^{μν} · cos((p_3)_μ/2) · (p_1_hat - p_2_hat)^ρ
        + δ^{νρ} · cos((p_1)_ν/2) · (p_2_hat - p_3_hat)^μ
        + δ^{ρμ} · cos((p_2)_ρ/2) · (p_3_hat - p_1_hat)^ν

where p_hat_μ = 2 sin(p_μ / 2).

This is ONE of several equivalent forms (plaquette-symmetric vs link-symmetric
conventions give different explicit formulae but the same physical vertex).
"""
import numpy as np


def p_hat(p):
    """Lattice momentum p̂_μ = 2 sin(p_μ/2). Vectorized over 4-vectors."""
    return 2.0 * np.sin(p / 2.0)


def V_3g_ym(p1, p2, p3, mu1, mu2, mu3):
    """Wilson-action YM 3-gluon vertex, color-stripped.

    Returns the kinematic scalar K_{3g}^{μ_1 μ_2 μ_3}(p_1, p_2, p_3).
    The full vertex is -i · g_0 · f^{abc} · K_{3g}.

    Momentum conservation: p_1 + p_2 + p_3 = 0 (all incoming).

    At lattice spacing a → 0, p̂ → p and cos(p/2) → 1, reducing to
    continuum δ^{μν}(p_1-p_2)^ρ + cyclic.
    """
    p1h = p_hat(p1)
    p2h = p_hat(p2)
    p3h = p_hat(p3)
    K = 0.0
    # δ^{μν} · cos(p_3_μ / 2) · (p_1 - p_2)_hat^ρ
    if mu1 == mu2:
        K += np.cos(p3[mu1] / 2.0) * (p1h[mu3] - p2h[mu3])
    # δ^{νρ} · cos(p_1_ν / 2) · (p_2 - p_3)_hat^μ
    if mu2 == mu3:
        K += np.cos(p1[mu2] / 2.0) * (p2h[mu1] - p3h[mu1])
    # δ^{ρμ} · cos(p_2_ρ / 2) · (p_3 - p_1)_hat^ν
    if mu3 == mu1:
        K += np.cos(p2[mu3] / 2.0) * (p3h[mu2] - p1h[mu2])
    return K


def V_3g_continuum(p1, p2, p3, mu1, mu2, mu3):
    """Continuum limit: a→0 form (for cross-check)."""
    K = 0.0
    if mu1 == mu2:
        K += (p1[mu3] - p2[mu3])
    if mu2 == mu3:
        K += (p2[mu1] - p3[mu1])
    if mu3 == mu1:
        K += (p3[mu2] - p1[mu2])
    return K


# ============================================================
# Sanity tests
# ============================================================
if __name__ == "__main__":
    # Test 1: continuum limit. Use small momenta — lattice should match continuum.
    np.random.seed(0)
    p1 = 0.01 * np.random.randn(4)
    p2 = 0.01 * np.random.randn(4)
    p3 = -(p1 + p2)

    print("=== Wilson YM 3-gluon vertex sanity checks ===\n")

    print("--- Continuum limit check (small momenta, a→0) ---")
    print(f"{'μ':>10} {'lattice':>15} {'continuum':>15} {'rel err':>10}")
    for mu1, mu2, mu3 in [(0,0,1), (0,1,0), (1,0,0), (0,1,1), (1,1,0), (1,0,1),
                          (0,1,2), (1,2,0), (2,0,1)]:
        lat = V_3g_ym(p1, p2, p3, mu1, mu2, mu3)
        cont = V_3g_continuum(p1, p2, p3, mu1, mu2, mu3)
        rel = abs(lat - cont) / (abs(cont) + 1e-20)
        print(f"  ({mu1},{mu2},{mu3}):  {lat:+.6e}  {cont:+.6e}  {rel:.2e}")

    # Test 2: Bose antisymmetry under (1↔2). Since the vertex is
    # -i g_0 f^{abc} K_{3g}, and f^{bac} = -f^{abc}, we need
    # K_{3g}(p_2, p_1, p_3; μ_2, μ_1, μ_3) = -K_{3g}(p_1, p_2, p_3; μ_1, μ_2, μ_3).
    print("\n--- Bose antisymmetry under (1↔2) ---")
    # Larger momenta — test full lattice formula
    p1 = np.array([0.3, 0.1, 0, 0.2])
    p2 = np.array([0.1, 0.4, 0.2, 0])
    p3 = -(p1 + p2)
    print(f"{'μ':>10} {'K(1,2,3)':>15} {'K(2,1,3)':>15} {'sum':>12}")
    for mu1, mu2, mu3 in [(0,0,1), (0,1,0), (1,2,3), (0,1,1)]:
        K123 = V_3g_ym(p1, p2, p3, mu1, mu2, mu3)
        K213 = V_3g_ym(p2, p1, p3, mu2, mu1, mu3)
        print(f"  ({mu1},{mu2},{mu3}):  {K123:+.6e}  {K213:+.6e}  {K123+K213:+.2e}")

    # Test 3: Cyclic (1→2→3→1) — since f^{bca} = f^{abc}, K should cyclic-invariant
    print("\n--- Cyclic (1→2→3) invariance ---")
    for mu1, mu2, mu3 in [(0,0,1), (1,2,3), (0,1,2)]:
        K123 = V_3g_ym(p1, p2, p3, mu1, mu2, mu3)
        K231 = V_3g_ym(p2, p3, p1, mu2, mu3, mu1)
        K312 = V_3g_ym(p3, p1, p2, mu3, mu1, mu2)
        print(f"  ({mu1},{mu2},{mu3}):  {K123:+.4e}  {K231:+.4e}  {K312:+.4e}")
