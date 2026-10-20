"""A12: identify the SLP candidate: entries, G^2, relation to R and to R o (Zpi (x) 1)."""
import sys, json
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
body = cv.Body('eball3'); R = body.reference
G = cv.from_json_matrix(json.load(open(sys.argv[2]))['G'])
vals = sorted(set(v for r in G for v in r)); nz = sum(1 for r in G for v in r if v)
print('distinct entries', [str(v) for v in vals], 'nonzeros', nz)
print('G^2 == 1:', cv.mat_mul(G, G) == cv.eye(16))
Zc = cv.kron(cv.diag([1, -1, -1, 1]), cv.eye(4))
for name, M in (('R', R), ('R o (Zpi(x)1)', cv.mat_mul(R, Zc))):
    print('G ==', name, G == M)
K = cv.mat_mul(cv.inverse(R), G)
print('R^-1 G: distinct entries', sorted(set(str(v) for r in K for v in r)), 'diagonal?', all(K[i][j] == 0 for i in range(16) for j in range(16) if i != j))
print('R^-1 G diag', [str(K[i][i]) for i in range(16)])
