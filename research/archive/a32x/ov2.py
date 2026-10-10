exec(open('sym.py').read().split("print('(a)")[0])
zb, wb = sp.symbols('zb wb')
def conj(e, t): return e.subs(t, {z: zb, w: wb}[t])
def F(t):
    m = M(t)
    return [[[sp.Rational(1,4)*conj(sp.sympify(m[i][j]), t)*m[i][k] for k in range(4)] for j in range(4)] for i in range(4)]
def mt(G, q):
    (i1,i2,i3),(j1,j2,j3) = q
    return sp.expand(G[i1][j1][j2]*G[i2][j2][j3]*G[i3][j3][j1])
OV = {1:((0,0,2),(0,0,2)),2:((0,0,2),(0,0,1)),3:((0,0,2),(0,0,2)),4:((0,0,1),(3,0,0)),5:((0,0,1),(1,0,0)),6:((0,0,1),(0,0,2)),7:((0,0,1),(1,0,0)),8:((0,0,1),(1,0,0))}
for ci,q in OV.items(): print(ci, q, mt(F(z),q), '|', mt(circ(ci,w),q))
print('q1', mt(F(z),((0,0,1),(3,0,0))), mt(circ(4,w),((0,0,1),(3,0,0))))
print('q2', mt(F(z),((0,0,1),(2,0,0))), mt(circ(4,w),((0,0,1),(2,0,0))))
