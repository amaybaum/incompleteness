"""C19 — the clause's continuous group forces Q3; the Clifford chain above Stab_C(Z(x)1). Exact checks.

Node C19 (round 4, research/countermodels). S0 (predictions and decision rules) in NOTES-C19, written
2026-10-11T05:06Z (`date -u`) before this script was first run.

Part (i): T1 (explicit SU(2) x SU(2) elements carrying states to products), T2 (countercontrol: G384 does not carry phi0
to a product), T3 (the carried defect pairs negatively with a product).
Part (ii): K1 (orders along the chain), K2 (HO-24's seed h* along the chain), K3 (C15.2's h_C survives at the top),
K4 (survivors with a nontrivial stabilizer at the top, from Gaussian eigenspaces of class representatives).
Exact arithmetic only (Fractions, Gaussian rationals; sympy for square roots in T1 and for factoring). Deterministic.
"""
from fractions import Fraction as Fr
import itertools
import sympy as sp

RES = []


def rec(cid, ok, text, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print("%-4s %s %s%s" % (cid, "PASS" if ok else "FAIL", text, (" -- " + detail) if detail else ""))


class GQ:
    __slots__ = ("r", "i")

    def __init__(self, r, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r + o.r, s.i + o.i)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r - o.r, s.i - o.i)

    def __neg__(s):
        return GQ(-s.r, -s.i)

    def __mul__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)

    __rmul__ = __mul__

    def conj(s):
        return GQ(s.r, -s.i)

    def n2(s):
        return s.r * s.r + s.i * s.i

    def __truediv__(s, o):
        if not isinstance(o, GQ):
            o = GQ(o)
        d = o.n2()
        t = s * o.conj()
        return GQ(t.r / d, t.i / d)

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __eq__(s, o):
        o = o if isinstance(o, GQ) else GQ(o)
        return s.r == o.r and s.i == o.i

    def __hash__(s):
        return hash((s.r, s.i))

    def __repr__(s):
        return "%s%s%si" % (s.r, "+" if s.i >= 0 else "-", abs(s.i)) if s.i != 0 else str(s.r)


ZERO, ONE, II = GQ(0), GQ(1), GQ(0, 1)


def M(rows):
    return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]


def mmul(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), ZERO) for j in range(len(B[0]))] for i in range(len(A))]


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    return [[A[i // 2][j // 2] * B[i % 2][j % 2] for j in range(4)] for i in range(4)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c * x for x in r] for r in A]


def mv(A, v):
    return [sum((A[i][t] * v[t] for t in range(len(v))), ZERO) for i in range(len(A))]


def ipv(u, v):
    return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)


def n2v(v):
    return sum((x.n2() for x in v), Fr(0))


def ovl(u, v):
    return ipv(u, v).n2() / (n2v(u) * n2v(v))


def detr(v):
    return (v[0] * v[3] - v[1] * v[2]).n2() / n2v(v) ** 2


def canon(v):
    k = next(t for t in range(len(v)) if not v[t].iszero())
    a = v[k]
    return tuple(x / a for x in v)


def V(*xs):
    return [x if isinstance(x, GQ) else GQ(x) for x in xs]


s0 = M([[1, 0], [0, 1]])
sx = M([[0, 1], [1, 0]])
sy = M([[0, GQ(0, -1)], [II, 0]])
sz = M([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def coords(A):
    """Pauli coordinates tr(A sigma_m (x) sigma_n) of a Hermitian A (exact, real)."""
    out = []
    for m in range(4):
        for n in range(4):
            t = sum((A[i][j] * SS[m][n][j][i] for i in range(4) for j in range(4)), ZERO)
            assert t.i == 0
            out.append(t.r)
    return out


def Ad_sp(U):
    """signed permutation of the 16 Pauli coordinates induced by A -> U A U†."""
    out = []
    Ud = dag(U)
    for k in range(16):
        m, n = divmod(k, 4)
        img = coords(mmul(mmul(U, SS[m][n]), Ud))
        nz = [(j, x / 4) for j, x in enumerate(img) if x != 0]
        assert len(nz) == 1 and nz[0][1] in (1, -1), "not a Clifford element"
        out.append((nz[0][0], int(nz[0][1])))
    return tuple(out)


def compose(p, q):
    return tuple((p[i][0], p[i][1] * s) for (i, s) in q)


def inverse(p):
    out = [None] * 16
    for k, (i, s) in enumerate(p):
        out[i] = (k, s)
    return tuple(out)


IDSP = tuple((i, 1) for i in range(16))


def closure(gens_sp, gens_mat=None):
    grp = {IDSP: (M([[1 if i == j else 0 for j in range(4)] for i in range(4)]) if gens_mat else None)}
    fr = [IDSP]
    while fr:
        nf = []
        for a in fr:
            for t, g in enumerate(gens_sp):
                b = compose(g, a)
                if b not in grp:
                    grp[b] = mmul(gens_mat[t], grp[a]) if gens_mat else None
                    nf.append(b)
        fr = nf
    return grp


P0 = M([[1, 0], [0, 0]])
P1 = M([[0, 0], [0, 1]])
CNOT = madd(kron(P0, s0), kron(P1, sx))
S = M([[1, 0], [0, II]])
UJ = mscale(GQ(Fr(1, 2)), madd(s0, mscale(GQ(0, -1), madd(madd(sx, sy), sz))))
G_cnot, G_TS, G_TJ = CNOT, kron(s0, S), kron(s0, UJ)
G_CS, G_CJ, G_CX = kron(S, s0), kron(UJ, s0), kron(sx, s0)
sp_ = {name: Ad_sp(U) for name, U in
       [("cnot", G_cnot), ("TS", G_TS), ("TJ", G_TJ), ("CS", G_CS), ("CJ", G_CJ), ("CX", G_CX)]}
ZI = 12  # coordinate index of Z (x) 1

# ===================== Part (i) =====================
def su2_to_e0(a):
    """[[conj a0, conj a1], [-a1, a0]] / |a| as sympy matrix (exact), maps a to |a| e0."""
    a0, a1 = a
    nrm = sp.sqrt(sp.expand(a0 * sp.conjugate(a0) + a1 * sp.conjugate(a1)))
    return sp.Matrix([[sp.conjugate(a0), sp.conjugate(a1)], [-a1, a0]]) / nrm


def carry(psi):
    a, b = (psi[0], psi[1]), (psi[2], psi[3])
    U0 = su2_to_e0(a) if (a[0] != 0 or a[1] != 0) else sp.eye(2)
    U1 = su2_to_e0(b) if (b[0] != 0 or b[1] != 0) else sp.eye(2)
    g = sp.diag(U0, U1)
    img = sp.simplify(g * sp.Matrix(psi))
    ok_su = all(sp.simplify(U.det() - 1) == 0 and sp.simplify(U * U.H - sp.eye(2)) == sp.zeros(2) for U in (U0, U1))
    det = sp.simplify(img[0] * img[3] - img[1] * img[2])
    return ok_su, det, img


I = sp.I
cases = [[3, 4 * I, 5, 12], [1 + 2 * I, 2 - I, 0, 0], [0, 0, 3 - 4 * I, 5], [1, 2, 3 * I, -1 + I],
         [6, 8 * I, 7 - 24 * I, 0]]
t1 = []
for psi in cases:
    ok_su, det, img = carry(psi)
    t1.append(ok_su and det == 0)
rec("T1", all(t1), "explicit P0(x)U0 + P1(x)U1 with U0, U1 in SU(2) carries each test state to a product (det Psi = 0)",
    "%d states incl. phi0 = (1, 2, 3i, -1+i) and the edge cases a = 0, b = 0: %s" % (len(cases), t1))

# T2: the finite G384 carries phi0 to no product
gens384 = [sp_["cnot"], sp_["TS"], sp_["TJ"]]
mats384 = [G_cnot, G_TS, G_TJ]


def orbit_rays(h, gens):
    start = canon(h)
    seen = {start}
    fr = [list(start)]
    while fr:
        nf = []
        for v in fr:
            for U in gens:
                w = canon(mv(U, v))
                if w not in seen:
                    seen.add(w)
                    nf.append(list(w))
        fr = nf
    return [list(v) for v in seen]


phi0 = V(1, 2, GQ(0, 3), GQ(-1, 1))
orb_phi0 = orbit_rays(phi0, mats384)
dmin_phi0 = min(detr(v) for v in orb_phi0)
rec("T2", dmin_phi0 > 0, "countercontrol: G384 = <cnot, actT S, actT J> carries phi0 to no product",
    "%d rays, minimum normalised |det Psi|^2 = %s" % (len(orb_phi0), dmin_phi0))

# T3: the carried defect pairs negatively with the product it lands on
c_t3 = Fr(21, 20)
p_t3 = V(3, GQ(0, 4), 0, 0)  # a product, the image of a carried state
d_on_p = n2v(p_t3) - c_t3 * ipv(p_t3, p_t3).n2() / n2v(p_t3)
rec("T3", d_on_p < 0, "p†(I - cP_p)p = (1 - c)|p|^2 < 0 at a product p: the carried defect is not block-positive",
    "c = 21/20: %s" % d_on_p)

# ===================== Part (ii) =====================
GRP_C2 = closure([sp_["cnot"], sp_["TS"], sp_["TJ"], sp_["CS"], sp_["CJ"]], [G_cnot, G_TS, G_TJ, G_CS, G_CJ])
GRP_384 = closure(gens384)
GRP_768 = closure(gens384 + [sp_["CX"]])
GRP_384J = closure(gens384 + [sp_["CJ"]])
GRP_768J = closure(gens384 + [sp_["CX"], sp_["CJ"]])
stab = {p for p in GRP_C2 if p[ZI] == (ZI, 1)}
stab_pm = {p for p in GRP_C2 if p[ZI][0] == ZI}
k1 = (len(GRP_C2) == 11520 and set(GRP_384) == stab and len(GRP_384) == 384 and sp_["CS"] in GRP_384
      and set(GRP_768) == stab_pm and len(GRP_768) == 768 and len(GRP_384J) == 11520 and len(GRP_768J) == 11520
      and sp_["CX"] in GRP_C2)
rec("K1", k1, "orders along the chain",
    "|C2| = %d, |G384| = %d (= Stab(Z(x)1): %s), actC S in G384: %s, |<G384, actC nflip>| = %d (= Stab(+-Z(x)1): %s), "
    "|<G384, actC J>| = %d, |<G768, actC J>| = %d" % (len(GRP_C2), len(GRP_384), set(GRP_384) == stab,
                                                      sp_["CS"] in GRP_384, len(GRP_768), set(GRP_768) == stab_pm,
                                                      len(GRP_384J), len(GRP_768J)))


def survey(h, gens, order):
    orb = orbit_rays(h, gens)
    dets = [detr(v) for v in orb]
    dmin = min(dets)
    hc = canon(h)
    ovs = [ovl(h, v) for v in orb if tuple(v) != hc]
    smin = min(ovs) if ovs else None
    nperp = sum(1 for v in orb if tuple(v) != hc and ipv(h, v).iszero())
    survives = dmin > 0 and nperp == 0
    cgood = None
    if survives:
        for k in range(2, 12):
            c = 1 + Fr(1, 10 ** k)
            h1 = 1 - 4 * dmin <= (2 / c - 1) ** 2
            cc = c * c * smin >= 4 * (c - 1)
            if h1 and cc:
                cgood = c
                break
    return {"rays": len(orb), "stab": Fr(order, len(orb)), "dmin": dmin, "smin": smin, "nperp": nperp,
            "survives": survives, "c": cgood}


hstar = V(10, GQ(2, -2), GQ(-1, -3), GQ(3, -1))
chain = [("G384", mats384, 384), ("G768 = <G384, actC nflip>", mats384 + [G_CX], 768),
         ("C2 = <G384, actC J>", mats384 + [G_CJ], 11520)]
k2 = []
k2txt = []
for name, gens, order in chain:
    r = survey(hstar, gens, order)
    k2.append(r)
    k2txt.append("%s: %d rays (stabilizer %s), min det %s, min overlap %s, orthogonal partners %d, %s%s" % (
        name, r["rays"], r["stab"], r["dmin"], r["smin"], r["nperp"], "SURVIVES" if r["survives"] else "DIES",
        (" (c = %s satisfies H1 and (CC))" % r["c"]) if r["c"] else ""))
rec("K2", k2[0]["rays"] == 192 and k2[0]["survives"] and k2[0]["c"] is not None
    and all((not r["survives"]) or r["c"] is not None for r in k2),
    "HO-24's seed h* along the chain (a surviving orbit gets an exact c with H1 and (CC))", "; ".join(k2txt))

hC = V(GQ(-480, 7), GQ(357, 870), GQ(939, 834), GQ(448, 486))
rC = survey(hC, [G_cnot, G_TS, G_TJ, G_CS, G_CJ], 11520)
rec("K3", rC["rays"] == 11520 and rC["survives"] and rC["c"] is not None,
    "the top of the chain keeps an explicit surgery cone (C15.2's h_C)",
    "%d rays, min det %s, min overlap %s, orthogonal partners %d, c = %s" % (rC["rays"], rC["dmin"], rC["smin"],
                                                                           rC["nperp"], rC["c"]))

# K4: survivors with a nontrivial stabilizer at the top
gensC2 = [sp_["cnot"], sp_["TS"], sp_["TJ"], sp_["CS"], sp_["CJ"]]
inv_gens = [inverse(g) for g in gensC2]
classes = []
seen = set()
for x in sorted(GRP_C2):
    if x in seen:
        continue
    cl = {x}
    fr = [x]
    while fr:
        nf = []
        for y in fr:
            for g, gi in zip(gensC2, inv_gens):
                z = compose(compose(g, y), gi)
                if z not in cl:
                    cl.add(z)
                    nf.append(z)
        fr = nf
    seen |= cl
    classes.append((min(cl), len(cl)))
assert sum(n for _, n in classes) == 11520

PAULI_SP = {Ad_sp(kron(SIG[m], SIG[n])) for m in range(4) for n in range(4)}


def gauss_eigenspaces(U):
    """eigenvalues of U lying in Q(i), with a Q(i) basis of each eigenspace (sympy, exact)."""
    Ms = sp.Matrix(4, 4, lambda i, j: sp.Rational(U[i][j].r.numerator, U[i][j].r.denominator)
                   + I * sp.Rational(U[i][j].i.numerator, U[i][j].i.denominator))
    lam = sp.Symbol("lam")
    cp = sp.Poly((Ms - lam * sp.eye(4)).det(), lam)
    out = []
    for fac, mult in sp.factor_list(cp.as_expr(), lam, extension=I)[1]:
        fp = sp.Poly(fac, lam)
        if fp.degree() != 1:
            continue
        root = sp.simplify(-fp.all_coeffs()[1] / fp.all_coeffs()[0])
        ns = (Ms - root * sp.eye(4)).nullspace()
        basis = []
        for v in ns:
            vv = []
            for x in v:
                re_, im_ = sp.re(sp.nsimplify(x)), sp.im(sp.nsimplify(x))
                vv.append(GQ(Fr(int(sp.fraction(re_)[0]), int(sp.fraction(re_)[1])),
                             Fr(int(sp.fraction(im_)[0]), int(sp.fraction(im_)[1]))))
            basis.append(vv)
        out.append((root, basis))
    return out


COEFS = [GQ(1), GQ(2, 1), GQ(-1, 3), GQ(3, -2)]
allmats = list(GRP_C2.values())


def top_test(h):
    """C2-orbit of h via all lifted elements: (no product, no orthogonal partner, stabilizer order, orbit rays)."""
    hc = canon(h)
    rays = set()
    stabn = 0
    for U in allmats:
        w = mv(U, h)
        if (w[0] * w[3] - w[1] * w[2]).iszero():
            return False, "product", None
        if ipv(h, w).iszero():
            return False, "orthogonal partner", None
        k = canon(w)
        if k == hc:
            stabn += 1
        rays.add(k)
    return True, len(rays), stabn


found = []
dead_reasons = {}
pauli_ctrl = []
skipped = 0
for rep, size in classes:
    if rep == IDSP:
        continue
    U = GRP_C2[rep]
    spaces = gauss_eigenspaces(U)
    if not spaces:
        skipped += 1
    for root, basis in spaces:
        samples = []
        if len(basis) == 1:
            samples = [basis[0]]
        else:
            for cs_ in [COEFS[:len(basis)], COEFS[1:1 + len(basis)]]:
                samples.append([sum((c * b[t] for c, b in zip(cs_, basis)), ZERO) for t in range(4)])
        for h in samples:
            ok, info, stabn = top_test(h)
            if rep in PAULI_SP:
                pauli_ctrl.append(not ok)
            if ok:
                found.append((size, str(root), [str(x) for x in h], info, stabn))
            else:
                dead_reasons[info] = dead_reasons.get(info, 0) + 1
rec("K4", all(pauli_ctrl) and len(pauli_ctrl) > 0,
    "Gaussian eigenspaces of the %d nontrivial class representatives of C2 sampled; Pauli eigenvectors die (control)"
    % (len(classes) - 1),
    "classes %d, without a Gaussian eigenvalue %d; dead samples by reason %s; Pauli controls dead %d/%d; survivors with a "
    "nontrivial stabilizer: %d%s" % (len(classes), skipped, dead_reasons, sum(pauli_ctrl), len(pauli_ctrl), len(found),
                                     (" -- first: class size %d, eigenvalue %s, h = %s, %s rays, stabilizer %s"
                                      % found[0]) if found else ""))

n_ok = sum(RES)
print("CHECKS %d/%d" % (n_ok, len(RES)))
print("VERDICT C19-EXACT" if n_ok == len(RES) else "VERDICT C19-FAIL")
