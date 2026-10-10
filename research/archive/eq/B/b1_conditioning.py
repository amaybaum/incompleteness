"""EQ-B / B1: what a conditioning principle gives, exactly.

Checks (all exact, Fraction):
  C0  controls: reproduce landed facts (frame, relT, relC / its failure, involution) for
      cnot1 (d=1, neg1), cnot (d=3, nflip), gC5 (d=5, nC5).
  C1  COND(N): G(hom z (x) Y) = hom z (x) Y and G(hom(-z) (x) Y) = hom(-z) (x) Ntil Y  (all Y),
      i.e. the corner maps are M0 = I and M1 = Ntil.  Holds for all three gates.
  C2  relC = CI' and TR: the relC defect D = G(Ntil (x) I) - (Ntil (x) Ntil) G restricted to the
      classical control sector Csec (x) H, Csec = span(e0, lift z), and to the tangent sector
      T (x) H, T = lift(z-perp).  cnot1, cnot: both zero.  gC5: zero on Csec, nonzero on T.
  C3  the gC5 TR failure, with an explicit tangent input and exact values.
  C4  the splits (P, Q) of homMap N and tangentPlus p = P - 1.
  C5  two-NOT control relation for gC5: Rc(N_A, nC5) with the balanced N_A = diag(1,-1,1,-1,-1).
  C6  the three conditioning laws (Cov_N, Rel, Post_N) on gC5: any two are realised by an explicit
      assignment, the third fails; the triple fails at d = 5 for every assignment through gC5.
  C7  linear-algebra countercontrol: a map with TR and without CI (no positivity claimed).
  C8  natural conditioning with TOKEN-level groups (Cov over {I, N_A}, actions {I, nC5}) holds for gC5 at d = 5.
Run:  python3 -I -B b1_conditioning.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *  # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def setup():
    gates = []
    gates.append(("cnot1", 1, cnot1(), neg1(), Z1))
    gates.append(("cnot", 3, cnot3(), nflip(), Z3))
    gates.append(("gC5", 5, gC5(), nC5(), Z5))
    return gates


def frame_ok(G, z, d):
    zz = [Fr(t) for t in z]
    mz = [-t for t in zz]
    corner = [zz, mz]
    for a in (0, 1):
        for b in (0, 1):
            lhs = apply(G, prodState(corner[a], corner[b]))
            rhs = prodState(corner[a], corner[(a + b) % 2])
            if not meq(lhs, rhs):
                return False
    return True


def ops(Nt):
    n = len(Nt)
    return actT_op(Nt), actC_op(Nt)


def relT_defect(G, Nt):
    AT, _ = ops(Nt)
    return madd(matmul(AT, matmul(G, AT)), G, -1)


def relC_defect(G, NtA, NtB):
    """actC N_A (G (actC N_A w)) - actT N_B (G w)."""
    _, AC = ops(NtA)
    AT, _ = ops(NtB)
    return madd(matmul(AC, matmul(G, AC)), matmul(AT, G), -1)


def is_zero(M):
    return all(x == 0 for r in M for x in r)


def basis_vec(n, i):
    v = [Fr(0)] * n
    v[i] = Fr(1)
    return v


def main():
    gates = setup()
    for name, d, G, N, z in gates:
        n = d + 1
        Nt = homMap(N)
        # ---------------- C0 controls
        chk(f"C0 {name}: frame", frame_ok(G, z, d))
        chk(f"C0 {name}: involution G^2 = I", meq(matmul(G, G), eye(n * n)))
        chk(f"C0 {name}: relT", is_zero(relT_defect(G, Nt)))
        rc = is_zero(relC_defect(G, Nt, Nt))
        if name == "gC5":
            chk(f"C0 {name}: relC FAILS (landed gC5_not_relC)", not rc)
            w = entW(6, 3, 3)
            _, AC = ops(Nt)
            AT, _ = ops(Nt)
            lhs = unvecW(matvec(AC, matvec(G, matvec(AC, vecW(w)))), 6)[4][4]
            rhs = unvecW(matvec(AT, matvec(G, vecW(w))), 6)[4][4]
            chk(f"C0 {name}: landed values gC5_relC_lhs = 1, gC5_relC_rhs = -1", lhs == 1 and rhs == -1)
        else:
            chk(f"C0 {name}: relC", rc)
        # ---------------- C1 COND(N): corner maps M0 = I, M1 = Ntil
        hz = homvec(z)
        hmz = homvec([-t for t in z])
        ok0 = ok1 = True
        for nu in range(n):
            Y = basis_vec(n, nu)
            if not meq(apply(G, outer(hz, Y)), outer(hz, Y)):
                ok0 = False
            if not meq(apply(G, outer(hmz, Y)), outer(hmz, matvec(Nt, Y))):
                ok1 = False
        chk(f"C1 {name}: COND slice +z: G(hom z (x) Y) = hom z (x) Y  (M0 = I)", ok0)
        chk(f"C1 {name}: COND slice -z: G(hom -z (x) Y) = hom -z (x) Ntil Y  (M1 = Ntil)", ok1)
        # ---------------- C2 decomposition of the relC defect by control sector
        D = relC_defect(G, Nt, Nt)   # = actC(G(actC w)) - actT(G w); zero iff relC
        # sector bases of the control space
        zi = [Fr(t) for t in z]
        Csec = [basis_vec(n, 0), liftvec(zi)]
        # tangent: lift of an orthonormal-ish basis of z-perp (coordinate basis minus z component)
        Tsec = []
        for k in range(d):
            ek = [Fr(1) if j == k else Fr(0) for j in range(d)]
            c = [ek[j] - zi[k] * zi[j] for j in range(d)]
            if any(c):
                Tsec.append(liftvec(c))
        def restricted_zero(sec):
            for X in sec:
                for nu in range(n):
                    w = outer(X, basis_vec(n, nu))
                    if any(t != 0 for t in matvec(D, vecW(w))):
                        return False
            return True
        cz = restricted_zero(Csec)
        tz = restricted_zero(Tsec)
        if name == "gC5":
            chk(f"C2 {name}: relC defect vanishes on the classical sector (CI holds)", cz)
            chk(f"C2 {name}: relC defect NONZERO on the tangent sector (TR fails)", not tz)
        else:
            chk(f"C2 {name}: relC defect vanishes on the classical sector (CI)", cz)
            chk(f"C2 {name}: relC defect vanishes on the tangent sector (TR)", tz)
        # ---------------- C4 splits
        P = n - rank(madd(Nt, eye(n), -1))
        Q = n - rank(madd(Nt, eye(n), 1))
        print(f"     {name}: (P, Q) = ({P}, {Q}), tangentPlus p = {P - 1}")
        if name == "gC5":
            chk("C4 gC5/nC5: unbalanced (P,Q) = (2,4), p = 1", (P, Q) == (2, 4))
        elif name == "cnot":
            chk("C4 cnot/nflip: balanced (P,Q) = (2,2), p = 1", (P, Q) == (2, 2))
        else:
            chk("C4 cnot1/neg1: balanced (P,Q) = (1,1), p = 0", (P, Q) == (1, 1))

    # ---------------- C3 explicit TR failure for gC5
    G = gC5()
    Nt = homMap(nC5())
    n = 6
    # tangent control input lift(c) with c = e_w1 (coordinate index 2 -> hom index 3), target e_3
    c_in = liftvec([0, 0, 1, 0, 0])          # hom index 3 (w1)
    Nc = matvec(Nt, c_in)                   # = -lift(e_w1)
    Y = basis_vec(n, 3)
    lhs = apply(G, outer(Nc, Y))
    NN = kron(Nt, Nt)
    rhs = unvecW(matvec(NN, vecW(apply(G, outer(c_in, Y)))), n)
    diff = [(i, j, lhs[i][j], rhs[i][j]) for i in range(n) for j in range(n) if lhs[i][j] != rhs[i][j]]
    print("     C3 gC5 TR witness: input lift(e_w1) (x) e_3; entries where G(Nc(x)Y) != (N(x)N)G(c(x)Y):", diff)
    chk("C3 gC5: TR fails at the tangent input lift(e_w1) (x) e_3 (entry (4,4): -1 vs +1)",
        any(i == 4 and j == 4 for (i, j, a, b) in diff))

    # ---------------- C5 two-NOT control relation for gC5
    NA = diag([1, -1, 1, -1, -1])           # balanced: +1 on hom {0,1,3}, -1 on {2,4,5}
    NtA = homMap(NA)
    PA = n - rank(madd(NtA, eye(n), -1))
    QA = n - rank(madd(NtA, eye(n), 1))
    chk("C5 N_A = diag(1,-1,1,-1,-1) is a NOT of eball 5 with axis z5 (orthogonal involution, N_A z5 = -z5)",
        meq(matmul(NA, NA), eye(5)) and matvec(NA, [Fr(t) for t in Z5]) == [Fr(-t) for t in Z5])
    chk("C5 N_A balanced: (P,Q) = (3,3)", (PA, QA) == (3, 3))
    chk("C5 gC5 satisfies the two-NOT control relation Rc(N_A, nC5) exactly",
        is_zero(relC_defect(G, NtA, Nt)))
    chk("C5 gC5 fails Rc(nC5, nC5) (common-N relC)", not is_zero(relC_defect(G, Nt, Nt)))

    # ---------------- C6 the three conditioning laws on gC5
    # Assignment values on tests {+z, -z} and action pairs from {I, N}: Cond[(t, Tp, Tm)] (t = +1/-1)
    I36 = eye(36)
    IN = kron(eye(6), Nt)      # I (x) Ntil   (post-composition by N on the target)
    NI = kron(Nt, eye(6))      # Ntil (x) I   (control NOT)
    conj = lambda A: matmul(NI, matmul(A, NI))
    def slices_ok(A, t, Tp, Tm):
        """Slice law: on hom(t z) apply Tp, on hom(-t z) apply Tm."""
        zt = [Fr(t * s) for s in Z5]
        zmt = [-x for x in zt]
        for nu in range(6):
            Yv = basis_vec(6, nu)
            if not meq(apply(A, outer(homvec(zt), Yv)), outer(homvec(zt), matvec(Tp, Yv))):
                return False
            if not meq(apply(A, outer(homvec(zmt), Yv)), outer(homvec(zmt), matvec(Tm, Yv))):
                return False
        return True
    Id6 = eye(6)
    acts = {"I": Id6, "N": Nt}
    def laws(Cond):
        cov = all(meq(conj(Cond[(1, a, b)]), Cond[(-1, a, b)]) for a in acts for b in acts)
        rel = all(meq(Cond[(-1, a, b)], Cond[(1, b, a)]) for a in acts for b in acts)
        comp = {("I", "I"): "N", ("I", "N"): "N", ("N", "I"): "I", ("N", "N"): "I"}
        def NT(a):
            return "N" if a == "I" else "I"
        post = all(meq(matmul(IN, Cond[(t, a, b)]), Cond[(t, NT(a), NT(b))])
                   for t in (1, -1) for a in acts for b in acts)
        sl = all(slices_ok(Cond[(t, a, b)], t, acts[a], acts[b]) for t in (1, -1) for a in acts for b in acts)
        return sl, cov, rel, post
    base = {("I", "N"): G, ("N", "I"): matmul(IN, G), ("I", "I"): I36, ("N", "N"): IN}
    # (i) Cov + Post, no Rel: -z values by conjugation
    A1 = {}
    for (a, b), M in base.items():
        A1[(1, a, b)] = M
        A1[(-1, a, b)] = conj(M)
    sl, cov, rel, post = laws(A1)
    chk("C6(i)  gC5 assignment with Slice+Cov_N+Post_N, Rel fails", sl and cov and post and not rel)
    # (ii) Rel + Post, no Cov: -z values by relabelling
    A2 = {}
    for (a, b), M in base.items():
        A2[(1, a, b)] = M
    for (a, b) in base:
        A2[(-1, a, b)] = A2[(1, b, a)]
    sl, cov, rel, post = laws(A2)
    chk("C6(ii) gC5 assignment with Slice+Rel+Post_N, Cov_N fails", sl and rel and post and not cov)
    # (iii) Rel + Cov, no Post: Cond(+z; N, I) := conj(G)
    base3 = {("I", "N"): G, ("N", "I"): conj(G), ("I", "I"): I36, ("N", "N"): IN}
    A3 = {}
    for (a, b), M in base3.items():
        A3[(1, a, b)] = M
        A3[(-1, a, b)] = conj(M)
    sl, cov, rel, post = laws(A3)
    chk("C6(iii) gC5 assignment with Slice+Rel+Cov_N, Post_N fails", sl and rel and cov and not post)
    # the triple forces relC for Cond(+z; I, N): check the derivation numerically on the cnot assignment
    Gc = cnot3()
    Ntc = homMap(nflip())
    INc = kron(eye(4), Ntc)
    NIc = kron(Ntc, eye(4))
    chk("C6 cnot: Cov_N∘Rel∘Post_N chain closes: (N(x)I)G(N(x)I) = (I(x)N)G  (relC)",
        meq(matmul(NIc, matmul(Gc, NIc)), matmul(INc, Gc)))

    # ---------------- C8 natural conditioning with TOKEN-level groups holds at d = 5 (QB3 countermodel)
    # control group {I, N_A} (Cov), target actions {I, N_B} (Slice/Post), N_A = diag(1,-1,1,-1,-1), N_B = nC5
    NtA8 = homMap(diag([1, -1, 1, -1, -1]))
    NAI = kron(NtA8, eye(6))
    conjA = lambda A_: matmul(NAI, matmul(A_, NAI))
    base8 = {("I", "N"): G, ("N", "I"): matmul(IN, G), ("I", "I"): I36, ("N", "N"): IN}
    A8 = {}
    for (a, b), M in base8.items():
        A8[(1, a, b)] = M
        A8[(-1, a, b)] = conjA(M)
    def NT8(a):
        return "N" if a == "I" else "I"
    cov8 = all(meq(conjA(A8[(1, a, b)]), A8[(-1, a, b)]) for a in acts for b in acts)
    rel8 = all(meq(A8[(-1, a, b)], A8[(1, b, a)]) for a in acts for b in acts)
    post8 = all(meq(matmul(IN, A8[(t, a, b)]), A8[(t, NT8(a), NT8(b))])
                for t in (1, -1) for a in acts for b in acts)
    sl8 = all(slices_ok(A8[(t, a, b)], t, acts[a], acts[b]) for t in (1, -1) for a in acts for b in acts)
    chk("C8 gC5: natural conditioning with token-level groups (Cov over {I,N_A}, actions {I,nC5}) holds: "
        "Slice, Cov, Rel, Post all exact at d = 5", sl8 and cov8 and rel8 and post8)

    # ---------------- C7 linear countercontrol: TR without CI (d = 3), no positivity claimed
    # G7 := cnot on hom z (x) H and on T (x) H; on hom(-z) (x) H act as hom(-z) (x) R Y with R = diag(-1,1,-1)
    R = homMap(diag([-1, 1, -1]))
    n = 4
    hz = homvec(Z3)
    hmz = homvec([0, 0, -1])
    # basis of control space: hz, hmz, lift x, lift y
    basisC = [hz, hmz, liftvec([1, 0, 0]), liftvec([0, 1, 0])]
    Bm = transpose(basisC)               # columns = basis vectors
    Binv = inverse(Bm)
    # build G7 column by column on the standard basis e_mu (x) e_nu
    G7 = zeros(16, 16)
    for mu in range(4):
        coeff = [Binv[k][mu] for k in range(4)]   # e_mu = sum coeff_k basisC_k
        for nu in range(4):
            Yv = basis_vec(4, nu)
            out = zeros(4, 4)
            for k in range(4):
                if coeff[k] == 0:
                    continue
                if k == 1:
                    img = outer(hmz, matvec(R, Yv))
                else:
                    img = apply(Gc, outer(basisC[k], Yv))
                out = madd(out, mscale(coeff[k], img))
            col = vecW(out)
            for r in range(16):
                G7[r][mu * 4 + nu] = col[r]
    D7 = relC_defect(G7, Ntc, Ntc)
    def restricted_zero7(sec):
        for X in sec:
            for nu in range(4):
                if any(t != 0 for t in matvec(D7, vecW(outer(X, basis_vec(4, nu))))):
                    return False
        return True
    chk("C7 countercontrol: TR holds (tangent sector) and CI fails (classical sector), rank 16",
        restricted_zero7([liftvec([1, 0, 0]), liftvec([0, 1, 0])])
        and not restricted_zero7([basis_vec(4, 0), liftvec(Z3)]) and rank(G7) == 16)

    nfail = sum(1 for _, ok in checks if not ok)
    print(f"b1_conditioning: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B1-CHECKS-GREEN" if nfail == 0 else "B1-CHECKS-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
