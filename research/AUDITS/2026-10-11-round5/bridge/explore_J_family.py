# design exploration (not the check): is the two-term Bell family nonempty for U_J and for diag(1,w)?
import itertools, sympy as sp
I=sp.I; E2=sp.eye(2); X2=sp.Matrix([[0,1],[1,0]]); Y2=sp.Matrix([[0,-I],[I,0]]); Z2=sp.Matrix([[1,0],[0,-1]])
UJ=(E2-I*(X2+Y2+Z2))/2; w=sp.Rational(3,5)+I*sp.Rational(4,5); zPh=sp.diag(1,w)
SGN=[(1,1),(1,-1),(-1,1),(-1,-1)]
psi=lambda s: sp.Matrix([1,s[0]*s[1],s[0],-s[1]])/2
for name,U in (('zPh',zPh),('UJ',UJ),('id',E2),('X',X2)):
    W1=sp.kronecker_product(E2,U); found=[]
    for s in SGN:
        R=W1*psi(s)
        ov=[sp.simplify(sp.Abs((psi(t).H*R)[0,0])**2) for t in SGN]
        for a,b in itertools.permutations(SGN,2):
            for chi in (1,-1,I,-I):
                phi=(psi(a)+chi*psi(b))
                z_ok=all(sp.simplify(sp.Abs((psi(t).H*phi)[0,0])**2/2)<=sp.Rational(1,2) for t in SGN)
                o=sp.simplify(sp.Abs((phi.H*R)[0,0])**2/2)
                if z_ok and o>sp.Rational(1,2): found.append((s,a,b,chi,(1-2*o)/8))
    print(name,'overlaps of 1(x)U psi_(1,1) with Bell:',[sp.simplify(sp.Abs((psi(t).H*W1*psi((1,1)))[0,0])**2) for t in SGN],'certificates:',len(found),'min',min((f[4] for f in found),default=None))
