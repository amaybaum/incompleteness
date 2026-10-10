"""Exact checks of the non-literature steps of the written argument
   'admissible + IE1 + forward N-CLASS gate invariance  =>  K = Q3 or its twin'.
Decision rule (fixed before the first run): PASS iff C1-C4 all hold as stated.
 C1  the full transpose T = actC reflY . actT reflY commutes with cnot (16 symbolic entries).
 C2  for each of the 16 reflection patterns (a, b, a', b'), N0 = actC reflY^a actT reflY^b cnot
     actC reflY^a' actT reflY^b' is a signed permutation of the 16 entries of finite order.
 C3  for each pattern with a+a' != b+b' (mod 2), the N0-orbit of prodState xplus z3 contains a
     table that is negative at one of the 36 sharp pairs (+-e_i, +-e_j): no cone inside maxCone
     containing the products is N0-invariant.
 C4  countercontrol and consistency: for each pattern with a+a' == b+b' (mod 2), every table in
     that orbit is in T_S(Q3) with T_S = actC reflY^a' actT reflY^b' (pauliW of T_S(table) is PSD),
     and no orbit table is negative at a sharp pair.
"""
import itertools
import sympy as sp
from sympy import Rational as Q, Matrix, I as iu

def homMap(R, v): return [v[0]] + list(R * Matrix(v[1:]))
def actC(R, w):
    out = sp.zeros(4, 4)
    for n in range(4):
        col = homMap(R, [w[m, n] for m in range(4)])
        for m in range(4): out[m, n] = col[m]
    return out
def actT(R, w):
    out = sp.zeros(4, 4)
    for m in range(4):
        row = homMap(R, [w[m, n] for n in range(4)])
        for n in range(4): out[m, n] = row[n]
    return out
PC = [[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]
PT = [[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def sgn(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
def cnot(w): return Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])
reflY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
def hom(x): return [Q(1)] + list(x)
def prodState(x, y): return Matrix(4, 1, hom(x)) * Matrix(1, 4, hom(y))
sig = [sp.eye(2), Matrix([[0, 1], [1, 0]]), Matrix([[0, -iu], [iu, 0]]), Matrix([[1, 0], [0, -1]])]
def pauliW(w):
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if w[m, n] != 0: out += w[m, n] * sp.kronecker_product(sig[m], sig[n])
    return out / 4
def psd(M):
    # Hermitian 4x4 with exact entries: PSD iff all principal minors >= 0
    n = M.shape[0]
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if sp.simplify(M.extract(list(S), list(S)).det()) < 0: return False
    return True
sharp = [[s if i == j else 0 for i in range(3)] for j in range(3) for s in (1, -1)]
def min_sharp(w):
    vals = []
    for u in sharp:
        for v in sharp:
            a = Matrix(1, 4, [Q(1, 2)] + [Q(c, 2) for c in u]); b = Matrix(4, 1, [Q(1, 2)] + [Q(c, 2) for c in v])
            vals.append((a * w * b)[0, 0])
    return min(vals)
def P(e): return reflY if e else I3
def N0(pat):
    a, b, a2, b2 = pat
    return lambda w: actC(P(a), actT(P(b), cnot(actC(P(a2), actT(P(b2), w)))))

res = []
def check(name, ok, note=""):
    res.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name}  {note}")

X = Matrix(4, 4, sp.symbols('w0:16'))
T = lambda w: actC(reflY, actT(reflY, w))
check("C1 full transpose commutes with cnot", sp.simplify(T(cnot(X)) - cnot(T(X))) == sp.zeros(4, 4))

basis = [Matrix(4, 4, lambda m, n, k=k: 1 if 4 * m + n == k else 0) for k in range(16)]
ok2, orders = True, {}
for pat in itertools.product((0, 1), repeat=4):
    f = N0(pat)
    M = Matrix(16, 16, lambda i, j: f(basis[j])[i // 4, i % 4])
    signed_perm = all(sum(1 for x in M.row(i) if x != 0) == 1 and all(x in (0, 1, -1) for x in M.row(i)) for i in range(16))
    k, P_ = 1, M
    while P_ != sp.eye(16) and k <= 64: P_ = P_ * M; k += 1
    orders[pat] = k
    ok2 &= signed_perm and k <= 64
check("C2 every N0 is a signed permutation of finite order", ok2, f"orders {sorted(set(orders.values()))}")

xplus, z3 = [1, 0, 0], [0, 0, 1]
ok3, ok4 = True, True
for pat in itertools.product((0, 1), repeat=4):
    a, b, a2, b2 = pat
    f = N0(pat)
    orbit, w = [], prodState(xplus, z3)
    for _ in range(orders[pat]):
        orbit.append(w); w = f(w)
    mins = [min_sharp(t) for t in orbit]
    if (a + a2) % 2 != (b + b2) % 2:
        ok3 &= min(mins) < 0
    else:
        TS = lambda t, a2=a2, b2=b2: actC(P(a2), actT(P(b2), t))
        ok4 &= all(psd(pauliW(TS(t))) for t in orbit) and min(mins) >= 0
check("C3 mixed patterns (a+a' != b+b'): orbit leaves maxCone", ok3)
check("C4 matched patterns: orbit stays in T_S(Q3) and in maxCone", ok4)
print(f"{sum(res)}/{len(res)}")
print("VERDICT", "CLASSIFICATION-PROBE-PASS" if all(res) else "CLASSIFICATION-PROBE-FAIL")
