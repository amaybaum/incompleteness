"""EQ3-P probe p6 -- cheaper exact certificates for two exclusions (own code).  Research only; base bcbc516f.
Usage (from scratchpad/eq3/P): python3 -I -B p6_cheap_foils.py <base>/.../OIBridge/CompositeDimension.lean

CLAIMS:
  H1 the native group H = <cnot, actC nflip, actT nflip> has order 8 (closure on tables); every element is a signed
     permutation fixing the unit entry; cnot is in H
  H2 C_H := cone(H . products) is admissible (products inside; inside Q3 since every generator is Ad of a unitary:
     cnot = Ad CNOT, actC nflip = Ad(X (x) 1), actT nflip = Ad(1 (x) X) in the Pauli dictionary), closed (finite union of
     compact images, written), cnot-invariant (cnot in H), and Delta = cnot(prodState xplus z3) is in C_H
  H3 psi = (1,1,1,2)/sqrt7: the H-orbit of psi psi^dag has max marginal Bloch norm^2 = 45/49 <= (24/25)^2, so
     w = effect table of (49/50) 1 - psi psi^dag is in C_H* (8 orbit elements; Schmidt bound, written); f = effect table of
     psi psi^dag is in C_H* (PSD); the four-copy value <w, Delta.f.Delta> = -1/200 < 0: C_H violates KT(4; 01|23, 02|13)
     with an 8-element certificate (the K_F foil of p2 needs 11520)
  M1 own recheck of the six-copy exclusion of the biseparable hull BS (c = 0; EQ2-A D4): with Bell links on 03, 14, 25
     and effects w3 = effect table of 1/2 - GHZ (in BS*: <bisep|w3|bisep> >= 0 by the overlap bound 1/2, written) on
     012 and g3 = effect table of GHZ (PSD) on 345, the family-(ii3) value is <w3, T3 g3> = tr((1/2 - GHZ) GHZ^T)/8 < 0
     (exact); control: with g3 replaced by a biseparable state the value is >= 0
DECISION RULE (fixed before the first run): verdict `P6-CHEAP-FOILS-EXACT` iff all pass.  Exact arithmetic only.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check = L.check
cnot = L.cnot_from(L.parse_cnot(sys.argv[1]))
DEL = L.DELTA
Wv = Matrix(4, 4, lambda m, n: sp.Symbol(f"w{m}{n}", real=True))
gens = [("cnot", cnot, L.CNOT_U), ("actC nflip", lambda w: L.actC(L.NFLIP, w), L.kron(L.SX, L.S0)),
        ("actT nflip", lambda w: L.actT(L.NFLIP, w), L.kron(L.S0, L.SX))]
okad = all(L.zero(L.pauliW(g(Wv)) - (U * L.pauliW(Wv) * U.H).applyfunc(sp.expand)) for _, g, U in gens)


def key(M):
    return tuple(M[m, n] for m in range(4) for n in range(4))


# closure of H acting on tables, represented by images of the 16 basis tables
def as_perm(g):
    cols = []
    for k in range(16):
        Eb = zeros(4, 4)
        Eb[k // 4, k % 4] = 1
        img = g(Eb)
        nz = [(i, img[i // 4, i % 4]) for i in range(16) if img[i // 4, i % 4] != 0]
        cols.append((nz[0][0], int(nz[0][1])))
    return tuple(cols)


def comp(p, q):
    return tuple((p[i][0], p[i][1] * s) for (i, s) in q)


IDP = tuple((k, 1) for k in range(16))
gp = [as_perm(g) for _, g, _ in gens]
seen, frontier = {IDP}, [IDP]
while frontier:
    nxt = []
    for h in frontier:
        for g in gp:
            c = comp(g, h)
            if c not in seen:
                seen.add(c)
                nxt.append(c)
    frontier = nxt
H = list(seen)
check("H1 H = <cnot, actC nflip, actT nflip> has order 8, every element fixes the unit entry, and cnot is in H",
      len(H) == 8 and all(p[0] == (0, 1) for p in H) and as_perm(cnot) in seen, len(H))
check("H2 each generator is Ad of a unitary in the Pauli dictionary (symbolic): cnot = Ad CNOT, actC nflip = "
      "Ad(X (x) 1), actT nflip = Ad(1 (x) X); hence C_H <= Q3, and Delta = cnot(prodState xplus z3) is in C_H",
      okad and cnot(L.prod_state(L.XPLUS, L.Z3)) == DEL)


def act(p, vec):
    out = [Fr(0)] * 16
    for k in range(16):
        if vec[k] != 0:
            i, s = p[k]
            out[i] += s * vec[k]
    return out


psi = Matrix([1, 1, 1, 2])
rho = psi * psi.T / 7
fv = [Fr(int(sp.numer(x)), int(sp.denom(x))) for x in key(L.coordsW(rho))]
r2 = [sum(act(p, fv)[4 * k] ** 2 for k in (1, 2, 3)) / act(p, fv)[0] ** 2 for p in H]
Wop = R(49, 50) * eye(4) - rho
w_eff, f_eff = L.coordsW(Wop) / 4, L.coordsW(rho) / 4
val = L.eucl(w_eff, DEL * f_eff * DEL)
check("H3 the H-orbit of psi psi^dag (8 elements) has max marginal Bloch norm^2 = 45/49 <= 576/625 (so w is in C_H*), "
      "and the four-copy value <w, Delta.f.Delta> = -1/200 < 0: C_H violates KT(4; 01|23, 02|13)",
      max(r2) == Fr(45, 49) and max(r2) <= Fr(576, 625) and val == R(-1, 200), f"max = {max(r2)}, value = {val}")

# ---------------------------------------------------------------- M1 six-copy exclusion of BS (c = 0)
IDX = list(itertools.product(range(4), repeat=3))


def coords3(op):
    return {t: sp.expand((op * L.kron(L.PAULI[t[0]], L.PAULI[t[1]], L.PAULI[t[2]])).trace()) for t in IDX}


def T3(Tb):
    return {t: L.SGNY[t[0]] * L.SGNY[t[1]] * L.SGNY[t[2]] * Tb[t] for t in IDX}


g = Matrix([1, 0, 0, 0, 0, 0, 0, 1])
GHZ = g * g.T / 2
w3 = {t: v / 8 for t, v in coords3(eye(8) / 2 - GHZ).items()}        # effect table: op = sum w3 sigma sigma sigma
g3 = {t: v / 8 for t, v in coords3(GHZ).items()}
v6 = sp.expand(sum(w3[t] * T3(g3)[t] for t in IDX))
bis = L.kron(Matrix([1, 0, 0, 1]) * Matrix([1, 0, 0, 1]).T / 2, Matrix([[1, 1], [1, 1]]) / 2)   # Phi+_01 (x) |+><+|_2
b3 = {t: v / 8 for t, v in coords3(bis).items()}
v6c = sp.expand(sum(w3[t] * T3(b3)[t] for t in IDX))
check("M1 six-copy exclusion of BS (own code): <w3, T3 g3> = tr((1/2 - GHZ) GHZ^T)/8 = -1/16 < 0 with w3 in BS* and "
      "g3 = GHZ in BS*; control: a biseparable state in place of GHZ gives >= 0",
      v6 == R(-1, 16) and v6 == sp.expand(((eye(8) / 2 - GHZ) * GHZ.T).trace() / 8) and v6c >= 0,
      f"value {v6}, control {v6c}")

ok = L.summary("p6_cheap_foils")
print("VERDICT " + ("P6-CHEAP-FOILS-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
