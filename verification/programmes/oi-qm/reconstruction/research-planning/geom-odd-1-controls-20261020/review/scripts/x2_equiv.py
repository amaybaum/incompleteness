"""Is the SLP candidate a local relabelling of R?  And how many sign-twisted gates R o diag(s) exist?  Exact integer arithmetic."""
import sys, json, itertools
from fractions import Fraction as Fr
from math import lcm
import numpy as np
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
body = cv.Body('eball3'); n = 4; nn = 16
R = np.array([[int(c) for c in r] for r in body.reference], dtype=np.int64)
Gc = json.load(open(sys.argv[2]))['G']
G = np.array([[int(Fr(c)) for c in r] for r in Gc], dtype=np.int64)
assert all(Fr(c).denominator == 1 for r in Gc for c in r)
D = R @ G   # R^-1 = R
print('R^-1 G diagonal:', np.count_nonzero(D - np.diag(np.diag(D))) == 0, 'signs', np.diag(D).reshape(4, 4).tolist())
# local signed permutations of R^3, as 4x4 on hom coordinates (1, x)
locs = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((4, 4), dtype=np.int64); M[0, 0] = 1
        for i in range(3): M[1 + i, 1 + p[i]] = s[i]
        locs.append(M)
print('local signed permutations per factor:', len(locs))
def is_local_product(X):
    """X == C (x) D with C, D in locs?"""
    for C in locs:
        # X[(m,n),(m',n')] = C[m,m'] D[n,n']; with C[0,0]=1: D = X block (0,0)
        Dm = X[0:4, 0:4]
        if not np.array_equal(np.kron(C, Dm), X): continue
        if any(np.array_equal(Dm, L) for L in locs): return C, Dm
    return None
hits = []
for A in locs:
    for B in locs:
        AB = np.kron(A, B); ABinv = AB.T          # signed permutation: inverse = transpose
        X = R @ ABinv @ G                         # want X == C (x) D  with  G = (A(x)B) R (C(x)D)
        r = is_local_product(X)
        if r is not None: hits.append((A, B) + r)
print('decompositions G = (A(x)B) R (C(x)D) with local signed permutations:', len(hits))
if hits:
    A, B, C, Dm = hits[0]
    assert np.array_equal(np.kron(A, B) @ R @ np.kron(C, Dm), G)
    print(' first: A =', A[1:, 1:].tolist(), 'B =', B[1:, 1:].tolist(), 'C =', C[1:, 1:].tolist(), 'D =', Dm[1:, 1:].tolist())
    # conjugation form?
    conj = [h for h in hits if np.array_equal(np.kron(h[0], h[1]) @ np.kron(h[2], h[3]), np.eye(16, dtype=np.int64))]
    print(' of which pure conjugations (C(x)D = (A(x)B)^-1):', len(conj))
    if conj:
        A, B, C, Dm = conj[0]; print('  conj by A =', A[1:, 1:].tolist(), 'B =', B[1:, 1:].tolist())
    # do the local maps preserve the body data (z3 corner, N = nflip)?
    z = np.array([1, 0, 0, 1]); Nh = np.diag([1] + body.nflip)
    def keeps(L): return (np.array_equal(L @ z, z) or np.array_equal(L @ z, np.array([1, 0, 0, -1]))) , np.array_equal(L @ Nh, Nh @ L)
    print(' local maps of first hit: z-line kept / commute with N:', [keeps(L) for L in hits[0]])
# all sign twists R o diag(s) that pass the verifier exactly (pools A and B)
def scal(v):
    L = 1
    for c in v: L = lcm(L, Fr(c).denominator)
    return [int(Fr(c) * L) for c in v]
st = [s for p in 'AB' for s in body.pools[p]['states']]; ef = [e for p in 'AB' for e in body.pools[p]['effects']]
S = np.array([scal(cv.hom(x)) for x in st], dtype=np.int64); E = np.array([scal(e) for e in ef], dtype=np.int64)
def minval(M):
    W = np.einsum('mnkl,xk,yl->xymn', M.reshape(4, 4, 4, 4), S, S)
    return np.einsum('am,xymn,bn->xyab', E, W, E).min()
T = np.kron(np.eye(4, dtype=np.int64), np.array([[int(c) for c in r] for r in body.H]))
Cm = np.kron(np.array([[int(c) for c in r] for r in body.H]), np.eye(4, dtype=np.int64))
z = [1, 0, 0, 1]; zm = [1, 0, 0, -1]; cor = {0: z, 1: zm}
def inF(M):
    if not np.array_equal(T @ M @ T, M) or not np.array_equal(Cm @ M @ Cm, T @ M): return False
    return all(np.array_equal(M @ np.kron(cor[a], cor[b]), np.kron(cor[a], cor[(a + b) % 2])) for a in (0, 1) for b in (0, 1))
gates = []
for bits in itertools.product((1, -1), repeat=16):
    M = R @ np.diag(bits)
    if not inF(M): continue
    Mi = np.diag(bits) @ R
    if minval(M) >= 0 and minval(Mi) >= 0: gates.append(bits)
print('sign twists R o diag(s) in F passing posFwd and posInv exactly on pools A u B:', len(gates))
cand_bits = tuple(int(v) for v in np.diag(D))
print(' candidate among them:', cand_bits in gates)
nloc = 0
for bits in gates:
    M = R @ np.diag(bits); found = False
    for A in locs:
        for B in locs:
            if is_local_product(R @ np.kron(A, B).T @ M) is not None: found = True; break
        if found: break
    nloc += found
print(' of these, local relabellings (A(x)B) R (C(x)D) of R:', nloc)
