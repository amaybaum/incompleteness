# Exact check of the K2-GUARD-1 Target A chain on the kernel's own cnot tables (parsed, not transcribed).
import re, sys
from fractions import Fraction as Q
src = open(sys.argv[1], encoding='utf-8').read()
def table(name):
    block = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src).group(1)
    t = {}
    for m in re.finditer(r'(\d), (\d) => (\d)', block):
        t[(int(m.group(1)), int(m.group(2)))] = int(m.group(3))
    assert len(t) == 16
    return t
pc, pt = table('pc'), table('pt')
assert 'def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1' in src
sgn = lambda m, n: -1 if (m, n) in ((1, 3), (2, 2)) else 1
R = range(4)
cnot = lambda w: [[sgn(m, n) * w[pc[m, n]][pt[m, n]] for n in R] for m in R]
hom = lambda x: [Q(1)] + [Q(v) for v in x]
prod = lambda x, y: [[hom(x)[m] * hom(y)[n] for n in R] for m in R]
def actT(diag, w):  # homMap N on the second index: unit coordinate fixed
    D = [1] + diag
    return [[w[m][n] * D[n] for n in R] for m in R]
sharp = lambda b: [Q(1, 2)] + [Q(v, 2) for v in b]
pair = lambda a, b, w: sum(a[m] * w[m][n] * b[n] for m in R for n in R)
xplus, z3 = [1, 0, 0], [0, 0, 1]
phiW = cnot(prod(xplus, z3))
print('phiW =', phiW)
I4 = actT([1, -1, 1], phiW)
print('actT reflY phiW =', I4)
c = cnot(I4)
print('cnot(actT reflY phiW) =', c)
a, b = sharp([-1, 0, 0]), sharp([0, 0, -1])
print('sharpVec(-e1) =', a, ' sharpVec(-e3) =', b)
v = pair(a, b, c)
print('chain value (reflY) =', v)
rot = cnot(actT([1, -1, -1], phiW))
print('chain value (nflip, rotation control) =', pair(a, b, rot))
assert v == Q(-1, 2)
assert pair(a, b, rot) == 0
# reflY preserves the ball: it is diagonal with entries +-1
print('OK')
rotI = actT([1, -1, -1], phiW)
print('actT nflip phiW =', [[int(v) for v in r] for r in rotI])
print('cnot(actT nflip phiW) =', [[int(v) for v in r] for r in rot])
