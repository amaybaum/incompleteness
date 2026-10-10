"""d = 5 finite-local branch: signed-permutation constructions, exact algebra + block-coordinate positivity search.
Basis of each local R^6: 0 u, 1 x, 2 y, 3 z, 4 w1, 5 w2. Corners u +- z. Read-only; evidence where stated."""
import itertools, numpy as np
n = 6; D = n * n
U, X, Y, Z, W1, W2 = range(6)
idx = lambda i, j: i * n + j

class SP:
    """signed permutation on the 36 product basis vectors: e_k -> sign[k] e_perm[k]"""
    def __init__(self, perm, sign): self.p = np.array(perm); self.s = np.array(sign)
    def mat(self):
        M = np.zeros((D, D)); M[self.p, np.arange(D)] = self.s; return M
    def __mul__(self, o):               # self o other
        return SP(self.p[o.p], self.s[o.p] * o.s)
    def key(self): return (tuple(self.p), tuple(self.s))

def from_map(m):                         # m: dict (i,j) -> (sign, k, l); missing = identity
    perm = list(range(D)); sign = [1] * D
    for (i, j), (sg, k, l) in m.items(): perm[idx(i, j)] = idx(k, l); sign[idx(i, j)] = sg
    return SP(perm, sign)

def local(A):                            # A: dict i -> (sign, k) on one factor
    def f(i): return A.get(i, (1, i))
    return f

def loc_pair(fa, fb):
    perm = [0] * D; sign = [0] * D
    for i in range(n):
        for j in range(n):
            sa, k = fa(i); sb, l = fb(j); perm[idx(i, j)] = idx(k, l); sign[idx(i, j)] = sa * sb
    return SP(perm, sign)

ident = lambda i: (1, i)
def diagN(flips):
    return lambda i: (-1 if i in flips else 1, i)
S = loc_pair(ident, ident); S = SP([idx(j, i) for i in range(n) for j in range(n)], [1] * D)

def controlled(Nflip, rules):
    """classical control part: G(u(x)t) = u(x)P+t + z(x)P-t, G(z(x)t) = z(x)P+t + u(x)P-t  (M_0 = I, M_1 = N)
    rules: dict (i,j) -> (sign,k,l) for control transverse i in {x,y,w1,w2}"""
    m = {}
    for j in range(n):
        if j in Nflip: m[(U, j)] = (1, Z, j); m[(Z, j)] = (1, U, j)
    m.update(rules); return from_map(m)

def group(gens, cap=5000):
    seen = {g.key(): g for g in gens}; frontier = list(gens)
    while frontier:
        new = []
        for a in frontier:
            for b in gens:
                c = a * b
                if c.key() not in seen:
                    seen[c.key()] = c; new.append(c)
                    if len(seen) > cap: return None
        frontier = new
    return list(seen.values())

rng = np.random.default_rng(0)
def min_value(M, starts=200, iters=60):
    """min over unit s,t,a,b in R^5 of (1,a)(x)(1,b) . M ((1,s)(x)(1,t)); block-coordinate descent (each block exact)"""
    T = M.reshape(n, n, n, n)          # T[f_i, g_j, s_k, t_l]
    best = np.inf; arg = None
    for _ in range(starts):
        v = [rng.normal(size=5) for _ in range(4)]; v = [x / np.linalg.norm(x) for x in v]
        for _ in range(iters):
            for blk in range(4):
                vec = [np.concatenate([[1.], x]) for x in v]
                ops = [vec[0], vec[1], vec[2], vec[3]]
                # contract all but blk
                subs = ['i', 'j', 'k', 'l']
                expr = 'ijkl,' + ','.join(s for b, s in enumerate(subs) if b != blk) + '->' + subs[blk]
                c = np.einsum(expr, T, *[ops[b] for b in range(4) if b != blk])
                cv = c[1:]; nv = np.linalg.norm(cv)
                if nv > 1e-15: v[blk] = -cv / nv
        vec = [np.concatenate([[1.], x]) for x in v]
        val = np.einsum('ijkl,i,j,k,l->', T, *vec)
        if val < best: best, arg = val, [x.copy() for x in v]
    return best, arg
