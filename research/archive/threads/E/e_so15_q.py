"""Thread E -- pure-rational (no modular arithmetic) variant of e_so15_fast.py: same breadth-first bracket
queue, echelon over Q with Fractions, so the rank 105 is computed over Q directly; with the so(15)
containment it gives dim = 105 exactly.
"""
import itertools, sys, time
from fractions import Fraction as Fq
ns = {}
src = open('replay/k20_part3.py').read().split("U_=set(")[0]
import os; os.chdir('replay'); exec(src.replace("print(", "_p=("), ns); os.chdir('..')
Gs, cs = ns['Gs'], ns['cs']
def M(G): return [[int(G[i, j]) for j in range(16)] for i in range(16)]
def mul(A, B):
    Bt = list(zip(*B)); return [[sum(x*y for x, y in zip(r, c) if x and y) for c in Bt] for r in A]
def br(A, B):
    X, Y = mul(A, B), mul(B, A); return [[x - y for x, y in zip(r, s)] for r, s in zip(X, Y)]
def kron(A, B): return [[A[i//4][j//4]*B[i % 4][j % 4] for j in range(16)] for i in range(16)]
I4 = [[int(i == j) for j in range(4)] for i in range(4)]
def l(k):
    m = [[0]*4 for _ in range(4)]; a, b = [(2, 3), (3, 1), (1, 2)][k]; m[a][b] = -1; m[b][a] = 1; return m
local = [kron(l(k), I4) for k in range(3)] + [kron(I4, l(k)) for k in range(3)]
class ModSpan:
    def __init__(s): s.rows = {}
    def add(s, v):
        v = [Fq(x) for x in v]
        for p, r in s.rows.items():
            if v[p]:
                f = v[p]; v = [a - f*b for a, b in zip(v, r)]
        p = next((i for i, x in enumerate(v) if x), None)
        if p is None: return False
        pv = v[p]; v = [x/pv for x in v]
        for q in list(s.rows):
            r = s.rows[q]
            if r[p]:
                f = r[p]; s.rows[q] = [a - f*b for a, b in zip(r, v)]
        s.rows[p] = v; return True
def flat(A): return [x for r in A for x in r]
ok = True
for i in (2, 3, 4, 5, 8, 9, 14, 15):
    t0 = time.time()
    G = M(Gs[cs[i][0]]); Gt = [list(r) for r in zip(*G)]
    Id = [[int(a == b) for b in range(16)] for a in range(16)]
    upper = mul(G, Gt) == Id and G[0] == [1] + [0]*15 and all(G[j][0] == 0 for j in range(1, 16))
    pows = [Id]; Pw = G
    while Pw != Id: pows.append(Pw); Pw = mul(Pw, G)
    gens = [mul(mul(Q, x), [list(r) for r in zip(*Q)]) for Q in pows for x in local]
    S = ModSpan(); basis = []; queue = list(gens)
    while queue and len(basis) < 105:
        g = queue.pop(0)
        if S.add(flat(g)):
            queue += [br(g, b) for b in basis]; basis.append(g)
    anti = all(all(b[r][c] == -b[c][r] for r in range(16) for c in range(16)) and not any(b[0]) for b in basis)
    print('failing SO-class %2d: G orthogonal fixing u(x)u: %s; %d integer brackets, rank over Q = %d; all antisymmetric with zero u(x)u row: %s  (%.1fs)'
          % (i, upper, len(basis), len(S.rows), anti, time.time() - t0), flush=True)
    ok &= upper and len(S.rows) == 105 and anti
print('e_so15_q:', 'OK -- dim = 105 = dim so(15) for all 8 failing classes' if ok else 'FAILED')
sys.exit(0 if ok else 1)
