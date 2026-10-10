import itertools
from fractions import Fraction
I=1j
h1=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
hi=[[1,1,1,1],[1,I,-1,-I],[1,-1,1,-1],[1,-I,-1,I]]
hm=[[1,1,1,1],[1,-1,-1,1],[1,-1,1,-1],[1,1,-1,-1]]
def gram(h):
    return lambda i,j,k: (complex(h[i][j]).conjugate()*h[i][k])/4
X=gram(h1); Y=gram(hi); M=gram(hm)
def relab1(s,G): return lambda i,j,k: G(s[i],s[j],s[k])
sw23=[0,1,3,2]
Ys=relab1(sw23,Y)
idx=[(a,b) for a in range(4) for b in range(4)]
def prod(A,B): return lambda i,j,k: A(i[0],j[0],k[0])*B(i[1],j[1],k[1])
def swapperm(p,q):
    return lambda x: q if x==p else (p if x==q else x)
def relab(t,G): return lambda i,j,k: G(t(i),t(j),t(k))
def prodperm(s1,s2): return lambda x:(s1[x[0]],s2[x[1]])
t0=swapperm((0,1),(1,0))
P=prod(X,Y); W=relab(t0,P)
def eq(a,b): return abs(a-b)<1e-12
def offlocus_witness(G):
    for i1,i1p,i2,j1,j2,k2 in itertools.product(range(4),repeat=6):
        if not eq(G((i1,i2),(j1,j2),(j1,k2)),G((i1p,i2),(j1,j2),(j1,k2))):
            return (i1,i1p,i2,j1,j2,k2)
    return None
def ineq_witness(G,H):
    # indices i,i',j,k with G i j k == G i' j k but H differ, or vice versa
    for i in idx:
      for ip in idx:
        for j in idx:
          for k in idx:
            a=eq(G(i,j,k),G(ip,j,k)); b=eq(H(i,j,k),H(ip,j,k))
            if a!=b: return (i,ip,j,k,a)
    return None
def full_invariant_equiv(G,H):
    # necessary: ratio invariants equal
    for i in idx:
      for ip in idx:
        for j in idx:
          for k in idx:
            if not eq(G(i,j,k)*G(ip,j,k).conjugate(), H(i,j,k)*H(ip,j,k).conjugate()): return False
    return True
print("W offlocus", offlocus_witness(W))
cands={
 'relab t0 prod(X,Ys)':relab(t0,prod(X,Ys)),
 'relab t0 prod(Y,Y)':relab(t0,prod(Y,Y)),
 'relab t0 prod(Y,X)':relab(t0,prod(Y,X)),
 'relab t0 prod(X,M)':relab(t0,prod(X,M)),
 'relab (sw23 x id) W':relab(prodperm(sw23,[0,1,2,3]),W),
 'relab (id x sw23) W':relab(prodperm([0,1,2,3],sw23),W),
 'relab swap(0,2)(2,0) P':relab(swapperm((0,2),(2,0)),P),
 'relab swap(0,1)(1,0) prod(Ys... )':relab(t0,prod(Ys,Y)),
}
for n,G in cands.items():
    print(n, 'offlocus-first-index:',offlocus_witness(G), 'ratio-invariants-equal-to-W:',full_invariant_equiv(W,G), 'ineq:',ineq_witness(W,G))
print('---- detail')
W2=relab(t0,prod(X,Ys))
W3=relab(prodperm([0,1,2,3],sw23),W)
print('W2==W3 entrywise?', all(eq(W2(i,j,k),W3(i,j,k)) for i in idx for j in idx for k in idx))
fixed=lambda x: t0(x)==x
for name,H in [('W2',W2),('W3',W3)]:
    sols=[]
    for i in idx:
      for ip in idx:
        for j in idx:
          for k in idx:
            a=eq(W(i,j,k),W(ip,j,k)); b=eq(H(i,j,k),H(ip,j,k))
            if a and not b and all(fixed(x) for x in (i,ip,j,k)):
              sols.append((i,ip,j,k,W(i,j,k),H(i,j,k),H(ip,j,k)))
    print(name,len(sols)); 
    for s in sols[:6]: print('  ',s)
# also check W2 vs W with W unequal/H equal
# a28 indices for W2
print('W2 a28 idx', W2((0,1),(2,0),(2,1)), W2((1,1),(2,0),(2,1)))
