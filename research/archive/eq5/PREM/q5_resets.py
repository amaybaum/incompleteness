"""EQ5-PREM q5 — operation-level token identity for irreversible token operations (discard-and-prepare, "resets"),
against every countermodel, and the exact ingredient of its route to TokProdState.  An (o)-type candidate: it posits
operations on one token of the four-token composite.  Research only; nothing here is adopted.

Usage:  python3 -I -B q5_resets.py

Setting and conventions as q1 (COMP-1 coordinate carrier C = 17 x 17; iota, pi, R, sigma; twists rho, theta, tau).
The reset of token t to the unit Bloch vector s acts on four-token tables by
    (Res_{t,s} Z)_I = Z_{I with I_t := 0} * hom(s)_{I_t}
(discard token t, then prepare s), and on pair tables by the same rule on the token's index.  Its A-layout action on the
carrier is lift(Res_{t,s}) = iota Res pi + (id - iota pi).

OLTIres (the candidate): for every token t and every pure s there is an affine self-map Gamma of V with Gamma(Omega) in
Omega that resets token t to s in every PA product (A-covariance) and in every PB product (B-covariance).

DECISION RULE (fixed before the first run; rules, not expected numbers):
 C1 control: in M_sig, lift(Res_{t,s}) satisfies A- and B-covariance for every token t and every s in the test set
    (symbolic normalized pair tables).
 C2 forcing: in every C-carrier model (M_sig, M_rho, M_tw, M_id, M_T, M_th) the A-products of normalized pair tables are
    iota of their four-token tables (symbolic), so the A-covariance of an affine Gamma determines it on the normalized slice
    of iota(W4), which contains the B-products (q1); hence OLTIres HOLDS in such a model iff lift(Res_{t,s}) satisfies
    B-covariance for all t, s, and FAILS at the first (t, s) where it does not.
 C3 anchor sum (C x C): with a0 = b0 = c, the point (c, c) lies on both the A-slice and the B-slice; A-covariance forces
    Gamma(c, c) = (Res_A c, c) and B-covariance forces Gamma(c, c) = (c, Res_B c); OLTIres FAILS iff for some (t, s) the
    two values differ (exact), for both members ANCc (c = centre) and ANCz (c = all +z).
 D  route ingredient: the composite of the four resets maps iota(Z) to Z_0000 iota(H(s)) (symbolic Z), so it is constant
    on the normalized slice; hence, where the B-products lie in the affine span of the A-products, B-covariance of the
    composite gives pB(s) = pA(s) for every pure s (TokProdState on pure products, then on all products by
    multi-affinity) [W with this exact ingredient].
 VERDICT Q5-RESETS-EXACT iff C1, C2's symbolic identities, C3's evaluations and D pass (the per-model HOLDS / FAILS is
 then printed as a result, with the REFUTATION table: "OLTIres => G" is REFUTED by a model iff OLTIres HOLDS and G FAILS
 there, G in {tok, TPS}, using q1's verdicts that G FAILS in every countermodel).  Exact arithmetic only; no timing.
"""
import itertools
import sys

import sympy as sp

CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


R4 = range(4)
N16 = range(16)
N17 = range(17)
I4 = list(itertools.product(R4, R4, R4, R4))
Z0, O1 = sp.Integer(0), sp.Integer(1)
S_RHO = [1, 1, -1, 1]
S_TH = [1, -1, -1, -1]


def zero(e):
    return sp.expand(e) == 0


def hom16(x):
    return [O1] + list(x)


def pState(x, y):
    hx, hy = hom16(x), hom16(y)
    return [[hx[m] * hy[n] for n in N17] for m in N17]


def flat(T):
    return [T[m][n] for m in R4 for n in R4]


def unflat(v):
    return [[v[4 * m + n] for n in R4] for m in R4]


def ceq(u, v):
    return all(zero(u[m][n] - v[m][n]) for m in N17 for n in N17)


def cadd(u, v):
    return [[u[m][n] + v[m][n] for n in N17] for m in N17]


def csub(u, v):
    return [[u[m][n] - v[m][n] for n in N17] for m in N17]


def iota(Z):
    V = [[Z0] * 17 for _ in N17]
    for a, b, c, d in I4:
        V[1 + 4 * a + b][1 + 4 * c + d] = Z[(a, b, c, d)]
    for c, d in itertools.product(R4, R4):
        V[0][1 + 4 * c + d] = Z[(0, 0, c, d)]
    for a, b in itertools.product(R4, R4):
        V[1 + 4 * a + b][0] = Z[(a, b, 0, 0)]
    V[0][0] = Z[(0, 0, 0, 0)]
    return V


def piV(V):
    return {(a, b, c, d): V[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in I4}


def lift(F):
    def g(V):
        Z = piV(V)
        return cadd(csub(V, iota(Z)), iota(F(Z)))
    return g


def Rg(Z):
    return {(a, b, c, d): Z[(a, c, b, d)] for a, b, c, d in I4}


sigma = lift(Rg)


def twistT(signs, x):
    return [x[i] * signs[i % 4] for i in N16]


TAU = [4 * (k % 4) + k // 4 for k in N16]


def tau_f(x):
    return [x[TAU[i]] for i in N16]


def h3(x):
    return [O1] + [sp.sympify(v) for v in x]


def res4(t, s):
    hs = h3(s)

    def F(Z):
        out = {}
        for I in I4:
            J = list(I)
            J[t] = 0
            out[I] = Z[tuple(J)] * hs[I[t]]
        return out
    return F


def res_pair(pos, s, x):
    """reset the first (pos 0) or second (pos 1) token of a flat pair vector to s"""
    T = unflat(x)
    hs = h3(s)
    if pos == 0:
        T2 = [[T[0][n] * hs[m] for n in R4] for m in R4]
    else:
        T2 = [[T[m][0] * hs[n] for n in R4] for m in R4]
    return flat(T2)


A_POS = {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1, 1)}
B_POS = {0: (0, 0), 2: (0, 1), 1: (1, 0), 3: (1, 1)}

MODELS = {
    "M_sig": (lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, Lp))),
    "M_rho": (lambda X, Y: pState(X, Y), lambda L, Lp: pState(L, twistT(S_RHO, Lp))),
    "M_tw": (lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, twistT(S_RHO, Lp)))),
    "M_th": (lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, twistT(S_TH, Lp)))),
    "M_id": (lambda X, Y: pState(X, Y), lambda L, Lp: pState(L, Lp)),
    "M_T": (lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(tau_f(L), Lp))),
}


def sym_ntab(name):
    return [[O1 if (m, n) == (0, 0) else sp.Symbol("%s%d%d" % (name, m, n)) for n in R4] for m in R4]


Xn, Yn, Ln, Lpn = sym_ntab("X"), sym_ntab("Y"), sym_ntab("L"), sym_ntab("M")
SS = [[0, 0, 1], [1, 0, 0], [0, 1, 0], [sp.Rational(3, 5), sp.Rational(4, 5), 0]]


def covariance(Ast, Bst, t, s):
    G = lift(res4(t, s))
    sa, pa = A_POS[t]
    X, Y = flat(Xn), flat(Yn)
    Xt = res_pair(pa, s, X) if sa == 0 else X
    Yt = res_pair(pa, s, Y) if sa == 1 else Y
    a_ok = ceq(G(Ast(X, Y)), Ast(Xt, Yt))
    sb, pb = B_POS[t]
    L, Lp = flat(Ln), flat(Lpn)
    Lt = res_pair(pb, s, L) if sb == 0 else L
    Lpt = res_pair(pb, s, Lp) if sb == 1 else Lp
    b_ok = ceq(G(Bst(L, Lp)), Bst(Lt, Lpt))
    return a_ok, b_ok


RES = {}
c1 = True
forced = True
for nm, (Ast, Bst) in MODELS.items():
    # C2 forcing identity: A-products of normalized pair tables are iota of their four-token tables
    gA = Ast(flat(Xn), flat(Yn))
    forced = forced and ceq(gA, iota(piV(gA)))
    verdict, why = True, "A- and B-covariance hold for every token and every listed s"
    for t in R4:
        for s in SS:
            a_ok, b_ok = covariance(Ast, Bst, t, s)
            if not a_ok:
                verdict, why = None, "A-covariance of lift(Res) fails (token %d, s = %s)" % (t, s)
                break
            if not b_ok:
                verdict, why = False, "B-covariance fails at token %d, s = %s (Gamma forced by A-covariance)" % (t, s)
                break
        if verdict is not True:
            break
    RES[nm] = (verdict, why)
    if nm == "M_sig":
        c1 = verdict is True
check("C1 control M_sig: lift(Res_{t,s}) is A- and B-covariant for every token and every listed s (symbolic pair tables)",
      c1)
check("C2 forcing: in every C-carrier model the A-products of normalized pair tables are iota of their four-token "
      "tables (symbolic)", forced)


# C3: the anchor sum members
def anchor_conflict(c_flat_pair):
    c = pState(c_flat_pair, c_flat_pair)
    for t in R4:
        for s in SS:
            GA = lift(res4(t, s))
            # in the second component the B-layout token t sits at A-layout token t' (same slot/position)
            tp = {(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}[B_POS[t]]
            GB = lift(res4(tp, s))
            if not ceq(GA(c), c) or not ceq(GB(c), c):
                return False, "token %d, s = %s: Res(c) != c, so the two forced values of Gamma(c, c) differ" % (t, s)
    return True, "no conflict at (c, c) for the listed (t, s)"


E00 = flat([[O1 if (m, n) == (0, 0) else Z0 for n in R4] for m in R4])
ZZ = flat([[h3([0, 0, 1])[m] * h3([0, 0, 1])[n] for n in R4] for m in R4])
anc_c = anchor_conflict(E00)
anc_z = anchor_conflict(ZZ)
RES["ANCc"] = (False if not anc_c[0] else None, anc_c[1])
RES["ANCz"] = (False if not anc_z[0] else None, anc_z[1])
check("C3 anchor sum: at the common point (c, c) the A- and B-forced values of Gamma differ for some (t, s), in both "
      "members ANCc and ANCz (exact)", not anc_c[0] and not anc_z[0])

# D: the route ingredient
Zs = {I: sp.Symbol("Z%d%d%d%d" % I) for I in I4}
s0 = [sp.Rational(3, 5), 0, sp.Rational(4, 5)]
comp = iota(Zs)
for t in R4:
    comp = lift(res4(t, s0))(comp)
Hs = {I: h3(s0)[I[0]] * h3(s0)[I[1]] * h3(s0)[I[2]] * h3(s0)[I[3]] for I in I4}
target = iota({I: Zs[(0, 0, 0, 0)] * Hs[I] for I in I4})
check("D the composite of the four resets maps iota(Z) to Z_0000 iota(H(s)) (symbolic Z, s = (3/5, 0, 4/5)): constant on "
      "the normalized slice", ceq(comp, target))

nfail = sum(1 for _, ok in CHECKS if not ok)
for nm in ["M_sig", "ANCc", "ANCz", "M_rho", "M_tw", "M_id", "M_T", "M_th"]:
    v, why = RES[nm]
    print("RESULT %-5s OLTIres %-5s  (%s)" % (nm, {True: "HOLDS", False: "FAILS", None: "N/A"}[v], why))
if nfail == 0:
    MM = {"ANC": ["ANCc", "ANCz"], "M_rho": ["M_rho"], "M_tw": ["M_tw"], "M_id": ["M_id"], "M_T": ["M_T"],
          "M_th": ["M_th"]}
    ref = [m for m, mem in MM.items() if any(RES[x][0] is True for x in mem)]
    for G in ("tok", "TPS"):
        print("REFUTATION OLTIres => %-3s : %s" % (G, ("REFUTED by " + ", ".join(ref)) if ref else "SURVIVES"))
print("--- q5_resets: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q5-RESETS-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
