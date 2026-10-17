#!/usr/bin/env python3
"""Independent review checks for Track C (C1 identities, CX1, CX2, C_W).

Written from scratch by the reviewer with SymPy exact arithmetic; imports nothing from trackC/.
Phi_1 = (5/8) Ad_(I (x) D) + (3/8) id, D = diag(1, (3+4i)/5), as in #832's check.py.

  G1   Gamma2 o Ad_(A(x)B) o Gamma2 = Ad_(A(x)conj B) for SYMBOLIC A, B (all 2x2 complex), on all
       16 matrix units: the identity behind "every local CP map preserves Gamma(Q3)".
  G2   Gamma2 o Phi_1 o Gamma2 = (5/8) Ad_(I(x)conj D) + (3/8) id.
  G3   CNOT |+0><+0| = Phi+ and Gamma2(Phi+) has eigenvalue -1/2 (so CNOT leaves Gamma Q3).
  CX1  L(Y) = Y - (1/2)Tr(Y) sigma: inverse X + Tr(X) sigma, Tr o L = (1/2) Tr for symbolic Y;
       frame 2P_i - sigma, effects (1/2)P_i + (1/2)Tr(P_i sigma) I; member |00><00| - I/20 with
       spectrum check; Phi_1 witness and the minimal eigenvalue of L^-1(Phi_1 L(|00><00|)).
  CX2  same for L2(Y) = Y + Tr(Y) sigma.
  CW   Tr(W rho) = 0, Tr(W Phi_1 rho) = -1/4, Tr(W Ad rho) = -2/5; [W, rho_bad] = 0; the spectrum of
       M_w rho_bad as exact linear functions of w, pairwise coincidences only outside [0, 2),
       positivity on [0, 2); Phi+ is the eigenvector carrying the top line and is outside C_W.
"""
import itertools
import sys

import sympy as sp

OUT = []


def rec(ok, cid, text):
    OUT.append((bool(ok), cid, text))


I = sp.I
E2 = sp.eye(2)
E4 = sp.eye(4)
X = sp.Matrix([[0, 1], [1, 0]])
Yp = sp.Matrix([[0, -I], [I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
lam = (3 + 4 * I) / 5
D = sp.diag(1, lam)
UD = sp.kronecker_product(E2, D)


def kr(a, b):
    return sp.kronecker_product(a, b)


def ad(U, M):
    return U * M * U.H


def phi1(M):
    return sp.Rational(5, 8) * ad(UD, M) + sp.Rational(3, 8) * M


def pt2(M):
    """partial transpose on token 2, index 2*a1 + a2."""
    return sp.Matrix(4, 4, lambda r, c: M[2 * (r // 2) + (c % 2), 2 * (c // 2) + (r % 2)])


def zero(M):
    return sp.simplify(sp.expand(M)) == sp.zeros(*M.shape)


def units():
    for i, j in itertools.product(range(4), repeat=2):
        E = sp.zeros(4, 4)
        E[i, j] = 1
        yield E


def ket(*v):
    return sp.Matrix(v)


def proj(v):
    return v * v.H


def qf(M, v):
    return sp.nsimplify(sp.simplify((v.H * M * v)[0]))


# ---------------------------------------------------------------- G
def sec_g():
    a = sp.symbols('a0:4', real=True)
    b = sp.symbols('b0:4', real=True)
    c = sp.symbols('c0:4', real=True)
    d = sp.symbols('d0:4', real=True)
    A = sp.Matrix(2, 2, [a[i] + I * b[i] for i in range(4)])
    B = sp.Matrix(2, 2, [c[i] + I * d[i] for i in range(4)])
    ok = all(zero(pt2(ad(kr(A, B), pt2(E))) - ad(kr(A, B.conjugate()), E)) for E in units())
    rec(ok, "G1", "Gamma2(Ad_(A(x)B)(Gamma2 E)) = Ad_(A(x)conj B)(E) for symbolic complex A, B on all 16 units")
    ok = all(zero(pt2(phi1(pt2(E))) - (sp.Rational(5, 8) * ad(kr(E2, D.conjugate()), E) + sp.Rational(3, 8) * E)) for E in units())
    rec(ok, "G2", "Gamma2 o Phi_1 o Gamma2 = (5/8) Ad_(I(x)conj D) + (3/8) id on all 16 units")
    CN = sp.diag(1, 1, 0, 0) + kr(sp.diag(0, 1), X)
    plus0 = kr(ket(1, 1), ket(1, 0)) / sp.sqrt(2)
    bell = ad(CN, proj(plus0))
    phip = proj(ket(1, 0, 0, 1)) / 2
    ev = pt2(bell).eigenvals()
    rec(zero(bell - phip) and min(ev) == sp.Rational(-1, 2), "G3",
        f"CNOT|+0><+0|CNOT = Phi+, spectrum of Gamma2(Phi+) = {dict(ev)}: CNOT maps SEP outside Gamma(Q3)")


# ---------------------------------------------------------------- CX
SIG = (E4 + sp.Rational(1, 2) * kr(E2, X)) / 4


def sec_cx():
    ys = sp.symbols('y0:16')
    Ysym = sp.Matrix(4, 4, ys)

    def L(M):
        return M - sp.Rational(1, 2) * M.trace() * SIG

    def Li(M):
        return M + M.trace() * SIG

    ok = zero(L(Li(Ysym)) - Ysym) and zero(Li(L(Ysym)) - Ysym) and sp.expand(L(Ysym).trace() - Ysym.trace() / 2) == 0
    ok &= min(SIG.eigenvals()) > 0 and SIG.trace() == 1 and not zero(ad(UD, SIG) - SIG)
    basis = [kr(ket(*(1 - i, i)), ket(*(1 - j, j))) for i in (0, 1) for j in (0, 1)]
    Pb = [proj(v) for v in basis]
    Xs = [2 * P - SIG for P in Pb]
    Es = [P / 2 + (P * SIG).trace() / 2 * E4 for P in Pb]
    ok &= zero(sum(Es, sp.zeros(4, 4)) - E4)
    ok &= all(sp.simplify((Es[j] * Xs[i]).trace()) == (1 if i == j else 0) for i in range(4) for j in range(4))
    ok &= all(zero(sp.Matrix([sp.expand((Es[j] * L(Ysym)).trace() - (Pb[j] * Ysym).trace() / 2)])) for j in range(4))
    ok &= all(Xi.trace() == 1 and min(Li(Xi).eigenvals()) >= 0 for Xi in Xs)
    rec(ok, "CX1-iso", "L, L^-1 inverse and Tr L(Y) = Tr(Y)/2 for symbolic Y; frame 2P_i - sigma (in C_sigma), effects pull back to P_j/2 for symbolic Y, sum to I, Tr(E_j X_i) = delta")
    Xbad = Pb[0] - E4 / 20
    evs = Li(Xbad).eigenvals()
    rec(min(evs) >= 0 and qf(Xbad, basis[3]) == sp.Rational(-1, 20), "CX1-out",
        f"spec(L^-1(|00><00| - I/20)) = {sorted(evs)} >= 0 (member), <11|.|11> = {qf(Xbad, basis[3])}: C_sigma not in maxCone")
    Xm = L(Pb[0])
    Mout = Li(phi1(Xm))
    u = kr(ket(0, 1), ket(1, I))
    v = qf(Mout, u)
    mineig = min(sp.Poly(sp.simplify(Mout.charpoly().as_expr()), sp.Symbol('lambda')).nroots(n=30), key=lambda z: sp.re(z))
    rec(v == sp.Rational(-1, 16) and sp.re(mineig) < 0, "CX1-phi",
        f"<u|L^-1 Phi_1 L(|00><00|)|u> = {v} for u = |1>(1,i) (norm^2 2); min eigenvalue ~ {sp.N(sp.re(mineig), 8)} (float, sign only)")

    def L2(M):
        return M + M.trace() * SIG

    def M2(M):
        return M - sp.Rational(1, 2) * M.trace() * SIG

    ok = zero(M2(L2(Ysym)) - Ysym) and zero(L2(M2(Ysym)) - Ysym)
    ok &= min(M2(Pb[0]).eigenvals()) < 0
    X2 = Pb[0] + SIG
    ok &= zero(M2(X2) - Pb[0])
    u2 = kr(ket(0, 1), ket(1, -I))
    v2 = qf(M2(phi1(X2)), u2)
    rec(ok and v2 == sp.Rational(-1, 8), "CX2",
        f"C'_sigma = L2(Q3) (symbolic inverse), |00><00| not a member, X2 = |00><00| + sigma a member, <u'|M2(Phi_1 X2)|u'> = {v2}")


# ---------------------------------------------------------------- CW
def sec_cw():
    phip = proj(ket(1, 0, 0, 1)) / 2
    phim = proj(ket(1, 0, 0, -1)) / 2
    W = E4 / 2 - phip
    chi = ket(1, 0, 0, -I) / sp.sqrt(2)
    rho = proj(chi)
    v0 = sp.simplify((W * rho).trace())
    v1 = sp.simplify((W * phi1(rho)).trace())
    v2 = sp.simplify((W * ad(UD, rho)).trace())
    rec(v0 == 0 and v1 == sp.Rational(-1, 4) and v2 == sp.Rational(-2, 5), "CW-phi",
        f"Tr(W rho) = {v0}, Tr(W Phi_1 rho) = {v1}, Tr(W Ad rho) = {v2}")
    # product fidelity bound used for SEP <= C_W: |<ab|Phi+>|^2 = |a0 b0 + a1 b1|^2/2 <= |a|^2|b|^2/2
    e01 = proj(ket(0, 1, 0, 0))
    e10 = proj(ket(0, 0, 1, 0))
    rb = sp.Rational(2, 5) * phip + sp.Rational(3, 10) * e01 + sp.Rational(1, 5) * e10 + sp.Rational(1, 10) * phim
    w = sp.symbols('w', real=True)
    Mw = E4 - w * W
    ok = zero(W * rb - rb * W) and rb.trace() == 1 and min(rb.eigenvals()) > 0 and (W * rb).trace() == sp.Rational(1, 10)
    Zw = sp.expand(Mw * rb)
    evs = Zw.eigenvals()
    lines = sorted(evs.keys(), key=lambda e: sp.Poly(e, w).all_coeffs()[-1])
    pairs_ok = True
    roots = []
    for e1, e2 in itertools.combinations(lines, 2):
        diff = sp.expand(e1 - e2)
        sol = sp.solve(sp.Eq(diff, 0), w)
        roots.append(sol)
        pairs_ok &= all(not (0 <= s < 2) for s in sol) and diff != 0
    pos_ok = all(all(sp.Poly(e, w).eval(x) > 0 for x in (0, 2)) or (sp.Poly(e, w).eval(0) > 0 and sp.Poly(e, w).eval(2) >= 0) for e in lines)
    # Phi+ eigenvector carries the line 2/5 + w/5; Phi+ itself violates the cut
    vphi = ket(1, 0, 0, 1)
    top = sp.expand((vphi.H * Zw * vphi)[0] / 2)
    ok &= pairs_ok and pos_ok and zero(Zw * vphi - top * vphi) and qf(W, vphi / sp.sqrt(2)) == sp.Rational(-1, 2)
    rec(ok, "CW-SP",
        f"[W, rho_bad] = 0; spec(M_w rho_bad) = {lines} (exact, symbolic w); pairwise coincidences at w in {roots} (none in [0,2)); "
        f"all lines > 0 on [0,2) (linear, endpoint check); Phi+ eigenvector with line {top}; <Phi+|W|Phi+> = -1/2")


def main():
    sec_g()
    sec_cx()
    sec_cw()
    for ok, cid, text in OUT:
        print(("PASS " if ok else "FAIL ") + cid + "  " + text)
    nf = sum(1 for ok, _, _ in OUT if not ok)
    print(f"checks: {len(OUT)}, failures: {nf}")
    return 0 if nf == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
