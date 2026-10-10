import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, symbols, expand, simplify, kronecker_product as kron
def E(m,n): B=zeros(4,4); B[m,n]=1; return B
def zdef(s1,s2): return (E(0,0)+s1*E(1,3)+s2*E(2,2)-s1*s2*E(3,1))/4
def prodState(x,y): return Matrix([1]+list(x))*Matrix([1]+list(y)).T
def ipW(a,b): return expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
a1,a2,a3,b1,b2,b3=symbols('a1 a2 a3 b1 b2 b3', real=True)
E0=E(0,0)+E(1,3)-E(2,2)
print("E0 pairing:", expand(4*ipW(prodState([a1,a2,a3],[b1,b2,b3]),E0)))
z=zdef(1,-1); Ms=Matrix(3,3,lambda i,j: 4*z[i+1,j+1]); print("Ms", Ms.tolist())
val=expand(4*ipW(prodState([a1,a2,a3],[b1,b2,b3]),z)); print("val", val)
print("form", expand(1+(Matrix([[a1,a2,a3]])*Ms*Matrix([b1,b2,b3]))[0]))
e0,e1,e2,e3,f0,f1,f2,f3=symbols('e0 e1 e2 e3 f0 f1 f2 f3', real=True)
ev=Matrix([e0,e1,e2,e3]); fv=Matrix([f0,f1,f2,f3])
print("P3 val", expand(4*(ev.T*z*fv)[0]), "form", expand(e0*f0+(Matrix([[e1,e2,e3]])*Ms*Matrix([f1,f2,f3]))[0]))
ME=Matrix(3,3,lambda i,j: E0[i+1,j+1]); print("ME", ME.tolist(), "singular values^2", (ME*ME.T).eigenvals())
