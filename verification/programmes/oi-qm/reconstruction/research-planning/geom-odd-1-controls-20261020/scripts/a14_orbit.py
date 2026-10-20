"""A14 (correction pass, B1): independent exact check that the SLP candidate is a local relabelling of R, and the size
of R's local-relabelling class within F; Fraction arithmetic throughout (frozen verifier's helpers only).

Local group used: Gamma = {diag(1, a, b, c) : a, b, c = +-1} on hom coordinates (1, x) of eball 3.  Each element is an
orthogonal map of the ball, keeps the z3 line (z3 = e_3 -> +-e_3) and commutes with nflip = diag(1, -1, -1).
For L1 = A (x) B, L2 = C (x) D with A, B, C, D in Gamma:  (e (x) f)(L1 R L2 (x (x) y)) = (A^T e (x) B^T f)(R(Cx (x) Dy)),
and A^T, B^T map effects to effects and C, D map states to states, so whole-body posFwd of L1 R L2 follows from R's;
likewise posInv, since (L1 R L2)^-1 = L2^-1 R^-1 L1^-1 with local factors in Gamma.
Then: (i) the candidate equals (1 (x) diag(1,1,-1)) R (Zpi (x) -1_3); (ii) the class {L1 R L2} intersected with F;
(iii) all sign twists R o diag(s) in F, and exact posFwd/posInv on pools A u B for those outside the class."""
import itertools
import json
import sys
from fractions import Fraction as Fr

sys.path.insert(0, sys.argv[1])
import controls_verify as cv   # noqa: E402

body = cv.Body('eball3')
R = body.reference
G = cv.from_json_matrix(json.load(open(sys.argv[2]))['G'])
gam = {s: cv.diag([1] + list(s)) for s in itertools.product((1, -1), repeat=3)}
I4 = cv.eye(4)
# (i)
Bm = cv.diag([1, 1, 1, -1])            # diag(1, 1, -1) on the chart
Cm = cv.diag([1, -1, -1, 1])           # Zpi
Dm = cv.diag([1, -1, -1, -1])          # -1_3
dec = cv.mat_mul(cv.mat_mul(cv.kron(I4, Bm), R), cv.kron(Cm, Dm))
print('(i) candidate == (1 (x) diag(1,1,-1)) R (Zpi (x) -1_3):', dec == G)
nfl = cv.diag([1] + body.nflip)
z = [Fr(1), Fr(0), Fr(0), Fr(1)]
print('    every element of Gamma: orthogonal on the chart, keeps the z3 line, commutes with nflip:',
      all(cv.mat_mul(M, nfl) == cv.mat_mul(nfl, M) and cv.mat_vec(M, z)[3] in (1, -1) for M in gam.values()))


def inF(M):
    fr, rt, rc = cv.check_VL(body, M)
    return fr and rt and rc


key = lambda M: tuple(tuple(r) for r in M)
cls = {}
for a, b, c, d in itertools.product(gam, repeat=4):
    M = cv.mat_mul(cv.mat_mul(cv.kron(gam[a], gam[b]), R), cv.kron(gam[c], gam[d]))
    if inF(M):
        cls.setdefault(key(M), (a, b, c, d))
twist = lambda M: all(cv.mat_mul(R, M)[i][j] == 0 for i in range(16) for j in range(16) if i != j)
print('(ii) distinct members of the class {(A(x)B) R (C(x)D)} lying in F:', len(cls),
      '; of the form R o diag(s):', sum(1 for k in cls if twist([list(r) for r in k])),
      '; candidate in the class:', key(G) in cls, '; involutions in the class:',
      sum(1 for k in cls if cv.mat_mul([list(r) for r in k], [list(r) for r in k]) == cv.eye(16)))
# (iii) all sign twists in F
twF = []
for bits in itertools.product((1, -1), repeat=16):
    M = cv.mat_mul(R, cv.diag(bits))
    if inF(M):
        twF.append((bits, M))
inC = [t for t in twF if key(t[1]) in cls]
out = [t for t in twF if key(t[1]) not in cls]
print('(iii) sign twists R o diag(s) in F: %d; in the class: %d; outside: %d' % (len(twF), len(inC), len(out)), flush=True)
# exact integer evaluation (int64; positive rescalings of states and effects; |values| < 10^9, far from overflow)
import numpy as np
from math import lcm
def scal(v):
    L = 1
    for c in v:
        L = lcm(L, Fr(c).denominator)
    return [int(Fr(c) * L) for c in v]
Sx = np.array([scal(cv.hom(x)) for p in 'AB' for x in body.pools[p]['states']], dtype=np.int64)
Ex = np.array([scal(e) for p in 'AB' for e in body.pools[p]['effects']], dtype=np.int64)
print('    max |scaled state entry| %d, max |scaled effect entry| %d' % (np.abs(Sx).max(), np.abs(Ex).max()))
def mn(M):
    Mi = np.array([[int(v) for v in r] for r in M], dtype=np.int64).reshape(4, 4, 4, 4)
    Wv = np.einsum('mnkl,xk,yl->xymn', Mi, Sx, Sx)
    return int(np.einsum('am,xymn,bn->xyab', Ex, Wv, Ex).min())
ctrl = [(mn(M) >= 0 and mn(cv.inverse(M)) >= 0) for bits, M in inC]
print('    control: in-class twists passing exactly on A u B: %d of %d' % (sum(ctrl), len(inC)))
npass = sum(1 for bits, M in out if mn(M) >= 0 and mn(cv.inverse(M)) >= 0)
print('    outside-class twists passing posFwd and posInv exactly on A u B: %d of %d' % (npass, len(out)))
