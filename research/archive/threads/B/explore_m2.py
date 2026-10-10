# EXPLORATION ONLY (floating point) -- recorded for provenance; no claim rests on these numbers.
# exploration: Model II (per-type role NOTs) three-copy relations with the J/K gate, and the quantum control
from blib import *
J5m = {1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}
K5m = {2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}
G5 = jk_gate(5, [1, 1, -1, -1, -1, -1], J5m, K5m)
G3 = sp_from_dense(complex_cnot_d3())
for name, G, n in (('q3', G3, 4), ('jk5', G5, 6)):
    sp = Space(n, 3)
    g = {(X, Y): embed_two(G, n, (X, Y), sp) for X in range(3) for Y in range(3) if X != Y}
    c = sp_compose
    I = sp_identity(sp.dim)
    T1 = sp_eq(c(g[0,1], g[0,2]), c(g[0,2], g[0,1]), sp.dim)
    T2 = sp_eq(c(g[0,2], g[1,2]), c(g[1,2], g[0,2]), sp.dim)
    T3 = sp_eq(c(g[1,2], c(g[0,1], c(g[1,2], g[0,1]))), g[0,2], sp.dim)
    sw = c(g[0,1], c(g[1,0], g[0,1]))
    # SWAP of factors 0,1
    S = {}
    for j in range(sp.dim):
        dg = sp.digits(j); S[j] = {sp.idx([dg[1], dg[0], dg[2]]): Fr(1)}
    print(name, 'T1', T1, 'T2', T2, 'T3', T3, 'G_AB G_BA G_AB = SWAP', sp_eq(sw, S, sp.dim))
names = ['u','x','y','w1','w2','z']
n=6; sp=Space(n,3); G=G5
g = {(X, Y): embed_two(G, n, (X, Y), sp) for X in range(3) for Y in range(3) if X != Y}
c=sp_compose
L = c(g[1,2], c(g[0,1], c(g[1,2], g[0,1])))
bad=[]
for j in range(sp.dim):
    a={i:x for i,x in L[j].items() if x}; b={i:x for i,x in g[0,2][j].items() if x}
    if a!=b: bad.append(j)
print(len(bad),'bad columns of',sp.dim)
from collections import Counter
print(Counter(tuple(names[t] for t in sp.digits(j)) for j in bad).most_common(10))
for j in bad[:6]:
    print([names[t] for t in sp.digits(j)], '->', {tuple(names[t] for t in sp.digits(i)):str(x) for i,x in L[j].items()}, ' want', {tuple(names[t] for t in sp.digits(i)):str(x) for i,x in g[0,2][j].items()})
