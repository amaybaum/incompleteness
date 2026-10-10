"""u4_kf2.py -- thread U, node U4: K_F2 = (Q3 ∩ {F, cnot F}*) + cone{F, cnot F}, whose V+ part is exactly Q3+.

Decision rule (fixed before the first run):
- PASS/FAIL per check; countercontrols PASS only when the altered object FAILS the property.
- `VERDICT U4-KF2-EXACT` prints only if every check passes; else `VERDICT U4-KF2-FAILED`. Exact arithmetic.
Checked (the projection lemma for F and cnot F is u5_kf PL; the theorem is RESULT.md §1, Theorem S):
K1 F, cnot F orthogonal, both non-PSD, both in maxCone; K2 their cap centres t, CNOT t are orthogonal (a PSD q
violates at most one of the two constraints); K3 P+F = (F + cnot F)/2 is PSD, so P+(K_F2) ⊆ Q3+;
K4 every q ∈ Q3+ has <q, F> = <q, P+F> >= 0 on an instance family; K4c countercontrol: a q ∉ V+ can violate F.
"""
import sympy as sp

I = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


def kron(A, B):
    return sp.Matrix(A.rows * B.rows, A.cols * B.cols,
                     lambda i, j: A[i // B.rows, j // B.cols] * B[i % B.rows, j % B.cols])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in ((1, 3), (2, 2)) else 1) * w[PC[m][n], PT[m][n]])


def pauliW(w):
    R = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            R += w[m, n] * SS[m][n]
    return R / 4


def table(R):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((R * SS[m][n]).trace()))


def ipW(w, v):
    return sp.expand(sum(w[i] * v[i] for i in range(16)))


E = [[sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (m, n) else 0) for n in range(4)] for m in range(4)]
F = (E[0][0] - E[1][3] - E[2][2] - E[3][1]) / 4
cF = cnot(F)
UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
t = sp.Matrix([1, 1, 1, -1]) / 2
mc = all(all(z[0, k] == 0 and z[k, 0] == 0 for k in range(1, 4)) and
         sp.Matrix(3, 3, lambda j, k: z[j + 1, k + 1]).T * sp.Matrix(3, 3, lambda j, k: z[j + 1, k + 1])
         == sp.eye(3) / 16 for z in (F, cF))
check("K1", "exact", ipW(F, cF) == 0 and min(pauliW(F).eigenvals()) < 0 and min(pauliW(cF).eigenvals()) < 0 and mc,
      "<F, cnot F> = 0; both have eigenvalue -1/8; both in maxCone (no local part, bilinear part (1/4) x orthogonal)")
check("K2", "exact", pauliW(F) == (sp.eye(4) - 2 * t * t.T) / 8 and pauliW(cF) == (sp.eye(4) - 2 * (UC * t) * (UC * t).T) / 8
      and (t.T * UC * t)[0] == 0, "pauliW F = (I - 2|t><t|)/8, pauliW cnot F = (I - 2|Ut><Ut|)/8, <t|Ut> = 0")
Pf = pauliW((F + cF) / 2)
check("K3", "exact", min(Pf.eigenvals()) >= 0, "P+F = (F + cnot F)/2 has spectrum %s (PSD): P+(K_F2) ⊆ Q3+" %
      sorted(Pf.eigenvals().keys()))
ok4 = True
for v in (t, sp.Matrix([1, 0, 0, 0]), sp.Matrix([1, 1, 1, 1]), sp.Matrix([1, I, 2, -1])):
    q = table(v * v.H)
    qp = (q + cnot(q)) / 2
    ok4 = ok4 and ipW(qp, F) >= 0 and ipW(qp, cF) >= 0
check("K4", "instance", ok4, "P+ of pure states (t, |00>, |++>, a Gaussian-rational v) pair >= 0 with F and cnot F")
qt = table(t * t.T)
check("K4c", "countercontrol", ipW(qt, F) < 0, "the non-V+ state |t><t| itself violates F (<., F> = %s): the V+ "
      "restriction is load-bearing" % ipW(qt, F))
print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("U4-KF2-EXACT" if nfail == 0 else "U4-KF2-FAILED") + " -- %d checks" % len(RES))
