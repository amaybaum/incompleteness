"""EQ4-P probe p10 -- c = 1: the maximality certificate for the all-twin world, exact.  Research only.

Usage:  python3 -I -B p10_c1_maximality.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py (and sympy for one symbolic identity).

For c = 1 every K3 is Euclidean self-dual (K3 = K3*, twin links) and contains B_tw (so W3, p1 T5).  F, G (p1 T1: in
B_tw*, tr(FG) = -1/2) are GHZ-diagonal; if they are also nonnegative on Z = {X : PT_j(X) PSD, j = 1,2,3}, then a
self-dual K3 inside cone(B_tw u Z) would contain F and G (K3 = K3* contains cone(B_tw u Z)*) and violate its own
self-positivity.  So c = 1 completions must also leave cone(B_tw u Z).

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P10-C1-MAXIMALITY-EXACT` iff all:
  K  transcription control.
  F  (F1) F and G commute with the GHZ stabilizer generators X(x)X(x)X, Z(x)Z(x)1, 1(x)Z(x)Z (GHZ-diagonal) and their
     fibre coordinates are F: (P, C) = (0, 2) on fibre 00 and (1, 0) elsewhere, G: (0, -2) and (1, 0) (exact);
     (F2) for symbolic z in Z^GD: 2<F, z> = (P_01 + C_00) + (P_10 + C_00) + P_11 and
     2<G, z> = (P_01 - C_00) + (P_10 - C_00) + P_11 (symbolic), nonnegative combinations of the Z^GD inequalities
     (p8 Z3); (F3) tr(F G) < 0; (F4) control: W3 is in Z and in B_tw and pairs nonnegatively with F and G.
"""
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p10_c1_maximality")
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)
P6 = L.identity(X3) - L.ket_op(L.basis_vec([0, 0, 0]), X3) - L.ket_op(L.basis_vec([1, 1, 1]), X3)
XC = L.Op(X3, {(0, 7): L.ONE, (7, 0): L.ONE})
F = P6.scale(Fr(1, 2)) + XC
Gm = P6.scale(Fr(1, 2)) - XC
XXX = L.tensor(L.op(L.SX, (0,)), L.op(L.SX, (1,)), L.op(L.SX, (2,)))
ZZ1 = L.tensor(L.op(L.SZ, (0,)), L.op(L.SZ, (1,)), L.op(L.S0, (2,)))
ZZ2 = L.tensor(L.op(L.S0, (0,)), L.op(L.SZ, (1,)), L.op(L.SZ, (2,)))
fib = [(0, 0), (0, 1), (1, 0), (1, 1)]


def fibre_coords(M):
    out = []
    for (b1, b2) in fib:
        lo = 2 * b1 + b2
        hi = 4 + 2 * (1 - b1) + (1 - b2)
        P = M.get(lo, lo) + M.get(hi, hi)
        C = M.get(lo, hi) + M.get(hi, lo)
        out.append((P, C))
    return out


comm = all(L.matmul(S, M) == L.matmul(M, S) for S in (XXX, ZZ1, ZZ2) for M in (F, Gm))
cf, cg = fibre_coords(F), fibre_coords(Gm)
rep.check("F1 F, G are GHZ-diagonal; fibre coordinates F: %s, G: %s" % ([(str(a), str(b)) for a, b in cf],
                                                                      [(str(a), str(b)) for a, b in cg]),
          comm and cf == [(L.G(0), L.G(2)), (L.G(1), L.G(0)), (L.G(1), L.G(0)), (L.G(1), L.G(0))]
          and cg == [(L.G(0), L.G(-2)), (L.G(1), L.G(0)), (L.G(1), L.G(0)), (L.G(1), L.G(0))])
pz = sp.symbols("q0:4", real=True)
cz = sp.symbols("d0:4", real=True)
twoF = sum(int(cf[i][0].re) * pz[i] + int(cf[i][1].re) * cz[i] for i in range(4))
twoG = sum(int(cg[i][0].re) * pz[i] + int(cg[i][1].re) * cz[i] for i in range(4))
rep.check("F2 2<F,z> = (P_01 + C_00) + (P_10 + C_00) + P_11 and 2<G,z> = (P_01 - C_00) + (P_10 - C_00) + P_11 "
          "(symbolic): F, G are nonnegative on Z^GD, hence (twirl) on Z",
          sp.expand(twoF - ((pz[1] + cz[0]) + (pz[2] + cz[0]) + pz[3])) == 0
          and sp.expand(twoG - ((pz[1] - cz[0]) + (pz[2] - cz[0]) + pz[3])) == 0)
tFG = L.pair(F, Gm)
rep.check("F3 tr(F G) = %s < 0" % tFG, tFG.im == 0 and tFG.re < 0)
W3 = L.w3(X3)
inZ = all(L.psd(L.ptranspose(W3, [q]))[0] for q in X3)
rep.check("F4 control: W3 is in Z (PT_j PSD); tr(W3 F) = %s, tr(W3 G) = %s >= 0" % (L.pair(W3, F), L.pair(W3, Gm)),
          inZ and L.pair(W3, F).re >= 0 and L.pair(W3, Gm).re >= 0)

rep.verdict("P10-C1-MAXIMALITY-EXACT")
