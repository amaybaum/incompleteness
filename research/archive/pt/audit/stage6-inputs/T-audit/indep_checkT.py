#!/usr/bin/env python3
"""Coordinator's independent check of T6's countermodel claims (stage 6, step 4), with the coordinator's own
table-level code (conventions of preaudit_t6.py: states are tables with w00 = 1, defects z_s have z00 = 1/4,
ipW is the plain entrywise sum = 4 tr(pauliW . pauliW); T6's p_s is a quarter of my P_s, so T6's -sin(t)/8 is
my -sin(t)/2).  Reads nothing.  Run: python3 -I -B indep_checkT.py from pt/audit/stage6-inputs/T-audit/.
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-T-FIXED iff all CONFIRMED.
 X1 flow law, every axis: for a symbolic unit axis n and symbolic angle t, on either token and for every s,
    ipW(act_tau(R_n(t)) z_s, act_tau(R_n(pi/2)) P_s) = -sin(t)/2  (equivalently ipW(z_s, act_tau(R_n(u)) P_s) = -cos(u)/2).
 X2 the witness act_tau(R_n(pi/2)) P_s lies in Z_F* for every unit axis: its pairing with every z_t is a quadratic
    form d + sum a_i n_i^2 with no linear or cross terms and d + min a_i >= 0 (so >= 0 on the unit sphere); Q3
    membership is automatic (a pure state's rotation image is a pure state).
 X3 cyc3 and cyc3^-1 on either token move a defect out with witness -1/2 (image of its own eigenstate).
 X4 mixed placement: with the flow on C and J on T, or the flow on T and J on C, K(Z_F) is moved out by each.
 X5 controls: at u = 0 the construction gives -1/2 with y = P_s, which is NOT in Z_F* (no false witness: y must be
    in K); at u = pi the pairing is +1/2; nflip and rot3 pi on either token permute Z_F.
"""
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, symbols, sin, cos, pi, kronecker_product as kron
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M): return Matrix(4, 4, lambda m, n: sp.nsimplify(simplify(expand((KR[(m, n)] * M).trace()))))
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T
ACT = {'C': actC, 'T': actT}
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}
def negstate(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; v = v / sqrt((v.H * v)[0]); return tab(v * v.H)
PS = {s: negstate(ZF[s]) for s in SS}
n1, n2, n3, t, u = symbols('n1 n2 n3 t u', real=True)
def rodrigues(nv, c, s_):
    nv = Matrix(nv); K = Matrix([[0, -nv[2], nv[1]], [nv[2], 0, -nv[0]], [-nv[1], nv[0], 0]])
    return c * eye(3) + s_ * K + (1 - c) * nv * nv.T
def red(e):   # reduce with n1^2 = 1 - n2^2 - n3^2 (unit axis)
    return expand(sp.expand(e).subs(n1 ** 2, 1 - n2 ** 2 - n3 ** 2))
Rn_t = rodrigues([n1, n2, n3], cos(t), sin(t)); Rn_90 = rodrigues([n1, n2, n3], 0, 1); Rn_u = rodrigues([n1, n2, n3], cos(u), sin(u))
print("== X1 flow law for a symbolic unit axis")
ok1 = True; shown = None
for tau, act in ACT.items():
    for s in SS:
        val = red(ipW(act(Rn_t, ZF[s]), act(Rn_90, PS[s])))
        val2 = red(ipW(ZF[s], act(Rn_u, PS[s])))
        ok1 = ok1 and simplify(val + sin(t) / 2) == 0 and simplify(val2 + cos(u) / 2) == 0
        if shown is None: shown = (val, val2)
rec('X1', ok1, 'ipW(act(R_n(t)) z_s, act(R_n(pi/2)) P_s) = -sin(t)/2 and ipW(z_s, act(R_n(u)) P_s) = -cos(u)/2 for every unit axis, both tokens, all s', 'sample: %s ; %s' % shown)
print("== X2 the witness lies in Z_F* for every unit axis")
ok2 = True; forms = []
for tau, act in ACT.items():
    for s in SS:
        y = act(Rn_90, PS[s])
        for tt in SS:
            val = red(ipW(y, ZF[tt]))
            P = sp.Poly(val, n1, n2, n3)
            # no linear or cross terms: every monomial is 1 or n_i^2
            mons = P.monoms(); okm = all(sum(m) in (0, 2) and max(m) in (0, 2) for m in mons)
            d = P.coeff_monomial(1); a = [P.coeff_monomial(n1 ** 2), P.coeff_monomial(n2 ** 2), P.coeff_monomial(n3 ** 2)]
            ok2 = ok2 and okm and (d + min(a) >= 0)
            if tau == 'C' and s == (1, 1): forms.append(str(val))
rec('X2', ok2, 'every pairing of the witness with a defect is d + sum a_i n_i^2 with d + min a_i >= 0 (>= 0 on the sphere): the witness is in Z_F*, hence in K(Z_F)', 'token C, s=(1,1): %s' % forms)
print("== X3 cyc3 and its inverse")
cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); cyc3i = cyc3.T
def in_KZF_pure(p): return all(simplify(ipW(p, PS[tt])) <= 2 for tt in SS)
w3 = {}
for name, M in (('cyc3', cyc3), ('cyc3^-1', cyc3i)):
    for tau, act in ACT.items():
        vals = []
        for s in SS:
            p = act(M, PS[s])
            if in_KZF_pure(p): vals.append(simplify(ipW(p, act(M, ZF[s]))))
        w3[name + '@' + tau] = min(vals) if vals else None
rec('X3', all(v == Q(-1, 2) for v in w3.values()), 'cyc3 and cyc3^-1 on either token move a defect out of K(Z_F); witness -1/2', str(w3))
print("== X4 mixed placement")
Rx90 = rodrigues([1, 0, 0], 0, 1)
def witness(act, M, s):
    p = act(M, PS[s]); return simplify(ipW(p, act(M, ZF[s]))) if in_KZF_pure(p) else None
mixed = {'flow@C': witness(actC, Rx90, (1, 1)), 'J@T': witness(actT, cyc3, (1, 1)), 'flow@T': witness(actT, Rx90, (1, 1)), 'J@C': witness(actC, cyc3, (1, 1))}
rec('X4', all(v == Q(-1, 2) for v in mixed.values()), 'flow on C with J on T, and flow on T with J on C: each operation separately moves K(Z_F) out (witness -1/2)', str(mixed))
print("== X5 controls")
s0 = (1, 1)
c_u0 = simplify(ipW(ZF[s0], PS[s0])); c_upi = simplify(ipW(ZF[s0], actC(rodrigues([1, 0, 0], -1, 0), PS[s0])))
ps_in = in_KZF_pure(PS[s0])
def permutes(f): return all(any(f(ZF[s]) == ZF[tt] for tt in SS) for s in SS) and len({tuple(f(ZF[s])) for s in SS}) == 4
NF = Matrix.diag(1, -1, -1); R3 = Matrix.diag(-1, -1, 1)
perm = all(permutes(f) for f in (lambda w: actC(NF, w), lambda w: actT(NF, w), lambda w: actC(R3, w), lambda w: actT(R3, w)))
rec('X5', c_u0 == Q(-1, 2) and not ps_in and c_upi == Q(1, 2) and perm, 'u = 0: pairing -1/2 but P_s is not in Z_F* (not a witness); u = pi: +1/2; nflip and rot3 pi on either token permute Z_F', 'u0 %s in_K %s upi %s perm %s' % (c_u0, ps_in, c_upi, perm))
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('INDEP-T-FIXED' if all(R) else 'INDEP-T-MISMATCH')
