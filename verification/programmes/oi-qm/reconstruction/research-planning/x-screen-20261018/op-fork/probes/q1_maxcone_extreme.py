#!/usr/bin/env python3
"""q1_maxcone_extreme.py -- node N1 and controls C4, C5 of ../PREREG.md.  Exact (SymPy over Q(i)); research only.

N1  Extreme rays of maxCone (= SEP*, two qubits).  Zero-set first-order method: if Y = W1 + W2 with W1, W2 in
    maxCone, then at every product zero (a, b) of <ab|Y|ab> each f_i(a,b) = <ab|W_i|ab> >= 0 vanishes, hence is
    stationary there: (I(x)<b|) W_i |ab> = 0 and (<a|(x)I) W_i |ab> = 0.  The real-linear solution space S of these
    conditions at a finite set of zeros contains every such W_i; dim S = 1 (spanned by Y) certifies that Y is extreme
    in maxCone.  Using a finite subset of zeros can only enlarge S, so dim S = 1 is sound.
C4  countercontrol: the same routine on a non-extreme element must return dim S >= 2.
C5  identification of the relating set R = O(3) on tables: Gamma acts on token-2 Pauli coefficients as the
    y-reflection (det -1); Ad_{I(x)u} acts by an orthogonal matrix of det +1 (exact sample u).
Transport [WA, printed only]: Ad_{A(x)I} for invertible A and Gamma are linear automorphisms of maxCone, every
Schmidt-rank-2 vector is (A(x)I)Phi+ up to scale, every product is a local-unitary image of |00>, so N1 at B, Gamma(B),
P00 gives: Ext(maxCone) contains all rank-one PSD tables and their Gamma-images; with maxCone = Q3 + Gamma(Q3)
(Stormer-Woronowicz [L]) and Ext(C1 + C2) <= Ext(C1) u Ext(C2) it is exactly that set.
"""
import sympy as sp
from itertools import product

I = sp.I
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -I], [I, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)
PA = [I2, X, Y, Z]
kr = sp.kronecker_product
def pt2(M):
    R = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        R[2*a+d, 2*c+b] = M[2*a+b, 2*c+d]
    return R
res = []
def chk(name, c):
    res.append((name, bool(c))); print(('PASS ' if c else 'FAIL ') + name)

basis = [kr(PA[m], PA[n]) for m in range(4) for n in range(4)]
w = sp.symbols('w0:16', real=True)
Wsym = sum((w[k]*basis[k] for k in range(16)), sp.zeros(4, 4))
def coeffs(M):
    return [sp.nsimplify(sp.simplify((M*basis[k]).trace()/4)) for k in range(16)]

def nullspace_dim(zeros, target):
    eqs = []
    for a, b in zeros:
        a = sp.Matrix(a); b = sp.Matrix(b); ab = kr(a, b)
        v = Wsym*ab
        v1 = kr(I2, b.H)*v
        v2 = kr(a.H, I2)*v
        for e in list(v1) + list(v2):
            e = sp.expand(e)
            eqs += [sp.re(e), sp.im(e)]
    A = sp.Matrix([[sp.expand(e).coeff(w[k]) for k in range(16)] for e in eqs])
    ns = A.nullspace()
    tv = sp.Matrix(coeffs(target))
    inspan = False
    if len(ns) >= 1:
        Nm = sp.Matrix.hstack(*ns)
        inspan = Nm.rank() == sp.Matrix.hstack(Nm, tv).rank()
    return len(ns), inspan, A.rank()

qs = [0, 1, I, 2, 1 + I, -1, sp.Rational(1, 2) - I, 3*I, sp.Rational(-2, 3) + sp.Rational(1, 5)*I]
s2 = sp.sqrt(2)
phi = sp.Matrix([1, 0, 0, 1]); B = phi*phi.H/2

# zeros of <ab|B|ab> = |a0 b0 + a1 b1|^2/2 : b = (-a1, a0)
zB = [((1, q), (-q, 1)) for q in qs] + [((0, 1), (-1, 0))]
d, ins, r = nullspace_dim(zB, B)
chk('N1  B = Phi+Phi+^dag: zero-set nullspace dim = 1 and spanned by B (extreme in maxCone)', d == 1 and ins)
print('     dims: nullspace=%d constraint-rank=%d zeros=%d' % (d, r, len(zB)))
for a, b in zB:
    av = sp.Matrix(a); bv = sp.Matrix(b)
    assert sp.simplify((kr(av, bv).H*B*kr(av, bv))[0]) == 0
chk('N1  every sampled (a, b) is a zero of B (checked exactly)', True)

GB = pt2(B)
chk('N1  Gamma(B) = SWAP/2', GB == sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])/2)
# zeros of <ab|SWAP|ab> = |<a|b>|^2 : b orthogonal to a
zG = [((1, q), (-sp.conjugate(q), 1)) for q in qs] + [((0, 1), (1, 0))]
for a, b in zG:
    av = sp.Matrix(a); bv = sp.Matrix(b)
    assert sp.simplify((kr(av, bv).H*GB*kr(av, bv))[0]) == 0
d, ins, r = nullspace_dim(zG, GB)
chk('N1  Gamma(B) = SWAP/2: zero-set nullspace dim = 1 and spanned by Gamma(B) (extreme; direct check, independent of Gamma-transport)', d == 1 and ins)
print('     dims: nullspace=%d constraint-rank=%d zeros=%d' % (d, r, len(zG)))

P00 = sp.diag(1, 0, 0, 0)
z00 = [((0, 1), (1, q)) for q in qs] + [((1, q), (0, 1)) for q in qs]
d, ins, r = nullspace_dim(z00, P00)
chk('N1  P00 = |00><00|: zero-set nullspace dim = 1 and spanned by P00 (products extreme in maxCone)', d == 1 and ins)
print('     dims: nullspace=%d constraint-rank=%d zeros=%d' % (d, r, len(z00)))

# A non-maximally entangled direct instance (independent of congruence transport)
ca, cb = sp.Rational(3, 5), sp.Rational(4, 5)
chi = sp.Matrix([ca, 0, 0, cb]); Cch = chi*chi.H
# zeros: ca a0 b0 + cb a1 b1 = 0  ->  b = (-cb a1, ca a0)
zC = [((1, q), (-cb*q, ca)) for q in qs] + [((0, 1), (-cb, 0))]
for a, b in zC:
    av = sp.Matrix(a); bv = sp.Matrix(b)
    assert sp.simplify((kr(av, bv).H*Cch*kr(av, bv))[0]) == 0
d, ins, r = nullspace_dim(zC, Cch)
chk('N1  chi = 3/5|00> + 4/5|11>: nullspace dim = 1, spanned by chi chi^dag (direct instance)', d == 1 and ins)
# zeros of Gamma(chi chi^dag): <ab|Gamma(C)|ab> = <a b*|C|a b*> -> b* = (-cb a1, ca a0)
zGC = [((1, q), (sp.conjugate(-cb*q), sp.conjugate(ca))) for q in qs] + [((0, 1), (-cb, 0))]
for a, b in zGC:
    av = sp.Matrix(a); bv = sp.Matrix(b)
    assert sp.simplify((kr(av, bv).H*pt2(Cch)*kr(av, bv))[0]) == 0
d, ins, r = nullspace_dim(zGC, pt2(Cch))
chk('N1  Gamma(chi chi^dag): nullspace dim = 1, spanned by it (direct instance)', d == 1 and ins)

# C4 countercontrol: non-extreme element (B + P_{Psi+})/2 must give dim >= 2
psi_p = sp.Matrix([0, 1, 1, 0]); Mne = (B + psi_p*psi_p.H/2)/2
# common zeros: a0b0 + a1b1 = 0 and a0b1 + a1b0 = 0 -> (a0+a1)(b0+b1)=0 and (a0-a1)(b0-b1)=0
zM = [((1, 1), (1, -1)), ((1, -1), (1, 1))]
for a, b in zM:
    av = sp.Matrix(a); bv = sp.Matrix(b)
    assert sp.simplify((kr(av, bv).H*Mne*kr(av, bv))[0]) == 0
d, ins, r = nullspace_dim(zM, Mne)
chk('C4  countercontrol: non-extreme (B + P_Psi+)/2 gives nullspace dim >= 2 (routine can report non-extreme)', d >= 2)
print('     dims: nullspace=%d' % d)
d2, _, _ = nullspace_dim([zB[0]], B)
chk('C4  countercontrol: a single zero of B leaves dim >= 2 (dimension 1 is earned by the zero set, not forced)', d2 >= 2)

# C5 identification of R = O(3)
def action_matrix(f):
    """3x3 matrix of the token-2 action on Pauli coefficients (I(x)sigma_j -> sum_k R_kj I(x)sigma_k)."""
    R = sp.zeros(3, 3)
    for j in range(3):
        img = f(kr(I2, PA[j+1]))
        for k in range(3):
            R[k, j] = sp.simplify((img*kr(I2, PA[k+1])).trace()/4)
    return R
RG = action_matrix(pt2)
chk('C5  Gamma acts on token-2 Pauli coefficients as diag(1,-1,1) (y-reflection, det -1)', RG == sp.diag(1, -1, 1) and RG.det() == -1)
okG = all(pt2(kr(PA[m], PA[n])) == (-1 if n == 2 else 1)*kr(PA[m], PA[n]) for m in range(4) for n in range(4))
chk('C5  Gamma fixes token 1 and every token-2 coefficient except y (all 16 Pauli products)', okG)
us = [sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]]),
      sp.diag(1, I), sp.Matrix([[1, 1], [1, -1]])/s2,
      sp.Matrix([[1 + I, 1 - I], [1 - I, 1 + I]])/2]
okU = True
for u in us:
    Ru = action_matrix(lambda M: kr(I2, u)*M*kr(I2, u).H)
    okU &= sp.simplify(Ru.T*Ru) == sp.eye(3) and sp.simplify(Ru.det()) == 1
chk('C5  Ad_{I(x)u} acts by SO(3) on token-2 coefficients (4 exact u)', okU)
RT = action_matrix(lambda M: pt2(kr(I2, us[0])*M*kr(I2, us[0]).H))
chk('C5  Gamma o Ad_{I(x)u} acts by an improper orthogonal matrix (det -1)', sp.simplify(RT.T*RT) == sp.eye(3) and sp.simplify(RT.det()) == -1)

nf = sum(1 for _, c in res if not c)
print('SUMMARY checks=%d failed=%d' % (len(res), nf))
n1 = all(c for n, c in res if n.startswith('N1'))
ctl = all(c for n, c in res if n.startswith('C'))
print('RESULT N1_maxcone_ext_rank1_and_gamma=%s' % ('GREEN' if n1 else 'RED'))
print('RESULT C4=%s' % ('GREEN' if all(c for n, c in res if n.startswith('C4')) else 'RED'))
print('RESULT C5=%s' % ('GREEN' if all(c for n, c in res if n.startswith('C5')) else 'RED'))
print('VERDICT', 'N1-GREEN: B, Gamma(B), P00 and a non-maximal chi (and its Gamma-image) are extreme in maxCone by exact '
      'zero-set nullspaces of dimension 1; countercontrols report non-extreme where required' if nf == 0 else 'VOID')
