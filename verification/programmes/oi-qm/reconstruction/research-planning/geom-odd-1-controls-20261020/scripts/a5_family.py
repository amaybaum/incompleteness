"""A5: which elementary modifications of the eball3 reference stay gates (exact verifier, pools A+B)."""
import sys
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1])
import controls_verify as cv
body = cv.Body('eball3')
R = body.reference
I4 = cv.eye(4)
def rotz(c, s):  # rotation about z3 = e_3 on the chart (x, y), hom coords
    return [[Fr(1),0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,Fr(1)]]
cands = {
  'R o (Zpi (x) 1)': cv.mat_mul(R, cv.kron(cv.diag([1,-1,-1,1]), I4)),
  'R o (Rz(3/5,4/5) (x) 1)': cv.mat_mul(R, cv.kron([[Fr(v) for v in r] for r in rotz(Fr(3,5),Fr(4,5))], I4)),
  '(Zpi (x) 1) o R': cv.mat_mul(cv.kron(cv.diag([1,-1,-1,1]), I4), R),
  'R o (1 (x) Xpi)': cv.mat_mul(R, cv.kron(I4, cv.diag([1,1,-1,-1]))),
}
for k, G in cands.items():
    r = cv.verify(body, G)
    print(k, r['verdict'], 'VL', r['VL'], 'VP', {a: r['VP'].get(a) for a in ('posFwd', 'posInv', 'posFwd_min', 'posInv_min')}, flush=True)
