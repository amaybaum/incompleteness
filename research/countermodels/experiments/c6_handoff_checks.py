# c6_handoff_checks.py -- research/countermodels node C6: exact checks behind the realization-facing handoff on K(Z_F).
# DECISION RULE (fixed before the first run, 2026-10-10T20:57:52Z by date -u):
#  Conventions as in c1_cones.py. p_s = (E00 - s1 E13 - s2 E22 + s1 s2 E31)/4 (the cap-centre table, stage 6 T6 §3.2).
#  R_n(t) = cos t I + (1 - cos t) n n^T + sin t [n]_x with n symbolic and (cos t, sin t) = (c, s); identities are decided
#  as unique remainders modulo the Groebner basis {n1^2 + n2^2 + n3^2 - 1, c^2 + s^2 - 1}.
#  H1 (flow law, an independent re-derivation of T6 t3/t5): for tau in {C, T} and every s:
#     ipW(act_tau R_n(t) z_s, act_tau R_n(pi/2) p_s) = -s/8 identically, and act_tau R_n(pi/2) p_s pairs with every defect
#     z_u to 0 or to (1 - n_i^2)/8 for some i (so it lies in K(Z_F) = K(Z_F)*: it is a rotated pure state).
#  H2 (sum rules): sum_s z_s = E00; ipW(z_s, T_{psi_s}) = -1/2 with T_{psi_s} the pure cap-centre table (the Bell-type states
#     psi_s are not states of the pair); z_s + z_t is PSD of rank 2 (c2_structure E1 records the decomposition).
#  H3 (pure-like defects): 4 z_s has (0,0) entry 1, squared norm 4, pauliW spectrum (-1/2, 1/2, 1/2, 1/2).
#  H4 (maximal steering, stage 5 C5 theta re-checked): for every sharp effect on the control along a unit vector a, the
#     conditional target vector of 4 z_s is M_s^T a with |M_s^T a| = |a| (pure), symbolic in a.
#  H5 (no continuous local symmetry, a second route): the stabilizer of K(Z_F) among local unitary/antiunitary maps is
#     finite (c2_structure S1: 192, with SWAP 384), so no one-parameter local group preserves K(Z_F); re-checked here as: the
#     Lie algebra of local generators X (x) I + I (x) Y (Pauli coordinates) that map Z_F into its tangent span... simplified to
#     the exact statement: no nonzero local generator h = sum a_i s_i (x) I + b_i I (x) s_i keeps every z_s fixed to first
#     order (the commutator [h, P_s] = 0 for all s forces a = b = 0).
#  COUNTERCONTROLS: CC1 at n = (3,0,4)/5, t with (cos, sin) = (3/5, 4/5), the flow law pairing applied to Q3 members (a
#  pure product rotated and a pure product) is >= 0; CC2 the flow law with p_s replaced by the defect itself
#  (ipW(R z_s, R(pi/2) z_s)) is not identically -s/8.
#  VERDICT C6-HANDOFF-CHECKS-EXACT iff H1-H5 pass and the countercontrols fail as stated.
import sympy as sp
from itertools import product

iu, Rt = sp.I, sp.Rational
s_ = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s_[m], s_[n]) for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def ip(a, b): return sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4)))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def Hom(N):
    H = sp.eye(4); H[1:, 1:] = N; return H
def actC(N, w): return Hom(N) * w
def actT(N, w): return w * Hom(N).T
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-34s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))
n1, n2, n3, c, sn = sp.symbols('n1 n2 n3 c s', real=True)
nv = sp.Matrix([n1, n2, n3])
def cross(n): return sp.Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
def Rn(cv, sv): return cv * sp.eye(3) + (1 - cv) * nv * nv.T + sv * cross(nv)
GB = [n3 ** 2 + n1 ** 2 + n2 ** 2 - 1, c ** 2 + sn ** 2 - 1]     # a Groebner basis (disjoint leading variables)
def reduce(e):          # the unique remainder modulo |n| = 1 and cos^2 + sin^2 = 1
    return sp.expand(sp.reduced(sp.expand(e), GB, n3, c, n1, n2, sn, order='lex')[1])
SIG = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(a, b): return (E(0, 0) + a * E(1, 3) + b * E(2, 2) - a * b * E(3, 1)) / 4
def ps(a, b): return (E(0, 0) - a * E(1, 3) - b * E(2, 2) + a * b * E(3, 1)) / 4
ZF = [zs(a, b) for a, b in SIG]
# H1
okH1 = True; notes = []
for side, act in [('C', actC), ('T', actT)]:
    for a, b in SIG:
        z, p = zs(a, b), ps(a, b)
        lhs = reduce(ip(act(Rn(c, sn), z), act(Rn(0, 1), p)))
        okH1 &= sp.simplify(lhs + sn / 8) == 0
        wit = act(Rn(0, 1), p)
        pr = [reduce(ip(wit, zz)) for zz in ZF]
        allowed = {0, (1 - n1 ** 2) / 8, (1 - n2 ** 2) / 8, (n1 ** 2 + n2 ** 2) / 8}   # (1 - n3^2)/8 reduced
        okH1 &= all(any(sp.simplify(x - y) == 0 for y in allowed) for x in pr)
chk('H1 flow law (every axis, both tokens)', okH1, 'ipW(R_n(t) z_s, R_n(pi/2) p_s) = -sin t/8; witness pairings in {0, (1 - n_i^2)/8}')
# H2
sumZ = sum(ZF, sp.zeros(4, 4)) == E(0, 0)
psi = []
for z in ZF:
    M = pW(z); l = min(M.eigenvals()); v = (M - l * sp.eye(4)).nullspace()[0]; psi.append(v)
def Tpure(v):
    v = sp.Matrix(v); A = v * v.H / sp.expand((v.H * v)[0])
    return sp.Matrix(4, 4, lambda m, n: sp.expand((A * SS[m][n]).trace()))
excl = all(ip(ZF[k], Tpure(psi[k])) == Rt(-1, 2) for k in range(4))
pairs = all(min(pW(ZF[i] + ZF[j]).eigenvals()) >= 0 and (pW(ZF[i] + ZF[j])).rank() == 2 for i in range(4) for j in range(4) if i < j)
chk('H2 sum rules', sumZ and excl and pairs, 'sum z_s = E00; ipW(z_s, T_psi_s) = -1/2; z_s + z_t PSD of rank 2')
# H3
okH3 = all((4 * z)[0, 0] == 1 and ip(4 * z, 4 * z) == 4 and sorted(pW(4 * z).eigenvals().items()) == [(Rt(-1, 2), 1), (Rt(1, 2), 3)] for z in ZF)
chk('H3 pure-like defects', okH3, '4 z_s: entry (0,0) 1, squared norm 4, spectrum (-1/2, 1/2 x3)')
# H4 steering: effect (1 + a.x)/2 on the control -> unnormalized target vector hom(a)^T (4 z_s) / 2
a1, a2, a3 = sp.symbols('a1 a2 a3', real=True)
av = sp.Matrix([a1, a2, a3])
okH4 = True
for z in ZF:
    row = (sp.Matrix([1, a1, a2, a3]).T * (4 * z))
    t0, tb = row[0], sp.Matrix(row[1:])
    okH4 &= sp.expand(t0 - 1) == 0 and sp.expand((tb.T * tb)[0] - (av.T * av)[0]) == 0
chk('H4 maximal steering', okH4, 'conditional target vector of 4 z_s for the sharp effect along a has length |a| (pure on |a| = 1)')
# H5 no local first-order symmetry fixing every z_s: [h, P_s] = 0 for all s with h local forces h = 0
al = sp.symbols('al1:4', real=True); be = sp.symbols('be1:4', real=True)
h = sum((al[i] * kron(s_[i + 1], s_[0]) + be[i] * kron(s_[0], s_[i + 1]) for i in range(3)), sp.zeros(4, 4))
eqs = []
for v in psi:
    P = v * v.H / sp.expand((v.H * v)[0])
    Cm = sp.expand(h * P - P * h)
    eqs += [sp.re(x) for x in Cm] + [sp.im(x) for x in Cm]
sol = sp.solve(eqs, list(al) + list(be), dict=True)
okH5 = len(sol) == 1 and all(v == 0 for v in sol[0].values())
chk('H5 no local first-order symmetry', okH5, 'the only local generator commuting with every P_s is 0 (with c2_structure S1: the local stabilizer is finite)')
# countercontrols
nnum = sp.Matrix([Rt(3, 5), 0, Rt(4, 5)])
def Rnum(cv, sv): return cv * sp.eye(3) + (1 - cv) * nnum * nnum.T + sv * cross(nnum)
def hom(x): return sp.Matrix([1] + list(x))
P1 = hom([0, 0, 1]) * hom([1, 0, 0]).T; P2 = hom([0, 1, 0]) * hom([0, 0, -1]).T
cc1 = ip(actC(Rnum(Rt(3, 5), Rt(4, 5)), P1), actC(Rnum(0, 1), P2)) >= 0
RES['CC1 Q3 members pair nonnegatively'] = cc1
print('COUNTERCONTROL CC1 rotated product pairs %s with a rotated product (>= 0 as required)' % ip(actC(Rnum(Rt(3, 5), Rt(4, 5)), P1), actC(Rnum(0, 1), P2)))
cc2 = sp.simplify(reduce(ip(actC(Rn(c, sn), ZF[0]), actC(Rn(0, 1), ZF[0]))) + sn / 8) != 0
RES['CC2 witness must be p_s'] = cc2
print('COUNTERCONTROL CC2 with z_s in place of p_s the law fails: %s' % cc2)
bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
print('VERDICT C6-HANDOFF-CHECKS-EXACT' if not bad else 'NO VERDICT')
