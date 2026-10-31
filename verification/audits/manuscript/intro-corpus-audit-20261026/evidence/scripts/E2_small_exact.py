#!/usr/bin/env python3
"""E2: independent exact checks of three small witnesses the Introduction relies on.
(1) L94 / Main.md:121: monotone total-variation distance is not sufficient for P-divisibility.
    For the two witness pairs of translation_probes.py, the unique divisor L = T1^-1 T2 has a
    negative entry, and d(pT2, qT2) <= d(pT1, qT1) for every pair p, q. The latter is decided
    exactly through a sufficient condition: L contracts every zero-sum vector in l1, i.e.
    max_{i<j} ||L_i - L_j||_1 / 2 <= 1 (the vertices of the zero-sum unit ball are (e_i - e_j)/2);
    then d(pT2, qT2) = ||(p - q) T1 L||_1/2 <= ||(p - q) T1||_1/2 = d(pT1, qT1).
(2) L106 / Main.md:330: Phi_t1 = Ad_H, Phi_t2 = id is CP-divisible (Lambda = Ad_H, H^2 = I)
    while the computational-basis populations J/2 -> I are P-indivisible. Exact over Q(sqrt 2).
(3) L66 / Main.md:534: for a permutation unitary, the table |U_ij|^p is the same for every p > 0.

Usage: python3 -I E2_small_exact.py [out.json]
"""
import json, os, sys
import sympy as sp
from fractions import Fraction as F

out = {}
W = {"n=2": ([[0, 1], [F(1, 2), F(1, 2)]], [[F(4, 5), F(1, 5)], [1, 0]]),
     "n=3": ([[F(2, 7), F(2, 7), F(3, 7)], [F(4, 7), F(5, 14), F(1, 14)], [F(1, 7), F(5, 14), F(1, 2)]],
             [[F(5, 14), F(2, 7), F(5, 14)], [F(2, 7), F(5, 14), F(5, 14)], [F(5, 14), F(5, 14), F(2, 7)]])}
for name, (T1, T2) in W.items():
    M1, M2 = sp.Matrix(T1).applyfunc(sp.nsimplify), sp.Matrix(T2).applyfunc(sp.nsimplify)
    n = M1.shape[0]
    stoch = all(sum(M[i, :]) == 1 and min(M[i, :]) >= 0 for M in (M1, M2) for i in range(n))
    L = M1.inv() * M2
    contr = max(sum(abs(L[i, k] - L[j, k]) for k in range(n)) for i in range(n) for j in range(i + 1, n)) / 2
    out["L94 " + name] = {"stochastic_pair": stoch, "det_T1": str(M1.det()), "min_divisor_entry": str(min(L)),
                          "no_stochastic_divisor": min(L) < 0, "zero_sum_contraction_norm": str(contr),
                          "TV_monotone_all_pairs": contr <= 1}
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
x = sp.Matrix(2, 2, sp.symbols("r0:4"))
AdH = lambda r: H * r * H.T
pops = lambda ch: sp.Matrix(2, 2, lambda i, j: ch(sp.Matrix(2, 2, lambda a, b: int(a == b == i)))[j, j])
T1 = pops(AdH); T2 = pops(lambda r: r)
out["L106 Hadamard"] = {"H^2 = I": sp.simplify(H * H - sp.eye(2)) == sp.zeros(2),
                        "Phi_t2 = AdH o Phi_t1 (CP-divisible)": sp.simplify(AdH(AdH(x)) - x) == sp.zeros(2),
                        "T(t1) = J/2": T1 == sp.Matrix([[sp.Rational(1, 2)] * 2] * 2), "T(t2) = I": T2 == sp.eye(2),
                        "T(t1) singular, so no Lambda with T(t1) Lambda = I": T1.det() == 0}
p = sp.symbols("p", positive=True)
P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
out["L66 |U|^p"] = {"permutation entries 0/1: |U|^p == |U|^2 for p > 0":
                    all(sp.simplify(abs(e) ** p - abs(e) ** 2) == 0 for e in P)}
ok = all(v["no_stochastic_divisor"] and v["TV_monotone_all_pairs"] and v["stochastic_pair"] for k, v in out.items() if k.startswith("L94")) \
     and all(out["L106 Hadamard"].values()) and all(out["L66 |U|^p"].values())
out["all_ok"] = bool(ok)
js = json.dumps(out, indent=1, default=str)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
