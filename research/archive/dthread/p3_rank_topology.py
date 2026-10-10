"""P3 — the bridge steps: injective reading on a convex body => finite rank; the topology of the projection;
probability-closedness vs norm-closedness; boundedness of the joint-state slice.

Usage: python3 -I p3_rank_topology.py <seed>

Decision rule (fixed before the first run): verdict BRIDGE-STEPS-EXACT iff all checks pass:
  3.1 LEMMA (constructive direction).  For K = conv{b_1..b_m} in Q^n and a linear reading R : Q^n -> Q^k:
      whenever ker R meets the direction space of aff K, an explicit pair p != q in K with Rp = Rq is
      built from the decomposition of a kernel direction (exact, 40 random instances).  Hence
      "R injective on K" forces "R injective on dir aff K", so dim aff K <= rank R.        [X]+[W]
  3.2 countercontrol: for a NON-convex finite set the lemma fails (injective on the set, not on the span).
  3.3 the c0 countermodel for the norm topology: f_N = sum_{n<=N} 2^-n x_n has max 1 - 2^-N on the cube,
      the value 1 forces x = all-ones, whose sup-distance to every finitely supported vector is >= 1;
      the truncations 1_{[1,N]} converge to all-ones pointwise, not in sup norm.   [X] on truncations; [W]
  3.4 probability topology without local tomography (padding control): two points of the padded body
      agree on every product-effect value and differ; so a probability-closed set containing one contains
      the other, and the norm-closed padded body is not probability-closed.            [X]
  3.5 boundedness: for omega with omega_00 = 1 and all products of the effects (1 +- e_i)/2, (1 +- e_j)/2
      nonnegative, |omega_mu nu| <= 1 (exact identities); countercontrol: the padded maximal body is
      unbounded in the height coordinate.                                                [X]
Otherwise BRIDGE-STEP-FAILED.
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402
from dlib import Checks, prod_W, pairval  # noqa: E402

seed = int(sys.argv[1])
rng = random.Random(seed)
C = Checks('P3 bridge steps')


def rnd(lo=-5, hi=5):
    return sp.Rational(rng.randint(lo, hi), rng.randint(1, 4))


# 3.1 constructive lemma
ok_all = True
made = 0
tries = 0
while made < 40 and tries < 400:
    tries += 1
    n = rng.randint(3, 6)
    m = rng.randint(2, n + 2)
    k = rng.randint(1, n - 1)
    B = [sp.Matrix([rnd() for _ in range(n)]) for _ in range(m)]
    R = sp.Matrix(k, n, lambda i, j: rnd())
    Dir = sp.Matrix.hstack(*[B[i] - B[0] for i in range(1, m)])
    # kernel of R restricted to dir: solve R*Dir*c = 0
    ns = (R * Dir).nullspace()
    if not ns or (Dir * ns[0]).is_zero_matrix:
        continue
    cvec = ns[0]
    v = Dir * cvec
    # v = sum_i c_i (b_i - b_0) = sum_j w_j b_j with sum w_j = 0
    w = [-sum(cvec)] + list(cvec)
    pos = [max(x, 0) for x in w]
    neg = [max(-x, 0) for x in w]
    s = sum(pos)
    assert s == sum(neg) and s > 0
    p = sum((pos[j] / s * B[j] for j in range(m)), sp.zeros(n, 1))
    q = sum((neg[j] / s * B[j] for j in range(m)), sp.zeros(n, 1))
    good = (p != q) and (R * p == R * q) and all(x >= 0 for x in pos + neg) and \
        sum(pos) / s == 1 and sum(neg) / s == 1 and (p - q) == v / s
    ok_all &= good
    made += 1
C.check('3.1 kernel direction in dir aff K => explicit collision p != q in K', ok_all and made == 40,
        '%d instances (%d draws)' % (made, tries))
C.note('[W] general form: v = sum a_j (b_j - b_j\'), a_j >= 0 after swapping; v = A(p - q) with p, q convex')
C.note('    combinations; R v = 0 and R injective on K give p = q, v = 0.  So injective on K <=> on dir aff K.')

# 3.2 non-convex countercontrol
pts = [sp.Matrix([0, 0]), sp.Matrix([1, 0]), sp.Matrix([0, 1])]
Rr = sp.Matrix([[1, 2]])
vals = [(Rr * x)[0] for x in pts]
pc, qc = sp.Matrix([0, sp.Rational(1, 2)]), sp.Matrix([1, 0])
C.check('3.2 finite set {0,e1,e2}: R=(1,2) injective on it (values %s) but not on its hull' % vals,
        len(set(vals)) == 3 and Rr * pc == Rr * qc and pc != qc)

# 3.3 c0 countermodel, truncations
okc = True
for N in range(1, 25):
    w = [Fr(1, 2 ** n) for n in range(1, N + 1)]
    mx = sum(w)  # attained at all-ones on the N-cube
    okc &= (mx == 1 - Fr(1, 2 ** N))
    # any other vertex is strictly smaller
    okc &= all(mx - 2 * w[i] < mx for i in range(N))
C.check('3.3a max of f_N on [-1,1]^N is 1 - 2^-N (N=1..24), attained only at all-ones', okc)
C.note('3.3b [W] sup over the c0 ball is 1, never attained: value 1 needs sum 2^-n (1 - x_n) = 0, i.e. x = all-ones')
okd = True
for N in range(1, 12):
    for supp in range(0, N):
        # any vector supported in [1, supp] with entries in [-1,1]: coordinate supp+1 is 0, all-ones has 1 there
        okd &= abs(Fr(1) - Fr(0)) >= 1
C.note('3.3c [tautological, not counted] sup-distance(all-ones, vector supported in [1,s]) >= 1 at coordinate s+1: %s' % okd)
# pointwise convergence of truncations
okp = all(all((1 if n <= N else 0) == 1 for n in range(1, k + 1)) for k in range(1, 8) for N in range(k, k + 5))
C.note('3.3d [tautological, not counted] 1_[1,N] -> all-ones coordinatewise, sup-distance stays 1: %s' % okp)
C.note('[W] realisation: preparations = rescaled graph points ((1+f(x))/2, ((1+x_n)/2)_n) for finitely supported')
C.note('    rational x in the cube; labels = the coordinates + a unit; stage N = first N of each; SC-inf holds')
C.note('    trivially; CMP-1 body = norm closure = rescaled graph of the c0 ball (closed, convex, bounded); the')
C.note('    reading through the single label f has image the open interval (0,1): not closed.  FiniteRank fails.')
C.note('    Pointwise (Tychonoff) closure would add the all-ones point and make every finite reading compact.')

# 3.4 padding control
x1, x2, x3, y1, y2, y3, h = sp.symbols('x1:4 y1:4 h')
om0 = prod_W([0, 0, 0], [0, 0, 0])
# padEff e f (v, h) = prodEff e f v  (CompositeInterface.lean:841-844): evaluate on literal first component
eff_vecs = [sp.Matrix([sp.Rational(1, 2)] + [sp.Rational(sg, 2) if k == i else 0 for k in range(3)])
            for i in range(3) for sg in (1, -1)] + [sp.Matrix([1, 0, 0, 0])]
padEff = lambda a, b, pt: pairval(a, b, pt[0])  # noqa: E731  literal: read the first component only
pA, pB = (om0, 0), (om0, 1)
same = all(padEff(a, b, pA) == padEff(a, b, pB) for a in eff_vecs for b in eff_vecs)
C.check('3.4 padded points (om0,0), (om0,1): all %d sampled product-effect values equal, points differ'
        % len(eff_vecs) ** 2, same and pA != pB, 'definitional instance of padEff_apply :843; [K] :885')
C.note('[W] so in the initial topology of the product-effect values the padded body P.Om x [0,1] (norm-closed when')
C.note('    P.Om is) is not closed: its probability-closure is P.Om x R.  Norm-closed and probability-closed differ')
C.note('    exactly where local tomography fails.')

# 3.5 boundedness of the normalized slice
W = sp.Matrix(4, 4, lambda m, v: sp.Symbol('w%d%d' % (m, v)))
ok5 = True
for i in range(1, 4):
    for j in range(1, 4):
        for s in (1, -1):
            for t in (1, -1):
                a = sp.zeros(4, 1); a[0] = sp.Rational(1, 2); a[i] = sp.Rational(s, 2)
                b = sp.zeros(4, 1); b[0] = sp.Rational(1, 2); b[j] = sp.Rational(t, 2)
                val = pairval(a, b, W)
                ok5 &= sp.expand(4 * val - (W[0, 0] + s * W[i, 0] + t * W[0, j] + s * t * W[i, j])) == 0
# from the four sign choices: sum over (s,t) of s*t*val = W[i,j], sum of all = W[0,0]
for i in range(1, 4):
    for j in range(1, 4):
        tot = 0
        st = 0
        for s in (1, -1):
            for t in (1, -1):
                a = sp.zeros(4, 1); a[0] = sp.Rational(1, 2); a[i] = sp.Rational(s, 2)
                b = sp.zeros(4, 1); b[0] = sp.Rational(1, 2); b[j] = sp.Rational(t, 2)
                val = pairval(a, b, W)
                tot += val
                st += s * t * val
        ok5 &= sp.expand(tot - W[0, 0]) == 0 and sp.expand(st - W[i, j]) == 0
C.check('3.5a four sign-choice product values sum to omega_00 and their signed sum is omega_ij', ok5)
C.note('[W] nonnegative values summing to omega_00 = 1 give |omega_ij| <= 1; likewise |omega_i0|, |omega_0j| <= 1.')
C.note('    So the joint-state slice of two balls is bounded; closed cone <=> closed slice (base compact, 0 not in it).')
hbig = sp.Integer(10) ** 6
memb = all(padEff(a, b, (om0, hbig)) >= 0 for a in eff_vecs[:-1] for b in eff_vecs[:-1]) and \
    padEff(eff_vecs[-1], eff_vecs[-1], (om0, hbig)) == 1
C.check('3.5b countercontrol: (om0, 10^6) passes every sampled clause of the padded maximal body', memb,
        'definitional (height unread); [W] so the padded maximal body is unbounded')
C.summary('BRIDGE-STEPS-EXACT', 'BRIDGE-STEP-FAILED')
