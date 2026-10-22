"""C-SPH-1: the analytic read law derived from flux selection (owner derivation, 2026-10-22).

The fast-band herald of station S_w has direction law (w.lambda)_+ dOmega / pi (flux selection of an isotropic
reservoir; reference_checks.py V1). A destructive read along a reports s = sign(a.lambda). With x_+ = (|x| + x)/2 and
H the hemisphere of normal n = s a:
  integral over H of |w.lambda| dOmega = pi   (antipodal symmetry: half of the full-sphere integral 2 pi),
  integral over H of lambda dOmega = pi n,     so the linear part gives pi (n.w),
hence P(s | a, w) = (1/pi)(pi/2 + pi s a.w / 2) = (1 + s a.w)/2. The two hemisphere integrals are checked
symbolically here; the composed probability is then compared, as numerical evidence only, with direct quadrature of
the flux law for the menu pairs. Nothing here calls a quantum-reference routine.
"""
import sympy as sp
th,ph,al=sp.symbols('theta phi alpha',real=True)
lam=sp.Matrix([sp.sin(th)*sp.cos(ph),sp.sin(th)*sp.sin(ph),sp.cos(th)])
dO=sp.sin(th)
# full-sphere integral of |w.lambda| with w = z: 2 pi
full=sp.integrate(sp.integrate(sp.Abs(sp.cos(th))*dO,(th,0,sp.pi)),(ph,0,2*sp.pi))
# hemisphere H = {z > 0}: integral of lambda
hem=[sp.simplify(sp.integrate(sp.integrate(c*dO,(th,0,sp.pi/2)),(ph,0,2*sp.pi))) for c in lam]
ok=sp.simplify(full-2*sp.pi)==0 and hem==[0,0,sp.pi]
print('full-sphere integral of |w.lambda| = %s; hemisphere integral of lambda = %s: %s'%(full,hem,ok))
# |w.lambda| over the hemisphere equals half the full-sphere value for every w, by lambda -> -lambda
print('so P(s | a, w) = (1/pi)(pi/2 + pi s a.w/2) = (1 + s a.w)/2')
import numpy as np
# midpoint grid on (theta, phi), 2000 x 4000 cells; floating point, numerical evidence only
n1,n2=2000,4000
t=(np.arange(n1)+0.5)*np.pi/n1; p=(np.arange(n2)+0.5)*2*np.pi/n2
T,P=np.meshgrid(t,p,indexing='ij'); L=np.stack([np.sin(T)*np.cos(P),np.sin(T)*np.sin(P),np.cos(T)])
dA=np.sin(T)*(np.pi/n1)*(2*np.pi/n2)
AX={'X':(1,0,0),'Y':(0,1,0),'Z':(0,0,1),'R':(0.8,0.6,0)}
worst=0.0
for w in AX.values():
    fw=np.clip(np.tensordot(np.array(w,float),L,1),0,None)*dA/np.pi
    for a in AX.values():
        for s_ in (1,-1):
            v=fw[s_*np.tensordot(np.array(a,float),L,1)>0].sum()
            worst=max(worst,abs(v-(1+s_*sum(x*y for x,y in zip(a,w)))/2))
print('midpoint quadrature (2000 x 4000) of the flux law for the 32 menu cases agrees with (1 + s a.w)/2 to within %.1e (numerical evidence)'%worst)
print('derivation checks:','green' if ok else 'RED')
