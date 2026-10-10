# c4_bell_family.py -- research/countermodels node C4: the classification of the Bell-type defect cones.
# Class: K(Z) = (Q3 ∩ Z*) + cone Z for a finite set Z of Bell-type defects z_g = E00/2 - T_g/4 (pauliW(z_g) = (I - 2 gg^dag)/8,
# g maximally entangled, T_g its pure table). Conventions as in c1_cones.py.
# DECISION RULE (fixed before the first run, 2026-10-10T20:50:49Z by date -u):
#  B1 (cnot closure): for a maximally entangled table T = E00 + sum C_ij E_ij (C in O(3), det C = -1), the local entries of
#     cnot T are +-C_32, C_33 (row 0) and C_11, C_21 (column 0) (symbolic); hence cnot T_g is a maximally entangled table
#     iff C_11 = C_21 = C_32 = C_33 = 0. Every point of the circles C1(w) = (|0+> + w|1->)/sqrt2, C2(w) = (|0-> + w|1+>)/sqrt2,
#     w = ((1 - t^2) + 2it)/(1 + t^2) (and w = -1), has this form (symbolic in t), and conversely the form leaves exactly
#     these circles: C = [[0, a, b], [0, c, d], [e, 0, 0]] with [[a, b], [c, d]] orthogonal and e det = -1 is a 2-circle
#     family; checked by matching T_{C1(w)}, T_{C2(w)} with that form for both signs of e and both determinants.
#  B2 (group action on the circles, symbolic in t): cnot C1(w) = C1(-w), cnot C2(w) = C2(w); Ad(Z(x)I): Ck(w) -> Ck(-w);
#     Ad(I(x)Z): C1(w) <-> C2(w); transpose: w -> conj(w); SWAP and Ad(S(x)I) (S = diag(1, i)): Ad(S(x)I) Ck(w) = Ck(iw).
#     (as rays of the pure tables).
#  B3 (orthogonality, symbolic): |<C1(w)|C1(w')>|^2 = |1 + conj(w) w'|^2/4, the same on C2, and C1 ⊥ C2 always.
#  B4 (pair theorem, exact instances beyond stage 4's range): for two Bell-type defects at squared overlap c in
#     {16/25, 3/4, 9/10} (c >= 1/2, where stage 4 claimed nothing), an explicit y = T_v + lam z_2 with v in the open cap of
#     z_1 and outside the closed cap of z_2, lam = -ipW(T_v, z_1)/ipW(z_1, z_2) > 0: y pairs >= 0 with both defects (so y is
#     in K*) and pauliW(y) is not PSD (so y is not in K, by the written argument of NOTES-C4 W1). Control: for an orthogonal
#     pair the same construction is unavailable (ipW(z_1, z_2) = 0).
#  B5 (level (ii)): among w in {1, i, -1, -i} and five further rational points of the circle, the G16-orbit of C1(w) is
#     an orthonormal set of four maximally entangled vectors iff w in {+-1, +-i}; Z_F = orbit of w = 1, Z_Y = orbit of w = i.
#     For Z_Y: H1 (SOS as in c1_cones C1), G16-invariance, the SD certificates, orthogonality, Z_Y != Z_F, K(Z_Y) =
#     Ad(S(x)I) K(Z_F) (Ad(S(x)I) maps Z_F onto Z_Y and Q3 onto Q3), SWAP does not preserve Z_Y (it maps a member to a
#     non-member, so SWAP moves K(Z_Y) since the non-PSD extreme rays of K(Z) are exactly Z), and Ad(S(x)I) normalizes G16
#     (conjugates each generator into the 16-element group, as 16 x 16 matrices on tables).
#  B6 (level (i) family): for t, t' rational, Z = {C1(w), C1(-w)} ∪ {C2(w'), C2(-w')} (and its sub-cases) is cnot-invariant
#     and orthonormal; the C2 part is fixed pointwise by the gate flow U(x) = I + (x - 1)|1-><1-| (symbolic |x| = 1 via a
#     rational point), the C1 part is not (record for C5).
#  COUNTERCONTROLS: CC1 a maximally entangled vector off the circles (Phi+) has a non-maximally-entangled cnot image;
#  CC2 w = (3 + 4i)/5 gives a G16-orbit that is not orthogonal; CC3 the pair construction at c = 0 (orthogonal) has
#  ipW(z_1, z_2) = 0 (no lam).
#  VERDICT C4-BELL-FAMILY-EXACT iff B1-B6 pass and the countercontrols fail as stated.
import sympy as sp
from itertools import product

iu, Rt = sp.I, sp.Rational
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
SSP = [[[(i, j, SS[m][n][j, i]) for i in range(4) for j in range(4) if SS[m][n][j, i] != 0] for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def table(A):
    t = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(A[i, j] * v for i, j, v in SSP[m][n])))
    assert all(sp.simplify(sp.im(x)) == 0 for x in t), 'non-real table'
    return t.applyfunc(lambda x: sp.simplify(sp.re(x)))
def ip(a, b): return sp.simplify(sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4))))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def hom(x): return sp.Matrix([1] + list(x))
def prod(x, y): return hom(x) * hom(y).T
def Tpure(v):
    v = sp.Matrix(v); return table(v * v.H / sp.simplify((v.H * v)[0]))
def zdef(v): return E(0, 0) / 2 - Tpure(v) / 4
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return sp.Matrix(4, 4, lambda m, n: SGN(m, n) * w[PC[m][n], PT[m][n]])
def transposeW(w): return sp.Matrix(4, 4, lambda m, n: (-1 if m == 2 else 1) * (-1 if n == 2 else 1) * w[m, n])
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-34s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))
ket = {'0': sp.Matrix([1, 0]), '1': sp.Matrix([0, 1])}
ket['+'] = (ket['0'] + ket['1']) / sp.sqrt(2); ket['-'] = (ket['0'] - ket['1']) / sp.sqrt(2)
def k2(a, b): return sp.Matrix(sp.kronecker_product(ket[a], ket[b]))
def C1(w): return (k2('0', '+') + w * k2('1', '-')) / sp.sqrt(2)
def C2(w): return (k2('0', '-') + w * k2('1', '+')) / sp.sqrt(2)
def maxent(v):  # |v00 v11 - v01 v10| = 1/2 for a unit vector
    v = sp.Matrix(v); nrm = sp.simplify((v.H * v)[0])
    d = v[0] * v[3] - v[1] * v[2]
    return sp.simplify(d * sp.conjugate(d) / nrm ** 2) == Rt(1, 4)
def same_ray(a, b): return sp.simplify(sp.expand(Tpure(a) - Tpure(b))) == sp.zeros(4, 4)
tt = sp.Symbol('t', real=True)
wt = ((1 - tt ** 2) + 2 * iu * tt) / (1 + tt ** 2)

CNOTm = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
# B1
Cs = sp.Matrix(3, 3, sp.symbols('c11 c12 c13 c21 c22 c23 c31 c32 c33', real=True))
Tg = sp.zeros(4, 4); Tg[0, 0] = 1; Tg[1:, 1:] = Cs
cT = cnot(Tg)
locs = {(0, 2): cT[0, 2], (0, 3): cT[0, 3], (1, 0): cT[1, 0], (2, 0): cT[2, 0], (0, 1): cT[0, 1], (3, 0): cT[3, 0]}
b1a = (sp.expand(cT[0, 2] ** 2) == Cs[2, 1] ** 2 and cT[0, 3] == Cs[2, 2] and cT[1, 0] == Cs[0, 0] and cT[2, 0] == Cs[1, 0]
       and cT[0, 1] == 0 and cT[3, 0] == 0)
ok_form = True
for f in (C1, C2):
    T = Tpure(f(wt))
    ok_form &= all(sp.simplify(T[k, 0]) == 0 and sp.simplify(T[0, k]) == 0 for k in (1, 2, 3))
    ok_form &= all(sp.simplify(T[a, b]) == 0 for a, b in [(1, 1), (2, 1), (3, 2), (3, 3)])
    ok_form &= maxent(f(wt)) and maxent(CNOTm * f(wt))
# converse: the form C = [[0, a, b], [0, c, d], [e, 0, 0]], orthogonal, det C = -1: e = +-1, [[a,b],[c,d]] in O(2) with
# e det = -1; parametrize [[a, b], [c, d]] = [[x, -s y], [y, s x]] (x^2 + y^2 = 1, s = +-1) and match with T_{C1}, T_{C2}
xs, ys = (1 - tt ** 2) / (1 + tt ** 2), 2 * tt / (1 + tt ** 2)
conv = True
for e_, s_ in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    if e_ * s_ != -1: continue
    Cf = sp.Matrix([[0, xs, -s_ * ys], [0, ys, s_ * xs], [e_, 0, 0]])
    Tf = sp.zeros(4, 4); Tf[0, 0] = 1; Tf[1:, 1:] = Cf
    # find w on C1 or C2 with the same table: compare with the symbolic tables at w = wt and w = -wt, conj
    hit = False
    for f in (C1, C2):
        for wcand in (wt, -wt, sp.conjugate(wt), -sp.conjugate(wt), iu * wt, -iu * wt, iu * sp.conjugate(wt), -iu * sp.conjugate(wt)):
            if sp.simplify(sp.expand(Tpure(f(wcand)) - Tf)) == sp.zeros(4, 4): hit = True; break
        if hit: break
    conv &= hit
chk('B1 cnot keeps Bell-type iff on C1 ∪ C2', b1a and ok_form and conv,
    'local entries of cnot T: (C32, C33; C11, C21); C1, C2 tables have the vanishing pattern; the pattern family = C1 ∪ C2')
v_phi = (k2('0', '0') + k2('1', '1')) / sp.sqrt(2)
cc1 = maxent(v_phi) and not maxent(sp.Matrix([v_phi[0], v_phi[1], v_phi[3], v_phi[2]]))   # CNOT permutes |10>,|11>
RES['CC1 Phi+ image not max-entangled'] = cc1
print('COUNTERCONTROL CC1 Phi+ is maximally entangled, CNOT Phi+ is a product: %s' % cc1)

# B2
ZI, IZ = kron(s[3], s[0]), kron(s[0], s[3])
SI = kron(sp.diag(1, iu), s[0])
SWAPm = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
b2 = (same_ray(CNOTm * C1(wt), C1(-wt)) and same_ray(CNOTm * C2(wt), C2(wt)) and same_ray(ZI * C1(wt), C1(-wt)) and
      same_ray(ZI * C2(wt), C2(-wt)) and same_ray(IZ * C1(wt), C2(wt)) and same_ray(IZ * C2(wt), C1(wt)) and
      same_ray(C1(wt).conjugate(), C1(sp.conjugate(wt))) and same_ray(C2(wt).conjugate(), C2(sp.conjugate(wt))) and
      same_ray(SI * C1(wt), C1(iu * wt)) and same_ray(SI * C2(wt), C2(iu * wt)))
chk('B2 group action on the circles', b2, 'cnot: C1(w)->C1(-w), C2 fixed; ZI: w->-w; IZ: C1<->C2; T: w->conj w; S(x)I: w->iw')
# B3
w2 = sp.Symbol('u', real=True); wu = ((1 - w2 ** 2) + 2 * iu * w2) / (1 + w2 ** 2)
o11 = sp.simplify((C1(wt).H * C1(wu))[0] * sp.conjugate((C1(wt).H * C1(wu))[0]) - (1 + sp.conjugate(wt) * wu) * sp.conjugate(1 + sp.conjugate(wt) * wu) / 4)
o22 = sp.simplify((C2(wt).H * C2(wu))[0] * sp.conjugate((C2(wt).H * C2(wu))[0]) - (1 + sp.conjugate(wt) * wu) * sp.conjugate(1 + sp.conjugate(wt) * wu) / 4)
o12 = sp.simplify((C1(wt).H * C2(wu))[0])
chk('B3 orthogonality on the circles', o11 == 0 and o22 == 0 and o12 == 0, '|<Ck(w)|Ck(w\')>|^2 = |1 + conj(w) w\'|^2/4; C1 ⊥ C2')

# B4 pair theorem instances (c >= 1/2)
okb4 = True; notes = []
for cval in [Rt(16, 25), Rt(3, 4), Rt(9, 10)]:
    # g1 = C1(1); g2 = C1(w2) on the same circle with |1 + w2|^2/4 = c: w2 = x + iy, x = 2c - 1 (both maximally entangled)
    x = 2 * cval - 1; y = sp.sqrt(1 - x ** 2)
    g2 = C1(x + iu * y)
    g1 = C1(1)
    cc = sp.simplify(((g1.H * g2)[0]) * sp.conjugate((g1.H * g2)[0]))
    z1, z2 = zdef(g1), zdef(g2)
    # v: in the open cap of z1 (|<g1|v>|^2 > 1/2), outside the closed cap of z2 (|<g2|v>|^2 < 1/2):
    # u ⊥ g1, u ⊥ (g2 - <g1|g2> g1); v = (1 + d) g1 + u, d > 0 small enough
    r = g2 - ((g1.H * g2)[0]) * g1
    basis = [k2('0', '-'), k2('1', '+')]          # C2 directions, orthogonal to C1(w) for all w
    u = basis[0]
    best = None
    for dd in [Rt(1, 4), Rt(1, 8), Rt(1, 16)]:
        v = (1 + dd) * g1 + u
        nv = sp.simplify((v.H * v)[0])
        o1 = sp.simplify(((g1.H * v)[0]) * sp.conjugate((g1.H * v)[0]) / nv)
        o2 = sp.simplify(((g2.H * v)[0]) * sp.conjugate((g2.H * v)[0]) / nv)
        if o1 > Rt(1, 2) and o2 < Rt(1, 2): best = (dd, v); break
    if best is None:
        okb4 = False; notes.append('c=%s no v' % cval); continue
    v = best[1]; Tv = Tpure(v)
    p12 = ip(z1, z2)
    lam = sp.simplify(-ip(Tv, z1) / p12)
    y = Tv + lam * z2
    inKstar = sp.simplify(ip(y, z1)) >= 0 and sp.simplify(ip(y, z2)) >= 0 and lam > 0
    up = g2 - ((v.H * g2)[0] / (v.H * v)[0]) * v          # the projection of g2 on v^perp: a negative direction of pauliW(y)
    neg = sp.simplify((up.H * pW(y) * up)[0])
    notpsd = sp.simplify(sp.im(neg)) == 0 and sp.simplify(sp.re(neg)) < 0
    okb4 &= bool(sp.simplify(cc - cval) == 0 and p12 > 0 and inKstar and notpsd)
    notes.append('c=%s: lam=%s, ipW(y,z1)=%s, ipW(y,z2)=%s, u^dag pauliW(y) u=%s' % (cval, sp.nsimplify(lam), sp.simplify(ip(y, z1)), sp.nsimplify(sp.simplify(ip(y, z2))), sp.nsimplify(sp.re(neg))))
chk('B4 pair theorem instances (c >= 1/2)', okb4, '; '.join(notes))
cc3 = ip(zdef(C1(1)), zdef(C1(-1))) == 0
RES['CC3 orthogonal pair has no lam'] = cc3
print('COUNTERCONTROL CC3 ipW(z_C1(1), z_C1(-1)) = %s (orthogonal: the construction is unavailable)' % ip(zdef(C1(1)), zdef(C1(-1))))

# B5 level (ii)
def g16_orbit(w):
    pts = []
    for f in (C1, C2):
        for ww in (w, -w, sp.conjugate(w), -sp.conjugate(w)):
            v = f(ww)
            if not any(same_ray(v, q) for q in pts): pts.append(v)
    return pts
def orthonormal(pts):
    return all(sp.simplify((pts[i].H * pts[j])[0]) == 0 for i in range(len(pts)) for j in range(len(pts)) if i != j)
res5 = {}
for w in [1, iu, -1, -iu, Rt(3, 5) + Rt(4, 5) * iu, Rt(5, 13) + Rt(12, 13) * iu, Rt(-3, 5) + Rt(4, 5) * iu, Rt(8, 17) + Rt(15, 17) * iu, Rt(7, 25) - Rt(24, 25) * iu]:
    orb = g16_orbit(w)
    res5[str(w)] = (len(orb), orthonormal(orb))
ok5a = all((v[0] == 4 and v[1]) == (k in ('1', 'I', '-1', '-I')) for k, v in res5.items())
print('B5 G16-orbits on the circles (size, orthonormal): %s' % res5)
ZFv = g16_orbit(1); ZYv = g16_orbit(iu)
ZF = [zdef(v) for v in ZFv]; ZY = [zdef(v) for v in ZYv]
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
ZFk = [zs(a, b) for a, b in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
def setEq(A, B): return len(A) == len(B) and all(any(sp.simplify(a - b) == sp.zeros(4, 4) for b in B) for a in A)
sameZF = setEq(ZF, ZFk)
xs_, ys_ = sp.symbols('x1:4', real=True), sp.symbols('y1:4', real=True)
def H1ok(z):
    v = sp.expand(ip(z, prod(xs_, ys_)))
    M = sp.Matrix(3, 3, lambda i, j: sp.expand(v.coeff(xs_[i]).coeff(ys_[j])))
    c0 = sp.expand(v.subs({**{x: 0 for x in xs_}, **{y: 0 for y in ys_}}))
    Q = sp.eye(3) - M.T * M / c0 ** 2
    X, Y = sp.Matrix(xs_), sp.Matrix(ys_)
    sos = ((X + (M / c0) * Y).T * (X + (M / c0) * Y))[0] + (Y.T * Q * Y)[0] + (1 - (X.T * X)[0]) + (1 - (Y.T * Y)[0])
    return c0 > 0 and min(Q.eigenvals()) >= 0 and sp.expand(2 * v / c0 - sos) == 0
RzPi = sp.diag(-1, -1, 1)
def Hom(N):
    H = sp.eye(4); H[1:, 1:] = N; return H
g16maps = [cnot, lambda w: Hom(RzPi) * w, lambda w: w * Hom(RzPi).T, transposeW]
cert = all(sorted(pW(z).eigenvals().items()) == [(Rt(-1, 8), 1), (Rt(1, 8), 3)] for z in ZY)
orthZ = all(ip(ZY[i], ZY[j]) == 0 for i in range(4) for j in range(4) if i != j)
invY = all(setEq([g(z) for z in ZY], ZY) for g in g16maps)
def adS(w): return table(SI * pW(w) * SI.H)
mapS = setEq([adS(z) for z in ZFk], ZY)
basis = [E(m, n) for m in range(4) for n in range(4)]
def matof(f): return sp.Matrix(16, 16, lambda i, j: f(basis[j])[i // 4, i % 4])
Gm = [matof(g) for g in g16maps]
G16set = {sp.ImmutableMatrix(sp.eye(16))}; fr = [sp.eye(16)]
while fr:
    nf = []
    for A in fr:
        for B in Gm:
            Cm = sp.ImmutableMatrix(B * A)
            if Cm not in G16set: G16set.add(Cm); nf.append(Cm)
    fr = nf
MS = matof(adS); MSi = MS.inv()
normal = len(G16set) == 16 and all(sp.ImmutableMatrix(MS * A * MSi) in G16set for A in Gm)
swapY = setEq([z.T for z in ZY], ZY)
distinct = not setEq(ZY, ZFk)
chk('B5 level (ii) classification', ok5a and sameZF and all(H1ok(z) for z in ZY) and cert and orthZ and invY and mapS and normal
    and (not swapY) and distinct,
    'G16-orthonormal orbits exactly at w in {+-1, +-i}: Z_F (w=1) and Z_Y (w=i); Z_Y: H1, certificates, orthogonal, '
    'G16-invariant, = Ad(S(x)I) Z_F, not SWAP-invariant, != Z_F')
cc2 = res5[str(Rt(3, 5) + Rt(4, 5) * iu)][1] is False
RES['CC2 generic w not orthogonal'] = cc2
print('COUNTERCONTROL CC2 w = (3+4i)/5: G16-orbit orthonormal = %s (as required: False)' % res5[str(Rt(3, 5) + Rt(4, 5) * iu)][1])

# B6 level (i) family and the gate flow
tp = sp.Symbol('tp', real=True); wp = ((1 - tp ** 2) + 2 * iu * tp) / (1 + tp ** 2)
fam = [C1(wt), C1(-wt), C2(wp), C2(-wp)]
famZ = [zdef(v) for v in fam]
okfam = orthonormal(fam) and all(maxent(v) for v in fam) and setEq([cnot(z) for z in famZ], famZ)
xf = Rt(3, 5) + Rt(4, 5) * iu
Uf = sp.eye(4) + (xf - 1) * k2('1', '-') * k2('1', '-').H
c2fixed = all(same_ray(Uf * v, v) for v in fam[2:])
c1moved = not same_ray(Uf * fam[0], fam[0])
chk('B6 level (i) family; flow fixes C2', okfam and c2fixed and c1moved,
    '{C1(w), C1(-w), C2(w\'), C2(-w\')} orthonormal, maximally entangled, cnot-invariant (symbolic t, t\'); U(x) fixes C2, moves C1')

bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
print('VERDICT C4-BELL-FAMILY-EXACT' if not bad else 'NO VERDICT')
