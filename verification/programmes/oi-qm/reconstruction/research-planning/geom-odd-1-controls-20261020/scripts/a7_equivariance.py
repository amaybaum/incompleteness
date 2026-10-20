"""A7: is the eball3 reference gate equivariant under the stabiliser of (z3, nflip) (sign group diag(a, b, 1)),
acting on the control, the target, or both?  And the swap?  Exact."""
import sys, itertools
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1])
import controls_verify as cv
body = cv.Body('eball3'); R = body.reference
for a, b in itertools.product((1, -1), repeat=2):
    g = cv.diag([1, a, b, 1])
    for name, L in (('g(x)1', cv.kron(g, cv.eye(4))), ('1(x)g', cv.kron(cv.eye(4), g)), ('g(x)g', cv.kron(g, g))):
        print('diag(%d,%d,1) %s: commutes %s' % (a, b, name, cv.mat_mul(L, R) == cv.mat_mul(R, L)))
