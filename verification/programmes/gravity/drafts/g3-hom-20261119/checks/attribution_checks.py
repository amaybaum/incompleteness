#!/usr/bin/env python3
"""G3-HOM node 2-3: algebra and curves for candidate horizon attribution rules.

Units hbar = c = k_B = 1.  Exact identities are checked with Fractions at
seeded random rational points (each identity is also derived in RESULT.md;
the checks guard the algebra, they do not replace the derivation).  The
w(z) curves and horizon radii are numerical (RK4 and quadrature in floats)
and are reported as illustrations at a supplied Omega_de0; no verdict reads
a floating-point value as an exact equality.

Run:  python3 -I attribution_checks.py   (exit status 0 iff every check holds)
"""
import math
import random
import sys
from fractions import Fraction as Fr

RESULTS = []


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")


rng = random.Random(20261119)


def rq(lo=1, hi=97):
    return Fr(rng.randint(lo, hi), rng.randint(lo, hi))


# Quantities containing pi are carried as (coefficient of pi^k) by hand:
#   S = sigma*4*pi*R^2/eps^2,  T = eps^2*kappa/(8*pi*G*sigma),  V = 4*pi*R^3/3.
# S*T is pi-free; rho*pi = S*T/(V/pi).

def rho_times_pi(sigma, eps, G, R, kappa, factor=1):
    ST = (sigma * 4 * R**2 / eps**2) * (eps**2 * kappa / (8 * G * sigma))  # pi cancels
    V_over_pi = Fr(4, 3) * R**3
    return factor * ST / V_over_pi


def exact_identities():
    ok_norm = ok_dimfree = ok_ms = ok_nodyn = ok_nu = ok_kod = ok_kod_ode = ok_li_ode = ok_li_ds = True
    for _ in range(200):
        sigma, eps, G, R = rq(), rq(), rq(), rq()
        # (a) E = S*T with kappa = 1/R gives rho = 3/(8 pi G R^2), independent of sigma and eps.
        rp = rho_times_pi(sigma, eps, G, R, 1 / R)
        ok_norm &= (rp * 8 * G * R**2 / 3 == 1)
        ok_dimfree &= (rp == rho_times_pi(rq(), rq(), G, R, 1 / R))
        # (b) Misner-Sharp: E_s = S*T = R_A/(2G) equals (4 pi/3) R_A^3 rho_tot iff H^2 = 8 pi G rho_tot/3.
        H = rq()
        RA = 1 / H
        E_s = RA / (2 * G)
        rho_tot_pi = 3 * H**2 / (8 * G)          # pi * rho_crit
        ok_ms &= (E_s == Fr(4, 3) * RA**3 * rho_tot_pi)
        # (c) No dynamics: for arbitrary (H, Hdot) the pair rho_s = 3H^2/8piG and the conservation-
        #     defined p_s = -rho_s - rho_s_dot/(3H) satisfy both Friedmann equations.
        Hd = Fr(rng.randint(-97, 97), rng.randint(1, 97))
        rho_pi = 3 * H**2 / (8 * G)
        rhod_pi = 6 * H * Hd / (8 * G)
        p_pi = -rho_pi - rhod_pi / (3 * H)
        ok_nodyn &= (H**2 == Fr(8, 3) * G * rho_pi) and (Hd == -4 * G * (rho_pi + p_pi))
        # (d) Read as a running vacuum rho(H) = rho(H0) + 3 nu (H^2 - H0^2)/(8 pi G): nu = 1.
        H0 = rq()
        nu = (3 * H**2 / (8 * G) - 3 * H0**2 / (8 * G)) / (3 * (H**2 - H0**2) / (8 * G)) if H != H0 else Fr(1)
        ok_nu &= (nu == 1)
        # (e) Kodama-Hayward temperature T_A = (H/2pi)(1 + Hdot/(2H^2)) on the apparent horizon:
        #     rho_A = S T_A / V_A = 3(H^2 + Hdot/2)/(8 pi G) = (rho_tot - 3 p_tot)/4.
        rhoA_pi = 3 * (H**2 + Hd / 2) / (8 * G)
        S_over_pi = 1 / (G * H**2)                 # S/pi = R_A^2/G
        TA_times_pi = (H / 2) * (1 + Hd / (2 * H**2))
        VA_over_pi = Fr(4, 3) / H**3
        ok_kod &= (S_over_pi * TA_times_pi / VA_over_pi == rhoA_pi)
        ok_kod &= (rhoA_pi == (rho_pi - 3 * p_pi) / 4)
        # (f) As a separately conserved component with conserved matter:
        #     Omega = (1 - 3 w Omega)/4  =>  w = (1 - 4 Omega)/(3 Omega);  dOmega/dlna = (1-Omega)(4 Omega-1).
        Om = Fr(rng.randint(1, 96), 97)
        w = (1 - 4 * Om) / (3 * Om)
        ok_kod_ode &= (Om == (1 - 3 * w * Om) / 4)
        ok_kod_ode &= (-3 * w * Om * (1 - Om) == (1 - Om) * (4 * Om - 1))
        # (g) Event horizon, rho = 3 c^2/(8 pi G R_E^2), w = -1/3 - 2 sqrt(Omega)/(3c):
        #     dOmega/dlna = -3 w Omega (1-Omega) = Omega (1-Omega)(1 + 2 sqrt(Omega)/c).
        s = Fr(rng.randint(1, 96), 97)
        c = rq()
        w_li = Fr(-1, 3) - 2 * s / (3 * c)
        ok_li_ode &= (-3 * w_li * s**2 * (1 - s**2) == s**2 * (1 - s**2) * (1 + 2 * s / c))
        # (h) Exact de Sitter (R_E = R_A = 1/H, Omega = 1): Friedmann requires c^2 = 1, then w = -1.
        #     E = integral T dS = 2 S T doubles rho, i.e. c^2 = 2, and violates H^2 = 8 pi G rho/3.
        rho_ST_pi = rho_times_pi(sigma, eps, G, RA, H)
        rho_2ST_pi = rho_times_pi(sigma, eps, G, RA, H, factor=2)
        ok_li_ds &= (Fr(8, 3) * G * rho_ST_pi == H**2) and (Fr(8, 3) * G * rho_2ST_pi == 2 * H**2)
        ok_li_ds &= (Fr(-1, 3) - Fr(2, 3) * 1 / 1 == -1)
    # integral of T dS with T = 1/(2 pi R), S = pi R^2/G: d(R/G)/dR = 1/G = T dS/dR; E = R/G = 2 S T.
    Rg, Gg = rq(), rq()
    ST = (Rg**2 / Gg) * (1 / (2 * Rg))            # pi cancels
    check("E=S*T with kappa=1/R gives rho = 3/(8 pi G R^2) (sigma, eps cancel)", ok_norm and ok_dimfree)
    check("Integral T dS from R=0 equals 2 S T for S ~ R^2, T ~ 1/R", Rg / Gg == 2 * ST)
    check("Misner-Sharp: S*T at R_A equals (4pi/3) R_A^3 rho_tot iff Friedmann", ok_ms)
    check("rho_s = rho_crit with conservation-defined p solves both Friedmann equations for any (H, Hdot)", ok_nodyn)
    check("rho_s read as running vacuum has nu = 1", ok_nu)
    check("Kodama-Hayward variant: rho_A = 3(H^2+Hdot/2)/(8piG) = (rho-3p)/4", ok_kod)
    check("Kodama-Hayward separate component: w=(1-4Om)/(3Om), Om'=(1-Om)(4Om-1)", ok_kod_ode)
    check("Event-horizon rule: Om' = Om(1-Om)(1+2 sqrt(Om)/c)", ok_li_ode)
    check("Exact dS: E=S*T satisfies Friedmann, E=2ST gives 2 rho_crit; c^2=1 gives w=-1", ok_li_ds)


# ---------------------------------------------------------------- numerical curves
def rk4(f, y, x0, x1, n):
    h = (x1 - x0) / n
    x = x0
    out = [(x, y)]
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h / 2 * k1)
        k3 = f(x + h / 2, y + h / 2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        out.append((x, y))
    return out


def li_curve(Om0, c, xmin=-math.log(1 + 3.0), xmax=25.0, n=200000):
    f = lambda x, Om: Om * (1 - Om) * (1 + 2 * math.sqrt(max(Om, 0.0)) / c)
    back = rk4(f, Om0, 0.0, xmin, n)
    # forward in u = 1 - Om, which stays resolvable in floating point as Om -> 1
    g = lambda x, u: -(1 - u) * u * (1 + 2 * math.sqrt(max(1 - u, 0.0)) / c)
    fwd = rk4(g, 1 - Om0, 0.0, xmax, n)
    return back, fwd


def li_numerics():
    Om0 = 0.69  # supplied illustration value (E-class input), not fitted here
    rows = []
    for c in (1.0, math.sqrt(2.0)):
        back, fwd = li_curve(Om0, c)
        def Om_at(z):
            x = -math.log(1 + z)
            return min(back, key=lambda t: abs(t[0] - x))[1]
        ws = {z: -1 / 3 - 2 * math.sqrt(Om_at(z)) / (3 * c) for z in (0.0, 0.5, 1.0, 2.0, 3.0)}
        rows.append((c, ws))
        # Independent control: rebuild H(a) from conserved matter, integrate R_E, compare with H R_E = c/sqrt(Om).
        # H^2/H0^2 = (1-Om0) a^-3 / (1-Om(a)).
        num = 0.0
        prev = None
        for (x, u) in fwd:
            a = math.exp(x)
            E = math.sqrt((1 - Om0) * a ** -3 / u)
            integrand = 1.0 / (a * E)  # dt/a = dx/(a H); R_E(a=1) = int_0^inf dx/(a E)
            if prev is not None:
                num += 0.5 * (prev[1] + integrand) * (x - prev[0])
            prev = (x, integrand)
        print(f"Event-horizon rule c^2={c*c:.0f}: w(z) at z=0,0.5,1,2,3 = " +
              ", ".join(f"{ws[z]:+.4f}" for z in (0.0, 0.5, 1.0, 2.0, 3.0)) +
              f"; H0 R_E0 by quadrature = {num:.5f}, closed form c/sqrt(Om0) = {c/math.sqrt(Om0):.5f}")
        check(f"numerical control c^2={c*c:.0f}: quadrature H0 R_E0 matches c/sqrt(Om0) to 1e-4",
              abs(num - c / math.sqrt(Om0)) < 1e-4)
        if c == 1.0:
            # local running-vacuum slope along the trajectory at z=0: nu_eff = d(Om H^2)/d(H^2)
            w0 = ws[0.0]
            dOm = Om0 * (1 - Om0) * (1 + 2 * math.sqrt(Om0) / c)
            dlnH2 = -3 * (1 + w0 * Om0)
            nu_eff = Om0 + dOm / dlnH2
            print(f"Event-horizon rule c^2=1: local slope nu_eff = d(rho)/d(3H^2/8piG) at z=0 = {nu_eff:.4f}")
    return rows


def lcdm_horizons():
    Om = 0.31  # supplied illustration value
    OL = 1 - Om
    E = lambda a: math.sqrt(Om * a ** -3 + OL)
    def chiE(a0, n=400000, xmax=40.0):
        # comoving event horizon from a0: int_{a0}^inf da/(a^2 E) = int_{ln a0}^{xmax} dx/(a E)
        x0 = math.log(a0)
        h = (xmax - x0) / n
        s = 0.0
        for k in range(n + 1):
            x = x0 + k * h
            a = math.exp(x)
            f = 1.0 / (a * E(a))
            s += f * (0.5 if k in (0, n) else 1.0)
        return s * h
    RE0 = chiE(1.0)
    print(f"LCDM (Om=0.31): H0 R_E0 = {RE0:.4f} (apparent horizon H0 R_A = 1)")
    for z in (1.0, 2.0):
        a = 1 / (1 + z)
        REz = a * chiE(a)
        hub = E(a)
        evt = RE0 / REz
        print(f"LCDM z={z:.0f}: H(z)/H0 = {hub:.4f}; R_E0/R_E(z) = {evt:.4f}; "
              f"log10 ratio of the two a0(z) scalings = {math.log10(hub/evt):+.4f}")
    check("LCDM event horizon exceeds the apparent horizon today (control on the R_E vs R_A distinction)", RE0 > 1.0)


def main():
    exact_identities()
    li_numerics()
    lcdm_horizons()
    ok = all(o for _, o in RESULTS)
    print("ALL CHECKS", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
