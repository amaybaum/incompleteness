# EXPLORATION (floating point): positivity of composites of J/K gates on product states (block coordinate descent)
import numpy as np
from blib import *
J5m = {1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}
K5m = {2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}
G5 = jk_gate(5, [1, 1, -1, -1, -1, -1], J5m, K5m)
G3 = sp_from_dense(complex_cnot_d3())
def dense(A, dim):
    M = np.zeros((dim, dim))
    for j, col in A.items():
        for i, x in col.items(): M[i, j] = float(x)
    return M
def minval(W, n, k, starts=60, iters=150, seed=0):
    rng = np.random.default_rng(seed)
    T = W.reshape([n]*(2*k))  # out indices then in indices
    best = (9, None)
    for _ in range(starts):
        v = [np.r_[1, x/np.linalg.norm(x)] for x in rng.normal(size=(2*k, n-1))]  # effects 0..k-1, states k..2k-1
        for it in range(iters):
            for b in range(2*k):
                t = T
                # contract all but b
                ops = []
                letters = 'abcdefghij'[:2*k]
                expr = letters + ',' + ','.join(letters[i] for i in range(2*k) if i != b) + '->' + letters[b]
                c = np.einsum(expr, T, *[v[i] for i in range(2*k) if i != b])
                w = c[1:]; nn = np.linalg.norm(w)
                if nn > 1e-14: v[b] = np.r_[1, -w/nn]
        letters = 'abcdefghij'[:2*k]
        val = np.einsum(letters + ',' + ','.join(letters) + '->', T, *v)
        if val < best[0]: best = (val, [x.copy() for x in v])
    return best
for name, G, n in (('q3', G3, 4), ('jk5', G5, 6)):
    sp2 = Space(n, 2)
    S = {j: {sp2.idx(sp2.digits(j)[::-1]): Fr(1)} for j in range(sp2.dim)}
    GBA = sp_compose(S, sp_compose(G, S))
    W = dense(sp_compose(GBA, G), n*n)
    print(name, 'two copies G_BA G_AB: min', minval(W, n, 2)[0])
    sp = Space(n, 3)
    g = {(X, Y): embed_two(G, n, (X, Y), sp) for X in range(3) for Y in range(3) if X != Y}
    for lab, A in (('G_BC G_AB (chain)', sp_compose(g[1,2], g[0,1])), ('G_AC G_AB (out-star)', sp_compose(g[0,2], g[0,1])),
                   ('G_BC G_AC (in-star)', sp_compose(g[1,2], g[0,2]))):
        print(name, lab, 'min', minval(dense(A, sp.dim), n, 3, starts=30, iters=80)[0])
np.set_printoptions(precision=3, suppress=True)
G, n = G5, 6
sp2 = Space(n, 2)
S = {j: {sp2.idx(sp2.digits(j)[::-1]): Fr(1)} for j in range(sp2.dim)}
GBA = sp_compose(S, sp_compose(G, S))
W = dense(sp_compose(GBA, G), n*n)
for seed in range(4):
    val, v = minval(W, n, 2, starts=20, seed=seed)
    print(val, 'effects', v[0], v[1], 'states', v[2], v[3])
