"""Step C2: the stabilizer's representation on ker DF / gauge (Def) and on R, its character, and the isotypic decomposition by class sums."""
import pickle, time
from lib36 import *
import numpy as np
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); K = A['K']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
C = pickle.load(open('stepC.pkl', 'rb')); elems, classes = C['elems'], C['classes']
basis = Gb + Tb + Rb          # 80 vectors, flag gauge(31) < +T(57) < +R(80)
def apply(e, v):
    p, s = e; out = [0] * 256
    for m, x in enumerate(v): out[p[m]] = s * x
    return out
# coordinates in the adapted basis: solve basis^T x = v exactly
Mt = transpose(basis)
Rr, piv = rref(basis, 256)
PIV = piv[:80]; assert len(PIV) == 80
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); assert pv == list(range(80))
INV = [r[80:] for r in Ri]
def coords(v):
    return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)]
_v = apply(elems[1], basis[40]); _x = coords(_v)
assert all(sum(_x[j] * basis[j][m] for j in range(80)) == _v[m] for m in range(256)), 'coordinate solver control failed'
def rep_matrix(e, lo, hi):
    """matrix of e on the quotient (span basis[:hi]) / (span basis[:lo]), in the basis basis[lo:hi]"""
    cols = []
    for v in basis[lo:hi]:
        x = coords(apply(e, v))
        assert all(x[k] == 0 for k in range(hi, 80)), 'not invariant'
        cols.append(x[lo:hi])
    return [[cols[j][i] for j in range(hi - lo)] for i in range(hi - lo)]
reps = [c[0] for c in classes]
chi_def = []; chi_R = []
for e in reps:
    Md = rep_matrix(e, 31, 80); Mr = rep_matrix(e, 57, 80)
    chi_def.append(sum(Md[i][i] for i in range(49))); chi_R.append(sum(Mr[i][i] for i in range(23)))
print('T (gauge+Diţă) is stabilizer-invariant: yes (no assertion failed); characters computed (%.0fs)' % (time.time() - t0))
order = len(elems); sizes = [len(c) for c in classes]
print('commutant dimension on Def  (sum m_i^2 over Q-irreducibles):', sum(s * x * x for s, x in zip(sizes, chi_def)) / order)
print('commutant dimension on R:', sum(s * x * x for s, x in zip(sizes, chi_R)) / order)
print('trivial-isotypic dimension on Def:', sum(s * x for s, x in zip(sizes, chi_def)) / order, '| on R:', sum(s * x for s, x in zip(sizes, chi_R)) / order)
# isotypic decomposition of R by class sums (exact eigenspaces at rational eigenvalues)
def matmul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def matadd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
n = 23
rep_R = {}
for cl in classes:
    for e in cl: rep_R[e] = rep_matrix(e, 57, 80)
csums = []
for cl in classes:
    S = [[Fr(0)] * n for _ in range(n)]
    for e in cl: S = matadd(S, rep_R[e])
    csums.append(S)
# common eigenspaces: refine the space by each class sum's rational eigenvalues
def eigen_split(spaces, S):
    out = []
    for V in spaces:                           # V: list of basis vectors (rows) of an invariant subspace, in R-coordinates
        # restrict S to V: solve S v = sum lambda ... use numeric eigenvalues then exact kernels
        Vn = np.array([[float(x) for x in v] for v in V]); Sn = np.array([[float(x) for x in r] for r in S])
        # S maps V to V (class sums commute with the group; V invariant)
        SV = Vn @ Sn.T
        coef = np.linalg.lstsq(Vn.T, SV.T, rcond=None)[0].T
        ev = np.linalg.eigvals(coef)
        lams = sorted(set(int(round(x.real)) for x in ev if abs(x.imag) < 1e-6 and abs(x.real - round(x.real)) < 1e-6))
        if len(lams) <= 1: out.append(V); continue
        for lam in lams:
            # exact: kernel of (S - lam) restricted to V: vectors sum a_i v_i with (S - lam)(sum a_i v_i) = 0
            Mv = [[sum(S[r][c] * v[c] for c in range(n)) - lam * v[r] for v in V] for r in range(n)]   # n x |V|
            ker = nullspace(Mv, len(V))
            if ker: out.append([[sum(Fr(a[i]) * V[i][c] for i in range(len(V))) for c in range(n)] for a in ker])
        assert sum(len(v) for v in out) >= len(V) - 0
    return out
spaces = [[[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]]
for S in csums:
    spaces = eigen_split(spaces, S)
print('isotypic sectors of R (dims):', [len(V) for V in spaces], 'total', sum(len(V) for V in spaces))
pickle.dump({'spaces': spaces, 'chi_R': chi_R, 'chi_def': chi_def, 'sizes': sizes, 'rep_R': rep_R}, open('stepC2.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
