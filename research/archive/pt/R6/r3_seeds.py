# r3_seeds.py -- R6 node R3: exact checks of the EXOTIC-E seeds of stages 4 and 5 (existence alternatives).
# DECISION RULE (fixed before the first run, 18:21:03Z by date -u):
#  An EXOTIC-E alternative is a closed cone K, invariant under a compact group G-hat containing cnot, self-dual, with
#  K ⊇ cone(G-hat.SEP ∪ G-hat.e) for an exactly given seed e; existence is EBF [W, audited AUDIT-X] over the audited
#  stage-4 dichotomy (Y1 / Z claim D). This script re-checks, exactly, what each seed's record states that is cheap to
#  recompute; the overlap bound over the whole reachable set is cited [A] where it is not recomputed here.
#  Seed forms: Y-form e = table((I - c v v^dag)/8), v normalized; Z/C5-form e = alpha E00 - T_psi/4 (c = 1/alpha).
#  For every seed: S1 spectrum of pauliW(e): exactly one negative eigenvalue, (1-c)/8 resp. (alpha-1)/4, the rest positive;
#   S2 ipW(e, T_v) < 0 (so the pure state v, in Q3, is not in K = K*: K != Q3); S3 the window c <= min(2, 1/m) with
#   m = (1 + sqrt(1 - 4 d))/2 for the recorded or recomputed lower bound d of |det|^2 (normalized) over the reachable set,
#   decided by squaring with signs checked; S4 instance pairings: ipW(e, T_p) >= 0 for exact reachable states p listed per
#   seed, and ipW(e, g e) >= 0 for the listed group elements g.
#  Recomputed minima (exact): R-a the X(x)X torus form Q_psi for psi in {phi0, CNOT phi0} (det Q / tr Q, Y4 / C5 flow@C);
#   R-b min |det|^2 over the G16 orbit of phi0 (Y5's d_min, attained in G16) and over the level-(ii) orbits of
#   <J(x)I or I(x)J, CNOT, Z(x)I, I(x)Z, conj> with and without the NOT (C5's 768 / 384); R-c the Z(x)Z torus:
#   min_beta |det|^2 = (|ad| - |bc|)^2 for psi in {phi0, CNOT phi0} (C5 1/8704); R-d D5's monomial class: min |det| over
#   the 24 arrangements of (1,2,3,4)/sqrt(30); R-e Z's S3 seed: V-coefficients of psi_a and f = 1/2 + 5 sqrt(137)/162 <= 7/8;
#   R-f G_H = <G16, Ad(I(x)H)> orbit of psi_a: m = max squared token-1 Bloch length (Z: 4160/6561); R-g the kappa / S2
#   circles C1, C2: invariant under U(w), CNOT, Z(x)I, I(x)Z, conj and the S2 torus Rz(x)Rx (symbolic in a rational
#   parameter), every point maximally entangled, F = z_(-1,-1) = e_psi at psi = C1(1); R-h G_S = <G16, Ad(S(x)I)> orbit of
#   psi_F: 8 rays, all maximally entangled, off-diagonal pairings in {0, 1/8}.
#  Countercontrols (must hold as stated): a reachable state (|00>) has d = 0 and an empty window; c = 5/2 breaks orbit
#   self-positivity for the Y-form at v = phi0 with g = CNOT; (H(x)I) C1(1) leaves C1 ∪ C2; the product magnitudes
#   (1,2,2,4)/5 give min |det| = 0 in R-d.
#  VERDICT R3-SEEDS-EXACT printed only if every check passes and every countercontrol behaves as stated.
#  RUN-2 FIX (18:22:10Z, after run 1, kept as r3_seeds.run1.*, failed S4 for the Bell seed F): run 1 used one reachable
#   sample (the S3 group's: X(x)X torus) for every seed, against the rule's 'listed per seed'; the S3 torus is not in
#   the kappa/S2 group. Run 2 lists the instances per seed from that seed's own generators (no rule change).
import sympy as sp
from fractions import Fraction as Fr
from itertools import permutations

iu, Rt = sp.I, sp.Rational
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def table(A): return sp.Matrix(4, 4, lambda m, n: sp.re(sp.expand((A * SS[m][n]).trace())))
def ip(a, b): return sp.nsimplify(sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4))))
def nrm2(v): return sp.expand((sp.Matrix(v).H * sp.Matrix(v))[0])
def Tpure(v): v = sp.Matrix(v); return table(v * v.H / nrm2(v))
def det2(v): return sp.expand(v[0] * v[3] - v[1] * v[2])
def dnorm(v): return sp.nsimplify(sp.expand(sp.Abs(det2(v)) ** 2 / nrm2(v) ** 2))
P0, P1 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, s[0]) + kron(P1, s[1])
E00 = sp.zeros(4, 4); E00[0, 0] = 1
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-30s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))
def window_ok(c, d):   # c <= min(2, 1/m), m = (1+sqrt(1-4d))/2  <=>  c <= 2 and sqrt(1-4d) <= (2-c)/c
    if not (1 < c <= 2): return False
    rhs = (2 - c) / c
    return rhs >= 0 and (1 - 4 * d) <= rhs ** 2
def seedY(v, c): v = sp.Matrix(v); return table((sp.eye(4) - c * v * v.H / nrm2(v)) / 8)
def seedZ(v, alpha): return alpha * E00 - Tpure(v) / 4
def spectrum_ok(e, neg):
    ev = pW(e).eigenvals(); n = [l for l in ev if l < 0]
    return sum(ev.values()) == 4 and len(n) == 1 and ev[n[0]] == 1 and sp.simplify(n[0] - neg) == 0 and all(l > 0 for l in ev if l != n[0])
# ---- Gaussian-rational ray arithmetic for orbits
def gq(z): z = sp.nsimplify(z); return (Fr(str(sp.re(z))), Fr(str(sp.im(z))))
def gmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def gadd(a, b): return (a[0] + b[0], a[1] + b[1])
def gdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]; return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)
def gmat(M): return [[gq(M[i, j]) for j in range(4)] for i in range(4)]
def gapply(M, v):
    out = []
    for i in range(4):
        acc = (Fr(0), Fr(0))
        for j in range(4): acc = gadd(acc, gmul(M[i][j], v[j]))
        out.append(acc)
    return tuple(out)
def gconj(v): return tuple((x[0], -x[1]) for x in v)
def canon(v):
    k = next(i for i in range(4) if v[i] != (0, 0)); return tuple(gdiv(x, v[k]) for x in v)
def orbit(v0, gens, conj=True):
    seen = {canon(v0)}; todo = [canon(v0)]
    while todo:
        v = todo.pop(); imgs = [gapply(M, v) for M in gens] + ([gconj(v)] if conj else [])
        for w in imgs:
            cw = canon(w)
            if cw not in seen: seen.add(cw); todo.append(cw)
    return seen
def gdet_norm(v):
    d = gadd(gmul(v[0], v[3]), gmul((-v[1][0], -v[1][1]), v[2])); n2 = sum(x[0] * x[0] + x[1] * x[1] for x in v)
    return (d[0] * d[0] + d[1] * d[1]) / (n2 * n2)
def gvec(v): return tuple(gq(x) for x in v)

phi0 = sp.Matrix([1, 2, 3 * iu, -1 + iu])                    # |phi0|^2 = 16
cphi0 = CNOT * phi0
chk('S0 phi0 data', nrm2(phi0) == 16 and cphi0 == sp.Matrix([1, 2, -1 + iu, 3 * iu]), 'CNOT phi0 = (1, 2, -1+i, 3i)')
# ---- R-a: the X(x)X torus form (Y4; C5 flow@C, d_low = 1/2304)
cb, sb = sp.symbols('cb sb', real=True)
XX = kron(s[1], s[1])
def Qform(v):
    vp = (cb * sp.eye(4) - iu * sb * XX) * v
    D = det2(v); M = sp.expand(v[0] ** 2 + v[3] ** 2 - v[1] ** 2 - v[2] ** 2)
    ident = sp.expand(det2(vp) - ((cb ** 2 - sb ** 2) * D - iu / 2 * (2 * cb * sb) * M)) == 0
    u, w = D, -iu * M / 2
    Q = sp.Matrix([[sp.expand(u * sp.conjugate(u)), sp.re(sp.expand(u * sp.conjugate(w)))],
                   [sp.re(sp.expand(u * sp.conjugate(w))), sp.expand(w * sp.conjugate(w))]]).applyfunc(sp.nsimplify)
    return ident, Q
ratios = []
for v in (phi0, cphi0):
    ident, Q = Qform(v)
    chk('R-a identity+posdef %s' % list(v), ident and Q.det() > 0 and Q.trace() > 0, 'det Q/tr Q = %s' % (Q.det() / Q.trace()))
    ratios.append(Q.det() / Q.trace())
d_a = min(ratios) / 256
chk('R-a d_low = 1/2304', d_a == Rt(1, 2304) and sorted(ratios) == [Rt(1, 9), Rt(121, 42)], 'AUDIT-Y C1-C6: 1/9, 121/42')
SEEDS = []   # (name, table, negative eigenvalue, test vector, c, d used for the window, d provenance)
c_y4 = 1 + 4 * d_a / 8
SEEDS.append(('A3a Y4 c=4609/4608 (S3, drive)', seedY(phi0, c_y4), (1 - c_y4) / 8, phi0, c_y4, d_a, 'R-a [X]; reduction [A] Y4'))
al = Rt(499783, 500000)
SEEDS.append(('A4a C5 d_low=1/2304 (flow@C)', seedZ(phi0, al), (al - 1) / 4, phi0, 1 / al, d_a, 'R-a [X]; reduction [A] C5'))
chk('R-a seeds', c_y4 == Rt(4609, 4608) and (2 * al - 1) ** 2 >= 1 - 4 * d_a, 'c = %s; r^2 >= 1 - 4 d_low' % c_y4)
# ---- R-b: finite orbits (Y5 d_min = 5/256; C5 {J}, {NOT, J} at level (ii))
UJ = (s[0] - iu * (s[1] + s[2] + s[3])) / 2
G16g = [gmat(CNOT), gmat(kron(s[3], s[0])), gmat(kron(s[0], s[3]))]
SWAPm = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
orbs = {'G16': G16g, 'G16+SWAP': G16g + [gmat(SWAPm)], 'J@C': G16g + [gmat(kron(UJ, s[0]))],
        'J@T': G16g + [gmat(kron(s[0], UJ))], 'NOT,J@C': G16g + [gmat(kron(UJ, s[0])), gmat(kron(s[1], s[0]))],
        'NOT,J@T': G16g + [gmat(kron(s[0], UJ)), gmat(kron(s[0], s[1]))]}
sizes, mins = {}, {}
for k, gens in orbs.items():
    o = orbit(gvec(phi0), gens); sizes[k] = len(o); mins[k] = min(gdet_norm(v) for v in o)
    print('ORBIT %-9s phi0-rays %4d  min|det|^2 %s' % (k, sizes[k], mins[k]))
chk('R-b d_min = 5/256', all(m == Fr(5, 256) for m in mins.values()), 'every listed orbit')
chk('R-b orbit sizes (ii)', sizes['G16'] == 16 and {sizes['J@C'], sizes['J@T']} == {768, 384}, 'C5 level-(ii) 768 / 384')
d_b = Rt(5, 256)
SEEDS.append(('A3b Y5 c=517/512 (S1, finite)', seedY(phi0, Rt(517, 512)), (1 - Rt(517, 512)) / 8, phi0, Rt(517, 512), d_b,
              'R-b G16 orbit [X]; Clifford census [A] Y5'))
al = Rt(122509, 125000)
SEEDS.append(('A4a C5 d_low=5/256 (J, NOT+J, flow@T)', seedZ(phi0, al), (al - 1) / 4, phi0, 1 / al, d_b, 'R-b [X]'))
# ---- R-c: the Z(x)Z torus (C5 ball3Drive flow on the target, 1/8704)
def zz_min_ge(v, t):
    p = sp.nsimplify(sp.expand(sp.Abs(v[0] * v[3]) ** 2)) / 256; q = sp.nsimplify(sp.expand(sp.Abs(v[1] * v[2]) ** 2)) / 256
    lhs = p + q - t
    return lhs >= 0 and lhs ** 2 >= 4 * p * q
chk('R-c d_low = 1/8704', all(zz_min_ge(v, Rt(1, 8704)) for v in (phi0, cphi0)) and not zz_min_ge(cphi0, Rt(1, 8600)),
    'min_beta |det|^2 = (|ad|-|bc|)^2 >= 1/8704 at phi0, CNOT phi0; and < 1/8600 at CNOT phi0 (sharpness)')
c_c = Rt(17409, 17408)
SEEDS.append(('A4a C5 d_low=1/8704 (ball3Drive@T)', seedY(phi0, c_c), (1 - c_c) / 8, phi0, c_c, Rt(1, 8704), 'R-c [X]; reduction [A]'))
# ---- R-d: D5's monomial class
mags = [1, 2, 3, 4]
dmin = min(abs(p[0] * p[3] - p[1] * p[2]) for p in permutations(mags))
cc_d = min(abs(p[0] * p[3] - p[1] * p[2]) for p in permutations([1, 2, 2, 4]))
chk('R-d min|det| = 1/15', Rt(dmin, 30) == Rt(1, 15) and cc_d == 0, 'countercontrol (1,2,2,4): 0')
m4 = sp.Matrix([1, 2, 3, 4]); c_d = Rt(513, 512)
SEEDS.append(('A4c D5 c=513/512 (monomial class)', seedY(m4, c_d), (1 - c_d) / 8, m4, c_d, Rt(1, 225), 'R-d [X]; [W] arrangement bound [A] D5'))
# ---- R-e: Z's S3 seed psi_a, and R-f: G_H
psa = sp.Matrix([15, -1, 7, 7])
Hn = (s[1] + s[3]) / sp.sqrt(2)
V = (kron(Hn, Hn) * psa / 18).applyfunc(sp.nsimplify)
chk('R-e V-coefficients', list(V) == [Rt(7, 9), Rt(4, 9), 0, Rt(4, 9)], '%s' % list(V))
f2 = 1 - 4 * (Rt(28, 81)) ** 2
chk('R-e f <= 7/8', f2 == Rt(3425, 6561) and (2 * Rt(7, 8) - 1) ** 2 >= f2, 'f = 1/2 + sqrt(3425)/162 = 1/2 + 5 sqrt(137)/162')
SEEDS.append(('A3c Z alpha=7/8 (S3)', seedZ(psa, Rt(7, 8)), (Rt(7, 8) - 1) / 4, psa, Rt(8, 7), (1 - f2) / 4, 'R-e [X]; reachable-set formula [A] Z z3'))
GH = G16g + [gmat(kron(s[0], s[1] + s[3]))]
oH = orbit(gvec(psa), GH); mH = max(1 - 4 * gdet_norm(v) for v in oH)
chk('R-f G_H m = 4160/6561', mH == Fr(4160, 6561) and (2 * Rt(9, 10) - 1) ** 2 >= Rt(4160, 6561), 'rays %d' % len(oH))
SEEDS.append(('A5 G_H alpha=9/10', seedZ(psa, Rt(9, 10)), (Rt(9, 10) - 1) / 4, psa, Rt(10, 9), (1 - Rt(4160, 6561)) / 4, 'R-f [X]'))
chk('R-f G_Cl window', (2 * Rt(99, 100) - 1) ** 2 >= Rt(6272, 6561), 'm = 6272/6561 [A] Z z4 (not recomputed)')
SEEDS.append(('A5 G_Cl alpha=99/100', seedZ(psa, Rt(99, 100)), (Rt(99, 100) - 1) / 4, psa, Rt(100, 99), (1 - Rt(6272, 6561)) / 4, '[A] Z z4'))
# ---- R-g: the kappa / S2 circles
t, t0, t1, t2 = sp.symbols('t t0 t1 t2', real=True)
def unit(x): return (1 - x ** 2 + 2 * iu * x) / (1 + x ** 2)
w, w0 = unit(t), unit(t0)
C1 = lambda z: sp.Matrix([1, 1, z, -z]); C2 = lambda z: sp.Matrix([1, -1, z, z])
def on_circles(v):
    v = v / v[0]; v = v.applyfunc(lambda x: sp.simplify(x))
    for sgn, pat in ((1, C1), (-1, C2)):
        if sp.simplify(v[1] - sgn) == 0:
            z = v[2]
            return sp.simplify(pat(z) - v) == sp.zeros(4, 1) and sp.simplify(z * sp.conjugate(z) - 1) == 0
    return False
k1m = sp.Matrix([0, 0, 1, -1]) / sp.sqrt(2)
Uw = sp.eye(4) + (w0 - 1) * k1m * k1m.H
Rz = sp.diag(1, unit(t1)); a_, b_ = (1 - t2 ** 2) / (1 + t2 ** 2), 2 * t2 / (1 + t2 ** 2)
Rx = a_ * s[0] - iu * b_ * s[1]
gens_c = [('U(w0)', Uw), ('CNOT', CNOT), ('Z(x)I', kron(s[3], s[0])), ('I(x)Z', kron(s[0], s[3])), ('Rz(x)Rx torus', kron(Rz, Rx))]
okg = all(on_circles(g * C(w)) for _, g in gens_c for C in (C1, C2)) and all(on_circles(C(w).conjugate()) for C in (C1, C2))
chk('R-g circles invariant', okg, 'U(w), CNOT, Z(x)I, I(x)Z, conj, actC Rz o actT Rx (symbolic)')
okm = all(sp.simplify(sp.Abs(det2(C(w))) ** 2 / nrm2(C(w)) ** 2 - Rt(1, 4)) == 0 for C in (C1, C2))
chk('R-g maximally entangled', okm, '|det|^2 = 1/4 on both circles')
psiF = C1(1) / 2
eF = E00 / 2 - Tpure(psiF) / 4
zF = (E00 - sp.Matrix(4, 4, lambda m, n: 1 if (m, n) in [(1, 3), (2, 2), (3, 1)] else 0)) / 4
chk('R-g F = z_(-1,-1)', eF == zF, 'Bell seed at C1(1)')
chk('R-g cc (H(x)I)C1(1) leaves', not on_circles(kron(s[1] + s[3], s[0]) * C1(1)), 'non-vacuity')
SEEDS.append(('A4b kappa / A5 S2 Bell seed F', eF, Rt(-1, 8), psiF, 2, Rt(1, 4), 'R-g [X]; EBF [A]'))
# ---- R-h: G_S
GS = G16g + [gmat(sp.diag(1, 1, iu, iu))]          # S(x)I with S = diag(1, i)
oS = orbit(gvec(C1(1)), GS)
ent = all(gdet_norm(v) == Fr(1, 4) for v in oS)
vs = [sp.Matrix([sp.Rational(x[0].numerator, x[0].denominator) + iu * sp.Rational(x[1].numerator, x[1].denominator) for x in v]) for v in oS]
ovl = set()
for i in range(len(vs)):
    for j in range(i + 1, len(vs)):
        ovl.add(sp.nsimplify(sp.Abs((vs[i].H * vs[j])[0]) ** 2 / (nrm2(vs[i]) * nrm2(vs[j]))))
chk('R-h G_S orbit', len(oS) == 8 and ent and ovl <= {0, Rt(1, 2)}, '8 rays, maximally entangled, overlaps %s (pairings in {0, 1/8})' % sorted(ovl))
# ---- per-seed checks S1-S4
loc = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([1, 1]), sp.Matrix([1, -1]), sp.Matrix([1, iu]), sp.Matrix([1, -iu])]
prods = [kron(a, sp.eye(2)) * sp.Matrix([b[0], b[1], 0, 0]) if False else sp.Matrix([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]) for a in loc for b in loc]
Tb = Rt(3, 5) * sp.eye(4) - iu * Rt(4, 5) * XX
Ta = Rt(3, 5) * sp.eye(4) - iu * Rt(4, 5) * kron(s[1], s[0])
Hd = s[1] + s[3]
Uw0 = sp.eye(4) + (Rt(3, 5) + iu * Rt(4, 5) - 1) * k1m * k1m.H
Tzz = Rt(3, 5) * sp.eye(4) - iu * Rt(4, 5) * kron(s[3], s[3])
perms = [sp.Matrix(4, 4, lambda i, j: 1 if q[j] == i else 0) for q in permutations(range(4))]
base = prods + [CNOT * p for p in prods]
REACH = {
  'S3': base + [Tb * p for p in base] + [Ta * Tb * p for p in base],
  'G16cl': base + [CNOT * kron(Hd, s[0]) * CNOT * p for p in prods] + [CNOT * kron(s[0], Hd) * CNOT * p for p in prods],
  'J': base + [kron(UJ, s[0]) * CNOT * p for p in prods] + [CNOT * kron(UJ, s[0]) * CNOT * p for p in prods]
        + [kron(s[0], UJ) * CNOT * p for p in prods] + [CNOT * kron(s[0], UJ) * CNOT * p for p in prods],
  'ZZ': base + [Tzz * p for p in base],
  'mono': [P * p for P in perms for p in prods[:12]],
  'GH': base + [kron(s[0], Hd) * CNOT * p for p in prods] + [CNOT * kron(s[0], Hd) * CNOT * p for p in prods],
  'kappa': base + [Uw0 * p for p in base] + [CNOT * Uw0 * p for p in prods],
}
GROUP = {'A3a': 'S3', 'A4a C5 d_low=1/2304': 'S3', 'A3b': 'G16cl', 'A4a C5 d_low=5/256': 'J', 'A4a C5 d_low=1/8704': 'ZZ',
         'A4c': 'mono', 'A3c': 'S3', 'A5 G_H': 'GH', 'A5 G_Cl': 'G16cl', 'A4b': 'kappa'}
def group_of(name): return next(v for k, v in GROUP.items() if name.startswith(k))
for name, e, neg, v, c, d, prov in SEEDS:
    s1 = spectrum_ok(e, neg)
    s2 = ip(e, Tpure(v)) < 0
    s3 = window_ok(c, d)
    reach = REACH[group_of(name)]
    s4 = all(ip(e, Tpure(p)) >= 0 for p in reach) and ip(e, table(CNOT * pW(e) * CNOT.H)) >= 0
    chk('S %s' % name, s1 and s2 and s3 and s4, 'neg eig %s; <e,T_v> = %s; window c=%s; %d reachable instances (%s); %s'
        % (neg, ip(e, Tpure(v)), c, len(reach), group_of(name), prov))
# ---- countercontrols
chk('CC reachable |00> no seed', not window_ok(Rt(1025, 1024), 0), 'd = 0: m = 1, the window (1, 1] is empty')
vA, vB = sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 0, 0])
chk('CC c = 5/2 breaks orbit', ip(seedY(vA, Rt(5, 2)), seedY(vB, Rt(5, 2))) < 0 and ip(seedY(vA, 2), seedY(vB, 2)) == 0,
    'orthogonal seeds pair (4 - 2c)/16: -1/16 at c = 5/2, 0 at c = 2')
bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
if not bad:
    print('VERDICT R3-SEEDS-EXACT: every listed seed has one negative eigenvalue, excludes its own pure state, lies in its '
          'window for the recomputed or recorded overlap bound, and pairs >= 0 with the listed reachable instances; '
          'recomputed: X(x)X form 1/9 and 121/42, G16 and J-orbit minima 5/256 (768 / 384), Z(x)Z bound 1/8704, monomial 1/15, '
          'psi_a f-bound, G_H m = 4160/6561, the invariant circles, G_S orbit 8; controls green')
else:
    print('NO VERDICT')
