"""Exact certificates for the written coPSD family argument; not a cone search."""
import sympy as s

checks = 0
def require(value, name):
    global checks
    if not value:
        raise AssertionError(name)
    checks += 1

def zero(x):
    return x.applyfunc(s.simplify) == s.zeros(*x.shape)

def pt(x):
    return s.Matrix(4, 4, lambda i, j: x[2*(i//2)+j%2, 2*(j//2)+i%2])

def outer(v):
    return v * v.conjugate().T

def ad(k, x):
    return k*x*k.conjugate().T

eye = s.eye(4)
d = s.diag(1, (3+4*s.I)/5)
u = s.kronecker_product(s.eye(2), d)
p = s.Rational(5, 8)
def phi(x):
    return p*ad(u, x)+(1-p)*x

b = outer(s.Matrix([1, 0, 0, 1]))/2
require(pt(pt(b)) == b, 'transpose involution')
require(sorted(pt(b).eigenvals()) == [-s.Rational(1,2), s.Rational(1,2)], 'Bell exclusion')
require(pt(b).trace() == 1, 'trace normalization')
quantum_output = phi(b).applyfunc(s.simplify)
require(quantum_output.extract([0,3],[0,3]).det() == s.Rational(3,64), 'actual quantum PSD comparison')

# The actual local CP branch has genuinely complex, non-unitary coefficients.
k = s.Matrix([[1, s.I/3], [s.Rational(2, 5), s.Rational(1, 2)]])
lift = s.kronecker_product(s.eye(2), k)
liftbar = s.kronecker_product(s.eye(2), k.conjugate())
for i in range(4):
    for j in range(4):
        e = s.zeros(4)
        e[i,j] = 1
        require(pt(pt(e)) == e, f'involution {i},{j}')
        require(pt(e).trace() == e.trace(), f'trace {i},{j}')
        require(zero(pt(ad(lift,pt(e)))-ad(liftbar,e)), f'CP covariance {i},{j}')
        require(zero(pt(phi(pt(e)))-(p*ad(u.conjugate(),e)+(1-p)*e)), f'protocol covariance {i},{j}')

# A full orthogonal entangled frame, transformed as both states and effects.
h = s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
cnot = s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
frame_u = u*cnot*s.kronecker_product(h,s.eye(2))
frame = [pt(outer(frame_u[:,i])) for i in range(4)]
require(zero(sum(frame,s.zeros(4))-eye), 'frame effects sum to I')
for i in range(4):
    require(s.simplify(frame[i].trace()) == 1, f'frame trace {i}')
    require(zero(pt(frame[i])**2 - pt(frame[i])), f'preimage projector {i}')
    for j in range(4):
        require(s.simplify(s.trace(frame[i]*frame[j])) == int(i == j), f'frame distinction {i},{j}')
mixed = sum((s.Rational(i+1,10)*frame[i] for i in range(4)),s.zeros(4))
require(s.simplify(mixed.trace()) == 1, 'spectral mixture normalization')
require(sorted(pt(mixed).eigenvals()) == [s.Rational(i,10) for i in range(1,5)], 'spectral mixture probabilities')

# Classical diagonal control uses Phi itself, on a spanning cone family.
for i in range(4):
    e = s.zeros(4); e[i,i] = 1
    require(zero(phi(e)-e), f'classical fixed {i}')

# CNOT-tilted coPSD is still spectral, but is outside the common domain.
plus0 = outer(s.Matrix([1,0,1,0]))/2
tilt_preimage = pt(ad(cnot,plus0))
require(tilt_preimage == pt(b), 'tilted product preimage')
require(s.Rational(-1,2) in tilt_preimage.eigenvals(), 'tilted product fails inclusion')
singlet = outer(s.Matrix([0,1,-1,0]))/2
tilt_generator = ad(cnot,pt(singlet))
require(s.trace(tilt_generator*plus0) == -s.Rational(1,2), 'tilt also fails maxCone')
seed = outer(s.Matrix([1,1,1,0]))/3
tilt_state = ad(cnot,pt(seed))
test_vector = s.Matrix([1,s.I,-s.I,0])
tilt_test = ad(cnot,pt(outer(test_vector)/3))
require(pt(ad(cnot,tilt_state)) == seed, 'tilted seed membership')
require(s.simplify(s.trace(tilt_test*tilt_state)) == s.Rational(1,9), 'tilted input test positive')
require(s.simplify(s.trace(tilt_test*phi(tilt_state))) == -s.Rational(1,9), 'tilted actual protocol failure')

mutations = [
    ('wrong transpose', lambda: zero(pt(ad(lift,pt(b)))-ad(lift,b))),
    ('wrong phase', lambda: zero(pt(phi(pt(b)))-(p*ad(u,b)+(1-p)*b))),
    ('wrong effect', lambda: s.trace(frame[0]*frame[1]) == 1),
    ('wrong product claim', lambda: all(x >= 0 for x in tilt_preimage.eigenvals())),
]
for name, mutation in mutations:
    require(not mutation(), 'reject '+name)
print('CONTROLS', checks)
print('MUTATIONS rejected', len(mutations))
print('CERTIFICATES coPSD local preservation; CNOT tilt fails protocol and domain')
print('SP => guaranteed stopped-map preservation: OPEN on the common domain')
