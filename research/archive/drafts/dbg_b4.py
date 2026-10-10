import sympy as sp
I2 = sp.eye(2); SX = sp.Matrix([[0,1],[1,0]]); SY = sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ = sp.Matrix([[1,0],[0,-1]])
SG = [I2, SX, SY, SZ]; kron = sp.kronecker_product
KR = {(m,n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m,n]*KR[(m,n)] for m in range(4) for n in range(4) if w[m,n] != 0), sp.zeros(4,4))/4
def tab(M): return sp.Matrix(4,4, lambda m,n: sp.nsimplify(sp.expand((KR[(m,n)]*M).trace())))
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
def E(m,n): B = sp.zeros(4,4); B[m,n] = 1; return B
def zdef(s1, s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = {(s1,s2): zdef(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
def bellstate(s1, s2): return sp.Matrix([1, s1*s2, s1, -s2])/2
fs = {s: bellstate(*s) for s in ZF}
for s in ZF:
    print(s, (tab((sp.eye(4) - 2*fs[s]*fs[s].H)/8) - ZF[s]).applyfunc(sp.simplify) == sp.zeros(4,4))
Ux = lambda t: sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SX
fprime = kron(Ux(sp.Rational(1,3)), I2)*fs[(1,1)]
for s in ZF: print("overlap", s, sp.simplify((fs[s].H*fprime)[0,0]))
alpha = sp.simplify((fs[(1,1)].H*fprime)[0,0]); beta = sp.simplify((fs[(1,-1)].H*fprime)[0,0])
print("alpha", alpha, "beta", beta, "rest", sp.simplify((fprime - alpha*fs[(1,1)] - beta*fs[(1,-1)]).norm()))
