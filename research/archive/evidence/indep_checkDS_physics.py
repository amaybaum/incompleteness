#!/usr/bin/env python3
"""Coordinator's independent check for the DS review: physics and the in-framework which-path computation.
Written without DS code (drafted before DS finished; DS's outputs not read).

Decision rule, fixed before the first run:
- each check prints CONFIRMED or MISMATCH; each countercontrol prints CONFIRMED only if the
  predicted failure occurs;
- the verdict line is INDEP-DS-PHYS-CONFIRMED iff all are CONFIRMED (exit 1 otherwise).

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

n_ok = sum(RESULTS)
print()
print(f"checks: {len(RESULTS)}, confirmed: {n_ok}")
verdict = "INDEP-DS-PHYS-CONFIRMED" if n_ok == len(RESULTS) else "INDEP-DS-PHYS-MISMATCH"
print(f"VERDICT {verdict}")
sys.exit(0 if n_ok == len(RESULTS) else 1)
