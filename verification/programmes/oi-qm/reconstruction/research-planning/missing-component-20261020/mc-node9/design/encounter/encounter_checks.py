"""Exact checks of the owner's first encounter calculation (2026-10-22): crossing-time independence, the planar
two-collector deadline leak, and the spherical collector's constant arrival time. Hidden direction = direction of
motion at fixed speed v (an Added modelling identification)."""
import sympy as sp
from fractions import Fraction as F
from itertools import product
t,tau,L,v,th,ph,y,z,d=sp.symbols('t tau L v theta phi y z d',positive=True)
# ---- 1: crossing time and direction in the ideal slab ----
joint=v*sp.cos(th)/(4*sp.pi*L)                     # density in (t, Omega) on the facing hemisphere, before depletion
mass=sp.integrate(sp.integrate(sp.integrate(joint*sp.sin(th),(th,0,sp.pi/2)),(ph,0,2*sp.pi)),(t,0,tau))
cond=sp.simplify(joint/mass)
print('1: P(cross in [0,tau]) =',sp.simplify(mass),'; conditional density in (t, Omega) =',cond,
      '= (1/tau) * cos(theta)/pi  -> time uniform and independent of direction')
assert sp.simplify(cond-(1/tau)*sp.cos(th)/sp.pi)==0
# ---- 2: planar collectors at z = +-d with a deadline bit B: T < sqrt(2) d / v, i.e. lambda_z^2 > 1/2 ----
# Z-mix: on the Z+ disk (uniform), lambda_z^2 = 1 - r^2 > 1/2  <=>  r^2 < 1/2 : area pi/2.
PZ=sp.Rational(1,2)
# X-mix: on the X+ disk with coordinates (y, z), lambda_z = z: event |z| > 1/sqrt(2): two circular segments.
seg=sp.integrate(2*sp.sqrt(1-z**2),(z,1/sp.sqrt(2),1))
PX=sp.simplify(2*seg/sp.pi)
print('2: P(B | Z-mix) =',PZ,'; P(B | X-mix) =',PX,'; gap =',sp.simplify(PZ-PX),
      '; minimum common-prediction error =',sp.simplify((PZ-PX)/2))
assert sp.simplify(PX-(sp.Rational(1,2)-1/sp.pi))==0
# both collectors equally likely under either mixture (symmetric), so the Z outcome itself does not separate them
# ---- 3: finite disk grids, exact rational counts ----
def grid(M):
    return [(F(2*i+1,2*M),F(2*j+1,2*M)) for i,j in product(range(-M,M),repeat=2) if F(2*i+1,2*M)**2+F(2*j+1,2*M)**2<1]
for M in (10,40,160):
    g=grid(M)
    pz=F(sum(1 for a,b in g if 1-a*a-b*b>F(1,2)),len(g))     # Z disk: lambda_z^2 = 1 - r^2
    px=F(sum(1 for a,b in g if b*b>F(1,2)),len(g))           # X disk: lambda_z = second disk coordinate
    print('3: M=%3d: P(B|Z-mix) = %s, P(B|X-mix) = %s, gap = %s (1/pi ~ 0.31831)'%(M,pz,px,float(pz-px)))
# ---- 4: spherical collector of radius d ----
T_sphere=sp.simplify(d/v)
print('4: spherical collector: first-arrival time =',T_sphere,'for every direction; impact point = d * lambda',
      '(the old direction is written into the impact location)')
