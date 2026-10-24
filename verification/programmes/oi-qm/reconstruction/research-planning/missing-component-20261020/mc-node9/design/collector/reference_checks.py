"""C-SPH-1 reference construction and coupling bound (REFERENCE.md): checks of the components.

V1  (sympy) the aperture-crossing intensity of one station inside the fast band factorizes as (Lambda/T) dt x mu_w,
    with Lambda = mu q and q = eta v T/(4L).
V2  (sympy) TV(Bernoulli(q), Poisson(q)) = q (1 - e^-q) <= q^2.
V3  (mpmath interval arithmetic, rigorous) TV(Binomial(N, q), Poisson(Nq)) <= N q^2 on a grid. This is the per-station
    distance of the full arrival records, since conditional on the count both have i.i.d. points (Unif[0,T] x mu_w).
V4  (exact) protocol W of herald_checks.py against the coupling bound: the fixed-pool difference is at most
    2 m Lambda^2 / N with m = 8 and Lambda = N (a + b), and it vanishes for the Poisson reference.
"""
import sympy as sp
import mpmath as mp
from fractions import Fraction as F
import sys, os, math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import herald_checks as HC

def V1():
    mu,eta,v,L,T,th=sp.symbols('mu eta v L T theta',positive=True)
    # direction measure dOmega/(4 pi) in polar angle about w; c = cos(theta) > 0; crossing at depth z = v t c, so the
    # time density is v c / L for t < L/(v c), which for t <= T <= L/v holds for every c in (0, 1]
    dens=mu*eta*(v*sp.cos(th)/L)*sp.sin(th)/2              # per dt per dtheta, azimuth integrated
    rate=sp.integrate(dens,(th,0,sp.pi/2))
    q=eta*v*T/(4*L); Lam=mu*q
    ok=sp.simplify(rate-Lam/T)==0
    mark=sp.simplify(dens/rate)                              # conditional law of theta given a crossing at t
    ok&=sp.simplify(mark-2*sp.cos(th)*sp.sin(th))==0         # = (c/pi) dOmega with azimuth integrated: mu_w
    print('V1  crossing rate = %s = Lambda/T; mark density in theta = %s (the projected-area law mu_w): %s'%(sp.simplify(rate),mark,ok))
    return ok
def V2():
    q=sp.symbols('q',positive=True)
    pb={0:1-q,1:q}; pp=lambda k: sp.exp(-q)*q**k/sp.factorial(k)
    tv=sp.simplify(((pp(0)-pb[0])+(pb[1]-pp(1))+(1-pp(0)-pp(1)))/2)   # signs: e^-q >= 1-q and q >= q e^-q
    ok=sp.simplify(tv-q*(1-sp.exp(-q)))==0
    # q (1 - e^-q) <= q^2 iff 1 - e^-q <= q, i.e. e^-q >= 1 - q
    g=sp.exp(-q)-(1-q); ok&= sp.simplify(sp.diff(g,q)-(1-sp.exp(-q)))==0 and g.subs(q,0)==0
    print('V2  TV(Bernoulli(q), Poisson(q)) = %s <= q^2 (e^-q >= 1 - q): %s'%(tv,ok))
    return ok
def V3():
    iv=mp.iv; iv.dps=40; ok=True; worst=0.0; n=0
    for N in (1,2,3,5,10,30,100):
        for q in (F(1,1000),F(1,100),F(1,20),F(1,8),F(1,3),F(1,2)):
            Q=iv.mpf(q.numerator)/q.denominator; lam=N*Q
            tv=iv.mpf(0)
            for k in range(N+1):
                pb=iv.mpf(math.comb(N,k))*Q**k*(1-Q)**(N-k)
                pp=iv.exp(-lam)*lam**k/iv.mpf(math.factorial(k))
                d=pb-pp
                if d.a>0: tv+=d
                elif d.b>0: tv+=iv.mpf([0,d.b])           # sign undecided at this precision: take the safe upper end
            bound=N*Q*Q
            ok&= tv.b<=bound.a; n+=1; worst=max(worst,float(mp.mpf(tv.b)/mp.mpf(bound.a)))
    print('V3  TV(Binomial(N, q), Poisson(Nq)) <= N q^2 on %d grid points (interval arithmetic): %s; largest ratio %.3f'%(n,ok,worst))
    return ok
def V4():
    ok=True; n=0; worst=F(0)
    for N in (1,2,3,4,6,10):
        for a,b in ((F(1,16),F(1,16)),(F(1,3),F(1,3)),(F(1,100),F(1,7)),(F(2,5),F(1,2))):
            _,_,d=HC.protocol(N,a,b); Lam=N*(a+b); bound=min(F(1),2*8*Lam**2/N)
            ok&= 0<d<=bound; n+=1; worst=max(worst,d/bound)
    print('V4  protocol W: 0 < fixed-pool difference <= min(1, 16 Lambda^2/N) on %d cases: %s; largest ratio %.4f'%(n,ok,float(worst)))
    print('    Poisson reference: difference identically 0 (herald_checks.py H3)')
    return ok
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[V1(),V2(),V3(),V4(),HC.H3()]
    print('all checks:', 'green' if all(r) else 'RED')
