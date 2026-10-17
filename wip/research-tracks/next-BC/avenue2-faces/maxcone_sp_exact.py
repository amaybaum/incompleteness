#!/usr/bin/env python3
"""Avenue 2 (Track C): maxCone is not spectral; close product pairs are indistinguishable in every
domain cone; SEP + F is not spectral; maxCone is preserved by Phi_1.

Requires SymPy.  Self-contained: reads no file.  Run:  <python with sympy> -I maxcone_sp_exact.py

Definitions (frozen for this script).  A domain cone is a closed convex cone C with
SEP <= C <= BP on Herm(4) (BP = maxCone = block-positive cone), unit effect the trace.  Effects of C
are E in C* with I - E in C*.  A frame is a set of pure states (extreme rays, trace one) with
effects E_i, sum E_i <= I in the C* order, E_i(w_j) = delta_ij.  SP (BMU Postulate 1): every state is
a convex combination of a frame.  For C = BP, C* = SEP, so every effect E has E >= 0, Gamma(E) >= 0,
E <= I and Gamma(E) <= I (separable implies PPT; no converse is used).

Written argument (report, node C2.5) for the state w below, in the face B6 = W cap BP of
z = |ab><ab| + |a'b'><a'b'|:
  (1) frame members of w lie in W cap BP and are extreme there, so each is either rank one on
      S = span{ab, a'b'} (P-type) or Gamma of rank one on S' = span{a b*, a' b'*} (G-type);
  (2) P-type members are mutually orthogonal vectors of S, G-type members mutually orthogonal
      vectors of S'; ga(w) != 0 needs a P-type member, de(w) != 0 a G-type member;
  (3) two P-type members and one G-type member are impossible: E_3 <= I - P_S forces the G-type
      vector orthogonal to a b* and a' b'*, hence zero; by Gamma, one P-type and two G-type are
      impossible; so the frame is {psi, Gamma(phi)} and w = P + Q with the two summands rank one;
  (4) such a frame needs |<psi|cd>|^2 + |<phi|c d*>|^2 <= 1 for every unit product c (x) d.
Checks:
  RI    w = w(1, 1, (1+i)/3, (1-i)/3) satisfies sqrt(al be) = 1 > |ga| + |de| (relative interior).
  DEC   the decompositions w = P + Q (P rank one on S with coordinates (A1,B1,ga,0), Q = Gamma of
        rank one with (A2,B2,0,de)) are exactly A1 in {1/3, 2/3}: the quadratic's roots, and both
        identities P + Q = w hold, P = |psi><psi|/k, Q = Gamma(|u><u|)/k' (exact).
  VIOL  for each decomposition, at c (x) d = a (x) b: |<psi|ab>|^2/|psi|^2 + |<u|a b*>|^2/|u|^2 > 1.
  GAMMA <c(x)e|Gamma(M)|c(x)e> = <c(x)conj(e)|M|c(x)conj(e)> for symbolic c, e and every matrix unit M.
  CLOSE the indistinguishability lemma's two bounds on an instance with |<a|a'>|^2 + |<b|b'>|^2 > 1
        (a = (4,3)/5, a' = (3,4)/5, b = (5,12)/13, b' = (12,5i)/13): f(a,b') >= |<b|b'>|^2 = 7200/28561
        and f(a,b') <= 1 - |<a|a'>|^2 = 49/625 (exact values), which contradict each other.
  PHI   Phi_1 = (5/8) Ad_(I(x)D) + (3/8) id, D = diag(1, (3+4i)/5): Tr(Phi_1(X) Y) = Tr(X Phi_1*(Y)) on all
        matrix units, and Phi_1* maps every product projector to |c><c| (x) (a PSD matrix) (symbolic):
        Phi_1 preserves SEP's dual, maxCone.
  SEPF  for the face F at the pair (x, y) of the instance and the close pair (x', y'), W(z) cap W(z')
        = {0} (the combined 20 real conditions have exact rank 16): in SEP + F the face of z' is the
        segment, and SEP + F is not SP.
"""
import sys
import sympy as sp

MUT = set()
RESULTS = []
I = sp.I


def check(ok, cid, text):
    RESULTS.append((bool(ok), cid, text))


def ket(*v):
    return sp.Matrix(v)


def kron(u, v):
    return sp.Matrix([u[i] * v[j] for i in range(2) for j in range(2)])


def perp(v):
    return sp.Matrix([-sp.conjugate(v[1]), sp.conjugate(v[0])])


def outer(u, v):
    return u * v.H


def gamma2(M):
    out = sp.zeros(4, 4)
    for a1 in range(2):
        for a2 in range(2):
            for b1 in range(2):
                for b2 in range(2):
                    out[2 * a1 + a2, 2 * b1 + b2] = M[2 * a1 + b2, 2 * b1 + a2]
    return out


def herm_basis():
    B = []
    for i in range(4):
        for j in range(4):
            M = sp.zeros(4, 4)
            if i == j:
                M[i, i] = 1
            elif i < j:
                M[i, j] = 1
                M[j, i] = 1
            else:
                M[i, j] = I
                M[j, i] = -I
            B.append(M)
    return B


def w_coords(a, b, a2, b2, al, be, ga, de):
    ab, a2b2, ab2, a2b = kron(a, b), kron(a2, b2), kron(a, b2), kron(a2, b)
    return (al * outer(ab, ab) + be * outer(a2b2, a2b2) + ga * outer(ab, a2b2) + sp.conjugate(ga) * outer(a2b2, ab)
            + de * outer(ab2, a2b) + sp.conjugate(de) * outer(a2b, ab2))


def W_conditions(a, b, a2, b2):
    rows = []
    for (gm, dl) in [(perp(a), perp(b2)), (perp(a2), perp(b))]:
        p = kron(gm, dl)
        for q in [p, kron(perp(gm), dl), kron(gm, perp(dl))]:
            row = [sp.expand((q.H * M * p)[0, 0]) for M in herm_basis()]
            rows.append([sp.re(r) for r in row])
            rows.append([sp.im(r) for r in row])
    return rows


def nsq(v):
    return sp.nsimplify(sp.expand((v.H * v)[0, 0]))


def run():
    RESULTS.clear()
    a, b = ket(1, 0), ket(1, 0)
    a2, b2 = ket(sp.Rational(3, 5), sp.Rational(4, 5)), ket(sp.Rational(5, 13), sp.Rational(12, 13) * I)
    ga, de = (1 + I) / 3, (1 - I) / 3
    if "outside" in MUT:
        ga, de = (1 + I) / 2, (1 - I) / 2
    # ---- RI
    s2 = sp.nsimplify(sp.Abs(ga) + sp.Abs(de)) ** 2
    check(sp.simplify(1 - s2) > 0, "RI", f"(|ga| + |de|)^2 = {sp.simplify(s2)} < 1 = al be: w lies in the relative interior of B6")
    w = w_coords(a, b, a2, b2, 1, 1, ga, de)
    # ---- DEC
    A1 = sp.symbols("A1")
    g2, e2 = sp.nsimplify(sp.Abs(ga) ** 2), sp.nsimplify(sp.Abs(de) ** 2)
    roots = sp.solve(sp.Eq(-A1 ** 2 + (1 + g2 - e2) * A1 - g2, 0), A1)
    roots = sorted(roots, key=str)
    ab, a2b2 = kron(a, b), kron(a2, b2)
    abc, a2b2c = kron(a, b.conjugate()), kron(a2, b2.conjugate())
    okdec = set(roots) == {sp.Rational(1, 3), sp.Rational(2, 3)}
    decs = []
    for r in roots:
        A1v = r
        if "wrong_root" in MUT:
            A1v = r + sp.Rational(1, 10)
        B1v = g2 / A1v
        A2v, B2v = 1 - A1v, 1 - B1v
        psi = A1v * ab + sp.conjugate(ga) * a2b2
        u = A2v * abc + sp.conjugate(de) * a2b2c
        P = outer(psi, psi) / A1v
        Q = gamma2(outer(u, u)) / A2v
        okdec &= sp.expand(P - w_coords(a, b, a2, b2, A1v, B1v, ga, 0)) == sp.zeros(4, 4)
        okdec &= sp.expand(Q - w_coords(a, b, a2, b2, A2v, B2v, 0, de)) == sp.zeros(4, 4)
        okdec &= sp.expand(P + Q - w) == sp.zeros(4, 4)
        decs.append((A1v, psi, u))
    check(okdec, "DEC", f"the (1,1) decompositions of w are exactly A1 in {[str(x) for x in roots]}; for each, P = |psi><psi|/A1 and Q = Gamma(|u><u|)/A2 have the stated coordinates and sum to w")
    # ---- VIOL
    okv = True
    vals = []
    for A1v, psi, u in decs:
        cd, cdc = kron(a, b), kron(a, b.conjugate())
        if "weak_witness" in MUT:
            cd, cdc = kron(a, b2), kron(a, b2.conjugate())
        v1 = sp.nsimplify(sp.expand((psi.H * cd)[0, 0] * (cd.H * psi)[0, 0]) / nsq(psi))
        v2 = sp.nsimplify(sp.expand((u.H * cdc)[0, 0] * (cdc.H * u)[0, 0]) / nsq(u))
        tot = sp.nsimplify(v1 + v2)
        vals.append(tot)
        okv &= tot > 1
    check(okv, "VIOL", f"at the product a (x) b the frame condition |<psi|cd>|^2 + |<phi|c d*>|^2 <= 1 fails for both decompositions: values {[str(v) for v in vals]} > 1; with (1)-(3), w has no frame decomposition in maxCone, so maxCone is not SP")
    # ---- GAMMA
    c0, c1, e0, e1 = sp.symbols("c0 c1 e0 e1")
    c, e = ket(c0, c1), ket(e0, e1)
    okg = True
    for i in range(4):
        for j in range(4):
            M = sp.zeros(4, 4)
            M[i, j] = 1
            v = kron(c, e)
            vc = kron(c, e.conjugate())
            lhs = (v.H * gamma2(M) * v)[0, 0]
            rhs = (vc.H * M * vc)[0, 0]
            if "gamma_mut" in MUT:
                rhs = (v.H * M * v)[0, 0]
            okg &= sp.expand(lhs - rhs) == 0
    check(okg, "GAMMA", "<c(x)e|Gamma(M)|c(x)e> = <c(x)e*|M|c(x)e*> for symbolic c, e on all 16 matrix units")
    # ---- CLOSE
    ac, ac2 = ket(sp.Rational(4, 5), sp.Rational(3, 5)), ket(sp.Rational(3, 5), sp.Rational(4, 5))
    bc_, bc2 = ket(sp.Rational(5, 13), sp.Rational(12, 13)), ket(sp.Rational(12, 13), sp.Rational(5, 13) * I)
    if "not_close" in MUT:
        ac2 = ket(sp.Rational(-3, 5), sp.Rational(4, 5))
    oa = sp.nsimplify(sp.Abs((ac.H * ac2)[0, 0]) ** 2)
    ob = sp.nsimplify(sp.Abs((bc_.H * bc2)[0, 0]) ** 2)
    check(oa + ob > 1, "CLOSE", f"close pair: |<a|a'>|^2 = {oa}, |<b|b'>|^2 = {ob}, sum {oa + ob} > 1; an effect with f(a,b) = 1, f(a',b') = 0 would need {ob} <= f(a,b') <= {1 - oa}: no domain cone distinguishes x' and y'")
    # ---- PHI
    lam = sp.Rational(3, 5) + sp.Rational(4, 5) * I
    D = sp.Matrix([[1, 0], [0, lam]])
    if "phi_nonunitary" in MUT:
        D = sp.Matrix([[1, 0], [0, 2 * lam]])
    ID = sp.kronecker_product(sp.eye(2), D)

    def phi1(X):
        return sp.Rational(5, 8) * ID * X * ID.H + sp.Rational(3, 8) * X

    def phi1s(Y):
        return sp.Rational(5, 8) * ID.H * Y * ID + sp.Rational(3, 8) * Y
    units = []
    for i in range(4):
        for j in range(4):
            M = sp.zeros(4, 4)
            M[i, j] = 1
            units.append(M)
    okp = all(sp.expand((phi1(X) * Y).trace() - (X * phi1s(Y)).trace()) == 0 for X in units for Y in units)
    d0, d1 = sp.symbols("d0 d1")
    d = ket(d0, d1)
    Pc = outer(c, c)
    Pd = outer(d, d)
    img = phi1s(sp.kronecker_product(Pc, Pd))
    local = sp.Rational(5, 8) * D.H * Pd * D + sp.Rational(3, 8) * Pd
    okp &= sp.expand(img - sp.kronecker_product(Pc, local)) == sp.zeros(4, 4)
    # D unitary makes D^dag Pd D a rank-one projector multiple: PSD
    okp &= sp.simplify(D.H * D - sp.eye(2)) == sp.zeros(2, 2)
    check(okp, "PHI", "Tr(Phi_1(X)Y) = Tr(X Phi_1*(Y)) on all units; Phi_1*(|c><c| (x) |d><d|) = |c><c| (x) ((5/8) D^dag|d><d|D + (3/8)|d><d|) with D unitary: Phi_1* preserves SEP, so Phi_1 preserves maxCone = SEP*")
    # ---- SEPF
    rows = W_conditions(a, b, a2, b2) + W_conditions(ac, bc_, ac2, bc2)
    rk = sp.Matrix(rows).rank()
    check(rk == 16 if "same_pair" not in MUT else sp.Matrix(W_conditions(a, b, a2, b2) * 2).rank() == 16, "SEPF",
          f"W(z) cap W(z') = {{0}} for the instance pair and the close pair (combined condition rank {rk} = 16): in SEP + F (F <= B6(z)) the face of z' is cone{{x', y'}}, so by CLOSE the state z'/Tr z' has no frame and SEP + F is not SP")


MUTATIONS = {
    "outside": "RI",
    "wrong_root": "DEC",
    "weak_witness": "VIOL",
    "gamma_mut": "GAMMA",
    "not_close": "CLOSE",
    "phi_nonunitary": "PHI",
    "same_pair": "SEPF",
}


def main():
    global MUT
    detected = {}
    for m, target in MUTATIONS.items():
        MUT = {m}
        try:
            run()
            failed = {cid for ok, cid, _ in RESULTS if not ok}
        except Exception as exc:
            failed = {target}
            print(f"  (mutation {m} raised {type(exc).__name__})")
        detected[m] = target in failed
        print(f"mutation {m:15s} target {target:5s} {'REJECTED' if detected[m] else 'MUTATION-MISSED'} (failing: {sorted(failed)})")
    MUT = set()
    run()
    for ok, cid, text in RESULTS:
        print(f"{'PASS' if ok else 'FAIL'} {cid}: {text}")
    nfail = sum(1 for ok, _, _ in RESULTS if not ok)
    print(f"checks: {len(RESULTS)}, failures: {nfail}, mutations rejected: {sum(detected.values())}/{len(MUTATIONS)}")
    print(f"sympy {sp.__version__}")
    if nfail == 0 and all(detected.values()):
        print("VERDICT MAXCONE-NOT-SP-EXACT")
    else:
        print("VERDICT NOT-ESTABLISHED")
        sys.exit(1)


if __name__ == "__main__":
    main()
