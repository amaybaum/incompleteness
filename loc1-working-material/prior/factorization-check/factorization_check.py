"""Independent exact check of the SM §2.4 countermodel: the 1-D wave rule
x_i(t+1) = x_{i-1}(t) + x_{i+1}(t) - x_i(t-1) on a ring of N=4 sites over F_3, phase-space form on F_3^8.
Coupling graph of a linear map in coordinates given by an invertible change of basis B (new = B old):
component a of the new update depends on component b iff (B M B^-1)[a][b] != 0 (exact for linear maps)."""
import itertools
q, N = 3, 4
def mat_mul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) % q for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
    n = len(A); M = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] % q)
        M[c], M[p] = M[p], M[c]; iv = pow(M[c][c], q - 2, q)
        M[c] = [x * iv % q for x in M[c]]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c]; M[r] = [(x - f * y) % q for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]
# state (x_0..x_3, p_0..p_3); p = previous x
D = 2 * N
M = [[0]*D for _ in range(D)]
for i in range(N):
    M[i][(i-1) % N] += 1; M[i][(i+1) % N] += 1; M[i][N+i] -= 1   # x_i' = x_{i-1}+x_{i+1}-p_i
    M[N+i][i] = 1                                                # p_i' = x_i
M = [[v % q for v in r] for r in M]
def graph(B):
    T = mat_mul(mat_mul(B, M), inv(B))
    E = {frozenset((a, b)) for a in range(D) for b in range(D) if a != b and T[a][b]}
    deg = [sum(1 for e in E if a in e) for a in range(D)]
    return E, max(deg), T
FAIL = []
def chk(n, ok, d=''):
    print(('PASS ' if ok else 'FAIL ') + n + ('  ' + d if d else '')); ok or FAIL.append(n)
I = [[int(i == j) for j in range(D)] for i in range(D)]
E0, d0, _ = graph(I)
chk('natural factorization: 8 edges, max degree 3', (len(E0), d0) == (8, 3), str((len(E0), d0)))
# hypotheses of the SM theorem on the natural factorization
S = [[int(j == (i + 1) % N) for j in range(N)] for i in range(N)]       # site shift
Sh = [[0]*D for _ in range(D)]
for i in range(N):
    for j in range(N):
        Sh[i][j] = S[i][j]; Sh[N+i][N+j] = S[i][j]
chk('(a) translation invariance: M commutes with the shift', mat_mul(M, Sh) == mat_mul(Sh, M))
chk('(b) range 1: x_i depends only on x_{i±1}, p_i; p_i only on x_i', all((M[i][j] != 0) <= (j in ((i-1) % N, (i+1) % N, N+i)) for i in range(N) for j in range(D)) and all((M[N+i][j] != 0) <= (j == i) for i in range(N) for j in range(D)))
chk('(c) bidirectional: every edge used in both directions', all(M[a][b] != 0 and M[b][a] != 0 for e in E0 for a, b in [tuple(e)]))
# eigenmode change of basis on positions and on previous positions alike
V = [[1, 1, 1, 1], [1, -1, 1, -1], [1, 0, -1, 0], [0, 1, 0, -1]]
A = [[int(j in ((i-1) % N, (i+1) % N)) for j in range(N)] for i in range(N)]
for v in V:
    Av = [sum(A[i][j]*v[j] for j in range(N)) % q for i in range(N)]
    lam = next(((l for l in range(q) if all((Av[i] - l*v[i]) % q == 0 for i in range(N)))), None)
    chk('eigenvector %s of the ring adjacency over F_3' % v, lam is not None, 'lambda=%s' % lam)
P = [[v % q for v in r] for r in V]
Pinv = inv(P)                    # columns of Pinv... use B = P^{-T}? coordinates c = W x with W rows = dual basis
W = [list(r) for r in zip(*inv([list(c) for c in zip(*P)]))]  # rows of W: dual basis so that x = sum c_k v_k
W = inv([list(c) for c in zip(*P)])   # c = (P^T)^{-1} x
B = [[0]*D for _ in range(D)]
for i in range(N):
    for j in range(N):
        B[i][j] = W[i][j]; B[N+i][N+j] = W[i][j]
E1, d1, T1 = graph(B)
chk('eigenmode factorization: 4 edges, max degree 1', (len(E1), d1) == (4, 1), str((len(E1), d1)))
chk('eigenmode factorization differs from the natural one (not a coordinate permutation with scalings)',
    any(sum(1 for x in row if x) != 1 for row in B))
# brute-force control of the eigenmode coupling graph over all 3^8 states (dependence of each new coordinate)
def apply(Mx, s): return tuple(sum(Mx[i][j]*s[j] for j in range(D)) % q for i in range(D))
Bi = inv(B)
def step_new(c):                 # c in new coordinates -> new coordinates of the image
    x = apply(Bi, c); return apply(B, apply(M, x))
dep = set()
for c in itertools.product(range(q), repeat=D):
    out = step_new(c)
    for b in range(D):
        for dv in (1, 2):
            c2 = list(c); c2[b] = (c2[b] + dv) % q
            out2 = step_new(tuple(c2))
            for a in range(D):
                if a != b and out[a] != out2[a]: dep.add(frozenset((a, b)))
chk('brute force over all 6561 states reproduces the eigenmode graph', dep == E1, str(len(dep)))
# A4 clause (b), "no explicit copy of the present value": holds in the spatial coordinates, fails in the eigenmode ones
chk('A4(b) holds in the spatial factorization: x_i\' has no x_i term', all(M[i][i] == 0 for i in range(N)))
selfdep = [a for a in range(N) if T1[a][a] != 0]
chk('A4(b) fails in the eigenmode factorization: c_k\' depends on c_k for lambda_k != 0', len(selfdep) == 2, str(selfdep))
# phi-pullback: the coordinates beta.phi give the same map, hence the same graph, and are a different factorization
Bp = mat_mul(B, M)
E2, d2, T2 = graph(Bp)
chk('pullback of the eigenmode factorization by phi has the same coupling graph', E2 == E1 and T2 == T1)
R = mat_mul(Bp, inv(B))         # change of coordinates from beta to beta.phi
chk('pullback is a distinct factorization (transition is not monomial)', any(sum(1 for x in row if x) != 1 for row in R))
print('controls:', 'OK' if not FAIL else 'FAILED ' + ', '.join(FAIL))
