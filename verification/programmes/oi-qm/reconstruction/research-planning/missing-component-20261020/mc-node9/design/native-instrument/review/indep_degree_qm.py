"""Reviewer checks: (1) GF(2) degree of acceptance flags; alternatives of lower degree that give the exact menu laws;
(2) quantum record laws from density matrices and Lueders instruments (sympy, exact)."""
from itertools import product
from fractions import Fraction as Fr
import sympy as sp

def anf_degree(f, n):
    """f: function on n-bit tuples -> {0,1}. Moebius transform; returns algebraic degree."""
    t = [f(tuple((x >> i) & 1 for i in range(n))) for x in range(2 ** n)]
    for i in range(n):
        for x in range(2 ** n):
            if x >> i & 1: t[x] ^= t[x ^ (1 << i)]
    return max((bin(x).count('1') for x in range(2 ** n) if t[x]), default=-1)

# threshold flag u<10 on 4 bits (b0 = LSB)
thr = lambda b: int(b[0] + 2 * b[1] + 4 * b[2] + 8 * b[3] < 10)
print('per-component threshold flag u<10: degree', anf_degree(thr, 4), 'weight', sum(thr(b) for b in product((0, 1), repeat=4)))
joint = lambda b: thr(b[0:4]) & thr(b[4:8]) & thr(b[8:12]) & thr(b[12:16])
print('joint threshold flag (16 bits): degree', anf_degree(joint, 16))
# degree-2 per-component alternative: complement of bent function x0x1+x2x3, weight 10
bent = lambda b: 1 ^ (b[0] & b[1]) ^ (b[2] & b[3])
print('per-component flag 1+x0x1+x2x3: degree', anf_degree(bent, 4), 'weight', sum(bent(b) for b in product((0, 1), repeat=4)))
j2 = lambda b: bent(b[0:4]) & bent(b[4:8]) & bent(b[8:12]) & bent(b[12:16])
print('joint of four degree-2 flags: degree', anf_degree(j2, 16))
# single joint degree-3 flag on 6 bits: complement of x0x1x2 + x3x4x5, weight 50
g = lambda b: 1 ^ (b[0] & b[1] & b[2]) ^ (b[3] & b[4] & b[5])
A = [b for b in product((0, 1), repeat=6) if g(b)]
print('joint flag 1+x0x1x2+x3x4x5 on 6 bits: degree', anf_degree(g, 6), 'weight', len(A))
# Exact menu laws from it: (lam_X, lam_Y, lam_R) by lookup on A (50 elements); lam components with value 1/2 use
# three extra fair bits e1,e2,e3 (not in the flag). Check exact product law for all 8 stations, station-independent acceptance.
AXv = {'X': (1, 0, 0), 'Y': (0, 1, 0), 'Z': (0, 0, 1), 'R': (Fr(4, 5), Fr(3, 5), 0)}
N4 = ['X', 'Y', 'Z', 'R']
def born(c, w): return (1 + sum(Fr(x) * Fr(y) for x, y in zip(AXv[c], w))) / 2
ok = True
for n in N4:
    for sg in (1, -1):
        w = tuple(sg * Fr(x) for x in AXv[n])
        ps = [born(c, w) for c in N4]
        half = [i for i, p in enumerate(ps) if p == Fr(1, 2)]
        other = [i for i, p in enumerate(ps) if p != Fr(1, 2)]
        assert len(half) <= 3
        # build lookup: assign each element of A an 'other' pattern with exact counts 50*P
        pats = []
        for pat in product((0, 1), repeat=len(other)):
            pr = Fr(1)
            for i, v in zip(other, pat): pr *= ps[i] if v else 1 - ps[i]
            cnt = pr * 50
            if cnt.denominator != 1: ok = False; break
            pats += [pat] * int(cnt)
        if len(pats) != 50: ok = False; continue
        law = {}
        for a_el, pat in zip(A, pats):
            for e in product((0, 1), repeat=3):
                lam = [0] * 4
                for i, v in zip(other, pat): lam[i] = v
                for i, v in zip(half, e): lam[i] = v
                law[tuple(lam)] = law.get(tuple(lam), Fr(0)) + Fr(1, 50 * 8)
        for lam in product((0, 1), repeat=4):
            pr = Fr(1)
            for i in range(4): pr *= ps[i] if lam[i] else 1 - ps[i]
            ok &= law.get(lam, Fr(0)) == pr
print('degree-3 single joint flag (6 bits, accept 50/64 for every station) + 3 free fair bits gives exact product law for all 8 stations:', ok)
# Lower bound: any degree<=1 flag has weight in {0, 2^(n-1), 2^n} -> dyadic conditionals. Quick exhaustive confirm n<=5.
for n in range(1, 6):
    ws = set()
    for coeffs in product((0, 1), repeat=n + 1):
        f = lambda b: (coeffs[0] + sum(c * x for c, x in zip(coeffs[1:], b))) & 1
        ws.add(sum(f(b) for b in product((0, 1), repeat=n)))
    print('n=%d affine-function weights:' % n, sorted(ws))
# degree-2 flag with weight divisible by 25 (single station-independent herald for the joint law): quadratic weights are
# 2^(n-1) +- 2^(n-1-h); 2^h+1 = 1025 = 25*41 at h=10, so n=20 works with weight 2^9*1025.
print('2^10+1 =', 2 ** 10 + 1, '= 25*41:', 2 ** 10 + 1 == 25 * 41, '; weight 2^9*1025 / 50 =', Fr(2 ** 9 * 1025, 50))

# ---------- quantum laws from density matrices (exact)
I2 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
def op(v): return (I2 + sp.Rational(v[0]) * sx + sp.Rational(v[1]) * sy + sp.Rational(v[2]) * sz) / 2
def rv(v): return tuple(sp.Rational(str(x)) for x in v)
okq = True
for n in N4:
    for sg in (1, -1):
        w = tuple(sg * Fr(x) for x in AXv[n]); rho = op(rv(w))
        for a in N4:
            for o in (0, 1):
                Pi = op(rv(AXv[a])) if o else op(rv(tuple(-x for x in AXv[a])))
                po = sp.nsimplify(sp.simplify((Pi * rho).trace()))
                okq &= po == sp.Rational(str(born(a, w) if o else 1 - born(a, w)))
                if po == 0: continue
                post = sp.simplify(Pi * rho * Pi / po)
                for c in N4:
                    Pc = op(rv(AXv[c]))
                    p2 = sp.nsimplify(sp.simplify((Pc * post).trace()))
                    s = 1 if o else -1
                    okq &= p2 == sp.Rational(str((1 + s * sum(Fr(x) * Fr(y) for x, y in zip(AXv[a], AXv[c]))) / 2))
print('density-matrix Born and Lueders second-read values equal (1+a.w)/2 and (1+s a.c)/2 for all stations/axes:', okq)
