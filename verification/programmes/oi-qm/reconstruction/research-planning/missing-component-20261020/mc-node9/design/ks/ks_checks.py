"""Design audit checks for the Kochen-Specker qubit model with projected-area preparation (owner, 2026-10-22).
Part 1 uses sympy for exact symbolic algebra; parts 2-3 use exact rationals on finite disk grids."""
import sympy as sp
from fractions import Fraction as F
from itertools import product
# ---- Part 1: projected-area density and the first-read formula (exact, symbolic) ----
th,ph,al,r,x1,x2,c=sp.symbols('theta phi alpha r x1 x2 c',positive=True)
# lifting a point of the unit disk (area pi) onto the facing hemisphere: dA = cos(theta) dOmega
J=sp.simplify(sp.diff(sp.sin(th),th)*sp.sin(th))      # dA = d(rho^2/2) dphi with rho = sin(theta): rho drho = sin cos dtheta
print('Part 1a: dA/(dtheta dphi) =',J,'= cos(theta) * [sin(theta) dtheta dphi = dOmega]')
print('         density on the hemisphere = cos(theta)/pi; total mass =',
      sp.integrate(sp.integrate(sp.cos(th)/sp.pi*sp.sin(th),(th,0,sp.pi/2)),(ph,0,2*sp.pi)))
# region of the u-disk whose lift lies in H_n, n at angle alpha from u (0 < alpha < pi/2): boundary
# sin(alpha) x1 + cos(alpha) sqrt(1 - x1^2 - x2^2) = 0 with x1 < 0, i.e. an ellipse of semi-axes cos(alpha), 1
ell=sp.simplify((sp.cos(al)**2*(1-x1**2-x2**2)-sp.sin(al)**2*x1**2) - sp.cos(al)**2*(1-x1**2/sp.cos(al)**2-x2**2))
print('Part 1b: boundary equation minus ellipse x1^2/cos^2(alpha) + x2^2 = 1 :',ell)
P=sp.simplify((sp.pi - (sp.pi/2 - sp.pi*sp.cos(al)/2))/sp.pi)
print('         P(+ | u, n) = [area of disk minus (left half-disk minus left half-ellipse)]/pi =',P)
assert sp.simplify(P-(1+sp.cos(al))/2)==0
# ---- Part 2: finite grid family; exact rational counts ----
def grid(M):
    pts=[]
    for i,j in product(range(-M,M),repeat=2):
        X,Y=F(2*i+1,2*M),F(2*j+1,2*M)
        if X*X+Y*Y<1: pts.append((X,Y))
    return pts
def in_Hn(pt,s,cA):      # lift of pt (u-disk) lies in H_n, n = (s, 0, cA), s = sin(alpha) >= 0, cA = cos(alpha) >= 0
    X,Y=pt; lhs=s*X               # need s*X + cA*sqrt(1-X^2-Y^2) > 0
    if lhs>=0: return lhs>0 or cA>0
    return cA*cA*(1-X*X-Y*Y) > lhs*lhs
print('Part 2: finite disk grids, u = X+, n = R (cos alpha = 4/5): target 9/10')
for M in (5,20,80):
    g=grid(M); k=sum(in_Hn(p,F(3,5),F(4,5)) for p in g); P_=F(k,len(g))
    print('   M=%3d: %5d cells, P = %s, error = %s'%(M,len(g),P_,abs(P_-F(9,10))))
# ---- Part 3: the conditional-swap recording interaction on a finite grid ----
# State: system direction lambda (a lifted grid cell, stored as (hemisphere axis, cell)); apparatus: one fresh
# disk seed s (a grid cell) plus a dump register. Measuring along n: sigma = sign(n . lambda); the system receives
# the lift of s around sigma*n; the dump register receives the old lambda. The map is injective on its domain.
def measure(lam_cell_axis, seed, n_axis_sign):
    return ('lift', n_axis_sign, seed), lam_cell_axis
M=5; g=grid(M)
seen={}
inj=True
for axis_sign in (1,-1):
    for lam in g:
        for s in g:
            lamstate=('lift',axis_sign,lam)
            sigma=axis_sign                      # measuring along the preparation axis itself: sign = axis_sign
            out=measure(lamstate,s,sigma)
            if out in seen: inj=False
            seen[out]=(lamstate,s)
print('Part 3: conditional swap on the M=5 grid is injective:',inj,'(',len(seen),'images )')
print('        scope: a restricted ready-state domain (fresh seed), measurement along the preparation axis only;')
print('        not a permutation of a complete apparatus state space and not an implementation by OI dynamics.')
print('        The fresh seed lifted around sigma*n already incorporates the KS reset law: it implements the')
print('        reset, it does not derive it.')
# ---- Part 4: owner's discard-access witness (exact) ----
# Procedures Z-mix = (mu_{+Z} + mu_{-Z})/2 and X-mix, both quantum I/2. Discard read E: lambda_z^2 > lambda_x^2.
# On the +Z preparation disk E is 1 - x^2 - y^2 > x^2, the ellipse 2x^2 + y^2 < 1.
x=sp.symbols('x',real=True)
area=sp.integrate(2*sp.sqrt(1-2*x**2),(x,-1/sp.sqrt(2),1/sp.sqrt(2)))
PZ=sp.simplify(area/sp.pi)
PX=sp.simplify(1-PZ)          # x <-> z symmetry: under X-mix, P(lambda_z^2 > lambda_x^2) = 1 - P(lambda_x^2 > lambda_z^2)
print('Part 4: discard read E = [lambda_z^2 > lambda_x^2]: P(E|Z-mix) =',PZ,' P(E|X-mix) =',PX,
      ' gap =',sp.nsimplify(sp.simplify(PZ-PX)),'; quantum value 0 (both procedures are I/2)')
assert sp.simplify(PZ-1/sp.sqrt(2))==0 and sp.simplify(PZ-PX-(sp.sqrt(2)-1))==0
