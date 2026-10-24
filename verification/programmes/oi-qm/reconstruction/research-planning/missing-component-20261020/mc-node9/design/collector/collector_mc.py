"""Post-hoc numerical control (not part of the preregistered rule): a Monte Carlo of the mechanism itself, independent
of collector_predict.py's quadrature. Particles: isotropic directions, depth z ~ U[0,1) behind the plane of station
w, crossing time T = z/c for c = w.lambda > 0 (L = v = 1). The herald of window k is a particle with T in
[(k-1)/4, k/4); its first read along n is sign(n.lambda). Fixed seed; 4 * 10^7 particles; floating point, so this is
numerical evidence about the continuum value, not an exact check."""
import numpy as np, sys
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import collector_predict as CP
rng=np.random.default_rng(20261022)
n=40_000_000
v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
z=rng.random(n)
AX={'X':np.array([1.,0,0]),'Y':np.array([0,1.,0]),'Z':np.array([0,0,1.]),'R':np.array([.8,.6,0])}
W={'X+':AX['X'],'Y+':AX['Y'],'Z+':AX['Z'],'R+':AX['R']}
print(__doc__.splitlines()[0])
worst=0.
for w,nax,ca in CP.CASES:
    c=v@W[w]; ok=c>0; T=np.full(n,np.inf); T[ok]=z[ok]/c[ok]; s=(v@AX[nax])>0
    row=[]
    for k in range(1,9):
        m=(T>=(k-1)/4)&(T<k/4); cnt=m.sum(); p=s[m].mean(); se=np.sqrt(p*(1-p)/cnt)
        pc=float(CP.P_window(CP.mp.mpf(ca),k)); zsc=(p-pc)/se; worst=max(worst,abs(zsc))
        row.append('k=%d %.4f(%.4f) z=%+.1f'%(k,p,pc,zsc))
    print('  %s/%s: '%(w,nax)+'  '.join(row))
print('largest |z| over 32 cells: %.2f'%worst)
