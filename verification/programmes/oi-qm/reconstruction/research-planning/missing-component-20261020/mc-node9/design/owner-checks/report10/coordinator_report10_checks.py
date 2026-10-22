"""Coordinator check of the preparation/instrument screening report (2026-10-22), separate code.
The first-read feasible set for two preparations is the 2-D zonotope sum_lambda [0, (mu+(l), mu-(l))];
its vertices are enumerated exactly and the targets are tested against its edges."""
from fractions import Fraction as F
from itertools import product
lam=list(product((1,-1),repeat=3))
def corr(sign,c): return [(1+sign*x/F(2)+sign*y/F(2)+c*x*y)/8 for x,y,z in lam]
def zonotope(gs):
    gs=[g for g in gs if g!=(0,0)]
    # generators all lie in the first quadrant (probabilities); sort by slope, then walk both chains
    pos=[g for g in gs if g[0]!=0]; vert=[g for g in gs if g[0]==0]
    lower=sorted(pos,key=lambda g: g[1]/g[0])+vert          # increasing slope: lower-right chain
    pts=[(F(0),F(0))]
    for g in lower: pts.append((pts[-1][0]+g[0],pts[-1][1]+g[1]))
    for g in lower: pts.append((pts[-1][0]-g[0],pts[-1][1]-g[1]))   # upper-left chain, same slope order
    return pts[:-1]
def inside(pt,poly):
    n=len(poly); s=None
    for i in range(n):
        a,b=poly[i],poly[(i+1)%n]
        cr=(b[0]-a[0])*(pt[1]-a[1])-(b[1]-a[1])*(pt[0]-a[0])
        if cr!=0:
            if s is None: s=cr>0
            elif (cr>0)!=s: return False
    return True
target=(F(17,20),F(3,20))
mu,nu=corr(1,F(1)),corr(-1,F(0))
poly=zonotope(list(zip(mu,nu)))
print('correlated repair: target (17/20, 3/20) first-read feasible:',inside(target,poly))
print('  max over feasible set of P+ - P-/2 =',max(p[0]-p[1]/2 for p in poly),' target value',target[0]-target[1]/2)
print('  (5/6, 1/6) feasible:',inside((F(5,6),F(1,6)),poly))
# independent product encoding control
def prod_enc(s): return [ (1+s*x/F(2))/2*(1+s*y/F(2))/2*F(1,2) for x,y,z in lam]
poly2=zonotope(list(zip(prod_enc(1),prod_enc(-1))))
print('independent product encoding: target feasible:',inside(target,poly2))
# triple-correlation positive control
def tag(s): return [ (1+s*(x+y)/F(2))/4 if z==s*x*y else F(0) for x,y,z in lam]
tp,tm=tag(1),tag(-1)
E=lambda m,f: sum(w*f(*l) for w,l in zip(m,lam))
print('triple control: E(x),E(y),E(z) for s=+1:',[E(tp,lambda x,y,z,i=i:(x,y,z)[i]) for i in range(3)],
      ' s=-1:',[E(tm,lambda x,y,z,i=i:(x,y,z)[i]) for i in range(3)])
resp=lambda x,y,z:(1+F(7,10)*x*y*z)/2
print('  rotated response:',(E(tp,resp),E(tm,resp)),' first-read feasible (zonotope):',inside(target,zonotope(list(zip(tp,tm)))))
print('  TV(mu+,mu-) =',sum(abs(a-b) for a,b in zip(tp,tm))/2)
# quantum same-copy bound: ((X+Y)/2)^2 = I/2, so trace distance between rho_+- is 1/sqrt(2)
X=[[0,1],[1,0]]; Y=[[(0,0),(0,-1)],[(0,1),(0,0)]]
M=[[(F(0),F(0)),(F(1,2),F(-1,2))],[(F(1,2),F(1,2)),(F(0),F(0))]]      # (X+Y)/2 as complex pairs
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
sq=[[ (cm(M[i][0],M[0][j])[0]+cm(M[i][1],M[1][j])[0], cm(M[i][0],M[0][j])[1]+cm(M[i][1],M[1][j])[1]) for j in range(2)] for i in range(2)]
print('  ((X+Y)/2)^2 =',sq,' -> eigenvalues +-1/sqrt(2), trace distance 1/sqrt(2)')
# three retained nondisturbing reads, majority vote
p=F(17,20)
def maj(pp):
    tot=F(0)
    for outs in product((1,0),repeat=3):
        pr=F(1)
        for o in outs: pr*= pp if o else 1-pp
        if sum(outs)>=2: tot+=pr
    return tot
gap=maj(F(17,20))-maj(F(3,20))
print('three reads: P(maj=1|+) =',maj(F(17,20)),' gap =',gap,' gap^2 > 1/2:',gap*gap>F(1,2))
