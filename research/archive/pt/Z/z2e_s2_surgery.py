"""z2e_s2_surgery.py -- thread Z, node S2: surgeries with non-orthogonal Bell-type defects are not self-dual. EXACT.

Matrices are written in basis B = (|0+>, |1->, |0->, |1+>) of z2c (W its change of basis); pairing tr(ab); a matrix a
corresponds to the table table(W a W^*), with ipW(table a, table b) = 4 tr(ab), and the Bell defect of psi is
d_psi = I - 2 psi psi^* = 8 rho(e_psi). Circle k defect cone: L1 = {l1(u,L) = -u E12 - conj(u) E21 + L(E33+E44)},
L2 = {l2(u,L) = -u E34 - conj(u) E43 + L(E11+E22)}, |u| <= L. K' = (Q n L1*) + L1, K_T = (Q n L1* n L2*) + L1 + L2.
DECISION RULE (fixed before the first run). PASS/FAIL per line, exact sympy:
  P1  (pair, symbolic: e^{i delta} = (1-t^2+2it)/(1+t^2), t real) psi_l = C1(0), psi_j = C1(delta), c = 1/(1+t^2):
      tr(P_l d_l) = -1, tr(d_j d_l) = 4c, tr(P_l P_j) = c, tr(P_l d_j) = 1 - 2c, and for sigma = 1/(4c):
      y = P_l + sigma d_j, w = P_j + sigma d_l satisfy tr(y d_l) = tr(w d_j) = 0, tr(y d_j) = tr(w d_l) > 0 and
      tr(y w) = c - 1/(4c) (identities).
  P2  exact instance e^{i delta} = (-7 + 24 i)/25 (c = 9/25 < 1/2): y, w in (Q + cone Z) n Z*, tr(y w) = -301/900.
  S1  circle defects: I - 2 C1(g) C1(g)^* = l1(e^{-ig}, 1), I - 2 C2(g) C2(g)^* = l2(e^{-ig}, 1) (symbolic g); the
      pairing formula tr(a l1(u,L)) = -2 Re(conj(u) a12) + L(a33 + a44) (symbolic a, u, L).
  S2  y = [[1,1,c1,0],[1,1,c2,0],[conj c1, conj c2,1,0],[0,0,0,1]], c1 = (1+2i)/5, c2 = (2-i)/5: y in Q + L1 (q0 = y -
      l1(u0, L0) PSD by characteristic-polynomial signs, |u0|^2 <= L0^2, u0 = x0 - 1, x0 = 31/50 + 13i/100,
      L0 = 7/17); y in L1* (4|y12|^2 <= (y33+y44)^2) and in L2* (y34 = 0); y is not PSD.
  S3  w = v v^* + l1(zeta, tau), v = (1, -(4+3i)/5, 157i/125, 0), tau = 17, zeta = p12 + (p33 + 2 tau)/2 (p = v v^*):
      |zeta|^2 <= tau^2, w in L1* (4|w12|^2 <= (w33+w44)^2), w in L2* (w34 = 0); tr(y w) = -6/625.
  S4  the independent route for y not in K': x det S(x) + (x^3 - x + 2/5) = 0 identically (S(x) the Schur complement
      of q(x) = y - l1(x - 1, 1 - x) on its e3 entry), and x^3 - x + 2/5 > 0 on [0, 1] (critical point 1/sqrt3:
      (2/5)^2 > (2/(3 sqrt3))^2; endpoint values 2/5).
  S5  table form: ipW(table(W y W*), table(W w W*)) = -24/625; ipW(table of e_g, table y) = tr(d_g y)/2 >= 0 for the
      circle-1 defects at g = 0, pi/2, pi, 3pi/2 (spot values) and for all g by S1 + L1*.
 Countercontrols (each must be REJECTED):
  CC1 orthogonal pair (delta = pi, c = 0, lemma SD2): tr((P_l + s d_j) d_l) = -1 for every s, so the construction
      cannot put y in Z*.
  CC2 c = 16/25 >= 1/2: the same construction gives tr(y w) = 399/1600 > 0 (no refutation; nothing is claimed there).
  CC3 the pure cap state P = C1(0) C1(0)^* is not in L1* (the L1*-test is not vacuous).
  CC4 a member y0 = q + l1(u, L) + l2(u', L') of K_T (q PSD in L1* n L2*) pairs nonnegatively with w (consistency of
      w in K_T*): tr(y0 w) >= 0.
VERDICT 'VERDICT S2-SURGERY-NOT-SELF-DUAL ...' only if all checks PASS and all countercontrols are REJECTED;
otherwise 'VERDICT S2-SURGERY-FAILED'.
"""
import sys
import sympy as sp

I, R, sq2 = sp.I, sp.Rational, sp.sqrt(2)
de, g = sp.symbols('delta gamma', real=True)
results = []


def check(name, ok, note=''):
    results.append((name, bool(ok)))
    print(f"{name:5s} {'PASS' if ok else 'FAIL'}  {note}")


def S(e):
    return sp.simplify(sp.expand(e))


def tr(a, b):
    return S((a * b).trace())


def psd(M):
    t = sp.symbols('t')
    cp = sp.Poly(sp.expand((t * sp.eye(M.shape[0]) - M).det()), t).all_coeffs()
    return all(S((-1) ** k * c) >= 0 for k, c in enumerate(cp))


def cvec(vals):
    return sp.Matrix(vals)


def C1(gg):
    return cvec([1, sp.exp(I * gg), 0, 0]) / sq2


def C2(gg):
    return cvec([0, 0, 1, sp.exp(I * gg)]) / sq2


def proj(v):
    return v * v.H


def dft(v):
    return sp.eye(4) - 2 * proj(v)


def l1(u, L):
    m = sp.zeros(4)
    m[0, 1], m[1, 0], m[2, 2], m[3, 3] = -u, -sp.conjugate(u), L, L
    return m


def l2(u, L):
    m = sp.zeros(4)
    m[2, 3], m[3, 2], m[0, 0], m[1, 1] = -u, -sp.conjugate(u), L, L
    return m


print('== P  two non-orthogonal Bell-type defects')
tt = sp.symbols('t', real=True)
et_ = ((1 - tt ** 2) + 2 * I * tt) / (1 + tt ** 2)      # e^{i delta}, rational parametrization (delta != pi)
Pl, Pj, dl, dj = proj(C1(0)), proj(cvec([1, et_, 0, 0]) / sq2), dft(C1(0)), dft(cvec([1, et_, 0, 0]) / sq2)
c = 1 / (1 + tt ** 2)


def Z0(e):
    e = sp.expand(e)
    return sp.cancel(sp.re(e)) == 0 and sp.cancel(sp.im(e)) == 0


okP1 = all(Z0(a - b) for a, b in ((tr(Pl, dl), -1), (tr(dj, dl), 4 * c), (tr(Pl, Pj), c), (tr(Pl, dj), 1 - 2 * c)))
sig = 1 / (4 * c)
yP, wP = Pl + sig * dj, Pj + sig * dl
okP1 &= Z0(tr(yP, dl)) and Z0(tr(wP, dj)) and Z0(tr(yP, wP) - (c - 1 / (4 * c)))
okP1 &= Z0(tr(yP, dj) - (1 - 2 * c + 1 / c)) and Z0(tr(wP, dl) - (1 - 2 * c + 1 / c))
okP1 &= Z0((1 - 2 * c + 1 / c) - (1 - c) * (2 * c + 1) / c)
check('P1', okP1, 'symbolic in t (e^{i delta} = (1-t^2+2it)/(1+t^2), c = 1/(1+t^2)): pairings -1, 4c, c, 1-2c; '
      'sigma = 1/(4c): tr(y d_l) = 0, tr(y d_j) = (1-c)(2c+1)/c, tr(y w) = c - 1/(4c)')

ed = (-7 + 24 * I) / 25
vl, vj = C1(0), cvec([1, ed, 0, 0]) / sq2
Pl, Pj, dl, dj = proj(vl), proj(vj), dft(vl), dft(vj)
cc = tr(Pl, Pj)
sg = 1 / (4 * cc)
y2, w2 = Pl + sg * dj, Pj + sg * dl
okP2 = cc == R(9, 25) and psd(Pl) and psd(Pj) and sg > 0
okP2 &= all(tr(y2, d) >= 0 for d in (dl, dj)) and all(tr(w2, d) >= 0 for d in (dl, dj))
okP2 &= tr(y2, w2) == R(-301, 900)
check('P2', okP2, f'c = {cc}; y, w in (Q + cone Z) n Z*; tr(y w) = {tr(y2, w2)}')

print('== S  the circle surgery: an exact pair y, w in K_T* with negative pairing')
uu, LL = sp.symbols('u L')
a = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'a{i}{j}'))
okS1 = S(dft(C1(g)) - l1(sp.exp(-I * g), 1)) == sp.zeros(4) and S(dft(C2(g)) - l2(sp.exp(-I * g), 1)) == sp.zeros(4)
okS1 &= S((a * l1(uu, LL)).trace() - (-sp.conjugate(uu) * a[0, 1] - uu * a[1, 0] + LL * (a[2, 2] + a[3, 3]))) == 0
check('S1', okS1, 'circle defects are l1(e^{-ig},1), l2(e^{-ig},1); tr(a l1(u,L)) = -conj(u) a01 - u a10 + L(a22+a33)')

c1, c2 = (1 + 2 * I) / 5, (2 - I) / 5
y = sp.Matrix([[1, 1, c1, 0], [1, 1, c2, 0], [sp.conjugate(c1), sp.conjugate(c2), 1, 0], [0, 0, 0, 1]])
x0, L0 = R(31, 50) + R(13, 100) * I, R(7, 17)
u0 = x0 - 1
q0 = y - l1(u0, L0)
okS2 = psd(q0) and S(u0 * sp.conjugate(u0)) <= L0 ** 2
okS2 &= 4 * S(y[0, 1] * sp.conjugate(y[0, 1])) <= (y[2, 2] + y[3, 3]) ** 2 and y[2, 3] == 0
okS2 &= not psd(y)
check('S2', okS2, f'y = q0 + l1(u0, L0), q0 PSD, |u0|^2 = {S(u0 * sp.conjugate(u0))} <= {L0 ** 2}; y in L1* n L2*; '
      'y not PSD')

v = cvec([1, -(4 + 3 * I) / 5, R(157, 125) * I, 0])
P = proj(v)
tau = sp.Integer(17)
zeta = S(P[0, 1] + (P[2, 2] + 2 * tau) / 2)
w = P + l1(zeta, tau)
okS3 = psd(P) and S(zeta * sp.conjugate(zeta)) <= tau ** 2
okS3 &= 4 * S(w[0, 1] * sp.conjugate(w[0, 1])) <= S(w[2, 2] + w[3, 3]) ** 2 and S(w[2, 2] + w[3, 3]) >= 0
okS3 &= w[2, 3] == 0 and S(w[0, 0] + w[1, 1]) >= 0
val = tr(y, w)
okS3 &= val == R(-6, 625)
check('S3', okS3, f'zeta = {zeta}; |zeta|^2 <= tau^2; w in (Q + L1) n L1* n L2*; tr(y w) = {val}')

xx = sp.symbols('x', positive=True)
qx = y - l1(xx - 1, 1 - xx)
Sx = qx[:2, :2] - qx[:2, 2:3] * qx[2:3, :2] / qx[2, 2]
okS4 = S(xx * Sx.det() + (xx ** 3 - xx + R(2, 5))) == 0
okS4 &= qx[3, 3] == xx and qx[0, 1] == xx
xs = 1 / sp.sqrt(3)
okS4 &= sp.diff(xx ** 3 - xx, xx).subs(xx, xs) == 0 and R(2, 5) ** 2 > (2 / (3 * sp.sqrt(3))) ** 2
okS4 &= (xx ** 3 - xx + R(2, 5)).subs(xx, 0) > 0 and (xx ** 3 - xx + R(2, 5)).subs(xx, 1) > 0
okS4 &= S(sp.Matrix([[1, c1], [sp.conjugate(c1), 0]]).det()) < 0
check('S4', okS4, 'x det S(x) = -(x^3 - x + 2/5); min on [0,1] at 1/sqrt3 is 2/5 - 2/(3 sqrt3) > 0; x = 0 excluded')

s0m, sxm, sym, szm = sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])
SIG = [s0m, sxm, sym, szm]
kp, km = sp.Matrix([1, 1]) / sq2, sp.Matrix([1, -1]) / sq2
e0, e1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
Wb = sp.Matrix.hstack(sp.kronecker_product(e0, kp), sp.kronecker_product(e1, km), sp.kronecker_product(e0, km),
                      sp.kronecker_product(e1, kp))


def table(mB):
    m = Wb * mB * Wb.H
    return [S((m * sp.kronecker_product(SIG[i], SIG[j])).trace()) for i in range(4) for j in range(4)]


Yt, Wt = table(y), table(w)
okS5 = S(sum(Yt[k] * Wt[k] for k in range(16))) == R(-24, 625)
for gg in (0, sp.pi / 2, sp.pi, 3 * sp.pi / 2):
    et = table(dft(C1(gg)) / 8)
    okS5 &= S(sum(et[k] * Yt[k] for k in range(16)) - tr(dft(C1(gg)), y) / 2) == 0
    okS5 &= tr(dft(C1(gg)), y) >= 0
check('S5', okS5, 'ipW(Y, W) = -24/625 in table form; ipW(e_g, Y) = tr(d_g y)/2 >= 0 at four spot angles')

print('== CC countercontrols (each must be REJECTED)')
s_ = sp.symbols('s', nonnegative=True)
rej1 = S(tr(proj(C1(0)) + s_ * dft(C1(sp.pi)), dft(C1(0))) + 1) == 0
print(f"CC1   {'REJECTED' if rej1 else 'NOT REJECTED'}  orthogonal pair: tr((P_l + s d_j) d_l) = -1 for every s")
eh = (7 + 24 * I) / 25
vj2 = cvec([1, eh, 0, 0]) / sq2
c3 = tr(proj(vl), proj(vj2))
sg3 = 1 / (4 * c3)
val3 = tr(proj(vl) + sg3 * dft(vj2), proj(vj2) + sg3 * dft(vl))
rej2 = bool(c3 == R(16, 25) and val3 == R(399, 1600))
print(f"CC2   {'REJECTED' if rej2 else 'NOT REJECTED'}  c = {c3}: tr(y w) = {val3} > 0 (no refutation)")
Pc = proj(C1(0))
rej3 = bool(4 * S(Pc[0, 1] * sp.conjugate(Pc[0, 1])) > S(Pc[2, 2] + Pc[3, 3]) ** 2)
print(f"CC3   {'REJECTED' if rej3 else 'NOT REJECTED'}  pure cap state P: 2|P12| = 1 > P33 + P44 = 0")
q = sp.Matrix([[2, R(1, 2), R(3, 10), 0], [R(1, 2), 2, 0, R(1, 5)], [R(3, 10), 0, 1, R(1, 4)], [0, R(1, 5), R(1, 4), 1]])
y0 = q + l1(R(3, 10) + R(1, 5) * I, R(1, 2)) + l2(R(1, 5), R(1, 3))
okq = psd(q) and 4 * q[0, 1] ** 2 <= (q[2, 2] + q[3, 3]) ** 2 and 4 * q[2, 3] ** 2 <= (q[0, 0] + q[1, 1]) ** 2
rej4 = bool(okq and tr(y0, w) >= 0)
print(f"CC4   {'REJECTED' if rej4 else 'NOT REJECTED'}  member y0 of K_T: tr(y0 w) = {tr(y0, w)} >= 0")

allok = all(ok for _, ok in results) and rej1 and rej2 and rej3 and rej4
print(f"SUMMARY checks {sum(ok for _, ok in results)}/{len(results)} PASS; countercontrols rejected "
      f"{int(rej1) + int(rej2) + int(rej3) + int(rej4)}/4")
print('VERDICT S2-SURGERY-NOT-SELF-DUAL plain pair (c = 9/25) and the circle surgeries K\', K_T' if allok
      else 'VERDICT S2-SURGERY-FAILED')
