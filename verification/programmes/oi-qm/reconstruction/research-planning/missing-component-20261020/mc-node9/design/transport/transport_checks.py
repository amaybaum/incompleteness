"""Design calculation: can transport across an oriented surface produce the projected-area preparation law?
Part A (sympy): flux weighting of an isotropic direction law. Parts B-C (exact rationals): finite direction sets,
and reservoir depletion over repeated heralding windows."""
import sympy as sp
from fractions import Fraction as F
from itertools import product
# ---- Part A: flux weighting ----
th,ph=sp.symbols('theta phi',positive=True)
# isotropic directions (density 1/(4 pi)), fixed speed, positions uniform in a slab of thickness L behind a surface
# with normal u: during a short window tau, a particle with direction lambda crosses iff its depth < (u.lambda) tau,
# so the crossing-conditioned law is proportional to max(0, u.lambda) = cos(theta) on the facing hemisphere.
Z=sp.integrate(sp.integrate(sp.cos(th)*sp.sin(th),(th,0,sp.pi/2)),(ph,0,2*sp.pi))
print('Part A: integral of (u.lambda)_+ over directions =',Z,'-> herald law (u.lambda)_+/pi = mu_u (projected area)')
print('        herald success per window = tau/L * E[(u.lambda)_+] =',sp.simplify(Z/(4*sp.pi)),'* tau/L')
# ---- Part B: finite direction sets ----
def rational_sphere(N):
    return [(F(a,N),F(b,N),F(c,N)) for a,b,c in product(range(-N,N+1),repeat=3) if a*a+b*b+c*c==N*N]
def first_read(V,u,n):
    w={v:max(F(0),sum(a*b for a,b in zip(v,u))) for v in V}
    tot=sum(w.values())
    plus=sum(p for v,p in w.items() if sum(a*b for a,b in zip(v,n))>0)
    tie=sum(p for v,p in w.items() if sum(a*b for a,b in zip(v,n))==0)
    return plus/tot, tie/tot
X=(F(1),F(0),F(0)); Zax=(F(0),F(0),F(1)); R=(F(4,5),F(3,5),F(0))
lattice6=[(F(s),F(0),F(0)) for s in (1,-1)]+[(F(0),F(s),F(0)) for s in (1,-1)]+[(F(0),F(0),F(s)) for s in (1,-1)]
print('Part B: target P(+ | u=X+, n=R) = 9/10, P(+ | u=Z+, n=R) = 1/2 (ties: weight on the boundary n.lambda = 0)')
for name,V in [('cubic lattice, 6 directions',lattice6)]+[('rational sphere N=%d'%N,rational_sphere(N)) for N in (3,9,15,25,45)]:
    p1,t1=first_read(V,X,R); p2,t2=first_read(V,Zax,R)
    print('   %-30s |V|=%4d  X+/R: P=%s (err %s, tie %s)   Z+/R: P=%s (err %s, tie %s)'%(name,len(V),p1,abs(p1-F(9,10)),t1,p2,abs(p2-F(1,2)),t2))
# ---- Part C: reservoir depletion over repeated windows ----
# Slab depth L = 1 and window tau; direction v crosses in window k iff its depth lies in [(k-1) c tau, k c tau) with
# c = u.v > 0, intersected with [0, L). Herald law in window k is proportional to that band length.
def window_law(V,u,tau,k):
    out={}
    for v in V:
        c=sum(a*b for a,b in zip(v,u))
        if c<=0: continue
        lo,hi=(k-1)*c*tau,k*c*tau
        out[v]=max(F(0),min(hi,F(1))-min(lo,F(1)))
    return out
V=rational_sphere(15); tau=F(1,4)
print('Part C: rational sphere N=15, slab depth 1, window 1/4; herald law per window vs (u.v)_+')
for k in range(1,8):
    w=window_law(V,X,tau,k); tot=sum(w.values())
    if tot==0: print('   window %d: reservoir exhausted'%k); continue
    ref={v:max(F(0),v[0]) for v in V}; rt=sum(ref.values())
    dev=max(abs(w.get(v,F(0))/tot-ref[v]/rt) for v in V)
    plus=sum(p for v,p in w.items() if sum(a*b for a,b in zip(v,R))>0)/tot
    print('   window %d: max deviation from (u.v)_+ law = %s; P(+ | X+, R) = %s'%(k,dev,plus))
