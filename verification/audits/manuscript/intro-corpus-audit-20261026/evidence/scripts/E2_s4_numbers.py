#!/usr/bin/env python3
"""E2: the numbers behind Introduction section 4 (L140, L148).
(a) Weinberg 1989 Eq. (3.6): Lambda = (8 pi G)^(-1/2), <rho> = Lambda^4/(16 pi^2) = 2^-10 pi^-4 G^-2
    ~ 2e71 GeV^4 against |rho_V| <~ 1e-47 GeV^4 (Eq. 3.4): 118 decimal places; G^-2 instead: ~123.
    Also against the measured dark-energy density (Planck 2018 h, Omega_L; PDG rho_c).
(b) GR.md:366 / book ch07:193: (rho_QFT/rho_classical)/S_dS lies between 1/(96 pi^2) and 8/3.
    Exact symbolic factor over the conventions the book names: cutoff 1/eps = M_Pl/(2 sqrt(sigma))
    at sigma = 1, or M_Pl; zero-point normalization Lambda^4/(16 pi^2) or Lambda^4; with
    rho_classical the critical density 3H^2/(8 pi G) or H^2/G, and S_dS = pi/(G H^2) (hbar=c=k=1).
(c) The identity with measured values: (M_Pl^4/rho_L)/S_dS = (8/3)/Omega_L.
Inputs (PDG 2024 / Planck 2018): G/(hbar c) = 6.70883e-39 GeV^-2; rho_c = 8.0992e-47 h^2 GeV^4
(natural units, hbar=c=1, from rho_c = 1.05375e-5 h^2 GeV cm^-3); H0 = 2.1332e-42 h GeV;
h = 0.6736, Omega_L = 0.6847. Floating point is adequate: every claim is an order of magnitude
or a convention factor; the factors in (b) are exact (sympy).

Usage: python3 -I E2_s4_numbers.py [out.json]
"""
import json, math, os, sys
import sympy as sp

G = 6.70883e-39
MPl = G ** -0.5
lam_w = (8 * math.pi * G) ** -0.5
rho_w = lam_w ** 4 / (16 * math.pi ** 2)
rho_w_closed = 2 ** -10 * math.pi ** -4 * G ** -2
h, OmL = 0.6736, 0.6847
rho_L = OmL * 8.0992e-47 * h ** 2
H0 = 2.1332e-42 * h
S_dS = math.pi / (G * H0 ** 2)
out = {"(8piG)^-1/2_GeV": lam_w, "rho_Weinberg_GeV4": rho_w, "closed_form_agrees": abs(rho_w / rho_w_closed - 1) < 1e-12,
       "log10_rho_W_over_1e-47": math.log10(rho_w / 1e-47),
       "log10_Gm2_over_1e-47": math.log10(G ** -2 / 1e-47),
       "rho_Lambda_measured_GeV4": rho_L,
       "log10_rho_W_over_measured": math.log10(rho_w / rho_L),
       "log10_Gm2_over_measured": math.log10(G ** -2 / rho_L),
       "S_dS_present": S_dS,
       "(MPl^4/rho_L)/S_dS": (MPl ** 4 / rho_L) / S_dS, "(8/3)/Omega_L": (8 / 3) / OmL}
# (b) exact convention factors
Gs, Hs = sp.symbols("G H", positive=True)
M = Gs ** sp.Rational(-1, 2)
Ssym = sp.pi / (Gs * Hs ** 2)
fac = {}
for cut_name, cut in (("M_Pl/2", M / 2), ("M_Pl", M), ("(8piG)^-1/2 [Weinberg]", (8 * sp.pi * Gs) ** sp.Rational(-1, 2))):
    for norm_name, norm in (("/16pi^2", 1 / (16 * sp.pi ** 2)), ("x1", sp.Integer(1))):
        for cl_name, cl in (("3H^2/8piG", 3 * Hs ** 2 / (8 * sp.pi * Gs)), ("H^2/G", Hs ** 2 / Gs)):
            f = sp.simplify(cut ** 4 * norm / cl / Ssym)
            fac["%s, %s, %s" % (cut_name, norm_name, cl_name)] = str(f)
book = [k for k in fac if not k.startswith("(8piG)") and "3H^2" in k]
vals = {k: sp.sympify(fac[k]) for k in book}
out["convention_factors_exact"] = fac
out["book_conventions_min"] = str(min(vals.values(), key=lambda v: float(v)))
out["book_conventions_max"] = str(max(vals.values(), key=lambda v: float(v)))
out["range_1/(96pi^2)_to_8/3_reproduced"] = (sp.simplify(min(vals.values(), key=float) - 1 / (96 * sp.pi ** 2)) == 0
                                             and sp.simplify(max(vals.values(), key=float) - sp.Rational(8, 3)) == 0)
js = json.dumps(out, indent=1)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
