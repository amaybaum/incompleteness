# exploratory (record-only): does Ad U(1/2) leave K(Z_F)? exact search for W = |w><w| with <w|z_m|w> >= 0 for all m
# and <w| U z U^dag |w> < 0.  Candidate w from a fixed rational/Gaussian-rational grid.
import sympy as sp
from itertools import product
I=sp.I; X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-I],[I,0]]); Z=sp.diag(1,-1); kr=sp.kronecker_product
S=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
Ps=(sp.eye(4)+S)/2; Pa=(sp.eye(4)-S)/2; U=Ps+I*Pa   # U(1/2) = P_sym + i P_anti
def z(s,t): return (sp.eye(4)+s*kr(X,Z)+t*kr(Y,Y)-s*t*kr(Z,X))/4
keys=[(1,1),(1,-1),(-1,1),(-1,-1)]
vals=[0,1,-1,I,-I]
found=None
for k in keys:
    M=U*z(*k)*U.H
    for c in product(vals,repeat=4):
        w=sp.Matrix(c)
        if w==sp.zeros(4,1): continue
        q=sp.expand((w.H*M*w)[0])
        if q.is_real and q<0 and all(sp.expand((w.H*z(*kk)*w)[0])>=0 for kk in keys):
            found=(k,list(c),q); break
    if found: break
print('witness (defect, w, <w|U z U^dag|w>):', found)
