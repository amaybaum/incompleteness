#!/usr/bin/env python3
"""p5_m1_retained_law.py -- exact (Fractions, standard library).  Research only; decides no round.

Decision (c), M1: the monitored law must survive on the retained original OI protocols.  For a
conservative extension (CONS: permClass <= I, configuration carrier kept, native readout kept as
the local Lueders projection, `readout_is_localLuders`), a retained protocol is built only from
native permutations and native readouts.  This probe computes, for OI's q = 3 leap
L_m(x, xi) = (m x - xi, x) with registered start x0 = a and hidden xi0 uniform (the protocol of
check B, f2-census-checks/monitored_law.py):
  (OI)   the classical trajectory law P(x1, x2 | x0), x1 and x2 read without disturbance;
  (CONS) the same protocol run as a quantum protocol on C^9 (permutation unitary, Lueders readout
         of the visible value), from the diagonal start and from a coherent start (hidden in a
         Fourier state), entrywise;
Controls that must FAIL the equality (so the comparison can fail):
  (RR)   re-randomizing readout at t = 1 (E1's back-acting law);
  (NEW)  a new X-supplied operation inserted between the steps (Fourier map on the hidden half):
         a new protocol, whose law is a prediction under M1, not a retained-law obligation.
"""
from fractions import Fraction as Fr
from itertools import product
q = 3
# exact arithmetic in Q(omega), omega = e^{2 pi i/3}: represent x + y*omega, omega^2 = -1 - omega
class W:
    __slots__ = ('x', 'y')
    def __init__(s, x=0, y=0): s.x = Fr(x); s.y = Fr(y)
    def __add__(s, o): return W(s.x + o.x, s.y + o.y)
    def __sub__(s, o): return W(s.x - o.x, s.y - o.y)
    def __mul__(s, o):  # (a + b w)(c + d w) = ac + (ad + bc) w + bd w^2
        a, b, c_, d = s.x, s.y, o.x, o.y
        return W(a*c_ - b*d, a*d + b*c_ - b*d)
    def conj(s):  # conj(w) = w^2 = -1 - w
        return W(s.x - s.y, -s.y)
    def iszero(s): return s.x == 0 and s.y == 0
def omega(k): return [W(1), W(0, 1), W(-1, -1)][k % 3]
idx = lambda x, xi: 3*x + xi
D = 9
def zeros(): return [[W() for _ in range(D)] for _ in range(D)]
def mm(A, B):
    R = zeros()
    for i in range(D):
        for k in range(D):
            if A[i][k].iszero(): continue
            for j in range(D):
                if not B[k][j].iszero(): R[i][j] = R[i][j] + A[i][k]*B[k][j]
    return R
def dag(A): return [[A[j][i].conj() for j in range(D)] for i in range(D)]
def perm_unitary(f):
    U = zeros()
    for x, xi in product(range(q), repeat=2):
        y, eta = f(x, xi); U[idx(y, eta)][idx(x, xi)] = W(1)
    return U
def proj_vis(k):
    P = zeros()
    for xi in range(q): P[idx(k, xi)][idx(k, xi)] = W(1)
    return P
def tr(A):
    s = W()
    for i in range(D): s = s + A[i][i]
    return s
def real(z):
    assert z.y == 0; return z.x
F = zeros()  # Fourier on the hidden half, unnormalized (normalization 1/3 applied to the state)
for x, xi, eta in product(range(q), repeat=3): F[idx(x, eta)][idx(x, xi)] = omega(xi*eta)
ok = True
summary = {}
for m in range(q):
    L = lambda x, xi, m=m: ((m*x - xi) % q, x)
    U = perm_unitary(L); Ud = dag(U)
    Fd = dag(F)
    for a in range(q):
        oi = {k: Fr(0) for k in product(range(q), repeat=2)}; rr = dict(oi)
        for xi0 in range(q):
            x1, xi1 = L(a, xi0); x2, _ = L(x1, xi1); oi[(x1, x2)] += Fr(1, q)
            for xir in range(q):
                y2, _ = L(x1, xir); rr[(x1, y2)] += Fr(1, q*q)
        rho_d = zeros()
        for xi in range(q): rho_d[idx(a, xi)][idx(a, xi)] = W(Fr(1, q))
        rho_c = zeros()   # |a> (x) (uniform superposition over xi), a coherent start with the same diagonal
        for xi, xj in product(range(q), repeat=2): rho_c[idx(a, xi)][idx(a, xj)] = W(Fr(1, q))
        def law(rho, insert=None):
            out = {}
            r1 = mm(mm(U, rho), Ud)
            for k in range(q):
                rk = mm(mm(proj_vis(k), r1), proj_vis(k))
                if insert is not None:
                    rk = mm(mm(insert, rk), dag(insert)); rk = [[z*W(Fr(1, 3)) for z in row] for row in rk]
                r2 = mm(mm(U, rk), Ud)
                for l in range(q):
                    out[(k, l)] = real(tr(mm(mm(proj_vis(l), r2), proj_vis(l))))
            return out
        cd, cc, cn = law(rho_d), law(rho_c), law(rho_d, insert=F)
        summary[(m, a)] = (cd == oi, cc == oi, rr != oi, cn != oi)
for (m, a), (e1, e2, n1, n2) in sorted(summary.items()):
    print('m=%d a=%d  CONS(diag)==OI: %s  CONS(coherent)==OI: %s  RR!=OI: %s  NEW!=OI: %s' % (m, a, e1, e2, n1, n2))
eq_all = all(v[0] and v[1] for v in summary.values())
rr_can_fail = any(v[2] for v in summary.values()); new_can_fail = any(v[3] for v in summary.values())
ok = rr_can_fail and new_can_fail
if not ok:
    print('VERDICT VOID (a negative control did not separate)')
else:
    print('VERDICT M1-CONS: retained-protocol monitored law %s under the conservative extension at q = 3 '
          '(diagonal and coherent starts); the RR readout and a new inserted operation each change the law.'
          % ('REPRODUCED entrywise' if eq_all else 'NOT reproduced'))
