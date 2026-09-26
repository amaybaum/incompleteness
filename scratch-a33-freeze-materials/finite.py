"""A33 research, derivation B (independent of the circle-permutation normal form).

P = the distinct feature points f_r(i^k), r in 0..8, k in 0..3 -- a finite subset of X.
1. Aut(P, d): every bijection of P preserving the exact squared distances, found by label-free
   backtracking over the distance matrix alone (no circle labels, no parameters).
2. Each such bijection extends uniquely to an affine isometry T of aff(P) = aff(X) (every circle
   lies in aff(P): it is the circle through three of its points of P).
3. T carries X onto X iff for every circle r the three image points of f_r(1), f_r(i), f_r(-1)
   lie on one circle s of the nine: T(circle r) is the unique circle through them. Membership is
   read off coordinates exactly. Nothing here assumes how circles are permuted or reparametrized.
Output: the subgroup Isom(X) cap Stab(P), as permutations of P."""
import sys, pickle
from points import point, d2, on_circle
from circles import N

pts, where = [], {}
for r in range(N):
    for k in range(4):
        x = point(r, k)
        if x not in where:
            where[x] = len(pts); pts.append(x)
n = len(pts)
lab = {(r, k): where[point(r, k)] for r in range(N) for k in range(4)}
D = [[d2(pts[a], pts[b]) for b in range(n)] for a in range(n)]
vals = sorted({v for row in D for v in row})
Di = [[vals.index(v) for v in row] for row in D]
sig = [tuple(sorted(row)) for row in Di]

def automorphisms():
    order = sorted(range(n), key=lambda a: (-len(set(Di[a])), a))
    img = [-1] * n; used = [False] * n; out = []
    def rec(t):
        if t == n:
            out.append(tuple(img)); return
        a = order[t]
        for b in range(n):
            if used[b] or sig[b] != sig[a]:
                continue
            if all(Di[a][order[u]] == Di[b][img[order[u]]] for u in range(t)):
                img[a] = b; used[b] = True
                rec(t + 1)
                img[a] = -1; used[b] = False
    rec(0)
    return out

MEM = [[bool(on_circle(pts[a], s)) for s in range(N)] for a in range(n)]

def preserves_X(p):
    for r in range(N):
        ims = [p[lab[r, k]] for k in (0, 1, 2)]
        if not any(all(MEM[x][s] for x in ims) for s in range(N)):
            return False
    return True

if __name__ == '__main__':
    print('points of P:', n, ' distinct squared distances:', len(vals))
    A = automorphisms()
    print('Aut(P, d):', len(A))
    I = [p for p in A if preserves_X(p)]
    print('of which carry X onto X:', len(I))
    pickle.dump({'pts': pts, 'lab': lab, 'aut': A, 'iso': I}, open('finite.pkl', 'wb'))
