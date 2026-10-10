"""K2, first read-only checks (exact). Not a record."""
import itertools, sympy as sp
I2=sp.eye(2); X=sp.Matrix([[0,1],[1,0]]); Y=sp.Matrix([[0,-sp.I],[sp.I,0]]); Z=sp.Matrix([[1,0],[0,-1]])
P=[I2,X,Y,Z]; kp=lambda A,B: sp.kronecker_product(A,B)
CN=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
# (a) the native group on C^4: <CNOT, X(x)I, I(x)X> is a finite group of permutation matrices
gens=[CN,kp(X,I2),kp(I2,X)]; H={sp.ImmutableMatrix(sp.eye(4))}; frontier=list(H)
while frontier:
    new=[]
    for h in frontier:
        for g in gens:
            k=sp.ImmutableMatrix(g*h)
            if k not in H: H.add(k); new.append(k)
    frontier=new
print('(a) |H| =',len(H),'; all permutation matrices:',all(all(x in (0,1) for x in h) for h in H))
# (b) the witness psi=(1,2,3,5): entangled after every basis permutation (det of the 2x2 amplitude matrix)
psi=[1,2,3,5]
dets=[q[0]*q[3]-q[1]*q[2] for q in itertools.permutations(psi)]
print('(b) min |a00 a11 - a01 a10| over all 24 permutations =',min(abs(x) for x in dets))
# (c) the reflected CNOT G' = (I(x)R) G (I(x)R), R: y -> -y (a ball automorphism, not in SO(3)), in Pauli coordinates
def bloch(U):
    B=[kp(P[a],P[b]) for a in range(4) for b in range(4)]
    return sp.Matrix(16,16,lambda i,j: sp.simplify((U*B[j]*U.H*B[i]).trace()/4))
G=bloch(CN); R=sp.diag(1,1,-1,1); IR=sp.kronecker_product(sp.eye(4),R)
Gp=IR*G*IR; N=sp.diag(1,1,-1,-1); IN=sp.kronecker_product(sp.eye(4),N); NI=sp.kronecker_product(N,sp.eye(4))
u=sp.Matrix([1,0,0,0]); z=sp.Matrix([0,0,0,1]); k=[u+z,u-z]
kr=lambda a,b: sp.kronecker_product(a,b)
frame=all(Gp*kr(k[a],k[b])==kr(k[a],k[a^b]) for a in (0,1) for b in (0,1))
print('(c) G\': frame',frame,'; G\'^2=I',Gp*Gp==sp.eye(16),'; Rt',IN*Gp*IN==Gp,'; Rc',NI*Gp*NI==IN*Gp)
# its image of the product state |+>|0> (Bloch (u+x)(x)(u+z)) as a 4x4 operator
v=Gp*kr(u+sp.Matrix([0,1,0,0]),u+z)
rho=sum((v[4*a+b]*kp(P[a],P[b]) for a in range(4) for b in range(4)),sp.zeros(4))/4
print('(c) eigenvalues of G\'(|+0><+0|):',sorted(rho.eigenvals().keys(), key=lambda e: float(e)))
