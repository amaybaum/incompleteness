"""Review-A exact check (standard library only; run with python3 -I).

Literal re-implementation of the design definitions in FiniteReach.lean / FiniteReachTable.lean
(recursive carriers, bitAt, blockFam, flipX, cnotM, localM, pauliWord, dictionary, coordinates,
tabAct) and of #829's proposed coordinate actions (cnotK with the landed sgn/pc/pt, actK with
homMap of rotLin t and cycEquiv), compared with exact Gaussian-rational arithmetic for k = 1..4.

Also re-evaluates, under the literal design definitions, the hypothesis each named countermodel
violates (SEP3, CUT3, SHIFT3, CM1 = Track B's H = S (x) I4, Gamma-Q3 at k = 2).

Countercontrols: reversed CNOT direction (NEG-REV), reversed rotation sign and the inverse
cyclic map must each be detected as mismatches. NEG-SWAPDEF is a degenerate CNOT whose control
reads past the end of the prefix and so acts as the identity.
"""
from fractions import Fraction as F
from itertools import product
import sys


class Q:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re - o.re, self.im - o.im)

    def __neg__(self):
        return Q(-self.re, -self.im)

    def __mul__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return Q(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return Q(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, Q) else Q(o)
        return self.re == o.re and self.im == o.im

    def iszero(self):
        return self.re == 0 and self.im == 0


I_ = Q(0, 1)

# ---- one-token matrices (as dicts (i,j)->Q over Fin 2) -------------------------------------
def m2(a, b, c, d):
    return {(0, 0): a, (0, 1): b, (1, 0): c, (1, 1): d}

ONE2 = m2(Q(1), Q(0), Q(0), Q(1))
XM = m2(Q(0), Q(1), Q(1), Q(0))                                     # EqvK2Generation.Xm
PAULI = [ONE2, XM, m2(Q(0), -I_, I_, Q(0)), m2(Q(1), Q(0), Q(0), Q(-1))]  # EqvK2Schema.pauli
CYC = m2(Q(F(1, 2), F(-1, 2)), Q(F(-1, 2), F(-1, 2)), Q(F(1, 2), F(-1, 2)), Q(F(1, 2), F(1, 2)))  # cycMat

def phaseMat(c, s):                                                   # EqvK2Converse.phaseMat
    return m2(Q(1), Q(0), Q(0), Q(c, s))

# ---- recursive carriers: Bits n elements as tuples (b_0, ..., b_{n-1}); p.1 = prefix, p.2 = last
def bits(n):
    return list(product(range(2), repeat=n))

def labels(n):
    return list(product(range(4), repeat=n))

def bitAt(n, i, b):          # FiniteReach.bitAt, literally
    if n == 0:
        return 0
    return b[n - 1] if i == n - 1 else bitAt(n - 1, i, b[:-1])

def ident(n):
    return {(a, b): Q(1 if a == b else 0) for a in bits(n) for b in bits(n)}

def tensorOf(P, Q2, n):      # P on Bits n, Q2 on Fin 2 -> Bits (n+1)
    return {(a + (i,), b + (j,)): P[(a, b)] * Q2[(i, j)]
            for a in bits(n) for b in bits(n) for i in range(2) for j in range(2)}

def blockFam(n, U):          # FiniteReach.blockFam
    return {(a + (i,), b + (j,)): (U(a)[(i, j)] if a == b else Q(0))
            for a in bits(n) for b in bits(n) for i in range(2) for j in range(2)}

def flipX(c):
    return XM if c == 1 else ONE2

def cnotM(n, i, j, swap=False):   # FiniteReach.cnotM; swap=True is a deliberately wrong variant
    if n == 0:
        return ident(0)
    m = n - 1
    if j == m:
        if swap:
            return blockFam(m, lambda b: flipX(bitAt(m, j, b)))
        return blockFam(m, lambda b: flipX(bitAt(m, i, b)))
    return tensorOf(cnotM(m, i, j, swap), ONE2, m)

def localM(n, j, V):         # FiniteReach.localM
    if n == 0:
        return ident(0)
    m = n - 1
    if j == m:
        return tensorOf(ident(m), V, m)
    return tensorOf(localM(m, j, V), ONE2, m)

def matmul(A, B, n):
    # sparse product; result is total over Bits n x Bits n (zeros filled in)
    bs = bits(n)
    rows = {}
    for (b, c), v in B.items():
        if not v.iszero():
            rows.setdefault(b, []).append((c, v))
    out = {(a, c): Q(0) for a in bs for c in bs}
    for (a, b), u in A.items():
        if u.iszero():
            continue
        for c, v in rows.get(b, ()):
            out[(a, c)] = out[(a, c)] + u * v
    return out

def ctrans(A, n):
    return {(a, b): A[(b, a)].conj() for a in bits(n) for b in bits(n)}

def pauliWord(n, mu):        # FinitePauli.pauliWord, literally recursive
    if n == 0:
        return ident(0)
    return tensorOf(pauliWord(n - 1, mu[:-1]), PAULI[mu[-1]], n - 1)

_PW = {}
def pw(n, mu):
    key = (n, mu)
    if key not in _PW:
        _PW[key] = pauliWord(n, mu)
    return _PW[key]

_PWNZ = {}
def pw_nz(n, mu):
    key = (n, mu)
    if key not in _PWNZ:
        _PWNZ[key] = [(ab, x) for ab, x in pw(n, mu).items() if not x.iszero()]
    return _PWNZ[key]

def dictionary(n, w):        # FinitePauli.dictionary
    bs = bits(n)
    out = {(a, b): Q(0) for a in bs for b in bs}
    for mu, val in w.items():
        if val == 0:
            continue
        for key, x in pw_nz(n, mu):
            out[key] = out[key] + x * Q(F(val) / 2 ** n)
    return out

def coordinates(n, H):       # FinitePauli.coordinates: Re Tr(P_mu H)
    bs = bits(n)
    res = {}
    for mu in labels(n):
        tr = Q(0)
        for (a, b), x in pw_nz(n, mu):
            tr = tr + x * H[(b, a)]
        res[mu] = tr.re
    return res

def tabAct(n, U, w):         # FiniteReachTable.tabAct
    return coordinates(n, matmul(matmul(U, dictionary(n, w), n), ctrans(U, n), n))

# ---- #829's proposed coordinate actions, from the landed sgn / pc / pt / homMap -----------
def sgn(m, v):
    return -1 if (m == 1 and v == 3) or (m == 2 and v == 2) else 1

PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]

def update(mu, i, v):
    mu = list(mu)
    mu[i] = v
    return tuple(mu)

def cnotK(n, i, j, w):
    out = {}
    for mu in labels(n):
        a, b = mu[i], mu[j]
        src = update(update(mu, i, PC[a][b]), j, PT[a][b])
        out[mu] = sgn(a, b) * w.get(src, F(0))
    return out

def homMatrix(N):            # 4x4 homogenized matrix of a linear map N on R^3
    M = [[F(0)] * 4 for _ in range(4)]
    M[0][0] = F(1)
    for r in range(3):
        for c in range(3):
            M[r + 1][c + 1] = F(N[r][c])
    return M

def rotLin(c, s):            # KInfFoundations.rotLin via homMap_rotLin: (x0,x1,x2) -> (c x0 - s x1, s x0 + c x1, x2)
    return [[c, -s, 0], [s, c, 0], [0, 0, 1]]

CYCEQ = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]      # cycEquiv v = (v2, v0, v1)
CYCEQ_INV = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]

def actK(n, j, N, w):
    M = homMatrix(N)
    out = {}
    for mu in labels(n):
        out[mu] = sum((M[mu[j]][v] * w.get(update(mu, j, v), F(0)) for v in range(4)), F(0))
    return out

# ---- comparison -----------------------------------------------------------------------------
def basis(n, nu):
    return {nu: F(1)}

_IMG = {}
def images(n, U, tag):
    if tag not in _IMG:
        _IMG[tag] = {nu: tabAct(n, U, basis(n, nu)) for nu in labels(n)}
    return _IMG[tag]

def same_images(n, imgs, g):
    for nu in labels(n):
        a, b = imgs[nu], g(basis(n, nu))
        for mu in labels(n):
            if a.get(mu, F(0)) != b.get(mu, F(0)):
                return False
    return True

def same_action(n, f, g):
    for nu in labels(n):
        e = basis(n, nu)
        a, b = f(e), g(e)
        for mu in labels(n):
            if a.get(mu, F(0)) != b.get(mu, F(0)):
                return False
    return True

CHECKS = []
def check(code, cond):
    CHECKS.append((code, bool(cond)))
    print(("PASS " if cond else "FAIL ") + code)

ANGLES = [(F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(0), F(-1))]

def run():
    for k in range(1, 5):
        # dictionary = #829 dictK under the token identification (entry = prod_i pauli(mu_i)(a_i)(b_i))
        okd = True
        for mu in labels(k):
            P = pw(k, mu)
            for a in bits(k):
                for b in bits(k):
                    x = Q(1)
                    for t in range(k):
                        x = x * PAULI[mu[t]][(a[t], b[t])]
                    if not (P[(a, b)] == x):
                        okd = False
        check(f"DICTK-k{k}", okd)
        for i in range(k):
            for j in range(i + 1, k):
                im = images(k, cnotM(k, i, j), ("cnot", k, i, j))
                check(f"CNOT-k{k}-{i}->{j}", same_images(k, im, lambda w: cnotK(k, i, j, w)))
                # countercontrols: reversed direction and swapped-definition must be detected
                check(f"NEG-REV-k{k}-{i}->{j}", not same_images(k, im, lambda w: cnotK(k, j, i, w)))
                imsw = images(k, cnotM(k, i, j, swap=True), ("cnotsw", k, i, j))
                check(f"NEG-SWAPDEF-k{k}-{i}->{j}", not same_images(k, imsw, lambda w: cnotK(k, i, j, w)))
        for j in range(1, k):
            for (c, s) in ANGLES:
                im = images(k, localM(k, j, phaseMat(c, s)), ("rot", k, j, c, s))
                check(f"ROT-k{k}-t{j}-({c},{s})", same_images(k, im, lambda w: actK(k, j, rotLin(c, s), w)))
                if s != 0:
                    check(f"NEG-ROTSIGN-k{k}-t{j}-({c},{s})", not same_images(k, im, lambda w: actK(k, j, rotLin(c, -s), w)))
            im = images(k, localM(k, j, CYC), ("cyc", k, j))
            check(f"CYC-k{k}-t{j}", same_images(k, im, lambda w: actK(k, j, CYCEQ, w)))
            check(f"NEG-CYCINV-k{k}-t{j}", not same_images(k, im, lambda w: actK(k, j, CYCEQ_INV, w)))

    # ---- countermodels under the literal design definitions ---------------------------------
    def vec_apply(U, x, n):
        return {a: sum((U[(a, b)] * x[b] for b in bits(n)), Q(0)) for a in bits(n)}

    def proj(x, n):
        return {(a, b): x[a] * x[b].conj() for a in bits(n) for b in bits(n)}

    def pt_first(R, n):      # partial transpose on token 0 (index position 0)
        return {(a, b): R[((b[0],) + a[1:], (a[0],) + b[1:])] for a in bits(n) for b in bits(n)}

    def pt_last(R, n):       # partial transpose on token n-1
        return {(a, b): R[(a[:-1] + (b[-1],), b[:-1] + (a[-1],))] for a in bits(n) for b in bits(n)}

    def min_2x2(R, a, b):
        return R[(a, a)] * R[(b, b)] - R[(a, b)] * R[(b, a)]

    h = F(1, 2)
    # SEP3: CNOT(0->1) |+00>, |+> = (1,1)/sqrt2 handled by the 1/2 in the projector
    x = {a: Q(1 if (a[1] == 0 and a[2] == 0) else 0) for a in bits(3)}          # (1,1)(x)|0>(x)|0>
    y = vec_apply(cnotM(3, 0, 1), x, 3)
    R = {key: v * Q(h) for key, v in proj(y, 3).items()}
    G = pt_first(R, 3)
    check("SEP3-literal-minor(-1/4)", min_2x2(G, (0, 1, 0), (1, 0, 0)) == Q(F(-1, 4)))
    # CUT3: CNOT(1->2) (Bell_01 (x) |0>) = GHZ; partial transpose across 01|2
    x = {a: Q(1 if (a[0] == a[1] and a[2] == 0) else 0) for a in bits(3)}
    y = vec_apply(cnotM(3, 1, 2), x, 3)
    check("CUT3-literal-GHZ", all(y[a] == Q(1 if a in ((0, 0, 0), (1, 1, 1)) else 0) for a in bits(3)))
    R = {key: v * Q(h) for key, v in proj(y, 3).items()}
    G = pt_last(R, 3)
    check("CUT3-literal-minor(-1/4)", min_2x2(G, (0, 0, 1), (1, 1, 0)) == Q(F(-1, 4)))
    # SHIFT3: A = I - 2 P000; product value -1 (hmax violated); A + Tr(A)/6 I = 2I - 2P000 >= 0
    A = {(a, b): Q((1 if a == b else 0) - (2 if a == b == (0, 0, 0) else 0)) for a in bits(3) for b in bits(3)}
    check("SHIFT3-product-value(-1)", A[((0, 0, 0), (0, 0, 0))] == Q(-1))
    # CM1: H = S (x) I (x) I with S = I - (626/625) w w^T, w = (3,4)/5, token 0 = first factor
    S = m2(Q(1 - F(626, 625) * F(9, 25)), Q(-F(626, 625) * F(12, 25)), Q(-F(626, 625) * F(12, 25)), Q(1 - F(626, 625) * F(16, 25)))
    H = tensorOf(tensorOf(tensorOf(ident(0), S, 0), ONE2, 1), ONE2, 2)
    p = {a: Q((3 if a[0] == 0 else 4) if (a[1] == 0 and a[2] == 0) else 0) for a in bits(3)}
    val = sum((p[a].conj() * H[(a, b)] * p[b] for a in bits(3) for b in bits(3)), Q(0))
    check("CM1-hmax-violated(-1/25)", val == Q(F(-1, 25)))
    # Gamma-Q3 at k=2 (partial transpose on token 1): CNOT(0->1)|+0> = Bell; Gamma(Bell) has
    # singlet value -1/2 (normalized), so Bell is not in Gamma-Q3: hH2 is violated.
    x = {a: Q(1 if a[1] == 0 else 0) for a in bits(2)}
    y = vec_apply(cnotM(2, 0, 1), x, 2)
    R = {key: v * Q(h) for key, v in proj(y, 2).items()}
    G = pt_last(R, 2)
    s_ = {(0, 0): Q(0), (0, 1): Q(1), (1, 0): Q(-1), (1, 1): Q(0)}
    sval = sum((s_[a].conj() * G[(a, b)] * s_[b] for a in bits(2) for b in bits(2)), Q(0)) * Q(h)
    check("GQ3-hH2-violated(-1/2)", sval == Q(F(-1, 2)))
    # Gamma-Q3 satisfies hA: Gamma o Ad(localM 2 1 V) o Gamma = Ad(localM 2 1 conj(V)) on all units
    def conjm(V):
        return {key: v.conj() for key, v in V.items()}
    okA = True
    for V in [phaseMat(F(3, 5), F(4, 5)), CYC]:
        L = localM(2, 1, V)
        Lb = localM(2, 1, conjm(V))
        for a0 in bits(2):
            for b0 in bits(2):
                E = {(a, b): Q(1 if (a, b) == (a0, b0) else 0) for a in bits(2) for b in bits(2)}
                lhs = pt_last(matmul(matmul(L, pt_last(E, 2), 2), ctrans(L, 2), 2), 2)
                rhs = matmul(matmul(Lb, E, 2), ctrans(Lb, 2), 2)
                if any(not (lhs[key] == rhs[key]) for key in lhs):
                    okA = False
    check("GQ3-hA-intertwining", okA)

    fails = [c for c, ok in CHECKS if not ok]
    print(f"checks: {len(CHECKS)}, failures: {len(fails)}")
    print("VERDICT " + ("TABACT-MATCHES-829-FORMULAS-k1..4" if not fails else "NOT-ESTABLISHED"))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(run())
