#!/usr/bin/env python3
"""Thread G -- exact controls for candidate effect families P2 (read-only research; certified main 6d0abf6b).

Exact arithmetic only: fractions.Fraction and sympy (rationals, sqrt(3), Gaussian rationals). No floats in any check.
Each check is labelled with its kind:
  identity  -- a symbolic identity simplified to exactly 0
  witness   -- an exact instance
  enumerate -- an exhaustive finite enumeration
  deduce    -- an exact step of a written deduction (the deduction is in REPORT.md)
  mutation  -- a countercontrol: the opposite verdict appears when the load-bearing ingredient changes
Written steps are printed as notes and not counted.

Sections
  ONT   closure stability: a fixed ontic realization's response family Resp(p) is closed under every ontically
        implemented operation (mixing, complement, coarse-graining, sequential instruments, attach/stochastic/readout/
        discard); the map is c -> M^T c with M column-(sub)stochastic
  DOM   the domination certificate: 1-h(z) <= (1/delta)(1-h(x)) for every h in Resp(p), delta = min_i p_i(x); linear in
        h, so it survives convex hulls and pointwise limits; mutation at a tangency point (delta = 0)
  SIC   tight SIC (t=1) vs loose SIC (t=1/2) realization of the same Bloch ball; response coefficients of the sharp
        effect; tangency sets; pullback by a rotation covers a target pure state in the tight case only
  ONTD  the ball drive is not ontically implementable in the tight SIC realization: p o R o p^{-1} is not stochastic
  BID   the bidisk with two simplex realizations R1 (all facets touch at torus points) and R2 (facets on flat faces):
        same body, same automorphism group; SEC of the G-closed response family fails for R1 (delta = 2/C > 0 at
        (e1, 0) over the whole orbit) and holds for R2
  STG   a finite stage (triangle) with the GPT-standard operational closure conv{0,1,a,1-a,b,1-b}: SEC fails at an edge
        midpoint (delta = 1/4); the no-restriction effect (2a+b)/2 supports it
  MAT   matrix regime, qubit: monomial (substratum) unitaries fix the Bloch z-axis up to sign, so J_off_axis fails;
        their effects are diagonal = response on two configurations; Naimark circuit with a non-monomial V gives the
        sharp effect V|0><0|V^dagger; with monomial V it stays diagonal
  NR    no-restriction closure on the SIC: the affine span of the responses is all affine functionals; the sharp effect
        has coefficients outside [0,1]
"""
import sys
from fractions import Fraction as Fr
from itertools import product
import random

import sympy as sp

FAIL = []
COUNT = [0]
NOTES = []


def chk(name, ok, kind):
    COUNT[0] += 1
    tag = 'ok  ' if ok else 'FAIL'
    print('  [%s] %-80s (%s)' % (tag, name, kind))
    if not ok:
        FAIL.append(name)


def note(text):
    NOTES.append(text)
    print('  [note] %s  (written step, not a check)' % text)


def section(title):
    print('\n== %s' % title)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


rng = random.Random(20261001)


def rfrac(den=7):
    return Fr(rng.randint(0, den), den)


# ================================================================== ONT
section('ONT  Resp(p) is closed under ontically implemented operations (c -> M^T c)')


def rand_stoch(nrow, ncol, den=6):
    """column-stochastic nrow x ncol with rational entries"""
    M = [[Fr(0)] * ncol for _ in range(nrow)]
    for j in range(ncol):
        w = [rng.randint(0, den) for _ in range(nrow)]
        if sum(w) == 0:
            w[0] = 1
        s = sum(w)
        for i in range(nrow):
            M[i][j] = Fr(w[i], s)
    return M


def in01(v):
    return all(0 <= x <= 1 for x in v)


N = 4
ok_seq = ok_att = ok_mix = ok_coarse = True
for trial in range(200):
    # sequential instrument: sub-stochastic M_k summing to a stochastic map, then outcome-dependent responses c_k
    K = 3
    Mfull = rand_stoch(N * K, N)  # rows (j,k) -> split into M_k
    Mk = [[Mfull[j * K + k] for j in range(N)] for k in range(K)]
    ck = [[rfrac() for _ in range(N)] for _ in range(K)]
    newc = [sum(Mk[k][j][s] * ck[k][j] for k in range(K) for j in range(N)) for s in range(N)]
    ok_seq &= in01(newc)
    # attach ancilla (ontic state a0 of A=3), joint stochastic map on N*3, response on joint, discard
    A = 3
    M = rand_stoch(N * A, N * A)
    cj = [rfrac() for _ in range(N * A)]
    a0 = rng.randrange(A)
    newc2 = [sum(cj[r] * M[r][s * A + a0] for r in range(N * A)) for s in range(N)]
    ok_att &= in01(newc2)
    # mixing and complement and coarse-graining of a test
    c1 = [rfrac() for _ in range(N)]
    c2 = [rfrac() for _ in range(N)]
    lam = rfrac(5)
    ok_mix &= in01([lam * a + (1 - lam) * b for a, b in zip(c1, c2)]) and in01([1 - a for a in c1])
    test = rand_stoch(3, N)  # a three-outcome test: columns sum to one
    ok_coarse &= in01([test[0][s] + test[2][s] for s in range(N)])
chk('sequential instrument (sub-stochastic M_k, responses c_k): sum_k M_k^T c_k in [0,1]^N, 200 trials', ok_seq,
    'enumerate')
chk('attach ancilla, joint stochastic map, joint readout, discard: vector in [0,1]^N, 200 trials', ok_att, 'enumerate')
chk('mixing and complement of response vectors stay in [0,1]^N, 200 trials', ok_mix, 'enumerate')
chk('coarse-graining two outcomes of a test stays in [0,1]^N, 200 trials', ok_coarse, 'enumerate')
note('Resp(p) = {q -> c.q : c in [0,1]^N} is compact and convex, so limits and convex closure add nothing; with the '
     'four checks, every operation implemented by stochastic maps on the N ontic states returns a response vector')

# ================================================================== DOM
section('DOM  the domination certificate')
# generic check on random realizations of a polytope-free body: take q = p(x) with all coordinates positive
ok_dom = True
for trial in range(300):
    qx = [Fr(rng.randint(1, 9)) for _ in range(N)]
    s = sum(qx)
    qx = [a / s for a in qx]
    delta = min(qx)
    c = [rfrac() for _ in range(N)]
    qz = [Fr(rng.randint(0, 9)) for _ in range(N)]
    s = sum(qz) or 1
    qz = [a / s for a in qz] if sum(qz) else [Fr(1)] + [Fr(0)] * (N - 1)
    one_minus_hx = sum((1 - ci) * a for ci, a in zip(c, qx))
    one_minus_hz = sum((1 - ci) * a for ci, a in zip(c, qz))
    ok_dom &= (one_minus_hz * delta <= one_minus_hx)
chk('1 - h(z) <= (1/delta)(1 - h(x)) for random response h, ontic z, delta = min_i p_i(x) > 0 (300 trials)', ok_dom,
    'enumerate')
note('the inequality delta (1 - h(z)) <= 1 - h(x) is affine in h, so it holds on the closed convex hull of any family '
     'satisfying it; if it holds and h(x) = 1 then h = 1 on the body, so h is not proper')
# mutation: at a point with a zero coordinate, delta = 0 and the certificate is silent; 1 - p_i is certain there
qx = [Fr(0), Fr(1, 2), Fr(1, 4), Fr(1, 4)]
h = [Fr(0), Fr(1), Fr(1), Fr(1)]
chk('mutation: at a tangency point (p_0 = 0) the effect 1 - p_0 is certain and proper', sum(a * b for a, b in zip(h, qx))
    == 1 and sum(a * b for a, b in zip(h, [Fr(1), 0, 0, 0])) < 1, 'mutation')

# ================================================================== SIC
section('SIC  tight (t = 1) and loose (t = 1/2) realizations of the same Bloch ball')
r3 = sp.sqrt(3)
S = [sp.Matrix([1, 1, 1]), sp.Matrix([1, -1, -1]), sp.Matrix([-1, 1, -1]), sp.Matrix([-1, -1, 1])]
a = [si / r3 for si in S]
chk('s_i . s_j = 3 delta_ij - (1 - delta_ij)', all((S[i].dot(S[j]) == (3 if i == j else -1)) for i in range(4)
                                                     for j in range(4)), 'enumerate')
chk('sum_i a_i = 0 and sum_i a_i a_i^T = (4/3) I', zero(sum(a, sp.zeros(3, 1)).norm()) and
    all(zero(e) for e in (sum((ai * ai.T for ai in a), sp.zeros(3, 3)) - sp.Rational(4, 3) * sp.eye(3))), 'identity')
MINS = {}
x, y, z = sp.symbols('x y z', real=True)
rv = sp.Matrix([x, y, z])
for t in (sp.Integer(1), sp.Rational(1, 2)):
    p = [(1 + t * ai.dot(rv)) / 4 for ai in a]
    J = sp.Matrix([[sp.diff(pi, v) for v in (x, y, z)] for pi in p])
    chk('t = %s: p is affine, sums to 1, linear part rank 3 (injective on the ball)' % t,
        zero(sum(p) - 1) and J.rank() == 3, 'identity')
    # minimum of p_i on the unit ball is (1 - t)/4 at r = -a_i (Cauchy-Schwarz; attained)
    mins = [sp.nsimplify(pi.subs({x: -ai[0], y: -ai[1], z: -ai[2]})) for pi, ai in zip(p, a)]
    chk('t = %s: min_ball p_i = (1 - t)/4, attained at r = -a_i' % t, all(zero(m - (1 - t) / 4) for m in mins), 'identity')
    MINS[t] = min(mins)
note('Cauchy-Schwarz: a_i . r >= -|r| >= -1 on the ball with equality only at r = -a_i, so p_i >= (1 - t)/4 with the '
     'tangency set T = {-a_i} for t = 1 (Main.md:540 SIC) and T empty for t = 1/2')
chk('loose (t = 1/2): delta = min_i min_ball p_i = %s > 0 at EVERY state (a global minimum, so rotation-invariant)'
    % MINS[sp.Rational(1, 2)], MINS[sp.Rational(1, 2)] == sp.Rational(1, 8), 'deduce')
chk('mutation: tight (t = 1): the same minimum is %s, attained (tangency points exist)' % MINS[sp.Integer(1)],
    MINS[sp.Integer(1)] == 0, 'mutation')
note('so by DOM, in the loose realization no closure of Resp(p) under mixing, limits, ontic operations or pullback by any '
     'rotation group contains a proper effect certain anywhere: SEC fails at every boundary state; the tight '
     'realization of the same ball has 4 tangency points')
# sharp effect coefficients
n = sp.Matrix([0, 0, 1])
c = [(1 + 3 * n.dot(ai)) / 2 for ai in a]
chk('sharp effect (1+z)/2 = sum_i c_i p_i (tight) with c_i = (1 + 3 n.a_i)/2', zero(
    sum(ci * (1 + ai.dot(rv)) / 4 for ci, ai in zip(c, a)) - (1 + z) / 2), 'identity')
chk('c_1 = 1/2 + sqrt(3)/2 > 1 (Main.md:540) and c_2 = 1/2 - sqrt(3)/2 < 0', zero(c[0] - (sp.Rational(1, 2) + r3 / 2))
    and sp.simplify(c[0] - 1) > 0 and sp.simplify(c[1]) < 0, 'witness')
# pullback by a rotation R with R(-a_1) = b, b rational unit
b = sp.Matrix([sp.Rational(3, 5), 0, sp.Rational(4, 5)])
pb = [sp.nsimplify(sp.simplify((1 + ai.dot(b)) / 4)) for ai in a]
chk('tight, no drive: at the pure state b = (3/5, 0, 4/5) every p_i > 0 (min %s), so DOM excludes support at b'
    % sp.nsimplify(min(pb, key=lambda q: float(q))), all(sp.simplify(q) > 0 for q in pb), 'witness')


def refl(w):
    return sp.eye(3) - 2 * (w * w.T) / (w.T * w)[0]


Hw = refl(-a[0] - b)
Hu = refl(sp.Matrix([0, 1, 0]))
R = sp.simplify(Hu * Hw)
chk('R = H_u H_w is a rotation (R^T R = I, det R = 1) with R(-a_1) = b', all(zero(e) for e in (R.T * R - sp.eye(3)))
    and zero(R.det() - 1) and all(zero(e) for e in (R * (-a[0]) - b)), 'identity')
p_t = [(1 + ai.dot(rv)) / 4 for ai in a]
pulled = 1 - p_t[0].subs(dict(zip((x, y, z), list(R.T * rv))), simultaneous=True)
chk('tight: the pulled-back response 1 - p_1 o R^{-1} is certain at b and proper (value 1/2 at -b)',
    zero(pulled.subs({x: b[0], y: b[1], z: b[2]}) - 1) and zero(pulled.subs({x: -b[0], y: -b[1], z: -b[2]}) - sp.Rational(1, 2)),
    'witness')
note('ball3Drive (KF:449) has flow = rotations about the third axis and J = cyc3 (KF:425); conjugating by cyc3 gives the '
     'rotations about the other two axes, so the group generated is SO(3) (Euler angles): in the tight realization the '
     'drive group carries the 4 tangency points onto the whole sphere, so the G-closed response family is SEC-complete')

# ================================================================== ONTD
section('ONTD  the ball drive is not ontically implementable in the tight SIC realization')


def rotz(cs, sn):
    return sp.Matrix([[cs, -sn, 0], [sn, cs, 0], [0, 0, 1]])


def ontic_map(Rm):
    # column i = p(R * 3 a_i) = ((1 + s_j . R s_i)/4)_j
    return sp.Matrix(4, 4, lambda j, i: (1 + S[j].dot(Rm * S[i])) / 4)


Mpi = ontic_map(rotz(-1, 0))
chk('control: the half-turn about z (a tetrahedral symmetry) induces a permutation matrix (stochastic)',
    all(e in (0, 1) for e in Mpi) and all(sum(Mpi[:, i]) == 1 for i in range(4)), 'witness')
for (cs, sn) in [(Fr(3, 5), Fr(4, 5)), (Fr(12, 13), Fr(5, 13)), (Fr(99, 101), Fr(20, 101))]:
    Mt = ontic_map(rotz(sp.Rational(cs.numerator, cs.denominator), sp.Rational(sn.numerator, sn.denominator)))
    colsum = all(zero(sum(Mt[:, i]) - 1) for i in range(4))
    neg = min(Mt)
    chk('rotation about z with (cos, sin) = (%s, %s): columns sum to 1, min entry %s < 0 (not stochastic)'
        % (cs, sn, neg), colsum and neg < 0, 'witness')
note('the affine extension of a drive member to the simplex hyperplane is unique (p(ball) spans it), so a drive member '
     'is implementable by a stochastic map of the 4 ontic states only if this matrix is stochastic: small rotations are '
     'not; at a fixed finite realization both effects (Main.md:540) and the drive fail, as design note §9 states')

# ================================================================== BID
section('BID  the bidisk D x D with two simplex realizations')
U = [(3, 4), (-3, 4), (4, -3), (-4, -3), (0, -2)]
Vv = [(0, -2), (3, 4), (-3, 4), (4, -3), (-4, -3)]


def norm2(w):
    return sp.sqrt(sp.Integer(w[0]) ** 2 + sp.Integer(w[1]) ** 2)


def realization(Us, Vs):
    cs = [norm2(u) + norm2(v) for u, v in zip(Us, Vs)]
    C = sum(cs)
    return cs, C


x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2', real=True)
for label, Us, Vs in [('R1', U, Vv),
                      ('R2', [(3, 0), (0, 4), (0, 0), (0, 0), (-3, -4)], [(0, 0), (0, 0), (3, 0), (0, 4), (-3, -4)])]:
    cs, C = realization(Us, Vs)
    ell = [ci - (u[0] * x1 + u[1] * x2) - (v[0] * y1 + v[1] * y2) for ci, u, v in zip(cs, Us, Vs)]
    p = [e / C for e in ell]
    lin = sp.Matrix([[u[0], u[1], v[0], v[1]] for u, v in zip(Us, Vs)])
    chk('%s: sum_i p_i = 1, linear part rank 4 (affine injective into the simplex Delta_4)' % label,
        zero(sum(p) - 1) and lin.rank() == 4, 'identity')
    chk('%s: c_i = |u_i| + |v_i|, so min_bidisk p_i = 0 (tangent facets)' % label,
        all(zero(ci - norm2(u) - norm2(v)) for ci, u, v in zip(cs, Us, Vs)), 'identity')
    if label == 'R1':
        chk('R1: every facet touches the bidisk at one torus point (u_i, v_i both nonzero)',
            all(norm2(u) > 0 and norm2(v) > 0 for u, v in zip(Us, Vs)), 'enumerate')
        # min over |w| = 1 of p_i(w, 0) is (c_i - |u_i|)/C and of p_i(0, w) is (c_i - |v_i|)/C (Cauchy-Schwarz)
        orbmins = [min(ci - norm2(u), ci - norm2(v)) / C for ci, u, v in zip(cs, Us, Vs)]
        delta = min(orbmins)
        chk('R1: min over the orbit {(w,0),(0,w): |w|=1} of (e1,0) of p_i is min(|v_i|,|u_i|)/C; delta = %s > 0' % delta,
            all(zero(om - min(norm2(u), norm2(v)) / C) for om, u, v in zip(orbmins, Us, Vs)) and delta > 0, 'identity')
        # exact spot check on rational points of the orbit
        okspot = True
        for (cw, sw) in [(1, 0), (Fr(3, 5), Fr(4, 5)), (Fr(-5, 13), Fr(12, 13)), (0, -1), (Fr(-8, 17), Fr(-15, 17))]:
            cw, sw = sp.nsimplify(cw), sp.nsimplify(sw)
            for pt in ({x1: cw, x2: sw, y1: 0, y2: 0}, {x1: 0, x2: 0, y1: cw, y2: sw}):
                okspot &= all(sp.nsimplify(pi.subs(pt)) >= delta for pi in p)
        chk('R1: exact spot check of p_i >= delta at 10 rational orbit points of (e1, 0)', okspot, 'enumerate')
        chk('(e1,0) is a boundary state: (e1,0) + eps((e1,0) - (-e1,0)) has |x|^2 = (1 + 2 eps)^2 > 1, eps = 1/k, k < 50',
            all((1 + 2 * Fr(1, k)) ** 2 > 1 for k in range(1, 50)), 'witness')
        note('(e1,0) + eps((e1,0) - y) for y = (-e1, 0) in D x D leaves D x D for every eps > 0, so (e1,0) is an '
             'IsBoundaryState (KF:130) of the bidisk, and it is not a torus point')
        note('R1 verdict: by DOM with delta = 2/C uniform over the orbit, no member of the closure of Resp(R1) under the '
             'full automorphism group O(2) x O(2) x swap, mixing, ontic operations and limits is a proper effect certain at '
             '(e1, 0); the same holds at every point of the flat faces off the torus; the bidisk is drivable '
             '(Thread F CM-RSC), so the G-closed response family fails SEC on a drivable body')
    else:
        face = [sp.simplify(pi.subs({x1: 1, x2: 0})) for pi in p]
        chk('R2: p_1 vanishes on the whole flat face {e1} x D (facet on the face)', zero(face[0]), 'identity')
        # pulled back by the rotation (R w = e1) the facet effect 1 - p_1 is certain at (w, y)
        cw, sw = sp.Rational(3, 5), sp.Rational(4, 5)
        # rotation taking w=(cw,sw) to e1: [[cw, sw],[-sw, cw]]
        xr1 = cw * x1 + sw * x2
        xr2 = -sw * x1 + cw * x2
        pulled = 1 - p[0].subs({x1: xr1, x2: xr2}, simultaneous=True)
        val = pulled.subs({x1: cw, x2: sw, y1: sp.Rational(1, 3), y2: -sp.Rational(1, 2)})
        prop = pulled.subs({x1: -cw, x2: -sw, y1: 0, y2: 0})
        chk('R2: 1 - p_1 o g is certain at the flat-face point ((3/5,4/5),(1/3,-1/2)) and proper (value %s at -w)' % prop,
            zero(val - 1) and sp.simplify(prop - 1) < 0, 'witness')
        note('R2 verdict: rotations carry {e1} x D onto every face {w} x D and the swap onto D x {w}; these cover the '
             'relative boundary of D x D, so the G-closed Resp(R2) is SEC-complete. R1 and R2 realize the same body with '
             'the same automorphism group: the candidate depends on the realization')

# ================================================================== STG
section('STG  a finite stage (triangle) with the operational closure conv{0, 1, a, 1-a, b, 1-b}')
verts = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(1, 2), Fr(1))]
m = (Fr(3, 4), Fr(1, 2))
gens = {'a': lambda v: v[0], '1-a': lambda v: 1 - v[0], 'b': lambda v: v[1], '1-b': lambda v: 1 - v[1],
        '0': lambda v: Fr(0)}
chk('stage table in [0,1]: every generator takes values in [0,1] at the three preparations',
    all(0 <= g(v) <= 1 for g in gens.values() for v in verts), 'enumerate')
chk('m = (3/4, 1/2) is the midpoint of the edge from (1,0) to (1/2,1): a boundary state of the triangle',
    m == ((verts[1][0] + verts[2][0]) / 2, (verts[1][1] + verts[2][1]) / 2), 'witness')
ratios = []
for nm, g in gens.items():
    num = 1 - g(m)
    den = max(1 - g(v) for v in verts)
    ratios.append(num / den)
dlt = min(ratios)
chk('delta = min over non-unit generators of (1 - h(m)) / max_vertices (1 - h) = %s > 0' % dlt, dlt == Fr(1, 4), 'enumerate')
note('the domination inequality holds for each generator with delta = 1/4 and the unit satisfies it trivially, so it '
     'holds on the convex hull (which is compact): no proper effect of the closure is certain at m')
f = lambda v: (2 * v[0] + v[1]) / 2
chk('mutation: the no-restriction effect (2a + b)/2 is in [0,1] on the stage, certain at m, proper',
    all(0 <= f(v) <= 1 for v in verts) and f(m) == 1 and f(verts[0]) < 1, 'mutation')
chk('(2a + b)/2 violates the domination inequality (1/4)(1 - f(z)) <= 1 - f(m) at z = (0,0), so it is not in the closure',
    Fr(1, 4) * (1 - f(verts[0])) > 1 - f(m), 'deduce')
note('the triangle is a polytope, so no drive exists on it (Thread F B5) and KInf1 is vacuous there; the control shows '
     'that the GPT-standard closure of a finite stage table is not SEC-complete even on its own body')

# ================================================================== MAT
section('MAT  matrix regime on the qubit: substratum (monomial) operations and the Naimark circuit')
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
paulis = [X, Y, Z]


def bloch_rot(Um):
    return sp.Matrix(3, 3, lambda i, j: sp.simplify((paulis[i] * Um * paulis[j] * Um.H).trace() / 2))


ph = (sp.Rational(3, 5) + sp.I * sp.Rational(4, 5))
mono = [sp.diag(1, ph), X * sp.diag(1, ph), sp.diag(ph, 1) * X, X]
ok_axis = True
for Um in mono:
    Rb = bloch_rot(Um)
    e3img = Rb * sp.Matrix([0, 0, 1])
    ok_axis &= (zero(e3img[0]) and zero(e3img[1]) and zero(abs(e3img[2]) - 1))
chk('monomial unitaries (phases, swap, products) map the Bloch z-axis to +-z-axis (4 instances)', ok_axis, 'enumerate')
th = sp.Symbol('theta', real=True)
Rz = sp.Matrix([[sp.cos(th), -sp.sin(th), 0], [sp.sin(th), sp.cos(th), 0], [0, 0, 1]])
RX = bloch_rot(X)
chk('swap conjugates the z-rotation flow to its inverse: R_X R_z(t) R_X^-1 = R_z(-t)',
    all(zero(e) for e in (RX * Rz * RX.T - Rz.subs(th, -th))), 'identity')
note('every monomial unitary normalizes the z-rotation group on the Bloch ball, so no monomial J satisfies J_off_axis '
     '(KF:276): the substratum class does not drive the Bloch ball in KF terms, matching substratum_residual (SC:383)')
# diagonal effects of monomial Kraus families
Kd = sp.diag(sp.Rational(1, 2), ph * sp.Rational(1, 3))
E = (X * Kd).H * (X * Kd)
chk('a monomial Kraus operator K gives the diagonal effect K^dagger K', zero(E[0, 1]) and zero(E[1, 0]), 'witness')
note('realized_of_instAvail (IL:530) writes every branch of a substratum-generated family as a sum of conjugations by '
     'monomials (block and product closures: StructuralClosure); its effect sum K^dagger K is diagonal, i.e. a response '
     'function on the two configurations; on the ball it is (a+b)/2 + (a-b) z/2, certain only at the poles')


def kron(A, B):
    return sp.kronecker_product(A, B)


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
P0 = sp.Matrix([[1, 0], [0, 0]])
P1 = sp.Matrix([[0, 0], [0, 1]])


def cayley(Hm):
    return (sp.eye(2) + sp.I * Hm) * (sp.eye(2) - sp.I * Hm).inv()


Vc = sp.simplify(cayley(sp.Matrix([[sp.Rational(1, 3), sp.Rational(1, 2) - sp.I / 5], [sp.Rational(1, 2) + sp.I / 5, -1]])))
chk('V (Cayley transform of a Hermitian Gaussian-rational matrix) is unitary', all(zero(e) for e in (Vc.H * Vc - I2)),
    'identity')
r_ = sp.symbols('r0:4')
rho = sp.Matrix([[r_[0], r_[1] + sp.I * r_[2]], [r_[1] - sp.I * r_[2], r_[3]]])


def naimark_effect(Vm, k):
    W = CNOT * kron(Vm.H, I2)
    out = W * kron(rho, P0) * W.H
    Pk = P0 if k == 0 else P1
    val = (kron(I2, Pk) * out).trace()
    Ek = Vm * (P0 if k == 0 else P1) * Vm.H
    return sp.simplify(sp.expand(val - (Ek * rho).trace())), Ek


d0, E0 = naimark_effect(Vc, 0)
d1, E1 = naimark_effect(Vc, 1)
chk('Naimark circuit (attach |0>, CNOT (V^dag x 1), read ancilla k, discard): effect = V|k><k|V^dag, k = 0, 1',
    zero(d0) and zero(d1), 'identity')
chk('V|0><0|V^dag is a rank-one projector with nonzero off-diagonal (a non-pole sharp effect)',
    all(zero(e) for e in (E0 * E0 - E0)) and not zero(E0[0, 1]), 'identity')
dm, Em = naimark_effect(X * sp.diag(1, ph), 0)
chk('mutation: with a monomial V the same circuit yields a diagonal effect (a pole)', zero(dm) and zero(Em[0, 1]),
    'mutation')
note('the sharpness is supplied by the postulated native register readout (FiniteOperationalTheory.readout_avail, OA:594;'
     ' form derived by readout_is_localLuders OA:658) and transported to the system by a non-monomial (driving) '
     'operation: in the matrix regime P2 is generated from K-infinity-R, not independent of it')

# diagTheory (DiagonalTheory.lean:246) admits measure-and-prepare instruments: Kraus |0><v_k| preserve the diagonal
plus = sp.Matrix([1, 1]) / sp.sqrt(2)
minus = sp.Matrix([1, -1]) / sp.sqrt(2)
e0 = sp.Matrix([1, 0])
Ks = [e0 * plus.H, e0 * minus.H]
chk('measure-and-prepare Kraus {|0><+|, |0><-|} is trace preserving: sum K^dag K = I',
    all(zero(q) for q in (Ks[0].H * Ks[0] + Ks[1].H * Ks[1] - I2)), 'identity')
w0, w1 = sp.symbols('w0 w1')
outd = [K * sp.diag(w0, w1) * K.H for K in Ks]
chk('each branch maps diagonal inputs to diagonal outputs (PreservesDiag, DiagonalTheory.lean:68)',
    all(zero(o[0, 1]) and zero(o[1, 0]) for o in outd), 'identity')
Eplus = Ks[0].H * Ks[0]
chk('its first effect is the sharp non-diagonal |+><+| (certain at the Bloch point (1,0,0))',
    all(zero(q) for q in (Eplus - plus * plus.H)) and not zero(Eplus[0, 1]), 'identity')
note('diagTheory realizes the sealed OI core (diag_realizesSealedOICore, DiagonalTheory.lean:358) and has no composite '
     'control (diag_not_control :390), yet carries sharp effects in every direction; substratumTheory = genTheory '
     'substratumClass (RouteB.lean:279) realizes the same core (RouteB.lean:375) with diagonal effects only: the OI core '
     'does not determine the effect family, and full effects do not need a drive')

# ================================================================== NR
section('NR  the no-restriction closure on the SIC realization')
pt = [(1 + ai.dot(rv)) / 4 for ai in a]
coeffs = sp.Matrix([[sp.diff(pi, v) for v in (x, y, z)] + [pi.subs({x: 0, y: 0, z: 0})] for pi in pt])
chk('the four tight-SIC responses span all affine functionals on R^3 (rank 4)', coeffs.rank() == 4, 'identity')
n1 = a[0]
c1v = [sp.simplify((1 + 3 * n1.dot(ai)) / 2) for ai in a]
chk('the sharp effect certain at a_1 (antipode of the tangency point -a_1) is 2 p_1: coefficients %s, c_1 = 2 > 1'
    % c1v, c1v == [2, 0, 0, 0] and zero(sum(ci * pi for ci, pi in zip(c1v, pt)) - (1 + n1.dot(rv)) / 2), 'identity')
note('c_i = (1 + sqrt(3) n.s_i)/2 ranges over [-1, 2] as n runs over the unit sphere; the response box is [0,1]')
note('no-restriction (all affine maps in [0,1] on the body) gives fullEffects in the operational embedding, hence (SEC) by '
     'Thread F B8; it contains effects that are not response functions of the realization (Main.md:540), so it is not the '
     'closure of anything the realization implements (ONT)')

# ================================================================== summary
print()
if FAIL:
    print('g_controls: FAIL -- %d of %d checks failed: %s' % (len(FAIL), COUNT[0], FAIL))
    sys.exit(1)
print('g_controls: OK -- %d checks, %d written notes' % (COUNT[0], len(NOTES)))
