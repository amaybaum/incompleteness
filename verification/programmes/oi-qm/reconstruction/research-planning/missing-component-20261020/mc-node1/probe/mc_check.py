"""Measurement-as-condition node: exact checks (SymPy, symbolic angles). Token order: data (token 0) first,
ancilla (token 1) second; |ij> = |i>_data |j>_anc. Every check prints PASS/FAIL; the script exits nonzero on FAIL."""
import sys
import sympy as sp
from sympy import Matrix, I, sqrt, cos, sin, exp, simplify, eye, zeros, Rational, symbols, KroneckerProduct as KP

phi, th = symbols('phi theta', real=True)
a, b, cc, d = symbols('a b c d')
results = []
def check(name, cond):
    ok = bool(cond)
    results.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name)

def kron(A, B): return Matrix(sp.kronecker_product(A, B))
def z(M): return all(sp.simplify(sp.expand(x)) == 0 for x in M)
def eqm(A, B): return z(A - B)
ket0 = Matrix([1, 0]); ket1 = Matrix([0, 1]); I2 = eye(2)
X = Matrix([[0, 1], [1, 0]]); Zm = Matrix([[1, 0], [0, -1]]); Sg = Matrix([[1, 0], [0, I]])
ones2 = Matrix([1, 1]); ones4 = Matrix([1, 1, 1, 1])
def proj(v): v = Matrix(v); return (v * v.H) / (v.H * v)[0]
def Rx(t): return cos(t/2) * I2 - I * sin(t/2) * X
def Rz(t): return Matrix([[exp(-I*t/2), 0], [0, exp(I*t/2)]])
CN_a2d = Matrix([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])   # control ancilla (token 1), target data (token 0)
CN_d2a = Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])   # control data, target ancilla
def on_anc(A): return kron(I2, A)
def on_dat(A): return kron(A, I2)
def anc_attach(v): return kron(I2, Matrix(v))                   # 4x2 isometry ψ -> ψ⊗v
def anc_bra(v): return kron(I2, Matrix(v).H)                    # 2x4: (I ⊗ <v|)
def prop_unitary(K, U):
    # K = c U for a scalar c: check K * U^H is scalar multiple of identity
    M = sp.simplify(K * U.H)
    return sp.simplify(M[0, 1]) == 0 and sp.simplify(M[1, 0]) == 0 and sp.simplify(M[0, 0] - M[1, 1]) == 0

# ---------------- Block A: TU supplies the layer flow of X, deterministically ----------------
# A1: deterministic |+i> on the ancilla from |0>: Lueders Y-test, X correction on outcome -i.
plus_i = Matrix([1, I]) / sqrt(2); minus_i = Matrix([1, -I]) / sqrt(2)
br1 = proj(plus_i) * ket0; br2 = X * proj(minus_i) * ket0
check('A1 Y-test branches on |0> are both proportional to |+i> (outcome -i after native X)',
      z(br1 - (br1[0] / plus_i[0]) * plus_i) and z(br2 - (br2[0] / plus_i[0]) * plus_i))
# A2: the layer-flow protocol: ancilla |+i>, CNOT ancilla->data, Lueders test of the ancilla in the real basis
# w=(cos phi, sin phi), w_perp=(-sin phi, cos phi), native X on data for outcome w_perp, ancilla discarded.
w = Matrix([cos(phi), sin(phi)]); wp = Matrix([-sin(phi), cos(phi)])
K_w = anc_bra(w) * CN_a2d * anc_attach(plus_i)
K_wp = X * anc_bra(wp) * CN_a2d * anc_attach(plus_i)
U = Rx(-2*phi)
check('A2 outcome-w branch is proportional to R_x(-2 phi)', prop_unitary(K_w, U))
check('A3 outcome-w_perp branch after native X is proportional to R_x(-2 phi)', prop_unitary(K_wp, U))
check('A4 branches complete: K_w^H K_w + K_wp^H K_wp = I', eqm(K_w.H*K_w + K_wp.H*K_wp, I2))
rho = Matrix([[a, b], [cc, d]])
check('A5 coarse-grained channel equals conjugation by R_x(-2 phi) on a generic input',
      eqm(K_w*rho*K_w.H + K_wp*rho*K_wp.H, U*rho*U.H))
Uq = Rx(sp.pi/2)
check('A6 R_x(pi/2) is non-monomial (two nonzero entries in a row)', all(x != 0 for x in Uq))
img = sp.simplify(Uq * Matrix([[1, 0], [0, 0]]) * Uq.H)
check('A7 R_x(pi/2) breaks entrywise nonnegativity and reality (image of |0><0| has entry +-i/2)',
      any(sp.im(sp.nsimplify(x)) != 0 for x in img))
check('A8 every R_x(t) fixes the uniform ray (ones-fixing): R_x(t) 1 = e^{-it/2} 1',
      z(Rx(th)*ones2 - (cos(th/2) - I*sin(th/2))*ones2))

# ---------------- Block B: the protocol invariant (OnesNormal) holds for TU protocols ----------------
# Full Kraus list of A's protocol on the data token, including the |+i> preparation subtree on a fresh
# ancilla |0> and the configuration Kraus of the discard: sum_b K_b^H 1 = 1.
prep = [proj(plus_i) * ket0, X * proj(minus_i) * ket0]          # ancilla preparation branches (vectors)
# Lueders test of the ancilla, then discard with its configuration Kraus <0|, <1| (the decomposition the
# invariant is stated for; the single Kraus I(x)<w| is another decomposition of the same channel).
Kall = []
for pv in prep:
    for (tv, corr) in [(w, I2), (wp, X)]:
        for cv in (ket0, ket1):
            Kall.append(corr * anc_bra(cv) * on_anc(proj(tv)) * CN_a2d * anc_attach(pv))
check('B0 the Lueders+configuration-discard Kraus list gives the same channel as A5',
      eqm(sum((K*rho*K.H for K in Kall), zeros(2, 2)), U*rho*U.H))
check('B1 TU layer-flow protocol: sum over all branches of K^H 1 equals 1 (OnesNormal)',
      z(sum((K.H * ones2 for K in Kall), zeros(2, 1)) - ones2))
check('B2 TU layer-flow protocol: sum K^H K = I', eqm(sum((K.H*K for K in Kall), zeros(2, 2)), I2))
# B3: the one-bit phase teleport (equatorial TU test at angle theta, ancilla |0>, CNOT data->ancilla) keeps the
# invariant and is NOT deterministic: its two branches differ by Z, which no ones-fixing correction removes.
m_p = Matrix([1, exp(I*th)]) / sqrt(2); m_m = Matrix([1, -exp(I*th)]) / sqrt(2)
T1 = anc_bra(m_p) * CN_d2a * anc_attach(ket0); T2 = anc_bra(m_m) * CN_d2a * anc_attach(ket0)
TL = [anc_bra(cv) * on_anc(proj(mv)) * CN_d2a * anc_attach(ket0) for mv in (m_p, m_m) for cv in (ket0, ket1)]
check('B3 phase teleport (Lueders + configuration discard Kraus) keeps OnesNormal: sum K^H 1 = 1',
      z(sum((K.H*ones2 for K in TL), zeros(2, 1)) - ones2))
check('B3b mutation of the decomposition: the single-Kraus form I(x)<m| does not satisfy the identity (it is not the invariant)',
      not z(T1.H*ones2 + T2.H*ones2 - ones2))
D = Matrix([[1, 0], [0, exp(-I*th)]])
check('B4 phase-teleport branches are D and Z D (D = diag(1, e^{-i theta}))', prop_unitary(T1, D) and prop_unitary(T2, Zm*D))
check('B5 Z moves the uniform ray (no ones-fixing correction can equal it)', not z(Zm*ones2 - ones2) and not z(Zm*ones2 + ones2))
# B6 mutation: replace the projective test by an unsharp Lueders instrument sqrt(E), E = diag(1/4, 3/4) on the
# ancilla after the coupling: the invariant fails, so B1 is sensitive to completeness of the projective family.
E0 = sp.diag(Rational(1, 4), Rational(3, 4)); E1 = eye(2) - E0
U0 = [anc_bra(ket0) * on_anc(E0.applyfunc(sp.sqrt)) * CN_d2a * anc_attach(ket0),
      anc_bra(ket1) * on_anc(E0.applyfunc(sp.sqrt)) * CN_d2a * anc_attach(ket0),
      anc_bra(ket0) * on_anc(E1.applyfunc(sp.sqrt)) * CN_d2a * anc_attach(ket0),
      anc_bra(ket1) * on_anc(E1.applyfunc(sp.sqrt)) * CN_d2a * anc_attach(ket0)]
# the single-Kraus-per-branch choice; OnesNormal asks for SOME decomposition with phases, so test the best phases:
# branch channels are rank-one per (outcome, readout) pair, so only branch phases are free; check no phase choice works
s = [sp.simplify(K.H * ones2) for K in U0]
check('B6 sensitivity: for an unsharp Lueders instrument (E = diag(1/4,3/4)) the identity fails for this decomposition (no claim about other decompositions)',
      not z(sum(s, zeros(2, 1)) - ones2))
# B7 mutation: attach |-> instead of |0> (a preparation of zero uniform weight): CNOT data->anc kicks back Z,
# deterministically, and the invariant fails.
minus = Matrix([1, -1]) / sqrt(2)
Kz = anc_bra(minus) * CN_d2a * anc_attach(minus)
check('B7 mutation (|-> preparation): the kickback branch is exactly Z and K^H 1 != 1',
      eqm(Kz, Zm) and not z(Kz.H*ones2 - ones2))

# ---------------- Block C: TU + Z (one discrete sign) gives every single-token unitary exactly ----------------
# With Z available, the phase teleport is deterministic: correct outcome m_m by Z.
check('C1 with Z: phase teleport deterministic, both branches proportional to D', prop_unitary(T1, D) and prop_unitary(Zm*T2, D))
Hd = Matrix([[1, 1], [1, -1]]) / sqrt(2)
Hc = Rz(sp.pi/2) * Rx(sp.pi/2) * Rz(sp.pi/2)
check('C2 Hadamard = phase * R_z(pi/2) R_x(pi/2) R_z(pi/2) exactly', prop_unitary(Hc, Hd))
check('C3 quarter phase S = phase * R_z(pi/2)', prop_unitary(Rz(sp.pi/2), Sg))

# ---------------- Block D: real TU tests alone stay real-orthogonal? no: R_x is complex; Y basis needed ----------
# D1: without the Y basis (ancilla left in |0> or |+>), the same coupling with real tests gives only real branches.
plus = Matrix([1, 1]) / sqrt(2)
Kr = anc_bra(w) * CN_a2d * anc_attach(plus)
check('D1 control: with ancilla |+> and real tests the branch is real (cos phi I + sin phi X)/sqrt2, not unitary-proportional in general',
      all(sp.im(sp.simplify(x)) == 0 for x in Kr) and not prop_unitary(Kr, U))

fails = [n for n, ok in results if not ok]
print('SUMMARY', len(results) - len(fails), 'PASS', len(fails), 'FAIL')
sys.exit(1 if fails else 0)
