# y6_structural.py -- thread Y (stage 4, Q-EX): exact ingredients of the structural nodes H, T, F.
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * H-lines: (H1) the dimension formulas of the irreducible symmetric-cone families [L: Jordan-von Neumann-Wigner]
#    are enumerated; PASS iff exactly the families printed occur at dimension 16 and at least two families occur at
#    the control dimensions 15 and 27 (the enumerator is not vacuous). (H2) three pure products with
#    <P00 + P01, P11> = 0 and P00, P01 independent, exact; Lorentz control: two distinct extreme rays (1,u), (1,v)
#    of the Lorentz cone have |u + v|^2 < 4 (so their sum pairs positively with every nonzero element). (H3) twin
#    fails H2: idW = actT reflY phiW, phiW in Q3, cnot idW = chainW, and a product effect gives chainW a negative
#    value, all exact. (H4) retention: an exact M with M M^H = a given rational positive definite P.
#  * T-lines: c(x) = dim span{y in K : <x, y> = 0}. PASS iff the exhibited members of the cone orthogonal to the
#    defect have exact rank 15, every exhibited member is checked to lie in the cone exactly, the pure product
#    P00 pairs strictly positively with every defect (so c(P00) <= 9, written argument), and 9 exhibited members
#    of K_gen orthogonal to P00 have rank 9. Countercontrol: in Q3, three different pure states all give c = 9.
#  * F-lines: the face of K(E0) exposed by E0 spans E0^perp (rank 15 from the T-line) and the witness
#    y = P_f3 - E0 is in E0^perp, is not PSD, and pairs >= 0 with the 15 exhibited members; countercontrol: for
#    Q3's face exposed by P00 the same construction (compression to 00^perp) stays PSD.
#  * "VERDICT Y6-STRUCTURAL-EXACT" iff every line passes; else "VERDICT Y6-STRUCTURAL-FAILED" and the failing ids.
import itertools
import sympy as sp

I = sp.I
S = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
pauliW = lambda w: sum((w[m][n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4
table = lambda R: [[sp.expand((R * SS[m][n]).trace()) for n in range(4)] for m in range(4)]
ipW = lambda a, b: sp.expand(sum(a[m][n] * b[m][n] for m in range(4) for n in range(4)))
flat = lambda w: [w[m][n] for m in range(4) for n in range(4)]
R_ = sp.Rational
fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


def proj(v):
    return table(v * v.H / sp.expand((v.H * v)[0]))


def greedy(tables, target):
    chosen, rows = [], []
    for t in tables:
        if sp.Matrix(rows + [flat(t)]).rank() > len(rows):
            rows.append(flat(t)); chosen.append(t)
            if len(rows) == target:
                break
    return chosen


# H1: irreducible symmetric cones: L_n (n), Sym_n(R) (n(n+1)/2), Herm_n(C) (n^2), Herm_n(H) (n(2n-1)), n >= 3,
# Herm_3(O) (27).
def fams(d):
    out = []
    if d >= 3: out.append('Lorentz L%d' % d)
    for n in range(3, 30):
        if n * (n + 1) // 2 == d: out.append('Sym%d(R)' % n)
        if n * n == d: out.append('Herm%d(C)' % n)
        if n * (2 * n - 1) == d: out.append('Herm%d(H)' % n)
    if d == 27: out.append('Herm3(O)')
    return out


f16, f15, f27 = fams(16), fams(15), fams(27)
report("H1", f16 == ['Lorentz L16', 'Herm4(C)'] and len(f15) >= 2 and len(f27) >= 2,
       "dim 16: %s; controls dim 15: %s; dim 27: %s" % (f16, f15, f27))
k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
kv = lambda a, b: sp.Matrix([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]])
P00, P01, P11 = proj(kv(k0, k0)), proj(kv(k0, k1)), proj(kv(k1, k1))
P00p01 = [[P00[m][n] + P01[m][n] for n in range(4)] for m in range(4)]
u, v = sp.Matrix([1] + [0] * 14), sp.Matrix([0, 1] + [0] * 13)
report("H2", ipW(P00p01, P11) == 0 and sp.Matrix([flat(P00), flat(P01)]).rank() == 2 and ((u + v).T * (u + v))[0] < 4,
       "<P00 + P01, P11> = 0 with P00, P01 independent pure products; Lorentz control |u + v|^2 = 2 < 4")
SGN = lambda m, n: -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
cnotW = lambda w: [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
phiW = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
idW = [[1 if m == n else 0 for n in range(4)] for m in range(4)]
chainW = [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]
reflYt = [[phiW[m][n] * (-1 if n == 2 else 1) for n in range(4)] for m in range(4)]      # actT reflY phiW
hx, hz = [1, -1, 0, 0], [1, 0, 0, -1]                                                    # homogenized -e1, -e3 (x 2)
val = sum(hx[m] * chainW[m][n] * hz[n] for m in range(4) for n in range(4)) / R_(4)
okH3 = (reflYt == idW and cnotW(idW) == chainW and val < 0 and
        all(e >= 0 for e in pauliW(phiW).eigenvals().keys()))
report("H3", okH3, "idW = actT reflY phiW, phiW in Q3, cnot idW = chainW, product effect value on chainW = %s < 0" % val)
P = sp.Matrix([[4, 1, 0, I], [1, 3, 1, 0], [0, 1, 2, 0], [-I, 0, 0, 5]])
L_, D_ = P.LDLdecomposition(hermitian=True)
M = L_ * sp.diag(*[sp.sqrt(D_[i, i]) for i in range(4)])
report("H4", all(sp.simplify(x) == 0 for x in (M * M.H - P)) and all(D_[i, i] > 0 for i in range(4)),
       "retention instance: Ad(M) carries I to the positive definite P exactly (Q3 homogeneous)")

# T and F. E0 and its exact eigenvectors (columns: f3 for 3/4, f1 and f4 for 1/4, g for -1/4).
E0 = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, 0, 0]]
rE0 = pauliW(E0)
f3, f1, f4, gv = [sp.Matrix(x) / 2 for x in ([1, -1, 1, 1], [1, 1, 1, -1], [1, 1, -1, 1], [1, -1, -1, -1])]
okeig = all(rE0 * w == lam * w for w, lam in ((f3, R_(3, 4)), (f1, R_(1, 4)), (f4, R_(1, 4)), (gv, -R_(1, 4))))
GI = [0, 1, -1, I, -I, 1 + I, 1 - I, -1 + I, -1 - I, 2, 2 * I]
cands = []
for a, b, d in itertools.product(GI[:7], GI[:7], GI[:7]):
    s = 3 * sp.Abs(a)**2 + sp.Abs(b)**2 + sp.Abs(d)**2
    for e in GI[1:]:
        if sp.Abs(e)**2 == s:
            cands.append(a * f3 + b * f1 + d * f4 + e * gv)
nullT = [proj(w) for w in cands]
selE = greedy(nullT, 15)
okmem = all(ipW(t, E0) == 0 for t in selE)
report("T1", okeig and len(selE) == 15 and okmem,
       "K(E0): %d independent pure states in Q3 with <P, E0> = 0 (members of K(E0)): c(E0) = 15" % len(selE))
k_p, k_pi = (k0 + k1), (k0 + I * k1)
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
gen9 = [kv(k1, b) for b in (k0, k1, k_p, k_pi)] + [kv(a, k1) for a in (k0, k_p, k_pi)] + [CN * kv(a, k1) for a in (k_p, k_pi)]
sel9 = greedy([proj(w) for w in gen9], 9)
ok9 = len(sel9) == 9 and all(ipW(t, P00) == 0 and ipW(t, E0) >= 0 for t in sel9)     # pure, in Q3 and E0^*: in K(E0)
report("T2", ok9 and ipW(P00, E0) > 0, "K(E0): <P00, E0> = %s > 0 so c(P00) <= 9 (written), and 9 members of K_gen orthogonal "
       "to P00 give c(P00) = 9 != 15 = c(E0): no automorphism of K(E0) maps P00 to E0" % ipW(P00, E0))
ZF = [[[R_(1, 4), 0, 0, 0], [0, 0, 0, R_(s1, 4)], [0, 0, R_(s2, 4), 0], [0, -R_(s1 * s2, 4), 0, 0]]
      for s1 in (1, -1) for s2 in (1, -1)]
capF = [[vv for (val_, mu, vs) in pauliW(z).eigenvects() if val_ < 0 for vv in vs][0] for z in ZF]
capF = [w / sp.sqrt(sp.expand((w.H * w)[0])) for w in capF]          # orthonormal cap centres
assert all(sp.simplify((capF[i].H * capF[j])[0] - (1 if i == j else 0)) == 0 for i in range(4) for j in range(4))
GI2 = [0, 1, I, 1 + I, 2]
candZ = []
for cs in itertools.product(GI2, repeat=4):
    if sp.Abs(cs[0])**2 == sum(sp.Abs(x)**2 for x in cs[1:]) and cs[0] != 0:
        candZ.append(sum((cs[k] * capF[k] for k in range(4)), sp.zeros(4, 1)))
pool = [ZF[1], ZF[2], ZF[3]] + [proj(w) for w in candZ]
selZ = greedy(pool, 15)
okZ = len(selZ) == 15 and all(ipW(t, ZF[0]) == 0 and all(ipW(t, z) >= 0 for z in ZF) for t in selZ)
posZ = all(ipW(P00, z) > 0 for z in ZF) and all(ipW(t, z) >= 0 for t in sel9 for z in ZF)
report("T3", okZ and posZ and ok9, "K(Z_F): %d independent members orthogonal to z_0 (c(z_0) = 15); <P00, z> > 0 for all z "
       "in Z_F, so c(P00) = 9: no automorphism of K(Z_F) maps P00 to z_0" % len(selZ))
cnt = []
for x in (kv(k0, k0), sp.Matrix([1, 0, 0, 1]), sp.Matrix([1, 2, 3 * I, -1 + I])):
    perp = (x.H).nullspace()
    fam = [proj(w) for w in perp] + [proj(perp[i] + perp[j]) for i in range(3) for j in range(i + 1, 3)] + \
          [proj(perp[i] + I * perp[j]) for i in range(3) for j in range(i + 1, 3)]
    cnt.append(sp.Matrix([flat(t) for t in fam]).rank())
report("T4", cnt == [9, 9, 9], "countercontrol: in Q3 the pure states |00>, Bell, phi0 all have c = %s (span Herm(x^perp))" % cnt)
y = [[proj(f3)[m][n] - E0[m][n] for n in range(4)] for m in range(4)]
evy = pauliW(y).eigenvals()
okF = ipW(y, E0) == 0 and min(evy.keys()) < 0 and all(ipW(y, t) >= 0 for t in selE)
report("F1", okF and len(selE) == 15, "K(E0) not perfect: y = P_f3 - E0 lies in E0^perp = span of the face, is not PSD "
       "(eigenvalues %s) and pairs >= 0 with the face" % sorted(evy.keys()))
Pi = sp.eye(4) - kv(k0, k0) * kv(k0, k0).H
comp = Pi * f3 * f3.H * Pi
report("F2", all(e >= 0 for e in comp.eigenvals().keys()), "countercontrol: for Q3's face exposed by P00 the same construction "
       "(compression of P_f3 to 00^perp) is PSD, i.e. stays in the face")
if fails:
    print("VERDICT Y6-STRUCTURAL-FAILED " + " ".join(fails))
else:
    print("VERDICT Y6-STRUCTURAL-EXACT")
