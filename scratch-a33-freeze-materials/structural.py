"""A33 research, derivation A (structural): isometries in the normal form
   circle r  ->  circle sigma(r),  w -> lam_r * w^eps_r,
solved exactly from the coefficient identities of Re<f_r(w), f_s(w')>:
   RE[sigma r, sigma s][eps_r a, eps_s b] * lam_r^(eps_r a) * lam_s^(eps_s b) = RE[r, s][a, b].
Angles are in turns (lam = exp(2 pi i phi)); every ratio is +-1, so each identity is an integer
congruence  (eps_r a) phi_r + (eps_s b) phi_s = c  (mod 1), c in {0, 1/2}, solved by Smith normal form."""
import itertools
from fractions import Fraction
from circles import RE

N = 9
def inv(r, s):
    return tuple(sorted((abs(a), abs(b), abs(c)) for (a, b), c in RE[r, s].items()))
INV = {(r, s): inv(r, s) for r in range(N) for s in range(N)}

def sigmas():
    out = []
    for sg in itertools.permutations(range(N)):
        if all(INV[sg[r], sg[s]] == INV[r, s] for r in range(N) for s in range(r, N)):
            out.append(sg)
    return out

def equations(sg, ep):
    """rows ([coeffs over 9 unknowns], rhs in turns), or None if a support or magnitude fails."""
    rows = []
    for r in range(N):
        for s in range(r, N):
            A, B = RE[r, s], RE[sg[r], sg[s]]
            img = {(ep[r] * a, ep[s] * b) for (a, b) in A}
            if img != set(B):
                return None
            for (a, b), c in A.items():
                c2 = B[ep[r] * a, ep[s] * b]
                if abs(c2) != abs(c):
                    return None
                row = [0] * N
                row[r] += ep[r] * a
                row[s] += ep[s] * b
                rhs = Fraction(0) if c2 == c else Fraction(1, 2)
                if any(row):
                    rows.append((row, rhs))
                elif rhs:
                    return None
    return rows

def snf(A):
    """Smith normal form over Z: returns (U, D, V) with U A V = D, U and V unimodular."""
    m, n = len(A), len(A[0])
    D = [row[:] for row in A]
    U = [[int(i == j) for j in range(m)] for i in range(m)]
    V = [[int(i == j) for j in range(n)] for i in range(n)]
    def swap_rows(M, i, j): M[i], M[j] = M[j], M[i]
    def swap_cols(M, i, j):
        for row in M: row[i], row[j] = row[j], row[i]
    def add_row(M, src, dst, k):
        M[dst] = [x + k * y for x, y in zip(M[dst], M[src])]
    def add_col(M, src, dst, k):
        for row in M: row[dst] += k * row[src]
    t = 0
    while t < min(m, n):
        piv = [(abs(D[i][j]), i, j) for i in range(t, m) for j in range(t, n) if D[i][j]]
        if not piv: break
        _, i, j = min(piv)
        swap_rows(D, t, i); swap_rows(U, t, i); swap_cols(D, t, j); swap_cols(V, t, j)
        done = False
        while not done:
            done = True
            for i in range(t + 1, m):
                if D[i][t]:
                    q = D[i][t] // D[t][t]; add_row(D, t, i, -q); add_row(U, t, i, -q)
                    if D[i][t]:
                        swap_rows(D, t, i); swap_rows(U, t, i); done = False
            for j in range(t + 1, n):
                if D[t][j]:
                    q = D[t][j] // D[t][t]; add_col(D, t, j, -q); add_col(V, t, j, -q)
                    if D[t][j]:
                        swap_cols(D, t, j); swap_cols(V, t, j); done = False
            if done:
                bad = [(i, j) for i in range(t + 1, m) for j in range(t + 1, n) if D[i][j] % D[t][t]]
                if bad:
                    i, _ = bad[0]; add_row(D, i, t, 1); add_row(U, i, t, 1); done = False
        if D[t][t] < 0:
            D[t] = [-x for x in D[t]]; U[t] = [-x for x in U[t]]
        t += 1
    return U, D, V

def solve(rows):
    """Solutions of A phi = c (mod 1): ('none',) or ('finite', [phi...]) or ('continuous', dim)."""
    rows = sorted(set((tuple(r), c) for r, c in rows))
    A = [list(r) for r, _ in rows]; c = [x for _, x in rows]
    U, D, V = snf(A)
    Uc = [sum(Fraction(u) * x for u, x in zip(row, c)) for row in U]
    d = [D[i][i] if i < len(D) else 0 for i in range(N)]
    for i in range(len(D)):
        di = D[i][i] if i < N else 0
        if di == 0 and Uc[i] % 1:
            return ('none',)
    free = [i for i in range(N) if d[i] == 0]
    if free:
        return ('continuous', len(free))
    sols = []
    for ks in itertools.product(*[range(d[i]) for i in range(N)]):
        psi = [(Uc[i] + ks[i]) / d[i] for i in range(N)]
        phi = tuple(sum(Fraction(V[r][i]) * psi[i] for i in range(N)) % 1 for r in range(N))
        sols.append(phi)
    return ('finite', sorted(set(sols)))

if __name__ == '__main__':
    SG = sigmas()
    print('circle permutations preserving the pair invariants:', len(SG))
    G = []
    cont = 0
    for sg in SG:
        for ep in itertools.product((1, -1), repeat=N):
            rows = equations(sg, ep)
            if rows is None:
                continue
            res = solve(rows)
            if res[0] == 'continuous':
                cont += 1
            elif res[0] == 'finite':
                for phi in res[1]:
                    G.append((sg, ep, phi))
    print('continuous families:', cont)
    print('group elements (sigma, eps, phi):', len(G))
    print('distinct sigma realized:', len({g[0] for g in G}))
    print('angle values used:', sorted({x for g in G for x in g[2]}))
    import pickle; pickle.dump(G, open('G_structural.pkl', 'wb'))
