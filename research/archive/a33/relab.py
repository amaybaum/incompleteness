"""NF (sigma, lambda, eps) of every shape-0 relabelling (pi, tau) on the nine circles, from the exact
coordinate tables: relabel_{pi,tau}(G)[i][j][k] = G[pi i][tau j][tau k], so the coordinate at
((i1,i2,i3),(j1,j2,j3)) of relabel(pt r z) is the coordinate of pt r z at ((pi i1, pi i2, pi i3),(tau j1,...))."""
import itertools, pickle
from circles import C, IDX, R, N
S4 = list(itertools.permutations(range(4)))
pos = {p: k for k, p in enumerate(IDX)}
def relabelled(r, pi, tau):
    return [C[r][pos[((pi[i1], pi[i2], pi[i3]), (tau[j1], tau[j2], tau[j3]))]] for (i1, i2, i3), (j1, j2, j3) in IDX]
def variants(s):  # (lambda, eps): pt s (lambda * z^eps): eps=True -> z, False -> conj z (exponent negated)
    out = {}
    for lam in (1, -1):
        for eps in (True, False):
            out[(lam, eps)] = [(sg * (lam ** e), e if eps else -e) for (sg, e) in C[s]]
    return out
V = [variants(s) for s in range(N)]
def nf(pi, tau):
    res = []
    for r in range(N):
        img = relabelled(r, pi, tau)
        hits = [(s, lam, eps) for s in range(N) for (lam, eps), v in V[s].items() if v == img]
        assert len(hits) >= 1, (r, pi, tau)
        # the constant coordinates (e = 0) do not see eps; prefer a unique hit up to that ambiguity
        hits2 = set((s, lam) for s, lam, eps in hits)
        assert len(hits2) == 1, (r, pi, tau, hits)
        s, lam = hits2.pop()
        epss = set(eps for _, _, eps in hits)
        res.append((s, lam, epss))
    return res
v1 = [0, 2, 4, 2, 0, 3, 4, 5, 0]; v2 = [1, 3, 5, 5, 4, 1, 3, 1, 2]
def vertex_perm(res):
    nu = [None] * 6
    for r, (s, lam, _) in enumerate(res):
        a, b = (v1[s], v2[s]) if lam == 1 else (v2[s], v1[s])
        for v, w in ((v1[r], a), (v2[r], b)):
            assert nu[v] in (None, w); nu[v] = w
    assert sorted(nu) == list(range(6))
    return tuple(nu)
table = {}
for pi in S4:
    for tau in S4:
        res = nf(pi, tau); table[(pi, tau)] = (res, vertex_perm(res))
nus = set(v for _, v in table.values())
print('distinct vertex permutations from shape-0 relabellings:', len(nus))
amb = sum(1 for (res, _) in table.values() for (_, _, e) in res if len(e) == 2)
print('eps-ambiguous circle images (all coordinates constant?):', amb)
pickle.dump(table, open('relab.pkl', 'wb'))
# R r themselves
for r in range(N):
    print('R', r, table[R[r]][0], table[R[r]][1])
