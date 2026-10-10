"""Ball-composite CNOT no-go for d-balls, d != 3 -- exact checks (integers / Q; rank bounds mod p). Read-only.

Setting: local state space = unit d-ball, n = d + 1, V = R^n (x) R^n (local tomography), closed cone C with
min <= C <= max, L = SO(d) x SO(d) <= Aut(C). V = 1 + A + B + AB.
Uniform lemmas (checked here per d; the proof is dimension-uniform, see BALL-NOGO.md):
 U1  first-order space Lam = l_A + l_B + Sig_A + Sig_B + Z exactly, where Sig_A ~ Lam2(A) (x) B are the antisymmetric
     A<->AB couplings X_{AB<-A} a = Om a (x) f, X_{A<-AB} = -X_{AB<-A}^T; Sig_B mirror; Z = Lam2(A) (x) Lam2(B) acting
     on AB only.  dim = d(d-1) + d^2(d-1) + (d(d-1)/2)^2.   [sampled superset == family: nullity mod p == family rank]
 U2  ad-Casimir pairs (c_A, c_B) of the five pieces are pairwise distinct iff d != 2, 3.
 U3  bracket obstruction: [S(Om (x) f1), S(Om (x) f2)] violates the first-order condition at an exact rational point.
 U4  Z consists of symmetric operators (nonzero => real eigenvalue => not compact).
 U5  Burnside: rational rotations span End(R^d) for d >= 3 (so any nonzero invariant subspace of Sig_A contains
     Om (x) f1 and Om (x) f2 with Om != 0).
 U6  normalizer: total Casimir on V has u(x)z in eigenvalue -(d-1) and z(x)z in eigenvalue -2(d-1).
Controls (d = 3): Casimir pairs coincide on Sig_A, Sig_B, Z; su(4) generators and all their brackets satisfy the exact
sampled constraints (the obstruction method does not flag complex QM); the extra su(4) generators have nonzero Sig_A
and Sig_B components (the diagonal loophole).  d = 2 reproduces the disc (dim 7, l ~ Z coincidence).
"""
import sys, itertools, time
import numpy as np
import sympy as sp
P = 2147483647
OUT = []
def rep(name, ok, detail=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''), flush=True)

def rank_modp(M):
    A = np.array(M, dtype=np.int64) % P
    r = 0; rows, cols = A.shape
    for c in range(cols):
        if r == rows: break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        k = r + nz[0]
        if k != r: A[[r, k]] = A[[k, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = (A[r] * inv) % P
        col = A[:, c].copy(); col[r] = 0
        idx = np.nonzero(col)[0]
        if len(idx): A[idx] = (A[idx] - (col[idx, None] * A[r]) % P) % P
        r += 1
    return r

def J(m, a, b):
    M = np.zeros((m, m), dtype=np.int64); M[a, b] = -1; M[b, a] = 1; return M

def pieces(d):
    n = d + 1; N = n * n; I = np.eye(n, dtype=np.int64)
    idx = lambda i, j: i * n + j
    def emb(Om):      # d x d on coords 1..d of R^n
        M = np.zeros((n, n), dtype=np.int64); M[1:, 1:] = Om; return M
    Js = [J(d, a, b) for a in range(d) for b in range(a + 1, d)]
    lA = [np.kron(emb(Om), I) for Om in Js]; lB = [np.kron(I, emb(Om)) for Om in Js]
    SA, SB, Z = [], [], []
    for Om in Js:
        for k in range(d):
            M = np.zeros((N, N), dtype=np.int64); M2 = np.zeros((N, N), dtype=np.int64)
            for p in range(d):
                for q in range(d):
                    if Om[p, q]:
                        M[idx(p + 1, k + 1), idx(q + 1, 0)] = Om[p, q]; M[idx(q + 1, 0), idx(p + 1, k + 1)] = -Om[p, q]
                        M2[idx(k + 1, p + 1), idx(0, q + 1)] = Om[p, q]; M2[idx(0, q + 1), idx(k + 1, p + 1)] = -Om[p, q]
            SA.append(M); SB.append(M2)
    for OA in Js:
        for OB in Js: Z.append(np.kron(emb(OA), emb(OB)))
    return dict(lA=lA, lB=lB, SA=SA, SB=SB, Z=Z, Js=Js, emb=emb, n=n, N=N)

def sphere_pts(d, K):
    pts = []; g = np.random.default_rng(1000 + d); seen = set()
    while len(pts) < K:                                               # generic rational points (seeded)
        t = tuple(int(x) for x in g.integers(-3, 4, size=d - 1))
        if t in seen: continue
        seen.add(t); s = sum(x * x for x in t)
        pts.append(tuple([s + 1] + [2 * x for x in t] + [s - 1]))    # (den, num...) : v = num/den, |v| = 1
    return pts

def constraint_rows(d, pts):
    n = d + 1; N = n * n; rows = []
    e = np.eye(n, dtype=np.int64)
    vecs = [(np.array(pt, dtype=np.int64), np.array([pt[0]] + [-x for x in pt[1:]], dtype=np.int64)) for pt in pts]
    for (pv, fv), (pw, fw) in itertools.product(vecs, repeat=2):
        p = np.kron(pv, pw)
        for c in range(n):
            rows.append(np.kron(np.kron(fv, e[c]), p)); rows.append(np.kron(np.kron(e[c], fw), p))
    uu = np.zeros(N, dtype=np.int64); uu[0] = 1
    for j in range(N):
        r = np.zeros(N * N, dtype=np.int64); r[j::N] = 0
        r[np.arange(N) * N + j] = uu; rows.append(r)
    return np.array(rows), vecs

def violates(X, vecs):
    n = int(round(len(vecs[0][0])))
    e = np.eye(n, dtype=np.int64)
    for (pv, fv), (pw, fw) in itertools.product(vecs, repeat=2):
        y = X @ np.kron(pv, pw)
        a = np.kron(fv.reshape(1, -1), np.eye(n, dtype=np.int64)) @ y
        b = np.kron(np.eye(n, dtype=np.int64), fw.reshape(1, -1)) @ y
        if np.any(a) or np.any(b): return (pv.tolist(), pw.tolist())
    return None

def run(d, K):
    t0 = time.time(); pc = pieces(d); n, N = pc['n'], pc['N']
    fam = pc['lA'] + pc['lB'] + pc['SA'] + pc['SB'] + pc['Z']
    D = d * (d - 1) + d * d * (d - 1) + (d * (d - 1) // 2) ** 2
    pts = sphere_pts(d, K); M, vecs = constraint_rows(d, pts)
    F = np.array([X.reshape(-1) for X in fam]).T
    rep('d=%d U1 family (%d elements, formula %d) satisfies every sampled constraint exactly' % (d, len(fam), D),
        len(fam) == D and not np.any(M @ F))
    rF = rank_modp(F.T)
    Mc = M
    if M.shape[0] > N * N + 200:                       # random compression: rank can only drop, nullity bound stays valid
        R = np.random.default_rng(d).integers(0, 1000, size=(N * N + 200, M.shape[0]), dtype=np.int64)
        Mc = np.zeros((N * N + 200, N * N), dtype=np.int64)
        Mm = M % P
        for s in range(0, M.shape[0], 256):
            Mc = (Mc + (R[:, s:s + 256] @ Mm[s:s + 256]) % P) % P
    nul = N * N - rank_modp(Mc)
    rep('d=%d U1 sampled first-order space == family: nullity mod p %d == family rank %d' % (d, nul, rF), nul == rF == D,
        '(%.0fs)' % (time.time() - t0))
    # U2 Casimirs
    gA, gB = pc['lA'], pc['lB']
    def cas(gs, X): return sum(g @ (g @ X - X @ g) - (g @ X - X @ g) @ g for g in gs)
    pairs = {}
    for name in ('lA', 'lB', 'SA', 'SB', 'Z'):
        cs = set()
        for X in pc[name]:
            CA, CB = cas(gA, X), cas(gB, X)
            k = np.flatnonzero(X)[0]
            ca, cb = CA.flat[k] // X.flat[k], CB.flat[k] // X.flat[k]
            assert np.array_equal(CA, ca * X) and np.array_equal(CB, cb * X), name
            cs.add((int(ca), int(cb)))
        assert len(cs) == 1; pairs[name] = cs.pop()
    distinct = len(set(pairs.values())) == 5
    rep('d=%d U2 ad-Casimir pairs %s pairwise distinct: %s' % (d, pairs, distinct), distinct == (d not in (2, 3)))
    # U3 bracket obstruction
    Om = J(d, 0, 1)
    def SA_(Om, k, side):
        M = np.zeros((N, N), dtype=np.int64); idx = lambda i, j: i * n + j
        for p in range(d):
            for q in range(d):
                if Om[p, q]:
                    if side == 'A':
                        M[idx(p + 1, k + 1), idx(q + 1, 0)] = Om[p, q]; M[idx(q + 1, 0), idx(p + 1, k + 1)] = -Om[p, q]
                    else:
                        M[idx(k + 1, p + 1), idx(0, q + 1)] = Om[p, q]; M[idx(0, q + 1), idx(k + 1, p + 1)] = -Om[p, q]
        return M
    for side in 'AB':
        S1, S2 = SA_(Om, 0, side), SA_(Om, 1, side)
        Cm = S1 @ S2 - S2 @ S1
        w = violates(Cm, vecs)
        rep('d=%d U3 [S(Om(x)f1), S(Om(x)f2)] in Sig_%s violates first order at an exact point' % (d, side), w is not None,
            'witness %s' % (w,))
    if d == 4:
        for sgn in (1, -1):
            Om4 = J(4, 0, 1) + sgn * J(4, 2, 3)
            S1, S2 = SA_(Om4, 0, 'A'), SA_(Om4, 1, 'A')
            rep('d=4 U3 (%s-dual Om) obstruction also holds' % ('self' if sgn > 0 else 'anti-self'),
                violates(S1 @ S2 - S2 @ S1, vecs) is not None)
    rep('d=%d U4 every Z basis element is a nonzero symmetric operator' % d, all(np.array_equal(X, X.T) and np.any(X) for X in pc['Z']))
    # U5 Burnside: the det +1 signed permutation matrices (a subgroup of SO(d)) already span End(R^d) for d >= 3
    mats = []
    for perm in itertools.permutations(range(d)):
        for signs in itertools.product((1, -1), repeat=d):
            Q = np.zeros((d, d), dtype=np.int64)
            for i, j in enumerate(perm): Q[j, i] = signs[i]
            if round(np.linalg.det(Q)) == 1: mats.append(Q.reshape(-1))
    rk = rank_modp(np.array(mats))                  # rank mod p <= rank over Q <= d^2
    rep('d=%d U5 SO(d) elements span %d of %d dims of End(R^d) (rank mod p, a lower bound)' % (d, rk, d * d),
        (rk == d * d) == (d >= 3))
    # U6 normalizer via total Casimir on V
    Ctot = sum(g @ g for g in gA) + sum(g @ g for g in gB)
    e = np.eye(n, dtype=np.int64); uz = np.kron(e[0], e[d]); zz = np.kron(e[d], e[d])
    rep('d=%d U6 total Casimir: u(x)z eigenvalue %d, z(x)z eigenvalue %d' % (d, -(d - 1), -2 * (d - 1)),
        np.array_equal(Ctot @ uz, -(d - 1) * uz) and np.array_equal(Ctot @ zz, -2 * (d - 1) * zz))
    return pc, M, fam

def controls_d3(pc, M):
    X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Zp = sp.diag(1, -1)
    Pl = [sp.eye(2), X, Y, Zp]; b16 = [sp.kronecker_product(a, b) for a in Pl for b in Pl]
    def gen(H):
        G = np.zeros((16, 16), dtype=np.int64)
        for j, Bj in enumerate(b16):
            img = sp.I * (H * Bj - Bj * H)
            for i, Bi in enumerate(b16):
                val = sp.nsimplify((img * Bi).trace() / 4); G[i, j] = int(val)
        return G
    gs = [gen(b) for b in b16[1:]]
    ok = all(not np.any(M @ g.reshape(-1)) for g in gs)
    okb = all(not np.any(M @ (a @ b - b @ a).reshape(-1)) for a in gs for b in gs)
    rep('C d=3: all 15 su(4) generators satisfy the exact sampled constraints', ok)
    rep('C d=3: all 225 brackets of su(4) generators satisfy them (obstruction method does not flag complex QM)', okb)
    H = gs[5]      # X (x) X
    n = 4; A_rows = [i * n + 0 for i in range(1, n)]; AB = [i * n + j for i in range(1, n) for j in range(1, n)]
    B_rows = [0 * n + j for j in range(1, n)]
    rep('C d=3: the X(x)X generator couples both A<->AB and B<->AB (diagonal of Sig_A + Sig_B)',
        np.any(H[np.ix_(AB, A_rows)]) and np.any(H[np.ix_(AB, B_rows)]))

if __name__ == '__main__':
    ds = [int(x) for x in sys.argv[1:]] or [5, 4, 2, 3]
    for d in ds:
        print('=== d = %d ===' % d, flush=True)
        K = {2: 5, 3: 14, 4: 30, 5: 50, 6: 50}[d]
        pc, M, fam = run(d, K)
        if d == 3: controls_d3(pc, M)
    print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
