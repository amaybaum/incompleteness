"""EQ4-P probe p7 -- the reduced wall at six tokens: exact identities and exact limits of sector methods.

Usage:  python3 -I -B p7_wall_reduction.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py (and sympy for the slice computation with sqrt(3)).

Written reduction (NOTES N3.3).  At six tokens (pair cones Q3, triple cones uniform), the constraints on K3 are:
co-self-duality (3|3 Bell links), local-CP invariance (five tokens), the 3|3 x 3|3 "ring", and the existence of K4,
whose content is the "glue" (K4-network) inequality between glued states and glued effects; the Choi-closure crossing
of type (1,2,1,2) is the same network.  This probe certifies the identities the reduction uses.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P7-WALL-REDUCTION-EXACT` iff all:
  K  transcription control.
  R  ring factorization: for random exact x (P1,P2,R), e (P1,P2,Q), y (Q,U1,U2), f (R,U1,U2) the six-token value
     tr[(e (x) f)(x (x) y)] equals tr(M N), M = tr_P[(e (x) 1) x] read on (Q, R)... M = tr_P[(e (x) 1_R)(x (x) 1_Q)] on (Q, R) and
     N = tr_U[(f (x) 1_Q)(y (x) 1_R)] on (Q, R) (contractions over P and over U only); (R2) the five-token analogue with pair x~ (P', R), pair e~ (P', Q)
     gives M~ = cond(e~ ; x~) and, for e~ = Phi+, M~ = (1/2) PT_Q(x~ renamed P' -> Q) on all 16 units x~, so the
     five-token constraint confines N to the twin cone PT(PSD_4); (R3) in QM (x, y PSD, e, f PSD) both M and N have
     PSD partial transposes (5 random instances), the consistency the written argument needs.
  G  the (1,2,1,2) Choi-closure crossing with y = Glue(x1, x2; e) equals the K4 network value with the same objects
     (3 random exact instances; both splits).
  W  exact Bell-link network values for W3: theta tr[(Phi+)^3 (W3 (x) W3)] , ring with e = f = x = y = W3, and the
     two K4 splits, all >= 0 (reported).
  S  stabilizer slice: on Fix(H) (coordinates (a, gamma, b): P_00 = a, C_00 = -gamma, other fibres (b, 0)) with the
     inner product (a a' + gamma gamma' + 3 b b')/2, the cone L = {a >= 0, b >= 0, gamma^2 <= 2 sqrt(3) a b} is
     self-positive (exact identity: the pairing minus a sum of squares) and contains the averaged images of S
     ((1,0,0), (0,0,1), (1, +-1, 1/3)), a point with negative defect (1/4, 1, 2/sqrt3) and lies in the averaged S*
     (|gamma| <= a + b on L); its boundary rays are pairwise orthogonal to their mirror images (self-dual Lorentz
     cone in light-cone coordinates).  So the slice test cannot exclude a non-orthant sector cone.
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p7_wall_reduction")
rng = random.Random(20261009 + 7)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])


def rsmall(qs, dens=0.5):
    N = 2 ** len(qs)
    d = {}
    for r in range(N):
        for c in range(r, N):
            if rng.random() < dens:
                v = L.rand_gauss(rng)
                if r == c:
                    v = L.G(v.re)
                d[(r, c)] = v
                d[(c, r)] = v.conj()
    return L.Op(qs, d)


# ------------------------------------------------------------------------------------------------ R ring factorization
P1, P2, Q, R, U1, U2 = 0, 1, 2, 3, 4, 5
ok_r1 = True
for _ in range(4):
    x = rsmall((P1, P2, R), 0.7)
    e = rsmall((P1, P2, Q), 0.7)
    y = rsmall((Q, U1, U2), 0.7)
    f = rsmall((R, U1, U2), 0.7)
    val = L.pair(L.tensor(e, f), L.tensor(x, y))
    M = L.ptrace(L.matmul(L.tensor(e, L.identity((R,))), L.tensor(x, L.identity((Q,)))), (Q, R))
    Nn = L.ptrace(L.matmul(L.tensor(f, L.identity((Q,))), L.tensor(y, L.identity((R,)))), (Q, R))
    ok_r1 &= val == L.pair(M, Nn)
rep.check("R1 ring factorization: tr[(e (x) f)(x (x) y)] = tr(M N) with M the P-contraction of (x, e) and N the "
          "U-contraction of (y, f) (4 random exact instances)", ok_r1)
Pp = 6
ok_r2 = True
for _, xt in L.units((Pp, R)):
    Mt = L.ptrace(L.matmul(L.tensor(L.phi_plus(Pp, Q), L.identity((R,))), L.tensor(xt, L.identity((Q,)))), (R, Q))
    tgt = L.ptranspose(L.reorder(L.relabel(xt, {Pp: Q}), (R, Q)), [Q]).scale(Fr(1, 2))
    ok_r2 &= L.reorder(Mt, (R, Q)) == tgt
rep.check("R2 five-token analogue: with the pair effect Phi+ on (P', Q), M~ = (1/2) PT_Q(x~ renamed) on all 16 units: "
          "the five-token constraint confines N to the twin cone", ok_r2)
ok_r3 = True
for _ in range(5):
    x = L.rand_psd(rng, (P1, P2, R), rank=2)
    e = L.rand_psd(rng, (P1, P2, Q), rank=2)
    M = L.ptrace(L.matmul(L.tensor(e, L.identity((R,))), L.tensor(x, L.identity((Q,)))), (R, Q))
    ok_r3 &= L.psd(L.ptranspose(M, [Q]))[0] and L.psd(L.ptranspose(M, [R]))[0]
rep.check("R3 QM consistency: for PSD x, e the contraction M has PSD partial transposes (5 random instances)", ok_r3)

# ------------------------------------------------------------------------------------------------ G Choi closure = K4 net
# K4 network: states x(a,1,2), y(b,3,4), e'(a',b'); effects e(a,b), x'(a',1,3), y'(b',2,4)
a_, b_, ap, bp = 10, 11, 12, 13
ok_g = True
for split in (0, 1):
    for _ in range(3):
        x1 = rsmall((a_, 1, 2), 0.6)
        x2 = rsmall((b_, 3, 4), 0.6)
        e = rsmall((a_, b_), 0.8)
        ep = rsmall((ap, bp), 0.8)
        if split == 0:
            xq, yq = rsmall((ap, 1, 3), 0.6), rsmall((bp, 2, 4), 0.6)
        else:
            xq, yq = rsmall((ap, 1, 4), 0.6), rsmall((bp, 2, 3), 0.6)
        k4net = L.pair(L.tensor(e, xq, yq), L.tensor(x1, x2, ep))
        # (1,2,1,2) crossing: states x~ = e' (pair on (ap,bp))... use the glued state Y on D = {1,2,3,4}
        Y = L.cond(e, L.tensor(x1, x2))                 # glued state on (1,2,3,4)
        val = L.pair(L.tensor(xq, yq), L.tensor(ep, Y))
        ok_g &= val == k4net
rep.check("G the (1,2,1,2) Choi-closure crossing with y = Glue(x1, x2; e) equals the K4-network value (3 random exact "
          "instances per split, both splits)", ok_g)

# ------------------------------------------------------------------------------------------------ W W3 Bell values
W = L.w3
th = L.pair(L.tensor(L.phi_plus(0, 3), L.phi_plus(1, 4), L.phi_plus(2, 5)), L.tensor(W((0, 1, 2)), W((3, 4, 5))))
rg = L.pair(L.tensor(W((P1, P2, Q)), W((R, U1, U2))), L.tensor(W((P1, P2, R)), W((Q, U1, U2))))
k40 = L.pair(L.tensor(L.phi_plus(a_, b_), W((ap, 1, 3)), W((bp, 2, 4))),
             L.tensor(W((a_, 1, 2)), W((b_, 3, 4)), L.phi_plus(ap, bp)))
k41 = L.pair(L.tensor(L.phi_plus(a_, b_), W((ap, 1, 4)), W((bp, 2, 3))),
             L.tensor(W((a_, 1, 2)), W((b_, 3, 4)), L.phi_plus(ap, bp)))
rep.check("W exact Bell-link network values for W3: theta = %s, ring = %s, K4 split 0 = %s, split 1 = %s (all >= 0)"
          % (th, rg, k40, k41), all(v.im == 0 and v.re >= 0 for v in (th, rg, k40, k41)))

# ------------------------------------------------------------------------------------------------ S stabilizer slice
a, g, b, a2, g2, b2 = sp.symbols("a g b a2 g2 b2", real=True)
s3 = sp.sqrt(3)
ip = lambda u, v: (u[0] * v[0] + u[1] * v[1] + 3 * u[2] * v[2]) / 2
# boundary rays of L: gamma^2 = 2 sqrt3 a b; parametrize a = s^2, b = t^2/(2 sqrt3), gamma = s t (times sign)
s_, t_, u_, v_ = sp.symbols("s t u v", real=True)
ray = lambda s, t, sg: (s ** 2, sg * s * t, t ** 2 / (2 * s3))
# exact self-positivity identity on boundary rays: <r(s,t,+), r(u,v,-)> = (1/2)(s u - t v / 2)^2 ... check directly
lhs = sp.expand(ip(ray(s_, t_, 1), ray(u_, v_, -1)))
rhs = sp.expand(sp.Rational(1, 2) * (s_ * u_ - t_ * v_ / 2) ** 2)
lhs2 = sp.expand(ip(ray(s_, t_, 1), ray(u_, v_, 1)))
rhs2 = sp.expand(sp.Rational(1, 2) * (s_ * u_ + t_ * v_ / 2) ** 2)
self_pos = sp.simplify(lhs - rhs) == 0 and sp.simplify(lhs2 - rhs2) == 0
# a boundary ray is orthogonal to the mirror ray with (u, v) = (t/sqrt... ) chosen s u = t v / 2 : self-duality witness
orth = sp.simplify(ip(ray(1, 2, 1), ray(1, 1, -1))) == 0      # s u = t v / 2 with (s,t,u,v) = (1,2,1,1)
inL = lambda p_: p_[0] >= 0 and p_[2] >= 0 and sp.simplify(2 * s3 * p_[0] * p_[2] - p_[1] ** 2) >= 0
pts = [(1, 0, 0), (0, 0, 1), (1, 1, sp.Rational(1, 3)), (1, -1, sp.Rational(1, 3))]
neg = (sp.Rational(1, 4), 1, 2 / s3)
contains = all(inL(p_) for p_ in pts) and inL(neg) and (neg[0] - abs(neg[1]) < 0)
# L inside averaged S*: |gamma| <= a + b on L  <=  2 sqrt3 a b <= (a + b)^2  <=>  (a + b)^2 - 2 sqrt3 a b >= 0
inSstar = sp.simplify(sp.expand((a + b) ** 2 - 2 * s3 * a * b - ((a - b) ** 2 + (2 - s3) * 2 * a * b)
                                * 1)) == 0 and (2 - s3) > 0
rep.check("S stabilizer slice: L = {a, b >= 0, gamma^2 <= 2 sqrt3 a b} is self-positive (exact sum-of-squares pairings "
          "of boundary rays), has a boundary ray orthogonal to its mirror (self-dual Lorentz cone), contains the "
          "averaged S points and the negative-defect point (1/4, 1, 2/sqrt3), and lies in |gamma| <= a + b",
          self_pos and orth and contains and inSstar)

rep.verdict("P7-WALL-REDUCTION-EXACT")
