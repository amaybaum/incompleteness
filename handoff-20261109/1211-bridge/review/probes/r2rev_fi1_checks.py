"""REVIEWER EXACT CHECKS FOR BRIDGE-UNIT1 r2, FI-1 (generic mathematical objects only).

Run under the owner's permission in #1211 c.6739843458 ("Allow generic checks (as #1210)").
Labelled controls on algebra used in the review; not evidence for any physical result.
No OI mechanism is run. Imports no earlier script. Exact sympy arithmetic only.

G1  "non-monomial" and "state-mixing" are different predicates for a general (Kraus) operator.
    (a) K = [[1,1],[0,0]] is non-monomial, yet X -> K X K^dag maps every diagonal matrix to a
        diagonal matrix (not state-mixing); its adjoint K^dag is state-mixing.
    (b) For a 2x2 real rotation U(c,s) (c^2+s^2=1), the (0,1) entry of U D U^T is c*s*(a-b), so U is
        diagonal-preserving under conjugation iff c*s = 0, i.e. iff U is monomial (the unitary case, where the two coincide).
G2  The two necessary conditions "a non-monomial operator" and "an operator moving the all-ones
    ray" are logically independent (cf. kernel `obligations_independent`, C5Discovery.lean):
    (a) G = (2/3)*ones(3) - I is real orthogonal, non-monomial and fixes the all-ones vector;
    (b) P = diag(1, i) is unitary, monomial and moves the all-ones ray.
    Control: the identity is monomial and fixes the ray.
G3  Encoded non-monomiality from a configuration-level permutation (generic 4-state toy model
    with an epistemic restriction; Spekkens-type, not an OI mechanism).
    Ontic set {1,2,3,4}; encoded states Z+={1,2}, Z-={3,4}, X+={1,3}, X-={2,4}, Y+={1,4},
    Y-={2,3}. The permutation pi=(2 3 4) is a permutation matrix (monomial on the configuration
    carrier) and maps Z+->X+, X+->Y+, Y+->Z+ (and the minus states likewise). The encoded qubit
    unitary realizing that Bloch rotation is non-monomial in the encoded Z basis.
    Control: the identity permutation induces the identity encoded map (monomial).
G4  Scope of "the exponent has no content": for permutation (0/1) unitaries every |U|^p table is
    the same; for a weighted monomial Kraus family {2^(-1/2) P_a, 2^(-1/2) P_b} the |K|^p
    transition table is normalized only at p = 2.
"""
import itertools
import sympy as sp

ok = True
def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

def is_monomial(M):
    rows = all(sum(1 for j in range(M.cols) if M[i, j] != 0) == 1 for i in range(M.rows))
    cols = all(sum(1 for i in range(M.rows) if M[i, j] != 0) == 1 for j in range(M.cols))
    return rows and cols

def is_diag(M):
    return all(sp.simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols) if i != j)

# ---------- G1 ----------
a, b = sp.symbols('a b')
Dg = sp.diag(a, b)
K = sp.Matrix([[1, 1], [0, 0]])
check("G1(a) K non-monomial", not is_monomial(K))
check("G1(a) K D K^dag diagonal for symbolic diagonal D", is_diag(K * Dg * K.H))
check("G1(a) K^dag D K is NOT diagonal (state-mixing)", not is_diag(K.H * Dg * K))
c, s = sp.symbols('c s', real=True)
U = sp.Matrix([[c, -s], [s, c]])
off = sp.expand((U * Dg * U.T)[0, 1])
check("G1(b) off-diagonal of U D U^T = c*s*(a - b): got %s" % sp.factor(off),
      sp.simplify(off - c * s * (a - b)) == 0)

# ---------- G2 ----------
G = sp.Rational(2, 3) * sp.ones(3, 3) - sp.eye(3)
one3 = sp.ones(3, 1)
check("G2(a) G orthogonal", G.T * G == sp.eye(3))
check("G2(a) G non-monomial", not is_monomial(G))
check("G2(a) G fixes all-ones", G * one3 == one3)
P = sp.diag(1, sp.I)
v = P * sp.ones(2, 1)
check("G2(b) P unitary", sp.simplify(P.H * P) == sp.eye(2))
check("G2(b) P monomial", is_monomial(P))
check("G2(b) P moves the all-ones ray (P*1 not parallel to 1)", sp.simplify(v[0] - v[1]) != 0)
check("G2 control: identity monomial and fixes ray", is_monomial(sp.eye(3)) and sp.eye(3) * one3 == one3)

# ---------- G3 ----------
enc = {'Z+': {1, 2}, 'Z-': {3, 4}, 'X+': {1, 3}, 'X-': {2, 4}, 'Y+': {1, 4}, 'Y-': {2, 3}}
pi = {1: 1, 2: 3, 3: 4, 4: 2}
Ppi = sp.zeros(4, 4)
for x, y in pi.items():
    Ppi[y - 1, x - 1] = 1
check("G3 pi is a permutation matrix (monomial on configurations)", is_monomial(Ppi))
img = {k: {pi[x] for x in S} for k, S in enc.items()}
target = {'Z+': 'X+', 'X+': 'Y+', 'Y+': 'Z+', 'Z-': 'X-', 'X-': 'Y-', 'Y-': 'Z-'}
check("G3 pi maps encoded states Z+->X+->Y+->Z+ (and minus states)",
      all(img[k] == enc[target[k]] for k in enc))
# Bloch rotation R: x->y, y->z, z->x as axes: e_z->e_x, e_x->e_y, e_y->e_z
R = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
check("G3 Bloch map is a proper rotation (det 1, orthogonal)", R.det() == 1 and R.T * R == sp.eye(3))
# qubit unitary for rotation by 2pi/3 about (1,1,1)/sqrt3
X_ = sp.Matrix([[0, 1], [1, 0]]); Y_ = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z_ = sp.Matrix([[1, 0], [0, -1]])
nvec = [1 / sp.sqrt(3)] * 3
th = 2 * sp.pi / 3
Uq = sp.cos(th / 2) * sp.eye(2) - sp.I * sp.sin(th / 2) * (nvec[0] * X_ + nvec[1] * Y_ + nvec[2] * Z_)
Uq = sp.simplify(Uq)
paulis = [X_, Y_, Z_]
Rq = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.Rational(1, 2) * (paulis[i] * Uq * paulis[j] * Uq.H).trace()))
check("G3 qubit unitary realizes exactly that Bloch rotation", sp.simplify(Rq - R) == sp.zeros(3, 3))
check("G3 encoded unitary is non-monomial in the encoded Z basis", not is_monomial(Uq))
idimg = {k: set(S) for k, S in enc.items()}
check("G3 control: identity permutation induces identity encoded map", all(idimg[k] == enc[k] for k in enc))

# ---------- G4 ----------
p = sp.symbols('p', positive=True)
perms = [sp.Matrix(sp.Matrix.eye(3)[list(q), :]) for q in itertools.permutations(range(3))]
tables = {pp: [m.applyfunc(lambda e: sp.Abs(e) ** pp) for m in perms] for pp in (1, 2, 3)}
check("G4 permutation unitaries: |U|^p tables identical for p = 1, 2, 3",
      tables[1] == tables[2] == tables[3])
Pa = perms[0]; Pb = perms[3]
w = 1 / sp.sqrt(2)
col_sum = sp.simplify(sum((w ** p) * (Pa[j, 0] + Pb[j, 0]) for j in range(3)))
check("G4 weighted monomial Kraus family: column sum = 2*2^(-p/2): got %s" % col_sum,
      sp.simplify(col_sum - 2 * 2 ** (-p / 2)) == 0)
check("G4 normalized only at p = 2", sp.solve(sp.Eq(col_sum, 1), p) == [2])

print("ALL PASS" if ok else "SOME CHECK FAILED")
