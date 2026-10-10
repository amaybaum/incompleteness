import sys, time; sys.path.insert(0, 'a38')
from lib38b import *
# relaxed census at SIG: proportionality candidates (both forms) that satisfy the relaxed rank-one condition on SIG's entries
def relaxed_ok(H, mn, cp, rows):
    m, n = mn
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    mu = {(a, b, c): H[row[(a, b)]][col[(c, 0)]] * H[row[(0, b)]][col[(c, 0)]].conj() for a in range(m) for b in range(n) for c in range(m)}
    # mu(a,b,c)/mu(a,0,c) independent of c  <=>  mu(a,b,c) conj mu(a,0,c) == mu(a,b,0) conj mu(a,0,0) (unimodular, scaled)
    return all(mu[(a, b, c)] * mu[(a, 0, c)].conj() == mu[(a, b, 0)] * mu[(a, 0, 0)].conj() for a in range(m) for b in range(n) for c in range(m))
tot = 0
for mn in SHAPES:
    res = dita_orientations(SIG, *mn)
    strict = sum(1 for cp, rows, ok, X, Y in res if ok)
    rel = sum(1 for cp, rows, ok, X, Y in res if relaxed_ok(SIG, mn, cp, rows))
    print('shape', mn, 'candidates', len(res), 'strict exact', strict, 'relaxed exact', rel)
    tot += rel
print('relaxed census column form total:', tot, '(row form identical by symmetry)')
# the second direction of L(Pi_W)
B = straight_lattice(W_matrix())
for v in B:
    M = [v[i*16:(i+1)*16] for i in range(16)]
    print('basis vector values', sorted(set(v)), 'nonzero', sum(1 for x in v if x))
    for r in M: print('  ', ' '.join('%2d' % x for x in r))
