"""E9 probe -- the Level III converse: exact finite-stage instances.  (exact; sympy rationals and Gaussian rationals)

QUESTION.  Level III (QuasilocalCharacterization.lean at L) proves uniqueness: the canonical map is the unique continuous
stage-compatible map (canon_unique :359) and OI systems with one substratum dynamics are isomorphic compatibly with their
automorphisms (systemEquiv_dyn :497).  The converse direction would derive the OI_Q conditions -- matrix-algebra stages
Matrix (Conf L Q) with inclusions X -> X (x) 1, commuting disjoint regions, uniform site type Q, and dynamics transported
from a reversible finite-range configuration map -- from "a quasilocal system carrying stages and a dynamics".  This
probe checks, on exact finite instances, which parts of that converse fail and which hypotheses repair it.

CHECKS (2 sites unless stated; Q = {0, 1}; configurations ordered 00, 01, 10, 11; site 0 is the left tensor factor).
  P1  dynamics, phase: the stage map X -> U X U* with U = diag(w), w(f) = i if f(site 0) = 0 else 1 (the kernel's
      phaseWt), is a unital *-automorphism of every stage, compatible with X -> X (x) 1, maps each region's algebra into
      itself; on the single-site matrix unit E_01 it gives an entry i, while every permutation transport P (E_01 (x) 1) P^T
      (all 24 permutations P of the four configurations) has entries in {0, 1}: no configuration bijection induces it.
  P2  dynamics, sign: conjugation by Z = diag(1, -1) at site 0 is real (commutes with entrywise conjugation), preserves
      the diagonal (configuration) algebra, is compatible with X -> X (x) 1, maps each region's algebra into itself, and
      gives -E_01: no permutation transport has a -1 entry.  Reality and diagonal preservation do not characterize the
      OI-induced dynamics.
  K1  kinematics, classical lattice: the diagonal algebras D_L (functions of configurations) form an isotone, local,
      generating net with a locality-preserving automorphism (the site swap); D is commutative, while [E_01, E_10] =
      diag(1, -1) != 0 in M_2, so no injective unital *-homomorphism M_q -> D exists for q >= 2 (its image of the
      commutator would be 0).  The net is not a member of QuasilocalSystem for any Q with |Q| >= 2.
  K2  kinematics, graded locality: Jordan-Wigner a0 = s- (x) 1, a1 = Z (x) s- on C^4 satisfy the CAR exactly; the site
      algebras alg(a0), alg(a1) have dimension 4 each and generate M_4 (dimension 16); a0 a1 = -a1 a0 != a1 a0, so the
      fermionic net fails local_comm; its even parts commute (graded locality).
  K3  kinematics, non-uniform sites: a qubit site and a qutrit site give single-site stage dimensions 4 and 9; every member
      of QuasilocalSystem iota Q has every single-site stage of dimension |Q|^2, so no uniform Q presents the net with
      its regions.
  T1  the converse at one finite level, under the repairing hypotheses (factor stages, commuting, generating, uniform):
      for an exact rational orthogonal U (a Householder reflection), the copies phi1(X) = U (X (x) 1) U^T and
      phi2(Y) = U (1 (x) Y) U^T commute, are unital and injective, and the 16 products phi1(E_ij) phi2(E_kl) are linearly
      independent (rank 16): the multiplication map M_2 (x) M_2 -> M_4 is a unital *-isomorphism (an instance of the
      tensor-product theorem for commuting factors, [L]).
  T2  countercontrol for T1: with the fermionic copies of K2 (alg(a0) ~ M_2 via the matrix units a0* a0, a0*, a0, a0 a0*,
      and likewise a1), the 16 products still span M_4 (rank 16), but the multiplication map is not multiplicative:
      phi1(X1) phi2(Y1) phi1(X2) phi2(Y2) != phi1(X1 X2) phi2(Y1 Y2) for X1 = Y2 = e01, X2 = Y1 = e10 (the two sides
      differ by a sign) -- commutation, not generation, carries the tensor identification.

DECISION RULE (fixed before run 1).  VERDICT LEVEL3-CONVERSE-BOUNDED is printed iff every check P1, P2, K1, K2, K3, T1, T2
passes.  Otherwise the verdict line is "VERDICT NOT RENDERED" followed by the failing checks.  The verdict says only:
on these finite instances the naive converse fails at the dynamics (P1, P2) and at the kinematics (K1-K3), and the
repaired converse holds on the instance T1 with commutation load-bearing (T2).  It proves nothing about infinite regions,
and nothing about the general tensor-product theorem, which is a literature input.
"""
import itertools
import sys

import sympy as sp

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''))


I = sp.I


def unit(n, i, j):
    M = sp.zeros(n, n)
    M[i, j] = 1
    return M


def kron(A, B):
    return sp.kronecker_product(A, B)


def span_rank(mats):
    rows = [list(M.reshape(1, M.rows * M.cols)) for M in mats]
    return sp.Matrix(rows).rank()


I2 = sp.eye(2)
E = {(i, j): unit(2, i, j) for i in range(2) for j in range(2)}
Z = sp.diag(1, -1)
sminus = unit(2, 1, 0)  # |1><0|

# ---------------- P1: the phase stage automorphism ----------------
w1 = [I, 1]                        # one site: w(f) = i if f = 0
U1 = sp.diag(*w1)
w2 = [I if f[0] == 0 else 1 for f in itertools.product(range(2), repeat=2)]
U2 = sp.diag(*w2)


def conj_by(U, X):
    return sp.simplify(U * X * U.H)


ok_unitary = sp.simplify(U1 * U1.H) == sp.eye(2) and sp.simplify(U2 * U2.H) == sp.eye(4)
ok_compat = all(sp.simplify(conj_by(U2, kron(E[k], I2)) - kron(conj_by(U1, E[k]), I2)) == sp.zeros(4, 4) for k in E)
# maps the site-0 algebra M_2 (x) 1 into itself and fixes the site-1 algebra 1 (x) M_2
ok_local = all(sp.simplify(conj_by(U2, kron(I2, E[k])) - kron(I2, E[k])) == sp.zeros(4, 4) for k in E)
ok_mult = all(sp.simplify(conj_by(U1, E[a] * E[b]) - conj_by(U1, E[a]) * conj_by(U1, E[b])) == sp.zeros(2, 2)
              for a in E for b in E)
img = conj_by(U1, E[(0, 1)])
ok_i = img[0, 1] == I
perms_entries = set()
for p in itertools.permutations(range(4)):
    P = sp.zeros(4, 4)
    for c, r in enumerate(p):
        P[r, c] = 1
    T = P * kron(E[(0, 1)], I2) * P.T
    perms_entries |= set(T)
ok_real01 = perms_entries <= {0, 1}
check('P1', ok_unitary and ok_compat and ok_local and ok_mult and ok_i and ok_real01,
      'phase image of E_01 has entry %s; permutation transports of E_01 (x) 1 take entries %s' % (img[0, 1], sorted(perms_entries)))

# ---------------- P2: the sign stage automorphism ----------------
ZZ = kron(Z, I2)
ok_real = all(conj_by(Z, E[k]).conjugate() == conj_by(Z, E[k].conjugate()) for k in E)
ok_diag = all(conj_by(ZZ, kron(E[(a, a)], E[(b, b)])) == kron(E[(a, a)], E[(b, b)]) for a in range(2) for b in range(2))
ok_compat2 = all(sp.simplify(conj_by(ZZ, kron(E[k], I2)) - kron(conj_by(Z, E[k]), I2)) == sp.zeros(4, 4) for k in E)
ok_local2 = all(conj_by(ZZ, kron(I2, E[k])) == kron(I2, E[k]) for k in E)
sign_img = conj_by(Z, E[(0, 1)])
ok_minus = sign_img[0, 1] == -1 and -1 not in perms_entries
check('P2', ok_real and ok_diag and ok_compat2 and ok_local2 and ok_minus,
      'sign image of E_01 has entry %s; real, diagonal-preserving, local; no permutation transport has -1' % sign_img[0, 1])

# ---------------- K1: the classical lattice ----------------
D1 = [kron(E[(a, a)], I2) for a in range(2)]
D2 = [kron(I2, E[(b, b)]) for b in range(2)]
ok_comm = all(A * B == B * A for A in D1 + D2 for B in D1 + D2)
gen = [A * B for A in D1 for B in D2]
ok_gen = span_rank(gen) == 4          # the diagonal algebra of C^4 has dimension 4
SWAP = sp.zeros(4, 4)
for a in range(2):
    for b in range(2):
        SWAP[2 * b + a, 2 * a + b] = 1
ok_shift = all(SWAP * A * SWAP.T in [*D2] for A in D1)
commutator = E[(0, 1)] * E[(1, 0)] - E[(1, 0)] * E[(0, 1)]
check('K1', ok_comm and ok_gen and ok_shift and commutator == Z,
      'diagonal net commutative, generating (rank 4), site swap local; [E_01, E_10] = diag(1, -1) != 0 in M_2')

# ---------------- K2: graded locality (Jordan-Wigner) ----------------
a0 = kron(sminus, I2)
a1 = kron(Z, sminus)
ad = [a0.H, a1.H]
aa = [a0, a1]
ok_car = all((aa[i] * ad[j] + ad[j] * aa[i]) == (sp.eye(4) if i == j else sp.zeros(4, 4)) for i in range(2) for j in range(2)) \
    and all((aa[i] * aa[j] + aa[j] * aa[i]) == sp.zeros(4, 4) for i in range(2) for j in range(2))
A0 = [a0 * a0.H, a0, a0.H, a0.H * a0]
A1 = [a1 * a1.H, a1, a1.H, a1.H * a1]
ok_dims = span_rank(A0) == 4 and span_rank(A1) == 4
ok_generate = span_rank([x * y for x in A0 for y in A1]) == 16
ok_anti = a0 * a1 == -(a1 * a0) and a0 * a1 != a1 * a0
even0 = [a0 * a0.H, a0.H * a0]
even1 = [a1 * a1.H, a1.H * a1]
ok_even = all(x * y == y * x for x in even0 for y in even1)
check('K2', ok_car and ok_dims and ok_generate and ok_anti and ok_even,
      'CAR exact; site algebras dim 4, 4, generate dim 16; a0 a1 = -a1 a0 != 0; even parts commute')

# ---------------- K3: non-uniform site dimension ----------------
dims = (2 * 2, 3 * 3)
check('K3', dims[0] != dims[1] and dims[0] * dims[1] == 6 * 6,
      'single-site stage dimensions %d and %d, region {0, 1} stage dimension 36 = 4 * 9; a member of QuasilocalSystem iota Q has |Q|^2 at every site' % dims)

# ---------------- T1: the converse at one finite level (an instance) ----------------
v = sp.Matrix([1, 2, 2, 4])                               # Householder reflection, rational and orthogonal
H = sp.eye(4) - 2 * (v * v.T) / (v.T * v)[0, 0]
ok_orth = sp.simplify(H * H.T) == sp.eye(4)
phi1 = {k: H * kron(E[k], I2) * H.T for k in E}
phi2 = {k: H * kron(I2, E[k]) * H.T for k in E}
ok_c = all(sp.simplify(phi1[a] * phi2[b] - phi2[b] * phi1[a]) == sp.zeros(4, 4) for a in E for b in E)
ok_unital = sp.simplify(phi1[(0, 0)] + phi1[(1, 1)]) == sp.eye(4) and sp.simplify(phi2[(0, 0)] + phi2[(1, 1)]) == sp.eye(4)
ok_hom = all(sp.simplify(phi1[(a, b)] * phi1[(c, d)] - (phi1[(a, d)] if b == c else sp.zeros(4, 4))) == sp.zeros(4, 4)
             for (a, b) in E for (c, d) in E)
ok_rank = span_rank([phi1[a] * phi2[b] for a in E for b in E]) == 16
check('T1', ok_orth and ok_c and ok_unital and ok_hom and ok_rank,
      'twisted commuting copies: commute, unital, multiplicative on matrix units, 16 products of rank 16')

# ---------------- T2: countercontrol (fermionic copies) ----------------
# matrix units of alg(a): e00 = a a*, e01 = a, e10 = a*, e11 = a* a  (a = |1><0| (x) ...: a maps |0> to |1>, so a = e10)
f1 = {(0, 0): a0.H * a0, (0, 1): a0.H, (1, 0): a0, (1, 1): a0 * a0.H}
f2 = {(0, 0): a1.H * a1, (0, 1): a1.H, (1, 0): a1, (1, 1): a1 * a1.H}
ok_units = all(f1[(a, b)] * f1[(c, d)] == (f1[(a, d)] if b == c else sp.zeros(4, 4)) for (a, b) in E for (c, d) in E) \
    and all(f2[(a, b)] * f2[(c, d)] == (f2[(a, d)] if b == c else sp.zeros(4, 4)) for (a, b) in E for (c, d) in E)
ok_span = span_rank([f1[a] * f2[b] for a in E for b in E]) == 16
lhs2 = f1[(0, 1)] * f2[(1, 0)] * f1[(1, 0)] * f2[(0, 1)]
rhs2 = (f1[(0, 1)] * f1[(1, 0)]) * (f2[(1, 0)] * f2[(0, 1)])
ok_nonhom = lhs2 != rhs2 and lhs2 == -rhs2 and rhs2 != sp.zeros(4, 4)
check('T2', ok_units and ok_span and ok_nonhom,
      'fermionic copies are matrix-unit systems and span M_4 (rank 16), but phi1(X1)phi2(Y1)phi1(X2)phi2(Y2) != phi1(X1X2)phi2(Y1Y2): %s vs %s'
      % (list(lhs2), list(rhs2)))

fails = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if fails:
    print('VERDICT NOT RENDERED -- failing: ' + ', '.join(fails))
else:
    print('VERDICT LEVEL3-CONVERSE-BOUNDED')
sys.exit(0)
