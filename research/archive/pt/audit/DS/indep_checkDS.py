#!/usr/bin/env python3
"""Coordinator's independent check of thread DS (double-slit review). Written without DS code.
Sections P and F were drafted before DS finished (DS outputs unread); sections B and S were added after
reading DS's RESULT, to test its structural claims with my own constructions.

Decision rule, fixed before the first run:
- each check prints CONFIRMED or MISMATCH; each countercontrol prints CONFIRMED only if the
  predicted failure occurs;
- the verdict line is INDEP-DS-CONFIRMED iff all are CONFIRMED (exit 1 otherwise).

Exact symbolic arithmetic only. Nothing nondeterministic is printed.
"""
import sys

import sympy as sp

RESULTS = []


def record(cid, kind, ok, text, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    line = f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}"
    if detail != "":
        line += f" -- {detail}"
    print(line)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


# complex amplitudes as real + i imag
aL, bL, aR, bR = sp.symbols("aL bL aR bR", real=True)
psiL, psiR = aL + sp.I * bL, aR + sp.I * bR
P0 = sp.expand((psiL + psiR) * sp.conjugate(psiL + psiR))
rhs0 = sp.expand(psiL * sp.conjugate(psiL) + psiR * sp.conjugate(psiR) + 2 * sp.re(sp.conjugate(psiL) * psiR))
record("P1", "identity", zero(P0 - rhs0), "|psiL + psiR|^2 = |psiL|^2 + |psiR|^2 + 2 Re(psiL* psiR), symbolic complex")

# detector states: normalized vectors in C^2; record unitary |L>|d0> -> |L>|dL>, |R>|d0> -> |R>|dR>
u1, u2, v1, v2, w1, w2, z1, z2 = sp.symbols("u1 u2 v1 v2 w1 w2 z1 z2", real=True)
dL = sp.Matrix([u1 + sp.I * u2, v1 + sp.I * v2])
dR = sp.Matrix([w1 + sp.I * w2, z1 + sp.I * z2])
Psi = psiL * dL + psiR * dR
P1 = sp.expand((Psi.H * Psi)[0, 0])
ov = (dL.H * dR)[0, 0]
rhs1 = sp.expand(psiL * sp.conjugate(psiL) * (dL.H * dL)[0, 0] + psiR * sp.conjugate(psiR) * (dR.H * dR)[0, 0]
                 + 2 * sp.re(sp.conjugate(psiL) * psiR * ov))
record("P2", "identity", zero(P1 - rhs1),
       "screen density with a path record (detector unread): |psiL|^2<dL|dL> + |psiR|^2<dR|dR> + 2 Re(psiL* psiR <dL|dR>), symbolic; the input's form is the normalized case")

# duality for equal path weights: visibility V = |<dL|dR>|, distinguishability D = trace distance = sqrt(1 - |<dL|dR>|^2)
t = sp.symbols("t", real=True)
dLr = sp.Matrix([1, 0])
dRr = sp.Matrix([sp.cos(t), sp.sin(t)])
Mdiff = dLr * dLr.T - dRr * dRr.T
evs = list(Mdiff.eigenvals().keys())
Dist = sp.simplify(sum(abs(sp.simplify(e)) for e in evs) / 2)
Vis = sp.Abs(sp.cos(t))
record("P3", "identity", zero(sp.simplify(Vis ** 2 + Dist ** 2 - 1).subs(sp.Abs(sp.sin(t)) ** 2, sp.sin(t) ** 2).rewrite(sp.cos)),
       "pure records, real overlap cos t: visibility^2 + distinguishability^2 = 1 (trace distance of the two record states)",
       f"D = {Dist}")

# the in-framework computation on the certified cnot table (path = first token, detector = second; z3 -> |0>)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in ((1, 3), (2, 2)) else 1) * w[PC[m][n], PT[m][n]])


a = sp.symbols("a1:4", real=True)
b = sp.symbols("b1:4", real=True)
hom = lambda x: sp.Matrix([1, *x])
W = cnot(hom(a) * hom(b).T)
path_bloch = [W[k, 0] for k in (1, 2, 3)]
record("F1", "identity", [sp.expand(e) for e in path_bloch] == [a[0] * b[0], a[1] * b[0], a[2]],
       "certified cnot table: after the record, the path's reduced Bloch vector is (a1 b1, a2 b1, a3) -- coherence multiplied by b1, populations unchanged (symbolic, every product preparation)")
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
rho_b = (sp.eye(2) + b[0] * SX + b[1] * SY + b[2] * SZ) / 2
record("F2", "identity", zero((SX * rho_b).trace() - b[0]),
       "for a detector prepared at Bloch vector b with records d_L = d0, d_R = X d0, the overlap <d_L|d_R> = <d0|X|d0> = b1 (tr X rho(b) = b1): the cnot table reproduces V = |<d_L|d_R>| for this record family")
Wid = hom(a) * hom(b).T
record("F1c", "countercontrol", [Wid[k, 0] for k in (1, 2, 3)] == list(a),
       "without the record (no gate) the path keeps its full Bloch vector (predicted)")


# ---------- B: non-discrimination of R1-R3 (screen of 4 points, psiL = 1/(2 sqrt 2), psiR = i^x/(2 sqrt 2)) ----------
g = sp.symbols("g", real=True)
def Q(gam):
    return [sp.nsimplify(sp.Rational(1, 4) * (1 + sp.re(sp.I ** x * gam))) for x in range(4)]
QQ = [sp.expand(sp.Rational(1, 4) * (1 + sp.re((sp.I ** x) * g))) for x in range(4)]
record("B1", "identity", Q(1) == [sp.Rational(1, 2), sp.Rational(1, 4), 0, sp.Rational(1, 4)] and Q(sp.Rational(1, 2)) == [sp.Rational(3, 8), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 4)] and Q(0) == [sp.Rational(1, 4)] * 4
       and all(sp.expand(QQ[x] - ((1 - g) * Q(0)[x] + g * Q(1)[x])) == 0 for x in range(4)),
       "with real record overlap g the screen law is the mixture (1-g) Q[0] + g Q[1] (symbolic): any classical device recording with probability r = 1 - g reproduces R1-R3 exactly, so R1-R3 do not discriminate",
       f"Q[1] = {Q(1)}, Q[1/2] = {Q(sp.Rational(1, 2))}")
bound = (1 / (2 * sp.sqrt(2)) + 1 / (2 * sp.sqrt(2))) ** 2
record("B2", "witness", sp.simplify(bound - sp.Rational(1, 2)) == 0 and 1 > bound,
       "two-path bound P_LR(x) <= (|psiL| + |psiR|)^2 = 1/2: the law (1,0,0,0) is not a quantum two-path law (CL0-type countercontrol)")
r = sp.Rational(1, 2)
Vc, Dc = 1 - r, r
record("B3", "witness", Vc ** 2 + Dc ** 2 == sp.Rational(1, 2),
       "a classical record made with probability r has V = 1 - r and D = r (total variation of the conditional records): V^2 + D^2 = 1/2 at r = 1/2, while pure quantum records give 1 (P3)")

# ---------- S: structural claims on the landed W3 objects ----------
def prodState(x, y):
    return hom(x) * hom(y).T
z3, mz3, xp = [0, 0, 1], [0, 0, -1], [1, 0, 0]
phiW = cnot(prodState(xp, z3))
omB = (prodState(z3, z3) + prodState(mz3, mz3)) / 2
diffpos = [(m, n) for m in range(4) for n in range(4) if phiW[m, n] != omB[m, n]]
record("S1", "witness", phiW == sp.diag(1, 1, -1, 1) and omB == sp.diag(1, 0, 0, 1) and diffpos == [(1, 1), (2, 2)]
       and phiW[:, 0] == omB[:, 0] and phiW[0, :] == omB[0, :] and phiW[3, 3] == omB[3, 3],
       "the coherent record phiW = cnot(prodState xplus z3) and the separable record omega_B share both marginals and the Z(x)Z entry; they differ only in X(x)X and Y(x)Y, which only a complementary (eraser) readout sees",
       str(diffpos))
Tc = phiW[1:, 1:]
s2 = sp.sqrt(2)
a, a2 = sp.Matrix([1, 0, 0]), sp.Matrix([0, 0, 1])
b, b2 = sp.Matrix([1, 0, 1]) / s2, sp.Matrix([1, 0, -1]) / s2
E = lambda u, v: (u.T * Tc * v)[0, 0]
S_phi = sp.simplify(E(a, b) + E(a, b2) + E(a2, b) - E(a2, b2))
To = omB[1:, 1:]
Eo = lambda u, v: (u.T * To * v)[0, 0]
S_om = sp.simplify(Eo(a, b) + Eo(a, b2) + Eo(a2, b) - Eo(a2, b2))
record("S2", "witness", S_phi == 2 * s2 and abs(S_om) <= 2,
       "with path readouts x, z and detector readouts (x +- z)/sqrt 2, CHSH(phiW) = 2 sqrt 2 > 2, while the separable record stays <= 2: path phase control plus an eraser readout is a Bell scenario",
       f"S(phiW) = {S_phi}, S(omega_B) = {S_om}")
SXm, SYm, SZm = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
SG = [sp.eye(2), SXm, SYm, SZm]
def pauliW(w):
    return sum((w[m, n] * sp.kronecker_product(SG[m], SG[n]) for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
H4 = sp.eye(4); H4[1:, 1:] = RH
Tpsi = phiW * H4.T
cz = sp.Matrix([1, 1, 1, -1]) / 2
F = sp.zeros(4, 4); F[0, 0] = sp.Rational(1, 2); F = F - Tpsi / 4
record("S3", "witness", (pauliW(Tpsi) - cz * cz.H).is_zero_matrix and sp.simplify((pauliW(F) * pauliW(Tpsi)).trace()) == -sp.Rational(1, 8),
       "the phase-kick record CZ|+>|+> is the landed T_psi = actT R_H phiW, and the K_gen-positive witness F = E00/2 - T_psi/4 (audited in AUDIT-S2 E3) is negative on it: a detector family with both markings leaves K_gen")
hM = sp.Matrix([[1, 1], [1, -1]]) / s2
img = hM * sp.Matrix([1, 1])
record("S4", "witness", img == sp.Matrix([s2, 0]),
       "the balanced mixer sends (1,1) to (sqrt 2, 0), not a multiple of (1,1): it does not fix the all-ones ray (the ones-fixing access cannot make it available, per the landed instAvail_unitary_fixes_ones)")

n_ok = sum(RESULTS)
print()
print(f"checks: {len(RESULTS)}, confirmed: {n_ok}")
verdict = "INDEP-DS-CONFIRMED" if n_ok == len(RESULTS) else "INDEP-DS-MISMATCH"
print(f"VERDICT {verdict}")
sys.exit(0 if n_ok == len(RESULTS) else 1)
