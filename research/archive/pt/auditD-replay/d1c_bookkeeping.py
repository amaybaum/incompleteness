#!/usr/bin/env python3
"""Thread D, certified script d1c -- bookkeeping identities of the written N-CLASS route (RESULT.md, D1.1 steps 1-13)
and one exact end-to-end instance of the normalization procedure.

Conventions as in d1b (DIM-1's): homMap R = diag(1, R); actC R w = homMap R . w; actT R w = w . homMap R^T;
prodState x y = hom x hom y^T; pairVal a b w = a^T w b. Ad_Q(G) := actC Q . actT Q . G . actC Q^T . actT Q^T.

DECISION RULES (fixed before the first run):
  B1  functoriality and commutation must hold as symbolic identities: actC A (actC B w) = actC (A B) w,
      actT A (actT B w) = actT (A B) w, actC A (actT B w) = actT B (actC A w).
  B2  local maps on products: actC M (prodState x y) = prodState (M x) y and actT M (prodState x y) = prodState x (M y)
      (symbolic M, x, y).
  B3  positivity transport: pairVal a b (actC M w) = pairVal (homMap(M)^T a) b w and
      pairVal a b (actT M w) = pairVal a (homMap(M)^T b) w (symbolic); and for an orthogonal M, homMap(M)^T preserves
      the head and the spatial norm of a vector: checked as the identity |M^T v|^2 = |v|^2 under M M^T = I written for a
      symbolic Cayley-parametrized rotation and for a symbolic reflection composed with it.
  B4  the -z3 corner trick: for corners of z3, nflip (corner z3 c) = corner z3 (c + 1), and corner (-z3) b = corner z3 (1 + b)
      (finite enumeration), so actT nflip . G satisfies corner_form's fixing frame at -z3 whenever G has the frame at z3.
  B5  Lorentz algebra of step 3: (1 + w0)^2 - r = 0 and (1 - w0)^2 - r = 0 imply w0 = 0 and r = 1 (exact solve);
      the Euclidean pairing of a null vector (t, v) with (t, -v) is t^2 - |v|^2 = 0 (symbolic).
  B6  end-to-end instance: a gate G built from rational orthogonal data as
      actC(Q^T Q2^T diag(a,1) reflY) . actT(Q^T Q2^T) . cnot . actC(reflY Q2 Q) . actT(Q2 R0 Q)
      must satisfy the frame at z = Q^T z3; running the normalization (corner maps at z, M0 = homMap R0', G3 = Ad_Q(G) .
      actT R0'^T, the axis w of R1', Q2' with Q2' w = e_x, G4 = Ad_{Q2'}(G3)) must return G4 = G(a', b') of the d1b family
      with a' orthogonal and b' = a' J' or -a' J', every step an exact identity on a symbolic table.
  Countercontrol CC-B: the same procedure applied to G(I/2, J'/2) (posInv fails) must return a non-orthogonal a'.
  A VERDICT line prints only if every check passes and the countercontrol behaves as stated.
Exact arithmetic only (sympy, rationals). No floating point, no randomness, no timing in stdout.
"""
import sys
import sympy as sp

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, k: (-1 if (m, k) in NEG else 1) * w[PC[m][k], PT[m][k]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def zero_mat(M):
    return all(sp.simplify(v) == 0 for v in M)


I3 = sp.eye(3)
NFLIP = sp.diag(1, -1, -1)
REFLY = sp.diag(1, -1, 1)
HN = homMap(NFLIP)
Smat = sp.zeros(4, 4); Smat[0, 1] = 1; Smat[1, 0] = 1
Tmat = sp.zeros(4, 4); Tmat[2, 3] = -1; Tmat[3, 2] = 1
Jp = sp.Matrix([[0, -1], [1, 0]])
E = [sp.Matrix([1 if k == m else 0 for k in R4]) for m in R4]
HZ = sp.Matrix([1, 0, 0, 1]); HMZ = sp.Matrix([1, 0, 0, -1])
W = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))


def G_family(a, b):
    a = sp.Matrix(a); b = sp.Matrix(b)

    def G(w):
        out = sp.zeros(4, 4)
        for mu in R4:
            row = w[mu, :].T
            if mu == 0:
                out += (HZ * row.T + HMZ * (HN * row).T) / 2
            elif mu == 3:
                out += (HZ * row.T - HMZ * (HN * row).T) / 2
            else:
                j = mu - 1
                for i in range(2):
                    out += E[i + 1] * (a[i, j] * Smat * row + b[i, j] * Tmat * row).T
        return out
    return G


A3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'A{i}{j}', real=True))
B3 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'B{i}{j}', real=True))
xs = sp.symbols('x0:3', real=True); ys = sp.symbols('y0:3', real=True)
av = sp.symbols('a0:4', real=True); bv = sp.symbols('b0:4', real=True)

print('== B1-B3  functoriality, products, positivity transport')
chk('B1', 'actC A (actC B w) = actC (AB) w; actT A (actT B w) = actT (AB) w; actC A (actT B w) = actT B (actC A w)',
    zero_mat(actC(A3, actC(B3, W)) - actC(A3 * B3, W)) and zero_mat(actT(A3, actT(B3, W)) - actT(A3 * B3, W))
    and zero_mat(actC(A3, actT(B3, W)) - actT(B3, actC(A3, W))), 'identity')
chk('B2', 'actC M (prodState x y) = prodState (Mx) y; actT M (prodState x y) = prodState x (My)',
    zero_mat(actC(A3, prodState(xs, ys)) - prodState(list(A3 * sp.Matrix(xs)), ys))
    and zero_mat(actT(A3, prodState(xs, ys)) - prodState(xs, list(A3 * sp.Matrix(ys)))), 'identity')
chk('B3a', 'pairVal a b (actC M w) = pairVal (homMap(M)^T a) b w; pairVal a b (actT M w) = pairVal a (homMap(M)^T b) w',
    sp.expand(pairVal(av, bv, actC(A3, W)) - pairVal(list(homMap(A3).T * sp.Matrix(av)), bv, W)) == 0
    and sp.expand(pairVal(av, bv, actT(A3, W)) - pairVal(av, list(homMap(A3).T * sp.Matrix(bv)), W)) == 0, 'identity')
p1, p2, p3 = sp.symbols('p1 p2 p3', real=True)
Ksk = sp.Matrix([[0, -p3, p2], [p3, 0, -p1], [-p2, p1, 0]])
Rc = (I3 - Ksk).inv() * (I3 + Ksk)          # Cayley rotation
vv = sp.Matrix(sp.symbols('v1:4', real=True))
ok3 = all(sp.simplify((M.T * vv).dot(M.T * vv) - vv.dot(vv)) == 0 for M in (Rc, Rc * REFLY))
chk('B3b', 'for a Cayley rotation R and for R reflY (symbolic), |M^T v|^2 = |v|^2; homMap(M)^T fixes the head: so '
    'homMap(M)^T maps L into L and actC M, actT M map maxCone (eball 3) into itself', ok3
    and all(homMap(M).T[0, k] == (1 if k == 0 else 0) for M in (I3,) for k in R4), 'identity')

print()
print('== B4  the -z3 corner trick')
z3 = [0, 0, 1]; mz3 = [0, 0, -1]


def corner(z, c):
    return list(z) if c % 2 == 0 else [-t for t in z]


ok4 = all(list(NFLIP * sp.Matrix(corner(z3, c))) == corner(z3, c + 1) for c in (0, 1)) \
    and all(corner(mz3, b) == corner(z3, 1 + b) for b in (0, 1))
chk('B4a', 'nflip (corner z3 c) = corner z3 (c+1) and corner (-z3) b = corner z3 (1+b), for all c, b in Fin 2', ok4,
    'enumerate')
Gc = cnot
ok4b = all(zero_mat(actT(NFLIP, Gc(prodState(mz3, corner(mz3, b)))) - prodState(mz3, corner(mz3, b))) for b in (0, 1))
chk('B4b', 'instance: actT nflip . cnot fixes prodState (-z3) (corner (-z3) b) for b = 0, 1 (corner_form applies at -z3)',
    ok4b, 'identity')

print()
print('== B5  Lorentz algebra of step 3')
w0, r = sp.symbols('w0 r', real=True)
sol = sp.solve([(1 + w0) ** 2 - r, (1 - w0) ** 2 - r], [w0, r], dict=True)
chk('B5a', f'(1+w0)^2 = r and (1-w0)^2 = r have the unique solution w0 = 0, r = 1: {sol}', sol == [{w0: 0, r: 1}],
    'identity')
tt = sp.Symbol('t', real=True)
chk('B5b', 'the pairing of (t, v) with (t, -v) is t^2 - |v|^2 (zero exactly on null vectors)',
    sp.expand(sp.Matrix([tt] + list(vv)).dot(sp.Matrix([tt] + [-c for c in vv])) - (tt ** 2 - vv.dot(vv))) == 0,
    'identity')

print()
print('== B6  end-to-end instance of the normalization procedure')
Q = sp.Matrix([[sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(2, 3)],
               [-sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3)],
               [sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3)]])
Q2 = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
R0 = sp.Matrix([[sp.Rational(5, 13), sp.Rational(12, 13), 0], [sp.Rational(12, 13), -sp.Rational(5, 13), 0], [0, 0, 1]])
aR = sp.Matrix([[sp.Rational(8, 17), -sp.Rational(15, 17)], [sp.Rational(15, 17), sp.Rational(8, 17)]])


def diag_a1(a):
    M = sp.zeros(3, 3)
    M[0:2, 0:2] = a
    M[2, 2] = 1
    return M


orth_ok = all(M.T * M == I3 for M in (Q, Q2, R0)) and aR.T * aR == sp.eye(2) and Q.det() == 1
zq = list(Q.T * sp.Matrix(z3))
chk('B6.0', f'instance data are orthogonal (Q, Q2, R0 rational; det Q = 1); z = Q^T z3 = {zq} is a unit vector',
    orth_ok and sum(t ** 2 for t in zq) == 1, 'witness')
Aq = Q.T * Q2.T * diag_a1(aR) * REFLY
Bq = Q.T * Q2.T
Apq = REFLY * Q2 * Q
Bpq = Q2 * R0 * Q


def Gin(w):
    return actC(Aq, actT(Bq, cnot(actC(Apq, actT(Bpq, w)))))


chk('B6.1', 'the instance gate (N-CLASS by construction) satisfies the frame at z = Q^T z3',
    all(zero_mat(Gin(prodState(corner(zq, p), corner(zq, q))) - prodState(corner(zq, p), corner(zq, p + q)))
        for p in (0, 1) for q in (0, 1)), 'identity')


def Ad(Qm, Gf):
    return lambda w: actC(Qm, actT(Qm, Gf(actC(Qm.T, actT(Qm.T, w)))))


def corner_map(Gf, zc):
    """cornerMap z G: the row 0 of G(tens(hom z) e_nu), as a 4x4 matrix (columns indexed by nu)."""
    M = sp.zeros(4, 4)
    for nu in R4:
        out = Gf(hom(zc) * E[nu].T)
        M[:, nu] = out[0, :].T
    return M


def normalize(Gf, zc, Qm):
    G1 = Ad(Qm, Gf)
    M0 = corner_map(G1, z3)
    R0p = M0[1:4, 1:4]
    G3 = lambda w: G1(actT(R0p.T, w))
    M1 = corner_map(G3, mz3)
    R1p = M1[1:4, 1:4]
    ker = (R1p - I3).nullspace()
    wv = ker[0] / sp.sqrt(ker[0].dot(ker[0])) if len(ker) == 1 else None
    if wv is None:
        return None
    Q2p = sp.Matrix([[wv[0], wv[1], 0], [-wv[1], wv[0], 0], [0, 0, 1]])
    G4 = Ad(Q2p, G3)
    ap = sp.Matrix(2, 2, lambda i, j: G4(E[j + 1] * E[0].T)[i + 1, 1])
    bp = sp.Matrix(2, 2, lambda i, j: -G4(E[j + 1] * E[3].T)[i + 1, 2])
    return dict(M0=M0, R0p=R0p, R1p=R1p, w=wv, Q2p=Q2p, G4=G4, ap=ap, bp=bp)


res = normalize(Gin, zq, Q)
chk('B6.2', 'M0 = homMap R0\' with R0\' orthogonal fixing z3 (step 3 on the instance)',
    res is not None and res['M0'][0, :] == sp.Matrix([[1, 0, 0, 0]]) and res['M0'][:, 0] == sp.Matrix([1, 0, 0, 0])
    and res['R0p'].T * res['R0p'] == I3 and res['R0p'] * sp.Matrix(z3) == sp.Matrix(z3), 'identity')
chk('B6.3', f'R1\' = {res["R1p"].tolist()} is a rotation by pi with axis w = {list(res["w"])} orthogonal to z3 (step 8)',
    res['R1p'].det() == 1 and res['R1p'] * res['R1p'] == I3 and res['w'][2] == 0, 'identity')
ok_fam = zero_mat(res['G4'](W) - G_family(res['ap'], res['bp'])(W))
chk('B6.4', f'G4 = G(a\', b\') on a symbolic table, with a\' = {res["ap"].tolist()}, b\' = {res["bp"].tolist()}', ok_fam,
    'identity')
sgn_ok = res['bp'] == res['ap'] * Jp or res['bp'] == -res['ap'] * Jp
chk('B6.5', 'a\' is orthogonal and b\' = a\' J\' or -a\' J\' (steps 11-12 on the instance)',
    res['ap'].T * res['ap'] == sp.eye(2) and sgn_ok, 'identity')

print()
print('== CC-B  countercontrol: the procedure on G(I/2, J\'/2)')
Gh = G_family(sp.eye(2) / 2, Jp / 2)
rh = normalize(Gh, z3, I3)
chk('CC-B', f'countercontrol: for G(I/2, J\'/2) the procedure returns a\' = {rh["ap"].tolist()}, NOT orthogonal',
    rh is not None and rh['ap'].T * rh['ap'] != sp.eye(2), 'countercontrol')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd1c_bookkeeping: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT D1-BOOKKEEPING-EXACT: functoriality, positivity transport, the -z3 corner trick and the Lorentz '
          'algebra hold; the normalization procedure returns an orthogonal a\' with b\' = +-a\'J\' on the instance and a '
          'non-orthogonal a\' on the posInv-failing countercontrol')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)
