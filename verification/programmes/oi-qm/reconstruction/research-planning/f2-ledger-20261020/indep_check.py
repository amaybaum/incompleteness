"""indep_check.py -- independent re-check of the decisive facts of reg3_exclusion.py (research only).

Separate code path: no SymPy, no Kronecker helper, no shared functions. Gaussian rationals are pairs of
Fractions; matrices are dicts. Operators are built from their action on configurations directly.

Checks:
  I1  each defect z_(s,t) = (I + s XZ + t YY - st ZX)/4, built entrywise from Pauli action tables,
      is mapped onto the defect set by every one of the 24 permutations of the 4 pair configurations;
  I2  Y = Ad_C (z_(1,1) (x) |0><0|), C: |x1 x2 x3> -> |x1 x2 (x3 xor x1 xor x2)>, has a negative value on
      the product test |+i>|-i>|+i> and on the real test (2,1)(1,2)(3,1);
  I3  the same Y is nonnegative on all 8 configuration tests (control);
  I4  P_m = I/2 - z_(1,1): readout-branch construction from (1,u1)(1,u2)(1,u3) through the inverse of the
      weight<=1 permutation and discard reproduces a matrix proportional to P_m; Tr(z P_m) = -1/2.
"""
import itertools
import sys
from fractions import Fraction as F

FAILS = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


class G:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re + o.re, s.im + o.im)

    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re - o.re, s.im - o.im)

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)

    __rmul__ = __mul__

    def conj(s):
        return G(s.re, -s.im)

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.re == o.re and s.im == o.im

    def __repr__(s):
        return f"({s.re}+{s.im}i)"


# single-token Pauli action: P|b> = coeff |b'>
PAULI = {
    "I": {0: (0, G(1)), 1: (1, G(1))},
    "X": {0: (1, G(1)), 1: (0, G(1))},
    "Y": {0: (1, G(0, 1)), 1: (0, G(0, -1))},
    "Z": {0: (0, G(1)), 1: (1, G(-1))},
}


def pauli2(p, q):
    """4x4 matrix of p (x) q as dict[(row,col)] over configs 2*b1+b2."""
    M = {}
    for b1, b2 in itertools.product((0, 1), repeat=2):
        r1, c1 = PAULI[p][b1]
        r2, c2 = PAULI[q][b2]
        M[(2 * r1 + r2, 2 * b1 + b2)] = c1 * c2
    return M


def lin(terms):
    M = {}
    for coef, mat in terms:
        for kk, v in mat.items():
            M[kk] = M.get(kk, G(0)) + v * coef
    return {kk: v for kk, v in M.items() if not v == 0}


def defect(s, t):
    q = F(1, 4)
    return lin([(G(q), pauli2("I", "I")), (G(s * q), pauli2("X", "Z")), (G(t * q), pauli2("Y", "Y")),
                (G(-s * t * q), pauli2("Z", "X"))])


defs = {(s, t): defect(s, t) for s in (1, -1) for t in (1, -1)}


def same(A, B):
    keys = set(A) | set(B)
    return all(A.get(kk, G(0)) == B.get(kk, G(0)) for kk in keys)


ok = True
for perm in itertools.permutations(range(4)):
    for z in defs.values():
        img = {(perm[r], perm[c]): v for (r, c), v in z.items()}
        if not any(same(img, w) for w in defs.values()):
            ok = False
check("I1 every permutation of the 4 pair configurations maps the defect set onto itself", ok)

z = defs[(1, 1)]


def cmap(x):  # x = (x1,x2,x3)
    return (x[0], x[1], x[2] ^ x[0] ^ x[1])


def lift(z4):
    """z4 (x) |0><0| on 3 tokens, then Ad_C, as dict over 3-bit tuples."""
    Y8 = {}
    for (r, c), v in z4.items():
        xr = (r >> 1, r & 1, 0)
        xc = (c >> 1, c & 1, 0)
        Y8[(cmap(xr), cmap(xc))] = v
    return Y8


def test_value(Y8, a, b, c):
    def amp(x):
        return a[x[0]] * b[x[1]] * c[x[2]]
    tot = G(0)
    for (xr, xc), v in Y8.items():
        tot = tot + amp(xr).conj() * v * amp(xc)
    return tot


Y8 = lift(z)
pi_ = (G(1), G(0, 1))
mi_ = (G(1), G(0, -1))
v1 = test_value(Y8, pi_, mi_, pi_)
check(f"I2a value on |+i>|-i>|+i> is {v1} (negative real)", v1.im == 0 and v1.re < 0)
v2 = test_value(Y8, (G(2), G(1)), (G(1), G(2)), (G(3), G(1)))
check(f"I2b value on real test (2,1)(1,2)(3,1) is {v2} (negative real)", v2.im == 0 and v2.re < 0)
cfg = [(G(1), G(0)), (G(0), G(1))]
mn = min(test_value(Y8, a, b, c).re for a, b, c in itertools.product(cfg, repeat=3))
check(f"I3 control: configuration tests give minimum {mn} >= 0", mn >= 0)

# I4: P_m = I/2 - z; build its -1/2 eigenvector by inspection-free route: P_m is rank one, take a nonzero column
Pm = lin([(G(F(1, 2)), pauli2("I", "I")), (G(-1), z)])
col = None
for cidx in range(4):
    colv = [Pm.get((r, cidx), G(0)) for r in range(4)]
    if any(not e == 0 for e in colv):
        col = colv
        break
# normalise so that entry 0 equals 1 (requires col[0] != 0)
check("I4a P_m has a column with nonzero first entry", col is not None and not col[0] == 0)
den = col[0]
# divide by Gaussian rational
nrm = den.re * den.re + den.im * den.im
inv = G(den.re / nrm, -den.im / nrm)
u = [e * inv for e in col]
# weight<=1 set T = 000,100,010,001 <- slice (x1,x2,0) for x = 00,01,10,11 (same ordering as the main script)
slice0 = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)]
T = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
inv_sigma = {t_: s_ for s_, t_ in zip(slice0, T)}   # only the part of sigma^-1 that lands in the slice matters
a = (G(1), u[1])
b = (G(1), u[2])
c = (G(1), u[3])
branch = {}
for x in itertools.product((0, 1), repeat=3):
    amp = a[x[0]] * b[x[1]] * c[x[2]]
    if x in inv_sigma:                     # sigma^-1 maps x into the slice x3 = 0; readout outcome 0 keeps it
        y = inv_sigma[x]
        branch[(y[0], y[1])] = amp
out = {}
for (p1, p2), va in branch.items():
    for (q1, q2), vb in branch.items():
        out[(2 * p1 + p2, 2 * q1 + q2)] = va * vb.conj()
# proportionality to P_m: out = lambda * P_m with lambda = out[0,0] / Pm[0,0]
lam_num = out[(0, 0)]
p00 = Pm[(0, 0)]
prop = all((out.get((r, cc), G(0)) * p00) == (Pm.get((r, cc), G(0)) * lam_num) for r in range(4) for cc in range(4))
check("I4b generated readout branch, discarded, is proportional to P_m", prop)
tr = G(0)
for (r, cc), v in z.items():
    tr = tr + v * Pm.get((cc, r), G(0))
check(f"I4c Tr(z P_m) = {tr} = -1/2", tr == G(F(-1, 2)))
sys.exit(1 if FAILS else 0)
