"""C-SPH-1: the herald-statistics witness (owner review, 2026-10-22) as an exact regression check, its dependence on
the pool size, and the Poisson reservoir as a comparison.

Protocol W: prepare Z-mix or X-mix (both I/2) with an initial herald in window A, measure Z, and call the routed
station in a later disjoint window B; record whether the initial herald succeeds (H_A) and whether the second fails
(F_B). Each particle of a station crosses the aperture in A with probability a, in B with probability b, at most
once. Under Z-mix the outcome routes back to the station that supplied the initial particle; under X-mix it routes
to a Z station that has not been called before.

H1  exact enumeration of particle categories (Fractions), N = 3, a = b = 1/16.
H2  closed form: P(H_A F_B | Z-mix) - P(H_A F_B | X-mix) = ((1-a)(1-b))^N - (1-a-b)^N > 0 for a, b > 0, with the
    exact bound N ab ((1-a)(1-b))^(N-1) and the large-N form alpha beta e^(-alpha-beta)/N at a = alpha/N, b = beta/N.
H3  a Poisson-distributed particle number (mean mu) per station: the difference vanishes identically.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

def station_pmf(N,a,b):
    """Law of (any crossing in A, any crossing in B) for one station of N independent particles."""
    out={}
    for cats in product('ABn',repeat=N):
        p=F(1)
        for c in cats: p*={'A':a,'B':b,'n':1-a-b}[c]
        k=('A' in cats,'B' in cats); out[k]=out.get(k,F(0))+p
    return out
def protocol(N,a,b):
    st=station_pmf(N,a,b)
    pA=sum(p for (hA,hB),p in st.items() if hA)
    pnB=sum(p for (hA,hB),p in st.items() if not hB)
    # Z-mix: the same station supplies A and is called again in B
    z_HF=sum(p for (hA,hB),p in st.items() if hA and not hB)
    # X-mix: the initial station is an X station; window B is served by an independent, uncalled Z station
    x_HF=pA*pnB
    return z_HF/pA, x_HF/pA, z_HF-x_HF
def H1():
    print('H1  exact enumeration, N = 3, a = b = 1/16')
    zc,xc,d=protocol(3,F(1,16),F(1,16))
    print('    P(F_B | H_A, Z-mix) = %s   P(F_B | H_A, X-mix) = %s   difference %.5f'%(zc,xc,float(zc-xc)))
    print('    P(H_A F_B | Z-mix) - P(H_A F_B | X-mix) = %s (%.6f)'%(d,float(d)))
    ok=(zc,xc,d)==(F(631,721),F(3375,4096),F(151201,16777216))
    print('    owner values reproduced: %s'%ok)
    return ok
def H2():
    print('H2  closed form and pool-size dependence')
    a,b=sp.symbols('a b',positive=True); N=sp.symbols('N',positive=True,integer=True)
    z=(1-b)**N-(1-a-b)**N; x=(1-(1-a)**N)*(1-b)**N
    delta=sp.simplify(z-x-(((1-a)*(1-b))**N-(1-a-b)**N))
    print('    Z - X - [((1-a)(1-b))^N - (1-a-b)^N] simplifies to', delta)
    ok=delta==0
    # exact checks of the closed form, positivity and the bound on a grid, against H1's enumeration
    worst=F(0)
    for n in (1,2,3,4,6):
        for aa,bb in ((F(1,16),F(1,16)),(F(1,5),F(1,7)),(F(1,100),F(1,3)),(F(2,5),F(1,2))):
            _,_,d=protocol(n,aa,bb)
            cf=((1-aa)*(1-bb))**n-(1-aa-bb)**n
            bound=n*aa*bb*((1-aa)*(1-bb))**(n-1)
            ok&= d==cf and d>0 and d<=bound
            worst=max(worst,d/bound) if bound else worst
    print('    enumeration = closed form, positive for every N >= 1, and <= N ab ((1-a)(1-b))^(N-1): %s'%ok)
    al,be,n=sp.symbols('alpha beta n',positive=True)
    lead=sp.limit(n*((((1-al/n)*(1-be/n))**n-(1-(al+be)/n)**n)),n,sp.oo)
    print('    n * difference at a = alpha/n, b = beta/n tends to', sp.simplify(lead))
    ok&= sp.simplify(lead-al*be*sp.exp(-al-be))==0
    print('    so the witness falls as alpha beta e^(-alpha-beta)/N at fixed expected crossings; the coefficient\'s maximum e^-2 is an asymptotic scale')
    _,_,d=protocol(3,F(1,3),F(1,3))
    above=sp.Rational(d.numerator,d.denominator)>sp.exp(-2)/3
    print('    not a finite-N bound: N = 3, a = b = 1/3 gives %s (%.5f) > e^-2/3 (%.5f): %s'%(d,float(d),float(sp.exp(-2)/3),above))
    return ok and d==F(37,729) and bool(above)
def H3():
    print('H3  Poisson particle number per station (mean mu)')
    a,b,mu=sp.symbols('a b mu',positive=True); k=sp.symbols('k',integer=True,nonnegative=True)
    E=lambda expr: sp.simplify(sp.summation(sp.exp(-mu)*mu**k/sp.factorial(k)*expr,(k,0,sp.oo)))
    nA=E((1-a)**k); nB=E((1-b)**k); nAB=E((1-a-b)**k)
    z=nB-nAB; x=(1-nA)*nB
    d=sp.simplify(z-x)
    print('    P(no A) = %s, P(no B) = %s, P(no A, no B) = %s'%(nA,nB,nAB))
    print('    P(H_A F_B | Z-mix) - P(H_A F_B | X-mix) =', d)
    return d==0
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    r=[H1(),H2(),H3()]
    print('all checks:', 'green' if all(r) else 'RED')
