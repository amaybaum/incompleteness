# y1_criteria.py -- thread Y (stage 4, Q-EX): exact identities behind the two criteria, re-derived.
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * Every check prints one line "PASS <id> ..." or "FAIL <id> ...".
#  * An identity check PASSES iff sympy reduces (lhs - rhs) to exactly 0 (expand, then simplify).
#  * A countercontrol PASSES iff the stated quantity has the stated strict sign, computed exactly.
#  * "VERDICT Y1-CRITERIA-EXACT" prints iff every check passes; otherwise "VERDICT Y1-CRITERIA-FAILED"
#    followed by the failing ids. No float enters any check.
# Conventions (landed at L): tables w[mu][nu], index 0 the unit, order 1,X,Y,Z, first index the control
# token; ipW = Euclidean pairing of the 16 entries; pauliW(w) = (1/4) sum w[mu][nu] s_mu (x) s_nu;
# cnot = the signed permutation sgn/pc/pt of CompositeDimension.lean:741-758 (transcribed below).
import sympy as sp

I = sp.I
S = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]


def pauliW(w):
    M = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            M += w[m][n] * SS[m][n]
    return M / 4


def table(R):
    return [[sp.expand((R * SS[m][n]).trace()) for n in range(4)] for m in range(4)]


def ipW(a, b):
    return sp.expand(sum(a[m][n] * b[m][n] for m in range(4) for n in range(4)))


def basis(m, n):
    return [[1 if (i, j) == (m, n) else 0 for j in range(4)] for i in range(4)]


SGN = lambda m, n: -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnotW(w):
    return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


# A1: ipW(w, v) = 4 tr(pauliW w pauliW v) on all 256 basis pairs.
ok = all(ipW(basis(a, b), basis(c, d)) == sp.expand(4 * (pauliW(basis(a, b)) * pauliW(basis(c, d))).trace())
         for a in range(4) for b in range(4) for c in range(4) for d in range(4))
report("A1", ok, "ipW = 4 tr(pauliW . pauliW) on all 256 basis pairs")
# A2: cnot (landed table map) = Ad(CNOT) on all 16 basis tables; and table(pauliW w) = w.
ok = all(table(CNOT * pauliW(basis(a, b)) * CNOT) == cnotW(basis(a, b)) for a in range(4) for b in range(4))
ok2 = all(table(pauliW(basis(a, b))) == basis(a, b) for a in range(4) for b in range(4))
report("A2", ok and ok2, "cnot = Ad(CNOT) on 16 basis tables; table o pauliW = id")

# Symbolic vectors phi, chi (8 real symbols each) and the cap parameter c.
c, lam = sp.symbols('c lam', real=True)
pr = sp.symbols('p0:4', real=True); pi_ = sp.symbols('q0:4', real=True)
xr = sp.symbols('x0:4', real=True); xi = sp.symbols('y0:4', real=True)
phi = sp.Matrix([pr[k] + I * pi_[k] for k in range(4)])
chi = sp.Matrix([xr[k] + I * xi[k] for k in range(4)])
nphi = sp.expand((phi.H * phi)[0]); nchi = sp.expand((chi.H * chi)[0])
ov = sp.expand((phi.H * chi)[0] * (chi.H * phi)[0])          # |<phi|chi>|^2
Id4 = sp.eye(4)
E_phi = (Id4 - c * phi * phi.H) / 8                          # cap defect, pauliW form
E_chi = (Id4 - c * chi * chi.H) / 8
# B1: <e_phi(c), P_chi> = (|chi|^2 - c |<phi|chi>|^2)/2 through the table dictionary.
lhs = ipW(table(E_phi), table(chi * chi.H))
report("B1", zero(lhs - (nchi - c * ov) / 2), "<e_phi(c), P_chi> = (|chi|^2 - c|<phi|chi>|^2)/2, symbolic")
# B2: <e_phi(c), e_chi(c)> = (4 - c|phi|^2 - c|chi|^2 + c^2 |<phi|chi>|^2)/16.
lhs = ipW(table(E_phi), table(E_chi))
report("B2", zero(lhs - (4 - c * nphi - c * nchi + c**2 * ov) / 16),
       "<e_phi(c), e_chi(c)> = (4 - c|phi|^2 - c|chi|^2 + c^2|<phi|chi>|^2)/16, symbolic")
# B3: char poly of I - c phi phi^H is (lam-1)^3 (lam - 1 + c|phi|^2).
cp = (lam * Id4 - (Id4 - c * phi * phi.H)).det(method='berkowitz')
report("B3", zero(cp - (lam - 1)**3 * (lam - 1 + c * nphi)), "spec(I - c phi phi^H) = {1 - c|phi|^2, 1, 1, 1}")
# B4: Schmidt: char poly of Psi Psi^H is lam^2 - |psi|^2 lam + |det Psi|^2 (psi = chi, Psi = [[x0,x1],[x2,x3]]).
Psi = sp.Matrix([[chi[0], chi[1]], [chi[2], chi[3]]])
dPsi = Psi.det()
cp2 = (lam * sp.eye(2) - Psi * Psi.H).det()
report("B4", zero(cp2 - (lam**2 - nchi * lam + sp.expand(dPsi * sp.conjugate(dPsi)))),
       "charpoly(Psi Psi^H) = lam^2 - |psi|^2 lam + |det Psi|^2 (max product overlap = top root)")
# B5: max_{a,b}|<a(x)b|psi>|^2 = top singular value^2 of Psi: <a(x)b|psi> = a^T Psi b (index check, symbolic).
a = sp.Matrix(sp.symbols('a0:2')); b = sp.Matrix(sp.symbols('b0:2'))
ab = sp.Matrix([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]])
report("B5", zero((ab.T * chi)[0] - (a.T * Psi * b)[0]), "<a(x)b|psi> (bilinear) = a^T Psi b, symbolic")

# Countercontrols and the window 1 < c <= 2.
e00 = sp.Matrix([1, 0, 0, 0]); e01 = sp.Matrix([0, 1, 0, 0])
def capT(v, cc):
    return table((Id4 - cc * v * v.H / (v.H * v)[0]) / 8)
val = ipW(capT(e00, sp.Rational(5, 2)), capT(e01, sp.Rational(5, 2)))
report("C1", val < 0, "c = 5/2: orthogonal caps pair to %s < 0 (orbit self-positivity fails above c = 2)" % val)
val = ipW(capT(e00, 2), capT(e01, 2))
report("C2", val >= 0, "c = 2: orthogonal caps pair to %s >= 0 (boundary of the window)" % val)
ev = list((Id4 - e00 * e00.H) .eigenvals().keys())
report("C3", min(ev) >= 0, "c = 1: I - phi phi^H has eigenvalues %s >= 0, so it is PSD: no defect" % sorted(ev))
psi = sp.Matrix([2, 0, 0, 1])                       # not maximally entangled
P00 = table(e00 * e00.H)
val = ipW(capT(psi, 2), P00)
report("C4", val < 0, "Bell-type seed e_psi(2), psi=(2,0,0,1): <e, P_00> = %s < 0 (needs max. entanglement)" % val)
bell = sp.Matrix([1, 0, 0, 1])
Pb = sp.Matrix([[bell[0], bell[1]], [bell[2], bell[3]]])
d2 = sp.expand(Pb.det() * sp.conjugate(Pb.det())) / ((bell.H * bell)[0])**2
report("C5", d2 == sp.Rational(1, 4), "Bell (1,0,0,1): normalized |det Psi|^2 = %s, so lam_max = 1/2" % d2)
# D1: the EBF fixed vector E00 is fixed by Ad(CNOT), by Ad(U (x) I) (U = 1 - i(X+Y+Z), unnormalized) and by T.
U = sp.eye(2) - I * (S[1] + S[2] + S[3]); UU = kron(U, S[0])
E00 = basis(0, 0)
okd = (cnotW(E00) == E00 and table(UU * pauliW(E00) * UU.H / 4) == E00
       and table(pauliW(E00).T) == E00)
report("D1", okd, "E00 fixed by cnot, by Ad(U(x)I), by the transpose: nonzero fixed vector for EBF")

if fails:
    print("VERDICT Y1-CRITERIA-FAILED " + " ".join(fails))
else:
    print("VERDICT Y1-CRITERIA-EXACT")
