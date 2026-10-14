"""Thread E exact check: CHSH content of the kernel's pair-table objects at M = 5bfdaba6.

Transcribes, from verification/lean-mathlib/OIBridge/CompositeDimension.lean at M, the objects
hom (:100), prodState (:161), pairVal (:164), actT (:198), sgn/pc/pt/cnotFun (:741-758),
xplus/z3/phiW (:793, :1213, :1220); from EffectSpace.lean sharpVec/sharpEff (:57-67); from
EqvK2Schema.lean pauli (:25), tokMat/dict (:74-80); from K2Guard.lean reflY (:46), idW (:101).
Arithmetic is exact: Fractions, Q(sqrt 2) and Gaussian rationals. Standard library only.
Finite checks are controls; universal statements are written arguments in the note.
Usage: python3 -I -B e_bell_check.py [--mutate M1|M2|M3]
"""
from fractions import Fraction as Fr
import sys

MUT = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--mutate" else None


class S2:
    """a + b*sqrt(2), a, b rational."""
    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)
    def __add__(s, o):
        o = o if isinstance(o, S2) else S2(o)
        return S2(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s):
        return S2(-s.a, -s.b)
    def __sub__(s, o):
        return s + (-(o if isinstance(o, S2) else S2(o)))
    def __rsub__(s, o):
        return S2(o) - s
    def __mul__(s, o):
        o = o if isinstance(o, S2) else S2(o)
        return S2(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def sign(s):
        # sign of a + b sqrt2
        if s.a == 0 and s.b == 0:
            return 0
        if s.a >= 0 and s.b >= 0:
            return 1
        if s.a <= 0 and s.b <= 0:
            return -1
        # opposite signs: compare a^2 with 2 b^2
        if s.a > 0:  # b < 0
            return 1 if s.a * s.a > 2 * s.b * s.b else -1
        return 1 if 2 * s.b * s.b > s.a * s.a else -1
    def __eq__(s, o):
        o = o if isinstance(o, S2) else S2(o)
        return s.a == o.a and s.b == o.b
    def __le__(s, o):
        return (s - o).sign() <= 0
    def __ge__(s, o):
        return (s - o).sign() >= 0
    def __repr__(s):
        return f"{s.a}+{s.b}*sqrt2"


R2 = S2(0, Fr(1, 2))  # 1/sqrt2

# ---- CompositeDimension objects (d = 3) ----
def hom(x):
    return [S2(1)] + [xi if isinstance(xi, S2) else S2(xi) for xi in x]

def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[m] * hy[n] for n in range(4)] for m in range(4)]

def pairVal(a, b, w):
    tot = S2(0)
    for m in range(4):
        for n in range(4):
            tot = tot + a[m] * w[m][n] * b[n]
    return tot

def sgn(m, n):
    if MUT == "M1":
        return 1
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1

PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]

def cnot(w):
    return [[sgn(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]

def homMap(Ndiag, v):
    return [v[0]] + [Ndiag[j] * v[j + 1] for j in range(3)]

def actT(Ndiag, w):
    return [homMap(Ndiag, w[m]) for m in range(4)]

xplus = [1, 0, 0]
z3 = [0, 0, 1]
phiW = [[S2((-1 if m == 2 else 1) if m == n else 0) for n in range(4)] for m in range(4)]
idW = [[S2(1 if m == n else 0) for n in range(4)] for m in range(4)]
reflY = [1, -1, 1]

# ---- EffectSpace sharp effects ----
def sharpVec(b):
    return [S2(Fr(1, 2))] + [(bj if isinstance(bj, S2) else S2(bj)) * Fr(1, 2) for bj in b]

def neg(v):
    return [-(c if isinstance(c, S2) else S2(c)) for c in v]

def prob(w, a, s, b, t):
    """P(outcome s on token 1 along a, outcome t on token 2 along b): product sharp effects."""
    av = a if s == 1 else neg(a)
    bv = b if t == 1 else neg(b)
    return pairVal(sharpVec(av), sharpVec(bv), w)

def corr(w, a, b):
    if MUT == "M2":
        return sum((prob(w, a, s, b, t) for s in (1, -1) for t in (1, -1)), S2(0))
    return sum((s * t * prob(w, a, s, b, t) for s in (1, -1) for t in (1, -1)), S2(0))

def chsh(w, A, B):
    return corr(w, A[0], B[0]) + corr(w, A[0], B[1]) + corr(w, A[1], B[0]) - corr(w, A[1], B[1])

checks, fails = 0, 0
def check(name, cond):
    global checks, fails
    checks += 1
    if cond:
        print("PASS", name)
    else:
        fails += 1
        print("FAIL", name)

# Tsirelson settings: A0 = x, A1 = z, B0 = (x+z)/sqrt2, B1 = (x-z)/sqrt2
A = [[S2(1), S2(0), S2(0)], [S2(0), S2(0), S2(1)]]
B = [[R2, S2(0), R2], [R2, S2(0), -R2]]

# C1 the kernel's entangling chain
pre = prodState(xplus, z3)
if MUT == "M3":
    state = pre
else:
    state = cnot(pre)
check("C1 cnot(prodState xplus z3) = phiW (CompositeDimension.lean:1222)", cnot(pre) == phiW)

# C2 valid probabilities on all four setting pairs
ok = True
for a in A:
    for b in B:
        ps = [prob(state, a, s, b, t) for s in (1, -1) for t in (1, -1)]
        ok &= all(p >= 0 and p <= 1 for p in ps) and sum(ps, S2(0)) == S2(1)
check("C2 product sharp-test probabilities in [0,1], summing to 1", ok)

# C3 no-signalling marginals
ok = True
for s in (1, -1):
    for a in A:
        margs = [prob(state, a, s, b, 1) + prob(state, a, s, b, -1) for b in B]
        ok &= margs[0] == margs[1]
for t in (1, -1):
    for b in B:
        margs = [prob(state, a, 1, b, t) + prob(state, a, -1, b, t) for a in A]
        ok &= margs[0] == margs[1]
check("C3 marginals independent of the remote setting", ok)

# C4 Tsirelson value attained exactly
val = chsh(state, A, B)
print("   CHSH(phiW) =", val)
check("C4 CHSH(phiW) = 2*sqrt2 exactly", val == S2(0, 2))

# C5 correlator equals a^T T b (local terms cancel) on all setting pairs
ok = True
for a in A:
    for b in B:
        tb = sum((a[i] * state[i + 1][j + 1] * b[j] for i in range(3) for j in range(3)), S2(0))
        ok &= corr(state, a, b) == tb
check("C5 correlator = a^T T b with T the 3x3 block of the table", ok)

# C6 product-state control: CHSH <= 2 at the Tsirelson settings on a rational sphere grid
def sph(p, q):
    # rational points on the unit sphere by inverse stereographic projection
    den = 1 + p * p + q * q
    return [Fr(2 * p, den), Fr(2 * q, den), Fr(p * p + q * q - 1, den)]
grid = [sph(Fr(p, 2), Fr(q, 2)) for p in range(-4, 5) for q in range(-4, 5)]
ok = True
mx = S2(-10)
for x in grid[::3]:
    for y in grid[::3]:
        v = chsh(prodState(x, y), A, B)
        ok &= (v <= S2(2)) and (v >= S2(-2))
        if v >= mx:
            mx = v
check(f"C6 product tables: |CHSH| <= 2 on {len(grid[::3])**2} grid products", ok)

# C7 diagonal (computational-basis) tests only: every extreme dichotomic z-observable, CHSH <= 2
# observables alpha + gamma z with |alpha|+|gamma| <= 1; extreme points (+-1,0), (0,+-1)
def corr_obs(w, oa, ob):
    va = [oa[0], S2(0), S2(0), oa[1]]
    vb = [ob[0], S2(0), S2(0), ob[1]]
    return pairVal(va, vb, w)
ext = [(S2(1), S2(0)), (S2(-1), S2(0)), (S2(0), S2(1)), (S2(0), S2(-1))]
best = S2(-10)
for a0 in ext:
    for a1 in ext:
        for b0 in ext:
            for b1 in ext:
                v = corr_obs(phiW, a0, b0) + corr_obs(phiW, a0, b1) + corr_obs(phiW, a1, b0) - corr_obs(phiW, a1, b1)
                if v >= best:
                    best = v
print("   max CHSH(phiW) over diagonal observables =", best)
check("C7 diagonal-only local observables: max CHSH on phiW = 2", best == S2(2))

# C8 the one-copy reflection: actT reflY phiW = idW (K2Guard.lean:106); idW still reaches 2sqrt2
check("C8a actT reflY phiW = idW", actT(reflY, phiW) == idW)
Bref = [[b[0], -b[1], b[2]] for b in B]
check("C8b CHSH(idW) at reflected settings = 2*sqrt2", chsh(idW, A, Bref) == S2(0, 2))

# ---- Gaussian-rational dictionary checks (EqvK2Schema.dict) ----
class G:
    def __init__(s, re, im=0):
        s.re, s.im = Fr(re), Fr(im)
    def __add__(s, o):
        return G(s.re + o.re, s.im + o.im)
    def __mul__(s, o):
        return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s):
        return G(s.re, -s.im)
    def __eq__(s, o):
        return s.re == o.re and s.im == o.im

Z, O, I_ = G(0), G(1), G(0, 1)
pauli = [
    [[O, Z], [Z, O]],
    [[Z, O], [O, Z]],
    [[Z, G(0, -1)], [I_, Z]],
    [[O, Z], [Z, G(-1)]],
]
def kron(P, Q):
    return [[P[i // 2][k // 2] * Q[i % 2][k % 2] for k in range(4)] for i in range(4)]
def dict_(w):
    M = [[G(0) for _ in range(4)] for _ in range(4)]
    for m in range(4):
        for n in range(4):
            c = w[m][n]
            assert c.b == 0
            K = kron(pauli[m], pauli[n])
            for i in range(4):
                for k in range(4):
                    M[i][k] = M[i][k] + G(c.a / 4) * K[i][k]
    return M
def quad(M, v):
    tot = G(0)
    for i in range(4):
        for k in range(4):
            tot = tot + v[i].conj() * M[i][k] * v[k]
    return tot

Dphi = dict_(phiW)
bell = [[G(Fr(1, 2)) if (i in (0, 3) and k in (0, 3)) else G(0) for k in range(4)] for i in range(4)]
check("C9 dict(phiW) = |Phi+><Phi+| (index order (a,b) -> 2a+b)", Dphi == bell)
Did = dict_(idW)
sing = [G(0), G(1), G(-1), G(0)]
q = quad(Did, sing)
check("C10 dict(idW) has <psi-|.|psi-> = -1 (unnormalized): idW in maxCone, not in Q3", q == G(-1))
# C11 table correlators are trace pairings: T_ij = Tr(dict(phiW) sigma_i (x) sigma_j)
ok = True
for i in range(1, 4):
    for j in range(1, 4):
        K = kron(pauli[i], pauli[j])
        tr = G(0)
        for r in range(4):
            for c in range(4):
                tr = tr + Dphi[r][c] * K[c][r]
        ok &= tr == G(phiW[i][j].a)
check("C11 T_ij = Tr(dict(phiW) sigma_i (x) sigma_j) for i,j in 1..3", ok)

print(f"checks: {checks}, failures: {fails}")
print("VERDICT E-BELL-EXACT" if fails == 0 else "VERDICT E-BELL-FAILED")
