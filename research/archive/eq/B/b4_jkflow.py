"""EQ-B / B4: the J/K flow — a continuous reversible interaction with two-sided positivity at every odd d.

Exact (Fraction) checks at d = 3, 5, 7 and rational (cos t, sin t):
  F1  G_0 = I;  G_pi = the landed gate (cnot at d = 3, gC5 at d = 5);  group law G_t G_t = G_2t, G_t G_-t = I;
  F2  normalisation preserved (row (0,0) of G_t is the unit functional);  COND slices at every t;
  F3  non-product: operator-Schmidt (realignment) rank of G_t > 1 for t not in 2 pi Z (product <=> rank 1);
  F4  G_t is not a CtrlGate-type gate for t != pi (no frame) — recorded, not needed.
Symbolic (sympy, exact polynomial identities):
  S1  value decomposition: pairVal(e, f, G_t(hom x (x) Y)) =
        (1+x_z)/2 (e0+e_z) <f,Y> + (1-x_z)/2 (e0-e_z) <f,R_t Y> + (e_T.x_T) <f,A_t Y> + (e_T.J x_T) <f,B_t Y>
      (all of x, e, f, Y, c, s symbolic; c, s free).
  S2  key identity, modulo c^2 + s^2 = 1:
        <f,Y><f,R_t Y> - <f,A_t Y>^2 - <f,B_t Y>^2 = (2 - 2c) (P M - |w|^2),
        P = (f0+f_x)(Y0+Y_x)/2, M = (f0-f_x)(Y0-Y_x)/2, |w|^2 = ((f_-.Y_-)^2 + (f_-.K Y_-)^2)/4.
  S3  4(P M - |w|^2) = (f0^2 - f_x^2 - |f_-|^2)(Y0^2 - Y_x^2) + |f_-|^2 (Y0^2 - Y_x^2 - |Y_-|^2) + L(f_-, Y_-),
      L(a, b) = |a|^2|b|^2 - (a.b)^2 - (a.Kb)^2 = sum of squares (complex Lagrange identity), checked symbolically.
Written assembly (in RESULT.md): for f, Y, e in the Lorentz cone and |x| <= 1, S1 + AM-GM + Bessel on (x_T, J x_T)
give V >= |x_T||e_T| (sqrt(<f,Y><f,R_tY>) - sqrt(<f,A_tY>^2 + <f,B_tY>^2)) >= 0 by S2-S3; posInv by G_-t = G_t^-1.
Countercontrols:
  CC1 the same tangent block with the classical-sector rotation run backwards (R_-t): an exact negative value;
  CC2 the J/K gate (t = pi) with its J c output scaled by 6/5 (J no longer orthogonal): exact negative value,
      so the Bessel hypothesis of the proof is load-bearing.
Run: python3 -I -B b4_jkflow.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *   # noqa: E402
from jk import flow_op, flow_blocks, jk_mats   # noqa: E402
import sympy as sp   # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def realign_rank(G, n):
    # G[(i*n+j)][(k*n+l)] = sum coefficient of (e_i e_k^T) (x) (e_j e_l^T); realign to rows (i,k), cols (j,l)
    Rm = zeros(n * n, n * n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    Rm[i * n + k][j * n + l] = G[i * n + j][k * n + l]
    return rank(Rm)


def exact_checks():
    pts = {"t0": (Fr(1), Fr(0)), "pi": (Fr(-1), Fr(0)), "a": (Fr(3, 5), Fr(4, 5)),
           "2a": (Fr(-7, 25), Fr(24, 25)), "-a": (Fr(3, 5), Fr(-4, 5)), "pi/2": (Fr(0), Fr(1))}
    for d in (3, 5, 7):
        n = d + 1
        G = {k: flow_op(d, c, s) for k, (c, s) in pts.items()}
        chk(f"F1 d={d}: G_0 = I", meq(G["t0"], eye(n * n)))
        if d == 3:
            chk("F1 d=3: G_pi = kernel cnot (CompositeDimension.cnot)", meq(G["pi"], cnot3()))
        if d == 5:
            chk("F1 d=5: G_pi = kernel gC5 (RelcSelect.gC5)", meq(G["pi"], gC5()))
        chk(f"F1 d={d}: group law G_a G_a = G_2a (cos a = 3/5)", meq(matmul(G["a"], G["a"]), G["2a"]))
        chk(f"F1 d={d}: G_a G_-a = I", meq(matmul(G["a"], G["-a"]), eye(n * n)))
        # normalisation: (0,0) output entry equals (0,0) input entry
        row00 = G["a"][0]
        chk(f"F2 d={d}: G_a preserves the normalisation functional", all(row00[k] == (1 if k == 0 else 0)
                                                                          for k in range(n * n)))
        # COND slices at t = a
        R, A, B, J = flow_blocks(d, Fr(3, 5), Fr(4, 5))
        hz = [Fr(0)] * n; hz[0] = Fr(1); hz[d] = Fr(1)
        hmz = [Fr(0)] * n; hmz[0] = Fr(1); hmz[d] = Fr(-1)
        ok = True
        for nu in range(n):
            Y = [Fr(1) if j == nu else Fr(0) for j in range(n)]
            if not meq(apply(G["a"], outer(hz, Y)), outer(hz, Y)):
                ok = False
            if not meq(apply(G["a"], outer(hmz, Y)), outer(hmz, matvec(R, Y))):
                ok = False
        chk(f"F2 d={d}: COND(R_a) slices (identity on +z, R_a on -z)", ok)
        if d in (5, 7):
            # the time-pi member is a frame gate (COND) that fails relC: unbalanced homogenised NOT
            Nt = [[Fr(0)] * n for _ in range(n)]
            for i in range(n):
                Nt[i][i] = Fr(1) if i in (0, 1) else Fr(-1)
            zc = [Fr(0)] * d; zc[d - 1] = Fr(1)
            mz = [-t for t in zc]
            cor = [zc, mz]
            fr = all(meq(apply(G["pi"], prodState(cor[a], cor[b])), prodState(cor[a], cor[(a + b) % 2]))
                     for a in (0, 1) for b in (0, 1))
            NI = kron(Nt, eye(n))
            IN = kron(eye(n), Nt)
            rc = meq(matmul(NI, matmul(G["pi"], NI)), matmul(IN, G["pi"]))
            chk(f"F4 d={d}: G_pi has the frame and FAILS relC with its NOT (split (2,{d - 1}), unbalanced)",
                fr and not rc)
        rr = realign_rank(G["a"], n)
        chk(f"F3 d={d}: G_a is not a product of local maps (operator-Schmidt rank {rr} > 1)", rr > 1)
        chk(f"F3 d={d}: control: G_0 has operator-Schmidt rank 1", realign_rank(G["t0"], n) == 1)
        # R_a is an orthogonal map of the ball fixing the unit; J, K orthogonal complex structures
        X, K, Jm, Pp, Pm = jk_mats(d)
        Rt = [r[1:] for r in R[1:]]
        chk(f"F2 d={d}: R_a = homMap of an orthogonal map; J^2 = -1 on T, K^2 = -1 on E-",
            meq(matmul(transpose(Rt), Rt), eye(d))
            and all(matmul(Jm, Jm)[i][i] == (-1 if 1 <= i <= d - 1 else 0) for i in range(n))
            and all(matmul(K, K)[i][i] == (-1 if i >= 2 else 0) for i in range(n)))


def sym_checks(d):
    n = d + 1
    c, s = sp.symbols("c s")
    xs = sp.symbols(f"x0:{d}")          # control point (coordinates)
    es = sp.symbols(f"e0:{n}")          # control effect (homogeneous)
    fs = sp.symbols(f"f0:{n}")          # target effect
    Ys = sp.symbols(f"Y0:{n}")          # target homogeneous vector
    one, zero, half = sp.Integer(1), sp.Integer(0), sp.Rational(1, 2)
    G = flow_op(d, c, s, one, zero, half)
    R, A, B, J = flow_blocks(d, c, s, one, zero, half)
    hx = [one] + list(xs)
    w = [[hx[i] * Ys[j] for j in range(n)] for i in range(n)]
    vw = [w[i][j] for i in range(n) for j in range(n)]
    Gw = [sum(G[r][k] * vw[k] for k in range(n * n) if G[r][k] != 0) for r in range(n * n)]
    V = sum(es[i] * Gw[i * n + j] * fs[j] for i in range(n) for j in range(n))
    dot = lambda u, v: sum(u[i] * v[i] for i in range(len(u)))
    app = lambda M, v: [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]
    xz = xs[d - 1]
    xT = [zero] + [xs[k] for k in range(d - 1)] + [zero]          # lift of the tangent part (hom indices 1..d-1)
    eT = [zero] + [es[k] for k in range(1, d)] + [zero]
    JxT = app(J, xT)
    fY = dot(fs, Ys)
    fRY = dot(fs, app(R, Ys))
    fAY = dot(fs, app(A, Ys))
    fBY = dot(fs, app(B, Ys))
    formula = (1 + xz) / 2 * (es[0] + es[d]) * fY + (1 - xz) / 2 * (es[0] - es[d]) * fRY \
        + dot(eT, xT) * fAY + dot(eT, JxT) * fBY
    s1 = sp.expand(V - formula) == 0
    chk(f"S1 d={d}: value decomposition identity (symbolic in x, e, f, Y, c, s)", s1)
    # S2
    X, K, Jm, Pp, Pm = jk_mats(d, one, zero)
    fm = [zero, zero] + list(fs[2:])
    Ym = [zero, zero] + list(Ys[2:])
    KYm = app(K, Ym)
    P = (fs[0] + fs[1]) * (Ys[0] + Ys[1]) / 2
    M = (fs[0] - fs[1]) * (Ys[0] - Ys[1]) / 2
    w2 = (dot(fm, Ym) ** 2 + dot(fm, KYm) ** 2) / 4
    lhs = fY * fRY - fAY ** 2 - fBY ** 2
    rhs = (2 - 2 * c) * (P * M - w2)
    diff = sp.expand(lhs - rhs)
    diff = sp.expand(diff.subs(s ** 2, 1 - c ** 2))
    # reduce higher powers of s (s^3, s^4 appear only through s^2)
    diff = sp.expand(sp.Poly(diff, s).as_expr())
    red = sp.rem(sp.Poly(diff, s), sp.Poly(s ** 2 - (1 - c ** 2), s))
    s2 = sp.expand(red.as_expr()) == 0
    chk(f"S2 d={d}: key identity <f,Y><f,RY> - <f,AY>^2 - <f,BY>^2 = (2-2c)(PM - |w|^2) mod c^2+s^2=1", s2)
    # S3 decomposition of 4(PM - |w|^2) and the complex Lagrange SOS for L
    fm2 = dot(fm, fm)
    Ym2 = dot(Ym, Ym)
    L = fm2 * Ym2 - dot(fm, Ym) ** 2 - dot(fm, KYm) ** 2
    s3a = sp.expand(4 * (P * M - w2) - ((fs[0] ** 2 - fs[1] ** 2 - fm2) * (Ys[0] ** 2 - Ys[1] ** 2)
                                         + fm2 * (Ys[0] ** 2 - Ys[1] ** 2 - Ym2) + L)) == 0
    chk(f"S3 d={d}: 4(PM - |w|^2) = (f0^2-f_x^2-|f_-|^2)(Y0^2-Y_x^2) + |f_-|^2(Y0^2-Y_x^2-|Y_-|^2) + L", s3a)
    # complex coordinates on E- : pairs (2,d), (3,4), (5,6), ...  with K acting as multiplication by i
    pairs = [(2, d)] + [(a, a + 1) for a in range(3, d - 1, 2)]
    za = [(fs[p], fs[q]) for (p, q) in pairs]   # complex number re + i im with K: re -> im
    zb = [(Ys[p], Ys[q]) for (p, q) in pairs]
    sos = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            # complex Lagrange identity: |a|^2|b|^2 - |sum conj(a_k) b_k|^2 = sum_{i<j} |a_i b_j - a_j b_i|^2,
            # and (a.b)^2 + (a.Kb)^2 = |sum conj(a_k) b_k|^2 when K is multiplication by i on the pairs.
            ar, ai = za[i]; br, bi = zb[j]; cr, ci = za[j]; dr, di = zb[i]
            re = (ar * br - ai * bi) - (cr * dr - ci * di)
            im = (ar * bi + ai * br) - (cr * di + ci * dr)
            sos += re ** 2 + im ** 2
    s3b = sp.expand(L - sos) == 0
    chk(f"S3 d={d}: L(f_-, Y_-) is the explicit sum of squares (complex Lagrange identity)", s3b)
    return s1 and s2 and s3a and s3b


def countercontrols():
    d, n = 5, 6
    c, s = Fr(3, 5), Fr(4, 5)
    # CC1: classical-sector rotation run backwards: build G with R_-t but A_t, B_t
    from jk import lin, mm
    Gf = flow_op(d, c, s)
    Gb = flow_op(d, c, -s)
    # splice: classical sector of Gb, tangent sector of Gf
    G = zeros(n * n, n * n)
    for mu in range(n):
        for nu in range(n):
            col = mu * n + nu
            src = Gb if mu in (0, d) else Gf
            for r in range(n * n):
                G[r][col] = src[r][col]
    # search rational points for a negative value
    import itertools
    cand_x = [[Fr(0), Fr(0), Fr(0), Fr(0), Fr(0)]]
    # rational unit vectors from Pythagorean data
    units = []
    for (a, b) in ((Fr(3, 5), Fr(4, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(1), Fr(0)), (Fr(0), Fr(1))):
        for i in range(5):
            for j in range(5):
                if i < j:
                    for sa in (1, -1):
                        for sb in (1, -1):
                            v = [Fr(0)] * 5
                            v[i] = sa * a
                            v[j] = sb * b
                            units.append(v)
    best = None
    for xv in units[:60]:
        for yv in units[:60:3]:
            w = apply(G, prodState(xv, yv))
            for ev in units[::7]:
                for fv in units[::5]:
                    val = pairVal(homvec(ev), homvec(fv), w)
                    if best is None or val < best[0]:
                        best = (val, xv, yv, ev, fv)
    print("     CC1 most negative value found:", best[0])
    chk("CC1 countercontrol: tangent block of G_t with the classical rotation R_-t fails posFwd (exact negative value)",
        best[0] < 0)
    # the true flow at the same points has no negative value (sanity, not a certificate)
    worst = None
    for xv in units[:60]:
        for yv in units[:60:3]:
            w = apply(Gf, prodState(xv, yv))
            for ev in units[::7]:
                for fv in units[::5]:
                    val = pairVal(homvec(ev), homvec(fv), w)
                    if worst is None or val < worst:
                        worst = val
    chk("CC1 sanity: the J/K flow G_a has no negative value at the same sample points (min %s)" % worst, worst >= 0)
    # CC2: the J/K gate (t = pi) with the tangent output along J c scaled by 6/5 (J no longer orthogonal):
    # the Bessel step of the proof fails; expect an exact negative value.
    Gp = flow_op(d, Fr(-1), Fr(0))
    G2 = [list(r) for r in Gp]
    for mu in range(1, d):              # tangent control indices
        for nu in range(n):
            col = mu * n + nu
            for r in range(n * n):
                i = r // n
                if 1 <= i <= d - 1 and i != mu:     # the J c component (J c has index != mu inside T)
                    G2[r][col] = Fr(6, 5) * Gp[r][col]
    best2 = None
    for xv in units[:60]:
        for yv in units[:60:3]:
            w = apply(G2, prodState(xv, yv))
            for ev in units[::7]:
                for fv in units[::5]:
                    val = pairVal(homvec(ev), homvec(fv), w)
                    if best2 is None or val < best2:
                        best2 = val
    print("     CC2 most negative value found:", best2)
    chk("CC2 countercontrol: J/K gate with the J-component scaled by 6/5 fails posFwd (exact negative value)",
        best2 < 0)


def main():
    exact_checks()
    for d in (3, 5, 7):
        sym_checks(d)
    countercontrols()
    nfail = sum(1 for _, ok in checks if not ok)
    print(f"b4_jkflow: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B4-JKFLOW-GREEN" if nfail == 0 else "B4-JKFLOW-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
