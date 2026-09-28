"""Test of K10: predict the relaxed union of the Dita loci from (i) index-permutation sign flips and (ii) identical membership of
the transported remaining atoms in one of SIG's twenty structures; compare with the computed (s5) unions.
usage: t_k10.py <loci pickle> [orbit ...]"""
import pickle, sys, itertools, time
from t_k8 import SIG_STRUCTS, S0, identically_Dita, faces_of
from align import *
from splitters import cells_to_mat
t0 = time.time()
L = pickle.load(open(os.path.join(HERE, sys.argv[1]), 'rb'))
which = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else sorted(L)
ROWS0 = {tuple(S0[i]): i for i in range(16)}
COLS0 = {tuple(S0[i][j] for i in range(16)): j for j in range(16)}
def flip_perm_multi(pieces, signs):
    _, base = rebase(pieces, signs)
    pi = [ROWS0.get(tuple(base[i])) for i in range(16)]
    if None not in pi and sorted(pi) == list(range(16)): return ('row', pi)
    pj = [COLS0.get(tuple(base[i][j] for i in range(16))) for j in range(16)]
    if None not in pj and sorted(pj) == list(range(16)): return ('col', pj)
    return None
def dephase_rows(T): return [tuple(vsub(T[i][j], T[i][0]) for j in range(16)) for i in range(16)]
def dephase_cols(T): return [tuple(vsub(T[i][j], T[0][j]) for i in range(16)) for j in range(16)]
DR0 = {r: i for i, r in enumerate(dephase_rows(S0))}; DC0 = {c: j for j, c in enumerate(dephase_cols(S0))}
def flip_monomial(pieces, signs):
    """SIG o flip = (row phases) x (row permutation of SIG), or the same on columns"""
    _, base = rebase(pieces, signs)
    pi = [DR0.get(r) for r in dephase_rows(base)]
    if None not in pi and sorted(pi) == list(range(16)): return ('row', pi)
    pj = [DC0.get(c) for c in dephase_cols(base)]
    if None not in pj and sorted(pj) == list(range(16)): return ('col', pj)
    return None
def transport(P, fp):
    kind, pi = fp; Q = [[0] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if kind == 'row': Q[pi[i]][j] = P[i][j]
            else: Q[i][pi[j]] = P[i][j]
    return Q
def predict(Ms, relaxed=False):
    d = len(Ms); pred = []
    for size in range(0, d + 1):
        for S in itertools.combinations(range(d), size):
            for sv in itertools.product((1, -1), repeat=size):
                rows = [((tuple(1 if t == k else 0 for t in range(d))), (0, 0, 0) if s == 1 else (2, 0, 0)) for k, s in zip(S, sv)]
                F = FlatD(d, rows)
                if any(P_.contains(F) for P_ in pred): continue   # already implied by a larger predicted subtorus
                signs = [None] * d
                for k, s in zip(S, sv): signs[k] = s
                fp = (flip_monomial if relaxed else flip_perm_multi)(Ms, [s if s is not None else 1 for s in signs])
                if fp is None: continue
                rem = [Ms[j] for j in range(d) if j not in S]
                if not rem or identically_Dita([transport(M, fp) for M in rem], relaxed=relaxed) is not None:
                    pred.append(F)
    return minimal_union(pred)
n = okS = okR = 0
for t in which:
    r = L[t]; Ms = [cells_to_mat(a) for a in r['atoms']]; d = len(Ms)
    PS = sorted(F.B for F in predict(Ms, False)); PR = sorted(F.B for F in predict(Ms, True))
    gs, gr = sorted(r['U_strict']) == PS, sorted(r['U_relaxed']) == PR
    n += 1; okS += gs; okR += gr
    print("orbit %2d d=%d K10'-strict %s K10'-relaxed %s | computed strict %s relaxed %s%s  %.0fs" % (t, d, gs, gr, r['show_strict'], r['show_relaxed'],
          '' if gs and gr else '  PREDICTED strict %s relaxed %s' % (sorted(FlatD.of(d, B).show() for B in PS), sorted(FlatD.of(d, B).show() for B in PR)), time.time() - t0), flush=True)
print("K10' holds: strict %d of %d, relaxed %d of %d" % (okS, n, okR, n))
