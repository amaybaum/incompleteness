import sympy as sp, random
exec(open('dim1_lean_check.py').read().split('# SOS identity')[0])
def bloch(p):
    a,b,c,d=p
    return sp.Matrix([a*a+b*b+c*c+d*d, 2*(a*c+b*d), 2*(a*d-b*c), a*a+b*b-c*c-d*d])
def amp(p): return (p[0]+sp.I*p[1], p[2]+sp.I*p[3])
random.seed(1)
for trial in range(3):
    eta,xi,psi,phi=[tuple(sp.Rational(random.randint(-3,3)) for _ in range(4)) for _ in range(4)]
    E,F,P,Q=map(amp,(eta,xi,psi,phi))
    # identity gate normalization
    V0=(bloch(eta).T*(bloch(psi)*bloch(phi).T)*bloch(xi))[0,0]
    a0=sum(sp.conjugate(E[a])*P[a] for a in (0,1))*sum(sp.conjugate(F[b])*Q[b] for b in (0,1))
    print("id:", V0, sp.simplify(sp.Abs(a0)**2))
    c={(0,0):P[0]*Q[0],(0,1):P[0]*Q[1],(1,0):P[1]*Q[1],(1,1):P[1]*Q[0]}
    A=sum(sp.conjugate(E[a]*F[b])*c[(a,b)] for a in (0,1) for b in (0,1))
    V=(bloch(eta).T*cnot(bloch(psi)*bloch(phi).T)*bloch(xi))[0,0]
    print("cnot:", V, sp.simplify(sp.Abs(A)**2))
