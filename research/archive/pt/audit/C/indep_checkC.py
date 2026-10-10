"""Coordinator's independent check of thread C's key claims (audit; exact arithmetic; no thread code used).

Definitions re-typed from the landed and design sources (read in this audit):
  landed CompositeDimension.lean: sgn, pc, pt (:741-756), cnotFun (:759), hom (:100), homMap (:112),
    prodState (:161), actT (:198), actC (:201), z3 (:793), xplus (:1213), phiW (:1220);
  landed K2Guard.lean: reflY (:46), CandidateCone (:95);
  landed CompositeInterface.lean: ProductData/PreComposite (:210-230), coeff (:602), pState, pEff (:635-660),
    modelData (:686);
  design FourCopyDefs.lean: ipW, tabMul, tabT, dualW, FourCopyCoherent famI/famII (:56-60);
  design FourCopyCore.lean: flatW, pairBody, tabCoord (:46-56), KT4Core (:99-114), NClass (:132), orient (:152),
    IE1 (:156).
The two K_c tables E0 and G and the rotation R are the objects under audit, transcribed from thread C's printed
output (c1 K1, K5; c4 N1); the MSIG maps iota, pi, R, sigma are implemented from thread C's prose description.

DECISION RULE (fixed before the first run). Each check prints CONFIRMED or MISMATCH. Countercontrols (ids ending
in 'c') are CONFIRMED exactly when the mutated object gives the opposite verdict. The script prints
'AUDIT-C ALL CONFIRMED' iff every check is CONFIRMED, otherwise 'AUDIT-C MISMATCH FOUND'. No timing in stdout.

Sections:
  P  primitives: the landed cnot is conjugation by CNOT; Q3 and dualW Q3 via the trace pairing; partial transposes.
  M  the mixed assignment (Q3, Q3, Q3, twin): memberships, famI and famII at -1/8, countercontrols.
  T  per-token transport and the 16 twist patterns of {Q3, twin}^4 (thread C B2).
  K  the uniform foil K_c = cone(SEP u cnot SEP): memberships, FCC failures, IE1 failure (thread C B4, A5 HBA/HAB).
  A  the A2 route's linear algebra: the 16 token products are a basis of R^16 inside H00; bi-affine = bilinear on
     H00 x H00 (thread C A2 step 3).
  S  the MSIG carrier: sigma, TPS, and the cross values are the FCC forms (thread C A3 converse).
  B  scope of the tree obstruction (thread C B3): chart transport of cones and gate maps versus the supplied
     locals; an enumeration over Z2 patterns of post-local determinants.
"""
import sympy as sp
from itertools import product, combinations

Q = sp.Rational
I_ = sp.I
R4 = range(4)
ok_all = True


def report(cid, ok, detail):
    global ok_all
    ok = bool(ok)
    ok_all = ok_all and ok
    print(f"{'CONFIRMED' if ok else 'MISMATCH '} {cid}: {detail}", flush=True)


def section(t):
    print(f"\n== {t}", flush=True)


# ---------------------------------------------------------------- landed / design primitives (re-typed)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(Rm):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = Rm
    return M


def actT(Rm, w):  # (actT N w) mu = homMap N (w mu): w . homMap(N)^T
    return w * homMap(Rm).T


def actC(Rm, w):  # homMap N applied to each column: homMap(N) . w
    return homMap(Rm) * w


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sp.expand(sum(E[m, n] * X[m, n] for m in R4 for n in R4))


def tabMul(A, B):
    return A * B


def tabT(A):
    return A.T


def famI(X, Y, E, F):  # design: 0 <= ipW X (tabMul (tabMul E Y) (tabT F))
    return ipW(X, tabMul(tabMul(E, Y), tabT(F)))


def famII(L, Lp, e, f):  # design: 0 <= ipW e (tabMul (tabMul L f) (tabT L'))
    return ipW(e, tabMul(tabMul(L, f), tabT(Lp)))


s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I_], [I_, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
S = [s0, sx, sy, sz]
kron = sp.kronecker_product


def opW(E):
    return sum((E[m, n] * kron(S[m], S[n]) for m in R4 for n in R4), sp.zeros(4, 4))


def pauliW(w):
    return opW(w) / 4


def herm(M):
    return all(sp.simplify(M[i, j] - sp.conjugate(M[j, i])) == 0 for i in R4 for j in R4)


def psd(M):
    """Exact PSD test for a Hermitian matrix: det(tI - M) = sum a_k t^(n-k) with (-1)^k a_k >= 0 for all k."""
    if not herm(M):
        return False
    t = sp.Symbol('t')
    cp = sp.Poly(sp.expand((t * sp.eye(M.shape[0]) - M).det()), t)
    coeffs = cp.all_coeffs()
    for k, a in enumerate(coeffs):
        a = sp.simplify(sp.expand(a))
        if sp.im(a) != 0:
            return False
        if (-1) ** k * sp.re(a) < 0:
            return False
    return True


def ptrans(M, which):  # partial transpose of a 2-qubit 4x4 matrix on qubit `which` (1 or 2)
    N = sp.zeros(4, 4)
    for a, b, c, d in product(range(2), repeat=4):
        i, j = 2 * a + b, 2 * c + d
        if which == 1:
            N[2 * c + b, 2 * a + d] = M[i, j]
        else:
            N[2 * a + d, 2 * c + b] = M[i, j]
    return N


D = homMap(sp.diag(1, -1, 1))  # homMap reflY
reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
xplus, z3 = [1, 0, 0], [0, 0, 1]
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
sing4 = sp.diag(1, -1, -1, -1)

ws = sp.Matrix(4, 4, sp.symbols('w0:16', real=True))
es = sp.Matrix(4, 4, sp.symbols('e0:16', real=True))


def in_Q3(w):
    return psd(pauliW(w))


def in_dQ3(E):
    return psd(opW(E))


def in_twin(w):  # twin = actT reflY '' Q3; actT reflY is an involution
    return psd(pauliW(actT(reflY, w)))


def in_dtwin(E):  # dualW twin = actT reflY '' dualW Q3 (P4)
    return psd(opW(actT(reflY, E)))


# ---------------------------------------------------------------- P
section('P  primitives')
CNOTU = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control = first qubit
lhs = pauliW(cnot(ws))
rhs = CNOTU * pauliW(ws) * CNOTU.H
report('P1', all(sp.expand(lhs[i, j] - rhs[i, j]) == 0 for i in R4 for j in R4),
       'pauliW (cnot w) = U pauliW(w) U^dagger with U = CNOT (control first qubit), symbolic w: cnot is the CNOT '
       'conjugation, so cnot Q3 = Q3 and cnot is an ipW-isometric involution')
report('P2', all(sp.expand(cnot(cnot(ws))[i, j] - ws[i, j]) == 0 for i in R4 for j in R4)
       and sp.expand(ipW(cnot(es), cnot(ws)) - ipW(es, ws)) == 0,
       'cnot (cnot w) = w and ipW (cnot E) (cnot w) = ipW E w, symbolic (hence ipW E (cnot w) = ipW (cnot E) w)')
tr = sp.expand((opW(es) * pauliW(ws)).trace())
report('P3', sp.expand(tr - ipW(es, ws)) == 0,
       'trace pairing: tr(opW E . pauliW w) = ipW E w, symbolic; with pauliW onto Hermitian matrices, Q3 <-> PSD and '
       'dualW Q3 = {E : opW E PSD} (PSD self-duality, written)')
ok4 = all(sp.expand(pauliW(actT(reflY, ws))[i, j] - ptrans(pauliW(ws), 2)[i, j]) == 0 for i in R4 for j in R4) and \
    all(sp.expand(pauliW(actC(reflY, ws))[i, j] - ptrans(pauliW(ws), 1)[i, j]) == 0 for i in R4 for j in R4) and \
    all(sp.expand(pauliW(actC(reflY, actT(reflY, ws)))[i, j] - pauliW(ws).T[i, j]) == 0 for i in R4 for j in R4) and \
    all(sp.expand(ptrans(pauliW(ws), 1)[i, j] - ptrans(pauliW(ws), 2).T[i, j]) == 0 for i in R4 for j in R4)
report('P4', ok4 and sp.expand(ipW(actT(reflY, es), ws) - ipW(es, actT(reflY, ws))) == 0
       and all(sp.expand(actT(reflY, actT(reflY, ws))[i, j] - ws[i, j]) == 0 for i in R4 for j in R4),
       'actT reflY = partial transpose on token 2, actC reflY = on token 1, both = full transpose; PT1 = (PT2)^T; '
       'actT reflY is an ipW-self-adjoint involution. Hence actC reflY Q3 = actT reflY Q3 = twin, D Q3 D = Q3, and '
       'dualW twin = actT reflY (dualW Q3) (written from these identities)')

# ---------------------------------------------------------------- M
section('M  the mixed assignment (Q3, Q3, Q3, twin)')
Lp = actT(reflY, sing4)
report('M1', in_Q3(phiW) and in_dQ3(phiW / 4) and in_Q3(sing4) and Lp == sp.diag(1, -1, 1, -1) and in_twin(Lp)
       and in_dtwin(Lp / 4),
       f"phiW in Q3; phiW/4 in dualW Q3; sing4 in Q3; L' = actT reflY sing4 = {list(Lp.diagonal())} in twin; "
       "L'/4 in dualW twin")
report('M1e', in_dQ3(E00 - phiW / 4) and in_dQ3(E00 - sing4 / 4),
       'complements E00 - phiW/4 and E00 - sing4/4 lie in dualW Q3: the dual tables are effects (values in [0, 1])')
v1 = famI(phiW, phiW, phiW / 4, Lp / 4)
report('M2', v1 == Q(-1, 8), f"famI(X = phiW in K01, Y = phiW in K23, E = phiW/4 in dualW K02, F = L'/4 in dualW K13 = "
                              f"dualW twin) = {v1}")
v2 = famII(phiW, Lp, phiW / 4, phiW / 4)
report('M3', v2 == Q(-1, 8), f"famII(L = phiW in K02, L' in K13 = twin, e = phiW/4, f = phiW/4 in dualW Q3) = {v2}")
c1 = famI(phiW, phiW, phiW / 4, phiW / 4)
c2 = famII(phiW, phiW, phiW / 4, phiW / 4)
report('M2c', c1 >= 0 and c2 >= 0, f'countercontrols with the twin argument replaced by a Q3 one: famI {c1}, famII {c2}')

# ---------------------------------------------------------------- T
section('T  per-token transport and the 16 twist patterns of {Q3, twin}^4 (pairs 01, 23, 02, 13)')
Xs = sp.Matrix(4, 4, sp.symbols('x0:16', real=True))
Ys = sp.Matrix(4, 4, sp.symbols('y0:16', real=True))
Es = sp.Matrix(4, 4, sp.symbols('u0:16', real=True))
Fs = sp.Matrix(4, 4, sp.symbols('v0:16', real=True))
PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3)]  # (row token, column token) of pairs 01, 23, 02, 13


def chart(w, a, b):  # reflect the row token a times and the column token b times: D^a w D^b
    return (D ** a) * w * (D ** b)


baseI = famI(Xs, Ys, Es, Fs)
baseII = famII(Es, Fs, Xs, Ys)  # L on 02, L' on 13, e on 01, f on 23
okT = True
for g in product(range(2), repeat=4):
    gp = [(g[i], g[j]) for (i, j) in PAIRS]
    X2, Y2 = chart(Xs, *gp[0]), chart(Ys, *gp[1])
    E2, F2 = chart(Es, *gp[2]), chart(Fs, *gp[3])
    okT = okT and sp.expand(famI(X2, Y2, E2, F2) - baseI) == 0
    okT = okT and sp.expand(famII(E2, F2, X2, Y2) - baseII) == 0
report('T1', okT, 'for all 16 token charts g, famI and famII are unchanged when the table of each pair (i, j) is '
                  'replaced by D^g_i . T . D^g_j (symbolic, 64 variables)')
v_bad = famI(chart(Xs, 1, 0), Ys, Es, Fs)
report('T1c', sp.expand(v_bad - baseI) != 0, 'countercontrol: reflecting token 0 in X alone changes famI')
cob = set()
for g in product(range(2), repeat=4):
    cob.add(tuple((g[i] + g[j]) % 2 for (i, j) in PAIRS))
even = {t for t in product(range(2), repeat=4) if sum(t) % 2 == 0}
report('T2', cob == even and len(cob) == 8, f'the coboundaries of the 4-cycle are exactly the {len(cob)} even patterns')
base = (0, 0, 0, 1)
witI = (phiW, phiW, phiW / 4, Lp / 4)  # states on 01, 23; duals on 02, 13
witII = (phiW, Lp, phiW / 4, phiW / 4)  # states on 02, 13; duals on 01, 23
okw = True
vals = set()
for tau in sorted(set(product(range(2), repeat=4)) - even):
    g = next(g for g in product(range(2), repeat=4)
             if tuple((base[k] + g[i] + g[j]) % 2 for k, (i, j) in enumerate(PAIRS)) == tau)
    gp = [(g[i], g[j]) for (i, j) in PAIRS]
    cone = lambda k, w: in_Q3(w) if tau[k] == 0 else in_twin(w)
    dual = lambda k, E: in_dQ3(E) if tau[k] == 0 else in_dtwin(E)
    X2, Y2, E2, F2 = (chart(witI[0], *gp[0]), chart(witI[1], *gp[1]), chart(witI[2], *gp[2]), chart(witI[3], *gp[3]))
    L2, Lp2, e2, f2 = (chart(witII[0], *gp[2]), chart(witII[1], *gp[3]), chart(witII[2], *gp[0]), chart(witII[3], *gp[1]))
    mem = cone(0, X2) and cone(1, Y2) and dual(2, E2) and dual(3, F2) and cone(2, L2) and cone(3, Lp2) \
        and dual(0, e2) and dual(1, f2)
    a, b = famI(X2, Y2, E2, F2), famII(L2, Lp2, e2, f2)
    vals.add((a, b))
    okw = okw and mem and a < 0 and b < 0
report('T3', okw and vals == {(Q(-1, 8), Q(-1, 8))},
       f'each of the 8 odd patterns: the transported witnesses are members of that pattern\'s cones and duals '
       f'(checked directly), with (famI, famII) values {sorted(vals)}')
print('  NOTE [written] even patterns: by T1 FCC(tau) <=> FCC(0) for every coboundary tau, and FCC(0) (uniform Q3) holds by '
      'the trace pairing P3 with the Kronecker product of PSD matrices (landed probe F2/F3, replayed byte-identically). '
      'So on {Q3, twin}^4, FCC holds exactly at the 8 even patterns (thread C B2 confirmed).')

# ---------------------------------------------------------------- K
section('K  the uniform foil K_c = cone(SEP u cnot SEP)')
E0 = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, 0, 0]])
G = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0]])
x1, x2, x3, y1, y2, y3 = sp.symbols('x1 x2 x3 y1 y2 y3', real=True)
form = sp.expand((hom([x1, x2, x3]).T * E0 * hom([y1, y2, y3]))[0, 0])
lag = sp.expand((x1 ** 2 + x2 ** 2) * (y3 ** 2 + y2 ** 2) - (x1 * y3 - x2 * y2) ** 2 - (x1 * y2 + x2 * y3) ** 2)
report('K1', form == sp.expand(1 + x1 * y3 - x2 * y2) and lag == 0 and cnot(E0) == E0,
       f'hom x^T E0 hom y = {form}; Lagrange identity (x1^2+x2^2)(y3^2+y2^2) - (x1 y3 - x2 y2)^2 = (x1 y2 + x2 y3)^2; '
       'cnot E0 = E0. Hence |x1 y3 - x2 y2| <= |x||y| <= 1 on the ball, E0 >= 0 on SEP, and by P2 on cnot SEP: '
       'E0 in dualW K_c')
report('K2', not in_dQ3(E0), 'E0 is not in dualW Q3 (opW E0 has a negative eigenvalue): K_c is a proper subcone of Q3')
Pxy = prodState([x1, x2, x3], [y1, y2, y3])
rx = (s0 + x1 * sx + x2 * sy + x3 * sz) / 2
ry = (s0 + y1 * sx + y2 * sy + y3 * sz) / 2
okprod = all(sp.expand(pauliW(Pxy)[i, j] - kron(rx, ry)[i, j]) == 0 for i in R4 for j in R4)
report('K3', okprod and in_Q3(G),
       'pauliW (prodState x y) = rho_x (x) rho_y, symbolic (products PSD on the ball); with P1, K_c is inside Q3. '
       'G is in Q3 = dualW Q3 (as sets), hence G in dualW K_c')
report('K4', cnot(prodState(xplus, z3)) == phiW, 'phiW = cnot (prodState xplus z3): phiW lies in cnot SEP, so in K_c')
vk = famI(phiW, phiW, E0, G)
vk2 = famII(phiW, phiW, E0, G)
report('K5', vk == -1 and vk2 == -1,
       f'famI(phiW, phiW, E0, G) = {vk}: famI fails for uniform K_c and for (Q3, Q3, K_c, K_c); '
       f'famII(L = phiW, L\' = phiW, e = E0, f = G) = {vk2}: famII fails for (K_c, K_c, Q3, Q3)')
report('K5c', famI(phiW, phiW, E00, G) > 0, f'countercontrol: with the unit E00 in place of E0 the value is '
                                             f'{famI(phiW, phiW, E00, G)} > 0')
Rr = sp.Matrix([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
report('K6', Rr.T * Rr == sp.eye(3) and Rr.det() == 1 and actC(Rr, phiW) == G and ipW(E0, G) == -1,
       'R is a rotation; actC R phiW = G; ipW E0 G = -1 with E0 in dualW K_c: G is not in K_c, so actC R does not '
       'map K_c into itself and IE1 (K_c) fails (IE1 asks actC R K = K for every rotation)')
report('K6c', in_Q3(actC(Rr, phiW)), 'countercontrol: the same rotation keeps phiW inside Q3 (IE1 of Q3 is not refuted)')
print('  NOTE [written] uniform K_c with cnot gates and identity locals: hcls holds (NClass with identity locals is '
      'N = cnot); hadm: products in K_c by definition, K_c inside Q3 inside maxCone (P3 with the Lorentz-cone '
      'factorization), convex cone; hcl: generated by a compact base avoiding 0; hgate: cnot exchanges SEP and cnot SEP '
      '(P2). So the four pair hypotheses hold and FCC and C fail (K5, K6): thread C B4 confirmed.')

# ---------------------------------------------------------------- A
section('A  the A2 route: linear algebra of step 3')
Ssts = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]


def flat(w):
    return [w[a, b] for a in R4 for b in R4]  # finProdFinEquiv (a, b) = b + 4 a


TP = sp.Matrix([flat(prodState(s, t)) for s in Ssts for t in Ssts])
dt = TP.det()
report('A1', abs(dt) == 256 and all(TP[k, 0] == 1 for k in range(16)),
       f'the 16 token products tp s t (s, t in S = {{e_x, e_y, e_z, -e_z}}) have det {dt} and flat index 0 equal to 1: '
       'a basis of R^16 inside H00')
alpha = sp.Symbol('alpha')
beta = sp.Matrix(sp.symbols('b0:16'))
gamma = sp.Matrix(sp.symbols('g0:16'))
Mm = sp.Matrix(16, 16, sp.symbols('m0:256'))
uu = sp.Matrix(sp.symbols('p0:16'))
vv = sp.Matrix(sp.symbols('q0:16'))
biaff = alpha + (beta.T * uu)[0] + (gamma.T * vv)[0] + (uu.T * Mm * vv)[0]
e0v = sp.zeros(16, 1)
e0v[0] = 1
Cp = Mm + beta * e0v.T + e0v * gamma.T + alpha * e0v * e0v.T
sub = {uu[0]: 1, vv[0]: 1}
report('A2', sp.expand(biaff.subs(sub) - (uu.T * Cp * vv)[0].subs(sub)) == 0,
       'a general bi-affine map (289 coefficients) restricted to H00 x H00 equals the bilinear form u^T C\' w with '
       'C\' = M + beta e0^T + e0 gamma^T + alpha e0 e0^T: two bi-affine maps that agree on basis x basis inside H00 '
       'agree on H00 x H00 (with A1)')
xs4 = [sp.symbols(f'z{t}_1:4', real=True) for t in range(4)]
tp = lambda a, b: flat(prodState(a, b))
okA3 = True
for a, b, c, d in product(R4, repeat=4):
    lhs = sp.expand(tp(xs4[0], xs4[2])[4 * a + c] * tp(xs4[1], xs4[3])[4 * b + d])
    rhs = sp.expand(tp(xs4[0], xs4[1])[4 * a + b] * tp(xs4[2], xs4[3])[4 * c + d])
    okA3 = okA3 and lhs == rhs
report('A3', okA3, 'Psi(tp x0 x2, tp x1 x3)_abcd = tabCoord a b (tp x0 x1) * tabCoord c d (tp x2 x3) for all a, b, c, d, '
                   'symbolic x: under N2 and prodEff_apply the two bi-affine maps of step 3 agree at the 256 points')

# ---------------------------------------------------------------- S
section('S  the MSIG carrier (thread C A3, converse direction)')


def hom16(u):
    return sp.Matrix([1] + list(u))


def pState(u, w):
    return hom16(u) * hom16(w).T


def iota(Z):
    P = sp.zeros(17, 17)
    for a, b, c, d in product(R4, repeat=4):
        P[1 + 4 * a + b, 1 + 4 * c + d] = Z[(a, b, c, d)]
    for c, d in product(R4, repeat=2):
        P[0, 1 + 4 * c + d] = Z[(0, 0, c, d)]
    for a, b in product(R4, repeat=2):
        P[1 + 4 * a + b, 0] = Z[(a, b, 0, 0)]
    P[0, 0] = Z[(0, 0, 0, 0)]
    return P


def pi_(P):
    return {(a, b, c, d): P[1 + 4 * a + b, 1 + 4 * c + d] for a, b, c, d in product(R4, repeat=4)}


def Rg(Z):
    return {(a, b, c, d): Z[(a, c, b, d)] for a, b, c, d in product(R4, repeat=4)}


def sigma(P):
    Z = pi_(P)
    return iota(Rg(Z)) + P - iota(Z)


def pEff(ce, cf, P):
    return sp.expand(sum(ce[m] * cf[n] * P[m, n] for m in range(17) for n in range(17)))


ok_inv = True
for i in range(17):
    for j in range(17):
        Bm = sp.zeros(17, 17)
        Bm[i, j] = 1
        ok_inv = ok_inv and sigma(sigma(Bm)) == Bm
Zs = {k: sp.Symbol('Z%d%d%d%d' % k) for k in product(R4, repeat=4)}
okG2 = all(sp.expand(sigma(iota(Zs))[i, j] - iota(Rg(Zs))[i, j]) == 0 for i in range(17) for j in range(17))
report('S1', ok_inv and okG2, 'sigma is an involution of R^{17x17} (289 basis arrays) and sigma iota = iota R (symbolic)')
okN2 = sp.expand(sigma(pState(tp(xs4[0], xs4[2]), tp(xs4[1], xs4[3]))) - pState(tp(xs4[0], xs4[1]),
                                                                                tp(xs4[2], xs4[3]))) == sp.zeros(17, 17)
report('S2', okN2, 'N2 in MSIG for all token vectors (symbolic x0..x3 in R^3): PB.prodState (tp x0 x2) (tp x1 x3) = '
                   'sigma (pState ..) = pState (tp x0 x1) (tp x2 x3) = PA.prodState ..; and PB.prodEff e f := pEff e f o sigma '
                   'satisfies the evaluation law by S1')
Xn = sp.Matrix(4, 4, [1] + list(sp.symbols('xa1:16', real=True)))
Yn = sp.Matrix(4, 4, [1] + list(sp.symbols('ya1:16', real=True)))
ce = sp.symbols('ce0:17', real=True)
cf = sp.symbols('cf0:17', real=True)


def homTab(c):  # the homogenized coefficient table of an affine functional on the pair chart
    T = sp.Matrix(4, 4, lambda a, b: c[1 + 4 * a + b])
    T[0, 0] += c[0]
    return T


Et, Ft = homTab(ce), homTab(cf)
V1 = sp.expand(pEff(ce, cf, sigma(pState(flat(Xn), flat(Yn)))) - famI(Xn, Yn, Et, Ft))
V2 = sp.expand(pEff(ce, cf, sigma(pState(flat(Xn), flat(Yn)))) - famII(Xn, Yn, Et, Ft))
report('S3', V1 == 0 and V2 == 0,
       "cross values: for normalized X, Y (entry (0,0) = 1) and general affine e, f, PB.prodEff e f (PA.prodState X Y) "
       "= famI(X, Y, E~, F~) and, read the other way, PA.prodEff e f (PB.prodState L L') = famII(L, L', e~, f~), with "
       "E~ the homogenized coefficient table (symbolic)")
unit = [1] + [0] * 16
report('S4', pEff(unit, unit, sigma(pState(flat(Xn), flat(Yn)))) == 1,
       'the unit pairing is 1 at the other grouping\'s normalized products (prodEff_unit on the hull body)')
print('  NOTE [written] with hadm (K inside maxCone, so a maxCone table with entry (0,0) = 0 vanishes), an effect e on '
      'pairBody K has E~ in dualW K; FCC gives each cross value >= 0, and with the complement E00 - E~ and '
      'famI(X, Y, E00, E00) = 1, each is <= 1. By S2-S4 MSIG with Omega = conv(A products u B products) satisfies '
      'N0, N1, N2: FCC and hadm imply the existence of a carrier with N0 and N1 and N2 (thread C A3 confirmed).')

# ---------------------------------------------------------------- B
section('B  scope of the tree obstruction (thread C B3)')
okR2 = True
for a in range(2):
    for b in range(2):
        lhs = chart(cnot(chart(ws, a, b)), a, b)
        tw = actT(reflY, cnot(actT(reflY, ws)))  # M_tok's cnotTw = actT reflY . cnot . actT reflY
        tgt = cnot(ws) if a == b else tw
        okR2 = okR2 and all(sp.expand(lhs[i, j] - tgt[i, j]) == 0 for i in R4 for j in R4)
report('B1', okR2, 'gate maps: D^a cnot(D^a w D^b) D^b is cnot for a = b and cnotTw = actT reflY . cnot . actT reflY '
                   'for a != b (symbolic): per-token charts carry cones and gate maps of the quantum data onto those of '
                   'M_tok on every 3-pair subset (with T2 and R1 of thread C)')
tauM = (0, 0, 0, 1)
okR1 = all(any(all((g[PAIRS[k][0]] + g[PAIRS[k][1]]) % 2 == tauM[k] for k in Sk) for g in product(range(2), repeat=4))
           for Sk in combinations(range(4), 3))
report('B2', okR1 and tauM not in cob, 'M_tok\'s twist pattern is a coboundary on every 3-pair subset, not on the cycle')

# post-local determinant patterns: (r_p, c_p) in Z2^2 per pair, r = [det A_p = -1], c = [det B_p = -1];
# orient (A p) (B p) = r_p + c_p (mod 2). The NClass-preserving chart action of token flips g is
# (A, B, A', B') -> (D^g_i A, D^g_j B, A' D^g_i, B' D^g_j), i.e. (r_p, c_p) += (g_i, g_j).
SUB = list(combinations(range(4), 3))


def Pi(Sk, pat):
    return any(all(pat[k] == (f[PAIRS[k][0]], f[PAIRS[k][1]]) for k in Sk) for f in product(range(2), repeat=4))


pats = [tuple(tuple(p[2 * k:2 * k + 2]) for k in range(4)) for p in product(range(2), repeat=8)]
act = lambda pat, g: tuple(((pat[k][0] + g[PAIRS[k][0]]) % 2, (pat[k][1] + g[PAIRS[k][1]]) % 2) for k in range(4))
inv = all(Pi(Sk, pat) == Pi(Sk, act(pat, g)) for Sk in SUB for pat in pats for g in product(range(2), repeat=4))
quantum = ((0, 0), (0, 0), (0, 0), (0, 0))
mtok = ((0, 0), (0, 0), (0, 0), (0, 1))  # B_13 = B'_13 = reflY, other locals identity
fail = [Sk for Sk in SUB if not Pi(Sk, mtok)]
names = ['01', '23', '02', '13']
report('B3', inv and all(Pi(Sk, quantum) for Sk in SUB) and len(fail) == 2,
       'each Pi_S ("the post-local determinant pattern on the 3-pair subset S is a chart image of the quantum one") is '
       'chart-invariant (enumeration, 256 patterns x 16 charts) and holds at the quantum data; at M_tok\'s locals it '
       f'fails on {[[names[k] for k in Sk] for Sk in fail]}: there the chart does not carry the quantum locals onto '
       'M_tok\'s')
Sa, Sb = (0, 1, 2), (0, 1, 3)
glue = all((not (Pi(Sa, pat) and Pi(Sb, pat))) or sum(pat[k][0] + pat[k][1] for k in range(4)) % 2 == 0 for pat in pats)
odd_pats = [pat for pat in pats if tuple((pat[k][0] + pat[k][1]) % 2 for k in range(4)) == tauM]
excl = all(not (Pi(Sa, pat) and Pi(Sb, pat)) for pat in odd_pats)
report('B4', glue and excl and len(odd_pats) == 16,
       'Pi_{01,23,02} and Pi_{01,23,13} together imply EvenCycle of the orientation bits (enumeration over all 256 '
       'patterns), and fail at all 16 patterns with M_tok\'s orientation bits (0,0,0,1), i.e. at every NClass '
       'decomposition of M_tok\'s gates (orientation is a gate invariant, thread D T2)')
idW = sp.eye(4)
cnotTw = lambda w: actT(reflY, cnot(actT(reflY, w)))
report('B5', actT(reflY, phiW) == idW and not in_Q3(idW) and cnotTw(prodState(xplus, z3)) == idW,
       'twin is not inside Q3 (actT reflY phiW = idW, pauliW idW not PSD) and cnotTw maps the product state '
       '(xplus, z3) to idW, so cnot does not map twin into twin')
print('  NOTE [written] B5 with P1 and P4: an NClass gate L . cnot . L\' (L = actC A . actT B) preserves Q3 only if '
      'det A det B = det A\' det B\' = 1, and preserves twin only if det A det B = -1. So on cones in {Q3, twin} with '
      'hcls and hgate the orientation bits equal the twist bits; with B4, the conjunction of "each cone is Q3 or twin" '
      '(one pair each) and the two 3-pair conditions of B4, all chart-invariant, implies an even twist pattern and '
      'hence FCC (T1-T3). So B3 holds for conditions on cones and gate MAPS (or reading the locals only through the '
      'gate), as in thread C\'s B5 wording "intrinsic condition on at most three pair cones"; it fails for conditions '
      'that may read the supplied locals, as the B3 header states.')

print('\nAUDIT-C', 'ALL CONFIRMED' if ok_all else 'MISMATCH FOUND')
