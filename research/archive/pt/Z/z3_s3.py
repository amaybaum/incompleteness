"""z3_s3.py -- thread Z, node S3: G16 plus the one-parameter rotation actC Rx(theta) (not commuting with cnot). EXACT.

Basis V = (|++>, |+->, |-+>, |-->) (X eigenbasis of both tokens; V = H(x)H as a matrix, entries +-1/2).
Coefficients of chi in V: (c1, c2, c3, c4) = (c++, c+-, c-+, c--); A = c++ c--, B = c+- c-+, A' = c++ c+-, B' = c-+ c--.
DECISION RULE (fixed before the first run). PASS/FAIL per line, exact sympy (alpha, beta, gamma real symbols).
  G1  CNOT (X(x)I) CNOT = X(x)X; [X(x)I, X(x)X] = 0; Z(x)I, I(x)Z conjugate X(x)I, X(x)X to +-themselves; both are
      real (T sends exp(-i a H/2) to exp(+i a H/2)). Hence the connected group generated is the closed 2-torus
      T2 = {exp(-i(alpha X(x)I + beta X(x)X)/2)}, normalized by G16.
  G2  V^* exp(-i(alpha X(x)I + beta X(x)X)/2) V = diag(e^{-i(a+b)/2}, e^{-i(a-b)/2}, e^{i(a+b)/2}, e^{i(a-b)/2}).
  G3  in V, CNOT is the permutation (++)->(++), (+-)->(--), (-+)->(-+), (--)->(+-), and CNOT = I(x)P+ + Z(x)P- while
      I(x)P+ + X(x)P- differs from CNOT (the amendment's erratum, checked).
  G4  the unitary part of G16 (8 elements mod phase) meets T2 only in I (criterion: V-diagonal with
      d++ d-+ = d+- d--); hence identity component T2 (dim 2) and component group G16 (order 16).
  R1  invariants: det = A - B in V; the torus sends (A, B) to (e^{-i beta} A, e^{i beta} B) and (A', B') to
      (e^{-i alpha} A', e^{i alpha} B'); det(CNOT chi) = A' - B'; for products c_st = a_s b_t: A = B; for CNOT
      products: A' = B' (symbolic).
  R2  the Schmidt formula on the instance: largest eigenvalue of M M^* (M the V-coefficient matrix of psi) equals
      (1 + sqrt(1 - 4|det|^2))/2.
  R3  psi = (15, -1, 7, 7)/18 (computational) has V-coefficients (7/9, 4/9, 0, 4/9), |A| = |A'| = 28/81, B = B' = 0;
      so psi is not in T2.SEP (needs |A| = |B|) nor in T2.CNOT.SEP (needs |A'| = |B'|), and
      f(psi) = (1 + sqrt(1 - 4 (28/81)^2))/2 <= 7/8 (exact: 16 * 3425 <= 9 * 6561).
  R4  the seed e = (7/8) E00 - T_psi/4: rho(e) has eigenvalue -1/32 (on psi), so e is not in Q3; <e, T_phi> =
      7/8 - |<psi|phi>|^2 on three instances (product, torus image of a product, CNOT image of a product), each >= 0;
      <e, g e> >= 49/64 - 7/16 = 21/64 > 0.
  R5  no Bell-type defect: the only maximally entangled psi with ||A|-|B|| = 1/2 are (|++> + e^{ig}|-->)/sqrt2 and
      (|+-> + e^{ig}|-+>)/sqrt2 [W, AM-GM]; CNOT maps both to products (det = 0, symbolic g).
 Countercontrols (each must be REJECTED):
  CC1 a product p (a = (3,4)/5, b = (5,12)/13 in the X basis) has A = B: the unreachability test does not accept it.
  CC2 CNOT p has A' = B': not accepted either.
  CC3 the sketch's form I(x)P+ + X(x)P- is not CNOT (also printed in G3).
  CC4 a non-equatorial control axis n = (3,0,4)/5: n.s(x)I and its CNOT conjugate do not commute (the abelian
      2-torus structure of S3 is specific to equatorial axes).
VERDICT 'VERDICT S3-EXOTIC-EXISTENCE ...' only if all checks PASS and all countercontrols are REJECTED; else
'VERDICT S3-FAILED'.
"""
import sympy as sp

I, R = sp.I, sp.Rational
al, be, g = sp.symbols('alpha beta gamma', real=True)
results = []


def check(name, ok, note=''):
    results.append((name, bool(ok)))
    print(f"{name:5s} {'PASS' if ok else 'FAIL'}  {note}")


def Z(M):
    return sp.simplify(sp.expand(M)) == sp.zeros(*M.shape)


s0, sx, sz = sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[1, 0], [0, -1]])
kr = sp.kronecker_product
XI, XX, ZI, IZ = kr(sx, s0), kr(sx, sx), kr(sz, s0), kr(s0, sz)
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Pp, Pm = (s0 + sx) / 2, (s0 - sx) / 2
Hn = sp.Matrix([[1, 1], [1, -1]])
V = kr(Hn, Hn) / 2          # columns |++>, |+->, |-+>, |-->
E4 = sp.eye(4)

print('== G  the generated group')
okG1 = Z(CN * XI * CN - XX) and Z(XI * XX - XX * XI)
okG1 &= Z(ZI * XI * ZI + XI) and Z(ZI * XX * ZI + XX) and Z(IZ * XI * IZ - XI) and Z(IZ * XX * IZ + XX)
okG1 &= XI.conjugate() == XI and XX.conjugate() == XX and Z(CN * XX * CN - XI)
check('G1', okG1, 'CNOT XI CNOT = XX; [XI, XX] = 0; G16 generators send XI, XX to +-XI, +-XX; real')
TOR = (sp.exp(-I * al / 2) * (E4 + XI) / 2 + sp.exp(I * al / 2) * (E4 - XI) / 2) * \
      (sp.exp(-I * be / 2) * (E4 + XX) / 2 + sp.exp(I * be / 2) * (E4 - XX) / 2)
Dg = sp.diag(sp.exp(-I * (al + be) / 2), sp.exp(-I * (al - be) / 2), sp.exp(I * (al + be) / 2),
             sp.exp(I * (al - be) / 2))
check('G2', Z(V.H * TOR * V - Dg), 'torus = diag(e^{-i(a+b)/2}, e^{-i(a-b)/2}, e^{i(a+b)/2}, e^{i(a-b)/2}) in V')
Pcn = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
okG3 = Z(V.H * CN * V - Pcn) and Z(CN - (kr(s0, Pp) + kr(sz, Pm))) and not Z(CN - (kr(s0, Pp) + kr(sx, Pm)))
check('G3', okG3, 'CNOT permutes (+-) <-> (--) in V; CNOT = I(x)P+ + Z(x)P- (erratum); != I(x)P+ + X(x)P-')


def key(U):
    for e in U:
        if e != 0:
            return tuple(sp.nsimplify(x / e) for x in U)


units, fr = {key(E4): E4}, [E4]
while fr:
    nx = []
    for U in fr:
        for Gm in (CN, ZI, IZ):
            W_ = sp.expand(Gm * U)
            if key(W_) not in units:
                units[key(W_)] = W_
                nx.append(W_)
    fr = nx


def in_T2(U):
    Ub = sp.expand(V.H * U * V)
    if any(Ub[i, j] != 0 for i in range(4) for j in range(4) if i != j):
        return False
    return sp.simplify(Ub[0, 0] * Ub[2, 2] - Ub[1, 1] * Ub[3, 3]) == 0


inT = [k for k, U in units.items() if in_T2(U)]
okG4 = len(units) == 8 and len(inT) == 1 and in_T2(E4) and in_T2(TOR) and in_T2(XI) and in_T2(kr(s0, sx))
check('G4', okG4, f'unitary part of G16: {len(units)} mod phase, {len(inT)} in T2 (identity); X(x)I, I(x)X in T2')

print('== R  reachable set, the unreachable psi, the seed')
c1, c2, c3, c4 = sp.symbols('c1:5')
cv = sp.Matrix([c1, c2, c3, c4])


def coeffs(U, chi_c):
    return sp.expand(V.H * U * V * chi_c)


def inv(c):
    return (sp.expand(c[0] * c[3]), sp.expand(c[1] * c[2]), sp.expand(c[0] * c[1]), sp.expand(c[2] * c[3]))


A0, B0, Ap0, Bp0 = inv(cv)
ct = coeffs(TOR, cv)
At, Bt, Apt, Bpt = inv(ct)
okR1 = all(sp.simplify(x) == 0 for x in (At - sp.exp(-I * be) * A0, Bt - sp.exp(I * be) * B0,
                                          Apt - sp.exp(-I * al) * Ap0, Bpt - sp.exp(I * al) * Bp0))
cc = coeffs(CN, cv)
okR1 &= sp.expand(cc[0] * cc[3] - cc[1] * cc[2] - (Ap0 - Bp0)) == 0
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2')
prod = sp.Matrix([a1 * b1, a1 * b2, a2 * b1, a2 * b2])
Ap_, Bp_ = inv(prod)[0], inv(prod)[1]
okR1 &= sp.expand(Ap_ - Bp_) == 0
cp = coeffs(CN, prod)
okR1 &= sp.expand(inv(cp)[2] - inv(cp)[3]) == 0
check('R1', okR1, 'torus: (A,B) -> (e^{-ib}A, e^{ib}B), (A\',B\') -> (e^{-ia}A\', e^{ia}B\'); det(CNOT chi) = A\'-B\'; '
      'products A = B; CNOT products A\' = B\'')

psi = sp.Matrix([15, -1, 7, 7]) / 18
cpsi = sp.expand(V.H * psi)
M = sp.Matrix([[cpsi[0], cpsi[1]], [cpsi[2], cpsi[3]]])
detM = sp.expand(M.det())
lam = max((MM_ev for MM_ev in (M * M.H).eigenvals().keys()), key=lambda z: float(z))
okR2 = sp.simplify(lam - (1 + sp.sqrt(1 - 4 * detM * sp.conjugate(detM))) / 2) == 0
check('R2', okR2, f'largest eigenvalue of M M* = (1 + sqrt(1 - 4|det|^2))/2 = {sp.nsimplify(lam)}')

A_, B_, Ap_, Bp_ = inv(cpsi)
fA = (1 + sp.sqrt(1 - 4 * (sp.Abs(A_) - sp.Abs(B_)) ** 2)) / 2
fB = (1 + sp.sqrt(1 - 4 * (sp.Abs(Ap_) - sp.Abs(Bp_)) ** 2)) / 2
okR3 = (psi.H * psi)[0] == 1 and list(cpsi) == [R(7, 9), R(4, 9), 0, R(4, 9)]
okR3 &= sp.Abs(A_) == R(28, 81) and B_ == 0 and sp.Abs(Ap_) == R(28, 81) and Bp_ == 0
okR3 &= sp.Abs(A_) != sp.Abs(B_) and sp.Abs(Ap_) != sp.Abs(Bp_)
okR3 &= fA == fB and 16 * (1 - 4 * R(28, 81) ** 2) <= 9 and 16 * 3425 <= 9 * 6561
check('R3', okR3, f'psi unreachable (|A| != |B|, |A\'| != |B\'|); f(psi) = {fA} <= 7/8')

s0_, sx_, sy_, sz_ = s0, sx, sp.Matrix([[0, -I], [I, 0]]), sz
SIG = [s0_, sx_, sy_, sz_]


def table(rho):
    return [sp.expand((rho * kr(SIG[i], SIG[j])).trace()) for i in range(4) for j in range(4)]


alpha = R(7, 8)
Tpsi = table(psi * psi.H)
e = [alpha * (1 if k == 0 else 0) - Tpsi[k] / 4 for k in range(16)]
rho_e = sum((e[4 * i + j] * kr(SIG[i], SIG[j]) for i in range(4) for j in range(4)), sp.zeros(4)) / 4
okR4 = sp.expand(rho_e * psi + psi / 32) == sp.zeros(4, 1)
phis = [sp.Matrix([1, 0, 0, 0]), sp.expand((E4 - I * XX) / sp.sqrt(2) * sp.Matrix([1, 0, 0, 0])),
        sp.expand(CN * kr(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 0])))]
vals = []
for ph_ in phis:
    ov = (psi.H * ph_)[0]
    lhs = sum(e[k] * table(ph_ * ph_.H)[k] for k in range(16))
    rhs = alpha - sp.expand(ov * sp.conjugate(ov))
    okR4 &= sp.simplify(lhs - rhs) == 0 and rhs >= 0
    vals.append(sp.nsimplify(rhs))
okR4 &= alpha ** 2 - alpha / 2 == R(21, 64)
check('R4', okR4, f'rho(e) psi = -psi/32; <e, T_phi> = 7/8 - |<psi|phi>|^2 >= 0 on instances {vals}; '
      'alpha^2 - alpha/2 = 21/64')

okR5 = True
for cvv in (sp.Matrix([1, 0, 0, sp.exp(I * g)]) / sp.sqrt(2), sp.Matrix([0, 1, sp.exp(I * g), 0]) / sp.sqrt(2)):
    d0 = sp.expand(cvv[0] * cvv[3] - cvv[1] * cvv[2])
    okR5 &= sp.simplify(d0 * sp.conjugate(d0)) == R(1, 4)
    cn_c = Pcn * cvv
    okR5 &= sp.expand(cn_c[0] * cn_c[3] - cn_c[1] * cn_c[2]) == 0
check('R5', okR5, 'the two maximally entangled circles with ||A|-|B|| = 1/2 are sent to products by CNOT')

print('== CC countercontrols (each must be REJECTED)')
pa, pb = sp.Matrix([R(3, 5), R(4, 5)]), sp.Matrix([R(5, 13), R(12, 13)])
pc = kr(pa, pb)
Ap, Bp, _, _ = inv(pc)
rej1 = bool(sp.Abs(Ap) == sp.Abs(Bp))
print(f"CC1   {'REJECTED' if rej1 else 'NOT REJECTED'}  product: |A| = |B| = {sp.Abs(Ap)} (not certified unreachable)")
_, _, Ap2, Bp2 = inv(Pcn * pc)
rej2 = bool(sp.Abs(Ap2) == sp.Abs(Bp2))
print(f"CC2   {'REJECTED' if rej2 else 'NOT REJECTED'}  CNOT product: |A'| = |B'| = {sp.Abs(Ap2)}")
rej3 = not Z(CN - (kr(s0, Pp) + kr(sx, Pm)))
print(f"CC3   {'REJECTED' if rej3 else 'NOT REJECTED'}  I(x)P+ + X(x)P- is not CNOT")
Rn = kr((3 * sx + 4 * sz) / 5, s0)
rej4 = not Z(Rn * (CN * Rn * CN) - (CN * Rn * CN) * Rn)
print(f"CC4   {'REJECTED' if rej4 else 'NOT REJECTED'}  axis (3,0,4)/5: generator and its CNOT conjugate do not commute")

allok = all(ok for _, ok in results) and rej1 and rej2 and rej3 and rej4
print(f"SUMMARY checks {sum(ok for _, ok in results)}/{len(results)} PASS; countercontrols rejected "
      f"{int(rej1) + int(rej2) + int(rej3) + int(rej4)}/4")
print('VERDICT S3-EXOTIC-EXISTENCE seed (7/8) E00 - T_psi/4, psi = (15,-1,7,7)/18, f(psi) <= 7/8; '
      'no Bell-type defect' if allok else 'VERDICT S3-FAILED')
