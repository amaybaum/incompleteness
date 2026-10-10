import sympy as sp, itertools
exec(open('sym.py').read().split("gA=(P1")[0])
zb, wb = sp.symbols('zb wb')
def Mr(t, tb): return [[1,1,1,1],[1,t,-1,-t],[1,-1,1,-1],[1,-t,-1,t]], [[1,1,1,1],[1,tb,-1,-tb],[1,-1,1,-1],[1,-tb,-1,tb]]
def Fr(t, tb):
    m, mb = Mr(t, tb)
    return [[[sp.Rational(1,4)*mb[i][j]*m[i][k] for k in range(4)] for j in range(4)] for i in range(4)]
def circr(ri, t, tb): a,b = R9[ri]; return rel(Fr(t,tb), a, b)
def mtr(G,q):
    (i1,i2,i3),(j1,j2,j3) = q
    return sp.expand(G[i1][j1][j2]*G[i2][j2][j3]*G[i3][j3][j1])
IDX=[((a,b,c),(d,e,f)) for a in range(4) for b in range(4) for c in range(4) for d in range(4) for e in range(4) for f in range(4)]
print('q_inj raw:', mtr(Fr(z,zb), ((1,0,0),(0,1,0))))
for ri,q in [(1,((0,0,2),(0,0,2))),(2,((0,0,2),(0,0,1))),(3,((0,0,2),(0,0,2))),(4,((0,0,1),(1,0,2))),(5,((0,0,1),(1,0,0))),(6,((0,0,1),(0,0,2))),(7,((0,0,1),(1,0,0))),(8,((0,0,1),(1,0,0)))]:
    print(' circle', ri, q, 'F raw:', mtr(Fr(z,zb),q), ' circ raw:', mtr(circr(ri,w,wb),q))
# quarter: circle 4; q2 with F constant c (no z,zb) and circ4 = c*w (no wb)
for q in IDX:
    a, b = mtr(Fr(z,zb),q), mtr(circr(4,w,wb),q)
    if a != 0 and not a.has(z) and not a.has(zb) and sp.simplify(b - a*w) == 0:
        print('q2 for circle 4:', q, a, b); break
# circle 4 at w=1 vs F(1): phases
exec(open('sym.py').read().split("print('(a)")[0].split("gA=(P1")[1].join(["",""]) if False else "")
c = phases(F(sp.Integer(1)), circ(4, sp.Integer(1)), z)
print('circ4(1) = conj(c_j) F(1) c_k with c =', c)
