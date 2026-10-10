"""Thread B helper library -- exact sparse linear algebra over Q for maps on (R^n)^{(x)k}.

Conventions follow NB-1's probe: local basis index 0 = u, 1..d-1 = T, d = z; corners k_a = u + (-1)^a z.
A map on (R^n)^{(x)k} is a dict  col -> {row: Fraction}  (sparse columns), index = mixed radix, first factor most
significant.  Everything here is exact (Fraction); nothing in this file uses floating point.
"""
from fractions import Fraction as Fr
from itertools import product


# ------------------------------------------------------------------ dense helpers (small local matrices)
def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def diag(v):
    return [[Fr(v[i]) if i == j else Fr(0) for j in range(len(v))] for i in range(len(v))]


def zeros(n, m=None):
    return [[Fr(0)] * (n if m is None else m) for _ in range(n)]


def mm(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B)) if A[i][l] != 0), Fr(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def mv(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v)) if v[j] != 0), Fr(0)) for i in range(len(A))]


def neg(A):
    return [[-x for x in r] for r in A]


def inv(A):
    """exact Gauss-Jordan inverse"""
    n = len(A)
    M = [[Fr(x) for x in r] + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        piv = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [r[n:] for r in M]


def rank(rows, ncols=None):
    M = [[Fr(x) for x in r] for r in rows]
    if not M:
        return 0
    ncols = len(M[0]) if ncols is None else ncols
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def split_of(N):
    """(p, q) of a ball NOT: dims of the +1 / -1 eigenspaces on T (u is +1, z is -1), by exact ranks"""
    n = len(N)
    I = eye(n)
    plus = n - rank([[N[i][j] - I[i][j] for j in range(n)] for i in range(n)])
    minus = n - rank([[N[i][j] + I[i][j] for j in range(n)] for i in range(n)])
    return plus - 1, minus - 1, plus, minus


def cayley(Aanti):
    """rational orthogonal (I - A)(I + A)^-1 for antisymmetric A"""
    n = len(Aanti)
    I = eye(n)
    P = [[I[i][j] - Aanti[i][j] for j in range(n)] for i in range(n)]
    Q = [[I[i][j] + Aanti[i][j] for j in range(n)] for i in range(n)]
    return mm(P, inv(Q))


def frame_preserving(gT, flip=False):
    """embed an orthogonal matrix of T as g = 1 (+) gT (+) (+-1) on u, T, z"""
    m = len(gT)
    n = m + 2
    g = zeros(n)
    g[0][0] = Fr(1)
    g[n - 1][n - 1] = Fr(-1 if flip else 1)
    for i in range(m):
        for j in range(m):
            g[i + 1][j + 1] = Fr(gT[i][j])
    return g


def corners(n):
    k0 = [Fr(0)] * n; k0[0] = Fr(1); k0[n - 1] = Fr(1)
    k1 = [Fr(0)] * n; k1[0] = Fr(1); k1[n - 1] = Fr(-1)
    return [k0, k1]


def is_ball_automorphism_fixing_u(g):
    """g orthogonal (g^T g = I) and g u = u: then g preserves the Lorentz form and u, so g(L) = L"""
    n = len(g)
    return mm(tr(g), g) == eye(n) and [g[i][0] for i in range(n)] == [Fr(int(i == 0)) for i in range(n)]


# ------------------------------------------------------------------ sparse maps on (R^n)^{(x)k}
class Space:
    def __init__(self, n, k):
        self.n, self.k = n, k
        self.dim = n ** k

    def idx(self, digits):
        r = 0
        for x in digits:
            r = r * self.n + x
        return r

    def digits(self, i):
        out = []
        for _ in range(self.k):
            out.append(i % self.n)
            i //= self.n
        return out[::-1]


def sp_from_dense(M):
    out = {}
    for j in range(len(M[0])):
        col = {i: Fr(M[i][j]) for i in range(len(M)) if M[i][j] != 0}
        out[j] = col
    return out


def sp_identity(dim):
    return {j: {j: Fr(1)} for j in range(dim)}


def sp_apply(A, v):
    """v: dict index->value"""
    out = {}
    for j, x in v.items():
        if x == 0:
            continue
        for i, a in A.get(j, {}).items():
            out[i] = out.get(i, Fr(0)) + a * x
    return {i: x for i, x in out.items() if x != 0}


def sp_compose(A, B):
    """A o B"""
    return {j: sp_apply(A, col) for j, col in B.items()}


def sp_eq(A, B, dim):
    for j in range(dim):
        a = {i: x for i, x in A.get(j, {}).items() if x != 0}
        b = {i: x for i, x in B.get(j, {}).items() if x != 0}
        if a != b:
            return False
    return True


def sp_sub(A, B, dim):
    out = {}
    for j in range(dim):
        c = dict(A.get(j, {}))
        for i, x in B.get(j, {}).items():
            c[i] = c.get(i, Fr(0)) - x
        out[j] = {i: x for i, x in c.items() if x != 0}
    return out


def sp_is_zero(A):
    return all(not col for col in A.values())


def embed_local(M, slot, sp):
    """local matrix M (n x n) acting on factor `slot` of sp"""
    out = {}
    for j in range(sp.dim):
        dj = sp.digits(j)
        col = {}
        for a in range(sp.n):
            x = M[a][dj[slot]]
            if x != 0:
                di = list(dj); di[slot] = a
                col[sp.idx(di)] = x
        out[j] = col
    return out


def embed_two(G2, n, slots, sp):
    """two-copy map G2 (sparse, on R^n (x) R^n, first factor = slots[0]) acting on factors slots of sp"""
    X, Y = slots
    out = {}
    for j in range(sp.dim):
        dj = sp.digits(j)
        src = dj[X] * n + dj[Y]
        col = {}
        for r, x in G2.get(src, {}).items():
            di = list(dj); di[X] = r // n; di[Y] = r % n
            ii = sp.idx(di)
            col[ii] = col.get(ii, Fr(0)) + x
        out[j] = {i: x for i, x in col.items() if x != 0}
    return out


def kron_vecs(vs):
    out = {(): Fr(1)}
    for v in vs:
        new = {}
        for key, x in out.items():
            for i, y in enumerate(v):
                if y != 0:
                    new[key + (i,)] = x * y
        out = new
    return out


def tensor_vec(vs, sp):
    return {sp.idx(list(key)): x for key, x in kron_vecs(vs).items()}


def value(A, states, effects, sp):
    """(f1 (x) ... (x) fk) . A (s1 (x) ... (x) sk)"""
    w = sp_apply(A, tensor_vec(states, sp))
    e = tensor_vec(effects, sp)
    return sum((x * e.get(i, 0) for i, x in w.items()), Fr(0))


# ------------------------------------------------------------------ gates
def jk_gate(d, NB, J, K):
    """the J/K map of NB-1 (M_0 = I): basis u=0, T=1..d-1, z=d.  NB: diagonal of the TARGET NOT (length n).
    G(k_a (x) t) = k_a (x) NB^a t; for c in T: target E+ = {u, x} exchanged u <-> x (x = the unique +1 transverse
    axis of NB), target V- (NB = -1, z included): G(c (x) t) = Jc (x) Kt.  J, K: dicts i -> (sign, j)."""
    n = d + 1
    plus = [i for i in range(1, d) if NB[i] == 1]
    assert len(plus) == 1, 'the J/K map needs p_B = 1'
    x = plus[0]
    G = {}
    e = eye(n)
    for j in range(n):
        colu, colz = {}, {}
        for i in range(n):
            if e[j][i] != 0:
                if NB[i] == 1:
                    colu[0 * n + i] = Fr(1); colz[d * n + i] = Fr(1)
                else:
                    colu[d * n + i] = Fr(1); colz[0 * n + i] = Fr(1)
        G[0 * n + j] = colu; G[d * n + j] = colz
    for c in range(1, d):
        G[c * n + 0] = {c * n + x: Fr(1)}
        G[c * n + x] = {c * n + 0: Fr(1)}
        for j in range(1, n):
            if NB[j] == -1:
                s1, cc = J[c]; s2, l = K[j]
                G[c * n + j] = {cc * n + l: Fr(s1 * s2)}
    return G


def as_mat(mp, n):
    M = zeros(n)
    for a, (s, b) in mp.items():
        M[b][a] = Fr(s)
    return M


def complex_cnot_d3():
    """complex CNOT in Pauli coordinates (u, x, y, z), Gaussian-integer arithmetic, as in NB-1's probe"""
    def gmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
    def gadd(a, b): return (a[0] + b[0], a[1] + b[1])
    def sum_g(xs):
        acc = (0, 0)
        for x in xs: acc = gadd(acc, x)
        return acc
    def gm(A, B):
        n = len(A)
        return [[sum_g([gmul(A[i][l], B[l][j]) for l in range(n)]) for j in range(n)] for i in range(n)]
    def gk(A, B):
        n, m = len(A), len(B)
        return [[gmul(A[i // m][j // m], B[i % m][j % m]) for j in range(n * m)] for i in range(n * m)]
    def dag(A):
        return [[(A[j][i][0], -A[j][i][1]) for j in range(len(A))] for i in range(len(A))]
    ONE, ZER, IM = (1, 0), (0, 0), (0, 1)
    PAULI = [[[ONE, ZER], [ZER, ONE]], [[ZER, ONE], [ONE, ZER]], [[ZER, (0, -1)], [IM, ZER]],
             [[ONE, ZER], [ZER, (-1, 0)]]]
    CN = [[ONE if (i == j and i < 2) or (i, j) in ((2, 3), (3, 2)) else ZER for j in range(4)] for i in range(4)]
    basis16 = [gk(PAULI[a], PAULI[b]) for a in range(4) for b in range(4)]
    G3 = zeros(16)
    for jj, Bj in enumerate(basis16):
        img = gm(gm(CN, Bj), dag(CN))
        for ii, Bi in enumerate(basis16):
            t = sum_g([gm(img, Bi)[k][k] for k in range(4)])
            assert t[1] == 0 and t[0] % 4 == 0
            G3[ii][jj] = Fr(t[0], 4)
    return G3


# ------------------------------------------------------------------ the NB-1 relations on two copies
def frame_ok(G, n):
    sp = Space(n, 2)
    k = corners(n)
    for a in (0, 1):
        for b in (0, 1):
            img = sp_apply(G, tensor_vec([k[a], k[b]], sp))
            if img != tensor_vec([k[a], k[a ^ b]], sp):
                return False
    return True


def rel_t(G, n, NB):
    sp = Space(n, 2)
    INB = embed_local(NB, 1, sp)
    return sp_eq(sp_compose(INB, sp_compose(G, INB)), G, sp.dim)


def rel_c(G, n, NA, NB):
    sp = Space(n, 2)
    NAI = embed_local(NA, 0, sp)
    INB = embed_local(NB, 1, sp)
    return sp_eq(sp_compose(NAI, sp_compose(G, NAI)), sp_compose(INB, G), sp.dim)


def is_ball_not(N):
    """orthogonal involution fixing u with N z = -z"""
    n = len(N)
    I = eye(n)
    return (mm(N, N) == I and mm(tr(N), N) == I and [N[i][0] for i in range(n)] == I[0]
            and [N[i][n - 1] for i in range(n)] == [-x for x in I[n - 1]])
