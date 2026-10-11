#!/usr/bin/env python3
"""indep_checkB5.py — the coordinator's independent check of the research/bridge round-5 results (B18–B21).

Standalone: reads nothing the thread wrote.  Inputs: the kernel sources at the certified base L = 9f9f8257 (read with
`git show` from the repository given as argv[1], for the textual reading checks Z3 only) and exact arithmetic (sympy:
rationals, the imaginary unit, and one formal variable q standing for e^{i pi t}).  No floating point anywhere.
Every object is rebuilt here from the kernel's definitions at L, not from the thread's scripts:
  gateFlow tau t = unit (permMat tau) t = 1 + (q - 1) * (1 - P)/2                         (LiftAudit.lean:47, SecondOrderCircuit.lean:356)
  flow H s = exp(-i s H);  for the transition X_ab and s = pi t:  1 + (cos - 1) Pi_ab - i sin X_ab
                           with cos = (q + 1/q)/2, i sin = (q - 1/q)/2                      (ReachabilitySeam.lean:95, LiftAudit.lean:276)
  transition a b = E_ab + E_ba;  pairProj a b = E_aa + E_bb                                (LieRankSource.lean:199, LiftAudit.lean:252)
  signFun tau e a z = -1 iff tau z != z and z not in {a, tau a} and e z < e (tau z), else 1   (LiftAudit.lean:582)
  phaseFun tau t z = 1 if tau z = z else e^{-i pi t} = 1/q                                  (LiftAudit.lean:586)
  phaseGate a = diag(i at a, 1 elsewhere)                                                   (LieRankSource.lean:209)
  gateFlow_isolation: diag(phaseFun) * G * (D * G * D) = flow (transition a (tau a)) (pi t)  (LiftAudit.lean:660)

DECISION RULE (fixed before run 1, 2026-10-11): the verdict is INDEP-B5-FIXED iff Z1–Z12 all PASS and the
countercontrols CC1–CC7 all evaluate False (each is a statement that must come out False); otherwise INDEP-B5-FAILED
followed by the failing ids.  A failed run is kept, the defect named, and the script re-run; the first run's output is
never overwritten.

  Z1  B18, fixed-point-free involutions.  Carriers Fin 2 x Fin n (n = 1, 2, 3) with tau = levelPerm swap, and
      (Fin 2 x Fin 2) x Fin n (n = 1, 2) with tau = the exchange of the second token: tau is an involution without
      fixed points; phaseFun tau t is the constant 1/q; the kernel's isolation identity holds exactly (rational
      functions of q) for every configuration a and two enumerations e; and the scalar-free form
      G * D * G * D = q * flow (transition a (tau a)) (pi t) holds — the phase diagonal is a unimodular scalar.
  Z2  B18, the sign diagonal from quarter phases: for every case of Z1 and every a, diag(signFun tau e a) equals the
      product over the configurations p with sign -1 of phaseGate(p)^2; the empty product is phaseGate(p)^4 = 1.
  Z3  B18, the kernel's statements read at L (textual): PhasesAvailable quantifies over every state of every level;
      ExchangesAvailable over every pair of every level; DerivedOI is the five-fold conjunction with Exchanges third
      and Phases fourth; PhaseFreeRichness's exchange clause ranges over distinct pairs (implied by
      ExchangesAvailable); conjChannel_smul (ReachabilitySeam.lean) has the hypothesis norm lam = 1 and the conclusion
      conjChannel (lam . V) = conjChannel V; avail_conj_mul has no SubstratumAvail hypothesis; diagonal_avail and
      phaseFree_of_layerFlowExecutable and derivedOI_qm_iff_layerFlowExecutable do (the hypothesis the correction
      removes).
  Z4  B18, the countercontrol carrier Fin 3 x Fin 1 with tau = swap(0, 1) (fixing 2): the kernel identity holds
      (positive control of this implementation), phaseFun is not constant, and G * D * G * D is not a scalar multiple
      of the transition flow (two entries with different ratios).
  Z5  B19, the discard identity: for exact random V, rho on Fin 2 x Fin n (n = 1, 2), the partial trace over the last
      factor of (V (x) 1_2)(rho (x) (1/2) 1_2)(V (x) 1_2)^* is V rho V^*; and the associator identity
      reindex((1 (x) (U (x) 1_n))) = (1 (x) U) (x) 1_n entrywise.
  Z6  B20, P1: w = 3/5 + (4/5)i has |w| = 1, w^4 = (-527 - 336 i)/625, w^k != 1 for k = 1..1000;
      U_J = (1 - i(X + Y + Z))/2 is unitary and U_J^3 is a scalar multiple of 1.
  Z7  B20, P2: through the dictionary dict(w) = (1/4) sum w_mn sigma_m (x) sigma_n and coordOf, on all 16 basis
      tables, Ad(1 (x) diag(1, w)) = actT R_z(3/5, 4/5) and Ad(1 (x) U_J) = actT cyc.
  Z8  B20, P3: K(Z_F) = (Q3 cap Z*) + cone Z, Z = {e_s} (e_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4): dict(e_s)
      = (1 - 2 P_s)/8 with psi_s the unit vector spanning ker(dict(e_s) + 1/8), computed exactly [run 2: run 1 took
      psi_s = (1, s1 s2, s1, -s2)/2 from the archive, whose tensor convention differs from this dictionary's]; for U in {diag(1, w), U_J} there are s and phi in the
      family F_U = {(psi_a + chi psi_b)/sqrt2 : a != b, chi in {1, -1, i, -i}} u {(1 (x) U) psi_s} with y = P_phi in
      Q3 cap Z* (subset of K*) and <y, Ad(1 (x) U) e_s> < 0, so Ad(1 (x) U) e_s is not in K(Z_F); the exact values are
      printed (for diag(1, w) the minimum -1/10 = -sin(theta0)/8, the stage-6 law; for U_J the image ray itself, whose
      Bell overlaps are all 1/4, at -1/8).  [Design note, before run 1: the image-ray member was added after a separate
      exploration (explore_J_family.py) showed the two-term family empty for U_J.]
  Z9  B20, P4: R_z(theta0) (cos 3/5, sin 4/5) has no power equal to 1 up to 1000; actT R_z(theta0) and actT cyc do
      not commute.
  Z10 B21, G1: symbolically, with U(u, v) = diag(e^{iu}, e^{-iu}, e^{iv}, e^{-iv}) and CNOT controlled on token A:
      CNOT U(u, v) CNOT = U(u, -v); X_B U(u, v) X_B = U(-u, -v); CNOT and X_B commute and square to 1;
      1 (x) diag(1, e^{it}) = e^{it/2} U(-t/2, -t/2) and its CNOT conjugate is e^{it/2} U(-t/2, t/2).
  Z11 B21, G3: symbolically <h | U(u, v) X_B h> = 2 Re(conj(h00) h01 e^{iu}) + 2 Re(conj(h10) h11 e^{iv}); the
      exact instance h = (1, 1, 2, i), U = diag(i, -i, 1, 1) gives 0.
  Z12 B21, G2: the 2 x 2 determinant of U(u, v) h is e^{i(u - v)} h00 h11 - e^{i(v - u)} h01 h10 (symbolic); the seed
      (2, 1, 1, 0) has |h00 h11| != |h01 h10| for itself and for its CNOT image (h10 <-> h11) (product-free orbit);
      the countercontrol seed (1, 2, 2, -4) reaches an exact product at U = diag(i, -i, 1, 1).
  CC1 "phaseFun is constant on the Fin 3 carrier" — must be False.
  CC2 "the discard with the ancilla attached as 1_2 (not 1_2/2) returns V rho V^*" — must be False.
  CC3 "Ad(1 (x) 1) moves K(Z_F) within the certificate family of Z8" — must be False.
  CC4 "Ad(1 (x) X) moves K(Z_F) within the certificate family of Z8" — must be False.
  CC5 "actT R_z(theta0) commutes with actT cyc" — must be False.
  CC6 "CNOT U(u, v) CNOT = U(v, u) identically" — must be False.
  CC7 "the G-orbit of (2, 1, 1, 0) contains a product (|h00 h11| = |h01 h10| on some component)" — must be False.

Run: python3 -I -B indep_checkB5.py <repo-with-L>
"""
import itertools
import random
import re
import subprocess
import sys

import sympy as sp

REPO = sys.argv[1]
L = '9f9f8257a980a1819fbbc1dc0019917cf8678626'
I = sp.I
q = sp.Symbol('q', nonzero=True)
results = {}
ccs = []


def check(cid, ok, msg=''):
    results[cid] = bool(ok)
    print(f'{cid:4} {"PASS" if ok else "FAIL"}  {msg}', flush=True)


def countercontrol(cid, value, msg=''):
    ccs.append((cid, bool(value)))
    print(f'{cid:4} evaluates {bool(value)} (must be False)  {msg}', flush=True)


def zero_mat(M):
    return all(sp.simplify(sp.together(x)) == 0 for x in M)


# ------------------------------------------------------------------ kernel objects on a finite carrier
def kernel_objects(states, tau, a, enum):
    """states: list of hashable configurations; tau: dict involution; a: chosen configuration; enum: dict z -> int."""
    N = len(states)
    ix = {z: k for k, z in enumerate(states)}
    P = sp.zeros(N, N)
    for z in states:  # permMat tau: column z has its 1 at row tau z
        P[ix[tau[z]], ix[z]] = 1
    One = sp.eye(N)
    G = One + (q - 1) * (One - P) / 2
    b = tau[a]
    X = sp.zeros(N, N)
    X[ix[a], ix[b]] = 1
    X[ix[b], ix[a]] = 1
    Pi = sp.zeros(N, N)
    Pi[ix[a], ix[a]] = 1
    Pi[ix[b], ix[b]] = 1
    flow = One + ((q + 1 / q) / 2 - 1) * Pi - ((q - 1 / q) / 2) * X
    sign = [(-1 if (tau[z] != z and z not in (a, b) and enum[z] < enum[tau[z]]) else 1) for z in states]
    phase = [(1 if tau[z] == z else 1 / q) for z in states]
    D = sp.diag(*sign)
    Ph = sp.diag(*phase)
    return dict(P=P, G=G, flow=flow, D=D, Ph=Ph, sign=sign, phase=phase, ix=ix, One=One)


def phase_gate(N, k):
    return sp.diag(*[(I if j == k else 1) for j in range(N)])


def cases_fpf():
    out = []
    for n in (1, 2, 3):
        st = [(x, k) for x in range(2) for k in range(n)]
        tau = {(x, k): (1 - x, k) for (x, k) in st}
        out.append((f'Fin2xFin{n}', st, tau))
    for n in (1, 2):
        st = [((x, y), k) for x in range(2) for y in range(2) for k in range(n)]
        tau = {((x, y), k): ((x, 1 - y), k) for ((x, y), k) in st}
        out.append((f'(Fin2xFin2)xFin{n}', st, tau))
    return out


# ------------------------------------------------------------------ Z1, Z2
ok1 = True
ok2 = True
n_id = 0
for name, st, tau in cases_fpf():
    invol = all(tau[tau[z]] == z for z in st)
    fpf = all(tau[z] != z for z in st)
    ok1 &= invol and fpf
    for enum in ({z: k for k, z in enumerate(st)}, {z: len(st) - 1 - k for k, z in enumerate(st)}):
        for a in st:
            ob = kernel_objects(st, tau, a, enum)
            const_phase = all(sp.simplify(p - 1 / q) == 0 for p in ob['phase'])
            lhs = ob['Ph'] * ob['G'] * (ob['D'] * ob['G'] * ob['D'])
            iso = zero_mat(lhs - ob['flow'])
            scal = zero_mat(ob['G'] * ob['D'] * ob['G'] * ob['D'] - q * ob['flow'])
            ok1 &= const_phase and iso and scal
            n_id += 1
            # Z2: the sign diagonal as a product of squared quarter phases
            N = len(st)
            prod = sp.eye(N)
            for k, s in enumerate(ob['sign']):
                if s == -1:
                    prod = prod * phase_gate(N, k) ** 2
            ok2 &= (prod - ob['D']) == sp.zeros(N, N)
            ok2 &= (phase_gate(N, 0) ** 4) == sp.eye(N)
check('Z1', ok1, f'{len(cases_fpf())} fixed-point-free carriers, {n_id} (a, enumeration) cases: involution without fixed points, '
                 f'phaseFun = 1/q constant, isolation identity exact, G D G D = q * flow')
check('Z2', ok2, 'every sign diagonal = product of squared quarter phases; phaseGate^4 = 1')

# ------------------------------------------------------------------ Z3 (textual reading at L)
def src(path):
    return subprocess.run(['git', '-C', REPO, 'show', f'{L}:verification/lean-mathlib/OIBridge/{path}'],
                          capture_output=True, text=True, check=True).stdout


routeB = src('RouteB.lean')
minrep = src('MinimalRepertoire.lean')
reach = src('ReachabilitySeam.lean')
lift = src('LiftAudit.lean')
z3 = {}
z3['phases'] = re.search(r'def PhasesAvailable \(T : FiniteOperationalTheory A\) : Prop :=\s*'
                         r'∀ \(n : ℕ\) \(a : A × Fin n\), T\.availExt n Unit \(fun _ => conjChannel \(phaseGate a\)\)', routeB) is not None
z3['exchanges'] = re.search(r'def ExchangesAvailable \(T : FiniteOperationalTheory A\) : Prop :=\s*'
                            r'∀ \(n : ℕ\) \(a b : A × Fin n\),\s*T\.availExt n Unit \(fun _ => conjChannel \(permMatrix \(Equiv\.swap a b\)\)\)', routeB) is not None
z3['derivedOI'] = re.search(r'def DerivedOI \(T : FiniteOperationalTheory A\) : Prop :=\s*'
                            r'ReversibleImplementationLocality T ∧ EmbeddedObservation T\s*∧ ExchangesAvailable T ∧ PhasesAvailable T ∧ ReadWriteAvailable T', routeB) is not None
z3['pfr_exchange_distinct'] = re.search(r'∧ \(∀ a b : A × Fin n, a ≠ b →\s*T\.availExt n Unit \(fun _ => conjChannel \(permMatrix \(Equiv\.swap a b\)\)\)\)', minrep) is not None
z3['smul'] = re.search(r'theorem conjChannel_smul \{lam : ℂ\} \(h : ‖lam‖ = 1\) \(V : Matrix S S ℂ\) :\s*conjChannel \(lam • V\) = conjChannel V', reach) is not None
m = re.search(r'theorem avail_conj_mul(.*?):= by', lift, re.S)
z3['conj_mul_no_sub'] = m is not None and 'SubstratumAvail' not in m.group(1) and 'hsub' not in m.group(1)
for nm in ('diagonal_avail', 'phaseFree_of_layerFlowExecutable', 'derivedOI_qm_iff_layerFlowExecutable'):
    mm = re.search(r'theorem ' + nm + r' (.*?)(:= by|:=\n)', lift, re.S)
    z3[nm + '_needs_sub'] = mm is not None and 'SubstratumAvail' in mm.group(1)
check('Z3', all(z3.values()), ', '.join(f'{k}: {v}' for k, v in z3.items()))

# ------------------------------------------------------------------ Z4 and CC1
st3 = [(x, 0) for x in range(3)]
tau3 = {(0, 0): (1, 0), (1, 0): (0, 0), (2, 0): (2, 0)}
enum3 = {z: k for k, z in enumerate(st3)}
ob3 = kernel_objects(st3, tau3, (0, 0), enum3)
iso3 = zero_mat(ob3['Ph'] * ob3['G'] * (ob3['D'] * ob3['G'] * ob3['D']) - ob3['flow'])
const3 = all(sp.simplify(p - ob3['phase'][0]) == 0 for p in ob3['phase'])
GDGD = ob3['G'] * ob3['D'] * ob3['G'] * ob3['D']
F3 = ob3['flow']
r00 = sp.simplify(GDGD[0, 0] / F3[0, 0])
r22 = sp.simplify(GDGD[2, 2] / F3[2, 2])
not_prop = sp.simplify(r00 - r22) != 0
check('Z4', iso3 and (not const3) and not_prop,
      f'Fin 3 swap(0,1): kernel identity {iso3}; phaseFun constant {const3}; ratio at (0,0) {r00}, at (2,2) {r22}')
countercontrol('CC1', const3, 'phaseFun is constant on the Fin 3 carrier')

# ------------------------------------------------------------------ Z5 and CC2
random.seed(20261011)


def rgauss():
    return sp.Rational(random.randint(-5, 5), random.randint(1, 4)) + I * sp.Rational(random.randint(-5, 5), random.randint(1, 4))


def ptrace_last(M, d, m):
    out = sp.zeros(d, d)
    for i in range(d):
        for j in range(d):
            out[i, j] = sum(M[i * m + k, j * m + k] for k in range(m))
    return out


ok5 = True
cc2 = False
for n in (1, 2):
    d = 2 * n
    for _ in range(3):
        V = sp.Matrix(d, d, lambda i, j: rgauss())
        rho = sp.Matrix(d, d, lambda i, j: rgauss())
        big = sp.kronecker_product(V, sp.eye(2))
        att = sp.kronecker_product(rho, sp.eye(2) / 2)
        res = ptrace_last(big * att * big.H, d, 2)
        ok5 &= sp.simplify(res - V * rho * V.H) == sp.zeros(d, d)
        att1 = sp.kronecker_product(rho, sp.eye(2))
        res1 = ptrace_last(big * att1 * big.H, d, 2)
        cc2 |= sp.simplify(res1 - V * rho * V.H) == sp.zeros(d, d)
    # associator: index ((x, y), k) <-> (x, (y, k)); 1 (x) (U (x) 1_n) vs (1 (x) U) (x) 1_n
    U = sp.Matrix(2, 2, lambda i, j: rgauss())
    A = sp.kronecker_product(sp.eye(2), sp.kronecker_product(U, sp.eye(n)))  # index (x, (y, k)) = x*2n + y*n + k
    B = sp.kronecker_product(sp.kronecker_product(sp.eye(2), U), sp.eye(n))  # index ((x, y), k) = (x*2 + y)*n + k
    ok5 &= (A - B) == sp.zeros(4 * n, 4 * n)  # the two flattenings coincide: the associator is the identity relabelling
check('Z5', ok5, 'discard over a uniformly attached two-level ancilla returns V rho V^* (n = 1, 2, three exact samples each); '
                 'associator identity entrywise')
countercontrol('CC2', cc2, 'the discard with the ancilla attached as 1_2 returns V rho V^*')

# ------------------------------------------------------------------ Paulis, dictionary, actT
X2 = sp.Matrix([[0, 1], [1, 0]])
Y2 = sp.Matrix([[0, -I], [I, 0]])
Z2m = sp.Matrix([[1, 0], [0, -1]])
E2 = sp.eye(2)
SIG = [E2, X2, Y2, Z2m]
PT = [[sp.kronecker_product(SIG[m_], SIG[n_]) for n_ in range(4)] for m_ in range(4)]


def dict_(w):
    out = sp.zeros(4, 4)
    for m_ in range(4):
        for n_ in range(4):
            if w[m_][n_] != 0:
                out += sp.Rational(1, 4) * w[m_][n_] * PT[m_][n_]
    return out


def coordOf(H):
    return [[sp.re(sp.simplify((PT[m_][n_] * H).trace())) for n_ in range(4)] for m_ in range(4)]


def hom(N):
    H = sp.eye(4)
    for a_ in range(3):
        for b_ in range(3):
            H[a_ + 1, b_ + 1] = N[a_, b_]
    return H


def actT(N, w):
    W = sp.Matrix(w) * hom(N).T
    return [[W[i, j] for j in range(4)] for i in range(4)]


def rotZ(c, s):
    return sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


CYC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
w = sp.Rational(3, 5) + I * sp.Rational(4, 5)
zPh = sp.diag(1, w)
UJ = (E2 - I * (X2 + Y2 + Z2m)) / 2

# ------------------------------------------------------------------ Z6
abs1 = sp.simplify(w * sp.conjugate(w)) == 1
w4 = sp.expand(w ** 4)
w4ok = w4 == sp.Rational(-527, 625) - I * sp.Rational(336, 625)
pw = sp.Integer(1)
noroot = True
for k in range(1, 1001):
    pw = sp.expand(pw * w)
    if pw == 1:
        noroot = False
        break
UJunit = sp.simplify(UJ * UJ.H - E2) == sp.zeros(2, 2)
UJ3 = sp.simplify(UJ ** 3)
UJ3scalar = UJ3[0, 1] == 0 and UJ3[1, 0] == 0 and sp.simplify(UJ3[0, 0] - UJ3[1, 1]) == 0
check('Z6', abs1 and w4ok and noroot and UJunit and UJ3scalar,
      f'|w| = 1: {abs1}; w^4 = {w4}; w^k != 1 for k <= 1000: {noroot}; U_J unitary: {UJunit}; U_J^3 = {UJ3[0, 0]} * 1')

# ------------------------------------------------------------------ Z7
def basis_table(m_, n_):
    return [[(1 if (r, c) == (m_, n_) else 0) for c in range(4)] for r in range(4)]


ok7 = True
for (U, N) in ((zPh, rotZ(sp.Rational(3, 5), sp.Rational(4, 5))), (UJ, CYC)):
    W1 = sp.kronecker_product(E2, U)
    for m_ in range(4):
        for n_ in range(4):
            bt = basis_table(m_, n_)
            lhs = coordOf(W1 * dict_(bt) * W1.H)
            rhs = actT(N, bt)
            ok7 &= all(sp.simplify(lhs[i][j] - rhs[i][j]) == 0 for i in range(4) for j in range(4))
check('Z7', ok7, 'Ad(1 (x) diag(1, w)) = actT R_z(3/5, 4/5) and Ad(1 (x) U_J) = actT cyc on the 16 basis tables')

# ------------------------------------------------------------------ Z8, CC3, CC4
SGN = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def psi_archive(s):
    s1, s2 = s
    return sp.Matrix([1, s1 * s2, s1, -s2]) / 2


_PSI = {}


def psi(s):
    """The defect vector of e_s in THIS dictionary: the unit vector spanning ker(dict(e_s) + 1/8), computed exactly.
    (Run 1 used psi_archive, the archive's formula, whose tensor convention differs from this dictionary's; see
    RUN-HISTORY.)"""
    if s not in _PSI:
        ns = (dict_(e_table(s)) + sp.eye(4) / 8).nullspace()
        assert len(ns) == 1
        v = ns[0]
        nrm2 = sp.simplify((v.H * v)[0, 0])
        k = next(i for i in range(4) if v[i] != 0)
        v = v / v[k]                      # first nonzero entry 1
        nrm2 = sp.simplify((v.H * v)[0, 0])
        _PSI[s] = (v, nrm2)
    return _PSI[s]


def proj(s):
    v, nrm2 = psi(s)
    return v * v.H / nrm2


def e_table(s):
    s1, s2 = s
    t = [[0] * 4 for _ in range(4)]
    t[0][0], t[1][3], t[2][2], t[3][1] = sp.Rational(1, 4), sp.Rational(s1, 4), sp.Rational(s2, 4), sp.Rational(-s1 * s2, 4)
    return t


dict_e_ok = all(sp.simplify(dict_(e_table(s)) - (sp.eye(4) - 2 * proj(s)) / 8) == sp.zeros(4, 4) for s in SGN)
bell_orth = all(sp.simplify((psi(a_)[0].H * psi(b_)[0])[0, 0]) == 0 for a_, b_ in itertools.combinations(SGN, 2))
archive_conv = all(sp.simplify(dict_(e_table(s)) - (sp.eye(4) - 2 * psi_archive(s) * psi_archive(s).H) / 8) == sp.zeros(4, 4) for s in SGN)
print(f'      (dictionary convention: archive psi_s formula reproduces dict(e_s): {archive_conv}; '
      f'computed defect vectors {[list(psi(s_)[0]) for s_ in SGN]}, pairwise orthogonal: {bell_orth})')


def certificates(U):
    """All (s, label, value) with y = P_phi (phi in F_U) in Q3 cap Z* and tr(y Ad(1 (x) U) dict(e_s)) = value < 0."""
    W1 = sp.kronecker_product(E2, U)
    out = []
    for s in SGN:
        Xs = W1 * dict_(e_table(s)) * W1.H
        fam = []
        for a_, b_ in itertools.permutations(SGN, 2):
            for chi in (1, -1, I, -I):
                va, na = psi(a_)
                vb, nb = psi(b_)
                phi = va / sp.sqrt(na) + chi * vb / sp.sqrt(nb)
                fam.append(((a_, b_, chi), sp.simplify(phi * phi.H / 2)))
        R = W1 * psi(s)[0]
        fam.append((('image', s), sp.simplify(R * R.H / psi(s)[1])))
        for lab, Py in fam:
            inZstar = all(sp.simplify((Py * dict_(e_table(t_))).trace()) >= 0 for t_ in SGN)
            if not inZstar:
                continue
            val = sp.nsimplify(sp.simplify((Py * Xs).trace()))
            if val < 0:
                out.append((s, lab, val))
    return out


cz = certificates(zPh)
cj = certificates(UJ)
c1 = certificates(E2)
cx = certificates(X2)
minz = min((c[2] for c in cz), default=None)
minj = min((c[2] for c in cj), default=None)
check('Z8', dict_e_ok and bell_orth and len(cz) > 0 and len(cj) > 0 and minz == sp.Rational(-1, 10) and minj == sp.Rational(-1, 8),
      f'dict(e_s) = (1 - 2 P_s)/8: {dict_e_ok}; certificates for R_z(theta0): {len(cz)} (min pairing {minz}, '
      f'e.g. {cz[0] if cz else None}); for J: {len(cj)} (min pairing {minj}, e.g. {cj[0] if cj else None})')
countercontrol('CC3', len(c1) > 0, f'Ad(1 (x) 1) moves K(Z_F) within the family ({len(c1)} certificates)')
countercontrol('CC4', len(cx) > 0, f'Ad(1 (x) X) moves K(Z_F) within the family ({len(cx)} certificates)')

# ------------------------------------------------------------------ Z9, CC5
R = rotZ(sp.Rational(3, 5), sp.Rational(4, 5))
Pw = sp.eye(3)
fin = False
for k in range(1, 1001):
    Pw = Pw * R
    if Pw == sp.eye(3):
        fin = True
        break
comm = (R * CYC - CYC * R) == sp.zeros(3, 3)
check('Z9', (not fin) and (not comm), f'R_z(theta0)^k != 1 for k <= 1000: {not fin}; actT R_z(theta0) and actT cyc commute: {comm}')
countercontrol('CC5', comm, 'actT R_z(theta0) commutes with actT cyc')

# ------------------------------------------------------------------ Z10, CC6
u, v, t = sp.symbols('u v t', real=True)


def Uuv(a_, b_):
    return sp.diag(sp.exp(I * a_), sp.exp(-I * a_), sp.exp(I * b_), sp.exp(-I * b_))


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control token A (first factor), target B
XB = sp.kronecker_product(E2, X2)
g1a = sp.simplify(CNOT * Uuv(u, v) * CNOT - Uuv(u, -v)) == sp.zeros(4, 4)
g1b = sp.simplify(XB * Uuv(u, v) * XB - Uuv(-u, -v)) == sp.zeros(4, 4)
g1c = (CNOT * XB == XB * CNOT) and (CNOT * CNOT == sp.eye(4)) and (XB * XB == sp.eye(4))
D1 = sp.kronecker_product(E2, sp.diag(1, sp.exp(I * t)))
g1d = sp.simplify(D1 - sp.exp(I * t / 2) * Uuv(-t / 2, -t / 2)) == sp.zeros(4, 4)
g1e = sp.simplify(CNOT * D1 * CNOT - sp.exp(I * t / 2) * Uuv(-t / 2, t / 2)) == sp.zeros(4, 4)
check('Z10', g1a and g1b and g1c and g1d and g1e,
      f'CNOT U(u,v) CNOT = U(u,-v): {g1a}; X_B U X_B = U(-u,-v): {g1b}; commute and involutive: {g1c}; '
      f'1 (x) diag(1, e^it) = e^(it/2) U(-t/2,-t/2): {g1d}; its CNOT conjugate e^(it/2) U(-t/2, t/2): {g1e}')
cc6 = sp.simplify(CNOT * Uuv(u, v) * CNOT - Uuv(v, u)) == sp.zeros(4, 4)
countercontrol('CC6', cc6, 'CNOT U(u, v) CNOT = U(v, u) identically')

# ------------------------------------------------------------------ Z11
hs = sp.symbols('a0 b0 a1 b1 a2 b2 a3 b3', real=True)
h = sp.Matrix([hs[0] + I * hs[1], hs[2] + I * hs[3], hs[4] + I * hs[5], hs[6] + I * hs[7]])
lhs11 = (h.H * Uuv(u, v) * XB * h)[0, 0]
rhs11 = 2 * sp.re(sp.conjugate(h[0]) * h[1] * sp.exp(I * u)) + 2 * sp.re(sp.conjugate(h[2]) * h[3] * sp.exp(I * v))
g3 = sp.simplify(sp.expand_complex(lhs11 - rhs11)) == 0
hi = sp.Matrix([1, 1, 2, I])
inst = sp.simplify((hi.H * sp.diag(I, -I, 1, 1) * XB * hi)[0, 0])
check('Z11', g3 and inst == 0, f'orthogonality identity symbolic: {g3}; instance <h | diag(i,-i,1,1) X_B h> = {inst}')

# ------------------------------------------------------------------ Z12, CC7
def det2(vec):
    return vec[0] * vec[3] - vec[1] * vec[2]


hv = sp.Matrix(sp.symbols('h00 h01 h10 h11'))
d12 = sp.simplify(det2(Uuv(u, v) * hv) - (sp.exp(I * (u - v)) * hv[0] * hv[3] - sp.exp(I * (v - u)) * hv[1] * hv[2])) == 0


def unequal(vec):
    return sp.Abs(vec[0] * vec[3]) != sp.Abs(vec[1] * vec[2])


seed = sp.Matrix([2, 1, 1, 0])
comps = [seed, CNOT * seed, XB * seed, CNOT * XB * seed]
pf = all(unequal(c) for c in comps)
cc7 = not pf
cseed = sp.Matrix([1, 2, 2, -4])
reach0 = sp.simplify(det2(sp.diag(I, -I, 1, 1) * cseed)) == 0
check('Z12', d12 and pf and reach0, f'determinant law symbolic: {d12}; (2,1,1,0) product-free on the four components: {pf}; '
                                     f'(1,2,2,-4) reaches a product at diag(i,-i,1,1): {reach0}')
countercontrol('CC7', cc7, 'the G-orbit of (2, 1, 1, 0) contains a product')

# ------------------------------------------------------------------ verdict
fails = [k for k, ok_ in results.items() if not ok_]
bad_cc = [k for k, val in ccs if val]
print()
print('CHECKS: PASS', [k for k, ok_ in results.items() if ok_], 'FAIL', fails)
print('COUNTERCONTROLS:', ccs)
print('VERDICT', 'INDEP-B5-FIXED' if not fails and not bad_cc else 'INDEP-B5-FAILED ' + ' '.join(fails + bad_cc))
