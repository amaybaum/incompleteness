#!/usr/bin/env python3
"""
Boundary spectral measure of the substratum-to-observer coarse-graining map.

Reconstruction of the linear-map computation (ch19 §19.3.7 / SM §3.1), which is the
baseline the interacting (condensate-dressed) extension must be measured against.

SETUP
  d = 3 simple-cubic substratum, OI linear wave equation, exact lattice dispersion
      cos(w) = (1/d) * sum_j cos(k_j)                                [SM §4.1]
  Frequency-domain operator H = A/(2d), eigenvalue E = cos(w); w -> 0 is E -> 1.

PARTITION (horizon ontology)
  hidden = semi-infinite half-space z >= 1; boundary = the interface plane.
  Because the visible/hidden split is translation-invariant along the interface, the
  trace-out is EXACT per transverse momentum k_par: G_RR restricted to the interface
  is the surface Green's function of the hidden half-space — the smearing kernel —
  given by the decaying root of

      t^2 g^2 - (E - eps(k_par)) g + 1 = 0,
      eps(k_par) = (cos kx + cos ky)/d,      t = 1/(2d).

OBSERVABLE
  rho_RR(w) = -(1/pi) Im Tr_bd G_RR(E(w)+i0) * |dE/dw|

DECISION RULE (pre-registered)
  rho(w) ~ w^p.   p > 0  => LOCAL (power-suppressed IR weight).
                  p = -1 => log-uniform / NON-LOCAL.
  The non-local branch is what would be needed to lift nu to the DESI-detectable
  ~1e-4 level, and would show up simultaneously as rotational Lorentz violation and
  a breakdown of the K=2d mode count.
"""
import numpy as np

D = 3
T = 1.0 / (2 * D)


def fit_loglog(x, y):
    m = (y > 0) & (x > 0) & np.isfinite(y)
    return np.polyfit(np.log(x[m]), np.log(y[m]), 1)[0] if m.sum() >= 4 else np.nan


def g_surface(E_eff, t=T):
    """Decaying root of t^2 g^2 - E_eff g + 1 = 0, retarded branch (Im g <= 0)."""
    E = np.asarray(E_eff, dtype=complex)
    disc = np.sqrt(E**2 - 4 * t**2 + 0j)
    g1 = (E - disc) / (2 * t**2)
    g2 = (E + disc) / (2 * t**2)
    # retarded: pick the root with non-positive imaginary part
    return np.where(np.imag(g1) <= np.imag(g2), g1, g2)


def rho_boundary(w, n_k=4001):
    """Boundary-projected spectral density at frequency w, by radial k_par integration.

    CANCELLATION-FREE FORMULATION. The naive route computes E = cos(w) and subtracts;
    for w below ~1e-8, cos(w) rounds to 1.0 in float64 and the w^2/2 information is
    destroyed — the naive Part C sweep returned p = +3.55 at s = 1e-26 and NaN at
    1e-30 for exactly this reason. The stable variable is the distance to the band
    edge, built from 1 - cos(x) = 2 sin^2(x/2), which never cancels:

        E_eff - 2t = -2 sin^2(w/2) + (2/D) [sin^2(kx/2) + sin^2(ky/2)]
        E_eff + 2t = (E_eff - 2t) + 4t          (4t = 2/D, exact)

    and the surface GF discriminant is sqrt((E_eff-2t)(E_eff+2t)) directly.
    """
    kmax = min(np.pi, max(6.0 * w, 3.0e-12))
    k = np.linspace(kmax * 1e-9, kmax, n_k)
    th = np.linspace(0, np.pi / 2, 97)
    KX = np.outer(k, np.cos(th))
    KY = np.outer(k, np.sin(th))
    em2t = -2.0 * np.sin(w / 2) ** 2            + (2.0 / D) * (np.sin(KX / 2) ** 2 + np.sin(KY / 2) ** 2) + 0j
    ep2t = em2t + 4.0 * T
    E_eff = em2t + 2.0 * T
    disc = np.sqrt(em2t * ep2t)
    g1 = (E_eff - disc) / (2 * T**2)
    g2 = (E_eff + disc) / (2 * T**2)
    g = np.where(np.imag(g1) <= np.imag(g2), g1, g2)
    im = -np.imag(g) / np.pi
    ang = np.trapezoid(im, th, axis=1) * (2.0 / np.pi)
    integ = np.trapezoid(ang * k, k) * 2 * np.pi
    return integ * abs(np.sin(w))


def control_2d(w):
    """Intrinsic 2D local theory: DOS ~ w  (known exponent +1)."""
    return w * np.ones_like(w)


def control_3d_bulk(w, n=400000, seed=0):
    """3D bulk OI dispersion: DOS ~ w^2 (known exponent +2).

    Importance-sampled inside the small-|k| ball that carries the support. Uniform
    sampling over the full Brillouin zone does NOT work here and returned a spurious
    +1.4: at w = 2.5e-3 the relevant shell is |k| ~ sqrt(3) w, a fraction ~1e-10 of
    the zone, so the estimate was noise. The failure was in the estimator, not the
    dispersion — which is why the control exists.
    """
    rng = np.random.default_rng(seed)
    out = []
    for wi in w:
        R = 3.0 * np.sqrt(D) * wi
        u = rng.normal(size=(n, 3))
        u /= np.linalg.norm(u, axis=1)[:, None]
        r = R * rng.random(n) ** (1 / 3)
        wk = np.arccos(np.clip(np.mean(np.cos(u * r[:, None]), axis=1), -1, 1))
        dw = 0.10 * wi
        vol = (4 / 3) * np.pi * R**3
        out.append(np.mean(np.abs(wk - wi) < dw) * vol / (2 * dw))
    return np.array(out)


if __name__ == "__main__":
    w = np.logspace(np.log10(2.5e-3), np.log10(1.3e-1), 22)

    print("PART 0 — estimator controls (acceptance criterion)")
    p2 = fit_loglog(w, control_2d(w))
    p3 = fit_loglog(w, control_3d_bulk(w))
    print(f"   intrinsic 2D local   p = {p2:+.2f}   (known +1)")
    print(f"   3D bulk OI           p = {p3:+.2f}   (known +2)")
    ok = abs(p2 - 1) < 0.15 and abs(p3 - 2) < 0.25
    print(f"   controls {'PASS' if ok else 'FAIL'}")

    print("\nPART A — actual boundary-projected measure from G_RR")
    rho = np.array([rho_boundary(wi) for wi in w])
    pA = fit_loglog(w, rho)
    print(f"   rho_RR(w) ~ w^p      p = {pA:+.2f}")
    print(f"   verdict: {'LOCAL (power-suppressed)' if pA > 0.5 else 'NON-LOCAL'}")

    print("\nPART C — slow-bath robustness (lambda = w^2 representation)")
    for s in (1.0, 1e-8, 1e-15, 1e-22, 1e-30):
        ws = w * (s ** 0.25)
        r = np.array([rho_boundary(wi) for wi in ws])
        print(f"   s = tau_S/tau_B = {s:<8.0e}  p = {fit_loglog(ws, r):+.2f}")
