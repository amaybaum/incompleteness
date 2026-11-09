"""rv_1059_checks.py -- independent reviewer probe for ASSESS-1059 (generic exact checks only).

Imports neither writer probe. Every object below is a generic mathematical object (unit vectors,
stabilizer states, frame functions); nothing is computed on an OI mechanism.

 C1  Column lemma, independently: for exact unit columns with profiles on a 1/4-grid of the
     4-simplex and on Pythagorean columns, sum_j |u_j|^p = 1 holds for p in {1/2, 1, 3, 4} iff the
     column is monomial.                                                   (supports R2/R3 =>)
 C2  Power family at the dyadic point: 2 * (2^{-1/2})^p = 1 has the unique positive solution p = 2.
     So stabilizer-scope agreement read through |amp|^p WOULD select p = 2.  (tests claim 4 scope)
 C3  Renormalised readout |u|^p / sum|u|^p: on a non-monomial column it is a law for every p, and the
     laws differ across p.  So R3 (=>) needs H-RF_p to mean the UNrenormalised |amp|^p summing to 1.
 C4  Supplied coherent preparation (1/sqrt2, 1/sqrt2): sum |a|^p = 2^{1-p/2} != 1 for p != 2.  So
     R3 (<=) "coherent preparations included" needs preparations to be p-normalised or generated
     by the admissible (monomial) operations.
 C5  All-n dyadic countercontrol: g(u) = u^2 (1 + sin^2(pi log_2 u^2)) equals u^2 at every
     u = 2^{-k/2}, k = 0..40, exactly; differs from u^2 at cos(pi/8).  (P2's f covers k <= 3 only)
 C6  Gleason-form check at stabilizer scope, dim 4 (two qubits): the frame functions on the 60
     stabilizer states over their 105 stabilizer orthonormal bases are exactly the trace forms
     <s|X|s>, X Hermitian with Tr X = 1 (affine dimension 15 both ways), but nonnegativity on the
     stabilizer states does not force X >= 0: a nonnegative frame function with non-PSD X exists.
     Controls: the trace-rule frame functions of rho = I/4 and rho = |00><00| satisfy the
     constraint system (count control: 60 states); mutation: a perturbed vector fails it.
Exit status 0 iff all checks pass.
"""
import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp

fails = []


def need(cond, msg):
    if not cond:
        fails.append(msg)


# ---------- C1 ----------------------------------------------------------------------------------
ps = [sp.Rational(1, 2), 1, 3, 4]
cnt = 0
for a in range(5):
    for b in range(5 - a):
        for c in range(5 - a - b):
            x = [sp.Rational(a, 4), sp.Rational(b, 4), sp.Rational(c, 4), sp.Rational(4 - a - b - c, 4)]
            mono = sorted(x)[-1] == 1
            for p in ps:
                s = sum(sp.sqrt(xi) ** p for xi in x)
                is_one = sp.simplify(s - 1) == 0
                need(is_one == mono, f"C1 grid {x} p={p}")
            cnt += 1
pyth = [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (2, 6, 9, 11)]   # a^2+b^2+c^2 = d^2
for a, b, c, d in pyth:
    u = [sp.Rational(a, d), sp.Rational(b, d), sp.Rational(c, d)]
    need(sum(t ** 2 for t in u) == 1, "C1 pyth unit")
    for p in ps:
        need(sp.simplify(sum(t ** p for t in u) - 1) != 0, f"C1 pyth {a,b,c,d} p={p}")
print(f"C1 column lemma: {cnt} grid profiles (n=4, step 1/4) + {len(pyth)} Pythagorean columns, p in {ps}:", not fails)

# ---------- C2 ----------------------------------------------------------------------------------
p = sp.symbols('p', positive=True)
sol = sp.solve(sp.Eq(2 * (2 ** sp.Rational(-1, 2)) ** p, 1), p)
need(sol == [2], f"C2 solution {sol}")
print("C2 power family at u = 2^{-1/2}, support 2: 2*u^p = 1 solves to p =", sol, ":", not fails)

# ---------- C3 ----------------------------------------------------------------------------------
col = [sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)]        # unit, non-monomial
laws = {}
for q in [1, 2, 3, sp.Rational(1, 2)]:
    w = [t ** q for t in col]
    tot = sum(w)
    law = [sp.nsimplify(t / tot) for t in w]
    need(sp.simplify(sum(law) - 1) == 0 and all(l >= 0 for l in law), f"C3 law p={q}")
    laws[q] = tuple(law)
need(len(set(laws.values())) == len(laws), "C3 laws distinct across p")
print("C3 renormalised readout is a law for every p and the laws differ:", not fails,
      {str(k): [str(v) for v in vv] for k, vv in laws.items()})

# ---------- C4 ----------------------------------------------------------------------------------
for q in [1, 3, 4, sp.Rational(1, 2)]:
    s = 2 * (1 / sp.sqrt(2)) ** q
    need(sp.simplify(s - 1) != 0, f"C4 p={q}")
need(sp.simplify(2 * (1 / sp.sqrt(2)) ** 2 - 1) == 0, "C4 control p=2")
print("C4 supplied 2-normalised coherent preparation is not p-normalised for p != 2:", not fails)

# ---------- C5 ----------------------------------------------------------------------------------
uu = sp.symbols('u', positive=True)
g = uu ** 2 * (1 + sp.sin(sp.pi * sp.log(uu ** 2, 2)) ** 2)
for k in range(41):
    pt = 2 ** sp.Rational(-k, 2)
    need(sp.simplify(g.subs(uu, pt) - pt ** 2) == 0, f"C5 k={k}")
    # normalisation on a flat support of size 2^k
    need(sp.simplify(2 ** k * g.subs(uu, pt) - 1) == 0, f"C5 norm k={k}")
cpi = sp.cos(sp.pi / 8)
val = sp.N(g.subs(uu, cpi) - cpi ** 2, 30)
need(abs(val) > sp.Float('1e-6'), "C5 non-dyadic control")
print("C5 g = u^2 on all 2^{-k/2} (k<=40) and normalises every flat 2^k support; g(cos pi/8)-cos^2 =", sp.N(val, 8), ":", not fails)

# ---------- C6 ----------------------------------------------------------------------------------
# Own enumeration: two-qubit stabilizer states as Gaussian-integer 4-vectors, canonical up to
# global phase and positive scale, generated by closure under H_1, H_2, S_1, S_2, CZ.
def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def canon(v):
    # normalise: divide by gcd of all real/imag parts; then fix phase by making the first nonzero
    # entry real positive after multiplying by its conjugate's unit part where possible; to be
    # robust against (1+i) phases, compare via the projector (outer product) instead.
    from math import gcd
    n2 = sum(a * a + b * b for a, b in v)
    # projector entries v_i conj(v_j) / n2 as exact Fractions: a phase-free key
    key = []
    for i in range(4):
        for j in range(4):
            a, b = v[i]
            c, d = v[j]
            re = a * c + b * d
            im = b * c - a * d
            key.append((Fr(re, n2), Fr(im, n2)))
    return tuple(key)


def H(v, q):
    w = list(v)
    for i in range(4):
        if not (i >> q) & 1:
            j = i | (1 << q)
            a, b = v[i], v[j]
            w[i] = (a[0] + b[0], a[1] + b[1])
            w[j] = (a[0] - b[0], a[1] - b[1])
    return tuple(w)


def S(v, q):
    return tuple(gmul(x, (0, 1)) if (i >> q) & 1 else x for i, x in enumerate(v))


def CZ(v):
    return tuple(((-x[0], -x[1]) if i == 3 else x) for i, x in enumerate(v))


start = ((1, 0), (0, 0), (0, 0), (0, 0))
seen = {canon(start): start}
front = [start]
while front:
    nxt = []
    for v in front:
        for w in (H(v, 0), H(v, 1), S(v, 0), S(v, 1), CZ(v)):
            k = canon(w)
            if k not in seen:
                seen[k] = w
                nxt.append(w)
    front = nxt
states = list(seen.values())
need(len(states) == 60, f"C6 count {len(states)}")


def ip(v, w):  # <v|w>
    re = sum(a * c + b * d for (a, b), (c, d) in zip(v, w))
    im = sum(a * d - b * c for (a, b), (c, d) in zip(v, w))
    return re, im


orth = {(i, j) for i in range(60) for j in range(60) if i != j and ip(states[i], states[j]) == (0, 0)}
bases = [b for b in itertools.combinations(range(60), 4)
         if all((b[x], b[y]) in orth for x in range(4) for y in range(x + 1, 4))]
need(len(bases) > 0, "C6 bases")
# frame functions: w in R^60 with sum over each basis = 1.  Affine dim = 60 - rank(A).
A = sp.Matrix([[1 if i in b else 0 for i in range(60)] for b in bases])
r = A.rank()
ff_dim = 60 - r
# trace-rule image: w_i = <s_i|rho|s_i>, rho Hermitian trace 1: affine dim = rank of the map
# from the 15-dim traceless Hermitian space; compute the rank of the 60 x 16 map on all Hermitian.
def proj_real_coords(v):
    n2 = sum(a * a + b * b for a, b in v)
    # <v|E|v> for a basis E of Hermitian 4x4: E_kk, (E_kl+E_lk), i(E_kl-E_lk)
    row = []
    for k in range(4):
        a, b = v[k]
        row.append(Fr(a * a + b * b, n2))
    for k in range(4):
        for l in range(k + 1, 4):
            a, b = v[k]
            c, d = v[l]
            re = a * c + b * d  # Re(conj(v_k) v_l)
            im = a * d - b * c  # Im(conj(v_k) v_l)
            row.append(Fr(2 * re, n2))
            row.append(Fr(-2 * im, n2))
    return row


B = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in proj_real_coords(s)] for s in states])
born_rank = B.rank()          # dim of span of Born frame functions as linear functionals of rho
born_affine = born_rank - 1   # trace-1 slice
need(born_affine == 15, f"C6 Born affine dim {born_affine}")
# The trace-form frame functions <s|X|s> (X Hermitian, Tr X = 1) lie in the frame-function space;
# equal affine dimensions mean every stabilizer-scope frame function has trace form.
need(ff_dim == born_affine, f"C6 frame-function dim {ff_dim} vs trace-form {born_affine}")
# Controls: trace-rule frame functions satisfy the constraints; a perturbation off them fails.
w_mixed = sp.Matrix([sp.Rational(1, 4)] * 60)
need(A * w_mixed == sp.ones(len(bases), 1), "C6 control rho=I/4")
w_pure = sp.Matrix([sp.Rational(x[0][0].numerator, x[0][0].denominator) for x in (canon(s) for s in states)])
need(A * w_pure == sp.ones(len(bases), 1), "C6 control rho=|00><00|")
bad = w_mixed.copy(); bad[0] += sp.Rational(1, 100)
need(A * bad != sp.ones(len(bases), 1), "C6 mutation: perturbed vector must fail")
# Positivity is not forced: X = I/4 + t (I/4 - |psi><psi|), psi = |0> (x) (cos pi/8 |0> + sin pi/8 |1>),
# t = 2/5.  X has eigenvalue 1/4 - 3t/4 = -1/20 < 0 on psi (not a density operator), yet
# <s|X|s> >= 0 on all 60 stabilizer states.
c8, s8 = sp.cos(sp.pi / 8), sp.sin(sp.pi / 8)
psi = sp.Matrix([c8, s8, 0, 0])        # index = 2*q1 + q0 ordering irrelevant: a product state
t = sp.Rational(2, 5)
X = sp.eye(4) / 4 + t * (sp.eye(4) / 4 - psi * psi.T)
need(sp.simplify(X.trace() - 1) == 0, "C6 trace")
need(sp.simplify((psi.T * X * psi)[0] + sp.Rational(1, 20)) == 0, "C6 X not PSD")
vals = []
for st in states:
    n2 = sum(a * a + b * b for a, b in st)
    vec = sp.Matrix([sp.Integer(a) + sp.I * b for a, b in st]) / sp.sqrt(n2)
    v = sp.nsimplify(sp.simplify((vec.H * X * vec)[0]))
    vals.append(v)
need(all(sp.N(v, 30) >= 0 and sp.simplify(sp.im(v)) == 0 for v in vals), "C6 nonneg on stabilizer states")
wq = sp.Matrix(vals)
need(all(sp.simplify(x) == 0 for x in (A * wq - sp.ones(len(bases), 1))), "C6 quasi-state frame function")
print(f"C6 two-qubit stabilizer scope: {len(states)} states, {len(bases)} stabilizer ONBs; frame-function "
      f"affine dim {ff_dim} = trace-form {born_affine}; a nonnegative frame function with non-PSD X "
      f"(min value {sp.N(min(vals, key=lambda z: sp.N(z)), 6)}):", not fails)

if fails:
    print("FAIL:", fails[:20])
    sys.exit(1)
print("ALL RV CHECKS PASS")
