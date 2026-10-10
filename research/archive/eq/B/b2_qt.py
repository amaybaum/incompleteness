"""EQ-B / B2: complex QT against the conditioning principles (exact, over Q(i)).

  Q1  the kernel's d = 3 gate `cnot` is a QT channel: cnot = Ad(CNOT) or a local relabelling of it.
  Q2  natural conditioning over SO(3) in QT (spot checks): with G = Ad(CNOT) and N = Ad(X):
        Cov for a z-flipping pi-rotation g about (3/5, 4/5, 0):  (g (x) I) G (g (x) I)^-1 = (I (x) N) G,
        Cov for a stabiliser rotation R_z(phi), cos(phi/2) = 3/5:  (R (x) I) G (R (x) I)^-1 = G.
  Q3  composition of conditionings is QT-incompatible on the Klein group: for every phase choice the
      controlled versions of Ad X and Ad Z do not commute; the commutator channel is Ad(Z (x) I).
  Q4  covariance under the full O(3) fails for QT's gate: the reflection y -> -y on the control does not
      commute with cnot (orientation restriction).
  Q5  CNOT lies on a one-parameter group of QT channels G_t = Ad(|0><0| (x) I + |1><1| (x) (P+ + e^{it} P-)),
      a homomorphic controlled U(1); G_pi = Ad(CNOT); slices hold at every t (exact at cos t = 3/5).
Run: python3 -I -B b2_qt.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *   # noqa: E402,F401
from qlib import *   # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def kronR(A, B):
    return kron(A, B)


def main():
    CNOT = controlled(PI, PX)
    G = channel_W(CNOT)
    K = cnot3()
    # ---------------- Q1
    same = meq(G, K)
    print("     Q1 cnot == Ad(CNOT) exactly:", same)
    found = None
    # search local relabellings by signed diagonal orthogonal maps fixing e0 on each copy
    import itertools
    sgns = list(itertools.product([1, -1], repeat=3))
    for sa in sgns:
        for sb in sgns:
            A = homMap(diag(list(sa)))
            B = homMap(diag(list(sb)))
            L = kron(A, B)
            Linv = L  # involution
            if meq(matmul(L, matmul(G, Linv)), K):
                found = (sa, sb)
                break
        if found:
            break
    print("     Q1 relabelling (control signs, target signs) with cnot = L Ad(CNOT) L^-1:", found)
    chk("Q1 the kernel cnot is Ad(CNOT) up to a local signed-diagonal relabelling (a QT channel up to"
        " local orthogonal relabelling)", same or found is not None)
    # QT gate is a CtrlGate's relations with N = Ad X = nflip
    Nt = homMap(nflip())
    assert meq(local_W(PX), Nt)
    NI = kron(Nt, eye(4))
    IN = kron(eye(4), Nt)
    chk("Q1 Ad(CNOT) satisfies relC with N = Ad(X)", meq(matmul(NI, matmul(G, NI)), matmul(IN, G)))
    chk("Q1 Ad(CNOT) satisfies relT with N = Ad(X)", meq(matmul(IN, matmul(G, IN)), G))

    # ---------------- Q2 natural conditioning: Cov over SO(3) spot checks
    a, b = Fr(3, 5), Fr(4, 5)
    Vg = cadd(cscale(Q(a), PX), cscale(Q(b), PY))       # pi-rotation about (3/5, 4/5, 0), Hermitian unitary
    gW = local_W(Vg)
    gI = kron(gW, eye(4))
    gIinv = kron(inverse(gW), eye(4))
    chk("Q2 Cov_g with g = pi-rotation about (3/5,4/5,0) (a z-flipper in SO(3)): (g(x)I)G(g(x)I)^-1 = (I(x)N)G",
        meq(matmul(gI, matmul(G, gIinv)), matmul(IN, G)))
    Rz = [[Q(Fr(3, 5), Fr(-4, 5)), Q()], [Q(), Q(Fr(3, 5), Fr(4, 5))]]   # exp(-i phi Z/2), cos(phi/2)=3/5
    RW = local_W(Rz)
    RI = kron(RW, eye(4))
    RIinv = kron(inverse(RW), eye(4))
    chk("Q2 Cov over the stabiliser: R_z(phi) (x) I commutes with G (cos phi = -7/25)",
        meq(matmul(RI, matmul(G, RIinv)), G))
    # the natural assignment on {+z,-z} x {I,N}^2 with lifts L(I) = I, L(N) = X satisfies Slice/Cov/Rel/Post
    def cond(t, Lp, Lm):
        Pp, Pm = (P0, P1) if t == 1 else (P1, P0)
        return channel_W(cadd(ckron(Pp, Lp), ckron(Pm, Lm)))
    lifts = {"I": PI, "N": PX}
    vals = {(t, p, m): cond(t, lifts[p], lifts[m]) for t in (1, -1) for p in lifts for m in lifts}
    cov = all(meq(matmul(NI, matmul(vals[(1, p, m)], NI)), vals[(-1, p, m)]) for p in lifts for m in lifts)
    rel = all(meq(vals[(-1, p, m)], vals[(1, m, p)]) for p in lifts for m in lifts)
    flip = {"I": "N", "N": "I"}
    post = all(meq(matmul(IN, vals[(t, p, m)]), vals[(t, flip[p], flip[m])])
               for t in (1, -1) for p in lifts for m in lifts)
    chk("Q2 QT natural conditioning on {+z,-z} x {I,N}^2 (lift N -> X): Cov_N, Rel, Post_N all hold",
        cov and rel and post)
    # with the SU(2) lift N -> iX the chain breaks (the lift must satisfy L(N)^2 = I)
    lifts2 = {"I": PI, "N": cscale(I_, PX)}
    vals2 = {(t, p, m): cond(t, lifts2[p], lifts2[m]) for t in (1, -1) for p in lifts2 for m in lifts2}
    rel2 = all(meq(vals2[(-1, p, m)], vals2[(1, m, p)]) for p in lifts2 for m in lifts2)
    post2 = all(meq(matmul(IN, vals2[(t, p, m)]), vals2[(t, flip[p], flip[m])])
                for t in (1, -1) for p in lifts2 for m in lifts2)
    chk("Q2 countercontrol: with the SU(2) lift N -> iX, Rel holds but Post_N fails (the lift must square to I)",
        rel2 and not post2)
    G_iX = vals2[(1, "I", "N")]
    hz_, hmz_ = homvec(Z3), homvec([0, 0, -1])
    cond_iX = all(meq(apply(G_iX, outer(hz_, [Fr(1) if j == nu else Fr(0) for j in range(4)])),
                      outer(hz_, [Fr(1) if j == nu else Fr(0) for j in range(4)]))
                  and meq(apply(G_iX, outer(hmz_, [Fr(1) if j == nu else Fr(0) for j in range(4)])),
                          outer(hmz_, matvec(Nt, [Fr(1) if j == nu else Fr(0) for j in range(4)])))
                  for nu in range(4))
    chk("Q2 countercontrol: Ad(|0><0|(x)I + |1><1|(x)iX) = (S(x)I)CNOT has COND(N) but fails relC(N,N)",
        cond_iX and not meq(matmul(NI, matmul(G_iX, NI)), matmul(IN, G_iX)))

    # ---------------- Q3 composition on the Klein group is impossible in QT
    phases = [Q(1), Q(-1), I_, Q(0, -1)]
    ZI = channel_W(ckron(PZ, PI))
    allbad = True
    for pa in phases:
        for pb in phases:
            CX = channel_W(controlled(PI, cscale(pa, PX)))
            CZ = channel_W(controlled(PI, cscale(pb, PZ)))
            lhs = matmul(CX, CZ)
            rhs = matmul(CZ, CX)
            if meq(lhs, rhs) or not meq(lhs, matmul(ZI, rhs)):
                allbad = False
    chk("Q3 for all 16 phase choices: C(X)C(Z) != C(Z)C(X) and C(X)C(Z) = Ad(Z(x)I) C(Z)C(X)", allbad)
    chk("Q3 while Ad(X) and Ad(Z) commute on one copy", meq(matmul(local_W(PX), local_W(PZ)),
                                                          matmul(local_W(PZ), local_W(PX))))

    # ---------------- Q4 O(3)-covariance fails: reflection y -> -y on the control
    ry = homMap(diag([1, -1, 1]))
    ryI = kron(ry, eye(4))
    chk("Q4 the reflection r_y (x) I does not commute with the kernel cnot", not meq(matmul(ryI, matmul(K, ryI)), K))
    chk("Q4 the reflection r_y (x) I does not commute with Ad(CNOT)", not meq(matmul(ryI, matmul(G, ryI)), G))

    # ---------------- Q5 the one-parameter group through CNOT
    Pp = cscale(Q(Fr(1, 2)), cadd(PI, PX))
    Pm = cscale(Q(Fr(1, 2)), cadd(PI, PX, -1))
    def Vt(e):   # e = e^{it}
        return cadd(Pp, cscale(e, Pm))
    e = Q(Fr(3, 5), Fr(4, 5))
    e2 = e * e
    Gt = channel_W(controlled(PI, Vt(e)))
    G2t = channel_W(controlled(PI, Vt(e2)))
    chk("Q5 group law: G_t G_t = G_2t (cos t = 3/5)", meq(matmul(Gt, Gt), G2t))
    chk("Q5 G_pi = Ad(CNOT)", meq(channel_W(controlled(PI, Vt(Q(-1)))), G))
    # slices of G_t: +z slice identity, -z slice Ad(V_t)
    VtW = local_W(Vt(e))
    ok = True
    hz, hmz = homvec(Z3), homvec([0, 0, -1])
    for nu in range(4):
        Yv = [Fr(1) if j == nu else Fr(0) for j in range(4)]
        if not meq(apply(Gt, outer(hz, Yv)), outer(hz, Yv)):
            ok = False
        if not meq(apply(Gt, outer(hmz, Yv)), outer(hmz, matvec(VtW, Yv))):
            ok = False
    chk("Q5 G_t has COND(V_t): identity on the +z slice, Ad(V_t) on the -z slice", ok)
    print("     Q5 Ad(V_t) on one copy (cos t = 3/5):", [[str(x) for x in r] for r in VtW])
    from jk import flow_op
    chk("Q5 the J/K flow of jk.py at d = 3 equals this QT group exactly (cos t = 3/5 and cos t = -7/25)",
        meq(flow_op(3, Fr(3, 5), Fr(4, 5)), Gt) and meq(flow_op(3, Fr(-7, 25), Fr(24, 25)), G2t))
    # print the tangent-sector block of G_t for the d = 5 transcription
    print("     Q5 tangent-sector action of G_t on lift(x), lift(y) controls (rows: output index mu*4+nu):")
    for cidx, cname in ((1, "x"), (2, "y")):
        for nu in range(4):
            w = entW(4, cidx, nu)
            out = apply(Gt, w)
            nz = [(m, n_, str(out[m][n_])) for m in range(4) for n_ in range(4) if out[m][n_] != 0]
            print(f"        G_t(e_{cname} (x) e_{nu}) = {nz}")

    nfail = sum(1 for _, ok in checks if not ok)
    print(f"b2_qt: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B2-QT-GREEN" if nfail == 0 else "B2-QT-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
