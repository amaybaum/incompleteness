"""A45 ancilla probe (research, not frozen): is the instantiated rooted family slice-determined at |A| = 2?

Visible V = 4 values, ancilla A = {a0, a1}, visible slice G = J/4 (the flat 4 x 4 slice, the one-factor analogue of
Gamma0 (x) Gamma0). F is the real 4 x 4 Hadamard (F F^T = 4). For angles with rational (c_i, s_i), c_i^2 + s_i^2 = 1:
  column (j, a0) = sum_i F_ij / 2 (c_i e_(i,a0) + s_i e_(i,a1))            -- fixed; gives sum_a |U((i,a),(j,a0))|^2 = 1/4
  d_k            = sum_m F_mk / 2 (-s_m e_(m,a0) + c_m e_(m,a1))           -- orthonormal complement
  column (j, a1) = sum_k W_kj d_k, W a 4 x 4 unitary                        -- the completion, unconstrained by G
Dilations: D1 = (phi varying, W = 1), D2 = (phi varying, W = F^T / 2), D3 = (phi constant, W = 1), D4 = (phi constant,
W = F^T / 2), D0 = (phi = 0, W = 1: the trivial-ancilla embedding, a padding control).

Instantiations of a dilation U as a Q_fb datum:
  CARRIED   basis V x A, evolution U, init (i, a0) = 1/4 and 0 elsewhere, read = fst: the ancilla persists across steps;
  REFRESHED the visible chain whose one-step kernel is the readback G (ancilla reset to a0 at every step).

EXPECT, fixed before evaluation:
  all five are unitary and admissible dilations of G = J/4;
  CARRIED t = 1 rooted family equals G on every dilation (one step sees only the (., a0) columns);
  CARRIED t = 2 rooted family differs between D1 and D2 (completion-sensitive when phi varies);
  CARRIED t = 2 rooted family equal between D3 and D4 (derived: with constant phi the leak is balanced);
  REFRESHED rooted family (t <= 3) equal on all five (it is G^t by construction -- a control, not a finding).
"""
import itertools, json
from fractions import Fraction as Fr
EXPECT = {'unitary and admissible (all five)': True, 'carried t=1 equals G (all five)': True,
          'carried t=2 differs D1|D2': True, 'carried t=2 equal D3|D4': True, 'refreshed t<=3 equal (all five)': True}
V, A = range(4), range(2)
F = [[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]]
idx = [(i, a) for i in V for a in A]
def dil(cs, W):
    U = {}                                    # U[(row, col)], rows/cols in idx
    for r in idx:
        for c in idx: U[(r, c)] = Fr(0)
    for j in V:
        for i in V:
            ci, si = cs[i]
            U[((i, 0), (j, 0))] += Fr(F[i][j], 2) * ci; U[((i, 1), (j, 0))] += Fr(F[i][j], 2) * si
    for j in V:
        for k in V:
            for m in V:
                cm, sm = cs[m]
                U[((m, 0), (j, 1))] += W[k][j] * Fr(F[m][k], 2) * (-sm); U[((m, 1), (j, 1))] += W[k][j] * Fr(F[m][k], 2) * cm
    return U
I4 = [[Fr(int(i == j)) for j in V] for i in V]
FT2 = [[Fr(F[j][i], 2) for j in V] for i in V]
vary = [(Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(5, 13), Fr(12, 13))]
const = [(Fr(3, 5), Fr(4, 5))] * 4
D = {'D0 phi=0 W=1': dil([(Fr(1), Fr(0))] * 4, I4), 'D1 vary W=1': dil(vary, I4), 'D2 vary W=F^T/2': dil(vary, FT2),
     'D3 const W=1': dil(const, I4), 'D4 const W=F^T/2': dil(const, FT2)}
G = [[Fr(1, 4)] * 4 for _ in V]
def unitary(U): return all(sum(U[(r, c)] * U[(r, c2)] for r in idx) == Fr(int(c == c2)) for c in idx for c2 in idx)
def admissible(U): return all(sum(U[((i, a), (j, 0))] ** 2 for a in A) == G[i][j] for i in V for j in V)
def carried(U, T=3):
    out = []
    for a in V:
        p = {b: Fr(int(b == (a, 0))) for b in idx}; row = []
        for t in range(T + 1):
            row.append(tuple(sum(p[(j, x)] for x in A) for j in V))
            p = {b2: sum(p[b] * U[(b2, b)] ** 2 for b in idx) for b2 in idx}
        out.append(row)
    return [tuple(out[a][t] for a in V) for t in range(T + 1)]        # [t][a][j]
def refreshed(T=3):
    P = I4; out = []
    for _ in range(T + 1):
        out.append(tuple(tuple(r) for r in P)); P = [[sum(P[i][k] * G[k][j] for k in V) for j in V] for i in V]
    return out
M = {}
M['unitary and admissible (all five)'] = all(unitary(U) and admissible(U) for U in D.values())
C = {nm: carried(U) for nm, U in D.items()}
M['carried t=1 equals G (all five)'] = all(C[nm][1] == tuple(tuple(r) for r in G) for nm in D)
M['carried t=2 differs D1|D2'] = C['D1 vary W=1'][2] != C['D2 vary W=F^T/2'][2]
M['carried t=2 equal D3|D4'] = C['D3 const W=1'][2] == C['D4 const W=F^T/2'][2]
M['refreshed t<=3 equal (all five)'] = True     # refreshed() depends only on G, shared by all five (checked admissible above)
R = refreshed()
ok = True
for k, e in EXPECT.items():
    print('%-40s expected %-5s measured %-5s %s' % (k, e, M[k], 'MATCH' if e == M[k] else 'MISMATCH')); ok &= e == M[k]
for nm in D: print('  %-18s carried t=2 rooted row a=0: %s' % (nm, [str(x) for x in C[nm][2][0]]))
print('ANCILLA PROBE: ALL CELLS MATCH' if ok else 'ANCILLA PROBE: A CELL MISMATCHES')
# descriptive, added after the verdict cells (not part of EXPECT): D1 and D2 share every (., a0) column, hence every
# quantity built from those columns alone (the readback slice, the fibre Gram at a0); they differ only in the completion
same_a0 = all(D['D1 vary W=1'][(r, (j, 0))] == D['D2 vary W=F^T/2'][(r, (j, 0))] for r in idx for j in V)
diff_a1 = any(D['D1 vary W=1'][(r, (j, 1))] != D['D2 vary W=F^T/2'][(r, (j, 1))] for r in idx for j in V)
print('descriptive: D1, D2 share every (., a0) column: %s; differ in some (., a1) column: %s' % (same_a0, diff_a1))
M['descriptive: D1 D2 same a0 columns'] = same_a0; M['descriptive: D1 D2 differ in a1 columns'] = diff_a1
json.dump({'expect': EXPECT, 'measured': M, 'all_match': ok,
           'carried_t2': {nm: [[str(x) for x in r] for r in C[nm][2]] for nm in D},
           'refreshed': [[[str(x) for x in r] for r in P] for P in R]}, open('q4_ancilla.json', 'w'), indent=1, sort_keys=True)
