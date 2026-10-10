"""Exploration: exact symbolic data for A32's execution proofs (unit parameters: conj z = 1/z)."""
import sympy as sp, itertools
z, w = sp.symbols('z w')
def M(t): return [[1,1,1,1],[1,t,-1,-t],[1,-1,1,-1],[1,-t,-1,t]]
def conj(e, t): return sp.simplify(e.subs(t, 1/t)) if e.has(t) else e
def F(t):
    m = M(t)
    return [[[sp.Rational(1,4)*conj(sp.sympify(m[i][j]), t)*m[i][k] for k in range(4)] for j in range(4)] for i in range(4)]
ID=(0,1,2,3)
def sw(a,b): p=list(ID); p[a],p[b]=p[b],p[a]; return tuple(p)
def comp(p,q): return tuple(q[p[i]] for i in range(4))  # (p.trans q) i = q (p i)
def rel(G, s, r): return [[[G[s[i]][r[j]][r[k]] for k in range(4)] for j in range(4)] for i in range(4)]
S23, S12, P1 = sw(2,3), sw(1,2), ID
R9=[(P1,P1),(P1,S23),(P1,S12),(S23,P1),(S23,S23),(S23,S12),(S12,P1),(S12,S23),(S12,S12)]
def circ(ri, t): a,b = R9[ri]; return rel(F(t), a, b)
def mt(G, q):
    (i1,i2,i3),(j1,j2,j3) = q
    return sp.simplify(G[i1][j1][j2]*G[i2][j2][j3]*G[i3][j3][j1])
def phases(src, tgt, t):
    """c with tgt[i][j][k] = conj(c_j) src[i][j][k] c_k, c_0 = 1, or None"""
    c = [sp.Integer(1)] + [sp.simplify(tgt[0][0][k]/src[0][0][k]) for k in range(1,4)]
    for i,j,k in itertools.product(range(4),repeat=3):
        if sp.simplify(tgt[i][j][k] - conj(c[j],t)*src[i][j][k]*c[k]) != 0: return None
    return c
gA=(P1, comp(sw(0,3), sw(1,2))); gB=(P1, comp(sw(0,1), sw(2,3))); gC=(comp(sw(0,3),sw(1,2)), P1); gD=(comp(sw(0,1),sw(2,3)), P1)
G={'gA':gA,'gB':gB,'gC':gC,'gD':gD}
print('(a) relabel g F(z) ~ F(conj z):')
for n,g in G.items():
    print(' ', n, g, phases(rel(F(z), g[0], g[1]), F(1/z), z))
print('(b) relabel g circ_r(w) ~ circ_r(w):')
for ri in range(1,9):
    for n,g in G.items():
        src = rel(circ(ri,w), g[0], g[1]); c = phases(src, circ(ri,w), w)
        if c is not None: print('  circle', ri, R9[ri], n, c); break
    else: print('  circle', ri, 'NONE')
IDX=[((a,b,c),(d,e,f)) for a in range(4) for b in range(4) for c in range(4) for d in range(4) for e in range(4) for f in range(4)]
print('(A) q_inj', mt(F(z), ((1,0,0),(0,1,0))))
print('(B) overlap coordinates:')
for ri in range(1,9):
    C=circ(ri,w); f=F(z); found=None
    for q in IDX:
        a, b = mt(f,q), mt(C,q)
        if not a.has(z) and not b.has(w) and sp.simplify(a+b)==0 and a!=0: found=('clash',q,a,b); break
    if not found:
        for q in IDX:
            a, b = mt(f,q), mt(C,q)
            if sp.simplify(a - z*sp.Rational(1,64))==0 or sp.simplify(a + z*sp.Rational(1,64))==0:
                if not b.has(w): found=('force',q,a,b); break
    print('  circle', ri, found)
