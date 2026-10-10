#!/usr/bin/env python3
"""Thread X (EXOT), node X1(a)/(c) -- exact ingredients of the class results (orthogonal images; indecomposability).

Run (cwd pt/X/): python3 -I -B x6_orth.py > x6_orth.out 2> x6_orth.err

Written argument (RESULT 1, X1(a)): if Psi is ipW-orthogonal with SEP <= Psi(Q3), then Phi = Psi^-1 fixes I and maps
pure products to pure states (S3 ORTH.W, audited); M_A(X) = Phi(X (x) I), M_B(Y) = Phi(I (x) Y) are unital Jordan
maps Herm(2) -> Herm(4); S_i = M_A(sigma_i) are anticommuting Hermitian involutions, and C^4 splits into the +-1
eigenspaces of -i S1 S2 S3, carrying sigma_i (x) I_k and sigma_i^T (x) I_l; Phi(X (x) Y) = M_A(X) M_B(Y) with commuting
images. Checked exactly here:
  O1  the Jordan product of Herm(2) is not associative: (sx o sx) o sz != sx o (sx o sz) (used to exclude a
      commutative image of an injective Jordan map);
  O2  commutant dimensions in M4(C): of {sigma_i (x) I}: 4; of {sigma_i^T (x) I}: 4; of {sigma_i (+) sigma_i^T}: 2
      (so in the mixed case M_B would land in C (+) C, which holds no anticommuting involutions);
  O3  for the three models, -i S1 S2 S3 = +I, -I, diag(I, -I) respectively, and each triple consists of
      anticommuting Hermitian involutions;
  O4  T_A(Q3) = T_B(Q3): pauliW(T_A w) = pauliW(T_B w)^T and pauliW(T w) = pauliW(w)^T (symbolic), so the images
      Phi^-1(Q3) = tau(Q3), tau in {id, T_A, T_B, T}, are exactly Q3 and twin = actT reflY Q3;
  O5  (indecomposability ingredient) for u = (1,0,0,-1), l = (1,0,0,1), e1, e2 (a = e3 without loss of generality):
      x = alpha u + beta l + g1 e1 + g2 e2 has x0^2 - |x'|^2 = 4 alpha beta - g1^2 - g2^2 (symbolic).
Countercontrol:
  Oc  the test 'Psi^-1(p) in Q3 for every axis product p' rejects the ipW-reflection R(w) = w - 2 <E11, w> E11
      (an orthogonal map with R(Q3) self-dual): R(prodState(e1, e1)) has pauliW with eigenvalue -1/2;
      and accepts cnot and actT reflY (their inverse images of the 36 axis products are PSD).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check, tagged (identity, enumerate, witness, countercontrol).
  R2. A countercontrol PASSES iff the test REJECTS the control object (and accepts the positive controls named).
  R3. VERDICT only if all checks pass; else 'X6-ORTH: FAILED -- <ids>' and exit 1.
  R4. Exact arithmetic only (sympy); no floating point or randomness.
"""
import sys
from itertools import product

import sympy as sp

R4 = range(4)
iu = sp.I
CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def mzero(M):
    return all(sp.expand(v) == 0 for v in M)


SIG = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in R4] for m in R4]


def jor(a, b):
    return (a * b + b * a) / 2


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def commutant_dim(mats):
    zs = sp.symbols('z0:32', real=True)
    Z = sp.Matrix(4, 4, lambda i, j: zs[2 * (4 * i + j)] + iu * zs[2 * (4 * i + j) + 1])
    eqs = []
    for A in mats:
        C = A * Z - Z * A
        for v in C:
            v = sp.expand(v)
            eqs += [sp.re(v), sp.im(v)]
    M = sp.Matrix([[sp.diff(e, z) for z in zs] for e in eqs])
    return (32 - M.rank()) // 2           # complex dimension (the solution space is a complex subspace)


# =====================================================================================================
section('O  the Jordan / Clifford ingredients')
sx, sz = SIG[1], SIG[3]
chk('O1', 'Herm(2) Jordan product is not associative: (sx o sx) o sz = sz but sx o (sx o sz) = 0',
    jor(jor(sx, sx), sz) == sz and jor(sx, jor(sx, sz)) == sp.zeros(2, 2), 'identity')
A_std = [sp.kronecker_product(SIG[i], SIG[0]) for i in (1, 2, 3)]
A_tr = [sp.kronecker_product(SIG[i].T, SIG[0]) for i in (1, 2, 3)]
A_mix = [sp.diag(SIG[i], SIG[i].T) for i in (1, 2, 3)]
dims = [commutant_dim(A_std), commutant_dim(A_tr), commutant_dim(A_mix)]
print(f"INFO commutant complex dimensions: std {dims[0]}, transposed {dims[1]}, mixed {dims[2]}")
chk('O2', 'commutant dimensions in M4(C): {s_i (x) I}: 4, {s_i^T (x) I}: 4, {s_i (+) s_i^T}: 2', dims == [4, 4, 2],
    'enumerate')


def clifford_ok(S):
    inv = all(mzero(s * s - sp.eye(4)) and mzero(s - s.H) for s in S)
    anti = all(mzero(S[i] * S[j] + S[j] * S[i]) for i in range(3) for j in range(3) if i != j)
    return inv and anti


sig_std = -iu * A_std[0] * A_std[1] * A_std[2]
sig_tr = -iu * A_tr[0] * A_tr[1] * A_tr[2]
sig_mix = -iu * A_mix[0] * A_mix[1] * A_mix[2]
chk('O3', 'each model is a triple of anticommuting Hermitian involutions, with -i S1 S2 S3 = I, -I, '
    'diag(1,1,-1,-1) respectively', all(clifford_ok(S) for S in (A_std, A_tr, A_mix))
    and mzero(sig_std - sp.eye(4)) and mzero(sig_tr + sp.eye(4)) and mzero(sig_mix - sp.diag(1, 1, -1, -1)),
    'identity')
wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
sA, sB = sp.diag(1, 1, -1, 1), sp.diag(1, 1, -1, 1)
TA = lambda w: sA * w                      # actC reflY: transpose on the control (Y -> -Y)
TB = lambda w: w * sB                      # actT reflY: transpose on the target
chk('O4', 'pauliW(T_A w) = pauliW(T_B w)^T and pauliW(T_A T_B w) = pauliW(w)^T, symbolic: T_A(Q3) = T_B(Q3) = twin '
    'and the full transpose preserves Q3', mzero(pauliW(TA(wsym)) - pauliW(TB(wsym)).T)
    and mzero(pauliW(TA(TB(wsym))) - pauliW(wsym).T), 'identity')
al, be, g1, g2 = sp.symbols('alpha beta g1 g2', real=True)
xv = al * sp.Matrix([1, 0, 0, -1]) + be * sp.Matrix([1, 0, 0, 1]) + g1 * sp.Matrix([0, 1, 0, 0]) + g2 * sp.Matrix([0, 0, 1, 0])
chk('O5', 'x = alpha u + beta l + g1 e1 + g2 e2 (u = (1,0,0,-1), l = (1,0,0,1)): x0^2 - |x\'|^2 = 4 alpha beta - '
    'g1^2 - g2^2, symbolic', sp.expand(xv[0] ** 2 - xv[1] ** 2 - xv[2] ** 2 - xv[3] ** 2
                                       - (4 * al * be - g1 ** 2 - g2 ** 2)) == 0, 'identity')

# =====================================================================================================
section('Oc  countercontrol: an orthogonal map with self-dual image that does not contain SEP')
SGN_NEG = {(1, 3), (2, 2)}
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
cnot = lambda w: sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in SGN_NEG else 1) * w[PC[m][n], PT[m][n]])
E11 = sp.zeros(4, 4)
E11[1, 1] = 1
refl = lambda w: w - 2 * w[1, 1] * E11
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
PRODS = [sp.Matrix([1] + list(a)) * sp.Matrix([1] + list(b)).T for a, b in product(AX, AX)]


def psd(M):
    return all(ev >= 0 for ev in M.eigenvals())


bad = refl(PRODS[0])
chk('Oc', 'the inverse-image test rejects the reflection R (R^-1 = R): pauliW(R(prodState(e1, e1))) has eigenvalue '
    '-1/2; it accepts cnot and actT reflY (inverse images of all 36 axis products are PSD)',
    sp.Rational(-1, 2) in pauliW(bad).eigenvals() and all(psd(pauliW(cnot(p))) for p in PRODS)
    and all(psd(pauliW(TB(p))) for p in PRODS), 'countercontrol')

# =====================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'enumerate', 'witness', 'countercontrol')), flush=True)
if failed:
    print(f"X6-ORTH: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT X6-ORTH-EXACT -- {len(CHECKS)} checks', flush=True)
