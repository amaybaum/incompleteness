"""Exact certificates for next-plan.md; universal claims are in next-result.md."""
import sympy as s

I = s.I
R = s.Rational
count = 0


def require(ok, name):
    global count
    if not ok:
        raise AssertionError(name)
    count += 1


def eq(a, b):
    return all(s.simplify(x) == 0 for x in a - b)


def gamma(x):
    return s.Matrix(4, 4, lambda r, c: x[2*(r//2)+c%2, 2*(c//2)+r%2])


def ad(u, x):
    return u*x*u.conjugate().T


z = (3+4*I)/5
D = s.diag(1, z)
L = s.kronecker_product(s.eye(2), D)
Lc = s.kronecker_product(s.eye(2), D.conjugate())
S = s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
A = s.Matrix([[R(3,5),-R(4,5)],[R(4,5),R(3,5)]])
U = s.kronecker_product(A,D)
V = s.kronecker_product(A,D.conjugate())


def phi(x):
    return R(5,8)*ad(L,x)+R(3,8)*x


# Symbolic certificate for the two-dimensional product-subspace lemma.
x0,x1,y0,y1,r0,r1,t0,t1 = s.symbols('x0 x1 y0 y1 r0 r1 t0 t1')
M = s.Matrix([x0,x1])*s.Matrix([[y0,y1]]) + s.Matrix([r0,r1])*s.Matrix([[t0,t1]])
require(s.expand(M.det()-(x0*r1-x1*r0)*(y0*t1-y1*t0)) == 0,
        'product-subspace determinant')
# Complex pure-projector partial-transpose certificate in a phase-fixed chart.
a,b,c,d,e = s.symbols('a b c d e', real=True)
w = s.Matrix([a,b,c,d+I*e])
detpt = gamma(w*w.conjugate().T).det(method='domain-ge')
require(s.expand(detpt+((a*d-b*c)**2+a*a*e*e)**2) == 0,
        'pure partial-transpose determinant')
require(eq(U.conjugate().T*U,s.eye(4)), 'local unitary')
require(eq(S*S,s.eye(4)), 'swap involution')

for r in range(4):
    for c0 in range(4):
        X = s.zeros(4); X[r,c0] = 1
        require(eq(gamma(gamma(X)),X), 'transpose involution')
        require(eq(gamma(ad(U,gamma(X))),ad(V,X)), 'local cone covariance')
        require(eq(gamma(ad(U*S,gamma(X))),ad(V*S,X.T)), 'swap cone covariance')
        require(eq(gamma(phi(gamma(X))),R(5,8)*ad(Lc,X)+R(3,8)*X),
                'actual stopped-map covariance')

p = s.Matrix([1,1,1,1])/2
E = s.diag(1,1,1,z)
Q = p*p.conjugate().T
bad = gamma(ad(E.conjugate().T,Q))
require(s.simplify(bad.det()) == -R(1,400), 'entangling tilt rejects product')
require(eq(E.conjugate().T*E,s.eye(4)), 'entangling tilt unitary')

m0,m1,m2,m3 = s.symbols('m0 m1 m2 m3',real=True)
require(s.expand(sum(2*m-1 for m in (m0,m1,m2,m3))) == 2*(m0+m1+m2+m3)-4,
        'all-center obstruction')
require(2*1-4 == -2, 'normalized obstruction')
B = s.Matrix([1,0,0,1])*s.Matrix([[1,0,0,1]])/2
out = phi(B)
require(s.simplify(out.extract([0,3],[0,3]).det()) == R(3,64),
        'quantum positive comparison')
require(s.simplify(gamma(B).det()) == -R(1,16), 'Q3 inclusion gate')
for j in range(4):
    P = s.zeros(4); P[j,j] = 1
    require(eq(phi(P),P), 'classical actual-map comparison')

# Countercontrols reject altered hypotheses/identities rather than print
# an outcome over red required controls.
mutations = [
    not eq(gamma(ad(L,gamma(B))),ad(L,B)),  # omitted phase conjugation
    not eq(gamma(B),B),                   # full transpose substituted
    s.simplify(s.Matrix(2,2,list(E.conjugate().T*p)).det()) != 0,
                                             # entangling tilt admitted as local
    s.trace(s.eye(4)/2) != 1,              # unnormalized center substituted
]
for i, rejected in enumerate(mutations):
    require(bool(rejected), f'mutation {i+1}')
print(f'controls: {count}; mutations rejected: {len(mutations)}')
print('entangling phase product preimage determinant: -1/400')
print('four-outcome reflection pairing sum: -2')
print('certificate controls pass; generic SP implication remains open')
